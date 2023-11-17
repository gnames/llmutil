# Large Language Model Utilities: llmutil

This project is a RESTful wrapper for LLM functionalities.

## Usage


### Nvidia Container Toolkit

In case if there is an Nvidia GPU, you need Nvidia's docker toolkit

```bash
# on Arch
yay -S nvidia-container-toolkit
sudo systemctl restart docker
```

### Usage from Command Line 

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# to run tests
pytest

# for production
gunicorn --workers 1 --timeout 300 --bind 0.0.0.0:8000 main:app
```

### API endpoints

#### `/api/v1/embed`

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

## Usage with Docker

From the root of the project

```bash
docker build -t gnames/llmutil:latest .
```

Then run:

```bash
docker run -d --workers 1 --gpus all -p 8000:8000 gnames/llmutil:latest
```

Do not use `--gpus all` option if you do not have GPU.

## Testing

Tests are located in `tests` directory.
Install `pytest` and run:

```bash
pytest
```
