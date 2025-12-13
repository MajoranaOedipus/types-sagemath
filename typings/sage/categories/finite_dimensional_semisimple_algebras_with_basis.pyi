from sage.categories.algebras import Algebras as Algebras
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.semisimple_algebras import SemisimpleAlgebras as SemisimpleAlgebras
from sage.misc.cachefunc import cached_method as cached_method

class FiniteDimensionalSemisimpleAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of finite dimensional semisimple algebras with a distinguished basis.

    EXAMPLES::

        sage: from sage.categories.finite_dimensional_semisimple_algebras_with_basis import FiniteDimensionalSemisimpleAlgebrasWithBasis
        sage: C = FiniteDimensionalSemisimpleAlgebrasWithBasis(QQ); C
        Category of finite dimensional semisimple algebras with basis over Rational Field

    This category is best constructed as::

        sage: D = Algebras(QQ).Semisimple().FiniteDimensional().WithBasis(); D
        Category of finite dimensional semisimple algebras with basis over Rational Field
        sage: D is C
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    class ParentMethods:
        def radical_basis(self, **keywords):
            """
            Return a basis of the Jacobson radical of this algebra.

            - ``keywords`` -- for compatibility; ignored

            OUTPUT: the empty list since this algebra is semisimple

            EXAMPLES::

                sage: A = SymmetricGroup(4).algebra(QQ)                                 # needs sage.combinat sage.groups sage.modules
                sage: A.radical_basis()                                                 # needs sage.combinat sage.groups sage.modules
                ()

            TESTS::

                sage: A.radical_basis.__module__                                        # needs sage.combinat sage.groups sage.modules
                'sage.categories.finite_dimensional_semisimple_algebras_with_basis'
            """
        @cached_method
        def central_orthogonal_idempotents(self):
            """
            Return a maximal list of central orthogonal
            idempotents of ``self``.

            .. TODO::

                The implementation assumes that the algebra
                is split over its base field.

            *Central orthogonal idempotents* of an algebra `A`
            are idempotents `(e_1, \\ldots, e_n)` in the center
            of `A` such that `e_i e_j = 0` whenever `i \\neq j`.

            With the maximality condition, they sum up to `1`
            and are uniquely determined (up to order).

            EXAMPLES:

            For the algebra of the (abelian) alternating group `A_3`,
            we recover three idempotents corresponding to the three
            one-dimensional representations `V_i` on which `(1,2,3)`
            acts on `V_i` as multiplication by the `i`-th power of a
            cube root of unity::

                sage: # needs sage.groups sage.rings.number_field
                sage: R = CyclotomicField(3)
                sage: A3 = AlternatingGroup(3).algebra(R)
                sage: idempotents = A3.central_orthogonal_idempotents()
                sage: idempotents
                (1/3*() + 1/3*(1,2,3) + 1/3*(1,3,2),
                 1/3*() - (1/3*zeta3+1/3)*(1,2,3) - (-1/3*zeta3)*(1,3,2),
                 1/3*() - (-1/3*zeta3)*(1,2,3) - (1/3*zeta3+1/3)*(1,3,2))
                sage: A3.is_identity_decomposition_into_orthogonal_idempotents(idempotents)
                True

            For the semisimple quotient of a quiver algebra,
            we recover the vertices of the quiver::

                sage: # needs sage.graphs sage.modules sage.rings.number_field
                sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
                An example of a finite dimensional algebra with basis:
                the path algebra of the Kronecker quiver (containing
                the arrows a:x->y and b:x->y) over Rational Field
                sage: Aquo = A.semisimple_quotient()
                sage: Aquo.central_orthogonal_idempotents()
                (B['x'], B['y'])
            """
    class Commutative(CategoryWithAxiom_over_base_ring):
        class ParentMethods:
            @cached_method
            def central_orthogonal_idempotents(self):
                """
                Return the central orthogonal idempotents of
                this semisimple commutative algebra.

                Those idempotents form a maximal decomposition
                of the identity into primitive orthogonal
                idempotents.

                .. TODO::

                    The implementation assumes that the algebra
                    is split over its base field.

                OUTPUT: list of orthogonal idempotents of ``self``

                EXAMPLES::

                    sage: # needs sage.combinat sage.groups sage.modules
                    sage: A4 = SymmetricGroup(4).algebra(QQ)
                    sage: Z4 = A4.center()
                    sage: idempotents = Z4.central_orthogonal_idempotents()
                    sage: idempotents
                    (1/24*B[0] + 1/24*B[1] + 1/24*B[2] + 1/24*B[3] + 1/24*B[4],
                     3/8*B[0] + 1/8*B[1] - 1/8*B[2] - 1/8*B[4],
                     1/6*B[0] + 1/6*B[2] - 1/12*B[3],
                     3/8*B[0] - 1/8*B[1] - 1/8*B[2] + 1/8*B[4],
                     1/24*B[0] - 1/24*B[1] + 1/24*B[2] + 1/24*B[3] - 1/24*B[4])

                Lifting those idempotents from the center, we
                recognize among them the sum and alternating
                sum of all permutations::

                    sage: [e.lift() for e in idempotents]                               # needs sage.combinat sage.groups sage.modules
                    [1/24*() + 1/24*(3,4) + 1/24*(2,3) + 1/24*(2,3,4) + 1/24*(2,4,3)
                     + 1/24*(2,4) + 1/24*(1,2) + 1/24*(1,2)(3,4) + 1/24*(1,2,3)
                     + 1/24*(1,2,3,4) + 1/24*(1,2,4,3) + 1/24*(1,2,4) + 1/24*(1,3,2)
                     + 1/24*(1,3,4,2) + 1/24*(1,3) + 1/24*(1,3,4) + 1/24*(1,3)(2,4)
                     + 1/24*(1,3,2,4) + 1/24*(1,4,3,2) + 1/24*(1,4,2) + 1/24*(1,4,3)
                     + 1/24*(1,4) + 1/24*(1,4,2,3) + 1/24*(1,4)(2,3),
                     ...,
                     1/24*() - 1/24*(3,4) - 1/24*(2,3) + 1/24*(2,3,4) + 1/24*(2,4,3)
                     - 1/24*(2,4) - 1/24*(1,2) + 1/24*(1,2)(3,4) + 1/24*(1,2,3)
                     - 1/24*(1,2,3,4) - 1/24*(1,2,4,3) + 1/24*(1,2,4) + 1/24*(1,3,2)
                     - 1/24*(1,3,4,2) - 1/24*(1,3) + 1/24*(1,3,4) + 1/24*(1,3)(2,4)
                     - 1/24*(1,3,2,4) - 1/24*(1,4,3,2) + 1/24*(1,4,2) + 1/24*(1,4,3)
                     - 1/24*(1,4) - 1/24*(1,4,2,3) + 1/24*(1,4)(2,3)]

                We check that they indeed form a decomposition
                of the identity of `Z_4` into orthogonal idempotents::

                    sage: # needs sage.combinat sage.groups sage.modules
                    sage: Z4.is_identity_decomposition_into_orthogonal_idempotents(idempotents)
                    True
                """
