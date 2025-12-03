#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 10:33:26 2025

@author: victoriascott
"""

from pyfirmata import Arduino, util
import time

# Change to your board's port
board = Arduino("/dev/cu.usbmodem14101")

# Servo pin: digital 9
servo = board.get_pin('d:9:s')   # "s" = servo mode

# Give time for board to initialize
time.sleep(1)

pos = 0

while True:
    # Sweep from 0 to 180
    for pos in range(0, 181, 1):
        servo.write(pos)
        time.sleep(0.015)  # 15 ms like Arduino
        print("Sweeping from 0 to 180...")

    # Sweep from 180 down to 0
    for pos in range(180, -1, -1):
        servo.write(pos)
        time.sleep(0.015)
        print("Sweeping from 180 to 0...")
