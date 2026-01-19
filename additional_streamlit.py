import streamlit as st
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load .env
load_dotenv()

# ---- Initialize Streamlit UI ----
st.set_page_config(page_title="Azure Chatbot", layout="centered")

st.title("🤖 Azure OpenAI Chatbot")

# ---- Initialize LLM ----
llm = AzureChatOpenAI(
    azure_endpoint="",
    azure_deployment="",
    api_version="",
    model='',
)

# ---- Token parser ----
def parse_the_output(result):
    usage = result.response_metadata.get("token_usage", {})
    return {
        "prompt": usage.get("prompt_tokens"),
        "completion": usage.get("completion_tokens"),
        "total": usage.get("total_tokens"),
    }

# ---- Initialize chat history ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

if "token_logs" not in st.session_state:
    st.session_state.token_logs = []


# ---- Chat message display ----
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---- User input ----
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # LLM response
    result = llm.invoke(st.session_state.messages)

    # Log tokens
    token_info = parse_the_output(result)
    st.session_state.token_logs.append(token_info)

    # Add assistant message
    assistant_msg = AIMessage(content=result.content)
    st.session_state.messages.append(assistant_msg)

    # Display assistant message
    with st.chat_message("assistant"):
        st.write(result.content)

        # Display token info under AI message
        st.caption(
            f"🧮 Tokens — Prompt: {token_info['prompt']}, "
            f"Completion: {token_info['completion']}, Total: {token_info['total']}"
        )

# ---- Display token summary ----
with st.expander("📊 Token Usage Summary"):
    st.write(st.session_state.token_logs)


#streamlit run additional_streamlit.py
