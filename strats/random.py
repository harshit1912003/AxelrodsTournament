import random
from .base import Strategy, COOPERATE, DEFECT

class RandomStrategy(Strategy):
    def move(self, history):
        return random.choice([COOPERATE, DEFECT])
