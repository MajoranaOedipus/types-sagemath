from sage.coding.all import codes as codes
from sage.coding.encoder import Encoder as Encoder
from sage.coding.linear_code import AbstractLinearCode as AbstractLinearCode
from sage.modules.free_module_element import vector as vector

class GoppaCode(AbstractLinearCode):
    """
    Implementation of Goppa codes.

    Goppa codes are a generalization of narrow-sense BCH codes.
    These codes are defined by a generating polynomial `g` over a finite field
    `\\GF{p^m}`, and a defining set `L` of elements from `\\GF{p^m}`, which are not roots
    of `g`. The number of defining elements determines the length of the code.

    In binary cases, the minimum distance is `2t + 1`, where `t` is the degree
    of `g`.

    INPUT:

    - ``generating_pol`` -- a monic polynomial with coefficients in a finite
      field `\\GF{p^m}`, the code is defined over `\\GF{p}`, `p` must be a prime number

    - ``defining_set`` -- set of elements of `\\GF{p^m}` that are not roots
      of `g`, its cardinality is the length of the code

    EXAMPLES::

        sage: F = GF(2^6)
        sage: R.<x> = F[]
        sage: g = x^9 + 1
        sage: L = [a for a in F.list() if g(a) != 0]
        sage: C = codes.GoppaCode(g, L)
        sage: C
        [55, 16] Goppa code over GF(2)
    """
    def __init__(self, generating_pol, defining_set) -> None:
        """
        Initialize.

        TESTS::

            sage: F = GF(2^6)
            sage: R.<x> = F[]
            sage: g = x^9 + 1
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: TestSuite(C).run()
        """
    def __eq__(self, other):
        """
        Test equality with ``other``.

        Two Goppa codes are considered the same when defining sets and
        generating polynomials are the same.

        EXAMPLES::

            sage: F  = GF(2^3)
            sage: R.<x> = F[]
            sage: g = x^2 + x+ 1
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: D = codes.GoppaCode(g, L)
            sage: C == D
            True

        Note that equality check will be false if ``other`` represents the same
        linear code as ``self`` but not constructed as a Goppa code::

            sage: E = LinearCode(C.generator_matrix())
            sage: C == E
            False
        """
    def parity_check_matrix(self):
        """
        Return a parity check matrix for ``self``.

        The element in row `t`, column `i` is `h[i](D[i]^t)`, where:

        - `h[i]` -- is the inverse of `g(D[i])`
        - `D[i]` -- is the `i`-th element of the defining set

        In the resulting `d \\times n` matrix we interpret each entry as an
        `m`-column vector and return a `dm \\times n` matrix.

        EXAMPLES::

            sage: F  = GF(2^3)
            sage: R.<x> = F[]
            sage: g = x^2 + x+ 1
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: C
            [8, 2] Goppa code over GF(2)
            sage: C.parity_check_matrix()
            [1 0 0 0 0 0 0 1]
            [0 0 1 0 1 1 1 0]
            [0 1 1 1 0 0 1 0]
            [0 1 1 1 1 1 1 1]
            [0 1 0 1 1 0 1 0]
            [0 0 1 1 1 1 0 0]
        """
    def distance_bound(self):
        """
        Return a lower bound for the minimum distance of the code.

        Computed using the degree of the generating polynomial of ``self``.
        The minimum distance is guaranteed to be bigger than or equal to this bound.

        EXAMPLES::

            sage: F = GF(2^3)
            sage: R.<x> = F[]
            sage: g = x^2 + x + 1
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: C
            [8, 2] Goppa code over GF(2)
            sage: C.distance_bound()
            3
            sage: C.minimum_distance()                                                  # needs sage.libs.gap
            5
        """

class GoppaCodeEncoder(Encoder):
    """
    Encoder for Goppa codes.

    Encodes words represented as vectors of length `k`, where `k` is
    the dimension of ``self``, with entries from `\\GF{p}`, the prime field of
    the base field of the generating polynomial of ``self``, into codewords
    of length `n`, with entries from `\\GF{p}`.

    EXAMPLES::

        sage: F = GF(2^3)
        sage: R.<x> = F[]
        sage: g = x^2 + x + 1
        sage: L = [a for a in F.list() if g(a) != 0]
        sage: C = codes.GoppaCode(g, L)
        sage: C
        [8, 2] Goppa code over GF(2)
        sage: E = codes.encoders.GoppaCodeEncoder(C)
        sage: E
        Encoder for [8, 2] Goppa code over GF(2)
        sage: word = vector(GF(2), (0, 1))
        sage: c = E.encode(word)
        sage: c
        (0, 1, 1, 1, 1, 1, 1, 0)
        sage: c in C
        True
    """
    def __init__(self, code) -> None:
        """
        Initialize.

        TESTS::

            sage: F = GF(2^3)
            sage: R.<x> = F[]
            sage: g = x^2 + x + 1
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: E = codes.encoders.GoppaCodeEncoder(C)
            sage: TestSuite(E).run()
        """
    def __eq__(self, other):
        """
        Test equality with ``other``.

        EXAMPLES::

            sage: F = GF(2^3)
            sage: R.<x> = F[]
            sage: g = (x^2 + x + 1)^2
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: E1 = codes.encoders.GoppaCodeEncoder(C)
            sage: E2 = codes.encoders.GoppaCodeEncoder(C)
            sage: E1 == E2
            True
        """
    def generator_matrix(self):
        """
        A generator matrix for ``self``.

        Dimension of resulting matrix is `k \\times n`, where `k` is
        the dimension of ``self`` and `n` is the length of ``self``.

        EXAMPLES::

            sage: F = GF(2^3)
            sage: R.<x> = F[]
            sage: g = (x^2 + x + 1)^2
            sage: L = [a for a in F.list() if g(a) != 0]
            sage: C = codes.GoppaCode(g, L)
            sage: C
            [8, 2] Goppa code over GF(2)
            sage: C.generator_matrix()
            [1 0 0 1 0 1 1 1]
            [0 1 1 1 1 1 1 0]
        """
