import random
from .base import Strategy, COOPERATE, DEFECT

class Joss(Strategy):
    def __init__(self, prob_defect=0.1):
        self.prob_defect = prob_defect

    def move(self, history):
        if random.random() < self.prob_defect:
            return DEFECT
        if not history:
            return COOPERATE
        return history[-1][1]

