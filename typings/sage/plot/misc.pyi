from sage.ext.fast_callable import FastCallableFloatWrapper as FastCallableFloatWrapper

def setup_for_eval_on_grid(funcs, ranges, plot_points=None, return_vars: bool = False, imaginary_tolerance: float = 1e-08):
    """
    Calculate the necessary parameters to construct a list of points,
    and make the functions fast_callable.

    INPUT:

    - ``funcs`` -- a function, or a list, tuple, or vector of functions

    - ``ranges`` -- list of ranges.  A range can be a 2-tuple of
      numbers specifying the minimum and maximum, or a 3-tuple giving
      the variable explicitly.

    - ``plot_points`` -- tuple of integers specifying the number of
      plot points for each range.  If a single number is specified, it
      will be the value for all ranges.  This defaults to 2.

    - ``return_vars`` -- (default: ``False``) if ``True``, return the variables,
      in order

    - ``imaginary_tolerance`` -- (default: ``1e-8``) if an imaginary
      number arises (due, for example, to numerical issues), this
      tolerance specifies how large it has to be in magnitude before
      we raise an error. In other words, imaginary parts smaller than
      this are ignored in your plot points.

    OUTPUT:

    - ``fast_funcs`` -- if only one function passed, then a fast
      callable function.  If funcs is a list or tuple, then a tuple
      of fast callable functions is returned.

    - ``range_specs`` -- list of range_specs: for each range, a
      tuple is returned of the form (range_min, range_max,
      range_step) such that ``srange(range_min, range_max,
      range_step, include_endpoint=True)`` gives the correct points
      for evaluation.

    EXAMPLES::

        sage: x,y,z = var('x,y,z')
        sage: f(x,y) = x+y-z
        sage: g(x,y) = x+y
        sage: h(y) = -y
        sage: sage.plot.misc.setup_for_eval_on_grid(f, [(0, 2),(1,3),(-4,1)], plot_points=5)
        (<sage...>, [(0.0, 2.0, 0.5), (1.0, 3.0, 0.5), (-4.0, 1.0, 1.25)])
        sage: sage.plot.misc.setup_for_eval_on_grid([g,h], [(0, 2),(-1,1)], plot_points=5)
        ((<sage...>, <sage...>), [(0.0, 2.0, 0.5), (-1.0, 1.0, 0.5)])
        sage: sage.plot.misc.setup_for_eval_on_grid([sin,cos], [(-1,1)], plot_points=9)
        ((<sage...>, <sage...>), [(-1.0, 1.0, 0.25)])
        sage: sage.plot.misc.setup_for_eval_on_grid([lambda x: x^2,cos], [(-1,1)], plot_points=9)
        ((<function <lambda> ...>, <sage...>), [(-1.0, 1.0, 0.25)])
        sage: sage.plot.misc.setup_for_eval_on_grid([x+y], [(x,-1,1),(y,-2,2)])
        ((<sage...>,), [(-1.0, 1.0, 2.0), (-2.0, 2.0, 4.0)])
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x,-1,1),(y,-1,1)], plot_points=[4,9])
        (<sage...>, [(-1.0, 1.0, 0.6666666666666666), (-1.0, 1.0, 0.25)])
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x,-1,1),(y,-1,1)], plot_points=[4,9,10])
        Traceback (most recent call last):
        ...
        ValueError: plot_points must be either an integer or a list of integers, one for each range
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(1,-1),(y,-1,1)], plot_points=[4,9,10])
        Traceback (most recent call last):
        ...
        ValueError: Some variable ranges specify variables while others do not

    Beware typos: a comma which should be a period, for instance::

        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x, 1, 2), (y, 0,1, 0.2)], plot_points=[4,9,10])
        Traceback (most recent call last):
        ...
        ValueError: At least one variable range has more than 3 entries: each should either have 2 or 3 entries, with one of the forms (xmin, xmax) or (x, xmin, xmax)

        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(y,1,-1),(x,-1,1)], plot_points=5)
        (<sage...>, [(-1.0, 1.0, 0.5), (-1.0, 1.0, 0.5)])
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x,1,-1),(x,-1,1)], plot_points=5)
        Traceback (most recent call last):
        ...
        ValueError: range variables should be distinct, but there are duplicates
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x,1,1),(y,-1,1)])
        Traceback (most recent call last):
        ...
        ValueError: plot start point and end point must be different
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(x,1,-1),(y,-1,1)], return_vars=True)
        (<sage...>, [(-1.0, 1.0, 2.0), (-1.0, 1.0, 2.0)], [x, y])
        sage: sage.plot.misc.setup_for_eval_on_grid(x+y, [(y,1,-1),(x,-1,1)], return_vars=True)
        (<sage...>, [(-1.0, 1.0, 2.0), (-1.0, 1.0, 2.0)], [y, x])

    TESTS:

    Ensure that we can plot expressions with intermediate complex
    terms as in :issue:`8450`::

        sage: x, y = SR.var('x y')
        sage: contour_plot(abs(x+i*y), (x,-1,1), (y,-1,1))
        Graphics object consisting of 1 graphics primitive
        sage: density_plot(abs(x+i*y), (x,-1,1), (y,-1,1))
        Graphics object consisting of 1 graphics primitive
        sage: plot3d(abs(x+i*y), (x,-1,1),(y,-1,1))
        Graphics3d Object
        sage: streamline_plot(abs(x+i*y), (x,-1,1),(y,-1,1))
        Graphics object consisting of 1 graphics primitive
    """
def unify_arguments(funcs):
    '''
    Return a tuple of variables of the functions, as well as the
    number of "free" variables (i.e., variables that defined in a
    callable function).

    INPUT:

    - ``funcs`` -- list of functions; these can be symbolic
      expressions, polynomials, etc.

    OUTPUT: functions, expected arguments

    - A tuple of variables in the functions

    - A tuple of variables that were "free" in the functions

    EXAMPLES::

        sage: x,y,z = var(\'x,y,z\')
        sage: f(x,y) = x+y-z
        sage: g(x,y) = x+y
        sage: h(y) = -y
        sage: sage.plot.misc.unify_arguments((f,g,h))
        ((x, y, z), (z,))
        sage: sage.plot.misc.unify_arguments((g,h))
        ((x, y), ())
        sage: sage.plot.misc.unify_arguments((f,z))
        ((x, y, z), (z,))
        sage: sage.plot.misc.unify_arguments((h,z))
        ((y, z), (z,))
        sage: sage.plot.misc.unify_arguments((x+y,x-y))
        ((x, y), (x, y))
    '''
def get_matplotlib_linestyle(linestyle, return_type):
    '''
    Function which translates between matplotlib linestyle in short notation
    (i.e. \'-\', \'--\', \':\', \'-.\') and long notation (i.e. \'solid\', \'dashed\',
    \'dotted\', \'dashdot\' ).

    If linestyle is none of these allowed options, the function raises
    a :exc:`ValueError`.

    INPUT:

    - ``linestyle`` -- the style of the line, which is one of
       - ``\'-\'`` or ``\'solid\'``
       - ``\'--\'`` or ``\'dashed\'``
       - ``\'-.\'`` or ``\'dash dot\'``
       - ``\':\'`` or ``\'dotted\'``
       - ``"None"`` or ``" "`` or ``""`` (nothing)

       The linestyle can also be prefixed with a drawing style (e.g., ``\'steps--\'``)

       - ``\'default\'`` (connect the points with straight lines)
       - ``\'steps\'`` or ``\'steps-pre\'`` (step function; horizontal
         line is to the left of point)
       - ``\'steps-mid\'`` (step function; points are in the middle of
         horizontal lines)
       - ``\'steps-post\'`` (step function; horizontal line is to the
         right of point)

       If ``linestyle`` is ``None`` (of type NoneType), then we return it
       back unmodified.

    - ``return_type`` -- the type of linestyle that should be output. This
      argument takes only two values - ``\'long\'`` or ``\'short\'``

    EXAMPLES:

    Here is an example how to call this function::

        sage: from sage.plot.misc import get_matplotlib_linestyle
        sage: get_matplotlib_linestyle(\':\', return_type=\'short\')
        \':\'

        sage: get_matplotlib_linestyle(\':\', return_type=\'long\')
        \'dotted\'

    TESTS:

    Make sure that if the input is already in the desired format, then it
    is unchanged::

        sage: get_matplotlib_linestyle(\':\', \'short\')
        \':\'

    Empty linestyles should be handled properly::

        sage: get_matplotlib_linestyle("", \'short\')
        \'\'
        sage: get_matplotlib_linestyle("", \'long\')
        \'None\'
        sage: get_matplotlib_linestyle(None, \'short\') is None
        True

    Linestyles with ``\'default\'`` or ``\'steps\'`` in them should also be
    properly handled.  For instance, matplotlib understands only the short
    version when ``\'steps\'`` is used::

        sage: get_matplotlib_linestyle("default", "short")
        \'\'
        sage: get_matplotlib_linestyle("steps--", "short")
        \'steps--\'
        sage: get_matplotlib_linestyle("steps-predashed", "long")
        \'steps-pre--\'

    Finally, raise error on invalid linestyles::

        sage: get_matplotlib_linestyle("isthissage", "long")
        Traceback (most recent call last):
        ...
        ValueError: WARNING: Unrecognized linestyle \'isthissage\'. Possible
        linestyle options are:
        {\'solid\', \'dashed\', \'dotted\', dashdot\', \'None\'}, respectively {\'-\',
        \'--\', \':\', \'-.\', \'\'}
    '''

class FastCallablePlotWrapper(FastCallableFloatWrapper):
    '''
    A fast-callable wrapper for plotting that returns ``nan`` instead
    of raising an error whenever the imaginary tolerance is exceeded.

    A detailed rationale for this can be found in the superclass
    documentation.

    EXAMPLES:

    The ``float`` incarnation of "not a number" is returned instead
    of an error being thrown if the answer is complex::

        sage: from sage.plot.misc import FastCallablePlotWrapper
        sage: f = sqrt(x)
        sage: ff = fast_callable(f, vars=[x], domain=CDF)
        sage: fff = FastCallablePlotWrapper(ff, imag_tol=1e-8)
        sage: fff(1)
        1.0
        sage: fff(-1)
        nan
    '''
    def __call__(self, *args):
        """
        Evaluate the underlying fast-callable and convert the result to
        ``float``.

        TESTS:

        Evaluation never fails and always returns a ``float``::

            sage: from sage.plot.misc import FastCallablePlotWrapper
            sage: f = x
            sage: ff = fast_callable(f, vars=[x], domain=CDF)
            sage: fff = FastCallablePlotWrapper(ff, imag_tol=0.1)
            sage: type(fff(CDF.random_element())) is float
            True
        """
