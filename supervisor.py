from google import genai

from config import GOOGLE_API_KEY, MODEL_NAME

# Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)


def supervisor_node(state):
    """
    Reviews and improves the generated response.
    """

    # If approval is required, don't generate a final answer
    if state["approval_required"]:

        state["final_response"] = f"""
Your request requires manual review by a human supervisor.

Request Type : {state["intent"]}

Approval Status : Pending

Our support team will contact you within 24 hours.

Thank you for your patience.
"""

        return state

    prompt = f"""
You are a Senior Customer Support Supervisor.

Review the following response.

Requirements:
- Professional
- Friendly
- Clear
- Correct grammar
- Keep the same meaning

Customer Query:
{state["query"]}

Agent Response:
{state["agent_response"]}

Return only the improved response.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    state["final_response"] = response.text

    return state