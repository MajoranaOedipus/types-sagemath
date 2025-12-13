from _typeshed import Incomplete
from collections.abc import Generator
from sage.algebras.lie_algebras.lie_algebra import LieAlgebra as LieAlgebra
from sage.arith.misc import bernoulli as bernoulli, factorial as factorial
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.combinat.integer_lists import IntegerListsLex as IntegerListsLex
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import canonical_coercion as canonical_coercion

def bch_iterator(X=None, Y=None) -> Generator[Incomplete]:
    """
    A generator function which returns successive terms of the
    Baker-Campbell-Hausdorff formula.

    INPUT:

    - ``X`` -- (optional) an element of a Lie algebra
    - ``Y`` -- (optional) an element of a Lie algebra

    The BCH formula is an expression for `\\log(\\exp(X)\\exp(Y))` as a sum of Lie
    brackets of ``X`` and ``Y`` with rational coefficients. In arbitrary Lie
    algebras, the infinite sum is only guaranteed to converge for ``X`` and
    ``Y`` close to zero.

    If the elements ``X`` and ``Y`` are not given, then the iterator will
    return successive terms of the abstract BCH formula, i.e., the BCH formula
    for the generators of the free Lie algebra on 2 generators.

    If the Lie algebra containing ``X`` and ``Y`` is not nilpotent, the
    iterator will output infinitely many elements. If the Lie algebra is
    nilpotent, the number of elements outputted is equal to the nilpotency step.

    EXAMPLES:

    The terms of the abstract BCH formula up to fifth order brackets::

        sage: from sage.algebras.lie_algebras.bch import bch_iterator
        sage: bch = bch_iterator()
        sage: next(bch)
        X + Y
        sage: next(bch)
        1/2*[X, Y]
        sage: next(bch)
        1/12*[X, [X, Y]] + 1/12*[[X, Y], Y]
        sage: next(bch)
        1/24*[X, [[X, Y], Y]]
        sage: next(bch)
        -1/720*[X, [X, [X, [X, Y]]]] + 1/180*[X, [X, [[X, Y], Y]]]
        + 1/360*[[X, [X, Y]], [X, Y]] + 1/180*[X, [[[X, Y], Y], Y]]
        + 1/120*[[X, Y], [[X, Y], Y]] - 1/720*[[[[X, Y], Y], Y], Y]

    For nilpotent Lie algebras the BCH formula only has finitely many terms::

        sage: L = LieAlgebra(QQ, 2, step=3)
        sage: L.inject_variables()
        Defining X_1, X_2, X_12, X_112, X_122
        sage: [Z for Z in bch_iterator(X_1, X_2)]
        [X_1 + X_2, 1/2*X_12, 1/12*X_112 + 1/12*X_122]
        sage: [Z for Z in bch_iterator(X_1 + X_2, X_12)]
        [X_1 + X_2 + X_12, 1/2*X_112 - 1/2*X_122, 0]

    The elements ``X`` and ``Y`` don't need to be elements of the same Lie
    algebra if there is a coercion from one to the other::

        sage: L = LieAlgebra(QQ, 3, step=2)
        sage: L.inject_variables()
        Defining X_1, X_2, X_3, X_12, X_13, X_23
        sage: S = L.subalgebra(X_1, X_2)
        sage: bch1 = [Z for Z in bch_iterator(S(X_1), S(X_2))]; bch1
        [X_1 + X_2, 1/2*X_12]
        sage: bch1[0].parent() == S
        True
        sage: bch2 = [Z for Z in bch_iterator(S(X_1), X_3)]; bch2
        [X_1 + X_3, 1/2*X_13]
        sage: bch2[0].parent() == L
        True

    The BCH formula requires a coercion from the rationals::

        sage: L.<X,Y,Z> = LieAlgebra(ZZ, 2, step=2)
        sage: bch = bch_iterator(X, Y); next(bch)
        Traceback (most recent call last):
        ...
        TypeError: the BCH formula is not well defined since Integer Ring has no coercion from Rational Field

    TESTS:

    Compare to the BCH formula up to degree 5 given by wikipedia::

        sage: from sage.algebras.lie_algebras.bch import bch_iterator
        sage: bch = bch_iterator()
        sage: L.<X,Y> = LieAlgebra(QQ)
        sage: L = L.Lyndon()
        sage: computed_BCH = L.sum(next(bch) for k in range(5))
        sage: wikiBCH = X + Y + 1/2*L[X,Y] + 1/12*(L[X,[X,Y]] + L[Y,[Y,X]])
        sage: wikiBCH += -1/24*L[Y,[X,[X,Y]]]
        sage: wikiBCH += -1/720*(L[Y,[Y,[Y,[Y,X]]]] + L[X,[X,[X,[X,Y]]]])
        sage: wikiBCH += 1/360*(L[X,[Y,[Y,[Y,X]]]] + L[Y,[X,[X,[X,Y]]]])
        sage: wikiBCH += 1/120*(L[Y,[X,[Y,[X,Y]]]] + L[X,[Y,[X,[Y,X]]]])
        sage: computed_BCH == wikiBCH
        True

    ALGORITHM:

    The BCH formula `\\log(\\exp(X)\\exp(Y)) = \\sum_k Z_k` is computed starting
    from `Z_1 = X + Y`, by the recursion

    .. MATH::

        (m+1)Z_{m+1} =  \\frac{1}{2}[X - Y, Z_m]
        + \\sum_{2\\leq 2p \\leq m}\\frac{B_{2p}}{(2p)!}\\sum_{k_1+\\cdots+k_{2p}=m}
        [Z_{k_1}, [\\cdots [Z_{k_{2p}}, X + Y]\\cdots],

    where `B_{2p}` are the Bernoulli numbers, see Lemma 2.15.3. in [Var1984]_.

    .. WARNING::

        The time needed to compute each successive term increases exponentially.
        For example on one machine iterating through `Z_{11},...,Z_{18}` for a
        free Lie algebra, computing each successive term took 4-5 times longer,
        going from 0.1s for `Z_{11}` to 21 minutes for `Z_{18}`.
    """
