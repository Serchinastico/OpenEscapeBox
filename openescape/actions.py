import serial
from openescape.environment import environment


class Action(object):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        pass


class GameVictoryAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        print('Game victory!')
        self.__game.trigger_victory()


class GameLossAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        print('Game lost :(')
        self.__game.trigger_loss()


class HintAvailableAction(Action):
    def __init__(self, game, image_url):
        self.__game = game
        self.__image_url = image_url

    def execute(self):
        print('Make hint available [{}]'.format(self.__image_url))
        self.__game.set_hint_available(self.__image_url)


class HintCriticalAction(Action):
    def __init__(self, game, config):
        self.__game = game

    def execute(self):
        print('Make hint critical')
        self.__game.set_hint_critical()


class TurnLightOnAction(Action):
    def __init__(self, game, config):
        if not environment.is_development:
            self.connection = serial.Serial('/dev/ttyACM0', 57600)

    def execute(self):
        print('Turn light on')

        if not environment.is_development:
            self.connection.write(b'd13=1\n')
            self.connection.flush()
