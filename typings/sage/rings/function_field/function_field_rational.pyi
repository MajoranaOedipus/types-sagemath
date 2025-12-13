from .element import FunctionFieldElement as FunctionFieldElement
from .element_rational import FunctionFieldElement_rational as FunctionFieldElement_rational
from .function_field import FunctionField as FunctionField
from sage.arith.functions import lcm as lcm
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.homset import Hom as Hom
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.integer import Integer as Integer
from sage.structure.category_object import CategoryObject as CategoryObject

class RationalFunctionField(FunctionField):
    """
    Rational function field in one variable, over an arbitrary base field.

    INPUT:

    - ``constant_field`` -- arbitrary field

    - ``names`` -- string or tuple of length 1

    EXAMPLES::

        sage: K.<t> = FunctionField(GF(3)); K
        Rational function field in t over Finite Field of size 3
        sage: K.gen()
        t
        sage: 1/t + t^3 + 5
        (t^4 + 2*t + 1)/t

        sage: K.<t> = FunctionField(QQ); K
        Rational function field in t over Rational Field
        sage: K.gen()
        t
        sage: 1/t + t^3 + 5
        (t^4 + 5*t + 1)/t

    There are various ways to get at the underlying fields and rings
    associated to a rational function field::

        sage: K.<t> = FunctionField(GF(7))
        sage: K.base_field()
        Rational function field in t over Finite Field of size 7
        sage: K.field()
        Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 7
        sage: K.constant_field()
        Finite Field of size 7
        sage: K.maximal_order()
        Maximal order of Rational function field in t over Finite Field of size 7

        sage: K.<t> = FunctionField(QQ)
        sage: K.base_field()
        Rational function field in t over Rational Field
        sage: K.field()
        Fraction Field of Univariate Polynomial Ring in t over Rational Field
        sage: K.constant_field()
        Rational Field
        sage: K.maximal_order()
        Maximal order of Rational function field in t over Rational Field

    We define a morphism::

        sage: K.<t> = FunctionField(QQ)
        sage: L = FunctionField(QQ, 'tbar') # give variable name as second input
        sage: K.hom(L.gen())
        Function Field morphism:
          From: Rational function field in t over Rational Field
          To:   Rational function field in tbar over Rational Field
          Defn: t |--> tbar

    Here are some calculations over a number field::

        sage: R.<x> = FunctionField(QQ)
        sage: L.<y> = R[]
        sage: F.<y> = R.extension(y^2 - (x^2+1))                                        # needs sage.rings.function_field
        sage: (y/x).divisor()                                                           # needs sage.rings.function_field
        - Place (x, y - 1)
         - Place (x, y + 1)
         + Place (x^2 + 1, y)

        sage: # needs sage.rings.number_field
        sage: A.<z> = QQ[]
        sage: NF.<i> = NumberField(z^2 + 1)
        sage: R.<x> = FunctionField(NF)
        sage: L.<y> = R[]
        sage: F.<y> = R.extension(y^2 - (x^2+1))                                        # needs sage.rings.function_field
        sage: (x/y*x.differential()).divisor()                                          # needs sage.rings.function_field
        -2*Place (1/x, 1/x*y - 1)
         - 2*Place (1/x, 1/x*y + 1)
         + Place (x, y - 1)
         + Place (x, y + 1)
        sage: (x/y).divisor()                                                           # needs sage.rings.function_field
        - Place (x - i, y)
         + Place (x, y - 1)
         + Place (x, y + 1)
         - Place (x + i, y)
    """
    Element = FunctionFieldElement_rational
    def __init__(self, constant_field, names, category=None) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: K.<t> = FunctionField(CC); K                                          # needs sage.rings.real_mpfr
            Rational function field in t over Complex Field with 53 bits of precision
            sage: TestSuite(K).run()            # long time (5s)                        # needs sage.rings.real_mpfr

            sage: FunctionField(QQ[I], 'alpha')                                         # needs sage.rings.number_field
            Rational function field in alpha over
             Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        Must be over a field::

            sage: FunctionField(ZZ, 't')
            Traceback (most recent call last):
            ...
            TypeError: constant_field must be a field
        """
    def __reduce__(self):
        """
        Return the arguments which were used to create this instance. The
        rationale for this is explained in the documentation of
        :class:`UniqueRepresentation`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: clazz,args = K.__reduce__()
            sage: clazz(*args)
            Rational function field in x over Rational Field
        """
    def __hash__(self):
        """
        Return hash of the function field.

        The hash is formed from the constant field and the variable names.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: hash(K) == hash((K.constant_base_field(), K.variable_names()))
            True
        """
    def extension(self, f, names=None):
        """
        Create an extension `L = K[y]/(f(y))` of the rational function field.

        INPUT:

        - ``f`` -- univariate polynomial over self

        - ``names`` -- string or length-1 tuple

        OUTPUT: a function field

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: K.extension(y^5 - x^3 - 3*x + x*y)                                    # needs sage.rings.function_field
            Function field in y defined by y^5 + x*y - x^3 - 3*x

        A nonintegral defining polynomial::

            sage: K.<t> = FunctionField(QQ); R.<y> = K[]
            sage: K.extension(y^3 + (1/t)*y + t^3/(t+1))                                # needs sage.rings.function_field
            Function field in y defined by y^3 + 1/t*y + t^3/(t + 1)

        The defining polynomial need not be monic or integral::

            sage: K.extension(t*y^3 + (1/t)*y + t^3/(t+1))                              # needs sage.rings.function_field
            Function field in y defined by t*y^3 + 1/t*y + t^3/(t + 1)
        """
    @cached_method
    def polynomial_ring(self, var: str = 'x'):
        """
        Return a polynomial ring in one variable over the rational function field.

        INPUT:

        - ``var`` -- string; name of the variable

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.polynomial_ring()
            Univariate Polynomial Ring in x over Rational function field in x over Rational Field
            sage: K.polynomial_ring('T')
            Univariate Polynomial Ring in T over Rational function field in x over Rational Field
        """
    def free_module(self, base=None, basis=None, map: bool = True):
        """
        Return a vector space `V` and isomorphisms from the field to `V` and
        from `V` to the field.

        This function allows us to identify the elements of this field with
        elements of a one-dimensional vector space over the field itself. This
        method exists so that all function fields (rational or not) have the
        same interface.

        INPUT:

        - ``base`` -- the base field of the vector space; must be the function
          field itself (the default)

        - ``basis`` -- (ignored) a basis for the vector space

        - ``map`` -- (default: ``True``) whether to return maps to and from the
          vector space

        OUTPUT:

        - a vector space `V` over base field

        - an isomorphism from `V` to the field

        - the inverse isomorphism from the field to `V`

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.free_module()                                                                                       # needs sage.modules
            (Vector space of dimension 1 over Rational function field in x over Rational Field,
             Isomorphism:
              From: Vector space of dimension 1 over Rational function field in x over Rational Field
              To:   Rational function field in x over Rational Field,
             Isomorphism:
              From: Rational function field in x over Rational Field
              To:   Vector space of dimension 1 over Rational function field in x over Rational Field)

        TESTS::

            sage: K.free_module()                                                                                       # needs sage.modules
            (Vector space of dimension 1 over Rational function field in x over Rational Field,
             Isomorphism:
              From: Vector space of dimension 1 over Rational function field in x over Rational Field
              To:   Rational function field in x over Rational Field,
             Isomorphism:
              From: Rational function field in x over Rational Field
              To:   Vector space of dimension 1 over Rational function field in x over Rational Field)
        """
    def random_element(self, *args, **kwds):
        """
        Create a random element of the rational function field.

        Parameters are passed to the random_element method of the
        underlying fraction field.

        EXAMPLES::

            sage: FunctionField(QQ,'alpha').random_element()   # random
            (-1/2*alpha^2 - 4)/(-12*alpha^2 + 1/2*alpha - 1/95)
        """
    def degree(self, base=None):
        """
        Return the degree over the base field of the rational function
        field.  Since the base field is the rational function field itself, the
        degree is 1.

        INPUT:

        - ``base`` -- the base field of the vector space; must be the function
          field itself (the default)

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.degree()
            1
        """
    def gen(self, n: int = 0):
        """
        Return the ``n``-th generator of the function field.  If ``n`` is not
        0, then an :class:` IndexError` is raised.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ); K.gen()
            t
            sage: K.gen().parent()
            Rational function field in t over Rational Field
            sage: K.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: Only one generator.
        """
    def ngens(self):
        """
        Return the number of generators, which is 1.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.ngens()
            1
        """
    def base_field(self):
        """
        Return the base field of the rational function field, which is just
        the function field itself.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: K.base_field()
            Rational function field in t over Finite Field of size 7
        """
    def hom(self, im_gens, base_morphism=None):
        """
        Create a homomorphism from ``self`` to another ring.

        INPUT:

        - ``im_gens`` -- exactly one element of some ring.  It must be
          invertible and transcendental over the image of
          ``base_morphism``; this is not checked.

        - ``base_morphism`` -- a homomorphism from the base field into the
          other ring; if ``None``, try to use a coercion map

        OUTPUT: a map between function fields

        EXAMPLES:

        We make a map from a rational function field to itself::

            sage: K.<x> = FunctionField(GF(7))
            sage: K.hom((x^4 + 2)/x)
            Function Field endomorphism of Rational function field in x over Finite Field of size 7
              Defn: x |--> (x^4 + 2)/x

        We construct a map from a rational function field into a
        non-rational extension field::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + 6*x^3 + x)
            sage: f = K.hom(y^2 + y  + 2); f
            Function Field morphism:
              From: Rational function field in x over Finite Field of size 7
              To:   Function field in y defined by y^3 + 6*x^3 + x
              Defn: x |--> y^2 + y + 2
            sage: f(x)
            y^2 + y + 2
            sage: f(x^2)
            5*y^2 + (x^3 + 6*x + 4)*y + 2*x^3 + 5*x + 4
        """
    def field(self):
        """
        Return the underlying field, forgetting the function field
        structure.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: K.field()
            Fraction Field of Univariate Polynomial Ring in t over Finite Field of size 7

        .. SEEALSO::

            :meth:`sage.rings.fraction_field.FractionField_1poly_field.function_field`
        """
    @cached_method
    def maximal_order(self):
        """
        Return the maximal order of the function field.

        Since this is a rational function field it is of the form `K(t)`, and the
        maximal order is by definition `K[t]`, where `K` is the constant field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.maximal_order()
            Maximal order of Rational function field in t over Rational Field
            sage: K.equation_order()
            Maximal order of Rational function field in t over Rational Field
        """
    equation_order = maximal_order
    @cached_method
    def maximal_order_infinite(self):
        """
        Return the maximal infinite order of the function field.

        By definition, this is the valuation ring of the degree valuation of
        the rational function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.maximal_order_infinite()
            Maximal infinite order of Rational function field in t over Rational Field
            sage: K.equation_order_infinite()
            Maximal infinite order of Rational function field in t over Rational Field
        """
    equation_order_infinite = maximal_order_infinite
    def constant_base_field(self):
        """
        Return the field of which the rational function field is a
        transcendental extension.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.constant_base_field()
            Rational Field
        """
    constant_field = constant_base_field
    def different(self):
        """
        Return the different of the rational function field.

        For a rational function field, the different is simply the zero
        divisor.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.different()                                                         # needs sage.modules
            0
        """
    def genus(self):
        """
        Return the genus of the function field, namely 0.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.genus()
            0
        """
    def change_variable_name(self, name):
        """
        Return a field isomorphic to this field with variable ``name``.

        INPUT:

        - ``name`` -- string or tuple consisting of a single string; the
          name of the new variable

        OUTPUT:

        A triple ``F,f,t`` where ``F`` is a rational function field, ``f`` is
        an isomorphism from ``F`` to this field, and ``t`` is the inverse of
        ``f``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: L,f,t = K.change_variable_name('y')
            sage: L,f,t
            (Rational function field in y over Rational Field,
             Function Field morphism:
              From: Rational function field in y over Rational Field
              To:   Rational function field in x over Rational Field
              Defn: y |--> x,
             Function Field morphism:
              From: Rational function field in x over Rational Field
              To:   Rational function field in y over Rational Field
              Defn: x |--> y)
            sage: L.change_variable_name('x')[0] is K
            True
        """
    def residue_field(self, place, name=None):
        """
        Return the residue field of the place along with the maps from
        and to it.

        INPUT:

        - ``place`` -- place of the function field

        - ``name`` -- string; name of the generator of the residue field

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(5))
            sage: p = F.places_finite(2)[0]                                             # needs sage.libs.pari
            sage: R, fr_R, to_R = F.residue_field(p)                                    # needs sage.libs.pari sage.rings.function_field
            sage: R                                                                     # needs sage.libs.pari sage.rings.function_field
            Finite Field in z2 of size 5^2
            sage: to_R(x) in R                                                          # needs sage.libs.pari sage.rings.function_field
            True
        """

class RationalFunctionField_char_zero(RationalFunctionField):
    """
    Rational function fields of characteristic zero.
    """
    @cached_method
    def higher_derivation(self):
        """
        Return the higher derivation for the function field.

        This is also called the Hasse-Schmidt derivation.

        EXAMPLES::

            sage: F.<x> = FunctionField(QQ)
            sage: d = F.higher_derivation()                                             # needs sage.libs.singular sage.modules
            sage: [d(x^5,i) for i in range(10)]                                         # needs sage.libs.singular sage.modules
            [x^5, 5*x^4, 10*x^3, 10*x^2, 5*x, 1, 0, 0, 0, 0]
            sage: [d(x^9,i) for i in range(10)]                                         # needs sage.libs.singular sage.modules
            [x^9, 9*x^8, 36*x^7, 84*x^6, 126*x^5, 126*x^4, 84*x^3, 36*x^2, 9*x, 1]
        """

class RationalFunctionField_global(RationalFunctionField):
    """
    Rational function field over finite fields.
    """
    def places(self, degree: int = 1):
        """
        Return all places of the degree.

        INPUT:

        - ``degree`` -- (default: 1) a positive integer

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(5))
            sage: F.places()                                                            # needs sage.libs.pari
            [Place (1/x),
             Place (x),
             Place (x + 1),
             Place (x + 2),
             Place (x + 3),
             Place (x + 4)]
        """
    def places_finite(self, degree: int = 1):
        """
        Return the finite places of the degree.

        INPUT:

        - ``degree`` -- (default: 1) a positive integer

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(5))
            sage: F.places_finite()                                                     # needs sage.libs.pari
            [Place (x), Place (x + 1), Place (x + 2), Place (x + 3), Place (x + 4)]
        """
    def place_infinite(self):
        """
        Return the unique place at infinity.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(5))
            sage: F.place_infinite()
            Place (1/x)
        """
    def get_place(self, degree):
        """
        Return a place of ``degree``.

        INPUT:

        - ``degree`` -- positive integer

        EXAMPLES::

            sage: F.<a> = GF(2)
            sage: K.<x> = FunctionField(F)
            sage: K.get_place(1)                                                        # needs sage.libs.pari
            Place (x)
            sage: K.get_place(2)                                                        # needs sage.libs.pari
            Place (x^2 + x + 1)
            sage: K.get_place(3)                                                        # needs sage.libs.pari
            Place (x^3 + x + 1)
            sage: K.get_place(4)                                                        # needs sage.libs.pari
            Place (x^4 + x + 1)
            sage: K.get_place(5)                                                        # needs sage.libs.pari
            Place (x^5 + x^2 + 1)
        """
    @cached_method
    def higher_derivation(self):
        """
        Return the higher derivation for the function field.

        This is also called the Hasse-Schmidt derivation.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(5))
            sage: d = F.higher_derivation()                                             # needs sage.rings.function_field
            sage: [d(x^5,i) for i in range(10)]                                         # needs sage.rings.function_field
            [x^5, 0, 0, 0, 0, 1, 0, 0, 0, 0]
            sage: [d(x^7,i) for i in range(10)]                                         # needs sage.rings.function_field
            [x^7, 2*x^6, x^5, 0, 0, x^2, 2*x, 1, 0, 0]
        """
