import serial
from openescape.environment import environment

class Action(object):
    def execute(self):
        pass

class TurnLightOnAction(Action):
    def __init__(self, config):
    	if not environment.is_development:
        	self.connection = serial.Serial('/dev/ttyACM0', 57600)

    def execute(self):
    	if environment.is_development:
    		print('Turn light on')
    	else:
    		self.connection.write("d13=1")
    		self.connection.flush()
