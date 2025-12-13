from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import divisors as divisors
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.modules import Modules as Modules
from sage.categories.monoids import Monoids as Monoids
from sage.categories.sets_cat import cartesian_product as cartesian_product
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.categories.tensor import tensor as tensor
from sage.combinat.cyclic_sieving_phenomenon import orbit_decomposition as orbit_decomposition
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.set_partition_ordered import OrderedSetPartitions as OrderedSetPartitions
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.groups.perm_gps.constructor import PermutationGroupElement as PermutationGroupElement
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup, PermutationGroup_generic as PermutationGroup_generic
from sage.groups.perm_gps.permgroup_named import SymmetricGroup as SymmetricGroup
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid, IndexedFreeAbelianMonoidElement as IndexedFreeAbelianMonoidElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import Element as Element, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_GT as op_GT, op_LE as op_LE, op_LT as op_LT, op_NE as op_NE
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation, WithPicklingByInitArgs as WithPicklingByInitArgs

GAP_FAIL: Incomplete

class AtomicSpeciesElement(WithEqualityById, Element, WithPicklingByInitArgs, metaclass=InheritComparisonClasscallMetaclass):
    """
    An atomic species.

    Two atomic species are equal if the underlying groups are
    conjugate, and their domain partitions are equal under the
    conjugating element.

    INPUT:

    - ``dis`` -- a directly indecomposable permutation group
    - ``domain_partition`` -- a `k`-tuple of ``frozenset`` entries,
      where `k` is the arity, representing the assignment of each
      element of the domain of ``dis`` to a sort
    """
    @staticmethod
    def __classcall__(cls, parent, C, dompart):
        '''
        Normalize the input for unique representation.

        INPUT:

        - ``C`` -- a directly indecomposable permutation group
        - ``dompart`` -- a `k`-tuple of iterables, where `k` is the
          arity, representing the assignment of each element of the
          domain of ``dis`` to a sort

        .. WARNING::

            We do not check whether ``C`` is indeed directly
            indecomposable.

        TESTS::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X")
            sage: G = PermutationGroup([(2,3), (1,2,3)])
            sage: A(G)
            E_3
            sage: G = CyclicPermutationGroup(4)
            sage: A(G)
            C_4
            sage: G = PermutationGroup([[(1,2), (3,4)], [(1,4), (2,3)]])
            sage: A(G)
            Pb_4

        Check that the domain is irrelevant::

            sage: A = AtomicSpecies("X, Y")
            sage: G = PermutationGroup([[("a", "b", "c", "d"), ("e", "f")]])
            sage: a = A(G, {0: "abcd", 1: "ef"}); a  # random
            {((1,2,3,4)(5,6),): ({1, 2, 3, 4}, {5, 6})}
            sage: H = PermutationGroup([[(1,2,3,4), (5,6)]])
            sage: a is A(H, {0: [1,2,3,4], 1: [5,6]})
            True

        The advantage of the unique representation is that we can
        rename the species::

            sage: a.rename("CD(X,Y)"); a
            CD(X,Y)

        We create two different atomic species `a` and `b` with the
        same multicardinality and the same underlying permutation
        group::

            sage: G = PermutationGroup([[(1,2),(3,4),(5,6),(7,8,9,10)]]); G
            Permutation Group with generators [(1,2)(3,4)(5,6)(7,8,9,10)]
            sage: H = PermutationGroup([[(1,2,3,4),(5,6),(7,8),(9,10)]]); H
            Permutation Group with generators [(1,2,3,4)(5,6)(7,8)(9,10)]
            sage: a = A(G, {0: [1,2,3,4], 1: [5,6,7,8,9,10]}); a
            {((1,2,3,4)(5,6)(7,8)(9,10),): ({5, 6, 7, 8}, {1, 2, 3, 4, 9, 10})}
            sage: b = A(H, {0: [1,2,3,4], 1: [5,6,7,8,9,10]}); b
            {((1,2,3,4)(5,6)(7,8)(9,10),): ({1, 2, 3, 4}, {5, 6, 7, 8, 9, 10})}
            sage: c = A(G, {0: [1,2,5,6], 1: [3,4,7,8,9,10]}); c
            {((1,2,3,4)(5,6)(7,8)(9,10),): ({5, 6, 7, 8}, {1, 2, 3, 4, 9, 10})}
            sage: a == b
            False
            sage: a is c
            True
        '''
    def __init__(self, parent, dis, domain_partition) -> None:
        '''
        Initialize an atomic species.

        TESTS::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X")
            sage: G = PermutationGroup([[(1,3),(4,7)], [(2,5),(6,8)], [(1,4),(2,5),(3,7)]])
            sage: TestSuite(A(G)).run()

            sage: loads(dumps(A(G))) is A(G)
            True
        '''
    def grade(self):
        '''
        Return the grade of ``self``.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X, Y")
            sage: G = PermutationGroup([[(1,2),(3,4),(5,6),(7,8,9,10)]])
            sage: a = A(G, {0: [1,2,3,4], 1: [5,6,7,8,9,10]})
            sage: a.grade()
            [4, 6]
        '''
    def __lt__(self, other):
        '''
        Return whether ``self`` is less than ``other``.

        ``self`` is less than or equal to ``other`` if it is
        conjugate to a subgroup of ``other`` in the parent group.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X")
            sage: A(DihedralGroup(4)) < A(CyclicPermutationGroup(4))
            True

        We create the poset of atomic species of degree four::

            sage: P = Poset([A.subset(4), lambda b, c: b <= c])
            sage: len(P.cover_relations())
            7
            sage: sorted(P.cover_relations(), key=str)
            [[C_4, E_2(X^2)],
             [E_2(E_2), C_4],
             [E_2(E_2), Pb_4],
             [E_4, E_2(E_2)],
             [E_4, Eo_4],
             [Eo_4, Pb_4],
             [Pb_4, E_2(X^2)]]

        TESTS::

            sage: A = AtomicSpecies("X")
            sage: [(a, b) for a, b in Subsets(A.subset(4), 2) if (a < b) != (b > a)]
            []
            sage: [(a, b) for a, b in Subsets(A.subset(4), 2) if (a <= b) != (b >= a)]
            []
            sage: A = AtomicSpecies("X, Y")
            sage: [(a, b) for a, b in Subsets(A.subset(3), 2) if (a < b) != (b > a)]
            []
        '''
    def __le__(self, other):
        '''
        Return whether ``self`` is less than or equal to ``other``.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X")
            sage: A(SymmetricGroup(3)) <= A(SymmetricGroup(3))
            True
        '''
    def structures(self, *labels) -> Generator[Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        This yields a list of relabelled representatives of the
        cosets of corresponding groups.

        The relabelling is such that the first few labels correspond
        to the first sort, etc.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X, Y")
            sage: G = PermutationGroup([[("a", "b", "c", "d"), ("e", "f")]])
            sage: a = A(G, {0: "abcd", 1: "ef"})
            sage: list(a.structures([1, 2, 3, 4], ["a", "b"]))
            [(1, 2, 3, 4, \'a\', \'b\'),
             (1, 2, 3, 4, \'b\', \'a\'),
             (1, 2, 4, 3, \'a\', \'b\'),
             (1, 2, 4, 3, \'b\', \'a\'),
             (1, 3, 2, 4, \'a\', \'b\'),
             (1, 3, 2, 4, \'b\', \'a\'),
             (1, 3, 4, 2, \'a\', \'b\'),
             (1, 3, 4, 2, \'b\', \'a\'),
             (1, 4, 2, 3, \'a\', \'b\'),
             (1, 4, 2, 3, \'b\', \'a\'),
             (1, 4, 3, 2, \'a\', \'b\'),
             (1, 4, 3, 2, \'b\', \'a\')]

            sage: G = PermutationGroup([[(2,3),(4,5)]], domain=[2,3,4,5])
            sage: a = A(G, {0: [2, 3], 1: [4, 5]})
            sage: list(a.structures([1, 2],["a", "b"]))
            [(1, 2, \'a\', \'b\'), (1, 2, \'b\', \'a\')]
        '''
    def __call__(self, *args):
        '''
        Substitute `M_1,\\ldots, M_k` into ``self``.

        ``self`` must not be a singleton.  The arguments must all
        have the same parent and must all be molecular.  The number
        of arguments must be equal to the arity of ``self``.

        The result is an atomic species, whose parent has the
        same variable names as the arguments.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies, MolecularSpecies
            sage: A = AtomicSpecies("X")
            sage: M = MolecularSpecies("X")
            sage: Xmol = M(SymmetricGroup(1))
            sage: E2atom = M(SymmetricGroup(2))
            sage: E2mol = M(SymmetricGroup(2))
            sage: E2atom(Xmol)
            E_2
            sage: E2atom(E2mol)
            E_2(E_2)

        A multisort example::

            sage: A = AtomicSpecies("X")
            sage: M2 = MolecularSpecies("X, Y")
            sage: C3 = A(CyclicPermutationGroup(3))
            sage: X = M2(SymmetricGroup(1), {0: [1]})
            sage: Y = M2(SymmetricGroup(1), {1: [1]})
            sage: C3(X*Y)
            {((1,2,3)(4,5,6),): ({1, 2, 3}, {4, 5, 6})}
        '''

class AtomicSpecies(UniqueRepresentation, Parent):
    """
    The set of multisort atomic species.

    INPUT:

    - ``names`` -- an iterable of strings for the sorts of the
      species
    """
    @staticmethod
    def __classcall__(cls, names):
        '''
        Normalize the arguments.

        TESTS::

            sage: from sage.rings.species import AtomicSpecies
            sage: A1 = AtomicSpecies("X")
            sage: A2 = AtomicSpecies("Y")
            sage: A3 = AtomicSpecies("X, Y")
            sage: A4 = AtomicSpecies(["X", "Y"])
            sage: A1 == A2
            False
            sage: A3 is A4
            True
        '''
    def __init__(self, names) -> None:
        '''
        Initialize the class of atomic species.

        TESTS:

        We have to exclude ``_test_graded_components``, because
        :meth:`~sage.combinat.integer_vector.IntegerVectors.some_elements`
        yields degrees that are too large::

            sage: from sage.rings.species import AtomicSpecies
            sage: A1 = AtomicSpecies(["X"])
            sage: A2 = AtomicSpecies(["X", "Y"])
            sage: TestSuite(A1).run(skip="_test_graded_components")
            sage: TestSuite(A2).run(skip="_test_graded_components")
        '''
    def __contains__(self, x) -> bool:
        '''
        Return whether ``x`` is in ``self``.

        TESTS::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies("X")
            sage: G = PermutationGroup([[(1,2)], [(3,4)]]); G
            Permutation Group with generators [(3,4), (1,2)]
            sage: G.disjoint_direct_product_decomposition()
            {{1, 2}, {3, 4}}
            sage: G in A
            False

        For convenience, directly indecomposable permutation groups
        are regarded as being in `AtomicSpecies`::

            sage: G = PermutationGroup([(1,2)])
            sage: G in AtomicSpecies("X")
            True
            sage: A(G) in A
            True
            sage: G in AtomicSpecies("X, Y")
            False
            sage: (G, {0: [1,2]}) in AtomicSpecies("X, Y")
            True
            sage: (G, {3: [1,2]}) in AtomicSpecies("X, Y")
            False
            sage: (G, {0: [1]}) in AtomicSpecies("X, Y")
            False
            sage: (G, {0: [1], 1: [2]}) in AtomicSpecies("X, Y")
            False
            sage: (0, {0: []}) in AtomicSpecies("X, Y")
            False
        '''
    def grading_set(self):
        '''
        Return the set of non-negative integer vectors, whose length is
        the arity of ``self``.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: AtomicSpecies(["X"]).grading_set()
            Integer vectors of length 1
        '''
    def subset(self, size):
        '''
        Return the set of atomic species with given total cardinality.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies(["X", "Y"])
            sage: sorted(A.subset(3))
            [E_3(X), C_3(X), E_3(Y), C_3(Y)]
        '''
    def graded_component(self, mc):
        '''
        Return the set of atomic species with given multicardinality.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies
            sage: A = AtomicSpecies(["X", "Y"])
            sage: len(A.graded_component([2, 3]))
            1
            sage: A.graded_component([2, 3])  # random
            {{((2,3)(4,5), (1,2,3)): ({4, 5}, {1, 2, 3})}}

        TESTS::

            sage: A.graded_component([0])
            Traceback (most recent call last):
            ...
            ValueError: invalid degree
        '''
    Element = AtomicSpeciesElement

class MolecularSpecies(IndexedFreeAbelianMonoid):
    '''
    The monoid of multisort molecular species.

    INPUT:

    - ``names`` -- an iterable of strings for the sorts of the
      species

    EXAMPLES::

        sage: from sage.rings.species import MolecularSpecies
        sage: M = MolecularSpecies("X,Y")
        sage: G = PermutationGroup([[(1,2),(3,4)], [(5,6)]])
        sage: M(G, {0: [5,6], 1: [1,2,3,4]})
        E_2(X)*E_2(Y^2)
    '''
    @staticmethod
    def __classcall__(cls, names):
        '''
        Normalize the arguments.

        EXAMPLES::

            sage: from sage.rings.species import MolecularSpecies
            sage: MolecularSpecies("X,Y") is MolecularSpecies(["X", "Y"])
            True

            sage: MolecularSpecies("X,Y") == MolecularSpecies(["X", "Z"])
            False
        '''
    def __init__(self, names) -> None:
        '''
        Initialize the monoid of molecular species.

        TESTS:

        We have to exclude ``_test_graded_components``, because
        :meth:`~sage.combinat.integer_vector.IntegerVectors.some_elements`
        yields degrees that are too large::

            sage: from sage.rings.species import MolecularSpecies
            sage: M1 = MolecularSpecies("X")
            sage: TestSuite(M1).run(skip="_test_graded_components")
            sage: M2 = MolecularSpecies(["X", "Y"])
            sage: TestSuite(M2).run(skip="_test_graded_components")
        '''
    def grading_set(self):
        '''
        Return the set of non-negative integer vectors, whose length is
        the arity of ``self``.

        EXAMPLES::

            sage: from sage.rings.species import MolecularSpecies
            sage: MolecularSpecies(["X", "Y"]).grading_set()
            Integer vectors of length 2
        '''
    def subset(self, size):
        '''
        Return the set of molecular species with given total cardinality.

        EXAMPLES::

            sage: from sage.rings.species import MolecularSpecies
            sage: M = MolecularSpecies(["X", "Y"])
            sage: M.subset(3)  # random
            {X*E_2(Y), X*Y^2, C_3(Y), E_3(X), Y^3, Y*E_2(Y), C_3(X), X^2*Y,
             E_3(Y), E_2(X)*Y, X*E_2(X), X^3}
        '''
    def graded_component(self, mc):
        '''
        Return the set of molecular species with given multicardinality.

        EXAMPLES::

            sage: from sage.rings.species import MolecularSpecies
            sage: M = MolecularSpecies(["X", "Y"])
            sage: M.graded_component([3, 2])  # random
            {E_3(X)*Y^2, X^3*Y^2, X*E_2(X)*E_2(Y), X^3*E_2(Y),
             {((1,2,3), (1,3)(4,5)): ({1, 2, 3}, {4, 5})},
             X*{((1,2)(3,4),): ({1, 2}, {3, 4})}, X*E_2(X)*Y^2, E_3(X)*E_2(Y),
             C_3(X)*Y^2, C_3(X)*E_2(Y)}

        TESTS::

            sage: M.graded_component([0])
            Traceback (most recent call last):
            ...
            ValueError: invalid degree
        '''
    class Element(IndexedFreeAbelianMonoidElement):
        '''
        A molecular species.

        EXAMPLES::

            sage: from sage.rings.species import MolecularSpecies
            sage: M = MolecularSpecies("X")
            sage: M(CyclicPermutationGroup(3))
            C_3

        TESTS::

            sage: X = M(CyclicPermutationGroup(3))
            sage: C3 = M(CyclicPermutationGroup(3))
            sage: TestSuite(X*C3).run()
        '''
        @cached_method
        def grade(self):
            '''
            Return the grade of ``self``.

            EXAMPLES::

                sage: from sage.rings.species import MolecularSpecies
                sage: M = MolecularSpecies("X, Y")
                sage: G = PermutationGroup([[(1,2),(3,4),(5,6),(7,8,9,10)]]); G
                Permutation Group with generators [(1,2)(3,4)(5,6)(7,8,9,10)]
                sage: a = M(G, {0: [1,2,3,4], 1: [5,6,7,8,9,10]}); a
                {((1,2,3,4)(5,6)(7,8)(9,10),): ({5, 6, 7, 8}, {1, 2, 3, 4, 9, 10})}
                sage: a.grade()
                [4, 6]

            TESTS::

                sage: M.one().grade()
                [0, 0]
            '''
        @cached_method
        def permutation_group(self):
            '''
            Return the (transitive) permutation group
            corresponding to ``self``, together with the partition of
            the domain into sorts.

            EXAMPLES::

                sage: from sage.rings.species import MolecularSpecies
                sage: M = MolecularSpecies("X,Y")
                sage: G = PermutationGroup([[(1,2),(3,4)], [(5,6)]])
                sage: A = M(G, {0: [5,6], 1: [1,2,3,4]}); A
                E_2(X)*E_2(Y^2)
                sage: A.permutation_group()
                (Permutation Group with generators [(3,4)(5,6), (1,2)],
                 (frozenset({1, 2}), frozenset({3, 4, 5, 6})))

            Note that we cannot rely on blocks of the partition being
            consecutive::

                sage: A = M(PermutationGroup([(3,4)]), {0:[1,3,4], 1:[2]})
                sage: A
                X*Y*E_2(X)
                sage: A.permutation_group()[1]
                (frozenset({1, 3, 4}), frozenset({2}))

            TESTS::

                sage: B = M(PermutationGroup([(1,2,3)]), {0: [1,2,3]}); B
                C_3(X)
                sage: B.permutation_group()
                (Permutation Group with generators [(1,2,3)],
                 (frozenset({1, 2, 3}), frozenset()))

                sage: G = PermutationGroup([[(1,2),(3,4)], [(5,6)]])
                sage: A = M(G, {0: [5,6], 1: [1,2,3,4]})
                sage: A * B
                E_2(X)*C_3(X)*E_2(Y^2)
                sage: (A*B).permutation_group()
                (Permutation Group with generators [(6,7)(8,9), (3,4,5), (1,2)],
                 (frozenset({1, 2, 3, 4, 5}), frozenset({6, 7, 8, 9})))

                sage: C = M(PermutationGroup([(2,3)]), {0: [1], 1: [2,3]}); C
                X*E_2(Y)
                sage: C.permutation_group()
                (Permutation Group with generators [(2,3)],
                 (frozenset({1}), frozenset({2, 3})))

                sage: (C^3).permutation_group()
                (Permutation Group with generators [(8,9), (6,7), (4,5)],
                 (frozenset({1, 2, 3}), frozenset({4, 5, 6, 7, 8, 9})))

                sage: M = MolecularSpecies("X")
                sage: F = M(SymmetricGroup(1)) * M(SymmetricGroup(2))
                sage: F.permutation_group()
                (Permutation Group with generators [(2,3)], (frozenset({1, 2, 3}),))

                sage: F = M(PermutationGroup([(1,2),(3,)]))
                sage: F.permutation_group()[0].domain()
                {1, 2, 3}

                sage: F = M(AlternatingGroup(2))
                sage: F.permutation_group()[0].domain()
                {1, 2}
            '''
        def cycle_index(self, parent=None):
            '''
            Return the cycle index of ``self``.

            This is essentially a variant of
            :meth:`~sage.categories.finite_permutation_groups.FinitePermutationGroups.ParentMethods.cycle_index`
            for subgroups of a Young subgroup of the symmetric group.

            EXAMPLES::

                sage: from sage.rings.species import MolecularSpecies
                sage: M = MolecularSpecies("X,Y")
                sage: G = PermutationGroup([[(1,2),(3,4)], [(5,6)]])
                sage: A = M(G, {0: [5,6], 1: [1,2,3,4]})
                sage: A.cycle_index()
                1/4*p[1, 1] # p[1, 1, 1, 1] + 1/4*p[1, 1] # p[2, 2] + 1/4*p[2] # p[1, 1, 1, 1] + 1/4*p[2] # p[2, 2]

            Find two molecular species with the same cycle index::

                sage: M = MolecularSpecies("X")
                sage: n = 6
                sage: Ms = M.subset(n)  # long time
                sage: Cs = [m.cycle_index() for m in Ms]  # long time
                sage: d = [m for m in Ms if Cs.count(m.cycle_index()) > 1]  # long time
                sage: len(d)  # long time
                2
                sage: Pb_4 = M(PermutationGroup([[(1,2), (3,4)], [(1,4), (2,3)]]))
                sage: X = M(SymmetricGroup(1))
                sage: X^2*Pb_4 in d  # long time
                True

            Find two atomic species with the same cycle index::

                sage: from sage.rings.species import AtomicSpecies
                sage: A = AtomicSpecies("X")
                sage: n = 8
                sage: As = A.subset(n)  # long time
                sage: Cs = [M({a: 1}).cycle_index() for a in As]  # long time
                sage: len([a for a in As if Cs.count(M({a: 1}).cycle_index()) > 1])  # long time
                10

            TESTS:

            Check that we support different parents::

                sage: F = CombinatorialFreeModule(QQ, Partitions())
                sage: M = MolecularSpecies("X,Y")
                sage: A = M(G, {0: [5,6], 1: [1,2,3,4]})
                sage: P = A.cycle_index(parent=tensor([F, F]))
                sage: P
                1/4*B[[1, 1]] # B[[1, 1, 1, 1]] + 1/4*B[[1, 1]] # B[[2, 2]] + 1/4*B[[2]] # B[[1, 1, 1, 1]] + 1/4*B[[2]] # B[[2, 2]]
                sage: P.parent() is tensor([F, F])
                True

            This parent should be a module with basis indexed by partitions::

                sage: A.cycle_index(parent=QQ)
                Traceback (most recent call last):
                  ...
                ValueError: `parent` should be a module with basis indexed by partitions
            '''
        def __call__(self, *args):
            '''
            Substitute `M_1,\\ldots, M_k` into ``self``.

            The arguments must all have the same parent and must all
            be molecular.  The number of arguments must be equal to
            the arity of ``self``.

            The result is a molecular species, whose parent is the
            same as those of the arguments.

            EXAMPLES::

                sage: from sage.rings.species import MolecularSpecies
                sage: M = MolecularSpecies("X")
                sage: X = M(SymmetricGroup(1))
                sage: E2 = M(SymmetricGroup(2))
                sage: E2(X)
                E_2
                sage: E2(X^2)
                E_2(X^2)
                sage: (X^2)(E2^3)
                E_2^6
                sage: X(E2)
                E_2
                sage: E2(E2)
                E_2(E_2)

                sage: M = MolecularSpecies(["X","Y"])
                sage: X = M(SymmetricGroup(1), {0: [1]})
                sage: Y = M(SymmetricGroup(1), {1: [1]})
                sage: (X*Y)(X, Y^2)
                X*Y^2

            A multisort example::

                sage: M1 = MolecularSpecies("X")
                sage: M2 = MolecularSpecies("X, Y")
                sage: C3 = M1(CyclicPermutationGroup(3))
                sage: X = M2(SymmetricGroup(1), {0: [1]})
                sage: Y = M2(SymmetricGroup(1), {1: [1]})
                sage: C3(X*Y)
                {((1,2,3)(4,5,6),): ({1, 2, 3}, {4, 5, 6})}

            TESTS::

                sage: M = MolecularSpecies("X")
                sage: M.one()()
                Traceback (most recent call last):
                ...
                ValueError: number of args must match arity of self

                sage: M.one()(2)
                Traceback (most recent call last):
                ...
                ValueError: all args must be molecular species

                sage: M2 = MolecularSpecies("X, Y")
                sage: X2 = M2(SymmetricGroup(1), {0: [1]})
                sage: Y2 = M2(SymmetricGroup(1), {1: [1]})
                sage: X = M(SymmetricGroup(1))
                sage: (X2*Y2)(X2, X)
                Traceback (most recent call last):
                ...
                ValueError: all args must have the same parent
            '''
        def structures(self, *labels) -> Generator[Incomplete, Incomplete]:
            '''
            Iterate over the structures on the given set of labels.

            This yields a list of relabelled representatives of the
            cosets of corresponding groups.

            The relabelling is such that the first few labels
            correspond to the first factor in the atomic
            decomposition, etc.

            EXAMPLES::

                sage: from sage.rings.species import MolecularSpecies
                sage: M = MolecularSpecies("X,Y")
                sage: a = M(PermutationGroup([(3,4),(5,)]), {0:[1,3,4], 1:[2,5]})
                sage: a
                X*Y^2*E_2(X)
                sage: sorted(a.structures([1, 2, 3], ["a", "b"]))
                [((1,), (\'a\',), (\'b\',), (2, 3)),
                 ((1,), (\'b\',), (\'a\',), (2, 3)),
                 ((2,), (\'a\',), (\'b\',), (1, 3)),
                 ((2,), (\'b\',), (\'a\',), (1, 3)),
                 ((3,), (\'a\',), (\'b\',), (1, 2)),
                 ((3,), (\'b\',), (\'a\',), (1, 2))]

                sage: G = PermutationGroup([[(2,3),(4,5)]])
                sage: a = M(G, {0: [1, 2, 3], 1: [4, 5]})
                sage: a
                X*E_2(X*Y)
                sage: sorted(a.structures([1, 2, 3], ["a", "b"]))
                [((1,), (2, 3, \'a\', \'b\')),
                 ((1,), (2, 3, \'b\', \'a\')),
                 ((2,), (1, 3, \'a\', \'b\')),
                 ((2,), (1, 3, \'b\', \'a\')),
                 ((3,), (1, 2, \'a\', \'b\')),
                 ((3,), (1, 2, \'b\', \'a\'))]
            '''

class PolynomialSpeciesElement(CombinatorialFreeModule.Element):
    '''
    A (virtual) polynomial species.

    TESTS::

        sage: from sage.rings.species import PolynomialSpecies
        sage: P = PolynomialSpecies(ZZ, ["X"])
        sage: C3 = P(CyclicPermutationGroup(3))
        sage: X = P(SymmetricGroup(1))
        sage: E2 = P(SymmetricGroup(2))
        sage: (E2*X + C3).homogeneous_degree()
        3

        sage: TestSuite(E2*X + C3).run()
    '''
    def is_constant(self):
        '''
        Return ``True`` if this is a constant polynomial species.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: X = P(SymmetricGroup(1), {0: [1]})
            sage: X.is_constant()
            False
            sage: (3*P.one()).is_constant()
            True
            sage: P(0).is_constant()
            True
            sage: (1 + X).is_constant()
            False
        '''
    def is_virtual(self):
        '''
        Return if ``self`` is a virtual species.

        TESTS::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: X = P(SymmetricGroup(1), {0: [1]})
            sage: Y = P(SymmetricGroup(1), {1: [1]})
            sage: V = 2 * X - 3 * Y; V
            2*X - 3*Y
            sage: V.is_virtual()
            True
            sage: (X * Y).is_virtual()
            False
        '''
    def is_molecular(self):
        '''
        Return if ``self`` is a molecular species.

        TESTS::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: X = P(SymmetricGroup(1), {0: [1]})
            sage: Y = P(SymmetricGroup(1), {1: [1]})
            sage: V = 2 * X - 3 * Y; V
            2*X - 3*Y
            sage: V.is_molecular()
            False
            sage: (2 * X).is_molecular()
            False
            sage: (X * Y).is_molecular()
            True
        '''
    def is_atomic(self):
        '''
        Return if ``self`` is an atomic species.

        TESTS::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: X = P(SymmetricGroup(1), {0: [1]})
            sage: Y = P(SymmetricGroup(1), {1: [1]})
            sage: V = 2 * X - 3 * Y; V
            2*X - 3*Y
            sage: V.is_atomic()
            False
            sage: (2 * X).is_atomic()
            False
            sage: (X * Y).is_atomic()
            False
            sage: Y.is_atomic()
            True
        '''
    def tilde(self):
        '''
        Return the tilde species of ``self``.

        The tilde species `\\tilde F` of a species `F` has as
        structures the set of pairs `(s, a)`, consisting of an
        `F`-structure `s` and an automorphism `a` of `s`.

        We use https://mathoverflow.net/a/480852 to compute it.

        EXAMPLES::

            sage: from sage.rings.species import AtomicSpecies, MolecularSpecies, PolynomialSpecies
            sage: M = MolecularSpecies("X")
            sage: P = PolynomialSpecies(QQ, "X")
            sage: sortkey = lambda x: (len(x[1]), sum(x[1].coefficients()), str(x[0]))
            sage: n=4; table(sorted([(m, P.monomial(m).tilde()) for m in M.subset(n)], key=sortkey))
            X^4        X^4
            E_2(X^2)   2*E_2(X^2)
            X^2*E_2    2*X^2*E_2
            X*C_3      3*X*C_3
            C_4        4*C_4
            E_2^2      4*E_2^2
            Pb_4       4*Pb_4
            X*E_3      X*E_3 + X^2*E_2 + X*C_3
            Eo_4       Eo_4 + 2*X*C_3 + Pb_4
            E_2(E_2)   2*E_2(E_2) + E_2^2 + Pb_4 + C_4
            E_4        E_4 + E_2^2 + X*C_3 + E_2(E_2) + C_4

            sage: P.<X,Y> = PolynomialSpecies(QQ)
            sage: E2 = PolynomialSpecies(QQ, "X")(SymmetricGroup(2))
            sage: E2(X*Y).tilde()
            2*E_2(X*Y)
        '''
    def hadamard_product(self, other):
        '''
        Compute the hadamard product of ``self`` and ``other``.

        EXAMPLES:

        Exercise 2.1.9 from [BLL1998]_::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X"])
            sage: C3 = P(CyclicPermutationGroup(3))
            sage: X = P(SymmetricGroup(1))
            sage: E2 = P(SymmetricGroup(2))
            sage: C3.hadamard_product(C3)
            2*C_3
            sage: (X^3).hadamard_product(C3)
            2*X^3
            sage: (X*E2).hadamard_product(X*E2)
            X*E_2 + X^3

            sage: C3.hadamard_product(E2^2)
            0

        We can create the table of marks for the symmetric group::

            sage: E3 = P(SymmetricGroup(3))
            sage: C = [X^3, X*E2, C3, E3]
            sage: table([(b, [(a.hadamard_product(b)).coefficient(b.support()[0]) for a in C]) for b in C])
              X^3     [6, 3, 2, 1]
              X*E_2   [0, 1, 0, 1]
              C_3     [0, 0, 2, 1]
              E_3     [0, 0, 0, 1]

        TESTS::

            sage: C3.hadamard_product(-C3)
            -2*C_3

            sage: Q = PolynomialSpecies(ZZ, ["Y"])
            sage: P.one().hadamard_product(Q.one())
            Traceback (most recent call last):
            ...
            ValueError: the factors of a Hadamard product must have the same parent
        '''
    def __call__(self, *args):
        '''
        Substitute the arguments into ``self``.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(QQ, ["X"])
            sage: X = P(SymmetricGroup(1))
            sage: E2 = P(SymmetricGroup(2))
            sage: E2(-X)
            -E_2 + X^2
            sage: E2(X^2)
            E_2(X^2)

            sage: E2(X + X^2)
            E_2 + X^3 + E_2(X^2)

            sage: P2 = PolynomialSpecies(QQ, ["X", "Y"])
            sage: X = P2(SymmetricGroup(1), {0: [1]})
            sage: Y = P2(SymmetricGroup(1), {1: [1]})
            sage: E2(X + Y)
            E_2(X) + X*Y + E_2(Y)

            sage: E2(X*Y)(E2(X), E2(Y))
            E_2(E_2(X)*E_2(Y))

            sage: R.<q> = QQ[]
            sage: P = PolynomialSpecies(R, ["X"])
            sage: X = P(SymmetricGroup(1))
            sage: E2 = P(SymmetricGroup(2))
            sage: E2(q*X)
            q^2*E_2

        TESTS::

            sage: P = PolynomialSpecies(QQ, "X")
            sage: P.one()()
            Traceback (most recent call last):
            ...
            ValueError: number of args must match arity of self

            sage: P.one()(2)
            Traceback (most recent call last):
            ...
            ValueError: the args must be PolynomialSpecies

            sage: P = PolynomialSpecies(QQ, "X, Y")
            sage: Q.<X> = PolynomialSpecies(QQ)
            sage: R.<Y> = PolynomialSpecies(QQ)
            sage: P.one()(X, Y)
            Traceback (most recent call last):
            ...
            ValueError: all args must have the same parent

            sage: P.zero()(X, X)
            0
        '''
    def factor(self):
        '''
        Return the factorization of this species.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X"])
            sage: C3 = P(CyclicPermutationGroup(3))
            sage: X = P(SymmetricGroup(1))
            sage: E2 = P(SymmetricGroup(2))
            sage: f = (3*E2*X + C3)*(2*E2 + C3)
            sage: factor(f)
            (2*E_2 + C_3) * (3*X*E_2 + C_3)

        TESTS::

            sage: P(6).factor()
            2 * 3
        '''
    def structures(self, *labels) -> Generator[Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        This yields a list of pairs consisting of a molecular species
        and a relabelled representative of the cosets of
        corresponding groups.

        The relabelling is such that the first few labels correspond
        to the first factor in the atomic decomposition, etc.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X"])
            sage: C3 = P(CyclicPermutationGroup(3))
            sage: X = P(SymmetricGroup(1))
            sage: E2 = P(SymmetricGroup(2))
            sage: f = 2*E2*X + E2^2
            sage: list(f.structures([1, 2, 3]))
            [(X*E_2, ((1, 3), (2,)), 0),
             (X*E_2, ((2, 3), (1,)), 0),
             (X*E_2, ((1, 2), (3,)), 0),
             (X*E_2, ((1, 3), (2,)), 1),
             (X*E_2, ((2, 3), (1,)), 1),
             (X*E_2, ((1, 2), (3,)), 1)]
        '''

class PolynomialSpecies(CombinatorialFreeModule):
    """
    The ring of polynomial weighted virtual multisort species.

    INPUT:

    - ``base_ring`` -- a ring
    - ``names`` -- an iterable of strings for the sorts of the
      species

    EXAMPLES::

        sage: from sage.rings.species import PolynomialSpecies
        sage: P.<X,Y> = PolynomialSpecies(QQ)
        sage: G = SymmetricGroup(5).young_subgroup([2, 3])
        sage: P(G, ([1,2], [3,4,5]))
        E_2(X)*E_3(Y)
    """
    def __classcall__(cls, base_ring, names):
        '''
        Normalize the arguments.

        TESTS::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P1 = PolynomialSpecies(ZZ, "X, Y")
            sage: P2 = PolynomialSpecies(ZZ, "X, Y")
            sage: P3 = PolynomialSpecies(ZZ, ["X", "Z"])
            sage: P1 is P2
            True
            sage: P1 == P3
            False
        '''
    def __init__(self, base_ring, names) -> None:
        '''
        Initialize the ring of polynomial species.

        TESTS::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, "X")
            sage: TestSuite(P).run()
            sage: P2 = PolynomialSpecies(ZZ, "X, Y")
            sage: TestSuite(P2).run()
        '''
    def change_ring(self, R):
        '''
        Return the base change of ``self`` to `R`.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: P.change_ring(QQ)
            Polynomial species in X, Y over Rational Field

        TESTS::

            sage: P.change_ring(ZZ) is P
            True
        '''
    def degree_on_basis(self, m):
        '''
        Return the degree of the molecular species indexed by ``m``.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, ["X", "Y"])
            sage: E4X = P(SymmetricGroup(4), {0: range(1, 5)}); E4X
            E_4(X)
            sage: E4Y = P(SymmetricGroup(4), {1: range(1, 5)}); E4Y
            E_4(Y)
            sage: P.degree_on_basis(E4X.support()[0])
            4
            sage: P.degree_on_basis(E4Y.support()[0])
            4
        '''
    @cached_method
    def one_basis(self):
        '''
        Return ``SymmetricGroup(0)``, which indexes the one of this algebra,
        as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, "X")
            sage: P.one_basis()
            1
            sage: P2 = PolynomialSpecies(ZZ, "X, Y")
            sage: P2.one_basis()
            1
        '''
    def product_on_basis(self, H, K):
        '''
        Return the product of the basis elements indexed by `H` and `K`.

        EXAMPLES::

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(ZZ, "X")
            sage: L1 = [P(H) for H in SymmetricGroup(3).conjugacy_classes_subgroups()]
            sage: L2 = [P(H) for H in SymmetricGroup(2).conjugacy_classes_subgroups()]
            sage: matrix([[F * G for F in L1] for G in L2])  # indirect doctest
            [    X^5 X^3*E_2 X^2*C_3 X^2*E_3]
            [X^3*E_2 X*E_2^2 E_2*C_3 E_2*E_3]

        TESTS::

            sage: P = PolynomialSpecies(ZZ, "X")
            sage: X = P(SymmetricGroup(1))
            sage: type(list(X^2)[0][1])
            <class \'sage.rings.integer.Integer\'>
        '''
    Element = PolynomialSpeciesElement
