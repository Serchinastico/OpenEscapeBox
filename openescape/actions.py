import logging
import serial
from openescape.environment import environment


class Action(object):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        pass


class BlinkLedAction(Action):
    def __init__(self, led_component):
        self.__led_component = led_component

    def execute(self):
        self.__led_component.blink()


class GameVictoryAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        logging.info('Game victory!')
        self.__game.trigger_victory()


class GameLossAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        logging.info('Game lost :(')
        self.__game.trigger_loss()


class HintAvailableAction(Action):
    def __init__(self, game, image_url):
        self.__game = game
        self.__image_url = image_url

    def execute(self):
        logging.info('Make hint available [{}]'.format(self.__image_url))
        self.__game.set_hint_available(self.__image_url)


class HintCriticalAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        logging.info('Make hint critical')
        self.__game.set_hint_critical()


class TurnLightOnAction(Action):
    def __init__(self, game, config):
        if environment.use_arduino:
            self.connection = serial.Serial('/dev/ttys000', 57600)

    def execute(self):
        logging.info('Turn light on')

        if environment.use_arduino:
            self.connection.write(b'd13=1\n')
            self.connection.flush()
