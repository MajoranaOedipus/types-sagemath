from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras

class FiniteDimensionalNilpotentLieAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    Category of finite dimensional nilpotent Lie algebras with basis.

    TESTS::

        sage: C1 = LieAlgebras(QQ).FiniteDimensional().WithBasis().Nilpotent()
        sage: C2 = LieAlgebras(QQ).FiniteDimensional().Nilpotent().WithBasis()
        sage: C3 = LieAlgebras(QQ).Nilpotent().FiniteDimensional().WithBasis()
        sage: C4 = LieAlgebras(QQ).Nilpotent().WithBasis().FiniteDimensional()
        sage: C5 = LieAlgebras(QQ).WithBasis().Nilpotent().FiniteDimensional()
        sage: C6 = LieAlgebras(QQ).WithBasis().FiniteDimensional().Nilpotent()
        sage: C1 is C2
        True
        sage: C2 is C3
        True
        sage: C3 is C4
        True
        sage: C4 is C5
        True
        sage: C5 is C6
        True
        sage: TestSuite(C1).run()
    """
    class ParentMethods:
        def lie_group(self, name: str = 'G', **kwds):
            """
            Return the Lie group associated to ``self``.

            INPUT:

            - ``name`` -- string (default: ``'G'``);
              the name (symbol) given to the Lie group

            EXAMPLES:

            We define the Heisenberg group::

                sage: L = lie_algebras.Heisenberg(QQ, 1)                                # needs sage.combinat sage.modules
                sage: G = L.lie_group('G'); G                                           # needs sage.combinat sage.modules sage.symbolic
                Lie group G of Heisenberg algebra of rank 1 over Rational Field

            We test multiplying elements of the group::

                sage: # needs sage.combinat sage.modules sage.symbolic
                sage: p, q, z = L.basis()
                sage: g = G.exp(p); g
                exp(p1)
                sage: h = G.exp(q); h
                exp(q1)
                sage: g * h
                exp(p1 + q1 + 1/2*z)

            We extend an element of the Lie algebra to a left-invariant
            vector field::

                sage: X = G.left_invariant_extension(2*p + 3*q, name='X'); X            # needs sage.combinat sage.modules sage.symbolic
                Vector field X on the Lie group G of
                 Heisenberg algebra of rank 1 over Rational Field
                sage: X.at(G.one()).display()                                           # needs sage.combinat sage.modules sage.symbolic
                X = 2 ∂/∂x_0 + 3 ∂/∂x_1
                sage: X.display()                                                       # needs sage.combinat sage.modules sage.symbolic
                X = 2 ∂/∂x_0 + 3 ∂/∂x_1 + (3/2*x_0 - x_1) ∂/∂x_2

            .. SEEALSO::

                :class:`~sage.groups.lie_gps.nilpotent_lie_group.NilpotentLieGroup`
            """
        def step(self):
            """
            Return the nilpotency step of ``self``.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, {('X','Y'): {'Z': 1}}, nilpotent=True)
                sage: L.step()
                2
                sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
                sage: LieAlgebra(QQ, sc, nilpotent=True).step()
                3
            """
        def is_nilpotent(self):
            """
            Return ``True`` since ``self`` is nilpotent.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, {('x','y'): {'z': 1}}, nilpotent=True)         # needs sage.combinat sage.modules
                sage: L.is_nilpotent()                                                  # needs sage.combinat sage.modules
                True
            """
