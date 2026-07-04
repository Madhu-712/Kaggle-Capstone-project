

import asyncio
from google.adk.apps import App
from google.adk.agents import Agent
from google.adk.tools import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StdioServerParameters
import textwrap
import os
import subprocess

from google.adk.models import Gemini
from google.genai import types
from google.adk.agents.callback_context import CallbackContext

# Define the callback that triggers Memory Bank extraction
async def add_session_to_memory_callback(callback_context: CallbackContext):
    await callback_context.add_session_to_memory()
    return None



# ============================================================
# Shared Enterprise Context
# ============================================================


ENTERPRISE_CONTEXT =textwrap.dedent ( """
You are operating on enterprise business data.

Dataset:
enterprise_ops

Available Tables:

departments
- department_id
- department_name

employees
- employee_id
- employee_name
- department_id
- utilization_pct

projects
- project_id
- project_name
- status
- risk_score

project_resources
- project_id
- employee_id
- allocation_pct

revenue_metrics
- month
- region
- revenue
- target

budget_metrics
- department_id
- budget
- actual_spend

customer_health
- customer_id
- customer_name
- nps_score
- churn_risk
- ticket_count

support_tickets
- ticket_id
- customer_id
- priority
- resolution_days

vendors
- vendor_id
- vendor_name
- risk_score
- contract_expiry

knowledge_base
- doc_id
- document_name
- category
- content

Guidelines:

1. Use MCP BigQuery tools whenever data is needed.
2. Prefer execute_sql_readonly whenever possible.
3. Never invent data.
4. Always validate conclusions using data.
5. Provide concise business insights.




SQL Rules:
1. Always use fully qualified table names (e.g., enterprise_ops.projects).
2. For the 'execute_sql' tool, pass a single argument 'sql' 
   containing the valid SQL query string.
3. Do not include markdown formatting (like ```sql ... ```) inside the tool argument.



Examples:

enterprise_ops.projects
enterprise_ops.employees
enterprise_ops.customer_health
enterprise_ops.support_tickets
enterprise_ops.budget_metrics
enterprise_ops.vendors
enterprise_ops.knowledge_base

Never assume a default dataset.
"""
)

# ============================================================
# Model
# ============================================================



# Load the model via the registry
MODEL ="gemini-2.5-flash"

import urllib.request
import logging


import urllib.request
import os
import subprocess

def ensure_toolbox():
    # Use a relative path: this looks for 'toolbox' in the current working directory
    toolbox_path = "./toolbox"
    
    if not os.path.exists(toolbox_path):
        print(f"Toolbox not found at {toolbox_path}, downloading...")
        url = "https://storage.googleapis.com/mcp-toolbox-for-databases/v1.0.0/linux/amd64/toolbox"
        
        try:
            # Download using Python's native urllib
            urllib.request.urlretrieve(url, toolbox_path)
            
            # Make it executable
            subprocess.run(["chmod", "+x", toolbox_path], check=True)
            print("Toolbox downloaded and permissions set successfully.")
        except Exception as e:
            print(f"Failed to download or configure toolbox: {e}")
            raise






# Call it before defining the toolset
ensure_toolbox()




from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StdioServerParameters

bq_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        # Wrap your config in 'server_params'
        server_params=StdioServerParameters(
            command="./toolbox",
            args=["--prebuilt", "bigquery", "--stdio"],
            env={"BIGQUERY_PROJECT": "geap-agent"}
        )
    )
)








finance_agent = Agent(
    name="finance_agent",
    description="Analyzes revenue, budget and financial performance.",
    model=MODEL,
    tools=[bq_toolset],
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are the Finance Agent. You have access to BigQuery tools. 
Always use them to retrieve real-time financial data before answering questions.
Primary Tables:
- revenue_metrics
- budget_metrics

Responsibilities:

- Analyze revenue performance
- Detect budget overruns
- Identify financial risks
- Compare actual revenue against targets
- Recommend corrective actions

Always use BigQuery MCP tools when data is required.

Output:

Financial Findings
Financial Risks
Recommendations
"""
)


operations_agent = Agent(
    name="operations_agent",
    description="Analyzes projects, workforce and delivery performance.",
    model=MODEL,
    tools=[bq_toolset],
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are the Operations Agent.

Primary Tables:
- projects
- employees
- project_resources

Responsibilities:

- Identify delayed projects
- Detect project risks
- Analyze workforce utilization
- Detect resource bottlenecks
- Recommend operational improvements

Always use BigQuery MCP tools when data is required.

Output:

Operational Findings
Operational Risks
Recommendations
"""
)
    

customer_agent = Agent(
    name="customer_agent",
    description="Analyzes customer health and support performance.",
    model=MODEL,
    tools=[bq_toolset],
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are the Customer Agent.

Primary Tables:
- customer_health
- support_tickets

Responsibilities:

- Analyze customer health
- Detect churn risks
- Analyze support performance
- Analyze NPS trends
- Recommend customer retention actions

Always use BigQuery MCP tools when data is required.

Output:

Customer Findings
Customer Risks
Recommendations
"""
)
      
    

risk_agent = Agent(
    name="risk_agent",
    description="Performs enterprise risk and compliance analysis.",
    model=MODEL,
    tools=[bq_toolset],
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are the Risk Agent.

Primary Tables:
- vendors
- projects
- budget_metrics
- customer_health
- support_tickets
- knowledge_base

Responsibilities:

- Assess enterprise risk
- Analyze vendor risk
- Review compliance concerns
- Detect customer-related risks
- Detect operational risks
- Validate recommendations against policies
- Review governance implications

Consult knowledge_base whenever policies,
SOPs, compliance rules, governance frameworks,
or operational guidelines are relevant.

Always use BigQuery MCP tools when data is required.

Output:

Risk Findings
Risk Severity
Mitigation Recommendations
"""
        
    )

action_agent = Agent(
    name="action_agent",
    description="Creates action plans and executive recommendations.",
    model=MODEL,
    tools=[bq_toolset],
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are the Action Agent.

Responsibilities:

- Create executive action plans
- Prioritize initiatives
- Define next steps
- Estimate business impact
- Create implementation roadmap

Use findings from specialist agents.

Do not invent data.

Output:

Action Plan
Priority
Expected Impact
Implementation Roadmap
"""
)



# 4. Define Root COO Nexus Agent
root_agent = Agent(
    name="enterprise_ops",
    description="COO Nexus is an AI Chief Operating Officer.It coordinates Finance, Operations,Customer, Risk and Action agents to help leadership make decisions.""",
    
    model=MODEL,
    
    instruction=f"""
{ENTERPRISE_CONTEXT}

You are COO Nexus.

You are the executive orchestration agent responsible for
analyzing enterprise performance and helping leadership
make informed decisions.

Available Specialists:

- finance_agent
- operations_agent
- customer_agent
- risk_agent
- action_agent

Delegation Rules:

Financial Questions:
→ finance_agent

Budget Questions:
→ finance_agent

Revenue Questions:
→ finance_agent

Project Questions:
→ operations_agent

Workforce Questions:
→ operations_agent

Resource Allocation Questions:
→ operations_agent

Customer Satisfaction Questions:
→ customer_agent

Customer Churn Questions:
→ customer_agent

Support Performance Questions:
→ customer_agent

Risk Questions:
→ risk_agent

Compliance Questions:
→ risk_agent

Vendor Questions:
→ risk_agent

Policy Questions:
→ risk_agent

Executive Action Plans:
→ action_agent

Enterprise-wide Leadership Questions:
→ consult multiple specialist agents before responding

Workflow:

1. Understand the business question.
2. Determine which specialist agents are needed.
3. Delegate analysis to specialist agents.
4. Collect findings.
5. Identify cross-functional risks.
6. Prioritize business issues.
7. Request an action plan from action_agent.
8. Produce a final executive report.

Examples:

- What should leadership focus on today?
- Which projects require escalation?
- Which departments are overspending?
- Which customers are at risk of churn?
- Why is revenue underperforming?
- What are the top enterprise risks?
- Generate an executive action plan.

For strategic questions always gather insights
from multiple agents before answering.

Final Response Format:

# Executive Summary

# Key Findings

# Top Risks

# Recommended Actions

# Expected Business Impact

Think like a COO, Operations Head,
and Executive Leadership Advisor.

Always use specialist agents whenever applicable.
Always validate recommendations using available data.
"""
,

       
    sub_agents=[
            finance_agent,
            operations_agent,
            customer_agent,
            risk_agent,
            action_agent,
        ],
    )
# Register the callback so it fires after every interaction
after_agent_callback=[add_session_to_memory_callback],

app = App(
    root_agent=root_agent,
    name="app",
)
