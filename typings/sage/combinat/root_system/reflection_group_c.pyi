import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

iterator_tracking_words: _cython_3_2_1.cython_function_or_method
parabolic_iteration_application: _cython_3_2_1.cython_function_or_method
reduce_in_coset: _cython_3_2_1.cython_function_or_method
reduced_word_c: _cython_3_2_1.cython_function_or_method

class Iterator:
    """Iterator(W, int N, str algorithm='depth', bool tracking_words=True, order=None)

    File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 25)

    Iterator class for reflection groups."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, W, intN, stralgorithm=..., booltracking_words=..., order=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 67)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.combinat.root_system.reflection_group_c import Iterator
                    sage: W = ReflectionGroup(["B", 4])               # optional - gap3
                    sage: I = Iterator(W, W.number_of_reflections())  # optional - gap3
                    sage: TestSuite(I).run(skip=\'_test_pickling\')     # optional - gap3
        '''
    @overload
    def iter_breadth(self) -> Any:
        """Iterator.iter_breadth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 263)

        Iterate over ``self`` using breadth-first-search.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: list(I.iter_breadth())
            [(),
             (1,3)(2,6)(5,7),
             (1,5)(2,4)(6,8),
             (1,7,5,3)(2,4,6,8),
             (1,3,5,7)(2,8,6,4),
             (2,8)(3,7)(4,6),
             (1,7)(3,5)(4,8),
             (1,5)(2,6)(3,7)(4,8)]"""
    @overload
    def iter_breadth(self) -> Any:
        """Iterator.iter_breadth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 263)

        Iterate over ``self`` using breadth-first-search.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: list(I.iter_breadth())
            [(),
             (1,3)(2,6)(5,7),
             (1,5)(2,4)(6,8),
             (1,7,5,3)(2,4,6,8),
             (1,3,5,7)(2,8,6,4),
             (2,8)(3,7)(4,6),
             (1,7)(3,5)(4,8),
             (1,5)(2,6)(3,7)(4,8)]"""
    @overload
    def iter_depth(self) -> Any:
        """Iterator.iter_depth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 187)

        Iterate over ``self`` using depth-first-search.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: list(I.iter_depth())
            [(),
             (1,3)(2,6)(5,7),
             (1,5)(2,4)(6,8),
             (1,3,5,7)(2,8,6,4),
             (1,7)(3,5)(4,8),
             (1,7,5,3)(2,4,6,8),
             (2,8)(3,7)(4,6),
             (1,5)(2,6)(3,7)(4,8)]"""
    @overload
    def iter_depth(self) -> Any:
        """Iterator.iter_depth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 187)

        Iterate over ``self`` using depth-first-search.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: list(I.iter_depth())
            [(),
             (1,3)(2,6)(5,7),
             (1,5)(2,4)(6,8),
             (1,3,5,7)(2,8,6,4),
             (1,7)(3,5)(4,8),
             (1,7,5,3)(2,4,6,8),
             (2,8)(3,7)(4,6),
             (1,5)(2,6)(3,7)(4,8)]"""
    @overload
    def iter_parabolic(self) -> Any:
        """Iterator.iter_parabolic(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 338)

        This algorithm is an alternative to the one in *chevie* and about
        20% faster. It yields indeed all elements in the group rather than
        applying a given function.

        The output order is not deterministic.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: sorted(I.iter_parabolic())
            [(),
             (2,8)(3,7)(4,6),
             (1,3)(2,6)(5,7),
             (1,3,5,7)(2,8,6,4),
             (1,5)(2,4)(6,8),
             (1,5)(2,6)(3,7)(4,8),
             (1,7)(3,5)(4,8),
             (1,7,5,3)(2,4,6,8)]"""
    @overload
    def iter_parabolic(self) -> Any:
        """Iterator.iter_parabolic(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 338)

        This algorithm is an alternative to the one in *chevie* and about
        20% faster. It yields indeed all elements in the group rather than
        applying a given function.

        The output order is not deterministic.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: sorted(I.iter_parabolic())
            [(),
             (2,8)(3,7)(4,6),
             (1,3)(2,6)(5,7),
             (1,3,5,7)(2,8,6,4),
             (1,5)(2,4)(6,8),
             (1,5)(2,6)(3,7)(4,8),
             (1,7)(3,5)(4,8),
             (1,7,5,3)(2,4,6,8)]"""
    @overload
    def iter_words_breadth(self) -> Any:
        """Iterator.iter_words_breadth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 298)

        Iterate over ``self`` using breadth-first-search and setting
        the reduced word.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: for w in I.iter_words_breadth(): w._reduced_word
            []
            [1]
            [0]
            [0, 1]
            [1, 0]
            [1, 0, 1]
            [0, 1, 0]
            [0, 1, 0, 1]"""
    @overload
    def iter_words_breadth(self) -> Any:
        """Iterator.iter_words_breadth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 298)

        Iterate over ``self`` using breadth-first-search and setting
        the reduced word.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: for w in I.iter_words_breadth(): w._reduced_word
            []
            [1]
            [0]
            [0, 1]
            [1, 0]
            [1, 0, 1]
            [0, 1, 0]
            [0, 1, 0, 1]"""
    @overload
    def iter_words_depth(self) -> Any:
        """Iterator.iter_words_depth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 222)

        Iterate over ``self`` using depth-first-search and setting
        the reduced word.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: for w in I.iter_words_depth(): w._reduced_word
            []
            [1]
            [0]
            [1, 0]
            [0, 1, 0]
            [0, 1]
            [1, 0, 1]
            [0, 1, 0, 1]"""
    @overload
    def iter_words_depth(self) -> Any:
        """Iterator.iter_words_depth(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 222)

        Iterate over ``self`` using depth-first-search and setting
        the reduced word.

        EXAMPLES::

            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = CoxeterGroup(['B',2], implementation='permutation')
            sage: I = Iterator(W, W.number_of_reflections())
            sage: for w in I.iter_words_depth(): w._reduced_word
            []
            [1]
            [0]
            [1, 0]
            [0, 1, 0]
            [0, 1]
            [1, 0, 1]
            [0, 1, 0, 1]"""
    def __iter__(self) -> Any:
        '''Iterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_c.pyx (starting at line 152)

        EXAMPLES::

            sage: # optional - gap3
            sage: from sage.combinat.root_system.reflection_group_c import Iterator
            sage: W = ReflectionGroup(["B", 4])
            sage: N = W.number_of_reflections()
            sage: I = Iterator(W, N)
            sage: len(list(I)) == W.cardinality()
            True

            sage: # optional - gap3
            sage: I = Iterator(W, N, "breadth", False)
            sage: len(list(I)) == W.cardinality()
            True
            sage: I = Iterator(W, N, "parabolic")
            sage: len(list(I)) == W.cardinality()
            True'''
