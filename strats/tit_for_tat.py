from .base import Strategy, COOPERATE, DEFECT

class TitForTat(Strategy):
    def move(self, history):
        if not history:
            return COOPERATE
        return history[-1][1]
