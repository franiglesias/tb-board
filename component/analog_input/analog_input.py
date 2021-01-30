from component.component import Component


class AnalogInput(Component):
    def __init__(self, analog_digital_converter, channel, voltage=3.3, name='Potentiometer') -> None:
        super().__init__(name)
        self.__adc = analog_digital_converter
        self.__channel = channel
        self.__voltage = voltage

    def raw(self):
        return self.__adc.analog_read(channel=self.__channel)

    def percent(self):
        return self.raw() * 100 / 255.0

    def voltage(self):
        return self.raw() * self.__voltage / 255.0

    def read(self):
        return self.percent()

    def status(self):
        print('%s -> Value: %d, PCT: %.2f, Voltage: %.2f' % (self.name, self.raw(), self.percent(), self.voltage()))

    def run(self):
        pass

    def connect_input(self, component):
        pass