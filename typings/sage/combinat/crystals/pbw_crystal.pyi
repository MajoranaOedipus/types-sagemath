from _typeshed import Incomplete
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.crystals.pbw_datum import PBWData as PBWData, PBWDatum as PBWDatum
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PBWCrystalElement(Element):
    """
    A crystal element in the PBW model.
    """
    def __init__(self, parent, lusztig_datum, long_word=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['F', 4])
            sage: u = B.highest_weight_vector()
            sage: b = u.f_string([1,2,3,4,2,3,2,3,4,1,2])
            sage: TestSuite(b).run()
        """
    def lusztig_datum(self, word=None):
        """
        Return the Lusztig datum of ``self`` with respect to the reduced
        expression of the long word ``word``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: u = B.highest_weight_vector()
            sage: b = u.f_string([2,1,2,2,2,2,1,1,2,1,2,1,2,1,2,2])
            sage: b.lusztig_datum()
            (6, 0, 10)
            sage: b.lusztig_datum(word=[2,1,2])
            (4, 6, 0)
        """
    def __eq__(self, other):
        """
        Check equality of ``self`` with ``other``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: u = B.highest_weight_vector()
            sage: b = u.f_string([2,1,2,2,2,2,1,1,2,1,2,1,2,1,2,2])
            sage: bp = u.f_string([2,1,2,2,1,1,2,2,2,1,2,1,2,2,1,2])
            sage: b == bp
            True
        """
    def __ne__(self, other):
        """
        Check inequality of ``self`` with ``other``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: u = B.highest_weight_vector()
            sage: b = u.f_string([2,1,2,2,2,2,1,1,2,1,2,1,2,1,2,2])
            sage: bp = u.f_string([2,1,2,2,1,1,2,2,2,1,2,1,2,2,1,2])
            sage: b != bp
            False
        """
    @cached_method
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: u = B.highest_weight_vector()
            sage: b = u.f_string([2,1,2,2,2,2,1,1,2,1,2,1,2,1,2,2])
            sage: bp = u.f_string([2,1,2,2,1,1,2,2,2,1,2,1,2,2,1,2])
            sage: hash(b) == hash(bp)
            True
        """
    def e(self, i):
        """
        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['B', 3])
            sage: b = B.highest_weight_vector()
            sage: c = b.f_string([2,1,3,2,1,3,2,2]); c
            PBW monomial with Lusztig datum (0, 1, 0, 1, 0, 0, 0, 1, 2)
            sage: c.e(2)
            PBW monomial with Lusztig datum (0, 1, 0, 1, 0, 0, 0, 1, 1)
            sage: c.e_string([2,2,1,3,2,1,3,2]) == b
            True
        """
    def f(self, i):
        '''
        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW("D4")
            sage: b = B.highest_weight_vector()
            sage: c = b.f_string([1,2,3,1,2,3,4]); c
            PBW monomial with Lusztig datum (0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0)
            sage: c == b.f_string([1,2,4,1,2,3,3])
            True
        '''
    def epsilon(self, i):
        '''
        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(["A2"])
            sage: s = B((3,0,0), (1,2,1))
            sage: s.epsilon(1)
            3
            sage: s.epsilon(2)
            0
        '''
    def phi(self, i):
        """
        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: s = B((3,0,0), (1,2,1))
            sage: s.phi(1)
            -3
            sage: s.phi(2)
            3
        """
    def weight(self):
        """
        Return weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['A', 2])
            sage: s = B((2,2,2), (1,2,1))
            sage: s.weight()
            (-4, 0, 4)
        """
    def star(self):
        """
        Return the starred crystal element corresponding
        to ``self``.

        Let `b` be an element of ``self`` with Lusztig datum
        `(b_1, \\ldots, b_N)` with respect to `w_0 = s_{i_1} \\cdots s_{i_N}`.
        Then `b^*` is the element with Lusztig datum `(b_N, \\ldots, b_1)`
        with respect to `w_0 = s_{i_N^*} \\cdots s_{i_1^*}`, where
        `i_j^* = \\omega(i_j)` with `\\omega` being the :meth:`automorphism
        <sage.combinat.root_system.cartan_type.CartanType_standard_finite.opposition_automorphism>`
        given by the action of `w_0` on the simple roots.

        EXAMPLES::

            sage: P = crystals.infinity.PBW(['A', 2])
            sage: P((1,2,3), (1,2,1)).star() == P((3,2,1), (2,1,2))
            True

            sage: B = crystals.infinity.PBW(['E', 6])
            sage: b = B.highest_weight_vector()
            sage: c = b.f_string([1,2,6,3,4,2,5,2,3,4,1,6])
            sage: c == c.star().star()
            True

        TESTS::

            sage: from itertools import product
            sage: def test_star(PBW, depth):
            ....:     S = crystals.infinity.Star(PBW)
            ....:     for f_str in product(*([PBW.index_set()]*depth)):
            ....:         x = PBW.highest_weight_vector().f_string(f_str).star()
            ....:         y = S.highest_weight_vector().f_string(f_str)
            ....:         assert x.lusztig_datum() == y.value.lusztig_datum()
            sage: P = crystals.infinity.PBW(['A', 2])
            sage: test_star(P, 5)
            sage: P = crystals.infinity.PBW(['A', 3])
            sage: test_star(P, 5)
            sage: P = crystals.infinity.PBW(['B', 3])
            sage: test_star(P, 5)
            sage: P = crystals.infinity.PBW(['C', 3])
            sage: test_star(P, 5)
            sage: P = crystals.infinity.PBW(['D', 4])
            sage: test_star(P, 5)  # long time
            sage: P = crystals.infinity.PBW(['D', 5])
            sage: test_star(P, 4)  # long time
            sage: P = crystals.infinity.PBW(['E', 6])
            sage: test_star(P, 4)  # long time
            sage: P = crystals.infinity.PBW(['F', 4])
            sage: test_star(P, 4)  # long time
            sage: P = crystals.infinity.PBW(['G', 2])
            sage: test_star(P, 5)
        """

class PBWCrystal(Parent, UniqueRepresentation):
    """
    Crystal of `\\mathcal{B}(\\infty)` given by PBW monomials.

    A model of the crystal `\\mathcal{B}(\\infty)` whose elements are
    PBW datum up to equivalence by the tropical Plücker relations.
    The crystal structure on Lusztig data `x = (x_1, \\ldots, x_m)`
    for the reduced word `s_{i_1} \\cdots s_{i_m} = w_0` is given as
    follows. Suppose `i_1 = j`, then `f_j x = (x_1 + 1, x_2, \\ldots, x_m)`.
    If `i_1 \\neq j`, then we use the tropical Plücker relations to
    change the reduced expression such that `i_1' = j` and then we
    change back to the original word.

    EXAMPLES::

        sage: PBW = crystals.infinity.PBW(['B', 3])
        sage: hw = PBW.highest_weight_vector()
        sage: x = hw.f_string([1,2,2,3,3,1,3,3,2,3,2,1,3,1,2,3,1,2,1,3,2]); x
        PBW monomial with Lusztig datum (1, 1, 1, 3, 1, 0, 0, 1, 1)

    Elements are expressed in terms of Lusztig datum for a fixed
    reduced expression of `w_0`::

        sage: PBW.default_long_word()
        [1, 3, 2, 3, 1, 2, 3, 1, 2]
        sage: PBW.set_default_long_word([2,1,3,2,1,3,2,3,1])
        sage: x
        PBW monomial with Lusztig datum (3, 1, 1, 0, 1, 0, 1, 3, 4)
        sage: PBW.set_default_long_word([1, 3, 2, 3, 1, 2, 3, 1, 2])

    We can construct elements by giving it Lusztig data (with respect
    to the default long word)::

        sage: PBW([1,1,1,3,1,0,0,1,1])
        PBW monomial with Lusztig datum (1, 1, 1, 3, 1, 0, 0, 1, 1)

    We can also construct elements by passing in a reduced expression
    for a long word::

        sage: x = PBW([1,1,1,3,1,0,0,1,1], [3,2,1,3,2,3,2,1,2]); x
        PBW monomial with Lusztig datum (1, 1, 1, 0, 1, 0, 5, 1, 1)
        sage: x.to_highest_weight()[1]
        [1, 2, 2, 2, 2, 2, 1, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1, 3]
    """
    @staticmethod
    def __classcall__(cls, cartan_type):
        '''
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B1 = crystals.infinity.PBW([\'A\', 2])
            sage: B2 = crystals.infinity.PBW("A2")
            sage: B3 = crystals.infinity.PBW(CartanType("A2"))
            sage: B1 is B2 and B2 is B3
            True
        '''
    module_generators: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['B', 2])
            sage: TestSuite(B).run()
        """
    def default_long_word(self):
        """
        Return the default long word used to express elements of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['E', 6])
            sage: B.default_long_word()
            [1, 3, 4, 5, 6, 2, 4, 5, 3, 4, 1, 3, 2, 4, 5, 6, 2, 4,
             5, 3, 4, 1, 3, 2, 4, 5, 3, 4, 1, 3, 2, 4, 1, 3, 2, 1]
        """
    def set_default_long_word(self, word) -> None:
        """
        Set the default long word used to express elements of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.PBW(['C', 3])
            sage: B.default_long_word()
            [1, 3, 2, 3, 1, 2, 3, 1, 2]
            sage: x = B.highest_weight_vector().f_string([2,1,3,2,3,1,2,3,3,1])
            sage: x
            PBW monomial with Lusztig datum (1, 2, 2, 0, 0, 0, 0, 0, 1)
            sage: B.set_default_long_word([2,1,3,2,1,3,2,3,1])
            sage: B.default_long_word()
            [2, 1, 3, 2, 1, 3, 2, 3, 1]
            sage: x
            PBW monomial with Lusztig datum (2, 0, 0, 0, 0, 0, 1, 3, 2)

        TESTS::

            sage: B = crystals.infinity.PBW(['A', 3])
            sage: B._check_is_long_word([1,2,1,3,2,1,2])
            Traceback (most recent call last):
            ...
            ValueError: not a reduced word of the long element
        """
    Element = PBWCrystalElement
