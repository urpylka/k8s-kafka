#! /usr/bin/env bash

docker build . -t urpylka/kafka-producer:latest
docker push urpylka/kafka-producer:latest