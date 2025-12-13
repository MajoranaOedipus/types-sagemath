from _typeshed import Incomplete

class TallListFormatter:
    """
    Special representation for lists with tall entries (e.g. matrices).

    .. automethod:: __call__
    """
    MAX_COLUMN: int
    def try_format(self, the_list):
        '''
        First check whether a list is "tall" -- whether the reprs of the
        elements of the list will span multiple lines and cause the list
        to be printed awkwardly.  If not, this function returns ``None`` and
        does nothing; you should revert back to the normal method for
        printing an object (its repr). If so, return the string in the
        special format. Note that the special format isn\'t just for
        matrices. Any object with a multiline repr will be formatted.

        INPUT:

        - ``the_list`` -- the list (or a tuple)

        OUTPUT:

        String or ``None``. The latter is returned if the list is not
        deemed to be tall enough and another formatter should be used.

        TESTS::

            sage: from sage.repl.display.util import format_list
            sage: print(format_list.try_format(                                         # needs sage.modules
            ....:        [matrix([[1, 2, 3, 4], [5, 6, 7, 8]]) for i in range(7)]))
            [
            [1 2 3 4]  [1 2 3 4]  [1 2 3 4]  [1 2 3 4]  [1 2 3 4]  [1 2 3 4]
            [5 6 7 8], [5 6 7 8], [5 6 7 8], [5 6 7 8], [5 6 7 8], [5 6 7 8],
            <BLANKLINE>
            [1 2 3 4]
            [5 6 7 8]
            ]

            sage: format_list.try_format([\'not\', \'tall\']) is None
            True
        '''
    def __call__(self, the_list):
        '''
        Return "tall list" string representation.

        See also :meth:`try_format`.

        INPUT:

        - ``the_list`` -- list or tuple

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.display.util import format_list
            sage: format_list([\'not\', \'tall\'])
            "[\'not\', \'tall\']"
        '''

format_list: Incomplete
