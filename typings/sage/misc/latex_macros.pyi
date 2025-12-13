from _typeshed import Incomplete

def produce_latex_macro(name, *sample_args):
    '''
    Produce a string defining a LaTeX macro.

    INPUT:

    - ``name`` -- name of macro to be defined, also name of corresponding Sage object

    - ``sample_args`` -- (optional) sample arguments for this Sage object

    EXAMPLES::

        sage: from sage.misc.latex_macros import produce_latex_macro
        sage: produce_latex_macro(\'ZZ\')
        \'\\\\newcommand{\\\\ZZ}{\\\\Bold{Z}}\'

    If the Sage object takes arguments, then the LaTeX macro will
    accept arguments as well. You must pass valid arguments, which
    will then be converted to #1, #2, etc. in the macro
    definition. The following allows the use of "\\GF{p^n}", for
    example::

         sage: produce_latex_macro(\'GF\', 37)
         \'\\\\newcommand{\\\\GF}[1]{\\\\Bold{F}_{#1}}\'

    If the Sage object is not in the global namespace, describe it
    like so::

         sage: produce_latex_macro(\'sage.rings.finite_rings.finite_field_constructor.FiniteField\', 3)
         \'\\\\newcommand{\\\\FiniteField}[1]{\\\\Bold{F}_{#1}}\'
    '''
def convert_latex_macro_to_mathjax(macro):
    """
    This converts a LaTeX macro definition (\\newcommand...) to a
    MathJax macro definition (MathJax.Macro...).

    INPUT:

    - ``macro`` -- LaTeX macro definition

    See the web page
    https://docs.mathjax.org/en/latest/input/tex/macros.html for a
    description of the format for MathJax macros.

    EXAMPLES::

        sage: from sage.misc.latex_macros import convert_latex_macro_to_mathjax
        sage: convert_latex_macro_to_mathjax('\\\\newcommand{\\\\ZZ}{\\\\Bold{Z}}')
        ('ZZ', '\\\\Bold{Z}')
        sage: convert_latex_macro_to_mathjax('\\\\newcommand{\\\\GF}[1]{\\\\Bold{F}_{#1}}')
        ('GF', ['\\\\Bold{F}_{#1}', 1])
    """

macros: Incomplete
latex_macros: Incomplete
sage_configurable_latex_macros: Incomplete

def sage_latex_macros():
    """
    Return list of LaTeX macros for Sage. This just runs the function
    :func:`produce_latex_macro` on the list ``macros`` defined in this
    file, and appends ``sage_configurable_latex_macros``. To add a new
    macro for permanent use in Sage, modify ``macros``.

    EXAMPLES::

        sage: from sage.misc.latex_macros import sage_latex_macros
        sage: sage_latex_macros()
        ['\\\\newcommand{\\\\ZZ}{\\\\Bold{Z}}', '\\\\newcommand{\\\\NN}{\\\\Bold{N}}', ...
    """
def sage_mathjax_macros():
    """
    Return Sage's macro definitions for usage with MathJax.

    This feeds each item output by :func:`sage_latex_macros` to
    :func:`convert_latex_macro_to_mathjax`.

    EXAMPLES::

        sage: from sage.misc.latex_macros import sage_mathjax_macros
        sage: sage_mathjax_macros()
        {'Bold': ['\\\\mathbf{#1}', 1], 'CC': '\\\\Bold{C}', ...
    """
