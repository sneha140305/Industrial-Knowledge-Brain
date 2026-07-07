from pathlib import Path

from pypdf import PdfReader
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

class PDFService:
    """
    Reads PDF documents.
    """

    def extract_text(
        self,
        pdf_path: str,
    ) -> str:

        pdf_file = Path(pdf_path)

        if not pdf_file.exists():
            raise FileNotFoundError(
                f"{pdf_path} not found."
            )

        reader = PdfReader(pdf_file)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)


pdf_service = PDFService()