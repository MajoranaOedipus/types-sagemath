from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.supercrystals import SuperCrystals as SuperCrystals
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class RegularSuperCrystals(Category_singleton):
    """
    The category of crystals for super Lie algebras.

    EXAMPLES::

        sage: from sage.categories.regular_supercrystals import RegularSuperCrystals
        sage: C = RegularSuperCrystals()
        sage: C
        Category of regular super crystals
        sage: C.super_categories()
        [Category of finite super crystals]

    Parents in this category should implement the following methods:

    - either an attribute ``_cartan_type`` or a method ``cartan_type``

    - ``module_generators`` -- a list (or container) of distinct elements
      that generate the crystal using `f_i` and `e_i`

    Furthermore, their elements ``x`` should implement the following
    methods:

    - ``x.e(i)`` (returning `e_i(x)`)

    - ``x.f(i)`` (returning `f_i(x)`)

    - ``x.weight()`` (returning `\\operatorname{wt}(x)`)

    EXAMPLES::

        sage: from sage.misc.abstract_method import abstract_methods_of_class
        sage: from sage.categories.regular_supercrystals import RegularSuperCrystals
        sage: abstract_methods_of_class(RegularSuperCrystals().element_class)
        {'optional': [], 'required': ['e', 'f', 'weight']}

    TESTS::

        sage: from sage.categories.regular_supercrystals import RegularSuperCrystals
        sage: C = RegularSuperCrystals()
        sage: TestSuite(C).run()
        sage: B = crystals.Letters(['A',[1,1]]); B
        The crystal of letters for type ['A', [1, 1]]
        sage: TestSuite(B).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.regular_supercrystals import RegularSuperCrystals
            sage: C = RegularSuperCrystals()
            sage: C.super_categories()
            [Category of finite super crystals]
        """
    class ElementMethods:
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            EXAMPLES::

                sage: C = crystals.Tableaux(['A',[1,2]], shape=[2,1])
                sage: c = C.an_element(); c
                [[-2, -2], [-1]]
                sage: c.epsilon(2)
                0
                sage: c.epsilon(0)
                0
                sage: c.epsilon(-1)
                0
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            EXAMPLES::

                sage: C = crystals.Tableaux(['A',[1,2]], shape=[2,1])
                sage: c = C.an_element(); c
                [[-2, -2], [-1]]
                sage: c.phi(1)
                0
                sage: c.phi(2)
                0
                sage: c.phi(0)
                1
            """
    class TensorProducts(TensorProductsCategory):
        """
        The category of regular crystals constructed by tensor
        product of regular crystals.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: from sage.categories.regular_supercrystals import RegularSuperCrystals
                sage: RegularSuperCrystals().TensorProducts().extra_super_categories()
                [Category of regular super crystals]
            """
