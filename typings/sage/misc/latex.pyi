from _typeshed import Incomplete
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.sage_object import SageObject as SageObject

COMMON_HEADER: str
LATEX_HEADER: Incomplete
SLIDE_HEADER: Incomplete

def list_function(x):
    """
    Return the LaTeX code for a list ``x``.

    INPUT:

    - ``x`` -- list

    EXAMPLES::

        sage: from sage.misc.latex import list_function
        sage: list_function([1,2,3])
        '\\\\left[1, 2, 3\\\\right]'
        sage: latex([1,2,3])  # indirect doctest
        \\left[1, 2, 3\\right]
        sage: latex([Matrix(ZZ, 3, range(9)),   # indirect doctest                      # needs sage.modules
        ....:        Matrix(ZZ, 3, range(9))])
        \\left[\\left(\\begin{array}{rrr}
        0 & 1 & 2 \\\\\n        3 & 4 & 5 \\\\\n        6 & 7 & 8
        \\end{array}\\right), \\left(\\begin{array}{rrr}
        0 & 1 & 2 \\\\\n        3 & 4 & 5 \\\\\n        6 & 7 & 8
        \\end{array}\\right)\\right]
    """
def tuple_function(x, combine_all: bool = False):
    """
    Return the LaTeX code for a tuple ``x``.

    INPUT:

    - ``x`` -- tuple

    - ``combine_all`` -- boolean (default: ``False``); if ``combine_all`` is
      ``True``, then it does not return a tuple and instead returns a string
      with all the elements separated by a single space. It does not collapse
      tuples which are inside tuples.

    EXAMPLES::

        sage: from sage.misc.latex import tuple_function
        sage: tuple_function((1,2,3))
        '\\\\left(1, 2, 3\\\\right)'

    Check that :issue:`11775` is fixed::

        sage: tuple_function((1,2,3), combine_all=True)
        '1 2 3'
        sage: tuple_function(((1,2),3), combine_all=True)
        '\\\\left(1, 2\\\\right) 3'
    """
def bool_function(x):
    """
    Return the LaTeX code for a boolean ``x``.

    INPUT:

    - ``x`` -- boolean

    EXAMPLES::

        sage: from sage.misc.latex import bool_function
        sage: print(bool_function(2==3))
        \\mathrm{False}
        sage: print(bool_function(3==(2+1)))
        \\mathrm{True}
    """
def builtin_constant_function(x):
    """
    Return the LaTeX code for a builtin constant ``x``.

    INPUT:

    - ``x`` -- builtin constant

    .. SEEALSO:: Python built-in Constants http://docs.python.org/library/constants.html

    EXAMPLES::

        sage: from sage.misc.latex import builtin_constant_function
        sage: builtin_constant_function(True)
        '\\\\mbox{\\\\rm True}'
        sage: builtin_constant_function(None)
        '\\\\mbox{\\\\rm None}'
        sage: builtin_constant_function(NotImplemented)
        '\\\\mbox{\\\\rm NotImplemented}'
        sage: builtin_constant_function(Ellipsis)
        '\\\\mbox{\\\\rm Ellipsis}'
    """
def None_function(x):
    """
    Return the LaTeX code for ``None``.

    INPUT:

    - ``x`` -- ``None``

    EXAMPLES::

        sage: from sage.misc.latex import None_function
        sage: print(None_function(None))
        \\mathrm{None}
    """
def str_function(x):
    '''
    Return a LaTeX representation of the string ``x``.

    The main purpose of this function is to generate LaTeX representation for
    classes that do not provide a customized method.

    If ``x`` contains only digits with, possibly, a single decimal point and/or
    a sign in front, it is considered to be its own representation. Otherwise
    each line of ``x`` is wrapped in a ``\\texttt`` command and these lines are
    assembled in a left-justified array. This gives to complicated strings the
    closest look to their "terminal representation".

    .. WARNING::

        Such wrappers **cannot** be used as arguments of LaTeX
        commands or in command definitions. If this causes you any problems,
        they probably can be solved by implementing a suitable ``_latex_``
        method for an appropriate class.

    INPUT:

    - ``x`` -- string

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.latex import str_function
        sage: str_function(\'34\')
        \'34\'
        sage: str_function(\'34.5\')
        \'34.5\'
        sage: str_function(\'-34.5\')
        \'-34.5\'
        sage: str_function(\'+34.5\')
        \'+34.5\'
        sage: str_function(\'hello_world\')
        \'\\\\text{\\\\texttt{hello{\\\\char`\\\\_}world}}\'
        sage: str_function(\'-1.00000?\') # trac 12178
        \'-1.00000?\'
    '''
def dict_function(x):
    """
    Return the LaTeX code for a dictionary ``x``.

    INPUT:

    - ``x`` -- dictionary

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.misc.latex import dict_function
        sage: x,y,z = var('x,y,z')
        sage: print(dict_function({x/2: y^2}))
        \\left\\{\\frac{1}{2} \\, x : y^{2}\\right\\}
        sage: d = {(1,2,x^2): [sin(z^2), y/2]}
        sage: latex(d)
        \\left\\{\\left(1, 2, x^{2}\\right) :
               \\left[\\sin\\left(z^{2}\\right), \\frac{1}{2} \\, y\\right]\\right\\}
    """
def float_function(x):
    """
    Return the LaTeX code for a python float ``x``.

    INPUT:

    - ``x`` -- a python float

    EXAMPLES::

        sage: from sage.misc.latex import float_function
        sage: float_function(float(3.14))
        3.14
        sage: float_function(float(1e-10))
        1 \\times 10^{-10}
        sage: float_function(float(2e10))
        20000000000.0

    TESTS:

    Check that :issue:`7356` is fixed::

        sage: latex(float(2e-13))
        2 \\times 10^{-13}
    """

latex_table: Incomplete

class LatexExpr(str):
    '''
    A class for LaTeX expressions.

    Normally, objects of this class are created by a :func:`latex` call. It is
    also possible to generate :class:`LatexExpr` directly from a string, which
    must contain valid LaTeX code for typesetting in math mode (without dollar
    signs). In the Jupyter notebook, use
    :func:`~sage.repl.rich_output.pretty_print.pretty_print` to actually see
    the typeset LaTeX code; alternatively, from either the command-line or the
    notebook, use the :func:`view` function.

    INPUT:

    - ``str`` -- string with valid math mode LaTeX code (or something
      which can be converted to such a string)

    OUTPUT: :class:`LatexExpr` wrapping the string representation of the input

    EXAMPLES::

        sage: latex(x^20 + 1)                                                           # needs sage.symbolic
        x^{20} + 1
        sage: LatexExpr(r"\\frac{x^2 + 1}{x - 2}")                                       # needs sage.symbolic
        \\frac{x^2 + 1}{x - 2}

    ``LatexExpr`` simply converts to string without doing anything
    extra, it does *not* call :func:`latex`::

        sage: latex(ZZ)
        \\Bold{Z}
        sage: LatexExpr(ZZ)
        Integer Ring

    The result of :func:`latex` is of type ``LatexExpr``::

        sage: L = latex(x^20 + 1)                                                       # needs sage.symbolic
        sage: L                                                                         # needs sage.symbolic
        x^{20} + 1
        sage: type(L)                                                                   # needs sage.symbolic
        <class \'sage.misc.latex.LatexExpr\'>

    A ``LatexExpr`` can be converted to a plain string::

        sage: str(latex(x^20 + 1))                                                      # needs sage.symbolic
        \'x^{20} + 1\'
    '''
    def __add__(self, other):
        '''
        Add a LatexExpr and another LatexExpr (or a string).

        EXAMPLES::

            sage: o = LatexExpr(r"\\Delta\\neq") + LatexExpr(r"\\frac{x}{2}"); o
            \\Delta\\neq \\frac{x}{2}
            sage: type(o)
            <class \'sage.misc.latex.LatexExpr\'>
            sage: o = LatexExpr(r"\\Delta\\neq") + r"\\frac{x}{2}"; o
            \\Delta\\neq \\frac{x}{2}
            sage: type(o)
            <class \'sage.misc.latex.LatexExpr\'>

        We add extra space only if it was not there yet::

            sage: LatexExpr("foo ") + LatexExpr("bar")
            foo bar
            sage: LatexExpr("foo") + LatexExpr(" bar")
            foo bar
            sage: str(LatexExpr("") + LatexExpr("bar"))
            \'bar\'
            sage: str(LatexExpr("foo") + LatexExpr(""))
            \'foo\'
        '''
    def __radd__(self, other):
        '''
        Add a string and a LatexExpr.

        EXAMPLES::

            sage: o = "a =" + LatexExpr("b")
            sage: o
            a = b
            sage: type(o)
            <class \'sage.misc.latex.LatexExpr\'>
        '''

def has_latex_attr(x) -> bool:
    '''
    Return ``True`` if ``x`` has a ``_latex_`` attribute, except if ``x``
    is a ``type``, in which case return ``False``.

    EXAMPLES::

        sage: from sage.misc.latex import has_latex_attr
        sage: has_latex_attr(identity_matrix(3))                                        # needs sage.modules
        True
        sage: has_latex_attr("abc")  # strings have no _latex_ method
        False

    Types inherit the ``_latex_`` method of the class to which they refer,
    but calling it is broken::

        sage: # needs sage.modules
        sage: T = type(identity_matrix(3)); T
        <class \'sage.matrix.matrix_integer_dense.Matrix_integer_dense\'>
        sage: hasattr(T, \'_latex_\')
        True
        sage: T._latex_()
        Traceback (most recent call last):
        ...
        TypeError: ..._latex_... needs an argument
        sage: has_latex_attr(T)
        False
    '''
@cached_function
def default_engine():
    """
    Return the default latex engine and the official name of the engine.
    This is determined by availability of the popular engines on the user's
    system. It is assumed that at least latex is available.

    This function is deprecated as part of the public API. There is
    instead an internal counterpart :func:`_default_engine`, but no
    stability promises are made with regards to its interface.

    EXAMPLES::

        sage: from sage.misc.latex import default_engine
        sage: default_engine()  # random
        ('lualatex', 'LuaLaTeX')
    """

class _Latex_prefs_object(SageObject):
    """
    An object that holds LaTeX global preferences.
    """
    def __init__(self, bb: bool = False, delimiters=['(', ')'], matrix_column_alignment: str = 'r') -> None:
        """
        Define an object that holds LaTeX global preferences.

        EXAMPLES::

            sage: from sage.misc.latex import _Latex_prefs_object
            sage: latex_prefs = _Latex_prefs_object()
            sage: TestSuite(latex_prefs).run(skip ='_test_pickling')
        """

def latex_extra_preamble():
    """
    Return the string containing the user-configured preamble,
    ``sage_latex_macros``, and any user-configured macros.  This is
    used in the :meth:`~Latex.eval` method for the :class:`Latex`
    class, and in :func:`_latex_file_`; it follows either
    ``LATEX_HEADER`` or ``SLIDE_HEADER`` (defined at the top of this
    file) which is a string containing the documentclass and standard
    usepackage commands.

    EXAMPLES::

        sage: from sage.misc.latex import latex_extra_preamble
        sage: print(latex_extra_preamble())
        <BLANKLINE>
        \\newcommand{\\ZZ}{\\Bold{Z}}
        \\newcommand{\\NN}{\\Bold{N}}
        \\newcommand{\\RR}{\\Bold{R}}
        \\newcommand{\\CC}{\\Bold{C}}
        \\newcommand{\\QQ}{\\Bold{Q}}
        \\newcommand{\\QQbar}{\\overline{\\QQ}}
        \\newcommand{\\GF}[1]{\\Bold{F}_{#1}}
        \\newcommand{\\Zp}[1]{\\Bold{Z}_{#1}}
        \\newcommand{\\Qp}[1]{\\Bold{Q}_{#1}}
        \\newcommand{\\Zmod}[1]{\\ZZ/#1\\ZZ}
        \\newcommand{\\CDF}{\\Bold{C}}
        \\newcommand{\\CIF}{\\Bold{C}}
        \\newcommand{\\CLF}{\\Bold{C}}
        \\newcommand{\\RDF}{\\Bold{R}}
        \\newcommand{\\RIF}{\\Bold{I} \\Bold{R}}
        \\newcommand{\\RLF}{\\Bold{R}}
        \\newcommand{\\SL}{\\mathrm{SL}}
        \\newcommand{\\PSL}{\\mathrm{PSL}}
        \\newcommand{\\lcm}{\\mathop{\\operatorname{lcm}}}
        \\newcommand{\\dist}{\\mathrm{dist}}
        \\newcommand{\\Bold}[1]{\\mathbf{#1}}
        <BLANKLINE>
    """

class LatexCall:
    """
    Typeset Sage objects via a ``__call__`` method to this class,
    typically by calling those objects' ``_latex_`` methods.  The
    class :class:`Latex` inherits from this. This class is used in
    :mod:`~sage.misc.latex_macros`, while functions from
    :mod:`~sage.misc.latex_macros` are used in :class:`Latex`, so this
    is here primarily to avoid circular imports.

    EXAMPLES::

        sage: from sage.misc.latex import LatexCall
        sage: LatexCall()(ZZ)
        \\Bold{Z}
        sage: LatexCall().__call__(ZZ)
        \\Bold{Z}

    This returns an instance of the class :class:`LatexExpr`::

        sage: type(LatexCall()(ZZ))
        <class 'sage.misc.latex.LatexExpr'>
    """
    def __call__(self, x, combine_all: bool = False):
        """
        Return a :class:`LatexExpr` built out of the argument ``x``.

        INPUT:

        - ``x`` -- a Sage object

        - ``combine_all`` -- boolean (default: ``False``); if ``combine_all``
          is ``True`` and the input is a tuple, then it does not return a
          tuple and instead returns a string with all the elements separated by
          a single space

        OUTPUT: a :class:`LatexExpr` built from ``x``

        EXAMPLES::

            sage: latex(Integer(3))  # indirect doctest
            3
            sage: latex(1==0)
            \\mathrm{False}
            sage: print(latex([x, 2]))                                                  # needs sage.symbolic
            \\left[x, 2\\right]

        Check that :issue:`11775` is fixed::

            sage: latex((x,2), combine_all=True)                                        # needs sage.symbolic
            x 2
        """

class Latex(LatexCall):
    '''nodetex
    Enter, e.g.,

    ::

        %latex
        The equation $y^2 = x^3 + x$ defines an elliptic curve.
        We have $2006 = \\sage{factor(2006)}$.

    in an input cell in the notebook to get a typeset version. Use
    ``%latex_debug`` to get debugging output.

    Use ``latex(...)`` to typeset a Sage object.  Use :class:`LatexExpr`
    to typeset LaTeX code that you create by hand.

    Use ``%slide`` instead to typeset slides.

    .. WARNING::

       You must have dvipng (or dvips and magick/convert) installed
       on your operating system, or this command will not work.

    EXAMPLES::

        sage: latex(x^20 + 1)                                                           # needs sage.symbolic
        x^{20} + 1
        sage: latex(FiniteField(25,\'a\'))                                                # needs sage.rings.finite_rings
        \\Bold{F}_{5^{2}}
        sage: latex("hello")
        \\text{\\texttt{hello}}
        sage: LatexExpr(r"\\frac{x^2 - 1}{x + 1} = x - 1")
        \\frac{x^2 - 1}{x + 1} = x - 1

    LaTeX expressions can be added; note that a space is automatically
    inserted::

        sage: LatexExpr(r"y \\neq") + latex(x^20 + 1)                                    # needs sage.symbolic
        y \\neq x^{20} + 1
    '''
    def __init__(self, debug: bool = False, slide: bool = False, density: int = 150, engine=None) -> None:
        """
        Initialize the latex builder.

        EXAMPLES::

            sage: from sage.misc.latex import Latex
            sage: l = Latex()
            sage: TestSuite(l).run(skip ='_test_pickling')
        """
    def eval(self, x, globals, strip: bool = False, filename=None, debug=None, density=None, engine=None, locals={}):
        '''
        Compile the formatted tex given by ``x`` as a png and writes the
        output file to the directory given by ``filename``.

        INPUT:

        - ``globals`` -- a globals dictionary

        - ``x`` -- string to evaluate

        - ``strip`` -- ignored

        - ``filename`` -- output filename

        - ``debug`` -- whether to print verbose debugging output

        - ``density`` -- how big output image is

        - ``engine`` -- latex engine to use. Currently ``\'latex\'``,
          ``\'pdflatex\'``, ``\'xelatex\'`` and ``\'lualatex\'`` are supported

        - ``locals`` -- extra local variables used when evaluating Sage code in ``x``

        .. WARNING::

            When using ``\'latex\'`` (the default), you must have ``dvipng`` (or
            ``dvips`` and ``magick/convert``) installed on your operating system, or
            this command will not work.  When using ``\'pdflatex\'``, ``\'xelatex\'``
            or ``\'lualatex\'``, you must have ``magick/convert`` installed.

        OUTPUT:

        If it compiled successfully, this returns an empty string ``\'\'``,
        otherwise it returns ``None``.

        EXAMPLES::

            sage: fn = tmp_filename()
            sage: latex.eval("$\\\\ZZ[x]$", locals(), filename=fn) # not tested
            \'\'
            sage: latex.eval(r"\\ThisIsAnInvalidCommand", {}) # optional -- latex ImageMagick
            An error occurred...
        '''
    def blackboard_bold(self, t=None):
        """nodetex
        Controls whether Sage uses blackboard bold or ordinary bold
        face for typesetting ``ZZ``, ``RR``, etc.

        INPUT:

        - ``t`` -- boolean or ``None``

        OUTPUT:

        If ``t`` is ``None``, return the current setting (``True`` or
        ``False``).

        If ``t`` is ``True``, use blackboard bold (``\\mathbb``); otherwise use
        boldface (``\\mathbf``).

        EXAMPLES::

            sage: latex.blackboard_bold()
            False
            sage: latex.blackboard_bold(True)
            sage: latex.blackboard_bold()
            True
            sage: latex.blackboard_bold(False)
        """
    def matrix_delimiters(self, left=None, right=None):
        """nodetex
        Change the left and right delimiters for the LaTeX representation
        of matrices

        INPUT:

        - ``left``, ``right`` -- strings or ``None``

        If both ``left`` and ``right`` are ``None``, then return the
        current delimiters.  Otherwise, set the left and/or right
        delimiters, whichever are specified.

        Good choices for ``left`` and ``right`` are any delimiters which
        LaTeX understands and knows how to resize; some examples are:

        - parentheses: ``'('``, ``')'``
        - brackets: ``'['``, ``']'``
        - braces: ``'\\\\{'``, ``'\\\\}'``
        - vertical lines: ``'|'``
        - angle brackets: ``'\\\\langle'``, ``'\\\\rangle'``

        .. NOTE::

            Putting aside aesthetics, you may combine these in any way
            imaginable; for example, you could set ``left`` to be a right-hand
            bracket ``']'`` and ``right`` to be a right-hand brace ``'\\\\}'``,
            and it will be typeset correctly.

        EXAMPLES::

            sage: # needs sage.modules
            sage: a = matrix(1, 1, [17])
            sage: latex(a)
            \\left(\\begin{array}{r}
            17
            \\end{array}\\right)
            sage: latex.matrix_delimiters('[', ']')
            sage: latex(a)
            \\left[\\begin{array}{r}
            17
            \\end{array}\\right]
            sage: latex.matrix_delimiters(left='\\\\{')
            sage: latex(a)
            \\left\\{\\begin{array}{r}
            17
            \\end{array}\\right]
            sage: latex.matrix_delimiters()
            ['\\\\{', ']']

        Restore defaults::

            sage: latex.matrix_delimiters('(', ')')
        """
    def vector_delimiters(self, left=None, right=None):
        """nodetex
        Change the left and right delimiters for the LaTeX representation
        of vectors

        INPUT:

        - ``left``, ``right`` -- strings or ``None``

        If both ``left`` and ``right`` are ``None``, then return the
        current delimiters.  Otherwise, set the left and/or right
        delimiters, whichever are specified.

        Good choices for ``left`` and ``right`` are any delimiters which
        LaTeX understands and knows how to resize; some examples are:

        - parentheses: ``'('``, ``')'``
        - brackets: ``'['``, ``']'``
        - braces: ``'\\\\{'``, ``'\\\\}'``
        - vertical lines: ``'|'``
        - angle brackets: ``'\\\\langle'``, ``'\\\\rangle'``

        .. NOTE::

            Putting aside aesthetics, you may combine these in any way
            imaginable; for example, you could set ``left`` to be a right-hand
            bracket ``']'`` and ``right`` to be a right-hand brace ``'\\\\}'``, and it
            will be typeset correctly.

        EXAMPLES::

            sage: # needs sage.modules
            sage: a = vector(QQ, [1,2,3])
            sage: latex(a)
            \\left(1,\\,2,\\,3\\right)
            sage: latex.vector_delimiters('[', ']')
            sage: latex(a)
            \\left[1,\\,2,\\,3\\right]
            sage: latex.vector_delimiters(right='\\\\}')
            sage: latex(a)
            \\left[1,\\,2,\\,3\\right\\}
            sage: latex.vector_delimiters()
            ['[', '\\\\}']

        Restore defaults::

            sage: latex.vector_delimiters('(', ')')
        """
    def matrix_column_alignment(self, align=None):
        """nodetex
        Changes the column-alignment of the LaTeX representation of
        matrices.

        INPUT:

        - ``align`` -- string (``'r'`` for right, ``'c'`` for center,
          ``'l'`` for left) or ``None``

        OUTPUT:

        If ``align`` is ``None``, then returns the current
        alignment-string. Otherwise, set this alignment.

        The input ``align`` can be any string which the LaTeX
        ``array``-environment understands as a parameter for
        aligning a column.

        EXAMPLES::

            sage: # needs sage.modules
            sage: a = matrix(1, 1, [42])
            sage: latex(a)
            \\left(\\begin{array}{r}
            42
            \\end{array}\\right)
            sage: latex.matrix_column_alignment('c')
            sage: latex(a)
            \\left(\\begin{array}{c}
            42
            \\end{array}\\right)
            sage: latex.matrix_column_alignment('l')
            sage: latex(a)
            \\left(\\begin{array}{l}
            42
            \\end{array}\\right)

        Restore defaults::

            sage: latex.matrix_column_alignment('r')
        """
    @cached_method
    def has_file(self, file_name) -> bool:
        '''
        INPUT:

        - ``file_name`` -- string

        Tests whether the local LaTeX installation includes ``file_name``.

        EXAMPLES::

            sage: latex.has_file("article.cls")      # optional - latex
            True
            sage: latex.has_file("some_inexistent_file.sty")
            False
        '''
    @cached_method
    def check_file(self, file_name, more_info: str = '') -> None:
        '''
        INPUT:

        - ``file_name`` -- string

        - ``more_info`` -- string (default: ``\'\'``)

        Emit a warning if the local LaTeX installation does not
        include ``file_name``. The string ``more_info`` is appended
        to the warning message. The warning is only emitted the first
        time this method is called.

        EXAMPLES::

            sage: latex.check_file("article.cls")       # optional - latex
            sage: latex.check_file("some_inexistent_file.sty")
            Warning: `some_inexistent_file.sty` is not part of this computer\'s TeX installation.
            sage: latex.check_file("some_inexistent_file.sty")
            sage: latex.check_file("some_inexistent_file.sty", "This file is required for blah. It can be downloaded from: http://blah.org/")
            Warning: `some_inexistent_file.sty` is not part of this computer\'s TeX installation.
            This file is required for blah. It can be downloaded from: http://blah.org/

        This test checks that the bug in :issue:`9091` is fixed::

            sage: latex.check_file("article.cls", "The article class is really critical.")    # optional - latex
        '''
    def extra_macros(self, macros=None):
        '''nodetex
        String containing extra LaTeX macros to use with ``%latex`` and ``%html``.

        INPUT:

        - ``macros`` -- string (default: ``None``)

        If ``macros`` is ``None``, return the current string.  Otherwise,
        set it to ``macros``.  If you want to *append* to the string
        of macros instead of replacing it, use
        :meth:`latex.add_macro <Latex.add_macro>`.

        EXAMPLES::

            sage: latex.extra_macros("\\\\newcommand{\\\\foo}{bar}")
            sage: latex.extra_macros()
            \'\\\\newcommand{\\\\foo}{bar}\'
            sage: latex.extra_macros("")
            sage: latex.extra_macros()
            \'\'
        '''
    def add_macro(self, macro) -> None:
        '''nodetex
        Append to the string of extra LaTeX macros, for use with %latex and %html.

        INPUT:

        - ``macro`` -- string

        EXAMPLES::

            sage: latex.extra_macros()
            \'\'
            sage: latex.add_macro("\\\\newcommand{\\\\foo}{bar}")
            sage: latex.extra_macros()
            \'\\\\newcommand{\\\\foo}{bar}\'
            sage: latex.extra_macros("")  # restore to default
        '''
    def extra_preamble(self, s=None):
        '''nodetex
        String containing extra preamble to be used with %latex.

        INPUT:

        - ``s`` -- string or ``None``

        If ``s`` is ``None``, return the current preamble.  Otherwise, set
        it to ``s``.  If you want to *append* to the current extra
        preamble instead of replacing it, use
        :meth:`latex.add_to_preamble <Latex.add_to_preamble>`.

        You will almost certainly need to use this when using the
        XeLaTeX engine; see below or the documentation for
        :func:`engine` for a suggested preamble.

        EXAMPLES::

            sage: latex.extra_preamble("\\\\DeclareMathOperator{\\\\Ext}{Ext}")
            sage: latex.extra_preamble()
            \'\\\\DeclareMathOperator{\\\\Ext}{Ext}\'
            sage: latex.extra_preamble("\\\\"+r"usepackage{fontspec,xunicode,xltxtra}\\setmainfont[Mapping=tex-text]{UnBatang}\\setmonofont[Mapping=tex-text]{UnDotum}")
            sage: latex.extra_preamble()
            \'\\\\usepackage{fontspec,xunicode,xltxtra}\\\\setmainfont[Mapping=tex-text]{UnBatang}\\\\setmonofont[Mapping=tex-text]{UnDotum}\'
            sage: latex.extra_preamble("")
            sage: latex.extra_preamble()
            \'\'
        '''
    def add_to_preamble(self, s) -> None:
        '''nodetex
        Append to the string ``s`` of extra LaTeX macros, for use with
        ``%latex``.

        EXAMPLES::

            sage: latex.extra_preamble()
            \'\'
            sage: latex.add_to_preamble("\\\\DeclareMathOperator{\\\\Ext}{Ext}")

        At this point, a notebook cell containing

        ::

          %latex
          $\\Ext_A^*(\\GF{2}, \\GF{2}) \\Rightarrow \\pi_*^s*(S^0)$

        will be typeset correctly.

        ::

            sage: latex.add_to_preamble("\\\\usepackage{xypic}")
            sage: latex.extra_preamble()
            \'\\\\DeclareMathOperator{\\\\Ext}{Ext}\\\\usepackage{xypic}\'

        Now one can put various xypic diagrams into a ``%latex`` cell, such as

        ::

          %latex
          \\[ \\xymatrix{ \\circ \\ar `r[d]^{a} `[rr]^{b} `/4pt[rr]^{c} `[rrr]^{d}
          `_dl[drrr]^{e} [drrr]^{f} & \\circ & \\circ & \\circ \\\\ \\circ & \\circ &
          \\circ & \\circ } \\]

        Reset the preamble to its default, the empty string::

            sage: latex.extra_preamble(\'\')
            sage: latex.extra_preamble()
            \'\'
        '''
    def add_package_to_preamble_if_available(self, package_name) -> None:
        '''
        Add a ``\\usepackage{package_name}`` instruction to the latex
        preamble if not yet present there, and if ``package_name.sty``
        is available in the LaTeX installation.

        INPUT:

        - ``package_name`` -- string

        .. SEEALSO::

            - :meth:`add_to_preamble`
            - :meth:`has_file`.

        TESTS::

            sage: latex.add_package_to_preamble_if_available("tkz-graph")
            sage: latex.add_package_to_preamble_if_available("nonexistent_package")
            sage: latex.extra_preamble()  # optional - latex latex_package_tkz_graph
            \'\\\\usepackage{tkz-graph}\\n\'
            sage: latex.extra_preamble(\'\')
        '''
    def engine(self, e=None):
        '''
        Set Sage to use ``e`` as latex engine when typesetting with
        :func:`view`, in ``%latex`` cells, etc.

        INPUT:

        - ``e`` -- ``\'latex\'``, ``\'pdflatex\'``, ``\'xelatex\'``, ``\'lualatex\'`` or ``None``

        If  ``e`` is ``None``, return the current engine.

        If using the XeLaTeX engine, it will almost always be necessary
        to set the proper preamble with :func:`extra_preamble` or
        :func:`add_to_preamble`. For example::

            latex.extra_preamble(r\'\'\'\\usepackage{fontspec,xunicode,xltxtra}
            \\setmainfont[Mapping=tex-text]{some font here}
            \\setmonofont[Mapping=tex-text]{another font here}\'\'\')

        EXAMPLES::

            sage: latex.engine()  # random
            \'lualatex\'
            sage: latex.engine("latex")
            sage: latex.engine()
            \'latex\'
            sage: latex.engine("pdflatex")
            sage: latex.engine()
            \'pdflatex\'
        '''

latex: Incomplete

def view(objects, title: str = 'Sage', debug: bool = False, sep: str = '', tiny: bool = False, engine=None, viewer=None, tightpage: bool = True, margin=None, mode: str = 'inline', combine_all: bool = False, **kwds) -> None:
    '''nodetex
    Compute a latex representation of each object in objects, compile,
    and display typeset. If used from the command line, this requires
    that latex be installed.

    INPUT:

    - ``objects`` -- list (or object)

    - ``title`` -- string (default: ``\'Sage\'``); title for the
      document

    - ``debug`` -- boolean (default: ``False``); print verbose
      output

    - ``sep`` -- string (default: ``\'\'``); separator between
      math objects

    - ``tiny`` -- boolean (default: ``False``); use tiny font

    - ``engine`` -- string or ``None`` (default: ``None``); can take the
      following values:

      - ``None`` -- the value defined in the LaTeX global preferences
        ``latex.engine()`` is used

      - ``\'pdflatex\'`` -- compilation does ``tex`` -> ``pdf``

      - ``\'xelatex\'`` -- compilation does ``tex`` -> ``pdf``

      - ``\'lualatex\'`` -- compilation does ``tex`` -> ``pdf``

      - ``\'latex\'`` -- compilation first tries ``tex`` -> ``dvi`` -> ``png`` and if an
        error occurs then tries ``dvi`` -> ``ps`` -> ``pdf``. This is slower than
        ``\'pdflatex\'`` and known to be broken when overfull hboxes are detected.

    - ``viewer`` -- string or ``None`` (default: ``None``); specify a viewer
      to use; currently the only options are ``None`` and ``\'pdf\'``

    - ``tightpage`` -- boolean (default: ``True``); use the LaTeX package
       ``preview`` with the \'tightpage\' option

    - ``margin`` -- float or ``None`` (default: ``None``); adds a margin
      of ``margin`` mm. Has no affect if the option ``tightpage`` is ``False``.

    - ``mode`` -- string (default: ``\'inline\'``); ``\'display\'`` for
      displaymath or ``\'inline\'`` for inline math

    - ``combine_all`` -- boolean (default: ``False``); if ``combine_all`` is
      ``True`` and the input is a tuple, then it does not return a tuple and
      instead returns a string with all the elements separated by a single
      space

    OUTPUT: display typeset objects

    The output is displayed in a separate viewer displaying a dvi (or pdf)
    file, with the following: the title string is printed, centered, at the
    top. Beneath that, each object in ``objects`` is typeset on its own line,
    with the string ``sep`` inserted between these lines.

    The value of ``sep`` is inserted between each element of the list
    ``objects``; you can, for example, add vertical space between
    objects with ``sep=\'\\\\vspace{15mm}\'``, while ``sep=\'\\\\hrule\'``
    adds a horizontal line between objects, and ``sep=\'\\\\newpage\'``
    inserts a page break between objects.

    If the ``engine`` is either ``\'pdflatex\'``, ``\'xelatex\'``, or ``\'lualatex\'``,
    it produces a pdf file. Otherwise, it produces a dvi file, and if the program
    ``dvipng`` is installed, it checks the dvi file by trying to convert it to a
    png file.  If this conversion fails, the dvi file probably contains some
    postscript special commands or it has other issues which might make
    displaying it a problem; in this case, the file is converted to a pdf file,
    which is then displayed.

    Setting ``viewer`` to ``\'pdf\'`` forces the use of a separate
    viewer, even in notebook mode. This also sets the latex engine to be
    ``pdflatex`` if the current engine is ``latex``.

    Setting the option ``tightpage`` to ``True`` (this is the default setting)
    tells LaTeX to use  the package \'preview\' with the \'tightpage\' option.
    Then, each object is typeset in its own page, and that page is cropped to
    exactly the size of the object. This is typically useful for very
    large pictures (like graphs) generated with tikz. This only works
    when using a separate viewer. Note that the object are currently
    typeset in plain math mode rather than displaymath, because the
    latter imposes a limit on the width of the picture. Technically,
    ``tightpage`` adds ::

        \\\\usepackage[tightpage,active]{preview}
        \\\\PreviewEnvironment{page}

    to the LaTeX preamble, and replaces the ``\\\\[`` and ``\\\\]`` around
    each object by ``\\\\begin{page}$`` and ``$\\\\end{page}``.
    Setting ``tightpage`` to ``False`` turns off this behavior and provides
    the latex output as a full page. If ``tightpage`` is set to ``True``,
    the ``Title`` is ignored.

    TESTS::

        sage: from sage.misc.latex import _run_latex_, _latex_file_
        sage: from tempfile import NamedTemporaryFile
        sage: g = sage.misc.latex.latex_examples.graph()
        sage: latex.add_to_preamble(r"\\usepackage{tkz-graph}")  # optional - latex_package_tkz_graph
        sage: with NamedTemporaryFile(mode=\'w+t\', suffix=\'.tex\') as f:  # optional - latex latex_package_tkz_graph
        ....:     _ = f.write(_latex_file_(g))
        ....:     f.flush()
        ....:     _run_latex_(f.name, engine=\'pdflatex\')
        \'pdf\'

        sage: view(4, margin=5, debug=True)     # not tested
        \\documentclass{article}
        ...
        \\usepackage[tightpage,active]{preview}
        \\PreviewEnvironment{page}
        \\setlength\\PreviewBorder{5.000000mm}
        \\begin{document}\\begin{page}$4$\\end{page}
        \\end{document}
        ...

        sage: view(4, debug=True)               # not tested
        \\documentclass{article}
        ...
        \\usepackage[tightpage,active]{preview}
        \\PreviewEnvironment{page}
        \\begin{document}\\begin{page}$4$\\end{page}
        \\end{document}
        ...


        sage: latex.extra_preamble(\'\') # reset the preamble

        sage: view(4, engine=\'garbage\')
        Traceback (most recent call last):
        ...
        ValueError: Unsupported LaTeX engine.
    '''
def pdf(x, filename, tiny: bool = False, tightpage: bool = True, margin=None, engine=None, debug: bool = False) -> None:
    '''
    Create an image from the latex representation of ``x`` and save it as a pdf
    file with the given filename.

    INPUT:

    - ``x`` -- a Sage object

    - ``filename`` -- the filename with which to save the image

    - ``tiny`` -- boolean (default: ``False``); if ``True``, use a tiny font

    - ``tightpage`` -- boolean (default: ``True``); use the LaTeX package
      ``preview`` with the \'tightpage\' option

    - ``margin`` -- float (default: no margin); width of border, only effective
      with \'tight page\'

    - ``engine`` -- (default: ``None``) ``\'latex\'``, ``\'pdflatex\'``,
      ``\'xelatex\'`` or ``\'lualatex\'``; if ``None``, the value defined in the
      LaTeX global preferences ``latex.engine()`` is used

    - ``debug`` -- boolean (default: ``False``); if ``True``, print verbose output

    EXAMPLES::

        sage: # optional - latex
        sage: from sage.misc.latex import pdf
        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(suffix=".pdf") as f:  # random
        ....:     pdf(ZZ[x], f.name)
    '''
def png(x, filename, density: int = 150, debug: bool = False, do_in_background: bool = False, tiny: bool = False, engine=None):
    """
    Create a png image representation of ``x`` and save to the given
    filename.

    INPUT:

    - ``x`` -- object to be displayed

    - ``filename`` -- file in which to save the image

    - ``density`` -- integer (default: 150)

    - ``debug`` -- boolean (default: ``False``); print verbose output

    - ``do_in_background`` -- boolean (default: ``False``); unused, kept for
      backwards compatibility

    - ``tiny`` -- boolean (default: ``False``); use tiny font

    - ``engine`` -- (default: ``None``) ``'latex'``, ``'pdflatex'``,
      ``'xelatex'`` or ``'lualatex'``

    EXAMPLES::

        sage: # optional - imagemagick latex, needs sage.plot
        sage: from sage.misc.latex import png
        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:  # random
        ....:     png(ZZ[x], f.name)
    """
def coeff_repr(c):
    """
    LaTeX string representing coefficients in a linear combination.

    INPUT:

    - ``c`` -- a coefficient (i.e., an element of a ring)

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.latex import coeff_repr
        sage: coeff_repr(QQ(1/2))
        '\\\\frac{1}{2}'
        sage: coeff_repr(-x^2)                                                          # needs sage.symbolic
        '\\\\left(-x^{2}\\\\right)'
    """
def repr_lincomb(symbols, coeffs):
    """
    Compute a latex representation of a linear combination of some
    formal symbols.

    INPUT:

    - ``symbols`` -- list of symbols

    - ``coeffs`` -- list of coefficients of the symbols

    OUTPUT: string

    EXAMPLES::

        sage: t = PolynomialRing(QQ, 't').0
        sage: from sage.misc.latex import repr_lincomb
        sage: repr_lincomb(['a', 's', ''], [-t, t - 2, t^12 + 2])
        '-t\\\\text{\\\\texttt{a}} + \\\\left(t - 2\\\\right)\\\\text{\\\\texttt{s}} + \\\\left(t^{12} + 2\\\\right)'
        sage: repr_lincomb(['a', 'b'], [1,1])
        '\\\\text{\\\\texttt{a}} + \\\\text{\\\\texttt{b}}'

    Verify that a certain corner case works (see :issue:`5707` and
    :issue:`5766`)::

        sage: repr_lincomb([1,5,-3],[2,8/9,7])
        '2\\\\cdot 1 + \\\\frac{8}{9}\\\\cdot 5 + 7\\\\cdot -3'

    Verify that :issue:`17299` (latex representation of modular symbols)
    is fixed::

        sage: x = EllipticCurve('64a1').modular_symbol_space(sign=1).basis()[0]         # needs sage.schemes
        sage: from sage.misc.latex import repr_lincomb
        sage: latex(x.modular_symbol_rep())                                             # needs sage.schemes
        \\left\\{\\frac{-3}{11}, \\frac{-1}{4}\\right\\} - \\left\\{\\frac{3}{13}, \\frac{1}{4}\\right\\}

    Verify that it works when the symbols are numbers::

        sage: x = FormalSum([(1,2),(3,4)])
        sage: latex(x)
        2 + 3\\cdot 4

    Verify that it works when ``bv in CC`` raises an error::

        sage: x = FormalSum([(1,'x'),(2,'y')])
        sage: latex(x)
        \\text{\\texttt{x}} + 2\\text{\\texttt{y}}
    """

common_varnames: Incomplete

def latex_varify(a, is_fname: bool = False):
    '''
    Convert a string ``a`` to a LaTeX string: if it\'s an element of
    ``common_varnames``, then prepend a backslash.  If ``a`` consists
    of a single letter, then return it.  Otherwise, return
    either "{\\\\rm a}" or "\\\\mbox{a}" if "is_fname" flag is ``True``
    or ``False``.

    INPUT:

    - ``a`` -- string

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.latex import latex_varify
        sage: latex_varify(\'w\')
        \'w\'
        sage: latex_varify(\'aleph\')
        \'\\\\mathit{aleph}\'
        sage: latex_varify(\'aleph\', is_fname=True)
        \'{\\\\rm aleph}\'
        sage: latex_varify(\'alpha\')
        \'\\\\alpha\'
        sage: latex_varify(\'ast\')
        \'\\\\ast\'

    TESTS:

        sage: abc = var(\'abc\')                                                          # needs sage.symbolic
        sage: latex((abc/(abc+1)+42)/(abc-1))  # trac #15870                            # needs sage.symbolic
        \\frac{\\frac{\\mathit{abc}}{\\mathit{abc} + 1} + 42}{\\mathit{abc} - 1}
    '''
def latex_variable_name(x, is_fname: bool = False):
    """
    Return latex version of a variable name.

    Here are some guiding principles for usage of this function:

    1. If the variable is a single letter, that is the latex version.

    2. If the variable name is suffixed by a number, we put the number
       in the subscript.

    3. If the variable name contains an ``'_'`` we start the subscript at
       the underscore. Note that #3 trumps rule #2.

    4. If a component of the variable is a Greek letter, escape it
       properly.

    5. Recurse nicely with subscripts.

    Refer to the examples section for how these rules might play out in
    practice.

    EXAMPLES::

        sage: from sage.misc.latex import latex_variable_name
        sage: latex_variable_name('a')
        'a'
        sage: latex_variable_name('abc')
        '\\\\mathit{abc}'
        sage: latex_variable_name('sigma')
        '\\\\sigma'
        sage: latex_variable_name('sigma_k')
        '\\\\sigma_{k}'
        sage: latex_variable_name('sigma389')
        '\\\\sigma_{389}'
        sage: latex_variable_name('beta_00')
        '\\\\beta_{00}'
        sage: latex_variable_name('Omega84')
        '\\\\Omega_{84}'
        sage: latex_variable_name('sigma_alpha')
        '\\\\sigma_{\\\\alpha}'
        sage: latex_variable_name('nothing1')
        '\\\\mathit{nothing}_{1}'
        sage: latex_variable_name('nothing1', is_fname=True)
        '{\\\\rm nothing}_{1}'
        sage: latex_variable_name('nothing_abc')
        '\\\\mathit{nothing}_{\\\\mathit{abc}}'
        sage: latex_variable_name('nothing_abc', is_fname=True)
        '{\\\\rm nothing}_{{\\\\rm abc}}'
        sage: latex_variable_name('alpha_beta_gamma12')
        '\\\\alpha_{\\\\beta_{\\\\gamma_{12}}}'
        sage: latex_variable_name('x_ast')
        'x_{\\\\ast}'

    TESTS::

        sage: latex_variable_name('_C')  # trac #16007                                  # needs sage.symbolic
        'C'
        sage: latex_variable_name('_K1')                                                # needs sage.symbolic
        'K_{1}'

        sage: latex_variable_name('5')                                                  # needs sage.symbolic
        '5'
    """

class LatexExamples:
    """
    A catalogue of Sage objects with complicated ``_latex_`` methods.
    Use these for testing :func:`latex`, :func:`view`, the Typeset
    button in the notebook, etc.

    The classes here only have ``__init__``, ``_repr_``, and ``_latex_``
    methods.

    EXAMPLES::

        sage: from sage.misc.latex import latex_examples
        sage: K = latex_examples.knot()
        sage: K
        LaTeX example for testing display of a knot produced by xypic...
        sage: latex(K)
        \\vtop{\\vbox{\\xygraph{!{0;/r1.5pc/:}
        [u] !{\\vloop<(-.005)\\khole||\\vcrossneg \\vunder- }
        [] !{\\ar @{-}@'{p-(1,0)@+}+(-1,1)}
        [ul] !{\\vcap[3]>\\khole}
        [rrr] !{\\ar @{-}@'{p-(0,1)@+}-(1,1)}
        }}}
    """
    class graph(SageObject):
        """
        LaTeX example for testing display of graphs.  See its string
        representation for details.

        EXAMPLES::

            sage: from sage.misc.latex import latex_examples
            sage: G = latex_examples.graph()
            sage: G
            LaTeX example for testing display of graphs...
        """
    class pstricks(SageObject):
        """
        LaTeX example for testing display of pstricks output.  See its
        string representation for details.

        EXAMPLES::

            sage: from sage.misc.latex import latex_examples
            sage: PS = latex_examples.pstricks()
            sage: PS
            LaTeX example for testing display of pstricks...
        """
    class knot(SageObject):
        """
        LaTeX example for testing display of knots.  See its string
        representation for details.

        EXAMPLES::

            sage: from sage.misc.latex import latex_examples
            sage: K = latex_examples.knot()
            sage: K
            LaTeX example for testing display of a knot...
        """
    class diagram(SageObject):
        """
        LaTeX example for testing display of commutative diagrams.
        See its string representation for details.

        EXAMPLES::

            sage: from sage.misc.latex import latex_examples
            sage: CD = latex_examples.diagram()
            sage: CD
            LaTeX example for testing display of a commutative diagram...
        """

latex_examples: Incomplete
