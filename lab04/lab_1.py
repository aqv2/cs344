'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
Modified by Alastair Van Maren
'''

from probability import JointProbDist, enumerate_joint_ask

# # The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
# P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
# T, F = True, False
# P[T, T, T] = 0.108; P[T, T, F] = 0.012
# P[F, T, T] = 0.072; P[F, T, F] = 0.008
# P[T, F, T] = 0.016; P[T, F, F] = 0.064
# P[F, F, T] = 0.144; P[F, F, F] = 0.576
#
# # Compute P(Cavity|Catch=T), as the homework requests
# PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
# print(PC.show_approx())

# Exercise 4.1c
# Flipping two coins probabilities setup
P2 = JointProbDist(['Coin1', 'Coin2'])
# We'll say that what is true or false, here is whether the coin got heads; ergo heads is true and tails is false
T, F = True, False
# Since the coins flips are each independent events the probability of any specific outcome is .5 * .5, always
P2[T, T] = 0.25; P2[T, F] = 0.25
P2[F, T] = 0.25; P2[F, F] = 0.25

# Asking what the probability that Coin2 will be Heads given that Coin1 is Heads
PC2 = enumerate_joint_ask('Coin2', {"Coin1": T}, P2)
# This yields a 50-50 chance of Coin2 being heads. Again, this makes sense because the result of Coin1 in no way
# changes the probability of Coin2's result.
print(PC2.show_approx())
