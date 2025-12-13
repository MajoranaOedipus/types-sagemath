from sage.rings.polynomial.pbori.PyPolyBoRi import Ring as Ring, WeakRingRef as WeakRingRef
from sage.rings.polynomial.pbori.gbcore import groebner_basis as groebner_basis
from sage.rings.polynomial.pbori.pbori import BooleSet as BooleSet, CCuddNavigator as CCuddNavigator, Monomial as Monomial, Polynomial as Polynomial, Variable as Variable, if_then_else as if_then_else

def to_fast_pickable(l):
    """
    Convert a list of polynomials into a builtin Python value, which is fast pickable and compact.

    INPUT:

    - ``l`` -- a list of Boolean polynomials

    OUTPUT:

    It is converted to a tuple consisting of
    - codes referring to the polynomials
    - list of conversions of nodes.
    The nodes are sorted, so that n occurs before n.else_branch(), n.then_branch()
    nodes are only listed, if they are not constant.

    A node is converted in this way:
    0 -> 0
    1 -> 1
    if_then_else(v,t,e) -> (v, index of then branch +2, index of else branch +2)
    the shift of +2 is for the constant values implicitly contained in the list.
    Each code c refers to the c-2-th position in the conversion list, if c >=2, else to
    the corresponding Boolean constant if c in {0, 1}

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori import Ring, Polynomial
        sage: from sage.rings.polynomial.pbori.parallel import to_fast_pickable, from_fast_pickable
        sage: r = Ring(1000)
        sage: x = r.variable
        sage: to_fast_pickable([Polynomial(1, r)])
        [[1], []]
        sage: to_fast_pickable([Polynomial(0, r)])
        [[0], []]
        sage: to_fast_pickable([x(0)])
        [[2], [(0, 1, 0)]]
        sage: to_fast_pickable([x(0)*x(1)+x(1)])
        [[2], [(0, 3, 3), (1, 1, 0)]]
        sage: to_fast_pickable([x(1)])
        [[2], [(1, 1, 0)]]
        sage: to_fast_pickable([x(0)+1])
        [[2], [(0, 1, 1)]]
        sage: to_fast_pickable([x(0)*x(1)])
        [[2], [(0, 3, 0), (1, 1, 0)]]
        sage: to_fast_pickable([x(0)*x(1)+x(1)])
        [[2], [(0, 3, 3), (1, 1, 0)]]
        sage: to_fast_pickable([x(0)*x(1)+x(2)])
        [[2], [(0, 3, 4), (1, 1, 0), (2, 1, 0)]]
        sage: p=x(5)*x(23) + x(5)*x(24)*x(59) + x(5) + x(6)*x(23)*x(89) + x(6)*x(60)*x(89) + x(23) + x(24)*x(89) + x(24) + x(60)*x(89) + x(89) + 1
        sage: from_fast_pickable(to_fast_pickable([p]), r)==[p]
        True
        sage: to_fast_pickable([x(0)*x(1), Polynomial(0, r), Polynomial(1, r), x(3)])
        [[2, 0, 1, 4], [(0, 3, 0), (1, 1, 0), (3, 1, 0)]]
    """
def from_fast_pickable(l, r):
    """
    Undo the operation :func:`to_fast_pickable`.

    The first argument is an object created by :func:`to_fast_pickable`.

    For the specified format, see the documentation of :func:`to_fast_pickable`.
    The second argument is ring, in which this polynomial should be created.

    INPUT:

    See OUTPUT of :func:`to_fast_pickable`.

    OUTPUT: list of Boolean polynomials

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori import Ring
        sage: from sage.rings.polynomial.pbori.parallel import from_fast_pickable
        sage: r = Ring(1000)
        sage: x = r.variable
        sage: from_fast_pickable([[1], []], r)
        [1]
        sage: from_fast_pickable([[0], []], r)
        [0]
        sage: from_fast_pickable([[2], [(0, 1, 0)]], r)
        [x(0)]
        sage: from_fast_pickable([[2], [(1, 1, 0)]], r)
        [x(1)]
        sage: from_fast_pickable([[2], [(0, 1, 1)]], r)
        [x(0) + 1]
        sage: from_fast_pickable([[2], [(0, 3, 0), (1, 1, 0)]], r)
        [x(0)*x(1)]
        sage: from_fast_pickable([[2], [(0, 3, 3), (1, 1, 0)]], r)
        [x(0)*x(1) + x(1)]
        sage: from_fast_pickable([[2], [(0, 3, 4), (1, 1, 0), (2, 1, 0)]], r)
        [x(0)*x(1) + x(2)]
        sage: from_fast_pickable([[2, 0, 1, 4], [(0, 3, 0), (1, 1, 0), (3, 1, 0)]], r)
        [x(0)*x(1), 0, 1, x(3)]
    """
def pickle_polynomial(self): ...
def pickle_bset(self): ...
def pickle_monom(self): ...
def pickle_var(self): ...
def pickle_ring(self): ...
def groebner_basis_first_finished(I, *l):
    """

    INPUT:

    - ``I`` -- ideal
    - ``l`` -- keyword dictionaries, which will be keyword arguments to
      ``groebner_basis``

    OUTPUT:

    - tries to compute ``groebner_basis(I, **kwd)`` for kwd in l
    - returns the result of the first terminated computation

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori.PyPolyBoRi import Ring
        sage: r = Ring(1000)
        sage: ideal = [r.variable(1)*r.variable(2)+r.variable(2)+r.variable(1)]
        sage: from sage.rings.polynomial.pbori.parallel import groebner_basis_first_finished
        sage: groebner_basis_first_finished(ideal, dict(heuristic=True), dict(heuristic=False))
        [x1, x2]
    """
