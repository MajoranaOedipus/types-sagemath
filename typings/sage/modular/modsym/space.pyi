from sage.arith.misc import divisors as divisors, next_prime as next_prime
from sage.categories.fields import Fields as Fields
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.hecke.module import HeckeModule_free_module as HeckeModule_free_module
from sage.modular.modsym.element import ModularSymbolsElement as ModularSymbolsElement
from sage.modules.free_module import EchelonMatrixKey as EchelonMatrixKey, FreeModule as FreeModule, VectorSpace as VectorSpace
from sage.modules.free_module_element import FreeModuleElement as FreeModuleElement
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.all import SageObject as SageObject, Sequence as Sequence
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

def is_ModularSymbolsSpace(x):
    """
    Return ``True`` if ``x`` is a space of modular symbols.

    EXAMPLES::

        sage: M = ModularForms(3, 2)
        sage: sage.modular.modsym.space.is_ModularSymbolsSpace(M)
        doctest:warning...
        DeprecationWarning: The function is_ModularSymbolsSpace is deprecated; use 'isinstance(..., ModularForms)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        False
        sage: sage.modular.modsym.space.is_ModularSymbolsSpace(M.modular_symbols(sign=1))
        True
    """

class ModularSymbolsSpace(HeckeModule_free_module):
    """
    Base class for spaces of modular symbols.
    """
    Element = ModularSymbolsElement
    def __init__(self, group, weight, character, sign, base_ring, category=None) -> None:
        """
        Create a space of modular symbols.

        EXAMPLES::

            sage: M = ModularSymbols(22,6) ; M
            Modular Symbols space of dimension 30 for Gamma_0(22) of weight 6 with sign 0 over Rational Field
            sage: M == loads(dumps(M))
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        When spaces are in a common ambient space, we order
        lexicographically by the sequence of traces of Hecke operators
        `T_p`, for all primes `p`. In general we order
        first by the group, then the weight, then the character, then the
        sign then the base ring, then the dimension.

        EXAMPLES::

            sage: M = ModularSymbols(21,4) ; N = ModularSymbols(Gamma1(5),6)
            sage: M.cuspidal_submodule() > N
            True
            sage: M.cuspidal_submodule() == N
            False
        """
    def compact_system_of_eigenvalues(self, v, names: str = 'alpha', nz=None):
        """
        Return a compact system of eigenvalues `a_n` for
        `n\\in v`.

        This should only be called on simple factors of modular
        symbols spaces.

        INPUT:

        - ``v`` -- list of positive integers
        - ``nz`` -- (default: ``None``) if given specifies a column index
          such that the dual module has that column nonzero

        OUTPUT:

        - ``E`` -- matrix such that E\\*v is a vector with components
          the eigenvalues `a_n` for `n \\in v`
        - ``v`` -- a vector over a number field

        EXAMPLES::

            sage: M = ModularSymbols(43,2,1)[2]; M
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field
            sage: E, v = M.compact_system_of_eigenvalues(prime_range(10))
            sage: E
            [ 2/3 -4/3]
            [-2/3  4/3]
            [ 4/3  4/3]
            [-4/3 -4/3]
            sage: v
            (1, -3/4*alpha + 1/2)
            sage: E*v
            (alpha, -alpha, -alpha + 2, alpha - 2)

        TESTS:

        Verify that :issue:`12772` is fixed::

            sage: M = ModularSymbols(1,12,sign=1).cuspidal_subspace().new_subspace()
            sage: A = M.decomposition()[0]
            sage: A.compact_system_of_eigenvalues(prime_range(10))
            (
            [   -24]
            [   252]
            [  4830]
            [-16744], (1)
            )
        """
    def character(self):
        """
        Return the character associated to ``self``.

        EXAMPLES::

            sage: ModularSymbols(12,8).character()
            Dirichlet character modulo 12 of conductor 1 mapping 7 |--> 1, 5 |--> 1
            sage: ModularSymbols(DirichletGroup(25).0, 4).character()
            Dirichlet character modulo 25 of conductor 25 mapping 2 |--> zeta20
        """
    def cuspidal_submodule(self) -> None:
        """
        Return the cuspidal submodule of ``self``.

        .. NOTE::

            This should be overridden by all derived classes.

        EXAMPLES::

            sage: sage.modular.modsym.space.ModularSymbolsSpace(Gamma0(11),2,DirichletGroup(11).gens()[0]**10,0,QQ).cuspidal_submodule()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of cuspidal submodule not yet implemented for this class
            sage: ModularSymbols(Gamma0(11),2).cuspidal_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
        """
    def cuspidal_subspace(self):
        """
        Synonym for cuspidal_submodule.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma1(3),12); m.dimension()
            8
            sage: m.cuspidal_subspace().new_subspace().dimension()
            2
        """
    def new_subspace(self, p=None):
        """
        Synonym for new_submodule.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma0(5),12); m.dimension()
            12
            sage: m.new_subspace().dimension()
            6
            sage: m = ModularSymbols(Gamma1(3),12); m.dimension()
            8
            sage: m.new_subspace().dimension()
            2
        """
    def old_subspace(self, p=None):
        """
        Synonym for old_submodule.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma1(3),12); m.dimension()
            8
            sage: m.old_subspace().dimension()
            6
        """
    def eisenstein_subspace(self):
        """
        Synonym for eisenstein_submodule.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma1(3),12); m.dimension()
            8
            sage: m.eisenstein_subspace().dimension()
            2
            sage: m.cuspidal_subspace().dimension()
            6
        """
    def dimension_of_associated_cuspform_space(self):
        """
        Return the dimension of the corresponding space of cusp forms.

        The input space must be cuspidal, otherwise there is no
        corresponding space of cusp forms.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma0(389),2).cuspidal_subspace(); m.dimension()
            64
            sage: m.dimension_of_associated_cuspform_space()
            32
            sage: m = ModularSymbols(Gamma0(389),2,sign=1).cuspidal_subspace(); m.dimension()
            32
            sage: m.dimension_of_associated_cuspform_space()
            32
        """
    def dual_star_involution_matrix(self) -> None:
        """
        Return the matrix of the dual star involution, which is induced by
        complex conjugation on the linear dual of modular symbols.

        .. NOTE::

            This should be overridden in all derived classes.

        EXAMPLES::

            sage: sage.modular.modsym.space.ModularSymbolsSpace(Gamma0(11),2,DirichletGroup(11).gens()[0]**10,0,QQ).dual_star_involution_matrix()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of dual star involution matrix not yet implemented for this class
            sage: ModularSymbols(Gamma0(11),2).dual_star_involution_matrix()
            [ 1  0  0]
            [ 0 -1  0]
            [ 0  1  1]
        """
    def group(self):
        """
        Return the group of this modular symbols space.

        INPUT:

        - ``ModularSymbols self`` -- an arbitrary space of
          modular symbols

        OUTPUT:

        - ``CongruenceSubgroup`` -- the congruence subgroup
          that this is a space of modular symbols for

        ALGORITHM: The group is recorded when this space is created.

        EXAMPLES::

            sage: m = ModularSymbols(20)
            sage: m.group()
            Congruence Subgroup Gamma0(20)
        """
    def is_ambient(self) -> bool:
        """
        Return ``True`` if ``self`` is an ambient space of modular symbols.

        EXAMPLES::

            sage: ModularSymbols(21,4).is_ambient()
            True
            sage: ModularSymbols(21,4).cuspidal_submodule().is_ambient()
            False
        """
    def is_cuspidal(self) -> bool:
        """
        Return ``True`` if ``self`` is a cuspidal space of modular symbols.

        .. NOTE::

            This should be overridden in all derived classes.

        EXAMPLES::

            sage: sage.modular.modsym.space.ModularSymbolsSpace(Gamma0(11),2,DirichletGroup(11).gens()[0]**10,0,QQ).is_cuspidal()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of cuspidal subspace not yet implemented for this class
            sage: ModularSymbols(Gamma0(11),2).is_cuspidal()
            False
        """
    def is_simple(self) -> bool:
        """
        Return whether this modular symbols space is simple as a module
        over the anemic Hecke algebra adjoin \\*.

        EXAMPLES::

            sage: m = ModularSymbols(Gamma0(33),2,sign=1)
            sage: m.is_simple()
            False
            sage: o = m.old_subspace()
            sage: o.decomposition()
            [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 6 for Gamma_0(33) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 6 for Gamma_0(33) of weight 2 with sign 1 over Rational Field]
            sage: C = ModularSymbols(1,14,0,GF(5)).cuspidal_submodule(); C
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5
            sage: C.is_simple()
            True
        """
    def multiplicity(self, S, check_simple: bool = True):
        """
        Return the multiplicity of the simple modular symbols space S in
        ``self``. S must be a simple anemic Hecke module.

        ASSUMPTION: ``self`` is an anemic Hecke module with the same weight and
        group as S, and S is simple.

        EXAMPLES::

            sage: M = ModularSymbols(11,2,sign=1)
            sage: N1, N2 = M.decomposition()
            sage: N1.multiplicity(N2)
            0
            sage: M.multiplicity(N1)
            1
            sage: M.multiplicity(ModularSymbols(14,2))
            0
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        INPUT:

        - ``ModularSymbols self`` -- arbitrary space of modular symbols

        OUTPUT:

        - ``int`` -- the number of generators, which is the same as the
          dimension of ``self``

        ALGORITHM: Call the dimension function.

        EXAMPLES::

            sage: m = ModularSymbols(33)
            sage: m.ngens()
            9
            sage: m.rank()
            9
            sage: ModularSymbols(100, weight=2, sign=1).ngens()
            18
        """
    def default_prec(self):
        """
        Get the default precision for computation of `q`-expansion
        associated to the ambient space of this space of modular symbols
        (and all subspaces). Use ``set_default_prec`` to
        change the default precision.

        EXAMPLES::

            sage: M = ModularSymbols(15)
            sage: M.cuspidal_submodule().q_expansion_basis()
            [q - q^2 - q^3 - q^4 + q^5 + q^6 + O(q^8)]
            sage: M.set_default_prec(20)

        Notice that setting the default precision of the ambient space
        affects the subspaces.

        ::

            sage: M.cuspidal_submodule().q_expansion_basis()
            [q - q^2 - q^3 - q^4 + q^5 + q^6 + 3*q^8 + q^9 - q^10 - 4*q^11 + q^12 - 2*q^13 - q^15 - q^16 + 2*q^17 - q^18 + 4*q^19 + O(q^20)]
            sage: M.cuspidal_submodule().default_prec()
            20
        """
    def set_default_prec(self, prec):
        """
        Set the default precision for computation of `q`-expansion
        associated to the ambient space of this space of modular symbols
        (and all subspaces).

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(13),2)
            sage: M.set_default_prec(5)
            sage: M.cuspidal_submodule().q_expansion_basis()
            [q - 4*q^3 - q^4 + O(q^5), q^2 - 2*q^3 - q^4 + O(q^5)]
        """
    def set_precision(self, prec) -> None:
        """
        Same as self.set_default_prec(prec).

        EXAMPLES::

            sage: M = ModularSymbols(17,2)
            sage: M.cuspidal_submodule().q_expansion_basis()
            [q - q^2 - q^4 - 2*q^5 + 4*q^7 + O(q^8)]
            sage: M.set_precision(10)
            sage: M.cuspidal_submodule().q_expansion_basis()
            [q - q^2 - q^4 - 2*q^5 + 4*q^7 + 3*q^8 - 3*q^9 + O(q^10)]
        """
    def q_expansion_basis(self, prec=None, algorithm: str = 'default'):
        """
        Return a basis of `q`-expansions (as power series) to precision ``prec``
        of the space of modular forms associated to ``self``.

        The `q`-expansions are defined over the same base ring as ``self``,
        and a put in echelon form.

        INPUT:

        - ``self`` -- a space of CUSPIDAL modular symbols

        - ``prec`` -- integer

        - ``algorithm`` -- string; one of

          - ``'default'`` -- (default) decide which algorithm to
            use based on heuristics

          - ``'hecke'`` -- compute basis by computing
            homomorphisms T - K, where T is the Hecke algebra

          - ``'eigen'`` -- compute basis using eigenvectors for
            the Hecke action and Atkin-Lehner-Li theory to patch them together

          - ``'all'`` -- compute using hecke_dual and eigen
            algorithms and verify that the results are the same


        The computed basis is *not* cached, though of course Hecke
        operators used in computing the basis are cached.

        EXAMPLES::

            sage: M = ModularSymbols(1, 12).cuspidal_submodule()
            sage: M.q_expansion_basis(8)
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + O(q^8)]

        ::

            sage: M.q_expansion_basis(8, algorithm='eigen')
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + O(q^8)]

        ::

            sage: M = ModularSymbols(1, 24).cuspidal_submodule()
            sage: M.q_expansion_basis(8, algorithm='eigen')
            [q + 195660*q^3 + 12080128*q^4 + 44656110*q^5 - 982499328*q^6 - 147247240*q^7 + O(q^8),
             q^2 - 48*q^3 + 1080*q^4 - 15040*q^5 + 143820*q^6 - 985824*q^7 + O(q^8)]

        ::

            sage: M = ModularSymbols(11, 2, sign=-1).cuspidal_submodule()
            sage: M.q_expansion_basis(8, algorithm='eigen')
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + 2*q^6 - 2*q^7 + O(q^8)]

        ::

            sage: M = ModularSymbols(Gamma1(13), 2, sign=1).cuspidal_submodule()
            sage: M.q_expansion_basis(8, algorithm='eigen')
            [q - 4*q^3 - q^4 + 3*q^5 + 6*q^6 + O(q^8),
             q^2 - 2*q^3 - q^4 + 2*q^5 + 2*q^6 + O(q^8)]

        ::

            sage: M = ModularSymbols(Gamma1(5), 3, sign=-1).cuspidal_submodule()
            sage: M.q_expansion_basis(8, algorithm='eigen')   # dimension is 0
            []

        ::

            sage: M = ModularSymbols(Gamma1(7), 3, sign=-1).cuspidal_submodule()
            sage: M.q_expansion_basis(8)
            [q - 3*q^2 + 5*q^4 - 7*q^7 + O(q^8)]

        ::

            sage: M = ModularSymbols(43, 2, sign=0).cuspidal_submodule()
            sage: M[0]
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 for Gamma_0(43) of weight 2 with sign 0 over Rational Field
            sage: M[0].q_expansion_basis()
            [q - 2*q^2 - 2*q^3 + 2*q^4 - 4*q^5 + 4*q^6 + O(q^8)]
            sage: M[1]
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 7 for Gamma_0(43) of weight 2 with sign 0 over Rational Field
            sage: M[1].q_expansion_basis()
            [q + 2*q^5 - 2*q^6 - 2*q^7 + O(q^8), q^2 - q^3 - q^5 + q^7 + O(q^8)]
        """
    def q_expansion_module(self, prec=None, R=None):
        """
        Return a basis over R for the space spanned by the coefficient
        vectors of the `q`-expansions corresponding to ``self``.

        If R is not the base ring of ``self``, this returns the
        restriction of scalars down to R (for this, ``self`` must have
        base ring `\\QQ` or a number field).

        INPUT:

        - ``self`` -- must be cuspidal

        - ``prec`` -- integer (default: ``self.default_prec()``)

        - ``R`` -- either `\\ZZ`, `\\QQ`, or the ``base_ring`` of ``self``
           (which is the default)

        OUTPUT: a free module over `R`

        .. TODO::

           extend to more general R (though that is fairly easy for the
           user to get by just doing base_extend or change_ring on the
           output of this function).

        Note that the prec needed to distinguish elements of the
        restricted-down-to-R basis may be bigger than ``self.hecke_bound()``,
        since one must use the Sturm bound for modular forms on `\\Gamma_H(N)`.

        EXAMPLES WITH SIGN 1 and R=QQ:

        Basic example with sign 1::

            sage: M = ModularSymbols(11, sign=1).cuspidal_submodule()
            sage: M.q_expansion_module(5, QQ)
            Vector space of degree 5 and dimension 1 over Rational Field
            Basis matrix:
            [ 0  1 -2 -1  2]

        Same example with sign -1::

            sage: M = ModularSymbols(11, sign=-1).cuspidal_submodule()
            sage: M.q_expansion_module(5, QQ)
            Vector space of degree 5 and dimension 1 over Rational Field
            Basis matrix:
            [ 0  1 -2 -1  2]

        An example involving old forms::

            sage: M = ModularSymbols(22, sign=1).cuspidal_submodule()
            sage: M.q_expansion_module(5, QQ)
            Vector space of degree 5 and dimension 2 over Rational Field
            Basis matrix:
            [ 0  1  0 -1 -2]
            [ 0  0  1  0 -2]

        An example that (somewhat spuriously) is over a number field::

            sage: x = polygen(QQ)
            sage: k = NumberField(x^2+1, 'a')
            sage: M = ModularSymbols(11, base_ring=k, sign=1).cuspidal_submodule()
            sage: M.q_expansion_module(5, QQ)
            Vector space of degree 5 and dimension 1 over Rational Field
            Basis matrix:
            [ 0  1 -2 -1  2]

        An example that involves an eigenform with coefficients in a number
        field::

            sage: M = ModularSymbols(23, sign=1).cuspidal_submodule()
            sage: M.q_eigenform(4, 'gamma')
            q + gamma*q^2 + (-2*gamma - 1)*q^3 + O(q^4)
            sage: M.q_expansion_module(11, QQ)
            Vector space of degree 11 and dimension 2 over Rational Field
            Basis matrix:
            [ 0  1  0 -1 -1  0 -2  2 -1  2  2]
            [ 0  0  1 -2 -1  2  1  2 -2  0 -2]

        An example that is genuinely over a base field besides QQ.

        ::

            sage: eps = DirichletGroup(11).0
            sage: M = ModularSymbols(eps,3,sign=1).cuspidal_submodule(); M
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 and level 11, weight 3, character [zeta10], sign 1, over Cyclotomic Field of order 10 and degree 4
            sage: M.q_eigenform(4, 'beta')
            q + (-zeta10^3 + 2*zeta10^2 - 2*zeta10)*q^2 + (2*zeta10^3 - 3*zeta10^2 + 3*zeta10 - 2)*q^3 + O(q^4)
            sage: M.q_expansion_module(7, QQ)
            Vector space of degree 7 and dimension 4 over Rational Field
            Basis matrix:
            [  0   1   0   0   0 -40  64]
            [  0   0   1   0   0 -24  41]
            [  0   0   0   1   0 -12  21]
            [  0   0   0   0   1  -4   4]

        An example involving an eigenform rational over the base, but the
        base is not QQ.

        ::

            sage: k.<a> = NumberField(x^2-5)
            sage: M = ModularSymbols(23, base_ring=k, sign=1).cuspidal_submodule()
            sage: D = M.decomposition(); D
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(23) of weight 2 with sign 1 over Number Field in a with defining polynomial x^2 - 5,
             Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(23) of weight 2 with sign 1 over Number Field in a with defining polynomial x^2 - 5]
            sage: M.q_expansion_module(8, QQ)
            Vector space of degree 8 and dimension 2 over Rational Field
            Basis matrix:
            [ 0  1  0 -1 -1  0 -2  2]
            [ 0  0  1 -2 -1  2  1  2]

        An example involving an eigenform not rational over the base and
        for which the base is not QQ.

        ::

            sage: eps = DirichletGroup(25).0^2
            sage: M = ModularSymbols(eps,2,sign=1).cuspidal_submodule(); M
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 and level 25, weight 2, character [zeta10], sign 1, over Cyclotomic Field of order 10 and degree 4
            sage: D = M.decomposition(); D
            [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 and level 25, weight 2, character [zeta10], sign 1, over Cyclotomic Field of order 10 and degree 4]
            sage: D[0].q_eigenform(4, 'mu')
            q + mu*q^2 + ((zeta10^3 + zeta10 - 1)*mu + zeta10^2 - 1)*q^3 + O(q^4)
            sage: D[0].q_expansion_module(11, QQ)
            Vector space of degree 11 and dimension 8 over Rational Field
            Basis matrix:
            [  0   1   0   0   0   0   0   0 -20  -3   0]
            [  0   0   1   0   0   0   0   0 -16  -1   0]
            [  0   0   0   1   0   0   0   0 -11  -2   0]
            [  0   0   0   0   1   0   0   0  -8  -1   0]
            [  0   0   0   0   0   1   0   0  -5  -1   0]
            [  0   0   0   0   0   0   1   0  -3  -1   0]
            [  0   0   0   0   0   0   0   1  -2   0   0]
            [  0   0   0   0   0   0   0   0   0   0   1]
            sage: D[0].q_expansion_module(11)
            Vector space of degree 11 and dimension 2 over Cyclotomic Field of order 10 and degree 4
            Basis matrix:
            [                                  0                                   1                                   0                        zeta10^2 - 1                       -zeta10^2 - 1                -zeta10^3 - zeta10^2                   zeta10^2 - zeta10           2*zeta10^3 + 2*zeta10 - 1    zeta10^3 - zeta10^2 - zeta10 + 1        zeta10^3 - zeta10^2 + zeta10   -2*zeta10^3 + 2*zeta10^2 - zeta10]
            [                                  0                                   0                                   1               zeta10^3 + zeta10 - 1                         -zeta10 - 1                -zeta10^3 - zeta10^2 -2*zeta10^3 + zeta10^2 - zeta10 + 1                            zeta10^2                                   0                        zeta10^3 + 1  2*zeta10^3 - zeta10^2 + zeta10 - 1]

        EXAMPLES WITH SIGN 0 and R=QQ:

        .. TODO::  This doesn't work yet as it's not implemented!!

        ::

            sage: M = ModularSymbols(11,2).cuspidal_submodule() #not tested
            sage: M.q_expansion_module() #not tested
            ... boom ...

        EXAMPLES WITH SIGN 1 and R=ZZ (computes saturation)::

            sage: M = ModularSymbols(43,2, sign=1).cuspidal_submodule()
            sage: M.q_expansion_module(8, QQ)
            Vector space of degree 8 and dimension 3 over Rational Field
            Basis matrix:
            [   0    1    0    0    0    2   -2   -2]
            [   0    0    1    0 -1/2    1 -3/2    0]
            [   0    0    0    1 -1/2    2 -3/2   -1]
            sage: M.q_expansion_module(8, ZZ)
            Free module of degree 8 and rank 3 over Integer Ring
            Echelon basis matrix:
            [ 0  1  0  0  0  2 -2 -2]
            [ 0  0  1  1 -1  3 -3 -1]
            [ 0  0  0  2 -1  4 -3 -2]
        """
    def congruence_number(self, other, prec=None):
        """
        Given two cuspidal spaces of modular symbols, compute the
        congruence number, using ``prec`` terms of the `q`-expansions.

        The congruence number is defined as follows. If `V` is the
        submodule of integral cusp forms corresponding to ``self`` (saturated in
        `\\ZZ[[q]]`, by definition) and `W` is the
        submodule corresponding to other, each computed to precision ``prec``,
        the congruence number is the index of `V+W` in its
        saturation in `\\ZZ[[q]]`.

        If ``prec`` is not given it is set equal to the max of the
        ``hecke_bound`` function called on each space.

        EXAMPLES::

            sage: A, B = ModularSymbols(48, 2).cuspidal_submodule().decomposition()
            sage: A.congruence_number(B)
            2
        """
    @cached_method
    def q_eigenform_character(self, names=None):
        """
        Return the Dirichlet character associated to the specific
        choice of `q`-eigenform attached to this simple cuspidal
        modular symbols space.

        INPUT:

        - ``names`` -- string; name of the variable

        OUTPUT:

        - a Dirichlet character taking values in the Hecke eigenvalue
          field, where the indeterminate of that field is determined
          by the given variable name.

        EXAMPLES::

            sage: f = ModularSymbols(Gamma1(13),2,sign=1).cuspidal_subspace().decomposition()[0]
            sage: eps = f.q_eigenform_character('a'); eps
            Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -a - 1
            sage: parent(eps)
            Group of Dirichlet characters modulo 13 with values in Number Field in a with defining polynomial x^2 + 3*x + 3
            sage: eps(3)
            a + 1

        The modular symbols space must be simple.::

            sage: ModularSymbols(Gamma1(17),2,sign=1).cuspidal_submodule().q_eigenform_character('a')
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be simple

        If the character is specified when making the modular symbols
        space, then names need not be given and the returned character
        is just the character of the space.::

            sage: f = ModularSymbols(kronecker_character(19),2,sign=1).cuspidal_subspace().decomposition()[0]
            sage: f
            Modular Symbols subspace of dimension 8 of Modular Symbols space of dimension 10 and level 76, weight 2, character [-1, -1], sign 1, over Rational Field
            sage: f.q_eigenform_character()
            Dirichlet character modulo 76 of conductor 76 mapping 39 |--> -1, 21 |--> -1
            sage: f.q_eigenform_character() is f.character()
            True

        The input space need not be cuspidal::

            sage: M = ModularSymbols(Gamma1(13),2,sign=1).eisenstein_submodule()[0]
            sage: M.q_eigenform_character('a')
            Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -1

        The modular symbols space does not have to come from a decomposition::

            sage: ModularSymbols(Gamma1(16),2,sign=1).cuspidal_submodule().q_eigenform_character('a')
            Dirichlet character modulo 16 of conductor 16 mapping 15 |--> 1, 5 |--> -a - 1
        """
    def q_eigenform(self, prec, names=None):
        """
        Return the `q`-expansion to precision ``prec`` of a new eigenform
        associated to ``self``.

        Here ``self`` must be new, cuspidal, and simple.

        EXAMPLES::

            sage: ModularSymbols(2, 8)[1].q_eigenform(5, 'a')
            q - 8*q^2 + 12*q^3 + 64*q^4 + O(q^5)
            sage: ModularSymbols(2, 8)[0].q_eigenform(5,'a')
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be cuspidal.
        """
    def q_expansion_cuspforms(self, prec=None):
        """
        Return a function f(i,j) such that each value f(i,j) is the
        `q`-expansion, to the given precision, of an element of the
        corresponding space `S` of cusp forms.

        Together these functions span `S`. Here `i,j` are integers
        with `0\\leq i,j < d`, where `d` is the dimension of ``self``.

        For a reduced echelon basis, use the function
        ``q_expansion_basis`` instead.

        More precisely, this function returns the `q`-expansions
        obtained by taking the `ij` entry of the matrices of the
        Hecke operators `T_n` acting on the subspace of the linear
        dual of modular symbols corresponding to ``self``.

        EXAMPLES::

            sage: S = ModularSymbols(11,2, sign=1).cuspidal_submodule()
            sage: f = S.q_expansion_cuspforms(8)
            sage: f(0,0)
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + 2*q^6 - 2*q^7 + O(q^8)

        ::

            sage: S = ModularSymbols(37,2).cuspidal_submodule()
            sage: f = S.q_expansion_cuspforms(8)
            sage: f(0,0)
            q + q^3 - 2*q^4 - q^7 + O(q^8)
            sage: f(3,3)
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + 6*q^6 - q^7 + O(q^8)
            sage: f(1,2)
            q^2 + 2*q^3 - 2*q^4 + q^5 - 3*q^6 + O(q^8)

        ::

            sage: S = ModularSymbols(Gamma1(13),2,sign=-1).cuspidal_submodule()
            sage: f = S.q_expansion_cuspforms(8)
            sage: f(0,0)
            q - 2*q^2 + q^4 - q^5 + 2*q^6 + O(q^8)
            sage: f(0,1)
            -q^2 + 2*q^3 + q^4 - 2*q^5 - 2*q^6 + O(q^8)

        ::

            sage: S = ModularSymbols(1,12,sign=-1).cuspidal_submodule()
            sage: f = S.q_expansion_cuspforms(8)
            sage: f(0,0)
            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + O(q^8)
        """
    def hecke_module_of_level(self, level):
        """
        Alias for ``self.modular_symbols_of_level(level)``.

        EXAMPLES::

            sage: ModularSymbols(11, 2).hecke_module_of_level(22)
            Modular Symbols space of dimension 7 for Gamma_0(22) of weight 2 with sign 0 over Rational Field
        """
    def sign(self):
        """
        Return the sign of ``self``.

        For efficiency reasons, it is often useful to compute in the
        (largest) quotient of modular symbols where the \\* involution acts
        as +1, or where it acts as -1.

        INPUT:

        - ``ModularSymbols self`` -- arbitrary space of modular symbols

        OUTPUT:

        - ``-1`` -- if this is factor of quotient where \\* acts as -1,

        - ``+1`` -- if this is factor of quotient where \\* acts as +1,

        - ``0`` -- if this is full space of modular symbols (no quotient)

        EXAMPLES::

            sage: m = ModularSymbols(33)
            sage: m.rank()
            9
            sage: m.sign()
            0
            sage: m = ModularSymbols(33, sign=0)
            sage: m.sign()
            0
            sage: m.rank()
            9
            sage: m = ModularSymbols(33, sign=-1)
            sage: m.sign()
            -1
            sage: m.rank()
            3
        """
    def simple_factors(self):
        """
        Return a list modular symbols spaces `S` where `S`
        is simple spaces of modular symbols (for the anemic Hecke algebra)
        and ``self`` is isomorphic to the direct sum of the `S` with
        some multiplicities, as a module over the *anemic* Hecke algebra.

        For the multiplicities use factorization() instead.

        ASSUMPTION: self is a module over the anemic Hecke algebra.

        EXAMPLES::

            sage: ModularSymbols(1,100,sign=-1).simple_factors()
            [Modular Symbols subspace of dimension 8 of Modular Symbols space of dimension 8 for Gamma_0(1) of weight 100 with sign -1 over Rational Field]
            sage: ModularSymbols(1,16,0,GF(5)).simple_factors()
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) of weight 16 with sign 0 over Finite Field of size 5,
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) of weight 16 with sign 0 over Finite Field of size 5,
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) of weight 16 with sign 0 over Finite Field of size 5]
        """
    def star_eigenvalues(self):
        """
        Return the eigenvalues of the star involution acting on ``self``.

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: D = M.decomposition()
            sage: M.star_eigenvalues()
            [1, -1]
            sage: D[0].star_eigenvalues()
            [1]
            sage: D[1].star_eigenvalues()
            [1, -1]
            sage: D[1].plus_submodule().star_eigenvalues()
            [1]
            sage: D[1].minus_submodule().star_eigenvalues()
            [-1]
        """
    def star_decomposition(self):
        """
        Decompose ``self`` into subspaces which are eigenspaces for the star
        involution.

        EXAMPLES::

            sage: ModularSymbols(Gamma1(19), 2).cuspidal_submodule().star_decomposition()
            [Modular Symbols subspace of dimension 7 of Modular Symbols space of dimension 31 for Gamma_1(19) of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 7 of Modular Symbols space of dimension 31 for Gamma_1(19) of weight 2 with sign 0 over Rational Field]
        """
    def integral_structure(self):
        """
        Return the `\\ZZ`-structure of this modular symbols
        spaces generated by all integral modular symbols.

        EXAMPLES::

            sage: M = ModularSymbols(11,4)
            sage: M.integral_structure()
            Free module of degree 6 and rank 6 over Integer Ring
            Echelon basis matrix:
            [    1     0     0     0     0     0]
            [    0  1/14   1/7  5/14   1/2 13/14]
            [    0     0   1/2     0     0   1/2]
            [    0     0     0     1     0     0]
            [    0     0     0     0     1     0]
            [    0     0     0     0     0     1]
            sage: M.cuspidal_submodule().integral_structure()
            Free module of degree 6 and rank 4 over Integer Ring
            Echelon basis matrix:
            [     0   1/14    1/7   5/14    1/2 -15/14]
            [     0      0    1/2      0      0   -1/2]
            [     0      0      0      1      0     -1]
            [     0      0      0      0      1     -1]
        """
    def intersection_number(self, M):
        """
        Given modular symbols spaces ``self`` and ``M`` in some common ambient
        space, returns the intersection number of these two spaces.

        This is the index in their saturation of the sum of their
        underlying integral structures.

        If ``self`` and ``M`` are of weight two and defined over QQ,
        and correspond to newforms f and g, then this number equals
        the order of the intersection of the modular abelian varieties
        attached to f and g.

        EXAMPLES::

            sage: m = ModularSymbols(389,2)
            sage: d = m.decomposition(2)
            sage: eis = d[0]
            sage: ell = d[1]
            sage: af = d[-1]
            sage: af.intersection_number(eis)
            97
            sage: af.intersection_number(ell)
            400
        """
    def integral_basis(self):
        """
        Return a basis for the `\\ZZ`-submodule of this
        modular symbols space spanned by the generators.

        Modular symbols spaces for congruence subgroups have a
        `\\ZZ`-structure. Computing this
        `\\ZZ`-structure is expensive, so by default modular
        symbols spaces for congruence subgroups in Sage are defined over
        `\\QQ`. This function returns a tuple of independent
        elements in this modular symbols space whose
        `\\ZZ`-span is the corresponding space of modular
        symbols over `\\ZZ`.

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: M.basis()
            ((1,0), (1,8), (1,9))
            sage: M.integral_basis()
            ((1,0), (1,8), (1,9))
            sage: S = M.cuspidal_submodule()
            sage: S.basis()
            ((1,8), (1,9))
            sage: S.integral_basis()
            ((1,8), (1,9))

        ::

            sage: M = ModularSymbols(13,4)
            sage: M.basis()
            ([X^2,(0,1)], [X^2,(1,4)], [X^2,(1,5)], [X^2,(1,7)], [X^2,(1,9)], [X^2,(1,10)], [X^2,(1,11)], [X^2,(1,12)])
            sage: M.integral_basis()
            ([X^2,(0,1)], 1/28*[X^2,(1,4)] + 2/7*[X^2,(1,5)] + 3/28*[X^2,(1,7)] + 11/14*[X^2,(1,9)] + 2/7*[X^2,(1,10)] + 11/28*[X^2,(1,11)] + 3/28*[X^2,(1,12)], [X^2,(1,5)], 1/2*[X^2,(1,7)] + 1/2*[X^2,(1,9)], [X^2,(1,9)], [X^2,(1,10)], [X^2,(1,11)], [X^2,(1,12)])
            sage: S = M.cuspidal_submodule()
            sage: S.basis()
            ([X^2,(1,4)] - [X^2,(1,12)], [X^2,(1,5)] - [X^2,(1,12)], [X^2,(1,7)] - [X^2,(1,12)], [X^2,(1,9)] - [X^2,(1,12)], [X^2,(1,10)] - [X^2,(1,12)], [X^2,(1,11)] - [X^2,(1,12)])
            sage: S.integral_basis()
            (1/28*[X^2,(1,4)] + 2/7*[X^2,(1,5)] + 3/28*[X^2,(1,7)] + 11/14*[X^2,(1,9)] + 2/7*[X^2,(1,10)] + 11/28*[X^2,(1,11)] - 53/28*[X^2,(1,12)], [X^2,(1,5)] - [X^2,(1,12)], 1/2*[X^2,(1,7)] + 1/2*[X^2,(1,9)] - [X^2,(1,12)], [X^2,(1,9)] - [X^2,(1,12)], [X^2,(1,10)] - [X^2,(1,12)], [X^2,(1,11)] - [X^2,(1,12)])

        This function currently raises a NotImplementedError on modular
        symbols spaces with character of order bigger than `2`:

        EXAMPLES::

            sage: M = ModularSymbols(DirichletGroup(13).0^2, 2); M
            Modular Symbols space of dimension 4 and level 13, weight 2, character [zeta6], sign 0, over Cyclotomic Field of order 6 and degree 2
            sage: M.basis()
            ((1,0), (1,5), (1,10), (1,11))
            sage: M.integral_basis()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def integral_hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on the integral
        structure on ``self`` (as returned by ``self.integral_structure()``).

        This is often (but not always) different from the matrix
        returned by ``self.hecke_matrix``, even if the latter has
        integral entries.

        EXAMPLES::

            sage: M = ModularSymbols(6,4)
            sage: M.hecke_matrix(3)
            [27  0  0  0  6 -6]
            [ 0  1 -4  4  8 10]
            [18  0  1  0  6 -6]
            [18  0  4 -3  6 -6]
            [ 0  0  0  0  9 18]
            [ 0  0  0  0 12 15]
            sage: M.integral_hecke_matrix(3)
            [ 27   0   0   0   6  -6]
            [  0   1  -8   8  12  14]
            [ 18   0   5  -4  14   8]
            [ 18   0   8  -7   2 -10]
            [  0   0   0   0   9  18]
            [  0   0   0   0  12  15]
        """
    def sturm_bound(self):
        """
        Return the Sturm bound for this space of modular symbols.

        Type ``sturm_bound?`` for more details.

        EXAMPLES::

            sage: ModularSymbols(11,2).sturm_bound()
            2
            sage: ModularSymbols(389,2).sturm_bound()
            65
            sage: ModularSymbols(1,12).sturm_bound()
            1
            sage: ModularSymbols(1,36).sturm_bound()
            3
            sage: ModularSymbols(DirichletGroup(31).0^2).sturm_bound()
            6
            sage: ModularSymbols(Gamma1(31)).sturm_bound()
            160
        """
    def plus_submodule(self, compute_dual: bool = True):
        """
        Return the subspace of ``self`` on which the star involution acts as +1.

        INPUT:

        - ``compute_dual`` -- boolean (default: ``True``); also
          compute dual subspace. This is useful for many algorithms.

        OUTPUT: subspace of modular symbols

        EXAMPLES::

            sage: ModularSymbols(17,2)
            Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field
            sage: ModularSymbols(17,2).plus_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field
        """
    def minus_submodule(self, compute_dual: bool = True):
        """
        Return the subspace of ``self`` on which the star involution acts as -1.

        INPUT:

        - ``compute_dual`` -- boolean (default: ``True``); also
          compute dual subspace. This is useful for many algorithms.

        OUTPUT: subspace of modular symbols

        EXAMPLES::

            sage: ModularSymbols(14,4)
            Modular Symbols space of dimension 12 for Gamma_0(14) of weight 4 with sign 0 over Rational Field
            sage: ModularSymbols(14,4).minus_submodule()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 12 for Gamma_0(14) of weight 4 with sign 0 over Rational Field
        """
    def sign_submodule(self, sign, compute_dual: bool = True):
        """
        Return the subspace of ``self`` that is fixed under the star involution.

        INPUT:

        - ``sign`` -- integer (either -1, 0 or +1)

        - ``compute_dual`` -- boolean (default: ``True``); also
          compute dual subspace. This is useful for many algorithms.

        OUTPUT: subspace of modular symbols

        EXAMPLES::

            sage: M = ModularSymbols(29,2)
            sage: M.sign_submodule(1)
            Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(29) of weight 2 with sign 0 over Rational Field
            sage: M.sign_submodule(-1)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(29) of weight 2 with sign 0 over Rational Field
            sage: M.sign_submodule(-1).sign()
            -1
        """
    def star_involution(self) -> None:
        """
        Return the star involution on ``self``, which is induced by complex
        conjugation on modular symbols.

        Not implemented in this abstract base class.

        EXAMPLES::

            sage: M = ModularSymbols(11, 2); sage.modular.modsym.space.ModularSymbolsSpace.star_involution(M)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def abelian_variety(self):
        """
        Return the corresponding abelian variety.

        INPUT:

        - ``self`` -- modular symbols space of weight 2 for a
          congruence subgroup such as Gamma0, Gamma1 or GammaH

        EXAMPLES::

            sage: ModularSymbols(Gamma0(11)).cuspidal_submodule().abelian_variety()
            Abelian variety J0(11) of dimension 1
            sage: ModularSymbols(Gamma1(11)).cuspidal_submodule().abelian_variety()
            Abelian variety J1(11) of dimension 1
            sage: ModularSymbols(GammaH(11,[3])).cuspidal_submodule().abelian_variety()
            Abelian variety JH(11,[3]) of dimension 1

        The abelian variety command only works on cuspidal modular symbols
        spaces::

            sage: M = ModularSymbols(37)
            sage: M[0].abelian_variety()
            Traceback (most recent call last):
            ...
            ValueError: self must be cuspidal
            sage: M[1].abelian_variety()
            Abelian subvariety of dimension 1 of J0(37)
            sage: M[2].abelian_variety()
            Abelian subvariety of dimension 1 of J0(37)
        """
    def rational_period_mapping(self):
        """
        Return the rational period mapping associated to ``self``.

        This is a homomorphism to a vector space whose kernel is the
        same as the kernel of the period mapping associated to
        ``self``. For this to exist, ``self`` must be Hecke equivariant.

        Use :meth:`integral_period_mapping` to obtain a homomorphism to a
        `\\ZZ`-module, normalized so the image of integral modular symbols is
        exactly `\\ZZ^n`.

        EXAMPLES::

            sage: M = ModularSymbols(37)
            sage: A = M[1]; A
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
            sage: r = A.rational_period_mapping(); r
            Rational period mapping associated to Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
            sage: r(M.0)
            (0, 0)
            sage: r(M.1)
            (1, 0)
            sage: r.matrix()
            [ 0  0]
            [ 1  0]
            [ 0  1]
            [-1 -1]
            [ 0  0]
            sage: r.domain()
            Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
            sage: r.codomain()
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
        """
    def integral_period_mapping(self):
        """
        Return the integral period mapping associated to ``self``.

        This is a homomorphism to a vector space whose kernel is the same
        as the kernel of the period mapping associated to ``self``, normalized
        so the image of integral modular symbols is exactly `\\ZZ^n`.

        EXAMPLES::

            sage: m = ModularSymbols(23).cuspidal_submodule()
            sage: i = m.integral_period_mapping()
            sage: i
            Integral period mapping associated to Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 2 with sign 0 over Rational Field
            sage: i.matrix()
            [-1/11  1/11     0  3/11]
            [    1     0     0     0]
            [    0     1     0     0]
            [    0     0     1     0]
            [    0     0     0     1]
            sage: [i(b) for b in m.integral_structure().basis()]
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
            sage: [i(b) for b in m.ambient_module().basis()]
            [(-1/11, 1/11, 0, 3/11),
             (1, 0, 0, 0),
             (0, 1, 0, 0),
             (0, 0, 1, 0),
             (0, 0, 0, 1)]

        We compute the image of the winding element::

            sage: m = ModularSymbols(37,sign=1)
            sage: a = m[1]
            sage: f = a.integral_period_mapping()
            sage: e = m([0,oo])
            sage: f(e)
            (-2/3)

        The input space must be cuspidal::

            sage: m = ModularSymbols(37,2,sign=1)
            sage: m.integral_period_mapping()
            Traceback (most recent call last):
            ...
            ValueError: integral mapping only defined for cuspidal spaces
        """
    @cached_method
    def modular_symbols_of_sign(self, sign, bound=None):
        """
        Return a space of modular symbols with the same defining
        properties (weight, level, etc.) and Hecke eigenvalues as this
        space except with given sign.

        INPUT:

        - ``self`` -- a cuspidal space of modular symbols

        - ``sign`` -- integer, one of -1, 0, or 1

        - ``bound`` -- integer (default: ``None``); if specified
          only use Hecke operators up to the given bound

        EXAMPLES::

            sage: S = ModularSymbols(Gamma0(11),2,sign=0).cuspidal_subspace()
            sage: S
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: S.modular_symbols_of_sign(-1)
            Modular Symbols space of dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field

        ::

            sage: S = ModularSymbols(43,2,sign=1)[2]; S
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field
            sage: S.modular_symbols_of_sign(-1)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(43) of weight 2 with sign -1 over Rational Field

        ::

            sage: S.modular_symbols_of_sign(0)
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 7 for Gamma_0(43) of weight 2 with sign 0 over Rational Field

        ::

            sage: S = ModularSymbols(389,sign=1)[3]; S
            Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 33 for Gamma_0(389) of weight 2 with sign 1 over Rational Field
            sage: S.modular_symbols_of_sign(-1)
            Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 32 for Gamma_0(389) of weight 2 with sign -1 over Rational Field
            sage: S.modular_symbols_of_sign(0)
            Modular Symbols subspace of dimension 6 of Modular Symbols space of dimension 65 for Gamma_0(389) of weight 2 with sign 0 over Rational Field

        ::

            sage: S = ModularSymbols(23,sign=1,weight=4)[2]; S
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 7 for Gamma_0(23) of weight 4 with sign 1 over Rational Field
            sage: S.modular_symbols_of_sign(1) is S
            True
            sage: S.modular_symbols_of_sign(0)
            Modular Symbols subspace of dimension 8 of Modular Symbols space of dimension 12 for Gamma_0(23) of weight 4 with sign 0 over Rational Field
            sage: S.modular_symbols_of_sign(-1)
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 5 for Gamma_0(23) of weight 4 with sign -1 over Rational Field
        """
    @cached_method
    def abvarquo_cuspidal_subgroup(self):
        """
        Compute the rational subgroup of the cuspidal subgroup (as an
        abstract abelian group) of the abelian variety quotient A of
        the relevant modular Jacobian attached to this modular symbols
        space.

        We assume that ``self`` is defined over QQ and has weight 2.  If
        the sign of ``self`` is not 0, then the power of 2 may be wrong.

        EXAMPLES::

            sage: D = ModularSymbols(66,2,sign=0).cuspidal_subspace().new_subspace().decomposition()
            sage: D[0].abvarquo_cuspidal_subgroup()
            Finitely generated module V/W over Integer Ring with invariants (3)
            sage: [A.abvarquo_cuspidal_subgroup().invariants() for A in D]
            [(3,), (2,), ()]
            sage: D = ModularSymbols(66,2,sign=1).cuspidal_subspace().new_subspace().decomposition()
            sage: [A.abvarquo_cuspidal_subgroup().invariants() for A in D]
            [(3,), (2,), ()]
            sage: D = ModularSymbols(66,2,sign=-1).cuspidal_subspace().new_subspace().decomposition()
            sage: [A.abvarquo_cuspidal_subgroup().invariants() for A in D]
            [(), (), ()]
        """
    @cached_method
    def abvarquo_rational_cuspidal_subgroup(self):
        """
        Compute the rational subgroup of the cuspidal subgroup (as an
        abstract abelian group) of the abelian variety quotient A of
        the relevant modular Jacobian attached to this modular symbols
        space.

        If C is the subgroup of A generated by differences of
        cusps, then C is equipped with an action of Gal(Qbar/Q), and
        this function computes the fixed subgroup, i.e., C(Q).

        We assume that ``self`` is defined over QQ and has weight 2.  If
        the sign of ``self`` is not 0, then the power of 2 may be wrong.

        EXAMPLES:

        First we consider the fairly straightforward level 37 case,
        where the torsion subgroup of the optimal quotients (which are
        all elliptic curves) are all cuspidal::

            sage: M = ModularSymbols(37).cuspidal_subspace().new_subspace()
            sage: D = M.decomposition()
            sage: [(A.abvarquo_rational_cuspidal_subgroup().invariants(), A.T(19)[0,0]) for A in D]
            [((), 0), ((3,), 2)]
            sage: [(E.torsion_subgroup().invariants(),E.ap(19)) for E in cremona_optimal_curves([37])]
            [((), 0), ((3,), 2)]

        Next we consider level 54, where the rational cuspidal
        subgroups of the quotients are also cuspidal::

            sage: M = ModularSymbols(54).cuspidal_subspace().new_subspace()
            sage: D = M.decomposition()
            sage: [A.abvarquo_rational_cuspidal_subgroup().invariants() for A in D]
            [(3,), (3,)]
            sage: [E.torsion_subgroup().invariants() for E in cremona_optimal_curves([54])]
            [(3,), (3,)]

        Level 66 is interesting, since not all torsion of the quotient
        is rational. In fact, for each elliptic curve quotient, the
        `\\QQ`-rational subgroup of the image of the cuspidal subgroup
        in the quotient is a nontrivial subgroup of `E(\\QQ)_{tor}`.
        Thus not all torsion in the quotient is cuspidal!::

            sage: M = ModularSymbols(66).cuspidal_subspace().new_subspace()
            sage: D = M.decomposition()
            sage: [(A.abvarquo_rational_cuspidal_subgroup().invariants(), A.T(19)[0,0]) for A in D]
            [((3,), -4), ((2,), 4), ((), 0)]
            sage: [(E.torsion_subgroup().invariants(),E.ap(19)) for E in cremona_optimal_curves([66])]
            [((6,), -4), ((4,), 4), ((10,), 0)]
            sage: [A.abelian_variety().rational_cuspidal_subgroup().invariants() for A in D]
            [[6], [4], [10]]

        In this example, the abelian varieties involved all having
        dimension bigger than 1 (unlike above).  We find that all torsion
        in the quotient in each of these cases is cuspidal::

            sage: M = ModularSymbols(125).cuspidal_subspace().new_subspace()
            sage: D = M.decomposition()
            sage: [A.abvarquo_rational_cuspidal_subgroup().invariants() for A in D]
            [(), (5,), (5,)]
            sage: [A.abelian_variety().rational_torsion_subgroup().multiple_of_order() for A in D]
            [1, 5, 5]
        """

class PeriodMapping(SageObject):
    """
    Base class for representing a period mapping attached to a space of modular
    symbols.

    To be used via the derived classes :class:`RationalPeriodMapping` and
    :class:`IntegralPeriodMapping`.
    """
    def __init__(self, modsym, A) -> None:
        """
        Standard initialisation function.

        INPUT:

        - ``modsym`` -- a space of modular symbols

        - ``A`` -- matrix of the associated period map

        EXAMPLES::

            sage: ModularSymbols(2, 8).cuspidal_submodule().integral_period_mapping() # indirect doctest
            Integral period mapping associated to Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(2) of weight 8 with sign 0 over Rational Field
        """
    def modular_symbols_space(self):
        """
        Return the space of modular symbols to which this period mapping
        corresponds.

        EXAMPLES::

            sage: ModularSymbols(17, 2).rational_period_mapping().modular_symbols_space()
            Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field
        """
    def __call__(self, x):
        """
        Evaluate this mapping at an element of the domain.

        EXAMPLES::

            sage: M = ModularSymbols(17, 2).cuspidal_submodule().integral_period_mapping()
            sage: M(vector([1,0,2]))
            (0, 9/4)
        """
    def matrix(self):
        """
        Return the matrix of this period mapping.

        EXAMPLES::

            sage: ModularSymbols(11, 2).cuspidal_submodule().integral_period_mapping().matrix()
            [  0 1/5]
            [  1   0]
            [  0   1]
        """
    def domain(self):
        """
        Return the domain of this mapping (which is the ambient space of the
        corresponding modular symbols space).

        EXAMPLES::

            sage: ModularSymbols(17, 2).cuspidal_submodule().integral_period_mapping().domain()
            Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field
        """
    def codomain(self):
        """
        Return the codomain of this mapping.

        EXAMPLES:

        Note that this presently returns the wrong answer, as a consequence of
        various bugs in the free module routines::

            sage: ModularSymbols(11, 2).cuspidal_submodule().integral_period_mapping().codomain()
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
        """

class RationalPeriodMapping(PeriodMapping): ...
class IntegralPeriodMapping(PeriodMapping): ...
