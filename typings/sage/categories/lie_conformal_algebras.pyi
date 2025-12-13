from _typeshed import Incomplete
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.lambda_bracket_algebras import LambdaBracketAlgebras as LambdaBracketAlgebras
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class LieConformalAlgebras(Category_over_base_ring):
    """
    The category of Lie conformal algebras.

    This is the base category for all Lie conformal algebras.
    Subcategories with axioms are ``FinitelyGenerated`` and
    ``WithBasis``. A *finitely generated* Lie conformal algebra is a
    Lie conformal algebra over `R` which is finitely generated as an
    `R[T]`-module. A Lie conformal algebra *with basis* is one with a
    preferred basis as an `R`-module.

    EXAMPLES:

    The base category::

        sage: C = LieConformalAlgebras(QQ); C
        Category of Lie conformal algebras over Rational Field
        sage: C.is_subcategory(VectorSpaces(QQ))
        True

    Some subcategories::

        sage: LieConformalAlgebras(QQbar).FinitelyGenerated().WithBasis()               # needs sage.rings.number_field
        Category of finitely generated Lie conformal algebras with basis
         over Algebraic Field

    In addition we support functorial constructions ``Graded`` and
    ``Super``. These functors commute::

        sage: CGS = LieConformalAlgebras(AA).Graded().Super(); CGS                      # needs sage.rings.number_field
        Category of H-graded super Lie conformal algebras over Algebraic Real Field
        sage: CGS is LieConformalAlgebras(AA).Super().Graded()                          # needs sage.rings.number_field
        True

    That is, we only consider gradings on super Lie conformal algebras
    that are compatible with the `\\ZZ/2\\ZZ` grading.

    The base ring needs to be a commutative ring::

        sage: LieConformalAlgebras(QuaternionAlgebra(2))                                # needs sage.combinat sage.modules
        Traceback (most recent call last):
        ValueError: base must be a commutative ring
        got Quaternion Algebra (-1, -1) with base ring Rational Field
    """
    @cached_method
    def super_categories(self):
        """
        The list of super categories of this category.

        EXAMPLES::

            sage: C = LieConformalAlgebras(QQ)
            sage: C.super_categories()
            [Category of Lambda bracket algebras over Rational Field]
            sage: C = LieConformalAlgebras(QQ).FinitelyGenerated(); C
            Category of finitely generated Lie conformal algebras over Rational Field
            sage: C.super_categories()
            [Category of finitely generated lambda bracket algebras over Rational Field,
             Category of Lie conformal algebras over Rational Field]
            sage: C.all_super_categories()
            [Category of finitely generated Lie conformal algebras over Rational Field,
             Category of finitely generated lambda bracket algebras over Rational Field,
             Category of Lie conformal algebras over Rational Field,
             Category of Lambda bracket algebras over Rational Field,
             Category of vector spaces over Rational Field,
             Category of modules over Rational Field,
             Category of bimodules over Rational Field on the left and Rational Field on the right,
             Category of right modules over Rational Field,
             Category of left modules over Rational Field,
             Category of commutative additive groups,
             Category of additive groups,
             Category of additive inverse additive unital additive magmas,
             Category of commutative additive monoids,
             Category of additive monoids,
             Category of additive unital additive magmas,
             Category of commutative additive semigroups,
             Category of additive commutative additive magmas,
             Category of additive semigroups,
             Category of additive magmas,
             Category of sets,
             Category of sets with partial maps,
             Category of objects]
        """
    def example(self):
        """
        An example of parent in this category.

        EXAMPLES::

            sage: LieConformalAlgebras(QQ).example()                                    # needs sage.combinat sage.modules
            The Virasoro Lie conformal algebra over Rational Field
        """
    class ParentMethods: ...
    class ElementMethods:
        def is_even_odd(self):
            """
            Return ``0`` if this element is *even* and ``1`` if it is
            *odd*.

            .. NOTE::

                This method returns ``0`` by default since every Lie
                conformal algebra can be thought as a purely even Lie
                conformal algebra. In order to
                implement a super Lie conformal algebra, the user
                needs to implement this method.

            EXAMPLES::

                sage: R = lie_conformal_algebras.NeveuSchwarz(QQ)                       # needs sage.combinat sage.modules
                sage: R.inject_variables()                                              # needs sage.combinat sage.modules
                Defining L, G, C
                sage: G.is_even_odd()                                                   # needs sage.combinat sage.modules
                1
            """
    Graded: Incomplete
    Super: Incomplete
    WithBasis: Incomplete
    FinitelyGeneratedAsLambdaBracketAlgebra: Incomplete
