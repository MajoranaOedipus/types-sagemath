from _typeshed import Incomplete
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.misc.lazy_import import LazyImport as LazyImport

class GradedLieAlgebrasWithBasis(GradedModulesCategory):
    """
    The category of graded Lie algebras with a distinguished basis.

    EXAMPLES::

        sage: C = LieAlgebras(ZZ).WithBasis().Graded(); C
        Category of graded Lie algebras with basis over Integer Ring
        sage: C.super_categories()
        [Category of graded modules with basis over Integer Ring,
         Category of Lie algebras with basis over Integer Ring,
         Category of graded Lie algebras over Integer Ring]

        sage: C is LieAlgebras(ZZ).WithBasis().Graded()
        True
        sage: C is LieAlgebras(ZZ).Graded().WithBasis()
        False

    TESTS::

        sage: TestSuite(C).run()
    """
    FiniteDimensional: Incomplete
