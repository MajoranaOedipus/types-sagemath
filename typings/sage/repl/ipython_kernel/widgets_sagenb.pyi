from .widgets import EvalText as EvalText, EvalTextarea as EvalTextarea, Grid as Grid, SageColorPicker as SageColorPicker, TransformFloatRangeSlider as TransformFloatRangeSlider, TransformFloatSlider as TransformFloatSlider, TransformIntRangeSlider as TransformIntRangeSlider, TransformIntSlider as TransformIntSlider, TransformText as TransformText, TransformTextarea as TransformTextarea
from _typeshed import Incomplete
from sage.arith.srange import srange as srange
from sage.structure.all import parent as parent

Color: Incomplete

def input_box(default=None, label=None, type=None, width: int = 80, height: int = 1):
    '''
    A textbox widget.

    INPUT:

    - ``default`` -- initial value

    - ``label`` -- (optional)

    - ``type`` -- function of one variable or ``None``. if ``type`` is
      ``str``, the value of this widget for interactive functions is
      just the text as ``str``. Otherwise, the text is evaluated using
      :func:`sage_eval`, ``type`` is called on it and the result is used
      as value. Except if ``type`` is ``None``, then the evaluated text
      is used as value.

    - ``width`` -- width of the box

    - ``height`` -- if ``height > 1``, create a textarea instead of a
      single-line textbox

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import input_box

    The most basic usage is when ``type=str``::

        sage: w = input_box("4+5", type=str, label="enter a string")
        sage: w
        TransformText(value=\'4+5\', description=\'enter a string\', layout=Layout(max_width=\'81em\'))
        sage: w.get_interact_value()
        \'4+5\'

    Without ``type``, the text is evaluated::

        sage: w = input_box("4+5")
        sage: w
        EvalText(value=\'4+5\', layout=Layout(max_width=\'81em\'))
        sage: w.get_interact_value()
        9

    With a different ``type``, the text is evaluated and ``type`` is
    called on it::

        sage: w = input_box("4+5", type=float)
        sage: w
        EvalText(value=\'4+5\', layout=Layout(max_width=\'81em\'))
        sage: w.get_interact_value()
        9.0

    Despite the keyword name, ``type`` does not need to be a type::

        sage: w = input_box("4+5", type=sqrt)
        sage: w
        EvalText(value=\'4+5\', layout=Layout(max_width=\'81em\'))
        sage: w.get_interact_value()
        3

    When ``height > 1``, a textarea is returned::

        sage: w = input_box("4+5", width=100, height=1)
        sage: w
        EvalText(value=\'4+5\', layout=Layout(max_width=\'101em\'))
        sage: w = input_box("4+5", width=100, height=5)
        sage: w
        EvalTextarea(value=\'4+5\', layout=Layout(max_width=\'101em\'))

    TESTS::

        sage: w = input_box(type=Color)
        Traceback (most recent call last):
        ...
        NotImplementedError: type=Color is not supported
    '''
def slider(vmin, vmax=None, step_size=None, default=None, label=None, display_value: bool = True, _range: bool = False):
    '''
    A slider widget.

    INPUT:

    For a numeric slider (select a value from a range):

    - ``vmin``, ``vmax`` -- minimum and maximum value

    - ``step_size`` -- the step size

    For a selection slider (select a value from a list of values):

    - ``vmin`` -- list of possible values for the slider

    For all sliders:

    - ``default`` -- initial value

    - ``label`` -- (optional)

    - ``display_value`` -- boolean; if ``True``, display the current value

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import slider
        sage: slider(5, label="slide me")
        TransformIntSlider(value=5, description=\'slide me\', min=5)
        sage: slider(5, 20)
        TransformIntSlider(value=5, max=20, min=5)
        sage: slider(5, 20, 0.5)
        TransformFloatSlider(value=5.0, max=20.0, min=5.0, step=0.5)
        sage: slider(5, 20, default=12)
        TransformIntSlider(value=12, max=20, min=5)

    The parent of the inputs determines the parent of the value::

        sage: w = slider(5); w
        TransformIntSlider(value=5, min=5)
        sage: parent(w.get_interact_value())
        Integer Ring
        sage: w = slider(int(5)); w
        IntSlider(value=5, min=5)
        sage: parent(w.get_interact_value())
        <... \'int\'>
        sage: w = slider(5, 20, step_size=RDF("0.1")); w
        TransformFloatSlider(value=5.0, max=20.0, min=5.0)
        sage: parent(w.get_interact_value())
        Real Double Field
        sage: w = slider(5, 20, step_size=10/3); w
        SelectionSlider(index=2, options=(5, 25/3, 35/3, 15, 55/3), value=35/3)
        sage: parent(w.get_interact_value())
        Rational Field

    Symbolic input is evaluated numerically::

        sage: w = slider(e, pi); w
        TransformFloatSlider(value=2.718281828459045, max=3.141592653589793, min=2.718281828459045)
        sage: parent(w.get_interact_value())
        Real Field with 53 bits of precision

    For a selection slider, the default is adjusted to one of the
    possible values::

        sage: slider(range(10), default=17/10)
        SelectionSlider(index=2, options=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), value=2)

    TESTS::

        sage: slider(range(5), range(5))
        Traceback (most recent call last):
        ...
        TypeError: unexpected argument \'vmax\' for a selection slider
        sage: slider(range(5), step_size=2)
        Traceback (most recent call last):
        ...
        TypeError: unexpected argument \'step_size\' for a selection slider
        sage: slider(5).readout
        True
        sage: slider(5, display_value=False).readout
        False

    Symbolic subrings work like ``SR``::

        sage: SCR = SR.subring(no_variables=True)
        sage: w = slider(SCR(e), SCR(pi)); w
        TransformFloatSlider(value=2.718281828459045, max=3.141592653589793, min=2.718281828459045)
        sage: parent(w.get_interact_value())
        Real Field with 53 bits of precision
    '''
def range_slider(*args, **kwds):
    '''
    A slider widget to select a range of values.

    INPUT:

    - ``vmin``, ``vmax`` -- minimum and maximum value

    - ``step_size`` -- the step size

    - ``default`` -- initial value, given as a 2-tuple

    - ``label`` -- (optional)

    - ``display_value`` -- boolean; if ``True``, display the current value

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import range_slider
        sage: range_slider(5, label="slide me")
        TransformIntRangeSlider(value=(28, 76), description=\'slide me\', min=5)
        sage: range_slider(5, 20)
        TransformIntRangeSlider(value=(8, 16), max=20, min=5)
        sage: range_slider(5, 20, 0.5)
        TransformFloatRangeSlider(value=(8.75, 16.25), max=20.0, min=5.0, step=0.5)
        sage: range_slider(5, 20, default=(12,15))
        TransformIntRangeSlider(value=(12, 15), max=20, min=5)

    The parent of the inputs determines the parent of the value::

        sage: w = range_slider(5); w
        TransformIntRangeSlider(value=(28, 76), min=5)
        sage: [parent(x) for x in w.get_interact_value()]
        [Integer Ring, Integer Ring]
        sage: w = range_slider(int(5)); w
        IntRangeSlider(value=(28, 76), min=5)
        sage: [parent(x) for x in w.get_interact_value()]
        [<... \'int\'>, <... \'int\'>]
        sage: w = range_slider(5, 20, step_size=RDF("0.1")); w
        TransformFloatRangeSlider(value=(8.75, 16.25), max=20.0, min=5.0)
        sage: [parent(x) for x in w.get_interact_value()]
        [Real Double Field, Real Double Field]

    Unfortunately, rational numbers are not supported::

        sage: w = range_slider(5, 20, step_size=10/3); w
        Traceback (most recent call last):
        ...
        NotImplementedError: range_slider does not support rational numbers

    TESTS::

        sage: range_slider(range(5))
        Traceback (most recent call last):
        ...
        NotImplementedError: range_slider does not support a list of values
    '''
def checkbox(default: bool = True, label=None):
    '''
    A checkbox widget.

    INPUT:

    - ``default`` -- boolean; initial value

    - ``label`` -- (optional)

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import checkbox
        sage: checkbox(label="toggle me")
        Checkbox(value=True, description=\'toggle me\')
        sage: checkbox(default=0)
        Checkbox(value=False)
    '''
def selector(values, label=None, default=None, nrows=None, ncols=None, width=None, buttons: bool = False):
    '''
    A widget to select a value from a given list of values.

    This is rendered as a dropdown box (if ``buttons`` is False) or
    as a list of buttons (if ``buttons`` is True).

    INPUT:

    - ``values`` -- list of values to choose from (see examples below
      for the accepted formats for this)

    - ``label`` -- (optional)

    - ``default`` -- initial value

    - ``buttons`` -- boolean; if ``True``, display buttons instead of a
      dropdown box

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import selector
        sage: selector(range(5), label="choose one")
        Dropdown(description=\'choose one\', options=(0, 1, 2, 3, 4), value=0)
        sage: selector(range(5), buttons=True, default=4)
        ToggleButtons(index=4, options=(0, 1, 2, 3, 4), value=4)

    Apart from a simple list, ``values`` can be given as a list of
    2-tuples ``(value, label)``::

        sage: selector([(1,"one"), (2,"two"), (3,"three")])
        Dropdown(options=((\'one\', 1), (\'two\', 2), (\'three\', 3)), value=1)
        sage: selector([(1,"one"), (2,"two"), (3,"three")], buttons=True)
        ToggleButtons(options=((\'one\', 1), (\'two\', 2), (\'three\', 3)), value=1)

    The values can be any kind of object::

        sage: selector([sin(x^2), GF(29), EllipticCurve(\'37a1\')])
        Dropdown(options=(sin(x^2), Finite Field of size 29, Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field), value=sin(x^2))
    '''
def input_grid(nrows, ncols, default=None, label=None, to_value=None, width: int = 4):
    """
    A widget consisting of a grid (matrix) of textboxes.

    The values entered in the textboxes are evaluated (using
    :func:`sage_eval`). These are stored as a list of lists on the
    ``value`` attribute. The value of this widget for an interactive
    function is the result of calling ``to_value`` on this list of
    lists.

    INPUT:

    - ``nrows``, ``ncols`` -- number of rows and columns in the grid

    - ``default`` -- initial value (given as a list of lists, a single
      constant value or a flat list)

    - ``label`` -- (optional)

    - ``to_value`` -- function to be called to get the value for
      interactive functions

    - ``width`` -- width of each textbox

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import input_grid
        sage: input_grid(2, 2, default=42, label='answers')
        Grid(value=[[42, 42], [42, 42]], children=(Label(value='answers'), VBox(children=(EvalText(value='42', layout=Layout(max_width='5em')), EvalText(value='42', layout=Layout(max_width='5em')))), VBox(children=(EvalText(value='42', layout=Layout(max_width='5em')), EvalText(value='42', layout=Layout(max_width='5em'))))))
        sage: w = input_grid(2, 2, default=[[cos(x), sin(x)], [-sin(x), cos(x)]], to_value=matrix); w
        Grid(value=[[cos(x), sin(x)], [-sin(x), cos(x)]], children=(Label(value=''), VBox(children=(EvalText(value='cos(x)', layout=Layout(max_width='5em')), EvalText(value='-sin(x)', layout=Layout(max_width='5em')))), VBox(children=(EvalText(value='sin(x)', layout=Layout(max_width='5em')), EvalText(value='cos(x)', layout=Layout(max_width='5em'))))))
        sage: w.get_interact_value()
        [ cos(x)  sin(x)]
        [-sin(x)  cos(x)]
        sage: w = input_grid(2, 2, default=[1, x, x^2, x^3], to_value=lambda x: x[1][1]); w
        Grid(value=[[1, x], [x^2, x^3]], children=(Label(value=''), VBox(children=(EvalText(value='1', layout=Layout(max_width='5em')), EvalText(value='x^2', layout=Layout(max_width='5em')))), VBox(children=(EvalText(value='x', layout=Layout(max_width='5em')), EvalText(value='x^3', layout=Layout(max_width='5em'))))))
        sage: w.get_interact_value()
        x^3
    """
def color_selector(default=(0, 0, 1), label=None, widget=None, hide_box: bool = False):
    '''
    A widget for choosing a color.

    INPUT:

    - ``default`` -- initial value

    - ``label`` -- (optional)

    - ``hide_box`` -- boolean; if ``True``, do not show the textbox

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.all_jupyter import color_selector
        sage: w = color_selector("orange", label="color me"); w
        SageColorPicker(value=\'#ffa500\', description=\'color me\')
        sage: w.get_interact_value()
        RGB color (1.0, 0.6470588235294118, 0.0)
        sage: color_selector(Color(0.1, 0.2, 0.3))
        SageColorPicker(value=\'#19334c\')
    '''
