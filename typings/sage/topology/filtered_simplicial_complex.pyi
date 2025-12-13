from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject
from sage.topology.simplicial_complex import Simplex as Simplex, SimplicialComplex as SimplicialComplex

class FilteredSimplicialComplex(SageObject):
    """
    Define a filtered complex.

    INPUT:

    - ``simplices`` -- list of simplices and filtration values
    - ``verbose`` -- boolean (default: ``False``); if ``True``, any change to
      the filtration value of a simplex will be printed

    ``simplices`` should be a list of tuples ``(l, v)``, where
    ``l`` is a list of vertices and ``v`` is the corresponding
    filtration value.

    EXAMPLES::

        sage: FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 2.27)])
        Filtered complex on vertex set (0, 1, 2) and with simplices
         ((0,) : 0), ((1,) : 0), ((2,) : 1), ((0, 1) : 2.27000000000000)
    """
    def __init__(self, simplices=[], verbose: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 2.27)])
            sage: TestSuite(X).run()
        """
    def __eq__(self, other):
        """
        Check equality.

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 2.27)])
            sage: Y = FilteredSimplicialComplex()
            sage: Y.insert([0], 0)
            sage: Y.insert([1], 0)
            sage: Y.insert([2], 1)
            sage: Y.insert([0,1], 2.27)
            sage: X == Y
            True
            sage: Y.filtration([1,2], 2)
            sage: X == Y
            False

            sage: Y = FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 2)])
            sage: X == Y
            False
        """
    def __ne__(self, other):
        """
        Check inequality.

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 2.27)])
            sage: Y = FilteredSimplicialComplex([([0], 0), ([1], 0), ([2], 1), ([0,1], 3)])
            sage: X != Y
            True
            sage: Y.filtration([0,1], 2.27)
            sage: X != Y
            False
        """
    __call__: Incomplete
    __getitem__: Incomplete
    def insert(self, vertex_list, filtration_value) -> None:
        """
        Add a simplex to the complex.

        All faces of the simplex are added recursively if they are
        not already present, with the same value.
        If the simplex is already present, and the new value is lower
        than its current value in the complex, the value gets updated,
        otherwise it does not change. This propagates recursively to faces.

        If verbose has been enabled, this method will describe what it
        is doing during an insertion.

        INPUT:

        - ``vertex_list`` -- list of vertices
        - ``filtration_value`` -- desired value of the simplex to be added

        EXAMPLES::

            sage: X = FilteredSimplicialComplex()
            sage: X.insert(Simplex([0]),3)
            sage: X
            Filtered complex on vertex set (0,) and with simplices ((0,) : 3)

        If the verbose parameter was set to true, this method will print
        some info::

            sage: X = FilteredSimplicialComplex(verbose=True)
            sage: X.insert(Simplex([0, 1]), 2)
            Also inserting face (1,) with value 2
            Also inserting face (0,) with value 2
            sage: X.insert(Simplex([0]),1)
            Face (0,) is already in the complex.
            However its value is 2: updating it to 1
            sage: X.insert(Simplex([0]), 77)
            Face (0,) is already in the complex.
            Its value is 1: keeping it that way
        """
    def filtration(self, s, filtration_value=None):
        """
        Set filtration value of a simplex, or return value
        of existing simplex.

        INPUT:

        - ``s`` -- :class:`Simplex` for which to set or obtain the
          value of
        - ``filtration_value`` -- (optional) filtration value
          for the simplex

        If no filtration value is specified, this returns the value of
        the simplex in the complex. If the simplex is not in the complex,
        this returns ``None``.

        If ``filtration_value`` is set, this function inserts the
        simplex into the complex with the specified value.
        See documentation of :meth:`insert` for more details.

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 1)])
            sage: X.filtration(Simplex([0, 1])) is None
            True
            sage: X.filtration(Simplex([0, 1]), 2)
            sage: X.filtration([0, 1])
            2
        """
    def prune(self, threshold):
        """
        Return a copy of the filtered complex, where simplices above
        the threshold value have been removed.

        INPUT:

        - ``threshold`` -- a real value, above which simplices are discarded

        Simplices with filtration value exactly equal to ``threshold``
        are kept in the result.

        EXAMPLES::

            sage: a = FilteredSimplicialComplex()
            sage: a.insert([0], 0)
            sage: a.insert([0, 1], 1)
            sage: a.insert([0, 2], 2)
            sage: b = a.prune(1)
            sage: b
            Filtered complex on vertex set (0, 1) and
             with simplices ((0,) : 0), ((1,) : 1), ((0, 1) : 1)
        """
    def persistence_intervals(self, dimension, field: int = 2, strict: bool = True, verbose=None):
        """
        Return the list of `d`-dimensional homology elements.

        INPUT:

        - ``dimension`` -- integer; dimension `d` for which to
          return intervals
        - ``field`` -- prime number (default: 2); modulo which persistent
          homology is computed
        - ``strict`` -- boolean (default: ``True``); if ``False``, takes into account
          intervals of persistence 0
        - ``verbose`` -- (optional) if ``True``, print the steps of the
          persistent homology computation; the default is the verbosity
          of ``self``

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 1), ([0,1], 2)])
            sage: X.persistence_intervals(0)                                            # needs sage.modules
            [(1, 2), (0, +Infinity)]
        """
    def betti_number(self, k, a, b, field: int = 2, strict: bool = True, verbose=None):
        """
        Return the ``k``-dimensional Betti number from ``a`` to ``a + b``.

        INPUT:

        - ``k`` -- the dimension for the Betti number
        - ``a`` -- the lower filtration value
        - ``b`` -- the size of the interval
        - ``field`` -- prime number (default: 2); modulo which persistent
          homology is computed
        - ``strict`` -- boolean (default: ``True``); if ``False``, takes into account
          intervals of persistence 0
        - ``verbose`` -- (optional) if ``True``, print the steps of the
          persistent homology computation; the default is the verbosity
          of ``self``

        The Betti number `\\beta_k^{a,a+b}` counts the number of
        homology elements which are alive throughout the whole
        duration ``[a, a+b]``.

        EXAMPLES::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 0), ([0,1], 2)])
            sage: X.betti_number(0, 0.5, 1)                                             # needs sage.modules
            2
            sage: X.betti_number(0, 1.5, 1)                                             # needs sage.modules
            1

        If an element vanishes at time ``a + b`` exactly,
        it does not count towards the Betti number::

            sage: X = FilteredSimplicialComplex([([0], 0), ([1], 0), ([0,1], 2)])
            sage: X.betti_number(0, 1.5, 0.5)                                           # needs sage.modules
            1
        """
