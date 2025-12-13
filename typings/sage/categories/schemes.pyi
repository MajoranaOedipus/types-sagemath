from sage.categories.category import Category as Category
from sage.categories.category_types import Category_over_base as Category_over_base
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.fields import Fields as Fields
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.rings import Rings as Rings
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.lazy_import import lazy_import as lazy_import

class Schemes(Category):
    """
    The category of all schemes.

    EXAMPLES::

        sage: Schemes()
        Category of schemes

    ``Schemes`` can also be used to construct the category of schemes
    over a given base::

        sage: Schemes(Spec(ZZ))
        Category of schemes over Integer Ring

        sage: Schemes(ZZ)
        Category of schemes over Integer Ring

    .. TODO::

        Make ``Schemes()`` a singleton category (and remove
        :class:`Schemes` from the workaround in
        :meth:`.category_types.Category_over_base._test_category_over_bases`).

        This is currently incompatible with the dispatching below.

    TESTS::

        sage: TestSuite(Schemes()).run()

    Check that Hom sets of schemes are in the correct category::

        sage: Schemes().Homsets().super_categories()
        [Category of homsets]
    """
    @staticmethod
    def __classcall_private__(cls, X=None):
        """
        Implement the dispatching ``Schemes(ZZ)`` -> ``Schemes_over_base``.

        EXAMPLES::

            sage: Schemes()
            Category of schemes

            sage: Schemes(Spec(ZZ))
            Category of schemes over Integer Ring

            sage: Schemes(ZZ)
            Category of schemes over Integer Ring
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Schemes().super_categories()
            [Category of sets]
        """

class Schemes_over_base(Category_over_base):
    """
    The category of schemes over a given base scheme.

    EXAMPLES::

        sage: Schemes(Spec(ZZ))
        Category of schemes over Integer Ring

    TESTS::

        sage: C = Schemes(ZZ)
        sage: TestSuite(C).run()
    """
    def base_scheme(self):
        """
        EXAMPLES::

            sage: Schemes(Spec(ZZ)).base_scheme()
            Spectrum of Integer Ring
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Schemes(Spec(ZZ)).super_categories()
            [Category of schemes]
        """

class AbelianVarieties(Schemes_over_base):
    """
    The category of abelian varieties over a given field.

    EXAMPLES::

        sage: AbelianVarieties(QQ)
        Category of abelian varieties over Rational Field
        sage: AbelianVarieties(ZZ)
        Traceback (most recent call last):
        ...
        ValueError: category of abelian varieties is only defined over fields
    """
    def __init__(self, base) -> None:
        """
        Constructor for the ``AbelianVarieties`` category.

        EXAMPLES::

            sage: AbelianVarieties(QQ)
            Category of abelian varieties over Rational Field
            sage: AbelianVarieties(Spec(QQ))
            Category of abelian varieties over Rational Field
        """
    def base_scheme(self):
        """
        EXAMPLES::

            sage: Schemes(Spec(ZZ)).base_scheme()
            Spectrum of Integer Ring
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: AbelianVarieties(QQ).super_categories()
            [Category of schemes over Rational Field,
             Category of commutative additive groups]
        """
    class Homsets(HomsetsCategory):
        """
        Overloaded ``Homsets`` class to register the homset
        as an additive abelian group.

        EXAMPLES::

            sage: AbelianVarieties(QQ).Homsets().is_subcategory(CommutativeAdditiveGroups())
            True
        """
        def extra_super_categories(self):
            """
            Register the homset as an additive abelian group.

            EXAMPLES::

                sage: Hom(EllipticCurve(j=1), EllipticCurve(j=2)) in CommutativeAdditiveGroups()
                True
            """
        class Endset(CategoryWithAxiom):
            """
            Overloaded ``Endset`` class to register the endset
            as a ring.

            sage: AbelianVarieties(QQ).Endsets().is_subcategory(Rings())
            True
            """
            def extra_super_categories(self):
                """
                Register the endset as a ring.

                EXAMPLES::

                    sage: End(EllipticCurve(j=1)) in Rings()
                    True
                """

class Jacobians(Schemes_over_base):
    """
    The category of Jacobians attached to curves or function fields.

    EXAMPLES::

        sage: Jacobians(QQ)
        Category of Jacobians over Rational Field

    TESTS::

        sage: TestSuite(Jacobians(QQ)).run()
    """
    def __init__(self, base) -> None:
        """
        Constructor of this category.

        EXAMPLES::

            sage: Jacobians(QQ)
            Category of Jacobians over Rational Field
            sage: Jacobians(Spec(QQ))
            Category of Jacobians over Rational Field
        """
    def base_scheme(self):
        """
        Return the base scheme of this Jacobians category.

        EXAMPLES::

            sage: Jacobians(QQ).base_scheme()
            Spectrum of Rational Field
        """
    def super_categories(self):
        """
        Return the super categories of this Jacobians category.

        EXAMPLES::

            sage: Jacobians(QQ).super_categories()
            [Category of abelian varieties over Rational Field]
        """
    class ParentMethods:
        @abstract_method
        def base_curve(self) -> None:
            """
            Return the curve to which this Jacobian is attached.

            EXAMPLES::

                sage: # needs sage.rings.function_field
                sage: K.<x> = FunctionField(GF(2))
                sage: J = K.jacobian()
                sage: J.base_curve()
                Rational function field in x over Finite Field of size 2
            """
