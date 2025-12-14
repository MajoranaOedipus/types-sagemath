r"""
Congruence subgroup `\Gamma(N)`
"""
from .congroup_generic import CongruenceSubgroup as CongruenceSubgroup
from .congroup_sl2z import SL2Z as SL2Z
from sage.arith.misc import gcd as gcd
from sage.groups.matrix_gps.finitely_generated import MatrixGroup as MatrixGroup
from sage.matrix.constructor import matrix as matrix
from sage.misc.misc_c import prod as prod
from sage.modular.cusps import Cusp as Cusp
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer import GCD_list as GCD_list
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

def Gamma_constructor(N):
    """
    Return the congruence subgroup `\\Gamma(N)`.

    EXAMPLES::

        sage: Gamma(5) # indirect doctest
        Congruence Subgroup Gamma(5)
        sage: G = Gamma(23)
        sage: G is Gamma(23)
        True
        sage: TestSuite(G).run()

    Test global uniqueness::

        sage: G = Gamma(17)
        sage: G is loads(dumps(G))
        True
        sage: G2 = sage.modular.arithgroup.congroup_gamma.Gamma_class(17)
        sage: G == G2
        True
        sage: G is G2
        False
    """

class Gamma_class(CongruenceSubgroup):
    """
    The principal congruence subgroup `\\Gamma(N)`.
    """
    def __reduce__(self):
        """
        Used for pickling ``self``.

        EXAMPLES::

            sage: Gamma(5).__reduce__()
            (<function Gamma_constructor at ...>, (5,))
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: Gamma(3) == SymmetricGroup(8)                                         # needs sage.groups
            False
            sage: Gamma(3) == Gamma1(3)
            False
            sage: Gamma(5) < Gamma(6)
            True
            sage: Gamma(5) == Gamma(5)
            True
            sage: Gamma(3) == Gamma(3).as_permutation_group()                           # needs sage.groups
            True
        """
    def index(self):
        """
        Return the index of ``self`` in the full modular group. This is given by

        .. MATH::

          \\prod_{\\substack{p \\mid N \\\\ \\text{$p$ prime}}}\\left(p^{3e}-p^{3e-2}\\right).

        EXAMPLES::

            sage: [Gamma(n).index() for n in [1..19]]
            [1, 6, 24, 48, 120, 144, 336, 384, 648, 720, 1320, 1152, 2184, 2016, 2880, 3072, 4896, 3888, 6840]
            sage: Gamma(32041).index()
            32893086819240
        """
    def ncusps(self):
        """
        Return the number of cusps of this subgroup `\\Gamma(N)`.

        EXAMPLES::

            sage: [Gamma(n).ncusps() for n in [1..19]]
            [1, 3, 4, 6, 12, 12, 24, 24, 36, 36, 60, 48, 84, 72, 96, 96, 144, 108, 180]
            sage: Gamma(30030).ncusps()
            278691840
            sage: Gamma(2^30).ncusps()
            432345564227567616
        """
    def nirregcusps(self):
        """
        Return the number of irregular cusps of ``self``. For principal
        congruence subgroups this is always 0.

        EXAMPLES::

            sage: Gamma(17).nirregcusps()
            0
        """
    def reduce_cusp(self, c):
        """
        Calculate the unique reduced representative of the equivalence of the
        cusp `c` modulo this group. The reduced representative of an
        equivalence class is the unique cusp in the class of the form `u/v`
        with `u, v \\ge 0` coprime, `v` minimal, and `u` minimal for that `v`.

        EXAMPLES::

            sage: Gamma(5).reduce_cusp(1/5)
            Infinity
            sage: Gamma(5).reduce_cusp(7/8)
            3/2
            sage: Gamma(6).reduce_cusp(4/3)
            2/3

        TESTS::

            sage: G = Gamma(50)
            sage: all(c == G.reduce_cusp(c) for c in G.cusps())
            True

        We test that :issue:`36163` is fixed::

            sage: Gamma(7).reduce_cusp(Cusp(6,7))
            Infinity
        """
    def are_equivalent(self, x, y, trans: bool = False):
        """
        Check if the cusps `x` and `y` are equivalent under the action of this group.

        ALGORITHM: The cusps `u_1 / v_1` and `u_2 / v_2` are equivalent modulo
        `\\Gamma(N)` if and only if `(u_1, v_1) = \\pm (u_2, v_2) \\bmod N`.

        EXAMPLES::

            sage: Gamma(7).are_equivalent(Cusp(2/3), Cusp(5/4))
            True
        """
    def nu3(self):
        """
        Return the number of elliptic points of order 3 for this arithmetic
        subgroup. Since this subgroup is `\\Gamma(N)` for `N \\ge 2`, there are
        no such points, so we return 0.

        EXAMPLES::

            sage: Gamma(89).nu3()
            0
        """
    def image_mod_n(self):
        """
        Return the image of this group modulo `N`, as a subgroup of `SL(2, \\ZZ
        / N\\ZZ)`. This is just the trivial subgroup.

        EXAMPLES::

            sage: Gamma(3).image_mod_n()
            Matrix group over Ring of integers modulo 3 with 1 generators (
            [1 0]
            [0 1]
            )
        """

def is_Gamma(x):
    """
    Return ``True`` if x is a congruence subgroup of type Gamma.

    EXAMPLES::

        sage: from sage.modular.arithgroup.congroup_gamma import Gamma_class
        sage: isinstance(Gamma0(13), Gamma_class)
        False
        sage: isinstance(Gamma(4), Gamma_class)
        True
    """
