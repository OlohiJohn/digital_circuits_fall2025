#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 10:15:18 2025

@author: victoriascott and olohijohn
"""

from pyfirmata import Arduino, util
import math
import time

# Constants
SERIES_RESISTOR = 10000       # 10k resistor
THERMISTOR_PIN = 0            # A0 corresponds to analog pin 0 on PyFirmata

# Setup board
board = Arduino("/dev/cu.usbmodem14101")       # <-- change to your port
it = util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
time.sleep(1)                 # allow time for startup

while True:
    reading = analog_input.read()

    if reading is None:
        print("Waiting for sensor...")
        time.sleep(1)
        continue

    # PyFirmata returns value between 0.0 and 1.0
    adc_value = reading * 1023  

    print("Analog reading:", adc_value)

    # Convert ADC value to resistance
    resistance = (1023 / adc_value) - 1
    resistance = SERIES_RESISTOR / resistance

    print("Thermistor resistance:", resistance)

    # Temperature calculation (Steinhart-Hart simplified)
    termA = 1 / 298.15
    termB = 1 / 3950
    termC = math.log(resistance / 10000)

    tempRecip = termA + termB  * termC

    tempK = 1 / tempRecip
    print("Temperature (K):", tempK)
    tempC = tempK - 273.15
    print("Temperature (C):", tempC)

    print("---------------")
    time.sleep(10)
