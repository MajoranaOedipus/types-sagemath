from sage.structure.sequence import Sequence as Sequence

def is_skew(seq, verbose: bool = False):
    """
    Check if the given sequence is skew.

    A sequence `X=\\{x_1, x_2, ...,x_n\\}` is defined skew (according to Definition
    7.4 of [Seb2017]_) if `n` is even and `x_i = -x_{n-i+1}`.

    INPUT:

    - ``seq`` -- the sequence that should be checked

    - ``verbose`` -- boolean (default: ``False``); if ``True`` the function
      will be verbose when the sequences do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.t_sequences import is_skew
        sage: is_skew([1, -1, 1, -1, 1, -1])
        True
        sage: is_skew([1, -1, -1, -1], verbose=True)
        Constraint not satisfied at index 1
        False

    TESTS::

        sage: is_skew([1, -1, -1])
        False
        sage: is_skew([1, -1, -1, 1, -1], verbose=True)
        Sequence should be of even length
        False
    """
def is_symmetric(seq, verbose: bool = False) -> bool:
    """
    Check if the given sequence is symmetric.

    A sequence `X=\\{x_1, x_2, ...,x_n\\}` is defined symmetric (according to Definition
    7.4 of [Seb2017]_) if `n` is odd and `x_i = x_{n-i+1}`.

    INPUT:

    - ``seq`` -- the sequence that should be checked

    - ``verbose`` -- boolean (default: ``False``); if ``True`` the function will be
      verbose when the sequences do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.t_sequences import is_symmetric
        sage: is_symmetric([1, -1, 1, -1, 1])
        True
        sage: is_symmetric([1, -1, 1, 1, 1], verbose=True)
        Constraint not satisfied at index 1
        False

    TESTS::

        sage: is_symmetric([1, -1, -1, 1])
        False
        sage: is_symmetric([1, -1, -1, 1], verbose=True)
        Sequence should be of odd length
        False
    """
def is_T_sequences_set(sequences, verbose: bool = False):
    """
    Check if a family of sequences is composed of T-sequences.

    Given 4 (-1, 0, +1) sequences, they will be T-sequences if
    (Definition 7.4 of [Seb2017]_):

    * they have all the same length `t`
    * for each index `i`, exactly one sequence is nonzero at `i`
    * the nonperiodic autocorrelation is equal to `0`

    INPUT:

    - ``sequences`` -- list of four sequences

    - ``verbose`` -- boolean (default: ``False``); if ``True`` the function will be
      verbose when the sequences do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.t_sequences import is_T_sequences_set
        sage: seqs = [[1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, -1], [0, 0, 0, 0, 0]]
        sage: is_T_sequences_set(seqs)
        True
        sage: seqs = [[1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, -1], [0, 0, 0, 0, 0]]
        sage: is_T_sequences_set(seqs, verbose=True)
        There should be exactly a nonzero element at every index, found 2 such
         elements at index 3
        False


    TESTS::

        sage: seqs = [[1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, -1], [0, 0, 0, 0, 0]]
        sage: is_T_sequences_set(seqs)
        False
        sage: seqs = [[1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, -1, -1], [0, 0, 0, 0, 0]]
        sage: is_T_sequences_set(seqs, verbose=True)
        Nonperiodic autocorrelation should always be zero, found 2 for parameter 1
        False
        sage: is_T_sequences_set([[1, 0, ], [0, -1, 0], [0, 0, 1]])
        False
        sage: seqs = [[1, 2, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, -1, -1], [0, 0, 0, 0, 0]]
        sage: is_T_sequences_set(seqs, verbose=True)
        Elements should be in (-1, 0, +1), but 2 was found at index 1
        False
    """
def turyn_sequences_smallcases(l, existence: bool = False):
    """
    Construction of Turyn sequences for small values of `l`.

    The data is taken from [Seb2017]_ and [CRSKKY1989]_.

    INPUT:

    - ``l`` -- integer; the length of the Turyn sequences

    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the Turyn sequences are available for the given length

    EXAMPLES:

    By default, this method returns the four Turyn sequences ::

        sage: from sage.combinat.t_sequences import turyn_sequences_smallcases
        sage: turyn_sequences_smallcases(4)
        [[1, 1, -1, -1], [1, 1, -1, 1], [1, 1, 1], [1, -1, 1]]

    If we pass the ``existence`` flag, the method will return a boolean ::

        sage: turyn_sequences_smallcases(4, existence=True)
        True

    TESTS::

        sage: turyn_sequences_smallcases(17)
        Traceback (most recent call last):
        ...
        ValueError: Turyn sequence of length 17 is not implemented yet.
        sage: turyn_sequences_smallcases(17, existence=True)
        False
    """
def T_sequences_construction_from_base_sequences(base_sequences, check: bool = True):
    """
    Construct T-sequences of length `2n+p` from base sequences of length `n+p, n+p, n, n`.

    Given base sequences `A, B, C, D`, the T-sequences are constructed as described in
    [KTR2005]_:

    .. MATH::

        \\begin{aligned}
        T_1 &= \\frac{1}{2}(A+B); 0_{n} \\\\\n        T_2 &= \\frac{1}{2}(A-B); 0_{n} \\\\\n        T_3 &= 0_{n+p} + \\frac{1}{2}(C+D) \\\\\n        T_4 &= 0_{n+p} + \\frac{1}{2}(C-D)
        \\end{aligned}

    INPUT:

    - ``base_sequences`` -- the base sequences that should be used to construct
      the T-sequences

    - ``check`` -- boolean (default: ``True``); check that the sequences
      created are T-sequences before returning them

    EXAMPLES::

        sage: from sage.combinat.t_sequences import turyn_sequences_smallcases, T_sequences_construction_from_base_sequences
        sage: seqs = turyn_sequences_smallcases(4)
        sage: T_sequences_construction_from_base_sequences(seqs)
        [[1, 1, -1, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]]

    TESTS::

        sage: from sage.combinat.t_sequences import base_sequences_construction, is_T_sequences_set
        sage: seqs = turyn_sequences_smallcases(4)
        sage: is_T_sequences_set(T_sequences_construction_from_base_sequences(seqs))
        True
        sage: T_sequences_construction_from_base_sequences([[1, -1], [-1, 1], [1]])
        Traceback (most recent call last):
        ...
        AssertionError
        sage: X = [1,1,-1,1,-1,1,-1,1]
        sage: Y = [1,-1,-1,-1,-1,-1,-1,1]
        sage: Z = [1,-1,-1,1,1,1,1,-1]
        sage: W = [1,1,1,-1,1,1,-1]
        sage: base_seqs = base_sequences_construction([X, Y, Z, W])
        sage: is_T_sequences_set(T_sequences_construction_from_base_sequences(base_seqs))
        True
    """
def T_sequences_construction_from_turyn_sequences(turyn_sequences, check: bool = True):
    """
    Construct T-sequences of length `4l-1` from Turyn sequences of length `l`.

    Given Turyn sequences `X, U, Y, V`, the T-sequences are constructed as described in
    theorem 7.7 of [Seb2017]_:

    .. MATH::

        \\begin{aligned}
        T_1 &= 1; 0_{4l-2} \\\\\n        T_2 &= 0; X/Y; 0_{2l-1} \\\\\n        T_3 &= 0_{2l}; U/0_{l-2} \\\\\n        T_4 &= 0_{2l} + 0_{l}/V
        \\end{aligned}

    INPUT:

    - ``turyn_sequences`` -- the Turyn sequences that should be used to
      construct the T-sequences

    - ``check`` -- boolean (default: ``True``); check that the sequences
      created are T-sequences before returning them

    EXAMPLES::

        sage: from sage.combinat.t_sequences import turyn_sequences_smallcases, T_sequences_construction_from_turyn_sequences, is_T_sequences_set
        sage: seqs = turyn_sequences_smallcases(4)
        sage: T_sequences_construction_from_turyn_sequences(seqs)
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, -1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0]]

    TESTS::

        sage: seqs = turyn_sequences_smallcases(4)
        sage: is_T_sequences_set(T_sequences_construction_from_turyn_sequences(seqs))
        True
        sage: T_sequences_construction_from_turyn_sequences([[1, -1], [-1, 1], [1]])
        Traceback (most recent call last):
        ...
        AssertionError
    """
def T_sequences_smallcases(t, existence: bool = False, check: bool = True):
    """
    Construct T-sequences for some small values of `t`.

    This method will try to use the constructions defined in
    :func:`T_sequences_construction_from_base_sequences` and
    :func:`T_sequences_construction_from_turyn_sequences`
    together with the Turyn sequences stored in :func:`turyn_sequences_smallcases`,
    or base sequences created by :func:`base_sequences_smallcases`.

    This function contains also some T-sequences taken directly from [CRSKKY1989]_.

    INPUT:

    - ``t`` -- integer; the length of the T-sequences to construct

    - ``existence`` -- boolean (default: ``False``); if ``True``, this method
      only returns whether a T-sequences of the given size can be constructed

    - ``check`` -- boolean (default: ``True``); check that the sequences are
      T-sequences before returning them

    EXAMPLES:

    By default, this method returns the four T-sequences ::

        sage: from sage.combinat.t_sequences import T_sequences_smallcases, is_T_sequences_set
        sage: T_sequences_smallcases(9)
        [[1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 1, -1, 0]]

    If the existence flag is passed, the method returns a boolean ::

        sage: T_sequences_smallcases(9, existence=True)
        True

    TESTS::

        sage: T_sequences_smallcases(66)
        Traceback (most recent call last):
        ...
        ValueError: T Sequences of length 66 not yet implemented.
        sage: is_T_sequences_set(T_sequences_smallcases(47))
        True
        sage: is_T_sequences_set(T_sequences_smallcases(11))
        True
        sage: T_sequences_smallcases(69, existence=True)
        False
    """
def base_sequences_construction(turyn_type_seqs, check: bool = True):
    """
    Construct base sequences of length `2n-1, 2n-1, n, n` from Turyn type
    sequences of length `n,n,n,n-1`.

    Given Turyn type sequences `X, Y, Z, W` of length `n,n,n,n-1`, Theorem 1 of
    [KTR2005]_  shows that the following are base sequences of length
    `2n-1, 2n-1, n, n`:

    .. MATH::

        \\begin{aligned}
        A &= Z;W \\\\\n        B &= Z; -W \\\\\n        C &= X \\\\\n        D &= Y
        \\end{aligned}

    INPUT:

    - ``turyn_type_seqs`` -- the list of 4 Turyn type sequences that should be
      used to construct the base sequences

    - ``check`` -- boolean (default: ``True``); check that the resulting
      sequences are base sequences before returning them

    OUTPUT: list containing the four base sequences

    EXAMPLES::

        sage: from sage.combinat.t_sequences import base_sequences_construction
        sage: X = [1,1,-1,1,-1,1,-1,1]
        sage: Y = [1,-1,-1,-1,-1,-1,-1,1]
        sage: Z = [1,-1,-1,1,1,1,1,-1]
        sage: W = [1,1,1,-1,1,1,-1]
        sage: base_sequences_construction([X, Y, Z, W])
        [[1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1],
        [1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1],
        [1, 1, -1, 1, -1, 1, -1, 1],
        [1, -1, -1, -1, -1, -1, -1, 1]]

    TESTS::

        sage: base_sequences_construction([[1, -1], [1], [1], [-1]])
        Traceback (most recent call last):
        ...
        AssertionError

    .. SEEALSO::

        :func:`is_base_sequences_tuple`
    """
def is_base_sequences_tuple(base_sequences, verbose: bool = False):
    """Check if the given sequences are base sequences.

    Four (-1, +1) sequences `A, B, C, D` of length `n+p, n+p, n, n` are called
    base sequences if for all `j \\ge 1`:

    .. MATH::

        N_A(j)+N_B(j)+N_C(j)+N_D(j) = 0

    where `N_X(j)` is the nonperiodic autocorrelation (See definition in [KTR2005]_).

    INPUT:

    - ``base_sequences`` -- the list of 4 sequences that should be checked

    - ``verbose`` -- boolean (default: ``False``); if ``True`` the function
      will be verbose when the sequences do not satisfy the constraints

    EXAMPLES::

        sage: from sage.combinat.t_sequences import is_base_sequences_tuple
        sage: seqs = [[1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1],[1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1],[1, 1, -1, 1, -1, 1, -1, 1],[1, -1, -1, -1, -1, -1, -1, 1]]
        sage: is_base_sequences_tuple(seqs)
        True

    If verbose is true, the function will be verbose ::

        sage: seqs = [[1, -1], [1, 1], [-1], [2]]
        sage: is_base_sequences_tuple(seqs, verbose=True)
        Base sequences should only contain -1, +1, found 2
        False

    TESTS:

        sage: seqs = [[1, -1], [1], [-1]]
        sage: is_base_sequences_tuple(seqs)
        False
        sage: seqs = [[1, -1], [1, -1], [-1], [1]]
        sage: is_base_sequences_tuple(seqs)
        False
        sage: seqs = [[1, -1], [1, 1], [-1], [2]]
        sage: is_base_sequences_tuple(seqs)
        False
        sage: seqs = [[1, -1], [1], [-1], [1]]
        sage: is_base_sequences_tuple(seqs)
        False

    .. SEEALSO::

        :func:`base_sequences_construction`
    """
def turyn_type_sequences_smallcases(n, existence: bool = False):
    """
    Construction of Turyn type sequences for small values of `n`.

    The data is taken from [KTR2005]_ for `n= 36`, and from [BDKR2013]_ for `n\\le 32`.

    INPUT:

    - ``n`` -- integer; the length of the Turyn type sequences

    - ``existence`` -- boolean (default: ``False``); if ``True``, only return
      whether the Turyn type sequences are available for the given length

    EXAMPLES:

    By default, this method returns the four Turyn type sequences ::

        sage: from sage.combinat.t_sequences import turyn_type_sequences_smallcases
        sage: turyn_type_sequences_smallcases(4)
        [[1, 1, 1, 1], [1, 1, -1, 1], [1, 1, -1, -1], [1, -1, 1]]

    If we pass the ``existence`` flag, the method will return a boolean ::

        sage: turyn_type_sequences_smallcases(4, existence=True)
        True

    TESTS::

        sage: turyn_type_sequences_smallcases(17)
        Traceback (most recent call last):
        ...
        ValueError: Turyn type sequences of length 17 are not implemented yet.
        sage: turyn_type_sequences_smallcases(17, existence=True)
        False

    ALGORITHM:

    The Turyn type sequences are stored in hexadecimal format.
    Given `n` hexadecimal digits `h_1, h_2,...,h_n`, it is possible to get the
    Turyn type sequences by converting each `h_i` (`1 \\le i \\le n-1`) into a
    four digits binary number. Then, the `j`-th binary digit is `0` if the `i`-th
    number in the `j`-th sequence is `1`, and it is `1` if the number in the
    sequence is -1.

    For the `n`-th digit, it should be converted to a 3 digits binary number, and
    then the same mapping as before can be used (see also [BDKR2013]_).
    """
def base_sequences_smallcases(n, p, existence: bool = False, check: bool = True):
    """Construct base sequences of length `n+p, n+p, n, n` from available data.

    The function uses the construction :func:`base_sequences_construction`,
    together with Turyn type sequences from :func:`turyn_type_sequences_smallcases`
    to construct base sequences with `p = n-1`.

    Furthermore, this function uses also Turyn sequences (i.e. base sequences
    with `p=1`) from :func:`turyn_sequences_smallcases`.

    INPUT:

    - ``n`` -- integer; the length of the last two base sequences

    - ``p`` -- integer; `n+p` will be the length of the first two base
      sequences

    - ``existence`` -- boolean (default: ``False``); if ``True``, the function
      will only check whether the base sequences can be constructed

    - ``check`` -- boolean (default: ``True``); check that the resulting
      sequences are base sequences before returning them

    OUTPUT:

    If ``existence`` is ``False``, the function returns a list containing the
    four base sequences, or raises an error if the base sequences cannot be
    constructed. If ``existence`` is ``True``, the function returns a boolean,
    which is ``True`` if the base sequences can be constructed and ``False``
    otherwise.

    EXAMPLES::

        sage: from sage.combinat.t_sequences import base_sequences_smallcases
        sage: base_sequences_smallcases(8, 7)
        [[1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1],
        [1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1],
        [1, 1, -1, 1, -1, 1, -1, 1],
        [1, -1, -1, -1, -1, -1, -1, 1]]

    If ``existence`` is ``True``, the function returns a boolean ::

        sage: base_sequences_smallcases(8, 7, existence=True)
        True
        sage: base_sequences_smallcases(7, 5, existence=True)
        False

    TESTS::

        sage: base_sequences_smallcases(7, 5)
        Traceback (most recent call last):
        ...
        ValueError: Base sequences of order 12, 12, 7, 7 not yet implemented.
        sage: seqs = base_sequences_smallcases(16, 15)
        sage: len(seqs[0]) == len(seqs[1]) == 16+15
        True
        sage: len(seqs[2]) == len(seqs[3]) == 16
        True
    """
