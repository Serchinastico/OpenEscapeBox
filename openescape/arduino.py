import serial


class Arduino(object):
    def __init__(self):
        self.__connection = serial.Serial('/dev/ttyACM0', 57600)

    def read(self, pin):
        self.__connection.write('print {}\n'.format(pin).encode('utf-8'))
        value_so_far = b""
        next_character = self.__connection.read()

        while self.__connection.read() != b'\n':
            pass

        while next_character != b'\n':
            value_so_far += next_character
            next_character = self.__connection.read()

        value_so_far = value_so_far.strip()[1:]
        return value_so_far

    def write(self, pin, value):
        self.__connection.write('{}={}\n'.format(pin, value).encode('utf-8'))
        self.__connection.flush()
