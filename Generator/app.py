import random
import time
from kafka import KafkaProducer

class GENERATOR:
    def __init__(self, bootstrap_servers='kafka:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: v.encode('utf-8')
        )
        self.topics = ['tenant-1', 'tenant-2']

    def generate_message(self):
        return f"msg-{random.randint(1000, 9999)}"

    def run(self):
        while True:
            topic = random.choice(self.topics)
            message = self.generate_message()

            print(f"[GENERATOR] Sending '{message}' to {topic}")
            self.producer.send(topic, message)

            time.sleep(random.uniform(0.5, 2))


if __name__ == "__main__":
    gen = GENERATOR()
    gen.run()