from openescape.environment import environment


class Component(object):
    def update(self):
        pass


class ButtonComponent(Component):
    def __init__(self, arduino, input_pin):
        self.__arduino = arduino
        self.__input_pin = input_pin
        self.__was_pressed = False

    def update(self):
        if not environment.is_development:
            read_value = self.__arduino.read(self.__input_pin)
            self.__was_pressed = self.__was_pressed or read_value == b'1'

    def was_pressed(self):
        return self.__was_pressed
