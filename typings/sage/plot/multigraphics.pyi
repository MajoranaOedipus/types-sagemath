from .graphics import ALLOWED_EXTENSIONS as ALLOWED_EXTENSIONS, Graphics as Graphics
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.structure.sage_object import SageObject as SageObject

class MultiGraphics(WithEqualityById, SageObject):
    """
    Base class for objects composed of :class:`~sage.plot.graphics.Graphics`
    objects.

    Both the display and the output to a file of ``MultiGraphics`` objects
    are governed by the method :meth:`save`, which is called by the rich output
    display manager, via
    :meth:`~sage.repl.rich_output.display_manager.DisplayManager.graphics_from_save`.

    The user interface is through the functions
    :func:`~sage.plot.plot.multi_graphics` (generic multi-graphics) and
    :func:`~sage.plot.plot.graphics_array` (subclass :class:`GraphicsArray`).

    INPUT:

    - ``graphics_list`` -- list of graphics along with their positions on the
      common canvas; each element of ``graphics_list`` is either

      - a pair ``(graphics, position)``, where ``graphics`` is a
        :class:`~sage.plot.graphics.Graphics` object and ``position`` is the
        4-tuple ``(left, bottom, width, height)`` specifying the location and
        size of the graphics on the canvas, all quantities being in fractions
        of the canvas width and height

      - or a single :class:`~sage.plot.graphics.Graphics` object; its position
        is then assumed to occupy the whole canvas, except for some padding;
        this corresponds to the default position
        ``(left, bottom, width, height) = (0.125, 0.11, 0.775, 0.77)``

    EXAMPLES:

    A multi-graphics made from two graphics objects::

        sage: g1 = plot(sin(x^3), (x, -pi, pi))
        sage: g2 = circle((0,0), 1, color='red')
        sage: G = multi_graphics([g1, (g2, (0.2, 0.55, 0.3, 0.3))])
        sage: G
        Multigraphics with 2 elements

    .. PLOT::

        g1 = plot(sin(x**3), (x, -pi, pi))
        g2 = circle((0,0), 1, color='red')
        G = multi_graphics([g1, (g2, (0.2, 0.55, 0.3, 0.3))])
        sphinx_plot(G)

    Since no position was given for ``g1``, it occupies the whole canvas.
    Moreover, we note that ``g2`` has been drawn over ``g1`` with a white
    background. To have a transparent background instead, one has to construct
    ``g2`` with the keyword ``transparent`` set to ``True``::

        sage: g2 = circle((0,0), 1, color='red', transparent=True)
        sage: G = multi_graphics([g1, (g2, (0.2, 0.55, 0.3, 0.3))])
        sage: G
        Multigraphics with 2 elements

    .. PLOT::

        g1 = plot(sin(x**3), (x, -pi, pi))
        g2 = circle((0,0), 1, color='red', transparent=True)
        G = multi_graphics([g1, (g2, (0.2, 0.55, 0.3, 0.3))])
        sphinx_plot(G)

    We can add a new graphics object to G via the method :meth:`append`::

        sage: g3 = complex_plot(zeta, (-20, 10), (-20, 20),
        ....:                   axes_labels=['$x$', '$y$'], frame=True)
        sage: G.append(g3, pos=(0.63, 0.12, 0.3, 0.3))
        sage: G
        Multigraphics with 3 elements

    .. PLOT::

        g1 = plot(sin(x**3), (x, -pi, pi))
        g2 = circle((0,0), 1, color='red', transparent=True)
        G = multi_graphics([g1, (g2, (0.2, 0.55, 0.3, 0.3))])
        g3 = complex_plot(zeta, (-20, 10), (-20, 20), \\\n                          axes_labels=['$x$', '$y$'], frame=True)
        G.append(g3, pos=(0.63, 0.12, 0.3, 0.3))
        sphinx_plot(G)

    We can access the individual elements composing ``G`` with the
    square-bracket operator::

        sage: print(G[0])
        Graphics object consisting of 1 graphics primitive
        sage: G[0] is g1
        True
        sage: G[1] is g2
        True
        sage: G[2] is g3
        True

    ``G[:]`` returns the full list of graphics objects composing ``G``::

        sage: G[:]
        [Graphics object consisting of 1 graphics primitive,
         Graphics object consisting of 1 graphics primitive,
         Graphics object consisting of 1 graphics primitive]
        sage: len(G)
        3
    """
    def __init__(self, graphics_list) -> None:
        """
        Initialize the attributes common to all MultiGraphics objects.

        TESTS::

            sage: from sage.plot.multigraphics import MultiGraphics
            sage: G = MultiGraphics([])
            sage: print(G)
            Multigraphics with 0 element
            sage: c = circle((0,0), 1)
            sage: G = MultiGraphics([c, (c, (0.7, 0.6, 0.2, 0.2))])
            sage: print(G)
            Multigraphics with 2 elements
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th element of the list of graphics composing ``self``.

        EXAMPLES:

        We can access and view individual plots::

            sage: L = [[plot(x^2)], [plot(x^3)]]
            sage: G = graphics_array(L)
            sage: G[1]
            Graphics object consisting of 1 graphics primitive

        Another example::

            sage: L = [plot(sin(k*x), (x,-pi,pi)) + circle((k,k), 1,
            ....:           color='red') for k in range(10)]
            sage: G = graphics_array(L, 5, 2)
            sage: G[3]
            Graphics object consisting of 2 graphics primitives
        """
    def __setitem__(self, i, g) -> None:
        """
        Set the ``i``-th element of the list of graphics composing ``self``.

        EXAMPLES::

            sage: L = [[plot(x^2)], [plot(x^3)]]
            sage: G = graphics_array(L)
            sage: G[1] # the plot of x^3
            Graphics object consisting of 1 graphics primitive

        Now we change it::

            sage: G[1] = circle((1,1), 2) + points([(1,2), (3,2), (5,5)],
            ....:                                  color='purple')
            sage: G[1] # a circle and some purple points
            Graphics object consisting of 2 graphics primitives
        """
    def __len__(self) -> int:
        """
        Total number of Graphics objects composing ``self``.

        EXAMPLES::

            sage: L = [circle((0,0), n) for n in range(6)]
            sage: G = graphics_array(L, 2, 3)
            sage: len(G)
            6
        """
    def matplotlib(self, figure=None, figsize=None, **kwds):
        """
        Construct or modify a Matplotlib figure by drawing ``self`` on it.

        INPUT:

        - ``figure`` -- (default: ``None``) Matplotlib figure (class
          ``matplotlib.figure.Figure``) on which ``self`` is to be displayed;
          if ``None``, the figure will be created from the parameter
          ``figsize``

        - ``figsize`` -- (default: ``None``) width or [width, height] in inches
          of the Matplotlib figure in case ``figure`` is ``None``; if
          ``figsize`` is ``None``, Matplotlib's default (6.4 x 4.8 inches) is
          used

        - ``kwds`` -- options passed to the
          :meth:`~sage.plot.graphics.Graphics.matplotlib` method of
          each graphics object constituting ``self``

        OUTPUT:

        - a ``matplotlib.figure.Figure`` object; if the argument ``figure`` is
          provided, this is the same object as ``figure``.

        EXAMPLES:

        Let us consider a :class:`GraphicsArray` object with 3 elements::

            sage: G = graphics_array([plot(sin(x^k), (x, 0, 3))
            ....:                     for k in range(1, 4)])

        If ``matplotlib()`` is invoked without any argument, a Matplotlib
        figure is created and contains the 3 graphics element of the array
        as 3 Matplotlib ``Axes``::

            sage: fig = G.matplotlib()
            sage: fig
            <Figure size 640x480 with 3 Axes>
            sage: type(fig)
            <class 'matplotlib.figure.Figure'>

        Specifying the figure size (in inches)::

            sage: G.matplotlib(figsize=(8., 5.))
            <Figure size 800x500 with 3 Axes>

        If a single number is provided for ``figsize``, it is considered to be
        the width; the height is then computed according to Matplotlib's
        default aspect ratio (4/3)::

            sage: G.matplotlib(figsize=8.)
            <Figure size 800x600 with 3 Axes>

        An example of use with a preexisting created figure, created by
        ``pyplot``::

            sage: import matplotlib.pyplot as plt
            sage: fig1 = plt.figure(1)
            sage: fig1
            <Figure size 640x480 with 0 Axes>
            sage: fig_out = G.matplotlib(figure=fig1)
            sage: fig_out
            <Figure size 640x480 with 3 Axes>

        Note that the output figure is the same object as the input one::

            sage: fig_out is fig1
            True

        It has however been modified by ``G.matplotlib(figure=fig1)``, which
        has added 3 new ``Axes`` to it.

        Another example, with a figure created from scratch, via Matplolib's
        ``Figure``::

            sage: from matplotlib.figure import Figure
            sage: fig2 = Figure()
            sage: fig2
            <Figure size 640x480 with 0 Axes>
            sage: G.matplotlib(figure=fig2)
            <Figure size 640x480 with 3 Axes>
            sage: fig2
            <Figure size 640x480 with 3 Axes>
        """
    def save(self, filename, figsize=None, **kwds) -> None:
        """
        Save ``self`` to a file, in various formats.

        INPUT:

        - ``filename`` -- string; the file name. The image format is given by
          the extension, which can be one of the following:

            * ``.eps``,

            * ``.pdf``,

            * ``.png``,

            * ``.ps``,

            * ``.sobj`` (for a Sage object you can load later),

            * ``.svg``,

            * empty extension will be treated as ``.sobj``.

        - ``figsize`` -- (default: ``None``) width or [width, height] in inches
          of the Matplotlib figure; if none is provided, Matplotlib's default
          (6.4 x 4.8 inches) is used

        - ``kwds`` -- keyword arguments, like ``dpi=...``, passed to the
          plotter, see :meth:`show`

        EXAMPLES::

            sage: F = tmp_filename(ext='.png')
            sage: L = [plot(sin(k*x), (x,-pi,pi)) for k in [1..3]]
            sage: G = graphics_array(L)
            sage: G.save(F, dpi=500, axes=False)

        TESTS::

            sage: graphics_array([]).save(F)
            sage: graphics_array([[]]).save(F)
        """
    def save_image(self, filename=None, *args, **kwds) -> None:
        """
        Save an image representation of ``self``.  The image type is
        determined by the extension of the filename.  For example,
        this could be ``.png``, ``.jpg``, ``.gif``, ``.pdf``,
        ``.svg``.  Currently this is implemented by calling the
        :meth:`save` method of self, passing along all arguments and
        keywords.

        .. NOTE::

            Not all image types are necessarily implemented for all
            graphics types.  See :meth:`save` for more details.

        EXAMPLES::

            sage: plots = [[plot(m*cos(x + n*pi/4), (x, 0, 2*pi))
            ....:           for n in range(3)] for m in range(1,3)]
            sage: G = graphics_array(plots)
            sage: G.save_image(tmp_filename(ext='.png'))
        """
    def show(self, **kwds) -> None:
        """
        Show ``self`` immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        OPTIONAL INPUT:

        - ``dpi`` -- dots per inch

        - ``figsize`` -- width or [width, height] of the figure, in inches; the
          default is 6.4 x 4.8 inches

        - ``axes`` -- boolean; if ``True``, all individual graphics are
          endowed with axes; if ``False``, all axes are removed (this overrides
          the ``axes`` option set in each graphics)

        - ``frame`` -- boolean; if ``True``, all individual graphics are
          drawn with a frame around them; if ``False``, all frames are removed
          (this overrides the ``frame`` option set in each graphics)

        - ``fontsize`` -- positive integer, the size of fonts for the axes
          labels (this overrides the ``fontsize`` option set in each graphics)

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES:

        This draws a graphics array with four trig plots and no axes in any of
        the plots and a figure width of 4 inches::

            sage: G = graphics_array([[plot(sin), plot(cos)],
            ....:                     [plot(tan), plot(sec)]])
            sage: G.show(axes=False, figsize=4)

        .. PLOT::

            G = graphics_array([[plot(sin), plot(cos)], \\\n                                [plot(tan), plot(sec)]])
            sphinx_plot(G, axes=False, figsize=4)

        Same thing with a frame around each individual graphics::

            sage: G.show(axes=False, frame=True, figsize=4)

        .. PLOT::

            G = graphics_array([[plot(sin), plot(cos)], \\\n                                [plot(tan), plot(sec)]])
            sphinx_plot(G, axes=False, frame=True, figsize=4)

        Actually, many options are possible; for instance, we may set
        ``fontsize`` and ``gridlines``::

            sage: G.show(axes=False, frame=True, figsize=4, fontsize=8,
            ....:        gridlines='major')

        .. PLOT::

            G = graphics_array([[plot(sin), plot(cos)], \\\n                                [plot(tan), plot(sec)]])
            sphinx_plot(G, axes=False, frame=True, figsize=4, fontsize=8, \\\n                        gridlines='major')
        """
    def plot(self):
        """
        Return ``self`` since ``self`` is already a graphics object.

        EXAMPLES::

            sage: g1 = plot(cos, 0, 1)
            sage: g2 = circle((0,0), 1)
            sage: G = multi_graphics([g1, g2])
            sage: G.plot() is G
            True
        """
    def inset(self, graphics, pos=None, fontsize=None):
        """
        Add a graphics object as an inset.

        INPUT:

        - ``graphics`` -- the graphics object (instance of :class:`Graphics`)
          to be added as an inset

        - ``pos`` -- (default: ``None``) 4-tuple
          ``(left, bottom, width, height)`` specifying the location and
          relative size of the inset on the canvas, all quantities being
          expressed in fractions of the canvas width and height; if ``None``,
          the value ``(0.7, 0.7, 0.2, 0.2)`` is used

        - ``fontsize`` -- (default: ``None``)  integer, font size (in points)
          for the inset; if ``None``, the value of 6 points is used, unless
          ``fontsize`` has been explicitly set in the construction of
          ``graphics`` (in this case, it is not overwritten here)

        OUTPUT: instance of :class:`~sage.plot.multigraphics.MultiGraphics`

        EXAMPLES:

        Let us consider a graphics array of 2 elements::

            sage: G = graphics_array([plot(sin, (0, 2*pi)),
            ....:                     plot(cos, (0, 2*pi))])
            sage: G
            Graphics Array of size 1 x 2

        .. PLOT::

            G = graphics_array([plot(sin, (0, 2*pi)), plot(cos, (0, 2*pi))])
            sphinx_plot(G)

        and add some inset at the default position::

            sage: c = circle((0,0), 1, color='red', thickness=2, frame=True)
            sage: G.inset(c)
            Multigraphics with 3 elements

        .. PLOT::

            G = graphics_array([plot(sin, (0, 2*pi)), plot(cos, (0, 2*pi))])
            c = circle((0,0), 1, color='red', thickness=2, frame=True)
            sphinx_plot(G.inset(c))

        We may customize the position and font size of the inset::

            sage: G.inset(c, pos=(0.3, 0.7, 0.2, 0.2), fontsize=8)
            Multigraphics with 3 elements

        .. PLOT::

            G = graphics_array([plot(sin, (0, 2*pi)), plot(cos, (0, 2*pi))])
            c = circle((0,0), 1, color='red', thickness=2, frame=True)
            sphinx_plot(G.inset(c, pos=(0.3, 0.7, 0.2, 0.2), fontsize=8))
        """
    def position(self, index):
        """
        Return the position and relative size of an element of ``self`` on the
        canvas.

        INPUT:

        - ``index`` -- integer specifying which element of ``self``

        OUTPUT:

        - a 4-tuple ``(left, bottom, width, height)`` giving the location and
          relative size of the element on the canvas, all quantities being
          expressed in fractions of the canvas width and height

        EXAMPLES::

            sage: g1 = plot(sin(x^2), (x, 0, 4))
            sage: g2 = circle((0,0), 1, rgbcolor='red', fill=True, axes=False)
            sage: G = multi_graphics([g1, (g2, (0.15, 0.2, 0.1, 0.15))])
            sage: G.position(0)  # tol 1.0e-13
            (0.125, 0.11, 0.775, 0.77)
            sage: G.position(1)  # tol 1.0e-13
            (0.15, 0.2, 0.1, 0.15)
        """
    def append(self, graphics, pos=None) -> None:
        '''
        Append a graphics object to ``self``.

        INPUT:

        - ``graphics`` -- the graphics object (instance of :class:`Graphics`)
          to be added to ``self``

        - ``pos`` -- (default: ``None``) 4-tuple
          ``(left, bottom, width, height)`` specifying the location and size
          of ``graphics`` on the canvas, all quantities being in fractions of
          the canvas width and height; if ``None``, ``graphics`` is assumed to
          occupy the whole canvas, except for some padding; this corresponds to
          the default position
          ``(left, bottom, width, height) = (0.125, 0.11, 0.775, 0.77)``

        EXAMPLES:

        Let us consider a multigraphics with 2 elements::

            sage: g1 = plot(chebyshev_T(4, x), (x, -1, 1), title=\'n=4\')
            sage: g2 = plot(chebyshev_T(8, x), (x, -1, 1), title=\'n=8\',
            ....:           color=\'red\')
            sage: G = multi_graphics([(g1, (0.125, 0.2, 0.4, 0.4)),
            ....:                     (g2, (0.55, 0.4, 0.4, 0.4))])
            sage: G
            Multigraphics with 2 elements

        .. PLOT::

            g1 = plot(chebyshev_T(4, x), (x, -1, 1), title=\'n=4\')
            g2 = plot(chebyshev_T(8, x), (x, -1, 1), title=\'n=8\', color=\'red\')
            G = multi_graphics([(g1, (0.125, 0.2, 0.4, 0.4)), \\\n                                (g2, (0.55, 0.4, 0.4, 0.4))])
            sphinx_plot(G)

        We append a third plot to it::

            sage: g3 = plot(chebyshev_T(16, x), (x, -1, 1), title=\'n=16\',
            ....:           color=\'brown\')
            sage: G.append(g3, pos=(0.55, 0.11, 0.4, 0.15))
            sage: G
            Multigraphics with 3 elements

        .. PLOT::

            g1 = plot(chebyshev_T(4, x), (x, -1, 1), title=\'n=4\')
            g2 = plot(chebyshev_T(8, x), (x, -1, 1), title=\'n=8\', color=\'red\')
            G = multi_graphics([(g1, (0.125, 0.2, 0.4, 0.4)), \\\n                                (g2, (0.55, 0.4, 0.4, 0.4))])
            g3 = plot(chebyshev_T(16, x), (x, -1, 1), title=\'n=16\', \\\n                      color=\'brown\')
            G.append(g3, pos=(0.55, 0.11, 0.4, 0.15))
            sphinx_plot(G)

        We may use ``append`` to add a title::

            sage: title = text("Chebyshev polynomials", (0, 0), fontsize=16,
            ....:              axes=False)
            sage: G.append(title, pos=(0.18, 0.8, 0.7, 0.1))
            sage: G
            Multigraphics with 4 elements

        .. PLOT::

            g1 = plot(chebyshev_T(4, x), (x, -1, 1), title=\'n=4\')
            g2 = plot(chebyshev_T(8, x), (x, -1, 1), title=\'n=8\', color=\'red\')
            G = multi_graphics([(g1, (0.125, 0.2, 0.4, 0.4)), \\\n                                (g2, (0.55, 0.4, 0.4, 0.4))])
            g3 = plot(chebyshev_T(16, x), (x, -1, 1), title=\'n=16\', \\\n                      color=\'brown\')
            G.append(g3, pos=(0.55, 0.11, 0.4, 0.15))
            title = text("Chebyshev polynomials", (0, 0), fontsize=16, \\\n                         axes=False)
            G.append(title, pos=(0.18, 0.8, 0.7, 0.1))
            sphinx_plot(G)

        .. SEEALSO::

            :meth:`inset`
        '''

class GraphicsArray(MultiGraphics):
    """
    This class implements 2-dimensional graphical objects that constitute
    an array of :class:`~sage.plot.graphics.Graphics` drawn on a single
    canvas.

    The user interface is through the function
    :func:`~sage.plot.plot.graphics_array`.

    INPUT:

    - ``array`` -- either a list of lists of
      :class:`~sage.plot.graphics.Graphics` elements (generic case) or a
      single list of :class:`~sage.plot.graphics.Graphics` elements (case of a
      single-row array)

    EXAMPLES:

    An array made of four graphics objects::

        sage: g1 = plot(sin(x^2), (x, 0, 6), axes_labels=['$x$', '$y$'],
        ....:           axes=False, frame=True, gridlines='minor')
        sage: y = var('y')
        sage: g2 = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3),
        ....:                      aspect_ratio=1)
        sage: g3 = graphs.DodecahedralGraph().plot()
        sage: g4 = polar_plot(sin(5*x)^2, (x, 0, 2*pi), color='green',
        ....:                 fontsize=8) \\\n        ....:      + circle((0,0), 0.5, rgbcolor='red', fill=True, alpha=0.1,
        ....:               legend_label='pink')
        sage: g4.set_legend_options(loc='upper right')
        sage: G = graphics_array([[g1, g2], [g3, g4]])
        sage: G
        Graphics Array of size 2 x 2

    .. PLOT::

        g1 = plot(sin(x**2), (x, 0, 6), axes_labels=['$x$', '$y$'], \\\n                  axes=False, frame=True, gridlines='minor')
        y = var('y')
        g2 = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3), \\\n                             aspect_ratio=1)
        g3 = graphs.DodecahedralGraph().plot()
        g4 = polar_plot(sin(5*x)**2, (x, 0, 2*pi), color='green', fontsize=8) \\\n             + circle((0,0), 0.5, rgbcolor='red', fill=True, alpha=0.1, \\\n                      legend_label='pink')
        g4.set_legend_options(loc='upper right')
        G = graphics_array([[g1, g2], [g3, g4]])
        sphinx_plot(G)

    If one constructs the graphics array from a single list of graphics
    objects, one obtains a single-row array::

        sage: G = graphics_array([g1, g2, g3, g4])
        sage: G
        Graphics Array of size 1 x 4

    .. PLOT::

        g1 = plot(sin(x**2), (x, 0, 6), axes_labels=['$x$', '$y$'], \\\n                  axes=False, frame=True, gridlines='minor')
        y = var('y')
        g2 = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3), \\\n                             aspect_ratio=1)
        g3 = graphs.DodecahedralGraph().plot()
        g4 = polar_plot(sin(5*x)**2, (x, 0, 2*pi), color='green', fontsize=8) \\\n             + circle((0,0), 0.5, rgbcolor='red', fill=True, alpha=0.1, \\\n                      legend_label='pink')
        g4.set_legend_options(loc='upper right')
        G = graphics_array([g1, g2, g3, g4])
        sphinx_plot(G)

    We note that the overall aspect ratio of the figure is 4/3 (the default),
    which makes ``g1`` elongated, while the aspect ratio of ``g2``, which has
    been specified with the parameter ``aspect_ratio=1`` is preserved. To get
    a better aspect ratio for the whole figure, one can use the option
    ``figsize`` in the method :meth:`~MultiGraphics.show`::

        sage: G.show(figsize=[8, 3])

    .. PLOT::

        g1 = plot(sin(x**2), (x, 0, 6), axes_labels=['$x$', '$y$'], \\\n                  axes=False, frame=True, gridlines='minor')
        y = var('y')
        g2 = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3), \\\n                             aspect_ratio=1)
        g3 = graphs.DodecahedralGraph().plot()
        g4 = polar_plot(sin(5*x)**2, (x, 0, 2*pi), color='green', fontsize=8) \\\n             + circle((0,0), 0.5, rgbcolor='red', fill=True, alpha=0.1, \\\n                      legend_label='pink')
        g4.set_legend_options(loc='upper right')
        G = graphics_array([g1, g2, g3, g4])
        sphinx_plot(G, figsize=[8, 3])

    We can access individual elements of the graphics array with the
    square-bracket operator::

        sage: G = graphics_array([[g1, g2], [g3, g4]])  # back to the 2x2 array
        sage: print(G)
        Graphics Array of size 2 x 2
        sage: G[0] is g1
        True
        sage: G[1] is g2
        True
        sage: G[2] is g3
        True
        sage: G[3] is g4
        True

    Note that with respect to the square-bracket operator, ``G`` is considered
    as a flattened list of graphics objects, not as an array. For instance,
    ``G[0, 1]`` throws an error::

        sage: G[0, 1]
        Traceback (most recent call last):
        ...
        TypeError: list indices must be integers or slices, not tuple

    ``G[:]`` returns the full (flattened) list of graphics objects composing
    ``G``::

        sage: G[:]
        [Graphics object consisting of 1 graphics primitive,
        Graphics object consisting of 1 graphics primitive,
        Graphics object consisting of 51 graphics primitives,
        Graphics object consisting of 2 graphics primitives]

    The total number of Graphics objects composing the array is returned
    by the function ``len``::

        sage: len(G)
        4

    The square-bracket operator can be used to replace elements in the array::

        sage: G[0] = g4
        sage: G
        Graphics Array of size 2 x 2

    .. PLOT::

        g1 = plot(sin(x**2), (x, 0, 6), axes_labels=['$x$', '$y$'], \\\n                  axes=False, frame=True, gridlines='minor')
        y = var('y')
        g2 = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3), \\\n                             aspect_ratio=1)
        g3 = graphs.DodecahedralGraph().plot()
        g4 = polar_plot(sin(5*x)**2, (x, 0, 2*pi), color='green', fontsize=8) \\\n             + circle((0,0), 0.5, rgbcolor='red', fill=True, alpha=0.1, \\\n                      legend_label='pink')
        g4.set_legend_options(loc='upper right')
        G = graphics_array([[g1, g2], [g3, g4]])
        G[0] = g4
        sphinx_plot(G)
    """
    def __init__(self, array) -> None:
        """
        Construct a ``GraphicsArray``.

        TESTS::

            sage: from sage.plot.multigraphics import GraphicsArray
            sage: g = circle((0,0), 1)  # a Graphics object
            sage: G = GraphicsArray([[g, g], [g, g]])
            sage: print(G)
            Graphics Array of size 2 x 2

        Construction from a single list ==> 1-row array::

            sage: G = GraphicsArray([g, g, g])
            sage: print(G)
            Graphics Array of size 1 x 3
            sage: G = GraphicsArray([g])
            sage: print(G)
            Graphics Array of size 1 x 1

        Empty array::

            sage: G = GraphicsArray([])
            sage: print(G)
            Graphics Array of size 0 x 0
            sage: len(G)
            0
            sage: G = GraphicsArray([[]])
            sage: print(G)
            Graphics Array of size 1 x 0
            sage: len(G)
            0

        Check treatment of wrong inputs::

            sage: G = GraphicsArray([[g, g], [g]])
            Traceback (most recent call last):
            ...
            TypeError: array must be a list of equal-size lists of Graphics
             objects, not [[Graphics object consisting of 1 graphics primitive,
             Graphics object consisting of 1 graphics primitive],
             [Graphics object consisting of 1 graphics primitive]]
            sage: G = GraphicsArray(g)
            Traceback (most recent call last):
            ...
            TypeError: array must be a list of lists of Graphics objects, not
             Graphics object consisting of 1 graphics primitive
            sage: G = GraphicsArray([g, x])
            Traceback (most recent call last):
            ...
            TypeError: every element of array must be a Graphics object
        """
    def nrows(self):
        """
        Number of rows of the graphics array.

        EXAMPLES::

            sage: R = rainbow(6)
            sage: L = [plot(x^n, (x,0,1), color=R[n]) for n in range(6)]
            sage: G = graphics_array(L, 2, 3)
            sage: G.nrows()
            2
            sage: graphics_array(L).nrows()
            1
        """
    def ncols(self):
        """
        Number of columns of the graphics array.

        EXAMPLES::

            sage: R = rainbow(6)
            sage: L = [plot(x^n, (x,0,1), color=R[n]) for n in range(6)]
            sage: G = graphics_array(L, 2, 3)
            sage: G.ncols()
            3
            sage: graphics_array(L).ncols()
            6
        """
    def append(self, g) -> None:
        """
        Append a graphics to the array.

        Currently not implemented.

        TESTS::

            sage: from sage.plot.multigraphics import GraphicsArray
            sage: c = circle((0,0), 1)
            sage: G = GraphicsArray([c, c])
            sage: G.append(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: Appending to a graphics array is not yet
             implemented
        """
    def position(self, index):
        '''
        Return the position and relative size of an element of ``self`` on the
        canvas.

        INPUT:

        - ``index`` -- integer specifying which element of ``self``

        OUTPUT:

        - a 4-tuple ``(left, bottom, width, height)`` giving the location and
          relative size of the element on the canvas, all quantities being
          expressed in fractions of the canvas width and height

        EXAMPLES::

            sage: g1 = plot(sin(x), (x, -pi, pi))
            sage: g2 = circle((0,1), 1.)
            sage: G = graphics_array([g1, g2])
            sage: import numpy  # to ensure numpy 2.0 compatibility
            sage: if int(numpy.version.short_version[0]) > 1:
            ....:     _ = numpy.set_printoptions(legacy="1.25")
            sage: G.position(0)  # tol 5.0e-3
            (0.025045451349937315,
             0.03415488992713045,
             0.4489880779745068,
             0.9345951100728696)
            sage: G.position(1)  # tol 5.0e-3
            (0.5170637412999687,
             0.20212705964722733,
             0.4489880779745068,
             0.5986507706326758)
        '''
