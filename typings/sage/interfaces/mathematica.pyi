from _typeshed import Incomplete
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.richcmp import rich_to_bool as rich_to_bool

def clean_output(s): ...

class Mathematica(ExtraTabCompletion, Expect):
    """
    Interface to the Mathematica interpreter.
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, command=None, verbose_start: bool = False) -> None:
        '''
        TESTS:

        Test that :issue:`28075` is fixed::

            sage: repr(mathematica.eval("Print[1]; Print[2]; Print[3]"))  # optional - mathematica
            \'1\\n2\\n3\'
        '''
    def eval(self, code, strip: bool = True, **kwds): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var, ascii_art: bool = False):
        """
        Get the value of the variable var.

        AUTHORS:

        - William Stein

        - Kiran Kedlaya (2006-02-04): suggested using InputForm
        """
    def chdir(self, dir) -> None:
        '''
        Change Mathematica\'s current working directory.

        EXAMPLES::

            sage: mathematica.chdir(\'/\')          # optional - mathematica
            sage: mathematica(\'Directory[]\')      # optional - mathematica
            "/"
        '''
    def console(self, readline: bool = True) -> None: ...
    def help(self, cmd): ...
    def __getattr__(self, attrname): ...

class MathematicaElement(ExpectElement):
    def __getitem__(self, n): ...
    def __getattr__(self, attrname): ...
    def __float__(self, precision: int = 16) -> float: ...
    def __reduce__(self): ...
    def __len__(self) -> int:
        """
        Return the object's length, evaluated by mathematica.

        EXAMPLES::

            sage: len(mathematica([1,1.,2]))    # optional - mathematica
            3

        AUTHORS:
        - Felix Lawrence (2009-08-21)
        """
    def save_image(self, filename, ImageSize: int = 600) -> None:
        """
        Save a mathematica graphics.

        INPUT:

        - ``filename`` -- string; the filename to save as. The
          extension determines the image file format

        - ``ImageSize`` -- integer; the size of the resulting image

        EXAMPLES::

            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: filename = tmp_filename()                      # optional - mathematica
            sage: P.save_image(filename, ImageSize=800)                # optional - mathematica
        """
    def show(self, ImageSize: int = 600) -> None:
        """
        Show a mathematica expression immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        INPUT:

        - ``ImageSize`` -- integer; the size of the resulting image

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES::

            sage: Q = mathematica('Sin[x Cos[y]]/Sqrt[1-x^2]')   # optional - mathematica
            sage: show(Q)                                        # optional - mathematica
            Sin[x*Cos[y]]/Sqrt[1 - x^2]

        The following example starts a Mathematica frontend to do the rendering
        (:issue:`28819`)::

            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: show(P)                                        # optional - mathematica mathematicafrontend
            sage: P.show(ImageSize=800)                          # optional - mathematica mathematicafrontend
        """
    def str(self): ...
    def __bool__(self) -> bool:
        """
        Return whether this Mathematica element is not identical to ``False``.

        EXAMPLES::

            sage: bool(mathematica(True))  # optional - mathematica
            True
            sage: bool(mathematica(False))  # optional - mathematica
            False

        In Mathematica, `0` cannot be used to express falsity::

            sage: bool(mathematica(0))  # optional - mathematica
            True
        """
    def n(self, *args, **kwargs):
        """
        Numerical approximation by converting to Sage object first.

        Convert the object into a Sage object and return its numerical
        approximation. See documentation of the function
        :func:`sage.misc.functional.n` for details.

        EXAMPLES::

            sage: mathematica('Pi').n(10)    # optional -- mathematica
            3.1
            sage: mathematica('Pi').n()      # optional -- mathematica
            3.14159265358979
            sage: mathematica('Pi').n(digits=10)   # optional -- mathematica
            3.141592654
        """

class MathematicaFunction(ExpectFunction): ...
class MathematicaFunctionElement(FunctionElement): ...

mathematica: Incomplete

def reduce_load(X): ...
def mathematica_console(readline: bool = True) -> None: ...
def request_wolfram_alpha(input, verbose: bool = False):
    """
    Request Wolfram Alpha website.

    INPUT:

    - ``input`` -- string
    - ``verbose`` -- boolean (default: ``False``)

    OUTPUT: json

    EXAMPLES::

        sage: from sage.interfaces.mathematica import request_wolfram_alpha
        sage: page_data = request_wolfram_alpha('integrate Sin[x]')      # optional internet
        sage: [str(a) for a in sorted(page_data.keys())]                 # optional internet
        ['queryresult']
        sage: [str(a) for a in sorted(page_data['queryresult'].keys())]  # optional internet
        ['datatypes',
         'encryptedEvaluatedExpression',
         'encryptedParsedExpression',
         'error',
         'host',
         'id',
         'inputstring',
         'numpods',
         'parsetimedout',
         'parsetiming',
         'pods',
         'recalculate',
         'related',
         'server',
         'sponsorCategories',
         'success',
         'timedout',
         'timedoutpods',
         'timing',
         'version']
    """
def parse_moutput_from_json(page_data, verbose: bool = False):
    """
    Return the list of outputs found in the json (with key ``'moutput'``).

    INPUT:

    - ``page_data`` -- json obtained from Wolfram Alpha
    - ``verbose`` -- boolean (default: ``False``)

    OUTPUT: list of unicode strings

    EXAMPLES::

        sage: from sage.interfaces.mathematica import request_wolfram_alpha
        sage: from sage.interfaces.mathematica import parse_moutput_from_json
        sage: page_data = request_wolfram_alpha('integrate Sin[x]') # optional internet
        sage: parse_moutput_from_json(page_data)                    # optional internet
        ['-Cos[x]']

    ::

        sage: page_data = request_wolfram_alpha('Sin[x]')           # optional internet
        sage: L = parse_moutput_from_json(page_data)                # optional internet
        sage: sorted(L)                                             # optional internet
        ['-Cos[x]', '{x == 0}', '{x == Pi C[1], Element[C[1], Integers]}']

    TESTS::

        sage: page_data = request_wolfram_alpha('Integrate(Sin[z], y)')  # optional internet
        sage: parse_moutput_from_json(page_data)                         # optional internet
        Traceback (most recent call last):
        ...
        ValueError: asking wolframalpha.com was not successful
    """
def symbolic_expression_from_mathematica_string(mexpr):
    """
    Translate a mathematica string into a symbolic expression.

    INPUT:

    - ``mexpr`` -- string

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.mathematica import symbolic_expression_from_mathematica_string
        sage: symbolic_expression_from_mathematica_string('-Cos[x]')
        -cos(x)
    """
