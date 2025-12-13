var_name: str

def variable_names(n, name=None):
    """
    Convert a root string into a tuple of variable names by adding
    numbers in sequence.

    INPUT:

    - ``n`` -- a nonnegative Integer; the number of variable names to
      output
    - ``names`` a string (default: ``None``); the root of the variable
      name

    EXAMPLES::

        sage: from sage.misc.defaults import variable_names
        sage: variable_names(0)
        ()
        sage: variable_names(1)
        ('x',)
        sage: variable_names(1,'alpha')
        ('alpha',)
        sage: variable_names(2,'alpha')
        ('alpha0', 'alpha1')
    """
def latex_variable_names(n, name=None):
    """
    Convert a root string into a tuple of variable names by adding
    numbers in sequence.

    INPUT:

    - ``n`` -- a nonnegative Integer; the number of variable names to
      output
    - ``names`` a string (default: ``None``); the root of the variable
      name

    EXAMPLES::

        sage: from sage.misc.defaults import latex_variable_names
        sage: latex_variable_names(0)
        ()
        sage: latex_variable_names(1,'a')
        ('a',)
        sage: latex_variable_names(3,beta)
        ('beta_{0}', 'beta_{1}', 'beta_{2}')
        sage: latex_variable_names(3,r'\\beta')
        ('\\\\beta_{0}', '\\\\beta_{1}', '\\\\beta_{2}')
    """
def set_default_variable_name(name, separator: str = '') -> None:
    """
    Change the default variable name and separator.
    """

series_prec: int

def series_precision():
    """
    Return the Sage-wide precision for series (symbolic,
    power series, Laurent series).

    EXAMPLES::

        sage: series_precision()
        20
    """
def set_series_precision(prec) -> None:
    """
    Change the Sage-wide precision for series (symbolic,
    power series, Laurent series).

    EXAMPLES::

        sage: set_series_precision(5)
        sage: series_precision()
        5
        sage: set_series_precision(20)
    """
