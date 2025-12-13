import sage.combinat.integer_lists.base
import sage.combinat.integer_lists.lists
from sage.combinat.integer_lists.lists import IntegerLists as IntegerLists
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass, typecall as typecall
from typing import Any, overload

DECREASE: int
Infinity: float
LOOKAHEAD: int
ME: int
POP: int
PUSH: int
STOP: int

class IntegerListsBackend_invlex(sage.combinat.integer_lists.base.IntegerListsBackend):
    """IntegerListsBackend_invlex(check=True, *args, **kwds)

    File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 797)

    Cython back-end of a set of lists of integers with specified
    constraints enumerated in inverse lexicographic order."""
    check: check
    def __init__(self, check=..., *args, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 802)

                Initialize ``self``.

                TESTS::

                    sage: C = IntegerListsLex(2, length=3)
                    sage: C == loads(dumps(C))
                    True
                    sage: C.cardinality().parent() is ZZ
                    True
                    sage: TestSuite(C).run()
                    sage: IntegerListsLex(min_part=-1)
                    Traceback (most recent call last):
                    ...
                    NotImplementedError: strictly negative min_part
        """

class IntegerListsLex(sage.combinat.integer_lists.lists.IntegerLists):
    '''File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 40)

        Lists of nonnegative integers with constraints, in inverse
        lexicographic order.

        An *integer list* is a list `l` of nonnegative integers, its *parts*. The
        slope (at position `i`) is the difference ``l[i+1]-l[i]`` between two
        consecutive parts.

        This class allows to construct the set `S` of all integer lists
        `l` satisfying specified bounds on the sum, the length, the slope,
        and the individual parts, enumerated in *inverse* lexicographic
        order, that is from largest to smallest in lexicographic
        order. Note that, to admit such an enumeration, `S` is almost
        necessarily finite (see :ref:`IntegerListsLex_finiteness`).

        The main purpose is to provide a generic iteration engine for all the
        enumerated sets like :class:`Partitions`, :class:`Compositions`,
        :class:`IntegerVectors`. It can also be used to generate many other
        combinatorial objects like Dyck paths, Motzkin paths, etc. Mathematically
        speaking, this is a special case of set of integral points of a polytope (or
        union thereof, when the length is not fixed).

        INPUT:

        - ``min_sum`` -- nonnegative integer (default: 0);
          a lower bound on ``sum(l)``

        - ``max_sum`` -- nonnegative integer or `\\infty` (default: `\\infty`);
          an upper bound on ``sum(l)``

        - ``n`` -- nonnegative integer (optional); if specified, this
          overrides ``min_sum`` and ``max_sum``

        - ``min_length`` -- nonnegative integer (default: `0`); a lower
          bound on ``len(l)``

        - ``max_length`` -- nonnegative integer or `\\infty` (default:
          `\\infty`); an upper bound on ``len(l)``

        - ``length`` -- integer (optional); overrides ``min_length``
          and ``max_length`` if specified

        - ``min_part`` -- nonnegative integer; a lower bounds on all
          parts: ``min_part <= l[i]`` for ``0 <= i < len(l)``

        - ``floor`` -- list of nonnegative integers or a function; lower
          bounds on the individual parts `l[i]`

          If ``floor`` is a list of integers, then ``floor<=l[i]`` for ``0
          <= i < min(len(l), len(floor)``. Similarly, if ``floor`` is a
          function, then ``floor(i) <= l[i]`` for ``0 <= i < len(l)``.

        - ``max_part`` -- nonnegative integer or `\\infty`; an upper
          bound on all parts: ``l[i] <= max_part`` for ``0 <= i < len(l)``

        - ``ceiling`` -- upper bounds on the individual parts ``l[i]``;
          this takes the same type of input as ``floor``, except that
          `\\infty` is allowed in addition to integers, and the default
          value is `\\infty`.

        - ``min_slope`` -- integer or `-\\infty` (default: `-\\infty`);
          a lower bound on the slope between consecutive parts:
          ``min_slope <= l[i+1]-l[i]`` for ``0 <= i < len(l)-1``

        - ``max_slope`` -- integer or `+\\infty` (defaults: `+\\infty`);
          an upper bound on the slope between consecutive parts:
          ``l[i+1]-l[i] <= max_slope`` for ``0 <= i < len(l)-1``

        - ``category`` -- a category (default: :class:`FiniteEnumeratedSets`)

        - ``check`` -- boolean (default: ``True``); whether to display the
          warnings raised when functions are given as input to ``floor``
          or ``ceiling`` and the errors raised when there is no proper
          enumeration.

        - ``name`` -- string or ``None`` (default: ``None``); if set,
          this will be passed down to :meth:`Parent.rename` to specify the
          name of ``self``. It is recommended to use rename method directly
          because this feature may become deprecated.

        - ``element_constructor`` -- a function (or callable) that creates
          elements of ``self`` from a list. See also :class:`Parent`

        - ``element_class`` -- a class for the elements of ``self``
          (default: `ClonableArray`). This merely sets the attribute
          ``self.Element``. See the examples for details.

        .. NOTE::

            When several lists satisfying the constraints differ only by
            trailing zeroes, only the shortest one is enumerated (and
            therefore counted). The others are still considered valid.
            See the examples below.

            This feature is questionable. It is recommended not to rely on
            it, as it may eventually be discontinued.

        EXAMPLES:

        We create the enumerated set of all lists of nonnegative integers
        of length `3` and sum `2`::

            sage: C = IntegerListsLex(2, length=3)
            sage: C
            Integer lists of sum 2 satisfying certain constraints
            sage: C.cardinality()
            6
            sage: [p for p in C]
            [[2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]

            sage: [2, 0, 0] in C
            True
            sage: [2, 0, 1] in C
            False
            sage: "a" in C
            False
            sage: ["a"] in C
            False
            sage: C.first()
            [2, 0, 0]

        One can specify lower and upper bounds on each part::

            sage: list(IntegerListsLex(5, length=3, floor=[1,2,0], ceiling=[3,2,3]))
            [[3, 2, 0], [2, 2, 1], [1, 2, 2]]

        When the length is fixed as above, one can also use
        :class:`IntegerVectors`::

            sage: IntegerVectors(2,3).list()
            [[2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]

        Using the slope condition, one can generate integer partitions
        (but see :class:`Partitions`)::

            sage: list(IntegerListsLex(4, max_slope=0))
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

        The following is the list of all partitions of `7` with parts at least `2`::

            sage: list(IntegerListsLex(7, max_slope=0, min_part=2))
            [[7], [5, 2], [4, 3], [3, 2, 2]]


        .. RUBRIC:: floor and ceiling conditions

        Next we list all partitions of `5` of length at most `3` which are
        bounded below by ``[2,1,1]``::

            sage: list(IntegerListsLex(5, max_slope=0, max_length=3, floor=[2,1,1]))
            [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1]]

        Note that ``[5]`` is considered valid, because the floor
        constraints only apply to existing positions in the list. To
        obtain instead the partitions containing ``[2,1,1]``, one needs to
        use ``min_length`` or ``length``::

            sage: list(IntegerListsLex(5, max_slope=0, length=3, floor=[2,1,1]))
            [[3, 1, 1], [2, 2, 1]]

        Here is the list of all partitions of `5` which are contained in
        ``[3,2,2]``::

            sage: list(IntegerListsLex(5, max_slope=0, max_length=3, ceiling=[3,2,2]))
            [[3, 2], [3, 1, 1], [2, 2, 1]]

        This is the list of all compositions of `4` (but see :class:`Compositions`)::

            sage: list(IntegerListsLex(4, min_part=1))
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 3], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]

        This is the list of all integer vectors of sum `4` and length `3`::

            sage: list(IntegerListsLex(4, length=3))
            [[4, 0, 0], [3, 1, 0], [3, 0, 1], [2, 2, 0], [2, 1, 1],
             [2, 0, 2], [1, 3, 0], [1, 2, 1], [1, 1, 2], [1, 0, 3],
             [0, 4, 0], [0, 3, 1], [0, 2, 2], [0, 1, 3], [0, 0, 4]]

        For whatever it is worth, the ``floor`` and ``min_part``
        constraints can be combined::

            sage: L = IntegerListsLex(5, floor=[2,0,2], min_part=1)
            sage: L.list()
            [[5], [4, 1], [3, 2], [2, 3], [2, 1, 2]]

        This is achieved by updating the floor upon constructing ``L``::

            sage: [L.floor(i) for i in range(5)]
            [2, 1, 2, 1, 1]

        Similarly, the ``ceiling`` and ``max_part`` constraints can be
        combined::

            sage: L = IntegerListsLex(4, ceiling=[2,3,1], max_part=2, length=3)
            sage: L.list()
            [[2, 2, 0], [2, 1, 1], [1, 2, 1]]
            sage: [L.ceiling(i) for i in range(5)]
            [2, 2, 1, 2, 2]


        This can be used to generate Motzkin words (see
        :wikipedia:`Motzkin_number`)::

            sage: def motzkin_words(n):
            ....:     return IntegerListsLex(length=n+1, min_slope=-1, max_slope=1,
            ....:                ceiling=[0]+[+oo for i in range(n-1)]+[0])
            sage: motzkin_words(4).list()
            [[0, 1, 2, 1, 0],
             [0, 1, 1, 1, 0],
             [0, 1, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0]]
            sage: [motzkin_words(n).cardinality() for n in range(8)]
            [1, 1, 2, 4, 9, 21, 51, 127]
            sage: oeis(_)                  # optional -- internet
            0: A001006: Motzkin numbers: number of ways of drawing any number
            of nonintersecting chords joining n (labeled) points on a circle.
            1: ...
            2: ...

        or Dyck words (see also :class:`DyckWords`), through the bijection
        with paths from `(0,0)` to `(n,n)` with left and up steps that remain
        below the diagonal::

            sage: def dyck_words(n):
            ....:     return IntegerListsLex(length=n, ceiling=list(range(n+1)), min_slope=0)
            sage: [dyck_words(n).cardinality() for n in range(8)]
            [1, 1, 2, 5, 14, 42, 132, 429]
            sage: dyck_words(3).list()
            [[0, 1, 2], [0, 1, 1], [0, 0, 2], [0, 0, 1], [0, 0, 0]]


        .. _IntegerListsLex_finiteness:

        .. RUBRIC:: On finiteness and inverse lexicographic enumeration

        The set of all lists of integers cannot be enumerated in inverse
        lexicographic order, since there is no largest list (take `[n]`
        for `n` as large as desired)::

            sage: IntegerListsLex().first()
            Traceback (most recent call last):
            ...
            ValueError: could not prove that the specified constraints yield a finite set

        Here is a variant which could be enumerated in lexicographic order
        but not in inverse lexicographic order::

            sage: L = IntegerListsLex(length=2, ceiling=[Infinity, 0], floor=[0,1])
            sage: for l in L: print(l)
            Traceback (most recent call last):
            ...
            ValueError: infinite upper bound for values of m

        Even when the sum is specified, it is not necessarily possible to
        enumerate *all* elements in inverse lexicographic order. In the
        following example, the list ``[1, 1, 1]`` will never appear in the
        enumeration::

            sage: IntegerListsLex(3).first()
            Traceback (most recent call last):
            ...
            ValueError: could not prove that the specified constraints yield a finite set

        If one wants to proceed anyway, one can sign a waiver by setting
        ``check=False`` (again, be warned that some valid lists may never appear)::

            sage: L = IntegerListsLex(3, check=False)
            sage: it = iter(L)
            sage: [next(it) for i in range(6)]
            [[3], [2, 1], [2, 0, 1], [2, 0, 0, 1], [2, 0, 0, 0, 1], [2, 0, 0, 0, 0, 1]]

        In fact, being inverse lexicographically enumerable is almost
        equivalent to being finite. The only infinity that can occur would
        be from a tail of numbers `0,1` as in the previous example, where
        the `1` moves further and further to the right. If there is any
        list that is inverse lexicographically smaller than such a
        configuration, the iterator would not reach it and hence would not
        be considered iterable. Given that the infinite cases are very
        specific, at this point only the finite cases are supported
        (without signing the waiver).

        The finiteness detection is not complete yet, so some finite cases
        may not be supported either, at least not without disabling the
        checks. Practical examples of such are welcome.

        .. RUBRIC:: On trailing zeroes, and their caveats

        As mentioned above, when several lists satisfying the constraints
        differ only by trailing zeroes, only the shortest one is listed::

            sage: L = IntegerListsLex(max_length=4, max_part=1)
            sage: L.list()
            [[1, 1, 1, 1],
             [1, 1, 1],
             [1, 1, 0, 1],
             [1, 1],
             [1, 0, 1, 1],
             [1, 0, 1],
             [1, 0, 0, 1],
             [1],
             [0, 1, 1, 1],
             [0, 1, 1],
             [0, 1, 0, 1],
             [0, 1],
             [0, 0, 1, 1],
             [0, 0, 1],
             [0, 0, 0, 1],
             []]

        and counted::

            sage: L.cardinality()
            16

        Still, the others are considered as elements of `L`::

            sage: L = IntegerListsLex(4,min_length=3,max_length=4)
            sage: L.list()
            [..., [2, 2, 0], ...]

            sage: [2, 2, 0] in L       # in L.list()
            True
            sage: [2, 2, 0, 0] in L    # not in L.list() !
            True
            sage: [2, 2, 0, 0, 0] in L
            False

        .. RUBRIC:: Specifying functions as input for the floor or ceiling

        We construct all lists of sum `4` and length `4` such that ``l[i] <= i``::

            sage: list(IntegerListsLex(4, length=4, ceiling=lambda i: i, check=False))
            [[0, 1, 2, 1], [0, 1, 1, 2], [0, 1, 0, 3], [0, 0, 2, 2], [0, 0, 1, 3]]

        .. WARNING::

            When passing a function as ``floor`` or ``ceiling``, it may
            become undecidable to detect improper inverse lexicographic
            enumeration. For example, the following example has a finite
            enumeration::

                sage: L = IntegerListsLex(3, floor=lambda i: 1 if i>=2 else 0, check=False)
                sage: L.list()
                [[3],
                 [2, 1],
                 [2, 0, 1],
                 [1, 2],
                 [1, 1, 1],
                 [1, 0, 2],
                 [1, 0, 1, 1],
                 [0, 3],
                 [0, 2, 1],
                 [0, 1, 2],
                 [0, 1, 1, 1],
                 [0, 0, 3],
                 [0, 0, 2, 1],
                 [0, 0, 1, 2],
                 [0, 0, 1, 1, 1]]

            but one cannot decide whether the following has an improper
            inverse lexicographic enumeration without computing the floor
            all the way to ``Infinity``::

                sage: L = IntegerListsLex(3, floor=lambda i: 0, check=False)
                sage: it = iter(L)
                sage: [next(it) for i in range(6)]
                [[3], [2, 1], [2, 0, 1], [2, 0, 0, 1], [2, 0, 0, 0, 1], [2, 0, 0, 0, 0, 1]]

            Hence a warning is raised when a function is specified as
            input, unless the waiver is signed by setting ``check=False``::

                sage: L = IntegerListsLex(3, floor=lambda i: 1 if i>=2 else 0)
                doctest:...
                A function has been given as input of the floor=[...] or ceiling=[...]
                arguments of IntegerListsLex. Please see the documentation for the caveats.
                If you know what you are doing, you can set check=False to skip this warning.

            Similarly, the algorithm may need to search forever for a
            solution when the ceiling is ultimately zero::

                sage: L = IntegerListsLex(2,ceiling=lambda i:0, check=False)
                sage: L.first()           # not tested: will hang forever
                sage: L = IntegerListsLex(2,ceiling=lambda i:0 if i<20 else 1, check=False)
                sage: it = iter(L)
                sage: next(it)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
                sage: next(it)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
                sage: next(it)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]


        .. RUBRIC:: Tip: using disjoint union enumerated sets for additional flexibility

        Sometimes, specifying a range for the sum or the length may be too
        restrictive. One would want instead to specify a list, or
        iterable `L`, of acceptable values. This is easy to achieve using
        a :class:`disjoint union of enumerated sets <DisjointUnionEnumeratedSets>`.
        Here we want to accept the values `n=0,2,3`::

            sage: C = DisjointUnionEnumeratedSets(Family([0,2,3],
            ....:         lambda n: IntegerListsLex(n, length=2)))
            sage: C
            Disjoint union of Finite family
            {0: Integer lists of sum 0 satisfying certain constraints,
             2: Integer lists of sum 2 satisfying certain constraints,
             3: Integer lists of sum 3 satisfying certain constraints}
            sage: C.list()
            [[0, 0],
             [2, 0], [1, 1], [0, 2],
             [3, 0], [2, 1], [1, 2], [0, 3]]

        The price to pay is that the enumeration order is now *graded
        lexicographic* instead of lexicographic: first choose the value
        according to the order specified by `L`, and use lexicographic
        order within each value. Here is we reverse `L`::

            sage: DisjointUnionEnumeratedSets(Family([3,2,0],
            ....:     lambda n: IntegerListsLex(n, length=2))).list()
            [[3, 0], [2, 1], [1, 2], [0, 3],
             [2, 0], [1, 1], [0, 2],
             [0, 0]]

        Note that if a given value appears several times, the
        corresponding elements will be enumerated several times, which
        may, or not, be what one wants::

            sage: DisjointUnionEnumeratedSets(Family([2,2],
            ....:     lambda n: IntegerListsLex(n, length=2))).list()
            [[2, 0], [1, 1], [0, 2], [2, 0], [1, 1], [0, 2]]

        Here is a variant where we specify acceptable values for the
        length::

            sage: DisjointUnionEnumeratedSets(Family([0,1,3],
            ....:     lambda l: IntegerListsLex(2, length=l))).list()
            [[2],
             [2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]


        This technique can also be useful to obtain a proper enumeration
        on infinite sets by using a graded lexicographic enumeration::

            sage: C = DisjointUnionEnumeratedSets(Family(NN,
            ....:         lambda n: IntegerListsLex(n, length=2)))
            sage: C
            Disjoint union of Lazy family (<lambda>(i))_{i in Non negative integer semiring}
            sage: it = iter(C)
            sage: [next(it) for i in range(10)]
            [[0, 0],
             [1, 0], [0, 1],
             [2, 0], [1, 1], [0, 2],
             [3, 0], [2, 1], [1, 2], [0, 3]]


        .. RUBRIC:: Specifying how to construct elements

        This is the list of all monomials of degree `4` which divide the
        monomial `x^3y^1z^2` (a monomial being identified with its
        exponent vector)::

            sage: R.<x,y,z> = QQ[]
            sage: m = [3,1,2]
            sage: def term(exponents):
            ....:     return x^exponents[0] * y^exponents[1] * z^exponents[2]
            sage: list( IntegerListsLex(4, length=len(m), ceiling=m, element_constructor=term) )
            [x^3*y, x^3*z, x^2*y*z, x^2*z^2, x*y*z^2]

        Note the use of the ``element_constructor`` option to specify how
        to construct elements from a plain list.

        A variant is to specify a class for the elements. With the default
        element constructor, this class should take as input the parent
        ``self`` and a list.

        .. WARNING::

            The protocol for specifying the element class and constructor
            is subject to changes.

        ALGORITHM:

        The iteration algorithm uses a depth first search through the
        prefix tree of the list of integers (see also
        :ref:`section-generic-integerlistlex`). While doing so, it does
        some lookahead heuristics to attempt to cut dead branches.

        In most practical use cases, most dead branches are cut. Then,
        roughly speaking, the time needed to iterate through all the
        elements of `S` is proportional to the number of elements, where
        the proportion factor is controlled by the length `l` of the
        longest element of `S`. In addition, the memory usage is also
        controlled by `l`, which is to say negligible in practice.

        Still, there remains much room for efficiency improvements; see
        :issue:`18055`, :issue:`18056`.

        .. NOTE::

            The generation algorithm could in principle be extended to
            deal with non-constant slope constraints and with negative
            parts.

        TESTS:

        This example from the combinatorics tutorial used to fail before
        :issue:`17979` because the floor conditions did not satisfy the
        slope conditions::

            sage: I = IntegerListsLex(16, min_length=2, max_slope=-1, floor=[5,3,3])
            sage: I.list()
            [[13, 3], [12, 4], [11, 5], [10, 6], [9, 7], [9, 4, 3], [8, 5, 3], [8, 4, 3, 1],
             [7, 6, 3], [7, 5, 4], [7, 5, 3, 1], [7, 4, 3, 2], [6, 5, 4, 1], [6, 5, 3, 2],
             [6, 4, 3, 2, 1]]

        ::

            sage: Partitions(2, max_slope=-1, length=2).list()                              # needs sage.combinat
            []
            sage: list(IntegerListsLex(0, floor=ConstantFunction(1), min_slope=0))
            [[]]
            sage: list(IntegerListsLex(0, floor=ConstantFunction(1), min_slope=0, max_slope=0))
            [[]]
            sage: list(IntegerListsLex(0, max_length=0, floor=ConstantFunction(1), min_slope=0, max_slope=0))
            [[]]
            sage: list(IntegerListsLex(0, max_length=0, floor=ConstantFunction(0), min_slope=0, max_slope=0))
            [[]]
            sage: list(IntegerListsLex(0, min_part=1, min_slope=0))
            [[]]
            sage: list(IntegerListsLex(1, min_part=1, min_slope=0))
            [[1]]
            sage: list(IntegerListsLex(0, min_length=1, min_part=1, min_slope=0))
            []
            sage: list(IntegerListsLex(0, min_length=1, min_slope=0))
            [[0]]
            sage: list(IntegerListsLex(3, max_length=2))
            [[3], [2, 1], [1, 2], [0, 3]]
            sage: partitions = {"min_part": 1, "max_slope": 0}
            sage: partitions_min_2 = {"floor": ConstantFunction(2), "max_slope": 0}
            sage: compositions = {"min_part": 1}
            sage: integer_vectors = lambda l: {"length": l}
            sage: lower_monomials = lambda c: {"length": c, "floor": lambda i: c[i]}
            sage: upper_monomials = lambda c: {"length": c, "ceiling": lambda i: c[i]}
            sage: constraints = { "min_part":1, "min_slope": -1, "max_slope": 0}
            sage: list(IntegerListsLex(6, **partitions))
            [[6],
             [5, 1],
             [4, 2],
             [4, 1, 1],
             [3, 3],
             [3, 2, 1],
             [3, 1, 1, 1],
             [2, 2, 2],
             [2, 2, 1, 1],
             [2, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1]]
            sage: list(IntegerListsLex(6, **constraints))
            [[6],
             [3, 3],
             [3, 2, 1],
             [2, 2, 2],
             [2, 2, 1, 1],
             [2, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1]]
            sage: list(IntegerListsLex(1, **partitions_min_2))
            []
            sage: list(IntegerListsLex(2, **partitions_min_2))
            [[2]]
            sage: list(IntegerListsLex(3, **partitions_min_2))
            [[3]]
            sage: list(IntegerListsLex(4, **partitions_min_2))
            [[4], [2, 2]]
            sage: list(IntegerListsLex(5, **partitions_min_2))
            [[5], [3, 2]]
            sage: list(IntegerListsLex(6, **partitions_min_2))
            [[6], [4, 2], [3, 3], [2, 2, 2]]
            sage: list(IntegerListsLex(7, **partitions_min_2))
            [[7], [5, 2], [4, 3], [3, 2, 2]]
            sage: list(IntegerListsLex(9, **partitions_min_2))
            [[9], [7, 2], [6, 3], [5, 4], [5, 2, 2], [4, 3, 2], [3, 3, 3], [3, 2, 2, 2]]
            sage: list(IntegerListsLex(10, **partitions_min_2))
            [[10],
             [8, 2],
             [7, 3],
             [6, 4],
             [6, 2, 2],
             [5, 5],
             [5, 3, 2],
             [4, 4, 2],
             [4, 3, 3],
             [4, 2, 2, 2],
             [3, 3, 2, 2],
             [2, 2, 2, 2, 2]]
            sage: list(IntegerListsLex(4, **compositions))
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 3], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
            sage: list(IntegerListsLex(6, min_length=1, floor=[7]))
            []
            sage: L = IntegerListsLex(10**100,length=1)
            sage: L.list()
            [[10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000]]

        Noted on :issue:`17898`::

            sage: list(IntegerListsLex(4, min_part=1, length=3, min_slope=1))
            []
            sage: IntegerListsLex(6, ceiling=[4,2], floor=[3,3]).list()
            []
            sage: IntegerListsLex(6, min_part=1, max_part=3, max_slope=-4).list()
            []

        Noted in :issue:`17548`, which are now fixed::

            sage: IntegerListsLex(10, min_part=2, max_slope=-1).list()
            [[10], [8, 2], [7, 3], [6, 4], [5, 3, 2]]
            sage: IntegerListsLex(5, min_slope=1, floor=[2,1,1], max_part=2).list()
            []
            sage: IntegerListsLex(4, min_slope=0, max_slope=0).list()
            [[4], [2, 2], [1, 1, 1, 1]]
            sage: IntegerListsLex(6, min_slope=-1, max_slope=-1).list()
            [[6], [3, 2, 1]]
            sage: IntegerListsLex(6, min_length=3, max_length=2, min_part=1).list()
            []
            sage: I = IntegerListsLex(3, max_length=2, min_part=1)
            sage: I.list()
            [[3], [2, 1], [1, 2]]
            sage: [1,1,1] in I
            False
            sage: I = IntegerListsLex(10, ceiling=[4], max_length=1, min_part=1)
            sage: I.list()
            []
            sage: [4,6] in I
            False
            sage: I = IntegerListsLex(4, min_slope=1, min_part=1, max_part=2)
            sage: I.list()
            []
            sage: I = IntegerListsLex(7, min_slope=1, min_part=1, max_part=4)
            sage: I.list()
            [[3, 4], [1, 2, 4]]
            sage: I = IntegerListsLex(4, floor=[2,1], ceiling=[2,2], max_length=2, min_slope=0)
            sage: I.list()
            [[2, 2]]
            sage: I = IntegerListsLex(10, min_part=1, max_slope=-1)
            sage: I.list()
            [[10], [9, 1], [8, 2], [7, 3], [7, 2, 1], [6, 4], [6, 3, 1], [5, 4, 1],
             [5, 3, 2], [4, 3, 2, 1]]


        .. RUBRIC:: TESTS from comments on :issue:`17979`

        Comment 191::

            sage: list(IntegerListsLex(1, min_length=2, min_slope=0, max_slope=0))
            []

        Comment 240::

            sage: L = IntegerListsLex(min_length=2, max_part=0)
            sage: L.list()
            [[0, 0]]

        .. RUBRIC:: Tests on the element constructor feature and mutability

        Internally, the iterator works on a single list that is mutated
        along the way. Therefore, you need to make sure that the
        ``element_constructor`` actually **copies** its input. This example
        shows what can go wrong::

            sage: P = IntegerListsLex(n=3, max_slope=0, min_part=1, element_constructor=lambda x: x)
            sage: list(P)
            [[], [], []]

        However, specifying ``list()`` as constructor solves this problem::

            sage: P = IntegerListsLex(n=3, max_slope=0, min_part=1, element_constructor=list)
            sage: list(P)
            [[3], [2, 1], [1, 1, 1]]

        Same, step by step::

            sage: it = iter(P)
            sage: a = next(it); a
            [3]
            sage: b = next(it); b
            [2, 1]
            sage: a
            [3]
            sage: a is b
            False

        Tests from `MuPAD-Combinat <http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/COMBINAT/TEST/MachineIntegerListsLex.tst>`_::

            sage: IntegerListsLex(7, min_length=2, max_length=6, floor=[0,0,2,0,0,1], ceiling=[3,2,3,2,1,2]).cardinality()
            83
            sage: IntegerListsLex(7, min_length=2, max_length=6, floor=[0,0,2,0,1,1], ceiling=[3,2,3,2,1,2]).cardinality()
            53
            sage: IntegerListsLex(5, min_length=2, max_length=6, floor=[0,0,2,0,0,0], ceiling=[2,2,2,2,2,2]).cardinality()
            30
            sage: IntegerListsLex(5, min_length=2, max_length=6, floor=[0,0,1,1,0,0], ceiling=[2,2,2,2,2,2]).cardinality()
            43

            sage: IntegerListsLex(0, min_length=0, max_length=7, floor=[1,1,0,0,1,0], ceiling=[4,3,2,3,2,2,1]).first()
            []

            sage: IntegerListsLex(0, min_length=1, max_length=7, floor=[0,1,0,0,1,0], ceiling=[4,3,2,3,2,2,1]).first()
            [0]
            sage: IntegerListsLex(0, min_length=1, max_length=7, floor=[1,1,0,0,1,0], ceiling=[4,3,2,3,2,2,1]).cardinality()
            0

            sage: IntegerListsLex(2, min_length=0, max_length=7, floor=[1,1,0,0,0,0], ceiling=[4,3,2,3,2,2,1]).first()  # Was [1,1], due to slightly different specs
            [2]
            sage: IntegerListsLex(1, min_length=1, max_length=7, floor=[1,1,0,0,0,0], ceiling=[4,3,2,3,2,2,1]).first()
            [1]
            sage: IntegerListsLex(1, min_length=2, max_length=7, floor=[1,1,0,0,0,0], ceiling=[4,3,2,3,2,2,1]).cardinality()
            0
            sage: IntegerListsLex(2, min_length=5, max_length=7, floor=[1,1,0,0,0,0], ceiling=[4,3,2,3,2,2,1]).first()
            [1, 1, 0, 0, 0]
            sage: IntegerListsLex(2, min_length=5, max_length=7, floor=[1,1,0,0,0,1], ceiling=[4,3,2,3,2,2,1]).first()
            [1, 1, 0, 0, 0]
            sage: IntegerListsLex(2, min_length=5, max_length=7, floor=[1,1,0,0,1,0], ceiling=[4,3,2,3,2,2,1]).cardinality()
            0

            sage: IntegerListsLex(4, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).cardinality()
            0
            sage: IntegerListsLex(5, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).first()
            [2, 1, 2]
            sage: IntegerListsLex(6, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).first()
            [3, 1, 2]
            sage: IntegerListsLex(12, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).first()
            [3, 1, 2, 3, 2, 1]
            sage: IntegerListsLex(13, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).first()
            [3, 1, 2, 3, 2, 2]
            sage: IntegerListsLex(14, min_length=3, max_length=6, floor=[2, 1, 2, 1, 1, 1], ceiling=[3, 1, 2, 3, 2, 2]).cardinality()
            0

        This used to hang (see comment 389 and fix in :meth:`Envelope.__init__`)::

            sage: IntegerListsLex(7, max_part=0, ceiling=lambda i:i, check=False).list()
            []
    '''

    class backend_class(sage.combinat.integer_lists.base.IntegerListsBackend):
        """IntegerListsBackend_invlex(check=True, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 797)

        Cython back-end of a set of lists of integers with specified
        constraints enumerated in inverse lexicographic order."""
        check: check
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 802)

                    Initialize ``self``.

                    TESTS::

                        sage: C = IntegerListsLex(2, length=3)
                        sage: C == loads(dumps(C))
                        True
                        sage: C.cardinality().parent() is ZZ
                        True
                        sage: TestSuite(C).run()
                        sage: IntegerListsLex(min_part=-1)
                        Traceback (most recent call last):
                        ...
                        NotImplementedError: strictly negative min_part
        """
    @staticmethod
    def __classcall_private__(cls, n=..., **kwargs) -> Any:
        """IntegerListsLex.__classcall_private__(cls, n=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 787)

        Specifying a list or iterable as argument was deprecated in
        :issue:`17979`. Please use ``DisjointUnionEnumeratedSets`` or
        the ``min_sum`` and ``max_sum`` arguments instead."""

class IntegerListsLexIter:
    """File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 1080)

        Iterator class for IntegerListsLex.

        Let ``T`` be the prefix tree of all lists of nonnegative
        integers that satisfy all constraints except possibly for
        ``min_length`` and ``min_sum``; let the children of a list
        be sorted decreasingly according to their last part.

        The iterator is based on a depth-first search exploration of a
        subtree of this tree, trying to cut branches that do not
        contain a valid list. Each call of ``next`` iterates through
        the nodes of this tree until it finds a valid list to return.

        Here are the attributes describing the current state of the
        iterator,  and their invariants:

        - ``backend`` -- the :class:`IntegerListsBackend` object this is
          iterating on;

        - ``_current_list`` -- the list corresponding to the current
          node of the tree;

        - ``_j`` -- the index of the last element of ``_current_list``:
          ``self._j == len(self._current_list) - 1``;

        - ``_current_sum`` -- the sum of the parts of ``_current_list``;

        - ``_search_ranges`` -- list of same length as
          ``_current_list``: the range for each part

        Furthermore, we assume that there is no obvious contradiction
        in the constraints:

        - ``self.backend.min_length <= self.backend.max_length``;
        - ``self.backend.min_slope <= self.backend.max_slope``
          unless ``self.backend.min_length <= 1``.

        Along this iteration, ``next`` switches between the following
        states:

        - LOOKAHEAD: determine whether the current list could be a
          prefix of a valid list;
        - PUSH: go deeper into the prefix tree by appending the
          largest possible part to the current list;
        - ME: check whether the current list is valid and if yes return it
        - DECREASE: decrease the last part;
        - POP: pop the last part of the current list;
        - STOP: the iteration is finished.

        The attribute ``_next_state`` contains the next state ``next``
        should enter in.
    """
    def __init__(self, backend) -> Any:
        """IntegerListsLexIter.__init__(self, backend)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 1133)

        TESTS::

            sage: from sage.combinat.integer_lists.invlex import IntegerListsLexIter
            sage: C = IntegerListsLex(2, length=3)
            sage: I = IntegerListsLexIter(C)
            sage: I._search_ranges
            []
            sage: I._current_list
            []
            sage: I._j
            -1
            sage: I._current_sum
            0"""
    @overload
    def __iter__(self) -> Any:
        """IntegerListsLexIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 1163)

        Return ``self`` as per the iterator protocol.

        EXAMPLES::

            sage: from sage.combinat.integer_lists.invlex import IntegerListsLexIter
            sage: C = IntegerListsLex(2, length=3)
            sage: it = IntegerListsLexIter(C)
            sage: it.__iter__() is it
            True"""
    @overload
    def __iter__(self) -> Any:
        """IntegerListsLexIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 1163)

        Return ``self`` as per the iterator protocol.

        EXAMPLES::

            sage: from sage.combinat.integer_lists.invlex import IntegerListsLexIter
            sage: C = IntegerListsLex(2, length=3)
            sage: it = IntegerListsLexIter(C)
            sage: it.__iter__() is it
            True"""
    def __next__(self) -> Any:
        """IntegerListsLexIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/invlex.pyx (starting at line 1277)

        Return the next element in the iteration.

        EXAMPLES::

            sage: from sage.combinat.integer_lists.invlex import IntegerListsLexIter
            sage: C = IntegerListsLex(2, length=3)
            sage: I = IntegerListsLexIter(C)
            sage: next(I)
            [2, 0, 0]
            sage: next(I)
            [1, 1, 0]"""
