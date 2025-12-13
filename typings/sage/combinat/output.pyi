from _typeshed import Incomplete
from sage.combinat.tableau import Tableaux as Tableaux

lr_macro: Incomplete

def tex_from_array(array, with_lines: bool = True) -> str:
    '''
    Return a latex string for a two dimensional array of partition, composition
    or skew composition shape.

    INPUT:

    - ``array`` -- list of list
    - ``with_lines`` -- boolean (default: ``True``); whether to draw a line to
      separate the entries in the array

    Empty rows are allowed; however, such rows should be given as
    ``[None]`` rather than ``[]``.

    The array is drawn using either the English or French convention
    following :meth:`Tableaux.options`.

    .. SEEALSO:: :meth:`tex_from_array_tuple`

    EXAMPLES::

        sage: from sage.combinat.output import tex_from_array
        sage: print(tex_from_array([[1,2,3],[4,5]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\cline{1-3}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-3}
        \\lr{4}&\\lr{5}\\\\\\cline{1-2}
        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\lr{4}&\\lr{5}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\cline{1-3}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-4}
        \\lr{4}&\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{1-4}
        \\lr{8}\\\\\\cline{1-1}
        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\lr{4}&\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        \\lr{8}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\cline{3-3}
        &&\\lr{3}\\\\\\cline{2-4}
        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{1-4}
        \\lr{8}\\\\\\cline{1-1}
        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\cline{3-3}
        &&\\lr{3}\\\\\\cline{2-4}
        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{2-4}
        &\\lr{8}\\\\\\cline{2-2}
        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\\\\n        &&\\lr{3}\\\\\n        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        \\lr{8}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\\\\n        &&\\lr{3}\\\\\n        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        &\\lr{8}\\\\\n        \\end{array}$}
        }
        sage: Tableaux.options.convention="french"
        sage: print(tex_from_array([[1,2,3],[4,5]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\cline{1-2}
        \\lr{4}&\\lr{5}\\\\\\cline{1-3}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-3}
        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{4}&\\lr{5}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\cline{1-1}
        \\lr{8}\\\\\\cline{1-4}
        \\lr{4}&\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{1-4}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-3}
        \\end{array}$}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\\\\n        \\lr{8}\\\\\n        \\lr{4}&\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\cline{1-1}
        \\lr{8}\\\\\\cline{1-4}
        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{2-4}
        &&\\lr{3}\\\\\\cline{3-3}
        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\cline{2-2}
        &\\lr{8}\\\\\\cline{2-4}
        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\\cline{2-4}
        &&\\lr{3}\\\\\\cline{3-3}
        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\\\\n        \\lr{8}\\\\\n        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        &&\\lr{3}\\\\\n        \\end{array}$}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{4}c}\\\\\n        &\\lr{8}\\\\\n        &\\lr{5}&\\lr{6}&\\lr{7}\\\\\n        &&\\lr{3}\\\\\n        \\end{array}$}
        }
        sage: Tableaux.options.convention="russian"
        sage: print(tex_from_array([[1,2,3],[4,5]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\cline{1-2}
        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}\\\\\\cline{1-3}
        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\\cline{1-3}
        \\end{array}$}}
        }
        sage: print(tex_from_array([[1,2,3],[4,5]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}\\\\\n        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\n        \\end{array}$}}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\cline{1-1}
        \\lr{\\rotatebox{-45}{8}}\\\\\\cline{1-4}
        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\\cline{1-4}
        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\\cline{1-3}
        \\end{array}$}}
        }
        sage: print(tex_from_array([[1,2,3],[4,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\\\\n        \\lr{\\rotatebox{-45}{8}}\\\\\n        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\n        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\n        \\end{array}$}}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\cline{1-1}
        \\lr{\\rotatebox{-45}{8}}\\\\\\cline{1-4}
        &\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\\cline{2-4}
        &&\\lr{\\rotatebox{-45}{3}}\\\\\\cline{3-3}
        \\end{array}$}}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\cline{2-2}
        &\\lr{\\rotatebox{-45}{8}}\\\\\\cline{2-4}
        &\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\\cline{2-4}
        &&\\lr{\\rotatebox{-45}{3}}\\\\\\cline{3-3}
        \\end{array}$}}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\\\\n        \\lr{\\rotatebox{-45}{8}}\\\\\n        &\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\n        &&\\lr{\\rotatebox{-45}{3}}\\\\\n        \\end{array}$}}
        }
        sage: print(tex_from_array([[None,None,3],[None,5,6,7],[None,8]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{4}c}\\\\\n        &\\lr{\\rotatebox{-45}{8}}\\\\\n        &\\lr{\\rotatebox{-45}{5}}&\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\n        &&\\lr{\\rotatebox{-45}{3}}\\\\\n        \\end{array}$}}
        }

        sage: Tableaux.options._reset()
    '''
def svg_from_array(array, with_lines: bool = True) -> str:
    '''
    Return the svg code for this array.

    EXAMPLES::

        sage: array=[[1,9,1],[6,9,1],[2,8,3,3]]
        sage: sage.combinat.output.svg_from_array(array)
        \'<?xml version="1.0" ...</svg>\'
    '''
def tex_from_array_tuple(a_tuple, with_lines: bool = True) -> str:
    '''
    Return a latex string for a tuple of two dimensional array of partition,
    composition or skew composition shape.

    INPUT:

    - ``a_tuple`` -- tuple of lists of lists
    - ``with_lines`` -- boolean (default: ``True``); whether to draw lines to
      separate the entries in the components of ``a_tuple``

    .. SEEALSO:: :meth:`tex_from_array` for the description of each array

    EXAMPLES::

        sage: from sage.combinat.output import tex_from_array_tuple
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\cline{1-3}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-3}
        \\lr{4}&\\lr{5}\\\\\\cline{1-2}
        \\end{array}$},\\emptyset,\\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\cline{2-3}
        &\\lr{6}&\\lr{7}\\\\\\cline{2-3}
        &\\lr{8}\\\\\\cline{1-2}
        \\lr{9}\\\\\\cline{1-1}
        \\end{array}$}
        }
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\lr{4}&\\lr{5}\\\\\n        \\end{array}$},\\emptyset,\\raisebox{-.6ex}{$\\begin{array}[b]{*{3}c}\\\\\n        &\\lr{6}&\\lr{7}\\\\\n        &\\lr{8}\\\\\n        \\lr{9}\\\\\n        \\end{array}$}
        }
        sage: Tableaux.options.convention="french"
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\cline{1-2}
        \\lr{4}&\\lr{5}\\\\\\cline{1-3}
        \\lr{1}&\\lr{2}&\\lr{3}\\\\\\cline{1-3}
        \\end{array}$},\\emptyset,\\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\cline{1-1}
        \\lr{9}\\\\\\cline{1-2}
        &\\lr{8}\\\\\\cline{2-3}
        &\\lr{6}&\\lr{7}\\\\\\cline{2-3}
        \\end{array}$}
        }
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{4}&\\lr{5}\\\\\n        \\lr{1}&\\lr{2}&\\lr{3}\\\\\n        \\end{array}$},\\emptyset,\\raisebox{-.6ex}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{9}\\\\\n        &\\lr{8}\\\\\n        &\\lr{6}&\\lr{7}\\\\\n        \\end{array}$}
        }
        sage: Tableaux.options.convention="russian"
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]]))
        {\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\cline{1-2}
        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}\\\\\\cline{1-3}
        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\\cline{1-3}
        \\end{array}$}},\\emptyset,\\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\cline{1-1}
        \\lr{\\rotatebox{-45}{9}}\\\\\\cline{1-2}
        &\\lr{\\rotatebox{-45}{8}}\\\\\\cline{2-3}
        &\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\\cline{2-3}
        \\end{array}$}}
        }
        sage: print(tex_from_array_tuple([[[1,2,3],[4,5]],[],[[None,6,7],[None,8],[9]]], with_lines=False))
        {\\def\\lr#1{\\multicolumn{1}{@{\\hspace{.6ex}}c@{\\hspace{.6ex}}}{\\raisebox{-.3ex}{$#1$}}}
        \\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{\\rotatebox{-45}{4}}&\\lr{\\rotatebox{-45}{5}}\\\\\n        \\lr{\\rotatebox{-45}{1}}&\\lr{\\rotatebox{-45}{2}}&\\lr{\\rotatebox{-45}{3}}\\\\\n        \\end{array}$}},\\emptyset,\\raisebox{-.6ex}{\\rotatebox{45}{$\\begin{array}[t]{*{3}c}\\\\\n        \\lr{\\rotatebox{-45}{9}}\\\\\n        &\\lr{\\rotatebox{-45}{8}}\\\\\n        &\\lr{\\rotatebox{-45}{6}}&\\lr{\\rotatebox{-45}{7}}\\\\\n        \\end{array}$}}
        }

        sage: Tableaux.options._reset()
    '''
def tex_from_skew_array(array, with_lines: bool = False, align: str = 'b') -> str:
    '''
    Create latex code for a "skew composition" ``array``.

    That is, for a two dimensional array in which each row can begin
    with an arbitrary number ``None``\'s and the remaining entries
    could, in principle, be anything but probably should be strings or
    integers of similar width. A row consisting completely of
    ``None``\'s is allowed.

    INPUT:

    - ``array`` -- the array

    - ``with_lines`` -- (default: ``False``) if ``True`` lines are drawn, if
      ``False`` they are not

    - ``align`` -- (default: ``\'b\'``) determine the alignment on the latex
      array environments

    EXAMPLES::

        sage: array=[[None, 2,3,4],[None,None],[5,6,7,8]]
        sage: print(sage.combinat.output.tex_from_skew_array(array))
        \\raisebox{-.6ex}{$\\begin{array}[b]{*{4}c}\\\\\n        &\\lr{2}&\\lr{3}&\\lr{4}\\\\\n        &\\\\\n        \\lr{5}&\\lr{6}&\\lr{7}&\\lr{8}\\\\\n        \\end{array}$}

    TESTS::

        sage: sage.combinat.output.tex_from_skew_array([(1,2,3), (2,3,4)])
        \'\\\\raisebox{-.6ex}{$\\\\begin{array}[b]{*{3}c}\\\\\\\\\\n\\\\lr{1}&\\\\lr{2}&\\\\lr{3}\\\\\\\\\\n\\\\lr{2}&\\\\lr{3}&\\\\lr{4}\\\\\\\\\\n\\\\end{array}$}\'
        sage: sage.combinat.output.tex_from_skew_array([((1,2,),)])
        \'\\\\raisebox{-.6ex}{$\\\\begin{array}[b]{*{1}c}\\\\\\\\\\n\\\\lr{(1, 2)}\\\\\\\\\\n\\\\end{array}$}\'
    '''
def svg_from_skew_array(array, with_lines: bool = False, align: str = 'b') -> str:
    '''
    Return the svg code for this skew array.

    EXAMPLES::

        sage: array=[[None, 2,3,4],[None,None],[5,6,7,8]]
        sage: sage.combinat.output.svg_from_skew_array(array)
        \'<?xml version="1.0" ...</svg>\'
    '''
def ascii_art_table(data, use_unicode: bool = False, convention: str = 'English'):
    """
    Return an ascii art table of ``data``.

    EXAMPLES::

        sage: from sage.combinat.output import ascii_art_table

        sage: data = [[None, None, 1], [2, 2], [3,4,5], [None, None, 10], [], [6]]
        sage: print(ascii_art_table(data))
                +----+
                | 1  |
        +---+---+----+
        | 2 | 2 |
        +---+---+----+
        | 3 | 4 | 5  |
        +---+---+----+
                | 10 |
                +----+
        <BLANKLINE>
        +---+
        | 6 |
        +---+
        sage: print(ascii_art_table(data, use_unicode=True))
                ┌────┐
                │ 1  │
        ┌───┬───┼────┘
        │ 2 │ 2 │
        ├───┼───┼────┐
        │ 3 │ 4 │ 5  │
        └───┴───┼────┤
                │ 10 │
                └────┘
        <BLANKLINE>
        ┌───┐
        │ 6 │
        └───┘

        sage: data = [[1, None, 2], [None, 2]]
        sage: print(ascii_art_table(data))
        +---+   +---+
        | 1 |   | 2 |
        +---+---+---+
            | 2 |
            +---+
        sage: print(ascii_art_table(data, use_unicode=True))
        ┌───┐   ┌───┐
        │ 1 │   │ 2 │
        └───┼───┼───┘
            │ 2 │
            └───┘
    """
def ascii_art_table_russian(data, use_unicode: bool = False, compact: bool = False):
    """
    Return an ascii art table of ``data`` for the russian convention.

    EXAMPLES::

        sage: from sage.combinat.output import ascii_art_table_russian
        sage: data = [[None, None, 1], [2, 2], [3,4,5], [None, None, 10], [], [6]]
        sage: print(ascii_art_table_russian(data))
           / \\         / \\\n          /   \\       /   \\\n         \\  6  /     \\ 10  \\\n          \\   /       \\   / \\\n           \\ /         \\ /   \\\n                        X  5  /
                       / \\   /
                      /   \\ /
                     /  4  X
                    / \\   / \\   / \\\n                   /   \\ /   \\ /   \\\n                  \\  3  X  2  X  1  /
                   \\   / \\   / \\   /
                    \\ /   \\ /   \\ /
                     \\  2  /
                      \\   /
                       \\ /
        sage: print(ascii_art_table_russian(data, use_unicode=True))
           ╱ ╲         ╱ ╲
          ╱   ╲       ╱   ╲
         ╲  6  ╱     ╲ 10  ╲
          ╲   ╱       ╲   ╱ ╲
           ╲ ╱         ╲ ╱   ╲
                        ╳  5  ╱
                       ╱ ╲   ╱
                      ╱   ╲ ╱
                     ╱  4  ╳
                    ╱ ╲   ╱ ╲   ╱ ╲
                   ╱   ╲ ╱   ╲ ╱   ╲
                  ╲  3  ╳  2  ╳  1  ╱
                   ╲   ╱ ╲   ╱ ╲   ╱
                    ╲ ╱   ╲ ╱   ╲ ╱
                     ╲  2  ╱
                      ╲   ╱
                       ╲ ╱
        sage: data = [[1, None, 2], [None, 2]]
        sage: print(ascii_art_table_russian(data))
          / \\ / \\\n         \\ 2 X 2 /
          \\ / \\ /
           X
          / \\\n         \\ 1 /
          \\ /
        sage: print(ascii_art_table_russian(data, use_unicode=True))
          ╱ ╲ ╱ ╲
         ╲ 2 ╳ 2 ╱
          ╲ ╱ ╲ ╱
           ╳
          ╱ ╲
         ╲ 1 ╱
          ╲ ╱
    """
def box_exists(tab, i, j) -> bool:
    """
    Return ``True`` if ``tab[i][j]`` exists and is not ``None``.

    In particular this
    allows for `tab[i][j]` to be ``''`` or ``0``.

    INPUT:

    - ``tab`` -- list of lists
    - ``i`` -- first coordinate
    - ``j`` -- second coordinate

    TESTS::

        sage: from sage.combinat.output import box_exists
        sage: tab = [[1,None,'', 0],[None]]
        sage: box_exists(tab, 0, 0)
        True
        sage: box_exists(tab, 0, 1)
        False
        sage: box_exists(tab, 0, 2)
        True
        sage: box_exists(tab, 0, 3)
        True
        sage: box_exists(tab, 0, 4)
        False
        sage: box_exists(tab, 1, 0)
        False
        sage: box_exists(tab, 1, 1)
        False
        sage: box_exists(tab, 0, -1)
        False
    """
