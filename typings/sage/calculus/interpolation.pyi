from typing import Any, ClassVar, overload

class Spline:
    """Spline(v=None)

    File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 9)

    Create a spline interpolation object.

    Given a list `v` of pairs, ``s = spline(v)`` is an object ``s`` such that
    `s(x)` is the value of the spline interpolation through the points
    in `v` at the point `x`.

    The values in `v` do not have to be sorted.  Moreover, one can append
    values to `v`, delete values from `v`, or change values in `v`, and the
    spline is recomputed.

    EXAMPLES::

        sage: S = spline([(0, 1), (1, 2), (4, 5), (5, 3)]); S
        [(0, 1), (1, 2), (4, 5), (5, 3)]
        sage: S(1.5)
        2.76136363636...

    Changing the points of the spline causes the spline to be recomputed::

        sage: S[0] = (0, 2); S
        [(0, 2), (1, 2), (4, 5), (5, 3)]
        sage: S(1.5)
        2.507575757575...

    We may delete interpolation points of the spline::

        sage: del S[2]; S
        [(0, 2), (1, 2), (5, 3)]
        sage: S(1.5)
        2.04296875

    We may append to the list of interpolation points::

        sage: S.append((4, 5)); S
        [(0, 2), (1, 2), (5, 3), (4, 5)]
        sage: S(1.5)
        2.507575757575...

    If we set the `n`-th interpolation point, where `n` is larger than
    ``len(S)``, then points `(0, 0)` will be inserted between the
    interpolation points and the point to be added::

        sage: S[6] = (6, 3); S
        [(0, 2), (1, 2), (5, 3), (4, 5), (0, 0), (0, 0), (6, 3)]

    This example is in the GSL documentation::

        sage: v = [(i + RDF(i).sin()/2, i + RDF(i^2).cos()) for i in range(10)]
        sage: s = spline(v)
        sage: show(point(v) + plot(s,0,9, hue=.8))                                      # needs sage.plot

    We compute the area underneath the spline::

        sage: s.definite_integral(0, 9)
        41.196516041067...

    The definite integral is additive::

        sage: s.definite_integral(0, 4) + s.definite_integral(4, 9)
        41.196516041067...

    Switching the order of the bounds changes the sign of the integral::

        sage: s.definite_integral(9, 0)
        -41.196516041067...

    We compute the first and second-order derivatives at a few points::

        sage: s.derivative(5)
        -0.1623008526180...
        sage: s.derivative(6)
        0.2099798628571...
        sage: s.derivative(5, order=2)
        -3.0874707456138...
        sage: s.derivative(6, order=2)
        2.6187684827485...

    Only the first two derivatives are supported::

        sage: s.derivative(4, order=3)
        Traceback (most recent call last):
        ...
        ValueError: Order of derivative must be 1 or 2."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 95)

                EXAMPLES::

                    sage: S = spline([(1,1), (2,3), (4,5)]); S
                    [(1, 1), (2, 3), (4, 5)]
                    sage: type(S)
                    <class 'sage.calculus.interpolation.Spline'>
        """
    def append(self, xy) -> Any:
        """Spline.append(self, xy)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 180)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.append((5,7)); S
            [(1, 1), (2, 3), (4, 5), (5, 7)]

        The spline is recomputed when points are appended (:issue:`13519`)::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: S(3)
            4.25
            sage: S.append((5, 5)); S
            [(1, 1), (2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.375"""
    def definite_integral(self, doublea, doubleb) -> Any:
        """Spline.definite_integral(self, double a, double b)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 345)

        Value of the definite integral between `a` and `b`.

        INPUT:

        - ``a`` -- lower bound for the integral

        - ``b`` -- upper bound for the integral

        EXAMPLES:

        We draw a cubic spline through three points and compute the
        area underneath the curve::

            sage: s = spline([(0, 0), (1, 3), (2, 0)])
            sage: s.definite_integral(0, 2)
            3.75
            sage: s.definite_integral(0, 1)
            1.875
            sage: s.definite_integral(0, 1) + s.definite_integral(1, 2)
            3.75
            sage: s.definite_integral(2, 0)
            -3.75"""
    def derivative(self, doublex, intorder=...) -> Any:
        """Spline.derivative(self, double x, int order=1)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 303)

        Value of the first or second derivative of the spline at `x`.

        INPUT:

        - ``x`` -- value at which to evaluate the derivative

        - ``order`` -- (default: 1) order of the derivative; must be 1 or 2

        EXAMPLES:

        We draw a cubic spline through three points and compute the
        derivatives::

            sage: s = spline([(0, 0), (2, 3), (4, 0)])
            sage: s.derivative(0)
            2.25
            sage: s.derivative(2)
            0.0
            sage: s.derivative(4)
            -2.25
            sage: s.derivative(1, order=2)
            -1.125
            sage: s.derivative(3, order=2)
            -1.125"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    def __call__(self, doublex) -> Any:
        """Spline.__call__(self, double x)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 280)

        Value of the spline function at `x`.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: S(1)
            1.0
            sage: S(2)
            3.0
            sage: S(4)
            5.0
            sage: S(3.5)
            4.65625"""
    def __delitem__(self, inti) -> Any:
        """Spline.__delitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 156)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: del S[1]
            sage: S
            [(1, 1), (4, 5)]

        The spline is recomputed when points are deleted (:issue:`13519`)::

            sage: S = spline([(1,1), (2,3), (4,5), (5, 5)]); S
            [(1, 1), (2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.375
            sage: del S[0]; S
            [(2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.25"""
    def __getitem__(self, inti) -> Any:
        """Spline.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 143)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S[0]
            (1, 1)
            sage: S[-1]
            (4, 5)
            sage: S[1]
            (2, 3)"""
    def __len__(self) -> Any:
        """Spline.__len__(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 223)

        Number of points that the spline goes through.

        EXAMPLES::

            sage: len(spline([(1,1), (2,3), (4,5)]))
            3"""
    def __setitem__(self, inti, xy) -> Any:
        """Spline.__setitem__(self, int i, xy)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 110)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: S(1.5)
            2.0625

        Replace `0`-th point, which changes the spline::

            sage: S[0] = (0,1); S
            [(0, 1), (2, 3), (4, 5)]
            sage: S(1.5)
            2.5

        If you set the `n`-th point and `n` is larger than ``len(S)``,
        then `(0,0)` points are inserted and the `n`-th entry is set
        (which may be a weird thing to do, but that is what happens)::

            sage: S[4] = (6,10)
            sage: S
            [(0, 1), (2, 3), (4, 5), (0, 0), (6, 10)]"""

class spline:
    """Spline(v=None)

    File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 9)

    Create a spline interpolation object.

    Given a list `v` of pairs, ``s = spline(v)`` is an object ``s`` such that
    `s(x)` is the value of the spline interpolation through the points
    in `v` at the point `x`.

    The values in `v` do not have to be sorted.  Moreover, one can append
    values to `v`, delete values from `v`, or change values in `v`, and the
    spline is recomputed.

    EXAMPLES::

        sage: S = spline([(0, 1), (1, 2), (4, 5), (5, 3)]); S
        [(0, 1), (1, 2), (4, 5), (5, 3)]
        sage: S(1.5)
        2.76136363636...

    Changing the points of the spline causes the spline to be recomputed::

        sage: S[0] = (0, 2); S
        [(0, 2), (1, 2), (4, 5), (5, 3)]
        sage: S(1.5)
        2.507575757575...

    We may delete interpolation points of the spline::

        sage: del S[2]; S
        [(0, 2), (1, 2), (5, 3)]
        sage: S(1.5)
        2.04296875

    We may append to the list of interpolation points::

        sage: S.append((4, 5)); S
        [(0, 2), (1, 2), (5, 3), (4, 5)]
        sage: S(1.5)
        2.507575757575...

    If we set the `n`-th interpolation point, where `n` is larger than
    ``len(S)``, then points `(0, 0)` will be inserted between the
    interpolation points and the point to be added::

        sage: S[6] = (6, 3); S
        [(0, 2), (1, 2), (5, 3), (4, 5), (0, 0), (0, 0), (6, 3)]

    This example is in the GSL documentation::

        sage: v = [(i + RDF(i).sin()/2, i + RDF(i^2).cos()) for i in range(10)]
        sage: s = spline(v)
        sage: show(point(v) + plot(s,0,9, hue=.8))                                      # needs sage.plot

    We compute the area underneath the spline::

        sage: s.definite_integral(0, 9)
        41.196516041067...

    The definite integral is additive::

        sage: s.definite_integral(0, 4) + s.definite_integral(4, 9)
        41.196516041067...

    Switching the order of the bounds changes the sign of the integral::

        sage: s.definite_integral(9, 0)
        -41.196516041067...

    We compute the first and second-order derivatives at a few points::

        sage: s.derivative(5)
        -0.1623008526180...
        sage: s.derivative(6)
        0.2099798628571...
        sage: s.derivative(5, order=2)
        -3.0874707456138...
        sage: s.derivative(6, order=2)
        2.6187684827485...

    Only the first two derivatives are supported::

        sage: s.derivative(4, order=3)
        Traceback (most recent call last):
        ...
        ValueError: Order of derivative must be 1 or 2."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, v) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 95)

                EXAMPLES::

                    sage: S = spline([(1,1), (2,3), (4,5)]); S
                    [(1, 1), (2, 3), (4, 5)]
                    sage: type(S)
                    <class 'sage.calculus.interpolation.Spline'>
        """
    @overload
    def __init__(self, v) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 95)

                EXAMPLES::

                    sage: S = spline([(1,1), (2,3), (4,5)]); S
                    [(1, 1), (2, 3), (4, 5)]
                    sage: type(S)
                    <class 'sage.calculus.interpolation.Spline'>
        """
    def append(self, xy) -> Any:
        """Spline.append(self, xy)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 180)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.append((5,7)); S
            [(1, 1), (2, 3), (4, 5), (5, 7)]

        The spline is recomputed when points are appended (:issue:`13519`)::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: S(3)
            4.25
            sage: S.append((5, 5)); S
            [(1, 1), (2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.375"""
    def definite_integral(self, doublea, doubleb) -> Any:
        """Spline.definite_integral(self, double a, double b)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 345)

        Value of the definite integral between `a` and `b`.

        INPUT:

        - ``a`` -- lower bound for the integral

        - ``b`` -- upper bound for the integral

        EXAMPLES:

        We draw a cubic spline through three points and compute the
        area underneath the curve::

            sage: s = spline([(0, 0), (1, 3), (2, 0)])
            sage: s.definite_integral(0, 2)
            3.75
            sage: s.definite_integral(0, 1)
            1.875
            sage: s.definite_integral(0, 1) + s.definite_integral(1, 2)
            3.75
            sage: s.definite_integral(2, 0)
            -3.75"""
    def derivative(self, doublex, intorder=...) -> Any:
        """Spline.derivative(self, double x, int order=1)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 303)

        Value of the first or second derivative of the spline at `x`.

        INPUT:

        - ``x`` -- value at which to evaluate the derivative

        - ``order`` -- (default: 1) order of the derivative; must be 1 or 2

        EXAMPLES:

        We draw a cubic spline through three points and compute the
        derivatives::

            sage: s = spline([(0, 0), (2, 3), (4, 0)])
            sage: s.derivative(0)
            2.25
            sage: s.derivative(2)
            0.0
            sage: s.derivative(4)
            -2.25
            sage: s.derivative(1, order=2)
            -1.125
            sage: s.derivative(3, order=2)
            -1.125"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    @overload
    def list(self) -> Any:
        """Spline.list(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 201)

        Underlying list of points that this spline goes through.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S.list()
            [(1, 1), (2, 3), (4, 5)]

        This is a copy of the list, not a reference (:issue:`13530`)::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: L = S.list(); L
            [(1, 1), (2, 3), (4, 5)]
            sage: L[2] = (3, 2)
            sage: L
            [(1, 1), (2, 3), (3, 2)]
            sage: S.list()
            [(1, 1), (2, 3), (4, 5)]"""
    def __call__(self, doublex) -> Any:
        """Spline.__call__(self, double x)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 280)

        Value of the spline function at `x`.

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)])
            sage: S(1)
            1.0
            sage: S(2)
            3.0
            sage: S(4)
            5.0
            sage: S(3.5)
            4.65625"""
    def __delitem__(self, inti) -> Any:
        """Spline.__delitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 156)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: del S[1]
            sage: S
            [(1, 1), (4, 5)]

        The spline is recomputed when points are deleted (:issue:`13519`)::

            sage: S = spline([(1,1), (2,3), (4,5), (5, 5)]); S
            [(1, 1), (2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.375
            sage: del S[0]; S
            [(2, 3), (4, 5), (5, 5)]
            sage: S(3)
            4.25"""
    def __getitem__(self, inti) -> Any:
        """Spline.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 143)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S[0]
            (1, 1)
            sage: S[-1]
            (4, 5)
            sage: S[1]
            (2, 3)"""
    def __len__(self) -> Any:
        """Spline.__len__(self)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 223)

        Number of points that the spline goes through.

        EXAMPLES::

            sage: len(spline([(1,1), (2,3), (4,5)]))
            3"""
    def __setitem__(self, inti, xy) -> Any:
        """Spline.__setitem__(self, int i, xy)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolation.pyx (starting at line 110)

        EXAMPLES::

            sage: S = spline([(1,1), (2,3), (4,5)]); S
            [(1, 1), (2, 3), (4, 5)]
            sage: S(1.5)
            2.0625

        Replace `0`-th point, which changes the spline::

            sage: S[0] = (0,1); S
            [(0, 1), (2, 3), (4, 5)]
            sage: S(1.5)
            2.5

        If you set the `n`-th point and `n` is larger than ``len(S)``,
        then `(0,0)` points are inserted and the `n`-th entry is set
        (which may be a weird thing to do, but that is what happens)::

            sage: S[4] = (6,10)
            sage: S
            [(0, 1), (2, 3), (4, 5), (0, 0), (6, 10)]"""
