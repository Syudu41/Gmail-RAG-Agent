# config.py
import os

# Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TO_EMAIL = "recipient@example.com"
EMAIL_SUBJECT = "Summary of Your Requested Notes"

# File paths
PDF_PATH = "docs/my_notes.pdf"
CHROMA_DIR = "rag_db"

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
