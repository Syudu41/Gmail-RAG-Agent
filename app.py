# app.py
import os
import streamlit as st
from tempfile import NamedTemporaryFile

from rag_utils import create_vectorstore_from_pdf
from agent import build_agent_from_vectorstore
from gmail_utils import gmail_authenticate, send_email
from config import EMAIL_SUBJECT

st.set_page_config(page_title="Agentic RAG Gmail Bot", layout="centered")

st.title("📧 AI-Powered Email Agent with RAG")
st.write("Upload a PDF, generate a summary using RAG, and send it to any email.")

# --- Upload PDF ---
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
user_prompt = st.text_input("What do you want the agent to do?", value="Summarize this document.")
email_to = st.text_input("Enter recipient email")

# Session state to track summary
if "summary" not in st.session_state:
    st.session_state.summary = ""

if uploaded_file:
    with NamedTemporaryFile(delete=False, suffix=".pdf", dir="uploaded_docs") as tmp:
        tmp.write(uploaded_file.read())
        temp_pdf_path = tmp.name

    if st.button("🧠 Run Agent"):
        with st.spinner("Creating vectorstore and summarizing..."):
            vectordb = create_vectorstore_from_pdf(temp_pdf_path)
            agent = build_agent_from_vectorstore(vectordb)
            result = agent.run(user_prompt)
            st.session_state.summary = result

if st.session_state.summary:
    st.subheader("📄 Generated Summary")
    st.text_area("Summary (editable)", value=st.session_state.summary, height=300, key="summary_edit")

    if st.button("📤 Send Email"):
        if email_to:
            with st.spinner("Authenticating and sending email..."):
                service = gmail_authenticate()
                send_email(service, email_to, EMAIL_SUBJECT, st.session_state.summary_edit)
                st.success(f"✅ Email sent to {email_to}")
        else:
            st.error("Please enter a valid email address.")
