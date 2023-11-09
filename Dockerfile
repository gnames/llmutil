FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production

EXPOSE 8000

CMD ["gunicorn", "llmutil.py", "-b", "0.0.0.0:8000"]

