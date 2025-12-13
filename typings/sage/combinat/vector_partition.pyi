from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.partition import Partition as Partition
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def find_min(vect):
    """
    Return a string of ``0``'s with one ``1`` at the location where the list
    ``vect`` has its last entry which is not equal to ``0``.

    INPUT:

    - ``vec`` -- list of integers

    OUTPUT:

    A list of the same length with ``0``'s everywhere, except for a ``1``
    at the last position where ``vec`` has an entry not equal to ``0``.

    EXAMPLES::

        sage: from sage.combinat.vector_partition import find_min
        sage: find_min([2, 1])
        [0, 1]
        sage: find_min([2, 1, 0])
        [0, 1, 0]
    """
def IntegerVectorsIterator(vect, min=None) -> Generator[Incomplete]:
    """
    Return an iterator over the list of integer vectors which are componentwise
    less than or equal to ``vect``, and lexicographically greater than or equal
    to ``min``.

    INPUT:

    - ``vect`` -- list of nonnegative integers
    - ``min`` -- list of nonnegative integers dominated elementwise by ``vect``

    OUTPUT:

    A list in lexicographic order of all integer vectors (as lists) which are
    dominated elementwise by ``vect`` and are greater than or equal to ``min`` in
    lexicographic order.

    EXAMPLES::

        sage: from sage.combinat.vector_partition import IntegerVectorsIterator
        sage: list(IntegerVectorsIterator([1, 1]))
        [[0, 0], [0, 1], [1, 0], [1, 1]]

        sage: list(IntegerVectorsIterator([1, 1], min = [1, 0]))
        [[1, 0], [1, 1]]
    """

class VectorPartition(CombinatorialElement):
    """
    A vector partition is a multiset of integer vectors.
    """
    @staticmethod
    def __classcall_private__(cls, vecpar):
        """
        Create a vector partition.

        EXAMPLES::

            sage: VectorPartition([[3, 2, 1], [2, 2, 1]])
            [[2, 2, 1], [3, 2, 1]]

        The parent class is the class of vector partitions of the sum of the
        vectors in ``vecpar``::

            sage: V = VectorPartition([[3, 2, 1], [2, 2, 1]])
            sage: V.parent()._vec
            (5, 4, 2)
        """
    def __init__(self, parent, vecpar) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: elt =  VectorPartition([[3, 2, 1], [2, 2, 1]])
            sage: TestSuite(elt).run()
        """
    def sum(self):
        """
        Return the sum vector as a list.

        EXAMPLES::

            sage: V = VectorPartition([[3, 2, 1], [2, 2, 1]])
            sage: V.sum()
            [5, 4, 2]
        """
    def partition_at_vertex(self, i):
        """
        Return the partition obtained by sorting the ``i``-th elements of
        the vectors in the vector partition.

        EXAMPLES::

            sage: V = VectorPartition([[1, 2, 1], [2, 4, 1]])
            sage: V.partition_at_vertex(1)
            [4, 2]
        """

class VectorPartitions(UniqueRepresentation, Parent):
    """
    Class of all vector partitions of ``vec`` with all parts greater than
    or equal to ``min`` in lexicographic order, with parts from ``parts``.

    A vector partition of ``vec`` is a list of vectors with nonnegative
    integer entries whose sum is ``vec``.

    INPUT:

    - ``vec`` -- integer vector
    - ``min`` -- integer vector dominated elementwise by ``vec``
    - ``parts`` -- finite list of possible parts
    - ``distinct`` -- boolean, set to ``True`` if only vector partitions with
      distinct parts are enumerated
    - ``is_repeatable`` -- boolean function on ``parts`` which gives ``True``
      in parts that can be repeated

    EXAMPLES:

    If ``min`` is not specified, then the class of all vector partitions of
    ``vec`` is created::

        sage: VP = VectorPartitions([2, 2])
        sage: for vecpar in VP:
        ....:     print(vecpar)
        [[0, 1], [0, 1], [1, 0], [1, 0]]
        [[0, 1], [0, 1], [2, 0]]
        [[0, 1], [1, 0], [1, 1]]
        [[0, 1], [2, 1]]
        [[0, 2], [1, 0], [1, 0]]
        [[0, 2], [2, 0]]
        [[1, 0], [1, 2]]
        [[1, 1], [1, 1]]
        [[2, 2]]

    If ``distinct`` is set to be True, then distinct part partitions are created::

        sage: VP = VectorPartitions([2,2], distinct = True)
        sage: list(VP)
        [[[0, 1], [1, 0], [1, 1]],
         [[0, 1], [2, 1]],
         [[0, 2], [2, 0]],
         [[1, 0], [1, 2]],
         [[2, 2]]]

    If ``min`` is specified, then the class consists of only those vector
    partitions whose parts are all greater than or equal to ``min`` in
    lexicographic order::

        sage: VP = VectorPartitions([2, 2], min = [1, 0])
        sage: for vecpar in VP:
        ....:     print(vecpar)
        [[1, 0], [1, 2]]
        [[1, 1], [1, 1]]
        [[2, 2]]
        sage: VP = VectorPartitions([2, 2], min = [1, 0], distinct = True)
        sage: for vecpar in VP:
        ....:     print(vecpar)
        [[1, 0], [1, 2]]
        [[2, 2]]

    If ``parts`` is specified, then the class consists only of those vector partitions
    whose parts are from ``parts``::

        sage: Vec_Par = VectorPartitions([2,2], parts=[[0,1],[1,0],[1,1]])
        sage: list(Vec_Par)
        [[[0, 1], [0, 1], [1, 0], [1, 0]], [[0, 1], [1, 0], [1, 1]], [[1, 1], [1, 1]]]

    If ``is_repeatable`` is specified, then the parts which satisfy the boolean function
    ``is_repeatable`` are allowed to be repeated::


        sage: Vector_Partitions = VectorPartitions([2,2], parts=[[0,1],[1,0],[1,1]], is_repeatable=lambda vec: sum(vec)%2!=0)
        sage: list(Vector_Partitions)
        [[[0, 1], [0, 1], [1, 0], [1, 0]], [[0, 1], [1, 0], [1, 1]]]
    """
    @staticmethod
    def __classcall_private__(cls, vec, min=None, parts=None, distinct: bool = False, is_repeatable=None):
        """
        Create the class of vector partitions of ``vec`` where all parts
        are greater than or equal to the vector ``min``.

        EXAMPLES::

            sage: VP1 = VectorPartitions([2, 1])
            sage: VP2 = VectorPartitions((2, 1), min = [0, 1])
            sage: VP1 is VP2
            True
        """
    def __init__(self, vec, min=None, parts=None, distinct: bool = False, is_repeatable=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: VP = VectorPartitions([2, 2])
            sage: TestSuite(VP).run()
        """
    Element = VectorPartition
    def __iter__(self):
        """
        Iterator for vector partitions.

        EXAMPLES::

            sage: VP = VectorPartitions([2, 2])
            sage: VP.cardinality()
            9
        """
