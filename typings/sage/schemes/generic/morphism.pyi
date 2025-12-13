from sage.arith.power import generic_power as generic_power
from sage.categories.homset import End as End, Hom as Hom, Homset as Homset
from sage.categories.map import FormalCompositeMap as FormalCompositeMap, Map as Map
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.structure.element import Element as Element, coercion_model as coercion_model, parent as parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

def is_SchemeMorphism(f):
    """
    Test whether ``f`` is a scheme morphism.

    INPUT:

    - ``f`` -- anything

    OUTPUT:

    boolean; return ``True`` if ``f`` is a scheme morphism or a point
    on an elliptic curve.

    EXAMPLES::

        sage: A.<x,y> = AffineSpace(QQ, 2); H = A.Hom(A)
        sage: f = H([y, x^2 + y]); f
        Scheme endomorphism of Affine Space of dimension 2 over Rational Field
          Defn: Defined on coordinates by sending (x, y) to (y, x^2 + y)
        sage: from sage.schemes.generic.morphism import is_SchemeMorphism
        sage: is_SchemeMorphism(f)
        doctest:warning...
        DeprecationWarning: The function is_SchemeMorphism is deprecated;
        use 'isinstance(..., SchemeMorphism)' instead.
        See https://github.com/sagemath/sage/issues/38296 for details.
        True
    """

class SchemeMorphism(Element):
    """
    Base class for scheme morphisms.

    INPUT:

    - ``parent`` -- the parent of the morphism

    .. TODO::

        For historical reasons, :class:`SchemeMorphism` copies code from
        :class:`~sage.categories.map.Map` rather than inheriting from it.
        Proper inheritance should be used instead. See :issue:`14711`.

    EXAMPLES::

        sage: X = Spec(ZZ)
        sage: Hom = X.Hom(X)
        sage: from sage.schemes.generic.morphism import SchemeMorphism
        sage: f = SchemeMorphism(Hom)
        sage: type(f)
        <class 'sage.schemes.generic.morphism.SchemeMorphism'>

    TESTS::

        sage: A2 = AffineSpace(QQ, 2)
        sage: A2.structure_morphism().domain()
        Affine Space of dimension 2 over Rational Field
        sage: A2.structure_morphism().category()
        Category of homsets of schemes
    """
    def __init__(self, parent, codomain=None) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: X = Spec(ZZ)
            sage: Hom = X.Hom(X)
            sage: from sage.schemes.generic.morphism import SchemeMorphism
            sage: f = SchemeMorphism(Hom)
            sage: type(f)
            <class 'sage.schemes.generic.morphism.SchemeMorphism'>
        """
    @lazy_attribute
    def domain(self):
        """
        The constant function from the domain.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ['x,y'])
            sage: H = A.Hom(A)
            sage: f = H([y, x^2 + y])
            sage: f.domain() is A
            True
        """
    @lazy_attribute
    def codomain(self):
        """
        The constant function from the codomain.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ['x,y'])
            sage: H = A.Hom(A)
            sage: f = H([y, x^2 + y])
            sage: f.codomain() is A
            True
        """
    def __call__(self, x, *args, **kwds):
        """
        Do not override this method!

        For implementing application of maps, implement a method
        ``_call_(self, x)`` and/or a method ``_call_with_args(x, args, kwds)`.
        In these methods, you can assume that ``x`` belongs to the domain of
        this morphism, ``args`` is a tuple and ``kwds`` is a dict.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: A.<x,y> = AffineSpace(R)
            sage: H = A.Hom(A)
            sage: f = H([y, x^2 + y])
            sage: f([2,3])    # indirect doctest
            (3, 7)

        An example with optional arguments::

            sage: PS.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(PS, PS)
            sage: f = H([x^3, x*y^2])
            sage: P = PS(0, 1)
            sage: f(P, check=False)     # indirect doctest
            (0 : 0)
        """
    def __mul__(self, right):
        """
        We can currently only multiply scheme morphisms.

        If one factor is an identity morphism, the other is returned.
        Otherwise, a formal composition of maps obtained from the scheme
        morphisms is returned.

        EXAMPLES:

        Identity maps do not contribute to the product::

            sage: X = AffineSpace(QQ, 2)
            sage: id = X.identity_morphism()
            sage: id^0    # indirect doctest
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Identity map
            sage: id^2
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Identity map

        Here, we see a formal composition::

            sage: X = AffineSpace(QQ, 2)
            sage: f = X.structure_morphism()
            sage: Y = Spec(QQ)
            sage: g = Y.structure_morphism()
            sage: g * f    # indirect doctest
            Composite map:
              From: Affine Space of dimension 2 over Rational Field
              To:   Spectrum of Integer Ring
              Defn:   Generic morphism:
                      From: Affine Space of dimension 2 over Rational Field
                      To:   Spectrum of Rational Field
                    then
                      Generic morphism:
                      From: Spectrum of Rational Field
                      To:   Spectrum of Integer Ring

        Of course, the codomain of the first factor must coincide with the
        domain of the second factor::

            sage: f * g
            Traceback (most recent call last):
            ...
            TypeError: self (=Scheme morphism:
              From: Affine Space of dimension 2 over Rational Field
              To:   Spectrum of Rational Field
              Defn: Structure map) domain must equal right (=Scheme morphism:
              From: Spectrum of Rational Field
              To:   Spectrum of Integer Ring
              Defn: Structure map) codomain
        """
    def __pow__(self, n, dummy=None):
        """
        Exponentiate an endomorphism.

        INPUT:

        - ``n`` -- integer; the exponent

        OUTPUT: a composite map that belongs to the same endomorphism set as ``self``

        EXAMPLES::

            sage: X = AffineSpace(QQ, 2)
            sage: id = X.identity_morphism()
            sage: id^0
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Identity map
            sage: id^2
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Identity map
        """
    def category(self):
        """
        Return the category of the Hom-set.

        OUTPUT: a category

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A2.structure_morphism().category()
            Category of homsets of schemes
        """
    def category_for(self):
        """
        Return the category which this morphism belongs to.

        EXAMPLES::

            sage: A2 = AffineSpace(QQ, 2)
            sage: A2.structure_morphism().category_for()
            Category of schemes
        """
    def is_endomorphism(self) -> bool:
        """
        Return whether the morphism is an endomorphism.

        OUTPUT: boolean; whether the domain and codomain are identical

        EXAMPLES::

            sage: X = AffineSpace(QQ, 2)
            sage: X.structure_morphism().is_endomorphism()
            False
            sage: X.identity_morphism().is_endomorphism()
            True
        """
    def base_ring(self):
        """
        Return the base ring of ``self``, that is, the ring over which
        the defining polynomials of ``self`` are defined.

        OUTPUT: ring

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([3/5*x^2, 6*y^2])
            sage: f.base_ring()
            Rational Field

        ::

            sage: R.<t> = PolynomialRing(ZZ, 1)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: H = Hom(P, P)
            sage: f = H([3*x^2, y^2])
            sage: f.base_ring()
            Multivariate Polynomial Ring in t over Integer Ring

        Points have correct base rings too (:issue:`34336`)::

            sage: x = P(t, 5); x
            (t : 5)
            sage: x.base_ring()
            Multivariate Polynomial Ring in t over Integer Ring

        ::

            sage: # needs sage.rings.finite_rings sage.schemes
            sage: E = EllipticCurve(GF((17,2)), [1,2,3,4,5])
            sage: P = E.random_point()
            sage: P.base_ring()
            Finite Field in z2 of size 17^2
        """
    def glue_along_domains(self, other):
        """
        Glue two morphisms.

        INPUT:

        - ``other`` -- a scheme morphism with the same domain

        OUTPUT:

        Assuming that ``self`` and ``other`` are open immersions with the same
        domain, return scheme obtained by gluing along the images.

        EXAMPLES:

        We construct a scheme isomorphic to the projective line over
        `\\mathrm{Spec}(\\QQ)` by gluing two copies of `\\mathbb{A}^1`
        minus a point::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: S.<xbar, ybar> = R.quotient(x*y - 1)
            sage: Rx = PolynomialRing(QQ, 'x')
            sage: i1 = Rx.hom([xbar])
            sage: Ry = PolynomialRing(QQ, 'y')
            sage: i2 = Ry.hom([ybar])
            sage: Sch = Schemes()
            sage: f1 = Sch(i1)
            sage: f2 = Sch(i2)

        Now f1 and f2 have the same domain, which is a
        `\\mathbb{A}^1` minus a point. We glue along the domain::

            sage: # needs sage.libs.singular
            sage: P1 = f1.glue_along_domains(f2); P1
            Scheme obtained by gluing X and Y along U, where
              X: Spectrum of Univariate Polynomial Ring in x over Rational Field
              Y: Spectrum of Univariate Polynomial Ring in y over Rational Field
              U: Spectrum of Quotient of Multivariate Polynomial Ring in x, y
                 over Rational Field by the ideal (x*y - 1)
            sage: a, b = P1.gluing_maps()
            sage: a
            Affine Scheme morphism:
              From: Spectrum of Quotient of Multivariate Polynomial Ring in x, y
                    over Rational Field by the ideal (x*y - 1)
              To:   Spectrum of Univariate Polynomial Ring in x over Rational Field
              Defn: Ring morphism:
                      From: Univariate Polynomial Ring in x over Rational Field
                      To:   Quotient of Multivariate Polynomial Ring in x, y over
                            Rational Field by the ideal (x*y - 1)
                      Defn: x |--> xbar
            sage: b
            Affine Scheme morphism:
              From: Spectrum of Quotient of Multivariate Polynomial Ring in x, y
                    over Rational Field by the ideal (x*y - 1)
              To:   Spectrum of Univariate Polynomial Ring in y over Rational Field
              Defn: Ring morphism:
                      From: Univariate Polynomial Ring in y over Rational Field
                      To:   Quotient of Multivariate Polynomial Ring in x, y over
                            Rational Field by the ideal (x*y - 1)
                      Defn: y |--> ybar
        """

class SchemeMorphism_id(SchemeMorphism):
    """
    Return the identity morphism from `X` to itself.

    INPUT:

    - ``X`` -- the scheme

    EXAMPLES::

        sage: X = Spec(ZZ)
        sage: X.identity_morphism()  # indirect doctest
        Scheme endomorphism of Spectrum of Integer Ring
          Defn: Identity map
    """
    def __init__(self, X) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_id` for details.

        TESTS::

            sage: Spec(ZZ).identity_morphism()
            Scheme endomorphism of Spectrum of Integer Ring
              Defn: Identity map
        """

class SchemeMorphism_structure_map(SchemeMorphism):
    """
    The structure morphism.

    INPUT:

    - ``parent`` -- Hom-set with codomain equal to the base scheme of
      the domain

    EXAMPLES::

        sage: Spec(ZZ).structure_morphism()    # indirect doctest
        Scheme endomorphism of Spectrum of Integer Ring
          Defn: Structure map
    """
    def __init__(self, parent, codomain=None) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_structure_map` for details.

        TESTS::

            sage: from sage.schemes.generic.morphism import SchemeMorphism_structure_map
            sage: SchemeMorphism_structure_map( Spec(QQ).Hom(Spec(ZZ)) )
            Scheme morphism:
              From: Spectrum of Rational Field
              To:   Spectrum of Integer Ring
              Defn: Structure map
        """

class SchemeMorphism_spec(SchemeMorphism):
    """
    Morphism of spectra of rings.

    INPUT:

    - ``parent`` -- Hom-set whose domain and codomain are affine schemes

    - ``phi`` -- a ring morphism with matching domain and codomain

    - ``check`` -- boolean (default: ``True``); whether to
      check the input for consistency

    EXAMPLES::

        sage: R.<x> = PolynomialRing(QQ)
        sage: phi = R.hom([QQ(7)]); phi
        Ring morphism:
          From: Univariate Polynomial Ring in x over Rational Field
          To:   Rational Field
          Defn: x |--> 7

        sage: X = Spec(QQ); Y = Spec(R)
        sage: f = X.hom(phi); f
        Affine Scheme morphism:
          From: Spectrum of Rational Field
          To:   Spectrum of Univariate Polynomial Ring in x over Rational Field
          Defn: Ring morphism:
                  From: Univariate Polynomial Ring in x over Rational Field
                  To:   Rational Field
                  Defn: x |--> 7

        sage: f.ring_homomorphism()
        Ring morphism:
          From: Univariate Polynomial Ring in x over Rational Field
          To:   Rational Field
          Defn: x |--> 7
    """
    def __init__(self, parent, phi, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_structure_map` for details.

        TESTS::

            sage: from sage.schemes.generic.morphism import SchemeMorphism_spec
            sage: SchemeMorphism_spec(Spec(QQ).Hom(Spec(ZZ)), ZZ.hom(QQ))
            Affine Scheme morphism:
              From: Spectrum of Rational Field
              To:   Spectrum of Integer Ring
              Defn: Natural morphism:
                      From: Integer Ring
                      To:   Rational Field
        """
    def ring_homomorphism(self):
        """
        Return the underlying ring homomorphism.

        OUTPUT: a ring homomorphism

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: phi = R.hom([QQ(7)])
            sage: X = Spec(QQ); Y = Spec(R)
            sage: f = X.hom(phi)
            sage: f.ring_homomorphism()
            Ring morphism:
              From: Univariate Polynomial Ring in x over Rational Field
              To:   Rational Field
              Defn: x |--> 7
        """

class SchemeMorphism_polynomial(SchemeMorphism):
    """
    A morphism of schemes determined by polynomials that define what
    the morphism does on points in the ambient space.

    INPUT:

    - ``parent`` -- Hom-set whose domain and codomain are affine or
      projective schemes

    - ``polys`` -- list/tuple/iterable of polynomials defining the
      scheme morphism

    - ``check`` -- boolean (default: ``True``); whether to
      check the input for consistency

    EXAMPLES:

    An example involving the affine plane::

        sage: R.<x,y> = QQ[]
        sage: A2 = AffineSpace(R)
        sage: H = A2.Hom(A2)
        sage: f = H([x - y, x*y])
        sage: f([0, 1])
        (-1, 0)

    An example involving the projective line::

        sage: R.<x,y> = QQ[]
        sage: P1 = ProjectiveSpace(R)
        sage: H = P1.Hom(P1)
        sage: f = H([x^2 + y^2, x*y])
        sage: f([0, 1])
        (1 : 0)

    Some checks are performed to make sure the given polynomials
    define a morphism::

        sage: f = H([exp(x),exp(y)])                                                    # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: polys (=[e^x, e^y]) must be elements of Multivariate
        Polynomial Ring in x, y over Rational Field
    """
    def __init__(self, parent, polys, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_polynomial` for details.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: H = A2.Hom(A2)
            sage: H([x - y, x*y])
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x, y) to (x - y, x*y)
        """
    def __eq__(self, other):
        """
        Check equality of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a morphism

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: I = A.identity_morphism()
            sage: I.parent().identity() == I
            True
        """
    def defining_polynomials(self):
        """
        Return the defining polynomials.

        OUTPUT:

        An immutable sequence of polynomials that defines this scheme
        morphism.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: A.<x,y> = AffineSpace(R)
            sage: H = A.Hom(A)
            sage: H([x^3 + y, 1 - x - y]).defining_polynomials()
            (x^3 + y, -x - y + 1)
        """
    def __getitem__(self, i):
        """
        Return the i-th poly with ``self[i]``.

        INPUT:

        - ``i`` -- integer

        OUTPUT: element of the coordinate ring of the domain

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([3/5*x^2, 6*y^2])
            sage: f[1]
            6*y^2
        """
    def __copy__(self):
        """
        Return a copy of ``self``.

        OUTPUT: :class:`SchemeMorphism_polynomial`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([3/5*x^2, 6*y^2])
            sage: g = copy(f)
            sage: f == g
            True
            sage: f is g
            False

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: Q = X(23, 23, 46)
            sage: P = X(1, 1, 1)
            sage: P != Q
            True
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of the ambient projective space.

        OUTPUT: a multivariable polynomial ring over the base ring

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([3/5*x^2, 6*y^2])
            sage: f.coordinate_ring()
            Multivariate Polynomial Ring in x, y over Rational Field

        ::

            sage: R.<t> = PolynomialRing(ZZ, 1)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: H = Hom(P, P)
            sage: f = H([3*x^2, y^2])
            sage: f.coordinate_ring()
            Multivariate Polynomial Ring in x, y over Multivariate Polynomial Ring
            in t over Integer Ring
        """
    def change_ring(self, R, check: bool = True):
        """
        Return a new :class:`SchemeMorphism_polynomial` which is this map
        coerced to ``R``.

        If ``check`` is ``True``, then the initialization checks are performed.

        INPUT:

        - ``R`` -- ring or morphism

        - ``check`` -- boolean

        OUTPUT: a new :class:`SchemeMorphism_polynomial` which is this map
        coerced to ``R``

        TESTS::

            sage: # needs sage.rings.number_field
            sage: R.<t> = QQ[]
            sage: K.<v> = QuadraticField(2)
            sage: K2.<w> = NumberField(t**4 - 2)
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: phi = K.embeddings(K2)[0]
            sage: f = DynamicalSystem_projective([x**2 + 3*y**2, y**2])                 # needs sage.schemes
            sage: f.change_ring(phi)                                                    # needs sage.schemes
            Dynamical System of Projective Space of dimension 1 over
             Number Field in w with defining polynomial t^4 - 2
              Defn: Defined on coordinates by sending (x : y) to (x^2 + 3*y^2 : y^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<t> = QQ[]
            sage: K.<u> = QuadraticField(2)
            sage: K1.<v> = NumberField(t^4 - 2)
            sage: K2.<w> = NumberField(t^8 - 2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: phi = K1.embeddings(K2)[0]
            sage: f = DynamicalSystem_projective([x^2 + 3*y^2, y^2])                    # needs sage.schemes
            sage: f.change_ring(phi)                                                    # needs sage.schemes
            Traceback (most recent call last):
            ...
            ValueError: no canonical coercion of base ring of morphism to domain of embedding

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: H = Hom(P, P)
            sage: f = H([3*x^2, y^2])
            sage: f.change_ring(GF(3))
            Scheme endomorphism of Projective Space of dimension 1 over Finite Field of size 3
              Defn: Defined on coordinates by sending (x : y) to (0 : y^2)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([5/2*x^3 + 3*x*y^2 - y^3, 3*z^3 + y*x^2, x^3 - z^3])
            sage: f.change_ring(GF(3))
            Scheme endomorphism of Projective Space of dimension 2 over Finite Field of size 3
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^3 - y^3 : x^2*y : x^3 - z^3)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: X = P.subscheme([5*x^2 - y^2])
            sage: H = Hom(X, X)
            sage: f = H([x, y])
            sage: f.change_ring(GF(3))
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 1
            over Finite Field of size 3 defined by: -x^2 - y^2
              Defn: Defined on coordinates by sending (x : y) to (x : y)


        Check that :issue:`16834` is fixed::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y,z> = AffineSpace(RR, 3)
            sage: h = Hom(A, A)
            sage: f = h([x^2 + 1.5, y^3, z^5 - 2.0])
            sage: f.change_ring(CC)
            Scheme endomorphism of Affine Space of dimension 3 over
             Complex Field with 53 bits of precision
              Defn: Defined on coordinates by sending (x, y, z) to
                    (x^2 + 1.50000000000000, y^3, z^5 - 2.00000000000000)

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: B.<u,v> = ProjectiveSpace(QQ, 1)
            sage: h = Hom(A,B)
            sage: f = h([x^2, y^2])
            sage: f.change_ring(QQ)
            Scheme morphism:
              From: Affine Space of dimension 2 over Rational Field
              To:   Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x, y) to (x^2 : y^2)

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: H = Hom(A, A)
            sage: f = H([3*x^2/y, y^2/x])
            sage: f.change_ring(RR)                                                     # needs sage.rings.real_mpfr
            Scheme endomorphism of Affine Space of dimension 2 over Real Field with
            53 bits of precision
              Defn: Defined on coordinates by sending (x, y) to
                    (3.00000000000000*x^2/y, y^2/x)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^3 - x + 1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: f = H([x^2 + a*x*y + a^2*y^2, y^2])
            sage: emb = K.embeddings(QQbar)
            sage: f.change_ring(emb[0])
            Scheme endomorphism of Projective Space of dimension 1
             over Algebraic Field
               Defn: Defined on coordinates by sending (x : y) to
                     (x^2 + (-1.324717957244746?)*x*y + 1.754877666246693?*y^2 : y^2)
            sage: f.change_ring(emb[1])
            Scheme endomorphism of Projective Space of dimension 1
             over Algebraic Field
               Defn: Defined on coordinates by sending (x : y) to
                     (x^2 + (0.6623589786223730? - 0.5622795120623013?*I)*x*y
                      + (0.1225611668766537? - 0.744861766619745?*I)*y^2 : y^2)

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K.<v> = QuadraticField(2, embedding=QQbar(sqrt(2)))
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: f = H([x^2 + v*y^2, y^2])
            sage: f.change_ring(QQbar)
            Scheme endomorphism of Projective Space of dimension 1
             over Algebraic Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + 1.414213562373095?*y^2 : y^2)

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(-1)
            sage: K.<w> = QuadraticField(2, embedding=QQbar(-sqrt(2)))
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: X = P.subscheme(x - y)
            sage: H = End(X)
            sage: f = H([6*x^2 + 2*x*y + 16*y^2, -w*x^2 - 4*x*y - 4*y^2])
            sage: f.change_ring(QQbar)
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 1
             over Algebraic Field defined by: x - y
              Defn: Defined on coordinates by sending (x : y) to
                    (6*x^2 + 2*x*y + 16*y^2 : 1.414213562373095?*x^2 + (-4)*x*y + (-4)*y^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: f = x^6 - 2
            sage: L.<b> = NumberField(f, embedding=f.roots(QQbar)[1][0])
            sage: A.<x,y> = AffineSpace(L, 2)
            sage: H = Hom(A, A)
            sage: F = H([b*x/y, 1 + y])
            sage: F.change_ring(QQbar)
            Scheme endomorphism of Affine Space of dimension 2 over Algebraic Field
              Defn: Defined on coordinates by sending (x, y) to
                    (1.122462048309373?*x/y, y + 1)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(-1)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: H = End(A)
            sage: phi = H([x/y, y])
            sage: emb = K.embeddings(QQbar)[0]
            sage: phi.change_ring(emb)
            Scheme endomorphism of Affine Space of dimension 2 over Algebraic Field
              Defn: Defined on coordinates by sending (x, y) to (x/y, y)
        """
    def specialization(self, D=None, phi=None, homset=None):
        """
        Specialization of this map.

        Given a family of maps defined over a polynomial ring. A specialization
        is a particular member of that family. The specialization can be specified either
        by a dictionary or a :class:`SpecializationMorphism`.

        INPUT:

        - ``D`` -- dictionary (optional)

        - ``phi`` -- SpecializationMorphism (optional)

        - ``homset`` -- homset of specialized map (optional)

        OUTPUT: :class:`SchemeMorphism_polynomial`

        EXAMPLES::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: H = End(P)
            sage: f = H([x^2 + c*y^2, y^2])
            sage: f.specialization({c: 1})
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^2 + y^2 : y^2)

        ::

            sage: R.<a,b> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: H = End(P)
            sage: f = H([x^3 + a*x*y^2 + b*y^3, y^3])
            sage: from sage.rings.polynomial.flatten import SpecializationMorphism
            sage: phi = SpecializationMorphism(P.coordinate_ring(), {a: 2, b: -1})
            sage: F = f.specialization(phi=phi); F
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^3 + 2*x*y^2 - y^3 : y^3)
            sage: g = H([x^2 + a*y^2, y^2])
            sage: G = g.specialization(phi=phi)
            sage: G.parent() is F.parent()
            True
            sage: G = g.specialization(phi=phi, homset=F.parent())
            sage: G.parent() is F.parent()
            True

        ::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: X = P.subscheme([x - c*y])
            sage: H = End(X)
            sage: f = H([x^2, c*y^2])
            sage: f.specialization({c: 2})
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 1
             over Rational Field defined by: x - 2*y
                  Defn: Defined on coordinates by sending (x : y) to (x^2 : 2*y^2)

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2], domain=P)
            sage: F = f.dynatomic_polynomial(3)                                         # needs sage.libs.pari
            sage: g = F.specialization({c: 1}); g
            x^6 + x^5*y + 4*x^4*y^2 + 3*x^3*y^3 + 7*x^2*y^4 + 4*x*y^5 + 5*y^6
            sage: g == f.specialization({c:1}).dynatomic_polynomial(3)                  # needs sage.libs.pari
            True

        ::

            sage: R1.<alpha, beta> = QQ[]
            sage: A.<x> = AffineSpace(Frac(R1), 1)
            sage: f = DynamicalSystem_affine([alpha/(x^2 + 1/alpha)/(x - 1/beta^2)])
            sage: f.specialization({alpha: 5, beta: 10})
            Dynamical System of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to
                      (5/(x^3 - 1/100*x^2 + 1/5*x - 1/500))
            sage: f_5_10 = f.specialization({alpha: 5}).specialization({beta: 10})
            sage: f_5_10 == f.specialization({alpha: 5, beta: 10})
            True
        """

class SchemeMorphism_polynomial_id(SchemeMorphism_id, SchemeMorphism_polynomial):
    """
    Return the identity morphism from `X` to itself.

    INPUT:

    - ``X`` -- an affine or projective scheme

    EXAMPLES::

        sage: X = Spec(ZZ)
        sage: X.identity_morphism()  # indirect doctest
        Scheme endomorphism of Spectrum of Integer Ring
          Defn: Identity map
    """
    def __init__(self, X) -> None:
        """
        Initialize.

        TESTS::

            sage: A = AffineSpace(2, GF(3))
            sage: A.identity_morphism().defining_polynomials()
            (x0, x1)
        """

class SchemeMorphism_point(SchemeMorphism):
    """
    Base class for rational points on schemes.

    Recall that the `K`-rational points of a scheme `X` over `k` can
    be identified with the set of morphisms `\\mathrm{Spec}(K) \\to X`. In Sage,
    the rational points are implemented by such scheme morphisms.

    EXAMPLES::

        sage: from sage.schemes.generic.morphism import SchemeMorphism
        sage: f = SchemeMorphism(Spec(ZZ).Hom(Spec(ZZ)))
        sage: type(f)
        <class 'sage.schemes.generic.morphism.SchemeMorphism'>
    """
    def __getitem__(self, n):
        """
        Return the ``n``-th coordinate.

        OUTPUT: the coordinate values as an element of the base ring

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)
            sage: a = A(1,2)
            sage: a[0]
            1
            sage: a[1]
            2
        """
    def __iter__(self):
        """
        Iterate over the coordinates of the point.

        OUTPUT: an iterator

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)
            sage: a = A(1,2)
            sage: iter = a.__iter__()
            sage: next(iter)
            1
            sage: next(iter)
            2
            sage: list(a)
            [1, 2]
        """
    def __tuple__(self):
        """
        Return the coordinates as a tuple.

        OUTPUT: a tuple

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)
            sage: a = A(1,2)
            sage: tuple(a)
            (1, 2)
        """
    def __len__(self) -> int:
        """
        Return the number of coordinates.

        OUTPUT: integer. The number of coordinates used to describe the point

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)
            sage: a = A(1,2)
            sage: len(a)
            2
        """
    def scheme(self):
        """
        Return the scheme whose point is represented.

        OUTPUT: a scheme

        EXAMPLES::

            sage: A = AffineSpace(2, QQ)
            sage: a = A(1,2)
            sage: a.scheme()
            Affine Space of dimension 2 over Rational Field
        """
    def change_ring(self, R, check: bool = True):
        """
        Return a new :class:`SchemeMorphism_point` which is this point coerced
        to ``R``.

        If ``check`` is true, then the initialization checks are performed.

        INPUT:

        - ``R`` -- ring or morphism

        - ``check`` -- boolean

        OUTPUT: :class:`SchemeMorphism_point`

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: X(23,23,1).change_ring(GF(13))
            (10 : 10 : 1)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P(-2/3,1).change_ring(CC)                                             # needs sage.rings.real_mpfr
            (-0.666666666666667 : 1.00000000000000)

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: P(152,113).change_ring(Zp(5))                                         # needs sage.rings.padics
            (2 + 5^2 + 5^3 + O(5^20) : 3 + 2*5 + 4*5^2 + O(5^20))

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(-7)
            sage: O = K.maximal_order()
            sage: P.<x,y> = ProjectiveSpace(O, 1)
            sage: H = End(P)
            sage: F = H([x^2 + O(v)*y^2, y^2])
            sage: F.change_ring(K).change_ring(K.embeddings(QQbar)[0])
            Scheme endomorphism of Projective Space of dimension 1
             over Algebraic Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + (-2.645751311064591?*I)*y^2 : y^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 - x + 1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: Q = P([a + 1, 1])
            sage: emb = K.embeddings(QQbar)
            sage: Q.change_ring(emb[0])
            (1.5000000000000000? - 0.866025403784439?*I : 1)
            sage: Q.change_ring(emb[1])
            (1.5000000000000000? + 0.866025403784439?*I : 1)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: Q = P([v,1])
            sage: Q.change_ring(K.embeddings(QQbar)[0])
            (-1.414213562373095? : 1)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: f = x^6 - 2
            sage: L.<b> = NumberField(f, embedding=f.roots(QQbar)[1][0])
            sage: A.<x,y> = AffineSpace(L, 2)
            sage: P = A([b,1])
            sage: P.change_ring(QQbar)
            (1.122462048309373?, 1)
        """
    def __copy__(self):
        """
        Return a copy of the :class:`SchemeMorphism_point` ``self`` coerced to
        `R`.

        OUTPUT: :class:`SchemeMorphism_point`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: Q = P(152, 113)
            sage: Q2 = copy(Q)
            sage: Q2 is Q
            False
            sage: Q2 == Q
            True
        """
    def specialization(self, D=None, phi=None, ambient=None):
        """
        Specialization of this point.

        Given a family of points defined over a polynomial ring. A specialization
        is a particular member of that family. The specialization can be specified either
        by a dictionary or a :class:`SpecializationMorphism`.

        INPUT:

        - ``D`` -- dictionary (optional)

        - ``phi`` -- SpecializationMorphism (optional)

        - ``ambient`` -- ambient space of specialized point (optional)

        OUTPUT: :class:`SchemeMorphism_polynomial`

        EXAMPLES::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: Q = P([c,1])
            sage: Q.specialization({c: 1})
            (1 : 1)

        ::

            sage: R.<a,b> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: Q = P([a^2 + 2*a*b + 34, 1])
            sage: from sage.rings.polynomial.flatten import SpecializationMorphism
            sage: phi = SpecializationMorphism(P.coordinate_ring(), {a: 2, b: -1})
            sage: T = Q.specialization(phi=phi); T
            (34 : 1)
            sage: Q2 = P([a,1])
            sage: T2 = Q2.specialization(phi=phi)
            sage: T2.codomain() is T.codomain()
            True
            sage: T3 = Q2.specialization(phi=phi, ambient=T.codomain())
            sage: T3.codomain() is T.codomain()
            True

        ::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: X = P.subscheme([x - c*y])
            sage: Q = X([c, 1])
            sage: Q2 = Q.specialization({c:2}); Q2
            (2 : 1)
            sage: Q2.codomain()
            Closed subscheme of Projective Space of dimension 1 over Rational Field
             defined by: x - 2*y

        ::

            sage: R.<l> = PolynomialRing(QQ)
            sage: S.<k,j> = PolynomialRing(R)
            sage: K.<a,b,c,d> = S[]
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: Q = P([a^2, b^2])
            sage: Q.specialization({a: 2})
            (4 : b^2)
        """
