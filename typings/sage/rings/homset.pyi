from _typeshed import Incomplete
from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.categories.rings import Rings as Rings
from sage.rings import morphism as morphism, quotient_ring as quotient_ring

def is_RingHomset(H):
    """
    Return ``True`` if ``H`` is a space of homomorphisms between two rings.

    EXAMPLES::

        sage: from sage.rings.homset import is_RingHomset as is_RH
        sage: is_RH(Hom(ZZ, QQ))
        doctest:warning...
        DeprecationWarning: the function is_RingHomset is deprecated;
        use 'isinstance(..., RingHomset_generic)' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        True
        sage: is_RH(ZZ)
        False
        sage: is_RH(Hom(RR, CC))                                                        # needs sage.rings.real_mpfr
        True
        sage: is_RH(Hom(FreeModule(ZZ,1), FreeModule(QQ,1)))                            # needs sage.modules
        False
    """
def RingHomset(R, S, category=None):
    """
    Construct a space of homomorphisms between the rings ``R`` and ``S``.

    For more on homsets, see :func:`Hom()`.

    EXAMPLES::

        sage: Hom(ZZ, QQ) # indirect doctest
        Set of Homomorphisms from Integer Ring to Rational Field
    """

class RingHomset_generic(HomsetWithBase):
    """
    A generic space of homomorphisms between two rings.

    EXAMPLES::

        sage: Hom(ZZ, QQ)
        Set of Homomorphisms from Integer Ring to Rational Field
        sage: QQ.Hom(ZZ)
        Set of Homomorphisms from Rational Field to Integer Ring
    """
    Element: Incomplete
    def __init__(self, R, S, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Hom(ZZ, QQ)
            Set of Homomorphisms from Integer Ring to Rational Field
        """
    def has_coerce_map_from(self, x):
        """
        The default for coercion maps between ring homomorphism spaces is
        very restrictive (until more implementation work is done).

        Currently this checks if the domains and the codomains are equal.

        EXAMPLES::

            sage: H = Hom(ZZ, QQ)
            sage: H2 = Hom(QQ, ZZ)
            sage: H.has_coerce_map_from(H2)
            False
        """
    def natural_map(self):
        """
        Return the natural map from the domain to the codomain.

        The natural map is the coercion map from the domain ring to the
        codomain ring.

        EXAMPLES::

            sage: H = Hom(ZZ, QQ)
            sage: H.natural_map()
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
        """
    def zero(self):
        """
        Return the zero element of this homset.

        EXAMPLES:

        Since a ring homomorphism maps 1 to 1, there can only be a zero
        morphism when mapping to the trivial ring::

            sage: Hom(ZZ, Zmod(1)).zero()
            Ring morphism:
              From: Integer Ring
              To:   Ring of integers modulo 1
              Defn: 1 |--> 0
            sage: Hom(ZZ, Zmod(2)).zero()
            Traceback (most recent call last):
            ...
            ValueError: homset has no zero element
        """

class RingHomset_quo_ring(RingHomset_generic):
    """
    Space of ring homomorphisms where the domain is a (formal) quotient
    ring.

    EXAMPLES::

        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S.<a,b> = R.quotient(x^2 + y^2)                                           # needs sage.libs.singular
        sage: phi = S.hom([b,a]); phi                                                   # needs sage.libs.singular
        Ring endomorphism of Quotient of Multivariate Polynomial Ring in x, y
         over Rational Field by the ideal (x^2 + y^2)
          Defn: a |--> b
                b |--> a
        sage: phi(a)                                                                    # needs sage.libs.singular
        b
        sage: phi(b)                                                                    # needs sage.libs.singular
        a

    TESTS:

    We test pickling of a homset from a quotient.

    ::

        sage: # needs sage.libs.singular
        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S.<a,b> = R.quotient(x^2 + y^2)
        sage: H = S.Hom(R)
        sage: H == loads(dumps(H))
        True

    We test pickling of actual homomorphisms in a quotient::

        sage: phi = S.hom([b,a])                                                        # needs sage.libs.singular
        sage: phi == loads(dumps(phi))                                                  # needs sage.libs.singular
        True
    """
    Element: Incomplete
