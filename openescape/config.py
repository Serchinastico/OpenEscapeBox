from ruamel.yaml import YAML


class GameConfig(object):
    def __init__(self, config):
        self.__config = config

    @staticmethod
    def from_yaml_config_file_path(path):
        file = open(path)
        config = YAML().load(file)
        return GameConfig(config)

    def duration_seconds(self):
        return self.__config.get('durationSeconds')

    def title(self):
        return self.__config.get('title')

    def actions(self):
        return self.__config.get('actions')

    def components(self):
        return self.__config.get('components')

    def conditions(self):
        return self.__config.get('conditions')

    def triggers(self):
        return self.__config.get('triggers')
