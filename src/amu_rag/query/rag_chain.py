from ..prompts import INFERENCE_PROMPT
from ..storage import VectorStore
from ..clients import ollama_generate

def generate_context(query: str) -> str:
    """Generates context for a given query using the INFERENCE_PROMPT template
    
    Args:
        query (str): The input query for which context needs to be generated
    
    Returns:
        str: The generated context based on the query
    """

    response = VectorStore().search(query)
    return "".join(response["documents"][0])

def generate_answer(query: str) -> str:
    """Generates an answer for a given query and context using the INFERENCE_PROMPT template
    
    Args:
        query (str): The input query for which an answer needs to be generated
        context (str): The context based on which the answer needs to be generated
    
    Returns:
        str: The generated answer based on the query and context
    """

    context = generate_context(query)
    prompt = INFERENCE_PROMPT.replace("{CONTEXT}", context).replace("{QUESTION}", query)

    response = ollama_generate(prompt)
    return response
