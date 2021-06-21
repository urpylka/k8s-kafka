FROM debian:buster

RUN apt update

RUN apt install -y python3 python3-pip nano kafkacat ipython3

RUN pip3 install kafka-python prometheus-client rfc3339

EXPOSE 8002

COPY main2.py /main2.py

CMD [ "sh", "python3", "/main2.py" ]