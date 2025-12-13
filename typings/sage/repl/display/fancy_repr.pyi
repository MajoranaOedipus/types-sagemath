from sage.repl.display.util import format_list as format_list

class ObjectReprABC:
    """
    The abstract base class of an object representer.

    .. automethod:: __call__
    """
    def __call__(self, obj, p, cycle):
        """
        Format object.

        INPUT:

        - ``obj`` -- anything; object to format

        - ``p`` -- PrettyPrinter instance

        - ``cycle`` -- boolean; whether there is a cycle

        OUTPUT:

        boolean; whether the representer is applicable to ``obj``. If
        ``True``, the string representation is appended to ``p``.

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import ObjectReprABC
            sage: ObjectReprABC().format_string(123)   # indirect doctest
            'Error: ObjectReprABC.__call__ is abstract'
        """
    def format_string(self, obj):
        """
        For doctesting only: Directly return string.

        INPUT:

        - ``obj`` -- anything; object to format

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import ObjectReprABC
            sage: ObjectReprABC().format_string(123)
            'Error: ObjectReprABC.__call__ is abstract'
        """

class SomeIPythonRepr(ObjectReprABC):
    def __init__(self) -> None:
        """
        Some selected representers from IPython.

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import SomeIPythonRepr
            sage: SomeIPythonRepr()
            SomeIPythonRepr pretty printer

        .. automethod:: __call__
        """
    def __call__(self, obj, p, cycle):
        """
        Format object.

        INPUT:

        - ``obj`` -- anything; object to format

        - ``p`` -- PrettyPrinter instance

        - ``cycle`` -- boolean; whether there is a cycle

        OUTPUT:

        boolean; whether the representer is applicable to ``obj``. If
        ``True``, the string representation is appended to ``p``.

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import SomeIPythonRepr
            sage: pp = SomeIPythonRepr()
            sage: pp.format_string(set([1, 2, 3]))
            '{1, 2, 3}'

        TESTS::

            sage: pp.format_string(Sequence([[1]*20, [2]*20]))
            '[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\\n [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]'
        """

class LargeMatrixHelpRepr(ObjectReprABC):
    """
    Representation including help for large Sage matrices.

    .. automethod:: __call__
    """
    def __call__(self, obj, p, cycle):
        '''
        Format matrix.

        INPUT:

        - ``obj`` -- anything; object to format

        - ``p`` -- PrettyPrinter instance

        - ``cycle`` -- boolean; whether there is a cycle

        OUTPUT:

        boolean; whether the representer is applicable to ``obj``. If
        ``True``, the string representation is appended to ``p``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.repl.display.fancy_repr import LargeMatrixHelpRepr
            sage: M = identity_matrix(40)
            sage: pp = LargeMatrixHelpRepr()
            sage: pp.format_string(M)
            "40 x 40 dense matrix over Integer Ring (use the \'.str()\' method...)"
            sage: pp.format_string([M, M])
            \'--- object not handled by representer ---\'

        Leads to::

            sage: M                                                                     # needs sage.modules
            40 x 40 dense matrix over Integer Ring (use the \'.str()\' method...)
            sage: [M, M]                                                                # needs sage.modules
            [40 x 40 dense matrix over Integer Ring,
             40 x 40 dense matrix over Integer Ring]
        '''

class PlainPythonRepr(ObjectReprABC):
    """
    The ordinary Python representation.

    .. automethod:: __call__
    """
    def __call__(self, obj, p, cycle):
        '''
        Format object.

        INPUT:

        - ``obj`` -- anything; object to format

        - ``p`` -- PrettyPrinter instance

        - ``cycle`` -- boolean; whether there is a cycle

        OUTPUT:

        boolean; whether the representer is applicable to ``obj``. If
        ``True``, the string representation is appended to ``p``.

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import PlainPythonRepr
            sage: pp = PlainPythonRepr()
            sage: pp.format_string(type(1))
            "<class \'sage.rings.integer.Integer\'>"

        Do not swallow a trailing newline at the end of the output of
        a custom representer. Note that it is undesirable to have a
        trailing newline, and if we don\'t display it you can\'t fix
        it::

            sage: class Newline():
            ....:     def __repr__(self):
            ....:         return \'newline\\n\'
            sage: n = Newline()
            sage: pp.format_string(n)
            \'newline\\n\'
            sage: pp.format_string([n, n, n])
            \'[newline\\n, newline\\n, newline\\n]\'
            sage: [n, n, n]
            [newline
             , newline
             , newline
             ]
        '''

class TallListRepr(ObjectReprABC):
    """
    Special representation for lists with tall entries (e.g. matrices).

    .. automethod:: __call__
    """
    def __call__(self, obj, p, cycle):
        """
        Format list/tuple.

        INPUT:

        - ``obj`` -- anything; object to format

        - ``p`` -- PrettyPrinter instance

        - ``cycle`` -- boolean; whether there is a cycle

        OUTPUT:

        boolean; whether the representer is applicable to ``obj``. If
        ``True``, the string representation is appended to ``p``.

        EXAMPLES::

            sage: from sage.repl.display.fancy_repr import TallListRepr
            sage: format_list = TallListRepr().format_string
            sage: format_list([1, 2, identity_matrix(2)])                               # needs sage.modules
            '[\\n      [1 0]\\n1, 2, [0 1]\\n]'

        Check that :issue:`18743` is fixed::

            sage: class Foo():
            ....:     def __repr__(self):
            ....:         return '''BBB    AA   RRR
            ....: B  B  A  A  R  R
            ....: BBB   AAAA  RRR
            ....: B  B  A  A  R  R
            ....: BBB   A  A  R   R'''
            ....:     def _repr_option(self, key):
            ....:         return key == 'ascii_art'
            sage: F = Foo()
            sage: [F, F]
            [
            BBB    AA   RRR    BBB    AA   RRR
            B  B  A  A  R  R   B  B  A  A  R  R
            BBB   AAAA  RRR    BBB   AAAA  RRR
            B  B  A  A  R  R   B  B  A  A  R  R
            BBB   A  A  R   R, BBB   A  A  R   R
            ]
        """
