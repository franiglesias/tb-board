from ADCDevice import ADCDevice, PCF8591, ADS7830

from component.component import Component


class AnalogDigitalConverter(Component):

    def __init__(self, name='ADC') -> None:
        self.adc = self.__detect_adc()
        super().__init__('Analog Digital Converter ' + type(self.adc).__name__)

    @staticmethod
    def __detect_adc():
        device = ADCDevice()  # Define an ADCDevice class object
        if device.detectI2C(0x48):  # Detect the pcf8591.
            return PCF8591()
        elif device.detectI2C(0x4b):  # Detect the ads7830
            return ADS7830()
        else:
            print("No correct I2C address found, \n"
                  "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
                  "Program Exit. \n")
            exit(-1)

    def analog_read(self, channel):
        return self.adc.analogRead(channel)

    def close(self):
        self.adc.close()

    def connect_input(self, component):
        pass