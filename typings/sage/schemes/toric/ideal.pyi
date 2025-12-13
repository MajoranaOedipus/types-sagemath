from sage.matrix.constructor import matrix as matrix
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal as MPolynomialIdeal
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

class ToricIdeal(MPolynomialIdeal):
    """
    This class represents a toric ideal defined by an integral matrix.

    INPUT:

    - ``A`` -- integer matrix; the defining matrix of the toric ideal

    - ``names`` -- string (optional); names for the variables. By
      default, this is ``'z'`` and the variables will be named ``z0``,
      ``z1``, ...

    - ``base_ring`` -- a ring (default: `\\QQ`); the base
      ring of the ideal. A toric ideal uses only coefficients `\\pm 1`.

    - ``polynomial_ring`` -- a polynomial ring (optional); the
      polynomial ring to construct the ideal in

      You may specify the ambient polynomial ring via the
      ``polynomial_ring`` parameter or via the ``names`` and
      ``base_ring`` parameter. A :exc:`ValueError` is raised if you
      specify both.

    - ``algorithm`` -- string (optional); the algorithm to use. For
      now, must be ``'HostenSturmfels'`` which is the algorithm
      proposed by Hosten and Sturmfels in [SH1995b]_.

    EXAMPLES::

        sage: A = matrix([[1,1,1], [0,1,2]])
        sage: ToricIdeal(A)
        Ideal (-z1^2 + z0*z2) of Multivariate Polynomial Ring
        in z0, z1, z2 over Rational Field

    First way of specifying the polynomial ring::

        sage: ToricIdeal(A, names='x,y,z', base_ring=ZZ)
        Ideal (-y^2 + x*z) of Multivariate Polynomial Ring
        in x, y, z over Integer Ring

    Second way of specifying the polynomial ring::

        sage: R.<x,y,z> = ZZ[]
        sage: ToricIdeal(A, polynomial_ring=R)
        Ideal (-y^2 + x*z) of Multivariate Polynomial Ring
        in x, y, z over Integer Ring

    It is an error to specify both::

        sage: ToricIdeal(A, names='x,y,z', polynomial_ring=R)
        Traceback (most recent call last):
        ...
        ValueError: you must not specify both variable names and a polynomial ring
    """
    def __init__(self, A, names: str = 'z', base_ring=..., polynomial_ring=None, algorithm: str = 'HostenSturmfels') -> None:
        """
        Create an ideal and a multivariate polynomial ring containing it.

        See the :mod:`module documentation
        <sage.schemes.toric.ideal>` for an introduction to
        toric ideals.

        INPUT:

        See the :class:`class-level documentation <ToricIdeal>` for
        input values.

        EXAMPLES::

            sage: A = matrix([[1,1,1], [0,1,2]])
            sage: ToricIdeal(A)
            Ideal (-z1^2 + z0*z2) of Multivariate Polynomial Ring
            in z0, z1, z2 over Rational Field
            sage: ToricIdeal(A, names='x', base_ring=GF(101))
            Ideal (-x1^2 + x0*x2) of Multivariate Polynomial Ring
            in x0, x1, x2 over Finite Field of size 101
            sage: ToricIdeal(A, names='x', base_ring=FractionField(QQ['t']))
            Ideal (-x1^2 + x0*x2) of
            Multivariate Polynomial Ring in x0, x1, x2 over
             Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def A(self):
        """
        Return the defining matrix.

        OUTPUT: integer matrix

        EXAMPLES::

            sage: A = matrix([[1,1,1], [0,1,2]])
            sage: IA = ToricIdeal(A)
            sage: IA.A()
            [1 1 1]
            [0 1 2]
        """
    def ker(self):
        """
        Return the kernel of the defining matrix.

        OUTPUT: the kernel of ``self.A()``.

        EXAMPLES::

            sage: A = matrix([[1,1,1], [0,1,2]])
            sage: IA = ToricIdeal(A)
            sage: IA.ker()
            Free module of degree 3 and rank 1 over Integer Ring
             User basis matrix: [-1  2 -1]
        """
    def nvariables(self):
        """
        Return the number of variables of the ambient polynomial ring.

        OUTPUT: integer; the number of columns of the defining matrix :meth:`A`

        EXAMPLES::

            sage: A = matrix([[1,1,1], [0,1,2]])
            sage: IA = ToricIdeal(A)
            sage: IA.nvariables()
            3
        """
