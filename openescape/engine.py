import logging
import pygame
import sys
import time
from openescape.game import Game


class Engine(object):
    def start_game(self, game):
        clock = pygame.time.Clock()
        on_frame_listeners = [
            GameComponentUpdater(game),
            GameDurationUpdater(game),
            GameTriggerEvaluator(game),
            FpsMeter(),
            PyGameEventProcessor(game),
        ]

        logging.info('Starting game')
        while not game.is_finished():
            for listener in on_frame_listeners:
                listener.on_frame()

            clock.tick(60)

        pygame.quit()
        sys.exit()


class OnFrameListener(object):
    def on_frame(self):
        pass


class FpsMeter(OnFrameListener):
    def __init__(self):
        self.__num_frames = 0
        self.__last_measure_time = None

    def on_frame(self):
        if self.__last_measure_time is None:
            self.__last_measure_time = time.time()

        self.__num_frames += 1

        if time.time() - self.__last_measure_time >= 1:
            logging.debug('Game running at {} FPS, or {:.2f} ms/frame'.format(self.__num_frames,
                                                                              1000 / self.__num_frames))
            self.__num_frames = 0
            self.__last_measure_time += 1


class GameComponentUpdater(OnFrameListener):
    def __init__(self, game):
        self.__game = game

    def on_frame(self):
        for component in self.__game.components.values():
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
            logging.info('Time remaining: {} seconds'.format(seconds_remaining))


class GameTriggerEvaluator(OnFrameListener):
    def __init__(self, game):
        self.__game = game

    def on_frame(self):
        for trigger in self.__game.triggers:
            trigger.evaluate()


class PyGameEventProcessor(OnFrameListener):
    def __init__(self, game):
        self.__game = game

    def on_frame(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                self.__game.trigger_loss()
