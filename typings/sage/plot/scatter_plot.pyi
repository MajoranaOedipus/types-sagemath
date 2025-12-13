from _typeshed import Incomplete
from sage.misc.decorators import options as options
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class ScatterPlot(GraphicPrimitive):
    """
    Scatter plot graphics primitive.

    Input consists of two lists/arrays of the same length, whose
    values give the horizontal and vertical coordinates of each
    point in the scatter plot.  Options may be passed in
    dictionary format.

    EXAMPLES::

        sage: from sage.plot.scatter_plot import ScatterPlot
        sage: ScatterPlot([0,1,2], [3.5,2,5.1], {'facecolor':'white', 'marker':'s'})
        Scatter plot graphics primitive on 3 data points
    """
    xdata: Incomplete
    ydata: Incomplete
    def __init__(self, xdata, ydata, options) -> None:
        """
        Scatter plot graphics primitive.

        EXAMPLES::

            sage: import numpy
            sage: from sage.plot.scatter_plot import ScatterPlot
            sage: ScatterPlot(numpy.array([0,1,2]), numpy.array([3.5,2,5.1]), {'facecolor':'white', 'marker':'s'})
            Scatter plot graphics primitive on 3 data points
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: s = scatter_plot([[0,1],[2,4],[3.2,6]])
            sage: d = s.get_minmax_data()
            sage: d['xmin']
            ...0.0...
            sage: d['ymin']
            ...1.0...
        """

def scatter_plot(datalist, **options):
    """
    Return a Graphics object of a scatter plot containing all points in
    the datalist.  Type ``scatter_plot.options`` to see all available
    plotting options.

    INPUT:

    - ``datalist`` -- list of tuples ``(x,y)``

    - ``alpha`` -- (default: 1)

    - ``markersize`` -- (default: 50)

    - ``marker`` -- the style of the markers (default: ``'o'``); see the
      documentation of :func:`plot` for the full list of markers

    - ``facecolor`` -- (default: ``'#fec7b8'``)

    - ``edgecolor`` -- (default: ``'black'``)

    - ``zorder`` -- (default: 5)

    EXAMPLES::

        sage: scatter_plot([[0,1],[2,2],[4.3,1.1]], marker='s')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        from sage.plot.scatter_plot import ScatterPlot
        S = scatter_plot([[0,1],[2,2],[4.3,1.1]], marker='s')
        sphinx_plot(S)

    Extra options will get passed on to :meth:`~Graphics.show`, as long as they are valid::

        sage: scatter_plot([(0, 0), (1, 1)], markersize=100, facecolor='green', ymax=100)
        Graphics object consisting of 1 graphics primitive
        sage: scatter_plot([(0, 0), (1, 1)], markersize=100, facecolor='green').show(ymax=100) # These are equivalent

    .. PLOT::

        from sage.plot.scatter_plot import ScatterPlot
        S = scatter_plot([(0, 0), (1, 1)], markersize=100, facecolor='green', ymax=100)
        sphinx_plot(S)
    """
