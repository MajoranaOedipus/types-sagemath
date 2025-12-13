from sage.arith.functions import lcm as lcm
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def CyclicSievingPolynomial(L, cyc_act=None, order=None, get_order: bool = False):
    """
    Return the unique polynomial ``p`` of degree smaller than ``order`` such
    that the triple ``(L, cyc_act, p)`` exhibits the Cyclic Sieving Phenomenon.

    If ``cyc_act`` is None, ``L`` is expected to contain the orbit lengths.

    INPUT:

    - ``L`` -- if ``cyc_act`` is ``None``: list of orbit sizes,
      otherwise list of objects

    - ``cyc_act`` -- (default: ``None``) bijective function from ``L`` to ``L``

    - ``order`` -- (default: ``None``) if set to an integer, this
        cyclic order of ``cyc_act`` is used (must be an integer multiple
        of the order of ``cyc_act``) otherwise, the order of ``cyc_action`` is
        used

    - ``get_order`` -- (default: ``False``) if ``True``, a tuple ``[p,n]``
      is returned where ``p`` is as above, and ``n`` is the order

    EXAMPLES::

        sage: from sage.combinat.cyclic_sieving_phenomenon import CyclicSievingPolynomial
        sage: S42 = Subsets([1,2,3,4], 2)
        sage: def cyc_act(S): return Set(i.mod(4) + 1 for i in S)
        sage: cyc_act([1,3])
        {2, 4}
        sage: cyc_act([1,4])
        {1, 2}
        sage: CyclicSievingPolynomial(S42, cyc_act)
        q^3 + 2*q^2 + q + 2
        sage: CyclicSievingPolynomial(S42, cyc_act, get_order=True)
        [q^3 + 2*q^2 + q + 2, 4]
        sage: CyclicSievingPolynomial(S42, cyc_act, order=8)
        q^6 + 2*q^4 + q^2 + 2
        sage: CyclicSievingPolynomial([4,2])
        q^3 + 2*q^2 + q + 2

    TESTS:

    We check that :issue:`13997` is handled::

        sage: CyclicSievingPolynomial(S42, cyc_act, order=8, get_order=True)
        [q^6 + 2*q^4 + q^2 + 2, 8]
        sage: CyclicSievingPolynomial(S42, cyc_act, order=11)
        Traceback (most recent call last):
        ...
        ValueError: order is not a multiple of the order of the cyclic action
    """
def CyclicSievingCheck(L, cyc_act, f, order=None) -> bool:
    """
    Return whether the triple ``(L, cyc_act, f)`` exhibits
    the cyclic sieving phenomenon.

    If ``cyc_act`` is None, ``L`` is expected to contain the orbit lengths.

    INPUT:

    - ``L`` -- if ``cyc_act`` is ``None``: list of orbit sizes,
      otherwise list of objects

    - ``cyc_act`` -- (default: ``None``) bijective function from ``L`` to ``L``

    - ``order`` -- (default: ``None``) if set to an integer, this
        cyclic order of ``cyc_act`` is used (must be an integer
        multiple of the order of ``cyc_act``) otherwise, the order of
        ``cyc_action`` is used

    EXAMPLES::

        sage: from sage.combinat.cyclic_sieving_phenomenon import *
        sage: from sage.combinat.q_analogues import q_binomial
        sage: S42 = Subsets([1,2,3,4], 2)
        sage: def cyc_act(S): return Set(i.mod(4) + 1 for i in S)
        sage: cyc_act([1,3])
        {2, 4}
        sage: cyc_act([1,4])
        {1, 2}
        sage: p = q_binomial(4,2); p
        q^4 + q^3 + 2*q^2 + q + 1
        sage: CyclicSievingPolynomial( S42, cyc_act )
        q^3 + 2*q^2 + q + 2
        sage: CyclicSievingCheck( S42, cyc_act, p )
        True
    """
def orbit_decomposition(L, cyc_act) -> list[list]:
    """
    Return the orbit decomposition of ``L`` by the action of ``cyc_act``.

    INPUT:

    - ``L`` -- list

    - ``cyc_act`` -- bijective function from ``L`` to ``L``

    OUTPUT: list of lists, the orbits under the cyc_act acting on ``L``

    EXAMPLES::

        sage: from sage.combinat.cyclic_sieving_phenomenon import *
        sage: S42 = Subsets([1,2,3,4], 2); S42
        Subsets of {1, 2, 3, 4} of size 2
        sage: def cyc_act(S): return Set(i.mod(4) + 1 for i in S)
        sage: cyc_act([1,3])
        {2, 4}
        sage: cyc_act([1,4])
        {1, 2}
        sage: orbits = orbit_decomposition(S42, cyc_act)
        sage: sorted([sorted(orb, key=sorted) for orb in orbits], key=len)
        [[{1, 3}, {2, 4}], [{1, 2}, {1, 4}, {2, 3}, {3, 4}]]
    """
