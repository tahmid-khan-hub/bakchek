from app.schemas.assessment import AssessmentInput
from app.schemas.prediction import Suggestion

def generate_suggestions(data: AssessmentInput, risk_level: str) -> list[Suggestion]:
    suggestions = []

    # Sitting hours check
    if data.sitting_hours_per_day > 6:
        suggestions.append(Suggestion(
            category = "Posture",
            message = "You sit more than 6 hours daily. Try to stand or stretch every 45 minutes.",
            priority = "high" if data.sitting_hours_per_day > 10 else "medium"
        ))

    # Break frequency check
    if data.break_frequency_minutes > 60:
        suggestions.append(Suggestion(
            category="Break Habits",
            message="Take a short break every 30-45 minutes to reduce spinal pressure.",
            priority="high"
        ))
    
    # Sleep check
    if data.sleep_hours_per_day < 7:
        suggestions.append(Suggestion(
            category = "Sleep",
            message="You are sleeping less than 7 hours. Poor sleep slows muscle recovery and increases back pain risk.",
            priority="high"
        ))
    elif data.sleep_hours_per_day > 9:
        suggestions.append(Suggestion(
            category="Sleep",
            message="Sleeping more than 9 hours can cause stiffness. Aim for 7-9 hours.",
            priority="low"
        ))

    # Exercise check
    if data.exercise_hours_per_week < 2:
        suggestions.append(Suggestion(
            category="Exercise",
            message="You exercise less than 2 hours per week. Aim for at least 3 hours of light exercise weekly.",
            priority="high" if risk_level == "high" else "medium"
        ))
    
    # Ergonomic chair check
    if not data.has_ergonomic_chair:
        suggestions.append(Suggestion(
            category="Ergonomics",
            message="Consider using an ergonomic chair to maintain proper spinal alignment while sitting.",
            priority="medium"
        ))
    
    # Monitor level check
    if not data.monitor_at_eye_level:
        suggestions.append(Suggestion(
            category="Ergonomics",
            message="Place your monitor at eye level to avoid neck strain and forward head posture.",
            priority="medium"
        ))
    
    # Current pain check
    if data.current_back_pain:
        suggestions.append(Suggestion(
            category="Medical",
            message="You currently have back pain. Consider consulting a physiotherapist.",
            priority="high"
        ))
    if data.neck_pain:
        suggestions.append(Suggestion(
            category="Medical",
            message="You currently have neck pain. Check your monitor height and pillow support.",
            priority="high"
        ))
    
    # Walking check
    if data.walking_hours_per_day < 0.5:
        suggestions.append(Suggestion(
            category="Activity",
            message="Try to walk at least 30 minutes daily. Even short walks reduce back pain risk significantly.",
            priority="medium"
        ))
    
    return suggestions
