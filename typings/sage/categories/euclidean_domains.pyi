from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.structure.element import coerce_binop as coerce_binop
from sage.structure.sequence import Sequence as Sequence

class EuclideanDomains(Category_singleton):
    """
    The category of constructive euclidean domains, i.e., one can divide
    producing a quotient and a remainder where the remainder is either zero or
    its :meth:`ElementMethods.euclidean_degree` is smaller than the divisor.

    EXAMPLES::

      sage: EuclideanDomains()
      Category of euclidean domains
      sage: EuclideanDomains().super_categories()
      [Category of principal ideal domains]

    TESTS::

        sage: TestSuite(EuclideanDomains()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: EuclideanDomains().super_categories()
            [Category of principal ideal domains]
        """
    class ParentMethods:
        def is_euclidean_domain(self):
            """
            Return ``True``, since this in an object of the category of Euclidean domains.

            EXAMPLES::

                sage: Parent(QQ,category=EuclideanDomains()).is_euclidean_domain()
                True
            """
        def gcd_free_basis(self, elts):
            """
            Compute a set of coprime elements that can be used to express the
            elements of ``elts``.

            INPUT:

            - ``elts`` -- a sequence of elements of ``self``

            OUTPUT:

            A GCD-free basis (also called a coprime base) of ``elts``; that is,
            a set of pairwise relatively prime elements of ``self`` such that
            any element of ``elts`` can be written as a product of elements of
            the set.

            ALGORITHM:

            Naive implementation of the algorithm described in Section 4.8 of
            Bach & Shallit [BS1996]_.

            EXAMPLES::

                sage: ZZ.gcd_free_basis([1])
                []
                sage: ZZ.gcd_free_basis([4, 30, 14, 49])
                [2, 15, 7]

                sage: Pol.<x> = QQ[]
                sage: sorted(Pol.gcd_free_basis([
                ....:     (x+1)^3*(x+2)^3*(x+3), (x+1)*(x+2)*(x+3),
                ....:     (x+1)*(x+2)*(x+4)]))
                [x + 3, x + 4, x^2 + 3*x + 2]

            TESTS::

                sage: R.<x> = QQ[]
                sage: QQ.gcd_free_basis([x+1,x+2])
                Traceback (most recent call last):
                ...
                TypeError: unable to convert x + 1 to an element of Rational Field
            """
    class ElementMethods:
        @abstract_method
        def euclidean_degree(self) -> None:
            """
            Return the degree of this element as an element of a Euclidean
            domain, i.e., for elements `a`, `b` the euclidean degree `f`
            satisfies the usual properties:

            1. if `b` is not zero, then there are elements `q` and `r` such
               that `a = bq + r` with `r = 0` or `f(r) < f(b)`
            2. if `a,b` are not zero, then `f(a) \\leq f(ab)`

            .. NOTE::

                The name ``euclidean_degree`` was chosen because the euclidean
                function has different names in different contexts, e.g.,
                absolute value for integers, degree for polynomials.

            OUTPUT:

            For nonzero elements, a natural number. For the zero element, this
            might raise an exception or produce some other output, depending on
            the implementation.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: x.euclidean_degree()
                1
                sage: ZZ.one().euclidean_degree()
                1
            """
        @coerce_binop
        def gcd(self, other):
            """
            Return the greatest common divisor of this element and ``other``.

            INPUT:

            - ``other`` -- an element in the same ring as ``self``

            ALGORITHM:

            Algorithm 3.2.1 in [Coh1993]_.

            EXAMPLES::

                sage: R.<x> = PolynomialRing(QQ, sparse=True)
                sage: EuclideanDomains().element_class.gcd(x,x+1)
                -1
            """
        @abstract_method
        def quo_rem(self, other) -> None:
            """
            Return the quotient and remainder of the division of this element
            by the nonzero element ``other``.

            INPUT:

            - ``other`` -- an element in the same euclidean domain

            OUTPUT: a pair of elements

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: x.quo_rem(x)
                (1, 0)
            """
