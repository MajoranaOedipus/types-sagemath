from _typeshed import Incomplete
from sage.categories.functor import Functor as Functor, IdentityFunctor_generic as IdentityFunctor_generic
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from typing import Self

class ConstructionFunctor(Functor):
    """
    Base class for construction functors.

    A construction functor is a functorial algebraic construction,
    such as the construction of a matrix ring over a given ring
    or the fraction field of a given ring.

    In addition to the class :class:`~sage.categories.functor.Functor`,
    construction functors provide rules for combining and merging
    constructions. This is an important part of Sage's coercion model,
    namely the pushout of two constructions: When a polynomial ``p`` in
    a variable ``x`` with integer coefficients is added to a rational
    number ``q``, then Sage finds that the parents ``ZZ['x']`` and
    ``QQ`` are obtained from ``ZZ`` by applying a polynomial ring
    construction respectively the fraction field construction. Each
    construction functor has an attribute ``rank``, and the rank of
    the polynomial ring construction is higher than the rank of the
    fraction field construction. This means that the pushout of ``QQ``
    and ``ZZ['x']``, and thus a common parent in which ``p`` and ``q``
    can be added, is ``QQ['x']``, since the construction functor with
    a lower rank is applied first.

    ::

        sage: F1, R = QQ.construction()
        sage: F1
        FractionField
        sage: R
        Integer Ring
        sage: F2, R = (ZZ['x']).construction()
        sage: F2
        Poly[x]
        sage: R
        Integer Ring
        sage: F3 = F2.pushout(F1)
        sage: F3
        Poly[x](FractionField(...))
        sage: F3(R)
        Univariate Polynomial Ring in x over Rational Field
        sage: from sage.categories.pushout import pushout
        sage: P.<x> = ZZ[]
        sage: pushout(QQ,P)
        Univariate Polynomial Ring in x over Rational Field
        sage: ((x+1) + 1/2).parent()
        Univariate Polynomial Ring in x over Rational Field

    When composing two construction functors, they are sometimes
    merged into one, as is the case in the Quotient construction::

        sage: Q15, R = (ZZ.quo(15*ZZ)).construction()
        sage: Q15
        QuotientFunctor
        sage: Q35, R = (ZZ.quo(35*ZZ)).construction()
        sage: Q35
        QuotientFunctor
        sage: Q15.merge(Q35)
        QuotientFunctor
        sage: Q15.merge(Q35)(ZZ)
        Ring of integers modulo 5

    Functors can not only be applied to objects, but also to morphisms in the
    respective categories. For example::

        sage: P.<x,y> = ZZ[]
        sage: F = P.construction()[0]; F
        MPoly[x,y]
        sage: A.<a,b> = GF(5)[]
        sage: f = A.hom([a + b, a - b], A)
        sage: F(A)
        Multivariate Polynomial Ring in x, y
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5
        sage: F(f)
        Ring endomorphism of Multivariate Polynomial Ring in x, y
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5
          Defn: Induced from base ring by
                Ring endomorphism of Multivariate Polynomial Ring in a, b
                 over Finite Field of size 5
                  Defn: a |--> a + b
                        b |--> a - b
        sage: F(f)(F(A)(x)*a)
        (a + b)*x
    """
    def __mul__(self, other):
        """
        Compose ``self`` and ``other`` to a composite construction
        functor, unless one of them is the identity.

        .. NOTE::

            The product is in functorial notation, i.e., when applying the
            product to an object, the second factor is applied first.

        TESTS::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: F*P
            FractionField(Poly[t](...))
            sage: P*F
            Poly[t](FractionField(...))
            sage: (F*P)(ZZ)
            Fraction Field of Univariate Polynomial Ring in t over Integer Ring
            sage: I*P is P
            True
            sage: F*I is F
            True
        """
    def pushout(self, other):
        """
        Composition of two construction functors, ordered by their ranks.

        .. NOTE::

            - This method seems not to be used in the coercion model.

            - By default, the functor with smaller rank is applied first.

        TESTS::

            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: F.pushout(P)
            Poly[t](FractionField(...))
            sage: P.pushout(F)
            Poly[t](FractionField(...))
        """
    def __eq__(self, other):
        """
        Equality here means that they are mathematically equivalent, though they may have
        specific implementation data. This method will usually be overloaded in subclasses.
        by default, only the types of the functors are compared. Also see the :meth:`merge` function.

        TESTS::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: I == F        # indirect doctest
            False
            sage: I == I        # indirect doctest
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: I != F        # indirect doctest
            True
            sage: I != I        # indirect doctest
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: F = QQ.construction()[0]
            sage: hash(I) == hash(F)
            False
            sage: hash(I) == hash(I)
            True
        """
    def merge(self, other) -> Self | None:
        """
        Merge ``self`` with another construction functor, or return ``None``.

        .. NOTE::

            The default is to merge only if the two functors coincide. But this
            may be overloaded for subclasses, such as the quotient functor.

        EXAMPLES::

            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: F.merge(F)
            FractionField
            sage: F.merge(P)
            sage: P.merge(F)
            sage: P.merge(P)
            Poly[t]
        """
    def commutes(self, other):
        """
        Determine whether ``self`` commutes with another construction functor.

        .. NOTE::

            By default, ``False`` is returned in all cases (even if the two
            functors are the same, since in this case :meth:`merge` will apply
            anyway). So far there is no construction functor that overloads
            this method. Anyway, this method only becomes relevant if two
            construction functors have the same rank.

        EXAMPLES::

            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: F.commutes(P)
            False
            sage: P.commutes(F)
            False
            sage: F.commutes(F)
            False
        """
    def expand(self):
        """
        Decompose ``self`` into a list of construction functors.

        .. NOTE::

            The default is to return the list only containing ``self``.

        EXAMPLES::

            sage: F = QQ.construction()[0]
            sage: F.expand()
            [FractionField]
            sage: Q = ZZ.quo(2).construction()[0]
            sage: Q.expand()
            [QuotientFunctor]
            sage: P = ZZ['t'].construction()[0]
            sage: FP = F*P
            sage: FP.expand()
            [FractionField, Poly[t]]
        """
    coercion_reversed: bool
    def common_base(self, other_functor, self_bases, other_bases) -> None:
        '''
        This function is called by :func:`pushout` when no common parent
        is found in the construction tower.

        .. NOTE::

            The main use is for multivariate construction functors,
            which use this function to implement recursion for
            :func:`pushout`.

        INPUT:

        - ``other_functor`` -- a construction functor

        - ``self_bases`` -- the arguments passed to this functor

        - ``other_bases`` -- the arguments passed to the functor
          ``other_functor``

        OUTPUT:

        Nothing, since a
        :class:`~sage.structure.coerce_exceptions.CoercionException`
        is raised.

        .. NOTE::

            Overload this function in derived class, see
            e.e. :class:`MultivariateConstructionFunctor`.

        TESTS::

            sage: from sage.categories.pushout import pushout
            sage: pushout(QQ, cartesian_product([ZZ]))  # indirect doctest
            Traceback (most recent call last):
            ...
            CoercionException: No common base ("join") found for
            FractionField(Integer Ring) and The cartesian_product functorial construction(Integer Ring).
        '''

class CompositeConstructionFunctor(ConstructionFunctor):
    """
    A Construction Functor composed by other Construction Functors.

    INPUT:

    - ``F1, F2,...`` -- a list of Construction Functors. The result is the
      composition ``F1`` followed by ``F2`` followed by ...

    EXAMPLES::

        sage: from sage.categories.pushout import CompositeConstructionFunctor
        sage: F = CompositeConstructionFunctor(QQ.construction()[0], ZZ['x'].construction()[0],
        ....:                                  QQ.construction()[0], ZZ['y'].construction()[0])
        sage: F
        Poly[y](FractionField(Poly[x](FractionField(...))))
        sage: F == loads(dumps(F))
        True
        sage: F == CompositeConstructionFunctor(*F.all)
        True
        sage: F(GF(2)['t'])                                                             # needs sage.libs.ntl
        Univariate Polynomial Ring in y
         over Fraction Field of Univariate Polynomial Ring in x
          over Fraction Field of Univariate Polynomial Ring in t
           over Finite Field of size 2 (using GF2X)
    """
    all: Incomplete
    def __init__(self, *args) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F = CompositeConstructionFunctor(QQ.construction()[0], ZZ['x'].construction()[0],
            ....:                                  QQ.construction()[0], ZZ['y'].construction()[0])
            sage: F
            Poly[y](FractionField(Poly[x](FractionField(...))))
            sage: F == CompositeConstructionFunctor(*F.all)
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F = CompositeConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0],QQ.construction()[0],ZZ['y'].construction()[0])
            sage: F == loads(dumps(F)) # indirect doctest
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F = CompositeConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0],QQ.construction()[0],ZZ['y'].construction()[0])
            sage: F != loads(dumps(F)) # indirect doctest
            False
        """
    __hash__: Incomplete
    def __mul__(self, other):
        """
        Compose construction functors to a composite construction functor, unless one of them is the identity.

        .. NOTE::

            The product is in functorial notation, i.e., when applying the product to an object
            then the second factor is applied first.

        EXAMPLES::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F1 = CompositeConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0])
            sage: F2 = CompositeConstructionFunctor(QQ.construction()[0],ZZ['y'].construction()[0])
            sage: F1*F2
            Poly[x](FractionField(Poly[y](FractionField(...))))
        """
    def expand(self):
        """
        Return expansion of a CompositeConstructionFunctor.

        .. NOTE::

            The product over the list of components, as returned by
            the ``expand()`` method, is equal to ``self``.

        EXAMPLES::

            sage: from sage.categories.pushout import CompositeConstructionFunctor
            sage: F = CompositeConstructionFunctor(QQ.construction()[0],
            ....:                                  ZZ['x'].construction()[0],
            ....:                                  QQ.construction()[0],
            ....:                                  ZZ['y'].construction()[0])
            sage: F
            Poly[y](FractionField(Poly[x](FractionField(...))))
            sage: prod(F.expand()) == F
            True
        """

class IdentityConstructionFunctor(ConstructionFunctor):
    """
    A construction functor that is the identity functor.

    TESTS::

        sage: from sage.categories.pushout import IdentityConstructionFunctor
        sage: I = IdentityConstructionFunctor()
        sage: I(RR) is RR
        True
        sage: I == loads(dumps(I))
        True
    """
    rank: int
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: IdentityFunctor(Sets()) == I
            True
            sage: I(RR) is RR
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: I == IdentityFunctor(Sets())     # indirect doctest
            True
            sage: I == QQ.construction()[0]
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: I != IdentityFunctor(Sets())     # indirect doctest
            False
            sage: I != QQ.construction()[0]
            True
        """
    __hash__: Incomplete
    def __mul__(self, other):
        """
        Compose construction functors to a composite construction functor, unless one of them is the identity.

        .. NOTE::

            The product is in functorial notation, i.e., when applying the
            product to an object then the second factor is applied first.

        TESTS::

            sage: from sage.categories.pushout import IdentityConstructionFunctor
            sage: I = IdentityConstructionFunctor()
            sage: F = QQ.construction()[0]
            sage: P = ZZ['t'].construction()[0]
            sage: I*F is F     # indirect doctest
            True
            sage: F*I is F
            True
            sage: I*P is P
            True
            sage: P*I is P
            True
        """

class MultivariateConstructionFunctor(ConstructionFunctor):
    """
    An abstract base class for functors that take
    multiple inputs (e.g. Cartesian products).

    TESTS::

        sage: from sage.categories.pushout import pushout
        sage: A = cartesian_product((QQ['z'], QQ))
        sage: B = cartesian_product((ZZ['t']['z'], QQ))
        sage: pushout(A, B)
        The Cartesian product of (Univariate Polynomial Ring in z over
        Univariate Polynomial Ring in t over Rational Field,
        Rational Field)
        sage: A.construction()
        (The cartesian_product functorial construction,
         (Univariate Polynomial Ring in z over Rational Field, Rational Field))
        sage: pushout(A, B)
        The Cartesian product of (Univariate Polynomial Ring in z over Univariate Polynomial Ring in t over Rational Field, Rational Field)
    """
    def common_base(self, other_functor, self_bases, other_bases):
        '''
        This function is called by :func:`pushout` when no common parent
        is found in the construction tower.

        INPUT:

        - ``other_functor`` -- a construction functor

        - ``self_bases`` -- the arguments passed to this functor

        - ``other_bases`` -- the arguments passed to the functor
          ``other_functor``

        OUTPUT: a parent

        If no common base is found a :class:`sage.structure.coerce_exceptions.CoercionException`
        is raised.

        .. NOTE::

            Overload this function in derived class, see
            e.g. :class:`MultivariateConstructionFunctor`.

        TESTS::

            sage: from sage.categories.pushout import pushout
            sage: pushout(cartesian_product([ZZ]), QQ)  # indirect doctest
            Traceback (most recent call last):
            ...
            CoercionException: No common base ("join") found for
            The cartesian_product functorial construction(Integer Ring) and FractionField(Integer Ring):
            (Multivariate) functors are incompatible.
            sage: pushout(cartesian_product([ZZ]), cartesian_product([ZZ, QQ]))  # indirect doctest
            Traceback (most recent call last):
            ...
            CoercionException: No common base ("join") found ...
        '''

class PolynomialFunctor(ConstructionFunctor):
    """
    Construction functor for univariate polynomial rings.

    EXAMPLES::

        sage: P = ZZ['t'].construction()[0]
        sage: P(GF(3))
        Univariate Polynomial Ring in t over Finite Field of size 3
        sage: P == loads(dumps(P))
        True
        sage: R.<x,y> = GF(5)[]
        sage: f = R.hom([x + 2*y, 3*x - y], R)
        sage: P(f)((x+y) * P(R).0)
        (-x + y)*t

    By :issue:`9944`, the construction functor distinguishes sparse and
    dense polynomial rings. Before, the following example failed::

        sage: R.<x> = PolynomialRing(GF(5), sparse=True)
        sage: F, B = R.construction()
        sage: F(B) is R
        True
        sage: S.<x> = PolynomialRing(ZZ)
        sage: R.has_coerce_map_from(S)
        False
        sage: S.has_coerce_map_from(R)
        False
        sage: S.0 + R.0
        2*x
        sage: (S.0 + R.0).parent()
        Univariate Polynomial Ring in x over Finite Field of size 5
        sage: (S.0 + R.0).parent().is_sparse()
        False
    """
    rank: int
    var: Incomplete
    multi_variate: Incomplete
    sparse: Incomplete
    implementation: Incomplete
    def __init__(self, var, multi_variate: bool = False, sparse: bool = False, implementation=None) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import PolynomialFunctor
            sage: P = PolynomialFunctor('x')
            sage: P(GF(3))
            Univariate Polynomial Ring in x over Finite Field of size 3

        There is an optional parameter ``multi_variate``, but
        apparently it is not used::

            sage: Q = PolynomialFunctor('x',multi_variate=True)
            sage: Q(ZZ)
            Univariate Polynomial Ring in x over Integer Ring
            sage: Q == P
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.categories.pushout import MultiPolynomialFunctor
            sage: Q = MultiPolynomialFunctor(('x',),'lex')
            sage: P = ZZ['x'].construction()[0]
            sage: P
            Poly[x]
            sage: Q
            MPoly[x]
            sage: P == Q
            True
            sage: P == loads(dumps(P))
            True
            sage: P == QQ.construction()[0]
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import MultiPolynomialFunctor
            sage: Q = MultiPolynomialFunctor(('x',),'lex')
            sage: P = ZZ['x'].construction()[0]
            sage: P != Q
            False
            sage: P != loads(dumps(P))
            False
            sage: P != QQ.construction()[0]
            True
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        .. NOTE::

            Internally, the merging is delegated to the merging of
            multipolynomial construction functors. But in effect,
            this does the same as the default implementation, that
            returns ``None`` unless the to-be-merged functors coincide.

        EXAMPLES::

            sage: P = ZZ['x'].construction()[0]
            sage: Q = ZZ['y','x'].construction()[0]
            sage: P.merge(Q)
            sage: P.merge(P) is P
            True
        """

class MultiPolynomialFunctor(ConstructionFunctor):
    """
    A constructor for multivariate polynomial rings.

    EXAMPLES::

        sage: P.<x,y> = ZZ[]
        sage: F = P.construction()[0]; F
        MPoly[x,y]
        sage: A.<a,b> = GF(5)[]
        sage: F(A)
        Multivariate Polynomial Ring in x, y
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5
        sage: f = A.hom([a+b, a-b], A)
        sage: F(f)
        Ring endomorphism of Multivariate Polynomial Ring in x, y
         over Multivariate Polynomial Ring in a, b over Finite Field of size 5
          Defn: Induced from base ring by
                Ring endomorphism of Multivariate Polynomial Ring in a, b over Finite Field of size 5
                  Defn: a |--> a + b
                        b |--> a - b
        sage: F(f)(F(A)(x)*a)
        (a + b)*x
    """
    rank: int
    vars: Incomplete
    term_order: Incomplete
    def __init__(self, vars, term_order) -> None:
        """
        EXAMPLES::

            sage: F = sage.categories.pushout.MultiPolynomialFunctor(['x','y'], None)
            sage: F
            MPoly[x,y]
            sage: F(ZZ)
            Multivariate Polynomial Ring in x, y over Integer Ring
            sage: F(CC)                                                                 # needs sage.rings.real_mpfr
            Multivariate Polynomial Ring in x, y over Complex Field with 53 bits of precision
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: F = ZZ['x,y,z'].construction()[0]
            sage: G = QQ['x,y,z'].construction()[0]
            sage: F == G
            True
            sage: G == loads(dumps(G))
            True
            sage: G = ZZ['x,y'].construction()[0]
            sage: F == G
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F = ZZ['x,y,z'].construction()[0]
            sage: G = QQ['x,y,z'].construction()[0]
            sage: F != G
            False
            sage: G != loads(dumps(G))
            False
            sage: G = ZZ['x,y'].construction()[0]
            sage: F != G
            True
        """
    __hash__: Incomplete
    def __mul__(self, other):
        """
        If two MPoly functors are given in a row, form a single MPoly functor
        with all of the variables.

        EXAMPLES::

            sage: F = sage.categories.pushout.MultiPolynomialFunctor(['x','y'], None)
            sage: G = sage.categories.pushout.MultiPolynomialFunctor(['t'], None)
            sage: G*F
            MPoly[x,y,t]
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        EXAMPLES::

            sage: F = sage.categories.pushout.MultiPolynomialFunctor(['x','y'], None)
            sage: G = sage.categories.pushout.MultiPolynomialFunctor(['t'], None)
            sage: F.merge(G) is None
            True
            sage: F.merge(F)
            MPoly[x,y]
        """
    def expand(self):
        """
        Decompose ``self`` into a list of construction functors.

        EXAMPLES::

            sage: F = QQ['x,y,z,t'].construction()[0]; F
            MPoly[x,y,z,t]
            sage: F.expand()
            [MPoly[t], MPoly[z], MPoly[y], MPoly[x]]

        Now an actual use case::

            sage: R.<x,y,z> = ZZ[]
            sage: S.<z,t> = QQ[]
            sage: x+t
            x + t
            sage: parent(x+t)
            Multivariate Polynomial Ring in x, y, z, t over Rational Field
            sage: T.<y,s> = QQ[]
            sage: x + s
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Multivariate Polynomial Ring in x, y, z over Integer Ring' and
            'Multivariate Polynomial Ring in y, s over Rational Field'
            sage: R = PolynomialRing(ZZ, 'x', 50)
            sage: S = PolynomialRing(GF(5), 'x', 20)
            sage: R.gen(0) + S.gen(0)
            2*x0
        """

class InfinitePolynomialFunctor(ConstructionFunctor):
    '''
    A Construction Functor for Infinite Polynomial Rings (see :mod:`~sage.rings.polynomial.infinite_polynomial_ring`).

    AUTHOR:

    -- Simon King

    This construction functor is used to provide uniqueness of infinite polynomial rings as parent structures.
    As usual, the construction functor allows for constructing pushouts.

    Another purpose is to avoid name conflicts of variables of the to-be-constructed infinite polynomial ring with
    variables of the base ring, and moreover to keep the internal structure of an Infinite Polynomial Ring as simple
    as possible: If variables `v_1,...,v_n` of the given base ring generate an *ordered* sub-monoid of the monomials
    of the ambient Infinite Polynomial Ring, then they are removed from the base ring and merged with the generators
    of the ambient ring. However, if the orders don\'t match, an error is raised, since there was a name conflict
    without merging.

    EXAMPLES::

        sage: A.<a,b> = InfinitePolynomialRing(ZZ[\'t\'])
        sage: A.construction()
        [InfPoly{[a,b], "lex", "dense"},
         Univariate Polynomial Ring in t over Integer Ring]
        sage: type(_[0])
        <class \'sage.categories.pushout.InfinitePolynomialFunctor\'>
        sage: B.<x,y,a_3,a_1> = PolynomialRing(QQ, order=\'lex\')
        sage: B.construction()
        (MPoly[x,y,a_3,a_1], Rational Field)
        sage: A.construction()[0] * B.construction()[0]
        InfPoly{[a,b], "lex", "dense"}(MPoly[x,y](...))

    Apparently the variables `a_1,a_3` of the polynomial ring are merged with the variables
    `a_0, a_1, a_2, ...` of the infinite polynomial ring; indeed, they form an ordered sub-structure.
    However, if the polynomial ring was given a different ordering, merging would not be allowed,
    resulting in a name conflict::

        sage: R = PolynomialRing(QQ, names=[\'x\',\'y\',\'a_3\',\'a_1\'])
        sage: A.construction()[0] * R.construction()[0]
        Traceback (most recent call last):
        ...
        CoercionException: Incompatible term orders lex, degrevlex

    In an infinite polynomial ring with generator `a_\\ast`, the variable `a_3` will always be greater
    than the variable `a_1`. Hence, the orders are incompatible in the next example as well::

        sage: R = PolynomialRing(QQ, names=[\'x\',\'y\',\'a_1\',\'a_3\'], order=\'lex\')
        sage: A.construction()[0] * R.construction()[0]
        Traceback (most recent call last):
        ...
        CoercionException: Overlapping variables ((\'a\', \'b\'),[\'a_1\', \'a_3\'])
        are incompatible

    Another requirement is that after merging the order of the remaining variables must be unique.
    This is not the case in the following example, since it is not clear whether the variables `x,y`
    should be greater or smaller than the variables `b_\\ast`::

        sage: R = PolynomialRing(QQ, names=[\'a_3\',\'a_1\',\'x\',\'y\'], order=\'lex\')
        sage: A.construction()[0] * R.construction()[0]
        Traceback (most recent call last):
        ...
        CoercionException: Overlapping variables ((\'a\', \'b\'),[\'a_3\', \'a_1\'])
        are incompatible

    Since the construction functors are actually used to construct infinite polynomial rings, the following
    result is no surprise::

        sage: C.<a,b> = InfinitePolynomialRing(B); C
        Infinite polynomial ring in a, b
         over Multivariate Polynomial Ring in x, y over Rational Field

    There is also an overlap in the next example::

        sage: X.<w,x,y> = InfinitePolynomialRing(ZZ)
        sage: Y.<x,y,z> = InfinitePolynomialRing(QQ)

    `X` and `Y` have an overlapping generators `x_\\ast, y_\\ast`. Since the default lexicographic order is
    used in both rings, it gives rise to isomorphic sub-monoids in both `X` and `Y`. They are merged in the
    pushout, which also yields a common parent for doing arithmetic::

        sage: P = sage.categories.pushout.pushout(Y,X); P
        Infinite polynomial ring in w, x, y, z over Rational Field
        sage: w[2]+z[3]
        w_2 + z_3
        sage: _.parent() is P
        True
    '''
    rank: float
    def __init__(self, gens, order, implementation) -> None:
        '''
        TESTS::

            sage: F = sage.categories.pushout.InfinitePolynomialFunctor([\'a\',\'b\',\'x\'],\'degrevlex\',\'sparse\'); F # indirect doctest
            InfPoly{[a,b,x], "degrevlex", "sparse"}
            sage: F == loads(dumps(F))
            True
        '''
    def __eq__(self, other):
        '''
        TESTS::

            sage: F = sage.categories.pushout.InfinitePolynomialFunctor([\'a\',\'b\',\'x\'],\'degrevlex\',\'sparse\'); F # indirect doctest
            InfPoly{[a,b,x], "degrevlex", "sparse"}
            sage: F == loads(dumps(F)) # indirect doctest
            True
            sage: F == sage.categories.pushout.InfinitePolynomialFunctor([\'a\',\'b\',\'x\'],\'deglex\',\'sparse\')
            False
        '''
    def __ne__(self, other):
        '''
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F = sage.categories.pushout.InfinitePolynomialFunctor([\'a\',\'b\',\'x\'],\'degrevlex\',\'sparse\'); F # indirect doctest
            InfPoly{[a,b,x], "degrevlex", "sparse"}
            sage: F != loads(dumps(F)) # indirect doctest
            False
            sage: F != sage.categories.pushout.InfinitePolynomialFunctor([\'a\',\'b\',\'x\'],\'deglex\',\'sparse\')
            True
        '''
    __hash__: Incomplete
    def __mul__(self, other):
        '''
        Compose construction functors to a composite construction functor, unless one of them is the identity.

        .. NOTE::

            The product is in functorial notation, i.e., when applying the
            product to an object then the second factor is applied first.

        TESTS::

            sage: F1 = QQ[\'a\',\'x_2\',\'x_1\',\'y_3\',\'y_2\'].construction()[0]; F1
            MPoly[a,x_2,x_1,y_3,y_2]
            sage: F2 = InfinitePolynomialRing(QQ, [\'x\',\'y\'],order=\'degrevlex\').construction()[0]; F2
            InfPoly{[x,y], "degrevlex", "dense"}
            sage: F3 = InfinitePolynomialRing(QQ, [\'x\',\'y\'],order=\'degrevlex\',implementation=\'sparse\').construction()[0]; F3
            InfPoly{[x,y], "degrevlex", "sparse"}
            sage: F2*F1
            InfPoly{[x,y], "degrevlex", "dense"}(Poly[a](...))
            sage: F3*F1
            InfPoly{[x,y], "degrevlex", "sparse"}(Poly[a](...))
            sage: F4 = sage.categories.pushout.FractionField()
            sage: F2*F4
            InfPoly{[x,y], "degrevlex", "dense"}(FractionField(...))
        '''
    def merge(self, other):
        '''
        Merge two construction functors of infinite polynomial rings, regardless of monomial order and implementation.

        The purpose is to have a pushout (and thus, arithmetic) even in cases when the parents are isomorphic as
        rings, but not as ordered rings.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ, implementation=\'sparse\')
            sage: Y.<x,y> = InfinitePolynomialRing(QQ, order=\'degrevlex\')
            sage: X.construction()
            [InfPoly{[x,y], "lex", "sparse"}, Rational Field]
            sage: Y.construction()
            [InfPoly{[x,y], "degrevlex", "dense"}, Rational Field]
            sage: Y.construction()[0].merge(Y.construction()[0])
            InfPoly{[x,y], "degrevlex", "dense"}
            sage: y[3] + X(x[2])
            x_2 + y_3
            sage: _.parent().construction()
            [InfPoly{[x,y], "degrevlex", "dense"}, Rational Field]
        '''
    def expand(self):
        '''
        Decompose the functor `F` into sub-functors, whose product returns `F`.

        EXAMPLES::

            sage: A = InfinitePolynomialRing(QQ, [\'x\',\'y\'], order=\'degrevlex\')
            sage: F = A.construction()[0]; F
            InfPoly{[x,y], "degrevlex", "dense"}
            sage: F.expand()
            [InfPoly{[y], "degrevlex", "dense"}, InfPoly{[x], "degrevlex", "dense"}]
            sage: A = InfinitePolynomialRing(QQ, [\'x\',\'y\',\'z\'], order=\'degrevlex\')
            sage: F = A.construction()[0]; F
            InfPoly{[x,y,z], "degrevlex", "dense"}
            sage: F.expand()
            [InfPoly{[z], "degrevlex", "dense"},
             InfPoly{[y], "degrevlex", "dense"},
             InfPoly{[x], "degrevlex", "dense"}]
            sage: prod(F.expand())==F
            True
        '''

class MatrixFunctor(ConstructionFunctor):
    """
    A construction functor for matrices over rings.

    EXAMPLES::

        sage: # needs sage.modules
        sage: MS = MatrixSpace(ZZ, 2, 3)
        sage: F = MS.construction()[0]; F
        MatrixFunctor
        sage: MS = MatrixSpace(ZZ, 2)
        sage: F = MS.construction()[0]; F
        MatrixFunctor
        sage: P.<x,y> = QQ[]
        sage: R = F(P); R
        Full MatrixSpace of 2 by 2 dense matrices
         over Multivariate Polynomial Ring in x, y over Rational Field
        sage: f = P.hom([x+y, x-y], P); F(f)
        Ring endomorphism
         of Full MatrixSpace of 2 by 2 dense matrices
          over Multivariate Polynomial Ring in x, y over Rational Field
          Defn: Induced from base ring by
                Ring endomorphism
                 of Multivariate Polynomial Ring in x, y over Rational Field
                  Defn: x |--> x + y
                        y |--> x - y
        sage: M = R([x, y, x*y, x + y])
        sage: F(f)(M)
        [    x + y     x - y]
        [x^2 - y^2       2*x]
    """
    rank: int
    nrows: Incomplete
    ncols: Incomplete
    is_sparse: Incomplete
    def __init__(self, nrows, ncols, is_sparse: bool = False) -> None:
        """
        TESTS::

            sage: # needs sage.modules
            sage: from sage.categories.pushout import MatrixFunctor
            sage: F = MatrixFunctor(2, 3)
            sage: F == MatrixSpace(ZZ, 2, 3).construction()[0]
            True
            sage: F.codomain()
            Category of commutative additive groups
            sage: R = MatrixSpace(ZZ, 2, 2).construction()[0]
            sage: R.codomain()
            Category of rings
            sage: F(ZZ)
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
            sage: F(ZZ) in F.codomain()
            True
            sage: R(GF(2))
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 2
            sage: R(GF(2)) in R.codomain()
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: F = MatrixSpace(ZZ, 2, 3).construction()[0]                           # needs sage.modules
            sage: F == loads(dumps(F))                                                  # needs sage.modules
            True
            sage: F == MatrixSpace(ZZ, 2, 2).construction()[0]                          # needs sage.modules
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F = MatrixSpace(ZZ, 2, 3).construction()[0]                           # needs sage.modules
            sage: F != loads(dumps(F))                                                  # needs sage.modules
            False
            sage: F != MatrixSpace(ZZ, 2, 2).construction()[0]                          # needs sage.modules
            True
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Merging is only happening if both functors are matrix functors of the same dimension.

        The result is sparse if and only if both given functors are sparse.

        EXAMPLES::

            sage: # needs sage.modules
            sage: F1 = MatrixSpace(ZZ, 2, 2).construction()[0]
            sage: F2 = MatrixSpace(ZZ, 2, 3).construction()[0]
            sage: F3 = MatrixSpace(ZZ, 2, 2, sparse=True).construction()[0]
            sage: F1.merge(F2)
            sage: F1.merge(F3)
            MatrixFunctor
            sage: F13 = F1.merge(F3)
            sage: F13.is_sparse
            False
            sage: F1.is_sparse
            False
            sage: F3.is_sparse
            True
            sage: F3.merge(F3).is_sparse
            True
        """

class LaurentPolynomialFunctor(ConstructionFunctor):
    """
    Construction functor for Laurent polynomial rings.

    EXAMPLES::

        sage: L.<t> = LaurentPolynomialRing(ZZ)
        sage: F = L.construction()[0]
        sage: F
        LaurentPolynomialFunctor
        sage: F(QQ)
        Univariate Laurent Polynomial Ring in t over Rational Field
        sage: K.<x> = LaurentPolynomialRing(ZZ)
        sage: F(K)
        Univariate Laurent Polynomial Ring in t
         over Univariate Laurent Polynomial Ring in x over Integer Ring
        sage: P.<x,y> = ZZ[]
        sage: f = P.hom([x + 2*y, 3*x - y],P)
        sage: F(f)
        Ring endomorphism of Univariate Laurent Polynomial Ring in t
         over Multivariate Polynomial Ring in x, y over Integer Ring
          Defn: Induced from base ring by
                Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
                  Defn: x |--> x + 2*y
                        y |--> 3*x - y
        sage: F(f)(x*F(P).gen()^-2 + y*F(P).gen()^3)
        (x + 2*y)*t^-2 + (3*x - y)*t^3
    """
    rank: int
    var: Incomplete
    multi_variate: Incomplete
    def __init__(self, var, multi_variate: bool = False) -> None:
        """
        INPUT:

        - ``var`` -- string or list of strings
        - ``multi_variate`` -- boolean (default: ``False``); if ``var`` is a
          string and ``True`` otherwise: If ``True``, application to a Laurent
          polynomial ring yields a multivariate Laurent polynomial ring.

        TESTS::

            sage: from sage.categories.pushout import LaurentPolynomialFunctor
            sage: F1 = LaurentPolynomialFunctor('t')
            sage: F2 = LaurentPolynomialFunctor('s', multi_variate=True)
            sage: F3 = LaurentPolynomialFunctor(['s','t'])
            sage: F1(F2(QQ))
            Univariate Laurent Polynomial Ring in t over
             Univariate Laurent Polynomial Ring in s over Rational Field
            sage: F2(F1(QQ))                                                            # needs sage.modules
            Multivariate Laurent Polynomial Ring in t, s over Rational Field
            sage: F3(QQ)                                                                # needs sage.modules
            Multivariate Laurent Polynomial Ring in s, t over Rational Field
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.categories.pushout import LaurentPolynomialFunctor
            sage: F1 = LaurentPolynomialFunctor('t')
            sage: F2 = LaurentPolynomialFunctor('t', multi_variate=True)
            sage: F3 = LaurentPolynomialFunctor(['s','t'])
            sage: F1 == F2
            True
            sage: F1 == loads(dumps(F1))
            True
            sage: F1 == F3
            False
            sage: F1 == QQ.construction()[0]
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import LaurentPolynomialFunctor
            sage: F1 = LaurentPolynomialFunctor('t')
            sage: F2 = LaurentPolynomialFunctor('t', multi_variate=True)
            sage: F3 = LaurentPolynomialFunctor(['s','t'])
            sage: F1 != F2
            False
            sage: F1 != loads(dumps(F1))
            False
            sage: F1 != F3
            True
            sage: F1 != QQ.construction()[0]
            True
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Two Laurent polynomial construction functors merge if the variable names coincide.

        The result is multivariate if one of the arguments is multivariate.

        EXAMPLES::

            sage: from sage.categories.pushout import LaurentPolynomialFunctor
            sage: F1 = LaurentPolynomialFunctor('t')
            sage: F2 = LaurentPolynomialFunctor('t', multi_variate=True)
            sage: F1.merge(F2)
            LaurentPolynomialFunctor
            sage: F1.merge(F2)(LaurentPolynomialRing(GF(2), 'a'))                       # needs sage.modules
            Multivariate Laurent Polynomial Ring in a, t over Finite Field of size 2
            sage: F1.merge(F1)(LaurentPolynomialRing(GF(2), 'a'))
            Univariate Laurent Polynomial Ring in t over
             Univariate Laurent Polynomial Ring in a over Finite Field of size 2
        """

class VectorFunctor(ConstructionFunctor):
    """
    A construction functor for free modules over commutative rings.

    EXAMPLES::

        sage: # needs sage.modules
        sage: F = (ZZ^3).construction()[0]
        sage: F
        VectorFunctor
        sage: F(GF(2)['t'])                                                             # needs sage.libs.ntl
        Ambient free module of rank 3
         over the principal ideal domain Univariate Polynomial Ring in t
          over Finite Field of size 2 (using GF2X)
    """
    rank: int
    n: Incomplete
    is_sparse: Incomplete
    inner_product_matrix: Incomplete
    with_basis: Incomplete
    basis_keys: Incomplete
    name_mapping: Incomplete
    latex_name_mapping: Incomplete
    def __init__(self, n=None, is_sparse: bool = False, inner_product_matrix=None, *, with_basis: str = 'standard', basis_keys=None, name_mapping=None, latex_name_mapping=None) -> None:
        """
        INPUT:

        - ``n`` -- the rank of the to-be-created modules (nonnegative integer)
        - ``is_sparse`` -- boolean (default: ``False``); create sparse
          implementation of modules
        - ``inner_product_matrix`` -- ``n`` by ``n`` matrix, used to compute inner products in the
          to-be-created modules
        - ``name_mapping``, ``latex_name_mapping`` -- Dictionaries from base rings to names
        - other keywords: see :func:`~sage.modules.free_module.FreeModule`

        TESTS::

            sage: # needs sage.modules
            sage: from sage.categories.pushout import VectorFunctor
            sage: F1 = VectorFunctor(3, inner_product_matrix=Matrix(3, 3, range(9)))
            sage: F1.domain()
            Category of commutative rings
            sage: F1.codomain()
            Category of commutative additive groups
            sage: M1 = F1(ZZ)
            sage: M1.is_sparse()
            False
            sage: v = M1([3, 2, 1])
            sage: v * Matrix(3, 3, range(9)) * v.column()
            (96)
            sage: v.inner_product(v)
            96
            sage: F2 = VectorFunctor(3, is_sparse=True)
            sage: M2 = F2(QQ); M2; M2.is_sparse()
            Sparse vector space of dimension 3 over Rational Field
            True
        """
    def __eq__(self, other):
        """
        The rank and the inner product matrix are compared.

        TESTS::

            sage: # needs sage.modules
            sage: from sage.categories.pushout import VectorFunctor
            sage: F1 = VectorFunctor(3, inner_product_matrix=Matrix(3, 3, range(9)))
            sage: F2 = (ZZ^3).construction()[0]
            sage: F1 == F2
            False
            sage: F1(QQ) == F2(QQ)
            False
            sage: F1 == loads(dumps(F1))
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.categories.pushout import VectorFunctor
            sage: F1 = VectorFunctor(3, inner_product_matrix=Matrix(3, 3, range(9)))
            sage: F2 = (ZZ^3).construction()[0]
            sage: F1 != F2
            True
            sage: F1(QQ) != F2(QQ)
            True
            sage: F1 != loads(dumps(F1))
            False
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Two constructors of free modules merge, if the module ranks and the inner products coincide. If both
        have explicitly given inner product matrices, they must coincide as well.

        EXAMPLES:

        Two modules without explicitly given inner product allow coercion::

            sage: M1 = QQ^3                                                             # needs sage.modules
            sage: P.<t> = ZZ[]
            sage: M2 = FreeModule(P, 3)                                                 # needs sage.modules
            sage: M1([1,1/2,1/3]) + M2([t,t^2+t,3])     # indirect doctest              # needs sage.modules
            (t + 1, t^2 + t + 1/2, 10/3)

        If only one summand has an explicit inner product, the result will be provided
        with it::

            sage: M3 = FreeModule(P, 3, inner_product_matrix=Matrix(3, 3, range(9)))    # needs sage.modules
            sage: M1([1,1/2,1/3]) + M3([t,t^2+t,3])                                     # needs sage.modules
            (t + 1, t^2 + t + 1/2, 10/3)
            sage: (M1([1,1/2,1/3]) + M3([t,t^2+t,3])).parent().inner_product_matrix()   # needs sage.modules
            [0 1 2]
            [3 4 5]
            [6 7 8]

        If both summands have an explicit inner product (even if it is the standard
        inner product), then the products must coincide. The only difference between
        ``M1`` and ``M4`` in the following example is the fact that the default
        inner product was *explicitly* requested for ``M4``. It is therefore not
        possible to coerce with a different inner product::

            sage: # needs sage.modules
            sage: M4 = FreeModule(QQ, 3, inner_product_matrix=Matrix(3, 3, 1))
            sage: M4 == M1
            True
            sage: M4.inner_product_matrix() == M1.inner_product_matrix()
            True
            sage: M4([1,1/2,1/3]) + M3([t,t^2+t,3])      # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Ambient quadratic space of dimension 3 over Rational Field
            Inner product matrix:
            [1 0 0]
            [0 1 0]
            [0 0 1]' and
            'Ambient free quadratic module of rank 3 over the integral domain
            Univariate Polynomial Ring in t over Integer Ring
            Inner product matrix:
            [0 1 2]
            [3 4 5]
            [6 7 8]'

        Names are removed when they conflict::

            sage: # needs sage.modules
            sage: from sage.categories.pushout import VectorFunctor, pushout
            sage: M_ZZx = FreeModule(ZZ['x'], 4, with_basis=None, name='M_ZZx')
            sage: N_ZZx = FreeModule(ZZ['x'], 4, with_basis=None, name='N_ZZx')
            sage: pushout(M_ZZx, QQ)
            Rank-4 free module M_ZZx_base_ext
             over the Univariate Polynomial Ring in x over Rational Field
            sage: pushout(M_ZZx, N_ZZx)
            Rank-4 free module
             over the Univariate Polynomial Ring in x over Integer Ring
            sage: pushout(pushout(M_ZZx, N_ZZx), QQ)
            Rank-4 free module
             over the Univariate Polynomial Ring in x over Rational Field
        """

class SubspaceFunctor(ConstructionFunctor):
    """
    Constructing a subspace of an ambient free module, given by a basis.

    .. NOTE::

        This construction functor keeps track of the basis. It can only be
        applied to free modules into which this basis coerces.

    EXAMPLES::

        sage: # needs sage.modules
        sage: M = ZZ^3
        sage: S = M.submodule([(1,2,3), (4,5,6)]); S
        Free module of degree 3 and rank 2 over Integer Ring
        Echelon basis matrix:
        [1 2 3]
        [0 3 6]
        sage: F = S.construction()[0]
        sage: F(GF(2)^3)
        Vector space of degree 3 and dimension 2 over Finite Field of size 2
        User basis matrix:
        [1 0 1]
        [0 1 0]
    """
    rank: int
    coercion_reversed: bool
    basis: Incomplete
    def __init__(self, basis) -> None:
        """
        INPUT:

        - ``basis`` -- list of elements of a free module

        TESTS::

            sage: from sage.categories.pushout import SubspaceFunctor
            sage: M = ZZ^3                                                              # needs sage.modules
            sage: F = SubspaceFunctor([M([1,2,3]), M([4,5,6])])                         # needs sage.modules
            sage: F(GF(5)^3)                                                            # needs sage.modules
            Vector space of degree 3 and dimension 2 over Finite Field of size 5
            User basis matrix:
            [1 2 3]
            [4 0 1]
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: # needs sage.modules
            sage: F1 = (GF(5)^3).span([(1,2,3),(4,5,6)]).construction()[0]
            sage: F2 = (ZZ^3).span([(1,2,3),(4,5,6)]).construction()[0]
            sage: F3 = (QQ^3).span([(1,2,3),(4,5,6)]).construction()[0]
            sage: F4 = (ZZ^3).span([(1,0,-1),(0,1,2)]).construction()[0]
            sage: F1 == loads(dumps(F1))
            True

        The ``span`` method automatically transforms the given basis into
        echelon form. The bases look like that::

            sage: # needs sage.modules
            sage: F1.basis
            [(1, 0, 4), (0, 1, 2)]
            sage: F2.basis
            [(1, 2, 3), (0, 3, 6)]
            sage: F3.basis
            [(1, 0, -1), (0, 1, 2)]
            sage: F4.basis
            [(1, 0, -1), (0, 1, 2)]


        The basis of ``F2`` is modulo 5 different from the other bases.
        So, we have::

            sage: F1 != F2 != F3                                                        # needs sage.modules
            True

        The bases of ``F1``, ``F3`` and ``F4`` are the same modulo 5; however,
        there is no coercion from ``QQ^3`` to ``GF(5)^3``. Therefore, we have::

            sage: F1 == F3                                                              # needs sage.modules
            False

        But there are coercions from ``ZZ^3`` to ``QQ^3`` and ``GF(5)^3``, thus::

            sage: F1 == F4 == F3                                                        # needs sage.modules
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: F1 = (GF(5)^3).span([(1,2,3),(4,5,6)]).construction()[0]              # needs sage.modules
            sage: F1 != loads(dumps(F1))                                                # needs sage.modules
            False
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Two Subspace Functors are merged into a construction functor of the sum of two subspaces.

        EXAMPLES::

            sage: # needs sage.modules
            sage: M = GF(5)^3
            sage: S1 = M.submodule([(1,2,3),(4,5,6)])
            sage: S2 = M.submodule([(2,2,3)])
            sage: F1 = S1.construction()[0]
            sage: F2 = S2.construction()[0]
            sage: F1.merge(F2)
            SubspaceFunctor
            sage: F1.merge(F2)(GF(5)^3) == S1 + S2
            True
            sage: F1.merge(F2)(GF(5)['t']^3)
            Free module of degree 3 and rank 3
             over Univariate Polynomial Ring in t over Finite Field of size 5
            User basis matrix:
            [1 0 0]
            [0 1 0]
            [0 0 1]

        TESTS::

            sage: # needs sage.modules
            sage: P.<t> = ZZ[]
            sage: S1 = (ZZ^3).submodule([(1,2,3), (4,5,6)])
            sage: S2 = (Frac(P)^3).submodule([(t,t^2,t^3+1), (4*t,0,1)])
            sage: v = S1([0,3,6]) + S2([2,0,1/(2*t)]); v   # indirect doctest
            (2, 3, (-12*t - 1)/(-2*t))
            sage: v.parent()
            Vector space of degree 3 and dimension 3
             over Fraction Field of Univariate Polynomial Ring in t over Integer Ring
            User basis matrix:
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """

class FractionField(ConstructionFunctor):
    """
    Construction functor for fraction fields.

    EXAMPLES::

        sage: F = QQ.construction()[0]
        sage: F
        FractionField
        sage: F.domain()
        Category of integral domains
        sage: F.codomain()
        Category of fields
        sage: F(GF(5)) is GF(5)
        True
        sage: F(ZZ['t'])
        Fraction Field of Univariate Polynomial Ring in t over Integer Ring
        sage: P.<x,y> = QQ[]
        sage: f = P.hom([x+2*y,3*x-y],P)
        sage: F(f)
        Ring endomorphism of
         Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
          Defn: x |--> x + 2*y
                y |--> 3*x - y
        sage: F(f)(1/x)
        1/(x + 2*y)
        sage: F == loads(dumps(F))
        True
    """
    rank: int
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import FractionField
            sage: F = FractionField()
            sage: F
            FractionField
            sage: F(ZZ['t'])
            Fraction Field of Univariate Polynomial Ring in t over Integer Ring
        """

class CompletionFunctor(ConstructionFunctor):
    """
    Completion of a ring with respect to a given prime (including infinity).

    EXAMPLES::

        sage: # needs sage.rings.padics
        sage: R = Zp(5)
        sage: R
        5-adic Ring with capped relative precision 20
        sage: F1 = R.construction()[0]
        sage: F1
        Completion[5, prec=20]
        sage: F1(ZZ) is R
        True
        sage: F1(QQ)
        5-adic Field with capped relative precision 20

        sage: F2 = RR.construction()[0]
        sage: F2
        Completion[+Infinity, prec=53]
        sage: F2(QQ) is RR
        True

        sage: P.<x> = ZZ[]
        sage: Px = P.completion(x) # currently the only implemented completion of P
        sage: Px
        Power Series Ring in x over Integer Ring
        sage: F3 = Px.construction()[0]
        sage: F3(GF(3)['x'])
        Power Series Ring in x over Finite Field of size 3

    TESTS::

        sage: # needs sage.rings.padics
        sage: R1.<a> = Zp(5, prec=20)[]
        sage: R2 = Qp(5, prec=40)
        sage: R2(1) + a
        (1 + O(5^20))*a + 1 + O(5^40)
        sage: 1/2 + a
        (1 + O(5^20))*a + 3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + 2*5^10 + 2*5^11 + 2*5^12 + 2*5^13 + 2*5^14 + 2*5^15 + 2*5^16 + 2*5^17 + 2*5^18 + 2*5^19 + O(5^20)
    """
    rank: int
    p: Incomplete
    prec: Incomplete
    extras: Incomplete
    type: Incomplete
    def __init__(self, p, prec, extras=None) -> None:
        """
        INPUT:

        - ``p`` -- prime number, the generator of a univariate polynomial ring,
          or ``+Infinity``

        - ``prec`` -- integer; yielding the precision in bits. Note that
          if ``p`` is prime then the ``prec`` is the *capped* precision,
          while it is the *set* precision if ``p`` is ``+Infinity``.
          In the ``lattice-cap`` precision case, ``prec`` will be a tuple instead.

        - ``extras`` -- dictionary (optional); information on how to print elements, etc.
          If 'type' is given as a key, the corresponding value should be a string among
          the following:

          - 'RDF', 'Interval', 'RLF', or 'RR' for completions at infinity

          - 'capped-rel', 'capped-abs', 'fixed-mod', 'lattice-cap' or 'lattice-float'
            for completions at a finite place or ideal of a DVR.

        TESTS::

            sage: from sage.categories.pushout import CompletionFunctor
            sage: F1 = CompletionFunctor(5, 100)
            sage: F1(QQ)                                                                # needs sage.rings.padics
            5-adic Field with capped relative precision 100
            sage: F1(ZZ)                                                                # needs sage.rings.padics
            5-adic Ring with capped relative precision 100
            sage: F1.type is None
            True
            sage: sorted(F1.extras.items())
            []
            sage: F2 = RR.construction()[0]
            sage: F2
            Completion[+Infinity, prec=53]
            sage: F2.type                                                               # needs sage.rings.real_mpfr
            'MPFR'
            sage: F2.extras                                                             # needs sage.rings.real_mpfr
            {'rnd': 0, 'sci_not': False}
        """
    def __eq__(self, other):
        """
        .. NOTE::

            Only the prime used in the completion is relevant to comparison
            of Completion functors, although the resulting rings also take
            the precision into account.

        TESTS::

            sage: # needs sage.rings.padics
            sage: R1 = Zp(5, prec=30)
            sage: R2 = Zp(5, prec=40)
            sage: F1 = R1.construction()[0]
            sage: F2 = R2.construction()[0]
            sage: F1 == loads(dumps(F1))    # indirect doctest
            True
            sage: F1 == F2
            True
            sage: F1(QQ) == F2(QQ)
            False
            sage: R3 = Zp(7)
            sage: F3 = R3.construction()[0]
            sage: F1 == F3
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: R1 = Zp(5, prec=30)
            sage: R2 = Zp(5, prec=40)
            sage: F1 = R1.construction()[0]
            sage: F2 = R2.construction()[0]
            sage: F1 != loads(dumps(F1))    # indirect doctest
            False
            sage: F1 != F2
            False
            sage: F1(QQ) != F2(QQ)
            True
            sage: R3 = Zp(7)
            sage: F3 = R3.construction()[0]
            sage: F1 != F3
            True
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Two Completion functors are merged, if they are equal. If the precisions of
        both functors coincide, then a Completion functor is returned that results
        from updating the ``extras`` dictionary of ``self`` by ``other.extras``.
        Otherwise, if the completion is at infinity then merging does not increase
        the set precision, and if the completion is at a finite prime, merging
        does not decrease the capped precision.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: R1.<a> = Zp(5, prec=20)[]
            sage: R2 = Qp(5, prec=40)
            sage: R2(1) + a       # indirect doctest
            (1 + O(5^20))*a + 1 + O(5^40)
            sage: R3 = RealField(30)
            sage: R4 = RealField(50)
            sage: R3(1) + R4(1)   # indirect doctest
            2.0000000
            sage: (R3(1) + R4(1)).parent()
            Real Field with 30 bits of precision

        TESTS:

        We check that :issue:`12353` has been resolved::

            sage: RIF(1) > RR(1)                                                        # needs sage.rings.real_interval_field
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for >:
            'Real Interval Field with 53 bits of precision' and 'Real Field with 53 bits of precision'

        We check that various pushouts work::

            sage: # needs sage.rings.real_interval_field sage.rings.real_mpfr
            sage: R0 = RealIntervalField(30)
            sage: R1 = RealIntervalField(30, sci_not=True)
            sage: R2 = RealIntervalField(53)
            sage: R3 = RealIntervalField(53, sci_not=True)
            sage: R4 = RealIntervalField(90)
            sage: R5 = RealIntervalField(90, sci_not=True)
            sage: R6 = RealField(30)
            sage: R7 = RealField(30, sci_not=True)
            sage: R8 = RealField(53, rnd='RNDD')
            sage: R9 = RealField(53, sci_not=True, rnd='RNDZ')
            sage: R10 = RealField(53, sci_not=True)
            sage: R11 = RealField(90, sci_not=True, rnd='RNDZ')
            sage: Rlist = [R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11]
            sage: from sage.categories.pushout import pushout
            sage: pushouts = [R0,R0,R0,R1,R0,R1,R0,R1,R0,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R1,R0,R1,R2,R2,R2,R3,R0,R1,R2,R3,R3,R3,R1,R1,R3,R3,R3,R3,R1,R1,R3,R3,R3,R3,R0,R1,R2,R3,R4,R4,R0,R1,R2,R3,R3,R5,R1,R1,R3,R3,R5,R5,R1,R1,R3,R3,R3,R5,R0,R1,R0,R1,R0,R1,R6,R6,R6,R7,R7,R7,R1,R1,R1,R1,R1,R1,R7,R7,R7,R7,R7,R7,R0,R1,R2,R3,R2,R3,R6,R7,R8,R9,R10,R9,R1,R1,R3,R3,R3,R3,R7,R7,R9,R9,R10,R9,R1,R1,R3,R3,R3,R3,R7,R7,R10,R10,R10,R10,R1,R1,R3,R3,R5,R5,R7,R7,R9,R9,R10,R11]
            sage: all(R is S for R, S in zip(pushouts, [pushout(a, b) for a in Rlist for b in Rlist]))
            True

        ::

            sage: # needs sage.rings.padics
            sage: P0 = ZpFM(5, 10)
            sage: P1 = ZpFM(5, 20)
            sage: P2 = ZpCR(5, 10)
            sage: P3 = ZpCR(5, 20)
            sage: P4 = ZpCA(5, 10)
            sage: P5 = ZpCA(5, 20)
            sage: P6 = Qp(5, 10)
            sage: P7 = Qp(5, 20)
            sage: Plist = [P2,P3,P4,P5,P6,P7]
            sage: from sage.categories.pushout import pushout
            sage: pushouts = [P2,P3,P4,P5,P6,P7,P3,P3,P5,P5,P7,P7,P4,P5,P4,P5,P6,P7,
            ....:             P5,P5,P5,P5,P7,P7,P6,P7,P6,P7,P6,P7,P7,P7,P7,P7,P7,P7]
            sage: all(P is Q
            ....:     for P, Q in zip(pushouts, [pushout(a, b) for a in Plist for b in Plist]))
            True
        """
    def commutes(self, other):
        """
        Completion commutes with fraction fields.

        EXAMPLES::

            sage: F1 = Zp(5).construction()[0]                                          # needs sage.rings.padics
            sage: F2 = QQ.construction()[0]
            sage: F1.commutes(F2)                                                       # needs sage.rings.padics
            True

        TESTS:

        The fraction field ``R`` in the example below has no completion
        method. But completion commutes with the fraction field functor,
        and so it is tried internally whether applying the construction
        functors in opposite order works. It does::

            sage: P.<x> = ZZ[]
            sage: C = P.completion(x).construction()[0]
            sage: R = FractionField(P)
            sage: hasattr(R,'completion')
            False
            sage: C(R) is Frac(C(P))
            True
            sage: F = R.construction()[0]
            sage: (C*F)(ZZ['x']) is (F*C)(ZZ['x'])
            True

        The following was fixed in :issue:`15329` (it used to result
        in an infinite recursion. In :issue:`23218` the construction
        of `p`-adic fields changed, so there is no longer an
        Ambiguous base extension error raised)::

            sage: from sage.categories.pushout import pushout
            sage: pushout(Qp(7), RLF)                                                   # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            CoercionException: Don't know how to
            apply Completion[+Infinity, prec=+Infinity]
            to 7-adic Ring with capped relative precision 20
        """

class QuotientFunctor(ConstructionFunctor):
    """
    Construction functor for quotient rings.

    .. NOTE::

        The functor keeps track of variable names. Optionally, it may
        keep track of additional properties of the quotient, such as
        its category or its implementation.

    EXAMPLES::

        sage: P.<x,y> = ZZ[]
        sage: Q = P.quo([x^2 + y^2] * P)
        sage: F = Q.construction()[0]
        sage: F(QQ['x','y'])
        Quotient of Multivariate Polynomial Ring in x, y over Rational Field
         by the ideal (x^2 + y^2)
        sage: F(QQ['x','y']) == QQ['x','y'].quo([x^2 + y^2] * QQ['x','y'])
        True
        sage: F(QQ['x','y','z'])
        Traceback (most recent call last):
        ...
        CoercionException: Cannot apply this quotient functor to
         Multivariate Polynomial Ring in x, y, z over Rational Field
        sage: F(QQ['y','z'])                                                            # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        TypeError: Could not find a mapping of the passed element to this ring.
    """
    rank: float
    I: Incomplete
    names: Incomplete
    as_field: Incomplete
    kwds: Incomplete
    def __init__(self, I, names=None, as_field: bool = False, domain=None, codomain=None, **kwds) -> None:
        """
        INPUT:

        - ``I`` -- an ideal (the modulus)
        - ``names`` -- string or list of strings (optional); the names for the
          quotient ring generators
        - ``as_field`` -- boolean (default: ``False``); return the quotient
          ring as field (if available)
        - ``domain`` -- category (default: ``Rings()``); the domain of
          this functor
        - ``codomain`` -- category (default: ``Rings()``); the codomain
          of this functor
        - Further named arguments. In particular, an implementation of the
          quotient can be suggested here.  These named arguments are passed to
          the quotient construction.

        TESTS::

            sage: from sage.categories.pushout import QuotientFunctor
            sage: P.<t> = ZZ[]
            sage: F = QuotientFunctor([5 + t^2] * P)
            sage: F(P)                                                                  # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in tbar
             over Integer Ring with modulus t^2 + 5
            sage: F(QQ['t'])                                                            # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in tbar
             over Rational Field with modulus t^2 + 5
            sage: F = QuotientFunctor([5 + t^2] * P, names='s')
            sage: F(P)                                                                  # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in s
             over Integer Ring with modulus t^2 + 5
            sage: F(QQ['t'])                                                            # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in s
             over Rational Field with modulus t^2 + 5
            sage: F = QuotientFunctor([5] * ZZ, as_field=True)
            sage: F(ZZ)
            Finite Field of size 5
            sage: F = QuotientFunctor([5] * ZZ)
            sage: F(ZZ)
            Ring of integers modulo 5
        """
    def __eq__(self, other):
        """
        The types, domain, codomain, names and moduli are compared.

        TESTS::

            sage: # needs sage.libs.pari
            sage: P.<x> = QQ[]
            sage: F = P.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            sage: F == loads(dumps(F))
            True
            sage: P2.<x,y> = QQ[]
            sage: F == P2.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            False
            sage: P3.<x> = ZZ[]
            sage: F == P3.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: P.<x> = QQ[]
            sage: F = P.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            sage: F != loads(dumps(F))
            False
            sage: P2.<x,y> = QQ[]
            sage: F != P2.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            True
            sage: P3.<x> = ZZ[]
            sage: F != P3.quo([(x^2+1)^2*(x^2-3),(x^2+1)^2*(x^5+3)]).construction()[0]
            False
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Two quotient functors with coinciding names are merged by taking the gcd
        of their moduli, the meet of their domains, and the join of their codomains.

        In particular, if one of the functors being merged knows that the quotient
        is going to be a field, then the merged functor will return fields as
        well.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: P.<x> = QQ[]
            sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
            sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
            sage: from sage.categories.pushout import pushout
            sage: pushout(Q1,Q2)    # indirect doctest
            Univariate Quotient Polynomial Ring in xbar over Rational Field
             with modulus x^4 + 2*x^2 + 1

        The following was fixed in :issue:`8800`::

            sage: pushout(GF(5), Integers(5))                                           # needs sage.libs.pari
            Finite Field of size 5
        """

class AlgebraicExtensionFunctor(ConstructionFunctor):
    """
    Algebraic extension (univariate polynomial ring modulo principal ideal).

    EXAMPLES::

        sage: x = polygen(QQ, 'x')
        sage: K.<a> = NumberField(x^3 + x^2 + 1)                                        # needs sage.rings.number_field
        sage: F = K.construction()[0]                                                   # needs sage.rings.number_field
        sage: F(ZZ['t'])                                                                # needs sage.rings.number_field
        Univariate Quotient Polynomial Ring in a
         over Univariate Polynomial Ring in t over Integer Ring
         with modulus a^3 + a^2 + 1

    Note that, even if a field is algebraically closed, the algebraic
    extension will be constructed as the quotient of a univariate
    polynomial ring::

        sage: F(CC)                                                                     # needs sage.rings.number_field
        Univariate Quotient Polynomial Ring in a
         over Complex Field with 53 bits of precision
         with modulus a^3 + a^2 + 1.00000000000000
        sage: F(RR)                                                                     # needs sage.rings.number_field
        Univariate Quotient Polynomial Ring in a
         over Real Field with 53 bits of precision
         with modulus a^3 + a^2 + 1.00000000000000

    Note that the construction functor of a number field applied to
    the integers returns an order (not necessarily maximal) of that
    field, similar to the behaviour of ``ZZ.extension(...)``::

        sage: F(ZZ)                                                                     # needs sage.rings.number_field
        Order generated by a in Number Field in a with defining polynomial x^3 + x^2 + 1

    This also holds for non-absolute number fields::

        sage: # needs sage.rings.number_field
        sage: x = polygen(QQ, 'x')
        sage: K.<a,b> = NumberField([x^3 + x^2 + 1, x^2 + x + 1])
        sage: F = K.construction()[0]
        sage: O = F(ZZ); O
        Relative Order
         generated by [(b - 2)*a^2 + (3*b - 1)*a + 3*b + 4, a - b]
         in Number Field in a with defining polynomial x^3 + x^2 + 1
         over its base field
        sage: O.ambient() is K
        True

    Special cases are made for cyclotomic fields and residue fields::

        sage: # needs sage.rings.number_field
        sage: C = CyclotomicField(8)
        sage: F, R = C.construction()
        sage: F
        AlgebraicExtensionFunctor
        sage: R
        Rational Field
        sage: F(R)
        Cyclotomic Field of order 8 and degree 4
        sage: F(ZZ)
        Maximal Order generated by zeta8 in Cyclotomic Field of order 8 and degree 4

    ::

        sage: # needs sage.rings.number_field
        sage: K.<z> = CyclotomicField(7)
        sage: P = K.factor(17)[0][0]
        sage: k = K.residue_field(P)
        sage: F, R = k.construction()
        sage: F
        AlgebraicExtensionFunctor
        sage: R
        Cyclotomic Field of order 7 and degree 6
        sage: F(R) is k
        True
        sage: F(ZZ)
        Residue field of Integers modulo 17
        sage: F(CyclotomicField(49))
        Residue field in zbar of Fractional ideal (17)
    """
    rank: int
    polys: Incomplete
    names: Incomplete
    embeddings: Incomplete
    structures: Incomplete
    cyclotomic: Incomplete
    precs: Incomplete
    implementations: Incomplete
    residue: Incomplete
    latex_names: Incomplete
    kwds: Incomplete
    def __init__(self, polys, names, embeddings=None, structures=None, cyclotomic=None, precs=None, implementations=None, *, residue=None, latex_names=None, **kwds) -> None:
        """
        INPUT:

        - ``polys`` -- list of polynomials (or of integers, for
          finite fields and unramified local extensions)

        - ``names`` -- list of strings of the same length as the
          list ``polys``

        - ``embeddings`` -- (optional) list of approximate complex
          values, determining an embedding of the generators into the
          complex field, or ``None`` for each generator whose
          embedding is not prescribed.

        - ``structures`` -- (optional) list of structural morphisms of
          number fields; see
          :class:`~sage.rings.number_field.structure.NumberFieldStructure`.

        - ``cyclotomic`` -- (optional) integer. If it is provided,
          application of the functor to the rational field yields a
          cyclotomic field, rather than just a number field.

        - ``precs`` -- (optional) list of integers. If it is provided,
          it is used to determine the precision of `p`-adic extensions.

        - ``implementations`` -- (optional) list of strings.
          If it is provided, it is used to determine an implementation in the
          `p`-adic case.

        - ``residue`` -- (optional) prime ideal of an order in a number
          field, determining a residue field. If it is provided,
          application of the functor to a number field yields the
          residue field with respect to the given prime ideal
          (coerced into the number field).

        - ``latex_names`` -- (optional) list of strings of the same length
          as the list ``polys``

        - ``**kwds`` -- further keywords; when the functor is applied
          to a ring `R`, these are passed to the ``extension()``
          method of `R`.

        REMARK:

        Currently, an embedding can only be provided for the last
        generator, and only when the construction functor is applied
        to the rational field. There will be no error when constructing
        the functor, but when applying it.

        TESTS::

            sage: from sage.categories.pushout import AlgebraicExtensionFunctor
            sage: P.<x> = ZZ[]
            sage: F1 = AlgebraicExtensionFunctor([x^3 - x^2 + 1], ['a'], [None])
            sage: F2 = AlgebraicExtensionFunctor([x^3 - x^2 + 1], ['a'], [0])
            sage: F1 == F2
            False
            sage: F1(QQ)                                                                # needs sage.rings.number_field
            Number Field in a with defining polynomial x^3 - x^2 + 1
            sage: F1(QQ).coerce_embedding()                                             # needs sage.rings.number_field
            sage: phi = F2(QQ).coerce_embedding().__copy__(); phi                       # needs sage.rings.number_field
            Generic morphism:
              From: Number Field in a with defining polynomial x^3 - x^2 + 1
                    with a = -0.7548776662466928?
              To:   Real Lazy Field
              Defn: a -> -0.7548776662466928?
            sage: F1(QQ) == F2(QQ)                                                      # needs sage.rings.number_field
            False
            sage: F1(GF(5))                                                             # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in a over Finite Field of size 5
             with modulus a^3 + 4*a^2 + 1
            sage: F2(GF(5))                                                             # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            NotImplementedError: ring extension with prescribed embedding is not implemented

        When applying a number field constructor to the ring of
        integers, an order (not necessarily maximal) of that field is
        returned, similar to the behaviour of ``ZZ.extension``::

            sage: F1(ZZ)                                                                # needs sage.rings.number_field
            Order generated by a in Number Field in a with defining polynomial x^3 - x^2 + 1

        The cyclotomic fields form a special case of number fields
        with prescribed embeddings::

            sage: # needs sage.rings.number_field
            sage: C = CyclotomicField(8)
            sage: F, R = C.construction()
            sage: F
            AlgebraicExtensionFunctor
            sage: R
            Rational Field
            sage: F(R)
            Cyclotomic Field of order 8 and degree 4
            sage: F(ZZ)
            Maximal Order generated by zeta8 in Cyclotomic Field of order 8 and degree 4

        The data stored in this construction includes structural
        morphisms of number fields (see :issue:`20826`)::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: K.<a> = NumberField(x^2 - 3)
            sage: L0.<b> = K.change_names()
            sage: L0.structure()
            (Isomorphism given by variable name change map:
               From: Number Field in b with defining polynomial x^2 - 3
               To:   Number Field in a with defining polynomial x^2 - 3,
             Isomorphism given by variable name change map:
               From: Number Field in a with defining polynomial x^2 - 3
               To:   Number Field in b with defining polynomial x^2 - 3)
            sage: L1 = (b*x).parent().base_ring()
            sage: L1 is L0
            True
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + 1)
            sage: F = K.construction()[0]
            sage: F == loads(dumps(F))
            True

            sage: K2.<a> = NumberField(x^3 + x^2 + 1, latex_names='a')                  # needs sage.rings.number_field
            sage: F2 = K2.construction()[0]                                             # needs sage.rings.number_field
            sage: F2 == F                                                               # needs sage.rings.number_field
            True

            sage: K3.<a> = NumberField(x^3 + x^2 + 1, latex_names='alpha')              # needs sage.rings.number_field
            sage: F3 = K3.construction()[0]                                             # needs sage.rings.number_field
            sage: F3 == F                                                               # needs sage.rings.number_field
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + 1)                                    # needs sage.rings.number_field
            sage: F = K.construction()[0]                                               # needs sage.rings.number_field
            sage: F != loads(dumps(F))                                                  # needs sage.rings.number_field
            False
        """
    __hash__: Incomplete
    def merge(self, other):
        """
        Merging with another :class:`AlgebraicExtensionFunctor`.

        INPUT:

        - ``other`` -- Construction Functor

        OUTPUT:

        - If ``self==other``, ``self`` is returned.
        - If ``self`` and ``other`` are simple extensions
          and both provide an embedding, then it is tested
          whether one of the number fields provided by
          the functors coerces into the other; the functor
          associated with the target of the coercion is
          returned. Otherwise, the construction functor
          associated with the pushout of the codomains
          of the two embeddings is returned, provided that
          it is a number field.
        - If these two extensions are defined by Conway polynomials
          over finite fields, merges them into a single extension of
          degree the lcm of the two degrees.
        - Otherwise, ``None`` is returned.

        REMARK:

        Algebraic extension with embeddings currently only
        works when applied to the rational field. This is
        why we use the admittedly strange rule above for
        merging.

        EXAMPLES:

        The following demonstrate coercions for finite fields using Conway or
        pseudo-Conway polynomials::

            sage: k = GF(3^2, prefix='z'); a = k.gen()                                  # needs sage.rings.finite_rings
            sage: l = GF(3^3, prefix='z'); b = l.gen()                                  # needs sage.rings.finite_rings
            sage: a + b  # indirect doctest                                             # needs sage.rings.finite_rings
            z6^5 + 2*z6^4 + 2*z6^3 + z6^2 + 2*z6 + 1

        Note that embeddings are compatible in lattices of such finite fields::

            sage: # needs sage.rings.finite_rings
            sage: m = GF(3^5, prefix='z'); c = m.gen()
            sage: (a + b) + c == a + (b + c) # indirect doctest
            True
            sage: from sage.categories.pushout import pushout
            sage: n = pushout(k, l)
            sage: o = pushout(l, m)
            sage: q = pushout(n, o)
            sage: q(o(b)) == q(n(b)) # indirect doctest
            True

        Coercion is also available for number fields::

            sage: # needs sage.rings.number_field
            sage: P.<x> = QQ[]
            sage: L.<b> = NumberField(x^8 - x^4 + 1, embedding=CDF.0)
            sage: M1.<c1> = NumberField(x^2 + x + 1, embedding=b^4 - 1)
            sage: M2.<c2> = NumberField(x^2 + 1, embedding=-b^6)
            sage: M1.coerce_map_from(M2)
            sage: M2.coerce_map_from(M1)
            sage: c1 + c2; parent(c1 + c2)    #indirect doctest
            -b^6 + b^4 - 1
            Number Field in b with defining polynomial x^8 - x^4 + 1
             with b = -0.2588190451025208? + 0.9659258262890683?*I
            sage: pushout(M1['x'], M2['x'])                                             # needs sage.rings.finite_rings
            Univariate Polynomial Ring in x
             over Number Field in b with defining polynomial x^8 - x^4 + 1
              with b = -0.2588190451025208? + 0.9659258262890683?*I

        In the previous example, the number field ``L`` becomes the pushout
        of ``M1`` and ``M2`` since both are provided with an embedding into
        ``L``, *and* since ``L`` is a number field. If two number fields
        are embedded into a field that is not a numberfield, no merging
        occurs::

            sage: # needs sage.rings.complex_double sage.rings.number_field
            sage: cbrt2 = CDF(2)^(1/3)
            sage: zeta3 = CDF.zeta(3)
            sage: K.<a> = NumberField(x^3 - 2, embedding=cbrt2 * zeta3)
            sage: L.<b> = NumberField(x^6 - 2, embedding=1.1)
            sage: L.coerce_map_from(K)
            sage: K.coerce_map_from(L)
            sage: pushout(K, L)                                                         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            CoercionException: ('Ambiguous Base Extension', Number Field in a with
            defining polynomial x^3 - 2 with a = -0.6299605249474365? + 1.091123635971722?*I,
            Number Field in b with defining polynomial x^6 - 2 with b = 1.122462048309373?)
        """
    def __mul__(self, other):
        """
        Compose construction functors to a composite construction functor, unless one of them is the identity.

        .. NOTE::

            The product is in functorial notation, i.e., when applying the
            product to an object then the second factor is applied first.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: P.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 5, embedding=0)
            sage: L.<b> = K.extension(x^2 + a)
            sage: F, R = L.construction()
            sage: prod(F.expand())(R) == L  #indirect doctest
            True
        """
    def expand(self):
        """
        Decompose the functor `F` into sub-functors, whose product returns `F`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 5, embedding=0)
            sage: L.<b> = K.extension(x^2 + a)
            sage: F, R = L.construction()
            sage: prod(F.expand())(R) == L
            True
            sage: K = NumberField([x^2 - 2, x^2 - 3],'a')
            sage: F, R = K.construction()
            sage: F
            AlgebraicExtensionFunctor
            sage: L = F.expand(); L
            [AlgebraicExtensionFunctor, AlgebraicExtensionFunctor]
            sage: L[-1](QQ)
            Number Field in a1 with defining polynomial x^2 - 3
        """

class AlgebraicClosureFunctor(ConstructionFunctor):
    """
    Algebraic Closure.

    EXAMPLES::

        sage: # needs sage.rings.complex_double sage.rings.number_field
        sage: F = CDF.construction()[0]
        sage: F(QQ)
        Algebraic Field
        sage: F(RR)                                                                     # needs sage.rings.real_mpfr
        Complex Field with 53 bits of precision
        sage: F(F(QQ)) is F(QQ)
        True
    """
    rank: int
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import AlgebraicClosureFunctor
            sage: F = AlgebraicClosureFunctor()
            sage: F(QQ)                                                                 # needs sage.rings.number_field
            Algebraic Field
            sage: F(RR)                                                                 # needs sage.rings.real_mpfr
            Complex Field with 53 bits of precision
            sage: F == loads(dumps(F))
            True
        """
    def merge(self, other):
        """
        Mathematically, Algebraic Closure subsumes Algebraic Extension.
        However, it seems that people do want to work with algebraic
        extensions of ``RR``. Therefore, we do not merge with algebraic extension.

        TESTS::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + 1)                                    # needs sage.rings.number_field
            sage: CDF.construction()[0].merge(K.construction()[0]) is None              # needs sage.rings.number_field
            True
            sage: CDF.construction()[0].merge(CDF.construction()[0])                    # needs sage.rings.complex_double
            AlgebraicClosureFunctor
        """

class PermutationGroupFunctor(ConstructionFunctor):
    rank: int
    def __init__(self, gens, domain) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.pushout import PermutationGroupFunctor
            sage: PF = PermutationGroupFunctor([PermutationGroupElement([(1,2)])],      # needs sage.groups
            ....:                              [1,2]); PF
            PermutationGroupFunctor[(1,2)]
        """
    def __call__(self, R):
        """
        EXAMPLES::

            sage: P1 = PermutationGroup([[(1,2)]])                                      # needs sage.groups
            sage: PF, P = P1.construction()                                             # needs sage.groups
            sage: PF(P)                                                                 # needs sage.groups
            Permutation Group with generators [(1,2)]
        """
    def gens(self) -> tuple:
        """
        EXAMPLES::

            sage: P1 = PermutationGroup([[(1,2)]])                                      # needs sage.groups
            sage: PF, P = P1.construction()                                             # needs sage.groups
            sage: PF.gens()                                                             # needs sage.groups
            ((1,2),)
        """
    def merge(self, other):
        """
        Merge ``self`` with another construction functor, or return ``None``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: P1 = PermutationGroup([[(1,2)]])
            sage: PF1, P = P1.construction()
            sage: P2 = PermutationGroup([[(1,3)]])
            sage: PF2, P = P2.construction()
            sage: PF1.merge(PF2)
            PermutationGroupFunctor[(1,2), (1,3)]
        """

class EquivariantSubobjectConstructionFunctor(ConstructionFunctor):
    """
    Constructor for subobjects invariant or equivariant under given semigroup actions.

    Let `S` be a semigroup that
    - acts on a parent `X` as `s \\cdot x` (``action``, ``side='left'``) or
    - acts on `X` as `x \\cdot s` (``action``, ``side='right'``),
    and (possibly trivially)
    - acts on `X` as `s * x` (``other_action``, ``other_side='left'``) or
    - acts on `X` as `x * s` (``other_action``, ``other_side='right'``).

    The `S`-equivariant subobject is the subobject

    .. MATH::

        X^S := \\{x \\in X : s \\cdot x = s * x,\\, \\forall s \\in S \\}

    when ``side = other_side = 'left'`` and mutatis mutandis for the other values
    of ``side`` and ``other_side``.

    When ``other_action`` is trivial, `X^S` is called the `S`-invariant subobject.

    EXAMPLES:

    Monoterm symmetries of a tensor, here only for matrices: row (index 0),
    column (index 1); the order of the extra element 2 in a permutation determines
    whether it is a symmetry or an antisymmetry::

        sage: # needs sage.groups sage.modules
        sage: GSym01 = PermutationGroup([[(0,1),(2,),(3,)]]); GSym01
        Permutation Group with generators [(0,1)]
        sage: GASym01 = PermutationGroup([[(0,1),(2,3)]]); GASym01
        Permutation Group with generators [(0,1)(2,3)]
        sage: from sage.categories.action import Action
        sage: from sage.structure.element import Matrix
        sage: class TensorIndexAction(Action):
        ....:     def _act_(self, g, x):
        ....:         if isinstance(x, Matrix):
        ....:             if g(0) == 1:
        ....:                 if g(2) == 2:
        ....:                     return x.transpose()
        ....:                 else:
        ....:                     return -x.transpose()
        ....:             else:
        ....:                 return x
        ....:         raise NotImplementedError
        sage: M = matrix([[1, 2], [3, 4]]); M
        [1 2]
        [3 4]
        sage: GSym01_action = TensorIndexAction(GSym01, M.parent())
        sage: GASym01_action = TensorIndexAction(GASym01, M.parent())
        sage: GSym01_action.act(GSym01.0, M)
        [1 3]
        [2 4]
        sage: GASym01_action.act(GASym01.0, M)
        [-1 -3]
        [-2 -4]
        sage: Sym01 = M.parent().invariant_module(GSym01, action=GSym01_action); Sym01
        (Permutation Group with generators [(0,1)])-invariant submodule
         of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
        sage: list(Sym01.basis())
        [B[0], B[1], B[2]]
        sage: list(Sym01.basis().map(Sym01.lift))
        [
        [1 0]  [0 1]  [0 0]
        [0 0], [1 0], [0 1]
        ]
        sage: ASym01 = M.parent().invariant_module(GASym01, action=GASym01_action)
        sage: ASym01
        (Permutation Group with generators [(0,1)(2,3)])-invariant submodule
         of Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
        sage: list(ASym01.basis())
        [B[0]]
        sage: list(ASym01.basis().map(ASym01.lift))
        [
        [ 0  1]
        [-1  0]
        ]
        sage: from sage.categories.pushout import pushout
        sage: pushout(Sym01, QQ)
        (Permutation Group with generators [(0,1)])-invariant submodule
         of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
    """
    S: Incomplete
    action: Incomplete
    side: Incomplete
    other_action: Incomplete
    other_side: Incomplete
    def __init__(self, S, action=..., side: str = 'left', other_action=None, other_side: str = 'left') -> None:
        """
        EXAMPLES::

            sage: # needs sage.combinat sage.groups sage.modules
            sage: G = SymmetricGroup(3); G.rename('S3')
            sage: M = FreeModule(ZZ, [1,2,3], prefix='M'); M.rename('M')
            sage: action = lambda g, x: M.term(g(x))
            sage: I = M.invariant_module(G, action_on_basis=action); I
            (S3)-invariant submodule of M
            sage: I.construction()
            (EquivariantSubobjectConstructionFunctor,
            Representation of S3 indexed by {1, 2, 3} over Integer Ring)
        """

class BlackBoxConstructionFunctor(ConstructionFunctor):
    """
    Construction functor obtained from any callable object.

    EXAMPLES::

        sage: from sage.categories.pushout import BlackBoxConstructionFunctor

        sage: # needs sage.libs.gap
        sage: from sage.interfaces.gap import gap
        sage: FG = BlackBoxConstructionFunctor(gap)
        sage: FG
        BlackBoxConstructionFunctor
        sage: FG(ZZ)
        Integers
        sage: FG(ZZ).parent()
        Gap
        sage: FG == loads(dumps(FG))
        True

        sage: FS = BlackBoxConstructionFunctor(singular)
        sage: FS(QQ['t'])                                                               # needs sage.libs.singular
        polynomial ring, over a field, global ordering
        // coefficients: QQ...
        // number of vars : 1
        //        block   1 : ordering lp
        //                  : names    t
        //        block   2 : ordering C
        sage: FG == FS                                                                  # needs sage.libs.gap sage.libs.singular
        False
    """
    rank: int
    box: Incomplete
    def __init__(self, box) -> None:
        """
        TESTS::

            sage: from sage.categories.pushout import BlackBoxConstructionFunctor
            sage: FG = BlackBoxConstructionFunctor(gap)
            sage: FM = BlackBoxConstructionFunctor(maxima)                              # needs sage.symbolic
            sage: FM == FG                                                              # needs sage.libs.gap sage.symbolic
            False
            sage: FM == loads(dumps(FM))                                                # needs sage.symbolic
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.categories.pushout import BlackBoxConstructionFunctor
            sage: FG = BlackBoxConstructionFunctor(gap)
            sage: FM = BlackBoxConstructionFunctor(maxima)                              # needs sage.symbolic
            sage: FM == FG       # indirect doctest                                     # needs sage.libs.gap sage.symbolic
            False
            sage: FM == loads(dumps(FM))                                                # needs sage.symbolic
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.categories.pushout import BlackBoxConstructionFunctor
            sage: FG = BlackBoxConstructionFunctor(gap)
            sage: FM = BlackBoxConstructionFunctor(maxima)                              # needs sage.symbolic
            sage: FM != FG       # indirect doctest                                     # needs sage.libs.gap sage.symbolic
            True
            sage: FM != loads(dumps(FM))                                                # needs sage.symbolic
            False
        """
    __hash__: Incomplete

def pushout(R, S):
    '''
    Given a pair of objects `R` and `S`, try to construct a
    reasonable object `Y` and return maps such that
    canonically `R \\leftarrow Y \\rightarrow S`.

    ALGORITHM:

    This incorporates the idea of functors discussed at Sage Days 4.
    Every object `R` can be viewed as an initial object and a series
    of functors (e.g. polynomial, quotient, extension, completion,
    vector/matrix, etc.). Call the series of increasingly simple
    objects (with the associated functors) the "tower" of `R`. The
    construction method is used to create the tower.

    Given two objects `R` and `S`, try to find a common initial object
    `Z`. If the towers of `R` and `S` meet, let `Z` be their join.
    Otherwise, see if the top of one coerces naturally into the other.

    Now we have an initial object and two ordered lists of functors to
    apply. We wish to merge these in an unambiguous order, popping
    elements off the top of one or the other tower as we apply them to
    `Z`.

    - If the functors are of distinct types, there is an absolute
      ordering given by the rank attribute. Use this.

    - Otherwise:

      - If the tops are equal, we (try to) merge them.

      - If exactly one occurs lower in the other tower, we may
        unambiguously apply the other (hoping for a later merge).

      - If the tops commute, we can apply either first.

      - Otherwise fail due to ambiguity.

    The algorithm assumes by default that when a construction `F` is
    applied to an object `X`, the object `F(X)` admits a coercion map
    from `X`.  However, the algorithm can also handle the case where
    `F(X)` has a coercion map *to* `X` instead.  In this case, the
    attribute ``coercion_reversed`` of the class implementing `F`
    should be set to ``True``.

    EXAMPLES:

    Here our "towers" are `R = Complete_7(Frac(\\ZZ))` and `Frac(Poly_x(\\ZZ))`,
    which give us `Frac(Poly_x(Complete_7(Frac(\\ZZ))))`::

        sage: from sage.categories.pushout import pushout
        sage: pushout(Qp(7), Frac(ZZ[\'x\']))                                             # needs sage.rings.padics
        Fraction Field of Univariate Polynomial Ring in x
         over 7-adic Field with capped relative precision 20

    Note we get the same thing with
    ::

        sage: pushout(Zp(7), Frac(QQ[\'x\']))                                             # needs sage.rings.padics
        Fraction Field of Univariate Polynomial Ring in x
         over 7-adic Field with capped relative precision 20
        sage: pushout(Zp(7)[\'x\'], Frac(QQ[\'x\']))                                        # needs sage.rings.padics
        Fraction Field of Univariate Polynomial Ring in x
         over 7-adic Field with capped relative precision 20

    Note that polynomial variable ordering must be unambiguously determined.
    ::

        sage: pushout(ZZ[\'x,y,z\'], QQ[\'w,z,t\'])
        Traceback (most recent call last):
        ...
        CoercionException: (\'Ambiguous Base Extension\',
        Multivariate Polynomial Ring in x, y, z over Integer Ring,
        Multivariate Polynomial Ring in w, z, t over Rational Field)
        sage: pushout(ZZ[\'x,y,z\'], QQ[\'w,x,z,t\'])
        Multivariate Polynomial Ring in w, x, y, z, t over Rational Field

    Some other examples::

        sage: pushout(Zp(7)[\'y\'], Frac(QQ[\'t\'])[\'x,y,z\'])                               # needs sage.rings.padics
        Multivariate Polynomial Ring in x, y, z
         over Fraction Field of Univariate Polynomial Ring in t
          over 7-adic Field with capped relative precision 20
        sage: pushout(ZZ[\'x,y,z\'], Frac(ZZ[\'x\'])[\'y\'])
        Multivariate Polynomial Ring in y, z
         over Fraction Field of Univariate Polynomial Ring in x over Integer Ring
        sage: pushout(MatrixSpace(RDF, 2, 2), Frac(ZZ[\'x\']))                            # needs sage.modules
        Full MatrixSpace of 2 by 2 dense matrices
         over Fraction Field of Univariate Polynomial Ring in x over Real Double Field
        sage: pushout(ZZ, MatrixSpace(ZZ[[\'x\']], 3, 3))                                 # needs sage.modules
        Full MatrixSpace of 3 by 3 dense matrices
         over Power Series Ring in x over Integer Ring
        sage: pushout(QQ[\'x,y\'], ZZ[[\'x\']])
        Univariate Polynomial Ring in y
         over Power Series Ring in x over Rational Field
        sage: pushout(Frac(ZZ[\'x\']), QQ[[\'x\']])
        Laurent Series Ring in x over Rational Field

    A construction with ``coercion_reversed=True`` (currently only
    the :class:`SubspaceFunctor` construction) is only applied if it
    leads to a valid coercion::

        sage: # needs sage.modules
        sage: A = ZZ^2
        sage: V = span([[1, 2]], QQ)
        sage: P = sage.categories.pushout.pushout(A, V)
        sage: P
        Vector space of dimension 2 over Rational Field
        sage: P.has_coerce_map_from(A)
        True

        sage: # needs sage.modules
        sage: V = (QQ^3).span([[1, 2, 3/4]])
        sage: A = ZZ^3
        sage: pushout(A, V)
        Vector space of dimension 3 over Rational Field
        sage: B = A.span([[0, 0, 2/3]])
        sage: pushout(B, V)
        Vector space of degree 3 and dimension 2 over Rational Field
        User basis matrix:
        [1 2 0]
        [0 0 1]

    Some more tests with ``coercion_reversed=True``::

        sage: from sage.categories.pushout import ConstructionFunctor
        sage: class EvenPolynomialRing(type(QQ[\'x\'])):
        ....:     def __init__(self, base, var):
        ....:         super().__init__(base, var)
        ....:         self.register_embedding(base[var])
        ....:     def __repr__(self):
        ....:         return "Even Power " + super().__repr__()
        ....:     def construction(self):
        ....:         return EvenPolynomialFunctor(), self.base()[self.variable_name()]
        ....:     def _coerce_map_from_(self, R):
        ....:         return self.base().has_coerce_map_from(R)
        sage: class EvenPolynomialFunctor(ConstructionFunctor):
        ....:     rank = 10
        ....:     coercion_reversed = True
        ....:     def __init__(self):
        ....:         ConstructionFunctor.__init__(self, Rings(), Rings())
        ....:     def _apply_functor(self, R):
        ....:         return EvenPolynomialRing(R.base(), R.variable_name())
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), ZZ)
        Even Power Univariate Polynomial Ring in x over Rational Field
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), QQ)
        Even Power Univariate Polynomial Ring in x over Rational Field
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), RR)                                  # needs sage.rings.real_mpfr
        Even Power Univariate Polynomial Ring in x over Real Field with 53 bits of precision

        sage: pushout(EvenPolynomialRing(QQ, \'x\'), ZZ[\'x\'])
        Univariate Polynomial Ring in x over Rational Field
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), QQ[\'x\'])
        Univariate Polynomial Ring in x over Rational Field
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), RR[\'x\'])                             # needs sage.rings.real_mpfr
        Univariate Polynomial Ring in x over Real Field with 53 bits of precision

        sage: pushout(EvenPolynomialRing(QQ, \'x\'), EvenPolynomialRing(QQ, \'x\'))
        Even Power Univariate Polynomial Ring in x over Rational Field
        sage: pushout(EvenPolynomialRing(QQ, \'x\'), EvenPolynomialRing(RR, \'x\'))         # needs sage.rings.real_mpfr
        Even Power Univariate Polynomial Ring in x over Real Field with 53 bits of precision

        sage: pushout(EvenPolynomialRing(QQ, \'x\')^2, RR^2)                              # needs sage.modules sage.rings.real_mpfr
        Ambient free module of rank 2
         over the principal ideal domain Even Power Univariate Polynomial Ring in x
          over Real Field with 53 bits of precision
        sage: pushout(EvenPolynomialRing(QQ, \'x\')^2, RR[\'x\']^2)                         # needs sage.modules sage.rings.real_mpfr
        Ambient free module of rank 2
         over the principal ideal domain Univariate Polynomial Ring in x
         over Real Field with 53 bits of precision

    Some more tests related to univariate/multivariate
    constructions. We consider a generalization of polynomial rings,
    where in addition to the coefficient ring `C` we also specify
    an additive monoid `E` for the exponents of the indeterminate.
    In particular, the elements of such a parent are given by

    .. MATH::

        \\sum_{i=0}^I c_i X^{e_i}

    with `c_i \\in C` and `e_i \\in E`. We define
    ::

        sage: class GPolynomialRing(Parent):
        ....:     def __init__(self, coefficients, var, exponents):
        ....:         self.coefficients = coefficients
        ....:         self.var = var
        ....:         self.exponents = exponents
        ....:         super().__init__(category=Rings())
        ....:     def _repr_(self):
        ....:         return \'Generalized Polynomial Ring in %s^(%s) over %s\' % (
        ....:                self.var, self.exponents, self.coefficients)
        ....:     def construction(self):
        ....:         return GPolynomialFunctor(self.var, self.exponents), self.coefficients
        ....:     def _coerce_map_from_(self, R):
        ....:         return self.coefficients.has_coerce_map_from(R)

    and
    ::

        sage: class GPolynomialFunctor(ConstructionFunctor):
        ....:     rank = 10
        ....:     def __init__(self, var, exponents):
        ....:         self.var = var
        ....:         self.exponents = exponents
        ....:         ConstructionFunctor.__init__(self, Rings(), Rings())
        ....:     def _repr_(self):
        ....:         return \'GPoly[%s^(%s)]\' % (self.var, self.exponents)
        ....:     def _apply_functor(self, coefficients):
        ....:         return GPolynomialRing(coefficients, self.var, self.exponents)
        ....:     def merge(self, other):
        ....:         if isinstance(other, GPolynomialFunctor) and self.var == other.var:
        ....:             exponents = pushout(self.exponents, other.exponents)
        ....:             return GPolynomialFunctor(self.var, exponents)

    We can construct a parent now in two different ways::

        sage: GPolynomialRing(QQ, \'X\', ZZ)
        Generalized Polynomial Ring in X^(Integer Ring) over Rational Field
        sage: GP_ZZ = GPolynomialFunctor(\'X\', ZZ); GP_ZZ
        GPoly[X^(Integer Ring)]
        sage: GP_ZZ(QQ)
        Generalized Polynomial Ring in X^(Integer Ring) over Rational Field

    Since the construction
    ::

        sage: GP_ZZ(QQ).construction()
        (GPoly[X^(Integer Ring)], Rational Field)

    uses the coefficient ring, we have the usual coercion with respect
    to this parameter::

        sage: pushout(GP_ZZ(ZZ), GP_ZZ(QQ))
        Generalized Polynomial Ring in X^(Integer Ring) over Rational Field
        sage: pushout(GP_ZZ(ZZ[\'t\']), GP_ZZ(QQ))
        Generalized Polynomial Ring in X^(Integer Ring)
          over Univariate Polynomial Ring in t over Rational Field
        sage: pushout(GP_ZZ(ZZ[\'a,b\']), GP_ZZ(ZZ[\'b,c\']))
        Generalized Polynomial Ring in X^(Integer Ring)
          over Multivariate Polynomial Ring in a, b, c over Integer Ring
        sage: pushout(GP_ZZ(ZZ[\'a,b\']), GP_ZZ(QQ[\'b,c\']))
        Generalized Polynomial Ring in X^(Integer Ring)
          over Multivariate Polynomial Ring in a, b, c over Rational Field
        sage: pushout(GP_ZZ(ZZ[\'a,b\']), GP_ZZ(ZZ[\'c,d\']))
        Traceback (most recent call last):
        ...
        CoercionException: (\'Ambiguous Base Extension\', ...)

    ::

        sage: GP_QQ = GPolynomialFunctor(\'X\', QQ)
        sage: pushout(GP_ZZ(ZZ), GP_QQ(ZZ))
        Generalized Polynomial Ring in X^(Rational Field) over Integer Ring
        sage: pushout(GP_QQ(ZZ), GP_ZZ(ZZ))
        Generalized Polynomial Ring in X^(Rational Field) over Integer Ring

    ::

        sage: GP_ZZt = GPolynomialFunctor(\'X\', ZZ[\'t\'])
        sage: pushout(GP_ZZt(ZZ), GP_QQ(ZZ))
        Generalized Polynomial Ring in X^(Univariate Polynomial Ring in t
          over Rational Field) over Integer Ring

    ::

        sage: pushout(GP_ZZ(ZZ), GP_QQ(QQ))
        Generalized Polynomial Ring in X^(Rational Field) over Rational Field
        sage: pushout(GP_ZZ(QQ), GP_QQ(ZZ))
        Generalized Polynomial Ring in X^(Rational Field) over Rational Field
        sage: pushout(GP_ZZt(QQ), GP_QQ(ZZ))
        Generalized Polynomial Ring in X^(Univariate Polynomial Ring in t
          over Rational Field) over Rational Field
        sage: pushout(GP_ZZt(ZZ), GP_QQ(QQ))
        Generalized Polynomial Ring in X^(Univariate Polynomial Ring in t
          over Rational Field) over Rational Field
        sage: pushout(GP_ZZt(ZZ[\'a,b\']), GP_QQ(ZZ[\'c,d\']))
        Traceback (most recent call last):
        ...
        CoercionException: (\'Ambiguous Base Extension\', ...)
        sage: pushout(GP_ZZt(ZZ[\'a,b\']), GP_QQ(ZZ[\'b,c\']))
        Generalized Polynomial Ring
         in X^(Univariate Polynomial Ring in t over Rational Field)
          over Multivariate Polynomial Ring in a, b, c over Integer Ring

    Some tests with Cartesian products::

        sage: from sage.sets.cartesian_product import CartesianProduct
        sage: A = CartesianProduct((ZZ[\'x\'], QQ[\'y\'], QQ[\'z\']),
        ....:                      Sets().CartesianProducts())
        sage: B = CartesianProduct((ZZ[\'x\'], ZZ[\'y\'], ZZ[\'t\'][\'z\']),
        ....:                      Sets().CartesianProducts())
        sage: A.construction()
        (The cartesian_product functorial construction,
         (Univariate Polynomial Ring in x over Integer Ring,
          Univariate Polynomial Ring in y over Rational Field,
          Univariate Polynomial Ring in z over Rational Field))
        sage: pushout(A, B)
        The Cartesian product of
         (Univariate Polynomial Ring in x over Integer Ring,
          Univariate Polynomial Ring in y over Rational Field,
          Univariate Polynomial Ring in z over
           Univariate Polynomial Ring in t over Rational Field)
        sage: pushout(ZZ, cartesian_product([ZZ, QQ]))
        Traceback (most recent call last):
        ...
        CoercionException: \'NoneType\' object is not iterable

    ::

        sage: from sage.categories.pushout import PolynomialFunctor
        sage: from sage.sets.cartesian_product import CartesianProduct
        sage: class CartesianProductPoly(CartesianProduct):
        ....:     def __init__(self, polynomial_rings):
        ....:         sort = sorted(polynomial_rings,
        ....:                       key=lambda P: P.variable_name())
        ....:         super().__init__(sort, Sets().CartesianProducts())
        ....:     def vars(self):
        ....:         return tuple(P.variable_name()
        ....:                      for P in self.cartesian_factors())
        ....:     def _pushout_(self, other):
        ....:         if isinstance(other, CartesianProductPoly):
        ....:             s_vars = self.vars()
        ....:             o_vars = other.vars()
        ....:             if s_vars == o_vars:
        ....:                 return
        ....:             return pushout(CartesianProductPoly(
        ....:                     self.cartesian_factors() +
        ....:                     tuple(f for f in other.cartesian_factors()
        ....:                           if f.variable_name() not in s_vars)),
        ....:                 CartesianProductPoly(
        ....:                     other.cartesian_factors() +
        ....:                     tuple(f for f in self.cartesian_factors()
        ....:                           if f.variable_name() not in o_vars)))
        ....:         C = other.construction()
        ....:         if C is None:
        ....:             return
        ....:         elif isinstance(C[0], PolynomialFunctor):
        ....:             return pushout(self, CartesianProductPoly((other,)))

    ::

        sage: pushout(CartesianProductPoly((ZZ[\'x\'],)),
        ....:         CartesianProductPoly((ZZ[\'y\'],)))
        The Cartesian product of
         (Univariate Polynomial Ring in x over Integer Ring,
          Univariate Polynomial Ring in y over Integer Ring)
        sage: pushout(CartesianProductPoly((ZZ[\'x\'], ZZ[\'y\'])),
        ....:         CartesianProductPoly((ZZ[\'x\'], ZZ[\'z\'])))
        The Cartesian product of
         (Univariate Polynomial Ring in x over Integer Ring,
          Univariate Polynomial Ring in y over Integer Ring,
          Univariate Polynomial Ring in z over Integer Ring)
        sage: pushout(CartesianProductPoly((QQ[\'a,b\'][\'x\'], QQ[\'y\'])),                  # needs sage.symbolic
        ....:         CartesianProductPoly((ZZ[\'b,c\'][\'x\'], SR[\'z\'])))
        The Cartesian product of
         (Univariate Polynomial Ring in x over
            Multivariate Polynomial Ring in a, b, c over Rational Field,
          Univariate Polynomial Ring in y over Rational Field,
          Univariate Polynomial Ring in z over Symbolic Ring)

    ::

        sage: pushout(CartesianProductPoly((ZZ[\'x\'],)), ZZ[\'y\'])
        The Cartesian product of
         (Univariate Polynomial Ring in x over Integer Ring,
          Univariate Polynomial Ring in y over Integer Ring)
        sage: pushout(QQ[\'b,c\'][\'y\'], CartesianProductPoly((ZZ[\'a,b\'][\'x\'],)))
        The Cartesian product of
         (Univariate Polynomial Ring in x over
            Multivariate Polynomial Ring in a, b over Integer Ring,
          Univariate Polynomial Ring in y over
            Multivariate Polynomial Ring in b, c over Rational Field)

    ::

        sage: pushout(CartesianProductPoly((ZZ[\'x\'],)), ZZ)
        Traceback (most recent call last):
        ...
        CoercionException: No common base ("join") found for
        The cartesian_product functorial construction(...) and None(Integer Ring):
        (Multivariate) functors are incompatible.

    AUTHORS:

    - Robert Bradshaw
    - Peter Bruin
    - Simon King
    - Daniel Krenn
    - David Roe
    '''
def pushout_lattice(R, S):
    """
    Given a pair of objects `R` and `S`, try to construct a
    reasonable object `Y` and return maps such that
    canonically `R \\leftarrow Y \\rightarrow S`.

    ALGORITHM:

    This is based on the model that arose from much discussion at
    Sage Days 4.  Going up the tower of constructions of `R` and `S`
    (e.g. the reals come from the rationals come from the integers),
    try to find a common parent, and then try to fill in a lattice
    with these two towers as sides with the top as the common ancestor
    and the bottom will be the desired ring.

    See the code for a specific worked-out example.

    EXAMPLES::

        sage: from sage.categories.pushout import pushout_lattice
        sage: A, B = pushout_lattice(Qp(7), Frac(ZZ['x']))                              # needs sage.rings.padics
        sage: A.codomain()                                                              # needs sage.rings.padics
        Fraction Field of Univariate Polynomial Ring in x
         over 7-adic Field with capped relative precision 20
        sage: A.codomain() is B.codomain()                                              # needs sage.rings.padics
        True
        sage: A, B = pushout_lattice(ZZ, MatrixSpace(ZZ[['x']], 3, 3))                  # needs sage.modules
        sage: B                                                                         # needs sage.modules
        Identity endomorphism of Full MatrixSpace of 3 by 3 dense matrices
         over Power Series Ring in x over Integer Ring

    AUTHOR:

    - Robert Bradshaw
    """
def construction_tower(R):
    """
    An auxiliary function that is used in :func:`pushout` and :func:`pushout_lattice`.

    INPUT:

    - ``R`` -- an object

    OUTPUT:

    A constructive description of the object from scratch, by a list of pairs
    of a construction functor and an object to which the construction functor
    is to be applied. The first pair is formed by ``None`` and the given object.

    EXAMPLES::

        sage: from sage.categories.pushout import construction_tower
        sage: construction_tower(MatrixSpace(FractionField(QQ['t']), 2))                # needs sage.modules
        [(None, Full MatrixSpace of 2 by 2 dense matrices over Fraction Field
                 of Univariate Polynomial Ring in t over Rational Field),
         (MatrixFunctor, Fraction Field
                          of Univariate Polynomial Ring in t over Rational Field),
         (FractionField, Univariate Polynomial Ring in t over Rational Field),
         (Poly[t], Rational Field), (FractionField, Integer Ring)]
    """
def expand_tower(tower):
    """
    An auxiliary function that is used in :func:`pushout`.

    INPUT:

    - ``tower`` -- a construction tower as returned by
      :func:`construction_tower`

    OUTPUT: a new construction tower with all the construction functors expanded

    EXAMPLES::

        sage: from sage.categories.pushout import construction_tower, expand_tower
        sage: construction_tower(QQ['x,y,z'])
        [(None, Multivariate Polynomial Ring in x, y, z over Rational Field),
         (MPoly[x,y,z], Rational Field),
         (FractionField, Integer Ring)]
        sage: expand_tower(construction_tower(QQ['x,y,z']))
        [(None, Multivariate Polynomial Ring in x, y, z over Rational Field),
         (MPoly[z], Univariate Polynomial Ring in y
                     over Univariate Polynomial Ring in x over Rational Field),
         (MPoly[y], Univariate Polynomial Ring in x over Rational Field),
         (MPoly[x], Rational Field),
         (FractionField, Integer Ring)]
    """
def type_to_parent(P):
    """
    An auxiliary function that is used in :func:`pushout`.

    INPUT:

    - ``P`` -- a type

    OUTPUT: a Sage parent structure corresponding to the given type

    TESTS::

        sage: from sage.categories.pushout import type_to_parent
        sage: type_to_parent(int)
        Integer Ring
        sage: type_to_parent(float)
        Real Double Field
        sage: type_to_parent(complex)                                                   # needs sage.rings.complex_double
        Complex Double Field
        sage: type_to_parent(list)
        Traceback (most recent call last):
        ...
        TypeError: not a scalar type
    """
