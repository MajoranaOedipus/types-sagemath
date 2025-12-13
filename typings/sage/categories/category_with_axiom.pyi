from _typeshed import Incomplete
from sage.categories.category import Category as Category
from sage.categories.category_cy_helper import AxiomContainer as AxiomContainer, canonicalize_axioms as canonicalize_axioms
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.call import call_method as call_method
from sage.misc.lazy_attribute import lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.structure.dynamic_class import DynamicMetaclass as DynamicMetaclass

all_axioms: Incomplete

def uncamelcase(s, separator: str = ' '):
    '''
    EXAMPLES::

        sage: sage.categories.category_with_axiom.uncamelcase("FiniteDimensionalAlgebras")
        \'finite dimensional algebras\'
        sage: sage.categories.category_with_axiom.uncamelcase("JTrivialMonoids")
        \'j trivial monoids\'
        sage: sage.categories.category_with_axiom.uncamelcase("FiniteDimensionalAlgebras", "_")
        \'finite_dimensional_algebras\'
    '''
def base_category_class_and_axiom(cls):
    """
    Try to deduce the base category and the axiom from the name of ``cls``.

    The heuristic is to try to decompose the name as the concatenation
    of the name of a category and the name of an axiom, and looking up
    that category in the standard location (i.e. in
    :mod:`sage.categories.hopf_algebras` for :class:`HopfAlgebras`,
    and in :mod:`sage.categories.sets_cat` as a special case
    for :class:`Sets`).

    If the heuristic succeeds, the result is guaranteed to be
    correct. Otherwise, an error is raised.

    EXAMPLES::

        sage: from sage.categories.category_with_axiom import base_category_class_and_axiom, CategoryWithAxiom
        sage: base_category_class_and_axiom(FiniteSets)
        (<class 'sage.categories.sets_cat.Sets'>, 'Finite')
        sage: Sets.Finite
        <class 'sage.categories.finite_sets.FiniteSets'>
        sage: base_category_class_and_axiom(Sets.Finite)
        (<class 'sage.categories.sets_cat.Sets'>, 'Finite')

        sage: base_category_class_and_axiom(FiniteDimensionalHopfAlgebrasWithBasis)
        (<class 'sage.categories.hopf_algebras_with_basis.HopfAlgebrasWithBasis'>,
         'FiniteDimensional')

        sage: base_category_class_and_axiom(HopfAlgebrasWithBasis)
        (<class 'sage.categories.hopf_algebras.HopfAlgebras'>, 'WithBasis')

    Along the way, this does some sanity checks::

        sage: class FacadeSemigroups(CategoryWithAxiom):
        ....:     pass
        sage: base_category_class_and_axiom(FacadeSemigroups)
        Traceback (most recent call last):
        ...
        AssertionError: Missing (lazy import) link
        for <class 'sage.categories.semigroups.Semigroups'>
        to <class '__main__.FacadeSemigroups'> for axiom Facade?

        sage: Semigroups.Facade = FacadeSemigroups
        sage: base_category_class_and_axiom(FacadeSemigroups)
        (<class 'sage.categories.semigroups.Semigroups'>, 'Facade')

    .. NOTE::

        In the following example, we could possibly retrieve ``Sets``
        from the class name. However this cannot be implemented
        robustly until :issue:`9107` is fixed. Anyway this feature
        has not been needed so far::

            sage: Sets.Infinite
            <class 'sage.categories.sets_cat.Sets.Infinite'>
            sage: base_category_class_and_axiom(Sets.Infinite)
            Traceback (most recent call last):
            ...
            TypeError: Could not retrieve the base category class and axiom
            for <class 'sage.categories.sets_cat.Sets.Infinite'>.
            ...
    """
@cached_function
def axiom_of_nested_class(cls, nested_cls):
    """
    Given a class and a nested axiom class, return the axiom.

    EXAMPLES:

    This uses some heuristics like checking if the nested_cls carries
    the name of the axiom, or is built by appending or prepending the
    name of the axiom to that of the class::

        sage: from sage.categories.category_with_axiom import TestObjects, axiom_of_nested_class
        sage: axiom_of_nested_class(TestObjects, TestObjects.FiniteDimensional)
        'FiniteDimensional'
        sage: axiom_of_nested_class(TestObjects.FiniteDimensional,
        ....:                       TestObjects.FiniteDimensional.Finite)
        'Finite'
        sage: axiom_of_nested_class(Sets, FiniteSets)
        'Finite'
        sage: axiom_of_nested_class(Algebras, AlgebrasWithBasis)
        'WithBasis'

    In all other cases, the nested class should provide an attribute
    ``_base_category_class_and_axiom``::

        sage: Semigroups._base_category_class_and_axiom
        (<class 'sage.categories.magmas.Magmas'>, 'Associative')
        sage: axiom_of_nested_class(Magmas, Semigroups)
        'Associative'
    """

class CategoryWithAxiom(Category):
    """
    An abstract class for categories obtained by adding an axiom
    to a base category.

    See the :mod:`category primer <sage.categories.primer>`, and in
    particular its :ref:`section about axioms <category-primer-axioms>`
    for an introduction to axioms, and :class:`CategoryWithAxiom` for
    how to implement axioms and the documentation of the axiom
    infrastructure.

    .. automethod:: CategoryWithAxiom.__classcall__
    .. automethod:: CategoryWithAxiom.__classget__
    .. automethod:: CategoryWithAxiom.__init__
    .. automethod:: CategoryWithAxiom._repr_object_names
    .. automethod:: CategoryWithAxiom._repr_object_names_static
    .. automethod:: CategoryWithAxiom._test_category_with_axiom
    .. automethod:: CategoryWithAxiom._without_axioms
    """
    @staticmethod
    def __classcall__(cls, *args, **options):
        '''
        Make ``FoosBar(**)`` an alias for ``Foos(**)._with_axiom("Bar")``.

        EXAMPLES::

            sage: FiniteGroups()
            Category of finite groups
            sage: ModulesWithBasis(ZZ)
            Category of modules with basis over Integer Ring
            sage: AlgebrasWithBasis(QQ)
            Category of algebras with basis over Rational Field

        This is relevant when e.g. ``Foos(**)`` does some non trivial
        transformations::

            sage: Modules(QQ) is VectorSpaces(QQ)
            True
            sage: type(Modules(QQ))
            <class \'sage.categories.vector_spaces.VectorSpaces_with_category\'>

            sage: ModulesWithBasis(QQ) is VectorSpaces(QQ).WithBasis()
            True
            sage: type(ModulesWithBasis(QQ))
            <class \'sage.categories.vector_spaces.VectorSpaces.WithBasis_with_category\'>
        '''
    @staticmethod
    def __classget__(cls, base_category, base_category_class):
        """
        Implement the binding behavior for categories with axioms.

        This method implements a binding behavior on category with
        axioms so that, when a category ``Cs`` implements an axiom
        ``A`` with a nested class ``Cs.A``, the expression ``Cs().A``
        evaluates to the method defining the axiom ``A`` and not the
        nested class. See `those design notes
        <category-with-axiom-design>`_ for the rationale behind this
        behavior.

        EXAMPLES::

            sage: Sets().Infinite()
            Category of infinite sets
            sage: Sets().Infinite
            Cached version of <function ...Infinite at ...>
            sage: Sets().Infinite.f == Sets.SubcategoryMethods.Infinite.f
            True

        We check that this also works when the class is implemented in
        a separate file, and lazy imported::

            sage: Sets().Finite
            Cached version of <function ...Finite at ...>

        There is no binding behavior when accessing ``Finite`` or
        ``Infinite`` from the class of the category instead of the
        category itself::

            sage: Sets.Finite
            <class 'sage.categories.finite_sets.FiniteSets'>
            sage: Sets.Infinite
            <class 'sage.categories.sets_cat.Sets.Infinite'>

        This method also initializes the attribute
        ``_base_category_class_and_axiom`` if not already set::

            sage: Sets.Infinite._base_category_class_and_axiom
            (<class 'sage.categories.sets_cat.Sets'>, 'Infinite')
            sage: Sets.Infinite._base_category_class_and_axiom_origin
            'set by __classget__'
        """
    def __init__(self, base_category) -> None:
        """
        TESTS::

            sage: C = Sets.Finite(); C
            Category of finite sets
            sage: type(C)
            <class 'sage.categories.finite_sets.FiniteSets_with_category'>
            sage: type(C).__base__.__base__
            <class 'sage.categories.category_with_axiom.CategoryWithAxiom_singleton'>

            sage: TestSuite(C).run()
        """
    def extra_super_categories(self):
        """
        Return the extra super categories of a category with axiom.

        Default implementation which returns ``[]``.

        EXAMPLES::

            sage: FiniteSets().extra_super_categories()
            []
        """
    @cached_method
    def super_categories(self):
        """
        Return a list of the (immediate) super categories of
        ``self``, as per :meth:`Category.super_categories`.

        This implements the property that if ``As`` is a subcategory
        of ``Bs``, then the intersection of ``As`` with ``FiniteSets()``
        is a subcategory of ``As`` and of the intersection of ``Bs``
        with ``FiniteSets()``.

        EXAMPLES:

        A finite magma is both a magma and a finite set::

            sage: Magmas().Finite().super_categories()
            [Category of magmas, Category of finite sets]

        Variants::

            sage: Sets().Finite().super_categories()
            [Category of sets]

            sage: Monoids().Finite().super_categories()
            [Category of monoids, Category of finite semigroups]

        EXAMPLES:

        TESTS::

            sage: from sage.categories.category_with_axiom import TestObjects
            sage: C = TestObjects().FiniteDimensional().Unital().Commutative().Finite()
            sage: sorted(C.super_categories(), key=str)
            [Category of finite commutative test objects,
             Category of finite dimensional commutative unital test objects,
             Category of finite finite dimensional test objects]
        """
    def additional_structure(self) -> None:
        """
        Return the additional structure defined by ``self``.

        OUTPUT: ``None``

        By default, a category with axiom defines no additional
        structure.

        .. SEEALSO:: :meth:`Category.additional_structure`.

        EXAMPLES::

            sage: Sets().Finite().additional_structure()
            sage: Monoids().additional_structure()

        TESTS::

            sage: Sets().Finite().additional_structure.__module__
            'sage.categories.category_with_axiom'
        """
    def base_category(self):
        """
        Return the base category of ``self``.

        EXAMPLES::

            sage: C = Sets.Finite(); C
            Category of finite sets
            sage: C.base_category()
            Category of sets
            sage: C._without_axioms()
            Category of sets

        TESTS::

            sage: from sage.categories.category_with_axiom import TestObjects, CategoryWithAxiom
            sage: C = TestObjects().Commutative().Facade()
            sage: assert isinstance(C, CategoryWithAxiom)
            sage: C._without_axioms()
            Category of test objects
        """
    def __reduce__(self):
        """
        Implement the pickle protocol.

        This overrides the implementation in
        :meth:`UniqueRepresentation.__reduce__` in order to not
        exposes the implementation detail that, for example, the
        category of magmas which distribute over an associative
        additive magma is implemented as
        ``MagmasAndAdditiveMagmas.Distributive.AdditiveAssociative.AdditiveCommutative``
        and not
        ``MagmasAndAdditiveMagmas.Distributive.AdditiveCommutative.AdditiveAssociative``.

        EXAMPLES::

            sage: C = Semigroups()
            sage: reduction = C.__reduce__(); reduction
            (<function call_method at ...>, (Category of magmas, '_with_axiom', 'Associative'))
            sage: loads(dumps(C)) is C
            True
            sage: FiniteSets().__reduce__()
            (<function call_method at ...>, (Category of sets, '_with_axiom', 'Finite'))

            sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
            sage: C = MagmasAndAdditiveMagmas().Distributive().AdditiveAssociative().AdditiveCommutative()
            sage: C.__class__
            <class 'sage.categories.distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative_with_category'>
            sage: C.__reduce__()
            (<function call_method at ...>, (Category of additive associative distributive magmas and additive magmas, '_with_axiom', 'AdditiveCommutative'))
        """
    @cached_method
    def axioms(self):
        """
        Return the axioms known to be satisfied by all the
        objects of ``self``.

        .. SEEALSO:: :meth:`Category.axioms`

        EXAMPLES::

            sage: C = Sets.Finite(); C
            Category of finite sets
            sage: C.axioms()
            frozenset({'Finite'})

            sage: C = Modules(GF(5)).FiniteDimensional(); C
            Category of finite dimensional vector spaces over Finite Field of size 5
            sage: sorted(C.axioms())
            ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse',
             'AdditiveUnital', 'Finite', 'FiniteDimensional']

            sage: sorted(FiniteMonoids().Algebras(QQ).axioms())
            ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse',
             'AdditiveUnital', 'Associative', 'Distributive',
             'FiniteDimensional', 'Unital', 'WithBasis']
            sage: sorted(FiniteMonoids().Algebras(GF(3)).axioms())
            ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse',
             'AdditiveUnital', 'Associative', 'Distributive', 'Finite',
             'FiniteDimensional', 'Unital', 'WithBasis']

            sage: from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas
            sage: MagmasAndAdditiveMagmas().Distributive().Unital().axioms()
            frozenset({'Distributive', 'Unital'})

            sage: D = MagmasAndAdditiveMagmas().Distributive()
            sage: X = D.AdditiveAssociative().AdditiveCommutative().Associative()
            sage: X.Unital().super_categories()[1]
            Category of monoids
            sage: X.Unital().super_categories()[1] is Monoids()
            True
        """

class CategoryWithAxiom_over_base_ring(CategoryWithAxiom, Category_over_base_ring):
    def __init__(self, base_category) -> None:
        """
        TESTS::

            sage: C = Modules(ZZ).FiniteDimensional(); C
            Category of finite dimensional modules over Integer Ring
            sage: type(C)
            <class 'sage.categories.modules.Modules.FiniteDimensional_with_category'>
            sage: type(C).__base__.__base__
            <class 'sage.categories.category_with_axiom.CategoryWithAxiom_over_base_ring'>

            sage: TestSuite(C).run()
        """

class CategoryWithAxiom_singleton(Category_singleton, CategoryWithAxiom): ...

def axiom(axiom):
    '''
    Return a function/method ``self -> self._with_axiom(axiom)``.

    This can used as a shorthand to define axioms, in particular in
    the tests below. Usually one will want to attach documentation to
    an axiom, so the need for such a shorthand in real life might not
    be that clear, unless we start creating lots of axioms.

    In the long run maybe this could evolve into an ``@axiom`` decorator.

    EXAMPLES::

        sage: from sage.categories.category_with_axiom import axiom
        sage: axiom("Finite")(Semigroups())
        Category of finite semigroups

    Upon assigning the result to a class this becomes a method::

        sage: class As:
        ....:     def _with_axiom(self, axiom): return self, axiom
        ....:     Finite = axiom("Finite")
        sage: As().Finite()
        (<__main__.As ... at ...>, \'Finite\')
    '''

class Blahs(Category_singleton):
    """
    A toy singleton category, for testing purposes.

    This is the root of a hierarchy of mathematically meaningless
    categories, used for testing Sage's category framework:

    - :class:`Bars`
    - :class:`TestObjects`
    - :class:`DummyObjectsOverBaseRing`
    """
    def super_categories(self):
        """
        TESTS::

             sage: from sage.categories.category_with_axiom import Blahs
             sage: Blahs().super_categories()
             [Category of sets]
             sage: TestSuite(Blahs()).run()
        """
    class SubcategoryMethods:
        FiniteDimensional: Incomplete
        Commutative: Incomplete
        Unital: Incomplete
        Connected: Incomplete
        Flying: Incomplete
        Blue: Incomplete
    class FiniteDimensional(CategoryWithAxiom): ...
    class Commutative(CategoryWithAxiom): ...
    class Connected(CategoryWithAxiom): ...
    class Unital(CategoryWithAxiom):
        class Blue(CategoryWithAxiom): ...
    class Flying(CategoryWithAxiom):
        def extra_super_categories(self):
            """
            This illustrates a way to have an axiom imply another one.

            Here, we want ``Flying`` to imply ``Unital``, and to put
            the class for the category of unital flying blahs in
            ``Blahs.Flying`` rather than ``Blahs.Unital.Flying``.

            TESTS::

                sage: from sage.categories.category_with_axiom import Blahs, TestObjects, Bars
                sage: Blahs().Flying().extra_super_categories()
                [Category of unital blahs]
                sage: Blahs().Flying()
                Category of flying unital blahs
            """
    def Blue_extra_super_categories(self):
        """
        Illustrates a current limitation in the way to have an axiom
        imply another one.

        Here, we would want ``Blue`` to imply ``Unital``, and to put
        the class for the category of unital blue blahs in
        ``Blahs.Unital.Blue`` rather than ``Blahs.Blue``.

        This currently fails because ``Blahs`` is the category where
        the axiom ``Blue`` is defined, and the specifications
        currently impose that a category defining an axiom should also
        implement it (here in a category with axiom
        ``Blahs.Blue``). In practice, due to this violation of the
        specifications, the axiom is lost during the join calculation.

        .. TODO::

            Decide whether we care about this feature. In such a
            situation, we are not really defining a new axiom, but
            just defining an axiom as an alias for a couple others,
            which might not be that useful.

        .. TODO::

            Improve the infrastructure to detect and report this
            violation of the specifications, if this is
            easy. Otherwise, it's not so bad: when defining an axiom A
            in a category ``Cs`` the first thing one is supposed to
            doctest is that ``Cs().A()`` works. So the problem should
            not go unnoticed.

        TESTS::

            sage: from sage.categories.category_with_axiom import Blahs, TestObjects, Bars
            sage: Blahs().Blue_extra_super_categories()
            [Category of unital blahs]
            sage: Blahs().Blue()                          # todo: not implemented
            Category of blue unital blahs
        """

class Bars(Category_singleton):
    """
    A toy singleton category, for testing purposes.

    .. SEEALSO:: :class:`Blahs`
    """
    def super_categories(self):
        """
        TESTS::

            sage: from sage.categories.category_with_axiom import Bars
            sage: Bars().super_categories()
            [Category of blahs]
            sage: TestSuite(Bars()).run()
        """
    def Unital_extra_super_categories(self):
        """
        Return extraneous super categories for the unital objects of ``self``.

        This method specifies that a unital bar is a test object.
        Thus, the categories of unital bars and of unital test objects
        coincide.

        EXAMPLES::

            sage: from sage.categories.category_with_axiom import Bars, TestObjects
            sage: Bars().Unital_extra_super_categories()
            [Category of test objects]
            sage: Bars().Unital()
            Category of unital test objects
            sage: TestObjects().Unital().all_super_categories()
            [Category of unital test objects,
             Category of unital blahs,
             Category of test objects,
             Category of bars,
             Category of blahs,
             Category of sets,
             Category of sets with partial maps,
             Category of objects]
        """

class TestObjects(Category_singleton):
    """
    A toy singleton category, for testing purposes.

    .. SEEALSO:: :class:`Blahs`
    """
    def super_categories(self):
        """
        TESTS::

            sage: from sage.categories.category_with_axiom import TestObjects
            sage: TestObjects().super_categories()
            [Category of bars]
            sage: TestSuite(TestObjects()).run()
        """
    class FiniteDimensional(CategoryWithAxiom):
        class Finite(CategoryWithAxiom): ...
        class Unital(CategoryWithAxiom):
            class Commutative(CategoryWithAxiom): ...
    class Commutative(CategoryWithAxiom):
        class Facade(CategoryWithAxiom): ...
        class FiniteDimensional(CategoryWithAxiom): ...
        class Finite(CategoryWithAxiom): ...
    class Unital(CategoryWithAxiom): ...

class DummyObjectsOverBaseRing(Category_over_base_ring):
    """
    A toy singleton category, for testing purposes.

    .. SEEALSO:: :class:`Blahs`
    """
    def super_categories(self):
        """
        TESTS::

            sage: from sage.categories.category_with_axiom import DummyObjectsOverBaseRing
            sage: DummyObjectsOverBaseRing(QQ).super_categories()
            [Category of test objects]
            sage: DummyObjectsOverBaseRing.Unital.an_instance()
            Category of unital dummy objects over base ring over Rational Field
            sage: DummyObjectsOverBaseRing.FiniteDimensional.Unital.an_instance()
            Category of finite dimensional unital dummy objects over base ring over Rational Field
            sage: C = DummyObjectsOverBaseRing(QQ).FiniteDimensional().Unital().Commutative()
            sage: TestSuite(C).run()
        """
    class FiniteDimensional(CategoryWithAxiom_over_base_ring):
        class Finite(CategoryWithAxiom_over_base_ring): ...
        class Unital(CategoryWithAxiom_over_base_ring):
            class Commutative(CategoryWithAxiom_over_base_ring): ...
    class Commutative(CategoryWithAxiom_over_base_ring):
        class Facade(CategoryWithAxiom_over_base_ring): ...
        class FiniteDimensional(CategoryWithAxiom_over_base_ring): ...
        class Finite(CategoryWithAxiom_over_base_ring): ...
    class Unital(CategoryWithAxiom_over_base_ring): ...
