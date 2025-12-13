from sage.categories.category import Category as Category
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory

class GradedModulesCategory(RegressiveCovariantConstructionCategory, Category_over_base_ring):
    def __init__(self, base_category) -> None:
        """
        EXAMPLES::

            sage: C = GradedAlgebras(QQ)
            sage: C
            Category of graded algebras over Rational Field
            sage: C.base_category()
            Category of algebras over Rational Field
            sage: sorted(C.super_categories(), key=str)
            [Category of filtered algebras over Rational Field,
             Category of graded vector spaces over Rational Field]

            sage: AlgebrasWithBasis(QQ).Graded().base_ring()
            Rational Field
            sage: GradedHopfAlgebrasWithBasis(QQ).base_ring()
            Rational Field

        TESTS::

            sage: GradedModules(ZZ)
            Category of graded modules over Integer Ring
            sage: Modules(ZZ).Graded()
            Category of graded modules over Integer Ring
            sage: GradedModules(ZZ) is Modules(ZZ).Graded()
            True
        """
    @classmethod
    def default_super_categories(cls, category, *args):
        """
        Return the default super categories of ``category.Graded()``.

        Mathematical meaning: every graded object (module, algebra,
        etc.) is a filtered object with the (implicit) filtration
        defined by `F_i = \\bigoplus_{j \\leq i} G_j`.

        INPUT:

        - ``cls`` -- the class ``GradedModulesCategory``
        - ``category`` -- a category

        OUTPUT: a (join) category

        In practice, this returns ``category.Filtered()``, joined
        together with the result of the method
        :meth:`RegressiveCovariantConstructionCategory.default_super_categories() <sage.categories.covariant_functorial_construction.RegressiveCovariantConstructionCategory.default_super_categories>`
        (that is the join of ``category.Filtered()`` and ``cat`` for
        each ``cat`` in the super categories of ``category``).

        EXAMPLES:

        Consider ``category=Algebras()``, which has ``cat=Modules()``
        as super category. Then, a grading of an algebra `G`
        is also a filtration of `G`::

            sage: Algebras(QQ).Graded().super_categories()
            [Category of filtered algebras over Rational Field,
             Category of graded vector spaces over Rational Field]

        This resulted from the following call::

            sage: sage.categories.graded_modules.GradedModulesCategory.default_super_categories(Algebras(QQ))
            Join of Category of filtered algebras over Rational Field
             and Category of graded vector spaces over Rational Field
        """

class GradedModules(GradedModulesCategory):
    """
    The category of graded modules.

    We consider every graded module `M = \\bigoplus_i M_i` as a
    filtered module under the (natural) filtration given by

    .. MATH::

        F_i = \\bigoplus_{j < i} M_j.

    EXAMPLES::

        sage: GradedModules(ZZ)
        Category of graded modules over Integer Ring
        sage: GradedModules(ZZ).super_categories()
        [Category of filtered modules over Integer Ring]

    The category of graded modules defines the graded structure which
    shall be preserved by morphisms::

        sage: Modules(ZZ).Graded().additional_structure()
        Category of graded modules over Integer Ring

    TESTS::

        sage: TestSuite(GradedModules(ZZ)).run()
    """
    class ParentMethods: ...
    class ElementMethods: ...
