import _cython_3_2_1
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.modular.cusps import Cusp as Cusp
from sage.rings.infinity import Infinity as Infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_ManinSymbol: _cython_3_2_1.cython_function_or_method

class ManinSymbol(sage.structure.element.Element):
    """ManinSymbol(parent, t)

    File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 61)

    A Manin symbol `[X^i Y^{k-2-i}, (u, v)]`.

    INPUT:

    - ``parent`` -- :class:`~sage.modular.modsym.manin_symbol_list.ManinSymbolList`

    - ``t`` -- a triple `(i, u, v)` of integers

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol import ManinSymbol
        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
        sage: m = ManinSymbolList_gamma0(5,2)
        sage: s = ManinSymbol(m,(2,2,3)); s
        (2,3)
        sage: s == loads(dumps(s))
        True

    ::

        sage: m = ManinSymbolList_gamma0(5,8)
        sage: s = ManinSymbol(m,(2,2,3)); s
        [X^2*Y^4,(2,3)]

    ::

        sage: from sage.modular.modsym.manin_symbol import ManinSymbol
        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
        sage: m = ManinSymbolList_gamma0(5,8)
        sage: s = ManinSymbol(m,(2,2,3))
        sage: s.parent()
        Manin Symbol List of weight 8 for Gamma0(5)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    i: i
    u: u
    v: v
    def __init__(self, parent, t) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 96)

                Create a Manin symbol `[X^i Y^{k-2-i}, (u, v)]`, where
                `k` is the weight.

                INPUT:

                - ``parent`` -- :class:`~sage.modular.modsym.manin_symbol_list.ManinSymbolList`

                - ``t`` -- a triple `(i, u, v)` of integers

                EXAMPLES::

                    sage: from sage.modular.modsym.manin_symbol import ManinSymbol
                    sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
                    sage: m = ManinSymbolList_gamma0(5,2)
                    sage: s = ManinSymbol(m,(2,2,3)); s
                    (2,3)

                ::

                    sage: m = ManinSymbolList_gamma0(5,8)
                    sage: s = ManinSymbol(m,(2,2,3)); s
                    [X^2*Y^4,(2,3)]
        """
    def apply(self, a, b, c, d) -> Any:
        """ManinSymbol.apply(self, a, b, c, d)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 290)

        Return the image of ``self`` under the matrix `[a,b;c,d]`.

        Not implemented for raw ManinSymbol objects, only for members
        of ManinSymbolLists.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,2)
            sage: m.apply(10,[1,0,0,1]) # not implemented for base class"""
    def endpoints(self, N=...) -> Any:
        """ManinSymbol.endpoints(self, N=None)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 383)

        Return cusps `alpha`, `beta` such that this Manin symbol, viewed as a
        symbol for level `N`, is `X^i*Y^{k-2-i} \\{alpha, beta\\}`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3)); s
            [X^2*Y^4,(2,3)]
            sage: s.endpoints()
            (1/3, 1/2)"""
    @overload
    def level(self) -> Any:
        """ManinSymbol.level(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 422)

        Return the level of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.level()
            5"""
    @overload
    def level(self) -> Any:
        """ManinSymbol.level(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 422)

        Return the level of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.level()
            5"""
    def lift_to_sl2z(self, N=...) -> Any:
        """ManinSymbol.lift_to_sl2z(self, N=None)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 322)

        Return a lift of this Manin symbol to `SL_2(\\ZZ)`.

        If this Manin symbol is `(c,d)` and `N` is its level, this
        function returns a list `[a,b, c',d']` that defines a 2x2
        matrix with determinant 1 and integer entries, such that
        `c=c'` (mod `N`) and `d=d'` (mod `N`).

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s
            [X^2*Y^4,(2,3)]
            sage: s.lift_to_sl2z()
            [1, 1, 2, 3]"""
    @overload
    def modular_symbol_rep(self) -> Any:
        """ManinSymbol.modular_symbol_rep(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 437)

        Return a representation of ``self`` as a formal sum of modular
        symbols.

        The result is not cached.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.modular_symbol_rep()
             144*X^6*{1/3, 1/2} - 384*X^5*Y*{1/3, 1/2} + 424*X^4*Y^2*{1/3, 1/2} - 248*X^3*Y^3*{1/3, 1/2} + 81*X^2*Y^4*{1/3, 1/2} - 14*X*Y^5*{1/3, 1/2} + Y^6*{1/3, 1/2}"""
    @overload
    def modular_symbol_rep(self) -> Any:
        """ManinSymbol.modular_symbol_rep(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 437)

        Return a representation of ``self`` as a formal sum of modular
        symbols.

        The result is not cached.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.modular_symbol_rep()
             144*X^6*{1/3, 1/2} - 384*X^5*Y*{1/3, 1/2} + 424*X^4*Y^2*{1/3, 1/2} - 248*X^3*Y^3*{1/3, 1/2} + 81*X^2*Y^4*{1/3, 1/2} - 14*X*Y^5*{1/3, 1/2} + Y^6*{1/3, 1/2}"""
    @overload
    def tuple(self) -> Any:
        """ManinSymbol.tuple(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 158)

        Return the 3-tuple `(i,u,v)` of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.tuple()
            (2, 2, 3)"""
    @overload
    def tuple(self) -> Any:
        """ManinSymbol.tuple(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 158)

        Return the 3-tuple `(i,u,v)` of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.tuple()
            (2, 2, 3)"""
    @overload
    def weight(self) -> Any:
        """ManinSymbol.weight(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 407)

        Return the weight of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.weight()
            8"""
    @overload
    def weight(self) -> Any:
        """ManinSymbol.weight(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 407)

        Return the weight of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s.weight()
            8"""
    def __copy__(self) -> Any:
        """ManinSymbol.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 306)

        Return a copy of this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s2 = copy(s)
            sage: s2
            [X^2*Y^4,(2,3)]"""
    def __hash__(self) -> Any:
        """ManinSymbol.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 239)

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,2)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: hash(s)  # random
            7331463901"""
    def __mul__(self, matrix) -> Any:
        """ManinSymbol.__mul__(self, matrix)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 255)

        Return the result of applying a matrix to this Manin symbol.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,2)
            sage: s = ManinSymbol(m,(0,2,3))
            sage: s*[1,2,0,1]
            (2,7)

        ::

            sage: m = ManinSymbolList_gamma0(5,8)
            sage: s = ManinSymbol(m,(2,2,3))
            sage: s*[1,2,0,1]
            Traceback (most recent call last):
            ...
            NotImplementedError: ModSym * Matrix only implemented in weight 2"""
    def __reduce__(self) -> Any:
        """ManinSymbol.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/manin_symbol.pyx (starting at line 127)

        For pickling.

        TESTS::

            sage: from sage.modular.modsym.manin_symbol import ManinSymbol
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma1
            sage: m = ManinSymbolList_gamma1(3, 2)
            sage: s = ManinSymbol(m, (2, 2, 3))
            sage: loads(dumps(s))
            (2,3)"""
    def __rmul__(self, other):
        """Return value*self."""
