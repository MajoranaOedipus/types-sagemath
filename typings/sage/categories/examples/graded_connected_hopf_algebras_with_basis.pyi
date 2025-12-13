from sage.categories.graded_hopf_algebras_with_basis import GradedHopfAlgebrasWithBasis as GradedHopfAlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

class GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator(CombinatorialFreeModule):
    """
    This class illustrates an implementation of a graded Hopf algebra
    with basis that has one primitive generator of degree 1 and basis
    elements indexed by nonnegative integers.

    This Hopf algebra example differs from what topologists refer to as
    a graded Hopf algebra because the twist operation in the tensor rule
    satisfies

    .. MATH::

        (\\mu \\otimes \\mu) \\circ (id \\otimes \\tau \\otimes id) \\circ
        (\\Delta \\otimes \\Delta) = \\Delta \\circ \\mu

    where `\\tau(x\\otimes y) = y\\otimes x`.
    """
    def __init__(self, base_ring) -> None:
        """
        EXAMPLES::

            sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
            sage: TestSuite(H).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return 0, which index the unit of the Hopf algebra.

        OUTPUT: the nonnegative integer 0

        EXAMPLES::

            sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
            sage: H.one_basis()
            0
            sage: H.one()
            P0
        """
    def degree_on_basis(self, i):
        """
        The degree of a nonnegative integer is itself.

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: nonnegative integer

        TESTS::

            sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
            sage: H.degree_on_basis(45)
            45
        """
    def product_on_basis(self, i, j):
        """
        The product of two basis elements.

        The product of elements of degree ``i`` and ``j`` is an element
        of degree ``i+j``.

        INPUT:

        - ``i``, ``j`` -- nonnegative integers

        OUTPUT: a basis element indexed by ``i+j``

        TESTS::

            sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
            sage: H.monomial(4) * H.monomial(5)
            P9
        """
    def coproduct_on_basis(self, i):
        """
        The coproduct of a basis element.

        .. MATH::

            \\Delta(P_i) = \\sum_{j=0}^i P_{i-j} \\otimes P_j

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: an element of the tensor square of ``self``

        TESTS::

            sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
            sage: H.monomial(3).coproduct()
            P0 # P3 + 3*P1 # P2 + 3*P2 # P1 + P3 # P0
        """
Example = GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator
