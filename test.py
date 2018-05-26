import openescape
import pygame
import timer
import time
import openescape.arduino

ar = openescape.arduino.Arduino()
while True:
    value = ar.read('d12')
    time.sleep(0.05)


# openescape.environment.is_development = True

# pygame.init()

# game_config = openescape.GameConfig.from_yaml_config_file_path('examples/simple-game/game.yaml')
# game_engine = openescape.Engine()

# game_engine.start_game(game_config)
