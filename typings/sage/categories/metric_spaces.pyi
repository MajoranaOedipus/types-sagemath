from _typeshed import Incomplete
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category import Category as Category
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.with_realizations import WithRealizationsCategory as WithRealizationsCategory
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias

class MetricSpacesCategory(RegressiveCovariantConstructionCategory):
    @classmethod
    def default_super_categories(cls, category):
        """
        Return the default super categories of ``category.Metric()``.

        Mathematical meaning: if `A` is a metric space in the
        category `C`, then `A` is also a topological space.

        INPUT:

        - ``cls`` -- the class ``MetricSpaces``
        - ``category`` -- a category `Cat`

        OUTPUT:

        A (join) category

        In practice, this returns ``category.Metric()``, joined
        together with the result of the method
        :meth:`RegressiveCovariantConstructionCategory.default_super_categories()
        <sage.categories.covariant_functorial_construction.RegressiveCovariantConstructionCategory.default_super_categories>`
        (that is the join of ``category`` and ``cat.Metric()`` for
        each ``cat`` in the super categories of ``category``).

        EXAMPLES:

        Consider ``category=Groups()``. Then, a group `G` with a metric
        is simultaneously a topological group by itself, and a
        metric space::

            sage: Groups().Metric().super_categories()
            [Category of topological groups, Category of metric spaces]

        This resulted from the following call::

            sage: sage.categories.metric_spaces.MetricSpacesCategory.default_super_categories(Groups())
            Join of Category of topological groups and Category of metric spaces
        """

class MetricSpaces(MetricSpacesCategory):
    """
    The category of metric spaces.

    A *metric* on a set `S` is a function `d : S \\times S \\to \\RR`
    such that:

    - `d(a, b) \\geq 0`,
    - `d(a, b) = 0` if and only if `a = b`.

    A metric space is a set `S` with a distinguished metric.

    .. RUBRIC:: Implementation

    Objects in this category must implement either a ``dist`` on the parent
    or the elements or ``metric`` on the parent; otherwise this will cause
    an infinite recursion.

    .. TODO::

        - Implement a general geodesics class.
        - Implement a category for metric additive groups
          and move the generic distance `d(a, b) = |a - b|` there.
        - Incorporate the length of a geodesic as part of the default
          distance cycle.

    EXAMPLES::

        sage: from sage.categories.metric_spaces import MetricSpaces
        sage: C = MetricSpaces()
        sage: C
        Category of metric spaces
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        def metric_function(self):
            """
            Return the metric function of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: UHP = HyperbolicPlane().UHP()
                sage: m = UHP.metric_function()
                sage: p1 = UHP.get_point(5 + 7*I)
                sage: p2 = UHP.get_point(1.0 + I)
                sage: m(p1, p2)
                2.23230104635820
            """
        metric: Incomplete
        def dist(self, a, b):
            """
            Return the distance between ``a`` and ``b`` in ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: UHP = HyperbolicPlane().UHP()
                sage: p1 = UHP.get_point(5 + 7*I)
                sage: p2 = UHP.get_point(1.0 + I)
                sage: UHP.dist(p1, p2)
                2.23230104635820

                sage: PD = HyperbolicPlane().PD()                                       # needs sage.symbolic
                sage: PD.dist(PD.get_point(0), PD.get_point(I/2))                       # needs sage.symbolic
                arccosh(5/3)

            TESTS::

                sage: RR.dist(-1, pi)                                                   # needs sage.rings.real_mpfr sage.symbolic
                4.14159265358979
                sage: RDF.dist(1, -1/2)
                1.5
                sage: CC.dist(3, 2)                                                     # needs sage.rings.real_mpfr
                1.00000000000000
                sage: CC.dist(-1, I)                                                    # needs sage.rings.real_mpfr sage.symbolic
                1.41421356237310
                sage: CDF.dist(-1, I)                                                   # needs sage.rings.real_mpfr sage.symbolic
                1.4142135623730951
            """
    class ElementMethods:
        def abs(self):
            """
            Return the absolute value of ``self``.

            EXAMPLES::

                sage: CC(I).abs()                                                       # needs sage.rings.real_mpfr sage.symbolic
                1.00000000000000
            """
        def dist(self, b):
            """
            Return the distance between ``self`` and ``other``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: UHP = HyperbolicPlane().UHP()
                sage: p1 = UHP.get_point(5 + 7*I)
                sage: p2 = UHP.get_point(1 + I)
                sage: p1.dist(p2)
                arccosh(33/7)
            """
    class Homsets(HomsetsCategory):
        """
        The category of homsets of metric spaces.

        It consists of the metric maps, that is, the Lipschitz functions
        with Lipschitz constant 1.
        """
        class ElementMethods: ...
    class WithRealizations(WithRealizationsCategory):
        class ParentMethods:
            def dist(self, a, b):
                """
                Return the distance between ``a`` and ``b`` by converting them
                to a realization of ``self`` and doing the computation.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: H = HyperbolicPlane()
                    sage: PD = H.PD()
                    sage: p1 = PD.get_point(0)
                    sage: p2 = PD.get_point(I/2)
                    sage: H.dist(p1, p2)
                    arccosh(5/3)
                """
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a (finite) Cartesian product of metric spaces is
            a metric space.

            EXAMPLES::

                sage: from sage.categories.metric_spaces import MetricSpaces
                sage: C = MetricSpaces().CartesianProducts()
                sage: C.extra_super_categories()
                [Category of metric spaces]
                sage: C.super_categories()
                [Category of Cartesian products of topological spaces,
                 Category of metric spaces]
                sage: C.axioms()
                frozenset()
            """
        class ParentMethods:
            def dist(self, a, b):
                """
                Return the distance between ``a`` and ``b`` in ``self``.

                It is defined as the maximum of the distances within
                the Cartesian factors.

                EXAMPLES::

                    sage: from sage.categories.metric_spaces import MetricSpaces
                    sage: Q2 = QQ.cartesian_product(QQ)
                    sage: Q2.category()
                    Join of
                    Category of Cartesian products of commutative rings and
                    Category of Cartesian products of metric spaces
                    sage: Q2 in MetricSpaces()
                    True
                    sage: Q2.dist((0, 0), (2, 3))
                    3
                """
    class SubcategoryMethods:
        @cached_method
        def Complete(self):
            """
            Return the full subcategory of the complete objects of ``self``.

            EXAMPLES::

                sage: Sets().Metric().Complete()
                Category of complete metric spaces

            TESTS::

                sage: TestSuite(Sets().Metric().Complete()).run()
                sage: Sets().Metric().Complete.__module__
                'sage.categories.metric_spaces'
            """
    class Complete(CategoryWithAxiom):
        """
        The category of complete metric spaces.
        """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a (finite) Cartesian product of complete
                metric spaces is a complete metric space.

                EXAMPLES::

                    sage: from sage.categories.metric_spaces import MetricSpaces
                    sage: C = MetricSpaces().Complete().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of complete metric spaces]
                    sage: C.super_categories()
                    [Category of Cartesian products of metric spaces,
                     Category of complete metric spaces]
                    sage: C.axioms()
                    frozenset({'Complete'})

                    sage: R2 = RR.cartesian_product(RR)
                    sage: R2 in MetricSpaces()
                    True
                    sage: R2 in MetricSpaces().Complete()
                    True

                    sage: QR = QQ.cartesian_product(RR)
                    sage: QR in MetricSpaces()
                    True
                    sage: QR in MetricSpaces().Complete()
                    False
                """
