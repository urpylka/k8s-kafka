#! /bin/bash

KDIR=/k8s

NODES=(); +(){ NODES=(${NODES[@]} ${@}); }

+ 172.16.20.12
+ 172.16.20.13

for node in "${NODES[@]}"; do
    while ! ping -c 1 -n -w 1 ${node} &> /dev/null
    do
        sleep 1
        printf "%c" "."
    done
    echo ""
    echo "> Node ${node} is available"
done

echo "> All nodes is available"

for node in "${NODES[@]}"; do
    while ! gluster peer probe ${node} &> /dev/null
    do
        sleep 1
        printf "%c" "."
    done
    echo ""
    echo "> Node ${node} has been joined to glusterfs"
done

echo "> Gluster nodes have been joined"

gluster peer status

# gluster volume create main replica 2 172.16.20.12:/gluster/main 172.16.20.13:/gluster/main force

gluster volume create volume01 172.16.20.12:/gluster/volume01 force
gluster volume start volume01
gluster volume status volume01
gluster volume create volume02 172.16.20.13:/gluster/volume02 force
gluster volume start volume02
gluster volume status volume02
gluster volume create volume03 172.16.20.12:/gluster/volume03 force
gluster volume start volume03
gluster volume status volume03
gluster volume create volume04 172.16.20.13:/gluster/volume04 force
gluster volume start volume04
gluster volume status volume04
gluster volume create volume05 172.16.20.12:/gluster/volume05 force
gluster volume start volume05
gluster volume status volume05
gluster volume create volume06 172.16.20.13:/gluster/volume06 force
gluster volume start volume06
gluster volume status volume06
gluster volume create volume07 172.16.20.12:/gluster/volume07 force
gluster volume start volume07
gluster volume status volume07
gluster volume create volume08 172.16.20.13:/gluster/volume08 force
gluster volume start volume08
gluster volume status volume08
gluster volume create volume09 172.16.20.12:/gluster/volume09 force
gluster volume start volume09
gluster volume status volume09
gluster volume create volume10 172.16.20.13:/gluster/volume10 force
gluster volume start volume10
gluster volume status volume10

echo "> Login vagrant"



echo "> Gluster volumes have been setup"

kubectl version

while ! kubectl get all -A &> /dev/null
do
    sleep 1
    printf "%c" "."
done
echo ""

kubectl get all -A

echo "> Apply solution"

kubectl apply -k ${KDIR}

echo "> The solution has been enabled"
