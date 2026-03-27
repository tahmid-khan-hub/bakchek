from pydantic import BaseModel, Field

class AssesmentInput(BaseModel):
    # Work habits
    sitting_hours_per_day: float = Field(..., ge=0, le=24, description="Hours spent sitting daily")
    coding_hours_per_day: float = Field(..., ge=0, le=24, description="Hours spent coding daily")
    break_frequency_minutes: float = Field(..., ge=0, description="How often they take breaks in minutes")

    # Sleep
    sleep_hours_per_day: float = Field(..., ge=0, le=24, description="Hours of sleep daily")

     # Physical activity
    exercise_hours_per_week: float = Field(..., ge=0, description="Hours of exercise per week")
    walking_hours_per_day: float = Field(..., ge=0, le=24, description="Hours of walking daily")
    
    # Ergonomics
    has_ergonomic_chair: bool = Field(..., description="Whether they use ergonomic chair")
    monitor_at_eye_level: bool = Field(..., description="Whether monitor is at eye level")
    
    # Pain indicators
    current_back_pain: bool = Field(..., description="Currently experiencing back pain")
    neck_pain: bool = Field(..., description="Currently experiencing neck pain")
    
    # Age
    age: int = Field(..., ge=10, le=100, description="User age")
    