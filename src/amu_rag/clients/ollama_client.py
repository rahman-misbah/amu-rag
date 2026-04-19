"""Client for interacting with local Ollama LLM (Llama 3.2)"""
import requests
from typing import Optional

from ..config import OLLAMA_BASE_URL, OLLAMA_MODEL

def generate_content(prompt: str, options: Optional[dict] = None) -> str:
    """Generates content using the local Ollama LLM based on the provided prompt.
    
    Args:
        prompt (str): The prompt to be sent to the Ollama LLM.
        options (dict, optional): Additional options for the LLM generation.

    Returns:
        str: The generated content from the Ollama LLM.
    """
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": options or {}
            }
        )

        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to generate content: {e}")