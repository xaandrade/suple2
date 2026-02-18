FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Arrancamos el script que escucha Kafka
CMD ["python", "-m", "app.application.services"]