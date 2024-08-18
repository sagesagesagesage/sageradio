import os
import signal
import subprocess
import random

import RPi.GPIO as GPIO
import time

from display import Display

from stations import stations

GPIO.setmode(GPIO.BCM)

#google configuring pulse audio for mono - it works! 

def play(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn = os.setsid)
    return p

switches = [17, 27, 22, 5, 6, 26, 23, 24, 25, 8, 7]
station_led = 12
power_sw = 16

GPIO.setup([power_sw], GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(station_led, GPIO.OUT)

for i in range(5):
    GPIO.output(station_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(station_led, GPIO.LOW)
    time.sleep(0.2)

os.system("killall vlc")

# Max out the volume
os.system("amixer set Master 65535")
def get_active_index():
    active_index = -1
    for index, switch in enumerate(switches):
        if not(GPIO.input(switch)):
            active_index = index
            break
    return active_index

active_index = -1
last_active_index = -1

d = Display()
while True:
    
    active_index = get_active_index()
    

    if (GPIO.input(power_sw)):
        GPIO.output(station_led, GPIO.LOW)
        os.system("killall vlc")
        last_active_index = -1
        d.clear()
    else:
        #display "static" on LED
        if active_index == -1:
            val = random.random()
            if val < 0.2:
                GPIO.output(station_led, GPIO.HIGH)
            else:
                GPIO.output(station_led, GPIO.LOW)

        if active_index != last_active_index:
            last_active_index = active_index
            print("New index: {}".format(active_index))
            #between switches, play static
            if active_index == -1:
                GPIO.output(station_led, GPIO.LOW)
                os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                os.system("killall vlc")

                #cmd = "cvlc {}\"german radio tuning.mp3\" --start-time {} ".format(streams_loc, random.randrange(0, 15))
                #print(cmd)

                #p = play(cmd)

            # start the new station 
            else: 
                try:
                    os.system("killall vlc")
                    os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                except:
                    pass
                GPIO.output(station_led, GPIO.HIGH)
                
                stream_name = list(stations.keys())[active_index % len(stations)]
                stream_url = stations[stream_name]
                
                cmd = "cvlc {}".format(stream_url)
                print(cmd)

                p = play(cmd)
                print(stream_name)    
                d.set_channel(stream_name)

    time.sleep(0.05)
