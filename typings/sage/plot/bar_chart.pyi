from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.graphics import Graphics as Graphics
from sage.plot.plot import minmax_data as minmax_data
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class BarChart(GraphicPrimitive):
    """
    Graphics primitive that represents a bar chart.

    EXAMPLES::

        sage: from sage.plot.bar_chart import BarChart
        sage: g = BarChart(list(range(4)), [1,3,2,0], {}); g
        BarChart defined by a 4 datalist
        sage: type(g)
        <class 'sage.plot.bar_chart.BarChart'>
    """
    datalist: Incomplete
    ind: Incomplete
    def __init__(self, ind, datalist, options) -> None:
        """
        Initialize a ``BarChart`` primitive.

        EXAMPLES::

            sage: from sage.plot.bar_chart import BarChart
            sage: BarChart(list(range(3)), [10,3,5], {'width':0.7})
            BarChart defined by a 3 datalist
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: b = bar_chart([-2.3,5,-6,12])
            sage: d = b.get_minmax_data()
            sage: d['xmin']
            0
            sage: d['xmax']
            4
        """

def bar_chart(datalist, **options):
    """
    A bar chart of (currently) one list of numerical data.
    Support for more data lists in progress.

    EXAMPLES:

    A bar_chart with blue bars::

        sage: bar_chart([1,2,3,4])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(bar_chart([1,2,3,4]))

    A bar_chart with thinner bars::

        sage: bar_chart([x^2 for x in range(1,20)], width=0.2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(bar_chart([x**2 for x in range(1,20)], width=0.2))

    A bar_chart with negative values and red bars::

        sage: bar_chart([-3,5,-6,11], rgbcolor=(1,0,0))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(bar_chart([-3,5,-6,11], rgbcolor=(1,0,0)))

    A bar chart with a legend (it's possible, not necessarily useful)::

        sage: bar_chart([-1,1,-1,1], legend_label='wave')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(bar_chart([-1,1,-1,1], legend_label='wave'))

    Extra options will get passed on to show(), as long as they are valid::

        sage: bar_chart([-2,8,-7,3], rgbcolor=(1,0,0), axes=False)
        Graphics object consisting of 1 graphics primitive
        sage: bar_chart([-2,8,-7,3], rgbcolor=(1,0,0)).show(axes=False) # These are equivalent

    .. PLOT::

        sphinx_plot(bar_chart([-2,8,-7,3], rgbcolor=(1,0,0), axes=False))
    """
