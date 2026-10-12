### Sergey Sannikov

Senior DevOps / Platform engineer, 10+ years running production infrastructure: AWS and on-prem, Kubernetes, CI/CD, observability, incident response. I work across the whole delivery path, from the application code through the pipelines that ship it to the infrastructure it runs on, and I treat security as part of the job rather than a separate stage.

Member of the [kubernetes-sigs](https://github.com/kubernetes-sigs) and [etcd-io](https://github.com/etcd-io) GitHub organizations. Maintainer of [netbox-sync](https://github.com/bb-Ricardo/netbox-sync).

**Contact:** [sannikov.dev](https://sannikov.dev) · [sergey@sannikov.dev](mailto:sergey@sannikov.dev) · Georgia (UTC+4), remote

---

#### What I work on

- **Platform:** AWS (EKS, IAM, RDS, Route 53, CloudFront), Kubernetes, Helm, Argo CD, Flux, Docker, Proxmox
- **Delivery and IaC:** Terraform, Terragrunt, Ansible, GitHub Actions, GitLab CI, TeamCity, Jenkins
- **Observability and security:** Prometheus, Grafana, Loki, OpenTelemetry, OPA/Gatekeeper, Vault, FreeIPA
- **Languages:** Go, Python, Bash, PHP; PostgreSQL, MySQL, Redis

---

#### Open source

I fix bugs in the tools I run in production. Each change starts from a reproduction, ships with a regression test, and explains the root cause in the pull request.

**79 merged pull requests in 26 upstream projects** ([live list](https://github.com/search?q=is%3Apr+author%3Asemx+is%3Amerged+-user%3Asemx&type=pullrequests)). Selected work:

- **Kubernetes** — four changes in `kubernetes/kubernetes`, including skipping unchanged pod resources on in-place resize in the LimitRanger admission plugin ([#142171](https://github.com/kubernetes/kubernetes/pull/142171)) and `resource.Quantity` correctness fixes ([#140459](https://github.com/kubernetes/kubernetes/pull/140459), [#141169](https://github.com/kubernetes/kubernetes/pull/141169)); a Cluster API controller fix ([kubernetes-sigs/cluster-api#14303](https://github.com/kubernetes-sigs/cluster-api/pull/14303)); removed the reachable CVEs from `autoscaler/addon-resizer`, fixed `go vet` and added its first CI workflow ([#10112](https://github.com/kubernetes/autoscaler/pull/10112)–[#10114](https://github.com/kubernetes/autoscaler/pull/10114)).
- **netbox-sync** (VMware vCenter and Redfish to NetBox) — maintainer; 34 merged pull requests and the v1.9.1 release, plus review of incoming contributions against a vcsim test bench built from real vCenter captures.
- **Symfony** — security hardening of the weak-secret guard in `Uuid47Transformer`, released in [v8.1.4](https://github.com/symfony/symfony/releases/tag/v8.1.4) ([#65105](https://github.com/symfony/symfony/pull/65105)); five merged fixes in total.
- **kubernetes-zfs-provisioner** — with the maintainer: leader election on coordination Leases, a native Go SSH runner in place of shell wrappers, in-process volume expansion.
- **Argo** — a `ParseProgress` panic in Workflows with release-branch backports ([#16537](https://github.com/argoproj/argo-workflows/pull/16537)), the `Suspended` condition for suspended Jobs in Argo CD ([#28738](https://github.com/argoproj/argo-cd/pull/28738)), input validation in Argo Rollouts ([#4924](https://github.com/argoproj/argo-rollouts/pull/4924)).
- **Supply chain and release tooling** — case-insensitive checksum comparison in `cosign` ([#5036](https://github.com/sigstore/cosign/pull/5036)), anchored `goarm64` validation in goreleaser ([#6727](https://github.com/goreleaser/goreleaser/pull/6727)), single-character repository paths in go-containerregistry ([#2407](https://github.com/google/go-containerregistry/pull/2407)).
- Also: Node.js `assert` ([#64449](https://github.com/nodejs/node/pull/64449)), Ansible, Laravel, Spinnaker, mydumper, iTerm2 and its nushell shell integration.

<sub>Counts as of October 2026.</sub>

---

#### Own projects

- **[helmtide](https://github.com/semx/helmtide)** — maintained fork of helmwave on Helm v4: current dependencies, no known reachable CVEs with available fixes, hermetic tests and a kind-based integration suite.
- **[ansible-secops-linter](https://github.com/semx/ansible-secops-linter)** — static checks for Ansible: hardcoded secrets, disabled TLS and host-key verification, missing `no_log`, world-writable modes.
- **[mr-rca-toolkit](https://github.com/semx/mr-rca-toolkit)** — utilities for infrastructure merge review and incident root-cause analysis.
