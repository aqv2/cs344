13.1
a)
    i. directlyIn(katarina, olga).
        directlyIn(olga, natasha).
        directlyIn(natasha, irina).
        in(X, Y) :- directlyIn(X, Y) ; in(Y, Z).

    ii. listtran([], []).
        listtran([Hg | Tg], [He | Te]) :-
        tran(Hg, He), listtran(Tg, Te).

b) Prolog does not do generalized Modus Ponens, because if it did, then its horn clause based approach would no longer be
    both consistent and complete. That is, if you use both generalized Modus Ponens and horn clauses, you can prove things
    that are not true.
