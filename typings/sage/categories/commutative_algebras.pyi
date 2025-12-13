from sage.categories.algebras import Algebras as Algebras
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method

class CommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    """
    The category of commutative algebras with unit over a given base ring.

    EXAMPLES::

        sage: M = CommutativeAlgebras(GF(19))
        sage: M
        Category of commutative algebras over Finite Field of size 19
        sage: CommutativeAlgebras(QQ).super_categories()
        [Category of algebras over Rational Field, Category of commutative rings]

    This is just a shortcut for::

        sage: Algebras(QQ).Commutative()
        Category of commutative algebras over Rational Field

    TESTS::

        sage: Algebras(QQ).Commutative() is CommutativeAlgebras(QQ)
        True
        sage: TestSuite(CommutativeAlgebras(ZZ)).run()

    .. TODO::

     - product   ( = Cartesian product)
     - coproduct ( = tensor product over base ring)
    """
    def __contains__(self, A) -> bool:
        """
        EXAMPLES::

            sage: QQ['a'] in CommutativeAlgebras(QQ)
            True
            sage: QQ['a,b'] in CommutativeAlgebras(QQ)
            True
            sage: FreeAlgebra(QQ, 2, 'a,b') in CommutativeAlgebras(QQ)                  # needs sage.combinat sage.modules
            False

        TODO: get rid of this method once all commutative algebras in
        Sage declare themselves in this category
        """
    class TensorProducts(TensorProductsCategory):
        """
        The category of commutative algebras constructed by tensor product of commutative algebras.
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Algebras(QQ).Commutative().TensorProducts().extra_super_categories()
                [Category of commutative rings]
                sage: Algebras(QQ).Commutative().TensorProducts().super_categories()
                [Category of tensor products of algebras over Rational Field,
                 Category of commutative algebras over Rational Field]

            TESTS::

                sage: # needs sage.combinat sage.modules
                sage: X = algebras.Shuffle(QQ, 'ab')
                sage: Y = algebras.Shuffle(QQ, 'bc')
                sage: X in Algebras(QQ).Commutative()
                True
                sage: T = tensor([X, Y])
                sage: T in CommutativeRings()
                True
            """
