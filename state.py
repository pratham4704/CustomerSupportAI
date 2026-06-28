from typing import TypedDict, List


class SupportState(TypedDict):

    customer_name: str

    query: str

    intent: str

    retrieved_context: str

    conversation_history: List[str]

    approval_required: bool

    approval_status: str

    agent_response: str

    final_response: str