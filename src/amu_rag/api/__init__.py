"""FastAPI application for RAG query interface."""

from .app import app, ask_question

__all__ = ["app", "ask_question"]