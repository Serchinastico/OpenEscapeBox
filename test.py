import openescape
import pygame
import timer
import time

openescape.environment.is_development = True

pygame.init()

arduino = openescape.Arduino()

game_config = openescape.GameConfig.from_yaml_config_file_path(
    'examples/v1-game/game.yaml')
game_engine = openescape.Engine(arduino)

game_engine.start_game(game_config)
