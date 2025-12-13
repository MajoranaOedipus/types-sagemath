from .apply import apply_to_monomial as apply_to_monomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.modular.modsym.manin_symbol import ManinSymbol as ManinSymbol
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

class ManinSymbolList(Parent):
    """
    Base class for lists of all Manin symbols for a given weight, group or character.
    """
    Element = ManinSymbol
    def __init__(self, weight, lst) -> None:
        """
        Constructor for a ManinSymbolList.

        INPUT:

        - ``weight`` -- the weight of the symbols

        - ``lst`` -- the list of symbols

        On construction, a ManinSymbolList constructs a dict for
        rapid determination of the index of any given symbol.

        This is a base class only; users will only directly construct
        objects in the derived classes ManinSymbolList_gamma0,
        ManinSymbolList_gamma1, ManinSymbolList_gamma_h,
        ManinSymbolList_gamma_character.  Many standard methods are
        only implemented in the derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: ManinSymbolList(6,P1List(11))
            <sage.modular.modsym.manin_symbol_list.ManinSymbolList_with_category object at ...>
        """
    def __richcmp__(self, right, op):
        """
        Comparison function for ManinSymbolList objects.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m1 = ManinSymbolList(6,P1List(11))
            sage: m2 = ManinSymbolList(6,P1List(13))
            sage: m3 = ManinSymbolList(4,P1List(11))
            sage: m1 < m2
            True
            sage: m2 < m3
            False
            sage: m1 < m3
            False
        """
    def symbol_list(self):
        """
        Return the list of symbols of ``self``.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6, P1List(11))
        """
    def __len__(self) -> int:
        """
        Return the length of this :class:`ManinSymbolList`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: len(m)
            12
        """
    def apply(self, j, X) -> None:
        """
        Apply the matrix `X = [a, b; c, d]` to the `j`-th Manin symbol.

        Implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.apply(10, [1,2,0,1])
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in derived classes
        """
    def apply_S(self, j) -> None:
        """
        Apply the matrix `S = [0, -1; 1, 0]` to the `j`-th Manin symbol.

        Implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.apply_S(10)
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in derived classes
        """
    def apply_I(self, j) -> None:
        """
        Apply the matrix `I = [-1, 0; 0, 1]` to the `j`-th Manin symbol.

        Implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.apply_I(10)
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in derived classes
        """
    def apply_T(self, j) -> None:
        """
        Apply the matrix `T = [0, 1; -1, -1]` to the `j`-th Manin symbol.

        Implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.apply_T(10)
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in derived classes
        """
    def apply_TT(self, j) -> None:
        """
        Apply the matrix `TT = T^2 = [-1, -1; 0, 1]` to the `j`-th
        Manin symbol.

        Implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.apply_TT(10)
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in derived classes
        """
    def index(self, x):
        """
        Return the index of ``x`` in the list of Manin symbols.

        INPUT:

        - ``x`` -- a triple of integers `(i, u, v)` defining a valid
          Manin symbol, which need not be normalized

        OUTPUT:

        integer -- the index of the normalized Manin symbol equivalent
        to `(i, u, v)`.  If ``x`` is not in ``self``, -1 is returned.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.index(m.symbol_list()[2])
            2
            sage: S = m.symbol_list()
            sage: all(i == m.index(S[i]) for i in range(len(S)))
            True
        """
    @cached_method
    def manin_symbol_list(self):
        """
        Return all the Manin symbols in ``self`` as a list.

        Cached for subsequent calls.

        OUTPUT:

        A list of :class:`ManinSymbol` objects, which is a copy of the
        complete list of Manin symbols.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.manin_symbol_list() # not implemented for the base class

        ::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(6, 4)
            sage: m.manin_symbol_list()
            [[Y^2,(0,1)],
            [Y^2,(1,0)],
            [Y^2,(1,1)],
            ...
            [X^2,(3,1)],
            [X^2,(3,2)]]
        """
    list = manin_symbol_list
    def manin_symbol(self, i):
        """
        Return the ``i``-th Manin symbol in this :class:`ManinSymbolList`.

        INPUT:

        - ``i`` -- integer; a valid index of a symbol in this list

        OUTPUT:

        :class:`ManinSymbol` -- the `i`-th Manin symbol in the list.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.manin_symbol(3) # not implemented for base class

        ::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(6, 4)
            sage: s = m.manin_symbol(3); s
            [Y^2,(1,2)]
            sage: type(s)
            <class 'sage.modular.modsym.manin_symbol.ManinSymbol'>
        """
    def normalize(self, x) -> None:
        """
        Return a normalized Manin symbol from ``x``.

        To be implemented in derived classes.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList
            sage: m = ManinSymbolList(6,P1List(11))
            sage: m.normalize((0,6,7)) # not implemented in base class
        """
    def weight(self):
        """
        Return the weight of the Manin symbols in this :class:`ManinSymbolList`.

        OUTPUT: integer; the weight of the Manin symbols in the list

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(6, 4)
            sage: m.weight()
            4
        """

class ManinSymbolList_group(ManinSymbolList):
    """
    Base class for Manin symbol lists for a given group.

    INPUT:

    - ``level`` -- integer level

    - ``weight`` -- integer weight

    - ``syms`` -- something with ``normalize`` and ``list`` methods,
      e.g. :class:`~sage.modular.modsym.p1list.P1List`

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_group
        sage: ManinSymbolList_group(11, 2, P1List(11))
        <sage.modular.modsym.manin_symbol_list.ManinSymbolList_group_with_category object at ...>
    """
    def __init__(self, level, weight, syms) -> None:
        """
        Constructor for class ManinSymbolList_group.

        INPUT:

        - ``level`` -- integer level

        - ``weight`` -- integer weight

        - ``syms`` -- something with ``normalize`` and ``list``
          methods, e.g. :class:`~sage.modular.modsym.p1list.P1List`

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_group
            sage: L = ManinSymbolList_group(11, 2, P1List(11)); L
            <sage.modular.modsym.manin_symbol_list.ManinSymbolList_group_with_category object at ...>
        """
    def level(self):
        """
        Return the level of this :class:`ManinSymbolList`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: ManinSymbolList_gamma0(5,2).level()
            5

        ::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma1
            sage: ManinSymbolList_gamma1(51,2).level()
            51

        ::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma_h
            sage: ManinSymbolList_gamma_h(GammaH(117, [4]),2).level()
            117
        """
    def apply_S(self, j):
        """
        Apply the matrix `S = [0, -1; 1, 0]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        ``(k, s)`` where k is the index of the symbol obtained by acting on the
        `j`-th symbol with `S`, and `s` is the parity of the `j`-th symbol
        (a Python ``int``, either 1 or -1).

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: m.apply_S(4)
            (40, 1)
            sage: [m.apply_S(i) for i in range(len(m))]
            [(37, 1),
            (36, 1),
            (41, 1),
            (39, 1),
            (40, 1),
            (38, 1),
            (31, -1),
            (30, -1),
            (35, -1),
            (33, -1),
            (34, -1),
            (32, -1),
            ...
            (4, 1),
            (2, 1)]
        """
    def apply_I(self, j):
        """
        Apply the matrix `I=[-1,0,0,1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        ``(k, s)`` where k is the index of the symbol obtained by acting on the
        `j`-th symbol with `I`, and `s` is the parity of the `j`-th symbol
        (a Python ``int``, either 1 or -1)

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: m.apply_I(4)
            (3, 1)
            sage: [m.apply_I(i) for i in range(10)]
            [(0, 1),
            (1, 1),
            (5, 1),
            (4, 1),
            (3, 1),
            (2, 1),
            (6, -1),
            (7, -1),
            (11, -1),
            (10, -1)]
        """
    def apply_T(self, j):
        """
        Apply the matrix `T=[0,1,-1,-1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT: see documentation for apply()

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: m.apply_T(4)
            [(3, 1), (9, -6), (15, 15), (21, -20), (27, 15), (33, -6), (39, 1)]
            sage: [m.apply_T(i) for i in range(10)]
            [[(5, 1), (11, -6), (17, 15), (23, -20), (29, 15), (35, -6), (41, 1)],
            [(0, 1), (6, -6), (12, 15), (18, -20), (24, 15), (30, -6), (36, 1)],
            [(4, 1), (10, -6), (16, 15), (22, -20), (28, 15), (34, -6), (40, 1)],
            [(2, 1), (8, -6), (14, 15), (20, -20), (26, 15), (32, -6), (38, 1)],
            [(3, 1), (9, -6), (15, 15), (21, -20), (27, 15), (33, -6), (39, 1)],
            [(1, 1), (7, -6), (13, 15), (19, -20), (25, 15), (31, -6), (37, 1)],
            [(5, 1), (11, -5), (17, 10), (23, -10), (29, 5), (35, -1)],
            [(0, 1), (6, -5), (12, 10), (18, -10), (24, 5), (30, -1)],
            [(4, 1), (10, -5), (16, 10), (22, -10), (28, 5), (34, -1)],
            [(2, 1), (8, -5), (14, 10), (20, -10), (26, 5), (32, -1)]]
        """
    def apply_TT(self, j):
        """
        Apply the matrix `TT=[-1,-1,0,1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT: see documentation for apply()

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: m.apply_TT(4)
            [(38, 1)]
            sage: [m.apply_TT(i) for i in range(10)]
            [[(37, 1)],
            [(41, 1)],
            [(39, 1)],
            [(40, 1)],
            [(38, 1)],
            [(36, 1)],
            [(31, -1), (37, 1)],
            [(35, -1), (41, 1)],
            [(33, -1), (39, 1)],
            [(34, -1), (40, 1)]]
        """
    def apply(self, j, m):
        """
        Apply the matrix `m = [a, b; c, d]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        - ``m = [a, b, c, d]`` a list of 4 integers, which defines a 2x2 matrix

        OUTPUT:

        a list of pairs `(j_i, \\alpha_i)`, where each `\\alpha_i` is a nonzero
        integer, `j_i` is an integer (index of the `j_i`-th Manin symbol), and
        `\\sum_i \\alpha_i\\*x_{j_i}` is the image of the `j`-th Manin symbol under
        the right action of the matrix [a,b;c,d]. Here the right action of
        `g = [a, b; c, d]` on a Manin symbol `[P(X,Y),(u,v)]` is
        `[P(aX+bY,cX+dY),(u,v)\\*g]`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: m.apply(40, [2,3,1,1])
            [(0, 729), (6, 2916), (12, 4860), (18, 4320),
             (24, 2160), (30, 576), (36, 64)]
        """
    def normalize(self, x):
        """
        Return the normalization of the Manin symbol ``x`` with
        respect to this list.

        INPUT:

        - ``x`` -- (3-tuple of ints) a tuple defining a ManinSymbol

        OUTPUT:

        ``(i,u,v)`` -- (3-tuple of ints) another tuple defining the associated
        normalized ManinSymbol

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: m = ManinSymbolList_gamma0(5,8)
            sage: [m.normalize(s.tuple()) for s in m.manin_symbol_list()][:10]
            [(0, 0, 1),
             (0, 1, 0),
             (0, 1, 1),
             (0, 1, 2),
             (0, 1, 3),
             (0, 1, 4),
             (1, 0, 1),
             (1, 1, 0),
             (1, 1, 1),
             (1, 1, 2)]
        """

class ManinSymbolList_gamma0(ManinSymbolList_group):
    """
    Class for Manin symbols for `\\Gamma_0(N)`.

    INPUT:

    - ``level`` -- integer; the level

    - ``weight`` -- integer; the weight

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
        sage: m = ManinSymbolList_gamma0(5,2); m
        Manin Symbol List of weight 2 for Gamma0(5)
        sage: m.manin_symbol_list()
        [(0,1), (1,0), (1,1), (1,2), (1,3), (1,4)]
        sage: m = ManinSymbolList_gamma0(6,4); m
        Manin Symbol List of weight 4 for Gamma0(6)
        sage: len(m)
        36
    """
    def __init__(self, level, weight) -> None:
        """
        Constructor for a ModularSymbolList for Gamma_0(N).

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma0
            sage: M11 = ManinSymbolList_gamma0(11,2)
            sage: M11
            Manin Symbol List of weight 2 for Gamma0(11)
            sage: M11 == loads(dumps(M11))
            True
        """

class ManinSymbolList_gamma1(ManinSymbolList_group):
    """
    Class for Manin symbols for `\\Gamma_1(N)`.

    INPUT:

    - ``level`` -- integer; the level

    - ``weight`` -- integer; the weight

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma1
        sage: m = ManinSymbolList_gamma1(5,2); m
        Manin Symbol List of weight 2 for Gamma1(5)
        sage: m.manin_symbol_list()
        [(0,1),
        (0,2),
        (0,3),
        ...
        (4,3),
        (4,4)]
        sage: m = ManinSymbolList_gamma1(6,4); m
        Manin Symbol List of weight 4 for Gamma1(6)
        sage: len(m)
        72
        sage: m == loads(dumps(m))
        True
    """
    def __init__(self, level, weight) -> None:
        """
        Constructor for a ModularSymbolList for `\\Gamma_0(N)`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma1
            sage: M11 = ManinSymbolList_gamma1(11,2)
            sage: M11
            Manin Symbol List of weight 2 for Gamma1(11)
        """

class ManinSymbolList_gamma_h(ManinSymbolList_group):
    """
    Class for Manin symbols for `\\Gamma_H(N)`.

    INPUT:

    - ``group`` -- integer; the congruence subgroup

    - ``weight`` -- integer; the weight

    EXAMPLES::

        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma_h
        sage: G = GammaH(117, [4])
        sage: m = ManinSymbolList_gamma_h(G,2); m
        Manin Symbol List of weight 2 for Congruence Subgroup Gamma_H(117) with H generated by [4]
        sage: m.manin_symbol_list()[100:110]
        [(1,88),
        (1,89),
        (1,90),
        (1,91),
        (1,92),
        (1,93),
        (1,94),
        (1,95),
        (1,96),
        (1,97)]
        sage: len(m.manin_symbol_list())
        2016
        sage: m == loads(dumps(m))
        True
    """
    def __init__(self, group, weight) -> None:
        """
        Constructor for Manin symbols for `\\Gamma_H(N)`.

        EXAMPLES::

            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_gamma_h
            sage: G = GammaH(117, [4])
            sage: m = ManinSymbolList_gamma_h(G,2); m
            Manin Symbol List of weight 2 for Congruence Subgroup Gamma_H(117) with H generated by [4]
        """
    def group(self):
        """
        Return the group associated to ``self``.

        EXAMPLES::

            sage: ModularSymbols(GammaH(12, [5]), 2).manin_symbols().group()
            Congruence Subgroup Gamma_H(12) with H generated by [5]
        """

class ManinSymbolList_character(ManinSymbolList):
    """
    List of Manin symbols with character.

    INPUT:

    - ``character`` -- (DirichletCharacter) the Dirichlet character

    - ``weight`` -- integer; the weight

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: eps = DirichletGroup(4).gen(0)
        sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
        sage: m = ManinSymbolList_character(eps,2); m
        Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
        sage: m.manin_symbol_list()
        [(0,1), (1,0), (1,1), (1,2), (1,3), (2,1)]
        sage: m == loads(dumps(m))
        True
    """
    def __init__(self, character, weight) -> None:
        """
        Constructor for :class:`ManinSymbolList_character` objects.

        INPUT:

        - ``character`` -- (DirichletCharacter) the Dirichlet character

        - ``weight`` -- integer; the weight

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.manin_symbol_list()
            [(0,1), (1,0), (1,1), (1,2), (1,3), (2,1)]
            sage: TestSuite(m).run()
        """
    def level(self):
        """
        Return the level of this :class:`ManinSymbolList`.

        OUTPUT: integer; the level of the symbols in this list

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: ManinSymbolList_character(eps,4).level()
            4
        """
    def apply(self, j, m):
        """
        Apply the integer matrix `m=[a,b;c,d]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; the index of the symbol to act on

        - ``m`` -- list of integers `[a,b,c,d]` where `m = [a, b; c, d]` is the
          matrix to be applied

        OUTPUT:

        A list of pairs `(j, c_i)`, where each `c_i` is an
        integer, `j` is an integer (the `j`-th Manin symbol), and the
        sum `c_i*x_i` is the image of ``self`` under the right action
        of the matrix `[a,b;c,d]`. Here the right action of
        `g = [a,b;c,d]` on a Manin symbol `[P(X,Y),(u,v)]` is by
        definition `[P(aX+bY,cX+dY),(u,v)*g]`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,4)
            sage: m[6]
            [X*Y,(0,1)]
            sage: m.apply(4, [1,0,0,1])
            [(4, 1)]
            sage: m.apply(1, [-1,0,0,1])
            [(1, -1)]
        """
    def apply_S(self, j):
        """
        Apply the matrix `S=[0,1;-1,0]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        ``(k, s)`` where `k` is the index of the symbol obtained by acting
        on the `j`-th symbol with `S`, and `s` is the parity of the
        `j`-th symbol.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.apply_S(4)
            (2, -1)
            sage: [m.apply_S(i) for i in range(len(m))]
            [(1, 1), (0, -1), (4, 1), (5, -1), (2, -1), (3, 1)]
        """
    def apply_I(self, j):
        """
        Apply the matrix `I=[-1,0,0,1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        ``(k, s)`` where `k` is the index of the symbol obtained by acting
        on the `j`-th symbol with `I`, and `s` is the parity of the
        `j`-th symbol.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.apply_I(4)
            (2, -1)
            sage: [m.apply_I(i) for i in range(len(m))]
            [(0, 1), (1, -1), (4, -1), (3, -1), (2, -1), (5, 1)]
        """
    def apply_T(self, j):
        """
        Apply the matrix `T=[0,1,-1,-1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        A list of pairs `(j, c_i)`, where each `c_i` is an
        integer, `j` is an integer (the `j`-th Manin symbol), and the
        sum `c_i*x_i` is the image of ``self`` under the right action
        of the matrix `T`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.apply_T(4)
            [(1, -1)]
            sage: [m.apply_T(i) for i in range(len(m))]
            [[(4, 1)], [(0, -1)], [(3, 1)], [(5, 1)], [(1, -1)], [(2, 1)]]
        """
    def apply_TT(self, j):
        """
        Apply the matrix `TT=[-1,-1,0,1]` to the `j`-th Manin symbol.

        INPUT:

        - ``j`` -- integer; a symbol index

        OUTPUT:

        A list of pairs `(j, c_i)`, where each `c_i` is an
        integer, `j` is an integer (the `j`-th Manin symbol), and the
        sum `c_i*x_i` is the image of ``self`` under the right action
        of the matrix `T^2`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.apply_TT(4)
            [(0, 1)]
            sage: [m.apply_TT(i) for i in range(len(m))]
            [[(1, -1)], [(4, -1)], [(5, 1)], [(2, 1)], [(0, 1)], [(3, 1)]]
        """
    def character(self):
        """
        Return the character of this :class:`ManinSymbolList_character` object.

        OUTPUT: the Dirichlet character of this Manin symbol list

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,2); m
            Manin Symbol List of weight 2 for Gamma1(4) with character [-1]
            sage: m.character()
            Dirichlet character modulo 4 of conductor 4 mapping 3 |--> -1
        """
    def index(self, x):
        """
        Return the index of a standard Manin symbol equivalent to
        ``x``, together with a scaling factor.

        INPUT:

        - ``x`` -- 3-tuple of integers defining an element of this
          list of Manin symbols, which need not be normalized

        OUTPUT:

        A pair ``(i, s)`` where ``i`` is the index of the Manin symbol
        equivalent to ``x`` and ``s`` is the scalar (an element of the
        base field).  If there is no Manin symbol equivalent to ``x``
        in the list, then ``(-1, 0)`` is returned.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,4); m
            Manin Symbol List of weight 4 for Gamma1(4) with character [-1]
            sage: [m.index(s.tuple()) for s in m.manin_symbol_list()]
            [(0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            ...
            (16, 1),
            (17, 1)]
        """
    def normalize(self, x):
        """
        Return the normalization of the Manin Symbol ``x`` with
        respect to this list, together with the normalizing scalar.

        INPUT:

        - ``x`` -- 3-tuple of integers ``(i,u,v)``, defining an element of this
          list of Manin symbols, which need not be normalized

        OUTPUT:

        ``((i,u,v),s)``, where ``(i,u,v)`` is the normalized Manin symbol equivalent
        to ``x``, and ``s`` is the normalizing scalar.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(4).gen(0)
            sage: from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character
            sage: m = ManinSymbolList_character(eps,4); m
            Manin Symbol List of weight 4 for Gamma1(4) with character [-1]
            sage: [m.normalize(s.tuple()) for s in m.manin_symbol_list()]
            [((0, 0, 1), 1),
             ((0, 1, 0), 1),
             ((0, 1, 1), 1),
             ...
             ((2, 1, 3), 1),
             ((2, 2, 1), 1)]
        """
