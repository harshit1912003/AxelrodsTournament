from .base import Strategy, COOPERATE, DEFECT

class AlwaysDefect(Strategy):
    def move(self, history):
        return DEFECT
