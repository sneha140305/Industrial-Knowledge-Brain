from app.services.gemini_service import gemini_service


class ComparisonService:

    def compare_documents(
        self,
        text1: str,
        text2: str
    ):

        prompt = f"""
You are an Industrial AI Engineer.

Compare these two industrial documents.

Return:

## Summary

## Similarities

## Differences

## Safety Changes

## Maintenance Changes

## Operational Impact

Document A:

{text1[:8000]}

----------------------------

Document B:

{text2[:8000]}
"""

        return gemini_service.generate_response(prompt)


comparison_service = ComparisonService()