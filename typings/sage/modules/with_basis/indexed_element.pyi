import sage.structure.element
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.misc.superseded import deprecation as deprecation
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.typeset.ascii_art import AsciiArt as AsciiArt, ascii_art as ascii_art, empty_ascii_art as empty_ascii_art
from sage.typeset.unicode_art import UnicodeArt as UnicodeArt, empty_unicode_art as empty_unicode_art, unicode_art as unicode_art
from typing import Any, ClassVar, overload

class IndexedFreeModuleElement(sage.structure.element.ModuleElement):
    """IndexedFreeModuleElement(M, x)

    File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 32)

    Element class for :class:`~sage.combinat.free_module.CombinatorialFreeModule`.

    TESTS::

        sage: import collections.abc
        sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
        sage: B = F.basis()
        sage: f = B['a'] + 3*B['c']; f
        B['a'] + 3*B['c']
        sage: isinstance(f, collections.abc.Sized)
        True
        sage: isinstance(f, collections.abc.Iterable)
        True
        sage: isinstance(f, collections.abc.Collection)  # known bug - will be fixed by removing __contains__
        False"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, M, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 50)

                Create a combinatorial module element.

                This should never be called directly, but only through the
                parent combinatorial free module's :meth:`__call__` method.

                TESTS::

                    sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
                    sage: B = F.basis()
                    sage: f = B['a'] + 3*B['c']; f
                    B['a'] + 3*B['c']
                    sage: f == loads(dumps(f))
                    True
        """
    @overload
    def monomial_coefficients(self, boolcopy=...) -> dict:
        '''IndexedFreeModuleElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 230)

        Return the internal dictionary which has the combinatorial objects
        indexing the basis as keys and their corresponding coefficients as
        values.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, [\'a\',\'b\',\'c\'])
            sage: B = F.basis()
            sage: f = B[\'a\'] + 3*B[\'c\']
            sage: d = f.monomial_coefficients()
            sage: d[\'a\']
            1
            sage: d[\'c\']
            3

        To run through the monomials of an element, it is better to
        use the idiom::

            sage: for (t,c) in f:
            ....:     print("{} {}".format(t,c))
            a 1
            c 3

        ::

            sage: # needs sage.combinat
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a = s([2,1])+2*s([3,2])
            sage: d = a.monomial_coefficients()
            sage: type(d)
            <... \'dict\'>
            sage: d[ Partition([2,1]) ]
            1
            sage: d[ Partition([3,2]) ]
            2'''
    @overload
    def monomial_coefficients(self) -> Any:
        '''IndexedFreeModuleElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 230)

        Return the internal dictionary which has the combinatorial objects
        indexing the basis as keys and their corresponding coefficients as
        values.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, [\'a\',\'b\',\'c\'])
            sage: B = F.basis()
            sage: f = B[\'a\'] + 3*B[\'c\']
            sage: d = f.monomial_coefficients()
            sage: d[\'a\']
            1
            sage: d[\'c\']
            3

        To run through the monomials of an element, it is better to
        use the idiom::

            sage: for (t,c) in f:
            ....:     print("{} {}".format(t,c))
            a 1
            c 3

        ::

            sage: # needs sage.combinat
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a = s([2,1])+2*s([3,2])
            sage: d = a.monomial_coefficients()
            sage: type(d)
            <... \'dict\'>
            sage: d[ Partition([2,1]) ]
            1
            sage: d[ Partition([3,2]) ]
            2'''
    @overload
    def monomial_coefficients(self) -> Any:
        '''IndexedFreeModuleElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 230)

        Return the internal dictionary which has the combinatorial objects
        indexing the basis as keys and their corresponding coefficients as
        values.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``.
          If ``False``, then this can cause undesired behavior by
          mutating ``d``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, [\'a\',\'b\',\'c\'])
            sage: B = F.basis()
            sage: f = B[\'a\'] + 3*B[\'c\']
            sage: d = f.monomial_coefficients()
            sage: d[\'a\']
            1
            sage: d[\'c\']
            3

        To run through the monomials of an element, it is better to
        use the idiom::

            sage: for (t,c) in f:
            ....:     print("{} {}".format(t,c))
            a 1
            c 3

        ::

            sage: # needs sage.combinat
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a = s([2,1])+2*s([3,2])
            sage: d = a.monomial_coefficients()
            sage: type(d)
            <... \'dict\'>
            sage: d[ Partition([2,1]) ]
            1
            sage: d[ Partition([3,2]) ]
            2'''
    @overload
    def to_vector(self) -> Any:
        """IndexedFreeModuleElement._vector_(self, new_base_ring=None, order=None, sparse=False)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 780)

        Return ``self`` as a vector.

        INPUT:

        - ``new_base_ring`` -- a ring (default: ``None``)
        - ``order`` -- (optional) an ordering of the support of ``self``
        - ``sparse`` -- boolean (default: ``False``); whether to return a sparse
          vector or a dense vector

        OUTPUT: a :func:`FreeModule` vector

        .. WARNING:: This will crash/run forever if ``self`` is infinite dimensional!

        .. SEEALSO::

            - :func:`vector`
            - :meth:`CombinatorialFreeModule.get_order`
            - :meth:`CombinatorialFreeModule.from_vector`
            - :meth:`CombinatorialFreeModule._dense_free_module`

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] - 3*B['c']
            sage: f._vector_()
            (1, 0, -3)

        One can use equivalently::

            sage: f.to_vector()
            (1, 0, -3)
            sage: vector(f)
            (1, 0, -3)

        More examples::

            sage: # needs sage.combinat
            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = 2*QS3([1,2,3]) + 4*QS3([3,2,1])
            sage: a._vector_()
            (2, 0, 0, 0, 0, 4)
            sage: a.to_vector()
            (2, 0, 0, 0, 0, 4)
            sage: vector(a)
            (2, 0, 0, 0, 0, 4)
            sage: a == QS3.from_vector(a.to_vector())
            True
            sage: a.to_vector(sparse=True)
            (2, 0, 0, 0, 0, 4)

        If ``new_base_ring`` is specified, then a vector over
        ``new_base_ring`` is returned::

            sage: a._vector_(RDF)                                                       # needs sage.combinat
            (2.0, 0.0, 0.0, 0.0, 0.0, 4.0)

        .. NOTE::

            :issue:`13406`: the current implementation has been optimized, at
            the price of breaking the encapsulation for FreeModule
            elements creation, with the following use case as metric,
            on a 2008' Macbook Pro::

                sage: F = CombinatorialFreeModule(QQ, range(10))
                sage: f = F.an_element()
                sage: %timeit f._vector_()   # not tested
                625 loops, best of 3: 17.5 micros per loop

             Other use cases may call for different or further
             optimizations."""
    @overload
    def to_vector(self) -> Any:
        """IndexedFreeModuleElement._vector_(self, new_base_ring=None, order=None, sparse=False)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 780)

        Return ``self`` as a vector.

        INPUT:

        - ``new_base_ring`` -- a ring (default: ``None``)
        - ``order`` -- (optional) an ordering of the support of ``self``
        - ``sparse`` -- boolean (default: ``False``); whether to return a sparse
          vector or a dense vector

        OUTPUT: a :func:`FreeModule` vector

        .. WARNING:: This will crash/run forever if ``self`` is infinite dimensional!

        .. SEEALSO::

            - :func:`vector`
            - :meth:`CombinatorialFreeModule.get_order`
            - :meth:`CombinatorialFreeModule.from_vector`
            - :meth:`CombinatorialFreeModule._dense_free_module`

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] - 3*B['c']
            sage: f._vector_()
            (1, 0, -3)

        One can use equivalently::

            sage: f.to_vector()
            (1, 0, -3)
            sage: vector(f)
            (1, 0, -3)

        More examples::

            sage: # needs sage.combinat
            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = 2*QS3([1,2,3]) + 4*QS3([3,2,1])
            sage: a._vector_()
            (2, 0, 0, 0, 0, 4)
            sage: a.to_vector()
            (2, 0, 0, 0, 0, 4)
            sage: vector(a)
            (2, 0, 0, 0, 0, 4)
            sage: a == QS3.from_vector(a.to_vector())
            True
            sage: a.to_vector(sparse=True)
            (2, 0, 0, 0, 0, 4)

        If ``new_base_ring`` is specified, then a vector over
        ``new_base_ring`` is returned::

            sage: a._vector_(RDF)                                                       # needs sage.combinat
            (2.0, 0.0, 0.0, 0.0, 0.0, 4.0)

        .. NOTE::

            :issue:`13406`: the current implementation has been optimized, at
            the price of breaking the encapsulation for FreeModule
            elements creation, with the following use case as metric,
            on a 2008' Macbook Pro::

                sage: F = CombinatorialFreeModule(QQ, range(10))
                sage: f = F.an_element()
                sage: %timeit f._vector_()   # not tested
                625 loops, best of 3: 17.5 micros per loop

             Other use cases may call for different or further
             optimizations."""
    @overload
    def to_vector(self) -> Any:
        """IndexedFreeModuleElement._vector_(self, new_base_ring=None, order=None, sparse=False)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 780)

        Return ``self`` as a vector.

        INPUT:

        - ``new_base_ring`` -- a ring (default: ``None``)
        - ``order`` -- (optional) an ordering of the support of ``self``
        - ``sparse`` -- boolean (default: ``False``); whether to return a sparse
          vector or a dense vector

        OUTPUT: a :func:`FreeModule` vector

        .. WARNING:: This will crash/run forever if ``self`` is infinite dimensional!

        .. SEEALSO::

            - :func:`vector`
            - :meth:`CombinatorialFreeModule.get_order`
            - :meth:`CombinatorialFreeModule.from_vector`
            - :meth:`CombinatorialFreeModule._dense_free_module`

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] - 3*B['c']
            sage: f._vector_()
            (1, 0, -3)

        One can use equivalently::

            sage: f.to_vector()
            (1, 0, -3)
            sage: vector(f)
            (1, 0, -3)

        More examples::

            sage: # needs sage.combinat
            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = 2*QS3([1,2,3]) + 4*QS3([3,2,1])
            sage: a._vector_()
            (2, 0, 0, 0, 0, 4)
            sage: a.to_vector()
            (2, 0, 0, 0, 0, 4)
            sage: vector(a)
            (2, 0, 0, 0, 0, 4)
            sage: a == QS3.from_vector(a.to_vector())
            True
            sage: a.to_vector(sparse=True)
            (2, 0, 0, 0, 0, 4)

        If ``new_base_ring`` is specified, then a vector over
        ``new_base_ring`` is returned::

            sage: a._vector_(RDF)                                                       # needs sage.combinat
            (2.0, 0.0, 0.0, 0.0, 0.0, 4.0)

        .. NOTE::

            :issue:`13406`: the current implementation has been optimized, at
            the price of breaking the encapsulation for FreeModule
            elements creation, with the following use case as metric,
            on a 2008' Macbook Pro::

                sage: F = CombinatorialFreeModule(QQ, range(10))
                sage: f = F.an_element()
                sage: %timeit f._vector_()   # not tested
                625 loops, best of 3: 17.5 micros per loop

             Other use cases may call for different or further
             optimizations."""
    @overload
    def to_vector(self, sparse=...) -> Any:
        """IndexedFreeModuleElement._vector_(self, new_base_ring=None, order=None, sparse=False)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 780)

        Return ``self`` as a vector.

        INPUT:

        - ``new_base_ring`` -- a ring (default: ``None``)
        - ``order`` -- (optional) an ordering of the support of ``self``
        - ``sparse`` -- boolean (default: ``False``); whether to return a sparse
          vector or a dense vector

        OUTPUT: a :func:`FreeModule` vector

        .. WARNING:: This will crash/run forever if ``self`` is infinite dimensional!

        .. SEEALSO::

            - :func:`vector`
            - :meth:`CombinatorialFreeModule.get_order`
            - :meth:`CombinatorialFreeModule.from_vector`
            - :meth:`CombinatorialFreeModule._dense_free_module`

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] - 3*B['c']
            sage: f._vector_()
            (1, 0, -3)

        One can use equivalently::

            sage: f.to_vector()
            (1, 0, -3)
            sage: vector(f)
            (1, 0, -3)

        More examples::

            sage: # needs sage.combinat
            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = 2*QS3([1,2,3]) + 4*QS3([3,2,1])
            sage: a._vector_()
            (2, 0, 0, 0, 0, 4)
            sage: a.to_vector()
            (2, 0, 0, 0, 0, 4)
            sage: vector(a)
            (2, 0, 0, 0, 0, 4)
            sage: a == QS3.from_vector(a.to_vector())
            True
            sage: a.to_vector(sparse=True)
            (2, 0, 0, 0, 0, 4)

        If ``new_base_ring`` is specified, then a vector over
        ``new_base_ring`` is returned::

            sage: a._vector_(RDF)                                                       # needs sage.combinat
            (2.0, 0.0, 0.0, 0.0, 0.0, 4.0)

        .. NOTE::

            :issue:`13406`: the current implementation has been optimized, at
            the price of breaking the encapsulation for FreeModule
            elements creation, with the following use case as metric,
            on a 2008' Macbook Pro::

                sage: F = CombinatorialFreeModule(QQ, range(10))
                sage: f = F.an_element()
                sage: %timeit f._vector_()   # not tested
                625 loops, best of 3: 17.5 micros per loop

             Other use cases may call for different or further
             optimizations."""
    def __contains__(self, x) -> Any:
        """IndexedFreeModuleElement.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 87)

        Return whether or not a combinatorial object ``x`` indexing a basis
        element is in the support of ``self``.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] + 3*B['c']
            sage: 'a' in f
            doctest:warning...
            DeprecationWarning: using 'index in vector' is deprecated; use 'index in vector.support()' instead
            See https://github.com/sagemath/sage/issues/34509 for details.
            True
            sage: 'b' in f
            False

            sage: # needs sage.combinat
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a = s([2,1]) + s([3])
            sage: Partition([2,1]) in a
            True
            sage: Partition([1,1,1]) in a
            False"""
    def __copy__(self) -> Any:
        """IndexedFreeModuleElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 204)

        Return ``self`` since ``self`` is immutable.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: x = F.an_element()
            sage: copy(x) is x
            True"""
    def __deepcopy__(self, memo=...) -> Any:
        """IndexedFreeModuleElement.__deepcopy__(self, memo=None)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 217)

        Return ``self`` since ``self`` is immutable.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: x = F.an_element()
            sage: deepcopy(x) is x
            True"""
    def __getitem__(self, m) -> Any:
        """IndexedFreeModuleElement.__getitem__(self, m)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 755)

        Return the coefficient of ``m`` in ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: p = Partition([2,1])
            sage: q = Partition([1,1,1])
            sage: s = SymmetricFunctions(QQ).schur()
            sage: a = s(p)
            sage: a[p]
            1
            sage: a[q]
            0
            sage: a[[2,1]]
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'list'"""
    def __hash__(self) -> Any:
        """IndexedFreeModuleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 116)

        Return the hash value for ``self``.

        The result is cached.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] + 3*B['c']
            sage: hash(f) == hash(B['a'] + 3*B['c'])
            True
            sage: hash(f) == hash(B['a'] + 4*B['c'])
            False

            sage: # needs sage.combinat
            sage: F = RootSystem(['A',2]).ambient_space()
            sage: f = F.simple_root(0)
            sage: hash(f) == hash(F.simple_root(0))
            True
            sage: hash(f) == hash(F.simple_root(1))
            False

        This uses the recipe that was proposed for frozendicts in
        :pep:`416` (and adds the hash of the parent). This recipe
        relies on the hash function for frozensets which uses tricks
        to mix the hash values of the items in case they are similar.

        .. TODO::

            It would be desirable to make the hash value depend on the
            hash value of the parent. See :issue:`15959`."""
    def __iter__(self) -> Any:
        """IndexedFreeModuleElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 70)

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: B = F.basis()
            sage: f = B['a'] + 3*B['c']
            sage: [i for i in sorted(f)]
            [('a', 1), ('c', 3)]

            sage: s = SymmetricFunctions(QQ).schur()                                    # needs sage.combinat
            sage: a = s([2,1]) + s([3])                                                 # needs sage.combinat
            sage: [i for i in sorted(a)]                                                # needs sage.combinat
            [([2, 1], 1), ([3], 1)]"""
    def __reduce__(self) -> Any:
        """IndexedFreeModuleElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 155)

        For pickling.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, ['a','b','c'])
            sage: loads(dumps(F.an_element())) == F.an_element()
            True"""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, left, x) -> Any:
        '''IndexedFreeModuleElement.__truediv__(left, x)

        File: /build/sagemath/src/sage/src/sage/modules/with_basis/indexed_element.pyx (starting at line 972)

        Division by coefficients.

        EXAMPLES::

            sage: F = CombinatorialFreeModule(QQ, [1,2,3])
            sage: x = F._from_dict({1:2, 2:3})
            sage: from operator import truediv
            sage: truediv(x, 2)
            B[1] + 3/2*B[2]

        ::

            sage: F = CombinatorialFreeModule(QQ, [1,2,3])
            sage: B = F.basis()
            sage: f = 2*B[2] + 4*B[3]
            sage: truediv(f, 2)
            B[2] + 2*B[3]

        TESTS::

            sage: truediv(x, x)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2*B[1] + 3*B[2] to a rational
            sage: truediv("hello", x)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for /: \'str\' and \'CombinatorialFreeModule_with_category.element_class\'

            sage: L = LazyPowerSeriesRing(QQ, \'t\')
            sage: t = L.gen()
            sage: F = algebras.Free(L, [\'A\', \'B\'])
            sage: A, B = F.gens()
            sage: f = t*A + t**2*B/2'''
