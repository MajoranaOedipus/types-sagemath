from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.sage_object import SageObject as SageObject

class Triangle(SageObject):
    """
    Common class for different kinds of triangles.

    This serves as a base class for F-triangles, H-triangles, M-triangles
    and Gamma-triangles.

    The user should use these subclasses directly.

    The input is a polynomial in two variables. One can also give a
    polynomial with more variables and specify two chosen variables.

    EXAMPLES::

        sage: from sage.combinat.triangles_FHM import Triangle
        sage: x, y = polygens(ZZ, 'x,y')
        sage: ht = Triangle(1+4*x+2*x*y)
        sage: unicode_art(ht)                                                           # needs sage.modules
        ⎛0 2⎞
        ⎝1 4⎠
    """
    def __init__(self, poly, variables=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import Triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: ht = Triangle(1+2*x*y)
            sage: unicode_art(ht)                                                       # needs sage.modules
            ⎛0 2⎞
            ⎝1 0⎠
        """
    def __eq__(self, other) -> bool:
        """
        Test for equality.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h1 = H_triangle(1+2*x*y)
            sage: h2 = H_triangle(1+3*x*y)
            sage: h1 == h1
            True
            sage: h1 == h2
            False
        """
    def __ne__(self, other) -> bool:
        """
        Test for unequality.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h1 = H_triangle(1+2*x*y)
            sage: h2 = H_triangle(1+3*x*y)
            sage: h1 != h1
            False
            sage: h1 != h2
            True
        """
    def __call__(self, *args):
        """
        Return the evaluation (as a polynomial).

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+3*x*y)
            sage: h(4,5)
            61
        """
    def __getitem__(self, *args):
        """
        Return some coefficient.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+2*x+3*x*y)
            sage: h[1,1]
            3
        """
    def __hash__(self) -> int:
        """
        Return the hash value.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+2*x*y)
            sage: g = H_triangle(1+2*x*y)
            sage: hash(h) == hash(g)
            True
        """
    def matrix(self):
        """
        Return the associated matrix for display.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+2*x*y)
            sage: h.matrix()                                                            # needs sage.modules
            [0 2]
            [1 0]
        """
    def polynomial(self):
        """
        Return the triangle as a bare polynomial.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+2*x*y)
            sage: h.polynomial()
            2*x*y + 1
        """
    def truncate(self, d):
        """
        Return the truncated triangle.

        INPUT:

        - ``d`` -- integer

        As a polynomial, this means that all monomials with a power
        of either `x` or `y` greater than or equal to ``d`` are dismissed.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: h = H_triangle(1+2*x*y)
            sage: h.truncate(2)
            H: 2*x*y + 1
        """
    def factor(self) -> list:
        """
        Return the decomposition of ``self`` as a product.

        This is defined by factoring the underlying polynomial.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import M_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: p = 3*x^3*y^3 - 7*x^2*y^3 + 5*x^2*y^2
            sage: p += 5*x*y^3 - 8*x*y^2 - y^3 + 3*x*y + 3*y^2 - 3*y + 1
            sage: m = M_triangle(p)
            sage: m.factor()
            [M: x*y - y + 1, M: 3*x^2*y^2 - 4*x*y^2 + 2*x*y + y^2 - 2*y + 1]
        """

class M_triangle(Triangle):
    """
    Class for the M-triangles.

    This is motivated by generating series of Möbius numbers of graded posets.

    EXAMPLES::

        sage: x, y = polygens(ZZ, 'x,y')
        sage: P = Poset({2: [1]})                                                       # needs sage.graphs
        sage: P.M_triangle()                                                            # needs sage.graphs
        M: x*y - y + 1
    """
    def dual(self) -> M_triangle:
        """
        Return the dual M-triangle.

        This is the M-triangle of the dual poset, hence an involution.

        When seen as a matrix, this performs a symmetry with respect to the
        northwest-southeast diagonal.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import  M_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: mt = M_triangle(x*y - y + 1)
            sage: mt.dual() == mt
            True
        """
    def transmute(self) -> M_triangle:
        """
        Return the image of ``self`` by an involution.

        OUTPUT: another M-triangle

        The involution is defined by converting to an H-triangle,
        transposing the matrix, and then converting back to an M-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import  M_triangle
            sage: x, y = polygens(ZZ, 'x,y')
            sage: nc3 = x^2*y^2 - 3*x*y^2 + 3*x*y + 2*y^2 - 3*y + 1
            sage: m = M_triangle(nc3)
            sage: m2 = m.transmute(); m2                                                # needs sage.libs.flint
            M: 2*x^2*y^2 - 3*x*y^2 + 2*x*y + y^2 - 2*y + 1
            sage: m2.transmute() == m                                                   # needs sage.libs.flint
            True
        """
    def h(self) -> H_triangle:
        """
        Return the associated H-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import M_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: M_triangle(1-y+x*y).h()
            H: x*y + 1

        TESTS::

            sage: h = polygen(ZZ, 'h')
            sage: x, y = polygens(h.parent(),'x,y')
            sage: mt = x**2*y**2+(-2*h+2)*x*y**2+(2*h-2)*x*y+(2*h-3)*y**2+(-2*h+2)*y+1
            sage: M_triangle(mt, [x,y]).h()
            H: x^2*y^2 + 2*x*y + (2*h - 4)*x + 1
        """
    def f(self) -> F_triangle:
        """
        Return the associated F-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import M_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: M_triangle(1-y+x*y).f()
            F: x + y + 1

        TESTS::

            sage: h = polygen(ZZ, 'h')
            sage: x, y = polygens(h.parent(),'x,y')
            sage: mt = x**2*y**2+(-2*h+2)*x*y**2+(2*h-2)*x*y+(2*h-3)*y**2+(-2*h+2)*y+1
            sage: M_triangle(mt, [x,y]).f()
            F: (2*h - 3)*x^2 + 2*x*y + y^2 + (2*h - 2)*x + 2*y + 1
        """

class H_triangle(Triangle):
    """
    Class for the H-triangles.
    """
    def transpose(self) -> H_triangle:
        """
        Return the transposed H-triangle.

        OUTPUT: another H-triangle

        This operation is an involution.  When seen as a matrix, it
        performs a symmetry with respect to the northwest-southeast
        diagonal.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: H_triangle(1+x*y).transpose()
            H: x*y + 1
            sage: H_triangle(x^2*y^2 + 2*x*y + x + 1).transpose()
            H: x^2*y^2 + x^2*y + 2*x*y + 1
        """
    def m(self) -> M_triangle:
        """
        Return the associated M-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: h = polygen(ZZ, 'h')
            sage: x, y = polygens(h.parent(),'x,y')
            sage: ht = H_triangle(x^2*y^2 + 2*x*y + 2*x*h - 4*x + 1, variables=[x,y])
            sage: ht.m()
            M: x^2*y^2 + (-2*h + 2)*x*y^2 + (2*h - 2)*x*y
            + (2*h - 3)*y^2 + (-2*h + 2)*y + 1
        """
    def f(self) -> F_triangle:
        """
        Return the associated F-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: H_triangle(1+x*y).f()
            F: x + y + 1
            sage: H_triangle(x^2*y^2 + 2*x*y + x + 1).f()
            F: 2*x^2 + 2*x*y + y^2 + 3*x + 2*y + 1
            sage: flo = H_triangle(1+4*x+2*x**2+x*y*(4+8*x)+
            ....:   x**2*y**2*(6+4*x)+4*(x*y)**3+(x*y)**4).f(); flo
            F: 7*x^4 + 12*x^3*y + 10*x^2*y^2 + 4*x*y^3 + y^4 + 20*x^3
            + 28*x^2*y + 16*x*y^2 + 4*y^3 + 20*x^2 + 20*x*y
            + 6*y^2 + 8*x + 4*y + 1
            sage: flo(-1-x,-1-y) == flo
            True

        TESTS::

            sage: x,y,h = polygens(ZZ,'x,y,h')
            sage: ht = x^2*y^2 + 2*x*y + 2*x*h - 4*x + 1
            sage: H_triangle(ht,[x,y]).f()
            F: 2*x^2*h - 3*x^2 + 2*x*y + y^2 + 2*x*h - 2*x + 2*y + 1
        """
    def gamma(self) -> Gamma_triangle:
        """
        Return the associated Gamma-triangle.

        In some cases, this is a more condensed way to encode
        the same amount of information.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygen(ZZ,'x,y')
            sage: ht = x**2*y**2 + 2*x*y + x + 1
            sage: H_triangle(ht).gamma()
            Γ: y^2 + x

            sage: W = SymmetricGroup(5)                                                 # needs sage.groups
            sage: P = posets.NoncrossingPartitions(W)                                   # needs sage.graphs sage.groups
            sage: P.M_triangle().h().gamma()                                            # needs sage.graphs sage.groups
            Γ: y^4 + 3*x*y^2 + 2*x^2 + 2*x*y + x
        """
    def vector(self):
        """
        Return the h-vector as a polynomial in one variable.

        This is obtained by letting `y=1`.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygen(ZZ,'x,y')
            sage: ht = x**2*y**2 + 2*x*y + x + 1
            sage: H_triangle(ht).vector()
            x^2 + 3*x + 1
        """

class F_triangle(Triangle):
    """
    Class for the F-triangles.
    """
    def h(self) -> H_triangle:
        """
        Return the associated H-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import F_triangle
            sage: x,y = polygens(ZZ,'x,y')
            sage: ft = F_triangle(1+x+y)
            sage: ft.h()
            H: x*y + 1

        TESTS::

            sage: h = polygen(ZZ, 'h')
            sage: x, y = polygens(h.parent(),'x,y')
            sage: ft = 1+2*y+(2*h-2)*x+y**2+2*x*y+(2*h-3)*x**2
            sage: F_triangle(ft, [x,y]).h()
            H: x^2*y^2 + 2*x*y + (2*h - 4)*x + 1
        """
    def m(self) -> M_triangle:
        """
        Return the associated M-triangle.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: H_triangle(1+x*y).f()
            F: x + y + 1
            sage: _.m()
            M: x*y - y + 1

            sage: H_triangle(x^2*y^2 + 2*x*y + x + 1).f()
            F: 2*x^2 + 2*x*y + y^2 + 3*x + 2*y + 1
            sage: _.m()
            M: x^2*y^2 - 3*x*y^2 + 3*x*y + 2*y^2 - 3*y + 1

        TESTS::

            sage: p = 1+4*x+2*x**2+x*y*(4+8*x)
            sage: p += x**2*y**2*(6+4*x)+4*(x*y)**3+(x*y)**4
            sage: flo = H_triangle(p).f(); flo
            F: 7*x^4 + 12*x^3*y + 10*x^2*y^2 + 4*x*y^3 + y^4 + 20*x^3
            + 28*x^2*y + 16*x*y^2 + 4*y^3 + 20*x^2 + 20*x*y
            + 6*y^2 + 8*x + 4*y + 1
            sage: flo.m()
            M: x^4*y^4 - 8*x^3*y^4 + 8*x^3*y^3 + 20*x^2*y^4 - 36*x^2*y^3
            - 20*x*y^4 + 16*x^2*y^2 + 48*x*y^3 + 7*y^4 - 36*x*y^2 - 20*y^3
            + 8*x*y + 20*y^2 - 8*y + 1

            sage: from sage.combinat.triangles_FHM import F_triangle
            sage: h = polygen(ZZ, 'h')
            sage: x, y = polygens(h.parent(),'x,y')
            sage: ft = F_triangle(1+2*y+(2*h-2)*x+y**2+2*x*y+(2*h-3)*x**2,(x,y))
            sage: ft.m()
            M: x^2*y^2 + (-2*h + 2)*x*y^2 + (2*h - 2)*x*y
            + (2*h - 3)*y^2 + (-2*h + 2)*y + 1
        """
    def parabolic(self) -> F_triangle:
        """
        Return a parabolic version of the F-triangle.

        This is obtained by replacing the variable `y` by `y-1`.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import H_triangle
            sage: x, y = polygens(ZZ,'x,y')
            sage: H_triangle(1+x*y).f()
            F: x + y + 1
            sage: _.parabolic()
            F: x + y

        TESTS::

            sage: a, b = polygens(ZZ,'a,b')
            sage: H_triangle(1+a*b).f()
            F: a + b + 1
            sage: _.parabolic()
            F: a + b
        """
    def vector(self):
        """
        Return the f-vector as a polynomial in one variable.

        This is obtained by letting `y=x`.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import F_triangle
            sage: x, y = polygen(ZZ,'x,y')
            sage: ft = 2*x^2 + 2*x*y + y^2 + 3*x + 2*y + 1
            sage: F_triangle(ft).vector()
            5*x^2 + 5*x + 1
        """

class Gamma_triangle(Triangle):
    """
    Class for the Gamma-triangles.
    """
    def h(self) -> H_triangle:
        """
        Return the associated H-triangle.

        The transition between Gamma-triangles and H-triangles is defined by

        .. MATH::

            H(x,y) = (1+x)^d \\sum_{0\\leq i; 0\\leq j \\leq d-2i} \\gamma_{i,j}
            \\left(\\frac{x}{(1+x)^2}\\right)^i \\left(\\frac{1+xy}{1+x}\\right)^j

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import Gamma_triangle
            sage: x, y = polygen(ZZ,'x,y')
            sage: g = y**2 + x
            sage: Gamma_triangle(g).h()
            H: x^2*y^2 + 2*x*y + x + 1

            sage: a, b = polygen(ZZ, 'a, b')
            sage: x, y = polygens(a.parent(),'x,y')
            sage: g = Gamma_triangle(y**3+a*x*y+b*x,(x,y))
            sage: hh = g.h()
            sage: hh.gamma() == g
            True
        """
    def vector(self):
        """
        Return the gamma-vector as a polynomial in one variable.

        This is obtained by letting `y=1`.

        EXAMPLES::

            sage: from sage.combinat.triangles_FHM import Gamma_triangle
            sage: x, y = polygen(ZZ,'x,y')
            sage: gt = y**2 + x
            sage: Gamma_triangle(gt).vector()
            x + 1
        """
