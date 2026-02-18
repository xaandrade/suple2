from app.infrastructure.kafka_consumer import KafkaConsumerAdapter

if __name__ == "__main__":
    consumer = KafkaConsumerAdapter()
    consumer.listen()