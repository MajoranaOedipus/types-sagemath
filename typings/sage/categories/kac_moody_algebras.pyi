from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.misc.cachefunc import cached_method as cached_method

class KacMoodyAlgebras(Category_over_base_ring):
    """
    Category of Kac-Moody algebras.
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.kac_moody_algebras import KacMoodyAlgebras
            sage: KacMoodyAlgebras(QQ).super_categories()
            [Category of Lie algebras over Rational Field]
        """
    def example(self, n: int = 2):
        """
        Return an example of a Kac-Moody algebra as per
        :meth:`Category.example <sage.categories.category.Category.example>`.

        EXAMPLES::

            sage: from sage.categories.kac_moody_algebras import KacMoodyAlgebras
            sage: KacMoodyAlgebras(QQ).example()                                        # needs sage.combinat sage.modules
            Lie algebra of ['A', 2] in the Chevalley basis

        We can specify the rank of the example::

            sage: KacMoodyAlgebras(QQ).example(4)                                       # needs sage.combinat sage.modules
            Lie algebra of ['A', 4] in the Chevalley basis
        """
    class ParentMethods:
        def cartan_type(self):
            """
            Return the Cartan type of ``self``.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=['A', 2])                          # needs sage.combinat sage.modules
                sage: L.cartan_type()                                                   # needs sage.combinat sage.modules
                ['A', 2]
            """
        def weyl_group(self):
            """
            Return the Weyl group of ``self``.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=['A', 2])                          # needs sage.combinat sage.modules
                sage: L.weyl_group()                                                    # needs sage.combinat sage.modules
                Weyl Group of type ['A', 2] (as a matrix group acting on the ambient space)
            """
