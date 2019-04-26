a)
    i.
        1. yes. bread.
        2. yes. bread.
            note: 'Bread' indicates a variable since it begins with a capital letter, and variables unify with anything.
        8. yes. food(bread)
        9. yes. food(bread, sausage)
        14. yes. meal(food(bread), drink(beer))

    ii.
        Two terms unify if they are the same term or if they contain variables that can be uniformly instantiated with
        terms in such a way that the resulting terms are equal. In trivial cases, this is simple. In non-trivial cases
        Prolog fiddles with the contents of the variables in an attempt to get the terms to be the same. If it cannot do
        this, then it will say that no, they do not unify.
b)
It does not use unification, no. Because it does not need to. Unification is a tool more appropriate to first-order logic,
not propositional logic.

c)
Prolog inference does not use resolution. That is because resolution is a tool for inference, and Prolog uses unification
rather than inference to arrive at its conclusions.