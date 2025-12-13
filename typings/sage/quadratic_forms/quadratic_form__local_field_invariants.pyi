from sage.arith.misc import hilbert_symbol as hilbert_symbol, prime_divisors as prime_divisors
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def rational_diagonal_form(self, return_matrix: bool = False):
    """
    Return a diagonal form equivalent to the given quadratic from
    over the fraction field of its defining ring.

    INPUT:

    - ``return_matrix`` -- boolean (default: ``False``); also return the
      transformation matrix

    OUTPUT: either the diagonal quadratic form `D` (if ``return_matrix`` is false)
    or the pair `(D, T)` (if ``return_matrix`` is true) where

    - ``D`` -- the diagonalized form of this quadratic form

    - ``T`` -- transformation matrix. This is such that
      ``T.transpose() * self.matrix() * T`` gives ``D.matrix()``

    Both `D` and `T` are defined over the fraction field of the
    base ring of the given form.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [0,1,-1])
        sage: Q
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 0 1 ]
        [ * -1 ]
        sage: Q.rational_diagonal_form()
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1/4 0 ]
        [ * -1 ]

    If we start with a diagonal form, we get back the same form defined
    over the fraction field::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.rational_diagonal_form()
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ 1 0 0 0 ]
        [ * 3 0 0 ]
        [ * * 5 0 ]
        [ * * * 7 ]

    In the following example, we check the consistency of the
    transformation matrix::

        sage: Q = QuadraticForm(ZZ, 4, range(10))
        sage: D, T = Q.rational_diagonal_form(return_matrix=True)
        sage: D
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ -1/16 0 0 0 ]
        [ * 4 0 0 ]
        [ * * 13 0 ]
        [ * * * 563/52 ]
        sage: T
        [     1      0     11 149/26]
        [  -1/8      1     -2 -10/13]
        [     0      0      1 -29/26]
        [     0      0      0      1]
        sage: T.transpose() * Q.matrix() * T
        [  -1/8      0      0      0]
        [     0      8      0      0]
        [     0      0     26      0]
        [     0      0      0 563/26]
        sage: D.matrix()
        [  -1/8      0      0      0]
        [     0      8      0      0]
        [     0      0     26      0]
        [     0      0      0 563/26]

    ::

        sage: Q1 = QuadraticForm(ZZ, 4, [1, 1, 0, 0, 1, 0, 0, 1, 0, 18])
        sage: Q1
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 1 0 0 ]
        [ * 1 0 0 ]
        [ * * 1 0 ]
        [ * * * 18 ]
        sage: Q1.rational_diagonal_form(return_matrix=True)
        (
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ 1 0 0 0 ]
        [ * 3/4 0 0 ]
        [ * * 1 0 ]
        [ * * * 18 ]                                                         ,
        <BLANKLINE>
        [   1 -1/2    0    0]
        [   0    1    0    0]
        [   0    0    1    0]
        [   0    0    0    1]
        )

    PARI returns a singular transformation matrix for this case::

        sage: Q = QuadraticForm(QQ, 2, [1/2, 1, 1/2])
        sage: Q.rational_diagonal_form()
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1/2 0 ]
        [ * 0 ]

    This example cannot be computed by PARI::

        sage: Q = QuadraticForm(RIF, 4, range(10))
        sage: Q.__pari__()
        Traceback (most recent call last):
        ...
        TypeError
        sage: Q.rational_diagonal_form()
        Quadratic form in 4 variables over Real Interval Field with 53 bits of precision
        with coefficients:
        [ 5 0.?e-14 0.?e-13 0.?e-13 ]
        [ * -0.05000000000000? 0.?e-12 0.?e-12 ]
        [ * * 13.00000000000? 0.?e-10 ]
        [ * * * 10.8269230769? ]

    TESTS:

    Changing the output quadratic form does not affect the caching::

        sage: Q, T = Q1.rational_diagonal_form(return_matrix=True)
        sage: Q[0,0] = 13
        sage: Q1.rational_diagonal_form()
        Quadratic form in 4 variables over Rational Field with coefficients:
        [ 1 0 0 0 ]
        [ * 3/4 0 0 ]
        [ * * 1 0 ]
        [ * * * 18 ]

    The transformation matrix is immutable::

        sage: T[0,0] = 13
        Traceback (most recent call last):
        ...
        ValueError: matrix is immutable; please change a copy instead
        (i.e., use copy(M) to change a copy of M).

    Test for a singular form::

        sage: m = matrix(GF(11), [[1,5,0,0], [5,1,9,0], [0,9,1,5], [0,0,5,1]])
        sage: qf = QuadraticForm(m)
        sage: Q, T = qf.rational_diagonal_form(return_matrix=True)
        sage: T
        [ 1  6  5 10]
        [ 0  1 10  9]
        [ 0  0  1  2]
        [ 0  0  0  1]
    """
def signature_vector(self):
    """
    Return the triple `(p, n, z)` of integers where

    - `p` = number of positive eigenvalues
    - `n` = number of negative eigenvalues
    - `z` = number of zero eigenvalues

    for the symmetric matrix associated to `Q`.

    OUTPUT: a triple of integers `\\geq 0`

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,0,0,-4])
        sage: Q.signature_vector()
        (1, 1, 2)

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,-3,-4])
        sage: Q.signature_vector()
        (2, 2, 0)

    ::

        sage: Q = QuadraticForm(ZZ, 4, range(10)); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 0 1 2 3 ]
        [ * 4 5 6 ]
        [ * * 7 8 ]
        [ * * * 9 ]
        sage: Q.signature_vector()
        (3, 1, 0)
    """
def signature(self):
    """
    Return the signature of the quadratic form, defined as:

       number of positive eigenvalues `-` number of negative eigenvalues

    of the matrix of the quadratic form.

    OUTPUT: integer

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,0,0,-4,3,11,3])
        sage: Q.signature()
        3

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,2,-3,-4])
        sage: Q.signature()
        0

    ::

        sage: Q = QuadraticForm(ZZ, 4, range(10)); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 0 1 2 3 ]
        [ * 4 5 6 ]
        [ * * 7 8 ]
        [ * * * 9 ]
        sage: Q.signature()
        2
    """
def hasse_invariant(self, p):
    """
    Compute the Hasse invariant at a prime `p` or at infinity, as given on p55 of
    Cassels's book.  If `Q` is diagonal with coefficients `a_i`, then the
    (Cassels) Hasse invariant is given by

    .. MATH::

        c_p = \\prod_{i < j} (a_i, a_j)_p

    where `(a,b)_p` is the Hilbert symbol at `p`.  The underlying
    quadratic form must be non-degenerate over `\\QQ_p` for this to make
    sense.

    .. WARNING::

        This is different from the O'Meara Hasse invariant, which
        allows `i \\leq j` in the product.  That is given by the method
        :meth:`hasse_invariant__OMeara`.

    .. NOTE::

        We should really rename this ``hasse_invariant__Cassels``, and
        set :meth:`hasse_invariant` as a front-end to it.

    INPUT:

    - ``p`` -- a prime number > 0 or `-1` for the infinite place

    OUTPUT: `1` or `-1`

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
        sage: Q.rational_diagonal_form()
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1 0 ]
        [ * 2 ]
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1])
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [-1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1,5])
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [-1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 23)                                             # needs sage.rings.number_field
        sage: Q = DiagonalQuadraticForm(K, [-a, a + 2])                                 # needs sage.rings.number_field
        sage: [Q.hasse_invariant(p) for p in K.primes_above(19)]                        # needs sage.rings.number_field
        [-1, 1]
    """
def hasse_invariant__OMeara(self, p):
    """
    Compute the O'Meara Hasse invariant at a prime `p`.

    This is defined on
    p167 of O'Meara's book. If `Q` is diagonal with coefficients `a_i`,
    then the (Cassels) Hasse invariant is given by

    .. MATH::

        c_p = \\prod_{i \\leq j} (a_i, a_j)_p

    where `(a,b)_p` is the Hilbert symbol at `p`.

    .. WARNING::

        This is different from the (Cassels) Hasse invariant, which
        only allows `i < j` in the product.  That is given by the method
        hasse_invariant(p).

    INPUT:

    - ``p`` -- a prime number > 0 or `-1` for the infinite place

    OUTPUT: `1` or `-1`

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
        sage: Q.rational_diagonal_form()
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1 0 ]
        [ * 2 ]
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1])
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [-1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: Q = DiagonalQuadraticForm(ZZ,[1,-1,-1])
        sage: [Q.hasse_invariant(p) for p in prime_range(20)]                           # needs sage.libs.pari
        [-1, 1, 1, 1, 1, 1, 1, 1]
        sage: [Q.hasse_invariant__OMeara(p) for p in prime_range(20)]                   # needs sage.libs.pari
        [-1, 1, 1, 1, 1, 1, 1, 1]

    ::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 23)                                             # needs sage.rings.number_field
        sage: Q = DiagonalQuadraticForm(K, [-a, a + 2])                                 # needs sage.rings.number_field
        sage: [Q.hasse_invariant__OMeara(p) for p in K.primes_above(19)]                # needs sage.rings.number_field
        [1, 1]
    """
def is_hyperbolic(self, p) -> bool:
    '''
    Check if the quadratic form is a sum of hyperbolic planes over
    the `p`-adic numbers `\\QQ_p` or over the real numbers `\\RR`.

    REFERENCES:

    This criterion follows from Cassels\'s "Rational Quadratic Forms":

    - local invariants for hyperbolic plane (Lemma 2.4, p58)
    - direct sum formulas (Lemma 2.3, p58)

    INPUT:

    - ``p`` -- a prime number > 0 or `-1` for the infinite place

    OUTPUT: boolean

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q.is_hyperbolic(-1)
        False
        sage: Q.is_hyperbolic(2)
        False
        sage: Q.is_hyperbolic(3)
        False
        sage: Q.is_hyperbolic(5)     # Here -1 is a square, so it\'s true.
        True
        sage: Q.is_hyperbolic(7)
        False
        sage: Q.is_hyperbolic(13)    # Here -1 is a square, so it\'s true.
        True
    '''
def is_anisotropic(self, p) -> bool:
    """
    Check if the quadratic form is anisotropic over the `p`-adic numbers `\\QQ_p` or `\\RR`.

    INPUT:

    - ``p`` -- a prime number > 0 or `-1` for the infinite place

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q.is_anisotropic(2)                                                       # needs sage.libs.pari
        True
        sage: Q.is_anisotropic(3)                                                       # needs sage.libs.pari
        True
        sage: Q.is_anisotropic(5)                                                       # needs sage.libs.pari
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1])
        sage: Q.is_anisotropic(2)                                                       # needs sage.libs.pari
        False
        sage: Q.is_anisotropic(3)                                                       # needs sage.libs.pari
        False
        sage: Q.is_anisotropic(5)                                                       # needs sage.libs.pari
        False

    ::

        sage: [DiagonalQuadraticForm(ZZ,                                                # needs sage.libs.pari
        ....:                        [1, -least_quadratic_nonresidue(p)]).is_anisotropic(p)
        ....:  for p in prime_range(3, 30)]
        [True, True, True, True, True, True, True, True, True]

    ::

        sage: [DiagonalQuadraticForm(ZZ, [1, -least_quadratic_nonresidue(p),            # needs sage.libs.pari
        ....:                             p, -p*least_quadratic_nonresidue(p)]).is_anisotropic(p)
        ....:  for p in prime_range(3, 30)]
        [True, True, True, True, True, True, True, True, True]
    """
def is_isotropic(self, p) -> bool:
    """
    Check if `Q` is isotropic over the `p`-adic numbers `\\QQ_p` or `\\RR`.

    INPUT:

    - ``p`` -- a prime number > 0 or `-1` for the infinite place

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q.is_isotropic(2)                                                         # needs sage.libs.pari
        False
        sage: Q.is_isotropic(3)                                                         # needs sage.libs.pari
        False
        sage: Q.is_isotropic(5)                                                         # needs sage.libs.pari
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1])
        sage: Q.is_isotropic(2)                                                         # needs sage.libs.pari
        True
        sage: Q.is_isotropic(3)                                                         # needs sage.libs.pari
        True
        sage: Q.is_isotropic(5)                                                         # needs sage.libs.pari
        True

    ::

        sage: [DiagonalQuadraticForm(ZZ,                                                # needs sage.libs.pari
        ....:                        [1, -least_quadratic_nonresidue(p)]).is_isotropic(p)
        ....:  for p in prime_range(3, 30)]
        [False, False, False, False, False, False, False, False, False]

    ::

        sage: [DiagonalQuadraticForm(ZZ, [1, -least_quadratic_nonresidue(p),            # needs sage.libs.pari
        ....:                             p, -p*least_quadratic_nonresidue(p)]).is_isotropic(p)
        ....:  for p in prime_range(3, 30)]
        [False, False, False, False, False, False, False, False, False]
    """
def anisotropic_primes(self):
    """
    Return a list with all of the anisotropic primes of the quadratic form.

    The infinite place is denoted by `-1`.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.anisotropic_primes()                                                    # needs sage.libs.pari
        [2, -1]

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.anisotropic_primes()                                                    # needs sage.libs.pari
        [2, -1]

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,1])
        sage: Q.anisotropic_primes()                                                    # needs sage.libs.pari
        [-1]
    """
def compute_definiteness(self) -> None:
    '''
    Compute whether the given quadratic form is positive-definite,
    negative-definite, indefinite, degenerate, or the zero form.

    This caches one of the following strings in ``self.__definiteness_string``:
    "pos_def", "neg_def", "indef", "zero", "degenerate".  It is called
    from all routines like: :meth:`is_positive_definite`, :meth:`is_negative_definite`,
    :meth:`is_indefinite`, etc.

    .. NOTE::

        A degenerate form is considered neither definite nor indefinite.

    .. NOTE::

        The zero-dimensional form is considered both positive definite and negative definite.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,1])
        sage: Q.compute_definiteness()
        sage: Q.is_positive_definite()
        True
        sage: Q.is_negative_definite()
        False
        sage: Q.is_indefinite()
        False
        sage: Q.is_definite()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [])
        sage: Q.compute_definiteness()
        sage: Q.is_positive_definite()
        True
        sage: Q.is_negative_definite()
        True
        sage: Q.is_indefinite()
        False
        sage: Q.is_definite()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,0,-1])
        sage: Q.compute_definiteness()
        sage: Q.is_positive_definite()
        False
        sage: Q.is_negative_definite()
        False
        sage: Q.is_indefinite()
        False
        sage: Q.is_definite()
        False
    '''
def compute_definiteness_string_by_determinants(self):
    """
    Compute the (positive) definiteness of a quadratic form by looking
    at the signs of all of its upper-left subdeterminants.  See also
    :meth:`compute_definiteness` for more documentation.

    OUTPUT: string describing the definiteness

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,1])
        sage: Q.compute_definiteness_string_by_determinants()
        'pos_def'

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [])
        sage: Q.compute_definiteness_string_by_determinants()
        'zero'

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,0,-1])
        sage: Q.compute_definiteness_string_by_determinants()
        'degenerate'

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-1])
        sage: Q.compute_definiteness_string_by_determinants()
        'indefinite'

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [-1,-1])
        sage: Q.compute_definiteness_string_by_determinants()
        'neg_def'
    """
def is_positive_definite(self) -> bool:
    """
    Determine if the given quadratic form is positive-definite.

    .. NOTE::

        A degenerate form is considered neither definite nor indefinite.

    .. NOTE::

        The zero-dimensional form is considered both positive definite and negative definite.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5])
        sage: Q.is_positive_definite()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-3,5])
        sage: Q.is_positive_definite()
        False
    """
def is_negative_definite(self) -> bool:
    """
    Determine if the given quadratic form is negative-definite.

    .. NOTE::

        A degenerate form is considered neither definite nor indefinite.

    .. NOTE::

        The zero-dimensional form is considered both positive definite and negative definite.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [-1,-3,-5])
        sage: Q.is_negative_definite()
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-3,5])
        sage: Q.is_negative_definite()
        False
    """
def is_indefinite(self) -> bool:
    """
    Determine if the given quadratic form is indefinite.

    .. NOTE::

        A degenerate form is considered neither definite nor indefinite.

    .. NOTE::

        The zero-dimensional form is not considered indefinite.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [-1,-3,-5])
        sage: Q.is_indefinite()
        False

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-3,5])
        sage: Q.is_indefinite()
        True
    """
def is_definite(self) -> bool:
    """
    Determine if the given quadratic form is (positive or negative) definite.

    .. NOTE::

        A degenerate form is considered neither definite nor indefinite.

    .. NOTE::

        The zero-dimensional form is considered indefinite.

    OUTPUT: boolean

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [-1,-3,-5])
        sage: Q.is_definite()
        True

        sage: Q = DiagonalQuadraticForm(ZZ, [1,-3,5])
        sage: Q.is_definite()
        False
    """
