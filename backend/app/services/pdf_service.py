from pathlib import Path

from pypdf import PdfReader

import pytesseract
from pdf2image import convert_from_path

# ----------------------------
# Windows Tesseract Path
# ----------------------------
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class PDFService:
    """
    Extracts text from normal PDFs.
    Falls back to OCR for scanned PDFs.
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

        # ---------------------------------
        # Try Normal PDF Extraction
        # ---------------------------------

        reader = PdfReader(pdf_file)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text and text.strip():

                pages.append(text)

        extracted_text = "\n".join(pages)

        # ---------------------------------
        # If enough text exists, return it
        # ---------------------------------

        if len(extracted_text.strip()) > 100:

            return extracted_text

        print("Scanned PDF detected. Running OCR...")

        # ---------------------------------
        # OCR Fallback
        # ---------------------------------

        try:

            images = convert_from_path(
                pdf_path,
                dpi=300,
                poppler_path=r"C:\Users\sneha\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
            )

            ocr_pages = []

            for image in images:

                text = pytesseract.image_to_string(
                    image,
                    lang="eng"
                )

                ocr_pages.append(text)

            return "\n".join(ocr_pages)

        except Exception as e:

            print("OCR Error:", e)

            return extracted_text


pdf_service = PDFService()