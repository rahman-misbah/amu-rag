from ..config import RAW_DATA_TEXT_DIR, PROCESSED_DATA_DIR
from ..prompts import TEXT_PROMPT
from ..core.gemini_client import generate_content
from datetime import datetime

def process_text(file_name: str):
    """Process a text file and generate content using the Gemini API.
    
    Args:
        file_name (str): The name of the text file to process.
    
    Returns:
        None: The generated content is saved to a text file.
    """
    # Read the text file
    with open(RAW_DATA_TEXT_DIR / file_name, "r") as f:
        text = f.read()

    # Generate content using the Gemini API
    prompt = (TEXT_PROMPT, text)
    response = generate_content(prompt)

    # Generate timestamped file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = PROCESSED_DATA_DIR / f"{now}.txt"

    # Save the response to a text file
    with open(output_file_name, "w") as f:
        f.write(response)