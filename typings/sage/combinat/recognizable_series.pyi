from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PrefixClosedSet:
    words: Incomplete
    elements: Incomplete
    def __init__(self, words) -> None:
        """
        A prefix-closed set.

        Creation of this prefix-closed set is interactive
        iteratively.

        INPUT:

        - ``words`` -- a class of words
          (instance of :class:`~sage.combinat.words.words.Words`)

        EXAMPLES::

            sage: from sage.combinat.recognizable_series import PrefixClosedSet
            sage: P = PrefixClosedSet(Words([0, 1], infinite=False)); P
            [word: ]

            sage: P = PrefixClosedSet.create_by_alphabet([0, 1]); P
            [word: ]

        See :meth:`iterate_possible_additions` for further examples.
        """
    @classmethod
    def create_by_alphabet(cls, alphabet):
        """
        A prefix-closed set.

        This is a convenience method for the
        creation of prefix-closed sets by specifying an alphabet.

        INPUT:

        - ``alphabet`` -- finite words over this ``alphabet``
          will used

        EXAMPLES::

            sage: from sage.combinat.recognizable_series import PrefixClosedSet
            sage: P = PrefixClosedSet.create_by_alphabet([0, 1]); P
            [word: ]
        """
    def add(self, w, check: bool = True) -> None:
        """
        Add a word to this prefix-closed set.

        INPUT:

        - ``w`` -- a word

        - ``check`` -- boolean (default: ``True``); if set, then it is verified
          whether all proper prefixes of ``w`` are already in this
          prefix-closed set

        OUTPUT:

        Nothing, but a
        :python:`RuntimeError<library/exceptions.html#exceptions.ValueError>`
        is raised if the check fails.

        EXAMPLES::

            sage: from sage.combinat.recognizable_series import PrefixClosedSet
            sage: P = PrefixClosedSet.create_by_alphabet([0, 1])
            sage: W = P.words
            sage: P.add(W([0])); P
            [word: , word: 0]
            sage: P.add(W([0, 1])); P
            [word: , word: 0, word: 01]
            sage: P.add(W([1, 1]))
            Traceback (most recent call last):
            ...
            ValueError: cannot add as not all prefixes of 11 are included yet
        """
    def iterate_possible_additions(self) -> Generator[Incomplete]:
        """
        Return an iterator over all elements including possible new elements.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.combinat.recognizable_series import PrefixClosedSet
            sage: P = PrefixClosedSet.create_by_alphabet([0, 1]); P
            [word: ]
            sage: for n, p in enumerate(P.iterate_possible_additions()):
            ....:     print('{}?'.format(p))
            ....:     if n in (0, 2, 3, 5):
            ....:         P.add(p)
            ....:         print('...added')
            0?
            ...added
            1?
            00?
            ...added
            01?
            ...added
            000?
            001?
            ...added
            010?
            011?
            0010?
            0011?
            sage: P.elements
            [word: , word: 0, word: 00, word: 01, word: 001]

        Calling the iterator once more, returns all elements::

            sage: list(P.iterate_possible_additions())
            [word: 0,
             word: 1,
             word: 00,
             word: 01,
             word: 000,
             word: 001,
             word: 010,
             word: 011,
             word: 0010,
             word: 0011]

        The method :meth:`iterate_possible_additions` is roughly equivalent to
        ::

            sage: list(p + a
            ....:      for p in P.elements
            ....:      for a in P.words.iterate_by_length(1))
            [word: 0,
             word: 1,
             word: 00,
             word: 01,
             word: 000,
             word: 001,
             word: 010,
             word: 011,
             word: 0010,
             word: 0011]

        However, the above does not allow to add elements during iteration,
        whereas :meth:`iterate_possible_additions` does.
        """
    def prefix_set(self):
        """
        Return the set of minimal (with respect to prefix ordering) elements
        of the complement of this prefix closed set.

        See also Proposition 2.3.1 of [BR2010a]_.

        OUTPUT: list

        EXAMPLES::

            sage: from sage.combinat.recognizable_series import PrefixClosedSet
            sage: P = PrefixClosedSet.create_by_alphabet([0, 1]); P
            [word: ]
            sage: for n, p in enumerate(P.iterate_possible_additions()):
            ....:     if n in (0, 1, 2, 4, 6):
            ....:         P.add(p)
            sage: P
            [word: , word: 0, word: 1, word: 00, word: 10, word: 000]
            sage: P.prefix_set()
            [word: 01, word: 11, word: 001, word: 100,
             word: 101, word: 0000, word: 0001]
        """

def minimize_result(operation):
    """
    A decorator for operations that enables control of
    automatic minimization on the result.

    INPUT:

    - ``operation`` -- a method

    OUTPUT: a method with the following additional argument:

    - ``minimize`` -- (default: ``None``) a boolean or ``None``.
      If ``True``, then :meth:`minimized` is called after the operation,
      if ``False``, then not. If this argument is ``None``, then
      the default specified by the parent's ``minimize_results`` is used.

    .. NOTE::

        If the result of ``operation`` is ``self``, then minimization is
        not applied unless ``minimize=True`` is explicitly set,
        in particular, independent of the parent's ``minimize_results``.

    TESTS::

        sage: from sage.combinat.recognizable_series import minimize_result
        sage: class P():
        ....:     pass
        sage: p = P()
        sage: class S():
        ....:     def __init__(self, s):
        ....:         self.s = s
        ....:     def __repr__(self):
        ....:         return self.s
        ....:     def parent(self):
        ....:         return p
        ....:     def minimized(self):
        ....:         return S(self.s + ' minimized')
        ....:     @minimize_result
        ....:     def operation(self):
        ....:         return S(self.s + ' result')

        sage: p.minimize_results = True
        sage: S('some').operation()
        some result minimized
        sage: S('some').operation(minimize=True)
        some result minimized
        sage: S('some').operation(minimize=False)
        some result

        sage: p.minimize_results = False
        sage: S('some').operation()
        some result
        sage: S('some').operation(minimize=True)
        some result minimized
        sage: S('some').operation(minimize=False)
        some result

    ::

        sage: class T(S):
        ....:     @minimize_result
        ....:     def nooperation(self):
        ....:         return self
        sage: t = T('some')
        sage: p.minimize_results = True
        sage: t.nooperation() is t
        True
        sage: t.nooperation(minimize=True) is t
        False
        sage: t.nooperation(minimize=False) is t
        True
        sage: p.minimize_results = False
        sage: t.nooperation() is t
        True
        sage: t.nooperation(minimize=True) is t
        False
        sage: t.nooperation(minimize=False) is t
        True
    """

class RecognizableSeries(ModuleElement):
    def __init__(self, parent, mu, left, right) -> None:
        """
        A recognizable series.

        - ``parent`` -- an instance of :class:`RecognizableSeriesSpace`

        - ``mu`` -- a family of square matrices, all of which have the
          same dimension.
          The indices of this family are the elements of the alphabet.
          ``mu`` may be a list or tuple of the same cardinality as the
          alphabet as well. See also :meth:`mu <mu>`.

        - ``left`` -- a vector. When evaluating a
          coefficient, this vector is multiplied from the left to the
          matrix obtained from :meth:`mu <mu>` applying on a word.
          See also :meth:`left <left>`.

        - ``right`` -- a vector. When evaluating a
          coefficient, this vector is multiplied from the right to the
          matrix obtained from :meth:`mu <mu>` applying on a word.
          See also :meth:`right <right>`.

        When created via the parent :class:`RecognizableSeriesSpace`, then
        the following option is available.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: S = Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:         vector([0, 1]), vector([1, 0])).transposed(); S
            [1] + 3*[01] + [10] + 5*[11] + 9*[001] + 3*[010] + ...

        We can access coefficients by
        ::

            sage: W = Rec.indices()
            sage: S[W([0, 0, 1])]
            9

        .. SEEALSO::

            :doc:`recognizable series <recognizable_series>`,
            :class:`RecognizableSeriesSpace`.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, (0,1))
            sage: M0 = Matrix([[1, 0], [0, 1]])
            sage: M1 = Matrix([[0, -1], [1, 2]])
            sage: Rec((M0, M1), (0, 1), (1, 1))
            [] + [0] + 3*[1] + [00] + 3*[01] + 3*[10] + 5*[11] + [000] + 3*[001] + 3*[010] + ...

            sage: M0 = Matrix([[3, 6], [0, 1]])
            sage: M1 = Matrix([[0, -6], [1, 5]])
            sage: L = vector([0, 1])
            sage: R = vector([1, 0])
            sage: S = Rec((M0, M1), L, R)
            sage: S.mu[0] is M0, S.mu[1] is M1, S.left is L, S.right is R
            (False, False, False, False)
            sage: S.mu[0].is_immutable(), S.mu[1].is_immutable(), S.left.is_immutable(), S.right.is_immutable()
            (True, True, True, True)
            sage: M0.set_immutable()
            sage: M1.set_immutable()
            sage: L.set_immutable()
            sage: R.set_immutable()
            sage: S = Rec((M0, M1), L, R)
            sage: S.mu[0] is M0, S.mu[1] is M1, S.left is L, S.right is R
            (True, True, True, True)
        """
    @property
    def mu(self):
        """
        When evaluating a coefficient, this is applied on each letter
        of a word; the result is a matrix.
        This extends :meth:`mu <mu>` to words over the parent's
        :meth:`~RecognizableSeriesSpace.alphabet`.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: M0 = Matrix([[1, 0], [0, 1]])
            sage: M1 = Matrix([[0, -1], [1, 2]])
            sage: S = Rec((M0, M1), vector([0, 1]), vector([1, 1]))
            sage: S.mu[0] == M0 and S.mu[1] == M1
            True
        """
    @property
    def left(self):
        """
        When evaluating a coefficient, this vector is multiplied from
        the left to the matrix obtained from :meth:`mu <mu>` applied on a
        word.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:     vector([0, 1]), vector([1, 0])).transposed().left
            (1, 0)
        """
    @property
    def right(self):
        """
        When evaluating a coefficient, this vector is multiplied from
        the right to the matrix obtained from :meth:`mu <mu>` applied on a
        word.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:     vector([0, 1]), vector([1, 0])).transposed().right
            (0, 1)
        """
    def linear_representation(self):
        """
        Return the linear representation of this series.

        OUTPUT:

        A triple ``(left, mu, right)`` containing
        the vectors :meth:`left <left>` and :meth:`right <right>`,
        and the family of matrices :meth:`mu <mu>`.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:     vector([0, 1]), vector([1, 0])
            ....:    ).transposed().linear_representation()
            ((1, 0),
             Finite family {0: [3 0]
                               [6 1],
                            1: [ 0  1]
                               [-6  5]},
             (0, 1))
        """
    @cached_method
    def coefficient_of_word(self, w, multiply_left: bool = True, multiply_right: bool = True):
        """
        Return the coefficient to word `w` of this series.

        INPUT:

        - ``w`` -- a word over the parent's
          :meth:`~RecognizableSeriesSpace.alphabet`

        - ``multiply_left`` -- boolean (default: ``True``); if ``False``,
          then multiplication by :meth:`left <left>` is skipped

        - ``multiply_right`` -- boolean (default: ``True``); if ``False``,
          then multiplication by :meth:`right <right>` is skipped

        OUTPUT:

        An element in the parent's
        :meth:`~RecognizableSeriesSpace.coefficient_ring`

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: W = Rec.indices()
            sage: S = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[0, -1], [1, 2]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: S[W(7.digits(2))]  # indirect doctest
            3

        TESTS::

            sage: w = W(6.digits(2))
            sage: S.coefficient_of_word(w)
            2
            sage: S.coefficient_of_word(w, multiply_left=False)
            (-1, 2)
            sage: S.coefficient_of_word(w, multiply_right=False)
            (2, 3)
            sage: S.coefficient_of_word(w, multiply_left=False, multiply_right=False)
            [-1 -2]
            [ 2  3]
        """
    __getitem__ = coefficient_of_word
    def __iter__(self):
        """
        Return an iterator over pairs ``(index, coefficient)``.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: S = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[0, -1], [1, 2]])),
            ....:         left=vector([0, 1]), right=vector([1, 0]))
            sage: from itertools import islice
            sage: list(islice(S, 10))
            [(word: , 0),
             (word: 0, 0),
             (word: 1, 1),
             (word: 00, 0),
             (word: 01, 1),
             (word: 10, 1),
             (word: 11, 2),
             (word: 000, 0),
             (word: 001, 1),
             (word: 010, 1)]
            sage: list(islice((s for s in S if s[1] != 0), 10))
            [(word: 1, 1),
             (word: 01, 1),
             (word: 10, 1),
             (word: 11, 2),
             (word: 001, 1),
             (word: 010, 1),
             (word: 011, 2),
             (word: 100, 1),
             (word: 101, 2),
             (word: 110, 2)]

            sage: S = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[0, -1], [1, 2]])),
            ....:         left=vector([1, 0]), right=vector([1, 0]))
            sage: list(islice((s for s in S if s[1] != 0), 10))
            [(word: , 1),
             (word: 0, 1),
             (word: 00, 1),
             (word: 11, -1),
             (word: 000, 1),
             (word: 011, -1),
             (word: 101, -1),
             (word: 110, -1),
             (word: 111, -2),
             (word: 0000, 1)]

        TESTS::

            sage: it = iter(S)
            sage: iter(it) is it
            True
            sage: iter(S) is not it
            True
        """
    def is_trivial_zero(self):
        """
        Return whether this recognizable series is trivially equal to
        zero (without any :meth:`minimization <minimized>`).

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:     left=vector([0, 1]), right=vector([1, 0])).is_trivial_zero()
            False
            sage: Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:     left=vector([0, 0]), right=vector([1, 0])).is_trivial_zero()
            True
            sage: Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:     left=vector([0, 1]), right=vector([0, 0])).is_trivial_zero()
            True

        The following two differ in the coefficient of the empty word::

            sage: Rec((Matrix([[0, 0], [0, 0]]), Matrix([[0, 0], [0, 0]])),
            ....:     left=vector([0, 1]), right=vector([1, 0])).is_trivial_zero()
            True
            sage: Rec((Matrix([[0, 0], [0, 0]]), Matrix([[0, 0], [0, 0]])),
            ....:     left=vector([1, 1]), right=vector([1, 1])).is_trivial_zero()
            False

        TESTS::

            sage: Rec.zero().is_trivial_zero()
            True

        The following is zero, but not trivially zero::

            sage: S = Rec((Matrix([[1, 0], [0, 0]]), Matrix([[1, 0], [0, 0]])),
            ....:         left=vector([0, 1]), right=vector([1, 0]))
            sage: S.is_trivial_zero()
            False
            sage: S.is_zero()
            True
        """
    def __bool__(self) -> bool:
        """
        Return whether this recognizable series is nonzero.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: bool(Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 1]), right=vector([1, 0])))
            False
            sage: bool(Rec((Matrix([[0, 0], [0, 0]]), Matrix([[0, 0], [0, 0]])),
            ....:          left=vector([0, 1]), right=vector([1, 0])))
            False
            sage: bool(Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 0]), right=vector([1, 0])))
            False
            sage: bool(Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 1]), right=vector([0, 0])))
            False

        ::

            sage: S = Rec((Matrix([[1, 0], [0, 0]]), Matrix([[1, 0], [0, 0]])),
            ....:         left=vector([0, 1]), right=vector([1, 0]))
            sage: bool(S)
            False
        """
    def __hash__(self):
        """
        A hash value of this recognizable series.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: S = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: hash(S)  # random
            42
        """
    def __eq__(self, other):
        """
        Return whether this recognizable series is equal to ``other``.

        INPUT:

        - ``other`` -- an object

        OUTPUT: boolean

        .. NOTE::

            This function uses the coercion model to find a common
            parent for the two operands.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: S = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([1, 1]), right=vector([1, 0]))
            sage: S
            [] + [0] + [1] + [00] + [01] + [10]
               + [11] + [000] + [001] + [010] + ...
            sage: Z1 = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: Z1
            0 + ...
            sage: Z2 = Rec((Matrix([[0, 0], [0, 0]]), Matrix([[0, 0], [0, 0]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: Z2
            0
            sage: S == Z1
            False
            sage: S == Z2
            False
            sage: Z1 == Z2
            True

        TESTS::

            sage: S == S
            True
            sage: S == None
            False
        """
    def __ne__(self, other):
        """
        Return whether this recognizable series is not equal to ``other``.

        INPUT:

        - ``other`` -- an object

        OUTPUT: boolean

        .. NOTE::

            This function uses the coercion model to find a common
            parent for the two operands.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Z1 = Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: Z2 = Rec((Matrix([[0, 0], [0, 0]]), Matrix([[0, 0], [0, 0]])),
            ....:          left=vector([0, 1]), right=vector([1, 0]))
            sage: Z1 != Z2
            False
            sage: Z1 != Z1
            False
        """
    def transposed(self):
        """
        Return the transposed series.

        OUTPUT: a :class:`RecognizableSeries`

        Each of the matrices in :meth:`mu <mu>` is transposed. Additionally
        the vectors :meth:`left <left>` and :meth:`right <right>` are switched.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: S = Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:         vector([0, 1]), vector([1, 0])).transposed()
            sage: S
            [1] + 3*[01] + [10] + 5*[11] + 9*[001] + 3*[010]
                + 15*[011] + [100] + 11*[101] + 5*[110] + ...
            sage: S.mu[0], S.mu[1], S.left, S.right
            (
            [3 0]  [ 0  1]
            [6 1], [-6  5], (1, 0), (0, 1)
            )
            sage: T = S.transposed()
            sage: T
            [1] + [01] + 3*[10] + 5*[11] + [001] + 3*[010]
                + 5*[011] + 9*[100] + 11*[101] + 15*[110] + ...
            sage: T.mu[0], T.mu[1], T.left, T.right
            (
            [3 6]  [ 0 -6]
            [0 1], [ 1  5], (0, 1), (1, 0)
            )

        TESTS::

            sage: T.mu[0].is_immutable(), T.mu[1].is_immutable(), T.left.is_immutable(), T.right.is_immutable()
            (True, True, True, True)
        """
    @cached_method
    def minimized(self):
        """
        Return a recognizable series equivalent to this series, but
        with a minimized linear representation.

        The coefficients of the involved matrices need be in a field.
        If this is not the case, then the coefficients are
        automatically coerced to their fraction field.

        OUTPUT: a :class:`RecognizableSeries`

        ALGORITHM:

        This method implements the minimization algorithm presented in
        Chapter 2 of [BR2010a]_.

        .. NOTE::

            Due to the algorithm, the left vector of the result
            is always `(1, 0, \\ldots, 0)`, i.e., the first vector of the
            standard basis.

        EXAMPLES::

            sage: from itertools import islice
            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])

            sage: S = Rec((Matrix([[3, 6], [0, 1]]), Matrix([[0, -6], [1, 5]])),
            ....:         vector([0, 1]), vector([1, 0])).transposed()
            sage: S
            [1] + 3*[01] + [10] + 5*[11] + 9*[001] + 3*[010]
                + 15*[011] + [100] + 11*[101] + 5*[110] + ...
            sage: M = S.minimized()
            sage: M.mu[0], M.mu[1], M.left, M.right
            (
            [3 0]  [ 0  1]
            [6 1], [-6  5], (1, 0), (0, 1)
            )
            sage: M.left == vector([1, 0])
            True
            sage: all(c == d and v == w
            ....:     for (c, v), (d, w) in islice(zip(iter(S), iter(M)), 20))
            True

            sage: S = Rec((Matrix([[2, 0], [1, 1]]), Matrix([[2, 0], [2, 1]])),
            ....:         vector([1, 0]), vector([1, 1]))
            sage: S
            [] + 2*[0] + 2*[1] + 4*[00] + 4*[01] + 4*[10] + 4*[11]
               + 8*[000] + 8*[001] + 8*[010] + ...
            sage: M = S.minimized()
            sage: M.mu[0], M.mu[1], M.left, M.right
            ([2], [2], (1), (1))
            sage: all(c == d and v == w
            ....:     for (c, v), (d, w) in islice(zip(iter(S), iter(M)), 20))
            True

        TESTS::

            sage: Rec((Matrix([[0]]), Matrix([[0]])),
            ....:     vector([1]), vector([0])).minimized().linear_representation()
            ((), Finite family {0: [], 1: []}, ())
        """
    def dimension(self):
        """
        Return the dimension of this recognizable series.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]])),
            ....:     left=vector([0, 1]), right=vector([1, 0])).dimension()
            2
        """
    @minimize_result
    def hadamard_product(self, other):
        """
        Return the Hadamard product of this recognizable series
        and the ``other`` recognizable series, i.e., multiply the two
        series coefficient-wise.

        INPUT:

        - ``other`` -- a :class:`RecognizableSeries` with the same parent
          as this recognizable series

        - ``minimize`` -- (default: ``None``) a boolean or ``None``.
          If ``True``, then :meth:`minimized` is called after the operation,
          if ``False``, then not. If this argument is ``None``, then
          the default specified by the parent's ``minimize_results`` is used.

        OUTPUT: a :class:`RecognizableSeries`

        EXAMPLES::

            sage: Seq2 = RegularSequenceRing(2, ZZ)

            sage: E = Seq2((Matrix([[0, 1], [0, 1]]), Matrix([[0, 0], [0, 1]])),
            ....:          vector([1, 0]), vector([1, 1]))
            sage: E
            2-regular sequence 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, ...

            sage: O = Seq2((Matrix([[0, 0], [0, 1]]), Matrix([[0, 1], [0, 1]])),
            ....:          vector([1, 0]), vector([0, 1]))
            sage: O
            2-regular sequence 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ...

            sage: C = Seq2((Matrix([[2, 0], [2, 1]]), Matrix([[0, 1], [-2, 3]])),
            ....:          vector([1, 0]), vector([0, 1]))
            sage: C
            2-regular sequence 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

        ::

            sage: CE = C.hadamard_product(E)
            sage: CE
            2-regular sequence 0, 0, 2, 0, 4, 0, 6, 0, 8, 0, ...
            sage: CE.linear_representation()
            ((1, 0, 0),
             Finite family {0: [0 1 0]
                               [0 2 0]
                               [0 2 1],
                            1: [ 0  0  0]
                               [ 0  0  1]
                               [ 0 -2  3]},
             (0, 0, 2))

            sage: Z = E.hadamard_product(O)
            sage: Z
            2-regular sequence 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...
            sage: Z.linear_representation()
            ((),
             Finite family {0: [],
                            1: []},
             ())

        TESTS::

            sage: EC = E.hadamard_product(C, minimize=False)
            sage: EC
            2-regular sequence 0, 0, 2, 0, 4, 0, 6, 0, 8, 0, ...
            sage: EC.linear_representation()
            ((1, 0, 0, 0),
             Finite family {0: [0 0 2 0]
                               [0 0 2 1]
                               [0 0 2 0]
                               [0 0 2 1],
                            1: [ 0  0  0  0]
                               [ 0  0  0  0]
                               [ 0  0  0  1]
                               [ 0  0 -2  3]},
             (0, 1, 0, 1))
            sage: MEC = EC.minimized()
            sage: MEC
            2-regular sequence 0, 0, 2, 0, 4, 0, 6, 0, 8, 0, ...
            sage: MEC.linear_representation()
            ((1, 0, 0),
             Finite family {0: [0 1 0]
                               [0 2 0]
                               [0 2 1],
                            1: [ 0  0  0]
                               [ 0  0  1]
                               [ 0 -2  3]},
             (0, 0, 2))
        """

class RecognizableSeriesSpace(UniqueRepresentation, Parent):
    """
    The space of recognizable series on the given alphabet and
    with the given coefficients.

    INPUT:

    - ``coefficient_ring`` -- a (semi-)ring

    - ``alphabet`` -- tuple, list or
      :class:`~sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet`.
      If specified, then the ``indices`` are the
      finite words over this ``alphabet``.
      ``alphabet`` and ``indices`` cannot be specified
      at the same time.

    - ``indices`` -- a SageMath-parent of finite words over an alphabet.
      ``alphabet`` and ``indices`` cannot be specified
      at the same time.

    - ``category`` -- (default: ``None``) the category of this
      space

    EXAMPLES:

    We create a recognizable series that counts the number of ones in each word::

        sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
        sage: Rec
        Space of recognizable series on {0, 1} with coefficients in Integer Ring
        sage: Rec((Matrix([[1, 0], [0, 1]]), Matrix([[1, 1], [0, 1]])),
        ....:     vector([1, 0]), vector([0, 1]))
        [1] + [01] + [10] + 2*[11] + [001] + [010] + 2*[011] + [100] + 2*[101] + 2*[110] + ...

    All of the following examples create the same space::

        sage: Rec1 = RecognizableSeriesSpace(ZZ, [0, 1])
        sage: Rec1
        Space of recognizable series on {0, 1} with coefficients in Integer Ring
        sage: Rec2 = RecognizableSeriesSpace(coefficient_ring=ZZ, alphabet=[0, 1])
        sage: Rec2
        Space of recognizable series on {0, 1} with coefficients in Integer Ring
        sage: Rec3 = RecognizableSeriesSpace(ZZ, indices=Words([0, 1], infinite=False))
        sage: Rec3
        Space of recognizable series on {0, 1} with coefficients in Integer Ring

    .. SEEALSO::

        :doc:`recognizable series <recognizable_series>`,
        :class:`RecognizableSeries`.
    """
    Element = RecognizableSeries
    @staticmethod
    def __classcall__(cls, *args, **kwds):
        """
        Prepare normalizing the input in order to ensure a
        unique representation.

        For more information see :class:`RecognizableSeriesSpace`
        and :meth:`__normalize__`.

        TESTS::

            sage: Rec1 = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec1
            Space of recognizable series on {0, 1} with coefficients in Integer Ring
            sage: Rec2 = RecognizableSeriesSpace(coefficient_ring=ZZ, alphabet=[0, 1])
            sage: Rec2
            Space of recognizable series on {0, 1} with coefficients in Integer Ring
            sage: Rec3 = RecognizableSeriesSpace(ZZ, indices=Words([0, 1], infinite=False))
            sage: Rec3
            Space of recognizable series on {0, 1} with coefficients in Integer Ring
            sage: Rec1 is Rec2 is Rec3
            True
        """
    @classmethod
    def __normalize__(cls, coefficient_ring=None, alphabet=None, indices=None, category=None, minimize_results: bool = True):
        """
        Normalize the input in order to ensure a unique
        representation.

        For more information see :class:`RecognizableSeriesSpace`.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])  # indirect doctest
            sage: Rec.category()
            Category of modules over Integer Ring
            sage: RecognizableSeriesSpace([0, 1], [0, 1])
            Traceback (most recent call last):
            ...
            ValueError: coefficient ring [0, 1] is not a semiring

        ::

            sage: W = Words([0, 1], infinite=False)
            sage: RecognizableSeriesSpace(ZZ)
            Traceback (most recent call last):
            ...
            ValueError: specify either 'alphabet' or 'indices'
            sage: RecognizableSeriesSpace(ZZ, alphabet=[0, 1], indices=W)
            Traceback (most recent call last):
            ...
            ValueError: specify either 'alphabet' or 'indices'
            sage: RecognizableSeriesSpace(alphabet=[0, 1])
            Traceback (most recent call last):
            ...
            ValueError: no coefficient ring specified
            sage: RecognizableSeriesSpace(ZZ, indices=Words(ZZ))
            Traceback (most recent call last):
            ...
            NotImplementedError: alphabet is not finite
        """
    def __init__(self, coefficient_ring, indices, category, minimize_results) -> None:
        """
        See :class:`RecognizableSeriesSpace` for details.

        INPUT:

        - ``coefficients`` -- a (semi-)ring

        - ``indices`` -- a SageMath-parent of finite words over an alphabet

        - ``category`` -- (default: ``None``) the category of this
          space

        - ``minimize_results`` -- boolean (default: ``True``); if set, then
          :meth:`RecognizableSeries.minimized` is automatically called
          after performing operations.

        TESTS::

            sage: RecognizableSeriesSpace(ZZ, [0, 1])
            Space of recognizable series on {0, 1} with coefficients in Integer Ring

        ::

            sage: from itertools import islice
            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: TestSuite(Rec).run(  # long time
            ....:    verbose=True,
            ....:    elements=tuple(islice(Rec.some_elements(), 4)))
            running ._test_additive_associativity() . . . pass
            running ._test_an_element() . . . pass
            running ._test_cardinality() . . . pass
            running ._test_category() . . . pass
            running ._test_construction() . . . pass
            running ._test_elements() . . .
              Running the test suite of self.an_element()
              running ._test_category() . . . pass
              running ._test_eq() . . . pass
              running ._test_new() . . . pass
              running ._test_nonzero_equal() . . . pass
              running ._test_not_implemented_methods() . . . pass
              running ._test_pickling() . . . pass
              pass
            running ._test_elements_eq_reflexive() . . . pass
            running ._test_elements_eq_symmetric() . . . pass
            running ._test_elements_eq_transitive() . . . pass
            running ._test_elements_neq() . . . pass
            running ._test_eq() . . . pass
            running ._test_new() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . pass
            running ._test_some_elements() . . . pass
            running ._test_zero() . . . pass
        """
    def __reduce__(self):
        """
        Pickling support.

        TESTS::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: loads(dumps(Rec))  # indirect doctest
            Space of recognizable series on {0, 1} with coefficients in Integer Ring
        """
    def alphabet(self):
        """
        Return the alphabet of this recognizable series space.

        OUTPUT: a totally ordered set

        EXAMPLES::

            sage: RecognizableSeriesSpace(ZZ, [0, 1]).alphabet()
            {0, 1}

        TESTS::

            sage: type(RecognizableSeriesSpace(ZZ, [0, 1]).alphabet())
            <class 'sage.sets.totally_ordered_finite_set.TotallyOrderedFiniteSet_with_category'>
        """
    def indices(self):
        """
        Return the indices of the recognizable series.

        OUTPUT: the set of finite words over the alphabet

        EXAMPLES::

            sage: RecognizableSeriesSpace(ZZ, [0, 1]).indices()
            Finite words over {0, 1}
        """
    def coefficient_ring(self):
        """
        Return the coefficients of this recognizable series space.

        OUTPUT:

        A (semi-)ring

        EXAMPLES::

            sage: RecognizableSeriesSpace(ZZ, [0, 1]).coefficient_ring()
            Integer Ring
        """
    @property
    def minimize_results(self):
        """
        A boolean indicating whether
        :meth:`RecognizableSeries.minimized` is automatically called
        after performing operations.

        TESTS::

            sage: RecognizableSeriesSpace(ZZ, [0, 1]).minimize_results
            True
            sage: RecognizableSeriesSpace(ZZ, [0, 1], minimize_results=True).minimize_results
            True
            sage: RecognizableSeriesSpace(ZZ, [0, 1], minimize_results=False).minimize_results
            False
        """
    def some_elements(self, **kwds) -> Generator[Incomplete]:
        """
        Return some elements of this recognizable series space.

        See :class:`TestSuite` for a typical use case.

        INPUT:

        - ``kwds`` are passed on to the element constructor

        OUTPUT: an iterator

        EXAMPLES::

            sage: tuple(RecognizableSeriesSpace(ZZ, [0, 1]).some_elements())
            ([1] + [01] + [10] + 2*[11] + [001] + [010]
                 + 2*[011] + [100] + 2*[101] + 2*[110] + ...,
             [] + [1] + [11] + [111] + [1111] + [11111] + [111111] + ...,
             [] + [0] + [1] + [00] + [10] + [11]
                + [000] - 1*[001] + [100] + [110] + ...,
             2*[] - 1*[1] + 2*[10] - 1*[101]
                  + 2*[1010] - 1*[10101] + 2*[101010] + ...,
             [] + [1] + 6*[00] + [11] - 39*[000] + 5*[001] + 6*[100] + [111]
                + 288*[0000] - 33*[0001] + ...,
             -5*[] + ...,
             ...
             210*[] + ...,
             2210*[] - 170*[0] + 170*[1] + ...)
        """
    @cached_method
    def one(self):
        """
        Return the one element of this :class:`RecognizableSeriesSpace`,
        i.e. the embedding of the one of the coefficient ring into
        this :class:`RecognizableSeriesSpace`.

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: O = Rec.one(); O
            [] + ...
            sage: O.linear_representation()
            ((1), Finite family {0: [0], 1: [0]}, (1))

        TESTS::

            sage: Rec.one() is Rec.one()
            True
        """
    @cached_method
    def one_hadamard(self):
        """
        Return the identity with respect to the
        :meth:`~RecognizableSeries.hadamard_product`, i.e. the
        coefficient-wise multiplication.

        OUTPUT: a :class:`RecognizableSeries`

        EXAMPLES::

            sage: Rec = RecognizableSeriesSpace(ZZ, [0, 1])
            sage: Rec.one_hadamard()
            [] + [0] + [1] + [00] + [01] + [10]
               + [11] + [000] + [001] + [010] + ...

        TESTS::

            sage: Rec.one_hadamard() is Rec.one_hadamard()
            True
        """
