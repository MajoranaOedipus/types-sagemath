from _typeshed import Incomplete
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings import ideal as ideal, quotient_ring_element as quotient_ring_element, ring as ring
from sage.structure.category_object import check_default_category as check_default_category, normalize_names as normalize_names
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

MPolynomialIdeal_quotient: Incomplete

def QuotientRing(R, I, names=None, **kwds):
    """
    Create a quotient ring of the ring `R` by the twosided ideal `I`.

    Variables are labeled by ``names`` (if the quotient ring is a quotient
    of a polynomial ring).  If ``names`` isn't given, 'bar' will be appended
    to the variable names in `R`.

    INPUT:

    - ``R`` -- a ring

    - ``I`` -- a twosided ideal of `R`

    - ``names`` -- (optional) a list of strings to be used as names for
      the variables in the quotient ring `R/I`

    - further named arguments that will be passed to the constructor
      of the quotient ring instance

    OUTPUT: `R/I` - the quotient ring `R` mod the ideal `I`

    ASSUMPTION:

    ``I`` has a method ``I.reduce(x)`` returning the normal form
    of elements `x\\in R`. In other words, it is required that
    ``I.reduce(x)==I.reduce(y)`` `\\iff x-y \\in I`, and
    ``x-I.reduce(x) in I``, for all `x,y\\in R`.

    EXAMPLES:

    Some simple quotient rings with the integers::

        sage: R = QuotientRing(ZZ, 7*ZZ); R
        Quotient of Integer Ring by the ideal (7)
        sage: R.gens()
        (1,)
        sage: 1*R(3); 6*R(3); 7*R(3)
        3
        4
        0

    ::

        sage: S = QuotientRing(ZZ,ZZ.ideal(8)); S
        Quotient of Integer Ring by the ideal (8)
        sage: 2*S(4)
        0

    With polynomial rings (note that the variable name of the quotient
    ring can be specified as shown below)::

        sage: # needs sage.libs.pari
        sage: P.<x> = QQ[]
        sage: R.<xx> = QuotientRing(P, P.ideal(x^2 + 1))
        sage: R
        Univariate Quotient Polynomial Ring in xx over Rational Field
         with modulus x^2 + 1
        sage: R.gens(); R.gen()
        (xx,)
        xx
        sage: for n in range(4): xx^n
        1
        xx
        -1
        -xx

    ::

        sage: # needs sage.libs.pari
        sage: P.<x> = QQ[]
        sage: S = QuotientRing(P, P.ideal(x^2 - 2))
        sage: S
        Univariate Quotient Polynomial Ring in xbar over Rational Field
         with modulus x^2 - 2
        sage: xbar = S.gen(); S.gen()
        xbar
        sage: for n in range(3): xbar^n
        1
        xbar
        2

    Sage coerces objects into ideals when possible::

        sage: P.<x> = QQ[]
        sage: R = QuotientRing(P, x^2 + 1); R                                           # needs sage.libs.pari
        Univariate Quotient Polynomial Ring in xbar over Rational Field
         with modulus x^2 + 1

    By Noether's homomorphism theorems, the quotient of a quotient ring
    of `R` is just the quotient of `R` by the sum of the ideals. In this
    example, we end up modding out the ideal `(x)` from the ring
    `\\QQ[x,y]`::

        sage: # needs sage.libs.pari sage.libs.singular
        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S.<a,b> = QuotientRing(R, R.ideal(1 + y^2))
        sage: T.<c,d> = QuotientRing(S, S.ideal(a))
        sage: T
        Quotient of Multivariate Polynomial Ring in x, y over Rational Field
         by the ideal (x, y^2 + 1)
        sage: R.gens(); S.gens(); T.gens()
        (x, y)
        (a, b)
        (0, d)
        sage: for n in range(4): d^n
        1
        d
        -1
        -d

    TESTS:

    By :issue:`11068`, the following does not return a generic
    quotient ring but a usual quotient of the integer ring::

        sage: R = Integers(8)
        sage: I = R.ideal(2)
        sage: R.quotient(I)
        Ring of integers modulo 2

    Here is an example of the quotient of a free algebra by a
    twosided homogeneous ideal (see :issue:`7797`)::

        sage: # needs sage.combinat sage.libs.singular sage.modules
        sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
        sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2] * F
        sage: Q.<a,b,c> = F.quo(I); Q
        Quotient of Free Associative Unital Algebra on 3 generators (x, y, z)
         over Rational Field by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)
        sage: a*b
        -b*c
        sage: a^3
        -b*c*a - b*c*b - b*c*c
        sage: J = Q * [a^3 - b^3] * Q
        sage: R.<i,j,k> = Q.quo(J); R
        Quotient of Free Associative Unital Algebra on 3 generators (x, y, z)
         over Rational Field by the ideal
         (-y*y*z - y*z*x - 2*y*z*z, x*y + y*z, x*x + x*y - y*x - y*y)
        sage: i^3
        -j*k*i - j*k*j - j*k*k
        sage: j^3
        -j*k*i - j*k*j - j*k*k

    Check that :issue:`5978` is fixed by if we quotient by the zero ideal `(0)`
    then we just return ``R``::

        sage: R = QQ['x']
        sage: R.quotient(R.zero_ideal())
        Univariate Polynomial Ring in x over Rational Field
        sage: R.<x> = PolynomialRing(ZZ)
        sage: R is R.quotient(R.zero_ideal())
        True
        sage: I = R.ideal(0)
        sage: R is R.quotient(I)
        True
    """
def is_QuotientRing(x):
    """
    Test whether or not ``x`` inherits from :class:`QuotientRing_nc`.

    EXAMPLES::

        sage: from sage.rings.quotient_ring import is_QuotientRing
        sage: R.<x> = PolynomialRing(ZZ,'x')
        sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
        sage: S = R.quotient_ring(I)
        sage: is_QuotientRing(S)
        doctest:warning...
        DeprecationWarning: The function is_QuotientRing is deprecated;
        use 'isinstance(..., QuotientRing_nc)' instead.
        See https://github.com/sagemath/sage/issues/38266 for details.
        True
        sage: is_QuotientRing(R)
        False

    ::

        sage: # needs sage.combinat sage.libs.singular sage.modules
        sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
        sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2] * F
        sage: Q = F.quo(I)
        sage: is_QuotientRing(Q)
        True
        sage: is_QuotientRing(F)
        False
    """

class QuotientRing_nc(Parent):
    """
    The quotient ring of `R` by a twosided ideal `I`.

    This class is for rings that are not in the category
    ``Rings().Commutative()``.

    EXAMPLES:

    Here is a quotient of a free algebra by a twosided homogeneous ideal::

        sage: # needs sage.combinat sage.libs.singular sage.modules
        sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
        sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2]*F
        sage: Q.<a,b,c> = F.quo(I); Q
        Quotient of Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field
         by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)
        sage: a*b
        -b*c
        sage: a^3
        -b*c*a - b*c*b - b*c*c

    A quotient of a quotient is just the quotient of the original top
    ring by the sum of two ideals::

        sage: # needs sage.combinat sage.libs.singular sage.modules
        sage: J = Q * [a^3 - b^3] * Q
        sage: R.<i,j,k> = Q.quo(J); R
        Quotient of
         Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field
         by the ideal (-y*y*z - y*z*x - 2*y*z*z, x*y + y*z, x*x + x*y - y*x - y*y)
        sage: i^3
        -j*k*i - j*k*j - j*k*k
        sage: j^3
        -j*k*i - j*k*j - j*k*k

    For rings that *do* inherit from :class:`~sage.rings.ring.CommutativeRing`,
    we provide a subclass :class:`QuotientRing_generic`, for backwards
    compatibility.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(ZZ,'x')
        sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
        sage: S = R.quotient_ring(I); S
        Quotient of Univariate Polynomial Ring in x over Integer Ring
         by the ideal (x^2 + 3*x + 4, x^2 + 1)

    ::

        sage: R.<x,y> = PolynomialRing(QQ)
        sage: S.<a,b> = R.quo(x^2 + y^2)                                                # needs sage.libs.singular
        sage: a^2 + b^2 == 0                                                            # needs sage.libs.singular
        True
        sage: S(0) == a^2 + b^2                                                         # needs sage.libs.singular
        True

    Again, a quotient of a quotient is just the quotient of the original top
    ring by the sum of two ideals.

    ::

        sage: # needs sage.libs.singular
        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S.<a,b> = R.quo(1 + y^2)
        sage: T.<c,d> = S.quo(a)
        sage: T
        Quotient of Multivariate Polynomial Ring in x, y over Rational Field
         by the ideal (x, y^2 + 1)
        sage: T.gens()
        (0, d)
    """
    Element = quotient_ring_element.QuotientRingElement
    def __init__(self, R, I, names, category=None) -> None:
        """
        Create the quotient ring of `R` by the twosided ideal `I`.

        INPUT:

        - ``R`` -- a ring

        - ``I`` -- a twosided ideal of `R`

        - ``names`` -- list of generator names

        EXAMPLES::

            sage: # needs sage.combinat sage.libs.singular sage.modules
            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2] * F
            sage: Q.<a,b,c> = F.quo(I); Q
            Quotient of
             Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field
             by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)
            sage: a*b
            -b*c
            sage: a^3
            -b*c*a - b*c*b - b*c*c
        """
    def construction(self):
        """
        Return the functorial construction of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ,'x')
            sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
            sage: R.quotient_ring(I).construction()
            (QuotientFunctor, Univariate Polynomial Ring in x over Integer Ring)

            sage: # needs sage.combinat sage.libs.singular sage.modules
            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2] * F
            sage: Q = F.quo(I)
            sage: Q.construction()
            (QuotientFunctor,
             Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field)

        TESTS::

            sage: F, R = Integers(5).construction()
            sage: F(R)
            Ring of integers modulo 5
            sage: F, R = GF(5).construction()
            sage: F(R)
            Finite Field of size 5
        """
    def is_commutative(self) -> bool:
        """
        Tell whether this quotient ring is commutative.

        .. NOTE::

            This is certainly the case if the cover ring is commutative.
            Otherwise, if this ring has a finite number of generators, it
            is tested whether they commute. If the number of generators is
            infinite, a :exc:`NotImplementedError` is raised.

        AUTHOR:

        - Simon King (2011-03-23): See :issue:`7797`.

        EXAMPLES:

        Any quotient of a commutative ring is commutative::

            sage: P.<a,b,c> = QQ[]
            sage: P.quo(P.random_element()).is_commutative()
            True

        The non-commutative case is more interesting::

            sage: # needs sage.combinat sage.libs.singular sage.modules
            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: I = F * [x*y + y*z, x^2 + x*y - y*x - y^2] * F
            sage: Q = F.quo(I)
            sage: Q.is_commutative()
            False
            sage: Q.1*Q.2 == Q.2*Q.1
            False

        In the next example, the generators apparently commute::

            sage: # needs sage.combinat sage.libs.singular sage.modules
            sage: J = F * [x*y - y*x, x*z - z*x, y*z - z*y, x^3 - y^3] * F
            sage: R = F.quo(J)
            sage: R.is_commutative()
            True
        """
    @cached_method
    def cover(self):
        """
        The covering ring homomorphism `R \\to R/I`, equipped with a section.

        EXAMPLES::

            sage: R = ZZ.quo(3 * ZZ)
            sage: pi = R.cover()
            sage: pi
            Ring morphism:
              From: Integer Ring
              To:   Ring of integers modulo 3
              Defn: Natural quotient map
            sage: pi(5)
            2
            sage: l = pi.lift()

        ::

            sage: # needs sage.libs.singular
            sage: R.<x,y>  = PolynomialRing(QQ)
            sage: Q = R.quo((x^2, y^2))
            sage: pi = Q.cover()
            sage: pi(x^3 + y)
            ybar
            sage: l = pi.lift(x + y^3)
            sage: l
            x
            sage: l = pi.lift(); l
            Set-theoretic ring morphism:
              From: Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                    by the ideal (x^2, y^2)
              To:   Multivariate Polynomial Ring in x, y over Rational Field
              Defn: Choice of lifting map
            sage: l(x + y^3)
            x
        """
    @cached_method
    def lifting_map(self):
        """
        Return the lifting map to the cover.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S = R.quotient(x^2 + y^2)
            sage: pi = S.cover(); pi
            Ring morphism:
              From: Multivariate Polynomial Ring in x, y over Rational Field
              To:   Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                    by the ideal (x^2 + y^2)
              Defn: Natural quotient map
            sage: L = S.lifting_map(); L
            Set-theoretic ring morphism:
              From: Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                    by the ideal (x^2 + y^2)
              To:   Multivariate Polynomial Ring in x, y over Rational Field
              Defn: Choice of lifting map
            sage: L(S.0)
            x
            sage: L(S.1)
            y

        Note that some reduction may be applied so that the lift of a
        reduction need not equal the original element::

            sage: z = pi(x^3 + 2*y^2); z                                                # needs sage.libs.singular
            -xbar*ybar^2 + 2*ybar^2
            sage: L(z)                                                                  # needs sage.libs.singular
            -x*y^2 + 2*y^2
            sage: L(z) == x^3 + 2*y^2                                                   # needs sage.libs.singular
            False

        Test that there also is a lift for rings that are no
        instances of :class:`~sage.rings.ring.Ring` (see :issue:`11068`)::

            sage: # needs sage.modules
            sage: MS = MatrixSpace(GF(5), 2, 2)
            sage: I = MS * [MS.0*MS.1, MS.2 + MS.3] * MS
            sage: Q = MS.quo(I)
            sage: Q.lift()
            Set-theoretic ring morphism:
              From: Quotient of Full MatrixSpace of 2 by 2 dense matrices
                    over Finite Field of size 5 by the ideal
            (
              [0 1]
              [0 0],
            <BLANKLINE>
              [0 0]
              [1 1]
            )
            <BLANKLINE>
              To:   Full MatrixSpace of 2 by 2 dense matrices over Finite Field of size 5
              Defn: Choice of lifting map
        """
    def lift(self, x=None):
        """
        Return the lifting map to the cover, or the image
        of an element under the lifting map.

        .. NOTE::

            The category framework imposes that ``Q.lift(x)`` returns
            the image of an element `x` under the lifting map. For
            backwards compatibility, we let ``Q.lift()`` return the
            lifting map.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S = R.quotient(x^2 + y^2)
            sage: S.lift()                                                              # needs sage.libs.singular
            Set-theoretic ring morphism:
              From: Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                    by the ideal (x^2 + y^2)
              To:   Multivariate Polynomial Ring in x, y over Rational Field
              Defn: Choice of lifting map
            sage: S.lift(S.0) == x                                                      # needs sage.libs.singular
            True
        """
    def retract(self, x):
        """
        The image of an element of the cover ring under the quotient map.

        INPUT:

        - ``x`` -- an element of the cover ring

        OUTPUT: the image of the given element in ``self``

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S = R.quotient(x^2 + y^2)
            sage: S.retract((x+y)^2)                                                    # needs sage.libs.singular
            2*xbar*ybar
        """
    def characteristic(self) -> None:
        """
        Return the characteristic of the quotient ring.

        .. TODO::

            Not yet implemented!

        EXAMPLES::

            sage: Q = QuotientRing(ZZ,7*ZZ)
            sage: Q.characteristic()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def defining_ideal(self):
        """
        Return the ideal generating this quotient ring.

        EXAMPLES:

        In the integers::

            sage: Q = QuotientRing(ZZ,7*ZZ)
            sage: Q.defining_ideal()
            Principal ideal (7) of Integer Ring

        An example involving a quotient of a quotient. By Noether's
        homomorphism theorems, this is actually a quotient by a sum of two
        ideals::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S.<a,b> = QuotientRing(R, R.ideal(1 + y^2))
            sage: T.<c,d> = QuotientRing(S, S.ideal(a))
            sage: S.defining_ideal()
            Ideal (y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field
            sage: T.defining_ideal()
            Ideal (x, y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field
        """
    @cached_method
    def is_field(self, proof: bool = True):
        """
        Return ``True`` if the quotient ring is a field. Checks to see if the
        defining ideal is maximal.

        TESTS::

            sage: Q = QuotientRing(ZZ, 7*ZZ)
            sage: Q.is_field()
            True

        Requires the ``is_maximal`` method of the defining ideal to be
        implemented::

            sage: R.<x, y> = ZZ[]
            sage: R.quotient_ring(R.ideal([2, 4 + x])).is_field()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    @cached_method
    def is_integral_domain(self, proof: bool = True):
        """
        With ``proof`` equal to ``True``  (the default), this function may
        raise a :exc:`NotImplementedError`.

        When ``proof`` is ``False``, if ``True`` is returned, then ``self`` is
        definitely an integral domain.  If the function returns ``False``,
        then either ``self`` is not an integral domain or it was unable to
        determine whether or not ``self`` is an integral domain.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: R.quo(x^2 - y).is_integral_domain()                                   # needs sage.libs.singular
            True
            sage: R.quo(x^2 - y^2).is_integral_domain()                                 # needs sage.libs.singular
            False
            sage: R.quo(x^2 - y^2).is_integral_domain(proof=False)                      # needs sage.libs.singular
            False
            sage: R.<a,b,c> = ZZ[]
            sage: Q = R.quotient_ring([a, b])
            sage: Q.is_integral_domain()
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: Q.is_integral_domain(proof=False)
            False
        """
    def is_noetherian(self):
        """
        Return ``True`` if this ring is Noetherian.

        EXAMPLES::

            sage: R = QuotientRing(ZZ, 102 * ZZ)
            sage: R.is_noetherian()
            True

            sage: P.<x> = QQ[]
            sage: R = QuotientRing(P, x^2 + 1)                                          # needs sage.libs.pari
            sage: R.is_noetherian()
            True

        If the cover ring of ``self`` is not Noetherian, we currently
        have no way of testing whether ``self`` is Noetherian, so we
        raise an error::

            sage: R.<x> = InfinitePolynomialRing(QQ)
            sage: R.is_noetherian()
            False
            sage: I = R.ideal([x[1]^2, x[2]])
            sage: S = R.quotient(I)
            sage: S.is_noetherian()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def cover_ring(self):
        """
        Return the cover ring of the quotient ring: that is, the original
        ring `R` from which we modded out an ideal, `I`.

        EXAMPLES::

            sage: Q = QuotientRing(ZZ, 7 * ZZ)
            sage: Q.cover_ring()
            Integer Ring

        ::

            sage: P.<x> = QQ[]
            sage: Q = QuotientRing(P, x^2 + 1)                                          # needs sage.libs.pari
            sage: Q.cover_ring()                                                        # needs sage.libs.pari
            Univariate Polynomial Ring in x over Rational Field
        """
    ambient = cover_ring
    def ideal(self, *gens, **kwds):
        """
        Return the ideal of ``self`` with the given generators.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: S = R.quotient_ring(x^2 + y^2)
            sage: S.ideal()                                                             # needs sage.libs.singular
            Ideal (0) of Quotient of Multivariate Polynomial Ring in x, y
             over Rational Field by the ideal (x^2 + y^2)
            sage: S.ideal(x + y + 1)                                                    # needs sage.libs.singular
            Ideal (xbar + ybar + 1) of Quotient of Multivariate Polynomial Ring in x, y
             over Rational Field by the ideal (x^2 + y^2)

        TESTS:

        We create an ideal of a fairly generic integer ring (see
        :issue:`5666`)::

            sage: R = Integers(10)
            sage: R.ideal(1)
            Principal ideal (1) of Ring of integers modulo 10
        """
    def __richcmp__(self, other, op):
        """
        Only quotients by the *same* ring and same ideal (with the same
        generators!!) are considered equal.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: S = R.quotient_ring(x^2 + y^2)
            sage: S == R.quotient_ring(x^2 + y^2)
            True

        The ideals `(x^2 + y^2)` and `(-x^2-y^2)` are
        equal, but since the generators are different, the corresponding
        quotient rings are not equal::

            sage: R.ideal(x^2 + y^2) == R.ideal(-x^2 - y^2)                             # needs sage.libs.singular
            True
            sage: R.quotient_ring(x^2 + y^2) == R.quotient_ring(-x^2 - y^2)
            False
        """
    def ngens(self):
        '''
        Return the number of generators for this quotient ring.

        .. TODO::

            Note that ``ngens`` counts 0 as a generator. Does
            this make sense? That is, since 0 only generates itself and the
            fact that this is true for all rings, is there a way to "knock it
            off" of the generators list if a generator of some original ring is
            modded out?

        EXAMPLES::

            sage: R = QuotientRing(ZZ, 7*ZZ)
            sage: R.gens(); R.ngens()
            (1,)
            1

        ::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: S.<a,b> = QuotientRing(R, R.ideal(1 + y^2))
            sage: T.<c,d> = QuotientRing(S, S.ideal(a))
            sage: T
            Quotient of Multivariate Polynomial Ring in x, y over Rational Field
             by the ideal (x, y^2 + 1)
            sage: R.gens(); S.gens(); T.gens()
            (x, y)
            (a, b)
            (0, d)
            sage: R.ngens(); S.ngens(); T.ngens()
            2
            2
            2
        '''
    def gen(self, i: int = 0):
        """
        Return the `i`-th generator for this quotient ring.

        EXAMPLES::

            sage: R = QuotientRing(ZZ, 7*ZZ)
            sage: R.gen(0)
            1

        ::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ,2)
            sage: S.<a,b> = QuotientRing(R, R.ideal(1 + y^2))
            sage: T.<c,d> = QuotientRing(S, S.ideal(a))
            sage: T
            Quotient of Multivariate Polynomial Ring in x, y over Rational Field
             by the ideal (x, y^2 + 1)
            sage: R.gen(0); R.gen(1)
            x
            y
            sage: S.gen(0); S.gen(1)
            a
            b
            sage: T.gen(0); T.gen(1)
            0
            d
        """
    def gens(self) -> tuple:
        """
        Return a tuple containing generators of ``self``.

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: S = R.quotient_ring(x^2 + y^2)
            sage: S.gens()
            (xbar, ybar)
        """
    def term_order(self):
        """
        Return the term order of this ring.

        EXAMPLES::

            sage: P.<a,b,c> = PolynomialRing(QQ)
            sage: I = Ideal([a^2 - a, b^2 - b, c^2 - c])
            sage: Q = P.quotient(I)
            sage: Q.term_order()
            Degree reverse lexicographic term order
        """
    def random_element(self):
        """
        Return a random element of this quotient ring obtained by
        sampling a random element of the cover ring and reducing
        it modulo the defining ideal.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: S = R.quotient([x^3, y^2])
            sage: S.random_element()  # random
            -8/5*xbar^2 + 3/2*xbar*ybar + 2*xbar - 4/23

        TESTS:

        Make sure we are not just getting images of integers in this
        ring (which would be the case if the default implementation
        of this method was inherited from generic rings)::

            sage: any(S.random_element() not in ZZ for _ in range(999))
            True
        """

class QuotientRing_generic(QuotientRing_nc, ring.CommutativeRing):
    """
    Create a quotient ring of a *commutative* ring `R` by the ideal `I`.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(ZZ)
        sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
        sage: S = R.quotient_ring(I); S
        Quotient of Univariate Polynomial Ring in x over Integer Ring
         by the ideal (x^2 + 3*x + 4, x^2 + 1)
    """
    def __init__(self, R, I, names, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``R`` -- a ring that is a :class:`~sage.rings.ring.CommutativeRing`

        - ``I`` -- an ideal of `R`

        - ``names`` -- list of generator names

        TESTS::

            sage: ZZ.quo(2) in Rings().Commutative()  # indirect doctest
            True
        """

class QuotientRingIdeal_generic(ideal.Ideal_generic):
    """
    Specialized class for quotient-ring ideals.

    EXAMPLES::

        sage: Zmod(9).ideal([-6,9])
        Ideal (3, 0) of Ring of integers modulo 9
    """
    def radical(self):
        """
        Return the radical of this ideal.

        EXAMPLES::

            sage: Zmod(16).ideal(4).radical()
            Principal ideal (2) of Ring of integers modulo 16
        """

class QuotientRingIdeal_principal(ideal.Ideal_principal, QuotientRingIdeal_generic):
    """
    Specialized class for principal quotient-ring ideals.

    EXAMPLES::

        sage: Zmod(9).ideal(-33)
        Principal ideal (3) of Ring of integers modulo 9
    """
