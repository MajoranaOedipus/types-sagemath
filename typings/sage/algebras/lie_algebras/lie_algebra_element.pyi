import sage.modules.with_basis.indexed_element
import sage.structure.element
import sage.structure.element_wrapper
import sage.structure.sage_object
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FreeLieAlgebraElement(LieAlgebraElement):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1481)

        An element of a free Lie algebra.
    """
    @overload
    def lift(self) -> Any:
        """FreeLieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1488)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: a = Lyn([z, [[x, y], x]]); a
            [x, [x, [y, z]]] + [x, [[x, z], y]] - [[x, y], [x, z]]
            sage: a.lift()
            x^2*y*z - 2*x*y*x*z + y*x^2*z - z*x^2*y + 2*z*x*y*x - z*y*x^2"""
    @overload
    def lift(self) -> Any:
        """FreeLieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1488)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: a = Lyn([z, [[x, y], x]]); a
            [x, [x, [y, z]]] + [x, [[x, z], y]] - [[x, y], [x, z]]
            sage: a.lift()
            x^2*y*z - 2*x*y*x*z + y*x^2*z - z*x^2*y + 2*z*x*y*x - z*y*x^2"""
    @overload
    def list(self) -> Any:
        """FreeLieAlgebraElement.list(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1511)

        Return ``self`` as a list of pairs ``(m, c)`` where ``m`` is a
        basis key (i.e., a key of one of the basis elements)
        and ``c`` is its coefficient.

        This list is sorted from highest to lowest degree.

        EXAMPLES::

            sage: L.<x, y> = LieAlgebra(QQ)
            sage: elt = x + L.bracket(y, x)
            sage: elt.list()
            [([x, y], -1), (x, 1)]"""
    @overload
    def list(self) -> Any:
        """FreeLieAlgebraElement.list(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1511)

        Return ``self`` as a list of pairs ``(m, c)`` where ``m`` is a
        basis key (i.e., a key of one of the basis elements)
        and ``c`` is its coefficient.

        This list is sorted from highest to lowest degree.

        EXAMPLES::

            sage: L.<x, y> = LieAlgebra(QQ)
            sage: elt = x + L.bracket(y, x)
            sage: elt.list()
            [([x, y], -1), (x, 1)]"""

class GradedLieBracket(LieBracket):
    """GradedLieBracket(LieObject l, LieObject r, grade)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1967)

    A Lie bracket (:class:`LieBracket`) for a graded Lie algebra.

    Unlike the vanilla Lie bracket class, this also stores a
    degree, and uses it as a first criterion when comparing
    graded Lie brackets.
    (Graded Lie brackets still compare greater than Lie
    generators.)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LieObjectl, LieObjectr, grade) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1977)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, GradedLieBracket
                    sage: x = LieGenerator('x', 0)
                    sage: y = LieGenerator('y', 1)
                    sage: b = GradedLieBracket(x, y, 2)
                    sage: TestSuite(b).run()
        """
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """GradedLieBracket.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 2037)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, GradedLieBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: z = LieGenerator('z', 2)
            sage: b = GradedLieBracket(x, y, 2)
            sage: hash(b) == hash(b)
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """GradedLieBracket.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1992)

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, GradedLieBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: b = GradedLieBracket(x, y, 2)
            sage: loads(dumps(b)) == b
            True"""

class LieAlgebraElement(sage.modules.with_basis.indexed_element.IndexedFreeModuleElement):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 30)

        A Lie algebra element.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def lift(self) -> Any:
        """LieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 143)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: x.lift().parent() == L.universal_enveloping_algebra()
            True

        TESTS::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: x = L.basis()[2]
            sage: y = L.basis()[3]
            sage: x.lift()
            b2
            sage: y.lift()
            b3
            sage: x * y
            b2*b3
            sage: y * x
            b2*b3 + b0

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.an_element()
            d[-1] + d[0] - 3*d[1]
            sage: L.an_element().lift()
            PBW[-1] + PBW[0] - 3*PBW[1]"""
    @overload
    def lift(self) -> Any:
        """LieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 143)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: x.lift().parent() == L.universal_enveloping_algebra()
            True

        TESTS::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: x = L.basis()[2]
            sage: y = L.basis()[3]
            sage: x.lift()
            b2
            sage: y.lift()
            b3
            sage: x * y
            b2*b3
            sage: y * x
            b2*b3 + b0

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.an_element()
            d[-1] + d[0] - 3*d[1]
            sage: L.an_element().lift()
            PBW[-1] + PBW[0] - 3*PBW[1]"""
    @overload
    def lift(self) -> Any:
        """LieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 143)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: x.lift().parent() == L.universal_enveloping_algebra()
            True

        TESTS::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: x = L.basis()[2]
            sage: y = L.basis()[3]
            sage: x.lift()
            b2
            sage: y.lift()
            b3
            sage: x * y
            b2*b3
            sage: y * x
            b2*b3 + b0

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.an_element()
            d[-1] + d[0] - 3*d[1]
            sage: L.an_element().lift()
            PBW[-1] + PBW[0] - 3*PBW[1]"""
    @overload
    def lift(self) -> Any:
        """LieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 143)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: x.lift().parent() == L.universal_enveloping_algebra()
            True

        TESTS::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: x = L.basis()[2]
            sage: y = L.basis()[3]
            sage: x.lift()
            b2
            sage: y.lift()
            b3
            sage: x * y
            b2*b3
            sage: y * x
            b2*b3 + b0

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.an_element()
            d[-1] + d[0] - 3*d[1]
            sage: L.an_element().lift()
            PBW[-1] + PBW[0] - 3*PBW[1]"""
    @overload
    def lift(self) -> Any:
        """LieAlgebraElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 143)

        Lift ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'):{'z':1}})
            sage: x.lift().parent() == L.universal_enveloping_algebra()
            True

        TESTS::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: x = L.basis()[2]
            sage: y = L.basis()[3]
            sage: x.lift()
            b2
            sage: y.lift()
            b3
            sage: x * y
            b2*b3
            sage: y * x
            b2*b3 + b0

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.an_element()
            d[-1] + d[0] - 3*d[1]
            sage: L.an_element().lift()
            PBW[-1] + PBW[0] - 3*PBW[1]"""
    def __mul__(self, left, right) -> Any:
        """LieAlgebraElement.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 35)

        If we are multiplying two nonzero elements, automatically
        lift up to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: y*x
            x*y - z

        Check that actions work::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: d = L.basis()
            sage: M = L.chargeless_representation(1/2, 3/4)
            sage: d[-5] * M.basis()[10]
            -47/4*v[5]

        TESTS::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: int(3) * x
            3*x
            sage: x * int(3)
            3*x
            sage: y * x.lift()
            x*y - z
            sage: y.lift() * x
            x*y - z"""
    def __rmul__(self, other):
        """Return value*self."""

class LieAlgebraElementWrapper(sage.structure.element_wrapper.ElementWrapper):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 194)

        Wrap an element as a Lie algebra element.

        TESTS:

        We check comparisons::

            sage: L = lie_algebras.sl(QQ, 2, representation='matrix')
            sage: L.bracket(L.gen(0), L.gen(1)) == -L.bracket(L.gen(1), L.gen(0))
            True

        The next doctests show similar behavior, although on elements of
        other classes::

            sage: L = lie_algebras.three_dimensional_by_rank(QQ, 3)
            sage: L.bracket(L.gen(0), L.gen(1)) == -L.bracket(L.gen(1), L.gen(0))
            True

            sage: L = lie_algebras.three_dimensional_by_rank(QQ, 1)
            sage: L.bracket(L.gen(0), L.gen(1)) == -L.bracket(L.gen(1), L.gen(0))
            True

        Check inequality::

            sage: L = lie_algebras.sl(QQ, 2, representation='matrix')
            sage: L.bracket(L.gen(0), L.gen(1)) != -L.bracket(L.gen(1), L.gen(0))
            False
            sage: L.zero() == 0
            True
            sage: L.zero() != 0
            False

        The next doctests show similar behavior, although on elements of
        other classes::

            sage: L = lie_algebras.three_dimensional_by_rank(QQ, 3)
            sage: L.bracket(L.gen(0), L.gen(1)) != -L.bracket(L.gen(1), L.gen(0))
            False
            sage: L.an_element()
            X + Y + Z
            sage: L.an_element() == 0
            False
            sage: L.an_element() != 0
            True

            sage: L = lie_algebras.three_dimensional_by_rank(QQ, 1)
            sage: L.bracket(L.gen(0), L.gen(1)) != -L.bracket(L.gen(1), L.gen(0))
            False
            sage: L.zero() == 0
            True
            sage: L.zero() != 0
            False
            sage: L.zero() >= 0
            True
            sage: L.zero() < 0
            False

        We check the display of elements::

            sage: R = FreeAlgebra(QQ, 3, 'x')
            sage: L.<l0,l1,l2> = LieAlgebra(associative=R.gens())
            sage: elt = l0 + l1
            sage: elt
            x0 + x1
            sage: latex(elt)
            x_{0} + x_{1}

            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LieAlgebra(associative=s)
            sage: P = Partition([4,2,2,1])
            sage: x = L.basis()[P]
            sage: ascii_art(x)
            s
             ****
             **
             **
             *
            sage: unicode_art(x)
            s
             ┌┬┬┬┐
             ├┼┼┴┘
             ├┼┤
             ├┼┘
             └┘
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __getitem__(self, i) -> Any:
        """LieAlgebraElementWrapper.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 465)

        Redirect the ``__getitem__()`` to the wrapped element.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 2, representation='matrix')
            sage: m = L.gen(0)
            sage: m[0,0]
            0
            sage: m[0][1]
            1"""
    @overload
    def __getitem__(self) -> Any:
        """LieAlgebraElementWrapper.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 465)

        Redirect the ``__getitem__()`` to the wrapped element.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 2, representation='matrix')
            sage: m = L.gen(0)
            sage: m[0,0]
            0
            sage: m[0][1]
            1"""
    def __iter__(self) -> Any:
        """LieAlgebraElementWrapper.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 480)

        Iterate over ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: S = G.algebra(QQ)
            sage: L = LieAlgebra(associative=S)
            sage: x = L.an_element() + L.basis()[G.one()]
            sage: x
            2*() + (2,3) + (1,2) + (1,2,3) + (1,3,2) + (1,3)
            sage: sorted(x)
            [((), 2), ((2,3), 1), ((1,2), 1), ((1,2,3), 1),
             ((1,3,2), 1), ((1,3), 1)]"""
    def __mul__(self, left, right) -> Any:
        """LieAlgebraElementWrapper.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 322)

        If we are multiplying two nonzero elements, automatically
        lift up to the universal enveloping algebra.

        .. TODO::

            Write more tests for this method.

        EXAMPLES::

            sage: S = SymmetricGroup(3).algebra(QQ)
            sage: L = LieAlgebra(associative=S)
            sage: x = L.gen(2); x
            (1,2,3)
            sage: y = L.gen(3); y
            (2,3)
            sage: u = x*3; u
            3*(1,2,3)
            sage: parent(u) == L
            True
            sage: u = x*(3/2); u
            3/2*(1,2,3)
            sage: parent(u) == L
            True
            sage: elt = x*y - y*x; elt
            b4 - b5
            sage: xp, yp = x.lift_associative(), y.lift_associative()
            sage: eltp = xp*yp - yp*xp; eltp
            -(1,2) + (1,3)
            sage: G = list(S.basis())
            sage: G[4] - G[5]
            -(1,2) + (1,3)

        TESTS::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L.<x,y> = LieAlgebra(associative=S.gens())
            sage: int(3) * x
            3*(1,2,3)
            sage: y * int(3)
            3*(1,2)"""
    def __neg__(self) -> Any:
        """LieAlgebraElementWrapper.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 452)

        Return the negation of ``self``.

        EXAMPLES::

            sage: R = FreeAlgebra(QQ, 3, 'x,y,z')
            sage: L.<x,y,z> = LieAlgebra(associative=R.gens())
            sage: -x
            -x"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, x) -> Any:
        """LieAlgebraElementWrapper.__truediv__(self, x)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 399)

        Division by coefficients.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 3)
            sage: x = L.an_element(); x
            p1
            sage: x / 2
            1/2*p1"""

class LieAlgebraMatrixWrapper(LieAlgebraElementWrapper):
    """LieAlgebraMatrixWrapper(parent, value)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 501)

    Lie algebra element wrapper around a matrix."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, value) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 505)

                Initialize ``self``.

                EXAMPLES::

                    sage: L = lie_algebras.Heisenberg(QQ, 1, representation='matrix')
                    sage: z = L.z()
                    sage: z.value.is_immutable()
                    True
        """

class LieBracket(LieObject):
    """LieBracket(LieObject l, LieObject r)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1747)

    An abstract Lie bracket (formally, just a binary tree)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LieObjectl, LieObjectr) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1751)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
                    sage: x = LieGenerator('x', 0)
                    sage: y = LieGenerator('y', 1)
                    sage: z = LieBracket(x, y)
                    sage: TestSuite(z).run()
        """
    @overload
    def lift(self, dictUEA_gens_dict) -> Any:
        """LieBracket.lift(self, dict UEA_gens_dict)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1917)

        Lift ``self`` to the universal enveloping algebra.

        ``UEA_gens_dict`` should be the dictionary for the
        generators of the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: a = Lyn([z, [[x, y], x]]); a
            [x, [x, [y, z]]] + [x, [[x, z], y]] - [[x, y], [x, z]]
            sage: a.lift() # indirect doctest
            x^2*y*z - 2*x*y*x*z + y*x^2*z - z*x^2*y + 2*z*x*y*x - z*y*x^2"""
    @overload
    def lift(self) -> Any:
        """LieBracket.lift(self, dict UEA_gens_dict)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1917)

        Lift ``self`` to the universal enveloping algebra.

        ``UEA_gens_dict`` should be the dictionary for the
        generators of the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: a = Lyn([z, [[x, y], x]]); a
            [x, [x, [y, z]]] + [x, [[x, z], y]] - [[x, y], [x, z]]
            sage: a.lift() # indirect doctest
            x^2*y*z - 2*x*y*x*z + y*x^2*z - z*x^2*y + 2*z*x*y*x - z*y*x^2"""
    @overload
    def to_word(self) -> tuple:
        '''LieBracket.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1946)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
            sage: x = LieGenerator(\'x\', 0)
            sage: y = LieGenerator(\'y\', 1)
            sage: b = LieBracket(x, y)
            sage: c = LieBracket(b, x)
            sage: c.to_word()
            (\'x\', \'y\', \'x\')'''
    @overload
    def to_word(self) -> Any:
        '''LieBracket.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1946)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
            sage: x = LieGenerator(\'x\', 0)
            sage: y = LieGenerator(\'y\', 1)
            sage: b = LieBracket(x, y)
            sage: c = LieBracket(b, x)
            sage: c.to_word()
            (\'x\', \'y\', \'x\')'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """LieBracket.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1812)

        Return the `i`-th item of ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: z = LieBracket(x, y)
            sage: z[0]
            x
            sage: z[1] is y
            True
            sage: z[2]
            Traceback (most recent call last):
            ...
            IndexError: must be either 0 or 1"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LieBracket.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1877)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: z = LieGenerator('z', 2)
            sage: b = LieBracket(x, y)
            sage: hash(b) == hash(b)
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """LieBracket.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1769)

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LieBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: z = LieBracket(x, y)
            sage: loads(dumps(z)) == z
            True"""

class LieGenerator(LieObject):
    """LieGenerator(name, index)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1597)

    A wrapper around an object so it can ducktype with and do
    comparison operations with :class:`LieBracket`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, index) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1602)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator
                    sage: x = LieGenerator('x', 0)
                    sage: TestSuite(x).run()
        """
    @overload
    def lift(self, dictUEA_gens_dict) -> Any:
        """LieGenerator.lift(self, dict UEA_gens_dict)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1728)

        Lift ``self`` to the universal enveloping algebra.

        ``UEA_gens_dict`` should be the dictionary for the
        generators of the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: x.lift()
            x
            sage: x.lift().parent()
            Free Algebra on 3 generators (x, y, z) over Rational Field"""
    @overload
    def lift(self) -> Any:
        """LieGenerator.lift(self, dict UEA_gens_dict)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1728)

        Lift ``self`` to the universal enveloping algebra.

        ``UEA_gens_dict`` should be the dictionary for the
        generators of the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: x.lift()
            x
            sage: x.lift().parent()
            Free Algebra on 3 generators (x, y, z) over Rational Field"""
    @overload
    def lift(self) -> Any:
        """LieGenerator.lift(self, dict UEA_gens_dict)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1728)

        Lift ``self`` to the universal enveloping algebra.

        ``UEA_gens_dict`` should be the dictionary for the
        generators of the universal enveloping algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 'x,y,z')
            sage: Lyn = L.Lyndon()
            sage: x,y,z = Lyn.gens()
            sage: x.lift()
            x
            sage: x.lift().parent()
            Free Algebra on 3 generators (x, y, z) over Rational Field"""
    @overload
    def to_word(self) -> tuple:
        '''LieGenerator.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1712)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator
            sage: x = LieGenerator(\'x\', 0)
            sage: x.to_word()
            (\'x\',)'''
    @overload
    def to_word(self) -> Any:
        '''LieGenerator.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1712)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator
            sage: x = LieGenerator(\'x\', 0)
            sage: x.to_word()
            (\'x\',)'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LieGenerator.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1641)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator
            sage: x = LieGenerator('x', 0)
            sage: hash(x) == hash('x')
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """LieGenerator.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1616)

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator
            sage: x = LieGenerator('x', 0)
            sage: loads(dumps(x)) == x
            True"""

class LieObject(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1574)

        Abstract base class for :class:`LieGenerator` and :class:`LieBracket`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def to_word(self) -> tuple:
        '''LieObject.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1578)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        TESTS::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieObject
            sage: x = LieObject()
            sage: x.to_word()
            Traceback (most recent call last):
            ...
            NotImplementedError'''
    @overload
    def to_word(self) -> Any:
        '''LieObject.to_word(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1578)

        Return the word ("flattening") of ``self``.

        If ``self`` is a tree of Lie brackets, this word is
        usually obtained by "forgetting the brackets".

        TESTS::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieObject
            sage: x = LieObject()
            sage: x.to_word()
            Traceback (most recent call last):
            ...
            NotImplementedError'''

class LieSubalgebraElementWrapper(LieAlgebraElementWrapper):
    """LieSubalgebraElementWrapper(parent, value)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 520)

    Wrap an element of the ambient Lie algebra as an element."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, value) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 524)

                Initialize ``self``.

                TESTS::

                    sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
                    sage: S = L.subalgebra([X, Y])
                    sage: TestSuite(S(X)).run()
        """
    @overload
    def monomial_coefficients(self, boolcopy=...) -> dict:
        """LieSubalgebraElementWrapper.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 613)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``;
          if ``False``, then this can cause undesired behavior by
          mutating ``d``

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 3}
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 9}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """LieSubalgebraElementWrapper.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 613)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``;
          if ``False``, then this can cause undesired behavior by
          mutating ``d``

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 3}
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 9}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """LieSubalgebraElementWrapper.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 613)

        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``self`` is internally
          represented by a dictionary ``d``, then make a copy of ``d``;
          if ``False``, then this can cause undesired behavior by
          mutating ``d``

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 3}
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2(2*Y + 9*Z).monomial_coefficients()
            {'Y': 2, 'Z': 9}"""
    @overload
    def to_vector(self) -> Any:
        """LieSubalgebraElementWrapper._vector_(self, sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 581)

        Return the vector in ``g.module()`` corresponding to the
        element ``self`` of ``g`` (where ``g`` is the parent of ``self``).

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S.basis()
            Finite family {'X': X, 'Y': Y, 'Z': 3*Z}
            sage: S(2*Y + 9*Z).to_vector()
            (0, 2, 9)
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2.basis()
            Finite family {'Y': Y, 'Z': Z}
            sage: S2(2*Y + 9*Z).to_vector()
            (0, 2, 9)

        TESTS::

            sage: L.<X,Y> = LieAlgebra(ZZ, abelian=True)
            sage: S = L.subalgebra(X)
            sage: S(X).to_vector() in S.module()
            True
            sage: S(X).to_vector().parent() is S.module()
            True"""
    @overload
    def to_vector(self) -> Any:
        """LieSubalgebraElementWrapper._vector_(self, sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 581)

        Return the vector in ``g.module()`` corresponding to the
        element ``self`` of ``g`` (where ``g`` is the parent of ``self``).

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S.basis()
            Finite family {'X': X, 'Y': Y, 'Z': 3*Z}
            sage: S(2*Y + 9*Z).to_vector()
            (0, 2, 9)
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2.basis()
            Finite family {'Y': Y, 'Z': Z}
            sage: S2(2*Y + 9*Z).to_vector()
            (0, 2, 9)

        TESTS::

            sage: L.<X,Y> = LieAlgebra(ZZ, abelian=True)
            sage: S = L.subalgebra(X)
            sage: S(X).to_vector() in S.module()
            True
            sage: S(X).to_vector().parent() is S.module()
            True"""
    @overload
    def to_vector(self) -> Any:
        """LieSubalgebraElementWrapper._vector_(self, sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 581)

        Return the vector in ``g.module()`` corresponding to the
        element ``self`` of ``g`` (where ``g`` is the parent of ``self``).

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S.basis()
            Finite family {'X': X, 'Y': Y, 'Z': 3*Z}
            sage: S(2*Y + 9*Z).to_vector()
            (0, 2, 9)
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2.basis()
            Finite family {'Y': Y, 'Z': Z}
            sage: S2(2*Y + 9*Z).to_vector()
            (0, 2, 9)

        TESTS::

            sage: L.<X,Y> = LieAlgebra(ZZ, abelian=True)
            sage: S = L.subalgebra(X)
            sage: S(X).to_vector() in S.module()
            True
            sage: S(X).to_vector().parent() is S.module()
            True"""
    @overload
    def to_vector(self) -> Any:
        """LieSubalgebraElementWrapper._vector_(self, sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 581)

        Return the vector in ``g.module()`` corresponding to the
        element ``self`` of ``g`` (where ``g`` is the parent of ``self``).

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z': 3}})
            sage: S = L.subalgebra([X, Y])
            sage: S.basis()
            Finite family {'X': X, 'Y': Y, 'Z': 3*Z}
            sage: S(2*Y + 9*Z).to_vector()
            (0, 2, 9)
            sage: S2 = L.subalgebra([Y, Z])
            sage: S2.basis()
            Finite family {'Y': Y, 'Z': Z}
            sage: S2(2*Y + 9*Z).to_vector()
            (0, 2, 9)

        TESTS::

            sage: L.<X,Y> = LieAlgebra(ZZ, abelian=True)
            sage: S = L.subalgebra(X)
            sage: S(X).to_vector() in S.module()
            True
            sage: S(X).to_vector().parent() is S.module()
            True"""
    def __getitem__(self, i) -> Any:
        """LieSubalgebraElementWrapper.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 537)

        Return the coefficient of ``self`` indexed by ``i``.

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: S = L.subalgebra([X, Y])
            sage: S.indices()
            {'X', 'Y', 'Z'}
            sage: el = S(2*Y + 9*Z)
            sage: el['Y']
            2
            sage: el['Z']
            9"""

class LyndonBracket(GradedLieBracket):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 2055)

        A Lie bracket (:class:`LieBracket`) tailored for the Lyndon
        basis.

        The order on these brackets is defined by `l < r`
        if `w(l) < w(r)`, where `w(l)` is the word corresponding
        to `l`.
        (This is also true if one or both of `l` and `r` is a
        :class:`LieGenerator`.)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LyndonBracket.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 2081)

        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.lie_algebra_element import LieGenerator, LyndonBracket
            sage: x = LieGenerator('x', 0)
            sage: y = LieGenerator('y', 1)
            sage: b = LyndonBracket(x, y, 2)
            sage: hash(b) == hash((0, 1))
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class StructureCoefficientsElement(LieAlgebraMatrixWrapper):
    """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 736)

        An element of a Lie algebra given by structure coefficients.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def bracket(self, right) -> Any:
        """StructureCoefficientsElement.bracket(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 799)

        Return the Lie bracket ``[self, right]``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}, ('y','z'): {'x':1}, ('z','x'): {'y':1}})
            sage: x.bracket(y)
            z
            sage: y.bracket(x)
            -z
            sage: (x + y - z).bracket(x - y + z)
            -2*y - 2*z"""
    @overload
    def bracket(self, y) -> Any:
        """StructureCoefficientsElement.bracket(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 799)

        Return the Lie bracket ``[self, right]``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}, ('y','z'): {'x':1}, ('z','x'): {'y':1}})
            sage: x.bracket(y)
            z
            sage: y.bracket(x)
            -z
            sage: (x + y - z).bracket(x - y + z)
            -2*y - 2*z"""
    @overload
    def bracket(self, x) -> Any:
        """StructureCoefficientsElement.bracket(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 799)

        Return the Lie bracket ``[self, right]``.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}, ('y','z'): {'x':1}, ('z','x'): {'y':1}})
            sage: x.bracket(y)
            z
            sage: y.bracket(x)
            -z
            sage: (x + y - z).bracket(x - y + z)
            -2*y - 2*z"""
    @overload
    def lift(self) -> Any:
        """StructureCoefficientsElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 902)

        Return the lift of ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
            sage: elt = x - 3/2 * y
            sage: l = elt.lift(); l
            x - 3/2*y
            sage: l.parent()
            Noncommutative Multivariate Polynomial Ring in x, y
             over Rational Field, nc-relations: {y*x: x*y - x}"""
    @overload
    def lift(self) -> Any:
        """StructureCoefficientsElement.lift(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 902)

        Return the lift of ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
            sage: elt = x - 3/2 * y
            sage: l = elt.lift(); l
            x - 3/2*y
            sage: l.parent()
            Noncommutative Multivariate Polynomial Ring in x, y
             over Rational Field, nc-relations: {y*x: x*y - x}"""
    @overload
    def monomial_coefficients(self, boolcopy=...) -> dict:
        """StructureCoefficientsElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 920)

        Return the monomial coefficients of ``self`` as a dictionary.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: a = 2*x - 3/2*y + z
            sage: a.monomial_coefficients()
            {'x': 2, 'y': -3/2, 'z': 1}
            sage: a = 2*x - 3/2*z
            sage: a.monomial_coefficients()
            {'x': 2, 'z': -3/2}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """StructureCoefficientsElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 920)

        Return the monomial coefficients of ``self`` as a dictionary.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: a = 2*x - 3/2*y + z
            sage: a.monomial_coefficients()
            {'x': 2, 'y': -3/2, 'z': 1}
            sage: a = 2*x - 3/2*z
            sage: a.monomial_coefficients()
            {'x': 2, 'z': -3/2}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """StructureCoefficientsElement.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 920)

        Return the monomial coefficients of ``self`` as a dictionary.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: a = 2*x - 3/2*y + z
            sage: a.monomial_coefficients()
            {'x': 2, 'y': -3/2, 'z': 1}
            sage: a = 2*x - 3/2*z
            sage: a.monomial_coefficients()
            {'x': 2, 'z': -3/2}"""
    @overload
    def to_vector(self, boolsparse=..., order=...) -> Any:
        """StructureCoefficientsElement.to_vector(self, bool sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 889)

        Return ``self`` as a vector.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: a = x + 3*y - z/2
            sage: a.to_vector()
            (1, 3, -1/2)"""
    @overload
    def to_vector(self) -> Any:
        """StructureCoefficientsElement.to_vector(self, bool sparse=False, order=None)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 889)

        Return ``self`` as a vector.

        EXAMPLES::

            sage: L.<x,y,z> = LieAlgebra(QQ, {('x','y'): {'z':1}})
            sage: a = x + 3*y - z/2
            sage: a.to_vector()
            (1, 3, -1/2)"""
    def __getitem__(self, i) -> Any:
        """StructureCoefficientsElement.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 937)

        Return the coefficient of the basis element indexed by ``i``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
            sage: elt = x - 3/2 * y
            sage: elt['y']
            -3/2"""
    def __iter__(self) -> Any:
        """StructureCoefficientsElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 856)

        Iterate over ``self``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {('x','y'): {'x':1}})
            sage: elt = x - 3/2 * y
            sage: list(elt)
            [('x', 1), ('y', -3/2)]"""

class UntwistedAffineLieAlgebraElement(sage.structure.element.Element):
    """UntwistedAffineLieAlgebraElement(parent, dict t_dict, c_coeff, d_coeff)

    File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 951)

    An element of an untwisted affine Lie algebra."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, dictt_dict, c_coeff, d_coeff) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 955)

                Initialize ``self``.

                TESTS::

                    sage: L = lie_algebras.Affine(QQ, ['A',2,1])
                    sage: x = L.an_element()
                    sage: TestSuite(x).run()
        """
    @overload
    def bracket(self, right) -> Any:
        """UntwistedAffineLieAlgebraElement.bracket(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1347)

        Return the Lie bracket ``[self, right]``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A',1,1])
            sage: e1,f1,h1,e0,f0,c,d = list(L.lie_algebra_generators())
            sage: e0.bracket(f0)
            (-h1)#t^0 + 4*c
            sage: e1.bracket(0)
            0
            sage: e1.bracket(1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
             'Affine Kac-Moody algebra of ['A', 1] in the Chevalley basis'
             and 'Integer Ring'"""
    @overload
    def bracket(self, f0) -> Any:
        """UntwistedAffineLieAlgebraElement.bracket(self, right)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1347)

        Return the Lie bracket ``[self, right]``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A',1,1])
            sage: e1,f1,h1,e0,f0,c,d = list(L.lie_algebra_generators())
            sage: e0.bracket(f0)
            (-h1)#t^0 + 4*c
            sage: e1.bracket(0)
            0
            sage: e1.bracket(1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
             'Affine Kac-Moody algebra of ['A', 1] in the Chevalley basis'
             and 'Integer Ring'"""
    @overload
    def c_coefficient(self) -> Any:
        """UntwistedAffineLieAlgebraElement.c_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1143)

        Return the coefficient of `c` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element() - 3 * L.c()
            sage: x.c_coefficient()
            -2"""
    @overload
    def c_coefficient(self) -> Any:
        """UntwistedAffineLieAlgebraElement.c_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1143)

        Return the coefficient of `c` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element() - 3 * L.c()
            sage: x.c_coefficient()
            -2"""
    def canonical_derivation(self) -> Any:
        """UntwistedAffineLieAlgebraElement.canonical_derivation(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1438)

        Return the canonical derivation `d` applied to ``self``.

        The canonical derivation `d` is defined as

        .. MATH::

            d(a \\otimes t^m + \\alpha c) = a \\otimes m t^m.

        Another formulation is by `d = t \\frac{d}{dt}`.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['E',6,1])
            sage: al = RootSystem(['E',6]).root_lattice().simple_roots()
            sage: x = L.basis()[al[2]+al[3]+2*al[4]+al[5],5] + 4*L.c() + L.d()
            sage: x.canonical_derivation()
            (5*E[alpha[2] + alpha[3] + 2*alpha[4] + alpha[5]])#t^5"""
    @overload
    def d_coefficient(self) -> Any:
        """UntwistedAffineLieAlgebraElement.d_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1156)

        Return the coefficient of `d` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element() + L.d()
            sage: x.d_coefficient()
            2"""
    @overload
    def d_coefficient(self) -> Any:
        """UntwistedAffineLieAlgebraElement.d_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1156)

        Return the coefficient of `d` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element() + L.d()
            sage: x.d_coefficient()
            2"""
    @overload
    def monomial_coefficients(self, boolcopy=...) -> Any:
        """UntwistedAffineLieAlgebraElement.monomial_coefficients(self, bool copy=True)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1317)

        Return the monomial coefficients of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['C',2,1])
            sage: x = L.an_element()
            sage: sorted(x.monomial_coefficients(), key=str)
            [(-2*alpha[1] - alpha[2], 1),
             (-alpha[1], 0),
             (-alpha[2], 0),
             (2*alpha[1] + alpha[2], -1),
             (alpha[1], 0),
             (alpha[2], 0),
             (alphacheck[1], 0),
             (alphacheck[2], 0),
             'c',
             'd']"""
    @overload
    def monomial_coefficients(self) -> Any:
        """UntwistedAffineLieAlgebraElement.monomial_coefficients(self, bool copy=True)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1317)

        Return the monomial coefficients of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['C',2,1])
            sage: x = L.an_element()
            sage: sorted(x.monomial_coefficients(), key=str)
            [(-2*alpha[1] - alpha[2], 1),
             (-alpha[1], 0),
             (-alpha[2], 0),
             (2*alpha[1] + alpha[2], -1),
             (alpha[1], 0),
             (alpha[2], 0),
             (alphacheck[1], 0),
             (alphacheck[2], 0),
             'c',
             'd']"""
    @overload
    def t_dict(self) -> dict:
        """UntwistedAffineLieAlgebraElement.t_dict(self) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1127)

        Return the ``dict``, whose keys are powers of `t` and values are
        elements of the classical Lie algebra, of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element()
            sage: x.t_dict()
            {-1: E[alpha[1]],
             0: E[alpha[1]] + h1 + E[-alpha[1]],
             1: E[-alpha[1]]}"""
    @overload
    def t_dict(self) -> Any:
        """UntwistedAffineLieAlgebraElement.t_dict(self) -> dict

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1127)

        Return the ``dict``, whose keys are powers of `t` and values are
        elements of the classical Lie algebra, of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.Affine(QQ, ['A',1,1])
            sage: x = L.an_element()
            sage: x.t_dict()
            {-1: E[alpha[1]],
             0: E[alpha[1]] + h1 + E[-alpha[1]],
             1: E[-alpha[1]]}"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __hash__(self) -> Any:
        """UntwistedAffineLieAlgebraElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 1197)

        Return the hash of ``self``.

        EXAMPLES::

            sage: asl = lie_algebras.Affine(QQ, ['A',4,1])
            sage: x = asl.an_element()
            sage: hash(x) == hash(x)
            True
            sage: hash(asl.zero())
            0"""
    def __reduce__(self) -> Any:
        """UntwistedAffineLieAlgebraElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/lie_algebras/lie_algebra_element.pyx (starting at line 971)

        Used in pickling.

        TESTS::

            sage: L = lie_algebras.Affine(QQ, ['B',3,1])
            sage: x = L.an_element()
            sage: loads(dumps(x)) == x
            True"""
