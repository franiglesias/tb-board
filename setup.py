from setuptools import setup

setup(
    name='tb-board',
    version='0.0.0',
    packages=['board', 'component', 'component.led', 'component.control', 'component.analog_input'],
    url='https://github.com/franiglesias/tb-board',
    license='GNU GPL3',
    author='Fran Iglesias',
    author_email='franiglesias@mac.com',
    description='Objects library to represent components for circuits with the Raspberry Pi GPIO'
)
