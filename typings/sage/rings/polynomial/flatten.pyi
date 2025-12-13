from .multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from .polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from .polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.categories.homset import Homset as Homset
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.polynomial.polydict import ETuple as ETuple

class FlatteningMorphism(Morphism):
    """
    EXAMPLES::

        sage: R = QQ['a','b']['x','y','z']['t1','t2']
        sage: from sage.rings.polynomial.flatten import FlatteningMorphism
        sage: f = FlatteningMorphism(R)
        sage: f.codomain()
        Multivariate Polynomial Ring in a, b, x, y, z, t1, t2 over Rational Field
        sage: p = R('(a+b)*x + (a^2-b)*t2*(z+y)')
        sage: p
        ((a^2 - b)*y + (a^2 - b)*z)*t2 + (a + b)*x
        sage: f(p)
        a^2*y*t2 + a^2*z*t2 - b*y*t2 - b*z*t2 + a*x + b*x
        sage: f(p).parent()
        Multivariate Polynomial Ring in a, b, x, y, z, t1, t2 over Rational Field

    Also works when univariate polynomial ring are involved::

        sage: R = QQ['x']['y']['s','t']['X']
        sage: from sage.rings.polynomial.flatten import FlatteningMorphism
        sage: f = FlatteningMorphism(R)
        sage: f.codomain()
        Multivariate Polynomial Ring in x, y, s, t, X over Rational Field
        sage: p = R('((x^2 + 1) + (x+2)*y + x*y^3)*(s+t) + x*y*X')
        sage: p
        x*y*X + (x*y^3 + (x + 2)*y + x^2 + 1)*s + (x*y^3 + (x + 2)*y + x^2 + 1)*t
        sage: f(p)
        x*y^3*s + x*y^3*t + x^2*s + x*y*s + x^2*t + x*y*t + x*y*X + 2*y*s + 2*y*t + s + t
        sage: f(p).parent()
        Multivariate Polynomial Ring in x, y, s, t, X over Rational Field
    """
    def __init__(self, domain) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: R = ZZ['a', 'b', 'c']['x', 'y', 'z']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: FlatteningMorphism(R)
            Flattening morphism:
              From: Multivariate Polynomial Ring in x, y, z over Multivariate Polynomial Ring in a, b, c over Integer Ring
              To:   Multivariate Polynomial Ring in a, b, c, x, y, z over Integer Ring

        ::

            sage: R = ZZ['a']['b']['c']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: FlatteningMorphism(R)
            Flattening morphism:
              From: Univariate Polynomial Ring in c over Univariate Polynomial Ring in b over Univariate Polynomial Ring in a over Integer Ring
              To:   Multivariate Polynomial Ring in a, b, c over Integer Ring

        ::

            sage: R = ZZ['a']['a','b']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: FlatteningMorphism(R)
            Flattening morphism:
              From: Multivariate Polynomial Ring in a, b over Univariate Polynomial Ring in a over Integer Ring
              To:   Multivariate Polynomial Ring in a, a0, b over Integer Ring

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<v> = NumberField(x^3 - 2)
            sage: R = K['x','y']['a','b']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: f = FlatteningMorphism(R)
            sage: f(R('v*a*x^2 + b^2 + 1/v*y'))
            v*x^2*a + b^2 + (1/2*v^2)*y

        ::

            sage: # needs sage.rings.number_field
            sage: R = QQbar['x','y']['a','b']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: f = FlatteningMorphism(R)
            sage: f(R('QQbar(sqrt(2))*a*x^2 + b^2 + QQbar(I)*y'))                       # needs sage.symbolic
            1.414213562373095?*x^2*a + b^2 + I*y

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQbar, 1)
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: f = FlatteningMorphism(R)
            sage: f.domain(), f.codomain()
            (Multivariate Polynomial Ring in z over Algebraic Field,
             Multivariate Polynomial Ring in z over Algebraic Field)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQbar)
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: f = FlatteningMorphism(R)
            sage: f.domain(), f.codomain()
            (Univariate Polynomial Ring in z over Algebraic Field,
             Univariate Polynomial Ring in z over Algebraic Field)

        TESTS::

            sage: Pol = QQ['x']['x0']['x']
            sage: fl = FlatteningMorphism(Pol)
            sage: fl
            Flattening morphism:
              From: Univariate Polynomial Ring in x over Univariate Polynomial Ring in x0 over Univariate Polynomial Ring in x over Rational Field
              To:   Multivariate Polynomial Ring in x, x0, x1 over Rational Field
            sage: p = Pol([[[1,2],[3,4]],[[5,6],[7,8]]])
            sage: fl.section()(fl(p)) == p
            True
        """
    @cached_method
    def section(self):
        """
        Inverse of this flattening morphism.

        EXAMPLES::

            sage: R = QQ['a','b','c']['x','y','z']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: h = FlatteningMorphism(R)
            sage: h.section()
            Unflattening morphism:
              From: Multivariate Polynomial Ring in a, b, c, x, y, z over Rational Field
              To:   Multivariate Polynomial Ring in x, y, z
                    over Multivariate Polynomial Ring in a, b, c over Rational Field

        ::

            sage: R = ZZ['a']['b']['c']
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: FlatteningMorphism(R).section()
            Unflattening morphism:
              From: Multivariate Polynomial Ring in a, b, c over Integer Ring
              To:   Univariate Polynomial Ring in c over Univariate Polynomial Ring in b
                    over Univariate Polynomial Ring in a over Integer Ring
        """
    def inverse(self):
        """
        Return the inverse of this flattening morphism.

        This is the same as calling :meth:`section`.

        EXAMPLES::

            sage: f = QQ['x,y']['u,v'].flattening_morphism()
            sage: f.inverse()
            Unflattening morphism:
              From: Multivariate Polynomial Ring in x, y, u, v over Rational Field
              To:   Multivariate Polynomial Ring in u, v
                    over Multivariate Polynomial Ring in x, y over Rational Field
        """

class UnflatteningMorphism(Morphism):
    """
    Inverses for :class:`FlatteningMorphism`.

    EXAMPLES::

        sage: R = QQ['c','x','y','z']
        sage: S = QQ['c']['x','y','z']
        sage: from sage.rings.polynomial.flatten import UnflatteningMorphism
        sage: f = UnflatteningMorphism(R, S)
        sage: g = f(R('x^2 + c*y^2 - z^2'));g
        x^2 + c*y^2 - z^2
        sage: g.parent()
        Multivariate Polynomial Ring in x, y, z
         over Univariate Polynomial Ring in c over Rational Field

    ::

        sage: R = QQ['a','b', 'x','y']
        sage: S = QQ['a','b']['x','y']
        sage: from sage.rings.polynomial.flatten import UnflatteningMorphism
        sage: UnflatteningMorphism(R, S)
        Unflattening morphism:
          From: Multivariate Polynomial Ring in a, b, x, y over Rational Field
          To:   Multivariate Polynomial Ring in x, y
                over Multivariate Polynomial Ring in a, b over Rational Field
    """
    def __init__(self, domain, codomain) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: R = QQ['x']['y']['s','t']['X']
            sage: p = R.random_element()
            sage: from sage.rings.polynomial.flatten import FlatteningMorphism
            sage: f = FlatteningMorphism(R)
            sage: g = f.section()
            sage: g(f(p)) == p
            True

        ::

            sage: R = QQ['a','b','x','y']
            sage: S = ZZ['a','b']['x','z']
            sage: from sage.rings.polynomial.flatten import UnflatteningMorphism
            sage: UnflatteningMorphism(R, S)
            Traceback (most recent call last):
            ...
            ValueError: rings must have same base ring

        ::

            sage: R = QQ['a','b','x','y']
            sage: S = QQ['a','b']['x','z','w']
            sage: from sage.rings.polynomial.flatten import UnflatteningMorphism
            sage: UnflatteningMorphism(R, S)
            Traceback (most recent call last):
            ...
            ValueError: rings must have the same number of variables
        """

class SpecializationMorphism(Morphism):
    """
    Morphisms to specialize parameters in (stacked) polynomial rings.

    EXAMPLES::

        sage: R.<c> = PolynomialRing(QQ)
        sage: S.<x,y,z> = PolynomialRing(R)
        sage: D = dict({c:1})
        sage: from sage.rings.polynomial.flatten import SpecializationMorphism
        sage: f = SpecializationMorphism(S, D)
        sage: g = f(x^2 + c*y^2 - z^2); g
        x^2 + y^2 - z^2
        sage: g.parent()
        Multivariate Polynomial Ring in x, y, z over Rational Field

    ::

        sage: R.<c> = PolynomialRing(QQ)
        sage: S.<z> = PolynomialRing(R)
        sage: from sage.rings.polynomial.flatten import SpecializationMorphism
        sage: xi = SpecializationMorphism(S, {c:0}); xi
        Specialization morphism:
          From: Univariate Polynomial Ring in z
                over Univariate Polynomial Ring in c over Rational Field
          To:   Univariate Polynomial Ring in z over Rational Field
        sage: xi(z^2+c)
        z^2

    ::

        sage: R1.<u,v> = PolynomialRing(QQ)
        sage: R2.<a,b,c> = PolynomialRing(R1)
        sage: S.<x,y,z> = PolynomialRing(R2)
        sage: D = dict({a:1, b:2, x:0, u:1})
        sage: from sage.rings.polynomial.flatten import SpecializationMorphism
        sage: xi = SpecializationMorphism(S, D); xi
        Specialization morphism:
          From: Multivariate Polynomial Ring in x, y, z
                over Multivariate Polynomial Ring in a, b, c
                over Multivariate Polynomial Ring in u, v over Rational Field
          To:   Multivariate Polynomial Ring in y, z over Univariate Polynomial Ring in c
                over Univariate Polynomial Ring in v over Rational Field
        sage: xi(a*(x*z+y^2)*u+b*v*u*(x*z+y^2)*y^2*c+c*y^2*z^2)
        2*v*c*y^4 + c*y^2*z^2 + y^2
    """
    def __init__(self, domain, D) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: S.<x,y> = PolynomialRing(QQ)
            sage: D = dict({x:1})
            sage: from sage.rings.polynomial.flatten import SpecializationMorphism
            sage: phi = SpecializationMorphism(S, D); phi
            Specialization morphism:
              From: Multivariate Polynomial Ring in x, y over Rational Field
              To:   Univariate Polynomial Ring in y over Rational Field
            sage: phi(x^2 + y^2)
            y^2 + 1

        ::

            sage: R.<a,b,c> = PolynomialRing(ZZ)
            sage: S.<x,y,z> = PolynomialRing(R)
            sage: from sage.rings.polynomial.flatten import SpecializationMorphism
            sage: xi = SpecializationMorphism(S, {a:1/2})
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        The following was fixed in :issue:`23811`::

            sage: R.<c> = RR[]
            sage: P.<z> = AffineSpace(R, 1)
            sage: H = End(P)
            sage: f = H([z^2 + c])
            sage: f.specialization({c:1})                                               # needs sage.modules
            Scheme endomorphism of
             Affine Space of dimension 1 over Real Field with 53 bits of precision
              Defn: Defined on coordinates by sending (z) to
                    (z^2 + 1.00000000000000)
        """

class FractionSpecializationMorphism(Morphism):
    """
    A specialization morphism for fraction fields over (stacked) polynomial rings
    """
    def __init__(self, domain, D) -> None:
        """
        Initialize the morphism with a domain and dictionary of specializations.

        EXAMPLES::

            sage: R.<a,c> = QQ[]
            sage: S.<x,y> = R[]
            sage: from sage.rings.polynomial.flatten import FractionSpecializationMorphism
            sage: phi = FractionSpecializationMorphism(Frac(S), {c:3})
            sage: phi
            Fraction Specialization morphism:
              From: Fraction Field of Multivariate Polynomial Ring in x, y
                    over Multivariate Polynomial Ring in a, c over Rational Field
              To:   Fraction Field of Multivariate Polynomial Ring in x, y
                    over Univariate Polynomial Ring in a over Rational Field
        """
