#!/usr/bin/env python3

from kafka import KafkaProducer

bootstrap_servers = ['kafka-hs.default.svc.cluster.local:9092']
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, api_version=(0, 10))
topicName = 'input'

ack = producer.send(topicName, b'Hello World!', b'timestamp')
producer.flush()
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
