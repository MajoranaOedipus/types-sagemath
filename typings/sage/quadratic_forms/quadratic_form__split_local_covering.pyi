from sage.arith.misc import GCD as GCD
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.quadratic_forms.extras import extend_to_primitive as extend_to_primitive
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_double import RDF as RDF

def cholesky_decomposition(self, bit_prec: int = 53):
    '''
    Give the Cholesky decomposition of this quadratic form `Q` as a real matrix
    of precision ``bit_prec``.

    RESTRICTIONS:

        `Q` must be given as a :class:`QuadraticForm` defined over `\\ZZ`, `\\QQ`, or some
        real field. If it is over some real field, then an error is raised if
        the precision given is not less than the defined precision of the real
        field defining the quadratic form!

    REFERENCE:

    - Cohen\'s "A Course in Computational Algebraic Number Theory" book, p 103.

    INPUT:

    - ``bit_prec`` -- a natural number (default: 53)

    OUTPUT: an upper triangular real matrix of precision ``bit_prec``


    .. TODO::

        If we only care about working over the real double field (``RDF``), then we
        can use the method :meth:`cholesky` present for square matrices over that.

    .. NOTE::

        There is a note in the original code reading

        ::

            Finds the Cholesky decomposition of a quadratic form -- as an upper-triangular matrix!
            (It\'s assumed to be global, hence twice the form it refers to.)  <-- Python revision asks:  Is this true?!? =|

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.cholesky_decomposition()
        [ 1.00000000000000 0.000000000000000 0.000000000000000]
        [0.000000000000000  1.00000000000000 0.000000000000000]
        [0.000000000000000 0.000000000000000  1.00000000000000]

    ::

        sage: Q = QuadraticForm(QQ, 3, range(1,7)); Q
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ 1 2 3 ]
        [ * 4 5 ]
        [ * * 6 ]
        sage: Q.cholesky_decomposition()
        [ 1.00000000000000  1.00000000000000  1.50000000000000]
        [0.000000000000000  3.00000000000000 0.333333333333333]
        [0.000000000000000 0.000000000000000  3.41666666666667]
    '''
def vectors_by_length(self, bound):
    '''
    Return a list of short vectors together with their values.

    This is a naive algorithm which uses the Cholesky decomposition,
    but does not use the LLL-reduction algorithm.

    INPUT:

    - ``bound`` -- integer `\\geq 0`

    OUTPUT:

    - a list ``L`` of length (``bound`` + 1) whose entry ``L[i]`` is a list of
      all vectors of length `i`.

    REFERENCES:

    This is a slightly modified version of Cohn\'s Algorithm
    2.7.5 in "A Course in Computational Number Theory", with the
    increment step moved around and slightly re-indexed to allow clean
    looping.

    .. NOTE::

        We could speed this up for very skew matrices by using LLL
        first, and then changing coordinates back, but for our purposes
        the simpler method is efficient enough.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1])
        sage: Q.vectors_by_length(5)                                                    # needs sage.symbolic
        [[[0, 0]],
         [[0, -1], [-1, 0]],
         [[-1, -1], [1, -1]],
         [],
         [[0, -2], [-2, 0]],
         [[-1, -2], [1, -2], [-2, -1], [2, -1]]]

    ::

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q1.vectors_by_length(5)                                                   # needs sage.symbolic
        [[[0, 0, 0, 0]],
         [[-1, 0, 0, 0]],
         [],
         [[0, -1, 0, 0]],
         [[-1, -1, 0, 0], [1, -1, 0, 0], [-2, 0, 0, 0]],
         [[0, 0, -1, 0]]]

    ::

        sage: Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1])
        sage: list(map(len, Q.vectors_by_length(2)))                                    # needs sage.symbolic
        [1, 12, 12]

    ::

        sage: Q = QuadraticForm(ZZ, 4, [1,-1,-1,-1, 1,0,0, 4,-3, 4])
        sage: list(map(len, Q.vectors_by_length(3)))                                    # needs sage.symbolic
        [1, 3, 0, 3]
    '''
def complementary_subform_to_vector(self, v):
    """
    Find the `(n-1)`-dimensional quadratic form orthogonal to the vector `v`.

    .. NOTE::

        This is usually not a direct summand!

    .. NOTE::

        There is a minor difference in the cancellation
        code here (form the C++ version) since the notation ``Q[i,j]`` indexes
        coefficients of the quadratic polynomial here, not the symmetric
        matrix.  Also, it produces a better splitting now, for the full
        lattice (as opposed to a sublattice in the C++ code) since we
        now extend `v` to a unimodular matrix.

    INPUT:

    - ``v`` -- list of ``self.dim()`` integers

    OUTPUT: a :class:`QuadraticForm` over `\\ZZ`

    EXAMPLES::

        sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q1.complementary_subform_to_vector([1,0,0,0])
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 7 0 0 ]
        [ * 5 0 ]
        [ * * 3 ]

    ::

        sage: Q1.complementary_subform_to_vector([1,1,0,0])
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 7 0 0 ]
        [ * 5 0 ]
        [ * * 12 ]

    ::

        sage: Q1.complementary_subform_to_vector([1,1,1,1])
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 880 -480 -160 ]
        [ * 624 -96 ]
        [ * * 240 ]
    """
def split_local_cover(self):
    """
    Try to find subform of the given (positive definite quaternary)
    quadratic form `Q` of the form

    .. MATH::

        d\\cdot x^2 + T(y,z,w)

    where `d > 0` is as small as possible.

    This is done by exhaustive search on small vectors, and then
    comparing the local conditions of its sum with its complementary
    lattice and the original quadratic form `Q`.

    OUTPUT: a :class:`QuadraticForm` over `\\ZZ`

    EXAMPLES::

        sage: Q1 = DiagonalQuadraticForm(ZZ, [7,5,3])
        sage: Q1.split_local_cover()                                                    # needs sage.symbolic
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 3 0 0 ]
        [ * 5 0 ]
        [ * * 7 ]
    """
