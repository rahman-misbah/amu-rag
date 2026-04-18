from ..config import RAW_DATA_IMAGE_DIR, PROCESSED_DATA_DIR
from ..prompts import IMAGE_PROMPT
from ..core.gemini_client import generate_content
from datetime import datetime
from PIL import Image

def process_image(file_name: str):
    """Process an image file and generate content using the Gemini API.
    
    Args:
        file_name (str): The name of the image file to process.
    
    Returns:
        None: The generated content is saved to a text file.
    """
    # Load the image
    image = Image.open(RAW_DATA_IMAGE_DIR / file_name)
    
    # Generate content using the Gemini API
    prompt = (IMAGE_PROMPT, image)
    response = generate_content(prompt)

    # Generate timestamped file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = PROCESSED_DATA_DIR / f"{now}.txt"

    # Save the response to a text file
    with open(output_file_name, "w") as f:
        f.write(response)