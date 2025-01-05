#!/bin/bash
sudo iptables -t nat -A POSTROUTING -o weave -j MASQUERADE
sudo iptables -A FORWARD -i weave -o eno1 -j ACCEPT
sudo iptables -A FORWARD -i eno1 -o weave -m state --state RELATED,ESTABLISHED -j ACCEPT
