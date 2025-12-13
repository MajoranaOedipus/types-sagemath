from _typeshed import Incomplete
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.misc.function_mangling import ArgumentFixer as ArgumentFixer
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.lazy_list import lazy_list as lazy_list
from sage.structure.parent import Parent as Parent

class EnumeratedSetFromIterator(Parent):
    '''
    A class for enumerated set built from an iterator.

    INPUT:

    - ``f`` -- a function that returns an iterable from which the set is built from

    - ``args`` -- tuple; arguments to be sent to the function `f`

    - ``kwds`` -- dictionary; keywords to be sent to the function `f`

    - ``name`` -- an optional name for the set

    - ``category`` -- (default: ``None``) an optional category for that
      enumerated set. If you know that your iterator will stop after a finite
      number of steps you should set it as :class:`FiniteEnumeratedSets`, conversely if
      you know that your iterator will run over and over you should set it as
      :class:`InfiniteEnumeratedSets`.

    - ``cache`` -- boolean (default: ``False``); whether or not use a cache
      mechanism for the iterator. If ``True``, then the function `f` is called
      only once.

    EXAMPLES::

        sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
        sage: E = EnumeratedSetFromIterator(graphs, args=(7,)); E                       # needs sage.graphs
        {Graph on 7 vertices, Graph on 7 vertices, Graph on 7 vertices,
         Graph on 7 vertices, Graph on 7 vertices, ...}
        sage: E.category()                                                              # needs sage.graphs
        Category of facade enumerated sets

    The same example with a cache and a custom name::

        sage: E = EnumeratedSetFromIterator(graphs, args=(8,), cache=True,              # needs sage.graphs
        ....:                               name="Graphs with 8 vertices",
        ....:                               category=FiniteEnumeratedSets()); E
        Graphs with 8 vertices
        sage: E.unrank(3)                                                               # needs sage.graphs
        Graph on 8 vertices
        sage: E.category()                                                              # needs sage.graphs
        Category of facade finite enumerated sets

    TESTS:

    The cache is compatible with multiple call to ``__iter__``::

        sage: from itertools import count
        sage: E = EnumeratedSetFromIterator(count, args=(0,), category=InfiniteEnumeratedSets(), cache=True)
        sage: e1 = iter(E)
        sage: e2 = iter(E)
        sage: next(e1), next(e1)
        (0, 1)
        sage: next(e2), next(e2), next(e2)
        (0, 1, 2)
        sage: next(e1), next(e1)
        (2, 3)
        sage: next(e2)
        3

    The following warning is due to ``E`` being a facade parent. For more,
    see the discussion on :issue:`16239`::

        sage: TestSuite(E).run()
        doctest:...: UserWarning: Testing equality of infinite sets which will not end in case of equality

        sage: E = EnumeratedSetFromIterator(xsrange, args=(10,), category=FiniteEnumeratedSets(), cache=True)
        sage: TestSuite(E).run()

    .. NOTE::

        In order to make the ``TestSuite`` works, the elements of the set
        should have parents.
    '''
    def __init__(self, f, args=None, kwds=None, name=None, category=None, cache: bool = False) -> None:
        """
        TESTS::

            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: S = EnumeratedSetFromIterator(xsrange, (1, 200, -1), category=FiniteEnumeratedSets())
            sage: TestSuite(S).run()
        """
    def __hash__(self):
        """
        A simple hash using the first elements of the set.

        EXAMPLES::

            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E = EnumeratedSetFromIterator(xsrange, (1, 200))
            sage: hash(E) == hash(tuple(range(1, 14)))
            True
        """
    def __reduce__(self):
        '''
        Support for pickle.

        TESTS::

            sage: # needs sage.graphs
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: from sage.graphs.graph_generators import graphs
            sage: E = EnumeratedSetFromIterator(graphs,
            ....:    args=(3,),
            ....:    category=FiniteEnumeratedSets(),
            ....:    name="Graphs on 3 vertices")
            sage: E
            Graphs on 3 vertices
            sage: F = loads(dumps(E)); F
            Graphs on 3 vertices
            sage: E == F
            True
        '''
    def __contains__(self, x) -> bool:
        """
        Test whether ``x`` is in ``self``.

        If the set is infinite, only the answer ``True`` should be expected in
        finite time.

        EXAMPLES::

            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: P = Partitions(12, min_part=2, max_part=5)                            # needs sage.combinat
            sage: E = EnumeratedSetFromIterator(P.__iter__)                             # needs sage.combinat
            sage: P([5,5,2]) in E                                                       # needs sage.combinat
            True
        """
    is_parent_of = __contains__
    def __eq__(self, other):
        """
        Equality test.

        The function returns ``True`` if and only if other is an enumerated
        set and has the same element as ``self``.

        TESTS::

            sage: # needs sage.graphs
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E4 = EnumeratedSetFromIterator(graphs, args=(4,),
            ....:                                category=FiniteEnumeratedSets())
            sage: F4 = EnumeratedSetFromIterator(graphs, args=(4,),
            ....:                                category=FiniteEnumeratedSets())
            sage: E5 = EnumeratedSetFromIterator(graphs, args=(5,),
            ....:                                category=FiniteEnumeratedSets())
            sage: E4 == E4
            True
            sage: E4 == F4
            True
            sage: E4 == E5
            False
            sage: E5 == E4
            False
            sage: E5 == E5
            True
        """
    def __ne__(self, other):
        """
        Difference test.

        The function calls the ``__eq__`` test.

        TESTS::

            sage: # needs sage.graphs
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E4 = EnumeratedSetFromIterator(graphs, args=(4,),
            ....:                                category=FiniteEnumeratedSets())
            sage: F4 = EnumeratedSetFromIterator(graphs, args=(4,),
            ....:                                category=FiniteEnumeratedSets())
            sage: E5 = EnumeratedSetFromIterator(graphs, args=(5,),
            ....:                                category=FiniteEnumeratedSets())
            sage: E4 != E4
            False
            sage: E4 != F4
            False
            sage: E4 != E5
            True
            sage: E5 != E4
            True
            sage: E5 != E5
            False
        """
    def __iter__(self):
        """
        Return an iterator over the element of ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E = EnumeratedSetFromIterator(graphs, args=(8,))
            sage: g1 = next(iter(E)); g1
            Graph on 8 vertices
            sage: E = EnumeratedSetFromIterator(graphs, args=(8,), cache=True)
            sage: g2 = next(iter(E)); g2
            Graph on 8 vertices
            sage: g1 == g2
            True
        """
    def unrank(self, i):
        """
        Return the element at position ``i``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E = EnumeratedSetFromIterator(graphs, args=(8,), cache=True)
            sage: F = EnumeratedSetFromIterator(graphs, args=(8,), cache=False)
            sage: E.unrank(2)
            Graph on 8 vertices
            sage: E.unrank(2) == F.unrank(2)
            True
        """
    def clear_cache(self) -> None:
        """
        Clear the cache.

        EXAMPLES::

            sage: from itertools import count
            sage: from sage.sets.set_from_iterator import EnumeratedSetFromIterator
            sage: E = EnumeratedSetFromIterator(count, args=(1,), cache=True)
            sage: e1 = E._cache; e1
            lazy list [1, 2, 3, ...]
            sage: E.clear_cache()
            sage: E._cache
            lazy list [1, 2, 3, ...]
            sage: e1 is E._cache
            False
        """

class Decorator:
    """
    Abstract class that manage documentation and sources of the wrapped object.

    The method needs to be stored in the attribute ``self.f``
    """
    def __call__(self, *args, **kwds) -> None:
        """
        Call function.

        Needs to be implemented in derived subclass.

        TESTS::

            sage: from sage.sets.set_from_iterator import Decorator
            sage: d = Decorator()
            sage: d()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

class EnumeratedSetFromIterator_function_decorator(Decorator):
    '''
    Decorator for :class:`EnumeratedSetFromIterator`.

    Name could be string or a function ``(args, kwds) -> string``.

    .. WARNING::

        If you are going to use this with the decorator :func:`cached_function`,
        you must place the ``@cached_function`` first. See the example below.

    EXAMPLES::

        sage: from sage.sets.set_from_iterator import set_from_function
        sage: @set_from_function
        ....: def f(n):
        ....:     for i in range(n):
        ....:         yield i**2 + i + 1
        sage: f(3)
        {1, 3, 7}
        sage: f(100)
        {1, 3, 7, 13, 21, ...}

    To avoid ambiguity, it is always better to use it with a call which
    provides optional global initialization for the call to
    :class:`EnumeratedSetFromIterator`::

        sage: @set_from_function(category=InfiniteEnumeratedSets())
        ....: def Fibonacci():
        ....:     a = 1; b = 2
        ....:     while True:
        ....:         yield a
        ....:         a, b = b, a + b
        sage: F = Fibonacci(); F
        {1, 2, 3, 5, 8, ...}
        sage: F.cardinality()
        +Infinity

    A simple example with many options::

        sage: @set_from_function(name="From %(m)d to %(n)d",
        ....:                    category=FiniteEnumeratedSets())
        ....: def f(m, n): return xsrange(m, n + 1)
        sage: E = f(3,10); E
        From 3 to 10
        sage: E.list()
        [3, 4, 5, 6, 7, 8, 9, 10]
        sage: E = f(1,100); E
        From 1 to 100
        sage: E.cardinality()
        100
        sage: f(n=100, m=1) == E
        True

    An example which mixes together :func:`set_from_function` and
    :func:`cached_method`::

        sage: @cached_function
        ....: @set_from_function(name="Graphs on %(n)d vertices",
        ....:                    category=FiniteEnumeratedSets(), cache=True)
        ....: def Graphs(n): return graphs(n)
        sage: Graphs(10)                                                                # needs sage.graphs
        Graphs on 10 vertices
        sage: Graphs(10).unrank(0)                                                      # needs sage.graphs
        Graph on 10 vertices
        sage: Graphs(10) is Graphs(10)                                                  # needs sage.graphs
        True

    The ``@cached_function`` must go first::

        sage: @set_from_function(name="Graphs on %(n)d vertices",
        ....:                    category=FiniteEnumeratedSets(), cache=True)
        ....: @cached_function
        ....: def Graphs(n): return graphs(n)
        sage: Graphs(10)                                                                # needs sage.graphs
        Graphs on 10 vertices
        sage: Graphs(10).unrank(0)                                                      # needs sage.graphs
        Graph on 10 vertices
        sage: Graphs(10) is Graphs(10)                                                  # needs sage.graphs
        False
    '''
    f: Incomplete
    __module__: Incomplete
    af: Incomplete
    name: Incomplete
    options: Incomplete
    def __init__(self, f=None, name=None, **options) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.sets.set_from_iterator import set_from_function
            sage: F = set_from_function(category=FiniteEnumeratedSets())(xsrange)
            sage: TestSuite(F(100)).run()
            sage: TestSuite(F(1,5,2)).run()
            sage: TestSuite(F(0)).run()
        """
    def __call__(self, *args, **kwds):
        """
        Build a new :class:`EnumeratedSet` by calling ``self.f`` with
        appropriate argument. If ``f`` is ``None``, then returns a new instance
        of :class:`EnumeratedSetFromIterator`.

        EXAMPLES::

            sage: from sage.sets.set_from_iterator import set_from_function
            sage: F = set_from_function(category=FiniteEnumeratedSets())(xsrange)
            sage: F(3)
            {0, 1, 2}
            sage: F(end=7,start=3)
            {3, 4, 5, 6}
            sage: F(10).cardinality()
            10
        """
set_from_function = EnumeratedSetFromIterator_function_decorator

class EnumeratedSetFromIterator_method_caller(Decorator):
    """
    Caller for decorated method in class.

    INPUT:

    - ``inst`` -- an instance of a class

    - ``f`` -- a method of a class of ``inst`` (and not of the instance itself)

    - ``name`` -- (optional) either a string (which may contains substitution
      rules from argument or a function ``args, kwds -> string``

    - ``options`` -- any option accepted by :class:`EnumeratedSetFromIterator`
    """
    inst: Incomplete
    f: Incomplete
    af: Incomplete
    __module__: Incomplete
    name: Incomplete
    options: Incomplete
    def __init__(self, inst, f, name=None, **options) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.sets.set_from_iterator import DummyExampleForPicklingTest
            sage: d = DummyExampleForPicklingTest()
            sage: d.f()
            {10, 11, 12, 13, 14, ...}

        It is possible to pickle/unpickle the class and the instance::

            sage: loads(dumps(DummyExampleForPicklingTest))().f()
            {10, 11, 12, 13, 14, ...}
            sage: loads(dumps(d)).f()
            {10, 11, 12, 13, 14, ...}

        But not the enumerated set::

            sage: loads(dumps(d.f()))
            Traceback (most recent call last):
            ...
            _pickle.PicklingError: Can't pickle <function DummyExampleForPicklingTest.f at ...>:
            it's not the same object as sage.sets.set_from_iterator.DummyExampleForPicklingTest.f
        """
    def __call__(self, *args, **kwds):
        '''
        Return an instance of :class:`EnumeratedSetFromIterator` with
        proper argument.

        TESTS::

            sage: from sage.sets.set_from_iterator import set_from_method
            sage: class A:
            ....:  @set_from_method(name = lambda self,n: str(self)*n)
            ....:  def f(self, n):
            ....:      return xsrange(n)
            ....:  def __repr__(self):
            ....:      return "A"
            sage: a = A()
            sage: a.f(3)                         # indirect doctest
            AAA
            sage: A.f(a,3)                       # indirect doctest
            AAA
            sage: [x for x in a.f(6)]            # indirect doctest
            [0, 1, 2, 3, 4, 5]
        '''
    def __get__(self, inst, cls):
        """
        Get a :class:`EnumeratedSetFromIterator_method_caller` bound to a
        specific instance of the class of the cached method.

        .. NOTE::

            :class:`EnumeratedSetFromIterator_method_caller` has a separate
            ``__get__`` because of the special behavior of category framework
            for element classes which are not of extension type (see
            :meth:`sage.structure.element.Element.__get__`).

        TESTS::

            sage: from sage.sets.set_from_iterator import set_from_method
            sage: class A:
            ....:    stop = 10000
            ....:    @set_from_method
            ....:    def f(self, start):
            ....:        return xsrange(start, self.stop)
            sage: a = A()
            sage: A.f(a,4)
            {4, 5, 6, 7, 8, ...}

            sage: class B:
            ....:    stop = 10000
            ....:    @set_from_method(category=FiniteEnumeratedSets())
            ....:    def f(self, start):
            ....:        return xsrange(start, self.stop)
            sage: b = B()
            sage: B.f(b,2)
            {2, 3, 4, 5, 6, ...}
        """

class EnumeratedSetFromIterator_method_decorator:
    '''
    Decorator for enumerated set built from a method.

    INPUT:

    - ``f`` -- (optional) function from which are built the enumerated sets at
      each call

    - ``name`` -- (optional) string (which may contains substitution rules from
      argument) or a function ``(args,kwds) -> string``

    - any option accepted by :class:`EnumeratedSetFromIterator`.

    EXAMPLES::

        sage: from sage.sets.set_from_iterator import set_from_method
        sage: class A():
        ....:     def n(self): return 12
        ....:     @set_from_method
        ....:     def f(self): return xsrange(self.n())
        sage: a = A()
        sage: print(a.f.__class__)
        <class \'sage.sets.set_from_iterator.EnumeratedSetFromIterator_method_caller\'>
        sage: a.f()
        {0, 1, 2, 3, 4, ...}
        sage: A.f(a)
        {0, 1, 2, 3, 4, ...}

    A more complicated example with a parametrized name::

        sage: class B():
        ....:     @set_from_method(name="Graphs(%(n)d)",
        ....:                      category=FiniteEnumeratedSets())
        ....:     def graphs(self, n): return graphs(n)
        sage: b = B()
        sage: G3 = b.graphs(3); G3
        Graphs(3)
        sage: G3.cardinality()                                                          # needs sage.graphs
        4
        sage: G3.category()
        Category of facade finite enumerated sets
        sage: B.graphs(b, 3)
        Graphs(3)

    And a last example with a name parametrized by a function::

        sage: class D():
        ....:     def __init__(self, name): self.name = str(name)
        ....:     def __str__(self): return self.name
        ....:     @set_from_method(name=lambda self, n: str(self) * n,
        ....:                      category=FiniteEnumeratedSets())
        ....:     def subset(self, n):
        ....:         return xsrange(n)
        sage: d = D(\'a\')
        sage: E = d.subset(3); E
        aaa
        sage: E.list()
        [0, 1, 2]
        sage: F = d.subset(n=10); F
        aaaaaaaaaa
        sage: F.list()
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    .. TODO::

        It is not yet possible to use ``set_from_method`` in conjunction with
        ``cached_method``.
    '''
    f: Incomplete
    __module__: Incomplete
    options: Incomplete
    def __init__(self, f=None, **options) -> None:
        """
        Initialize ``self``.

        TESTS:

        We test if pickling works correctly on the Permutation class (in
        :mod:`sage.combinat.permutation`) because its method ``bruhat_succ``
        and ``bruhat_pred`` are decorated with ``set_from_method``::

            sage: from sage.combinat.permutation import Permutation
            sage: loads(dumps(Permutation))
            <class 'sage.combinat.permutation.Permutation'>
            sage: p = Permutation([3,2,1])
            sage: loads(dumps(p)) == p
            True
        """
    def __call__(self, f):
        """
        Trick if :class:`EnumeratedSetFromIterator_method` was created with
        some options and is called with a function as argument.

        TESTS::

            sage: from sage.sets.set_from_iterator import set_from_method
            sage: class A:                # indirect doctest
            ....:     @set_from_method()
            ....:     def f(self):
            ....:         return xsrange(3)
            sage: a = A()
            sage: a.f()
            {0, 1, 2}
        """
    def __get__(self, inst, cls):
        """
        TESTS::

            sage: from sage.sets.set_from_iterator import set_from_method
            sage: class A():
            ....:     def n(self): return 12
            ....:     @set_from_method
            ....:     def f(self): return xsrange(self.n())
            sage: a = A()
            sage: print(A.f.__class__)
            <class 'sage.sets.set_from_iterator.EnumeratedSetFromIterator_method_caller'>
            sage: print(a.f.__class__)
            <class 'sage.sets.set_from_iterator.EnumeratedSetFromIterator_method_caller'>
        """
set_from_method = EnumeratedSetFromIterator_method_decorator

class DummyExampleForPicklingTest:
    """
    Class example to test pickling with the decorator :class:`set_from_method`.

    .. WARNING::

        This class is intended to be used in doctest only.

    EXAMPLES::

        sage: from sage.sets.set_from_iterator import DummyExampleForPicklingTest
        sage: DummyExampleForPicklingTest().f()
        {10, 11, 12, 13, 14, ...}
    """
    start: int
    stop: int
    @set_from_method
    def f(self):
        """
        Return the set between ``self.start`` and ``self.stop``.

        EXAMPLES::

            sage: from sage.sets.set_from_iterator import DummyExampleForPicklingTest
            sage: d = DummyExampleForPicklingTest()
            sage: d.f()
            {10, 11, 12, 13, 14, ...}
            sage: d.start = 4
            sage: d.stop = 200
            sage: d.f()
            {4, 5, 6, 7, 8, ...}
        """
