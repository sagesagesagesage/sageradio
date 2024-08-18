# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

class Display(object):
    def __init__(self):
        # Create the I2C interface.
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # This creates a 14 segment alphanumeric 4 character display:
        self.display = segments.Seg14x4(self.i2c)

        # Clear the display.
        self.display.fill(0)

    def set_channel(self, channel_name):
        
        if len(channel_name) > 4:
            # this seems to hijack the program
            #self.display.marquee(channel_name, 0.2)
            self.display.print(channel_name[0:4])
        else:
            self.display.print(channel_name)

    def clear(self):
        self.display.fill(0)
