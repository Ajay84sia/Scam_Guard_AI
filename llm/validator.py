# llm/validator.py

from pydantic import BaseModel, Field, ValidationError
from typing import List

class ScamDetectionOutput(BaseModel):
    label: str = Field(..., description="Scam | Not Scam | Uncertain")
    reasoning: str = Field(..., description="Step-by-step analysis of why the label was assigned")
    intent: str = Field(..., description="Short description of the user's intent")
    risk_factors: List[str] = Field(..., description="List of red flags identified in the message")

def validate_output(response: dict) -> ScamDetectionOutput:
    """
    Validate and return structured ScamDetectionOutput model.
    If validation fails, raise a clear error.
    """
    try:
        return ScamDetectionOutput(**response)
    except ValidationError as e:
        raise ValueError(f"LLM output failed schema validation: {str(e)}") 