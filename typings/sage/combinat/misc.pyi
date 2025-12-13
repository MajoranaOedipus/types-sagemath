from _typeshed import Incomplete
from sage.misc.misc_c import prod as prod

class DoublyLinkedList:
    """
    A doubly linked list class that provides constant time hiding and
    unhiding of entries.

    Note that this list's indexing is 1-based.

    EXAMPLES::

        sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3]); dll
        Doubly linked list of [1, 2, 3]: [1, 2, 3]
        sage: dll.hide(1); dll
        Doubly linked list of [1, 2, 3]: [2, 3]
        sage: dll.unhide(1); dll
        Doubly linked list of [1, 2, 3]: [1, 2, 3]
        sage: dll.hide(2); dll
        Doubly linked list of [1, 2, 3]: [1, 3]
        sage: dll.unhide(2); dll
        Doubly linked list of [1, 2, 3]: [1, 2, 3]
    """
    l: Incomplete
    next_value: Incomplete
    prev_value: Incomplete
    def __init__(self, l) -> None:
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll == loads(dumps(dll))
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll2 = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll == dll2
            True
            sage: dll.hide(1)
            sage: dll == dll2
            False
        """
    def __ne__(self, other):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll2 = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll != dll2
            False
            sage: dll.hide(1)
            sage: dll != dll2
            True
        """
    def __iter__(self):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: list(dll)
            [1, 2, 3]
        """
    def hide(self, i) -> None:
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll.hide(1)
            sage: list(dll)
            [2, 3]
        """
    def unhide(self, i) -> None:
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll.hide(1); dll.unhide(1)
            sage: list(dll)
            [1, 2, 3]
        """
    def head(self):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll.head()
            1
            sage: dll.hide(1)
            sage: dll.head()
            2
        """
    def next(self, j):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll.next(1)
            2
            sage: dll.hide(2)
            sage: dll.next(1)
            3
        """
    def prev(self, j):
        """
        TESTS::

            sage: dll = sage.combinat.misc.DoublyLinkedList([1,2,3])
            sage: dll.prev(3)
            2
            sage: dll.hide(2)
            sage: dll.prev(3)
            1
        """

def umbral_operation(poly):
    """
    Return the umbral operation `\\downarrow` applied to poly.

    The umbral operation replaces each instance of
    `x_i^{a_i}` with
    `x_i*(x_i - 1)*\\cdots*(x_i - a_i + 1)`.

    EXAMPLES::

        sage: P = PolynomialRing(QQ, 2, 'x')
        sage: x = P.gens()
        sage: from sage.combinat.misc import umbral_operation
        sage: umbral_operation(x[0]^3) == x[0]*(x[0]-1)*(x[0]-2)
        True
        sage: umbral_operation(x[0]*x[1])
        x0*x1
        sage: umbral_operation(x[0]+x[1])
        x0 + x1
        sage: umbral_operation(x[0]^2*x[1]^2) == x[0]*(x[0]-1)*x[1]*(x[1]-1)
        True
    """

class IterableFunctionCall:
    """
    This class wraps functions with a yield statement (generators) by
    an object that can be iterated over. For example,

    EXAMPLES::

        sage: def f(): yield 'a'; yield 'b'

    This does not work::

        sage: for z in f: print(z)
        Traceback (most recent call last):
        ...
        TypeError: 'function' object is not iterable

    Use IterableFunctionCall if you want something like the above to
    work::

        sage: from sage.combinat.misc import IterableFunctionCall
        sage: g = IterableFunctionCall(f)
        sage: for z in g: print(z)
        a
        b

    If your function takes arguments, just put them after the function
    name. You needn't enclose them in a tuple or anything, just put them
    there::

        sage: def f(n, m): yield 'a' * n; yield 'b' * m; yield 'foo'
        sage: g = IterableFunctionCall(f, 2, 3)
        sage: for z in g: print(z)
        aa
        bbb
        foo
    """
    f: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, f, *args, **kwargs) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.misc import IterableFunctionCall
            sage: IterableFunctionCall(iter, [1,2,3])
            Iterable function call <built-in function iter> with args=([1, 2, 3],) and kwargs={}
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.misc import IterableFunctionCall
            sage: list(iter(IterableFunctionCall(iter, [1,2,3])))
            [1, 2, 3]
        """

def check_integer_list_constraints(l, **kwargs):
    """
    EXAMPLES::

        sage: from sage.combinat.misc import check_integer_list_constraints
        sage: cilc = check_integer_list_constraints
        sage: l = [[2,1,3],[1,2],[3,3],[4,1,1]]
        sage: cilc(l, min_part=2)
        [[3, 3]]
        sage: cilc(l, max_part=2)
        [[1, 2]]
        sage: cilc(l, length=2)
        [[1, 2], [3, 3]]
        sage: cilc(l, max_length=2)
        [[1, 2], [3, 3]]
        sage: cilc(l, min_length=3)
        [[2, 1, 3], [4, 1, 1]]
        sage: cilc(l, max_slope=0)
        [[3, 3], [4, 1, 1]]
        sage: cilc(l, min_slope=1)
        [[1, 2]]
        sage: cilc(l, outer=[2,2])
        [[1, 2]]
        sage: cilc(l, inner=[2,2])
        [[3, 3]]

    ::

        sage: cilc([1,2,3], length=3, singleton=True)
        [1, 2, 3]
        sage: cilc([1,2,3], length=2, singleton=True) is None
        True
    """
