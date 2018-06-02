import pygame
import sys
import time
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
            GameComponentUpdater(self.__game),
            GameDurationUpdater(self.__game),
            PyGameEventProcessor(),
        ]

        while True:
            for listener in on_frame_listeners:
                listener.on_frame()

            self.clock.tick(60)

    def on_tick(self, data):
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


class GameDurationUpdater(OnFrameListener):
    def __init__(self, game):
        self.__game = game
        self.__game_duration_seconds = game.seconds_remaining()
        self.__first_frame_time = None
        self.__seconds_remaining = None

    def on_frame(self):
        if self.__first_frame_time is None:
            self.__first_frame_time = time.time()

        seconds_remaining = self.__game_duration_seconds - \
            int(time.time() - self.__first_frame_time)

        if seconds_remaining != self.__seconds_remaining:
            self.__seconds_remaining = seconds_remaining
            self.__game.set_seconds_remaining(seconds_remaining)
            print('Time remaining: {} seconds'.format(seconds_remaining))


class PyGameEventProcessor(OnFrameListener):
    def on_frame(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
