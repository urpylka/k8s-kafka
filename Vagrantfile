# coding: utf-8
# -*- mode: ruby -*-

N = 3

Vagrant.configure(2) do |config|
  (1..N).each do |i|

    if i == 1 then
      vm_name = "master"
    else
      vm_name = "node#{i-1}"
    end

    config.vm.define vm_name do |s|
      s.vm.box = "ubuntu/xenial64"
      s.vm.hostname = vm_name

      #s.vm.network :forwarded_port, host: 4040, guest: 4040
      #if i == 1 then
      #  s.vm.network :forwarded_port, host: 8001, guest: 8001
      #end

      private_ip = "172.16.20.#{i+10}"
      s.vm.network "private_network", ip: private_ip

      # public_ip = "192.168.1.#{i+90}"
      # s.vm.network :public_network, ip: public_ip, bridge: "en0: Ethernet"

      s.vm.provider "virtualbox" do |v|
        v.gui = false
        if i == 1 then
          # Params for the master node
          v.cpus = 2
          v.memory = 2048
        else
          v.cpus = 1
          v.memory = 1024
        end
      end

      s.vm.provision "ansible_local" do |p|
        p.playbook = "ansible/playbook.yml"
        p.install_mode = "pip3"
        p.version = "2.9.22"
        p.verbose = true
        p.extra_vars =
        {
            network_cidr: "10.244.0.0/16",
            cluster_dns: "10.244.0.10",
            private_ip: private_ip,
            vm_name: vm_name
        }
      end

    end
  end

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
end
