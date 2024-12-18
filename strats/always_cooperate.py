from .base import Strategy, COOPERATE, DEFECT


class AlwaysCooperate(Strategy):
    def move(self, history):
        return COOPERATE
