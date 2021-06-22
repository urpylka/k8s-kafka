# Kubernetes cluster

## Quick Start

Install `virtualbox` and `vagrant` by method you preffer. There is an example at macOS by `brew` below.

```bash
brew install ansible vargant vagrant-manager virtualbox virtualbox-extension-pack
```

Download or clone the solution and change directory:

```bash
git clone https://github.com/urpylka/k8s-kafka.git
cd k8s-kafka
```

For setup cluster and switch on the solution use `vagrant up`. Most common command you can find below:

```bash
# Setup & switch on
vagrant up

# Switch off
vagrant suspend

# Remove virtual machines (force)
vagrant destroy -f
```

After all machines setup it will take some time (usualy 5 mins) to pull and start all service to Kubernetes. You can check status by:

```bash
# Connect to master machine
vagrant ssh master

# Get common information about cluster
kubectl get all

# Check setup.log
cat /k8s/setup.log
```

After there are next interfaces from the host machine.

* [Grafana](http://172.16.20.11:32000) (http://172.16.20.11:32000)
* [Prometheus](http://172.16.20.11:32090) (http://172.16.20.11:32090)

You can open `Grafana` by default user/password (admin/admin). There will be available two dashboard:

* `Kminion` with information about Kafka broker
* `Business Logic` with metrics from `producer` & `consumer`. Theese metrics show how many messages will be produced and processed after.

![image](./kminion.png)

![image](./business.png)

![image](./prometheus.png)

## Next

To get more fun at the graphics you can delete & add `consumer` or `producer` node separately. Connect to the master. And execute one of the next command:

```bash
kubectl delete -f /k8s/71-producer.yaml
kubectl delete -f /k8s/72-consumer.yaml
kubectl apply -f /k8s/71-producer.yaml
kubectl apply -f /k8s/72-consumer.yaml
```

Also you can change message per second delay in `producer`. Last parametr in command section in `/k8s/71-producer.yaml`. By default it is 10 sec. You can set with another value.

Dev notes you can [here](./devnotes.md).

## Possible upgrade

* Add `kafdrop` for looking topics and messages.
* Add `jmx-exporter` to Kafka image to get more metrics.
* Setup limits (cpu, mem) to more compitable machine.

___
MIT License
Copyright (c) 2021 Artem Smirnov
