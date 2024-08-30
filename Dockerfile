FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
# Устанавливаем pre-commit если требуется использовать в контейнер
#RUN pip install pre-commit

# Устанавливаем pre-commit хуки если требуется использовать в контейнере
#RUN pre-commit install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
