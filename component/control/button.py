from RPi import GPIO as GPIO

from component.component import Component


class Button(Component):

    def __init__(self, pin, name='Button') -> None:
        super().__init__(name)
        self.pin = pin

    def read(self):
        if self.pin.get() == GPIO.LOW:
            return GPIO.HIGH
        return GPIO.LOW

    def status(self):
        if self.pin.get() == GPIO.LOW:
            print('%s -> ON (%d)' % (self.name, self.pin.get()))
        else:
            print('%s -> OFF (%d)' % (self.name, self.pin.get()))