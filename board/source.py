from component.component import Component


class Source(Component):

    def __init__(self, value, name) -> None:
        super().__init__(name)
        self.__value = value

    def read(self):
        return self.__value