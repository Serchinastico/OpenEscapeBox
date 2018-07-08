import re
import os


class Bitlash(object):
    def __init__(self, fd, arduino):
        self.__fd = fd
        self.__arduino = arduino

    def run(self):
        file = os.fdopen(self.__fd, 'r+')
        commands = [
            ReadPinBitlashCommand,
            UnsupportedBitlashCommand
        ]

        while True:
            request = file.readline()
            file.write(request)

            for command in commands:
                if command.can_handle(request):
                    response = command.handle(request, self.__arduino)
                    break

            if response is not None:
                file.write('{}\n'.format(response))


class BitlashCommand(object):
    @classmethod
    def can_handle(cls, request):
        return False

    @classmethod
    def handle(cls, request, arduino):
        pass


class ReadPinBitlashCommand(BitlashCommand):
    COMMAND_RE = re.compile('^{print} {pin}$'.format(
        print='\s*print\s*',
        pin='\s*(?P<pin>d\d+)\s*'))

    @classmethod
    def can_handle(cls, request):
        return cls.COMMAND_RE.match(request)

    @classmethod
    def handle(cls, request, arduino):
        pin = cls.COMMAND_RE.match(request).group('pin')
        return arduino.read(pin)


class UnsupportedBitlashCommand(BitlashCommand):
    @classmethod
    def can_handle(cls, request):
        return True

    @classmethod
    def handle(cls, request, arduino):
        print('Unsupported command [{}]'.format(request.strip()))
