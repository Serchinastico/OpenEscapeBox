class Action(object):
	def execute(self):
		pass

class TurnLightOnAction(Action):
	def __init__(self, config):
		# TODO Add real dependencies
		pass

	def execute(self):
		print('Turn light on')
