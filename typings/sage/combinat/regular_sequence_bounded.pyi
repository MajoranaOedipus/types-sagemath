def multiply_reduce(A, B):
    """
    Return the matrix `A\\cdot B` with entries `\\min{(A\\cdot B)_{ij},2}`.

    INPUT:

    - ``A`` -- an `m \\times n` matrix
    - ``B`` -- an `n \\times p` matrix

    OUTPUT:

    An `m \\times p` matrix with entries `\\min{(A\\cdot B)_{ij},2}`.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import multiply_reduce
        sage: A = Matrix([[2, 0], [0, 2]])
        sage: B = Matrix([[-2, 0], [0, 2]])
        sage: A*B
        [-4  0]
        [ 0  4]
        sage: multiply_reduce(A, B)
        [-4  0]
        [ 0  2]

    ::

        sage: A = Matrix([[1, 2, 3], [-1, -2, -3], [1, 2, 3]])
        sage: B = Matrix([[1, 2, 3], [2, 3, 4], [1, 2, 3]])
        sage: A*B
        [  8  14  20]
        [ -8 -14 -20]
        [  8  14  20]
        sage: multiply_reduce(A, B)
        [  2   2   2]
        [ -8 -14 -20]
        [  2   2   2]
    """
def construct_phi(matrices):
    """
    Return the set `\\phi(S)` as defined in [MS1977a]_.

    INPUT:

    - ``matrices`` -- a list of non-negative square matrices
      in the same dimension

    OUTPUT:

    A list of matrices.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import construct_phi
        sage: L = [Matrix([[2, 2], [1, 3]]), Matrix([[0, 2], [1, 1]])]
        sage: construct_phi(L)
        [
        [2 2]  [2 2]  [0 2]
        [2 2], [1 2], [1 1]
        ]

    ::

        sage: L = [Matrix([[42, 1, 0], [5, 0, 1], [0, 0, 1]]), Matrix([[0, 1, 1],
        ....: [4, 1, 1], [1, 2, 2]]), Matrix([[5, 1, 1], [1, 7, 1], [0, 1, 32]])]
        sage: construct_phi(L)
        [
        [2 2 1]  [1 2 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 0 2]  [2 2 2]
        [2 2 1]  [2 2 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 1 2]
        [0 0 1], [2 2 2], [2 2 2], [0 1 2], [2 0 2], [0 0 1], [2 1 2], [2 1 2],
        <BLANKLINE>
        [2 1 2]  [2 2 2]  [2 2 2]  [2 2 2]  [2 1 1]  [2 2 2]  [0 1 1]  [2 1 0]
        [2 2 2]  [1 2 2]  [2 2 2]  [2 2 2]  [1 2 1]  [2 1 2]  [2 1 1]  [2 0 1]
        [2 2 2], [1 2 2], [1 2 2], [2 1 2], [0 1 2], [2 0 2], [1 2 2], [0 0 1]
        ]

    TESTS::

        sage: L = [Matrix([[20, 1, 0], [2, 0, 0], [117, 0, 8]]),
        ....: Matrix([[0, 2, 1], [1, 0, 0], [1,1,2]]), Matrix([[8, 1, 0],
        ....: [0, 0, 3], [0, 1, 0]])]
        sage: construct_phi(L)
        [
        [2 1 0]  [2 2 2]  [2 1 2]  [2 2 2]  [2 2 2]  [2 0 2]  [1 2 2]  [2 1 2]
        [2 0 0]  [2 2 2]  [2 2 2]  [2 2 2]  [0 2 0]  [2 2 2]  [2 2 2]  [0 2 1]
        [2 0 2], [2 2 2], [2 1 0], [2 0 0], [0 0 2], [2 2 2], [1 0 0], [2 2 2],
        <BLANKLINE>
        [2 2 2]  [2 2 2]  [2 2 0]  [2 2 2]  [0 2 2]  [2 0 2]  [2 1 2]  [2 2 2]
        [0 1 2]  [2 2 2]  [2 2 0]  [0 2 2]  [2 2 2]  [2 1 0]  [2 0 2]  [2 2 2]
        [2 2 2], [2 0 2], [2 2 2], [2 2 2], [2 2 2], [2 1 2], [2 2 2], [2 1 0],
        <BLANKLINE>
        [2 2 2]  [2 2 0]  [2 2 2]  [0 1 2]  [2 2 2]  [1 2 2]  [2 2 0]  [2 2 2]
        [2 2 0]  [2 2 2]  [2 0 0]  [2 1 0]  [2 2 2]  [0 2 2]  [2 0 2]  [2 2 2]
        [2 2 0], [2 2 0], [2 2 2], [2 2 2], [0 1 2], [2 2 2], [2 0 0], [2 1 2],
        <BLANKLINE>
        [2 2 0]  [2 2 2]  [2 2 2]  [2 1 0]  [2 2 2]  [2 2 2]  [2 2 2]  [2 0 2]
        [2 2 2]  [2 2 0]  [1 2 2]  [0 0 2]  [2 0 0]  [2 2 2]  [2 2 2]  [2 2 0]
        [2 2 2], [2 2 2], [2 2 2], [0 1 0], [2 0 2], [0 2 1], [2 2 0], [2 2 2],
        <BLANKLINE>
        [2 2 2]  [2 2 2]  [2 2 2]  [0 2 1]  [2 2 2]  [2 2 2]  [2 2 2]
        [2 0 2]  [0 0 2]  [2 2 2]  [1 0 0]  [2 0 2]  [2 1 2]  [2 2 2]
        [2 2 2], [0 2 0], [0 2 2], [1 1 2], [2 0 0], [2 2 2], [1 2 2]
        ]
    """
def is_integer_valued(matrices):
    """
    Return whether every matrix in ``matrices`` is integer-valued.

    INPUT:

    - ``matrices`` -- a list of square matrices in the same dimension

    OUTPUT:

    A boolean.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import is_integer_valued
        sage: matrices = [Matrix([[1, 2], [-1, 0]]), Matrix([[42, -42], [0, 0]])]
        sage: is_integer_valued(matrices)
        True

    ::

        sage: matrices = [Matrix([[1, pi], [-1, 0]])]
        sage: is_integer_valued(matrices)
        False

    ::

        sage: matrices = [Matrix([[1, 1/2], [2/4, 0]])]
        sage: is_integer_valued(matrices)
        False

    ::

        sage: matrices = [Matrix([[1, 4/2], [-1, 0]])]
        sage: is_integer_valued(matrices)
        True
    """
def is_non_negative(matrices):
    """
    Return whether every matrix in ``matrices`` is non-negative.

    INPUT:

    - ``matrices`` -- a list of square matrices in the same dimension

    OUTPUT:

    A boolean.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import is_non_negative
        sage: matrices = [Matrix([[1, 2], [1, 0]]), Matrix([[42, -42], [0, 0]])]
        sage: is_non_negative(matrices)
        False

    ::

        sage: matrices = [Matrix([[0]])]
        sage: is_non_negative(matrices)
        True

    ::

        sage: matrices = [Matrix([[1, 1/2], [2/4, 0]])]
        sage: is_non_negative(matrices)
        True
    """
def is_bounded_via_mandel_simon_algorithm(matrices):
    """
    Return whether the semigroup generated whether the semigroup of all
    possible products of ``matrices`` is finite/bounded.

    INPUT:

    - ``matrices`` -- a list of non-negative square matrices
      in the same dimension

    OUTPUT:

    A boolean.

    ALGORITHM:

    A criterion based on [MS1977a]_ is used here.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import is_bounded_via_mandel_simon_algorithm
        sage: J = [Matrix([[1, 0, 1], [0, 1, 1], [0, 0, 0]])]
        sage: is_bounded_via_mandel_simon_algorithm(J)
        True

    ::

        sage: from sage.combinat.regular_sequence_bounded import is_bounded_via_mandel_simon_algorithm
        sage: K = [Matrix([[1, 1], [1, 1]])]
        sage: is_bounded_via_mandel_simon_algorithm(K)
        False

    ::

        sage: L = [Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 0]])]
        sage: is_bounded_via_mandel_simon_algorithm(L)
        True

    ::

        sage: M = [Matrix([[1, 0], [0, 2]]), Matrix([[1, 0], [0, 0]])]
        sage: is_bounded_via_mandel_simon_algorithm(M)
        False

    Non-integer-valued input::

        sage: N = [Matrix([[0.5, 0], [1, 0]])]
        sage: is_bounded_via_mandel_simon_algorithm(N)
        Traceback (most recent call last):
        ...
        ValueError: Not all matrices are integer-valued.
    """
def has_bounded_matrix_powers(matrices) -> bool:
    """
    Return whether `M^n` is bounded for `n \\to \\infty`
    for all `M` in ``matrices``.

    INPUT:

    - ``matrices`` -- a list of square matrices

    ALGORITHM:

    Eigenvalues are used for the check.

    EXAMPLES:

    Maximum of the absolute value of the eigenvalues `=1`,
    algebraic multiplicity equals geometric multiplicity
    for all eigenvalues with absolute value `=1`::

        sage: from sage.combinat.regular_sequence_bounded import has_bounded_matrix_powers
        sage: matrices = [Matrix([[-1, 1, 1], [-1, 1, 1], [1, -1, 1]]),
        ....:             Matrix([[-1, 1, 1], [-1, 0, 0], [1, 1, 1]])]
        sage: has_bounded_matrix_powers(matrices)
        True

    Maximum of the absolute value of the eigenvalues `>1`::

        sage: matrices = [Matrix([[1, 1], [1/2, -1]])]
        sage: has_bounded_matrix_powers(matrices)
        False

    Maximum of the absolute value of the eigenvalues `=1`,
    algebraic and geometric multiplicities different for eigenvalue `1`::

        sage: matrices = [Matrix([[1,1],[0,1]])]
        sage: has_bounded_matrix_powers(matrices)
        False

    Maximum of the absolute value of the eigenvalues `<1`::

        sage: matrices = [Matrix([[1, -1], [1/2, -1]])]
        sage: has_bounded_matrix_powers(matrices)
        True
    """
def make_positive(matrices) -> list:
    """
    Return a list of non-negative matrices

    INPUT:

    - ``matrices`` -- a list of matrices where every matrix is either
      non-negative or non-positive.

    OUTPUT:

    A list of matrices containing every non-negative matrix of ``matrices``,
    and `-M` if `M` is a non-positive matrix of ``matrices``.

    EXAMPLES::

        sage: from sage.combinat.regular_sequence_bounded import make_positive
        sage: matrices = [Matrix([[1, 2], [1, 0]]), Matrix([[42, 42], [0, 0]])]
        sage: make_positive(matrices)
        [
        [1 2]  [42 42]
        [1 0], [ 0  0]
        ]

    ::

        sage: matrices = [Matrix([[1, 2], [1, 0]]), Matrix([[-42, -42], [0, 0]])]
        sage: make_positive(matrices)
        [
        [1 2]  [42 42]
        [1 0], [ 0  0]
        ]

    ::

        sage: matrices = [Matrix([[1, 2], [1, 0]]), Matrix([[42, -42], [0, 0]])]
        sage: make_positive(matrices)
        Traceback (most recent call last):
        ...
        ValueError: There is a matrix which is neither non-negative nor non-positive.
    """
def regular_sequence_is_bounded(S):
    """
    Return whether this `k`-regular sequence is bounded.

    INPUT:

    - ``S`` -- a `k`-regular sequence

    OUTPUT:

    A boolean.

    EXAMPLES:

    Thue--Morse Sequence::

        sage: from sage.combinat.regular_sequence_bounded import regular_sequence_is_bounded
        sage: Seq2 = RegularSequenceRing(2, ZZ)
        sage: TM = Seq2([Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [1, 0]])],
        ....:            left=vector([1, 0]), right=vector([0, 1]))
        sage: regular_sequence_is_bounded(TM)
        True

    Binary Sum of Digits::

        sage: SD = Seq2([Matrix([[1, 0], [0, 1]]), Matrix([[0, -1], [1, 2]])],
        ....:           left=vector([0, 1]), right=vector([1, 0]))
        sage: regular_sequence_is_bounded(SD)
        False

    Sequence of All Natural Numbers::

        sage: N = Seq2([Matrix([[2, 0], [2, 1]]), Matrix([[0, 1], [-2, 3]])],
        ....:          left=vector([1, 0]), right=vector([0, 1]))
        sage: regular_sequence_is_bounded(N)
        False

    Indicator Function of Even Integers::

        sage: E = Seq2([Matrix([[0, 1], [0, 1]]), Matrix([[0, 0], [0, 1]])],
        ....:          left=vector([1, 0]), right=vector([1, 1]))
        sage: regular_sequence_is_bounded(E)
        True

    Indicator Function of Odd Integers::

        sage: O = Seq2([Matrix([[0, 0], [0, 1]]), Matrix([[0, 1], [0, 1]])],
        ....:          left=vector([1, 0]), right=vector([0, 1]))
        sage: regular_sequence_is_bounded(O)
        True

    Number of Odd Entries in Pascal's Triangle::

        sage: U = Seq2([Matrix([[3, 0], [6, 1]]), Matrix([[0, 1], [-6, 5]])],
        ....:          left=vector([1, 0]), right=vector([0, 1]))
        sage: regular_sequence_is_bounded(U)
        False

    Counting '10' in the Binary Representation::

        sage: C = Seq2([Matrix([[0, 1, 0, 0], [0, 0, 0, 1],
        ....:                   [-1, 0, 1, 1], [0, 0, 0, 1]]),
        ....:           Matrix([[0, 0, 1, 0], [0, 1, 0, 0],
        ....:                   [0, 0, 1, 0], [-1, 0, 1, 1]])],
        ....:                  left=vector([1, 0, 0, 0]),
        ....:                  right=vector([0, 0, 1, 0]))
        sage: regular_sequence_is_bounded(C)
        False

    Numbers Starting with '10'::

        sage: D = Seq2([Matrix([[0, 1, 0, 0], [0, 0, 1, 0],
        ....:                   [0, -2, 3, 0], [0, -2, 2, 1]]),
        ....:           Matrix([[2, 0, 0, 0], [0, 0, 0, 1],
        ....:                   [0, 2, 0, 1], [0, -2, 0, 3]])],
        ....:                  left=vector([1, 0, 0, 0]),
        ....:                  right=vector([2, 2, 2, 5]))
        sage: regular_sequence_is_bounded(D)
        False

    Signum Function::

        sage: S = Seq2([Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [0, 1]])],
        ....:          left=vector([1, 0]), right=vector([0, 1]))
        sage: regular_sequence_is_bounded(S)
        True

    Number of Digits from the Right to the First '1'::

        sage: S = Seq2([Matrix([[0, 1, 0], [-1, 2, 0], [0, 0, 1]]),
        ....:           Matrix([[0, 0, 1], [0, 0, 2], [0, 0, 1]])],
        ....:          left=vector([1, 0, 0]), right=vector([0, 0, 1]))
        sage: regular_sequence_is_bounded(S)
        False

    TESTS::

        sage: S = Seq2((Matrix([[0, 1, 0], [0, 0, 1], [-1, 2, 0]]),
        ....: Matrix([[-1, 0, 0], [-3/4, -1/4, 3/4], [-1/4, 1/4, -3/4]])),
        ....: left=vector([1, 0, 0]), right=vector([-4, -4, -4]))
        sage: regular_sequence_is_bounded(S)
        False

    ::

        sage: S = Seq2((Matrix([[1, 0], [1, 0]]), Matrix([[0, 1],[1, 0]])),
        ....:          left = vector([1, 1]), right = vector([1, 0]),
        ....:          allow_degenerated_sequence=True)
        sage: regular_sequence_is_bounded(S)
        True
    """
