#!/usr/bin/env python
"""Launcher script for the AMU RAG API."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.amu_rag.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )