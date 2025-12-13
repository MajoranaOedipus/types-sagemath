import sage as sage
import sage.categories.morphism
import sage.rings.ideal as ideal
from sage.categories.facade_sets import FacadeSets as FacadeSets
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FrobeniusEndomorphism_generic(RingHomomorphism):
    """FrobeniusEndomorphism_generic(domain, n=1)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2957)

    A class implementing Frobenius endomorphisms on rings of prime
    characteristic."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, n=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2962)

                INPUT:

                - ``domain`` -- a ring

                - ``n`` -- nonnegative integer (default: 1)

                OUTPUT:

                The `n`-th power of the absolute (arithmetic) Frobenius
                endomorphism on ``domain``

                TESTS::

                    sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
                    sage: K.<u> = PowerSeriesRing(GF(5))
                    sage: FrobeniusEndomorphism_generic(K)
                    Frobenius endomorphism x |--> x^5 of Power Series Ring in u
                     over Finite Field of size 5
                    sage: FrobeniusEndomorphism_generic(K, 2)
                    Frobenius endomorphism x |--> x^(5^2) of Power Series Ring in u
                     over Finite Field of size 5
        """
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_generic.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 3129)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_generic.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 3129)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_generic.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 3129)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9"""
    def __hash__(self) -> Any:
        """FrobeniusEndomorphism_generic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 3186)

        Return a hash of this morphism.

        It is the hash of the triple (domain, codomain, definition)
        where ``definition`` is:

        - a tuple consisting of the images of the generators
          of the domain if domain has generators

        - the string representation of this morphism otherwise

        AUTHOR:

        - Xavier Caruso (2012-07-09)"""
    def __pow__(self, n, ignored) -> Any:
        """FrobeniusEndomorphism_generic.__pow__(self, n, ignored)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 3147)

        Return the `n`-th iterate of this endomorphism.

        EXAMPLES::

            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: Frob = K.frobenius_endomorphism(); Frob
            Frobenius endomorphism x |--> x^5 of Power Series Ring in u
             over Finite Field of size 5
            sage: Frob^2
            Frobenius endomorphism x |--> x^(5^2) of Power Series Ring in u
             over Finite Field of size 5"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class RingHomomorphism(RingMap):
    """RingHomomorphism(parent)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 633)

    Homomorphism of rings."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 637)

                Initialize ``self``.

                EXAMPLES::

                    sage: f = ZZ.hom(Zp(3)); f                                                  # needs sage.rings.padics
                    Ring morphism:
                      From: Integer Ring
                      To:   3-adic Ring with capped relative precision 20

                TESTS::

                    sage: isinstance(f, sage.rings.morphism.RingHomomorphism)                   # needs sage.rings.padics
                    True
        """
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1402)

        Return the inverse of this ring homomorphism if it exists.

        Raises a :exc:`ZeroDivisionError` if the inverse does not exist.

        ALGORITHM:

        By default, this computes a Gröbner basis of the ideal corresponding to
        the graph of the ring homomorphism.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: f = R.hom([2*t - 1], R)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> 1/2*t + 1/2

        The following non-linear homomorphism is not invertible, but it induces
        an isomorphism on a quotient ring::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = QQ[]
            sage: f = R.hom([y*z, x*z, x*y], R)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: f.is_injective()
            True
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)
            sage: g = Q.hom([y*z, x*z, x*y], Q)
            sage: g.inverse()
            Ring endomorphism of Quotient of Multivariate Polynomial Ring
            in x, y, z over Rational Field by the ideal (x*y*z - 1)
              Defn: x |--> y*z
                    y |--> x*z
                    z |--> x*y

        Homomorphisms over the integers are supported::

            sage: S.<x,y> = ZZ[]
            sage: f = S.hom([x + 2*y, x + 3*y], S)
            sage: f.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> 3*x - 2*y
                    y |--> -x + y
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        The following homomorphism is invertible over the rationals, but not
        over the integers::

            sage: g = S.hom([x + y, x - y - 2], S)
            sage: g.inverse()                                                           # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: R.<x,y> = QQ[x,y]
            sage: h = R.hom([x + y, x - y - 2], R)
            sage: (h.inverse() * h).is_identity()                                       # needs sage.libs.singular
            True

        This example by M. Nagata is a wild automorphism::

            sage: R.<x,y,z> = QQ[]
            sage: sigma = R.hom([x - 2*y*(z*x+y^2) - z*(z*x+y^2)^2,
            ....:                y + z*(z*x+y^2), z], R)
            sage: tau = sigma.inverse(); tau                                            # needs sage.libs.singular
            Ring endomorphism of Multivariate Polynomial Ring in x, y, z over
            Rational Field
              Defn: x |--> -y^4*z - 2*x*y^2*z^2 - x^2*z^3 + 2*y^3 + 2*x*y*z + x
                    y |--> -y^2*z - x*z^2 + y
                    z |--> z
            sage: (tau * sigma).is_identity()                                           # needs sage.libs.singular
            True

        We compute the triangular automorphism that converts moments to
        cumulants, as well as its inverse, using the moment generating
        function. The choice of a term ordering can have a great impact on the
        computation time of a Gröbner basis, so here we choose a weighted
        ordering such that the images of the generators are homogeneous
        polynomials.  ::

            sage: d = 12
            sage: T = TermOrder('wdegrevlex', [1..d])
            sage: R = PolynomialRing(QQ, ['x%s' % j for j in (1..d)], order=T)
            sage: S.<t> = PowerSeriesRing(R)
            sage: egf = S([0] + list(R.gens())).ogf_to_egf().exp(prec=d+1)
            sage: phi = R.hom(egf.egf_to_ogf().list()[1:], R)
            sage: phi.im_gens()[:5]
            [x1,
             x1^2 + x2,
             x1^3 + 3*x1*x2 + x3,
             x1^4 + 6*x1^2*x2 + 3*x2^2 + 4*x1*x3 + x4,
             x1^5 + 10*x1^3*x2 + 15*x1*x2^2 + 10*x1^2*x3 + 10*x2*x3 + 5*x1*x4 + x5]
            sage: all(p.is_homogeneous() for p in phi.im_gens())                        # needs sage.libs.singular
            True
            sage: phi.inverse().im_gens()[:5]                                           # needs sage.libs.singular
            [x1,
             -x1^2 + x2,
             2*x1^3 - 3*x1*x2 + x3,
             -6*x1^4 + 12*x1^2*x2 - 3*x2^2 - 4*x1*x3 + x4,
             24*x1^5 - 60*x1^3*x2 + 30*x1*x2^2 + 20*x1^2*x3 - 10*x2*x3 - 5*x1*x4 + x5]
            sage: (phi.inverse() * phi).is_identity()                                   # needs sage.libs.singular
            True

        Automorphisms of number fields as well as Galois fields are supported::

            sage: K.<zeta7> = CyclotomicField(7)                                        # needs sage.rings.number_field
            sage: c = K.hom([1/zeta7])                                                  # needs sage.rings.number_field
            sage: (c.inverse() * c).is_identity()                                       # needs sage.libs.singular sage.rings.number_field
            True

            sage: F.<t> = GF(7^3)                                                       # needs sage.rings.finite_rings
            sage: f = F.hom(t^7, F)                                                     # needs sage.rings.finite_rings
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular sage.rings.finite_rings
            True

        An isomorphism between the algebraic torus and the circle over a number
        field::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: A.<z,w> = K['z,w'].quotient('z*w - 1')
            sage: B.<x,y> = K['x,y'].quotient('x^2 + y^2 - 1')
            sage: f = A.hom([x + i*y, x - i*y], B)
            sage: g = f.inverse()
            sage: g.morphism_from_cover().im_gens()
            [1/2*z + 1/2*w, (-1/2*i)*z + (1/2*i)*w]
            sage: all(g(f(z)) == z for z in A.gens())
            True

        TESTS:

        Morphisms involving quotient rings::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<s,u,t> = QQ['s,u,t'].quotient('u-t^2')
            sage: f = R.hom([s, -t], S)
            sage: (f.inverse() * f).is_identity()
            True
            sage: Q.<v,w> = R.quotient(x - y^2)
            sage: g = Q.hom([v, -w], Q)
            sage: g.inverse()(g(v)) == v and g.inverse()(g(w)) == w
            True
            sage: S.<z> = QQ[]
            sage: h = Q.hom([z^2, -z], S)
            sage: h.inverse()(h(v)) == v and h.inverse()(h(w)) == w
            True

        Morphisms between number fields and quotient rings::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: f = K.hom([-sqrt2], K.polynomial_quotient_ring())
            sage: (f.inverse() * f).is_identity()
            True
            sage: g = K.polynomial_quotient_ring().hom([-sqrt2], K)
            sage: (g.inverse() * g).is_identity()
            True

        Morphisms involving Galois fields::

            sage: # needs sage.rings.finite_rings
            sage: A.<t> = GF(7^3)
            sage: R = A.polynomial_ring().quotient(A.polynomial())
            sage: g = A.hom(R.gens(), R)
            sage: (g.inverse() * g).is_identity()                                       # needs sage.libs.singular
            True
            sage: B.<T>, f = A.extension(3, map=True)
            sage: f.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not surjective
            sage: B.<T>, f = A.extension(1, map=True)
            sage: f.inverse()
            Ring morphism:
              From: Finite Field in T of size 7^3
              To:   Finite Field in t of size 7^3
              Defn: T |--> t

        Non-injective homomorphisms::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b,c> = QQ[]
            sage: S.hom([x, y, 0], R).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: T.<z> = QQ[]
            sage: R.hom([2*z, 3*z], T).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.<u,v> = R.quotient([x^5, y^4])
            sage: R.hom([u, v], Q).inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective
            sage: Q.cover().inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ring homomorphism not injective

        Univariate quotient rings::

            sage: R.<t> = QQ['t'].quotient('t^5')                                       # needs sage.libs.pari
            sage: f = R.hom([2*t], R)
            sage: (f.inverse() * f).is_identity()                                       # needs sage.libs.singular
            True

        A homomorphism over ``QQbar``::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = R.hom([x + QQbar(I)*y^2, -y], R)                                  # needs sage.rings.number_field
            sage: (f.inverse() * f).is_identity()                                       # needs sage.rings.number_field
            True

        Check that results are cached::

            sage: R.<x,y> = GF(823)[]
            sage: f = R.hom([x, y + x^2], R)
            sage: f.inverse() is f.inverse()                                            # needs sage.libs.singular
            True

        Some subclasses of ring homomorphisms are not supported::

            sage: from sage.rings.morphism import FrobeniusEndomorphism_generic
            sage: K.<u> = PowerSeriesRing(GF(5))
            sage: FrobeniusEndomorphism_generic(K).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)                                   # needs sage.modules
            sage: R.hom([y, x], R).inverse()                                            # needs sage.libs.singular sage.modules
            Traceback (most recent call last):
            ...
            NotImplementedError

        ::

            sage: K.<x> = FunctionField(QQ)
            sage: K.hom(1/x).inverse()
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse not implemented...

        The implementation performs several computations that require a Gröbner
        basis of the graph ideal, so we check that the Gröbner basis is cached
        after the first such computation::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x + 123*y^2, y], R)
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()
            False
            sage: f.is_injective()                                                      # needs sage.libs.singular
            True
            sage: f._graph_ideal()[0].groebner_basis.is_in_cache()                      # needs sage.libs.singular
            True

        Check case where domain is quotient ring and codomain a finite field of same characteristic. Fixes (:issue:`39690`)::

            sage: F4.<a> = GF(2^2, modulus=[1,1,1])
            sage: PR.<y> = PolynomialRing(F4)
            sage: IP = y^3 + y + 1
            sage: assert IP.is_irreducible()
            sage: Q.<w> = PR.quotient(IP)
            sage: SF.<z> = IP.splitting_field()
            sage: SF
            Finite Field in z of size 2^6
            sage: r = z^4 + z^2 + z + 1
            sage: assert IP.change_ring(SF)(r) == 0
            sage: f = Q.hom([r,], SF)
            sage: f
            Ring morphism:
                From: Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
                To:   Finite Field in z of size 2^6
                Defn: w |--> z^4 + z^2 + z + 1
            sage: f.inverse()                   # indirect doctest
            Ring morphism:
              From: Finite Field in z of size 2^6
              To:   Univariate Quotient Polynomial Ring in w over Finite Field in a of size 2^2 with modulus y^3 + y + 1
              Defn: z |--> (a + 1)*w^2 + a*w + 1"""
    @overload
    def inverse_image(self, I) -> Any:
        """RingHomomorphism.inverse_image(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 902)

        Return the inverse image of an ideal or an element in the codomain
        of this ring homomorphism.

        INPUT:

        - ``I`` -- an ideal or element in the codomain

        OUTPUT:

        For an ideal `I` in the codomain, this returns the largest ideal in the
        domain whose image is contained in `I`.

        Given an element `b` in the codomain, this returns an arbitrary element
        `a` in the domain such that ``self(a) = b`` if one such exists.
        The element `a` is unique if this ring homomorphism is injective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: S.<u,v> = QQ[]
            sage: f = R.hom([u^2, u*v, v^2], S)
            sage: I = S.ideal([u^6, u^5*v, u^4*v^2, u^3*v^3])
            sage: J = f.inverse_image(I); J                                             # needs sage.libs.singular
            Ideal (y^2 - x*z, x*y*z, x^2*z, x^2*y, x^3)
            of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f(J) == I                                                             # needs sage.libs.singular
            True

        Under the above homomorphism, there exists an inverse image for
        every element that only involves monomials of even degree::

            sage: [f.inverse_image(p) for p in [u^2, u^4, u*v + u^3*v^3]]               # needs sage.libs.singular
            [x, x^2, x*y*z + y]
            sage: f.inverse_image(u*v^2)                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: element u*v^2 does not have preimage

        The image of the inverse image ideal can be strictly smaller than the
        original ideal::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: S.<u,v> = QQ['u,v'].quotient('v^2 - 2')
            sage: f = QuadraticField(2).hom([v], S)
            sage: I = S.ideal(u + v)
            sage: J = f.inverse_image(I)
            sage: J.is_zero()
            True
            sage: f(J) < I
            True

        Fractional ideals are not yet fully supported::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(QQ['x']('x^2+2'))
            sage: f = K.hom([-a], K)
            sage: I = K.ideal([a + 1])
            sage: f.inverse_image(I)                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse image not implemented...
            sage: f.inverse_image(K.ideal(0)).is_zero()                                 # needs sage.libs.singular
            True
            sage: f.inverse()(I)                                                        # needs sage.rings.padics
            Fractional ideal (-a + 1)

        ALGORITHM:

        By default, this computes a Gröbner basis of an ideal related to the
        graph of the ring homomorphism.

        REFERENCES:

        - Proposition 2.5.12 [DS2009]_

        TESTS::

            sage: ZZ.hom(Zp(2)).inverse_image(ZZ.ideal(2))                              # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: not an ideal or element in codomain 2-adic Ring
            with capped relative precision 20

        ::

            sage: ZZ.hom(Zp(2)).inverse_image(Zp(2).ideal(2))                           # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def inverse_image(self, I) -> Any:
        """RingHomomorphism.inverse_image(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 902)

        Return the inverse image of an ideal or an element in the codomain
        of this ring homomorphism.

        INPUT:

        - ``I`` -- an ideal or element in the codomain

        OUTPUT:

        For an ideal `I` in the codomain, this returns the largest ideal in the
        domain whose image is contained in `I`.

        Given an element `b` in the codomain, this returns an arbitrary element
        `a` in the domain such that ``self(a) = b`` if one such exists.
        The element `a` is unique if this ring homomorphism is injective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: S.<u,v> = QQ[]
            sage: f = R.hom([u^2, u*v, v^2], S)
            sage: I = S.ideal([u^6, u^5*v, u^4*v^2, u^3*v^3])
            sage: J = f.inverse_image(I); J                                             # needs sage.libs.singular
            Ideal (y^2 - x*z, x*y*z, x^2*z, x^2*y, x^3)
            of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f(J) == I                                                             # needs sage.libs.singular
            True

        Under the above homomorphism, there exists an inverse image for
        every element that only involves monomials of even degree::

            sage: [f.inverse_image(p) for p in [u^2, u^4, u*v + u^3*v^3]]               # needs sage.libs.singular
            [x, x^2, x*y*z + y]
            sage: f.inverse_image(u*v^2)                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: element u*v^2 does not have preimage

        The image of the inverse image ideal can be strictly smaller than the
        original ideal::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: S.<u,v> = QQ['u,v'].quotient('v^2 - 2')
            sage: f = QuadraticField(2).hom([v], S)
            sage: I = S.ideal(u + v)
            sage: J = f.inverse_image(I)
            sage: J.is_zero()
            True
            sage: f(J) < I
            True

        Fractional ideals are not yet fully supported::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(QQ['x']('x^2+2'))
            sage: f = K.hom([-a], K)
            sage: I = K.ideal([a + 1])
            sage: f.inverse_image(I)                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse image not implemented...
            sage: f.inverse_image(K.ideal(0)).is_zero()                                 # needs sage.libs.singular
            True
            sage: f.inverse()(I)                                                        # needs sage.rings.padics
            Fractional ideal (-a + 1)

        ALGORITHM:

        By default, this computes a Gröbner basis of an ideal related to the
        graph of the ring homomorphism.

        REFERENCES:

        - Proposition 2.5.12 [DS2009]_

        TESTS::

            sage: ZZ.hom(Zp(2)).inverse_image(ZZ.ideal(2))                              # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: not an ideal or element in codomain 2-adic Ring
            with capped relative precision 20

        ::

            sage: ZZ.hom(Zp(2)).inverse_image(Zp(2).ideal(2))                           # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def inverse_image(self, p) -> Any:
        """RingHomomorphism.inverse_image(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 902)

        Return the inverse image of an ideal or an element in the codomain
        of this ring homomorphism.

        INPUT:

        - ``I`` -- an ideal or element in the codomain

        OUTPUT:

        For an ideal `I` in the codomain, this returns the largest ideal in the
        domain whose image is contained in `I`.

        Given an element `b` in the codomain, this returns an arbitrary element
        `a` in the domain such that ``self(a) = b`` if one such exists.
        The element `a` is unique if this ring homomorphism is injective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: S.<u,v> = QQ[]
            sage: f = R.hom([u^2, u*v, v^2], S)
            sage: I = S.ideal([u^6, u^5*v, u^4*v^2, u^3*v^3])
            sage: J = f.inverse_image(I); J                                             # needs sage.libs.singular
            Ideal (y^2 - x*z, x*y*z, x^2*z, x^2*y, x^3)
            of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f(J) == I                                                             # needs sage.libs.singular
            True

        Under the above homomorphism, there exists an inverse image for
        every element that only involves monomials of even degree::

            sage: [f.inverse_image(p) for p in [u^2, u^4, u*v + u^3*v^3]]               # needs sage.libs.singular
            [x, x^2, x*y*z + y]
            sage: f.inverse_image(u*v^2)                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: element u*v^2 does not have preimage

        The image of the inverse image ideal can be strictly smaller than the
        original ideal::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: S.<u,v> = QQ['u,v'].quotient('v^2 - 2')
            sage: f = QuadraticField(2).hom([v], S)
            sage: I = S.ideal(u + v)
            sage: J = f.inverse_image(I)
            sage: J.is_zero()
            True
            sage: f(J) < I
            True

        Fractional ideals are not yet fully supported::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(QQ['x']('x^2+2'))
            sage: f = K.hom([-a], K)
            sage: I = K.ideal([a + 1])
            sage: f.inverse_image(I)                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse image not implemented...
            sage: f.inverse_image(K.ideal(0)).is_zero()                                 # needs sage.libs.singular
            True
            sage: f.inverse()(I)                                                        # needs sage.rings.padics
            Fractional ideal (-a + 1)

        ALGORITHM:

        By default, this computes a Gröbner basis of an ideal related to the
        graph of the ring homomorphism.

        REFERENCES:

        - Proposition 2.5.12 [DS2009]_

        TESTS::

            sage: ZZ.hom(Zp(2)).inverse_image(ZZ.ideal(2))                              # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: not an ideal or element in codomain 2-adic Ring
            with capped relative precision 20

        ::

            sage: ZZ.hom(Zp(2)).inverse_image(Zp(2).ideal(2))                           # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def inverse_image(self, I) -> Any:
        """RingHomomorphism.inverse_image(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 902)

        Return the inverse image of an ideal or an element in the codomain
        of this ring homomorphism.

        INPUT:

        - ``I`` -- an ideal or element in the codomain

        OUTPUT:

        For an ideal `I` in the codomain, this returns the largest ideal in the
        domain whose image is contained in `I`.

        Given an element `b` in the codomain, this returns an arbitrary element
        `a` in the domain such that ``self(a) = b`` if one such exists.
        The element `a` is unique if this ring homomorphism is injective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: S.<u,v> = QQ[]
            sage: f = R.hom([u^2, u*v, v^2], S)
            sage: I = S.ideal([u^6, u^5*v, u^4*v^2, u^3*v^3])
            sage: J = f.inverse_image(I); J                                             # needs sage.libs.singular
            Ideal (y^2 - x*z, x*y*z, x^2*z, x^2*y, x^3)
            of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f(J) == I                                                             # needs sage.libs.singular
            True

        Under the above homomorphism, there exists an inverse image for
        every element that only involves monomials of even degree::

            sage: [f.inverse_image(p) for p in [u^2, u^4, u*v + u^3*v^3]]               # needs sage.libs.singular
            [x, x^2, x*y*z + y]
            sage: f.inverse_image(u*v^2)                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: element u*v^2 does not have preimage

        The image of the inverse image ideal can be strictly smaller than the
        original ideal::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: S.<u,v> = QQ['u,v'].quotient('v^2 - 2')
            sage: f = QuadraticField(2).hom([v], S)
            sage: I = S.ideal(u + v)
            sage: J = f.inverse_image(I)
            sage: J.is_zero()
            True
            sage: f(J) < I
            True

        Fractional ideals are not yet fully supported::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(QQ['x']('x^2+2'))
            sage: f = K.hom([-a], K)
            sage: I = K.ideal([a + 1])
            sage: f.inverse_image(I)                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse image not implemented...
            sage: f.inverse_image(K.ideal(0)).is_zero()                                 # needs sage.libs.singular
            True
            sage: f.inverse()(I)                                                        # needs sage.rings.padics
            Fractional ideal (-a + 1)

        ALGORITHM:

        By default, this computes a Gröbner basis of an ideal related to the
        graph of the ring homomorphism.

        REFERENCES:

        - Proposition 2.5.12 [DS2009]_

        TESTS::

            sage: ZZ.hom(Zp(2)).inverse_image(ZZ.ideal(2))                              # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: not an ideal or element in codomain 2-adic Ring
            with capped relative precision 20

        ::

            sage: ZZ.hom(Zp(2)).inverse_image(Zp(2).ideal(2))                           # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def inverse_image(self, I) -> Any:
        """RingHomomorphism.inverse_image(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 902)

        Return the inverse image of an ideal or an element in the codomain
        of this ring homomorphism.

        INPUT:

        - ``I`` -- an ideal or element in the codomain

        OUTPUT:

        For an ideal `I` in the codomain, this returns the largest ideal in the
        domain whose image is contained in `I`.

        Given an element `b` in the codomain, this returns an arbitrary element
        `a` in the domain such that ``self(a) = b`` if one such exists.
        The element `a` is unique if this ring homomorphism is injective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: S.<u,v> = QQ[]
            sage: f = R.hom([u^2, u*v, v^2], S)
            sage: I = S.ideal([u^6, u^5*v, u^4*v^2, u^3*v^3])
            sage: J = f.inverse_image(I); J                                             # needs sage.libs.singular
            Ideal (y^2 - x*z, x*y*z, x^2*z, x^2*y, x^3)
            of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f(J) == I                                                             # needs sage.libs.singular
            True

        Under the above homomorphism, there exists an inverse image for
        every element that only involves monomials of even degree::

            sage: [f.inverse_image(p) for p in [u^2, u^4, u*v + u^3*v^3]]               # needs sage.libs.singular
            [x, x^2, x*y*z + y]
            sage: f.inverse_image(u*v^2)                                                # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: element u*v^2 does not have preimage

        The image of the inverse image ideal can be strictly smaller than the
        original ideal::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: S.<u,v> = QQ['u,v'].quotient('v^2 - 2')
            sage: f = QuadraticField(2).hom([v], S)
            sage: I = S.ideal(u + v)
            sage: J = f.inverse_image(I)
            sage: J.is_zero()
            True
            sage: f(J) < I
            True

        Fractional ideals are not yet fully supported::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(QQ['x']('x^2+2'))
            sage: f = K.hom([-a], K)
            sage: I = K.ideal([a + 1])
            sage: f.inverse_image(I)                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            NotImplementedError: inverse image not implemented...
            sage: f.inverse_image(K.ideal(0)).is_zero()                                 # needs sage.libs.singular
            True
            sage: f.inverse()(I)                                                        # needs sage.rings.padics
            Fractional ideal (-a + 1)

        ALGORITHM:

        By default, this computes a Gröbner basis of an ideal related to the
        graph of the ring homomorphism.

        REFERENCES:

        - Proposition 2.5.12 [DS2009]_

        TESTS::

            sage: ZZ.hom(Zp(2)).inverse_image(ZZ.ideal(2))                              # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: not an ideal or element in codomain 2-adic Ring
            with capped relative precision 20

        ::

            sage: ZZ.hom(Zp(2)).inverse_image(Zp(2).ideal(2))                           # needs sage.rings.padics
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def is_invertible(self) -> Any:
        """RingHomomorphism.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1742)

        Return whether this ring homomorphism is bijective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_invertible()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: Q.hom([y*z, x*z, x*y], Q).is_invertible()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def is_invertible(self) -> Any:
        """RingHomomorphism.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1742)

        Return whether this ring homomorphism is bijective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_invertible()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: Q.hom([y*z, x*z, x*y], Q).is_invertible()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def is_invertible(self) -> Any:
        """RingHomomorphism.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1742)

        Return whether this ring homomorphism is bijective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_invertible()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: Q.hom([y*z, x*z, x*y], Q).is_invertible()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def is_surjective(self) -> Any:
        """RingHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1718)

        Return whether this ring homomorphism is surjective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_surjective()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: R.hom([y*z, x*z, x*y], Q).is_surjective()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def is_surjective(self) -> Any:
        """RingHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1718)

        Return whether this ring homomorphism is surjective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_surjective()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: R.hom([y*z, x*z, x*y], Q).is_surjective()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def is_surjective(self) -> Any:
        """RingHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1718)

        Return whether this ring homomorphism is surjective.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.hom([y*z, x*z, x*y], R).is_surjective()                             # needs sage.libs.singular
            False
            sage: Q.<x,y,z> = R.quotient(x*y*z - 1)                                     # needs sage.libs.singular
            sage: R.hom([y*z, x*z, x*y], Q).is_surjective()                             # needs sage.libs.singular
            True

        ALGORITHM:

        By default, this requires the computation of a Gröbner basis."""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1196)

        Return the kernel ideal of this ring homomorphism.

        EXAMPLES::

            sage: A.<x,y> = QQ[]
            sage: B.<t> = QQ[]
            sage: f = A.hom([t^4, t^3 - t^2], B)
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (y^4 - x^3 + 4*x^2*y - 2*x*y^2 + x^2)
            of Multivariate Polynomial Ring in x, y over Rational Field

        We express a Veronese subring of a polynomial ring as a quotient ring::

            sage: A.<a,b,c,d> = QQ[]
            sage: B.<u,v> = QQ[]
            sage: f = A.hom([u^3, u^2*v, u*v^2, v^3], B)
            sage: f.kernel() == A.ideal(matrix.hankel([a, b, c], [d]).minors(2))        # needs sage.libs.singular
            True
            sage: Q = A.quotient(f.kernel())                                            # needs sage.libs.singular
            sage: Q.hom(f.im_gens(), B).is_injective()                                  # needs sage.libs.singular
            True

        The Steiner-Roman surface::

            sage: R.<x,y,z> = QQ[]
            sage: S = R.quotient(x^2 + y^2 + z^2 - 1)
            sage: f = R.hom([x*y, x*z, y*z], S)                                         # needs sage.libs.singular
            sage: f.kernel()                                                            # needs sage.libs.singular
            Ideal (x^2*y^2 + x^2*z^2 + y^2*z^2 - x*y*z)
             of Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS:

        The results are cached::

            sage: f.kernel() is f.kernel()                                              # needs sage.libs.singular
            True

        A degenerate case::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([0, 0], R.quotient(1))                                      # needs sage.libs.singular
            sage: f.kernel().is_one()                                                   # needs sage.libs.singular
            True

        ::

            sage: K.<sqrt2> = QuadraticField(2)                                         # needs sage.rings.number_field
            sage: K.hom([-sqrt2], K).kernel().is_zero()                                 # needs sage.libs.singular sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<a> = QuadraticField(2)
            sage: B.<b> = A.extension(A['b']('b^2-3'))
            sage: C.<c> = B.absolute_field()
            sage: A.hom([B(a)], C).kernel().is_zero()                                   # needs sage.libs.singular
            True
            sage: A.hom([a], B).kernel()
            Traceback (most recent call last):
            ...
            NotImplementedError: base rings must be equal"""
    @overload
    def lift(self, x=...) -> Any:
        """RingHomomorphism.lift(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1265)

        Return a lifting map associated to this homomorphism, if
        it has been defined.

        If ``x`` is not ``None``, return the value of the lift morphism on
        ``x``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x,x])
            sage: f(x+y)
            2*x
            sage: f.lift()
            Traceback (most recent call last):
            ...
            ValueError: no lift map defined
            sage: g = R.hom(R)
            sage: f._set_lift(g)
            sage: f.lift() == g
            True
            sage: f.lift(x)
            x"""
    @overload
    def lift(self) -> Any:
        """RingHomomorphism.lift(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1265)

        Return a lifting map associated to this homomorphism, if
        it has been defined.

        If ``x`` is not ``None``, return the value of the lift morphism on
        ``x``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x,x])
            sage: f(x+y)
            2*x
            sage: f.lift()
            Traceback (most recent call last):
            ...
            ValueError: no lift map defined
            sage: g = R.hom(R)
            sage: f._set_lift(g)
            sage: f.lift() == g
            True
            sage: f.lift(x)
            x"""
    @overload
    def lift(self) -> Any:
        """RingHomomorphism.lift(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1265)

        Return a lifting map associated to this homomorphism, if
        it has been defined.

        If ``x`` is not ``None``, return the value of the lift morphism on
        ``x``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x,x])
            sage: f(x+y)
            2*x
            sage: f.lift()
            Traceback (most recent call last):
            ...
            ValueError: no lift map defined
            sage: g = R.hom(R)
            sage: f._set_lift(g)
            sage: f.lift() == g
            True
            sage: f.lift(x)
            x"""
    @overload
    def lift(self, x) -> Any:
        """RingHomomorphism.lift(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1265)

        Return a lifting map associated to this homomorphism, if
        it has been defined.

        If ``x`` is not ``None``, return the value of the lift morphism on
        ``x``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x,x])
            sage: f(x+y)
            2*x
            sage: f.lift()
            Traceback (most recent call last):
            ...
            ValueError: no lift map defined
            sage: g = R.hom(R)
            sage: f._set_lift(g)
            sage: f.lift() == g
            True
            sage: f.lift(x)
            x"""
    def pushforward(self, I) -> Any:
        """RingHomomorphism.pushforward(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 885)

        Return the pushforward of the ideal `I` under this ring
        homomorphism.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<xx,yy> = R.quo([x^2, y^2]); f = S.cover()          # needs sage.libs.singular
            sage: f.pushforward(R.ideal([x, 3*x + x*y + y^2]))                          # needs sage.libs.singular
            Ideal (xx, xx*yy + 3*xx) of Quotient of Multivariate Polynomial Ring
             in x, y over Rational Field by the ideal (x^2, y^2)"""
    def __invert__(self) -> Any:
        """RingHomomorphism.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1703)

        Return the inverse of this ring homomorphism if it exists.

        This simply calls :meth:`inverse`.

        EXAMPLES::

            sage: R.<x,y> = GF(17)[]
            sage: f = R.hom([3*x, y + x^2 + x^3], R)
            sage: (f * ~f).is_identity()                                                # needs sage.libs.singular
            True"""

class RingHomomorphism_cover(RingHomomorphism):
    """RingHomomorphism_cover(parent)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2547)

    A homomorphism induced by quotienting a ring out by an ideal.

    EXAMPLES::

        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S.<a,b> = R.quo(x^2 + y^2)                                                # needs sage.libs.singular
        sage: phi = S.cover(); phi                                                      # needs sage.libs.singular
        Ring morphism:
          From: Multivariate Polynomial Ring in x, y over Rational Field
          To:   Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                by the ideal (x^2 + y^2)
          Defn: Natural quotient map
        sage: phi(x + y)                                                                # needs sage.libs.singular
        a + b"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2564)

                Create a covering ring homomorphism, induced by quotienting out by an
                ideal.

                EXAMPLES::

                    sage: f = Zmod(6).cover(); f    # implicit test
                    Ring morphism:
                      From: Integer Ring
                      To:   Ring of integers modulo 6
                      Defn: Natural quotient map
                    sage: type(f)
                    <class 'sage.rings.morphism.RingHomomorphism_cover'>
        """
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism_cover.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2627)

        Return the kernel of this covering morphism, which is the ideal that
        was quotiented out by.

        EXAMPLES::

            sage: f = Zmod(6).cover()
            sage: f.kernel()
            Principal ideal (6) of Integer Ring"""
    @overload
    def kernel(self) -> Any:
        """RingHomomorphism_cover.kernel(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2627)

        Return the kernel of this covering morphism, which is the ideal that
        was quotiented out by.

        EXAMPLES::

            sage: f = Zmod(6).cover()
            sage: f.kernel()
            Principal ideal (6) of Integer Ring"""
    def __hash__(self) -> Any:
        """RingHomomorphism_cover.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2661)

        Return the hash of this morphism.

        TESTS::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S.<a,b> = R.quo(x^2 + y^2)
            sage: phi = S.cover()
            sage: type(phi)
            <class 'sage.rings.morphism.RingHomomorphism_cover'>
            sage: hash(phi) == hash(phi)
            True
            sage: {phi: 1}[phi]
            1"""

class RingHomomorphism_from_base(RingHomomorphism):
    """RingHomomorphism_from_base(parent, underlying)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2076)

    A ring homomorphism determined by a ring homomorphism of the base ring.

    AUTHOR:

    - Simon King (initial version, 2010-04-30)

    EXAMPLES:

    We define two polynomial rings and a ring homomorphism::

        sage: R.<x,y> = QQ[]
        sage: S.<z> = QQ[]
        sage: f = R.hom([2*z,3*z],S)

    Now we construct polynomial rings based on ``R`` and ``S``, and let
    ``f`` act on the coefficients::

        sage: PR.<t> = R[]
        sage: PS = S['t']
        sage: Pf = PR.hom(f,PS)
        sage: Pf
        Ring morphism:
          From: Univariate Polynomial Ring in t
                over Multivariate Polynomial Ring in x, y over Rational Field
          To:   Univariate Polynomial Ring in t
                over Univariate Polynomial Ring in z over Rational Field
          Defn: Induced from base ring by
                Ring morphism:
                  From: Multivariate Polynomial Ring in x, y over Rational Field
                  To:   Univariate Polynomial Ring in z over Rational Field
                  Defn: x |--> 2*z
                        y |--> 3*z
        sage: p = (x - 4*y + 1/13)*t^2 + (1/2*x^2 - 1/3*y^2)*t + 2*y^2 + x
        sage: Pf(p)
        (-10*z + 1/13)*t^2 - z^2*t + 18*z^2 + 2*z

    Similarly, we can construct the induced homomorphism on a matrix ring over
    our polynomial rings::

        sage: # needs sage.modules
        sage: MR = MatrixSpace(R, 2, 2)
        sage: MS = MatrixSpace(S, 2, 2)
        sage: M = MR([x^2 + 1/7*x*y - y^2, -1/2*y^2 + 2*y + 1/6,
        ....:         4*x^2 - 14*x, 1/2*y^2 + 13/4*x - 2/11*y])
        sage: Mf = MR.hom(f, MS)
        sage: Mf
        Ring morphism:
          From: Full MatrixSpace of 2 by 2 dense matrices
                over Multivariate Polynomial Ring in x, y over Rational Field
          To:   Full MatrixSpace of 2 by 2 dense matrices
                over Univariate Polynomial Ring in z over Rational Field
          Defn: Induced from base ring by
                Ring morphism:
                  From: Multivariate Polynomial Ring in x, y over Rational Field
                  To:   Univariate Polynomial Ring in z over Rational Field
                  Defn: x |--> 2*z
                        y |--> 3*z
        sage: Mf(M)
        [           -29/7*z^2 -9/2*z^2 + 6*z + 1/6]
        [       16*z^2 - 28*z   9/2*z^2 + 131/22*z]

    The construction of induced homomorphisms is recursive, and so we have::

        sage: # needs sage.modules
        sage: MPR = MatrixSpace(PR, 2)
        sage: MPS = MatrixSpace(PS, 2)
        sage: M = MPR([(-x + y)*t^2 + 58*t - 3*x^2 + x*y,
        ....:          (- 1/7*x*y - 1/40*x)*t^2 + (5*x^2 + y^2)*t + 2*y,
        ....:          (- 1/3*y + 1)*t^2 + 1/3*x*y + y^2 + 5/2*y + 1/4,
        ....:          (x + 6*y + 1)*t^2])
        sage: MPf = MPR.hom(f, MPS); MPf
        Ring morphism:
          From: Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial
                Ring in t over Multivariate Polynomial Ring in x, y over Rational Field
          To:   Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial
                Ring in t over Univariate Polynomial Ring in z over Rational Field
          Defn: Induced from base ring by
                Ring morphism:
                  From: Univariate Polynomial Ring in t
                        over Multivariate Polynomial Ring in x, y over Rational Field
                  To:   Univariate Polynomial Ring in t
                        over Univariate Polynomial Ring in z over Rational Field
                  Defn: Induced from base ring by
                        Ring morphism:
                          From: Multivariate Polynomial Ring in x, y over Rational Field
                          To:   Univariate Polynomial Ring in z over Rational Field
                          Defn: x |--> 2*z
                                y |--> 3*z
        sage: MPf(M)
        [                    z*t^2 + 58*t - 6*z^2 (-6/7*z^2 - 1/20*z)*t^2 + 29*z^2*t + 6*z]
        [    (-z + 1)*t^2 + 11*z^2 + 15/2*z + 1/4                           (20*z + 1)*t^2]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, underlying) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2170)

                Initialize ``self``.

                TESTS::

                    sage: from sage.rings.morphism import RingHomomorphism_from_base
                    sage: R.<x> = ZZ[]
                    sage: f = R.hom([2*x], R)
                    sage: P = MatrixSpace(R, 2).Hom(MatrixSpace(R, 2))                          # needs sage.modules
                    sage: g = RingHomomorphism_from_base(P, f)                                  # needs sage.modules
                    sage: g                                                                     # needs sage.modules
                    Ring endomorphism of Full MatrixSpace of 2 by 2 dense matrices
                     over Univariate Polynomial Ring in x over Integer Ring
                      Defn: Induced from base ring by
                            Ring endomorphism of Univariate Polynomial Ring in x over Integer Ring
                              Defn: x |--> 2*x

                Note that an induced homomorphism only makes sense if domain and
                codomain are constructed in a compatible way. So, the following
                results in an error::

                    sage: P = MatrixSpace(R, 2).Hom(R['t'])                                     # needs sage.modules
                    sage: g = RingHomomorphism_from_base(P, f)                                  # needs sage.modules
                    Traceback (most recent call last):
                    ...
                    ValueError: domain (Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Integer Ring)
                     and codomain (Univariate Polynomial Ring in t over Univariate Polynomial Ring in x over Integer Ring)
                     must have the same functorial construction over their base rings
        """
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism_from_base.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2397)

        Return the inverse of this ring homomorphism if the underlying
        homomorphism of the base ring is invertible.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = QQ[]
            sage: f = R.hom([a + b, a - b], S)
            sage: PR.<t> = R[]
            sage: PS = S['t']
            sage: Pf = PR.hom(f, PS)
            sage: Pf.inverse()                                                          # needs sage.libs.singular
            Ring morphism:
              From: Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in a, b over Rational Field
              To:   Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in x, y over Rational Field
              Defn: Induced from base ring by
                    Ring morphism:
                      From: Multivariate Polynomial Ring in a, b over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
                      Defn: a |--> 1/2*x + 1/2*y
                            b |--> 1/2*x - 1/2*y
            sage: Pf.inverse()(Pf(x*t^2 + y*t))                                         # needs sage.libs.singular
            x*t^2 + y*t"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism_from_base.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2397)

        Return the inverse of this ring homomorphism if the underlying
        homomorphism of the base ring is invertible.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = QQ[]
            sage: f = R.hom([a + b, a - b], S)
            sage: PR.<t> = R[]
            sage: PS = S['t']
            sage: Pf = PR.hom(f, PS)
            sage: Pf.inverse()                                                          # needs sage.libs.singular
            Ring morphism:
              From: Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in a, b over Rational Field
              To:   Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in x, y over Rational Field
              Defn: Induced from base ring by
                    Ring morphism:
                      From: Multivariate Polynomial Ring in a, b over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
                      Defn: a |--> 1/2*x + 1/2*y
                            b |--> 1/2*x - 1/2*y
            sage: Pf.inverse()(Pf(x*t^2 + y*t))                                         # needs sage.libs.singular
            x*t^2 + y*t"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism_from_base.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2397)

        Return the inverse of this ring homomorphism if the underlying
        homomorphism of the base ring is invertible.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = QQ[]
            sage: f = R.hom([a + b, a - b], S)
            sage: PR.<t> = R[]
            sage: PS = S['t']
            sage: Pf = PR.hom(f, PS)
            sage: Pf.inverse()                                                          # needs sage.libs.singular
            Ring morphism:
              From: Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in a, b over Rational Field
              To:   Univariate Polynomial Ring in t over Multivariate
                    Polynomial Ring in x, y over Rational Field
              Defn: Induced from base ring by
                    Ring morphism:
                      From: Multivariate Polynomial Ring in a, b over Rational Field
                      To:   Multivariate Polynomial Ring in x, y over Rational Field
                      Defn: a |--> 1/2*x + 1/2*y
                            b |--> 1/2*x - 1/2*y
            sage: Pf.inverse()(Pf(x*t^2 + y*t))                                         # needs sage.libs.singular
            x*t^2 + y*t"""
    @overload
    def underlying_map(self) -> Any:
        """RingHomomorphism_from_base.underlying_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2209)

        Return the underlying homomorphism of the base ring.

        EXAMPLES::

            sage: # needs sage.modules
            sage: R.<x,y> = QQ[]
            sage: S.<z> = QQ[]
            sage: f = R.hom([2*z, 3*z], S)
            sage: MR = MatrixSpace(R, 2)
            sage: MS = MatrixSpace(S, 2)
            sage: g = MR.hom(f, MS)
            sage: g.underlying_map() == f
            True"""
    @overload
    def underlying_map(self) -> Any:
        """RingHomomorphism_from_base.underlying_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2209)

        Return the underlying homomorphism of the base ring.

        EXAMPLES::

            sage: # needs sage.modules
            sage: R.<x,y> = QQ[]
            sage: S.<z> = QQ[]
            sage: f = R.hom([2*z, 3*z], S)
            sage: MR = MatrixSpace(R, 2)
            sage: MS = MatrixSpace(S, 2)
            sage: g = MR.hom(f, MS)
            sage: g.underlying_map() == f
            True"""

class RingHomomorphism_from_fraction_field(RingHomomorphism):
    """RingHomomorphism_from_fraction_field(parent, morphism)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2429)

    Morphisms between fraction fields.

    TESTS::

        sage: S.<x> = QQ[]
        sage: f = S.hom([x^2])
        sage: g = f.extend_to_fraction_field()                                          # needs sage.libs.singular
        sage: type(g)                                                                   # needs sage.libs.singular
        <class 'sage.rings.morphism.RingHomomorphism_from_fraction_field'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, morphism) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2441)

                Initialize this morphism.

                TESTS::

                    sage: # needs sage.rings.number_field
                    sage: x = polygen(ZZ, 'x')
                    sage: A.<a> = ZZ.extension(x^2 - 2)
                    sage: f = A.coerce_map_from(ZZ)
                    sage: g = f.extend_to_fraction_field()   # indirect doctest
                    sage: g
                    Ring morphism:
                      From: Rational Field
                      To:   Number Field in a with defining polynomial x^2 - 2
        """
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism_from_fraction_field.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2529)

        Return the inverse of this ring homomorphism if it exists.

        EXAMPLES::

            sage: S.<x> = QQ[]
            sage: f = S.hom([2*x - 1])
            sage: g = f.extend_to_fraction_field()                                      # needs sage.libs.singular
            sage: g.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Fraction Field of Univariate Polynomial Ring
             in x over Rational Field
              Defn: x |--> 1/2*x + 1/2"""
    @overload
    def inverse(self) -> Any:
        """RingHomomorphism_from_fraction_field.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2529)

        Return the inverse of this ring homomorphism if it exists.

        EXAMPLES::

            sage: S.<x> = QQ[]
            sage: f = S.hom([2*x - 1])
            sage: g = f.extend_to_fraction_field()                                      # needs sage.libs.singular
            sage: g.inverse()                                                           # needs sage.libs.singular
            Ring endomorphism of Fraction Field of Univariate Polynomial Ring
             in x over Rational Field
              Defn: x |--> 1/2*x + 1/2"""

class RingHomomorphism_from_quotient(RingHomomorphism):
    """RingHomomorphism_from_quotient(parent, phi)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2718)

    A ring homomorphism with domain a generic quotient ring.

    INPUT:

    - ``parent`` -- a ring homset ``Hom(R,S)``

    - ``phi`` -- a ring homomorphism ``C --> S``, where ``C`` is the
      domain of ``R.cover()``

    OUTPUT: a ring homomorphism

    The domain `R` is a quotient object `C \\to R`, and
    ``R.cover()`` is the ring homomorphism
    `\\varphi: C \\to R`. The condition on the elements
    ``im_gens`` of `S` is that they define a
    homomorphism `C \\to S` such that each generator of the
    kernel of `\\varphi` maps to `0`.

    EXAMPLES::

        sage: # needs sage.libs.singular
        sage: R.<x, y, z> = PolynomialRing(QQ, 3)
        sage: S.<a, b, c> = R.quo(x^3 + y^3 + z^3)
        sage: phi = S.hom([b, c, a]); phi
        Ring endomorphism of Quotient of Multivariate Polynomial Ring in x, y, z
         over Rational Field by the ideal (x^3 + y^3 + z^3)
          Defn: a |--> b
                b |--> c
                c |--> a
        sage: phi(a + b + c)
        a + b + c
        sage: loads(dumps(phi)) == phi
        True

    Validity of the homomorphism is determined, when possible, and a
    :exc:`TypeError` is raised if there is no homomorphism sending the
    generators to the given images::

        sage: S.hom([b^2, c^2, a^2])                                                    # needs sage.libs.singular
        Traceback (most recent call last):
        ...
        ValueError: relations do not all (canonically) map to 0
        under map determined by images of generators"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, phi) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2764)

                Initialize ``self``.

                EXAMPLES::

                    sage: R.<x,y> = QQ[]; S.<xx,yy> = R.quo([x^2,y^2]); S.hom([yy,xx])          # needs sage.libs.singular
                    Ring endomorphism of Quotient of Multivariate Polynomial Ring in x, y
                     over Rational Field by the ideal (x^2, y^2)
                      Defn: xx |--> yy
                            yy |--> xx
        """
    @overload
    def morphism_from_cover(self) -> Any:
        """RingHomomorphism_from_quotient.morphism_from_cover(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2865)

        Underlying morphism used to define this quotient map, i.e.,
        the morphism from the cover of the domain.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<xx,yy> = R.quo([x^2, y^2])                         # needs sage.libs.singular
            sage: S.hom([yy,xx]).morphism_from_cover()                                  # needs sage.libs.singular
            Ring morphism:
              From: Multivariate Polynomial Ring in x, y over Rational Field
              To:   Quotient of Multivariate Polynomial Ring in x, y
                    over Rational Field by the ideal (x^2, y^2)
              Defn: x |--> yy
                    y |--> xx"""
    @overload
    def morphism_from_cover(self) -> Any:
        """RingHomomorphism_from_quotient.morphism_from_cover(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2865)

        Underlying morphism used to define this quotient map, i.e.,
        the morphism from the cover of the domain.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<xx,yy> = R.quo([x^2, y^2])                         # needs sage.libs.singular
            sage: S.hom([yy,xx]).morphism_from_cover()                                  # needs sage.libs.singular
            Ring morphism:
              From: Multivariate Polynomial Ring in x, y over Rational Field
              To:   Quotient of Multivariate Polynomial Ring in x, y
                    over Rational Field by the ideal (x^2, y^2)
              Defn: x |--> yy
                    y |--> xx"""
    def __hash__(self) -> Any:
        """RingHomomorphism_from_quotient.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2908)

        Return the hash of this morphism.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x, y, z> = PolynomialRing(GF(19), 3)
            sage: S.<a, b, c> = R.quo(x^3 + y^3 + z^3)
            sage: phi = S.hom([b, c, a])
            sage: type(phi)
            <class 'sage.rings.morphism.RingHomomorphism_from_quotient'>
            sage: hash(phi) == hash(phi)
            True
            sage: {phi: 1}[phi]
            1"""

class RingHomomorphism_im_gens(RingHomomorphism):
    """RingHomomorphism_im_gens(parent, im_gens, check=True, base_map=None)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1762)

    A ring homomorphism determined by the images of generators."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, im_gens, check=..., base_map=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1766)

                EXAMPLES::

                    sage: R.<x,y> = QQ[]
                    sage: phi = R.hom([x, x + y]); phi
                    Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
                      Defn: x |--> x
                            y |--> x + y
                    sage: type(phi)
                    <class 'sage.rings.morphism.RingHomomorphism_im_gens'>

                Here's another example where the domain isn't free::

                    sage: S.<xx,yy> = R.quotient(x - y)                                         # needs sage.libs.singular
                    sage: phi = S.hom([xx + 1, xx + 1])                                         # needs sage.libs.singular

                Note that one has to specify valid images::

                    sage: phi = S.hom([xx + 1, xx - 1])                                         # needs sage.libs.singular
                    Traceback (most recent call last):
                    ...
                    ValueError: relations do not all (canonically) map to 0
                     under map determined by images of generators

                You can give a map of the base ring::

                    sage: # needs sage.rings.number_field
                    sage: Zx.<x> = ZZ[]
                    sage: K.<i> = NumberField(x^2 + 1)
                    sage: cc = K.hom([-i])
                    sage: R.<t> = K[]
                    sage: z = 1 + i*t + (3+4*i)*t^2
                    sage: z._im_gens_(R, [t^2], base_map=cc)
                    (-4*i + 3)*t^4 - i*t^2 + 1

                The base map's codomain is extended to the whole codomain::

                    sage: S.<x> = QQ[]
                    sage: T.<y> = S[]
                    sage: cc = S.hom([x + 1])
                    sage: f = T.hom([x - y], base_map=cc)
                    sage: g = T.hom([x - y], base_map=cc.extend_codomain(T))
                    sage: f == g
                    True
                    sage: f.base_map() == cc.extend_codomain(T)
                    True

                There is a check option, but it may be ignored in some cases
                -- it's purpose isn't so you can lie to Sage, but to sometimes
                speed up creation of a homomorphism::

                    sage: R.<x,y> = QQ[]
                    sage: S.<xx,yy> = R.quotient(x - y)                                         # needs sage.libs.singular
                    sage: phi = S.hom([xx + 1, xx - 1], check=False)                            # needs sage.libs.singular
                    Traceback (most recent call last):
                    ...
                    ValueError: relations do not all (canonically) map to 0
                     under map determined by images of generators
        """
    def base_map(self, *args, **kwargs):
        """RingHomomorphism_im_gens.base_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1875)

        Return the map on the base ring that is part of the defining
        data for this morphism.  May return ``None`` if a coercion is used.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = ZZ[]
            sage: K.<i> = NumberField(x^2 + 1)
            sage: cc = K.hom([-i])
            sage: S.<y> = K[]
            sage: phi = S.hom([y^2], base_map=cc)
            sage: phi
            Ring endomorphism of Univariate Polynomial Ring in y
             over Number Field in i with defining polynomial x^2 + 1
              Defn: y |--> y^2
                    with map of base ring
            sage: phi(y)
            y^2
            sage: phi(i*y)
            -i*y^2
            sage: phi.base_map()
            Composite map:
              From: Number Field in i with defining polynomial x^2 + 1
              To:   Univariate Polynomial Ring in y over Number Field in i
                    with defining polynomial x^2 + 1
              Defn:   Ring endomorphism of Number Field in i with defining polynomial x^2 + 1
                      Defn: i |--> -i
                    then
                      Polynomial base injection morphism:
                      From: Number Field in i with defining polynomial x^2 + 1
                      To:   Univariate Polynomial Ring in y over Number Field in i
                            with defining polynomial x^2 + 1"""
    @overload
    def im_gens(self) -> Any:
        """RingHomomorphism_im_gens.im_gens(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1851)

        Return the images of the generators of the domain.

        OUTPUT:

        - ``list`` -- a copy of the list of gens (it is safe to change this)

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x, x + y])
            sage: f.im_gens()
            [x, x + y]

        We verify that the returned list of images of gens is a copy,
        so changing it doesn't change ``f``::

            sage: f.im_gens()[0] = 5
            sage: f.im_gens()
            [x, x + y]"""
    @overload
    def im_gens(self) -> Any:
        """RingHomomorphism_im_gens.im_gens(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 1851)

        Return the images of the generators of the domain.

        OUTPUT:

        - ``list`` -- a copy of the list of gens (it is safe to change this)

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.hom([x, x + y])
            sage: f.im_gens()
            [x, x + y]

        We verify that the returned list of images of gens is a copy,
        so changing it doesn't change ``f``::

            sage: f.im_gens()[0] = 5
            sage: f.im_gens()
            [x, x + y]"""
    def __hash__(self) -> Any:
        """RingHomomorphism_im_gens.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 2025)

        Return the hash of this morphism.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: s = R.hom([x+1])
            sage: type(s)
            <class 'sage.rings.morphism.RingHomomorphism_im_gens'>
            sage: hash(s) == hash(s)
            True
            sage: {s: 1}[s]
            1"""

class RingMap(sage.categories.morphism.Morphism):
    """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 416)

        Set-theoretic map between rings.

        TESTS:

        This is an abstract base class that is not directly instantiated,
        but we will do so anyway as a test::

            sage: f = sage.rings.morphism.RingMap(ZZ.Hom(ZZ))
            sage: parent(f)
            Set of Homomorphisms from Integer Ring to Integer Ring
            sage: type(f)
            <class 'sage.rings.morphism.RingMap'>
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class RingMap_lift(RingMap):
    """RingMap_lift(R, S)

    File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 446)

    Given rings `R` and `S` such that for any
    `x \\in R` the function ``x.lift()`` is an
    element that naturally coerces to `S`, this returns the
    set-theoretic ring map `R \\to S` sending `x` to
    ``x.lift()``.

    EXAMPLES::

        sage: R.<x,y> = QQ[]
        sage: S.<xbar,ybar> = R.quo( (x^2 + y^2, y) )                                   # needs sage.libs.singular
        sage: S.lift()                                                                  # needs sage.libs.singular
        Set-theoretic ring morphism:
          From: Quotient of Multivariate Polynomial Ring in x, y
                 over Rational Field by the ideal (x^2 + y^2, y)
          To:   Multivariate Polynomial Ring in x, y over Rational Field
          Defn: Choice of lifting map
        sage: S.lift() == 0                                                             # needs sage.libs.singular
        False

    Since :issue:`11068`, it is possible to create
    quotient rings of non-commutative rings by two-sided
    ideals. It was needed to modify :class:`RingMap_lift`
    so that rings can be accepted that are no instances
    of :class:`sage.rings.ring.Ring`, as in the following
    example::

        sage: # needs sage.modules sage.rings.finite_rings
        sage: MS = MatrixSpace(GF(5), 2, 2)
        sage: I = MS * [MS.0*MS.1, MS.2+MS.3] * MS
        sage: Q = MS.quo(I)
        sage: Q.0*Q.1   # indirect doctest
        [0 1]
        [0 0]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 482)

                Create a lifting ring map.

                EXAMPLES::

                    sage: f = Zmod(8).lift()          # indirect doctest
                    sage: f(3)
                    3
                    sage: type(f(3))
                    <class 'sage.rings.integer.Integer'>
                    sage: type(f)
                    <class 'sage.rings.morphism.RingMap_lift'>

                An invalid example::

                    sage: GF9.<one, a> = GaussianIntegers().quotient(3)                         # needs sage.rings.number_field
                    sage: from sage.rings.morphism import RingMap_lift
                    sage: RingMap_lift(GF9, ZZ)                                                 # needs sage.rings.number_field
                    Traceback (most recent call last):
                    ...
                    TypeError: no canonical coercion from Number Field in I
                    with defining polynomial x^2 + 1 with I = 1*I to Integer Ring
        """
    def __hash__(self) -> Any:
        """RingMap_lift.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/morphism.pyx (starting at line 580)

        Return the hash of this morphism.

        TESTS::

            sage: f = Zmod(8).lift()
            sage: type(f)
            <class 'sage.rings.morphism.RingMap_lift'>
            sage: hash(f) == hash(f)
            True
            sage: {f: 1}[f]
            1
            sage: g = Zmod(10).lift()
            sage: hash(f) == hash(g)
            False"""
