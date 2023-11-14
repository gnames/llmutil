# Large Language Model Utilities: llmutil

This project is a RESTful wrapper for LLM functionalities.

## Build with Docker

From the root of the project

```bash
docker build -t gnames/llmutil:latest .
```
## Usage

In case if there is an Nvidia GPU, you need Nvidia's docker toolkit

```bash
# on Arch
yay -S nvidia-container-toolkit
sudo systemctl restart docker
```

```bash
docker run -d --gpus all -p 8000:8000 gnames/llmutil:latest
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

### Usage without Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# for tests
python main.py

# for production
gunicorn --workers 1 --timeout 300 --bind 0.0.0.0:8000 main:app
```

## Testing

Tests are located in `tests` directory.
Install `pytest` and run:

```bash
pytest
```
