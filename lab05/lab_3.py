from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happyNetwork = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# a.i
print(enumeration_ask('Raise', dict(Sunny=T), happyNetwork).show_approx())
# This is really a depressingly low probability, sitting at an even 0.01, which is just straight up the probability
# of getting a raise. Which is really low.

# a.ii
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happyNetwork).show_approx())
# This is not very much more likely, sitting at .0142. The fact that you are happy does eliminate the times when
# you are not happy despite it being sunny from the equation.

# b.i
print(enumeration_ask('Raise', dict(Happy=T), happyNetwork).show_approx())
# This is yet slightly more likely again, since you aren't always happy when it is sunny, but you are almost always
# happy when you have gotten a raise. So the fact that you are happy makes it more likely that you got a raise than
# the fact that it is sunny does, even though the probability of having gotten a raise is still pretty miniscule.

# b.ii
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happyNetwork).show_approx())
# This is the highest probability, sitting at almost 0.083. This makes sense, because it eliminates the
# (potentially) confounding variable of whether or not it is sunny on hour happiness, and leaves you at just the
# getting a raise making you happy (which is likely -- if you got a raise), and the probability that you are
# happy despite the clouds and lack of a raise (which is quite likely, in comparison to the probability of getting
# a raise.