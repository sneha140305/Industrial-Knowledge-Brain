import os

from app.core.config import settings
from app.services.pdf_service import pdf_service
from app.services.gemini_service import gemini_service


class ComparisonService:

    def compare_documents(
        self,
        document1: str,
        document2: str,
    ):

        path1 = os.path.join(
            settings.UPLOAD_DIR,
            document1
        )

        path2 = os.path.join(
            settings.UPLOAD_DIR,
            document2
        )

        text1 = pdf_service.extract_text(path1)
        text2 = pdf_service.extract_text(path2)

        prompt = f"""
Compare these two industrial documents.

Document 1:
{text1[:6000]}

Document 2:
{text2[:6000]}

Return:

1. Summary

2. Similarities

3. Differences

4. Maintenance Comparison

5. Safety Comparison

6. Compliance Comparison

7. Recommendations

Format clearly using bullet points.
"""

        answer = gemini_service.generate_response(prompt)

        return {
            "summary": answer,
            "similarities": [],
            "differences": [],
            "recommendations": []
        }


comparison_service = ComparisonService()