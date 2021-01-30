import math

from component.analog_input.analog_input import AnalogInput


class Thermistor(AnalogInput):
    def __init__(self, analog_digital_converter, channel, voltage=3.3, name='Photoresistor') -> None:
        super().__init__(analog_digital_converter, channel, voltage, name)

    def status(self):
        print('%s -> Value: %d, ºK: %.2f, C: %.2f' % (self.name, self.raw(), self.kelvin(), (self.celsius())))

    def celsius(self):
        return self.kelvin() - 273.15

    def kelvin(self):
        return 1 / (1 / (273.15 + 25) + math.log(self.resistance() / 10) / 3950.0)

    def resistance(self):
        return 10 * self.voltage() / (3.3 - self.voltage())