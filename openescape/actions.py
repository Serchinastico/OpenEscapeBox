import serial
import time
import os


class Action(object):
    def execute(self):
        pass


class TurnLightOnAction(Action):
    def __init__(self, config):
        self.connection = serial.Serial('/dev/ttyACM0', 57600)
        pass

    def execute(self):
        self.connection.write("d13=1")
        self.connection.flush()
