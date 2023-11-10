FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

ENV FLASK_ENV=production

EXPOSE 8000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "main:app"]

