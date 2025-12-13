from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.rngs import Rngs as Rngs
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.misc.prandom import randint as randint
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent

class Rings(CategoryWithAxiom):
    """
    The category of rings.

    Associative rings with unit, not necessarily commutative

    EXAMPLES::

        sage: Rings()
        Category of rings
        sage: sorted(Rings().super_categories(), key=str)
        [Category of rngs, Category of semirings]

        sage: sorted(Rings().axioms())
        ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse',
         'AdditiveUnital', 'Associative', 'Distributive', 'Unital']

        sage: Rings() is (CommutativeAdditiveGroups() & Monoids()).Distributive()
        True
        sage: Rings() is Rngs().Unital()
        True
        sage: Rings() is Semirings().AdditiveInverse()
        True

    TESTS::

        sage: TestSuite(Rings()).run()

    .. TODO::

        (see :issue:`sage_trac/wiki/CategoriesRoadMap`)

        - Make Rings() into a subcategory or alias of Algebras(ZZ);

        - A parent P in the category ``Rings()`` should automatically be
          in the category ``Algebras(P)``.
    """
    class MorphismMethods:
        @cached_method
        def is_injective(self) -> bool:
            """
            Return whether or not this morphism is injective.

            EXAMPLES::

                sage: # needs sage.libs.singular
                sage: R.<x,y> = QQ[]
                sage: R.hom([x, y^2], R).is_injective()
                True
                sage: R.hom([x, x^2], R).is_injective()
                False
                sage: S.<u,v> = R.quotient(x^3*y)
                sage: R.hom([v, u], S).is_injective()
                False
                sage: S.hom([-u, v], S).is_injective()
                True
                sage: S.cover().is_injective()
                False

            If the domain is a field, the homomorphism is injective::

                sage: K.<x> = FunctionField(QQ)
                sage: L.<y> = FunctionField(QQ)
                sage: f = K.hom([y]); f
                Function Field morphism:
                  From: Rational function field in x over Rational Field
                  To:   Rational function field in y over Rational Field
                  Defn: x |--> y
                sage: f.is_injective()
                True

            Unless the codomain is the zero ring::

                sage: codomain = Integers(1)
                sage: f = QQ.hom([Zmod(1)(0)], check=False)
                sage: f.is_injective()
                False

            Homomorphism from rings of characteristic zero to rings of positive
            characteristic can not be injective::

                sage: R.<x> = ZZ[]
                sage: f = R.hom([GF(3)(1)]); f
                Ring morphism:
                  From: Univariate Polynomial Ring in x over Integer Ring
                  To:   Finite Field of size 3
                  Defn: x |--> 1
                sage: f.is_injective()
                False

            A morphism whose domain is an order in a number field is injective if
            the codomain has characteristic zero::

                sage: K.<x> = FunctionField(QQ)
                sage: f = ZZ.hom(K); f
                Composite map:
                  From: Integer Ring
                  To:   Rational function field in x over Rational Field
                  Defn:   Conversion via FractionFieldElement_1poly_field map:
                          From: Integer Ring
                          To:   Fraction Field of Univariate Polynomial Ring in x
                                over Rational Field
                        then
                          Isomorphism:
                          From: Fraction Field of Univariate Polynomial Ring in x
                                over Rational Field
                          To:   Rational function field in x over Rational Field
                sage: f.is_injective()
                True

            A coercion to the fraction field is injective::

                sage: R = ZpFM(3)                                                       # needs sage.rings.padics
                sage: R.fraction_field().coerce_map_from(R).is_injective()
                True
            """
        def extend_to_fraction_field(self):
            """
            Return the extension of this morphism to fraction fields of
            the domain and the codomain.

            EXAMPLES::

                sage: S.<x> = QQ[]
                sage: f = S.hom([x + 1]); f
                Ring endomorphism of Univariate Polynomial Ring in x over Rational Field
                    Defn: x |--> x + 1

                sage: g = f.extend_to_fraction_field(); g                               # needs sage.libs.singular
                Ring endomorphism of Fraction Field of Univariate Polynomial Ring in x
                 over Rational Field
                    Defn: x |--> x + 1
                sage: g(x)                                                              # needs sage.libs.singular
                x + 1
                sage: g(1/x)                                                            # needs sage.libs.singular
                1/(x + 1)

            If this morphism is not injective, it does not extend to the fraction
            field and an error is raised::

                sage: f = GF(5).coerce_map_from(ZZ)
                sage: f.extend_to_fraction_field()
                Traceback (most recent call last):
                ...
                ValueError: the morphism is not injective

            TESTS::

                sage: A.<x> = RR[]
                sage: phi = A.hom([x + 1])
                sage: phi.extend_to_fraction_field()                                    # needs sage.libs.singular
                Ring endomorphism of Fraction Field of
                 Univariate Polynomial Ring in x over Real Field with 53 bits of precision
                  Defn: x |--> x + 1.00000000000000
            """
    class SubcategoryMethods:
        def NoZeroDivisors(self):
            """
            Return the full subcategory of the objects of ``self`` having
            no nonzero zero divisors.

            A *zero divisor* in a ring `R` is an element `x \\in R` such
            that there exists a nonzero element `y \\in R` such that
            `x \\cdot y = 0` or `y \\cdot x = 0`
            (see :wikipedia:`Zero_divisor`).

            EXAMPLES::

                sage: Rings().NoZeroDivisors()
                Category of domains

            TESTS::

                sage: TestSuite(Rings().NoZeroDivisors()).run()
                sage: Algebras(QQ).NoZeroDivisors.__module__
                'sage.categories.rings'
            """
        def Division(self):
            """
            Return the full subcategory of the division objects of ``self``.

            A ring satisfies the *division axiom* if all nonzero
            elements have multiplicative inverses.

            EXAMPLES::

                sage: Rings().Division()
                Category of division rings
                sage: Rings().Commutative().Division()
                Category of fields

            TESTS::

                sage: TestSuite(Rings().Division()).run()
                sage: Algebras(QQ).Division.__module__
                'sage.categories.rings'
            """
    NoZeroDivisors: Incomplete
    Division: Incomplete
    Commutative: Incomplete
    class ParentMethods:
        def is_ring(self) -> bool:
            """
            Return ``True``, since this in an object of the category of rings.

            EXAMPLES::

                sage: Parent(QQ,category=Rings()).is_ring()
                True
            """
        def is_commutative(self) -> bool:
            """
            Return whether the ring is commutative.

            The answer is ``True`` only if the category is a sub-category of
            ``CommutativeRings``.

            It is recommended to use instead ``R in Rings().Commutative()``.

            EXAMPLES::

                sage: Q.<i,j,k> = QuaternionAlgebra(QQ, -1, -1)                             # needs sage.combinat sage.modules
                sage: Q.is_commutative()                                                    # needs sage.combinat sage.modules
                False
            """
        def is_integral_domain(self, proof: bool = True) -> bool:
            """
            Return ``True`` if this ring is an integral domain.

            INPUT:

            - ``proof`` -- boolean (default: ``True``); determine what to do
              in unknown cases

            ALGORITHM:

            If the parameter ``proof`` is set to ``True``, the returned value is
            correct but the method might throw an error.  Otherwise, if it is set
            to ``False``, the method returns ``True`` if it can establish that ``self``
            is an integral domain and ``False`` otherwise.

            EXAMPLES::

                sage: QQ.is_integral_domain()
                True
                sage: ZZ.is_integral_domain()
                True
                sage: ZZ['x,y,z'].is_integral_domain()
                True
                sage: Integers(8).is_integral_domain()
                False
                sage: Zp(7).is_integral_domain()                                            # needs sage.rings.padics
                True
                sage: Qp(7).is_integral_domain()                                            # needs sage.rings.padics
                True
                sage: R.<a,b> = QQ[]
                sage: S.<x,y> = R.quo((b^3))                                                # needs sage.libs.singular
                sage: S.is_integral_domain()                                                # needs sage.libs.singular
                False
                sage: R = ZZ.quotient(ZZ.ideal(10)); R.is_integral_domain()
                False

            This illustrates the use of the ``proof`` parameter::

                sage: R.<a,b> = ZZ[]
                sage: S.<x,y> = R.quo((b^3))                                                # needs sage.libs.singular
                sage: S.is_integral_domain(proof=True)                                      # needs sage.libs.singular
                Traceback (most recent call last):
                ...
                NotImplementedError
                sage: S.is_integral_domain(proof=False)                                     # needs sage.libs.singular
                False

            TESTS:

            Make sure :issue:`10481` is fixed::

                sage: x = polygen(ZZ, 'x')
                sage: R.<a> = ZZ['x'].quo(x^2)                                              # needs sage.libs.pari
                sage: R.fraction_field()                                                    # needs sage.libs.pari
                Traceback (most recent call last):
                ...
                TypeError: self must be an integral domain.
                sage: R.is_integral_domain()                                                # needs sage.libs.pari
                False

            Forward the proof flag to ``is_field``, see :issue:`22910`::

                sage: # needs sage.libs.singular
                sage: R1.<x> = GF(5)[]
                sage: F1 = R1.quotient_ring(x^2 + x + 1)
                sage: R2.<x> = F1[]
                sage: F2 = R2.quotient_ring(x^2 + x + 1)
                sage: F2.is_integral_domain(False)
                False
            """
        def is_integrally_closed(self) -> bool:
            """
            Return whether this ring is integrally closed.

            This is the default implementation that
            raises a :exc:`NotImplementedError`.

            EXAMPLES::

                sage: x = polygen(ZZ, 'x')
                sage: K.<a> = NumberField(x^2 + 189*x + 394)
                sage: R = K.order(2*a)
                sage: R.is_integrally_closed()
                False
                sage: R
                Order of conductor 2 generated by 2*a in Number Field in a with defining polynomial x^2 + 189*x + 394
                sage: S = K.maximal_order(); S
                Maximal Order generated by a in Number Field in a with defining polynomial x^2 + 189*x + 394
                sage: S.is_integrally_closed()
                True
            """
        def is_noetherian(self):
            """
            Return ``True`` if this ring is Noetherian.

            EXAMPLES::

                sage: QQ.is_noetherian()
                True
                sage: ZZ.is_noetherian()
                True
            """
        def is_prime_field(self):
            """
            Return ``True`` if this ring is one of the prime fields `\\QQ` or
            `\\GF{p}`.

            EXAMPLES::

                sage: QQ.is_prime_field()
                True
                sage: GF(3).is_prime_field()
                True
                sage: GF(9, 'a').is_prime_field()                                           # needs sage.rings.finite_rings
                False
                sage: ZZ.is_prime_field()
                False
                sage: QQ['x'].is_prime_field()
                False
                sage: Qp(19).is_prime_field()                                               # needs sage.rings.padics
                False
            """
        def is_zero(self) -> bool:
            """
            Return ``True`` if this is the zero ring.

            EXAMPLES::

                sage: Integers(1).is_zero()
                True
                sage: Integers(2).is_zero()
                False
                sage: QQ.is_zero()
                False
                sage: R.<x> = ZZ[]
                sage: R.quo(1).is_zero()
                True
                sage: R.<x> = GF(101)[]
                sage: R.quo(77).is_zero()
                True
                sage: R.quo(x^2 + 1).is_zero()                                          # needs sage.libs.pari
                False
            """
        def is_subring(self, other):
            """
            Return ``True`` if the canonical map from ``self`` to ``other`` is
            injective.

            This raises a :exc:`NotImplementedError` if not known.

            EXAMPLES::

                sage: ZZ.is_subring(QQ)
                True
                sage: ZZ.is_subring(GF(19))
                False

            TESTS::

                sage: QQ.is_subring(QQ['x'])
                True
                sage: QQ.is_subring(GF(7))
                False
                sage: QQ.is_subring(CyclotomicField(7))                                     # needs sage.rings.number_field
                True
                sage: QQ.is_subring(ZZ)
                False

            Every ring is a subring of itself, :issue:`17287`::

                sage: QQbar.is_subring(QQbar)                                               # needs sage.rings.number_field
                True
                sage: RR.is_subring(RR)
                True
                sage: CC.is_subring(CC)                                                     # needs sage.rings.real_mpfr
                True
                sage: x = polygen(ZZ, 'x')
                sage: K.<a> = NumberField(x^3 - x + 1/10)                                   # needs sage.rings.number_field
                sage: K.is_subring(K)                                                       # needs sage.rings.number_field
                True
                sage: R.<x> = RR[]
                sage: R.is_subring(R)
                True
            """
        def is_field(self, proof: bool = True):
            """
            Return ``True`` if this ring is a field.

            INPUT:

            - ``proof`` -- boolean (default: ``True``); determines what to do in
              unknown cases

            ALGORITHM:

            If the parameter ``proof`` is set to ``True``, the returned value is
            correct but the method might throw an error.  Otherwise, if it is set
            to ``False``, the method returns ``True`` if it can establish that
            ``self`` is a field and ``False`` otherwise.

            EXAMPLES::

                sage: QQ.is_field()
                True
                sage: GF(9, 'a').is_field()                                                 # needs sage.rings.finite_rings
                True
                sage: ZZ.is_field()
                False
                sage: QQ['x'].is_field()
                False
                sage: Frac(QQ['x']).is_field()
                True

            This illustrates the use of the ``proof`` parameter::

                sage: R.<a,b> = QQ[]
                sage: S.<x,y> = R.quo((b^3))                                                # needs sage.libs.singular
                sage: S.is_field(proof=True)                                                # needs sage.libs.singular
                Traceback (most recent call last):
                ...
                NotImplementedError
                sage: S.is_field(proof=False)                                               # needs sage.libs.singular
                False
            """
        def zeta(self, n: int = 2, all: bool = False):
            """
            Return a primitive ``n``-th root of unity in ``self`` if there
            is one, or raise a :exc:`ValueError` otherwise.

            INPUT:

            - ``n`` -- positive integer

            - ``all`` -- boolean (default: ``False``); whether to return
              a list of all primitive `n`-th roots of unity. If ``True``, raise a
              :exc:`ValueError` if ``self`` is not an integral domain.

            OUTPUT: element of ``self`` of finite order

            EXAMPLES::

                sage: QQ.zeta()
                -1
                sage: QQ.zeta(1)
                1
                sage: CyclotomicField(6).zeta(6)                                            # needs sage.rings.number_field
                zeta6
                sage: CyclotomicField(3).zeta(3)                                            # needs sage.rings.number_field
                zeta3
                sage: CyclotomicField(3).zeta(3).multiplicative_order()                     # needs sage.rings.number_field
                3

                sage: # needs sage.rings.finite_rings
                sage: a = GF(7).zeta(); a
                3
                sage: a.multiplicative_order()
                6
                sage: a = GF(49,'z').zeta(); a
                z
                sage: a.multiplicative_order()
                48
                sage: a = GF(49,'z').zeta(2); a
                6
                sage: a.multiplicative_order()
                2

                sage: QQ.zeta(3)
                Traceback (most recent call last):
                ...
                ValueError: no n-th root of unity in rational field
                sage: Zp(7, prec=8).zeta()                                                  # needs sage.rings.padics
                3 + 4*7 + 6*7^2 + 3*7^3 + 2*7^5 + 6*7^6 + 2*7^7 + O(7^8)

            TESTS::

                sage: R.<x> = QQ[]
                sage: R.zeta(1)
                1
                sage: R.zeta(2)
                -1
                sage: R.zeta(3)                                                             # needs sage.libs.pari
                Traceback (most recent call last):
                ...
                ValueError: no 3rd root of unity in Univariate Polynomial Ring in x over Rational Field
                sage: IntegerModRing(8).zeta(2, all = True)
                Traceback (most recent call last):
                ...
                ValueError: ring is not an integral domain
            """
        def zeta_order(self):
            """
            Return the order of the distinguished root of unity in ``self``.

            EXAMPLES::

                sage: CyclotomicField(19).zeta_order()                                      # needs sage.rings.number_field
                38
                sage: GF(19).zeta_order()
                18
                sage: GF(5^3,'a').zeta_order()                                              # needs sage.rings.finite_rings
                124
                sage: Zp(7, prec=8).zeta_order()                                            # needs sage.rings.padics
                6
            """
        def localization(self, *args, **kwds) -> None:
            """
            Return the localization of ``self``.

            This only works for integral domains.

            EXAMPLES::

                sage: R = Zmod(6)
                sage: R.localization((4))
                Traceback (most recent call last):
                ...
                TypeError: self must be an integral domain
            """
        def bracket(self, x, y):
            """
            Return the Lie bracket `[x, y] = x y - y x` of `x` and `y`.

            INPUT:

            - ``x``, ``y`` -- elements of ``self``

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: F = AlgebrasWithBasis(QQ).example()
                sage: F
                An example of an algebra with basis:
                 the free algebra on the generators ('a', 'b', 'c') over Rational Field
                sage: a, b, c = F.algebra_generators()
                sage: F.bracket(a, b)
                B[word: ab] - B[word: ba]

            This measures the default of commutation between `x` and `y`.
            `F` endowed with the bracket operation is a Lie algebra;
            in particular, it satisfies Jacobi's identity::

                sage: (F.bracket(F.bracket(a,b), c) + F.bracket(F.bracket(b,c), a)      # needs sage.combinat sage.modules
                ....:  + F.bracket(F.bracket(c,a), b))
                0
            """
        def __pow__(self, n):
            """
            Return the free module of rank `n` over this ring.  If n is a tuple of
            two elements, creates a matrix space.

            EXAMPLES::

                sage: QQ^5                                                              # needs sage.modules
                Vector space of dimension 5 over Rational Field
                sage: Integers(20)^1000                                                 # needs sage.modules
                Ambient free module of rank 1000 over Ring of integers modulo 20

                sage: QQ^(2, 3)                                                         # needs sage.modules
                Full MatrixSpace of 2 by 3 dense matrices over Rational Field
            """
        def nilradical(self):
            """
            Return the nilradical of this ring.

            EXAMPLES::

                sage: QQ['x,y'].nilradical()
                Ideal (0) of Multivariate Polynomial Ring in x, y over Rational Field

            .. SEEALSO::

                :meth:`~sage.categories.finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis.ParentMethods.nilradical`
            """
        @cached_method
        def unit_ideal(self):
            """
            Return the unit ideal of this ring.

            EXAMPLES::

                sage: Zp(7).unit_ideal()                                                    # needs sage.rings.padics
                Principal ideal (1 + O(7^20)) of 7-adic Ring with capped relative precision 20
            """
        def characteristic(self):
            """
            Return the characteristic of this ring.

            EXAMPLES::

                sage: QQ.characteristic()
                0
                sage: GF(19).characteristic()
                19
                sage: Integers(8).characteristic()
                8
                sage: Zp(5).characteristic()                                            # needs sage.rings.padics
                0
            """
        def ideal(self, *args, **kwds):
            """
            Create an ideal of this ring.

            INPUT:

            - an element or a list/tuple/sequence of elements, the generators

            - ``coerce`` -- boolean (default: ``True``); whether to first coerce
              the elements into this ring. This must be a keyword
              argument. Only set it to ``False`` if you are certain that each
              generator is already in the ring.

            - ``ideal_class`` -- callable (default: ``self._ideal_class_()``);
              this must be a keyword argument. A constructor for ideals, taking
              the ring as the first argument and then the generators.
              Usually a subclass of :class:`~sage.rings.ideal.Ideal_generic` or
              :class:`~sage.rings.noncommutative_ideals.Ideal_nc`.

            - Further named arguments (such as ``side`` in the case of
              non-commutative rings) are forwarded to the ideal class.

            The keyword ``side`` can be one of ``'twosided'``,
            ``'left'``, ``'right'``. It determines whether
            the resulting ideal is twosided, a left ideal or a right ideal.

            EXAMPLES:

            Matrix rings::

                sage: # needs sage.modules
                sage: MS = MatrixSpace(QQ, 2, 2)
                sage: MS.ideal(2)
                Twosided Ideal
                (
                  [2 0]
                  [0 2]
                )
                 of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
                sage: MS.ideal([MS.0, MS.1], side='right')
                Right Ideal
                (
                  [1 0]
                  [0 0],
                <BLANKLINE>
                  [0 1]
                  [0 0]
                )
                 of Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            Polynomial rings::

                sage: R.<x,y> = QQ[]
                sage: R.ideal(x,y)
                Ideal (x, y) of Multivariate Polynomial Ring in x, y over Rational Field
                sage: R.ideal(x+y^2)
                Ideal (y^2 + x) of Multivariate Polynomial Ring in x, y over Rational Field
                sage: R.ideal( [x^3,y^3+x^3] )
                Ideal (x^3, x^3 + y^3) of Multivariate Polynomial Ring in x, y over Rational Field

            Non-commutative rings::

                sage: A = SteenrodAlgebra(2)                                                # needs sage.combinat sage.modules
                sage: A.ideal(A.1, A.2^2)                                                   # needs sage.combinat sage.modules
                Twosided Ideal (Sq(2), Sq(2,2)) of mod 2 Steenrod algebra, milnor basis
                sage: A.ideal(A.1, A.2^2, side='left')                                      # needs sage.combinat sage.modules
                Left Ideal (Sq(2), Sq(2,2)) of mod 2 Steenrod algebra, milnor basis

            TESTS:

            Make sure that :issue:`11139` is fixed::

                sage: R.<x> = QQ[]
                sage: R.ideal([])
                Principal ideal (0) of Univariate Polynomial Ring in x over Rational Field
                sage: R.ideal(())
                Principal ideal (0) of Univariate Polynomial Ring in x over Rational Field
                sage: R.ideal()
                Principal ideal (0) of Univariate Polynomial Ring in x over Rational Field

            Check ``ideal_class=`` keyword argument when input is empty::

                sage: from sage.rings.ideal import Ideal_pid
                sage: class CustomIdealClass(Ideal_pid):
                ....:     pass
                sage: type(ZZ.ideal(6))
                <class 'sage.rings.ideal.Ideal_pid'>
                sage: type(ZZ.ideal(6, ideal_class=CustomIdealClass))
                <class '...CustomIdealClass'>
                sage: type(ZZ.ideal())
                <class 'sage.rings.ideal.Ideal_pid'>
                sage: type(ZZ.ideal(ideal_class=CustomIdealClass))
                <class '...CustomIdealClass'>
                sage: type(ZZ.ideal((), ideal_class=CustomIdealClass))
                <class '...CustomIdealClass'>
            """
        def quotient(self, I, names=None, **kwds):
            """
            Quotient of a ring by a two-sided ideal.

            INPUT:

            - ``I`` -- a twosided ideal of this ring
            - ``names`` -- (optional) names of the generators of the quotient (if
              there are multiple generators, you can specify a single character
              string and the generators are named in sequence starting with 0).
            - further named arguments that may be passed to the
              quotient ring constructor.

            EXAMPLES:

            Usually, a ring inherits a method :meth:`sage.rings.ring.Ring.quotient`.
            So, we need a bit of effort to make the following example work with the
            category framework::

                sage: # needs sage.combinat sage.modules
                sage: F.<x,y,z> = FreeAlgebra(QQ)
                sage: from sage.rings.noncommutative_ideals import Ideal_nc
                sage: from itertools import product
                sage: class PowerIdeal(Ideal_nc):
                ....:  def __init__(self, R, n):
                ....:      self._power = n
                ....:      Ideal_nc.__init__(self, R, [R.prod(m)
                ....:                                  for m in product(R.gens(), repeat=n)])
                ....:  def reduce(self, x):
                ....:      R = self.ring()
                ....:      return add([c*R(m) for m, c in x
                ....:                  if len(m) < self._power], R(0))
                sage: I = PowerIdeal(F, 3)
                sage: Q = Rings().parent_class.quotient(F, I); Q
                Quotient of Free Algebra on 3 generators (x, y, z) over Rational Field
                 by the ideal (x^3, x^2*y, x^2*z, x*y*x, x*y^2, x*y*z, x*z*x,
                               x*z*y, x*z^2, y*x^2, y*x*y, y*x*z, y^2*x, y^3,
                               y^2*z, y*z*x, y*z*y, y*z^2, z*x^2, z*x*y, z*x*z,
                               z*y*x, z*y^2, z*y*z, z^2*x, z^2*y, z^3)
                sage: Q.0
                xbar
                sage: Q.1
                ybar
                sage: Q.2
                zbar
                sage: Q.0*Q.1
                xbar*ybar
                sage: Q.0*Q.1*Q.0
                0

            An example with polynomial rings::

                sage: R.<x> = PolynomialRing(ZZ)
                sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
                sage: S = R.quotient(I, 'a')
                sage: S.gens()
                (a,)

                sage: # needs sage.libs.singular
                sage: R.<x,y> = PolynomialRing(QQ, 2)
                sage: S.<a,b> = R.quotient((x^2, y))
                sage: S
                Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                 by the ideal (x^2, y)
                sage: S.gens()
                (a, 0)
                sage: a == b
                False
            """
        def quo(self, I, names=None, **kwds):
            """
            Quotient of a ring by a two-sided ideal.

            .. NOTE::

                This is a synonym for :meth:`quotient`.

            EXAMPLES::

                sage: MS = MatrixSpace(QQ, 2)                                           # needs sage.modules
                sage: I = MS * MS.gens() * MS                                           # needs sage.modules

            ``MS`` is not an instance of :class:`~sage.rings.ring.Ring`.

            However it is an instance of the parent class of the
            category of rings. The quotient method is inherited from
            there::

                sage: isinstance(MS, sage.rings.ring.Ring)                              # needs sage.modules
                False
                sage: isinstance(MS, Rings().parent_class)                              # needs sage.modules
                True
                sage: MS.quo(I, names=['a','b','c','d'])                                # needs sage.modules
                Quotient of Full MatrixSpace of 2 by 2 dense matrices
                 over Rational Field by the ideal
                (
                  [1 0]
                  [0 0],
                <BLANKLINE>
                  [0 1]
                  [0 0],
                <BLANKLINE>
                  [0 0]
                  [1 0],
                <BLANKLINE>
                  [0 0]
                  [0 1]
                )

            A test with a subclass of :class:`~sage.rings.ring.Ring`::

                sage: # needs sage.libs.singular
                sage: R.<x,y> = PolynomialRing(QQ, 2)
                sage: S.<a,b> = R.quo((x^2, y))
                sage: S
                Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                 by the ideal (x^2, y)
                sage: S.gens()
                (a, 0)
                sage: a == b
                False
            """
        def quotient_ring(self, I, names=None, **kwds):
            """
            Quotient of a ring by a two-sided ideal.

            .. NOTE::

                This is a synonym for :meth:`quotient`.

            INPUT:

            - ``I`` -- an ideal of `R`

            - ``names`` -- (optional) names of the generators of the quotient. (If
              there are multiple generators, you can specify a single character
              string and the generators are named in sequence starting with 0.)

            - further named arguments that may be passed to the quotient ring
              constructor.

            OUTPUT: ``R/I`` -- the quotient ring of `R` by the ideal `I`

            EXAMPLES::

                sage: MS = MatrixSpace(QQ, 2)                                           # needs sage.modules
                sage: I = MS * MS.gens() * MS                                           # needs sage.modules

            ``MS`` is not an instance of :class:`~sage.rings.ring.Ring`,
            but it is an instance of the parent class of the category of
            rings. The quotient method is inherited from there::

                sage: isinstance(MS, sage.rings.ring.Ring)                              # needs sage.modules
                False
                sage: isinstance(MS, Rings().parent_class)                              # needs sage.modules
                True
                sage: MS.quotient_ring(I, names=['a','b','c','d'])                      # needs sage.modules
                Quotient of Full MatrixSpace of 2 by 2 dense matrices
                 over Rational Field by the ideal
                (
                  [1 0]
                  [0 0],
                <BLANKLINE>
                  [0 1]
                  [0 0],
                <BLANKLINE>
                  [0 0]
                  [1 0],
                <BLANKLINE>
                  [0 0]
                  [0 1]
                )

            A test with a subclass of :class:`~sage.rings.ring.Ring`::

                sage: R.<x> = PolynomialRing(ZZ)
                sage: I = R.ideal([4 + 3*x + x^2, 1 + x^2])
                sage: S = R.quotient_ring(I, 'a')
                sage: S.gens()
                (a,)

                sage: # needs sage.libs.singular
                sage: R.<x,y> = PolynomialRing(QQ,2)
                sage: S.<a,b> = R.quotient_ring((x^2, y))
                sage: S
                Quotient of Multivariate Polynomial Ring in x, y over Rational Field
                 by the ideal (x^2, y)
                sage: S.gens()
                (a, 0)
                sage: a == b
                False
            """
        def __truediv__(self, I) -> None:
            """
            Since assigning generator names would not work properly,
            the construction of a quotient ring using division syntax
            is not supported.

            EXAMPLES::

                sage: MS = MatrixSpace(QQ, 2)                                           # needs sage.modules
                sage: I = MS * MS.gens() * MS                                           # needs sage.modules
                sage: MS/I                                                              # needs sage.modules
                Traceback (most recent call last):
                ...
                TypeError: use self.quotient(I) to construct the quotient ring

                sage: QQ['x'] / ZZ
                Traceback (most recent call last):
                ...
                TypeError: use self.quotient(I) to construct the quotient ring
            """
        def __getitem__(self, arg):
            """
            Extend this ring by one or several elements to create a polynomial
            ring, a power series ring, or an algebraic extension.

            This is a convenience method intended primarily for interactive
            use.

            .. SEEALSO::

                :func:`~sage.rings.polynomial.polynomial_ring_constructor.PolynomialRing`,
                :func:`~sage.rings.power_series_ring.PowerSeriesRing`,
                :meth:`~sage.rings.ring.Ring.extension`,
                :meth:`sage.rings.integer_ring.IntegerRing_class.__getitem__`,
                :meth:`sage.rings.matrix_space.MatrixSpace.__getitem__`,
                :meth:`sage.structure.parent.Parent.__getitem__`

            EXAMPLES:

            We create several polynomial rings::

                sage: ZZ['x']
                Univariate Polynomial Ring in x over Integer Ring
                sage: QQ['x']
                Univariate Polynomial Ring in x over Rational Field
                sage: GF(17)['abc']
                Univariate Polynomial Ring in abc over Finite Field of size 17
                sage: GF(17)['a,b,c']
                Multivariate Polynomial Ring in a, b, c over Finite Field of size 17
                sage: GF(17)['a']['b']
                Univariate Polynomial Ring in b over
                 Univariate Polynomial Ring in a over Finite Field of size 17

            We can create Ore polynomial rings::

                sage: k.<t> = GF(5^3)                                                   # needs sage.rings.finite_rings
                sage: Frob = k.frobenius_endomorphism()                                 # needs sage.rings.finite_rings
                sage: k['x', Frob]                                                      # needs sage.modules sage.rings.finite_rings
                Ore Polynomial Ring in x over Finite Field in t of size 5^3
                 twisted by t |--> t^5

                sage: R.<t> = QQ[]
                sage: der = R.derivation()                                              # needs sage.modules
                sage: R['d', der]                                                       # needs sage.modules
                Ore Polynomial Ring in d
                 over Univariate Polynomial Ring in t over Rational Field
                 twisted by d/dt

            We can also create power series rings by using double brackets::

                sage: QQ[['t']]
                Power Series Ring in t over Rational Field
                sage: ZZ[['W']]
                Power Series Ring in W over Integer Ring

                sage: ZZ[['x,y,z']]
                Multivariate Power Series Ring in x, y, z over Integer Ring
                sage: ZZ[['x','T']]
                Multivariate Power Series Ring in x, T over Integer Ring

            Use :func:`~sage.rings.fraction_field.Frac` or
            :meth:`~sage.rings.ring.CommutativeRing.fraction_field` to obtain
            the fields of rational functions and Laurent series::

                sage: Frac(QQ['t'])
                Fraction Field of Univariate Polynomial Ring in t over Rational Field
                sage: Frac(QQ[['t']])
                Laurent Series Ring in t over Rational Field
                sage: QQ[['t']].fraction_field()
                Laurent Series Ring in t over Rational Field

            Note that the same syntax can be used to create number fields::

                sage: QQ[I]                                                             # needs sage.rings.number_field sage.symbolic
                Number Field in I with defining polynomial x^2 + 1 with I = 1*I
                sage: QQ[I].coerce_embedding()                                          # needs sage.rings.number_field sage.symbolic
                Generic morphism:
                  From: Number Field in I with defining polynomial x^2 + 1 with I = 1*I
                  To:   Complex Lazy Field
                  Defn: I -> 1*I

            ::

                sage: QQ[sqrt(2)]                                                       # needs sage.rings.number_field sage.symbolic
                Number Field in sqrt2 with defining polynomial x^2 - 2
                 with sqrt2 = 1.414213562373095?
                sage: QQ[sqrt(2)].coerce_embedding()                                    # needs sage.rings.number_field sage.symbolic
                Generic morphism:
                  From: Number Field in sqrt2 with defining polynomial x^2 - 2
                        with sqrt2 = 1.414213562373095?
                  To:   Real Lazy Field
                  Defn: sqrt2 -> 1.414213562373095?

            ::

                sage: QQ[sqrt(2), sqrt(3)]                                              # needs sage.rings.number_field sage.symbolic
                Number Field in sqrt2
                 with defining polynomial x^2 - 2 over its base field

            and orders in number fields::

                sage: ZZ[I]                                                             # needs sage.rings.number_field sage.symbolic
                Gaussian Integers generated by I0 in Number Field in I0
                 with defining polynomial x^2 + 1 with I0 = 1*I
                sage: ZZ[sqrt(5)]                                                       # needs sage.rings.number_field sage.symbolic
                Order of conductor 2 generated by sqrt5 in Number Field in sqrt5
                 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?
                sage: ZZ[sqrt(2) + sqrt(3)]                                             # needs sage.rings.number_field sage.symbolic
                Order generated by a in Number Field in a
                 with defining polynomial x^4 - 10*x^2 + 1 with a = 3.146264369941973?

            Embeddings are found for simple extensions (when that makes sense)::

                sage: QQi.<i> = QuadraticField(-1, 'i')                                 # needs sage.rings.number_field sage.symbolic
                sage: QQ[i].coerce_embedding()                                          # needs sage.rings.number_field sage.symbolic
                Generic morphism:
                  From: Number Field in i with defining polynomial x^2 + 1 with i = 1*I
                  To:   Complex Lazy Field
                  Defn: i -> 1*I

            TESTS:

            A few corner cases::

                sage: QQ[()]
                Multivariate Polynomial Ring in no variables over Rational Field

                sage: QQ[[]]
                Traceback (most recent call last):
                ...
                TypeError: power series rings must have at least one variable

            These kind of expressions do not work::

                sage: QQ['a,b','c']
                Traceback (most recent call last):
                ...
                ValueError: variable name 'a,b' is not alphanumeric
                sage: QQ[['a,b','c']]
                Traceback (most recent call last):
                ...
                ValueError: variable name 'a,b' is not alphanumeric

                sage: QQ[[['x']]]
                Traceback (most recent call last):
                ...
                TypeError: expected R[...] or R[[...]], not R[[[...]]]

            Extension towers are built as follows and use distinct generator names::

                sage: # needs sage.rings.number_field sage.symbolic
                sage: K = QQ[2^(1/3), 2^(1/2), 3^(1/3)]
                sage: K
                Number Field in a with defining polynomial x^3 - 2
                 over its base field
                sage: K.base_field()
                Number Field in sqrt2 with defining polynomial x^2 - 2
                 over its base field
                sage: K.base_field().base_field()
                Number Field in b with defining polynomial x^3 - 3

            Embeddings::

                sage: # needs sage.rings.number_field sage.symbolic
                sage: a = 10^100; expr = (2*a + sqrt(2))/(2*a^2-1)
                sage: QQ[expr].coerce_embedding() is None
                False
                sage: QQ[sqrt(5)].gen() > 0
                True
                sage: expr = sqrt(2) + I*(cos(pi/4, hold=True) - sqrt(2)/2)
                sage: QQ[expr].coerce_embedding()
                Generic morphism:
                  From: Number Field in a with defining polynomial x^2 - 2
                        with a = 1.414213562373095?
                  To:   Real Lazy Field
                  Defn: a -> 1.414213562373095?
            """
        def free_module(self, base=None, basis=None, map: bool = True):
            """
            Return a free module `V` over the specified subring together with maps to and from `V`.

            The default implementation only supports the case that the base ring is the ring itself.

            INPUT:

            - ``base`` -- a subring `R` so that this ring is isomorphic
              to a finite-rank free `R`-module `V`

            - ``basis`` -- (optional) a basis for this ring over the base

            - ``map`` -- boolean (default: ``True``); whether to return
              `R`-linear maps to and from `V`

            OUTPUT: a finite-rank free `R`-module `V`

            - An `R`-module isomorphism from `V` to this ring
              (only included if ``map`` is ``True``)

            - An `R`-module isomorphism from this ring to `V`
              (only included if ``map`` is ``True``)

            EXAMPLES::

                sage: # needs sage.modules
                sage: R.<x> = QQ[[]]
                sage: V, from_V, to_V = R.free_module(R)
                sage: v = to_V(1 + x); v
                (1 + x)
                sage: from_V(v)
                1 + x
                sage: W, from_W, to_W = R.free_module(R, basis=(1 - x))
                sage: W is V
                True
                sage: w = to_W(1 + x); w
                (1 - x^2)
                sage: from_W(w)
                1 + x + O(x^20)
            """
        def random_element(self, *args):
            """
            Return a random integer coerced into this ring.

            INPUT:

            - either no integer, one integer or two integers

            The integer is chosen uniformly from the closed interval
            ``[-2,2]``, ``[-a,a]`` or ``[a,b]`` according to the
            length of the input.

            ALGORITHM:

            This uses Python's ``randint``.

            EXAMPLES::

                sage: -8 <= ZZ.random_element(8) <= 8
                True
                sage: -8 <= QQ.random_element(8) <= 8
                True
                sage: 4 <= ZZ.random_element(4,12) <= 12
                True
            """
        @cached_method
        def epsilon(self):
            """
            Return the precision error of elements in this ring.

            .. NOTE:: This is not used anywhere inside the code base.

            EXAMPLES::

                sage: RDF.epsilon()
                2.220446049250313e-16
                sage: ComplexField(53).epsilon()                                            # needs sage.rings.real_mpfr
                2.22044604925031e-16
                sage: RealField(10).epsilon()                                               # needs sage.rings.real_mpfr
                0.0020

            For exact rings, zero is returned::

                sage: ZZ.epsilon()
                0

            This also works over derived rings::

                sage: RR['x'].epsilon()                                                     # needs sage.rings.real_mpfr
                2.22044604925031e-16
                sage: QQ['x'].epsilon()
                0

            For the symbolic ring, there is no reasonable answer::

                sage: SR.epsilon()                                                          # needs sage.symbolic
                Traceback (most recent call last):
                ...
                NotImplementedError
            """
    class ElementMethods:
        def is_unit(self) -> bool:
            """
            Return whether this element is a unit in the ring.

            .. NOTE::

                This is a generic implementation for (non-commutative) rings
                which only works for the one element, its additive inverse, and
                the zero element. Most rings should provide a more specialized
                implementation.

            EXAMPLES::

                sage: # needs sage.modules
                sage: MS = MatrixSpace(ZZ, 2)
                sage: MS.one().is_unit()
                True
                sage: MS.zero().is_unit()
                False
                sage: MS([1,2,3,4]).is_unit()
                False
            """
        def inverse_of_unit(self):
            """
            Return the inverse of this element if it is a unit.

            OUTPUT: an element in the same ring as this element

            EXAMPLES::

                sage: R.<x> = ZZ[]
                sage: S = R.quo(x^2 + x + 1)                                            # needs sage.libs.pari
                sage: S(1).inverse_of_unit()                                            # needs sage.libs.pari
                1

            This method fails when the element is not a unit::

                sage: 2.inverse_of_unit()
                Traceback (most recent call last):
                ...
                ArithmeticError: inverse does not exist

            The inverse returned is in the same ring as this element::

                sage: a = -1
                sage: a.parent()
                Integer Ring
                sage: a.inverse_of_unit().parent()
                Integer Ring

            Note that this is often not the case when computing inverses in other ways::

                sage: (~a).parent()
                Rational Field
                sage: (1/a).parent()
                Rational Field
            """
