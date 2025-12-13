from _typeshed import Incomplete
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp_method as richcmp_method
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class UnknownError(TypeError):
    """
    Raised whenever :class:`Unknown` is used in a boolean operation.

    EXAMPLES::

        sage: not Unknown
        Traceback (most recent call last):
        ...
        UnknownError: Unknown does not evaluate in boolean context
    """

class UnknownClass(UniqueRepresentation):
    """
    The Unknown truth value.

    The ``Unknown`` object is used in Sage in several places as return value
    in addition to ``True`` and ``False``, in order to signal uncertainty
    about or inability to compute the result. ``Unknown`` can be identified
    using ``is``, or by catching :exc:`UnknownError` from a boolean
    operation.

    .. WARNING::

        Calling ``bool()`` with ``Unknown`` as argument will throw an
        :exc:`UnknownError`. This also means that applying ``and``, ``not``,
        and ``or`` to ``Unknown`` might fail.

    TESTS::

        sage: TestSuite(Unknown).run()
    """
    def __bool__(self) -> bool:
        """
        When evaluated in a boolean context ``Unknown`` raises a :exc:`UnknownError`.

        EXAMPLES::

            sage: bool(Unknown)
            Traceback (most recent call last):
            ...
            UnknownError: Unknown does not evaluate in boolean context
            sage: not Unknown
            Traceback (most recent call last):
            ...
            UnknownError: Unknown does not evaluate in boolean context
        """
    def __and__(self, other):
        """
        The ``&`` logical operation.

        EXAMPLES::

            sage: Unknown & False
            False
            sage: Unknown & Unknown
            Unknown
            sage: Unknown & True
            Unknown

            sage: Unknown.__or__(3)
            NotImplemented
        """
    def __or__(self, other):
        """
        The ``|`` logical connector.

        EXAMPLES::

            sage: Unknown | False
            Unknown
            sage: Unknown | Unknown
            Unknown
            sage: Unknown | True
            True

            sage: Unknown.__or__(3)
            NotImplemented
        """
    def __richcmp__(self, other, op):
        """
        Comparison of truth value.

        EXAMPLES::

            sage: l = [False, Unknown, True]
            sage: for a in l: print([a < b for b in l])
            [False, True, True]
            [False, False, True]
            [False, False, False]

            sage: for a in l: print([a <= b for b in l])
            [True, True, True]
            [False, True, True]
            [False, False, True]
        """

Unknown: Incomplete
