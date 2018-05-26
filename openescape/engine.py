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

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    self.exit()

            for component in self.__game.components():
                component.update()

            self.clock.tick(60)

    def on_tick(self, data):
        seconds_remaining = data['remaining_time_ms'] // 1000
        self.__game.set_seconds_remaining(seconds_remaining)

        print('Time remaining: {} seconds'.format(seconds_remaining))
        for trigger in self.__game.triggers():
            trigger.evaluate()

    def exit(self):
        pygame.quit()
        sys.exit()
