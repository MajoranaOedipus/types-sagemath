from _typeshed import Incomplete
from sage.categories.covariant_functorial_construction import CovariantConstructionCategory as CovariantConstructionCategory, CovariantFunctorialConstruction as CovariantFunctorialConstruction
from sage.typeset.unicode_characters import unicode_otimes as unicode_otimes

class TensorProductFunctor(CovariantFunctorialConstruction):
    """
    A singleton class for the tensor functor.

    This functor takes a collection of vector spaces (or modules with
    basis), and constructs the tensor product of those vector spaces.
    If this vector space is in a subcategory, say that of
    ``Algebras(QQ)``, it is automatically endowed with its natural
    algebra structure, thanks to the category
    ``Algebras(QQ).TensorProducts()`` of tensor products of algebras.
    For elements, it constructs the natural tensor product element in the
    corresponding tensor product of their parents.

    The tensor functor is covariant: if ``A`` is a subcategory of ``B``, then
    ``A.TensorProducts()`` is a subcategory of ``B.TensorProducts()`` (see
    also
    :class:`~sage.categories.covariant_functorial_construction.CovariantFunctorialConstruction`). Hence,
    the role of ``Algebras(QQ).TensorProducts()`` is solely to provide
    mathematical information and algorithms which are relevant to tensor
    product of algebras.

    Those are implemented in the nested class
    :class:`~sage.categories.algebras.Algebras.TensorProducts`
    of ``Algebras(QQ)``. This nested class is itself a subclass of
    :class:`~sage.categories.tensor.TensorProductsCategory`.


    TESTS::

        sage: TestSuite(tensor).run()
    """
    symbol: str
    unicode_symbol: Incomplete

tensor: Incomplete

class TensorProductsCategory(CovariantConstructionCategory):
    """
    An abstract base class for all TensorProducts's categories.

    TESTS::

        sage: C = ModulesWithBasis(QQ).TensorProducts()
        sage: C
        Category of tensor products of vector spaces with basis over Rational Field
        sage: C.base_category()
        Category of vector spaces with basis over Rational Field
        sage: latex(C)
        \\mathbf{TensorProducts}(\\mathbf{WithBasis}_{\\Bold{Q}})
        sage: TestSuite(C).run()
    """
    def TensorProducts(self):
        """
        Return the category of tensor products of objects of ``self``.

        By associativity of tensor products, this is ``self`` (a tensor
        product of tensor products of `Cat`'s is a tensor product of `Cat`'s)

        EXAMPLES::

            sage: ModulesWithBasis(QQ).TensorProducts().TensorProducts()
            Category of tensor products of vector spaces with basis over Rational Field
        """
    def base(self):
        """
        The base of a tensor product is the base (usually a ring) of the underlying category.

        EXAMPLES::

            sage: ModulesWithBasis(ZZ).TensorProducts().base()
            Integer Ring
        """
