from .arithgroup_element import ArithmeticSubgroupElement as ArithmeticSubgroupElement
from .congroup_gamma0 import Gamma0_class as Gamma0_class
from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd
from sage.modular.cusps import Cusp as Cusp
from sage.modular.modsym.p1list import lift_to_sl2z as lift_to_sl2z
from sage.rings.integer_ring import ZZ as ZZ

def is_SL2Z(x):
    """
    Return ``True`` if x is the modular group `\\SL_2(\\ZZ)`.

    EXAMPLES::

        sage: from sage.modular.arithgroup.all import is_SL2Z
        sage: is_SL2Z(SL2Z)
        doctest:warning...
        DeprecationWarning: The function is_SL2Z is deprecated; use 'isinstance(..., SL2Z_class)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        True
        sage: is_SL2Z(Gamma0(6))
        False
    """

class SL2Z_class(Gamma0_class):
    """
    The full modular group `\\SL_2(\\ZZ)`, regarded as a congruence
    subgroup of itself.
    """
    def __init__(self) -> None:
        """
        The modular group `\\SL_2(\\Z)`.

        EXAMPLES::

            sage: G = SL2Z; G
            Modular Group SL(2,Z)
            sage: G.gens()
            (
            [ 0 -1]  [1 1]
            [ 1  0], [0 1]
            )
            sage: G.0
            [ 0 -1]
            [ 1  0]
            sage: G.1
            [1 1]
            [0 1]
            sage: latex(G)
            \\mbox{\\rm SL}_2(\\Bold{Z})
            sage: G([1,-1,0,1])
            [ 1 -1]
            [ 0  1]
            sage: TestSuite(G).run()
            sage: SL2Z.0 * SL2Z.1
            [ 0 -1]
            [ 1  1]
            sage: SL2Z is loads(dumps(SL2Z))
            True
        """
    def __reduce__(self):
        """
        Used for pickling ``self``.

        EXAMPLES::

            sage: SL2Z.__reduce__()
            (<function _SL2Z_ref at ...>, ())
        """
    def is_subgroup(self, right) -> bool:
        """
        Return ``True`` if ``self`` is a subgroup of ``right``.

        EXAMPLES::

            sage: SL2Z.is_subgroup(SL2Z)
            True
            sage: SL2Z.is_subgroup(Gamma1(1))
            True
            sage: SL2Z.is_subgroup(Gamma0(6))
            False
        """
    def reduce_cusp(self, c):
        """
        Return the unique reduced cusp equivalent to c under the
        action of ``self``. Always returns Infinity, since there is only
        one equivalence class of cusps for `SL_2(Z)`.

        EXAMPLES::

            sage: SL2Z.reduce_cusp(Cusps(-1/4))
            Infinity
        """
    def random_element(self, bound: int = 100, *args, **kwds):
        """
        Return a random element of `\\SL_2(\\ZZ)` with entries whose
        absolute value is strictly less than bound (default: 100).
        Additional arguments and keywords are passed to the random_element
        method of ZZ.

        (Algorithm: Generate a random pair of integers at most bound. If they
        are not coprime, throw them away and start again. If they are, find an
        element of `\\SL_2(\\ZZ)` whose bottom row is that, and
        left-multiply it by `\\begin{pmatrix} 1 & w \\\\ 0 & 1\\end{pmatrix}` for
        an integer `w` randomly chosen from a small enough range that the
        answer still has entries at most bound.)

        It is, unfortunately, not true that all elements of SL2Z with entries <
        bound appear with equal probability; those with larger bottom rows are
        favoured, because there are fewer valid possibilities for w.

        EXAMPLES::

            sage: s = SL2Z.random_element()
            sage: s.parent() is SL2Z
            True
            sage: all(a in range(-99, 100) for a in list(s))
            True
            sage: S = set()
            sage: while len(S) < 180:
            ....:     s = SL2Z.random_element(5)
            ....:     assert all(a in range(-4, 5) for a in list(s))
            ....:     assert s.parent() is SL2Z
            ....:     assert s in SL2Z
            ....:     S.add(s)

        Passes extra positional or keyword arguments through::

            sage: SL2Z.random_element(5, distribution='1/n').parent() is SL2Z
            True
        """

SL2Z: SL2Z_class    # TODO: with category
