import matplotlib.pyplot as plt
from game.game import PrisonersDilemmaGame

import matplotlib.pyplot as plt

class Tournament:
    def __init__(self, participants, n_rounds=200):
        self.participants = participants
        self.n_rounds = n_rounds
        self.K = len(self.participants)

        self.resarr = {participant.__class__.__name__: [0] * (self.K * self.n_rounds) for participant in participants}

    def run_tournament(self):
        for i, strategy1 in enumerate(self.participants):
            for j, strategy2 in enumerate(self.participants):
                game = PrisonersDilemmaGame(strategy1, strategy2, self.n_rounds)
                game.play_game()
                for k in range(self.n_rounds):

                    current_index = self.n_rounds * j + k

                    if current_index == 0:
                        self.resarr[strategy1.__class__.__name__][current_index] = game.payoff[game.history[k][0]][game.history[k][1]][0]
                    else:
                        self.resarr[strategy1.__class__.__name__][current_index] = self.resarr[strategy1.__class__.__name__][current_index - 1] + game.payoff[game.history[k][0]][game.history[k][1]][0]

    def plot_graph(self):
        plt.figure(figsize=(10, 6))
        for strategy, payoffs in self.resarr.items():
            plt.plot(range(1, self.K * self.n_rounds + 1), payoffs, label=strategy)
        plt.xlabel("Iteration")
        plt.ylabel("Cumulative Payoffs")
        plt.title("Cumulative Payoffs for Each Strategy Over Time")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_results(self):

        strategies = list(self.resarr.keys())
        total_payoffs = [payoff[-1] for payoff in self.resarr.values()]
        plt.bar(strategies, total_payoffs)
        plt.xlabel('Strategies')
        plt.ylabel('Total Payoff')
        plt.title(f'Total Payoff of Each Strategy over {self.K * self.n_rounds} Rounds')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()