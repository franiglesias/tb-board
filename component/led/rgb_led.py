from component.component import Component


class RGBLed(Component):

    def __init__(self, red_pin, green_pin, blue_pin, name='RGB Led') -> None:
        super().__init__(name)
        self.blue_pin = blue_pin
        self.green_pin = green_pin
        self.red_pin = red_pin

    def run(self):
        self.blue_pin.run()
        self.red_pin.run()
        self.green_pin.run()

    def ready(self):
        super().ready()