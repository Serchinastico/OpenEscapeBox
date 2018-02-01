import pygame
import sys

class Game:
	def __init__(self, countdown_timer, display):
		self.countdown_timer = countdown_timer
		self.countdown_timer.subscribe(self)
		self.display = display

	def on_tick(self, data):
		remaining_time_ms = data['remaining_time_ms']
		minutes, seconds = divmod(remaining_time_ms / 1000, 60)
		hours, minutes = divmod(minutes, 60)
		remaining_time_text = '%d:%02d:%02d' % (hours, minutes, seconds)

		self.display.display_text(remaining_time_text)

	def start(self):
		self.countdown_timer.start()

		while True:
			for event in pygame.event.get():
				if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
					self.exit()

	def exit(self):
		pygame.quit()
		sys.exit()