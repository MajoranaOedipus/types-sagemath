from _typeshed import Incomplete
from sage.categories.functor import Functor as Functor
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.pushout import CompositeConstructionFunctor as CompositeConstructionFunctor, ConstructionFunctor as ConstructionFunctor, IdentityConstructionFunctor as IdentityConstructionFunctor
from sage.categories.rings import Rings as Rings
from sage.combinat.binary_tree import BinaryTree as BinaryTree, BinaryTrees as BinaryTrees, LabelledBinaryTree as LabelledBinaryTree, LabelledBinaryTrees as LabelledBinaryTrees
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import Infinity as Infinity
from sage.sets.family import Family as Family
from sage.structure.coerce_exceptions import CoercionException as CoercionException

class FreeDendriformAlgebra(CombinatorialFreeModule):
    """
    The free dendriform algebra.

    Dendriform algebras are associative algebras, where the associative
    product `*` is decomposed as a sum of two binary operations

    .. MATH::

        x * y = x \\succ y + x \\prec y

    that satisfy the axioms:

    .. MATH::

        (x \\succ y) \\prec z = x \\succ (y \\prec z),

    .. MATH::

        (x \\prec y) \\prec z = x \\prec (y * z).

    .. MATH::

        (x * y) \\succ z = x \\succ (y \\succ z).

    The free Dendriform algebra on a given set `E` has an explicit
    description using (planar) binary trees, just as the free
    associative algebra can be described using words. The underlying
    vector space has a basis indexed by finite binary trees endowed
    with a map from their vertices to `E`. In this basis, the
    associative product of two (decorated) binary trees `S * T` is the
    sum over all possible ways of identifying (glueing) the rightmost path in
    `S` and the leftmost path in `T`.

    The decomposition of the associative product as the sum of two
    binary operations `\\succ` and
    `\\prec` is made by separating the terms according to the origin of
    the root vertex. For `x \\succ y`, one keeps the terms where the root
    vertex comes from `y`, whereas for `x \\prec y` one keeps the terms
    where the root vertex comes from `x`.

    The free dendriform algebra can also be considered as the free
    algebra over the Dendriform operad.

    .. NOTE::

        The usual binary operator `*` is used for the
        associative product.

    EXAMPLES::

        sage: F = algebras.FreeDendriform(ZZ, 'xyz')
        sage: x,y,z = F.gens()
        sage: (x * y) * z
        B[x[., y[., z[., .]]]] + B[x[., z[y[., .], .]]] + B[y[x[., .], z[., .]]]
         + B[z[x[., y[., .]], .]] + B[z[y[x[., .], .], .]]

    The free dendriform algebra is associative::

        sage: x * (y * z) == (x * y) * z
        True

    The associative product decomposes in two parts::

        sage: x * y == F.prec(x, y) + F.succ(x, y)
        True

    The axioms hold::

        sage: F.prec(F.succ(x, y), z) == F.succ(x, F.prec(y, z))
        True
        sage: F.prec(F.prec(x, y), z) == F.prec(x, y * z)
        True
        sage: F.succ(x * y, z) == F.succ(x, F.succ(y, z))
        True

    When there is only one generator, unlabelled trees are used instead::

        sage: F1 = algebras.FreeDendriform(QQ)
        sage: w = F1.gen(0); w
        B[[., .]]
        sage: w * w * w
        B[[., [., [., .]]]] + B[[., [[., .], .]]] + B[[[., .], [., .]]]
         + B[[[., [., .]], .]] + B[[[[., .], .], .]]

    The set `E` can be infinite::

        sage: F = algebras.FreeDendriform(QQ, ZZ)
        sage: w = F.gen(1); w
        B[1[., .]]
        sage: x = F.gen(2); x
        B[-1[., .]]
        sage: w*x
        B[-1[1[., .], .]] + B[1[., -1[., .]]]

    REFERENCES:

    - [LR1998]_
    """
    @staticmethod
    def __classcall_private__(cls, R, names=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: F1 = algebras.FreeDendriform(QQ, 'xyz')
            sage: F2 = algebras.FreeDendriform(QQ, ['x','y','z'])
            sage: F3 = algebras.FreeDendriform(QQ, Alphabet('xyz'))
            sage: F1 is F2 and F1 is F3
            True
        """
    def __init__(self, R, names=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.FreeDendriform(QQ, '@'); A
            Free Dendriform algebra on one generator ['@'] over Rational Field
            sage: TestSuite(A).run()  # long time (3s)

            sage: F = algebras.FreeDendriform(QQ, 'xy')
            sage: TestSuite(F).run() # long time (3s)
        """
    def variable_names(self):
        """
        Return the names of the variables.

        EXAMPLES::

            sage: R = algebras.FreeDendriform(QQ, 'xy')
            sage: R.variable_names()
            {'x', 'y'}
        """
    def gen(self, i):
        """
        Return the `i`-th generator of the algebra.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: F = algebras.FreeDendriform(ZZ, 'xyz')
            sage: F.gen(0)
            B[x[., .]]

            sage: F.gen(4)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 4) must be between 0 and 2
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the generators of this algebra.

        These are the binary trees with just one vertex.

        EXAMPLES::

            sage: A = algebras.FreeDendriform(ZZ, 'fgh'); A
            Free Dendriform algebra on 3 generators ['f', 'g', 'h']
             over Integer Ring
            sage: list(A.algebra_generators())
            [B[f[., .]], B[g[., .]], B[h[., .]]]

            sage: A = algebras.FreeDendriform(QQ, ['x1','x2'])
            sage: list(A.algebra_generators())
            [B[x1[., .]], B[x2[., .]]]
        """
    def change_ring(self, R):
        """
        Return the free dendriform algebra in the same variables over `R`.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: A = algebras.FreeDendriform(ZZ, 'fgh')
            sage: A.change_ring(QQ)
            Free Dendriform algebra on 3 generators ['f', 'g', 'h'] over
            Rational Field
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self`` (as an algebra).

        EXAMPLES::

            sage: A = algebras.FreeDendriform(ZZ, 'fgh')
            sage: A.gens()
            (B[f[., .]], B[g[., .]], B[h[., .]])
        """
    def degree_on_basis(self, t):
        """
        Return the degree of a binary tree in the free Dendriform algebra.

        This is the number of vertices.

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ,'@')
            sage: RT = A.basis().keys()
            sage: u = RT([], '@')
            sage: A.degree_on_basis(u.over(u))
            2
        """
    def some_elements(self):
        """
        Return some elements of the free dendriform algebra.

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: A.some_elements()
            [B[.],
             B[[., .]],
             B[[., [., .]]] + B[[[., .], .]],
             B[.] + B[[., [., .]]] + B[[[., .], .]]]

        With several generators::

            sage: A = algebras.FreeDendriform(QQ, 'xy')
            sage: A.some_elements()
            [B[.],
             B[x[., .]],
             B[x[., x[., .]]] + B[x[x[., .], .]],
             B[.] + B[x[., x[., .]]] + B[x[x[., .], .]]]
        """
    def one_basis(self):
        """
        Return the index of the unit.

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ, '@')
            sage: A.one_basis()
            .
            sage: A = algebras.FreeDendriform(QQ, 'xy')
            sage: A.one_basis()
            .
        """
    def product_on_basis(self, x, y):
        """
        Return the `*` associative dendriform product of two trees.

        This is the sum over all possible ways of identifying the
        rightmost path in `x` and the leftmost path in `y`. Every term
        corresponds to a shuffle of the vertices on the rightmost path
        in `x` and the vertices on the leftmost path in `y`.

        .. SEEALSO::

            - :meth:`succ_product_on_basis`, :meth:`prec_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = RT([])
            sage: A.product_on_basis(x, x)
            B[[., [., .]]] + B[[[., .], .]]
        """
    def succ_product_on_basis(self, x, y):
        """
        Return the `\\succ` dendriform product of two trees.

        This is the sum over all possible ways to identify the rightmost path
        in `x` and the leftmost path in `y`, with the additional condition
        that the root vertex of the result comes from `y`.

        The usual symbol for this operation is `\\succ`.

        .. SEEALSO::

            - :meth:`product_on_basis`, :meth:`prec_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = RT([])
            sage: A.succ_product_on_basis(x, x)
            B[[[., .], .]]

        TESTS::

            sage: u = A.one().support()[0]
            sage: A.succ_product_on_basis(u, u)
            Traceback (most recent call last):
            ...
            ValueError: dendriform products | < | and | > | are not defined
        """
    @lazy_attribute
    def succ(self):
        """
        Return the `\\succ` dendriform product.

        This is the sum over all possible ways of identifying the
        rightmost path in `x` and the leftmost path in `y`, with the
        additional condition that the root vertex of the result comes
        from `y`.

        The usual symbol for this operation is `\\succ`.

        .. SEEALSO::

            :meth:`product`, :meth:`prec`, :meth:`over`, :meth:`under`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = A.gen(0)
            sage: A.succ(x, x)
            B[[[., .], .]]
        """
    def prec_product_on_basis(self, x, y):
        """
        Return the `\\prec` dendriform product of two trees.

        This is the sum over all possible ways of identifying the
        rightmost path in `x` and the leftmost path in `y`, with the
        additional condition that the root vertex of the result comes
        from `x`.

        The usual symbol for this operation is `\\prec`.

        .. SEEALSO::

            - :meth:`product_on_basis`, :meth:`succ_product_on_basis`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = RT([])
            sage: A.prec_product_on_basis(x, x)
            B[[., [., .]]]

        TESTS::

            sage: u = A.one().support()[0]
            sage: A.prec_product_on_basis(u, u)
            Traceback (most recent call last):
            ...
            ValueError: dendriform products | < | and | > | are not defined
        """
    @lazy_attribute
    def prec(self):
        """
        Return the `\\prec` dendriform product.

        This is the sum over all possible ways to identify the rightmost path
        in `x` and the leftmost path in `y`, with the additional condition
        that the root vertex of the result comes from `x`.

        The usual symbol for this operation is `\\prec`.

        .. SEEALSO::

            :meth:`product`, :meth:`succ`, :meth:`over`, :meth:`under`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = A.gen(0)
            sage: A.prec(x, x)
            B[[., [., .]]]
        """
    @lazy_attribute
    def over(self):
        """
        Return the over product.

        The over product `x/y` is the binary tree obtained by
        grafting the root of `y` at the rightmost leaf of `x`.

        The usual symbol for this operation is `/`.

        .. SEEALSO::

            :meth:`product`, :meth:`succ`, :meth:`prec`, :meth:`under`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = A.gen(0)
            sage: A.over(x, x)
            B[[., [., .]]]
        """
    @lazy_attribute
    def under(self):
        """
        Return the under product.

        The over product `x \\backslash y` is the binary tree obtained by
        grafting the root of `x` at the leftmost leaf of `y`.

        The usual symbol for this operation is `\\backslash`.

        .. SEEALSO::

            :meth:`product`, :meth:`succ`, :meth:`prec`, :meth:`over`

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: RT = A.basis().keys()
            sage: x = A.gen(0)
            sage: A.under(x, x)
            B[[[., .], .]]
        """
    def coproduct_on_basis(self, x):
        """
        Return the coproduct of a binary tree.

        EXAMPLES::

            sage: A = algebras.FreeDendriform(QQ)
            sage: x = A.gen(0)
            sage: ascii_art(A.coproduct(A.one()))  # indirect doctest
            1 # 1

            sage: ascii_art(A.coproduct(x))  # indirect doctest
            1 # B  + B  # 1
                 o    o

            sage: A = algebras.FreeDendriform(QQ, 'xyz')
            sage: x, y, z = A.gens()
            sage: w = A.under(z,A.over(x,y))
            sage: A.coproduct(z)
            B[.] # B[z[., .]] + B[z[., .]] # B[.]
            sage: A.coproduct(w)
            B[.] # B[x[z[., .], y[., .]]] + B[x[., .]] # B[z[., y[., .]]] +
            B[x[., .]] # B[y[z[., .], .]] + B[x[., y[., .]]] # B[z[., .]] +
            B[x[z[., .], .]] # B[y[., .]] + B[x[z[., .], y[., .]]] # B[.]
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a :class:`DendriformFunctor`
        and `R` is a ring, such that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: P = algebras.FreeDendriform(ZZ, 'x,y')
            sage: x,y = P.gens()
            sage: F, R = P.construction()
            sage: F
            Dendriform[x,y]
            sage: R
            Integer Ring
            sage: F(ZZ) is P
            True
            sage: F(QQ)
            Free Dendriform algebra on 2 generators ['x', 'y'] over Rational Field
        """

class DendriformFunctor(ConstructionFunctor):
    """
    A constructor for dendriform algebras.

    EXAMPLES::

        sage: P = algebras.FreeDendriform(ZZ, 'x,y')
        sage: x,y = P.gens()
        sage: F = P.construction()[0]; F
        Dendriform[x,y]

        sage: A = GF(5)['a,b']
        sage: a, b = A.gens()
        sage: F(A)
        Free Dendriform algebra on 2 generators ['x', 'y']
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: f = A.hom([a+b,a-b],A)
        sage: F(f)
        Generic endomorphism of Free Dendriform algebra on 2 generators ['x', 'y']
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: F(f)(a * F(A)(x))
        (a+b)*B[x[., .]]
    """
    rank: int
    vars: Incomplete
    def __init__(self, vars) -> None:
        """
        EXAMPLES::

            sage: F = sage.combinat.free_dendriform_algebra.DendriformFunctor(['x','y'])
            sage: F
            Dendriform[x,y]
            sage: F(ZZ)
            Free Dendriform algebra on 2 generators ['x', 'y']  over Integer Ring
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: F = algebras.FreeDendriform(ZZ, 'x,y,z').construction()[0]
            sage: G = algebras.FreeDendriform(QQ, 'x,y,z').construction()[0]
            sage: F == G
            True
            sage: G == loads(dumps(G))
            True
            sage: G = algebras.FreeDendriform(QQ, 'x,y').construction()[0]
            sage: F == G
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: F = algebras.FreeDendriform(ZZ, 'x,y,z').construction()[0]
            sage: G = algebras.FreeDendriform(QQ, 'x,y,z').construction()[0]
            sage: F != G
            False
            sage: G != loads(dumps(G))
            False
            sage: G = algebras.FreeDendriform(QQ, 'x,y').construction()[0]
            sage: F != G
            True
        """
    def __mul__(self, other):
        """
        If two Dendriform functors are given in a row, form a single Dendriform functor
        with all of the variables.

        EXAMPLES::

            sage: F = sage.combinat.free_dendriform_algebra.DendriformFunctor(['x','y'])
            sage: G = sage.combinat.free_dendriform_algebra.DendriformFunctor(['t'])
            sage: G * F
            Dendriform[x,y,t]
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        EXAMPLES::

            sage: F = sage.combinat.free_dendriform_algebra.DendriformFunctor(['x','y'])
            sage: G = sage.combinat.free_dendriform_algebra.DendriformFunctor(['t'])
            sage: F.merge(G)
            Dendriform[x,y,t]
            sage: F.merge(F)
            Dendriform[x,y]

        Now some actual use cases::

            sage: R = algebras.FreeDendriform(ZZ, 'x,y,z')
            sage: x,y,z = R.gens()
            sage: 1/2 * x
            1/2*B[x[., .]]
            sage: parent(1/2 * x)
            Free Dendriform algebra on 3 generators ['x', 'y', 'z'] over Rational Field

            sage: S = algebras.FreeDendriform(QQ, 'zt')
            sage: z,t = S.gens()
            sage: x + t
            B[t[., .]] + B[x[., .]]
            sage: parent(x + t)
            Free Dendriform algebra on 4 generators ['z', 't', 'x', 'y'] over Rational Field
        """
