from openescape.actions import *
from openescape.components import *
from openescape.conditions import *
from openescape.triggers import *


class Game:
    def __init__(self, game_config, arduino):
        self.__game_config = game_config
        self.__arduino = arduino
        self.__seconds_remaining = game_config.duration_seconds()
        self.__is_finished = False
        self.__init_actions()
        self.__init_components()
        self.__init_conditions()
        self.__init_triggers()

    def actions(self):
        return self.__actions

    def components(self):
        return self.__components

    def conditions(self):
        return self.__conditions

    def triggers(self):
        return self.__triggers

    def is_finished(self):
        return self.__is_finished

    def seconds_remaining(self):
        return self.__seconds_remaining

    def set_hint_available(self, image_url):
        pass

    def set_hint_critical(self):
        pass

    def trigger_loss(self):
        self.__is_finished = True

    def trigger_victory(self):
        self.__is_finished = True

    def set_seconds_remaining(self, seconds_remaining):
        self.__seconds_remaining = seconds_remaining

    def __init_actions(self):
        self.__actions = {}
        for id, action_data in self.__game_config.actions().items():
            if id in self.__actions:
                print('Duplicated action [{}]'.format(id))

            action_type = action_data.get('type')
            action_config = action_data.get('config')
            if action_type == 'GAME_LOSS':
                self.__actions[id] = GameLossAction(self, action_config)
            elif action_type == 'GAME_VICTORY':
                self.__actions[id] = GameVictoryAction(self, action_config)
            elif action_type == 'HINT_AVAILABLE':
                self.__actions[id] = HintAvailableAction(self, action_config)
            elif action_type == 'HINT_CRITICAL':
                self.__actions[id] = HintCriticalAction(self, action_config)
            elif action_type == 'TURN_LIGHT_ON':
                self.__actions[id] = TurnLightOnAction(self, action_config)
            else:
                print('Unrecognized action type [{}]'.format(action_type))

    def __init_components(self):
        self.__components = {}
        for id, component_data in self.__game_config.components().items():
            if id in self.__components:
                print('Duplicated component [{}]'.format(id))

            component_type = component_data.get('type')
            component_input_pin = component_data.get('inputPin')
            if component_type == 'BUTTON':
                self.__components[id] = ButtonComponent(
                    self.__arduino, component_input_pin)
            else:
                print('Unrecognized component type [{}]'.format(
                    component_type))

    def __init_conditions(self):
        self.__conditions = {}
        for id, condition_data in self.__game_config.conditions().items():
            if id in self.__conditions:
                print('Duplicated condition [{}]'.format(id))

            condition_type = condition_data.get('type')
            condition_value = condition_data.get('value')
            if condition_type == 'BUTTON_PRESSED':
                self.__conditions[id] = ButtonPressedCondition(
                    self, self.__components[condition_value])
            elif condition_type == 'SECONDS_REMAINING':
                self.__conditions[id] = SecondsRemainingCondition(
                    self, condition_value)
            else:
                print('Unrecognized condition type [{}]'.format(
                    condition_type))

    def __init_triggers(self):
        self.__triggers = []
        for trigger_data in self.__game_config.triggers():
            enable_condition = self.__conditions.get(
                trigger_data['enableConditionId'], AlwaysTrueCondition())
            disable_condition = self.__conditions.get(
                trigger_data['disableConditionId'], AlwaysFalseCondition())
            trigger_condition = self.__conditions.get(
                trigger_data['triggerConditionId'], AlwaysTrueCondition())
            actions = map(self.__actions.get, trigger_data['actionIds'])
            self.__triggers.append(
                Trigger(enable_condition, disable_condition, trigger_condition, actions))
