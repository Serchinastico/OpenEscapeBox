import pygame
import sys
import timer
from openescape.game import Game


class Engine(object):
    def __init__(self, arduino):
        self.clock = pygame.time.Clock()
        self.__arduino = arduino

    def start_game(self, game_config):
        self.__game = Game(game_config, self.__arduino)

        self.countdown_timer = timer.CountdownTimer(
            game_config.duration_seconds() * 1000)
        self.countdown_timer.subscribe(self)

        print('Starting game [{}]'.format(game_config.title()))
        self.countdown_timer.start()

        on_frame_listeners = [
            PyGameEventProcessor(),
            GameComponentUpdater(self.__game)
        ]

        while True:
            for listener in on_frame_listeners:
                listener.on_frame()

            self.clock.tick(60)

    def on_tick(self, data):
        seconds_remaining = data['remaining_time_ms'] // 1000
        self.__game.set_seconds_remaining(seconds_remaining)

        print('Time remaining: {} seconds'.format(seconds_remaining))
        for trigger in self.__game.triggers():
            trigger.evaluate()


class OnFrameListener(object):
    def on_frame(self):
        pass


class GameComponentUpdater(OnFrameListener):
    def __init__(self, game):
        self.__game = game

    def on_frame(self):
        for component in self.__game.components().values():
            component.update()


class PyGameEventProcessor(OnFrameListener):
    def on_frame(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
