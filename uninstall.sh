#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "please run as root"
    exit
fi

SERVICE_NAME="sageradio"

echo "uninstall vlc"
#apt remove vlc

echo "Check if '${SERVICE_NAME}' service is installed"

if systemctl list-unit-files | grep "^${SERVICE_NAME}.service"; then
    echo "'${SERVICE_NAME}' is installed... removing"
    systemctl stop ${SERVICE_NAME}.service
    systemctl stop ${SERVICE_NAME}.service
else
    echo "'${SERVICE_NAME}' is not installed"
fi

# Try to remove any files just in case
sudo rm /etc/systemd/system/${SERVICE_NAME}.service

sudo systemctl daemon-reload
