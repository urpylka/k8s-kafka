#!/usr/bin/env python3

# sudo apt install python3 python3-pip
# sudo pip3 install kafka-python prometheus-client rfc3339

import datetime, sys
from kafka import KafkaConsumer, KafkaProducer
from prometheus_client import start_http_server
from prometheus_client import Counter
from rfc3339 import rfc3339

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(kafka):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=[kafka], api_version=(0, 10))
        print("Producer connected.")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def main(delay, kafka):
    prod = connect_kafka_producer(kafka)
    consumer = KafkaConsumer("input", group_id = 'group1', bootstrap_servers = [kafka], auto_offset_reset = 'earliest')

    print("Consumer was set up:")

    for msg in consumer:
        # print(str(msg))
        if msg.key == b'timestamp':
            print(str(msg.value))
            d = datetime.datetime.fromtimestamp(float(msg.value))

            # What is correct format
            d = d.strftime('%Y-%m-%dT%H:%M:%SZ')
            # d = rfc3339(d)
            print(d)

            publish_message(prod, "output", "timestamp", str(d))
            c1.inc()

c1 = Counter('successfully_processed', 'Description of counter successfully_processed')

if __name__ == '__main__':

    print("Consumer has been started.")

    kafka = "kafka-hs.default.svc.cluster.local:9092"
    prome = 8001

    if len(sys.argv) == 4:
        kafka = sys.argv[1]
        prome = int(sys.argv[2])

    print("kafka = " + str(kafka))
    print("prome = " + str(prome))

    start_http_server(8002)
    kafka = "kafka-hs.default.svc.cluster.local:9092"
    while(True):
        try:
            main(kafka)
        except(KeyboardInterrupt, SystemExit):
            pass
