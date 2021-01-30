from component.analog_input.analog_input import AnalogInput


class PhotoResistor(AnalogInput):

    def __init__(self, analog_digital_converter, channel, voltage=3.3, name='Photoresistor', low_trim=7,
                 high_trim=224) -> None:
        super().__init__(analog_digital_converter, channel, voltage, name)
        self.__low_trim = low_trim
        self.__high_trim = high_trim

    def raw(self):
        reading = super(PhotoResistor, self).raw()

        return (reading - self.__low_trim) * (self.__high_trim - self.__low_trim) / 255