from ..config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str) -> list:
    """
    Splits the input text into chunks of specified size with overlap.

    Args:
        text (str): The input text to be chunked.

    Returns:
        list: A list of text chunks.
    """

    if not text:
        return [""]
    
    text = text.strip()

    if len(text) <= CHUNK_SIZE:
        return [text]
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE

        if end >= len(text):
            chunks.append(text[start:])
            break

        # Find chunk end while respecting word boundaries
        # Try to find the last space to the left of the end index
        last_space = text.rfind(' ', start, end)

        # If a space is found and it's within the current chunk, use it as the end of the chunk
        if last_space != -1 and last_space > start:
            new_end = last_space
        else:
            # If no space is found, try to find the next space to the right of the end index
            next_space = text.find(' ', end)
            if next_space != -1:
                new_end = next_space
            else:
                # No space found anywhere, take the rest of the text
                new_end = len(text)
        
        end = new_end
        
        # Extract the chunk
        extracted_chunk = text[start:end].strip()
        if extracted_chunk:
            chunks.append(extracted_chunk)
        
        # Find next start while respecting overlap and word boundaries
        next_start = end - CHUNK_OVERLAP

        if next_start <= start:
            next_start = end + 1
        else:
            # Try to find the next space to the left of the next start index
            last_space = text.rfind(' ', end, next_start)
            if last_space != -1 and last_space > start:
                next_start = last_space + 1
            else:
                # If no space is found, try to find the next space to the right of the next start index
                next_space = text.find(' ', next_start)
                if next_space != -1:
                    next_start = next_space + 1
                    
                # If no space is foudn, just use the next start index as is 
        
        start = next_start
    
    return chunks

        