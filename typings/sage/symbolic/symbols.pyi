from _typeshed import Incomplete

symbol_table: Incomplete

def register_symbol(obj, conversions, nargs=None) -> None:
    """
    Add an object to the symbol table, along with how to convert it to
    other systems such as Maxima, Mathematica, etc.  This table is used
    to convert *from* other systems back to Sage.

    INPUT:

    - ``obj`` -- a symbolic object or function

    - ``conversions`` -- dictionary of conversions, where the keys
      are the names of interfaces (e.g., ``'maxima'``), and the values
      are the string representation of ``obj`` in that system

    - ``nargs`` -- (optional) number of arguments; for most functions,
      this can be deduced automatically

    EXAMPLES::

        sage: from sage.symbolic.symbols import register_symbol as rs
        sage: rs(SR(5), {'maxima': 'five'})                                             # needs sage.symbolic
        sage: SR(maxima_calculus('five'))                                               # needs sage.symbolic
        5
    """
