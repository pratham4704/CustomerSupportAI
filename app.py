import streamlit as st
from graph import graph

st.set_page_config(
    page_title="AI Customer Support Automation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Support Automation System")
st.markdown("### Powered by LangGraph + Gemini + RAG + SQLite")

st.divider()

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter customer name"
)

query = st.text_area(
    "Customer Query",
    placeholder="Type your query..."
)

if st.button("Submit Query"):

    if customer_name == "" or query == "":
        st.warning("Please fill all fields.")

    else:

        state = {

            "customer_name": customer_name,

            "query": query,

            "intent": "",

            "retrieved_context": "",

            "conversation_history": [],

            "approval_required": False,

            "approval_status": "",

            "agent_response": "",

            "final_response": ""

        }

        with st.spinner("Processing..."):

            result = graph.invoke(state)

        st.success("Request Processed Successfully")

        st.subheader("Detected Department")

        st.info(result["intent"])

        st.subheader("Approval Status")

        if result["approval_required"]:

            st.error(result["approval_status"])

        else:

            st.success(result["approval_status"])

        st.subheader("Retrieved Context")

        st.write(result["retrieved_context"])

        st.subheader("Final Response")

        st.success(result["final_response"])