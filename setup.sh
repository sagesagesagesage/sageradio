#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "please run as root"
    exit
fi

echo "Verify vlc is installed"
if command -v vlc &>/dev/null; then
    echo "VLC is not installed"
    apt install -y vlc
else
    echo "VLC is already installed"
fi

echo "Copying service file to systemd"
cp sageradio.service /etc/systemd/system/

echo "Enabling radio service"
systemctl enable sageradio.service

echo "Starting service"
systemctl start sageradio.service

echo "Install Adafruit circuit python stuff for the display"


echo "Remember to reconfigure pulse audio for mono!"
