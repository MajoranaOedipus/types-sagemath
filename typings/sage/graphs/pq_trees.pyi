from _typeshed import Incomplete
from collections.abc import Generator

FULL: int
PARTIAL: int
EMPTY: int
ALIGNED: bool
UNALIGNED: bool
impossible_msg: str

def reorder_sets(sets):
    """
    Reorders a collection of sets such that each element appears on an
    interval.

    Given a collection of sets `C = S_1,...,S_k` on a ground set `X`,
    this function attempts to reorder them in such a way that `\\forall
    x \\in X` and `i<j` with `x\\in S_i, S_j`, then `x\\in S_l` for every
    `i<l<j` if it exists.

    INPUT:

    - ``sets`` -- list of instances of ``list, Set`` or ``set``

    ALGORITHM: PQ-Trees

    EXAMPLES:

    There is only one way (up to reversal) to represent contiguously
    the sequence of sets `\\{i-1, i, i+1\\}`::

        sage: from sage.graphs.pq_trees import reorder_sets
        sage: seq = [Set([i-1,i,i+1]) for i in range(1,15)]

    We apply a random permutation::

        sage: p = Permutations(len(seq)).random_element()
        sage: seq = [ seq[p(i+1)-1] for i in range(len(seq)) ]
        sage: ordered = reorder_sets(seq)
        sage: if not 0 in ordered[0]:
        ....:    ordered = ordered.reverse()
        sage: print(ordered)
        [{0, 1, 2}, {1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {4, 5, 6}, {5, 6, 7},
         {8, 6, 7}, {8, 9, 7}, {8, 9, 10}, {9, 10, 11}, {10, 11, 12},
         {11, 12, 13}, {12, 13, 14}, {13, 14, 15}]
    """

class PQ:
    """
    PQ-Trees

    This class should not be instantiated by itself: it is extended by
    :class:`P` and :class:`Q`. See the documentation of
    :mod:`sage.graphs.pq_trees` for more information.

    AUTHOR : Nathann Cohen
    """
    def __init__(self, seq) -> None:
        """
        Construction of a PQ-Tree.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])

        :issue:`17787`::

            sage: Graph('GvGNp?').is_interval()
            False
        """
    def reverse(self) -> None:
        """
        Recursively reverse ``self`` and its children.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])
            sage: p.ordering()
            [{1, 2}, {2, 3}, {2, 4}, {8, 2}, {9, 2}]
            sage: p.reverse()
            sage: p.ordering()
            [{9, 2}, {8, 2}, {2, 4}, {2, 3}, {1, 2}]
        """
    def __contains__(self, v) -> bool:
        """
        Test whether there exists an element of ``self`` containing
        an element ``v``.

        INPUT:

        - ``v`` -- an element of the ground set

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])
            sage: 5 in p
            False
            sage: 9 in p
            True
        """
    def __iter__(self):
        """
        Iterate over the children of ``self``.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])
            sage: for i in p:
            ....:     print(i)
            {1, 2}
            {2, 3}
            ('P', [{2, 4}, {8, 2}, {9, 2}])
        """
    def number_of_children(self):
        """
        Return the number of children of ``self``.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])
            sage: p.number_of_children()
            3
        """
    def ordering(self):
        """
        Return the current ordering given by listing the leaves from
        left to right.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([[1,2], [2,3], P([[2,4], [2,8], [2,9]])])
            sage: p.ordering()
            [{1, 2}, {2, 3}, {2, 4}, {8, 2}, {9, 2}]
        """
    def simplify(self, v, left: bool = False, right: bool = False):
        '''
        Return a simplified copy of ``self`` according to the element ``v``.

        If ``self`` is a partial P-tree for ``v``, we would like to
        restrict the permutations of its children to permutations
        keeping the children containing ``v`` contiguous. This
        function also "locks" all the elements not containing ``v``
        inside a `P`-tree, which is useful when one want to keep the
        elements containing ``v`` on one side (which is the case when
        this method is called).

        INPUT:

        - ``left``, ``right`` -- booleans; whether ``v`` is aligned to the
          right or to the left

        - ``v`` -- an element of the ground set

        OUTPUT:

        If ``self`` is a `Q`-Tree, the sequence of its children is
        returned. If ``self`` is a `P`-tree, 2 `P`-tree are returned,
        namely the two `P`-tree defined above and restricting the
        permutations, in the order implied by ``left, right`` (if
        ``right =True``, the second `P`-tree will be the one gathering
        the elements containing ``v``, if ``left=True``, the
        opposite).

        .. NOTE::

           This method is assumes that ``self`` is partial for ``v``,
           and aligned to the side indicated by ``left, right``.

        EXAMPLES:

        A `P`-Tree ::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = P([[2,4], [1,2], [0,8], [0,5]])
            sage: p.simplify(0, right = True)
            [(\'P\', [{2, 4}, {1, 2}]), (\'P\', [{0, 8}, {0, 5}])]

        A `Q`-Tree ::

            sage: q = Q([[2,4], [1,2], [0,8], [0,5]])
            sage: q.simplify(0, right = True)
            [{2, 4}, {1, 2}, {0, 8}, {0, 5}]
        '''
    def flatten(self):
        '''
        Return a flattened copy of ``self``.

        If ``self`` has only one child, we may as well consider its
        child\'s children, as ``self`` encodes no information. This
        method recursively "flattens" trees having only on PQ-tree
        child, and returns it.

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = Q([P([[2,4], [2,8], [2,9]])])
            sage: p.flatten()
            (\'P\', [{2, 4}, {8, 2}, {9, 2}])
        '''

class P(PQ):
    """
    A P-Tree is a PQ-Tree whose children can be permuted in any way.

    For more information, see the documentation of :mod:`sage.graphs.pq_trees`.
    """
    def set_contiguous(self, v):
        """
        Update ``self`` so that the sets containing ``v`` are
        contiguous for any admissible permutation of its subtrees.

        INPUT:

        - ``v`` -- an element of the ground set

        OUTPUT:

        According to the cases:

            * ``(EMPTY, ALIGNED)`` if no set of the tree contains
              an occurrence of ``v``

            * ``(FULL, ALIGNED)`` if all the sets of the tree contain
              ``v``

            * ``(PARTIAL, ALIGNED)`` if some (but not all) of the sets
              contain ``v``, all of which are aligned
              to the right of the ordering at the end when the function ends

            * ``(PARTIAL, UNALIGNED)`` if some (but not all) of the
              sets contain ``v``, though it is impossible to align them
              all to the right

        In any case, the sets containing ``v`` are contiguous when this
        function ends. If there is no possibility of doing so, the function
        raises a :exc:`ValueError` exception.

        EXAMPLES:

        Ensuring the sets containing ``0`` are continuous::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = P([[0,3], [1,2], [2,3], [2,4], [4,0],[2,8], [2,9]])
            sage: p.set_contiguous(0)
            (1, True)
            sage: print(p)
            ('P', [{1, 2}, {2, 3}, {2, 4}, {8, 2}, {9, 2}, ('P', [{0, 3}, {0, 4}])])

        Impossible situation::

            sage: p = P([[0,1], [1,2], [2,3], [3,0]])
            sage: p.set_contiguous(0)
            (1, True)
            sage: p.set_contiguous(1)
            (1, True)
            sage: p.set_contiguous(2)
            (1, True)
            sage: p.set_contiguous(3)
            Traceback (most recent call last):
            ...
            ValueError: Impossible
        """
    def cardinality(self):
        """
        Return the number of orderings allowed by the structure.

        .. SEEALSO::

            :meth:`orderings` -- iterate over all admissible orderings

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = P([[0,3], [1,2], [2,3], [2,4], [4,0],[2,8], [2,9]])
            sage: p.cardinality()
            5040
            sage: p.set_contiguous(3)
            (1, True)
            sage: p.cardinality()
            1440
        """
    def orderings(self) -> Generator[Incomplete, Incomplete]:
        """
        Iterate over all orderings of the sets allowed by the structure.

        .. SEEALSO::

            :meth:`cardinality` -- return the number of orderings

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: p = P([[2,4], [1,2], [0,8], [0,5]])
            sage: for o in p.orderings():
            ....:    print(o)
            ({2, 4}, {1, 2}, {0, 8}, {0, 5})
            ({2, 4}, {1, 2}, {0, 5}, {0, 8})
            ({2, 4}, {0, 8}, {1, 2}, {0, 5})
            ({2, 4}, {0, 8}, {0, 5}, {1, 2})
            ...
        """

class Q(PQ):
    """
    A Q-Tree is a PQ-Tree whose children are ordered up to reversal.

    For more information, see the documentation of :mod:`sage.graphs.pq_trees`.
    """
    def set_contiguous(self, v):
        """
        Update ``self`` so that the sets containing ``v`` are
        contiguous for any admissible permutation of its subtrees.

        INPUT:

        - ``v`` -- an element of the ground set

        OUTPUT:

        According to the cases:

            * ``(EMPTY, ALIGNED)`` if no set of the tree contains
              an occurrence of ``v``

            * ``(FULL, ALIGNED)`` if all the sets of the tree contain
              ``v``

            * ``(PARTIAL, ALIGNED)`` if some (but not all) of the sets
              contain ``v``, all of which are aligned
              to the right of the ordering at the end when the function ends

            * ``(PARTIAL, UNALIGNED)`` if some (but not all) of the
              sets contain ``v``, though it is impossible to align them
              all to the right

        In any case, the sets containing ``v`` are contiguous when this
        function ends. If there is no possibility of doing so, the function
        raises a :exc:`ValueError` exception.

        EXAMPLES:

        Ensuring the sets containing ``0`` are continuous::

            sage: from sage.graphs.pq_trees import P, Q
            sage: q = Q([[2,3], Q([[3,0],[3,1]]), Q([[4,0],[4,5]])])
            sage: q.set_contiguous(0)
            (1, False)
            sage: print(q)
            ('Q', [{2, 3}, {1, 3}, {0, 3}, {0, 4}, {4, 5}])

        Impossible situation::

            sage: p = Q([[0,1], [1,2], [2,0]])
            sage: p.set_contiguous(0)
            Traceback (most recent call last):
            ...
            ValueError: Impossible
        """
    def cardinality(self):
        """
        Return the number of orderings allowed by the structure.

        .. SEEALSO::

            :meth:`orderings` -- iterate over all admissible orderings

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: q = Q([[0,3], [1,2], [2,3], [2,4], [4,0],[2,8], [2,9]])
            sage: q.cardinality()
            2
        """
    def orderings(self) -> Generator[Incomplete, Incomplete]:
        """
        Iterate over all orderings of the sets allowed by the structure.

        .. SEEALSO::

            :meth:`cardinality` -- return the number of orderings

        EXAMPLES::

            sage: from sage.graphs.pq_trees import P, Q
            sage: q = Q([[2,4], [1,2], [0,8], [0,5]])
            sage: for o in q.orderings():
            ....:    print(o)
            ({2, 4}, {1, 2}, {0, 8}, {0, 5})
            ({0, 5}, {0, 8}, {1, 2}, {2, 4})
        """
