#!/bin/bash

# Backup the original hosts file
sudo cp /etc/hosts /etc/hosts.bak

# Modify the hosts file
sudo sed -i 's/127.0.0.1/127.0.0.2/g' /etc/hosts
sudo sed -i 's/facebook.com/8.8.8.8/g' /etc/hosts

# Flush DNS cache
sudo systemctl restart systemd-resolved

echo "Configuration complete."
