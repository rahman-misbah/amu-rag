from datetime import datetime

from pdf2image import convert_from_path
from PIL import Image

from ..config import RAW_DATA_IMAGE_DIR, RAW_DATA_TEXT_DIR, RAW_DATA_PDF_DIR, PROCESSED_DATA_DIR
from ..prompts import TEXT_PROMPT, IMAGE_PROMPT
from ..clients import generate_content

class DocumentProcessor:
    """A class to process various types of documents and generate content using the Gemini API."""
    @staticmethod
    def process(file_name: str) -> None:
        """Determine the type of the file and process it accordingly.
        
        Args:
            file_name (str): The name of the file to process.
        
        Returns:
            None: The generated content is saved to a text file.
        """
        if file_name.endswith((".txt", ".md")):
            DocumentProcessor.process_text(file_name)
        elif file_name.endswith((".jpg", ".jpeg", ".png")):
            DocumentProcessor.process_image(file_name)
        elif file_name.endswith(".pdf"):
            DocumentProcessor.process_pdf(file_name)
        else:
            raise ValueError(f"Unsupported file type: {file_name}")
    
    @staticmethod
    def process_text(file_name: str) -> None:
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
        DocumentProcessor.__save_response(response)

    @staticmethod
    def process_image(file_name: str) -> None:
        """Process an image file and generate content using the Gemini API.
        
        Args:
            file_name (str): The name of the image file to process.
        
        Returns:
            None: The generated content is saved to a text file.
        """
        # Open the image file
        image = Image.open(RAW_DATA_IMAGE_DIR / file_name)

        if image.mode != "RGB":
            image = image.convert("RGB")

        # Generate content using the Gemini API
        prompt = (IMAGE_PROMPT, image)
        response = generate_content(prompt)
        DocumentProcessor.__save_response(response)

    @staticmethod
    def process_pdf(file_name: str) -> None:
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
        DocumentProcessor.__save_response(response)

    @staticmethod
    def __save_response(response: str) -> None:
        """Save the generated response to a text file with a timestamped name.
        
        Args:
            response (str): The content to save.
        
        Returns:
            None: The content is saved to a text file.
        """
        # Generate timestamped file name
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file_name = PROCESSED_DATA_DIR / f"{now}.txt"

        # Save the response to a text file
        with open(output_file_name, "w") as f:
            f.write(response)