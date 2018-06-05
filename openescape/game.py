class Game:
    def __init__(self, duration_seconds):
        self.__seconds_remaining = duration_seconds
        self.__is_finished = False
        self.actions = {}
        self.components = {}
        self.conditions = {}
        self.triggers = []

    def is_finished(self):
        return self.__is_finished

    def seconds_remaining(self):
        return self.__seconds_remaining

    def set_hint_available(self, image_url):
        pass

    def set_hint_critical(self):
        pass

    def set_seconds_remaining(self, seconds_remaining):
        self.__seconds_remaining = seconds_remaining

    def trigger_loss(self):
        self.__is_finished = True

    def trigger_victory(self):
        self.__is_finished = True
