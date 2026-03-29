from app.schemas.assessment import AssessmentInput
from app.schemas.prediction import PredictionOutput
from app.services.suggestion_service import generate_suggestions
from app.ml.predictor import BackRiskPredictor
from app.utils.logger import logger
from app.core.exceptions import ModelNotLoadedError

predictor = BackRiskPredictor()

RISK_LEVELS = {
    "low": "Low Risk",
    "medium": "Medium Risk",
    "high": "High Risk"
}

DISCLAIMER = (
    "This assessment is AI-generated and intended for informational purposes only. "
    "It is not a substitute for professional medical advice. "
    "Please consult a doctor or physiotherapist for proper diagnosis."
)

async def get_prediction(data: AssessmentInput) -> PredictionOutput:
    logger.info("Running prediction for new assessment input")

    if not predictor.is_loaded:
        logger.error("ML model is not loaded")
        raise ModelNotLoadedError()

    risk_level, risk_score = predictor.predict(data)
    logger.info(f"Prediction result: {risk_level} ({risk_score:.2f})")

    suggestions = generate_suggestions(data, risk_level)
    logger.info(f"Generated {len(suggestions)} suggestions")

    return PredictionOutput(
        risk_level = risk_level,
        risk_score = round(risk_score, 2),
        risk_label = RISK_LEVELS[risk_level],
        suggestions = suggestions,
        disclaimer=DISCLAIMER
    )
