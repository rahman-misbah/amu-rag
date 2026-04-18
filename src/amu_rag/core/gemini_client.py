from google import genai
from google.genai import types
from ..config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_TOKENS

_GEN_CONFIG = types.GenerateContentConfig(
    temperature=GEMINI_TEMPERATURE,
    top_p=GEMINI_TOP_P,
    top_k=GEMINI_TOP_K,
    max_output_tokens=GEMINI_MAX_TOKENS,
)

_client = genai.Client(api_key=GEMINI_API_KEY)

def generate_content(prompt: str) -> str:
    try:
        response = _client.models.generate_content(
            model=GEMINI_MODEL,
            config=_GEN_CONFIG,
            contents=[prompt],
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"Failed to generate content: {e}")
