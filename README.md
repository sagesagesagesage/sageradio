# sageradio
Raspberry pi radio tuner





'''
Service file
'''
Copy `radio.service` to `/etc/systemd/system/`
`sudo systemctl enable radio.service`
`sudo systemclt start radio.service`

TODO - put the service configuration in a setup file

debugging service:
`sudo journalctl -u radio.service | tail`



'''
forcing mono:
'''
add these lines to the end of /etc/pulse/default.pa:

load-module module-remap-sink sink_name=mono master=alsa_output.platform-bcm2835_audio.analog-stereo channels=2 channel_map=mono,mono
set-default-sink mono
