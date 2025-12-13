from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd
from sage.categories.rings import Rings as Rings
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.prandom import randint as randint
from sage.quadratic_forms.quadratic_form import QuadraticForm as QuadraticForm
from sage.rings.finite_rings.integer_mod import mod as mod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygens as polygens
from sage.structure.element import Matrix as Matrix, Vector as Vector
from sage.structure.sage_object import SageObject as SageObject

class TernaryQF(SageObject):
    """
    The ``TernaryQF`` class represents a quadratic form in 3 variables with coefficients in `\\ZZ`.

    INPUT:

    - ``v`` -- list or tuple of 6 entries:  ``[a,b,c,r,s,t]``

    OUTPUT: the ternary quadratic form `a\\cdot x^2 + b\\cdot y^2 + c\\cdot z^2 + r\\cdot y\\cdot z + s\\cdot x\\cdot z + t\\cdot x\\cdot y`

    EXAMPLES::

        sage: Q = TernaryQF([1, 2, 3, 4, 5, 6]); Q
        Ternary quadratic form with integer coefficients:
        [1 2 3]
        [4 5 6]
        sage: A = matrix(ZZ, 3, [1, -7, 1, 0, -2, 1, 0, -1, 0])
        sage: Q(A)
        Ternary quadratic form with integer coefficients:
        [1 187 9]
        [-85 8 -31]
        sage: TestSuite(TernaryQF).run()
    """
    possible_automorphisms: Incomplete
    def __init__(self, v) -> None:
        """
        Create the ternary quadratic form `a\\cdot x^2 + b\\cdot y^2 + c\\cdot z^2 + r\\cdot y\\cdot z + s\\cdot x\\cdot z + t\\cdot x\\cdot y` from the
        tuple ``v=[a,b,c,r,s,t]`` over `\\ZZ`.

        INPUT:

        - ``v`` -- 6-tuple of integers

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 4, 5, 6]); Q
            Ternary quadratic form with integer coefficients:
            [1 2 3]
            [4 5 6]
        """
    def coefficients(self) -> tuple:
        """
        Return the tuple of coefficients of the ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 4, 5, 6]); Q
            Ternary quadratic form with integer coefficients:
            [1 2 3]
            [4 5 6]
            sage: Q.coefficients()
            (1, 2, 3, 4, 5, 6)
        """
    def __hash__(self) -> int:
        """
        Return a hash for ``self``.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 4, 5, 6])
            sage: Q.__hash__()
            5881802312257552497  # 64-bit
            1770036893           # 32-bit
        """
    def coefficient(self, n):
        """
        Return the `n`-th coefficient of the ternary quadratic form.

        INPUT:

        - ``n`` -- integer with `0 \\leq n \\leq 5`

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 4, 5, 6]); Q
            Ternary quadratic form with integer coefficients:
            [1 2 3]
            [4 5 6]
            sage: Q.coefficient(2)
            3
            sage: Q.coefficient(5)
            6
        """
    def polynomial(self, names: str = 'x,y,z'):
        """
        Return the polynomial associated to the ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 0, 2, -3, -1]); Q
            Ternary quadratic form with integer coefficients:
            [1 1 0]
            [2 -3 -1]
            sage: p = Q.polynomial(); p
            x^2 - x*y + y^2 - 3*x*z + 2*y*z
            sage: p.parent()
            Multivariate Polynomial Ring in x, y, z over Integer Ring
        """
    def __call__(self, v):
        """
        Evaluate this ternary quadratic form `Q` on a vector of 3 elements,
        or matrix of elements in Z, with 3 rows.

        OUTPUT:

        If a vector is given, then the output will be an integer `Q(v)`,
        but if a matrix is given, the output will be a ternary quadratic form
        if the matrix has 3 columns, or a quadratic form if not.
        The quadratic form in matrix notation will be:

        .. MATH::

            Q' = v^t\\cdot Q\\cdot v.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 1, -1, -2, -3])
            sage: Q((1, 1, 1))
            -3
            sage: M = matrix(ZZ, 3, 2, [358, 6, 2, 0, 0, 4])
            sage: Q(M)
            Quadratic form in 2 variables over Integer Ring with coefficients:
            [ 126020 1388 ]
            [ * 4 ]
            sage: M = matrix(ZZ, 3, 3, [1, 3, 0, -1, 4, 2, 1, -1, -1])
            sage: M
            [ 1  3  0]
            [-1  4  2]
            [ 1 -1 -1]
            sage: Q(M)
            Ternary quadratic form with integer coefficients:
            [5 0 7]
            [12 -13 -16]
        """
    def quadratic_form(self):
        """
        Return a :class:`QuadraticForm` with the same coefficients as ``self`` over `\\ZZ`.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 1, 1, 1])
            sage: QF1 = Q.quadratic_form(); QF1
            Quadratic form in 3 variables over Integer Ring with coefficients:
            [ 1 1 1 ]
            [ * 2 1 ]
            [ * * 3 ]
            sage: QF2 = QuadraticForm(ZZ, 3, [1, 1, 1, 2, 1, 3])
            sage: bool(QF1 == QF2)
            True
        """
    def matrix(self):
        """
        Return the Hessian matrix associated to the ternary quadratic form.

        That is, if `Q` is a ternary quadratic form, `Q(x,y,z) = a\\cdot x^2 + b\\cdot y^2 + c\\cdot z^2 + r\\cdot y\\cdot z + s\\cdot x\\cdot z + t\\cdot x\\cdot y`,
        then the Hessian matrix associated to `Q` is
        ::

            [2\\cdot a t s]
            [t 2\\cdot b r]
            [s r 2\\cdot c]

        EXAMPLES::

            sage: Q = TernaryQF([1,1,2,0,-1,4]); Q
            Ternary quadratic form with integer coefficients:
            [1 1 2]
            [0 -1 4]
            sage: M = Q.matrix(); M
            [ 2  4 -1]
            [ 4  2  0]
            [-1  0  4]
            sage: v = vector((1, 2, 3))
            sage: Q(v)
            28
            sage: (v*M*v.column())[0]//2
            28
        """
    def disc(self):
        """
        Return the discriminant of the ternary quadratic form.

        This is the determinant of the matrix divided by 2.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 2, 0, -1, 4])
            sage: Q.disc()
            -25
            sage: Q.matrix().det()
            -50
        """
    def is_definite(self) -> bool:
        """
        Determine if the ternary quadratic form is definite.

        EXAMPLES::

            sage: Q = TernaryQF([10, 10, 1, -1, 2, 3])
            sage: Q.is_definite()
            True
            sage: (-Q).is_definite()
            True
            sage: Q = TernaryQF([1, 1, 2, -3, 0, -1])
            sage: Q.is_definite()
            False
        """
    def is_positive_definite(self) -> bool:
        """
        Determine if the ternary quadratic form is positive definite.

        EXAMPLES::

            sage: Q = TernaryQF([10, 10, 1, -1, 2, 3])
            sage: Q.is_positive_definite()
            True
            sage: (-Q).is_positive_definite()
            False
            sage: Q = TernaryQF([1, 1, 0, 0, 0, 0])
            sage: Q.is_positive_definite()
            False
            sage: Q = TernaryQF([1, 1, 1, -1, -2, -3])
            sage: Q((1,1,1))
            -3
            sage: Q.is_positive_definite()
            False
        """
    def is_negative_definite(self) -> bool:
        """
        Determine if the ternary quadratic form is negative definite.

        EXAMPLES::

            sage: Q = TernaryQF([-8, -9, -10, 1, 9, -3])
            sage: Q.is_negative_definite()
            True
            sage: Q = TernaryQF([-4, -1, 6, -5, 1, -5])
            sage: Q((0, 0, 1))
            6
            sage: Q.is_negative_definite()
            False
        """
    def __neg__(self):
        """
        Return the ternary quadratic form with coefficients negatives of ``self``.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 2, -2, 0, -1]); Q
            Ternary quadratic form with integer coefficients:
            [1 1 2]
            [-2 0 -1]
            sage: -Q
            Ternary quadratic form with integer coefficients:
            [-1 -1 -2]
            [2 0 1]
            sage: Q = TernaryQF([0, 0, 0, 0, 0, 0])
            sage: Q == -Q
            True
        """
    def is_primitive(self) -> bool:
        """
        Determine if the ternary quadratic form is primitive.

        This means that the greatest common divisor of the coefficients
        of the form is 1.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 4, 5, 6])
            sage: Q.is_primitive()
            True
            sage: Q.content()
            1
            sage: Q = TernaryQF([10, 10, 10, 5, 5, 5])
            sage: Q.content()
            5
            sage: Q.is_primitive()
            False
        """
    def primitive(self):
        """
        Return the primitive version of the ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([2, 2, 2, 1, 1, 1])
            sage: Q.is_primitive()
            True
            sage: Q.primitive()
            Ternary quadratic form with integer coefficients:
            [2 2 2]
            [1 1 1]
            sage: Q.primitive() == Q
            True
            sage: Q = TernaryQF([10, 10, 10, 5, 5, 5])
            sage: Q.primitive()
            Ternary quadratic form with integer coefficients:
            [2 2 2]
            [1 1 1]
        """
    def scale_by_factor(self, k):
        """
        Scale the values of the ternary quadratic form by the number ``k``.

        OUTPUT:

        If ``k`` times the content of the ternary quadratic form is an integer, return a ternary quadratic form;
        otherwise, return a quadratic form of dimension 3.

        EXAMPLES::

            sage: Q = TernaryQF([2, 2, 4, 0, -2, 8])
            sage: Q
            Ternary quadratic form with integer coefficients:
            [2 2 4]
            [0 -2 8]
            sage: Q.scale_by_factor(5)
            Ternary quadratic form with integer coefficients:
            [10 10 20]
            [0 -10 40]
            sage: Q.scale_by_factor(1/2)
            Ternary quadratic form with integer coefficients:
            [1 1 2]
            [0 -1 4]
            sage: Q.scale_by_factor(1/3)
            Quadratic form in 3 variables over Rational Field with coefficients:
            [ 2/3 8/3 -2/3 ]
            [ * 2/3 0 ]
            [ * * 4/3 ]
        """
    def reciprocal(self):
        """
        Return the reciprocal quadratic form associated to the given form.

        This is defined as the multiple of the primitive adjoint with the same
        content as the given form.

        EXAMPLES::

            sage: Q = TernaryQF([2, 2, 14, 0, 0, 0])
            sage: Q.reciprocal()
            Ternary quadratic form with integer coefficients:
            [14 14 2]
            [0 0 0]
            sage: Q.content()
            2
            sage: Q.reciprocal().content()
            2
            sage: Q.adjoint().content()
            16
        """
    def reciprocal_reduced(self):
        """
        Return the reduced form of the reciprocal form of the given ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 3, 0, -1, 0])
            sage: Qrr = Q.reciprocal_reduced(); Qrr
            Ternary quadratic form with integer coefficients:
            [4 11 12]
            [0 -4 0]
            sage: Q.is_eisenstein_reduced()
            True
            sage: Qr = Q.reciprocal()
            sage: Qr.reduced_form_eisenstein(matrix=False) == Qrr
            True
        """
    def divisor(self):
        """
        Return the content of the adjoint form associated to the given form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 17, 0, 0, 0])
            sage: Q.divisor()
            4
        """
    def __eq__(self, right) -> bool:
        """
        Determine if two ternary quadratic forms are equal.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 3, 1, 2, 3])
            sage: Q == Q
            True
            sage: Q1 = TernaryQF([1, 2, 3, 1, 2, 2])
            sage: Q == Q1
            False
        """
    def adjoint(self):
        """
        Return the adjoint form associated to the given ternary quadratic
        form.

        That is, the Hessian matrix of the adjoint form is twice the
        classical adjoint matrix of the Hessian matrix of the given form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 17, 0, 0, 1])
            sage: Q.adjoint()
            Ternary quadratic form with integer coefficients:
            [68 68 3]
            [0 0 -68]
            sage: Q.adjoint().matrix() == 2*Q.matrix().adjoint_classical()
            True
        """
    def content(self):
        """
        Return the greatest common divisor of the coefficients of the given ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 2, 0, 0, 0])
            sage: Q.content()
            1
            sage: Q = TernaryQF([2, 4, 6, 0, 0, 0])
            sage: Q.content()
            2
            sage: Q.scale_by_factor(100).content()
            200
        """
    def omega(self):
        """
        Return the content of the adjoint of the primitive associated
        ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([4, 11, 12, 0, -4, 0])
            sage: Q.omega()
            176
            sage: Q.primitive().adjoint().content()
            176
        """
    def delta(self):
        """
        Return the omega of the adjoint of the given ternary quadratic form,
        which is the same as the omega of the reciprocal form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 2, -1, 0, -1])
            sage: Q.delta()
            208
            sage: Q.adjoint().omega()
            208
            sage: Q = TernaryQF([1, -1, 1, 0, 0, 0])
            sage: Q.delta()
            4
            sage: Q.omega()
            4
        """
    def level(self):
        """
        Return the level of the ternary quadratic form, which is 4 times the discriminant divided by the divisor.

        EXAMPLES::

            sage: Q = TernaryQF([1, 2, 2, -1, 0, -1])
            sage: Q.level()
            52
            sage: 4*Q.disc()/Q.divisor()
            52
        """
    def is_eisenstein_reduced(self) -> bool:
        """
        Determine if the ternary quadratic form is Eisenstein reduced.

        That is, if we have a ternary quadratic form:
        ::

        [a b c]
        [r s t]

        then

        1. `a \\leq b \\leq c`;
        2. `r`, `s`, and `t` are all positive or all nonpositive;
        3. `a \\geq |t|`; `a \\geq |s|`; `b \\geq |r|`;
        4. `a+b+r+s+t \\geq 0`;
        5. `a=t` implies `s \\leq 2\\cdot r`; `a=s` implies `t \\leq 2\\cdot r`; `b=r` implies `t \\leq 2\\cdot s`;
        6. `a=-t` implies `s=0`; `a=-s` implies `t=0`; `b=-r` implies `t=0`;
        7. `a+b+r+s+t = 0` implies `2\\cdot a+2\\cdot s+t \\leq 0`;
        8. `a=b` implies `|r| \\leq |s|`; `b=c` implies `|s| \\leq |t|`.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 1, 0, 0, 0])
            sage: Q.is_eisenstein_reduced()
            True
            sage: Q = TernaryQF([34, 14, 44, 12, 25, -22])
            sage: Q.is_eisenstein_reduced()
            False
        """
    def reduced_form_eisenstein(self, matrix: bool = True):
        """
        Return the Eisenstein reduced form equivalent to the given positive ternary quadratic form,
        which is unique.

        EXAMPLES::

            sage: Q = TernaryQF([293, 315, 756, 908, 929, 522])
            sage: Qr, m = Q.reduced_form_eisenstein()
            sage: Qr
            Ternary quadratic form with integer coefficients:
            [1 2 2]
            [-1 0 -1]
            sage: Qr.is_eisenstein_reduced()
            True
            sage: m
            [ -54  137  -38]
            [ -23   58  -16]
            [  47 -119   33]
            sage: m.det()
            1
            sage: Q(m) == Qr
            True
            sage: Q = TernaryQF([12,36,3,14,-7,-19])
            sage: Q.reduced_form_eisenstein(matrix = False)
            Ternary quadratic form with integer coefficients:
            [3 8 20]
            [3 2 1]
        """
    def pseudorandom_primitive_zero_mod_p(self, p):
        """
        Return a tuple of the form `v = (a, b, 1)` such that is a zero of the given ternary quadratic
        positive definite form modulo an odd prime `p`, where `p` doesn't divides the discriminant of the form.

        EXAMPLES::

             sage: Q = TernaryQF([1, 1, 11, 0, -1, 0])
             sage: Q.disc()
             43
             sage: Q.pseudorandom_primitive_zero_mod_p(3)  # random
             (1, 2, 1)
             sage: Q((1, 2, 1))
             15
             sage: v = Q.pseudorandom_primitive_zero_mod_p(1009)                        # needs sage.libs.pari
             sage: Q(v) % 1009                                                          # needs sage.libs.pari
             0
             sage: v[2]                                                                 # needs sage.libs.pari
             1
        """
    def find_zeros_mod_p(self, p):
        """
        Find the zeros of the given ternary quadratic positive definite form modulo a prime `p`, where `p` doesn't divide the discriminant of the form.

        EXAMPLES::

            sage: Q = TernaryQF([4, 7, 8, -4, -1, -3])
            sage: Q.is_positive_definite()
            True
            sage: Q.disc().factor()
            3 * 13 * 19
            sage: Q.find_zeros_mod_p(2)
            [(1, 0, 0), (1, 1, 0), (0, 0, 1)]
            sage: zeros_17 = Q.find_zeros_mod_p(17)                                     # needs sage.libs.pari
            sage: len(zeros_17)                                                         # needs sage.libs.pari
            18
            sage: [Q(v)%17 for v in zeros_17]                                           # needs sage.libs.pari
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        """
    def find_p_neighbor_from_vec(self, p, v, mat: bool = False):
        """
        Finds the reduced equivalent of the `p`-neighbor of this ternary quadratic form associated to a given
        vector `v` satisfying:

        1. `Q(v) = 0`  (mod `p`)

        2. `v` is a non-singular point of the conic `Q(v) = 0` (mod `p`).

        REFERENCES:

        Gonzalo Tornaria's Thesis, Thrm 3.5, p34.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: Q = TernaryQF([1, 3, 3, -2, 0, -1]); Q
            Ternary quadratic form with integer coefficients:
            [1 3 3]
            [-2 0 -1]
            sage: Q.disc()
            29
            sage: v = (9, 7, 1)
            sage: v in Q.find_zeros_mod_p(11)
            True
            sage: Q11, M = Q.find_p_neighbor_from_vec(11, v, mat=True)
            sage: Q11
            Ternary quadratic form with integer coefficients:
            [1 2 4]
            [-1 -1 0]
            sage: M
            [    -1  -5/11   7/11]
            [     0 -10/11   3/11]
            [     0  -3/11  13/11]
            sage: Q(M) == Q11
            True

        Test that it works with (0, 0, 1)::

            sage: Q.find_p_neighbor_from_vec(3, (0,0,1))                                # needs sage.libs.pari
            Ternary quadratic form with integer coefficients:
            [1 3 3]
            [-2 0 -1]
        """
    def find_p_neighbors(self, p, mat: bool = False):
        """
        Find a list with all the reduced equivalent of the `p`-neighbors of this ternary quadratic form, given by the zeros mod `p` of the form.
        See :meth:`find_p_neighbor_from_vec` for more information.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: Q0 = TernaryQF([1, 3, 3, -2, 0, -1]); Q0
            Ternary quadratic form with integer coefficients:
            [1 3 3]
            [-2 0 -1]
            sage: neig = Q0.find_p_neighbors(5)
            sage: len(neig)
            6
            sage: Q1 = TernaryQF([1, 1, 10, 1, 1, 1])
            sage: Q2 = TernaryQF([1, 2, 4, -1, -1, 0])
            sage: neig.count(Q0)
            2
            sage: neig.count(Q1)
            1
            sage: neig.count(Q2)
            3
        """
    def basic_lemma(self, p):
        """
        Find a number represented by ``self`` and coprime to the prime `p`.

        EXAMPLES::

            sage: Q = TernaryQF([3, 3, 3, -2, 0, -1])
            sage: Q.basic_lemma(3)
            4
        """
    def xi(self, p):
        '''
        Return the value of the genus characters Xi_p... which may be
        missing one character. We allow `-1` as a prime.

        REFERENCES:

        Dickson\'s "Studies in the Theory of Numbers"

        EXAMPLES::

            sage: Q1 = TernaryQF([26, 42, 53, -36, -17, -3])
            sage: Q2 = Q1.find_p_neighbors(2)[1]
            sage: Q1.omega()
            3
            sage: Q1.xi(3), Q2.xi(3)
            (-1, -1)
        '''
    def xi_rec(self, p):
        """
        Return Xi(p) for the reciprocal form.

        EXAMPLES::

            sage: Q1 = TernaryQF([1, 1, 7, 0, 0, 0])
            sage: Q2 = Q1.find_p_neighbors(3)[0]
            sage: Q1.delta()
            28
            sage: Q1.xi_rec(7), Q2.xi_rec(7)
            (1, 1)
        """
    def symmetry(self, v):
        """
        Return `A`, the automorphism of the ternary quadratic form such that:

        - `Av = -v`,
        - `Au = 0`, if `u` is orthogonal to `v`,

        where `v` is a given vector.

        EXAMPLES::

            sage: Q = TernaryQF([4, 5, 8, 5, 2, 2])
            sage: v = vector((1,1,1))
            sage: M = Q.symmetry(v)
            sage: M
            [  7/13 -17/26 -23/26]
            [ -6/13   9/26 -23/26]
            [ -6/13 -17/26   3/26]
            sage: M.det()
            -1
            sage: M*v
            (-1, -1, -1)
            sage: v1 = vector((23, 0, -12))
            sage: v2 = vector((0, 23, -17))
            sage: v1*Q.matrix()*v
            0
            sage: v2*Q.matrix()*v
            0
            sage: M*v1 == v1
            True
            sage: M*v2 == v2
            True
        """
    def automorphism_symmetries(self, A) -> list:
        """
        Given the automorphism `A`, if `A` is the identity, return the empty list.
        Otherwise, return a list of two vectors `v_1`, `v_2` such that the product of
        the symmetries of the ternary quadratic form given by the two vectors is `A`.

        EXAMPLES::

            sage: Q = TernaryQF([9, 12, 30, -26, -28, 20])
            sage: A = matrix(ZZ, 3, [9, 10, -10, -6, -7, 6, 2, 2, -3])
            sage: Q(A) == Q
            True
            sage: v1, v2 = Q.automorphism_symmetries(A)
            sage: v1, v2
            ((8, -6, 2), (1, -5/4, -1/4))
            sage: A1 = Q.symmetry(v1)
            sage: A1
            [    9     9   -13]
            [   -6 -23/4  39/4]
            [    2   9/4  -9/4]
            sage: A2 = Q.symmetry(v2)
            sage: A2
            [    1     1     3]
            [    0  -1/4 -15/4]
            [    0  -1/4   1/4]
            sage: A1*A2 == A
            True
            sage: Q.automorphism_symmetries(identity_matrix(ZZ,3))
            []
        """
    def automorphism_spin_norm(self, A):
        """
        Return the spin norm of the automorphism `A`.

        EXAMPLES::

            sage: Q = TernaryQF([9, 12, 30, -26, -28, 20])
            sage: A = matrix(ZZ, 3, [9, 10, -10, -6, -7, 6, 2, 2, -3])
            sage: A.det()
            1
            sage: Q(A) == Q
            True
            sage: Q.automorphism_spin_norm(A)
            7
        """
    def automorphisms(self, slow: bool = True):
        """
        Return a list with the automorphisms of the definite ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 7, 0, 0, 0])
            sage: auts = Q.automorphisms(); auts
            [
            [-1  0  0]  [-1  0  0]  [ 0 -1  0]  [ 0 -1  0]  [ 0  1  0]  [ 0  1  0]
            [ 0 -1  0]  [ 0  1  0]  [-1  0  0]  [ 1  0  0]  [-1  0  0]  [ 1  0  0]
            [ 0  0  1], [ 0  0 -1], [ 0  0 -1], [ 0  0  1], [ 0  0  1], [ 0  0 -1],
            [ 1  0  0]  [1 0 0]
            [ 0 -1  0]  [0 1 0]
            [ 0  0 -1], [0 0 1]
            ]
            sage: all(Q == Q(A) for A in auts)
            True
            sage: Q = TernaryQF([3, 4, 5, 3, 3, 2])
            sage: Q.automorphisms(slow=False)
            [
            [1 0 0]
            [0 1 0]
            [0 0 1]
            ]
            sage: Q = TernaryQF([4, 2, 4, 3, -4, -5])
            sage: auts = Q.automorphisms(slow=False)
            sage: auts
            [
            [1 0 0]  [ 2 -1 -1]
            [0 1 0]  [ 3 -2 -1]
            [0 0 1], [ 0  0 -1]
            ]
            sage: A = auts[1]
            sage: Q(A) == Q
            True
            sage: Qr, M_red = Q.reduced_form_eisenstein()
            sage: Qr
            Ternary quadratic form with integer coefficients:
            [1 2 3]
            [-1 0 -1]
            sage: Q(A*M_red) == Qr
            True
        """
    def number_of_automorphisms(self, slow: bool = True):
        """
        Return the number of automorphisms of the definite ternary quadratic form.

        EXAMPLES::

            sage: Q = TernaryQF([1, 1, 7, 0, 0, 0])
            sage: A = matrix(ZZ, 3, [0, 1, 0, -1, 5, 0, -8, -1, 1])
            sage: A.det()
            1
            sage: Q1 = Q(A); Q1
            Ternary quadratic form with integer coefficients:
            [449 33 7]
            [-14 -112 102]
            sage: Q1.number_of_automorphisms()
            8
            sage: Q = TernaryQF([-19, -7, -6, -12, 20, 23])
            sage: Q.is_negative_definite()
            True
            sage: Q.number_of_automorphisms(slow=False)
            24
        """

def find_all_ternary_qf_by_level_disc(N, d):
    """
    Find the coefficients of all the reduced ternary quadratic forms given its discriminant `d` and level `N`.

    If `N|4d` and `d|N^2`, then it may be some forms with that discriminant and level.

    EXAMPLES::

        sage: find_all_ternary_qf_by_level_disc(44, 11)
        [Ternary quadratic form with integer coefficients:
        [1 1 3]
        [0 -1 0], Ternary quadratic form with integer coefficients:
        [1 1 4]
        [1 1 1]]
        sage: find_all_ternary_qf_by_level_disc(44, 11^2 * 16)
        [Ternary quadratic form with integer coefficients:
        [3 15 15]
        [-14 -2 -2], Ternary quadratic form with integer coefficients:
        [4 11 12]
        [0 -4 0]]
        sage: Q = TernaryQF([1, 1, 3, 0, -1, 0])
        sage: Q.is_eisenstein_reduced()
        True
        sage: Q.reciprocal_reduced()
        Ternary quadratic form with integer coefficients:
        [4 11 12]
        [0 -4 0]
        sage: find_all_ternary_qf_by_level_disc(44, 22)
        []
        sage: find_all_ternary_qf_by_level_disc(44, 33)
        Traceback (most recent call last):
        ...
        ValueError: There are no ternary forms of this level and discriminant
    """
def find_a_ternary_qf_by_level_disc(N, d):
    """
    Find a reduced ternary quadratic form given its discriminant `d` and level `N`.
    If `N|4d` and `d|N^2`, then it may be a form with that discriminant and level.

    EXAMPLES::

        sage: Q1 = find_a_ternary_qf_by_level_disc(44, 11); Q1
        Ternary quadratic form with integer coefficients:
        [1 1 3]
        [0 -1 0]
        sage: Q2 = find_a_ternary_qf_by_level_disc(44, 11^2 * 16)
        sage: Q2
        Ternary quadratic form with integer coefficients:
        [3 15 15]
        [-14 -2 -2]
        sage: Q1.is_eisenstein_reduced()
        True
        sage: Q1.level()
        44
        sage: Q1.disc()
        11
        sage: find_a_ternary_qf_by_level_disc(44, 22)
        sage: find_a_ternary_qf_by_level_disc(44, 33)
        Traceback (most recent call last):
        ...
        ValueError: There are no ternary forms of this level and discriminant
    """
