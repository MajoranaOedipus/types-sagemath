from _typeshed import Incomplete
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.categories.map import Section as Section
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.morphism import RingHomomorphism as RingHomomorphism
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing as OrePolynomialRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE

WORKING_CENTER_MAX_TRIES: int

class SkewPolynomialRing(OrePolynomialRing):
    Element: Incomplete
    def __init__(self, base_ring, morphism, derivation, name, sparse, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``twisting_morphism`` -- an automorphism of the base ring

        - ``name`` -- string or list of strings representing the name of
          the variables of ring

        - ``sparse`` -- boolean (default: ``False``)

        - ``category`` -- a category

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = SkewPolynomialRing(R,sigma)
            sage: S.category()
            Category of algebras over Univariate Polynomial Ring in t over Integer Ring
            sage: S([1]) + S([-1])
            0
            sage: TestSuite(S).run()
        """
    def minimal_vanishing_polynomial(self, eval_pts):
        """
        Return the minimal-degree, monic skew polynomial which vanishes at all
        the given evaluation points.

        The degree of the vanishing polynomial is at most the length of
        ``eval_pts``. Equality holds if and only if the elements of
        ``eval_pts`` are linearly independent over the fixed field of
        ``self.twisting_morphism()``.

        - ``eval_pts`` -- list of evaluation points which are linearly
          independent over the fixed field of the twisting morphism of
          the associated skew polynomial ring

        OUTPUT: the minimal vanishing polynomial

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: eval_pts = [1, t, t^2]
            sage: b = S.minimal_vanishing_polynomial(eval_pts); b
            x^3 + 4

        The minimal vanishing polynomial evaluates to 0 at each of
        the evaluation points::

            sage: eval = b.multi_point_evaluation(eval_pts); eval                       # needs sage.rings.finite_rings
            [0, 0, 0]

        If the evaluation points are linearly dependent over the fixed
        field of the twisting morphism, then the returned polynomial has
        lower degree than the number of evaluation points::

            sage: S.minimal_vanishing_polynomial([t])                                   # needs sage.rings.finite_rings
            x + 3*t^2 + 3*t
            sage: S.minimal_vanishing_polynomial([t, 3*t])                              # needs sage.rings.finite_rings
            x + 3*t^2 + 3*t
        """
    def lagrange_polynomial(self, points):
        """
        Return the minimal-degree polynomial which interpolates the given
        points.

        More precisely, given `n` pairs `(x_1, y_1), \\ldots, (x_n, y_n) \\in R^2`,
        where `R` is ``self.base_ring()``, compute a skew polynomial `p(x)`
        such that `p(x_i) = y_i` for each `i`, under the condition that
        the `x_i` are linearly independent over the fixed field of
        ``self.twisting_morphism()``.

        If the `x_i` are linearly independent over the fixed field of
        ``self.twisting_morphism()`` then such a polynomial is guaranteed
        to exist. Otherwise, it might exist depending on the `y_i`, but
        the algorithm used in this implementation does not support that,
        and so an error is always raised.

        INPUT:

        - ``points`` -- list of pairs `(x_1, y_1), \\ldots, (x_n, y_n)` of
          elements of the base ring of ``self``; the `x_i` should be linearly
          independent over the fixed field of ``self.twisting_morphism()``

        OUTPUT: the Lagrange polynomial

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: points = [(t, 3*t^2 + 4*t + 4), (t^2, 4*t)]
            sage: d = S.lagrange_polynomial(points); d
            x + t

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t + 1])
            sage: T.<x> = R['x', sigma]
            sage: points = [(1, t^2 + 3*t + 4), (t, 2*t^2 + 3*t + 1), (t^2, t^2 + 3*t + 4)]
            sage: p = T.lagrange_polynomial(points); p
            ((-t^4 - 2*t - 3)/-2)*x^2 + (-t^4 - t^3 - t^2 - 3*t - 2)*x
             + (-t^4 - 2*t^3 - 4*t^2 - 10*t - 9)/-2
            sage: p.multi_point_evaluation([1, t, t^2]) == [t^2 + 3*t + 4, 2*t^2 + 3*t + 1, t^2 + 3*t + 4]
            True

        If the `x_i` are linearly dependent over the fixed field of
        ``self.twisting_morphism()``, then an error is raised::

            sage: T.lagrange_polynomial([(t, 1), (2*t, 3)])
            Traceback (most recent call last):
            ...
            ValueError: the given evaluation points are linearly dependent over the fixed field of the twisting morphism,
            so a Lagrange polynomial could not be determined (and might not exist)
        """

class SectionSkewPolynomialCenterInjection(Section):
    """
    Section of the canonical injection of the center of a skew
    polynomial ring into this ring.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: k.<a> = GF(5^3)
        sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
        sage: Z = S.center()
        sage: iota = S.convert_map_from(Z)
        sage: sigma = iota.section()
        sage: TestSuite(sigma).run(skip=['_test_category'])
    """

class SkewPolynomialCenterInjection(RingHomomorphism):
    """
    Canonical injection of the center of a skew polynomial ring
    into this ring.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: k.<a> = GF(5^3)
        sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
        sage: Z = S.center()
        sage: iota = S.convert_map_from(Z)
        sage: TestSuite(iota).run(skip=['_test_category'])
    """
    def __init__(self, domain, codomain, embed, order) -> None:
        """
        Initialize this morphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
            sage: Z = S.center()
            sage: S.convert_map_from(Z)   # indirect doctest
            Embedding of the center of Ore Polynomial Ring in x over Finite Field in a of size 5^3 twisted by a |--> a^5 into this ring
        """
    def section(self):
        """
        Return a section of this morphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
            sage: Z = S.center()
            sage: iota = S.convert_map_from(Z)
            sage: sigma = iota.section()
            sage: sigma(x^3)
            z
        """

class SkewPolynomialRing_finite_order(SkewPolynomialRing):
    """
    A specialized class for skew polynomial rings whose twising morphism
    has finite order.

    .. SEEALSO::

        - :class:`sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing`
        - :mod:`sage.rings.polynomial.skew_polynomial_finite_order`
    """
    Element: Incomplete
    def __init__(self, base_ring, morphism, derivation, name, sparse, category=None) -> None:
        """
        Initialize this skew polynomial ring.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]; S
            Ore Polynomial Ring in x over Finite Field in t of size 5^3 twisted by t |--> t^5
            sage: S.category()
            Category of algebras over Finite Field in t of size 5^3
            sage: TestSuite(S).run()

        We check that a call to the method
        :meth:`sage.rings.polynomial.skew_polynomial_finite_order.SkewPolynomial_finite_order.is_central`
        does not affect the behaviour of default central variable names::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(7^4)
            sage: phi = k.frobenius_endomorphism()
            sage: S.<x> = k['x', phi]
            sage: (x^4).is_central()
            True
            sage: Z.<u> = S.center()
            sage: S.center() is Z
            True
        """
    def center(self, name=None, names=None, default: bool = False):
        """
        Return the center of this skew polynomial ring.

        .. NOTE::

            If `F` denotes the subring of `R` fixed by `\\sigma` and `\\sigma`
            has order `r`, the center of `K[x,\\sigma]` is `F[x^r]`, that
            is a univariate polynomial ring over `F`.

        INPUT:

        - ``name`` -- string or ``None`` (default: ``None``);
          the name for the central variable (namely `x^r`)

        - ``default`` -- boolean (default: ``False``); if ``True``,
          set the default variable name for the center to ``name``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]; S
            Ore Polynomial Ring in x over Finite Field in t of size 5^3
             twisted by t |--> t^5
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5
            sage: Z.gen()
            z

        We can pass in another variable name::

            sage: S.center(name='y')                                                    # needs sage.rings.finite_rings
            Univariate Polynomial Ring in y over Finite Field of size 5

        or use the bracket notation::

            sage: Zy.<y> = S.center(); Zy                                               # needs sage.rings.finite_rings
            Univariate Polynomial Ring in y over Finite Field of size 5
            sage: y.parent() is Zy                                                      # needs sage.rings.finite_rings
            True

        A coercion map from the center to the skew polynomial ring is set::

            sage: # needs sage.rings.finite_rings
            sage: S.has_coerce_map_from(Zy)
            True
            sage: P = y + x; P
            x^3 + x
            sage: P.parent()
            Ore Polynomial Ring in x over Finite Field in t of size 5^3
             twisted by t |--> t^5
            sage: P.parent() is S
            True

        together with a conversion map in the reverse direction::

            sage: Zy(x^6 + 2*x^3 + 3)                                                   # needs sage.rings.finite_rings
            y^2 + 2*y + 3

            sage: Zy(x^2)                                                               # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: x^2 is not in the center

        Two different skew polynomial rings can share the same center::

            sage: S1.<x1> = k['x1', Frob]                                               # needs sage.rings.finite_rings
            sage: S2.<x2> = k['x2', Frob]                                               # needs sage.rings.finite_rings
            sage: S1.center() is S2.center()                                            # needs sage.rings.finite_rings
            True

        .. RUBRIC:: About the default name of the central variable

        A priori, the default is ``z``.

        However, a variable name is given the first time this method is
        called, the given name become the default for the next calls::

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = GF(11^3)
            sage: phi = K.frobenius_endomorphism()
            sage: A.<X> = K['X', phi]
            sage: C.<u> = A.center()  # first call
            sage: C
            Univariate Polynomial Ring in u over Finite Field of size 11
            sage: A.center()  # second call: the variable name is still u
            Univariate Polynomial Ring in u over Finite Field of size 11
            sage: A.center() is C
            True

        We can update the default variable name by passing in the argument
        ``default=True``::

            sage: # needs sage.rings.finite_rings
            sage: D.<v> = A.center(default=True)
            sage: D
            Univariate Polynomial Ring in v over Finite Field of size 11
            sage: A.center()
            Univariate Polynomial Ring in v over Finite Field of size 11
            sage: A.center() is D
            True

        TESTS::

            sage: C.<a,b> = S.center()                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            IndexError: the number of names must equal the number of generators
        """

class SkewPolynomialRing_finite_field(SkewPolynomialRing_finite_order):
    """
    A specialized class for skew polynomial rings over finite fields.

    .. SEEALSO::

        - :class:`sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing`
        - :mod:`sage.rings.polynomial.skew_polynomial_finite_field`

    .. TODO::

        Add methods related to center of skew polynomial ring, irreducibility, karatsuba
        multiplication and factorization.
    """
    Element: Incomplete
    def __init__(self, base_ring, morphism, derivation, names, sparse, category=None) -> None:
        """
        This method is a constructor for a general, dense univariate skew polynomial ring
        over a finite field.

        INPUT:

        - ``base_ring`` -- a commutative ring

        - ``map`` -- an automorphism of the base ring

        - ``name`` -- string or list of strings representing the name of the variables of ring

        - ``sparse`` -- boolean (default: ``False``)

        - ``element_class`` -- class representing the type of element to be used in ring

        ..NOTE::

            Multivariate and Sparse rings are not implemented.

        EXAMPLES::

            sage: k.<t> = GF(5^3)                                                       # needs sage.rings.finite_rings
            sage: Frob = k.frobenius_endomorphism()                                     # needs sage.rings.finite_rings
            sage: T.<x> = k['x', Frob]; T                                               # needs sage.rings.finite_rings
            Ore Polynomial Ring in x over Finite Field in t of size 5^3 twisted by t |--> t^5
        """
