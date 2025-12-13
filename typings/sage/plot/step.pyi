from sage.plot.line import line as line

def plot_step_function(v, vertical_lines: bool = True, **kwds):
    '''
    Return the line graphics object that gives the plot of the step
    function `f` defined by the list `v` of pairs `(a,b)`.  Here if
    `(a,b)` is in `v`, then `f(a) = b`.  The user does not have to
    worry about sorting the input list `v`.

    INPUT:

    - ``v`` -- list of pairs (a,b)

    - ``vertical_lines`` -- boolean (default: ``True``); if ``True``, draw
      vertical risers at each step of this step function.
      Technically these vertical lines are not part of the graph
      of this function, but they look very nice in the plot, so we
      include them by default.

    EXAMPLES:

    We plot the prime counting function::

        sage: plot_step_function([(i, prime_pi(i)) for i in range(20)])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(plot_step_function([(i, prime_pi(i)) for i in range(20)]))

    ::

        sage: plot_step_function([(i, sin(i)) for i in range(5, 20)])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(plot_step_function([(i, sin(i)) for i in range(5, 20)]))

    We pass in many options and get something that looks like "Space Invaders"::

        sage: v = [(i, sin(i)) for i in range(5, 20)]
        sage: plot_step_function(v, vertical_lines=False, thickness=30,
        ....:                    rgbcolor=\'purple\', axes=False)
        Graphics object consisting of 14 graphics primitives

    .. PLOT::

        v = [(i, sin(i)) for i in range(5, 20)]
        sphinx_plot(plot_step_function(v, vertical_lines=False, thickness=30, rgbcolor=\'purple\', axes=False))
    '''
