class Component:

    def __init__(self, name) -> None:
        self.name = name
        self.input = None

    def close(self):
        pass

    def run(self):
        pass

    def read(self):
        pass

    def ready(self):
        print('{0} ready.'.format(self.name))

    def status(self):
        print('{0} OK.'.format(self.name))

    def connect_input(self, component):
        self.input = component