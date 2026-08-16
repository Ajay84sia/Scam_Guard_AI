import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
PROJECT_ROOT = Path(__file__).parent
load_dotenv(PROJECT_ROOT / ".env")

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Settings
DEFAULT_MODEL = os.getenv("GEMINI_MODEL")
MAX_RETRIES = 3
RETRY_DELAY = 2

# Processing Settings
DEFAULT_BATCH_SIZE = 10
STREAMLIT_BATCH_SIZE = 5