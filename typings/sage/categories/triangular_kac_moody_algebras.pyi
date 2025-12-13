from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.kac_moody_algebras import KacMoodyAlgebras as KacMoodyAlgebras
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class TriangularKacMoodyAlgebras(Category_over_base_ring):
    """
    Category of Kac-Moody algebras with a distinguished basis that
    respects the triangular decomposition.

    We require that the grading group is the root lattice of the
    appropriate Cartan type.
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.triangular_kac_moody_algebras import TriangularKacMoodyAlgebras
            sage: TriangularKacMoodyAlgebras(QQ).super_categories()
            [Join of Category of graded Lie algebras with basis over Rational Field
                 and Category of kac moody algebras over Rational Field]
        """
    class ParentMethods:
        def e(self, i=None):
            """
            Return the generators `e` of ``self``.

            INPUT:

            - ``i`` -- (optional) if specified, return just the
              generator `e_i`

            EXAMPLES::

                sage: L = lie_algebras.so(QQ, 5)                                        # needs sage.combinat sage.modules
                sage: L.e()                                                             # needs sage.combinat sage.modules
                Finite family {1: E[alpha[1]], 2: E[alpha[2]]}
                sage: L.e(1)                                                            # needs sage.combinat sage.modules
                E[alpha[1]]
            """
        def f(self, i=None):
            """
            Return the generators `f` of ``self``.

            INPUT:

            - ``i`` -- (optional) if specified, return just the
              generator `f_i`

            EXAMPLES::

                sage: L = lie_algebras.so(QQ, 5)                                        # needs sage.combinat sage.modules
                sage: L.f()                                                             # needs sage.combinat sage.modules
                Finite family {1: E[-alpha[1]], 2: E[-alpha[2]]}
                sage: L.f(1)                                                            # needs sage.combinat sage.modules
                E[-alpha[1]]
            """
        def verma_module(self, la, basis_key=None, **kwds):
            """
            Return the Verma module with highest weight ``la``
            over ``self``.

            INPUT:

            - ``basis_key`` -- (optional) a key function for the indexing
              set of the basis elements of ``self``

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = lie_algebras.sl(QQ, 3)
                sage: P = L.cartan_type().root_system().weight_lattice()
                sage: La = P.fundamental_weights()
                sage: M = L.verma_module(La[1] + La[2])
                sage: M
                Verma module with highest weight Lambda[1] + Lambda[2]
                 of Lie algebra of ['A', 2] in the Chevalley basis
            """
        def simple_module(self, la, basis_key=None, **kwds):
            """
            Return the simple module with highest weight ``la``
            over ``self``.

            INPUT:

            - ``la`` -- the weight
            - ``basis_key`` -- (optional) a key function for the indexing
              set of the basis elements of ``self``

            OUTPUT:

            If ``la`` is :meth:`Verma antidominant
            <sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.is_verma_dominant>`,
            then this returns the
            :class:`~sage.algebras.lie_algebras.verma_module.VermaModule`
            of highest weight ``la`` (which is simple and more efficient).
            Otherwise this returns a
            :class:`~sage.algebras.lie_algebras.bgg_dual_module.SimpleModule`.

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: g = lie_algebras.sl(QQ, 3)
                sage: P = g.cartan_type().root_system().weight_lattice()
                sage: La = P.fundamental_weights()
                sage: L = g.simple_module(La[1] + La[2])
                sage: L
                Simple module with highest weight Lambda[1] + Lambda[2]
                 of Lie algebra of ['A', 2] in the Chevalley basis
                sage: L = g.simple_module(-La[1] - La[2])
                sage: L
                Verma module with highest weight -Lambda[1] - Lambda[2]
                 of Lie algebra of ['A', 2] in the Chevalley basis
            """
    class ElementMethods:
        def part(self):
            """
            Return whether the element ``v`` is in the lower,
            zero, or upper part of ``self``.

            OUTPUT:

            `-1` if ``v`` is in the lower part, `0` if in the
            zero part, or `1` if in the upper part

            EXAMPLES::

                sage: # needs sage.combinat sage.modules
                sage: L = LieAlgebra(QQ, cartan_type='F4')
                sage: L.inject_variables()
                Defining e1, e2, e3, e4, f1, f2, f3, f4, h1, h2, h3, h4
                sage: e1.part()
                1
                sage: f4.part()
                -1
                sage: (h2 + h3).part()
                0
                sage: (f1.bracket(f2) + 4*f4).part()
                -1
                sage: (e1 + f1).part()
                Traceback (most recent call last):
                ...
                ValueError: element is not in one part
            """
    class FiniteDimensional(CategoryWithAxiom_over_base_ring):
        """
        Category of finite dimensional Kac-Moody algebras (which correspond
        to semisimple Lie algebras) with a distinguished basis that
        respects the triangular decomposition.
        """
        class ParentMethods:
            @lazy_attribute
            def transpose(self):
                """
                The transpose map of ``self``.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: g = LieAlgebra(QQ, cartan_type=['B', 2])
                    sage: g.transpose
                    Generic endomorphism of Lie algebra of ['B', 2] in the Chevalley basis
                """
        class ElementMethods:
            def transpose(self):
                """
                Return the transpose of ``self``.

                The transpose `\\tau` is the map that sends the root basis
                elements `e_{\\alpha} \\leftrightarrow e_{-\\alpha}` and fixes
                the Cartan subalgebra `h_{\\alpha}`. It is an anti-involution
                in the sense `[\\tau(a), \\tau(b)] = \\tau([b, a])`.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
                    sage: for b in g.basis():
                    ....:     for bp in g.basis():
                    ....:         a = g[b.transpose(), bp.transpose()]
                    ....:         ap = g[bp, b].transpose()
                    ....:         assert a == ap
                """
