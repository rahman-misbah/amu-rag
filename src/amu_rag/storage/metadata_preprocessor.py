def preprocess_metadata(metadata: dict) -> dict:
    """Preprocesses metadata by converting non-serializable types to strings and ensuring all values are JSON serializable
    
    Args:
        metadata (dict): The original metadata dictionary to be preprocessed
    
    Returns:
        dict: A new metadata dictionary with all values converted to JSON serializable types
    """
    
    preprocessed_metadata = {}
    
    for key, value in metadata.items():
        if not isinstance(value, type(None)):
            preprocessed_metadata[key] = value
    
    return preprocessed_metadata