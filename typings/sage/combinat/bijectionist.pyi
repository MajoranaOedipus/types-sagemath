from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.set_partition import SetPartition as SetPartition, SetPartitions as SetPartitions
from sage.misc.verbose import get_verbose as get_verbose
from sage.numerical.mip import MIPSolverException as MIPSolverException, MixedIntegerLinearProgram as MixedIntegerLinearProgram
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_set import DisjointSet as DisjointSet
from sage.structure.sage_object import SageObject as SageObject

class Bijectionist(SageObject):
    """
    A toolbox to list all possible bijections between two finite sets
    under various constraints.

    INPUT:

    - ``A``, ``B`` -- sets of equal size, given as a list

    - ``tau`` -- (optional) a function from ``B`` to ``Z``, in case of
      ``None``, the identity map ``lambda x: x`` is used

    - ``alpha_beta`` -- (optional) a list of pairs of statistics ``alpha`` from
      ``A`` to ``W`` and ``beta`` from ``B`` to ``W``

    - ``P`` -- (optional) a partition of ``A``

    - ``pi_rho`` -- (optional) a list of triples ``(k, pi, rho)``, where

      * ``pi`` -- a ``k``-ary operation composing objects in ``A`` and
      * ``rho`` -- a ``k``-ary function composing statistic values in ``Z``

    - ``elements_distributions`` -- (optional) a list of pairs ``(tA, tZ)``,
      specifying the distributions of ``tA``

    - ``value_restrictions`` -- (optional) a list of pairs ``(a, tZ)``,
      restricting the possible values of ``a``

    - ``solver`` -- (optional) the backend used to solve the mixed integer
      linear programs

    ``W`` and ``Z`` can be arbitrary sets.  As a natural example we may think
    of the natural numbers or tuples of integers.

    We are looking for a statistic `s: A\\to Z` and a bijection `S: A\\to B` such
    that

    - `s = \\tau \\circ S`: the statistics `s` and `\\tau` are equidistributed and
      `S` is an intertwining bijection.

    - `\\alpha = \\beta \\circ S`: the statistics `\\alpha` and `\\beta` are
      equidistributed and `S` is an intertwining bijection.

    - `s` is constant on the blocks of `P`.

    - `s(\\pi(a_1,\\dots, a_k)) = \\rho(s(a_1),\\dots, s(a_k))`.

    Additionally, we may require that

    - `s(a)\\in Z_a` for specified sets `Z_a\\subseteq Z`, and

    - `s|_{\\tilde A}` has a specified distribution for specified sets `\\tilde A
      \\subset A`.

    If `\\tau` is the identity, the two unknown functions `s` and `S` coincide.
    Although we do not exclude other bijective choices for `\\tau`, they
    probably do not make sense.

    If we want that `S` is graded, i.e. if elements of `A` and `B` have a
    notion of size and `S` should preserve this size, we can add grading
    statistics as `\\alpha` and `\\beta`.  Since `\\alpha` and `\\beta` will be
    equidistributed with `S` as an intertwining bijection, `S` will then also
    be graded.

    In summary, we have the following two commutative diagrams, where `s` and
    `S` are unknown functions.

    .. MATH::

        \\begin{array}{rrl}
                                          & A \\\\\n            {\\scriptstyle\\alpha}\\swarrow  & {\\scriptstyle S}\\downarrow & \\searrow{\\scriptstyle s}\\\\\n            W \\overset{\\beta}{\\leftarrow} & B                          & \\overset{\\tau}{\\rightarrow} Z
        \\end{array}
        \\qquad
        \\begin{array}{lcl}
            A^k                          &\\overset{\\pi}{\\rightarrow} & A\\\\\n            \\downarrow{\\scriptstyle s^k} &                           & \\downarrow{\\scriptstyle s}\\\\\n            Z^k                          &\\overset{\\rho}{\\rightarrow} & Z\\\\\n        \\end{array}

    .. NOTE::

        If `\\tau` is the identity map, the partition `P` of `A` necessarily
        consists only of singletons.

    .. NOTE::

        The order of invocation of the methods with prefix ``set``, i.e.,
        :meth:`set_statistics`, :meth:`set_intertwining_relations`,
        :meth:`set_constant_blocks`, etc., is irrelevant.  Calling any of these
        methods a second time overrides the previous specification.
    """
    def __init__(self, A, B, tau=None, alpha_beta=..., P=None, pi_rho=..., phi_psi=..., Q=None, elements_distributions=..., value_restrictions=..., solver=None, key=None) -> None:
        """
        Initialize the bijectionist.

        TESTS:

        Check that large input sets are handled well::

            sage: A = B = range(20000)
            sage: bij = Bijectionist(A, B)
        """
    def set_constant_blocks(self, P) -> None:
        """
        Declare that `s: A\\to Z` is constant on each block of `P`.

        .. WARNING::

             Any restriction imposed by a previous invocation of
             :meth:`set_constant_blocks` will be overwritten,
             including restrictions discovered by
             :meth:`set_intertwining_relations` and
             :meth:`solutions_iterator`!

        A common example is to use the orbits of a bijection acting
        on `A`.  This can be achieved using the function
        :meth:`~sage.combinat.cyclic_sieving_phenomenon.orbit_decomposition`.

        INPUT:

        - ``P`` -- set partition of `A`, singletons may be omitted

        EXAMPLES:

        Initially the partitions are set to singleton blocks.  The
        current partition can be reviewed using
        :meth:`constant_blocks`::

            sage: A = B = 'abcd'
            sage: bij = Bijectionist(A, B, lambda x: B.index(x) % 2)
            sage: bij.constant_blocks()
            {}

            sage: bij.set_constant_blocks([['a', 'c']])
            sage: bij.constant_blocks()
            {{'a', 'c'}}

        We now add a map that combines some blocks::

            sage: def pi(p1, p2): return 'abcdefgh'[A.index(p1) + A.index(p2)]
            sage: def rho(s1, s2): return (s1 + s2) % 2
            sage: bij.set_intertwining_relations((2, pi, rho))
            sage: list(bij.solutions_iterator())
            [{'a': 0, 'b': 1, 'c': 0, 'd': 1}]
            sage: bij.constant_blocks()
            {{'a', 'c'}, {'b', 'd'}}

        Setting constant blocks overrides any previous assignment::

            sage: bij.set_constant_blocks([['a', 'b']])
            sage: bij.constant_blocks()
            {{'a', 'b'}}

        If there is no solution, and the coarsest partition is
        requested, an error is raised::

            sage: bij.constant_blocks(optimal=True)
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def constant_blocks(self, singletons: bool = False, optimal: bool = False):
        '''
        Return the set partition `P` of `A` such that `s: A\\to Z` is
        known to be constant on the blocks of `P`.

        INPUT:

        - ``singletons`` -- boolean (default: ``False``); whether or not to
          include singleton blocks in the output

        - ``optimal`` -- boolean (default: ``False``); whether or not to
          compute the coarsest possible partition

        .. NOTE::

            computing the coarsest possible partition may be
            computationally expensive, but may speed up generating
            solutions.

        EXAMPLES::

            sage: A = B = ["a", "b", "c"]
            sage: bij = Bijectionist(A, B, lambda x: 0)
            sage: bij.set_constant_blocks([["a", "b"]])
            sage: bij.constant_blocks()
            {{\'a\', \'b\'}}

            sage: bij.constant_blocks(singletons=True)
            {{\'a\', \'b\'}, {\'c\'}}
        '''
    def set_statistics(self, *alpha_beta):
        """
        Set constraints of the form `\\alpha = \\beta\\circ S`.

        .. WARNING::

             Any restriction imposed by a previous invocation of
             :meth:`set_statistics` will be overwritten!

        INPUT:

        - ``alpha_beta`` -- one or more pairs `(\\alpha: A\\to W,
          \\beta: B\\to W)`

        If the statistics `\\alpha` and `\\beta` are not
        equidistributed, an error is raised.

        ALGORITHM:

        We add

        .. MATH::

            \\sum_{a\\in A, z\\in Z} x_{p(a), z} s^z t^{\\alpha(a)}
            = \\sum_{b\\in B} s^{\\tau(b)} t(\\beta(b))

        as a matrix equation to the MILP.

        EXAMPLES:

        We look for bijections `S` on permutations such that the
        number of weak exceedences of `S(\\pi)` equals the number of
        descents of `\\pi`, and statistics `s`, such that the number
        of fixed points of `S(\\pi)` equals `s(\\pi)`::

            sage: N = 4; A = B = [permutation for n in range(N) for permutation in Permutations(n)]
            sage: def wex(p): return len(p.weak_excedences())
            sage: def fix(p): return len(p.fixed_points())
            sage: def des(p): return len(p.descents(final_descent=True)) if p else 0
            sage: def adj(p): return len([e for e, f in zip(p, p[1:]+[0]) if e == f+1])
            sage: bij = Bijectionist(A, B, fix)
            sage: bij.set_statistics((wex, des), (len, len))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 3, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 3, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 3, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 0}

            sage: bij = Bijectionist(A, B, fix)
            sage: bij.set_statistics((wex, des), (fix, adj), (len, len))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 3, [3, 2, 1]: 0}

        Calling this with non-equidistributed statistics yields an error::

            sage: bij = Bijectionist(A, B, fix)
            sage: bij.set_statistics((wex, fix))
            Traceback (most recent call last):
            ...
            ValueError: statistics alpha and beta are not equidistributed

        TESTS:

        Calling ``set_statistics`` without arguments should restore the previous state::

            sage: N = 3; A = B = [permutation for n in range(N) for permutation in Permutations(n)]
            sage: def wex(p): return len(p.weak_excedences())
            sage: def fix(p): return len(p.fixed_points())
            sage: def des(p): return len(p.descents(final_descent=True)) if p else 0
            sage: bij = Bijectionist(A, B, fix)
            sage: bij.set_statistics((wex, des), (len, len))
            sage: for solution in bij.solutions_iterator():
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2}
            sage: bij.set_statistics()
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 0, [1, 2]: 1, [2, 1]: 2}
            {[]: 0, [1]: 0, [1, 2]: 2, [2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0}
            {[]: 0, [1]: 2, [1, 2]: 0, [2, 1]: 1}
            {[]: 0, [1]: 2, [1, 2]: 1, [2, 1]: 0}
            {[]: 1, [1]: 0, [1, 2]: 0, [2, 1]: 2}
            {[]: 1, [1]: 0, [1, 2]: 2, [2, 1]: 0}
            {[]: 1, [1]: 2, [1, 2]: 0, [2, 1]: 0}
            {[]: 2, [1]: 0, [1, 2]: 0, [2, 1]: 1}
            {[]: 2, [1]: 0, [1, 2]: 1, [2, 1]: 0}
            {[]: 2, [1]: 1, [1, 2]: 0, [2, 1]: 0}
        """
    def statistics_fibers(self):
        """
        Return a dictionary mapping statistic values in `W` to their
        preimages in `A` and `B`.

        This is a (computationally) fast way to obtain a first
        impression which objects in `A` should be mapped to which
        objects in `B`.

        EXAMPLES::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: def wex(p): return len(p.weak_excedences())
            sage: def fix(p): return len(p.fixed_points())
            sage: def des(p): return len(p.descents(final_descent=True)) if p else 0
            sage: def adj(p): return len([e for e, f in zip(p, p[1:]+[0]) if e == f+1])
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((len, len), (wex, des), (fix, adj))
            sage: table([[key, AB[0], AB[1]] for key, AB in bij.statistics_fibers().items()])
              (0, 0, 0)   [[]]                                [[]]
              (1, 1, 1)   [[1]]                               [[1]]
              (2, 2, 2)   [[1, 2]]                            [[2, 1]]
              (2, 1, 0)   [[2, 1]]                            [[1, 2]]
              (3, 3, 3)   [[1, 2, 3]]                         [[3, 2, 1]]
              (3, 2, 1)   [[1, 3, 2], [2, 1, 3], [3, 2, 1]]   [[1, 3, 2], [2, 1, 3], [2, 3, 1]]
              (3, 2, 0)   [[2, 3, 1]]                         [[3, 1, 2]]
              (3, 1, 0)   [[3, 1, 2]]                         [[1, 2, 3]]
        """
    def statistics_table(self, header: bool = True):
        """
        Provide information about all elements of `A` with corresponding
        `\\alpha` values and all elements of `B` with corresponding
        `\\beta` and `\\tau` values.

        INPUT:

        - ``header`` -- boolean (default: ``True``); whether to include a
          header with the standard Greek letters

        OUTPUT:

        A pair of lists suitable for :class:`~sage.misc.table.table`,
        where

        - the first contains the elements of `A` together with the
          values of `\\alpha`

        - the second contains the elements of `B` together with the
          values of `\\tau` and `\\beta`

        EXAMPLES::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: def wex(p): return len(p.weak_excedences())
            sage: def fix(p): return len(p.fixed_points())
            sage: def des(p): return len(p.descents(final_descent=True)) if p else 0
            sage: def adj(p): return len([e for e, f in zip(p, p[1:]+[0]) if e == f+1])
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((wex, des), (fix, adj))
            sage: a, b = bij.statistics_table()
            sage: table(a, header_row=True, frame=True)
            ┌───────────┬────────┬────────┐
            │ a         │ α_1(a) │ α_2(a) │
            ╞═══════════╪════════╪════════╡
            │ []        │ 0      │ 0      │
            ├───────────┼────────┼────────┤
            │ [1]       │ 1      │ 1      │
            ├───────────┼────────┼────────┤
            │ [1, 2]    │ 2      │ 2      │
            ├───────────┼────────┼────────┤
            │ [2, 1]    │ 1      │ 0      │
            ├───────────┼────────┼────────┤
            │ [1, 2, 3] │ 3      │ 3      │
            ├───────────┼────────┼────────┤
            │ [1, 3, 2] │ 2      │ 1      │
            ├───────────┼────────┼────────┤
            │ [2, 1, 3] │ 2      │ 1      │
            ├───────────┼────────┼────────┤
            │ [2, 3, 1] │ 2      │ 0      │
            ├───────────┼────────┼────────┤
            │ [3, 1, 2] │ 1      │ 0      │
            ├───────────┼────────┼────────┤
            │ [3, 2, 1] │ 2      │ 1      │
            └───────────┴────────┴────────┘
            sage: table(b, header_row=True, frame=True)
            ┌───────────┬───┬────────┬────────┐
            │ b         │ τ │ β_1(b) │ β_2(b) │
            ╞═══════════╪═══╪════════╪════════╡
            │ []        │ 0 │ 0      │ 0      │
            ├───────────┼───┼────────┼────────┤
            │ [1]       │ 1 │ 1      │ 1      │
            ├───────────┼───┼────────┼────────┤
            │ [1, 2]    │ 2 │ 1      │ 0      │
            ├───────────┼───┼────────┼────────┤
            │ [2, 1]    │ 1 │ 2      │ 2      │
            ├───────────┼───┼────────┼────────┤
            │ [1, 2, 3] │ 3 │ 1      │ 0      │
            ├───────────┼───┼────────┼────────┤
            │ [1, 3, 2] │ 2 │ 2      │ 1      │
            ├───────────┼───┼────────┼────────┤
            │ [2, 1, 3] │ 2 │ 2      │ 1      │
            ├───────────┼───┼────────┼────────┤
            │ [2, 3, 1] │ 2 │ 2      │ 1      │
            ├───────────┼───┼────────┼────────┤
            │ [3, 1, 2] │ 2 │ 2      │ 0      │
            ├───────────┼───┼────────┼────────┤
            │ [3, 2, 1] │ 1 │ 3      │ 3      │
            └───────────┴───┴────────┴────────┘

        TESTS:

        If no statistics are given, the table should still be able to be generated::

            sage: A = B = [permutation for n in range(3) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: a, b = bij.statistics_table()
            sage: table(a, header_row=True, frame=True)
            ┌────────┐
            │ a      │
            ╞════════╡
            │ []     │
            ├────────┤
            │ [1]    │
            ├────────┤
            │ [1, 2] │
            ├────────┤
            │ [2, 1] │
            └────────┘
            sage: table(b, header_row=True, frame=True)
            ┌────────┬───┐
            │ b      │ τ │
            ╞════════╪═══╡
            │ []     │ 0 │
            ├────────┼───┤
            │ [1]    │ 1 │
            ├────────┼───┤
            │ [1, 2] │ 2 │
            ├────────┼───┤
            │ [2, 1] │ 1 │
            └────────┴───┘

        We can omit the header::

            sage: bij.statistics_table(header=True)[1]
            [['b', 'τ'], [[], 0], [[1], 1], [[1, 2], 2], [[2, 1], 1]]
            sage: bij.statistics_table(header=False)[1]
            [[[], 0], [[1], 1], [[1, 2], 2], [[2, 1], 1]]
        """
    def set_value_restrictions(self, *value_restrictions) -> None:
        """
        Restrict the set of possible values `s(a)` for a given element
        `a`.

        .. WARNING::

             Any restriction imposed by a previous invocation of
             :meth:`set_value_restrictions` will be overwritten!

        INPUT:

        - ``value_restrictions`` -- one or more pairs `(a\\in A, \\tilde
          Z\\subseteq Z)`

        EXAMPLES:

        We may want to restrict the value of a given element to a
        single or multiple values.  We do not require that the
        specified values are in the image of `\\tau`.  In some
        cases, the restriction may not be able to provide a better
        solution, as for size 3 in the following example. ::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((len, len))
            sage: bij.set_value_restrictions((Permutation([1, 2]), [1]),
            ....:                            (Permutation([3, 2, 1]), [2, 3, 4]))
            sage: for sol in sorted(bij.solutions_iterator(), key=lambda d: sorted(d.items())):
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 3, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 3, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 2, [2, 1, 3]: 3, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 3, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 3, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 1, [2, 1, 3]: 3, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 3, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 3, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 3, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 3, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 3, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 2, [2, 1, 3]: 3, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}

        However, an error occurs if the set of possible values is
        empty.  In this example, the image of `\\tau` under any
        legal bijection is disjoint to the specified values.

        TESTS::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_value_restrictions((Permutation([1, 2]), [4, 5]))
            sage: bij._compute_possible_block_values()
            Traceback (most recent call last):
            ...
            ValueError: no possible values found for singleton block [[1, 2]]

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([[permutation for permutation in Permutations(n)] for n in range(4)])
            sage: bij.set_value_restrictions((Permutation([1, 2]), [4, 5]))
            sage: bij._compute_possible_block_values()
            Traceback (most recent call last):
            ...
            ValueError: no possible values found for block [[1, 2], [2, 1]]

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_value_restrictions(((1, 2), [4, 5, 6]))
            Traceback (most recent call last):
            ...
            AssertionError: element (1, 2) was not found in A
        """
    def set_distributions(self, *elements_distributions) -> None:
        """
        Specify the distribution of `s` for a subset of elements.

        .. WARNING::

             Any restriction imposed by a previous invocation of
             :meth:`set_distributions` will be overwritten!

        INPUT:

        - one or more pairs of `(\\tilde A, \\tilde Z)`, where `\\tilde
          A\\subseteq A` and `\\tilde Z` is a list of values in `Z` of
          the same size as `\\tilde A`

        This method specifies that `\\{s(a) | a\\in\\tilde A\\}` equals
        `\\tilde Z` as a multiset for each of the pairs.

        When specifying several distributions, the subsets of `A` do
        not have to be disjoint.

        ALGORITHM:

        We add

        .. MATH::

            \\sum_{a\\in\\tilde A} x_{p(a), z}t^z = \\sum_{z\\in\\tilde Z} t^z,

        where `p(a)` is the block containing `a`, for each given
        distribution as a vector equation to the MILP.

        EXAMPLES::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((len, len))
            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([1, 3, 2])], [1, 3]))
            sage: for sol in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 1, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}

            sage: bij.constant_blocks(optimal=True)
            {{[2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]}}
            sage: sorted(bij.minimal_subdistributions_blocks_iterator(), key=lambda d: (len(d[0]), d[0]))
            [([[]], [0]),
             ([[1]], [1]),
             ([[2, 1, 3]], [2]),
             ([[1, 2], [2, 1]], [1, 2]),
             ([[1, 2, 3], [1, 3, 2]], [1, 3])]

        We may also specify multiple, possibly overlapping distributions::

            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([1, 3, 2])], [1, 3]),
            ....:                       ([Permutation([1, 3, 2]), Permutation([3, 2, 1]),
            ....:                        Permutation([2, 1, 3])], [1, 2, 2]))
            sage: for sol in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}

            sage: bij.constant_blocks(optimal=True)
            {{[1], [1, 3, 2]}, {[2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]}}
            sage: sorted(bij.minimal_subdistributions_blocks_iterator(), key=lambda d: (len(d[0]), d[0]))
            [([[]], [0]),
             ([[1]], [1]),
             ([[1, 2, 3]], [3]),
             ([[2, 3, 1]], [2]),
             ([[1, 2], [2, 1]], [1, 2])]

        TESTS:

        Because of the current implementation of the output calculation, we do
        not improve our solution if we do not gain any unique solutions::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((len, len))
            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([1, 3, 2])], [2, 3]))
            sage: for sol in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 1, [2, 1]: 2, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 1, [3, 1, 2]: 2, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}

        Another example with statistics::

            sage: bij = Bijectionist(A, B, tau)
            sage: def alpha(p): return p(1) if len(p) > 0 else 0
            sage: def beta(p): return p(1) if len(p) > 0 else 0
            sage: bij.set_statistics((alpha, beta), (len, len))
            sage: for sol in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 2, [1, 3, 2]: 3, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 1, [3, 2, 1]: 2}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}

        The solution above is not unique.  We can add a feasible distribution to force uniqueness::

            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((alpha, beta), (len, len))
            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([3, 2, 1])], [1, 3]))
            sage: for sol in bij.solutions_iterator():
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 1, [1, 2, 3]: 3, [1, 3, 2]: 2, [2, 1, 3]: 2, [2, 3, 1]: 2, [3, 1, 2]: 2, [3, 2, 1]: 1}

        Let us try to add a distribution that cannot be satisfied,
        because there is no solution where a permutation that starts
        with 1 is mapped onto 1::

            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((alpha, beta), (len, len))
            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([1, 3, 2])], [1, 3]))
            sage: list(bij.solutions_iterator())
            []

        The specified elements have to be in `A` and have to be of the same size::

            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((len, len))
            sage: bij.set_distributions(([Permutation([1, 2, 3, 4])], [1]))
            Traceback (most recent call last):
            ...
            ValueError: element [1, 2, 3, 4] was not found in A
            sage: bij.set_distributions(([Permutation([1, 2, 3])], [-1]))
            Traceback (most recent call last):
            ...
            ValueError: value -1 was not found in tau(A)

        Note that the same error occurs when an element that is not the first element of the list is
        not in `A`.
        """
    def set_intertwining_relations(self, *pi_rho) -> None:
        """
        Add restrictions of the form `s(\\pi(a_1,\\dots, a_k)) =
        \\rho(s(a_1),\\dots, s(a_k))`.

        .. WARNING::

             Any restriction imposed by a previous invocation of
             :meth:`set_intertwining_relations` will be overwritten!

        INPUT:

        - ``pi_rho`` -- one or more tuples `(k, \\pi: A^k\\to A, \\rho:
          Z^k\\to Z, \\tilde A)` where `\\tilde A` (optional) is a
          `k`-ary function that returns true if and only if a
          `k`-tuple of objects in `A` is in the domain of `\\pi`

        ALGORITHM:

        The relation

        .. MATH::

            s(\\pi(a_1,\\dots, a_k)) = \\rho(s(a_1),\\dots, s(a_k))

        for each pair `(\\pi, \\rho)` implies immediately that
        `s(\\pi(a_1,\\dots, a_k))` only depends on the blocks of
        `a_1,\\dots, a_k`.

        The MILP formulation is as follows.  Let `a_1,\\dots,a_k \\in
        A` and let `a = \\pi(a_1,\\dots,a_k)`.  Let `z_1,\\dots,z_k \\in
        Z` and let `z = \\rho(z_1,\\dots,z_k)`.  Suppose that `a_i\\in
        p_i` for all `i` and that `a\\in p`.

        We then want to model the implication

        .. MATH::

           x_{p_1, z_1} = 1,\\dots, x_{p_k, z_k} = 1 \\Rightarrow x_{p, z} = 1.

        We achieve this by requiring

        .. MATH::

            x_{p, z}\\geq 1 - k + \\sum_{i=1}^k x_{p_i, z_i}.

        Note that `z` must be a possible value of `p` and each `z_i`
        must be a possible value of `p_i`.

        EXAMPLES:

        We can concatenate two permutations by increasing the values
        of the second permutation by the length of the first
        permutation::

            sage: def concat(p1, p2): return Permutation(p1 + [i + len(p1) for i in p2])

        We may be interested in statistics on permutations which are
        equidistributed with the number of fixed points, such that
        concatenating permutations corresponds to adding statistic
        values::

            sage: A = B = [permutation for n in range(4) for permutation in Permutations(n)]
            sage: bij = Bijectionist(A, B, Permutation.number_of_fixed_points)
            sage: bij.set_statistics((len, len))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            ...
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 3}
            ...
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 1, [2, 1, 3]: 3, [2, 3, 1]: 0, [3, 1, 2]: 0, [3, 2, 1]: 1}
            ...

            sage: bij.set_intertwining_relations((2, concat, lambda x, y: x + y))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 0, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 1, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 0, [3, 2, 1]: 0}

        The domain of the composition may be restricted.  E.g., if we
        concatenate only permutations starting with a 1, we obtain
        fewer forced elements::

            sage: in_domain = lambda p1, p2: (not p1 or p1(1) == 1) and (not p2 or p2(1) == 1)
            sage: bij.set_intertwining_relations((2, concat, lambda x, y: x + y, in_domain))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 0, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 1, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 0, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 0, [3, 1, 2]: 1, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 0, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 0, [3, 2, 1]: 1}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 0, [3, 1, 2]: 1, [3, 2, 1]: 0}
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 0, [1, 2, 3]: 3, [1, 3, 2]: 1, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 0, [3, 2, 1]: 0}

        We can also restrict according to several composition
        functions.  For example, we may additionally concatenate
        permutations by incrementing the elements of the first::

            sage: skew_concat = lambda p1, p2: Permutation([i + len(p2) for i in p1] + list(p2))
            sage: bij.set_intertwining_relations((2, skew_concat, lambda x, y: x + y))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 0, [1, 3, 2]: 0, [2, 1, 3]: 1, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 0, [1, 3, 2]: 1, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 3}
            {[]: 0, [1]: 1, [1, 2]: 0, [2, 1]: 2, [1, 2, 3]: 1, [1, 3, 2]: 0, [2, 1, 3]: 0, [2, 3, 1]: 1, [3, 1, 2]: 1, [3, 2, 1]: 3}

        However, this yields no solution::

            sage: bij.set_intertwining_relations((2, concat, lambda x, y: x + y), (2, skew_concat, lambda x, y: x + y))
            sage: list(bij.solutions_iterator())
            []
        """
    set_semi_conjugacy = set_intertwining_relations
    def set_quadratic_relation(self, *phi_psi) -> None:
        """
        Add restrictions of the form `s\\circ\\psi\\circ s = \\phi`.

        INPUT:

        - ``phi_psi`` -- (optional) a list of pairs `(\\phi, \\rho)` where `\\phi:
          A\\to Z` and `\\psi: Z\\to A`

        ALGORITHM:

        We add

        .. MATH::

            x_{p(a), z} = x_{p(\\psi(z)), \\phi(a)}

        for `a\\in A` and `z\\in Z` to the MILP, where `\\phi:A\\to Z`
        and `\\psi:Z\\to A`.  Note that, in particular, `\\phi` must be
        constant on blocks.

        EXAMPLES::

            sage: A = B = DyckWords(3)
            sage: bij = Bijectionist(A, B)
            sage: bij.set_statistics((lambda D: D.number_of_touch_points(), lambda D: D.number_of_initial_rises()))
            sage: ascii_art(sorted(bij.minimal_subdistributions_iterator()))
            [ (             [   /\\   ] )
            [ (             [  /  \\  ] )  ( [    /\\    /\\    ]  [  /\\      /\\/\\  ] )
            [ ( [ /\\/\\/\\ ], [ /    \\ ] ), ( [ /\\/  \\, /  \\/\\ ], [ /  \\/\\, /    \\ ] ),
            <BLANKLINE>
             ( [           /\\   ]                     ) ]
             ( [  /\\/\\    /  \\  ]  [            /\\  ] ) ]
             ( [ /    \\, /    \\ ], [ /\\/\\/\\, /\\/  \\ ] ) ]
            sage: bij.set_quadratic_relation((lambda D: D, lambda D: D))
            sage: ascii_art(sorted(bij.minimal_subdistributions_iterator()))
            [ (             [   /\\   ] )
            [ (             [  /  \\  ] )  ( [    /\\  ]  [  /\\/\\  ] )
            [ ( [ /\\/\\/\\ ], [ /    \\ ] ), ( [ /\\/  \\ ], [ /    \\ ] ),
            <BLANKLINE>
            <BLANKLINE>
             ( [  /\\    ]  [  /\\    ] )  ( [  /\\/\\  ]  [    /\\  ] )
             ( [ /  \\/\\ ], [ /  \\/\\ ] ), ( [ /    \\ ], [ /\\/  \\ ] ),
            <BLANKLINE>
             ( [   /\\   ]             ) ]
             ( [  /  \\  ]             ) ]
             ( [ /    \\ ], [ /\\/\\/\\ ] ) ]
        """
    def set_homomesic(self, Q) -> None:
        """
        Assert that the average of `s` on each block of `Q` is
        constant.

        INPUT:

        - ``Q`` -- set partition of ``A``

        EXAMPLES::

            sage: A = B = [1,2,3]
            sage: bij = Bijectionist(A, B, lambda b: b % 3)
            sage: bij.set_homomesic([[1,2], [3]])
            sage: list(bij.solutions_iterator())
            [{1: 2, 2: 0, 3: 1}, {1: 0, 2: 2, 3: 1}]
        """
    def possible_values(self, p=None, optimal: bool = False):
        '''
        Return for each block the values of `s` compatible with the
        imposed restrictions.

        INPUT:

        - ``p`` -- (optional) a block of `P`, or an element of a
          block of `P`, or a list of these

        - ``optimal`` -- boolean (default: ``False``); whether or not to
          compute the minimal possible set of statistic values

        .. NOTE::

            Computing the minimal possible set of statistic values
            may be computationally expensive.

        .. TODO::

            currently, calling this method with ``optimal=True`` does
            not update the internal dictionary, because this would
            interfere with the variables of the MILP.

        EXAMPLES::

            sage: A = B = ["a", "b", "c", "d"]
            sage: tau = {"a": 1, "b": 1, "c": 1, "d": 2}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a", "b"]])
            sage: bij.possible_values(A)
            {\'a\': {1, 2}, \'b\': {1, 2}, \'c\': {1, 2}, \'d\': {1, 2}}
            sage: bij.possible_values(A, optimal=True)
            {\'a\': {1}, \'b\': {1}, \'c\': {1, 2}, \'d\': {1, 2}}

        The internal dictionary is not updated::

            sage: bij.possible_values(A)
            {\'a\': {1, 2}, \'b\': {1, 2}, \'c\': {1, 2}, \'d\': {1, 2}}

        TESTS::

            sage: A = B = ["a", "b", "c", "d"]
            sage: tau = {"a": 1, "b": 1, "c": 2, "d": 2}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a", "b"]])

        Test if all formats are really possible::

            sage: bij.possible_values(p=\'a\')
            {\'a\': {1, 2}, \'b\': {1, 2}}
            sage: bij.possible_values(p=["a", "b"])
            {\'a\': {1, 2}, \'b\': {1, 2}}
            sage: bij.possible_values(p=[["a", "b"]])
            {\'a\': {1, 2}, \'b\': {1, 2}}
            sage: bij.possible_values(p=[["a", "b"], ["c"]])
            {\'a\': {1, 2}, \'b\': {1, 2}, \'c\': {1, 2}}

        Test an unfeasible problem::

            sage: A = B = \'ab\'
            sage: bij = Bijectionist(A, B, lambda x: B.index(x) % 2)
            sage: bij.set_constant_blocks([[\'a\', \'b\']])
            sage: bij.possible_values(p=\'a\')
            {\'a\': {0, 1}, \'b\': {0, 1}}
            sage: bij.possible_values(p=\'a\', optimal=True)
            {\'a\': set(), \'b\': set()}
        '''
    def minimal_subdistributions_iterator(self) -> Generator[Incomplete]:
        '''
        Return all minimal subsets `\\tilde A` of `A`
        together with submultisets `\\tilde Z` with `s(\\tilde A) =
        \\tilde Z` as multisets.

        EXAMPLES::

            sage: A = B = [permutation for n in range(3) for permutation in Permutations(n)]
            sage: bij = Bijectionist(A, B, len)
            sage: bij.set_statistics((len, len))
            sage: for sol in bij.solutions_iterator():
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 2}
            sage: sorted(bij.minimal_subdistributions_iterator())
            [([[]], [0]), ([[1]], [1]), ([[1, 2]], [2]), ([[2, 1]], [2])]

        Another example::

            sage: N = 2; A = B = [dyck_word for n in range(N+1) for dyck_word in DyckWords(n)]
            sage: def tau(D): return D.number_of_touch_points()
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((lambda d: d.semilength(), lambda d: d.semilength()))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1, 0]: 1, [1, 0, 1, 0]: 1, [1, 1, 0, 0]: 2}
            {[]: 0, [1, 0]: 1, [1, 0, 1, 0]: 2, [1, 1, 0, 0]: 1}
            sage: for subdistribution in bij.minimal_subdistributions_iterator():
            ....:     print(subdistribution)
            ([[]], [0])
            ([[1, 0]], [1])
            ([[1, 0, 1, 0], [1, 1, 0, 0]], [1, 2])

        An example with two elements of the same block in a subdistribution::

            sage: A = B = ["a", "b", "c", "d", "e"]
            sage: tau = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a", "b"]])
            sage: bij.set_value_restrictions(("a", [1, 2]))
            sage: bij.constant_blocks(optimal=True)
            {{\'a\', \'b\'}}
            sage: list(bij.minimal_subdistributions_iterator())
            [([\'a\', \'b\', \'c\', \'d\', \'e\'], [1, 1, 2, 2, 3])]
        '''
    def minimal_subdistributions_blocks_iterator(self) -> Generator[Incomplete]:
        '''
        Return all representatives of minimal subsets `\\tilde P`
        of `P` together with submultisets `\\tilde Z`
        with `s(\\tilde P) = \\tilde Z` as multisets.

        .. WARNING::

            If there are several solutions with the same support
            (i.e., the sets of block representatives are the same),
            only one of these will be found, even if the
            distributions are different, see the doctest below.  To
            find all solutions, use
            :meth:`minimal_subdistributions_iterator`, which is,
            however, computationally more expensive.

        EXAMPLES::

            sage: A = B = [permutation for n in range(3) for permutation in Permutations(n)]
            sage: bij = Bijectionist(A, B, len)
            sage: bij.set_statistics((len, len))
            sage: for sol in bij.solutions_iterator():
            ....:     print(sol)
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 2}
            sage: sorted(bij.minimal_subdistributions_blocks_iterator())
            [([[]], [0]), ([[1]], [1]), ([[1, 2]], [2]), ([[2, 1]], [2])]

        Another example::

            sage: N = 2; A = B = [dyck_word for n in range(N+1) for dyck_word in DyckWords(n)]
            sage: def tau(D): return D.number_of_touch_points()
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_statistics((lambda d: d.semilength(), lambda d: d.semilength()))
            sage: for solution in sorted(list(bij.solutions_iterator()), key=lambda d: tuple(sorted(d.items()))):
            ....:     print(solution)
            {[]: 0, [1, 0]: 1, [1, 0, 1, 0]: 1, [1, 1, 0, 0]: 2}
            {[]: 0, [1, 0]: 1, [1, 0, 1, 0]: 2, [1, 1, 0, 0]: 1}
            sage: for subdistribution in bij.minimal_subdistributions_blocks_iterator():
            ....:     print(subdistribution)
            ([[]], [0])
            ([[1, 0]], [1])
            ([[1, 0, 1, 0], [1, 1, 0, 0]], [1, 2])

        An example with two elements of the same block in a subdistribution::

            sage: A = B = ["a", "b", "c", "d", "e"]
            sage: tau = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a", "b"]])
            sage: bij.set_value_restrictions(("a", [1, 2]))
            sage: bij.constant_blocks(optimal=True)
            {{\'a\', \'b\'}}
            sage: list(bij.minimal_subdistributions_blocks_iterator())
            [([\'b\', \'b\', \'c\', \'d\', \'e\'], [1, 1, 2, 2, 3])]

        An example with overlapping minimal subdistributions::

            sage: A = B = ["a", "b", "c", "d", "e"]
            sage: tau = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_distributions((["a", "b"], [1, 2]), (["a", "c", "d"], [1, 2, 3]))
            sage: sorted(bij.solutions_iterator(), key=lambda d: tuple(sorted(d.items())))
            [{\'a\': 1, \'b\': 2, \'c\': 2, \'d\': 3, \'e\': 1},
             {\'a\': 1, \'b\': 2, \'c\': 3, \'d\': 2, \'e\': 1},
             {\'a\': 2, \'b\': 1, \'c\': 1, \'d\': 3, \'e\': 2},
             {\'a\': 2, \'b\': 1, \'c\': 3, \'d\': 1, \'e\': 2}]
            sage: bij.constant_blocks(optimal=True)
            {{\'a\', \'e\'}}
            sage: list(bij.minimal_subdistributions_blocks_iterator())
            [([\'a\', \'b\'], [1, 2]), ([\'a\', \'c\', \'d\'], [1, 2, 3])]

        Fedor Petrov\'s example from https://mathoverflow.net/q/424187::

            sage: A = B = ["a"+str(i) for i in range(1, 9)] + ["b"+str(i) for i in range(3, 9)] + ["d"]
            sage: tau = {b: 0 if i < 10 else 1 for i, b in enumerate(B)}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a"+str(i), "b"+str(i)] for i in range(1, 9) if "b"+str(i) in A])
            sage: d = [0]*8+[1]*4
            sage: bij.set_distributions((A[:8] + A[8+2:-1], d), (A[:8] + A[8:-3], d))
            sage: sorted([s[a] for a in A] for s in bij.solutions_iterator())
            [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
             [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]

            sage: sorted(bij.minimal_subdistributions_blocks_iterator())        # random
            [([\'a1\', \'a2\', \'a3\', \'a4\', \'a5\', \'a5\', \'a6\', \'a6\', \'a7\', \'a7\', \'a8\', \'a8\'],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
             ([\'a3\', \'a4\', \'d\'], [0, 0, 1]),
             ([\'a7\', \'a8\', \'d\'], [0, 0, 1])]

        The following solution is not found, because it happens to
        have the same support as the other::

            sage: D = set(A).difference([\'b7\', \'b8\', \'d\'])
            sage: sorted(a.replace("b", "a") for a in D)
            [\'a1\', \'a2\', \'a3\', \'a3\', \'a4\', \'a4\', \'a5\', \'a5\', \'a6\', \'a6\', \'a7\', \'a8\']
            sage: set(tuple(sorted(s[a] for a in D)) for s in bij.solutions_iterator())
            {(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1)}

        But it is, by design, included here::

            sage: sorted(D) in [d for d, _ in bij.minimal_subdistributions_iterator()]
            True
        '''
    def solutions_iterator(self) -> Generator[Incomplete, Incomplete]:
        '''
        An iterator over all solutions of the problem.

        OUTPUT: an iterator over all possible mappings `s: A\\to Z`

        ALGORITHM:

        We solve an integer linear program with a binary variable
        `x_{p, z}` for each partition block `p\\in P` and each
        statistic value `z\\in Z`:

        - `x_{p, z} = 1` if and only if `s(a) = z` for all `a\\in p`.

        Then we add the constraint `\\sum_{x\\in V} x<|V|`, where `V`
        is the set containing all `x` with `x = 1`, that is, those
        indicator variables representing the current solution.
        Therefore, a solution of this new program must be different
        from all those previously obtained.

        INTEGER LINEAR PROGRAM:

        * Let `m_w(p)`, for a block `p` of `P`, be the multiplicity
          of the value `w` in `W` under `\\alpha`, that is, the number
          of elements `a \\in p` with `\\alpha(a)=w`.

        * Let `n_w(z)` be the number of elements `b \\in B` with
          `\\beta(b)=w` and `\\tau(b)=z` for `w \\in W`, `z \\in Z`.

        * Let `k` be the arity of a pair `(\\pi, \\rho)` in an
          intertwining relation.

        and the following constraints:

        * because every block is assigned precisely one value, for
          all `p\\in P`,

        .. MATH::

            \\sum_z x_{p, z} = 1.

        * because the statistics `s` and `\\tau` and also `\\alpha` and
          `\\beta` are equidistributed, for all `w\\in W` and `z\\in Z`,

        .. MATH::

            \\sum_p m_w(p) x_{p, z} = n_w(z).

        * for each intertwining relation `s(\\pi(a_1,\\dots, a_k)) =
          \\rho(s(a_1),\\dots, s(a_r))`, and for all `k`-combinations
          of blocks `p_i\\in P` such that there exist `(a_1,\\dots,
          a_k)\\in p_1\\times\\dots\\times p_k` with `\\pi(a_1,\\dots,
          a_k)\\in W` and `z = \\rho(z_1,\\dots, z_k)`,

        .. MATH::

            x_{p, z} \\geq 1-k + \\sum_{i=1}^k x_{p_i, z_i}.

        * for each distribution restriction, i.e. a set of elements
          `\\tilde A` and a distribution of values given by integers
          `d_z` representing the multiplicity of each `z \\in Z`, and
          `r_p = |p \\cap\\tilde A|` indicating the relative size of
          block `p` in the set of elements of the distribution,

        .. MATH::

            \\sum_p r_p x_{p, z} = d_z.

        EXAMPLES::

            sage: A = B = \'abc\'
            sage: bij = Bijectionist(A, B, lambda x: B.index(x) % 2, solver=\'GLPK\')
            sage: next(bij.solutions_iterator())
            {\'a\': 0, \'b\': 1, \'c\': 0}

            sage: list(bij.solutions_iterator())
            [{\'a\': 0, \'b\': 1, \'c\': 0},
             {\'a\': 1, \'b\': 0, \'c\': 0},
             {\'a\': 0, \'b\': 0, \'c\': 1}]

            sage: N = 4
            sage: A = B = [permutation for n in range(N) for permutation in Permutations(n)]

        Let `\\tau` be the number of non-left-to-right-maxima of a
        permutation::

            sage: def tau(pi):
            ....:    pi = list(pi)
            ....:    i = count = 0
            ....:    for j in range(len(pi)):
            ....:        if pi[j] > i:
            ....:            i = pi[j]
            ....:        else:
            ....:            count += 1
            ....:    return count

        We look for a statistic which is constant on conjugacy classes::

            sage: P = [list(a) for n in range(N) for a in Permutations(n).conjugacy_classes()]

            sage: bij = Bijectionist(A, B, tau, solver=\'GLPK\')
            sage: bij.set_statistics((len, len))
            sage: bij.set_constant_blocks(P)
            sage: for solution in bij.solutions_iterator():
            ....:     print(solution)
            {[]: 0, [1]: 0, [1, 2]: 1, [2, 1]: 0, [1, 2, 3]: 0, [1, 3, 2]: 1, [2, 1, 3]: 1, [3, 2, 1]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2}
            {[]: 0, [1]: 0, [1, 2]: 0, [2, 1]: 1, [1, 2, 3]: 0, [1, 3, 2]: 1, [2, 1, 3]: 1, [3, 2, 1]: 1, [2, 3, 1]: 2, [3, 1, 2]: 2}

        Changing or re-setting problem parameters clears the internal
        cache.  Setting the verbosity prints the MILP which is solved.::

            sage: set_verbose(2)
            sage: bij.set_constant_blocks(P)
            sage: _ = list(bij.solutions_iterator())
            Constraints are:
                block []: 1 <= x_0 <= 1
                block [1]: 1 <= x_1 <= 1
                block [1, 2]: 1 <= x_2 + x_3 <= 1
                block [2, 1]: 1 <= x_4 + x_5 <= 1
                block [1, 2, 3]: 1 <= x_6 + x_7 + x_8 <= 1
                block [1, 3, 2]: 1 <= x_9 + x_10 + x_11 <= 1
                block [2, 3, 1]: 1 <= x_12 + x_13 + x_14 <= 1
                statistics: 1 <= x_0 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_1 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_2 + x_4 <= 1
                statistics: 1 <= x_3 + x_5 <= 1
                statistics: 0 <= <= 0
                statistics: 1 <= x_6 + 3 x_9 + 2 x_12 <= 1
                statistics: 3 <= x_7 + 3 x_10 + 2 x_13 <= 3
                statistics: 2 <= x_8 + 3 x_11 + 2 x_14 <= 2
            Variables are:
                x_0: s([]) = 0
                x_1: s([1]) = 0
                x_2: s([1, 2]) = 0
                x_3: s([1, 2]) = 1
                x_4: s([2, 1]) = 0
                x_5: s([2, 1]) = 1
                x_6: s([1, 2, 3]) = 0
                x_7: s([1, 2, 3]) = 1
                x_8: s([1, 2, 3]) = 2
                x_9: s([1, 3, 2]) = s([2, 1, 3]) = s([3, 2, 1]) = 0
                x_10: s([1, 3, 2]) = s([2, 1, 3]) = s([3, 2, 1]) = 1
                x_11: s([1, 3, 2]) = s([2, 1, 3]) = s([3, 2, 1]) = 2
                x_12: s([2, 3, 1]) = s([3, 1, 2]) = 0
                x_13: s([2, 3, 1]) = s([3, 1, 2]) = 1
                x_14: s([2, 3, 1]) = s([3, 1, 2]) = 2
            after vetoing
            Constraints are:
                block []: 1 <= x_0 <= 1
                block [1]: 1 <= x_1 <= 1
                block [1, 2]: 1 <= x_2 + x_3 <= 1
                block [2, 1]: 1 <= x_4 + x_5 <= 1
                block [1, 2, 3]: 1 <= x_6 + x_7 + x_8 <= 1
                block [1, 3, 2]: 1 <= x_9 + x_10 + x_11 <= 1
                block [2, 3, 1]: 1 <= x_12 + x_13 + x_14 <= 1
                statistics: 1 <= x_0 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_1 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_2 + x_4 <= 1
                statistics: 1 <= x_3 + x_5 <= 1
                statistics: 0 <= <= 0
                statistics: 1 <= x_6 + 3 x_9 + 2 x_12 <= 1
                statistics: 3 <= x_7 + 3 x_10 + 2 x_13 <= 3
                statistics: 2 <= x_8 + 3 x_11 + 2 x_14 <= 2
                veto: x_0 + x_1 + x_3 + x_4 + x_6 + x_10 + x_14 <= 6
            after vetoing
            Constraints are:
                block []: 1 <= x_0 <= 1
                block [1]: 1 <= x_1 <= 1
                block [1, 2]: 1 <= x_2 + x_3 <= 1
                block [2, 1]: 1 <= x_4 + x_5 <= 1
                block [1, 2, 3]: 1 <= x_6 + x_7 + x_8 <= 1
                block [1, 3, 2]: 1 <= x_9 + x_10 + x_11 <= 1
                block [2, 3, 1]: 1 <= x_12 + x_13 + x_14 <= 1
                statistics: 1 <= x_0 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_1 <= 1
                statistics: 0 <= <= 0
                statistics: 0 <= <= 0
                statistics: 1 <= x_2 + x_4 <= 1
                statistics: 1 <= x_3 + x_5 <= 1
                statistics: 0 <= <= 0
                statistics: 1 <= x_6 + 3 x_9 + 2 x_12 <= 1
                statistics: 3 <= x_7 + 3 x_10 + 2 x_13 <= 3
                statistics: 2 <= x_8 + 3 x_11 + 2 x_14 <= 2
                veto: x_0 + x_1 + x_3 + x_4 + x_6 + x_10 + x_14 <= 6
                veto: x_0 + x_1 + x_2 + x_5 + x_6 + x_10 + x_14 <= 6

            sage: set_verbose(0)

        TESTS:

        An unfeasible problem::

            sage: A = ["a", "b", "c", "d"]; B = [1, 2, 3, 4]
            sage: bij = Bijectionist(A, B)
            sage: bij.set_value_restrictions(("a", [1, 2]), ("b", [1, 2]), ("c", [1, 3]), ("d", [2, 3]))
            sage: list(bij.solutions_iterator())
            []

        Testing interactions between multiple instances using Fedor Petrov\'s example from https://mathoverflow.net/q/424187::

            sage: A = B = ["a"+str(i) for i in range(1, 9)] + ["b"+str(i) for i in range(3, 9)] + ["d"]
            sage: tau = {b: 0 if i < 10 else 1 for i, b in enumerate(B)}.get
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_constant_blocks([["a"+str(i), "b"+str(i)] for i in range(1, 9) if "b"+str(i) in A])
            sage: d = [0]*8+[1]*4
            sage: bij.set_distributions((A[:8] + A[8+2:-1], d), (A[:8] + A[8:-3], d))
            sage: iterator1 = bij.solutions_iterator()
            sage: iterator2 = bij.solutions_iterator()

        Generate a solution in iterator1, iterator2 should generate the same solution and vice versa::

            sage: s1_1 = next(iterator1)
            sage: s2_1 = next(iterator2)
            sage: s1_1 == s2_1
            True
            sage: s2_2 = next(iterator2)
            sage: s1_2 = next(iterator1)
            sage: s1_2 == s2_2
            True

        Re-setting the distribution resets the cache, so a new
        iterator will generate the first solutions again, but the old
        iterator continues::

            sage: bij.set_distributions((A[:8] + A[8+2:-1], d), (A[:8] + A[8:-3], d))
            sage: iterator3 = bij.solutions_iterator()

            sage: s3_1 = next(iterator3)
            sage: s1_1 == s3_1
            True

            sage: s1_3 = next(iterator1)
            sage: len(set([tuple(sorted(s.items())) for s in [s1_1, s1_2, s1_3]]))
            3
        '''

class _BijectionistMILP:
    """
    Wrapper class for the MixedIntegerLinearProgram (MILP).

    This class is used to manage the MILP, add constraints, solve the
    problem and check for uniqueness of solution values.
    """
    milp: Incomplete
    def __init__(self, bijectionist: Bijectionist, solutions=None) -> None:
        '''
        Initialize the mixed integer linear program.

        INPUT:

        - ``bijectionist`` -- an instance of :class:`Bijectionist`

        - ``solutions`` -- (optional) a list of solutions of the
          problem, each provided as a dictionary mapping `(a, z)` to
          a boolean, such that at least one element from each block
          of `P` appears as `a`.

        .. TODO::

            it might be cleaner not to pass the full bijectionist
            instance, but only those attributes we actually use

        TESTS::

            sage: A = B = ["a", "b", "c", "d"]
            sage: bij = Bijectionist(A, B)
            sage: from sage.combinat.bijectionist import _BijectionistMILP
            sage: _BijectionistMILP(bij)
            <sage.combinat.bijectionist._BijectionistMILP object at ...>
        '''
    def show(self, variables: bool = True) -> None:
        '''
        Print the constraints and variables of the MILP together
        with some explanations.

        EXAMPLES::

            sage: A = B = ["a", "b", "c"]
            sage: bij = Bijectionist(A, B, lambda x: A.index(x) % 2, solver=\'GLPK\')
            sage: bij.set_constant_blocks([["a", "b"]])
            sage: next(bij.solutions_iterator())
            {\'a\': 0, \'b\': 0, \'c\': 1}
            sage: bij._bmilp.show()
            Constraints are:
                block a: 1 <= x_0 + x_1 <= 1
                block c: 1 <= x_2 + x_3 <= 1
                statistics: 2 <= 2 x_0 + x_2 <= 2
                statistics: 1 <= 2 x_1 + x_3 <= 1
                veto: x_0 + x_3 <= 1
            Variables are:
                x_0: s(a) = s(b) = 0
                x_1: s(a) = s(b) = 1
                x_2: s(c) = 0
                x_3: s(c) = 1
        '''
    def solutions_iterator(self, on_blocks, additional_constraints) -> Generator[Incomplete]:
        """
        Iterate over all solutions satisfying the additional constraints.

        INPUT:

        - ``additional_constraints`` -- list of constraints for the
          underlying MILP

        - ``on_blocks`` -- whether to return the solution on blocks or
          on all elements

        TESTS::

            sage: A = B = 'abc'
            sage: bij = Bijectionist(A, B, lambda x: B.index(x) % 2, solver='GLPK')
            sage: from sage.combinat.bijectionist import _BijectionistMILP
            sage: bmilp = _BijectionistMILP(bij)
            sage: it = bmilp.solutions_iterator(False, [])
            sage: it2 = bmilp.solutions_iterator(False, [bmilp._x[('c', 1)] == 1])
            sage: next(it)
            {'a': 0, 'b': 1, 'c': 0}
            sage: next(it2)
            {'a': 0, 'b': 0, 'c': 1}
            sage: next(it)
            {'a': 0, 'b': 0, 'c': 1}
            sage: next(it)
            {'a': 1, 'b': 0, 'c': 0}
        """
    def add_alpha_beta_constraints(self) -> None:
        """
        Add constraints enforcing that `(alpha, s)` is equidistributed
        with `(beta, tau)` and `S` is the intertwining bijection.

        We do this by adding

        .. MATH::

            \\sum_{a\\in A, z\\in Z} x_{p(a), z} s^z t^{\\alpha(a)}
            = \\sum_{b\\in B} s^{\\tau(b)} t(\\beta(b))

        as a matrix equation.

        EXAMPLES::

            sage: A = B = [permutation for n in range(3) for permutation in Permutations(n)]
            sage: bij = Bijectionist(A, B, len)
            sage: bij.set_statistics((len, len))
            sage: from sage.combinat.bijectionist import _BijectionistMILP
            sage: bmilp = _BijectionistMILP(bij)                                # indirect doctest
            sage: next(bmilp.solutions_iterator(False, []))
            {[]: 0, [1]: 1, [1, 2]: 2, [2, 1]: 2}
        """
    def add_distribution_constraints(self) -> None:
        """
        Add constraints so the distributions given by
        :meth:`set_distributions` are fulfilled.

        To accomplish this we add

        .. MATH::

            \\sum_{a\\in\\tilde A} x_{p(a), z}t^z = \\sum_{z\\in\\tilde Z} t^z,

        where `p(a)` is the block containing `a`, for each given
        distribution as a vector equation.

        EXAMPLES::

            sage: A = B = Permutations(3)
            sage: tau = Permutation.longest_increasing_subsequence_length
            sage: bij = Bijectionist(A, B, tau)
            sage: bij.set_distributions(([Permutation([1, 2, 3]), Permutation([1, 3, 2])], [1, 3]))
            sage: from sage.combinat.bijectionist import _BijectionistMILP
            sage: bmilp = _BijectionistMILP(bij)                                # indirect doctest
            sage: next(bmilp.solutions_iterator(False, []))
            {[1, 2, 3]: 3,
             [1, 3, 2]: 1,
             [2, 1, 3]: 2,
             [2, 3, 1]: 2,
             [3, 1, 2]: 2,
             [3, 2, 1]: 2}
        """
    def add_intertwining_relation_constraints(self) -> None:
        """
        Add constraints corresponding to the given intertwining
        relations.

        INPUT:

        - origins, a list of triples `((\\pi/\\rho, p,
          (p_1,\\dots,p_k))`, where `p` is the block of
          `\\rho(s(a_1),\\dots, s(a_k))`, for any `a_i\\in p_i`.

        This adds the constraints imposed by
        :meth:`set_intertwining_relations`,

        .. MATH::

            s(\\pi(a_1,\\dots, a_k)) = \\rho(s(a_1),\\dots, s(a_k))

        for each pair `(\\pi, \\rho)`.  The relation implies
        immediately that `s(\\pi(a_1,\\dots, a_k))` only depends on the
        blocks of `a_1,\\dots, a_k`.

        The MILP formulation is as follows.  Let `a_1,\\dots,a_k \\in
        A` and let `a = \\pi(a_1,\\dots,a_k)`.  Let `z_1,\\dots,z_k \\in
        Z` and let `z = \\rho(z_1,\\dots,z_k)`.  Suppose that `a_i\\in
        p_i` for all `i` and that `a\\in p`.

        We then want to model the implication

        .. MATH::

           x_{p_1, z_1} = 1,\\dots, x_{p_k, z_k} = 1 \\Rightarrow x_{p, z} = 1.

        We achieve this by requiring

        .. MATH::

            x_{p, z}\\geq 1 - k + \\sum_{i=1}^k x_{p_i, z_i}.

        Note that `z` must be a possible value of `p` and each `z_i`
        must be a possible value of `p_i`.

        EXAMPLES::

            sage: A = B = 'abcd'
            sage: bij = Bijectionist(A, B, lambda x: B.index(x) % 2)
            sage: def pi(p1, p2): return 'abcdefgh'[A.index(p1) + A.index(p2)]
            sage: def rho(s1, s2): return (s1 + s2) % 2
            sage: bij.set_intertwining_relations((2, pi, rho))
            sage: from sage.combinat.bijectionist import _BijectionistMILP
            sage: bmilp = _BijectionistMILP(bij)                                # indirect doctest
            sage: next(bmilp.solutions_iterator(False, []))
            {'a': 0, 'b': 1, 'c': 0, 'd': 1}
        """
    def add_quadratic_relation_constraints(self) -> None:
        """
        Add constraints enforcing that `s\\circ\\phi\\circ s =
        \\psi`.

        We do this by adding

        .. MATH::

            x_{p(a), z} = x_{p(\\psi(z)), \\phi(a)}

        for `a\\in A` and `z\\in Z`, where `\\phi:A\\to Z` and `\\psi:Z\\to
        A`.  Note that, in particular, `\\phi` must be constant on
        blocks.

        EXAMPLES::

            sage: A = B = DyckWords(3)
            sage: bij = Bijectionist(A, B)
            sage: bij.set_statistics((lambda D: D.number_of_touch_points(), lambda D: D.number_of_initial_rises()))
            sage: ascii_art(sorted(bij.minimal_subdistributions_iterator()))
            [ (             [   /\\   ] )
            [ (             [  /  \\  ] )  ( [    /\\    /\\    ]  [  /\\      /\\/\\  ] )
            [ ( [ /\\/\\/\\ ], [ /    \\ ] ), ( [ /\\/  \\, /  \\/\\ ], [ /  \\/\\, /    \\ ] ),
            <BLANKLINE>
             ( [           /\\   ]                     ) ]
             ( [  /\\/\\    /  \\  ]  [            /\\  ] ) ]
             ( [ /    \\, /    \\ ], [ /\\/\\/\\, /\\/  \\ ] ) ]
            sage: bij.set_quadratic_relation((lambda D: D, lambda D: D))   # indirect doctest
            sage: ascii_art(sorted(bij.minimal_subdistributions_iterator()))
            [ (             [   /\\   ] )
            [ (             [  /  \\  ] )  ( [    /\\  ]  [  /\\/\\  ] )
            [ ( [ /\\/\\/\\ ], [ /    \\ ] ), ( [ /\\/  \\ ], [ /    \\ ] ),
            <BLANKLINE>
            <BLANKLINE>
             ( [  /\\    ]  [  /\\    ] )  ( [  /\\/\\  ]  [    /\\  ] )
             ( [ /  \\/\\ ], [ /  \\/\\ ] ), ( [ /    \\ ], [ /\\/  \\ ] ),
            <BLANKLINE>
             ( [   /\\   ]             ) ]
             ( [  /  \\  ]             ) ]
             ( [ /    \\ ], [ /\\/\\/\\ ] ) ]
        """
    def add_homomesic_constraints(self):
        """
        Add constraints enforcing that `s` has constant average
        on the blocks of `Q`.

        We do this by adding

        .. MATH::

            \\frac{1}{|q|}\\sum_{a\\in q} \\sum_z z x_{p(a), z} =
            \\frac{1}{|q_0|}\\sum_{a\\in q_0} \\sum_z z x_{p(a), z},

        for `q\\in Q`, where `q_0` is some fixed block of `Q`.

        EXAMPLES::

            sage: A = B = [1,2,3]
            sage: bij = Bijectionist(A, B, lambda b: b % 3)
            sage: bij.set_homomesic([[1,2], [3]])                               # indirect doctest
            sage: list(bij.solutions_iterator())
            [{1: 2, 2: 0, 3: 1}, {1: 0, 2: 2, 3: 1}]
        """
