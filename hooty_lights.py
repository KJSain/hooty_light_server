#!/usr/bin/python3
# why did I write this cooooooooooooooooooooooooooooooooooooooode
import time
import datetime
from threading import Lock
from neopixel import *

class OwlLight():

    def __init__(self):
        # LED OWL configuration:
        self._LED_COUNT = 4      # Number of LED pixels. Hooty only has so many LEDs
        self._LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        self._LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self._LED_DMA = 10      # DMA channel to use for generating signal (try 10)
        self._LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        self._LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
        self._LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.eye_state = False
        self.beak_state = False
        self.head_state = False
        self.last_active_ping = None
        self.eye_mode = None # TODO: Want to add varying led modes
        self.beak_mode = None # TODO: Want to add varying led modes
        self.head_mode = None # TODO: Want to add varying led modes
        self.indicator = Adafruit_NeoPixel( self._LED_COUNT,
                                            self._LED_PIN,
                                            self._LED_FREQ_HZ,
                                            self._LED_DMA,
                                            self._LED_INVERT,
                                            self._LED_BRIGHTNESS,
                                            self._LED_CHANNEL)
        self.indicator.begin()
        self.data_lock = Lock()

    # Update the last the time we had an active ping for something
    def update_time(self, timestamp):
        self.last_active_ping = timestamp

    # Check if the last active ping was longer than 10 seconds ago
    def check_if_stale(self):
        if self.last_active_ping == None:
            return False
        else:
            current_time = datetime.datetime.now()
            if (current_time.timestamp() - self.last_active_ping.timestamp()) > 10: # idk I picked 10 seconds because
                return True
            else:
                return False

    # Clear all LEDs
    def clear(self):
        for i in range(self.indicator.numPixels()):
            self.indicator.setPixelColor(i, Color(0, 0, 0))
            self.indicator.show()

    def eyes(self, state):

        # If our state is already true then exit
        if (state is True and self.eye_state is True) or (state is False and self.eye_state is False):
            return
        # If state should be off but the eye_state is true, we should make it false
        # Let the presumably active thread finish it off
        elif state is False and self.eye_state is True:
            with self.data_lock:
                    self.eye_state = False
            self.eye_state = False
        # Final Case, State is True and eye State is true
        #else state is True and self.eye_state is False:
        else:
            with self.data_lock:
                self.eye_state = True
            # Keeping the thread alive & fade that possessed hooty color!
            while self.eye_state is True:

                if self.check_if_stale():
                    with self.data_lock:
                        self.eye_state = False

                for i in reversed(range(255)):
                    if self.eye_state is False:
                        break
                    self.indicator.setPixelColor(1, Color(i, i, 255))
                    self.indicator.setPixelColor(3, Color(i, i, 255))
                    self.indicator.show()
                    time.sleep(0.005)
                time.sleep(0.5)
                for i in range(255):
                    if self.eye_state is False:
                        break
                    self.indicator.setPixelColor(1, Color(i, i, 255))
                    self.indicator.setPixelColor(3, Color(i, i, 255))
                    self.indicator.show()
                    time.sleep(0.005)
                time.sleep(0.5)
            self.indicator.setPixelColor(1, Color(0, 0, 0))
            self.indicator.setPixelColor(3, Color(0, 0, 0))
            self.indicator.show()

    def beak(self, state):
        # If our state is already true then exit
        if (state is True and self.beak_state is True) or (state is False and self.beak_state is False):
            return
        # If state should be off but the eye_state is true, we should make it false
        # Let the presumably active thread finish it off
        elif state is False and self.beak_state is True:
            with self.data_lock:
                    self.beak_state = False
        # Final Case, State is True and eye State is true
        #else state is True and self.beak_state is False:
        else:
            with self.data_lock:
                self.beak_state = True
            while self.beak_state is True:
                if self.check_if_stale():
                    with self.data_lock:
                        self.beak_state = False
                self.indicator.setPixelColor(0, Color(0, 255, 0))
                self.indicator.show()
            self.indicator.setPixelColor(0, Color(0, 0, 0))
            self.indicator.show()

    def head(self, state):
        # If our state is already true then exit
        if (state is True and self.head_state is True) or (state is False and self.head_state is False):
            return
        # If state should be off but the eye_state is true, we should make it false
        # Let the presumably active thread finish it off
        elif state is False and self.head_state is True:
            with self.data_lock:
                    self.head_state = False
        # Final Case, State is True and eye State is true
        #else state is True and self.head_state is False:
        else:
            with self.data_lock:
                self.head_state = True
            while self.head_state is True:
                if self.check_if_stale():
                    with self.data_lock:
                        self.head_state = False
                self.indicator.setPixelColor(2, Color(0, 255, 0))
                self.indicator.show()
            self.indicator.setPixelColor(2, Color(0, 0, 0))
            self.indicator.show()