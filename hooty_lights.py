#!/usr/bin/env python3
import time
from neopixel import *

class OwlLight():

    def __init__(self, state = "off"):
        # LED OWL configuration:
        self.LED_COUNT = 4      # Number of LED pixels. Hooty only has so many LEDs
        self.LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.state = state
        self.indicator = Adafruit_NeoPixel( self.LED_COUNT,
                                            self.LED_PIN,
                                            self.LED_FREQ_HZ,
                                            self.LED_DMA,
                                            self.LED_INVERT,
                                            self.LED_BRIGHTNESS,
                                            self.LED_CHANNEL)
        self.indicator.begin()

    # Clear all LEDs
    def clear(self):
        for i in range(self.indicator.numPixels()):
            self.indicator.setPixelColor(i, Color(0, 0, 0))
            self.indicator.show()

    def eyes(self, state):
        if state is True:
            self.indicator.setPixelColor(1, Color(0, 255, 0))
            self.indicator.setPixelColor(3, Color(0, 255, 0))
            self.indicator.show()
        if state is False:
            self.indicator.setPixelColor(1, Color(0, 0, 0))
            self.indicator.setPixelColor(3, Color(0, 0, 0))
            self.indicator.show()

    def beak(self, state):
        if state is True:
            self.indicator.setPixelColor(0, Color(255, 0, 0))
            self.indicator.show()
        if state is False:
            self.indicator.setPixelColor(0, Color(0, 0, 0))
            self.indicator.show()

    def head(self, state):
        if state is True:
            self.indicator.setPixelColor(2, Color(255, 0, 255))
            self.indicator.show()
        if state is False:
            self.indicator.setPixelColor(2, Color(0, 0, 0))
            self.indicator.show()