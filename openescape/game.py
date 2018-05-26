from openescape.actions import *
from openescape.conditions import *
from openescape.triggers import *

class Game:
	def __init__(self, game_config):
		self.__game_config = game_config
		self.__seconds_remaining = game_config.duration_seconds()
		self.__init_actions()
		self.__init_conditions()
		self.__init_triggers()

	def actions(self):
		return self.__actions

	def conditions(self):
		return self.__conditions

	def triggers(self):
		return self.__triggers

	def seconds_remaining(self):
		return self.__seconds_remaining

	def set_seconds_remaining(self, seconds_remaining):
		self.__seconds_remaining = seconds_remaining

	def __init_actions(self):
		self.__actions = {}
		for id, action_data in self.__game_config.actions().items():
			if id in self.__actions:
				print('Duplicated action [{}]'.format(id))

			action_type = action_data.get('type')
			action_config = action_data.get('config')
			if action_type == 'TURN_LIGHT_ON':
				self.__actions[id] = TurnLightOnAction(action_config)
			else:
				print('Unrecognized action type [{}]'.format(action_type))

	def __init_conditions(self):
		self.__conditions = {}
		for id, condition_data in self.__game_config.conditions().items():
			if id in self.__conditions:
				print('Duplicated condition [{}]'.format(id))

			condition_type = condition_data.get('type')
			condition_value = condition_data.get('value')
			if condition_type == 'SECONDS_REMAINING':
				self.__conditions[id] = SecondsRemainingCondition(self, condition_value)
			else:
				print('Unrecognized condition type [{}]'.format(condition_type))

	def __init_triggers(self):
		self.__triggers = []
		for trigger_data in self.__game_config.triggers():
			enable_condition = self.__conditions[trigger_data['enableConditionId']]
			disable_condition = self.__conditions[trigger_data['disableConditionId']]
			trigger_condition = self.__conditions[trigger_data['triggerConditionId']]
			actions = map(self.__actions.get, trigger_data['actionIds'])
			self.__triggers.append(Trigger(enable_condition, disable_condition, trigger_condition, actions))
