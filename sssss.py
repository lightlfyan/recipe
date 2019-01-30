#!/bin/bash

mkdir -p /root/.ssh
chmod 600 /root/.ssh

echo 'key' >> /root/.ssh/authorized_keys

chmod 700 /root/.ssh/authorized_keys

echo "alias l='ls -l'" >> ~/.bashrc
echo "alias ll='ls -al'" >> ~/.bashrc
echo "alias vi='vim'" >> ~/.bashrc

source ~/.bashrc

yum install -y vim-enhanced.x86_64
yum install -y bzip2
yum install -y lrzsz
yum install -y wget
yum install python36.x86_64

ln -s /usr/bin/python36 /usr/bin/python3

curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
python3.6 /tmp/get-pip.py

pip3.6 install requests
pip3.6 install gevent
pip3.6 install shadowsocks

firewall-cmd --zone=public --add-port=443/tcp --permanent 
firewall-cmd --zone=public --add-port=8388/tcp --permanent 
firewall-cmd --reload

echo '{
    "server":"0.0.0.0",
    "server_port":8388,
    "password":"1234",
    "timeout":300,
    "method":"aes-128-cfb",
    "fast_open": true
}' > /etc/shadowsocks.json


ssserver -c /etc/shadowsocks.json -d start

cd /opt
wget https://github.com/shadowsocks/shadowsocks-go/releases/download/1.2.1/shadowsocks-server.tar.gz
tar xzvf shadowsocks-server.tar.gz
echo '{
    "server":"0.0.0.0",
    "server_port":443,
    "password":"1234",
    "method": "aes-128-cfb",
    "timeout":600
}' > /opt/config.json
nohup ./shadowsocks-server &


echo "done"
