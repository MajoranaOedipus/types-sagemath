from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.functor import Functor as Functor
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.magmas import Magmas as Magmas
from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.categories.pushout import CompositeConstructionFunctor as CompositeConstructionFunctor, ConstructionFunctor as ConstructionFunctor, IdentityConstructionFunctor as IdentityConstructionFunctor
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.grossman_larson_algebras import GrossmanLarsonAlgebra as GrossmanLarsonAlgebra, ROOT as ROOT
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.rooted_tree import LabelledRootedTree as LabelledRootedTree, LabelledRootedTrees as LabelledRootedTrees, RootedTree as RootedTree, RootedTrees as RootedTrees
from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.functions.other import factorial as factorial
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import Infinity as Infinity
from sage.sets.family import Family as Family
from sage.structure.coerce_exceptions import CoercionException as CoercionException

class FreePreLieAlgebra(CombinatorialFreeModule):
    '''
    The free pre-Lie algebra.

    Pre-Lie algebras are non-associative algebras, where the product `*`
    satisfies

    .. MATH::

        (x * y) * z - x * (y * z) = (x * z) * y - x * (z * y).

    We use here the convention where the associator

    .. MATH::

        (x, y, z) := (x * y) * z - x * (y * z)

    is symmetric in its two rightmost arguments. This is sometimes called
    a right pre-Lie algebra.

    They have appeared in numerical analysis and deformation theory.

    The free Pre-Lie algebra on a given set `E` has an explicit
    description using rooted trees, just as the free associative algebra
    can be described using words. The underlying vector space has a basis
    indexed by finite rooted trees endowed with a map from their vertices
    to `E`. In this basis, the product of two (decorated) rooted trees `S
    * T` is the sum over vertices of `S` of the rooted tree obtained by
    adding one edge from the root of `T` to the given vertex of `S`. The
    root of these trees is taken to be the root of `S`. The free pre-Lie
    algebra can also be considered as the free algebra over the PreLie operad.

    .. WARNING::

        The usual binary operator ``*`` can be used for the pre-Lie product.
        Beware that it but must be parenthesized properly, as the pre-Lie
        product is not associative. By default, a multiple product will be
        taken with left parentheses.

    EXAMPLES::

        sage: F = algebras.FreePreLie(ZZ, \'xyz\')
        sage: x,y,z = F.gens()
        sage: (x * y) * z
        B[x[y[z[]]]] + B[x[y[], z[]]]
        sage: (x * y) * z - x * (y * z) == (x * z) * y - x * (z * y)
        True

    The free pre-Lie algebra is non-associative::

        sage: x * (y * z) == (x * y) * z
        False

    The default product is with left parentheses::

        sage: x * y * z == (x * y) * z
        True
        sage: x * y * z * x == ((x * y) * z) * x
        True

    The NAP product as defined in [Liv2006]_ is also implemented on the same
    vector space::

        sage: N = F.nap_product
        sage: N(x*y,z*z)
        B[x[y[], z[z[]]]]

    When ``None`` is given as input, unlabelled trees are used instead::

        sage: F1 = algebras.FreePreLie(QQ, None)
        sage: w = F1.gen(0); w
        B[[]]
        sage: w * w * w * w
        B[[[[[]]]]] + B[[[[], []]]] + 3*B[[[], [[]]]] + B[[[], [], []]]

    However, it is equally possible to use labelled trees instead::

        sage: F1 = algebras.FreePreLie(QQ, \'q\')
        sage: w = F1.gen(0); w
        B[q[]]
        sage: w * w * w * w
        B[q[q[q[q[]]]]] + B[q[q[q[], q[]]]] + 3*B[q[q[], q[q[]]]] + B[q[q[], q[], q[]]]

    The set `E` can be infinite::

        sage: F = algebras.FreePreLie(QQ, ZZ)
        sage: w = F.gen(1); w
        B[1[]]
        sage: x = F.gen(2); x
        B[-1[]]
        sage: y = F.gen(3); y
        B[2[]]
        sage: w*x
        B[1[-1[]]]
        sage: (w*x)*y
        B[1[-1[2[]]]] + B[1[-1[], 2[]]]
        sage: w*(x*y)
        B[1[-1[2[]]]]

    Elements of a free pre-Lie algebra can be lifted to the universal
    enveloping algebra of the associated Lie algebra. The universal
    enveloping algebra is the Grossman-Larson Hopf algebra::

        sage: F = algebras.FreePreLie(QQ,\'abc\')
        sage: a,b,c = F.gens()
        sage: (a*b+b*c).lift()
        B[#[a[b[]]]] + B[#[b[c[]]]]

    .. NOTE::

        Variables names can be ``None``, a list of strings, a string
        or an integer. When ``None`` is given, unlabelled rooted
        trees are used. When a single string is given, each letter is taken
        as a variable. See
        :func:`sage.combinat.words.alphabet.build_alphabet`.

    .. WARNING::

        Beware that the underlying combinatorial free module is based
        either on ``RootedTrees`` or on ``LabelledRootedTrees``, with no
        restriction on the labellings. This means that all code calling
        the :meth:`basis` method would not give meaningful results, since
        :meth:`basis` returns many "chaff" elements that do not belong to
        the algebra.

    REFERENCES:

    - [ChLi]_

    - [Liv2006]_
    '''
    @staticmethod
    def __classcall_private__(cls, R, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: F1 = algebras.FreePreLie(QQ, 'xyz')
            sage: F2 = algebras.FreePreLie(QQ, 'x,y,z')
            sage: F3 = algebras.FreePreLie(QQ, ['x','y','z'])
            sage: F4 = algebras.FreePreLie(QQ, Alphabet('xyz'))
            sage: F1 is F2 and F1 is F3 and F1 is F4
            True
        """
    def __init__(self, R, names=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.FreePreLie(QQ, '@'); A
            Free PreLie algebra on one generator ['@'] over Rational Field
            sage: TestSuite(A).run()

            sage: A = algebras.FreePreLie(QQ, None); A
            Free PreLie algebra on one generator ['o'] over Rational Field

            sage: F = algebras.FreePreLie(QQ, 'xy')
            sage: TestSuite(F).run() # long time
        """
    def variable_names(self):
        """
        Return the names of the variables.

        EXAMPLES::

            sage: R = algebras.FreePreLie(QQ, 'xy')
            sage: R.variable_names()
            {'x', 'y'}

            sage: R = algebras.FreePreLie(QQ, None)
            sage: R.variable_names()
            {'o'}
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of the algebra.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: F = algebras.FreePreLie(ZZ, 'xyz')
            sage: F.gen(0)
            B[x[]]

            sage: F.gen(4)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 4) must be between 0 and 2
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the generators of this algebra.

        These are the rooted trees with just one vertex.

        EXAMPLES::

            sage: A = algebras.FreePreLie(ZZ, 'fgh'); A
            Free PreLie algebra on 3 generators ['f', 'g', 'h']
             over Integer Ring
            sage: list(A.algebra_generators())
            [B[f[]], B[g[]], B[h[]]]

            sage: A = algebras.FreePreLie(QQ, ['x1','x2'])
            sage: list(A.algebra_generators())
            [B[x1[]], B[x2[]]]
        """
    def change_ring(self, R):
        """
        Return the free pre-Lie algebra in the same variables over `R`.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: A = algebras.FreePreLie(ZZ, 'fgh')
            sage: A.change_ring(QQ)
            Free PreLie algebra on 3 generators ['f', 'g', 'h'] over
            Rational Field
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self`` (as an algebra).

        EXAMPLES::

            sage: A = algebras.FreePreLie(ZZ, 'fgh')
            sage: A.gens()
            (B[f[]], B[g[]], B[h[]])
        """
    def degree_on_basis(self, t):
        """
        Return the degree of a rooted tree in the free Pre-Lie algebra.

        This is the number of vertices.

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: A.degree_on_basis(RT([RT([])]))
            2
        """
    def some_elements(self):
        """
        Return some elements of the free pre-Lie algebra.

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: A.some_elements()
            [B[[]], B[[[]]], B[[[[[]]]]] + B[[[], [[]]]], B[[[[]]]] + B[[[], []]], B[[[]]]]

        With several generators::

            sage: A = algebras.FreePreLie(QQ, 'xy')
            sage: A.some_elements()
            [B[x[]],
             B[x[x[]]],
             B[x[x[x[x[]]]]] + B[x[x[], x[x[]]]],
             B[x[x[x[]]]] + B[x[x[], x[]]],
             B[x[x[y[]]]] + B[x[x[], y[]]]]
        """
    def product_on_basis(self, x, y):
        """
        Return the pre-Lie product of two trees.

        This is the sum over all graftings of the root of `y` over a vertex
        of `x`. The root of the resulting trees is the root of `x`.

        .. SEEALSO::

            :meth:`pre_Lie_product`

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = RT([RT([])])
            sage: A.product_on_basis(x, x)
            B[[[[[]]]]] + B[[[], [[]]]]
        """
    pre_Lie_product_on_basis = product_on_basis
    @lazy_attribute
    def pre_Lie_product(self):
        """
        Return the pre-Lie product.

        .. SEEALSO::

            :meth:`pre_Lie_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = A(RT([RT([])]))
            sage: A.pre_Lie_product(x, x)
            B[[[[[]]]]] + B[[[], [[]]]]
        """
    def bracket_on_basis(self, x, y):
        """
        Return the Lie bracket of two trees.

        This is the commutator `[x, y] = x * y - y * x` of the pre-Lie product.

        .. SEEALSO::

            :meth:`pre_Lie_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = RT([RT([])])
            sage: y = RT([x])
            sage: A.bracket_on_basis(x, y)
            -B[[[[], [[]]]]] + B[[[], [[[]]]]] - B[[[[]], [[]]]]
        """
    def nap_product_on_basis(self, x, y):
        """
        Return the NAP product of two trees.

        This is the grafting of the root of `y` over the root
        of `x`. The root of the resulting tree is the root of `x`.

        .. SEEALSO::

            :meth:`nap_product`

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = RT([RT([])])
            sage: A.nap_product_on_basis(x, x)
            B[[[], [[]]]]
        """
    @lazy_attribute
    def nap_product(self):
        """
        Return the NAP product.

        .. SEEALSO::

            :meth:`nap_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ, None)
            sage: RT = A.basis().keys()
            sage: x = A(RT([RT([])]))
            sage: A.nap_product(x, x)
            B[[[], [[]]]]
        """
    def corolla(self, x, y, n, N):
        """
        Return the corolla obtained with ``x`` as root and ``y`` as leaves.

        INPUT:

        - ``x``, ``y`` -- two elements
        - ``n`` -- integer; width of the corolla
        - ``N`` -- integer; truncation order (up to order ``N`` included)

        OUTPUT:

        the sum over all possible ways to graft ``n`` copies of ``y``
        on top of ``x`` (with at most ``N`` vertices in total)

        This operation can be defined by induction starting from the
        pre-Lie product.

        EXAMPLES::

            sage: A = algebras.FreePreLie(QQ)
            sage: a = A.gen(0)
            sage: b = A.corolla(a,a,1,4); b
            B[[[]]]
            sage: A.corolla(b,b,2,7)
            B[[[[[]], [[]]]]] + 2*B[[[[]], [[[]]]]] + B[[[], [[]], [[]]]]

            sage: A = algebras.FreePreLie(QQ, 'o')
            sage: a = A.gen(0)
            sage: b = A.corolla(a,a,1,4)

            sage: A = algebras.FreePreLie(QQ,'ab')
            sage: a, b = A.gens()
            sage: A.corolla(a,b,1,4)
            B[a[b[]]]
            sage: A.corolla(b,a,3,4)
            B[b[a[], a[], a[]]]

            sage: A.corolla(a+b,a+b,2,4)
            B[a[a[], a[]]] + 2*B[a[a[], b[]]] + B[a[b[], b[]]] + B[b[a[], a[]]] +
            2*B[b[a[], b[]]] + B[b[b[], b[]]]

        TESTS::

            sage: A = algebras.FreePreLie(QQ,'ab')
            sage: a, b = A.gens()
            sage: A.corolla(a,A.zero(),2,2)
            0
        """
    def group_product(self, x, y, n, N: int = 10):
        """
        Return the truncated group product of ``x`` and ``y``.

        This is a weighted sum of all corollas with up to ``n`` leaves, with
        ``x`` as root and ``y`` as leaves.

        The result is computed up to order ``N`` (included).

        When considered with infinitely many terms and infinite precision,
        this is an analogue of the Baker-Campbell-Hausdorff formula: it
        defines an associative product on the completed free pre-Lie algebra.

        INPUT:

        - ``x``, ``y`` -- two elements
        - ``n`` -- integer; the maximal width of corollas
        - ``N`` -- integer (default: 10); truncation order

        EXAMPLES:

        In the free pre-Lie algebra with one generator::

            sage: PL = algebras.FreePreLie(QQ)
            sage: a = PL.gen(0)
            sage: PL.group_product(a, a, 3, 3)
            B[[]] + B[[[]]] + 1/2*B[[[], []]]

        In the free pre-Lie algebra with several generators::

            sage: PL = algebras.FreePreLie(QQ,'@O')
            sage: a, b = PL.gens()
            sage: PL.group_product(a, b, 3, 3)
            B[@[]] + B[@[O[]]] + 1/2*B[@[O[], O[]]]
            sage: PL.group_product(a, b, 3, 10)
            B[@[]] + B[@[O[]]] + 1/2*B[@[O[], O[]]] + 1/6*B[@[O[], O[], O[]]]
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a :class:`PreLieFunctor`
        and `R` is a ring, such that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: P = algebras.FreePreLie(ZZ, 'x,y')
            sage: x,y = P.gens()
            sage: F, R = P.construction()
            sage: F
            PreLie[x,y]
            sage: R
            Integer Ring
            sage: F(ZZ) is P
            True
            sage: F(QQ)
            Free PreLie algebra on 2 generators ['x', 'y'] over Rational Field
        """
    class Element(CombinatorialFreeModule.Element):
        def lift(self):
            """
            Lift element to the Grossman-Larson algebra.

            EXAMPLES::

                sage: F = algebras.FreePreLie(QQ,'abc')
                sage: elt = F.an_element().lift(); elt
                B[#[a[a[a[a[]]]]]] + B[#[a[a[], a[a[]]]]]
                sage: parent(elt)
                Grossman-Larson Hopf algebra on 3 generators ['a', 'b', 'c']
                over Rational Field
            """
        def valuation(self):
            """
            Return the valuation of ``self``.

            EXAMPLES::

                sage: a = algebras.FreePreLie(QQ).gen(0)
                sage: a.valuation()
                1
                sage: (a*a).valuation()
                2

                sage: a, b = algebras.FreePreLie(QQ,'ab').gens()
                sage: (a+b).valuation()
                1
                sage: (a*b).valuation()
                2
                sage: (a*b+a).valuation()
                1

            TESTS::

                sage: z = algebras.FreePreLie(QQ).zero()
                sage: z.valuation()
                +Infinity
            """

class PreLieFunctor(ConstructionFunctor):
    """
    A constructor for pre-Lie algebras.

    EXAMPLES::

        sage: P = algebras.FreePreLie(ZZ, 'x,y')
        sage: x,y = P.gens()
        sage: F = P.construction()[0]; F
        PreLie[x,y]

        sage: A = GF(5)['a,b']
        sage: a, b = A.gens()
        sage: F(A)
        Free PreLie algebra on 2 generators ['x', 'y'] over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: f = A.hom([a+b,a-b],A)
        sage: F(f)
        Generic endomorphism of Free PreLie algebra on 2 generators ['x', 'y']
        over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: F(f)(a * F(A)(x))
        (a+b)*B[x[]]
    """
    rank: int
    vars: Incomplete
    def __init__(self, vars) -> None:
        """
        EXAMPLES::

            sage: F = sage.combinat.free_prelie_algebra.PreLieFunctor(['x','y'])
            sage: F
            PreLie[x,y]
            sage: F(ZZ)
            Free PreLie algebra on 2 generators ['x', 'y']  over Integer Ring
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: F = algebras.FreePreLie(ZZ, 'x,y,z').construction()[0]
            sage: G = algebras.FreePreLie(QQ, 'x,y,z').construction()[0]
            sage: F == G
            True
            sage: G == loads(dumps(G))
            True
            sage: G = algebras.FreePreLie(QQ, 'x,y').construction()[0]
            sage: F == G
            False
        """
    def __mul__(self, other):
        """
        If two PreLie functors are given in a row, form a single PreLie functor
        with all of the variables.

        EXAMPLES::

            sage: F = sage.combinat.free_prelie_algebra.PreLieFunctor(['x','y'])
            sage: G = sage.combinat.free_prelie_algebra.PreLieFunctor(['t'])
            sage: G * F
            PreLie[x,y,t]
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return None.

        EXAMPLES::

            sage: F = sage.combinat.free_prelie_algebra.PreLieFunctor(['x','y'])
            sage: G = sage.combinat.free_prelie_algebra.PreLieFunctor(['t'])
            sage: F.merge(G)
            PreLie[x,y,t]
            sage: F.merge(F)
            PreLie[x,y]

        Now some actual use cases::

            sage: R = algebras.FreePreLie(ZZ, 'xyz')
            sage: x,y,z = R.gens()
            sage: 1/2 * x
            1/2*B[x[]]
            sage: parent(1/2 * x)
            Free PreLie algebra on 3 generators ['x', 'y', 'z'] over Rational Field

            sage: S = algebras.FreePreLie(QQ, 'zt')
            sage: z,t = S.gens()
            sage: x + t
            B[t[]] + B[x[]]
            sage: parent(x + t)
            Free PreLie algebra on 4 generators ['z', 't', 'x', 'y'] over Rational Field
        """

def tree_from_sortkey(ch, labels: bool = True):
    """
    Transform a list of ``(valence, label)`` into a tree and a remainder.

    This is like an inverse of the ``sort_key`` method.

    INPUT:

    - ``ch`` -- list of pairs ``(integer, label)``
    - ``labels`` -- boolean (default: ``True``); whether to use labelled trees

    OUTPUT:

    a pair ``(tree, remainder of the input)``

    EXAMPLES::

        sage: from sage.combinat.free_prelie_algebra import tree_from_sortkey
        sage: a = algebras.FreePreLie(QQ).gen(0)
        sage: t = (a*a*a*a).support()
        sage: all(tree_from_sortkey(u.sort_key(), False)[0] == u for u in t)
        True

        sage: a, b = algebras.FreePreLie(QQ,'ab').gens()
        sage: t = (a*b*a*b).support()
        sage: all(tree_from_sortkey(u.sort_key())[0] == u for u in t)
        True
    """
def corolla_gen(tx, list_ty, labels: bool = True) -> Generator[Incomplete]:
    """
    Yield the terms in the corolla with given bottom tree and top trees.

    These are the possible terms in the simultaneous grafting of the
    top trees on vertices of the bottom tree.

    INPUT:

    - ``tx`` -- a tree
    - ``list_ty`` -- list of trees

    EXAMPLES::

        sage: from sage.combinat.free_prelie_algebra import corolla_gen
        sage: a = algebras.FreePreLie(QQ).gen(0)
        sage: ta = a.support()[0]
        sage: list(corolla_gen(ta,[ta],False))
        [[[]]]

        sage: a, b = algebras.FreePreLie(QQ,'ab').gens()
        sage: ta = a.support()[0]
        sage: tb = b.support()[0]
        sage: ab = (a*b).support()[0]
        sage: list(corolla_gen(ta,[tb]))
        [a[b[]]]
        sage: list(corolla_gen(tb,[ta,ta]))
        [b[a[], a[]]]
        sage: list(corolla_gen(ab,[ab,ta]))
        [a[a[], b[], a[b[]]], a[a[b[]], b[a[]]], a[a[], b[a[b[]]]],
        a[b[a[], a[b[]]]]]
    """
