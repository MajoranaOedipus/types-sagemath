import _cython_3_2_1
import sage.structure.list_clone
from sage.sets.set import Set_object_enumerated as Set_object_enumerated
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

FiniteSetMap_Set_from_dict: _cython_3_2_1.cython_function_or_method
FiniteSetMap_Set_from_list: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
fibers: _cython_3_2_1.cython_function_or_method
fibers_args: _cython_3_2_1.cython_function_or_method

class FiniteSetEndoMap_N(FiniteSetMap_MN):
    """File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 601)

        Map from ``range(n)`` to itself.

        .. SEEALSO:: :class:`FiniteSetMap_MN` for assumptions on the parent

        TESTS::

            sage: fs = FiniteSetMaps(3)([1, 0, 2])
            sage: TestSuite(fs).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __mul__(self, FiniteSetEndoMap_Nself, FiniteSetEndoMap_Nother) -> Any:
        """FiniteSetEndoMap_N.__mul__(FiniteSetEndoMap_N self, FiniteSetEndoMap_N other)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 613)

        TESTS::

            sage: F = FiniteSetMaps(3)
            sage: F([1, 0, 2]) * F([2, 1, 0])
            [2, 0, 1]
            sage: F = FiniteSetMaps(3, action='right')
            sage: F([1, 0, 2]) * F([2, 1, 0])
            [1, 2, 0]"""
    def __pow__(self, n, dummy) -> Any:
        """FiniteSetEndoMap_N.__pow__(self, n, dummy)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 629)

        Return the ``n``-th power of ``self``.

        INPUT:

        - ``n`` -- positive integer
        - ``dummy`` -- not used; must be set to ``None`` (for compatibility only)

        EXAMPLES::

            sage: fs = FiniteSetMaps(3)([1,0,2])
            sage: fs^2
            [0, 1, 2]
            sage: fs^0
            [0, 1, 2]
            sage: fs.__pow__(2)
            [0, 1, 2]"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class FiniteSetEndoMap_Set(FiniteSetMap_Set):
    '''File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 653)

        Map from a set to itself.

        .. SEEALSO:: :class:`FiniteSetMap_Set` for assumptions on the parent

        TESTS::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: f = F.from_dict({"a": "b", "b": "a", "c": "b"}); f
            map: a -> b, b -> a, c -> b
            sage: TestSuite(f).run()
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __mul__(self, FiniteSetEndoMap_Setself, FiniteSetEndoMap_Setother) -> Any:
        '''FiniteSetEndoMap_Set.__mul__(FiniteSetEndoMap_Set self, FiniteSetEndoMap_Set other)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 667)

        TESTS::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: f = F.from_dict({"a": "b", "b": "a", "c": "b"}); f
            map: a -> b, b -> a, c -> b
            sage: g = F.from_dict({"a": "c", "b": "c", "c": "a"}); g
            map: a -> c, b -> c, c -> a
            sage: f * g
            map: a -> b, b -> b, c -> b
            sage: g * f
            map: a -> c, b -> c, c -> c'''
    def __pow__(self, n, dummy) -> Any:
        '''FiniteSetEndoMap_Set.__pow__(self, n, dummy)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 686)

        Return the ``n``-th power of ``self``.

        INPUT:

        - ``n`` -- positive integer
        - ``dummy`` -- not used; must be set to None (for compatibility only)

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: f = F.from_dict({"a": "b", "b": "a", "c": "b"}); f
            map: a -> b, b -> a, c -> b
            sage: f^2
            map: a -> a, b -> b, c -> a
            sage: f^3 == f
            True'''
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class FiniteSetMap_MN(sage.structure.list_clone.ClonableIntArray):
    """File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 115)

        Data structure for maps from ``range(m)`` to ``range(n)``.

        We assume that the parent given as argument is such that:

        - ``m`` -- stored in ``self.parent()._m``
        - ``n`` -- stored in ``self.parent()._n``
        - the domain is in ``self.parent().domain()``
        - the codomain is in ``self.parent().codomain()``
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def check(self) -> Any:
        """FiniteSetMap_MN.check(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 332)

        Perform checks on ``self``.

        Check that ``self`` is a proper function and then calls
        ``parent.check_element(self)`` where ``parent`` is the parent
        of ``self``.

        TESTS::

            sage: fs = FiniteSetMaps(3, 2)
            sage: for el in fs: el.check()
            sage: fs([1,1])
            Traceback (most recent call last):
            ...
            AssertionError: Wrong number of values
            sage: fs([0,0,2])
            Traceback (most recent call last):
            ...
            AssertionError: Wrong value self(2) = 2"""
    @overload
    def check(self) -> Any:
        """FiniteSetMap_MN.check(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 332)

        Perform checks on ``self``.

        Check that ``self`` is a proper function and then calls
        ``parent.check_element(self)`` where ``parent`` is the parent
        of ``self``.

        TESTS::

            sage: fs = FiniteSetMaps(3, 2)
            sage: for el in fs: el.check()
            sage: fs([1,1])
            Traceback (most recent call last):
            ...
            AssertionError: Wrong number of values
            sage: fs([0,0,2])
            Traceback (most recent call last):
            ...
            AssertionError: Wrong value self(2) = 2"""
    @overload
    def codomain(self) -> Any:
        """FiniteSetMap_MN.codomain(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 169)

        Return the codomain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).codomain()
            {0, 1, 2}"""
    @overload
    def codomain(self) -> Any:
        """FiniteSetMap_MN.codomain(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 169)

        Return the codomain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).codomain()
            {0, 1, 2}"""
    @overload
    def domain(self) -> Any:
        """FiniteSetMap_MN.domain(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 158)

        Return the domain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).domain()
            {0, 1, 2, 3}"""
    @overload
    def domain(self) -> Any:
        """FiniteSetMap_MN.domain(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 158)

        Return the domain of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).domain()
            {0, 1, 2, 3}"""
    @overload
    def fibers(self) -> Any:
        '''FiniteSetMap_MN.fibers(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 300)

        Return the fibers of ``self``.

        OUTPUT:

            a dictionary ``d`` such that ``d[y]`` is the set of all ``x`` in
            ``domain`` such that ``f(x) = y``

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).fibers()
            {0: {1}, 1: {0, 3}, 2: {2}}
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).fibers() == {\'a\': {\'b\'}, \'b\': {\'a\', \'c\'}}
            True'''
    @overload
    def fibers(self) -> Any:
        '''FiniteSetMap_MN.fibers(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 300)

        Return the fibers of ``self``.

        OUTPUT:

            a dictionary ``d`` such that ``d[y]`` is the set of all ``x`` in
            ``domain`` such that ``f(x) = y``

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).fibers()
            {0: {1}, 1: {0, 3}, 2: {2}}
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).fibers() == {\'a\': {\'b\'}, \'b\': {\'a\', \'c\'}}
            True'''
    @overload
    def fibers(self) -> Any:
        '''FiniteSetMap_MN.fibers(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 300)

        Return the fibers of ``self``.

        OUTPUT:

            a dictionary ``d`` such that ``d[y]`` is the set of all ``x`` in
            ``domain`` such that ``f(x) = y``

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).fibers()
            {0: {1}, 1: {0, 3}, 2: {2}}
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).fibers() == {\'a\': {\'b\'}, \'b\': {\'a\', \'c\'}}
            True'''
    def getimage(self, i) -> Any:
        """FiniteSetMap_MN.getimage(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 269)

        Return the image of ``i`` by ``self``.

        INPUT:

        - ``i`` -- any object

        .. NOTE:: if you need speed, please use instead :meth:`_getimage`

        EXAMPLES::

            sage: fs = FiniteSetMaps(4, 3)([1, 0, 2, 1])
            sage: fs.getimage(0), fs.getimage(1), fs.getimage(2), fs.getimage(3)
            (1, 0, 2, 1)"""
    @overload
    def image_set(self) -> Any:
        """FiniteSetMap_MN.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 287)

        Return the image set of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).image_set()
            {0, 1, 2}
            sage: FiniteSetMaps(4, 3)([1, 0, 0, 1]).image_set()
            {0, 1}"""
    @overload
    def image_set(self) -> Any:
        """FiniteSetMap_MN.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 287)

        Return the image set of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).image_set()
            {0, 1, 2}
            sage: FiniteSetMaps(4, 3)([1, 0, 0, 1]).image_set()
            {0, 1}"""
    @overload
    def image_set(self) -> Any:
        """FiniteSetMap_MN.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 287)

        Return the image set of ``self``.

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).image_set()
            {0, 1, 2}
            sage: FiniteSetMaps(4, 3)([1, 0, 0, 1]).image_set()
            {0, 1}"""
    @overload
    def items(self) -> Any:
        """FiniteSetMap_MN.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 319)

        The items of ``self``.

        Return the list of the ordered pairs ``(x, self(x))``

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).items()
            [(0, 1), (1, 0), (2, 2), (3, 1)]"""
    @overload
    def items(self) -> Any:
        """FiniteSetMap_MN.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 319)

        The items of ``self``.

        Return the list of the ordered pairs ``(x, self(x))``

        EXAMPLES::

            sage: FiniteSetMaps(4, 3)([1, 0, 2, 1]).items()
            [(0, 1), (1, 0), (2, 2), (3, 1)]"""
    def setimage(self, i, j) -> Any:
        """FiniteSetMap_MN.setimage(self, i, j)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 240)

        Set the image of ``i`` as ``j`` in ``self``.

        .. warning:: ``self`` must be mutable; otherwise an exception is raised.

        INPUT:

        - ``i``, ``j`` -- two ``object``'s

        OUTPUT: none

        .. NOTE:: if you need speed, please use instead :meth:`_setimage`

        EXAMPLES::

            sage: fs = FiniteSetMaps(4, 3)([1, 0, 2, 1])
            sage: fs2 = copy(fs)
            sage: fs2.setimage(2, 1)
            sage: fs2
            [1, 0, 1, 1]
            sage: with fs.clone() as fs3:
            ....:     fs3.setimage(0, 2)
            ....:     fs3.setimage(1, 2)
            sage: fs3
            [2, 2, 2, 1]"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, inti) -> Any:
        """FiniteSetMap_MN.__call__(self, int i)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 127)

        Return the image of ``i`` under the map ``self``.

        INPUT:

        - ``i`` -- integer

        OUTPUT: integer

        EXAMPLES::

            sage: fs = FiniteSetMaps(4, 3)([1, 0, 2, 1])
            sage: fs(0), fs(1), fs(2), fs(3)
            (1, 0, 2, 1)"""

class FiniteSetMap_Set(FiniteSetMap_MN):
    """FiniteSetMap_Set(parent, fun, check=True)

    File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 431)

    Data structure for maps.

    We assume that the parent given as argument is such that:

    - the domain is in ``parent.domain()``
    - the codomain is in ``parent.codomain()``
    - ``parent._m`` contains the cardinality of the domain
    - ``parent._n`` contains the cardinality of the codomain
    - ``parent._unrank_domain`` and ``parent._rank_domain`` is a pair of
      reciprocal rank and unrank functions between the domain and
      ``range(parent._m)``.
    - ``parent._unrank_codomain`` and ``parent._rank_codomain`` is a pair of
      reciprocal rank and unrank functions between the codomain and
      ``range(parent._n)``."""
    from_dict: ClassVar[method] = ...
    from_list: ClassVar[method] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, fun, check=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 449)

                EXAMPLES::

                    sage: F = FiniteSetMaps(["a", "b", "c", "d"], ["u", "v", "w"])
                    sage: F(lambda x: "v")
                    map: a -> v, b -> v, c -> v, d -> v
        '''
    def getimage(self, i) -> Any:
        '''FiniteSetMap_Set.getimage(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 549)

        Return the image of ``i`` by ``self``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c", "d"], ["u", "v", "w"])
            sage: fs = F._from_list_([1, 0, 2, 1])
            sage: list(map(fs.getimage, ["a", "b", "c", "d"]))
            [\'v\', \'u\', \'w\', \'v\']'''
    @overload
    def image_set(self) -> Any:
        '''FiniteSetMap_Set.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 490)

        Return the image set of ``self``.

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: sorted(F.from_dict({"a": "b", "b": "a", "c": "b"}).image_set())
            [\'a\', \'b\']
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F(lambda x: "c").image_set()
            {\'c\'}'''
    @overload
    def image_set(self) -> Any:
        '''FiniteSetMap_Set.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 490)

        Return the image set of ``self``.

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: sorted(F.from_dict({"a": "b", "b": "a", "c": "b"}).image_set())
            [\'a\', \'b\']
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F(lambda x: "c").image_set()
            {\'c\'}'''
    @overload
    def image_set(self) -> Any:
        '''FiniteSetMap_Set.image_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 490)

        Return the image set of ``self``.

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: sorted(F.from_dict({"a": "b", "b": "a", "c": "b"}).image_set())
            [\'a\', \'b\']
            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F(lambda x: "c").image_set()
            {\'c\'}'''
    @overload
    def items(self) -> Any:
        '''FiniteSetMap_Set.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 567)

        The items of ``self``.

        Return the list of the couple ``(x, self(x))``

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).items()
            [(\'a\', \'b\'), (\'b\', \'a\'), (\'c\', \'b\')]

        TESTS::

            sage: all(F.from_dict(dict(f.items())) == f for f in F)
            True'''
    @overload
    def items(self) -> Any:
        '''FiniteSetMap_Set.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 567)

        The items of ``self``.

        Return the list of the couple ``(x, self(x))``

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).items()
            [(\'a\', \'b\'), (\'b\', \'a\'), (\'c\', \'b\')]

        TESTS::

            sage: all(F.from_dict(dict(f.items())) == f for f in F)
            True'''
    @overload
    def items(self) -> Any:
        '''FiniteSetMap_Set.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 567)

        The items of ``self``.

        Return the list of the couple ``(x, self(x))``

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c"])
            sage: F.from_dict({"a": "b", "b": "a", "c": "b"}).items()
            [(\'a\', \'b\'), (\'b\', \'a\'), (\'c\', \'b\')]

        TESTS::

            sage: all(F.from_dict(dict(f.items())) == f for f in F)
            True'''
    def setimage(self, i, j) -> Any:
        '''FiniteSetMap_Set.setimage(self, i, j)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 506)

        Set the image of ``i`` as ``j`` in ``self``.

        .. warning:: ``self`` must be mutable otherwise an exception is raised.

        INPUT:

        - ``i``, ``j`` -- two ``object``\'s

        OUTPUT: none

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b", "c", "d"], ["u", "v", "w"])
            sage: fs = F(lambda x: "v")
            sage: fs2 = copy(fs)
            sage: fs2.setimage("a", "w")
            sage: fs2
            map: a -> w, b -> v, c -> v, d -> v
            sage: with fs.clone() as fs3:
            ....:     fs3.setimage("a", "u")
            ....:     fs3.setimage("c", "w")
            sage: fs3
            map: a -> u, b -> v, c -> w, d -> v

        TESTS::

            sage: with fs.clone() as fs3:
            ....:     fs3.setimage("z", 2)
            Traceback (most recent call last):
            ...
            ValueError: \'z\' is not in dict

            sage: with fs.clone() as fs3:
            ....:     fs3.setimage(1, 4)
            Traceback (most recent call last):
            ...
            ValueError: 1 is not in dict'''
    def __call__(self, i) -> Any:
        '''FiniteSetMap_Set.__call__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/finite_set_map_cy.pyx (starting at line 470)

        Return the image of ``i`` under the map ``self``.

        INPUT:

        - ``i`` -- integer

        OUTPUT: integer

        EXAMPLES::

            sage: F = FiniteSetMaps(["a", "b"], [3, 4, 5])
            sage: fs = F.from_dict({"a": 3, "b": 5})
            sage: fs(\'a\'), fs(\'b\')
            (3, 5)'''
