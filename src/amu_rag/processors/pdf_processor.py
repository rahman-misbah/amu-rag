from ..config import RAW_DATA_PDF_DIR, PROCESSED_DATA_DIR
from ..prompts import IMAGE_PROMPT
from ..core.gemini_client import generate_content
from datetime import datetime
from pdf2image import convert_from_path

def process_pdf(file_name: str):
    """Process a PDF file and generate content using the Gemini API.
    
    Args:
        file_name (str): The name of the PDF file to process.
    
    Returns:
        None: The generated content is saved to a text file.
    """
    
    # Convert PDF to images
    images = convert_from_path(RAW_DATA_PDF_DIR / file_name, dpi=200)

    # Generate content using the Gemini API
    prompt = (IMAGE_PROMPT,) + tuple(images)
    response = generate_content(prompt)

    # Generate timestamped file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = PROCESSED_DATA_DIR / f"{now}.txt"

    # Save the response to a text file
    with open(output_file_name, "w") as f:
        f.write(response)
