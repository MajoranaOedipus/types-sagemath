from _typeshed import Incomplete
from sage.arith.functions import lcm as lcm
from sage.arith.misc import is_prime as is_prime, legendre_symbol as legendre_symbol, next_prime as next_prime, next_prime_power as next_prime_power
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class BinaryRecurrenceSequence(SageObject):
    """
    Create a linear binary recurrence sequence defined by initial conditions
    `u_0` and `u_1` and recurrence relation `u_{n+2} = b*u_{n+1}+c*u_n`.

    INPUT:

    - ``b`` -- integer; (partially determining the recurrence relation)

    - ``c`` -- integer; (partially determining the recurrence relation)

    - ``u0`` -- integer; (the `0`-th term of the binary recurrence sequence)

    - ``u1`` -- integer; (the `1`-st term of the binary recurrence sequence)

    OUTPUT: an integral linear binary recurrence sequence defined by `u_0`,
    `u_1`, and `u_{n+2} = b u_{n+1}+c u_n`

    .. SEEALSO::

        :func:`fibonacci`, :func:`lucas_number1`, :func:`lucas_number2`

    EXAMPLES::

        sage: R = BinaryRecurrenceSequence(3,3,2,1)
        sage: R
        Binary recurrence sequence defined by: u_n = 3 * u_{n-1} + 3 * u_{n-2};
        With initial conditions: u_0 = 2, and u_1 = 1
    """
    b: Incomplete
    c: Incomplete
    u0: Incomplete
    u1: Incomplete
    def __init__(self, b, c, u0: int = 0, u1: int = 1) -> None:
        """
        See :class:`BinaryRecurrenceSequence` for full documentation.

        EXAMPLES::

            sage: R = BinaryRecurrenceSequence(3,3,2,1)
            sage: R
            Binary recurrence sequence defined by: u_n = 3 * u_{n-1} + 3 * u_{n-2};
            With initial conditions: u_0 = 2, and u_1 = 1

            sage: R = BinaryRecurrenceSequence(1,1)
            sage: loads(R.dumps()) == R
            True
        """
    def __eq__(self, other) -> bool:
        """
        Compare two binary recurrence sequences.

        EXAMPLES::

            sage: R = BinaryRecurrenceSequence(3,3,2,1)
            sage: S = BinaryRecurrenceSequence(3,3,2,1)
            sage: R == S
            True

            sage: T = BinaryRecurrenceSequence(3,3,2,2)
            sage: R == T
            False
        """
    def __call__(self, n, modulus: int = 0):
        """
        Give the `n`-th term of a binary recurrence sequence, possibly mod some modulus.

        INPUT:

        - ``n`` -- integer; the index of the term in the binary recurrence sequence

        - ``modulus`` -- a natural number (optional --  default value is 0)

        OUTPUT:

        - An integer (the `n`-th term of the binary recurrence sequence modulo ``modulus``)

        EXAMPLES::

            sage: R = BinaryRecurrenceSequence(3,3,2,1)
            sage: R(2)
            9
            sage: R(101)
            16158686318788579168659644539538474790082623100896663971001
            sage: R(101,12)
            9
            sage: R(101)%12
            9
        """
    def is_degenerate(self) -> bool:
        """
        Decide whether the binary recurrence sequence is degenerate.

        Let `\\alpha` and `\\beta` denote the roots of the characteristic polynomial
        `p(x) = x^2-bx -c`.  Let `a = u_1-u_0\\beta/(\\beta - \\alpha)` and
        `b = u_1-u_0\\alpha/(\\beta - \\alpha)`.  The sequence is, thus, given by
        `u_n = a \\alpha^n - b\\beta^n`.  Then we say that the sequence is nondegenerate
        if and only if `a*b*\\alpha*\\beta \\neq 0` and `\\alpha/\\beta` is not a
        root of unity.

        More concretely, there are 4 classes of degeneracy, that can all be formulated
        in terms of the matrix `F = [[0,1], [c, b]]`.

        - `F` is singular -- this corresponds to ``c`` = 0, and thus
          `\\alpha*\\beta = 0`. This sequence is geometric after term ``u0``
          and so we call it ``quasigeometric``

        - `v = [[u_0], [u_1]]` is an eigenvector of `F` -- this corresponds to
          a ``geometric`` sequence with `a*b = 0`

        - `F` is nondiagonalizable -- this corresponds to `\\alpha = \\beta`.
          This sequence will be the point-wise product of an arithmetic and
          geometric sequence.

        - `F^k` is scalar, for some `k>1` -- this corresponds to
          `\\alpha/\\beta` a `k` th root of unity. This sequence is a union of
          several geometric sequences, and so we again call it ``quasigeometric``.

        EXAMPLES::

            sage: S = BinaryRecurrenceSequence(0,1)
            sage: S.is_degenerate()
            True
            sage: S.is_geometric()
            False
            sage: S.is_quasigeometric()
            True

            sage: R = BinaryRecurrenceSequence(3,-2)
            sage: R.is_degenerate()
            False

            sage: T = BinaryRecurrenceSequence(2,-1)
            sage: T.is_degenerate()
            True
            sage: T.is_arithmetic()
            True
        """
    def is_geometric(self) -> bool:
        """
        Decide whether the binary recurrence sequence is geometric - ie a geometric sequence.

        This is a subcase of a degenerate binary recurrence sequence, for which `ab=0`, i.e.
        `u_{n}/u_{n-1}=r` for some value of `r`.

        See :meth:`is_degenerate` for a description of
        degeneracy and definitions of `a` and `b`.

        EXAMPLES::

            sage: S = BinaryRecurrenceSequence(2,0,1,2)
            sage: [S(i) for i in range(10)]
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: S.is_geometric()
            True
        """
    def is_quasigeometric(self) -> bool:
        """
        Decide whether the binary recurrence sequence is degenerate and similar to a geometric sequence,
        i.e. the union of multiple geometric sequences, or geometric after term ``u0``.

        If `\\alpha/\\beta` is a `k` th root of unity, where `k>1`, then necessarily `k = 2, 3, 4, 6`.
        Then `F = [[0,1],[c,b]` is diagonalizable, and `F^k = [[\\alpha^k, 0], [0,\\beta^k]]` is a diagonal
        matrix.  Thus for all values of `j` mod `k`, the `j` mod `k` terms of `u_n` form a geometric
        series.

        If `\\alpha` or `\\beta` is zero, this implies that `c=0`.  This is the case when `F` is
        singular.  In this case, `u_1, u_2, u_3, ...` is geometric.

        EXAMPLES::

            sage: S = BinaryRecurrenceSequence(0,1)
            sage: [S(i) for i in range(10)]
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
            sage: S.is_quasigeometric()
            True

            sage: R = BinaryRecurrenceSequence(3,0)
            sage: [R(i) for i in range(10)]
            [0, 1, 3, 9, 27, 81, 243, 729, 2187, 6561]
            sage: R.is_quasigeometric()
            True
        """
    def is_arithmetic(self) -> bool:
        """
        Decide whether the sequence is degenerate and an arithmetic sequence.

        The sequence is arithmetic if and only if `u_1 - u_0 = u_2 - u_1 = u_3 - u_2`.

        This corresponds to the matrix `F = [[0,1],[c,b]]` being nondiagonalizable
        and `\\alpha/\\beta = 1`.

        EXAMPLES::

            sage: S = BinaryRecurrenceSequence(2,-1)
            sage: [S(i) for i in range(10)]
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: S.is_arithmetic()
            True
        """
    def period(self, m, *, eventual: bool = False):
        """
        Return the period of the binary recurrence sequence modulo
        an integer ``m``.

        If `n_1` is congruent to `n_2` modulo ``period(m)``, then `u_{n_1}` is
        is congruent to `u_{n_2}` modulo ``m``.

        INPUT:

        - ``m`` -- integer; modulo which the period of the recurrence relation is calculated

        - ``eventual`` -- boolean (default: ``False``); if ``True``, allow the
          sequence to be eventually periodic, rather than requiring it to be
          purely periodic. So `n_1` might not be congruent to `n_2` modulo
          ``period(m)`` unless `n_1` and `n_2` are large.

        OUTPUT: integer (the period of the sequence modulo m)

        EXAMPLES:

        If `p = \\pm 1 \\mod 5`, then the period of the Fibonacci sequence
        mod `p` is `p-1` (c.f. Lemma 3.3 of [BMS2006]_).

        ::

            sage: R = BinaryRecurrenceSequence(1,1)
            sage: R.period(31)
            30

            sage: [R(i) % 4 for i in range(12)]
            [0, 1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1]
            sage: R.period(4)
            6

        This function works for degenerate sequences as well.

        ::

            sage: S = BinaryRecurrenceSequence(2,0,1,2)
            sage: S.is_degenerate()
            True
            sage: S.is_geometric()
            True
            sage: [S(i) % 17 for i in range(16)]
            [1, 2, 4, 8, 16, 15, 13, 9, 1, 2, 4, 8, 16, 15, 13, 9]
            sage: S.period(17)
            8

        Letting ``eventual`` be ``True`` allows us to find the period of a
        sequence that is not purely periodic. ::

            sage: T = BinaryRecurrenceSequence(5,12,u0=0,u1=1)
            sage: [T(n) % 10 for n in range(20)]
            [0, 1, 5, 7, 5, 9, 5, 3, 5, 1, 5, 7, 5, 9, 5, 3, 5, 1, 5, 7]
            sage: T.period(10)
            Traceback (most recent call last):
            ...
            ValueError: Binary recurrence sequence modulo 10 is not a purely
            periodic sequence.
            sage: T.period(10,eventual=True)
            8

        .. NOTE:: The answer is cached.

        TESTS:

        Verify that :issue:`38112` is fixed::

            sage: T = BinaryRecurrenceSequence(3,2,u0=0,u1=1)
            sage: [T(n) % 4 for n in range(5)]
            [0, 1, 3, 3, 3]
            sage: T.period(4)
            Traceback (most recent call last):
            ...
            ValueError: Binary recurrence sequence modulo 4 is not a purely
            periodic sequence.
            sage: T.period(4,eventual=True)
            1
        """
    def pthpowers(self, p, Bound):
        """
        Find the indices of proveably all `p`-th powers in the recurrence sequence
        bounded by Bound.

        Let `u_n` be a binary recurrence sequence.  A ``p`` th power in `u_n`
        is a solution to `u_n = y^p` for some integer `y`.  There are only
        finitely many ``p`` th powers in any recurrence sequence [SS1983]_.

        INPUT:

        - ``p`` -- a rational prime integer (the fixed p in `u_n = y^p`)

        - ``Bound`` -- a natural number (the maximum index `n` in `u_n = y^p` that is checked)

        OUTPUT:

        A list of the indices of all ``p`` th powers less bounded by
        ``Bound``. If the sequence is degenerate and there are many
        ``p`` th powers, raises :exc:`ValueError`.

        EXAMPLES::

            sage: R = BinaryRecurrenceSequence(1,1)        #the Fibonacci sequence
            sage: R.pthpowers(2, 10**10)        # long time (7 seconds) -- in fact these are all squares, c.f. [BMS2006]_
            [0, 1, 2, 12]

            sage: S = BinaryRecurrenceSequence(8,1) #a Lucas sequence
            sage: S.pthpowers(3,10**10)    # long time (3 seconds) -- provably finds the indices of all 3rd powers less than 10^10
            [0, 1, 2]

            sage: Q = BinaryRecurrenceSequence(3,3,2,1)
            sage: Q.pthpowers(11,10**10)          # long time (7.5 seconds)
            [1]

        If the sequence is degenerate, and there are no ``p`` th powers, returns `[]`.  Otherwise, if
        there are many ``p`` th powers, raises :exc:`ValueError`.

        ::

            sage: T = BinaryRecurrenceSequence(2,0,1,2)
            sage: T.is_degenerate()
            True
            sage: T.is_geometric()
            True
            sage: T.pthpowers(7, 10**30)                                                # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: the degenerate binary recurrence sequence is geometric or
            quasigeometric and has many pth powers

            sage: L = BinaryRecurrenceSequence(4,0,2,2)
            sage: [L(i).factor() for i in range(10)]
            [2, 2, 2^3, 2^5, 2^7, 2^9, 2^11, 2^13, 2^15, 2^17]
            sage: L.is_quasigeometric()
            True
            sage: L.pthpowers(2, 10**30)                                                # needs sage.symbolic
            []

        .. NOTE::

            This function is primarily optimized in the range where
            ``Bound`` is much larger than ``p``.
        """
