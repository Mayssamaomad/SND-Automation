# SND Automation Toolkit

A Python-based automation framework for telecom Service Network Deployment (SND).  
Designed for automating network device configuration, service provisioning, inventory management, and bulk configuration workflows using NETCONF/RESTCONF and API integration.

---

## 🚀 Features

- Automated service provisioning (L2/L3 services)
- NETCONF-based device configuration
- RESTCONF/HTTP API integration
- Inventory management
- Bulk configuration push
- Central YAML-configured device inventory
- Structured logging
- Modular, scalable architecture

---

## 🏗️ Architecture

### High-level flow:

+---------------------+
| main.py |
+---------------------+
|
v
+---------------------+
| services/ |
| (provision/deactivate) |
+---------------------+
|
v
+-----------------------------+
| devices/ |
| (NETCONF + RESTCONF clients)|
+-----------------------------+
|
v
+-----------------------------+
| Network Devices / SND APIs |
+-----------------------------+

### Mermaid Diagram:

```mermaid
flowchart TD
    A[main.py] --> B[Service Provision Layer]
    B --> C[NETCONF Client]
    B --> D[RESTCONF Client]
    C --> E[Routers/Switches]
    D --> E
