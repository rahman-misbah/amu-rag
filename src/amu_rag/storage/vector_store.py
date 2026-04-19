from typing import List, Dict, Optional, Any

import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings

from ..config import CHROMA_PERSISTENT_DIR, CHROME_COLLECTION_NAME

class VectorStore:
    """Wrapper for ChromaDB vector database operations"""

    def __init__(self):
        """Initializes the ChromaDB client and collection"""

        # Create persistent client
        self.client = chromadb.PersistentClient(path=str(CHROMA_PERSISTENT_DIR), settings=Settings(anonymized_telemetry=False))

        # Define embedding function
        # Local embedding model
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name=CHROME_COLLECTION_NAME,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_documents(self, documents: List[str], metadatas: List[Dict[str, Any]], ids: List[str]) -> None:
        """Adds documents to the vector store with associated metadata and IDs
        
        Args:
            documents (List[str]): List of document texts to be added to the vector store
            metadatas (List[Dict[str, Any]]): List of metadata dictionaries corresponding to each document
            ids (List[str]): List of unique IDs for each document
        
        Returns:
            None
        """
        
        if not documents:
            return
        
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def search(self, query: str, n_results: int = 5, where_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Searches the vector store for relevant documents based on the query and optional filters
        Args:
            query (str): The search query to find relevant documents
            n_results (int, optional): The number of top results to return (default is 5)
            where_filter (Dict[str, Any], optional): Optional filter to narrow down search results based on metadata (default is None)
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the relevant documents and their metadata
        """
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter
        )
        
        return results
    
    def get_collection_info(self) -> Dict[str, Any]:
        """Retrieves information about the current collection in the vector store
        
        Returns:
            Dict[str, Any]: A dictionary containing information about the collection, such as number of documents and metadata
        """
        
        info = {
            "name": self.collection.name,
            "count": self.collection.count(),
            "metadata": self.collection.metadata
        }

        return info

    def delete_collection(self) -> None:
        """Deletes the entire collection from the vector store (use with caution)"""
        
        self.client.delete_collection(name=CHROME_COLLECTION_NAME)
    
    def reset(self) -> None:
        """Resets the vector store by deleting and recreating the collection (use with caution)"""
        try:
            self.delete_collection()
        except:
            pass
        
        self.collection = self.client.get_or_create_collection(
            name=CHROME_COLLECTION_NAME,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )