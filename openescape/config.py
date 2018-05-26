from openescape.actions import *
from openescape.conditions import *
from openescape.triggers import *
from ruamel.yaml import YAML

class GameConfig(object):
	def __init__(self, config):
		self.__config = config
		self.__init_actions()
		self.__init_conditions()
		self.__init_triggers()

	@staticmethod
	def from_yaml_config_file_path(path):
		file = open(path)
		config = YAML().load(file)
		return GameConfig(config)

	def duration_seconds(self):
		return self.__config.get('durationSeconds')

	def title(self):
		return self.__config.get('title')

	def triggers(self):
		return self.__triggers

	def __init_actions(self):
		self.__actions = {}
		for id, action_data in self.__config.get('actions').items():
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
		for id, condition_data in self.__config.get('conditions').items():
			if id in self.__conditions:
				print('Duplicated condition [{}]'.format(id))

			condition_type = condition_data.get('type')
			condition_value = condition_data.get('value')
			if condition_type == 'SECONDS_REMAINING':
				self.__conditions[id] = SecondsRemainingCondition(condition_value)
			else:
				print('Unrecognized condition type [{}]'.format(condition_type))

	def __init_triggers(self):
		self.__triggers = []
		for trigger_data in self.__config.get('triggers'):
			enable_condition = self.__conditions[trigger_data['enableConditionId']]
			disable_condition = self.__conditions[trigger_data['disableConditionId']]
			trigger_condition = self.__conditions[trigger_data['triggerConditionId']]
			actions = map(self.__actions.get, trigger_data['actionIds'])
			self.__triggers.append(Trigger(enable_condition, disable_condition, trigger_condition, actions))
