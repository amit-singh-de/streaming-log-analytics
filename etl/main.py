from logGenerator import generate_log
from producer import KafkaProducer
import time


def main():

    # set kafka server address
    bootstrap_server = "localhost:9095"
    # set kafka topic name
    topic= "logs"
    #instantiate kafkaProducer
    producer = KafkaProducer(bootstrap_server)

    # we will stream records for 1 mins only
    start_time = time.time()
    while time.time() - start_time<60:
        # create a fake log record
        message = generate_log()
        # send the fake log record to kafka
        producer.send_to_kafka(topic,message)
        # poll to ensure the message is sent
        producer.poll()
    # flush messages to ensure they are sent
    producer.flush()




if __name__ == "__main__":
    main()