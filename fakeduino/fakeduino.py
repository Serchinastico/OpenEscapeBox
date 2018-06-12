import sys
from PyQt5.QtWidgets import *


class Fakeduino(object):
    def __init__(self):
        self.__components = {}

        self.__app = QApplication(sys.argv)
        self.__form_layout = QFormLayout()
        self.__main_window = QWidget()
        self.__main_window.setWindowTitle('Fakeduino')
        self.__main_window.setLayout(self.__form_layout)
        self.__main_window.show()

    def attach(self, component, pin):
        if pin in self.__components:
            print('Pin {} already in use'.format(pin))

        self.__components[pin] = component
        self.__form_layout.addRow(QLabel(pin), component)

    def read(self, pin):
        if pin not in self.__components:
            print('Trying to read from unattached pin {}'.format(pin))

        return self.__components[pin].value

    def run(self):
        sys.exit(self.__app.exec_())


class FakeduinoComponent(object):
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value
