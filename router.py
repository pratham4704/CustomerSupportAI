def route_query(state):
    """
    Returns the next node name based on intent.
    """

    intent = state["intent"]

    routes = {
        "Sales": "sales_agent",
        "Technical": "technical_agent",
        "Billing": "billing_agent",
        "Account": "account_agent",
        "Memory": "memory_agent",
        "General": "general_agent"
    }

    return routes.get(intent, "general_agent")