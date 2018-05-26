import pygame
import sys
import timer

class Engine(object):
	def __init__(self):
		self.clock = pygame.time.Clock()

	def start_game(self, game_config):
		self.countdown_timer = timer.CountdownTimer(game_config.duration_seconds() * 1000)
		self.countdown_timer.subscribe(self)

		print('Starting game [{}]'.format(game_config.title()))
		self.countdown_timer.start()

		self.__game_config = game_config

		while True:
			for event in pygame.event.get():
				if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
					self.exit()

				self.clock.tick(60)

	def on_tick(self, data):
		remaining_time_ms = data['remaining_time_ms']

		print('Time remaining: {} seconds'.format(remaining_time_ms // 1000))
		for trigger in self.__game_config.triggers():
			trigger.evaluate()

	def exit(self):
		pygame.quit()
		sys.exit()