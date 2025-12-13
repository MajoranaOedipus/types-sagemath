from sage.categories.finite_dimensional_algebras_with_basis import FiniteDimensionalAlgebrasWithBasis as FiniteDimensionalAlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method

class KroneckerQuiverPathAlgebra(CombinatorialFreeModule):
    """
    An example of a finite dimensional algebra with basis: the path
    algebra of the Kronecker quiver.

    This class illustrates a minimal implementation of a finite
    dimensional algebra with basis. See
    :class:`sage.quivers.algebra.PathAlgebra` for a full-featured
    implementation of path algebras.
    """
    def __init__(self, base_ring) -> None:
        """
        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
            An example of a finite dimensional algebra with basis:
            the path algebra of the Kronecker quiver
            (containing the arrows a:x->y and b:x->y) over Rational Field
            sage: TestSuite(A).run()
        """
    def one(self):
        """
        Return the unit of this algebra.

        .. SEEALSO:: :meth:`AlgebrasWithBasis.ParentMethods.one_basis`

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example()
            sage: A.one()
            x + y
        """
    def product_on_basis(self, w1, w2):
        """
        Return the product of the two basis elements indexed by ``w1`` and ``w2``.

        .. SEEALSO:: :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example()

        Here is the multiplication table for the algebra::

            sage: matrix([[p*q for q in A.basis()] for p in A.basis()])
            [x 0 a b]
            [0 y 0 0]
            [0 a 0 0]
            [0 b 0 0]

        Here we take some products of linear combinations of basis elements::

            sage: x, y, a, b = A.basis()
            sage: a * (1-b)^2 * x
            0
            sage: x*a + b*y
            a + b
            sage: x*x
            x
            sage: x*y
            0
            sage: x*a*y
            a
        """
    @cached_method
    def algebra_generators(self):
        """
        Return algebra generators for this algebra.

        .. SEEALSO:: :meth:`Algebras.ParentMethods.algebra_generators`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
            An example of a finite dimensional algebra with basis:
            the path algebra of the Kronecker quiver
            (containing the arrows a:x->y and b:x->y) over Rational Field
            sage: A.algebra_generators()
            Finite family {'x': x, 'y': y, 'a': a, 'b': b}
        """
Example = KroneckerQuiverPathAlgebra
