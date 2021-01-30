from RPi import GPIO as GPIO

from component.component import Component


class Switch(Component):

    def __init__(self, pin, name='Switch') -> None:
        super().__init__(name)
        self.pin = pin
        self.__state = 0
        self.__prev = GPIO.HIGH

    def read(self):
        reading = self.pin.get()

        if reading == GPIO.LOW:
            if self.__state == 0:
                self.__state = 100
            else:
                self.__state = 0

        return self.__state

    def status(self):
        if self.__state == 0:
            print('%s -> ON (%d)' % (self.name, self.__state))
        else:
            print('%s -> OFF (%d)' % (self.name, self.__state))