from sage.misc.latex import LatexExpr as LatexExpr
from sage.structure.sage_object import SageObject as SageObject

def is_atomic(expr, sep=['+', '-']):
    '''
    Helper function to check whether some LaTeX expression is atomic.

    Adapted from method
    :meth:`~sage.tensor.differential_form_element.DifferentialFormFormatter._is_atomic`
    of class
    :class:`~sage.tensor.differential_form_element.DifferentialFormFormatter`
    written by Joris Vankerschaver (2010) and modified by Michael Jung (2020).

    INPUT:

    - ``expr`` -- string representing the expression (e.g. LaTeX string)
    - ``sep`` -- (default: ``[\'+\', \'-\']``) a list of strings representing the
      operations (e.g. LaTeX strings)

    OUTPUT:

    - ``True`` if the operations are enclosed in parentheses and
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import is_atomic
        sage: is_atomic("2*x")
        True
        sage: is_atomic("2+x")
        False
        sage: is_atomic("(2+x)")
        True

    Moreover the separator can be changed::

        sage: is_atomic("a*b", sep=[\'*\'])
        False
        sage: is_atomic("(a*b)", sep=[\'*\'])
        True
        sage: is_atomic("a mod b", sep=[\'mod\'])
        False
        sage: is_atomic("(a mod b)", sep=[\'mod\'])
        True
    '''
def is_atomic_wedge_txt(expression):
    '''
    Helper function to check whether some text-formatted expression is atomic
    in terms of wedge products.

    Adapted from method
    :meth:`~sage.tensor.differential_form_element.DifferentialFormFormatter._is_atomic`
    of class
    :class:`~sage.tensor.differential_form_element.DifferentialFormFormatter`
    written by Joris Vankerschaver (2010) and modified by Michael Jung (2020).

    INPUT:

    - ``expression`` -- string representing the text-formatted expression

    OUTPUT:

    - ``True`` if wedge products are enclosed in parentheses and
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import is_atomic_wedge_txt
        sage: is_atomic_wedge_txt("a")
        True
        sage: is_atomic_wedge_txt(r"a∧b")
        False
        sage: is_atomic_wedge_txt(r"(a∧b)")
        True
        sage: is_atomic_wedge_txt(r"(a∧b)∧c")
        False
        sage: is_atomic_wedge_txt(r"(a∧b∧c)")
        True
    '''
def is_atomic_wedge_latex(expression):
    '''
    Helper function to check whether LaTeX-formatted expression is atomic in
    terms of wedge products.

    Adapted from method
    :meth:`~sage.tensor.differential_form_element.DifferentialFormFormatter._is_atomic`
    of class
    :class:`~sage.tensor.differential_form_element.DifferentialFormFormatter`
    written by Joris Vankerschaver (2010) and modified by Michael Jung (2020).

    INPUT:

    - ``expression`` -- string representing the LaTeX expression

    OUTPUT:

    - ``True`` if wedge products are enclosed in parentheses and
      ``False`` otherwise.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import is_atomic_wedge_latex
        sage: is_atomic_wedge_latex(r"a")
        True
        sage: is_atomic_wedge_latex(r"a\\wedge b")
        False
        sage: is_atomic_wedge_latex(r"(a\\wedge b)")
        True
        sage: is_atomic_wedge_latex(r"(a\\wedge b)\\wedge c")
        False
        sage: is_atomic_wedge_latex(r"((a\\wedge b)\\wedge c)")
        True
        sage: is_atomic_wedge_latex(r"(a\\wedge b\\wedge c)")
        True
        sage: is_atomic_wedge_latex(r"\\omega\\wedge\\theta")
        False
        sage: is_atomic_wedge_latex(r"(\\omega\\wedge\\theta)")
        True
        sage: is_atomic_wedge_latex(r"\\omega\\wedge(\\theta+a)")
        False
    '''
def format_mul_txt(name1, operator, name2):
    """
    Helper function for text-formatted names of results of multiplication or
    tensor product.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import format_mul_txt
        sage: format_mul_txt('a', '*', 'b')
        'a*b'
        sage: format_mul_txt('a+b', '*', 'c')
        '(a+b)*c'
        sage: format_mul_txt('a', '*', 'b+c')
        'a*(b+c)'
        sage: format_mul_txt('a+b', '*', 'c+d')
        '(a+b)*(c+d)'
        sage: format_mul_txt(None, '*', 'b')
        sage: format_mul_txt('a', '*', None)
    """
def format_mul_latex(name1, operator, name2):
    """
    Helper function for LaTeX names of results of multiplication or tensor
    product.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import format_mul_latex
        sage: format_mul_latex('a', '*', 'b')
        'a*b'
        sage: format_mul_latex('a+b', '*', 'c')
        '\\\\left(a+b\\\\right)*c'
        sage: format_mul_latex('a', '*', 'b+c')
        'a*\\\\left(b+c\\\\right)'
        sage: format_mul_latex('a+b', '*', 'c+d')
        '\\\\left(a+b\\\\right)*\\\\left(c+d\\\\right)'
        sage: format_mul_latex(None, '*', 'b')
        sage: format_mul_latex('a', '*', None)
    """
def format_unop_txt(operator, name):
    """
    Helper function for text-formatted names of results of unary operator.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import format_unop_txt
        sage: format_unop_txt('-', 'a')
        '-a'
        sage: format_unop_txt('-', 'a+b')
        '-(a+b)'
        sage: format_unop_txt('-', '(a+b)')
        '-(a+b)'
        sage: format_unop_txt('-', None)
    """
def format_unop_latex(operator, name):
    """
    Helper function for LaTeX names of results of unary operator.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import format_unop_latex
        sage: format_unop_latex('-', 'a')
        '-a'
        sage: format_unop_latex('-', 'a+b')
        '-\\\\left(a+b\\\\right)'
        sage: format_unop_latex('-', '(a+b)')
        '-(a+b)'
        sage: format_unop_latex('-', None)
    """

class FormattedExpansion(SageObject):
    """
    Helper class for displaying tensor expansions.

    EXAMPLES::

        sage: from sage.tensor.modules.format_utilities import FormattedExpansion
        sage: f = FormattedExpansion('v', r'\\tilde v')
        sage: f
        v
        sage: latex(f)
        \\tilde v
        sage: f = FormattedExpansion('x/2', r'\\frac{x}{2}')
        sage: f
        x/2
        sage: latex(f)
        \\frac{x}{2}
    """
    def __init__(self, txt=None, latex=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.format_utilities import FormattedExpansion
            sage: f = FormattedExpansion('v', r'\\tilde v')
            sage: f
            v
        """
