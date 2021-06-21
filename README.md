# Kubernetes cluster

## Instructions

Instalation

```bash
brew install ansible vargant vagrant-manager virtualbox virtualbox-extension-pack
```

Problem: Failed to create the host only adapter ([stackoverflow.com](https://stackoverflow.com/questions/21069908/vboxmanage-error-failed-to-create-the-host-only-adapter)).

https://devops.stackexchange.com/questions/5898/how-to-get-kubernetes-pod-network-cidr
kubectl get nodes -o jsonpath='{.items[*].spec.podCIDR}'

https://stackoverflow.com/questions/50833616/kube-flannel-cant-get-cidr-although-podcidr-available-on-node

```bash
git clone https://github.com/urpylka/evolution-test.git
cd evolution-test

vagrant up
```

## Notes

Ещё одна ошибка https://github.com/Azure/vscode-kubernetes-tools/issues/880

```log
error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'
```

Kubernetes DNS

* [medium.com](https://medium.com/kubernetes-tutorials/kubernetes-dns-for-services-and-pods-664804211501)
* [unofficial-kubernetes.readthedocs.io](https://unofficial-kubernetes.readthedocs.io/en/latest/concepts/services-networking/dns-pod-service/)
* [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
* [DNS in Pods, Service](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
* [Custom DNS](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)
* []()
* []()
* []()
* []()
* []()

Kubernetes instructions:

* [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
* [Persistent Volumes](https://rtfm.co.ua/kubernetes-persistentvolume-i-persistentvolumeclaim-obzor-i-primery/)
* [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
* [Persistent Volumes](https://serveradmin.ru/hranilishha-dannyh-persistent-volumes-v-kubernetes/)
* [Resources](https://ealebed.github.io/posts/2019/ресурсы-в-kubernetes-часть-1-memory/)
* [StatefulSet](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)
* [Operator framework](https://m.habr.com/ru/company/lamoda/blog/446648/)
* []()
* []()
* []()
* []()

Deprecated API

https://kubernetes.io/blog/2019/07/18/api-deprecations-in-1-16/
https://stackoverflow.com/questions/59480373/validationerror-missing-required-field-selector-in-io-k8s-api-v1-deploymentsp

Настройка glusterfs

* https://losst.ru/nastrojka-glusterfs
* https://russianblogs.com/article/112646342/
* https://delfer.ru/2017/10/20/kubernetes-и-glusterfs/ (heketi)
* https://github.com/psyhomb/heketi
* https://cloud.croc.ru/blog/byt-v-teme/kubernetes-ispolzovanie-sovmestno-s-glusterfs/
* https://dougbtv.com/nfvpe/2017/04/05/glusterfs-persistent/
* https://habr.com/ru/post/498160/

```bash
sudo gluster volume create volume0 172.16.20.11:/gluster/volume0 force
sudo gluster volume create volume1 172.16.20.12:/gluster/volume1 force
sudo gluster volume create volume2 172.16.20.13:/gluster/volume2 force
sudo gluster volume create volume3 172.16.20.12:/gluster/volume3 force
sudo gluster volume create volume4 172.16.20.13:/gluster/volume4 force
```

https://github.com/cloudhut/kminion
https://itsecforu.ru/2020/01/28/☸%EF%B8%8F-как-настроить-grafana-на-kubernetes/
https://github.com/obsidiandynamics/kafdrop


https://habr.com/ru/company/X5RetailGroup/blog/539396/

dig kafka.default.svc.cluster.local @10.96.0.10

cука
https://github.com/kubernetes/kubernetes/issues/60835

Kafka + Zookeeper

* https://github.com/kow3ns/kubernetes-zookeeper
* https://kow3ns.github.io/kubernetes-kafka/manifests/

Проблема с kafka by Yolean https://github.com/Yolean/kubernetes-kafka/issues/300

https://yandex.ru/search?clid=1906725&text=ERROR:+%27~ansible%27+user+or+team+does+not+exist.

Поднятие кластера [eternalhost.net](https://eternalhost.net/blog/razrabotka/kubernetes-chto-eto), [digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-cluster-using-kubeadm-on-ubuntu-18-04-ru)

Шпаргалка по k8s [kubernetes.io](https://kubernetes.io/ru/docs/reference/kubectl/cheatsheet/).

Flannel [github.com](https://github.com/flannel-io/flannel).

Проблема со Flannel [github.com](https://github.com/flannel-io/flannel/issues/671).

https://stackoverflow.com/questions/50833616/kube-flannel-cant-get-cidr-although-podcidr-available-on-node

```log
Error registering network: failed to acquire lease: node "master" pod cidr not assigned
```

**RBAC** (Role Based Access Control) – Модуль k8s используемых для разделения прав для работы с ресурсами. Подробнее [тут](https://habr.com/ru/company/flant/blog/422801/).

**Kustomize** – встроенное средство для объединения конфигураций и их перегрузки. Подробнее [тут](https://habr.com/ru/company/flant/blog/469179/) и [тут](https://kustomize.io).

Операторы в k8s используются для слежением и сохранения состояния. Например `etcd`. Подробнее [тут](https://habr.com/ru/company/flant/blog/326414/).

**kafka** in kubernetes

* https://habr.com/ru/post/515584/
* https://github.com/Yolean/kubernetes-kafka
* https://habr.com/ru/company/piter/blog/462257/
* https://www.bigdataschool.ru/blog/kafka-kubernetes-big-data-devops.html
* https://medium.com/accenture-the-dock/when-how-to-deploy-kafka-on-kubernetes-b18f5270db63

**kubespray** – Подробнее на [официальном сайте](https://kubespray.io).

**k3s** https://habr.com/ru/company/southbridge/blog/551214/

**microk8s** by Canonical – программный пакет включающий в себя `kubelet`, `kubectl`, `kubeadm`, `docker` и все что необходимо для поднятия собстевенного k8s-кластера. Основной вид поставки `microk8s` snap-пакеты в Ubuntu, но также есть реализации для Windows & macOS. Особенностью `microk8s` является то, что k8s-нода запускается внутри docker (а не на хосте). Также `microk8s` содержит множество готовых плагинов, например DNS-сервер, метрики для ELK, storage-плагин. Подробнее на [официальном сайте](https://microk8s.io/#quick-start).

Помимо **microk8s** есть **minikube**. Основное отличие `minikube` – использование виртуальной машины, а не контейнера для создания ноды.

**helm** – пакетный менеджер для Kubernetes. Подробнее на [официальном сайте](https://helm.sh).

**vagrant** by Hashicorp – утилита для создания и настройки виртуальных машин без GUI. Использует `Vagrantfile` на Ruby для описания создаваемых машин. Подробнее на [официальном сайте](https://www.vagrantup.com/).

Текущая версия LTS [Ubuntu](https://ubuntu.com/#download) – 20.04.

As of Ansible 2.9, sudo is no longer a valid keyword type. If you change that to become: yes things should start working. This will have to be done throughout all of your tasks. https://github.com/ansible/ansible/issues/65700

Есть разные способы настройки системы в Vagrant, помимо ansible и ansible_local можно использовать такие варианты:

```ruby
config.vm.provision "file", source: "./ansible/files/script.sh", destination: "/script.sh"
config.vm.provision "shell", inline: "/script.sh"

config.vm.provision "bootstrap", type: "shell", path: "./ansible/files/script.sh"

config.vm.provision "shell", inline: <<-EOF <some_code_here> EOF
```

Проблема с container-runtimes:

* [gist.github.com](https://gist.github.com/iamcryptoki/ed6925ce95f047673e7709f23e0b9939)
* [stackoverflow.com](https://stackoverflow.com/questions/54059636/ansible-failed-to-reload-sysctl-sysctl-cannot-stat-proc-sys-net-bridge-bridg)
* [kubernetes.io](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

Проблема с `--extra-config=kubelet.cgroup-driver=systemd` [stackoverflow.com](https://stackoverflow.com/questions/45708175/kubelet-failed-with-kubelet-cgroup-driver-cgroupfs-is-different-from-docker-c)

Flannel yaml [github.com](https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml)

## Источники

* [habr.com](https://habr.com/ru/post/439734/): microk8s, django
* [darkfess.ru](https://darkfess.ru/microk8s-kompose-helm/): microk8s, kompose, helm
* [gist.github.com](https://gist.github.com/maxivak/c318fd085231b9ab934e631401c876b1): virtualbox, vagrant, ansible
* [habr.com](https://habr.com/ru/company/southbridge/blog/455290/): prometheus
* [github.com](https://github.com/takara9/vagrant-k8s): virtualbox, vagrant, k8s
* [github.com](https://github.com/adidenko/vagrant-k8s): vagrant, ansible, k8s
* [docs.ansible.comdocs.ansible.com](https://docs.ansible.com/ansible/latest/user_guide/become.html): ansible become
* [ealebed.github.io](https://ealebed.github.io/posts/2017/ansible-ввод-sudo-пароля-при-выполнении-playbook/): ansible vault
* [vagrantup.com](https://www.vagrantup.com/docs/provisioning/ansible_local): vagrant + ansible_local
* [docs.ansible.com](https://docs.ansible.com/ansible/2.9/modules/systemd_module.html) + [docs.ansible.com](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/systemd_module.html): ansible + systemd module
* [habr.com](https://habr.com/ru/company/flant/blog/332432/): k8s, flannel, ipvlan
