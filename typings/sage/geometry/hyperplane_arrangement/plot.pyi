from sage.misc.lazy_import import lazy_import as lazy_import

def plot(hyperplane_arrangement, **kwds):
    """
    Return a plot of the hyperplane arrangement.

    If the arrangement is in 4 dimensions but inessential, a plot of
    the essentialization is returned.

    .. NOTE::

        This function is available as the
        :meth:`~sage.geometry.hyperplane_arrangement.arrangement.HyperplaneArrangementElement.plot`
        method of hyperplane arrangements. You should not call this
        function directly, only through the method.

    INPUT:

    - ``hyperplane_arrangement`` -- the hyperplane arrangement to plot

    - ``**kwds`` -- plot options: see
      :mod:`sage.geometry.hyperplane_arrangement.plot`

    OUTPUT: a graphics object of the plot

    EXAMPLES::

        sage: B = hyperplane_arrangements.semiorder(4)
        sage: B.plot()                                                                  # needs sage.combinat sage.plot
        Displaying the essentialization.
        Graphics3d Object
    """
def plot_hyperplane(hyperplane, **kwds):
    """
    Return the plot of a single hyperplane.

    INPUT:

    - ``**kwds`` -- plot options: see below

    OUTPUT: a graphics object of the plot

    .. RUBRIC:: Plot Options

    Beside the usual plot options (enter ``plot?``), the plot command for
    hyperplanes includes the following:

    - ``hyperplane_label`` -- boolean value or string (default: ``True``);
      if ``True``, the hyperplane is labeled with its equation, if a
      string, it is labeled by that string, otherwise it is not
      labeled

    - ``label_color`` -- (default: ``'black'``) color for hyperplane_label

    - ``label_fontsize`` -- size for ``hyperplane_label`` font (default: 14)
      (does not work in 3d, yet)

    - ``label_offset`` -- (default: 0-dim: 0.1, 1-dim: (0,1),
      2-dim: (0,0,0.2)); amount by which label is offset from
      ``hyperplane.point()``

    - ``point_size`` -- (default: 50) size of points in a zero-dimensional
      arrangement or of an arrangement over a finite field

    - ``ranges`` -- range for the parameters for the parametric plot of the
      hyperplane. If a single positive number ``r`` is given for the
      value of ``ranges``, then the ranges for all parameters are set to
      `[-r, r]`.  Otherwise, for a line in the plane, ``ranges`` has the
      form ``[a, b]`` (default: [-3,3]), and for a plane in 3-space, the
      ``ranges`` has the form ``[[a, b], [c, d]]`` (default: [[-3,3],[-3,3]]).
      (The ranges are centered around ``hyperplane.point()``.)

    EXAMPLES::

        sage: H1.<x> = HyperplaneArrangements(QQ)
        sage: a = 3*x + 4
        sage: a.plot()    # indirect doctest                                            # needs sage.plot
        Graphics object consisting of 3 graphics primitives
        sage: a.plot(point_size=100, hyperplane_label='hello')                          # needs sage.plot
        Graphics object consisting of 3 graphics primitives

        sage: H2.<x,y> = HyperplaneArrangements(QQ)
        sage: b = 3*x + 4*y + 5
        sage: b.plot()                                                                  # needs sage.plot
        Graphics object consisting of 2 graphics primitives
        sage: b.plot(ranges=(1,5), label_offset=(2,-1))                                 # needs sage.plot
        Graphics object consisting of 2 graphics primitives
        sage: opts = {'hyperplane_label': True, 'label_color': 'green',
        ....:         'label_fontsize': 24, 'label_offset': (0,1.5)}
        sage: b.plot(**opts)                                                            # needs sage.plot
        Graphics object consisting of 2 graphics primitives

        sage: # needs sage.plot
        sage: H3.<x,y,z> = HyperplaneArrangements(QQ)
        sage: c = 2*x + 3*y + 4*z + 5
        sage: c.plot()
        Graphics3d Object
        sage: c.plot(label_offset=(1,0,1), color='green', label_color='red',
        ....:        frame=False)
        Graphics3d Object
        sage: d = -3*x + 2*y + 2*z + 3
        sage: d.plot(opacity=0.8)
        Graphics3d Object
        sage: e = 4*x + 2*z + 3
        sage: e.plot(ranges=[[-1,1],[0,8]], label_offset=(2,2,1), aspect_ratio=1)
        Graphics3d Object
    """
def legend_3d(hyperplane_arrangement, hyperplane_colors, length):
    """
    Create plot of a 3d legend for an arrangement of planes in 3-space.

    The ``length`` parameter determines whether short or long labels
    are used in the legend.

    INPUT:

    - ``hyperplane_arrangement`` -- a hyperplane arrangement

    - ``hyperplane_colors`` -- list of colors

    - ``length`` -- either ``'short'`` or ``'long'``

    OUTPUT: a graphics object

    EXAMPLES::

        sage: a = hyperplane_arrangements.semiorder(3)
        sage: from sage.geometry.hyperplane_arrangement.plot import legend_3d
        sage: legend_3d(a, list(colors.values())[:6], length='long')                    # needs sage.combinat sage.plot
        Graphics object consisting of 6 graphics primitives

        sage: b = hyperplane_arrangements.semiorder(4)
        sage: c = b.essentialization()
        sage: legend_3d(c, list(colors.values())[:12], length='long')                   # needs sage.combinat sage.plot
        Graphics object consisting of 12 graphics primitives

        sage: legend_3d(c, list(colors.values())[:12], length='short')                  # needs sage.combinat sage.plot
        Graphics object consisting of 12 graphics primitives

        sage: p = legend_3d(c, list(colors.values())[:12], length='short')              # needs sage.combinat sage.plot
        sage: p.set_legend_options(ncol=4)                                              # needs sage.combinat sage.plot
        sage: type(p)                                                                   # needs sage.combinat sage.plot
        <class 'sage.plot.graphics.Graphics'>
    """
