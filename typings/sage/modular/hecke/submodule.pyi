from . import module as module
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.verbose import verbose as verbose
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.structure.richcmp import richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

def is_HeckeSubmodule(x):
    """
    Return ``True`` if x is of type HeckeSubmodule.

    EXAMPLES::

        sage: sage.modular.hecke.submodule.is_HeckeSubmodule(ModularForms(1, 12))
        doctest:warning...
        DeprecationWarning: the function is_HeckeSubmodule is deprecated;
        use 'isinstance(..., HeckeSubmodule)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        False
        sage: sage.modular.hecke.submodule.is_HeckeSubmodule(CuspForms(1, 12))
        True
    """

class HeckeSubmodule(module.HeckeModule_free_module):
    """
    Submodule of a Hecke module.
    """
    def __init__(self, ambient, submodule, dual_free_module=None, check: bool = True) -> None:
        """
        Initialise a submodule of an ambient Hecke module.

        INPUT:

        - ``ambient`` -- an ambient Hecke module

        - ``submodule`` -- a free module over the base ring which is a submodule
          of the free module attached to the ambient Hecke module. This should
          be invariant under all Hecke operators.

        - ``dual_free_module`` -- the submodule of the dual of the ambient
          module corresponding to this submodule (or ``None``)

        - ``check`` -- whether or not to explicitly check that the submodule is
          Hecke equivariant

        EXAMPLES::

            sage: CuspForms(1,60) # indirect doctest
            Cuspidal subspace of dimension 5 of Modular Forms space of dimension 6 for Modular Group SL(2,Z) of weight 60 over Rational Field

            sage: M = ModularForms(4,10)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.submodule(M.basis()[:3]).free_module())
            sage: S
            Rank 3 submodule of a Hecke module of level 4

            sage: S == loads(dumps(S))
            True
        """
    def __add__(self, other):
        """
        Sum of ``self`` and ``other`` (as submodules of a common ambient
        module).

        EXAMPLES::

            sage: M = ModularForms(4,10)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.submodule(M.basis()[:3]).free_module())
            sage: E = sage.modular.hecke.submodule.HeckeSubmodule(M, M.submodule(M.basis()[3:]).free_module())
            sage: S + E # indirect doctest
            Modular Forms subspace of dimension 6 of Modular Forms space of dimension 6 for Congruence Subgroup Gamma0(4) of weight 10 over Rational Field
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: M = ModularSymbols(12,6)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: T = sage.modular.hecke.submodule.HeckeSubmodule(M, M.new_submodule().free_module())
            sage: S
            Rank 14 submodule of a Hecke module of level 12
            sage: T
            Rank 0 submodule of a Hecke module of level 12
            sage: S > T
            True
            sage: T < S
            True
            sage: S == S
            True
        """
    def ambient_hecke_module(self):
        """
        Return the ambient Hecke module of which this is a submodule.

        EXAMPLES::

            sage: CuspForms(2, 12).ambient_hecke_module()
            Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(2) of weight 12 over Rational Field
        """
    def ambient(self):
        """
        Synonym for ambient_hecke_module.

        EXAMPLES::

            sage: CuspForms(2, 12).ambient()
            Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(2) of weight 12 over Rational Field
        """
    @cached_method
    def complement(self, bound=None):
        '''
        Return the largest Hecke-stable complement of this space.

        EXAMPLES::

            sage: M = ModularSymbols(15, 6).cuspidal_subspace()
            sage: M.complement()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 20 for Gamma_0(15) of weight 6 with sign 0 over Rational Field
            sage: E = EllipticCurve("128a")
            sage: ME = E.modular_symbol_space()
            sage: ME.complement()
            Modular Symbols subspace of dimension 17 of Modular Symbols space of dimension 18 for Gamma_0(128) of weight 2 with sign 1 over Rational Field
        '''
    def degeneracy_map(self, level, t: int = 1):
        """
        The `t`-th degeneracy map from ``self`` to the space of ambient modular
        symbols of the given level. The level of ``self`` must be a divisor or
        multiple of level, and `t` must be a divisor of the quotient.

        INPUT:

        - ``level`` -- positive integer; the level of the codomain of the
          map

        - ``t`` -- integer; the parameter of the degeneracy map,
          i.e., the map is related to `f(q)` - `f(q^t)`

        OUTPUT:

        A linear function from ``self`` to the space of modular symbols of given
        level with the same weight, character, sign, etc., as this space.

        EXAMPLES::

            sage: D = ModularSymbols(10,4).cuspidal_submodule().decomposition(); D
            [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 10 for Gamma_0(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 10 for Gamma_0(10) of weight 4 with sign 0 over Rational Field]
            sage: d = D[1].degeneracy_map(5); d
            Hecke module morphism defined by the matrix
            [   0    0   -1    1]
            [   0  1/2  3/2   -2]
            [   0   -1    1    0]
            [   0 -3/4 -1/4    1]
            Domain: Modular Symbols subspace of dimension 4 of Modular Symbols space ...
            Codomain: Modular Symbols space of dimension 4 for Gamma_0(5) of weight ...

        ::

            sage: d.rank()
            2
            sage: d.kernel()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 10 for Gamma_0(10) of weight 4 with sign 0 over Rational Field
            sage: d.image()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(5) of weight 4 with sign 0 over Rational Field
        """
    @cached_method
    def dual_free_module(self, bound=None, anemic: bool = True, use_star: bool = True):
        """
        Compute embedded dual free module if possible.

        In general this will not be possible, e.g., if this space is
        not Hecke equivariant, possibly if it is not cuspidal, or if
        the characteristic is not 0. In all these cases we raise a
        :exc:`RuntimeError` exception.

        If ``use_star`` is ``True`` (which is the default), we also use the +/-
        eigenspaces for the star operator to find the dual free module of ``self``.
        If ``self`` does not have a star involution, ``use_star`` will automatically be
        set to ``False``.

        EXAMPLES::

            sage: M = ModularSymbols(11, 2)
            sage: M.dual_free_module()
            Vector space of dimension 3 over Rational Field
            sage: Mpc = M.plus_submodule().cuspidal_submodule()
            sage: Mcp = M.cuspidal_submodule().plus_submodule()
            sage: Mcp.dual_free_module() == Mpc.dual_free_module()
            True
            sage: Mpc.dual_free_module()
            Vector space of degree 3 and dimension 1 over Rational Field
            Basis matrix:
            [  1 5/2   5]

            sage: M = ModularSymbols(35,2).cuspidal_submodule()
            sage: M.dual_free_module(use_star=False)
            Vector space of degree 9 and dimension 6 over Rational Field
            Basis matrix:
            [   1    0    0    0   -1    0    0    4   -2]
            [   0    1    0    0    0    0    0 -1/2  1/2]
            [   0    0    1    0    0    0    0 -1/2  1/2]
            [   0    0    0    1   -1    0    0    1    0]
            [   0    0    0    0    0    1    0   -2    1]
            [   0    0    0    0    0    0    1   -2    1]

            sage: M = ModularSymbols(40,2)
            sage: Mmc = M.minus_submodule().cuspidal_submodule()
            sage: Mcm = M.cuspidal_submodule().minus_submodule()
            sage: Mcm.dual_free_module() == Mmc.dual_free_module()
            True
            sage: Mcm.dual_free_module()
            Vector space of degree 13 and dimension 3 over Rational Field
            Basis matrix:
            [ 0  1  0  0  0  0  1  0 -1 -1  1 -1  0]
            [ 0  0  1  0 -1  0 -1  0  1  0  0  0  0]
            [ 0  0  0  0  0  1  1  0 -1  0  0  0  0]

            sage: M = ModularSymbols(43).cuspidal_submodule()
            sage: S = M[0].plus_submodule() + M[1].minus_submodule()
            sage: S.dual_free_module(use_star=False)
            Traceback (most recent call last):
            ...
            RuntimeError: Computation of complementary space failed (cut down to rank 7, but should have cut down to rank 4).
            sage: S.dual_free_module().dimension() == S.dimension()
            True

        We test that :issue:`5080` is fixed::

            sage: EllipticCurve('128a').congruence_number()
            32
        """
    def free_module(self):
        """
        Return the free module corresponding to ``self``.

        EXAMPLES::

            sage: M = ModularSymbols(33,2).cuspidal_subspace() ; M
            Modular Symbols subspace of dimension 6 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field
            sage: M.free_module()
            Vector space of degree 9 and dimension 6 over Rational Field
            Basis matrix:
            [ 0  1  0  0  0  0  0 -1  1]
            [ 0  0  1  0  0  0  0 -1  1]
            [ 0  0  0  1  0  0  0 -1  1]
            [ 0  0  0  0  1  0  0 -1  1]
            [ 0  0  0  0  0  1  0 -1  1]
            [ 0  0  0  0  0  0  1 -1  0]
        """
    def module(self):
        """
        Alias for \\code{self.free_module()}.

        EXAMPLES::

            sage: M = ModularSymbols(17,4).cuspidal_subspace()
            sage: M.free_module() is M.module()
            True
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other``, which must both lie in
        a common ambient space of modular symbols.

        EXAMPLES::

            sage: M = ModularSymbols(43, sign=1)
            sage: A = M[0] + M[1]
            sage: B = M[1] + M[2]
            sage: A.dimension(), B.dimension()
            (2, 3)
            sage: C = A.intersection(B); C.dimension()
            1

        TESTS::

            sage: M = ModularSymbols(1,80)
            sage: M.plus_submodule().cuspidal_submodule().sign() # indirect doctest
            1
        """
    def is_ambient(self) -> bool:
        """
        Return ``True`` if ``self`` is an ambient space of modular symbols.

        EXAMPLES::

            sage: M = ModularSymbols(17,4)
            sage: M.cuspidal_subspace().is_ambient()
            False
            sage: A = M.ambient_hecke_module()
            sage: S = A.submodule(A.basis())
            sage: sage.modular.hecke.submodule.HeckeSubmodule.is_ambient(S)
            True
        """
    def is_new(self, p=None) -> bool:
        """
        Return ``True`` if this Hecke module is `p`-new. If `p` is None,
        returns ``True`` if it is new.

        EXAMPLES::

            sage: M = ModularSymbols(1,16)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S.is_new()
            True
        """
    def is_old(self, p=None) -> bool:
        """
        Return ``True`` if this Hecke module is `p`-old. If `p` is ``None``,
        returns ``True`` if it is old.

        EXAMPLES::

            sage: M = ModularSymbols(50,2)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.old_submodule().free_module())
            sage: S.is_old()
            True
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.new_submodule().free_module())
            sage: S.is_old()
            False
        """
    def is_submodule(self, V) -> bool:
        """
        Return ``True`` if and only if ``self`` is a submodule of V.

        EXAMPLES::

            sage: M = ModularSymbols(30,4)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S.is_submodule(M)
            True
            sage: SS = sage.modular.hecke.submodule.HeckeSubmodule(M, M.old_submodule().free_module())
            sage: S.is_submodule(SS)
            False
        """
    def linear_combination_of_basis(self, v):
        """
        Return the linear combination of the basis of ``self`` given
        by the entries of `v`.

        The result can be of different types, and is printed
        accordingly, depending on the type of submodule.

        EXAMPLES::

            sage: M = ModularForms(Gamma0(2),12)

            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S.basis()
            ((1, 0, 0, 0), (0, 1, 0, 0))
            sage: S.linear_combination_of_basis([3, 10])
            (3, 10, 0, 0)

            sage: S = M.cuspidal_submodule()
            sage: S.basis()
            [q + 252*q^3 - 2048*q^4 + 4830*q^5 + O(q^6), q^2 - 24*q^4 + O(q^6)]
            sage: S.linear_combination_of_basis([3, 10])
            3*q + 10*q^2 + 756*q^3 - 6384*q^4 + 14490*q^5 + O(q^6)
        """
    def new_submodule(self, p=None):
        """
        Return the new or `p`-new submodule of this space of modular
        symbols.

        EXAMPLES::

            sage: M = ModularSymbols(20,4)
            sage: M.new_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_0(20) of weight 4 with sign 0 over Rational Field
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S
            Rank 12 submodule of a Hecke module of level 20
            sage: S.new_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_0(20) of weight 4 with sign 0 over Rational Field
        """
    def nonembedded_free_module(self):
        """
        Return the free module corresponding to ``self`` as an abstract
        free module, i.e. not as an embedded vector space.

        EXAMPLES::

            sage: M = ModularSymbols(12,6)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S
            Rank 14 submodule of a Hecke module of level 12
            sage: S.nonembedded_free_module()
            Vector space of dimension 14 over Rational Field
        """
    def old_submodule(self, p=None):
        """
        Return the old or `p`-old submodule of this space of modular
        symbols.

        EXAMPLES: We compute the old and new submodules of
        `\\mathbf{S}_2(\\Gamma_0(33))`.

        ::

            sage: M = ModularSymbols(33); S = M.cuspidal_submodule(); S
            Modular Symbols subspace of dimension 6 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field
            sage: S.old_submodule()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field
            sage: S.new_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field
        """
    def rank(self):
        """
        Return the rank of ``self`` as a free module over the base ring.

        EXAMPLES::

            sage: ModularSymbols(6, 4).cuspidal_subspace().rank()
            2
            sage: ModularSymbols(6, 4).cuspidal_subspace().dimension()
            2
        """
    def submodule(self, M, Mdual=None, check: bool = True):
        """
        Construct a submodule of ``self`` from the free module M, which
        must be a subspace of ``self``.

        EXAMPLES::

            sage: M = ModularSymbols(18,4)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: S[0]
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_0(18) of weight 4 with sign 0 over Rational Field
            sage: S.submodule(S[0].free_module())
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_0(18) of weight 4 with sign 0 over Rational Field
        """
    def submodule_from_nonembedded_module(self, V, Vdual=None, check: bool = True):
        """
        Construct a submodule of ``self`` from V. Here V should be a
        subspace of a vector space whose dimension is the same as that
        of ``self``.

        INPUT:

        - ``V`` -- submodule of ambient free module of the same
          rank as the rank of ``self``

        - ``check`` -- whether to check that V is Hecke
          equivariant

        OUTPUT: Hecke submodule of self

        EXAMPLES::

            sage: M = ModularSymbols(37,2)
            sage: S = sage.modular.hecke.submodule.HeckeSubmodule(M, M.cuspidal_submodule().free_module())
            sage: V = (QQ**4).subspace([[1,-1,0,1/2],[0,0,1,-1/2]])
            sage: S.submodule_from_nonembedded_module(V)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
        """
    def hecke_bound(self):
        """
        Compute the Hecke bound for ``self``.

        This is a number `n` such that the `T_m` for `m \\leq n`
        generate the Hecke algebra.

        EXAMPLES::

            sage: M = ModularSymbols(24,8)
            sage: M.hecke_bound()
            53
            sage: M.cuspidal_submodule().hecke_bound()
            32
            sage: M.eisenstein_submodule().hecke_bound()
            53
        """
