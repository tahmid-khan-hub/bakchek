from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import time
import logging

logger = logging.getLogger(__name__)

def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # react default port
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method}{request.url.path} - {response.status_code} - {duration:.2f}s")
    return response