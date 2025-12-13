from sage.sets.family import FiniteFamily as FiniteFamily

class ManifoldObjectFiniteFamily(FiniteFamily):
    """
    Finite family of manifold objects, indexed by their names.

    The class :class:`ManifoldObjectFiniteFamily` inherits from
    :class:`FiniteFamily`.  Therefore it is an associative container.

    It provides specialized ``__repr__`` and ``_latex_`` methods.

    :class:`ManifoldObjectFiniteFamily` instances are totally ordered
    according to their lexicographically ordered element names.

    EXAMPLES::

        sage: from sage.manifolds.family import ManifoldObjectFiniteFamily
        sage: M = Manifold(2, 'M', structure='topological')
        sage: A = M.subset('A')
        sage: B = M.subset('B')
        sage: C = B.subset('C')
        sage: F = ManifoldObjectFiniteFamily([A, B, C]); F
        Set {A, B, C} of objects of the 2-dimensional topological manifold M
        sage: latex(F)
        \\{A, B, C\\}
        sage: F['B']
        Subset B of the 2-dimensional topological manifold M

    All objects must have the same base manifold::

        sage: N = Manifold(2, 'N', structure='topological')
        sage: ManifoldObjectFiniteFamily([M, N])
        Traceback (most recent call last):
        ...
        TypeError: all objects must have the same manifold
    """
    def __init__(self, objects=(), keys=None) -> None:
        """
        Initialize a new instance of :class:`ManifoldObjectFiniteFamily`.

        TESTS:

            sage: from sage.manifolds.family import ManifoldObjectFiniteFamily
            sage: M = Manifold(2, 'M', structure='topological')
            sage: A = M.subset('A')
            sage: B = M.subset('B')
            sage: C = B.subset('C')
            sage: F = ManifoldObjectFiniteFamily([A, B, C]); F
            Set {A, B, C} of objects of the 2-dimensional topological manifold M
            sage: TestSuite(F).run(skip='_test_elements')

        Like ``frozenset``, it can be created from any iterable::

            sage: from sage.manifolds.family import ManifoldSubsetFiniteFamily
            sage: M = Manifold(2, 'M', structure='topological')
            sage: I = M.subset('I')
            sage: gen = (subset for subset in (M, I, M, I, M, I)); gen
            <generator object ...>
            sage: ManifoldSubsetFiniteFamily(gen)
            Set {I, M} of subsets of the 2-dimensional topological manifold M
        """
    def __lt__(self, other):
        """
        Implement the total order on instances of :class:`ManifoldObjectFiniteFamily`.

        TESTS::

            sage: from sage.manifolds.family import ManifoldSubsetFiniteFamily
            sage: M = Manifold(2, 'M', structure='topological')
            sage: A = M.subset('A')
            sage: B = M.subset('B')
            sage: sorted([ManifoldSubsetFiniteFamily([A, B]), ManifoldSubsetFiniteFamily([]),
            ....:         ManifoldSubsetFiniteFamily([B]), ManifoldSubsetFiniteFamily([A])])
            [{},
             Set {A} of subsets of the 2-dimensional topological manifold M,
             Set {A, B} of subsets of the 2-dimensional topological manifold M,
             Set {B} of subsets of the 2-dimensional topological manifold M]
        """

class ManifoldSubsetFiniteFamily(ManifoldObjectFiniteFamily):
    """
    Finite family of subsets of a topological manifold, indexed by their names.

    The class :class:`ManifoldSubsetFiniteFamily` inherits from
    :class:`ManifoldObjectFiniteFamily`.  It provides an associative
    container with specialized ``__repr__`` and ``_latex_`` methods.

    :class:`ManifoldSubsetFiniteFamily` instances are totally ordered according
    to their lexicographically ordered element (subset) names.

    EXAMPLES::

        sage: from sage.manifolds.family import ManifoldSubsetFiniteFamily
        sage: M = Manifold(2, 'M', structure='topological')
        sage: A = M.subset('A')
        sage: B = M.subset('B')
        sage: C = B.subset('C')
        sage: ManifoldSubsetFiniteFamily([A, B, C])
        Set {A, B, C} of subsets of the 2-dimensional topological manifold M
        sage: latex(_)
        \\{A, B, C\\}

    All subsets must have the same base manifold::

        sage: N = Manifold(2, 'N', structure='topological')
        sage: ManifoldSubsetFiniteFamily([M, N])
        Traceback (most recent call last):
        ...
        TypeError: all open subsets must have the same manifold
    """
    @classmethod
    def from_subsets_or_families(cls, *subsets_or_families):
        """
        Construct a ``ManifoldSubsetFiniteFamily`` from given subsets or
        iterables of subsets.

        EXAMPLES::

            sage: from sage.manifolds.family import ManifoldSubsetFiniteFamily
            sage: M = Manifold(2, 'M', structure='topological')
            sage: A = M.subset('A')
            sage: Bs = (M.subset(f'B{i}') for i in range(5))
            sage: Cs = ManifoldSubsetFiniteFamily([M.subset('C0'), M.subset('C1')])
            sage: ManifoldSubsetFiniteFamily.from_subsets_or_families(A, Bs, Cs)
            Set {A, B0, B1, B2, B3, B4, C0, C1} of subsets of the 2-dimensional topological manifold M
        """
