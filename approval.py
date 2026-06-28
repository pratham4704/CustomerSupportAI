HIGH_RISK = [
    "refund",
    "subscription cancellation",
    "cancel subscription",
    "account closure",
    "close my account",
    "compensation",
    "management",
    "escalate"
]


def approval_node(state):

    query = state["query"].lower()

    state["approval_required"] = any(
        keyword in query for keyword in HIGH_RISK
    )

    if state["approval_required"]:
        # In a real system this would pause for a human.
        state["approval_status"] = "Pending Human Approval"
    else:
        state["approval_status"] = "Approved"

    return state


def approval_router(state):
    """
    Route based on approval status.
    """
    if state["approval_required"]:
        return "human_review"

    return "supervisor"