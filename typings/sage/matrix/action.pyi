import sage.categories.action
from sage.categories.homset import End as End, Hom as Hom
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modules.free_module import FreeModule as FreeModule, FreeModule_generic as FreeModule_generic
from sage.schemes.generic.homset import SchemeHomset_generic as SchemeHomset_generic, SchemeHomset_points as SchemeHomset_points
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class MatrixMatrixAction(MatrixMulAction):
    """MatrixMatrixAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 123)

    Action of a matrix on another matrix.

    This is always implemented as a left action.

    EXAMPLES:

    By :issue:`715`, there only is a weak reference on the underlying set,
    so that it can be garbage collected if only the action itself is
    explicitly referred to. Hence, we first assign the involved matrix
    spaces to a variable::

        sage: R.<x> = ZZ[]
        sage: MSR = MatrixSpace(R, 3, 3)
        sage: MSQ = MatrixSpace(QQ, 3, 2)
        sage: from sage.matrix.action import MatrixMatrixAction
        sage: A = MatrixMatrixAction(MSR, MSQ); A
        Left action
         by Full MatrixSpace of 3 by 3 dense matrices
            over Univariate Polynomial Ring in x over Integer Ring
         on Full MatrixSpace of 3 by 2 dense matrices over Rational Field
        sage: A.codomain()
        Full MatrixSpace of 3 by 2 dense matrices
         over Univariate Polynomial Ring in x over Rational Field
        sage: A(matrix(R, 3, 3, x), matrix(QQ, 3, 2, range(6)))
        [  0   x]
        [2*x 3*x]
        [4*x 5*x]

    .. NOTE::

        The :func:`MatrixSpace` function caches the object it creates.
        Therefore, the underlying set ``MSZ`` in the above example will not
        be garbage collected, even if it is not strongly ref'ed.
        Nonetheless, there is no guarantee that the set that is acted upon
        will always be cached in such a way, so that following the above
        example is good practice."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 162)"""
    @overload
    def __init__(self, MSR, MSQ) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 162)"""

class MatrixMulAction(sage.categories.action.Action):
    """MatrixMulAction(G, S, is_left)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 81)

    Abstract base class for a matrix space acting on something.

    EXAMPLES::

        sage: MSQ = MatrixSpace(QQ, 2)
        sage: MSZ = MatrixSpace(ZZ['x'], 2)
        sage: A = MSQ.get_action(MSZ); A
        Left action by Full MatrixSpace of 2 by 2 dense matrices over Rational Field
         on Full MatrixSpace of 2 by 2 dense matrices
            over Univariate Polynomial Ring in x over Integer Ring
        sage: A.actor()
        Full MatrixSpace of 2 by 2 dense matrices over Rational Field
        sage: A.domain()
        Full MatrixSpace of 2 by 2 dense matrices
         over Univariate Polynomial Ring in x over Integer Ring
        sage: A.codomain()
        Full MatrixSpace of 2 by 2 dense matrices
         over Univariate Polynomial Ring in x over Rational Field"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S, is_left) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 102)"""
    def codomain(self) -> Any:
        """MatrixMulAction.codomain(self)

        File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 119)"""

class MatrixPolymapAction(MatrixMulAction):
    """MatrixPolymapAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 394)

    Left action of a matrix on a scheme polynomial morphism"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 398)

                Initialize the action.

                EXAMPLES::

                    sage: from sage.matrix.action import MatrixPolymapAction
                    sage: M = MatrixSpace(QQ,2,2)
                    sage: P.<x,y> = ProjectiveSpace(QQ,1)
                    sage: H = Hom(P,P)
                    sage: A = MatrixPolymapAction(M,H)
                    sage: A
                    Left action by Full MatrixSpace of 2 by 2 dense matrices over Rational
                    Field on Set of morphisms
                      From: Projective Space of dimension 1 over Rational Field
                      To:   Projective Space of dimension 1 over Rational Field
        """

class MatrixSchemePointAction(MatrixMulAction):
    """MatrixSchemePointAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 539)

    Action class for left multiplication of schemes points by matrices."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 543)

                Initialization of action class.

                EXAMPLES::

                    sage: from sage.matrix.action import MatrixSchemePointAction
                    sage: M = MatrixSpace(QQ, 2, 2)
                    sage: P.<x,y> = ProjectiveSpace(QQ, 1)
                    sage: A = MatrixSchemePointAction(M, P(QQ))
                    sage: A
                    Left action by Full MatrixSpace of 2 by 2 dense matrices over
                    Rational Field on Set of rational points of Projective Space
                    of dimension 1 over Rational Field
        """

class MatrixVectorAction(MatrixMulAction):
    """MatrixVectorAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 292)

    Left action of a matrix on a vector"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 296)

                EXAMPLES::

                    sage: from sage.matrix.action import MatrixVectorAction
                    sage: A = MatrixVectorAction(MatrixSpace(QQ, 3, 3), VectorSpace(CDF, 4)); A
                    Traceback (most recent call last):
                    ...
                    TypeError: incompatible dimensions 3, 4
            """

class PolymapMatrixAction(MatrixMulAction):
    """PolymapMatrixAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 465)

    Right action of a matrix on a scheme polynomial morphism"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 469)

                Initialize the action.

                EXAMPLES::

                    sage: from sage.matrix.action import PolymapMatrixAction
                    sage: M = MatrixSpace(QQ,2,2)
                    sage: P.<x,y> = ProjectiveSpace(QQ,1)
                    sage: H = Hom(P,P)
                    sage: A = PolymapMatrixAction(M,H)
                    sage: A
                    Right action by Full MatrixSpace of 2 by 2 dense matrices over Rational
                    Field on Set of morphisms
                      From: Projective Space of dimension 1 over Rational Field
                      To:   Projective Space of dimension 1 over Rational Field
        """

class VectorMatrixAction(MatrixMulAction):
    """VectorMatrixAction(G, S)

    File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 343)

    Right action of a matrix on a vector"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/action.pyx (starting at line 347)

                EXAMPLES::

                    sage: from sage.matrix.action import VectorMatrixAction
                    sage: A = VectorMatrixAction(MatrixSpace(QQ, 5, 3), VectorSpace(CDF, 3)); A
                    Traceback (most recent call last):
                    ...
                    TypeError: incompatible dimensions 5, 3
        """
