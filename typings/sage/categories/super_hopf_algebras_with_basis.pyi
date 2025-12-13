from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class SuperHopfAlgebrasWithBasis(SuperModulesCategory):
    """
    The category of super Hopf algebras with a distinguished basis.

    EXAMPLES::

        sage: C = HopfAlgebras(ZZ).WithBasis().Super(); C
        Category of super Hopf algebras with basis over Integer Ring
        sage: sorted(C.super_categories(), key=str)
        [Category of super Hopf algebras over Integer Ring,
         Category of super algebras with basis over Integer Ring,
         Category of super coalgebras with basis over Integer Ring]

    TESTS::

        sage: C = HopfAlgebras(ZZ).WithBasis().Super()
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        @lazy_attribute
        def antipode(self):
            """
            The antipode of this Hopf algebra.

            If :meth:`.antipode_basis` is available, this constructs the
            antipode morphism from ``self`` to ``self`` by extending it by
            linearity. Otherwise, :meth:`self.antipode_by_coercion` is used,
            if available.

            EXAMPLES::

                sage: A = SteenrodAlgebra(7)                                            # needs sage.combinat sage.modules
                sage: a = A.an_element()                                                # needs sage.combinat sage.modules
                sage: a, A.antipode(a)                                                  # needs sage.combinat sage.modules
                (6 Q_1 Q_3 P(2,1), Q_1 Q_3 P(2,1))

            TESTS::

                sage: E.<x,y> = ExteriorAlgebra(QQ)                                     # needs sage.modules
                sage: [b.antipode() for b in E.basis()]                                 # needs sage.modules
                [1, -x, -y, x*y]
            """
