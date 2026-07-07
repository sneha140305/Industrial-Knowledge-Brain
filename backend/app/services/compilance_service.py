from app.services.gemini_service import gemini_service


class ComplianceService:

    def check_compliance(self, text: str):

        prompt = f"""
You are an Industrial Compliance Auditor.

Analyze this industrial document.

Check whether it includes:

- PPE Instructions
- Safety Warnings
- Emergency Procedure
- Lockout/Tagout
- Fire Safety
- Maintenance Instructions

For each item write:

✅ Present

or

❌ Missing

Finally give an Overall Compliance Score out of 100.

Document:

{text[:12000]}
"""

        return gemini_service.generate_response(prompt)


compliance_service = ComplianceService()