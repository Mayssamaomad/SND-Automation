SND Automation Toolkit

Automated telecom Service Network Deployment (SND) system built in Python.
This project is designed for telecom operator workflows such as:

Network device automation

NETCONF / RESTCONF configuration

Inventory management

Service provisioning

Bulk configuration pushes

API-based OSS/BSS integrations

🚀 Features

Automated L2/L3 service provisioning

NETCONF-based configuration management

RESTCONF inventory collection

Bulk pushes for mass rollout

Central YAML-configured device inventory

Structured logging

Modular architecture

Ready for CI/CD pipelines

🏗️ Architecture
High Level Diagram
+---------------------+
|     main.py         |
+---------------------+
            |
            v
+---------------------+
|   services/         |
|  (provisioning)     |
+---------------------+
            |
            v
+------------------------------+
|     devices/                 |
|  NETCONF + RESTCONF clients  |
+------------------------------+
            |
            v
+------------------------------+
|  Network Devices / SND API   |
+------------------------------+

Mermaid Diagram (Optional)
flowchart TD
    A[main.py] --> B[Service Provision Layer]
    B --> C[NETCONF Client]
    B --> D[RESTCONF Client]
    C --> E[Routers / Switches]
    D --> E

🛠️ Tech Stack

Python 3.10+

ncclient (NETCONF)

requests (RESTCONF / APIs)

PyYAML

Logging

Telecom YANG models

📦 Installation
git clone https://github.com/yourusername/snd-automation.git
cd snd-automation
pip install -r requirements.txt

🧪 Usage
Provision all services:
python src/main.py

Example output:
Provisioning service SVC001...
Success
Provisioning service SVC002...
Success

🌐 API Endpoints (RESTCONF)
API	Description
/restconf/data/ietf-network:networks	Get network inventory
/restconf/data/ietf-interfaces:interfaces	Interface details
/restconf/data/...	Extend based on platform
📁 Config Examples
configs/devices.yml
router1:
  host: "10.10.10.1"
  username: "admin"
  password: "admin123"

configs/services.yml
- service_id: "SVC001"
  ce: "CE1"
  pe: "PE1"

🤝 Contributing

Fork the repo

Create feature branch

Add tests when possible

Submit Pull Request

📝 Screenshots / Logs
2025-02-01 10:33:12 - INFO - Fetching interface info from 10.10.10.1
2025-02-01 10:33:12 - INFO - Provisioning service SVC001
