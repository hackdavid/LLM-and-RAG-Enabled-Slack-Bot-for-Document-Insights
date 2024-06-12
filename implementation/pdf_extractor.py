import fitz

class PDFExtractor:
    
    @classmethod
    def process(cls, pdf_path):
        try:
            doc = fitz.open(pdf_path)
            text = []
            for page in doc:
                text.append(page.get_text())
            return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return None
