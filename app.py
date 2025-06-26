import streamlit as st
from utils import get_chat_response
from prompts import SYSTEM_PROMPT

st.set_page_config(
    page_title="Career GPT Chatbot",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Career GPT Chatbot")
st.write("Get tailored career advice, CV tips and skill suggestions with Cohere.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a career question:")

if st.button("Ask") and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = get_chat_response(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display the chat history
for message in st.session_state.chat_history:
    role = "You" if message["role"] == "user" else "CareerGPT"
    st.markdown(f"**{role}:** {message['content']}")
