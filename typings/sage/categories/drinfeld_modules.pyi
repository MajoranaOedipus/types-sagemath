from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.homsets import Homsets as Homsets
from sage.categories.objects import Objects as Objects
from sage.misc.functional import log as log
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer

class DrinfeldModules(Category_over_base_ring):
    """
    This class implements the category of Drinfeld
    `\\mathbb{F}_q[T]`-modules on a given base field.

    Let `\\mathbb{F}_q[T]` be a polynomial ring with coefficients in a
    finite field `\\mathbb{F}_q` and let `K` be a field. Fix a ring
    morphism `\\gamma: \\mathbb{F}_q[T] \\to K`; we say that `K` is an
    `\\mathbb{F}_q[T]`*-field*. Let `K\\{\\tau\\}` be the ring of Ore
    polynomials with coefficients in `K`, whose multiplication is given
    by the rule `\\tau \\lambda = \\lambda^q \\tau` for any `\\lambda \\in K`.

    The extension `K`/`\\mathbb{F}_q[T]` (represented as an instance of
    the class :class:`sage.rings.ring_extension.RingExtension`) is the
    *base field* of the category; its defining morphism `\\gamma` is
    called the *base morphism*.

    The monic polynomial that generates the kernel of `\\gamma` is called
    the `\\mathbb{F}_q[T]`-*characteristic*, or *function-field
    characteristic*, of the base field. We say that `\\mathbb{F}_q[T]` is
    the *function ring* of the category; `K\\{\\tau\\}` is the *Ore
    polynomial ring*. The constant coefficient of the category is the
    image of `T` under the base morphism.

    .. RUBRIC:: Construction

    Generally, Drinfeld modules objects are created before their
    category, and the category is retrieved as an attribute of the
    Drinfeld module::

        sage: Fq = GF(11)
        sage: A.<T> = Fq[]
        sage: K.<z> = Fq.extension(4)
        sage: p_root = z^3 + 7*z^2 + 6*z + 10
        sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
        sage: C = phi.category()
        sage: C
        Category of Drinfeld modules over Finite Field in z of size 11^4

    The output tells the user that the category is only defined by its
    base.

    .. RUBRIC:: Properties of the category

    The base field is retrieved using the method :meth:`base`.

        sage: C.base()
        Finite Field in z of size 11^4 over its base

    Equivalently, one can use :meth:`base_morphism` to retrieve the base
    morphism::

        sage: C.base_morphism()
        Ring morphism:
          From: Univariate Polynomial Ring in T over Finite Field of size 11
          To:   Finite Field in z of size 11^4
          Defn: T |--> z^3 + 7*z^2 + 6*z + 10

    The so-called constant coefficient --- which is the same for all
    Drinfeld modules in the category --- is simply the image of `T` by
    the base morphism::

        sage: C.constant_coefficient()
        z^3 + 7*z^2 + 6*z + 10
        sage: C.base_morphism()(T) == C.constant_coefficient()
        True

    Similarly, the function ring-characteristic of the category is
    either `0` or the unique monic polynomial in `\\mathbb{F}_q[T]` that
    generates the kernel of the base::

        sage: C.characteristic()
        T^2 + 7*T + 2
        sage: C.base_morphism()(C.characteristic())
        0

    The base field, base morphism, function ring and Ore polynomial ring
    are the same for the category and its objects::

        sage: C.base() is phi.base()
        True
        sage: C.base_morphism() is phi.base_morphism()
        True

        sage: C.function_ring()
        Univariate Polynomial Ring in T over Finite Field of size 11
        sage: C.function_ring() is phi.function_ring()
        True

        sage: C.ore_polring()
        Ore Polynomial Ring in t over Finite Field in z of size 11^4 twisted by z |--> z^11
        sage: C.ore_polring() is phi.ore_polring()
        True


    .. RUBRIC:: Creating Drinfeld module objects from the category

    Calling :meth:`object` with an Ore polynomial creates a Drinfeld module
    object in the category whose generator is the input::

        sage: psi = C.object([p_root, 1])
        sage: psi
        Drinfeld module defined by T |--> t + z^3 + 7*z^2 + 6*z + 10
        sage: psi.category() is C
        True

    Of course, the constant coefficient of the input must be the same as
    the category::

        sage: C.object([z, 1])
        Traceback (most recent call last):
        ...
        ValueError: constant coefficient must equal that of the category

    It is also possible to create a random object in the category. The
    input is the desired rank::

        sage: rho = C.random_object(2)
        sage: rho  # random
        Drinfeld module defined by T |--> (7*z^3 + 7*z^2 + 10*z + 2)*t^2 + (9*z^3 + 5*z^2 + 2*z + 7)*t + z^3 + 7*z^2 + 6*z + 10
        sage: rho.rank() == 2
        True
        sage: rho.category() is C
        True

    TESTS::

        sage: Fq = GF(11)
        sage: A.<T> = Fq[]
        sage: K.<z> = Fq.extension(4)
        sage: from sage.categories.drinfeld_modules import DrinfeldModules
        sage: base = Hom(A, K)(0)
        sage: C = DrinfeldModules(base)  # known bug (blankline)
        <BLANKLINE>
        Traceback (most recent call last):
        ...
        TypeError: base field must be a ring extension

    Note that `C.base_morphism()` has codomain `K` while
    the defining morphism of `C.base()` has codomain `K` viewed
    as an `A`-field. Thus, they differ::

        sage: C.base().defining_morphism() == C.base_morphism()
        False

    ::

        sage: base = Hom(A, A)(1)
        sage: C = DrinfeldModules(base)  # known bug (blankline)
        <BLANKLINE>
        Traceback (most recent call last):
        ...
        TypeError: base field must be a ring extension

    ::

        sage: base = 'I hate Rostropovitch'
        sage: C = DrinfeldModules(base)  # known bug (blankline)
        <BLANKLINE>
        Traceback (most recent call last):
        ...
        TypeError: input must be a ring morphism

    ::

        sage: ZZT.<T> = ZZ[]
        sage: base = Hom(ZZT, K)(1)
        sage: C = DrinfeldModules(base)  # known bug (blankline)
        <BLANKLINE>
        Traceback (most recent call last):
        ...
        TypeError: function ring base must be a finite field
    """
    def __init__(self, base_morphism, name: str = 't') -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base_field`` -- the base field, which is a ring extension
          over a base

        - ``name`` -- (default: ``'t'``) the name of the Ore polynomial
          variable

        TESTS::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: ore_polring.<t> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: C._ore_polring is ore_polring
            True
            sage: C._function_ring is A
            True
            sage: C._constant_coefficient == C._base_morphism(T)
            True
            sage: C._characteristic(C._constant_coefficient)
            0
        """
    def Homsets(self):
        """
        Return the category of homsets.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()

            sage: from sage.categories.homsets import Homsets
            sage: C.Homsets() is Homsets()
            True
        """
    def Endsets(self):
        """
        Return the category of endsets.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()

            sage: from sage.categories.homsets import Homsets
            sage: C.Endsets() is Homsets().Endsets()
            True
        """
    def A_field(self):
        """
        Return the underlying `A`-field of this category,
        viewed as an algebra over the function ring `A`.

        This is an instance of the class
        :class:`sage.rings.ring_extension.RingExtension`.

        NOTE::

            This method has the same behavior as :meth:`base`.

        EXAMPLES::

            sage: Fq = GF(25)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(6)
            sage: phi = DrinfeldModule(A, [z, z^3, z^5])
            sage: C = phi.category()
            sage: C.A_field()
            Finite Field in z of size 5^12 over its base
        """
    def base_morphism(self):
        """
        Return the base morphism of the category.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.base_morphism()
            Ring morphism:
              From: Univariate Polynomial Ring in T over Finite Field of size 11
              To:   Finite Field in z of size 11^4
              Defn: T |--> z^3 + 7*z^2 + 6*z + 10

            sage: C.constant_coefficient() == C.base_morphism()(T)
            True
        """
    def base_over_constants_field(self):
        """
        Return the base field, seen as an extension over the constants
        field `\\mathbb{F}_q`.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.base_over_constants_field()
            Field in z with defining polynomial x^4 + 8*x^2 + 10*x + 2 over its base
        """
    def characteristic(self):
        """
        Return the function ring-characteristic.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.characteristic()
            T^2 + 7*T + 2

        ::

            sage: psi = DrinfeldModule(A, [Frac(A).gen(), 1])
            sage: C = psi.category()
            sage: C.characteristic()
            0
        """
    def constant_coefficient(self):
        """
        Return the constant coefficient of the category.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.constant_coefficient()
            z^3 + 7*z^2 + 6*z + 10
            sage: C.constant_coefficient() == C.base()(T)
            True
        """
    def function_ring(self):
        """
        Return the function ring of the category.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.function_ring()
            Univariate Polynomial Ring in T over Finite Field of size 11
            sage: C.function_ring() is A
            True
        """
    def object(self, gen):
        """
        Return a Drinfeld module object in the category whose generator
        is the input.

        INPUT:

        - ``gen`` -- the generator of the Drinfeld module, given as an Ore
          polynomial or a list of coefficients

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: psi = DrinfeldModule(A, [p_root, 1])
            sage: C = psi.category()

            sage: phi = C.object([p_root, 0, 1])
            sage: phi
            Drinfeld module defined by T |--> t^2 + z^3 + 7*z^2 + 6*z + 10
            sage: t = phi.ore_polring().gen()
            sage: C.object(t^2 + z^3 + 7*z^2 + 6*z + 10) is phi
            True
        """
    def ore_polring(self):
        """
        Return the Ore polynomial ring of the category.

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.ore_polring()
            Ore Polynomial Ring in t over Finite Field in z of size 11^4 twisted by z |--> z^11
        """
    def random_object(self, rank):
        """
        Return a random Drinfeld module in the category with given rank.

        INPUT:

        - ``rank`` -- integer; the rank of the Drinfeld module

        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()

            sage: psi = C.random_object(3)  # random
            Drinfeld module defined by T |--> (6*z^3 + 4*z^2 + 10*z + 9)*t^3 + (4*z^3 + 8*z^2 + 8*z)*t^2 + (10*z^3 + 3*z^2 + 6*z)*t + z^3 + 7*z^2 + 6*z + 10
            sage: psi.rank() == 3
            True
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Fq = GF(11)
            sage: A.<T> = Fq[]
            sage: K.<z> = Fq.extension(4)
            sage: p_root = z^3 + 7*z^2 + 6*z + 10
            sage: phi = DrinfeldModule(A, [p_root, 0, 0, 1])
            sage: C = phi.category()
            sage: C.super_categories()
            [Category of objects]
        """
    class ParentMethods:
        def A_field(self):
            """
            Return the underlying `A`-field of this Drinfeld module,
            viewed as an algebra over the function ring `A`.

            This is an instance of the class
            :class:`sage.rings.ring_extension.RingExtension`.

            NOTE::

                This method has the same behavior as :meth:`base`.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z> = Fq.extension(6)
                sage: phi = DrinfeldModule(A, [z, z^3, z^5])
                sage: phi.A_field()
                Finite Field in z of size 5^12 over its base
            """
        def base(self):
            """
            Return the underlying `A`-field of this Drinfeld module,
            viewed as an algebra over the function ring `A`.

            This is an instance of the class
            :class:`sage.rings.ring_extension.RingExtension`.

            NOTE::

                This method has the same behavior as :meth:`A_field`.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.base()
                Finite Field in z12 of size 5^12 over its base

            The base can be infinite::

                sage: sigma = DrinfeldModule(A, [Frac(A).gen(), 1])
                sage: sigma.base()
                Fraction Field of Univariate Polynomial Ring in T over Finite Field in z2 of size 5^2 over its base
            """
        def base_morphism(self):
            """
            Return the base morphism of this Drinfeld module.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.base_morphism()
                Ring morphism:
                  From: Univariate Polynomial Ring in T over Finite Field in z2 of size 5^2
                  To:   Finite Field in z12 of size 5^12
                  Defn: T |--> 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12

            The base field can be infinite::

                sage: sigma = DrinfeldModule(A, [Frac(A).gen(), 1])
                sage: sigma.base_morphism()
                Coercion map:
                  From: Univariate Polynomial Ring in T over Finite Field in z2 of size 5^2
                  To:   Fraction Field of Univariate Polynomial Ring in T over Finite Field in z2 of size 5^2
            """
        def base_over_constants_field(self):
            """
            Return the base field, seen as an extension over the constants
            field `\\mathbb{F}_q`.

            This is an instance of the class
            :class:`sage.rings.ring_extension.RingExtension`.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.base_over_constants_field()
                Field in z12 with defining polynomial x^6 + (4*z2 + 3)*x^5 + x^4 + (3*z2 + 1)*x^3 + x^2 + (4*z2 + 1)*x + z2 over its base
            """
        def characteristic(self):
            """
            Return the function ring-characteristic.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.characteristic()
                T^2 + (4*z2 + 2)*T + 2
                sage: phi.base_morphism()(phi.characteristic())
                0

            ::

                sage: B.<Y> = Fq[]
                sage: L = Frac(B)
                sage: psi = DrinfeldModule(A, [L(1), 0, 0, L(1)])
                sage: psi.characteristic()
                Traceback (most recent call last):
                ...
                NotImplementedError: function ring characteristic not implemented in this case
            """
        def function_ring(self):
            """
            Return the function ring of this Drinfeld module.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.function_ring()
                Univariate Polynomial Ring in T over Finite Field in z2 of size 5^2
                sage: phi.function_ring() is A
                True
            """
        def constant_coefficient(self):
            """
            Return the constant coefficient of the generator
            of this Drinfeld module.

            OUTPUT: an element in the base field

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: phi.constant_coefficient() == p_root
                True

            Let `\\mathbb{F}_q[T]` be the function ring, and let `\\gamma` be
            the base of the Drinfeld module. The constant coefficient is
            `\\gamma(T)`::

                sage: C = phi.category()
                sage: base = C.base()
                sage: base(T) == phi.constant_coefficient()
                True

            Naturally, two Drinfeld modules in the same category have the
            same constant coefficient::

                sage: t = phi.ore_polring().gen()
                sage: psi = C.object(phi.constant_coefficient() + t^3)
                sage: psi
                Drinfeld module defined by T |--> t^3 + 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12

            Reciprocally, it is impossible to create two Drinfeld modules in
            this category if they do not share the same constant
            coefficient::

                sage: rho = C.object(phi.constant_coefficient() + 1 + t^3)
                Traceback (most recent call last):
                ...
                ValueError: constant coefficient must equal that of the category
            """
        def ore_polring(self):
            """
            Return the Ore polynomial ring of this Drinfeld module.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])
                sage: S = phi.ore_polring()
                sage: S
                Ore Polynomial Ring in t over Finite Field in z12 of size 5^12 twisted by z12 |--> z12^(5^2)

            The Ore polynomial ring can also be retrieved from the category
            of the Drinfeld module::

                sage: S is phi.category().ore_polring()
                True

            The generator of the Drinfeld module is in the Ore polynomial
            ring::

                sage: phi(T) in S
                True
            """
        def ore_variable(self):
            """
            Return the variable of the Ore polynomial ring of this Drinfeld module.

            EXAMPLES::

                sage: Fq = GF(25)
                sage: A.<T> = Fq[]
                sage: K.<z12> = Fq.extension(6)
                sage: p_root = 2*z12^11 + 2*z12^10 + z12^9 + 3*z12^8 + z12^7 + 2*z12^5 + 2*z12^4 + 3*z12^3 + z12^2 + 2*z12
                sage: phi = DrinfeldModule(A, [p_root, z12^3, z12^5])

                sage: phi.ore_polring()
                Ore Polynomial Ring in t over Finite Field in z12 of size 5^12 twisted by z12 |--> z12^(5^2)
                sage: phi.ore_variable()
                t
            """
