#!/usr/bin/env python3
"""Regenerate the open-source contributions matrix in README.md from the GitHub search API.

Counts merged pull requests authored by USER in repositories USER does not own, groups them by
repository, and writes a summary line plus a table sorted by repository stars between the
<!-- contributions:start --> and <!-- contributions:end --> markers. Standard library only.
Needs GITHUB_TOKEN (any token; the default Actions token is enough for public search).
"""
import json, os, re, sys, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone

USER = os.environ.get("PROFILE_USER", "semx")
README = os.environ.get("README_PATH", "README.md")
MIN_STARS = int(os.environ.get("MIN_STARS", "1000"))
# repositories that are not code contributions (membership requests etc.)
EXCLUDE = set(filter(None, os.environ.get("EXCLUDE_REPOS", "kubernetes/org").split(",")))
# always shown at the top of the table, with an optional role: "owner/repo=role,owner/repo"
PINNED = dict((x.split("=", 1) + [""])[:2] for x in filter(None, os.environ.get(
    "PINNED_REPOS", "bb-Ricardo/netbox-sync=maintainer,ccremer/kubernetes-zfs-provisioner").split(",")))
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

def api(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-profile",
                                               **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def merged_prs():
    q = urllib.parse.quote(f"is:pr is:merged author:{USER} -user:{USER}")
    items, page = [], 1
    while True:
        d = api(f"https://api.github.com/search/issues?q={q}&per_page=100&page={page}")
        items += d["items"]
        if len(items) >= d["total_count"] or not d["items"] or page >= 10:
            return items
        page += 1

def short(n):
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)

def main():
    prs = merged_prs()
    counts = Counter(p["repository_url"].split("/repos/")[1] for p in prs)
    for r in EXCLUDE:
        counts.pop(r, None)
    repos = []
    for name, n in counts.items():
        info = api(f"https://api.github.com/repos/{name}")
        repos.append({"name": name, "merged": n, "stars": info["stargazers_count"], "lang": info.get("language") or "",
                      "avatar": info["owner"]["avatar_url"], "desc": (info.get("description") or "").strip()})
    repos.sort(key=lambda r: (-r["stars"], -r["merged"], r["name"].lower()))
    pinned = [r for name in PINNED for r in repos if r["name"] == name]
    big = pinned + [r for r in repos if r["stars"] >= MIN_STARS and r["name"] not in PINNED]
    small = [r for r in repos if r["stars"] < MIN_STARS and r["name"] not in PINNED]
    total = sum(counts.values())
    stars = sum(r["stars"] for r in repos)
    search = "https://github.com/search?type=pullrequests&q=" + urllib.parse.quote(f"is:pr is:merged author:{USER} -user:{USER}")
    out = []
    out.append(f'<a href="{search}"><img src="https://img.shields.io/badge/merged_PRs-{total}-2EA043?style=flat-square&labelColor=0D1117"/></a> '
               f'<img src="https://img.shields.io/badge/projects-{len(repos)}-1F6FEB?style=flat-square&labelColor=0D1117"/> '
               f'<img src="https://img.shields.io/badge/upstream_stars-{short(stars)}-E3B341?style=flat-square&labelColor=0D1117"/>')
    out.append("")
    out.append("| | Project | ★ | Language | Merged |")
    out.append("| :-: | --- | --: | --- | --: |")
    for r in big:
        link = "https://github.com/search?type=pullrequests&q=" + urllib.parse.quote(f"is:pr is:merged author:{USER} repo:{r['name']}")
        role = f" · <sub>{PINNED[r['name']]}</sub>" if PINNED.get(r["name"]) else ""
        out.append(f'| <img src="{r["avatar"]}&s=40" width="20" height="20"/> | [{r["name"]}](https://github.com/{r["name"]}){role} '
                   f'| {short(r["stars"])} | {r["lang"]} | [{r["merged"]}]({link}) |')
    if small:
        rest = " · ".join(f'[{r["name"]}](https://github.com/{r["name"]}) {r["merged"]}' for r in sorted(small, key=lambda r: -r["merged"]))
        out.append("")
        out.append(f"Smaller projects: {rest}")
    out.append("")
    out.append(f"<sub>Merged pull requests to repositories I don't own, from the GitHub search API; "
               f"refreshed weekly by <code>.github/workflows/contributions.yml</code>, last run {datetime.now(timezone.utc):%Y-%m-%d}.</sub>")
    block = "\n".join(out)
    text = open(README, encoding="utf-8").read()
    pattern = re.compile(r"<!-- contributions:start -->.*?<!-- contributions:end -->", re.S)
    if not pattern.search(text):
        sys.exit("contributions markers not found in README")
    new = pattern.sub(lambda m: "<!-- contributions:start -->\n" + block + "\n<!-- contributions:end -->", text, count=1)
    open(README, "w", encoding="utf-8").write(new)
    print(f"{total} merged PRs, {len(repos)} projects, {short(stars)} stars in projects >= {MIN_STARS}")

if __name__ == "__main__":
    main()
