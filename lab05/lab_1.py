'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# # Compute P(Burglary | John and Mary both call).
# print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # elimination_ask() is a dynamic programming version of enumeration_ask().
# print(elimination_ask('Burglary',ict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
# print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # See the explanation of the algorithms in AIMA Section 14.4.

# Excercise a.i
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Explanation: This probability makes intuitive sense as 0.94; we can see the exact value in the distribution.

# Excercise a.ii
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Explanation: This is quite high simply because John mostly only calls if the Alarm goes off, and the alarm is
# quite likely to go off with just a burglary, regardless of whether there is an earthquake or not.

# Excercise a.iii
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# Explanation: This makes sense (as 0.374) because a burglary is so rare that, even if the alarm goes off,
# a burglary is fairly unlikely.

# Excercise a.iv
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# Explanation: This, being 0.284, makes sense. John and Mary both rarely call without an alarm, but an earthquake
# or a malfunction is much more likely than a burglary. What helps makes sense of this is that the Alarm
# malfunctioning and going off without a burglary or an earthquake is just as likely as a burglary.
