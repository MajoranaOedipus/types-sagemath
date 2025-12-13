from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElementWrapper as LieAlgebraElementWrapper, LieAlgebraMatrixWrapper as LieAlgebraMatrixWrapper
from sage.categories.algebras import Algebras as Algebras
from sage.categories.homset import Hom as Hom
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras, LiftMorphism as LiftMorphism
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.categories.rings import Rings as Rings
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import AbstractFamily as AbstractFamily, Family as Family
from sage.structure.indexed_generators import standardize_names_index_set as standardize_names_index_set
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LieAlgebra(Parent, UniqueRepresentation):
    '''
    A Lie algebra `L` over a base ring `R`.

    A Lie algebra is an `R`-module `L` with a bilinear operation called
    Lie bracket `[\\cdot, \\cdot] : L \\times L \\to L` such that
    `[x, x] = 0` and the following relation holds:

    .. MATH::

        \\bigl[ x, [y, z] \\bigr] + \\bigl[ y, [z, x] \\bigr]
        + \\bigl[ z, [x, y] \\bigr] = 0.

    This relation is known as the *Jacobi identity* (or sometimes the Jacobi
    relation). We note that from `[x, x] = 0`, we have `[x + y, x + y] = 0`.
    Next from bilinearity, we see that

    .. MATH::

        0 = [x + y, x + y] = [x, x] + [x, y] + [y, x] + [y, y]
        = [x, y] + [y, x],

    thus `[x, y] = -[y, x]` and the Lie bracket is antisymmetric.

    Lie algebras are closely related to Lie groups. Let `G` be a Lie group
    and fix some `g \\in G`. We can construct the Lie algebra `L` of `G` by
    considering the tangent space at `g`. We can also (partially) recover `G`
    from `L` by using what is known as the exponential map.

    Given any associative algebra `A`, we can construct a Lie algebra `L`
    on the `R`-module `A` by defining the Lie bracket to be the commutator
    `[a, b] = ab - ba`. We call an associative algebra `A` which contains
    `L` in this fashion an *enveloping algebra* of `L`. The embedding
    `L \\to A` which sends the Lie bracket to the commutator will be called
    a Lie embedding. Now if we are given a Lie algebra `L`, we
    can construct an enveloping algebra `U_L` with Lie embedding `h : L \\to
    U_L` which has the following universal property: for any enveloping
    algebra `A` with Lie embedding `f : L \\to A`, there exists a unique unital
    algebra homomorphism `g : U_L \\to A` such that `f = g \\circ h`. The
    algebra `U_L` is known as the *universal enveloping algebra* of `L`.

    INPUT:

    See examples below for various input options.

    EXAMPLES:

    **1.** The simplest examples of Lie algebras are *abelian Lie
    algebras*. These are Lie algebras whose Lie bracket is (identically)
    zero. We can create them using the ``abelian`` keyword::

        sage: L.<x,y,z> = LieAlgebra(QQ, abelian=True); L
        Abelian Lie algebra on 3 generators (x, y, z) over Rational Field

    **2.** A Lie algebra can be built from any associative algebra by
    defining the Lie bracket to be the commutator. For example, we can
    start with the descent algebra::

        sage: D = DescentAlgebra(QQ, 4).D()
        sage: L = LieAlgebra(associative=D); L
        Lie algebra of Descent algebra of 4 over Rational Field
         in the standard basis
        sage: L(D[2]).bracket(L(D[3]))
        D{1, 2} - D{1, 3} + D{2} - D{3}

    Next we use a free algebra and do some simple computations::

        sage: R.<a,b,c> = FreeAlgebra(QQ, 3)
        sage: L.<x,y,z> = LieAlgebra(associative=R.gens())
        sage: x-y+z
        a - b + c
        sage: L.bracket(x-y, x-z)
        a*b - a*c - b*a + b*c + c*a - c*b
        sage: L.bracket(x-y, L.bracket(x,y))
        a^2*b - 2*a*b*a + a*b^2 + b*a^2 - 2*b*a*b + b^2*a

    We can also use a subset of the elements as a generating set
    of the Lie algebra::

        sage: R.<a,b,c> = FreeAlgebra(QQ, 3)
        sage: L.<x,y> = LieAlgebra(associative=[a,b+c])
        sage: L.bracket(x, y)
        a*b + a*c - b*a - c*a

    Now for a more complicated example using the group ring of `S_3` as our
    base algebra::

        sage: G = SymmetricGroup(3)
        sage: S = GroupAlgebra(G, QQ)
        sage: L.<x,y> = LieAlgebra(associative=S.gens())
        sage: L.bracket(x, y)
        (2,3) - (1,3)
        sage: L.bracket(x, y-x)
        (2,3) - (1,3)
        sage: L.bracket(L.bracket(x, y), y)
        2*(1,2,3) - 2*(1,3,2)
        sage: L.bracket(x, L.bracket(x, y))
        (2,3) - 2*(1,2) + (1,3)
        sage: L.bracket(x, L.bracket(L.bracket(x, y), y))
        0

    Here is an example using matrices::

        sage: MS = MatrixSpace(QQ,2)
        sage: m1 = MS([[0, -1], [1, 0]])
        sage: m2 = MS([[-1, 4], [3, 2]])
        sage: L.<x,y> = LieAlgebra(associative=[m1, m2])
        sage: x
        [ 0 -1]
        [ 1  0]
        sage: y
        [-1  4]
        [ 3  2]
        sage: L.bracket(x,y)
        [-7 -3]
        [-3  7]
        sage: L.bracket(y,y)
        [0 0]
        [0 0]
        sage: L.bracket(y,x)
        [ 7  3]
        [ 3 -7]
        sage: L.bracket(x, L.bracket(y,x))
        [-6 14]
        [14  6]

    (See :class:`LieAlgebraFromAssociative` for other examples.)

    **3.** We can also creating a Lie algebra by inputting a set of
    structure coefficients. For example, we can create the Lie algebra
    of `\\QQ^3` under the Lie bracket `\\times` (cross-product)::

        sage: d = {(\'x\',\'y\'): {\'z\':1}, (\'y\',\'z\'): {\'x\':1}, (\'z\',\'x\'): {\'y\':1}}
        sage: L.<x,y,z> = LieAlgebra(QQ, d)
        sage: L
        Lie algebra on 3 generators (x, y, z) over Rational Field

    To compute the Lie bracket of two elements, you cannot use the ``*``
    operator. Indeed, this automatically lifts up to the universal
    enveloping algebra and takes the (associative) product there.
    To get elements in the Lie algebra, you must use :meth:`bracket`::

        sage: L = LieAlgebra(QQ, {(\'e\',\'h\'): {\'e\':-2}, (\'f\',\'h\'): {\'f\':2},
        ....:                     (\'e\',\'f\'): {\'h\':1}}, names=\'e,f,h\')
        sage: e,f,h = L.lie_algebra_generators()
        sage: L.bracket(h, e)
        2*e
        sage: elt = h*e; elt
        e*h + 2*e
        sage: P = elt.parent(); P
        Noncommutative Multivariate Polynomial Ring in e, f, h over Rational Field,
         nc-relations: {...}
        sage: R = P.relations()
        sage: for rhs in sorted(R, key=str): print("{} = {}".format(rhs, R[rhs]))
        f*e = e*f - h
        h*e = e*h + 2*e
        h*f = f*h - 2*f

    For convenience, there are two shorthand notations for computing
    Lie brackets::

        sage: L([h,e])
        2*e
        sage: L([h,[e,f]])
        0
        sage: L([[h,e],[e,f]])
        -4*e
        sage: L[h, e]
        2*e
        sage: L[h, L[e, f]]
        0

    .. WARNING::

        Because this is a modified (abused) version of python syntax, it
        does **NOT** work with addition. For example ``L([e + [h, f], h])``
        and ``L[e + [h, f], h]`` will both raise errors. Instead you must
        use ``L[e + L[h, f], h]``.

    **4.** We can construct a Lie algebra from a Cartan type by using
    the ``cartan_type`` option::

        sage: L = LieAlgebra(ZZ, cartan_type=[\'C\', 3])
        sage: L.inject_variables()
        Defining e1, e2, e3, f1, f2, f3, h1, h2, h3
        sage: e1.bracket(e2)
        -E[alpha[1] + alpha[2]]
        sage: L([[e1, e2], e2])
        0
        sage: L([[e2, e3], e3])
        0
        sage: L([e2, [e2, e3]])
        2*E[2*alpha[2] + alpha[3]]

        sage: L = LieAlgebra(ZZ, cartan_type=[\'E\', 6])
        sage: L
        Lie algebra of [\'E\', 6] in the Chevalley basis

    When the Cartan type is finite type and simply-laced, we can also
    specify an asymmetry function from [Ka1990]_ using a Dynkin diagram
    orientation with the ``epsilon`` option::

        sage: L = LieAlgebra(QQ, cartan_type=[\'A\', 2], epsilon=[(1, 2)])
        sage: e1, e2 = L.e()
        sage: L[e1, e2]
        -E[alpha[1] + alpha[2]]

        sage: L = LieAlgebra(QQ, cartan_type=[\'A\', 2], epsilon=[(2, 1)])
        sage: e1, e2 = L.e()
        sage: L[e1, e2]
        E[alpha[1] + alpha[2]]

    We also have matrix versions of the classical Lie algebras::

        sage: L = LieAlgebra(ZZ, cartan_type=[\'A\', 2], representation=\'matrix\')
        sage: L.gens()
        (
        [0 1 0]  [0 0 0]  [0 0 0]  [0 0 0]  [ 1  0  0]  [ 0  0  0]
        [0 0 0]  [0 0 1]  [1 0 0]  [0 0 0]  [ 0 -1  0]  [ 0  1  0]
        [0 0 0], [0 0 0], [0 0 0], [0 1 0], [ 0  0  0], [ 0  0 -1]
        )

    There is also the compact real form of matrix Lie algebras
    implemented (the base ring must currently be a field)::

        sage: L = LieAlgebra(QQ, cartan_type=[\'A\', 2], representation="compact real")
        sage: list(L.basis())
        [
        [ 0  1  0]  [ 0  0  1]  [ 0  0  0]  [ i  0  0]  [0 i 0]  [0 0 i]
        [-1  0  0]  [ 0  0  0]  [ 0  0  1]  [ 0  0  0]  [i 0 0]  [0 0 0]
        [ 0  0  0], [-1  0  0], [ 0 -1  0], [ 0  0 -i], [0 0 0], [i 0 0],
        <BLANKLINE>
        [ 0  0  0]  [0 0 0]
        [ 0  i  0]  [0 0 i]
        [ 0  0 -i], [0 i 0]
        ]

    **5.** We construct a free Lie algebra in a few different ways. There are
    two primary representations, as brackets and as polynomials::

        sage: L = LieAlgebra(QQ, \'x,y,z\'); L
        Free Lie algebra generated by (x, y, z) over Rational Field
        sage: P.<a,b,c> = LieAlgebra(QQ, representation=\'polynomial\'); P
        Lie algebra generated by (a, b, c) in
         Free Algebra on 3 generators (a, b, c) over Rational Field

    This has the basis given by Hall and the one indexed by Lyndon words.
    We do some computations and convert between the bases::

        sage: H = L.Hall()
        doctest:warning...:
        FutureWarning: The Hall basis has not been fully proven correct, but currently no bugs are known
        See https://github.com/sagemath/sage/issues/16823 for details.
        sage: H
        Free Lie algebra generated by (x, y, z) over Rational Field in the Hall basis
        sage: Lyn = L.Lyndon()
        sage: Lyn
        Free Lie algebra generated by (x, y, z) over Rational Field in the Lyndon basis
        sage: x,y,z = Lyn.lie_algebra_generators()
        sage: a = Lyn([x, [[z, [x, y]], [y, x]]]); a
        -[x, [[x, y], [x, [y, z]]]] - [x, [[x, y], [[x, z], y]]]
        sage: H(a)
        [[x, y], [z, [x, [x, y]]]] - [[x, y], [[x, y], [x, z]]]
         + [[x, [x, y]], [z, [x, y]]]

    We also have the free Lie algebra given in the polynomial
    representation, which is the canonical embedding of the free
    Lie algebra into the free algebra (i.e., the ring of
    noncommutative polynomials).
    So the generators of the free Lie algebra are the generators of the
    free algebra and the Lie bracket is the commutator::

        sage: P.<a,b,c> = LieAlgebra(QQ, representation=\'polynomial\'); P
        Lie algebra generated by (a, b, c) in
         Free Algebra on 3 generators (a, b, c) over Rational Field
        sage: P.bracket(a, b) + P.bracket(a - c, b + 3*c)
        2*a*b + 3*a*c - 2*b*a + b*c - 3*c*a - c*b

    **6.** Nilpotent Lie algebras are Lie algebras such that there exists an
    integer `s` such that all iterated brackets of length longer than `s`
    are zero. They can be constructed from structural coefficients using the
    ``nilpotent`` keyword::

        sage: L.<X,Y,Z> = LieAlgebra(QQ, {(\'X\',\'Y\'): {\'Z\': 1}}, nilpotent=True)
        sage: L
        Nilpotent Lie algebra on 3 generators (X, Y, Z) over Rational Field
        sage: L.category()
        Category of finite dimensional nilpotent Lie algebras with basis over Rational Field

    A second example defining the Engel Lie algebra::

        sage: sc = {(\'X\',\'Y\'): {\'Z\': 1}, (\'X\',\'Z\'): {\'W\': 1}}
        sage: E.<X,Y,Z,W> = LieAlgebra(QQ, sc, nilpotent=True); E
        Nilpotent Lie algebra on 4 generators (X, Y, Z, W) over Rational Field
        sage: E.step()
        3
        sage: E[X, Y + Z]
        Z + W
        sage: E[X, [X, Y + Z]]
        W
        sage: E[X, [X, [X, Y + Z]]]
        0

    A nilpotent Lie algebra will also be constructed if given a ``category``
    of a nilpotent Lie algebra::

        sage: C = LieAlgebras(QQ).Nilpotent().FiniteDimensional().WithBasis()
        sage: L.<X,Y,Z> = LieAlgebra(QQ, {(\'X\',\'Y\'): {\'Z\': 1}}, category=C); L
        Nilpotent Lie algebra on 3 generators (X, Y, Z) over Rational Field

    **7.** Free nilpotent Lie algebras are the truncated versions of the free
    Lie algebras. That is, the only relations other than anticommutativity
    and the Jacobi identity among the Lie brackets are that brackets of
    length higher than the nilpotency step vanish. They can be created by
    using the ``step`` keyword::

        sage: L = LieAlgebra(ZZ, 2, step=3); L
        Free Nilpotent Lie algebra on 5 generators (X_1, X_2, X_12, X_112, X_122) over Integer Ring
        sage: L.step()
        3

    REFERENCES:

    - [deG2000]_ Willem A. de Graaf. *Lie Algebras: Theory and Algorithms*.
    - [Ka1990]_ Victor Kac, *Infinite dimensional Lie algebras*.
    - :wikipedia:`Lie_algebra`
    '''
    @staticmethod
    def __classcall_private__(cls, R=None, arg0=None, arg1=None, names=None, index_set=None, abelian: bool = False, nilpotent: bool = False, category=None, **kwds):
        """
        Select the correct parent based upon input.

        TESTS::

            sage: LieAlgebra(QQ, abelian=True, names='x,y,z')
            Abelian Lie algebra on 3 generators (x, y, z) over Rational Field
            sage: LieAlgebra(QQ, {('e','h'): {'e':-2}, ('f','h'): {'f':2},
            ....:                 ('e','f'): {'h':1}}, names='e,f,h')
            Lie algebra on 3 generators (e, f, h) over Rational Field
        """
    def __init__(self, R, names=None, category=None) -> None:
        """
        The Lie algebra.

        INPUT:

        - ``R`` -- the base ring

        - ``names`` -- (optional) the names of the generators

        - ``category`` -- the category of the Lie algebra; the default is the
          category of Lie algebras over ``R``

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L.category()
            Category of finite dimensional nilpotent Lie algebras with basis over Rational Field
        """
    def __getitem__(self, x):
        """
        If ``x`` is a pair `(a, b)`, return the Lie bracket `[a, b]
        (including if `a` or `b` are Lie (sub)algebras, in which case the
        corresponding ideal is constructed).
        Otherwise try to return the `x`-th element of ``self``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, representation='polynomial')
            sage: L[x, [y, x]]
            -x^2*y + 2*x*y*x - y*x^2

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L[L, L]
            Ideal () of Abelian Lie algebra on 2 generators (x, y) over Rational Field

            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: Z = L[L, L]; Z
            Ideal (z) of Heisenberg algebra of rank 1 over Rational Field
            sage: L[Z, L]
            Ideal () of Heisenberg algebra of rank 1 over Rational Field

            sage: p,q,z = L.basis(); (p, q, z)
            (p1, q1, z)
            sage: L[p, L]
            Ideal (p1) of Heisenberg algebra of rank 1 over Rational Field
            sage: L[L, p+q]
            Ideal (p1 + q1) of Heisenberg algebra of rank 1 over Rational Field
        """
    @cached_method
    def zero(self):
        """
        Return the element `0`.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, representation='polynomial')
            sage: L.zero()
            0
        """
    def monomial(self, i):
        """
        Return the monomial indexed by ``i``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.monomial('p1')
            p1
        """
    def term(self, i, c=None):
        """
        Return the term indexed by ``i`` with coefficient ``c``.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, oo)
            sage: L.term('p1', 4)
            4*p1
        """
    def get_order(self):
        """
        Return an ordering of the basis indices.

        .. TODO::

            Remove this method and in :class:`CombinatorialFreeModule`
            in favor of a method in the category of (finite dimensional)
            modules with basis.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, {})
            sage: L.get_order()
            ('x', 'y')
        """

class LieAlgebraWithGenerators(LieAlgebra):
    """
    A Lie algebra with distinguished generators.
    """
    def __init__(self, R, names=None, index_set=None, category=None, prefix: str = 'L', **kwds) -> None:
        """
        The Lie algebra.

        INPUT:

        - ``R`` -- the base ring
        - ``names`` -- (optional) the names of the generators
        - ``index_set`` -- (optional) the indexing set
        - ``category`` -- the category of the Lie algebra; the default is the
          category of Lie algebras over ``R``
        - ``prefix`` -- (optional) the prefix for the generator representation
        - any keyword accepted by
          :class:`~sage.structure.indexed_generators.IndexedGenerators`

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L.category()
            Category of finite dimensional nilpotent Lie algebras with basis over Rational Field
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, representation='polynomial')
            sage: L.lie_algebra_generators()
            Finite family {'x': x, 'y': y}
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return a tuple whose entries are the generators for this
        object, in some order.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L.gens()
            (x, y)
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L.gen(0)
            x
        """
    def indices(self):
        """
        Return the indices of ``self``.

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, representation='polynomial')
            sage: L.indices()
            {'x', 'y'}
        """

class FinitelyGeneratedLieAlgebra(LieAlgebraWithGenerators):
    """
    A finitely generated Lie algebra.
    """
    def __init__(self, R, names=None, index_set=None, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``R`` -- the base ring

        - ``names`` -- the names of the generators

        - ``index_set`` -- the index set of the generators

        - ``category`` -- the category of the Lie algebra

        EXAMPLES::

            sage: L.<x,y> = LieAlgebra(QQ, abelian=True)
            sage: L.category()
            Category of finite dimensional nilpotent Lie algebras with basis over Rational Field
        """

class InfinitelyGeneratedLieAlgebra(LieAlgebraWithGenerators):
    """
    An infinitely generated Lie algebra.
    """

class LieAlgebraFromAssociative(LieAlgebraWithGenerators):
    """
    A Lie algebra whose elements are from an associative algebra and whose
    bracket is the commutator.

    .. TODO::

        Split this class into 2 classes, the base class for the Lie
        algebra corresponding to the full associative algebra and a
        subclass for the Lie subalgebra (of the full algebra)
        generated by a generating set?

    .. TODO::

        Return the subalgebra generated by the basis
        elements of ``self`` for the universal enveloping algebra.

    EXAMPLES:

    For the first example, we start with a commutative algebra.
    Note that the bracket of everything will be 0::

        sage: R = SymmetricGroupAlgebra(QQ, 2)
        sage: L = LieAlgebra(associative=R)
        sage: x, y = L.basis()
        sage: L.bracket(x, y)
        0

    Next we use a free algebra and do some simple computations::

        sage: R.<a,b> = FreeAlgebra(QQ, 2)
        sage: L = LieAlgebra(associative=R)
        sage: x,y = L(a), L(b)
        sage: x-y
        a - b
        sage: L.bracket(x-y, x)
        a*b - b*a
        sage: L.bracket(x-y, L.bracket(x,y))
        a^2*b - 2*a*b*a + a*b^2 + b*a^2 - 2*b*a*b + b^2*a

    We can also use a subset of the generators as a generating set
    of the Lie algebra::

        sage: R.<a,b,c> = FreeAlgebra(QQ, 3)
        sage: L.<x,y> = LieAlgebra(associative=[a,b])

    Now for a more complicated example using the group ring of `S_3`
    as our base algebra::

        sage: G = SymmetricGroup(3)
        sage: S = GroupAlgebra(G, QQ)
        sage: L.<x,y> = LieAlgebra(associative=S.gens())
        sage: L.bracket(x, y)
        (2,3) - (1,3)
        sage: L.bracket(x, y-x)
        (2,3) - (1,3)
        sage: L.bracket(L.bracket(x, y), y)
        2*(1,2,3) - 2*(1,3,2)
        sage: L.bracket(x, L.bracket(x, y))
        (2,3) - 2*(1,2) + (1,3)
        sage: L.bracket(x, L.bracket(L.bracket(x, y), y))
        0

    Here is an example using matrices::

        sage: MS = MatrixSpace(QQ,2)
        sage: m1 = MS([[0, -1], [1, 0]])
        sage: m2 = MS([[-1, 4], [3, 2]])
        sage: L.<x,y> = LieAlgebra(associative=[m1, m2])
        sage: x
        [ 0 -1]
        [ 1  0]
        sage: y
        [-1  4]
        [ 3  2]
        sage: L.bracket(x,y)
        [-7 -3]
        [-3  7]
        sage: L.bracket(y,y)
        [0 0]
        [0 0]
        sage: L.bracket(y,x)
        [ 7  3]
        [ 3 -7]
        sage: L.bracket(x, L.bracket(y,x))
        [-6 14]
        [14  6]
    """
    @staticmethod
    def __classcall_private__(cls, A, gens=None, names=None, index_set=None, free_lie_algebra: bool = False, category=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L1 = LieAlgebra(associative=tuple(S.gens()), names=['x','y'])
            sage: L2 = LieAlgebra(associative=[ S(G((1,2,3))), S(G((1,2))) ], names='x,y')
            sage: L1 is L2
            True

            sage: F.<x,y,z> = FreeAlgebra(QQ)
            sage: L1 = LieAlgebra(associative=F.algebra_generators(), names='x,y,z')
            sage: L2.<x,y,z> = LieAlgebra(associative=F.gens())
            sage: L1 is L2
            True
        """
    def __init__(self, A, gens=None, names=None, index_set=None, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L = LieAlgebra(associative=S)
            sage: TestSuite(L).run()

        TESTS::

            sage: from sage.algebras.lie_algebras.lie_algebra import LieAlgebraFromAssociative as LAFA
            sage: LAFA(MatrixSpace(QQ, 0, sparse=True), [], names=())
            Lie algebra generated by () in Full MatrixSpace of 0 by 0 sparse matrices over Rational Field
        """
    def associative_algebra(self):
        """
        Return the associative algebra used to construct ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L = LieAlgebra(associative=S)
            sage: L.associative_algebra() is S
            True
        """
    def lie_algebra_generators(self):
        """
        Return the Lie algebra generators of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L = LieAlgebra(associative=S)
            sage: L.lie_algebra_generators()
            Finite family {(): (), (1,3,2): (1,3,2), (1,2,3): (1,2,3),
                           (2,3): (2,3), (1,3): (1,3), (1,2): (1,2)}
        """
    def monomial(self, i):
        """
        Return the monomial indexed by ``i``.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(QQ)
            sage: L = LieAlgebra(associative=F)
            sage: L.monomial(x.leading_support())
            x
        """
    def term(self, i, c=None):
        """
        Return the term indexed by ``i`` with coefficient ``c``.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(QQ)
            sage: L = LieAlgebra(associative=F)
            sage: L.term(x.leading_support(), 4)
            4*x
        """
    @cached_method
    def zero(self):
        """
        Return the element `0` in ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L = LieAlgebra(associative=S)
            sage: L.zero()
            0
        """
    def is_abelian(self):
        """
        Return ``True`` if ``self`` is abelian.

        EXAMPLES::

            sage: R = FreeAlgebra(QQ, 2, 'x,y')
            sage: L = LieAlgebra(associative=R.gens())
            sage: L.is_abelian()
            False

            sage: R = PolynomialRing(QQ, 'x,y')
            sage: L = LieAlgebra(associative=R.gens())
            sage: L.is_abelian()
            True

        An example with a Lie algebra from the group algebra::

            sage: G = SymmetricGroup(3)
            sage: S = GroupAlgebra(G, QQ)
            sage: L = LieAlgebra(associative=S)
            sage: L.is_abelian()
            False

        Now we construct a Lie algebra from commuting elements in the group
        algebra::

            sage: G = SymmetricGroup(5)
            sage: S = GroupAlgebra(G, QQ)
            sage: gens = map(S, [G((1, 2)), G((3, 4))])
            sage: L.<x,y> = LieAlgebra(associative=gens)
            sage: L.is_abelian()
            True
        """
    class Element(LieAlgebraElementWrapper):
        def lift_associative(self):
            """
            Lift ``self`` to the ambient associative algebra (which
            might be smaller than the universal enveloping algebra).

            EXAMPLES::

                sage: R = FreeAlgebra(QQ, 3, 'x,y,z')
                sage: L.<x,y,z> = LieAlgebra(associative=R.gens())
                sage: x.lift_associative()
                x
                sage: x.lift_associative().parent()
                Free Algebra on 3 generators (x, y, z) over Rational Field
            """
        def monomial_coefficients(self, copy: bool = True):
            """
            Return the monomial coefficients of ``self`` (if this
            notion makes sense for ``self.parent()``).

            EXAMPLES::

                sage: R.<x,y,z> = FreeAlgebra(QQ)
                sage: L = LieAlgebra(associative=R)
                sage: elt = L(x) + 2*L(y) - L(z)
                sage: sorted(elt.monomial_coefficients().items())
                [(x, 1), (y, 2), (z, -1)]

                sage: L = LieAlgebra(associative=[x,y])
                sage: elt = L(x) + 2*L(y)
                sage: elt.monomial_coefficients()
                Traceback (most recent call last):
                ...
                NotImplementedError: the basis is not defined
            """

class LiftMorphismToAssociative(LiftMorphism):
    """
    The natural lifting morphism from a Lie algebra constructed from
    an associative algebra `A` to `A`.
    """
    def preimage(self, x):
        """
        Return the preimage of ``x`` under ``self``.

        EXAMPLES::

            sage: R = FreeAlgebra(QQ, 3, 'a,b,c')
            sage: L = LieAlgebra(associative=R)
            sage: x,y,z = R.gens()
            sage: f = R.coerce_map_from(L)
            sage: p = f.preimage(x*y - z); p
            -c + a*b
            sage: p.parent() is L
            True
        """
    def section(self):
        """
        Return the section map of ``self``.

        EXAMPLES::

            sage: R = FreeAlgebra(QQ, 3, 'x,y,z')
            sage: L.<x,y,z> = LieAlgebra(associative=R.gens())
            sage: f = R.coerce_map_from(L)
            sage: f.section()
            Generic morphism:
              From: Free Algebra on 3 generators (x, y, z) over Rational Field
              To:   Lie algebra generated by (x, y, z) in Free Algebra on 3 generators (x, y, z) over Rational Field
        """

class MatrixLieAlgebraFromAssociative(LieAlgebraFromAssociative):
    """
    A Lie algebra constructed from a matrix algebra.

    This means a Lie algebra consisting of matrices,
    with commutator as Lie bracket.
    """
    class Element(LieAlgebraMatrixWrapper, LieAlgebraFromAssociative.Element):
        def matrix(self):
            """
            Return ``self`` as element of the underlying matrix algebra.

            OUTPUT: an instance of the element class of MatrixSpace

            EXAMPLES::

                sage: sl3m = lie_algebras.sl(ZZ, 3, representation='matrix')
                sage: e1,e2, f1, f2, h1, h2 = sl3m.gens()
                sage: h1m = h1.matrix(); h1m
                [ 1  0  0]
                [ 0 -1  0]
                [ 0  0  0]
                sage: h1m.parent()
                Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring
                sage: matrix(h2)
                [ 0  0  0]
                [ 0  1  0]
                [ 0  0 -1]
                sage: L = lie_algebras.so(QQ['z'], 5, representation='matrix')
                sage: matrix(L.an_element())
                [ 1  1  0  0  0]
                [ 1  1  0  0  2]
                [ 0  0 -1 -1  0]
                [ 0  0 -1 -1 -1]
                [ 0  1  0 -2  0]

                sage: gl2 = lie_algebras.gl(QQ, 2)
                sage: matrix(gl2.an_element())
                [1 1]
                [1 1]
            """
