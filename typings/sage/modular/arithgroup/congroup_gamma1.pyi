from .congroup_gammaH import GammaH_class as GammaH_class, GammaH_constructor as GammaH_constructor, is_GammaH as is_GammaH
from sage.arith.misc import divisors as divisors, moebius as moebius
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.rings.integer_ring import ZZ as ZZ

def is_Gamma1(x):
    """
    Return ``True`` if x is a congruence subgroup of type Gamma1.

    EXAMPLES::

        sage: from sage.modular.arithgroup.congroup_gamma1 import is_Gamma1
        sage: is_Gamma1(SL2Z)
        doctest:warning...
        DeprecationWarning: The function is_Gamma1 is deprecated; use 'isinstance(..., Gamma1_class)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        False
        sage: is_Gamma1(Gamma1(13))
        True
        sage: is_Gamma1(Gamma0(6))
        False
        sage: is_Gamma1(GammaH(12, [])) # trick question!
        True
        sage: is_Gamma1(GammaH(12, [5]))
        False
    """
def Gamma1_constructor(N):
    """
    Return the congruence subgroup `\\Gamma_1(N)`.

    EXAMPLES::

        sage: Gamma1(5) # indirect doctest
        Congruence Subgroup Gamma1(5)
        sage: G = Gamma1(23)
        sage: G is Gamma1(23)
        True
        sage: G is GammaH(23, [1])
        True
        sage: TestSuite(G).run()
        sage: G is loads(dumps(G))
        True
    """

class Gamma1_class(GammaH_class):
    """
    The congruence subgroup `\\Gamma_1(N)`.

    TESTS::

        sage: [Gamma1(n).genus() for n in prime_range(2,100)]
        [0, 0, 0, 0, 1, 2, 5, 7, 12, 22, 26, 40, 51, 57, 70, 92, 117, 126, 155, 176, 187, 222, 247, 287, 345]
        sage: [Gamma1(n).index() for n in [1..10]]
        [1, 3, 8, 12, 24, 24, 48, 48, 72, 72]

        sage: [Gamma1(n).dimension_cusp_forms() for n in [1..20]]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 2, 5, 2, 7, 3]
        sage: [Gamma1(n).dimension_cusp_forms(1) for n in [1..20]]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sage: [Gamma1(4).dimension_cusp_forms(k) for k in [1..20]]
        [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

        sage: Gamma1(23).dimension_cusp_forms(1)
        1
    """
    def __init__(self, level) -> None:
        """
        The congruence subgroup `\\Gamma_1(N)`.

        EXAMPLES::

            sage: G = Gamma1(11); G
            Congruence Subgroup Gamma1(11)
            sage: loads(G.dumps()) == G
            True
        """
    def __reduce__(self):
        """
        Used for pickling ``self``.

        EXAMPLES::

            sage: Gamma1(82).__reduce__()
            (<function Gamma1_constructor at ...>, (82,))
        """
    def is_even(self) -> bool:
        """
        Return ``True`` precisely if this subgroup contains the matrix -1.

        EXAMPLES::

            sage: Gamma1(1).is_even()
            True
            sage: Gamma1(2).is_even()
            True
            sage: Gamma1(15).is_even()
            False
        """
    def is_subgroup(self, right) -> bool:
        """
        Return ``True`` if ``self`` is a subgroup of ``right``.

        EXAMPLES::

            sage: Gamma1(3).is_subgroup(SL2Z)
            True
            sage: Gamma1(3).is_subgroup(Gamma1(5))
            False
            sage: Gamma1(3).is_subgroup(Gamma1(6))
            False
            sage: Gamma1(6).is_subgroup(Gamma1(3))
            True
            sage: Gamma1(6).is_subgroup(Gamma0(2))
            True
            sage: Gamma1(80).is_subgroup(GammaH(40, []))
            True
            sage: Gamma1(80).is_subgroup(GammaH(40, [21]))
            True
        """
    @cached_method
    def generators(self, algorithm: str = 'farey'):
        """
        Return generators for this congruence subgroup. The result is cached.

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

            sage: Gamma1(3).generators()
            [
            [1 1]  [ 1 -1]
            [0 1], [ 3 -2]
            ]
            sage: Gamma1(3).generators(algorithm='todd-coxeter')
            [
            [1 1]  [-2  1]  [1 1]  [ 1 -1]  [1 0]  [1 1]  [-5  2]  [ 1  0]
            [0 1], [-3  1], [0 1], [ 0  1], [3 1], [0 1], [12 -5], [-3  1],
            <BLANKLINE>
            [ 1 -1]  [ 1 -1]  [ 4 -1]  [ -5   3]
            [ 3 -2], [ 3 -2], [ 9 -2], [-12   7]
            ]
        """
    def nu2(self):
        """
        Calculate the number of orbits of elliptic points of order 2 for this
        subgroup `\\Gamma_1(N)`. This is known to be 0 if N > 2.

        EXAMPLES::

            sage: Gamma1(2).nu2()
            1
            sage: Gamma1(457).nu2()
            0
            sage: [Gamma1(n).nu2() for n in [1..16]]
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        """
    def nu3(self):
        """
        Calculate the number of orbits of elliptic points of order 3 for this
        subgroup `\\Gamma_1(N)`. This is known to be 0 if N > 3.

        EXAMPLES::

            sage: Gamma1(2).nu3()
            0
            sage: Gamma1(3).nu3()
            1
            sage: Gamma1(457).nu3()
            0
            sage: [Gamma1(n).nu3() for n in [1..10]]
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        """
    def ncusps(self):
        """
        Return the number of cusps of this subgroup `\\Gamma_1(N)`.

        EXAMPLES::

            sage: [Gamma1(n).ncusps() for n in [1..15]]
            [1, 2, 2, 3, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 16]
            sage: [Gamma1(n).ncusps() for n in prime_range(2, 100)]
            [2, 2, 4, 6, 10, 12, 16, 18, 22, 28, 30, 36, 40, 42, 46, 52, 58, 60, 66, 70, 72, 78, 82, 88, 96]
        """
    def index(self):
        """
        Return the index of ``self`` in the full modular group. This is given by the formula

        .. MATH::

            N^2 \\prod_{\\substack{p \\mid N \\\\ \\text{$p$ prime}}} \\left( 1 - \\frac{1}{p^2}\\right).

        EXAMPLES::

            sage: Gamma1(180).index()
            20736
            sage: [Gamma1(n).projective_index() for n in [1..16]]
            [1, 3, 4, 6, 12, 12, 24, 24, 36, 36, 60, 48, 84, 72, 96, 96]
        """
    def dimension_modular_forms(self, k: int = 2, eps=None, algorithm: str = 'CohenOesterle'):
        """
        Return the dimension of the space of modular forms for ``self``, or the
        dimension of the subspace corresponding to the given character if one
        is supplied.

        INPUT:

        - ``k`` -- integer (default: 2); the weight

        - ``eps`` -- either ``None`` or a Dirichlet character modulo N, where N is
          the level of this group. If this is ``None``, then the dimension of the
          whole space is returned; otherwise, the dimension of the subspace of
          forms of character eps.

        - ``algorithm`` -- either ``'CohenOesterle'`` (the default) or
          ``'Quer'``. This specifies the method to use in the case of
          nontrivial character: either the Cohen--Oesterle formula as described
          in Stein's book, or by Möbius inversion using the subgroups GammaH (a
          method due to Jordi Quer).

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(3)
            sage: eps = DirichletGroup(7*43,K).0^2
            sage: G = Gamma1(7*43)
            sage: G.dimension_modular_forms(2, eps)
            32
            sage: G.dimension_modular_forms(2, eps, algorithm='Quer')
            32

        TESTS:

        Check that :issue:`18436` is fixed::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: G = DirichletGroup(13, base_ring=K)
            sage: Gamma1(13).dimension_modular_forms(2, G[1])
            3
            sage: Gamma1(13).dimension_modular_forms(2, G[1], algorithm='Quer')
            3
            sage: Gamma1(39).dimension_modular_forms(2, G[1])
            7
            sage: Gamma1(39).dimension_modular_forms(2, G[1], algorithm='Quer')
            7
        """
    def dimension_cusp_forms(self, k: int = 2, eps=None, algorithm: str = 'CohenOesterle'):
        """
        Return the dimension of the space of cusp forms for ``self``, or the
        dimension of the subspace corresponding to the given character if one
        is supplied.

        INPUT:

        - ``k`` -- integer (default: 2); the weight

        - ``eps`` -- either ``None`` or a Dirichlet character modulo N, where N is
          the level of this group. If this is ``None``, then the dimension of the
          whole space is returned; otherwise, the dimension of the subspace of
          forms of character eps.

        - ``algorithm`` -- either ``'CohenOesterle'`` (the default) or
          ``'Quer'``. This specifies the method to use in the case of nontrivial
          character: either the Cohen--Oesterle formula as described in Stein's
          book, or by Möbius inversion using the subgroups GammaH (a method due
          to Jordi Quer). Ignored for weight 1.

        EXAMPLES:

        We compute the same dimension in two different ways ::

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(3)
            sage: eps = DirichletGroup(7*43,K).0^2
            sage: G = Gamma1(7*43)

        Via Cohen--Oesterle::

            sage: Gamma1(7*43).dimension_cusp_forms(2, eps)                             # needs sage.rings.number_field
            28

        Via Quer's method::

            sage: Gamma1(7*43).dimension_cusp_forms(2, eps, algorithm='Quer')           # needs sage.rings.number_field
            28

        Some more examples::

            sage: G.<eps> = DirichletGroup(9)
            sage: [Gamma1(9).dimension_cusp_forms(k, eps) for k in [1..10]]
            [0, 0, 1, 0, 3, 0, 5, 0, 7, 0]
            sage: [Gamma1(9).dimension_cusp_forms(k, eps^2) for k in [1..10]]
            [0, 0, 0, 2, 0, 4, 0, 6, 0, 8]

        In weight 1, we can sometimes rule out cusp forms existing via
        Riemann-Roch, but if this does not work, we trigger computation of the
        cusp forms space via Schaeffer's algorithm::

            sage: chi = [u for u in DirichletGroup(40) if u(-1) == -1 and u(21) == 1][0]
            sage: Gamma1(40).dimension_cusp_forms(1, chi)
            0
            sage: G = DirichletGroup(57); chi = (G.0) * (G.1)^6
            sage: Gamma1(57).dimension_cusp_forms(1, chi)
            1
        """
    def dimension_eis(self, k: int = 2, eps=None, algorithm: str = 'CohenOesterle'):
        """
        Return the dimension of the space of Eisenstein series forms for self,
        or the dimension of the subspace corresponding to the given character
        if one is supplied.

        INPUT:

        - ``k`` -- integer (default: 2); the weight

        - ``eps`` -- either ``None`` or a Dirichlet character modulo N, where N is
          the level of this group. If this is ``None``, then the dimension of the
          whole space is returned; otherwise, the dimension of the subspace of
          Eisenstein series of character eps.

        - ``algorithm`` -- either ``'CohenOesterle'`` (the default) or
          ``'Quer'``. This specifies the method to use in the case of nontrivial
          character: either the Cohen--Oesterle formula as described in Stein's
          book, or by Möbius inversion using the subgroups GammaH (a method due
          to Jordi Quer).

        AUTHORS:

        - William Stein - Cohen--Oesterle algorithm

        - Jordi Quer - algorithm based on GammaH subgroups

        - David Loeffler (2009) - code refactoring

        EXAMPLES:

        The following two computations use different algorithms::

            sage: [Gamma1(36).dimension_eis(1,eps) for eps in DirichletGroup(36)]
            [0, 4, 3, 0, 0, 2, 6, 0, 0, 2, 3, 0]
            sage: [Gamma1(36).dimension_eis(1,eps,algorithm='Quer') for eps in DirichletGroup(36)]
            [0, 4, 3, 0, 0, 2, 6, 0, 0, 2, 3, 0]

        So do these::

            sage: [Gamma1(48).dimension_eis(3,eps) for eps in DirichletGroup(48)]
            [0, 12, 0, 4, 0, 8, 0, 4, 12, 0, 4, 0, 8, 0, 4, 0]
            sage: [Gamma1(48).dimension_eis(3,eps,algorithm='Quer') for eps in DirichletGroup(48)]
            [0, 12, 0, 4, 0, 8, 0, 4, 12, 0, 4, 0, 8, 0, 4, 0]
        """
    def dimension_new_cusp_forms(self, k: int = 2, eps=None, p: int = 0, algorithm: str = 'CohenOesterle'):
        """
        Dimension of the new subspace (or `p`-new subspace) of cusp forms of
        weight `k` and character `\\varepsilon`.

        INPUT:

        - ``k`` -- integer (default: 2)

        - ``eps`` -- a Dirichlet character

        - ``p`` -- a prime (default: 0); just the `p`-new subspace if given

        - ``algorithm`` -- either ``'CohenOesterle'`` (the default) or
          ``'Quer'``. This specifies the method to use in the case of nontrivial
          character: either the Cohen--Oesterle formula as described in Stein's
          book, or by Möbius inversion using the subgroups GammaH (a method due
          to Jordi Quer).

        EXAMPLES::

            sage: G = DirichletGroup(9)
            sage: eps = G.0^3
            sage: eps.conductor()
            3
            sage: [Gamma1(9).dimension_new_cusp_forms(k, eps) for k in [2..10]]
            [0, 0, 0, 2, 0, 2, 0, 2, 0]
            sage: [Gamma1(9).dimension_cusp_forms(k, eps) for k in [2..10]]
            [0, 0, 0, 2, 0, 4, 0, 6, 0]
            sage: [Gamma1(9).dimension_new_cusp_forms(k, eps, 3) for k in [2..10]]
            [0, 0, 0, 2, 0, 2, 0, 2, 0]

        Double check using modular symbols (independent calculation)::

            sage: [ModularSymbols(eps,k,sign=1).cuspidal_subspace().new_subspace().dimension()  for k in [2..10]]
            [0, 0, 0, 2, 0, 2, 0, 2, 0]
            sage: [ModularSymbols(eps,k,sign=1).cuspidal_subspace().new_subspace(3).dimension()  for k in [2..10]]
            [0, 0, 0, 2, 0, 2, 0, 2, 0]

        Another example at level 33::

            sage: G = DirichletGroup(33)
            sage: eps = G.1
            sage: eps.conductor()
            11
            sage: [Gamma1(33).dimension_new_cusp_forms(k, G.1) for k in [2..4]]
            [0, 4, 0]
            sage: [Gamma1(33).dimension_new_cusp_forms(k, G.1, algorithm='Quer') for k in [2..4]]
            [0, 4, 0]
            sage: [Gamma1(33).dimension_new_cusp_forms(k, G.1^2) for k in [2..4]]
            [2, 0, 6]
            sage: [Gamma1(33).dimension_new_cusp_forms(k, G.1^2, p=3) for k in [2..4]]
            [2, 0, 6]
        """
