from _typeshed import Incomplete
from sage.misc.decorators import options as options
from sage.plot.plot import Graphics as Graphics, minmax_data as minmax_data
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class Histogram(GraphicPrimitive):
    """
    Graphics primitive that represents a histogram.  This takes
    quite a few options as well.

    EXAMPLES::

        sage: from sage.plot.histogram import Histogram
        sage: g = Histogram([1,3,2,0], {}); g
        Histogram defined by a data list of size 4
        sage: type(g)
        <class 'sage.plot.histogram.Histogram'>
        sage: opts = { 'bins':20, 'label':'mydata'}
        sage: g = Histogram([random() for _ in range(500)], opts); g
        Histogram defined by a data list of size 500

    We can accept multiple sets of the same length::

        sage: g = Histogram([[1,3,2,0], [4,4,3,3]], {}); g
        Histogram defined by 2 data lists
    """
    datalist: Incomplete
    def __init__(self, datalist, options) -> None:
        """
        Initialize a ``Histogram`` primitive along with
        its options.

        EXAMPLES::

            sage: from sage.plot.histogram import Histogram
            sage: Histogram([10,3,5], {'width':0.7})
            Histogram defined by a data list of size 3
        """
    def get_minmax_data(self):
        """
        Get minimum and maximum horizontal and vertical ranges
        for the Histogram object.

        EXAMPLES::

            sage: H = histogram([10,3,5], density=True); h = H[0]
            sage: h.get_minmax_data()  # rel tol 1e-15
            {'xmax': 10.0, 'xmin': 3.0, 'ymax': 0.4761904761904765, 'ymin': 0}
            sage: G = histogram([random() for _ in range(500)]); g = G[0]
            sage: g.get_minmax_data() # random output
            {'xmax': 0.99729312925213209, 'xmin': 0.00013024562219410285, 'ymax': 61, 'ymin': 0}
            sage: Y = histogram([random()*10 for _ in range(500)], range=[2,8]); y = Y[0]
            sage: ymm = y.get_minmax_data(); ymm['xmax'], ymm['xmin']
            (8.0, 2.0)
            sage: Z = histogram([[1,3,2,0], [4,4,3,3]]); z = Z[0]
            sage: z.get_minmax_data()
            {'xmax': 4.0, 'xmin': 0, 'ymax': 2, 'ymin': 0}

        TESTS::

            sage: h = histogram([10,3,5], density=True)[0]
            sage: h.get_minmax_data()
            {'xmax': 10.0, 'xmin': 3.0, 'ymax': 0.476190476190..., 'ymin': 0}
        """

def histogram(datalist, **options):
    '''
    Compute and draw the histogram for list(s) of numerical data.
    See examples for the many options; even more customization is
    available using matplotlib directly.

    INPUT:

    - ``datalist`` -- list, or a list of lists, of numerical data
    - ``align`` -- (default: ``\'mid\'``) how the bars align inside of each bin.
      Acceptable values are ``\'left\'`` ``\'right\'`` or ``\'mid\'``
    - ``alpha`` -- (float in [0,1], default: 1) The transparency of the plot
    - ``bins`` -- the number of sections in which to divide the range. Also
      can be a sequence of points within the range that create the
      partition
    - ``color`` -- the color of the face of the bars or list of colors if
      multiple data sets are given
    - ``cumulative`` -- boolean (default: ``False``); if True, then
      a histogram is computed in which each bin gives the counts in that
      bin plus all bins for smaller values.  Negative values give
      a reversed direction of accumulation
    - ``edgecolor`` -- the color of the border of each bar
    - ``fill`` -- boolean (default: ``True``); whether to fill the bars
    - ``hatch`` -- (default: ``None``) symbol to fill the bars with; one of
      "/", "\\", "|", "-", "+", "x", "o", "O", ".", "*", "" (or None)
    - ``hue`` -- the color of the bars given as a hue. See
      :mod:`~sage.plot.colors.hue` for more information on the hue
    - ``label`` -- string label for each data list given
    - ``linewidth`` -- (float) width of the lines defining the bars
    - ``linestyle`` -- (default: ``\'solid\'``) style of the line. One of \'solid\'
      or \'-\', \'dashed\' or \'--\', \'dotted\' or \':\', \'dashdot\' or \'-.\'
    - ``density`` -- boolean (default: ``False``); if True, the result is the
      value of the probability density function at the bin, normalized such
      that the integral over the range is 1.
    - ``range`` -- list [min, max] which define the range of the
      histogram. Values outside of this range are treated as outliers and
      omitted from counts
    - ``rwidth`` -- (float in [0,1], default: 1) The relative width of the bars
      as a fraction of the bin width
    - ``stacked`` -- boolean (default: ``False``); if True, multiple data are
      stacked on top of each other
    - ``weights`` -- (list) A sequence of weights the same length as the data
      list. If supplied, then each value contributes its associated weight
      to the bin count
    - ``zorder`` -- integer; the layer level at which to draw the histogram

    .. NOTE::

        The ``weights`` option works only with a single list. List of lists
        representing multiple data are not supported.

    EXAMPLES:

    A very basic histogram for four data points::

        sage: histogram([1, 2, 3, 4], bins=2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(histogram([1, 2, 3, 4], bins=2))

    We can see how the histogram compares to various distributions.
    Note the use of the ``density`` keyword to guarantee the plot
    looks like the probability density function::

        sage: nv = normalvariate
        sage: H = histogram([nv(0, 1) for _ in range(1000)], bins=20, density=True, range=[-5, 5])
        sage: P = plot(1/sqrt(2*pi)*e^(-x^2/2), (x, -5, 5), color=\'red\', linestyle=\'--\')            # needs sage.symbolic
        sage: H + P                                                                     # needs sage.symbolic
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        nv = normalvariate
        H = histogram([nv(0, 1) for _ in range(1000)], bins=20, density=True, range=[-5,5 ])
        P = plot(1/sqrt(2*pi)*e**(-x**2/2), (x, -5, 5), color=\'red\', linestyle=\'--\')
        sphinx_plot(H+P)

    There are many options one can use with histograms.  Some of these
    control the presentation of the data, even if it is boring::

        sage: histogram(list(range(100)), color=(1,0,0), label=\'mydata\', rwidth=.5, align=\'right\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(histogram(list(range(100)), color=(1,0,0), label=\'mydata\', rwidth=.5, align=\'right\'))

    This includes many usual matplotlib styling options::

        sage: T = RealDistribution(\'lognormal\', [0, 1])
        sage: histogram( [T.get_random_element() for _ in range(100)], alpha=0.3, edgecolor=\'red\', fill=False, linestyle=\'dashed\', hatch=\'O\', linewidth=5)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        T = RealDistribution(\'lognormal\', [0, 1])
        H = histogram( [T.get_random_element() for _ in range(100)], alpha=0.3, edgecolor=\'red\', fill=False, linestyle=\'dashed\', hatch=\'O\', linewidth=5)
        sphinx_plot(H)

    ::

        sage: histogram( [T.get_random_element() for _ in range(100)],linestyle=\'-.\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        T = RealDistribution(\'lognormal\', [0, 1])
        sphinx_plot(histogram( [T.get_random_element() for _ in range(100)],linestyle=\'-.\'))

    We can do several data sets at once if desired::

        sage: histogram([srange(0, 1, .1)*10, [nv(0, 1) for _ in range(100)]], color=[\'red\', \'green\'], bins=5)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        nv = normalvariate
        sphinx_plot(histogram([srange(0, 1, .1)*10, [nv(0, 1) for _ in range(100)]], color=[\'red\', \'green\'], bins=5))

    We have the option of stacking the data sets too::

        sage: histogram([[1, 1, 1, 1, 2, 2, 2, 3, 3, 3], [4, 4, 4, 4, 3, 3, 3, 2, 2, 2] ], stacked=True, color=[\'blue\', \'red\'])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(histogram([[1, 1, 1, 1, 2, 2, 2, 3, 3, 3], [4, 4, 4, 4, 3, 3, 3, 2, 2, 2] ], stacked=True, color=[\'blue\', \'red\']))

    It is possible to use weights with the histogram as well::

        sage: histogram(list(range(10)), bins=3, weights=[1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(histogram(list(range(10)), bins=3, weights=[1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
    '''
