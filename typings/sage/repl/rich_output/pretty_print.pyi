from _typeshed import Incomplete
from sage.repl.rich_output import get_display_manager as get_display_manager
from sage.structure.sage_object import SageObject as SageObject

class SequencePrettyPrinter(SageObject):
    args: Incomplete
    kwds: Incomplete
    def __init__(self, *args, **kwds) -> None:
        """
        Pretty Printer for Multiple Arguments.

        INPUT/OUTPUT:

        Same as :func:`pretty_print`, except that the number of
        arguments must be >= 2. Otherwise its not a sequence of things
        to print.

        EXAMPLES::

            sage: pretty_print(1, 2, 3)   # indirect doctest
            1 2 3
            sage: from sage.repl.rich_output.pretty_print import SequencePrettyPrinter
            sage: SequencePrettyPrinter(1, 2, 3).pretty_print()
            1 2 3
        """
    def is_homogeneous(self, common_type):
        """
        Return whether the pretty print items are homogeneous.

        INPUT:

        - ``common_type`` -- a type

        OUTPUT:

        boolean; whether all items to be pretty printed are of said
        type.

        EXAMPLES::

            sage: from sage.repl.rich_output.pretty_print import SequencePrettyPrinter
            sage: seq = SequencePrettyPrinter(1, 2, 3)
            sage: seq.is_homogeneous(Integer)
            True
            sage: seq.is_homogeneous(str)
            False
        """
    def pretty_print(self) -> None:
        """
        Actually do the pretty print.

        EXAMPLES::

            sage: from sage.repl.rich_output.pretty_print import SequencePrettyPrinter
            sage: SequencePrettyPrinter(1, 2, 3).pretty_print()
            1 2 3

        The keyword arguments are only used the first time graphics
        output is generated::

            sage: seq = SequencePrettyPrinter(Graph(), Graph(), edge_labels=True)       # needs sage.graphs sage.plot
            sage: seq.pretty_print()   # does not pass edge_labels to graphics object   # needs sage.graphs sage.plot
            sage: seq._concatenate_graphs().show(edge_labels=True)                      # needs sage.graphs sage.plot
            Traceback (most recent call last):
            ...
            TypeError: ...matplotlib() got an unexpected keyword argument 'edge_labels'...
        """

def pretty_print(*args, **kwds) -> None:
    '''
    Pretty print the arguments using rich output if available.

    This function is similar to ``print()``, except that a rich output
    representation such as ``ascii_art`` or Latex is printed instead of the
    string representation.

    Note that the output depends on the global display preferences specified
    via
    :meth:`~sage.repl.rich_output.display_manager.DisplayManager.preferences`.
    If the display preference for ``text`` is not specified, Latex output is
    preferred.

    For graphical objects, a graphical output is used.

    For certain homogeneous multiple positional arguments, a suitable
    combined graphical output is generated. In particular, graphs and
    plots are treated special. Otherwise this function concatenates the
    textual representations.

    INPUT:

    - ``*args`` -- any number of positional arguments; the objects to
      pretty print

    - ``**kwds`` -- optional keyword arguments that are passed to the
      rich representation. Examples include:

        - ``dpi`` -- dots per inch

        - ``figsize``- [width, height] (same for square aspect)

        - ``axes`` -- (default: ``True``)

        - ``fontsize`` -- positive integer

        - ``frame`` -- boolean (default: ``False``); draw a MATLAB-like frame around
          the image

    EXAMPLES::

        sage: pretty_print(ZZ)
        Integer Ring

        sage: pretty_print("Integers = ", ZZ) # trac 11775
        \'Integers = \' Integer Ring

    To typeset LaTeX code as-is, use :class:`LatexExpr`::

        sage: pretty_print(LatexExpr(r"\\frac{x^2 + 1}{x - 2}"))
        \\frac{x^2 + 1}{x - 2}

    For text-based backends, the default text display preference is to output
    plain text which is usually the same as using ``print()``::

        sage: pretty_print(x^2 / (x + 1))                                               # needs sage.symbolic
        x^2/(x + 1)

        sage: t = BinaryTrees(3).first()                                                # needs sage.graphs
        sage: pretty_print(t)                                                           # needs sage.graphs
        [., [., [., .]]]
        sage: print(t)                                                                  # needs sage.graphs
        [., [., [., .]]]

    TESTS::

        sage: dm = get_display_manager()
        sage: dm.preferences.text = \'ascii_art\'

    EXAMPLES:

    Changing the text display preference affects the output of this function.
    The following illustrates a possible use-case::

        sage: %display ascii_art  # not tested
        sage: for t in BinaryTrees(3)[:3]:                                              # needs sage.graphs
        ....:     pretty_print(t)
        o
         \\\n          o
           \\\n            o
        o
         \\\n          o
         /
        o
          o
         / \\\n        o   o

        sage: pretty_print(x^2 / (x + 1))                                               # needs sage.symbolic
           2
          x
        -----
        x + 1

    TESTS:

    After the previous example, we need to reset the text display preferences::

        sage: dm.preferences.text = None

    ::

        sage: # needs sage.plot sage.symbolic
        sage: plt = plot(sin)
        sage: pretty_print(plt)             # graphics output
        sage: pretty_print(plt, plt)        # graphics output
        sage: pretty_print(ZZ, 123, plt)
        Integer Ring 123 Graphics object consisting of 1 graphics primitive
    '''
def show(*args, **kwds) -> None:
    """
    Alias for ``pretty_print``.

    This function is an alias for :func:`pretty_print`.

    INPUT/OUTPUT:

    See :func:`pretty_print`. Except if the argument is a graph, in
    which case it is plotted instead.

    EXAMPLES::

        sage: show(1)
        1
    """
