# Large Language Model Utilities: llmutil

This project is a RESTful wrapper for LLM functionalities.

## Build with Docker

From the root of the project

```bash
docker build -t gnames/llmutil:latest .
```
## Usage

```bash
docker run -d -p 8000:8000 gnames/llmutil:latest
```

## API endpoints

### `/api/v1/embed`

Takes POST with

```json
{
  "texts": [
    "first text",
    "second text",
    ...
  ]
}
```

Response contains an array of embeddings with 384-dimentional vectors.