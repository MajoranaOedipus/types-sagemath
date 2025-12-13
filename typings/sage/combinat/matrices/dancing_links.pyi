import _cython_3_2_1
from sage.misc.cachefunc import cached_method as cached_method
from typing import Any, overload

dlx_solver: _cython_3_2_1.cython_function_or_method
make_dlxwrapper: _cython_3_2_1.cython_function_or_method

class dancing_linksWrapper:
    """dancing_linksWrapper(rows)

    File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 95)

    A simple class that implements dancing links.

    The main methods to list the solutions are :meth:`search` and
    :meth:`get_solution`. You can also use :meth:`number_of_solutions` to count
    them.

    This class simply wraps a C++ implementation of Carlo Hamalainen."""
    def __init__(self, rows) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 108)

                Initialize our wrapper (self._x) as an actual C++ object.

                We must pass a list of rows at start up.

                EXAMPLES::

                    sage: from sage.combinat.matrices.dancing_links import dlx_solver
                    sage: rows = [[0,1,2]]
                    sage: rows+= [[0,2]]
                    sage: rows+= [[1]]
                    sage: rows+= [[3]]
                    sage: x = dlx_solver(rows)
                    sage: x
                    Dancing links solver for 4 columns and 4 rows
                    sage: x.search()
                    1
                    sage: x.get_solution()
                    [3, 0]

                ::

                    sage: rows = [[0,1,2], [1, 2]]
                    sage: from sage.combinat.matrices.dancing_links import dlx_solver
                    sage: x = dlx_solver(rows)
                    sage: x
                    Dancing links solver for 3 columns and 2 rows
                    sage: type(x)
                    <class 'sage.combinat.matrices.dancing_links.dancing_linksWrapper'>

                TESTS:

                The following example would crash in Sage's debug version
                from :issue:`13864` prior to the fix from :issue:`13882`::

                    sage: from sage.combinat.matrices.dancing_links import dlx_solver
                    sage: x = dlx_solver([])
                    sage: x.get_solution()
                    []
        """
    @overload
    def all_solutions(self, ncpus=..., column=...) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def all_solutions(self) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def all_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def all_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def all_solutions(self) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def all_solutions(self, column=...) -> Any:
        """dancing_linksWrapper.all_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 672)

        Return all solutions found after splitting the problem to allow
        parallel computation.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen

        OUTPUT: list of solutions

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: S = d.all_solutions()
            sage: sorted(sorted(s) for s in S)
            [[0, 1], [2, 3], [4, 5]]

        The number of CPUs can be specified as input::

            sage: S = Subsets(range(4))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 4 columns and 16 rows
            sage: dlx.number_of_solutions()
            15
            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=2))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        If ``ncpus=1``, the computation is not done in parallel::

            sage: sorted(sorted(s) for s in dlx.all_solutions(ncpus=1))
            [[1, 2, 3, 4],
             [1, 2, 10],
             [1, 3, 9],
             [1, 4, 8],
             [1, 14],
             [2, 3, 7],
             [2, 4, 6],
             [2, 13],
             [3, 4, 5],
             [3, 12],
             [4, 11],
             [5, 10],
             [6, 9],
             [7, 8],
             [15]]

        TESTS:

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.all_solutions()
            []

        ::

            sage: [d.all_solutions(column=i) for i in range(6)]
            [[], [], [], [], [], []]"""
    @overload
    def get_solution(self) -> Any:
        """dancing_linksWrapper.get_solution(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 329)

        Return the current solution.

        After a new solution is found using the method :meth:`search` this
        method return the rows that make up the current solution.

        TESTS::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]"""
    @overload
    def get_solution(self) -> Any:
        """dancing_linksWrapper.get_solution(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 329)

        Return the current solution.

        After a new solution is found using the method :meth:`search` this
        method return the rows that make up the current solution.

        TESTS::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]"""
    @overload
    def ncols(self) -> Any:
        """dancing_linksWrapper.ncols(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 263)

        Return the number of columns.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0], [3,4,5]]
            sage: dlx = dlx_solver(rows)
            sage: dlx.ncols()
            6"""
    @overload
    def ncols(self) -> Any:
        """dancing_linksWrapper.ncols(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 263)

        Return the number of columns.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0], [3,4,5]]
            sage: dlx = dlx_solver(rows)
            sage: dlx.ncols()
            6"""
    @overload
    def nrows(self) -> Any:
        """dancing_linksWrapper.nrows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 277)

        Return the number of rows.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0], [3,4,5]]
            sage: dlx = dlx_solver(rows)
            sage: dlx.nrows()
            4"""
    @overload
    def nrows(self) -> Any:
        """dancing_linksWrapper.nrows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 277)

        Return the number of rows.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0], [3,4,5]]
            sage: dlx = dlx_solver(rows)
            sage: dlx.nrows()
            4"""
    @overload
    def number_of_solutions(self, ncpus=..., column=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self, ncpus=..., column=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def number_of_solutions(self, ncpus=...) -> Any:
        """dancing_linksWrapper.number_of_solutions(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 788)

        Return the number of distinct solutions.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``ncpus>1`` the dancing
          links problem is split into independent subproblems to allow
          parallel computation. If ``None``, it detects the number of
          effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem, if ``None`` a random column is chosen (this argument
          is ignored if ``ncpus`` is ``1``)

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows += [[0,2]]
            sage: rows += [[1]]
            sage: rows += [[3]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions()
            2

        The number of CPUs can be specified as input::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=2, column=3)
            3

        ::

            sage: S = Subsets(range(5))
            sage: rows = map(list, S)
            sage: d = dlx_solver(rows)
            sage: d.number_of_solutions()
            52

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when counting the number of solutions a second time (:issue:`25125`)::

            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.number_of_solutions(ncpus=1)
            3
            sage: x.number_of_solutions(ncpus=1)
            3

        Works with empty rows::

            sage: dlx_solver([]).number_of_solutions(ncpus=None)
            0
            sage: dlx_solver([]).number_of_solutions(ncpus=1)
            0"""
    @overload
    def one_solution(self, ncpus=..., column=...) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self, ncpus=...) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self, ncpus=..., column=...) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self, column=...) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution(self) -> Any:
        """dancing_linksWrapper.one_solution(self, ncpus=None, column=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 568)

        Return the first solution found.

        This method allows parallel computations which might be useful for
        some kind of problems when it is very hard just to find one
        solution.

        INPUT:

        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.
        - ``column`` -- integer (default: ``None``); the column used to split
          the problem (see :meth:`restrict`). If ``None``, a random column
          is chosen. This argument is ignored if ``ncpus=1``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            For some case, increasing the number of cpus makes it
            faster. For other instances, ``ncpus=1`` is faster. It all
            depends on problem which is considered.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: sorted(d.one_solution()) in solutions
            True

        The number of CPUs can be specified as input::

            sage: sorted(d.one_solution(ncpus=2)) in solutions
            True

        The column used to split the problem for parallel computations can
        be given::

            sage: sorted(d.one_solution(ncpus=2, column=4)) in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution() is None
            True

        TESTS::

            sage: [d.one_solution(column=i) for i in range(6)]
            [None, None, None, None, None, None]

        The preprocess needed to start the parallel computation is not so
        big (less than 50ms in the example below)::

            sage: S = Subsets(range(11))
            sage: rows = list(map(list, S))
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: solution = dlx.one_solution()
            sage: subsets = [set(rows[i]) for i in solution]

        We make sure the solution is an exact cover::

            sage: set.union(*subsets)
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            sage: from itertools import combinations
            sage: any(p.intersection(q) for p,q in combinations(subsets, 2))
            False"""
    @overload
    def one_solution_using_milp_solver(self, solver=..., integrality_tolerance=...) -> Any:
        """dancing_linksWrapper.one_solution_using_milp_solver(self, solver=None, integrality_tolerance=1e-3)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 1057)

        Return a solution found using a MILP solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``); possible
          values include ``'GLPK'``, ``'GLPK/exact'``, ``'Coin'``,
          ``'CPLEX'``, ``'Gurobi'``, ``'CVXOPT'``, ``'PPL'``,
          ``'InteractiveLP'``

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``, have in
            mind that ``one_solution_using_milp_solver`` first creates (and
            caches) the MILP solver instance from the dancing links solver.
            This copy of data may take many seconds depending on the size
            of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_milp_solver() in solutions                       # needs sage.numerical.mip
            True

        Using optional solvers::

            sage: # optional - gurobi sage_numerical_backends_gurobi, needs sage.numerical.mip
            sage: s = d.one_solution_using_milp_solver('gurobi')
            sage: s in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_milp_solver() is None                            # needs sage.numerical.mip
            True"""
    @overload
    def one_solution_using_milp_solver(self) -> Any:
        """dancing_linksWrapper.one_solution_using_milp_solver(self, solver=None, integrality_tolerance=1e-3)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 1057)

        Return a solution found using a MILP solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``); possible
          values include ``'GLPK'``, ``'GLPK/exact'``, ``'Coin'``,
          ``'CPLEX'``, ``'Gurobi'``, ``'CVXOPT'``, ``'PPL'``,
          ``'InteractiveLP'``

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``, have in
            mind that ``one_solution_using_milp_solver`` first creates (and
            caches) the MILP solver instance from the dancing links solver.
            This copy of data may take many seconds depending on the size
            of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_milp_solver() in solutions                       # needs sage.numerical.mip
            True

        Using optional solvers::

            sage: # optional - gurobi sage_numerical_backends_gurobi, needs sage.numerical.mip
            sage: s = d.one_solution_using_milp_solver('gurobi')
            sage: s in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_milp_solver() is None                            # needs sage.numerical.mip
            True"""
    @overload
    def one_solution_using_milp_solver(self) -> Any:
        """dancing_linksWrapper.one_solution_using_milp_solver(self, solver=None, integrality_tolerance=1e-3)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 1057)

        Return a solution found using a MILP solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``); possible
          values include ``'GLPK'``, ``'GLPK/exact'``, ``'Coin'``,
          ``'CPLEX'``, ``'Gurobi'``, ``'CVXOPT'``, ``'PPL'``,
          ``'InteractiveLP'``

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``, have in
            mind that ``one_solution_using_milp_solver`` first creates (and
            caches) the MILP solver instance from the dancing links solver.
            This copy of data may take many seconds depending on the size
            of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_milp_solver() in solutions                       # needs sage.numerical.mip
            True

        Using optional solvers::

            sage: # optional - gurobi sage_numerical_backends_gurobi, needs sage.numerical.mip
            sage: s = d.one_solution_using_milp_solver('gurobi')
            sage: s in solutions
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_milp_solver() is None                            # needs sage.numerical.mip
            True"""
    @overload
    def one_solution_using_sat_solver(self, solver=...) -> Any:
        """dancing_linksWrapper.one_solution_using_sat_solver(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 937)

        Return a solution found using a SAT solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``),
          possible values include ``'picosat'``, ``'cryptominisat'``,
          ``'LP'``, ``'glucose'``, ``'glucose-syrup'``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``,
            have in mind that ``one_solution_using_sat_solver`` first
            creates the SAT solver instance from the dancing links
            solver. This copy of data may take many seconds depending on
            the size of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_sat_solver() in solutions                        # needs sage.sat
            True

        Using optional solvers::

            sage: s = d.one_solution_using_sat_solver('glucose')                # optional - glucose, needs sage.sat
            sage: s in solutions                                                # optional - glucose, needs sage.sat
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_sat_solver() is None                             # needs sage.sat
            True"""
    @overload
    def one_solution_using_sat_solver(self) -> Any:
        """dancing_linksWrapper.one_solution_using_sat_solver(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 937)

        Return a solution found using a SAT solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``),
          possible values include ``'picosat'``, ``'cryptominisat'``,
          ``'LP'``, ``'glucose'``, ``'glucose-syrup'``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``,
            have in mind that ``one_solution_using_sat_solver`` first
            creates the SAT solver instance from the dancing links
            solver. This copy of data may take many seconds depending on
            the size of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_sat_solver() in solutions                        # needs sage.sat
            True

        Using optional solvers::

            sage: s = d.one_solution_using_sat_solver('glucose')                # optional - glucose, needs sage.sat
            sage: s in solutions                                                # optional - glucose, needs sage.sat
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_sat_solver() is None                             # needs sage.sat
            True"""
    @overload
    def one_solution_using_sat_solver(self) -> Any:
        """dancing_linksWrapper.one_solution_using_sat_solver(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 937)

        Return a solution found using a SAT solver.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``),
          possible values include ``'picosat'``, ``'cryptominisat'``,
          ``'LP'``, ``'glucose'``, ``'glucose-syrup'``.

        OUTPUT: list of rows or ``None`` if no solution is found

        .. NOTE::

            When comparing the time taken by method ``one_solution``,
            have in mind that ``one_solution_using_sat_solver`` first
            creates the SAT solver instance from the dancing links
            solver. This copy of data may take many seconds depending on
            the size of the problem.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: solutions = [[0,1], [2,3], [4,5]]
            sage: d.one_solution_using_sat_solver() in solutions                        # needs sage.sat
            True

        Using optional solvers::

            sage: s = d.one_solution_using_sat_solver('glucose')                # optional - glucose, needs sage.sat
            sage: s in solutions                                                # optional - glucose, needs sage.sat
            True

        When no solution is found::

            sage: rows = [[0,1,2], [2,3,4,5], [0,1,2,3]]
            sage: d = dlx_solver(rows)
            sage: d.one_solution_using_sat_solver() is None                             # needs sage.sat
            True"""
    @overload
    def reinitialize(self) -> Any:
        """dancing_linksWrapper.reinitialize(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 189)

        Reinitialization of the search algorithm.

        This recreates an empty ``dancing_links`` object and adds the rows to
        the instance of ``dancing_links.``

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]

        Reinitialization of the algorithm::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None

        Reinitialization works after solutions are exhausted::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None"""
    @overload
    def reinitialize(self) -> Any:
        """dancing_linksWrapper.reinitialize(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 189)

        Reinitialization of the search algorithm.

        This recreates an empty ``dancing_links`` object and adds the rows to
        the instance of ``dancing_links.``

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]

        Reinitialization of the algorithm::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None

        Reinitialization works after solutions are exhausted::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None"""
    @overload
    def reinitialize(self) -> Any:
        """dancing_linksWrapper.reinitialize(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 189)

        Reinitialization of the search algorithm.

        This recreates an empty ``dancing_links`` object and adds the rows to
        the instance of ``dancing_links.``

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: x = dlx_solver(rows)
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]

        Reinitialization of the algorithm::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None

        Reinitialization works after solutions are exhausted::

            sage: x.reinitialize()
            sage: x.get_solution() if x.search() else None
            [0, 1]
            sage: x.get_solution() if x.search() else None
            [2, 3]
            sage: x.get_solution() if x.search() else None
            [4, 5]
            sage: x.get_solution() if x.search() else None"""
    def restrict(self, indices) -> Any:
        """dancing_linksWrapper.restrict(self, indices)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 400)

        Return a dancing links solver solving the subcase which uses some
        given rows.

        For every row that is wanted in the solution, we add a new column
        to the row to make sure it is in the solution.

        INPUT:

        - ``indices`` -- list; row indices to be found in the solution

        OUTPUT: dancing links solver

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: d
            Dancing links solver for 6 columns and 6 rows
            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]

        To impose that the `0`-th row is part of the solution, the rows of the new
        problem are::

            sage: d_using_0 = d.restrict([0])
            sage: d_using_0
            Dancing links solver for 7 columns and 6 rows
            sage: d_using_0.rows()
            [[0, 1, 2, 6], [3, 4, 5], [0, 1], [2, 3, 4, 5], [0], [1, 2, 3, 4, 5]]

        After restriction the subproblem has one more columns and the same
        number of rows as the original one::

            sage: d.restrict([1]).rows()
            [[0, 1, 2], [3, 4, 5, 6], [0, 1], [2, 3, 4, 5], [0], [1, 2, 3, 4, 5]]
            sage: d.restrict([2]).rows()
            [[0, 1, 2], [3, 4, 5], [0, 1, 6], [2, 3, 4, 5], [0], [1, 2, 3, 4, 5]]

        This method allows to find solutions where the `0`-th row is part of a
        solution::

            sage: sorted(map(sorted, d.restrict([0]).solutions_iterator()))
            [[0, 1]]

        Some other examples::

            sage: sorted(map(sorted, d.restrict([1]).solutions_iterator()))
            [[0, 1]]
            sage: sorted(map(sorted, d.restrict([2]).solutions_iterator()))
            [[2, 3]]
            sage: sorted(map(sorted, d.restrict([3]).solutions_iterator()))
            [[2, 3]]

        Here there are no solutions using both 0th and 3rd row::

            sage: list(d.restrict([0,3]).solutions_iterator())
            []

        TESTS::

            sage: d.restrict([]).rows()
            [[0, 1, 2], [3, 4, 5], [0, 1], [2, 3, 4, 5], [0], [1, 2, 3, 4, 5]]"""
    @overload
    def rows(self) -> Any:
        """dancing_linksWrapper.rows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 249)

        Return the list of rows.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0]]
            sage: x = dlx_solver(rows)
            sage: x.rows()
            [[0, 1, 2], [1, 2], [0]]"""
    @overload
    def rows(self) -> Any:
        """dancing_linksWrapper.rows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 249)

        Return the list of rows.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [1,2], [0]]
            sage: x = dlx_solver(rows)
            sage: x.rows()
            [[0, 1, 2], [1, 2], [0]]"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def search(self) -> Any:
        """dancing_linksWrapper.search(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 356)

        Search for a new solution.

        Return ``1`` if a new solution is found and ``0`` otherwise. To recover
        the solution, use the method :meth:`get_solution`.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: rows+= [[0,2]]
            sage: rows+= [[1]]
            sage: rows+= [[3]]
            sage: x = dlx_solver(rows)
            sage: print(x.search())
            1
            sage: print(x.get_solution())
            [3, 0]

        TESTS:

        Test that :issue:`11814` is fixed::

            sage: dlx_solver([]).search()
            0
            sage: dlx_solver([[]]).search()
            0

        If search is called once too often, it keeps returning 0::

            sage: x = dlx_solver([[0]])
            sage: x.search()
            1
            sage: x.search()
            0
            sage: x.search()
            0"""
    @overload
    def solutions_iterator(self) -> Any:
        """dancing_linksWrapper.solutions_iterator(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 543)

        Return an iterator of the solutions.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when iterating the solutions a second time (:issue:`25125`)::

            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]"""
    @overload
    def solutions_iterator(self) -> Any:
        """dancing_linksWrapper.solutions_iterator(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 543)

        Return an iterator of the solutions.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when iterating the solutions a second time (:issue:`25125`)::

            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]"""
    @overload
    def solutions_iterator(self) -> Any:
        """dancing_linksWrapper.solutions_iterator(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 543)

        Return an iterator of the solutions.

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]

        TESTS:

        The algorithm is automatically reinitialized if needed, for example
        when iterating the solutions a second time (:issue:`25125`)::

            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]"""
    def split(self, column) -> Any:
        """dancing_linksWrapper.split(self, column)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 474)

        Return a dict of independent solvers.

        For each ``i``-th row containing a ``1`` in the ``column``, the
        dict associates the solver giving all solution using the ``i``-th
        row.

        This is used for parallel computations.

        INPUT:

        - ``column`` -- integer; the column used to split the problem into
          independent subproblems

        OUTPUT: dict where keys are row numbers and values are dlx solvers

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [3,4,5], [0,1], [2,3,4,5], [0], [1,2,3,4,5]]
            sage: d = dlx_solver(rows)
            sage: d
            Dancing links solver for 6 columns and 6 rows
            sage: sorted(map(sorted, d.solutions_iterator()))
            [[0, 1], [2, 3], [4, 5]]

        After the split each subproblem has one more column and the same
        number of rows as the original problem::

            sage: D = d.split(0)
            sage: D
            {0: Dancing links solver for 7 columns and 6 rows,
             2: Dancing links solver for 7 columns and 6 rows,
             4: Dancing links solver for 7 columns and 6 rows}

        The (disjoint) union of the solutions of the subproblems is equal to the
        set of solutions shown above::

            sage: for x in D.values(): sorted(map(sorted, x.solutions_iterator()))
            [[0, 1]]
            [[2, 3]]
            [[4, 5]]

        TESTS::

            sage: d.split(6)
            Traceback (most recent call last):
            ...
            ValueError: column(=6) must be in range(ncols) where ncols=6

        This use to take a lot of time and memory. Not anymore since
        :issue:`24315`::

            sage: S = Subsets(range(11))
            sage: rows = map(list, S)
            sage: dlx = dlx_solver(rows)
            sage: dlx
            Dancing links solver for 11 columns and 2048 rows
            sage: d = dlx.split(0)
            sage: d[1]
            Dancing links solver for 12 columns and 2048 rows"""
    @overload
    def to_milp(self, solver=...) -> Any:
        """dancing_linksWrapper.to_milp(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 985)

        Return the mixed integer linear program (MILP) representing an
        equivalent problem.

        See also :mod:`sage.numerical.mip.MixedIntegerLinearProgram`.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``); possible
          values include ``'GLPK'``, ``'GLPK/exact'``, ``'Coin'``,
          ``'CPLEX'``, ``'Gurobi'``, ``'CVXOPT'``, ``'PPL'``,
          ``'InteractiveLP'``

        OUTPUT:

        - MixedIntegerLinearProgram instance
        - MIPVariable with binary components

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [0,2], [1], [3]]
            sage: d = dlx_solver(rows)
            sage: p,x = d.to_milp()                                                     # needs sage.numerical.mip
            sage: p                                                                     # needs sage.numerical.mip
            Boolean Program (no objective, 4 variables, ... constraints)
            sage: x                                                                     # needs sage.numerical.mip
            MIPVariable with 4 binary components

        In the reduction, the boolean variable `x_i` is ``True`` if and only if
        the `i`-th row is in the solution::

            sage: p.show()                                                              # needs sage.numerical.mip
            Constraints:...
              one 1 in 0-th column: 1.0 <= x_0 + x_1 <= 1.0
              one 1 in 1-th column: 1.0 <= x_0 + x_2 <= 1.0
              one 1 in 2-th column: 1.0 <= x_0 + x_1 <= 1.0
              one 1 in 3-th column: 1.0 <= x_3 <= 1.0
            Variables:
              x_0 is a boolean variable (min=0.0, max=1.0)
              x_1 is a boolean variable (min=0.0, max=1.0)
              x_2 is a boolean variable (min=0.0, max=1.0)
              x_3 is a boolean variable (min=0.0, max=1.0)

        Using some optional MILP solvers::

            sage: d.to_milp('gurobi')           # optional - gurobi sage_numerical_backends_gurobi, needs sage.numerical.mip
            (Boolean Program (no objective, 4 variables, 4 constraints),
             MIPVariable with 4 binary components)"""
    @overload
    def to_milp(self) -> Any:
        """dancing_linksWrapper.to_milp(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 985)

        Return the mixed integer linear program (MILP) representing an
        equivalent problem.

        See also :mod:`sage.numerical.mip.MixedIntegerLinearProgram`.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``); possible
          values include ``'GLPK'``, ``'GLPK/exact'``, ``'Coin'``,
          ``'CPLEX'``, ``'Gurobi'``, ``'CVXOPT'``, ``'PPL'``,
          ``'InteractiveLP'``

        OUTPUT:

        - MixedIntegerLinearProgram instance
        - MIPVariable with binary components

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [0,2], [1], [3]]
            sage: d = dlx_solver(rows)
            sage: p,x = d.to_milp()                                                     # needs sage.numerical.mip
            sage: p                                                                     # needs sage.numerical.mip
            Boolean Program (no objective, 4 variables, ... constraints)
            sage: x                                                                     # needs sage.numerical.mip
            MIPVariable with 4 binary components

        In the reduction, the boolean variable `x_i` is ``True`` if and only if
        the `i`-th row is in the solution::

            sage: p.show()                                                              # needs sage.numerical.mip
            Constraints:...
              one 1 in 0-th column: 1.0 <= x_0 + x_1 <= 1.0
              one 1 in 1-th column: 1.0 <= x_0 + x_2 <= 1.0
              one 1 in 2-th column: 1.0 <= x_0 + x_1 <= 1.0
              one 1 in 3-th column: 1.0 <= x_3 <= 1.0
            Variables:
              x_0 is a boolean variable (min=0.0, max=1.0)
              x_1 is a boolean variable (min=0.0, max=1.0)
              x_2 is a boolean variable (min=0.0, max=1.0)
              x_3 is a boolean variable (min=0.0, max=1.0)

        Using some optional MILP solvers::

            sage: d.to_milp('gurobi')           # optional - gurobi sage_numerical_backends_gurobi, needs sage.numerical.mip
            (Boolean Program (no objective, 4 variables, 4 constraints),
             MIPVariable with 4 binary components)"""
    @overload
    def to_sat_solver(self, solver=...) -> Any:
        """dancing_linksWrapper.to_sat_solver(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 883)

        Return the SAT solver solving an equivalent problem.

        Note that row index `i` in the dancing links solver corresponds to
        the boolean variable index `ì+1` for the SAT solver to avoid
        the variable index `0`.

        See also :mod:`sage.sat.solvers.satsolver`.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``),
          possible values include ``'picosat'``, ``'cryptominisat'``,
          ``'LP'``, ``'glucose'``, ``'glucose-syrup'``.

        OUTPUT: SAT solver instance

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [0,2], [1], [3]]
            sage: x = dlx_solver(rows)
            sage: s = x.to_sat_solver()                                                 # needs sage.sat

        Using some optional SAT solvers::

            sage: x.to_sat_solver('cryptominisat')      # optional - pycryptosat        # needs sage.sat
            CryptoMiniSat solver: 4 variables, 7 clauses."""
    @overload
    def to_sat_solver(self) -> Any:
        """dancing_linksWrapper.to_sat_solver(self, solver=None)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 883)

        Return the SAT solver solving an equivalent problem.

        Note that row index `i` in the dancing links solver corresponds to
        the boolean variable index `ì+1` for the SAT solver to avoid
        the variable index `0`.

        See also :mod:`sage.sat.solvers.satsolver`.

        INPUT:

        - ``solver`` -- string or ``None`` (default: ``None``),
          possible values include ``'picosat'``, ``'cryptominisat'``,
          ``'LP'``, ``'glucose'``, ``'glucose-syrup'``.

        OUTPUT: SAT solver instance

        EXAMPLES::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2], [0,2], [1], [3]]
            sage: x = dlx_solver(rows)
            sage: s = x.to_sat_solver()                                                 # needs sage.sat

        Using some optional SAT solvers::

            sage: x.to_sat_solver('cryptominisat')      # optional - pycryptosat        # needs sage.sat
            CryptoMiniSat solver: 4 variables, 7 clauses."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """dancing_linksWrapper.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/matrices/dancing_links.pyx (starting at line 291)

        This is used when pickling.

        TESTS::

            sage: from sage.combinat.matrices.dancing_links import dlx_solver
            sage: rows = [[0,1,2]]
            sage: X = dlx_solver(rows)
            sage: X == loads(dumps(X))
            1
            sage: rows += [[2]]
            sage: Y = dlx_solver(rows)
            sage: Y == loads(dumps(X))
            0"""
