from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat import permutation as permutation
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DecreasingHeckeFactorization(Element, metaclass=InheritComparisonClasscallMetaclass):
    """
    Class of decreasing factorizations in the 0-Hecke monoid.

    INPUT:

    - ``t`` -- decreasing factorization inputted as list of lists

    - ``max_value`` -- maximal value of entries

    EXAMPLES::

        sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
        sage: t = [[3, 2], [], [2, 1]]
        sage: h = DecreasingHeckeFactorization(t, 3); h
        (3, 2)()(2, 1)
        sage: h.excess
        1
        sage: h.factors
        3
        sage: h.max_value
        3
        sage: h.value
        ((3, 2), (), (2, 1))

        sage: u = [[3, 2, 1], [3], [2, 1]]
        sage: h = DecreasingHeckeFactorization(u); h
        (3, 2, 1)(3)(2, 1)
        sage: h.weight()
        (2, 1, 3)
        sage: h.parent()
        Decreasing Hecke factorizations with 3 factors associated to [2, 1, 3, 2, 1] with excess 1
    """
    @staticmethod
    def __classcall_private__(self, t, max_value=None, parent=None):
        """
        Assign the correct parent for ``t`` and call ``t`` as an element of that parent.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: h1 = DecreasingHeckeFactorization([[3, 1], [], [3, 2]])
            sage: h1.parent()
            Fully commutative stable Grothendieck crystal of type A_2 associated to [1, 3, 2] with excess 1
            sage: h2 = DecreasingHeckeFactorization(h1)
            sage: h1 == h2
            True

            sage: h1 = DecreasingHeckeFactorization([[3, 1], [2, 1], [2, 1]])
            sage: F = h1.parent(); F
            Decreasing Hecke factorizations with 3 factors associated to [1, 3, 2, 1] with excess 2
            sage: h2 = F(h1)
            sage: h1 == h2
            True

        TESTS::

            sage: DecreasingHeckeFactorization([[]])
            ()
        """
    factors: Incomplete
    max_value: Incomplete
    w: Incomplete
    excess: Incomplete
    value: Incomplete
    def __init__(self, parent, t) -> None:
        """
        Initialize a decreasing factorization for ``self`` given the relevant data.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[2, 1], [2], [], [1]]
            sage: h1 = DecreasingHeckeFactorization(t); h1
            (2, 1)(2)()(1)
            sage: h1.excess
            1
            sage: h2 = DecreasingHeckeFactorization(t, 2)
            sage: h2.value
            ((2, 1), (2,), (), (1,))
            sage: h1 == h2
            True

            sage: t = [[2, 1], [2], [], [3, 1]]
            sage: h = DecreasingHeckeFactorization(t, 5)
            sage: h.max_value
            5
            sage: h.factors
            4
            sage: h.w
            (1, 2, 1, 3)

        TESTS::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t1 = [[], [3, 1], [], [2, 1], [1]]
            sage: t2 = [[], [3, 1], [], [2, 1], [2]]
            sage: h1 = DecreasingHeckeFactorization(t1, 3)
            sage: h2 = DecreasingHeckeFactorization(t2, 3)
            sage: h3 = DecreasingHeckeFactorization(t1)
            sage: h1 == h2, h1 == h3
            (False, True)
            sage: h1 != h2, h1 != h3
            (True, False)
        """
    def __hash__(self):
        """
        Return hash of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[], [2, 1], [2], [], [2]]
            sage: h1 = DecreasingHeckeFactorization(t)
            sage: h2 = DecreasingHeckeFactorization(t, 3)
            sage: h3 = DecreasingHeckeFactorization(t, 2)
            sage: hash(h1) == hash(h2)
            False
            sage: hash(h1) == hash(h3)
            True
        """
    def __eq__(self, other):
        """
        Return ``True`` if ``self`` equals ``other`` and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[], [2, 1], [2], [], [2]]
            sage: h1 = DecreasingHeckeFactorization(t)
            sage: h2 = DecreasingHeckeFactorization(t, 3)
            sage: h1 == h2
            True
        """
    def __lt__(self, other):
        """
        Return ``True`` if ``self`` comes before ``other`` and ``False``
        otherwise.

        We say that `h_1` comes before `h_2` if either weight of `h_1 <` weight of `h_2`
        lexicographically, or if both weights of `h_1` and `h_2` are equal,
        but `h_1 < h_2` lexicographically.
        This ordering is mainly used for sorting or comparison.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t1 = [[], [2, 1], [], [2, 1], [1]]
            sage: t2 = [[], [2, 1], [], [2, 1], [2]]
            sage: t3 = [[], [2, 1], [2], [1], [1]]
            sage: h1 = DecreasingHeckeFactorization(t1)
            sage: h2 = DecreasingHeckeFactorization(t2)
            sage: h3 = DecreasingHeckeFactorization(t3)
            sage: h1 < h2
            True
            sage: h1 < h3
            False
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[2], [2, 1], [], [4, 3, 1]]
            sage: h = DecreasingHeckeFactorization(t, 6)
            sage: h.weight()
            (3, 0, 2, 1)
        """
    def to_word(self):
        """
        Return the word associated to ``self`` in the 0-Hecke monoid.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[2], [], [2, 1], [4, 3, 1]]
            sage: h = DecreasingHeckeFactorization(t)
            sage: h.to_word()
            [2, 2, 1, 4, 3, 1]
        """
    def to_increasing_hecke_biword(self):
        """
        Return the associated increasing Hecke biword of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: t = [[2], [], [2, 1],[4, 3, 1]]
            sage: h = DecreasingHeckeFactorization(t, 4)
            sage: h.to_increasing_hecke_biword()
            [[1, 1, 1, 2, 2, 4], [1, 3, 4, 1, 2, 2]]
        """

class DecreasingHeckeFactorizations(UniqueRepresentation, Parent):
    """
    Set of decreasing factorizations in the 0-Hecke monoid.

    INPUT:

    - ``w`` -- an element in the symmetric group

    - ``factors`` -- the number of factors in the factorization

    - ``excess`` -- the total number of letters in the factorization minus the length of a reduced word for ``w``

    EXAMPLES::

        sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorizations
        sage: S = SymmetricGroup(3+1)
        sage: w = S.from_reduced_word([1, 3, 2, 1])
        sage: F = DecreasingHeckeFactorizations(w, 3, 3); F
        Decreasing Hecke factorizations with 3 factors associated to [1, 3, 2, 1] with excess 3
        sage: F.list()
        [(3, 1)(3, 1)(3, 2, 1), (3, 1)(3, 2, 1)(2, 1), (3, 2, 1)(2, 1)(2, 1)]
    """
    @staticmethod
    def __classcall_private__(cls, w, factors, excess):
        """
        Classcall to mend the input.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorizations
            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([1, 2 ,1])
            sage: F = DecreasingHeckeFactorizations(w, 4, 1); F
            Decreasing Hecke factorizations with 4 factors associated to [1, 2, 1] with excess 1

            sage: from sage.monoids.hecke_monoid import HeckeMonoid
            sage: H = HeckeMonoid(SymmetricGroup(3+1))
            sage: w = H.from_reduced_word([1, 2 ,1])
            sage: G = DecreasingHeckeFactorizations(w, 4, 1); G
            Decreasing Hecke factorizations with 4 factors associated to [1, 2, 1] with excess 1
            sage: F is G
            True
        """
    w: Incomplete
    factors: Incomplete
    H: Incomplete
    max_value: Incomplete
    excess: Incomplete
    def __init__(self, w, factors, excess) -> None:
        """
        Initialize a set for ``self`` given reduced word ``w`` in the symmetric group,
        number of factors ``factors`` and``excess`` extra letters.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorizations
            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([2, 1, 3, 2, 1])
            sage: F = DecreasingHeckeFactorizations(w, 4, 2)
            sage: F.w
            (2, 1, 3, 2, 1)
            sage: F.factors
            4
            sage: F.excess
            2
            sage: F.H
            0-Hecke monoid of the Symmetric group of order 4! as a permutation group

        TESTS::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorizations
            sage: S = SymmetricGroup(2+1)
            sage: w = S.from_reduced_word([1, 2, 1])
            sage: F = DecreasingHeckeFactorizations(w, 3, 1)
            sage: TestSuite(F).run()
        """
    def list(self):
        """
        Return list of all elements of ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorizations
            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([1, 3, 2, 1])
            sage: F = DecreasingHeckeFactorizations(w, 3, 3)
            sage: F.list()
            [(3, 1)(3, 1)(3, 2, 1), (3, 1)(3, 2, 1)(2, 1), (3, 2, 1)(2, 1)(2, 1)]
        """
    Element = DecreasingHeckeFactorization

class FullyCommutativeStableGrothendieckCrystal(UniqueRepresentation, Parent):
    """
    The crystal on fully commutative decreasing factorizations in the 0-Hecke
    monoid, as introduced by [MPPS2020]_.

    INPUT:

    - ``w`` -- an element in the symmetric group or a (skew) shape

    - ``factors`` -- the number of factors in the factorization

    - ``excess`` -- the total number of letters in the factorization minus the
      length of a reduced word for ``w``

    - ``shape`` -- boolean (default: ``False``); indicator for input ``w``,
      ``True`` if ``w`` is entered as a (skew) shape and ``False`` otherwise

    EXAMPLES::

        sage: S = SymmetricGroup(3+1)
        sage: w = S.from_reduced_word([1, 3, 2])
        sage: B = crystals.FullyCommutativeStableGrothendieck(w, 3, 2); B
        Fully commutative stable Grothendieck crystal of type A_2 associated to [1, 3, 2] with excess 2
        sage: B.list()
        [(1)(3, 1)(3, 2),
         (3, 1)(1)(3, 2),
         (3, 1)(3, 1)(2),
         (3)(3, 1)(3, 2),
         (3, 1)(3)(3, 2),
         (3, 1)(3, 2)(2)]

    We can also access the crystal by specifying a skew shape::

        sage: crystals.FullyCommutativeStableGrothendieck([[2, 2], [1]], 4, 1, shape=True)
        Fully commutative stable Grothendieck crystal of type A_3 associated to [2, 1, 3] with excess 1

    We can compute the highest weight elements::

        sage: hw = [w for w in B if w.is_highest_weight()]
        sage: hw
        [(1)(3, 1)(3, 2), (3)(3, 1)(3, 2)]
        sage: hw[0].weight()
        (2, 2, 1)

    The crystal operators themselves move elements between adjacent factors::

        sage: b = hw[0]; b
        (1)(3, 1)(3, 2)
        sage: b.f(2)
        (3, 1)(1)(3, 2)
    """
    @staticmethod
    def __classcall_private__(cls, w, factors, excess, shape: bool = False):
        """
        Classcall to mend the input.

        EXAMPLES::

            sage: A = crystals.FullyCommutativeStableGrothendieck([[3, 3], [2, 1]], 4, 1, shape=True); A
            Fully commutative stable Grothendieck crystal of type A_3 associated to [3, 2, 4] with excess 1
            sage: B = crystals.FullyCommutativeStableGrothendieck(SkewPartition([[3, 3], [2, 1]]), 4, 1, shape=True)
            sage: A is B
            True

            sage: C = crystals.FullyCommutativeStableGrothendieck((2, 1), 3, 2, shape=True); C
            Fully commutative stable Grothendieck crystal of type A_2 associated to [1, 3, 2] with excess 2
            sage: D = crystals.FullyCommutativeStableGrothendieck(Partition([2, 1]), 3, 2, shape=True)
            sage: C is D
            True
        """
    w: Incomplete
    factors: Incomplete
    H: Incomplete
    max_value: Incomplete
    excess: Incomplete
    def __init__(self, w, factors, excess) -> None:
        """
        Initialize a crystal for ``self`` given reduced word ``w`` in the symmetric group,
        number of factors ``factors`` and``excess`` extra letters.

        EXAMPLES::

            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([1, 3, 2])
            sage: B = crystals.FullyCommutativeStableGrothendieck(w, 3, 2)
            sage: B.w
            (1, 3, 2)
            sage: B.factors
            3
            sage: B.excess
            2
            sage: B.H
            0-Hecke monoid of the Symmetric group of order 4! as a permutation group

        The reduced word ``w`` should be fully commutative, that is, its
        associated permutation should avoid the pattern 321::

            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([1, 2, 1])
            sage: B = crystals.FullyCommutativeStableGrothendieck(w, 4, 2)
            Traceback (most recent call last):
            ...
            ValueError: w should be fully commutative

        TESTS::

            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([2, 3, 1])
            sage: B = crystals.FullyCommutativeStableGrothendieck(w, 4, 2)
            sage: TestSuite(B).run()
        """
    @lazy_attribute
    def module_generators(self):
        """
        Return generators for ``self`` as a crystal.

        EXAMPLES::

            sage: S = SymmetricGroup(3+1)
            sage: w = S.from_reduced_word([1, 3, 2])
            sage: B = crystals.FullyCommutativeStableGrothendieck(w, 3, 2)
            sage: B.module_generators
            ((1)(3, 1)(3, 2), (3)(3, 1)(3, 2))
            sage: C = crystals.FullyCommutativeStableGrothendieck(w, 4, 2)
            sage: C.module_generators
            (()(1)(3, 1)(3, 2),
             ()(3)(3, 1)(3, 2),
             (1)(1)(1)(3, 2),
             (1)(1)(3)(3, 2),
             (1)(3)(3)(3, 2))
        """
    class Element(DecreasingHeckeFactorization):
        def __init__(self, parent, t) -> None:
            """
            Create an instance ``self`` of element ``t``.

            This method takes into account the constraints on the word,
            the number of factors, and excess statistic associated to the parent class.

            EXAMPLES::

                sage: S = SymmetricGroup(3+1)
                sage: w = S.from_reduced_word([1, 3, 2])
                sage: B = crystals.FullyCommutativeStableGrothendieck(w, 3, 2)
                sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
                sage: h = DecreasingHeckeFactorization([[3, 1], [3], [3, 2]], 4)
                sage: u = B(h); u.value
                ((3, 1), (3,), (3, 2))
                sage: v = B([[3, 1], [3], [3, 2]]); v.value
                ((3, 1), (3,), (3, 2))
            """
        def e(self, i):
            """
            Return the action of `e_i` on ``self`` using the rules described in [MPPS2020]_.

            EXAMPLES::

                sage: S = SymmetricGroup(4+1)
                sage: w = S.from_reduced_word([2, 1, 4, 3, 2])
                sage: B = crystals.FullyCommutativeStableGrothendieck(w, 4, 3)
                sage: h = B([[4, 2], [4, 2, 1], [3, 2], [2]]); h
                (4, 2)(4, 2, 1)(3, 2)(2)
                sage: h.e(1)
                (4, 2)(4, 2, 1)(3)(3, 2)
                sage: h.e(2)
                (4, 2)(2, 1)(4, 3, 2)(2)
                sage: h.e(3)
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self`` using the rules described in [MPPS2020]_.

            EXAMPLES::

                sage: S = SymmetricGroup(4+1)
                sage: w = S.from_reduced_word([3, 2, 1, 4, 3])
                sage: B = crystals.FullyCommutativeStableGrothendieck(w, 4, 3)
                sage: h = B([[3, 2], [2, 1], [4, 3], [3, 1]]); h
                (3, 2)(2, 1)(4, 3)(3, 1)
                sage: h.f(1)
                (3, 2)(2, 1)(4, 3, 1)(3)
                sage: h.f(2)
                sage: h.f(3)
                (3, 2, 1)(1)(4, 3)(3, 1)
            """
        def bracketing(self, i):
            """
            Remove all bracketed letters between `i`-th and `(i+1)`-th entry.

            EXAMPLES::

                sage: S = SymmetricGroup(4+1)
                sage: w = S.from_reduced_word([3, 2, 1, 4, 3])
                sage: B = crystals.FullyCommutativeStableGrothendieck(w, 3, 2)
                sage: h = B([[3], [4, 2, 1], [4, 3, 1]])
                sage: h.bracketing(1)
                [[], []]
                sage: h.bracketing(2)
                [[], [2, 1]]
            """
