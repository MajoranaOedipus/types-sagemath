from sage.categories.category import ZZ as ZZ
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

Infinity: float
MInfinity: float

class Envelope:
    '''Envelope(f, min_part=0, *, max_part=Infinity, min_slope=MInfinity, max_slope=Infinity, min_length=0, max_length=Infinity, sign=1)

    File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 282)

    The (currently approximated) upper (lower) envelope of a function
    under the specified constraints.

    INPUT:

    - ``f`` -- a function, list, or tuple; if ``f`` is a list, it is
      considered as the function ``f(i)=f[i]``, completed for larger
      `i` with ``f(i)=max_part``.

    - ``min_part``, ``max_part``, ``min_slope``, ``max_slope``, ...
      as for :class:`IntegerListsLex` (please consult for details).

    - ``sign`` -- (+1 or -1) multiply the input values with ``sign``
      and multiply the output with ``sign``. Setting this to `-1` can
      be used to implement a lower envelope.

    The *upper envelope* `U(f)` of `f` is the (pointwise) largest
    function which is bounded above by `f` and satisfies the
    ``max_part`` and ``max_slope`` conditions. Furthermore, for
    ``i,i+1<min_length``, the upper envelope also satisfies the
    ``min_slope`` condition.

    Upon computing `U(f)(i)`, all the previous values
    for `j\\leq i` are computed and cached; in particular `f(i)` will
    be computed at most once for each `i`.

    .. TODO::

        - This class is a good candidate for Cythonization, especially
          to get the critical path in ``__call__`` super fast.

        - To get full envelopes, we would want both the ``min_slope``
          and ``max_slope`` conditions to always be satisfied. This is
          only properly defined for the restriction of `f` to a finite
          interval `0,..,k`, and depends on `k`.

        - This is the core "data structure" of
          ``IntegerListsLex``. Improving the lookahead there
          essentially depends on having functions with a good
          complexity to compute the area below an envelope; and in
          particular how it evolves when increasing the length.

    EXAMPLES::

        sage: from sage.combinat.integer_lists import Envelope

    Trivial upper and lower envelopes::

        sage: f = Envelope([3,2,2])
        sage: [f(i) for i in range(10)]
        [3, 2, 2, inf, inf, inf, inf, inf, inf, inf]
        sage: f = Envelope([3,2,2], sign=-1)
        sage: [f(i) for i in range(10)]
        [3, 2, 2, 0, 0, 0, 0, 0, 0, 0]

    A more interesting lower envelope::

        sage: f = Envelope([4,1,5,3,5], sign=-1, min_part=2, min_slope=-1)
        sage: [f(i) for i in range(10)]
        [4, 3, 5, 4, 5, 4, 3, 2, 2, 2]

    Currently, adding ``max_slope`` has no effect::

        sage: f = Envelope([4,1,5,3,5], sign=-1, min_part=2, min_slope=-1, max_slope=0)
        sage: [f(i) for i in range(10)]
        [4, 3, 5, 4, 5, 4, 3, 2, 2, 2]

    unless ``min_length`` is large enough::

        sage: f = Envelope([4,1,5,3,5], sign=-1, min_part=2, min_slope=-1, max_slope=0, min_length=2)
        sage: [f(i) for i in range(10)]
        [4, 3, 5, 4, 5, 4, 3, 2, 2, 2]

        sage: f = Envelope([4,1,5,3,5], sign=-1, min_part=2, min_slope=-1, max_slope=0, min_length=4)
        sage: [f(i) for i in range(10)]
        [5, 5, 5, 4, 5, 4, 3, 2, 2, 2]

        sage: f = Envelope([4,1,5,3,5], sign=-1, min_part=2, min_slope=-1, max_slope=0, min_length=5)
        sage: [f(i) for i in range(10)]
        [5, 5, 5, 5, 5, 4, 3, 2, 2, 2]

    A non trivial upper envelope::

        sage: f = Envelope([9,1,5,4], max_part=7, max_slope=2)
        sage: [f(i) for i in range(10)]
        [7, 1, 3, 4, 6, 7, 7, 7, 7, 7]

    TESTS::

        sage: f = Envelope(3, min_slope=1)
        sage: [f(i) for i in range(10)]
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

        sage: f = Envelope(3, min_slope=1, min_length=5)
        sage: [f(i) for i in range(10)]
        [-1, 0, 1, 2, 3, 3, 3, 3, 3, 3]

        sage: f = Envelope(3, sign=-1, min_slope=1)
        sage: [f(i) for i in range(10)]
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        sage: f = Envelope(3, sign=-1, max_slope=-1, min_length=4)
        sage: [f(i) for i in range(10)]
        [6, 5, 4, 3, 3, 3, 3, 3, 3, 3]'''
    max_part: File
    max_slope: File
    min_slope: File
    sign: File
    def __init__(self, f, min_part=..., max_part=..., min_slope=..., max_slope=..., min_length=..., max_length=..., sign=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 389)

                Initialize this envelope.

                TESTS::

                    sage: from sage.combinat.integer_lists import Envelope
                    sage: f = Envelope(3, sign=-1, max_slope=-1, min_length=4)
                    sage: f.sign
                    -1
                    sage: f.max_part
                    -3
                    sage: f.max_slope
                    inf
                    sage: f.min_slope
                    1
                    sage: TestSuite(f).run(skip='_test_pickling')
                    sage: Envelope(3, sign=1/3, max_slope=-1, min_length=4)
                    Traceback (most recent call last):
                    ...
                    TypeError: no conversion of this rational to integer
                    sage: Envelope(3, sign=-2, max_slope=-1, min_length=4)
                    Traceback (most recent call last):
                    ...
                    ValueError: sign should be +1 or -1
        """
    def adapt(self, m, j) -> Any:
        """Envelope.adapt(self, m, j)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 612)

        Return this envelope adapted to an additional local constraint.

        INPUT:

        - ``m`` -- nonnegative integer (starting value)

        - ``j`` -- nonnegative integer (position)

        This method adapts this envelope to the additional local
        constraint imposed by having a part `m` at position `j`.
        Namely, this returns a function which computes, for any `i>j`,
        the minimum of the ceiling function and the value restriction
        given by the slope conditions.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: f = Envelope(3)
            sage: g = f.adapt(1,1)
            sage: g is f
            True
            sage: [g(i) for i in range(10)]
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

            sage: f = Envelope(3, max_slope=1)
            sage: g = f.adapt(1,1)
            sage: [g(i) for i in range(10)]
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3]

        Note that, in both cases above, the adapted envelope is only
        guaranteed to be valid for `i>j`! This is to leave potential
        room in the future for sharing similar adapted envelopes::

            sage: g = f.adapt(0,0)
            sage: [g(i) for i in range(10)]
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3]

            sage: g = f.adapt(2,2)
            sage: [g(i) for i in range(10)]
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3]

            sage: g = f.adapt(3,3)
            sage: [g(i) for i in range(10)]
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 3]

        Now with a lower envelope::

            sage: f = Envelope(1, sign=-1, min_slope=-1)
            sage: g = f.adapt(2,2)
            sage: [g(i) for i in range(10)]
            [4, 3, 2, 1, 1, 1, 1, 1, 1, 1]
            sage: g = f.adapt(1,3)
            sage: [g(i) for i in range(10)]
            [4, 3, 2, 1, 1, 1, 1, 1, 1, 1]"""
    def limit(self) -> Any:
        """Envelope.limit(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 535)

        Return a bound on the limit of ``self``.

        OUTPUT: nonnegative integer or `\\infty`

        This returns some upper bound for the accumulation points of
        this upper envelope. For a lower envelope, a lower bound is
        returned instead.

        In particular this gives a bound for the value of ``self`` at
        `i` for `i` large enough. Special case: for a lower envelop,
        and when the limit is `\\infty`, the envelope is guaranteed to
        tend to `\\infty` instead.

        When ``s=self.limit_start()`` is finite, this bound is
        guaranteed to be valid for `i>=s`.

        Sometimes it's better to have a loose bound that starts early;
        sometimes the converse holds. At this point which specific
        bound and starting point is returned is not set in stone, in
        order to leave room for later optimizations.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit()
            inf
            sage: Envelope([4,1,5], max_part=2).limit()
            2
            sage: Envelope([4,1,5], max_slope=0).limit()
            1
            sage: Envelope(lambda x: 3, max_part=2).limit()
            2

        Lower envelopes::

            sage: Envelope(lambda x: 3, min_part=2, sign=-1).limit()
            2
            sage: Envelope([4,1,5], min_slope=0, sign=-1).limit()
            5
            sage: Envelope([4,1,5], sign=-1).limit()
            0

        .. SEEALSO:: :meth:`limit_start`"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    @overload
    def limit_start(self) -> Any:
        """Envelope.limit_start(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 503)

        Return from which `i` on the bound returned by ``limit`` holds.

        .. SEEALSO:: :meth:`limit` for the precise specifications.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: Envelope([4,1,5]).limit_start()
            3
            sage: Envelope([4,1,5], sign=-1).limit_start()
            3

            sage: Envelope([4,1,5], max_part=2).limit_start()
            3

            sage: Envelope(4).limit_start()
            0
            sage: Envelope(4, sign=-1).limit_start()
            0

            sage: Envelope(lambda x: 3).limit_start() == Infinity
            True
            sage: Envelope(lambda x: 3, max_part=2).limit_start() == Infinity
            True

            sage: Envelope(lambda x: 3, sign=-1, min_part=2).limit_start() == Infinity
            True"""
    def __call__(self, Py_ssize_tk) -> Any:
        """Envelope.__call__(self, Py_ssize_t k)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 586)

        Return the value of this envelope at `k`.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: f = Envelope([4,1,5,3,5])
            sage: f.__call__(2)
            5
            sage: [f(i) for i in range(10)]
            [4, 1, 5, 3, 5, inf, inf, inf, inf, inf]

        .. NOTE::

            See the documentation of :class:`Envelope` for tests and
            examples."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """Envelope.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 675)

        Pickle ``self``.

        EXAMPLES::

            sage: from sage.combinat.integer_lists import Envelope
            sage: h = Envelope(3, min_part=2)
            sage: loads(dumps(h)) == h
            True"""

class IntegerListsBackend:
    """IntegerListsBackend(n=None, length=None, min_length=0, *, max_length=Infinity, floor=None, ceiling=None, min_part=0, max_part=Infinity, min_slope=MInfinity, max_slope=Infinity, min_sum=0, max_sum=Infinity)

    File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 35)

    Base class for the Cython back-end of an enumerated set of lists of
    integers with specified constraints.

    This base implements the basic operations, including checking for
    containment using :meth:`_contains`, but not iteration. For
    iteration, subclass this class and implement an ``_iter()`` method.

    EXAMPLES::

        sage: from sage.combinat.integer_lists.base import IntegerListsBackend
        sage: L = IntegerListsBackend(6, max_slope=-1)
        sage: L._contains([3,2,1])
        True"""
    ceiling: File
    floor: File
    max_length: File
    max_part: File
    max_slope: File
    max_sum: File
    min_length: File
    min_part: File
    min_slope: File
    min_sum: File
    def __init__(self, n=..., length=..., min_length=..., max_length=..., floor=..., ceiling=..., min_part=..., max_part=..., min_slope=..., max_slope=..., min_sum=..., max_sum=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/integer_lists/base.pyx (starting at line 51)

                Initialize ``self``.

                TESTS::

                    sage: from sage.combinat.integer_lists.base import IntegerListsBackend
                    sage: C = IntegerListsBackend(2, length=3)
                    sage: C = IntegerListsBackend(min_sum=1.4)                                  # needs sage.rings.real_mpfr
                    Traceback (most recent call last):
                    ...
                    TypeError: Attempt to coerce non-integral RealNumber to Integer
                    sage: C = IntegerListsBackend(min_sum=Infinity)
                    Traceback (most recent call last):
                    ...
                    TypeError: unable to coerce <class 'sage.rings.infinity.PlusInfinity'> to an integer
        """
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
