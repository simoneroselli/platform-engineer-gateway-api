# Project: Wordsmith Platform Engineering Lab

Welcome to the Platform Engineer Gateway API laboratory project! This repository is designed to explore and master modern Kubernetes platform engineering practices. Instead of focusing on basic single-application deployments, this lab dives into the complexities of running dynamic, multi-environment microservice architectures using an industry-standard cloud-native stack.

## 🏛️ Core Learning Objectives & Pillars
This project is structured around five foundational pillars of modern Kubernetes operations:

### 1. GitOps Orchestration with ArgoCD

* Implements automated, scalable resource management using the App-of-Apps pattern and ApplicationSets.

* Manages directory-based environment segregation (dev vs prod).

### 2. Helm Chart Engineering

* Transitions from static configuration files to a reusable "Package Once, Configure Many" model.

* Utilizes advanced template rendering, helper functions, and environment-specific value injection (values.yaml).

### 3. Modern Traffic Management (Gateway API)

* Evolves away from legacy Ingress controllers toward the native Kubernetes Gateway API (GatewayClass, Gateway, and HTTPRoute).

* Handles north/south traffic routing for out-of-the-box container services like the Wordsmith Stack.

### 4. Service Mesh & Security with Istio

* Manages cluster-level control planes (istiod) and foundational CRDs via ArgoCD sync-waves.

* Enforces Strict mTLS (Mutual TLS) encryption across internal service-to-service communications (web <-> api <-> db) transparently using Envoy sidecar proxies.

### 5. Custom Kubernetes Operators (Python / Kopf)

* Extends the Kubernetes API by designing Custom Resource Definitions (CRDs).

* Implements custom reconciliation loops using Python-based operators via the Kopf framework to automate domain-specific operations.

## 🏗️ Sample Application (The Wordsmith Stack)
To test these platform principles, the lab deploys the Wordsmith demo application, which features a clean, decoupled microservices layout:

* Frontend (web - Go): Renders the user interface.
* Backend (api - Python/Node): Handles core application logic.
* Database (db - Redis/Postgres): Stores state and persistent data.

## 📂 Repository Structure
```text
.
├── infra-root.yaml             # Core infrastructure root application (ArgoCD)
├── platform-root.yaml          # Workloads root application / ApplicationSet
└── platform-workloads
    ├── charts
    │   └── wordsmith           # Centralized Helm chart for the Wordsmith stack
    ├── environments
    │   ├── dev                 # Dev environment overrides & values
    │   └── prod                # Prod environment overrides & values
    ├── infrastructure
    │   ├── argocd.yaml         # ArgoCD configurations
    │   ├── gateways            # Gateway API definitions (GatewayClass, Gateway)
    │   └── istio-system        # Istio Base CRDs & Istiod Control Plane (Sync Waves)
    └── operators
        └── wordsmith-ops       # Custom Python/Kopf operator extension
```

## 🚀 Getting Started & Local Testing
1. Spin up a local cluster (e.g., using k3d):
```bash
k3d cluster create platform-lab --api-port 6443 -p "80:80@loadbalancer" -p "443:443@loadbalancer"
```
2. Bootstrap ArgoCD & Infrastructure:
Apply your root infrastructure manifests to spin up the control planes, custom operators, gateways, and Istio mesh infrastructure.

3. Validate the Mesh Layer:
Check that your sidecar proxies are active and enforcing strict mTLS security:
```bash
istioctl proxy-status
istioctl x describe pod <your-web-pod-name> -n wordsmith-prod-app
```

