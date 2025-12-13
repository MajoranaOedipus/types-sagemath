from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix
from sage.structure.sage_object import SageObject as SageObject

def lifting(p, t, A, G):
    """
    Compute generators of `\\{f \\in D[X]^d \\mid Af \\equiv 0 \\pmod{p^{t}}\\}` given
    generators of `\\{f\\in D[X]^d \\mid Af \\equiv 0\\pmod{p^{t-1}}\\}`.

    INPUT:

    - ``p`` -- a prime element of some principal ideal domain `D`

    - ``t`` -- nonnegative integer

    - ``A`` -- a `c\\times d` matrix over `D[X]`

    - ``G`` -- a matrix over `D[X]`. The columns of
      `\\begin{pmatrix}p^{t-1}I& G\\end{pmatrix}` are generators
      of `\\{ f\\in D[X]^d \\mid Af \\equiv 0\\pmod{p^{t-1}}\\}`;
      can be set to ``None`` if ``t`` is zero

    OUTPUT:

    A matrix `F` over `D[X]` such that the columns of
    `\\begin{pmatrix}p^tI&F&pG\\end{pmatrix}` are generators of
    `\\{ f\\in D[X]^d \\mid Af \\equiv 0\\pmod{p^t}\\}`.

    EXAMPLES::

        sage: from sage.matrix.compute_J_ideal import lifting
        sage: X = polygen(ZZ, 'X')
        sage: A = matrix([[1, X], [2*X, X^2]])
        sage: G0 = lifting(5, 0, A, None)
        sage: G1 = lifting(5, 1, A, G0); G1
        []
        sage: (A*G1 % 5).is_zero()
        True
        sage: A = matrix([[1, X, X^2], [2*X, X^2, 3*X^3]])
        sage: G0 = lifting(5, 0, A, None)
        sage: G1 = lifting(5, 1, A, G0); G1
        [3*X^2]
        [    X]
        [    1]
        sage: (A*G1 % 5).is_zero()
        True
        sage: G2 = lifting(5, 2, A, G1); G2
        [15*X^2 23*X^2]
        [   5*X      X]
        [     5      1]
        sage: (A*G2 % 25).is_zero()
        True
        sage: lifting(5, 10, A, G1)
        Traceback (most recent call last):
        ...
        ValueError: A*G not zero mod 5^9

    ALGORITHM:

    [HR2016]_, Algorithm 1.

    TESTS::

        sage: A = matrix([[1, X], [X, X^2]])
        sage: G0 = lifting(5, 0, A, None)
        sage: G1 = lifting(5, 1, A, G0); G1
        Traceback (most recent call last):
        ...
        ValueError: [  1   X|]
        [  X X^2|] does not have full rank.
    """
def p_part(f, p):
    """
    Compute the `p`-part of a polynomial.

    INPUT:

    - ``f`` -- a polynomial over `D`

    - ``p`` -- a prime in `D`

    OUTPUT:

    A polynomial `g` such that `\\deg g \\le \\deg f` and
    all nonzero coefficients of `f - p g` are not divisible by `p`.

    EXAMPLES::

        sage: from sage.matrix.compute_J_ideal import p_part
        sage: X = polygen(ZZ, 'X')
        sage: f = X^3 + 5*X + 25
        sage: g = p_part(f, 5); g
        X + 5
        sage: f - 5*g
        X^3

    TESTS:

    Return value is supposed to be a polynomial, see :issue:`22402`

        sage: g = p_part(X+1, 2)
        sage: g.parent()
        Univariate Polynomial Ring in X over Integer Ring
    """

class ComputeMinimalPolynomials(SageObject):
    """
    Create an object for computing `(p^t)`-minimal polynomials and `J`-ideals.

    For an ideal `J` and a square matrix `B` over a principal ideal
    domain `D`, the `J`-ideal of `B` is defined to be
    `N_J(B) = \\{ f\\in D[X] \\mid f(B) \\in M_n(J) \\}`.

    For a prime element `p` of `D` and `t\\ge 0`, a `(p^t)`-minimal
    polynomial of `B` is a monic polynomial `f\\in N_{(p^t)}(B)` of
    minimal degree.

    The characteristic polynomial of `B` is denoted by `\\chi_B`; `n`
    is the size of `B`.

    INPUT:

    - ``B`` -- a square matrix over a principal ideal domain `D`

    OUTPUT:

    An object which allows to call :meth:`p_minimal_polynomials`,
    :meth:`null_ideal` and :meth:`integer_valued_polynomials_generators`.

    EXAMPLES::

        sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
        sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
        sage: C = ComputeMinimalPolynomials(B)
        sage: C.prime_candidates()
        [2, 3, 5]
        sage: for t in range(4):
        ....:     print(C.null_ideal(2^t))
        Principal ideal (1) of
            Univariate Polynomial Ring in x over Integer Ring
        Ideal (2, x^2 + x) of
            Univariate Polynomial Ring in x over Integer Ring
        Ideal (4, x^2 + 3*x + 2) of
            Univariate Polynomial Ring in x over Integer Ring
        Ideal (8, x^3 + x^2 - 12*x - 20, 2*x^2 + 6*x + 4) of
            Univariate Polynomial Ring in x over Integer Ring
        sage: C.p_minimal_polynomials(2)
        {2: x^2 + 3*x + 2}
        sage: C.integer_valued_polynomials_generators()
        (x^3 + x^2 - 12*x - 20, [1, 1/4*x^2 + 3/4*x + 1/2])
    """
    chi_B: Incomplete
    mu_B: Incomplete
    def __init__(self, B) -> None:
        """
        Initialize the ComputeMinimalPolynomials class.

        INPUT:

        - ``B`` -- a square matrix

        TESTS::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: ComputeMinimalPolynomials(matrix([[1, 2]]))
            Traceback (most recent call last):
            ...
            TypeError: square matrix required
        """
    def find_monic_replacements(self, p, t, pt_generators, prev_nu):
        """
        Replace possibly non-monic generators of `N_{(p^t)}(B)` by monic
        generators.

        INPUT:

        - ``p`` -- a prime element of `D`

        - ``t`` -- nonnegative integer

        - ``pt_generators`` -- list `(g_1, \\ldots, g_s)` of polynomials in
          `D[X]` such that `N_{(p^t)}(B) = (g_1, \\ldots, g_s) + pN_{(p^{t-1})}(B)`

        - ``prev_nu`` -- a `(p^{t-1})`-minimal polynomial of `B`

        OUTPUT:

        A list `(h_1, \\ldots, h_r)` of monic polynomials such that
        `N_{(p^t)}(B) = (h_1, \\ldots, h_r) + pN_{(p^{t-1})}(B)`.

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: x = polygen(ZZ, 'x')
            sage: nu_1 = x^2 + x
            sage: generators_4 = [2*x^2 + 2*x, x^2 + 3*x + 2]
            sage: C.find_monic_replacements(2, 2, generators_4, nu_1)
            [x^2 + 3*x + 2]

        TESTS::

            sage: C.find_monic_replacements(2, 3, generators_4, nu_1)
            Traceback (most recent call last):
            ...
            ValueError: [2*x^2 + 2*x, x^2 + 3*x + 2] not in N_{(2^3)}(B)
            sage: C.find_monic_replacements(2, 2, generators_4, x^2)
            Traceback (most recent call last):
            ...
            ValueError: x^2 not in N_{(2^1)}(B)

        ALGORITHM:

        [HR2016]_, Algorithms 2 and 3.
        """
    def current_nu(self, p, t, pt_generators, prev_nu):
        """
        Compute `(p^t)`-minimal polynomial of `B`.

        INPUT:

        - ``p`` -- a prime element of `D`

        - ``t`` -- positive integer

        - ``pt_generators`` -- list `(g_1, \\ldots, g_s)` of polynomials in
          `D[X]` such that `N_{(p^t)}(B) = (g_1, \\ldots, g_s) + pN_{(p^{t-1})}(B)`

        - ``prev_nu`` -- a `(p^{t-1})`-minimal polynomial of `B`

        OUTPUT:

        A `(p^t)`-minimal polynomial of `B`.

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: x = polygen(ZZ, 'x')
            sage: nu_1 = x^2 + x
            sage: generators_4 = [2*x^2 + 2*x, x^2 + 3*x + 2]
            sage: C.current_nu(2, 2, generators_4, nu_1)
            x^2 + 3*x + 2

        ALGORITHM:

        [HR2016]_, Algorithm 4.

        TESTS::

            sage: C.current_nu(2, 3, generators_4, nu_1)
            Traceback (most recent call last):
            ...
            ValueError: [2*x^2 + 2*x, x^2 + 3*x + 2] not in N_{(2^3)}(B)
            sage: C.current_nu(2, 2, generators_4, x^2)
            Traceback (most recent call last):
            ...
            ValueError: x^2 not in N_{(2^1)}(B)
        """
    def mccoy_column(self, p, t, nu):
        """
        Compute matrix for McCoy's criterion.

        INPUT:

        - ``p`` -- a prime element in `D`

        - ``t`` -- positive integer

        - ``nu`` -- a `(p^t)`-minimal polynomial of `B`

        OUTPUT:

        An `(n^2 + 1) \\times 1` matrix `g` with first entry ``nu`` such that
        `\\begin{pmatrix}b& -\\chi_B I\\end{pmatrix}g \\equiv 0\\pmod{p^t}` where `b`
        consists of the entries of `\\operatorname{adj}(X-B)`.

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: x = polygen(ZZ, 'x')
            sage: nu_4 = x^2 + 3*x + 2
            sage: g = C.mccoy_column(2, 2, nu_4)
            sage: b = matrix(9, 1, (x - B).adjugate().list())
            sage: M = matrix.block([[b, -B.charpoly(x)*matrix.identity(9)]])
            sage: (M*g % 4).is_zero()
            True

        ALGORITHM:

        [HR2016]_, Algorithm 5.

        TESTS::

            sage: nu_2 = x^2 + x
            sage: C.mccoy_column(2, 2, nu_2)
            Traceback (most recent call last):
            ...
            ValueError: x^2 + x not in (2^2)-ideal
        """
    def p_minimal_polynomials(self, p, s_max=None):
        """
        Compute `(p^s)`-minimal polynomials `\\nu_s` of `B`.

        Compute a finite subset `\\mathcal{S}` of the positive
        integers and `(p^s)`-minimal polynomials
        `\\nu_s` for `s \\in \\mathcal{S}`.

        For `0 < t \\le \\max \\mathcal{S}`, a `(p^t)`-minimal polynomial is
        given by `\\nu_s` where
        `s = \\min\\{ r \\in \\mathcal{S} \\mid r\\ge t \\}`.
        For `t > \\max \\mathcal{S}`, the minimal polynomial of `B` is
        also a `(p^t)`-minimal polynomial.

        INPUT:

        - ``p`` -- a prime in `D`

        - ``s_max`` -- positive integer (default: ``None``); if set, only
          `(p^s)`-minimal polynomials for ``s <= s_max`` are computed
          (see below for details)

        OUTPUT:

        A dictionary. Keys are the finite set `\\mathcal{S}`, the values
        are the associated `(p^s)`-minimal polynomials `\\nu_s`,
        `s \\in \\mathcal{S}`.

        Setting ``s_max`` only affects the output if ``s_max`` is at
        most `\\max\\mathcal{S}` where `\\mathcal{S}` denotes the full
        set. In that case, only those `\\nu_s` with ``s <= s_max`` are
        returned where ``s_max`` is always included even if it is not
        included in the full set `\\mathcal{S}`.

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: C.p_minimal_polynomials(2)
            {2: x^2 + 3*x + 2}
            sage: set_verbose(1)
            sage: C = ComputeMinimalPolynomials(B)
            sage: C.p_minimal_polynomials(2)
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            p = 2, t = 1:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            Result of lifting:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            F =
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            [x^2 + x]
            [      x]
            [      0]
            [      1]
            [      1]
            [  x + 1]
            [      1]
            [      0]
            [      0]
            [  x + 1]
            verbose 1 (...: compute_J_ideal.py, current_nu)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, current_nu)
            (x^2 + x)
            verbose 1 (...: compute_J_ideal.py, current_nu)
            Generators with (p^t)-generating property:
            verbose 1 (...: compute_J_ideal.py, current_nu)
            [x^2 + x]
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            nu = x^2 + x
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            corresponding columns for G
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            [x^2 + x]
            [  x + 2]
            [      0]
            [      1]
            [      1]
            [  x - 1]
            [     -1]
            [     10]
            [      0]
            [  x + 1]
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            p = 2, t = 2:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            Result of lifting:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            F =
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            [  2*x^2 + 2*x x^2 + 3*x + 2]
            [          2*x         x + 4]
            [            0             0]
            [            2             1]
            [            2             1]
            [      2*x + 2         x + 1]
            [            2            -1]
            [            0            10]
            [            0             0]
            [      2*x + 2         x + 3]
            verbose 1 (...: compute_J_ideal.py, current_nu)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, current_nu)
            (2*x^2 + 2*x, x^2 + 3*x + 2)
            verbose 1 (...: compute_J_ideal.py, current_nu)
            Generators with (p^t)-generating property:
            verbose 1 (...: compute_J_ideal.py, current_nu)
            [x^2 + 3*x + 2]
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            nu = x^2 + 3*x + 2
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            corresponding columns for G
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            [x^2 + 3*x + 2]
            [        x + 4]
            [            0]
            [            1]
            [            1]
            [        x + 1]
            [           -1]
            [           10]
            [            0]
            [        x + 3]
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            p = 2, t = 3:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            Result of lifting:
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            F =
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            [x^3 + 7*x^2 + 6*x x^3 + 3*x^2 + 2*x]
            [        x^2 + 8*x         x^2 + 4*x]
            [                0                 0]
            [                x             x + 4]
            [            x + 4                 x]
            [    x^2 + 5*x + 4           x^2 + x]
            [           -x + 4                -x]
            [             10*x              10*x]
            [                0                 0]
            [        x^2 + 7*x     x^2 + 3*x + 4]
            verbose 1 (...: compute_J_ideal.py, current_nu)
            ------------------------------------------
            verbose 1 (...: compute_J_ideal.py, current_nu)
            (x^3 + 7*x^2 + 6*x, x^3 + 3*x^2 + 2*x)
            verbose 1 (...: compute_J_ideal.py, current_nu)
            Generators with (p^t)-generating property:
            verbose 1 (...: compute_J_ideal.py, current_nu)
            ...
            verbose 1 (...: compute_J_ideal.py, current_nu)
            [x^3 + 3*x^2 + 2*x]
            verbose 1 (...: compute_J_ideal.py, p_minimal_polynomials)
            nu = x^3 + 3*x^2 + 2*x
            {2: x^2 + 3*x + 2}
            sage: set_verbose(0)
            sage: C.p_minimal_polynomials(2, s_max=1)
            {1: x^2 + x}
            sage: C.p_minimal_polynomials(2, s_max=2)
            {2: x^2 + 3*x + 2}
            sage: C.p_minimal_polynomials(2, s_max=3)
            {2: x^2 + 3*x + 2}

        ALGORITHM:

        [HR2016]_, Algorithm 5.
        """
    def null_ideal(self, b: int = 0):
        """
        Return the `(b)`-ideal `N_{(b)}(B)=\\{f\\in D[X] \\mid f(B)\\in M_n(bD)\\}`.

        INPUT:

        - ``b`` -- an element of `D` (default: 0)

        OUTPUT: an ideal in `D[X]`

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: C.null_ideal()
            Principal ideal (x^3 + x^2 - 12*x - 20) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: C.null_ideal(2)
            Ideal (2, x^2 + x) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: C.null_ideal(4)
            Ideal (4, x^2 + 3*x + 2) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: C.null_ideal(8)
            Ideal (8, x^3 + x^2 - 12*x - 20, 2*x^2 + 6*x + 4) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: C.null_ideal(3)
            Ideal (3, x^3 + x^2 - 12*x - 20) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: C.null_ideal(6)
            Ideal (6, 2*x^3 + 2*x^2 - 24*x - 40, 3*x^2 + 3*x) of
                Univariate Polynomial Ring in x over Integer Ring
        """
    def prime_candidates(self):
        """
        Determine those primes `p` where `\\mu_B` might not be a
        `(p)`-minimal polynomial.

        OUTPUT: list of primes

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: C.prime_candidates()
            [2, 3, 5]
            sage: C.p_minimal_polynomials(2)
            {2: x^2 + 3*x + 2}
            sage: C.p_minimal_polynomials(3)
            {}
            sage: C.p_minimal_polynomials(5)
            {}

        This means that `3` and `5` were candidates, but actually, `\\mu_B` turns
        out to be a `(3)`-minimal polynomial and a `(5)`-minimal polynomial.
        """
    def integer_valued_polynomials_generators(self):
        """
        Determine the generators of the ring of integer valued polynomials on `B`.

        OUTPUT:

        A pair ``(mu_B, P)`` where ``P`` is a list of polynomials in `K[X]`
        such that

        .. MATH::

           \\{f \\in K[X] \\mid f(B) \\in M_n(D)\\} = \\mu_B K[X]
               + \\sum_{g\\in P} g D[X]

        where `K` denotes the fraction field of `D`.

        EXAMPLES::

            sage: from sage.matrix.compute_J_ideal import ComputeMinimalPolynomials
            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: C = ComputeMinimalPolynomials(B)
            sage: C.integer_valued_polynomials_generators()
            (x^3 + x^2 - 12*x - 20, [1, 1/4*x^2 + 3/4*x + 1/2])
        """
