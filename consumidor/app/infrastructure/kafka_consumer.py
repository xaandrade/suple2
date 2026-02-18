import json
from confluent_kafka import Consumer
# Importamos el adaptador correcto basado en tus archivos reales
from .mongo_adapter import MongoAdapter 

class KafkaConsumerAdapter:
    def __init__(self):
        self.consumer = Consumer({
            'bootstrap.servers': 'kafka:9092',
            'group.id': 'xavier-final-group', # Cambiamos el grupo para asegurar lectura
            'auto.offset.reset': 'earliest'
        })
        # Usamos el tópico que confirmamos con el comando anterior
        self.consumer.subscribe(['suple-topic'])
        self.db = MongoAdapter()

    def listen(self):
        print("Escuchando Kafka en 'suple-topic'...")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Error de Kafka: {msg.error()}")
                continue

            try:
                # 1. Decodificar el valor del mensaje
                raw_value = msg.value().decode('utf-8')

                # 2. Validar si el mensaje no está vacío
                if not raw_value or raw_value.strip() == "":
                    print("Se recibió un mensaje vacío, ignorando...")
                    continue

                # 3. Intentar convertir a JSON
                data = json.loads(raw_value)

                # 4. Guardar en MongoDB usando el método del adaptador
                self.db.save_data(data)
                print(f"Mensaje procesado y guardado con éxito: {data}")

            except json.JSONDecodeError:
                print(f"Error: El mensaje no tiene formato JSON válido: {raw_value}")
                continue
            except Exception as e:
                print(f"Error inesperado procesando mensaje: {e}")
                continue

    def close(self):
        self.consumer.close()