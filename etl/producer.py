from confluent_kafka import Producer
import json


class KafkaProducer:
    def __init__(self, bootstrap_server):
        self.producer = Producer({'bootstrap.servers': bootstrap_server})

    # Delivery report callback
    def delivery_report(self,err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to topic {msg.topic()} [{msg.partition()}]')

    def send_to_kafka(self, topic, message):
        """
        Sends a record to the specified Kafka topic.
        :param topic: Kafka topic to send the record to.
        :param record: Record to be sent to Kafka.
        """
        # Produce the record
        self.producer.produce(topic, value=json.dumps(message), callback=self.delivery_report)

    def poll(self):
        # ensure the message is sent
        self.producer.poll(0)

    def flush(self):
        # Flush messages to ensure they are sent
        self.producer.flush()

