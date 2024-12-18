# Axelrod's Tournament Simulation

This repository contains a Python-based simulation of the classic **Prisoner's Dilemma**, a foundational concept in game theory. The simulation explores how different strategies interact over multiple iterations of the game.

## Key Features

### 1. Multiple Predefined Strategies
The simulation includes the following built-in strategies:

- **Tit-for-Tat**: Cooperates on the first move, then mimics the opponent's last action.
- **Random**: Chooses randomly between cooperating and defecting.
- **Friedman/GrimTrigger**: Cooperates until the opponent defects, then always defects.
- **Joss**: Similar to Tit-for-Tat, but occasionally defects.
- **Harrington**: Defects after the opponent defects twice in a row, else cooperates.
- **AlwaysCooperate**: Always cooperates.
- **AlwaysDefect**: Always defects.
  
### 2. Tournament Framework
The simulation implements a tournament framework to compare strategies:
- Tracks cumulative payoffs for each strategy.
- Provides a round-robin tournament format to evaluate all pairwise interactions.

### 3. Graphical Result Representation
Results are visualized as graphs showing the cumulative payoff of each strategy across iterations.

---

## Implementation Details

### Framework Overview
The simulation is implemented in Python and structured to allow maximum flexibility for extensions. Key components include:

1. **Strategy Interface**
   Each strategy is defined as a class implementing a `move()` method, which determines the next action based on the game history.

2. **Game Simulator**
   Handles the logic for individual games between two strategies, including payoff calculations.

3. **Tournament Engine**
   Automates multiple rounds of games between all strategies, collects payoffs, and aggregates results.

4. **Visualization Module**
   Uses libraries like Matplotlib to create visual representations of cumulative payoffs.

### Example: Adding a Custom Strategy
Here is how you can define and add your own strategy:

```python
class AlwaysCooperate:
    def move(self, history):
        return COOPERATE
```

Register the strategy in the tournament framework:
```python

my_strategy = AlwaysCooperate()
tournament = Tournament([my_strategy, TitForTat(), Random()], n_rounds = 100)
tournament.run_tournament()
```

### Visualizing Results
After running the tournament, the results can be plotted:

```python
tournament.plot_graph()
tournament.plot_results()
```
