from _typeshed import Incomplete
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.real_double import RDF as RDF
from sage.structure.sage_object import SageObject as SageObject

class ToricPlotter(SageObject):
    '''
    Create a toric plotter.

    INPUT:

    - ``all_options`` -- a :class:`dictionary <dict>`, containing any of the
      options related to toric objects (see :func:`options`) and any other
      options that will be passed to lower level plotting functions

    - ``dimension`` -- integer (1, 2, or 3); dimension of toric objects to
      be plotted

    - ``generators`` -- (optional) a list of ray generators; see examples for
      a detailed explanation of this argument

    OUTPUT: a toric plotter

    EXAMPLES:

    In most cases there is no need to create and use :class:`ToricPlotter`
    directly. Instead, use plotting method of the object which you want to
    plot, e.g. ::

        sage: fan = toric_varieties.dP6().fan()                                         # needs palp sage.graphs
        sage: fan.plot()                                                                # needs palp sage.graphs sage.plot
        Graphics object consisting of 31 graphics primitives
        sage: print(fan.plot())                                                         # needs palp sage.graphs sage.plot
        Graphics object consisting of 31 graphics primitives

    If you do want to create your own plotting function for some toric
    structure, the anticipated usage of toric plotters is the following:

    - collect all necessary options in a dictionary;

    - pass these options and ``dimension`` to :class:`ToricPlotter`;

    - call :meth:`include_points` on ray generators and any other points that
      you want to be present on the plot (it will try to set appropriate
      cut-off bounds);

    - call :meth:`adjust_options` to choose "nice" default values for all
      options that were not set yet and ensure consistency of rectangular and
      spherical cut-off bounds;

    - call :meth:`set_rays` on ray generators to scale them to the cut-off
      bounds of the plot;

    - call appropriate ``plot_*`` functions to actually construct the plot.

    For example, the plot from the previous example can be obtained as
    follows::

        sage: # needs palp sage.graphs sage.plot
        sage: from sage.geometry.toric_plotter import ToricPlotter
        sage: options = dict()  # use default for everything
        sage: tp = ToricPlotter(options, fan.lattice().degree())
        sage: tp.include_points(fan.rays())
        sage: tp.adjust_options()
        sage: tp.set_rays(fan.rays())
        sage: result = tp.plot_lattice()
        sage: result += tp.plot_rays()
        sage: result += tp.plot_generators()
        sage: result += tp.plot_walls(fan(2))
        sage: result
        Graphics object consisting of 31 graphics primitives

    In most situations it is only necessary to include generators of rays, in
    this case they can be passed to the constructor as an optional argument.
    In the example above, the toric plotter can be completely set up using ::

        sage: tp = ToricPlotter(options, fan.lattice().degree(), fan.rays())            # needs palp sage.graphs sage.plot

    All options are exposed as attributes of toric plotters and can be modified
    after constructions, however you will have to manually call
    :meth:`adjust_options` and :meth:`set_rays` again if you decide to change
    the plotting mode and/or cut-off bounds. Otherwise plots maybe invalid.
    '''
    extra_options: Incomplete
    dimension: Incomplete
    origin: Incomplete
    def __init__(self, all_options, dimension, generators=None) -> None:
        """
        See :class:`ToricPlotter` for documentation.

        TESTS::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: TestSuite(tp).run()
        """
    def __eq__(self, other):
        """
        Check if ``self`` is equal to ``other``.

        INPUT:

        - ``other`` -- anything

        OUTPUT: ``True`` if ``self`` is equal to ``other``, ``False`` otherwise

        TESTS::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: ToricPlotter(dict(), 2) == ToricPlotter(dict(), 2)
            True
            sage: ToricPlotter(dict(), 2) == 0
            False
        """
    point_size: int
    generator_thickness: Incomplete
    radius: Incomplete
    show_lattice: Incomplete
    def adjust_options(self) -> None:
        """
        Adjust plotting options.

        This function determines appropriate default values for those options,
        that were not specified by the user, based on the other options. See
        :class:`ToricPlotter` for a detailed example.

        OUTPUT: none

        TESTS::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: print(tp.show_lattice)
            None
            sage: tp.adjust_options()
            sage: print(tp.show_lattice)
            True
        """
    def include_points(self, points, force: bool = False) -> None:
        """
        Try to include ``points`` into the bounding box of ``self``.

        INPUT:

        - ``points`` -- list of points

        - ``force`` -- boolean (default: ``False``); by default, only bounds
          that were not set before will be chosen to include ``points``. Use
          ``force=True`` if you don't mind increasing existing bounding box.

        OUTPUT: none

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: print(tp.radius)
            None
            sage: tp.include_points([(3, 4)])
            sage: print(tp.radius)
            5.5...
            sage: tp.include_points([(5, 12)])
            sage: print(tp.radius)
            5.5...
            sage: tp.include_points([(5, 12)], force=True)
            sage: print(tp.radius)
            13.5...
        """
    def plot_generators(self):
        """
        Plot ray generators.

        Ray generators must be specified during construction or using
        :meth:`set_rays` before calling this method.

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2, [(3,4)])
            sage: tp.plot_generators()                                                  # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def plot_labels(self, labels, positions):
        '''
        Plot ``labels`` at specified ``positions``.

        INPUT:

        - ``labels`` -- string or list of strings

        - ``positions`` -- list of points

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: tp.plot_labels("u", [(1.5,0)])                                        # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        '''
    def plot_lattice(self):
        """
        Plot the lattice (i.e. its points in the cut-off bounds of ``self``).

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: tp.adjust_options()
            sage: tp.plot_lattice()                                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def plot_points(self, points):
        """
        Plot given ``points``.

        INPUT:

        - ``points`` -- list of points

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: tp.adjust_options()
            sage: tp.plot_points([(1,0), (0,1)])                                        # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def plot_ray_labels(self):
        """
        Plot ray labels.

        Usually ray labels are plotted together with rays, but in some cases it
        is desirable to output them separately.

        Ray generators must be specified during construction or using
        :meth:`set_rays` before calling this method.

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2, [(3,4)])
            sage: tp.plot_ray_labels()                                                  # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def plot_rays(self):
        """
        Plot rays and their labels.

        Ray generators must be specified during construction or using
        :meth:`set_rays` before calling this method.

        OUTPUT: a plot

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2, [(3,4)])
            sage: tp.plot_rays()                                                        # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """
    def plot_walls(self, walls):
        '''
        Plot ``walls``, i.e. 2-d cones, and their labels.

        Ray generators must be specified during construction or using
        :meth:`set_rays` before calling this method and these specified
        ray generators will be used in conjunction with
        :meth:`~sage.geometry.cone.ConvexRationalPolyhedralCone.ambient_ray_indices`
        of ``walls``.

        INPUT:

        - ``walls`` -- list of 2-d cones

        OUTPUT: a plot

        EXAMPLES::

            sage: quadrant = Cone([(1,0), (0,1)])
            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2, quadrant.rays())
            sage: tp.plot_walls([quadrant])                                             # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        Let\'s also check that the truncating polyhedron is functioning
        correctly::

            sage: tp = ToricPlotter({"mode": "box"}, 2, quadrant.rays())
            sage: tp.plot_walls([quadrant])                                             # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        '''
    generators: Incomplete
    rays: Incomplete
    def set_rays(self, generators) -> None:
        """
        Set up rays and their ``generators`` to be used by plotting functions.

        As an alternative to using this method, you can pass ``generators`` to
        :class:`ToricPlotter` constructor.

        INPUT:

        - ``generators`` -- list of primitive nonzero ray generators

        OUTPUT: none

        EXAMPLES::

            sage: from sage.geometry.toric_plotter import ToricPlotter
            sage: tp = ToricPlotter(dict(), 2)
            sage: tp.adjust_options()
            sage: tp.plot_rays()                                                        # needs sage.plot
            Traceback (most recent call last):
            ...
            AttributeError: 'ToricPlotter' object has no attribute 'rays'...
            sage: tp.set_rays([(0,1)])
            sage: tp.plot_rays()                                                        # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """

def color_list(color, n):
    '''
    Normalize a list of ``n`` colors.

    INPUT:

    - ``color`` -- anything specifying a :class:`Color`, a list of such
      specifications, or the string "rainbow";

    - ``n`` -- integer

    OUTPUT: list of ``n`` colors

    If ``color`` specified a single color, it is repeated ``n`` times. If it
    was a list of ``n`` colors, it is returned without changes. If it was
    "rainbow", the rainbow of ``n`` colors is returned.

    EXAMPLES::

        sage: # needs sage.plot
        sage: from sage.geometry.toric_plotter import color_list
        sage: color_list("grey", 1)
        [RGB color (0.5019607843137255, 0.5019607843137255, 0.5019607843137255)]
        sage: len(color_list("grey", 3))
        3
        sage: L = color_list("rainbow", 3)
        sage: L
        [RGB color (1.0, 0.0, 0.0),
         RGB color (0.0, 1.0, 0.0),
         RGB color (0.0, 0.0, 1.0)]
        sage: color_list(L, 3)
        [RGB color (1.0, 0.0, 0.0),
         RGB color (0.0, 1.0, 0.0),
         RGB color (0.0, 0.0, 1.0)]
        sage: color_list(L, 4)
        Traceback (most recent call last):
        ...
        ValueError: expected 4 colors, got 3!
    '''
def label_list(label, n, math_mode, index_set=None):
    '''
    Normalize a list of ``n`` labels.

    INPUT:

    - ``label`` -- ``None``, a string, or a list of string

    - ``n`` -- integer

    - ``math_mode`` -- boolean; if ``True``, will produce LaTeX expressions
      for labels

    - ``index_set`` -- list of integers (default: ``range(n)``) that will be
      used as subscripts for labels

    OUTPUT: list of ``n`` labels

    If ``label`` was a list of ``n`` entries, it is returned without changes.
    If ``label`` is ``None``, a list of ``n`` ``None``\'s is returned. If
    ``label`` is a string, a list of strings of the form ``$label_{i}$`` is
    returned, where `i` ranges over ``index_set``. (If ``math_mode=False``, the
    form "label_i" is used instead.) If ``n=1``, there is no subscript added,
    unless ``index_set`` was specified explicitly.

    EXAMPLES::

        sage: from sage.geometry.toric_plotter import label_list
        sage: label_list("u", 3, False)
        [\'u_0\', \'u_1\', \'u_2\']
        sage: label_list("u", 3, True)
        [\'$u_{0}$\', \'$u_{1}$\', \'$u_{2}$\']
        sage: label_list("u", 1, True)
        [\'$u$\']
    '''
def options(option=None, **kwds):
    '''
    Get or set options for plots of toric geometry objects.

    .. NOTE::

        This function provides access to global default options. Any of these
        options can be overridden by passing them directly to plotting
        functions. See also :func:`reset_options`.

    INPUT:

    - None;

    OR:

    - ``option`` -- string, name of the option whose value you wish to get;

    OR:

    - keyword arguments specifying new values for one or more options.

    OUTPUT:

    - if there was no input, the dictionary of current options for toric plots;

    - if ``option`` argument was given, the current value of ``option``;

    - if other keyword arguments were given, none.

    **Name Conventions**

    To clearly distinguish parts of toric plots, in options and methods we use
    the following name conventions:

    Generator
        A primitive integral vector generating a 1-dimensional cone, plotted as
        an arrow from the origin (or a line, if the head of the arrow is beyond
        cut-off bounds for the plot).

    Ray
        A 1-dimensional cone, plotted as a line from the origin to the cut-off
        bounds for  the plot.

    Wall
        A 2-dimensional cone, plotted as a region between rays (in the above
        sense). Its exact shape depends on the plotting mode (see below).

    Chamber
        A 3-dimensional cone, plotting is not implemented yet.

    **Plotting Modes**

    A plotting mode mostly determines the shape of the cut-off region (which is
    always relevant for toric plots except for trivial objects consisting of
    the origin only). The following options are available:

    Box
        The cut-off region is a box with edges parallel to coordinate axes.

    Generators
        The cut-off region is determined by primitive integral generators of
        rays. Note that this notion is well-defined only for rays and walls,
        in particular you should plot the lattice on your own
        (:meth:`~ToricPlotter.plot_lattice` will use box mode which is likely
        to be unsuitable). While this method may not be suitable for general
        fans, it is quite natural for fans of :class:`CPR-Fano toric varieties.
        <sage.schemes.toric.fano_variety.CPRFanoToricVariety_field`

    Round
        The cut-off regions is a sphere centered at the origin.

    **Available Options**

    Default values for the following options can be set using this function:


    - ``mode`` -- "box", "generators", or "round", see above for descriptions;

    - ``show_lattice`` -- boolean, whether to show lattice points in the
      cut-off region or not;

    - ``show_rays`` -- boolean, whether to show rays or not;

    - ``show_generators`` -- boolean, whether to show rays or not;

    - ``show_walls`` -- boolean, whether to show rays or not;

    - ``generator_color`` -- a color for generators;

    - ``label_color`` -- a color for labels;

    - ``point_color`` -- a color for lattice points;

    - ``ray_color`` -- a color for rays, a list of colors (one for each ray),
      or the string "rainbow";

    - ``wall_color`` -- a color for walls, a list of colors (one for each
      wall), or the string "rainbow";

    - ``wall_alpha`` -- a number between 0 and 1, the alpha-value for walls
      (determining their transparency);

    - ``point_size`` -- integer; the size of lattice points

    - ``ray_thickness`` -- integer; the thickness of rays

    - ``generator_thickness`` -- integer; the thickness of generators

    - ``font_size`` -- integer; the size of font used for labels

    - ``ray_label`` -- string or list of strings used for ray labels; use
      ``None`` to hide labels

    - ``wall_label`` -- string or list of strings used for wall labels; use
      ``None`` to hide labels

    - ``radius`` -- a positive number, the radius of the cut-off region for
      "round" mode

    - ``xmin``, ``xmax``, ``ymin``, ``ymax``, ``zmin``, ``zmax`` -- numbers
      determining the cut-off region for "box" mode. Note that you cannot
      exclude the origin - if you try to do so, bounds will be automatically
      expanded to include it.

    - ``lattice_filter`` -- a callable, taking as an argument a lattice point
      and returning ``True`` if this point should be included on the plot
      (useful, e.g. for plotting sublattices)

    - ``wall_zorder``, ``ray_zorder``, ``generator_zorder``, ``point_zorder``,
      ``label_zorder`` -- integers, z-orders for different classes of objects.
      By default all values are negative, so that you can add other graphic
      objects on top of a toric plot. You may need to adjust these parameters
      if you want to put a toric plot on top of something else or if you want
      to overlap several toric plots.

    You can see the current default value of any options by typing, e.g. ::

        sage: toric_plotter.options("show_rays")
        True

    If the default value is ``None``, it means that the actual default is
    determined later based on the known options. Note, that not all options can
    be determined in such a way, so you should not set options to ``None``
    unless it was its original state. (You can always revert to this "original
    state" using :meth:`reset_options`.)

    EXAMPLES:

    The following line will make all subsequent toric plotting commands to draw
    "rainbows" from walls::

        sage: toric_plotter.options(wall_color=\'rainbow\')

    If you prefer a less colorful output (e.g. if you need black-and-white
    illustrations for a paper), you can use something like this::

        sage: toric_plotter.options(wall_color=\'grey\')
    '''
def reset_options() -> None:
    '''
    Reset options for plots of toric geometry objects.

    OUTPUT: none

    EXAMPLES::

        sage: toric_plotter.options("show_rays")
        True
        sage: toric_plotter.options(show_rays=False)
        sage: toric_plotter.options("show_rays")
        False

    Now all toric plots will not show rays, unless explicitly requested. If you
    want to go back to "default defaults", use this method::

        sage: toric_plotter.reset_options()
        sage: toric_plotter.options("show_rays")
        True
    '''
def sector(ray1, ray2, **extra_options):
    """
    Plot a sector between ``ray1`` and ``ray2`` centered at the origin.

    .. NOTE::

        This function was intended for plotting strictly convex cones, so it
        plots the smaller sector between ``ray1`` and ``ray2`` and, therefore,
        they cannot be opposite. If you do want to use this function for bigger
        regions, split them into several parts.

    .. NOTE::

        As of version 4.6 Sage does not have a graphic primitive for sectors in
        3-dimensional space, so this function will actually approximate them
        using polygons (the number of vertices used depends on the angle
        between rays).

    INPUT:

    - ``ray1``, ``ray2`` -- rays in 2- or 3-dimensional space of the same
      length

    - ``extra_options`` -- dictionary of options that should be passed to
      lower level plotting functions

    OUTPUT: a plot

    EXAMPLES::

        sage: from sage.geometry.toric_plotter import sector
        sage: sector((1,0), (0,1))                                                      # needs sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: sector((3,2,1), (1,2,3))                                                  # needs sage.plot
        Graphics3d Object
    """
