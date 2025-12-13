from _typeshed import Incomplete
from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.realizations import RealizationsCategory as RealizationsCategory
from sage.categories.sets_cat import Sets as Sets
from sage.categories.subquotients import SubquotientsCategory as SubquotientsCategory
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.misc.abstract_method import AbstractMethod as AbstractMethod, abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class Magmas(Category_singleton):
    """
    The category of (multiplicative) magmas.

    A magma is a set with a binary operation `*`.

    EXAMPLES::

        sage: Magmas()
        Category of magmas
        sage: Magmas().super_categories()
        [Category of sets]
        sage: Magmas().all_super_categories()
        [Category of magmas, Category of sets,
         Category of sets with partial maps, Category of objects]

    The following axioms are defined by this category::

        sage: Magmas().Associative()
        Category of semigroups
        sage: Magmas().Unital()
        Category of unital magmas
        sage: Magmas().Commutative()
        Category of commutative magmas
        sage: Magmas().Unital().Inverse()
        Category of inverse unital magmas
        sage: Magmas().Associative()
        Category of semigroups
        sage: Magmas().Associative().Unital()
        Category of monoids
        sage: Magmas().Associative().Unital().Inverse()
        Category of groups

    TESTS::

        sage: C = Magmas()
        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Magmas().super_categories()
            [Category of sets]
        """
    class SubcategoryMethods:
        @cached_method
        def Associative(self):
            """
            Return the full subcategory of the associative objects
            of ``self``.

            A (multiplicative) :class:`magma Magmas` `M` is
            *associative* if, for all `x,y,z\\in M`,

            .. MATH:: x * (y * z) = (x * y) * z

            .. SEEALSO:: :wikipedia:`Associative_property`

            EXAMPLES::

                sage: Magmas().Associative()
                Category of semigroups

            TESTS::

                sage: TestSuite(Magmas().Associative()).run()
                sage: Rings().Associative.__module__
                'sage.categories.magmas'
            """
        @cached_method
        def Commutative(self):
            """
            Return the full subcategory of the commutative objects
            of ``self``.

            A (multiplicative) :class:`magma Magmas` `M` is
            *commutative* if, for all `x,y\\in M`,

            .. MATH:: x * y = y * x

            .. SEEALSO:: :wikipedia:`Commutative_property`

            EXAMPLES::

                sage: Magmas().Commutative()
                Category of commutative magmas
                sage: Monoids().Commutative()
                Category of commutative monoids

            TESTS::

                sage: TestSuite(Magmas().Commutative()).run()
                sage: Rings().Commutative.__module__
                'sage.categories.magmas'
            """
        @cached_method
        def Unital(self):
            """
            Return the subcategory of the unital objects of ``self``.

            A (multiplicative) :class:`magma Magmas` `M` is *unital*
            if it admits an element `1`, called *unit*, such that for
            all `x\\in M`,

            .. MATH:: 1 * x = x * 1 = x

            This element is necessarily unique, and should be provided
            as ``M.one()``.

            .. SEEALSO:: :wikipedia:`Unital_magma#unital`

            EXAMPLES::

                sage: Magmas().Unital()
                Category of unital magmas
                sage: Semigroups().Unital()
                Category of monoids
                sage: Monoids().Unital()
                Category of monoids
                sage: from sage.categories.associative_algebras import AssociativeAlgebras
                sage: AssociativeAlgebras(QQ).Unital()
                Category of algebras over Rational Field

            TESTS::

                sage: TestSuite(Magmas().Unital()).run()
                sage: Semigroups().Unital.__module__
                'sage.categories.magmas'
            """
        @cached_method
        def FinitelyGeneratedAsMagma(self):
            """
            Return the subcategory of the objects of ``self`` that are
            endowed with a distinguished finite set of
            (multiplicative) magma generators.

            A set `S` of elements of a multiplicative magma form a
            *set of generators* if any element of the magma can be
            expressed recursively from elements of `S` and products
            thereof.

            It is not imposed that morphisms shall preserve the
            distinguished set of generators; hence this is a full
            subcategory.

            .. SEEALSO:: :wikipedia:`Unital_magma#unital`

            EXAMPLES::

                sage: Magmas().FinitelyGeneratedAsMagma()
                Category of finitely generated magmas

            Being finitely generated does depend on the structure: for
            a ring, being finitely generated as a magma, as an
            additive magma, or as a ring are different concepts. Hence
            the name of this axiom is explicit::

                sage: Rings().FinitelyGeneratedAsMagma()
                Category of finitely generated as magma enumerated rings

            On the other hand, it does not depend on the
            multiplicative structure: for example a group is finitely
            generated if and only if it is finitely generated as a
            magma. A short hand is provided when there is no
            ambiguity, and the output tries to reflect that::

                sage: Semigroups().FinitelyGenerated()
                Category of finitely generated semigroups
                sage: Groups().FinitelyGenerated()
                Category of finitely generated enumerated groups

                sage: Semigroups().FinitelyGenerated().axioms()
                frozenset({'Associative', 'Enumerated', 'FinitelyGeneratedAsMagma'})

            Note that the set of generators may depend on the actual
            category; for example, in a group, one can often use less
            generators since it is allowed to take inverses.

            TESTS::

                sage: TestSuite(Magmas().FinitelyGeneratedAsMagma()).run()
                sage: Semigroups().FinitelyGeneratedAsMagma.__module__
                'sage.categories.magmas'
            """
        @cached_method
        def FinitelyGenerated(self):
            '''
            Return the subcategory of the objects of ``self`` that are
            endowed with a distinguished finite set of
            (multiplicative) magma generators.

            EXAMPLES:

            This is a shorthand for :meth:`FinitelyGeneratedAsMagma`,
            which see::

                sage: Magmas().FinitelyGenerated()
                Category of finitely generated magmas
                sage: Semigroups().FinitelyGenerated()
                Category of finitely generated semigroups
                sage: Groups().FinitelyGenerated()
                Category of finitely generated enumerated groups

            An error is raised if this is ambiguous::

                sage: (Magmas() & AdditiveMagmas()).FinitelyGenerated()
                Traceback (most recent call last):
                ...
                ValueError: FinitelyGenerated is ambiguous for
                Join of Category of magmas and Category of additive magmas.
                Please use explicitly one of the FinitelyGeneratedAsXXX methods

            .. NOTE::

                Checking that there is no ambiguity currently assumes
                that all the other "finitely generated" axioms involve
                an additive structure. As of Sage 6.4, this is
                correct.

                The use of this shorthand should be reserved for casual
                interactive use or when there is no risk of ambiguity.
            '''
        @cached_method
        def Distributive(self):
            """
            Return the full subcategory of the objects of ``self``
            where `*` is distributive on `+`.

            INPUT:

            - ``self`` -- a subcategory of :class:`Magmas`
              and :class:`AdditiveMagmas`

            Given that Sage does not yet know that the category
            :class:`MagmasAndAdditiveMagmas` is the intersection of
            the categories :class:`Magmas` and
            :class:`AdditiveMagmas`, the method
            :meth:`MagmasAndAdditiveMagmas.SubcategoryMethods.Distributive`
            is not available, as would be desirable, for this intersection.

            This method is a workaround. It checks that ``self`` is a
            subcategory of both :class:`Magmas` and
            :class:`AdditiveMagmas` and upgrades it to a subcategory
            of :class:`MagmasAndAdditiveMagmas` before applying the
            axiom. It complains otherwise, since the ``Distributive``
            axiom does not make sense for a plain magma.

            EXAMPLES::

                sage: (Magmas() & AdditiveMagmas()).Distributive()
                Category of distributive magmas and additive magmas
                sage: (Monoids() & CommutativeAdditiveGroups()).Distributive()
                Category of rings

                sage: Magmas().Distributive()
                Traceback (most recent call last):
                ...
                ValueError: The distributive axiom only makes sense on a magma
                which is simultaneously an additive magma
                sage: Semigroups().Distributive()
                Traceback (most recent call last):
                ...
                ValueError: The distributive axiom only makes sense on a magma
                which is simultaneously an additive magma

            TESTS::

                sage: Semigroups().Distributive.__module__
                'sage.categories.magmas'
                sage: Rings().Distributive.__module__
                'sage.categories.magmas_and_additive_magmas'
            """
        def JTrivial(self):
            """
            Return the full subcategory of the `J`-trivial objects of ``self``.

            This axiom is in fact only meaningful for
            :class:`semigroups <Semigroups>`. This stub definition is
            here as a workaround for :issue:`20515`, in order to define
            the `J`-trivial axiom as the intersection of the `L` and
            `R`-trivial axioms.

            .. SEEALSO:: :meth:`Semigroups.SubcategoryMethods.JTrivial`

            TESTS::

                sage: Magmas().JTrivial()
                Category of j trivial magmas
                sage: C = Semigroups().RTrivial() & Semigroups().LTrivial()
                sage: C is Semigroups().JTrivial()
                True
            """
    Associative: Incomplete
    FinitelyGeneratedAsMagma: Incomplete
    class JTrivial(CategoryWithAxiom): ...
    class Algebras(AlgebrasCategory):
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: MCA = Magmas().Commutative().Algebras(QQ)
                sage: MCA.extra_super_categories()
                [Category of commutative magmas]

            This implements the fact that the algebra of a commutative
            magma is commutative::

                sage: MCA.super_categories()
                [Category of magma algebras over Rational Field,
                 Category of commutative magmas]

            In particular, commutative monoid algebras are
            commutative algebras::

                sage: MoCA = Monoids().Commutative().Algebras(QQ)
                sage: MoCA.is_subcategory(Algebras(QQ).Commutative())
                True
            """
        class ParentMethods:
            def is_field(self, proof: bool = True):
                """
                Return ``True`` if ``self`` is a field.

                For a magma algebra `R S` this is always false unless
                `S` is trivial and the base ring `R` is a field.

                EXAMPLES::

                    sage: SymmetricGroup(1).algebra(QQ).is_field()                      # needs sage.combinat sage.groups
                    True
                    sage: SymmetricGroup(1).algebra(ZZ).is_field()                      # needs sage.combinat sage.groups
                    False
                    sage: SymmetricGroup(2).algebra(QQ).is_field()                      # needs sage.combinat sage.groups
                    False
                    sage: Magmas().example().algebra(QQ).is_field()
                    False

                """
    class Commutative(CategoryWithAxiom):
        class ParentMethods:
            def is_commutative(self) -> bool:
                """
                Return ``True``, since commutative magmas are commutative.

                EXAMPLES::

                    sage: Parent(QQ, category=CommutativeRings()).is_commutative()
                    True
                """
        class Algebras(AlgebrasCategory):
            def extra_super_categories(self):
                """
                EXAMPLES::

                    sage: MCA = Magmas().Commutative().Algebras(QQ)
                    sage: MCA.extra_super_categories()
                    [Category of commutative magmas]

                This implements the fact that the algebra of a commutative
                magma is commutative::

                    sage: MCA.super_categories()
                    [Category of magma algebras over Rational Field,
                     Category of commutative magmas]

                In particular, commutative monoid algebras are
                commutative algebras::

                    sage: MoCA = Monoids().Commutative().Algebras(QQ)
                    sage: MoCA.is_subcategory(Algebras(QQ).Commutative())
                    True
                """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a Cartesian product of commutative
                additive magmas is still a commutative additive magmas.

                EXAMPLES::

                    sage: C = Magmas().Commutative().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of commutative magmas]
                    sage: C.axioms()
                    frozenset({'Commutative'})
                """
    class Unital(CategoryWithAxiom):
        def additional_structure(self):
            """
            Return ``self``.

            Indeed, the category of unital magmas defines an
            additional structure, namely the unit of the magma which
            shall be preserved by morphisms.

            .. SEEALSO:: :meth:`Category.additional_structure`

            EXAMPLES::

                sage: Magmas().Unital().additional_structure()
                Category of unital magmas
            """
        class ParentMethods:
            @cached_method
            def one(self):
                """
                Return the unit of the monoid, that is the unique neutral
                element for `*`.

                .. NOTE::

                   The default implementation is to coerce `1` into ``self``.
                   It is recommended to override this method because the
                   coercion from the integers:

                    - is not always meaningful (except for `1`);
                    - often uses ``self.one()``.

                EXAMPLES::

                    sage: M = Monoids().example(); M
                    An example of a monoid:
                     the free monoid generated by ('a', 'b', 'c', 'd')
                    sage: M.one()
                    ''
                """
            def is_empty(self):
                """
                Return whether ``self`` is empty.

                Since this set is a unital magma it is not empty and this method
                always return ``False``.

                EXAMPLES::

                    sage: S = SymmetricGroup(2)                                         # needs sage.groups
                    sage: S.is_empty()                                                  # needs sage.groups
                    False

                    sage: M = Monoids().example()
                    sage: M.is_empty()
                    False

                TESTS::

                    sage: S.is_empty.__module__                                         # needs sage.groups
                    'sage.categories.magmas'
                    sage: M.is_empty.__module__
                    'sage.categories.magmas'
                """
        class ElementMethods: ...
        class SubcategoryMethods:
            @cached_method
            def Inverse(self):
                """
                Return the full subcategory of the inverse objects of ``self``.

                An inverse :class:` (multiplicative) magma <Magmas>`
                is a :class:`unital magma <Magmas.Unital>` such that
                every element admits both an inverse on the left and
                on the right. Such a magma is also called a *loop*.

                .. SEEALSO::

                    :wikipedia:`Inverse_element`, :wikipedia:`Quasigroup`

                EXAMPLES::

                    sage: Magmas().Unital().Inverse()
                    Category of inverse unital magmas
                    sage: Monoids().Inverse()
                    Category of groups

                TESTS::

                    sage: TestSuite(Magmas().Unital().Inverse()).run()
                    sage: Algebras(QQ).Inverse.__module__
                    'sage.categories.magmas'
                """
        class Inverse(CategoryWithAxiom):
            class CartesianProducts(CartesianProductsCategory):
                def extra_super_categories(self):
                    """
                    Implement the fact that a Cartesian product of magmas with
                    inverses is a magma with inverse.

                    EXAMPLES::

                        sage: C = Magmas().Unital().Inverse().CartesianProducts()
                        sage: C.extra_super_categories()
                        [Category of inverse unital magmas]
                        sage: sorted(C.axioms())
                        ['Inverse', 'Unital']
                    """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a Cartesian product of unital magmas is
                a unital magma

                EXAMPLES::

                    sage: C = Magmas().Unital().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of unital magmas]
                    sage: C.axioms()
                    frozenset({'Unital'})

                    sage: Monoids().CartesianProducts().is_subcategory(Monoids())
                    True
                """
            class ParentMethods:
                @cached_method
                def one(self):
                    """
                    Return the unit of this Cartesian product.

                    It is built from the units for the Cartesian factors of ``self``.

                    EXAMPLES::

                        sage: cartesian_product([QQ, ZZ, RR]).one()                     # needs sage.rings.real_mpfr
                        (1, 1, 1.00000000000000)
                    """
            class ElementMethods:
                def __invert__(self):
                    """
                    Return the inverse of ``self``, if it exists.

                    The inverse is computed by inverting each
                    Cartesian factor and attempting to convert the
                    result back to the original parent.

                    For example, if one of the Cartesian factor is an
                    element ``x`` of `\\ZZ`, the result of ``~x`` is in
                    `\\QQ`. So we need to convert it back to `\\ZZ`. As
                    a side effect, this checks that ``x`` is indeed
                    invertible in `\\ZZ`.

                    If needed an optimized version without this
                    conversion could be implemented in
                    :class:`Magmas.Unital.Inverse.ElementMethods`.

                    EXAMPLES::

                        sage: C = cartesian_product([QQ, ZZ, RR, GF(5)])
                        sage: c = C([2,-1,2,2]); c                                      # needs sage.rings.real_mpfr
                        (2, -1, 2.00000000000000, 2)
                        sage: ~c                                                        # needs sage.rings.real_mpfr
                        (1/2, -1, 0.500000000000000, 3)

                    This fails as soon as one of the entries is not
                    invertible::

                        sage: ~C([0,2,2,2])
                        Traceback (most recent call last):
                        ...
                        ZeroDivisionError: rational division by zero

                        sage: ~C([2,2,2,2])                                             # needs sage.rings.real_mpfr
                        (1/2, 1/2, 0.500000000000000, 3)
                    """
        class Algebras(AlgebrasCategory):
            def extra_super_categories(self):
                """
                EXAMPLES::

                    sage: MCA = Magmas().Commutative().Algebras(QQ)
                    sage: MCA.extra_super_categories()
                    [Category of commutative magmas]

                This implements the fact that the algebra of a
                commutative magma is commutative::

                    sage: MCA.super_categories()
                    [Category of magma algebras over Rational Field,
                     Category of commutative magmas]

                In particular, commutative monoid algebras are
                commutative algebras::

                    sage: MoCA = Monoids().Commutative().Algebras(QQ)
                    sage: MoCA.is_subcategory(Algebras(QQ).Commutative())
                    True
                """
        class Realizations(RealizationsCategory):
            class ParentMethods:
                @cached_method
                def one(self):
                    """
                    Return the unit element of ``self``.

                    EXAMPLES::

                        sage: # needs sage.combinat sage.groups
                        sage: from sage.combinat.root_system.extended_affine_weyl_group import ExtendedAffineWeylGroup
                        sage: PvW0 = ExtendedAffineWeylGroup(['A',2,1]).PvW0()
                        sage: PvW0 in Magmas().Unital().Realizations()
                        True
                        sage: PvW0.one()
                        1
                    """
    class ParentMethods:
        def product(self, x, y):
            '''
            The binary multiplication of the magma.

            INPUT:

            - ``x``, ``y`` -- elements of this magma

            OUTPUT:

            - an element of the magma (the product of ``x`` and ``y``)

            EXAMPLES::

                sage: S = Semigroups().example("free")
                sage: x = S(\'a\'); y = S(\'b\')
                sage: S.product(x, y)
                \'ab\'

            A parent in ``Magmas()`` must either implement
            :meth:`.product` in the parent class or ``_mul_`` in the
            element class. By default, the addition method on elements
            ``x._mul_(y)`` calls ``S.product(x,y)``, and reciprocally.

            As a bonus, ``S.product`` models the binary function from
            ``S`` to ``S``::

                sage: bin = S.product
                sage: bin(x,y)
                \'ab\'

            Currently, ``S.product`` is just a bound method::

                sage: bin
                <bound method FreeSemigroup.product of An example of a semigroup:
                 the free semigroup generated by (\'a\', \'b\', \'c\', \'d\')>

            When Sage will support multivariate morphisms, it will be
            possible, and in fact recommended, to enrich ``S.product``
            with extra mathematical structure. This will typically be
            implemented using lazy attributes.::

                sage: bin                 # todo: not implemented
                Generic binary morphism:
                From: (S x S)
                To:   S
            '''
        product_from_element_class_mul = product
        def __init_extra__(self) -> None:
            '''
            EXAMPLES::

                sage: S = Semigroups().example("free")
                sage: S(\'a\') * S(\'b\') # indirect doctest
                \'ab\'
                sage: S(\'a\').__class__._mul_ == S(\'a\').__class__._mul_parent
                True
            '''
        def multiplication_table(self, names: str = 'letters', elements=None):
            """
            Return a table describing the multiplication operation.

            .. NOTE:: The order of the elements in the row and column
              headings is equal to the order given by the table's
              :meth:`~sage.matrix.operation_table.OperationTable.list`
              method.  The association can also be retrieved with the
              :meth:`~sage.matrix.operation_table.OperationTable.dict`
              method.

            INPUT:

            - ``names`` -- the type of names used

              * ``'letters'`` -- lowercase ASCII letters are used
                for a base 26 representation of the elements'
                positions in the list given by
                :meth:`~sage.matrix.operation_table.OperationTable.column_keys`,
                padded to a common width with leading 'a's.
              * ``'digits'`` -- base 10 representation of the
                elements' positions in the list given by
                :meth:`~sage.matrix.operation_table.OperationTable.column_keys`,
                padded to a common width with leading zeros.
              * ``'elements'`` -- the string representations
                of the elements themselves.
              * a list - a list of strings, where the length
                of the list equals the number of elements.
            - ``elements`` -- (default: ``None``) a list of
              elements of the magma, in forms that can be
              coerced into the structure, eg. their string
              representations. This may be used to impose an
              alternate ordering on the elements, perhaps when
              this is used in the context of a particular structure.
              The default is to use whatever ordering the ``S.list``
              method returns. Or the ``elements`` can be a subset
              which is closed under the operation. In particular,
              this can be used when the base set is infinite.

            OUTPUT:

            The multiplication table as an object of the class
            :class:`~sage.matrix.operation_table.OperationTable`
            which defines several methods for manipulating and
            displaying the table.  See the documentation there
            for full details to supplement the documentation
            here.

            EXAMPLES:

            The default is to represent elements as lowercase
            ASCII letters.  ::

                sage: G = CyclicPermutationGroup(5)                                     # needs sage.groups
                sage: G.multiplication_table()                                          # needs sage.groups
                *  a b c d e
                 +----------
                a| a b c d e
                b| b c d e a
                c| c d e a b
                d| d e a b c
                e| e a b c d

            All that is required is that an algebraic structure
            has a multiplication defined.  A
            :class:`~sage.categories.examples.finite_semigroups.LeftRegularBand`
            is an example of a finite semigroup.  The ``names`` argument allows
            displaying the elements in different ways.  ::

                sage: from sage.categories.examples.finite_semigroups import LeftRegularBand
                sage: L = LeftRegularBand(('a', 'b'))
                sage: T = L.multiplication_table(names='digits')                        # needs sage.modules
                sage: T.column_keys()                                                   # needs sage.modules
                ('a', 'ab', 'b', 'ba')
                sage: T                                                                 # needs sage.modules
                *  0 1 2 3
                 +--------
                0| 0 1 1 1
                1| 1 1 1 1
                2| 3 3 2 3
                3| 3 3 3 3

            Specifying the elements in an alternative order can provide
            more insight into how the operation behaves.  ::

                sage: L = LeftRegularBand(('a', 'b', 'c'))
                sage: elts = sorted(L.list())
                sage: L.multiplication_table(elements=elts)                             # needs sage.modules
                *  a b c d e f g h i j k l m n o
                 +------------------------------
                a| a b c d e b b c c c d d e e e
                b| b b c c c b b c c c c c c c c
                c| c c c c c c c c c c c c c c c
                d| d e e d e e e e e e d d e e e
                e| e e e e e e e e e e e e e e e
                f| g g h h h f g h i j i j j i j
                g| g g h h h g g h h h h h h h h
                h| h h h h h h h h h h h h h h h
                i| j j j j j i j j i j i j j i j
                j| j j j j j j j j j j j j j j j
                k| l m m l m n o o n o k l m n o
                l| l m m l m m m m m m l l m m m
                m| m m m m m m m m m m m m m m m
                n| o o o o o n o o n o n o o n o
                o| o o o o o o o o o o o o o o o

            The ``elements`` argument can be used to provide
            a subset of the elements of the structure.  The subset
            must be closed under the operation.  Elements need only
            be in a form that can be coerced into the set.  The
            ``names`` argument can also be used to request that
            the elements be represented with their usual string
            representation.  ::

                sage: L = LeftRegularBand(('a','b','c'))
                sage: elts=['a', 'c', 'ac', 'ca']
                sage: L.multiplication_table(names='elements', elements=elts)           # needs sage.modules
                   *   'a'  'c' 'ac' 'ca'
                    +--------------------
                 'a'|  'a' 'ac' 'ac' 'ac'
                 'c'| 'ca'  'c' 'ca' 'ca'
                'ac'| 'ac' 'ac' 'ac' 'ac'
                'ca'| 'ca' 'ca' 'ca' 'ca'

            The table returned can be manipulated in various ways.  See
            the documentation for
            :class:`~sage.matrix.operation_table.OperationTable` for more
            comprehensive documentation. ::

                sage: # needs sage.groups sage.modules
                sage: G = AlternatingGroup(3)
                sage: T = G.multiplication_table()
                sage: T.column_keys()
                ((), (1,2,3), (1,3,2))
                sage: T.translation()
                {'a': (), 'b': (1,2,3), 'c': (1,3,2)}
                sage: T.change_names(['x', 'y', 'z'])
                sage: T.translation()
                {'x': (), 'y': (1,2,3), 'z': (1,3,2)}
                sage: T
                *  x y z
                 +------
                x| x y z
                y| y z x
                z| z x y
            """
    class ElementMethods:
        def is_idempotent(self):
            '''
            Test whether ``self`` is idempotent.

            EXAMPLES::

                sage: S = Semigroups().example("free"); S
                An example of a semigroup:
                 the free semigroup generated by (\'a\', \'b\', \'c\', \'d\')
                sage: a = S(\'a\')
                sage: a^2
                \'aa\'
                sage: a.is_idempotent()
                False

            ::

                sage: L = Semigroups().example("leftzero"); L
                An example of a semigroup: the left zero semigroup
                sage: x = L(\'x\')
                sage: x^2
                \'x\'
                sage: x.is_idempotent()
                True
            '''
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            This implements the fact that a subquotient (and therefore
            a quotient or subobject) of a finite set is finite.

            EXAMPLES::

                sage: Semigroups().CartesianProducts().extra_super_categories()
                [Category of semigroups]
                sage: Semigroups().CartesianProducts().super_categories()
                [Category of semigroups, Category of Cartesian products of magmas]
            """
        def example(self):
            """
            Return an example of Cartesian product of magmas.

            EXAMPLES::

                sage: C = Magmas().CartesianProducts().example(); C
                The Cartesian product of (Rational Field, Integer Ring, Integer Ring)
                sage: C.category()
                Join of Category of Cartesian products of commutative rings and
                Category of Cartesian products of metric spaces
                sage: sorted(C.category().axioms())
                ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse',
                 'AdditiveUnital', 'Associative', 'Commutative',
                 'Distributive', 'Unital']

                sage: TestSuite(C).run()
            """
        class ParentMethods:
            def product(self, left, right):
                """
                EXAMPLES::

                    sage: C = Magmas().CartesianProducts().example(); C
                    The Cartesian product of (Rational Field, Integer Ring, Integer Ring)
                    sage: x = C.an_element(); x
                    (1/2, 1, 1)
                    sage: x * x
                    (1/4, 1, 1)

                    sage: # needs sage.groups sage.modules
                    sage: A = SymmetricGroupAlgebra(QQ, 3)
                    sage: x = cartesian_product([A([1,3,2]), A([2,3,1])])
                    sage: y = cartesian_product([A([1,3,2]), A([2,3,1])])
                    sage: cartesian_product([A,A]).product(x,y)
                    B[(0, [1, 2, 3])] + B[(1, [3, 1, 2])]
                    sage: x*y
                    B[(0, [1, 2, 3])] + B[(1, [3, 1, 2])]
                """
    class Subquotients(SubquotientsCategory):
        """
        The category of subquotient magmas.

        See :meth:`Sets.SubcategoryMethods.Subquotients` for the
        general setup for subquotients. In the case of a subquotient
        magma `S` of a magma `G`, the condition that `r` be a
        morphism in ``As`` can be rewritten as follows:

         - for any two `a,b \\in S` the identity
           `a \\times_S b = r(l(a) \\times_G l(b))` holds.

        This is used by this category to implement the product
        `\\times_S` of `S` from `l` and `r` and the product of `G`.

        EXAMPLES::

            sage: Semigroups().Subquotients().all_super_categories()
            [Category of subquotients of semigroups, Category of semigroups,
             Category of subquotients of magmas, Category of magmas,
             Category of subquotients of sets, Category of sets,
             Category of sets with partial maps,
             Category of objects]
        """
        class ParentMethods:
            def product(self, x, y):
                """
                Return the product of two elements of ``self``.

                EXAMPLES::

                    sage: S = Semigroups().Subquotients().example()
                    sage: S
                    An example of a (sub)quotient semigroup:
                    a quotient of the left zero semigroup
                    sage: S.product(S(19), S(3))
                    19

                Here is a more elaborate example involving a sub algebra::

                    sage: Z = SymmetricGroup(5).algebra(QQ).center()                    # needs sage.combinat sage.groups
                    sage: B = Z.basis()                                                 # needs sage.combinat sage.groups
                    sage: B[3] * B[2]                                                   # needs sage.combinat sage.groups
                    4*B[2] + 6*B[3] + 5*B[6]
                """
    class Realizations(RealizationsCategory):
        class ParentMethods:
            def product_by_coercion(self, left, right):
                """
                Default implementation of product for realizations.

                This method coerces to the realization specified by
                ``self.realization_of().a_realization()``, computes
                the product in that realization, and then coerces
                back.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: Out = Sets().WithRealizations().example().Out(); Out
                    The subset algebra of {1, 2, 3} over Rational Field
                     in the Out basis
                    sage: Out.product
                    <bound method Magmas.Realizations.ParentMethods.product_by_coercion
                     of The subset algebra of {1, 2, 3} over Rational Field
                      in the Out basis>
                    sage: Out.product.__module__
                    'sage.categories.magmas'
                    sage: x = Out.an_element()
                    sage: y = Out.an_element()
                    sage: Out.product(x, y)
                    Out[{}] + 4*Out[{1}] + 9*Out[{2}] + Out[{1, 2}]
                """
