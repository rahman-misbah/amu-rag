"""Configuration module for AMU RAG system. This module loads environment variables and sets up configuration parameters for the Gemini API and other components of the system."""

import os
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

# Load environment variables from .env file
load_dotenv(PROJECT_ROOT / ".env")

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.1"))
GEMINI_TOP_P = float(os.getenv("GEMINI_TOP_P", "0.1"))
GEMINI_TOP_K = int(os.getenv("GEMINI_TOP_K", "10"))
GEMINI_MAX_TOKENS = int(os.getenv("GEMINI_MAX_TOKENS", "8192"))

# Validation
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it to your Gemini API key.")

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# Raw data directories
RAW_DATA_DIR = DATA_DIR / "raw"
RAW_DATA_IMAGE_DIR = RAW_DATA_DIR / "image"
RAW_DATA_TEXT_DIR = RAW_DATA_DIR / "text"

# Processed data directory
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Create necessary directories if they don't exist
for dir in [DATA_DIR, RAW_DATA_DIR, RAW_DATA_IMAGE_DIR, RAW_DATA_TEXT_DIR, PROCESSED_DATA_DIR]:
    if not dir.exists():
        dir.mkdir(parents=True, exist_ok=True)