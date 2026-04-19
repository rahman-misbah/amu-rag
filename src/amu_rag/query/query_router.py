from datetime import datetime
import json

from ..prompts import FILTER_EXTRACTION_PROMPT
from ..clients import ollama_generate

def filter_extraction_prompt(query: str) -> str:
    """Generate a prompt for extracting filters from a query.
    Args:
        query (str): The user query for which to extract filters.
    
    Returns:
        str: The generated prompt for filter extraction.
    """

    return FILTER_EXTRACTION_PROMPT.replace("{QUESTION}", query).replace("{DATE}", datetime.now().strftime("%Y-%m-%d"))

def filter_extraction(query: str) -> dict:
    """Extract filters from a user query using the filter extraction prompt.
    Args:
        query (str): The user query for which to extract filters.
    
    Returns:
        dict: A dictionary containing the extracted filters.
    """

    prompt = filter_extraction_prompt(query)
    response = ollama_generate(prompt)
    
    # Assuming the response is a JSON string containing the extracted filters
    try:
        features = json.loads(response)
        return features
    except json.JSONDecodeError:
        raise ValueError("Failed to decode the response as JSON. Response: " + response)