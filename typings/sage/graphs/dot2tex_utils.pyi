from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.latex import latex as latex

@cached_function
def have_dot2tex() -> bool:
    """
    Return whether ``dot2tex`` >= 2.8.7 and graphviz are installed
    and functional.

    EXAMPLES::

        sage: sage.graphs.dot2tex_utils.have_dot2tex()  # optional - dot2tex graphviz
        True
        sage: sage.graphs.dot2tex_utils.have_dot2tex() in [True, False]
        True
    """
def assert_have_dot2tex() -> None:
    """
    Test whether ``dot2tex`` >= 2.8.7 and graphviz are installed and
    functional, and raises an error otherwise.

    EXAMPLES::

        sage: sage.graphs.dot2tex_utils.assert_have_dot2tex()  # optional - dot2tex graphviz
    """
def quoted_latex(x):
    """
    Strips the latex representation of ``x`` to make it suitable for a
    ``dot2tex`` string.

    EXAMPLES::

        sage: sage.graphs.dot2tex_utils.quoted_latex(matrix([[1,1],[0,1],[0,0]]))       # needs sage.modules
        '\\left(\\begin{array}{rr}1 & 1 \\\\0 & 1 \\\\0 & 0\\end{array}\\right)'
    """
def quoted_str(x):
    """
    Strip the string representation of ``x`` to make it suitable for
    a ``dot2tex`` string, and especially a node label.

    Indeed, ``dot2tex`` gets confused by newlines, and braces.

    EXAMPLES::

        sage: sage.graphs.dot2tex_utils.quoted_str(matrix([[1,1],[0,1],[0,0]]))         # needs sage.modules
        '[1 1]\\\\n\\\\\\n[0 1]\\\\n\\\\\\n[0 0]'
        sage: print(sage.graphs.dot2tex_utils.quoted_str(matrix([[1,1],[0,1],[0,0]])))  # needs sage.modules
        [1 1]\\n\\\n        [0 1]\\n\\\n        [0 0]
    """
