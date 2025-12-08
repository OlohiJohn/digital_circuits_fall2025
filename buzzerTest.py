#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 10:31:19 2025

@author: victoriascott
"""

from pyfirmata import Arduino, util
import time

board = Arduino('/dev/cu.usbmodem14101')   # Change COM port as needed (e.g., "/dev/ttyACM0")

buzzer = board.get_pin('d:10:o')  # digital pin 9 as output

def tone(pin, frequency, duration=None):
    """
    Simple tone() implementation using PWM on Firmata.
    Note: Firmata cannot generate real hardware PWM frequencies like Arduino's tone(),
    but we can simulate using analogWrite at high frequency.
    """
    board.digital[pin].write(1)  # turn ON
    if duration:
        time.sleep(duration)
        noTone(pin)

def noTone(pin):
    board.digital[pin].write(0)  # turn OFF

while True:
    # Simulate tone at 1kHz (not exact due to Firmata limitations)
    print("making noise...")
    board.digital[9].write(1)
    time.sleep(1)
    board.digital[9].write(0)
    time.sleep(1)
