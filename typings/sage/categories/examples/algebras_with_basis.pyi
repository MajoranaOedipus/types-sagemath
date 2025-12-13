from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.words import Words as Words
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import Family as Family

class FreeAlgebra(CombinatorialFreeModule):
    """
    An example of an algebra with basis: the free algebra.

    This class illustrates a minimal implementation of an algebra with basis.
    """
    def __init__(self, R, alphabet=('a', 'b', 'c')) -> None:
        """
        EXAMPLES::

            sage: A = AlgebrasWithBasis(QQ).example(); A                                # needs sage.modules
            An example of an algebra with basis: the free algebra on the generators ('a', 'b', 'c') over Rational Field
            sage: TestSuite(A).run()                                                    # needs sage.modules
        """
    @cached_method
    def one_basis(self):
        """
        Return the empty word, which index the one of this algebra,
        as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.

        EXAMPLES::

            sage: A = AlgebrasWithBasis(QQ).example()                                   # needs sage.modules
            sage: A.one_basis()                                                         # needs sage.modules
            word:
            sage: A.one()                                                               # needs sage.modules
            B[word: ]
        """
    def product_on_basis(self, w1, w2):
        '''
        Product of basis elements, as per
        :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis`.

        EXAMPLES::

            sage: # needs sage.modules
            sage: A = AlgebrasWithBasis(QQ).example()
            sage: Words = A.basis().keys()
            sage: A.product_on_basis(Words("acb"), Words("cba"))
            B[word: acbcba]
            sage: (a,b,c) = A.algebra_generators()
            sage: a * (1-b)^2 * c
            B[word: abbc] - 2*B[word: abc] + B[word: ac]
        '''
    @cached_method
    def algebra_generators(self):
        """
        Return the generators of this algebra, as per :meth:`~.magmatic_algebras.MagmaticAlgebras.ParentMethods.algebra_generators`.

        EXAMPLES::

            sage: A = AlgebrasWithBasis(QQ).example(); A                                # needs sage.modules
            An example of an algebra with basis: the free algebra on the generators ('a', 'b', 'c') over Rational Field
            sage: A.algebra_generators()                                                # needs sage.modules
            Family (B[word: a], B[word: b], B[word: c])
        """
Example = FreeAlgebra
