from sage.matrix.constructor import matrix as matrix
from sage.misc.superseded import deprecation as deprecation
from sage.rings.real_double import RDF as RDF
from sage.structure.element import Matrix as Matrix

def list_plot3d(v, interpolation_type: str = 'default', point_list=None, **kwds):
    """
    A 3-dimensional plot of a surface defined by the list `v`
    of points in 3-dimensional space.

    INPUT:

    - ``v`` -- something that defines a set of points in 3 space:

      - a matrix

      - a list of 3-tuples

      - a list of lists (all of the same length) -- this is treated the same as
        a matrix

    OPTIONAL KEYWORDS:

    - ``interpolation_type`` -- 'linear', 'clough' (CloughTocher2D), 'spline'

      'linear' will perform linear interpolation

      The option 'clough' will interpolate by using a piecewise cubic
      interpolating Bezier polynomial on each triangle, using a
      Clough-Tocher scheme.  The interpolant is guaranteed to be
      continuously differentiable.  The gradients of the interpolant
      are chosen so that the curvature of the interpolating surface is
      approximately minimized.

      The option 'spline' interpolates using a bivariate B-spline.

      When v is a matrix the default is to use linear interpolation, when
      v is a list of points the default is 'clough'.

    - ``degree`` -- integer between 1 and 5, controls the degree of spline
      used for spline interpolation. For data that is highly oscillatory
      use higher values

    - ``point_list`` -- if ``point_list=True`` is passed, then if the array
      is a list of lists of length three, it will be treated as an
      array of points rather than a 3xn array.

    - ``num_points`` -- number of points to sample interpolating
      function in each direction, when ``interpolation_type`` is not
      ``default``. By default for an `n\\times n` array this is `n`.

    - ``**kwds`` -- all other arguments are passed to the surface function

    OUTPUT: a 3d plot

    EXAMPLES:

    We plot a matrix that illustrates summation modulo `n`::

        sage: n = 5
        sage: list_plot3d(matrix(RDF, n, [(i+j)%n for i in [1..n] for j in [1..n]]))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(list_plot3d(matrix(RDF, 5, [(i+j)%5 for i in range(1,6) for j in range(1,6)])))

    We plot a matrix of values of ``sin``::

        sage: from math import pi
        sage: m = matrix(RDF, 6, [sin(i^2 + j^2)
        ....:                     for i in [0,pi/5,..,pi] for j in [0,pi/5,..,pi]])
        sage: list_plot3d(m, color='yellow', frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        pi = float(pi)
        import numpy as np
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', frame_aspect_ratio=[1, 1, 1/3]))

    Though it does not change the shape of the graph, increasing
    ``num_points`` can increase the clarity of the graph::

        sage: list_plot3d(m, color='yellow', num_points=40,
        ....:             frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        pi = float(pi)
        import numpy as np
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', frame_aspect_ratio=[1, 1, 1/3], num_points=40))

    We can change the interpolation type::

        sage: import warnings
        sage: warnings.simplefilter('ignore', UserWarning)
        sage: list_plot3d(m, color='yellow', interpolation_type='clough',
        ....:             frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        import warnings
        warnings.simplefilter('ignore', UserWarning)
        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='clough', frame_aspect_ratio=[1, 1, 1/3]))

    We can make this look better by increasing the number of samples::

        sage: list_plot3d(m, color='yellow', interpolation_type='clough',
        ....:             frame_aspect_ratio=[1, 1, 1/3], num_points=40)
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='clough', frame_aspect_ratio=[1, 1, 1/3], num_points=40))

    Let us try a spline::

        sage: list_plot3d(m, color='yellow', interpolation_type='spline',
        ....:             frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='spline', frame_aspect_ratio=[1, 1, 1/3]))

    That spline does not capture the oscillation very well; let's try a
    higher degree spline::

        sage: list_plot3d(m, color='yellow', interpolation_type='spline', degree=5,
        ....:             frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='spline', degree=5, frame_aspect_ratio=[1, 1, 1/3]))

    We plot a list of lists::

        sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))

    .. PLOT::

        sphinx_plot(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))

    We plot a list of points.  As a first example we can extract the
    (x,y,z) coordinates from the above example and make a list plot
    out of it. By default we do linear interpolation::

        sage: l = []
        sage: for i in range(6):
        ....:     for j in range(6):
        ....:         l.append((float(i*pi/5), float(j*pi/5), m[i, j]))
        sage: list_plot3d(l, color='red')
        Graphics3d Object

    .. PLOT::

        l = []
        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        for i in range(6):
             for j in range(6):
                 l.append((float(i*pi/5), float(j*pi/5), m[i, j]))
        sphinx_plot(list_plot3d(l, color='red'))

    Note that the points do not have to be regularly sampled. For example::

        sage: l = []
        sage: for i in range(-5, 5):
        ....:     for j in range(-5, 5):
        ....:         l.append((normalvariate(0, 1),
        ....:                   normalvariate(0, 1),
        ....:                   normalvariate(0, 1)))
        sage: L = list_plot3d(l, interpolation_type='clough',
        ....:                 color='orange', num_points=100)
        sage: L
        Graphics3d Object

    .. PLOT::

        l = []
        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        for i in range(-5, 5):
            for j in range(-5, 5):
                l.append((normalvariate(0, 1), normalvariate(0, 1), normalvariate(0, 1)))
        L = list_plot3d(l, interpolation_type='clough', color='orange', num_points=100)
        sphinx_plot(L)


    Check that no NaNs are produced (see :issue:`13135`)::

        sage: any(math.isnan(c) for v in L.vertices() for c in v)
        False

    TESTS:

    We plot 0, 1, and 2 points::

        sage: list_plot3d([])
        Graphics3d Object

        sage: list_plot3d([(2, 3, 4)])
        Graphics3d Object

        sage: list_plot3d([(0, 0, 1), (2, 3, 4)])
        Graphics3d Object

    However, if two points are given with the same x,y coordinates but
    different z coordinates, an exception will be raised::

        sage: pts = [(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
        sage: show(list_plot3d(pts, interpolation_type='clough'))
        Traceback (most recent call last):
        ...
        ValueError: points with same x,y coordinates and different
        z coordinates were given. Interpolation cannot handle this.

    Additionally we need at least 3 points to do the interpolation::

        sage: mat = matrix(RDF, 1, 2, [3.2, 1.550])
        sage: show(list_plot3d(mat, interpolation_type='clough'))
        Traceback (most recent call last):
        ...
        ValueError: we need at least 3 points to perform the interpolation

    TESTS::

        sage: P = list_plot3d([(0, 0, 1), (2, 3, 4)], texture='tomato')
        doctest:warning...:
        DeprecationWarning: please use 'color' instead of 'texture'
        See https://github.com/sagemath/sage/issues/27084 for details.
    """
def list_plot3d_matrix(m, **kwds):
    """
    A 3-dimensional plot of a surface defined by a matrix ``M``
    defining points in 3-dimensional space.

    See :func:`list_plot3d` for full details.

    INPUT:

    - ``M`` -- a matrix

    OPTIONAL KEYWORDS:

    - ``**kwds`` -- all other arguments are passed to the surface function

    OUTPUT: a 3d plot

    EXAMPLES:

    We plot a matrix that illustrates summation modulo `n`::

        sage: n = 5
        sage: list_plot3d(matrix(RDF, n, [(i+j) % n         # indirect doctest
        ....:                             for i in [1..n] for j in [1..n]]))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(list_plot3d(matrix(RDF, 5, [(i+j)%5 for i in range(1,6) for j in range(1,6)])))

    The interpolation type for matrices is 'linear'; for other types
    use other :func:`list_plot3d` input types.

    We plot a matrix of values of `sin`::

        sage: from math import pi
        sage: m = matrix(RDF, 6, [sin(i^2 + j^2)
        ....:                     for i in [0,pi/5,..,pi] for j in [0,pi/5,..,pi]])
        sage: list_plot3d(m, color='yellow', frame_aspect_ratio=[1, 1, 1/3])  # indirect doctest
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', frame_aspect_ratio=[1, 1, 1/3]))

    ::
        sage: list_plot3d(m, color='yellow', interpolation_type='linear')  # indirect doctest
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='linear'))

    Here is a colored example, using a colormap and a coloring function
    which must take values in (0, 1)::

        sage: cm = colormaps.rainbow
        sage: n = 20
        sage: cf = lambda x, y: ((2*(x-y)/n)**2) % 1
        sage: list_plot3d(matrix(RDF, n, [cos(pi*(i+j)/n) for i in [1..n]
        ....:                             for j in [1..n]]), color=(cf,cm))
        Graphics3d Object

    .. PLOT::

        cm = colormaps.rainbow
        cf = lambda x, y: ((2*(x-y)/20)**2) % 1
        expl = list_plot3d(matrix(RDF,20,20,[cos(pi*(i+j)/20) for i in range(1,21) for j in range(1,21)]),color=(cf,cm))
        sphinx_plot(expl)
    """
def list_plot3d_array_of_arrays(v, interpolation_type, **kwds):
    """
    A 3-dimensional plot of a surface defined by a list of lists ``v``
    defining points in 3-dimensional space.

    This is done by making the list of lists into a matrix and passing
    back to :func:`list_plot3d`.  See :func:`list_plot3d` for full
    details.

    INPUT:

    - ``v`` -- list of lists, all the same length
    - ``interpolation_type`` -- (default: ``'linear'``)

    OPTIONAL KEYWORDS:

    - ``**kwds`` -- all other arguments are passed to the surface function

    OUTPUT: a 3d plot

    EXAMPLES:

    The resulting matrix does not have to be square::

        sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1]])) # indirect doctest

    .. PLOT::

        sphinx_plot(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1]]))

    The normal route is for the list of lists to be turned into a matrix
    and use :func:`list_plot3d_matrix`::

        sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))

    .. PLOT::

        sphinx_plot(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))

    With certain extra keywords (see :func:`list_plot3d_matrix`), this function
    will end up using :func:`list_plot3d_tuples`::

        sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]],
        ....:                  interpolation_type='spline'))

    .. PLOT::

        sphinx_plot(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]], interpolation_type='spline'))
    """
def list_plot3d_tuples(v, interpolation_type, **kwds):
    """
    A 3-dimensional plot of a surface defined by the list `v`
    of points in 3-dimensional space.

    INPUT:

    - ``v`` -- something that defines a set of points in 3
      space, for example:

      - a matrix

        This will be if using an ``interpolation_type`` other than
        ``'linear'``, or if using ``num_points`` with ``'linear'``;
        otherwise see :func:`list_plot3d_matrix`.

      - a list of 3-tuples

      - a list of lists (all of the same length, under same conditions
        as a matrix)

    OPTIONAL KEYWORDS:

    - ``interpolation_type`` -- one of ``'linear'``, ``'clough'``
      (CloughTocher2D), ``'spline'``

      ``'linear'`` will perform linear interpolation

      The option 'clough' will interpolate by using a piecewise cubic
      interpolating Bezier polynomial on each triangle, using a
      Clough-Tocher scheme.  The interpolant is guaranteed to be
      continuously differentiable.

      The option ``'spline'`` interpolates using a bivariate B-spline.

      When ``v`` is a matrix the default is to use linear interpolation, when
      ``v`` is a list of points the default is ``'clough'``.

    - ``degree`` -- integer between 1 and 5, controls the degree of spline
      used for spline interpolation. For data that is highly oscillatory
      use higher values

    - ``point_list`` -- if ``point_list=True`` is passed, then if the array
      is a list of lists of length three, it will be treated as an
      array of points rather than a `3\\times n` array.

    - ``num_points`` -- number of points to sample interpolating
      function in each direction.  By default for an `n\\times n`
      array this is `n`.

    - ``**kwds`` -- all other arguments are passed to the
      surface function

    OUTPUT: a 3d plot

    EXAMPLES:

    All of these use this function; see :func:`list_plot3d` for other
    list plots::

        sage: from math import pi
        sage: m = matrix(RDF, 6, [sin(i^2 + j^2)
        ....:                     for i in [0,pi/5,..,pi] for j in [0,pi/5,..,pi]])
        sage: list_plot3d(m, color='yellow', interpolation_type='linear',  # indirect doctest
        ....:             num_points=5)
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='linear', num_points=5))

    ::

        sage: list_plot3d(m, color='yellow', interpolation_type='spline',
        ....:             frame_aspect_ratio=[1, 1, 1/3])
        Graphics3d Object

    .. PLOT::

        import numpy as np
        pi = float(pi)
        m = matrix(RDF, 6, [sin(i**2 + j**2) for i in np.linspace(0,pi,6) for j in np.linspace(0,pi,6)])
        sphinx_plot(list_plot3d(m, color='yellow', interpolation_type='spline', frame_aspect_ratio=[1, 1, 1/3]))

    ::

        sage: show(list_plot3d([[1, 1, 1], [1, 2, 1], [0, 1, 3], [1, 0, 4]],
        ....:                  point_list=True))

    .. PLOT::

        sphinx_plot(list_plot3d([[1, 1, 1], [1, 2, 1], [0, 1, 3], [1, 0, 4]],
                                point_list=True))

    ::

        sage: list_plot3d([(1, 2, 3), (0, 1, 3), (2, 1, 4), (1, 0, -2)],  # long time
        ....:             color='yellow', num_points=50)
        Graphics3d Object

    .. PLOT::

        sphinx_plot(list_plot3d([(1, 2, 3), (0, 1, 3), (2, 1, 4), (1, 0, -2)], color='yellow', num_points=50))
    """
