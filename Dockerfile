
# Используем официальный Python образ
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ENV_FILE=.env.smarttest

CMD ["python", "main.py"]

