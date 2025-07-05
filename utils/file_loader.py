# utils/file_loader.py
import docx
import fitz  # PyMuPDF
from typing import Union
from io import BytesIO

def load_resume_text(uploaded_file: Union[BytesIO, str]) -> str:
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return _read_pdf(uploaded_file)
    elif file_name.endswith(".docx"):
        return _read_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file type")

def _read_pdf(file) -> str:
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def _read_docx(file) -> str:
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
