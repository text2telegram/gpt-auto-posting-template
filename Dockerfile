
# Используем официальный Python образ
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Запускаем основной скрипт
CMD ["python", "main.py"]
