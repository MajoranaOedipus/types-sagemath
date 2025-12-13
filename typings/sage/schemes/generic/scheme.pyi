from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.point import SchemeTopologicalPoint_prime_ideal as SchemeTopologicalPoint_prime_ideal
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_Scheme(x):
    """
    Test whether ``x`` is a scheme.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean; whether ``x`` derives from :class:`Scheme`

    EXAMPLES::

        sage: from sage.schemes.generic.scheme import is_Scheme
        sage: is_Scheme(5)
        doctest:warning...
        DeprecationWarning: The function is_Scheme is deprecated; use 'isinstance(..., Scheme)' or categories instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: X = Spec(QQ)
        sage: is_Scheme(X)
        True
    """

class Scheme(Parent):
    """
    The base class for all schemes.

    INPUT:

    - ``X`` -- a scheme, scheme morphism, commutative ring,
      commutative ring morphism, or ``None`` (optional). Determines
      the base scheme. If a commutative ring is passed, the spectrum
      of the ring will be used as base.

    - ``category`` -- the category (optional); will be automatically
      constructed by default

    EXAMPLES::

        sage: from sage.schemes.generic.scheme import Scheme
        sage: Scheme(ZZ)
        <sage.schemes.generic.scheme.Scheme_with_category object at ...>

    A scheme is in the category of all schemes over its base::

        sage: ProjectiveSpace(4, QQ).category()
        Category of schemes over Rational Field

    There is a special and unique `\\mathrm{Spec}(\\ZZ)` that is the default base
    scheme::

        sage: Spec(ZZ).base_scheme() is Spec(QQ).base_scheme()
        True
    """
    def __init__(self, X=None, category=None) -> None:
        """
        Construct a scheme.

        TESTS:

        The full test suite works since :issue:`7946`::

            sage: R.<x, y> = QQ[]
            sage: I = (x^2 - y^2)*R
            sage: RmodI = R.quotient(I)
            sage: X = Spec(RmodI)
            sage: TestSuite(X).run()                                                    # needs sage.libs.singular
        """
    def union(self, X) -> None:
        """
        Return the disjoint union of the schemes ``self`` and ``X``.

        EXAMPLES::

            sage: S = Spec(QQ)
            sage: X = AffineSpace(1, QQ)
            sage: S.union(X)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    __add__ = union
    def base_extend(self, Y) -> None:
        """
        Extend the base of the scheme.

        Derived classes must override this method.

        EXAMPLES::

            sage: from sage.schemes.generic.scheme import Scheme
            sage: X = Scheme(ZZ)
            sage: X.base_scheme()
            Spectrum of Integer Ring
            sage: X.base_extend(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def __call__(self, *args):
        """
        Call syntax for schemes.

        INPUT/OUTPUT: the arguments must be one of the following:

        - a ring or a scheme `S`. Output will be the set `X(S)` of
          `S`-valued points on `X`.

        - If `S` is a list or tuple or just the coordinates, return a
          point in `X(T)`, where `T` is the base scheme of ``self``.

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)

        We create some point sets::

            sage: A(QQ)
            Set of rational points of Affine Space of dimension 2 over Rational Field
            sage: A(RR)                                                                 # needs sage.rings.real_mpfr
            Set of rational points of Affine Space of dimension 2
             over Real Field with 53 bits of precision

        Space of dimension 2 over Rational Field::

            sage: R.<x> = PolynomialRing(QQ)
            sage: A(NumberField(x^2 + 1, 'a'))                                          # needs sage.rings.number_field
            Set of rational points of Affine Space of dimension 2
             over Number Field in a with defining polynomial x^2 + 1
            sage: A(GF(7))
            Traceback (most recent call last):
            ...
            ValueError: There must be a natural map S --> R, but
            S = Rational Field and R = Finite Field of size 7

        We create some points::

            sage: A(QQ)([1, 0])
            (1, 0)

        We create the same point by giving the coordinates of the point
        directly::

            sage: A(1, 0)
            (1, 0)

        Check that :issue:`16832` is fixed::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: X(P([4, 4, 1]))
            (4 : 4 : 1)
        """
    @cached_method
    def point_homset(self, S=None):
        """
        Return the set of S-valued points of this scheme.

        INPUT:

        - ``S`` -- a commutative ring

        OUTPUT: the set of morphisms `\\mathrm{Spec}(S) \\to X`

        EXAMPLES::

            sage: P = ProjectiveSpace(ZZ, 3)
            sage: P.point_homset(ZZ)
            Set of rational points of Projective Space of dimension 3 over Integer Ring
            sage: P.point_homset(QQ)
            Set of rational points of Projective Space of dimension 3 over Rational Field
            sage: P.point_homset(GF(11))
            Set of rational points of Projective Space of dimension 3 over
             Finite Field of size 11

        TESTS::

            sage: P = ProjectiveSpace(QQ, 3)
            sage: P.point_homset(GF(11))
            Traceback (most recent call last):
            ...
            ValueError: There must be a natural map S --> R, but
            S = Rational Field and R = Finite Field of size 11
        """
    def point(self, v, check: bool = True):
        """
        Create a point.

        INPUT:

        - ``v`` -- anything that defines a point

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: a point of the scheme

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A2.point([4, 5])
            (4, 5)

            sage: R.<t> = PolynomialRing(QQ)
            sage: E = EllipticCurve([t + 1, t, t, 0, 0])                                # needs sage.schemes
            sage: E.point([0, 0])                                                       # needs sage.schemes
            (0 : 0 : 1)
        """
    def __truediv__(self, Y):
        """
        Return the base extension of ``self`` to Y.

        See :meth:`base_extend` for details.

        EXAMPLES::

            sage: A = AffineSpace(3, ZZ)
            sage: A
            Affine Space of dimension 3 over Integer Ring
            sage: A/QQ
            Affine Space of dimension 3 over Rational Field
            sage: A/GF(7)
            Affine Space of dimension 3 over Finite Field of size 7
        """
    def base_ring(self):
        """
        Return the base ring of the scheme ``self``.

        OUTPUT: a commutative ring

        EXAMPLES::

            sage: A = AffineSpace(4, QQ)
            sage: A.base_ring()
            Rational Field

            sage: X = Spec(QQ)
            sage: X.base_ring()
            Integer Ring
        """
    def base_scheme(self):
        """
        Return the base scheme.

        OUTPUT: a scheme

        EXAMPLES::

            sage: A = AffineSpace(4, QQ)
            sage: A.base_scheme()
            Spectrum of Rational Field

            sage: X = Spec(QQ)
            sage: X.base_scheme()
            Spectrum of Integer Ring
        """
    def base_morphism(self):
        """
        Return the structure morphism from ``self`` to its base
        scheme.

        OUTPUT: a scheme morphism

        EXAMPLES::

            sage: A = AffineSpace(4, QQ)
            sage: A.base_morphism()
            Scheme morphism:
              From: Affine Space of dimension 4 over Rational Field
              To:   Spectrum of Rational Field
              Defn: Structure map

            sage: X = Spec(QQ)
            sage: X.base_morphism()
            Scheme morphism:
              From: Spectrum of Rational Field
              To:   Spectrum of Integer Ring
              Defn: Structure map
        """
    structure_morphism = base_morphism
    def coordinate_ring(self):
        """
        Return the coordinate ring.

        OUTPUT:

        The global coordinate ring of this scheme, if
        defined. Otherwise this raises a :exc:`ValueError`.

        EXAMPLES::

            sage: R.<x, y> = QQ[]
            sage: I = (x^2 - y^2)*R
            sage: X = Spec(R.quotient(I))
            sage: X.coordinate_ring()
            Quotient of Multivariate Polynomial Ring in x, y over Rational Field
             by the ideal (x^2 - y^2)
        """
    def dimension_absolute(self) -> None:
        """
        Return the absolute dimension of this scheme.

        OUTPUT: integer

        EXAMPLES::

            sage: R.<x, y> = QQ[]
            sage: I = (x^2 - y^2)*R
            sage: X = Spec(R.quotient(I))
            sage: X.dimension_absolute()
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: X.dimension()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    dimension = dimension_absolute
    def dimension_relative(self) -> None:
        """
        Return the relative dimension of this scheme over its base.

        OUTPUT: integer

        EXAMPLES::

            sage: R.<x, y> = QQ[]
            sage: I = (x^2 - y^2)*R
            sage: X = Spec(R.quotient(I))
            sage: X.dimension_relative()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def identity_morphism(self):
        """
        Return the identity morphism.

        OUTPUT: the identity morphism of the scheme ``self``

        EXAMPLES::

            sage: X = Spec(QQ)
            sage: X.identity_morphism()
            Scheme endomorphism of Spectrum of Rational Field
              Defn: Identity map
        """
    def hom(self, x, Y=None, check: bool = True):
        """
        Return the scheme morphism from ``self`` to ``Y`` defined by ``x``.

        INPUT:

        - ``x`` -- anything that determines a scheme morphism; if
          ``x`` is a scheme, try to determine a natural map to ``x``

        - ``Y`` -- the codomain scheme (optional); if ``Y`` is not
          given, try to determine ``Y`` from context

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: the scheme morphism from ``self`` to ``Y`` defined by ``x``

        EXAMPLES::

            sage: P = ProjectiveSpace(ZZ, 3)
            sage: P.hom(Spec(ZZ))
            Scheme morphism:
              From: Projective Space of dimension 3 over Integer Ring
              To:   Spectrum of Integer Ring
              Defn: Structure map
        """
    point_set = point_homset
    def count_points(self, n):
        """
        Count points over finite fields.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        An integer. The number of points over `\\GF{q}, \\ldots,
        \\GF{q^n}` on a scheme over a finite field `\\GF{q}`.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: P.<x> = PolynomialRing(GF(3))
            sage: C = HyperellipticCurve(x^3 + x^2 + 1)
            sage: C.count_points(4)
            [6, 12, 18, 96]
            sage: C.base_extend(GF(9,'a')).count_points(2)                              # needs sage.rings.finite_rings
            [12, 96]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(4, 't'), 2)                            # needs sage.rings.finite_rings
            sage: X = P.subscheme([y^2*z - x^3 - z^3])                                  # needs sage.rings.finite_rings
            sage: X.count_points(2)                                                     # needs sage.libs.singular sage.rings.finite_rings
            [5, 17]
        """
    def zeta_function(self) -> None:
        """
        Compute the zeta function of a generic scheme.

        Derived classes should override this method.

        OUTPUT: rational function in one variable

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(4, 't'), 2)                            # needs sage.rings.finite_rings
            sage: X = P.subscheme([y^2*z - x^3 - z^3])                                  # needs sage.rings.finite_rings
            sage: X.zeta_function()                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def zeta_series(self, n, t):
        """
        Return the zeta series.

        Compute a power series approximation to the zeta function of a
        scheme over a finite field.

        INPUT:

        - ``n`` -- the number of terms of the power series to compute

        - ``t`` -- the variable which the series should be returned

        OUTPUT: a power series approximating the zeta function of ``self``

        EXAMPLES::

            sage: P.<x> = PolynomialRing(GF(3))
            sage: C = HyperellipticCurve(x^3 + x^2 + 1)                                 # needs sage.schemes
            sage: R.<t> = PowerSeriesRing(Integers())
            sage: C.zeta_series(4, t)                                                   # needs sage.schemes
            1 + 6*t + 24*t^2 + 78*t^3 + 240*t^4 + O(t^5)
            sage: (1+2*t+3*t^2)/(1-t)/(1-3*t) + O(t^5)
            1 + 6*t + 24*t^2 + 78*t^3 + 240*t^4 + O(t^5)

        If the scheme has a method ``zeta_function``, this is used to
        provide the required approximation.
        Otherwise this function depends on ``count_points``, which is only
        defined for prime order fields for general schemes.
        Nonetheless, since :issue:`15108` and :issue:`15148`, it supports
        hyperelliptic curves over non-prime fields::

            sage: C.base_extend(GF(9, 'a')).zeta_series(4, t)                           # needs sage.rings.finite_rings sage.schemes
            1 + 12*t + 120*t^2 + 1092*t^3 + 9840*t^4 + O(t^5)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(4, 't'), 2)                            # needs sage.rings.finite_rings
            sage: X = P.subscheme([y^2*z - x^3 - z^3])                                  # needs sage.rings.finite_rings

            sage: R.<t> = PowerSeriesRing(Integers())
            sage: X.zeta_series(2, t)                                                   # needs sage.libs.singular sage.rings.finite_rings
            1 + 5*t + 21*t^2 + O(t^3)

        TESTS::

            sage: P.<x> = PolynomialRing(ZZ)
            sage: C = HyperellipticCurve(x^3 + x + 1)                                   # needs sage.schemes
            sage: R.<t> = PowerSeriesRing(Integers())
            sage: C.zeta_series(4, t)                                                   # needs sage.schemes
            Traceback (most recent call last):
            ...
            TypeError: zeta functions only defined for schemes
            over finite fields
        """

def is_AffineScheme(x):
    """
    Return ``True`` if `x` is an affine scheme.

    EXAMPLES::

        sage: from sage.schemes.generic.scheme import is_AffineScheme
        sage: is_AffineScheme(5)
        doctest:warning...
        DeprecationWarning: The function is_AffineScheme is deprecated; use 'isinstance(..., AffineScheme)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: E = Spec(QQ)
        sage: is_AffineScheme(E)
        True
    """

class AffineScheme(UniqueRepresentation, Scheme):
    """
    Class for general affine schemes.

    TESTS::

        sage: from sage.schemes.generic.scheme import AffineScheme
        sage: A = QQ['t']
        sage: X_abs = AffineScheme(A); X_abs
        Spectrum of Univariate Polynomial Ring in t over Rational Field
        sage: X_rel = AffineScheme(A, QQ); X_rel
        Spectrum of Univariate Polynomial Ring in t over Rational Field

        sage: X_abs == X_rel
        False
        sage: X_abs.base_ring()
        Integer Ring
        sage: X_rel.base_ring()
        Rational Field

    .. SEEALSO::

        For affine spaces over a base ring and subschemes thereof, see
        :class:`sage.schemes.generic.algebraic_scheme.AffineSpace`.
    """
    def __init__(self, R, S=None, category=None) -> None:
        """
        Construct the affine scheme with coordinate ring `R`.

        INPUT:

        - ``R`` -- commutative ring

        - ``S`` -- (optional) commutative ring admitting a natural map
          to ``R``

        OUTPUT:

        The spectrum of `R`, i.e. the unique affine scheme with
        coordinate ring `R` as a scheme over the base ring `S`.

        EXAMPLES::

            sage: from sage.schemes.generic.scheme import AffineScheme
            sage: A.<x, y> = PolynomialRing(QQ)
            sage: X = AffineScheme(A, QQ)
            sage: X
            Spectrum of Multivariate Polynomial Ring in x, y over Rational Field
            sage: X.category()
            Category of schemes over Rational Field

        The standard way to construct an affine scheme is to use the
        :func:`~sage.schemes.generic.spec.Spec` functor::

            sage: S = Spec(ZZ)
            sage: S
            Spectrum of Integer Ring
            sage: S.category()
            Category of schemes
            sage: type(S)
            <class 'sage.schemes.generic.scheme.AffineScheme_with_category'>
        """
    def __call__(self, *args):
        """
        Construct a scheme-valued or topological point of ``self``.

        INPUT/OUTPUT: the argument ``x`` must be one of the following:

        - a prime ideal of the coordinate ring; the output will
          be the corresponding point of `X`

        - a ring or a scheme `S`; the output will be the set `X(S)` of
          `S`-valued points on `X`

        EXAMPLES::

            sage: S = Spec(ZZ)
            sage: P = S(ZZ.ideal(3)); P
            Point on Spectrum of Integer Ring defined by the Principal ideal (3) of Integer Ring
            sage: type(P)
            <class 'sage.schemes.generic.scheme.AffineScheme_with_category.element_class'>
            sage: S(ZZ.ideal(next_prime(1000000)))                                      # needs sage.libs.pari
            Point on Spectrum of Integer Ring
             defined by the Principal ideal (1000003) of Integer Ring

            sage: R.<x, y, z> = QQ[]
            sage: S = Spec(R)
            sage: P = S(R.ideal(x, y, z)); P
            Point on Spectrum of Multivariate Polynomial Ring
             in x, y, z over Rational Field defined by the Ideal (x, y, z)
              of Multivariate Polynomial Ring in x, y, z over Rational Field

        This indicates the fix of :issue:`12734`::

            sage: S = Spec(ZZ)
            sage: S(ZZ)
            Set of rational points of Spectrum of Integer Ring

        Note the difference between the previous example and the
        following one::

            sage: S(S)
            Set of morphisms
              From: Spectrum of Integer Ring
              To:   Spectrum of Integer Ring

        For affine or projective varieties, passing the correct number
        of elements of the base ring constructs the rational point
        with these elements as coordinates::

            sage: S = AffineSpace(ZZ, 1)
            sage: S(0)
            (0)

        To prevent confusion with this usage, topological points must
        be constructed by explicitly specifying a prime ideal, not
        just generators::

            sage: R = S.coordinate_ring()
            sage: S(R.ideal(0))
            Point on Affine Space of dimension 1 over Integer Ring
             defined by the Ideal (0) of Multivariate Polynomial Ring in x over Integer Ring

        This explains why the following example raises an error rather
        than constructing the topological point defined by the prime
        ideal `(0)` as one might expect::

            sage: S = Spec(ZZ)
            sage: S(0)
            Traceback (most recent call last):
            ...
            TypeError: cannot call Spectrum of Integer Ring with arguments (0,)
        """
    Element = SchemeTopologicalPoint_prime_ideal
    def coordinate_ring(self):
        """
        Return the underlying ring of this scheme.

        OUTPUT: a commutative ring

        EXAMPLES::

            sage: Spec(QQ).coordinate_ring()
            Rational Field
            sage: Spec(PolynomialRing(QQ, 3, 'x')).coordinate_ring()
            Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
        """
    def is_noetherian(self):
        """
        Return ``True`` if ``self`` is Noetherian, ``False`` otherwise.

        EXAMPLES::

            sage: Spec(ZZ).is_noetherian()
            True
        """
    def dimension_absolute(self):
        """
        Return the absolute dimension of this scheme.

        OUTPUT: integer

        EXAMPLES::

            sage: S = Spec(ZZ)
            sage: S.dimension_absolute()
            1
            sage: S.dimension()
            1
        """
    dimension = dimension_absolute
    def dimension_relative(self):
        """
        Return the relative dimension of this scheme over its base.

        OUTPUT: integer

        EXAMPLES::

            sage: S = Spec(ZZ)
            sage: S.dimension_relative()
            0
        """
    def base_extend(self, R):
        """
        Extend the base ring/scheme.

        INPUT:

        - ``R`` -- an affine scheme or a commutative ring

        EXAMPLES::

            sage: Spec_ZZ = Spec(ZZ);  Spec_ZZ
            Spectrum of Integer Ring
            sage: Spec_ZZ.base_extend(QQ)
            Spectrum of Rational Field

            sage: Spec(ZZ['x']).base_extend(Spec(QQ))
            Spectrum of Univariate Polynomial Ring in x over Rational Field
        """
    def hom(self, x, Y=None):
        """
        Return the scheme morphism from ``self`` to ``Y`` defined by ``x``.

        INPUT:

        - ``x`` -- anything that determines a scheme morphism; if
          ``x`` is a scheme, try to determine a natural map to ``x``

        - ``Y`` -- the codomain scheme (optional); if ``Y`` is not
          given, try to determine ``Y`` from context

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: the scheme morphism from ``self`` to ``Y`` defined by ``x``

        EXAMPLES:

        We construct the inclusion from `\\mathrm{Spec}(\\QQ)` into
        `\\mathrm{Spec}(\\ZZ)` induced by the inclusion from `\\ZZ` into
        `\\QQ`::

            sage: X = Spec(QQ)
            sage: X.hom(ZZ.hom(QQ))
            Affine Scheme morphism:
              From: Spectrum of Rational Field
              To:   Spectrum of Integer Ring
              Defn: Natural morphism:
                      From: Integer Ring
                      To:   Rational Field

        TESTS:

        We can construct a morphism to an affine curve (:issue:`7956`)::

            sage: S.<p,q> = QQ[]
            sage: A1.<r> = AffineSpace(QQ, 1)
            sage: A1_emb = Curve(p - 2)                                                 # needs sage.schemes
            sage: A1.hom([2, r], A1_emb)                                                # needs sage.schemes
            Scheme morphism:
              From: Affine Space of dimension 1 over Rational Field
              To:   Affine Plane Curve over Rational Field defined by p - 2
              Defn: Defined on coordinates by sending (r) to (2, r)
        """
