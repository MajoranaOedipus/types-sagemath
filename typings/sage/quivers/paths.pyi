import _cython_3_2_1
import sage.structure.element
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

NewQuiverPath: _cython_3_2_1.cython_function_or_method

class QuiverPath(sage.structure.element.MonoidElement):
    '''QuiverPath(parent, start, end, path)

    File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 29)

    Class for paths in a quiver.

    A path is given by two vertices, ``start`` and ``end``, and a finite
    (possibly empty) list of edges `e_1, e_2, \\ldots, e_n` such that the
    initial vertex of `e_1` is ``start``, the final vertex of `e_i` is
    the initial vertex of `e_{i+1}`, and the final vertex of `e_n` is
    ``end``.  In the case where no edges are specified, we must have
    ``start = end`` and the path is called the trivial path at the given
    vertex.

    .. NOTE::

        Do *not* use this constructor directly! Instead, pass the input to the
        path semigroup that shall be the parent of this path.

    EXAMPLES:

    Specify a path by giving a list of edges::

        sage: Q = DiGraph({1:{2:[\'a\',\'d\'], 3:[\'e\']}, 2:{3:[\'b\']}, 3:{1:[\'f\'], 4:[\'c\']}})
        sage: F = Q.path_semigroup()
        sage: p = F([(1, 2, \'a\'), (2, 3, \'b\')])
        sage: p
        a*b

    Paths are not *unique*, but different representations of "the same" path
    yield *equal* paths::

        sage: q = F([(1, 1)]) * F([(1, 2, \'a\'), (2, 3, \'b\')]) * F([(3, 3)])
        sage: p is q
        False
        sage: p == q
        True

    The ``*`` operator is concatenation of paths. If the two paths do not
    compose, its result is ``None``::

        sage: print(p*q)
        None
        sage: p*F([(3, 4, \'c\')])
        a*b*c
        sage: F([(2,3,\'b\'), (3,1,\'f\')])*p
        b*f*a*b

    The length of a path is the number of edges in that path.  Trivial paths
    are therefore length-`0`::

        sage: len(p)
        2
        sage: triv = F([(1, 1)])
        sage: len(triv)
        0

    List index and slice notation can be used to access the edges in a path.
    QuiverPaths can also be iterated over.  Trivial paths have no elements::

        sage: for x in p: print(x)
        (1, 2, \'a\')
        (2, 3, \'b\')
        sage: list(triv)
        []

    There are methods giving the initial and terminal vertex of a path::

        sage: p.initial_vertex()
        1
        sage: p.terminal_vertex()
        3'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, start, end, path) -> Any:
        """File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 125)

                Create a path object.  Type ``QuiverPath?`` for more information.

                INPUT:

                - ``parent`` -- a path semigroup
                - ``start`` -- integer; the label of the initial vertex
                - ``end`` -- integer; the label of the terminal vertex
                - ``path`` -- list of integers, providing the list of arrows
                  occurring in the path, labelled according to the position in
                  the list of all arrows (resp. the list of outgoing arrows at
                  each vertex)

                TESTS::

                    sage: from sage.quivers.paths import QuiverPath
                    sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
                    sage: p = Q([(1, 1)]) * Q([(1, 1)])
                    sage: Q([(1,3,'x')])
                    Traceback (most recent call last):
                    ...
                    ValueError: (1, 3, 'x') is not an edge

                Note that QuiverPath should not be called directly, because
                the elements of the path semigroup associated with a quiver
                may use a sub-class of QuiverPath. Nonetheless, just for test, we
                show that it *is* possible to create a path in a deprecated way::

                    sage: p == QuiverPath(Q, 1, 1, [])
                    True
                    sage: list(Q([(1, 1)])*Q([(1, 2, 'a')])*Q([(2, 2)])*Q([(2, 3, 'b')])*Q([(3, 3)]))
                    [(1, 2, 'a'), (2, 3, 'b')]
        """
    def complement(self, QuiverPathsubpath) -> tuple:
        """QuiverPath.complement(self, QuiverPath subpath) -> tuple

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 604)

        Return a pair ``(a,b)`` of paths s.t. ``self = a*subpath*b``,
        or ``(None, None)`` if ``subpath`` is not a subpath of this path.

        .. NOTE::

            ``a`` is chosen of minimal length.

        EXAMPLES::

            sage: S = DiGraph({1:{1:['a','b','c','d']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_1, a, b, c, d
            sage: (b*c*a*d*b*a*d*d).complement(a*d)
            (b*c, b*a*d*d)
            sage: (b*c*a*d*b).complement(a*c)
            (None, None)"""
    @overload
    def degree(self) -> Any:
        """QuiverPath.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 220)

        Return the length of the path.

        ``length()`` and ``degree()`` are aliases

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: len(Q([(1, 2, 'a'), (2, 3, 'b')]))
            2
            sage: Q([(1, 1)]).degree()
            0
            sage: Q([(1, 2, 'a')]).length()
            1"""
    @overload
    def degree(self) -> Any:
        """QuiverPath.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 220)

        Return the length of the path.

        ``length()`` and ``degree()`` are aliases

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: len(Q([(1, 2, 'a'), (2, 3, 'b')]))
            2
            sage: Q([(1, 1)]).degree()
            0
            sage: Q([(1, 2, 'a')]).length()
            1"""
    @overload
    def gcd(self, QuiverPathP) -> Any:
        '''QuiverPath.gcd(self, QuiverPath P)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 544)

        Greatest common divisor of two quiver paths, with co-factors.

        For paths, by "greatest common divisor", we mean the largest terminal
        segment of the first path that is an initial segment of the second
        path.

        INPUT:

        - ``P`` -- a :class:`QuiverPath`

        OUTPUT:

        - :class:`QuiverPath`s ``(C1,G,C2)`` such that ``self = C1*G`` and ``P = G*C2``, or
        - ``(None, None, None)``, if the paths do not overlap (or belong to different quivers).

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\']}, 2:{1:[\'b\'], 3:[\'c\']}, 3:{1:[\'d\']}}).path_semigroup()
            sage: p1 = Q([\'c\',\'d\',\'a\',\'b\',\'a\',\'c\',\'d\'])
            sage: p1
            c*d*a*b*a*c*d
            sage: p2 = Q([\'a\',\'b\',\'a\',\'c\',\'d\',\'a\',\'c\',\'d\',\'a\',\'b\'])
            sage: p2
            a*b*a*c*d*a*c*d*a*b
            sage: S1, G, S2 = p1.gcd(p2)
            sage: S1, G, S2
            (c*d, a*b*a*c*d, a*c*d*a*b)
            sage: S1*G == p1
            True
            sage: G*S2 == p2
            True
            sage: p2.gcd(p1)
            (a*b*a*c*d*a, c*d*a*b, a*c*d)

        We test that a full overlap is detected::

            sage: p2.gcd(p2)
            (e_1, a*b*a*c*d*a*c*d*a*b, e_1)

        The absence of an overlap is detected::

            sage: p2[2:-1]
            a*c*d*a*c*d*a
            sage: p2[1:]
            b*a*c*d*a*c*d*a*b
            sage: print(p2[2:-1].gcd(p2[1:]))
            (None, None, None)'''
    @overload
    def gcd(self, p2) -> Any:
        '''QuiverPath.gcd(self, QuiverPath P)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 544)

        Greatest common divisor of two quiver paths, with co-factors.

        For paths, by "greatest common divisor", we mean the largest terminal
        segment of the first path that is an initial segment of the second
        path.

        INPUT:

        - ``P`` -- a :class:`QuiverPath`

        OUTPUT:

        - :class:`QuiverPath`s ``(C1,G,C2)`` such that ``self = C1*G`` and ``P = G*C2``, or
        - ``(None, None, None)``, if the paths do not overlap (or belong to different quivers).

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\']}, 2:{1:[\'b\'], 3:[\'c\']}, 3:{1:[\'d\']}}).path_semigroup()
            sage: p1 = Q([\'c\',\'d\',\'a\',\'b\',\'a\',\'c\',\'d\'])
            sage: p1
            c*d*a*b*a*c*d
            sage: p2 = Q([\'a\',\'b\',\'a\',\'c\',\'d\',\'a\',\'c\',\'d\',\'a\',\'b\'])
            sage: p2
            a*b*a*c*d*a*c*d*a*b
            sage: S1, G, S2 = p1.gcd(p2)
            sage: S1, G, S2
            (c*d, a*b*a*c*d, a*c*d*a*b)
            sage: S1*G == p1
            True
            sage: G*S2 == p2
            True
            sage: p2.gcd(p1)
            (a*b*a*c*d*a, c*d*a*b, a*c*d)

        We test that a full overlap is detected::

            sage: p2.gcd(p2)
            (e_1, a*b*a*c*d*a*c*d*a*b, e_1)

        The absence of an overlap is detected::

            sage: p2[2:-1]
            a*c*d*a*c*d*a
            sage: p2[1:]
            b*a*c*d*a*c*d*a*b
            sage: print(p2[2:-1].gcd(p2[1:]))
            (None, None, None)'''
    @overload
    def gcd(self, p1) -> Any:
        '''QuiverPath.gcd(self, QuiverPath P)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 544)

        Greatest common divisor of two quiver paths, with co-factors.

        For paths, by "greatest common divisor", we mean the largest terminal
        segment of the first path that is an initial segment of the second
        path.

        INPUT:

        - ``P`` -- a :class:`QuiverPath`

        OUTPUT:

        - :class:`QuiverPath`s ``(C1,G,C2)`` such that ``self = C1*G`` and ``P = G*C2``, or
        - ``(None, None, None)``, if the paths do not overlap (or belong to different quivers).

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\']}, 2:{1:[\'b\'], 3:[\'c\']}, 3:{1:[\'d\']}}).path_semigroup()
            sage: p1 = Q([\'c\',\'d\',\'a\',\'b\',\'a\',\'c\',\'d\'])
            sage: p1
            c*d*a*b*a*c*d
            sage: p2 = Q([\'a\',\'b\',\'a\',\'c\',\'d\',\'a\',\'c\',\'d\',\'a\',\'b\'])
            sage: p2
            a*b*a*c*d*a*c*d*a*b
            sage: S1, G, S2 = p1.gcd(p2)
            sage: S1, G, S2
            (c*d, a*b*a*c*d, a*c*d*a*b)
            sage: S1*G == p1
            True
            sage: G*S2 == p2
            True
            sage: p2.gcd(p1)
            (a*b*a*c*d*a, c*d*a*b, a*c*d)

        We test that a full overlap is detected::

            sage: p2.gcd(p2)
            (e_1, a*b*a*c*d*a*c*d*a*b, e_1)

        The absence of an overlap is detected::

            sage: p2[2:-1]
            a*c*d*a*c*d*a
            sage: p2[1:]
            b*a*c*d*a*c*d*a*b
            sage: print(p2[2:-1].gcd(p2[1:]))
            (None, None, None)'''
    @overload
    def gcd(self, p2) -> Any:
        '''QuiverPath.gcd(self, QuiverPath P)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 544)

        Greatest common divisor of two quiver paths, with co-factors.

        For paths, by "greatest common divisor", we mean the largest terminal
        segment of the first path that is an initial segment of the second
        path.

        INPUT:

        - ``P`` -- a :class:`QuiverPath`

        OUTPUT:

        - :class:`QuiverPath`s ``(C1,G,C2)`` such that ``self = C1*G`` and ``P = G*C2``, or
        - ``(None, None, None)``, if the paths do not overlap (or belong to different quivers).

        EXAMPLES::

            sage: Q = DiGraph({1:{2:[\'a\']}, 2:{1:[\'b\'], 3:[\'c\']}, 3:{1:[\'d\']}}).path_semigroup()
            sage: p1 = Q([\'c\',\'d\',\'a\',\'b\',\'a\',\'c\',\'d\'])
            sage: p1
            c*d*a*b*a*c*d
            sage: p2 = Q([\'a\',\'b\',\'a\',\'c\',\'d\',\'a\',\'c\',\'d\',\'a\',\'b\'])
            sage: p2
            a*b*a*c*d*a*c*d*a*b
            sage: S1, G, S2 = p1.gcd(p2)
            sage: S1, G, S2
            (c*d, a*b*a*c*d, a*c*d*a*b)
            sage: S1*G == p1
            True
            sage: G*S2 == p2
            True
            sage: p2.gcd(p1)
            (a*b*a*c*d*a, c*d*a*b, a*c*d)

        We test that a full overlap is detected::

            sage: p2.gcd(p2)
            (e_1, a*b*a*c*d*a*c*d*a*b, e_1)

        The absence of an overlap is detected::

            sage: p2[2:-1]
            a*c*d*a*c*d*a
            sage: p2[1:]
            b*a*c*d*a*c*d*a*b
            sage: print(p2[2:-1].gcd(p2[1:]))
            (None, None, None)'''
    @overload
    def has_prefix(self, QuiverPathsubpath) -> bool:
        """QuiverPath.has_prefix(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 667)

        Tells whether this path starts with a given sub-path.

        INPUT:

        - ``subpath`` -- a path in the same path semigroup as this path

        OUTPUT: ``0`` or ``1``, which stands for ``False`` resp. ``True``

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_prefix(b*e)
            0
            sage: (c*b*e*a).has_prefix(c*b)
            1
            sage: (c*b*e*a).has_prefix(e_1)
            1
            sage: (c*b*e*a).has_prefix(e_2)
            0"""
    @overload
    def has_prefix(self, e_1) -> Any:
        """QuiverPath.has_prefix(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 667)

        Tells whether this path starts with a given sub-path.

        INPUT:

        - ``subpath`` -- a path in the same path semigroup as this path

        OUTPUT: ``0`` or ``1``, which stands for ``False`` resp. ``True``

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_prefix(b*e)
            0
            sage: (c*b*e*a).has_prefix(c*b)
            1
            sage: (c*b*e*a).has_prefix(e_1)
            1
            sage: (c*b*e*a).has_prefix(e_2)
            0"""
    @overload
    def has_prefix(self, e_2) -> Any:
        """QuiverPath.has_prefix(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 667)

        Tells whether this path starts with a given sub-path.

        INPUT:

        - ``subpath`` -- a path in the same path semigroup as this path

        OUTPUT: ``0`` or ``1``, which stands for ``False`` resp. ``True``

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_prefix(b*e)
            0
            sage: (c*b*e*a).has_prefix(c*b)
            1
            sage: (c*b*e*a).has_prefix(e_1)
            1
            sage: (c*b*e*a).has_prefix(e_2)
            0"""
    @overload
    def has_subpath(self, QuiverPathsubpath) -> bool:
        """QuiverPath.has_subpath(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 628)

        Tells whether this path contains a given sub-path.

        INPUT:

        - ``subpath`` -- a path of positive length in the same path semigroup
          as this path

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_subpath(b*e)
            1
            sage: (c*b*e*a).has_subpath(b*f)
            0
            sage: (c*b*e*a).has_subpath(e_1)
            Traceback (most recent call last):
            ...
            ValueError: we only consider sub-paths of positive length
            sage: (c*b*e*a).has_subpath(None)
            Traceback (most recent call last):
            ...
            ValueError: the given sub-path is empty"""
    @overload
    def has_subpath(self, e_1) -> Any:
        """QuiverPath.has_subpath(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 628)

        Tells whether this path contains a given sub-path.

        INPUT:

        - ``subpath`` -- a path of positive length in the same path semigroup
          as this path

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_subpath(b*e)
            1
            sage: (c*b*e*a).has_subpath(b*f)
            0
            sage: (c*b*e*a).has_subpath(e_1)
            Traceback (most recent call last):
            ...
            ValueError: we only consider sub-paths of positive length
            sage: (c*b*e*a).has_subpath(None)
            Traceback (most recent call last):
            ...
            ValueError: the given sub-path is empty"""
    @overload
    def has_subpath(self, _None) -> Any:
        """QuiverPath.has_subpath(self, QuiverPath subpath) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 628)

        Tells whether this path contains a given sub-path.

        INPUT:

        - ``subpath`` -- a path of positive length in the same path semigroup
          as this path

        EXAMPLES::

            sage: S = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup()
            sage: S.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: (c*b*e*a).has_subpath(b*e)
            1
            sage: (c*b*e*a).has_subpath(b*f)
            0
            sage: (c*b*e*a).has_subpath(e_1)
            Traceback (most recent call last):
            ...
            ValueError: we only consider sub-paths of positive length
            sage: (c*b*e*a).has_subpath(None)
            Traceback (most recent call last):
            ...
            ValueError: the given sub-path is empty"""
    @overload
    def initial_vertex(self) -> Any:
        """QuiverPath.initial_vertex(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 701)

        Return the initial vertex of the path.

        OUTPUT: integer; the label of the initial vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: y = Q([(1, 2, 'a'), (2, 3, 'b')])
            sage: y.initial_vertex()
            1"""
    @overload
    def initial_vertex(self) -> Any:
        """QuiverPath.initial_vertex(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 701)

        Return the initial vertex of the path.

        OUTPUT: integer; the label of the initial vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: y = Q([(1, 2, 'a'), (2, 3, 'b')])
            sage: y.initial_vertex()
            1"""
    @overload
    def length(self) -> Any:
        """QuiverPath.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 220)

        Return the length of the path.

        ``length()`` and ``degree()`` are aliases

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: len(Q([(1, 2, 'a'), (2, 3, 'b')]))
            2
            sage: Q([(1, 1)]).degree()
            0
            sage: Q([(1, 2, 'a')]).length()
            1"""
    @overload
    def length(self) -> Any:
        """QuiverPath.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 220)

        Return the length of the path.

        ``length()`` and ``degree()`` are aliases

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: len(Q([(1, 2, 'a'), (2, 3, 'b')]))
            2
            sage: Q([(1, 1)]).degree()
            0
            sage: Q([(1, 2, 'a')]).length()
            1"""
    @overload
    def reversal(self) -> Any:
        """QuiverPath.reversal(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 731)

        Return the path along the same edges in reverse order in the
        opposite quiver.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}, 3:{4:['c'], 1:['d']}}).path_semigroup()
            sage: p = Q([(1, 2, 'a'), (2, 3, 'b'), (3, 1, 'd'), (1, 2, 'a'), (2, 3, 'b'), (3, 4, 'c')])
            sage: p
            a*b*d*a*b*c
            sage: p.reversal()
            c*b*a*d*b*a
            sage: e = Q.idempotents()[0]
            sage: e
            e_1
            sage: e.reversal()
            e_1"""
    @overload
    def reversal(self) -> Any:
        """QuiverPath.reversal(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 731)

        Return the path along the same edges in reverse order in the
        opposite quiver.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}, 3:{4:['c'], 1:['d']}}).path_semigroup()
            sage: p = Q([(1, 2, 'a'), (2, 3, 'b'), (3, 1, 'd'), (1, 2, 'a'), (2, 3, 'b'), (3, 4, 'c')])
            sage: p
            a*b*d*a*b*c
            sage: p.reversal()
            c*b*a*d*b*a
            sage: e = Q.idempotents()[0]
            sage: e
            e_1
            sage: e.reversal()
            e_1"""
    @overload
    def reversal(self) -> Any:
        """QuiverPath.reversal(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 731)

        Return the path along the same edges in reverse order in the
        opposite quiver.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}, 3:{4:['c'], 1:['d']}}).path_semigroup()
            sage: p = Q([(1, 2, 'a'), (2, 3, 'b'), (3, 1, 'd'), (1, 2, 'a'), (2, 3, 'b'), (3, 4, 'c')])
            sage: p
            a*b*d*a*b*c
            sage: p.reversal()
            c*b*a*d*b*a
            sage: e = Q.idempotents()[0]
            sage: e
            e_1
            sage: e.reversal()
            e_1"""
    @overload
    def terminal_vertex(self) -> Any:
        """QuiverPath.terminal_vertex(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 716)

        Return the terminal vertex of the path.

        OUTPUT: integer; the label of the terminal vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: y = Q([(1, 2, 'a'), (2, 3, 'b')])
            sage: y.terminal_vertex()
            3"""
    @overload
    def terminal_vertex(self) -> Any:
        """QuiverPath.terminal_vertex(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 716)

        Return the terminal vertex of the path.

        OUTPUT: integer; the label of the terminal vertex

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: y = Q([(1, 2, 'a'), (2, 3, 'b')])
            sage: y.terminal_vertex()
            3"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __getitem__(self, index) -> Any:
        """QuiverPath.__getitem__(self, index)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 347)

        Implement index notation.

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}, 3:{4:['c'], 1:['d']}}).path_semigroup()
            sage: p = Q([(1, 2, 'a'), (2, 3, 'b'), (3, 1, 'd'), (1, 2, 'a'), (2, 3, 'b'), (3, 4, 'c')])
            sage: p
            a*b*d*a*b*c

        A single index returns the arrow that appears in the path at this index::

            sage: p[0]
            a
            sage: p[-1]
            c

        A slice with step 1 returns a sub-path of this path::

            sage: p[1:5]
            b*d*a*b

        A slice with step -1 return a sub-path of the reversed path::

            sage: p[4:1:-1]
            b*a*d

        If the start index is greater than the terminal index and the step
        -1 is not explicitly given, then a path of length zero is returned,
        which is compatible with Python lists::

            sage: list(range(6))[4:1]
            []

        The following was fixed in :issue:`22278`. A path slice of length
        zero of course has a specific start- and endpoint. It is always
        the startpoint of the arrow corresponding to the first item of
        the range::

            sage: p[4:1]
            e_2
            sage: p[4:1].initial_vertex() == p[4].initial_vertex()
            True

        If the slice boundaries are out of bound, then no error is raised,
        which is compatible with Python lists::

            sage: list(range(6))[20:40]
            []

        In that case, the startpoint of the slice of length zero is the
        endpoint of the path::

            sage: p[20:40]
            e_4
            sage: p[20:40].initial_vertex() == p.terminal_vertex()
            True"""
    def __hash__(self) -> Any:
        """QuiverPath.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 179)

        TESTS::

            sage: from sage.quivers.paths import QuiverPath
            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: p = Q(['a']) * Q(['b'])
            sage: q = Q([(1, 1)])
            sage: {p:1, q:2}[Q(['a','b'])]    # indirect doctest
            1"""
    def __iter__(self) -> Any:
        """QuiverPath.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 445)

        Iteration over the path.

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}, 3:{4:['c']}}).path_semigroup()
            sage: p = Q([(1, 2, 'a'), (2, 3, 'b'), (3, 4, 'c')])
            sage: for e in p: print(e)
            (1, 2, 'a')
            (2, 3, 'b')
            (3, 4, 'c')"""
    def __len__(self) -> Any:
        """QuiverPath.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 220)

        Return the length of the path.

        ``length()`` and ``degree()`` are aliases

        TESTS::

            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: len(Q([(1, 2, 'a'), (2, 3, 'b')]))
            2
            sage: Q([(1, 1)]).degree()
            0
            sage: Q([(1, 2, 'a')]).length()
            1"""
    def __reduce__(self) -> Any:
        """QuiverPath.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/paths.pyx (starting at line 164)

        TESTS::

            sage: from sage.quivers.paths import QuiverPath
            sage: Q = DiGraph({1:{2:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: p = Q(['a']) * Q(['b'])
            sage: loads(dumps(p)) == p   # indirect doctest
            True
            sage: loads(dumps(p)) is p
            False"""
