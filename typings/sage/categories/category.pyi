r"""
Categories

AUTHORS:

- David Kohel, William Stein and Nicolas M. Thiery

Every Sage object lies in a category. Categories in Sage are
modeled on the mathematical idea of category, and are distinct from
Python classes, which are a programming construct.

In most cases, typing ``x.category()`` returns the category to which ``x``
belongs. If ``C`` is a category and ``x`` is any object, ``C(x)`` tries to
make an object in ``C`` from ``x``. Checking if ``x`` belongs to ``C`` is done
as usually by ``x in C``.

See :class:`Category` and :mod:`sage.categories.primer` for more details.

EXAMPLES:

We create a couple of categories::

    sage: Sets()
    Category of sets
    sage: GSets(AbelianGroup([2, 4, 9]))                                                # needs sage.groups
    Category of G-sets for Multiplicative Abelian group isomorphic to C2 x C4 x C9
    sage: Semigroups()
    Category of semigroups
    sage: VectorSpaces(FiniteField(11))
    Category of vector spaces over Finite Field of size 11
    sage: Ideals(IntegerRing())
    Category of ring ideals in Integer Ring

Let's request the category of some objects::

    sage: V = VectorSpace(RationalField(), 3)                                           # needs sage.modules
    sage: V.category()                                                                  # needs sage.modules
    Category of finite dimensional vector spaces with basis
     over (number fields and quotient fields and metric spaces)

    sage: G = SymmetricGroup(9)                                                         # needs sage.groups
    sage: G.category()                                                                  # needs sage.groups
    Join of
     Category of finite enumerated permutation groups and
     Category of finite Weyl groups and
     Category of well generated finite irreducible complex reflection groups

    sage: P = PerfectMatchings(3)                                                       # needs sage.combinat
    sage: P.category()                                                                  # needs sage.combinat
    Category of finite enumerated sets

Let's check some memberships::

    sage: V in VectorSpaces(QQ)                                                         # needs sage.modules
    True
    sage: V in VectorSpaces(FiniteField(11))                                            # needs sage.modules
    False
    sage: G in Monoids()                                                                # needs sage.groups
    True
    sage: P in Rings()                                                                  # needs sage.combinat
    False

For parametrized categories one can use the following shorthand::

    sage: V in VectorSpaces                                                             # needs sage.modules
    True
    sage: G in VectorSpaces                                                             # needs sage.groups
    False

A parent ``P`` is in a category ``C`` if ``P.category()`` is a subcategory of
``C``.

.. NOTE::

    Any object of a category should be an instance of
    :class:`~sage.structure.category_object.CategoryObject`.

    For backward compatibility this is not yet enforced::

        sage: class A:
        ....:   def category(self):
        ....:       return Fields()
        sage: A() in Rings()
        True

    By default, the category of an element `x` of a parent `P` is the category
    of all objects of `P` (this is dubious and may be deprecated)::

        sage: V = VectorSpace(RationalField(), 3)                                       # needs sage.modules
        sage: v = V.gen(1)                                                              # needs sage.modules
        sage: v.category()                                                              # needs sage.modules
        Category of elements of Vector space of dimension 3 over Rational Field
"""

from typing import Self, Literal, TypeGuard, overload
from collections.abc import Iterable, Sequence
from sage.graphs.digraph import DiGraph
from sage.categories.objects import Objects

from sage.categories.category_cy_helper import category_sort_key as category_sort_key, join_as_tuple as join_as_tuple
from sage.misc.abstract_method import abstract_method as abstract_method, abstract_methods_of_class as abstract_methods_of_class
from sage.misc.c3_controlled import C3_sorted_merge as C3_sorted_merge
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.unknown import Unknown as Unknown
from sage.misc.weak_dict import WeakValueDictionary as WeakValueDictionary
from sage.structure.dynamic_class import DynamicMetaclass as DynamicMetaclass, dynamic_class as dynamic_class
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

HALL_OF_FAME: list[Literal[
    'Coxeter', 'Hopf', 'Weyl', 'Lie', 'Hecke', 'Dedekind', 'Stone']]

class Category(UniqueRepresentation, SageObject):
    '''
    The base class for modeling mathematical categories, like for example:

    - ``Groups()`` -- the category of groups
    - ``EuclideanDomains()`` -- the category of euclidean rings
    - ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
      rationals

    See :mod:`sage.categories.primer` for an introduction to
    categories in Sage, their relevance, purpose, and usage. The
    documentation below will focus on their implementation.

    Technically, a category is an instance of the class
    :class:`Category` or some of its subclasses. Some categories, like
    :class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
    many instances of the class :class:`VectorSpaces`. On the other
    hand, ``EuclideanDomains()`` is the single instance of the class
    :class:`EuclideanDomains`.

    Recall that an algebraic structure (say, the ring `\\QQ[x]`) is
    modelled in Sage by an object which is called a parent. This
    object belongs to certain categories (here ``EuclideanDomains()`` and
    ``Algebras()``). The elements of the ring are themselves objects.

    The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

    - Operations on the category itself (what is its super categories?
      its category of morphisms? its dual category?).
    - Generic operations on parents in this category, like the ring `\\QQ[x]`.
    - Generic operations on elements of such parents (e. g., the
      Euclidean algorithm for computing gcds).
    - Generic operations on morphisms of this category.

    This is achieved as follows::

        sage: from sage.categories.category import Category
        sage: class EuclideanDomains(Category):
        ....:     # operations on the category itself
        ....:     def super_categories(self):
        ....:         [Rings()]
        ....:
        ....:     def dummy(self): # TODO: find some good examples
        ....:          pass
        ....:
        ....:     class ParentMethods: # holds the generic operations on parents
        ....:          # TODO: find a good example of an operation
        ....:          pass
        ....:
        ....:     class ElementMethods:# holds the generic operations on elements
        ....:          def gcd(x, y):
        ....:              # Euclid algorithms
        ....:              pass
        ....:
        ....:     class MorphismMethods: # holds the generic operations on morphisms
        ....:          # TODO: find a good example of an operation
        ....:          pass
        ....:

    Note that the nested class ``ParentMethods`` is merely a container
    of operations, and does not inherit from anything. Instead, the
    hierarchy relation is defined once at the level of the categories,
    and the actual hierarchy of classes is built in parallel from all
    the ``ParentMethods`` nested classes, and stored in the attributes
    ``parent_class``. Then, a parent in a category ``C`` receives the
    appropriate operations from all the super categories by usual
    class inheritance from ``C.parent_class``.

    Similarly, two other hierarchies of classes, for elements and
    morphisms respectively, are built from all the ``ElementMethods``
    and ``MorphismMethods`` nested classes.

    EXAMPLES:

    We define a hierarchy of four categories ``As()``, ``Bs()``,
    ``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

    - ``As()`` -- the category of sets
    - ``Bs()`` -- the category of additive groups
    - ``Cs()`` -- the category of multiplicative monoids
    - ``Ds()`` -- the category of rings

    ::

        sage: from sage.categories.category import Category
        sage: from sage.misc.lazy_attribute import lazy_attribute
        sage: class As (Category):
        ....:     def super_categories(self):
        ....:         return []
        ....:
        ....:     class ParentMethods:
        ....:         def fA(self):
        ....:             return "A"
        ....:         f = fA

        sage: class Bs (Category):
        ....:     def super_categories(self):
        ....:         return [As()]
        ....:
        ....:     class ParentMethods:
        ....:         def fB(self):
        ....:             return "B"

        sage: class Cs (Category):
        ....:     def super_categories(self):
        ....:         return [As()]
        ....:
        ....:     class ParentMethods:
        ....:         def fC(self):
        ....:             return "C"
        ....:         f = fC

        sage: class Ds (Category):
        ....:     def super_categories(self):
        ....:         return [Bs(),Cs()]
        ....:
        ....:     class ParentMethods:
        ....:         def fD(self):
        ....:             return "D"

    Categories should always have unique representation; by :issue:`12215`,
    this means that it will be kept in cache, but only
    if there is still some strong reference to it.

    We check this before proceeding::

        sage: import gc
        sage: idAs = id(As())
        sage: _ = gc.collect()
        sage: n == id(As())
        False
        sage: a = As()
        sage: id(As()) == id(As())
        True
        sage: As().parent_class == As().parent_class
        True

    We construct a parent in the category ``Ds()`` (that, is an instance
    of ``Ds().parent_class``), and check that it has access to all the
    methods provided by all the categories, with the appropriate
    inheritance order::

        sage: D = Ds().parent_class()
        sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
        [\'A\', \'B\', \'C\', \'D\']
        sage: D.f()
        \'C\'

    ::

        sage: C = Cs().parent_class()
        sage: [ C.fA(), C.fC() ]
        [\'A\', \'C\']
        sage: C.f()
        \'C\'

    Here is the parallel hierarchy of classes which has been built
    automatically, together with the method resolution order (``.mro()``)::

        sage: As().parent_class
        <class \'__main__.As.parent_class\'>
        sage: As().parent_class.__bases__
        (<... \'object\'>,)
        sage: As().parent_class.mro()
        [<class \'__main__.As.parent_class\'>, <... \'object\'>]

    ::

        sage: Bs().parent_class
        <class \'__main__.Bs.parent_class\'>
        sage: Bs().parent_class.__bases__
        (<class \'__main__.As.parent_class\'>,)
        sage: Bs().parent_class.mro()
        [<class \'__main__.Bs.parent_class\'>, <class \'__main__.As.parent_class\'>, <... \'object\'>]

    ::

        sage: Cs().parent_class
        <class \'__main__.Cs.parent_class\'>
        sage: Cs().parent_class.__bases__
        (<class \'__main__.As.parent_class\'>,)
        sage: Cs().parent_class.__mro__
        (<class \'__main__.Cs.parent_class\'>, <class \'__main__.As.parent_class\'>, <... \'object\'>)

    ::

        sage: Ds().parent_class
        <class \'__main__.Ds.parent_class\'>
        sage: Ds().parent_class.__bases__
        (<class \'__main__.Cs.parent_class\'>, <class \'__main__.Bs.parent_class\'>)
        sage: Ds().parent_class.mro()
        [<class \'__main__.Ds.parent_class\'>, <class \'__main__.Cs.parent_class\'>,
         <class \'__main__.Bs.parent_class\'>, <class \'__main__.As.parent_class\'>, <... \'object\'>]

    Note that two categories in the same class need not have the
    same ``super_categories``. For example, ``Algebras(QQ)`` has
    ``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
    only has ``Modules(ZZ)`` as super category. In particular, the
    constructed parent class and element class will differ (inheriting,
    or not, methods specific for vector spaces)::

        sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
        False
        sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
        True

    On the other hand, identical hierarchies of classes are,
    preferably, built only once (e.g. for categories over a base ring)::

        sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
        True
        sage: F = FractionField(ZZ[\'t\'])
        sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F[\'x\'])).parent_class
        True

    We now construct a parent in the usual way::

        sage: class myparent(Parent):
        ....:     def __init__(self):
        ....:         Parent.__init__(self, category=Ds())
        ....:     def g(self):
        ....:         return "myparent"
        ....:     class Element():
        ....:         pass
        sage: D = myparent()
        sage: D.__class__
        <class \'__main__.myparent_with_category\'>
        sage: D.__class__.__bases__
        (<class \'__main__.myparent\'>, <class \'__main__.Ds.parent_class\'>)
        sage: D.__class__.mro()
        [<class \'__main__.myparent_with_category\'>,
        <class \'__main__.myparent\'>,
        <class \'sage.structure.parent.Parent\'>,
        <class \'sage.structure.category_object.CategoryObject\'>,
        <class \'sage.structure.sage_object.SageObject\'>,
        <class \'__main__.Ds.parent_class\'>,
        <class \'__main__.Cs.parent_class\'>,
        <class \'__main__.Bs.parent_class\'>,
        <class \'__main__.As.parent_class\'>,
        <... \'object\'>]
        sage: D.fA()
        \'A\'
        sage: D.fB()
        \'B\'
        sage: D.fC()
        \'C\'
        sage: D.fD()
        \'D\'
        sage: D.f()
        \'C\'
        sage: D.g()
        \'myparent\'

    ::

        sage: D.element_class
        <class \'__main__.myparent_with_category.element_class\'>
        sage: D.element_class.mro()
        [<class \'__main__.myparent_with_category.element_class\'>,
        <class ...__main__....Element...>,
        <class \'__main__.Ds.element_class\'>,
        <class \'__main__.Cs.element_class\'>,
        <class \'__main__.Bs.element_class\'>,
        <class \'__main__.As.element_class\'>,
        <... \'object\'>]


    TESTS::

        sage: import __main__
        sage: __main__.myparent = myparent
        sage: __main__.As = As
        sage: __main__.Bs = Bs
        sage: __main__.Cs = Cs
        sage: __main__.Ds = Ds
        sage: loads(dumps(Ds)) is Ds
        True
        sage: loads(dumps(Ds())) is Ds()
        True
        sage: loads(dumps(Ds().element_class)) is Ds().element_class
        True

    .. automethod:: Category._super_categories
    .. automethod:: Category._super_categories_for_classes
    .. automethod:: Category._all_super_categories
    .. automethod:: Category._all_super_categories_proper
    .. automethod:: Category._set_of_super_categories
    .. automethod:: Category._make_named_class
    .. automethod:: Category._repr_
    .. automethod:: Category._repr_object_names
    .. automethod:: Category._test_category
    .. automethod:: Category._with_axiom
    .. automethod:: Category._with_axiom_as_tuple
    .. automethod:: Category._without_axioms
    .. automethod:: Category._sort
    .. automethod:: Category._sort_uniq
    .. automethod:: Category.__classcall__
    .. automethod:: Category.__init__
    '''
    
    @staticmethod
    def __classcall__(cls, *args, **options): # pyright: ignore[reportSelfClsParameterName]
        """
        Input mangling for unique representation.

        Let ``C = Cs(...)`` be a category. Since :issue:`12895`, the
        class of ``C`` is a dynamic subclass ``Cs_with_category`` of
        ``Cs`` in order for ``C`` to inherit code from the
        ``SubcategoryMethods`` nested classes of its super categories.

        The purpose of this ``__classcall__`` method is to ensure that
        reconstructing ``C`` from its class with
        ``Cs_with_category(...)`` actually calls properly ``Cs(...)``
        and gives back ``C``.

        .. SEEALSO:: :meth:`subcategory_class`

        EXAMPLES::

            sage: A = Algebras(QQ)
            sage: A.__class__
            <class 'sage.categories.algebras.Algebras_with_category'>
            sage: A is Algebras(QQ)
            True
            sage: A is A.__class__(QQ)
            True
        """
    def __init__(self) -> None:
        """
        Initialize this category.

        EXAMPLES::

            sage: class SemiprimitiveRings(Category):
            ....:     def super_categories(self):
            ....:         return [Rings()]
            ....:     class ParentMethods:
            ....:         def jacobson_radical(self):
            ....:             return self.ideal(0)
            sage: C = SemiprimitiveRings()
            sage: C
            Category of semiprimitive rings
            sage: C.__class__
            <class '__main__.SemiprimitiveRings_with_category'>

        .. NOTE::

            If the default name of the category (built from the name of
            the class) is not adequate, please implement
            :meth:`_repr_object_names` to customize it.
        """
    @classmethod
    def an_instance(cls) -> Self:
        """
        Return an instance of this class.

        EXAMPLES::

            sage: Rings.an_instance()
            Category of rings

        Parametrized categories should overload this default
        implementation to provide appropriate arguments::

            sage: Algebras.an_instance()
            Category of algebras over Rational Field
            sage: Bimodules.an_instance()                                               # needs sage.rings.real_mpfr
            Category of bimodules over Rational Field on the left
             and Real Field with 53 bits of precision on the right
            sage: AlgebraIdeals.an_instance()
            Category of algebra ideals
             in Univariate Polynomial Ring in x over Rational Field
        """
    def __call__(self, x: object, *args, **opts) -> Self:
        """
        Construct an object in this category from the data in ``x``,
        or throw :exc:`TypeError` or :exc:`NotImplementedError`.

        If ``x`` is readily in ``self`` it is returned unchanged.
        Categories wishing to extend this minimal behavior should
        implement :meth:`._call_`.

        EXAMPLES::

            sage: Rings()(ZZ)
            Integer Ring
        """
    def __contains__(self, x: object) -> bool:
        """
        Membership testing.

        Returns whether ``x`` is an object in this category, that is
        if the category of ``x`` is a subcategory of ``self``.

        EXAMPLES::

            sage: ZZ in Sets()
            True
        """
    @staticmethod
    def __classcontains__(cls: type, x: object) -> bool: # pyright: ignore[reportSelfClsParameterName]
        """
        Membership testing, without arguments.

        INPUT:

        - ``cls`` -- a category class
        - ``x`` -- any object

        Returns whether ``x`` is an object of a category which is an instance
        of ``cls``.

        EXAMPLES:

        This method makes it easy to test if an object is, say, a
        vector space, without having to specify the base ring::

            sage: F = FreeModule(QQ, 3)                                                 # needs sage.modules
            sage: F in VectorSpaces                                                     # needs sage.modules
            True

            sage: F = FreeModule(ZZ, 3)                                                 # needs sage.modules
            sage: F in VectorSpaces                                                     # needs sage.modules
            False

            sage: F in Algebras                                                         # needs sage.modules
            False

        TESTS:

        Non category objects shall be handled properly::

            sage: [1,2] in Algebras
            False
        """
    def is_abelian(self) -> bool:
        """
        Return whether this category is abelian.

        An abelian category is a category satisfying:

        - It has a zero object;
        - It has all pullbacks and pushouts;
        - All monomorphisms and epimorphisms are normal.

        Equivalently, one can define an increasing sequence of conditions:

        - A category is pre-additive if it is enriched over abelian groups
          (all homsets are abelian groups and composition is bilinear);
        - A pre-additive category is additive if every finite set of objects
          has a biproduct (we can form direct sums and direct products);
        - An additive category is pre-abelian if every morphism has both a
          kernel and a cokernel;
        - A pre-abelian category is abelian if every monomorphism is the
          kernel of some morphism and every epimorphism is the cokernel of
          some morphism.

        EXAMPLES::

            sage: Modules(ZZ).is_abelian()
            True
            sage: FreeModules(ZZ).is_abelian()
            False
            sage: FreeModules(QQ).is_abelian()
            True
            sage: CommutativeAdditiveGroups().is_abelian()
            True
            sage: Semigroups().is_abelian()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_abelian
        """
    def category_graph(self) -> DiGraph:
        """
        Return the graph of all super categories of this category.

        EXAMPLES::

            sage: C = Algebras(QQ)
            sage: G = C.category_graph()                                                # needs sage.graphs
            sage: G.is_directed_acyclic()                                               # needs sage.graphs
            True

        The girth of a directed acyclic graph is infinite, however,
        the girth of the underlying undirected graph is 4 in this case::

            sage: Graph(G).girth()                                                      # needs sage.graphs
            4
        """
    # @abstract_method
    def super_categories(self) -> list[Category]:
        """
        Return the *immediate* super categories of ``self``.

        OUTPUT: a duplicate-free list of categories

        Every category should implement this method.

        EXAMPLES::

            sage: Groups().super_categories()
            [Category of monoids, Category of inverse unital magmas]
            sage: Objects().super_categories()
            []

        .. NOTE::

            Since :issue:`10963`, the order of the categories in the
            result is irrelevant. For details, see
            :ref:`category-primer-category-order`.

        .. NOTE::

            Whenever speed matters, developers are advised to use the
            lazy attribute :meth:`_super_categories` instead of
            calling this method.
        """
    def all_super_categories(self, proper: bool = False) -> list[Category]:
        """
        Return the list of all super categories of this category.

        INPUT:

        - ``proper`` -- boolean (default: ``False``); whether to exclude this category

        Since :issue:`11943`, the order of super categories is
        determined by Python's method resolution order C3 algorithm.

        .. NOTE::

            Whenever speed matters, the developers are advised to use
            instead the lazy attributes :meth:`_all_super_categories`,
            :meth:`_all_super_categories_proper`, or
            :meth:`_set_of_super_categories`, as
            appropriate. Simply because lazy attributes are much
            faster than any method.

        .. NOTE::

            This is not the same as the concept of super category in mathematics.
            In fact, this is not even the opposite relation of :meth:`is_subcategory`::

                sage: A = VectorSpaces(QQ); A
                Category of vector spaces over Rational Field
                sage: B = VectorSpaces(QQ.category()); B
                Category of vector spaces over (number fields and quotient fields and metric spaces)
                sage: A.is_subcategory(B)
                True
                sage: B in A.all_super_categories()
                False

        .. SEEALSO:: :meth:`_test_category_graph`

        EXAMPLES::

            sage: C = Rings(); C
            Category of rings
            sage: C.all_super_categories()
            [Category of rings, Category of rngs, Category of semirings, ...
             Category of monoids, ...
             Category of commutative additive groups, ...
             Category of sets, Category of sets with partial maps,
             Category of objects]

            sage: C.all_super_categories(proper = True)
            [Category of rngs, Category of semirings, ...
             Category of monoids, ...
             Category of commutative additive groups, ...
             Category of sets, Category of sets with partial maps,
             Category of objects]

            sage: Sets().all_super_categories()
            [Category of sets, Category of sets with partial maps, Category of objects]
            sage: Sets().all_super_categories(proper=True)
            [Category of sets with partial maps, Category of objects]
            sage: Sets().all_super_categories() is Sets()._all_super_categories
            True
            sage: Sets().all_super_categories(proper=True) is Sets()._all_super_categories_proper
            True
        """
    def additional_structure(self) -> Self | None:
        """
        Return whether ``self`` defines additional structure.

        OUTPUT:

        - ``self`` if ``self`` defines additional structure and
          ``None`` otherwise. This default implementation returns
          ``self``.

        A category `C` *defines additional structure* if `C`-morphisms
        shall preserve more structure (e.g. operations) than that
        specified by the super categories of `C`. For example, the
        category of magmas defines additional structure, namely the
        operation `*` that shall be preserved by magma morphisms. On
        the other hand the category of rings does not define additional
        structure: a function between two rings that is both a unital
        magma morphism and a unital additive magma morphism is
        automatically a ring morphism.

        Formally speaking `C` *defines additional structure*, if `C`
        is *not* a full subcategory of the join of its super
        categories: the morphisms need to preserve more structure, and
        thus the homsets are smaller.

        By default, a category is considered as defining additional
        structure, unless it is a :ref:`category with axiom
        <category-primer-axioms>`.

        EXAMPLES:

        Here are some typical structure categories, with the
        additional structure they define::

            sage: Sets().additional_structure()
            Category of sets
            sage: Magmas().additional_structure()         # `*`
            Category of magmas
            sage: AdditiveMagmas().additional_structure() # `+`
            Category of additive magmas
            sage: LeftModules(ZZ).additional_structure()  # left multiplication by scalar
            Category of left modules over Integer Ring
            sage: Coalgebras(QQ).additional_structure()   # coproduct
            Category of coalgebras over Rational Field
            sage: Crystals().additional_structure()       # crystal operators
            Category of crystals

        On the other hand, the category of semigroups is not a
        structure category, since its operation `+` is already defined
        by the category of magmas::

            sage: Semigroups().additional_structure()

        Most :ref:`categories with axiom <category-primer-axioms>`
        don't define additional structure::

            sage: Sets().Finite().additional_structure()
            sage: Rings().Commutative().additional_structure()
            sage: Modules(QQ).FiniteDimensional().additional_structure()
            sage: from sage.categories.magmatic_algebras import MagmaticAlgebras
            sage: MagmaticAlgebras(QQ).Unital().additional_structure()

        As of Sage 6.4, the only exceptions are the category of unital
        magmas or the category of unital additive magmas (both define
        a unit which shall be preserved by morphisms)::

            sage: Magmas().Unital().additional_structure()
            Category of unital magmas
            sage: AdditiveMagmas().AdditiveUnital().additional_structure()
            Category of additive unital additive magmas

        Similarly, :ref:`functorial construction categories
        <category-primer-functorial-constructions>` don't define
        additional structure, unless the construction is actually
        defined by their base category. For example, the category of
        graded modules defines a grading which shall be preserved by
        morphisms::

            sage: Modules(ZZ).Graded().additional_structure()
            Category of graded modules over Integer Ring

        On the other hand, the category of graded algebras does not
        define additional structure; indeed an algebra morphism which
        is also a module morphism is a graded algebra morphism::

            sage: Algebras(ZZ).Graded().additional_structure()

        Similarly, morphisms are requested to preserve the structure
        given by the following constructions::

            sage: Sets().Quotients().additional_structure()
            Category of quotients of sets
            sage: Sets().CartesianProducts().additional_structure()
            Category of Cartesian products of sets
            sage: Modules(QQ).TensorProducts().additional_structure()

        This might change, as we are lacking enough data points to
        guarantee that this was the correct design decision.

        .. NOTE::

            In some cases a category defines additional structure,
            where the structure can be useful to manipulate morphisms
            but where, in most use cases, we don't want the morphisms
            to necessarily preserve it. For example, in the context of
            finite dimensional vector spaces, having a distinguished
            basis allows for representing morphisms by matrices; yet
            considering only morphisms that preserve that
            distinguished basis would be boring.

            In such cases, we might want to eventually have two
            categories, one where the additional structure is
            preserved, and one where it's not necessarily preserved
            (we would need to find an idiom for this).

            At this point, a choice is to be made each time, according
            to the main use cases. Some of those choices are yet to be
            settled. For example, should by default:

            - an euclidean domain morphism preserve euclidean
              division? ::

                  sage: EuclideanDomains().additional_structure()
                  Category of euclidean domains

            - an enumerated set morphism preserve the distinguished
              enumeration? ::

                  sage: EnumeratedSets().additional_structure()

            - a module with basis morphism preserve the distinguished
              basis? ::

                  sage: Modules(QQ).WithBasis().additional_structure()

        .. SEEALSO::

            This method together with the methods overloading it
            provide the basic data to determine, for a given category,
            the super categories that define some structure (see
            :meth:`structure`), and to test whether a category is a
            full subcategory of some other category (see
            :meth:`is_full_subcategory`). For example, the category of
            Coxeter groups is not full subcategory of the category of
            groups since morphisms need to preserve the distinguished
            generators::

                sage: CoxeterGroups().is_full_subcategory(Groups())
                False

            The support for modeling full subcategories has been
            introduced in :issue:`16340`.
        """
    @cached_method
    def structure(self) -> frozenset[Category]:
        """
        Return the structure ``self`` is endowed with.

        This method returns the structure that morphisms in this
        category shall be preserving. For example, it tells that a
        ring is a set endowed with a structure of both a unital magma
        and an additive unital magma which satisfies some further
        axioms. In other words, a ring morphism is a function that
        preserves the unital magma and additive unital magma
        structure.

        In practice, this returns the collection of all the super
        categories of ``self`` that define some additional structure,
        as a frozen set.

        EXAMPLES::

            sage: Objects().structure()
            frozenset()

            sage: def structure(C):
            ....:     return Category._sort(C.structure())

            sage: structure(Sets())
            (Category of sets, Category of sets with partial maps)
            sage: structure(Magmas())
            (Category of magmas, Category of sets, Category of sets with partial maps)

        In the following example, we only list the smallest structure
        categories to get a more readable output::

            sage: def structure(C):
            ....:     return Category._sort_uniq(C.structure())

            sage: structure(Magmas())
            (Category of magmas,)
            sage: structure(Rings())
            (Category of unital magmas, Category of additive unital additive magmas)
            sage: structure(Fields())
            (Category of euclidean domains, Category of noetherian rings)
            sage: structure(Algebras(QQ))
            (Category of unital magmas,
             Category of right modules over Rational Field,
             Category of left modules over Rational Field)
            sage: structure(HopfAlgebras(QQ).Graded().WithBasis().Connected())
            (Category of Hopf algebras over Rational Field,
             Category of graded modules over Rational Field)

        This method is used in :meth:`is_full_subcategory` for
        deciding whether a category is a full subcategory of some
        other category, and for documentation purposes. It is computed
        recursively from the result of :meth:`additional_structure`
        on the super categories of ``self``.
        """
    def is_full_subcategory(self, other: Category) -> bool:
        """
        Return whether ``self`` is a full subcategory of ``other``.

        A subcategory `B` of a category `A` is a *full subcategory* if
        any `A`-morphism between two objects of `B` is also a
        `B`-morphism (the reciprocal always holds: any `B`-morphism
        between two objects of `B` is an `A`-morphism).

        This is computed by testing whether ``self`` is a subcategory
        of ``other`` and whether they have the same structure, as
        determined by :meth:`structure` from the
        result of :meth:`additional_structure` on the super
        categories.

        .. WARNING::

            A positive answer is guaranteed to be mathematically
            correct. A negative answer may mean that Sage has not been
            taught enough information (or can not yet within the
            current model) to derive this information. See
            :meth:`full_super_categories` for a discussion.

        .. SEEALSO::

            - :meth:`is_subcategory`
            - :meth:`full_super_categories`

        EXAMPLES::

            sage: Magmas().Associative().is_full_subcategory(Magmas())
            True
            sage: Magmas().Unital().is_full_subcategory(Magmas())
            False
            sage: Rings().is_full_subcategory(Magmas().Unital() & AdditiveMagmas().AdditiveUnital())
            True

        Here are two typical examples of false negatives::

            sage: Groups().is_full_subcategory(Semigroups())
            False
            sage: Groups().is_full_subcategory(Semigroups()) # todo: not implemented
            True
            sage: Fields().is_full_subcategory(Rings())
            False
            sage: Fields().is_full_subcategory(Rings())      # todo: not implemented
            True

        .. TODO::

            The latter is a consequence of :class:`EuclideanDomains`
            currently being a structure category. Is this what we
            want? ::

                sage: EuclideanDomains().is_full_subcategory(Rings())
                False
        """
    @cached_method
    def full_super_categories(self) -> list[Category]:
        """
        Return the *immediate* full super categories of ``self``.

        .. SEEALSO::

            - :meth:`super_categories`
            - :meth:`is_full_subcategory`

        .. WARNING::

            The current implementation selects the full subcategories
            among the immediate super categories of ``self``. This
            assumes that, if `C\\subset B\\subset A` is a chain of
            categories and `C` is a full subcategory of `A`, then `C`
            is a full subcategory of `B` and `B` is a full subcategory
            of `A`.

            This assumption is guaranteed to hold with the current
            model and implementation of full subcategories in
            Sage. However, mathematically speaking, this is too
            restrictive. This indeed prevents the complete modelling
            of situations where any `A` morphism between elements of
            `C` automatically preserves the `B` structure. See below
            for an example.

        EXAMPLES:

        A semigroup morphism between two finite semigroups is a finite
        semigroup morphism::

            sage: Semigroups().Finite().full_super_categories()
            [Category of semigroups]

        On the other hand, a semigroup morphism between two monoids is
        not necessarily a monoid morphism (which must map the unit to
        the unit)::

            sage: Monoids().super_categories()
            [Category of semigroups, Category of unital magmas]
            sage: Monoids().full_super_categories()
            [Category of unital magmas]

        Any semigroup morphism between two groups is automatically a
        monoid morphism (in a group the unit is the unique idempotent,
        so it has to be mapped to the unit). Yet, due to the
        limitation of the model advertised above, Sage currently cannot
        be taught that the category of groups is a full subcategory of
        the category of semigroups::

            sage: Groups().full_super_categories()     # todo: not implemented
            [Category of monoids, Category of semigroups, Category of inverse unital magmas]
            sage: Groups().full_super_categories()
            [Category of monoids, Category of inverse unital magmas]
        """
    @lazy_attribute
    def subcategory_class(self) -> type:
        """
        A common superclass for all subcategories of this category (including this one).

        This class derives from ``D.subcategory_class`` for each super
        category `D` of ``self``, and includes all the methods from
        the nested class ``self.SubcategoryMethods``, if it exists.

        .. SEEALSO::

            - :issue:`12895`
            - :meth:`parent_class`
            - :meth:`element_class`
            - :meth:`_make_named_class`

        EXAMPLES::

            sage: cls = Rings().subcategory_class; cls
            <class 'sage.categories.rings.Rings.subcategory_class'>
            sage: type(cls)
            <class 'sage.structure.dynamic_class.DynamicMetaclass'>

        ``Rings()`` is an instance of this class, as well as all its subcategories::

            sage: isinstance(Rings(), cls)
            True
            sage: isinstance(AlgebrasWithBasis(QQ), cls)
            True

        .. NOTE::

            See the note about :meth:`_test_category_graph` regarding Python
            class hierarchy.

        TESTS::

            sage: cls = Algebras(QQ).subcategory_class; cls
            <class 'sage.categories.algebras.Algebras.subcategory_class'>
            sage: type(cls)
            <class 'sage.structure.dynamic_class.DynamicMetaclass'>
        """
    @lazy_attribute
    def parent_class(self) -> type:
        """
        A common super class for all parents in this category (and its
        subcategories).

        This class contains the methods defined in the nested class
        ``self.ParentMethods`` (if it exists), and has as bases the
        parent classes of the super categories of ``self``.

        .. SEEALSO::

            - :meth:`element_class`, :meth:`morphism_class`
            - :class:`Category` for details

        EXAMPLES::

            sage: C = Algebras(QQ).parent_class; C
            <class 'sage.categories.algebras.Algebras.parent_class'>
            sage: type(C)
            <class 'sage.structure.dynamic_class.DynamicMetaclass'>

        By :issue:`11935`, some categories share their parent
        classes. For example, the parent class of an algebra only
        depends on the category of the base ring. A typical example is
        the category of algebras over a finite field versus algebras
        over a non-field::

            sage: Algebras(GF(7)).parent_class is Algebras(GF(5)).parent_class
            True
            sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
            False
            sage: Algebras(ZZ['t']).parent_class is Algebras(ZZ['t','x']).parent_class
            True

        See :class:`CategoryWithParameters` for an abstract base class for
        categories that depend on parameters, even though the parent
        and element classes only depend on the parent or element
        classes of its super categories. It is used in
        :class:`~sage.categories.bimodules.Bimodules`,
        :class:`~sage.categories.category_types.Category_over_base` and
        :class:`sage.categories.category.JoinCategory`.

        .. NOTE::

            See the note about :meth:`_test_category_graph` regarding Python
            class hierarchy.
        """
    @lazy_attribute
    def element_class(self) -> type:
        """
        A common super class for all elements of parents in this category
        (and its subcategories).

        This class contains the methods defined in the nested class
        ``self.ElementMethods`` (if it exists), and has as bases the
        element classes of the super categories of ``self``.

        .. SEEALSO::

            - :meth:`parent_class`, :meth:`morphism_class`
            - :class:`Category` for details

        EXAMPLES::

            sage: C = Algebras(QQ).element_class; C
            <class 'sage.categories.algebras.Algebras.element_class'>
            sage: type(C)
            <class 'sage.structure.dynamic_class.DynamicMetaclass'>

        By :issue:`11935`, some categories share their element
        classes. For example, the element class of an algebra only
        depends on the category of the base. A typical example is the
        category of algebras over a field versus algebras over a
        non-field::

            sage: Algebras(GF(5)).element_class is Algebras(GF(3)).element_class
            True
            sage: Algebras(QQ).element_class is Algebras(ZZ).element_class
            False
            sage: Algebras(ZZ['t']).element_class is Algebras(ZZ['t','x']).element_class
            True

        These classes are constructed with ``__slots__ = ()``, so
        instances may not have a ``__dict__``::

            sage: E = FiniteEnumeratedSets().element_class
            sage: E.__dictoffset__
            0

        .. SEEALSO:: :meth:`parent_class`

        .. NOTE::

            See the note about :meth:`_test_category_graph` regarding Python
            class hierarchy.
        """
    @lazy_attribute
    def morphism_class(self) -> type:
        """
        A common super class for all morphisms between parents in this
        category (and its subcategories).

        This class contains the methods defined in the nested class
        ``self.MorphismMethods`` (if it exists), and has as bases the
        morphism classes of the super categories of ``self``.

        .. SEEALSO::

            - :meth:`parent_class`, :meth:`element_class`
            - :class:`Category` for details

        EXAMPLES::

            sage: C = Algebras(QQ).morphism_class; C
            <class 'sage.categories.algebras.Algebras.morphism_class'>
            sage: type(C)
            <class 'sage.structure.dynamic_class.DynamicMetaclass'>
        """
    def required_methods(self) -> dict[
        Literal["parent", "element"], 
        dict[Literal["required", "optional"], list[str]]]:
        """
        Return the methods that are required and optional for parents
        in this category and their elements.

        EXAMPLES::

            sage: Algebras(QQ).required_methods()
            {'element': {'optional': ['_add_', '_mul_'], 'required': ['__bool__']},
             'parent': {'optional': ['algebra_generators'], 'required': ['__contains__']}}
        """
    def is_subcategory(self, c: Category) -> bool:
        """
        Return ``True`` if there is a natural forgetful functor from ``self`` to `c`.

        EXAMPLES::

            sage: AbGrps = CommutativeAdditiveGroups()
            sage: Rings().is_subcategory(AbGrps)
            True
            sage: AbGrps.is_subcategory(Rings())
            False

        The ``is_subcategory`` function takes into account the
        base.

        ::

            sage: M3 = VectorSpaces(FiniteField(3))
            sage: M9 = VectorSpaces(FiniteField(9, 'a'))                                # needs sage.rings.finite_rings
            sage: M3.is_subcategory(M9)                                                 # needs sage.rings.finite_rings
            False

        Join categories are properly handled::

            sage: CatJ = Category.join((CommutativeAdditiveGroups(), Semigroups()))
            sage: Rings().is_subcategory(CatJ)
            True

        ::

            sage: V3 = VectorSpaces(FiniteField(3))
            sage: POSet = PartiallyOrderedSets()
            sage: PoV3 = Category.join((V3, POSet))
            sage: A3 = AlgebrasWithBasis(FiniteField(3))
            sage: PoA3 = Category.join((A3, POSet))
            sage: PoA3.is_subcategory(PoV3)
            True
            sage: PoV3.is_subcategory(PoV3)
            True
            sage: PoV3.is_subcategory(PoA3)
            False
        """
    def or_subcategory(
        self, 
        category: Category | list[Category] | tuple[Category, ...] | None = None, 
        join: bool = False) -> Category:
        """
        Return ``category`` or ``self`` if ``category`` is ``None``.

        INPUT:

        - ``category`` -- a sub category of ``self``, tuple/list thereof,
          or ``None``
        - ``join`` -- boolean (default: ``False``)

        OUTPUT: a category

        EXAMPLES::

            sage: Monoids().or_subcategory(Groups())
            Category of groups
            sage: Monoids().or_subcategory(None)
            Category of monoids

        If category is a list/tuple, then a join category is returned::

            sage: Monoids().or_subcategory((CommutativeAdditiveMonoids(), Groups()))
            Join of Category of groups and Category of commutative additive monoids

        If ``join`` is ``False``, an error if raised if category is not a
        subcategory of ``self``::

            sage: Monoids().or_subcategory(EnumeratedSets())
            Traceback (most recent call last):
            ...
            ValueError: Subcategory of `Category of monoids` required;
            got `Category of enumerated sets`

        Otherwise, the two categories are joined together::

            sage: Monoids().or_subcategory(EnumeratedSets(), join=True)
            Category of enumerated monoids
        """
    @staticmethod
    def meet(categories: Iterable[Category]) -> Category:
        """
        Return the meet of a list of categories.

        INPUT:

        - ``categories`` -- a non empty list (or iterable) of categories

        .. SEEALSO:: :meth:`__or__` for a shortcut

        EXAMPLES::

            sage: Category.meet([Algebras(ZZ), Algebras(QQ), Groups()])
            Category of monoids

        That meet of an empty list should be a category which is a
        subcategory of all categories, which does not make practical sense::

            sage: Category.meet([])
            Traceback (most recent call last):
            ...
            ValueError: The meet of an empty list of categories is not implemented
        """
    @cached_method
    def axioms(self) -> frozenset[str]:
        """
        Return the axioms known to be satisfied by all the objects of ``self``.

        Technically, this is the set of all the axioms ``A`` such that, if
        ``Cs`` is the category defining ``A``, then ``self`` is a subcategory
        of ``Cs().A()``. Any additional axiom ``A`` would yield a strict
        subcategory of ``self``, at the very least ``self & Cs().A()`` where
        ``Cs`` is the category defining ``A``.

        EXAMPLES::

            sage: Monoids().axioms()
            frozenset({'Associative', 'Unital'})
            sage: (EnumeratedSets().Infinite() & Sets().Facade()).axioms()
            frozenset({'Enumerated', 'Facade', 'Infinite'})
        """
    def __and__(self, other: Category) -> Category:
        """
        Return the intersection of two categories.

        This is just a shortcut for :meth:`join`.

        EXAMPLES::

            sage: Sets().Finite() & Rings().Commutative()
            Category of finite commutative rings
            sage: Monoids() & CommutativeAdditiveMonoids()
            Join of Category of monoids and Category of commutative additive monoids
        """
    def __or__(self, other: Category) -> Category:
        """
        Return the smallest category containing the two categories.

        This is just a shortcut for :meth:`meet`.

        EXAMPLES::

            sage: Algebras(QQ) | Groups()
            Category of monoids
        """
    @overload
    @staticmethod
    def join(
        categories: Iterable[Category], 
        as_list: Literal[True], 
        ignore_axioms: tuple[str, ...] = (), axioms: tuple[str, ...] =()
    ) -> list[Category]: ...
    @overload
    @staticmethod
    def join(
        categories: Iterable[Category], 
        as_list: Literal[False] = False, 
        ignore_axioms: tuple[str, ...] = (), axioms: tuple[str, ...] =()
    ) -> Objects | Category | JoinCategory:
        """
        Return the join of the input categories in the lattice of categories.

        At the level of objects and morphisms, this operation
        corresponds to intersection: the objects and morphisms of a
        join category are those that belong to all its super
        categories.

        INPUT:

        - ``categories`` -- list (or iterable) of categories
        - ``as_list`` -- boolean (default: ``False``);
          whether the result should be returned as a list
        - ``axioms`` -- tuple of strings; the names of some
          supplementary axioms

        .. SEEALSO:: :meth:`__and__` for a shortcut

        EXAMPLES::

            sage: J = Category.join((Groups(), CommutativeAdditiveMonoids())); J
            Join of Category of groups and Category of commutative additive monoids
            sage: J.super_categories()
            [Category of groups, Category of commutative additive monoids]
            sage: J.all_super_categories(proper=True)
            [Category of groups, ..., Category of magmas,
             Category of commutative additive monoids, ..., Category of additive magmas,
             Category of sets, ...]

        As a short hand, one can use::

            sage: Groups() & CommutativeAdditiveMonoids()
            Join of Category of groups and Category of commutative additive monoids

        This is a commutative and associative operation::

            sage: Groups() & Posets()
            Join of Category of groups and Category of posets
            sage: Posets() & Groups()
            Join of Category of groups and Category of posets

            sage: Groups() & (CommutativeAdditiveMonoids() & Posets())
            Join of Category of groups
                and Category of commutative additive monoids
                and Category of posets
            sage: (Groups() & CommutativeAdditiveMonoids()) & Posets()
            Join of Category of groups
                and Category of commutative additive monoids
                and Category of posets

        The join of a single category is the category itself::

            sage: Category.join([Monoids()])
            Category of monoids

        Similarly, the join of several mutually comparable categories is
        the smallest one::

            sage: Category.join((Sets(), Rings(), Monoids()))
            Category of rings

        In particular, the unit is the top category :class:`Objects`::

            sage: Groups() & Objects()
            Category of groups

        If the optional parameter ``as_list`` is ``True``, this
        returns the super categories of the join as a list, without
        constructing the join category itself::

            sage: Category.join((Groups(), CommutativeAdditiveMonoids()), as_list=True)
            [Category of groups, Category of commutative additive monoids]
            sage: Category.join((Sets(), Rings(), Monoids()), as_list=True)
            [Category of rings]
            sage: Category.join((Modules(ZZ), FiniteFields()), as_list=True)
            [Category of finite enumerated fields, Category of modules over Integer Ring]
            sage: Category.join([], as_list=True)
            []
            sage: Category.join([Groups()], as_list=True)
            [Category of groups]
            sage: Category.join([Groups() & Posets()], as_list=True)
            [Category of groups, Category of posets]

        Support for axiom categories (TODO: put here meaningful examples)::

            sage: Sets().Facade() & Sets().Infinite()
            Category of facade infinite sets
            sage: Magmas().Infinite() & Sets().Facade()
            Category of facade infinite magmas

            sage: FiniteSets() & Monoids()
            Category of finite monoids
            sage: Rings().Commutative() & Sets().Finite()
            Category of finite commutative rings

        Note that several of the above examples are actually join
        categories; they are just nicely displayed::

            sage: AlgebrasWithBasis(QQ) & FiniteSets().Algebras(QQ)
            Join of Category of finite dimensional algebras with basis over Rational Field
                and Category of finite set algebras over Rational Field

            sage: UniqueFactorizationDomains() & Algebras(QQ)
            Join of Category of unique factorization domains
                and Category of commutative algebras over Rational Field

        TESTS::

            sage: Magmas().Unital().Commutative().Finite() is Magmas().Finite().Commutative().Unital()
            True
            sage: from sage.categories.category_with_axiom import TestObjects
            sage: T = TestObjects()
            sage: TCF = T.Commutative().Facade(); TCF
            Category of facade commutative test objects
            sage: TCF is T.Facade().Commutative()
            True
            sage: TCF is (T.Facade() & T.Commutative())
            True
            sage: TCF.axioms()
            frozenset({'Commutative', 'Facade'})
            sage: type(TCF)
            <class 'sage.categories.category_with_axiom.TestObjects.Commutative.Facade_with_category'>

            sage: TCF = T.Commutative().FiniteDimensional()
            sage: TCF is T.FiniteDimensional().Commutative()
            True
            sage: TCF is T.Commutative() & T.FiniteDimensional()
            True
            sage: TCF is T.FiniteDimensional() & T.Commutative()
            True
            sage: type(TCF)
            <class 'sage.categories.category_with_axiom.TestObjects.Commutative.FiniteDimensional_with_category'>

            sage: TCU = T.Commutative().Unital()
            sage: TCU is T.Unital().Commutative()
            True
            sage: TCU is T.Commutative() & T.Unital()
            True
            sage: TCU is T.Unital() & T.Commutative()
            True

            sage: TUCF = T.Unital().Commutative().FiniteDimensional(); TUCF
            Category of finite dimensional commutative unital test objects
            sage: type(TUCF)
            <class 'sage.categories.category_with_axiom.TestObjects.FiniteDimensional.Unital.Commutative_with_category'>

            sage: TFFC = T.Facade().FiniteDimensional().Commutative(); TFFC
            Category of facade finite dimensional commutative test objects
            sage: type(TFFC)
            <class 'sage.categories.category.JoinCategory_with_category'>
            sage: TFFC.super_categories()
            [Category of facade commutative test objects,
             Category of finite dimensional commutative test objects]
        """
    def category(self):
        """
        Return the category of this category. So far, all categories
        are in the category of objects.

        EXAMPLES::

            sage: Sets().category()
            Category of objects
            sage: VectorSpaces(QQ).category()
            Category of objects
        """
    def example(self, *args, **keywords):
        """
        Return an object in this category. Most of the time, this is a parent.

        This serves three purposes:

        - Give a typical example to better explain what the category is all about.
          (and by the way prove that the category is non empty :-) )
        - Provide a minimal template for implementing other objects in this category
        - Provide an object on which to test generic code implemented by the category

        For all those applications, the implementation of the object
        shall be kept to a strict minimum. The object is therefore not
        meant to be used for other applications; most of the time a
        full featured version is available elsewhere in Sage, and
        should be used instead.

        Technical note: by default ``FooBar(...).example()`` is
        constructed by looking up
        ``sage.categories.examples.foo_bar.Example`` and calling it as
        ``Example()``. Extra positional or named parameters are also
        passed down. For a category over base ring, the base ring is
        further passed down as an optional argument.

        Categories are welcome to override this default implementation.

        EXAMPLES::

            sage: Semigroups().example()
            An example of a semigroup: the left zero semigroup

            sage: Monoids().Subquotients().example()
            NotImplemented
        """

def is_Category(x: object) -> TypeGuard[Category]:
    """
    Return ``True`` if `x` is a category.

    EXAMPLES::

        sage: sage.categories.category.is_Category(CommutativeAdditiveSemigroups())
        doctest:warning...
        DeprecationWarning: the function is_Category is deprecated;
        use 'isinstance(..., Category)' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        True
        sage: sage.categories.category.is_Category(ZZ)
        False
    """
@cached_function
def category_sample() -> tuple[Category, ...]:
    """
    Return a sample of categories.

    It is constructed by looking for all concrete category classes declared in
    ``sage.categories.all``, calling :meth:`Category.an_instance` on those and
    taking all their super categories.

    EXAMPLES::

        sage: from sage.categories.category import category_sample
        sage: sorted(category_sample(), key=str)                                        # needs sage.groups
        [Category of Coxeter groups,
         Category of Dedekind domains,
         Category of G-sets for Symmetric group of order 8! as a permutation group,
         Category of Hecke modules over Rational Field,
         Category of Hopf algebras over Rational Field,
         Category of Hopf algebras with basis over Rational Field,
         Category of Jacobians over Rational Field,
         Category of Lie algebras over Rational Field,
         Category of Weyl groups,
         Category of abelian varieties over Rational Field,
         Category of additive magmas, ...,
         Category of fields, ...,
         Category of graded Hopf algebras with basis over Rational Field, ...,
         Category of modular abelian varieties over Rational Field, ...,
         Category of simplicial complexes, ...,
         Category of vector spaces over Rational Field, ...
    """
def category_graph(categories: Category | None = None) -> DiGraph:
    """
    Return the graph of the categories in Sage.

    INPUT:

    - ``categories`` -- list (or iterable) of categories

    If ``categories`` is specified, then the graph contains the
    mentioned categories together with all their super
    categories. Otherwise the graph contains (an instance of) each
    category in :mod:`sage.categories.all` (e.g. ``Algebras(QQ)`` for
    algebras).

    For readability, the names of the category are shortened.

    .. TODO:: Further remove the base ring (see also :issue:`15801`).

    EXAMPLES::

        sage: G = sage.categories.category.category_graph(categories=[Groups()])        # needs sage.graphs
        sage: G.vertices(sort=True)                                                     # needs sage.graphs
        ['groups', 'inverse unital magmas', 'magmas', 'monoids', 'objects',
         'semigroups', 'sets', 'sets with partial maps', 'unital magmas']
        sage: G.plot()                                                                  # needs sage.graphs sage.plot
        Graphics object consisting of 20 graphics primitives

        sage: sage.categories.category.category_graph().plot()                          # needs sage.graphs sage.groups sage.plot
        Graphics object consisting of ... graphics primitives
    """

class CategoryWithParameters(Category):
    """
    A parametrized category whose parent/element classes depend only on
    its super categories.

    Many categories in Sage are parametrized, like ``C = Algebras(K)``
    which takes a base ring as parameter. In many cases, however, the
    operations provided by ``C`` in the parent class and element class
    depend only on the super categories of ``C``. For example, the
    vector space operations are provided if and only if ``K`` is a
    field, since ``VectorSpaces(K)`` is a super category of ``C`` only
    in that case. In such cases, and as an optimization (see :issue:`11935`),
    we want to use the same parent and element class for all fields.
    This is the purpose of this abstract class.

    Currently, :class:`~sage.categories.category.JoinCategory`,
    :class:`~sage.categories.category_types.Category_over_base` and
    :class:`~sage.categories.bimodules.Bimodules` inherit from this
    class.

    EXAMPLES::

        sage: C1 = Algebras(GF(5))
        sage: C2 = Algebras(GF(3))
        sage: C3 = Algebras(ZZ)
        sage: from sage.categories.category import CategoryWithParameters
        sage: isinstance(C1, CategoryWithParameters)
        True
        sage: C1.parent_class is C2.parent_class
        True
        sage: C1.parent_class is C3.parent_class
        False

    .. automethod:: Category._make_named_class
    """

class JoinCategory(CategoryWithParameters):
    """
    A class for joins of several categories. Do not use directly;
    see Category.join instead.

    EXAMPLES::

        sage: from sage.categories.category import JoinCategory
        sage: J = JoinCategory((Groups(), CommutativeAdditiveMonoids())); J
        Join of Category of groups and Category of commutative additive monoids
        sage: J.super_categories()
        [Category of groups, Category of commutative additive monoids]
        sage: J.all_super_categories(proper=True)
        [Category of groups, ..., Category of magmas,
         Category of commutative additive monoids, ..., Category of additive magmas,
         Category of sets, Category of sets with partial maps, Category of objects]

    By :issue:`11935`, join categories and categories over base rings
    inherit from :class:`CategoryWithParameters`. This allows for
    sharing parent and element classes between similar categories. For
    example, since group algebras belong to a join category and since
    the underlying implementation is the same for all finite fields,
    we have::

        sage: # needs sage.groups sage.rings.finite_rings
        sage: G = SymmetricGroup(10)
        sage: A3 = G.algebra(GF(3))
        sage: A5 = G.algebra(GF(5))
        sage: type(A3.category())
        <class 'sage.categories.category.JoinCategory_with_category'>
        sage: type(A3) is type(A5)
        True

    .. automethod:: Category._repr_object_names
    .. automethod:: Category._repr_
    .. automethod:: Category._without_axioms
    """
    def __init__(self, super_categories: Sequence[Category], **kwds) -> None:
        """
        Initialize this JoinCategory.

        INPUT:

        - ``super_categories`` -- categories to join; this category will
          consist of objects and morphisms that lie in all of these
          categories

        - ``name`` -- ignored

        TESTS::

            sage: from sage.categories.category import JoinCategory
            sage: C = JoinCategory((Groups(), CommutativeAdditiveMonoids())); C
            Join of Category of groups and Category of commutative additive monoids
            sage: TestSuite(C).run()
        """
    def super_categories(self) -> list[Category]:
        """
        Return the immediate super categories, as per :meth:`Category.super_categories`.

        EXAMPLES::

            sage: from sage.categories.category import JoinCategory
            sage: JoinCategory((Semigroups(), FiniteEnumeratedSets())).super_categories()
            [Category of semigroups, Category of finite enumerated sets]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, a join category defines no additional structure.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: Modules(ZZ).additional_structure()
        """
    def is_subcategory(self, C: Category) -> bool: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Check whether this join category is subcategory of another
        category ``C``.

        EXAMPLES::

            sage: Category.join([Rings(),Modules(QQ)]).is_subcategory(Category.join([Rngs(),Bimodules(QQ,QQ)]))
            True
        """

from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.complex_double import CDF as CDF
from sage.rings.real_double import RDF as RDF
from sage.rings.real_mpfr import RR as RR, RR_min_prec as RR_min_prec
from sage.rings.real_mpfi import RIF as RIF