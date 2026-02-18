from confluent_kafka import Producer
import json

class KafkaAdapter:
    def __init__(self):
        # El host 'kafka' es el nombre del servicio en el docker-compose
        self.producer = Producer({'bootstrap.servers': 'kafka:9092'})

    def send_event(self, topic, data):
        self.producer.produce(topic, json.dumps(data).encode('utf-8'))
        self.producer.flush()