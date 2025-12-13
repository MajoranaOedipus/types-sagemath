from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Matrix as Matrix
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Rule(UniqueRepresentation):
    '''
    Generic base class for an insertion rule for an RSK-type correspondence.

    An instance of this class should implement a method
    :meth:`insertion` (which can be applied to a letter ``j``
    and a list ``r``, and modifies ``r`` in place by "bumping"
    ``j`` into it appropriately; it then returns the bumped-out
    entry or ``None`` if no such entry exists) and a method
    :meth:`reverse_insertion` (which does the same but for reverse
    bumping).
    It may also implement :meth:`_backward_format_output` and
    :meth:`_forward_format_output` if the RSK correspondence should
    return something other than (semi)standard tableaux (in the
    forward direction) and matrices or biwords (in the backward
    direction).
    The :meth:`to_pairs` method should also be overridden if
    the input for the (forward) RSK correspondence is not the
    usual kind of biwords (i.e., pairs of two `n`-tuples
    `[a_1, a_2, \\ldots, a_n]` and `[b_1, b_2, \\ldots, b_n]`
    satisfying `(a_1, b_1) \\leq (a_2, b_2) \\leq \\cdots
    \\leq (a_n, b_n)` in lexicographic order).
    Finally, it :meth:`forward_rule` and :meth:`backward_rule`
    have to be overridden if the overall structure of the
    RSK correspondence differs from that of classical RSK (see,
    e.g., the case of Hecke insertion, in which a letter bumped
    into a row may change a different row).
    '''
    def to_pairs(self, obj1=None, obj2=None, check: bool = True):
        '''
        Given a valid input for the RSK algorithm, such as
        two `n`-tuples ``obj1`` `= [a_1, a_2, \\ldots, a_n]`
        and ``obj2`` `= [b_1, b_2, \\ldots, b_n]` forming a biword
        (i.e., satisfying
        `a_1 \\leq a_2 \\leq \\cdots \\leq a_n`, and if
        `a_i = a_{i+1}`, then `b_i \\leq b_{i+1}`),
        or a matrix ("generalized permutation"), or a single word,
        return the array
        `[(a_1, b_1), (a_2, b_2), \\ldots, (a_n, b_n)]`.

        INPUT:

        - ``obj1``, ``obj2`` -- anything representing a biword
          (see the doc of :meth:`forward_rule` for the
          encodings accepted)

        - ``check`` -- boolean (default: ``True``); whether to check that
          ``obj1`` and ``obj2`` actually define a valid biword

        EXAMPLES::

            sage: from sage.combinat.rsk import Rule
            sage: list(Rule().to_pairs([1, 2, 2, 2], [2, 1, 1, 2]))
            [(1, 2), (2, 1), (2, 1), (2, 2)]
            sage: m = Matrix(ZZ, 3, 2, [0,1,1,0,0,2]) ; m
            [0 1]
            [1 0]
            [0 2]
            sage: list(Rule().to_pairs(m))
            [(1, 2), (2, 1), (3, 2), (3, 2)]
        '''
    def forward_rule(self, obj1, obj2, check_standard: bool = False, check: bool = True):
        """
        Return a pair of tableaux obtained by applying forward
        insertion to the generalized permutation ``[obj1, obj2]``.

        INPUT:

        - ``obj1``, ``obj2`` -- can be one of the following ways to
          represent a generalized permutation (or, equivalently,
          biword):

          - two lists ``obj1`` and ``obj2`` of equal length,
            to be interpreted as the top row and the bottom row of
            the biword

          - a matrix ``obj1`` of nonnegative integers, to be
            interpreted as the generalized permutation in matrix
            form (in this case, ``obj2`` is ``None``)

          - a word ``obj1`` in an ordered alphabet, to be
            interpreted as the bottom row of the biword (in this
            case, ``obj2`` is ``None``; the top row of the biword
            is understood to be `(1, 2, \\ldots, n)` by default)

          - any object ``obj1`` which has a method ``_rsk_iter()``,
            as long as this method returns an iterator yielding
            pairs of numbers, which then are interpreted as top
            entries and bottom entries in the biword (in this case,
            ``obj2`` is ``None``)

        - ``check_standard`` -- boolean (default: ``False``); check if either
          of the resulting tableaux is a standard tableau, and if so, typecast
          it as such

        - ``check`` -- boolean (default: ``True``); whether to check
          that ``obj1`` and ``obj2`` actually define a valid
          biword

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleRSK
            sage: RuleRSK().forward_rule([3,3,2,4,1], None)
            [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]
            sage: RuleRSK().forward_rule([1, 1, 1, 3, 7], None)
            [[[1, 1, 1, 3, 7]], [[1, 2, 3, 4, 5]]]
            sage: RuleRSK().forward_rule([7, 6, 3, 3, 1], None)
            [[[1, 3], [3], [6], [7]], [[1, 4], [2], [3], [5]]]
        """
    def backward_rule(self, p, q, output):
        """
        Return the generalized permutation obtained by applying reverse
        insertion to a pair of tableaux ``(p, q)``.

        INPUT:

        - ``p``, ``q`` -- two tableaux of the same shape

        - ``output`` -- (default: ``'array'``) if ``q`` is semi-standard:

          - ``'array'`` -- as a two-line array (i.e. generalized permutation
            or biword)
          - ``'matrix'`` -- as an integer matrix

          and if ``q`` is standard, we can also have the output:

          - ``'word'`` -- as a word

          and additionally if ``p`` is standard, we can also have the output:

          - ``'permutation'`` -- as a permutation

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleRSK
            sage: t1 = Tableau([[1, 3, 4], [2], [3]])
            sage: t2 = Tableau([[1, 2, 4], [3], [5]])
            sage: RuleRSK().backward_rule(t1, t2, 'array')
            [[1, 2, 3, 4, 5], [3, 3, 2, 4, 1]]
            sage: t1 = Tableau([[1, 1, 1, 3, 7]])
            sage: t2 = Tableau([[1, 2, 3, 4, 5]])
            sage: RuleRSK().backward_rule(t1, t2, 'array')
            [[1, 2, 3, 4, 5], [1, 1, 1, 3, 7]]
            sage: t1 = Tableau([[1, 3], [3], [6], [7]])
            sage: t2 = Tableau([[1, 4], [2], [3], [5]])
            sage: RuleRSK().backward_rule(t1, t2, 'array')
            [[1, 2, 3, 4, 5], [7, 6, 3, 3, 1]]
        """

class RuleRSK(Rule):
    """
    Rule for the classical Robinson-Schensted-Knuth insertion.

    See :func:`RSK` for the definition of this operation.

    EXAMPLES::

        sage: RSK([1, 2, 2, 2], [2, 1, 1, 2], insertion=RSK.rules.RSK)
        [[[1, 1, 2], [2]], [[1, 2, 2], [2]]]
        sage: p = Tableau([[1,2,2],[2]]); q = Tableau([[1,3,3],[2]])
        sage: RSK_inverse(p, q, insertion=RSK.rules.RSK)
        [[1, 2, 3, 3], [2, 1, 2, 2]]
    """
    def insertion(self, j, r):
        """
        Insert the letter ``j`` from the second row of the biword
        into the row `r` using classical Schensted insertion,
        if there is bumping to be done.

        The row `r` is modified in place if bumping occurs. The bumped-out
        entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleRSK
            sage: qr, r = [1,2,3,4,5], [3,3,2,4,8]
            sage: j = RuleRSK().insertion(9, r)
            sage: j is None
            True
            sage: qr, r = [1,2,3,4,5], [3,3,2,4,8]
            sage: j = RuleRSK().insertion(3, r)
            sage: j
            4
        """
    def reverse_insertion(self, x, row):
        """
        Reverse bump the row ``row`` of the current insertion tableau
        with the number ``x``.

        The row ``row`` is modified in place. The bumped-out entry
        is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleRSK
            sage: r =  [2,3,3,4,8]
            sage: x = RuleRSK().reverse_insertion(4, r); r
            [2, 3, 4, 4, 8]
            sage: x
            3
        """

class RuleEG(Rule):
    """
    Rule for Edelman-Greene insertion.

    For a reduced word of a permutation (i.e., an element of a type `A`
    Coxeter group), one can use Edelman-Greene insertion, an algorithm
    defined in [EG1987]_ Definition 6.20 (where it is referred to as
    Coxeter-Knuth insertion). The Edelman-Greene insertion is similar to the
    standard row insertion except that (using the notations in
    the documentation of :func:`RSK`) if `k_i` and `k_i + 1` both
    exist in row `i`, we *only* set `k_{i+1} = k_i + 1` and continue.

    EXAMPLES:

    Let us reproduce figure 6.4 in [EG1987]_::

        sage: RSK([2,3,2,1,2,3], insertion=RSK.rules.EG)
        [[[1, 2, 3], [2, 3], [3]], [[1, 2, 6], [3, 5], [4]]]

    Some more examples::

        sage: a = [2, 1, 2, 3, 2]
        sage: pq = RSK(a, insertion=RSK.rules.EG); pq
        [[[1, 2, 3], [2, 3]], [[1, 3, 4], [2, 5]]]
        sage: RSK(RSK_inverse(*pq, insertion=RSK.rules.EG, output='matrix'),
        ....:     insertion=RSK.rules.EG)
        [[[1, 2, 3], [2, 3]], [[1, 3, 4], [2, 5]]]
        sage: RSK_inverse(*pq, insertion=RSK.rules.EG)
        [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2]]

    The RSK algorithm (:func:`RSK`) built using the Edelman-Greene
    insertion rule ``RuleEG`` is a bijection from reduced words of
    permutations/elements of a type `A` Coxeter group to pairs
    consisting of an increasing tableau and a standard tableau
    of the same shape (see [EG1987]_ Theorem 6.25).
    The inverse of this bijection is obtained using :func:`RSK_inverse`.
    If the optional parameter ``output = 'permutation'`` is set in
    :func:`RSK_inverse`, then the function returns not the
    reduced word itself but the permutation (of smallest possible
    size) whose reduced word it is (although the order of the
    letters is reverse to the usual Sage convention)::

        sage: w = RSK_inverse(*pq, insertion=RSK.rules.EG, output='permutation'); w
        [4, 3, 1, 2]
        sage: list(reversed(a)) in w.reduced_words()
        True

    TESTS:

    Let us check that :func:`RSK_inverse` is the inverse of :func:`RSK`
    on the different types of inputs/outputs for Edelman-Greene.
    First we can check on the reduced words (specifically, those that can
    be obtained using the ``reduced_word()`` method from permutations)::

        sage: g = lambda w: RSK_inverse(*RSK(w, insertion=RSK.rules.EG),
        ....:                           insertion=RSK.rules.EG, output='word')
        sage: all(p.reduced_word() == list(g(p.reduced_word()))
        ....:     for n in range(7) for p in Permutations(n))
        True

    In case of non-standard tableaux `P, Q`::

        sage: RSK_inverse(*RSK([1, 2, 3, 2, 1], insertion='EG'),
        ....:             insertion='EG')
        [[1, 2, 3, 4, 5], [1, 2, 3, 2, 1]]
        sage: RSK_inverse(*RSK([1, 1, 1, 2], [1, 2, 3, 4],
        ....:             insertion=RSK.rules.EG), insertion=RSK.rules.EG)
        [[1, 1, 1, 2], [1, 2, 3, 4]]
        sage: RSK_inverse(*RSK([1, 2, 3, 3], [2, 1, 2, 2], insertion='EG'),
        ....:             insertion='EG')
        [[1, 2, 3, 3], [2, 1, 2, 2]]

    Since the column reading of the insertion tableau from
    Edelman-Greene insertion gives one of reduced words for the
    original permutation, we can also check for that::

        sage: f = lambda p: [x for row in reversed(p) for x in row]
        sage: g = lambda wd: RSK(wd, insertion=RSK.rules.EG)[0]
        sage: all(p == Permutations(n).from_reduced_word(f(g(wd)))
        ....:     for n in range(6) for p in Permutations(n)
        ....:     for wd in p.reduced_words())
        True
    """
    def insertion(self, j, r):
        """
        Insert the letter ``j`` from the second row of the biword
        into the row `r` using Edelman-Greene insertion,
        if there is bumping to be done.

        The row `r` is modified in place if bumping occurs. The bumped-out
        entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleEG
            sage: qr, r =  [1,2,3,4,5], [3,3,2,4,8]
            sage: j = RuleEG().insertion(9, r)
            sage: j is None
            True
            sage: qr, r = [1,2,3,4,5], [2,3,4,5,8]
            sage: j = RuleEG().insertion(3, r); r
            [2, 3, 4, 5, 8]
            sage: j
            4
            sage: qr, r = [1,2,3,4,5], [2,3,5,5,8]
            sage: j = RuleEG().insertion(3, r); r
            [2, 3, 3, 5, 8]
            sage: j
            5
        """
    def reverse_insertion(self, x, row):
        """
        Reverse bump the row ``row`` of the current insertion tableau
        with the number ``x``.

        The row ``row`` is modified in place. The bumped-out entry
        is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleEG
            sage: r =  [1,1,1,2,3,3]
            sage: x = RuleEG().reverse_insertion(3, r); r
            [1, 1, 1, 2, 3, 3]
            sage: x
            2
        """

class RuleHecke(Rule):
    '''
    Rule for Hecke insertion.

    The Hecke RSK algorithm is similar to the classical RSK algorithm,
    but is defined using the Hecke insertion introduced in in
    [BKSTY06]_ (but using rows instead of columns).
    It is not clear in what generality it works; thus, following
    [BKSTY06]_, we shall assume that our biword `p` has top row
    `(1, 2, \\ldots, n)` (or, at least, has its top row strictly
    increasing).

    The Hecke RSK algorithm returns a pair of an increasing tableau
    and a set-valued standard tableau. If
    `p = ((j_0, k_0), (j_1, k_1), \\ldots, (j_{\\ell-1}, k_{\\ell-1}))`,
    then the algorithm recursively constructs pairs
    `(P_0, Q_0), (P_1, Q_1), \\ldots, (P_\\ell, Q_\\ell)` of tableaux.
    The construction of `P_{t+1}` and `Q_{t+1}` from `P_t`, `Q_t`,
    `j_t` and `k_t` proceeds as follows: Set `i = j_t`, `x = k_t`,
    `P = P_t` and `Q = Q_t`. We are going to insert `x` into the
    increasing tableau `P` and update the set-valued "recording
    tableau" `Q` accordingly. As in the classical RSK algorithm, we
    first insert `x` into row `1` of `P`, then into row `2` of the
    resulting tableau, and so on, until the construction terminates.
    The details are different: Suppose we are inserting `x` into
    row `R` of `P`. If (Case 1) there exists an entry `y` in row `R`
    such that `x < y`, then let `y` be the minimal such entry. We
    replace this entry `y` with `x` if the result is still an
    increasing tableau; in either subcase, we then continue
    recursively, inserting `y` into the next row of `P`.
    If, on the other hand, (Case 2) no such `y` exists, then we
    append `x` to the end of `R` if the result is an increasing
    tableau (Subcase 2.1), and otherwise (Subcase 2.2) do nothing.
    Furthermore, in Subcase 2.1, we add the box that we have just
    filled with `x` in `P` to the shape of `Q`, and fill it with
    the one-element set `\\{i\\}`. In Subcase 2.2, we find the
    bottommost box of the column containing the rightmost box of
    row `R`, and add `i` to the entry of `Q` in this box (this
    entry is a set, since `Q` is set-valued). In either
    subcase, we terminate the recursion, and set
    `P_{t+1} = P` and `Q_{t+1} = Q`.

    Notice that set-valued tableaux are encoded as tableaux whose
    entries are tuples of positive integers; each such tuple is strictly
    increasing and encodes a set (namely, the set of its entries).

    EXAMPLES:

    As an example of Hecke insertion, we reproduce
    Example 2.1 in :arxiv:`0801.1319v2`::

        sage: w = [5, 4, 1, 3, 4, 2, 5, 1, 2, 1, 4, 2, 4]
        sage: P,Q = RSK(w, insertion=RSK.rules.Hecke); [P,Q]
        [[[1, 2, 4, 5], [2, 4, 5], [3, 5], [4], [5]],
         [[(1,), (4,), (5,), (7,)],
          [(2,), (9,), (11, 13)],
          [(3,), (12,)],
          [(6,)],
          [(8, 10)]]]
        sage: wp = RSK_inverse(P, Q, insertion=RSK.rules.Hecke,
        ....:                    output=\'list\'); wp
        [5, 4, 1, 3, 4, 2, 5, 1, 2, 1, 4, 2, 4]
        sage: wp == w
        True
    '''
    def forward_rule(self, obj1, obj2, check_standard: bool = False):
        """
        Return a pair of tableaux obtained by applying Hecke
        insertion to the generalized permutation ``[obj1, obj2]``.

        INPUT:

        - ``obj1``, ``obj2`` -- can be one of the following ways to
          represent a generalized permutation (or, equivalently,
          biword):

          - two lists ``obj1`` and ``obj2`` of equal length,
            to be interpreted as the top row and the bottom row of
            the biword

          - a word ``obj1`` in an ordered alphabet, to be
            interpreted as the bottom row of the biword (in this
            case, ``obj2`` is ``None``; the top row of the biword
            is understood to be `(1, 2, \\ldots, n)` by default)

        - ``check_standard`` -- boolean (default: ``False``); check if either
          of the resulting tableaux is a standard tableau, and if so, typecast
          it as such

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleHecke
            sage: p, q = RuleHecke().forward_rule([3,3,2,4,1], None);p
            [[1, 4], [2], [3]]
            sage: q
            [[(1, 2), (4,)], [(3,)], [(5,)]]
            sage: isinstance(p, SemistandardTableau)
            True
            sage: isinstance(q, Tableau)
            True
        """
    def backward_rule(self, p, q, output):
        """
        Return the generalized permutation obtained by applying reverse
        Hecke insertion to a pair of tableaux ``(p, q)``.

        INPUT:

        - ``p``, ``q`` -- two tableaux of the same shape

        - ``output`` -- (default: ``'array'``) if ``q`` is semi-standard:

          - ``'array'`` -- as a two-line array (i.e. generalized permutation
            or biword)

          and if ``q`` is standard set-valued, we can have the output:

          - ``'word'`` -- as a word
          - ``'list'`` -- as a list

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleHecke
            sage: t1 = Tableau([[1, 4], [2], [3]])
            sage: t2 = Tableau([[(1, 2), (4,)], [(3,)], [(5,)]])
            sage: RuleHecke().backward_rule(t1, t2, 'array')
            [[1, 2, 3, 4, 5], [3, 3, 2, 4, 1]]
            sage: t1 = Tableau([[1, 4], [2, 3]])
            sage: t2 = Tableau([[(1, 2), (4,)], [(3,)], [(5,)]])
            sage: RuleHecke().backward_rule(t1, t2, 'array')
            Traceback (most recent call last):
            ...
            ValueError: p(=[[1, 4], [2, 3]]) and
             q(=[[(1, 2), (4,)], [(3,)], [(5,)]]) must have the same shape
        """
    def insertion(self, j, ir, r, p):
        """
        Insert the letter ``j`` from the second row of the biword
        into the row `r` of the increasing tableau `p` using
        Hecke insertion, provided that `r` is the `ir`-th row
        of `p`, and provided that there is bumping to be done.

        The row `r` is modified in place if bumping occurs. The bumped-out
        entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleHecke
            sage: from bisect import bisect_right
            sage: p, q, r =  [], [], [3,3,8,8,8,9]
            sage: j, ir = 8, 1
            sage: j1 = RuleHecke().insertion(j, ir, r, p)
            sage: j1 == r[bisect_right(r, j)]
            True
        """
    def reverse_insertion(self, i, x, row, p):
        """
        Reverse bump the row ``row`` of the current insertion tableau
        ``p`` with the number ``x``, provided that ``row`` is the
        `i`-th row of `p`.

        The row ``row`` is modified in place. The bumped-out entry
        is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleHecke
            sage: from bisect import bisect_left
            sage: r =  [2,3,3,4,8,9]
            sage: x, i, p = 9, 1, [1, 2]
            sage: x1 = RuleHecke().reverse_insertion(i, x, r, p)
            sage: x1 == r[bisect_left(r,x) - 1]
            True
        """

class RuleDualRSK(Rule):
    """
    Rule for dual RSK insertion.

    Dual RSK insertion differs from classical RSK insertion in the
    following ways:

    * The input (in terms of biwords) is no longer an arbitrary biword,
      but rather a strict biword (i.e., a pair of two lists
      `[a_1, a_2, \\ldots, a_n]` and `[b_1, b_2, \\ldots, b_n]` that
      satisfy the strict inequalities
      `(a_1, b_1) < (a_2, b_2) < \\cdots < (a_n, b_n)` in
      lexicographic order).
      In terms of matrices, this means that the input is not an
      arbitrary matrix with nonnegative integer entries, but rather
      a `\\{0, 1\\}`-matrix (i.e., a matrix whose entries are `0`'s
      and `1`'s).

    * The output still consists of two tableaux `(P, Q)` of equal
      shapes, but rather than both of them being semistandard, now
      `P` is row-strict (i.e., its transpose is semistandard) while
      `Q` is semistandard.

    * The main difference is in the way bumping works. Namely,
      when a number `k_i` is inserted into the `i`-th row of `P`,
      it bumps out the first integer greater **or equal to** `k_i`
      in this row (rather than greater than `k_i`).

    The RSK and dual RSK algorithms agree for permutation matrices.

    For more information, see Chapter 7, Section 14 in [Sta-EC2]_
    (where dual RSK is called `\\mathrm{RSK}^{\\ast}`) or the third
    solution to Exercise 2.7.12(a) in [GR2018v5sol]_.

    EXAMPLES::

        sage: RSK([3,3,2,4,1], insertion=RSK.rules.dualRSK)
        [[[1, 4], [2], [3], [3]], [[1, 4], [2], [3], [5]]]
        sage: RSK(Word([3,3,2,4,1]), insertion=RSK.rules.dualRSK)
        [[[1, 4], [2], [3], [3]], [[1, 4], [2], [3], [5]]]
        sage: RSK(Word([2,3,3,2,1,3,2,3]), insertion=RSK.rules.dualRSK)
        [[[1, 2, 3], [2, 3], [2, 3], [3]], [[1, 2, 8], [3, 6], [4, 7], [5]]]

    Using dual RSK insertion with a strict biword::

        sage: RSK([1,1,2,4,4,5],[2,4,1,1,3,2], insertion=RSK.rules.dualRSK)
        [[[1, 2], [1, 3], [2, 4]], [[1, 1], [2, 4], [4, 5]]]
        sage: RSK([1,1,2,3,3,4,5],[1,3,2,1,3,3,2], insertion=RSK.rules.dualRSK)
        [[[1, 2, 3], [1, 2], [3], [3]], [[1, 1, 3], [2, 4], [3], [5]]]
        sage: RSK([1, 2, 2, 2], [2, 1, 2, 4], insertion=RSK.rules.dualRSK)
        [[[1, 2, 4], [2]], [[1, 2, 2], [2]]]
        sage: RSK(Word([1,1,3,4,4]), [1,4,2,1,3], insertion=RSK.rules.dualRSK)
        [[[1, 2, 3], [1], [4]], [[1, 1, 4], [3], [4]]]
        sage: RSK([1,3,3,4,4], Word([6,1,2,1,7]), insertion=RSK.rules.dualRSK)
        [[[1, 2, 7], [1], [6]], [[1, 3, 4], [3], [4]]]

    Using dual RSK insertion with a `\\{0, 1\\}`-matrix::

        sage: RSK(matrix([[0,1],[1,1]]), insertion=RSK.rules.dualRSK)
        [[[1, 2], [2]], [[1, 2], [2]]]

    We can also give it something looking like a matrix::

        sage: RSK([[0,1],[1,1]], insertion=RSK.rules.dualRSK)
        [[[1, 2], [2]], [[1, 2], [2]]]

    Let us now call the inverse correspondence::

        sage: RSK_inverse(*RSK([1, 2, 2, 2], [2, 1, 2, 3],
        ....:         insertion=RSK.rules.dualRSK),insertion=RSK.rules.dualRSK)
        [[1, 2, 2, 2], [2, 1, 2, 3]]
        sage: P,Q = RSK([1, 2, 2, 2], [2, 1, 2, 3],insertion=RSK.rules.dualRSK)
        sage: RSK_inverse(P, Q, insertion=RSK.rules.dualRSK)
        [[1, 2, 2, 2], [2, 1, 2, 3]]

    When applied to two standard tableaux, reverse dual RSK
    insertion behaves identically to the usual reverse RSK insertion::

        sage: t1 = Tableau([[1, 2, 5], [3], [4]])
        sage: t2 = Tableau([[1, 2, 3], [4], [5]])
        sage: RSK_inverse(t1, t2, insertion=RSK.rules.dualRSK)
        [[1, 2, 3, 4, 5], [1, 4, 5, 3, 2]]
        sage: RSK_inverse(t1, t2, 'word', insertion=RSK.rules.dualRSK)
        word: 14532
        sage: RSK_inverse(t1, t2, 'matrix', insertion=RSK.rules.dualRSK)
        [1 0 0 0 0]
        [0 0 0 1 0]
        [0 0 0 0 1]
        [0 0 1 0 0]
        [0 1 0 0 0]
        sage: RSK_inverse(t1, t2, 'permutation', insertion=RSK.rules.dualRSK)
        [1, 4, 5, 3, 2]
        sage: RSK_inverse(t1, t1, 'permutation', insertion=RSK.rules.dualRSK)
        [1, 4, 3, 2, 5]
        sage: RSK_inverse(t2, t2, 'permutation', insertion=RSK.rules.dualRSK)
        [1, 2, 5, 4, 3]
        sage: RSK_inverse(t2, t1, 'permutation', insertion=RSK.rules.dualRSK)
        [1, 5, 4, 2, 3]

    Let us check that forward and backward dual RSK are mutually
    inverse when the first tableau is merely transpose semistandard::

        sage: p = Tableau([[1,2,2],[1]]); q = Tableau([[1,2,4],[3]])
        sage: ret = RSK_inverse(p, q, insertion=RSK.rules.dualRSK); ret
        [[1, 2, 3, 4], [1, 2, 1, 2]]
        sage: RSK_inverse(p, q, 'word', insertion=RSK.rules.dualRSK)
        word: 1212

    In general for dual RSK::

        sage: p = Tableau([[1,1,2],[1]]); q = Tableau([[1,3,3],[2]])
        sage: RSK_inverse(p, q, insertion=RSK.rules.dualRSK)
        [[1, 2, 3, 3], [1, 1, 1, 2]]
        sage: RSK_inverse(p, q, 'matrix', insertion=RSK.rules.dualRSK)
        [1 0]
        [1 0]
        [1 1]

    TESTS:

    Empty objects::

        sage: RSK(Permutation([]), insertion=RSK.rules.dualRSK)
        [[], []]
        sage: RSK(Word([]), insertion=RSK.rules.dualRSK)
        [[], []]
        sage: RSK(matrix([[]]), insertion=RSK.rules.dualRSK)
        [[], []]
        sage: RSK([], [], insertion=RSK.rules.dualRSK)
        [[], []]
        sage: RSK([[]], insertion=RSK.rules.dualRSK)
        [[], []]

    Check that :func:`RSK_inverse` is the inverse of :func:`RSK` on the
    different types of inputs/outputs::

        sage: RSK_inverse(Tableau([]), Tableau([]),
        ....:                insertion=RSK.rules.dualRSK)
        [[], []]
        sage: f = lambda p: RSK_inverse(*RSK(p, insertion=RSK.rules.dualRSK),
        ....:                output='permutation', insertion=RSK.rules.dualRSK)
        sage: all(p == f(p) for n in range(7) for p in Permutations(n))
        True
        sage: all(RSK_inverse(*RSK(w, insertion=RSK.rules.dualRSK),
        ....:                 output='word', insertion=RSK.rules.dualRSK) == w
        ....:     for n in range(4) for w in Words(5, n))
        True
        sage: from sage.combinat.integer_matrices import IntegerMatrices
        sage: M = IntegerMatrices([1,2,2,1], [3,1,1,1]) #this is probably wrong
        sage: all(RSK_inverse(*RSK(m, insertion=RSK.rules.dualRSK),
        ....:                output='matrix', insertion=RSK.rules.dualRSK) == m
        ....:     for m in M if all(x in [0, 1] for x in m))
        True

        sage: n = ZZ.random_element(200)
        sage: p = Permutations(n).random_element()
        sage: True if p == f(p) else p
        True

    Checking that the tableaux should be of same shape::

        sage: RSK_inverse(Tableau([[1,2,3]]), Tableau([[1,2]]),
        ....:                          insertion=RSK.rules.dualRSK)
        Traceback (most recent call last):
        ...
        ValueError: p(=[[1, 2, 3]]) and q(=[[1, 2]]) must have the same shape
    """
    def to_pairs(self, obj1=None, obj2=None, check: bool = True):
        '''
        Given a valid input for the dual RSK algorithm, such as
        two `n`-tuples ``obj1`` `= [a_1, a_2, \\ldots, a_n]`
        and ``obj2`` `= [b_1, b_2, \\ldots, b_n]` forming a strict
        biword (i.e., satisfying `a_1 \\leq a_2 \\leq \\cdots \\leq a_n`,
        and if `a_i = a_{i+1}`, then `b_i < b_{i+1}`) or a
        `\\{0, 1\\}`-matrix ("rook placement"), or a single word, return
        the array `[(a_1, b_1), (a_2, b_2), \\ldots, (a_n, b_n)]`.

        INPUT:

        - ``obj1``, ``obj2`` -- anything representing a strict biword
          (see the doc of :meth:`forward_rule` for the
          encodings accepted)

        - ``check`` -- boolean (default: ``True``); whether to check
          that ``obj1`` and ``obj2`` actually define a valid
          strict biword

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleDualRSK
            sage: list(RuleDualRSK().to_pairs([1, 2, 2, 2], [2, 1, 2, 3]))
            [(1, 2), (2, 1), (2, 2), (2, 3)]
            sage: RuleDualRSK().to_pairs([1, 2, 2, 2], [1, 2, 3, 3])
            Traceback (most recent call last):
            ...
            ValueError: invalid strict biword
            sage: m = Matrix(ZZ, 3, 2, [0,1,1,1,0,1]) ; m
            [0 1]
            [1 1]
            [0 1]
            sage: list(RuleDualRSK().to_pairs(m))
            [(1, 2), (2, 1), (2, 2), (3, 2)]
            sage: m = Matrix(ZZ, 3, 2, [0,1,1,0,0,2]) ; m
            [0 1]
            [1 0]
            [0 2]
            sage: RuleDualRSK().to_pairs(m)
            Traceback (most recent call last):
            ...
            ValueError: dual RSK requires a {0, 1}-matrix
        '''
    def insertion(self, j, r):
        """
        Insert the letter ``j`` from the second row of the biword
        into the row `r` using dual RSK insertion, if there is
        bumping to be done.

        The row `r` is modified in place if bumping occurs. The bumped-out
        entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleDualRSK
            sage: r = [1, 3, 4, 5]
            sage: j = RuleDualRSK().insertion(4, r); j
            4
            sage: r
            [1, 3, 4, 5]
            sage: r = [1, 2, 3, 6, 7]
            sage: j = RuleDualRSK().insertion(4, r); j
            6
            sage: r
            [1, 2, 3, 4, 7]
            sage: r = [1, 3]
            sage: j = RuleDualRSK().insertion(4, r); j is None
            True
            sage: r
            [1, 3]
        """
    def reverse_insertion(self, x, row):
        """
        Reverse bump the row ``row`` of the current insertion tableau
        with the number ``x`` using dual RSK insertion.

        The row ``row`` is modified in place. The bumped-out entry
        is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleDualRSK
            sage: r = [1, 2, 4, 6, 7]
            sage: x = RuleDualRSK().reverse_insertion(6, r); r
            [1, 2, 4, 6, 7]
            sage: x
            6
            sage: r = [1, 2, 4, 5, 7]
            sage: x = RuleDualRSK().reverse_insertion(6, r); r
            [1, 2, 4, 6, 7]
            sage: x
            5
        """

class RuleCoRSK(RuleRSK):
    """
    Rule for coRSK insertion.

    CoRSK insertion differs from classical RSK insertion in the
    following ways:

    * The input (in terms of biwords) is no longer a biword,
      but rather a strict cobiword -- i.e., a pair of two lists
      `[a_1, a_2, \\ldots, a_n]` and `[b_1, b_2, \\ldots, b_n]` that
      satisfy the strict inequalities
      `(a_1, b_1) \\widetilde{<} (a_2, b_2) \\widetilde{<} \\cdots
      \\widetilde{<} (a_n, b_n)`, where
      the binary relation `\\widetilde{<}` on pairs of integers
      is defined by having `(u_1, v_1) \\widetilde{<} (u_2, v_2)`
      if and only if either `u_1 < u_2` or (`u_1 = u_2` and
      `v_1 > v_2`).
      In terms of matrices, this means that the input is not an
      arbitrary matrix with nonnegative integer entries, but rather
      a `\\{0, 1\\}`-matrix (i.e., a matrix whose entries are `0`'s
      and `1`'s).

    * The output still consists of two tableaux `(P, Q)` of equal
      shapes, but rather than both of them being semistandard, now
      `Q` is row-strict (i.e., its transpose is semistandard) while
      `P` is semistandard.

    Bumping proceeds in the same way as for RSK insertion.

    The RSK and coRSK algorithms agree for permutation matrices.

    For more information, see Section A.4 in [Ful1997]_ (specifically,
    construction (1d)) or the second solution to Exercise 2.7.12(a) in
    [GR2018v5sol]_.

    EXAMPLES::

        sage: RSK([1,2,5,3,1], insertion = RSK.rules.coRSK)
        [[[1, 1, 3], [2], [5]], [[1, 2, 3], [4], [5]]]
        sage: RSK(Word([2,3,3,2,1,3,2,3]), insertion = RSK.rules.coRSK)
        [[[1, 2, 2, 3, 3], [2, 3], [3]], [[1, 2, 3, 6, 8], [4, 7], [5]]]
        sage: RSK(Word([3,3,2,4,1]), insertion = RSK.rules.coRSK)
        [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]
        sage: from sage.combinat.rsk import to_matrix
        sage: RSK(to_matrix([1, 1, 3, 3, 4], [3, 2, 2, 1, 3]), insertion = RSK.rules.coRSK)
        [[[1, 2, 3], [2], [3]], [[1, 3, 4], [1], [3]]]

    Using coRSK insertion with a `\\{0, 1\\}`-matrix::

        sage: RSK(matrix([[0,1],[1,0]]), insertion = RSK.rules.coRSK)
        [[[1], [2]], [[1], [2]]]

    We can also give it something looking like a matrix::

        sage: RSK([[0,1],[1,0]], insertion = RSK.rules.coRSK)
        [[[1], [2]], [[1], [2]]]

    We can also use the inverse correspondence::

        sage: RSK_inverse(*RSK([1, 2, 2, 2], [2, 3, 2, 1],
        ....:         insertion=RSK.rules.coRSK),insertion=RSK.rules.coRSK)
        [[1, 2, 2, 2], [2, 3, 2, 1]]
        sage: P,Q = RSK([1, 2, 2, 2], [2, 3, 2, 1],insertion=RSK.rules.coRSK)
        sage: RSK_inverse(P, Q, insertion=RSK.rules.coRSK)
        [[1, 2, 2, 2], [2, 3, 2, 1]]

    When applied to two standard tableaux, backwards coRSK
    insertion behaves identically to the usual backwards RSK
    insertion::

        sage: t1 = Tableau([[1, 2, 5], [3], [4]])
        sage: t2 = Tableau([[1, 2, 3], [4], [5]])
        sage: RSK_inverse(t1, t2, insertion=RSK.rules.coRSK)
        [[1, 2, 3, 4, 5], [1, 4, 5, 3, 2]]
        sage: RSK_inverse(t1, t2, 'word', insertion=RSK.rules.coRSK)
        word: 14532
        sage: RSK_inverse(t1, t2, 'matrix', insertion=RSK.rules.coRSK)
        [1 0 0 0 0]
        [0 0 0 1 0]
        [0 0 0 0 1]
        [0 0 1 0 0]
        [0 1 0 0 0]
        sage: RSK_inverse(t1, t2, 'permutation', insertion=RSK.rules.coRSK)
        [1, 4, 5, 3, 2]
        sage: RSK_inverse(t1, t1, 'permutation', insertion=RSK.rules.coRSK)
        [1, 4, 3, 2, 5]
        sage: RSK_inverse(t2, t2, 'permutation', insertion=RSK.rules.coRSK)
        [1, 2, 5, 4, 3]
        sage: RSK_inverse(t2, t1, 'permutation', insertion=RSK.rules.coRSK)
        [1, 5, 4, 2, 3]

    For coRSK, the first tableau is semistandard while the second tableau
    is transpose semistandard::

        sage: p = Tableau([[1,2,2],[5]]); q = Tableau([[1,2,4],[3]])
        sage: ret = RSK_inverse(p, q, insertion=RSK.rules.coRSK); ret
        [[1, 2, 3, 4], [1, 5, 2, 2]]
        sage: RSK_inverse(p, q, 'word', insertion=RSK.rules.coRSK)
        word: 1522

    TESTS:

    Empty objects::

        sage: RSK(Permutation([]), insertion=RSK.rules.coRSK)
        [[], []]
        sage: RSK(Word([]), insertion=RSK.rules.coRSK)
        [[], []]
        sage: RSK(matrix([[]]), insertion=RSK.rules.coRSK)
        [[], []]
        sage: RSK([], [], insertion=RSK.rules.coRSK)
        [[], []]
        sage: RSK([[]], insertion=RSK.rules.coRSK)
        [[], []]

    Check that :func:`RSK_inverse` is the inverse of :func:`RSK` on the
    different types of inputs/outputs::

        sage: RSK_inverse(Tableau([]), Tableau([]),
        ....:                insertion=RSK.rules.coRSK)
        [[], []]
        sage: f = lambda p: RSK_inverse(*RSK(p, insertion=RSK.rules.coRSK),
        ....:                output='permutation', insertion=RSK.rules.coRSK)
        sage: all(p == f(p) for n in range(7) for p in Permutations(n))
        True
        sage: all(RSK_inverse(*RSK(w, insertion=RSK.rules.coRSK),
        ....:                 output='word', insertion=RSK.rules.coRSK) == w
        ....:     for n in range(4) for w in Words(5, n))
        True
        sage: from sage.combinat.integer_matrices import IntegerMatrices
        sage: M = IntegerMatrices([1,2,2,1], [3,1,1,1])
        sage: all(RSK_inverse(*RSK(m, insertion=RSK.rules.coRSK),
        ....:                output='matrix', insertion=RSK.rules.coRSK) == m
        ....:     for m in M if all(x in [0, 1] for x in m))
        True

        sage: n = ZZ.random_element(200)
        sage: p = Permutations(n).random_element()
        sage: True if p == f(p) else p
        True

    Checking that the tableaux should be of same shape::

        sage: RSK_inverse(Tableau([[1,2,3]]), Tableau([[1,2]]),
        ....:                          insertion=RSK.rules.dualRSK)
        Traceback (most recent call last):
        ...
        ValueError: p(=[[1, 2, 3]]) and q(=[[1, 2]]) must have the same shape

    Checking that the biword is a strict cobiword::

        sage: RSK([1,2,4,3], [1,2,3,4], insertion=RSK.rules.coRSK)
        Traceback (most recent call last):
        ...
        ValueError: invalid strict cobiword
        sage: RSK([1,2,3,3], [1,2,3,4], insertion=RSK.rules.coRSK)
        Traceback (most recent call last):
        ...
        ValueError: invalid strict cobiword
        sage: RSK([1,2,3,3], [1,2,3,3], insertion=RSK.rules.coRSK)
        Traceback (most recent call last):
        ...
        ValueError: invalid strict cobiword
    """
    def to_pairs(self, obj1=None, obj2=None, check: bool = True):
        '''
        Given a valid input for the coRSK algorithm, such as
        two `n`-tuples ``obj1`` `= [a_1, a_2, \\ldots, a_n]`
        and ``obj2`` `= [b_1, b_2, \\ldots, b_n]` forming a
        strict cobiword (i.e., satisfying
        `a_1 \\leq a_2 \\leq \\cdots \\leq a_n`, and if
        `a_i = a_{i+1}`, then `b_i > b_{i+1}`),
        or a `\\{0, 1\\}`-matrix ("rook placement"), or a
        single word, return the array
        `[(a_1, b_1), (a_2, b_2), \\ldots, (a_n, b_n)]`.

        INPUT:

        - ``obj1``, ``obj2`` -- anything representing a strict
          cobiword (see the doc of :meth:`forward_rule` for
          the encodings accepted)

        - ``check`` -- boolean (default: ``True``); whether to check
          that ``obj1`` and ``obj2`` actually define a valid
          strict cobiword

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleCoRSK
            sage: list(RuleCoRSK().to_pairs([1, 2, 2, 2], [2, 3, 2, 1]))
            [(1, 2), (2, 3), (2, 2), (2, 1)]
            sage: RuleCoRSK().to_pairs([1, 2, 2, 2], [1, 2, 3, 3])
            Traceback (most recent call last):
            ...
            ValueError: invalid strict cobiword
            sage: m = Matrix(ZZ, 3, 2, [0,1,1,1,0,1]) ; m
            [0 1]
            [1 1]
            [0 1]
            sage: list(RuleCoRSK().to_pairs(m))
            [(1, 2), (2, 2), (2, 1), (3, 2)]
            sage: m = Matrix(ZZ, 3, 2, [0,1,1,0,0,2]) ; m
            [0 1]
            [1 0]
            [0 2]
            sage: RuleCoRSK().to_pairs(m)
            Traceback (most recent call last):
            ...
            ValueError: coRSK requires a {0, 1}-matrix
        '''
    def backward_rule(self, p, q, output):
        """
        Return the strict cobiword obtained by applying reverse
        coRSK insertion to a pair of tableaux ``(p, q)``.

        INPUT:

        - ``p``, ``q`` -- two tableaux of the same shape

        - ``output`` -- (default: ``'array'``) if ``q`` is row-strict:

          - ``'array'`` -- as a two-line array (i.e. strict cobiword)
          - ``'matrix'`` -- as a `\\{0, 1\\}`-matrix

          and if ``q`` is standard, we can have the output:

          - ``'word'`` -- as a word

          and additionally if ``p`` is standard, we can also have the output:

          - ``'permutation'`` -- as a permutation

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleCoRSK
            sage: t1 = Tableau([[1, 1, 2], [2, 3], [4]])
            sage: t2 = Tableau([[1, 4, 5], [1, 4], [2]])
            sage: RuleCoRSK().backward_rule(t1, t2, 'array')
            [[1, 1, 2, 4, 4, 5], [4, 2, 1, 3, 1, 2]]
        """

class RuleSuperRSK(RuleRSK):
    '''
    Rule for super RSK insertion.

    Super RSK is based on `\\epsilon`-insertion, a combination of
    row and column classical RSK insertion.

    Super RSK insertion differs from the classical RSK insertion in the
    following ways:

    * The input (in terms of biwords) is no longer an arbitrary biword,
      but rather a restricted super biword (i.e., a pair of two lists
      `[a_1, a_2, \\ldots, a_n]` and `[b_1, b_2, \\ldots, b_n]` that
      contains entries with even and odd parity and pairs with mixed
      parity entries do not repeat).

    * The output still consists of two tableaux `(P, Q)` of equal
      shapes, but rather than both of them being semistandard, now
      they are semistandard super tableaux.

    * The main difference is in the way bumping works. Instead of having
      only row bumping super RSK uses `\\epsilon`-insertion, a combination
      of classical RSK bumping along the rows and a dual RSK like bumping
      (i.e. when a number `k_i` is inserted into the `i`-th row of `P`, it
      bumps out the first integer greater **or equal to** `k_i` in the column)
      along the column.

    EXAMPLES::

        sage: RSK([1], [1], insertion=\'superRSK\')
        [[[1]], [[1]]]
        sage: RSK([1, 2], [1, 3], insertion=\'superRSK\')
        [[[1, 3]], [[1, 2]]]
        sage: RSK([1, 2, 3], [1, 3, "3p"], insertion=\'superRSK\')
        [[[1, 3], [3\']], [[1, 2], [3]]]
        sage: RSK([1, 3, "3p", "2p"], insertion=\'superRSK\')
        [[[1, 3\', 3], [2\']], [[1\', 1, 2\'], [2]]]
        sage: RSK(["1p", "2p", 2, 2, "3p", "3p", 3, 3],
        ....:     ["1p", 1, "2p", 2, "3p", "3p", "3p", 3], insertion=\'superRSK\')
        [[[1\', 2, 3\', 3], [1, 3\'], [2\'], [3\']], [[1\', 2, 3\', 3], [2\', 3\'], [2], [3]]]
        sage: P = SemistandardSuperTableau([[1, \'3p\', 3], [\'2p\']])
        sage: Q = SemistandardSuperTableau([[\'1p\', 1, \'2p\'], [2]])
        sage: RSK_inverse(P, Q, insertion=RSK.rules.superRSK)
        [[1\', 1, 2\', 2], [1, 3, 3\', 2\']]

    We apply super RSK on Example 5.1 in [Muth2019]_::

        sage: P,Q = RSK(["1p", "2p", 2, 2, "3p", "3p", 3, 3],
        ....:           ["3p", 1, 2, 3, "3p", "3p", "2p", "1p"], insertion=\'superRSK\')
        sage: (P, Q)
        ([[1\', 2\', 3\', 3], [1, 2, 3\'], [3\']], [[1\', 2, 2, 3\'], [2\', 3, 3], [3\']])
        sage: ascii_art((P, Q))
        (  1\' 2\' 3\'  3   1\'  2  2 3\' )
        (   1  2 3\'      2\'  3  3    )
        (  3\'         ,  3\'          )
        sage: RSK_inverse(P, Q, insertion=RSK.rules.superRSK)
        [[1\', 2\', 2, 2, 3\', 3\', 3, 3], [3\', 1, 2, 3, 3\', 3\', 2\', 1\']]

    Example 6.1 in [Muth2019]_::

        sage: P,Q = RSK(["1p", "2p", 2, 2, "3p", "3p", 3, 3],
        ....:           ["3p", 1, 2, 3, "3p", "3p", "2p", "1p"], insertion=\'superRSK\')
        sage: ascii_art((P, Q))
        (  1\' 2\' 3\'  3   1\'  2  2 3\' )
        (   1  2 3\'      2\'  3  3    )
        (  3\'         ,  3\'          )
        sage: RSK_inverse(P, Q, insertion=RSK.rules.superRSK)
        [[1\', 2\', 2, 2, 3\', 3\', 3, 3], [3\', 1, 2, 3, 3\', 3\', 2\', 1\']]

        sage: P,Q = RSK(["1p", 1, "2p", 2, "3p", "3p", "3p", 3],
        ....:           [3, "2p", 3, 2, "3p", "3p", "1p", 2], insertion=\'superRSK\')
        sage: ascii_art((P, Q))
        (  1\'  2  2 3\'   1\' 2\' 3\'  3 )
        (  2\'  3  3       1  2 3\'    )
        (  3\'         ,  3\'          )
        sage: RSK_inverse(P, Q, insertion=RSK.rules.superRSK)
        [[1\', 1, 2\', 2, 3\', 3\', 3\', 3], [3, 2\', 3, 2, 3\', 3\', 1\', 2]]

    Let us now call the inverse correspondence::

        sage: P, Q = RSK([1, 2, 2, 2], [2, 1, 2, 3],
        ....:            insertion=RSK.rules.superRSK)
        sage: RSK_inverse(P, Q, insertion=RSK.rules.superRSK)
        [[1, 2, 2, 2], [2, 1, 2, 3]]

    When applied to two tableaux with only even parity elements, reverse super
    RSK insertion behaves identically to the usual reversel RSK insertion::

        sage: t1 = Tableau([[1, 2, 5], [3], [4]])
        sage: t2 = Tableau([[1, 2, 3], [4], [5]])
        sage: RSK_inverse(t1, t2, insertion=RSK.rules.RSK)
        [[1, 2, 3, 4, 5], [1, 4, 5, 3, 2]]
        sage: t1 = SemistandardSuperTableau([[1, 2, 5], [3], [4]])
        sage: t2 = SemistandardSuperTableau([[1, 2, 3], [4], [5]])
        sage: RSK_inverse(t1, t2, insertion=RSK.rules.superRSK)
        [[1, 2, 3, 4, 5], [1, 4, 5, 3, 2]]

    TESTS:

    Empty objects::

        sage: RSK(Word([]), insertion=RSK.rules.superRSK)
        [[], []]
        sage: RSK([], [], insertion=RSK.rules.superRSK)
        [[], []]

    Check that :func:`RSK_inverse` is the inverse of :func:`RSK` on the
    different types of inputs/outputs::

        sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
        sage: RSK_inverse(SemistandardSuperTableau([]),
        ....:             SemistandardSuperTableau([]), insertion=RSK.rules.superRSK)
        [[], []]
        sage: f = lambda p: RSK_inverse(*RSK(p, insertion=RSK.rules.superRSK),
        ....:                           insertion=RSK.rules.superRSK)
        sage: all(p == f(p)[1] for n in range(5) for p in Permutations(n))
        True

        sage: SST = StandardSuperTableaux([3,2,1])
        sage: f = lambda P, Q: RSK(*RSK_inverse(P, Q, insertion=RSK.rules.superRSK),
        ....:                      insertion=RSK.rules.superRSK)
        sage: all([P, Q] == f(P, Q) for n in range(7) for la in Partitions(n)
        ....:     for P in StandardSuperTableaux(la) for Q in StandardSuperTableaux(la))
        True

    Checking that tableaux should be of same shape::

        sage: RSK_inverse(SemistandardSuperTableau([[1, 2, 3]]),
        ....:             SemistandardSuperTableau([[1, 2]]),
        ....:             insertion=RSK.rules.superRSK)
        Traceback (most recent call last):
        ...
        ValueError: p(=[[1, 2, 3]]) and q(=[[1, 2]]) must have the same shape
    '''
    def to_pairs(self, obj1=None, obj2=None, check: bool = True):
        """
        Given a valid input for the super RSK algorithm, such as
        two `n`-tuples ``obj1`` `= [a_1, a_2, \\ldots, a_n]`
        and ``obj2`` `= [b_1, b_2, \\ldots, b_n]` forming a restricted
        super biword (i.e., entries with even and odd parity and no
        repetition of corresponding pairs with mixed parity entries)
        return the array `[(a_1, b_1), (a_2, b_2), \\ldots, (a_n, b_n)]`.

        INPUT:

        - ``obj1``, ``obj2`` -- anything representing a restricted super biword
          (see the doc of :meth:`forward_rule` for the
          encodings accepted)

        - ``check`` -- boolean (default: ``True``); whether to check
          that ``obj1`` and ``obj2`` actually define a valid
          restricted super biword

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleSuperRSK
            sage: list(RuleSuperRSK().to_pairs([2, '1p', 1],[1, 1, '1p']))
            [(2, 1), (1', 1), (1, 1')]
            sage: list(RuleSuperRSK().to_pairs([1, '1p', '2p']))
            [(1', 1), (1, 1'), (2', 2')]
            sage: list(RuleSuperRSK().to_pairs([1, 1], ['1p', '1p']))
            Traceback (most recent call last):
            ...
            ValueError: invalid restricted superbiword
        """
    def forward_rule(self, obj1, obj2, check_standard: bool = False, check: bool = True):
        """
        Return a pair of tableaux obtained by applying forward
        insertion to the restricted super biword ``[obj1, obj2]``.

        INPUT:

        - ``obj1``, ``obj2`` -- can be one of the following ways to
          represent a generalized permutation (or, equivalently,
          biword):

          - two lists ``obj1`` and ``obj2`` of equal length,
            to be interpreted as the top row and the bottom row of
            the biword

          - a word ``obj1`` in an ordered alphabet, to be
            interpreted as the bottom row of the biword (in this
            case, ``obj2`` is ``None``; the top row of the biword
            is understood to be `(1, 2, \\ldots, n)` by default)

          - any object ``obj1`` which has a method ``_rsk_iter()``,
            as long as this method returns an iterator yielding
            pairs of numbers, which then are interpreted as top
            entries and bottom entries in the biword (in this case,
            ``obj2`` is ``None``)

        - ``check_standard`` -- boolean (default: ``False``); check if either
          of the resulting tableaux is a standard super tableau, and if so,
          typecast it as such

        - ``check`` -- boolean (default: ``True``); whether to check
          that ``obj1`` and ``obj2`` actually define a valid
          restricted super biword

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleSuperRSK
            sage: p, q = RuleSuperRSK().forward_rule([1, 2], [1, 3]); p
            [[1, 3]]
            sage: q
            [[1, 2]]
            sage: isinstance(p, SemistandardSuperTableau)
            True
            sage: isinstance(q, SemistandardSuperTableau)
            True
        """
    def insertion(self, j, r, epsilon: int = 0):
        """
        Insert the letter ``j`` from the second row of the biword
        into the row ``r`` using dual RSK insertion or classical
        Schensted insertion depending on the value of ``epsilon``,
        if there is bumping to be done.

        The row `r` is modified in place if bumping occurs. The bumped-out
        entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleSuperRSK
            sage: from bisect import bisect_left, bisect_right
            sage: r = [1, 3, 3, 3, 4]
            sage: j = 3
            sage: j, y_pos = RuleSuperRSK().insertion(j, r, epsilon=0); r
            [1, 3, 3, 3, 3]
            sage: j
            4
            sage: y_pos
            4
            sage: r = [1, 3, 3, 3, 4]
            sage: j = 3
            sage: j, y_pos = RuleSuperRSK().insertion(j, r, epsilon=1); r
            [1, 3, 3, 3, 4]
            sage: j
            3
            sage: y_pos
            1
        """
    def backward_rule(self, p, q, output: str = 'array'):
        """
        Return the restricted super biword obtained by applying reverse
        super RSK insertion to a pair of tableaux ``(p, q)``.

        INPUT:

        - ``p``, ``q`` -- two tableaux of the same shape

        - ``output`` -- (default: ``'array'``) if ``q`` is row-strict:

          - ``'array'`` -- as a two-line array (i.e. restricted super biword)

          and if ``q`` is standard, we can have the output:

          - ``'word'`` -- as a word

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleSuperRSK
            sage: t1 = SemistandardSuperTableau([['1p', '3p', '4p'], [2], [3]])
            sage: t2 = SemistandardSuperTableau([[1, 2, 4], [3], [5]])
            sage: RuleSuperRSK().backward_rule(t1, t2, 'array')
            [[1, 2, 3, 4, 5], [4', 3, 3', 2, 1']]
            sage: t1 = SemistandardSuperTableau([[1, 3], ['3p']])
            sage: t2 = SemistandardSuperTableau([[1, 2], [3]])
            sage: RuleSuperRSK().backward_rule(t1, t2, 'array')
            [[1, 2, 3], [1, 3, 3']]
        """
    def reverse_insertion(self, x, row, epsilon: int = 0):
        """
        Reverse bump the row ``row`` of the current insertion tableau
        with the number ``x`` using dual RSK insertion or classical
        Schensted insertion depending on the value of `epsilon`.

        The row ``row`` is modified in place. The bumped-out entry
        is returned along with the bumped position.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleSuperRSK
            sage: from bisect import bisect_left, bisect_right
            sage: r = [1, 3, 3, 3, 4]
            sage: j = 2
            sage: j, y = RuleSuperRSK().reverse_insertion(j, r, epsilon=0); r
            [2, 3, 3, 3, 4]
            sage: j
            1
            sage: y
            0
            sage: r = [1, 3, 3, 3, 4]
            sage: j = 3
            sage: j, y = RuleSuperRSK().reverse_insertion(j, r, epsilon=0); r
            [3, 3, 3, 3, 4]
            sage: j
            1
            sage: y
            0
            sage: r = [1, 3, 3, 3, 4]
            sage: j = (3)
            sage: j, y = RuleSuperRSK().reverse_insertion(j, r, epsilon=1); r
            [1, 3, 3, 3, 4]
            sage: j
            3
            sage: y
            3
        """

class RuleStar(Rule):
    """
    Rule for `\\star`-insertion.

    The `\\star`-insertion is similar to the classical RSK algorithm
    and is defined in [MPPS2020]_. The bottom row of the increasing
    Hecke biword is a word in the 0-Hecke monoid that is fully
    commutative. When inserting a letter `x` into a row `R`, there
    are three cases:

    - Case 1: If `R` is empty or `x > \\max(R)`, append `x` to row `R`
      and terminate.

    - Case 2: Otherwise if `x` is not in `R`, locate the smallest `y` in `R`
      with `y > x`. Bump `y` with `x` and insert `y` into the next row.

    - Case 3: Otherwise, if `x` is in `R`, locate the smallest `y` in `R` with
      `y \\leq x` and interval `[y,x]` contained in `R`. Row `R` remains
      unchanged and `y` is to be inserted into the next row.

    The `\\star`-insertion returns a pair consisting a conjugate of a
    semistandard tableau and a semistandard tableau. It is a bijection from the
    collection of all increasing Hecke biwords whose bottom row is a fully
    commutative word to pairs (P, Q) of tableaux of the same shape such that
    P is conjugate semistandard, Q is semistandard and the row reading word of
    P is fully commutative [MPPS2020]_.

    EXAMPLES:

    As an example of `\\star`-insertion, we reproduce Example 28 in [MPPS2020]_::

        sage: from sage.combinat.rsk import RuleStar
        sage: p,q = RuleStar().forward_rule([1,1,2,2,4,4], [1,3,2,4,2,4])
        sage: ascii_art(p, q)
          1  2  4  1  1  2
          1  4     2  4
          3        4
        sage: line1,line2 = RuleStar().backward_rule(p, q)
        sage: line1,line2
        ([1, 1, 2, 2, 4, 4], [1, 3, 2, 4, 2, 4])
        sage: RSK_inverse(p, q, output='DecreasingHeckeFactorization', insertion='Star')
        (4, 2)()(4, 2)(3, 1)

        sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
        sage: h = DecreasingHeckeFactorization([[4, 2], [], [4, 2], [3, 1]])
        sage: RSK_inverse(*RSK(h,insertion='Star'),insertion='Star',
        ....:             output='DecreasingHeckeFactorization')
        (4, 2)()(4, 2)(3, 1)
        sage: p,q = RSK(h, insertion='Star')
        sage: ascii_art(p, q)
        1  2  4  1  1  2
        1  4     2  4
        3        4
        sage: RSK_inverse(p, q, insertion='Star')
        [[1, 1, 2, 2, 4, 4], [1, 3, 2, 4, 2, 4]]
        sage: f = RSK_inverse(p, q, output='DecreasingHeckeFactorization', insertion='Star')
        sage: f == h
        True

    .. WARNING::

        When ``output`` is set to ``'DecreasingHeckeFactorization'``, the
        inverse of `\\star`-insertion of `(P,Q)` returns a decreasing
        factorization whose number of factors is the maximum entry of `Q`::

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: h1 = DecreasingHeckeFactorization([[],[3,1],[1]]); h1
            ()(3, 1)(1)
            sage: P,Q = RSK(h1, insertion='Star')
            sage: ascii_art(P, Q)
              1  3  1  2
              1     2
            sage: h2 = RSK_inverse(P, Q, insertion='Star',
            ....: output='DecreasingHeckeFactorization'); h2
            (3, 1)(1)

    TESTS:

    Check that :func:`RSK` is the inverse of :func:`RSK_inverse` for various
    outputs/inputs::

        sage: from sage.combinat.partition import Partitions_n
        sage: shapes = [shape for n in range(7) for shape in Partitions_n(n)]
        sage: row_reading = lambda T: [x for row in reversed(T) for x in row]
        sage: from sage.monoids.hecke_monoid import HeckeMonoid
        sage: H = HeckeMonoid(SymmetricGroup(4+1))
        sage: from sage.combinat import permutation
        sage: reduce = lambda w: permutation.from_reduced_word(H.from_reduced_word(w).reduced_word())
        sage: fc = lambda w: not reduce(w).has_pattern([3,2,1])
        sage: FC_tabs = [T for shape in shapes
        ....:                  for T in SemistandardTableaux(shape, max_entry=4)
        ....:                      if fc(row_reading(T.conjugate()))]
        sage: from random import sample
        sage: FC_tabs = sample(FC_tabs, 25)  # verify only a random subset
        sage: Checks = []
        sage: for T in FC_tabs:  # long time
        ....:    shape = T.shape().conjugate()
        ....:    P = T.conjugate()
        ....:    Checks += [all((P,Q) == tuple(RSK(*RSK_inverse(P, Q,
        ....:               insertion='Star', output='array'),
        ....:               insertion='Star'))
        ....:               for Q in SemistandardTableaux(shape, max_entry=5))]
        sage: all(Checks)
        True
        sage: Checks = []
        sage: for T in FC_tabs:  # long time
        ....:    shape = T.shape().conjugate()
        ....:    P = T.conjugate()
        ....:    Checks += [all((P,Q) == tuple(RSK(RSK_inverse(P, Q,
        ....:               insertion='Star', output='DecreasingHeckeFactorization'),
        ....:               insertion='Star'))
        ....:               for Q in SemistandardTableaux(shape, max_entry=5))]
        sage: all(Checks)
        True
        sage: Checks = []
        sage: for T in FC_tabs:
        ....:    shape = T.shape().conjugate()
        ....:    P = T.conjugate()
        ....:    for Q in StandardTableaux(shape, max_entry=5):
        ....:        Checks += [(P,Q) == tuple(RSK(RSK_inverse(P, Q,
        ....:                   insertion='Star', output='word'),
        ....:                   insertion='Star'))]
        sage: all(Checks)
        True

    Check that :func:`RSK_inverse` is the inverse of :func:`RSK` on arrays
    and words::

        sage: S = SymmetricGroup(3+1)
        sage: from sage.combinat import permutation
        sage: FC = [x
        ....:       for x in S
        ....:           if (not permutation.from_reduced_word(
        ....:           x.reduced_word()).has_pattern([3,2,1]) and
        ....:           x.reduced_word())]
        sage: Triples = [(w, factors, ex)
        ....:            for w in FC
        ....:                for factors in range(2, 5+1)
        ....:                    for ex in range(4)]
        sage: Checks = []
        sage: for t in Triples:
        ....:     B = crystals.FullyCommutativeStableGrothendieck(*t)
        ....:     Checks += [all(b.to_increasing_hecke_biword() ==
        ....:                RSK_inverse(*RSK(
        ....:                *b.to_increasing_hecke_biword(),
        ....:                insertion='Star'), insertion='Star')
        ....:                for b in B)]
        sage: all(Checks)
        True

        sage: from sage.monoids.hecke_monoid import HeckeMonoid
        sage: Checks = []
        sage: H = HeckeMonoid(SymmetricGroup(3+1))
        sage: reduce = lambda w: permutation.from_reduced_word(H.from_reduced_word(w).reduced_word())
        sage: fc = lambda w: not reduce(w).has_pattern([3,2,1])
        sage: words = [w for n in range(10) for w in Words(3, n) if fc(w)]
        sage: all([all(w == RSK_inverse(*RSK(w, insertion='Star'),
        ....:          insertion='Star', output='word') for w in words)])
        True
    """
    def forward_rule(self, obj1, obj2=None, check_braid: bool = True):
        """
        Return a pair of tableaux obtained by applying forward insertion
        to the increasing Hecke biword ``[obj1, obj2]``.

        INPUT:

        - ``obj1``, ``obj2`` -- can be one of the following ways to represent a
          biword (or, equivalently, an increasing 0-Hecke factorization) that
          is fully commutative:

          - two lists ``obj1`` and ``obj2`` of equal length, to be
            interpreted as the top row and the bottom row of the biword.

          - a word ``obj1`` in an ordered alphabet, to be interpreted as
            the bottom row of the biword (in this case, ``obj2`` is ``None``;
            the top row of the biword is understood to be `(1,2,\\ldots,n)`
            by default).

          - a DecreasingHeckeFactorization ``obj1``, the whose increasing
            Hecke biword will be interpreted as the bottom row; the top row is
            understood to be the indices of the factors for each letter in
            this biword.

        - ``check_braid`` -- boolean (default: ``True``); indicator to validate
          that input is associated to a fully commutative word in the 0-Hecke
          monoid, validation is performed if set to ``True``. Οtherwise, this
          validation is ignored.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleStar
            sage: p,q = RuleStar().forward_rule([1,1,2,3,3], [2,3,3,1,3]); p,q
            ([[1, 3], [2, 3], [2]], [[1, 1], [2, 3], [3]])
            sage: p,q = RuleStar().forward_rule([2,3,3,1,3]); p,q
            ([[1, 3], [2, 3], [2]], [[1, 2], [3, 5], [4]])
            sage: p,q = RSK([1,1,2,3,3], [2,3,3,1,3], insertion=RSK.rules.Star); p,q
            ([[1, 3], [2, 3], [2]], [[1, 1], [2, 3], [3]])

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: h = DecreasingHeckeFactorization([[3, 1], [3], [3, 2]])
            sage: p,q = RSK(h, insertion=RSK.rules.Star); p,q
            ([[1, 3], [2, 3], [2]], [[1, 1], [2, 3], [3]])

        TESTS:

        Empty objects::

            sage: from sage.combinat.rsk import RuleStar
            sage: p,q = RuleStar().forward_rule([]); p,q
            ([], [])

            sage: from sage.combinat.crystals.fully_commutative_stable_grothendieck import DecreasingHeckeFactorization
            sage: h = DecreasingHeckeFactorization([[],[]])
            sage: p,q = RuleStar().forward_rule(h); p,q
            ([], [])

        Invalid inputs::

            sage: p,q = RuleStar().forward_rule([1,1,2,3,3], [2,2,3,1,3])
            Traceback (most recent call last):
            ...
            ValueError: [1, 1, 2, 3, 3], [2, 2, 3, 1, 3] is not an increasing factorization
            sage: p,q = RuleStar().forward_rule([1,1,2,2,4,4], [1,3,2,4,1,3])
            Traceback (most recent call last):
            ...
            ValueError: the Star insertion is not defined for non-fully commutative words
        """
    def backward_rule(self, p, q, output: str = 'array'):
        """
        Return the increasing Hecke biword obtained by applying reverse
        `\\star`-insertion to a pair of tableaux ``(p, q)``.

        INPUT:

        - ``p``, ``q`` -- two tableaux of the same shape, where ``p`` is the
          conjugate of a semistandard tableau, whose reading word is fully
          commutative and ``q`` is a semistandard tableau.

        - ``output`` -- (default: ``'array'``) if ``q`` is semi-standard:

          - ``'array'`` -- as a two-line array (i.e. generalized permutation
            or biword) that is an increasing Hecke biword
          - ``'DecreasingHeckeFactorization'`` -- as a decreasing
            factorization in the 0-Hecke monoid

          and if ``q`` is standard:

          - ``'word'`` -- as a (possibly non-reduced) word in the 0-Hecke
            monoid

        .. WARNING::

            When output is 'DecreasingHeckeFactorization', the number of factors
            in the output is the largest number in ``obj1``.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleStar
            sage: p,q = RuleStar().forward_rule([1,1,2,2,4,4], [1,3,2,4,2,4])
            sage: ascii_art(p, q)
              1  2  4  1  1  2
              1  4     2  4
              3        4
            sage: line1,line2 = RuleStar().backward_rule(p, q); line1,line2
            ([1, 1, 2, 2, 4, 4], [1, 3, 2, 4, 2, 4])
            sage: RuleStar().backward_rule(p, q, output = 'DecreasingHeckeFactorization')
            (4, 2)()(4, 2)(3, 1)

        TESTS:

        Empty objects::

            sage: RuleStar().backward_rule(Tableau([]), Tableau([]))
            [[], []]
            sage: RuleStar().backward_rule(Tableau([]), Tableau([]), output='word')
            word:
            sage: RuleStar().backward_rule(Tableau([]), Tableau([]),output='DecreasingHeckeFactorization')
            ()
        """
    def insertion(self, b, r):
        """
        Insert the letter ``b`` from the second row of the biword into the row
        ``r`` using `\\star`-insertion defined in [MPPS2020]_.

        The row `r` is modified in place if bumping occurs and `b` is not in
        row `r`. The bumped-out entry, if it exists, is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleStar
            sage: RuleStar().insertion(3, [1,2,4,5])
            4
            sage: RuleStar().insertion(3, [1,2,3,5])
            1
            sage: RuleStar().insertion(6, [1,2,3,5]) is None
            True
        """
    def reverse_insertion(self, x, r):
        """
        Reverse bump the row ``r`` of the current insertion tableau ``p``
        with number ``x``, provided that ``r`` is the ``i``-th row of ``p``.

        The row ``r`` is modified in place. The bumped-out entry is returned.

        EXAMPLES::

            sage: from sage.combinat.rsk import RuleStar
            sage: RuleStar().reverse_insertion(4, [1,2,3,5])
            3
            sage: RuleStar().reverse_insertion(1, [1,2,3,5])
            3
            sage: RuleStar().reverse_insertion(5, [1,2,3,5])
            5
        """

class InsertionRules:
    """
    Catalog of rules for RSK-like insertion algorithms.
    """
    RSK = RuleRSK
    EG = RuleEG
    Hecke = RuleHecke
    dualRSK = RuleDualRSK
    coRSK = RuleCoRSK
    superRSK = RuleSuperRSK
    Star = RuleStar

def RSK(obj1=None, obj2=None, insertion=..., check_standard: bool = False, **options):
    '''
    Perform the Robinson-Schensted-Knuth (RSK) correspondence.

    The Robinson-Schensted-Knuth (RSK) correspondence (also known
    as the RSK algorithm) is most naturally stated as a bijection
    between generalized permutations (also known as two-line arrays,
    biwords, ...) and pairs of semi-standard Young tableaux `(P, Q)`
    of identical shape. The tableau `P` is known as the insertion
    tableau, and `Q` is known as the recording tableau.

    The basic operation is known as row insertion `P \\leftarrow k`
    (where `P` is a given semi-standard Young tableau, and `k` is an
    integer). Row insertion is a recursive algorithm which starts by
    setting `k_0 = k`, and in its `i`-th step inserts the number `k_i`
    into the `i`-th row of `P` (we start counting the rows at `0`) by
    replacing the first integer greater than `k_i` in the row by `k_i`
    and defines `k_{i+1}` as the integer that has been replaced. If no
    integer greater than `k_i` exists in the `i`-th row, then `k_i` is
    simply appended to the row and the algorithm terminates at this point.

    A *generalized permutation* (or *biword*) is a list
    `((j_0, k_0), (j_1, k_1), \\ldots, (j_{\\ell-1}, k_{\\ell-1}))`
    of pairs such that the letters `j_0, j_1, \\ldots, j_{\\ell-1}`
    are weakly increasing (that is,
    `j_0 \\leq j_1 \\leq \\cdots \\leq j_{\\ell-1}`), whereas the letters
    `k_i` satisfy `k_i \\leq k_{i+1}` whenever `j_i = j_{i+1}`.
    The `\\ell`-tuple `(j_0, j_1, \\ldots, j_{\\ell-1})` is called the
    *top line* of this generalized permutation,
    whereas the `\\ell`-tuple `(k_0, k_1, \\ldots, k_{\\ell-1})` is
    called its *bottom line*.

    Now the RSK algorithm, applied to a generalized permutation
    `p = ((j_0, k_0), (j_1, k_1), \\ldots, (j_{\\ell-1}, k_{\\ell-1}))`
    (encoded as a lexicographically sorted list of pairs) starts by
    initializing two semi-standard tableaux `P_0` and `Q_0` as empty
    tableaux. For each nonnegative integer `t` starting at `0`, take
    the pair `(j_t, k_t)` from `p` and set
    `P_{t+1} = P_t \\leftarrow k_t`, and define `Q_{t+1}` by adding a
    new box filled with `j_t` to the tableau `Q_t` at the same
    location the row insertion on `P_t` ended (that is to say, adding
    a new box with entry `j_t` such that `P_{t+1}` and `Q_{t+1}` have
    the same shape). The iterative process stops when `t` reaches the
    size of `p`, and the pair `(P_t, Q_t)` at this point is the image
    of `p` under the Robinson-Schensted-Knuth correspondence.

    This correspondence has been introduced in [Knu1970]_, where it has
    been referred to as "Construction A".

    For more information, see Chapter 7 in [Sta-EC2]_.

    We also note that integer matrices are in bijection with generalized
    permutations. Furthermore, we can convert any word `w` (and, in
    particular, any permutation) to a generalized permutation by
    considering the top row to be `(1, 2, \\ldots, n)` where `n` is the
    length of `w`.

    The optional argument ``insertion`` allows to specify an alternative
    insertion procedure to be used instead of the standard
    Robinson-Schensted-Knuth insertion.

    INPUT:

    - ``obj1``, ``obj2`` -- can be one of the following:

      - a word in an ordered alphabet (in this case, ``obj1`` is said
        word, and ``obj2`` is ``None``)
      - an integer matrix
      - two lists of equal length representing a generalized permutation
        (namely, the lists `(j_0, j_1, \\ldots, j_{\\ell-1})` and
        `(k_0, k_1, \\ldots, k_{\\ell-1})` represent the generalized
        permutation
        `((j_0, k_0), (j_1, k_1), \\ldots, (j_{\\ell-1}, k_{\\ell-1}))`)
      - any object which has a method ``_rsk_iter()`` which returns an
        iterator over the object represented as generalized permutation or
        a pair of lists (in this case, ``obj1`` is said object,
        and ``obj2`` is ``None``).

    - ``insertion`` -- (default: ``RSK.rules.RSK``) the following types
      of insertion are currently supported:

      - ``RSK.rules.RSK`` (or ``\'RSK\'``) -- Robinson-Schensted-Knuth
        insertion (:class:`~sage.combinat.rsk.RuleRSK`)
      - ``RSK.rules.EG`` (or ``\'EG\'``) -- Edelman-Greene insertion
        (only for reduced words of permutations/elements of a type `A`
        Coxeter group) (:class:`~sage.combinat.rsk.RuleEG`)
      - ``RSK.rules.Hecke`` -- (or ``\'hecke\'``) Hecke insertion (only
        guaranteed for generalized permutations whose top row is strictly
        increasing) (:class:`~sage.combinat.rsk.RuleHecke`)
      - ``RSK.rules.dualRSK`` (or ``\'dualRSK\'``) -- Dual RSK insertion
        (only for strict biwords) (:class:`~sage.combinat.rsk.RuleDualRSK`)
      - ``RSK.rules.coRSK`` (or ``\'coRSK\'``) -- CoRSK insertion (only
        for strict cobiwords) (:class:`~sage.combinat.rsk.RuleCoRSK`)
      - ``RSK.rules.superRSK`` (or ``\'super\'``) -- Super RSK insertion (only for
        restricted super biwords) (:class:`~sage.combinat.rsk.RuleSuperRSK`)
      - ``RSK.rules.Star`` (or ``\'Star\'``) -- `\\star`-insertion (only for
        fully commutative words in the 0-Hecke monoid)
        (:class:`~sage.combinat.rsk.RuleStar`)

    - ``check_standard`` -- boolean (default: ``False``); check if either of
      the resulting tableaux is a standard tableau, and if so, typecast it
      as such

    For precise information about constraints on the input and output,
    as well as the definition of the algorithm (if it is not standard
    RSK), see the particular :class:`~sage.combinat.rsk.Rule` class.

    EXAMPLES:

    If we only input one row, it is understood that the top row
    should be `(1, 2, \\ldots, n)`::

        sage: RSK([3,3,2,4,1])
        [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]
        sage: RSK(Word([3,3,2,4,1]))
        [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]
        sage: RSK(Word([2,3,3,2,1,3,2,3]))
        [[[1, 2, 2, 3, 3], [2, 3], [3]], [[1, 2, 3, 6, 8], [4, 7], [5]]]

    We can provide a generalized permutation::

        sage: RSK([1, 2, 2, 2], [2, 1, 1, 2])
        [[[1, 1, 2], [2]], [[1, 2, 2], [2]]]
        sage: RSK(Word([1,1,3,4,4]), [1,4,2,1,3])
        [[[1, 1, 3], [2], [4]], [[1, 1, 4], [3], [4]]]
        sage: RSK([1,3,3,4,4], Word([6,2,2,1,7]))
        [[[1, 2, 7], [2], [6]], [[1, 3, 4], [3], [4]]]

    We can provide a matrix::

        sage: RSK(matrix([[0,1],[2,1]]))
        [[[1, 1, 2], [2]], [[1, 2, 2], [2]]]

    We can also provide something looking like a matrix::

        sage: RSK([[0,1],[2,1]])
        [[[1, 1, 2], [2]], [[1, 2, 2], [2]]]

    There is also :func:`~sage.combinat.rsk.RSK_inverse` which performs
    the inverse of the bijection on a pair of semistandard tableaux. We
    note that the inverse function takes 2 separate tableaux as inputs, so
    to compose with :func:`~sage.combinat.rsk.RSK`, we need to use the
    python ``*`` on the output::

        sage: RSK_inverse(*RSK([1, 2, 2, 2], [2, 1, 1, 2]))
        [[1, 2, 2, 2], [2, 1, 1, 2]]
        sage: P,Q = RSK([1, 2, 2, 2], [2, 1, 1, 2])
        sage: RSK_inverse(P, Q)
        [[1, 2, 2, 2], [2, 1, 1, 2]]

    TESTS:

    Empty objects::

        sage: RSK(Permutation([]))
        [[], []]
        sage: RSK(Word([]))
        [[], []]
        sage: RSK(matrix([[]]))
        [[], []]
        sage: RSK([], [])
        [[], []]
        sage: RSK([[]])
        [[], []]
        sage: RSK(Word([]), insertion=RSK.rules.EG)
        [[], []]
        sage: RSK(Word([]), insertion=RSK.rules.Hecke)
        [[], []]
    '''
robinson_schensted_knuth = RSK

def RSK_inverse(p, q, output: str = 'array', insertion=...):
    """
    Return the generalized permutation corresponding to the pair of
    tableaux `(p, q)` under the inverse of the Robinson-Schensted-Knuth
    correspondence.

    For more information on the bijection, see :func:`RSK`.

    INPUT:

    - ``p``, ``q`` -- two semi-standard tableaux of the same shape, or
      (in the case when Hecke insertion is used) an increasing tableau and
      a set-valued tableau of the same shape (see the note below for the
      format of the set-valued tableau)

    - ``output`` -- (default: ``'array'``) if ``q`` is semi-standard:

      - ``'array'`` -- as a two-line array (i.e. generalized permutation or
        biword)
      - ``'matrix'`` -- as an integer matrix

      and if ``q`` is standard, we can also have the output:

      - ``'word'`` -- as a word

      and additionally if ``p`` is standard, we can also have the output:

      - ``'permutation'`` -- as a permutation

    - ``insertion`` -- (default: ``RSK.rules.RSK``) the insertion algorithm
      used in the bijection. Currently the following are supported:

      - ``RSK.rules.RSK`` (or ``'RSK'``) -- Robinson-Schensted-Knuth
        insertion (:class:`~sage.combinat.rsk.RuleRSK`)
      - ``RSK.rules.EG`` (or ``'EG'``) -- Edelman-Greene insertion
        (only for reduced words of permutations/elements of a type `A`
        Coxeter group) (:class:`~sage.combinat.rsk.RuleEG`)
      - ``RSK.rules.Hecke`` (or ``'hecke'``) -- Hecke insertion (only
        guaranteed for generalized permutations whose top row is strictly
        increasing) (:class:`~sage.combinat.rsk.RuleHecke`)
      - ``RSK.rules.dualRSK`` (or ``'dualRSK'``) -- Dual RSK insertion
        (only for strict biwords) (:class:`~sage.combinat.rsk.RuleDualRSK`)
      - ``RSK.rules.coRSK`` (or ``'coRSK'``) -- CoRSK insertion (only
        for strict cobiwords) (:class:`~sage.combinat.rsk.RuleCoRSK`)
      - ``RSK.rules.superRSK`` (or ``'super'``) -- Super RSK insertion (only for
        restricted super biwords) (:class:`~sage.combinat.rsk.RuleSuperRSK`)
      - ``RSK.rules.Star`` (or ``'Star'``) -- `\\star`-insertion (only for
        fully commutative words in the 0-Hecke monoid)
        (:class:`~sage.combinat.rsk.RuleStar`)

    For precise information about constraints on the input and
    output, see the particular :class:`~sage.combinat.rsk.Rule` class.

    .. NOTE::

        In the case of Hecke insertion, the input variable ``q`` should
        be a set-valued tableau, encoded as a tableau whose entries are
        strictly increasing tuples of positive integers. Each such tuple
        encodes the set of its entries.

    EXAMPLES:

    If both ``p`` and ``q`` are standard::

        sage: t1 = Tableau([[1, 2, 5], [3], [4]])
        sage: t2 = Tableau([[1, 2, 3], [4], [5]])
        sage: RSK_inverse(t1, t2)
        [[1, 2, 3, 4, 5], [1, 4, 5, 3, 2]]
        sage: RSK_inverse(t1, t2, 'word')
        word: 14532
        sage: RSK_inverse(t1, t2, 'matrix')
        [1 0 0 0 0]
        [0 0 0 1 0]
        [0 0 0 0 1]
        [0 0 1 0 0]
        [0 1 0 0 0]
        sage: RSK_inverse(t1, t2, 'permutation')
        [1, 4, 5, 3, 2]
        sage: RSK_inverse(t1, t1, 'permutation')
        [1, 4, 3, 2, 5]
        sage: RSK_inverse(t2, t2, 'permutation')
        [1, 2, 5, 4, 3]
        sage: RSK_inverse(t2, t1, 'permutation')
        [1, 5, 4, 2, 3]

    If the first tableau is semistandard::

        sage: p = Tableau([[1,2,2],[3]]); q = Tableau([[1,2,4],[3]])
        sage: ret = RSK_inverse(p, q); ret
        [[1, 2, 3, 4], [1, 3, 2, 2]]
        sage: RSK_inverse(p, q, 'word')
        word: 1322

    In general::

        sage: p = Tableau([[1,2,2],[2]]); q = Tableau([[1,3,3],[2]])
        sage: RSK_inverse(p, q)
        [[1, 2, 3, 3], [2, 1, 2, 2]]
        sage: RSK_inverse(p, q, 'matrix')
        [0 1]
        [1 0]
        [0 2]

    Using Hecke insertion::

        sage: w = [5, 4, 3, 1, 4, 2, 5, 5]
        sage: pq = RSK(w, insertion=RSK.rules.Hecke)
        sage: RSK_inverse(*pq, insertion=RSK.rules.Hecke, output='list')
        [5, 4, 3, 1, 4, 2, 5, 5]

    .. NOTE::

        The constructor of ``Tableau`` accepts not only semistandard
        tableaux, but also arbitrary lists that are fillings of a
        partition diagram. (And such lists are used, e.g., for the
        set-valued tableau ``q`` that is passed to
        ``RSK_inverse(p, q, insertion='hecke')``.)
        The user is responsible for ensuring that the tableaux passed to
        ``RSK_inverse`` are of the right types (semistandard, standard,
        increasing, set-valued as needed).

    TESTS:

    From empty tableaux::

        sage: RSK_inverse(Tableau([]), Tableau([]))
        [[], []]

    Check that :func:`RSK_inverse` is the inverse of :func:`RSK` on the
    different types of inputs/outputs::

        sage: f = lambda p: RSK_inverse(*RSK(p), output='permutation')
        sage: all(p == f(p) for n in range(7) for p in Permutations(n))
        True
        sage: all(RSK_inverse(*RSK(w), output='word') == w for n in range(4)
        ....:                                            for w in Words(5, n))
        True
        sage: from sage.combinat.integer_matrices import IntegerMatrices
        sage: M = IntegerMatrices([1,2,2,1], [3,1,1,1])
        sage: all(RSK_inverse(*RSK(m), output='matrix') == m for m in M)
        True

        sage: n = ZZ.random_element(200)
        sage: p = Permutations(n).random_element()
        sage: is_fine = True if p == f(p) else p ; is_fine
        True

    Both tableaux must be of the same shape::

        sage: RSK_inverse(Tableau([[1,2,3]]), Tableau([[1,2]]))
        Traceback (most recent call last):
        ...
        ValueError: p(=[[1, 2, 3]]) and q(=[[1, 2]]) must have the same shape

    Check that :issue:`20430` is fixed::

        sage: RSK([1,1,1,1,1,1,1,2,2,2,3], [1,1,1,1,1,1,3,2,2,2,1])
        [[[1, 1, 1, 1, 1, 1, 1, 2, 2], [2], [3]],
         [[1, 1, 1, 1, 1, 1, 1, 2, 2], [2], [3]]]
        sage: t = SemistandardTableau([[1, 1, 1, 1, 1, 1, 1, 2, 2], [2], [3]])
        sage: RSK_inverse(t, t, 'array')
        [[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3],
         [1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 1]]
    """
robinson_schensted_knuth_inverse = RSK_inverse

def to_matrix(t, b):
    """
    Return the integer matrix corresponding to a two-line array.

    INPUT:

    - ``t`` -- the top row of the array
    - ``b`` -- the bottom row of the array

    OUTPUT:

    An `m \\times n`-matrix (where `m` and `n` are the maximum entries in
    `t` and `b` respectively) whose `(i, j)`-th entry, for any `i` and `j`,
    is the number of all positions `k` satisfying `t_k = i` and `b_k = j`.

    EXAMPLES::

        sage: from sage.combinat.rsk import to_matrix
        sage: to_matrix([1, 1, 3, 3, 4], [2, 3, 1, 1, 3])
        [0 1 1]
        [0 0 0]
        [2 0 0]
        [0 0 1]
    """
