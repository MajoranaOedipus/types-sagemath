from .element import FunctionFieldElement as FunctionFieldElement
from .element_polymod import FunctionFieldElement_polymod as FunctionFieldElement_polymod
from .function_field import FunctionField as FunctionField
from .function_field_rational import RationalFunctionField as RationalFunctionField
from sage.arith.functions import lcm as lcm
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.homset import Hom as Hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar_decorators import handle_AA_and_QQbar as handle_AA_and_QQbar

class FunctionField_polymod(FunctionField):
    """
    Function fields defined by a univariate polynomial, as an extension of the
    base field.

    INPUT:

    - ``polynomial`` -- univariate polynomial over a function field

    - ``names`` -- tuple of length 1 or string; variable names

    - ``category`` -- category (default: category of function fields)

    EXAMPLES:

    We make a function field defined by a degree 5 polynomial over the
    rational function field over the rational numbers::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x)); L
        Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x

    We next make a function field over the above nontrivial function
    field L::

        sage: S.<z> = L[]
        sage: M.<z> = L.extension(z^2 + y*z + y); M
        Function field in z defined by z^2 + y*z + y
        sage: 1/z
        ((-x/(x^4 + 1))*y^4 + 2*x^2/(x^4 + 1))*z - 1
        sage: z * (1/z)
        1

    We drill down the tower of function fields::

        sage: M.base_field()
        Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
        sage: M.base_field().base_field()
        Rational function field in x over Rational Field
        sage: M.base_field().base_field().constant_field()
        Rational Field
        sage: M.constant_base_field()
        Rational Field

    .. WARNING::

        It is not checked if the polynomial used to define the function field is irreducible
        Hence it is not guaranteed that this object really is a field!
        This is illustrated below.

    ::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(x^2 - y^2)
        sage: (y - x)*(y + x)
        0
        sage: 1/(y - x)
        1
        sage: y - x == 0; y + x == 0
        False
        False
    """
    Element = FunctionFieldElement_polymod
    def __init__(self, polynomial, names, category=None) -> None:
        """
        Create a function field defined as an extension of another function
        field by adjoining a root of a univariate polynomial.

        EXAMPLES:

        We create an extension of a function field::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L = K.extension(y^5 - x^3 - 3*x + x*y); L
            Function field in y defined by y^5 + x*y - x^3 - 3*x
            sage: TestSuite(L).run(max_runs=512)   # long time (15s)

        We can set the variable name, which doesn't have to be y::

            sage: L.<w> = K.extension(y^5 - x^3 - 3*x + x*y); L
            Function field in w defined by w^5 + x*w - x^3 - 3*x

        TESTS:

        Test that :issue:`17033` is fixed::

            sage: K.<t> = FunctionField(QQ)
            sage: R.<x> = QQ[]
            sage: M.<z> = K.extension(x^7 - x - t)
            sage: M(x)
            z
            sage: M('z')
            z
            sage: M('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to evaluate 'x' in Fraction Field of Univariate
            Polynomial Ring in t over Rational Field
        """
    def __hash__(self):
        """
        Return hash of the function field.

        The hash value is equal to the hash of the defining polynomial.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L = K.extension(y^5 - x^3 - 3*x + x*y)
            sage: hash(L) == hash(L.polynomial())
            True
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of the function field. By default, `n` is 0; any other
        value of `n` leads to an error. The generator is the class of `y`, if we view
        the function field as being presented as `K[y]/(f(y))`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.gen()
            y
            sage: L.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: there is only one generator
        """
    def ngens(self):
        """
        Return the number of generators of the function field over its base
        field. This is by definition 1.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.ngens()
            1
        """
    def monic_integral_model(self, names=None):
        """
        Return a function field isomorphic to this field but which is an
        extension of a rational function field with defining polynomial that is
        monic and integral over the constant base field.

        INPUT:

        - ``names`` -- string or tuple of up to two strings (default:
          ``None``); the name of the generator of the field, and the name of
          the generator of the underlying rational function field (if a tuple).
          If not given, then the names are chosen automatically.

        OUTPUT:

        A triple ``(F,f,t)`` where ``F`` is a function field, ``f`` is an
        isomorphism from ``F`` to this field, and ``t`` is the inverse of
        ``f``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(x^2*y^5 - 1/x); L
            Function field in y defined by x^2*y^5 - 1/x
            sage: A, from_A, to_A = L.monic_integral_model('z')
            sage: A
            Function field in z defined by z^5 - x^12
            sage: from_A
            Function Field morphism:
              From: Function field in z defined by z^5 - x^12
              To:   Function field in y defined by x^2*y^5 - 1/x
              Defn: z |--> x^3*y
                    x |--> x
            sage: to_A
            Function Field morphism:
              From: Function field in y defined by x^2*y^5 - 1/x
              To:   Function field in z defined by z^5 - x^12
              Defn: y |--> 1/x^3*z
                    x |--> x
            sage: to_A(y)
            1/x^3*z
            sage: from_A(to_A(y))
            y
            sage: from_A(to_A(1/y))
            x^3*y^4
            sage: from_A(to_A(1/y)) == 1/y
            True

        This also works for towers of function fields::

            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2*y - 1/x)
            sage: M.monic_integral_model()
            (Function field in z_ defined by z_^10 - x^18,
             Function Field morphism:
              From: Function field in z_ defined by z_^10 - x^18
              To:   Function field in z defined by y*z^2 - 1/x
              Defn: z_ |--> x^2*z
                    x |--> x, Function Field morphism:
              From: Function field in z defined by y*z^2 - 1/x
              To:   Function field in z_ defined by z_^10 - x^18
              Defn: z |--> 1/x^2*z_
                    y |--> 1/x^15*z_^8
                    x |--> x)

        TESTS:

        If the field is already a monic integral extension, then it is returned
        unchanged::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: L.monic_integral_model()
            (Function field in y defined by y^2 - x,
             Function Field endomorphism of Function field in y defined by y^2 - x
              Defn: y |--> y
                    x |--> x, Function Field endomorphism of Function field in y defined by y^2 - x
              Defn: y |--> y
                    x |--> x)

        unless ``names`` does not match with the current names::

            sage: L.monic_integral_model(names=('yy','xx'))
            (Function field in yy defined by yy^2 - xx,
             Function Field morphism:
              From: Function field in yy defined by yy^2 - xx
              To:   Function field in y defined by y^2 - x
              Defn: yy |--> y
                    xx |--> x, Function Field morphism:
              From: Function field in y defined by y^2 - x
              To:   Function field in yy defined by yy^2 - xx
              Defn: y |--> yy
                    x |--> xx)
        """
    def constant_field(self) -> None:
        """
        Return the algebraic closure of the constant field of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^5 - x)                                          # needs sage.rings.finite_rings
            sage: L.constant_field()                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def constant_base_field(self):
        """
        Return the base constant field of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x)); L
            Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
            sage: L.constant_base_field()
            Rational Field
            sage: S.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: M.constant_base_field()
            Rational Field
        """
    def degree(self, base=None):
        """
        Return the degree of the function field over the function field ``base``.

        INPUT:

        - ``base`` -- a function field (default: ``None``), a function field
          from which this field has been constructed as a finite extension

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x)); L
            Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
            sage: L.degree()
            5
            sage: L.degree(L)
            1

            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: M.degree(L)
            2
            sage: M.degree(K)
            10

        TESTS::

            sage: L.degree(M)
            Traceback (most recent call last):
            ...
            ValueError: base must be the rational function field itself
        """
    def base_field(self):
        """
        Return the base field of the function field. This function field is
        presented as `L = K[y]/(f(y))`, and the base field is by definition the
        field `K`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.base_field()
            Rational function field in x over Rational Field
        """
    def random_element(self, *args, **kwds):
        """
        Create a random element of the function field. Parameters are passed
        onto the random_element method of the base_field.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - (x^2 + x))
            sage: L.random_element() # random
            ((x^2 - x + 2/3)/(x^2 + 1/3*x - 1))*y^2 + ((-1/4*x^2 + 1/2*x - 1)/(-5/2*x + 2/3))*y
            + (-1/2*x^2 - 4)/(-12*x^2 + 1/2*x - 1/95)
        """
    def polynomial(self):
        """
        Return the univariate polynomial that defines the function field, that
        is, the polynomial `f(y)` so that the function field is of the form
        `K[y]/(f(y))`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.polynomial()
            y^5 - 2*x*y + (-x^4 - 1)/x
        """
    def is_separable(self, base=None):
        """
        Return whether this is a separable extension of ``base``.

        INPUT:

        - ``base`` -- a function field from which this field has been created
          as an extension or ``None`` (default: ``None``); if ``None``, then
          return whether this is a separable extension over its base field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: L.is_separable()
            False
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y)
            sage: M.is_separable()
            True
            sage: M.is_separable(K)
            False

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(5))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.is_separable()
            True

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(5))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - 1)
            sage: L.is_separable()
            False
        """
    def polynomial_ring(self):
        """
        Return the polynomial ring used to represent elements of the
        function field.  If we view the function field as being presented
        as `K[y]/(f(y))`, then this function returns the ring `K[y]`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.polynomial_ring()
            Univariate Polynomial Ring in y over Rational function field in x over Rational Field
        """
    def free_module(self, base=None, basis=None, map: bool = True):
        """
        Return a vector space and isomorphisms from the field to and from the
        vector space.

        This function allows us to identify the elements of this field with
        elements of a vector space over the base field, which is useful for
        representation and arithmetic with orders, ideals, etc.

        INPUT:

        - ``base`` -- a function field (default: ``None``), the returned vector
          space is over this subfield `R`, which defaults to the base field of this
          function field.

        - ``basis`` -- a basis for this field over the base

        - ``maps`` -- boolean (default: ``True``); whether to return
          `R`-linear maps to and from `V`

        OUTPUT:

        - a vector space over the base function field

        - an isomorphism from the vector space to the field (if requested)

        - an isomorphism from the field to the vector space (if requested)

        EXAMPLES:

        We define a function field::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x)); L
            Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x

        We get the vector spaces, and maps back and forth::

            sage: # needs sage.modules
            sage: V, from_V, to_V = L.free_module()
            sage: V
            Vector space of dimension 5 over Rational function field in x over Rational Field
            sage: from_V
            Isomorphism:
              From: Vector space of dimension 5 over Rational function field in x over Rational Field
              To:   Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
            sage: to_V
            Isomorphism:
              From: Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
              To:   Vector space of dimension 5 over Rational function field in x over Rational Field

        We convert an element of the vector space back to the function field::

            sage: from_V(V.1)                                                           # needs sage.modules
            y

        We define an interesting element of the function field::

            sage: a = 1/L.0; a                                                          # needs sage.modules
            (x/(x^4 + 1))*y^4 - 2*x^2/(x^4 + 1)

        We convert it to the vector space, and get a vector over the base field::

            sage: to_V(a)                                                               # needs sage.modules
            (-2*x^2/(x^4 + 1), 0, 0, 0, x/(x^4 + 1))

        We convert to and back, and get the same element::

            sage: from_V(to_V(a)) == a                                                  # needs sage.modules
            True

        In the other direction::

            sage: v = x*V.0 + (1/x)*V.1                                                 # needs sage.modules
            sage: to_V(from_V(v)) == v                                                  # needs sage.modules
            True

        And we show how it works over an extension of an extension field::

            sage: R2.<z> = L[]; M.<z> = L.extension(z^2 - y)
            sage: M.free_module()                                                       # needs sage.modules
            (Vector space of dimension 2 over Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x,
             Isomorphism:
              From: Vector space of dimension 2 over Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
              To:   Function field in z defined by z^2 - y,
             Isomorphism:
              From: Function field in z defined by z^2 - y
              To:   Vector space of dimension 2 over Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x)

        We can also get the vector space of ``M`` over ``K``::

            sage: M.free_module(K)                                                      # needs sage.modules
            (Vector space of dimension 10 over Rational function field in x over Rational Field,
             Isomorphism:
              From: Vector space of dimension 10 over Rational function field in x over Rational Field
              To:   Function field in z defined by z^2 - y,
             Isomorphism:
              From: Function field in z defined by z^2 - y
              To:   Vector space of dimension 10 over Rational function field in x over Rational Field)
        """
    def maximal_order(self):
        """
        Return the maximal order of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.maximal_order()
            Maximal order of Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x
        """
    def maximal_order_infinite(self):
        """
        Return the maximal infinite order of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: L.maximal_order_infinite()
            Maximal infinite order of Function field in y defined by y^5 - 2*x*y + (-x^4 - 1)/x

            sage: K.<x> = FunctionField(GF(2)); _.<t> = K[]                             # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(t^3 - x^2*(x^2 + x + 1)^2)                        # needs sage.rings.finite_rings
            sage: F.maximal_order_infinite()                                            # needs sage.rings.finite_rings
            Maximal infinite order of Function field in y defined by y^3 + x^6 + x^4 + x^2

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings
            sage: L.maximal_order_infinite()                                            # needs sage.rings.finite_rings
            Maximal infinite order of Function field in y defined by y^2 + y + (x^2 + 1)/x
        """
    def different(self):
        """
        Return the different of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)                        # needs sage.rings.finite_rings
            sage: F.different()                                                         # needs sage.rings.finite_rings
            2*Place (x, (1/(x^3 + x^2 + x))*y^2)
             + 2*Place (x^2 + x + 1, (1/(x^3 + x^2 + x))*y^2)
        """
    def equation_order(self):
        """
        Return the equation order of the function field.

        If we view the function field as being presented as `K[y]/(f(y))`, then
        the order generated by the class of `y` is returned.  If `f`
        is not monic, then :meth:`_make_monic_integral` is called, and instead
        we get the order generated by some integral multiple of a root of `f`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))
            sage: O = L.equation_order()
            sage: O.basis()
            (1, x*y, x^2*y^2, x^3*y^3, x^4*y^4)

        We try an example, in which the defining polynomial is not
        monic and is not integral::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(x^2*y^5 - 1/x); L
            Function field in y defined by x^2*y^5 - 1/x
            sage: O = L.equation_order()
            sage: O.basis()
            (1, x^3*y, x^6*y^2, x^9*y^3, x^12*y^4)
        """
    def hom(self, im_gens, base_morphism=None):
        """
        Create a homomorphism from the function field to another function field.

        INPUT:

        - ``im_gens`` -- list of images of the generators of the function field
          and of successive base rings

        - ``base_morphism`` -- homomorphism of the base ring, after the
          ``im_gens`` are used.  Thus if ``im_gens`` has length 2, then
          ``base_morphism`` should be a morphism from the base ring of the base
          ring of the function field.

        EXAMPLES:

        We create a rational function field, and a quadratic extension of it::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)

        We make the field automorphism that sends y to -y::

            sage: f = L.hom(-y); f
            Function Field endomorphism of Function field in y defined by y^2 - x^3 - 1
              Defn: y |--> -y

        Evaluation works::

            sage: f(y*x - 1/x)
            -x*y - 1/x

        We try to define an invalid morphism::

            sage: f = L.hom(y + 1)
            Traceback (most recent call last):
            ...
            ValueError: invalid morphism

        We make a morphism of the base rational function field::

            sage: phi = K.hom(x + 1); phi
            Function Field endomorphism of Rational function field in x over Rational Field
              Defn: x |--> x + 1
            sage: phi(x^3 - 3)
            x^3 + 3*x^2 + 3*x - 2
            sage: (x+1)^3 - 3
            x^3 + 3*x^2 + 3*x - 2

        We make a morphism by specifying where the generators and the
        base generators go::

            sage: L.hom([-y, x])
            Function Field endomorphism of Function field in y defined by y^2 - x^3 - 1
              Defn: y |--> -y
                    x |--> x

        You can also specify a morphism on the base::

            sage: R1.<q> = K[]
            sage: L1.<q> = K.extension(q^2 - (x+1)^3 - 1)
            sage: L.hom(q, base_morphism=phi)
            Function Field morphism:
              From: Function field in y defined by y^2 - x^3 - 1
              To:   Function field in q defined by q^2 - x^3 - 3*x^2 - 3*x - 2
              Defn: y |--> q
                    x |--> x + 1

        We make another extension of a rational function field::

            sage: K2.<t> = FunctionField(QQ); R2.<w> = K2[]
            sage: L2.<w> = K2.extension((4*w)^2 - (t+1)^3 - 1)

        We define a morphism, by giving the images of generators::

            sage: f = L.hom([4*w, t + 1]); f
            Function Field morphism:
              From: Function field in y defined by y^2 - x^3 - 1
              To:   Function field in w defined by 16*w^2 - t^3 - 3*t^2 - 3*t - 2
              Defn: y |--> 4*w
                    x |--> t + 1

        Evaluation works, as expected::

            sage: f(y+x)
            4*w + t + 1
            sage: f(x*y + x/(x^2+1))
            (4*t + 4)*w + (t + 1)/(t^2 + 2*t + 2)

        We make another extension of a rational function field::

            sage: K3.<yy> = FunctionField(QQ); R3.<xx> = K3[]
            sage: L3.<xx> = K3.extension(yy^2 - xx^3 - 1)

        This is the function field L with the generators exchanged. We define a morphism to L::

            sage: g = L3.hom([x,y]); g
            Function Field morphism:
              From: Function field in xx defined by -xx^3 + yy^2 - 1
              To:   Function field in y defined by y^2 - x^3 - 1
              Defn: xx |--> x
                    yy |--> y
        """
    @cached_method
    def genus(self):
        """
        Return the genus of the function field.

        For now, the genus is computed using Singular.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - (x^3 + 2*x*y + 1/x))
            sage: L.genus()
            3
        """
    @cached_method
    def simple_model(self, name=None):
        """
        Return a function field isomorphic to this field which is a simple
        extension of a rational function field.

        INPUT:

        - ``name`` -- string (default: ``None``); the name of generator of
          the simple extension. If ``None``, then the name of the generator
          will be the same as the name of the generator of this function field.

        OUTPUT:

        A triple ``(F,f,t)`` where ``F`` is a field isomorphic to this field,
        ``f`` is an isomorphism from ``F`` to this function field and ``t`` is
        the inverse of ``f``.

        EXAMPLES:

        A tower of four function fields::

            sage: K.<x> = FunctionField(QQ); R.<z> = K[]
            sage: L.<z> = K.extension(z^2 - x); R.<u> = L[]
            sage: M.<u> = L.extension(u^2 - z); R.<v> = M[]
            sage: N.<v> = M.extension(v^2 - u)

        The fields N and M as simple extensions of K::

            sage: N.simple_model()
            (Function field in v defined by v^8 - x,
             Function Field morphism:
              From: Function field in v defined by v^8 - x
              To:   Function field in v defined by v^2 - u
              Defn: v |--> v,
             Function Field morphism:
              From: Function field in v defined by v^2 - u
              To:   Function field in v defined by v^8 - x
              Defn: v |--> v
                    u |--> v^2
                    z |--> v^4
                    x |--> x)
            sage: M.simple_model()
            (Function field in u defined by u^4 - x,
             Function Field morphism:
              From: Function field in u defined by u^4 - x
              To:   Function field in u defined by u^2 - z
              Defn: u |--> u,
             Function Field morphism:
              From: Function field in u defined by u^2 - z
              To:   Function field in u defined by u^4 - x
              Defn: u |--> u
                    z |--> u^2
                    x |--> x)

        An optional parameter ``name`` can be used to set the name of the
        generator of the simple extension::

            sage: M.simple_model(name='t')
            (Function field in t defined by t^4 - x, Function Field morphism:
              From: Function field in t defined by t^4 - x
              To:   Function field in u defined by u^2 - z
              Defn: t |--> u, Function Field morphism:
              From: Function field in u defined by u^2 - z
              To:   Function field in t defined by t^4 - x
              Defn: u |--> t
                    z |--> t^2
                    x |--> x)

        An example with higher degrees::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3)); R.<y> = K[]
            sage: L.<y> = K.extension(y^5 - x); R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - x)
            sage: M.simple_model()
            (Function field in z defined by z^15 + x*z^12 + x^2*z^9 + 2*x^3*z^6 + 2*x^4*z^3 + 2*x^5 + 2*x^3,
             Function Field morphism:
               From: Function field in z defined by z^15 + x*z^12 + x^2*z^9 + 2*x^3*z^6 + 2*x^4*z^3 + 2*x^5 + 2*x^3
               To:   Function field in z defined by z^3 + 2*x
               Defn: z |--> z + y,
             Function Field morphism:
               From: Function field in z defined by z^3 + 2*x
               To:   Function field in z defined by z^15 + x*z^12 + x^2*z^9 + 2*x^3*z^6 + 2*x^4*z^3 + 2*x^5 + 2*x^3
               Defn: z |--> 2/x*z^6 + 2*z^3 + z + 2*x
                     y |--> 1/x*z^6 + z^3 + x
                     x |--> x)

        This also works for inseparable extensions::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x); R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: M.simple_model()
            (Function field in z defined by z^4 + x,
             Function Field morphism:
               From: Function field in z defined by z^4 + x
               To:   Function field in z defined by z^2 + y
               Defn: z |--> z,
             Function Field morphism:
               From: Function field in z defined by z^2 + y
               To:   Function field in z defined by z^4 + x
               Defn: z |--> z
                     y |--> z^2
                     x |--> x)
        """
    @cached_method
    def primitive_element(self):
        """
        Return a primitive element over the underlying rational function field.

        If this is a finite extension of a rational function field `K(x)` with
        `K` perfect, then this is a simple extension of `K(x)`, i.e., there is
        a primitive element `y` which generates this field over `K(x)`. This
        method returns such an element `y`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: R.<z> = L[]
            sage: N.<u> = L.extension(z^2 - x - 1)
            sage: N.primitive_element()
            u + y
            sage: M.primitive_element()
            z
            sage: L.primitive_element()
            y

        This also works for inseparable extensions::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x)
            sage: R.<Z> = L[]
            sage: M.<z> = L.extension(Z^2 - y)
            sage: M.primitive_element()
            z
        """
    @cached_method
    def separable_model(self, names=None):
        """
        Return a function field isomorphic to this field which is a separable
        extension of a rational function field.

        INPUT:

        - ``names`` -- tuple of two strings or ``None`` (default: ``None``);
          the second entry will be used as the variable name of the rational
          function field, the first entry will be used as the variable name of
          its separable extension. If ``None``, then the variable names will be
          chosen automatically.

        OUTPUT:

        A triple ``(F,f,t)`` where ``F`` is a function field, ``f`` is an
        isomorphism from ``F`` to this function field, and ``t`` is the inverse
        of ``f``.

        ALGORITHM:

        Suppose that the constant base field is perfect. If this is a monic
        integral inseparable extension of a rational function field, then the
        defining polynomial is separable if we swap the variables (Proposition
        4.8 in Chapter VIII of [Lan2002]_.)
        The algorithm reduces to this case with :meth:`monic_integral_model`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3)
            sage: L.separable_model(('t','w'))
            (Function field in t defined by t^3 + w^2,
             Function Field morphism:
               From: Function field in t defined by t^3 + w^2
               To:   Function field in y defined by y^2 + x^3
               Defn: t |--> x
                     w |--> y,
             Function Field morphism:
               From: Function field in y defined by y^2 + x^3
               To:   Function field in t defined by t^3 + w^2
               Defn: y |--> w
                     x |--> t)

        This also works for non-integral polynomials::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2/x - x^2)
            sage: L.separable_model()
            (Function field in y_ defined by y_^3 + x_^2,
             Function Field morphism:
               From: Function field in y_ defined by y_^3 + x_^2
               To:   Function field in y defined by 1/x*y^2 + x^2
               Defn: y_ |--> x
                     x_ |--> y,
             Function Field morphism:
               From: Function field in y defined by 1/x*y^2 + x^2
               To:   Function field in y_ defined by y_^3 + x_^2
               Defn: y |--> x_
                     x |--> y_)

        If the base field is not perfect this is only implemented in trivial cases::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = FunctionField(GF(2))
            sage: k.is_perfect()
            False
            sage: K.<x> = FunctionField(k)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^3 - t)
            sage: L.separable_model()
            (Function field in y defined by y^3 + t,
             Function Field endomorphism of Function field in y defined by y^3 + t
               Defn: y |--> y
                     x |--> x,
             Function Field endomorphism of Function field in y defined by y^3 + t
               Defn: y |--> y
                     x |--> x)

        Some other cases for which a separable model could be constructed are
        not supported yet::

            sage: R.<y> = K[]                                                           # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(y^2 - t)                                          # needs sage.rings.finite_rings
            sage: L.separable_model()                                                   # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            NotImplementedError: constructing a separable model is only implemented
            for function fields over a perfect constant base field

        TESTS:

        Check that this also works in characteristic zero::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3)
            sage: L.separable_model()
            (Function field in y defined by y^2 - x^3,
             Function Field endomorphism of Function field in y defined by y^2 - x^3
               Defn: y |--> y
                     x |--> x,
             Function Field endomorphism of Function field in y defined by y^2 - x^3
               Defn: y |--> y
                     x |--> x)

        Check that this works for towers of inseparable extensions::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)
            sage: M.separable_model()
            (Function field in z_ defined by z_ + x_^4,
             Function Field morphism:
               From: Function field in z_ defined by z_ + x_^4
               To:   Function field in z defined by z^2 + y
               Defn: z_ |--> x
                     x_ |--> z,
             Function Field morphism:
               From: Function field in z defined by z^2 + y
               To:   Function field in z_ defined by z_ + x_^4
               Defn: z |--> x_
                     y |--> x_^2
                     x |--> x_^4)

        Check that this also works if only the first extension is inseparable::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^3 - y)
            sage: M.separable_model()
            (Function field in z_ defined by z_ + x_^6,
             Function Field morphism:
               From: Function field in z_ defined by z_ + x_^6
               To:   Function field in z defined by z^3 + y
               Defn: z_ |--> x
                     x_ |--> z,
             Function Field morphism:
               From: Function field in z defined by z^3 + y
               To:   Function field in z_ defined by z_ + x_^6
               Defn: z |--> x_
                     y |--> x_^3
                     x |--> x_^6)
        """
    def change_variable_name(self, name):
        """
        Return a field isomorphic to this field with variable(s) ``name``.

        INPUT:

        - ``name`` -- string or tuple consisting of a strings; the names of
          the new variables starting with a generator of this field and going
          down to the rational function field

        OUTPUT:

        A triple ``F,f,t`` where ``F`` is a function field, ``f`` is an
        isomorphism from ``F`` to this field, and ``t`` is the inverse of
        ``f``.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2 - y)

            sage: M.change_variable_name('zz')
            (Function field in zz defined by zz^2 - y,
             Function Field morphism:
              From: Function field in zz defined by zz^2 - y
              To:   Function field in z defined by z^2 - y
              Defn: zz |--> z
                    y |--> y
                    x |--> x,
             Function Field morphism:
              From: Function field in z defined by z^2 - y
              To:   Function field in zz defined by zz^2 - y
              Defn: z |--> zz
                    y |--> y
                    x |--> x)
            sage: M.change_variable_name(('zz','yy'))
            (Function field in zz defined by zz^2 - yy,
             Function Field morphism:
              From: Function field in zz defined by zz^2 - yy
              To:   Function field in z defined by z^2 - y
              Defn: zz |--> z
                    yy |--> y
                    x |--> x,
             Function Field morphism:
              From: Function field in z defined by z^2 - y
              To:   Function field in zz defined by zz^2 - yy
              Defn: z |--> zz
                    y |--> yy
                    x |--> x)
            sage: M.change_variable_name(('zz','yy','xx'))
            (Function field in zz defined by zz^2 - yy,
             Function Field morphism:
              From: Function field in zz defined by zz^2 - yy
              To:   Function field in z defined by z^2 - y
              Defn: zz |--> z
                    yy |--> y
                    xx |--> x,
             Function Field morphism:
              From: Function field in z defined by z^2 - y
              To:   Function field in zz defined by zz^2 - yy
              Defn: z |--> zz
                    y |--> yy
                    x |--> xx)
        """

class FunctionField_simple(FunctionField_polymod):
    """
    Function fields defined by irreducible and separable polynomials
    over rational function fields.
    """
    def places_above(self, p):
        """
        Return places lying above ``p``.

        INPUT:

        - ``p`` -- place of the base rational function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)                        # needs sage.rings.finite_rings
            sage: all(q.place_below() == p                                              # needs sage.rings.finite_rings
            ....:     for p in K.places() for q in F.places_above(p))
            True

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: O = K.maximal_order()
            sage: pls = [O.ideal(x - c).place() for c in [-2, -1, 0, 1, 2]]
            sage: all(q.place_below() == p
            ....:     for p in pls for q in F.places_above(p))
            True

            sage: # needs sage.rings.number_field
            sage: K.<x> = FunctionField(QQbar); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: O = K.maximal_order()
            sage: pls = [O.ideal(x - QQbar(sqrt(c))).place()
            ....:        for c in [-2, -1, 0, 1, 2]]
            sage: all(q.place_below() == p      # long time (4s)
            ....:     for p in pls for q in F.places_above(p))
            True
        """
    def constant_field(self):
        """
        Return the algebraic closure of the base constant field in the function
        field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(3)); _.<y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(y^5 - (x^3 + 2*x*y + 1/x))                        # needs sage.rings.finite_rings
            sage: L.constant_field()                                                    # needs sage.rings.finite_rings
            Finite Field of size 3
        """
    def exact_constant_field(self, name: str = 't'):
        """
        Return the exact constant field and its embedding into the function field.

        INPUT:

        - ``name`` -- name (default: `t`) of the generator of the exact constant field

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3)); _.<Y> = K[]
            sage: f = Y^2 - x*Y + x^2 + 1 # irreducible but not absolutely irreducible
            sage: L.<y> = K.extension(f)
            sage: L.genus()
            0
            sage: L.exact_constant_field()
            (Finite Field in t of size 3^2, Ring morphism:
               From: Finite Field in t of size 3^2
               To:   Function field in y defined by y^2 + 2*x*y + x^2 + 1
               Defn: t |--> y + x)
            sage: (y+x).divisor()
            0
        """
    def genus(self):
        """
        Return the genus of the function field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(16)
            sage: K.<x> = FunctionField(F); K
            Rational function field in x over Finite Field in a of size 2^4
            sage: R.<t> = PolynomialRing(K)
            sage: L.<y> = K.extension(t^4 + t - x^5)
            sage: L.genus()
            6

            sage: # needs sage.rings.number_field
            sage: R.<T> = QQ[]
            sage: N.<a> = NumberField(T^2 + 1)
            sage: K.<x> = FunctionField(N); K
            Rational function field in x over Number Field in a with defining polynomial T^2 + 1
            sage: K.genus()
            0
            sage: S.<t> = PolynomialRing(K)
            sage: L.<y> = K.extension(t^2 - x^3 + x)
            sage: L.genus()
            1

        The genus is computed by the Hurwitz genus formula.
        """
    def residue_field(self, place, name=None):
        """
        Return the residue field associated with the place along with the maps
        from and to the residue field.

        INPUT:

        - ``place`` -- place of the function field

        - ``name`` -- string; name of the generator of the residue field

        The domain of the map to the residue field is the discrete valuation
        ring associated with the place.

        The discrete valuation ring is defined as the ring of all elements of
        the function field with nonnegative valuation at the place. The maximal
        ideal is the set of elements of positive valuation.  The residue field
        is then the quotient of the discrete valuation ring by its maximal
        ideal.

        If an element not in the valuation ring is applied to the map, an
        exception :exc:`TypeError` is raised.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: R, fr_R, to_R = L.residue_field(p)
            sage: R
            Finite Field of size 2
            sage: f = 1 + y
            sage: f.valuation(p)
            -1
            sage: to_R(f)
            Traceback (most recent call last):
            ...
            TypeError: ...
            sage: (1+1/f).valuation(p)
            0
            sage: to_R(1 + 1/f)
            1
            sage: [fr_R(e) for e in R]
            [0, 1]
        """
    def places_infinite(self, degree: int = 1):
        """
        Return a list of the infinite places with ``degree``.

        INPUT:

        - ``degree`` -- positive integer (default: `1`)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(2)
            sage: K.<x> = FunctionField(F)
            sage: R.<t> = PolynomialRing(K)
            sage: L.<y> = K.extension(t^4 + t - x^5)
            sage: L.places_infinite(1)
            [Place (1/x, 1/x^4*y^3)]
        """

class FunctionField_char_zero(FunctionField_simple):
    """
    Function fields of characteristic zero.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))
        sage: L
        Function field in y defined by y^3 + (-x^3 + 1)/(x^3 - 2)
        sage: L.characteristic()
        0
    """
    @cached_method
    def higher_derivation(self):
        """
        Return the higher derivation (also called the Hasse-Schmidt derivation)
        for the function field.

        The higher derivation of the function field is uniquely determined with
        respect to the separating element `x` of the base rational function
        field `k(x)`.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))
            sage: L.higher_derivation()                                                 # needs sage.modules
            Higher derivation map:
              From: Function field in y defined by y^3 + (-x^3 + 1)/(x^3 - 2)
              To:   Function field in y defined by y^3 + (-x^3 + 1)/(x^3 - 2)
        """

class FunctionField_global(FunctionField_simple):
    """
    Global function fields.

    INPUT:

    - ``polynomial`` -- monic irreducible and separable polynomial

    - ``names`` -- name of the generator of the function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                            # needs sage.rings.finite_rings
        sage: L                                                                         # needs sage.rings.finite_rings
        Function field in y defined by y^3 + (4*x^3 + 1)/(x^3 + 3)

    The defining equation needs not be monic::

        sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension((1 - x)*Y^7 - x^3)                                    # needs sage.rings.finite_rings
        sage: L.gaps()                          # long time (6s)                        # needs sage.rings.finite_rings
        [1, 2, 3]

    or may define a trivial extension::

        sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]                                 # needs sage.rings.finite_rings
        sage: L.<y> = K.extension(Y-1)                                                  # needs sage.rings.finite_rings
        sage: L.genus()                                                                 # needs sage.rings.finite_rings
        0
    """
    def __init__(self, polynomial, names) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.finite_rings
            sage: TestSuite(L).run()            # long time (7s)                        # needs sage.rings.finite_rings
        """
    def maximal_order(self):
        """
        Return the maximal order of the function field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^4 + x^12*t^2 + x^18*t + x^21 + x^18)
            sage: O = F.maximal_order()
            sage: O.basis()
            (1, 1/x^4*y, 1/x^11*y^2 + 1/x^2, 1/x^15*y^3 + 1/x^6*y)
        """
    @cached_method
    def higher_derivation(self):
        """
        Return the higher derivation (also called the Hasse-Schmidt derivation)
        for the function field.

        The higher derivation of the function field is uniquely determined with
        respect to the separating element `x` of the base rational function
        field `k(x)`.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.finite_rings
            sage: L.higher_derivation()                                                 # needs sage.modules sage.rings.finite_rings
            Higher derivation map:
              From: Function field in y defined by y^3 + (4*x^3 + 1)/(x^3 + 3)
              To:   Function field in y defined by y^3 + (4*x^3 + 1)/(x^3 + 3)
        """
    def get_place(self, degree):
        """
        Return a place of ``degree``.

        INPUT:

        - ``degree`` -- positive integer

        OUTPUT: a place of ``degree`` if any exists; otherwise ``None``

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(2)
            sage: K.<x> = FunctionField(F)
            sage: R.<Y> = PolynomialRing(K)
            sage: L.<y> = K.extension(Y^4 + Y - x^5)
            sage: L.get_place(1)
            Place (x, y)
            sage: L.get_place(2)
            Place (x, y^2 + y + 1)
            sage: L.get_place(3)
            Place (x^3 + x^2 + 1, y + x^2 + x)
            sage: L.get_place(4)
            Place (x + 1, x^5 + 1)
            sage: L.get_place(5)
            Place (x^5 + x^3 + x^2 + x + 1, y + x^4 + 1)
            sage: L.get_place(6)
            Place (x^3 + x^2 + 1, y^2 + y + x^2)
            sage: L.get_place(7)
            Place (x^7 + x + 1, y + x^6 + x^5 + x^4 + x^3 + x)
            sage: L.get_place(8)
        """
    def places(self, degree: int = 1):
        """
        Return a list of the places with ``degree``.

        INPUT:

        - ``degree`` -- positive integer (default: `1`)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(2)
            sage: K.<x> = FunctionField(F)
            sage: R.<t> = PolynomialRing(K)
            sage: L.<y> = K.extension(t^4 + t - x^5)
            sage: L.places(1)
            [Place (1/x, 1/x^4*y^3), Place (x, y), Place (x, y + 1)]
        """
    def places_finite(self, degree: int = 1):
        """
        Return a list of the finite places with ``degree``.

        INPUT:

        - ``degree`` -- positive integer (default: `1`)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(2)
            sage: K.<x> = FunctionField(F)
            sage: R.<t> = PolynomialRing(K)
            sage: L.<y> = K.extension(t^4 + t - x^5)
            sage: L.places_finite(1)
            [Place (x, y), Place (x, y + 1)]
        """
    def gaps(self):
        """
        Return the gaps of the function field.

        These are the gaps at the ordinary places, that is, places which are
        not Weierstrass places.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^3 + x^3 * Y + x)                                # needs sage.rings.finite_rings
            sage: L.gaps()                                                              # needs sage.modules sage.rings.finite_rings
            [1, 2, 3]
        """
    def weierstrass_places(self):
        """
        Return all Weierstrass places of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^3 + x^3 * Y + x)                                # needs sage.rings.finite_rings
            sage: L.weierstrass_places()                                                # needs sage.modules sage.rings.finite_rings
            [Place (1/x, 1/x^3*y^2 + 1/x),
             Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1),
             Place (x, y),
             Place (x + 1, (x^3 + 1)*y + x + 1),
             Place (x^3 + x + 1, y + 1),
             Place (x^3 + x + 1, y + x^2),
             Place (x^3 + x + 1, y + x^2 + 1),
             Place (x^3 + x^2 + 1, y + x),
             Place (x^3 + x^2 + 1, y + x^2 + 1),
             Place (x^3 + x^2 + 1, y + x^2 + x + 1)]
        """
    @cached_method
    def L_polynomial(self, name: str = 't'):
        """
        Return the L-polynomial of the function field.

        INPUT:

        - ``name`` -- (default: ``t``) name of the variable of the polynomial

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.finite_rings
            sage: F.L_polynomial()                                                      # needs sage.rings.finite_rings
            2*t^2 + t + 1
        """
    def number_of_rational_places(self, r: int = 1):
        """
        Return the number of rational places of the function field whose
        constant field extended by degree ``r``.

        INPUT:

        - ``r`` -- positive integer (default: `1`)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: F.number_of_rational_places()
            4
            sage: [F.number_of_rational_places(r) for r in [1..10]]
            [4, 8, 4, 16, 44, 56, 116, 288, 508, 968]
        """

class FunctionField_integral(FunctionField_simple):
    """
    Integral function fields.

    A function field is integral if it is defined by an irreducible separable
    polynomial, which is integral over the maximal order of the base rational
    function field.
    """
    @cached_method
    def equation_order(self):
        """
        Return the equation order of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); R.<t> = PolynomialRing(K)               # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)                            # needs sage.rings.finite_rings
            sage: F.equation_order()                                                    # needs sage.rings.finite_rings
            Order in Function field in y defined by y^3 + x^6 + x^4 + x^2

            sage: K.<x> = FunctionField(QQ); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: F.equation_order()
            Order in Function field in y defined by y^3 - x^6 - 2*x^5 - 3*x^4 - 2*x^3 - x^2
        """
    @cached_method
    def primitive_integal_element_infinite(self):
        """
        Return a primitive integral element over the base maximal infinite order.

        This element is integral over the maximal infinite order of the base
        rational function field and the function field is a simple extension by
        this element over the base order.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: b = F.primitive_integal_element_infinite(); b
            1/x^2*y
            sage: b.minimal_polynomial('t')
            t^3 + (x^4 + x^2 + 1)/x^4
        """
    @cached_method
    def equation_order_infinite(self):
        """
        Return the infinite equation order of the function field.

        This is by definition `o[b]` where `b` is the primitive integral
        element from :meth:`primitive_integal_element_infinite()` and `o` is
        the maximal infinite order of the base rational function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); R.<t> = PolynomialRing(K)               # needs sage.rings.finite_rings
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)                            # needs sage.rings.finite_rings
            sage: F.equation_order_infinite()                                           # needs sage.rings.finite_rings
            Infinite order in Function field in y defined by y^3 + x^6 + x^4 + x^2

            sage: K.<x> = FunctionField(QQ); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: F.equation_order_infinite()
            Infinite order in Function field in y defined by y^3 - x^6 - 2*x^5 - 3*x^4 - 2*x^3 - x^2
        """

class FunctionField_char_zero_integral(FunctionField_char_zero, FunctionField_integral):
    """
    Function fields of characteristic zero, defined by an irreducible and
    separable polynomial, integral over the maximal order of the base rational
    function field with a finite constant field.
    """
class FunctionField_global_integral(FunctionField_global, FunctionField_integral):
    """
    Global function fields, defined by an irreducible and separable polynomial,
    integral over the maximal order of the base rational function field with a
    finite constant field.
    """
