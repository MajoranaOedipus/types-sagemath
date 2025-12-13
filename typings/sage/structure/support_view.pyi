from collections.abc import MappingView, Sequence, Set
from sage.misc.superseded import deprecation as deprecation

class SupportView(MappingView, Sequence, Set):
    """
    Dynamic view of the set of keys of a dictionary that are associated with
    nonzero values.

    It behaves like the objects returned by the :meth:`keys`, :meth:`values`,
    :meth:`items` of a dictionary (or other :class:`collections.abc.Mapping`
    classes).

    INPUT:

    - ``mapping`` -- a :class:`dict` or another :class:`collections.abc.Mapping`

    - ``zero`` -- (optional) test for zeroness by comparing with this value

    EXAMPLES::

        sage: d = {'a': 47, 'b': 0, 'c': 11}
        sage: from sage.structure.support_view import SupportView
        sage: supp = SupportView(d); supp
        SupportView({'a': 47, 'b': 0, 'c': 11})
        sage: 'a' in supp, 'b' in supp, 'z' in supp
        (True, False, False)
        sage: len(supp)
        2
        sage: list(supp)
        ['a', 'c']
        sage: supp[0], supp[1]
        ('a', 'c')
        sage: supp[-1]
        'c'
        sage: supp[:]
        ('a', 'c')

    It reflects changes to the underlying dictionary::

        sage: d['b'] = 815
        sage: len(supp)
        3
    """
    def __init__(self, mapping, *, zero=None) -> None:
        """
        TESTS::

            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView({'a': 'b', 'c': ''}, zero='')
            sage: len(supp)
            1
        """
    def __len__(self) -> int:
        """
        TESTS::

            sage: d = {'a': 47, 'b': 0, 'c': 11}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({'a': 47, 'b': 0, 'c': 11})
            sage: len(supp)
            2
        """
    def __getitem__(self, index):
        """
        TESTS::

            sage: d = {'a': 47, 'b': 0, 'c': 11}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({'a': 47, 'b': 0, 'c': 11})
            sage: supp[2]
            Traceback (most recent call last):
            ...
            IndexError
        """
    def __iter__(self):
        """
        TESTS::

            sage: d = {'a': 47, 'b': 0, 'c': 11}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({'a': 47, 'b': 0, 'c': 11})
            sage: iter(supp)
            <generator object SupportView.__iter__ at ...>
        """
    def __contains__(self, key) -> bool:
        """
        TESTS::

            sage: d = {'a': 47, 'b': 0, 'c': 11}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({'a': 47, 'b': 0, 'c': 11})
            sage: 'a' in supp, 'b' in supp, 'z' in supp
            (True, False, False)
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: d = {1: 17, 2: 0}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({1: 17, 2: 0})
            sage: supp == [1]
            doctest:warning...
            DeprecationWarning: comparing a SupportView with a list is deprecated
            See https://github.com/sagemath/sage/issues/34509 for details.
            True
        """
    def __ne__(self, other):
        """
        TESTS::

            sage: d = {1: 17, 2: 0}
            sage: from sage.structure.support_view import SupportView
            sage: supp = SupportView(d); supp
            SupportView({1: 17, 2: 0})
            sage: supp != [1]
            doctest:warning...
            DeprecationWarning: comparing a SupportView with a list is deprecated
            See https://github.com/sagemath/sage/issues/34509 for details.
            False
        """
