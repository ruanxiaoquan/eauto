#!/usr/bin/env python
# -*- coding=utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


def default():
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)


def reverse():
    GPIO.output(7, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)

def stop():
    GPIO.cleanup()
