#!/usr/bin/env python3

from board.board import Board
from board.pin import Pin
from component.analog_input.photoresistor import PhotoResistor
from component.led.led import Led
from component.analog_digital_converter import AnalogDigitalConverter


def thermometer():
    board = Board()
    adc = AnalogDigitalConverter()

    thermistor = PhotoResistor(analog_digital_converter=adc, channel=0, voltage=3.3)
    red = Led(Pin(11), 'Red')
    red.connect_input(thermistor)

    board.connect(adc)
    board.connect(thermistor)
    board.connect(red)
    try:
        board.check()
        board.loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        board.destroy()


if __name__ == '__main__':
    thermometer()
