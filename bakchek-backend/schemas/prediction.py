from pydantic import BaseModel
from typing import List

class Suggestion(BaseModel):
    category: str        # e.g. "Sleep", "Exercise", "Ergonomics"
    message: str         # e.g. "Take a 5 min break every 30 minutes"
    priority: str        # "high", "medium", "low"

class PredictionOutput(BaseModel):
    risk_level: str              # "low", "medium", "high"
    risk_score: float            # e.g. 0.73 (probability)
    risk_label: str              # "High Risk" — human readable
    suggestions: List[Suggestion]
    disclaimer: str              # "This is not medical advice..."