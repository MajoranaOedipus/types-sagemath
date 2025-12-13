from _typeshed import Incomplete

class MultiplexFunction:
    """
    A simple wrapper object for functions that are called on a list of
    objects.
    """
    multiplexer: Incomplete
    name: Incomplete
    def __init__(self, multiplexer, name) -> None:
        """
        EXAMPLES::

            sage: from sage.misc.object_multiplexer import Multiplex, MultiplexFunction
            sage: m = Multiplex(1,1/2)
            sage: f = MultiplexFunction(m,'str')
            sage: f
            <sage.misc.object_multiplexer.MultiplexFunction object at 0x...>
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: from sage.misc.object_multiplexer import Multiplex, MultiplexFunction
            sage: m = Multiplex(1,1/2)
            sage: f = MultiplexFunction(m,'str')
            sage: f()
            ('1', '1/2')
        """

class Multiplex:
    """
    Object for a list of children such that function calls on this
    new object implies that the same function is called on all
    children.
    """
    children: Incomplete
    def __init__(self, *args) -> None:
        """
        EXAMPLES::

            sage: from sage.misc.object_multiplexer import Multiplex
            sage: m = Multiplex(1,1/2)
            sage: m.str()
            ('1', '1/2')
        """
    def __getattr__(self, name):
        """
        EXAMPLES::

            sage: from sage.misc.object_multiplexer import Multiplex
            sage: m = Multiplex(1,1/2)
            sage: m.str
            <sage.misc.object_multiplexer.MultiplexFunction object at 0x...>
            sage: m.__bork__
            Traceback (most recent call last):
            ...
            AttributeError: 'Multiplex' has no attribute '__bork__'...
        """
