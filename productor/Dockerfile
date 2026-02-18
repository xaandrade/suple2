FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Estructura hexagonal: app.infrastructure.api
CMD ["uvicorn", "app.infrastructure.api:app", "--host", "0.0.0.0", "--port", "8000"]