from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.sage_object import SageObject as SageObject

class table(SageObject):
    '''
    Display a rectangular array as a table, either in plain text, LaTeX,
    or html.

    INPUT:

    - ``rows`` -- (default: ``None``) list of lists (or list of tuples,
      etc.), containing the data to be displayed
    - ``columns`` -- (default: ``None``) list of lists (etc.), containing
      the data to be displayed, but stored as columns. Set either ``rows``
      or ``columns``, but not both.
    - ``header_row`` -- (default: ``False``) if ``True``, first row is
      highlighted
    - ``header_column`` -- (default: ``False``) if ``True``, first column is
      highlighted
    - ``frame`` -- (default: ``False``) if ``True``, put a box around each
      cell
    - ``align`` -- (default: ``\'left\'``) the alignment of each entry: either
      ``\'left\'``, ``\'center\'``, or ``\'right\'``

    EXAMPLES::

        sage: rows = [[\'a\', \'b\', \'c\'], [100,2,3], [4,5,60]]
        sage: table(rows)
          a     b   c
          100   2   3
          4     5   60
        sage: latex(table(rows))
        \\begin{tabular}{lll}
        a & b & c \\\\\n        $100$ & $2$ & $3$ \\\\\n        $4$ & $5$ & $60$ \\\\\n        \\end{tabular}

    If ``header_row`` is ``True``, then the first row is highlighted. If
    ``header_column`` is ``True``, then the first column is
    highlighted. If ``frame`` is ``True``, then print a box around every
    "cell". ::

        sage: table(rows, header_row=True)
            a     b   c
          ├─────┼───┼────┤
            100   2   3
            4     5   60
        sage: latex(table(rows, header_row=True))
        \\begin{tabular}{lll}
        a & b & c \\\\ \\hline
        $100$ & $2$ & $3$ \\\\\n        $4$ & $5$ & $60$ \\\\\n        \\end{tabular}
        sage: table(rows=rows, frame=True)
        ┌─────┬───┬────┐
        │ a   │ b │ c  │
        ├─────┼───┼────┤
        │ 100 │ 2 │ 3  │
        ├─────┼───┼────┤
        │ 4   │ 5 │ 60 │
        └─────┴───┴────┘
        sage: latex(table(rows=rows, frame=True))
        \\begin{tabular}{|l|l|l|} \\hline
        a & b & c \\\\ \\hline
        $100$ & $2$ & $3$ \\\\ \\hline
        $4$ & $5$ & $60$ \\\\ \\hline
        \\end{tabular}
        sage: table(rows, header_column=True, frame=True)
        ┌─────╥───┬────┐
        │ a   ║ b │ c  │
        ├─────╫───┼────┤
        │ 100 ║ 2 │ 3  │
        ├─────╫───┼────┤
        │ 4   ║ 5 │ 60 │
        └─────╨───┴────┘
        sage: latex(table(rows, header_row=True, frame=True))
        \\begin{tabular}{|l|l|l|} \\hline
        a & b & c \\\\ \\hline \\hline
        $100$ & $2$ & $3$ \\\\ \\hline
        $4$ & $5$ & $60$ \\\\ \\hline
        \\end{tabular}
        sage: table(rows, header_column=True)
          a   │ b   c
          100 │ 2   3
          4   │ 5   60

    The argument ``header_row`` can, instead of being ``True`` or
    ``False``, be the contents of the header row, so that ``rows``
    consists of the data, while ``header_row`` is the header
    information.  The same goes for ``header_column``. Passing lists
    for both arguments simultaneously is not supported. ::

        sage: table([(x,n(sin(x), digits=2)) for x in [0..3]],                          # needs sage.symbolic
        ....:       header_row=["$x$", r"$\\sin(x)$"], frame=True)
        ┌─────┬───────────┐
        │ $x$ │ $\\sin(x)$ │
        ╞═════╪═══════════╡
        │ 0   │ 0.00      │
        ├─────┼───────────┤
        │ 1   │ 0.84      │
        ├─────┼───────────┤
        │ 2   │ 0.91      │
        ├─────┼───────────┤
        │ 3   │ 0.14      │
        └─────┴───────────┘

    You can create the transpose of this table in several ways, for
    example, "by hand," that is, changing the data defining the table::

        sage: table(rows=[[x for x in [0..3]],                                          # needs sage.symbolic
        ....:             [n(sin(x), digits=2) for x in [0..3]]],
        ....:       header_column=[\'$x$\', r\'$\\sin(x)$\'], frame=True)
        ┌───────────╥──────┬──────┬──────┬──────┐
        │ $x$       ║ 0    │ 1    │ 2    │ 3    │
        ├───────────╫──────┼──────┼──────┼──────┤
        │ $\\sin(x)$ ║ 0.00 │ 0.84 │ 0.91 │ 0.14 │
        └───────────╨──────┴──────┴──────┴──────┘

    or by passing the original data as the ``columns`` of the table
    and using ``header_column`` instead of ``header_row``::

        sage: table(columns=[(x, n(sin(x), digits=2)) for x in [0..3]],                 # needs sage.symbolic
        ....:       header_column=[\'$x$\', r\'$\\sin(x)$\'], frame=True)
        ┌───────────╥──────┬──────┬──────┬──────┐
        │ $x$       ║ 0    │ 1    │ 2    │ 3    │
        ├───────────╫──────┼──────┼──────┼──────┤
        │ $\\sin(x)$ ║ 0.00 │ 0.84 │ 0.91 │ 0.14 │
        └───────────╨──────┴──────┴──────┴──────┘

    or by taking the :meth:`transpose` of the original table::

        sage: table(rows=[(x, n(sin(x), digits=2)) for x in [0..3]],                    # needs sage.symbolic
        ....:       header_row=[\'$x$\', r\'$\\sin(x)$\'], frame=True).transpose()
        ┌───────────╥──────┬──────┬──────┬──────┐
        │ $x$       ║ 0    │ 1    │ 2    │ 3    │
        ├───────────╫──────┼──────┼──────┼──────┤
        │ $\\sin(x)$ ║ 0.00 │ 0.84 │ 0.91 │ 0.14 │
        └───────────╨──────┴──────┴──────┴──────┘

    In either plain text or LaTeX, entries in tables can be aligned to the
    left (default), center, or right::

        sage: table(rows, align=\'left\')
          a     b   c
          100   2   3
          4     5   60
        sage: table(rows, align=\'center\')
          a    b   c
         100   2   3
          4    5   60
        sage: table(rows, align=\'right\', frame=True)
        ┌─────┬───┬────┐
        │   a │ b │  c │
        ├─────┼───┼────┤
        │ 100 │ 2 │  3 │
        ├─────┼───┼────┤
        │   4 │ 5 │ 60 │
        └─────┴───┴────┘

    To generate HTML you should use ``html(table(...))``::

        sage: # needs sage.symbolic
        sage: data = [["$x$", r"$\\sin(x)$"]] + [(x, n(sin(x), digits=2))
        ....:                                   for x in [0..3]]
        sage: output = html(table(data, header_row=True, frame=True))
        sage: type(output)
        <class \'sage.misc.html.HtmlFragment\'>
        sage: print(output)
        <div class="notruncate">
        <table border="1" class="table_form">
        <tbody>
        <tr>
        <th style="text-align:left">\\(x\\)</th>
        <th style="text-align:left">\\(\\sin(x)\\)</th>
        </tr>
        <tr class ="row-a">
        <td style="text-align:left">\\(0\\)</td>
        <td style="text-align:left">\\(0.00\\)</td>
        </tr>
        <tr class ="row-b">
        <td style="text-align:left">\\(1\\)</td>
        <td style="text-align:left">\\(0.84\\)</td>
        </tr>
        <tr class ="row-a">
        <td style="text-align:left">\\(2\\)</td>
        <td style="text-align:left">\\(0.91\\)</td>
        </tr>
        <tr class ="row-b">
        <td style="text-align:left">\\(3\\)</td>
        <td style="text-align:left">\\(0.14\\)</td>
        </tr>
        </tbody>
        </table>
        </div>

    It is an error to specify both ``rows`` and ``columns``::

        sage: table(rows=[[1,2,3], [4,5,6]], columns=[[0,0,0], [0,0,1024]])
        Traceback (most recent call last):
        ...
        ValueError: do not set both \'rows\' and \'columns\' when defining a table

        sage: table(columns=[[0,0,0], [0,0,1024]])
        0 0
        0 0
        0 1024

    Note that if ``rows`` is just a list or tuple, not nested, then
    it is treated as a single row::

        sage: table([1,2,3])
        1   2   3

    Also, if you pass a non-rectangular array, the longer rows or
    columns get truncated::

        sage: table([[1,2,3,7,12], [4,5]])
        1   2
        4   5
        sage: table(columns=[[1,2,3], [4,5,6,7]])
        1   4
        2   5
        3   6

    TESTS::

        sage: TestSuite(table([["$x$", r"$\\sin(x)$"]] +                                 # needs sage.symbolic
        ....:                  [(x, n(sin(x), digits=2)) for x in [0..3]],
        ....:                 header_row=True, frame=True)).run()

    .. automethod:: _rich_repr_
    '''
    def __init__(self, rows=None, columns=None, header_row: bool = False, header_column: bool = False, frame: bool = False, align: str = 'left') -> None:
        """
        EXAMPLES::

            sage: table([1,2,3], frame=True)
            ┌───┬───┬───┐
            │ 1 │ 2 │ 3 │
            └───┴───┴───┘
        """
    def __eq__(self, other):
        """
        Two tables are equal if and only if their data rowss and
        their options are the same.

        EXAMPLES::

            sage: # needs sage.modules sage.plot sage.symbolic
            sage: rows = [['a', 'b', 'c'], [1,plot(sin(x)),3], [4,5,identity_matrix(2)]]
            sage: T = table(rows, header_row=True)
            sage: T2 = table(rows, header_row=True)
            sage: T is T2
            False
            sage: T == T2
            True
            sage: T2.options(frame=True)
            sage: T == T2
            False
        """
    def options(self, **kwds):
        """
        With no arguments, return the dictionary of options for this
        table. With arguments, modify options.

        INPUT:

        - ``header_row`` -- if ``True``, first row is highlighted
        - ``header_column`` -- if ``True``, first column is highlighted
        - ``frame`` -- if ``True``, put a box around each cell
        - ``align`` -- the alignment of each entry: either ``'left'``,
          ``'center'``, or ``'right'``

        EXAMPLES::

            sage: T = table([['a', 'b', 'c'], [1,2,3]])
            sage: T.options()['align'], T.options()['frame']
            ('left', False)
            sage: T.options(align='right', frame=True)
            sage: T.options()['align'], T.options()['frame']
            ('right', True)

        Note that when first initializing a table, ``header_row`` or
        ``header_column`` can be a list. In this case, during the
        initialization process, the header is merged with the rest of
        the data, so changing the header option later using
        ``table.options(...)`` doesn't affect the contents of the
        table, just whether the row or column is highlighted. When
        using this :meth:`options` method, no merging of data occurs,
        so here ``header_row`` and ``header_column`` should just be
        ``True`` or ``False``, not a list. ::

            sage: T = table([[1,2,3], [4,5,6]], header_row=['a', 'b', 'c'], frame=True)
            sage: T
            ┌───┬───┬───┐
            │ a │ b │ c │
            ╞═══╪═══╪═══╡
            │ 1 │ 2 │ 3 │
            ├───┼───┼───┤
            │ 4 │ 5 │ 6 │
            └───┴───┴───┘
            sage: T.options(header_row=False)
            sage: T
            ┌───┬───┬───┐
            │ a │ b │ c │
            ├───┼───┼───┤
            │ 1 │ 2 │ 3 │
            ├───┼───┼───┤
            │ 4 │ 5 │ 6 │
            └───┴───┴───┘

        If you do specify a list for ``header_row``, an error is raised::

            sage: T.options(header_row=['x', 'y', 'z'])
            Traceback (most recent call last):
            ...
            TypeError: header_row should be either True or False.
        """
    def transpose(self):
        """
        Return a table which is the transpose of this one:
        rows and columns have been interchanged. Several of the
        properties of the original table are preserved: whether a
        frame is present and any alignment setting. On the other hand,
        header rows are converted to header columns, and vice versa.

        EXAMPLES::

            sage: T = table([[1,2,3], [4,5,6]])
            sage: T.transpose()
              1   4
              2   5
              3   6
            sage: T = table([[1,2,3], [4,5,6]], header_row=['x', 'y', 'z'], frame=True)
            sage: T.transpose()
            ┌───╥───┬───┐
            │ x ║ 1 │ 4 │
            ├───╫───┼───┤
            │ y ║ 2 │ 5 │
            ├───╫───┼───┤
            │ z ║ 3 │ 6 │
            └───╨───┴───┘
        """
