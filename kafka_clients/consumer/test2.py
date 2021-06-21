#!/usr/bin/env python3

from kafka import KafkaConsumer
import sys

bootstrap_servers = ['kafka-hs.default.svc.cluster.local:9092']
topicName = 'input'
consumer = KafkaConsumer(topicName, group_id = 'group1', bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')

print("Wait messages:")

for msg in consumer:
    print(str(msg))
