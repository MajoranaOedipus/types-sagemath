from _typeshed import Incomplete
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import LazyFamily as LazyFamily
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.set_factories import ParentWithSetFactory as ParentWithSetFactory, SetFactory as SetFactory, TopMostParentPolicy as TopMostParentPolicy
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

MAX: int

class XYPairsFactory(SetFactory):
    """
    An example of set factory, for sets of pairs of integers.

    .. SEEALSO::

        :mod:`.set_factories` for an introduction to set factories.
    """
    def __call__(self, x=None, y=None, policy=None):
        """
        Construct the subset from constraints.

        Consider the set `S` of couples `(x,y)` with `x` and `y` in
        `I:=\\{0,1,2,3,4\\}`. Returns the subsets of element of `S` satisfying
        some constraints.

        INPUT:

        - ``x=a`` -- where ``a`` is an integer (default: ``None``)
        - ``y=b`` -- where ``b`` is an integer (default: ``None``)
        - ``policy`` -- the policy passed to the created set

        .. SEEALSO::

            :class:`.set_factories.SetFactoryPolicy`

        EXAMPLES:

        Let us first create the set factory::

            sage: from sage.structure.set_factories_example import XYPairsFactory
            sage: XYPairs = XYPairsFactory()

        One can then use the set factory to construct a set::

            sage: P = XYPairs(); P.list()
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

        .. NOTE::

            This function is actually the ``__call__`` method of
            :class:`XYPairsFactory`.

        TESTS::

            sage: TestSuite(P).run()
        """
    def add_constraints(self, cons, args_opts):
        """
        Add constraints to the set ``cons`` as per
        :meth:`SetFactory.add_constraints<.set_factories.SetFactory.add_constraints>`.

        This is a crude implementation for the sake of the demonstration which
        should not be taken as an example.

        EXAMPLES::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs.add_constraints((3,None), ((2,), {}))
            Traceback (most recent call last):
            ...
            ValueError: Duplicate value for constraints 'x': was 3 now 2
            sage: XYPairs.add_constraints((), ((2,), {}))
            (2, None)
            sage: XYPairs.add_constraints((), ((2,), {'y':3}))
            (2, 3)
        """

XYPairs: Incomplete

class XYPair(ElementWrapper):
    """
    A class for Elements `(x,y)` with `x` and `y` in `\\{0,1,2,3,4\\}`.

    EXAMPLES::

        sage: from sage.structure.set_factories_example import XYPair
        sage: p = XYPair(Parent(), (0,1)); p
        (0, 1)
        sage: p = XYPair(Parent(), (0,8))
        Traceback (most recent call last):
        ...
        ValueError: numbers must be in range(5)
    """
    def __init__(self, parent, value, check: bool = True) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs(); p = P.list()[0]
            sage: TestSuite(p).run()
        """

class AllPairs(ParentWithSetFactory, DisjointUnionEnumeratedSets):
    """
    This parent shows how one can use set factories together with
    :class:`DisjointUnionEnumeratedSets`.

    It is constructed as the disjoint union
    (:class:`DisjointUnionEnumeratedSets`) of :class:`Pairs_Y` parents:

    .. MATH::

        S := \\bigcup_{i = 0,1,..., 4} S^y

    .. WARNING::

        When writing a parent ``P`` as a disjoint union of a family of parents
        ``P_i``, the parents ``P_i`` must be constructed as facade parents for
        ``P``. As a consequence, it should be passed ``P.facade_policy()`` as
        policy argument. See the source code of :meth:`pairs_y` for an
        example.

    TESTS::

        sage: from sage.structure.set_factories_example import XYPairs
        sage: P = XYPairs(); P.list()
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    """
    def __init__(self, policy) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: TestSuite(XYPairs()).run()
        """
    def pairs_y(self, letter):
        """
        Construct the parent for the disjoint union.

        Construct a parent in :class:`Pairs_Y` as a facade parent for ``self``.

        This is an internal function which should be hidden from the user
        (typically under the name ``_pairs_y``. We put it here for
        documentation.

        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs, XYPair
            sage: S = XYPairs()
            sage: S1 = S.pairs_y(1); S1
            {(a, 1) | a in range(5)}
            sage: S.an_element().parent()
            AllPairs

            sage: from sage.structure.set_factories import SelfParentPolicy
            sage: selfpolicy = SelfParentPolicy(XYPairs, XYPair)
            sage: selfS = XYPairs(policy=selfpolicy)
            sage: selfS1 = selfS.pairs_y(1); selfS1
            {(a, 1) | a in range(5)}
            sage: S.an_element().parent() is selfS
            False
            sage: selfS.an_element().parent() is selfS
            True
        """
    def check_element(self, el, check) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs()
            sage: P.check_element(P.an_element(), True)
            sage: XYPairs()((7, 0))  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: numbers must be in range(5)
        """

class PairsX_(ParentWithSetFactory, UniqueRepresentation):
    """
    The set of pairs `(x, 0), (x, 1), ..., (x, 4)`.

    TESTS::

        sage: from sage.structure.set_factories_example import XYPairs
        sage: P = XYPairs(0); P.list()
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    """
    def __init__(self, x, policy) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: TestSuite(XYPairs(0)).run()
        """
    def an_element(self):
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs(x=0); P.an_element()
            (0, 0)
        """
    def check_element(self, el, check) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs(x=1)
            sage: P.check_element(P.an_element(), True)
            sage: XYPairs(x=1)((0, 0))  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: Wrong first coordinate
        """
    def __iter__(self):
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: list(XYPairs(x=1))
            [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
        """

class Pairs_Y(ParentWithSetFactory, DisjointUnionEnumeratedSets):
    """
    The set of pairs `(0, y), (1, y), ..., (4, y)`.

    It is constructed as the disjoint union
    (:class:`DisjointUnionEnumeratedSets`) of :class:`SingletonPair` parents:

    .. MATH::

        S^y := \\bigcup_{i = 0,1,..., 4} S_i^y

    .. SEEALSO::

        :class:`AllPairs` for how to properly construct
        :class:`DisjointUnionEnumeratedSets` using
        :class:`~sage.structure.set_factories.ParentWithSetFactory`.

    TESTS::

        sage: from sage.structure.set_factories_example import XYPairs
        sage: P = XYPairs(y=1); P.list()
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
    """
    def __init__(self, y, policy) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: TestSuite(XYPairs(y=1)).run()
        """
    def an_element(self):
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs(y=1).an_element()
            (0, 1)
        """
    def single_pair(self, letter):
        """
        Construct the singleton pair parent.

        Construct a singleton pair for ``(self.y, letter)`` as a facade parent
        for ``self``.

        .. SEEALSO::

            :class:`AllPairs` for how to properly construct
            :class:`DisjointUnionEnumeratedSets` using
            :class:`~sage.structure.set_factories.ParentWithSetFactory`.

        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs(y=1)
            sage: P.single_pair(0)
            {(0, 1)}
            sage: P.single_pair(0).an_element().parent()
            AllPairs
        """
    def check_element(self, el, check) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: P = XYPairs(y=1)
            sage: P.check_element(P.an_element(), True)
            sage: XYPairs(y=1)((1, 0))  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: Wrong second coordinate
        """

class SingletonPair(ParentWithSetFactory, UniqueRepresentation):
    """
    TESTS::

        sage: from sage.structure.set_factories_example import XYPairs
        sage: P = XYPairs(0,1); P.list()
        [(0, 1)]
    """
    def __init__(self, x, y, policy) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: TestSuite(XYPairs(0,1)).run()
        """
    def check_element(self, el, check) -> None:
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: XYPairs(0,1).check_element(XYPairs()((0,1)), True)
            sage: XYPairs(0,1).check_element(XYPairs()((1,0)), True)
            Traceback (most recent call last):
            ...
            ValueError: Wrong coordinate
            sage: XYPairs(0,1)((1,1))
            Traceback (most recent call last):
            ...
            ValueError: Wrong coordinate
        """
    def __iter__(self):
        """
        TESTS::

            sage: from sage.structure.set_factories_example import XYPairs
            sage: list(XYPairs(0,1))
            [(0, 1)]
        """
