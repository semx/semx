<!-- profile README — Sergey Sannikov (semx) · v2 -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,100:1F6FEB&height=200&section=header&text=Sergey%20Sannikov&fontSize=52&fontColor=FFFFFF&fontAlignY=38&desc=Senior%20DevOps%20%C2%B7%20Platform%20%C2%B7%20Site%20Reliability%20Engineer&descAlignY=60&descSize=18" width="100%" alt="Sergey Sannikov — Senior DevOps / Platform / SRE"/>

<a href="https://github.com/semx">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3600&pause=1200&color=58A6FF&center=true&vCenter=true&width=680&lines=10%2B+years+running+production+systems+at+scale;Kubernetes+in+production+since+2022;I+read+source%2C+not+just+docs+%E2%80%94+and+fix+bugs+at+the+root" alt="tagline"/>
</a>

<br/>

<img src="https://img.shields.io/badge/AWS-EKS%20%C2%B7%20IAM%20%C2%B7%20RDS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Kubernetes-Helm%20%C2%B7%20ArgoCD-326CE5?style=flat-square&logo=kubernetes&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Terraform-Terragrunt-7B42BC?style=flat-square&logo=terraform&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Ansible-automation-EE0000?style=flat-square&logo=ansible&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Observability-Prometheus%20%C2%B7%20Grafana%20%C2%B7%20Loki-E6522C?style=flat-square&logo=prometheus&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/DevSecOps-hardening%20%C2%B7%20OPA-2EA043?style=flat-square&logo=opa&logoColor=white&labelColor=0D1117"/>

<br/><br/>

<a href="https://sannikov.dev"><img src="https://img.shields.io/badge/Website-sannikov.dev-1F6FEB?style=for-the-badge&labelColor=0D1117"/></a>
<a href="mailto:sergey@sannikov.dev"><img src="https://img.shields.io/badge/Email-sergey@sannikov.dev-0D1117?style=for-the-badge&logo=maildotru&logoColor=58A6FF"/></a>
<a href="https://t.me/GreySergo"><img src="https://img.shields.io/badge/Telegram-@GreySergo-0D1117?style=for-the-badge&logo=telegram&logoColor=26A5E4"/></a>
<img src="https://img.shields.io/badge/Yerevan,%20Armenia-0D1117?style=for-the-badge&logo=googlemaps&logoColor=EA4335"/>

</div>

---

### About

Senior infrastructure engineer with **10+ years** building and operating production systems at scale — from architecture and IaC through observability, incident response, and mentoring across remote, globally distributed teams. I work the whole delivery path (application code → the pipelines that ship it → the infrastructure it runs on) with a **security-first eye**, and I like finding the sharp edge in a system and fixing it at the root.

- 🛠️ Modernizing legacy workloads into Dockerized services on **Kubernetes / AWS EKS**; Kubernetes in production since **2022**.
- 📈 Track record of **99.95% uptime** SLAs, deployment time cut **45 → 12 min**, and **−30% incident MTTR**.
- 🔎 Read source, not just docs — [Kubernetes `kubelet` security research](https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Asemx) (subPath traversal, authorization bypass, `ImageVolume`, Pod resource consistency).

---

### Core expertise

| | |
| --- | --- |
| **Cloud & Platforms** | AWS (EC2, EKS, RDS, S3, IAM, Route53, CloudFront, CloudWatch, ELB, WAF), Azure, GCP |
| **Containers & GitOps** | Kubernetes, Helm, RBAC, HPA, cert-manager, Docker, ArgoCD, Flux |
| **Infrastructure as Code** | Terraform, Terragrunt, Ansible, Pulumi |
| **CI/CD** | TeamCity, GitLab CI, GitHub Actions, Jenkins |
| **Observability** | Prometheus, Grafana, Loki, OpenTelemetry, Datadog, New Relic, ELK |
| **Security & Identity** | IAM, OPA/Gatekeeper, FreeIPA, Active Directory, VPN, hardening, secrets management |
| **Databases** | PostgreSQL, MySQL, SQL Server, Redis, MongoDB, Neon |
| **Languages** | Bash, Python, Go, HCL, PHP, JavaScript/Node.js |

---

### Open-source contributions

**11 merged pull requests** in upstream projects, plus reports fixed by maintainers upstream. I fix real, reproducible bugs in the tools I run in production — each with a **failing test and a root-cause writeup**. The same class of bug shows up across Go, Python, PHP and JS; reproducing and root-causing it is the transferable skill.

| Project | Contribution | PR | State |
| --- | --- | --- | --- |
| **pallets-eco/croniter** | DOM/DOW union aborted when only the day-of-month half was unsatisfiable | [#243](https://github.com/pallets-eco/croniter/pull/243) | ![](https://img.shields.io/github/issues/detail/state/pallets-eco/croniter/243?style=flat-square&label=) |
| **goreleaser/goreleaser** | `goarm64` validation regex was unanchored and accepted junk values | [#6727](https://github.com/goreleaser/goreleaser/pull/6727) | ![](https://img.shields.io/github/issues/detail/state/goreleaser/goreleaser/6727?style=flat-square&label=) |
| **hashicorp/terraform** | `log()`/`pow()` panicked on NaN results — fixed upstream in 1.17 | [#38888](https://github.com/hashicorp/terraform/issues/38888) | ![](https://img.shields.io/github/issues/detail/state/hashicorp/terraform/38888?style=flat-square&label=) |
| **symfony/symfony** | `Yaml` parsed `.nan` as `+INF` and never round-tripped `NAN` | [#64915](https://github.com/symfony/symfony/pull/64915) | ![](https://img.shields.io/github/issues/detail/state/symfony/symfony/64915?style=flat-square&label=) |
| **symfony/symfony** | ISBN-10 validator accepted a misplaced `X` check character | [#64877](https://github.com/symfony/symfony/pull/64877) | ![](https://img.shields.io/github/issues/detail/state/symfony/symfony/64877?style=flat-square&label=) |
| **symfony/symfony** | `ProxyCacheWarmer` crashed on non-`.php` files in the proxy cache dir | [#64847](https://github.com/symfony/symfony/pull/64847) | ![](https://img.shields.io/github/issues/detail/state/symfony/symfony/64847?style=flat-square&label=) |
| **laravel/framework** | `Number::forHumans()` returned `"-0"` for tiny negatives | [#60736](https://github.com/laravel/framework/pull/60736) | ![](https://img.shields.io/github/issues/detail/state/laravel/framework/60736?style=flat-square&label=) |
| **ansible/ansible** | `is_netmask` accepted non-contiguous (invalid) netmasks | [#87235](https://github.com/ansible/ansible/pull/87235) | ![](https://img.shields.io/github/issues/detail/state/ansible/ansible/87235?style=flat-square&label=) |
| **ansible/ansible** | Uncaught `OverflowError` in `check_type_int` for `inf` | [#87253](https://github.com/ansible/ansible/pull/87253) | ![](https://img.shields.io/github/issues/detail/state/ansible/ansible/87253?style=flat-square&label=) |
| **argoproj/argo-cd** | Surface the `Suspended` condition message for suspended Jobs | [#28738](https://github.com/argoproj/argo-cd/pull/28738) | ![](https://img.shields.io/github/issues/detail/state/argoproj/argo-cd/28738?style=flat-square&label=) |
| **spinnaker/spinnaker** | `libdiffs` mis-ordered versions with differing component counts | [#7805](https://github.com/spinnaker/spinnaker/pull/7805) | ![](https://img.shields.io/github/issues/detail/state/spinnaker/spinnaker/7805?style=flat-square&label=) |
| **spinnaker/spinnaker** | Packer `-var` values `false` / `0` were silently dropped | [#7806](https://github.com/spinnaker/spinnaker/pull/7806) | ![](https://img.shields.io/github/issues/detail/state/spinnaker/spinnaker/7806?style=flat-square&label=) |
| **nodejs/node** | `assert.deepStrictEqual` `TypeError` on a null `Map` key / `Set` member | [#64449](https://github.com/nodejs/node/pull/64449) | ![](https://img.shields.io/github/issues/detail/state/nodejs/node/64449?style=flat-square&label=) |
| **kubernetes/kubernetes** | `Quantity.String()` dropped the suffix for DecimalSI above 10¹⁸ | [#140459](https://github.com/kubernetes/kubernetes/pull/140459) | ![](https://img.shields.io/github/issues/detail/state/kubernetes/kubernetes/140459?style=flat-square&label=) |
| **kubernetes/kubernetes** | Label `Gt`/`Lt` selectors silently dropped values above int64 | [#140462](https://github.com/kubernetes/kubernetes/pull/140462) | ![](https://img.shields.io/github/issues/detail/state/kubernetes/kubernetes/140462?style=flat-square&label=) |
| **python-humanize/humanize** | `fractional()` emitted degenerate output (`"2 1/1"`) on whole-rounding | [#354](https://github.com/python-humanize/humanize/pull/354) | ![](https://img.shields.io/github/issues/detail/state/python-humanize/humanize/354?style=flat-square&label=) |
| **argoproj/argo-rollouts** | `int32` overflow produced negative canary replica counts | [#4923](https://github.com/argoproj/argo-rollouts/pull/4923) | ![](https://img.shields.io/github/issues/detail/state/argoproj/argo-rollouts/4923?style=flat-square&label=) |
| **go-task/task** | Templated `dir:` left dynamic `sh:` vars running in the wrong directory | [#2944](https://github.com/go-task/task/pull/2944) | ![](https://img.shields.io/github/issues/detail/state/go-task/task/2944?style=flat-square&label=) |

<sub>Selected — more across Kubernetes, Ansible, argo-workflows, act, actionlint, docker-py.</sub>

---

### Projects

- **[ansible-linter](https://github.com/semx/ansible-linter)** — dependency-light static analysis for Ansible playbooks.
- **[mr-rca-toolkit](https://github.com/semx/mr-rca-toolkit)** — infrastructure merge review and incident RCA utilities.
- **[claude-arena](https://github.com/semx/claude-arena)** — cost-aware model routing and orchestration for dev tooling.

---

<div align="center">


<br/><br/>

**Open to Senior DevOps / Platform / DevSecOps / SRE roles** — best reached via [sannikov.dev](https://sannikov.dev)

</div>
