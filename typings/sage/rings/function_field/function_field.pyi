from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.homset import Hom as Hom
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.ring import Field as Field
from sage.structure.category_object import CategoryObject as CategoryObject

def is_FunctionField(x):
    """
    Return ``True`` if ``x`` is a function field.

    EXAMPLES::

        sage: from sage.rings.function_field.function_field import is_FunctionField
        sage: is_FunctionField(QQ)
        doctest:warning...
        DeprecationWarning: The function is_FunctionField is deprecated; use '... in FunctionFields()' instead.
        See https://github.com/sagemath/sage/issues/38289 for details.
        False
        sage: is_FunctionField(FunctionField(QQ, 't'))
        True
    """

class FunctionField(Field):
    """
    Abstract base class for all function fields.

    INPUT:

    - ``base_field`` -- field; the base of this function field

    - ``names`` -- string that gives the name of the generator

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: K
        Rational function field in x over Rational Field
    """
    def __init__(self, base_field, names, category=...) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: K = FunctionField(QQ, 'z')
            sage: K
            Rational function field in z over Rational Field

        """
    def is_perfect(self):
        """
        Return whether the field is perfect, i.e., its characteristic `p` is zero
        or every element has a `p`-th root.

        EXAMPLES::

            sage: FunctionField(QQ, 'x').is_perfect()
            True
            sage: FunctionField(GF(2), 'x').is_perfect()
            False
        """
    def some_elements(self):
        """
        Return some elements in this function field.

        EXAMPLES::

           sage: K.<x> = FunctionField(QQ)
           sage: K.some_elements()
           [1,
            x,
            2*x,
            x/(x^2 + 2*x + 1),
            1/x^2,
            x/(x^2 - 1),
            x/(x^2 + 1),
            1/2*x/(x^2 + 1),
            0,
            1/x,
            ...]

        ::

           sage: R.<y> = K[]
           sage: L.<y> = K.extension(y^2 - x)                                           # needs sage.rings.function_field
           sage: L.some_elements()                                                      # needs sage.rings.function_field
           [1,
            y,
            1/x*y,
            ((x + 1)/(x^2 - 2*x + 1))*y - 2*x/(x^2 - 2*x + 1),
            1/x,
            (1/(x - 1))*y,
            (1/(x + 1))*y,
            (1/2/(x + 1))*y,
            0,
            ...]
        """
    def characteristic(self):
        """
        Return the characteristic of the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.characteristic()
            0
            sage: K.<x> = FunctionField(QQbar)                                          # needs sage.rings.number_field
            sage: K.characteristic()
            0
            sage: K.<x> = FunctionField(GF(7))
            sage: K.characteristic()
            7
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)                                          # needs sage.rings.function_field
            sage: L.characteristic()                                                    # needs sage.rings.function_field
            7
        """
    def is_finite(self):
        """
        Return whether the function field is finite, which is false.

        EXAMPLES::

            sage: R.<t> = FunctionField(QQ)
            sage: R.is_finite()
            False
            sage: R.<t> = FunctionField(GF(7))
            sage: R.is_finite()
            False
        """
    def is_global(self):
        """
        Return whether the function field is global, that is, whether
        the constant field is finite.

        EXAMPLES::

            sage: R.<t> = FunctionField(QQ)
            sage: R.is_global()
            False
            sage: R.<t> = FunctionField(QQbar)                                          # needs sage.rings.number_field
            sage: R.is_global()
            False
            sage: R.<t> = FunctionField(GF(7))
            sage: R.is_global()
            True
        """
    def extension(self, f, names=None):
        """
        Create an extension `K(y)` of this function field `K` extended with
        a root `y` of the univariate polynomial `f` over `K`.

        INPUT:

        - ``f`` -- univariate polynomial over `K`

        - ``names`` -- string or tuple of length 1 that names the variable `y`

        OUTPUT: a function field

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: K.extension(y^5 - x^3 - 3*x + x*y)                                    # needs sage.rings.function_field
            Function field in y defined by y^5 + x*y - x^3 - 3*x

        A nonintegral defining polynomial::

            sage: K.<t> = FunctionField(QQ); R.<y> = K[]
            sage: K.extension(y^3 + (1/t)*y + t^3/(t+1), 'z')                           # needs sage.rings.function_field
            Function field in z defined by z^3 + 1/t*z + t^3/(t + 1)

        The defining polynomial need not be monic or integral::

            sage: K.extension(t*y^3 + (1/t)*y + t^3/(t+1))                              # needs sage.rings.function_field
            Function field in y defined by t*y^3 + 1/t*y + t^3/(t + 1)
        """
    def order_with_basis(self, basis, check: bool = True):
        """
        Return the order with given basis over the maximal order of
        the base field.

        INPUT:

        - ``basis`` -- list of elements of this function field

        - ``check`` -- boolean (default: ``True``); if ``True``, check that the
          basis is really linearly independent and that the module it spans is
          closed under multiplication, and contains the identity element.

        OUTPUT: an order in the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + x^3 + 4*x + 1)                              # needs sage.rings.function_field
            sage: O = L.order_with_basis([1, y, y^2]); O                                # needs sage.rings.function_field
            Order in Function field in y defined by y^3 + x^3 + 4*x + 1
            sage: O.basis()                                                             # needs sage.rings.function_field
            (1, y, y^2)

        Note that 1 does not need to be an element of the basis, as long it is in the module spanned by it::

            sage: O = L.order_with_basis([1+y, y, y^2]); O                              # needs sage.rings.function_field
            Order in Function field in y defined by y^3 + x^3 + 4*x + 1
            sage: O.basis()                                                             # needs sage.rings.function_field
            (y + 1, y, y^2)

        The following error is raised when the module spanned by the basis is not closed under multiplication::

            sage: O = L.order_with_basis([1, x^2 + x*y, (2/3)*y^2]); O                  # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: the module generated by basis (1, x*y + x^2, 2/3*y^2) must be closed under multiplication

        and this happens when the identity is not in the module spanned by the basis::

            sage: O = L.order_with_basis([x, x^2 + x*y, (2/3)*y^2])                     # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: the identity element must be in the module spanned by basis (x, x*y + x^2, 2/3*y^2)
        """
    def order(self, x, check: bool = True):
        """
        Return the order generated by ``x`` over the base maximal order.

        INPUT:

        - ``x`` -- element or list of elements of the function field

        - ``check`` -- boolean; if ``True``, check that ``x`` really generates an order

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + x^3 + 4*x + 1)
            sage: O = L.order(y); O                                                     # needs sage.modules
            Order in Function field in y defined by y^3 + x^3 + 4*x + 1
            sage: O.basis()                                                             # needs sage.modules
            (1, y, y^2)

            sage: Z = K.order(x); Z                                                     # needs sage.rings.function_field
            Order in Rational function field in x over Rational Field
            sage: Z.basis()                                                             # needs sage.rings.function_field
            (1,)

        Orders with multiple generators are not yet supported::

            sage: Z = K.order([x, x^2]); Z                                              # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def order_infinite_with_basis(self, basis, check: bool = True):
        """
        Return the order with given basis over the maximal infinite order of
        the base field.

        INPUT:

        - ``basis`` -- list of elements of the function field

        - ``check`` -- boolean (default: ``True``); if ``True``, check that the basis
          is really linearly independent and that the module it spans is closed
          under multiplication, and contains the identity element.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + x^3 + 4*x + 1)
            sage: O = L.order_infinite_with_basis([1, 1/x*y, 1/x^2*y^2]); O
            Infinite order in Function field in y defined by y^3 + x^3 + 4*x + 1
            sage: O.basis()
            (1, 1/x*y, 1/x^2*y^2)

        Note that 1 does not need to be an element of the basis, as long it is
        in the module spanned by it::

            sage: O = L.order_infinite_with_basis([1+1/x*y,1/x*y, 1/x^2*y^2]); O        # needs sage.rings.function_field
            Infinite order in Function field in y defined by y^3 + x^3 + 4*x + 1
            sage: O.basis()                                                             # needs sage.rings.function_field
            (1/x*y + 1, 1/x*y, 1/x^2*y^2)

        The following error is raised when the module spanned by the basis is
        not closed under multiplication::

            sage: O = L.order_infinite_with_basis([1,y, 1/x^2*y^2]); O                  # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: the module generated by basis (1, y, 1/x^2*y^2) must be closed under multiplication

        and this happens when the identity is not in the module spanned by the
        basis::

            sage: O = L.order_infinite_with_basis([1/x,1/x*y, 1/x^2*y^2])               # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: the identity element must be in the module spanned by basis (1/x, 1/x*y, 1/x^2*y^2)
        """
    def order_infinite(self, x, check: bool = True):
        """
        Return the order generated by ``x`` over the maximal infinite order.

        INPUT:

        - ``x`` -- element or a list of elements of the function field

        - ``check`` -- boolean; if ``True``, check that ``x`` really generates an order

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^3 + x^3 + 4*x + 1)                              # needs sage.rings.function_field
            sage: L.order_infinite(y)           # not implemented                       # needs sage.rings.function_field

            sage: Z = K.order(x); Z                                                     # needs sage.modules
            Order in Rational function field in x over Rational Field
            sage: Z.basis()                                                             # needs sage.modules
            (1,)

        Orders with multiple generators, not yet supported::

            sage: Z = K.order_infinite([x, x^2]); Z
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def rational_function_field(self):
        """
        Return the rational function field from which this field has been
        created as an extension.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: K.rational_function_field()
            Rational function field in x over Rational Field

            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)                                          # needs sage.rings.function_field
            sage: L.rational_function_field()                                           # needs sage.rings.function_field
            Rational function field in x over Rational Field

            sage: R.<z> = L[]                                                           # needs sage.rings.function_field
            sage: M.<z> = L.extension(z^2 - y)                                          # needs sage.rings.function_field
            sage: M.rational_function_field()                                           # needs sage.rings.function_field
            Rational function field in x over Rational Field
        """
    def valuation(self, prime):
        """
        Return the discrete valuation on this function field defined by
        ``prime``.

        INPUT:

        - ``prime`` -- a place of the function field, a valuation on a subring,
          or a valuation on another function field together with information
          for isomorphisms to and from that function field

        EXAMPLES:

        We create valuations that correspond to finite rational places of a
        function field::

            sage: K.<x> = FunctionField(QQ)
            sage: v = K.valuation(1); v                                                 # needs sage.rings.function_field
            (x - 1)-adic valuation
            sage: v(x)                                                                  # needs sage.rings.function_field
            0
            sage: v(x - 1)                                                              # needs sage.rings.function_field
            1

        A place can also be specified with an irreducible polynomial::

            sage: v = K.valuation(x - 1); v                                             # needs sage.rings.function_field
            (x - 1)-adic valuation

        Similarly, for a finite non-rational place::

            sage: v = K.valuation(x^2 + 1); v                                           # needs sage.rings.function_field
            (x^2 + 1)-adic valuation
            sage: v(x^2 + 1)                                                            # needs sage.rings.function_field
            1
            sage: v(x)                                                                  # needs sage.rings.function_field
            0

        Or for the infinite place::

            sage: v = K.valuation(1/x); v                                               # needs sage.rings.function_field
            Valuation at the infinite place
            sage: v(x)                                                                  # needs sage.rings.function_field
            -1

        Instead of specifying a generator of a place, we can define a valuation on a
        rational function field by giving a discrete valuation on the underlying
        polynomial ring::

            sage: # needs sage.rings.function_field
            sage: R.<x> = QQ[]
            sage: u = valuations.GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: w = u.augmentation(x - 1, 1)
            sage: v = K.valuation(w); v
            (x - 1)-adic valuation

        Note that this allows us to specify valuations which do not correspond to a
        place of the function field::

            sage: w = valuations.GaussValuation(R, QQ.valuation(2))                     # needs sage.rings.function_field
            sage: v = K.valuation(w); v                                                 # needs sage.rings.function_field
            2-adic valuation

        The same is possible for valuations with `v(1/x) > 0` by passing in an
        extra pair of parameters, an isomorphism between this function field and an
        isomorphic function field. That way you can, for example, indicate that the
        valuation is to be understood as a valuation on `K[1/x]`, i.e., after
        applying the substitution `x \\mapsto 1/x` (here, the inverse map is also `x
        \\mapsto 1/x`)::

            sage: # needs sage.rings.function_field
            sage: w = valuations.GaussValuation(R, QQ.valuation(2)).augmentation(x, 1)
            sage: w = K.valuation(w)
            sage: v = K.valuation((w, K.hom([~K.gen()]), K.hom([~K.gen()]))); v
            Valuation on rational function field
            induced by [ Gauss valuation induced by 2-adic valuation, v(x) = 1 ]
            (in Rational function field in x over Rational Field after x |--> 1/x)

        Note that classical valuations at finite places or the infinite place are
        always normalized such that the uniformizing element has valuation 1::

            sage: # needs sage.rings.function_field
            sage: K.<t> = FunctionField(GF(3))
            sage: M.<x> = FunctionField(K)
            sage: v = M.valuation(x^3 - t)
            sage: v(x^3 - t)
            1

        However, if such a valuation comes out of a base change of the ground
        field, this is not the case anymore. In the example below, the unique
        extension of ``v`` to ``L`` still has valuation 1 on `x^3 - t` but it has
        valuation ``1/3`` on its uniformizing element  `x - w`::

            sage: # needs sage.rings.function_field
            sage: R.<w> = K[]
            sage: L.<w> = K.extension(w^3 - t)
            sage: N.<x> = FunctionField(L)
            sage: w = v.extension(N)  # missing factorization, :issue:`16572`
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: w(x^3 - t)                    # not tested
            1
            sage: w(x - w)                      # not tested
            1/3

        There are several ways to create valuations on extensions of rational
        function fields::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x); L                                       # needs sage.rings.function_field
            Function field in y defined by y^2 - x

        A place that has a unique extension can just be defined downstairs::

            sage: v = L.valuation(x); v                                                 # needs sage.rings.function_field
            (x)-adic valuation
        """
    def space_of_differentials(self):
        """
        Return the space of differentials attached to the function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.space_of_differentials()                                            # needs sage.modules
            Space of differentials of Rational function field in t over Rational Field

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.function_field
            sage: L.space_of_differentials()                                            # needs sage.rings.function_field
            Space of differentials of Function field in y
             defined by y^3 + (4*x^3 + 1)/(x^3 + 3)
        """
    def space_of_holomorphic_differentials(self):
        """
        Return the space of holomorphic differentials of this function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.space_of_holomorphic_differentials()                                # needs sage.libs.pari sage.modules
            (Vector space of dimension 0 over Rational Field,
             Linear map:
               From: Vector space of dimension 0 over Rational Field
               To:   Space of differentials of Rational function field in t over Rational Field,
             Section of linear map:
               From: Space of differentials of Rational function field in t over Rational Field
               To:   Vector space of dimension 0 over Rational Field)

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.function_field
            sage: L.space_of_holomorphic_differentials()                                # needs sage.rings.function_field
            (Vector space of dimension 4 over Finite Field of size 5,
             Linear map:
               From: Vector space of dimension 4 over Finite Field of size 5
               To:   Space of differentials of Function field in y
                      defined by y^3 + (4*x^3 + 1)/(x^3 + 3),
             Section of linear map:
               From: Space of differentials of Function field in y
                      defined by y^3 + (4*x^3 + 1)/(x^3 + 3)
               To:   Vector space of dimension 4 over Finite Field of size 5)
        """
    space_of_differentials_of_first_kind = space_of_holomorphic_differentials
    def basis_of_holomorphic_differentials(self):
        """
        Return a basis of the space of holomorphic differentials of this function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.basis_of_holomorphic_differentials()                                # needs sage.libs.pari sage.modules
            []

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.function_field
            sage: L.basis_of_holomorphic_differentials()                                # needs sage.rings.function_field
            [((x/(x^3 + 4))*y) d(x),
             ((1/(x^3 + 4))*y) d(x),
             ((x/(x^3 + 4))*y^2) d(x),
             ((1/(x^3 + 4))*y^2) d(x)]
        """
    basis_of_differentials_of_first_kind = basis_of_holomorphic_differentials
    def divisor_group(self):
        """
        Return the group of divisors attached to the function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(QQ)
            sage: K.divisor_group()                                                     # needs sage.modules
            Divisor group of Rational function field in t over Rational Field

            sage: _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (t^3 - 1)/(t^3 - 2))                        # needs sage.rings.function_field
            sage: L.divisor_group()                                                     # needs sage.rings.function_field
            Divisor group of Function field in y defined by y^3 + (-t^3 + 1)/(t^3 - 2)

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 - (x^3 - 1)/(x^3 - 2))                        # needs sage.rings.function_field
            sage: L.divisor_group()                                                     # needs sage.rings.function_field
            Divisor group of Function field in y defined by y^3 + (4*x^3 + 1)/(x^3 + 3)
        """
    def place_set(self):
        """
        Return the set of all places of the function field.

        EXAMPLES::

            sage: K.<t> = FunctionField(GF(7))
            sage: K.place_set()
            Set of places of Rational function field in t over Finite Field of size 7

            sage: K.<t> = FunctionField(QQ)
            sage: K.place_set()
            Set of places of Rational function field in t over Rational Field

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: L.place_set()                                                         # needs sage.rings.function_field
            Set of places of Function field in y defined by y^2 + y + (x^2 + 1)/x
        """
    @cached_method
    def completion(self, place, name=None, prec=None, gen_name=None):
        """
        Return the completion of the function field at the place.

        INPUT:

        - ``place`` -- place

        - ``name`` -- string; name of the series variable

        - ``prec`` -- positive integer; default precision

        - ``gen_name`` -- string; name of the generator of the residue field;
          used only when the place is non-rational

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: m = L.completion(p); m
            Completion map:
              From: Function field in y defined by y^2 + y + (x^2 + 1)/x
              To:   Laurent Series Ring in s over Finite Field of size 2
            sage: m(x, 10)
            s^2 + s^3 + s^4 + s^5 + s^7 + s^8 + s^9 + s^10 + O(s^12)
            sage: m(y, 10)
            s^-1 + 1 + s^3 + s^5 + s^7 + O(s^9)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: m = L.completion(p); m
            Completion map:
              From: Function field in y defined by y^2 + y + (x^2 + 1)/x
              To:   Laurent Series Ring in s over Finite Field of size 2
            sage: m(x, 10)
            s^2 + s^3 + s^4 + s^5 + s^7 + s^8 + s^9 + s^10 + O(s^12)
            sage: m(y, 10)
            s^-1 + 1 + s^3 + s^5 + s^7 + O(s^9)

            sage: K.<x> = FunctionField(GF(2))
            sage: p = K.places_finite()[0]; p                                           # needs sage.libs.pari
            Place (x)
            sage: m = K.completion(p); m                                                # needs sage.rings.function_field
            Completion map:
              From: Rational function field in x over Finite Field of size 2
              To:   Laurent Series Ring in s over Finite Field of size 2
            sage: m(1/(x+1))                                                            # needs sage.rings.function_field
            1 + s + s^2 + s^3 + s^4 + s^5 + s^6 + s^7 + s^8 + s^9 + s^10 + s^11 + s^12
            + s^13 + s^14 + s^15 + s^16 + s^17 + s^18 + s^19 + O(s^20)

            sage: p = K.place_infinite(); p
            Place (1/x)
            sage: m = K.completion(p); m                                                # needs sage.rings.function_field
            Completion map:
              From: Rational function field in x over Finite Field of size 2
              To:   Laurent Series Ring in s over Finite Field of size 2
            sage: m(x)                                                                  # needs sage.rings.function_field
            s^-1 + O(s^19)

            sage: m = K.completion(p, prec=infinity); m                                 # needs sage.rings.function_field
            Completion map:
              From: Rational function field in x over Finite Field of size 2
              To:   Lazy Laurent Series Ring in s over Finite Field of size 2
            sage: f = m(x); f                                                           # needs sage.rings.function_field
            s^-1 + ...
            sage: f.coefficient(100)                                                    # needs sage.rings.function_field
            0

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x)
            sage: O = L.maximal_order()
            sage: decomp = O.decomposition(K.maximal_order().ideal(x - 1))
            sage: pls = (decomp[0][0].place(), decomp[1][0].place())
            sage: m = L.completion(pls[0]); m
            Completion map:
              From: Function field in y defined by y^2 - x
              To:   Laurent Series Ring in s over Rational Field
            sage: xe = m(x)
            sage: ye = m(y)
            sage: ye^2 - xe == 0
            True

            sage: # needs sage.rings.function_field
            sage: decomp2 = O.decomposition(K.maximal_order().ideal(x^2 + 1))
            sage: pls2 = decomp2[0][0].place()
            sage: m = L.completion(pls2); m
            Completion map:
              From: Function field in y defined by y^2 - x
              To:   Laurent Series Ring in s over
                     Number Field in a with defining polynomial x^4 + 2*x^2 + 4*x + 2
            sage: xe = m(x)
            sage: ye = m(y)
            sage: ye^2 - xe == 0
            True
        """
    def hilbert_symbol(self, a, b, P):
        """
        Return the Hilbert symbol `(a,b)_{F_P}` for the local field `F_P`.

        The local field `F_P` is the completion of this function field `F`
        at the place `P`.

        INPUT:

        - ``a``, ``b`` -- elements of this function field

        - ``P`` -- a place of this function field

        The Hilbert symbol `(a,b)_{F_P}` is `0` if `a` or `b` is zero.
        Otherwise it takes the value `1` if  the quaternion algebra
        defined by `(a,b)` over `F_P` is split, and `-1` if said
        algebra is a division ring.

        ALGORITHM:

        For the valuation `\\nu = \\nu_P` of `F`, we compute the valuations
        `\\nu(a)` and `\\nu(b)` as well as elements `a_0` and `b_0` of the
        residue field such that for a uniformizer `\\pi` at `P`,
        `a\\pi^{-\\nu(a))}` respectively `b\\pi^{-\\nu(b)}` has the residue class
        `a_0` respectively `b_0` modulo `\\pi`. Then the Hilbert symbol is
        computed by formula 12.4.10 in [Voi2021]_.

        Currently only implemented for global function fields.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(17))
            sage: P = K.places()[0]; P
            Place (1/x)
            sage: a = (5*x + 6)/(x + 15)
            sage: b = 7/x
            sage: K.hilbert_symbol(a, b, P)
            -1

            sage: Q = K.places()[7]; Q
            Place (x + 6)
            sage: c = 15*x + 12
            sage: d = 16/(x + 13)
            sage: K.hilbert_symbol(c, d, Q)
            1

        Check that the Hilbert symbol is symmetric and bimultiplicative::

            sage: K.<x> = FunctionField(GF(5)); R.<T> = PolynomialRing(K)
            sage: f = ((x^2 + 2*x + 2)*T^5 + (4*x^2 + 2*x + 3)*T^4 + 3*T^3 + 4*T^2
            ....:     + (2/(x^2 + 4*x + 1))*T + 3*x^2 + 2*x + 4)
            sage: L.<y> = K.extension(f)
            sage: a = L.random_element()
            sage: b = L.random_element()
            sage: c = L.random_element()
            sage: P = L.places_above(K.places()[0])[1]
            sage: Q = L.places_above(K.places()[1])[0]

            sage: hP_a_c = L.hilbert_symbol(a, c, P)
            sage: hP_a_c == L.hilbert_symbol(c, a, P)
            True
            sage: L.hilbert_symbol(a, b, P) * hP_a_c == L.hilbert_symbol(a, b*c, P)
            True
            sage: hP_a_c * L.hilbert_symbol(b, c, P) == L.hilbert_symbol(a*b, c, P)
            True

            sage: hQ_a_c = L.hilbert_symbol(a, c, Q)
            sage: hQ_a_c == L.hilbert_symbol(c, a, Q)
            True
            sage: L.hilbert_symbol(a, b, Q) * hQ_a_c == L.hilbert_symbol(a, b*c, Q)
            True
            sage: hQ_a_c * L.hilbert_symbol(b, c, Q) == L.hilbert_symbol(a*b, c, Q)
            True
        """
    def extension_constant_field(self, k):
        """
        Return the constant field extension with constant field `k`.

        INPUT:

        - ``k`` -- an extension field of the constant field of this function field

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: E = F.extension_constant_field(GF(2^4))
            sage: E
            Function field in y defined by y^2 + y + (x^2 + 1)/x over its base
            sage: E.constant_base_field()
            Finite Field in z4 of size 2^4
        """
    @cached_method
    def jacobian(self, model=None, base_div=None, **kwds):
        """
        Return the Jacobian of the function field.

        INPUT:

        - ``model`` -- (default: ``'hess'``) model to use for arithmetic

        - ``base_div`` -- an effective divisor

        The degree of the base divisor should satisfy certain degree condition
        corresponding to the model used. The following table lists these
        conditions. Let `g` be the genus of the function field.

        - ``hess``: ideal-based arithmetic; requires base divisor of degree `g`

        - ``km_large``: Khuri-Makdisi's large model; requires base divisor of
          degree at least `2g + 1`

        - ``km_medium``: Khuri-Makdisi's medium model; requires base divisor of
          degree at least `2g + 1`

        - ``km_small``: Khuri-Makdisi's small model requires base divisor of
          degree at least `g + 1`

        We assume the function field has a rational place. If a base divisor is
        not given, one is constructed using an arbitrary rational place.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(GF(5), 2)
            sage: C = Curve(y^2*(x^3 - 1) - (x^3 - 2))
            sage: F = C.function_field()
            sage: F.jacobian()
            Jacobian of Function field in y defined by (x^3 + 4)*y^2 + 4*x^3 + 2 (Hess model)

        TESTS:

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve(y^2 - x^3 - 1, A).projective_closure()
            sage: C.jacobian(model='hess')
            Traceback (most recent call last):
            ...
            ValueError: failed to obtain a rational place; provide a base divisor
        """
