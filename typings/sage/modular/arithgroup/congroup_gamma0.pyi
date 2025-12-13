from .congroup_gamma1 import Gamma1_class as Gamma1_class
from .congroup_gammaH import GammaH_class as GammaH_class
from .congroup_generic import CongruenceSubgroup as CongruenceSubgroup
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import divisors as divisors, euler_phi as euler_phi, gcd as gcd, kronecker_symbol as kronecker_symbol, moebius as moebius
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.modular.cusps import Cusp as Cusp
from sage.modular.modsym.p1list import P1List as P1List, lift_to_sl2z as lift_to_sl2z
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ

def is_Gamma0(x):
    """
    Return ``True`` if x is a congruence subgroup of type Gamma0.

    EXAMPLES::

        sage: from sage.modular.arithgroup.congroup_gamma0 import is_Gamma0
        sage: is_Gamma0(SL2Z)
        doctest:warning...
        DeprecationWarning: The function is_Gamma0 is deprecated; use 'isinstance(..., Gamma0_class)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        True
        sage: is_Gamma0(Gamma0(13))
        True
        sage: is_Gamma0(Gamma1(6))
        False
    """
def Gamma0_constructor(N):
    """
    Return the congruence subgroup Gamma0(N).

    EXAMPLES::

        sage: G = Gamma0(51) ; G # indirect doctest
        Congruence Subgroup Gamma0(51)
        sage: G == Gamma0(51)
        True
        sage: G is Gamma0(51)
        True
    """

class Gamma0_class(GammaH_class):
    """
    The congruence subgroup `\\Gamma_0(N)`.

    TESTS::

        sage: Gamma0(11).dimension_cusp_forms(2)
        1
        sage: a = Gamma0(1).dimension_cusp_forms(2); a
        0
        sage: type(a)
        <class 'sage.rings.integer.Integer'>
        sage: Gamma0(5).dimension_cusp_forms(0)
        0
        sage: Gamma0(20).dimension_cusp_forms(1)
        0
        sage: Gamma0(20).dimension_cusp_forms(4)
        6

        sage: Gamma0(23).dimension_cusp_forms(2)
        2
        sage: Gamma0(1).dimension_cusp_forms(24)
        2
        sage: Gamma0(3).dimension_cusp_forms(3)
        0
        sage: Gamma0(11).dimension_cusp_forms(-1)
        0

        sage: Gamma0(22).dimension_new_cusp_forms()
        0
        sage: Gamma0(100).dimension_new_cusp_forms(2, 5)
        5

    Independently compute the dimension 5 above::

        sage: m = ModularSymbols(100, 2, sign=1).cuspidal_subspace()
        sage: m.new_subspace(5)
        Modular Symbols subspace of dimension 5 of
         Modular Symbols space of dimension 18 for Gamma_0(100)
          of weight 2 with sign 1 over Rational Field
    """
    def __init__(self, level) -> None:
        """
        The congruence subgroup `\\Gamma_0(N)`.

        EXAMPLES::

            sage: G = Gamma0(11); G
            Congruence Subgroup Gamma0(11)
            sage: TestSuite(G).run()
            sage: G is loads(dumps(G))
            True

        TESTS::

            sage: g = Gamma0(5)([1,1,0,1])
            sage: g in Gamma0(7)
            True
            sage: g = Gamma0(5)([1,0,5,1])
            sage: g in Gamma0(7)
            False
            sage: g = Gamma0(2)([1,0,0,1])
            sage: g in SL2Z
            True
        """
    def __reduce__(self):
        """
        Used for pickling ``self``.

        EXAMPLES::

            sage: Gamma0(22).__reduce__()
            (<function Gamma0_constructor at ...>, (22,))
        """
    def divisor_subgroups(self):
        """
        Return the subgroups of SL2Z of the form Gamma0(M) that contain this subgroup,
        i.e. those for M a divisor of N.

        EXAMPLES::

            sage: Gamma0(24).divisor_subgroups()
            [Modular Group SL(2,Z),
             Congruence Subgroup Gamma0(2),
             Congruence Subgroup Gamma0(3),
             Congruence Subgroup Gamma0(4),
             Congruence Subgroup Gamma0(6),
             Congruence Subgroup Gamma0(8),
             Congruence Subgroup Gamma0(12),
             Congruence Subgroup Gamma0(24)]
        """
    def is_even(self) -> bool:
        """
        Return ``True`` precisely if this subgroup contains the matrix -1.

        Since `\\Gamma0(N)` always contains the matrix -1, this always
        returns ``True``.

        EXAMPLES::

            sage: Gamma0(12).is_even()
            True
            sage: SL2Z.is_even()
            True
        """
    def is_subgroup(self, right) -> bool:
        """
        Return ``True`` if ``self`` is a subgroup of ``right``.

        EXAMPLES::

            sage: G = Gamma0(20)
            sage: G.is_subgroup(SL2Z)
            True
            sage: G.is_subgroup(Gamma0(4))
            True
            sage: G.is_subgroup(Gamma0(20))
            True
            sage: G.is_subgroup(Gamma0(7))
            False
            sage: G.is_subgroup(Gamma1(20))
            False
            sage: G.is_subgroup(GammaH(40, []))
            False
            sage: Gamma0(80).is_subgroup(GammaH(40, [31, 21, 17]))
            True
            sage: Gamma0(2).is_subgroup(Gamma1(2))
            True
        """
    def coset_reps(self) -> Generator[Incomplete]:
        """
        Return representatives for the right cosets of this congruence
        subgroup in `\\SL_2(\\ZZ)` as a generator object.

        Use ``list(self.coset_reps())`` to obtain coset reps as a
        list.

        EXAMPLES::

            sage: list(Gamma0(5).coset_reps())
            [
            [1 0]  [ 0 -1]  [1 0]  [ 0 -1]  [ 0 -1]  [ 0 -1]
            [0 1], [ 1  0], [1 1], [ 1  2], [ 1  3], [ 1  4]
            ]
            sage: list(Gamma0(4).coset_reps())
            [
            [1 0]  [ 0 -1]  [1 0]  [ 0 -1]  [ 0 -1]  [1 0]
            [0 1], [ 1  0], [1 1], [ 1  2], [ 1  3], [2 1]
            ]
            sage: list(Gamma0(1).coset_reps())
            [
            [1 0]
            [0 1]
            ]
        """
    @cached_method
    def generators(self, algorithm: str = 'farey'):
        """
        Return generators for this congruence subgroup.

        INPUT:

        - ``algorithm`` -- string; either ``'farey'`` (default) or
          ``'todd-coxeter'``

        If ``algorithm`` is set to ``'farey'``, then the generators will be
        calculated using Farey symbols, which will always return a *minimal*
        generating set. See :mod:`~sage.modular.arithgroup.farey_symbol` for
        more information.

        If ``algorithm`` is set to ``'todd-coxeter'``, a simpler algorithm
        based on Todd-Coxeter enumeration will be used. This tends to return
        far larger sets of generators.

        EXAMPLES::

            sage: Gamma0(3).generators()
            [
            [1 1]  [-1  1]
            [0 1], [-3  2]
            ]
            sage: Gamma0(3).generators(algorithm='todd-coxeter')
            [
            [1 1]  [-1  0]  [ 1 -1]  [1 0]  [1 1]  [-1  0]  [ 1  0]
            [0 1], [ 0 -1], [ 0  1], [3 1], [0 1], [ 3 -1], [-3  1]
            ]
            sage: SL2Z.gens()
            (
            [ 0 -1]  [1 1]
            [ 1  0], [0 1]
            )
        """
    def gamma_h_subgroups(self):
        """
        Return the subgroups of the form `\\Gamma_H(N)` contained
        in ``self``, where `N` is the level of ``self``.

        EXAMPLES::

            sage: G = Gamma0(11)
            sage: G.gamma_h_subgroups()  # optional - gap_package_polycyclic
            [Congruence Subgroup Gamma0(11),
             Congruence Subgroup Gamma_H(11) with H generated by [3],
             Congruence Subgroup Gamma_H(11) with H generated by [10],
             Congruence Subgroup Gamma1(11)]
            sage: G = Gamma0(12)
            sage: G.gamma_h_subgroups()  # optional - gap_package_polycyclic
            [Congruence Subgroup Gamma0(12),
             Congruence Subgroup Gamma_H(12) with H generated by [7],
             Congruence Subgroup Gamma_H(12) with H generated by [11],
             Congruence Subgroup Gamma_H(12) with H generated by [5],
             Congruence Subgroup Gamma1(12)]
        """
    def ncusps(self):
        """
        Return the number of cusps of this subgroup `\\Gamma_0(N)`.

        EXAMPLES::

            sage: [Gamma0(n).ncusps() for n in [1..19]]
            [1, 2, 2, 3, 2, 4, 2, 4, 4, 4, 2, 6, 2, 4, 4, 6, 2, 8, 2]
            sage: [Gamma0(n).ncusps() for n in prime_range(2,100)]
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        """
    def nu2(self):
        """
        Return the number of elliptic points of order 2 for this congruence
        subgroup `\\Gamma_0(N)`.

        The number of these is given by a standard formula:
        0 if `N` is divisible by 4 or any prime congruent to -1 mod 4, and
        otherwise `2^d` where d is the number of odd primes dividing `N`.

        EXAMPLES::

            sage: Gamma0(2).nu2()
            1
            sage: Gamma0(4).nu2()
            0
            sage: Gamma0(21).nu2()
            0
            sage: Gamma0(1105).nu2()
            8
            sage: [Gamma0(n).nu2() for n in [1..19]]
            [1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0]
        """
    def nu3(self):
        """
        Return the number of elliptic points of order 3 for this congruence
        subgroup `\\Gamma_0(N)`. The number of these is given by a standard formula:
        0 if `N` is divisible by 9 or any prime congruent to -1 mod 3, and
        otherwise `2^d` where d is the number of primes other than 3 dividing `N`.

        EXAMPLES::

            sage: Gamma0(2).nu3()
            0
            sage: Gamma0(3).nu3()
            1
            sage: Gamma0(9).nu3()
            0
            sage: Gamma0(7).nu3()
            2
            sage: Gamma0(21).nu3()
            2
            sage: Gamma0(1729).nu3()
            8
        """
    def index(self):
        """
        Return the index of ``self`` in the full modular group.

        This is given by

        .. MATH::

            N \\prod_{\\substack{p \\mid N \\\\ \\text{$p$ prime}}}\\left(1 + \\frac{1}{p}\\right).

        EXAMPLES::

            sage: [Gamma0(n).index() for n in [1..19]]
            [1, 3, 4, 6, 6, 12, 8, 12, 12, 18, 12, 24, 14, 24, 24, 24, 18, 36, 20]
            sage: Gamma0(32041).index()
            32220
        """
    def dimension_new_cusp_forms(self, k: int = 2, p: int = 0):
        """
        Return the dimension of the space of new (or `p`-new)
        weight `k` cusp forms for this congruence subgroup.

        INPUT:

        - ``k`` -- integer (default: 2); the weight. Not fully
          implemented for `k = 1`.
        - ``p`` -- integer (default: 0); if nonzero, compute the
          `p`-new subspace

        OUTPUT: integer

        ALGORITHM:

        This comes from the formula given in Theorem 1 of
        http://www.math.ubc.ca/~gerg/papers/downloads/DSCFN.pdf

        EXAMPLES::

            sage: Gamma0(11000).dimension_new_cusp_forms()
            240
            sage: Gamma0(11000).dimension_new_cusp_forms(k=1)
            0
            sage: Gamma0(22).dimension_new_cusp_forms(k=4)
            3
            sage: Gamma0(389).dimension_new_cusp_forms(k=2,p=17)
            32

        TESTS::

             sage: L = [1213, 1331, 2169, 2583, 2662, 2745, 3208,
             ....:      3232, 3465, 3608, 4040, 4302, 4338]
             sage: all(Gamma0(N).dimension_new_cusp_forms(2)==100 for N in L)
             True
        """
