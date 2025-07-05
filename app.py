# app.py
import streamlit as st
from utils.file_loader import load_resume_text

st.set_page_config(page_title="AI Resume Tailor", layout="centered")
st.title("AI Resume Tailor")

st.markdown("Upload your resume and paste the job description below to get a tailored rewrite.")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# Paste job description
job_description = st.text_area("Paste Job Description", height=200)

# Optional: user email
user_email = st.text_input("Optional: Enter your email to receive the tailored resume")

# Process button
if uploaded_file and job_description:
    resume_text = load_resume_text(uploaded_file)
    
    if st.button("Tailor My Resume"):
        st.session_state.resume_text = resume_text
        st.session_state.job_description = job_description
        st.success("Resume and job description loaded. Proceed to rewriting...")

elif not uploaded_file or not job_description:
    st.info("Please upload a resume and paste the job description.")
