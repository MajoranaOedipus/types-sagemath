from sage.categories.category import Category as Category, CategoryWithParameters as CategoryWithParameters, JoinCategory as JoinCategory
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.unknown import Unknown as Unknown

class Elements(Category):
    """
    The category of all elements of a given parent.

    EXAMPLES::

        sage: a = IntegerRing()(5)
        sage: C = a.category(); C
        Category of elements of Integer Ring
        sage: a in C
        True
        sage: 2/3 in C
        False
        sage: loads(C.dumps()) == C
        True
    """
    def __init__(self, object) -> None:
        """
        EXAMPLES::

            sage: TestSuite(Elements(ZZ)).run()
        """
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: Elements.an_instance()
            Category of elements of Rational Field
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Elements(ZZ).super_categories()
            [Category of objects]

        .. TODO::

            Check that this is what we want.
        """
    def object(self):
        """
        EXAMPLES::

            sage: Elements(ZZ).object()
            Integer Ring
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: C = Elements(ZZ)
            sage: loads(dumps(C)) == C
            True
        """

class Category_over_base(CategoryWithParameters):
    """
    A base class for categories over some base object.

    INPUT:

    - ``base`` -- a category `C` or an object of such a category

    Assumption: the classes for the parents, elements, morphisms, of
    ``self`` should only depend on `C`. See :issue:`11935` for details.

    EXAMPLES::

        sage: Algebras(GF(2)).element_class is Algebras(GF(3)).element_class
        True

        sage: C = GF(2).category()
        sage: Algebras(GF(2)).parent_class is Algebras(C).parent_class
        True

        sage: C = ZZ.category()
        sage: Algebras(ZZ).element_class is Algebras(C).element_class
        True
    """
    def __init__(self, base, name=None) -> None:
        """
        Initialize ``self``.

        The ``name`` parameter is ignored.

        EXAMPLES::

            sage: S = Spec(ZZ)
            sage: C = Schemes(S); C
            Category of schemes over Integer Ring
            sage: C.__class__.__init__ == sage.categories.category_types.Category_over_base.__init__
            True
            sage: C.base() is S
            True
            sage: TestSuite(C).run()
        """
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: Algebras.an_instance()
            Category of algebras over Rational Field
        """
    def base(self):
        """
        Return the base over which elements of this category are
        defined.

        EXAMPLES::

            sage: C = Algebras(QQ)
            sage: C.base()
            Rational Field
        """

class AbelianCategory(Category):
    def is_abelian(self):
        """
        Return ``True`` as ``self`` is an abelian category.

        EXAMPLES::

            sage: CommutativeAdditiveGroups().is_abelian()
            True
        """

class Category_over_base_ring(Category_over_base):
    def __init__(self, base, name=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = Algebras(GF(2)); C
            Category of algebras over Finite Field of size 2
            sage: TestSuite(C).run()
        """
    def base_ring(self):
        """
        Return the base ring over which elements of this category are
        defined.

        EXAMPLES::

            sage: C = Algebras(GF(2))
            sage: C.base_ring()
            Finite Field of size 2
        """
    def __contains__(self, x) -> bool:
        """
        Return whether ``x`` is an object of this category.

        In most cases, ``x`` is an object in this category, if and
        only if the category of ``x`` is a subcategory of ``self``.
        Exception: ``x`` is also an object in this category if ``x``
        is in a category over a base ring category ``C``, and ``self``
        is a category over a base ring in ``C``.

        This method implements this exception.

        EXAMPLES::

            sage: QQ['x'] in Algebras(QQ)
            True
            sage: ZZ['x'] in Algebras(ZZ)
            True

        We also would want the following to hold::

            sage: QQ['x'] in Algebras(Fields()) # todo: not implemented
            True
        """

class Category_in_ambient(Category):
    def __init__(self, ambient, name=None) -> None:
        """
        Initialize ``self``.

        The parameter ``name`` is ignored.

        EXAMPLES::

            sage: C = Ideals(IntegerRing())
            sage: TestSuite(C).run()
        """
    def ambient(self):
        """
        Return the ambient object in which objects of this category are
        embedded.

        EXAMPLES::

            sage: C = Ideals(IntegerRing())
            sage: C.ambient()
            Integer Ring
        """

class Category_module(AbelianCategory, Category_over_base_ring): ...

class Category_ideal(Category_in_ambient):
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: AlgebraIdeals.an_instance()
            Category of algebra ideals in Univariate Polynomial Ring in x over Rational Field
        """
    def ring(self):
        """
        Return the ambient ring used to describe objects ``self``.

        EXAMPLES::

            sage: C = Ideals(IntegerRing())
            sage: C.ring()
            Integer Ring
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: C = Ideals(IntegerRing())
            sage: IntegerRing().zero_ideal() in C
            True
        """
    def __call__(self, v):
        """
        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: Ig = [x, y]
            sage: I = R.ideal(Ig)
            sage: C = Ideals(R)
            sage: C(Ig)
            Ideal (x, y) of Multivariate Polynomial Ring in x, y over Integer Ring
            sage: I == C(I)
            True
        """
