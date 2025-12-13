from _typeshed import Incomplete
from sage.categories.regular_supercrystals import RegularSuperCrystals as RegularSuperCrystals
from sage.combinat.crystals.letters import CrystalOfBKKLetters as CrystalOfBKKLetters
from sage.combinat.crystals.tensor_product import CrystalOfWords as CrystalOfWords
from sage.combinat.crystals.tensor_product_element import CrystalOfBKKTableauxElement as CrystalOfBKKTableauxElement
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.structure.parent import Parent as Parent

class CrystalOfBKKTableaux(CrystalOfWords):
    """
    Crystal of tableaux for type `A(m|n)`.

    This is an implementation of the tableaux model of the
    Benkart-Kang-Kashiwara crystal [BKK2000]_ for the Lie
    superalgebra `\\mathfrak{gl}(m+1,n+1)`.

    INPUT:

    - ``ct`` -- a super Lie Cartan type of type `A(m|n)`
    - ``shape`` -- shape specifying the highest weight; this should be
      a partition contained in a hook of height `n+1` and width `m+1`

    EXAMPLES::

        sage: T = crystals.Tableaux(['A', [1,1]], shape = [2,1])
        sage: T.cardinality()
        20
    """
    @staticmethod
    def __classcall_private__(cls, ct, shape):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: crystals.Tableaux(['A', [1, 2]], shape=[2,1])
            Crystal of BKK tableaux of shape [2, 1] of gl(2|3)
            sage: crystals.Tableaux(['A', [1, 1]], shape=[3,3,3])
            Traceback (most recent call last):
            ...
            ValueError: invalid hook shape
        """
    module_generators: Incomplete
    def __init__(self, ct, shape) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: T = crystals.Tableaux(['A', [1,1]], shape = [2,1]); T
            Crystal of BKK tableaux of shape [2, 1] of gl(2|2)
            sage: TestSuite(T).run()
        """
    def shape(self):
        """
        Return the shape of ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A', [1, 2]], shape=[2,1])
            sage: T.shape()
            [2, 1]
        """
    def genuine_highest_weight_vectors(self, index_set=None):
        """
        Return a tuple of genuine highest weight elements.

        A *fake highest weight vector* is one which is annihilated by
        `e_i` for all `i` in the index set, but whose weight is not
        bigger in dominance order than all other elements in the
        crystal. A *genuine highest weight vector* is a highest
        weight element that is not fake.

        EXAMPLES::

            sage: B = crystals.Tableaux(['A', [1,1]], shape=[3,2,1])
            sage: B.genuine_highest_weight_vectors()
            ([[-2, -2, -2], [-1, -1], [1]],)
            sage: B.highest_weight_vectors()
            ([[-2, -2, -2], [-1, -1], [1]],
             [[-2, -2, -2], [-1, 2], [1]],
             [[-2, -2, 2], [-1, -1], [1]])
        """
    class Element(CrystalOfBKKTableauxElement): ...
