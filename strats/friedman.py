from .base import Strategy, COOPERATE, DEFECT


class Friedman(Strategy):
    def __init__(self):
        self.defected = False

    def move(self, history):
        if any(move[1] == DEFECT for move in history):
            self.defected = True
        return DEFECT if self.defected else COOPERATE
