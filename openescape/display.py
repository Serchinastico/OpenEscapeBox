import pygame


class Display:
    def __init__(self):
        screen_width = 480
        screen_height = 320
        self.screen = pygame.display.set_mode(
            [screen_width, screen_height], pygame.FULLSCREEN)
        self.font = pygame.font.Font('resources/fonts/DS-DIGI.TTF', 72)

    def display_text(self, text):
        rendered_text = self.font.render(text, True, (0, 128, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(rendered_text, (0, 0))
        pygame.display.flip()
