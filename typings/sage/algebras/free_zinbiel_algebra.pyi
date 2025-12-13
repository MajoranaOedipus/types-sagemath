from _typeshed import Incomplete
from sage.categories.coalgebras_with_basis import CoalgebrasWithBasis as CoalgebrasWithBasis
from sage.categories.functor import Functor as Functor
from sage.categories.magmas import Magmas as Magmas
from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.categories.pushout import CompositeConstructionFunctor as CompositeConstructionFunctor, ConstructionFunctor as ConstructionFunctor, IdentityConstructionFunctor as IdentityConstructionFunctor
from sage.categories.rings import Rings as Rings
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.combinat.words.words import Words as Words
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import Family as Family
from sage.structure.coerce_exceptions import CoercionException as CoercionException

class FreeZinbielAlgebra(CombinatorialFreeModule):
    """
    The free Zinbiel algebra on `n` generators.

    Let `R` be a ring. A *Zinbiel algebra* is a non-associative
    algebra with multiplication `\\circ` that satisfies

    .. MATH::

        (a \\circ b) \\circ c = a \\circ (b \\circ c) + a \\circ (c \\circ b).

    Zinbiel algebras were first introduced by Loday (see [Lod1995]_ and
    [LV2012]_) as the Koszul dual to Leibniz algebras (hence the name
    coined by Lemaire).

    By default, the convention above is used. The opposite product,
    which satisfy the opposite axiom, can be used instead by setting
    the ``side`` parameter to ``'>'`` instead of the default value ``'<'``.

    Zinbiel algebras are divided power algebras, in that for

    .. MATH::

        x^{\\circ n} = \\bigl(x \\circ (x \\circ \\cdots \\circ( x \\circ x) \\cdots
        ) \\bigr)

    we have

    .. MATH::

        x^{\\circ m} \\circ x^{\\circ n} = \\binom{n+m-1}{m} x^{n+m}

    and

    .. MATH::

        \\underbrace{\\bigl( ( x \\circ \\cdots \\circ x \\circ (x \\circ x) \\cdots
        ) \\bigr)}_{n+1 \\text{ times}} = n! x^n.

    .. NOTE::

        This implies that Zinbiel algebras are not power associative.

    To every Zinbiel algebra, we can construct a corresponding commutative
    associative algebra by using the symmetrized product:

    .. MATH::

        a * b = a \\circ b + b \\circ a.

    The free Zinbiel algebra on `n` generators is isomorphic as `R`-modules
    to the reduced tensor algebra `\\bar{T}(R^n)` with the product

    .. MATH::

        (x_0 x_1 \\cdots x_p) \\circ (x_{p+1} x_{p+2} \\cdots x_{p+q})
        = \\sum_{\\sigma \\in S_{p,q}} x_0 (x_{\\sigma(1)} x_{\\sigma(2)}
        \\cdots x_{\\sigma(p+q)},

    where `S_{p,q}` is the set of `(p,q)`-shuffles.

    The free Zinbiel algebra is free as a divided power algebra. Moreover,
    the corresponding commutative algebra is isomorphic to the (non-unital)
    shuffle algebra.

    INPUT:

    - ``R`` -- a ring
    - ``n`` -- (optional) the number of generators
    - ``names`` -- the generator names

    .. WARNING::

        Currently the basis is indexed by all finite words over the variables,
        including the empty word. This is a slight abuse as it is supposed
        to be indexed by all non-empty words.

    EXAMPLES:

    We create the free Zinbiel algebra and check the defining relation::

        sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
        sage: (x*y)*z
        Z[xyz] + Z[xzy]
        sage: x*(y*z) + x*(z*y)
        Z[xyz] + Z[xzy]

    We see that the Zinbiel algebra is not associative, not even
    power associative::

        sage: x*(y*z)
        Z[xyz]
        sage: x*(x*x)
        Z[xxx]
        sage: (x*x)*x
        2*Z[xxx]

    We verify that it is a divided power algebra::

        sage: (x*(x*x)) * (x*(x*(x*x)))
        15*Z[xxxxxxx]
        sage: binomial(3+4-1,4)
        15
        sage: (x*(x*(x*x))) * (x*(x*x))
        20*Z[xxxxxxx]
        sage: binomial(3+4-1,3)
        20
        sage: ((x*x)*x)*x
        6*Z[xxxx]
        sage: (((x*x)*x)*x)*x
        24*Z[xxxxx]

    A few tests with the opposite convention for the product::

        sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ, side='>')
        sage: (x*y)*z
        Z[xyz]
        sage: x*(y*z)
        Z[xyz] + Z[yxz]

    TESTS::

        sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
        sage: Z.basis().keys()
        Finite words over {'x', 'y', 'z'}

        sage: A = algebras.FreeZinbiel(QQ,'z2,z3')
        sage: x, y = A.gens()
        sage: x*y
        Z[z2,z3]

    REFERENCES:

    - :wikipedia:`Zinbiel_algebra`

    - [Lod1995]_

    - [LV2012]_
    """
    @staticmethod
    def __classcall_private__(cls, R, n=None, names=None, prefix=None, side=None):
        """
        Standardize input to ensure a unique representation.

        TESTS::

            sage: Z1.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: Z2.<x,y,z> = algebras.FreeZinbiel(QQ, 3)
            sage: Z3 = algebras.FreeZinbiel(QQ, 3, 'x,y,z')
            sage: Z4.<x,y,z> = algebras.FreeZinbiel(QQ, 'x,y,z')
            sage: Z1 is Z2 and Z1 is Z3 and Z1 is Z4
            True

            sage: algebras.FreeZinbiel(QQ, ['x', 'y'])
            Free Zinbiel algebra on generators (Z[x], Z[y]) over Rational Field
            sage: algebras.FreeZinbiel(QQ, ('x', 'y'))
            Free Zinbiel algebra on generators (Z[x], Z[y]) over Rational Field

            sage: Z = algebras.FreeZinbiel(QQ, ZZ)
        """
    product_on_basis: Incomplete
    def __init__(self, R, n, names, prefix, side) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: TestSuite(Z).run()

            sage: Z = algebras.FreeZinbiel(QQ, ZZ)
            sage: G = Z.algebra_generators()
            sage: TestSuite(Z).run(elements=[Z.an_element(), G[1], G[1]*G[2]*G[0]])

        TESTS::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(5)
            Traceback (most recent call last):
            ...
            TypeError: argument R must be a ring

            sage: algebras.FreeZinbiel(QQ, ['x', 'y'], prefix='f')
            Free Zinbiel algebra on generators (f[x], f[y]) over Rational Field
        """
    def side(self):
        """
        Return the choice of side for the product.

        This is either ``'<'`` or ``'>'``.

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: Z.side()
            '<'
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: list(Z.algebra_generators())
            [Z[x], Z[y], Z[z]]
        """
    def change_ring(self, R):
        """
        Return the free Zinbiel algebra in the same variables over ``R``.

        INPUT:

        - ``R`` -- a ring

        The same side convention is used for the product.

        EXAMPLES::

            sage: A = algebras.FreeZinbiel(ZZ, 'f,g,h')
            sage: A.change_ring(QQ)
            Free Zinbiel algebra on generators (Z[f], Z[g], Z[h])
            over Rational Field
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: Z.gens()
            (Z[x], Z[y], Z[z])
        """
    def degree_on_basis(self, t):
        """
        Return the degree of a word in the free Zinbiel algebra.

        This is the length.

        EXAMPLES::

            sage: A = algebras.FreeZinbiel(QQ, 'x,y')
            sage: W = A.basis().keys()
            sage: A.degree_on_basis(W('xy'))
            2
        """
    def product_on_basis_left(self, x, y):
        """
        Return the product < of the basis elements indexed by ``x`` and ``y``.

        This is one half of the shuffle product, where the first letter
        comes from the first letter of the first argument.

        INPUT:

        - ``x``, ``y`` -- two words

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ)
            sage: (x*y)*z  # indirect doctest
            Z[xyz] + Z[xzy]

        TESTS::

            sage: Z.<x,y> = algebras.FreeZinbiel(QQ)
            sage: Z.product_on_basis(Word(), Word('y'))
            Z[y]
        """
    def product_on_basis_right(self, x, y):
        """
        Return the product > of the basis elements indexed by ``x`` and ``y``.

        This is one half of the shuffle product, where the last letter
        comes from the last letter of the second argument.

        INPUT:

        - ``x``, ``y`` -- two words

        EXAMPLES::

            sage: Z.<x,y,z> = algebras.FreeZinbiel(QQ, side='>')
            sage: (x*y)*z  # indirect doctest
            Z[xyz]

        TESTS::

            sage: Z.<x,y> = algebras.FreeZinbiel(QQ, side='>')
            sage: Z.product_on_basis(Word('x'), Word())
            Z[x]
        """
    def coproduct_on_basis(self, w):
        """
        Return the coproduct of the element of the basis indexed by
        the word ``w``.

        The coproduct is given by deconcatenation.

        INPUT:

        - ``w`` -- a word

        EXAMPLES::

            sage: F = algebras.FreeZinbiel(QQ,['a','b'])
            sage: F.coproduct_on_basis(Word('a'))
            Z[] # Z[a] + Z[a] # Z[]
            sage: F.coproduct_on_basis(Word('aba'))
            Z[] # Z[aba] + Z[a] # Z[ba] + Z[ab] # Z[a] + Z[aba] # Z[]
            sage: F.coproduct_on_basis(Word())
            Z[] # Z[]

        TESTS::

            sage: F = algebras.FreeZinbiel(QQ,['a','b'])
            sage: S = F.an_element(); S
            Z[] + 2*Z[a] + 3*Z[b] + Z[bab]
            sage: F.coproduct(S)
            Z[] # Z[] + 2*Z[] # Z[a] + 3*Z[] # Z[b] + Z[] # Z[bab] +
            2*Z[a] # Z[] + 3*Z[b] # Z[] + Z[b] # Z[ab] + Z[ba] # Z[b] +
            Z[bab] # Z[]
        """
    def counit(self, S):
        """
        Return the counit of ``S``.

        EXAMPLES::

            sage: F = algebras.FreeZinbiel(QQ,['a','b'])
            sage: S = F.an_element(); S
            Z[] + 2*Z[a] + 3*Z[b] + Z[bab]
            sage: F.counit(S)
            1
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a :class:`ZinbielFunctor`
        and ``R`` is a ring, such that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: P = algebras.FreeZinbiel(ZZ, 'x,y')
            sage: x,y = P.gens()
            sage: F, R = P.construction()
            sage: F
            Zinbiel[x,y]
            sage: R
            Integer Ring
            sage: F(ZZ) is P
            True
            sage: F(QQ)
            Free Zinbiel algebra on generators (Z[x], Z[y]) over Rational Field
        """

class ZinbielFunctor(ConstructionFunctor):
    """
    A constructor for free Zinbiel algebras.

    EXAMPLES::

        sage: P = algebras.FreeZinbiel(ZZ, 'x,y')
        sage: x,y = P.gens()
        sage: F = P.construction()[0]; F
        Zinbiel[x,y]

        sage: A = GF(5)['a,b']
        sage: a, b = A.gens()
        sage: F(A)
        Free Zinbiel algebra on generators (Z[x], Z[y])
        over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: f = A.hom([a+b,a-b],A)
        sage: F(f)
        Generic endomorphism of Free Zinbiel algebra on generators (Z[x], Z[y])
        over Multivariate Polynomial Ring in a, b over Finite Field of size 5

        sage: F(f)(a * F(A)(x))
        (a+b)*Z[x]
    """
    rank: int
    vars: Incomplete
    def __init__(self, variables, side) -> None:
        """
        EXAMPLES::

            sage: functor = sage.algebras.free_zinbiel_algebra.ZinbielFunctor
            sage: F = functor(['x','y'], '<'); F
            Zinbiel[x,y]
            sage: F(ZZ)
            Free Zinbiel algebra on generators (Z[x], Z[y]) over Integer Ring
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: F = algebras.FreeZinbiel(ZZ, 'x,y,z').construction()[0]
            sage: G = algebras.FreeZinbiel(QQ, 'x,y,z').construction()[0]
            sage: F == G
            True
            sage: G == loads(dumps(G))
            True
            sage: G = algebras.FreeZinbiel(QQ, 'x,y').construction()[0]
            sage: F == G
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: F = algebras.FreeZinbiel(ZZ, 'x,y,z').construction()[0]
            sage: G = algebras.FreeZinbiel(QQ, 'x,y,z').construction()[0]
            sage: hash(F) == hash(G)
            True
        """
    def __mul__(self, other):
        """
        If two Zinbiel functors are given in a row, form a single
        Zinbiel functor with all of the variables.

        EXAMPLES::

            sage: from sage.algebras.free_zinbiel_algebra import ZinbielFunctor as functor
            sage: F = functor(['x','y'], '<')
            sage: G = functor(['t'], '<')
            sage: G * F
            Zinbiel[x,y,t]

        With an infinite generating set::

            sage: H = functor(ZZ, '<')
            sage: H * G
            Traceback (most recent call last):
            ...
            CoercionException: Unable to determine overlap for infinite sets
            sage: G * H
            Traceback (most recent call last):
            ...
            CoercionException: Unable to determine overlap for infinite sets
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        EXAMPLES::

            sage: functor = sage.algebras.free_zinbiel_algebra.ZinbielFunctor
            sage: F = functor(['x','y'], '<')
            sage: G = functor(['t'], '<')
            sage: F.merge(G)
            Zinbiel[x,y,t]
            sage: F.merge(F)
            Zinbiel[x,y]

        With an infinite generating set::

            sage: H = functor(ZZ, '<')
            sage: H.merge(H) is H
            True
            sage: H.merge(F) is None
            True
            sage: F.merge(H) is None
            True

        Now some actual use cases::

            sage: R = algebras.FreeZinbiel(ZZ, 'x,y,z')
            sage: x,y,z = R.gens()
            sage: 1/2 * x
            1/2*Z[x]
            sage: parent(1/2 * x)
            Free Zinbiel algebra on generators (Z[x], Z[y], Z[z])
            over Rational Field

            sage: S = algebras.FreeZinbiel(QQ, 'z,t')
            sage: z,t = S.gens()
            sage: x * t
            Z[xt]
            sage: parent(x * t)
            Free Zinbiel algebra on generators (Z[z], Z[t], Z[x], Z[y])
            over Rational Field

        TESTS:

        Using the other side convention::

            sage: F = functor(['x','y'], '>')
            sage: G = functor(['t'], '>')
            sage: H = functor(['t'], '<')
            sage: F.merge(G)
            Zinbiel[x,y,t]
            sage: F.merge(H)
            Traceback (most recent call last):
            ...
            TypeError: cannot merge free Zinbiel algebras with distinct sides
        """
