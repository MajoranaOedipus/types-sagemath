from _typeshed import Incomplete
from sage.categories.associative_algebras import AssociativeAlgebras as AssociativeAlgebras
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory as DualObjectsCategory
from sage.categories.quotients import QuotientsCategory as QuotientsCategory
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class Algebras(CategoryWithAxiom_over_base_ring):
    """
    The category of associative and unital algebras over a given base ring.

    An associative and unital algebra over a ring `R` is a module over
    `R` which is itself a ring.

    .. WARNING::

        :class:`Algebras` will be eventually be replaced by
        :class:`.magmatic_algebras.MagmaticAlgebras`
        for consistency with e.g. :wikipedia:`Algebras` which assumes
        neither associativity nor the existence of a unit (see
        :issue:`15043`).

    .. TODO:: Should `R` be a commutative ring?

    EXAMPLES::

        sage: Algebras(ZZ)
        Category of algebras over Integer Ring
        sage: sorted(Algebras(ZZ).super_categories(), key=str)
        [Category of associative algebras over Integer Ring,
         Category of rings,
         Category of unital algebras over Integer Ring]

    TESTS::

        sage: TestSuite(Algebras(ZZ)).run()
    """
    def __contains__(self, x) -> bool:
        """
        Membership testing.

        EXAMPLES::

            sage: QQ['x'] in Algebras(QQ)
            True

            sage: QQ^3 in Algebras(QQ)                                                  # needs sage.modules
            False
            sage: QQ['x'] in Algebras(CDF)                                              # needs sage.rings.complex_double
            False
        """
    class SubcategoryMethods:
        def Semisimple(self):
            """
            Return the subcategory of semisimple objects of ``self``.

            .. NOTE::

                This mimics the syntax of axioms for a smooth
                transition if ``Semisimple`` becomes one.

            EXAMPLES::

                sage: Algebras(QQ).Semisimple()
                Category of semisimple algebras over Rational Field
                sage: Algebras(QQ).WithBasis().FiniteDimensional().Semisimple()
                Category of finite dimensional semisimple algebras with basis over Rational Field
            """
        @cached_method
        def Supercommutative(self):
            """
            Return the full subcategory of the supercommutative objects
            of ``self``.

            This is shorthand for creating the corresponding super category.

            EXAMPLES::

                sage: Algebras(ZZ).Supercommutative()
                Category of supercommutative algebras over Integer Ring
                sage: Algebras(ZZ).WithBasis().Supercommutative()
                Category of supercommutative super algebras with basis over Integer Ring

                sage: Cat = Algebras(ZZ).Supercommutative()
                sage: Cat is Algebras(ZZ).Super().Supercommutative()
                True
            """
    Commutative: Incomplete
    Filtered: Incomplete
    Graded: Incomplete
    Super: Incomplete
    WithBasis: Incomplete
    Semisimple: Incomplete
    class ParentMethods:
        def characteristic(self):
            """
            Return the characteristic of this algebra, which is the same
            as the characteristic of its base ring.

            EXAMPLES::

                sage: # needs sage.modules
                sage: ZZ.characteristic()
                0
                sage: A = GF(7^3, 'a')                                                      # needs sage.rings.finite_rings
                sage: A.characteristic()                                                    # needs sage.rings.finite_rings
                7
            """
        def has_standard_involution(self) -> bool:
            """
            Return ``True`` if the algebra has a standard involution and ``False`` otherwise.

            This algorithm follows Algorithm 2.10 from John Voight's *Identifying the Matrix Ring*.
            Currently the only type of algebra this will work for is a quaternion algebra.
            Though this function seems redundant, once algebras have more functionality, in particular
            have a method to construct a basis, this algorithm will have more general purpose.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: B = QuaternionAlgebra(2)
                sage: B.has_standard_involution()
                True
                sage: R.<x> = PolynomialRing(QQ)
                sage: K.<u> = NumberField(x**2 - 2)                                         # needs sage.rings.number_field
                sage: A = QuaternionAlgebra(K, -2, 5)                                       # needs sage.rings.number_field
                sage: A.has_standard_involution()                                           # needs sage.rings.number_field
                True
                sage: L.<a,b> = FreeAlgebra(QQ, 2)
                sage: L.has_standard_involution()
                Traceback (most recent call last):
                ...
                NotImplementedError: has_standard_involution is not implemented for this algebra
                """
    class ElementMethods: ...
    class Quotients(QuotientsCategory):
        class ParentMethods:
            def algebra_generators(self):
                """
                Return algebra generators for ``self``.

                This implementation retracts the algebra generators
                from the ambient algebra.

                EXAMPLES::

                    sage: # needs sage.graphs sage.modules
                    sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
                    An example of a finite dimensional algebra with basis:
                    the path algebra of the Kronecker quiver
                    (containing the arrows a:x->y and b:x->y) over Rational Field
                    sage: S = A.semisimple_quotient()
                    sage: S.algebra_generators()
                    Finite family {'x': B['x'], 'y': B['y'], 'a': 0, 'b': 0}

                .. TODO:: this could possibly remove the elements that retract to zero.
                """
    class CartesianProducts(CartesianProductsCategory):
        """
        The category of algebras constructed as Cartesian products of algebras.

        This construction gives the direct product of algebras. See
        discussion on:

         - http://groups.google.fr/group/sage-devel/browse_thread/thread/35a72b1d0a2fc77a/348f42ae77a66d16#348f42ae77a66d16
         - :wikipedia:`Direct_product`
        """
        def extra_super_categories(self):
            """
            A Cartesian product of algebras is endowed with a natural
            algebra structure.

            EXAMPLES::

                sage: C = Algebras(QQ).CartesianProducts()
                sage: C.extra_super_categories()
                [Category of algebras over Rational Field]
                sage: sorted(C.super_categories(), key=str)
                [Category of Cartesian products of monoids,
                 Category of Cartesian products of unital algebras over Rational Field,
                 Category of algebras over Rational Field]
            """
    class TensorProducts(TensorProductsCategory):
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Algebras(QQ).TensorProducts().extra_super_categories()
                [Category of algebras over Rational Field]
                sage: Algebras(QQ).TensorProducts().super_categories()
                [Category of algebras over Rational Field,
                 Category of tensor products of vector spaces over Rational Field]

            Meaning: a tensor product of algebras is an algebra
            """
        class ParentMethods: ...
        class ElementMethods: ...
    class DualObjects(DualObjectsCategory):
        def extra_super_categories(self):
            """
            Return the dual category.

            EXAMPLES:

            The category of algebras over the Rational Field is dual
            to the category of coalgebras over the same field::

                sage: C = Algebras(QQ)
                sage: C.dual()
                Category of duals of algebras over Rational Field
                sage: C.dual().extra_super_categories()
                [Category of coalgebras over Rational Field]

            .. WARNING::

                This is only correct in certain cases (finite dimension, ...).
                See :issue:`15647`.
            """
