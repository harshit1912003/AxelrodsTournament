from strats.base import COOPERATE, DEFECT
import matplotlib.pyplot as plt

class PrisonersDilemmaGame:
    def __init__(self, strategy1, strategy2, n):
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.n = n
        self.history = []
        self.payoff = {COOPERATE: {COOPERATE: (3, 3), DEFECT: (0, 5)},
                       DEFECT: {COOPERATE: (5, 0), DEFECT: (1, 1)}}
        self.score1 = 0
        self.score2 = 0
        self.scores1, self.scores2 = [], []

    def play_round(self):
        move1 = self.strategy1.move(self.history)
        move2 = self.strategy2.move(self.history)
        self.history.append((move1, move2))
        payoff1, payoff2 = self.payoff[move1][move2]
        self.score1 += payoff1
        self.score2 += payoff2

        self.scores1.append(self.score1)
        self.scores2.append(self.score2)

    def play_game(self):
        for _ in range(self.n):
            self.play_round()

    def get_scores(self):
        return self.score1, self.score2
    
    def plot_payoffs(self):
        plt.plot(self.scores1, label=f'Strategy 1: {self.strategy1.__class__.__name__}')
        plt.plot(self.scores2, label=f'Strategy 2: {self.strategy2.__class__.__name__}')        
        plt.xlabel('Rounds')
        plt.ylabel('Total Payoff')
        plt.legend()
        plt.show()


