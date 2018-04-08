from docx import Document

# Function to convert Docx to Text
def parse_docx2txt(fname):
    text = str()
    doc = Document(fname)
    for p in doc.paragraphs:
        text = text + p.text
    return text