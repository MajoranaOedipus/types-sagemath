from _typeshed import Incomplete
from sage.categories.category_singleton import Category_contains_method_by_parent_class as Category_contains_method_by_parent_class
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.division_rings import DivisionRings as DivisionRings
from sage.categories.euclidean_domains import EuclideanDomains as EuclideanDomains
from sage.categories.noetherian_rings import NoetherianRings as NoetherianRings
from sage.misc.lazy_attribute import lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.structure.element import coerce_binop as coerce_binop

class Fields(CategoryWithAxiom):
    """
    The category of (commutative) fields, i.e. commutative rings where
    all nonzero elements have multiplicative inverses

    EXAMPLES::

        sage: K = Fields()
        sage: K
        Category of fields
        sage: Fields().super_categories()
        [Category of euclidean domains,
         Category of division rings,
         Category of noetherian rings]

        sage: K(IntegerRing())
        Rational Field
        sage: K(PolynomialRing(GF(3), 'x'))
        Fraction Field of Univariate Polynomial Ring in x over
        Finite Field of size 3
        sage: K(RealField())                                                            # needs sage.rings.real_mpfr
        Real Field with 53 bits of precision

    TESTS::

        sage: TestSuite(Fields()).run()
    """
    def extra_super_categories(self):
        """
        EXAMPLES::

            sage: Fields().extra_super_categories()
            [Category of euclidean domains, Category of noetherian rings]
        """
    def __contains__(self, x) -> bool:
        '''
        EXAMPLES::

            sage: GF(4, "a") in Fields()                                                # needs sage.rings.finite_rings
            True
            sage: QQ in Fields()
            True
            sage: ZZ in Fields()
            False
            sage: IntegerModRing(4) in Fields()
            False
            sage: InfinityRing in Fields()
            False

        This implementation will not be needed anymore once every
        field in Sage will be properly declared in the category
        :class:`Fields() <Fields>`.

        Caveat: this should eventually be fixed::

            sage: gap.Rationals in Fields()                                             # needs sage.libs.gap
            False

        typically by implementing the method :meth:`category`
        appropriately for Gap objects::

            sage: GR = gap.Rationals                                                    # needs sage.libs.gap
            sage: GR.category = lambda: Fields()                                        # needs sage.libs.gap
            sage: GR in Fields()                                                        # needs sage.libs.gap
            True

        The following tests against a memory leak fixed in :issue:`13370`. In order
        to prevent non-deterministic deallocation of fields that have been created
        in other doctests, we introduced a strong reference to all previously created
        uncollected objects in :issue:`19244`. ::

            sage: # needs sage.libs.pari
            sage: import gc
            sage: _ = gc.collect()
            sage: permstore = [X for X in gc.get_objects()
            ....:              if isinstance(X, sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic)]
            sage: n = len(permstore)
            sage: for i in prime_range(100):
            ....:     R = ZZ.quotient(i)
            ....:     t = R in Fields()

        First, we show that there are now more quotient rings in cache than before::

            sage: # needs sage.libs.pari
            sage: len([X for X in gc.get_objects()
            ....:      if isinstance(X, sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic)]) > n
            True

        When we delete the last quotient ring created in the loop and then do a garbage
        collection, all newly created rings vanish::

            sage: # needs sage.libs.pari
            sage: del R
            sage: _ = gc.collect()
            sage: len([X for X in gc.get_objects()
            ....:      if isinstance(X, sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic)]) - n
            0
        '''
    Finite: Incomplete
    class ParentMethods:
        def krull_dimension(self):
            """
            Return the Krull dimension of this field, which is 0.

            EXAMPLES::

                sage: QQ.krull_dimension()
                0
                sage: Frac(QQ['x,y']).krull_dimension()
                0
            """
        def is_field(self, proof: bool = True):
            """
            Return ``True`` as ``self`` is a field.

            EXAMPLES::

                sage: QQ.is_field()
                True
                sage: Parent(QQ,category=Fields()).is_field()
                True

                sage: Frac(ZZ['x,y']).is_field()
                True
            """
        def is_integrally_closed(self) -> bool:
            """
            Return whether ``self`` is integrally closed.

            For every field `F`, `F` is its own field of fractions.
            Therefore every element of `F` is integral over `F`.

            EXAMPLES::

                sage: QQ.is_integrally_closed()
                True
                sage: QQbar.is_integrally_closed()                                      # needs sage.rings.number_field
                True
                sage: Z5 = GF(5); Z5
                Finite Field of size 5
                sage: Z5.is_integrally_closed()
                True
                sage: Frac(ZZ['x,y']).is_integrally_closed()
                True
            """
        def integral_closure(self):
            """
            Return this field, since fields are integrally closed in their
            fraction field.

            EXAMPLES::

                sage: QQ.integral_closure()
                Rational Field
                sage: Frac(ZZ['x,y']).integral_closure()
                Fraction Field of Multivariate Polynomial Ring in x, y
                over Integer Ring
            """
        def algebraic_closure(self) -> None:
            """
            Return the algebraic closure of ``self``.

            .. NOTE::

               This is only implemented for certain classes of field.

            EXAMPLES::

                sage: K = PolynomialRing(QQ,'x').fraction_field(); K
                Fraction Field of Univariate Polynomial Ring in x over Rational Field
                sage: K.algebraic_closure()
                Traceback (most recent call last):
                ...
                NotImplementedError: algebraic closures of general fields not implemented
            """
        def an_embedding(self, K):
            """
            Return some embedding of this field into another field `K`,
            and raise a :class:`ValueError` if none exists.

            EXAMPLES::

                sage: GF(2).an_embedding(GF(4))
                Ring morphism:
                  From: Finite Field of size 2
                  To:   Finite Field in z2 of size 2^2
                  Defn: 1 |--> 1
                sage: GF(4).an_embedding(GF(8))
                Traceback (most recent call last):
                ...
                ValueError: no embedding from Finite Field in z2 of size 2^2 to Finite Field in z3 of size 2^3
                sage: GF(4).an_embedding(GF(16))
                Ring morphism:
                  From: Finite Field in z2 of size 2^2
                  To:   Finite Field in z4 of size 2^4
                  Defn: z2 |--> z4^2 + z4

            ::

                sage: CyclotomicField(5).an_embedding(QQbar)
                Coercion map:
                  From: Cyclotomic Field of order 5 and degree 4
                  To:   Algebraic Field
                sage: CyclotomicField(3).an_embedding(CyclotomicField(7))
                Traceback (most recent call last):
                ...
                ValueError: no embedding from Cyclotomic Field of order 3 and degree 2 to Cyclotomic Field of order 7 and degree 6
                sage: CyclotomicField(3).an_embedding(CyclotomicField(6))
                Generic morphism:
                  From: Cyclotomic Field of order 3 and degree 2
                  To:   Cyclotomic Field of order 6 and degree 2
                  Defn: zeta3 -> zeta6 - 1
            """
        def prime_subfield(self):
            """
            Return the prime subfield of ``self``.

            EXAMPLES::

                sage: k = GF(9, 'a')                                                        # needs sage.rings.finite_rings
                sage: k.prime_subfield()                                                    # needs sage.rings.finite_rings
                Finite Field of size 3
            """
        def divides(self, x, y, coerce: bool = True):
            """
            Return ``True`` if ``x`` divides ``y`` in this field.

            This is usually ``True`` in a field!.

            If ``coerce`` is ``True`` (the default), first coerce
            ``x`` and ``y`` into ``self``.

            EXAMPLES::

                sage: QQ.divides(2, 3/4)
                True
                sage: QQ.divides(0, 5)
                False
            """
        def is_perfect(self):
            """
            Return whether this field is perfect, i.e., its characteristic is
            `p=0` or every element has a `p`-th root.

            EXAMPLES::

                sage: QQ.is_perfect()
                True
                sage: GF(2).is_perfect()
                True
                sage: FunctionField(GF(2), 'x').is_perfect()
                False
            """
        def fraction_field(self):
            """
            Return the *fraction field* of ``self``, which is ``self``.

            EXAMPLES:

            Since fields are their own field of fractions, we simply get the
            original field in return::

                sage: QQ.fraction_field()
                Rational Field
                sage: RR.fraction_field()                                                   # needs sage.rings.real_mpfr
                Real Field with 53 bits of precision
                sage: CC.fraction_field()                                                   # needs sage.rings.real_mpfr
                Complex Field with 53 bits of precision

                sage: x = polygen(ZZ, 'x')
                sage: F = NumberField(x^2 + 1, 'i')                                         # needs sage.rings.number_field
                sage: F.fraction_field()                                                    # needs sage.rings.number_field
                Number Field in i with defining polynomial x^2 + 1
            """
        def ideal(self, *gens, **kwds):
            """
            Return the ideal generated by ``gens``.

            INPUT:

            - an element or a list/tuple/sequence of elements, the generators

            Any named arguments are ignored.

            EXAMPLES::

                sage: QQ.ideal(2)
                Principal ideal (1) of Rational Field
                sage: QQ.ideal(0)
                Principal ideal (0) of Rational Field

            TESTS::

                sage: QQ.ideal(2, 4)
                Principal ideal (1) of Rational Field

                sage: QQ.ideal([2, 4])
                Principal ideal (1) of Rational Field
            """
        def vector_space(self, *args, **kwds):
            """
            Give an isomorphism of this field with a vector space over a subfield.

            This method is an alias for ``free_module``, which may have more documentation.

            INPUT:

            - ``base`` -- a subfield or morphism into this field (defaults to the base field)

            - ``basis`` -- a basis of the field as a vector space
              over the subfield; if not given, one is chosen automatically

            - ``map`` -- whether to return maps from and to the vector space

            OUTPUT:

            - ``V`` -- a vector space over ``base``
            - ``from_V`` -- an isomorphism from ``V`` to this field
            - ``to_V`` -- the inverse isomorphism from this field to ``V``

            EXAMPLES::

                sage: # needs sage.rings.padics
                sage: K.<a> = Qq(125)
                sage: V, fr, to = K.vector_space()
                sage: v = V([1, 2, 3])
                sage: fr(v, 7)
                (3*a^2 + 2*a + 1) + O(5^7)
            """
    class ElementMethods:
        def euclidean_degree(self):
            """
            Return the degree of this element as an element of a Euclidean
            domain.

            In a field, this returns 0 for all but the zero element (for
            which it is undefined).

            EXAMPLES::

                sage: QQ.one().euclidean_degree()
                0
            """
        def quo_rem(self, other):
            """
            Return the quotient with remainder of the division of this element
            by ``other``.

            INPUT:

            - ``other`` -- an element of the field

            EXAMPLES::

                sage: f,g = QQ(1), QQ(2)
                sage: f.quo_rem(g)
                (1/2, 0)
            """
        def is_unit(self):
            """
            Return ``True`` if ``self`` has a multiplicative inverse.

            EXAMPLES::

                sage: QQ(2).is_unit()
                True
                sage: QQ(0).is_unit()
                False
            """
        @coerce_binop
        def gcd(self, other):
            """
            Greatest common divisor.

            .. NOTE::

                Since we are in a field and the greatest common divisor is only
                determined up to a unit, it is correct to either return zero or
                one. Note that fraction fields of unique factorization domains
                provide a more sophisticated gcd.

            EXAMPLES::

                sage: K = GF(5)
                sage: K(2).gcd(K(1))
                1
                sage: K(0).gcd(K(0))
                0
                sage: all(x.gcd(y) == (0 if x == 0 and y == 0 else 1)
                ....:     for x in K for y in K)
                True

            For field of characteristic zero, the gcd of integers is considered
            as if they were elements of the integer ring::

                sage: gcd(15.0,12.0)                                                    # needs sage.rings.real_mpfr
                3.00000000000000

            But for other floating point numbers, the gcd is just `0.0` or `1.0`::

                sage: gcd(3.2, 2.18)                                                    # needs sage.rings.real_mpfr
                1.00000000000000

                sage: gcd(0.0, 0.0)                                                     # needs sage.rings.real_mpfr
                0.000000000000000

            TESTS::

                sage: QQbar(0).gcd(QQbar.zeta(3))
                1

            AUTHOR:

            - Simon King (2011-02) -- :issue:`10771`
            - Vincent Delecroix (2015) -- :issue:`17671`
            """
        @coerce_binop
        def lcm(self, other):
            """
            Least common multiple.

            .. NOTE::

                Since we are in a field and the least common multiple is only
                determined up to a unit, it is correct to either return zero or
                one. Note that fraction fields of unique factorization domains
                provide a more sophisticated lcm.

            EXAMPLES::

                sage: GF(2)(1).lcm(GF(2)(0))
                0
                sage: GF(2)(1).lcm(GF(2)(1))
                1

            For field of characteristic zero, the lcm of integers is considered
            as if they were elements of the integer ring::

                sage: lcm(15.0, 12.0)                                                   # needs sage.rings.real_mpfr
                60.0000000000000

            But for others floating point numbers, it is just `0.0` or `1.0`::

                sage: lcm(3.2, 2.18)                                                    # needs sage.rings.real_mpfr
                1.00000000000000

                sage: lcm(0.0, 0.0)                                                     # needs sage.rings.real_mpfr
                0.000000000000000

            AUTHOR:

            - Simon King (2011-02) -- :issue:`10771`
            - Vincent Delecroix (2015) -- :issue:`17671`
            """
        @coerce_binop
        def xgcd(self, other):
            """
            Compute the extended gcd of ``self`` and ``other``.

            INPUT:

            - ``other`` -- an element with the same parent as ``self``

            OUTPUT:

            A tuple ``(r, s, t)`` of elements in the parent of ``self`` such
            that ``r = s * self + t * other``. Since the computations are done
            over a field, ``r`` is zero if ``self`` and ``other`` are zero,
            and one otherwise.

            AUTHORS:

            - Julian Rueth (2012-10-19): moved here from
              :class:`sage.structure.element.FieldElement`

            EXAMPLES::

                sage: K = GF(5)
                sage: K(2).xgcd(K(1))
                (1, 3, 0)
                sage: K(0).xgcd(K(4))
                (1, 0, 4)
                sage: K(1).xgcd(K(1))
                (1, 1, 0)
                sage: GF(5)(0).xgcd(GF(5)(0))
                (0, 0, 0)

            The xgcd of nonzero floating point numbers will be a triple of
            floating points. But if the input are two integral floating points
            the result is a floating point version of the standard gcd on
            `\\ZZ`::

                sage: xgcd(12.0, 8.0)                                                   # needs sage.rings.real_mpfr
                (4.00000000000000, 1.00000000000000, -1.00000000000000)

                sage: xgcd(3.1, 2.98714)                                                # needs sage.rings.real_mpfr
                (1.00000000000000, 0.322580645161290, 0.000000000000000)

                sage: xgcd(0.0, 1.1)                                                    # needs sage.rings.real_mpfr
                (1.00000000000000, 0.000000000000000, 0.909090909090909)
            """
        def factor(self):
            """
            Return a factorization of ``self``.

            Since ``self`` is either a unit or zero, this function is trivial.

            EXAMPLES::

                sage: x = GF(7)(5)
                sage: x.factor()
                5
                sage: RR(0).factor()                                                    # needs sage.rings.real_mpfr
                Traceback (most recent call last):
                ...
                ArithmeticError: factorization of 0.000000000000000 is not defined
            """
        def inverse_of_unit(self):
            """
            Return the inverse of this element.

            EXAMPLES::

                sage: x = polygen(ZZ, 'x')
                sage: NumberField(x^7 + 2, 'a')(2).inverse_of_unit()                    # needs sage.rings.number_field
                1/2

            Trying to invert the zero element typically raises a
            :exc:`ZeroDivisionError`::

                sage: QQ(0).inverse_of_unit()
                Traceback (most recent call last):
                ...
                ZeroDivisionError: rational division by zero

            To catch that exception in a way that also works for non-units
            in more general rings, use something like::

                sage: try:
                ....:    QQ(0).inverse_of_unit()
                ....: except ArithmeticError:
                ....:    pass

            Also note that some “fields” allow one to invert the zero element::

                sage: RR(0).inverse_of_unit()
                +infinity
            """
