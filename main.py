#!/usr/bin/env python3

from board.board import Board
from board.pin import Pin, InputPin
from component.analog_digital_converter import AnalogDigitalConverter
from component.analog_input.joystick import Joystick
from component.led.led import Led


def joystick():
    board = Board()
    adc = AnalogDigitalConverter()

    js = Joystick(analog_digital_converter=adc, channel_x=1, channel_y=0, button_pin=InputPin(12))

    red = Led(Pin(11))
    red.connect_input(js.output_y())
    board.connect(adc)
    board.connect(js)
    board.connect(red)

    try:
        board.check()
        board.loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        board.destroy()


if __name__ == '__main__':
    joystick()
