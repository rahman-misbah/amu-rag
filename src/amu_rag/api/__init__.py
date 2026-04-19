"""FastAPI application for RAG query interface."""

from .app import app, handle_query

__all__ = ["app", "handle_query"]