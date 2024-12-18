from .base import Strategy, COOPERATE, DEFECT

class Harrington(Strategy):
    def move(self, history):
        if len(history) >= 2 and history[-1][1] == DEFECT and history[-2][1] == DEFECT:
            return DEFECT
        return COOPERATE
