from google import genai

from config import GOOGLE_API_KEY, MODEL_NAME
from rag import retrieve
from memory import get_previous_issue, save_conversation

# Initialize Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)


# ----------------------------------------------------
# Helper Function
# ----------------------------------------------------

def generate_response(prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text


# ----------------------------------------------------
# Intent Classification
# ----------------------------------------------------

def classify_intent(state):

    query = state["query"].lower()

    if any(word in query for word in [
        "previous support issue",
        "previous issue",
        "last issue"
    ]):
        state["intent"] = "Memory"
        return state

    if any(word in query for word in [
        "price",
        "pricing",
        "subscription",
        "plan",
        "cost"
    ]):
        state["intent"] = "Sales"
        return state

    if any(word in query for word in [
        "error",
        "crash",
        "login",
        "installation",
        "install",
        "configuration",
        "bug"
    ]):
        state["intent"] = "Technical"
        return state

    if any(word in query for word in [
        "refund",
        "payment",
        "invoice",
        "billing"
    ]):
        state["intent"] = "Billing"
        return state

    if any(word in query for word in [
        "password",
        "profile",
        "account",
        "activate",
        "deactivate"
    ]):
        state["intent"] = "Account"
        return state

    state["intent"] = "General"

    return state


# ----------------------------------------------------
# Sales Agent
# ----------------------------------------------------

def sales_agent(state):

    context = retrieve(state["query"])

    prompt = f"""
You are the Sales Support Agent.

Use ONLY the information below.

Context:
{context}

Customer Question:
{state['query']}

Answer professionally.
"""

    state["retrieved_context"] = context
    state["agent_response"] = generate_response(prompt)

    return state


# ----------------------------------------------------
# Technical Agent
# ----------------------------------------------------

def technical_agent(state):

    context = retrieve(state["query"])

    prompt = f"""
You are the Technical Support Engineer.

Use ONLY the information below.

Context:
{context}

Customer Question:
{state['query']}

Give a step-by-step solution.
"""

    state["retrieved_context"] = context
    state["agent_response"] = generate_response(prompt)

    return state


# ----------------------------------------------------
# Billing Agent
# ----------------------------------------------------

def billing_agent(state):

    context = retrieve(state["query"])

    prompt = f"""
You are the Billing Department.

Use ONLY the following information.

Context:
{context}

Customer Question:
{state['query']}
"""

    state["retrieved_context"] = context
    state["agent_response"] = generate_response(prompt)

    return state


# ----------------------------------------------------
# Account Agent
# ----------------------------------------------------

def account_agent(state):

    context = retrieve(state["query"])

    prompt = f"""
You are the Account Support Team.

Use ONLY the following information.

Context:
{context}

Customer Question:
{state['query']}
"""

    state["retrieved_context"] = context
    state["agent_response"] = generate_response(prompt)

    return state


# ----------------------------------------------------
# Memory Agent
# ----------------------------------------------------

def memory_agent(state):

    previous = get_previous_issue(state["customer_name"])

    state["retrieved_context"] = previous

    state["agent_response"] = f"""
Your previous support issue was:

{previous}
"""

    return state


# ----------------------------------------------------
# General Agent
# ----------------------------------------------------

def general_agent(state):

    prompt = f"""
Answer professionally.

Question:

{state['query']}
"""

    state["agent_response"] = generate_response(prompt)

    return state


# ----------------------------------------------------
# Save Memory
# ----------------------------------------------------

def save_memory(state):

    if state["intent"] != "Memory":

        save_conversation(

            state["customer_name"],

            state["query"],

            state["final_response"]

        )

    return state