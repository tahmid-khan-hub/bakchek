from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class ModelNotLoadedError(Exception):
    pass

class InvalidInputError(Exception):
    pass

async def model_not_loaded_handler(request: Request, exc: ModelNotLoadedError ):
    return JSONResponse(
        status_code=503,
        content={
            "error": "Model not available",
            "message": "ML model is not loaded yet. Please try again later.",
            "status": "service_unavailable"
        }
    )

async def invalid_input_handler(request: Request, exc: InvalidInputError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Invalid input",
            "message": str(exc),
            "status": "unprocessable_entity"
        }
    )