#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 09:22:14 2025

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

# Servo pin: digital 9
servo = board.get_pin('d:9:s')   # "s" = servo mode
buzzer = board.get_pin('d:10:o') # "o" = digital output


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

   
    if (tempC > 30 or tempC < 10):
        # --- ring buzzer: 3 short beeps ---
        for _ in range(3):
            buzzer.write(1)       # ON
            time.sleep(0.2)
            buzzer.write(0)       # OFF
            time.sleep(0.2)
        # -----------------------------------
    
            # open door in gradual angle increments from 0 to 180
        print("---------Door Opening--------")
        for pos in range(0, 181, 1):
            servo.write(pos)
            time.sleep(0.015)  # 15 ms like Arduino
        # ring buzzer
        
        # wait for 30s
        time.sleep(30)
        
        # close door in gradual angle increments from 180 to 0
        print(f"---------Door Closing-------")
        for pos in range(180, -1, -1):
            servo.write(pos)
            time.sleep(0.015)
            
        # turn off buzzer

    time.sleep(10)
