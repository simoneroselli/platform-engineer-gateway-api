# Project: Wordsmith Platform Engineering Lab

## Overview
This repository serves as an academic laboratory designed to explore modern Kubernetes platform engineering practices. The goal of this project is to move beyond basic application deployment and master the complexities of managing dynamic, multi-environment microservice architectures.

The primary subject of this lab is the **Wordsmith** demo application—a multi-tier stack comprising a Go frontend, Java API backend, and PostgreSQL database.

## Core Learning Objectives
This project focuses on three fundamental pillars of modern Kubernetes operations:

1. **GitOps Orchestration with ArgoCD:** - Implementing `ApplicationSet` for automated, scalable resource management.
   - Achieving directory-based environment segregation (`dev` vs `prod`).

2. **Helm Chart Engineering:**
   - Transitioning from static manifests to a "Package Once, Configure Many" model.
   - Mastering template rendering and value injection to handle cross-namespace DNS resolution and environment-specific configurations.

3. **Modern Traffic Management:**
   - Evolving from traditional Nginx Ingress controllers toward the **Kubernetes Gateway API**.
   - Learning how to handle routing, traffic splitting, and infrastructure-level abstraction.

## Architecture
The application follows a clean, decoupled microservices architecture:
- **Web (Go):** Frontend rendering and API orchestration.
- **API (Java):** Logic tier responsible for data retrieval.
- **Database (PostgreSQL):** Persistence layer.

## Key Technical Achievements
- **Dynamic DNS Resolution:** Overcame internal service discovery challenges by parameterizing FQDNs for cross-namespace communication.
- **Infrastructure Automation:** Automated the reconciliation of application lifecycles using ArgoCD.
- **Operator Exploration:** (Ongoing) Experimentation with Python-based operators via the [Kopf](https://kopf.readthedocs.io/) framework to extend Kubernetes API functionality and handle custom reconciliation loops.

## Repository Structure
```text
.
└── platform-workloads/ # ArgoCD ApplicationSet and Gateway API manifests
   ├──charts/             # Centralized Helm chart for the application
   ├── environments/       # Environment-specific values.yaml (dev, prod)
   ├── operators/          # Custom operator logic (Python/Kopf)