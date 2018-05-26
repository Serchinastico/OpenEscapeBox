class Component(object):
    pass


class ButtonComponent(Component):
    def __init__(self, arduino, device, input_pin):
        self.__arduino = arduino
        self.__device = device
        self.__input_pin = input_pin

    def was_pressed(self):
        return False
