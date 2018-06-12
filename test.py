import logging
import openescape
import pygame

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
openescape.environment.use_arduino = True


pygame.init()

arduino = openescape.Arduino()

game_config = openescape.GameConfig.from_yaml_config_file_path(
    'examples/v2-game/game.yaml')
game = openescape.GameFactory.from_config(game_config, arduino)
game_engine = openescape.Engine()
game_engine.start_game(game)
