import _cython_3_2_1
import sage.modules.free_module_element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_v0: _cython_3_2_1.cython_function_or_method

class Vector_mod2_dense(sage.modules.free_module_element.FreeModuleElement):
    """Vector_mod2_dense(parent, x, coerce=True, copy=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, coerce=..., copy=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 141)

                EXAMPLES::

                    sage: VS = VectorSpace(GF(2),3)
                    sage: VS((0,0,1/3))
                    (0, 0, 1)
                    sage: type(_)
                    <class 'sage.modules.vector_mod2_dense.Vector_mod2_dense'>
                    sage: VS((0,0,int(3)))
                    (0, 0, 1)
                    sage: VS((0,0,3))
                    (0, 0, 1)
                    sage: VS((0,0,GF(2)(1)))
                    (0, 0, 1)

                TESTS:

                Check that issue :issue:`8601` is fixed::

                    sage: VS = VectorSpace(GF(2), 3)
                    sage: VS((-1,-2,-3))
                    (1, 0, 1)
                    sage: V = VectorSpace(GF(2), 2)
                    sage: V([1,3])
                    (1, 1)
                    sage: V([1,-3])
                    (1, 1)

                Check integer overflow prior to :issue:`21746`::

                    sage: VS = VectorSpace(GF(2),1)
                    sage: VS([2**64])
                    (0)
                    sage: VS([3**100/5**100])
                    (1)

                Check division error over rationals::

                    sage: V = VectorSpace(GF(2), 2)
                    sage: V([1/3, 3/4])
                    Traceback (most recent call last):
                    ...
                    ZeroDivisionError: inverse does not exist

                Check zero initialization::

                    sage: for _ in range(1,100):
                    ....:     assert VectorSpace(GF(2), randint(1,5000))(0).is_zero()
                    sage: (GF(2)**5)(1)
                    Traceback (most recent call last):
                    ...
                    TypeError: can...t initialize vector from nonzero non-list
                    sage: (GF(2)**0).zero_vector()
                    ()

                Check construction from numpy arrays::

                    sage: # needs numpy
                    sage: import numpy
                    sage: VS = VectorSpace(GF(2),3)
                    sage: VS(numpy.array([0,-3,7], dtype=numpy.int8))
                    (0, 1, 1)
                    sage: VS(numpy.array([0,-3,7], dtype=numpy.int32))
                    (0, 1, 1)
                    sage: VS(numpy.array([0,-3,7], dtype=numpy.int64))
                    (0, 1, 1)
                    sage: VS(numpy.array([False,True,False], dtype=bool))
                    (0, 1, 0)
                    sage: VS(numpy.array([[1]]))
                    Traceback (most recent call last):
                    ...
                    ValueError: numpy array must have dimension 1
                    sage: VS(numpy.array([1,2,3,4]))
                    Traceback (most recent call last):
                    ...
                    ValueError: numpy array must have the right length

                Make sure it's reasonably fast::

                    sage: # needs numpy
                    sage: import numpy
                    sage: VS = VectorSpace(GF(2),2*10^7)
                    sage: v = VS(numpy.random.randint(0, 1, size=VS.dimension()))  # around 300ms
        """
    @overload
    def hamming_weight(self) -> int:
        """Vector_mod2_dense.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 371)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector(GF(2), [1,1,0]).hamming_weight()
            2"""
    @overload
    def hamming_weight(self) -> Any:
        """Vector_mod2_dense.hamming_weight(self) -> int

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 371)

        Return the number of positions ``i`` such that ``self[i] != 0``.

        EXAMPLES::

            sage: vector(GF(2), [1,1,0]).hamming_weight()
            2"""
    @overload
    def list(self, copy=...) -> Any:
        """Vector_mod2_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 496)

        Return a list of entries in ``self``.

        INPUT:

        - ``copy`` -- always ``True``

        EXAMPLES::

            sage: VS = VectorSpace(GF(2), 10)
            sage: entries = [GF(2).random_element() for _ in range(10)]
            sage: e = VS(entries)
            sage: e.list() == entries
            True"""
    @overload
    def list(self) -> Any:
        """Vector_mod2_dense.list(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 496)

        Return a list of entries in ``self``.

        INPUT:

        - ``copy`` -- always ``True``

        EXAMPLES::

            sage: VS = VectorSpace(GF(2), 10)
            sage: entries = [GF(2).random_element() for _ in range(10)]
            sage: e = VS(entries)
            sage: e.list() == entries
            True"""
    def __copy__(self) -> Any:
        """Vector_mod2_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 89)

        EXAMPLES::

            sage: VS = VectorSpace(GF(2),10^4)
            sage: v = VS.random_element()
            sage: w = copy(v)
            sage: w == v
            True
            sage: v[:10] == w[:10]
            True
            sage: v[5] += 1
            sage: v == w
            False"""
    def __reduce__(self) -> Any:
        """Vector_mod2_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modules/vector_mod2_dense.pyx (starting at line 329)

        EXAMPLES::

            sage: VS = VectorSpace(GF(2),10^4)
            sage: e = VS.random_element()
            sage: loads(dumps(e)) == e
            True"""
