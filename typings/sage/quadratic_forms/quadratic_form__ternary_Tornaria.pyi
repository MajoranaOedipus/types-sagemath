from sage.arith.misc import CRT_vectors as CRT_vectors, factor as factor, gcd as gcd, hilbert_symbol as hilbert_symbol, prime_to_m_part as prime_to_m_part
from sage.misc.functional import is_odd as is_odd
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ

def disc(self):
    """
    Return the discriminant of the quadratic form, defined as

    - `(-1)^n {\\rm det}(B)` for even dimension `2n`
    - `{\\rm det}(B)/2` for odd dimension

    where `2Q(x) = x^t B x`.

    This agrees with the usual discriminant for binary and ternary quadratic forms.

    EXAMPLES::

        sage: DiagonalQuadraticForm(ZZ, [1]).disc()
        1
        sage: DiagonalQuadraticForm(ZZ, [1,1]).disc()
        -4
        sage: DiagonalQuadraticForm(ZZ, [1,1,1]).disc()
        4
        sage: DiagonalQuadraticForm(ZZ, [1,1,1,1]).disc()
        16
    """
def content(self):
    """
    Return the GCD of the coefficients of the quadratic form.

    .. warning::

        Only works over Euclidean domains (probably just `\\ZZ`).

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1, 1])
        sage: Q.matrix().gcd()
        2
        sage: Q.content()
        1
        sage: DiagonalQuadraticForm(ZZ, [1, 1]).is_primitive()
        True
        sage: DiagonalQuadraticForm(ZZ, [2, 4]).is_primitive()
        False
        sage: DiagonalQuadraticForm(ZZ, [2, 4]).primitive()
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 1 0 ]
        [ * 2 ]
    """
def adjoint(self):
    """
    Return the adjoint (integral) quadratic form associated to the
    given form, essentially defined by taking the adjoint of the matrix.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1,2,5])
        sage: Q.adjoint()
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 5 -2 ]
        [ * 1 ]

    ::

        sage: Q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q.adjoint()
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 39 2 8 ]
        [ * 19 4 ]
        [ * * 8 ]
    """
def antiadjoint(self):
    """
    This gives an (integral) form such that its adjoint is the given form.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q.adjoint().antiadjoint()
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 0 -1 ]
        [ * 2 -1 ]
        [ * * 5 ]
        sage: Q.antiadjoint()                                                           # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: not an adjoint
    """
def is_adjoint(self) -> bool:
    """
    Determine if the given form is the adjoint of another form.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q.is_adjoint()                                                            # needs sage.symbolic
        False
        sage: Q.adjoint().is_adjoint()
        True
    """
def reciprocal(self):
    """
    This gives the reciprocal quadratic form associated to the given form.

    This is defined as the multiple of the primitive adjoint with the same
    content as the given form.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,37])
        sage: Q.reciprocal()
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 37 0 0 ]
        [ * 37 0 ]
        [ * * 1 ]
        sage: Q.reciprocal().reciprocal()
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 0 0 ]
        [ * 1 0 ]
        [ * * 37 ]
        sage: Q.reciprocal().reciprocal() == Q
        True
    """
def omega(self):
    '''
    Return the content of the adjoint of the primitive associated quadratic form.

    Ref: See Dickson\'s "Studies in Number Theory".

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,37])
        sage: Q.omega()
        4
    '''
def delta(self):
    """
    Return the omega of the adjoint form.

    This is the same as the omega of the reciprocal form.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,37])
        sage: Q.delta()
        148
    """
def level__Tornaria(self):
    """
    Return the level of the quadratic form.

    This is defined as

    - level(`B`)    for even dimension,
    - level(`B`)/4  for odd dimension,

    where `2Q(x) = x^t\\cdot B\\cdot x`.

    This agrees with the usual level for even dimension.

    EXAMPLES::

        sage: DiagonalQuadraticForm(ZZ, [1]).level__Tornaria()
        1
        sage: DiagonalQuadraticForm(ZZ, [1,1]).level__Tornaria()
        4
        sage: DiagonalQuadraticForm(ZZ, [1,1,1]).level__Tornaria()
        1
        sage: DiagonalQuadraticForm(ZZ, [1,1,1,1]).level__Tornaria()
        4
    """
def discrec(self):
    """
    Return the discriminant of the reciprocal form.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,37])
        sage: Q.disc()
        148
        sage: Q.discrec()
        5476
        sage: [4 * 37, 4 * 37^2]
        [148, 5476]
    """
def hasse_conductor(self):
    """
    Return the Hasse conductor.

    This is the product of all primes where the Hasse invariant equals `-1`.

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q.hasse_invariant(2)
        -1
        sage: Q.hasse_invariant(37)
        -1
        sage: Q.hasse_conductor()
        74

        sage: DiagonalQuadraticForm(ZZ, [1, 1, 1]).hasse_conductor()                    # needs sage.libs.pari
        1
        sage: QuadraticForm(ZZ, 3, [2, -2, 0, 2, 0, 5]).hasse_conductor()               # needs sage.libs.pari
        10
    """
def clifford_invariant(self, p):
    """
    Return the Clifford invariant.

    This is the class in the Brauer group of the Clifford algebra for
    even dimension, of the even Clifford Algebra for odd dimension.

    See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula
    relating it to the Hasse invariant.

    EXAMPLES:

    For hyperbolic spaces, the Clifford invariant is +1::

        sage: # needs sage.libs.pari
        sage: H = QuadraticForm(ZZ, 2, [0, 1, 0])
        sage: H.clifford_invariant(2)
        1
        sage: (H + H).clifford_invariant(2)
        1
        sage: (H + H + H).clifford_invariant(2)
        1
        sage: (H + H + H + H).clifford_invariant(2)
        1
    """
def clifford_conductor(self):
    """
    Return the product of all primes where the Clifford invariant is `-1`.

    .. NOTE::

        For ternary forms, this is the discriminant of the
        quaternion algebra associated to the quadratic space
        (i.e. the even Clifford algebra).

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q.clifford_invariant(2)
        1
        sage: Q.clifford_invariant(37)
        -1
        sage: Q.clifford_conductor()
        37

        sage: DiagonalQuadraticForm(ZZ, [1, 1, 1]).clifford_conductor()                 # needs sage.libs.pari
        2
        sage: QuadraticForm(ZZ, 3, [2, -2, 0, 2, 0, 5]).clifford_conductor()            # needs sage.libs.pari
        30

    For hyperbolic spaces, the Clifford conductor is 1::

        sage: # needs sage.libs.pari
        sage: H = QuadraticForm(ZZ, 2, [0, 1, 0])
        sage: H.clifford_conductor()
        1
        sage: (H + H).clifford_conductor()
        1
        sage: (H + H + H).clifford_conductor()
        1
        sage: (H + H + H + H).clifford_conductor()
        1
    """
def basiclemma(self, M):
    """
    Find a number represented by ``self`` and coprime to `M`.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [2, 1, 3])
        sage: Q.basiclemma(6)
        71
    """
def basiclemmavec(self, M):
    """
    Find a vector where the value of the quadratic form is coprime to `M`.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [2, 1, 5])
        sage: Q.basiclemmavec(10)
        (6, 5)
        sage: Q(_)
        227
    """
def xi(self, p):
    '''
    Return the value of the genus characters Xi_p... which may be missing one character.
    We allow -1 as a prime.

    REFERENCES:

    Dickson\'s "Studies in the Theory of Numbers"

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 1, 1, 14, 3, 14])
        sage: Q2 = QuadraticForm(ZZ, 3, [2, -1, 0, 2, 0, 50])
        sage: [Q1.omega(), Q2.omega()]
        [5, 5]
        sage: [Q1.hasse_invariant(5),                   # equivalent over Q_5           # needs sage.libs.pari
        ....:  Q2.hasse_invariant(5)]
        [1, 1]
        sage: [Q1.xi(5), Q2.xi(5)]                      # not equivalent over Z_5       # needs sage.libs.pari
        [1, -1]
    '''
def xi_rec(self, p):
    """
    Return Xi(`p`) for the reciprocal form.

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q1 = QuadraticForm(ZZ, 3, [1, 1, 1, 14, 3, 14])
        sage: Q2 = QuadraticForm(ZZ, 3, [2, -1, 0, 2, 0, 50])
        sage: [Q1.clifford_conductor(),                 # equivalent over Q
        ....:  Q2.clifford_conductor()]
        [3, 3]
        sage: Q1.is_locally_equivalent_to(Q2)           # not in the same genus
        False
        sage: [Q1.delta(), Q2.delta()]
        [480, 480]
        sage: factor(480)
        2^5 * 3 * 5
        sage: list(map(Q1.xi_rec, [-1,2,3,5]))
        [-1, -1, -1, 1]
        sage: list(map(Q2.xi_rec, [-1,2,3,5]))
        [-1, -1, -1, -1]
    """
def lll(self):
    """
    Return an LLL-reduced form of `Q` (using PARI).

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 4, range(1,11))
        sage: Q.is_definite()
        True
        sage: Q.lll()                                                                   # needs sage.libs.pari
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 1 0 ]
        [ * 4 3 3 ]
        [ * * 6 3 ]
        [ * * * 6 ]
    """
def representation_number_list(self, B):
    """
    Return the vector of representation numbers < B.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1,1,1,1,1])
        sage: Q.representation_number_list(10)                                          # needs sage.libs.pari
        [1, 16, 112, 448, 1136, 2016, 3136, 5504, 9328, 12112]
    """
def representation_vector_list(self, B, maxvectors=...):
    """
    Find all vectors `v` where `Q(v) < B`.

    This only works for positive definite quadratic forms.

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: Q = DiagonalQuadraticForm(ZZ, [1, 1])
        sage: Q.representation_vector_list(10)
        [[(0, 0)],
         [(0, 1), (0, -1), (1, 0), (-1, 0)],
         [(1, 1), (-1, -1), (1, -1), (-1, 1)],
         [],
         [(0, 2), (0, -2), (2, 0), (-2, 0)],
         [(1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1)],
         [],
         [],
         [(2, 2), (-2, -2), (2, -2), (-2, 2)],
         [(0, 3), (0, -3), (3, 0), (-3, 0)]]
        sage: list(map(len, _))
        [1, 4, 4, 0, 4, 8, 0, 0, 4, 4]
        sage: Q.representation_number_list(10)
        [1, 4, 4, 0, 4, 8, 0, 0, 4, 4]

    TESTS::

        sage: R = QuadraticForm(ZZ, 2, [-4,-3,0])
        sage: R.representation_vector_list(10)                                          # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        PariError: domain error in minim0: form is not positive definite
    """
def is_zero(self, v, p: int = 0) -> bool:
    """
    Determine if the vector `v` is on the conic `Q(x) = 0` (mod `p`).

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q1.is_zero([0,1,0], 2)
        True
        sage: Q1.is_zero([1,1,1], 2)
        True
        sage: Q1.is_zero([1,1,0], 2)
        False
    """
def is_zero_nonsingular(self, v, p: int = 0) -> bool:
    """
    Determine if the vector `v` is on the conic `Q(x) = 0` (mod `p`),
    and that this point is non-singular point of the conic.

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q1.is_zero_nonsingular([1,1,1], 2)
        True
        sage: Q1.is_zero([1, 19, 2], 37)
        True
        sage: Q1.is_zero_nonsingular([1, 19, 2], 37)
        False
    """
def is_zero_singular(self, v, p: int = 0) -> bool:
    """
    Determine if the vector `v` is on the conic `Q(x) = 0` (mod `p`),
    and that this point is singular point of the conic.

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q1.is_zero([1,1,1], 2)
        True
        sage: Q1.is_zero_singular([1,1,1], 2)
        False
        sage: Q1.is_zero_singular([1, 19, 2], 37)
        True
    """
