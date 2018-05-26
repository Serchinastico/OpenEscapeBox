import openescape
import pygame
import timer

openescape.environment.is_development = True

pygame.init()

game_config = openescape.GameConfig.from_yaml_config_file_path('examples/v1-game/game.yaml')
game_engine = openescape.Engine()

game_engine.start_game(game_config)