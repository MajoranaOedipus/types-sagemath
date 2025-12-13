from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

def transvectant(f, g, h: int = 1, scale: str = 'default'):
    """
    Return the h-th transvectant of f and g.

    INPUT:

    - ``f``, ``g`` -- two homogeneous binary forms in the same polynomial ring

    - ``h`` -- the order of the transvectant; if it is not specified,
      the first transvectant is returned

    - ``scale`` -- the scaling factor applied to the result. Possible values
      are ``'default'`` and ``'none'``. The ``'default'`` scaling factor is
      the one that appears in the output statement below, if the scaling
      factor is ``'none'`` the quotient of factorials is left out.

    OUTPUT:

    The h-th transvectant of the listed forms `f` and `g`:

    .. MATH::

        (f,g)_h = \\frac{(d_f-h)! \\cdot (d_g-h)!}{d_f! \\cdot d_g!}\\left(
                  \\left(\\frac{\\partial}{\\partial x}\\frac{\\partial}{\\partial z'}
                  - \\frac{\\partial}{\\partial x'}\\frac{\\partial}{\\partial z}
                  \\right)^h \\left(f(x,z) \\cdot g(x',z')\\right)
                  \\right)_{(x',z')=(x,z)}

    EXAMPLES::

        sage: from sage.rings.invariants.invariant_theory import AlgebraicForm, transvectant
        sage: R.<x,y> = QQ[]
        sage: f = AlgebraicForm(2, 5, x^5 + 5*x^4*y + 5*x*y^4 + y^5)
        sage: transvectant(f, f, 4)
        Binary quadratic given by 2*x^2 - 4*x*y + 2*y^2
        sage: transvectant(f, f, 8)
        Binary form of degree -6 given by 0

    The default scaling will yield an error for fields of positive
    characteristic below `d_f!` or `d_g!` as the denominator of the scaling
    factor will not be invertible in that case. The scale argument ``'none'``
    can be used to compute the transvectant in this case::

        sage: # needs sage.rings.finite_rings
        sage: R.<a0,a1,a2,a3,a4,a5,x0,x1> = GF(5)[]
        sage: f = AlgebraicForm(2, 5, a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2
        ....:                         + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5, x0, x1)
        sage: transvectant(f, f, 4)
        Traceback (most recent call last):
        ...
        ZeroDivisionError
        sage: transvectant(f, f, 4, scale='none')
        Binary quadratic given by -a3^2*x0^2 + a2*a4*x0^2 + a2*a3*x0*x1
        - a1*a4*x0*x1 - a2^2*x1^2 + a1*a3*x1^2

    The additional factors that appear when ``scale='none'`` is used can be
    seen if we consider the same transvectant over the rationals and compare
    it to the scaled version::

        sage: R.<a0,a1,a2,a3,a4,a5,x0,x1> = QQ[]
        sage: f = AlgebraicForm(2, 5, a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2
        ....:                         + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5, x0, x1)
        sage: transvectant(f, f, 4)
        Binary quadratic given by 3/50*a3^2*x0^2 - 4/25*a2*a4*x0^2
        + 2/5*a1*a5*x0^2 + 1/25*a2*a3*x0*x1 - 6/25*a1*a4*x0*x1 + 2*a0*a5*x0*x1
        + 3/50*a2^2*x1^2 - 4/25*a1*a3*x1^2 + 2/5*a0*a4*x1^2
        sage: transvectant(f, f, 4, scale='none')
        Binary quadratic given by 864*a3^2*x0^2 - 2304*a2*a4*x0^2
        + 5760*a1*a5*x0^2 + 576*a2*a3*x0*x1 - 3456*a1*a4*x0*x1
        + 28800*a0*a5*x0*x1 + 864*a2^2*x1^2 - 2304*a1*a3*x1^2 + 5760*a0*a4*x1^2

    If the forms are given as inhomogeneous polynomials, the homogenisation
    might fail if the polynomial ring has multiple variables. You can
    circumvent this by making sure the base ring of the polynomial has only
    one variable::

        sage: R.<x,y> = QQ[]
        sage: quintic = invariant_theory.binary_quintic(x^5 + x^3 + 2*x^2 + y^5, x)
        sage: transvectant(quintic, quintic, 2)
        Traceback (most recent call last):
        ...
        ValueError: polynomial is not homogeneous
        sage: R.<y> = QQ[]
        sage: S.<x> = R[]
        sage: quintic = invariant_theory.binary_quintic(x^5 + x^3 + 2*x^2 + y^5, x)
        sage: transvectant(quintic, quintic, 2)
        Binary sextic given by 1/5*x^6 + 6/5*x^5*h - 3/25*x^4*h^2
        + (50*y^5 - 8)/25*x^3*h^3 - 12/25*x^2*h^4 + (3*y^5)/5*x*h^5
        + (2*y^5)/5*h^6
    """

class FormsBase(SageObject):
    """
    The common base class of :class:`AlgebraicForm` and
    :class:`SeveralAlgebraicForms`.

    This is an abstract base class to provide common methods. It does
    not make much sense to instantiate it.

    TESTS::

        sage: from sage.rings.invariants.invariant_theory import FormsBase
        sage: FormsBase(None, None, None, None)
        <sage.rings.invariants.invariant_theory.FormsBase object at ...>
    """
    def __init__(self, n, homogeneous, ring, variables) -> None:
        """
        The Python constructor.

        TESTS::

            sage: from sage.rings.invariants.invariant_theory import FormsBase
            sage: FormsBase(None, None, None, None)
            <sage.rings.invariants.invariant_theory.FormsBase object at ...>
        """
    def ring(self):
        """
        Return the polynomial ring.

        OUTPUT:

        A polynomial ring. This is where the defining polynomial(s)
        live. Note that the polynomials may be homogeneous or
        inhomogeneous, depending on how the user constructed the
        object.

        EXAMPLES::

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4 + t*x^2*y^2, [x,y])
            sage: quartic.ring()
            Multivariate Polynomial Ring in x, y, t over Rational Field

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + 1 + t*x^2, [x])
            sage: quartic.ring()
            Multivariate Polynomial Ring in x, y, t over Rational Field
        """
    def variables(self):
        """
        Return the variables of the form.

        OUTPUT:

        A tuple of variables. If inhomogeneous notation is used for the
        defining polynomial then the last entry will be ``None``.

        EXAMPLES::

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4 + t*x^2*y^2, [x,y])
            sage: quartic.variables()
            (x, y)

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + 1 + t*x^2, [x])
            sage: quartic.variables()
            (x, None)
        """
    def is_homogeneous(self):
        """
        Return whether the forms were defined by homogeneous polynomials.

        OUTPUT: boolean; whether the user originally defined the form via
        homogeneous variables

        EXAMPLES::

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4 + t*x^2*y^2, [x,y])
            sage: quartic.is_homogeneous()
            True
            sage: quartic.form()
            x^2*y^2*t + x^4 + y^4

            sage: R.<x,y,t> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + 1 + t*x^2, [x])
            sage: quartic.is_homogeneous()
            False
            sage: quartic.form()
            x^4 + x^2*t + 1
        """

class AlgebraicForm(FormsBase):
    """
    The base class of algebraic forms (i.e. homogeneous polynomials).

    You should only instantiate the derived classes of this base
    class.

    Derived classes must implement ``coeffs()`` and
    ``scaled_coeffs()``

    INPUT:

    - ``n`` -- the number of variables

    - ``d`` -- the degree of the polynomial

    - ``polynomial`` -- the polynomial

    - ``*args`` -- the variables, as a single list/tuple, multiple
      arguments, or ``None`` to use all variables of the polynomial

    Derived classes must implement the same arguments for the
    constructor.

    EXAMPLES::

        sage: from sage.rings.invariants.invariant_theory import AlgebraicForm
        sage: R.<x,y> = QQ[]
        sage: p = x^2 + y^2
        sage: AlgebraicForm(2, 2, p).variables()
        (x, y)
        sage: AlgebraicForm(2, 2, p, None).variables()
        (x, y)
        sage: AlgebraicForm(3, 2, p).variables()
        (x, y, None)
        sage: AlgebraicForm(3, 2, p, None).variables()
        (x, y, None)

        sage: from sage.rings.invariants.invariant_theory import AlgebraicForm
        sage: R.<x,y,s,t> = QQ[]
        sage: p = s*x^2 + t*y^2
        sage: AlgebraicForm(2, 2, p, [x,y]).variables()
        (x, y)
        sage: AlgebraicForm(2, 2, p, x,y).variables()
        (x, y)

        sage: AlgebraicForm(3, 2, p, [x,y,None]).variables()
        (x, y, None)
        sage: AlgebraicForm(3, 2, p, x,y,None).variables()
        (x, y, None)

        sage: AlgebraicForm(2, 1, p, [x,y]).variables()
        Traceback (most recent call last):
        ...
        ValueError: polynomial is of the wrong degree

        sage: AlgebraicForm(2, 2, x^2 + y, [x,y]).variables()
        Traceback (most recent call last):
        ...
        ValueError: polynomial is not homogeneous
    """
    def __init__(self, n, d, polynomial, *args, **kwds) -> None:
        """
        The Python constructor.

        INPUT:

        See the class documentation.

        TESTS::

            sage: from sage.rings.invariants.invariant_theory import AlgebraicForm
            sage: R.<x,y> = QQ[]
            sage: form = AlgebraicForm(2, 2, x^2 + y^2)
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` with ``other``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4+y^4)
            sage: quartic == 'foo'
            False
            sage: quartic == quartic
            True
        """
    def form(self):
        """
        Return the defining polynomial.

        OUTPUT: the polynomial used to define the algebraic form

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4)
            sage: quartic.form()
            x^4 + y^4
            sage: quartic.polynomial()
            x^4 + y^4
        """
    polynomial = form
    def homogenized(self, var: str = 'h'):
        """
        Return form as defined by a homogeneous polynomial.

        INPUT:

        - ``var`` -- either a variable name, variable index or a
          variable (default: ``'h'``)

        OUTPUT:

        The same algebraic form, but defined by a homogeneous
        polynomial.

        EXAMPLES::

            sage: T.<t> = QQ[]
            sage: quadratic = invariant_theory.binary_quadratic(t^2 + 2*t + 3)
            sage: quadratic
            Binary quadratic with coefficients (1, 3, 2)
            sage: quadratic.homogenized()
            Binary quadratic with coefficients (1, 3, 2)
            sage: quadratic == quadratic.homogenized()
            True
            sage: quadratic.form()
            t^2 + 2*t + 3
            sage: quadratic.homogenized().form()
            t^2 + 2*t*h + 3*h^2

            sage: R.<x,y,z> = QQ[]
            sage: quadratic = invariant_theory.ternary_quadratic(x^2 + 1, [x,y])
            sage: quadratic.homogenized().form()
            x^2 + h^2

            sage: R.<x> = QQ[]
            sage: quintic = invariant_theory.binary_quintic(x^4 + 1, x)
            sage: quintic.homogenized().form()
            x^4*h + h^5
        """
    def coefficients(self):
        """
        Alias for ``coeffs()``.

        See the documentation for ``coeffs()`` for details.

        EXAMPLES::

            sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
            sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
            sage: q = invariant_theory.quadratic_form(p, x,y,z)
            sage: q.coefficients()
            (a, b, c, d, e, f)
            sage: q.coeffs()
            (a, b, c, d, e, f)
        """
    def transformed(self, g):
        """
        Return the image under a linear transformation of the variables.

        INPUT:

        - ``g`` -- a `GL(n,\\CC)` matrix or a dictionary with the
          variables as keys. A matrix is used to define the linear
          transformation of homogeneous variables, a dictionary acts
          by substitution of the variables.

        OUTPUT:

        A new instance of a subclass of :class:`AlgebraicForm`
        obtained by replacing the variables of the homogeneous
        polynomial by their image under ``g``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + 2*y^3 + 3*z^3 + 4*x*y*z)
            sage: cubic.transformed({x: y, y: z, z: x}).form()
            3*x^3 + y^3 + 4*x*y*z + 2*z^3
            sage: cyc = matrix([[0,1,0], [0,0,1], [1,0,0]])
            sage: cubic.transformed(cyc) == cubic.transformed({x:y, y:z, z:x})
            True
            sage: g = matrix(QQ, [[1, 0, 0], [-1, 1, -3], [-5, -5, 16]])
            sage: cubic.transformed(g)
            Ternary cubic with coefficients (-356, -373, 12234, -1119, 3578, -1151,
            3582, -11766, -11466, 7360)
            sage: cubic.transformed(g).transformed(g.inverse()) == cubic
            True
        """

class QuadraticForm(AlgebraicForm):
    """
    Invariant theory of a multivariate quadratic form.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See :meth:`~InvariantTheoryFactory.quadratic_form`
    for details.

    TESTS::

        sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
        sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
        sage: invariant_theory.quadratic_form(p, x,y,z)
        Ternary quadratic with coefficients (a, b, c, d, e, f)
        sage: type(_)
        <class 'sage.rings.invariants.invariant_theory.TernaryQuadratic'>

        sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
        sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
        sage: invariant_theory.quadratic_form(p, x,y,z)
        Ternary quadratic with coefficients (a, b, c, d, e, f)
        sage: type(_)
        <class 'sage.rings.invariants.invariant_theory.TernaryQuadratic'>

    Since we cannot always decide whether the form is homogeneous or
    not based on the number of variables, you need to explicitly
    specify it if you want the variables to be treated as
    inhomogeneous::

        sage: invariant_theory.inhomogeneous_quadratic_form(p.subs(z=1), x,y)
        Ternary quadratic with coefficients (a, b, c, d, e, f)
    """
    def __init__(self, n, d, polynomial, *args) -> None:
        """
        The Python constructor.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import QuadraticForm
            sage: form = QuadraticForm(2, 2, x^2 + 2*y^2 + 3*x*y)
            sage: form
            Binary quadratic with coefficients (1, 2, 3)
            sage: form._check_covariant('discriminant', invariant=True)
            sage: QuadraticForm(3, 2, x^2 + y^2)
            Ternary quadratic with coefficients (1, 1, 0, 0, 0, 0)
        """
    @classmethod
    def from_invariants(cls, discriminant, x, z, *args, **kwargs):
        """
        Construct a binary quadratic from its discriminant.

        This function constructs a binary quadratic whose discriminant equal
        the one provided as argument up to scaling.

        INPUT:

        - ``discriminant`` -- value of the discriminant used to reconstruct
          the binary quadratic

        OUTPUT: a QuadraticForm with 2 variables

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import QuadraticForm
            sage: QuadraticForm.from_invariants(1, x, y)
            Binary quadratic with coefficients (1, -1/4, 0)
        """
    @cached_method
    def monomials(self):
        """
        List the basis monomials in the form.

        OUTPUT:

        A tuple of monomials. They are in the same order as
        :meth:`coeffs`.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quadratic = invariant_theory.quadratic_form(x^2 + y^2)
            sage: quadratic.monomials()
            (x^2, y^2, x*y)

            sage: quadratic = invariant_theory.inhomogeneous_quadratic_form(x^2 + y^2)
            sage: quadratic.monomials()
            (x^2, y^2, 1, x*y, x, y)
        """
    @cached_method
    def coeffs(self):
        """
        The coefficients of a quadratic form.

        Given

        .. MATH::

            f(x) = \\sum_{0\\leq i<n} a_i x_i^2 + \\sum_{0\\leq j <k<n}
            a_{jk} x_j x_k

        this function returns `a = (a_0, \\dots, a_n, a_{00}, a_{01}, \\dots, a_{n-1,n})`

        EXAMPLES::

            sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
            sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
            sage: inv = invariant_theory.quadratic_form(p, x,y,z); inv
            Ternary quadratic with coefficients (a, b, c, d, e, f)
            sage: inv.coeffs()
            (a, b, c, d, e, f)
            sage: inv.scaled_coeffs()
            (a, b, c, 1/2*d, 1/2*e, 1/2*f)
        """
    def scaled_coeffs(self):
        """
        The scaled coefficients of a quadratic form.

        Given

        .. MATH::

            f(x) = \\sum_{0\\leq i<n} a_i x_i^2 + \\sum_{0\\leq j <k<n}
            2 a_{jk} x_j x_k

        this function returns `a = (a_0, \\cdots, a_n, a_{00}, a_{01}, \\dots, a_{n-1,n})`

        EXAMPLES::

            sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
            sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
            sage: inv = invariant_theory.quadratic_form(p, x,y,z); inv
            Ternary quadratic with coefficients (a, b, c, d, e, f)
            sage: inv.coeffs()
            (a, b, c, d, e, f)
            sage: inv.scaled_coeffs()
            (a, b, c, 1/2*d, 1/2*e, 1/2*f)
        """
    @cached_method
    def matrix(self):
        """
        Return the quadratic form as a symmetric matrix.

        OUTPUT:

        This method returns a symmetric matrix `A` such that the
        quadratic `Q` equals

        .. MATH::

            Q(x,y,z,\\dots) = (x,y,\\dots) A (x,y,\\dots)^t

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: quadratic = invariant_theory.ternary_quadratic(x^2+y^2+z^2+x*y)
            sage: matrix(quadratic)
            [  1 1/2   0]
            [1/2   1   0]
            [  0   0   1]
            sage: quadratic._matrix_() == matrix(quadratic)
            True
        """
    def discriminant(self):
        """
        Return the discriminant of the quadratic form.

        Up to an overall constant factor, this is just the determinant
        of the defining matrix, see :meth:`matrix`. For a quadratic
        form in `n` variables, the overall constant is `2^{n-1}` if
        `n` is odd and `(-1)^{n/2} 2^n` if `n` is even.

        EXAMPLES::

            sage: R.<a,b,c, x,y> = QQ[]
            sage: p = a*x^2 + b*x*y + c*y^2
            sage: quadratic = invariant_theory.quadratic_form(p, x,y)
            sage: quadratic.discriminant()
            b^2 - 4*a*c

            sage: R.<a,b,c,d,e,f,g, x,y,z> = QQ[]
            sage: p = a*x^2 + b*y^2 + c*z^2 + d*x*y + e*x*z + f*y*z
            sage: quadratic = invariant_theory.quadratic_form(p, x,y,z)
            sage: quadratic.discriminant()
            4*a*b*c - c*d^2 - b*e^2 + d*e*f - a*f^2
        """
    @cached_method
    def invariants(self, type: str = 'discriminant'):
        """
        Return a tuple of invariants of a binary quadratic.

        INPUT:

        - ``type`` -- the type of invariants to return; the default choice
          is to return the discriminant

        OUTPUT: the invariants of the binary quadratic

        EXAMPLES::

            sage: R.<x0, x1> = QQ[]
            sage: p = 2*x1^2 + 5*x0*x1 + 3*x0^2
            sage: quadratic = invariant_theory.binary_quadratic(p, x0, x1)
            sage: quadratic.invariants()
            (1,)
            sage: quadratic.invariants('unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown type of invariants unknown for a binary quadratic
        """
    @cached_method
    def dual(self):
        """
        Return the dual quadratic form.

        OUTPUT:

        A new quadratic form (with the same number of variables)
        defined by the adjoint matrix.

        EXAMPLES::

            sage: R.<a,b,c,x,y,z> = QQ[]
            sage: cubic = x^2+y^2+z^2
            sage: quadratic = invariant_theory.ternary_quadratic(a*x^2+b*y^2+c*z^2, [x,y,z])
            sage: quadratic.form()
            a*x^2 + b*y^2 + c*z^2
            sage: quadratic.dual().form()
            b*c*x^2 + a*c*y^2 + a*b*z^2

            sage: R.<x,y,z, t> = QQ[]
            sage: cubic = x^2+y^2+z^2
            sage: quadratic = invariant_theory.ternary_quadratic(x^2+y^2+z^2 + t*x*y, [x,y,z])
            sage: quadratic.dual()
            Ternary quadratic with coefficients (1, 1, -1/4*t^2 + 1, -t, 0, 0)

            sage: R.<x,y, t> = QQ[]
            sage: quadratic = invariant_theory.ternary_quadratic(x^2+y^2+1 + t*x*y, [x,y])
            sage: quadratic.dual()
            Ternary quadratic with coefficients (1, 1, -1/4*t^2 + 1, -t, 0, 0)

        TESTS::

            sage: R = PolynomialRing(QQ, 'a20,a11,a02,a10,a01,a00,x,y,z', order='lex')
            sage: R.inject_variables()
            Defining a20, a11, a02, a10, a01, a00, x, y, z
            sage: p = ( a20*x^2 + a11*x*y + a02*y^2 +
            ....:       a10*x*z + a01*y*z + a00*z^2 )
            sage: quadratic = invariant_theory.ternary_quadratic(p, x,y,z)
            sage: quadratic.dual().dual().form().factor()
            (1/4) *
            (a20*x^2 + a11*x*y + a02*y^2 + a10*x*z + a01*y*z + a00*z^2) *
            (4*a20*a02*a00 - a20*a01^2 - a11^2*a00 + a11*a10*a01 - a02*a10^2)

            sage: R.<w,x,y,z> = QQ[]
            sage: q = invariant_theory.quaternary_quadratic(w^2+2*x^2+3*y^2+4*z^2+x*y+5*w*z)
            sage: q.form()
            w^2 + 2*x^2 + x*y + 3*y^2 + 5*w*z + 4*z^2
            sage: q.dual().dual().form().factor()
            (42849/256) * (w^2 + 2*x^2 + x*y + 3*y^2 + 5*w*z + 4*z^2)

            sage: R.<x,y,z> = QQ[]
            sage: q = invariant_theory.quaternary_quadratic(1+2*x^2+3*y^2+4*z^2+x*y+5*z)
            sage: q.form()
            2*x^2 + x*y + 3*y^2 + 4*z^2 + 5*z + 1
            sage: q.dual().dual().form().factor()
            (42849/256) * (2*x^2 + x*y + 3*y^2 + 4*z^2 + 5*z + 1)
        """
    def as_QuadraticForm(self):
        """
        Convert into a :class:`~sage.quadratic_forms.quadratic_form.QuadraticForm`.

        OUTPUT:

        Sage has a special quadratic forms subsystem. This method
        converts ``self`` into this
        :class:`~sage.quadratic_forms.quadratic_form.QuadraticForm`
        representation.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: p = x^2 + y^2 + z^2 + 2*x*y + 3*x*z
            sage: quadratic = invariant_theory.ternary_quadratic(p)
            sage: matrix(quadratic)
            [  1   1 3/2]
            [  1   1   0]
            [3/2   0   1]
            sage: quadratic.as_QuadraticForm()
            Quadratic form in 3 variables over Multivariate Polynomial
            Ring in x, y, z over Rational Field with coefficients:
            [ 1 2 3 ]
            [ * 1 0 ]
            [ * * 1 ]
            sage: _.polynomial('X,Y,Z')
            X^2 + 2*X*Y + Y^2 + 3*X*Z + Z^2
        """

class BinaryQuartic(AlgebraicForm):
    """
    Invariant theory of a binary quartic.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See :meth:`~InvariantTheoryFactory.binary_quartic`
    for details.

    TESTS::

        sage: R.<a0, a1, a2, a3, a4, x0, x1> = QQ[]
        sage: p = a0*x1^4 + a1*x1^3*x0 + a2*x1^2*x0^2 + a3*x1*x0^3 + a4*x0^4
        sage: quartic = invariant_theory.binary_quartic(p, x0, x1)
        sage: quartic._check_covariant('form')
        sage: quartic._check_covariant('EisensteinD', invariant=True)
        sage: quartic._check_covariant('EisensteinE', invariant=True)
        sage: quartic._check_covariant('g_covariant')
        sage: quartic._check_covariant('h_covariant')
        sage: TestSuite(quartic).run()
    """
    def __init__(self, n, d, polynomial, *args) -> None:
        """
        The Python constructor.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import BinaryQuartic
            sage: BinaryQuartic(2, 4, x^4 + y^4)
            Binary quartic with coefficients (1, 0, 0, 0, 1)
        """
    @cached_method
    def monomials(self):
        """
        List the basis monomials in the form.

        OUTPUT:

        A tuple of monomials. They are in the same order as
        :meth:`coeffs`.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4)
            sage: quartic.monomials()
            (y^4, x*y^3, x^2*y^2, x^3*y, x^4)
        """
    @cached_method
    def coeffs(self):
        """
        The coefficients of a binary quartic.

        Given

        .. MATH::

            f(x) = a_0 x_1^4 + a_1 x_0 x_1^3 + a_2 x_0^2 x_1^2 +
                   a_3 x_0^3 x_1 + a_4 x_0^4

        this function returns `a = (a_0, a_1, a_2, a_3, a_4)`

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x0, x1> = QQ[]
            sage: p = a0*x1^4 + a1*x1^3*x0 + a2*x1^2*x0^2 + a3*x1*x0^3 + a4*x0^4
            sage: quartic = invariant_theory.binary_quartic(p, x0, x1)
            sage: quartic.coeffs()
            (a0, a1, a2, a3, a4)

            sage: R.<a0, a1, a2, a3, a4, x> = QQ[]
            sage: p = a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4
            sage: quartic = invariant_theory.binary_quartic(p, x)
            sage: quartic.coeffs()
            (a0, a1, a2, a3, a4)
        """
    def scaled_coeffs(self):
        """
        The coefficients of a binary quartic.

        Given

        .. MATH::

            f(x) = a_0 x_1^4 + 4 a_1 x_0 x_1^3 + 6 a_2 x_0^2 x_1^2 +
                   4 a_3 x_0^3 x_1 + a_4 x_0^4

        this function returns `a = (a_0, a_1, a_2, a_3, a_4)`

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x0, x1> = QQ[]
            sage: quartic = a0*x1^4 + 4*a1*x1^3*x0 + 6*a2*x1^2*x0^2 + 4*a3*x1*x0^3 + a4*x0^4
            sage: inv = invariant_theory.binary_quartic(quartic, x0, x1)
            sage: inv.scaled_coeffs()
            (a0, a1, a2, a3, a4)

            sage: R.<a0, a1, a2, a3, a4, x> = QQ[]
            sage: quartic = a0 + 4*a1*x + 6*a2*x^2 + 4*a3*x^3 + a4*x^4
            sage: inv = invariant_theory.binary_quartic(quartic, x)
            sage: inv.scaled_coeffs()
            (a0, a1, a2, a3, a4)
        """
    @cached_method
    def EisensteinD(self):
        """
        One of the Eisenstein invariants of a binary quartic.

        OUTPUT: the Eisenstein D-invariant of the quartic

        .. MATH::

              f(x) = a_0 x_1^4 + 4 a_1 x_0 x_1^3 + 6 a_2 x_0^2 x_1^2 +
                      4 a_3 x_0^3 x_1 + a_4 x_0^4
              \\\\\n              \\Rightarrow
              D(f) = a_0 a_4+3 a_2^2-4 a_1 a_3

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x0, x1> = QQ[]
            sage: f = a0*x1^4 + 4*a1*x0*x1^3 + 6*a2*x0^2*x1^2 + 4*a3*x0^3*x1 + a4*x0^4
            sage: inv = invariant_theory.binary_quartic(f, x0, x1)
            sage: inv.EisensteinD()
            3*a2^2 - 4*a1*a3 + a0*a4
        """
    @cached_method
    def EisensteinE(self):
        """
        One of the Eisenstein invariants of a binary quartic.

        OUTPUT: the Eisenstein E-invariant of the quartic

        .. MATH::

            f(x) = a_0 x_1^4 + 4 a_1 x_0 x_1^3 + 6 a_2 x_0^2 x_1^2 +
                   4 a_3 x_0^3 x_1 + a_4 x_0^4
            \\\\ \\Rightarrow
            E(f) = a_0 a_3^2 +a_1^2 a_4 -a_0 a_2 a_4
            -2 a_1 a_2 a_3 + a_2^3

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x0, x1> = QQ[]
            sage: f = a0*x1^4 + 4*a1*x0*x1^3 + 6*a2*x0^2*x1^2 + 4*a3*x0^3*x1 + a4*x0^4
            sage: inv = invariant_theory.binary_quartic(f, x0, x1)
            sage: inv.EisensteinE()
            a2^3 - 2*a1*a2*a3 + a0*a3^2 + a1^2*a4 - a0*a2*a4
        """
    @cached_method
    def g_covariant(self):
        """
        The g-covariant of a binary quartic.

        OUTPUT: the g-covariant of the quartic

        .. MATH::

              f(x) = a_0 x_1^4 + 4 a_1 x_0 x_1^3 + 6 a_2 x_0^2 x_1^2 +
                      4 a_3 x_0^3 x_1 + a_4 x_0^4
              \\\\\n              \\Rightarrow
              D(f) = \\frac{1}{144}
              \\begin{pmatrix}
                 \\frac{\\partial^2 f}{\\partial x \\partial x}
              \\end{pmatrix}

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x, y> = QQ[]
            sage: p = a0*x^4 + 4*a1*x^3*y + 6*a2*x^2*y^2 + 4*a3*x*y^3 + a4*y^4
            sage: inv = invariant_theory.binary_quartic(p, x, y)
            sage: g = inv.g_covariant();  g
            a1^2*x^4 - a0*a2*x^4 + 2*a1*a2*x^3*y - 2*a0*a3*x^3*y + 3*a2^2*x^2*y^2
            - 2*a1*a3*x^2*y^2 - a0*a4*x^2*y^2 + 2*a2*a3*x*y^3
            - 2*a1*a4*x*y^3 + a3^2*y^4 - a2*a4*y^4

            sage: inv_inhomogeneous = invariant_theory.binary_quartic(p.subs(y=1), x)
            sage: inv_inhomogeneous.g_covariant()
            a1^2*x^4 - a0*a2*x^4 + 2*a1*a2*x^3 - 2*a0*a3*x^3 + 3*a2^2*x^2
            - 2*a1*a3*x^2 - a0*a4*x^2 + 2*a2*a3*x - 2*a1*a4*x + a3^2 - a2*a4

            sage: g == 1/144 * (p.derivative(x,y)^2 - p.derivative(x,x)*p.derivative(y,y))
            True
        """
    @cached_method
    def h_covariant(self):
        """
        The h-covariant of a binary quartic.

        OUTPUT: the h-covariant of the quartic

        .. MATH::

              f(x) = a_0 x_1^4 + 4 a_1 x_0 x_1^3 + 6 a_2 x_0^2 x_1^2 +
                      4 a_3 x_0^3 x_1 + a_4 x_0^4
              \\\\\n              \\Rightarrow
              D(f) = \\frac{1}{144}
              \\begin{pmatrix}
                 \\frac{\\partial^2 f}{\\partial x \\partial x}
              \\end{pmatrix}

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, x, y> = QQ[]
            sage: p = a0*x^4 + 4*a1*x^3*y + 6*a2*x^2*y^2 + 4*a3*x*y^3 + a4*y^4
            sage: inv = invariant_theory.binary_quartic(p, x, y)
            sage: h = inv.h_covariant();   h
            -2*a1^3*x^6 + 3*a0*a1*a2*x^6 - a0^2*a3*x^6 - 6*a1^2*a2*x^5*y + 9*a0*a2^2*x^5*y
            - 2*a0*a1*a3*x^5*y - a0^2*a4*x^5*y - 10*a1^2*a3*x^4*y^2 + 15*a0*a2*a3*x^4*y^2
            - 5*a0*a1*a4*x^4*y^2 + 10*a0*a3^2*x^3*y^3 - 10*a1^2*a4*x^3*y^3
            + 10*a1*a3^2*x^2*y^4 - 15*a1*a2*a4*x^2*y^4 + 5*a0*a3*a4*x^2*y^4
            + 6*a2*a3^2*x*y^5 - 9*a2^2*a4*x*y^5 + 2*a1*a3*a4*x*y^5 + a0*a4^2*x*y^5
            + 2*a3^3*y^6 - 3*a2*a3*a4*y^6 + a1*a4^2*y^6

            sage: inv_inhomogeneous = invariant_theory.binary_quartic(p.subs(y=1), x)
            sage: inv_inhomogeneous.h_covariant()
            -2*a1^3*x^6 + 3*a0*a1*a2*x^6 - a0^2*a3*x^6 - 6*a1^2*a2*x^5 + 9*a0*a2^2*x^5
            - 2*a0*a1*a3*x^5 - a0^2*a4*x^5 - 10*a1^2*a3*x^4 + 15*a0*a2*a3*x^4
            - 5*a0*a1*a4*x^4 + 10*a0*a3^2*x^3 - 10*a1^2*a4*x^3 + 10*a1*a3^2*x^2
            - 15*a1*a2*a4*x^2 + 5*a0*a3*a4*x^2 + 6*a2*a3^2*x - 9*a2^2*a4*x
            + 2*a1*a3*a4*x + a0*a4^2*x + 2*a3^3 - 3*a2*a3*a4 + a1*a4^2

            sage: g = inv.g_covariant()
            sage: h == 1/8 * (p.derivative(x)*g.derivative(y) - p.derivative(y)*g.derivative(x))
            True
        """

class BinaryQuintic(AlgebraicForm):
    """
    Invariant theory of a binary quintic form.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See :meth:`~InvariantTheoryFactory.binary_quintic`
    for details.

    REFERENCES:

    For a description of all invariants and covariants of a binary
    quintic, see section 73 of [Cle1872]_.

    TESTS::

        sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
        sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
        sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
        sage: quintic._check_covariant('form')
        sage: quintic._check_covariant('A_invariant', invariant=True)
        sage: quintic._check_covariant('B_invariant', invariant=True)
        sage: quintic._check_covariant('C_invariant', invariant=True)
        sage: quintic._check_covariant('R_invariant', invariant=True)
        sage: quintic._check_covariant('H_covariant')
        sage: quintic._check_covariant('i_covariant')
        sage: quintic._check_covariant('T_covariant')
        sage: quintic._check_covariant('j_covariant')
        sage: quintic._check_covariant('tau_covariant')
        sage: quintic._check_covariant('theta_covariant')
        sage: quintic._check_covariant('alpha_covariant')
        sage: quintic._check_covariant('beta_covariant')
        sage: quintic._check_covariant('gamma_covariant')
        sage: quintic._check_covariant('delta_covariant')
        sage: TestSuite(quintic).run()

    Testing that more general coefficient rings also work as expected::

        sage: R.<a0,a1,a2,a3,a4,a5> = QQ[]
        sage: S.<x,y> = R[]
        sage: p = a0*x^5+a1*x^4*y+a2*x^3*y^2+a3*x^2*y^3+a4*x*y^4+a5*y^5
        sage: quintic = invariant_theory.binary_quintic(p)
        sage: quintic.i_covariant()
        (3/50*a2^2 - 4/25*a1*a3 + 2/5*a0*a4)*x^2 + (1/25*a2*a3 - 6/25*a1*a4
        + 2*a0*a5)*x*y + (3/50*a3^2 - 4/25*a2*a4 + 2/5*a1*a5)*y^2
    """
    def __init__(self, n, d, polynomial, *args) -> None:
        """
        The Python constructor.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import BinaryQuintic
            sage: BinaryQuintic(2, 5, x^5+2*x^3*y^2+3*x*y^4)
            Binary quintic with coefficients (0, 3, 0, 2, 0, 1)
        """
    @classmethod
    def from_invariants(cls, invariants, x, z, *args, **kwargs):
        """
        Construct a binary quintic from its invariants.

        This function constructs a binary quintic whose invariants equal
        the ones provided as argument up to scaling.

        INPUT:

        - ``invariants`` -- list or tuple of invariants that are used to
          reconstruct the binary quintic

        OUTPUT: a BinaryQuintic

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import BinaryQuintic
            sage: BinaryQuintic.from_invariants([3,6,12], x, y)
            Binary quintic with coefficients (0, 1, 0, 0, 1, 0)
        """
    @cached_method
    def monomials(self):
        """
        List the basis monomials of the form.

        This function lists a basis of monomials of the space of binary
        quintics of which this form is an element.

        OUTPUT:

        A tuple of monomials. They are in the same order as
        :meth:`coeffs`.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quintic = invariant_theory.binary_quintic(x^5 + y^5)
            sage: quintic.monomials()
            (y^5, x*y^4, x^2*y^3, x^3*y^2, x^4*y, x^5)
        """
    @cached_method
    def coeffs(self):
        """
        The coefficients of a binary quintic.

        Given

        .. MATH::

            f(x) = a_0 x_1^5 + a_1 x_0 x_1^4 + a_2 x_0^2 x_1^3 +
                   a_3 x_0^3 x_1^2 + a_4 x_0^4 x_1 + a_5 x_1^5

        this function returns `a = (a_0, a_1, a_2, a_3, a_4, a_5)`

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.coeffs()
            (a0, a1, a2, a3, a4, a5)

            sage: R.<a0, a1, a2, a3, a4, a5, x> = QQ[]
            sage: p = a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 + a5*x^5
            sage: quintic = invariant_theory.binary_quintic(p, x)
            sage: quintic.coeffs()
            (a0, a1, a2, a3, a4, a5)
        """
    def scaled_coeffs(self):
        """
        The coefficients of a binary quintic.

        Given

        .. MATH::

            f(x) = a_0 x_1^5 + 5 a_1 x_0 x_1^4 + 10 a_2 x_0^2 x_1^3 +
                   10 a_3 x_0^3 x_1^2 + 5 a_4 x_0^4 x_1 + a_5 x_1^5

        this function returns `a = (a_0, a_1, a_2, a_3, a_4, a_5)`

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + 5*a1*x1^4*x0 + 10*a2*x1^3*x0^2 + 10*a3*x1^2*x0^3 + 5*a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.scaled_coeffs()
            (a0, a1, a2, a3, a4, a5)

            sage: R.<a0, a1, a2, a3, a4, a5, x> = QQ[]
            sage: p = a0 + 5*a1*x + 10*a2*x^2 + 10*a3*x^3 + 5*a4*x^4 + a5*x^5
            sage: quintic = invariant_theory.binary_quintic(p, x)
            sage: quintic.scaled_coeffs()
            (a0, a1, a2, a3, a4, a5)
        """
    @cached_method
    def H_covariant(self, as_form: bool = False):
        """
        Return the covariant `H` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT: the `H`-covariant of the binary quintic as polynomial or as binary form

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.H_covariant()
            -2/25*a4^2*x0^6 + 1/5*a3*a5*x0^6 - 3/25*a3*a4*x0^5*x1
            + 3/5*a2*a5*x0^5*x1 - 3/25*a3^2*x0^4*x1^2 + 3/25*a2*a4*x0^4*x1^2
            + 6/5*a1*a5*x0^4*x1^2 - 4/25*a2*a3*x0^3*x1^3 + 14/25*a1*a4*x0^3*x1^3
            + 2*a0*a5*x0^3*x1^3 - 3/25*a2^2*x0^2*x1^4 + 3/25*a1*a3*x0^2*x1^4
            + 6/5*a0*a4*x0^2*x1^4 - 3/25*a1*a2*x0*x1^5 + 3/5*a0*a3*x0*x1^5
            - 2/25*a1^2*x1^6 + 1/5*a0*a2*x1^6

            sage: quintic.H_covariant(as_form=True)
            Binary sextic given by ...
        """
    @cached_method
    def i_covariant(self, as_form: bool = False):
        """
        Return the covariant `i` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT: the `i`-covariant of the binary quintic as polynomial or as binary form

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.i_covariant()
            3/50*a3^2*x0^2 - 4/25*a2*a4*x0^2 + 2/5*a1*a5*x0^2 + 1/25*a2*a3*x0*x1
            - 6/25*a1*a4*x0*x1 + 2*a0*a5*x0*x1 + 3/50*a2^2*x1^2 - 4/25*a1*a3*x1^2
            + 2/5*a0*a4*x1^2

            sage: quintic.i_covariant(as_form=True)
            Binary quadratic given by ...
        """
    @cached_method
    def T_covariant(self, as_form: bool = False):
        """
        Return the covariant `T` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT: the `T`-covariant of the binary quintic as polynomial or as binary form

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.T_covariant()
            2/125*a4^3*x0^9 - 3/50*a3*a4*a5*x0^9 + 1/10*a2*a5^2*x0^9
            + 9/250*a3*a4^2*x0^8*x1 - 3/25*a3^2*a5*x0^8*x1 + 1/50*a2*a4*a5*x0^8*x1
            + 2/5*a1*a5^2*x0^8*x1 + 3/250*a3^2*a4*x0^7*x1^2 + 8/125*a2*a4^2*x0^7*x1^2
            ...
            11/25*a0*a1*a4*x0^2*x1^7 - a0^2*a5*x0^2*x1^7 - 9/250*a1^2*a2*x0*x1^8
            + 3/25*a0*a2^2*x0*x1^8 - 1/50*a0*a1*a3*x0*x1^8 - 2/5*a0^2*a4*x0*x1^8
            - 2/125*a1^3*x1^9 + 3/50*a0*a1*a2*x1^9 - 1/10*a0^2*a3*x1^9

            sage: quintic.T_covariant(as_form=True)
            Binary nonic given by ...
        """
    @cached_method
    def j_covariant(self, as_form: bool = False):
        """
        Return the covariant `j` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT: the `j`-covariant of the binary quintic as polynomial or as binary form

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.j_covariant()
            -3/500*a3^3*x0^3 + 3/125*a2*a3*a4*x0^3 - 6/125*a1*a4^2*x0^3
            - 3/50*a2^2*a5*x0^3 + 3/25*a1*a3*a5*x0^3 - 3/500*a2*a3^2*x0^2*x1
            + 3/250*a2^2*a4*x0^2*x1 + 3/125*a1*a3*a4*x0^2*x1 - 6/25*a0*a4^2*x0^2*x1
            - 3/25*a1*a2*a5*x0^2*x1 + 3/5*a0*a3*a5*x0^2*x1 - 3/500*a2^2*a3*x0*x1^2
            + 3/250*a1*a3^2*x0*x1^2 + 3/125*a1*a2*a4*x0*x1^2 - 3/25*a0*a3*a4*x0*x1^2
            - 6/25*a1^2*a5*x0*x1^2 + 3/5*a0*a2*a5*x0*x1^2 - 3/500*a2^3*x1^3
            + 3/125*a1*a2*a3*x1^3 - 3/50*a0*a3^2*x1^3 - 6/125*a1^2*a4*x1^3
            + 3/25*a0*a2*a4*x1^3

            sage: quintic.j_covariant(as_form=True)
            Binary cubic given by ...
        """
    @cached_method
    def tau_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\tau` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\tau`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.tau_covariant()
            1/62500*a2^2*a3^4*x0^2 - 3/62500*a1*a3^5*x0^2
            - 1/15625*a2^3*a3^2*a4*x0^2 + 1/6250*a1*a2*a3^3*a4*x0^2
            + 3/6250*a0*a3^4*a4*x0^2 - 1/31250*a2^4*a4^2*x0^2
            ...
            - 2/125*a0*a1*a2^2*a4*a5*x1^2 - 4/125*a0*a1^2*a3*a4*a5*x1^2
            + 2/25*a0^2*a2*a3*a4*a5*x1^2 - 8/625*a1^4*a5^2*x1^2
            + 8/125*a0*a1^2*a2*a5^2*x1^2 - 2/25*a0^2*a2^2*a5^2*x1^2

            sage: quintic.tau_covariant(as_form=True)
            Binary quadratic given by ...
        """
    @cached_method
    def theta_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\theta` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\theta`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.theta_covariant()
            -1/625000*a2^3*a3^5*x0^2 + 9/1250000*a1*a2*a3^6*x0^2
            - 27/1250000*a0*a3^7*x0^2 + 3/250000*a2^4*a3^3*a4*x0^2
            - 7/125000*a1*a2^2*a3^4*a4*x0^2 - 3/312500*a1^2*a3^5*a4*x0^2
            ...
            + 6/625*a0^2*a1*a2^2*a4*a5^2*x1^2 + 24/625*a0^2*a1^2*a3*a4*a5^2*x1^2
            - 12/125*a0^3*a2*a3*a4*a5^2*x1^2 + 8/625*a0*a1^4*a5^3*x1^2
            - 8/125*a0^2*a1^2*a2*a5^3*x1^2 + 2/25*a0^3*a2^2*a5^3*x1^2

            sage: quintic.theta_covariant(as_form=True)
            Binary quadratic given by ...
        """
    @cached_method
    def alpha_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\alpha` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\alpha`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.alpha_covariant()
            1/2500*a2^2*a3^3*x0 - 3/2500*a1*a3^4*x0 - 1/625*a2^3*a3*a4*x0
            + 3/625*a1*a2*a3^2*a4*x0 + 3/625*a0*a3^3*a4*x0 + 2/625*a1*a2^2*a4^2*x0
            - 6/625*a1^2*a3*a4^2*x0 - 12/625*a0*a2*a3*a4^2*x0 + 24/625*a0*a1*a4^3*x0
            ...
            - 12/625*a1^2*a2*a3*a5*x1 - 1/125*a0*a2^2*a3*a5*x1
            + 8/125*a0*a1*a3^2*a5*x1 + 24/625*a1^3*a4*a5*x1 - 8/125*a0*a1*a2*a4*a5*x1
            - 4/25*a0^2*a3*a4*a5*x1 - 4/25*a0*a1^2*a5^2*x1 + 2/5*a0^2*a2*a5^2*x1

            sage: quintic.alpha_covariant(as_form=True)
            Binary monic given by ...
        """
    @cached_method
    def beta_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\beta` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\beta`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.beta_covariant()
            -1/62500*a2^3*a3^4*x0 + 9/125000*a1*a2*a3^5*x0 - 27/125000*a0*a3^6*x0
            + 13/125000*a2^4*a3^2*a4*x0 - 31/62500*a1*a2^2*a3^3*a4*x0
            - 3/62500*a1^2*a3^4*a4*x0 + 27/15625*a0*a2*a3^4*a4*x0
            ...
            - 16/125*a0^2*a1*a3^2*a5^2*x1 - 28/625*a0*a1^3*a4*a5^2*x1
            + 6/125*a0^2*a1*a2*a4*a5^2*x1 + 8/25*a0^3*a3*a4*a5^2*x1
            + 4/25*a0^2*a1^2*a5^3*x1 - 2/5*a0^3*a2*a5^3*x1

            sage: quintic.beta_covariant(as_form=True)
            Binary monic given by ...
        """
    @cached_method
    def gamma_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\gamma` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\gamma`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.gamma_covariant()
            1/156250000*a2^5*a3^6*x0 - 3/62500000*a1*a2^3*a3^7*x0
            + 27/312500000*a1^2*a2*a3^8*x0 + 27/312500000*a0*a2^2*a3^8*x0
            - 81/312500000*a0*a1*a3^9*x0 - 19/312500000*a2^6*a3^4*a4*x0
            ...
            - 32/3125*a0^2*a1^3*a2^2*a5^4*x1 + 6/625*a0^3*a1*a2^3*a5^4*x1
            - 8/3125*a0^2*a1^4*a3*a5^4*x1 + 8/625*a0^3*a1^2*a2*a3*a5^4*x1
            - 2/125*a0^4*a2^2*a3*a5^4*x1

            sage: quintic.gamma_covariant(as_form=True)
            Binary monic given by ...
        """
    @cached_method
    def delta_covariant(self, as_form: bool = False):
        """
        Return the covariant `\\delta` of a binary quintic.

        INPUT:

        - ``as_form`` -- if ``as_form`` is ``False``, the result will be returned
          as polynomial (default). If it is ``True`` the result is returned as
          an object of the class :class:`AlgebraicForm`.

        OUTPUT:

        The `\\delta`-covariant of the binary quintic as polynomial or as binary form.

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.delta_covariant()
            1/1562500000*a2^6*a3^7*x0 - 9/1562500000*a1*a2^4*a3^8*x0
            + 9/625000000*a1^2*a2^2*a3^9*x0 + 9/781250000*a0*a2^3*a3^9*x0
            - 9/1562500000*a1^3*a3^10*x0 - 81/1562500000*a0*a1*a2*a3^10*x0
            ...
            + 64/3125*a0^3*a1^3*a2^2*a5^5*x1 - 12/625*a0^4*a1*a2^3*a5^5*x1
            + 16/3125*a0^3*a1^4*a3*a5^5*x1 - 16/625*a0^4*a1^2*a2*a3*a5^5*x1
            + 4/125*a0^5*a2^2*a3*a5^5*x1

            sage: quintic.delta_covariant(as_form=True)
            Binary monic given by ...
        """
    @cached_method
    def A_invariant(self):
        """
        Return the invariant `A` of a binary quintic.

        OUTPUT: the `A`-invariant of the binary quintic

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.A_invariant()
            4/625*a2^2*a3^2 - 12/625*a1*a3^3 - 12/625*a2^3*a4
            + 38/625*a1*a2*a3*a4 + 6/125*a0*a3^2*a4 - 18/625*a1^2*a4^2
            - 16/125*a0*a2*a4^2 + 6/125*a1*a2^2*a5 - 16/125*a1^2*a3*a5
            - 2/25*a0*a2*a3*a5 + 4/5*a0*a1*a4*a5 - 2*a0^2*a5^2
        """
    @cached_method
    def B_invariant(self):
        """
        Return the invariant `B` of a binary quintic.

        OUTPUT: the `B`-invariant of the binary quintic

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.B_invariant()
            1/1562500*a2^4*a3^4 - 3/781250*a1*a2^2*a3^5 + 9/1562500*a1^2*a3^6
            - 3/781250*a2^5*a3^2*a4 + 37/1562500*a1*a2^3*a3^3*a4
            - 57/1562500*a1^2*a2*a3^4*a4 + 3/312500*a0*a2^2*a3^4*a4
            ...
            + 8/625*a0^2*a1^2*a4^2*a5^2 - 4/125*a0^3*a2*a4^2*a5^2 - 16/3125*a1^5*a5^3
            + 4/125*a0*a1^3*a2*a5^3 - 6/125*a0^2*a1*a2^2*a5^3
            - 4/125*a0^2*a1^2*a3*a5^3 + 2/25*a0^3*a2*a3*a5^3
        """
    @cached_method
    def C_invariant(self):
        """
        Return the invariant `C` of a binary quintic.

        OUTPUT: the `C`-invariant of the binary quintic

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.C_invariant()
            -3/1953125000*a2^6*a3^6 + 27/1953125000*a1*a2^4*a3^7
            - 249/7812500000*a1^2*a2^2*a3^8 - 3/78125000*a0*a2^3*a3^8
            + 3/976562500*a1^3*a3^9 + 27/156250000*a0*a1*a2*a3^9
            ...
            + 192/15625*a0^2*a1^3*a2^2*a3*a5^4 - 36/3125*a0^3*a1*a2^3*a3*a5^4
            + 24/15625*a0^2*a1^4*a3^2*a5^4 - 24/3125*a0^3*a1^2*a2*a3^2*a5^4
            + 6/625*a0^4*a2^2*a3^2*a5^4
        """
    @cached_method
    def R_invariant(self):
        """
        Return the invariant `R` of a binary quintic.

        OUTPUT: the `R`-invariant of the binary quintic

        EXAMPLES::

            sage: R.<a0, a1, a2, a3, a4, a5, x0, x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.R_invariant()
            3/3906250000000*a1^2*a2^5*a3^11 - 3/976562500000*a0*a2^6*a3^11
            - 51/7812500000000*a1^3*a2^3*a3^12 + 27/976562500000*a0*a1*a2^4*a3^12
            + 27/1953125000000*a1^4*a2*a3^13 - 81/1562500000000*a0*a1^2*a2^2*a3^13
            ...
            + 384/9765625*a0*a1^10*a5^7 - 192/390625*a0^2*a1^8*a2*a5^7
            + 192/78125*a0^3*a1^6*a2^2*a5^7 - 96/15625*a0^4*a1^4*a2^3*a5^7
            + 24/3125*a0^5*a1^2*a2^4*a5^7 - 12/3125*a0^6*a2^5*a5^7
        """
    @cached_method
    def invariants(self, type: str = 'clebsch'):
        """
        Return a tuple of invariants of a binary quintic.

        INPUT:

        - ``type`` -- the type of invariants to return; the default choice
          is to return the Clebsch invariants

        OUTPUT: the invariants of the binary quintic

        EXAMPLES::

            sage: R.<x0, x1> = QQ[]
            sage: p = 2*x1^5 + 4*x1^4*x0 + 5*x1^3*x0^2 + 7*x1^2*x0^3 - 11*x1*x0^4 + x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.invariants()
            (-276032/625,
             4983526016/390625,
             -247056495846408/244140625,
             -148978972828696847376/30517578125)
            sage: quintic.invariants('unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown type of invariants unknown for a binary quintic
        """
    @cached_method
    def clebsch_invariants(self, as_tuple: bool = False):
        """
        Return the invariants of a binary quintic as described by Clebsch.

        The following invariants are returned: `A`, `B`, `C` and `R`.

        OUTPUT: the Clebsch invariants of the binary quintic

        EXAMPLES::

            sage: R.<x0, x1> = QQ[]
            sage: p = 2*x1^5 + 4*x1^4*x0 + 5*x1^3*x0^2 + 7*x1^2*x0^3 - 11*x1*x0^4 + x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.clebsch_invariants()
            {'A': -276032/625,
             'B': 4983526016/390625,
             'C': -247056495846408/244140625,
             'R': -148978972828696847376/30517578125}

            sage: quintic.clebsch_invariants(as_tuple=True)
            (-276032/625,
             4983526016/390625,
             -247056495846408/244140625,
             -148978972828696847376/30517578125)
        """
    @cached_method
    def arithmetic_invariants(self):
        """
        Return a set of generating arithmetic invariants of a binary quintic.

        An arithmetic invariants is an invariant whose coefficients are
        integers for a general binary quintic. They are linear combinations
        of the Clebsch invariants, such that they still generate the ring of
        invariants.

        OUTPUT: the arithmetic invariants of the binary quintic. They are given by

        .. MATH::

            \\begin{aligned}
            I_4 & = 2^{-1} \\cdot 5^4 \\cdot A \\\\\n            I_8 & = 5^5 \\cdot (2^{-1} \\cdot 47 \\cdot A^2 - 2^2 \\cdot B) \\\\\n            I_{12} & = 5^{10} \\cdot (2^{-1} \\cdot 3 \\cdot A^3
                            - 2^5 \\cdot 3^{-1} \\cdot C) \\\\\n            I_{18} & = 2^8 \\cdot 3^{-1} \\cdot 5^{15} \\cdot R \\\\\n            \\end{aligned}

        where `A`, `B`, `C` and `R` are the
        :meth:`BinaryQuintic.clebsch_invariants`.

        EXAMPLES::

            sage: R.<x0, x1> = QQ[]
            sage: p = 2*x1^5 + 4*x1^4*x0 + 5*x1^3*x0^2 + 7*x1^2*x0^3 - 11*x1*x0^4 + x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: quintic.arithmetic_invariants()
            {'I12': -1156502613073152,
             'I18': -12712872348048797642752,
             'I4': -138016,
             'I8': 14164936192}

        We can check that the coefficients of the invariants have no common divisor
        for a general quintic form::

            sage: R.<a0,a1,a2,a3,a4,a5,x0,x1> = QQ[]
            sage: p = a0*x1^5 + a1*x1^4*x0 + a2*x1^3*x0^2 + a3*x1^2*x0^3 + a4*x1*x0^4 + a5*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: invs = quintic.arithmetic_invariants()
            sage: [invs[x].content() for x in invs]
            [1, 1, 1, 1]
        """
    @cached_method
    def canonical_form(self, reduce_gcd: bool = False):
        """
        Return a canonical representative of the quintic.

        Given a binary quintic `f` with coefficients in a field `K`, returns a
        canonical representative of the `GL(2,\\bar{K})`-orbit of the quintic,
        where `\\bar{K}` is an algebraic closure of `K`. This means that two
        binary quintics `f` and `g` are `GL(2,\\bar{K})`-equivalent if and only
        if their canonical forms are the same.

        INPUT:

        - ``reduce_gcd`` -- if set to ``True``, then a variant of this canonical
          form is computed where the coefficients are coprime integers. The
          obtained form is then unique up to multiplication by a unit. See also
          :meth:`~sage.rings.invariants.reconstruction.binary_quintic_from_invariants`'.

        OUTPUT:

        A canonical `GL(2,\\bar{K})`-equivalent binary quintic.

        EXAMPLES::

            sage: R.<x0, x1> = QQ[]
            sage: p = 2*x1^5 + 4*x1^4*x0 + 5*x1^3*x0^2 + 7*x1^2*x0^3 - 11*x1*x0^4 + x0^5
            sage: f = invariant_theory.binary_quintic(p, x0, x1)
            sage: g = matrix(QQ, [[11,5],[7,2]])
            sage: gf = f.transformed(g)
            sage: f.canonical_form() == gf.canonical_form()
            True
            sage: h = f.canonical_form(reduce_gcd=True)
            sage: gcd(h.coeffs())
            1
        """

class TernaryQuadratic(QuadraticForm):
    """
    Invariant theory of a ternary quadratic.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See
    :meth:`~InvariantTheoryFactory.ternary_quadratic` for details.

    TESTS::

        sage: R.<x,y,z> = QQ[]
        sage: quadratic = invariant_theory.ternary_quadratic(x^2+y^2+z^2)
        sage: quadratic
        Ternary quadratic with coefficients (1, 1, 1, 0, 0, 0)
        sage: TestSuite(quadratic).run()
    """
    def __init__(self, n, d, polynomial, *args) -> None:
        """
        The Python constructor.

        INPUT:

        See :meth:`~InvariantTheoryFactory.ternary_quadratic`.

        TESTS::

            sage: R.<x,y,z> = QQ[]
            sage: from sage.rings.invariants.invariant_theory import TernaryQuadratic
            sage: TernaryQuadratic(3, 2, x^2+y^2+z^2)
            Ternary quadratic with coefficients (1, 1, 1, 0, 0, 0)
        """
    @cached_method
    def monomials(self):
        """
        List the basis monomials of the form.

        OUTPUT:

        A tuple of monomials. They are in the same order as
        :meth:`coeffs`.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: quadratic = invariant_theory.ternary_quadratic(x^2 + y*z)
            sage: quadratic.monomials()
            (x^2, y^2, z^2, x*y, x*z, y*z)
        """
    @cached_method
    def coeffs(self):
        """
        Return the coefficients of a quadratic.

        Given

        .. MATH::

            p(x,y) =&\\;
            a_{20} x^{2} + a_{11} x y + a_{02} y^{2} +
            a_{10} x + a_{01} y + a_{00}

        this function returns
        `a = (a_{20}, a_{02}, a_{00}, a_{11}, a_{10}, a_{01} )`

        EXAMPLES::

            sage: R.<x,y,z,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a20*x^2 + a11*x*y + a02*y^2 +
            ....:       a10*x*z + a01*y*z + a00*z^2 )
            sage: invariant_theory.ternary_quadratic(p, x,y,z).coeffs()
            (a20, a02, a00, a11, a10, a01)
            sage: invariant_theory.ternary_quadratic(p.subs(z=1), x, y).coeffs()
            (a20, a02, a00, a11, a10, a01)
        """
    def scaled_coeffs(self):
        """
        Return the scaled coefficients of a quadratic.

        Given

        .. MATH::

            p(x,y) =&\\;
            a_{20} x^{2} + a_{11} x y + a_{02} y^{2} +
            a_{10} x + a_{01} y + a_{00}

        this function returns
        `a = (a_{20}, a_{02}, a_{00}, a_{11}/2, a_{10}/2, a_{01}/2, )`

        EXAMPLES::

            sage: R.<x,y,z,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a20*x^2 + a11*x*y + a02*y^2 +
            ....:       a10*x*z + a01*y*z + a00*z^2 )
            sage: invariant_theory.ternary_quadratic(p, x,y,z).scaled_coeffs()
            (a20, a02, a00, 1/2*a11, 1/2*a10, 1/2*a01)
            sage: invariant_theory.ternary_quadratic(p.subs(z=1), x, y).scaled_coeffs()
            (a20, a02, a00, 1/2*a11, 1/2*a10, 1/2*a01)
        """
    def covariant_conic(self, other):
        """
        Return the ternary quadratic covariant to ``self`` and ``other``.

        INPUT:

        - ``other`` -- another ternary quadratic

        OUTPUT:

        The so-called covariant conic, a ternary quadratic. It is
        symmetric under exchange of ``self`` and ``other``.

        EXAMPLES::

            sage: ring.<x,y,z> = QQ[]
            sage: Q = invariant_theory.ternary_quadratic(x^2 + y^2 + z^2)
            sage: R = invariant_theory.ternary_quadratic(x*y + x*z + y*z)
            sage: Q.covariant_conic(R)
            -x*y - x*z - y*z
            sage: R.covariant_conic(Q)
            -x*y - x*z - y*z

        TESTS::

            sage: R.<a,a_,b,b_,c,c_,f,f_,g,g_,h,h_,x,y,z> = QQ[]
            sage: p = ( a*x^2 + 2*h*x*y + b*y^2 +
            ....:       2*g*x*z + 2*f*y*z + c*z^2 )
            sage: Q = invariant_theory.ternary_quadratic(p, [x,y,z])
            sage: Q.matrix()
            [a h g]
            [h b f]
            [g f c]
            sage: p = ( a_*x^2 + 2*h_*x*y + b_*y^2 +
            ....:       2*g_*x*z + 2*f_*y*z + c_*z^2 )
            sage: Q_ = invariant_theory.ternary_quadratic(p, [x,y,z])
            sage: Q_.matrix()
            [a_ h_ g_]
            [h_ b_ f_]
            [g_ f_ c_]
            sage: QQ_ = Q.covariant_conic(Q_)
            sage: invariant_theory.ternary_quadratic(QQ_, [x,y,z]).matrix()
            [      b_*c + b*c_ - 2*f*f_  f_*g + f*g_ - c_*h - c*h_ -b_*g - b*g_ + f_*h + f*h_]
            [ f_*g + f*g_ - c_*h - c*h_       a_*c + a*c_ - 2*g*g_ -a_*f - a*f_ + g_*h + g*h_]
            [-b_*g - b*g_ + f_*h + f*h_ -a_*f - a*f_ + g_*h + g*h_       a_*b + a*b_ - 2*h*h_]
        """

class TernaryCubic(AlgebraicForm):
    """
    Invariant theory of a ternary cubic.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See :meth:`~InvariantTheoryFactory.ternary_cubic`
    for details.

    TESTS::

        sage: R.<x,y,z> = QQ[]
        sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
        sage: cubic
        Ternary cubic with coefficients (1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
        sage: TestSuite(cubic).run()
    """
    def __init__(self, n, d, polynomial, *args) -> None:
        """
        The Python constructor.

        TESTS::

            sage: R.<x,y,z> = QQ[]
            sage: p = 2837*x^3 + 1363*x^2*y + 6709*x^2*z +             ....:   5147*x*y^2 + 2769*x*y*z + 912*x*z^2 + 4976*y^3 +             ....:   2017*y^2*z + 4589*y*z^2 + 9681*z^3
            sage: cubic = invariant_theory.ternary_cubic(p)
            sage: cubic._check_covariant('S_invariant', invariant=True)
            sage: cubic._check_covariant('T_invariant', invariant=True)
            sage: cubic._check_covariant('form')
            sage: cubic._check_covariant('Hessian')
            sage: cubic._check_covariant('Theta_covariant')
            sage: cubic._check_covariant('J_covariant')
        """
    @cached_method
    def monomials(self):
        """
        List the basis monomials of the form.

        OUTPUT:

        A tuple of monomials. They are in the same order as
        :meth:`coeffs`.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3+y*z^2)
            sage: cubic.monomials()
            (x^3, y^3, z^3, x^2*y, x^2*z, x*y^2, y^2*z, x*z^2, y*z^2, x*y*z)
        """
    @cached_method
    def coeffs(self):
        """
        Return the coefficients of a cubic.

        Given

        .. MATH::

            \\begin{split}
              p(x,y) =&\\;
              a_{30} x^{3} + a_{21} x^{2} y + a_{12} x y^{2} +
              a_{03} y^{3} + a_{20} x^{2} +
              \\\\ &\\;
              a_{11} x y +
              a_{02} y^{2} + a_{10} x + a_{01} y + a_{00}
            \\end{split}

        this function returns
        `a = (a_{30}, a_{03}, a_{00}, a_{21}, a_{20}, a_{12}, a_{02}, a_{10}, a_{01}, a_{11})`

        EXAMPLES::

            sage: R.<x,y,z,a30,a21,a12,a03,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a30*x^3 + a21*x^2*y + a12*x*y^2 + a03*y^3 + a20*x^2*z +
            ....:       a11*x*y*z + a02*y^2*z + a10*x*z^2 + a01*y*z^2 + a00*z^3 )
            sage: invariant_theory.ternary_cubic(p, x,y,z).coeffs()
            (a30, a03, a00, a21, a20, a12, a02, a10, a01, a11)
            sage: invariant_theory.ternary_cubic(p.subs(z=1), x, y).coeffs()
            (a30, a03, a00, a21, a20, a12, a02, a10, a01, a11)
        """
    def scaled_coeffs(self):
        """
        Return the coefficients of a cubic.

        Compared to :meth:`coeffs`, this method returns rescaled
        coefficients that are often used in invariant theory.

        Given

        .. MATH::

            \\begin{split}
              p(x,y) =&\\;
              a_{30} x^{3} + a_{21} x^{2} y + a_{12} x y^{2} +
              a_{03} y^{3} + a_{20} x^{2} +
              \\\\ &\\;
              a_{11} x y +
              a_{02} y^{2} + a_{10} x + a_{01} y + a_{00}
            \\end{split}

        this function returns
        `a = (a_{30}, a_{03}, a_{00}, a_{21}/3, a_{20}/3, a_{12}/3, a_{02}/3, a_{10}/3, a_{01}/3, a_{11}/6)`

        EXAMPLES::

            sage: R.<x,y,z,a30,a21,a12,a03,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a30*x^3 + a21*x^2*y + a12*x*y^2 + a03*y^3 + a20*x^2*z +
            ....:       a11*x*y*z + a02*y^2*z + a10*x*z^2 + a01*y*z^2 + a00*z^3 )
            sage: invariant_theory.ternary_cubic(p, x,y,z).scaled_coeffs()
            (a30, a03, a00, 1/3*a21, 1/3*a20, 1/3*a12, 1/3*a02, 1/3*a10, 1/3*a01, 1/6*a11)
        """
    def S_invariant(self):
        """
        Return the S-invariant.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^2*y + y^3 + z^3 + x*y*z)
            sage: cubic.S_invariant()
            -1/1296
        """
    def T_invariant(self):
        """
        Return the T-invariant.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
            sage: cubic.T_invariant()
            1

            sage: R.<x,y,z,t> = GF(7)[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3 + t*x*y*z, [x,y,z])
            sage: cubic.T_invariant()
            -t^6 - t^3 + 1
        """
    @cached_method
    def polar_conic(self):
        """
        Return the polar conic of the cubic.

        OUTPUT:

        Given the ternary cubic `f(X,Y,Z)`, this method returns the
        symmetric matrix `A(x,y,z)` defined by

        .. MATH::

            x f_X + y f_Y + z f_Z = (X,Y,Z) \\cdot A(x,y,z) \\cdot (X,Y,Z)^t

        EXAMPLES::

            sage: R.<x,y,z,X,Y,Z,a30,a21,a12,a03,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a30*x^3 + a21*x^2*y + a12*x*y^2 + a03*y^3 + a20*x^2*z +
            ....:       a11*x*y*z + a02*y^2*z + a10*x*z^2 + a01*y*z^2 + a00*z^3 )
            sage: cubic = invariant_theory.ternary_cubic(p, x,y,z)
            sage: cubic.polar_conic()
            [  3*x*a30 + y*a21 + z*a20 x*a21 + y*a12 + 1/2*z*a11 x*a20 + 1/2*y*a11 + z*a10]
            [x*a21 + y*a12 + 1/2*z*a11   x*a12 + 3*y*a03 + z*a02 1/2*x*a11 + y*a02 + z*a01]
            [x*a20 + 1/2*y*a11 + z*a10 1/2*x*a11 + y*a02 + z*a01   x*a10 + y*a01 + 3*z*a00]

            sage: polar_eqn = X*p.derivative(x) + Y*p.derivative(y) + Z*p.derivative(z)
            sage: polar = invariant_theory.ternary_quadratic(polar_eqn, [x,y,z])
            sage: polar.matrix().subs(X=x,Y=y,Z=z) == cubic.polar_conic()
            True
        """
    @cached_method
    def Hessian(self):
        """
        Return the Hessian covariant.

        OUTPUT:

        The Hessian matrix multiplied with the conventional
        normalization factor `1/216`.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
            sage: cubic.Hessian()
            x*y*z

            sage: R.<x,y> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + 1)
            sage: cubic.Hessian()
            x*y
        """
    def Theta_covariant(self):
        """
        Return the `\\Theta` covariant.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
            sage: cubic.Theta_covariant()
            -x^3*y^3 - x^3*z^3 - y^3*z^3

            sage: R.<x,y> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + 1)
            sage: cubic.Theta_covariant()
            -x^3*y^3 - x^3 - y^3

            sage: R.<x,y,z,a30,a21,a12,a03,a20,a11,a02,a10,a01,a00> = QQ[]
            sage: p = ( a30*x^3 + a21*x^2*y + a12*x*y^2 + a03*y^3 + a20*x^2*z +
            ....:       a11*x*y*z + a02*y^2*z + a10*x*z^2 + a01*y*z^2 + a00*z^3 )
            sage: cubic = invariant_theory.ternary_cubic(p, x,y,z)
            sage: len(list(cubic.Theta_covariant()))
            6952
        """
    def J_covariant(self):
        """
        Return the J-covariant of the ternary cubic.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
            sage: cubic.J_covariant()
            x^6*y^3 - x^3*y^6 - x^6*z^3 + y^6*z^3 + x^3*z^6 - y^3*z^6

            sage: R.<x,y> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + 1)
            sage: cubic.J_covariant()
            x^6*y^3 - x^3*y^6 - x^6 + y^6 + x^3 - y^3
        """
    def syzygy(self, U, S, T, H, Theta, J):
        """
        Return the syzygy of the cubic evaluated on the invariants
        and covariants.

        INPUT:

        - ``U``, ``S``, ``T``, ``H``, ``Theta``, ``J`` --
          polynomials from the same polynomial ring.

        OUTPUT:

        0 if evaluated for the form, the S invariant, the T invariant,
        the Hessian, the `\\Theta` covariant and the J-covariant
        of a ternary cubic.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: monomials = (x^3, y^3, z^3, x^2*y, x^2*z, x*y^2,
            ....:              y^2*z, x*z^2, y*z^2, x*y*z)
            sage: random_poly = sum([ randint(0,10000) * m for m in monomials ])
            sage: cubic = invariant_theory.ternary_cubic(random_poly)
            sage: U = cubic.form()
            sage: S = cubic.S_invariant()
            sage: T = cubic.T_invariant()
            sage: H = cubic.Hessian()
            sage: Theta = cubic.Theta_covariant()
            sage: J = cubic.J_covariant()
            sage: cubic.syzygy(U, S, T, H, Theta, J)
            0
        """

class SeveralAlgebraicForms(FormsBase):
    """
    The base class of multiple algebraic forms (i.e. homogeneous polynomials).

    You should only instantiate the derived classes of this base
    class.

    See :class:`AlgebraicForm` for the base class of a single
    algebraic form.

    INPUT:

    - ``forms`` -- list/tuple/iterable of at least one
      :class:`AlgebraicForm` object, all with the same number of
      variables. Interpreted as multiple homogeneous polynomials in a
      common polynomial ring.

    EXAMPLES::

        sage: from sage.rings.invariants.invariant_theory import AlgebraicForm, SeveralAlgebraicForms
        sage: R.<x,y> = QQ[]
        sage: p = AlgebraicForm(2, 2, x^2, (x,y))
        sage: q = AlgebraicForm(2, 2, y^2, (x,y))
        sage: pq = SeveralAlgebraicForms([p, q])
    """
    def __init__(self, forms) -> None:
        """
        The Python constructor.

        TESTS::

            sage: from sage.rings.invariants.invariant_theory import AlgebraicForm, SeveralAlgebraicForms
            sage: R.<x,y,z> = QQ[]
            sage: p = AlgebraicForm(2, 2, x^2 + y^2)
            sage: q = AlgebraicForm(2, 3, x^3 + y^3)
            sage: r = AlgebraicForm(3, 3, x^3 + y^3 + z^3)
            sage: pq = SeveralAlgebraicForms([p, q])
            sage: pr = SeveralAlgebraicForms([p, r])
            Traceback (most recent call last):
            ...
            ValueError: all forms must be in the same variables
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` with ``other``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: q1 = invariant_theory.quadratic_form(x^2 + y^2)
            sage: q2 = invariant_theory.quadratic_form(x*y)
            sage: from sage.rings.invariants.invariant_theory import SeveralAlgebraicForms
            sage: two_inv = SeveralAlgebraicForms([q1, q2])
            sage: two_inv == 'foo'
            False
            sage: two_inv == two_inv
            True
        """
    def n_forms(self):
        """
        Return the number of forms.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: q1 = invariant_theory.quadratic_form(x^2 + y^2)
            sage: q2 = invariant_theory.quadratic_form(x*y)
            sage: from sage.rings.invariants.invariant_theory import SeveralAlgebraicForms
            sage: q12 = SeveralAlgebraicForms([q1, q2])
            sage: q12.n_forms()
            2
            sage: len(q12) == q12.n_forms()    # syntactic sugar
            True
        """
    __len__ = n_forms
    def get_form(self, i):
        """
        Return the `i`-th form.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: q1 = invariant_theory.quadratic_form(x^2 + y^2)
            sage: q2 = invariant_theory.quadratic_form(x*y)
            sage: from sage.rings.invariants.invariant_theory import SeveralAlgebraicForms
            sage: q12 = SeveralAlgebraicForms([q1, q2])
            sage: q12.get_form(0) is q1
            True
            sage: q12.get_form(1) is q2
            True
            sage: q12[0] is q12.get_form(0)   # syntactic sugar
            True
            sage: q12[1] is q12.get_form(1)   # syntactic sugar
            True
        """
    __getitem__ = get_form
    def homogenized(self, var: str = 'h'):
        """
        Return form as defined by a homogeneous polynomial.

        INPUT:

        - ``var`` -- either a variable name, variable index or a
          variable (default: ``'h'``)

        OUTPUT:

        The same algebraic form, but defined by a homogeneous
        polynomial.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: q = invariant_theory.quaternary_biquadratic(x^2 + 1, y^2 + 1, [x,y,z])
            sage: q
            Joint quaternary quadratic with coefficients (1, 0, 0, 1, 0, 0, 0, 0, 0, 0)
            and quaternary quadratic with coefficients (0, 1, 0, 1, 0, 0, 0, 0, 0, 0)
            sage: q.homogenized()
            Joint quaternary quadratic with coefficients (1, 0, 0, 1, 0, 0, 0, 0, 0, 0)
            and quaternary quadratic with coefficients (0, 1, 0, 1, 0, 0, 0, 0, 0, 0)
            sage: type(q) is type(q.homogenized())
            True
        """

class TwoAlgebraicForms(SeveralAlgebraicForms):
    def first(self):
        """
        Return the first of the two forms.

        OUTPUT: the first algebraic form used in the definition

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: q0 = invariant_theory.quadratic_form(x^2 + y^2)
            sage: q1 = invariant_theory.quadratic_form(x*y)
            sage: from sage.rings.invariants.invariant_theory import TwoAlgebraicForms
            sage: q = TwoAlgebraicForms([q0, q1])
            sage: q.first() is q0
            True
            sage: q.get_form(0) is q0
            True
            sage: q.first().polynomial()
            x^2 + y^2
        """
    def second(self):
        """
        Return the second of the two forms.

        OUTPUT: the second form used in the definition

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: q0 = invariant_theory.quadratic_form(x^2 + y^2)
            sage: q1 = invariant_theory.quadratic_form(x*y)
            sage: from sage.rings.invariants.invariant_theory import TwoAlgebraicForms
            sage: q = TwoAlgebraicForms([q0, q1])
            sage: q.second() is q1
            True
            sage: q.get_form(1) is q1
            True
            sage: q.second().polynomial()
            x*y
        """

class TwoTernaryQuadratics(TwoAlgebraicForms):
    '''
    Invariant theory of two ternary quadratics.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See
    :meth:`~InvariantTheoryFactory.ternary_biquadratics` for
    details.

    REFERENCES:

    - Section on "Invariants and Covariants of Systems of Conics",
      Art. 388 (a) in [Sal1954]_

    TESTS::

        sage: R.<x,y,z> = QQ[]
        sage: inv = invariant_theory.ternary_biquadratic(x^2 + y^2 + z^2,
        ....:                                            x*y + y*z + x*z, [x, y, z])
        sage: inv
        Joint ternary quadratic with coefficients (1, 1, 1, 0, 0, 0) and ternary
        quadratic with coefficients (0, 0, 0, 1, 1, 1)
        sage: TestSuite(inv).run()

        sage: q1 = 73*x^2 + 96*x*y - 11*y^2 + 4*x + 63*y + 57
        sage: q2 = 61*x^2 - 100*x*y - 72*y^2 - 81*x + 39*y - 7
        sage: biquadratic = invariant_theory.ternary_biquadratic(q1, q2, [x,y]).homogenized()
        sage: biquadratic._check_covariant(\'Delta_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Delta_prime_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Theta_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Theta_prime_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'F_covariant\')
        sage: biquadratic._check_covariant(\'J_covariant\')
    '''
    def Delta_invariant(self):
        """
        Return the `\\Delta` invariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, y0, y1, y2, t> = QQ[]
            sage: p1 = a00*y0^2 + 2*a01*y0*y1 + a11*y1^2 + 2*a02*y0*y2 + 2*a12*y1*y2 + a22*y2^2
            sage: p2 = b00*y0^2 + 2*b01*y0*y1 + b11*y1^2 + 2*b02*y0*y2 + 2*b12*y1*y2 + b22*y2^2
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [y0, y1, y2])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Delta_invariant() == coeffs[3]
            True
        """
    def Delta_prime_invariant(self):
        """
        Return the `\\Delta'` invariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, y0, y1, y2, t> = QQ[]
            sage: p1 = a00*y0^2 + 2*a01*y0*y1 + a11*y1^2 + 2*a02*y0*y2 + 2*a12*y1*y2 + a22*y2^2
            sage: p2 = b00*y0^2 + 2*b01*y0*y1 + b11*y1^2 + 2*b02*y0*y2 + 2*b12*y1*y2 + b22*y2^2
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [y0, y1, y2])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Delta_prime_invariant() == coeffs[0]
            True
        """
    def Theta_invariant(self):
        """
        Return the `\\Theta` invariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, y0, y1, y2, t> = QQ[]
            sage: p1 = a00*y0^2 + 2*a01*y0*y1 + a11*y1^2 + 2*a02*y0*y2 + 2*a12*y1*y2 + a22*y2^2
            sage: p2 = b00*y0^2 + 2*b01*y0*y1 + b11*y1^2 + 2*b02*y0*y2 + 2*b12*y1*y2 + b22*y2^2
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [y0, y1, y2])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Theta_invariant() == coeffs[2]
            True
        """
    def Theta_prime_invariant(self):
        """
        Return the `\\Theta'` invariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, y0, y1, y2, t> = QQ[]
            sage: p1 = a00*y0^2 + 2*a01*y0*y1 + a11*y1^2 + 2*a02*y0*y2 + 2*a12*y1*y2 + a22*y2^2
            sage: p2 = b00*y0^2 + 2*b01*y0*y1 + b11*y1^2 + 2*b02*y0*y2 + 2*b12*y1*y2 + b22*y2^2
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [y0, y1, y2])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Theta_prime_invariant() == coeffs[1]
            True
        """
    def F_covariant(self):
        """
        Return the `F` covariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, x, y> = QQ[]
            sage: p1 = 73*x^2 + 96*x*y - 11*y^2 + 4*x + 63*y + 57
            sage: p2 = 61*x^2 - 100*x*y - 72*y^2 - 81*x + 39*y - 7
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [x, y])
            sage: q.F_covariant()
            -32566577*x^2 + 29060637/2*x*y + 20153633/4*y^2 -
            30250497/2*x - 241241273/4*y - 323820473/16
        """
    def J_covariant(self):
        """
        Return the `J` covariant.

        EXAMPLES::

            sage: R.<a00, a01, a11, a02, a12, a22, b00, b01, b11, b02, b12, b22, x, y> = QQ[]
            sage: p1 = 73*x^2 + 96*x*y - 11*y^2 + 4*x + 63*y + 57
            sage: p2 = 61*x^2 - 100*x*y - 72*y^2 - 81*x + 39*y - 7
            sage: q = invariant_theory.ternary_biquadratic(p1, p2, [x, y])
            sage: q.J_covariant()
            1057324024445*x^3 + 1209531088209*x^2*y + 942116599708*x*y^2 +
            984553030871*y^3 + 543715345505/2*x^2 - 3065093506021/2*x*y +
            755263948570*y^2 - 1118430692650*x - 509948695327/4*y + 3369951531745/8
        """
    def syzygy(self, Delta, Theta, Theta_prime, Delta_prime, S, S_prime, F, J):
        """
        Return the syzygy evaluated on the invariants and covariants.

        INPUT:

        - ``Delta``, ``Theta``, ``Theta_prime``, ``Delta_prime``,
          ``S``, ``S_prime``, ``F``, ``J`` -- polynomials from the
          same polynomial ring.

        OUTPUT:

        Zero if ``S`` is the first polynomial, ``S_prime`` the
        second polynomial, and the remaining input are the invariants
        and covariants of a ternary biquadratic.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: monomials = [x^2, x*y, y^2, x*z, y*z, z^2]
            sage: def q_rnd():  return sum(randint(-1000, 1000)*m for m in monomials)
            sage: biquadratic = invariant_theory.ternary_biquadratic(q_rnd(), q_rnd(), [x,y,z])
            sage: Delta = biquadratic.Delta_invariant()
            sage: Theta = biquadratic.Theta_invariant()
            sage: Theta_prime = biquadratic.Theta_prime_invariant()
            sage: Delta_prime = biquadratic.Delta_prime_invariant()
            sage: S = biquadratic.first().polynomial()
            sage: S_prime  = biquadratic.second().polynomial()
            sage: F = biquadratic.F_covariant()
            sage: J = biquadratic.J_covariant()
            sage: biquadratic.syzygy(Delta, Theta, Theta_prime, Delta_prime, S, S_prime, F, J)
            0

        If the arguments are not the invariants and covariants then
        the output is some (generically nonzero) polynomial::

            sage: biquadratic.syzygy(1, 1, 1, 1, 1, 1, 1, x)
            1/64*x^2 + 1
        """

class TwoQuaternaryQuadratics(TwoAlgebraicForms):
    '''
    Invariant theory of two quaternary quadratics.

    You should use the :class:`invariant_theory
    <InvariantTheoryFactory>` factory object to construct instances
    of this class. See
    :meth:`~InvariantTheoryFactory.quaternary_biquadratics` for
    details.

    REFERENCES:

    - section on "Invariants and Covariants of
      Systems of Quadrics" in [Sal1958]_, [Sal1965]_

    TESTS::

        sage: R.<w,x,y,z> = QQ[]
        sage: inv = invariant_theory.quaternary_biquadratic(w^2 + x^2, y^2 + z^2, w, x, y, z)
        sage: inv
        Joint quaternary quadratic with coefficients (1, 1, 0, 0, 0, 0, 0, 0, 0, 0) and
        quaternary quadratic with coefficients (0, 0, 1, 1, 0, 0, 0, 0, 0, 0)
        sage: TestSuite(inv).run()

        sage: q1 = 73*x^2 + 96*x*y - 11*y^2 - 74*x*z - 10*y*z + 66*z^2 + 4*x + 63*y - 11*z + 57
        sage: q2 = 61*x^2 - 100*x*y - 72*y^2 - 38*x*z + 85*y*z + 95*z^2 - 81*x + 39*y + 23*z - 7
        sage: biquadratic = invariant_theory.quaternary_biquadratic(q1, q2, [x,y,z]).homogenized()
        sage: biquadratic._check_covariant(\'Delta_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Delta_prime_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Theta_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Theta_prime_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'Phi_invariant\', invariant=True)
        sage: biquadratic._check_covariant(\'T_covariant\')
        sage: biquadratic._check_covariant(\'T_prime_covariant\')
        sage: biquadratic._check_covariant(\'J_covariant\')
    '''
    def Delta_invariant(self):
        """
        Return the `\\Delta` invariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Delta_invariant() == coeffs[4]
            True
        """
    def Delta_prime_invariant(self):
        """
        Return the `\\Delta'` invariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Delta_prime_invariant() == coeffs[0]
            True
        """
    def Theta_invariant(self):
        """
        Return the `\\Theta` invariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Theta_invariant() == coeffs[3]
            True
        """
    def Theta_prime_invariant(self):
        """
        Return the `\\Theta'` invariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Theta_prime_invariant() == coeffs[1]
            True
        """
    def Phi_invariant(self):
        """
        Return the `\\Phi'` invariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: coeffs = det(t * q[0].matrix() + q[1].matrix()).polynomial(t).coefficients(sparse=False)
            sage: q.Phi_invariant() == coeffs[2]
            True
        """
    def T_covariant(self):
        """
        The `T`-covariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: T = invariant_theory.quaternary_quadratic(q.T_covariant(), [x,y,z]).matrix()
            sage: M = q[0].matrix().adjugate() + t*q[1].matrix().adjugate()
            sage: M = M.adjugate().apply_map(             # long time (4s on my thinkpad W530)
            ....:         lambda m: m.coefficient(t))
            sage: M == q.Delta_invariant()*T             # long time
            True
        """
    def T_prime_covariant(self):
        """
        The `T'`-covariant.

        EXAMPLES::

            sage: R.<x,y,z,t,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5,A0,A1,A2,A3,B0,B1,B2,B3,B4,B5> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3
            sage: p1 += b0*x*y + b1*x*z + b2*x + b3*y*z + b4*y + b5*z
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3
            sage: p2 += B0*x*y + B1*x*z + B2*x + B3*y*z + B4*y + B5*z
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [x, y, z])
            sage: Tprime = invariant_theory.quaternary_quadratic(
            ....:     q.T_prime_covariant(), [x,y,z]).matrix()
            sage: M = q[0].matrix().adjugate() + t*q[1].matrix().adjugate()
            sage: M = M.adjugate().apply_map(                # long time (4s on my thinkpad W530)
            ....:         lambda m: m.coefficient(t^2))
            sage: M == q.Delta_prime_invariant() * Tprime   # long time
            True
        """
    def J_covariant(self):
        """
        The `J`-covariant.

        This is the Jacobian determinant of the two biquadratics, the
        `T`-covariant, and the `T'`-covariant with respect to the four
        homogeneous variables.

        EXAMPLES::

            sage: R.<w,x,y,z,a0,a1,a2,a3,A0,A1,A2,A3> = QQ[]
            sage: p1 = a0*x^2 + a1*y^2 + a2*z^2 + a3*w^2
            sage: p2 = A0*x^2 + A1*y^2 + A2*z^2 + A3*w^2
            sage: q = invariant_theory.quaternary_biquadratic(p1, p2, [w, x, y, z])
            sage: q.J_covariant().factor()
            z * y * x * w * (-a1*A0 + a0*A1) * (-a2*A0 + a0*A2) * (-a2*A1 + a1*A2)
            * (a3*A2 - a2*A3) * (a3*A1 - a1*A3) * (a3*A0 - a0*A3)
        """
    def syzygy(self, Delta, Theta, Phi, Theta_prime, Delta_prime, U, V, T, T_prime, J):
        """
        Return the syzygy evaluated on the invariants and covariants.

        INPUT:

        - ``Delta``, ``Theta``, ``Phi``, ``Theta_prime``,
          ``Delta_prime``, ``U``, ``V``, ``T``, ``T_prime``, ``J`` --
          polynomials from the same polynomial ring.

        OUTPUT:

        Zero if the ``U`` is the first polynomial, ``V`` the second
        polynomial, and the remaining input are the invariants and
        covariants of a quaternary biquadratic.

        EXAMPLES::

            sage: R.<w,x,y,z> = QQ[]
            sage: monomials = [x^2, x*y, y^2, x*z, y*z, z^2, x*w, y*w, z*w, w^2]
            sage: def q_rnd():  return sum(randint(-1000, 1000)*m for m in monomials)
            sage: biquadratic = invariant_theory.quaternary_biquadratic(q_rnd(), q_rnd())
            sage: Delta = biquadratic.Delta_invariant()
            sage: Theta = biquadratic.Theta_invariant()
            sage: Phi = biquadratic.Phi_invariant()
            sage: Theta_prime = biquadratic.Theta_prime_invariant()
            sage: Delta_prime = biquadratic.Delta_prime_invariant()
            sage: U = biquadratic.first().polynomial()
            sage: V  = biquadratic.second().polynomial()
            sage: T = biquadratic.T_covariant()
            sage: T_prime  = biquadratic.T_prime_covariant()
            sage: J = biquadratic.J_covariant()
            sage: biquadratic.syzygy(Delta, Theta, Phi, Theta_prime, Delta_prime, U, V, T, T_prime, J)
            0

        If the arguments are not the invariants and covariants then
        the output is some (generically nonzero) polynomial::

            sage: biquadratic.syzygy(1, 1, 1, 1, 1, 1, 1, 1, 1, x)
            -x^2 + 1
        """

class InvariantTheoryFactory:
    """
    Factory object for invariants of multilinear forms.

    Use the invariant_theory object to construct algebraic forms. These
    can then be queried for invariant and covariants.

    EXAMPLES::

        sage: R.<x,y,z> = QQ[]
        sage: invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
        Ternary cubic with coefficients (1, 1, 1, 0, 0, 0, 0, 0, 0, 0)

        sage: invariant_theory.ternary_cubic(x^3 + y^3 + z^3).J_covariant()
        x^6*y^3 - x^3*y^6 - x^6*z^3 + y^6*z^3 + x^3*z^6 - y^3*z^6
    """
    def quadratic_form(self, polynomial, *args):
        """
        Invariants of a homogeneous quadratic form.

        INPUT:

        - ``polynomial`` -- a homogeneous or inhomogeneous quadratic form

        - ``*args`` -- the variables as multiple arguments, or as a
          single list/tuple. If the last argument is ``None``, the
          cubic is assumed to be inhomogeneous.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: quadratic = x^2 + y^2 + z^2
            sage: inv = invariant_theory.quadratic_form(quadratic)
            sage: type(inv)
            <class 'sage.rings.invariants.invariant_theory.TernaryQuadratic'>

        If some of the ring variables are to be treated as coefficients
        you need to specify the polynomial variables::

            sage: R.<x,y,z, a,b> = QQ[]
            sage: quadratic = a*x^2 + b*y^2 + z^2 + 2*y*z
            sage: invariant_theory.quadratic_form(quadratic, x,y,z)
            Ternary quadratic with coefficients (a, b, 1, 0, 0, 2)
            sage: invariant_theory.quadratic_form(quadratic, [x,y,z])   # alternate syntax
            Ternary quadratic with coefficients (a, b, 1, 0, 0, 2)

        Inhomogeneous quadratic forms (see also
        :meth:`inhomogeneous_quadratic_form`) can be specified by
        passing ``None`` as the last variable::

            sage: inhom = quadratic.subs(z=1)
            sage: invariant_theory.quadratic_form(inhom, x,y,None)
            Ternary quadratic with coefficients (a, b, 1, 0, 0, 2)
        """
    def inhomogeneous_quadratic_form(self, polynomial, *args):
        """
        Invariants of an inhomogeneous quadratic form.

        INPUT:

        - ``polynomial`` -- an inhomogeneous quadratic form

        - ``*args`` -- the variables as multiple arguments, or as a
          single list/tuple

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: quadratic = x^2 + 2*y^2 + 3*x*y + 4*x + 5*y + 6
            sage: inv3 = invariant_theory.inhomogeneous_quadratic_form(quadratic)
            sage: type(inv3)
            <class 'sage.rings.invariants.invariant_theory.TernaryQuadratic'>
            sage: inv4 = invariant_theory.inhomogeneous_quadratic_form(x^2 + y^2 + z^2)
            sage: type(inv4)
            <class 'sage.rings.invariants.invariant_theory.QuadraticForm'>
        """
    def binary_quadratic(self, quadratic, *args):
        """
        Invariant theory of a quadratic in two variables.

        INPUT:

        - ``quadratic`` -- a quadratic form

        - ``x``, ``y`` -- the homogeneous variables. If ``y`` is
          ``None``, the quadratic is assumed to be inhomogeneous.

        REFERENCES:

        - :wikipedia:`Invariant_of_a_binary_form`

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: invariant_theory.binary_quadratic(x^2 + y^2)
            Binary quadratic with coefficients (1, 1, 0)

            sage: T.<t> = QQ[]
            sage: invariant_theory.binary_quadratic(t^2 + 2*t + 1, [t])
            Binary quadratic with coefficients (1, 1, 2)
        """
    def quaternary_quadratic(self, quadratic, *args):
        """
        Invariant theory of a quadratic in four variables.

        INPUT:

        - ``quadratic`` -- a quadratic form

        - ``w``, ``x``, ``y``, ``z`` -- the homogeneous variables. If
          ``z`` is ``None``, the quadratic is assumed to be inhomogeneous.

        REFERENCES:

        - :wikipedia:`Invariant_of_a_binary_form`

        EXAMPLES::

            sage: R.<w,x,y,z> = QQ[]
            sage: invariant_theory.quaternary_quadratic(w^2 + x^2 + y^2 + z^2)
            Quaternary quadratic with coefficients (1, 1, 1, 1, 0, 0, 0, 0, 0, 0)

            sage: R.<x,y,z> = QQ[]
            sage: invariant_theory.quaternary_quadratic(1 + x^2 + y^2 + z^2)
            Quaternary quadratic with coefficients (1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
        """
    def binary_quartic(self, quartic, *args, **kwds):
        """
        Invariant theory of a quartic in two variables.

        The algebra of invariants of a quartic form is generated by
        invariants `i`, `j` of degrees 2, 3.  This ring is naturally
        isomorphic to the ring of modular forms of level 1, with the
        two generators corresponding to the Eisenstein series `E_4`
        (see
        :meth:`~sage.rings.invariants.invariant_theory.BinaryQuartic.EisensteinD`)
        and `E_6` (see
        :meth:`~sage.rings.invariants.invariant_theory.BinaryQuartic.EisensteinE`). The
        algebra of covariants is generated by these two invariants
        together with the form `f` of degree 1 and order 4, the
        Hessian `g` (see :meth:`~BinaryQuartic.g_covariant`) of degree
        2 and order 4, and a covariant `h` (see
        :meth:`~BinaryQuartic.h_covariant`) of degree 3 and order
        6. They are related by a syzygy

        .. MATH::

            j f^3 - g f^2 i + 4 g^3 + h^2 = 0

        of degree 6 and order 12.

        INPUT:

        - ``quartic`` -- a quartic

        - ``x``, ``y`` -- the homogeneous variables. If ``y`` is
          ``None``, the quartic is assumed to be inhomogeneous.

        REFERENCES:

        - :wikipedia:`Invariant_of_a_binary_form`

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: quartic = invariant_theory.binary_quartic(x^4 + y^4)
            sage: quartic
            Binary quartic with coefficients (1, 0, 0, 0, 1)
            sage: type(quartic)
            <class 'sage.rings.invariants.invariant_theory.BinaryQuartic'>
        """
    def binary_quintic(self, quintic, *args, **kwds):
        """
        Create a binary quintic for computing invariants.

        A binary quintic is a homogeneous polynomial of degree 5 in two
        variables. The algebra of invariants of a binary quintic is generated
        by the invariants `A`, `B` and `C` of respective degrees 4, 8 and 12
        (see :meth:`~BinaryQuintic.A_invariant`,
        :meth:`~BinaryQuintic.B_invariant` and
        :meth:`~BinaryQuintic.C_invariant`).

        INPUT:

        - ``quintic`` -- a homogeneous polynomial of degree five in two
          variables or a (possibly inhomogeneous) polynomial of degree at most
          five in one variable.

        - ``*args`` -- the two homogeneous variables. If only one variable is
          given, the polynomial ``quintic`` is assumed to be univariate. If
          no variables are given, they are guessed.

        REFERENCES:

        - :wikipedia:`Invariant_of_a_binary_form`
        - [Cle1872]_

        EXAMPLES:

        If no variables are provided, they will be guessed::

            sage: R.<x,y> = QQ[]
            sage: quintic = invariant_theory.binary_quintic(x^5 + y^5)
            sage: quintic
            Binary quintic with coefficients (1, 0, 0, 0, 0, 1)

        If only one variable is given, the quintic is the homogenisation of
        the provided polynomial::

            sage: quintic = invariant_theory.binary_quintic(x^5 + y^5, x)
            sage: quintic
            Binary quintic with coefficients (y^5, 0, 0, 0, 0, 1)
            sage: quintic.is_homogeneous()
            False

        If the polynomial has three or more variables, the variables should be
        specified::

            sage: R.<x,y,z> = QQ[]
            sage: quintic = invariant_theory.binary_quintic(x^5 + z*y^5)
            Traceback (most recent call last):
            ...
            ValueError: need 2 or 1 variables, got (x, y, z)
            sage: quintic = invariant_theory.binary_quintic(x^5 + z*y^5, x, y)
            sage: quintic
            Binary quintic with coefficients (z, 0, 0, 0, 0, 1)

            sage: type(quintic)
            <class 'sage.rings.invariants.invariant_theory.BinaryQuintic'>
        """
    def binary_form_from_invariants(self, degree, invariants, variables=None, as_form: bool = True, *args, **kwargs):
        """
        Reconstruct a binary form from the values of its invariants.

        INPUT:

        - ``degree`` -- the degree of the binary form

        - ``invariants`` -- list or tuple of values of the invariants of the
          binary form

        - ``variables`` -- list or tuple of two variables that are used for
          the resulting form (only if ``as_form`` is ``True``). If no variables
          are provided, two abstract variables ``x`` and ``z`` will be used.

        - ``as_form`` -- boolean; if ``False``, the function will return a tuple
          of coefficients of a binary form

        OUTPUT:

        A binary form or a tuple of its coefficients, whose invariants are equal
        to the given ``invariants`` up to a scaling.

        EXAMPLES:

        In the case of binary quadratics and cubics, the form is reconstructed
        based on the value of the discriminant. See also
        :meth:`binary_quadratic_coefficients_from_invariants` and
        :meth:`binary_cubic_coefficients_from_invariants`. These methods will always return the
        same result if the discriminant is nonzero::

            sage: discriminant = 1
            sage: invariant_theory.binary_form_from_invariants(2, [discriminant])
            Binary quadratic with coefficients (1, -1/4, 0)
            sage: invariant_theory.binary_form_from_invariants(3, [discriminant], as_form=false)
            (0, 1, -1, 0)

        For binary cubics, there is no class implemented yet, so ``as_form=True``
        will yield a :exc:`NotImplementedError`::

            sage: invariant_theory.binary_form_from_invariants(3, [discriminant])
            Traceback (most recent call last):
            ...
            NotImplementedError: no class for binary cubics implemented

        For binary quintics, the three Clebsch invariants of the form should be
        provided to reconstruct the form. For more details about these invariants,
        see :meth:`~sage.rings.invariants.invariant_theory.BinaryQuintic.clebsch_invariants`::

            sage: invariants = [1, 0, 0]
            sage: invariant_theory.binary_form_from_invariants(5, invariants)
            Binary quintic with coefficients (1, 0, 0, 0, 0, 1)

        An optional ``scaling`` argument may be provided in order to scale the
        resulting quintic. For more details, see :meth:`binary_quintic_coefficients_from_invariants`::

            sage: invariants = [3, 4, 7]
            sage: invariant_theory.binary_form_from_invariants(5, invariants)
            Binary quintic with coefficients (-37725479487783/1048576,
            565882192316745/8388608, 0, 1033866765362693115/67108864,
            12849486940936328715/268435456, -23129076493685391687/2147483648)
            sage: invariant_theory.binary_form_from_invariants(5, invariants,
            ....:                                              scaling='normalized')
            Binary quintic with coefficients (24389/892616806656,
            4205/11019960576, 0, 1015/209952, -145/1296, -3/16)
            sage: invariant_theory.binary_form_from_invariants(5, invariants,
            ....:                                                 scaling='coprime')
            Binary quintic with coefficients (-2048, 3840, 0, 876960, 2724840, -613089)

        The invariants can also be computed using the invariants of a given binary
        quintic. The resulting form has the same invariants up to scaling, is
        `GL(2,\\QQ)`-equivalent to the provided form and hence has the same
        canonical form (see
        :meth:`~sage.rings.invariants.invariant_theory.BinaryQuintic.canonical_form`)::

            sage: R.<x0, x1> = QQ[]
            sage: p = 3*x1^5 + 6*x1^4*x0 + 3*x1^3*x0^2 + 4*x1^2*x0^3 - 5*x1*x0^4 + 4*x0^5
            sage: quintic = invariant_theory.binary_quintic(p, x0, x1)
            sage: invariants = quintic.clebsch_invariants(as_tuple=True)
            sage: newquintic = invariant_theory.binary_form_from_invariants(
            ....:                  5, invariants, variables=quintic.variables())
            sage: newquintic
            Binary quintic with coefficients (9592267437341790539005557/244140625000000,
            2149296928207625556323004064707/610351562500000000,
            11149651890347700974453304786783/76293945312500000,
            122650775751894638395648891202734239/47683715820312500000,
            323996630945706528474286334593218447/11920928955078125000,
            1504506503644608395841632538558481466127/14901161193847656250000)
            sage: quintic.canonical_form() == newquintic.canonical_form()
            True

        For binary forms of other degrees, no reconstruction has been
        implemented yet. For forms of degree 6, see :issue:`26462`::

            sage: invariant_theory.binary_form_from_invariants(6, invariants)
            Traceback (most recent call last):
            ...
            NotImplementedError: no reconstruction for binary forms of degree 6 implemented

        TESTS::

            sage: invariant_theory.binary_form_from_invariants(2, [1,2])
            Traceback (most recent call last):
            ...
            ValueError: incorrect number of invariants provided, only one invariant should be provided
            sage: invariant_theory.binary_form_from_invariants(2, [1], invariant_choice='unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown choice of invariants unknown for a binary quadratic
            sage: invariant_theory.binary_form_from_invariants(3, [1,2])
            Traceback (most recent call last):
            ...
            ValueError: incorrect number of invariants provided, only one invariant should be provided
            sage: invariant_theory.binary_form_from_invariants(3, [1], as_form=false, invariant_choice='unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown choice of invariants unknown for a binary cubic
            sage: invariant_theory.binary_form_from_invariants(5, [1,2,3], invariant_choice='unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown choice of invariants unknown for a binary quintic
            sage: invariant_theory.binary_form_from_invariants(42, invariants)
            Traceback (most recent call last):
            ...
            NotImplementedError: no reconstruction for binary forms of degree 42 implemented
        """
    def ternary_quadratic(self, quadratic, *args, **kwds):
        """
        Invariants of a quadratic in three variables.

        INPUT:

        - ``quadratic`` -- a homogeneous quadratic in 3 homogeneous
          variables, or an inhomogeneous quadratic in 2 variables

        - ``x``, ``y``, ``z`` -- the variables. If ``z`` is ``None``,
          the quadratic is assumed to be inhomogeneous.

        REFERENCES:

        - :wikipedia:`Invariant_of_a_binary_form`

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: invariant_theory.ternary_quadratic(x^2 + y^2 + z^2)
            Ternary quadratic with coefficients (1, 1, 1, 0, 0, 0)

            sage: T.<u, v> = QQ[]
            sage: invariant_theory.ternary_quadratic(1 + u^2 + v^2)
            Ternary quadratic with coefficients (1, 1, 1, 0, 0, 0)

            sage: quadratic = x^2 + y^2 + z^2
            sage: inv = invariant_theory.ternary_quadratic(quadratic)
            sage: type(inv)
            <class 'sage.rings.invariants.invariant_theory.TernaryQuadratic'>
        """
    def ternary_cubic(self, cubic, *args, **kwds):
        """
        Invariants of a cubic in three variables.

        The algebra of invariants of a ternary cubic under `SL_3(\\CC)`
        is a polynomial algebra generated by two invariants `S` (see
        :meth:`~sage.rings.invariants.invariant_theory.TernaryCubic.S_invariant`)
        and T (see
        :meth:`~sage.rings.invariants.invariant_theory.TernaryCubic.T_invariant`)
        of degrees 4 and 6, called Aronhold invariants.

        The ring of covariants is given as follows. The identity
        covariant U of a ternary cubic has degree 1 and order 3.  The
        Hessian `H` (see
        :meth:`~sage.rings.invariants.invariant_theory.TernaryCubic.Hessian`)
        is a covariant of ternary cubics of degree 3 and order 3.
        There is a covariant `\\Theta` (see
        :meth:`~sage.rings.invariants.invariant_theory.TernaryCubic.Theta_covariant`)
        of ternary cubics of degree 8 and order 6 that vanishes on
        points `x` lying on the Salmon conic of the polar of `x` with
        respect to the curve and its Hessian curve. The Brioschi
        covariant `J` (see
        :meth:`~sage.rings.invariants.invariant_theory.TernaryCubic.J_covariant`)
        is the Jacobian of `U`, `\\Theta`, and `H` of degree 12, order
        9.  The algebra of covariants of a ternary cubic is generated
        over the ring of invariants by `U`, `\\Theta`, `H`, and `J`,
        with a relation

        .. MATH::

            \\begin{split}
              J^2 =& 4 \\Theta^3 + T U^2 \\Theta^2 +
              \\Theta (-4 S^3 U^4 + 2 S T U^3 H
              - 72 S^2 U^2 H^2
              \\\\ &
              - 18 T U H^3 +  108 S H^4)
              -16 S^4 U^5 H - 11 S^2 T U^4 H^2
              \\\\ &
              -4 T^2 U^3 H^3
              +54 S T U^2 H^4 -432 S^2 U H^5 -27 T H^6
            \\end{split}


        REFERENCES:

        - :wikipedia:`Ternary_cubic`

        INPUT:

        - ``cubic`` -- a homogeneous cubic in 3 homogeneous variables,
          or an inhomogeneous cubic in 2 variables

        - ``x``, ``y``, ``z`` -- the variables. If ``z`` is ``None``, the
          cubic is assumed to be inhomogeneous.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: cubic = invariant_theory.ternary_cubic(x^3 + y^3 + z^3)
            sage: type(cubic)
            <class 'sage.rings.invariants.invariant_theory.TernaryCubic'>
        """
    def ternary_biquadratic(self, quadratic1, quadratic2, *args, **kwds):
        """
        Invariants of two quadratics in three variables.

        INPUT:

        - ``quadratic1``, ``quadratic2`` -- two polynomials. Either
          homogeneous quadratic in 3 homogeneous variables, or
          inhomogeneous quadratic in 2 variables.

        - ``x``, ``y``, ``z`` -- the variables. If ``z`` is ``None``,
          the quadratics are assumed to be inhomogeneous.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: q1 = x^2 + y^2 + z^2
            sage: q2 = x*y + y*z + x*z
            sage: inv = invariant_theory.ternary_biquadratic(q1, q2)
            sage: type(inv)
            <class 'sage.rings.invariants.invariant_theory.TwoTernaryQuadratics'>

        Distance between two circles::

            sage: R.<x,y, a,b, r1,r2> = QQ[]
            sage: S1 = -r1^2 + x^2 + y^2
            sage: S2 = -r2^2 + (x-a)^2 + (y-b)^2
            sage: inv = invariant_theory.ternary_biquadratic(S1, S2, [x, y])
            sage: inv.Delta_invariant()
            -r1^2
            sage: inv.Delta_prime_invariant()
            -r2^2
            sage: inv.Theta_invariant()
            a^2 + b^2 - 2*r1^2 - r2^2
            sage: inv.Theta_prime_invariant()
            a^2 + b^2 - r1^2 - 2*r2^2
            sage: inv.F_covariant()
            2*x^2*a^2 + y^2*a^2 - 2*x*a^3 + a^4 + 2*x*y*a*b - 2*y*a^2*b + x^2*b^2 +
            2*y^2*b^2 - 2*x*a*b^2 + 2*a^2*b^2 - 2*y*b^3 + b^4 - 2*x^2*r1^2 - 2*y^2*r1^2 +
            2*x*a*r1^2 - 2*a^2*r1^2 + 2*y*b*r1^2 - 2*b^2*r1^2 + r1^4 - 2*x^2*r2^2 -
            2*y^2*r2^2 + 2*x*a*r2^2 - 2*a^2*r2^2 + 2*y*b*r2^2 - 2*b^2*r2^2 + 2*r1^2*r2^2 +
            r2^4
            sage: inv.J_covariant()
            -8*x^2*y*a^3 + 8*x*y*a^4 + 8*x^3*a^2*b - 16*x*y^2*a^2*b - 8*x^2*a^3*b +
            8*y^2*a^3*b + 16*x^2*y*a*b^2 - 8*y^3*a*b^2 + 8*x*y^2*b^3 - 8*x^2*a*b^3 +
            8*y^2*a*b^3 - 8*x*y*b^4 + 8*x*y*a^2*r1^2 - 8*y*a^3*r1^2 - 8*x^2*a*b*r1^2 +
            8*y^2*a*b*r1^2 + 8*x*a^2*b*r1^2 - 8*x*y*b^2*r1^2 - 8*y*a*b^2*r1^2 + 8*x*b^3*r1^2 -
            8*x*y*a^2*r2^2 + 8*x^2*a*b*r2^2 - 8*y^2*a*b*r2^2 + 8*x*y*b^2*r2^2
        """
    def quaternary_biquadratic(self, quadratic1, quadratic2, *args, **kwds):
        """
        Invariants of two quadratics in four variables.

        INPUT:

        - ``quadratic1``, ``quadratic2`` -- two polynomials.
          Either homogeneous quadratic
          in 4 homogeneous variables, or inhomogeneous quadratic
          in 3 variables.

        - ``w``, ``x``, ``y``, ``z`` -- the variables. If ``z`` is
          ``None``, the quadratics are assumed to be inhomogeneous.

        EXAMPLES::

            sage: R.<w,x,y,z> = QQ[]
            sage: q1 = w^2 + x^2 + y^2 + z^2
            sage: q2 = w*x + y*z
            sage: inv = invariant_theory.quaternary_biquadratic(q1, q2)
            sage: type(inv)
            <class 'sage.rings.invariants.invariant_theory.TwoQuaternaryQuadratics'>

        Distance between two spheres [Sal1958]_, [Sal1965]_ ::

            sage: R.<x,y,z, a,b,c, r1,r2> = QQ[]
            sage: S1 = -r1^2 + x^2 + y^2 + z^2
            sage: S2 = -r2^2 + (x-a)^2 + (y-b)^2 + (z-c)^2
            sage: inv = invariant_theory.quaternary_biquadratic(S1, S2, [x, y, z])
            sage: inv.Delta_invariant()
            -r1^2
            sage: inv.Delta_prime_invariant()
            -r2^2
            sage: inv.Theta_invariant()
            a^2 + b^2 + c^2 - 3*r1^2 - r2^2
            sage: inv.Theta_prime_invariant()
            a^2 + b^2 + c^2 - r1^2 - 3*r2^2
            sage: inv.Phi_invariant()
            2*a^2 + 2*b^2 + 2*c^2 - 3*r1^2 - 3*r2^2
            sage: inv.J_covariant()
            0
        """

invariant_theory: Incomplete
