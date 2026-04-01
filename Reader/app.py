from kafka import KafkaConsumer

class READER:
    def __init__(self, bootstrap_servers='kafka:9092'):
        self.consumer = KafkaConsumer(
            'tenant-1',
            'tenant-2',
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            group_id='my-group',
            value_deserializer=lambda v: v.decode('utf-8')
        )

    def run(self):
        print("[READER] Listening...")

        for message in self.consumer:
            print(f"[READER] Topic: {message.topic} | Value: {message.value}")


if __name__ == "__main__":
    reader = READER()
    reader.run()