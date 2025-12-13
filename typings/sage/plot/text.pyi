from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class Text(GraphicPrimitive):
    '''
    Base class for Text graphics primitive.

    TESTS:

    We test creating some text::

        sage: text("I like Fibonacci",(3,5))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(text("I like Fibonacci",(3,5)))
    '''
    string: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, string, point, options) -> None:
        '''
        Initialize base class Text.

        EXAMPLES::

            sage: T = text("I like Fibonacci", (3,5))
            sage: t = T[0]
            sage: t.string
            \'I like Fibonacci\'
            sage: t.x
            3.0
            sage: t.options()[\'fontsize\']
            10
        '''
    def get_minmax_data(self):
        '''
        Return a dictionary with the bounding box data. Notice
        that, for text, the box is just the location itself.

        EXAMPLES::

            sage: T = text("Where am I?",(1,1))
            sage: t=T[0]
            sage: t.get_minmax_data()[\'ymin\']
            1.0
            sage: t.get_minmax_data()[\'ymax\']
            1.0
        '''
    def plot3d(self, **kwds):
        '''
        Plot 2D text in 3D.

        EXAMPLES::

            sage: T = text("ABC", (1, 1))
            sage: t = T[0]
            sage: s = t.plot3d()
            sage: s.jmol_repr(s.testing_render_params())[0][2]
            \'label "ABC"\'
            sage: s._trans
            (1.0, 1.0, 0)
        '''

def text(string, xy, **options):
    '''
    Return a 2D text graphics object at the point `(x, y)`.

    Type ``text.options`` for a dictionary of options for 2D text.

    2D OPTIONS:

    - ``fontsize`` -- how big the text is. Either an integer that
      specifies the size in points or a string which specifies a size (one of
      ``\'xx-small\'``, ``\'x-small\'``, ``\'small\'``, ``\'medium\'``, ``\'large\'``,
      ``\'x-large\'``, ``\'xx-large\'``).

    - ``fontstyle`` -- string either ``\'normal\'``, ``\'italic\'`` or ``\'oblique\'``

    - ``fontweight`` -- a numeric value in the range 0-1000 or a string (one of
      ``\'ultralight\'``, ``\'light\'``, ``\'normal\'``, ``\'regular\'``, ``\'book\'``,
      ``\'medium\'``, ``\'roman\'``, ``\'semibold\'``, ``\'demibold\'``, ``\'demi\'``,
      ``\'bold\'``, ``\'heavy\'``, ``\'extra bold\'``, ``\'black\'``)

    - ``rgbcolor`` -- the color as an RGB tuple

    - ``hue`` -- the color given as a hue

    - ``alpha`` -- a float (0.0 transparent through 1.0 opaque)

    - ``background_color`` -- the background color

    - ``rotation`` -- how to rotate the text: angle in degrees, vertical, horizontal

    - ``vertical_alignment`` -- how to align vertically: top, center, bottom

    - ``horizontal_alignment`` -- how to align horizontally: left, center, right

    - ``zorder`` -- the layer level in which to draw

    - ``clip`` -- boolean (default: ``False``); whether to clip or not

    - ``axis_coords`` -- boolean (default: ``False``); if ``True``, use axis
      coordinates, so that (0,0) is the lower left and (1,1) upper right,
      regardless of the x and y range of plotted values

    - ``bounding_box`` -- dictionary specifying a bounding box; currently the
      text location

    EXAMPLES::

        sage: text("Sage graphics are really neat because they use matplotlib!", (2,12))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        t = "Sage graphics are really neat because they use matplotlib!"
        sphinx_plot(text(t,(2,12)))

    Larger font, bold, colored red and transparent text::

        sage: text("I had a dream!", (2,12), alpha=0.3,
        ....:      fontsize=\'large\', fontweight=\'bold\', color=\'red\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(text("I had a dream!", (2,12), alpha=0.3, fontsize=\'large\', fontweight=\'bold\', color=\'red\'))

    By setting ``horizontal_alignment`` to \'left\' the text is guaranteed to be
    in the lower left no matter what::

        sage: text("I got a horse and he lives in a tree", (0,0),
        ....:      axis_coords=True, horizontal_alignment=\'left\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        t = "I got a horse and he lives in a tree"
        sphinx_plot(text(t, (0,0), axis_coords=True, horizontal_alignment=\'left\'))

    Various rotations::

        sage: text("noitator", (0,0), rotation=45.0,
        ....:      horizontal_alignment=\'left\', vertical_alignment=\'bottom\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(text("noitator", (0,0), rotation=45.0, horizontal_alignment=\'left\', vertical_alignment=\'bottom\'))

    ::

        sage: text("Sage is really neat!!", (0,0), rotation=\'vertical\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(text("Sage is really neat!!", (0,0), rotation=\'vertical\'))

    You can also align text differently::

        sage: t1 = text("Hello", (1,1), vertical_alignment=\'top\')
        sage: t2 = text("World", (1,0.5), horizontal_alignment=\'left\')
        sage: t1 + t2   # render the sum
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        t1 = text("Hello", (1,1), vertical_alignment=\'top\')
        t2 = text("World", (1,0.5), horizontal_alignment=\'left\')
        sphinx_plot(t1 + t2)

    You can save text as part of PDF output::

        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(suffix=\'.pdf\') as f:
        ....:     text("sage", (0,0), rgbcolor=(0,0,0)).save(f.name)

    Some examples of bounding box::

        sage: bbox = {\'boxstyle\': "rarrow,pad=0.3", \'fc\': "cyan", \'ec\': "b", \'lw\': 2}
        sage: text("I feel good", (1,2), bounding_box=bbox)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

         bbox = {\'boxstyle\':"rarrow,pad=0.3", \'fc\':"cyan", \'ec\':"b", \'lw\':2}
         sphinx_plot(text("I feel good", (1,2), bounding_box=bbox))

    ::

        sage: text("So good", (0,0), bounding_box={\'boxstyle\': \'round\', \'fc\': \'w\'})
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        bbox = {\'boxstyle\':\'round\', \'fc\':\'w\'}
        sphinx_plot(text("So good", (0,0), bounding_box=bbox))

    The possible options of the bounding box are \'boxstyle\' (one of \'larrow\',
    \'rarrow\', \'round\', \'round4\', \'roundtooth\', \'sawtooth\', \'square\'), \'fc\' or
    \'facecolor\', \'ec\' or \'edgecolor\', \'ha\' or \'horizontalalignment\', \'va\' or
    \'verticalalignment\', \'lw\' or \'linewidth\'.

    A text with a background color::

        sage: text("So good", (-2,2), background_color=\'red\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(text("So good", (-2,2), background_color=\'red\'))

    Use dollar signs for LaTeX and raw strings to avoid having to
    escape backslash characters::

        sage: A = arc((0, 0), 1, sector=(0.0, RDF.pi()))
        sage: a = sqrt(1./2.)
        sage: PQ = point2d([(-a, a), (a, a)])
        sage: botleft = dict(horizontal_alignment=\'left\', vertical_alignment=\'bottom\')
        sage: botright = dict(horizontal_alignment=\'right\', vertical_alignment=\'bottom\')
        sage: tp = text(r\'$z_P = e^{3i\\pi/4}$\',
        ....:           (-a, a), **botright)
        sage: tq = text(r\'$Q = (\\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{2}}{2})$\',
        ....:           (a, a), **botleft)
        sage: A + PQ + tp + tq
        Graphics object consisting of 4 graphics primitives

    .. PLOT::

        A = arc((0, 0), 1, sector=(0.0, RDF.pi()))
        a = sqrt(1./2.)
        PQ = point2d([(-a, a), (a, a)])
        botleft = dict(horizontal_alignment=\'left\', vertical_alignment=\'bottom\')
        botright = dict(horizontal_alignment=\'right\', vertical_alignment=\'bottom\')
        tp = text(r\'$z_P = e^{3i\\pi/4}$\', (-a, a), **botright)
        tq = text(r\'$Q = (\\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{2}}{2})$\', (a, a), **botleft)
        sphinx_plot(A + PQ + tp + tq)

    Text coordinates must be 2D, an error is raised if 3D coordinates are passed::

        sage: t = text("hi", (1, 2, 3))
        Traceback (most recent call last):
        ...
        ValueError: use text3d instead for text in 3d

    Use the :func:`text3d <sage.plot.plot3d.shapes2.text3d>` function for 3D text::

        sage: t = text3d("hi", (1, 2, 3))

    Or produce 2D text with coordinates `(x, y)` and plot it in 3D (at `z = 0`)::

        sage: t = text("hi", (1, 2))
        sage: t.plot3d()  # text at position (1, 2, 0)
        Graphics3d Object

    Extra options will get passed on to ``show()``, as long as they are valid. Hence this ::

        sage: text("MATH IS AWESOME", (0, 0), fontsize=40, axes=False)
        Graphics object consisting of 1 graphics primitive

    is equivalent to ::

        sage: text("MATH IS AWESOME", (0, 0), fontsize=40).show(axes=False)
    '''
