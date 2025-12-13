import _cython_3_2_1
from typing import Any, overload

complex_cubic_spline: _cython_3_2_1.cython_function_or_method
pi: float
polygon_spline: _cython_3_2_1.cython_function_or_method

class CCSpline:
    """CCSpline(pts)

    File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 207)

    A ``CCSpline`` object contains a cubic interpolation of a figure
    in the complex plane.

    EXAMPLES:

    A simple ``square``::

        sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        sage: cs = complex_cubic_spline(pts)
        sage: cs.value(0)
        (-1-1j)
        sage: cs.derivative(0)
        (0.9549296...-0.9549296...j)"""
    def __init__(self, pts) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 227)

                TESTS::

                    sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
                    sage: cs = complex_cubic_spline(pts)
        """
    @overload
    def derivative(self, doublet) -> Any:
        """CCSpline.derivative(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 295)

        Return the derivative (speed and direction of the curve) of a
        given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the derivative at the point on the
        figure corresponding to the input ``t``.

        EXAMPLES::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: cs = complex_cubic_spline(pts)
            sage: cs.derivative(3 / 5)
            (1.40578892327...-0.225417136326...j)
            sage: from math import pi
            sage: cs.derivative(0) - cs.derivative(2 * pi)
            0j
            sage: cs.derivative(-6)
            (2.52047692949...-1.89392588310...j)"""
    @overload
    def derivative(self, speedanddirectionofthecurve) -> Any:
        """CCSpline.derivative(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 295)

        Return the derivative (speed and direction of the curve) of a
        given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the derivative at the point on the
        figure corresponding to the input ``t``.

        EXAMPLES::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: cs = complex_cubic_spline(pts)
            sage: cs.derivative(3 / 5)
            (1.40578892327...-0.225417136326...j)
            sage: from math import pi
            sage: cs.derivative(0) - cs.derivative(2 * pi)
            0j
            sage: cs.derivative(-6)
            (2.52047692949...-1.89392588310...j)"""
    def value(self, doublet) -> Any:
        """CCSpline.value(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 262)

        Return the location of a given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the point on the figure corresponding
        to the input ``t``.

        EXAMPLES:

        ::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: cs = complex_cubic_spline(pts)
            sage: cs.value(4 / 7)
            (-0.303961332787...-1.34716728183...j)
            sage: from math import pi
            sage: cs.value(0) - cs.value(2*pi)
            0j
            sage: cs.value(-2.73452)
            (0.934561222231...+0.881366116402...j)"""

class PSpline:
    """PSpline(pts)

    File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 71)

    A ``CCSpline`` object contains a polygon interpolation of a figure
    in the complex plane.

    EXAMPLES:

    A simple ``square``::

        sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        sage: ps = polygon_spline(pts)
        sage: ps.value(0)
        (-1-1j)
        sage: ps.derivative(0)
        (1.27323954...+0j)"""
    def __init__(self, pts) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 90)

                TESTS::

                    sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
                    sage: ps = polygon_spline(pts)
        """
    @overload
    def derivative(self, doublet) -> Any:
        """PSpline.derivative(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 137)

        Return the derivative (speed and direction of the curve) of a
        given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the derivative at the point on the
        polygon corresponding to the input ``t``.

        EXAMPLES:

        ::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: ps = polygon_spline(pts)
            sage: ps.derivative(1 / 3)
            (1.27323954473...+0j)
            sage: from math import pi
            sage: ps.derivative(0) - ps.derivative(2*pi)
            0j
            sage: ps.derivative(10)
            (-1.27323954473...+0j)"""
    @overload
    def derivative(self, speedanddirectionofthecurve) -> Any:
        """PSpline.derivative(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 137)

        Return the derivative (speed and direction of the curve) of a
        given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the derivative at the point on the
        polygon corresponding to the input ``t``.

        EXAMPLES:

        ::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: ps = polygon_spline(pts)
            sage: ps.derivative(1 / 3)
            (1.27323954473...+0j)
            sage: from math import pi
            sage: ps.derivative(0) - ps.derivative(2*pi)
            0j
            sage: ps.derivative(10)
            (-1.27323954473...+0j)"""
    def value(self, doublet) -> Any:
        """PSpline.value(self, double t)

        File: /build/sagemath/src/sage/src/sage/calculus/interpolators.pyx (starting at line 104)

        Return the derivative (speed and direction of the curve) of a
        given point from the parameter ``t``.

        INPUT:

        - ``t`` -- double; the parameter value for the parameterized curve,
          between 0 and 2*pi

        OUTPUT:

        A complex number representing the point on the polygon corresponding
        to the input ``t``.

        EXAMPLES:

        ::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: ps = polygon_spline(pts)
            sage: ps.value(.5)
            (-0.363380227632...-1j)
            sage: ps.value(0) - ps.value(2*RDF.pi())
            0j
            sage: ps.value(10)
            (0.26760455264...+1j)"""
