import sage.groups
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Matrix as Matrix, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class MatrixGroupElement_gap(sage.groups.libgap_wrapper.ElementLibGAP):
    """MatrixGroupElement_gap(parent, M, check=True, convert=True)

    File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 28)

    Element of a matrix group over a generic ring.

    The group elements are implemented as wrappers around libGAP matrices.

    INPUT:

    - ``M`` -- a matrix

    - ``parent`` -- the parent

    - ``check`` -- boolean (default: ``True``); if ``True``, do some
      type checking

    - ``convert`` -- boolean (default: ``True``); if ``True``, convert
      ``M`` to the right matrix space"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, M, check=..., convert=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 46)

                Initialize ``self``.

                TESTS::

                    sage: MS = MatrixSpace(GF(3),2,2)
                    sage: G = MatrixGroup(MS([[1,0],[0,1]]), MS([[1,1],[0,1]]))
                    sage: G.gen(0)
                    [1 0]
                    [0 1]
                    sage: g = G.random_element()
                    sage: TestSuite(g).run()
        """
    @overload
    def list(self) -> list:
        """MatrixGroupElement_gap.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 233)

        Return list representation of this matrix.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: g = G.0
            sage: g
            [1 0]
            [0 1]
            sage: g.list()
            [[1, 0], [0, 1]]"""
    @overload
    def list(self) -> Any:
        """MatrixGroupElement_gap.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 233)

        Return list representation of this matrix.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: g = G.0
            sage: g
            [1 0]
            [0 1]
            sage: g.list()
            [[1, 0], [0, 1]]"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def matrix(self, asanelementofamatrixspace) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def matrix(self) -> Any:
        """MatrixGroupElement_gap.matrix(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 176)

        Obtain the usual matrix (as an element of a matrix space)
        associated to this matrix group element.

        EXAMPLES::

            sage: F = GF(3); MS = MatrixSpace(F,2,2)
            sage: gens = [MS([[1,0],[0,1]]),MS([[1,1],[0,1]])]
            sage: G = MatrixGroup(gens)
            sage: m = G.gen(0).matrix(); m
            [1 0]
            [0 1]
            sage: m.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 3

            sage: k = GF(7); G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])])
            sage: g = G.0
            sage: g.matrix()
            [1 1]
            [0 1]
            sage: parent(g.matrix())
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 7

        Matrices have extra functionality that matrix group elements
        do not have::

            sage: g.matrix().charpoly('t')
            t^2 + 5*t + 1"""
    @overload
    def multiplicative_order(self) -> Any:
        """MatrixGroupElement_gap.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 251)

        Return the order of this group element, which is the smallest
        positive integer `n` such that `g^n = 1`, or
        +Infinity if no such integer exists.

        EXAMPLES::

            sage: k = GF(7)
            sage: G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])]); G
            Matrix group over Finite Field of size 7 with 2 generators (
            [1 1]  [1 0]
            [0 1], [0 2]
            )
            sage: G.order()
            21
            sage: G.gen(0).multiplicative_order(), G.gen(1).multiplicative_order()
            (7, 3)

        ``order`` is just an alias for ``multiplicative_order``::

            sage: G.gen(0).order(), G.gen(1).order()
            (7, 3)

            sage: k = QQ
            sage: G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])]); G
            Matrix group over Rational Field with 2 generators (
            [1 1]  [1 0]
            [0 1], [0 2]
            )
            sage: G.order()
            +Infinity
            sage: G.gen(0).order(), G.gen(1).order()
            (+Infinity, +Infinity)

            sage: gl = GL(2, ZZ);  gl
            General Linear Group of degree 2 over Integer Ring
            sage: g = gl.gen(2);  g
            [1 1]
            [0 1]
            sage: g.order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """MatrixGroupElement_gap.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 251)

        Return the order of this group element, which is the smallest
        positive integer `n` such that `g^n = 1`, or
        +Infinity if no such integer exists.

        EXAMPLES::

            sage: k = GF(7)
            sage: G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])]); G
            Matrix group over Finite Field of size 7 with 2 generators (
            [1 1]  [1 0]
            [0 1], [0 2]
            )
            sage: G.order()
            21
            sage: G.gen(0).multiplicative_order(), G.gen(1).multiplicative_order()
            (7, 3)

        ``order`` is just an alias for ``multiplicative_order``::

            sage: G.gen(0).order(), G.gen(1).order()
            (7, 3)

            sage: k = QQ
            sage: G = MatrixGroup([matrix(k,2,[1,1,0,1]), matrix(k,2,[1,0,0,2])]); G
            Matrix group over Rational Field with 2 generators (
            [1 1]  [1 0]
            [0 1], [0 2]
            )
            sage: G.order()
            +Infinity
            sage: G.gen(0).order(), G.gen(1).order()
            (+Infinity, +Infinity)

            sage: gl = GL(2, ZZ);  gl
            General Linear Group of degree 2 over Integer Ring
            sage: g = gl.gen(2);  g
            [1 1]
            [0 1]
            sage: g.order()
            +Infinity"""
    @overload
    def word_problem(self, gens=...) -> Any:
        """MatrixGroupElement_gap.word_problem(self, gens=None)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 303)

        Solve the word problem.

        This method writes the group element as a product of the
        elements of the list ``gens``, or the standard generators of
        the parent of ``self`` if ``gens`` is ``None``.

        INPUT:

        - ``gens`` -- list/tuple/iterable of elements (or objects
          that can be converted to group elements), or ``None``
          (default); by default, the generators of the parent group
          are used

        OUTPUT:

        A factorization object that contains information about the
        order of factors and the exponents. A :exc:`ValueError` is raised
        if the group element cannot be written as a word in ``gens``.

        ALGORITHM:

        Use GAP, which has optimized algorithms for solving the word
        problem (the GAP functions ``EpimorphismFromFreeGroup`` and
        ``PreImagesRepresentative``).

        EXAMPLES::

            sage: G = GL(2,5); G
            General Linear Group of degree 2 over Finite Field of size 5
            sage: G.gens()
            (
            [2 0]  [4 1]
            [0 1], [4 0]
            )
            sage: G(1).word_problem([G.gen(0)])
            1
            sage: type(_)
            <class 'sage.structure.factorization.Factorization'>

            sage: g = G([0,4,1,4])
            sage: g.word_problem()
            ([4 1]
             [4 0])^-1

        Next we construct a more complicated element of the group from the
        generators::

            sage: s,t = G.0, G.1
            sage: a = (s * t * s); b = a.word_problem(); b
            ([2 0]
             [0 1]) *
            ([4 1]
             [4 0]) *
            ([2 0]
             [0 1])
            sage: flatten(b)
            [
            [2 0]     [4 1]     [2 0]
            [0 1], 1, [4 0], 1, [0 1], 1
            ]
            sage: b.prod() == a
            True

        We solve the word problem using some different generators::

            sage: s = G([2,0,0,1]); t = G([1,1,0,1]); u = G([0,-1,1,0])
            sage: a.word_problem([s,t,u])
            ([2 0]
             [0 1])^-1 *
            ([1 1]
             [0 1])^-1 *
            ([0 4]
             [1 0]) *
            ([2 0]
             [0 1])^-1

        We try some elements that don't actually generate the group::

            sage: a.word_problem([t,u])
            Traceback (most recent call last):
            ...
            ValueError: word problem has no solution

        AUTHORS:

        - David Joyner and William Stein
        - David Loeffler (2010): fixed some bugs
        - Volker Braun (2013): LibGAP"""
    @overload
    def word_problem(self) -> Any:
        """MatrixGroupElement_gap.word_problem(self, gens=None)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 303)

        Solve the word problem.

        This method writes the group element as a product of the
        elements of the list ``gens``, or the standard generators of
        the parent of ``self`` if ``gens`` is ``None``.

        INPUT:

        - ``gens`` -- list/tuple/iterable of elements (or objects
          that can be converted to group elements), or ``None``
          (default); by default, the generators of the parent group
          are used

        OUTPUT:

        A factorization object that contains information about the
        order of factors and the exponents. A :exc:`ValueError` is raised
        if the group element cannot be written as a word in ``gens``.

        ALGORITHM:

        Use GAP, which has optimized algorithms for solving the word
        problem (the GAP functions ``EpimorphismFromFreeGroup`` and
        ``PreImagesRepresentative``).

        EXAMPLES::

            sage: G = GL(2,5); G
            General Linear Group of degree 2 over Finite Field of size 5
            sage: G.gens()
            (
            [2 0]  [4 1]
            [0 1], [4 0]
            )
            sage: G(1).word_problem([G.gen(0)])
            1
            sage: type(_)
            <class 'sage.structure.factorization.Factorization'>

            sage: g = G([0,4,1,4])
            sage: g.word_problem()
            ([4 1]
             [4 0])^-1

        Next we construct a more complicated element of the group from the
        generators::

            sage: s,t = G.0, G.1
            sage: a = (s * t * s); b = a.word_problem(); b
            ([2 0]
             [0 1]) *
            ([4 1]
             [4 0]) *
            ([2 0]
             [0 1])
            sage: flatten(b)
            [
            [2 0]     [4 1]     [2 0]
            [0 1], 1, [4 0], 1, [0 1], 1
            ]
            sage: b.prod() == a
            True

        We solve the word problem using some different generators::

            sage: s = G([2,0,0,1]); t = G([1,1,0,1]); u = G([0,-1,1,0])
            sage: a.word_problem([s,t,u])
            ([2 0]
             [0 1])^-1 *
            ([1 1]
             [0 1])^-1 *
            ([0 4]
             [1 0]) *
            ([2 0]
             [0 1])^-1

        We try some elements that don't actually generate the group::

            sage: a.word_problem([t,u])
            Traceback (most recent call last):
            ...
            ValueError: word problem has no solution

        AUTHORS:

        - David Joyner and William Stein
        - David Loeffler (2010): fixed some bugs
        - Volker Braun (2013): LibGAP"""
    @overload
    def word_problem(self) -> Any:
        """MatrixGroupElement_gap.word_problem(self, gens=None)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 303)

        Solve the word problem.

        This method writes the group element as a product of the
        elements of the list ``gens``, or the standard generators of
        the parent of ``self`` if ``gens`` is ``None``.

        INPUT:

        - ``gens`` -- list/tuple/iterable of elements (or objects
          that can be converted to group elements), or ``None``
          (default); by default, the generators of the parent group
          are used

        OUTPUT:

        A factorization object that contains information about the
        order of factors and the exponents. A :exc:`ValueError` is raised
        if the group element cannot be written as a word in ``gens``.

        ALGORITHM:

        Use GAP, which has optimized algorithms for solving the word
        problem (the GAP functions ``EpimorphismFromFreeGroup`` and
        ``PreImagesRepresentative``).

        EXAMPLES::

            sage: G = GL(2,5); G
            General Linear Group of degree 2 over Finite Field of size 5
            sage: G.gens()
            (
            [2 0]  [4 1]
            [0 1], [4 0]
            )
            sage: G(1).word_problem([G.gen(0)])
            1
            sage: type(_)
            <class 'sage.structure.factorization.Factorization'>

            sage: g = G([0,4,1,4])
            sage: g.word_problem()
            ([4 1]
             [4 0])^-1

        Next we construct a more complicated element of the group from the
        generators::

            sage: s,t = G.0, G.1
            sage: a = (s * t * s); b = a.word_problem(); b
            ([2 0]
             [0 1]) *
            ([4 1]
             [4 0]) *
            ([2 0]
             [0 1])
            sage: flatten(b)
            [
            [2 0]     [4 1]     [2 0]
            [0 1], 1, [4 0], 1, [0 1], 1
            ]
            sage: b.prod() == a
            True

        We solve the word problem using some different generators::

            sage: s = G([2,0,0,1]); t = G([1,1,0,1]); u = G([0,-1,1,0])
            sage: a.word_problem([s,t,u])
            ([2 0]
             [0 1])^-1 *
            ([1 1]
             [0 1])^-1 *
            ([0 4]
             [1 0]) *
            ([2 0]
             [0 1])^-1

        We try some elements that don't actually generate the group::

            sage: a.word_problem([t,u])
            Traceback (most recent call last):
            ...
            ValueError: word problem has no solution

        AUTHORS:

        - David Joyner and William Stein
        - David Loeffler (2010): fixed some bugs
        - Volker Braun (2013): LibGAP"""
    def __hash__(self) -> Any:
        """MatrixGroupElement_gap.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 89)

        TESTS::

            sage: MS = MatrixSpace(GF(3), 2)
            sage: G = MatrixGroup([MS([1,1,0,1]), MS([1,0,1,1])])
            sage: g = G.an_element()
            sage: hash(g)
            -5306160029685893860  # 64-bit
            -181258980            # 32-bit"""
    def __reduce__(self) -> Any:
        """MatrixGroupElement_gap.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/groups/matrix_gps/group_element_gap.pyx (starting at line 75)

        Implement pickling.

        TESTS::

            sage: MS = MatrixSpace(GF(3), 2, 2)
            sage: G = MatrixGroup(MS([[1,0],[0,1]]), MS([[1,1],[0,1]]))
            sage: loads(G.gen(0).dumps())
            [1 0]
            [0 1]"""
