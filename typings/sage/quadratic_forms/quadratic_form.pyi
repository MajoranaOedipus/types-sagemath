from _typeshed import Incomplete
from sage.arith.misc import GCD as GCD
from sage.categories.fields import Fields as Fields
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.rings import Rings as Rings
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.functional import denominator as denominator, is_even as is_even
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias, deprecation as deprecation
from sage.modules.free_module_element import vector as vector
from sage.quadratic_forms.quadratic_form__count_local_2 import count_congruence_solutions as count_congruence_solutions, count_congruence_solutions__bad_type as count_congruence_solutions__bad_type, count_congruence_solutions__bad_type_I as count_congruence_solutions__bad_type_I, count_congruence_solutions__bad_type_II as count_congruence_solutions__bad_type_II, count_congruence_solutions__good_type as count_congruence_solutions__good_type, count_congruence_solutions__zero_type as count_congruence_solutions__zero_type, count_congruence_solutions_as_vector as count_congruence_solutions_as_vector
from sage.quadratic_forms.quadratic_form__equivalence_testing import has_equivalent_Jordan_decomposition_at_prime as has_equivalent_Jordan_decomposition_at_prime, is_globally_equivalent_to as is_globally_equivalent_to, is_locally_equivalent_to as is_locally_equivalent_to, is_rationally_isometric as is_rationally_isometric
from sage.quadratic_forms.quadratic_form__evaluate import QFEvaluateMatrix as QFEvaluateMatrix, QFEvaluateVector as QFEvaluateVector
from sage.quadratic_forms.quadratic_form__local_density_congruence import count_modp_solutions__by_Gauss_sum as count_modp_solutions__by_Gauss_sum, local_badII_density_congruence as local_badII_density_congruence, local_badI_density_congruence as local_badI_density_congruence, local_bad_density_congruence as local_bad_density_congruence, local_density_congruence as local_density_congruence, local_good_density_congruence as local_good_density_congruence, local_good_density_congruence_even as local_good_density_congruence_even, local_good_density_congruence_odd as local_good_density_congruence_odd, local_primitive_density_congruence as local_primitive_density_congruence, local_zero_density_congruence as local_zero_density_congruence
from sage.quadratic_forms.quadratic_form__local_field_invariants import anisotropic_primes as anisotropic_primes, compute_definiteness as compute_definiteness, compute_definiteness_string_by_determinants as compute_definiteness_string_by_determinants, hasse_invariant as hasse_invariant, hasse_invariant__OMeara as hasse_invariant__OMeara, is_anisotropic as is_anisotropic, is_definite as is_definite, is_hyperbolic as is_hyperbolic, is_indefinite as is_indefinite, is_isotropic as is_isotropic, is_negative_definite as is_negative_definite, is_positive_definite as is_positive_definite, rational_diagonal_form as rational_diagonal_form, signature as signature, signature_vector as signature_vector
from sage.quadratic_forms.quadratic_form__neighbors import find_p_neighbor_from_vec as find_p_neighbor_from_vec, find_primitive_p_divisible_vector__next as find_primitive_p_divisible_vector__next, find_primitive_p_divisible_vector__random as find_primitive_p_divisible_vector__random, neighbor_iteration as neighbor_iteration, orbits_lines_mod_p as orbits_lines_mod_p
from sage.quadratic_forms.quadratic_form__reduction_theory import minkowski_reduction as minkowski_reduction, minkowski_reduction_for_4vars__SP as minkowski_reduction_for_4vars__SP, reduced_binary_form as reduced_binary_form, reduced_binary_form1 as reduced_binary_form1, reduced_ternary_form__Dickson as reduced_ternary_form__Dickson
from sage.quadratic_forms.quadratic_form__split_local_covering import cholesky_decomposition as cholesky_decomposition, complementary_subform_to_vector as complementary_subform_to_vector, split_local_cover as split_local_cover, vectors_by_length as vectors_by_length
from sage.quadratic_forms.quadratic_form__ternary_Tornaria import adjoint as adjoint, antiadjoint as antiadjoint, basiclemma as basiclemma, basiclemmavec as basiclemmavec, clifford_conductor as clifford_conductor, clifford_invariant as clifford_invariant, content as content, delta as delta, disc as disc, discrec as discrec, hasse_conductor as hasse_conductor, is_adjoint as is_adjoint, is_zero as is_zero, is_zero_nonsingular as is_zero_nonsingular, is_zero_singular as is_zero_singular, level__Tornaria as level__Tornaria, lll as lll, omega as omega, reciprocal as reciprocal, representation_number_list as representation_number_list, representation_vector_list as representation_vector_list, xi as xi, xi_rec as xi_rec
from sage.quadratic_forms.quadratic_form__theta import theta_by_cholesky as theta_by_cholesky, theta_by_pari as theta_by_pari, theta_series as theta_series, theta_series_degree_2 as theta_series_degree_2
from sage.quadratic_forms.quadratic_form__variable_substitutions import add_symmetric as add_symmetric, divide_variable as divide_variable, elementary_substitution as elementary_substitution, extract_variables as extract_variables, multiply_variable as multiply_variable, scale_by_factor as scale_by_factor, swap_variables as swap_variables
from sage.rings.ideal import Ideal as Ideal
from sage.rings.integer_ring import IntegerRing as IntegerRing, ZZ as ZZ
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Matrix as Matrix, Vector as Vector
from sage.structure.sage_object import SageObject as SageObject

def is_QuadraticForm(Q):
    """
    Determine if the object ``Q`` is an element of the :class:`QuadraticForm` class.

    This function is deprecated.

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
        sage: from sage.quadratic_forms.quadratic_form import is_QuadraticForm
        sage: is_QuadraticForm(Q)
        doctest:...: DeprecationWarning: the function is_QuadraticForm is deprecated;
        use isinstance(x, sage.quadratic_forms.quadratic_form.QuadraticForm) instead...
        True
        sage: is_QuadraticForm(2)
        False
    """
def quadratic_form_from_invariants(F, rk, det, P, sminus):
    """
    Return a rational quadratic form with given invariants.

    INPUT:

    - ``F`` -- the base field; currently only ``QQ`` is allowed
    - ``rk`` -- integer; the rank
    - ``det`` -- rational; the determinant
    - ``P`` -- list of primes where Cassel's Hasse invariant
      is negative
    - ``sminus`` -- integer; the number of negative eigenvalues
      of any Gram matrix

    OUTPUT: a quadratic form with the specified invariants

    Let `(a_1, \\ldots, a_n)` be the Gram matrix of a regular quadratic space.
    Then Cassel's Hasse invariant is defined as

    .. MATH::

        \\prod_{i<j} (a_i,a_j),

    where `(a_i,a_j)` denotes the Hilbert symbol.

    ALGORITHM:

    We follow [Kir2016]_.

    EXAMPLES::

        sage: P = [3,5]
        sage: q = quadratic_form_from_invariants(QQ,2,-15,P,1); q                       # needs sage.rings.padics
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 5 0 ]
        [ * -3 ]
        sage: all(q.hasse_invariant(p) == -1 for p in P)                                # needs sage.rings.padics
        True

    TESTS:

    This shows that :issue:`28955` is fixed::

        sage: quadratic_form_from_invariants(QQ,3,2,[2],2)                              # needs sage.rings.padics
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ -1 0 0 ]
        [ * 1 0 ]
        [ * * -2 ]

        sage: quadratic_form_from_invariants(QQ,4,2,[2],4)                              # needs sage.rings.padics
        Traceback (most recent call last):
        ...
        ValueError: invariants do not define a rational quadratic form
    """

class QuadraticForm(SageObject):
    """
    The ``QuadraticForm`` class represents a quadratic form in `n` variables with
    coefficients in the ring `R`.

    INPUT:

    The constructor may be called in any of the following ways.

    #. ``QuadraticForm(R, n, entries)``, where

       - ``R`` -- ring for which the quadratic form is defined
       - ``n`` -- integer `\\geq 0`
       - ``entries`` -- list of `n(n+1)/2` coefficients of the quadratic form
         in `R` (given lexicographically, or equivalently, by rows of the
         matrix)

    #. ``QuadraticForm(p)``, where

       - ``p`` -- a homogeneous polynomial of degree `2`

    #. ``QuadraticForm(R, n)``, where

       - ``R`` -- a ring
       - ``n`` -- a symmetric `n \\times n` matrix with even diagonal (relative to
         `R`)

    #. ``QuadraticForm(R)``, where

       - ``R`` -- a symmetric `n \\times n` matrix with even diagonal (relative to
         its base ring)

    If the keyword argument ``unsafe_initialize`` is True, then the subsequent
    fields may by used to force the external initialization of various fields
    of the quadratic form. Currently the only fields which can be set are:

    - ``number_of_automorphisms``
    - ``determinant``

    OUTPUT: quadratic form

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [1,2,3,4,5,6]); Q
        Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 2 3 ]
        [ * 4 5 ]
        [ * * 6 ]

    ::

        sage: Q = QuadraticForm(QQ, 3, [1,2,3,4/3,5,6]); Q
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ 1 2 3 ]
        [ * 4/3 5 ]
        [ * * 6 ]
        sage: Q[0,0]
        1
        sage: Q[0,0].parent()
        Rational Field

    ::

        sage: Q = QuadraticForm(QQ, 7, range(28)); Q
        Quadratic form in 7 variables over Rational Field with coefficients:
        [ 0 1 2 3 4 5 6 ]
        [ * 7 8 9 10 11 12 ]
        [ * * 13 14 15 16 17 ]
        [ * * * 18 19 20 21 ]
        [ * * * * 22 23 24 ]
        [ * * * * * 25 26 ]
        [ * * * * * * 27 ]

    ::

        sage: Q = QuadraticForm(QQ, 2, range(1,4))
        sage: A = Matrix(ZZ, 2, 2, [-1,0,0,1])
        sage: Q(A)
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1 -2 ]
        [ * 3 ]

    ::

        sage: m = matrix(2, 2, [1,2,3,4])
        sage: m + m.transpose()
        [2 5]
        [5 8]
        sage: QuadraticForm(m + m.transpose())
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 1 5 ]
        [ * 4 ]

    ::

        sage: P.<x,y,z> = QQ[]
        sage: p = x^2 + 2*x*y + x*z/2 + y^2 + y*z/3
        sage: QuadraticForm(p)
        Quadratic form in 3 variables over Rational Field with coefficients:
        [ 1 2 1/2 ]
        [ * 1 1/3 ]
        [ * * 0 ]

    ::

        sage: QuadraticForm(ZZ, m + m.transpose())
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 1 5 ]
        [ * 4 ]

    ::

        sage: QuadraticForm(QQ, m + m.transpose())
        Quadratic form in 2 variables over Rational Field with coefficients:
        [ 1 5 ]
        [ * 4 ]
    """
    def __init__(self, R, n=None, entries=None, unsafe_initialization: bool = False, number_of_automorphisms=None, determinant=None) -> None:
        """
        EXAMPLES::

            sage: s = QuadraticForm(ZZ, 4, range(10))
            sage: s.dim()
            4

            sage: P.<x,y,z> = QQ[]
            sage: p = x^2 + y^2 + 2*x*z
            sage: QuadraticForm(p)
            Quadratic form in 3 variables over Rational Field with coefficients:
            [ 1 0 2 ]
            [ * 1 0 ]
            [ * * 0 ]
            sage: z = P.zero()
            sage: QuadraticForm(z)
            Quadratic form in 3 variables over Rational Field with coefficients:
            [ 0 0 0 ]
            [ * 0 0 ]
            [ * * 0 ]
            sage: q = x^2 + 3*y - z
            sage: QuadraticForm(q)
            Traceback (most recent call last):
            ...
            ValueError: polynomial is neither zero nor homogeneous of degree 2

        TESTS::

            sage: s == loads(dumps(s))
            True
            sage: QuadraticForm(ZZ, -1)
            Traceback (most recent call last):
            ...
            ValueError: the size must be a nonnegative integer, not -1

            sage: x = polygen(ZZ, 'x')
            sage: QuadraticForm(x**2)
            Quadratic form in 1 variables over Integer Ring with coefficients:
            [ 1 ]

            sage: QuadraticForm(1)
            Traceback (most recent call last):
            ....
            TypeError: wrong input for QuadraticForm
        """
    def list_external_initializations(self):
        """
        Return a list of the fields which were set externally at
        creation, and not created through the usual :class:`QuadraticForm`
        methods.  These fields are as good as the external process
        that made them, and are thus not guaranteed to be correct.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,0,5])
            sage: Q.list_external_initializations()
            []

            sage: # needs sage.libs.pari
            sage: T = Q.theta_series()
            sage: Q.list_external_initializations()
            []
            sage: Q = QuadraticForm(ZZ, 2, [1,0,5], unsafe_initialization=False,
            ....:                   number_of_automorphisms=3, determinant=0)
            sage: Q.list_external_initializations()
            []

        ::

            sage: # needs sage.libs.pari
            sage: Q = QuadraticForm(ZZ, 2, [1,0,5], unsafe_initialization=False,
            ....:                   number_of_automorphisms=3, determinant=0)
            sage: Q.list_external_initializations()
            []
            sage: Q = QuadraticForm(ZZ, 2, [1,0,5], unsafe_initialization=True,
            ....:                   number_of_automorphisms=3, determinant=0)
            sage: Q.list_external_initializations()
            ['number_of_automorphisms', 'determinant']
        """
    def __pari__(self):
        """
        Return a PARI-formatted Hessian matrix for Q.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,0,5])
            sage: Q.__pari__()                                                          # needs sage.libs.pari
            [2, 0; 0, 10]
        """
    def __getitem__(self, ij):
        """
        Return the coefficient `a_{ij}` of `x_i\\cdot x_j`.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 3, [1,2,3,4,5,6])
            sage: matrix(ZZ, 3, 3, [Q[i,j]  for i in range(3) for j in range(3)])
            [1 2 3]
            [2 4 5]
            [3 5 6]
        """
    def __setitem__(self, ij, coeff) -> None:
        """
        Set the coefficient `a_{ij}` in front of `x_i\\cdot x_j`.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 3, [1,2,3,4,5,6])
            sage: Q
            Quadratic form in 3 variables over Integer Ring with coefficients:
            [ 1 2 3 ]
            [ * 4 5 ]
            [ * * 6 ]
            sage: Q[2,1] = 17
            sage: Q
            Quadratic form in 3 variables over Integer Ring with coefficients:
            [ 1 2 3 ]
            [ * 4 17 ]
            [ * * 6 ]
        """
    def __hash__(self):
        """
        TESTS::

            sage: Q1 = QuadraticForm(QQ, 2, [1,1,1])
            sage: Q2 = QuadraticForm(QQ, 2, [1,1,1])
            sage: Q3 = QuadraticForm(QuadraticField(2), 2, [1,1,1])                     # needs sage.rings.number_field
            sage: hash(Q1) == hash(Q2)
            True
            sage: hash(Q1) == hash(Q3)                                                  # needs sage.rings.number_field
            False
        """
    def __eq__(self, right):
        """
        Determines if two quadratic forms are equal.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,4,10])
            sage: Q == Q
            True

            sage: Q1 = QuadraticForm(QQ, 2, [1,4,10])
            sage: Q == Q1
            False

            sage: Q2 = QuadraticForm(ZZ, 2, [1,4,-10])
            sage: Q == Q1
            False
            sage: Q == Q2
            False
            sage: Q1 == Q2
            False
        """
    def __add__(self, right):
        """
        Return the direct sum of two quadratic forms.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,4,10]); Q
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 4 ]
            [ * 10 ]
            sage: Q2 = QuadraticForm(ZZ, 2, [1,4,-10])
            sage: Q + Q2
            Quadratic form in 4 variables over Integer Ring with coefficients:
            [ 1 4 0 0 ]
            [ * 10 0 0 ]
            [ * * 1 4 ]
            [ * * * -10 ]
        """
    def sum_by_coefficients_with(self, right):
        """
        Return the sum (on coefficients) of two quadratic forms of the same size.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,4,10]); Q
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 4 ]
            [ * 10 ]
            sage: Q + Q
            Quadratic form in 4 variables over Integer Ring with coefficients:
            [ 1 4 0 0 ]
            [ * 10 0 0 ]
            [ * * 1 4 ]
            [ * * * 10 ]

            sage: Q2 = QuadraticForm(ZZ, 2, [1,4,-10])
            sage: Q.sum_by_coefficients_with(Q2)
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 2 8 ]
            [ * 0 ]
        """
    def __call__(self, v):
        """
        Evaluate this quadratic form `Q` on a vector or matrix of elements
        coercible to the base ring of the quadratic form.

        If a vector is given then the output will be the ring element
        `Q(v)`, but if a matrix is given then the output will be the
        quadratic form `Q'` which in matrix notation is given by:

        .. MATH::

            Q' = v^t\\cdot Q\\cdot v.

        EXAMPLES:

        Evaluate a quadratic form at a vector::

            sage: Q = QuadraticForm(QQ, 3, range(6))
            sage: Q
            Quadratic form in 3 variables over Rational Field with coefficients:
            [ 0 1 2 ]
            [ * 3 4 ]
            [ * * 5 ]
            sage: Q([1,2,3])
            89
            sage: Q([1,0,0])
            0
            sage: Q([1,1,1])
            15

        Evaluate a quadratic form using a column matrix::

            sage: Q = QuadraticForm(QQ, 2, range(1,4))
            sage: A = Matrix(ZZ,2,2,[-1,0,0,1])
            sage: Q(A)
            Quadratic form in 2 variables over Rational Field with coefficients:
            [ 1 -2 ]
            [ * 3 ]
            sage: Q([1,0])
            1
            sage: type(Q([1,0]))
            <... 'sage.rings.rational.Rational'>
            sage: Q = QuadraticForm(QQ, 2, range(1,4))
            sage: Q(matrix(2, [1,0]))
            Quadratic form in 1 variables over Rational Field with coefficients:
            [ 1 ]

        Simple 2x2 change of variables::

            sage: Q = QuadraticForm(ZZ, 2, [1,0,1])
            sage: Q
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 0 ]
            [ * 1 ]
            sage: M = Matrix(ZZ, 2, 2, [1,1,0,1])
            sage: M
            [1 1]
            [0 1]
            sage: Q(M)
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 2 ]
            [ * 2 ]

        Some more tests::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
            sage: Q([1,2,3])
            14
            sage: v = vector([1,2,3])
            sage: Q(v)
            14
            sage: t = tuple([1,2,3])
            sage: Q(v)
            14
            sage: M = Matrix(ZZ, 3, [1,2,3])
            sage: Q(M)
            Quadratic form in 1 variables over Integer Ring with coefficients:
            [ 14 ]
        """
    def matrix(self):
        """
        Return the Hessian matrix `A` for which `Q(X) = (1/2) X^t\\cdot A\\cdot X`.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 3, range(6))
            sage: Q.matrix()
            [ 0  1  2]
            [ 1  6  4]
            [ 2  4 10]
        """
    def Hessian_matrix(self):
        """
        Return the Hessian matrix `A` for which `Q(X) = (1/2) X^t\\cdot A\\cdot X`.

        EXAMPLES::

            sage: Q = QuadraticForm(QQ, 2, range(1,4)); Q
            Quadratic form in 2 variables over Rational Field with coefficients:
            [ 1 2 ]
            [ * 3 ]
            sage: Q.Hessian_matrix()
            [2 2]
            [2 6]
            sage: Q.matrix().base_ring()
            Rational Field
        """
    def Gram_matrix_rational(self):
        """
        Return a (symmetric) Gram matrix `A` for the quadratic form `Q`,
        meaning that

        .. MATH::

            Q(x) = x^t\\cdot A\\cdot x,

        defined over the fraction field of the base ring.

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
            sage: A = Q.Gram_matrix_rational(); A
            [1 0 0 0]
            [0 3 0 0]
            [0 0 5 0]
            [0 0 0 7]
            sage: A.base_ring()
            Rational Field
        """
    def Gram_matrix(self):
        """
        Return a (symmetric) Gram matrix `A` for the quadratic form `Q`,
        meaning that

        .. MATH::

            Q(x) = x^t\\cdot A\\cdot x,

        defined over the base ring of `Q`.  If this is not possible,
        then a :exc:`TypeError` is raised.

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
            sage: A = Q.Gram_matrix(); A
            [1 0 0 0]
            [0 3 0 0]
            [0 0 5 0]
            [0 0 0 7]
            sage: A.base_ring()
            Integer Ring
        """
    def has_integral_Gram_matrix(self) -> bool:
        """
        Return whether the quadratic form has an integral Gram matrix (with respect to its base ring).

        A warning is issued if the form is defined over a field,
        since in that case the return is trivially true.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [7,8,9])
            sage: Q.has_integral_Gram_matrix()
            True

        ::

            sage: Q = QuadraticForm(ZZ, 2, [4,5,6])
            sage: Q.has_integral_Gram_matrix()
            False
        """
    def gcd(self):
        """
        Return the greatest common divisor of the coefficients of the
        quadratic form (as a polynomial).

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 4, range(1, 21, 2))
            sage: Q.gcd()
            1

            sage: Q = QuadraticForm(ZZ, 4, range(0, 20, 2))
            sage: Q.gcd()
            2
        """
    def polynomial(self, names: str = 'x'):
        """
        Return the quadratic form as a polynomial in `n` variables.

        INPUT:

        - ``self`` -- a quadratic form over a commutative ring

        - ``names`` -- specification of the names of the variables; see :func:`PolynomialRing`

        OUTPUT: the polynomial form of the quadratic form

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(QQ,[1, 3, 5, 7])
            sage: P = Q.polynomial(); P
            x0^2 + 3*x1^2 + 5*x2^2 + 7*x3^2

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: F.<a> = NumberField(x^2 - 5)
            sage: Z = F.ring_of_integers()
            sage: Q = QuadraticForm(Z, 3, [2*a, 3*a, 0, 1 - a, 0, 2*a + 4])
            sage: P = Q.polynomial(names='y'); P
            2*a*y0^2 + 3*a*y0*y1 + (-a + 1)*y1^2 + (2*a + 4)*y2^2
            sage: Q = QuadraticForm(F, 4,
            ....:                   [a, 3*a, 0, 1 - a, a - 3, 0, 2*a + 4, 4 + a, 0, 1])
            sage: Q.polynomial(names='z')
            a*z0^2 + (3*a)*z0*z1 + (a - 3)*z1^2 + (a + 4)*z2^2
            + (-a + 1)*z0*z3 + (2*a + 4)*z1*z3 + z3^2
            sage: B.<i,j,k> = QuaternionAlgebra(F,-1,-1)
            sage: Q = QuadraticForm(B, 3, [2*a, 3*a, i, 1 - a, 0, 2*a + 4])
            sage: Q.polynomial()
            Traceback (most recent call last):
            ...
            ValueError: Can only create polynomial rings over commutative rings
        """
    @staticmethod
    def from_polynomial(poly):
        """
        Construct a :class:`QuadraticForm` from a multivariate
        polynomial. Inverse of :meth:`polynomial`.

        EXAMPLES::

            sage: R.<x,y,z> = ZZ[]
            sage: f = 5*x^2 - x*z - 3*y*z - 2*y^2 + 9*z^2
            sage: Q = QuadraticForm.from_polynomial(f); Q
            Quadratic form in 3 variables over Integer Ring with coefficients:
            [ 5 0 -1 ]
            [ * -2 -3 ]
            [ * * 9 ]
            sage: Q.polynomial()
            5*x0^2 - 2*x1^2 - x0*x2 - 3*x1*x2 + 9*x2^2
            sage: Q.polynomial()(R.gens()) == f
            True

        The method fails if the given polynomial is not a quadratic form::

            sage: QuadraticForm.from_polynomial(x^3 + x*z + 5*y^2)
            Traceback (most recent call last):
            ...
            ValueError: polynomial has monomials of degree != 2
        """
    def is_primitive(self) -> bool:
        """
        Determine if the given integer-valued form is primitive.

        This means not an integer (`> 1`) multiple of another integer-valued
        quadratic form.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [2,3,4])
            sage: Q.is_primitive()
            True
            sage: Q = QuadraticForm(ZZ, 2, [2,4,8])
            sage: Q.is_primitive()
            False
        """
    def primitive(self):
        """
        Return a primitive version of an integer-valued quadratic form, defined over `\\ZZ`.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [2,3,4])
            sage: Q.primitive()
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 2 3 ]
            [ * 4 ]
            sage: Q = QuadraticForm(ZZ, 2, [2,4,8])
            sage: Q.primitive()
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 2 ]
            [ * 4 ]
        """
    def adjoint_primitive(self):
        """
        Return the primitive adjoint of the quadratic form, which is
        the smallest discriminant integer-valued quadratic form whose
        matrix is a scalar multiple of the inverse of the matrix of
        the given quadratic form.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.adjoint_primitive()
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 3 -2 ]
            [ *  1 ]
        """
    def dim(self):
        """
        Return the number of variables of the quadratic form.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.dim()
            2
            sage: parent(Q.dim())
            Integer Ring
            sage: Q = QuadraticForm(Q.matrix())
            sage: Q.dim()
            2
            sage: parent(Q.dim())
            Integer Ring
        """
    def base_ring(self):
        """
        Return the ring over which the quadratic form is defined.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.base_ring()
            Integer Ring
        """
    def coefficients(self):
        """
        Return the matrix of upper triangular coefficients,
        by reading across the rows from the main diagonal.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.coefficients()
            [1, 2, 3]
        """
    def det(self):
        """
        Return the determinant of the Gram matrix of `2\\cdot Q`, or
        equivalently the determinant of the Hessian matrix of `Q`.

        .. NOTE::

            This is always defined over the same ring as the quadratic form.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.det()
            8
        """
    def Gram_det(self):
        """
        Return the determinant of the Gram matrix of `Q`.

        .. NOTE::

            This is defined over the fraction field of the ring of
            the quadratic form, but is often not defined over the same
            ring as the quadratic form.

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, [1,2,3])
            sage: Q.Gram_det()
            2
        """
    def change_ring(self, R):
        """
        Alters the quadratic form to have all coefficients
        defined over the new base ring `R`.  Here `R` must be
        coercible to from the current base ring.

        .. NOTE::

            This is preferable to performing an explicit
            coercion through the :meth:`base_ring` method, which does
            not affect the individual coefficients.  This is
            particularly useful for performing fast modular
            arithmetic evaluations.

        INPUT:

        - ``R`` -- a ring

        OUTPUT: quadratic form

        EXAMPLES::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,1]); Q
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 1 0 ]
            [ * 1 ]

            sage: Q1 = Q.change_ring(IntegerModRing(5)); Q1
            Quadratic form in 2 variables over Ring of integers modulo 5 with coefficients:
            [ 1 0 ]
            [ * 1 ]

            sage: Q1([35,11])
            1
        """
    base_change_to: Incomplete
    def level(self):
        """
        Determines the level of the quadratic form over a PID, which is a
        generator for the smallest ideal `N` of `R` such that `N\\cdot (` the matrix of
        `2*Q` `)^{(-1)}` is in `R` with diagonal in `2R`.

        Over `\\ZZ` this returns a nonnegative number.

        (Caveat: This always returns the unit ideal when working over a field!)

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, range(1,4))
            sage: Q.level()
            8

            sage: Q1 = QuadraticForm(QQ, 2, range(1,4))
            sage: Q1.level()      # random
            UserWarning: Warning -- The level of a quadratic form over a field is always 1.
            Do you really want to do this?!?
            1

            sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
            sage: Q.level()
            420
        """
    def level_ideal(self):
        """
        Determine the level of the quadratic form (over `R`), which is the
        smallest ideal `N` of `R` such that `N \\cdot (` the matrix of `2Q` `)^{(-1)}` is
        in `R` with diagonal in `2R`.
        (Caveat: This always returns the principal ideal when working over a field!)

        .. WARNING::

            This only works over a PID ring of integers for now!
            (Waiting for Sage fractional ideal support.)

        EXAMPLES::

            sage: Q = QuadraticForm(ZZ, 2, range(1,4))
            sage: Q.level_ideal()
            Principal ideal (8) of Integer Ring

            sage: Q1 = QuadraticForm(QQ, 2, range(1,4))
            sage: Q1.level_ideal()
            Principal ideal (1) of Rational Field

            sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
            sage: Q.level_ideal()
            Principal ideal (420) of Integer Ring
        """
    def bilinear_map(self, v, w):
        """
        Return the value of the associated bilinear map on two vectors.

        Given a quadratic form `Q` over some base ring `R` with
        characteristic not equal to 2, this gives the image of two
        vectors with coefficients in `R` under the associated bilinear
        map `B`, given by the relation `2 B(v,w) = Q(v) + Q(w) - Q(v+w)`.

        INPUT:

        - ``v``, ``w`` -- two vectors

        OUTPUT: an element of the base ring `R`

        EXAMPLES:

        First, an example over `\\ZZ`::

            sage: Q = QuadraticForm(ZZ, 3, [1,4,0,1,4,1])
            sage: v = vector(ZZ, (1,2,0))
            sage: w = vector(ZZ, (0,1,1))
            sage: Q.bilinear_map(v, w)
            8

        This also works over `\\QQ`::

            sage: Q = QuadraticForm(QQ, 2, [1/2,2,1])
            sage: v = vector(QQ, (1,1))
            sage: w = vector(QQ, (1/2,2))
            sage: Q.bilinear_map(v, w)
            19/4

        The vectors must have the correct length::

            sage: Q = DiagonalQuadraticForm(ZZ, [1,7,7])
            sage: v = vector((1,2))
            sage: w = vector((1,1,1))
            sage: Q.bilinear_map(v, w)
            Traceback (most recent call last):
            ...
            TypeError: vectors must have length 3

        This does not work if the characteristic is 2::

            sage: # needs sage.rings.finite_rings
            sage: Q = DiagonalQuadraticForm(GF(2), [1,1,1])
            sage: v = vector((1,1,1))
            sage: w = vector((1,1,1))
            sage: Q.bilinear_map(v, w)
            Traceback (most recent call last):
            ...
            TypeError: not defined for rings of characteristic 2
        """

def DiagonalQuadraticForm(R, diag):
    """
    Return a quadratic form over `R` which is a sum of squares.

    INPUT:

    - ``R`` -- ring
    - ``diag`` -- list/tuple of elements coercible to `R`

    OUTPUT: quadratic form

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7]); Q
        Quadratic form in 4 variables over Integer Ring with coefficients:
        [ 1 0 0 0 ]
        [ * 3 0 0 ]
        [ * * 5 0 ]
        [ * * * 7 ]
    """
