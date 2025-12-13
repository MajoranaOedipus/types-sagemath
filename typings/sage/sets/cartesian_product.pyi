from _typeshed import Incomplete
from sage.categories.rings import Rings as Rings
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.call import attrcall as attrcall
from sage.structure.element_wrapper import ElementWrapperCheckWrappedClass as ElementWrapperCheckWrappedClass
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CartesianProduct(UniqueRepresentation, Parent):
    """
    A class implementing a raw data structure for Cartesian products
    of sets (and elements thereof). See :obj:`cartesian_product` for
    how to construct full fledged Cartesian products.

    EXAMPLES::

        sage: G = cartesian_product([GF(5), Permutations(10)])
        sage: G.cartesian_factors()
        (Finite Field of size 5, Standard permutations of 10)
        sage: G.cardinality()
        18144000
        sage: G.random_element()    # random
        (1, [4, 7, 6, 5, 10, 1, 3, 2, 8, 9])
        sage: G.category()
        Join of Category of finite monoids
            and Category of Cartesian products of monoids
            and Category of Cartesian products of finite enumerated sets

    .. automethod:: CartesianProduct._cartesian_product_of_elements
    """
    def __init__(self, sets, category, flatten: bool = False) -> None:
        """
        INPUT:

        - ``sets`` -- tuple of parents
        - ``category`` -- a subcategory of ``Sets().CartesianProducts()``
        - ``flatten`` -- boolean (default: ``False``)

        ``flatten`` is current ignored, and reserved for future use.

        No other keyword arguments (``kwargs``) are accepted.

        TESTS::

            sage: from sage.sets.cartesian_product import CartesianProduct
            sage: C = CartesianProduct((QQ, ZZ, ZZ), category = Sets().CartesianProducts())
            sage: C
            The Cartesian product of (Rational Field, Integer Ring, Integer Ring)
            sage: C.an_element()
            (1/2, 1, 1)
            sage: TestSuite(C).run()
            sage: cartesian_product([ZZ, ZZ], blub=None)
            Traceback (most recent call last):
            ...
            TypeError: ...__init__() got an unexpected keyword argument 'blub'
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: C = cartesian_product([list(range(5)), list(range(5))])
            sage: (1, 1) in C
            True
            sage: (1, 6) in C
            False
        """
    def cartesian_factors(self):
        """
        Return the Cartesian factors of ``self``.

        .. SEEALSO::

            :meth:`Sets.CartesianProducts.ParentMethods.cartesian_factors()
            <sage.categories.sets_cat.Sets.CartesianProducts.ParentMethods.cartesian_factors>`.

        EXAMPLES::

            sage: cartesian_product([QQ, ZZ, ZZ]).cartesian_factors()
            (Rational Field, Integer Ring, Integer Ring)
        """
    @cached_method
    def cartesian_projection(self, i):
        """
        Return the natural projection onto the `i`-th Cartesian
        factor of ``self`` as per
        :meth:`Sets.CartesianProducts.ParentMethods.cartesian_projection()
        <sage.categories.sets_cat.Sets.CartesianProducts.ParentMethods.cartesian_projection>`.

        INPUT:

        - ``i`` -- the index of a Cartesian factor of ``self``

        EXAMPLES::

            sage: C = Sets().CartesianProducts().example(); C
            The Cartesian product of (Set of prime numbers (basic implementation), An example of an infinite enumerated set: the nonnegative integers, An example of a finite enumerated set: {1,2,3})
            sage: x = C.an_element(); x
            (47, 42, 1)
            sage: pi = C.cartesian_projection(1)
            sage: pi(x)
            42

            sage: C.cartesian_projection('hey')
            Traceback (most recent call last):
            ...
            ValueError: i (=hey) must be in {0, 1, 2}
        """
    def construction(self):
        """
        Return the construction functor and its arguments for this
        Cartesian product.

        OUTPUT:

        A pair whose first entry is a Cartesian product functor and
        its second entry is a list of the Cartesian factors.

        EXAMPLES::

            sage: cartesian_product([ZZ, QQ]).construction()
            (The cartesian_product functorial construction,
             (Integer Ring, Rational Field))
        """
    an_element: Incomplete
    class Element(ElementWrapperCheckWrappedClass):
        wrapped_class = tuple
        def cartesian_projection(self, i):
            """
            Return the projection of ``self`` on the `i`-th factor of
            the Cartesian product, as per
            :meth:`Sets.CartesianProducts.ElementMethods.cartesian_projection()
            <sage.categories.sets_cat.Sets.CartesianProducts.ElementMethods.cartesian_projection>`.

            INPUT:

            - ``i`` -- the index of a factor of the Cartesian product

            EXAMPLES::

                sage: C = Sets().CartesianProducts().example(); C
                The Cartesian product of (Set of prime numbers (basic implementation), An example of an infinite enumerated set: the nonnegative integers, An example of a finite enumerated set: {1,2,3})
                sage: x = C.an_element(); x
                (47, 42, 1)
                sage: x.cartesian_projection(1)
                42
            """
        __getitem__ = cartesian_projection
        def __iter__(self):
            """
            Iterate over the components of an element.

            EXAMPLES::

                sage: C = Sets().CartesianProducts().example(); C
                The Cartesian product of
                (Set of prime numbers (basic implementation),
                 An example of an infinite enumerated set: the nonnegative integers,
                 An example of a finite enumerated set: {1,2,3})
                sage: c = C.an_element(); c
                (47, 42, 1)
                sage: for i in c:
                ....:     print(i)
                47
                42
                1
            """
        def __len__(self) -> int:
            """
            Return the number of factors in the cartesian product from which ``self`` comes.

            EXAMPLES::

                sage: C = cartesian_product([ZZ, QQ, CC])                               # needs sage.rings.real_mpfr
                sage: e = C.random_element()                                            # needs sage.rings.real_mpfr
                sage: len(e)                                                            # needs sage.rings.real_mpfr
                3
            """
        def cartesian_factors(self):
            """
            Return the tuple of elements that compose this element.

            EXAMPLES::

                sage: A = cartesian_product([ZZ, RR])
                sage: A((1, 1.23)).cartesian_factors()                                  # needs sage.rings.real_mpfr
                (1, 1.23000000000000)
                sage: type(_)
                <... 'tuple'>
            """
