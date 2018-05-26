class Condition(object):
	def is_true(self):
		return False

class AlwaysFalseCondition(Condition):
	def is_true(self):
		return False

class AlwaysTrueCondition(Condition):
	def is_true(self):
		return True

class ButtonPressedCondition(Condition):
	def __init__(self, game, button):
		self.__game = game
		self.__button = button

	def is_true(self):
		return self.__button.was_pressed()

class SecondsRemainingCondition(Condition):
	def __init__(self, game, seconds_remaining):
		self.__game = game
		self.__seconds_remaining = seconds_remaining

	def is_true(self):
		return self.__game.seconds_remaining() <= self.__seconds_remaining
