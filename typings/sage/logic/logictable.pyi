class Truthtable:
    """
    A truth table.

    INPUT:

    - ``t`` -- a 2-D array containing the table values

    - ``vo`` -- list of the variables in the expression in order,
      with each variable occurring only once
    """
    def __init__(self, t, vo) -> None:
        '''
        Initialize the data fields.

        EXAMPLES:

        This example illustrates the creation of a table

        ::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("a&b|~(c|a)")
            sage: s.truthtable()
            a      b      c      value
            False  False  False  True
            False  False  True   False
            False  True   False  True
            False  True   True   False
            True   False  False  False
            True   False  True   False
            True   True   False  True
            True   True   True   True
        '''
    def get_table_list(self):
        '''
        Return a list representation of the calling table object.

        OUTPUT: list representation of the table

        EXAMPLES:

        This example illustrates how to show the table as a list::

            sage: import sage.logic.propcalc as propcalc
            sage: s = propcalc.formula("man->monkey&human")
            sage: s.truthtable().get_table_list()
             [[\'man\', \'monkey\', \'human\'], [False, False, False, True], [False, False, True, True], [False, True, False, True], [False, True, True, True], [True, False, False, False], [True, False, True, False], [True, True, False, False], [True, True, True, True]]
        '''
