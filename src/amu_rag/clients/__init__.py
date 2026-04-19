"""External API clients for Gemini"""
from .gemini_client import generate_content as gemini_generate
from .ollama_client import generate_content as ollama_generate

__all__ = ["gemini_generate", "ollama_generate"]