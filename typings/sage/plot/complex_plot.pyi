import _cython_3_2_1
import sage.plot.primitive
from sage.arith.srange import srange as srange
from sage.misc.decorators import options as options
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, Callable, overload

DEFAULT_LINEAR_CONTOUR_BASE: int
DEFAULT_LOGARITHMIC_CONTOUR_BASE: int
add_contours_to_rgb: _cython_3_2_1.cython_function_or_method
add_lightness_smoothing_to_rgb: _cython_3_2_1.cython_function_or_method
complex_plot: Callable
complex_to_cmap_rgb: _cython_3_2_1.cython_function_or_method
complex_to_rgb: _cython_3_2_1.cython_function_or_method
hls_to_rgb: _cython_3_2_1.cython_function_or_method
rgb_to_hls: _cython_3_2_1.cython_function_or_method

class ComplexPlot(sage.plot.primitive.GraphicPrimitive):
    """File: /build/sagemath/src/sage/src/sage/plot/complex_plot.pyx (starting at line 766)

        The GraphicsPrimitive to display complex functions in using the domain
        coloring method

        INPUT:

        - ``rgb_data`` -- an array of colored points to be plotted

        - ``x_range`` -- a minimum and maximum x value for the plot

        - ``y_range`` -- a minimum and maximum y value for the plot

        TESTS::

            sage: p = complex_plot(lambda z: z^2-1, (-2, 2), (-2, 2))
    """
    def __init__(self, rgb_data, x_range, y_range, options) -> Any:
        """ComplexPlot.__init__(self, rgb_data, x_range, y_range, options)

        File: /build/sagemath/src/sage/src/sage/plot/complex_plot.pyx (starting at line 783)

        TESTS::

            sage: p = complex_plot(lambda z: z^2-1, (-2, 2), (-2, 2))"""
    @overload
    def get_minmax_data(self) -> Any:
        """ComplexPlot.get_minmax_data(self)

        File: /build/sagemath/src/sage/src/sage/plot/complex_plot.pyx (starting at line 796)

        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: p = complex_plot(lambda z: z, (-1, 2), (-3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', -1.0), ('ymax', 4.0), ('ymin', -3.0)]
            sage: p = complex_plot(lambda z: z, (1, 2), (3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', 1.0), ('ymax', 4.0), ('ymin', 3.0)]"""
    @overload
    def get_minmax_data(self) -> Any:
        """ComplexPlot.get_minmax_data(self)

        File: /build/sagemath/src/sage/src/sage/plot/complex_plot.pyx (starting at line 796)

        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: p = complex_plot(lambda z: z, (-1, 2), (-3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', -1.0), ('ymax', 4.0), ('ymin', -3.0)]
            sage: p = complex_plot(lambda z: z, (1, 2), (3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', 1.0), ('ymax', 4.0), ('ymin', 3.0)]"""
    @overload
    def get_minmax_data(self) -> Any:
        """ComplexPlot.get_minmax_data(self)

        File: /build/sagemath/src/sage/src/sage/plot/complex_plot.pyx (starting at line 796)

        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: p = complex_plot(lambda z: z, (-1, 2), (-3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', -1.0), ('ymax', 4.0), ('ymin', -3.0)]
            sage: p = complex_plot(lambda z: z, (1, 2), (3, 4))
            sage: sorted(p.get_minmax_data().items())
            [('xmax', 2.0), ('xmin', 1.0), ('ymax', 4.0), ('ymin', 3.0)]"""
