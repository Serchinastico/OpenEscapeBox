from functools import partial
from openescape.actions import *
from openescape.components import *
from openescape.conditions import *
from openescape.game import Game
from openescape.triggers import *


class GameFactory(object):
    @staticmethod
    def from_config(game_config, arduino):
        game = Game(duration_seconds=game_config.duration_seconds())
        game.actions = ActionFactory.from_config(game_config.actions(), game)
        game.components = ComponentFactory.from_config(
            game_config.components(), arduino)
        game.conditions = ConditionFactory.from_config(
            game_config.conditions(), game)
        game.triggers = TriggerFactory.from_config(
            game_config.triggers(), game)

        return game


class ActionFactory(object):
    @staticmethod
    def from_config(actions_config, game):
        actions = {}
        for id, data in actions_config.items():
            if id in actions:
                logging.warning('Duplicated action [{}]'.format(id))

            action_type = data.get('type')
            action_config = data.get('config')
            if action_type == 'BLINK_LED':
                actions[id] = BlinkLedAction()
            elif action_type == 'GAME_LOSS':
                actions[id] = GameLossAction(game, action_config)
            elif action_type == 'GAME_VICTORY':
                actions[id] = GameVictoryAction(game, action_config)
            elif action_type == 'HINT_AVAILABLE':
                actions[id] = HintAvailableAction(game, action_config)
            elif action_type == 'HINT_CRITICAL':
                actions[id] = HintCriticalAction(game, action_config)
            elif action_type == 'TURN_LIGHT_ON':
                actions[id] = TurnLightOnAction(game, action_config)
            else:
                raise ValueError(
                    'Unrecognized action type [{}]'.format(action_type))

        return actions


class ComponentFactory(object):
    @staticmethod
    def from_config(components_config, arduino):
        components = {}
        for id, data in components_config.items():
            if id in components:
                logging.warning('Duplicated component [{}]'.format(id))

            component_type = data.get('type')
            component_input_pin = data.get('inputPin')
            if component_type == 'BUTTON':
                components[id] = ButtonComponent(arduino, component_input_pin)
            elif component_type == 'LED':
                components[id] = LedComponent()
            else:
                raise ValueError(
                    'Unrecognized component type [{}]'.format(component_type))

        return components


class ConditionFactory(object):
    @staticmethod
    def from_config(conditions_config, game):
        conditions = {}
        for id, data in conditions_config.items():
            if id in conditions:
                logging.warning('Duplicated condition [{}]'.format(id))

            condition_type = data.get('type')
            condition_value = data.get('value')
            if condition_type == 'ALL':
                conditions[id] = AllCondition()
            elif condition_type == 'BUTTON_PRESSED':
                conditions[id] = ButtonPressedCondition(
                    game, game.components[condition_value])
            elif condition_type == 'LED_ON':
                conditions[id] = LedOnCondition()
            elif condition_type == 'SECONDS_REMAINING':
                conditions[id] = SecondsRemainingCondition(
                    game, condition_value)
            else:
                raise ValueError(
                    'Unrecognized condition type [{}]'.format(condition_type))

        return conditions


class TriggerFactory(object):
    @classmethod
    def from_config(cls, triggers_config, game):
        triggers = []
        for data in triggers_config:
            enable_condition = cls.__resolve_condition(
                game, data, 'enableConditionId', AlwaysTrueCondition())
            disable_condition = cls.__resolve_condition(
                game, data, 'disableConditionId', AlwaysFalseCondition())
            trigger_condition = cls.__resolve_condition(
                game, data, 'triggerConditionId', AlwaysTrueCondition())
            actions = list(
                map(partial(cls.__resolve_action, game), data['actionIds']))
            triggers.append(
                Trigger(enable_condition, disable_condition, trigger_condition, actions))

        return triggers

    @staticmethod
    def __resolve_action(game, action_id):
        if action_id not in game.actions:
            raise ValueError('Undefined action id [{}]'.format(action_id))

        return game.actions[action_id]

    @staticmethod
    def __resolve_condition(game, trigger_config, config_key, condition_if_none):
        condition_id = trigger_config[config_key]

        if condition_id is None:
            return condition_if_none
        else:
            if condition_id not in game.conditions:
                raise ValueError(
                    'Undefined condition id [{}]'.format(condition_id))

            return game.conditions[condition_id]
