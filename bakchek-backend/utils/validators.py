from app.schemas.assessment import AssessmentInput
from app.core.exceptions import InvalidInputError

def validate_hours_consistency(data: AssessmentInput) -> None:
    total_hours = ( data.sitting_hours_per_day +
        data.walking_hours_per_day +
        data.sleep_hours_per_day )

    if total_hours > 24:
        raise InvalidInputError(
            f"Total hours (sitting + walking + sleep) cannot exceed 24. Got {total_hours}"
        )

def validate_assessment_input(data: AssessmentInput) -> None:
    validate_hours_consistency(data)