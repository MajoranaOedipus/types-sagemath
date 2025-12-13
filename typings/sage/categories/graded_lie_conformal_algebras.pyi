from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.misc.cachefunc import cached_method as cached_method

class GradedLieConformalAlgebrasCategory(GradedModulesCategory):
    @cached_method
    def Super(self, base_ring=None):
        """
        Return the super-analogue category of ``self``.

        INPUT:

        - ``base_ring`` -- this is ignored

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: C = LieConformalAlgebras(QQbar)
            sage: C.Graded().Super() is C.Super().Graded()
            True
            sage: Cp = C.WithBasis()
            sage: Cp.Graded().Super() is Cp.Super().Graded()
            True
        """

class GradedLieConformalAlgebras(GradedLieConformalAlgebrasCategory):
    """
    The category of graded Lie conformal algebras.

    EXAMPLES::

        sage: C = LieConformalAlgebras(QQbar).Graded(); C                               # needs sage.rings.number_field
        Category of H-graded Lie conformal algebras over Algebraic Field

        sage: CS = LieConformalAlgebras(QQ).Graded().Super(); CS
        Category of H-graded super Lie conformal algebras over Rational Field
        sage: CS is LieConformalAlgebras(QQ).Super().Graded()
        True
    """
