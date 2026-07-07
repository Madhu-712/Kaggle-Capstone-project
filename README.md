

# 🚀 EnterpriseOps-Agent

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Google ADK](https://img.shields.io/badge/Google-ADK-red)
![GEAP](https://img.shields.io/badge/GEAP-Multi--Agent-green)
![Gemini](https://img.shields.io/badge/Gemini-3.5_Flash-blueviolet)
![BigQuery](https://img.shields.io/badge/BigQuery-MCP-orange)
![Agent Runtime](https://img.shields.io/badge/Deployment-Agent_Runtime-success)
![NVIDIA](https://img.shields.io/badge/NVIDIA-GPU_Accelerated-76B900?style=for-the-badge&logo=nvidia)
</p>
<p align="center">

### 🧠 Enterprise Decision Intelligence powered by a Multi-Agent System

*Automating Enterprise Operations, Executive Decision-Making, and Business Insights using Google Agent Development Kit (GEAP).*

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/c882cda7-ad84-4d74-863f-8f5037442564" />
---

# 📌 Project Overview

EnterpriseOps-Agent is an **AI-powered Enterprise Decision Intelligence Platform** that transforms enterprise data into executive-ready insights through a **Multi-Agent System (MAS)**.

Unlike traditional chatbots that answer questions in isolation, EnterpriseOps-Agent functions as a **digital Chief Operating Officer**, coordinating multiple specialized AI agents that collaborate to analyze finance, operations, customers, risks, and strategic actions.

The system is built using the **Google Agent Development Kit (ADK)** through **GEAP (Google Enterprise Agent Platform)** and leverages **Gemini 3.5 Flash** as its reasoning engine.

Enterprise data is securely stored in **Google BigQuery**, while **BigQuery MCP** enables tool-based SQL execution by the agents.

The application is deployed using **Google Agent Runtime**, which runs on **NVIDIA GPU-backed Google Cloud infrastructure** to provide scalable and responsive agent execution.
**Google Agent Runtime** powered by high-performance **NVIDIA GPU**-backed infrastructure (such as H100 or Blackwell chips). By utilizing **NVIDIA Multi-Instance GPU (MIG)**, GEAP splits a single physical GPU into up to seven isolated hardware instances, ensuring that your agent's core reasoning loops, tool-calling execution, and safety filters run simultaneously on dedicated fractional GPU slices with absolute hardware-level isolation, zero resource contention, and guaranteed sub-second response times without instances interfearing with one another.

By adopting sophasticated **NVIDIA tech stack** GCP's **Vertex AI Engine**  is  eliminating latency, improving throughput , overall performance , CPU and Memory allocation in few milli seconds.

---

# 🎯 Problem Statement

Modern enterprises generate enormous volumes of operational data across departments such as finance, customer support, operations, and procurement.

However, business leaders still spend significant time:

- Gathering reports manually
- Switching between dashboards
- Correlating information from multiple systems
- Making decisions based on incomplete insights

Traditional BI dashboards only visualize data—they do not reason over it.

Similarly, conventional AI chatbots answer isolated questions but cannot autonomously coordinate across multiple business domains.

# 💡That's Why EnterpriseOps-Agent?
Unlike traditional AI assistants, EnterpriseOps-Agent combines autonomous reasoning with domain-specific specialists.

Instead of relying on a single LLM, an EnterpriseOps Orchestrator Agent coordinates five specialized agents.

This collaborative architecture enables:

Better reasoning and Understanding enterprise-wide business context
Task delegation to  specialized AI agents
Cross-functional insights(across departments)
Executive decision support and recommendations
Higher transparency
making the system behave more like an enterprise leadership team than a chatbot.


# 🌟 Key Features

- 🤖 Multi-Agent System (MAS)
- 🧠 EnterpriseOps Orchestrator Agent
- 💰 Finance Agent
- ⚙️ Operations Agent
- 👥 Customer Agent
- 🛡️ Risk Agent
- 📋 Action Agent
- 📊 BigQuery MCP Integration
- 🗃️ Structured Enterprise Data
- 📚 Enterprise Knowledge Base
- 📈 Executive Decision Support
- 🚀 Google Agent Runtime Deployment
- 🔐 Secure Tool-based SQL Execution
---

# 🚀 Live Demo

### Google Agent Runtime Playground

> Requires authenticated Google Cloud access.

https://console.cloud.google.com/agent-platform/runtimes/locations/us-central1/agent-engines/4736043532307922944/playground

### deployed on aistudio
https://enterpriseops-decision-intelligence-console-881601845310.asia-southeast1.run.app/

---

# 📸 Application Screenshots

> Replace these placeholders after uploading screenshots.

## Dashboard
<img width="1470" height="1026" alt="enterpriseops dashboard-1" src="https://github.com/user-attachments/assets/cf359f93-84e0-4548-9dd2-03826b25bc1c" />


---

## Multi-Agent Workflow

<img width="1470" height="1029" alt="MultiAgent Workflow" src="https://github.com/user-attachments/assets/54d9cbb7-ec1f-4a86-8b1c-6154ac2f5024" />


---

## Executive Summary

<img width="1470" height="1033" alt="Executive summary" src="https://github.com/user-attachments/assets/10b2049b-be19-4c2b-bcef-e3e055d0ac84" />


---

## Google Agent Runtime

<img width="1470" height="1033" alt="GoogleAgentRuntime" src="https://github.com/user-attachments/assets/22c88295-9dca-4259-9f3b-fae6539b87f7" />


---

# 👥 User Personas

| Persona | Responsibilities |
|----------|------------------|
| COO | Enterprise-wide operational monitoring |
| CFO | Revenue, budgeting, expenditure analysis |
| Operations Manager | Workforce utilization & project tracking |
| Customer Success Manager | Customer health & support insights |
| Risk & Compliance Officer | Enterprise risk assessment |

---

# 🏗️ System Architecture

```text
                           User Query
                                │
                                ▼
                EnterpriseOps Orchestrator Agent
                          (Root Agent)
                                │
      ┌──────────────┬──────────┼──────────┬──────────────┐
      ▼              ▼          ▼          ▼              ▼
 Finance Agent  Operations  Customer   Risk Agent   Action Agent
                   Agent      Agent
      │              │          │          │              │
      └──────────────┴──────────┴──────────┴──────────────┘
                                │
                                ▼
                     BigQuery MCP Server
                                │
                                ▼
                    Google BigQuery Dataset
                 (9 Structured Tables + Knowledge Base)
                                │
                                ▼
                     Google Agent Runtime
                                │
                                ▼
      NVIDIA GPU-backed Google Cloud Infrastructure
```

---

# 🧩 EnterpriseOps Framework

```text
User Query
      │
      ▼
EnterpriseOps Orchestrator
      │
      ▼
Task Planning
      │
      ▼
Agent Delegation
      │
      ▼
BigQuery MCP Tool Calls
      │
      ▼
Enterprise Data Retrieval
      │
      ▼
Multi-Agent Collaboration
      │
      ▼
Executive Summary
      │
      ▼
Action Plan
```
# 📂 Dataset Overview

EnterpriseOps-Agent uses a combination of structured enterprise datasets and an enterprise knowledge base stored in **Google BigQuery**.

## Structured Datasets

| Dataset | Description |
|----------|-------------|
| departments | Department master information |
| employees | Employee details and utilization metrics |
| projects | Active projects, status and risk scores |
| project_resources | Employee allocation across projects |
| revenue_metrics | Regional revenue and target metrics |
| budget_metrics | Department budgets and actual expenditure |
| customer_health | Customer health scores, NPS and churn risk |
| support_tickets | Customer support ticket analytics |
| vendors | Vendor information, contract expiry and risk |

## Enterprise Knowledge Base 

| Dataset | Description |
|----------|-------------|
| knowledge_base | Enterprise policies, SOPs, governance guidelines and operational documentation |

---

# 🏗 Data Layer

EnterpriseOps-Agent uses **Google BigQuery** as the centralized enterprise data warehouse.

Instead of allowing agents to directly access databases, the application securely interacts with BigQuery through the **BigQuery MCP Server**, enabling tool-based SQL execution.

### Data Flow

```
CSV Files
     │
     ▼
upload_csv_bq.py
     │
     ▼
Google BigQuery
     │
     ▼
BigQuery MCP Server
     │
     ▼
EnterpriseOps Agents
```

---

# 📊 Data Ingestion

Structured datasets are uploaded into BigQuery using the provided ingestion script.

```
upload_csv_bq.py
```

The script automatically:

- Reads all CSV files
- Creates tables (if required)
- Uploads data into the **enterprise_ops** dataset
- Validates successful ingestion

This allows rapid setup without manual table creation.

---

# 🤖 Multi-Agent Architecture

EnterpriseOps-Agent follows a **Hierarchical Multi-Agent System (MAS)** architecture.

Why MAS instead of Single Agent?

### Traditional Chatbot

   User
     │
     ▼
 Single LLM
     │
     ▼
   Answer
     


### EnterpriseOps-Agent

User
 │
 ▼
EnterpriseOps Orchestrator
 │
 ├── Finance
 ├── Operations
 ├── Customer
 ├── Risk
 └── Action
 │
 ▼
 Executive Report

## EnterpriseOps Orchestrator

Acts as the central decision maker.

Responsibilities:

- Understand user intent
- Plan execution
- Delegate work to specialist agents
- Collect insights
- Generate executive reports

---

## Finance Agent

Responsible for:

- Budget analysis
- Revenue performance
- Financial variance
- Spending trends
- Financial recommendations

Primary Tables:

- revenue_metrics
- budget_metrics

---

## Operations Agent

Responsible for:

- Project monitoring
- Workforce utilization
- Resource allocation
- Delivery bottlenecks
- Operational efficiency

Primary Tables:

- projects
- employees
- project_resources

---

## Customer Agent

Responsible for:

- Customer health
- Churn prediction
- NPS monitoring
- Support performance
- Customer satisfaction

Primary Tables:

- customer_health
- support_tickets

---

## Risk Agent

Responsible for:

- Vendor risk
- Project risk
- Compliance
- Governance
- Enterprise policies

Primary Tables:

- vendors
- projects
- knowledge_base

---

## Action Agent

Responsible for:

- Executive action plans
- Business recommendations
- Prioritization
- Expected impact
- Implementation roadmap

---

# 🔄 Enterprise Execution Flow

```
User Query
      │
      ▼
EnterpriseOps Orchestrator
      │
      ▼
Intent Classification
      │
      ▼
Agent Delegation
      │
      ▼
BigQuery MCP Tool Calls
      │
      ▼
SQL Execution
      │
      ▼
Business Insights
      │
      ▼
Executive Report
```

# 🛠 Technology Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Agent Framework | Google ADK |
| Agent Platform | GEAP |
| LLM | Gemini 3.5 Flash |
| Architecture | Multi-Agent System |
| Tool Integration | BigQuery MCP Server |
| Database | Google BigQuery |
| Deployment | Google Agent Runtime |
| Infrastructure | NVIDIA GPU-backed Google Cloud |
| Version Control | Git & GitHub |
----

# 📁 Project Structure

```
enterpriseops-agent/
│
├── app/
│   └── agent.py
│
├── data/
│   ├── departments.csv
│   ├── employees.csv
│   ├── projects.csv
│   ├── project_resources.csv
│   ├── revenue_metrics.csv
│   ├── budget_metrics.csv
│   ├── customer_health.csv
│   ├── support_tickets.csv
│   └── vendors.csv
│
├── deployment/
│
├── .gemini/
│
├── agent-cli-manifest.yaml
│
├── Gemini.md
│
├── upload_csv_bq.py
│
├── requirements.txt
│
├── uv.lock
|__ Assets
│
└── README.md
```

---

# ⚙️ Execution Steps

🚀 Getting Started
Prerequisites

Ensure the following tools are installed on your machine:

Python 3.11+
UV Package Manager
Google Cloud CLI (gcloud)
Git
BigQuery API enabled
Agent Engine API enabled

## Step 1 — Create Workspace

```bash
mkdir enterpriseops-agent

cd enterpriseops-agent
```

---

## Step 2 — Install Google Agents CLI

```bash
uv tool install google-agents-cli
```

---

## Step 3 — Authenticate

```bash
gcloud auth application-default login
```

---

## Step 4 — Create GEAP Project

```bash
agents-cli create enterpriseops-agent -y
```

This command automatically generates:

```
app/
deployment/
.gemini/
agent-cli-manifest.yaml
Gemini.md
uv.lock
```

Replace the generated **app/agent.py** with the implementation from this repository.

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 — Create BigQuery Dataset

Create a dataset named:

```
enterprise_ops
```

---

## Step 7 — Upload Enterprise Data

```bash
python upload_csv_bq.py
```

This uploads all structured datasets into BigQuery.

---

## Step 8 — Start BigQuery MCP Toolbox

Open **Terminal 1**

```bash
export VERSION=1.1.0

curl -L -o toolbox https://storage.googleapis.com/mcp-toolbox-for-databases/v$VERSION/linux/amd64/toolbox

chmod +x toolbox

export BIGQUERY_PROJECT=geap-agent

./toolbox --prebuilt=bigquery --address=0.0.0.0 --port=8080
```

---

## Step 9 — Launch EnterpriseOps-Agent

Open **Terminal 2**

```bash
agents-cli playground
OR
uvx google-agents-cli playground
```

Your Multi-Agent System is now ready.

---
## Step 10 -Interact with agent

# 💬 Example Executive Queries

EnterpriseOps-Agent can answer complex cross-functional business questions such as:

### Finance

- Which departments exceeded their allocated budgets?
- Which regions are underperforming against revenue targets?
- What are the major financial risks this quarter?

---

### Operations

- Which projects require executive escalation?
- Which employees are overallocated?
- Where are the current operational bottlenecks?
- Generate an executive action plan.

---

### Customer

- Which customers are most likely to churn?
- Which support issues are impacting customer satisfaction?

---

### Risk

- Which vendors present the highest operational risk?
- Are there any governance or compliance concerns?

---

### Enterprise Leadership

- What should leadership focus on today?
- Generate an executive action plan.
- Summarize the organization's operational health.

---

## Step 11 -Deployment

#1.Create a Service Account

gcloud iam service-accounts create Enterpriseops-agent-sa \
--project=geap-agent

#2.Assign Required IAM Roles

Grant the following roles to the Service Account:

Agent Platform User
Agent Platform Admin
BigQuery User
BigQuery Data Viewer
Cloud Run Developer

These permissions allow EnterpriseOps-Agent to:

Access BigQuery datasets
Execute SQL through the BigQuery MCP Server
Deploy to Google Agent Runtime
Manage Agent Engine resources
Deploy to Google Agent Runtime

#3.Deploy the application using Google Agent Runtime.

 uvx google-agents-cli deploy \
  --service-account Enterpriseops-agent-sa@geap-agent.iam.gserviceaccount.com \
  --region us-central1 \
  --interactive

The deployed architecture consists of:

EnterpriseOps Orchestrator Agent
Finance Agent
Operations Agent
Customer Agent
Risk Agent
Action Agent

The application is hosted on Google Agent Runtime, leveraging NVIDIA GPU-backed Google Cloud infrastructure for scalable agent execution while using Gemini 3.5 Flash as the reasoning model.

 # Example Conversation

User

What should leadership focus on today?

↓

Finance Agent

Budget exceeded in HR.

↓

Operations Agent

Project Phoenix risk increased.

↓

Customer Agent

Customer ACME has churn risk.

↓

Risk Agent

Vendor ABC contract expires in 15 days.

↓

Action Agent

Prioritized executive roadmap generated.

# Executive Summary example

Revenue:
North region below target.

Projects:
Phoenix project high risk.

Customers:
Customer 102 churn risk high.

Risk:
Vendor contract expires soon.

Recommended Actions

✔ Increase staffing

✔ Renew vendor contract

✔ Contact customer

✔ Review department budget

# Challenges Faced

Designing effective MAS delegation
Structuring enterprise data
BigQuery MCP integration
Prompt engineering for specialist agents
Balancing autonomy with human oversight
Secure SQL execution
Agent Runtime deployment

 # Responsible AI (Expand)

Current version is good.

I would add:

No hallucinated business metrics
SQL execution through tools only
Human approval before actions
Principle of least privilege IAM
Transparent reasoning
Enterprise data never leaves GCP

 # Observability

Instead of only logs:

Explain:

Agent Runtime traces
Tool invocation logs
SQL query visibility
Agent delegation transparency
End-to-end execution monitoring

# Future Roadmap

Make it ambitious.

Approval workflows
Slack integration
Outlook integration
Gmail notifications
Vertex AI Search
DataPlex governance
Knowledge Graph
Predictive forecasting
SAP & ERP  integration
Jira integration

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

Please open an issue first for major changes.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developed For

**Kaggle capstone project**

**Enterprise Operations & Automation**

Built with ❤️ using:

- Google ADK (GEAP)
- Gemini 3.5 Flash
- Google BigQuery
- BigQuery MCP Server
- Google Agent Runtime
- Python

---

<p align="center">

### ⭐ If you found this project interesting, consider giving it a Star ⭐

</p>
