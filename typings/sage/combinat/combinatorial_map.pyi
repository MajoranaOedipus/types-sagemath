from _typeshed import Incomplete
from typing import Self

def combinatorial_map_trivial(f=None, order=None, name=None):
    """
    Combinatorial map decorator.

    See :ref:`sage.combinat.combinatorial_map` for a description of
    this decorator and its purpose. This default implementation does
    nothing.

    INPUT:

    - ``f`` -- (default: ``None``, if combinatorial_map is used as a decorator) a function
    - ``name`` -- (default: ``None``) the name for nicer outputs on combinatorial maps
    - ``order`` -- (default: ``None``) the order of the combinatorial map, if it is known. Is not used, but might be helpful later

    OUTPUT: ``f`` unchanged

    EXAMPLES::

        sage: from sage.combinat.combinatorial_map import combinatorial_map_trivial as combinatorial_map
        sage: class MyPermutation():
        ....:     @combinatorial_map
        ....:     def reverse(self):
        ....:         '''
        ....:         Reverse the permutation
        ....:         '''
        ....:         # ... code ...
        ....:     @combinatorial_map(name='descent set of permutation')
        ....:     def descent_set(self):
        ....:         '''
        ....:         The descent set of the permutation
        ....:         '''
        ....:         # ... code ...

        sage: MyPermutation.reverse
        <function MyPermutation.reverse at ...>

        sage: MyPermutation.descent_set
        <function MyPermutation.descent_set at ...>
    """
def combinatorial_map_wrapper(f=None, order=None, name=None):
    """
    Combinatorial map decorator (basic example).

    See :ref:`sage.combinat.combinatorial_map` for a description of
    the ``combinatorial_map`` decorator and its purpose. This
    implementation, together with :func:`combinatorial_maps_in_class`
    illustrates how to use this decorator as a hook to instrument the
    Sage code.

    INPUT:

    - ``f`` -- (default: ``None``, if combinatorial_map is used as a decorator) a function
    - ``name`` -- (default: ``None``) the name for nicer outputs on combinatorial maps
    - ``order`` -- (default: ``None``) the order of the combinatorial map, if it is known. Is not used, but might be helpful later

    OUTPUT: a combinatorial map; this is an instance of the :class:`CombinatorialMap`

    EXAMPLES:

    We define a class illustrating the use of this implementation of
    the :obj:`combinatorial_map` decorator with its various arguments::

        sage: from sage.combinat.combinatorial_map import combinatorial_map_wrapper as combinatorial_map
        sage: class MyPermutation():
        ....:     @combinatorial_map()
        ....:     def reverse(self):
        ....:         '''
        ....:         Reverse the permutation
        ....:         '''
        ....:         pass
        ....:     @combinatorial_map(order=2)
        ....:     def inverse(self):
        ....:         '''
        ....:         The inverse of the permutation
        ....:         '''
        ....:         pass
        ....:     @combinatorial_map(name='descent set of permutation')
        ....:     def descent_set(self):
        ....:         '''
        ....:         The descent set of the permutation
        ....:         '''
        ....:         pass
        ....:     def major_index(self):
        ....:         '''
        ....:         The major index of the permutation
        ....:         '''
        ....:         pass
        sage: MyPermutation.reverse
        Combinatorial map: reverse
        sage: MyPermutation.descent_set
        Combinatorial map: descent set of permutation
        sage: MyPermutation.inverse
        Combinatorial map: inverse

    One can now determine all the combinatorial maps associated with a
    given object as follows::

        sage: from sage.combinat.combinatorial_map import combinatorial_maps_in_class
        sage: X = combinatorial_maps_in_class(MyPermutation); X # random
        [Combinatorial map: reverse,
         Combinatorial map: descent set of permutation,
         Combinatorial map: inverse]

    The method ``major_index`` defined about is not a combinatorial map::

        sage: MyPermutation.major_index
        <function MyPermutation.major_index at ...>

    But one can define a function that turns ``major_index`` into a combinatorial map::

        sage: def major_index(p):
        ....:     return p.major_index()
        sage: major_index
        <function major_index at ...>
        sage: combinatorial_map(major_index)
        Combinatorial map: major_index
    """
combinatorial_map = combinatorial_map_trivial

class CombinatorialMap:
    """
    This is a wrapper class for methods that are *combinatorial maps*.

    For further details and doctests, see
    :ref:`sage.combinat.combinatorial_map` and
    :func:`combinatorial_map_wrapper`.
    """
    __doc__: Incomplete
    __module__: Incomplete
    def __init__(self, f, order=None, name=None) -> None:
        '''
        Constructor for combinatorial maps.

        EXAMPLES::

            sage: from sage.combinat.combinatorial_map import combinatorial_map_wrapper as combinatorial_map
            sage: def f(x):
            ....:     "doc of f"
            ....:     return x
            sage: x = combinatorial_map(f); x
            Combinatorial map: f
            sage: x.__doc__
            \'doc of f\'
            sage: x.__name__
            \'f\'
            sage: x.__module__
            \'__main__\'
        '''
    def __get__(self, inst, cls=None) -> Self:
        """
        Bounds the method of ``self`` to the given instance.

        EXAMPLES::

            sage: sage.combinat.combinatorial_map.combinatorial_map = sage.combinat.combinatorial_map.combinatorial_map_wrapper
            sage: from importlib import reload
            sage: _ = reload(sage.combinat.permutation)
            sage: p = Permutation([1,3,2,4])
            sage: p.left_tableau #indirect doctest
            Combinatorial map: Robinson-Schensted insertion tableau
        """
    def __call__(self, *args, **kwds):
        """
        Call the combinatorial map.

        EXAMPLES::

            sage: sage.combinat.combinatorial_map.combinatorial_map = sage.combinat.combinatorial_map.combinatorial_map_wrapper
            sage: from importlib import reload
            sage: _ = reload(sage.combinat.permutation)
            sage: p = Permutation([1,3,2,4])
            sage: cm = type(p).left_tableau; cm
            Combinatorial map: Robinson-Schensted insertion tableau
            sage: cm(p)                                                                 # needs sage.combinat
            [[1, 2, 4], [3]]
            sage: cm(Permutation([4,3,2,1]))                                            # needs sage.combinat
            [[1], [2], [3], [4]]
        """
    def unbounded_map(self):
        """
        Return the unbounded version of ``self``.

        You can use this method to return a function which takes as input
        an element in the domain of the combinatorial map.
        See the example below.

        EXAMPLES::

            sage: sage.combinat.combinatorial_map.combinatorial_map = sage.combinat.combinatorial_map.combinatorial_map_wrapper
            sage: from importlib import reload
            sage: _ = reload(sage.combinat.permutation)
            sage: from sage.combinat.permutation import Permutation
            sage: pi = Permutation([1,3,2])
            sage: f = pi.reverse
            sage: F = f.unbounded_map()
            sage: F(pi)
            [2, 3, 1]
        """
    def order(self):
        """
        Return the order of ``self``, or ``None`` if the order is not known.

        EXAMPLES::

            sage: from sage.combinat.combinatorial_map import combinatorial_map
            sage: class CombinatorialClass:
            ....:     @combinatorial_map(order=2)
            ....:     def to_self_1(): pass
            ....:     @combinatorial_map()
            ....:     def to_self_2(): pass
            sage: CombinatorialClass.to_self_1.order()
            2
            sage: CombinatorialClass.to_self_2.order() is None
            True
        """
    def name(self):
        """
        Return the name of a combinatorial map.
        This is used for the string representation of ``self``.

        EXAMPLES::

            sage: from sage.combinat.combinatorial_map import combinatorial_map
            sage: class CombinatorialClass:
            ....:     @combinatorial_map(name='map1')
            ....:     def to_self_1(): pass
            ....:     @combinatorial_map()
            ....:     def to_self_2(): pass
            sage: CombinatorialClass.to_self_1.name()
            'map1'
            sage: CombinatorialClass.to_self_2.name()
            'to_self_2'
        """

def combinatorial_maps_in_class(cls):
    """
    Return the combinatorial maps of the class as a list of combinatorial maps.

    For further details and doctests, see
    :ref:`sage.combinat.combinatorial_map` and
    :func:`combinatorial_map_wrapper`.

    EXAMPLES::

        sage: sage.combinat.combinatorial_map.combinatorial_map = sage.combinat.combinatorial_map.combinatorial_map_wrapper
        sage: from importlib import reload
        sage: _ = reload(sage.combinat.permutation)
        sage: from sage.combinat.combinatorial_map import combinatorial_maps_in_class
        sage: p = Permutation([1,3,2,4])
        sage: cmaps = combinatorial_maps_in_class(p)
        sage: cmaps # random
        [Combinatorial map: Robinson-Schensted insertion tableau,
         Combinatorial map: Robinson-Schensted recording tableau,
         Combinatorial map: Robinson-Schensted tableau shape,
         Combinatorial map: complement,
         Combinatorial map: descent composition,
         Combinatorial map: inverse, ...]
        sage: p.left_tableau in cmaps
        True
        sage: p.right_tableau in cmaps
        True
        sage: p.complement in cmaps
        True
    """
