<div align="center">

<pre>
 █████╗ ███╗   ███╗██╗   ██╗      ██████╗  █████╗  ██████╗ 
██╔══██╗████╗ ████║██║   ██║      ██╔══██╗██╔══██╗██╔════╝ 
███████║██╔████╔██║██║   ██║█████╗██████╔╝███████║██║  ███╗
██╔══██║██║╚██╔╝██║██║   ██║╚════╝██╔══██╗██╔══██║██║   ██║
██║  ██║██║ ╚═╝ ██║╚██████╔╝      ██║  ██║██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
</pre>

### **Context-Aware RAG Assistant for Aligarh Muslim University**

*Multi-Modal Ingestion · Local-First RAG · Structured Document Understanding*

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136.0-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-1.5.8-FF6B35?style=for-the-badge)](https://www.trychroma.com/)
[![Ollama](https://img.shields.io/badge/Ollama-0.6.1-black?style=for-the-badge)](https://ollama.ai/)
[![Transformers](https://img.shields.io/badge/Transformers-4.57.6-FFCC00?style=for-the-badge)](https://huggingface.co/docs/transformers/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.11.0-EE4C2C?style=for-the-badge\&logo=pytorch\&logoColor=white)](https://pytorch.org/)
[![LangChain Core](https://img.shields.io/badge/LangChain_Core-1.3.0-1C3C3C?style=for-the-badge)](https://python.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Gemini-API_\(google--genai_1.73.1\)-4285F4?style=for-the-badge\&logo=google\&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)


</div>

---

## 📌 What is AMU-RAG?

**AMU-RAG** is a modular Retrieval-Augmented Generation (RAG) system designed for institutional knowledge at **Aligarh Muslim University**.

It focuses on transforming **raw, messy documents** (PDFs, images, notices) into:

* structured metadata
* clean summaries
* retrieval-ready text

…and enabling **accurate, local-first question answering** over that data.

> **Design Principle:**
> Gemini is used once during ingestion. All querying and reasoning happens locally via Ollama.

---

## ✨ Core Capabilities

| Capability                 | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| 🖼️ Multi-Modal Processing | Handles `.txt`, `.md`, `.pdf`, `.jpg`, `.png`        |
| 🧠 Structured Extraction   | Converts documents → metadata + normalized summaries |
| 🔍 Semantic Retrieval      | ChromaDB + embeddings for similarity search          |
| 🧩 Modular Design          | Clear separation: ingestion → processing → retrieval |
| 🔒 Local-First Querying    | No external calls during inference                   |
| ⚙️ Config-Driven           | Environment-based configuration                      |

---

## 🏗️ System Overview

```mermaid
graph TB
    A[Raw Documents] --> B[DocumentProcessor]
    B --> C[Gemini 2.5 Flash]
    C --> D[Structured Output]
    D --> E[Processed Text Files]

    E --> F[Chunker]
    F --> G[Embeddings]
    G --> H[ChromaDB]

    Q[User Query] --> I[Ollama]
    I --> H
    H --> I
    I --> R[Response]
```

---

## 📂 Project Structure

```
amu-rag/
│
├── src/amu_rag/
│   ├── config.py
│   │
│   ├── clients/
│   │   ├── gemini_client.py
│   │   └── ollama_client.py
│   │
│   ├── processing/
│   │   ├── document_processor.py
│   │   └── response_parser.py
│   │
│   ├── ingestion/
│   │   └── chunker.py
│   │
│   └── prompts/
│       ├── text_prompt.txt
│       └── image_prompt.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
└── README.md
```

---

## 🔄 Document Processing

Each document goes through:

1. **Type Detection**
2. **Conversion (if needed)**

   * PDFs → images (`pdf2image`)
3. **LLM Extraction (Gemini)**
4. **Structured Parsing**
5. **Saved Output**

### Output Format

```txt
---METADATA---
{ ... }

---SUMMARY---
Clean natural language summary
```

---

## 🧩 Metadata Schema

```json
{
  "doc_type": "notice",
  "issue_date": "YYYY-MM-DD",
  "effective_date": null,
  "deadline": null,
  "expires": false,
  "target_audience": ["students"]
}
```

---

## ⚙️ Configuration

```bash
cp .env.example .env
```

| Variable        | Description                      |
| --------------- | -------------------------------- |
| GEMINI_API_KEY  | Required for document processing |
| GEMINI_MODEL    | Default: gemini-2.5-flash        |
| OLLAMA_MODEL    | Default: llama3.2                |
| OLLAMA_BASE_URL | Local Ollama endpoint            |

---

## 🚀 Getting Started

### 1. Setup

```bash
git clone https://github.com/rahman-misbah/amu-rag.git
cd amu-rag

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Start Ollama

```bash
ollama pull llama3.2
```

### 3. Configure

```bash
cp .env.example .env
```

Add your Gemini API key.

---

### 4. Process Documents

```python
from src.amu_rag.processing.document_processor import DocumentProcessor

DocumentProcessor.process("notice.pdf")
```

---

## 🧠 Chunking Strategy

* Chunk size: **800 characters**
* Overlap: **160 characters**
* Word-boundary aware

This preserves semantic continuity for embeddings.

---

## 🤖 Model Roles

| Model              | Role                        |
| ------------------ | --------------------------- |
| Gemini 2.5 Flash   | Extraction + structuring    |
| Llama 3.2 (Ollama) | Local reasoning + answering |

---

## 📊 Current Scope

✅ Implemented:

* Document ingestion (multi-modal)
* Structured extraction pipeline
* Chunking system

🚧 In Progress:

* Full RAG query pipeline
* API layer
* Ranking improvements

---

## 🤝 Contributing

```
feat/<name>
fix/<bug>
refactor/<scope>
docs/<update>
```

Standard GitHub flow:

* Fork
* Branch
* PR

---

## 📜 License

MIT License

---

<div align="center">

Built for Aligarh Muslim University

</div>
