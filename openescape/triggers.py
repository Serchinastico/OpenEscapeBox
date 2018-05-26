class Trigger(object):
	def __init__(self, enableCondition, disableCondition, triggerCondition, actions):
		self.__enableCondition = enableCondition
		self.__disableCondition = disableCondition
		self.__triggerCondition = triggerCondition
		self.__actions = actions
		self.__done = False

	def evaluate(self):
		if self.__done or self.__disableCondition.is_true() or not self.__enableCondition.is_true():
			return

		if self.__triggerCondition.is_true():
			for action in self.__actions:
				action.execute()

		self.__done = True
