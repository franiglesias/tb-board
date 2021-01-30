import time

from component.component import Component

MEDIUM_SPEED = 0.005
FAST_SPEED = 0.001
SLOW_SPEED = 0.01


class Led(Component):
    input = None
    pin = None

    def __init__(self, pin, name='Led') -> None:
        super().__init__(name)
        self.pin = pin

    def send(self, value):
        self.pin.send(value)

    def run(self):
        if self.input is None:
            return
        self.send(self.input.read())

    def ready(self):
        self.__breath(times=3, speed=MEDIUM_SPEED)
        self.sleep(0.5)
        super(Led, self).ready()

    def __breath(self, times, speed=MEDIUM_SPEED):
        for i in range(0, times):
            self.__up(speed)
            self.__dim(speed)

    def __dim(self, speed=MEDIUM_SPEED):
        for v in range(100, -1, -1):
            self.send(v)
            self.sleep(speed)

    def __up(self, speed=MEDIUM_SPEED):
        for v in range(1, 101):
            self.send(v)
            self.sleep(speed)

    @staticmethod
    def sleep(speed):
        time.sleep(speed)


class InvLed(Led):

    def __init__(self, pin, name='Led') -> None:
        super().__init__(pin, name)

    def send(self, value):
        self.pin.send_inv(value)
