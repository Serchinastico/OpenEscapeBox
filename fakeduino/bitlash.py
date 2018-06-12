import os


class Bitlash(object):
    def __init__(self, fd, arduino):
        self.__fd = fd
        self.__arduino = arduino

    def run(self):
        file = os.fdopen(self.__fd, 'r+')

        while True:
            request = file.readline()
            file.write(request)
            response = self.__handle_request(request)
            file.write('{}\n'.format(response))

    def __handle_request(self, request):
        cmd, *args = tuple(map(lambda x: x.strip(), request.split(maxsplit=1)))

        if cmd == 'print':
            return self.__arduino.read(args[0])
        else:
            print('Unsupported command: [{}]'.format(cmd))
