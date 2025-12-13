from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.misc.cachefunc import cached_method as cached_method

class FiniteDimensionalGradedLieAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    Category of finite dimensional graded Lie algebras with a basis.

    A grading of a Lie algebra `\\mathfrak{g}` is a direct sum decomposition
    `\\mathfrak{g} = \\bigoplus_{i} V_i` such that `[V_i,V_j] \\subset V_{i+j}`.

    EXAMPLES::

        sage: C = LieAlgebras(ZZ).WithBasis().FiniteDimensional().Graded(); C
        Category of finite dimensional graded Lie algebras with basis over Integer Ring
        sage: C.super_categories()
        [Category of graded Lie algebras with basis over Integer Ring,
         Category of finite dimensional filtered modules with basis over Integer Ring,
         Category of finite dimensional Lie algebras with basis over Integer Ring]

        sage: C is LieAlgebras(ZZ).WithBasis().FiniteDimensional().Graded()
        True

    TESTS::

        sage: C = LieAlgebras(QQ).FiniteDimensional().WithBasis().Graded()
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        @cached_method
        def homogeneous_component_as_submodule(self, d):
            """
            Return the ``d``-th homogeneous component of ``self``
            as a submodule.

            EXAMPLES::

                sage: C = LieAlgebras(QQ).WithBasis().Graded()
                sage: C = C.FiniteDimensional().Stratified().Nilpotent()
                sage: L = LieAlgebra(QQ, {('x','y'): {'z': 1}},                         # needs sage.combinat sage.modules
                ....:                     nilpotent=True, category=C)
                sage: L.homogeneous_component_as_submodule(2)                           # needs sage.combinat sage.modules
                Sparse vector space of degree 3 and dimension 1 over Rational Field
                Basis matrix:
                [0 0 1]
            """
    class Stratified(CategoryWithAxiom_over_base_ring):
        """
        Category of finite dimensional stratified Lie algebras with a basis.

        A stratified Lie algebra is a graded Lie algebra that is generated
        as a Lie algebra by its homogeneous component of degree 1. That is
        to say, for a graded Lie algebra `L = \\bigoplus_{k=1}^M L_k`,
        we have `L_{k+1} = [L_1, L_k]`.

        EXAMPLES::

            sage: C = LieAlgebras(QQ).WithBasis().Graded().Stratified().FiniteDimensional()
            sage: C
            Category of finite dimensional stratified Lie algebras with basis over Rational Field

        A finite-dimensional stratified Lie algebra is nilpotent::

            sage: C is C.Nilpotent()
            True

        TESTS::

            sage: C = LieAlgebras(QQ).WithBasis().Graded().FiniteDimensional().Stratified()
            sage: TestSuite(C).run()
        """
        class ParentMethods:
            def degree_on_basis(self, m):
                """
                Return the degree of the basis element indexed by ``m``.

                If the degrees of the basis elements are not defined,
                they will be computed. By assumption the stratification
                `L_1 \\oplus \\cdots \\oplus L_s` of ``self`` is such that each
                component `L_k` is spanned by some subset of the basis.

                The degree of a basis element `X` is therefore the largest
                index `k` such that `X \\in L_k \\oplus \\cdots \\oplus L_s`. The
                space  `L_k \\oplus \\cdots \\oplus L_s` is by assumption the
                `k`-th term of the lower central series.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: C = LieAlgebras(QQ).WithBasis().Graded()
                    sage: C = C.FiniteDimensional().Stratified().Nilpotent()
                    sage: sc = {('X','Y'): {'Z': 1}}
                    sage: L.<X,Y,Z> = LieAlgebra(QQ, sc, nilpotent=True, category=C)
                    sage: L.degree_on_basis(X.leading_support())
                    1
                    sage: X.degree()
                    1
                    sage: Y.degree()
                    1
                    sage: L[X, Y]
                    Z
                    sage: Z.degree()
                    2
                """
