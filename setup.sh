#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "please run as root"
    exit
fi

echo "Copying service file to systemd"
cp radio.service /etc/systemd/system/

echo "Enabling radio service"
systemctl enable radio.service

echo "Starting service"
systemctl start radio.service
