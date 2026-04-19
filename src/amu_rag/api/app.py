"""FastAPI endpoint for RAG query interface."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

from ..query import generate_answer

app = FastAPI(
    title="AMU RAG API",
    description="API for the AMU RAG system to handle user queries and generate answers based on retrieved context.",
    version="1.0.0",
)

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500, description="The user's query to be processed by the RAG system.")

    class Config:
        json_schema_extra = {
            "example": {
                "query": "What are the key features of the latest iPhone model?"
            }
        }

class QueryResponse(BaseModel):
    question: str = Field(..., description="The original user query.")
    answer: str = Field(..., description="The generated answer based on the retrieved context.")

class HealthResponse(BaseModel):
    status: str
    version: str
    vector_db_status: str

# API Endpoints
@app.get("/",tags=["Health"])
async def root():
    """Root endpoint with basic info"""
    return {
        "message": "AMU RAG Assistant API",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint to verify API and vector database status."""
    # Here you would typically check the status of your vector database and other dependencies
    vector_db_status = "OK"  # Placeholder for actual status check
    return HealthResponse(
        status="OK",
        version="1.0.0",
        vector_db_status=vector_db_status
    )

@app.post("/query", response_model=QueryResponse, tags=["Query"])
async def handle_query(request: QueryRequest):
    """Endpoint to handle user queries and return generated answers."""
    try:
        answer = generate_answer(request.query)
        return QueryResponse(question=request.query, answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))