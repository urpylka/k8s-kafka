# coding: utf-8
# -*- mode: ruby -*-

N = 3
master_ip = ""

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
        case i
        when 1
          # Params for the master node
          v.cpus = 2
          v.memory = 2048
        when 2
          v.cpus = 2
          v.memory = 2048
        when 3
          v.cpus = 1
          v.memory = 2048
        else
          v.cpus = 1
          v.memory = 1024
        end
      end

      if i == 1 then
        master_ip = private_ip
      else
        s.vm.provision "file", source: "./.vagrant/machines/master/virtualbox/private_key", destination: "master_private_key"
      end

      s.vm.provision "ansible_local" do |p|
        p.playbook = "ansible/playbook.yml"
        p.install_mode = "pip3"
        p.version = "2.9.23"
        p.verbose = true
        p.extra_vars =
        {
            private_ip: private_ip,
            vm_name: vm_name,
            master_ip: master_ip
        }
      end

    end
  end

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
end
