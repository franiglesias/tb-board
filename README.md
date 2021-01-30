# tb-board

This is a library of components to help when building circuits with the Raspberry Pi GPIO.



## Example

This is a simple example of a LED being controlled with a PhotoResistor.


```python
def thermometer():
    board = Board()


    adc = AnalogDigitalConverter()
    thermistor = Thermistor(analog_digital_converter=adc, channel=0, voltage=3.3)

    red = Led(Pin(11), 'Red')
    red.connect_input(thermistor)

    board.connect(adc)
    board.connect(thermistor)
    board.connect(red)
    try:
        board.check()
        board.loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        board.destroy()
```

You init the Board to connect all components with:

```pyhton
    board = Board()
```

Thermistor is an Analog Input device, and needs an AnalogDigitalConverter. We should pass the ADC, the channel in which the Thermistor will be connected and the max voltage of the circuit.

```python
    adc = AnalogDigitalConverter()
    thermistor = Thermistor(analog_digital_converter=adc, channel=0, voltage=3.3)
```

This is how we connect a led. We need to specify the number of the pin of the GPIO and the component that will provide the input for the led.

I named the LED "red" because I use a red led for the circuit.

```python
    red = Led(Pin(11), 'Red')
    red.connect_input(thermistor)
```

Now, we "connect" the components to the board:

```python
    board.connect(adc)
    board.connect(thermistor)
    board.connect(red)
```

And, we can make it run. The 'check' method invokes a ready method in all components so they can indicate if the are ready to work or not.

```python
    try:
        board.check()
        board.loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        board.destroy()
```

An that's all.
