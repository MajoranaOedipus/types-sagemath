from sage.arith.srange import srange as srange
from sage.modules.free_module_element import vector as vector
from sage.plot.misc import setup_for_eval_on_grid as setup_for_eval_on_grid
from sage.plot.plot import plot as plot

def plot_vector_field3d(functions, xrange, yrange, zrange, plot_points: int = 5, colors: str = 'jet', center_arrows: bool = False, **kwds):
    """
    Plot a 3d vector field.

    INPUT:

    - ``functions`` -- list of three functions, representing the x-,
      y-, and z-coordinates of a vector

    - ``xrange``, ``yrange``, and ``zrange`` -- three tuples of the
      form (var, start, stop), giving the variables and ranges for each axis

    - ``plot_points`` -- (default: 5) either a number or list of three
      numbers, specifying how many points to plot for each axis

    - ``colors`` -- (default: ``'jet'``) a color, list of colors (which are
      interpolated between), or matplotlib colormap name, giving the coloring
      of the arrows.  If a list of colors or a colormap is given,
      coloring is done as a function of length of the vector

    - ``center_arrows`` -- (default: ``False``) if ``True``, draw the arrows
      centered on the points; otherwise, draw the arrows with the tail
      at the point

    - any other keywords are passed on to the :func:`plot` command for each arrow

    EXAMPLES:

    A 3d vector field::

      sage: x,y,z = var('x y z')
      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi))
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi)))

    same example with only a list of colors::

      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi),
      ....:                     colors=['red','green','blue'])
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),colors=['red','green','blue']))

    same example with only one color::

      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi), colors='red')
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),colors='red'))

    same example with the same plot points for the three axes::

      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi), plot_points=4)
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),plot_points=4))

    same example with different number of plot points for each axis::

      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi), plot_points=[3,5,7])
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),plot_points=[3,5,7]))

    same example with the arrows centered on the points::

      sage: plot_vector_field3d((x*cos(z), -y*cos(z), sin(z)),
      ....:                     (x,0,pi), (y,0,pi), (z,0,pi), center_arrows=True)
      Graphics3d Object

    .. PLOT::

      x,y,z=var('x y z')
      sphinx_plot(plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),center_arrows=True))


    TESTS:

    This tests that :issue:`2100` is fixed in a way compatible with this command::

        sage: plot_vector_field3d((x*cos(z),-y*cos(z),sin(z)), (x,0,pi), (y,0,pi), (z,0,pi),center_arrows=True,aspect_ratio=(1,2,1))
        Graphics3d Object
    """
