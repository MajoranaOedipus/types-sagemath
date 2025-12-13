import sage.structure.list_clone
from sage.categories.category import ZZ as ZZ
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class CrystalOfBKKTableauxElement(TensorProductOfSuperCrystalsElement):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1287)

        Element class for the crystal of tableaux for Lie superalgebras
        of [BKK2000]_.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def pp(self) -> Any:
        """CrystalOfBKKTableauxElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1317)

        Pretty print ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',[1,2]], shape=[1,1])
            sage: c = C.an_element()
            sage: c.pp()
            -2
            -1"""
    @overload
    def pp(self) -> Any:
        """CrystalOfBKKTableauxElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1317)

        Pretty print ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',[1,2]], shape=[1,1])
            sage: c = C.an_element()
            sage: c.pp()
            -2
            -1"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfBKKTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1380)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',[1,2]], shape=[1,1])
            sage: c = C.an_element()
            sage: c.to_tableau()
            [[-2], [-1]]
            sage: type(c.to_tableau())
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(c)
            <class 'sage.combinat.crystals.bkk_crystals.CrystalOfBKKTableaux_with_category.element_class'>"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfBKKTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1380)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',[1,2]], shape=[1,1])
            sage: c = C.an_element()
            sage: c.to_tableau()
            [[-2], [-1]]
            sage: type(c.to_tableau())
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(c)
            <class 'sage.combinat.crystals.bkk_crystals.CrystalOfBKKTableaux_with_category.element_class'>"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfBKKTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1380)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',[1,2]], shape=[1,1])
            sage: c = C.an_element()
            sage: c.to_tableau()
            [[-2], [-1]]
            sage: type(c.to_tableau())
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(c)
            <class 'sage.combinat.crystals.bkk_crystals.CrystalOfBKKTableaux_with_category.element_class'>"""

class CrystalOfTableauxElement(TensorProductOfRegularCrystalsElement):
    """CrystalOfTableauxElement(parent, *args, **options)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 683)

    Element in a crystal of tableaux."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, *args, **options) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 687)

                There are several ways to input tableaux, by rows, by columns,
                by columns, as the list of column elements, or as a sequence
                of numbers in column reading.

                EXAMPLES::

                    sage: T = crystals.Tableaux(['A',3], shape = [2,2])
                    sage: t = T(rows=[[1,2],[3,4]])
                    sage: t
                    [[1, 2], [3, 4]]
                    sage: TestSuite(t).run()

                    sage: t = T(columns=[[3,1],[4,2]])
                    sage: t
                    [[1, 2], [3, 4]]
                    sage: TestSuite(t).run()

                    sage: t = T(list=[3,1,4,2])
                    sage: t
                    [[1, 2], [3, 4]]

                    sage: t = T(3,1,4,2)
                    sage: t
                    [[1, 2], [3, 4]]

                Currently inputting the empty tableau as an empty sequence is
                broken due to a bug in the generic __call__ method (see :issue:`8648`).

                EXAMPLES::

                    sage: T = crystals.Tableaux(['A',3], shape=[])
                    sage: t = T()
                    sage: list(t)
                    [0]

                TESTS:

                Integer types that are not a Sage ``Integer`` (such as a Python ``int``
                and typically arise from compiled code) were not converted into a
                letter. This caused certain functions to fail. This is fixed in
                :issue:`13204`::

                    sage: T = crystals.Tableaux(['A',3], shape = [2,2])
                    sage: t = T(list=[int(3),1,4,2])
                    sage: type(t[0])
                    <class 'sage.combinat.crystals.letters.Crystal_of_letters_type_A_element'>
                    sage: t = T(list=[3,int(1),4,2])
                    sage: type(t[1])
                    <class 'sage.combinat.crystals.letters.Crystal_of_letters_type_A_element'>
                    sage: C = crystals.KirillovReshetikhin(['A',int(3),1], 1,1)
                    sage: C[0].e(0)
                    [[4]]
        """
    @overload
    def pp(self) -> Any:
        """CrystalOfTableauxElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 791)

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]])
            sage: t.pp()
            1  2
            3  4"""
    @overload
    def pp(self) -> Any:
        """CrystalOfTableauxElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 791)

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]])
            sage: t.pp()
            1  2
            3  4"""
    @overload
    def promotion(self) -> Any:
        '''CrystalOfTableauxElement.promotion(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 954)

        Return the result of applying promotion on ``self``.

        Promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion()
            [[1, 1, 2], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def promotion(self) -> Any:
        '''CrystalOfTableauxElement.promotion(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 954)

        Return the result of applying promotion on ``self``.

        Promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion()
            [[1, 1, 2], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def promotion(self) -> Any:
        '''CrystalOfTableauxElement.promotion(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 954)

        Return the result of applying promotion on ``self``.

        Promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion()
            [[1, 1, 2], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def promotion_inverse(self) -> Any:
        '''CrystalOfTableauxElement.promotion_inverse(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 977)

        Return the result of applying inverse promotion on ``self``.

        Inverse promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion_inverse()
            [[1, 1, 2], [2, 3, 3], [4, 4, 4]]
            sage: t.promotion_inverse().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def promotion_inverse(self) -> Any:
        '''CrystalOfTableauxElement.promotion_inverse(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 977)

        Return the result of applying inverse promotion on ``self``.

        Inverse promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion_inverse()
            [[1, 1, 2], [2, 3, 3], [4, 4, 4]]
            sage: t.promotion_inverse().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def promotion_inverse(self) -> Any:
        '''CrystalOfTableauxElement.promotion_inverse(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 977)

        Return the result of applying inverse promotion on ``self``.

        Inverse promotion for type A crystals of tableaux of rectangular shape.
        This method only makes sense in type A with rectangular shapes.

        EXAMPLES::

            sage: C = crystals.Tableaux(["A",3], shape = [3,3,3])
            sage: t = C(Tableau([[1,1,1],[2,2,3],[3,4,4]]))
            sage: t
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]]
            sage: t.promotion_inverse()
            [[1, 1, 2], [2, 3, 3], [4, 4, 4]]
            sage: t.promotion_inverse().parent()
            The crystal of tableaux of type [\'A\', 3] and shape(s) [[3, 3, 3]]'''
    @overload
    def shape(self) -> Any:
        '''CrystalOfTableauxElement.shape(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 933)

        Return the shape of the tableau corresponding to ``self``.

        OUTPUT: an instance of :class:`Partition`

        .. SEEALSO::

            :meth:`to_tableau`

        EXAMPLES::

            sage: C = crystals.Tableaux(["A", 2], shape=[2,1])
            sage: x = C.an_element()
            sage: x.to_tableau().shape()
            [2, 1]
            sage: x.shape()
            [2, 1]'''
    @overload
    def shape(self) -> Any:
        '''CrystalOfTableauxElement.shape(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 933)

        Return the shape of the tableau corresponding to ``self``.

        OUTPUT: an instance of :class:`Partition`

        .. SEEALSO::

            :meth:`to_tableau`

        EXAMPLES::

            sage: C = crystals.Tableaux(["A", 2], shape=[2,1])
            sage: x = C.an_element()
            sage: x.to_tableau().shape()
            [2, 1]
            sage: x.shape()
            [2, 1]'''
    @overload
    def shape(self) -> Any:
        '''CrystalOfTableauxElement.shape(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 933)

        Return the shape of the tableau corresponding to ``self``.

        OUTPUT: an instance of :class:`Partition`

        .. SEEALSO::

            :meth:`to_tableau`

        EXAMPLES::

            sage: C = crystals.Tableaux(["A", 2], shape=[2,1])
            sage: x = C.an_element()
            sage: x.to_tableau().shape()
            [2, 1]
            sage: x.shape()
            [2, 1]'''
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 896)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]]).to_tableau(); t
            [[1, 2], [3, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(t[0][0])
            <class 'int'>
            sage: T = crystals.Tableaux(['D',3], shape = [1,1])
            sage: t=T(rows=[[-3],[3]]).to_tableau(); t
            [[-3], [3]]
            sage: t=T(rows=[[3],[-3]]).to_tableau(); t
            [[3], [-3]]
            sage: T = crystals.Tableaux(['B',2], shape = [1,1])
            sage: t = T(rows=[[0],[0]]).to_tableau(); t
            [[0], [0]]"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 896)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]]).to_tableau(); t
            [[1, 2], [3, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(t[0][0])
            <class 'int'>
            sage: T = crystals.Tableaux(['D',3], shape = [1,1])
            sage: t=T(rows=[[-3],[3]]).to_tableau(); t
            [[-3], [3]]
            sage: t=T(rows=[[3],[-3]]).to_tableau(); t
            [[3], [-3]]
            sage: T = crystals.Tableaux(['B',2], shape = [1,1])
            sage: t = T(rows=[[0],[0]]).to_tableau(); t
            [[0], [0]]"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 896)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]]).to_tableau(); t
            [[1, 2], [3, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(t[0][0])
            <class 'int'>
            sage: T = crystals.Tableaux(['D',3], shape = [1,1])
            sage: t=T(rows=[[-3],[3]]).to_tableau(); t
            [[-3], [3]]
            sage: t=T(rows=[[3],[-3]]).to_tableau(); t
            [[3], [-3]]
            sage: T = crystals.Tableaux(['B',2], shape = [1,1])
            sage: t = T(rows=[[0],[0]]).to_tableau(); t
            [[0], [0]]"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 896)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]]).to_tableau(); t
            [[1, 2], [3, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(t[0][0])
            <class 'int'>
            sage: T = crystals.Tableaux(['D',3], shape = [1,1])
            sage: t=T(rows=[[-3],[3]]).to_tableau(); t
            [[-3], [3]]
            sage: t=T(rows=[[3],[-3]]).to_tableau(); t
            [[3], [-3]]
            sage: T = crystals.Tableaux(['B',2], shape = [1,1])
            sage: t = T(rows=[[0],[0]]).to_tableau(); t
            [[0], [0]]"""
    @overload
    def to_tableau(self) -> Any:
        """CrystalOfTableauxElement.to_tableau(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 896)

        Return the :class:`Tableau` object corresponding to ``self``.

        EXAMPLES::

            sage: T = crystals.Tableaux(['A',3], shape = [2,2])
            sage: t = T(rows=[[1,2],[3,4]]).to_tableau(); t
            [[1, 2], [3, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
            sage: type(t[0][0])
            <class 'int'>
            sage: T = crystals.Tableaux(['D',3], shape = [1,1])
            sage: t=T(rows=[[-3],[3]]).to_tableau(); t
            [[-3], [3]]
            sage: t=T(rows=[[3],[-3]]).to_tableau(); t
            [[3], [-3]]
            sage: T = crystals.Tableaux(['B',2], shape = [1,1])
            sage: t = T(rows=[[0],[0]]).to_tableau(); t
            [[0], [0]]"""

class ImmutableListWithParent(sage.structure.list_clone.ClonableArray):
    """ImmutableListWithParent(Parent parent, list)

    File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 43)

    A class for lists having a parent.

    Specification: any subclass ``C`` should implement ``__init__`` which
    accepts the following form ``C(parent, list=list)``"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Parentparent, list) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 50)

                Initialize ``self``.

                TESTS::

                    sage: b = crystals.Tableaux(['A',2], shape=[2,1]).module_generators[0]
                    sage: TestSuite(b).run()
        """

class InfinityCrystalOfTableauxElement(CrystalOfTableauxElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        """InfinityCrystalOfTableauxElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1001)

        Return the action of `\\widetilde{e}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['B',3])
            sage: b = B(rows=[[1,1,1,1,1,1,1,2,0,-3,-1,-1,-1,-1],[2,2,2,2,-2,-2],[3,-3,-3]])
            sage: b.e(3).pp()
            1  1  1  1  1  1  1  2  0 -3 -1 -1 -1 -1
            2  2  2  2 -2 -2
            3  0 -3
            sage: b.e(1).pp()
            1  1  1  1  1  1  1  0 -3 -1 -1 -1 -1
            2  2  2  2 -2 -2
            3 -3 -3"""
    def f(self, i) -> Any:
        """InfinityCrystalOfTableauxElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1039)

        Return the action of `\\widetilde{f}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['C',4])
            sage: b = B.highest_weight_vector()
            sage: b.f(1).pp()
            1  1  1  1  2
            2  2  2
            3  3
            4
            sage: b.f(3).pp()
            1  1  1  1  1
            2  2  2  2
            3  3  4
            4
            sage: b.f(3).f(4).pp()
            1  1  1  1  1
            2  2  2  2
            3  3 -4
            4"""

class InfinityCrystalOfTableauxElementTypeD(InfinityCrystalOfTableauxElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        """InfinityCrystalOfTableauxElementTypeD.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1085)

        Return the action of `\\widetilde{e}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['D',4])
            sage: b = B.highest_weight_vector().f_string([1,4,3,1,2]); b.pp()
            1  1  1  1  2  3
            2  2  2
            3 -3
            sage: b.e(2).pp()
            1  1  1  1  2  2
            2  2  2
            3 -3"""
    def f(self, i) -> Any:
        """InfinityCrystalOfTableauxElementTypeD.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1124)

        Return the action of `\\widetilde{f}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['D',5])
            sage: b = B.highest_weight_vector().f_string([1,4,3,1,5]); b.pp()
            1  1  1  1  1  1  2  2
            2  2  2  2  2
            3  3  3 -5
            4  5
            sage: b.f(1).pp()
            1  1  1  1  1  1  2  2  2
            2  2  2  2  2
            3  3  3 -5
            4  5
            sage: b.f(5).pp()
            1  1  1  1  1  1  2  2
            2  2  2  2  2
            3  3  3 -5
            4 -4"""

class InfinityQueerCrystalOfTableauxElement(TensorProductOfQueerSuperCrystalsElement):
    """InfinityQueerCrystalOfTableauxElement(parent, list, row_lengths=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, list, row_lengths=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1643)

                Initialize ``self``.

                EXAMPLES::

                    sage: B = crystals.infinity.Tableaux(['Q',4])
                    sage: t = B([[4,4,4,4,2,1],[3,3,3],[2,2],[1]])
                    sage: t
                    [[4, 4, 4, 4, 2, 1], [3, 3, 3], [2, 2], [1]]
                    sage: TestSuite(t).run()
        """
    def e(self, i) -> Any:
        """InfinityQueerCrystalOfTableauxElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1743)

        Return the action of `e_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.e(1)
            [[4, 4, 4, 4, 4, 4, 2, 1], [3, 3, 3, 3, 3], [2, 2, 1, 1], [1]]
            sage: t.e(3)
            [[4, 4, 4, 4, 4, 3, 2, 1], [3, 3, 3, 3], [2, 2, 1], [1]]
            sage: t.e(-1)"""
    def epsilon(self, i) -> Any:
        """InfinityQueerCrystalOfTableauxElement.epsilon(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1811)

        Return `\\varepsilon_i` of ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: [t.epsilon(i) for i in B.index_set()]
            [-1, 1, -2, 0]"""
    def f(self, i) -> Any:
        """InfinityQueerCrystalOfTableauxElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1777)

        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.f(1)
            [[4, 4, 4, 4, 4, 2, 2], [3, 3, 3, 3], [2, 2, 1], [1]]
            sage: t.f(3)
            sage: t.f(-1)
            [[4, 4, 4, 4, 4, 2, 2], [3, 3, 3, 3], [2, 2, 1], [1]]"""
    @overload
    def rows(self) -> Any:
        """InfinityQueerCrystalOfTableauxElement.rows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1722)

        Return the list of rows of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.rows()
            [[1, 2, 4, 4, 4, 4, 4], [3, 3, 3, 3], [1, 2, 2], [1]]"""
    @overload
    def rows(self) -> Any:
        """InfinityQueerCrystalOfTableauxElement.rows(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1722)

        Return the list of rows of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.rows()
            [[1, 2, 4, 4, 4, 4, 4], [3, 3, 3, 3], [1, 2, 2], [1]]"""
    @overload
    def weight(self) -> Any:
        """InfinityQueerCrystalOfTableauxElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1834)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.weight()
            (4, 2, 2, 0)"""
    @overload
    def weight(self) -> Any:
        """InfinityQueerCrystalOfTableauxElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1834)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['Q',4])
            sage: t = B([[4,4,4,4,4,2,1],[3,3,3,3],[2,2,1],[1]])
            sage: t.weight()
            (4, 2, 2, 0)"""

class TensorProductOfCrystalsElement(ImmutableListWithParent):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 97)

        A class for elements of tensor products of crystals.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        '''TensorProductOfCrystalsElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 399)

        Return the action of `e_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("D4")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([1,4,3])
            sage: b2 = B.highest_weight_vector().f_string([2,2,3,1,4])
            sage: t = T(b2, b1)
            sage: t.e(1)
            [[[1, 1, 1, 1, 1], [2, 2, 3, -3], [3]], [[1, 1, 1, 1, 2], [2, 2, 2], [3, -3]]]
            sage: t.e(2)
            sage: t.e(3)
            [[[1, 1, 1, 1, 1, 2], [2, 2, 3, -4], [3]], [[1, 1, 1, 1, 2], [2, 2, 2], [3, -3]]]
            sage: t.e(4)
            [[[1, 1, 1, 1, 1, 2], [2, 2, 3, 4], [3]], [[1, 1, 1, 1, 2], [2, 2, 2], [3, -3]]]'''
    def epsilon(self, i) -> Any:
        '''TensorProductOfCrystalsElement.epsilon(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 284)

        Return `\\varepsilon_i` of ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("G2")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f(2)
            sage: b2 = B.highest_weight_vector().f_string([2,2,1])
            sage: t = T(b2, b1)
            sage: [t.epsilon(i) for i in B.index_set()]
            [0, 3]'''
    def f(self, i) -> Any:
        """TensorProductOfCrystalsElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 432)

        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: La = RootSystem(['A',3,1]).weight_lattice(extended=True).fundamental_weights()
            sage: B = crystals.GeneralizedYoungWalls(3,La[0])
            sage: T = crystals.TensorProduct(B,B,B)
            sage: b1 = B.highest_weight_vector().f_string([0,3])
            sage: b2 = B.highest_weight_vector().f_string([0])
            sage: b3 = B.highest_weight_vector()
            sage: t = T(b3, b2, b1)
            sage: t.f(0)
            [[[0]], [[0]], [[0, 3]]]
            sage: t.f(1)
            [[], [[0]], [[0, 3], [1]]]
            sage: t.f(2)
            [[], [[0]], [[0, 3, 2]]]
            sage: t.f(3)
            [[], [[0, 3]], [[0, 3]]]"""
    def phi(self, i) -> Any:
        """TensorProductOfCrystalsElement.phi(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 304)

        Return `\\varphi_i` of ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: B = crystals.GeneralizedYoungWalls(2,La[0]+La[1])
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([1,0])
            sage: b2 = B.highest_weight_vector().f_string([0,1])
            sage: t = T(b2, b1)
            sage: [t.phi(i) for i in B.index_set()]
            [1, 1, 4]

        TESTS:

        Check that :issue:`15462` is fixed::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: La = RootSystem(['A',2]).ambient_space().fundamental_weights()
            sage: T = crystals.TensorProduct(crystals.elementary.T(['A',2], La[1]+La[2]), B)
            sage: t = T.an_element()
            sage: t.phi(1)
            2
            sage: t.phi(2)
            2"""
    @overload
    def pp(self) -> Any:
        """TensorProductOfCrystalsElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 238)

        Pretty print ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',3], shape=[3,1])
            sage: D = crystals.Tableaux(['A',3], shape=[1])
            sage: E = crystals.Tableaux(['A',3], shape=[2,2,2])
            sage: T = crystals.TensorProduct(C,D,E)
            sage: T.module_generators[0].pp()
              1  1  1 (X)   1 (X)   1  1
              2                     2  2
                                    3  3"""
    @overload
    def pp(self) -> Any:
        """TensorProductOfCrystalsElement.pp(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 238)

        Pretty print ``self``.

        EXAMPLES::

            sage: C = crystals.Tableaux(['A',3], shape=[3,1])
            sage: D = crystals.Tableaux(['A',3], shape=[1])
            sage: E = crystals.Tableaux(['A',3], shape=[2,2,2])
            sage: T = crystals.TensorProduct(C,D,E)
            sage: T.module_generators[0].pp()
              1  1  1 (X)   1 (X)   1  1
              2                     2  2
                                    3  3"""
    @overload
    def weight(self) -> Any:
        '''TensorProductOfCrystalsElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 255)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("A3")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([2,1,3])
            sage: b2 = B.highest_weight_vector().f(1)
            sage: t = T(b2, b1)
            sage: t
            [[[1, 1, 1, 2], [2, 2], [3]], [[1, 1, 1, 1, 2], [2, 2, 4], [3]]]
            sage: t.weight()
            (-2, 1, 0, 1)

        ::

            sage: C = crystals.Letters([\'A\',3])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(2)).weight()
            (1, 1, 0, 0)
            sage: T = crystals.Tableaux([\'D\',4],shape=[])
            sage: T.list()[0].weight()
            (0, 0, 0, 0)'''
    @overload
    def weight(self) -> Any:
        '''TensorProductOfCrystalsElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 255)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("A3")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([2,1,3])
            sage: b2 = B.highest_weight_vector().f(1)
            sage: t = T(b2, b1)
            sage: t
            [[[1, 1, 1, 2], [2, 2], [3]], [[1, 1, 1, 1, 2], [2, 2, 4], [3]]]
            sage: t.weight()
            (-2, 1, 0, 1)

        ::

            sage: C = crystals.Letters([\'A\',3])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(2)).weight()
            (1, 1, 0, 0)
            sage: T = crystals.Tableaux([\'D\',4],shape=[])
            sage: T.list()[0].weight()
            (0, 0, 0, 0)'''
    @overload
    def weight(self) -> Any:
        '''TensorProductOfCrystalsElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 255)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("A3")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([2,1,3])
            sage: b2 = B.highest_weight_vector().f(1)
            sage: t = T(b2, b1)
            sage: t
            [[[1, 1, 1, 2], [2, 2], [3]], [[1, 1, 1, 1, 2], [2, 2, 4], [3]]]
            sage: t.weight()
            (-2, 1, 0, 1)

        ::

            sage: C = crystals.Letters([\'A\',3])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(2)).weight()
            (1, 1, 0, 0)
            sage: T = crystals.Tableaux([\'D\',4],shape=[])
            sage: T.list()[0].weight()
            (0, 0, 0, 0)'''
    @overload
    def weight(self) -> Any:
        '''TensorProductOfCrystalsElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 255)

        Return the weight of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux("A3")
            sage: T = crystals.TensorProduct(B,B)
            sage: b1 = B.highest_weight_vector().f_string([2,1,3])
            sage: b2 = B.highest_weight_vector().f(1)
            sage: t = T(b2, b1)
            sage: t
            [[[1, 1, 1, 2], [2, 2], [3]], [[1, 1, 1, 1, 2], [2, 2, 4], [3]]]
            sage: t.weight()
            (-2, 1, 0, 1)

        ::

            sage: C = crystals.Letters([\'A\',3])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(2)).weight()
            (1, 1, 0, 0)
            sage: T = crystals.Tableaux([\'D\',4],shape=[])
            sage: T.list()[0].weight()
            (0, 0, 0, 0)'''

class TensorProductOfQueerSuperCrystalsElement(TensorProductOfRegularCrystalsElement):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1409)

        Element class for a tensor product of crystals for queer Lie superalgebras.

        This implements the tensor product rule for crystals of Grantcharov et al.
        [GJK+2014]_. Given crystals `B_1` and `B_2` of type `\\mathfrak{q}_{n+1}`,
        we define the tensor product `b_1 \\otimes b_2 \\in B_1 \\otimes B_2`,
        where `b_1 \\in B_1` and `b_2 \\in B_2`, as the following:

        In addition to the tensor product rule for type `A_n`, the tensor product
        rule for `e_{-1}` and `f_{-1}` on `b_1\\otimes b_2` are given by

        .. MATH::

            \\begin{aligned}
            e_{-1}(b_1\\otimes b_2) &=
            \\begin{cases}
            b_1 \\otimes e_{-1}b_2 &
             \\text{if } \\operatorname{wt}(b_1)_1 = \\operatorname{wt}(b_1)_2 = 0,\\\\\n            e_{-1}b_1 \\otimes b_2 & \\text{otherwise},
            \\end{cases}
            \\\\\n            f_{-1}(b_1\\otimes b_2) &=
            \\begin{cases}
            b_1 \\otimes f_{-1}b_2 &
             \\text{if } \\operatorname{wt}(b_1)_1 = \\operatorname{wt}(b_1)_2 = 0,\\\\\n            f_{-1}b_1 \\otimes b_2 & \\text{otherwise}.
            \\end{cases}
            \\end{aligned}

        For `1 < i \\leq n`, the operators `e_{-i}` and `f_{-i}` are defined as

        .. MATH::

            e_{-i} = s_{w^{-1}_i} e_{-1} s_{w_i}, \\quad
            f_{-i} = s_{w^{-1}_i} f_{-1} s_{w_i}.

        Here, `w_i = s_2 \\cdots s_i s_1 \\cdots s_{i-1}` and `s_i` is the reflection
        along the `i`-string in the crystal. Moreover, for `1<i\\leq n`, we define
        the operators `e_{-i'}` and `f_{-i'}` as

        .. MATH::

            e_{-i'} = s_{w_0} f_{-(n+1-i)} s_{w_0}, \\quad
            f_{-i'} = s_{w_0} e_{-(n+1-i)} s_{w_0},

        where `w_0` is the longest element in the symmetric group `S_{n+1}`
        generated by `s_1,\\ldots,s_n`. In this implementation, we use the integers
        `-2n, \\ldots, -(n+1)` to respectively denote the indices `-n', \\ldots, -1'`.

        TESTS::

            sage: Q = crystals.Letters(['Q', 3])
            sage: T = tensor([Q,Q]); T
            Full tensor product of the crystals
             [The queer crystal of letters for q(3),
              The queer crystal of letters for q(3)]
            sage: T.cardinality()
            9
            sage: t = T.an_element(); t
            [1, 1]
            sage: t.weight()
            (2, 0, 0)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        """TensorProductOfQueerSuperCrystalsElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1473)

        Return `e_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q', 3])
            sage: T = tensor([Q,Q])
            sage: t = T(Q(1),Q(1))
            sage: t.e(-1)
            sage: t = T(Q(2),Q(1))
            sage: t.e(-1)
            [1, 1]

            sage: T = tensor([Q,Q,Q,Q])
            sage: t = T(Q(1),Q(3),Q(2),Q(1))
            sage: t.e(-2)
            [2, 2, 1, 1]"""
    def epsilon(self, i) -> Any:
        """TensorProductOfQueerSuperCrystalsElement.epsilon(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1601)

        Return `\\varepsilon_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q', 3])
            sage: T = tensor([Q, Q, Q, Q])
            sage: t = T(Q(1), Q(3), Q(2), Q(1))
            sage: t.epsilon(-2)
            1"""
    def f(self, i) -> Any:
        """TensorProductOfQueerSuperCrystalsElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1540)

        Return `f_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q', 3])
            sage: T = tensor([Q, Q])
            sage: t = T(Q(1), Q(1))
            sage: t.f(-1)
            [2, 1]"""
    def phi(self, i) -> Any:
        """TensorProductOfQueerSuperCrystalsElement.phi(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1620)

        Return `\\varphi_i` on ``self``.

        EXAMPLES::

            sage: Q = crystals.Letters(['Q', 3])
            sage: T = tensor([Q, Q, Q, Q])
            sage: t = T(Q(1), Q(3), Q(2), Q(1))
            sage: t.phi(-2)
            0
            sage: t.phi(-1)
            1"""

class TensorProductOfRegularCrystalsElement(TensorProductOfCrystalsElement):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 469)

        Element class for a tensor product of regular crystals.

        TESTS::

            sage: C = crystals.Letters(['A',2])
            sage: T = crystals.TensorProduct(C, C)
            sage: elt = T(C(1), C(2))
            sage: from sage.combinat.crystals.tensor_product import TensorProductOfRegularCrystalsElement
            sage: isinstance(elt, TensorProductOfRegularCrystalsElement)
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 482)

        Return the action of `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(2)).e(1) == T(C(1),C(1))
            True
            sage: T(C(2),C(1)).e(1) is None
            True
            sage: T(C(2),C(2)).e(1) == T(C(1),C(2))
            True"""
    def epsilon(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.epsilon(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 551)

        Return `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(1)).epsilon(1)
            0
            sage: T(C(1),C(2)).epsilon(1)
            1
            sage: T(C(2),C(1)).epsilon(1)
            0"""
    def f(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 504)

        Return the action of `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(1)).f(1)
            [1, 2]
            sage: T(C(1),C(2)).f(1)
            [2, 2]
            sage: T(C(2),C(1)).f(1) is None
            True"""
    def phi(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.phi(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 526)

        Return `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(1),C(1)).phi(1)
            2
            sage: T(C(1),C(2)).phi(1)
            1
            sage: T(C(2),C(1)).phi(1)
            0"""
    def position_of_first_unmatched_plus(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.position_of_first_unmatched_plus(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 602)

        Return the position of the first unmatched `+` or ``None`` if
        there is no unmatched `+`.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(2),C(1)).position_of_first_unmatched_plus(1)
            sage: T(C(1),C(2)).position_of_first_unmatched_plus(1)
            1"""
    def position_of_last_unmatched_minus(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.position_of_last_unmatched_minus(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 576)

        Return the position of the last unmatched `-` or ``None`` if
        there is no unmatched `-`.

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(2),C(1)).position_of_last_unmatched_minus(1)
            sage: T(C(1),C(2)).position_of_last_unmatched_minus(1)
            0"""
    def positions_of_unmatched_minus(self, i, dual=..., reverse=...) -> Any:
        """TensorProductOfRegularCrystalsElement.positions_of_unmatched_minus(self, i, dual=False, reverse=False)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 630)

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(2),C(1)).positions_of_unmatched_minus(1)
            []
            sage: T(C(1),C(2)).positions_of_unmatched_minus(1)
            [0]"""
    def positions_of_unmatched_plus(self, i) -> Any:
        """TensorProductOfRegularCrystalsElement.positions_of_unmatched_plus(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 667)

        EXAMPLES::

            sage: C = crystals.Letters(['A',5])
            sage: T = crystals.TensorProduct(C,C)
            sage: T(C(2),C(1)).positions_of_unmatched_plus(1)
            []
            sage: T(C(1),C(2)).positions_of_unmatched_plus(1)
            [1]"""

class TensorProductOfSuperCrystalsElement(TensorProductOfRegularCrystalsElement):
    """File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1162)

        Element class for a tensor product of crystals for Lie superalgebras.

        This implements the tensor product rule for crystals of
        Lie superalgebras of [BKK2000]_.

        TESTS::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: T = tensor([C,C])
            sage: T
            Full tensor product of the crystals [The crystal of letters for type ['A', [2, 1]], The crystal of letters for type ['A', [2, 1]]]
            sage: T.cardinality()
            25
            sage: t = T.an_element(); t
            [-3, -3]
            sage: t.weight()
            (2, 0, 0, 0, 0)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def e(self, i) -> Any:
        """TensorProductOfSuperCrystalsElement.e(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1183)

        Return `e_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: T = tensor([C,C])
            sage: t = T(C(1),C(1))
            sage: t.e(0)
            [-1, 1]"""
    def epsilon(self, i) -> Any:
        """TensorProductOfSuperCrystalsElement.epsilon(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1245)

        Return `\\varepsilon_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: T = tensor([C,C])
            sage: t = T(C(1),C(1))
            sage: t.epsilon(0)
            1"""
    def f(self, i) -> Any:
        """TensorProductOfSuperCrystalsElement.f(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1213)

        Return `f_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: T = tensor([C,C])
            sage: t = T(C(1),C(1))
            sage: t.f(0)
            sage: t.f(1)
            [1, 2]"""
    def phi(self, i) -> Any:
        """TensorProductOfSuperCrystalsElement.phi(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/crystals/tensor_product_element.pyx (starting at line 1266)

        Return `\\varphi_i` on ``self``.

        EXAMPLES::

            sage: C = crystals.Letters(['A', [2, 1]])
            sage: T = tensor([C,C])
            sage: t = T(C(1),C(1))
            sage: t.phi(0)
            0"""
