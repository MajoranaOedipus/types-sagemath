from _typeshed import Incomplete
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class AttrCallObject:
    name: Incomplete
    args: Incomplete
    kwds: Incomplete
    def __init__(self, name, args, kwds) -> None:
        """
        TESTS::

            sage: f = attrcall('core', 3); f
            *.core(3)
            sage: TestSuite(f).run()
        """
    def __call__(self, x, *args):
        """
        Get the ``self.name`` method from ``x``, calls it with
        ``self.args`` and ``args`` as positional parameters and
        ``self.kwds`` as keyword parameters, and returns the result.

        EXAMPLES::

            sage: core = attrcall('core', 3)
            sage: core(Partition([4,2]))                                                # needs sage.combinat
            [4, 2]

            sage: series = attrcall('series', x)                                        # needs sage.symbolic
            sage: series(sin(x), 4)                                                     # needs sage.symbolic
            1*x + (-1/6)*x^3 + Order(x^4)
        """
    def __eq__(self, other):
        """
        Equality testing.

        EXAMPLES::

            sage: attrcall('core', 3, flatten = True) == attrcall('core', 3, flatten = True)
            True
            sage: attrcall('core', 2) == attrcall('core', 3)
            False
            sage: attrcall('core', 2) == 1
            False
        """
    def __ne__(self, other):
        """
        Equality testing.

        EXAMPLES::

            sage: attrcall('core', 3, flatten = True) != attrcall('core', 3, flatten = True)
            False
            sage: attrcall('core', 2) != attrcall('core', 3)
            True
            sage: attrcall('core', 2) != 1
            True
        """
    def __hash__(self):
        """
        Hash value.

        This method tries to ensure that, when two ``attrcall``
        objects are equal, they have the same hash value.

        .. warning::

            dicts are not hashable, so we instead hash their
            items; however the order of those items might differ. The
            proper fix would be to use a frozen dict for ``kwds``, when
            frozen dicts will be available in Python.

        EXAMPLES::

            sage: x = attrcall('core', 3, flatten = True, blah = 1)
            sage: hash(x)       # random # indirect doctest
            210434060
            sage: type(hash(x))
            <class 'int'>
            sage: y = attrcall('core', 3, blah = 1, flatten = True)
            sage: hash(y) == hash(x)
            True
            sage: y = attrcall('core', 3, flatten = True, blah = 2)
            sage: hash(y) != hash(x)
            True
            sage: hash(attrcall('core', 2)) != hash(attrcall('core', 3))
            True
            sage: hash(attrcall('core', 2)) != hash(1)
            True

        Note: a missing ``__hash__`` method here used to break the
        unique representation of parents taking ``attrcall`` objects
        as input; see :issue:`8911`.
        """

def attrcall(name, *args, **kwds):
    """
    Return a callable which takes in an object, gets the method named
    name from that object, and calls it with the specified arguments
    and keywords.

    INPUT:

    - ``name`` -- string of the name of the method you
      want to call

    - ``args, kwds`` -- arguments and keywords to be passed
      to the method

    EXAMPLES::

        sage: f = attrcall('core', 3); f
        *.core(3)
        sage: [f(p) for p in Partitions(5)]                                             # needs sage.combinat
        [[2], [1, 1], [1, 1], [3, 1, 1], [2], [2], [1, 1]]
    """
def call_method(obj, name, *args, **kwds):
    '''
    Call the method ``name`` on ``obj``.

    This has to exist somewhere in Python!!!

    .. SEEALSO:: :func:`operator.methodcaller` :func:`attrcal`

    EXAMPLES::

        sage: from sage.misc.call import call_method
        sage: call_method(1, "__add__", 2)
        3
    '''
