<!-- profile README — Sergey Sannikov (semx) · v2 -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,100:1F6FEB&height=200&section=header&text=Sergey%20Sannikov&fontSize=52&fontColor=FFFFFF&fontAlignY=38&desc=Senior%20DevOps%20%C2%B7%20Platform%20%C2%B7%20Site%20Reliability%20Engineer&descAlignY=60&descSize=18" width="100%" alt="Sergey Sannikov — Senior DevOps / Platform / SRE"/>

<img src="https://img.shields.io/badge/AWS-EKS%20%C2%B7%20IAM%20%C2%B7%20RDS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Kubernetes-Helm%20%C2%B7%20ArgoCD-326CE5?style=flat-square&logo=kubernetes&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Terraform-Terragrunt-7B42BC?style=flat-square&logo=terraform&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Ansible-automation-EE0000?style=flat-square&logo=ansible&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/Observability-Prometheus%20%C2%B7%20Grafana%20%C2%B7%20Loki-E6522C?style=flat-square&logo=prometheus&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/DevSecOps-hardening%20%C2%B7%20OPA-2EA043?style=flat-square&logo=opa&logoColor=white&labelColor=0D1117"/>

<br/><br/>

<a href="https://sannikov.dev"><img src="https://img.shields.io/badge/Website-sannikov.dev-1F6FEB?style=for-the-badge&labelColor=0D1117"/></a>
<a href="mailto:sergey@sannikov.dev"><img src="https://img.shields.io/badge/Email-sergey@sannikov.dev-0D1117?style=for-the-badge&logo=maildotru&logoColor=58A6FF"/></a>
<a href="https://t.me/sannikovdev"><img src="https://img.shields.io/badge/Telegram-@sannikovdev-0D1117?style=for-the-badge&logo=telegram&logoColor=26A5E4"/></a>
<img src="https://img.shields.io/badge/Georgia-0D1117?style=for-the-badge&logo=googlemaps&logoColor=EA4335"/>

</div>

---

### About

Senior infrastructure engineer with **10+ years** building and operating production systems at scale — from architecture and IaC through observability, incident response, and mentoring across remote, globally distributed teams. I work the whole delivery path (application code → the pipelines that ship it → the infrastructure it runs on) with a **security-first eye**, and I like finding the sharp edge in a system and fixing it at the root.

- Modernizing legacy workloads into Dockerized services on **Kubernetes / AWS EKS**; Kubernetes in production since **2022**.
- Read source, not just docs — [Kubernetes `kubelet` security research](https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Asemx) (subPath traversal, authorization bypass, `ImageVolume`, Pod resource consistency).
- **Currently:** modernizing [`kubernetes-zfs-provisioner`](https://github.com/ccremer/kubernetes-zfs-provisioner) together with its maintainer, and hunting reproducible bugs across CI/CD toolchains.

---

### Core expertise

| | |
| --- | --- |
| **Platform** | AWS (EKS, IAM, RDS, Route53, CloudFront), Kubernetes, Helm, ArgoCD, Flux, Docker |
| **Delivery & IaC** | Terraform, Terragrunt, Ansible, GitHub Actions, GitLab CI, TeamCity, Jenkins |
| **Observability & Security** | Prometheus, Grafana, Loki, OpenTelemetry, OPA/Gatekeeper, FreeIPA, secrets management |
| **Languages & Data** | Go, Python, Bash, PHP, HCL, PostgreSQL, MySQL, Redis |

---

### Open source

I fix real, reproducible bugs in the tools I run in production. Every patch starts from a failing reproduction and lands with a regression test and a root-cause writeup; the bug classes repeat across ecosystems, so the method carries across Go, PHP, Python and JS.

**29 merged upstream pull requests across 14 projects** — Kubernetes autoscaler, Argo Workflows & Argo CD, Symfony, Ansible, Spinnaker, goreleaser, Laravel, sigstore/cosign, PHP-CS-Fixer, iTerm2 and others → [all merged PRs](https://github.com/search?q=is%3Apr+author%3Asemx+is%3Amerged+-user%3Asemx&type=pullrequests)

- **Security fix released in Symfony v8.1.4** — hardened the weak-secret guard in `Uuid47Transformer` for secrets longer than 16 bytes ([#65105](https://github.com/symfony/symfony/pull/65105), [release notes](https://github.com/symfony/symfony/releases/tag/v8.1.4)), one of four merged Symfony fixes
- **Kubernetes `autoscaler/addon-resizer`** — eliminated its reachable CVEs, fixed `go vet`, and gave the subproject its first CI workflow ([#10112](https://github.com/kubernetes/autoscaler/pull/10112)-[#10114](https://github.com/kubernetes/autoscaler/pull/10114))
- **`kubernetes-zfs-provisioner`** — modernizing it together with the maintainer: leader election moved to coordination Leases, the SSH shell wrappers replaced with a native Go SSH runner, and provisioning made production-safe with in-process volume expansion (5 merged PRs and counting)
- **Argo** — fixed a `ParseProgress` panic in Workflows including the release-branch backports ([#16537](https://github.com/argoproj/argo-workflows/pull/16537)), and surfaced the `Suspended` condition for suspended Jobs in Argo CD ([#28738](https://github.com/argoproj/argo-cd/pull/28738))
- **Supply chain / release tooling** — checksum validation of the TUF root of trust in `cosign initialize` rejected valid uppercase digests ([#5036](https://github.com/sigstore/cosign/pull/5036)); unanchored `goarm64` validation in goreleaser ([#6727](https://github.com/goreleaser/goreleaser/pull/6727))

<sub>Numbers as of August 2026; the search link above is live.</sub>

---

### Projects

- **[helmtide](https://github.com/semx/helmtide)** — a maintained fork of helmwave: helm3-native release management with current dependencies and tests that don't need a live cluster.
- **[ansible-secops-linter](https://github.com/semx/ansible-secops-linter)** — security-focused static analysis for Ansible: hardcoded secrets, disabled TLS/host-key checks, missing `no_log`, world-writable modes.
- **[mr-rca-toolkit](https://github.com/semx/mr-rca-toolkit)** — infrastructure merge review and incident RCA utilities.

---

<div align="center">

Best reached via [sannikov.dev](https://sannikov.dev)

</div>
