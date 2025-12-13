from .colors import rgbcolor as rgbcolor
from _typeshed import Incomplete
from sage.misc.decorators import suboptions as suboptions
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.structure.sage_object import SageObject as SageObject

ALLOWED_EXTENSIONS: Incomplete
DEFAULT_DPI: int
do_verify: bool

def is_Graphics(x):
    """
    Return ``True`` if `x` is a Graphics object.

    EXAMPLES::

        sage: from sage.plot.graphics import is_Graphics
        sage: is_Graphics(1)
        doctest:warning...
        DeprecationWarning: The function is_Graphics is deprecated;
        use 'isinstance(..., Graphics)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        False
        sage: is_Graphics(disk((0.0, 0.0), 1, (0, pi/2)))                               # needs sage.symbolic
        True
    """

class Graphics(WithEqualityById, SageObject):
    """
    The Graphics object is an empty list of graphics objects. It is
    useful to use this object when initializing a for loop where
    different graphics object will be added to the empty object.

    EXAMPLES::

        sage: G = Graphics(); print(G)
        Graphics object consisting of 0 graphics primitives
        sage: c = circle((1,1), 1)
        sage: G += c; print(G)
        Graphics object consisting of 1 graphics primitive

    Here we make a graphic of embedded isosceles triangles, coloring
    each one with a different color as we go::

        sage: h = 10; c = 0.4; p = 0.5
        sage: G = Graphics()
        sage: for x in srange(1, h+1):                                                  # needs sage.symbolic
        ....:     l = [[0,x*sqrt(3)],[-x/2,-x*sqrt(3)/2],[x/2,-x*sqrt(3)/2],[0,x*sqrt(3)]]
        ....:     G += line(l, color=hue(c + p*(x/h)))
        sage: G.show(figsize=[5,5])                                                     # needs sage.symbolic

    We can change the scale of the axes in the graphics before displaying.::

        sage: G = plot(exp, 1, 10)              # long time                             # needs sage.symbolic
        sage: G.show(scale='semilogy')          # long time                             # needs sage.symbolic

    TESTS:

    From :issue:`4604`, ensure Graphics can handle 3d objects::

        sage: g = Graphics()
        sage: g += sphere((1, 1, 1), 2)
        sage: g.show()

    We check that graphics can be pickled (we can't use equality on
    graphics so we just check that the load/dump cycle gives a
    :class:`Graphics` instance)::

        sage: g = Graphics()
        sage: g2 = loads(dumps(g))
        sage: g2.show()

    ::

        sage: isinstance(g2, Graphics)
        True

        sage: hash(Graphics()) # random
        42

    .. automethod:: _rich_repr_
    """
    def __init__(self) -> None:
        """
        Create a new empty Graphics objects with all the defaults.

        EXAMPLES::

            sage: G = Graphics()
        """
    def set_aspect_ratio(self, ratio) -> None:
        """
        Set the aspect ratio, which is the ratio of height and width
        of a unit square (i.e., height/width of a unit square), or
        'automatic' (expand to fill the figure).

        INPUT:

        - ``ratio`` -- a positive real number or 'automatic'

        EXAMPLES: We create a plot of the upper half of a circle, but it
        doesn't look round because the aspect ratio is off::

            sage: P = plot(sqrt(1-x^2),(x,-1,1)); P                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        So we set the aspect ratio and now it is round::

            sage: P.set_aspect_ratio(1)                                                 # needs sage.symbolic
            sage: P.aspect_ratio()                                                      # needs sage.symbolic
            1.0
            sage: P                                                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Note that the aspect ratio is inherited upon addition (which takes
        the max of aspect ratios of objects whose aspect ratio has been
        set)::

            sage: P + plot(sqrt(4-x^2),(x,-2,2))                                        # needs sage.symbolic
            Graphics object consisting of 2 graphics primitives

        In the following example, both plots produce a circle that looks
        twice as tall as wide::

            sage: Q = circle((0,0), 0.5); Q.set_aspect_ratio(2)
            sage: (P + Q).aspect_ratio(); P + Q                                         # needs sage.symbolic
            2.0
            Graphics object consisting of 2 graphics primitives
            sage: (Q + P).aspect_ratio(); Q + P                                         # needs sage.symbolic
            2.0
            Graphics object consisting of 2 graphics primitives
        """
    def aspect_ratio(self):
        """
        Get the current aspect ratio, which is the ratio of height to
        width of a unit square, or ``'automatic'``.

        OUTPUT: a positive float (height/width of a unit square), or ``'automatic'``
        (expand to fill the figure).

        EXAMPLES:

        The default aspect ratio for a new blank :class:`Graphics` object is ``'automatic'``::

            sage: P = Graphics()
            sage: P.aspect_ratio()
            'automatic'

        The aspect ratio can be explicitly set different from the object's default::

            sage: P = circle((1,1), 1)
            sage: P.aspect_ratio()
            1.0
            sage: P.set_aspect_ratio(2)
            sage: P.aspect_ratio()
            2.0
            sage: P.set_aspect_ratio('automatic')
            sage: P.aspect_ratio()
            'automatic'
        """
    def legend(self, show=None):
        """
        Set whether or not the legend is shown by default.

        INPUT:

        - ``show`` -- (default: ``None``) a boolean

        If called with no input, return the current legend setting.

        EXAMPLES:

        By default no legend is displayed::

            sage: P = plot(sin)                                                         # needs sage.symbolic
            sage: P.legend()                                                            # needs sage.symbolic
            False

        But if we put a label then the legend is shown::

            sage: P = plot(sin, legend_label='sin')                                     # needs sage.symbolic
            sage: P.legend()                                                            # needs sage.symbolic
            True

        We can turn it on or off::

            sage: # needs sage.symbolic
            sage: P.legend(False)
            sage: P.legend()
            False
            sage: P.legend(True)
            sage: P  # show with the legend
            Graphics object consisting of 1 graphics primitive
        """
    def set_legend_options(self, **kwds):
        """
        Set various legend options.

        INPUT:

        - ``title`` -- (default: ``None``) string, the legend title

        - ``ncol`` -- (default: 1) positive integer, the number of columns

        - ``columnspacing`` -- (default: ``None``) the spacing between columns

        - ``borderaxespad`` -- (default: ``None``) float, length between the axes and the legend

        - ``back_color`` -- (default: ``'white'``) this parameter can be a string
          denoting a color or an RGB tuple. The string can be a color name
          as in ('red', 'green', 'yellow', ...) or a floating point number
          like '0.8' which gets expanded to (0.8, 0.8, 0.8). The
          tuple form is just a floating point RGB tuple with all values ranging
          from 0 to 1.

        - ``handlelength`` -- (default: 0.05) float, the length of the legend handles

        - ``handletextpad`` -- (default: 0.5) float, the pad between the legend handle and text

        - ``labelspacing`` -- (default: 0.02) float, vertical space between legend entries

        - ``loc`` -- (default: ``'best'``) may be a string, an integer or a tuple. String or
              integer inputs must be one of the following:

          - 0, 'best'

          - 1, 'upper right'

          - 2, 'upper left'

          - 3, 'lower left'

          - 4, 'lower right'

          - 5, 'right'

          - 6, 'center left'

          - 7, 'center right'

          - 8, 'lower center'

          - 9, 'upper center'

          - 10, 'center'

          - Tuple arguments represent an absolute (x, y) position on the plot
            in axes coordinates (meaning from 0 to 1 in each direction).

        - ``markerscale`` -- (default: 0.6) float, how much to scale the markers in the legend

        - ``numpoints`` -- (default: 2) integer, the number of points in the legend for line

        - ``borderpad`` -- (default: 0.6) float, the fractional whitespace inside the legend border
          (between 0 and 1)

        - ``font_family`` -- (default: ``'sans-serif'``) string, one of
          ``'serif'``, ``'sans-serif'``, ``'cursive'``, ``'fantasy'``,
          ``'monospace'``

        - ``font_style`` -- (default: ``'normal'``) string, one of
          ``'normal'``, ``'italic'``, ``'oblique'``

        - ``font_variant`` -- (default: ``'normal'``) string, one of
          ``'normal'``, ``'small-caps'``

        - ``font_weight`` -- (default: ``'medium'``) string, one of
          ``'black'``, ``'extra bold'``, ``'bold'``, ``'semibold'``,
          ``'medium'``, ``'normal'``, ``'light'``

        - ``font_size`` -- (default: ``'medium'``) string, one of
          ``'xx-small'``, ``'x-small'``, ``'small'``, ``'medium'``,
          ``'large'``, ``'x-large'``, ``'xx-large'``, or an absolute font size
          (e.g. 12)

        - ``shadow`` -- boolean (default: ``True``); draw a shadow behind the legend

        - ``fancybox`` -- boolean (default: ``False``); if
          ``True``, draws a frame with a round fancybox

        These are all keyword arguments.

        OUTPUT: a dictionary of all current legend options

        EXAMPLES:

        By default, no options are set::

            sage: p = plot(tan, legend_label='tan')                                     # needs sage.symbolic
            sage: p.set_legend_options()                                                # needs sage.symbolic
            {}

        We build a legend without a shadow::

            sage: p.set_legend_options(shadow=False)                                    # needs sage.symbolic
            sage: p.set_legend_options()['shadow']                                      # needs sage.symbolic
            False

        To set the legend position to the center of the plot, all these
        methods are roughly equivalent::

            sage: p.set_legend_options(loc='center'); p                                 # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        ::

            sage: p.set_legend_options(loc=10); p                                       # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        ::

            sage: p.set_legend_options(loc=(0.5,0.5)); p  # aligns the bottom of the box to the center                # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        The parameters ``loc`` and ``borderaxespad`` can be altered
        in order to place the legend below the x-axis label or to
        the left of the y-axis label::

            sage: p = line([(0, 0), (1, 1)], legend_label='test')
            sage: p.axes_labels(['X-Label', 'Y-Label'])  # adding labels for axes
            sage: p.set_legend_options(loc=8, borderaxespad=-7.5-0.01*p.fontsize())
            sage: p
            Graphics object consisting of 1 graphics primitive
        """
    def get_axes_range(self):
        """
        Return a dictionary of the range of the axes for this graphics
        object.  This is fall back to the ranges in ``get_minmax_data()`` for
        any value which the user has not explicitly set.

        .. warning::

           Changing the dictionary returned by this function does not
           change the axes range for this object.  To do that, use the
           :meth:`set_axes_range` method.

        EXAMPLES::

            sage: L = line([(1,2), (3,-4), (2, 5), (1,2)])
            sage: list(sorted(L.get_axes_range().items()))
            [('xmax', 3.0), ('xmin', 1.0), ('ymax', 5.0), ('ymin', -4.0)]
            sage: L.set_axes_range(xmin=-1)
            sage: list(sorted(L.get_axes_range().items()))
            [('xmax', 3.0), ('xmin', -1.0), ('ymax', 5.0), ('ymin', -4.0)]
        """
    def set_axes_range(self, xmin=None, xmax=None, ymin=None, ymax=None) -> None:
        """
        Set the ranges of the `x` and `y` axes.

        INPUT:

        - ``xmin``, ``xmax``, ``ymin``, ``ymax`` -- floats

        EXAMPLES::

            sage: L = line([(1,2), (3,-4), (2, 5), (1,2)])
            sage: L.set_axes_range(-1, 20, 0, 2)
            sage: d = L.get_axes_range()
            sage: d['xmin'], d['xmax'], d['ymin'], d['ymax']
            (-1.0, 20.0, 0.0, 2.0)
        """
    axes_range = set_axes_range
    def set_flip(self, flip_x=None, flip_y=None) -> None:
        """
        Set the flip options for this graphics object.

        INPUT:

        - ``flip_x`` -- boolean (default: ``None``); if not ``None``, set the
          ``flip_x`` option to this value
        - ``flip_y`` -- boolean (default: ``None``); if not ``None``, set the
          ``flip_y`` option to this value

        EXAMPLES::

            sage: L = line([(1, 0), (2, 3)])
            sage: L.set_flip(flip_y=True)
            sage: L.flip()
            (False, True)
            sage: L.set_flip(True, False)
            sage: L.flip()
            (True, False)
        """
    def flip(self, flip_x: bool = False, flip_y: bool = False):
        """
        Get the flip options and optionally mirror this graphics object.

        INPUT:

        - ``flip_x`` -- boolean (default: ``False``); if ``True``, replace the
          current ``flip_x`` option by its opposite
        - ``flip_y`` -- boolean (default: ``False``); if ``True``, replace the
          current ``flip_y`` option by its opposite

        OUTPUT: a tuple containing the new flip options

        EXAMPLES:

        When called without arguments, this just returns the current flip
        options::

            sage: L = line([(1, 0), (2, 3)])
            sage: L.flip()
            (False, False)

        Otherwise, the specified options are changed and the new options are
        returned::

            sage: L.flip(flip_y=True)
            (False, True)
            sage: L.flip(True, True)
            (True, False)
        """
    def fontsize(self, s=None):
        """
        Set the font size of axes labels and tick marks.

        Note that the relative size of the axes labels font w.r.t. the tick
        marks font can be adjusted via :meth:`axes_labels_size`.

        INPUT:

        - ``s`` -- integer, a font size in points


        If called with no input, return the current fontsize.

        EXAMPLES::

            sage: L = line([(1,2), (3,-4), (2, 5), (1,2)])
            sage: L.fontsize()
            10
            sage: L.fontsize(20)
            sage: L.fontsize()
            20

        All the numbers on the axes will be very large in this plot::

            sage: L
            Graphics object consisting of 1 graphics primitive
        """
    def axes_labels_size(self, s=None):
        """
        Set the relative size of axes labels w.r.t. the axes tick marks.

        INPUT:

        - ``s`` -- float, relative size of axes labels w.r.t. to the tick marks,
          the size of the tick marks being set by :meth:`fontsize`

        If called with no input, return the current relative size.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: p = plot(sin(x^2), (x, -3, 3), axes_labels=['$x$','$y$'])
            sage: p.axes_labels_size()  # default value
            1.6
            sage: p.axes_labels_size(2.5)
            sage: p.axes_labels_size()
            2.5

        Now the axes labels are large w.r.t. the tick marks::

            sage: p                                                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive
        """
    def axes(self, show=None):
        """
        Set whether or not the `x` and `y` axes are shown
        by default.

        INPUT:

        - ``show`` -- boolean

        If called with no input, return the current axes setting.

        EXAMPLES::

            sage: L = line([(1,2), (3,-4), (2, 5), (1,2)])

        By default the axes are displayed.

        ::

            sage: L.axes()
            True

        But we turn them off, and verify that they are off

        ::

            sage: L.axes(False)
            sage: L.axes()
            False

        Displaying L now shows a triangle but no axes.

        ::

            sage: L
            Graphics object consisting of 1 graphics primitive
        """
    def axes_color(self, c=None):
        """
        Set the axes color.

        If called with no input, return the current axes_color setting.

        INPUT:

        - ``c`` -- an RGB color 3-tuple, where each tuple entry
          is a float between 0 and 1

        EXAMPLES: We create a line, which has like everything a default
        axes color of black.

        ::

            sage: L = line([(1,2), (3,-4), (2, 5), (1,2)])
            sage: L.axes_color()
            (0, 0, 0)

        We change the axes color to red and verify the change.

        ::

            sage: L.axes_color((1,0,0))
            sage: L.axes_color()
            (1.0, 0.0, 0.0)

        When we display the plot, we'll see a blue triangle and bright red
        axes.

        ::

            sage: L
            Graphics object consisting of 1 graphics primitive
        """
    def axes_labels(self, l=None):
        """
        Set the axes labels.

        INPUT:

        - ``l`` -- (default: ``None``) a list of two strings or
          ``None``

        OUTPUT: a 2-tuple of strings

        If l is ``None``, returns the current ``axes_labels``,
        which is itself by default ``None``. The default labels are both
        empty.

        EXAMPLES: We create a plot and put x and y axes labels on it.

        ::

            sage: p = plot(sin(x), (x, 0, 10))                                          # needs sage.symbolic
            sage: p.axes_labels(['$x$','$y$'])                                          # needs sage.symbolic
            sage: p.axes_labels()                                                       # needs sage.symbolic
            ('$x$', '$y$')

        Now when you plot p, you see x and y axes labels::

            sage: p                                                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Notice that some may prefer axes labels which are not
        typeset::

            sage: plot(sin(x), (x, 0, 10), axes_labels=['x','y'])                       # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        TESTS:

        Unicode strings are acceptable; see :issue:`13161`. Note that
        this does not guarantee that matplotlib will handle the strings
        properly, although it should.

        ::

            sage: c = circle((0,0), 1)
            sage: c.axes_labels(['axe des abscisses', 'axe des ordonnées'])
            sage: c._axes_labels
            ('axe des abscisses', 'axe des ordonnées')
        """
    def axes_label_color(self, c=None):
        """
        Set the color of the axes labels.

        The axes labels are placed at the edge of the x and y axes, and are
        not on by default (use the :meth:`axes_labels` command to
        set them; see the example below). This function just changes their
        color.

        INPUT:

        - ``c`` -- an RGB 3-tuple of numbers between 0 and 1


        If called with no input, return the current axes_label_color
        setting.

        EXAMPLES: We create a plot, which by default has axes label color
        black.

        ::

            sage: p = plot(sin, (-1,1))                                                 # needs sage.symbolic
            sage: p.axes_label_color()                                                  # needs sage.symbolic
            (0, 0, 0)

        We change the labels to be red, and confirm this::

            sage: p.axes_label_color((1,0,0))                                           # needs sage.symbolic
            sage: p.axes_label_color()                                                  # needs sage.symbolic
            (1.0, 0.0, 0.0)

        We set labels, since otherwise we won't see anything.

        ::

            sage: p.axes_labels(['$x$ axis', '$y$ axis'])                               # needs sage.symbolic

        In the plot below, notice that the labels are red::

            sage: p                                                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive
        """
    def axes_width(self, w=None):
        """
        Set the axes width. Use this to draw a plot with really fat or
        really thin axes.

        INPUT:

        - ``w`` -- a float


        If called with no input, return the current
        ``axes_width`` setting.

        EXAMPLES: We create a plot, see the default axes width (with funny
        Python float rounding), then reset the width to 10 (very fat).

        ::

            sage: # needs sage.symbolic
            sage: p = plot(cos, (-3,3))
            sage: p.axes_width()
            0.8
            sage: p.axes_width(10)
            sage: p.axes_width()
            10.0

        Finally we plot the result, which is a graph with very fat axes.

        ::

            sage: p                                                                     # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive
        """
    def tick_label_color(self, c=None):
        """
        Set the color of the axes tick labels.

        INPUT:

        - ``c`` -- an RGB 3-tuple of numbers between 0 and 1


        If called with no input, return the current ``tick_label_color``
        setting.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: p = plot(cos, (-3,3))
            sage: p.tick_label_color()
            (0, 0, 0)
            sage: p.tick_label_color((1,0,0))
            sage: p.tick_label_color()
            (1.0, 0.0, 0.0)
            sage: p
            Graphics object consisting of 1 graphics primitive
        """
    def __getitem__(self, i):
        """
        Return the i-th graphics primitive object:

        EXAMPLES::

            sage: G = circle((1,1),2) + circle((2,2),5); print(G)
            Graphics object consisting of 2 graphics primitives
            sage: G[1]
            Circle defined by (2.0,2.0) with r=5.0
        """
    def __len__(self) -> int:
        """
        If G is of type Graphics, then len(G) gives the number of distinct
        graphics primitives making up that object.

        EXAMPLES::

            sage: G = circle((1,1),1) + circle((1,2),1) + circle((1,2),5); print(G)
            Graphics object consisting of 3 graphics primitives
            sage: len(G)
            3
        """
    def __delitem__(self, i) -> None:
        """
        If G is of type Graphics, then del(G[i]) removes the i-th distinct
        graphic primitive making up that object.

        EXAMPLES::

            sage: G = circle((1,1),1) + circle((1,2),1) + circle((1,2),5); print(G)
            Graphics object consisting of 3 graphics primitives
            sage: len(G)
            3
            sage: del(G[2])
            sage: print(G)
            Graphics object consisting of 2 graphics primitives
            sage: len(G)
            2
        """
    def __setitem__(self, i, x) -> None:
        """
        You can replace a :class:`GraphicPrimitive` (point, line, circle, etc...) in
        a :class:`Graphics` object G with any other :class:`GraphicPrimitive`

        EXAMPLES::

            sage: G = circle((1,1),1) + circle((1,2),1) + circle((1,2),5); print(G)
            Graphics object consisting of 3 graphics primitives

        ::

            sage: p = polygon([[1,3],[2,-2],[1,1],[1,3]]); print(p)
            Graphics object consisting of 1 graphics primitive

        ::

            sage: G[1] = p[0]
            sage: G    # show the plot
            Graphics object consisting of 3 graphics primitives
        """
    def __radd__(self, other):
        """
        Compute and return other + this graphics object.

        This only works when other is a Python int equal to 0. In all other
        cases a :exc:`TypeError` is raised. The main reason for this
        function is to make summing a list of graphics objects easier.

        EXAMPLES::

            sage: S = circle((0,0), 2)
            sage: print(int(0) + S)
            Graphics object consisting of 1 graphics primitive
            sage: print(S + int(0))
            Graphics object consisting of 1 graphics primitive

        The following would fail were it not for this function::

            sage: v = [circle((0,0), 2), circle((2,3), 1)]
            sage: print(sum(v))
            Graphics object consisting of 2 graphics primitives
        """
    def __add__(self, other):
        """
        If you have any Graphics object G1, you can always add any other
        amount of Graphics objects G2,G3,... to form a new Graphics object:
        ``G4 = G1 + G2 + G3``.

        The xmin, xmax, ymin, and ymax properties of the graphics objects
        are expanded to include all objects in both scenes. If the aspect
        ratio property of either or both objects are set, then the larger
        aspect ratio is chosen, with 'automatic' being overridden by a
        numeric aspect ratio.

        If one of the graphics object is set to show a legend, then
        the resulting object will also be set to show a legend. Legend
        options are propagated if set. If the same legend option is
        present in both arguments, the latter value is used.

        EXAMPLES::

            sage: g1 = plot(abs(sqrt(x^3-1)), (x,1,5), frame=True)                      # needs sage.symbolic
            sage: g2 = plot(-abs(sqrt(x^3-1)), (x,1,5), color='red')                    # needs sage.symbolic
            sage: g1 + g2  # displays the plot                                          # needs sage.symbolic
            Graphics object consisting of 2 graphics primitives

        TESTS:

        Extra keywords to show are propagated::

            sage: # needs sage.symbolic
            sage: (g1 + g2)._extra_kwds=={'aspect_ratio': 'automatic', 'frame': True}
            True
            sage: g1.set_aspect_ratio(2)
            sage: (g1+g2).aspect_ratio()
            2.0
            sage: g2.set_aspect_ratio(3)
            sage: (g1+g2).aspect_ratio()
            3.0

        As are legend options, :issue:`12936`::

            sage: # needs sage.symbolic
            sage: p1 = plot(x, x, 0, 1)
            sage: p2 = p1
            sage: p1.set_legend_options(back_color='black')
            sage: p2.set_legend_options(shadow=False)
            sage: p3 = p1 + p2
            sage: p3._legend_opts
            {'back_color': 'black', 'shadow': False}

        If the same legend option is specified more than once, the
        latter takes precedence::

            sage: # needs sage.symbolic
            sage: p1 = plot(x, x, 0, 1)
            sage: p2 = p1
            sage: p1.set_legend_options(shadow=True)
            sage: p2.set_legend_options(shadow=False)
            sage: p3 = p1 + p2
            sage: p3._legend_opts
            {'shadow': False}

        Flipped axes take precedence over non-flipped axes::

            sage: p1 = plot(x, x, 0, 1, flip_x=True, flip_y=True)                       # needs sage.symbolic
            sage: p2 = plot(x^2, x, 0, 1)                                               # needs sage.symbolic
            sage: [p._extra_kwds[k] for p in [p1 + p2, p2 + p1]                         # needs sage.symbolic
            ....:  for k in ['flip_x', 'flip_y']]
            [True, True, True, True]
        """
    def add_primitive(self, primitive) -> None:
        """
        Add a primitive to this graphics object.

        EXAMPLES:

        We give a very explicit example::

            sage: G = Graphics()
            sage: from math import e
            sage: from sage.plot.line import Line
            sage: from sage.plot.arrow import Arrow
            sage: L = Line([3,4,2,7,-2], [1,2,e,4,5.],
            ....:          {'alpha': 1, 'thickness': 2, 'rgbcolor': (0,1,1),
            ....:           'legend_label': ''})
            sage: A = Arrow(2, -5, .1, .2,
            ....:           {'width': 3, 'head': 0, 'rgbcolor': (1,0,0),
            ....:            'linestyle': 'dashed', 'zorder': 8, 'legend_label': ''})
            sage: G.add_primitive(L)
            sage: G.add_primitive(A)
            sage: G
            Graphics object consisting of 2 graphics primitives
        """
    def plot(self):
        """
        Draw a 2D plot of this graphics object, which just returns this
        object since this is already a 2D graphics object.

        EXAMPLES::

            sage: S = circle((0,0), 2)
            sage: S.plot() is S
            True

        It does not accept any argument (:issue:`19539`)::

            sage: S.plot(1)
            Traceback (most recent call last):
            ...
            TypeError: ...plot() takes 1 positional argument but 2 were given

            sage: S.plot(hey='hou')
            Traceback (most recent call last):
            ...
            TypeError: ...plot() got an unexpected keyword argument 'hey'
        """
    def plot3d(self, z: int = 0, **kwds):
        """
        Return an embedding of this 2D plot into the xy-plane of 3D space,
        as a 3D plot object. An optional parameter ``z`` can be given to
        specify the z-coordinate.

        EXAMPLES::

            sage: sum(plot(z*sin(x), 0, 10).plot3d(z)   # long time                     # needs sage.symbolic
            ....:     for z in range(6))
            Graphics3d Object
        """
    SHOW_OPTIONS: Incomplete
    LEGEND_OPTIONS: Incomplete
    def show(self, **kwds) -> None:
        '''
        Show this graphics image immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        OPTIONAL INPUT:

        - ``dpi`` -- (default: 100) dots per inch

        - ``figsize`` -- (default: [6.4, 4.8]) [width, height] inches. The
          maximum value of each of the width and the height can be 327
          inches, at the default ``dpi`` of 100 dpi, which is just shy of
          the maximum allowed value of 32768 dots (pixels).

        - ``fig_tight`` -- boolean (default: ``True``); whether to clip the drawing
          tightly around drawn objects.  If ``True``, then the resulting
          image will usually not have dimensions corresponding to
          ``figsize``.  If ``False``, the resulting image will have
          dimensions corresponding to ``figsize``.

        - ``aspect_ratio`` -- the perceived height divided by the
          perceived width. For example, if the aspect ratio is set to ``1``, circles
          will look round and a unit square will appear to have sides
          of equal length, and if the aspect ratio is set ``2``, vertical units will be
          twice as long as horizontal units, so a unit square will be twice as
          high as it is wide.  If set to ``\'automatic\'``, the aspect ratio
          is determined by ``figsize`` and the picture fills the figure.

        - ``axes`` -- (default: ``True``)

        - ``axes_labels`` -- (default: ``None``) list (or tuple) of two
          strings; the first is used as the label for the horizontal
          axis, and the second for the vertical axis.

        - ``axes_labels_size`` -- (default: current setting -- 1.6) scale factor
          relating the size of the axes labels with respect to the size of the
          tick marks.

        - ``fontsize`` -- (default: current setting -- 10) positive
          integer; used for axes labels; if you make this very large,
          you may have to increase figsize to see all labels.

        - ``frame`` -- boolean (default: ``False``); draw a frame around the image

        - ``gridlines`` -- (default: ``None``) can be any of the following:

          - None, False: do not add grid lines.

          - True, "automatic", "major": add grid lines at major ticks of the axes.

          - "minor": add grid at major and minor ticks.

          - [xlist,ylist]: a tuple or list containing
            two elements, where xlist (or ylist) can be
            any of the following.


            - None, False: don\'t add horizontal (or vertical) lines.

            - True, "automatic", "major": add horizontal (or vertical) grid lines at
              the major ticks of the axes.

            - "minor": add horizontal (or vertical) grid lines at major and minor ticks of
              axes.

            - an iterable yielding numbers n or pairs (n,opts), where n
              is the coordinate of the line and opt is a dictionary of
              MATPLOTLIB options for rendering the line.


        - ``gridlinesstyle, hgridlinesstyle, vgridlinesstyle`` -
          (default: ``None``); a dictionary of MATPLOTLIB options for the
          rendering of the grid lines, the horizontal grid lines or the
          vertical grid lines, respectively.

        - ``transparent`` -- boolean (default: ``False``); if True, make the
          background transparent

        - ``axes_pad`` -- (default: 0.02 on ``\'linear\'`` scale, 1 on
          ``\'log\'`` scale)

          - In the ``\'linear\'`` scale, it determines the percentage of the
            axis range that is added to each end of each axis. This helps
            avoid problems like clipping lines because of line-width, etc.
            To get axes that are exactly the specified limits, set
            ``axes_pad`` to zero.

          - On the ``\'log\'`` scale, it determines the exponent of the
            fraction of the minimum (resp. maximum) that is subtracted from
            the minimum (resp. added to the maximum) value of the axis. For
            instance if the minimum is `m` and the base of the axis is `b`
            then the new minimum after padding the axis will be
            `m - m/b^{\\mathrm{axes\\_pad}}`.

        - ``ticks_integer`` -- boolean (default: ``False``); guarantee that the ticks
          are integers (the ``ticks`` option, if specified, will
          override this)

        - ``ticks`` -- a matplotlib locator for the major ticks, or
          a number. There are several options.  For more information about
          locators, type ``from matplotlib import ticker`` and then
          ``ticker?``.

          - If this is a locator object, then it is the locator for
            the horizontal axis.  A value of None means use the default
            locator.

          - If it is a list of two locators, then the first is for the
            horizontal axis and one for the vertical axis.  A value of
            None means use the default locator (so a value of
            [None, my_locator] uses my_locator for the vertical axis and
            the default for the horizontal axis).

          - If in either case above one of the entries is a number `m`
            (something which can be coerced to a float), it will be
            replaced by a MultipleLocator which places major ticks at
            integer multiples of `m`.  See examples.

          - If in either case above one of the entries is a list of
            numbers, it will be replaced by a FixedLocator which places
            ticks at the locations specified.  This includes the case of
            of the empty list, which will give no ticks.  See examples.

        - ``tick_formatter`` -- a matplotlib formatter for the major
          ticks. There are several options.  For more information about
          formatters, type ``from matplotlib import ticker`` and then
          ``ticker?``.

          If the value of this keyword is a single item, then this will
          give the formatting for the horizontal axis *only* (except for
          the ``\'latex\'`` option).  If it is a list or tuple, the first
          is for the horizontal axis, the second for the vertical axis.
          The options are below:

          - If one of the entries is a formatter object, then it used.
            A value of None means to use the default locator (so using
            ``tick_formatter=[None, my_formatter]`` uses my_formatter
            for the vertical axis and the default for the horizontal axis).

          - If one of the entries is a symbolic constant such as `\\pi`,
            `e`, or `sqrt(2)`, ticks will be formatted nicely at rational
            multiples of this constant.

          .. warning::

             This should only be used with the ``ticks`` option using nice
             rational multiples of that constant!

          - If one of the entries is the string ``\'latex\'``, then the
            formatting will be nice typesetting of the ticks.  This is
            intended to be used when the tick locator for at least one of
            the axes is a list including some symbolic elements. This uses
            matplotlib\'s internal LaTeX rendering engine. If you want to
            use an external LaTeX compiler, then set the keyword option
            ``typeset``.  See examples.

        - ``title`` -- (default: ``None``) the title for the plot

        - ``title_pos`` -- (default: ``None``) the position of the title for the
            plot. It must be a tuple or a list of two real numbers
            ``(x_pos, y_pos)`` which indicate the relative position of the
            title within the plot. The plot itself can be considered to
            occupy, in relative terms, the region within a unit square
            `[0, 1] \\times [0, 1]`.  The title text is centered around the
            horizontal factor ``x_pos`` of the plot. The baseline of the
            title text is present at the vertical factor ``y_pos`` of the
            plot. Hence, ``title_pos=(0.5, 0.5)`` will center the title in
            the plot, whereas ``title_pos=(0.5, 1.1)`` will center the
            title along the horizontal direction, but will place the title
            a fraction `0.1` times above the plot.

          - If the first entry is a list of strings (or numbers), then the
            formatting for the horizontal axis will be typeset with the strings
            present in the list. Each entry of the list of strings must be
            provided with a corresponding number in the first entry of
            ``ticks`` to indicate its position on the axis. To typeset the
            strings with ``\'latex\'`` enclose them within ``\'$\'`` symbols. To
            have similar custom formatting of the labels along the vertical
            axis, the second entry must be a list of strings and the second
            entry of ``ticks`` must also be a list of numbers which give the
            positions of the labels. See the examples below.

        - ``show_legend`` -- (default: ``None``) if ``True``, show the legend

        - ``legend_*`` -- all the options valid for :meth:`set_legend_options`
            prefixed with ``legend_``

        - ``base`` -- (default: 10) the base of the logarithm if
          a logarithmic scale is set. This must be greater than 1. The base
          can be also given as a list or tuple ``(basex, basey)``.
          ``basex`` sets the base of the logarithm along the horizontal
          axis and ``basey`` sets the base along the vertical axis.

        - ``scale`` -- (default: ``\'linear\'``) string. The scale of the axes.
          Possible values are

          - ``\'linear\'`` -- linear scaling of both the axes
          - ``\'loglog\'`` -- sets both the horizontal and vertical axes to
            logarithmic scale
          - ``\'semilogx\'`` -- sets only the horizontal axis to logarithmic
            scale
          - ``\'semilogy\'`` -- sets only the vertical axis to logarithmic
            scale

          The scale can be also be given as single argument that is a list
          or tuple ``(scale, base)`` or ``(scale, basex, basey)``.

          .. NOTE::

            - If the ``scale`` is ``\'linear\'``, then irrespective of what
              ``base`` is set to, it will default to 10 and will remain
              unused.

        - ``xmin`` -- starting x value in the rendered figure

        - ``xmax`` -- ending x value in the rendered figure

        - ``ymin`` -- starting y value in the rendered figure

        - ``ymax`` -- ending y value in the rendered figure

        - ``flip_x`` -- boolean (default: ``False``); if ``True``, flip the horizontal
          axis

        - ``flip_y`` -- boolean (default: ``False``); if ``True``, flip the vertical
          axis

        - ``typeset`` -- (default: ``\'default\'``) string. The type of
          font rendering that should be used for the text. The possible
          values are

          - ``\'default\'`` -- uses matplotlib\'s internal text rendering
            engine called Mathtext ( see
            https://matplotlib.org/users/mathtext.html ). If you have
            modified the default matplotlib settings, for instance via
            a matplotlibrc file, then this option will not change any of
            those settings.
          - ``\'latex\'`` -- laTeX is used for rendering the fonts. This
            requires LaTeX, dvipng and Ghostscript to be installed
          - ``\'type1\'`` -- type 1 fonts are used by matplotlib in the text
            in the figure.  This requires LaTeX, dvipng and Ghostscript to
            be installed.

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES::

            sage: c = circle((1,1), 1, color=\'red\')
            sage: c.show(xmin=-1, xmax=3, ymin=-1, ymax=3)

        You can make the picture larger by changing ``figsize`` with width,
        height each having a maximum value of 327 inches at default dpi::

            sage: p = ellipse((0,0),4,1)
            sage: p.show(figsize=[327,10], dpi=100)
            sage: p.show(figsize=[328,10], dpi=80)

        You can turn off the drawing of the axes::

            sage: show(plot(sin,-4,4), axes=False)                                      # needs sage.symbolic

        You can also label the axes.  Putting something in dollar
        signs formats it as a mathematical expression::

            sage: show(plot(sin,-4,4), axes_labels=(\'$x$\',\'$y$\'))                       # needs sage.symbolic

        You can add a title to a plot::

            sage: show(plot(sin,-4,4), title=r\'A plot of $\\sin(x)$\')                    # needs sage.symbolic

        You can also provide the position for the title to the plot. In the
        plot below the title is placed on the bottom left of the figure.::

            sage: plot(sin, -4, 4, title=\'Plot sin(x)\', title_pos=(0.05,-0.05))         # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        If you want all the text to be rendered by using an external LaTeX
        installation then set the ``typeset`` to ``\'latex\'``. This
        requires that LaTeX, dvipng and Ghostscript be installed::

            sage: plot(x, typeset=\'latex\')                                      # optional - latex, needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        If you want all the text in your plot to use Type 1 fonts, then
        set the ``typeset`` option to ``\'type1\'``. This requires that
        LaTeX, dvipng and Ghostscript be installed::

            sage: plot(x, typeset=\'type1\')                                      # optional - latex, needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        You can turn on the drawing of a frame around the plots::

            sage: show(plot(sin,-4,4), frame=True)                                      # needs sage.symbolic

        You can make the background transparent::

            sage: plot(sin(x), (x, -4, 4), transparent=True)                            # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Prior to :issue:`19485`, legends by default had a shadowless gray
        background. This behavior can be recovered by passing in certain
        ``legend_options``::

            sage: p = plot(sin(x), legend_label=r\'$\\sin(x)$\')                           # needs sage.symbolic
            sage: p.show(legend_options={\'back_color\': (0.9,0.9,0.9),                   # needs sage.symbolic
            ....:                        \'shadow\': False})

        We can change the scale of the axes in the graphics before
        displaying::

            sage: G = plot(exp, 1, 10)                                                  # needs sage.symbolic
            sage: G.show(scale=\'semilogy\')                                              # needs sage.symbolic

        We can change the base of the logarithm too. The following changes
        the vertical axis to be on log scale, and with base 2. Note that
        the ``base`` argument will ignore any changes to the axis which is
        in linear scale.::

            sage: G.show(scale=\'semilogy\', base=2)  # y axis as powers of 2         # long time, needs sage.symbolic

        ::

            sage: G.show(scale=\'semilogy\', base=(3,2))  # base ignored for x-axis       # needs sage.symbolic

        The scale can be also given as a 2-tuple or a 3-tuple.::

            sage: G.show(scale=(\'loglog\', 2.1))   # both x and y axes in base 2.1   # long time, needs sage.symbolic

        ::

            sage: G.show(scale=(\'loglog\', 2, 3))  # x in base 2, y in base 3        # long time, needs sage.symbolic

        The base need not be an integer, though it does have to be made
        a float.::

            sage: G.show(scale=\'semilogx\', base=float(e))  # base is e                  # needs sage.symbolic

        Logarithmic scale can be used for various kinds of plots. Here are
        some examples.::

            sage: G = list_plot([10**i for i in range(10)])                         # long time, needs sage.symbolic
            sage: G.show(scale=\'semilogy\')                                          # long time, needs sage.symbolic

        ::

            sage: G = parametric_plot((x, x**2), (x, 1, 10))                            # needs sage.symbolic
            sage: G.show(scale=\'loglog\')                                                # needs sage.symbolic

        ::

            sage: disk((5,5), 4, (0, 3*pi/2)).show(scale=\'loglog\',base=2)               # needs sage.symbolic

        ::

            sage: x, y = var(\'x, y\')                                                    # needs sage.symbolic
            sage: G = plot_vector_field((2^x,y^2), (x,1,10), (y,1,100))                 # needs sage.symbolic
            sage: G.show(scale=\'semilogx\',base=2)                                       # needs sage.symbolic

        Flip the horizontal or vertical axis.

        ::

            sage: G = plot(x^3, -2, 3)                                                  # needs sage.symbolic
            sage: G.show(flip_x=True)                                                   # needs sage.symbolic
            sage: G.show(flip_y=True)                                                   # needs sage.symbolic

        Add grid lines at the major ticks of the axes.

        ::

            sage: c = circle((0,0), 1)
            sage: c.show(gridlines=True)
            sage: c.show(gridlines=\'automatic\')
            sage: c.show(gridlines=\'major\')

        Add grid lines at the major and minor ticks of the axes.

        ::

            sage: # needs sage.symbolic
            sage: u,v = var(\'u v\')
            sage: f = exp(-(u^2+v^2))
            sage: p = plot_vector_field(f.gradient(), (u,-2,2), (v,-2,2))
            sage: p.show(gridlines=\'minor\')

        Add only horizontal or vertical grid lines.

        ::

            sage: p = plot(sin, -10, 20)                                                # needs sage.symbolic
            sage: p.show(gridlines=[None, "automatic"])                                 # needs sage.symbolic
            sage: p.show(gridlines=["minor", False])                                    # needs sage.symbolic

        Add grid lines at specific positions (using lists/tuples).

        ::

            sage: x, y = var(\'x, y\')                                                    # needs sage.symbolic
            sage: p = implicit_plot((y^2-x^2)*(x-1)*(2*x-3) - 4*(x^2+y^2-2*x)^2,        # needs sage.symbolic
            ....:                   (x,-2,2), (y,-2,2), plot_points=1000)
            sage: p.show(gridlines=[[1,0],[-1,0,1]])                                    # needs sage.symbolic

        Add grid lines at specific positions (using iterators).

        ::

            sage: def maple_leaf(t):
            ....:     return (100/(100+(t-pi/2)^8))*(2-sin(7*t)-cos(30*t)/2)
            sage: p = polar_plot(maple_leaf, -pi/4, 3*pi/2,                         # long time, needs sage.symbolic
            ....:                color=\'red\',plot_points=1000)
            sage: p.show(gridlines=([-3,-2.75,..,3], range(-1,5,2)))                # long time, needs sage.symbolic

        Add grid lines at specific positions (using functions).

        ::

            sage: # needs sage.symbolic
            sage: y = x^5 + 4*x^4 - 10*x^3 - 40*x^2 + 9*x + 36
            sage: p = plot(y, -4.1, 1.1)
            sage: xlines = lambda a, b: [z for z, m in y.roots()]
            sage: p.show(gridlines=[xlines, [0]], frame=True, axes=False)

        Change the style of all the grid lines.

        ::

            sage: b = bar_chart([-3,5,-6,11], color=\'red\')
            sage: b.show(gridlines=([-1,-0.5,..,4], True),
            ....:        gridlinesstyle=dict(color=\'blue\', linestyle=\':\'))

        Change the style of the horizontal or vertical grid lines
        separately.

        ::

            sage: p = polar_plot(2 + 2*cos(x), 0, 2*pi, color=hue(0.3))                 # needs sage.symbolic
            sage: p.show(gridlines=True,                                                # needs sage.symbolic
            ....:        hgridlinesstyle=dict(color=\'orange\', linewidth=1.0),
            ....:        vgridlinesstyle=dict(color=\'blue\', linestyle=\':\'))

        Change the style of each grid line individually.

        ::

            sage: x, y = var(\'x, y\')                                                    # needs sage.symbolic
            sage: p = implicit_plot((y^2-x^2)*(x-1)*(2*x-3) - 4*(x^2+y^2-2*x)^2,        # needs sage.symbolic
            ....:                   (x,-2,2), (y,-2,2), plot_points=1000)
            sage: p.show(gridlines=(                                                    # needs sage.symbolic
            ....:    [
            ....:     (1,{"color":"red","linestyle":":"}),
            ....:     (0,{"color":"blue","linestyle":"--"})
            ....:    ],
            ....:    [
            ....:     (-1,{"color":"red","linestyle":":"}),
            ....:     (0,{"color":"blue","linestyle":"--"}),
            ....:     (1,{"color":"red","linestyle":":"}),
            ....:    ]
            ....:    ),
            ....:    gridlinesstyle=dict(marker=\'x\',color=\'black\'))

        Grid lines can be added to contour plots.

        ::

            sage: f = sin(x^2 + y^2)*cos(x)*sin(y)                                      # needs sage.symbolic
            sage: c = contour_plot(f, (x, -4, 4), (y, -4, 4), plot_points=100)          # needs sage.symbolic
            sage: c.show(gridlines=True,                                                # needs sage.symbolic
            ....:        gridlinesstyle={\'linestyle\': \':\', \'linewidth\': 1, \'color\': \'red\'})

        Grid lines can be added to matrix plots.

        ::

            sage: M = MatrixSpace(QQ,10).random_element()
            sage: matrix_plot(M).show(gridlines=True)

        By default, Sage increases the horizontal and vertical axes
        limits by a certain percentage in all directions.  This is
        controlled by the ``axes_pad`` parameter.  Increasing the range
        of the axes helps avoid problems with lines and dots being
        clipped because the linewidth extends beyond the axes.  To get
        axes limits that are exactly what is specified, set
        ``axes_pad`` to zero.  Compare the following two examples

        ::

            sage: (plot(sin(x), (x, -pi, pi), thickness=2)                              # needs sage.symbolic
            ....:   + point((pi, -1), pointsize=15))
            Graphics object consisting of 2 graphics primitives
            sage: (plot(sin(x), (x, -pi, pi), thickness=2, axes_pad=0)                  # needs sage.symbolic
            ....:   + point((pi, -1), pointsize=15))
            Graphics object consisting of 2 graphics primitives

        The behavior of the ``axes_pad`` parameter is different if the axis
        is in the ``\'log\'`` scale. If `b` is the base of the axis, the
        minimum value of the axis, is decreased by the factor
        `1/b^{\\mathrm{axes\\_pad}}` of the minimum and the maximum value of the axis
        is increased by the same factor of the maximum value.  Compare the
        axes in the following two plots to see the difference.

        ::

            sage: plot_loglog(x, (1.1*10**-2, 9990))                                    # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

            sage: plot_loglog(x, (1.1*10**-2, 9990), axes_pad=0)                        # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Via matplotlib, Sage allows setting of custom ticks.  See above
        for more details.

        Here the labels are not so useful::

            sage: plot(sin(pi*x), (x, -8, 8))                                           # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Now put ticks at multiples of 2::

            sage: plot(sin(pi*x), (x, -8, 8), ticks=2)                                  # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Or just choose where you want the ticks::

            sage: plot(sin(pi*x), (x, -8, 8), ticks=[[-7,-3,0,3,7], [-1/2,0,1/2]])      # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        Or no ticks at all::

            sage: plot(sin(pi*x), (x, -8, 8), ticks=[[], []])                           # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        This can be very helpful in showing certain features of plots. ::

            sage: plot(1.5/(1+e^(-x)), (x, -10, 10))  # doesn\'t quite show value of inflection point                    # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        ::

            sage: plot(1.5/(1+e^(-x)), (x, -10, 10),  # It\'s right at f(x)=0.75!        # needs sage.symbolic
            ....:      ticks=[None, 1.5/4])
            Graphics object consisting of 1 graphics primitive

        But be careful to leave enough room for at least two major ticks, so that
        the user can tell what the scale is::

            sage: plot(x^2, (x,1,8), ticks=6).show()                                    # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: Expand the range of the independent variable to
            allow two multiples of your tick locator (option `ticks`).

        We can also do custom formatting if you need it.  See above for full
        details::

            sage: plot(2*x + 1, (x,0,5),        # not tested (broken with matplotlib 3.6), needs sage.symbolic
            ....:      ticks=[[0,1,e,pi,sqrt(20)], 2],
            ....:      tick_formatter=\'latex\')
            Graphics object consisting of 1 graphics primitive

        This is particularly useful when setting custom ticks in multiples
        of `\\pi`.

        ::

            sage: plot(sin(x), (x,0,2*pi), ticks=pi/3, tick_formatter=pi)               # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        But keep in mind that you will get exactly the formatting you asked
        for if you specify both formatters.  The first syntax is recommended
        for best style in that case. ::

            sage: plot(arcsin(x), (x,-1,1), ticks=[None, pi/6],  # Nice-looking!        # needs sage.symbolic
            ....:      tick_formatter=["latex", pi])
            Graphics object consisting of 1 graphics primitive

        ::

            sage: plot(arcsin(x), (x,-1,1), ticks=[None, pi/6],  # Not so nice-looking  # needs sage.symbolic
            ....:      tick_formatter=[None, pi])
            Graphics object consisting of 1 graphics primitive

        Custom tick labels can be provided by providing the keyword
        ``tick_formatter`` with the list of labels, and simultaneously
        providing the keyword ``ticks`` with the positions of the labels. ::

            sage: plot(x, (x,0,3), ticks=[[1,2.5], [0.5,1,2]],                          # needs sage.symbolic
            ....:      tick_formatter=[["$x_1$","$x_2$"], ["$y_1$","$y_2$","$y_3$"]])
            Graphics object consisting of 1 graphics primitive

        The following sets the custom tick labels only along the horizontal
        axis. ::

            sage: plot(x**2, (x,0,2), ticks=[[1,2], None],                              # needs sage.symbolic
            ....:      tick_formatter=[["$x_1$","$x_2$"], None])
            Graphics object consisting of 1 graphics primitive

        If the number of tick labels do not match the number of positions of
        tick labels, then it results in an error.::

            sage: plot(x**2, (x,0,2), ticks=[[2], None],                                # needs sage.symbolic
            ....:      tick_formatter=[["$x_1$","$x_2$"], None]).show()
            Traceback (most recent call last):
            ...
            ValueError: If the first component of the list `tick_formatter` is a list
            then the first component of `ticks` must also be a list of equal length.

        When using logarithmic scale along the axis, make sure to have
        enough room for two ticks so that the user can tell what the scale
        is. This can be effected by increasing the range of the independent
        variable, or by changing the ``base``, or by providing enough tick
        locations by using the ``ticks`` parameter.

        By default, Sage will expand the variable range so that at least two
        ticks are included along the logarithmic axis. However, if you
        specify ``ticks`` manually, this safety measure can be defeated::

            sage: list_plot_loglog([(1,2),(2,3)], plotjoined=True, ticks=[[1],[1]])
            doctest:...: UserWarning: The x-axis contains fewer than 2 ticks;
            the logarithmic scale of the plot may not be apparent to the reader.
            doctest:...: UserWarning: The y-axis contains fewer than 2 ticks;
            the logarithmic scale of the plot may not be apparent to the reader.
            Graphics object consisting of 1 graphics primitive

        This one works, since the horizontal axis is automatically expanded
        to contain two ticks and the vertical axis is provided with two ticks::

            sage: list_plot_loglog([(1,2),(2,3)], plotjoined=True, ticks=[None,[1,10]])
            Graphics object consisting of 1 graphics primitive

        Another example in the log scale where both the axes are automatically
        expanded to show two major ticks::

            sage: list_plot_loglog([(2,0.5), (3, 4)], plotjoined=True)
            Graphics object consisting of 1 graphics primitive

        When using ``title_pos``, it must be ensured that a list or a tuple
        of length two is used. Otherwise, a warning is raised::

            sage: plot(x, -4, 4, title=\'Plot x\', title_pos=0.05)                        # needs sage.symbolic
            doctest:...: ...RichReprWarning: Exception in _rich_repr_ while displaying
            object: \'title_pos\' must be a list or tuple of two real numbers.
            Graphics object consisting of 1 graphics primitive

        TESTS:

        The following tests result in a segmentation fault and should not
        be run or doctested::

            sage: p = ellipse((0,0),4,1)
            sage: p.show(figsize=[232,232],dpi=100)  # not tested
            ------------------------------------------------------------------------
            Unhandled SIGSEGV: A segmentation fault occurred.
            This probably occurred because a *compiled* module has a bug
            in it and is not properly wrapped with sig_on(), sig_off().
            Python will now terminate.
            ------------------------------------------------------------------------
            sage: p.show(figsize=[327,181],dpi=100)  # not tested
            ------------------------------------------------------------------------
            Unhandled SIGSEGV: A segmentation fault occurred.
            This probably occurred because a *compiled* module has a bug
            in it and is not properly wrapped with sig_on(), sig_off().
            Python will now terminate.
            ------------------------------------------------------------------------

        The following tests ensure we give a good error message for
        negative figsizes::

            sage: # needs sage.symbolic
            sage: P = plot(x^2,(x,0,1))
            sage: P.show(figsize=[-1,1])
            Traceback (most recent call last):
            ...
            ValueError: figsize should be positive numbers, not -1.0 and 1.0
            sage: P.show(figsize=-1)
            Traceback (most recent call last):
            ...
            ValueError: figsize should be positive, not -1.0
            sage: P.show(figsize=x^2)
            Traceback (most recent call last):
            ...
            TypeError: figsize should be a positive number, not x^2
            sage: P.show(figsize=[2,3,4])
            Traceback (most recent call last):
            ...
            ValueError: figsize should be a positive number or
            a list of two positive numbers, not [2, 3, 4]
            sage: P.show(figsize=[sqrt(2),sqrt(3)])
        '''
    def xmin(self, xmin=None):
        """
        EXAMPLES::

            sage: g = line([(-1,1), (3,2)])
            sage: g.xmin()
            -1.0
            sage: g.xmin(-3)
            sage: g.xmin()
            -3.0
        """
    def xmax(self, xmax=None):
        """
        EXAMPLES::

            sage: g = line([(-1,1), (3,2)])
            sage: g.xmax()
            3.0
            sage: g.xmax(10)
            sage: g.xmax()
            10.0
        """
    def ymin(self, ymin=None):
        """
        EXAMPLES::

            sage: g = line([(-1,1), (3,2)])
            sage: g.ymin()
            1.0
            sage: g.ymin(-3)
            sage: g.ymin()
            -3.0
        """
    def ymax(self, ymax=None):
        """
        EXAMPLES::

            sage: g = line([(-1,1), (3,2)])
            sage: g.ymax()
            2.0
            sage: g.ymax(10)
            sage: g.ymax()
            10.0
        """
    def get_minmax_data(self):
        """
        Return the x and y coordinate minimum and maximum.

        .. warning::

           The returned dictionary is mutable, but changing it does
           not change the xmin/xmax/ymin/ymax data.  The minmax data is a function
           of the primitives which make up this Graphics object.  To change the
           range of the axes, call methods :meth:`xmin`, :meth:`xmax`,
           :meth:`ymin`, :meth:`ymax`, or :meth:`set_axes_range`.

        OUTPUT:

        A dictionary whose keys give the xmin, xmax, ymin, and ymax
        data for this graphic.

        EXAMPLES::

            sage: g = line([(-1,1), (3,2)])
            sage: list(sorted(g.get_minmax_data().items()))
            [('xmax', 3.0), ('xmin', -1.0), ('ymax', 2.0), ('ymin', 1.0)]

        Note that changing ymax doesn't change the output of get_minmax_data::

            sage: g.ymax(10)
            sage: list(sorted(g.get_minmax_data().items()))
            [('xmax', 3.0), ('xmin', -1.0), ('ymax', 2.0), ('ymin', 1.0)]

        The width/height ratio (in output units, after factoring in the
        chosen aspect ratio) of the plot is limited to `10^{-15}\\dots
        10^{15}`, otherwise floating point errors cause problems in
        matplotlib::

            sage: l = line([(1e-19,-1), (-1e-19,+1)], aspect_ratio=1.0)
            sage: l.get_minmax_data()
            {'xmax': 1.00010000000000e-15,
             'xmin': -9.99900000000000e-16,
             'ymax': 1.0,
             'ymin': -1.0}
            sage: l = line([(0,0), (1,1)], aspect_ratio=1e19)
            sage: l.get_minmax_data()
            {'xmax': 5000.50000000000, 'xmin': -4999.50000000000,
             'ymax': 1.0, 'ymin': 0.0}
        """
    def matplotlib(self, filename=None, xmin=None, xmax=None, ymin=None, ymax=None, figsize=None, figure=None, sub=None, axes=None, axes_labels=None, axes_labels_size=None, flip_x: bool = False, flip_y: bool = False, fontsize=None, frame: bool = False, verify: bool = True, aspect_ratio=None, gridlines=None, gridlinesstyle=None, vgridlinesstyle=None, hgridlinesstyle=None, show_legend=None, legend_options=None, axes_pad=None, ticks_integer=None, tick_formatter=None, ticks=None, title=None, title_pos=None, base=None, scale=None, stylesheet=None, typeset: str = 'default'):
        '''
        Construct or modify a Matplotlib figure by drawing ``self`` on it.

        INPUT (partial description, involving only Matplotlib objects; see
        :meth:`show` for the other arguments):

        - ``figure`` -- (default: ``None``) Matplotlib figure (class
          ``matplotlib.figure.Figure``) on which ``self`` is to be displayed;
          if ``None``, the figure will be created from the parameter
          ``figsize``

        - ``figsize`` -- (default: ``None``) width or [width, height] in inches
          of the Matplotlib figure in case ``figure`` is ``None``; if
          ``figsize`` is ``None``, Matplotlib\'s default (6.4 x 4.8 inches) is
          used

        - ``sub`` -- (default: ``None``) subpart of the figure, as an
          instance of Matplotlib "axes" (class ``matplotlib.axes.Axes``) on
          which ``self`` is to be drawn; if ``None``, the subpart will be
          created so as to cover the whole figure

        OUTPUT:

        - a ``matplotlib.figure.Figure`` object; if the argument ``figure`` is
          provided, this is the same object as ``figure``.

        EXAMPLES::

            sage: c = circle((1,1),1)
            sage: print(c.matplotlib())
            Figure(640x480)

        To obtain the first Matplotlib ``Axes`` object inside of the
        figure, you can do something like the following.

        ::

            sage: p = plot(sin(x), (x, -2*pi, 2*pi))                                    # needs sage.symbolic
            sage: figure = p.matplotlib()                                               # needs sage.symbolic
            sage: axes = figure.axes[0]                                                 # needs sage.symbolic

        TESTS:

        We verify that :issue:`10291` is fixed::

            sage: # needs sage.symbolic
            sage: p = plot(sin(x), (x, -2*pi, 2*pi))
            sage: figure = p.matplotlib()
            sage: axes_range = p.get_axes_range()
            sage: figure = p.matplotlib()
            sage: axes_range2 = p.get_axes_range()
            sage: axes_range == axes_range2
            True

        We verify that legend options are properly handled (:issue:`12960`).
        First, we test with no options, and next with an incomplete set of
        options.::

            sage: # needs sage.symbolic
            sage: p = plot(x, legend_label=\'aha\')
            sage: p.legend(True)
            sage: pm = p.matplotlib()
            sage: pm = p.matplotlib(legend_options={\'font_size\': \'small\'})

        The title should not overlap with the axes labels nor the frame in
        the following plot (see :issue:`10512`)::

            sage: plot(sin(x^2), (x, -3, 3), title=\'Plot of sin(x^2)\',                  # needs sage.symbolic
            ....:      axes_labels=[\'x\',\'y\'], frame=True)
            Graphics object consisting of 1 graphics primitive

        ``typeset`` must not be set to an arbitrary string::

            sage: plot(x, typeset=\'garbage\')                                            # needs sage.symbolic
            doctest:...: ...RichReprWarning: Exception in _rich_repr_ while
            displaying object: typeset must be set to one of \'default\',
            \'latex\', or \'type1\'; got \'garbage\'.
            Graphics object consisting of 1 graphics primitive

        We verify that numerical options are changed to float before saving (:issue:`14741`).
        By default, Sage 5.10 changes float objects to the `RealLiteral` type.
        The patch changes them to float before creating `matplotlib` objects.::

            sage: # long time, needs sage.symbolic
            sage: f = lambda x, y: abs(cos((x + I * y) ** 4)) - 1
            sage: g = implicit_plot(f, (-4, 4), (-3, 3), linewidth=0.6)
            sage: gm = g.matplotlib()

        If the axes are flipped, the limits of the axes get swapped::

            sage: # needs sage.symbolic
            sage: p = plot(2*x, 1, 2)
            sage: sub, = p.matplotlib(flip_y=True, flip_x=True).axes
            sage: xmin, xmax = sub.get_xlim()
            sage: ymin, ymax = sub.get_ylim()
            sage: xmin > xmax, ymin > ymax
            (...True..., ...True...)
        '''
    def save_image(self, filename=None, *args, **kwds) -> None:
        """
        Save an image representation of ``self``.

        The image type is determined by the extension of the filename.
        For example, this could be ``.png``, ``.jpg``, ``.gif``,
        ``.pdf``, ``.svg``.  Currently this is implemented by calling
        the :meth:`save` method of self, passing along all arguments
        and keywords.

        .. NOTE::

            Not all image types are necessarily implemented for all
            graphics types.  See :meth:`save` for more details.

        EXAMPLES::

            sage: import tempfile
            sage: c = circle((1,1), 1, color='red')
            sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:
            ....:     c.save_image(f.name, xmin=-1, xmax=3,
            ....:                  ymin=-1, ymax=3)
        """
    def save(self, filename, **kwds) -> None:
        """
        Save the graphics to an image file.

        INPUT:

        - ``filename`` -- string. The filename and the image format
          given by the extension, which can be one of the following:

            * ``.eps``,

            * ``.pdf``,

            * ``.pgf``,

            * ``.png``,

            * ``.ps``,

            * ``.sobj`` (for a Sage object you can load later),

            * ``.svg``,

            * empty extension will be treated as ``.sobj``.

        All other keyword arguments will be passed to the plotter.

        OUTPUT: none

        EXAMPLES::

            sage: c = circle((1,1), 1, color='red')
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(suffix='.png') as f:
            ....:     c.save(f.name, xmin=-1, xmax=3, ymin=-1, ymax=3)

        To make a figure bigger or smaller, use ``figsize``::

            sage: c.save(f.name, figsize=5, xmin=-1, xmax=3, ymin=-1, ymax=3)

        By default, the figure grows to include all of the graphics and text,
        so the final image may not be exactly the figure size you specified.
        If you want a figure to be exactly a certain size, specify the keyword
        ``fig_tight=False``::

            sage: c.save(f.name, figsize=[8,4], fig_tight=False,
            ....:        xmin=-1, xmax=3, ymin=-1, ymax=3)

        You can also pass extra options to the plot command instead of this
        method, e.g. ::

            sage: plot(x^2 - 5, (x, 0, 5), ymin=0).save(tmp_filename(ext='.png'))       # needs sage.symbolic

        will save the same plot as the one shown by this command::

            sage: plot(x^2 - 5, (x, 0, 5), ymin=0)                                      # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive

        (This test verifies that :issue:`8632` is fixed.)

        TESTS:

        Legend labels should save correctly::

            sage: # needs sage.symbolic
            sage: P = plot(x,(x,0,1),legend_label='$xyz$')
            sage: P.set_legend_options(back_color=(1,0,0))
            sage: P.set_legend_options(loc=7)
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:
            ....:     P.save(f.name)

        This plot should save with the frame shown, showing :issue:`7524`
        is fixed (same issue as :issue:`7981` and :issue:`8632`)::

            sage: var('x,y')                                                            # needs sage.symbolic
            (x, y)
            sage: a = plot_vector_field((x,-y),(x,-1,1),(y,-1,1))                       # needs sage.symbolic
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:                 # needs sage.symbolic
            ....:     a.save(f.name)

        The following plot should show the axes; fixes :issue:`14782` ::

            sage: plot(x^2, (x, 1, 2), ticks=[[], []])                                  # needs sage.symbolic
            Graphics object consisting of 1 graphics primitive
        """
    def description(self):
        """
        Print a textual description to stdout.

        This method is mostly used for doctests.

        EXAMPLES::

            sage: print(polytopes.hypercube(2).plot().description())                    # needs sage.geometry.polyhedron
            Polygon defined by 4 points: [(-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0)]
            Line defined by 2 points: [(-1.0, 1.0), (-1.0, -1.0)]
            Line defined by 2 points: [(1.0, -1.0), (-1.0, -1.0)]
            Line defined by 2 points: [(1.0, -1.0), (1.0, 1.0)]
            Line defined by 2 points: [(1.0, 1.0), (-1.0, 1.0)]
            Point set defined by 4 point(s): [(1.0, -1.0), (1.0, 1.0), (-1.0, 1.0), (-1.0, -1.0)]
        """
    def inset(self, graphics, pos=None, fontsize=None):
        """
        Add a graphics object as an inset.

        INPUT:

        - ``graphics`` -- the graphics object (instance of :class:`Graphics`)
          to be added as an inset to the current graphics

        - ``pos`` -- (default: ``None``) 4-tuple
          ``(left, bottom, width, height)``
          specifying the location and size of the inset on the final figure,
          all quantities being in fractions of the figure width and height; if
          ``None``, the value ``(0.7, 0.7, 0.2, 0.2)`` is used

        - ``fontsize`` -- (default: ``None``)  integer, font size (in points)
          for the inset; if ``None``, the value of 6 points is used, unless
          ``fontsize`` has been explicitly set in the construction of
          ``graphics`` (in this case, it is not overwritten here)

        OUTPUT: instance of :class:`~sage.plot.multigraphics.MultiGraphics`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: f(x) = x^2*sin(1/x)
            sage: g1 = plot(f(x), (x, -2, 2), axes_labels=['$x$', '$y$'])
            sage: g2 = plot(f(x), (x, -0.3, 0.3), axes_labels=['$x$', '$y$'],
            ....:           frame=True)
            sage: g1.inset(g2)
            Multigraphics with 2 elements

        .. PLOT::

            f = (x**2*sin(1/x)).function(x)
            g1 = plot(f(x), (x, -2, 2), axes_labels=['$x$', '$y$'])
            g2 = plot(f(x), (x, -0.3, 0.3), axes_labels=['$x$', '$y$'], \\\n                      frame=True)
            sphinx_plot(g1.inset(g2))

        Using non-default values for the position/size and the font size::

            sage: g1.inset(g2, pos=(0.15, 0.7, 0.25, 0.25), fontsize=8)                 # needs sage.symbolic
            Multigraphics with 2 elements

        .. PLOT::

            f = (x**2*sin(1/x)).function(x)
            g1 = plot(f(x), (x, -2, 2), axes_labels=['$x$', '$y$'])
            g2 = plot(f(x), (x, -0.3, 0.3), axes_labels=['$x$', '$y$'], \\\n                      frame=True)
            sphinx_plot(g1.inset(g2, pos=(0.15, 0.7, 0.25, 0.25), fontsize=8))

        We can add another inset by invoking ``inset`` on the last output::

            sage: g1g2 = _                                                              # needs sage.symbolic
            sage: g3 = plot(f(x), (x, -0.05, 0.05), axes_labels=['$x$', '$y$'],         # needs sage.symbolic
            ....:           frame=True)
            sage: g1g2.inset(g3, pos=(0.65, 0.12, 0.25, 0.25))                          # needs sage.symbolic
            Multigraphics with 3 elements

        .. PLOT::

            f = (x**2*sin(1/x)).function(x)
            g1 = plot(f(x), (x, -2, 2), axes_labels=['$x$', '$y$'])
            g2 = plot(f(x), (x, -0.3, 0.3), axes_labels=['$x$', '$y$'], \\\n                      frame=True)
            g1g2 = g1.inset(g2, pos=(0.15, 0.7, 0.25, 0.25), fontsize=8)
            g3 = plot(f(x), (x, -0.05, 0.05), axes_labels=['$x$', '$y$'], \\\n                      frame=True)
            sphinx_plot(g1g2.inset(g3, pos=(0.65, 0.12, 0.25, 0.25)))
        """

def GraphicsArray(*args, **kwargs):
    """
    This is deprecated (see :issue:`28675`).
    Use :class:`sage.plot.multigraphics.GraphicsArray` instead.

    TESTS::

        sage: from sage.plot.graphics import GraphicsArray
        sage: c = circle((0,0), 1)
        sage: G = GraphicsArray([c, c])
        doctest:...: DeprecationWarning: GraphicsArray must be imported from
        sage.plot.multigraphics and no longer from sage.plot.graphics.
        See https://github.com/sagemath/sage/issues/28675 for details.
        sage: G
        Graphics Array of size 1 x 2
    """
