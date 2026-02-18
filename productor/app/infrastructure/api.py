
from fastapi import FastAPI
from app.infrastructure.kafka_adapter import KafkaAdapter

app = FastAPI()
kafka_bus = KafkaAdapter() # Llamada directa al adaptador

@app.post("/enviar/{msg}")
def publish_message(msg: str):
    payload = {"mensaje": msg, "remitente": "Xavier"}
    kafka_bus.send_event("suple-topic", payload)
    return {"status": "Enviado", "data": payload}