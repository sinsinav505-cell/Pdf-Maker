from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from docx import Document
from reportlab.pdfgen import canvas
import io

app = FastAPI()


def extract_text(file: UploadFile) -> str:
    text = ""

    if file.content_type == "text/plain":
        text = file.file.read().decode("utf-8")

    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file.file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    return text


def text_to_pdf(text: str) -> io.BytesIO:
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)

    y = 800
    for line in text.split("\n"):
        pdf.drawString(40, y, line)
        y -= 15
        if y < 40:
            pdf.showPage()
            y = 800

    pdf.save()
    buffer.seek(0)
    return buffer


@app.post("/convert")
async def convert_file(file: UploadFile = File(...)):
    text = extract_text(file)

    if not text.strip():
        raise HTTPException(status_code=400, detail="File is empty")

    pdf_buffer = text_to_pdf(text)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=output.pdf"}
    )