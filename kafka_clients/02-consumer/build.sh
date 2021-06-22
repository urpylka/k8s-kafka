#! /usr/bin/env bash

docker build . -t urpylka/kafka-consumer:latest
docker push urpylka/kafka-consumer:latest