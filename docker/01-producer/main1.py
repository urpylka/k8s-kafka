#!/usr/bin/env python3

# sudo apt install python3 python3-pip
# sudo pip3 install kafka-python prometheus-client

import time, sys
from datetime import datetime
from kafka import KafkaProducer
from prometheus_client import start_http_server
from prometheus_client import Counter

c1 = Counter('my_successfuls', 'Description of counter my_successfuls')
c2 = Counter('my_failures', 'Description of counter my_failures')

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        c1.inc()
        # print('Message published successfully.')
    except Exception as ex:
        c2.inc()
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(kafka):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=[kafka], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def main(delay, kafka):
    prod = connect_kafka_producer(kafka)



    while(True):
        try:
            timestamp = datetime.today().timestamp()
            publish_message(prod, "input", "timestamp", str(timestamp))
            time.sleep(delay)
        except Exception:
            time.sleep(delay)

if __name__ == '__main__':

    print("Producer has been started.")

    kafka = "kafka-hs.default.svc.cluster.local:9092"
    prome = 8001
    delay = 10

    if len(sys.argv) == 4:
        kafka = sys.argv[1]
        prome = int(sys.argv[2])
        delay = float(sys.argv[3])

    print("kafka = " + str(kafka))
    print("prome = " + str(prome))
    print("delay = " + str(delay))

    start_http_server(prome)

    while(True):
        try:
            main(delay, kafka)
        except(KeyboardInterrupt, SystemExit):
            pass
