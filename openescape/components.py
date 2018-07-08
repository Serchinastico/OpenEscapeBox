import time
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
        if environment.use_arduino:
            read_value = self.__arduino.read(self.__input_pin)
            self.__was_pressed = self.__was_pressed or read_value == b'1'

    def was_pressed(self):
        return self.__was_pressed


class LedComponent(Component):
    def __init__(self, arduino, output_pin):
        self.__arduino = arduino
        self.__output_pin = output_pin
        self.__is_blinking = False
        self.__is_on = False
        self.__last_measure_time = None

    def update(self):
        if self.__is_blinking:
            if self.__last_measure_time is None:
                self.__last_measure_time = time.time()
                self.turn_on()

            if time.time() - self.__last_measure_time >= 1:
                self.__last_measure_time += 1
                self.toggle()

    def blink(self):
        self.__is_blinking = True

    def toggle(self):
        self.__is_on = not self.__is_on
        self.__arduino.write(self.__output_pin, 1 if self.__is_on else 0)

    def turn_on(self):
        self.__is_on = True
        if environment.use_arduino:
            self.__arduino.write(self.__output_pin, 1)

    def turn_off(self):
        self.__is_on = False
        if environment.use_arduino:
            self.__arduino.write(self.__output_pin, 0)
