from docx import Document
from app.services.vector_db_service import add_documents

def extract_paragraphs(doc):
    paragraphs = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())
    return paragraphs

def load_document(file_path):
    doc = Document(file_path)
    paragraphs = extract_paragraphs(doc)

    print(f"Número total de párrafos: {len(paragraphs)}")

    add_documents(paragraphs)

if __name__ == "__main__":
    load_document("./data/documento.docx")
