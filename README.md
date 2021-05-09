# sageradio
Raspberry pi radio tuner
### requirements:
install vlc
```shell
sudo apt install vlc
```

### systemd service

Copy `radio.service` to `/etc/systemd/system/` and enable service with:
```shell
sudo systemctl enable radio.service
sudo systemclt start radio.service
```

TODO - put the service configuration in a setup file

debugging service:
```shell
sudo journalctl -u radio.service | tail
```

### forcing mono:

add these lines to the end of /etc/pulse/default.pa:
```shell
load-module module-remap-sink sink_name=mono master=alsa_output.platform-bcm2835_audio.analog-stereo channels=2 channel_map=mono,mono
set-default-sink mono
```

or for the hifiberry-amp-hat (command pacmd to find sink name, seems like you need to play some audio before running this command to get pulse daemon started)
```shell
load-module module-remap-sink sink_name=mono master=alsa_output.platform-soc_sound.stereo-fallback channels=2 channel_map=mono,mono

set-default-sink mono
```
