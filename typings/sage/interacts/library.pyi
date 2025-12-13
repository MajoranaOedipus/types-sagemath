from _typeshed import Incomplete
from sage.arith.misc import factor as factor
from sage.arith.srange import srange as srange
from sage.calculus.all import symbolic_expression as symbolic_expression
from sage.calculus.functional import derivative as derivative
from sage.ext.fast_callable import fast_callable as fast_callable
from sage.functions.log import exp as exp
from sage.functions.trig import acos as acos, cos as cos, sin as sin, tan as tan
from sage.misc.decorators import sage_wraps as sage_wraps
from sage.misc.functional import N as N, sqrt as sqrt
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.misc.table import table as table
from sage.repl.ipython_kernel.all_jupyter import checkbox as checkbox, input_box as input_box, input_grid as input_grid, interact as interact, range_slider as range_slider, selector as selector, slider as slider, text_control as text_control
from sage.repl.rich_output.pretty_print import pretty_print as pretty_print, show as show
from sage.repl.user_globals import get_global as get_global
from sage.rings.complex_double import CDF as CDF
from sage.rings.integer import Integer as Integer
from sage.symbolic.constants import pi as pi
from sage.symbolic.relation import solve as solve
from sage.symbolic.ring import SR as SR
from typing import Any, Callable

x: Incomplete

def library_interact(decorator_target: Callable[..., Any] = None, **widgets: Callable[..., Any]):
    """
    This is a decorator for using interacts in the Sage library.

    This is essentially a wrapper around the ``interact`` function.

    INPUT:

    - ``**widgets`` -- keyword arguments that are passed to the
      ``interact`` function to create the widgets. Each value must
      be a callable that returns a widget.

    EXAMPLES::

        sage: from sage.interacts.library import library_interact
        sage: @library_interact(n=lambda: slider(-5, 15, None, 5))
        ....: def f(n):
        ....:     print(n)
        sage: f()  # an interact appears if using the notebook, else code
        ...Interactive function <function f at ...> with 1 widget
        n: TransformIntSlider(value=5, description='n', max=15, min=-5)

    TESTS:

    Backwards compatibility::

        sage: from sage.interacts.library import library_interact
        sage: @library_interact
        ....: def f(n=slider(-5, 15, None, 5)):
        ....:     print(n)
        doctest:warning
        ...
        DeprecationWarning: Use decorator factory @library_interact(widgets) instead of @library_interact without any arguments.
        See https://github.com/sagemath/sage/issues/33382 for details.
        sage: f()  # an interact appears if using the notebook, else code
        ...Interactive function <function f at ...> with 1 widget
        n: TransformIntSlider(value=5, description='n', max=15, min=-5)

    .. NOTE::

        We use a callable to construct the widget so that the widget is only
        initialized when the function is called and not upon loading the module.
    """
def html(obj) -> None:
    '''
    Shorthand to pretty print HTML.

    EXAMPLES::

        sage: from sage.interacts.library import html
        sage: html("<h1>Hello world</h1>")
        <h1>Hello world</h1>
    '''
def demo(n: int, m: int):
    """
    This is a demo interact that sums two numbers.

    INPUT:

    - ``n`` -- integer
    - ``m`` -- integer

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.demo()
        ...Interactive function <function demo at ...> with 2 widgets
          n: SelectionSlider(description='n', options=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), value=0)
          m: SelectionSlider(description='m', options=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), value=0)
    """
def taylor_polynomial(title, f, order: int):
    """
    Illustrate the Taylor polynomial approximation
    of various orders around `x=0`.

    INPUT:

    - ``f`` -- function expression
    - ``order`` -- integer

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.taylor_polynomial()
        ...Interactive function <function taylor_polynomial at ...> with 3 widgets
          title: HTMLText(value='<h2>Taylor polynomial</h2>')
          f: EvalText(value='e^(-x)*sin(x)', description='$f(x)=$', layout=Layout(max_width='81em'))
          order: SelectionSlider(description='order', options=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), value=1)
    """
def definite_integral(title, f, g, interval, x_range, selection) -> None:
    """
    This is a demo interact for plotting the definite integral of a function
    based on work by Lauri Ruotsalainen, 2010.

    INPUT:

    - ``function`` -- input box, function in x
    - ``interval`` -- interval for the definite integral
    - ``x_range`` -- range slider for plotting range
    - ``selection`` -- selector on how to visualize the integrals

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.definite_integral()
        ...Interactive function <function definite_integral at ...> with 6 widgets
          title: HTMLText(value='<h2>Definite integral</h2>')
          f: EvalText(value='3*x', description='$f(x)=$', layout=Layout(max_width='81em'))
          g: EvalText(value='x^2', description='$g(x)=$', layout=Layout(max_width='81em'))
          interval: IntRangeSlider(value=(0, 3), description='Interval', max=10, min=-10)
          x_range: IntRangeSlider(value=(0, 3), description='plot range (x)', max=10, min=-10)
          selection: Dropdown(description='Select', index=2,
                              options=('f', 'g', 'f and g', 'f - g'), value='f and g')
    """
def function_derivative(title, function, x_range, y_range) -> None:
    """
    This is a demo interact for plotting derivatives of a function based on work by
    Lauri Ruotsalainen, 2010.

    INPUT:

        - ``function`` -- input box, function in x
        - ``x_range`` -- range slider for plotting range
        - ``y_range`` -- range slider for plotting range

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.function_derivative()
        ...Interactive function <function function_derivative at ...> with 4 widgets
          title: HTMLText(value='<h2>Derivative grapher</h2>')
          function: EvalText(value='x^5-3*x^3+1', description='Function:', layout=Layout(max_width='81em'))
          x_range: FloatRangeSlider(value=(-2.0, 2.0), description='Range (x)', max=15.0, min=-15.0)
          y_range: FloatRangeSlider(value=(-8.0, 6.0), description='Range (y)', max=15.0, min=-15.0)
    """
def difference_quotient(title, f, interval, a, x0) -> None:
    """
    This is a demo interact for difference quotient based on work by
    Lauri Ruotsalainen, 2010.

    INPUT:

    - ``f`` -- input box, function in `x`
    - ``interval`` -- range slider for plotting
    - ``a`` -- slider for `a`
    - ``x0`` -- slider for starting point `x_0`

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.difference_quotient()
        ...Interactive function <function difference_quotient at ...> with 5 widgets
          title: HTMLText(value='<h2>Difference quotient</h2>')
          f: EvalText(value='sin(x)', description='f(x)', layout=Layout(max_width='81em'))
          interval: FloatRangeSlider(value=(0.0, 10.0), description='Range', max=10.0)
          a: IntSlider(value=5, description='$a$', max=10)
          x0: IntSlider(value=2, description='$x_0$ (start point)', max=10)
    """
def quadratic_equation(A, B, C) -> None:
    """
    This is a demo interact for solving quadratic equations based on work by
    Lauri Ruotsalainen, 2010.

    INPUT:

    - ``A`` -- integer slider
    - ``B`` -- integer slider
    - ``C`` -- integer slider

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.quadratic_equation()
        ...Interactive function <function quadratic_equation at ...> with 3 widgets
          A: IntSlider(value=1, description='A', max=7, min=-7)
          B: IntSlider(value=1, description='B', max=7, min=-7)
          C: IntSlider(value=-2, description='C', max=7, min=-7)
    """
def trigonometric_properties_triangle(a0, a1, a2):
    """
    This is an interact for demonstrating trigonometric properties
    in a triangle based on work by Lauri Ruotsalainen, 2010.

    INPUT:

    - ``a0`` -- angle
    - ``a1`` -- angle
    - ``a2`` -- angle

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.geometry.trigonometric_properties_triangle()
        ...Interactive function <function trigonometric_properties_triangle at ...> with 3 widgets
          a0: IntSlider(value=30, description='A', max=360)
          a1: IntSlider(value=180, description='B', max=360)
          a2: IntSlider(value=300, description='C', max=360)
    """
def unit_circle(function, x) -> None:
    """
    This is an interact for Sin, Cos and Tan in the Unit Circle
    based on work by Lauri Ruotsalainen, 2010.

    INPUT:

    - ``function`` -- select Sin, Cos or Tan
    - ``x`` -- slider to select angle in unit circle

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.geometry.unit_circle()
        ...Interactive function <function unit_circle at ...> with 2 widgets
          function: Dropdown(description='function', options=(('sin(x)', 0), ('cos(x)', 1), ('tan(x)', 2)), value=0)
          x: TransformFloatSlider(value=0.0, description='x', max=6.283185307179586, step=0.015707963267948967)
    """
def special_points(title, a0, a1, a2, show_median, show_pb, show_alt, show_ab, show_incircle, show_euler):
    '''
    This interact demo shows special points in a triangle
    based on work by Lauri Ruotsalainen, 2010.

    INPUT:

    - ``a0`` -- angle
    - ``a1`` -- angle
    - ``a2`` -- angle
    - ``show_median`` -- checkbox
    - ``show_pb`` -- checkbox to show perpendicular bisectors
    - ``show_alt`` -- checkbox to show altitudes
    - ``show_ab`` -- checkbox to show angle bisectors
    - ``show_incircle`` -- checkbox to show incircle
    - ``show_euler`` -- checkbox to show euler\'s line

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.geometry.special_points()
        ...Interactive function <function special_points at ...> with 10 widgets
          title: HTMLText(value=\'<h2>Special points in triangle</h2>\')
          a0: IntSlider(value=30, description=\'A\', max=360)
          a1: IntSlider(value=180, description=\'B\', max=360)
          a2: IntSlider(value=300, description=\'C\', max=360)
          show_median: Checkbox(value=False, description=\'Medians\')
          show_pb: Checkbox(value=False, description=\'Perpendicular Bisectors\')
          show_alt: Checkbox(value=False, description=\'Altitudes\')
          show_ab: Checkbox(value=False, description=\'Angle Bisectors\')
          show_incircle: Checkbox(value=False, description=\'Incircle\')
          show_euler: Checkbox(value=False, description="Euler\'s Line")
    '''
def coin(n, interval) -> None:
    """
    This interact demo simulates repeated tosses of a coin,
    based on work by Lauri Ruotsalainen, 2010.

    The points give the cumulative percentage of tosses which
    are heads in a given run of the simulation, so that the
    point `(x,y)` gives the percentage of the first `x` tosses
    that were heads; this proportion should approach .5, of
    course, if we are simulating a fair coin.

    INPUT:

    - ``n`` -- number of tosses
    - ``interval`` -- plot range along vertical axis

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.statistics.coin()
        ...Interactive function <function coin at ...> with 2 widgets
          n: IntSlider(value=1000, description='Number of Tosses', max=10000, min=2, step=100)
          interval: FloatRangeSlider(value=(0.45, 0.55), description='Plotting range (y)', max=1.0)
    """
def bisection_method(title, f, interval, d, maxn):
    """
    Interact explaining the bisection method, based on similar interact
    explaining secant method and Wiliam Stein's example from wiki.

    INPUT:

    - ``f`` -- function
    - ``interval`` -- range slider for the search interval
    - ``d`` -- slider for the precision (`10^{-d}`)
    - ``maxn`` -- max number of iterations

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.secant_method()
        ...Interactive function <function secant_method at ...> with 5 widgets
          title: HTMLText(value='<h2>Secant method for numerical root finding</h2>')
          f: EvalText(value='x^2-2', description='f(x)', layout=Layout(max_width='81em'))
          interval: IntRangeSlider(value=(0, 4), description='range', max=5, min=-5)
          d: IntSlider(value=3, description='10^-d precision', max=16, min=1)
          maxn: IntSlider(value=10, description='max iterations', max=15)
    """
def secant_method(title, f, interval, d, maxn):
    """
    Interact explaining the secant method, based on work by
    Lauri Ruotsalainen, 2010.
    Originally this is based on work by William Stein.

    INPUT:

    - ``f`` -- function
    - ``interval`` -- range slider for the search interval
    - ``d`` -- slider for the precision (10^-d)
    - ``maxn`` -- max number of iterations

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.secant_method()
        ...Interactive function <function secant_method at ...> with 5 widgets
          title: HTMLText(value='<h2>Secant method for numerical root finding</h2>')
          f: EvalText(value='x^2-2', description='f(x)', layout=Layout(max_width='81em'))
          interval: IntRangeSlider(value=(0, 4), description='range', max=5, min=-5)
          d: IntSlider(value=3, description='10^-d precision', max=16, min=1)
          maxn: IntSlider(value=10, description='max iterations', max=15)
    """
def newton_method(title, f, c, d, maxn, interval, list_steps):
    """
    Interact explaining the Newton method, based on work by
    Lauri Ruotsalainen, 2010.
    Originally this is based on work by William Stein.

    INPUT:

    - ``f`` -- function
    - ``c`` -- starting position (`x`)
    - ``d`` -- slider for the precision (`10^{-d}`)
    - ``maxn`` -- max number of iterations
    - ``interval`` -- range slider for the search interval
    - ``list_steps`` -- checkbox, if ``True`` shows the steps numerically

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.newton_method()
        ...Interactive function <function newton_method at ...> with 7 widgets
          title: HTMLText(value='<h2>Newton method</h2>')
          f: EvalText(value='x^2 - 2', description='f', layout=Layout(max_width='81em'))
          c: IntSlider(value=6, description='Start ($x$)', max=10, min=-10)
          d: IntSlider(value=3, description='$10^{-d}$ precision', max=16, min=1)
          maxn: IntSlider(value=10, description='max iterations', max=15)
          interval: IntRangeSlider(value=(0, 6), description='Interval', max=10, min=-10)
          list_steps: Checkbox(value=False, description='List steps')
    """
def trapezoid_integration(title, f, n, interval_input, interval_s, interval_g, output_form) -> None:
    '''
    Interact explaining the trapezoid method for definite integrals.

    Based on work by
    Lauri Ruotsalainen, 2010 (based on the application "Numerical integrals with various rules"
    by Marshall Hampton and Nick Alexander)

    INPUT:

    - ``f`` -- function of variable x to integrate
    - ``n`` -- number of divisions
    - ``interval_input`` -- switches the input for interval between slider and keyboard
    - ``interval_s`` -- slider for interval to integrate
    - ``interval_g`` -- input grid for interval to integrate
    - ``output_form`` -- the computation is formatted in a traditional form, in a table or missing

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.trapezoid_integration()
        ...Interactive function <function trapezoid_integration at ...> with 7 widgets
          title: HTMLText(value=\'<h2>Trapezoid integration</h2>\')
          f: EvalText(value=\'x^2-5*x + 10\', description=\'$f(x)=$\', layout=Layout(max_width=\'81em\'))
          n: IntSlider(value=5, description=\'# divisions\', min=1)
          interval_input: ToggleButtons(description=\'Integration interval\', options=(\'from slider\', \'from keyboard\'), value=\'from slider\')
          interval_s: IntRangeSlider(value=(0, 8), description=\'slider: \', max=10, min=-10)
          interval_g: Grid(value=[[0, 8]], children=(Label(value=\'keyboard: \'), VBox(children=(EvalText(value=\'0\', layout=Layout(max_width=\'5em\')),)), VBox(children=(EvalText(value=\'8\', layout=Layout(max_width=\'5em\')),))))
          output_form: ToggleButtons(description=\'Computations form\', options=(\'traditional\', \'table\', \'none\'), value=\'traditional\')
    '''
def simpson_integration(title, f, n, interval_input, interval_s, interval_g, output_form):
    '''
    Interact explaining the simpson method for definite integrals.

    Based on work by
    Lauri Ruotsalainen, 2010 (based on the application "Numerical integrals with various rules"
    by Marshall Hampton and Nick Alexander)

    INPUT:

    - ``f`` -- function of variable x to integrate
    - ``n`` -- number of divisions (mult. of 2)
    - ``interval_input`` -- switches the input for interval between slider and keyboard
    - ``interval_s`` -- slider for interval to integrate
    - ``interval_g`` -- input grid for interval to integrate
    - ``output_form`` -- the computation is formatted in a traditional form, in a table or missing

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.simpson_integration()
        ...Interactive function <function simpson_integration at ...> with 7 widgets
          title: HTMLText(value=\'<h2>Simpson integration</h2>\')
          f: EvalText(value=\'x*sin(x)+x+1\', description=\'$f(x)=$\', layout=Layout(max_width=\'81em\'))
          n: IntSlider(value=6, description=\'# divisions\', min=2, step=2)
          interval_input: ToggleButtons(description=\'Integration interval\', options=(\'from slider\', \'from keyboard\'), value=\'from slider\')
          interval_s: IntRangeSlider(value=(0, 10), description=\'slider: \', max=10, min=-10)
          interval_g: Grid(value=[[0, 10]], children=(Label(value=\'keyboard: \'), VBox(children=(EvalText(value=\'0\', layout=Layout(max_width=\'5em\')),)), VBox(children=(EvalText(value=\'10\', layout=Layout(max_width=\'5em\')),))))
          output_form: ToggleButtons(description=\'Computations form\', options=(\'traditional\', \'table\', \'none\'), value=\'traditional\')
    '''
def riemann_sum(title, f, n, hr1, interval_input, interval_s, interval_g, hr2, list_table, auto_update: bool = False) -> None:
    """
    Interact explaining the definition of Riemann integral.

    INPUT:

    - ``f`` -- function of variable x to integrate
    - ``n`` -- number of divisions
      - ``interval_input`` -- switches the input for interval between slider and keyboard
      - ``interval_s`` -- slider for interval to integrate
      - ``interval_g`` -- input grid for interval to integrate
    - ``list_table`` -- print table with values of the function

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.riemann_sum()
        Manual interactive function <function riemann_sum at ...> with 9 widgets
          title: HTMLText(value='<h2>Riemann integral with random sampling</h2>')
          f: EvalText(value='x^2+1',... description='$f(x)=$', layout=Layout(max_width='41em'))
          n: IntSlider(value=5, description='# divisions', max=30, min=1)
          hr1: HTMLText(value='<hr>')
          interval_input: ToggleButtons(description='Integration interval', options=('from slider', 'from keyboard'), value='from slider')
          interval_s: IntRangeSlider(value=(0, 2), description='slider: ', max=10, min=-5)
          interval_g: Grid(value=[[0, 2]], children=(Label(value='keyboard: '), VBox(children=(EvalText(value='0', layout=Layout(max_width='5em')),)), VBox(children=(EvalText(value='2', layout=Layout(max_width='5em')),))))
          hr2: HTMLText(value='<hr>')
          list_table: Checkbox(value=False, description='List table')

    AUTHORS:

    - Robert Marik (2010-08)
    """
def function_tool(f, g, xrange, yrange, a, action, do_plot) -> None:
    """
    `Function Plotting Tool <http://wiki.sagemath.org/interact/calculus#Functiontool>`_
    (by William Stein (?))

    INPUT:

    - ``f`` -- function f(x)
    - ``g`` -- function g(x)
    - ``xrange`` -- range for plotting (x)
    - ``yrange`` -- range for plotting ('auto' is default, otherwise a tuple)
    - ``a`` -- factor ``a``
    - ``action`` -- select given operation on or combination of functions
    - ``do_plot`` -- if ``True``, a plot is drawn

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.calculus.function_tool()  # long time
        ...Interactive function <function function_tool at ...> with 7 widgets
          f: EvalText(value='sin(x)', description='f')
          g: EvalText(value='cos(x)', description='g')
          xrange: IntRangeSlider(value=(0, 1), description='x-range', max=3, min=-3)
          yrange: Text(value='auto', description='yrange')
          a: IntSlider(value=1, description='a', max=3, min=-1)
          action: ToggleButtons(description='h = ', options=('f', 'df/dx', 'int f', 'num f', 'den f', '1/f', 'finv', 'f+a', 'f-a', 'f*a', 'f/a', 'f^a', 'f(x+a)', 'f(x*a)', 'f+g', 'f-g', 'f*g', 'f/g', 'f(g)'), value='f')
          do_plot: Checkbox(value=True, description='Draw Plots')
    """
def julia(expo, c_real, c_imag, iterations, zoom_x, zoom_y, plot_points, dpi):
    """
    Julia Fractal, based on
    `Julia by Harald Schilly <http://wiki.sagemath.org/interact/fractal#Julia>`_.

    INPUT:

    - ``exponent`` -- exponent ``e`` in `z^e+c`
    - ``c_real`` -- real part of the constant ``c``
    - ``c_imag`` -- imaginary part of the constant ``c``
    - ``iterations`` -- number of iterations
    - ``zoom_x`` -- range slider for zoom in x direction
    - ``zoom_y`` -- range slider for zoom in y direction
    - ``plot_points`` -- number of points to plot
    - ``dpi`` -- dots-per-inch parameter for the plot

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.fractals.julia()  # long time
        ...Interactive function <function julia at ...> with 8 widgets
          expo: FloatSlider(value=2.0, description='expo', max=10.0, min=-10.0)
          c_real: FloatSlider(value=0.5, description='real part const.', max=2.0, min=-2.0, step=0.01)
          c_imag: FloatSlider(value=0.5, description='imag part const.', max=2.0, min=-2.0, step=0.01)
          iterations: IntSlider(value=20, description='# iterations', min=1)
          zoom_x: FloatRangeSlider(value=(-1.5, 1.5), description='Zoom X', max=2.0, min=-2.0, step=0.01)
          zoom_y: FloatRangeSlider(value=(-1.5, 1.5), description='Zoom Y', max=2.0, min=-2.0, step=0.01)
          plot_points: IntSlider(value=150, description='plot points', max=400, min=20, step=20)
          dpi: IntSlider(value=80, description='dpi', max=200, min=20, step=10)
    """
def mandelbrot(expo, iterations, zoom_x, zoom_y, plot_points, dpi):
    """
    Mandelbrot Fractal, based on
    `Mandelbrot by Harald Schilly <http://wiki.sagemath.org/interact/fractal#Mandelbrot>`_.

    INPUT:

    - ``exponent`` -- exponent ``e`` in `z^e+c`
    - ``iterations`` -- number of iterations
    - ``zoom_x`` -- range slider for zoom in x direction
    - ``zoom_y`` -- range slider for zoom in y direction
    - ``plot_points`` -- number of points to plot
    - ``dpi`` -- dots-per-inch parameter for the plot

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.fractals.mandelbrot()  # long time
        ...Interactive function <function mandelbrot at ...> with 6 widgets
          expo: FloatSlider(value=2.0, description='expo', max=10.0, min=-10.0)
          iterations: IntSlider(value=20, description='# iterations', min=1)
          zoom_x: FloatRangeSlider(value=(-2.0, 1.0), description='Zoom X', max=2.0, min=-2.0, step=0.01)
          zoom_y: FloatRangeSlider(value=(-1.5, 1.5), description='Zoom Y', max=2.0, min=-2.0, step=0.01)
          plot_points: IntSlider(value=150, description='plot points', max=400, min=20, step=20)
          dpi: IntSlider(value=80, description='dpi', max=200, min=20, step=10)
    """
def cellular_automaton(N, rule_number, size) -> None:
    """
    Yields a matrix showing the evolution of a
    `Wolfram's cellular automaton <http://mathworld.wolfram.com/CellularAutomaton.html>`_.

    `Based on work by Pablo Angulo <http://wiki.sagemath.org/interact/misc#CellularAutomata>`_.

    INPUT:

    - ``N`` -- iterations
    - ``rule_number`` -- rule number (0 to 255)
    - ``size`` -- size of the shown picture

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: interacts.fractals.cellular_automaton()  # long time
        ...Interactive function <function cellular_automaton at ...> with 3 widgets
          N: IntSlider(value=100, description='Number of iterations', max=500, min=1)
          rule_number: IntSlider(value=110, description='Rule number', max=255)
          size: IntSlider(value=6, description='size of graphic', max=11, min=1)
    """
def polar_prime_spiral(interval, show_factors, highlight_primes, show_curves, n, dpi):
    """
    Polar Prime Spiral interact, based on work by David Runde.

    For more information about the factors in the spiral,
    `visit John Williamson's website <http://www.dcs.gla.ac.uk/~jhw/spirals/index.html>`_.

    INPUT:

    - ``interval`` -- range slider to specify start and end
    - ``show_factors`` -- if ``True``, show factors
    - ``highlight_primes`` -- if ``True``, prime numbers are highlighted
    - ``show_curves`` -- if ``True``, curves are plotted
    - ``n`` -- number `n`
    - ``dpi`` -- dots per inch resolution for plotting

    EXAMPLES:

    Invoked in the notebook, the following command will produce
    the fully formatted interactive mathlet.  In the command line,
    it will simply return the underlying HTML and Sage code which
    creates the mathlet::

        sage: sage.interacts.algebra.polar_prime_spiral()  # long time
        ...Interactive function <function polar_prime_spiral at ...> with 6 widgets
          interval: IntRangeSlider(value=(1, 1000), description='range', max=4000, min=1, step=10)
          show_factors: Checkbox(value=True, description='show_factors')
          highlight_primes: Checkbox(value=True, description='highlight_primes')
          show_curves: Checkbox(value=True, description='show_curves')
          n: IntSlider(value=89, description='number $n$', max=200, min=1)
          dpi: IntSlider(value=100, description='dpi', max=300, min=10, step=10)
    """
