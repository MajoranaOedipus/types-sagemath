from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.categories.morphism import Morphism as Morphism, SetMorphism as SetMorphism
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.morphism import RingHomomorphism as RingHomomorphism

class FunctionFieldVectorSpaceIsomorphism(Morphism):
    """
    Base class for isomorphisms between function fields and vector spaces.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
        sage: V, f, t = L.vector_space()
        sage: isinstance(f, sage.rings.function_field.maps.FunctionFieldVectorSpaceIsomorphism)
        True
    """
    def is_injective(self) -> bool:
        """
        Return ``True``, since the isomorphism is injective.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space()
            sage: f.is_injective()
            True
        """
    def is_surjective(self) -> bool:
        """
        Return ``True``, since the isomorphism is surjective.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space()
            sage: f.is_surjective()
            True
        """
    def __hash__(self):
        """
        Return a hash value of this map.

        This implementation assumes that this isomorphism is defined by its
        domain and codomain. Isomorphisms for which this is not true should
        override this implementation.

        EXAMPLES::

            sage: K = QQ['x'].fraction_field()
            sage: L = K.function_field()
            sage: f = K.coerce_map_from(L)
            sage: hash(f) == hash(f)
            True
        """

class MapVectorSpaceToFunctionField(FunctionFieldVectorSpaceIsomorphism):
    """
    Isomorphism from a vector space to a function field.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
        sage: V, f, t = L.vector_space(); f
        Isomorphism:
          From: Vector space of dimension 2 over Rational function field in x over Rational Field
          To:   Function field in y defined by y^2 - x*y + 4*x^3
    """
    def __init__(self, V, K) -> None:
        """
        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space(); type(f)
            <class 'sage.rings.function_field.maps.MapVectorSpaceToFunctionField'>
        """
    def domain(self):
        """
        Return the vector space which is the domain of the isomorphism.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space()
            sage: f.domain()
            Vector space of dimension 2 over Rational function field in x over Rational Field
        """
    def codomain(self):
        """
        Return the function field which is the codomain of the isomorphism.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space()
            sage: f.codomain()
            Function field in y defined by y^2 - x*y + 4*x^3
        """

class MapFunctionFieldToVectorSpace(FunctionFieldVectorSpaceIsomorphism):
    """
    Isomorphism from a function field to a vector space.

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
        sage: V, f, t = L.vector_space(); t
        Isomorphism:
          From: Function field in y defined by y^2 - x*y + 4*x^3
          To:   Vector space of dimension 2 over Rational function field in x over Rational Field
    """
    def __init__(self, K, V) -> None:
        """
        Initialize.

        INPUT:

        - ``K`` -- function field

        - ``V`` -- vector space isomorphic to the function field

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x*y + 4*x^3)
            sage: V, f, t = L.vector_space()
            sage: TestSuite(t).run(skip='_test_category')
        """

class FunctionFieldMorphism(RingHomomorphism):
    """
    Base class for morphisms between function fields.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: f = K.hom(1/x); f
        Function Field endomorphism of Rational function field in x over Rational Field
          Defn: x |--> 1/x
    """
    def __init__(self, parent, im_gen, base_morphism) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: f = K.hom(1/x); f
            Function Field endomorphism of Rational function field in x over Rational Field
              Defn: x |--> 1/x
            sage: TestSuite(f).run(skip='_test_category')
        """

class FunctionFieldMorphism_polymod(FunctionFieldMorphism):
    """
    Morphism from a finite extension of a function field to a function field.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings sage.rings.function_field
        sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
        sage: L.<y> = K.extension(y^3 + 6*x^3 + x)
        sage: f = L.hom(y*2); f
        Function Field endomorphism of Function field in y defined by y^3 + 6*x^3 + x
          Defn: y |--> 2*y
        sage: factor(L.polynomial())
        y^3 + 6*x^3 + x
        sage: f(y).charpoly('y')
        y^3 + 6*x^3 + x
    """
    def __init__(self, parent, im_gen, base_morphism) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + 6*x^3 + x)
            sage: f = L.hom(y*2)
            sage: TestSuite(f).run(skip='_test_category')
        """

class FunctionFieldMorphism_rational(FunctionFieldMorphism):
    """
    Morphism from a rational function field to a function field.
    """
    def __init__(self, parent, im_gen, base_morphism) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(7))
            sage: f = K.hom(1/x); f
            Function Field endomorphism of Rational function field in x over Finite Field of size 7
              Defn: x |--> 1/x
        """

class FunctionFieldConversionToConstantBaseField(Map):
    """
    Conversion map from the function field to its constant base field.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: QQ.convert_map_from(K)
        Conversion map:
          From: Rational function field in x over Rational Field
          To:   Rational Field
    """
    def __init__(self, parent) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: f = QQ.convert_map_from(K)
            sage: from sage.rings.function_field.maps import FunctionFieldConversionToConstantBaseField
            sage: isinstance(f, FunctionFieldConversionToConstantBaseField)
            True
        """

class FunctionFieldToFractionField(FunctionFieldVectorSpaceIsomorphism):
    """
    Isomorphism from rational function field to the isomorphic fraction
    field of a polynomial ring.

    EXAMPLES::

        sage: K = QQ['x'].fraction_field()
        sage: L = K.function_field()
        sage: f = K.coerce_map_from(L); f
        Isomorphism:
          From: Rational function field in x over Rational Field
          To:   Fraction Field of Univariate Polynomial Ring in x over Rational Field

    .. SEEALSO::

        :class:`FractionFieldToFunctionField`

    TESTS::

        sage: from sage.rings.function_field.maps import FunctionFieldToFractionField
        sage: isinstance(f, FunctionFieldToFractionField)
        True
        sage: TestSuite(f).run()
    """
    def section(self):
        """
        Return the inverse map of this isomorphism.

        EXAMPLES::

            sage: K = QQ['x'].fraction_field()
            sage: L = K.function_field()
            sage: f = K.coerce_map_from(L)
            sage: f.section()
            Isomorphism:
                From: Fraction Field of Univariate Polynomial Ring in x over Rational Field
                To:   Rational function field in x over Rational Field
        """

class FractionFieldToFunctionField(FunctionFieldVectorSpaceIsomorphism):
    """
    Isomorphism from a fraction field of a polynomial ring to the isomorphic
    function field.

    EXAMPLES::

        sage: K = QQ['x'].fraction_field()
        sage: L = K.function_field()
        sage: f = L.coerce_map_from(K); f
        Isomorphism:
            From: Fraction Field of Univariate Polynomial Ring in x over Rational Field
            To:   Rational function field in x over Rational Field

    .. SEEALSO::

        :class:`FunctionFieldToFractionField`

    TESTS::

        sage: from sage.rings.function_field.maps import FractionFieldToFunctionField
        sage: isinstance(f, FractionFieldToFunctionField)
        True
        sage: TestSuite(f).run()
    """
    def section(self):
        """
        Return the inverse map of this isomorphism.

        EXAMPLES::

            sage: K = QQ['x'].fraction_field()
            sage: L = K.function_field()
            sage: f = L.coerce_map_from(K)
            sage: f.section()
            Isomorphism:
                From: Rational function field in x over Rational Field
                To:   Fraction Field of Univariate Polynomial Ring in x over Rational Field
        """

class FunctionFieldCompletion(Map):
    """
    Completions on function fields.

    INPUT:

    - ``field`` -- function field

    - ``place`` -- place of the function field

    - ``name`` -- string for the name of the series variable

    - ``prec`` -- positive integer; default precision

    - ``gen_name`` -- string; name of the generator of the residue
      field; used only when place is non-rational

    EXAMPLES::

        sage: # needs sage.rings.finite_rings sage.rings.function_field
        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
        sage: p = L.places_finite()[0]
        sage: m = L.completion(p)
        sage: m
        Completion map:
          From: Function field in y defined by y^2 + y + (x^2 + 1)/x
          To:   Laurent Series Ring in s over Finite Field of size 2
        sage: m(x)
        s^2 + s^3 + s^4 + s^5 + s^7 + s^8 + s^9 + s^10 + s^12 + s^13
        + s^15 + s^16 + s^17 + s^19 + O(s^22)
        sage: m(y)
        s^-1 + 1 + s^3 + s^5 + s^7 + s^9 + s^13 + s^15 + s^17 + O(s^19)
        sage: m(x*y) == m(x) * m(y)
        True
        sage: m(x+y) == m(x) + m(y)
        True

    The variable name of the series can be supplied. If the place is not
    rational such that the residue field is a proper extension of the constant
    field, you can also specify the generator name of the extension::

        sage: # needs sage.rings.finite_rings sage.rings.function_field
        sage: p2 = L.places_finite(2)[0]
        sage: p2
        Place (x^2 + x + 1, x*y + 1)
        sage: m2 = L.completion(p2, 't', gen_name='b')
        sage: m2(x)
        (b + 1) + t + t^2 + t^4 + t^8 + t^16 + O(t^20)
        sage: m2(y)
        b + b*t + b*t^3 + b*t^4 + (b + 1)*t^5 + (b + 1)*t^7 + b*t^9 + b*t^11
        + b*t^12 + b*t^13 + b*t^15 + b*t^16 + (b + 1)*t^17 + (b + 1)*t^19 + O(t^20)
    """
    def __init__(self, field, place, name=None, prec=None, gen_name=None) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: m = L.completion(p)
            sage: m
            Completion map:
              From: Function field in y defined by y^2 + y + (x^2 + 1)/x
              To:   Laurent Series Ring in s over Finite Field of size 2
        """
    def default_precision(self):
        """
        Return the default precision.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: m = L.completion(p)
            sage: m.default_precision()
            20
        """

class FunctionFieldRingMorphism(SetMorphism):
    """
    Ring homomorphism.
    """
class FunctionFieldLinearMap(SetMorphism):
    """
    Linear map to function fields.
    """
class FunctionFieldLinearMapSection(SetMorphism):
    """
    Section of linear map from function fields.
    """
