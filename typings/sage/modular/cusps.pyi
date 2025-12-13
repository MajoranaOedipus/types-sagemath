from _typeshed import Incomplete
from sage.libs.pari import pari as pari
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import Singleton as Singleton
from sage.modular.modsym.p1list import lift_to_sl2z_llong as lift_to_sl2z_llong
from sage.rings.infinity import Infinity as Infinity, InfinityRing as InfinityRing
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element, InfinityElement as InfinityElement, Matrix as Matrix
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from typing import Any

class Cusp(Element):
    """
    A cusp.

    A cusp is either a rational number or infinity, i.e., an element of
    the projective line over Q. A Cusp is stored as a pair (a,b), where
    gcd(a,b)=1 and a,b are of type Integer.

    EXAMPLES::

        sage: a = Cusp(2/3); b = Cusp(oo)
        sage: a.parent()
        Set P^1(QQ) of all cusps
        sage: a.parent() is b.parent()
        True
    """
    def __init__(self, a, b=None, parent=None, check: bool = True) -> None:
        '''
        Create the cusp a/b in `\\mathbb{P}^1(\\QQ)`, where if b=0
        this is the cusp at infinity.

        When present, b must either be Infinity or coercible to an
        Integer.

        EXAMPLES::

            sage: Cusp(2,3)
            2/3
            sage: Cusp(3,6)
            1/2
            sage: Cusp(1,0)
            Infinity
            sage: Cusp(infinity)
            Infinity
            sage: Cusp(5)
            5
            sage: Cusp(1/2)
            1/2
            sage: Cusp(1.5)
            3/2
            sage: Cusp(int(7))
            7
            sage: Cusp(1, 2, check=False)
            1/2
            sage: Cusp(\'sage\', 2.5, check=False)          # don\'t do this!
            sage/2.50000000000000

        ::

            sage: I**2
            -1
            sage: Cusp(I)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert I to a cusp

        ::

            sage: a = Cusp(2,3)
            sage: loads(a.dumps()) == a
            True

        ::

            sage: Cusp(1/3,0)
            Infinity
            sage: Cusp((1,0))
            Infinity

        TESTS::

            sage: Cusp("1/3", 5)
            1/15
            sage: Cusp(Cusp(3/5), 7)
            3/35
            sage: Cusp(5/3, 0)
            Infinity
            sage: Cusp(3,oo)
            0
            sage: Cusp((7,3), 5)
            7/15
            sage: Cusp(int(5), 7)
            5/7

        ::

            sage: Cusp(0,0)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert (0, 0) to a cusp

        ::

            sage: Cusp(oo,oo)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert (+Infinity, +Infinity) to a cusp

        ::

            sage: Cusp(Cusp(oo),oo)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert (Infinity, +Infinity) to a cusp

        Conversion from PARI is supported (see :issue:`32091`)::

            sage: Cusp(pari.oo())
            Infinity
            sage: Cusp(pari(2/3))
            2/3
        '''
    def __hash__(self):
        """
        EXAMPLES::

            sage: hash(Cusp(1/3)) == hash((1,3))
            True
            sage: hash(Cusp(oo)) == hash((1,0))
            True
        """
    def is_infinity(self) -> bool:
        """
        Return ``True`` if this is the cusp infinity.

        EXAMPLES::

            sage: Cusp(3/5).is_infinity()
            False
            sage: Cusp(1,0).is_infinity()
            True
            sage: Cusp(0,1).is_infinity()
            False
        """
    def numerator(self):
        """
        Return the numerator of the cusp a/b.

        EXAMPLES::

            sage: x = Cusp(6,9); x
            2/3
            sage: x.numerator()
            2
            sage: Cusp(oo).numerator()
            1
            sage: Cusp(-5/10).numerator()
            -1
        """
    def denominator(self):
        """
        Return the denominator of the cusp a/b.

        EXAMPLES::

            sage: x = Cusp(6,9); x
            2/3
            sage: x.denominator()
            3
            sage: Cusp(oo).denominator()
            0
            sage: Cusp(-5/10).denominator()
            2
        """
    def __neg__(self):
        """
        The negative of this cusp.

        EXAMPLES::

            sage: -Cusp(2/7)
            -2/7
            sage: -Cusp(oo)
            Infinity
        """
    def is_gamma0_equiv(self, other, N, transformation=None) -> bool | tuple[bool, Any]:
        """
        Return whether ``self`` and ``other`` are equivalent modulo the action of
        `\\Gamma_0(N)` via linear fractional transformations.

        INPUT:

        - ``other`` -- cusp

        - ``N`` -- integer (specifies the group `\\Gamma_0(N)`)

        - ``transformation`` -- ``None`` (default) or either the string 'matrix' or
          ``'corner'``. If ``'matrix'``, it also returns a matrix in `\\Gamma_0(N)` that
          sends ``self`` to ``other``. The matrix is chosen such that the lower
          left entry is as small as possible in absolute value. If ``'corner'`` (or
          ``True`` for backwards compatibility), it returns only the upper left
          entry of such a matrix.

        OUTPUT:

        - a boolean -- ``True`` if ``self`` and ``other`` are equivalent

        - a matrix or an integer -- returned only if transformation is 'matrix'
          or 'corner', respectively

        EXAMPLES::

            sage: x = Cusp(2,3)
            sage: y = Cusp(4,5)
            sage: x.is_gamma0_equiv(y, 2)
            True
            sage: _, ga = x.is_gamma0_equiv(y, 2, 'matrix'); ga
            [-1  2]
            [-2  3]
            sage: x.is_gamma0_equiv(y, 3)
            False
            sage: x.is_gamma0_equiv(y, 3, 'matrix')
            (False, None)
            sage: Cusp(1/2).is_gamma0_equiv(1/3,11,'corner')
            (True, 19)

            sage: Cusp(1,0)
            Infinity
            sage: z = Cusp(1,0)
            sage: x.is_gamma0_equiv(z, 3, 'matrix')
            (
                  [-1  1]
            True, [-3  2]
            )


        ALGORITHM: See Proposition 2.2.3 of Cremona's book 'Algorithms for
        Modular Elliptic Curves', or Prop 2.27 of Stein's Ph.D. thesis.
        """
    def is_gamma1_equiv(self, other, N) -> tuple[bool, int]:
        """
        Return whether ``self`` and ``other`` are equivalent modulo the action of
        `\\Gamma_1(N)` via linear fractional transformations.

        INPUT:

        - ``other`` -- cusp

        - ``N`` -- integer (specifies the group `\\Gamma_1(N)`)

        OUTPUT:

        - ``bool`` -- ``True`` if ``self`` and ``other`` are equivalent

        - ``int`` -- 0, 1 or -1, gives further information
          about the equivalence: If the two cusps are u1/v1 and u2/v2, then
          they are equivalent if and only if v1 = v2 (mod N) and u1 = u2 (mod
          gcd(v1,N)) or v1 = -v2 (mod N) and u1 = -u2 (mod gcd(v1,N)) The
          sign is +1 for the first and -1 for the second. If the two cusps
          are not equivalent then 0 is returned.

        EXAMPLES::

            sage: x = Cusp(2,3)
            sage: y = Cusp(4,5)
            sage: x.is_gamma1_equiv(y,2)
            (True, 1)
            sage: x.is_gamma1_equiv(y,3)
            (False, 0)
            sage: z = Cusp(QQ(x) + 10)
            sage: x.is_gamma1_equiv(z,10)
            (True, 1)
            sage: z = Cusp(1,0)
            sage: x.is_gamma1_equiv(z, 3)
            (True, -1)
            sage: Cusp(0).is_gamma1_equiv(oo, 1)
            (True, 1)
            sage: Cusp(0).is_gamma1_equiv(oo, 3)
            (False, 0)
        """
    def is_gamma_h_equiv(self, other, G) -> tuple[bool, int]:
        """
        Return a pair ``(b, t)``, where ``b`` is ``True`` or ``False`` as
        ``self`` and ``other`` are equivalent under the action of `G`, and `t`
        is 1 or -1, as described below.

        Two cusps `u1/v1` and `u2/v2` are equivalent modulo
        Gamma_H(N) if and only if `v1 =  h*v2 (\\mathrm{mod} N)` and
        `u1 =  h^{(-1)}*u2 (\\mathrm{mod} gcd(v1,N))` or
        `v1 = -h*v2 (mod N)` and
        `u1 = -h^{(-1)}*u2 (\\mathrm{mod} gcd(v1,N))` for some
        `h \\in H`. Then t is 1 or -1 as c and c' fall into the
        first or second case, respectively.

        INPUT:

        - ``other`` -- cusp

        - ``G`` -- a congruence subgroup Gamma_H(N)

        OUTPUT:

        - ``bool`` -- ``True`` if ``self`` and ``other`` are equivalent

        - ``int`` -- -1, 0, 1; extra info

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = Cusp(2,3)
            sage: y = Cusp(4,5)
            sage: x.is_gamma_h_equiv(y,GammaH(13,[2]))
            (True, 1)
            sage: x.is_gamma_h_equiv(y,GammaH(13,[5]))
            (False, 0)
            sage: x.is_gamma_h_equiv(y,GammaH(5,[]))
            (False, 0)
            sage: x.is_gamma_h_equiv(y,GammaH(23,[4]))
            (True, -1)

        Enumerating the cusps for a space of modular symbols uses this
        function.

        ::

            sage: # needs sage.libs.pari
            sage: G = GammaH(25,[6]); M = G.modular_symbols(); M
            Modular Symbols space of dimension 11 for Congruence Subgroup Gamma_H(25)
             with H generated by [6] of weight 2 with sign 0 over Rational Field
            sage: M.cusps()
            [8/25, 1/3, 6/25, 1/4, 1/15, -7/15, 7/15, 4/15, 1/20, 3/20, 7/20, 9/20]
            sage: len(M.cusps())
            12

        This is always one more than the associated space of weight 2 Eisenstein
        series.

        ::

            sage: # needs sage.libs.pari
            sage: G.dimension_eis(2)
            11
            sage: M.cuspidal_subspace()
            Modular Symbols subspace of dimension 0 of
             Modular Symbols space of dimension 11 for Congruence Subgroup Gamma_H(25)
              with H generated by [6] of weight 2 with sign 0 over Rational Field
            sage: G.dimension_cusp_forms(2)
            0
        """
    def apply(self, g):
        """
        Return g(self), where g=[a,b,c,d] is a list of length 4, which we
        view as a linear fractional transformation.

        EXAMPLES: Apply the identity matrix::

            sage: Cusp(0).apply([1,0,0,1])
            0
            sage: Cusp(0).apply([0,-1,1,0])
            Infinity
            sage: Cusp(0).apply([1,-3,0,1])
            -3
        """
    def galois_action(self, t, N):
        '''
        Suppose this cusp is `\\alpha`, `G` a congruence subgroup of level `N`
        and `\\sigma` is the automorphism in the Galois group of
        `\\QQ(\\zeta_N)/\\QQ` that sends `\\zeta_N` to `\\zeta_N^t`. Then this
        function computes a cusp `\\beta` such that `\\sigma([\\alpha]) = [\\beta]`,
        where `[\\alpha]` is the equivalence class of `\\alpha` modulo `G`.

        This code only needs as input the level and not the group since the
        action of Galois for a congruence group `G` of level `N` is compatible
        with the action of the full congruence group `\\Gamma(N)`.

        INPUT:

        - ``t`` -- integer that is coprime to N

        - ``N`` -- positive integer (level)

        OUTPUT: a cusp

        .. WARNING::

            In some cases `N` must fit in a long long, i.e., there
            are cases where this algorithm isn\'t fully implemented.

        .. NOTE::

            Modular curves can have multiple non-isomorphic models over `\\QQ`.
            The action of Galois depends on such a model. The model over `\\QQ`
            of `X(G)` used here is the model where the function field
            `\\QQ(X(G))` is given by the functions whose Fourier expansion at
            `\\infty` have their coefficients in `\\QQ`. For `X(N):=X(\\Gamma(N))`
            the corresponding moduli interpretation over `\\ZZ[1/N]` is that
            `X(N)` parametrizes pairs `(E,a)` where `E` is a (generalized)
            elliptic curve and `a: \\ZZ / N\\ZZ \\times \\mu_N \\to E` is a closed
            immersion such that the Weil pairing of `a(1,1)` and `a(0,\\zeta_N)`
            is `\\zeta_N`. In this parameterisation the point `z \\in H`
            corresponds to the pair `(E_z,a_z)` with `E_z=\\CC/(z \\ZZ+\\ZZ)` and
            `a_z: \\ZZ / N\\ZZ \\times \\mu_N \\to E` given by `a_z(1,1) = z/N` and
            `a_z(0,\\zeta_N) = 1/N`.
            Similarly `X_1(N):=X(\\Gamma_1(N))` parametrizes pairs `(E,a)` where
            `a: \\mu_N \\to E` is a closed immersion.

        EXAMPLES::

            sage: Cusp(1/10).galois_action(3, 50)
            1/170
            sage: Cusp(oo).galois_action(3, 50)
            Infinity
            sage: c = Cusp(0).galois_action(3, 50); c
            50/17
            sage: Gamma0(50).reduce_cusp(c)
            0

        Here we compute the permutations of the action for t=3 on cusps for
        Gamma0(50). ::

            sage: N = 50; t=3; G = Gamma0(N); C = G.cusps()
            sage: cl = lambda z: exists(C, lambda y:y.is_gamma0_equiv(z, N))[1]
            sage: for i in range(5):
            ....:     print((i, t^i))
            ....:     print([cl(alpha.galois_action(t^i,N)) for alpha in C])
            (0, 1)
            [0, 1/25, 1/10, 1/5, 3/10, 2/5, 1/2, 3/5, 7/10, 4/5, 9/10, Infinity]
            (1, 3)
            [0, 1/25, 7/10, 2/5, 1/10, 4/5, 1/2, 1/5, 9/10, 3/5, 3/10, Infinity]
            (2, 9)
            [0, 1/25, 9/10, 4/5, 7/10, 3/5, 1/2, 2/5, 3/10, 1/5, 1/10, Infinity]
            (3, 27)
            [0, 1/25, 3/10, 3/5, 9/10, 1/5, 1/2, 4/5, 1/10, 2/5, 7/10, Infinity]
            (4, 81)
            [0, 1/25, 1/10, 1/5, 3/10, 2/5, 1/2, 3/5, 7/10, 4/5, 9/10, Infinity]

        TESTS:

        Here we check that the Galois action is indeed a permutation on the
        cusps of Gamma1(48) and check that :issue:`13253` is fixed. ::

            sage: # needs sage.libs.pari
            sage: G = Gamma1(48)
            sage: C = G.cusps()
            sage: for i in Integers(48).unit_gens():
            ....:   C_permuted = [G.reduce_cusp(c.galois_action(i,48)) for c in C]
            ....:   assert len(set(C_permuted))==len(C)

        We test that Gamma1(19) has 9 rational cusps and check that :issue:`8998`
        is fixed. ::

            sage: # needs sage.libs.pari
            sage: G = Gamma1(19)
            sage: [c for c in G.cusps() if c.galois_action(2,19).is_gamma1_equiv(c,19)[0]]
            [2/19, 3/19, 4/19, 5/19, 6/19, 7/19, 8/19, 9/19, Infinity]


        REFERENCES:

        - Section 1.3 of Glenn Stevens, "Arithmetic on Modular Curves"

        - There is a long comment about our algorithm in the source code for this function.

        AUTHORS:

        - William Stein, 2009-04-18
        '''
    def __pari__(self):
        """
        Return a PARI representation of ``self``.

        EXAMPLES::

            sage: Cusp(1, 0).__pari__()                                                 # needs sage.libs.pari
            +oo
            sage: pari(Cusp(3, 2))                                                      # needs sage.libs.pari
            3/2
        """

class Cusps_class(Singleton, Parent):
    """
    The set of cusps.

    EXAMPLES::

        sage: C = Cusps; C
        Set P^1(QQ) of all cusps
        sage: loads(C.dumps()) == C
        True
    """
    def __init__(self) -> None:
        """
        The set of cusps, i.e. `\\mathbb{P}^1(\\QQ)`.

        EXAMPLES::

            sage: C = sage.modular.cusps.Cusps_class() ; C
            Set P^1(QQ) of all cusps
            sage: Cusps == C
            True
        """
    Element = Cusp
    def __call__(self, x):
        """
        Coerce x into the set of cusps.

        EXAMPLES::

            sage: a = Cusps(-4/5); a
            -4/5
            sage: Cusps(a) is a
            False
            sage: Cusps(1.5)
            3/2
            sage: Cusps(oo)
            Infinity
            sage: Cusps(I)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert I to a cusp

        TESTS::

            sage: Cusps.has_coerce_map_from(ZZ)
            True
            sage: Cusps.has_coerce_map_from(QQ)
            True
            sage: Cusps.has_coerce_map_from(GF(7))
            False
        """

Cusps: Incomplete
