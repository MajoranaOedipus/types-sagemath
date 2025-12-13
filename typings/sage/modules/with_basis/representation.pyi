from _typeshed import Incomplete
from sage.categories.modules import Modules as Modules
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule, CombinatorialFreeModule_Tensor as CombinatorialFreeModule_Tensor
from sage.matrix.constructor import matrix as matrix
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.modules.with_basis.subquotient import QuotientModuleWithBasis as QuotientModuleWithBasis, SubmoduleWithBasis as SubmoduleWithBasis
from sage.structure.element import Element as Element

class Representation_abstract:
    """
    Abstract base class for representations of semigroups.

    INPUT:

    - ``semigroup`` -- a semigroup
    - ``side`` -- (default: ``'left'``) whether this is a
      ``'left'`` or ``'right'`` representation
    - ``algebra`` -- (default: ``semigroup.algebra(self.base_ring())``)
      the semigroup algebra

    .. NOTE::

        This class should come before :class:`CombinatorialFreeModule` in the
        MRO in order for tensor products to use the correct class.
    """
    __class__: Incomplete
    def __init__(self, semigroup, side, algebra=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = FreeGroup(3)
            sage: T = G.trivial_representation()
            sage: TestSuite(T).run()

        Verify that the dynamic mixin classes work::

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: S21 = SGA.specht_module([2,1])
            sage: T = tensor([S21, S21])
            sage: s21 = S21.frobenius_image()
            sage: T.frobenius_image() == s21.kronecker_product(s21)
            True
        """
    def semigroup(self):
        """
        Return the semigroup whose representation ``self`` is.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: M = CombinatorialFreeModule(QQ, ['v'])
            sage: on_basis = lambda g,m: M.term(m, g.sign())
            sage: R = G.representation(M, on_basis)
            sage: R.semigroup()
            Symmetric group of order 4! as a permutation group
        """
    def semigroup_algebra(self):
        """
        Return the semigroup algebra whose representation ``self`` is.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: M = CombinatorialFreeModule(QQ, ['v'])
            sage: on_basis = lambda g,m: M.term(m, g.sign())
            sage: R = G.representation(M, on_basis)
            sage: R.semigroup_algebra()
            Symmetric group algebra of order 4 over Rational Field
        """
    def side(self):
        """
        Return whether ``self`` is a left, right, or two-sided representation.

        OUTPUT: the string ``'left'``, ``'right'``, or ``'twosided'``

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(4)
            sage: R = G.regular_representation()
            sage: R.side()
            'left'
            sage: S = G.regular_representation(side='right')
            sage: S.side()
            'right'
            sage: R = G.sign_representation()
            sage: R.side()
            'twosided'
            sage: R = G.trivial_representation()
            sage: R.side()
            'twosided'
        """
    def invariant_module(self, S=None, **kwargs):
        """
        Return the submodule of ``self`` invariant under the action of ``S``.

        For a semigroup `S` acting on a module `M`, the invariant
        submodule is given by

        .. MATH::

            M^S = \\{m \\in M : s \\cdot m = m \\forall s \\in S\\}.

        INPUT:

        - ``S`` -- a finitely-generated semigroup (default: the semigroup
          this is a representation of)
        - ``action`` -- a function (default: :obj:`operator.mul`)
        - ``side`` -- ``'left'`` or ``'right'`` (default: :meth:`side()`);
          which side of ``self`` the elements of ``S`` acts

        .. NOTE::

            Two sided actions are considered as left actions for the
            invariant module.

        OUTPUT: :class:`~sage.modules.with_basis.invariant.FiniteDimensionalInvariantModule`

        EXAMPLES::

            sage: S3 = SymmetricGroup(3)
            sage: M = S3.regular_representation()
            sage: I = M.invariant_module()
            sage: [I.lift(b) for b in I.basis()]
            [() + (2,3) + (1,2) + (1,2,3) + (1,3,2) + (1,3)]

        We build the `D_4`-invariant representation inside of the regular
        representation of `S_4`::

            sage: D4 = groups.permutation.Dihedral(4)
            sage: S4 = SymmetricGroup(4)
            sage: R = S4.regular_representation()
            sage: I = R.invariant_module(D4)
            sage: [I.lift(b) for b in I.basis()]
            [() + (2,4) + (1,2)(3,4) + (1,2,3,4) + (1,3) + (1,3)(2,4) + (1,4,3,2) + (1,4)(2,3),
             (3,4) + (2,3,4) + (1,2) + (1,2,4) + (1,3,2) + (1,3,2,4) + (1,4,3) + (1,4,2,3),
             (2,3) + (2,4,3) + (1,2,3) + (1,2,4,3) + (1,3,4,2) + (1,3,4) + (1,4,2) + (1,4)]
        """
    def twisted_invariant_module(self, chi, G=None, **kwargs):
        """
        Create the isotypic component of the action of ``G`` on
        ``self`` with irreducible character given by ``chi``.

        .. SEEALSO::

            - :class:`~sage.modules.with_basis.invariant.FiniteDimensionalTwistedInvariantModule`

        INPUT:

        - ``chi`` -- list/tuple of character values or an instance
          of :class:`~sage.groups.class_function.ClassFunction_gap`
        - ``G`` -- a finitely-generated semigroup (default: the semigroup
          this is a representation of)

        This also accepts the first argument to be the group.

        OUTPUT: :class:`~sage.modules.with_basis.invariant.FiniteDimensionalTwistedInvariantModule`

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: R = G.regular_representation(QQ)
            sage: T = R.twisted_invariant_module([2,0,-1])
            sage: T.basis()
            Finite family {0: B[0], 1: B[1], 2: B[2], 3: B[3]}
            sage: [T.lift(b) for b in T.basis()]
            [() - (1,2,3), -(1,2,3) + (1,3,2), (2,3) - (1,2), -(1,2) + (1,3)]

        We check the different inputs work::

            sage: R.twisted_invariant_module([2,0,-1], G) is T
            True
            sage: R.twisted_invariant_module(G, [2,0,-1]) is T
            True
        """
    def representation_matrix(self, g, side=None, sparse: bool = False):
        """
        Return the matrix representation of ``g`` acting on ``self``.

        EXAMPLES::

            sage: S3 = SymmetricGroup(3)
            sage: g = S3.an_element(); g
            (2,3)
            sage: L = S3.regular_representation(side='left')
            sage: R = S3.regular_representation(side='right')
            sage: R.representation_matrix(g)
            [0 0 0 1 0 0]
            [0 0 0 0 0 1]
            [0 0 0 0 1 0]
            [1 0 0 0 0 0]
            [0 0 1 0 0 0]
            [0 1 0 0 0 0]
            sage: L.representation_matrix(g)
            [0 0 0 1 0 0]
            [0 0 0 0 1 0]
            [0 0 0 0 0 1]
            [1 0 0 0 0 0]
            [0 1 0 0 0 0]
            [0 0 1 0 0 0]
            sage: A = S3.algebra(ZZ)
            sage: R.representation_matrix(sum(A.basis()), side='right')
            [1 1 1 1 1 1]
            [1 1 1 1 1 1]
            [1 1 1 1 1 1]
            [1 1 1 1 1 1]
            [1 1 1 1 1 1]
            [1 1 1 1 1 1]

        We verify tensor products agree::

            sage: T = tensor([L, R])
            sage: for g in S3:
            ....:     gL = L.representation_matrix(g, side='left')
            ....:     gR = R.representation_matrix(g, side='left')
            ....:     gT = T.representation_matrix(g, side='left')
            ....:     assert gL.tensor_product(gR) == gT

        Some examples with Specht modules::

            sage: SM = Partition([3,1,1]).specht_module(QQ)
            sage: SM.representation_matrix(Permutation([2,1,3,5,4]))
            [-1  0  1  0  1  0]
            [ 0  0  0 -1 -1 -1]
            [ 0  0  0  0  1  0]
            [ 0 -1 -1  0  0  1]
            [ 0  0  1  0  0  0]
            [ 0  0  0  0  0 -1]

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([(0,0), (0,1), (0,2), (1,0), (2,0)])
            sage: SM.representation_matrix(Permutation([2,1,3,5,4]))
            [-1  0  0  0  0  0]
            [ 0  0  1  0  0  0]
            [ 0  1  0  0  0  0]
            [ 1  0 -1  0 -1  0]
            [-1 -1  0 -1  0  0]
            [ 0  1  1  0  0 -1]
            sage: SM.representation_matrix(SGA([3,1,5,2,4]))
            [ 0  0  0  0  1  0]
            [-1  0  0  0  0  0]
            [ 0  0  0 -1  0  0]
            [ 1  0 -1  0 -1  0]
            [ 0  0  0  1  1  1]
            [-1 -1  0 -1  0  0]

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: SM = SGA.specht_module([3, 1])
            sage: all(SM.representation_matrix(g) * b.to_vector() == (g * b).to_vector()
            ....:     for b in SM.basis() for g in SGA.group())
            True

            sage: SGA = SymmetricGroupAlgebra(QQ, SymmetricGroup(4))
            sage: SM = SGA.specht_module([3, 1])
            sage: all(SM.representation_matrix(g) * b.to_vector() == (g * b).to_vector()
            ....:     for b in SM.basis() for g in SGA.group())
            True
        """
    @cached_method
    def character(self):
        """
        Return the character of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([3,2])
            sage: SM.character()
            (5, 1, 1, -1, 1, -1, 0)
            sage: matrix(SGA.specht_module(la).character() for la in Partitions(5))
            [ 1  1  1  1  1  1  1]
            [ 4  2  0  1 -1  0 -1]
            [ 5  1  1 -1  1 -1  0]
            [ 6  0 -2  0  0  0  1]
            [ 5 -1  1 -1 -1  1  0]
            [ 4 -2  0  1  1  0 -1]
            [ 1 -1  1  1 -1 -1  1]

            sage: SGA = SymmetricGroupAlgebra(QQ, SymmetricGroup(5))
            sage: SM = SGA.specht_module([3,2])
            sage: SM.character()
            Character of Symmetric group of order 5! as a permutation group
            sage: SM.character().values()
            [5, 1, 1, -1, 1, -1, 0]
            sage: matrix(SGA.specht_module(la).character().values() for la in reversed(Partitions(5)))
            [ 1 -1  1  1 -1 -1  1]
            [ 4 -2  0  1  1  0 -1]
            [ 5 -1  1 -1 -1  1  0]
            [ 6  0 -2  0  0  0  1]
            [ 5  1  1 -1  1 -1  0]
            [ 4  2  0  1 -1  0 -1]
            [ 1  1  1  1  1  1  1]
            sage: SGA.group().character_table()
            [ 1 -1  1  1 -1 -1  1]
            [ 4 -2  0  1  1  0 -1]
            [ 5 -1  1 -1 -1  1  0]
            [ 6  0 -2  0  0  0  1]
            [ 5  1  1 -1  1 -1  0]
            [ 4  2  0  1 -1  0 -1]
            [ 1  1  1  1  1  1  1]
        """
    @cached_method
    def brauer_character(self):
        """
        Return the Brauer character of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: SM = SGA.specht_module([3, 2])
            sage: SM.brauer_character()
            (5, -1, 0)
            sage: SM.simple_module().brauer_character()
            (4, -2, -1)

            sage: T = SM.subrepresentation([])
            sage: T.brauer_character()
            (0, 0, 0)

            sage: W = CoxeterGroup(['D', 4], implementation='permutation')
            sage: R = W.reflection_representation(GF(2))
            sage: R.brauer_character()
            (4, 1)
            sage: T = R.subrepresentation([])
            sage: T.brauer_character()
            (0, 0)
        """
    def exterior_power(self, degree=None):
        """
        Return the exterior power of ``self``.

        INPUT:

        - ``degree`` -- (optional) if given, then only consider the
          given degree

        EXAMPLES::

            sage: DC3 = groups.permutation.DiCyclic(3)
            sage: L = DC3.regular_representation(QQ, side='left')
            sage: E5 = L.exterior_power(5)
            sage: E5
            Exterior power representation of Left Regular Representation of
             Dicyclic group of order 12 as a permutation group over Rational Field
             in degree 5
            sage: L.exterior_power()
            Exterior algebra representation of Left Regular Representation of
             Dicyclic group of order 12 as a permutation group over Rational Field
        """
    def symmetric_power(self, degree=None):
        """
        Return the symmetric power of ``self`` in degree ``degree``.

        EXAMPLES::

            sage: W = CoxeterGroup(['H', 3])
            sage: R = W.reflection_representation()
            sage: S3R = R.symmetric_power(3)
            sage: S3R
            Symmetric power representation of Reflection representation of
            Finite Coxeter group over ... with Coxeter matrix:
            [1 3 2]
            [3 1 5]
            [2 5 1] in degree 3
        """
    def schur_functor(self, la):
        """
        Return the :class:`Schur functor
        <sage.modules.with_basis.representation.SchurFunctorRepresentation>`
        with shape ``la`` applied to ``self``.

        EXAMPLES::

            sage: W = CoxeterGroup(['H', 3])
            sage: R = W.reflection_representation()
            sage: S111 = R.schur_functor([1,1,1])
            sage: S111.dimension()
            1
            sage: S3 = R.schur_functor([3])
            sage: S3.dimension()
            10
        """
    @cached_method
    def is_irreducible(self) -> bool:
        """
        Return if ``self`` is an irreducible module or not.

        A representation `M` is *irreducible* (also known as simple)
        if the only subrepresentations of `M` are the trivial module
        `\\{0\\}` and `M` itself.

        EXAMPLES::

            sage: DC3 = groups.permutation.DiCyclic(3)
            sage: L = DC3.regular_representation(GF(3), side='left')
            sage: L.is_irreducible()
            False
            sage: E3 = L.exterior_power(3)
            sage: E3.is_irreducible()
            False
            sage: E12 = L.exterior_power(12)
            sage: E12.is_irreducible()
            True

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: SGA.specht_module([3, 2]).is_irreducible()
            False
            sage: SGA.specht_module([4, 1]).is_irreducible()
            True
        """
    def find_subrepresentation(self):
        """
        Return a nontrivial (not ``self`` or the trivial module) submodule
        of ``self`` or ``None`` if ``self`` is irreducible.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: SM = SGA.specht_module([3, 2])
            sage: U = SM.find_subrepresentation()
            sage: [SM(b) for b in U.basis()]
            [S[[1, 2, 3], [4, 5]] + S[[1, 2, 4], [3, 5]]
             + S[[1, 2, 5], [3, 4]] + S[[1, 3, 4], [2, 5]]]
            sage: B = U.basis()[0].lift()
            sage: all(g * B == B for g in SGA.gens())
            True
            sage: SGA.specht_module([4, 1]).find_subrepresentation() is None
            True
            sage: SGA.specht_module([5]).find_subrepresentation() is None
            True
        """
    def subrepresentation(self, gens, check: bool = True, already_echelonized: bool = False, *args, is_closed: bool = False, **opts):
        """
        Construct a subrepresentation of ``self`` generated by ``gens``.

        INPUT:

        - ``gens`` -- the generators of the submodule
        - ``check`` -- ignored
        - ``already_echelonized`` -- (default: ``False``) whether
          the elements of ``gens`` are already in (not necessarily
          reduced) echelon form
        - ``is_closed`` -- (keyword only; default: ``False``) whether ``gens``
          already spans the subspace closed under the semigroup action

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: SM = SGA.specht_module([3, 2])
            sage: B = next(iter(SM.basis()))
            sage: U = SM.subrepresentation([B])
            sage: U.dimension()
            5
        """
    def quotient_representation(self, subrepr, already_echelonized: bool = False, **kwds):
        """
        Construct a quotient representation of ``self`` by ``subrepr``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: SM = SGA.specht_module([3, 2])
            sage: v = sum(list(SM.basis())[1:])
            sage: Q = SM.quotient_representation([v]); Q
            Quotient representation with basis {[[1, 3, 5], [2, 4]],
             [[1, 3, 4], [2, 5]], [[1, 2, 4], [3, 5]], [[1, 2, 3], [4, 5]]}
             of Specht module of [3, 2] over Finite Field of size 2
            sage: Q.is_irreducible()
            True
        """
    def composition_series(self):
        """
        Return a composition series of ``self``.

        EXAMPLES:

        The algorithm used here uses random elements, so we set the seed
        for testing purposes::

            sage: set_random_seed(0)
            sage: G = groups.permutation.Dihedral(5)
            sage: CFM = CombinatorialFreeModule(GF(2), [1, 2, 3, 4, 5],
            ....:                               bracket=False, prefix='e')
            sage: CFM.an_element()
            e3
            sage: R = G.representation(CFM, lambda g, i: CFM.basis()[g(i)], side='right')
            sage: CS = R.composition_series()
            sage: len(CS)
            3
            sage: [[R(b) for b in F.basis()] for F in CS]
            [[e1, e2, e3, e4, e5], [e1 + e5, e2 + e5, e3 + e5, e4 + e5], []]
            sage: [F.brauer_character() for F in CS]
            [(5, 0, 0), (4, -1, -1), (0, 0, 0)]
            sage: [F.brauer_character() for F in R.composition_factors()]
            [(1, 1, 1), (4, -1, -1)]
            sage: Reg = G.regular_representation(GF(2))
            sage: simple_brauer_chars = set([F.brauer_character()
            ....:                            for F in Reg.composition_factors()])
            sage: sorted(simple_brauer_chars)
            [(1, 1, 1), (4, -1, -1)]
        """
    def composition_factors(self):
        """
        Return the composition factors of ``self``.

        Given a composition series `V = V_0 \\subseteq V_1 \\subseteq \\cdots
        \\subseteq V_{\\ell} = 0`, the composition factor `S_i` is defined as
        `V_i / V_{i+1}`.

        EXAMPLES:

        The algorithm used here uses random elements, so we set the seed
        for testing purposes::

            sage: set_random_seed(0)
            sage: SGA = SymmetricGroupAlgebra(GF(3), 6)
            sage: SM = SGA.specht_module([4, 1, 1])
            sage: CF = SM.composition_factors()
            sage: CF
            (Quotient representation with basis
              {[[1, 2, 5, 6], [3], [4]], [[1, 2, 4, 6], [3], [5]], [[1, 2, 3, 6], [4], [5]],
               [[1, 2, 4, 5], [3], [6]], [[1, 2, 3, 5], [4], [6]], [[1, 2, 3, 4], [5], [6]]}
              of Specht module of [4, 1, 1] over Finite Field of size 3,
             Subrepresentation with basis {0, 1, 2, 3} of Specht module
              of [4, 1, 1] over Finite Field of size 3)
            sage: x = SGA.an_element()
            sage: v = CF[1].an_element(); v
            2*B[0] + 2*B[1]
            sage: x * v
            B[1] + B[2]

        We reproduce the decomposition matrix for `S_5` over `\\GF{2}`::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: simples = [SGA.simple_module(la).brauer_character()
            ....:            for la in SGA.simple_module_parameterization()]
            sage: D = []
            sage: for la in Partitions(5):
            ....:     SM = SGA.specht_module(la)
            ....:     data = [CF.brauer_character() for CF in SM.composition_factors()]
            ....:     D.append([data.count(bc) for bc in simples])
            sage: matrix(D)
            [1 0 0]
            [0 1 0]
            [1 0 1]
            [2 0 1]
            [1 0 1]
            [0 1 0]
            [1 0 0]
        """
    class Element(CombinatorialFreeModule.Element): ...

class Representation(Representation_abstract, CombinatorialFreeModule):
    """
    Representation of a semigroup.

    INPUT:

    - ``semigroup`` -- a semigroup
    - ``module`` -- a module with a basis
    - ``on_basis`` -- function which takes as input ``g``, ``m``, where
      ``g`` is an element of the semigroup and ``m`` is an element of the
      indexing set for the basis, and returns the result of ``g`` acting
      on ``m``
    - ``side`` -- (default: ``'left'``) whether this is a
      ``'left'`` or ``'right'`` representation

    EXAMPLES:

    We construct the sign representation of a symmetric group::

        sage: G = SymmetricGroup(4)
        sage: M = CombinatorialFreeModule(QQ, ['v'])
        sage: on_basis = lambda g,m: M.term(m, g.sign())
        sage: R = G.representation(M, on_basis)
        sage: x = R.an_element(); x
        2*B['v']
        sage: c,s = G.gens()
        sage: c,s
        ((1,2,3,4), (1,2))
        sage: c * x
        -2*B['v']
        sage: s * x
        -2*B['v']
        sage: c * s * x
        2*B['v']
        sage: (c * s) * x
        2*B['v']

    This extends naturally to the corresponding group algebra::

        sage: A = G.algebra(QQ)
        sage: s,c = A.algebra_generators()
        sage: c,s
        ((1,2,3,4), (1,2))
        sage: c * x
        -2*B['v']
        sage: s * x
        -2*B['v']
        sage: c * s * x
        2*B['v']
        sage: (c * s) * x
        2*B['v']
        sage: (c + s) * x
        -4*B['v']

    REFERENCES:

    - :wikipedia:`Group_representation`
    """
    product_on_basis: Incomplete
    def __init__(self, semigroup, module, on_basis, side: str = 'left', **kwargs) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: M = CombinatorialFreeModule(QQ, ['v'])
            sage: def on_basis(g, m):
            ....:     return M.term(m, g.sign())
            sage: R = G.representation(M, on_basis)
            sage: R._test_representation()

            sage: G = CyclicPermutationGroup(3)
            sage: M = algebras.Exterior(QQ, 'x', 3)
            sage: def on_basis(g, m):  # cyclically permute generators
            ....:     return M.prod([M.monomial(FrozenBitset([g(j+1)-1])) for j in m])
            sage: from sage.categories.algebras import Algebras
            sage: R = G.representation(M, on_basis, category=Algebras(QQ).WithBasis().FiniteDimensional())
            sage: r = R.an_element(); r
            1 + 2*x0 + x0*x1 + 3*x1
            sage: r*r
            1 + 4*x0 + 2*x0*x1 + 6*x1
            sage: x0, x1, x2 = M.gens()
            sage: s = R(x0*x1)
            sage: g = G.an_element()
            sage: g*s
            x1*x2
            sage: g*R(x1*x2)
            -x0*x2
            sage: g*r
            1 + 2*x1 + x1*x2 + 3*x2
            sage: g^2*r
            1 + 3*x0 - x0*x2 + 2*x2

            sage: G = SymmetricGroup(4)
            sage: A = SymmetricGroup(4).algebra(QQ)
            sage: def action(g, x):
            ....:     return A.monomial(g*x)
            sage: category = Algebras(QQ).WithBasis().FiniteDimensional()
            sage: R = G.representation(A, action, 'left', category=category)
            sage: r = R.an_element(); r
            () + (2,3,4) + 2*(1,3)(2,4) + 3*(1,4)(2,3)
            sage: r^2
            14*() + 2*(2,3,4) + (2,4,3) + 12*(1,2)(3,4) + 3*(1,2,4) + 2*(1,3,2) + 4*(1,3)(2,4) + 5*(1,4,3) + 6*(1,4)(2,3)
            sage: g = G.an_element(); g
            (2,3,4)
            sage: g*r
            (2,3,4) + (2,4,3) + 2*(1,3,2) + 3*(1,4,3)
        """
    def product_by_coercion(self, left, right):
        """
        Return the product of ``left`` and ``right`` by passing to
        ``self._module`` and then building a new element of ``self``.

        EXAMPLES::

            sage: G = groups.permutation.KleinFour()
            sage: E = algebras.Exterior(QQ,'e',4)
            sage: on_basis = lambda g,m: E.monomial(m) # the trivial representation
            sage: R = G.representation(E, on_basis)
            sage: r = R.an_element(); r
            1 + 2*e0 + 3*e1 + e1*e2
            sage: g = G.an_element();
            sage: g * r == r  # indirect doctest
            True
            sage: r * r  # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
             'Representation of The Klein 4 group of order 4, as a permutation
             group indexed by Subsets of {0,1,...,3} over Rational Field' and
             'Representation of The Klein 4 group of order 4, as a permutation
             group indexed by Subsets of {0,1,...,3} over Rational Field'

            sage: from sage.categories.algebras import Algebras
            sage: category = Algebras(QQ).FiniteDimensional().WithBasis()
            sage: T = G.representation(E, on_basis, category=category)
            sage: t = T.an_element(); t
            1 + 2*e0 + 3*e1 + e1*e2
            sage: g * t == t  # indirect doctest
            True
            sage: t * t  # indirect doctest
            1 + 4*e0 + 4*e0*e1*e2 + 6*e1 + 2*e1*e2
        """

class Subrepresentation(Representation_abstract, SubmoduleWithBasis):
    """
    A subrepresentation.

    Let `R` be a representation of an algebraic object `X`. A
    subrepresentation is a submodule of `R` that is closed under
    the action of `X`.
    """
    __classcall_private__: Incomplete
    def __init__(self, basis, support_order, ambient, *args, **opts) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(4)
            sage: R = G.regular_representation(QQ)
            sage: S = R.subrepresentation([sum(R.basis())])
            sage: TestSuite(S).run()
        """
    class Element(SubmoduleWithBasis.Element): ...

class QuotientRepresentation(Representation_abstract, QuotientModuleWithBasis):
    """
    The quotient of a representation by another representation, which
    admits a natural structure of a representation.
    """
    __classcall_private__: Incomplete
    def __init__(self, *args, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(4)
            sage: R = G.regular_representation(QQ)
            sage: S = R.subrepresentation([sum(R.basis())], is_closed=True)
            sage: Q = R.quotient_representation(S)
            sage: TestSuite(Q).run()
        """
    Element = Subrepresentation.Element

class Representation_Tensor(Representation_abstract, CombinatorialFreeModule_Tensor):
    """
    Tensor product of representations.
    """
    @staticmethod
    def __classcall_private__(cls, reps, **options):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S3 = SymmetricGroup(3)
            sage: L = S3.regular_representation(side='left')
            sage: S = S3.sign_representation()
            sage: R = S3.regular_representation(side='right')
            sage: tensor([tensor([L, S]), R]) == tensor([L, S, R])
            True
            sage: tensor([L, tensor([S, R])]) == tensor([L, S, R])
            True

        Check that the tensor product with more general modules
        can be constructed::

            sage: C = CombinatorialFreeModule(ZZ, ['a','b'])
            sage: T = tensor([C, R])
            sage: type(T)
            <class 'sage.combinat.free_module.CombinatorialFreeModule_Tensor_with_category'>
            sage: T = tensor([R, C])
            sage: type(T)
            <class 'sage.combinat.free_module.CombinatorialFreeModule_Tensor_with_category'>
        """
    def __init__(self, reps, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.Alternating(5)
            sage: L = G.regular_representation(side='left')
            sage: S = G.sign_representation()
            sage: T = tensor([L, S, L])
            sage: TestSuite(T).run()
        """
    class Element(Representation_abstract.Element): ...

class Representation_Exterior(Representation_abstract, CombinatorialFreeModule):
    """
    The exterior power representation (in a fixed degree).
    """
    def __init__(self, rep, degree=None, category=None, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.matrix.GL(3, 2)
            sage: R = G.regular_representation(side='right')
            sage: E2 = R.exterior_power(2)
            sage: E2.category()
            Category of finite dimensional modules with basis over Integer Ring
            sage: TestSuite(E2).run()

            sage: G = groups.matrix.GL(2, 3)
            sage: L = G.regular_representation(side='left')
            sage: E48 = L.exterior_power(48)
            sage: TestSuite(E48).run()

            sage: L.exterior_power(-2)
            Traceback (most recent call last):
            ...
            ValueError: the degree must be an integer in [0, 48]
            sage: L.exterior_power(120)
            Traceback (most recent call last):
            ...
            ValueError: the degree must be an integer in [0, 48]
            sage: L.exterior_power(5/6)
            Traceback (most recent call last):
            ...
            ValueError: the degree must be an integer in [0, 48]
        """

class Representation_ExteriorAlgebra(Representation_Exterior):
    """
    The exterior algebra representation.
    """
    def __init__(self, rep, degree=None, category=None, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.matrix.GL(3, 2)
            sage: R = G.regular_representation(side='right')
            sage: E0 = R.exterior_power(0)
            sage: E0.category()
            Category of finite dimensional algebras with basis over Integer Ring
            sage: TestSuite(E0).run()

            sage: G = groups.matrix.GL(2, 3)
            sage: L = G.regular_representation(side='left')
            sage: E = L.exterior_power()
            sage: E.category()
            Category of finite dimensional algebras with basis over Integer Ring
            sage: TestSuite(E).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis element indexing `1` in ``self`` if it exists.

        EXAMPLES::

            sage: S3 = SymmetricGroup(3)
            sage: L = S3.regular_representation(side='left')
            sage: E = L.exterior_power()
            sage: E.one_basis()
            0
            sage: E0 = L.exterior_power(0)
            sage: E0.one_basis()
            0
        """
    def product_on_basis(self, x, y):
        """
        Return the product of basis elements indexed by ``x`` and ``y``.

        EXAMPLES::

            sage: S3 = SymmetricGroup(3)
            sage: L = S3.regular_representation(side='left')
            sage: E = L.exterior_power()
            sage: B = list(E.basis())
            sage: B[:7]
            [1, (), (1,3,2), (1,2,3), (2,3), (1,3), (1,2)]
            sage: B[2] * B[4]  # indirect doctest
            (1,3,2)*(2,3)
        """

class Representation_Symmetric(Representation_abstract, CombinatorialFreeModule):
    """
    The symmetric power representation in a fixed degree.
    """
    def __init__(self, rep, degree, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.matrix.GL(3, 2)
            sage: R = G.regular_representation(side='right')
            sage: S2 = R.symmetric_power(2)
            sage: TestSuite(S2).run()
            sage: S0 = R.symmetric_power(0)
            sage: TestSuite(S2).run()

            sage: R.symmetric_power(-2)
            Traceback (most recent call last):
            ...
            ValueError: the degree must be a nonnegative integer
            sage: R.symmetric_power(3/2)
            Traceback (most recent call last):
            ...
            ValueError: the degree must be a nonnegative integer
        """

class RegularRepresentation(Representation):
    """
    The regular representation of a semigroup.

    The left regular representation of a semigroup `S` over a commutative
    ring `R` is the semigroup ring `R[S]` equipped with the left
    `S`-action `x b_y = b_{xy}`, where `(b_z)_{z \\in S}` is the natural
    basis of `R[S]` and `x,y \\in S`.

    INPUT:

    - ``semigroup`` -- a semigroup
    - ``base_ring`` -- the base ring for the representation
    - ``side`` -- (default: ``'left'``) whether this is a
      ``'left'`` or ``'right'`` representation

    REFERENCES:

    - :wikipedia:`Regular_representation`
    """
    def __init__(self, semigroup, base_ring, side: str = 'left') -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(4)
            sage: R = G.regular_representation()
            sage: TestSuite(R).run()
        """

class TrivialRepresentation(Representation_abstract, CombinatorialFreeModule):
    """
    The trivial representation of a semigroup.

    The trivial representation of a semigroup `S` over a commutative ring
    `R` is the `1`-dimensional `R`-module on which every element of `S`
    acts by the identity.

    This is simultaneously a left and right representation.

    INPUT:

    - ``semigroup`` -- a semigroup
    - ``base_ring`` -- the base ring for the representation

    REFERENCES:

    - :wikipedia:`Trivial_representation`
    """
    def __init__(self, semigroup, base_ring) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.PGL(2, 3)
            sage: V = G.trivial_representation()
            sage: TestSuite(V).run()
        """
    class Element(Representation_abstract.Element): ...

class SignRepresentation_abstract(Representation_abstract, CombinatorialFreeModule):
    """
    Generic implementation of a sign representation.

    The sign representation of a semigroup `S` over a commutative ring
    `R` is the `1`-dimensional `R`-module on which every element of `S`
    acts by `1` if order of element is even (including 0) or `-1` if
    order of element if odd.

    This is simultaneously a left and right representation.

    INPUT:

    - ``permgroup`` -- a permgroup
    - ``base_ring`` -- the base ring for the representation
    - ``sign_function`` -- a function which returns `1` or `-1` depending
      on the elements sign

    REFERENCES:

    - :wikipedia:`Representation_theory_of_the_symmetric_group`
    """
    sign_function: Incomplete
    def __init__(self, group, base_ring, sign_function=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.permutation.PGL(2, 3)
            sage: V = G.sign_representation()
            sage: TestSuite(V).run()
        """

class SignRepresentationPermgroup(SignRepresentation_abstract):
    """
    The sign representation for a permutation group.

    EXAMPLES::

        sage: G = groups.permutation.PGL(2, 3)
        sage: V = G.sign_representation()
        sage: TestSuite(V).run()
    """
class SignRepresentationMatrixGroup(SignRepresentation_abstract):
    """
    The sign representation for a matrix group.

    EXAMPLES::

        sage: G = groups.permutation.PGL(2, 3)
        sage: V = G.sign_representation()
        sage: TestSuite(V).run()
    """
class SignRepresentationCoxeterGroup(SignRepresentation_abstract):
    '''
    The sign representation for a Coxeter group.

    EXAMPLES::

        sage: G = WeylGroup(["A", 1, 1])
        sage: V = G.sign_representation()
        sage: TestSuite(V).run()

        sage: # optional - gap3
        sage: W = CoxeterGroup([\'B\', 3], implementation="coxeter3")
        sage: S = W.sign_representation()
        sage: TestSuite(S).run()
    '''

class ReflectionRepresentation(Representation_abstract, CombinatorialFreeModule):
    """
    The reflection representation of a Coxeter group.

    This is the canonical faithful representation of a Coxeter group.

    EXAMPLES::

        sage: W = CoxeterGroup(['B', 4])
        sage: R = W.reflection_representation()
        sage: all(g.matrix() == R.representation_matrix(g) for g in W)
        True
    """
    @staticmethod
    def __classcall_private__(cls, W, base_ring=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: W = CoxeterGroup(['D', 4])
            sage: R1 = W.reflection_representation()
            sage: R2 = W.reflection_representation(ZZ)
            sage: R1 is R2
            True
        """
    def __init__(self, W, base_ring) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: W = CoxeterGroup(['C', 3])
            sage: R = W.reflection_representation()
            sage: TestSuite(R).run()

            sage: W = CoxeterGroup(['E', 6, 1])
            sage: R = W.reflection_representation()
            sage: TestSuite(R).run()
        """

class NaturalMatrixRepresentation(Representation):
    """
    The natural representation of a matrix semigroup.

    A matrix semigroup is defined by its representation on a (finite
    dimensional) vector space `V`, which is called the *natural
    representation*.

    INPUT:

    - ``matrix_semigroup`` -- a matrix semigroup
    - ``base_ring`` -- (optional) the base ring; the default is the base ring
      of the semigroup
    """
    @staticmethod
    def __classcall_private__(cls, semigroup, base_ring=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: G = groups.matrix.SO(5, 2)
            sage: N1 = G.natural_representation()
            sage: N2 = G.natural_representation(GF(2))
            sage: N1 is N2
            True
        """
    def __init__(self, semigroup, base_ring) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = groups.matrix.SU(2, 2)
            sage: N = G.natural_representation()
            sage: TestSuite(N).run()

            sage: G = groups.matrix.Sp(4, 2)
            sage: N = G.natural_representation()
            sage: TestSuite(N).run()  # long time
        """

class SchurFunctorRepresentation(Subrepresentation):
    """
    The representation constructed by the Schur functor.

    Let `G` be a semigroup and let `V` be a representation of `G`. The
    *Schur functor* for a partition `\\lambda` of size `k` is the functor
    `\\mathbb{S}_{\\lambda}` that sends `V` to the `G`-subrepresentation of
    `V^{\\otimes k}` spanned by `(v_1 \\otimes \\cdots \\otimes v_k) c_{\\lambda}`,
    where `c_{\\lambda}` is the :meth:`Young symmetrizer
    <sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra.young_symmetrizer>`
    corresponding to `\\lambda`. When `G = GL_n(F)`, the Schur functor image
    `\\mathbb{S}_{\\lambda} F^n` is the (irreducible when `F` has characteristic
    `0`) highest representation of shape `\\lambda`.

    EXAMPLES::

        sage: G = groups.permutation.Dihedral(3)
        sage: V = G.regular_representation()
        sage: S21V = V.schur_functor([2, 1])
        sage: S21V.dimension()
        70
        sage: SemistandardTableaux([2,1], max_entry=V.dimension()).cardinality()
        70
        sage: chi = G.character([S21V.representation_matrix(g).trace()
        ....:                    for g in G.conjugacy_classes_representatives()])
        sage: chi.values()
        [70, 0, -2]
        sage: G.character_table()
        [ 1 -1  1]
        [ 2  0 -1]
        [ 1  1  1]
        sage: for m, phi in chi.decompose():
        ....:     print(m, phi.values())
        11 [1, -1, 1]
        11 [1, 1, 1]
        24 [2, 0, -1]

        sage: # long time
        sage: S211V = V.schur_functor([2, 1, 1])
        sage: S211V.dimension()
        105
        sage: SemistandardTableaux([2, 1, 1], max_entry=V.dimension()).cardinality()
        105
        sage: chi = G.character([S211V.representation_matrix(g).trace()
        ....:                    for g in G.conjugacy_classes_representatives()])
        sage: chi.values()
        [105, -3, 0]
        sage: for m, phi in chi.decompose():
        ....:     print(m, phi.values())
        19 [1, -1, 1]
        16 [1, 1, 1]
        35 [2, 0, -1]

    An example with the cyclic group::

        sage: C3 = groups.permutation.Cyclic(3)
        sage: V3 = C3.regular_representation()
        sage: S31V3 = V3.schur_functor([3, 1])
        sage: S31V3.dimension()
        15
        sage: chi = C3.character([S31V3.representation_matrix(g).trace()
        ....:                     for g in C3.conjugacy_classes_representatives()])
        sage: chi.values()
        [15, 0, 0]
        sage: C3.character_table()
        [         1          1          1]
        [         1      zeta3 -zeta3 - 1]
        [         1 -zeta3 - 1      zeta3]
        sage: for m, phi in chi.decompose():
        ....:     print(m, phi.values())
        5 [1, 1, 1]
        5 [1, -zeta3 - 1, zeta3]
        5 [1, zeta3, -zeta3 - 1]

    An example of `GL_3(\\GF{2})`::

        sage: G = groups.matrix.GL(3, 2)
        sage: from sage.modules.with_basis.representation import Representation
        sage: N = G.natural_representation()
        sage: S21N = N.schur_functor([2, 1])
        sage: S21N.dimension()
        8

    An example with the Weyl/Coxeter group of type `C_3`::

        sage: G = WeylGroup(['C', 3], prefix='s')
        sage: R = G.reflection_representation()
        sage: S = R.schur_functor([3, 2, 1])
        sage: g = G.an_element(); g
        s1*s2*s3
        sage: v = S.an_element(); v
        2*S[0] + 2*S[1] + 3*S[2]
        sage: v * g
        -(2*a+1)*S[0] - (a+2)*S[1] - (2*a-2)*S[2] + (2*a-2)*S[3]
         - (-2*a+4)*S[4] + (-2*a+4)*S[5] + 2*S[6] + 2*a*S[7]
        sage: g * v
        3*S[0] + (-2*a+5)*S[2] + 3*a*S[4] - (5*a-2)*S[6] - 6*S[7]
    """
    @staticmethod
    def __classcall_private__(cls, V, shape):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.modules.with_basis.representation import SchurFunctorRepresentation
            sage: G = groups.permutation.Cyclic(3)
            sage: V = G.regular_representation()
            sage: S1 = SchurFunctorRepresentation(V, Partition([2, 1, 1]))
            sage: S2 = SchurFunctorRepresentation(V, (2, 1, 1))
            sage: S1 is S2
            True
        """
    def __init__(self, V, shape) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``V`` -- a representation
        - ``shape`` -- a partition

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(3)
            sage: V = G.regular_representation()
            sage: S = V.schur_functor([2, 1])
            sage: TestSuite(S).run()

            sage: G = CoxeterGroup(['B', 3])
            sage: R = G.reflection_representation()
            sage: S = R.schur_functor([3, 2, 1])
            sage: TestSuite(S).run()

            sage: G = groups.matrix.GL(3, 2)
            sage: N = G.natural_representation()
            sage: S = N.schur_functor([2, 1])
            sage: TestSuite(S).run()
        """
    Element = Subrepresentation.Element
