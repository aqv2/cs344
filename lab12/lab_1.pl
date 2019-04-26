a)

i. I built the representations this way because it seemed like the way that would work, given the tutorial.
    1. killer(butch)
    2. married(mia, marsellus)
    3. dead(zed)
    4. massageMia(X) :- kills(marsellus, X)
    5. goodDancer(X) :- loves(mia, X)
    6. nutritious(X); tasty(X) :- eats(jules)
ii. Prolog checks to see if the query is in its knowledge base or can be inferred from it. It can also check to see if a
    variable that you give is fulfilled by some of the conditions in its knowledge base.

b)
Prolog does have Modus Ponens. If you set up an if-then condition with the symbol :- then ask it a question about the
post-then portion, it will check to see if the condition is met.

c)
Horn clauses are at least as powerful as propositional logic, but they have the added power of being capable of
representing first-order logic statements as well.

d)
Prolog does support this distinction. Ask queries are preceded by a ?-, while tellings are not.