from sage.arith.misc import gcd as gcd
from sage.libs.pari import pari as pari
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class BinaryQF(SageObject):
    """
    A binary quadratic form over `\\ZZ`.

    INPUT:

    One of the following:

    - ``a`` -- either a 3-tuple of integers, or a quadratic
      homogeneous polynomial in two variables with integer
      coefficients

    - ``a``, ``b``, ``c`` -- three integers

    OUTPUT: the binary quadratic form `a x^2 + b xy + c y^2`

    EXAMPLES::

        sage: b = BinaryQF([1, 2, 3])
        sage: b.discriminant()
        -8
        sage: b1 = BinaryQF(1, 2, 3)
        sage: b1 == b
        True
        sage: R.<x, y> = ZZ[]
        sage: BinaryQF(x^2 + 2*x*y + 3*y^2) == b
        True
        sage: BinaryQF(1, 0, 1)
        x^2 + y^2
    """
    def __init__(self, a, b=None, c=None) -> None:
        """
        Create a binary quadratic form `ax^2 + bxy + cy^2`.

        INPUT:

        One of the following:

        - ``a`` -- either a 3-tuple of integers, or a quadratic
          homogeneous polynomial in two variables with integer
          coefficients

        - ``a``, ``b``, ``c`` -- three integers

        EXAMPLES::

            sage: Q = BinaryQF([1, 2, 3]); Q
            x^2 + 2*x*y + 3*y^2
            sage: Q = BinaryQF([1, 2])
            Traceback (most recent call last):
            ...
            TypeError: binary quadratic form must be given by a quadratic homogeneous bivariate integer polynomial or its coefficients

            sage: R.<x, y> = ZZ[]
            sage: f = x^2 + 2*x*y + 3*y^2
            sage: BinaryQF(f)
            x^2 + 2*x*y + 3*y^2
            sage: BinaryQF(f + x)
            Traceback (most recent call last):
            ...
            TypeError: binary quadratic form must be given by a quadratic homogeneous bivariate integer polynomial or its coefficients

        TESTS::

            sage: BinaryQF(0)
            0
        """
    @staticmethod
    def principal(D):
        """
        Return the principal binary quadratic form of the given discriminant.

        EXAMPLES::

            sage: BinaryQF.principal(8)
            x^2 - 2*y^2
            sage: BinaryQF.principal(5)
            x^2 + x*y - y^2
            sage: BinaryQF.principal(4)
            x^2 - y^2
            sage: BinaryQF.principal(1)
            x^2 + x*y
            sage: BinaryQF.principal(-3)
            x^2 + x*y + y^2
            sage: BinaryQF.principal(-4)
            x^2 + y^2
            sage: BinaryQF.principal(-7)
            x^2 + x*y + 2*y^2
            sage: BinaryQF.principal(-8)
            x^2 + 2*y^2

        TESTS:

        Some randomized testing::

            sage: D = 1
            sage: while D.is_square():
            ....:     D = choice((-4,+4)) * randrange(9999) + randrange(2)
            sage: Q = BinaryQF.principal(D)
            sage: Q.discriminant() == D     # correct discriminant
            True
            sage: (Q*Q).is_equivalent(Q)    # idempotent (hence identity)
            True
        """
    def __mul__(self, right):
        """
        Gauss composition or right action by a 2x2 integer matrix.

        The result need not be reduced.

        EXAMPLES:

        We explicitly compute in the group of classes of positive
        definite binary quadratic forms of discriminant -23::

            sage: # needs sage.libs.pari
            sage: R = BinaryQF_reduced_representatives(-23, primitive_only=False); R
            [x^2 + x*y + 6*y^2, 2*x^2 - x*y + 3*y^2, 2*x^2 + x*y + 3*y^2]
            sage: R[0] * R[0]
            x^2 + x*y + 6*y^2
            sage: R[1] * R[1]
            4*x^2 + 3*x*y + 2*y^2
            sage: (R[1] * R[1]).reduced_form()
            2*x^2 + x*y + 3*y^2
            sage: (R[1] * R[1] * R[1]).reduced_form()
            x^2 + x*y + 6*y^2

            sage: q1 = BinaryQF(1, 1, 4)
            sage: M = Matrix(ZZ, [[1, 3], [0, 1]])
            sage: q1*M
            x^2 + 7*x*y + 16*y^2
            sage: q1.matrix_action_right(M)
            x^2 + 7*x*y + 16*y^2
            sage: N = Matrix(ZZ, [[1, 0], [1, 0]])
            sage: q1*(M*N) == q1.matrix_action_right(M).matrix_action_right(N)
            True
        """
    def __getitem__(self, n):
        """
        Return the `n`-th component of this quadratic form.

        If this form is `a x^2 + b x y + c y^2`, the 0-th component is `a`,
        the 1-st component is `b`, and `2`-nd component is `c`.

        Indexing is like lists -- negative indices and slices are allowed.

        EXAMPLES::

            sage: Q = BinaryQF([2, 3, 4])
            sage: Q[0]
            2
            sage: Q[2]
            4
            sage: Q[:2]
            (2, 3)
            sage: tuple(Q)
            (2, 3, 4)
            sage: list(Q)
            [2, 3, 4]
        """
    def __call__(self, *args):
        """
        Evaluate this quadratic form at a point.

        INPUT:

        - ``args`` -- x and y values, as a pair x, y or a list, tuple, or
          vector

        EXAMPLES::

            sage: Q = BinaryQF([2, 3, 4])
            sage: Q(1, 2)
            24

        TESTS::

            sage: Q = BinaryQF([2, 3, 4])
            sage: Q([1, 2])
            24
            sage: Q((1, 2))
            24
            sage: Q(vector([1, 2]))
            24
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(BinaryQF([2, 2, 3]))
            802
            sage: hash(BinaryQF([2, 3, 2]))
            562
            sage: hash(BinaryQF([3, 2, 2]))
            547
        """
    def __eq__(self, right):
        """
        Return ``True`` if ``self`` and ``right`` are identical.

        This means that they have the same coefficients.

        EXAMPLES::

            sage: P = BinaryQF([2, 2, 3])
            sage: Q = BinaryQF([2, 2, 3])
            sage: R = BinaryQF([1, 2, 3])
            sage: P == Q # indirect doctest
            True
            sage: P == R # indirect doctest
            False

        TESTS::

            sage: P == P
            True
            sage: Q == P
            True
            sage: R == P
            False
            sage: P == 2
            False
        """
    def __ne__(self, right):
        """
        Return ``True`` if ``self`` and ``right`` are not identical.

        This means that they have different coefficients.

        EXAMPLES::

            sage: P = BinaryQF([2, 2, 3])
            sage: Q = BinaryQF([2, 2, 3])
            sage: R = BinaryQF([1, 2, 3])
            sage: P != Q # indirect doctest
            False
            sage: P != R # indirect doctest
            True
        """
    def __lt__(self, right):
        """
        Compare the coefficients of ``self`` and ``right``.

        This is done lexicographically.

        EXAMPLES::

            sage: P = BinaryQF([2, 2, 3])
            sage: Q = BinaryQF([1, 2, 3])
            sage: P < Q
            False
            sage: Q < P
            True
            sage: Q <= P
            True
        """
    def __add__(self, Q):
        """
        Return the component-wise sum of two forms.

        Given `a_1 x^2 + b_1 x y + c_1 y^2` and `a_2 x^2 + b_2 x y +
        c_2 y^2`, this returns the form `(a_1 + a_2) x^2 + (b_1 + b_2)
        x y + (c_1 + c_2) y^2.`

        EXAMPLES::

            sage: P = BinaryQF([2, 2, 3]); P
            2*x^2 + 2*x*y + 3*y^2
            sage: Q = BinaryQF([-1, 2, 2]); Q
            -x^2 + 2*x*y + 2*y^2
            sage: P + Q
            x^2 + 4*x*y + 5*y^2
            sage: P + Q == BinaryQF([1, 4, 5]) # indirect doctest
            True

        TESTS::

            sage: Q + P == BinaryQF([1, 4, 5]) # indirect doctest
            True
        """
    def __sub__(self, Q):
        """
        Return the component-wise difference of two forms.

        Given two forms `a_1 x^2 + b_1 x y + c_1 y^2` and `a_2 x^2 +
        b_2 x y + c_2 y^2`, this returns the form `(a_1 - a_2) x^2 +
        (b_1 - b_2) x y + (c_1 - c_2) y^2.`

        EXAMPLES::

            sage: P = BinaryQF([2, 2, 3]); P
            2*x^2 + 2*x*y + 3*y^2
            sage: Q = BinaryQF([-1, 2, 2]); Q
            -x^2 + 2*x*y + 2*y^2
            sage: P - Q
            3*x^2 + y^2
            sage: P - Q == BinaryQF([3, 0, 1]) # indirect doctest
            True

        TESTS::

            sage: Q - P == BinaryQF([3, 0, 1]) # indirect doctest
            False
            sage: Q - P != BinaryQF([3, 0, 1]) # indirect doctest
            True
        """
    def __neg__(self):
        """
        Return the negative of this binary quadratic form.

        EXAMPLES::

            sage: Q = BinaryQF([1,-2,3])
            sage: -Q
            -x^2 + 2*x*y - 3*y^2
            sage: -Q == BinaryQF([0,0,0]) - Q
            True
        """
    @cached_method
    def content(self):
        """
        Return the content of the form, i.e., the `\\gcd` of the coefficients.

        EXAMPLES::

            sage: Q = BinaryQF(22, 14, 10)
            sage: Q.content()
            2
            sage: Q = BinaryQF(4, 4, -15)
            sage: Q.content()
            1
        """
    def polynomial(self):
        """
        Return ``self`` as a homogeneous 2-variable polynomial.

        EXAMPLES::

            sage: Q = BinaryQF([1, 2, 3])
            sage: Q.polynomial()
            x^2 + 2*x*y + 3*y^2

            sage: Q = BinaryQF([-1, -2, 3])
            sage: Q.polynomial()
            -x^2 - 2*x*y + 3*y^2

            sage: Q = BinaryQF([0, 0, 0])
            sage: Q.polynomial()
            0
        """
    @staticmethod
    def from_polynomial(poly):
        """
        Construct a :class:`BinaryQF` from a bivariate polynomial
        with integer coefficients. Inverse of :meth:`polynomial`.

        EXAMPLES::

            sage: R.<u,v> = ZZ[]
            sage: f = u^2 + 419*v^2
            sage: Q = BinaryQF.from_polynomial(f); Q
            x^2 + 419*y^2
            sage: Q.polynomial()
            x^2 + 419*y^2
            sage: Q.polynomial()(R.gens()) == f
            True

        The method fails if the given polynomial is not a quadratic form::

            sage: BinaryQF.from_polynomial(u^3 - 5*v)
            Traceback (most recent call last):
            ...
            ValueError: polynomial has monomials of degree != 2

        ...or if the coefficients aren't integers::

            sage: BinaryQF.from_polynomial(u^2/7 + v^2)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer
        """
    @cached_method
    def discriminant(self):
        """
        Return the discriminant of ``self``.

        Given a form `ax^2 + bxy + cy^2`, this returns `b^2 - 4ac`.

        EXAMPLES::

            sage: Q = BinaryQF([1, 2, 3])
            sage: Q.discriminant()
            -8
        """
    def determinant(self):
        """
        Return the determinant of the matrix associated to ``self``.

        The determinant is used by Gauss and by Conway-Sloane, for
        whom an integral quadratic form has coefficients `(a, 2b, c)`
        with `a`, `b`, `c` integers.

        OUTPUT: the determinant of the matrix::

            [  a  b/2]
            [b/2    c]

        as a rational.

        REMARK:

        This is just `-D/4` where `D` is the discriminant.  The return
        type is rational even if `b` (and hence `D`) is even.

        EXAMPLES::

            sage: q = BinaryQF(1, -1, 67)
            sage: q.determinant()
            267/4
        """
    det = determinant
    @cached_method
    def has_fundamental_discriminant(self) -> bool:
        """
        Return whether the discriminant `D` of this form is a
        fundamental discriminant (i.e. `D` is the smallest element
        of its squareclass with `D = 0` or `1` modulo `4`).

        EXAMPLES::

            sage: Q = BinaryQF([1, 0, 1])
            sage: Q.discriminant()
            -4
            sage: Q.has_fundamental_discriminant()                                      # needs sage.libs.pari
            True

            sage: Q = BinaryQF([2, 0, 2])
            sage: Q.discriminant()
            -16
            sage: Q.has_fundamental_discriminant()                                      # needs sage.libs.pari
            False
        """
    def is_primitive(self) -> bool:
        """
        Return whether the form `ax^2 + bxy + cy^2` satisfies
        `\\gcd(a, b, c) = 1`, i.e., is primitive.

        EXAMPLES::

            sage: Q = BinaryQF([6, 3, 9])
            sage: Q.is_primitive()
            False

            sage: Q = BinaryQF([1, 1, 1])
            sage: Q.is_primitive()
            True

            sage: Q = BinaryQF([2, 2, 2])
            sage: Q.is_primitive()
            False

            sage: rqf = BinaryQF_reduced_representatives(-23*9, primitive_only=False)
            sage: [qf.is_primitive() for qf in rqf]
            [True, True, True, False, True, True, False, False, True]
            sage: rqf
            [x^2 + x*y + 52*y^2,
            2*x^2 - x*y + 26*y^2,
            2*x^2 + x*y + 26*y^2,
            3*x^2 + 3*x*y + 18*y^2,
            4*x^2 - x*y + 13*y^2,
            4*x^2 + x*y + 13*y^2,
            6*x^2 - 3*x*y + 9*y^2,
            6*x^2 + 3*x*y + 9*y^2,
            8*x^2 + 7*x*y + 8*y^2]
            sage: [qf for qf in rqf if qf.is_primitive()]
            [x^2 + x*y + 52*y^2,
            2*x^2 - x*y + 26*y^2,
            2*x^2 + x*y + 26*y^2,
            4*x^2 - x*y + 13*y^2,
            4*x^2 + x*y + 13*y^2,
            8*x^2 + 7*x*y + 8*y^2]

        .. SEEALSO::

            :meth:`content`
        """
    def is_zero(self) -> bool:
        """
        Return whether ``self`` is identically zero.

        EXAMPLES::

            sage: Q = BinaryQF(195751, 37615, 1807)
            sage: Q.is_zero()
            False
            sage: Q = BinaryQF(0, 0, 0)
            sage: Q.is_zero()
            True
        """
    @cached_method
    def is_weakly_reduced(self) -> bool:
        """
        Check if the form `ax^2 + bxy + cy^2` satisfies
        `|b| \\leq a \\leq c`, i.e., is weakly reduced.

        EXAMPLES::

            sage: Q = BinaryQF([1, 2, 3])
            sage: Q.is_weakly_reduced()
            False

            sage: Q = BinaryQF([2, 1, 3])
            sage: Q.is_weakly_reduced()
            True

            sage: Q = BinaryQF([1, -1, 1])
            sage: Q.is_weakly_reduced()
            True
        """
    @cached_method
    def is_reducible(self) -> bool:
        """
        Return whether this form is reducible and cache the result.

        A binary form `q` is called reducible if it is the product of
        two linear forms `q = (a x + b y) (c x + d y)`, or
        equivalently if its discriminant is a square.

        EXAMPLES::

            sage: q = BinaryQF([1, 0, -1])
            sage: q.is_reducible()
            True

        .. WARNING::

            Despite the similar name, this method is unrelated to
            reduction of binary quadratic forms as implemented by
            :meth:`reduced_form` and :meth:`is_reduced`.
        """
    @cached_method
    def reduced_form(self, transformation: bool = False, algorithm: str = 'default'):
        """
        Return a reduced form equivalent to ``self``.

        INPUT:

        - ``self`` -- binary quadratic form of non-square discriminant

        - ``transformation`` -- boolean (default: ``False``); if ``True``, return
          both the reduced form and a matrix whose :meth:`matrix_action_right`
          transforms ``self`` into the reduced form

        - ``algorithm`` -- string; the algorithm to use. Valid options are:

          * ``'default'`` -- let Sage pick an algorithm (default)
          * ``'pari'`` -- use PARI (:pari:`qfbred` or :pari:`qfbredsl2`)
          * ``'sage'`` -- use Sage

        .. SEEALSO::

            - :meth:`is_reduced`
            - :meth:`is_equivalent`

        EXAMPLES::

            sage: a = BinaryQF([33, 11, 5])
            sage: a.is_reduced()
            False
            sage: b = a.reduced_form(); b                                               # needs sage.libs.pari
            5*x^2 - x*y + 27*y^2
            sage: b.is_reduced()                                                        # needs sage.libs.pari
            True

            sage: a = BinaryQF([15, 0, 15])
            sage: a.is_reduced()
            True
            sage: b = a.reduced_form(); b                                               # needs sage.libs.pari
            15*x^2 + 15*y^2
            sage: b.is_reduced()                                                        # needs sage.libs.pari
            True

        Examples of reducing indefinite forms::

            sage: f = BinaryQF(1, 0, -3)
            sage: f.is_reduced()
            False
            sage: g = f.reduced_form(); g                                               # needs sage.libs.pari
            x^2 + 2*x*y - 2*y^2
            sage: g.is_reduced()                                                        # needs sage.libs.pari
            True

            sage: q = BinaryQF(1, 0, -1)
            sage: q.reduced_form()                                                      # needs sage.libs.pari
            x^2 + 2*x*y

            sage: BinaryQF(1, 9, 4).reduced_form(transformation=True)                   # needs sage.libs.pari
            (
                                 [ 0 -1]
            4*x^2 + 7*x*y - y^2, [ 1  2]
            )
            sage: BinaryQF(3, 7, -2).reduced_form(transformation=True)                  # needs sage.libs.pari
            (
                                   [1 0]
            3*x^2 + 7*x*y - 2*y^2, [0 1]
            )
            sage: BinaryQF(-6, 6, -1).reduced_form(transformation=True)                 # needs sage.libs.pari
            (
                                  [ 0 -1]
            -x^2 + 2*x*y + 2*y^2, [ 1 -4]
            )

        TESTS:

        Check for :issue:`34229`::

            sage: BinaryQF([1,2,3]).reduced_form(transformation=True)                   # needs sage.libs.pari
            (
                         [ 1 -1]
            x^2 + 2*y^2, [ 0  1]
            )
            sage: BinaryQF([-225, -743, -743]).reduced_form().is_reduced()              # needs sage.libs.pari
            True

        Some randomized testing::

            sage: while True:
            ....:     f = BinaryQF([randrange(-10^3, 10^3) for _ in 'abc'])
            ....:     if not f.discriminant().is_square():
            ....:         break
            sage: algos = ['default']
            sage: assert pari; algos.append('pari')                                     # needs sage.libs.pari
            sage: if f.discriminant() > 0:
            ....:     algos.append('sage')
            sage: a = choice(algos)
            sage: g = f.reduced_form(algorithm=a)
            sage: g.is_reduced()
            True
            sage: g.is_equivalent(f)
            True
            sage: g,M = f.reduced_form(transformation=True, algorithm=a)
            sage: g.is_reduced()
            True
            sage: g.is_equivalent(f)
            True
            sage: f * M == g
            True
        """
    def cycle(self, proper: bool = False):
        """
        Return the cycle of reduced forms to which ``self`` belongs.

        This is based on Algorithm 6.1 of [BUVO2007]_.

        INPUT:

        - ``self`` -- reduced, indefinite form of non-square discriminant

        - ``proper`` -- boolean (default: ``False``); if ``True``, return the
          proper cycle

        The proper cycle of a form `f` consists of all reduced forms that are
        properly equivalent to `f`. This is useful when testing for proper
        equivalence (or equivalence) between indefinite forms.

        The cycle of `f` is a technical tool that is used when computing the proper
        cycle. Our definition of the cycle is slightly different from the one
        in [BUVO2007]_. In our definition, the cycle consists of all reduced
        forms `g`, such that the `a`-coefficient of `g` has the same sign as the
        `a`-coefficient of `f`, and `g` can be obtained from `f` by performing a
        change of variables, and then multiplying by the determinant of the
        change-of-variables matrix. It is important to note that `g` might not be
        equivalent to `f` (because of multiplying by the determinant).  However,
        either `g` or `-g` must be equivalent to `f`. Also note that the cycle
        does contain `f`. (Under the definition in [BUVO2007]_, the cycle might
        not contain `f`, because all forms in the cycle are required to have
        positive `a`-coefficient, even if the `a`-coefficient of `f` is negative.)

        EXAMPLES::

            sage: Q = BinaryQF(14, 17, -2)
            sage: Q.cycle()
            [14*x^2 + 17*x*y - 2*y^2,
             2*x^2 + 19*x*y - 5*y^2,
             5*x^2 + 11*x*y - 14*y^2]
            sage: Q.cycle(proper=True)
            [14*x^2 + 17*x*y - 2*y^2,
             -2*x^2 + 19*x*y + 5*y^2,
             5*x^2 + 11*x*y - 14*y^2,
             -14*x^2 + 17*x*y + 2*y^2,
             2*x^2 + 19*x*y - 5*y^2,
             -5*x^2 + 11*x*y + 14*y^2]

            sage: Q = BinaryQF(1, 8, -3)
            sage: Q.cycle()
            [x^2 + 8*x*y - 3*y^2,
             3*x^2 + 4*x*y - 5*y^2,
             5*x^2 + 6*x*y - 2*y^2,
             2*x^2 + 6*x*y - 5*y^2,
             5*x^2 + 4*x*y - 3*y^2,
             3*x^2 + 8*x*y - y^2]
            sage: Q.cycle(proper=True)
            [x^2 + 8*x*y - 3*y^2,
             -3*x^2 + 4*x*y + 5*y^2,
              5*x^2 + 6*x*y - 2*y^2,
              -2*x^2 + 6*x*y + 5*y^2,
              5*x^2 + 4*x*y - 3*y^2,
              -3*x^2 + 8*x*y + y^2]

            sage: Q = BinaryQF(1, 7, -6)
            sage: Q.cycle()
            [x^2 + 7*x*y - 6*y^2,
             6*x^2 + 5*x*y - 2*y^2,
             2*x^2 + 7*x*y - 3*y^2,
             3*x^2 + 5*x*y - 4*y^2,
             4*x^2 + 3*x*y - 4*y^2,
             4*x^2 + 5*x*y - 3*y^2,
             3*x^2 + 7*x*y - 2*y^2,
             2*x^2 + 5*x*y - 6*y^2,
             6*x^2 + 7*x*y - y^2]

        TESTS:

        Check an example in :issue:`28989`::

            sage: Q = BinaryQF(1, 1, -1)
            sage: Q.cycle(proper=True)
            [x^2 + x*y - y^2, -x^2 + x*y + y^2]

        This is Example 6.10.6 of [BUVO2007]_::

            sage: Q = BinaryQF(1, 7, -6)
            sage: Q.cycle()
            [x^2 + 7*x*y - 6*y^2,
             6*x^2 + 5*x*y - 2*y^2,
             2*x^2 + 7*x*y - 3*y^2,
             3*x^2 + 5*x*y - 4*y^2,
             4*x^2 + 3*x*y - 4*y^2,
             4*x^2 + 5*x*y - 3*y^2,
             3*x^2 + 7*x*y - 2*y^2,
             2*x^2 + 5*x*y - 6*y^2,
             6*x^2 + 7*x*y - y^2]
            sage: Q.cycle(proper=True)
            [x^2 + 7*x*y - 6*y^2,
             -6*x^2 + 5*x*y + 2*y^2,
             2*x^2 + 7*x*y - 3*y^2,
             -3*x^2 + 5*x*y + 4*y^2,
             4*x^2 + 3*x*y - 4*y^2,
             -4*x^2 + 5*x*y + 3*y^2,
             3*x^2 + 7*x*y - 2*y^2,
             -2*x^2 + 5*x*y + 6*y^2,
             6*x^2 + 7*x*y - y^2,
             -x^2 + 7*x*y + 6*y^2,
             6*x^2 + 5*x*y - 2*y^2,
             -2*x^2 + 7*x*y + 3*y^2,
             3*x^2 + 5*x*y - 4*y^2,
             -4*x^2 + 3*x*y + 4*y^2,
             4*x^2 + 5*x*y - 3*y^2,
             -3*x^2 + 7*x*y + 2*y^2,
             2*x^2 + 5*x*y - 6*y^2,
             -6*x^2 + 7*x*y + y^2]

        This is Example 6.10.7 of [BUVO2007]_::

            sage: Q = BinaryQF(1, 8, -3)
            sage: Q.cycle()
            [x^2 + 8*x*y - 3*y^2,
             3*x^2 + 4*x*y - 5*y^2,
             5*x^2 + 6*x*y - 2*y^2,
             2*x^2 + 6*x*y - 5*y^2,
             5*x^2 + 4*x*y - 3*y^2,
             3*x^2 + 8*x*y - y^2]
            sage: Q.cycle(proper=True)
            [x^2 + 8*x*y - 3*y^2,
             -3*x^2 + 4*x*y + 5*y^2,
             5*x^2 + 6*x*y - 2*y^2,
             -2*x^2 + 6*x*y + 5*y^2,
             5*x^2 + 4*x*y - 3*y^2,
             -3*x^2 + 8*x*y + y^2]
            sage: Q.cycle(proper=True) # should be the same as the previous one
            [x^2 + 8*x*y - 3*y^2,
             -3*x^2 + 4*x*y + 5*y^2,
             5*x^2 + 6*x*y - 2*y^2,
             -2*x^2 + 6*x*y + 5*y^2,
             5*x^2 + 4*x*y - 3*y^2,
             -3*x^2 + 8*x*y + y^2]

        Try an example where a is negative::

            sage: Q = BinaryQF(-1, 8, 3)
            sage: Q.cycle(proper=True)
            [-x^2 + 8*x*y + 3*y^2,
             3*x^2 + 4*x*y - 5*y^2,
             -5*x^2 + 6*x*y + 2*y^2,
             2*x^2 + 6*x*y - 5*y^2,
             -5*x^2 + 4*x*y + 3*y^2,
             3*x^2 + 8*x*y - y^2]
        """
    def is_positive_definite(self) -> bool:
        """
        Return ``True`` if ``self`` is positive definite, i.e., has
        negative discriminant with `a > 0`.

        EXAMPLES::

            sage: Q = BinaryQF(195751, 37615, 1807)
            sage: Q.is_positive_definite()
            True
            sage: Q = BinaryQF(195751, 1212121, -1876411)
            sage: Q.is_positive_definite()
            False
        """
    is_posdef = is_positive_definite
    def is_negative_definite(self) -> bool:
        """
        Return ``True`` if ``self`` is negative definite, i.e., has
        negative discriminant with `a < 0`.

        EXAMPLES::

            sage: Q = BinaryQF(-1, 3, -5)
            sage: Q.is_positive_definite()
            False
            sage: Q.is_negative_definite()
            True
        """
    is_negdef = is_negative_definite
    def is_indefinite(self) -> bool:
        """
        Return whether ``self`` is indefinite, i.e., has positive discriminant.

        EXAMPLES::

            sage: Q = BinaryQF(1, 3, -5)
            sage: Q.is_indef()
            True
        """
    is_indef = is_indefinite
    def is_singular(self) -> bool:
        """
        Return whether ``self`` is singular, i.e., has zero discriminant.

        EXAMPLES::

            sage: Q = BinaryQF(1, 3, -5)
            sage: Q.is_singular()
            False
            sage: Q = BinaryQF(1, 2, 1)
            sage: Q.is_singular()
            True
        """
    def is_nonsingular(self) -> bool:
        """
        Return whether this form is nonsingular, i.e., has nonzero discriminant.

        EXAMPLES::

            sage: Q = BinaryQF(1, 3, -5)
            sage: Q.is_nonsingular()
            True
            sage: Q = BinaryQF(1, 2, 1)
            sage: Q.is_nonsingular()
            False
        """
    def is_equivalent(self, other, proper: bool = True) -> bool:
        """
        Return whether ``self`` is equivalent to ``other``.

        INPUT:

        - ``proper`` -- boolean (default: ``True``); if ``True`` use proper
          equivalence
        - ``other`` -- a binary quadratic form

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: Q3 = BinaryQF(4, 4, 15)
            sage: Q2 = BinaryQF(4, -4, 15)
            sage: Q2.is_equivalent(Q3)
            True
            sage: a = BinaryQF([33, 11, 5])
            sage: b = a.reduced_form(); b
            5*x^2 - x*y + 27*y^2
            sage: a.is_equivalent(b)
            True
            sage: a.is_equivalent(BinaryQF((3, 4, 5)))
            False

        Some indefinite examples::

            sage: Q1 = BinaryQF(9, 8, -7)
            sage: Q2 = BinaryQF(9, -8, -7)
            sage: Q1.is_equivalent(Q2, proper=True)                                     # needs sage.libs.pari
            False
            sage: Q1.is_equivalent(Q2, proper=False)                                    # needs sage.libs.pari
            True

        TESTS:

        We check that :issue:`25888` is fixed::

            sage: # needs sage.libs.pari
            sage: Q1 = BinaryQF(3, 4, -2)
            sage: Q2 = BinaryQF(-2, 4, 3)
            sage: Q1.is_equivalent(Q2) == Q2.is_equivalent(Q1)
            True
            sage: Q1.is_equivalent(Q2, proper=False) == Q2.is_equivalent(Q1, proper=False)
            True
            sage: Q1.is_equivalent(Q2, proper=True)
            True

        We check that the first part of :issue:`29028` is fixed::

            sage: Q = BinaryQF(0, 2, 0)
            sage: Q.discriminant()
            4
            sage: Q.is_equivalent(Q, proper=True)                                       # needs sage.libs.pari
            True
            sage: Q.is_equivalent(Q, proper=False)                                      # needs sage.libs.pari
            True

        A test for rational forms::

            sage: Q1 = BinaryQF(0, 4, 2)
            sage: Q2 = BinaryQF(2, 4, 0)
            sage: Q1.is_equivalent(Q2, proper=False)                                    # needs sage.libs.pari
            True

        Test another part of :issue:`28989`::

            sage: Q1, Q2 = BinaryQF(1, 1, -1), BinaryQF(-1, 1, 1)
            sage: Q1.is_equivalent(Q2, proper=True)                                     # needs sage.libs.pari
            True
        """
    @cached_method
    def is_reduced(self) -> bool:
        """
        Return whether ``self`` is reduced.

        Let `f = a x^2 + b xy + c y^2` be a binary quadratic form of
        discriminant `D`.

        - If `f` is positive definite (`D < 0` and `a > 0`), then `f`
          is reduced if and only if `|b|\\leq a \\leq c`, and `b\\geq 0`
          if either `a = b` or `a = c`.

        - If `f` is negative definite (`D < 0` and `a < 0`), then `f`
          is reduced if and only if the positive definite form with
          coefficients `(-a, b, -c)` is reduced.

        - If `f` is indefinite (`D > 0`), then `f` is reduced if and
          only if [`b > 0`, `ac < 0` and `(a-c)^2 < D`]
          (equivalently if `|\\sqrt{D} - 2|a|| < b < \\sqrt{D}`)
          or [`a = 0` and `-b < 2c \\leq b`]
          or [`c = 0` and `-b < 2a \\leq b`].

        EXAMPLES::

            sage: Q = BinaryQF([1, 2, 3])
            sage: Q.is_reduced()
            False

            sage: Q = BinaryQF([2, 1, 3])
            sage: Q.is_reduced()
            True

            sage: Q = BinaryQF([1, -1, 1])
            sage: Q.is_reduced()
            False

            sage: Q = BinaryQF([1, 1, 1])
            sage: Q.is_reduced()
            True

        Examples using indefinite forms::

            sage: f = BinaryQF(-1, 2, 2)
            sage: f.is_reduced()
            True
            sage: BinaryQF(1, 9, 4).is_reduced()
            False
            sage: BinaryQF(1, 5, -1).is_reduced()
            True

        TESTS:

        We check that :issue:`37635` is fixed::

            sage: list = range(0xa19ae44106b09bfffffffffff0, 0xa19ae44106b09c000000000010)
            sage: all(BinaryQF([1, 0, -x]).reduced_form().is_reduced() for x in list)
            True
        """
    def complex_point(self):
        """
        Return the point in the complex upper half-plane associated to ``self``.

        This form, `ax^2 + b xy + cy^2`, must be definite with
        negative discriminant `b^2 - 4 a c < 0`.

        OUTPUT:

        - the unique complex root of `a x^2 + b x + c` with positive
          imaginary part

        EXAMPLES::

            sage: Q = BinaryQF([1, 0, 1])
            sage: Q.complex_point()                                                     # needs sage.libs.pari
            1.00000000000000*I
        """
    def matrix_action_left(self, M):
        """
        Return the binary quadratic form resulting from the left action
        of the 2-by-2 matrix `M` on ``self``.

        Here the action of the matrix `M = \\begin{pmatrix} a & b \\\\ c & d
        \\end{pmatrix}` on the form `Q(x, y)` produces the form `Q(ax+cy,
        bx+dy)`.

        EXAMPLES::

            sage: Q = BinaryQF([2, 1, 3]); Q
            2*x^2 + x*y + 3*y^2
            sage: M = matrix(ZZ, [[1, 2], [3, 5]])
            sage: Q.matrix_action_left(M)
            16*x^2 + 83*x*y + 108*y^2
        """
    def matrix_action_right(self, M):
        """
        Return the binary quadratic form resulting from the right action
        of the 2-by-2 matrix `M` on ``self``.

        Here the action of the matrix `M = \\begin{pmatrix} a & b \\\\ c & d
        \\end{pmatrix}` on the form `Q(x, y)` produces the form `Q(ax+by,
        cx+dy)`.

        EXAMPLES::

            sage: Q = BinaryQF([2, 1, 3]); Q
            2*x^2 + x*y + 3*y^2
            sage: M = matrix(ZZ, [[1, 2], [3, 5]])
            sage: Q.matrix_action_right(M)
            32*x^2 + 109*x*y + 93*y^2
        """
    def small_prime_value(self, Bmax: int = 1000):
        """
        Return a prime represented by this (primitive positive definite) binary form.

        INPUT:

        - ``Bmax`` -- a positive bound on the representing integers

        OUTPUT: a prime number represented by the form

        .. NOTE::

            This is a very elementary implementation which just substitutes
            values until a prime is found.

        EXAMPLES::

            sage: [Q.small_prime_value()                                                # needs sage.libs.pari
            ....:  for Q in BinaryQF_reduced_representatives(-23, primitive_only=True)]
            [23, 2, 2]
            sage: [Q.small_prime_value()                                                # needs sage.libs.pari
            ....:  for Q in BinaryQF_reduced_representatives(-47, primitive_only=True)]
            [47, 2, 2, 3, 3]
        """
    def solve_integer(self, n, *, algorithm: str = 'general', _flag: int = 2):
        '''
        Solve `Q(x, y) = n` in integers `x` and `y` where `Q` is this
        quadratic form.

        INPUT:

        - ``n`` -- positive integer or a
          `:sage:`~sage.structure.factorization.Factorization` object

        - ``algorithm`` -- ``\'general\'`` (default) or ``\'cornacchia\'``

        - ``_flag`` -- ``1``, ``2`` (default) or ``3``; passed onto the pari
          function``qfbsolve``. For internal use only.

        To use the Cornacchia algorithm, the quadratic form must have
        `a=1` and `b=0` and `c>0`, and ``n`` must be a prime or four
        times a prime (but this is not checked).

        OUTPUT:

        A tuple `(x, y)` of integers satisfying `Q(x, y) = n`, or ``None``
        if no solution exists.

        ALGORITHM: :pari:`qfbsolve` or :pari:`qfbcornacchia`

        TODO:: Replace ``_flag`` with human-readable parameters c.f. :issue:`37119`

        EXAMPLES::

            sage: Q = BinaryQF([1, 0, 419])
            sage: Q.solve_integer(773187972)                                            # needs sage.libs.pari
            (4919, 1337)

        If `Q` is of the form `[1,0,c]` as above and `n` is a prime
        (or four times a prime whenever `c \\equiv 3 \\pmod 4`), then
        Cornacchia\'s algorithm can be used, which is typically much
        faster than the general method::

            sage: Q = BinaryQF([1, 0, 12345])
            sage: n = 2^99 + 5273
            sage: Q.solve_integer(n)                                                    # needs sage.libs.pari
            (67446480057659, 7139620553488)
            sage: Q.solve_integer(n, algorithm=\'cornacchia\')                            # needs sage.libs.pari
            (67446480057659, 7139620553488)
            sage: timeit(\'Q.solve_integer(n)\')                          # not tested
            125 loops, best of 3: 3.13 ms per loop
            sage: timeit(\'Q.solve_integer(n, algorithm="cornacchia")\')  # not tested
            625 loops, best of 3: 18.6 μs per loop

        ::

            sage: # needs sage.libs.pari
            sage: Qs = BinaryQF_reduced_representatives(-23, primitive_only=True)
            sage: Qs
            [x^2 + x*y + 6*y^2, 2*x^2 - x*y + 3*y^2, 2*x^2 + x*y + 3*y^2]
            sage: [Q.solve_integer(3) for Q in Qs]
            [None, (0, 1), (0, 1)]
            sage: [Q.solve_integer(5) for Q in Qs]
            [None, None, None]
            sage: [Q.solve_integer(6) for Q in Qs]
            [(1, -1), (1, -1), (-1, -1)]

        ::

            sage: # needs sage.libs.pari
            sage: n = factor(126)
            sage: Q = BinaryQF([1, 0, 5])
            sage: Q.solve_integer(n)
            (11, -1)

        TESTS:

        The returned solutions are correct (random inputs)::

            sage: Q = BinaryQF([randrange(-10^3, 10^3) for _ in \'abc\'])
            sage: n = randrange(-10^9, 10^9)
            sage: xy = Q.solve_integer(n)                                               # needs sage.libs.pari
            sage: xy is None or Q(*xy) == n                                             # needs sage.libs.pari
            True

        Also when using the ``\'cornacchia\'`` algorithm::

            sage: # needs sage.libs.pari
            sage: n = random_prime(10^9)
            sage: c = randrange(1, 10^3)

            sage: # needs sage.libs.pari
            sage: Q1 = BinaryQF(1, 0, c)
            sage: xy = Q1.solve_integer(n, algorithm=\'cornacchia\')
            sage: xy is None or Q1(*xy) == n
            True
            sage: (xy is None) == (Q1.solve_integer(n) is None)
            True

            sage: # needs sage.libs.pari
            sage: Q3 = BinaryQF(1, 0, 4*c+3)
            sage: xy = Q3.solve_integer(n, algorithm=\'cornacchia\')
            sage: xy is None or Q3(*xy) == n
            True
            sage: (xy is None) == (Q3.solve_integer(n) is None)
            True

            sage: # needs sage.libs.pari
            sage: xy = Q3.solve_integer(4*n, algorithm=\'cornacchia\')
            sage: xy is None or Q3(*xy) == 4*n
            True
            sage: (xy is None) == (Q3.solve_integer(4*n) is None)
            True

        Test for square discriminants specifically (:issue:`33026`)::

            sage: n = randrange(-10^3, 10^3)
            sage: Q = BinaryQF([n, randrange(-10^3, 10^3), 0][::(-1)**randrange(2)])
            sage: U = random_matrix(ZZ, 2, 2, \'unimodular\')
            sage: U.rescale_row(0, choice((+1,-1)))
            sage: assert U.det() in (+1,-1)
            sage: Q = Q.matrix_action_right(U)
            sage: Q.discriminant().is_square()
            True
            sage: # needs sage.libs.pari
            sage: xy = Q.solve_integer(n)
            sage: Q(*xy) == n
            True

        Also test the `n=0` special case separately::

            sage: # needs sage.libs.pari
            sage: xy = Q.solve_integer(0)
            sage: Q(*xy)
            0

        Test for different ``_flag`` values::

            sage: # needs sage.libs.pari
            sage: Q = BinaryQF([1, 0, 5])
            sage: Q.solve_integer(126, _flag=1)
            [(-11, -1), (-1, -5), (-1, 5), (11, -1)]
            sage: Q.solve_integer(126, _flag=2)
            (11, -1)
            sage: Q.solve_integer(126, _flag=3)
            [(-11, -1), (-9, -3), (-1, -5), (-1, 5), (9, -3), (11, -1)]
        '''
    def form_class(self):
        """
        Return the class of this form modulo equivalence.

        EXAMPLES::

            sage: F = BinaryQF([3, -16, 161])
            sage: cl = F.form_class(); cl
            Class of 3*x^2 + 2*x*y + 140*y^2
            sage: cl.parent()
            Form Class Group of Discriminant -1676
            sage: cl.parent() is BQFClassGroup(-4*419)
            True
        """

def BinaryQF_reduced_representatives(D, primitive_only: bool = False, proper: bool = True):
    """
    Return representatives for the classes of binary quadratic forms
    of discriminant `D`.

    INPUT:

    - ``D`` -- integer; a discriminant

    - ``primitive_only`` -- boolean (default: ``True``); if ``True``, only
      return primitive forms

    - ``proper`` -- boolean (default: ``True``)

    OUTPUT:

    (list) A lexicographically-ordered list of inequivalent reduced
    representatives for the (im)proper equivalence classes of binary quadratic
    forms of discriminant `D`.  If ``primitive_only`` is ``True`` then
    imprimitive forms (which only exist when `D` is not fundamental) are
    omitted; otherwise they are included.

    EXAMPLES::

        sage: BinaryQF_reduced_representatives(-4)
        [x^2 + y^2]

        sage: BinaryQF_reduced_representatives(-163)
        [x^2 + x*y + 41*y^2]

        sage: BinaryQF_reduced_representatives(-12)
        [x^2 + 3*y^2, 2*x^2 + 2*x*y + 2*y^2]

        sage: BinaryQF_reduced_representatives(-16)
        [x^2 + 4*y^2, 2*x^2 + 2*y^2]

        sage: BinaryQF_reduced_representatives(-63)
        [x^2 + x*y + 16*y^2, 2*x^2 - x*y + 8*y^2, 2*x^2 + x*y + 8*y^2,
         3*x^2 + 3*x*y + 6*y^2, 4*x^2 + x*y + 4*y^2]

    The number of inequivalent reduced binary forms with a fixed negative
    fundamental discriminant `D` is the class number of the quadratic field
    `\\QQ(\\sqrt{D})`::

        sage: len(BinaryQF_reduced_representatives(-13*4))
        2
        sage: QuadraticField(-13*4, 'a').class_number()                                 # needs sage.rings.number_field
        2

        sage: # needs sage.libs.pari
        sage: p = next_prime(2^20); p
        1048583
        sage: len(BinaryQF_reduced_representatives(-p))
        689
        sage: QuadraticField(-p, 'a').class_number()                                    # needs sage.rings.number_field
        689
        sage: BinaryQF_reduced_representatives(-23*9)
        [x^2 + x*y + 52*y^2,
        2*x^2 - x*y + 26*y^2,
        2*x^2 + x*y + 26*y^2,
        3*x^2 + 3*x*y + 18*y^2,
        4*x^2 - x*y + 13*y^2,
        4*x^2 + x*y + 13*y^2,
        6*x^2 - 3*x*y + 9*y^2,
        6*x^2 + 3*x*y + 9*y^2,
        8*x^2 + 7*x*y + 8*y^2]
        sage: BinaryQF_reduced_representatives(-23*9, primitive_only=True)
        [x^2 + x*y + 52*y^2,
        2*x^2 - x*y + 26*y^2,
        2*x^2 + x*y + 26*y^2,
        4*x^2 - x*y + 13*y^2,
        4*x^2 + x*y + 13*y^2,
        8*x^2 + 7*x*y + 8*y^2]

    TESTS::

        sage: BinaryQF_reduced_representatives(73)
        [4*x^2 + 3*x*y - 4*y^2]
        sage: BinaryQF_reduced_representatives(76, primitive_only=True)                 # needs sage.libs.pari
        [-3*x^2 + 4*x*y + 5*y^2,
         3*x^2 + 4*x*y - 5*y^2]
        sage: BinaryQF_reduced_representatives(136)
        [-5*x^2 + 4*x*y + 6*y^2,
         -2*x^2 + 8*x*y + 9*y^2,
         2*x^2 + 8*x*y - 9*y^2,
         5*x^2 + 4*x*y - 6*y^2]
        sage: BinaryQF_reduced_representatives(136, proper=False)
        [-2*x^2 + 8*x*y + 9*y^2, 2*x^2 + 8*x*y - 9*y^2, 5*x^2 + 4*x*y - 6*y^2]

    Check that the primitive_only keyword does something::

        sage: BinaryQF_reduced_representatives(148, proper=False, primitive_only=False)
        [x^2 + 12*x*y - y^2, 4*x^2 + 6*x*y - 7*y^2, 6*x^2 + 2*x*y - 6*y^2]
        sage: BinaryQF_reduced_representatives(148, proper=False, primitive_only=True)  # needs sage.libs.pari
        [x^2 + 12*x*y - y^2, 4*x^2 + 6*x*y - 7*y^2]
        sage: BinaryQF_reduced_representatives(148, proper=True, primitive_only=True)   # needs sage.libs.pari
        [-7*x^2 + 6*x*y + 4*y^2, x^2 + 12*x*y - y^2, 4*x^2 + 6*x*y - 7*y^2]
        sage: BinaryQF_reduced_representatives(148, proper=True, primitive_only=False)
        [-7*x^2 + 6*x*y + 4*y^2,
         x^2 + 12*x*y - y^2,
         4*x^2 + 6*x*y - 7*y^2,
         6*x^2 + 2*x*y - 6*y^2]

    Test another part of :issue:`29028`::

        sage: BinaryQF_reduced_representatives(10^2, proper=False, primitive_only=False)
        [-4*x^2 + 10*x*y,
         -3*x^2 + 10*x*y,
         -2*x^2 + 10*x*y,
         -x^2 + 10*x*y,
         10*x*y,
         x^2 + 10*x*y,
         2*x^2 + 10*x*y,
         5*x^2 + 10*x*y]
        sage: BinaryQF_reduced_representatives(10^2, proper=False, primitive_only=True)             # needs sage.libs.pari
        [-3*x^2 + 10*x*y, -x^2 + 10*x*y, x^2 + 10*x*y]
        sage: BinaryQF_reduced_representatives(10^2, proper=True, primitive_only=True)  # needs sage.libs.pari
        [-3*x^2 + 10*x*y, -x^2 + 10*x*y, x^2 + 10*x*y, 3*x^2 + 10*x*y]
        sage: BinaryQF_reduced_representatives(10^2, proper=True, primitive_only=False)
        [-4*x^2 + 10*x*y,
         -3*x^2 + 10*x*y,
         -2*x^2 + 10*x*y,
         -x^2 + 10*x*y,
         10*x*y,
         x^2 + 10*x*y,
         2*x^2 + 10*x*y,
         3*x^2 + 10*x*y,
         4*x^2 + 10*x*y,
         5*x^2 + 10*x*y]
    """
