import _cython_3_2_1
import sage as sage
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

lift_to_sl2z: _cython_3_2_1.cython_function_or_method
lift_to_sl2z_int: _cython_3_2_1.cython_function_or_method
lift_to_sl2z_llong: _cython_3_2_1.cython_function_or_method
p1_normalize: _cython_3_2_1.cython_function_or_method
p1_normalize_int: _cython_3_2_1.cython_function_or_method
p1_normalize_llong: _cython_3_2_1.cython_function_or_method
p1list: _cython_3_2_1.cython_function_or_method
p1list_int: _cython_3_2_1.cython_function_or_method
p1list_llong: _cython_3_2_1.cython_function_or_method

class P1List:
    """P1List(int N)

    File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 677)

    The class for `\\mathbb{P}^1(\\ZZ/N\\ZZ)`, the projective line modulo `N`.

    EXAMPLES::

        sage: P = P1List(12); P
        The projective line over the integers modulo 12
        sage: list(P)
        [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 1), (2, 3), (2, 5), (3, 1), (3, 2), (3, 4), (3, 7), (4, 1), (4, 3), (4, 5), (6, 1)]

    Saving and loading works.

    ::

        sage: loads(dumps(P)) == P
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intN) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 695)

                The constructor for the class P1List.

                INPUT:

                - ``N`` -- positive integer (the modulus or level)

                OUTPUT: a P1List object representing `\\mathbb{P}^1(\\ZZ/N\\ZZ)`

                EXAMPLES::

                    sage: L = P1List(120) # indirect doctest
                    sage: L
                    The projective line over the integers modulo 120
        """
    @overload
    def N(self) -> Any:
        """P1List.N(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1165)

        Return the level or modulus of this P1List.

        EXAMPLES::

            sage: L = P1List(120)
            sage: L.N()
            120"""
    @overload
    def N(self) -> Any:
        """P1List.N(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1165)

        Return the level or modulus of this P1List.

        EXAMPLES::

            sage: L = P1List(120)
            sage: L.N()
            120"""
    def apply_I(self, inti) -> Any:
        """P1List.apply_I(self, int i)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 885)

        Return the index of the result of applying the matrix
        `I=[-1,0;0,1]` to the `i`-th element of this P1List.

        INPUT:

        - ``i`` -- integer (the index of the element to act on)

        EXAMPLES::

            sage: L = P1List(120)
            sage: L[10]
            (1, 9)
            sage: L.apply_I(10)
            112
            sage: L[112]
            (1, 111)
            sage: L.normalize(-1,9)
            (1, 111)

        This operation is an involution::

            sage: all(L.apply_I(L.apply_I(i)) == i for i in range(len(L)))
            True"""
    def apply_S(self, inti) -> Any:
        """P1List.apply_S(self, int i)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 917)

        Return the index of the result of applying the matrix
        `S=[0,-1;1,0]` to the `i`-th element of this P1List.

        INPUT:

        - ``i`` -- integer (the index of the element to act on)

        EXAMPLES::

            sage: L = P1List(120)
            sage: L[10]
            (1, 9)
            sage: L.apply_S(10)
            159
            sage: L[159]
            (3, 13)
            sage: L.normalize(-9,1)
            (3, 13)

        This operation is an involution::

            sage: all(L.apply_S(L.apply_S(i)) == i for i in range(len(L)))
            True"""
    def apply_T(self, inti) -> Any:
        """P1List.apply_T(self, int i)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 949)

        Return the index of the result of applying the matrix
        `T=[0,1;-1,-1]` to the `i`-th element of this P1List.

        INPUT:

        - ``i`` -- integer (the index of the element to act on)

        EXAMPLES::

            sage: L = P1List(120)
            sage: L[10]
            (1, 9)
            sage: L.apply_T(10)
            157
            sage: L[157]
            (3, 10)
            sage: L.normalize(9,-10)
            (3, 10)

        This operation has order three::

            sage: all(L.apply_T(L.apply_T(L.apply_T(i))) == i for i in range(len(L)))
            True"""
    def index(self, intu, intv) -> Any:
        """P1List.index(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 981)

        Return the index of the class of `(u,v)` in the fixed list
        of representatives of
        `\\mathbb{P}^1(\\ZZ/N\\ZZ)`.

        INPUT:

        - ``u``, ``v`` -- integers with `\\gcd(u,v,N)=1`

        OUTPUT:

        - ``i`` -- the index of `u`, `v`, in the P1list

        EXAMPLES::

            sage: L = P1List(120)
            sage: L[100]
            (1, 99)
            sage: L.index(1,99)
            100
            sage: all(L.index(L[i][0],L[i][1])==i for i in range(len(L)))
            True"""
    def index_of_normalized_pair(self, intu, intv) -> Any:
        """P1List.index_of_normalized_pair(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1062)

        Return the index of the class of `(u,v)` in the fixed list
        of representatives of
        `\\mathbb{P}^1(\\ZZ/N\\ZZ)`.

        INPUT:

        - ``u``, ``v`` -- integers with `\\gcd(u,v,N)=1`, normalized so they lie
          in the list

        OUTPUT:

        - ``i`` -- the index of `(u:v)`, in the P1list

        EXAMPLES::

            sage: L = P1List(120)
            sage: L[100]
            (1, 99)
            sage: L.index_of_normalized_pair(1,99)
            100
            sage: all(L.index_of_normalized_pair(L[i][0],L[i][1])==i for i in range(len(L)))
            True"""
    def lift_to_sl2z(self, inti) -> Any:
        """P1List.lift_to_sl2z(self, int i)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 843)

        Lift the `i`-th element of this P1list to an element of
        `SL(2,\\ZZ)`.

        If the `i`-th element is `(c,d)`, this function computes and
        returns a list `[a,b, c',d']` that defines a 2x2 matrix
        with determinant 1 and integer entries, such that `c=c'` (mod
        `N`) and `d=d'` (mod `N`).

        INPUT:

        - ``i`` -- integer (the index of the element to lift)

        EXAMPLES::

            sage: p = P1List(11)
            sage: p.list()[3]
            (1, 2)

            sage: p.lift_to_sl2z(3)
            [0, -1, 1, 2]

        AUTHORS:

        - Justin Walker"""
    @overload
    def list(self) -> Any:
        """P1List.list(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1092)

        Return the underlying list of this :class:`P1List` object.

        EXAMPLES::

            sage: L = P1List(8)
            sage: type(L)
            <... 'sage.modular.modsym.p1list.P1List'>
            sage: type(L.list())
            <... 'list'>"""
    @overload
    def list(self) -> Any:
        """P1List.list(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1092)

        Return the underlying list of this :class:`P1List` object.

        EXAMPLES::

            sage: L = P1List(8)
            sage: type(L)
            <... 'sage.modular.modsym.p1list.P1List'>
            sage: type(L.list())
            <... 'list'>"""
    def normalize(self, intu, intv) -> Any:
        """P1List.normalize(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1106)

        Return a normalised element of `\\mathbb{P}^1(\\ZZ/N\\ZZ)`.

        INPUT:

        - ``u``, ``v`` -- integers with `\\gcd(u,v,N)=1`

        OUTPUT: a 2-tuple ``(uu,vv)`` where `(uu:vv)` is a *normalized*
        representative of `(u:v)`

        NOTE: See also normalize_with_scalar() which also returns the
        normalizing scalar.

        EXAMPLES::

            sage: L = P1List(120)
            sage: (u,v) = (555555555,7777)
            sage: uu,vv = L.normalize(555555555,7777)
            sage: (uu,vv)
            (15, 13)
            sage: (uu*v-vv*u) % L.N() == 0
            True"""
    def normalize_with_scalar(self, intu, intv) -> Any:
        """P1List.normalize_with_scalar(self, int u, int v)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 1134)

        Return a normalised element of `\\mathbb{P}^1(\\ZZ/N\\ZZ)`, together with
        the normalizing scalar.

        INPUT:

        - ``u``, ``v`` -- integers with `\\gcd(u,v,N)=1`

        OUTPUT:

        - a 3-tuple ``(uu,vv,ss)`` where `(uu:vv)` is a *normalized*
          representative of `(u:v)`, and `ss` is a scalar such that
          `(ss*uu, ss*vv) = (u,v)` (mod `N`).

        EXAMPLES::

            sage: L = P1List(120)
            sage: (u,v) = (555555555,7777)
            sage: uu,vv,ss = L.normalize_with_scalar(555555555,7777)
            sage: (uu,vv)
            (15, 13)
            sage: ((ss*uu-u)%L.N(), (ss*vv-v)%L.N())
            (0, 0)
            sage: (uu*v-vv*u) % L.N() == 0
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, n) -> Any:
        """P1List.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 797)

        Standard indexing/slicing function for the class ``P1List``.

        EXAMPLES::

            sage: L = P1List(8)
            sage: list(L) # indirect doctest
            [(0, 1),
            (1, 0),
            ...
            (2, 3),
            (4, 1)]
            sage: L[4:8] # indirect doctest
            [(1, 3), (1, 4), (1, 5), (1, 6)]"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """P1List.__len__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 819)

        Return the length of this P1List.

        EXAMPLES::

            sage: L = P1List(8)
            sage: len(L) # indirect doctest
            12"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    @overload
    def __reduce__(self) -> Any:
        """P1List.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 785)

        Helper function used in pickling.

        EXAMPLES::

            sage: L = P1List(8)
            sage: L.__reduce__()
            (<... 'sage.modular.modsym.p1list.P1List'>, (8,))"""
    @overload
    def __reduce__(self) -> Any:
        """P1List.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/modsym/p1list.pyx (starting at line 785)

        Helper function used in pickling.

        EXAMPLES::

            sage: L = P1List(8)
            sage: L.__reduce__()
            (<... 'sage.modular.modsym.p1list.P1List'>, (8,))"""

class export:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
