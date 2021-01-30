from RPi import GPIO as GPIO


class Pin:

    def __init__(self, pin) -> None:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        self.pwm = GPIO.PWM(pin, 1000)
        self.pwm.start(0)

    def send(self, value):
        self.pwm.ChangeDutyCycle(value)

    def send_inv(self, value):
        v = 100 - value
        if v < 0:
            v = 0
        if v > 100:
            v = 100
        self.pwm.ChangeDutyCycle(v)


class InputPin:
    def __init__(self, pin) -> None:
        self.__pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get(self):
        return GPIO.input(self.pin())

    def pin(self):
        return self.__pin