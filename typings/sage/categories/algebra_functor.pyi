from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.covariant_functorial_construction import CovariantConstructionCategory as CovariantConstructionCategory, CovariantFunctorialConstruction as CovariantFunctorialConstruction, FunctorialConstructionCategory as FunctorialConstructionCategory
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor

class AlgebraFunctor(CovariantFunctorialConstruction):
    """
    For a fixed ring, a functor sending a group/...  to the
    corresponding group/...  algebra.

    EXAMPLES::

        sage: from sage.categories.algebra_functor import AlgebraFunctor
        sage: F = AlgebraFunctor(QQ); F
        The algebra functorial construction
        sage: F(DihedralGroup(3))
        Algebra of Dihedral group of order 6 as a permutation group
                over Rational Field
    """
    def __init__(self, base_ring) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.algebra_functor import AlgebraFunctor
            sage: F = AlgebraFunctor(QQ); F
            The algebra functorial construction
            sage: TestSuite(F).run()
        """
    def base_ring(self):
        """
        Return the base ring for this functor.

        EXAMPLES::

            sage: from sage.categories.algebra_functor import AlgebraFunctor
            sage: AlgebraFunctor(QQ).base_ring()
            Rational Field
        """
    def __call__(self, G, category=None):
        """
        Return the algebra of ``G``.

        See :ref:`sage.categories.algebra_functor` for details.

        INPUT:

        - ``G`` -- a group
        - ``category`` -- a category, or ``None``

        EXAMPLES::

            sage: from sage.categories.algebra_functor import AlgebraFunctor
            sage: F = AlgebraFunctor(QQ)
            sage: G = DihedralGroup(3)
            sage: A = F(G, category=Monoids()); A
            Algebra of Dihedral group of order 6 as a permutation group
                    over Rational Field
            sage: A.category()
            Category of finite dimensional monoid algebras over Rational Field
        """

class GroupAlgebraFunctor(ConstructionFunctor):
    """
    For a fixed group, a functor sending a commutative ring to the
    corresponding group algebra.

    INPUT:

    - ``group`` -- the group associated to each group algebra under
      consideration

    EXAMPLES::

        sage: from sage.categories.algebra_functor import GroupAlgebraFunctor
        sage: F = GroupAlgebraFunctor(KleinFourGroup()); F
        GroupAlgebraFunctor
        sage: A = F(QQ); A
        Algebra of The Klein 4 group of order 4, as a permutation group over Rational Field

    TESTS::

        sage: loads(dumps(F)) == F
        True
        sage: A is KleinFourGroup().algebra(QQ)
        True
    """
    def __init__(self, group) -> None:
        """
        See :class:`GroupAlgebraFunctor` for full documentation.

        EXAMPLES::

            sage: from sage.categories.algebra_functor import GroupAlgebraFunctor
            sage: GroupAlgebra(SU(2, GF(4, 'a')), IntegerModRing(12)).category()        # needs sage.rings.finite_rings
            Category of finite group algebras over Ring of integers modulo 12
        """
    def group(self):
        """
        Return the group which is associated to this functor.

        EXAMPLES::

            sage: from sage.categories.algebra_functor import GroupAlgebraFunctor
            sage: GroupAlgebraFunctor(CyclicPermutationGroup(17)).group() == CyclicPermutationGroup(17)
            True
        """

class AlgebrasCategory(CovariantConstructionCategory, Category_over_base_ring):
    """
    An abstract base class for categories of monoid algebras,
    groups algebras, and the like.

    .. SEEALSO::

        - :meth:`Sets.ParentMethods.algebra`
        - :meth:`Sets.SubcategoryMethods.Algebras`
        - :class:`~sage.categories.covariant_functorial_construction.CovariantFunctorialConstruction`

    INPUT:

    - ``base_ring`` -- a ring

    EXAMPLES::

        sage: C = Groups().Algebras(QQ); C
        Category of group algebras over Rational Field
        sage: C = Monoids().Algebras(QQ); C
        Category of monoid algebras over Rational Field

        sage: C._short_name()
        'Algebras'
        sage: latex(C) # todo: improve that
        \\mathbf{Algebras}(\\mathbf{Monoids})
    """
    @staticmethod
    def __classcall__(cls, category=None, R=None):
        """
        Make ``CatAlgebras(**)`` a shorthand for ``Cat().Algebras(**)``.

        EXAMPLES::

            sage: GradedModules(ZZ)   # indirect doctest
            Category of graded modules over Integer Ring
            sage: Modules(ZZ).Graded()
            Category of graded modules over Integer Ring
            sage: Modules.Graded(ZZ)
            Category of graded modules over Integer Ring
            sage: GradedModules(ZZ) is Modules(ZZ).Graded()
            True

        .. SEEALSO:: :meth:`_base_category_class`

        .. TODO::

            The logic is very similar to the default implementation
            :class:`FunctorialConstructionCategory.__classcall__`;
            the only difference is whether the additional arguments
            should be passed to ``Cat`` or to the construction.

            Find a way to refactor this to avoid the duplication.
        """
    class ParentMethods:
        def coproduct_on_basis(self, g):
            """
            Return the coproduct of the element ``g`` of the basis.

            Each basis element ``g`` is group-like. This method is
            used to compute the coproduct of any element.

            EXAMPLES::

                sage: # needs sage.combinat
                sage: PF = NonDecreasingParkingFunctions(4)
                sage: A = PF.algebra(ZZ); A
                Algebra of Non-decreasing parking functions of size 4 over Integer Ring
                sage: g = PF.an_element(); g
                [1, 1, 1, 1]
                sage: A.coproduct_on_basis(g)
                B[[1, 1, 1, 1]] # B[[1, 1, 1, 1]]
                sage: a = A.an_element(); a
                2*B[[1, 1, 1, 1]] + 2*B[[1, 1, 1, 2]] + 3*B[[1, 1, 1, 3]]
                sage: a.coproduct()
                2*B[[1, 1, 1, 1]] # B[[1, 1, 1, 1]] +
                2*B[[1, 1, 1, 2]] # B[[1, 1, 1, 2]] +
                3*B[[1, 1, 1, 3]] # B[[1, 1, 1, 3]]
            """
