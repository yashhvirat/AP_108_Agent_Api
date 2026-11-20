import streamlit as st
from backend.ai_engine import ask_powerbi

st.set_page_config(
    page_title="AP108 AI Business Analyst",
    page_icon="🚑",
    layout="wide"
)

st.title("🚑 AP108 AI Business Analyst")
st.caption("Ask questions about AP108 ambulance operations")

question = st.chat_input("Ask a question about AP108 data...")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("data") is not None:
            st.dataframe(message["data"], use_container_width=True)

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing AP108 data..."):
            result = ask_powerbi(question)

        if result["status"] == "success":
            st.success("Query executed successfully")

            data = result.get("data")

            if data is not None:
                st.dataframe(data, use_container_width=True)

            with st.expander("View generated DAX"):
                st.code(result.get("dax", ""), language="sql")

            assistant_message = {
                "role": "assistant",
                "content": "Here are your results.",
                "data": data
            }

        else:
            st.error(result.get("explanation", "Something went wrong"))

            assistant_message = {
                "role": "assistant",
                "content": f"Error: {result.get('explanation')}",
                "data": None
            }

        st.session_state.messages.append(assistant_message)
