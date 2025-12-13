from . import algebra as algebra, element as element, hecke_operator as hecke_operator
from sage.arith.misc import GCD as GCD, factor as factor, gcd as gcd, is_prime as is_prime, next_prime as next_prime, prime_divisors as prime_divisors, primes as primes, valuation as valuation
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.verbose import verbose as verbose
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.module import Module as Module
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sequence import Sequence as Sequence

def is_HeckeModule(x):
    """
    Return ``True`` if ``x`` is a Hecke module.

    EXAMPLES::

        sage: from sage.modular.hecke.module import is_HeckeModule
        sage: is_HeckeModule(ModularForms(Gamma0(7), 4))
        doctest:warning...
        DeprecationWarning: the function is_HeckeModule is deprecated;
        use 'isinstance(..., HeckeModule_generic)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
        sage: is_HeckeModule(QQ^3)
        False
        sage: is_HeckeModule(J0(37).homology())
        True
    """

class HeckeModule_generic(Module):
    """
    A very general base class for Hecke modules.

    We define a Hecke module of weight `k` to be a module over a commutative
    ring equipped with an action of operators `T_m` for all positive integers `m`
    coprime to some integer `n`(the level), which satisfy `T_r T_s = T_{rs}` for
    `r,s` coprime, and for powers of a prime `p`, `T_{p^r} = T_{p} T_{p^{r-1}} -
    \\varepsilon(p) p^{k-1} T_{p^{r-2}}`, where `\\varepsilon(p)` is some
    endomorphism of the module which commutes with the `T_m`.

    We distinguish between *full* Hecke modules, which also have an action of
    operators `T_m` for `m` not assumed to be coprime to the level, and
    *anemic* Hecke modules, for which this does not hold.
    """
    Element = element.HeckeModuleElement
    def __init__(self, base_ring, level, category=None) -> None:
        """
        Create a Hecke module. Not intended to be called directly.

        EXAMPLES::

            sage: CuspForms(Gamma0(17),2) # indirect doctest
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(17) of weight 2 over Rational Field
            sage: ModularForms(3, 3).category()
            Category of Hecke modules over Rational Field
        """
    def __hash__(self):
        """
        The hash is determined by the base ring and the level.

        EXAMPLES::

            sage: MS = sage.modular.hecke.module.HeckeModule_generic(QQ,1)
            sage: hash(MS) == hash((MS.base_ring(), MS.level()))
            True
        """
    def anemic_hecke_algebra(self):
        """
        Return the Hecke algebra associated to this Hecke module.

        EXAMPLES::

            sage: T = ModularSymbols(1,12).hecke_algebra()
            sage: A = ModularSymbols(1,12).anemic_hecke_algebra()
            sage: T == A
            False
            sage: A
            Anemic Hecke algebra acting on Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
            sage: A.is_anemic()
            True
        """
    def character(self) -> None:
        """
        Return the character of this space.

        As this is an abstract base class, return ``None``.

        EXAMPLES::

            sage: sage.modular.hecke.module.HeckeModule_generic(QQ, 10).character() is None
            True
        """
    def dimension(self):
        """
        Synonym for :meth:`rank`.

        EXAMPLES::

            sage: M = sage.modular.hecke.module.HeckeModule_generic(QQ, 10).dimension()
            Traceback (most recent call last):
            ...
            NotImplementedError: Derived subclasses must implement rank
        """
    def hecke_algebra(self):
        """
        Return the Hecke algebra associated to this Hecke module.

        EXAMPLES::

            sage: T = ModularSymbols(Gamma1(5),3).hecke_algebra()
            sage: T
            Full Hecke algebra acting on Modular Symbols space of dimension 4 for Gamma_1(5) of weight 3 with sign 0 over Rational Field
            sage: T.is_anemic()
            False

        ::

            sage: M = ModularSymbols(37,sign=1)
            sage: E, A, B = M.decomposition()
            sage: A.hecke_algebra() == B.hecke_algebra()
            False
        """
    def is_zero(self) -> bool:
        """
        Return ``True`` if this Hecke module has dimension 0.

        EXAMPLES::

            sage: ModularSymbols(11).is_zero()
            False
            sage: ModularSymbols(11).old_submodule().is_zero()
            True
            sage: CuspForms(10).is_zero()
            True
            sage: CuspForms(1,12).is_zero()
            False
        """
    def is_full_hecke_module(self) -> bool:
        """
        Return ``True`` if this space is invariant under all Hecke operators.

        Since ``self`` is guaranteed to be an anemic Hecke module, the
        significance of this function is that it also ensures
        invariance under Hecke operators of index that divide the level.

        EXAMPLES::

            sage: M = ModularSymbols(22); M.is_full_hecke_module()
            True
            sage: M.submodule(M.free_module().span([M.0.list()]), check=False).is_full_hecke_module()
            False
        """
    def is_hecke_invariant(self, n) -> bool:
        '''
        Return ``True`` if ``self`` is invariant under the Hecke operator `T_n`.

        Since ``self`` is guaranteed to be an anemic Hecke module it is only
        interesting to call this function when `n` is not coprime
        to the level.

        EXAMPLES::

            sage: M = ModularSymbols(22).cuspidal_subspace()
            sage: M.is_hecke_invariant(2)
            True

        We use ``check=False`` to create a nasty "module" that is not invariant
        under `T_2`::

            sage: S = M.submodule(M.free_module().span([M.0.list()]), check=False); S
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 for Gamma_0(22) of weight 2 with sign 0 over Rational Field
            sage: S.is_hecke_invariant(2)
            False
            sage: [n for n in range(1,12) if S.is_hecke_invariant(n)]
            [1, 3, 5, 7, 9, 11]
        '''
    def level(self):
        """
        Return the level of this modular symbols space.

        INPUT:

        - ``ModularSymbols self`` -- an arbitrary space of modular symbols

        OUTPUT: integer; the level

        EXAMPLES::

            sage: m = ModularSymbols(20)
            sage: m.level()
            20
        """
    def rank(self) -> None:
        """
        Return the rank of this module over its base ring.

        This raises a :exc:`NotImplementedError`, since this is an
        abstract base class.

        EXAMPLES::

            sage: sage.modular.hecke.module.HeckeModule_generic(QQ, 10).rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Derived subclasses must implement rank
        """
    def submodule(self, X) -> None:
        """
        Return the submodule of ``self`` corresponding to ``X``.

        As this is an abstract base class, this raises a
        :exc:`NotImplementedError`.

        EXAMPLES::

            sage: sage.modular.hecke.module.HeckeModule_generic(QQ, 10).submodule(0)
            Traceback (most recent call last):
            ...
            NotImplementedError: Derived subclasses should implement submodule
        """

class HeckeModule_free_module(HeckeModule_generic):
    """
    A Hecke module modeled on a free module over a commutative ring.
    """
    def __init__(self, base_ring, level, weight, category=None) -> None:
        '''
        Initialise a module.

        EXAMPLES::

            sage: M = sage.modular.hecke.module.HeckeModule_free_module(QQ, 12, -4); M
            <class \'sage.modular.hecke.module.HeckeModule_free_module_with_category\'>
            sage: skipped = ["_test_additive_associativity",
            ....:    "_test_an_element", "_test_elements",
            ....:    "_test_elements_eq_reflexive",
            ....:    "_test_elements_eq_symmetric",
            ....:    "_test_elements_eq_transitive", "_test_elements_neq",
            ....:    "_test_pickling", "_test_some_elements",
            ....:    "_test_zero", "_test_eq"]
            sage: TestSuite(M).run(skip=skipped)

        .. NOTE:: Is this supposed to be an abstract parent without elements?
        '''
    def __getitem__(self, n):
        """
        Return the `n`-th term in the decomposition of ``self``.

        See the docstring for :meth:`decomposition` for further information.

        EXAMPLES::

            sage: ModularSymbols(22)[0]
            Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 7 for Gamma_0(22) of weight 2 with sign 0 over Rational Field
        """
    def __hash__(self):
        """
        The hash is determined by the weight, the level and the base ring.

        EXAMPLES::

            sage: MS = ModularSymbols(22)
            sage: hash(MS) == hash((MS.weight(), MS.level(), MS.base_ring()))
            True
        """
    def __len__(self) -> int:
        """
        Return the number of factors in the decomposition of ``self``.

        EXAMPLES::

            sage: len(ModularSymbols(22))
            2
        """
    def ambient(self):
        """
        Return the ambient module associated to this module.

        Synonym for :meth:`ambient_hecke_module`.

        EXAMPLES::

            sage: CuspForms(1, 12).ambient()
            Modular Forms space of dimension 2 for Modular Group SL(2,Z) of weight 12 over Rational Field
        """
    def ambient_module(self):
        """
        Return the ambient module associated to this module.

        Synonym for :meth:`ambient_hecke_module`.

        EXAMPLES::

            sage: CuspForms(1, 12).ambient_module()
            Modular Forms space of dimension 2 for Modular Group SL(2,Z) of weight 12 over Rational Field
            sage: sage.modular.hecke.module.HeckeModule_free_module(QQ, 10, 3).ambient_module()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def ambient_hecke_module(self) -> None:
        """
        Return the ambient module associated to this module.

        As this is an abstract base class, raise :exc:`NotImplementedError`.

        EXAMPLES::

            sage: sage.modular.hecke.module.HeckeModule_free_module(QQ, 10, 3).ambient_hecke_module()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def atkin_lehner_operator(self, d=None):
        """
        Return the Atkin-Lehner operator `W_d` on this space, if defined, where
        `d` is a divisor of the level `N` such that `N/d` and `d` are coprime.
        If `d` is not given, we take `d = N`.  If `N/d` is not coprime to `d`,
        then we replace `d` with the unique integer having this property which
        has the same prime factors as `d`.

        .. NOTE::

            The operator `W_d` is given by the action of any matrix of the form

            .. math::

                W_d = \\begin{pmatrix} dx & y \\\\ Nz & dw \\end{pmatrix}

            with `\\det W_d = d` and such that `x = 1 \\bmod N/d`, `y = 1 \\bmod
            d`, as in [AL1978]_. However, our definition of the weight `k`
            action differs from theirs by a power of the determinant, so our
            operator `W_d` is `d^{k/2 - 1}` times the operator of Atkin-Li. In
            particular, if `k = 2` our conventions are identical to Atkin and
            Li's.

            With Sage's conventions, the operator `W_d` satisfies

            .. math::

                W_d^2 = d^{k - 2} \\langle x^{-1} \\rangle

            where `x` is congruent to `d` modulo `N/d` and to `-1` modulo `d`.
            In particular, the operator is an involution in weight 2 and
            trivial character (but not in most other situations).

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: w = M.atkin_lehner_operator()
            sage: w
            Hecke module morphism Atkin-Lehner operator W_11 defined by the matrix
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0 -1]
            Domain: Modular Symbols space of dimension 3 for Gamma_0(11) of weight ...
            Codomain: Modular Symbols space of dimension 3 for Gamma_0(11) of weight ...
            sage: M = ModularSymbols(Gamma1(13))
            sage: w = M.atkin_lehner_operator()
            sage: w.fcp('x')
            (x - 1)^7 * (x + 1)^8

        ::

            sage: M = ModularSymbols(33)
            sage: S = M.cuspidal_submodule()
            sage: S.atkin_lehner_operator()
            Hecke module morphism Atkin-Lehner operator W_33 defined by the matrix
            [ 0 -1  0  1 -1  0]
            [ 0 -1  0  0  0  0]
            [ 0 -1  0  0 -1  1]
            [ 1 -1  0  0 -1  0]
            [ 0  0  0  0 -1  0]
            [ 0 -1  1  0 -1  0]
            Domain: Modular Symbols subspace of dimension 6 of Modular Symbols space ...
            Codomain: Modular Symbols subspace of dimension 6 of Modular Symbols space ...

        ::

            sage: S.atkin_lehner_operator(3)
            Hecke module morphism Atkin-Lehner operator W_3 defined by the matrix
            [ 0  1  0 -1  1  0]
            [ 0  1  0  0  0  0]
            [ 0  1  0  0  1 -1]
            [-1  1  0  0  1  0]
            [ 0  0  0  0  1  0]
            [ 0  1 -1  0  1  0]
            Domain: Modular Symbols subspace of dimension 6 of Modular Symbols space ...
            Codomain: Modular Symbols subspace of dimension 6 of Modular Symbols space ...

        ::

            sage: N = M.new_submodule()
            sage: N.atkin_lehner_operator()
            Hecke module morphism Atkin-Lehner operator W_33 defined by the matrix
            [  1 2/5 4/5]
            [  0  -1   0]
            [  0   0  -1]
            Domain: Modular Symbols subspace of dimension 3 of Modular Symbols space ...
            Codomain: Modular Symbols subspace of dimension 3 of Modular Symbols space ...
        """
    def basis(self):
        """
        Return a basis for ``self``.

        EXAMPLES::

            sage: m = ModularSymbols(43)
            sage: m.basis()
            ((1,0), (1,31), (1,32), (1,38), (1,39), (1,40), (1,41))
        """
    def basis_matrix(self):
        """
        Return the matrix of the basis vectors of ``self`` (as vectors in some
        ambient module)

        EXAMPLES::

            sage: CuspForms(1, 12).basis_matrix()
            [1 0]
        """
    def coordinate_vector(self, x):
        """
        Write ``x`` as a vector with respect to the basis given by
        self.basis().

        EXAMPLES::

            sage: S = ModularSymbols(11,2).cuspidal_submodule()
            sage: S.0
            (1,8)
            sage: S.basis()
            ((1,8), (1,9))
            sage: S.coordinate_vector(S.0)
            (1, 0)
        """
    def decomposition(self, bound=None, anemic: bool = True, height_guess: int = 1, sort_by_basis: bool = False, proof=None):
        """
        Return the maximal decomposition of this Hecke module under the
        action of Hecke operators of index coprime to the level.

        This is the finest decomposition of ``self`` that we can obtain
        using factors obtained by taking kernels of Hecke operators.

        Each factor in the decomposition is a Hecke submodule obtained as
        the kernel of `f(T_n)^r` acting on self, where n is
        coprime to the level and `r=1`. If anemic is False, instead
        choose `r` so that `f(X)^r` exactly divides the
        characteristic polynomial.

        INPUT:

        - ``anemic`` -- boolean (default: ``True``); if ``True``, use only
          Hecke operators of index coprime to the level

        - ``bound`` -- integer or ``None`` (default: ``None``); if ``None``,
          use all Hecke operators up to the Sturm bound, and hence obtain the
          same result as one would obtain by using every element of the Hecke
          ring. If a fixed integer, decompose using only Hecke operators
          `T_p`, with `p` prime, up to bound.
        - ``sort_by_basis`` -- boolean (default: ``False``); if ``True`` the
          resulting decomposition will be sorted as if it was free modules,
          ignoring the Hecke module structure. This will save a lot of time.

        OUTPUT: list of subspaces of ``self``

        EXAMPLES::

            sage: ModularSymbols(17,2).decomposition()
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(17) of weight 2 with sign 0 over Rational Field]
            sage: ModularSymbols(Gamma1(10),4).decomposition()
            [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 18 for Gamma_1(10) of weight 4 with sign 0 over Rational Field]
            sage: ModularSymbols(GammaH(12, [11])).decomposition()
            [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(12) with H generated by [11] of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(12) with H generated by [11] of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(12) with H generated by [11] of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(12) with H generated by [11] of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 5 of Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(12) with H generated by [11] of weight 2 with sign 0 over Rational Field]

        TESTS::

            sage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
            sage: M.decomposition(3, sort_by_basis = True)
            [Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 154 for Gamma_0(1000) of weight 2 with sign 1 over Rational Field]
        """
    def degree(self):
        """
        Return the degree of this Hecke module.

        This is the rank of the ambient free module.

        EXAMPLES::

            sage: CuspForms(1, 12).degree()
            2
        """
    def dual_eigenvector(self, names: str = 'alpha', lift: bool = True, nz=None):
        """
        Return an eigenvector for the Hecke operators acting on the linear
        dual of this space.

        This eigenvector will have entries in an extension of the base
        ring of degree equal to the dimension of this space.

        .. WARNING::

           The input space must be simple.

        INPUT:

        - ``name`` -- print name of generator for eigenvalue
          field

        - ``lift`` -- boolean (default: ``True``)

        - ``nz`` -- if not ``None``, then normalize vector so dot
          product with this basis vector of ambient space is 1

        OUTPUT:

        A vector with entries possibly in an extension of the base
        ring. This vector is an eigenvector for all Hecke operators acting
        via their transpose.

        If lift = False, instead return an eigenvector in the subspace for
        the Hecke operators on the dual space. I.e., this is an eigenvector
        for the restrictions of Hecke operators to the dual space.

        .. NOTE::

           #. The answer is cached so subsequent calls always return
              the same vector. However, the algorithm is randomized,
              so calls during another session may yield a different
              eigenvector. This function is used mainly for computing
              systems of Hecke eigenvalues.

           #. One can also view a dual eigenvector as defining (via
              dot product) a functional phi from the ambient space of
              modular symbols to a field. This functional phi is an
              eigenvector for the dual action of Hecke operators on
              functionals.

        EXAMPLES::

            sage: SF = ModularSymbols(14).cuspidal_subspace().simple_factors()
            sage: sorted([u.dual_eigenvector() for u in SF])
            [(0, 1, 0, 0, 0), (1, 0, -3, 2, -1)]
        """
    def dual_hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on the dual
        embedded representation of ``self``.

        EXAMPLES::

            sage: CuspForms(1, 24).dual_hecke_matrix(5)
            [     44656110        -15040]
            [-307849789440      28412910]
        """
    def eigenvalue(self, n, name: str = 'alpha'):
        """
        Assuming that ``self`` is a simple space, return the eigenvalue of the
        `n`-th Hecke operator on ``self``.

        INPUT:

        - ``n`` -- index of Hecke operator

        - ``name`` -- print representation of generator of
          eigenvalue field

        EXAMPLES::

            sage: A = ModularSymbols(125,sign=1).new_subspace()[0]
            sage: A.eigenvalue(7)
            -3
            sage: A.eigenvalue(3)
            -alpha - 2
            sage: A.eigenvalue(3,'w')
            -w - 2
            sage: A.eigenvalue(3,'z').charpoly('x')
            x^2 + 3*x + 1
            sage: A.hecke_polynomial(3)
            x^2 + 3*x + 1

        ::

            sage: M = ModularSymbols(Gamma1(17)).decomposition()[8].plus_submodule()
            sage: M.eigenvalue(2,'a')
            a
            sage: M.eigenvalue(4,'a')
            4/3*a^3 + 17/3*a^2 + 28/3*a + 8/3

        .. NOTE::

           #. In fact there are `d` systems of eigenvalues
              associated to self, where `d` is the rank of
              ``self``. Each of the systems of eigenvalues is conjugate
              over the base field. This function chooses one of the
              systems and consistently returns eigenvalues from that
              system. Thus these are the coefficients `a_n` for
              `n\\geq 1` of a modular eigenform attached to ``self``.

           #. This function works even for Eisenstein subspaces,
              though it will not give the constant coefficient of one
              of the corresponding Eisenstein series (i.e., the
              generalized Bernoulli number).

        TESTS:

        This checks that :issue:`15201` is fixed::

            sage: M = ModularSymbols(5, 6, sign=1)
            sage: f = M.decomposition()[0]
            sage: f.eigenvalue(10)
            50
        """
    def factor_number(self):
        """
        If this Hecke module was computed via a decomposition of another
        Hecke module, this is the corresponding number. Otherwise return
        -1.

        EXAMPLES::

            sage: ModularSymbols(23)[0].factor_number()
            0
            sage: ModularSymbols(23).factor_number()
            -1
        """
    def gens(self) -> tuple:
        """
        Return a tuple of basis elements of ``self``.

        EXAMPLES::

            sage: ModularSymbols(23).gens()
            ((1,0), (1,17), (1,19), (1,20), (1,21))
        """
    def gen(self, n):
        """
        Return the `n`-th basis vector of the space.

        EXAMPLES::

            sage: ModularSymbols(23).gen(1)
            (1,17)
        """
    def hecke_matrix(self, n):
        """
        Return the matrix of the `n`-th Hecke operator acting on given basis.

        EXAMPLES::

            sage: C = CuspForms(1, 16)
            sage: C.hecke_matrix(3)
            [-3348]
        """
    def hecke_operator(self, n):
        """
        Return the `n`-th Hecke operator `T_n`.

        INPUT:

        - ``n`` -- integer at least 1

        EXAMPLES::

            sage: M = ModularSymbols(11,2)
            sage: T = M.hecke_operator(3) ; T
            Hecke operator T_3 on Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: T.matrix()
            [ 4  0 -1]
            [ 0 -1  0]
            [ 0  0 -1]
            sage: T(M.0)
            4*(1,0) - (1,9)
            sage: S = M.cuspidal_submodule()
            sage: T = S.hecke_operator(3) ; T
            Hecke operator T_3 on Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: T.matrix()
            [-1  0]
            [ 0 -1]
            sage: T(S.0)
            -(1,8)
        """
    def diamond_bracket_matrix(self, d):
        """
        Return the matrix of the diamond bracket operator `\\langle d \\rangle` on ``self``.

        EXAMPLES::

            sage: M = ModularSymbols(DirichletGroup(5).0, 3)
            sage: M.diamond_bracket_matrix(3)
            [-zeta4      0]
            [     0 -zeta4]
            sage: ModularSymbols(Gamma1(5), 3).diamond_bracket_matrix(3)
            [ 0  1  0  0]
            [-1  0  0  0]
            [ 0  0  0  1]
            [ 0  0 -1  0]
        """
    def diamond_bracket_operator(self, d):
        """
        Return the diamond bracket operator `\\langle d \\rangle` on ``self``.

        EXAMPLES::

            sage: M = ModularSymbols(DirichletGroup(5).0, 3)
            sage: M.diamond_bracket_operator(3)
            Diamond bracket operator <3> on Modular Symbols space of dimension 2 and level 5, weight 3, character [zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
        """
    def T(self, n):
        """
        Return the `n`-th Hecke operator `T_n`.

        This function is a synonym for :meth:`hecke_operator`.

        EXAMPLES::

            sage: M = ModularSymbols(11,2)
            sage: M.T(3)
            Hecke operator T_3 on Modular Symbols ...
        """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the characteristic polynomial of the `n`-th Hecke operator
        acting on this space.

        INPUT:

        - ``n`` -- integer

        OUTPUT: a polynomial

        EXAMPLES::

            sage: ModularSymbols(11,2).hecke_polynomial(3)
            x^3 - 2*x^2 - 7*x - 4
        """
    def is_simple(self) -> bool:
        """
        Return ``True`` if this space is simple as a module for the
        corresponding Hecke algebra.

        This raises :exc:`NotImplementedError`, as this is an abstract base
        class.

        EXAMPLES::

            sage: sage.modular.hecke.module.HeckeModule_free_module(QQ, 10, 3).is_simple()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def is_splittable(self) -> bool:
        """
        Return ``True`` if and only if only it is possible to split
        off a nontrivial generalized eigenspace of ``self`` as the
        kernel of some Hecke operator (not necessarily prime to the level).

        Note that the direct sum of several copies of the same simple
        module is not splittable in this sense.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma0(64)).cuspidal_subspace()
            sage: M.is_splittable()
            True
            sage: M.simple_factors()[0].is_splittable()
            False
        """
    def is_submodule(self, other) -> bool:
        """
        Return ``True`` if ``self`` is a submodule of ``other``.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma0(64))
            sage: M[0].is_submodule(M)
            True
            sage: CuspForms(1, 24).is_submodule(ModularForms(1, 24))
            True
            sage: CuspForms(1, 12).is_submodule(CuspForms(3, 12))
            False
        """
    def is_splittable_anemic(self) -> bool:
        """
        Return ``True`` if and only if only it is possible to split off a
        nontrivial generalized eigenspace of ``self`` as the kernel of some
        Hecke operator of index coprime to the level.

        Note that the direct sum of several copies of the same simple
        module is not splittable in this sense.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma0(64)).cuspidal_subspace()
            sage: M.is_splittable_anemic()
            True
            sage: M.simple_factors()[0].is_splittable_anemic()
            False
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        This is equal to the rank.

        EXAMPLES::

            sage: ModularForms(1, 12).ngens()
            2
        """
    def projection(self):
        """
        Return the projection map from the ambient space to ``self``.

        ALGORITHM: Let `B` be the matrix whose columns are obtained
        by concatenating together a basis for the factors of the ambient
        space. Then the projection matrix onto ``self`` is the submatrix of
        `B^{-1}` obtained from the rows corresponding to self,
        i.e., if the basis vectors for ``self`` appear as columns `n`
        through `m` of `B`, then the projection matrix is
        got from rows `n` through `m` of `B^{-1}`.
        This is because projection with respect to the B basis is just
        given by an `m-n+1` row slice `P` of a diagonal
        matrix D with 1s in the `n` through `m` positions,
        so projection with respect to the standard basis is given by
        `P\\cdot B^{-1}`, which is just rows `n`
        through `m` of `B^{-1}`.

        EXAMPLES::

            sage: e = EllipticCurve('34a')
            sage: m = ModularSymbols(34); s = m.cuspidal_submodule()
            sage: d = s.decomposition(7)
            sage: d
            [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field,
             Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field]
            sage: a = d[0]; a
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field
            sage: pi = a.projection()
            sage: pi(m([0,oo]))
            -1/6*(2,7) + 1/6*(2,13) - 1/6*(2,31) + 1/6*(2,33)
            sage: M = ModularSymbols(53,sign=1)
            sage: S = M.cuspidal_subspace()[1] ; S
            Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field
            sage: p = S.projection()
            sage: S.basis()
            ((1,43) - (1,45), (1,47), (1,50))
            sage: [ p(x) for x in S.basis() ]
            [(1,43) - (1,45), (1,47), (1,50)]
            sage: all(p(x)==x for x in S.basis())
            True
        """
    def system_of_eigenvalues(self, n, name: str = 'alpha'):
        '''
        Assuming that ``self`` is a simple space of modular symbols, return the
        eigenvalues `[a_1, \\ldots, a_nmax]` of the Hecke
        operators on ``self``. See ``self.eigenvalue(n)`` for more
        details.

        INPUT:

        - ``n`` -- number of eigenvalues

        - ``alpha`` -- name of generate for eigenvalue field

        EXAMPLES:

        The outputs of the following tests are very unstable. The algorithms
        are randomized and depend on cached results. A slight change in the
        sequence of pseudo-random numbers or a modification in caching is
        likely to modify the results. We reset the random number generator and
        clear some caches for reproducibility::

            sage: set_random_seed(0)
            sage: ModularSymbols_clear_cache()

        We compute eigenvalues for newforms of level 62::

            sage: M = ModularSymbols(62,2,sign=-1)
            sage: S = M.cuspidal_submodule().new_submodule()
            sage: [[o.minpoly() for o in A.system_of_eigenvalues(3)] for A in S.decomposition()]
            [[x - 1, x - 1, x], [x - 1, x + 1, x^2 - 2*x - 2]]

        Next we define a function that does the above::

            sage: def b(N, k=2):
            ....:    S = ModularSymbols(N,k,sign=-1).cuspidal_submodule().new_submodule()
            ....:    for A in S.decomposition():
            ....:        print("{} {}".format(N, A.system_of_eigenvalues(5)))

        ::

            sage: b(63)
            63 [1, 1, 0, -1, 2]
            63 [1, alpha, 0, 1, -2*alpha]

        This example illustrates finding field over which the eigenvalues
        are defined::

            sage: M = ModularSymbols(23,2,sign=1).cuspidal_submodule().new_submodule()
            sage: v = M.system_of_eigenvalues(10); v
            [1, alpha, -2*alpha - 1, -alpha - 1, 2*alpha, alpha - 2, 2*alpha + 2, -2*alpha - 1, 2, -2*alpha + 2]
            sage: v[0].parent()
            Number Field in alpha with defining polynomial x^2 + x - 1

        This example illustrates setting the print name of the eigenvalue
        field.

        ::

            sage: A = ModularSymbols(125,sign=1).new_subspace()[0]
            sage: A.system_of_eigenvalues(10)
            [1, alpha, -alpha - 2, -alpha - 1, 0, -alpha - 1, -3, -2*alpha - 1, 3*alpha + 2, 0]
            sage: A.system_of_eigenvalues(10,\'x\')
            [1, x, -x - 2, -x - 1, 0, -x - 1, -3, -2*x - 1, 3*x + 2, 0]
        '''
    def weight(self):
        """
        Return the weight of this Hecke module.

        INPUT:

        - ``self`` -- an arbitrary Hecke module

        OUTPUT: integer; the weight

        EXAMPLES::

            sage: m = ModularSymbols(20, weight=2)
            sage: m.weight()
            2
        """
    def zero_submodule(self):
        """
        Return the zero submodule of ``self``.

        EXAMPLES::

            sage: ModularSymbols(11,4).zero_submodule()
            Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 6 for Gamma_0(11) of weight 4 with sign 0 over Rational Field
            sage: CuspForms(11,4).zero_submodule()
            Modular Forms subspace of dimension 0 of Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(11) of weight 4 over Rational Field
        """
