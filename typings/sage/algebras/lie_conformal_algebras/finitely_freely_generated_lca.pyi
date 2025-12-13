from .freely_generated_lie_conformal_algebra import FreelyGeneratedLieConformalAlgebra as FreelyGeneratedLieConformalAlgebra
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras
from sage.misc.cachefunc import cached_method as cached_method

class FinitelyFreelyGeneratedLCA(FreelyGeneratedLieConformalAlgebra):
    """
    Abstract base class for finitely generated Lie conformal
    algebras.

    This class provides minimal functionality, simply sets the
    number of generators.
    """
    def __init__(self, R, index_set=None, central_elements=None, category=None, element_class=None, prefix=None, names=None, latex_names=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.Virasoro(QQ)
            sage: TestSuite(V).run()
        """
    def ngens(self):
        """
        The number of generators of this Lie conformal algebra.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ); Vir.ngens()
            2
            sage: V = lie_conformal_algebras.Affine(QQ, 'A1'); V.ngens()
            4
        """
    @cached_method
    def gens(self):
        """
        The generators for this Lie conformal algebra.

        OUTPUT:

        This method returns a tuple with the (finite) generators
        of this Lie conformal algebra.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ);
            sage: Vir.gens()
            (L, C)

        .. SEEALSO::

            :meth:`lie_conformal_algebra_generators<            FreelyGeneratedLieConformalAlgebra.            lie_conformal_algebra_generators>`
        """
    @cached_method
    def central_elements(self):
        """
        The central elements of this Lie conformal algebra.

        EXAMPLES::

            sage: R = lie_conformal_algebras.NeveuSchwarz(QQ); R.central_elements()
            (C,)
        """
