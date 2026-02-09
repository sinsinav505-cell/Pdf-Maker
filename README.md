# Document to PDF Converter (FastAPI + Streamlit)

## 📌 Project Overview
This project is a full-stack web application that allows users to upload **text (.txt)** or **Word (.docx)** files and download the converted **PDF file**.  
The frontend is built using **Streamlit**, and the backend is implemented using **FastAPI**.

The application follows a clean separation of concerns:
- **Streamlit** handles the user interface
- **FastAPI** handles file processing and PDF generation

---

## 🛠️ Technologies Used
- Python 3
- Streamlit (Frontend)
- FastAPI (Backend)
- python-docx (for reading `.docx` files)
- ReportLab (for PDF generation)
- Requests (for frontend–backend communication)
- Uvicorn (ASGI server)

---


## ✅ Features
- Upload `.txt` and `.docx` files
- Validates file type and empty files
- Converts uploaded content into PDF format
- Download the generated PDF
- Clean full-stack architecture
- Error handling for unsupported files
