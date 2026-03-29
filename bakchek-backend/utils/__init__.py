from .logger import logger
from .validators import validate_assessment_input

'''
**What these do simply:**

`logger.py` — sets up one **central logger** for the entire BakChek app. Every other file just imports this single logger instead of creating their own. In development mode it shows detailed debug logs, in production only important logs show.

The output format will look like:
2026-03-27 10:23:45 | INFO | bakchek | Server started
2026-03-27 10:23:46 | INFO | bakchek | POST /api/predict - 200 - 0.23s

'''
