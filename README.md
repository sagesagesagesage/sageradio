# sageradio
Raspberry pi radio tuner
### requirements:

debugging service:
```shell
journalctl --user-unit radio.service | tail
```

### forcing mono:
look at default.pa.back for pulseaudio configuration
file exists at /etc/pulse/
