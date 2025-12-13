import _cython_3_2_1
import sage.structure.parent
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.prandom import randint as randint
from typing import Any, ClassVar, overload

RecursivelyEnumeratedSet: _cython_3_2_1.cython_function_or_method
search_forest_iterator: _cython_3_2_1.cython_function_or_method

class RecursivelyEnumeratedSet_forest(sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1551)

        The enumerated set of the nodes of the forest having the given
        ``roots``, and where ``children(x)`` returns the children of the
        node ``x`` of the forest.

        See also :class:`sage.combinat.backtrack.GenericBacktracker`,
        :class:`RecursivelyEnumeratedSet_graded`, and
        :class:`RecursivelyEnumeratedSet_symmetric`.

        INPUT:

        - ``roots`` -- list (or iterable)
        - ``children`` -- a function returning a list (or iterable, or iterator)
        - ``post_process`` -- a function defined over the nodes of the
          forest (default: no post processing)
        - ``algorithm`` -- ``'depth'`` or ``'breadth'`` (default: ``'depth'``)
        - ``category`` -- a category (default: :class:`EnumeratedSets`)

        The option ``post_process`` allows for customizing the nodes that
        are actually produced. Furthermore, if ``f(x)`` returns ``None``,
        then ``x`` won't be output at all.

        EXAMPLES:

        We construct the set of all binary sequences of length at most
        three, and list them::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest( [[]],
            ....:     lambda l: [l + [0], l + [1]] if len(l) < 3 else [],
            ....:     category=FiniteEnumeratedSets())
            sage: S.list()
            [[],
             [0], [0, 0], [0, 0, 0], [0, 0, 1], [0, 1], [0, 1, 0], [0, 1, 1],
             [1], [1, 0], [1, 0, 0], [1, 0, 1], [1, 1], [1, 1, 0], [1, 1, 1]]

        ``RecursivelyEnumeratedSet_forest`` needs to be explicitly told that the set is
        finite for the following to work::

            sage: S.category()
            Category of finite enumerated sets
            sage: S.cardinality()
            15

        We proceed with the set of all lists of letters in ``0,1,2``
        without repetitions, ordered by increasing length (i.e. using a
        breadth first search through the tree)::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: tb = RecursivelyEnumeratedSet_forest( [[]],
            ....:       lambda l: [l + [i] for i in range(3) if i not in l],
            ....:       algorithm = 'breadth',
            ....:       category=FiniteEnumeratedSets())
            sage: tb[0]
            []
            sage: tb.cardinality()
            16
            sage: list(tb)
            [[],
             [0], [1], [2],
             [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1],
             [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

        For infinite sets, this option should be set carefully to ensure
        that all elements are actually generated. The following example
        builds the set of all ordered pairs `(i,j)` of nonnegative
        integers such that `j\\leq 1`::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: I = RecursivelyEnumeratedSet_forest([(0,0)],
            ....:                  lambda l: [(l[0]+1, l[1]), (l[0], 1)]
            ....:                            if l[1] == 0 else [(l[0], l[1]+1)])

        With a depth first search, only the elements of the form `(i,0)`
        are generated::

            sage: depth_search = I.depth_first_search_iterator()
            sage: [next(depth_search) for i in range(7)]
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]

        Using instead breadth first search gives the usual anti-diagonal
        iterator::

            sage: breadth_search = I.breadth_first_search_iterator()
            sage: [next(breadth_search) for i in range(15)]
            [(0, 0),
             (1, 0), (0, 1),
             (2, 0), (1, 1), (0, 2),
             (3, 0), (2, 1), (1, 2), (0, 3),
             (4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]

        .. rubric:: Deriving subclasses

        The class of a parent `A` may derive from :class:`RecursivelyEnumeratedSet_forest` so
        that `A` can benefit from enumeration tools. As a running example,
        we consider the problem of enumerating integers whose binary
        expansion have at most three nonzero digits. For example, `3 =
        2^1 + 2^0` has two nonzero digits. `15 = 2^3 + 2^2 + 2^1 + 2^0`
        has four nonzero digits. In fact, `15` is the smallest integer
        which is not in the enumerated set.

        To achieve this, we use ``RecursivelyEnumeratedSet_forest`` to enumerate binary tuples
        with at most three nonzero digits, apply a post processing to
        recover the corresponding integers, and discard tuples finishing
        by zero.

        A first approach is to pass the ``roots`` and ``children``
        functions as arguments to :meth:`RecursivelyEnumeratedSet_forest.__init__`::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: class A(UniqueRepresentation, RecursivelyEnumeratedSet_forest):
            ....:     def __init__(self):
            ....:         RecursivelyEnumeratedSet_forest.__init__(self, [()],
            ....:             lambda x: [x + (0,), x + (1,)] if sum(x) < 3 else [],
            ....:             lambda x: sum(x[i]*2^i for i in range(len(x)))
            ....:                           if sum(x) != 0 and x[-1] != 0 else None,
            ....:             algorithm='breadth',
            ....:             category=InfiniteEnumeratedSets())
            sage: MyForest = A(); MyForest
            An enumerated set with a forest structure
            sage: MyForest.category()
            Category of infinite enumerated sets
            sage: p = iter(MyForest)
            sage: [next(p) for i in range(30)]
            [1, 2, 3, 4, 6, 5, 7, 8, 12, 10, 14, 9, 13, 11, 16, 24,
             20, 28, 18, 26, 22, 17, 25, 21, 19, 32, 48, 40, 56, 36]

        An alternative approach is to implement ``roots`` and ``children``
        as methods of the subclass (in fact they could also be attributes
        of `A`). Namely, ``A.roots()`` must return an iterable containing
        the enumeration generators, and ``A.children(x)`` must return an
        iterable over the children of `x`. Optionally, `A` can have a
        method or attribute such that ``A.post_process(x)`` returns the
        desired output for the node ``x`` of the tree::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: class A(UniqueRepresentation, RecursivelyEnumeratedSet_forest):
            ....:     def __init__(self):
            ....:         RecursivelyEnumeratedSet_forest.__init__(self, algorithm='breadth',
            ....:                               category=InfiniteEnumeratedSets())
            ....:     def roots(self):
            ....:         return [()]
            ....:     def children(self, x):
            ....:         if sum(x) < 3:
            ....:             return [x + (0,), x + (1,)]
            ....:         else:
            ....:             return []
            ....:     def post_process(self, x):
            ....:         if sum(x) == 0 or x[-1] == 0:
            ....:             return None
            ....:         else:
            ....:             return sum(x[i]*2^i for i in range(len(x)))
            sage: MyForest = A(); MyForest
            An enumerated set with a forest structure
            sage: MyForest.category()
            Category of infinite enumerated sets
            sage: p = iter(MyForest)
            sage: [next(p) for i in range(30)]
            [1, 2, 3, 4, 6, 5, 7, 8, 12, 10, 14, 9, 13, 11, 16, 24,
             20, 28, 18, 26, 22, 17, 25, 21, 19, 32, 48, 40, 56, 36]

        .. warning::

            A :class:`RecursivelyEnumeratedSet_forest` instance is picklable if and only if
            the input functions are themselves picklable. This excludes
            anonymous or interactively defined functions::

                sage: def children(x):
                ....:     return [x + 1]
                sage: S = RecursivelyEnumeratedSet_forest([1], children, category=InfiniteEnumeratedSets())
                sage: dumps(S)
                Traceback (most recent call last):
                ...
                PicklingError: Can't pickle <...function...>: attribute lookup ... failed

            Let us now fake ``children`` being defined in a Python module::

                sage: import __main__
                sage: __main__.children = children
                sage: S = RecursivelyEnumeratedSet_forest([1], children, category=InfiniteEnumeratedSets())
                sage: loads(dumps(S))
                An enumerated set with a forest structure
    """
    __len__: ClassVar[None] = ...
    def __init__(self, roots=..., children=..., post_process=..., algorithm=..., facade=..., category=...) -> Any:
        """RecursivelyEnumeratedSet_forest.__init__(self, roots=None, children=None, post_process=None, algorithm='depth', facade=None, category=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1735)

        TESTS::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest(NN, lambda x: [], lambda x: x^2 if x.is_prime() else None)
            sage: S.category()
            Category of enumerated sets"""
    @overload
    def breadth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_forest.breadth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1847)

        Return a breadth first search iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: f = RecursivelyEnumeratedSet_forest([[]],
            ....:                  lambda l: [l+[0], l+[1]] if len(l) < 3 else [])
            sage: list(f.breadth_first_search_iterator())
            [[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
            sage: S = RecursivelyEnumeratedSet_forest([(0,0)],
            ....: lambda x : [(x[0], x[1]+1)] if x[1] != 0 else [(x[0]+1,0), (x[0],1)],
            ....: post_process = lambda x: x if ((is_prime(x[0]) and is_prime(x[1])) and ((x[0] - x[1]) == 2)) else None)
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(5, 3), (7, 5), (13, 11), (19, 17), (31, 29), (43, 41), (61, 59)]"""
    @overload
    def breadth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_forest.breadth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1847)

        Return a breadth first search iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: f = RecursivelyEnumeratedSet_forest([[]],
            ....:                  lambda l: [l+[0], l+[1]] if len(l) < 3 else [])
            sage: list(f.breadth_first_search_iterator())
            [[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
            sage: S = RecursivelyEnumeratedSet_forest([(0,0)],
            ....: lambda x : [(x[0], x[1]+1)] if x[1] != 0 else [(x[0]+1,0), (x[0],1)],
            ....: post_process = lambda x: x if ((is_prime(x[0]) and is_prime(x[1])) and ((x[0] - x[1]) == 2)) else None)
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(5, 3), (7, 5), (13, 11), (19, 17), (31, 29), (43, 41), (61, 59)]"""
    @overload
    def breadth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_forest.breadth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1847)

        Return a breadth first search iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: f = RecursivelyEnumeratedSet_forest([[]],
            ....:                  lambda l: [l+[0], l+[1]] if len(l) < 3 else [])
            sage: list(f.breadth_first_search_iterator())
            [[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
            sage: S = RecursivelyEnumeratedSet_forest([(0,0)],
            ....: lambda x : [(x[0], x[1]+1)] if x[1] != 0 else [(x[0]+1,0), (x[0],1)],
            ....: post_process = lambda x: x if ((is_prime(x[0]) and is_prime(x[1])) and ((x[0] - x[1]) == 2)) else None)
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(5, 3), (7, 5), (13, 11), (19, 17), (31, 29), (43, 41), (61, 59)]"""
    def children(self, x) -> Any:
        """RecursivelyEnumeratedSet_forest.children(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1783)

        Return the children of the element ``x``.

        The result can be a list, an iterable, an iterator, or even a
        generator.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: I = RecursivelyEnumeratedSet_forest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.children((0,0))]
            [(1, 0), (0, 1)]
            sage: [i for i in I.children((1,0))]
            [(2, 0), (1, 1)]
            sage: [i for i in I.children((1,1))]
            [(1, 2)]
            sage: [i for i in I.children((4,1))]
            [(4, 2)]
            sage: [i for i in I.children((4,0))]
            [(5, 0), (4, 1)]"""
    @overload
    def depth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_forest.depth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1832)

        Return a depth first search iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: f = RecursivelyEnumeratedSet_forest([[]],
            ....:                  lambda l: [l + [0], l + [1]] if len(l) < 3 else [])
            sage: list(f.depth_first_search_iterator())
            [[], [0], [0, 0], [0, 0, 0], [0, 0, 1], [0, 1], [0, 1, 0], [0, 1, 1],
                 [1], [1, 0], [1, 0, 0], [1, 0, 1], [1, 1], [1, 1, 0], [1, 1, 1]]"""
    @overload
    def depth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_forest.depth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1832)

        Return a depth first search iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: f = RecursivelyEnumeratedSet_forest([[]],
            ....:                  lambda l: [l + [0], l + [1]] if len(l) < 3 else [])
            sage: list(f.depth_first_search_iterator())
            [[], [0], [0, 0], [0, 0, 0], [0, 0, 1], [0, 1], [0, 1, 0], [0, 1, 1],
                 [1], [1, 0], [1, 0, 0], [1, 0, 1], [1, 1], [1, 1, 0], [1, 1, 1]]"""
    def elements_of_depth_iterator(self, depth=...) -> Any:
        """RecursivelyEnumeratedSet_forest.elements_of_depth_iterator(self, depth=0)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1901)

        Return an iterator over the elements of ``self`` of given depth.
        An element of depth `n` can be obtained by applying the
        children function `n` times from a root.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest([(0,0)] ,
            ....:        lambda x : [(x[0], x[1]+1)] if x[1] != 0 else [(x[0]+1,0), (x[0],1)],
            ....:        post_process = lambda x: x if ((is_prime(x[0]) and is_prime(x[1]))
            ....:                                        and ((x[0] - x[1]) == 2)) else None)
            sage: p = S.elements_of_depth_iterator(8)
            sage: next(p)
            (5, 3)
            sage: S = RecursivelyEnumeratedSet_forest(NN, lambda x : [],
            ....:                      lambda x: x^2 if x.is_prime() else None)
            sage: p = S.elements_of_depth_iterator(0)
            sage: [next(p), next(p), next(p), next(p), next(p)]
            [4, 9, 25, 49, 121]"""
    @overload
    def map_reduce(self, map_function=..., reduce_function=..., reduce_init=...) -> Any:
        """RecursivelyEnumeratedSet_forest.map_reduce(self, map_function=None, reduce_function=None, reduce_init=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 2022)

        Apply a Map/Reduce algorithm on ``self``.

        INPUT:

        - ``map_function`` -- a function from the element of ``self`` to some
          set with a reduce operation (e.g.: a monoid). The default value is
          the constant function ``1``.

        - ``reduce_function`` -- the reduce function (e.g.: the addition of a
          monoid); the default value is ``+``

        - ``reduce_init`` -- the initialisation of the reduction (e.g.: the
          neutral element of the monoid); the default value is ``0``

        .. NOTE::

            the effect of the default values is to compute the cardinality
            of ``self``.

        EXAMPLES::

            sage: seeds = [([i], i, i) for i in range(1, 10)]
            sage: def succ(t):
            ....:     list, sum, last = t
            ....:     return [(list + [i], sum + i, i) for i in range(1, last)]
            sage: F = RecursivelyEnumeratedSet(seeds, succ,
            ....:         structure='forest', enumeration='depth')

            sage: # needs sage.symbolic
            sage: y = var('y')
            sage: def map_function(t):
            ....:     li, sum, _ = t
            ....:     return y ^ sum
            sage: def reduce_function(x, y):
            ....:     return x + y
            sage: F.map_reduce(map_function, reduce_function, 0)
            y^45 + y^44 + y^43 + 2*y^42 + 2*y^41 + 3*y^40 + 4*y^39 + 5*y^38 + 6*y^37
            + 8*y^36 + 9*y^35 + 10*y^34 + 12*y^33 + 13*y^32 + 15*y^31 + 17*y^30
            + 18*y^29 + 19*y^28 + 21*y^27 + 21*y^26 + 22*y^25 + 23*y^24 + 23*y^23
            + 23*y^22 + 23*y^21 + 22*y^20 + 21*y^19 + 21*y^18 + 19*y^17 + 18*y^16
            + 17*y^15 + 15*y^14 + 13*y^13 + 12*y^12 + 10*y^11 + 9*y^10 + 8*y^9 + 6*y^8
            + 5*y^7 + 4*y^6 + 3*y^5 + 2*y^4 + 2*y^3 + y^2 + y

        Here is an example with the default values::

            sage: F.map_reduce()
            511

        .. SEEALSO:: :mod:`sage.parallel.map_reduce`"""
    @overload
    def map_reduce(self) -> Any:
        """RecursivelyEnumeratedSet_forest.map_reduce(self, map_function=None, reduce_function=None, reduce_init=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 2022)

        Apply a Map/Reduce algorithm on ``self``.

        INPUT:

        - ``map_function`` -- a function from the element of ``self`` to some
          set with a reduce operation (e.g.: a monoid). The default value is
          the constant function ``1``.

        - ``reduce_function`` -- the reduce function (e.g.: the addition of a
          monoid); the default value is ``+``

        - ``reduce_init`` -- the initialisation of the reduction (e.g.: the
          neutral element of the monoid); the default value is ``0``

        .. NOTE::

            the effect of the default values is to compute the cardinality
            of ``self``.

        EXAMPLES::

            sage: seeds = [([i], i, i) for i in range(1, 10)]
            sage: def succ(t):
            ....:     list, sum, last = t
            ....:     return [(list + [i], sum + i, i) for i in range(1, last)]
            sage: F = RecursivelyEnumeratedSet(seeds, succ,
            ....:         structure='forest', enumeration='depth')

            sage: # needs sage.symbolic
            sage: y = var('y')
            sage: def map_function(t):
            ....:     li, sum, _ = t
            ....:     return y ^ sum
            sage: def reduce_function(x, y):
            ....:     return x + y
            sage: F.map_reduce(map_function, reduce_function, 0)
            y^45 + y^44 + y^43 + 2*y^42 + 2*y^41 + 3*y^40 + 4*y^39 + 5*y^38 + 6*y^37
            + 8*y^36 + 9*y^35 + 10*y^34 + 12*y^33 + 13*y^32 + 15*y^31 + 17*y^30
            + 18*y^29 + 19*y^28 + 21*y^27 + 21*y^26 + 22*y^25 + 23*y^24 + 23*y^23
            + 23*y^22 + 23*y^21 + 22*y^20 + 21*y^19 + 21*y^18 + 19*y^17 + 18*y^16
            + 17*y^15 + 15*y^14 + 13*y^13 + 12*y^12 + 10*y^11 + 9*y^10 + 8*y^9 + 6*y^8
            + 5*y^7 + 4*y^6 + 3*y^5 + 2*y^4 + 2*y^3 + y^2 + y

        Here is an example with the default values::

            sage: F.map_reduce()
            511

        .. SEEALSO:: :mod:`sage.parallel.map_reduce`"""
    @overload
    def roots(self) -> Any:
        """RecursivelyEnumeratedSet_forest.roots(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1767)

        Return an iterable over the roots of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: I = RecursivelyEnumeratedSet_forest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0)]
            sage: I = RecursivelyEnumeratedSet_forest([(0,0),(1,1)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0), (1, 1)]"""
    @overload
    def roots(self) -> Any:
        """RecursivelyEnumeratedSet_forest.roots(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1767)

        Return an iterable over the roots of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: I = RecursivelyEnumeratedSet_forest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0)]
            sage: I = RecursivelyEnumeratedSet_forest([(0,0),(1,1)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0), (1, 1)]"""
    @overload
    def roots(self) -> Any:
        """RecursivelyEnumeratedSet_forest.roots(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1767)

        Return an iterable over the roots of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: I = RecursivelyEnumeratedSet_forest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0)]
            sage: I = RecursivelyEnumeratedSet_forest([(0,0),(1,1)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)])
            sage: [i for i in I.roots()]
            [(0, 0), (1, 1)]"""
    @overload
    def __contains__(self, elt) -> Any:
        """RecursivelyEnumeratedSet_forest.__contains__(self, elt)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1928)

        Return ``True`` if ``elt`` is in ``self``.

        .. warning::

           This is achieved by iterating through the elements until
           ``elt`` is found. In particular, this method will never
           stop when ``elt`` is not in ``self`` and ``self`` is
           infinite.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest([[]], lambda l: [l + [0], l + [1]] if len(l) < 3 else [],
            ....:                                     category=FiniteEnumeratedSets())
            sage: [4] in S
            False
            sage: [1] in S
            True
            sage: [1,1,1,1] in S
            False
            sage: all(S.__contains__(i) for i in iter(S))
            True
            sage: S = RecursivelyEnumeratedSet_forest([1], lambda x: [x + 1], category=InfiniteEnumeratedSets())
            sage: 1 in S
            True
            sage: 732 in S
            True
            sage: -1 in S  # not tested : Will never stop

        The algorithm uses a random enumeration of the nodes of the
        forest. This choice was motivated by examples in which both
        depth first search and breadth first search failed. The
        following example enumerates all ordered pairs of nonnegative
        integers, starting from an infinite set of roots, where each
        root has an infinite number of children::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest(
            ....:         Family(NN, lambda x: (x, 0)),
            ....:         lambda x: Family(PositiveIntegers(), lambda y: (x[0], y)) if x[1] == 0 else [])
            sage: p = S.depth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
            sage: (0,0) in S
            True
            sage: (1,1) in S
            True
            sage: (10,10) in S
            True
            sage: (42,18) in S
            True

        We now consider the same set of all ordered pairs of
        nonnegative integers but constructed in a different way. There
        still are infinitely many roots, but each node has a single
        child. From each root starts an infinite branch of breadth
        `1`::

            sage: S = RecursivelyEnumeratedSet_forest(Family(NN, lambda x: (x, 0)),
            ....:                                     lambda x: [(x[0], x[1] + 1)])
            sage: p = S.depth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
            sage: (0,0) in S
            True
            sage: (1,1) in S
            True
            sage: (10,10) in S
            True
            sage: (37,11) in S
            True"""
    @overload
    def __contains__(self, i) -> Any:
        """RecursivelyEnumeratedSet_forest.__contains__(self, elt)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1928)

        Return ``True`` if ``elt`` is in ``self``.

        .. warning::

           This is achieved by iterating through the elements until
           ``elt`` is found. In particular, this method will never
           stop when ``elt`` is not in ``self`` and ``self`` is
           infinite.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest([[]], lambda l: [l + [0], l + [1]] if len(l) < 3 else [],
            ....:                                     category=FiniteEnumeratedSets())
            sage: [4] in S
            False
            sage: [1] in S
            True
            sage: [1,1,1,1] in S
            False
            sage: all(S.__contains__(i) for i in iter(S))
            True
            sage: S = RecursivelyEnumeratedSet_forest([1], lambda x: [x + 1], category=InfiniteEnumeratedSets())
            sage: 1 in S
            True
            sage: 732 in S
            True
            sage: -1 in S  # not tested : Will never stop

        The algorithm uses a random enumeration of the nodes of the
        forest. This choice was motivated by examples in which both
        depth first search and breadth first search failed. The
        following example enumerates all ordered pairs of nonnegative
        integers, starting from an infinite set of roots, where each
        root has an infinite number of children::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: S = RecursivelyEnumeratedSet_forest(
            ....:         Family(NN, lambda x: (x, 0)),
            ....:         lambda x: Family(PositiveIntegers(), lambda y: (x[0], y)) if x[1] == 0 else [])
            sage: p = S.depth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
            sage: (0,0) in S
            True
            sage: (1,1) in S
            True
            sage: (10,10) in S
            True
            sage: (42,18) in S
            True

        We now consider the same set of all ordered pairs of
        nonnegative integers but constructed in a different way. There
        still are infinitely many roots, but each node has a single
        child. From each root starts an infinite branch of breadth
        `1`::

            sage: S = RecursivelyEnumeratedSet_forest(Family(NN, lambda x: (x, 0)),
            ....:                                     lambda x: [(x[0], x[1] + 1)])
            sage: p = S.depth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
            sage: p = S.breadth_first_search_iterator()
            sage: [next(p), next(p), next(p), next(p), next(p), next(p), next(p)]
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
            sage: (0,0) in S
            True
            sage: (1,1) in S
            True
            sage: (10,10) in S
            True
            sage: (37,11) in S
            True"""
    @overload
    def __iter__(self) -> Any:
        """RecursivelyEnumeratedSet_forest.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1807)

        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: def children(l):
            ....:      return [l + [0], l + [1]]
            sage: C = RecursivelyEnumeratedSet_forest(([],), children)
            sage: f = C.__iter__()
            sage: next(f)
            []
            sage: next(f)
            [0]
            sage: next(f)
            [0, 0]"""
    @overload
    def __iter__(self) -> Any:
        """RecursivelyEnumeratedSet_forest.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1807)

        Return an iterator over the elements of ``self``.

        EXAMPLES::

            sage: from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest
            sage: def children(l):
            ....:      return [l + [0], l + [1]]
            sage: C = RecursivelyEnumeratedSet_forest(([],), children)
            sage: f = C.__iter__()
            sage: next(f)
            []
            sage: next(f)
            [0]
            sage: next(f)
            [0, 0]"""

class RecursivelyEnumeratedSet_generic(sage.structure.parent.Parent):
    """RecursivelyEnumeratedSet_generic(seeds, successors, enumeration='depth', max_depth=float('inf'), post_process=None, facade=None, category=None)

    File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 432)

    A generic recursively enumerated set.

    For more information, see :func:`RecursivelyEnumeratedSet`.

    EXAMPLES::

        sage: f = lambda a:[a+1]

    Different structure for the sets::

        sage: RecursivelyEnumeratedSet([0], f, structure=None)
        A recursively enumerated set (breadth first search)
        sage: RecursivelyEnumeratedSet([0], f, structure='graded')
        A recursively enumerated set with a graded structure (breadth first search)
        sage: RecursivelyEnumeratedSet([0], f, structure='symmetric')
        A recursively enumerated set with a symmetric structure (breadth first search)
        sage: RecursivelyEnumeratedSet([0], f, structure='forest')
        An enumerated set with a forest structure

    Different default enumeration algorithms::

        sage: RecursivelyEnumeratedSet([0], f, enumeration='breadth')
        A recursively enumerated set (breadth first search)
        sage: RecursivelyEnumeratedSet([0], f, enumeration='naive')
        A recursively enumerated set (naive search)
        sage: RecursivelyEnumeratedSet([0], f, enumeration='depth')
        A recursively enumerated set (depth first search)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    successors: successors
    def __init__(self, seeds, successors, enumeration=..., max_depth=..., post_process=..., facade=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 462)

                TESTS::

                    sage: f = lambda a: [a+3, a+5]
                    sage: C = RecursivelyEnumeratedSet([0], f)
                    sage: C
                    A recursively enumerated set (breadth first search)
        """
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_generic.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 773)

        Iterate on the elements of ``self`` (breadth first).

        This code remembers every element generated.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.breadth_first_search_iterator()
            sage: [next(it) for _ in range(10)]
            [0, 3, 5, 6, 8, 10, 9, 11, 13, 15]"""
    @overload
    def breadth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_generic.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 773)

        Iterate on the elements of ``self`` (breadth first).

        This code remembers every element generated.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.breadth_first_search_iterator()
            sage: [next(it) for _ in range(10)]
            [0, 3, 5, 6, 8, 10, 9, 11, 13, 15]"""
    @overload
    def depth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_generic.depth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 872)

        Iterate on the elements of ``self`` (depth first).

        This code remembers every element generated.

        The elements are traversed right-to-left, so the last element returned
        by the successor function is visited first.

        See :wikipedia:`Depth-first_search`.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.depth_first_search_iterator()
            sage: [next(it) for _ in range(10)]
            [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]"""
    @overload
    def depth_first_search_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_generic.depth_first_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 872)

        Iterate on the elements of ``self`` (depth first).

        This code remembers every element generated.

        The elements are traversed right-to-left, so the last element returned
        by the successor function is visited first.

        See :wikipedia:`Depth-first_search`.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.depth_first_search_iterator()
            sage: [next(it) for _ in range(10)]
            [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]"""
    def elements_of_depth_iterator(self, depth) -> Any:
        """RecursivelyEnumeratedSet_generic.elements_of_depth_iterator(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 750)

        Iterate over the elements of ``self`` of given depth.

        An element of depth `n` can be obtained by applying the
        successor function `n` times to a seed.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: an iterator

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.elements_of_depth_iterator(2)
            sage: sorted(it)
            [3, 7, 8, 12]"""
    def graded_component(self, depth) -> Any:
        """RecursivelyEnumeratedSet_generic.graded_component(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 721)

        Return the graded component of given depth.

        This method caches each lower graded component.

        A graded component is a set of elements of the same depth where the
        depth of an element is its minimal distance to a root.

        It is currently implemented only for graded or symmetric structure.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: set

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: C.graded_component(0)
            Traceback (most recent call last):
            ...
            NotImplementedError: graded_component_iterator method currently implemented only for graded or symmetric structure"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_generic.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 702)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        It is currently implemented only for graded or symmetric structure.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.graded_component_iterator()    # todo: not implemented"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_generic.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 702)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        It is currently implemented only for graded or symmetric structure.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: it = C.graded_component_iterator()    # todo: not implemented"""
    @overload
    def naive_search_iterator(self) -> Any:
        '''RecursivelyEnumeratedSet_generic.naive_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 843)

        Iterate on the elements of ``self`` (in no particular order).

        This code remembers every element generated.

        TESTS:

        We compute all the permutations of 3::

            sage: # needs sage.combinat
            sage: seeds = [Permutation([1,2,3])]
            sage: succ = attrcall("permutohedron_succ")
            sage: R = RecursivelyEnumeratedSet(seeds, succ)
            sage: sorted(R.naive_search_iterator())
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]'''
    @overload
    def naive_search_iterator(self) -> Any:
        '''RecursivelyEnumeratedSet_generic.naive_search_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 843)

        Iterate on the elements of ``self`` (in no particular order).

        This code remembers every element generated.

        TESTS:

        We compute all the permutations of 3::

            sage: # needs sage.combinat
            sage: seeds = [Permutation([1,2,3])]
            sage: succ = attrcall("permutohedron_succ")
            sage: R = RecursivelyEnumeratedSet(seeds, succ)
            sage: sorted(R.naive_search_iterator())
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]'''
    @overload
    def seeds(self) -> Any:
        """RecursivelyEnumeratedSet_generic.seeds(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 673)

        Return an iterable over the seeds of ``self``.

        EXAMPLES::

            sage: R = RecursivelyEnumeratedSet([1], lambda x: [x + 1, x - 1])
            sage: R.seeds()
            [1]"""
    @overload
    def seeds(self) -> Any:
        """RecursivelyEnumeratedSet_generic.seeds(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 673)

        Return an iterable over the seeds of ``self``.

        EXAMPLES::

            sage: R = RecursivelyEnumeratedSet([1], lambda x: [x + 1, x - 1])
            sage: R.seeds()
            [1]"""
    @overload
    def to_digraph(self, max_depth=..., loops=..., multiedges=...) -> Any:
        """RecursivelyEnumeratedSet_generic.to_digraph(self, max_depth=None, loops=True, multiedges=True)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 904)

        Return the directed graph of the recursively enumerated set.

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth for which outgoing edges of elements are computed
        - ``loops`` -- boolean (default: ``True``); option for the digraph
        - ``multiedges`` -- boolean (default: ``True``); option of the digraph

        OUTPUT: a directed graph

        .. WARNING::

            If the set is infinite, this will loop forever unless ``max_depth``
            is finite.

        EXAMPLES::

            sage: child = lambda i: [(i+3) % 10, (i+8) % 10]
            sage: R = RecursivelyEnumeratedSet([0], child)
            sage: R.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 10 vertices

        Digraph of a recursively enumerated set with a symmetric structure of
        infinite cardinality using ``max_depth`` argument::

            sage: succ = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: seeds = [(0,0)]
            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric')
            sage: C.to_digraph(max_depth=3)                                             # needs sage.graphs
            Looped multi-digraph on 41 vertices

        The ``max_depth`` argument can be given at the creation of the set::

            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric',
            ....:                              max_depth=2)
            sage: C.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 25 vertices

        Digraph of a recursively enumerated set with a graded structure::

            sage: f = lambda a: [a+1, a+I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: C.to_digraph(max_depth=4)                                             # needs sage.graphs
            Looped multi-digraph on 21 vertices"""
    @overload
    def to_digraph(self) -> Any:
        """RecursivelyEnumeratedSet_generic.to_digraph(self, max_depth=None, loops=True, multiedges=True)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 904)

        Return the directed graph of the recursively enumerated set.

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth for which outgoing edges of elements are computed
        - ``loops`` -- boolean (default: ``True``); option for the digraph
        - ``multiedges`` -- boolean (default: ``True``); option of the digraph

        OUTPUT: a directed graph

        .. WARNING::

            If the set is infinite, this will loop forever unless ``max_depth``
            is finite.

        EXAMPLES::

            sage: child = lambda i: [(i+3) % 10, (i+8) % 10]
            sage: R = RecursivelyEnumeratedSet([0], child)
            sage: R.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 10 vertices

        Digraph of a recursively enumerated set with a symmetric structure of
        infinite cardinality using ``max_depth`` argument::

            sage: succ = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: seeds = [(0,0)]
            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric')
            sage: C.to_digraph(max_depth=3)                                             # needs sage.graphs
            Looped multi-digraph on 41 vertices

        The ``max_depth`` argument can be given at the creation of the set::

            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric',
            ....:                              max_depth=2)
            sage: C.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 25 vertices

        Digraph of a recursively enumerated set with a graded structure::

            sage: f = lambda a: [a+1, a+I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: C.to_digraph(max_depth=4)                                             # needs sage.graphs
            Looped multi-digraph on 21 vertices"""
    @overload
    def to_digraph(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_generic.to_digraph(self, max_depth=None, loops=True, multiedges=True)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 904)

        Return the directed graph of the recursively enumerated set.

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth for which outgoing edges of elements are computed
        - ``loops`` -- boolean (default: ``True``); option for the digraph
        - ``multiedges`` -- boolean (default: ``True``); option of the digraph

        OUTPUT: a directed graph

        .. WARNING::

            If the set is infinite, this will loop forever unless ``max_depth``
            is finite.

        EXAMPLES::

            sage: child = lambda i: [(i+3) % 10, (i+8) % 10]
            sage: R = RecursivelyEnumeratedSet([0], child)
            sage: R.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 10 vertices

        Digraph of a recursively enumerated set with a symmetric structure of
        infinite cardinality using ``max_depth`` argument::

            sage: succ = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: seeds = [(0,0)]
            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric')
            sage: C.to_digraph(max_depth=3)                                             # needs sage.graphs
            Looped multi-digraph on 41 vertices

        The ``max_depth`` argument can be given at the creation of the set::

            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric',
            ....:                              max_depth=2)
            sage: C.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 25 vertices

        Digraph of a recursively enumerated set with a graded structure::

            sage: f = lambda a: [a+1, a+I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: C.to_digraph(max_depth=4)                                             # needs sage.graphs
            Looped multi-digraph on 21 vertices"""
    @overload
    def to_digraph(self) -> Any:
        """RecursivelyEnumeratedSet_generic.to_digraph(self, max_depth=None, loops=True, multiedges=True)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 904)

        Return the directed graph of the recursively enumerated set.

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth for which outgoing edges of elements are computed
        - ``loops`` -- boolean (default: ``True``); option for the digraph
        - ``multiedges`` -- boolean (default: ``True``); option of the digraph

        OUTPUT: a directed graph

        .. WARNING::

            If the set is infinite, this will loop forever unless ``max_depth``
            is finite.

        EXAMPLES::

            sage: child = lambda i: [(i+3) % 10, (i+8) % 10]
            sage: R = RecursivelyEnumeratedSet([0], child)
            sage: R.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 10 vertices

        Digraph of a recursively enumerated set with a symmetric structure of
        infinite cardinality using ``max_depth`` argument::

            sage: succ = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: seeds = [(0,0)]
            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric')
            sage: C.to_digraph(max_depth=3)                                             # needs sage.graphs
            Looped multi-digraph on 41 vertices

        The ``max_depth`` argument can be given at the creation of the set::

            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric',
            ....:                              max_depth=2)
            sage: C.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 25 vertices

        Digraph of a recursively enumerated set with a graded structure::

            sage: f = lambda a: [a+1, a+I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: C.to_digraph(max_depth=4)                                             # needs sage.graphs
            Looped multi-digraph on 21 vertices"""
    @overload
    def to_digraph(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_generic.to_digraph(self, max_depth=None, loops=True, multiedges=True)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 904)

        Return the directed graph of the recursively enumerated set.

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth for which outgoing edges of elements are computed
        - ``loops`` -- boolean (default: ``True``); option for the digraph
        - ``multiedges`` -- boolean (default: ``True``); option of the digraph

        OUTPUT: a directed graph

        .. WARNING::

            If the set is infinite, this will loop forever unless ``max_depth``
            is finite.

        EXAMPLES::

            sage: child = lambda i: [(i+3) % 10, (i+8) % 10]
            sage: R = RecursivelyEnumeratedSet([0], child)
            sage: R.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 10 vertices

        Digraph of a recursively enumerated set with a symmetric structure of
        infinite cardinality using ``max_depth`` argument::

            sage: succ = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: seeds = [(0,0)]
            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric')
            sage: C.to_digraph(max_depth=3)                                             # needs sage.graphs
            Looped multi-digraph on 41 vertices

        The ``max_depth`` argument can be given at the creation of the set::

            sage: C = RecursivelyEnumeratedSet(seeds, succ, structure='symmetric',
            ....:                              max_depth=2)
            sage: C.to_digraph()                                                        # needs sage.graphs
            Looped multi-digraph on 25 vertices

        Digraph of a recursively enumerated set with a graded structure::

            sage: f = lambda a: [a+1, a+I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: C.to_digraph(max_depth=4)                                             # needs sage.graphs
            Looped multi-digraph on 21 vertices"""
    def __contains__(self, elt) -> Any:
        """RecursivelyEnumeratedSet_generic.__contains__(self, elt)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 597)

        Return ``True`` if ``elt`` is in ``self``.

        .. WARNING::

           This is achieved by iterating through the elements using the
           default enumeration until ``elt`` is found. In particular, this
           method will never stop when ``elt`` is not in ``self`` and
           ``self`` is infinite or when ``elt`` is in ``self`` but the
           enumeration is not appropriate.

        EXAMPLES::

            sage: f = lambda a:[a+3,a+5]
            sage: R = RecursivelyEnumeratedSet([0], f)
            sage: R
            A recursively enumerated set (breadth first search)
            sage: 8 in R
            True

        ::

            sage: R = RecursivelyEnumeratedSet([0], f, enumeration='depth')
            sage: R
            A recursively enumerated set (depth first search)
            sage: it = iter(R)
            sage: [next(it) for _ in range(6)]
            [0, 5, 10, 15, 20, 25]
            sage: 8 in R     # (should return True) not tested: does not terminate
            sage: 7 in R     # (should return False) not tested: does not terminate"""
    def __iter__(self) -> Any:
        """RecursivelyEnumeratedSet_generic.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 568)

        Iterate on the elements of ``self``.

        The enumeration is done depth first or breadth first depending on
        the value of ``self._enumeration``.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: it_naive = iter(RecursivelyEnumeratedSet([0], f, enumeration='naive'))
            sage: it_depth = iter(RecursivelyEnumeratedSet([0], f, enumeration='depth'))
            sage: it_breadth = iter(RecursivelyEnumeratedSet([0], f, enumeration='breadth'))
            sage: sorted([next(it_naive) for _ in range(10)])
            [0, 3, 5, 6, 8, 9, 10, 11, 12, 13]
            sage: [next(it_depth) for _ in range(10)]
            [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
            sage: [next(it_breadth) for _ in range(10)]
            [0, 3, 5, 6, 8, 10, 9, 11, 13, 15]"""
    @overload
    def __len__(self) -> Any:
        """RecursivelyEnumeratedSet_generic.__len__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 550)

        Disable ``__len__()`` from :class:`Parent` :issue:`12955`.

        Because Python assumes ``__len__()`` is fast and we cannot
        have a fast default implementation.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: len(C)
            Traceback (most recent call last):
            ...
            TypeError: cannot compute length of A recursively enumerated set (breadth first search)"""
    @overload
    def __len__(self) -> Any:
        """RecursivelyEnumeratedSet_generic.__len__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 550)

        Disable ``__len__()`` from :class:`Parent` :issue:`12955`.

        Because Python assumes ``__len__()`` is fast and we cannot
        have a fast default implementation.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: len(C)
            Traceback (most recent call last):
            ...
            TypeError: cannot compute length of A recursively enumerated set (breadth first search)"""
    @overload
    def __len__(self) -> Any:
        """RecursivelyEnumeratedSet_generic.__len__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 550)

        Disable ``__len__()`` from :class:`Parent` :issue:`12955`.

        Because Python assumes ``__len__()`` is fast and we cannot
        have a fast default implementation.

        EXAMPLES::

            sage: f = lambda a: [a+3, a+5]
            sage: C = RecursivelyEnumeratedSet([0], f)
            sage: len(C)
            Traceback (most recent call last):
            ...
            TypeError: cannot compute length of A recursively enumerated set (breadth first search)"""
    def __reduce__(self) -> Any:
        """RecursivelyEnumeratedSet_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 487)

        Return a tuple of three elements:

        - The function :func:`RecursivelyEnumeratedSet`
        - Arguments for the function :func:`RecursivelyEnumeratedSet`
        - The actual state of ``self``.

        EXAMPLES::

            sage: C = RecursivelyEnumeratedSet((1, 2, 3), factor)
            sage: loads(dumps(C))
            A recursively enumerated set (breadth first search)"""

class RecursivelyEnumeratedSet_graded(RecursivelyEnumeratedSet_generic):
    '''File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1235)

        Generic tool for constructing ideals of a graded relation.

        INPUT:

        - ``seeds`` -- list (or iterable) of hashable objects
        - ``successors`` -- function (or callable) returning a list (or iterable)
        - ``enumeration`` -- ``\'depth\'``, ``\'breadth\'`` or ``None`` (default: ``None``)
        - ``max_depth`` -- integer (default: ``float("inf")``)

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure=\'graded\', max_depth=3)
            sage: C
            A recursively enumerated set with a graded structure (breadth first
            search) with max_depth=3
            sage: list(C)
            [(0, 0),
             (1, 0), (0, 1),
             (2, 0), (1, 1), (0, 2),
             (3, 0), (2, 1), (1, 2), (0, 3)]
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_graded.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1259)

        Iterate on the elements of ``self`` (breadth first).

        This iterator makes use of the graded structure by remembering only
        the elements of the current depth.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='graded')
            sage: list(C.breadth_first_search_iterator(max_depth=3))
            [(0, 0),
             (1, 0), (0, 1),
             (2, 0), (1, 1), (0, 2),
             (3, 0), (2, 1), (1, 2), (0, 3)]"""
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_graded.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1259)

        Iterate on the elements of ``self`` (breadth first).

        This iterator makes use of the graded structure by remembering only
        the elements of the current depth.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='graded')
            sage: list(C.breadth_first_search_iterator(max_depth=3))
            [(0, 0),
             (1, 0), (0, 1),
             (2, 0), (1, 1), (0, 2),
             (3, 0), (2, 1), (1, 2), (0, 3)]"""
    @overload
    def graded_component(self, depth) -> Any:
        """RecursivelyEnumeratedSet_graded.graded_component(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1352)

        Return the graded component of given depth.

        This method caches each lower graded component. See
        :meth:`graded_component_iterator` to generate each graded component
        without caching the previous ones.

        A graded component is a set of elements of the same depth where the
        depth of an element is its minimal distance to a root.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: set

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: for i in range(5): sorted(C.graded_component(i))
            [0]
            [I, 1]
            [2*I, I + 1, 2]
            [3*I, 2*I + 1, I + 2, 3]
            [4*I, 3*I + 1, 2*I + 2, I + 3, 4]

        TESTS:

        We make sure that :issue:`21312` is fixed::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:    sleep(0.1r)
            ....:    return [a + 1, a + I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.45): C.graded_component(10)
            sage: C.graded_component(2)
            {2*I, I + 1, 2}
            sage: C.graded_component(3)
            {3*I, 2*I + 1, I + 2, 3}
            sage: C.graded_component(4)
            {4*I, 3*I + 1, 2*I + 2, I + 3, 4}"""
    @overload
    def graded_component(self, i) -> Any:
        """RecursivelyEnumeratedSet_graded.graded_component(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1352)

        Return the graded component of given depth.

        This method caches each lower graded component. See
        :meth:`graded_component_iterator` to generate each graded component
        without caching the previous ones.

        A graded component is a set of elements of the same depth where the
        depth of an element is its minimal distance to a root.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: set

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: for i in range(5): sorted(C.graded_component(i))
            [0]
            [I, 1]
            [2*I, I + 1, 2]
            [3*I, 2*I + 1, I + 2, 3]
            [4*I, 3*I + 1, 2*I + 2, I + 3, 4]

        TESTS:

        We make sure that :issue:`21312` is fixed::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:    sleep(0.1r)
            ....:    return [a + 1, a + I]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='graded')
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.45): C.graded_component(10)
            sage: C.graded_component(2)
            {2*I, I + 1, 2}
            sage: C.graded_component(3)
            {3*I, 2*I + 1, I + 2, 3}
            sage: C.graded_component(4)
            {4*I, 3*I + 1, 2*I + 2, I + 3, 4}"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_graded.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1307)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The algorithm remembers only the current graded component generated
        since the structure is graded.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='graded', max_depth=3)
            sage: it = C.graded_component_iterator()
            sage: for _ in range(4): sorted(next(it))
            [(0, 0)]
            [(0, 1), (1, 0)]
            [(0, 2), (1, 1), (2, 0)]
            [(0, 3), (1, 2), (2, 1), (3, 0)]

        TESTS:

        Make sure that :issue:`20225` is fixed::

            sage: child = lambda k:[2*k,2*k+1] if k<8 else []
            sage: root = [0]
            sage: R = RecursivelyEnumeratedSet(root, child, structure='graded')
            sage: it = R.graded_component_iterator()
            sage: for _ in range(7): next(it)
            {0}
            {1}
            {2, 3}
            {4, 5, 6, 7}
            {8, 9, 10, 11, 12, 13, 14, 15}
            set()
            set()"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_graded.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1307)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The algorithm remembers only the current graded component generated
        since the structure is graded.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='graded', max_depth=3)
            sage: it = C.graded_component_iterator()
            sage: for _ in range(4): sorted(next(it))
            [(0, 0)]
            [(0, 1), (1, 0)]
            [(0, 2), (1, 1), (2, 0)]
            [(0, 3), (1, 2), (2, 1), (3, 0)]

        TESTS:

        Make sure that :issue:`20225` is fixed::

            sage: child = lambda k:[2*k,2*k+1] if k<8 else []
            sage: root = [0]
            sage: R = RecursivelyEnumeratedSet(root, child, structure='graded')
            sage: it = R.graded_component_iterator()
            sage: for _ in range(7): next(it)
            {0}
            {1}
            {2, 3}
            {4, 5, 6, 7}
            {8, 9, 10, 11, 12, 13, 14, 15}
            set()
            set()"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_graded.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1307)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The algorithm remembers only the current graded component generated
        since the structure is graded.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [(a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='graded', max_depth=3)
            sage: it = C.graded_component_iterator()
            sage: for _ in range(4): sorted(next(it))
            [(0, 0)]
            [(0, 1), (1, 0)]
            [(0, 2), (1, 1), (2, 0)]
            [(0, 3), (1, 2), (2, 1), (3, 0)]

        TESTS:

        Make sure that :issue:`20225` is fixed::

            sage: child = lambda k:[2*k,2*k+1] if k<8 else []
            sage: root = [0]
            sage: R = RecursivelyEnumeratedSet(root, child, structure='graded')
            sage: it = R.graded_component_iterator()
            sage: for _ in range(7): next(it)
            {0}
            {1}
            {2, 3}
            {4, 5, 6, 7}
            {8, 9, 10, 11, 12, 13, 14, 15}
            set()
            set()"""

class RecursivelyEnumeratedSet_symmetric(RecursivelyEnumeratedSet_generic):
    '''File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 960)

        Generic tool for constructing ideals of a symmetric relation.

        INPUT:

        - ``seeds`` -- list (or iterable) of hashable objects
        - ``successors`` -- function (or callable) returning a list (or iterable)
        - ``enumeration`` -- ``\'depth\'``, ``\'breadth\'`` or ``None`` (default: ``None``)
        - ``max_depth`` -- integer (default: ``float("inf")``)

        EXAMPLES::

            sage: f = lambda a: [a-1,a+1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure=\'symmetric\')
            sage: C
            A recursively enumerated set with a symmetric structure (breadth first search)
            sage: it = iter(C)
            sage: [next(it) for _ in range(7)]
            [0, -1, 1, -2, 2, -3, 3]

        TESTS:

        Do not use lambda functions for saving purposes::

            sage: f = lambda a: [a-1,a+1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure=\'symmetric\')
            sage: loads(dumps(C))
            Traceback (most recent call last):
            ...
            PicklingError: ...

        This works in the command line but apparently not as a doctest::

            sage: def f(a): return [a-1,a+1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure=\'symmetric\')
            sage: loads(dumps(C))
            Traceback (most recent call last):
            ...
            PicklingError: ...
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_symmetric.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1002)

        Iterate on the elements of ``self`` (breadth first).

        This iterator makes use of the graded structure by remembering only
        the last two graded components since the structure is symmetric.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='symmetric')
            sage: s = list(C.breadth_first_search_iterator(max_depth=2)); s
            [(0, 0),
             (-1, 0), (0, -1), (1, 0), (0, 1),
             (-2, 0), (-1, -1), (-1, 1), (0, -2), (1, -1), (2, 0), (1, 1), (0, 2)]

        This iterator is used by default for symmetric structure::

            sage: it = iter(C)
            sage: s == [next(it) for _ in range(13)]
            True

        TESTS:

        Check that :issue:`28674` is fixed::

            sage: D = RecursivelyEnumeratedSet([(0,0)], f)
            sage: s == list(D.breadth_first_search_iterator(max_depth=2))
            True"""
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_symmetric.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1002)

        Iterate on the elements of ``self`` (breadth first).

        This iterator makes use of the graded structure by remembering only
        the last two graded components since the structure is symmetric.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='symmetric')
            sage: s = list(C.breadth_first_search_iterator(max_depth=2)); s
            [(0, 0),
             (-1, 0), (0, -1), (1, 0), (0, 1),
             (-2, 0), (-1, -1), (-1, 1), (0, -2), (1, -1), (2, 0), (1, 1), (0, 2)]

        This iterator is used by default for symmetric structure::

            sage: it = iter(C)
            sage: s == [next(it) for _ in range(13)]
            True

        TESTS:

        Check that :issue:`28674` is fixed::

            sage: D = RecursivelyEnumeratedSet([(0,0)], f)
            sage: s == list(D.breadth_first_search_iterator(max_depth=2))
            True"""
    @overload
    def breadth_first_search_iterator(self, max_depth=...) -> Any:
        """RecursivelyEnumeratedSet_symmetric.breadth_first_search_iterator(self, max_depth=None)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1002)

        Iterate on the elements of ``self`` (breadth first).

        This iterator makes use of the graded structure by remembering only
        the last two graded components since the structure is symmetric.

        The elements are guaranteed to be enumerated in the order in which they
        are first visited (left-to-right traversal).

        INPUT:

        - ``max_depth`` -- (default: ``self._max_depth``) specifies the
          maximal depth to which elements are computed

        EXAMPLES::

            sage: f = lambda a: [(a[0]-1,a[1]), (a[0],a[1]-1), (a[0]+1,a[1]), (a[0],a[1]+1)]
            sage: C = RecursivelyEnumeratedSet([(0,0)], f, structure='symmetric')
            sage: s = list(C.breadth_first_search_iterator(max_depth=2)); s
            [(0, 0),
             (-1, 0), (0, -1), (1, 0), (0, 1),
             (-2, 0), (-1, -1), (-1, 1), (0, -2), (1, -1), (2, 0), (1, 1), (0, 2)]

        This iterator is used by default for symmetric structure::

            sage: it = iter(C)
            sage: s == [next(it) for _ in range(13)]
            True

        TESTS:

        Check that :issue:`28674` is fixed::

            sage: D = RecursivelyEnumeratedSet([(0,0)], f)
            sage: s == list(D.breadth_first_search_iterator(max_depth=2))
            True"""
    @overload
    def graded_component(self, depth) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1139)

        Return the graded component of given depth.

        This method caches each lower graded component. See
        :meth:`graded_component_iterator` to generate each graded component
        without caching the previous ones.

        A graded component is a set of elements of the same depth where the
        depth of an element is its minimal distance to a root.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: set

        EXAMPLES::

            sage: f = lambda a: [a-1,a+1]
            sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
            sage: for i in range(5): sorted(C.graded_component(i))
            [10, 15]
            [9, 11, 14, 16]
            [8, 12, 13, 17]
            [7, 18]
            [6, 19]

        TESTS:

        We make sure that :issue:`21312` is fixed::

            sage: def f(a):
            ....:    sleep(0.1r)
            ....:    return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.45): C.graded_component(10)
            sage: C.graded_component(1)
            {-1, 1}
            sage: C.graded_component(2)
            {-2, 2}
            sage: C.graded_component(3)
            {-3, 3}
            sage: C.graded_component(4)
            {-4, 4}
            sage: C.graded_component(5)
            {-5, 5}"""
    @overload
    def graded_component(self, i) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component(self, depth)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1139)

        Return the graded component of given depth.

        This method caches each lower graded component. See
        :meth:`graded_component_iterator` to generate each graded component
        without caching the previous ones.

        A graded component is a set of elements of the same depth where the
        depth of an element is its minimal distance to a root.

        INPUT:

        - ``depth`` -- integer

        OUTPUT: set

        EXAMPLES::

            sage: f = lambda a: [a-1,a+1]
            sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
            sage: for i in range(5): sorted(C.graded_component(i))
            [10, 15]
            [9, 11, 14, 16]
            [8, 12, 13, 17]
            [7, 18]
            [6, 19]

        TESTS:

        We make sure that :issue:`21312` is fixed::

            sage: def f(a):
            ....:    sleep(0.1r)
            ....:    return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.45): C.graded_component(10)
            sage: C.graded_component(1)
            {-1, 1}
            sage: C.graded_component(2)
            {-2, 2}
            sage: C.graded_component(3)
            {-3, 3}
            sage: C.graded_component(4)
            {-4, 4}
            sage: C.graded_component(5)
            {-5, 5}"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1067)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The enumeration remembers only the last two graded components
        generated since the structure is symmetric.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[10], [9, 11], [8, 12], [7, 13], [6, 14]]

        Starting with two generators::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[5, 10], [4, 6, 9, 11], [3, 7, 8, 12], [2, 13], [1, 14]]

        Gaussian integers::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: S = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(7)]
            [[0],
             [I, 1],
             [2*I, I + 1, 2],
             [3*I, 2*I + 1, I + 2, 3],
             [4*I, 3*I + 1, 2*I + 2, I + 3, 4],
             [5*I, 4*I + 1, 3*I + 2, 2*I + 3, I + 4, 5],
             [6*I, 5*I + 1, 4*I + 2, 3*I + 3, 2*I + 4, I + 5, 6]]

        TESTS:

        Note that interrupting the computation (``KeyboardInterrupt`` for
        instance) breaks the iterator::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     sleep(0.05r)
            ....:     return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = C.graded_component_iterator()
            sage: next(it)
            {0}
            sage: next(it)
            {-1, 1}
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.02): next(it)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1067)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The enumeration remembers only the last two graded components
        generated since the structure is symmetric.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[10], [9, 11], [8, 12], [7, 13], [6, 14]]

        Starting with two generators::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[5, 10], [4, 6, 9, 11], [3, 7, 8, 12], [2, 13], [1, 14]]

        Gaussian integers::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: S = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(7)]
            [[0],
             [I, 1],
             [2*I, I + 1, 2],
             [3*I, 2*I + 1, I + 2, 3],
             [4*I, 3*I + 1, 2*I + 2, I + 3, 4],
             [5*I, 4*I + 1, 3*I + 2, 2*I + 3, I + 4, 5],
             [6*I, 5*I + 1, 4*I + 2, 3*I + 3, 2*I + 4, I + 5, 6]]

        TESTS:

        Note that interrupting the computation (``KeyboardInterrupt`` for
        instance) breaks the iterator::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     sleep(0.05r)
            ....:     return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = C.graded_component_iterator()
            sage: next(it)
            {0}
            sage: next(it)
            {-1, 1}
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.02): next(it)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1067)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The enumeration remembers only the last two graded components
        generated since the structure is symmetric.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[10], [9, 11], [8, 12], [7, 13], [6, 14]]

        Starting with two generators::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[5, 10], [4, 6, 9, 11], [3, 7, 8, 12], [2, 13], [1, 14]]

        Gaussian integers::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: S = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(7)]
            [[0],
             [I, 1],
             [2*I, I + 1, 2],
             [3*I, 2*I + 1, I + 2, 3],
             [4*I, 3*I + 1, 2*I + 2, I + 3, 4],
             [5*I, 4*I + 1, 3*I + 2, 2*I + 3, I + 4, 5],
             [6*I, 5*I + 1, 4*I + 2, 3*I + 3, 2*I + 4, I + 5, 6]]

        TESTS:

        Note that interrupting the computation (``KeyboardInterrupt`` for
        instance) breaks the iterator::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     sleep(0.05r)
            ....:     return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = C.graded_component_iterator()
            sage: next(it)
            {0}
            sage: next(it)
            {-1, 1}
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.02): next(it)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1067)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The enumeration remembers only the last two graded components
        generated since the structure is symmetric.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[10], [9, 11], [8, 12], [7, 13], [6, 14]]

        Starting with two generators::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[5, 10], [4, 6, 9, 11], [3, 7, 8, 12], [2, 13], [1, 14]]

        Gaussian integers::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: S = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(7)]
            [[0],
             [I, 1],
             [2*I, I + 1, 2],
             [3*I, 2*I + 1, I + 2, 3],
             [4*I, 3*I + 1, 2*I + 2, I + 3, 4],
             [5*I, 4*I + 1, 3*I + 2, 2*I + 3, I + 4, 5],
             [6*I, 5*I + 1, 4*I + 2, 3*I + 3, 2*I + 4, I + 5, 6]]

        TESTS:

        Note that interrupting the computation (``KeyboardInterrupt`` for
        instance) breaks the iterator::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     sleep(0.05r)
            ....:     return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = C.graded_component_iterator()
            sage: next(it)
            {0}
            sage: next(it)
            {-1, 1}
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.02): next(it)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
    @overload
    def graded_component_iterator(self) -> Any:
        """RecursivelyEnumeratedSet_symmetric.graded_component_iterator(self)

        File: /build/sagemath/src/sage/src/sage/sets/recursively_enumerated_set.pyx (starting at line 1067)

        Iterate over the graded components of ``self``.

        A graded component is a set of elements of the same depth.

        The enumeration remembers only the last two graded components
        generated since the structure is symmetric.

        OUTPUT: an iterator of sets

        EXAMPLES::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[10], [9, 11], [8, 12], [7, 13], [6, 14]]

        Starting with two generators::

            sage: f = lambda a: [a-1, a+1]
            sage: S = RecursivelyEnumeratedSet([5, 10], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(5)]
            [[5, 10], [4, 6, 9, 11], [3, 7, 8, 12], [2, 13], [1, 14]]

        Gaussian integers::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     return [a + 1, a + I]
            sage: S = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = S.graded_component_iterator()
            sage: [sorted(next(it)) for _ in range(7)]
            [[0],
             [I, 1],
             [2*I, I + 1, 2],
             [3*I, 2*I + 1, I + 2, 3],
             [4*I, 3*I + 1, 2*I + 2, I + 3, 4],
             [5*I, 4*I + 1, 3*I + 2, 2*I + 3, I + 4, 5],
             [6*I, 5*I + 1, 4*I + 2, 3*I + 3, 2*I + 4, I + 5, 6]]

        TESTS:

        Note that interrupting the computation (``KeyboardInterrupt`` for
        instance) breaks the iterator::

            sage: # needs sage.symbolic
            sage: def f(a):
            ....:     sleep(0.05r)
            ....:     return [a - 1, a + 1]
            sage: C = RecursivelyEnumeratedSet([0], f, structure='symmetric')
            sage: it = C.graded_component_iterator()
            sage: next(it)
            {0}
            sage: next(it)
            {-1, 1}
            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.02): next(it)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
