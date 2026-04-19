from pathlib import Path
from datetime import datetime

PROMPTS_DIR = Path(__file__).parent

def load_prompt(file_name: str) -> str:
    """Load a prompt template from a file.
    Args:
        file_name (str): The name of the prompt file to load.
    
    Returns:
        str: The content of the prompt file.
    """
    prompt_path = PROMPTS_DIR / file_name

    try:
        with open(prompt_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file '{file_name}' not found in {PROMPTS_DIR}")

IMAGE_PROMPT = load_prompt("image_prompt.txt")
TEXT_PROMPT = load_prompt("text_prompt.txt")
FILTER_EXTRACTION_PROMPT = load_prompt("filter_extraction_prompt.txt")