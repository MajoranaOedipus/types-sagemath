import _cython_3_2_1
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.groups.matrix_gps.group_element_gap import MatrixGroupElement_gap as MatrixGroupElement_gap
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
is_MatrixGroupElement: _cython_3_2_1.cython_function_or_method

class MatrixGroupElement_generic(sage.structure.element.MultiplicativeGroupElement):
    """MatrixGroupElement_generic(parent, M, check=True, convert=True)

    File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 118)

    Element of a matrix group over a generic ring.

    The group elements are implemented as Sage matrices.

    INPUT:

    - ``M`` -- a matrix

    - ``parent`` -- the parent

    - ``check`` -- boolean (default: ``True``); if ``True``, then
      do some type checking

    - ``convert`` -- boolean (default: ``True``); if ``True``, then
      convert ``M`` to the right matrix space

    EXAMPLES::

        sage: W = CoxeterGroup(['A',3], base_ring=ZZ)                                   # needs sage.graphs
        sage: g = W.an_element(); g                                                     # needs sage.graphs
        [ 0  0 -1]
        [ 1  0 -1]
        [ 0  1 -1]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, M, check=..., convert=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 144)

                Initialize ``self``.

                TESTS::

                    sage: W = CoxeterGroup(['A',3], base_ring=ZZ)                               # needs sage.graphs
                    sage: g = W.an_element()                                                    # needs sage.graphs
                    sage: TestSuite(g).run()                                                    # needs sage.graphs
        """
    def inverse(self, *args, **kwargs):
        """MatrixGroupElement_generic.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 369)

        Return the inverse group element.

        OUTPUT: a matrix group element

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.an_element()
            sage: ~g
            [-1  1  0]
            [-1  0  1]
            [-1  0  0]
            sage: g * ~g == W.one()
            True
            sage: ~g * g == W.one()
            True

            sage: # needs sage.combinat sage.libs.gap sage.rings.number_field
            sage: W = CoxeterGroup(['B',3])
            sage: W.base_ring()
            Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?
            sage: g = W.an_element()
            sage: ~g
            [-1  1  0]
            [-1  0  a]
            [-a  0  1]"""
    @overload
    def is_one(self) -> Any:
        """MatrixGroupElement_generic.is_one(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 351)

        Return whether ``self`` is the identity of the group.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = CoxeterGroup(['A',3])
            sage: g = W.gen(0)
            sage: g.is_one()
            False
            sage: W.an_element().is_one()
            False
            sage: W.one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """MatrixGroupElement_generic.is_one(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 351)

        Return whether ``self`` is the identity of the group.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = CoxeterGroup(['A',3])
            sage: g = W.gen(0)
            sage: g.is_one()
            False
            sage: W.an_element().is_one()
            False
            sage: W.one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """MatrixGroupElement_generic.is_one(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 351)

        Return whether ``self`` is the identity of the group.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = CoxeterGroup(['A',3])
            sage: g = W.gen(0)
            sage: g.is_one()
            False
            sage: W.an_element().is_one()
            False
            sage: W.one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """MatrixGroupElement_generic.is_one(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 351)

        Return whether ``self`` is the identity of the group.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = CoxeterGroup(['A',3])
            sage: g = W.gen(0)
            sage: g.is_one()
            False
            sage: W.an_element().is_one()
            False
            sage: W.one().is_one()
            True"""
    @overload
    def list(self) -> list:
        """MatrixGroupElement_generic.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 267)

        Return list representation of this matrix.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: g.list()
            [[-1, 1, 0], [0, 1, 0], [0, 0, 1]]"""
    @overload
    def list(self) -> Any:
        """MatrixGroupElement_generic.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 267)

        Return list representation of this matrix.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: g.list()
            [[-1, 1, 0], [0, 1, 0], [0, 0, 1]]"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_generic.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 285)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        One reason to compute the associated matrix is that matrices
        support a huge range of functionality.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g.matrix()
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: parent(g.matrix())
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')                                              # needs sage.combinat sage.libs.gap
            t^3 - t^2 - t + 1"""
    @overload
    def matrix(self, asanelementofamatrixspace) -> Any:
        """MatrixGroupElement_generic.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 285)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        One reason to compute the associated matrix is that matrices
        support a huge range of functionality.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g.matrix()
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: parent(g.matrix())
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')                                              # needs sage.combinat sage.libs.gap
            t^3 - t^2 - t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_generic.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 285)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        One reason to compute the associated matrix is that matrices
        support a huge range of functionality.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g.matrix()
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: parent(g.matrix())
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')                                              # needs sage.combinat sage.libs.gap
            t^3 - t^2 - t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_generic.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 285)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        One reason to compute the associated matrix is that matrices
        support a huge range of functionality.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g.matrix()
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: parent(g.matrix())
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')                                              # needs sage.combinat sage.libs.gap
            t^3 - t^2 - t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_generic.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 285)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        One reason to compute the associated matrix is that matrices
        support a huge range of functionality.

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.gen(0)
            sage: g.matrix()
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]
            sage: parent(g.matrix())
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')                                              # needs sage.combinat sage.libs.gap
            t^3 - t^2 - t + 1"""
    def __hash__(self) -> Any:
        """MatrixGroupElement_generic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 169)

        TESTS::

            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)                               # needs sage.graphs
            sage: g = W.an_element()                                                    # needs sage.graphs
            sage: hash(g)                                                               # needs sage.graphs
            660522311176098153  # 64-bit
            -606138007          # 32-bit"""
    def __invert__(self) -> Any:
        """MatrixGroupElement_generic.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 369)

        Return the inverse group element.

        OUTPUT: a matrix group element

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.gap
            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)
            sage: g = W.an_element()
            sage: ~g
            [-1  1  0]
            [-1  0  1]
            [-1  0  0]
            sage: g * ~g == W.one()
            True
            sage: ~g * g == W.one()
            True

            sage: # needs sage.combinat sage.libs.gap sage.rings.number_field
            sage: W = CoxeterGroup(['B',3])
            sage: W.base_ring()
            Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?
            sage: g = W.an_element()
            sage: ~g
            [-1  1  0]
            [-1  0  a]
            [-a  0  1]"""
    def __reduce__(self) -> Any:
        """MatrixGroupElement_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element.pyx (starting at line 181)

        Implement pickling.

        TESTS::

            sage: W = CoxeterGroup(['A',3], base_ring=ZZ)                               # needs sage.graphs
            sage: g = W.an_element()                                                    # needs sage.graphs
            sage: loads(g.dumps()) == g                                                 # needs sage.graphs
            True"""
