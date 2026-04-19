import streamlit as st
import requests

st.set_page_config(page_title="AMU RAG Assistant", page_icon="🎓", layout="centered")

st.markdown("""
<style>
.big-title {text-align: center; font-size: 34px; font-weight: 700;}
.subtitle {text-align: center; color: grey; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎓 AMU RAG Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything based on your data</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Settings")
    api_url = st.text_input("Backend URL", "http://127.0.0.1:8000/query")
    if st.button("Clear Chat"):
        st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Type your question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.spinner("Thinking..."):
            response = requests.post(api_url, json={"query": prompt}, timeout=30)

            if response.status_code != 200:
                answer = f"Server Error: {response.status_code}"
            else:
                data = response.json()
                answer = data.get("answer", "No answer returned")

    except Exception as e:
        answer = f"Connection Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)