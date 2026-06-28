from langgraph.graph import StateGraph, START, END

from state import SupportState

from nodes import (
    classify_intent,
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent,
    memory_agent,
    general_agent,
    save_memory
)

from approval import (
    approval_node,
    approval_router
)

from supervisor import supervisor_node

from router import route_query

builder = StateGraph(SupportState)

# ------------------------
# Nodes
# ------------------------

builder.add_node("classify", classify_intent)

builder.add_node("sales_agent", sales_agent)

builder.add_node("technical_agent", technical_agent)

builder.add_node("billing_agent", billing_agent)

builder.add_node("account_agent", account_agent)

builder.add_node("memory_agent", memory_agent)

builder.add_node("general_agent", general_agent)

builder.add_node("approval", approval_node)

builder.add_node("supervisor", supervisor_node)

builder.add_node("save_memory", save_memory)

# ------------------------
# Start
# ------------------------

builder.add_edge(START, "classify")

# ------------------------
# Intent Routing
# ------------------------

builder.add_conditional_edges(
    "classify",
    route_query,
    {
        "sales_agent": "sales_agent",
        "technical_agent": "technical_agent",
        "billing_agent": "billing_agent",
        "account_agent": "account_agent",
        "memory_agent": "memory_agent",
        "general_agent": "general_agent"
    }
)

# ------------------------
# Agents -> Approval
# ------------------------

builder.add_edge("sales_agent", "approval")
builder.add_edge("technical_agent", "approval")
builder.add_edge("billing_agent", "approval")
builder.add_edge("account_agent", "approval")
builder.add_edge("general_agent", "approval")

# Memory goes directly
builder.add_edge("memory_agent", "supervisor")

# ------------------------
# Approval Routing
# ------------------------

builder.add_conditional_edges(
    "approval",
    approval_router,
    {
        "human_review": "supervisor",
        "supervisor": "supervisor"
    }
)

# ------------------------
# Save Conversation
# ------------------------

builder.add_edge("supervisor", "save_memory")

builder.add_edge("save_memory", END)

graph = builder.compile()