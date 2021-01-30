import time

from RPi import GPIO as GPIO


class Board:

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        self.__components = []

    def connect(self, component):
        self.__components.append(component)

    def check(self):
        for component in self.__components:
            component.ready()

    def loop(self):
        while True:
            for component in self.__components:
                component.run()
                component.status()
            time.sleep(0.03)

    def destroy(self):
        GPIO.cleanup()
        for component in self.__components:
            component.close()