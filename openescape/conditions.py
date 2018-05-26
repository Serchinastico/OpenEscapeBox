class Condition(object):
	def is_true(self):
		return False

class SecondsRemainingCondition(Condition):
	def __init__(self, seconds_remaining):
		self.__seconds_remaining = seconds_remaining

	def is_true(self):
		# TODO Need game state
		return False
