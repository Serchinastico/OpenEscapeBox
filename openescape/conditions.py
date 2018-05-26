class Condition(object):
	def is_true(self):
		return False

class SecondsRemainingCondition(Condition):
	def __init__(self, game, seconds_remaining):
		self.__game = game
		self.__seconds_remaining = seconds_remaining

	def is_true(self):
		return self.__game.seconds_remaining() <= self.__seconds_remaining
