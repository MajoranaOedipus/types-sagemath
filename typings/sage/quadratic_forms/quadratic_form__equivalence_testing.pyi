from sage.arith.misc import GCD as GCD, hilbert_symbol as hilbert_symbol, is_prime as is_prime, legendre_symbol as legendre_symbol, prime_divisors as prime_divisors, valuation as valuation
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from typing import Any

def is_globally_equivalent_to(self, other, return_matrix: bool = False) -> bool | Any:
    """
    Determine if the current quadratic form is equivalent to the
    given form over `\\ZZ`.

    If ``return_matrix`` is True, then we return the transformation
    matrix `M` so that ``self(M) == other``.

    INPUT:

    - ``self``, ``other`` -- positive definite integral quadratic forms

    - ``return_matrix`` -- boolean (default: ``False``); return
      the transformation matrix instead of a boolean

    OUTPUT:

    - if ``return_matrix`` is ``False``: a boolean

    - if ``return_matrix`` is ``True``: either ``False`` or the
      transformation matrix

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: M = Matrix(ZZ, 4, 4, [1,2,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
        sage: Q1 = Q(M)
        sage: Q.is_globally_equivalent_to(Q1)                                           # needs sage.libs.pari
        True
        sage: MM = Q.is_globally_equivalent_to(Q1, return_matrix=True)                  # needs sage.libs.pari
        sage: Q(MM) == Q1                                                               # needs sage.libs.pari
        True

    ::

        sage: # needs sage.libs.pari
        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q2 = QuadraticForm(ZZ, 3, [2, 1, 2, 2, 1, 3])
        sage: Q3 = QuadraticForm(ZZ, 3, [8, 6, 5, 3, 4, 2])
        sage: Q1.is_globally_equivalent_to(Q2)
        False
        sage: Q1.is_globally_equivalent_to(Q2, return_matrix=True)
        False
        sage: Q1.is_globally_equivalent_to(Q3)
        True
        sage: M = Q1.is_globally_equivalent_to(Q3, True); M
        [-1 -1  0]
        [ 1  1  1]
        [-1  0  0]
        sage: Q1(M) == Q3
        True

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1, -1])
        sage: Q.is_globally_equivalent_to(Q)                                            # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: not a definite form in QuadraticForm.is_globally_equivalent_to()

    ALGORITHM: this uses the PARI function :pari:`qfisom`, implementing
    an algorithm by Plesken and Souvignier.

    TESTS:

    :issue:`27749` is fixed::

        sage: Q = QuadraticForm(ZZ, 2, [2, 3, 5])
        sage: P = QuadraticForm(ZZ, 2, [8, 6, 5])
        sage: Q.is_globally_equivalent_to(P)                                            # needs sage.libs.pari
        False
        sage: P.is_globally_equivalent_to(Q)                                            # needs sage.libs.pari
        False
    """
def is_locally_equivalent_to(self, other, check_primes_only: bool = False, force_jordan_equivalence_test: bool = False) -> bool:
    """
    Determine if the current quadratic form (defined over `\\ZZ`) is
    locally equivalent to the given form over the real numbers and the
    `p`-adic integers for every prime `p`.

    This works by comparing the local Jordan decompositions at every
    prime, and the dimension and signature at the real place.

    INPUT:

    - ``other`` -- a :class:`QuadraticForm`

    OUTPUT: boolean

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
        sage: Q2 = QuadraticForm(ZZ, 3, [2, 1, 2, 2, 1, 3])
        sage: Q1.is_globally_equivalent_to(Q2)                                          # needs sage.libs.pari
        False
        sage: Q1.is_locally_equivalent_to(Q2)                                           # needs sage.libs.pari
        True
    """
def has_equivalent_Jordan_decomposition_at_prime(self, other, p) -> bool:
    """
    Determine if the given quadratic form has a Jordan decomposition
    equivalent to that of ``self``.

    INPUT:

    - ``other`` -- a :class:`QuadraticForm`

    OUTPUT: boolean

    EXAMPLES::

        sage: Q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 1, 0, 3])
        sage: Q2 = QuadraticForm(ZZ, 3, [1, 0, 0, 2, -2, 6])
        sage: Q3 = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 11])
        sage: [Q1.level(), Q2.level(), Q3.level()]
        [44, 44, 44]

        sage: # needs sage.libs.pari
        sage: Q1.has_equivalent_Jordan_decomposition_at_prime(Q2, 2)
        False
        sage: Q1.has_equivalent_Jordan_decomposition_at_prime(Q2, 11)
        False
        sage: Q1.has_equivalent_Jordan_decomposition_at_prime(Q3, 2)
        False
        sage: Q1.has_equivalent_Jordan_decomposition_at_prime(Q3, 11)
        True
        sage: Q2.has_equivalent_Jordan_decomposition_at_prime(Q3, 2)
        True
        sage: Q2.has_equivalent_Jordan_decomposition_at_prime(Q3, 11)
        False
    """
def is_rationally_isometric(self, other, return_matrix: bool = False) -> bool | Any:
    """
    Determine if two regular quadratic forms over a number field are isometric.

    INPUT:

    - ``other`` -- a quadratic form over a number field

    - ``return_matrix`` -- boolean (default: ``False``); return
      the transformation matrix instead of a boolean; this is currently
      only implemented for forms over ``QQ``

    OUTPUT:

    - if ``return_matrix`` is ``False``: a boolean

    - if ``return_matrix`` is ``True``: either ``False`` or the
      transformation matrix

    EXAMPLES::

        sage: V = DiagonalQuadraticForm(QQ, [1, 1, 2])
        sage: W = DiagonalQuadraticForm(QQ, [2, 2, 2])
        sage: V.is_rationally_isometric(W)                                              # needs sage.libs.pari
        True

    ::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 3)
        sage: V = QuadraticForm(K, 4, [1, 0, 0, 0, 2*a, 0, 0, a, 0, 2]); V
        Quadratic form in 4 variables over Number Field in a
         with defining polynomial x^2 - 3 with coefficients:
        [ 1 0 0 0 ]
        [ * 2*a 0 0 ]
        [ * * a 0 ]
        [ * * * 2 ]
        sage: W = QuadraticForm(K, 4, [1, 2*a, 4, 6, 3, 10, 2, 1, 2, 5]); W
        Quadratic form in 4 variables over Number Field in a
         with defining polynomial x^2 - 3 with coefficients:
        [ 1 2*a 4 6 ]
        [ * 3 10 2 ]
        [ * * 1 2 ]
        [ * * * 5 ]
        sage: V.is_rationally_isometric(W)
        False

    ::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^4 + 2*x + 6)
        sage: V = DiagonalQuadraticForm(K, [a, 2, 3, 2, 1]); V
        Quadratic form in 5 variables over Number Field in a
         with defining polynomial x^4 + 2*x + 6 with coefficients:
        [ a 0 0 0 0 ]
        [ * 2 0 0 0 ]
        [ * * 3 0 0 ]
        [ * * * 2 0 ]
        [ * * * * 1 ]
        sage: W = DiagonalQuadraticForm(K, [a, a, a, 2, 1]); W
        Quadratic form in 5 variables over Number Field in a
         with defining polynomial x^4 + 2*x + 6 with coefficients:
        [ a 0 0 0 0 ]
        [ * a 0 0 0 ]
        [ * * a 0 0 ]
        [ * * * 2 0 ]
        [ * * * * 1 ]
        sage: V.is_rationally_isometric(W)
        False

    ::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^2 - 3)
        sage: V = DiagonalQuadraticForm(K, [-1, a, -2*a])
        sage: W = DiagonalQuadraticForm(K, [-1, -a, 2*a])
        sage: V.is_rationally_isometric(W)
        True

        sage: # needs sage.rings.number_field
        sage: V = DiagonalQuadraticForm(QQ, [1, 1, 2])
        sage: W = DiagonalQuadraticForm(QQ, [2, 2, 2])
        sage: T = V.is_rationally_isometric(W, True); T
        [   0    0    1]
        [-1/2 -1/2    0]
        [ 1/2 -1/2    0]
        sage: V.Gram_matrix() == T.transpose() * W.Gram_matrix() * T
        True

        sage: T = W.is_rationally_isometric(V, True); T                                 # needs sage.rings.number_field
        [ 0 -1  1]
        [ 0 -1 -1]
        [ 1  0  0]
        sage: W.Gram_matrix() == T.T * V.Gram_matrix() * T                              # needs sage.rings.number_field
        True

    ::

        sage: L = QuadraticForm(QQ, 3, [2, 2, 0, 2, 2, 5])
        sage: M = QuadraticForm(QQ, 3, [2, 2, 0, 3, 2, 3])
        sage: L.is_rationally_isometric(M, True)                                        # needs sage.libs.pari
        False

    ::

        sage: A = DiagonalQuadraticForm(QQ, [1, 5])
        sage: B = QuadraticForm(QQ, 2, [1, 12, 81])
        sage: T = A.is_rationally_isometric(B, True); T                                 # needs sage.libs.pari
        [  1  -2]
        [  0 1/3]
        sage: A.Gram_matrix() == T.T * B.Gram_matrix() * T                              # needs sage.libs.pari
        True

    ::

        sage: C = DiagonalQuadraticForm(QQ, [1, 5, 9])
        sage: D = DiagonalQuadraticForm(QQ, [6, 30, 1])
        sage: T = C.is_rationally_isometric(D, True); T                                 # needs sage.libs.pari
        [   0 -5/6  1/2]
        [   0  1/6  1/2]
        [  -1    0    0]
        sage: C.Gram_matrix() == T.T * D.Gram_matrix() * T                              # needs sage.libs.pari
        True

    ::

        sage: E = DiagonalQuadraticForm(QQ, [1, 1])
        sage: F = QuadraticForm(QQ, 2, [17, 94, 130])
        sage: T = F.is_rationally_isometric(E, True); T                                 # needs sage.libs.pari
        [     -4 -189/17]
        [     -1  -43/17]
        sage: F.Gram_matrix() == T.T * E.Gram_matrix() * T                              # needs sage.libs.pari
        True

    TESTS::

        sage: # needs sage.rings.number_field
        sage: K.<a> = QuadraticField(3)
        sage: V = DiagonalQuadraticForm(K, [1, 2])
        sage: W = DiagonalQuadraticForm(K, [1, 0])
        sage: V.is_rationally_isometric(W)
        Traceback (most recent call last):
        ...
        NotImplementedError: this only tests regular forms

    Forms must have the same base ring otherwise a :exc:`TypeError` is raised::

        sage: # needs sage.rings.number_field
        sage: K1.<a> = QuadraticField(5)
        sage: K2.<b> = QuadraticField(7)
        sage: V = DiagonalQuadraticForm(K1, [1, a])
        sage: W = DiagonalQuadraticForm(K2, [1, b])
        sage: V.is_rationally_isometric(W)
        Traceback (most recent call last):
        ...
        TypeError: forms must have the same base ring.

    Forms which have different dimension are not isometric::

        sage: W = DiagonalQuadraticForm(QQ, [1, 2])
        sage: V = DiagonalQuadraticForm(QQ, [1, 1, 1])
        sage: V.is_rationally_isometric(W)
        False

    Forms whose determinants do not differ by a square in the base field are not isometric::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^2 - 3)
        sage: V = DiagonalQuadraticForm(K, [-1, a, -2*a])
        sage: W = DiagonalQuadraticForm(K, [-1, a, 2*a])
        sage: V.is_rationally_isometric(W)
        False

    ::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^5 - x + 2, 'a')
        sage: Q = QuadraticForm(K, 3, [a, 1, 0, -a**2, -a**3, -1])
        sage: m = Q.matrix()
        sage: for _ in range(5):
        ....:     t = random_matrix(ZZ, 3, algorithm='unimodular')
        ....:     m2 = t*m*t.transpose()
        ....:     Q2 = QuadraticForm(K, 3, [m2[i,j] / (2 if i==j else 1)
        ....:                               for i in range(3) for j in range(i,3)])
        ....:     print(Q.is_rationally_isometric(Q2))
        True
        True
        True
        True
        True
    """
