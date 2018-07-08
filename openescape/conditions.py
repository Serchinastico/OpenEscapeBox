class Condition(object):
    def is_true(self):
        return False


class AllCondition(Condition):
    def __init__(self, conditions):
        self.__conditions = conditions

    def is_true(self):
        return all(condition.is_true() for condition in self.__conditions)


class AlwaysFalseCondition(Condition):
    def is_true(self):
        return False


class AlwaysTrueCondition(Condition):
    def is_true(self):
        return True


class AnyCondition(Condition):
    def __init__(self, conditions):
        self.__conditions = conditions

    def is_true(self):
        return any(condition.is_true() for condition in self.__conditions)


class ButtonPressedCondition(Condition):
    def __init__(self, game, button):
        self.__game = game
        self.__button = button

    def is_true(self):
        return self.__button.is_pressed()


class LedOnCondition(Condition):
    def __init__(self, game, led):
        self.__game = game
        self.__led = led

    def is_true(self):
        return self.__led.is_on()


class SecondsRemainingCondition(Condition):
    def __init__(self, game, seconds_remaining):
        self.__game = game
        self.__seconds_remaining = seconds_remaining

    def is_true(self):
        return self.__game.seconds_remaining() <= self.__seconds_remaining
