import openescape
import pygame
import sys
import timer

pygame.init()
pygame.mouse.set_visible(False)

countdown_timer = timer.CountdownTimer(60 * 60 * 1000)
display = openescape.Display()
game = openescape.Game(countdown_timer, display)
game.start()