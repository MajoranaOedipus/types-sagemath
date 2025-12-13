from typing import Any

class CallableDict(dict):
    """File: /build/sagemath/src/sage/src/sage/misc/callable_dict.pyx (starting at line 14)

        Callable dictionary.

        This is a trivial subclass of :class:`dict` with an alternative
        view as a function.

        Typical use cases involve passing a dictionary `d` down to some
        tool that takes a function as input. The usual idiom in such use
        cases is to pass the ``d.__getitem__`` bound method. A pitfall is
        that this object is not picklable. When this feature is desired, a
        :class:`CallableDict` can be used instead. Note however that, with
        the current implementation, :class:`CallableDict` is slightly
        slower than ``d.__getitem__`` (see :issue:`6484` for benchmarks, and
        :issue:`18330` for potential for improvement).

        EXAMPLES::

            sage: from sage.misc.callable_dict import CallableDict
            sage: d = CallableDict({'one': 1, 'zwei': 2, 'trois': 3})
            sage: d['zwei']
            2
            sage: d('zwei')
            2

        In case the input is not in the dictionary, a :exc:`ValueError`
        is raised, for consistency with the function call syntax::

            sage: d[1]
            Traceback (most recent call last):
            ...
            KeyError: 1
            sage: d(1)
            Traceback (most recent call last):
            ...
            ValueError: 1 is not in dict
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __call__(self, key) -> Any:
        """CallableDict.__call__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/callable_dict.pyx (starting at line 51)

        Return ``self[key]``.

        INPUT:

        - ``x`` -- any hashable object

        A :exc:`ValueError` is raised if ``x`` is not in ``self``.

        TESTS::

            sage: from sage.misc.callable_dict import CallableDict
            sage: d = CallableDict({'one': 1, 'zwei': 2, 'trois': 3})
            sage: d('one'), d('zwei'), d('trois')
            (1, 2, 3)
            sage: d('x')
            Traceback (most recent call last):
            ...
            ValueError: 'x' is not in dict"""
