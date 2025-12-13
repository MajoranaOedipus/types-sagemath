from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.combinat.diagram import Diagram as Diagram
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modules.with_basis.representation import Representation_abstract as Representation_abstract
from sage.modules.with_basis.subquotient import QuotientModuleWithBasis as QuotientModuleWithBasis, SubmoduleWithBasis as SubmoduleWithBasis
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family

class SymmetricGroupRepresentation(Representation_abstract):
    """
    Mixin class for symmetric group (algebra) representations.
    """
    def __init__(self, SGA) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SM = Partition([3,1,1]).specht_module(GF(3))
            sage: SM.side()
            'left'
            sage: TestSuite(SM).run()
        """
    @cached_method
    def frobenius_image(self):
        """
        Return the Frobenius image of ``self``.

        The Frobenius map is defined as the map to symmetric functions

        .. MATH::

            F(\\chi) = \\frac{1}{n!} \\sum_{w \\in S_n} \\chi(w) p_{\\rho(w)},

        where `\\chi` is the character of the `S_n`-module ``self``,
        `p_{\\lambda}` is the powersum symmetric function basis element
        indexed by `\\lambda`, and `\\rho(w)` is the cycle type of `w` as a
        partition. Specifically, this map takes irreducible representations
        indexed by `\\lambda` to the Schur function `s_{\\lambda}`.

        EXAMPLES::

            sage: SM = Partition([2,2,1]).specht_module(QQ)
            sage: SM.frobenius_image()
            s[2, 2, 1]
            sage: SM = Partition([4,1]).specht_module(CyclotomicField(5))
            sage: SM.frobenius_image()
            s[4, 1]

        We verify the regular representation::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,0), (1,1), (2,2), (3,3), (4,4)])
            sage: F = D.specht_module(QQ).frobenius_image(); F
            s[1, 1, 1, 1, 1] + 4*s[2, 1, 1, 1] + 5*s[2, 2, 1]
             + 6*s[3, 1, 1] + 5*s[3, 2] + 4*s[4, 1] + s[5]
            sage: s = SymmetricFunctions(QQ).s()
            sage: F == sum(StandardTableaux(la).cardinality() * s[la]
            ....:          for la in Partitions(5))
            True
            sage: all(s[la] == la.specht_module(QQ).frobenius_image()
            ....:     for n in range(1, 5) for la in Partitions(n))
            True

            sage: D = Diagram([(0,0), (1,1), (1,2), (2,3), (2,4)])
            sage: SM = D.specht_module(QQ)
            sage: SM.frobenius_image()
            s[2, 2, 1] + s[3, 1, 1] + 2*s[3, 2] + 2*s[4, 1] + s[5]

        An example using the tabloid module::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM = SGA.tabloid_module([2, 2, 1])
            sage: TM.frobenius_image()
            s[2, 2, 1] + s[3, 1, 1] + 2*s[3, 2] + 2*s[4, 1] + s[5]
        """

class SpechtModule(SymmetricGroupRepresentation, SubmoduleWithBasis):
    """
    A Specht module.

    Let `S_n` be the symmetric group on `n` letters and `R` be a commutative
    ring. The *Specht module* `S^D` for a diagram `D` is an `S_n`-module
    defined as follows. Let

    .. MATH::

        R(D) := \\sum_{w \\in R_D} w,
        \\qquad\\qquad
        C(D) := \\sum_{w \\in C_D} (-1)^w w,

    where `R_D` (resp. `C_D`) is the row (resp. column) stabilizer of `D`.
    Then, we construct the Specht module `S^D` as the left ideal

    .. MATH::

        S^D = R[S_n] C(D) R(D),

    where `R[S_n]` is the group algebra of `S_n` over `R`.

    INPUT:

    - ``SGA`` -- a symmetric group algebra
    - ``D`` -- a diagram

    EXAMPLES:

    We begin by constructing all irreducible Specht modules for the symmetric
    group `S_4` and show that they give a full set of irreducible
    representations both by having distinct Frobenius characters and the
    sum of the square of their dimensions is equal to `4!`::

        sage: SP = [la.specht_module(QQ) for la in Partitions(4)]
        sage: s = SymmetricFunctions(QQ).s()
        sage: [s(S.frobenius_image()) for S in SP]
        [s[4], s[3, 1], s[2, 2], s[2, 1, 1], s[1, 1, 1, 1]]
        sage: sum(S.dimension()^2 for S in SP)
        24

    Next, we compute the Specht module for a more general diagram
    for `S_5` and compute its irreducible decomposition by using
    its Frobenius character::

        sage: D = [(0,0), (0,1), (1,1), (1,2), (0,3)]
        sage: SGA = SymmetricGroupAlgebra(QQ, 5)
        sage: SM = SGA.specht_module(D)
        sage: SM.dimension()
        9
        sage: s(SM.frobenius_image())
        s[3, 2] + s[4, 1]

    This carries a natural (left) action of the symmetric group (algebra)::

        sage: S5 = SGA.group()
        sage: v = SM.an_element(); v
        2*S[0] + 2*S[1] + 3*S[2]
        sage: S5([2,1,5,3,4]) * v
        3*S[0] + 2*S[1] + 2*S[2]
        sage: x = SGA.an_element(); x
        [1, 2, 3, 4, 5] + 2*[1, 2, 3, 5, 4] + 3*[1, 2, 4, 3, 5] + [5, 1, 2, 3, 4]
        sage: x * v
        15*S[0] + 14*S[1] + 16*S[2] - 7*S[5] + 2*S[6] + 2*S[7]

    .. SEEALSO::

        :class:`~sage.combinat.symmetric_group_representations.SpechtRepresentation`
        for an implementation of the representation by matrices.
    """
    @staticmethod
    def __classcall_private__(cls, SGA, D):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.combinat.specht_module import SpechtModule
            sage: from sage.combinat.diagram import Diagram
            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: D = [(0,0), (1,1), (1,2)]
            sage: SM1 = SpechtModule(SGA, D)
            sage: SM2 = SpechtModule(SGA, Diagram(D))
            sage: SM1 is SM2
            True
            sage: SM1 is SpechtModule(SGA, [[1,1], [1,2], [0,0]])
            True

            sage: SpechtModule(SGA, [[0,0], [1,1]])
            Traceback (most recent call last):
            ...
            ValueError: the domain size (=3) does not match the number of boxes (=2) of the diagram
        """
    def __init__(self, SGA, D) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: SM = SGA.specht_module([(0,0), (1,1), (1,2), (2,1)])
            sage: TestSuite(SM).run()
        """
    class Element(SubmoduleWithBasis.Element): ...

class TabloidModule(SymmetricGroupRepresentation, CombinatorialFreeModule):
    """
    The vector space of all tabloids of a fixed shape with the natural
    symmetric group action.

    A *tabloid* is an :class:`OrderedSetPartition` whose underlying set
    is `\\{1, \\ldots, n\\}`. The symmetric group acts by permuting the
    entries of the set. Hence, this is a representation of the symmetric
    group defined over any field.

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
        sage: TM = SGA.tabloid_module([2, 2, 1])
        sage: TM.dimension()
        30
        sage: TM.brauer_character()
        (30, 6, 2, 0, 0)
        sage: IM = TM.invariant_module()
        sage: IM.dimension()
        1
        sage: IM.basis()[0].lift() == sum(TM.basis())
        True
    """
    @staticmethod
    def __classcall_private__(cls, SGA, shape):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.combinat.specht_module import TabloidModule
            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM1 = TabloidModule(SGA, [2, 2, 1])
            sage: TM2 = TabloidModule(SGA, Partition([2, 2, 1]))
            sage: TM1 is TM2
            True

            sage: TabloidModule(SGA, [3, 2, 1])
            Traceback (most recent call last):
            ...
            ValueError: the domain size (=5) does not match the number of boxes (=6) of the diagram
        """
    def __init__(self, SGA, shape) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM = SGA.tabloid_module([2,2,1])
            sage: TestSuite(TM).run()
        """
    def specht_module(self):
        """
        Return the Specht submodule of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM = SGA.tabloid_module([2,2,1])
            sage: TM.specht_module() is SGA.specht_module([2,2,1])
            True
        """
    def bilinear_form(self, u, v):
        """
        Return the natural bilinear form of ``self`` applied to ``u`` and ``v``.

        The natural bilinear form is given by defining the tabloid basis
        to be orthonormal.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM = SGA.tabloid_module([2,2,1])
            sage: u = TM.an_element(); u
            2*T[{1, 2}, {3, 4}, {5}] + 2*T[{1, 2}, {3, 5}, {4}] + 3*T[{1, 2}, {4, 5}, {3}]
            sage: v = sum(TM.basis())
            sage: TM.bilinear_form(u, v)
            7
            sage: TM.bilinear_form(u, TM.zero())
            0
        """
    class Element(CombinatorialFreeModule.Element): ...

class SpechtModuleTableauxBasis(SpechtModule):
    """
    A Specht module of a partition in the classical standard
    tableau basis.

    This is constructed as a `S_n`-submodule of the :class:`TabloidModule`
    (also referred to as the standard module).

    .. SEEALSO::

        - :class:`SpechtModule` for the generic diagram implementation
          constructed as a left ideal of the group algebra
        - :class:`~sage.combinat.symmetric_group_representations.SpechtRepresentation`
          for an implementation of the representation by matrices.
    """
    def __init__(self, ambient) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([2,2,1])
            sage: TestSuite(SM).run()
        """
    @lazy_attribute
    def lift(self):
        """
        The lift (embedding) map from ``self`` to the ambient space.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([3, 1, 1])
            sage: SM.lift
            Generic morphism:
              From: Specht module of [3, 1, 1] over Rational Field
              To:   Tabloid module of [3, 1, 1] over Rational Field
        """
    @lazy_attribute
    def retract(self):
        """
        The retract map from the ambient space.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: X = SGA.tabloid_module([2,2,1])
            sage: Y = X.specht_module()
            sage: Y.retract
            Generic morphism:
              From: Tabloid module of [2, 2, 1] over Rational Field
              To:   Specht module of [2, 2, 1] over Rational Field
            sage: all(Y.retract(u.lift()) == u for u in Y.basis())
            True

            sage: Y.retract(X.zero())
            0
            sage: Y.retract(sum(X.basis()))
            Traceback (most recent call last):
            ...
            ValueError: ... is not in the image
        """
    def bilinear_form(self, u, v):
        """
        Return the natural bilinear form of ``self`` applied to ``u`` and ``v``.

        The natural bilinear form is given by the pullback of the natural
        bilinear form on the tabloid module (where the tabloid basis is an
        orthonormal basis).

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([2,2,1])
            sage: u = SM.an_element(); u
            3*S[[1, 2], [3, 5], [4]] + 2*S[[1, 3], [2, 5], [4]] + 2*S[[1, 4], [2, 5], [3]]
            sage: v = sum(SM.basis())
            sage: SM.bilinear_form(u, v)
            140
        """
    @cached_method
    def gram_matrix(self):
        """
        Return the Gram matrix of the natural bilinear form of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([2,2,1])
            sage: M = SM.gram_matrix(); M
            [12  4 -4 -4  4]
            [ 4 12  4  4  4]
            [-4  4 12  4  4]
            [-4  4  4 12  4]
            [ 4  4  4  4 12]
            sage: M.det() != 0
            True
        """
    def maximal_submodule(self):
        """
        Return the maximal submodule of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: SM = SGA.specht_module([3,2])
            sage: U = SM.maximal_submodule()
            sage: U.dimension()
            4
        """
    def simple_module(self):
        """
        Return the simple (or irreducible) `S_n`-submodule of ``self``.

        .. SEEALSO::

            :class:`~sage.combinat.specht_module.SimpleModule`

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: SM = SGA.specht_module([3,2])
            sage: L = SM.simple_module()
            sage: L.dimension()
            1

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([3,2])
            sage: SM.simple_module() is SM
            True
        """
    def intrinsic_arrangement(self, base_ring=None):
        """
        Return the intrinsic arrangement of ``self``.

        Consider the Specht module `S^{\\lambda}` with `\\lambda` a
        (integer) partition of `n` (i.e., `S^{\\lambda}` is an `S_n`-module).
        The *intrinsic arrangement* of `S^{\\lambda}` is the central hyperplane
        arrangement in `S^{\\lambda}` given by the hyperplanes `H_{\\alpha}`,
        indexed by a set partition `\\alpha` of `\\{1, \\ldots, n\\}` of size
        `\\lambda`, defined by

        .. MATH::

            H_{\\alpha} := \\bigoplus_{\\tau \\in T_{\\alpha}} (S^{\\lambda})^{\\tau},

        where `T_{\\alpha}` is some set of generating transpositions
        of the Young subgroup `S_{\\alpha}` and `V^{\\tau}` denotes the
        `\\tau`-invariant subspace of `V`. (These hyperplanes do not
        depend on the choice of `T_{\\alpha}`.)

        This was introduced in [TVY2020]_ as a generalization of the
        braid arrangement, which is the case when `\\lambda = (n-1, 1)`
        (equivalently, for the irreducible representation of `S_n`
        given by the type `A_{n-1}` root system).

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: SM = SGA.specht_module([2, 1, 1])
            sage: A = SM.intrinsic_arrangement()
            sage: A.hyperplanes()
            (Hyperplane T0 - T1 - 3*T2 + 0,
             Hyperplane T0 - T1 + T2 + 0,
             Hyperplane T0 + 3*T1 + T2 + 0,
             Hyperplane 3*T0 + T1 - T2 + 0)
            sage: A.is_free()
            False

        We reproduce Example 3 of [TVY2020]_::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: for la in Partitions(5):
            ....:     SM = SGA.specht_module(la)
            ....:     A = SM.intrinsic_arrangement()
            ....:     print(la, A.characteristic_polynomial())
            [5] 1
            [4, 1] x^4 - 10*x^3 + 35*x^2 - 50*x + 24
            [3, 2] x^5 - 15*x^4 + 90*x^3 - 260*x^2 + 350*x - 166
            [3, 1, 1] x^6 - 10*x^5 + 45*x^4 - 115*x^3 + 175*x^2 - 147*x + 51
            [2, 2, 1] x^5 - 10*x^4 + 45*x^3 - 105*x^2 + 120*x - 51
            [2, 1, 1, 1] x^4 - 5*x^3 + 10*x^2 - 10*x + 4
            [1, 1, 1, 1, 1] 1

            sage: A = SGA.specht_module([4, 1]).intrinsic_arrangement()
            sage: A.characteristic_polynomial().factor()
            (x - 4) * (x - 3) * (x - 2) * (x - 1)
        """

class MaximalSpechtSubmodule(SymmetricGroupRepresentation, SubmoduleWithBasis):
    """
    The maximal submodule `U^{\\lambda}` of the Specht module `S^{\\lambda}`.

    ALGORITHM:

    We construct `U^{\\lambda}` as the intersection `S \\cap S^{\\perp}`,
    where `S^{\\perp}` is the orthogonal complement of the Specht module `S`
    inside of the tabloid module `T` (with respect to the natural
    bilinear form on `T`).

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
        sage: SM = SGA.specht_module([3,2])
        sage: U = SM.maximal_submodule()
        sage: u = U.an_element(); u
        2*U[0] + 2*U[1]
        sage: [p * u for p in list(SGA.basis())[:4]]
        [2*U[0] + 2*U[1], 2*U[2] + 2*U[3], 2*U[0] + 2*U[1], U[0] + 2*U[2]]
        sage: sum(SGA.basis()) * u
        0
    """
    def __init__(self, specht_module) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: SM = SGA.specht_module([3,2])
            sage: U = SM.maximal_submodule()
            sage: TestSuite(U).run()

            sage: SM = SGA.specht_module([2,1,1,1])
            sage: SM.maximal_submodule().dimension() == SM.dimension()
            True

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module([3,2])
            sage: U = SM.maximal_submodule()
            sage: TestSuite(U).run()
            sage: U.dimension()
            0
        """
    Element = SpechtModule.Element

class SimpleModule(SymmetricGroupRepresentation, QuotientModuleWithBasis):
    """
    The simple `S_n`-module associated with a partition `\\lambda`.

    The simple module `D^{\\lambda}` is the quotient of the Specht module
    `S^{\\lambda}` by its :class:`maximal submodule <MaximalSpechtSubmodule>`
    `U^{\\lambda}`.

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
        sage: SM = SGA.specht_module([3,1,1])
        sage: D = SM.simple_module()
        sage: v = D.an_element(); v
        2*D[[[1, 3, 5], [2], [4]]] + 2*D[[[1, 4, 5], [2], [3]]]
        sage: SGA.an_element() * v
        2*D[[[1, 2, 4], [3], [5]]] + 2*D[[[1, 3, 5], [2], [4]]]

    We give an example on how to construct the decomposition matrix
    (the Specht modules are a complete set of irreducible projective
    modules) and the Cartan matrix of a symmetric group algebra::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
        sage: BM = matrix(SGA.simple_module(la).brauer_character()
        ....:             for la in Partitions(4, regular=3))
        sage: SBT = matrix(SGA.specht_module(la).brauer_character()
        ....:              for la in Partitions(4))
        sage: D = SBT * ~BM; D
        [1 0 0 0]
        [0 1 0 0]
        [1 0 1 0]
        [0 0 0 1]
        [0 0 1 0]
        sage: D.transpose() * D
        [2 0 1 0]
        [0 1 0 0]
        [1 0 2 0]
        [0 0 0 1]

    We verify this against the direct computation (up to reindexing the
    rows and columns)::

        sage: SGA.cartan_invariants_matrix()  # long time
        [1 0 0 0]
        [0 1 0 0]
        [0 0 2 1]
        [0 0 1 2]
    """
    def __init__(self, specht_module) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: SM = SGA.specht_module([3,1,1])
            sage: D = SM.simple_module()
            sage: TestSuite(D).run()

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: SM = SGA.specht_module([2,1,1,1])
            sage: SM.simple_module()
            Traceback (most recent call last):
            ...
            ValueError: the partition must be 3-regular
        """
    Element = SpechtModule.Element

def specht_module_spanning_set(D, SGA=None):
    """
    Return a spanning set of the Specht module of diagram ``D``.

    INPUT:

    - ``D`` -- list of cells ``(r,c)`` for row ``r`` and column ``c``
    - ``SGA`` -- (optional) a symmetric group algebra

    EXAMPLES::

        sage: from sage.combinat.specht_module import specht_module_spanning_set
        sage: specht_module_spanning_set([(0,0), (1,1), (2,2)])
        ([1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1])
        sage: specht_module_spanning_set([(0,0), (1,1), (2,1)])
        ([1, 2, 3] - [1, 3, 2], -[1, 2, 3] + [1, 3, 2], [2, 1, 3] - [3, 1, 2],
         [2, 3, 1] - [3, 2, 1], -[2, 1, 3] + [3, 1, 2], -[2, 3, 1] + [3, 2, 1])

        sage: SGA = SymmetricGroup(3).algebra(QQ)
        sage: specht_module_spanning_set([(0,0), (1,1), (2,1)], SGA)
        (() - (2,3), -(1,2) + (1,3,2), (1,2,3) - (1,3),
         -() + (2,3), -(1,2,3) + (1,3), (1,2) - (1,3,2))

    TESTS:

    Verify that diagrams bigger than the rank work::

        sage: specht_module_spanning_set([(0,0), (3,5)])
        ([1, 2], [2, 1])
        sage: specht_module_spanning_set([(0,0), (5,3)])
        ([1, 2], [2, 1])
    """
def specht_module_rank(D, base_ring=None):
    """
    Return the rank of the Specht module of diagram ``D``.

    EXAMPLES::

        sage: from sage.combinat.specht_module import specht_module_rank
        sage: specht_module_rank([(0,0), (1,1), (2,2)])
        6
    """
def polytabloid(T):
    """
    Compute the polytabloid element associated to a tableau ``T``.

    For a tableau `T`, the polytabloid associated to `T` is

    .. MATH::

        e_T = \\sum_{\\sigma \\in C_T} (-1)^{\\sigma} \\{\\sigma T\\},

    where `\\{\\}` is the row-equivalence class, i.e. a tabloid,
    and `C_T` is the column stabilizer of `T`. The sum takes place in
    the module spanned by tabloids `\\{T\\}`.

    OUTPUT:

    A ``dict`` whose keys are tabloids represented by tuples of frozensets
    and whose values are the coefficient.

    EXAMPLES::

        sage: from sage.combinat.specht_module import polytabloid
        sage: T = StandardTableau([[1,3,4],[2,5]])
        sage: polytabloid(T)
        {(frozenset({1, 3, 4}), frozenset({2, 5})): 1,
         (frozenset({1, 4, 5}), frozenset({2, 3})): -1,
         (frozenset({2, 3, 4}), frozenset({1, 5})): -1,
         (frozenset({2, 4, 5}), frozenset({1, 3})): 1}
    """
def tabloid_gram_matrix(la, base_ring):
    """
    Compute the Gram matrix of the bilinear form of a Specht module
    pulled back from the tabloid module.

    For the module spanned by all tabloids, we define an bilinear form
    by having the tabloids be an orthonormal basis. We then pull this
    bilinear form back across the natural injection of the Specht module
    into the tabloid module.

    EXAMPLES::

        sage: from sage.combinat.specht_module import tabloid_gram_matrix
        sage: tabloid_gram_matrix([3,2], GF(5))
        [4 2 2 1 4]
        [2 4 1 2 1]
        [2 1 4 2 1]
        [1 2 2 4 2]
        [4 1 1 2 4]
    """
def simple_module_rank(la, base_ring):
    """
    Return the rank of the simple `S_n`-module corresponding to the
    partition ``la`` of size `n` over ``base_ring``.

    EXAMPLES::

        sage: from sage.combinat.specht_module import simple_module_rank
        sage: simple_module_rank([3,2,1,1], GF(3))
        13

    TESTS::

        sage: from sage.combinat.specht_module import simple_module_rank
        sage: simple_module_rank([1,1,1,1], GF(3))
        Traceback (most recent call last):
        ...
        ValueError: the partition [1, 1, 1, 1] is not 3-regular

        sage: from sage.combinat.specht_module import simple_module_rank
        sage: simple_module_rank([2,1], GF(3)['x'])
        Traceback (most recent call last):
        ...
        NotImplementedError: the base must be a field
    """
