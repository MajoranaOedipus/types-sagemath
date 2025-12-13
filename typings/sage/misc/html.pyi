from _typeshed import Incomplete
from sage.misc.latex import latex as latex
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.structure.sage_object import SageObject as SageObject

macro_regex: Incomplete

class HtmlFragment(str, SageObject):
    """
    A HTML fragment.

    This is a piece of HTML, usually not a complete document.  For
    example, just a ``<div>...</div>`` piece and not the entire
    ``<html>...</html>``.

    EXAMPLES::

        sage: from sage.misc.html import HtmlFragment
        sage: HtmlFragment('<b>test</b>')
        <b>test</b>

    .. automethod:: _rich_repr_
    """

def math_parse(s):
    """
    Transform the string ``s`` with TeX maths to an HTML string renderable by
    MathJax.

    INPUT:

    - ``s`` -- string

    OUTPUT: :class:`HtmlFragment`

    Specifically this method does the following:

    * Replace all ``\\$text\\$``\\'s by ``\\(text\\)``
    * Replace all ``\\$\\$text\\$\\$``\\'s by ``\\[text\\]``
    * Replace all ``\\\\\\$``\\'s by ``\\$``\\'s. Note that this has precedence over
      the above two cases.

    EXAMPLES::

        sage: print(sage.misc.html.math_parse('This is $2+2$.'))
        This is \\(2+2\\).
        sage: print(sage.misc.html.math_parse('This is $$2+2$$.'))
        This is \\[2+2\\].
        sage: print(sage.misc.html.math_parse('This is \\\\[2+2\\\\].'))
        This is \\[2+2\\].
        sage: print(sage.misc.html.math_parse(r'\\$2+2\\$ is rendered to $2+2$.'))
        <span>$</span>2+2<span>$</span> is rendered to \\(2+2\\).
    """

class MathJaxExpr:
    '''
    An arbitrary MathJax expression that can be nicely concatenated.

    EXAMPLES::

        sage: from sage.misc.html import MathJaxExpr
        sage: MathJaxExpr("a^{2}") + MathJaxExpr("x^{-1}")
        a^{2}x^{-1}
    '''
    def __init__(self, y) -> None:
        """
        Initialize a MathJax expression.

        INPUT:

        - ``y`` -- string

        Note that no error checking is done on the type of ``y``.

        EXAMPLES::

            sage: from sage.misc.html import MathJaxExpr
            sage: jax = MathJaxExpr(3); jax  # indirect doctest
            3
            sage: TestSuite(jax).run(skip ='_test_pickling')
        """
    def __add__(self, y):
        """
        'Add' MathJaxExpr ``self`` to ``y``.  This concatenates them
        (assuming that they're strings).

        EXAMPLES::

            sage: from sage.misc.html import MathJaxExpr
            sage: j3 = MathJaxExpr('3')
            sage: jx = MathJaxExpr('x')
            sage: j3 + jx
            3x
        """
    def __radd__(self, y):
        """
        'Add' MathJaxExpr ``y`` to ``self``.  This concatenates them
        (assuming that they're strings).

        EXAMPLES::

            sage: from sage.misc.html import MathJaxExpr
            sage: j3 = MathJaxExpr('3')
            sage: jx = MathJaxExpr('x')
            sage: j3.__radd__(jx)
            x3
        """

class MathJax:
    """
    Render LaTeX input using MathJax.  This returns a :class:`MathJaxExpr`.

    EXAMPLES::

        sage: from sage.misc.html import MathJax
        sage: MathJax()(3)
        <html>\\[3\\]</html>
        sage: MathJax()(ZZ)
        <html>\\[\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\Bold{Z}\\]</html>
    """
    def __call__(self, x, combine_all: bool = False):
        """
        Render LaTeX input using MathJax.  This returns a :class:`MathJaxExpr`.

        INPUT:

        - ``x`` -- a Sage object

        - ``combine_all`` -- boolean (default: ``False``); if ``combine_all``
          is ``True`` and the input is a tuple, then it does not return a tuple
          and instead returns a string with all the elements separated by
          a single space

        OUTPUT: :class:`MathJaxExpr`

        EXAMPLES::

            sage: from sage.misc.html import MathJax
            sage: MathJax()(3)
            <html>\\[3\\]</html>
            sage: str(MathJax().eval(ZZ['x'], mode='display')) == str(MathJax()(ZZ['x']))
            True
        """
    def eval(self, x, globals=None, locals=None, mode: str = 'display', combine_all: bool = False):
        """
        Render LaTeX input using MathJax.  This returns a :class:`MathJaxExpr`.

        INPUT:

        - ``x`` -- a Sage object

        - ``globals`` -- a globals dictionary

        - ``locals`` -- extra local variables used when
          evaluating Sage code in ``x``

        - ``mode`` -- string (default: ``'display'``);
          ``'display'`` for displaymath, ``'inline'`` for inline
          math, or ``'plain'`` for just the LaTeX code without the
          surrounding html and script tags

        - ``combine_all`` -- boolean (default: ``False``); if ``combine_all``
          is ``True`` and the input is a tuple, then it does not return a tuple
          and instead returns a string with all the elements separated by
          a single space

        OUTPUT: :class:`MathJaxExpr`

        EXAMPLES::

            sage: from sage.misc.html import MathJax
            sage: MathJax().eval(3, mode='display')
            <html>\\[3\\]</html>
            sage: MathJax().eval(3, mode='inline')
            <html>\\(3\\)</html>
            sage: MathJax().eval(type(3), mode='inline')
            <html>\\(\\verb|&lt;class|\\verb| |\\verb|'sage.rings.integer.Integer'>|\\)</html>

        TESTS:

            sage: from sage.misc.html import MathJax
            sage: MathJax().eval(IntegerModRing(6))
            <html>\\[\\newcommand{\\ZZ}{\\Bold{Z}}\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\ZZ/6\\ZZ\\]</html>
        """

class HTMLFragmentFactory(SageObject):
    def __call__(self, obj, concatenate: bool = True, strict: bool = False):
        '''
        Construct a HTML fragment.

        INPUT:

        - ``obj`` -- anything. An object for which you want an HTML
          representation

        - ``concatenate`` -- if ``True``, combine HTML representations of
          elements of the container ``obj``

        - ``strict`` -- if ``True``, construct an HTML representation of
          ``obj`` even if ``obj`` is a string

        OUTPUT: :class:`HtmlFragment`

        EXAMPLES::

            sage: h = html(\'<hr>\');  pretty_print(h)
            <hr>
            sage: type(h)
            <class \'sage.misc.html.HtmlFragment\'>

            sage: html(1/2)
            <html>\\(\\displaystyle \\frac{1}{2}\\)</html>

            sage: html(\'<a href="http://sagemath.org">sagemath</a>\')
            <a href="http://sagemath.org">sagemath</a>

            sage: html(\'<a href="http://sagemath.org">sagemath</a>\', strict=True)
            <html>\\(\\displaystyle \\verb|&lt;a|\\verb| |\\verb|href="http://sagemath.org">sagemath&lt;/a>|\\)</html>

        Display preference ``align_latex`` affects rendering of LaTeX expressions::

            sage: from sage.repl.rich_output.display_manager import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.preferences.align_latex = \'left\'
            sage: html(1/2)
            <html>\\(\\displaystyle \\frac{1}{2}\\)</html>
            sage: dm.preferences.align_latex = \'center\'
            sage: html(1/2)
            <html>\\[\\frac{1}{2}\\]</html>
            sage: dm.preferences.align_latex = None  # same with left
            sage: html(1/2)
            <html>\\(\\displaystyle \\frac{1}{2}\\)</html>
        '''
    def eval(self, s, locals=None):
        """
        Evaluate embedded <sage> tags.

        INPUT:

        - ``s`` -- string

        - ``globals`` -- dictionary; the global variables when
          evaluating ``s``. Default: the current global variables.

        OUTPUT: :class:`HtmlFragment`

        EXAMPLES::

            sage: a = 123
            sage: html.eval('<sage>a</sage>')
            \\(123\\)
            sage: html.eval('<sage>a</sage>', locals={'a': 456})
            \\(456\\)
        """
    def iframe(self, url, height: int = 400, width: int = 800):
        '''
        Generate an iframe HTML fragment.

        INPUT:

        - ``url`` -- string; a url, either with or without URI scheme
          (defaults to "http"), or an absolute file path

        - ``height`` -- the number of pixels for the page height
          Defaults to 400

        - ``width`` -- the number of pixels for the page width
          Defaults to 800

        OUTPUT: :class:`HtmlFragment`

        EXAMPLES::

            sage: pretty_print(html.iframe("sagemath.org"))
            <iframe height="400" width="800"
            src="http://sagemath.org"></iframe>
            sage: pretty_print(html.iframe("http://sagemath.org",30,40))
            <iframe height="30" width="40"
            src="http://sagemath.org"></iframe>
            sage: pretty_print(html.iframe("https://sagemath.org",30))
            <iframe height="30" width="800"
            src="https://sagemath.org"></iframe>
            sage: pretty_print(html.iframe("/home/admin/0/data/filename"))
            <iframe height="400" width="800"
            src="file:///home/admin/0/data/filename"></iframe>
            sage: pretty_print(html.iframe(\'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA\'
            ....: \'AUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBA\'
            ....: \'AO9TXL0Y4OHwAAAABJRU5ErkJggg=="\'))
            <iframe height="400" width="800"
            src="http://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==""></iframe>
        '''

html: Incomplete

def pretty_print_default(enable: bool = True) -> None:
    """
    Enable or disable default pretty printing.

    Pretty printing means rendering things in HTML and by MathJax so that a
    browser-based frontend can render real math.

    This function is pretty useless without the notebook, it should not
    be in the global namespace.

    INPUT:

    - ``enable`` -- boolean (default: ``True``);  if ``True``, turn on
      pretty printing. If ``False``, turn it off.

    EXAMPLES::

        sage: pretty_print_default(True)
        sage: 'foo'  # the doctest backend does not support html
        'foo'
        sage: pretty_print_default(False)
        sage: 'foo'
        'foo'
    """
