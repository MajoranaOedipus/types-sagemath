from _typeshed import Incomplete
from sage.misc.search import search as search
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

def P1NFList_clear_level_cache() -> None:
    """
    Clear the global cache of data for the level ideals.

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^3 + 11)
        sage: N = k.ideal(a+1)
        sage: alpha = MSymbol(N, 2*a^2, 5)
        sage: alpha.normalize()
        M-symbol (-4*a^2: 5*a^2) of level Fractional ideal (a + 1)
        sage: sage.modular.modsym.p1list_nf._level_cache
        {Fractional ideal (a + 1): (...)}
        sage: sage.modular.modsym.p1list_nf.P1NFList_clear_level_cache()
        sage: sage.modular.modsym.p1list_nf._level_cache
        {}
    """

class MSymbol(SageObject):
    """
    The constructor for an M-symbol over a number field.

    INPUT:

    - ``N`` -- integral ideal (the modulus or level)

    - ``c`` -- integral element of the underlying number field or an MSymbol of
      level N

    - ``d`` -- (optional) when present, it must be an integral element such
      that `\\langle c\\rangle + \\langle d\\rangle + N = R`, where `R` is the
      corresponding ring of integers

    - ``check`` -- boolean (default: ``True``); if ``check=False`` the
      constructor does not check the condition
      `\\langle c\\rangle + \\langle d\\rangle + N = R`

    OUTPUT:

    An M-symbol modulo the given ideal `N`, i.e. an element of the
    projective line `\\mathbb{P}^1(R/N)`, where `R` is the ring of integers of
    the underlying number field.

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^3 + 11)
        sage: N = k.ideal(a + 1, 2)
        sage: MSymbol(N, 3, a^2 + 1)
        M-symbol (3: a^2 + 1) of level Fractional ideal (2, a + 1)

    We can give a tuple as input:

    ::

        sage: MSymbol(N, (1, 0))
        M-symbol (1: 0) of level Fractional ideal (2, a + 1)

    We get an error if `\\langle c\\rangle`, `\\langle d\\rangle` and `N` are not coprime:

    ::

        sage: MSymbol(N, 2*a, a - 1)
        Traceback (most recent call last):
        ...
        ValueError: (2*a, a - 1) is not an element of P1(R/N).
        sage: MSymbol(N, (0, 0))
        Traceback (most recent call last):
        ...
        ValueError: (0, 0) is not an element of P1(R/N).

    Saving and loading works:

    ::

        sage: alpha = MSymbol(N, 3, a^2 + 1)
        sage: loads(dumps(alpha))==alpha
        True
    """
    def __init__(self, N, c, d=None, check: bool = True) -> None:
        """
        See ``MSymbol`` for full documentation.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^4 + 13*x - 7)
            sage: N = k.ideal(5)
            sage: MSymbol(N, 0, 6*a)
            M-symbol (0: 6*a) of level Fractional ideal (5)
            sage: MSymbol(N, a^2 + 3, 7)
            M-symbol (a^2 + 3: 7) of level Fractional ideal (5)
        """
    def __richcmp__(self, other, op):
        """
        Comparison function for objects of the class MSymbol.

        The order is the same as for the underlying lists of lists.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha = MSymbol(N, 3, a)
            sage: beta = MSymbol(N, 1, 0)
            sage: alpha < beta
            False
            sage: beta = MSymbol(N, 3, a + 1)
            sage: alpha < beta
            True
        """
    def N(self):
        """
        Return the level or modulus of this MSymbol.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha = MSymbol(N, 3, a)
            sage: alpha.N()
            Fractional ideal (3, 1/2*a - 1/2)
        """
    def tuple(self):
        """
        Return the :class:`MSymbol` as a list `(c, d)`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha = MSymbol(N, 3, a); alpha
            M-symbol (3: a) of level Fractional ideal (3, 1/2*a - 1/2)
            sage: alpha.tuple()
            (3, a)
        """
    def __getitem__(self, n):
        """
        Indexing function for the list defined by an M-symbol.

        INPUT:

        - ``n`` -- integer (0 or 1, since the list defined by an M-symbol has
          length 2)

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha = MSymbol(N, 3, a); alpha
            M-symbol (3: a) of level Fractional ideal (3, 1/2*a - 1/2)
            sage: alpha[0]
            3
            sage: alpha[1]
            a
        """
    c: Incomplete
    d: Incomplete
    def lift_to_sl2_Ok(self):
        """
        Lift the :class:`MSymbol` to an element of `SL(2, O_k)`, where `O_k` is the ring
        of integers of the corresponding number field.

        OUTPUT:

        A list of integral elements `[a, b, c', d']` that are the entries of
        a `2\\times 2` matrix with determinant 1. The lower two entries are congruent
        (modulo the level) to the coefficients `c`, `d` of the :class:`MSymbol` ``self``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha = MSymbol(N, 3*a + 1, a)
            sage: alpha.lift_to_sl2_Ok()
            [0, -1, 1, a]
        """
    def normalize(self, with_scalar: bool = False):
        """
        Return a normalized :class:`MSymbol` (a canonical representative of an element
        of `\\mathbb{P}^1(R/N)`) equivalent to ``self``.

        INPUT:

        - ``with_scalar`` -- boolean (default: ``False``)

        OUTPUT:

        - (only if ``with_scalar=True``) a transforming scalar `u`, such that
          `(u*c', u*d')` is congruent to `(c: d)` (mod `N`), where `(c: d)`
          are the coefficients of ``self`` and `N` is the level.

        -  a normalized :class:`MSymbol` `(c': d')` equivalent to ``self``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3, a - 1)
            sage: alpha1 = MSymbol(N, 3, a); alpha1
            M-symbol (3: a) of level Fractional ideal (3, 1/2*a - 1/2)
            sage: alpha1.normalize()
            M-symbol (0: 1) of level Fractional ideal (3, 1/2*a - 1/2)
            sage: alpha2 = MSymbol(N, 4, a + 1)
            sage: alpha2.normalize()
            M-symbol (1: -a) of level Fractional ideal (3, 1/2*a - 1/2)

        We get the scaling factor by setting ``with_scalar=True``:

        ::

            sage: alpha1.normalize(with_scalar=True)
            (a, M-symbol (0: 1) of level Fractional ideal (3, 1/2*a - 1/2))
            sage: r, beta1 = alpha1.normalize(with_scalar=True)
            sage: r*beta1.c - alpha1.c in N
            True
            sage: r*beta1.d - alpha1.d in N
            True
            sage: r, beta2 = alpha2.normalize(with_scalar=True)
            sage: r*beta2.c - alpha2.c in N
            True
            sage: r*beta2.d - alpha2.d in N
            True
        """

class P1NFList(SageObject):
    """
    The class for `\\mathbb{P}^1(R/N)`, the projective line modulo `N`, where
    `R` is the ring of integers of a number field `K` and `N` is an integral ideal.

    INPUT:

    - ``N`` -- integral ideal (the modulus or level)

    OUTPUT:

    A :class:`P1NFList` object representing `\\mathbb{P}^1(R/N)`.

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^3 + 11)
        sage: N = k.ideal(5, a + 1)
        sage: P = P1NFList(N); P
        The projective line over the ring of integers modulo the Fractional ideal (5, a + 1)

    Saving and loading works.

    ::

        sage: loads(dumps(P)) == P
        True
    """
    def __init__(self, N) -> None:
        """
        The constructor for the class P1NFList. See ``P1NFList`` for full
        documentation.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 5)
            sage: N = k.ideal(3, a - 1)
            sage: P = P1NFList(N); P
            The projective line over the ring of integers modulo the Fractional ideal (3, a + 2)
        """
    def __richcmp__(self, other, op):
        """
        Comparison function for objects of the class P1NFList.

        The order is the same as for the underlying modulus.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N1 = k.ideal(3, a + 1)
            sage: P1 = P1NFList(N1)
            sage: N2 = k.ideal(a + 2)
            sage: P2 = P1NFList(N2)
            sage: P1 < P2
            True
            sage: P1 > P2
            False
            sage: P1 == P1NFList(N1)
            True
        """
    def __getitem__(self, n):
        """
        Standard indexing function for the class P1NFList.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(a)
            sage: P = P1NFList(N)
            sage: list(P) == P._P1NFList__list
            True
            sage: j = randint(0,len(P)-1)
            sage: P[j] == P._P1NFList__list[j]
            True
        """
    def __len__(self) -> int:
        """
        Return the length of this P1NFList.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a^2 - a + 1)
            sage: P = P1NFList(N)
            sage: len(P)
            26
        """
    def list(self):
        """
        Return the underlying list of this :class:`P1NFList` object.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a+1)
            sage: P = P1NFList(N)
            sage: type(P)
            <class 'sage.modular.modsym.p1list_nf.P1NFList'>
            sage: type(P.list())
            <... 'list'>
        """
    def normalize(self, c, d=None, with_scalar: bool = False):
        """
        Return a normalised element of `\\mathbb{P}^1(R/N)`.

        INPUT:

        - ``c`` -- integral element of the underlying number field, or an
          MSymbol

        - ``d`` -- (optional) when present, it must be an integral element of
          the number field such that `(c, d)` defines an M-symbol of level `N`

        - ``with_scalar`` -- boolean (default: ``False``)

        OUTPUT:

        - (only if ``with_scalar=True``) a transforming scalar `u`, such that
          `(u*c', u*d')` is congruent to `(c: d)` (mod `N`).

        - a normalized :class:`MSymbol` `(c': d')` equivalent to `(c: d)`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 31)
            sage: N = k.ideal(5, a + 3)
            sage: P = P1NFList(N)
            sage: P.normalize(3, a)
            M-symbol (1: 2*a) of level Fractional ideal (5, 1/2*a + 3/2)

        We can use an :class:`MSymbol` as input:

        ::

            sage: alpha = MSymbol(N, 3, a)
            sage: P.normalize(alpha)
            M-symbol (1: 2*a) of level Fractional ideal (5, 1/2*a + 3/2)

        If we are interested in the normalizing scalar:

        ::

            sage: P.normalize(alpha, with_scalar=True)
            (-a, M-symbol (1: 2*a) of level Fractional ideal (5, 1/2*a + 3/2))
            sage: r, beta = P.normalize(alpha, with_scalar=True)
            sage: (r*beta.c - alpha.c in N) and (r*beta.d - alpha.d in N)
            True
        """
    def N(self):
        """
        Return the level or modulus of this :class:`P1NFList`.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 31)
            sage: N = k.ideal(5, a + 3)
            sage: P = P1NFList(N)
            sage: P.N()
            Fractional ideal (5, 1/2*a + 3/2)
        """
    def index(self, c, d=None, with_scalar: bool = False):
        """
        Return the index of the class of the pair `(c, d)` in the fixed list
        of representatives of `\\mathbb{P}^1(R/N)`.

        INPUT:

        - ``c`` -- integral element of the corresponding number field, or an
          :class:`MSymbol`

        - ``d`` -- (optional) when present, it must be an integral element of
          the number field such that `(c, d)` defines an M-symbol of level `N`

        - ``with_scalar`` -- boolean (default: ``False``)

        OUTPUT:

        - ``u`` -- the normalizing scalar (only if ``with_scalar=True``)

        - ``i`` -- the index of `(c, d)` in the list

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 31)
            sage: N = k.ideal(5, a + 3)
            sage: P = P1NFList(N)
            sage: P.index(3,a)
            5
            sage: P[5]==MSymbol(N, 3, a).normalize()
            True

        We can give an :class:`MSymbol` as input:

        ::

            sage: alpha = MSymbol(N, 3, a)
            sage: P.index(alpha)
            5

        We cannot look for the class of an :class:`MSymbol` of a different level:

        ::

            sage: M = k.ideal(a + 1)
            sage: beta = MSymbol(M, 0, 1)
            sage: P.index(beta)
            Traceback (most recent call last):
            ...
            ValueError: The MSymbol is of a different level

        If we are interested in the transforming scalar:

        ::

            sage: alpha = MSymbol(N, 3, a)
            sage: P.index(alpha, with_scalar=True)
            (-a, 5)
            sage: u, i = P.index(alpha, with_scalar=True)
            sage: (u*P[i].c - alpha.c in N) and (u*P[i].d - alpha.d in N)
            True
        """
    def index_of_normalized_pair(self, c, d=None):
        """
        Return the index of the class `(c, d)` in the fixed list of
        representatives of `\\mathbb(P)^1(R/N)`.

        INPUT:

        - ``c`` -- integral element of the corresponding number field, or a
          normalized :class:`MSymbol`

        - ``d`` -- (optional) when present, it must be an integral element of
          the number field such that `(c, d)` defines a normalized M-symbol of
          level `N`

        OUTPUT: ``i`` -- the index of `(c, d)` in the list

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 31)
            sage: N = k.ideal(5, a + 3)
            sage: P = P1NFList(N)
            sage: P.index_of_normalized_pair(1, 0)
            3
            sage: j = randint(0,len(P)-1)
            sage: P.index_of_normalized_pair(P[j])==j
            True
        """
    def lift_to_sl2_Ok(self, i):
        """
        Lift the `i`-th element of this :class:`P1NFList` to an element of `SL(2, R)`,
        where `R` is the ring of integers of the corresponding number field.

        INPUT:

        - ``i`` -- integer (index of the element to lift)

        OUTPUT:

        If the `i`-th element is `(c : d)`, the function returns a list of
        integral elements `[a, b, c', d']` that defines a `2\\times 2` matrix with
        determinant 1 and such that `c=c'` (mod `N`) and `d=d'` (mod `N`).

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3)
            sage: P = P1NFList(N)
            sage: len(P)
            16
            sage: P[5]
            M-symbol (1/2*a + 1/2: -a) of level Fractional ideal (3)
            sage: P.lift_to_sl2_Ok(5)
            [-a, 2*a - 2, 1/2*a + 1/2, -a]

        ::

            sage: Ok = k.ring_of_integers()
            sage: L = [Matrix(Ok, 2, P.lift_to_sl2_Ok(i)) for i in range(len(P))]
            sage: all(det(L[i]) == 1 for i in range(len(L)))
            True
        """
    def apply_S(self, i):
        """
        Applies the matrix `S` = [0, -1, 1, 0] to the `i`-th M-Symbol of the list.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        integer -- the index of the M-Symbol obtained by the right action of
        the matrix `S` = [0, -1, 1, 0] on the `i`-th M-Symbol.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a + 1)
            sage: P = P1NFList(N)
            sage: j = P.apply_S(P.index_of_normalized_pair(1, 0))
            sage: P[j]
            M-symbol (0: 1) of level Fractional ideal (5, a + 1)

        We test that S has order 2:

        ::

            sage: j = randint(0,len(P)-1)
            sage: P.apply_S(P.apply_S(j))==j
            True
        """
    def apply_TS(self, i):
        """
        Applies the matrix `TS` = [1, -1, 0, 1] to the `i`-th M-Symbol of the list.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        integer -- the index of the M-Symbol obtained by the right action of
        the matrix `TS` = [1, -1, 0, 1] on the `i`-th M-Symbol.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a + 1)
            sage: P = P1NFList(N)
            sage: P.apply_TS(3)
            2

        We test that `TS` has order 3:

        ::

            sage: j = randint(0,len(P)-1)
            sage: P.apply_TS(P.apply_TS(P.apply_TS(j)))==j
            True
        """
    def apply_T_alpha(self, i, alpha: int = 1):
        """
        Applies the matrix `T_{alpha}` = [1, `alpha`, 0, 1] to the `i`-th
        M-Symbol of the list.

        INPUT:

        - ``i`` -- integer

        - ``alpha`` -- (default: 1) element of the corresponding ring of integers

        OUTPUT:

        integer -- the index of the M-Symbol obtained by the right action of
        the matrix `T_{alpha}` = [1, `alpha`, 0, 1] on the `i`-th M-Symbol.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a + 1)
            sage: P = P1NFList(N)
            sage: P.apply_T_alpha(4, a^ 2 - 2)
            3

        We test that `T_a*T_b = T_{(a+b)}`:

        ::

            sage: P.apply_T_alpha(3, a^2 - 2)==P.apply_T_alpha(P.apply_T_alpha(3,a^2),-2)
            True
        """
    def apply_J_epsilon(self, i, e1, e2: int = 1):
        """
        Apply the matrix `J_{\\epsilon}` = [e1, 0, 0, e2] to the `i`-th
        M-Symbol of the list.

        e1, e2 are units of the underlying number field.

        INPUT:

        - ``i`` -- integer

        - ``e1`` -- unit

        - ``e2`` -- unit (default: 1)

        OUTPUT:

        integer -- the index of the M-Symbol obtained by the right action of
        the matrix `J_{\\epsilon}` = [e1, 0, 0, e2] on the `i`-th M-Symbol.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: k.<a> = NumberField(x^3 + 11)
            sage: N = k.ideal(5, a + 1)
            sage: P = P1NFList(N)
            sage: u = k.unit_group().gens_values(); u
            [-1, 2*a^2 + 4*a - 1]
            sage: P.apply_J_epsilon(4, -1)
            2
            sage: P.apply_J_epsilon(4, u[0], u[1])
            1

        ::

            sage: k.<a> = NumberField(x^4 + 13*x - 7)
            sage: N = k.ideal(a + 1)
            sage: P = P1NFList(N)
            sage: u = k.unit_group().gens_values(); u
            [-1, -a^3 - a^2 - a - 12, -a^3 - 3*a^2 + 1]
            sage: P.apply_J_epsilon(3, u[2]^2)==P.apply_J_epsilon(P.apply_J_epsilon(3, u[2]),u[2])
            True
        """

def p1NFlist(N):
    """
    Return a list of the normalized elements of `\\mathbb{P}^1(R/N)`, where
    `N` is an integral ideal.

    INPUT:

    - ``N`` -- integral ideal (the level or modulus)

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^2 + 23)
        sage: N = k.ideal(3)
        sage: from sage.modular.modsym.p1list_nf import p1NFlist, psi
        sage: len(p1NFlist(N))==psi(N)
        True
    """
def lift_to_sl2_Ok(N, c, d):
    """
    Lift a pair (c, d) to an element of `SL(2, O_k)`, where `O_k` is the ring
    of integers of the corresponding number field.

    INPUT:

    - ``N`` -- number field ideal

    - ``c`` -- integral element of the number field

    - ``d`` -- integral element of the number field

    OUTPUT:

    A list `[a, b, c', d']` of integral elements that are the entries of
    a `2\\times 2` matrix with determinant 1. The lower two entries are congruent to
    `c`, `d` modulo the ideal `N`.

    EXAMPLES::

        sage: from sage.modular.modsym.p1list_nf import lift_to_sl2_Ok
        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^2 + 23)
        sage: Ok = k.ring_of_integers()
        sage: N = k.ideal(3)
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 1, a))
        sage: det(M)
        1
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 0, a))
        sage: det(M)
        1
        sage: (M[1][0] in N) and (M[1][1] - a in N)
        True
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError: Cannot lift (0, 0) to an element of Sl2(Ok).

    ::

        sage: k.<a> = NumberField(x^3 + 11)
        sage: Ok = k.ring_of_integers()
        sage: N = k.ideal(3, a - 1)
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 2*a, 0))
        sage: det(M)
        1
        sage: (M[1][0] - 2*a in N) and (M[1][1] in N)
        True
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 4*a^2, a + 1))
        sage: det(M)
        1
        sage: (M[1][0] - 4*a^2 in N) and (M[1][1] - (a+1) in N)
        True

    ::

        sage: k.<a> = NumberField(x^4 - x^3 -21*x^2 + 17*x + 133)
        sage: Ok = k.ring_of_integers()
        sage: N = k.ideal(7, a)
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 0, a^2 - 1))
        sage: det(M)
        1
        sage: (M[1][0] in N) and (M[1][1] - (a^2-1) in N)
        True
        sage: M = Matrix(Ok, 2, lift_to_sl2_Ok(N, 0, 7))
        Traceback (most recent call last):
        ...
        ValueError: <0> + <7> and the Fractional ideal (7, -4/7*a^3 + 13/7*a^2 + 39/7*a - 19) are not coprime.
    """
def make_coprime(N, c, d):
    """
    Return (c, d') so d' is congruent to d modulo N, and such that c and d' are
    coprime (`\\langle c\\rangle + \\langle d'\\rangle = R`).

    INPUT:

    - ``N`` -- number field ideal

    - ``c`` -- integral element of the number field

    - ``d`` -- integral element of the number field

    OUTPUT:

    A pair `(c, d')` where `c`, `d'` are integral elements of the corresponding
    number field, with `d'` congruent to `d` mod `N`, and such that `\\langle c\\rangle + \\langle d'\\rangle = R`
    (`R` being the corresponding ring of integers).

    EXAMPLES::

        sage: from sage.modular.modsym.p1list_nf import make_coprime
        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^2 + 23)
        sage: N = k.ideal(3, a - 1)
        sage: c = 2*a; d = a + 1
        sage: N.is_coprime(k.ideal(c, d))
        True
        sage: k.ideal(c).is_coprime(d)
        False
        sage: c, dp = make_coprime(N, c, d)
        sage: k.ideal(c).is_coprime(dp)
        True
    """
def psi(N):
    """
    The index `[\\Gamma : \\Gamma_0(N)]`, where `\\Gamma = GL(2, R)` for `R` the
    corresponding ring of integers, and `\\Gamma_0(N)` standard congruence
    subgroup.

    EXAMPLES::

        sage: from sage.modular.modsym.p1list_nf import psi
        sage: x = polygen(QQ, 'x')
        sage: k.<a> = NumberField(x^2 + 23)
        sage: N = k.ideal(3, a - 1)
        sage: psi(N)
        4

    ::

        sage: k.<a> = NumberField(x^2 + 23)
        sage: N = k.ideal(5)
        sage: psi(N)
        26
    """
