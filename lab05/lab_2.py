from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancerNetwork = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
    ])

# a
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancerNetwork).show_approx())

# b
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancerNetwork).show_approx())

# Honestly, more than anything, the results are a relief. Since the probability of having cancer is so low,
# it is still far more likely that both tests were false positives than that you actually have cancer. It is four
# times (0.2 * 0.2 = 0.04) more likely that both tests were false positives than it is that you have cancer. As such
# one failed test makes it way, WAY less likely that you have cancer; it goes from a 17% chance with both tests
# positive to a 0.565% chance.

print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancerNetwork).show_approx())