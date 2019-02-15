"""
This module implements local search on a simple sine function variant.

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = AbsVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    hill_climbing_results = []
    hill_climbing_speeds = []
    for i in range(1000):
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=1.0)
        start = time.time()
        hill_solution = hill_climbing(p)
        end = time.time()
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              )
        hill_climbing_speeds.append(end - start)
        hill_climbing_results.append(p.value(hill_solution))
        print('\t' + str(end - start))

    # Solve the problem using simulated annealing.
    annealing_results = []
    annealing_speeds = []
    for i in range(1000):
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=1.0)
        start2 = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        end2 = time.time()
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
              )
        annealing_speeds.append(end2 - start2)
        annealing_results.append(p.value(annealing_solution))
        print('\t' + str(end2 - start2))

    print('Hill-climbing max: ' + str(max(hill_climbing_results)))
    print('Hill-climbing avg: ' + str(sum(hill_climbing_results) / len(hill_climbing_results)))
    print('Hill-climbing avg speed: ' + (str(sum(hill_climbing_speeds) / len(hill_climbing_speeds))))
    print('Simulated annealing max: ' + str(max(annealing_results)))
    print('Simulated annealing avg: ' + str(sum(annealing_results) / len(annealing_results)))
    print('Simulated annealing avg speed: ' + (str(sum(annealing_speeds) / len(hill_climbing_speeds))))
