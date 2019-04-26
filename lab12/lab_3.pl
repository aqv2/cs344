a)
witch(X) :- burn(X)
burn(X) :- wood(X)
wood(X) ; stone(X) :- bridge(X)
wood(X) ; duck(X) :- float(X)
sameWeight(duck, X) :- wood(X)
sameWeight(duck, X).
