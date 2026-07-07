import re


class EntityService:

    def extract_entities(self, text: str):

        text_lower = text.lower()

        entities = {
            "document_type": "Unknown",
            "equipment": [],
            "ppe": [],
            "standards": [],
            "maintenance": [],
            "dates": [],
            "reading_time": 0,
            "risk_level": "Low"
        }

        # -----------------------------------
        # Detect Document Type
        # -----------------------------------

        if "maintenance" in text_lower:
            entities["document_type"] = "Maintenance Manual"

        elif "inspection" in text_lower:
            entities["document_type"] = "Inspection Report"

        elif "safety" in text_lower:
            entities["document_type"] = "Safety Procedure"

        elif "operating procedure" in text_lower:
            entities["document_type"] = "SOP"

        # -----------------------------------
        # Equipment Tags
        # -----------------------------------

        equipment_pattern = r"\b[A-Z]{1,5}-\d+\b"

        entities["equipment"] = list(
            set(re.findall(equipment_pattern, text))
        )

        # -----------------------------------
        # PPE
        # -----------------------------------

        ppe = [
            "helmet",
            "gloves",
            "goggles",
            "face shield",
            "mask",
            "respirator",
            "ear plugs",
            "safety shoes"
        ]

        for item in ppe:

            if item in text_lower:

                entities["ppe"].append(item.title())

        # -----------------------------------
        # Standards
        # -----------------------------------

        standards = re.findall(
            r"(ISO\s?\d+|OSHA|OISD[- ]?STD[- ]?\d+|PESO)",
            text
        )

        entities["standards"] = list(set(standards))

        # -----------------------------------
        # Maintenance Interval
        # -----------------------------------

        maintenance = re.findall(
            r"every\s+\d+\s+(days?|weeks?|months?|hours?)",
            text_lower
        )

        entities["maintenance"] = list(set(maintenance))

        # -----------------------------------
        # Dates
        # -----------------------------------

        entities["dates"] = list(
            set(
                re.findall(
                    r"\d{2}/\d{2}/\d{4}",
                    text
                )
            )
        )

        # -----------------------------------
        # Reading Time
        # -----------------------------------

        words = len(text.split())

        entities["reading_time"] = max(
            1,
            round(words / 220)
        )

        # -----------------------------------
        # Risk Level
        # -----------------------------------

        danger_words = [
            "danger",
            "fatal",
            "hazard",
            "explosion",
            "fire",
            "high voltage"
        ]

        count = 0

        for word in danger_words:

            if word in text_lower:

                count += 1

        if count >= 4:

            entities["risk_level"] = "High"

        elif count >= 2:

            entities["risk_level"] = "Medium"

        return entities


entity_service = EntityService()