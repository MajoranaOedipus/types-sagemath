import _cython_3_2_1
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass, typecall as typecall
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.dynamic_class import dynamic_class as dynamic_class
from typing import Any, overload

C3_merge: _cython_3_2_1.cython_function_or_method
C3_sorted_merge: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
identity: _cython_3_2_1.cython_function_or_method

class CmpKey:
    """CmpKey()

    File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 385)

    This class implements the lazy attribute ``Category._cmp_key``.

    The comparison key ``A._cmp_key`` of a category is used to define
    an (almost) total order on non-join categories by setting, for two
    categories `A` and `B`, `A<B` if ``A._cmp_key > B._cmp_key``. This
    order in turn is used to give a normal form to join's, and help
    toward having a consistent method resolution order for
    parent/element classes.

    The comparison key should satisfy the following properties:

    - If `A` is a subcategory of `B`, then `A < B` (so that
      ``A._cmp_key > B._cmp_key``). In particular,
      :class:`Objects() <Objects>` is the largest category.

    - If `A != B` and taking the join of `A` and `B` makes sense
      (e.g. taking the join of ``Algebras(GF(5))`` and
      ``Algebras(QQ)`` does not make sense), then `A<B` or `B<A`.

    The rationale for the inversion above between `A<B` and
    ``A._cmp_key > B._cmp_key`` is that we want the order to
    be compatible with inclusion of categories, yet it's easier in
    practice to create keys that get bigger and bigger while we go
    down the category hierarchy.

    This implementation applies to join-irreducible categories
    (i.e. categories that are not join categories). It returns a
    pair of integers ``(flags, i)``, where ``flags`` is to be
    interpreted as a bit vector. The first bit is set if ``self``
    is a facade set. The second bit is set if ``self`` is finite.
    And so on. The choice of the flags is adhoc and was primarily
    crafted so that the order between categories would not change
    too much upon integration of :issue:`13589` and would be
    reasonably session independent. The number ``i`` is there
    to resolve ambiguities; it is session dependent, and is
    assigned increasingly when new categories are created.

    .. NOTE::

        This is currently not implemented using a
        :class:`lazy_attribute` for speed reasons only (the code is in
        Cython and takes advantage of the fact that Category objects
        always have a ``__dict__`` dictionary)

    .. TODO::

        - Handle nicely (covariant) functorial constructions and axioms

    EXAMPLES::

        sage: Objects()._cmp_key
        (0, 0)
        sage: SetsWithPartialMaps()._cmp_key
        (0, 1)
        sage: Sets()._cmp_key
        (0, 2)
        sage: Sets().Facade()._cmp_key
        (1, ...)
        sage: Sets().Finite()._cmp_key
        (2, ...)
        sage: Sets().Infinite()._cmp_key
        (4, ...)
        sage: EnumeratedSets()._cmp_key
        (8, ...)
        sage: FiniteEnumeratedSets()._cmp_key
        (10, ...)
        sage: SetsWithGrading()._cmp_key
        (16, ...)
        sage: Posets()._cmp_key
        (32, ...)
        sage: LatticePosets()._cmp_key
        (96, ...)
        sage: Crystals()._cmp_key
        (136, ...)
        sage: AdditiveMagmas()._cmp_key
        (256, ...)
        sage: Magmas()._cmp_key
        (4096, ...)
        sage: CommutativeAdditiveSemigroups()._cmp_key
        (256, ...)
        sage: Rings()._cmp_key
        (225536, ...)
        sage: Algebras(QQ)._cmp_key
        (225536, ...)
        sage: AlgebrasWithBasis(QQ)._cmp_key
        (227584, ...)
        sage: GradedAlgebras(QQ)._cmp_key
        (226560, ...)
        sage: GradedAlgebrasWithBasis(QQ)._cmp_key
        (228608, ...)

    For backward compatibility we currently want the following comparisons::

        sage: EnumeratedSets()._cmp_key > Sets().Facade()._cmp_key
        True
        sage: AdditiveMagmas()._cmp_key > EnumeratedSets()._cmp_key
        True

        sage: Category.join([EnumeratedSets(), Sets().Facade()]).parent_class._an_element_.__module__
        'sage.categories.enumerated_sets'

        sage: CommutativeAdditiveSemigroups()._cmp_key < Magmas()._cmp_key
        True
        sage: VectorSpaces(QQ)._cmp_key < Rings()._cmp_key
        True
        sage: VectorSpaces(QQ)._cmp_key < Magmas()._cmp_key
        True"""
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 497)

                Set the internal category counter to zero.

                EXAMPLES::

                    sage: Objects()._cmp_key    # indirect doctest
                    (0, 0)
        """
    def __get__(self, inst, cls) -> Any:
        """CmpKey.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 508)

        Bind the comparison key to the given instance.

        EXAMPLES::

            sage: C = Algebras(FractionField(QQ['x']))
            sage: C._cmp_key
            (225536, ...)
            sage: '_cmp_key' in C.__dict__    # indirect doctest
            True"""

class CmpKeyNamed:
    """File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 534)

        This class implements the lazy attribute ``CategoryWithParameters._cmp_key``.

        .. SEEALSO::

            - :class:`CmpKey`
            - :class:`lazy_attribute`
            - :class:`sage.categories.category.CategoryWithParameters`.

        .. NOTE::

            - The value of the attribute depends only on the parameters of
              this category.

            - This is currently not implemented using a
              :class:`lazy_attribute` for speed reasons only.

        EXAMPLES::

            sage: Algebras(GF(3))._cmp_key == Algebras(GF(5))._cmp_key  # indirect doctest
            True
            sage: Algebras(ZZ)._cmp_key != Algebras(GF(5))._cmp_key
            True
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __get__(self, inst, cls) -> Any:
        """CmpKeyNamed.__get__(self, inst, cls)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 559)

        EXAMPLES::

            sage: Algebras(GF(3))._cmp_key == Algebras(GF(5))._cmp_key  # indirect doctest
            True
            sage: Algebras(ZZ)._cmp_key != Algebras(GF(5))._cmp_key
            True"""

class HierarchyElement:
    """File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 961)

        A class for elements in a hierarchy.

        This class is for testing and experimenting with various variants
        of the ``C3`` algorithm to compute a linear extension of the
        elements above an element in a hierarchy. Given the topic at hand,
        we use the following naming conventions. For `x` an element of the
        hierarchy, we call the elements just above `x` its *bases*, and
        the linear extension of all elements above `x` its *MRO*.

        By convention, the bases are given as lists of instances of
        :class:`HierarchyElement`, and MROs are given a list of the
        corresponding values.

        INPUT:

        - ``value`` -- an object
        - ``succ`` -- a successor function, poset or digraph from which
          one can recover the successors of ``value``
        - ``key`` -- a function taking values as input (default: the
          identity) this function is used to compute comparison keys for
          sorting elements of the hierarchy.

        .. NOTE::

            Constructing a :class:`HierarchyElement` immediately constructs the
            whole hierarchy above it.

        EXAMPLES:

        See the introduction of this module :mod:`sage.misc.c3_controlled`
        for many examples. Here we consider a large example, originally
        taken from the hierarchy of categories above
        :class:`HopfAlgebrasWithBasis`::

            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: G = DiGraph({                                                             # needs sage.graphs
            ....:     44 :  [43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     43 :  [42, 41, 40, 36, 35, 39, 38, 37, 33, 32, 31, 30, 29, 28, 27, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     42 :  [36, 35, 37, 30, 29, 28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     41 :  [40, 36, 35, 33, 32, 31, 30, 29, 28, 27, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     40 :  [36, 35, 32, 31, 30, 29, 28, 27, 26, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     39 :  [38, 37, 33, 32, 31, 30, 29, 28, 27, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     38 :  [37, 33, 32, 31, 30, 29, 28, 27, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     37 :  [30, 29, 28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     36 :  [35, 30, 29, 28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     35 :  [29, 28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     34 :  [33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     33 :  [32, 31, 30, 29, 28, 27, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     32 :  [31, 30, 29, 28, 27, 26, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     31 :  [30, 29, 28, 27, 26, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     30 :  [29, 28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     29 :  [28, 27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     28 :  [27, 26, 15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     27 :  [15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     26 :  [15, 14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     25 :  [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     24 :  [4, 2, 1, 0],
            ....:     23 :  [22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     22 :  [21, 20, 18, 17, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     21 :  [20, 17, 4, 2, 1, 0],
            ....:     20 :  [4, 2, 1, 0],
            ....:     19 :  [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     18 :  [17, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     17 :  [4, 2, 1, 0],
            ....:     16 :  [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     15 :  [14, 12, 11, 9, 8, 5, 3, 2, 1, 0],
            ....:     14 :  [11, 3, 2, 1, 0],
            ....:     13 :  [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     12 :  [11, 9, 8, 5, 3, 2, 1, 0],
            ....:     11 :  [3, 2, 1, 0],
            ....:     10 :  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ....:     9 :  [8, 5, 3, 2, 1, 0],
            ....:     8 :  [3, 2, 1, 0],
            ....:     7 :  [6, 5, 4, 3, 2, 1, 0],
            ....:     6 :  [4, 3, 2, 1, 0],
            ....:     5 :  [3, 2, 1, 0],
            ....:     4 :  [2, 1, 0],
            ....:     3 :  [2, 1, 0],
            ....:     2 :  [1, 0],
            ....:     1 :  [0],
            ....:     0 :  [],
            ....:     })

            sage: # needs sage.combinat sage.graphs
            sage: x = HierarchyElement(44, G)
            sage: x.mro
            [44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            sage: x.cls
            <class '44.cls'>
            sage: x.cls.mro()
            [<class '44.cls'>, <class '43.cls'>, <class '42.cls'>, <class '41.cls'>, <class '40.cls'>, <class '39.cls'>, <class '38.cls'>, <class '37.cls'>, <class '36.cls'>, <class '35.cls'>, <class '34.cls'>, <class '33.cls'>, <class '32.cls'>, <class '31.cls'>, <class '30.cls'>, <class '29.cls'>, <class '28.cls'>, <class '27.cls'>, <class '26.cls'>, <class '25.cls'>, <class '24.cls'>, <class '23.cls'>, <class '22.cls'>, <class '21.cls'>, <class '20.cls'>, <class '19.cls'>, <class '18.cls'>, <class '17.cls'>, <class '16.cls'>, <class '15.cls'>, <class '14.cls'>, <class '13.cls'>, <class '12.cls'>, <class '11.cls'>, <class '10.cls'>, <class '9.cls'>, <class '8.cls'>, <class '7.cls'>, <class '6.cls'>, <class '5.cls'>, <class '4.cls'>, <class '3.cls'>, <class '2.cls'>, <class '1.cls'>, <class '0.cls'>, <... 'object'>]
    """
    def __init__(self, value, bases, key, from_value) -> Any:
        """HierarchyElement.__init__(self, value, bases, key, from_value)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1101)

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: x = HierarchyElement(10, P)
            sage: x
            10
            sage: x.value
            10
            sage: x._bases
            [5, 2]
            sage: x._key
            <cyfunction identity at ...>
            sage: x._key(10)
            10

        The ``_from_value`` attribute is a function that can be used
        to reconstruct an element of the hierarchy from its value::

            sage: x._from_value                                                         # needs sage.graphs
            Cached version of <...__classcall__...>
            sage: x._from_value(x.value) is x                                           # needs sage.graphs
            True"""
    @overload
    def all_bases(self) -> Any:
        """HierarchyElement.all_bases(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1358)

        Return the set of all instances of :class:`HierarchyElement` above
        ``self``, ``self`` included.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: HierarchyElement(1, P).all_bases()
            {1}
            sage: HierarchyElement(10, P).all_bases()  # random output
            {10, 5, 2, 1}
            sage: sorted([x.value for x in HierarchyElement(10, P).all_bases()])
            [1, 2, 5, 10]"""
    @overload
    def all_bases(self) -> Any:
        """HierarchyElement.all_bases(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1358)

        Return the set of all instances of :class:`HierarchyElement` above
        ``self``, ``self`` included.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: HierarchyElement(1, P).all_bases()
            {1}
            sage: HierarchyElement(10, P).all_bases()  # random output
            {10, 5, 2, 1}
            sage: sorted([x.value for x in HierarchyElement(10, P).all_bases()])
            [1, 2, 5, 10]"""
    @overload
    def all_bases(self) -> Any:
        """HierarchyElement.all_bases(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1358)

        Return the set of all instances of :class:`HierarchyElement` above
        ``self``, ``self`` included.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: HierarchyElement(1, P).all_bases()
            {1}
            sage: HierarchyElement(10, P).all_bases()  # random output
            {10, 5, 2, 1}
            sage: sorted([x.value for x in HierarchyElement(10, P).all_bases()])
            [1, 2, 5, 10]"""
    @overload
    def all_bases(self) -> Any:
        """HierarchyElement.all_bases(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1358)

        Return the set of all instances of :class:`HierarchyElement` above
        ``self``, ``self`` included.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: HierarchyElement(1, P).all_bases()
            {1}
            sage: HierarchyElement(10, P).all_bases()  # random output
            {10, 5, 2, 1}
            sage: sorted([x.value for x in HierarchyElement(10, P).all_bases()])
            [1, 2, 5, 10]"""
    @overload
    def all_bases_controlled_len(self) -> Any:
        """HierarchyElement.all_bases_controlled_len(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1391)

        Return the cumulated size of the controlled bases of the elements above ``self`` in the hierarchy.

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)     # needs sage.graphs
            sage: HierarchyElement(30, P).all_bases_controlled_len()                    # needs sage.graphs
            13"""
    @overload
    def all_bases_controlled_len(self) -> Any:
        """HierarchyElement.all_bases_controlled_len(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1391)

        Return the cumulated size of the controlled bases of the elements above ``self`` in the hierarchy.

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)     # needs sage.graphs
            sage: HierarchyElement(30, P).all_bases_controlled_len()                    # needs sage.graphs
            13"""
    @overload
    def all_bases_len(self) -> Any:
        """HierarchyElement.all_bases_len(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1378)

        Return the cumulated size of the bases of the elements above ``self`` in the hierarchy.

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)     # needs sage.graphs
            sage: HierarchyElement(30, P).all_bases_len()                               # needs sage.graphs
            12"""
    @overload
    def all_bases_len(self) -> Any:
        """HierarchyElement.all_bases_len(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1378)

        Return the cumulated size of the bases of the elements above ``self`` in the hierarchy.

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)     # needs sage.graphs
            sage: HierarchyElement(30, P).all_bases_len()                               # needs sage.graphs
            12"""
    def bases(self) -> Any:
        """HierarchyElement.bases(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1147)

        The bases of ``self``.

        The bases are given as a list of instances of
        :class:`HierarchyElement`, sorted decreasingly according to
        the ``key`` function.

        EXAMPLES::

            sage: # needs sage.combinat sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: x = HierarchyElement(10, P)
            sage: x.bases
            [5, 2]
            sage: type(x.bases[0])
            <class 'sage.misc.c3_controlled.HierarchyElement'>
            sage: x.mro
            [10, 5, 2, 1]
            sage: x._bases_controlled
            [5, 2]"""
    def cls(self) -> Any:
        """HierarchyElement.cls(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1332)

        Return a Python class with inheritance graph parallel to the hierarchy above ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: x = HierarchyElement(1, P)
            sage: x.cls
            <class '1.cls'>
            sage: x.cls.mro()
            [<class '1.cls'>, <... 'object'>]
            sage: x = HierarchyElement(30, P)
            sage: x.cls
            <class '30.cls'>
            sage: x.cls.mro()
            [<class '30.cls'>, <class '15.cls'>, <class '10.cls'>, <class '6.cls'>, <class '5.cls'>, <class '3.cls'>, <class '2.cls'>, <class '1.cls'>, <... 'object'>]"""
    def mro(self) -> Any:
        """HierarchyElement.mro(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1173)

        The MRO for this object, calculated with :meth:`C3_sorted_merge`.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement, C3_sorted_merge, identity
            sage: P = Poset({7: [5, 6], 5: [1, 2], 6: [3, 4]}, facade=True)
            sage: x = HierarchyElement(5, P)
            sage: x.mro
            [5, 2, 1]
            sage: x = HierarchyElement(6, P)
            sage: x.mro
            [6, 4, 3]
            sage: x = HierarchyElement(7, P)
            sage: x.mro
            [7, 6, 5, 4, 3, 2, 1]

            sage: C3_sorted_merge([[6, 4, 3], [5, 2, 1], [6, 5]], identity)             # needs sage.graphs
            ([6, 5, 4, 3, 2, 1], [6, 5, 4])

        TESTS::

            sage: assert all(isinstance(v, Integer) for v in x.mro)                     # needs sage.graphs"""
    def mro_controlled(self) -> Any:
        """HierarchyElement.mro_controlled(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1260)

        The MRO for this object, calculated with :meth:`C3_merge`, under
        control of :func:`C3_sorted_merge`

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement, C3_merge

            sage: # needs sage.graphs
            sage: P = Poset({7: [5, 6], 5: [1, 2], 6: [3, 4]}, facade=True)
            sage: x = HierarchyElement(5, P)
            sage: x.mro_controlled
            [5, 2, 1]
            sage: x = HierarchyElement(6, P)
            sage: x.mro_controlled
            [6, 4, 3]
            sage: x = HierarchyElement(7, P)
            sage: x.mro_controlled
            [7, 6, 5, 4, 3, 2, 1]
            sage: x._bases
            [6, 5]
            sage: x._bases_controlled
            [6, 5, 4]

            sage: C3_merge([[6, 4, 3], [5, 2, 1], [6, 5]])
            [6, 4, 3, 5, 2, 1]
            sage: C3_merge([[6, 4, 3], [5, 2, 1], [6, 5, 4]])
            [6, 5, 4, 3, 2, 1]

        TESTS::

            sage: assert all(isinstance(v, Integer) for v in x.mro_controlled)          # needs sage.graphs"""
    def mro_standard(self) -> Any:
        """HierarchyElement.mro_standard(self)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1229)

        The MRO for this object, calculated with :meth:`C3_merge`.

        EXAMPLES::

            sage: from sage.misc.c3_controlled import HierarchyElement, C3_merge

            sage: # needs sage.graphs
            sage: P = Poset({7: [5, 6], 5: [1, 2], 6: [3, 4]}, facade=True)
            sage: x = HierarchyElement(5, P)
            sage: x.mro_standard
            [5, 2, 1]
            sage: x = HierarchyElement(6, P)
            sage: x.mro_standard
            [6, 4, 3]
            sage: x = HierarchyElement(7, P)
            sage: x.mro_standard
            [7, 6, 4, 3, 5, 2, 1]

            sage: C3_merge([[6, 4, 3], [5, 2, 1], [6, 5]])
            [6, 4, 3, 5, 2, 1]

        TESTS::

            sage: assert all(isinstance(v, Integer) for v in x.mro_standard)            # needs sage.graphs"""
    @staticmethod
    def __classcall__(cls, value, succ, key=...) -> Any:
        """HierarchyElement.__classcall__(cls, value, succ, key=None)

        File: /build/sagemath/src/sage/src/sage/misc/c3_controlled.pyx (starting at line 1055)

        EXAMPLES::

            sage: # needs sage.combinat sage.graphs
            sage: from sage.misc.c3_controlled import HierarchyElement
            sage: P = Poset((divisors(30), lambda x, y: y.divides(x)), facade=True)
            sage: x = HierarchyElement(10, P)
            sage: x
            10
            sage: x.bases
            [5, 2]
            sage: x.mro
            [10, 5, 2, 1]"""
