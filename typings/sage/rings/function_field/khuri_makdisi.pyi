from sage.matrix.constructor import matrix as matrix
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class KhuriMakdisi_base:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add(self, Matrixwd1, Matrixwd2) -> Matrix:
        """KhuriMakdisi_base.add(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 200)

        Theorem 4.5 (addition).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p = G.point(pl - b)
            sage: p + p   # indirect doctest
            Point of Jacobian determined by
            [ 1  0  0  0  0  0  0 10  0]
            [ 0  1  0  0  0  0  5  1  4]
            [ 0  0  1  0  0  0 15  7 12]
            [ 0  0  0  1  0  0 14  8 16]
            [ 0  0  0  0  1  0  3 12 16]
            [ 0  0  0  0  0  1 13  5  7]"""
    def multiple(self, Matrixwd, n) -> Matrix:
        """KhuriMakdisi_base.multiple(self, Matrix wd, n) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 250)

        Compute multiple by additive square-and-multiply method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p = G.point(pl - b)
            sage: 10*p
            Point of Jacobian determined by
            [ 1  0  0  0  0  0  5  2  2]
            [ 0  1  0  0  0  0 13  6 11]
            [ 0  0  1  0  0  0  1 11  4]
            [ 0  0  0  1  0  0  1 13  7]
            [ 0  0  0  0  1  0 12 16  2]
            [ 0  0  0  0  0  1  6  9 10]
            sage: (-10)*p
            Point of Jacobian determined by
            [ 1  0  0  0  0 13  0 10  6]
            [ 0  1  0  0  0  5  0  4 16]
            [ 0  0  1  0  0  2  0  0  4]
            [ 0  0  0  1  0  9  0  6  9]
            [ 0  0  0  0  1  6  0  0  9]
            [ 0  0  0  0  0  0  1  9  5]
            sage: 0*p
            Point of Jacobian determined by
            [1 0 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0]
            [0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0 0 0]
            [0 0 0 0 0 0 0 1 0]"""
    def negate(self, Matrixwd) -> Matrix:
        """KhuriMakdisi_base.negate(self, Matrix wd) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 175)

        Theorem 4.4 (negation), first method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p = G.point(pl - b)
            sage: -p   # indirect doctest
            Point of Jacobian determined by
            [ 1  0  0  0  0  0 15 11  2]
            [ 0  1  0  0  0  0 16  0 12]
            [ 0  0  1  0  0  0  0 16  0]
            [ 0  0  0  1  0  0  0  0 16]
            [ 0  0  0  0  1  0 12  0 16]
            [ 0  0  0  0  0  1 15 16  2]"""
    def subtract(self, Matrixwd1, Matrixwd2) -> Matrix:
        """KhuriMakdisi_base.subtract(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 225)

        Theorem 4.6 (subtraction), first method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p = G.point(pl - b)
            sage: p - p   # indirect doctest
            Point of Jacobian determined by
            [1 0 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0]
            [0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0 0 0]
            [0 0 0 0 0 0 0 1 0]"""
    @overload
    def zero_divisor(self) -> Matrix:
        """KhuriMakdisi_base.zero_divisor(self) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 319)

        Return the matrix `w_L` representing zero divisor.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: G._km.zero_divisor()
            [1 0 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0]
            [0 0 0 1 0 0 0 0 0]
            [0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0 0 0]
            [0 0 0 0 0 0 1 0 0]
            [0 0 0 0 0 0 0 1 0]
            [0 0 0 0 0 0 0 0 1]"""
    @overload
    def zero_divisor(self) -> Any:
        """KhuriMakdisi_base.zero_divisor(self) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 319)

        Return the matrix `w_L` representing zero divisor.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: G._km.zero_divisor()
            [1 0 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0]
            [0 0 0 1 0 0 0 0 0]
            [0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0 0 0]
            [0 0 0 0 0 0 1 0 0]
            [0 0 0 0 0 0 0 1 0]
            [0 0 0 0 0 0 0 0 1]"""

class KhuriMakdisi_large(KhuriMakdisi_base):
    """KhuriMakdisi_large(V, mu, w0, d0, g)

    File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 346)

    Khuri-Makdisi's large model."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, V, mu, w0, d0, g) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 352)

                Initialize.

                TESTS::

                    sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
                    sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
                    sage: h = C.function(y/x).divisor_of_poles()
                    sage: b = C([0,1,0]).place()
                    sage: pl1 = C([-1,2,1]).place()
                    sage: pl2 = C([3,7,1]).place()
                    sage: J = C.jacobian(model='km_large', base_div=h)
                    sage: G = J.group()
                    sage: p1 = G.point(pl1 - b)
                    sage: p2 = G.point(pl2 - b)
                    sage: p1
                    Point of Jacobian determined by
                    [ 1  0  0  0  0  0  0 12 15]
                    [ 0  1  0  0  0  0  0  0 13]
                    [ 0  0  1  0  0  0  0  0  2]
                    [ 0  0  0  1  0  0  0  0 16]
                    [ 0  0  0  0  0  1  0  0 15]
                    [ 0  0  0  0  0  0  1  0  1]
                    sage: p2
                    Point of Jacobian determined by
                    [ 1  0  0  0  0  0  0 12  5]
                    [ 0  1  0  0  0  0  0  0  2]
                    [ 0  0  1  0  0  0  0  0 13]
                    [ 0  0  0  1  0  0  0  0  8]
                    [ 0  0  0  0  0  1  0  0 10]
                    [ 0  0  0  0  0  0  1  0 14]
                    sage: p1 + p2
                    Point of Jacobian determined by
                    [ 1  0  0  0  0 16  0  5  3]
                    [ 0  1  0  0  0  6  0  8 16]
                    [ 0  0  1  0  0 15  0  3 10]
                    [ 0  0  0  1  0  3  0  0  0]
                    [ 0  0  0  0  1 12  0 16  8]
                    [ 0  0  0  0  0  0  1  3  0]
                    sage: p1 - p2
                    Point of Jacobian determined by
                    [ 1  0  0  0  0  0 13  9  5]
                    [ 0  1  0  0  0  0  2  5  8]
                    [ 0  0  1  0  0  0  6  7  5]
                    [ 0  0  0  1  0  0 11  3 16]
                    [ 0  0  0  0  1  0  9  7 10]
                    [ 0  0  0  0  0  1  4 10  5]
                    sage: p1.addflip(p2) == -(p1 + p2)
                    True
        """
    def add_divisor(self, Matrixwd1, Matrixwd2, intd1, intd2) -> Matrix:
        """KhuriMakdisi_large.add_divisor(self, Matrix wd1, Matrix wd2, int d1, int d2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 499)

        Theorem 3.6 (addition of divisors, first method).

        We assume that `w_{D_1}`, `w_{D_2}` represent divisors of degree at most
        `3d_0 - 2g - 1`.

        TESTS::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='km_large')
            sage: G = J.group()
            sage: pts = G.get_points(G.order())  # indirect doctest
            sage: len(pts)
            11"""
    @overload
    def addflip(self, Matrixwd1, Matrixwd2) -> Matrix:
        """KhuriMakdisi_large.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 471)

        Theorem 4.3 (addflip).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: F = C.function_field()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1.addflip(p2)
            Point of Jacobian determined by
            [ 1  0  0  0  0  0  7 10  9]
            [ 0  1  0  0  0  0  4 14 10]
            [ 0  0  1  0  0  0  7  0  9]
            [ 0  0  0  1  0  0 10 10  6]
            [ 0  0  0  0  1  0  6  5 15]
            [ 0  0  0  0  0  1 14  9  1]"""
    @overload
    def addflip(self, p2) -> Any:
        """KhuriMakdisi_large.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 471)

        Theorem 4.3 (addflip).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: F = C.function_field()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1.addflip(p2)
            Point of Jacobian determined by
            [ 1  0  0  0  0  0  7 10  9]
            [ 0  1  0  0  0  0  4 14 10]
            [ 0  0  1  0  0  0  7  0  9]
            [ 0  0  0  1  0  0 10 10  6]
            [ 0  0  0  0  1  0  6  5 15]
            [ 0  0  0  0  0  1 14  9  1]"""
    def equal(self, wd, we) -> Any:
        """KhuriMakdisi_large.equal(self, wd, we)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 409)

        Theorem 4.1, second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='km_large')
            sage: b = C([0,1,0]).place()
            sage: J.set_base_place(b)
            sage: G = J.group()
            sage: pl1 = C([3,2,1]).place()
            sage: pl2 = C([5,5,1]).place()
            sage: p1 = G(pl1)
            sage: p2 = G(pl2)
            sage: p1 + p2 == p2 + p1  # indirect doctest
            True
            sage: p1 - p2 == -(p2 - p1)
            True
            sage: zero = G.zero()
            sage: p1 + zero == p1
            True
            sage: p1 - p1 == zero
            True"""

class KhuriMakdisi_medium(KhuriMakdisi_base):
    """KhuriMakdisi_medium(V, mu, w0, d0, g)

    File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 526)

    Khuri-Makdisi's *medium* model"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, V, mu, w0, d0, g) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 532)

                Initialize.

                TESTS::

                    sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
                    sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
                    sage: h = C.function(y/x).divisor_of_poles()
                    sage: b = C([0,1,0]).place()
                    sage: pl1 = C([-1,2,1]).place()
                    sage: pl2 = C([3,7,1]).place()
                    sage: J = C.jacobian(model='km_medium', base_div=h)
                    sage: G = J.group()
                    sage: p1 = G.point(pl1 - b)
                    sage: p2 = G.point(pl2 - b)
                    sage: p1
                    Point of Jacobian determined by
                    [ 1  0  0  0 16 12]
                    [ 0  1  0  0 15  0]
                    [ 0  0  1  0  1  0]
                    sage: p2
                    Point of Jacobian determined by
                    [ 1  0  0  0  8 12]
                    [ 0  1  0  0 10  0]
                    [ 0  0  1  0 14  0]
                    sage: p1 + p2
                    Point of Jacobian determined by
                    [ 1  0  0  6  3 16]
                    [ 0  1  0 15 16 10]
                    [ 0  0  1  3  0  0]
                    sage: p1 - p2
                    Point of Jacobian determined by
                    [ 1  0  0  8  0 14]
                    [ 0  1  0  1 10 10]
                    [ 0  0  1 15  3  6]
                    sage: p1.addflip(p2) == -(p1 + p2)
                    True
        """
    def add_divisor(self, Matrixwd1, Matrixwd2, intd1, intd2) -> Matrix:
        """KhuriMakdisi_medium.add_divisor(self, Matrix wd1, Matrix wd2, int d1, int d2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 663)

        Theorem 3.6 (addition of divisors, first method).

        We assume that `w_{D_1}`, `w_{D_2}` represent divisors of degree at
        most `4d_0 - 2g - 1`.

        TESTS::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='km_medium')
            sage: G = J.group()
            sage: pts = G.get_points(G.order())  # indirect doctest
            sage: len(pts)
            11"""
    @overload
    def addflip(self, Matrixwd1, Matrixwd2) -> Matrix:
        """KhuriMakdisi_medium.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 618)

        Theorem 5.1 (addflip in medium model).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_medium', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  6  3 16]
            [ 0  1  0  0  7  9]
            [ 0  0  1 14  2  3]

        We check the computation in other model::

            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == p1.addflip(p2)
            True"""
    @overload
    def addflip(self, p2) -> Any:
        """KhuriMakdisi_medium.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 618)

        Theorem 5.1 (addflip in medium model).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_medium', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  6  3 16]
            [ 0  1  0  0  7  9]
            [ 0  0  1 14  2  3]

        We check the computation in other model::

            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == p1.addflip(p2)
            True"""
    @overload
    def addflip(self, p2) -> Any:
        """KhuriMakdisi_medium.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 618)

        Theorem 5.1 (addflip in medium model).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_medium', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  6  3 16]
            [ 0  1  0  0  7  9]
            [ 0  0  1 14  2  3]

        We check the computation in other model::

            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == p1.addflip(p2)
            True"""
    def equal(self, wd, we) -> Any:
        """KhuriMakdisi_medium.equal(self, wd, we)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 583)

        Theorem 4.1, second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_medium', base_div=h)
            sage: G = J.group()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1 + p2 == p2 + p1  # indirect doctest
            True
            sage: p1 - p2 == -(p2 - p1)
            True
            sage: zero = G.zero()
            sage: p1 + zero == p1
            True
            sage: p1 - p1 == zero
            True"""

class KhuriMakdisi_small(KhuriMakdisi_base):
    """KhuriMakdisi_small(V, mu, w0, d0, g)

    File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 690)

    Khuri-Makdisi's *small* model"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, V, mu, w0, d0, g) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 697)

                Initialize.

                TESTS::

                    sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
                    sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
                    sage: b = C([0,1,0]).place()
                    sage: pl1 = C([-1,2,1]).place()
                    sage: pl2 = C([3,7,1]).place()
                    sage: J = C.jacobian(model='km_small', base_div=2*b)
                    sage: G = J.group()
                    sage: p1 = G.point(pl1 - b)
                    sage: p2 = G.point(pl2 - b)
                    sage: p1
                    Point of Jacobian determined by
                    [ 1  0  0  0  0 11]
                    [ 0  1  0  0  2  0]
                    [ 0  0  1  0 16 10]
                    [ 0  0  0  1  0  3]
                    sage: p2
                    Point of Jacobian determined by
                    [1 0 0 0 0 3]
                    [0 1 0 0 7 0]
                    [0 0 1 0 3 5]
                    [0 0 0 1 0 2]
                    sage: p1 + p2
                    Point of Jacobian determined by
                    [ 1  0  0  0 10  9]
                    [ 0  1  0  0  7  5]
                    [ 0  0  1  0 15  4]
                    [ 0  0  0  1  3 10]
                    sage: p1 - p2
                    Point of Jacobian determined by
                    [ 1  0  0  0 10  9]
                    [ 0  1  0  0  9  8]
                    [ 0  0  1  0 15  4]
                    [ 0  0  0  1 15 11]
                    sage: p1.addflip(p2) == -(p1 + p2)
                    True
        """
    def add_divisor(self, Matrixwd1, Matrixwd2, intd1, intd2) -> Matrix:
        """KhuriMakdisi_small.add_divisor(self, Matrix wd1, Matrix wd2, int d1, int d2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 904)

        Theorem 3.6 (addition of divisors, first method).

        We assume that `w_{D_1}`, `w_{D_2}` represent divisors of degree at most
        `6d_0 - 2g - 1`.

        TESTS::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='km_small')
            sage: G = J.group()
            sage: pts = G.get_points(G.order())  # indirect doctest
            sage: len(pts)
            11"""
    @overload
    def addflip(self, Matrixwd1, Matrixwd2) -> Matrix:
        """KhuriMakdisi_small.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 788)

        Theorem 5.3 (addflip in small model), second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_small', base_div=2*b)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  0 10  9]
            [ 0  1  0  0 10 12]
            [ 0  0  1  0 15  4]
            [ 0  0  0  1 14  7]

        We check the computation in other model::

            sage: h = C.function(y/x).divisor_of_poles()
            sage: Jl = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: q1 = G.point(pl1 - b)
            sage: q2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == q1.addflip(p2)
            True

        Check that :issue:`40237` is fixed::

            sage: K = GF(2)
            sage: F.<x> = FunctionField(K)
            sage: t = polygen(F)
            sage: E.<y> = F.extension(t^3 + (x^2 + x + 1)*t^2 + (x^3 + x + 1)*t + x^5 + x^4)
            sage: O = E.maximal_order()
            sage: Oinf = E.maximal_order_infinite()
            sage: D1 = (-5*O.ideal(x, y).divisor() + O.ideal(x + 1, y^2 + y + 1).divisor()
            ....:   + O.ideal(x^3 + x^2 + 1, y + x + 1).divisor())
            sage: D2 = (Oinf.ideal(1/x, y/x^2 + 1).divisor() - 5*O.ideal(x, y).divisor()
            ....:   + O.ideal(x^4 + x^3 + 1, y + x).divisor())
            sage: J = E.jacobian('km_small', base_div=5*O.ideal(x, y).divisor())
            sage: JD1 = J(D1)
            sage: JD2 = J(D2)
            sage: JD1 + JD2 == JD2 + JD1
            True"""
    @overload
    def addflip(self, p2) -> Any:
        """KhuriMakdisi_small.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 788)

        Theorem 5.3 (addflip in small model), second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_small', base_div=2*b)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  0 10  9]
            [ 0  1  0  0 10 12]
            [ 0  0  1  0 15  4]
            [ 0  0  0  1 14  7]

        We check the computation in other model::

            sage: h = C.function(y/x).divisor_of_poles()
            sage: Jl = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: q1 = G.point(pl1 - b)
            sage: q2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == q1.addflip(p2)
            True

        Check that :issue:`40237` is fixed::

            sage: K = GF(2)
            sage: F.<x> = FunctionField(K)
            sage: t = polygen(F)
            sage: E.<y> = F.extension(t^3 + (x^2 + x + 1)*t^2 + (x^3 + x + 1)*t + x^5 + x^4)
            sage: O = E.maximal_order()
            sage: Oinf = E.maximal_order_infinite()
            sage: D1 = (-5*O.ideal(x, y).divisor() + O.ideal(x + 1, y^2 + y + 1).divisor()
            ....:   + O.ideal(x^3 + x^2 + 1, y + x + 1).divisor())
            sage: D2 = (Oinf.ideal(1/x, y/x^2 + 1).divisor() - 5*O.ideal(x, y).divisor()
            ....:   + O.ideal(x^4 + x^3 + 1, y + x).divisor())
            sage: J = E.jacobian('km_small', base_div=5*O.ideal(x, y).divisor())
            sage: JD1 = J(D1)
            sage: JD2 = J(D2)
            sage: JD1 + JD2 == JD2 + JD1
            True"""
    @overload
    def addflip(self, p2) -> Any:
        """KhuriMakdisi_small.addflip(self, Matrix wd1, Matrix wd2) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 788)

        Theorem 5.3 (addflip in small model), second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_small', base_div=2*b)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: af = p1.addflip(p2)
            sage: af
            Point of Jacobian determined by
            [ 1  0  0  0 10  9]
            [ 0  1  0  0 10 12]
            [ 0  0  1  0 15  4]
            [ 0  0  0  1 14  7]

        We check the computation in other model::

            sage: h = C.function(y/x).divisor_of_poles()
            sage: Jl = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: q1 = G.point(pl1 - b)
            sage: q2 = G.point(pl2 - b)
            sage: G.point(af.divisor()) == q1.addflip(p2)
            True

        Check that :issue:`40237` is fixed::

            sage: K = GF(2)
            sage: F.<x> = FunctionField(K)
            sage: t = polygen(F)
            sage: E.<y> = F.extension(t^3 + (x^2 + x + 1)*t^2 + (x^3 + x + 1)*t + x^5 + x^4)
            sage: O = E.maximal_order()
            sage: Oinf = E.maximal_order_infinite()
            sage: D1 = (-5*O.ideal(x, y).divisor() + O.ideal(x + 1, y^2 + y + 1).divisor()
            ....:   + O.ideal(x^3 + x^2 + 1, y + x + 1).divisor())
            sage: D2 = (Oinf.ideal(1/x, y/x^2 + 1).divisor() - 5*O.ideal(x, y).divisor()
            ....:   + O.ideal(x^4 + x^3 + 1, y + x).divisor())
            sage: J = E.jacobian('km_small', base_div=5*O.ideal(x, y).divisor())
            sage: JD1 = J(D1)
            sage: JD2 = J(D2)
            sage: JD1 + JD2 == JD2 + JD1
            True"""
    def equal(self, wd, we) -> Any:
        """KhuriMakdisi_small.equal(self, wd, we)

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 754)

        Theorem 4.1, second method.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,7,1]).place()
            sage: J = C.jacobian(model='km_small', base_div=2*b)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1 + p2 == p2 + p1   # indirect doctest
            True
            sage: p1 - p2 == -(p2 - p1)
            True
            sage: zero = G.zero()
            sage: p1 + zero == p1
            True
            sage: p1 - p1 == zero
            True"""
    def negate(self, Matrixwd) -> Matrix:
        """KhuriMakdisi_small.negate(self, Matrix wd) -> Matrix

        File: /build/sagemath/src/sage/src/sage/rings/function_field/khuri_makdisi.pyx (starting at line 856)

        Theorem 5.4 (negation in small model).

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([3,2,1]).place()
            sage: pl2 = C([5,5,1]).place()
            sage: J = C.jacobian(model='km_small', base_div=2*b)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: -(-p1) == p1  # indirect doctest
            True

        Check that :issue:`39148` is fixed::

            sage: k.<x> = FunctionField(GF(17)); t = polygen(k)
            sage: F.<y> = k.extension(t^4 + (14*x + 14)*t^3 + 9*t^2 + (10*x^2 + 15*x + 8)*t
            ....:  + 7*x^3 + 15*x^2 + 6*x + 16)
            sage: infty1, infty2 = F.places_infinite()
            sage: O = F.maximal_order()
            sage: P = O.ideal((x + 1, y + 7)).divisor()
            sage: D1 = 3*infty2 + infty1 - 4*P
            sage: D2 = F.divisor_group().zero()
            sage: J = F.jacobian(model='km-small', base_div=4*P)
            sage: J(D1) + J(D2) == J(D1)
            True"""
