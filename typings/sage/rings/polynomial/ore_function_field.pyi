from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.categories.map import Section as Section
from sage.rings.morphism import RingHomomorphism as RingHomomorphism
from sage.rings.polynomial.ore_function_element import OreFunctionBaseringInjection as OreFunctionBaseringInjection, OreFunction_with_large_center as OreFunction_with_large_center
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing as OrePolynomialRing
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

WORKING_CENTER_MAX_TRIES: int

class OreFunctionField(Parent, UniqueRepresentation):
    """
    A class for fraction fields of Ore polynomial rings.
    """
    Element: Incomplete
    def __init__(self, ring, category=None) -> None:
        """
        Initialize this Ore function field.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(11^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: der = k.derivation(a, twist=Frob)
            sage: S.<x> = k['x', der]
            sage: K = S.fraction_field()
            sage: TestSuite(K).run()
        """
    def change_var(self, var):
        """
        Return the Ore function field in variable ``var`` with the same base
        ring, twisting morphism and twisting derivation as ``self``.

        INPUT:

        - ``var`` -- string representing the name of the new variable

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: R.<x> = OrePolynomialRing(k,Frob)
            sage: K = R.fraction_field()
            sage: K
            Ore Function Field in x over Finite Field in t of size 5^3 twisted by t |--> t^5
            sage: Ky = K.change_var('y'); Ky
            Ore Function Field in y over Finite Field in t of size 5^3 twisted by t |--> t^5
            sage: Ky is K.change_var('y')
            True
        """
    def characteristic(self):
        """
        Return the characteristic of this Ore function field.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S = R['x',sigma]
            sage: S.fraction_field().characteristic()                                   # needs sage.rings.function_field
            0

            sage: # needs sage.rings.finite_rings
            sage: k.<u> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S = k['y',Frob]
            sage: S.fraction_field().characteristic()                                   # needs sage.rings.function_field
            5
        """
    def twisting_morphism(self, n: int = 1):
        """
        Return the twisting endomorphism defining this Ore function field iterated ``n`` times
        or ``None`` if this Ore function field is not twisted by an endomorphism.

        INPUT:

        - ``n`` -- integer (default: 1)

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: K = S.fraction_field()                                                # needs sage.rings.function_field
            sage: K.twisting_morphism()                                                 # needs sage.rings.function_field
            Ring endomorphism of
             Fraction Field of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> t + 1

        When the Ore polynomial ring is only twisted by a derivation, this
        method returns nothing::

            sage: der = R.derivation()
            sage: A.<d> = R['x', der]
            sage: F = A.fraction_field()                                                # needs sage.rings.function_field
            sage: F.twisting_morphism()                                                 # needs sage.rings.function_field

        .. SEEALSO::

            :meth:`sage.rings.polynomial.ore_polynomial_element.OrePolynomial.twisting_morphism`,
            :meth:`twisting_derivation`
        """
    def twisting_derivation(self):
        """
        Return the twisting derivation defining this Ore function field
        or ``None`` if this Ore function field is not twisted by a derivation.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: der = R.derivation(); der
            d/dt
            sage: A.<d> = R['d', der]
            sage: F = A.fraction_field()
            sage: F.twisting_derivation()
            d/dt

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.twisting_derivation()

        .. SEEALSO::

            :meth:`sage.rings.polynomial.ore_polynomial_element.OrePolynomial.twisting_derivation`,
            :meth:`twisting_morphism`
        """
    def gen(self, n: int = 0):
        """
        Return the indeterminate generator of this Ore function field.

        INPUT:

        - ``n`` -- index of generator to return (default: 0); exists for
          compatibility with other polynomial rings

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^4)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.gen()
            x
        """
    def gens(self) -> tuple:
        """
        Return the tuple of generators of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^4)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.gens()
            (x,)
        """
    parameter = gen
    def gens_dict(self) -> dict:
        """
        Return a {name: variable} dictionary of the generators of
        this Ore function field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = OrePolynomialRing(R, sigma)
            sage: K = S.fraction_field()
            sage: K.gens_dict()
            {'x': x}
        """
    def is_finite(self) -> bool:
        """
        Return ``False`` since Ore function field are not finite.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: k.is_finite()
            True
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: K = S.fraction_field()
            sage: K.is_finite()
            False
        """
    def is_exact(self) -> bool:
        """
        Return ``True`` if elements of this Ore function field are exact.
        This happens if and only if elements of the base ring are exact.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.is_exact()
            True

            sage: # needs sage.rings.padics
            sage: k.<u> = Qq(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.is_exact()
            False
        """
    def is_sparse(self) -> bool:
        """
        Return ``True`` if the elements of this Ore function field are sparsely
        represented.

        .. WARNING::

            Since sparse Ore polynomials are not yet implemented, this
            function always returns ``False``.

        EXAMPLES::

            sage: # needs sage.rings.function_field sage.rings.real_mpfr
            sage: R.<t> = RR[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: K = S.fraction_field()
            sage: K.is_sparse()
            False
        """
    def ngens(self) -> int:
        """
        Return the number of generators of this Ore function field,
        which is `1`.

        EXAMPLES::

            sage: # needs sage.rings.function_field sage.rings.real_mpfr
            sage: R.<t> = RR[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: K = S.fraction_field()
            sage: K.ngens()
            1
        """
    def random_element(self, degree: int = 2, monic: bool = False, *args, **kwds):
        """
        Return a random Ore function in this field.

        INPUT:

        - ``degree`` -- (default: 2) an integer or a list of
          two integers; the degrees of the denominator and numerator

        - ``monic`` -- boolean (default: ``False``); if ``True``, return a monic
          Ore function with monic numerator and denominator

        - ``*args``, ``**kwds`` -- passed in to the :meth:`random_element`
          method for the base ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: K.random_element()              # random
            (x^2 + (2*t^2 + t + 1)*x + 2*t^2 + 2*t + 3)^(-1)
            * ((2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2)
            sage: K.random_element(monic=True)    # random
            (x^2 + (4*t^2 + 3*t + 4)*x + 4*t^2 + t)^(-1)
            * (x^2 + (2*t^2 + t + 3)*x + 3*t^2 + t + 2)
            sage: K.random_element(degree=3)      # random
            (x^3 + (2*t^2 + 3)*x^2 + (2*t^2 + 4)*x + t + 3)^(-1)
            * ((t + 4)*x^3 + (4*t^2 + 2*t + 2)*x^2 + (2*t^2 + 3*t + 3)*x + 3*t^2 + 3*t + 1)
            sage: K.random_element(degree=[2,5])  # random
            (x^2 + (4*t^2 + 2*t + 2)*x + 4*t^2 + t + 2)^(-1)
            * ((3*t^2 + t + 1)*x^5 + (2*t^2 + 2*t)*x^4 + (t^2 + 2*t + 4)*x^3
               + (3*t^2 + 2*t)*x^2 + (t^2 + t + 4)*x)
        """
    def is_field(self, proof: bool = False) -> bool:
        """
        Return always ``True`` since Ore function field are (skew) fields.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: S.is_field()
            False
            sage: K.is_field()
            True

        TESTS:

        We check that :issue:`31470` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = k['x', k.frobenius_endomorphism()]
            sage: K = S.fraction_field()
            sage: zero_matrix(K, 2).row(0)
            ...
            (0, 0)
        """
    def fraction_field(self):
        """
        Return the fraction field of this Ore function field,
        i.e. this Ore function field itself.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: K = A.fraction_field(); K
            Ore Function Field in d
             over Fraction Field of Univariate Polynomial Ring in t over Rational Field
             twisted by d/dt
            sage: K.fraction_field()
            Ore Function Field in d
             over Fraction Field of Univariate Polynomial Ring in t over Rational Field
             twisted by d/dt
            sage: K.fraction_field() is K
            True
        """

class SectionOreFunctionCenterInjection(Section):
    """
    Section of the canonical injection of the center of a Ore
    function field into this field
    """
    def __init__(self, embed) -> None:
        """
        Initialize this map.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = OrePolynomialRing(k, k.frobenius_endomorphism())
            sage: K = S.fraction_field()
            sage: Z = K.center()
            sage: iota = K.coerce_map_from(Z)
            sage: sigma = iota.section()
            sage: TestSuite(sigma).run(skip=['_test_category'])
        """

class OreFunctionCenterInjection(RingHomomorphism):
    """
    Canonical injection of the center of a Ore function field
    into this field.
    """
    def __init__(self, domain, codomain, ringembed) -> None:
        """
        Initialize this morphism.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
            sage: K = S.fraction_field()
            sage: Z = K.center()
            sage: iota = K.coerce_map_from(Z)
            sage: TestSuite(iota).run(skip=['_test_category'])
        """
    def section(self):
        """
        Return a section of this morphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: S.<x> = SkewPolynomialRing(k, k.frobenius_endomorphism())
            sage: K = S.fraction_field()
            sage: Z = K.center()
            sage: iota = K.coerce_map_from(Z)
            sage: sigma = iota.section()
            sage: sigma(x^3 / (x^6 + 1))
            z/(z^2 + 1)
        """

class OreFunctionField_with_large_center(OreFunctionField):
    """
    A specialized class for Ore polynomial fields whose center has finite index.
    """
    Element: Incomplete
    def __init__(self, ring, category=None) -> None:
        """
        Initialize this Ore function field.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: K = S.fraction_field()
            sage: TestSuite(K).run()
        """
    def center(self, name=None, names=None, default: bool = False):
        """
        Return the center of this Ore function field.

        .. NOTE::

            One can prove that the center is a field of rational functions
            over a subfield of the base ring of this Ore function field.

        INPUT:

        - ``name`` -- string or ``None`` (default: ``None``);
          the name for the central variable

        - ``default`` -- boolean (default: ``False``); if ``True``,
          set the default variable name for the center to ``name``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: K = S.fraction_field()
            sage: Z = K.center(); Z
            Fraction Field of Univariate Polynomial Ring in z over Finite Field of size 5

        We can pass in another variable name::

            sage: K.center(name='y')                                                    # needs sage.rings.finite_rings
            Fraction Field of Univariate Polynomial Ring in y over Finite Field of size 5

        or use the bracket notation::

            sage: Zy.<y> = K.center(); Zy                                               # needs sage.rings.finite_rings
            Fraction Field of Univariate Polynomial Ring in y over Finite Field of size 5

        A coercion map from the center to the Ore function field is set::

            sage: K.has_coerce_map_from(Zy)                                             # needs sage.rings.finite_rings
            True

        and pushout works::

            sage: # needs sage.rings.finite_rings
            sage: x.parent()
            Ore Polynomial Ring in x over Finite Field in t of size 5^3 twisted by t |--> t^5
            sage: y.parent()
            Fraction Field of Univariate Polynomial Ring in y over Finite Field of size 5
            sage: P = x + y; P
            x^3 + x
            sage: P.parent()
            Ore Function Field in x over Finite Field in t of size 5^3 twisted by t |--> t^5

        A conversion map in the reverse direction is also set::

            sage: # needs sage.rings.finite_rings
            sage: Zy(x^(-6) + 2)
            (2*y^2 + 1)/y^2
            sage: Zy(1/x^2)
            Traceback (most recent call last):
            ...
            ValueError: x^(-2) is not in the center

        ABOUT THE DEFAULT NAME OF THE CENTRAL VARIABLE:

        A priori, the default is ``z``.

        However, a variable name is given the first time this method is
        called, the given name become the default for the next calls::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(11^3)
            sage: phi = k.frobenius_endomorphism()
            sage: S.<X> = k['X', phi]
            sage: K = S.fraction_field()
            sage: C.<u> = K.center()  # first call
            sage: C
            Fraction Field of Univariate Polynomial Ring in u over Finite Field of size 11
            sage: K.center()  # second call: the variable name is still u
            Fraction Field of Univariate Polynomial Ring in u over Finite Field of size 11

        We can update the default variable name by passing in the argument
        ``default=True``::

            sage: # needs sage.rings.finite_rings
            sage: D.<v> = K.center(default=True)
            sage: D
            Fraction Field of Univariate Polynomial Ring in v over Finite Field of size 11
            sage: K.center()
            Fraction Field of Univariate Polynomial Ring in v over Finite Field of size 11
        """
