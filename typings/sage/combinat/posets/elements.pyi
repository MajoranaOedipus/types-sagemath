from _typeshed import Incomplete
from sage.structure.element import Element as Element, have_same_parent as have_same_parent

class PosetElement(Element):
    element: Incomplete
    vertex: Incomplete
    def __init__(self, poset, element, vertex) -> None:
        """
        Establish the parent-child relationship between ``poset``
        and ``element``, where ``element`` is associated to the
        vertex ``vertex`` of the Hasse diagram of the poset.

        INPUT:

        - ``poset`` -- a poset object

        - ``element`` -- any object

        - ``vertex`` -- a vertex of the Hasse diagram of the poset

        TESTS::

            sage: from sage.combinat.posets.elements import PosetElement
            sage: P = Poset([[1,2],[4],[3],[4],[]], facade = False)
            sage: e = P(0)
            sage: e.parent() is P
            True
            sage: TestSuite(e).run()
        """
    def __hash__(self) -> int:
        """
        TESTS::

            sage: P = Poset([[1,2],[4],[3],[4],[]], facade = False)
            sage: e = P(0)
            sage: hash(e)
            0
        """
    def __eq__(self, other):
        '''
        TESTS::

            sage: P = Poset([["a","b"],["d"],["c"],["d"],[]], facade = False)
            sage: Q = Poset([["a","b"],["d"],["c"],[],[]], facade = False)
            sage: P(0).__eq__(P(4))
            False
            sage: from sage.combinat.posets.elements import PosetElement
            sage: PosetElement(P,0,"c") == PosetElement(P,0,"c")
            True
            sage: PosetElement(P,0,"c") == PosetElement(Q,0,"c")
            False
            sage: PosetElement(P,0,"b") == PosetElement(P,0,"c")
            False

        .. warning:: as an optimization, this only compares the parent
           and vertex, using the invariant that, in a proper poset
           element, ``self.element == other.element`` if and only
           ``self.vertex == other.vertex``::

            sage: PosetElement(P,1,"c") == PosetElement(P,0,"c")
            True

        Test that :issue:`12351` is fixed::

            sage: P(0) == int(0)
            False
        '''
    def __ne__(self, other):
        '''
        TESTS::

            sage: P = Poset([[1,2],[4],[3],[4],[]])
            sage: P = Poset([["a","b"],["d"],["c"],["d"],[]])
            sage: P(0).__ne__(P(4))
            True
            sage: from sage.combinat.posets.elements import PosetElement
            sage: PosetElement(P,0,"c") != PosetElement(P,0,"c")
            False
            sage: PosetElement(P,0,"b") != PosetElement(P,0,"c")
            True

        For this one, see comment in :meth:`__eq__`::

            sage: PosetElement(P,1,"c") != PosetElement(P,0,"c")
            False
        '''
    def __lt__(self, other):
        """
        TESTS::

            sage: dag = DiGraph({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: P = Poset(dag, facade = False)
            sage: P(0) < P(1)
            False
            sage: P(4) < P(1)
            False
            sage: P(0) < P(0)
            False
        """
    def __le__(self, other):
        """
        TESTS::

            sage: dag = DiGraph({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: P = Poset(dag, facade = False)
            sage: P(1) <= P(0)
            False
            sage: P(0) <= P(1)
            False
            sage: P(0) <= P(3)
            True
            sage: P(0) <= P(0)
            True
        """
    def __gt__(self, other):
        """
        TESTS::

            sage: dag = DiGraph({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: P = Poset(dag)
            sage: P(0).__gt__(P(5))
            False
            sage: P(5).__gt__(P(0))
            True
            sage: P(0).__gt__(P(0))
            False
        """
    def __ge__(self, other):
        """
        TESTS::

            sage: dag = DiGraph({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: P = Poset(dag)
            sage: P(0).__ge__(P(5))
            False
            sage: P(5).__ge__(P(0))
            True
            sage: P(0).__ge__(P(0))
            True
        """

class MeetSemilatticeElement(PosetElement):
    def __mul__(self, other):
        """
        Return the meet of ``self`` and ``other`` in the lattice.

        EXAMPLES::

            sage: D = posets.DiamondPoset(5, facade=False)
            sage: D(1) * D(2)
            0
            sage: D(1) * D(1)
            1
            sage: D(1) * D(0)
            0
            sage: D(1) * D(4)
            1
        """

class JoinSemilatticeElement(PosetElement):
    def __add__(self, other):
        """
        Return the join of ``self`` and ``other`` in the lattice.

        EXAMPLES::

            sage: D = posets.DiamondPoset(5,facade=False)
            sage: D(1) + D(2)
            4
            sage: D(1) + D(1)
            1
            sage: D(1) + D(4)
            4
            sage: D(1) + D(0)
            1
        """

class LatticePosetElement(MeetSemilatticeElement, JoinSemilatticeElement): ...
