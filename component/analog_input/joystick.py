from component.analog_input.analog_input import AnalogInput
from component.control.button import Button


class Joystick(AnalogInput):
    def __init__(self, analog_digital_converter, channel_x, channel_y, button_pin, voltage=3.3,
                 name='Joystick') -> None:
        self.x = AnalogInput(analog_digital_converter, channel_x, voltage, 'Joystick X')
        self.y = AnalogInput(analog_digital_converter, channel_y, voltage, 'Joystick Y')
        self.button = Button(button_pin)
        self.name = name

    def raw(self):
        return self.x.raw(), self.y.raw(), self.button.read()

    def status(self):
        print('%s -> X,Y: %d,%d Button: %s' % (
            self.name, self.coordinates()[0], self.coordinates()[1], self.button.status()))

    def output_x(self):
        return self.x

    def output_y(self):
        return self.y

    def output_button(self):
        return self.button

    def coordinates(self):
        return self.x.raw(), self.y.raw()
