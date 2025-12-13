import _cython_3_2_1
from sage.arith.srange import srange as srange
from sage.calculus.integration import numerical_integral as numerical_integral
from sage.calculus.interpolation import spline as spline
from sage.categories.category import CDF as CDF
from sage.ext.fast_callable import fast_callable as fast_callable
from sage.misc.decorators import options as options
from typing import Any, Callable, ClassVar, overload

analytic_boundary: _cython_3_2_1.cython_function_or_method
analytic_interior: _cython_3_2_1.cython_function_or_method
cauchy_kernel: _cython_3_2_1.cython_function_or_method
complex_to_rgb: _cython_3_2_1.cython_function_or_method
complex_to_spiderweb: _cython_3_2_1.cython_function_or_method
get_derivatives: _cython_3_2_1.cython_function_or_method
pi: float

class Riemann_Map:
    '''Riemann_Map(fs, fprimes, double complex a, int N=500, int ncorners=4, opp=False, exterior=False)

    File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 70)

    The ``Riemann_Map`` class computes an interior or exterior Riemann map,
    or an Ahlfors map of a region given by the supplied boundary curve(s)
    and center point. The class also provides various methods to
    evaluate, visualize, or extract data from the map.

    A Riemann map conformally maps a simply connected region in
    the complex plane to the unit disc. The Ahlfors map does the same thing
    for multiply connected regions.

    Note that all the methods are numerical. As a result all answers have
    some imprecision. Moreover, maps computed with small number of
    collocation points, or for unusually shaped regions, may be very
    inaccurate. Error computations for the ellipse can be found in the
    documentation for :meth:`analytic_boundary` and :meth:`analytic_interior`.

    [BSV2010]_ provides an overview of the Riemann map and discusses the research
    that lead to the creation of this module.

    INPUT:

    - ``fs`` -- list of the boundaries of the region, given as
      complex-valued functions with domain `0` to `2*pi`. Note that the
      outer boundary must be parameterized counter clockwise
      (i.e. ``e^(I*t)``) while the inner boundaries must be clockwise
      (i.e. ``e^(-I*t)``).

    - ``fprimes`` -- list of the derivatives of the boundary functions
      (Must be in the same order as ``fs``)

    - ``a`` -- complex, the center of the Riemann map. Will be mapped to
      the origin of the unit disc. Note that ``a`` MUST be within
      the region in order for the results to be mathematically valid.

    The following inputs may be passed in as named parameters:

    - ``N`` -- integer (default: `500`); the number of collocation points
      used to compute the map. More points will give more accurate results,
      especially near the boundaries, but will take longer to compute.

    - ``exterior`` -- boolean (default: ``False``); if set to ``True``, the
      exterior map will be computed, mapping the exterior of the region to the
      exterior of the unit circle.

    The following inputs may be passed as named parameters in unusual
    circumstances:

    - ``ncorners`` -- integer (default: `4`); if mapping a figure with
      (equally t-spaced) corners -- corners that make a significant change in
      the direction of the boundary -- better results may be sometimes obtained by
      accurately giving this parameter. Used to add the proper constant to
      the theta correspondence function.

    - ``opp`` -- boolean (default: ``False``); set to ``True`` in very rare
      cases where the theta correspondence function is off by ``pi``, that
      is, if red is mapped left of the origin in the color plot.

    EXAMPLES:

    The unit circle identity map::

        sage: f(t) = e^(I*t)
        sage: fprime(t) = I*e^(I*t)
        sage: m = Riemann_Map([f], [fprime], 0)  # long time (4 sec)
        sage: m.plot_colored() + m.plot_spiderweb()  # long time
        Graphics object consisting of 22 graphics primitives

    The exterior map for the unit circle::

        sage: m = Riemann_Map([f], [fprime], 0, exterior=True)  # long time (4 sec)
        sage: #spiderwebs are not supported for exterior maps
        sage: m.plot_colored() # long time
        Graphics object consisting of 1 graphics primitive

    The unit circle with a small hole::

        sage: f(t) = e^(I*t)
        sage: fprime(t) = I*e^(I*t)
        sage: hf(t) = 0.5*e^(-I*t)
        sage: hfprime(t) = 0.5*-I*e^(-I*t)
        sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)
        sage: #spiderweb and color plots cannot be added for multiply
        sage: #connected regions. Instead we do this.
        sage: m.plot_spiderweb(withcolor = True)  # long time
        Graphics object consisting of 3 graphics primitives

    A square::

        sage: ps = polygon_spline([(-1, -1), (1, -1), (1, 1), (-1, 1)])
        sage: f = lambda t: ps.value(real(t))
        sage: fprime = lambda t: ps.derivative(real(t))
        sage: m = Riemann_Map([f], [fprime], 0.25, ncorners=4)
        sage: m.plot_colored() + m.plot_spiderweb()  # long time
        Graphics object consisting of 22 graphics primitives

    Compute rough error for this map::

        sage: x = 0.75  # long time
        sage: print("error = {}".format(m.inverse_riemann_map(m.riemann_map(x)) - x))  # long time
        error = (-0.000...+0.0016...j)

    A fun, complex region for demonstration purposes::

        sage: f(t) = e^(I*t)
        sage: fp(t) = I*e^(I*t)
        sage: ef1(t) = .2*e^(-I*t) +.4+.4*I
        sage: ef1p(t) = -I*.2*e^(-I*t)
        sage: ef2(t) = .2*e^(-I*t) -.4+.4*I
        sage: ef2p(t) = -I*.2*e^(-I*t)
        sage: pts = [(-.5,-.15-20/1000),(-.6,-.27-10/1000),(-.45,-.45),(0,-.65+10/1000),(.45,-.45),(.6,-.27-10/1000),(.5,-.15-10/1000),(0,-.43+10/1000)]
        sage: pts.reverse()
        sage: cs = complex_cubic_spline(pts)
        sage: mf = lambda x:cs.value(x)
        sage: mfprime = lambda x: cs.derivative(x)
        sage: m = Riemann_Map([f,ef1,ef2,mf],[fp,ef1p,ef2p,mfprime],0,N = 400) # long time
        sage: p = m.plot_colored(plot_points = 400) # long time

    ALGORITHM:

    This class computes the Riemann Map via the Szego kernel using an
    adaptation of the method described by [KT1986]_.'''
    plot_colored: ClassVar[Callable] = ...
    plot_spiderweb: ClassVar[Callable] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, fs, fprimes, doublecomplexa, intN=..., intncorners=..., opp=..., exterior=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 203)

                Initialize the ``Riemann_Map`` class. See the class :class:`Riemann_Map`
                for full documentation on the input of this initialization method.

                TESTS::

                    sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
                    sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
                    sage: m = Riemann_Map([f], [fprime], 0, N = 10)
        """
    def compute_on_grid(self, plot_range, intx_points) -> Any:
        """Riemann_Map.compute_on_grid(self, plot_range, int x_points)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 766)

        Compute the Riemann map on a grid of points.

        Note that these points are complex of the form z = x + y*i.

        INPUT:

        - ``plot_range`` -- tuple of the form ``[xmin, xmax, ymin, ymax]``;
          if the value is ``[]``, the default plotting window of the map will
          be used

        - ``x_points`` -- integer; the size of the grid in the x direction;
          the number of points in the y direction is scaled accordingly

        OUTPUT:

        - a tuple containing ``[z_values, xmin, xmax, ymin, ymax]``
          where ``z_values`` is the evaluation of the map on the specified grid.

        EXAMPLES:

        General usage::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: data = m.compute_on_grid([],5)
            sage: data[0][8,1]
            (-0.0879...+0.9709...j)"""
    @overload
    def get_szego(self, intboundary=..., absolute_value=...) -> Any:
        """Riemann_Map.get_szego(self, int boundary=-1, absolute_value=False)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 377)

        Return a discretized version of the Szego kernel for each boundary
        function.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          :meth:`get_theta_points` will return the points for all boundaries.
          If >= 0, :meth:`get_theta_points` will return only the points for
          the boundary specified.

        - ``absolute_value`` -- boolean (default: ``False``); if ``True``, will
          return the absolute value of the (complex valued) Szego kernel
          instead of the kernel itself. Useful for plotting.

        OUTPUT:

        A list of points of the form
        ``[t value, value of the Szego kernel at that t]``.

        EXAMPLES:

        Generic use::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: sz = m.get_szego(boundary=0)
            sage: points = m.get_szego(absolute_value=True)
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            0.0012158...
            sage: plot(s,0,2*pi)  # plot the kernel                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)

        Getting the szego for a specific boundary::

            sage: sz0 = m.get_szego(boundary=0)
            sage: sz1 = m.get_szego(boundary=1)"""
    @overload
    def get_szego(self, boundary=...) -> Any:
        """Riemann_Map.get_szego(self, int boundary=-1, absolute_value=False)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 377)

        Return a discretized version of the Szego kernel for each boundary
        function.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          :meth:`get_theta_points` will return the points for all boundaries.
          If >= 0, :meth:`get_theta_points` will return only the points for
          the boundary specified.

        - ``absolute_value`` -- boolean (default: ``False``); if ``True``, will
          return the absolute value of the (complex valued) Szego kernel
          instead of the kernel itself. Useful for plotting.

        OUTPUT:

        A list of points of the form
        ``[t value, value of the Szego kernel at that t]``.

        EXAMPLES:

        Generic use::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: sz = m.get_szego(boundary=0)
            sage: points = m.get_szego(absolute_value=True)
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            0.0012158...
            sage: plot(s,0,2*pi)  # plot the kernel                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)

        Getting the szego for a specific boundary::

            sage: sz0 = m.get_szego(boundary=0)
            sage: sz1 = m.get_szego(boundary=1)"""
    @overload
    def get_szego(self, absolute_value=...) -> Any:
        """Riemann_Map.get_szego(self, int boundary=-1, absolute_value=False)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 377)

        Return a discretized version of the Szego kernel for each boundary
        function.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          :meth:`get_theta_points` will return the points for all boundaries.
          If >= 0, :meth:`get_theta_points` will return only the points for
          the boundary specified.

        - ``absolute_value`` -- boolean (default: ``False``); if ``True``, will
          return the absolute value of the (complex valued) Szego kernel
          instead of the kernel itself. Useful for plotting.

        OUTPUT:

        A list of points of the form
        ``[t value, value of the Szego kernel at that t]``.

        EXAMPLES:

        Generic use::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: sz = m.get_szego(boundary=0)
            sage: points = m.get_szego(absolute_value=True)
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            0.0012158...
            sage: plot(s,0,2*pi)  # plot the kernel                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)

        Getting the szego for a specific boundary::

            sage: sz0 = m.get_szego(boundary=0)
            sage: sz1 = m.get_szego(boundary=1)"""
    @overload
    def get_szego(self, boundary=...) -> Any:
        """Riemann_Map.get_szego(self, int boundary=-1, absolute_value=False)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 377)

        Return a discretized version of the Szego kernel for each boundary
        function.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          :meth:`get_theta_points` will return the points for all boundaries.
          If >= 0, :meth:`get_theta_points` will return only the points for
          the boundary specified.

        - ``absolute_value`` -- boolean (default: ``False``); if ``True``, will
          return the absolute value of the (complex valued) Szego kernel
          instead of the kernel itself. Useful for plotting.

        OUTPUT:

        A list of points of the form
        ``[t value, value of the Szego kernel at that t]``.

        EXAMPLES:

        Generic use::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: sz = m.get_szego(boundary=0)
            sage: points = m.get_szego(absolute_value=True)
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            0.0012158...
            sage: plot(s,0,2*pi)  # plot the kernel                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)

        Getting the szego for a specific boundary::

            sage: sz0 = m.get_szego(boundary=0)
            sage: sz1 = m.get_szego(boundary=1)"""
    @overload
    def get_szego(self, boundary=...) -> Any:
        """Riemann_Map.get_szego(self, int boundary=-1, absolute_value=False)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 377)

        Return a discretized version of the Szego kernel for each boundary
        function.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          :meth:`get_theta_points` will return the points for all boundaries.
          If >= 0, :meth:`get_theta_points` will return only the points for
          the boundary specified.

        - ``absolute_value`` -- boolean (default: ``False``); if ``True``, will
          return the absolute value of the (complex valued) Szego kernel
          instead of the kernel itself. Useful for plotting.

        OUTPUT:

        A list of points of the form
        ``[t value, value of the Szego kernel at that t]``.

        EXAMPLES:

        Generic use::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: sz = m.get_szego(boundary=0)
            sage: points = m.get_szego(absolute_value=True)
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            0.0012158...
            sage: plot(s,0,2*pi)  # plot the kernel                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [fprime, hfprime], 0.5 + 0.5*I)

        Getting the szego for a specific boundary::

            sage: sz0 = m.get_szego(boundary=0)
            sage: sz1 = m.get_szego(boundary=1)"""
    @overload
    def get_theta_points(self, intboundary=...) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def get_theta_points(self) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def get_theta_points(self) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def get_theta_points(self) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def get_theta_points(self, boundary=...) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def get_theta_points(self, boundary=...) -> Any:
        """Riemann_Map.get_theta_points(self, int boundary=-1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 450)

        Return an array of points of the form
        ``[t value, theta in e^(I*theta)]``, that is, a discretized version
        of the theta/boundary correspondence function. In other words, a point
        in this array [t1, t2] represents that the boundary point given by f(t1)
        is mapped to a point on the boundary of the unit circle given by e^(I*t2).

        For multiply connected domains, ``get_theta_points`` will list the
        points for each boundary in the order that they were supplied.

        INPUT:

        The following input must all be passed in as named parameters:

        - ``boundary`` -- integer (default: `-1`); if < 0,
          ``get_theta_points()`` will return the points for all boundaries.
          If >= 0, ``get_theta_points()`` will return only the points for
          the boundary specified.

        OUTPUT:

        A list of points of the form ``[t value, theta in e^(I*theta)]``.

        EXAMPLES:

        Getting the list of points, extending it via a spline, getting the
        points for only the outside of a multiply connected domain::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: points = m.get_theta_points()
            sage: list_plot(points)                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Extending the points by a spline::

            sage: s = spline(points)
            sage: s(3*pi / 4)
            1.627660...

        The unit circle with a small hole::

            sage: f(t) = e^(I*t)
            sage: fprime(t) = I*e^(I*t)
            sage: hf(t) = 0.5*e^(-I*t)
            sage: hfprime(t) = 0.5*-I*e^(-I*t)
            sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)

        Getting the boundary correspondence for a specific boundary::

            sage: tp0 = m.get_theta_points(boundary=0)
            sage: tp1 = m.get_theta_points(boundary=1)"""
    @overload
    def inverse_riemann_map(self, doublecomplexpt) -> Any:
        """Riemann_Map.inverse_riemann_map(self, double complex pt)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 656)

        Return the inverse Riemann mapping of a point.

        That is, given ``pt`` on the interior of the unit disc,
        ``inverse_riemann_map()`` will return the point on the
        original region that would be Riemann mapped to ``pt``. Note
        that this method does not work for multiply connected domains.

        INPUT:

        - ``pt`` -- a complex number (usually with absolute value <= 1)
          representing the point to be inverse mapped

        OUTPUT: the point on the region that Riemann maps to the input point

        EXAMPLES:

        Can work for different types of complex numbers::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: m.inverse_riemann_map(0.5 + sqrt(-0.5))
            (0.406880...+0.3614702...j)
            sage: m.inverse_riemann_map(0.95)
            (0.486319...-4.90019052...j)
            sage: m.inverse_riemann_map(0.25 - 0.3*I)
            (0.1653244...-0.180936...j)
            sage: m.inverse_riemann_map(complex(-0.2, 0.5))
            (-0.156280...+0.321819...j)"""
    @overload
    def inverse_riemann_map(self) -> Any:
        """Riemann_Map.inverse_riemann_map(self, double complex pt)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 656)

        Return the inverse Riemann mapping of a point.

        That is, given ``pt`` on the interior of the unit disc,
        ``inverse_riemann_map()`` will return the point on the
        original region that would be Riemann mapped to ``pt``. Note
        that this method does not work for multiply connected domains.

        INPUT:

        - ``pt`` -- a complex number (usually with absolute value <= 1)
          representing the point to be inverse mapped

        OUTPUT: the point on the region that Riemann maps to the input point

        EXAMPLES:

        Can work for different types of complex numbers::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: m.inverse_riemann_map(0.5 + sqrt(-0.5))
            (0.406880...+0.3614702...j)
            sage: m.inverse_riemann_map(0.95)
            (0.486319...-4.90019052...j)
            sage: m.inverse_riemann_map(0.25 - 0.3*I)
            (0.1653244...-0.180936...j)
            sage: m.inverse_riemann_map(complex(-0.2, 0.5))
            (-0.156280...+0.321819...j)"""
    @overload
    def plot_boundaries(self, plotjoined=..., rgbcolor=..., thickness=...) -> Any:
        """Riemann_Map.plot_boundaries(self, plotjoined=True, rgbcolor=None, thickness=1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 707)

        Plot the boundaries of the region for the Riemann map.

        Note that this method DOES work for multiply connected domains.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``plotjoined`` -- boolean (default: ``True``); if ``False``,
          discrete points will be drawn; otherwise they will be connected
          by lines. In this case, if ``plotjoined=False``, the points shown
          will be the original collocation points used to generate the
          Riemann map.

        - ``rgbcolor`` -- float array (default: ``[0,0,0]``) the
          red-green-blue color of the boundary

        - ``thickness`` -- positive float (default: ``1``) the thickness of
          the lines or points in the boundary

        EXAMPLES:

        General usage::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)

        Default plot::

            sage: m.plot_boundaries()                                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Big blue collocation points::

            sage: m.plot_boundaries(plotjoined=False, rgbcolor=[0,0,1], thickness=6)    # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot_boundaries(self) -> Any:
        """Riemann_Map.plot_boundaries(self, plotjoined=True, rgbcolor=None, thickness=1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 707)

        Plot the boundaries of the region for the Riemann map.

        Note that this method DOES work for multiply connected domains.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``plotjoined`` -- boolean (default: ``True``); if ``False``,
          discrete points will be drawn; otherwise they will be connected
          by lines. In this case, if ``plotjoined=False``, the points shown
          will be the original collocation points used to generate the
          Riemann map.

        - ``rgbcolor`` -- float array (default: ``[0,0,0]``) the
          red-green-blue color of the boundary

        - ``thickness`` -- positive float (default: ``1``) the thickness of
          the lines or points in the boundary

        EXAMPLES:

        General usage::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)

        Default plot::

            sage: m.plot_boundaries()                                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Big blue collocation points::

            sage: m.plot_boundaries(plotjoined=False, rgbcolor=[0,0,1], thickness=6)    # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot_boundaries(self, plotjoined=..., rgbcolor=..., thickness=...) -> Any:
        """Riemann_Map.plot_boundaries(self, plotjoined=True, rgbcolor=None, thickness=1)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 707)

        Plot the boundaries of the region for the Riemann map.

        Note that this method DOES work for multiply connected domains.

        INPUT:

        The following inputs may be passed in as named parameters:

        - ``plotjoined`` -- boolean (default: ``True``); if ``False``,
          discrete points will be drawn; otherwise they will be connected
          by lines. In this case, if ``plotjoined=False``, the points shown
          will be the original collocation points used to generate the
          Riemann map.

        - ``rgbcolor`` -- float array (default: ``[0,0,0]``) the
          red-green-blue color of the boundary

        - ``thickness`` -- positive float (default: ``1``) the thickness of
          the lines or points in the boundary

        EXAMPLES:

        General usage::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)

        Default plot::

            sage: m.plot_boundaries()                                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Big blue collocation points::

            sage: m.plot_boundaries(plotjoined=False, rgbcolor=[0,0,1], thickness=6)    # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    def riemann_map(self, doublecomplexpt) -> Any:
        """Riemann_Map.riemann_map(self, double complex pt)

        File: /build/sagemath/src/sage/src/sage/calculus/riemann.pyx (starting at line 568)

        Return the Riemann mapping of a point.

        That is, given ``pt`` on the interior of the mapped region,
        ``riemann_map`` will return the point on the unit disk that
        ``pt`` maps to. Note that this method only works for interior
        points; accuracy breaks down very close to the boundary. To
        get boundary correspondence, use :meth:`get_theta_points`.

        INPUT:

        - ``pt`` -- a complex number representing the point to be
          inverse mapped

        OUTPUT:

        A complex number representing the point on the unit circle that
        the input point maps to.

        EXAMPLES:

        Can work for different types of complex numbers::

            sage: f(t) = e^(I*t) - 0.5*e^(-I*t)
            sage: fprime(t) = I*e^(I*t) + 0.5*I*e^(-I*t)
            sage: m = Riemann_Map([f], [fprime], 0)
            sage: m.riemann_map(0.25 + sqrt(-0.5))
            (0.137514...+0.876696...j)
            sage: I = CDF.gen()
            sage: m.riemann_map(1.3*I)
            (-1.56...e-05+0.989694...j)
            sage: m.riemann_map(0.4)
            (0.73324...+3.2...e-06j)
            sage: m.riemann_map(complex(-3, 0.0001))
            (1.405757...e-05+8.06...e-10j)"""
