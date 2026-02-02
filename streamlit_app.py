import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="RAG Support Bot", layout="centered")
st.title("📘 Support Assistant")

question = st.text_input("Ask a question about policies or FAQs")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            res = requests.post(API_URL, json={"question": question})
            if res.status_code == 200:
                data = res.json()
                st.success(data["answer"])
                st.caption(f"⏱️ Latency: {data['latency_ms']} ms")
            else:
                st.error("Backend error")
