"""
Complex Interpolation

AUTHORS:

- Ethan Van Andel (2009): initial version

Development supported by NSF award No. 0702939.
"""

from typings_sagemath import Num, Real
from collections import Sequence
from numpy import complex128
from numpy.typing import ArrayLike

pi: float

def polygon_spline(pts: Sequence[tuple[Num, Num]] | ArrayLike) -> PSpline:
    """
    Create a polygon from a set of complex or `(x,y)` points. The polygon
    will be a parametric curve from 0 to 2*pi. The returned values will be
    complex, not `(x,y)`.

    INPUT:

    - ``pts`` -- list or array of complex numbers of tuples of the form `(x,y)`

    EXAMPLES:

    A simple square::

        sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        sage: ps = polygon_spline(pts)
        sage: fx = lambda x: ps.value(x).real
        sage: fy = lambda x: ps.value(x).imag
        sage: show(parametric_plot((fx, fy), (0, 2*pi)))                                # needs sage.plot sage.symbolic
        sage: m = Riemann_Map([lambda x: ps.value(real(x))],
        ....:                 [lambda x: ps.derivative(real(x))], 0)
        sage: show(m.plot_colored() + m.plot_spiderweb())                               # needs sage.plot

    Polygon approximation of a circle::

        sage: # needs sage.symbolic
        sage: pts = [e^(I*t / 25) for t in range(25)]
        sage: ps = polygon_spline(pts)
        sage: ps.derivative(2)
        (-0.0470303661...+0.1520363883...j)
    """

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
    def __init__(self, pts: Sequence[tuple[Num, Num]]| ArrayLike):
        """
        TESTS::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: ps = polygon_spline(pts)
        """
    def derivative(self, t: Real) -> complex128:
        """
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
    def value(self, t: Real) -> complex128:
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

def complex_cubic_spline(pts: Sequence[tuple[Num, Num]] | ArrayLike) -> CCSpline:
    """
    Create a cubic spline interpolated figure from a set of complex or
    `(x,y)` points. The figure will be a parametric curve from 0 to 2*pi.
    The returned values will be complex, not `(x,y)`.

    INPUT:

    - ``pts`` -- list or array of complex numbers, or tuples of the form `(x,y)`

    EXAMPLES:

    A simple ``square``::

        sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        sage: cs = complex_cubic_spline(pts)
        sage: fx = lambda x: cs.value(x).real
        sage: fy = lambda x: cs.value(x).imag
        sage: from math import pi
        sage: show(parametric_plot((fx, fy), (0, 2*pi)))                                # needs sage.plot
        sage: m = Riemann_Map([lambda x: cs.value(real(x))],
        ....:                 [lambda x: cs.derivative(real(x))], 0)
        sage: show(m.plot_colored() + m.plot_spiderweb())                               # needs sage.plot

    Polygon approximation of a circle::

        sage: from cmath import exp
        sage: pts = [exp(1j * t / 25) for t in range(25)]
        sage: cs = complex_cubic_spline(pts)
        sage: cs.derivative(2)
        (-0.0497765406583...+0.151095006434...j)
    """

class CCSpline:
    """
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
    def __init__(self, pts: Sequence[tuple[Num, Num]] | ArrayLike):
        """
        TESTS::

            sage: pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
            sage: cs = complex_cubic_spline(pts)
        """
    def derivative(self, t: Real) -> complex128:
        """
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
    def value(self, t: Real) -> complex128:
        """
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
