from confluent_kafka import Consumer
import json
from app.infrastructure.mongo_adapter import MongoAdapter

class KafkaConsumerAdapter:
    def __init__(self):
        self.consumer = Consumer({
            'bootstrap.servers': 'kafka:9092',
            'group.id': 'suple-group',
            'auto.offset.reset': 'earliest'
        })
        self.db = MongoAdapter()

    def listen(self):
        self.consumer.subscribe(['suple-topic'])
        print("Escuchando Kafka...")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None: continue
            
            data = json.loads(msg.value().decode('utf-8'))
            self.db.save_data(data) # Aquí se comunica con la DB