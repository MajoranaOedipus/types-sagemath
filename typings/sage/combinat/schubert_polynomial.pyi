from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.key_polynomial import KeyPolynomial as KeyPolynomial
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial as InfinitePolynomial
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def SchubertPolynomialRing(R):
    """
    Return the Schubert polynomial ring over ``R`` on the X basis.

    This is the basis made of the Schubert polynomials.

    EXAMPLES::

        sage: X = SchubertPolynomialRing(ZZ); X
        Schubert polynomial ring with X basis over Integer Ring
        sage: TestSuite(X).run()
        sage: X(1)
        X[1]
        sage: X([1,2,3])*X([2,1,3])
        X[2, 1]
        sage: X([2,1,3])*X([2,1,3])
        X[3, 1, 2]
        sage: X([2,1,3])+X([3,1,2,4])
        X[2, 1] + X[3, 1, 2]
        sage: a = X([2,1,3])+X([3,1,2,4])
        sage: a^2
        X[3, 1, 2] + 2*X[4, 1, 2, 3] + X[5, 1, 2, 3, 4]
    """

class SchubertPolynomial_class(CombinatorialFreeModule.Element):
    def expand(self):
        """
        EXAMPLES::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: X([2,1,3]).expand()
            x0
            sage: [X(p).expand() for p in Permutations(3)]
            [1, x0 + x1, x0, x0*x1, x0^2, x0^2*x1]

        TESTS:

        Calling .expand() should always return an element of an
        MPolynomialRing::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: f = X([1]); f
            X[1]
            sage: type(f.expand())
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: f.expand()
            1
            sage: f = X([1,2])
            sage: type(f.expand())
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: f = X([1,3,2,4])
            sage: type(f.expand())
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>

        Now we check for correct handling of the empty
        permutation (:issue:`23443`)::

            sage: X([1]).expand() * X([2,1]).expand()
            x0
        """
    def divided_difference(self, i, algorithm: str = 'sage'):
        """
        Return the ``i``-th divided difference operator, applied to ``self``.

        Here, ``i`` can be either a permutation or a positive integer.

        INPUT:

        - ``i`` -- permutation or positive integer

        - ``algorithm`` -- (default: ``'sage'``) either ``'sage'``
          or ``'symmetrica'``; this determines which software is
          called for the computation

        OUTPUT:

        The result of applying the ``i``-th divided difference
        operator to ``self``.

        If `i` is a positive integer, then the `i`-th divided
        difference operator `\\delta_i` is the linear operator sending
        each polynomial `f = f(x_1, x_2, \\ldots, x_n)` (in
        `n \\geq i+1` variables) to the polynomial

        .. MATH::

            \\frac{f - f_i}{x_i - x_{i+1}}, \\qquad \\text{ where }
            f_i = f(x_1, x_2, ..., x_{i-1}, x_{i+1}, x_i,
            x_{i+1}, ..., x_n) .

        If `\\sigma` is a permutation in the `n`-th symmetric group,
        then the `\\sigma`-th divided difference operator `\\delta_\\sigma`
        is the composition
        `\\delta_{i_1} \\delta_{i_2} \\cdots \\delta_{i_k}`, where
        `\\sigma = s_{i_1} \\circ s_{i_2} \\circ \\cdots \\circ s_{i_k}` is
        any reduced expression for `\\sigma` (the precise choice of
        reduced expression is immaterial).

        .. NOTE::

            The :meth:`expand` method results in a polynomial
            in `n` variables named ``x0, x1, ..., x(n-1)`` rather than
            `x_1, x_2, \\ldots, x_n`.
            The variable named ``xi`` corresponds to `x_{i+1}`.
            Thus, ``self.divided_difference(i)`` involves the variables
            ``x(i-1)`` and ``xi`` getting switched (in the numerator).

        EXAMPLES::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: a = X([3,2,1])
            sage: a.divided_difference(1)
            X[2, 3, 1]
            sage: a.divided_difference([3,2,1])
            X[1]
            sage: a.divided_difference(5)
            0

        Any divided difference of `0` is `0`::

            sage: X.zero().divided_difference(2)
            0

        This is compatible when a permutation is given as input::

            sage: a = X([3,2,4,1])
            sage: a.divided_difference([2,3,1])
            0
            sage: a.divided_difference(1).divided_difference(2)
            0

        ::

            sage: a = X([4,3,2,1])
            sage: a.divided_difference([2,3,1])
            X[3, 2, 4, 1]
            sage: a.divided_difference(1).divided_difference(2)
            X[3, 2, 4, 1]
            sage: a.divided_difference([4,1,3,2])
            X[1, 4, 2, 3]
            sage: b = X([4, 1, 3, 2])
            sage: b.divided_difference(1).divided_difference(2)
            X[1, 3, 4, 2]
            sage: b.divided_difference(1).divided_difference(2).divided_difference(3)
            X[1, 3, 2]
            sage: b.divided_difference(1).divided_difference(2).divided_difference(3).divided_difference(2)
            X[1]
            sage: b.divided_difference(1).divided_difference(2).divided_difference(3).divided_difference(3)
            0
            sage: b.divided_difference(1).divided_difference(2).divided_difference(1)
            0

        TESTS:

        Check that :issue:`23403` is fixed::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: a = X([3,2,4,1])
            sage: a.divided_difference(2)
            0
            sage: a.divided_difference([3,2,1])
            0
            sage: a.divided_difference(0)
            Traceback (most recent call last):
            ...
            ValueError: cannot apply \\delta_{0} to a (= X[3, 2, 4, 1])
        """
    def scalar_product(self, x):
        """
        Return the standard scalar product of ``self`` and ``x``.

        EXAMPLES::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: a = X([3,2,4,1])
            sage: a.scalar_product(a)
            0
            sage: b = X([4,3,2,1])
            sage: b.scalar_product(a)
            X[1, 3, 4, 6, 2, 5]
            sage: Permutation([1, 3, 4, 6, 2, 5, 7]).to_lehmer_code()
            [0, 1, 1, 2, 0, 0, 0]
            sage: s = SymmetricFunctions(ZZ).schur()
            sage: c = s([2,1,1])
            sage: b.scalar_product(a).expand()
            x0^2*x1*x2 + x0*x1^2*x2 + x0*x1*x2^2 + x0^2*x1*x3 + x0*x1^2*x3
             + x0^2*x2*x3 + 3*x0*x1*x2*x3 + x1^2*x2*x3 + x0*x2^2*x3 + x1*x2^2*x3
             + x0*x1*x3^2 + x0*x2*x3^2 + x1*x2*x3^2
            sage: c.expand(4)
            x0^2*x1*x2 + x0*x1^2*x2 + x0*x1*x2^2 + x0^2*x1*x3 + x0*x1^2*x3
             + x0^2*x2*x3 + 3*x0*x1*x2*x3 + x1^2*x2*x3 + x0*x2^2*x3 + x1*x2^2*x3
             + x0*x1*x3^2 + x0*x2*x3^2 + x1*x2*x3^2
        """
    def multiply_variable(self, i):
        """
        Return the Schubert polynomial obtained by multiplying ``self``
        by the variable `x_i`.

        EXAMPLES::

            sage: X = SchubertPolynomialRing(ZZ)
            sage: a = X([3,2,4,1])
            sage: a.multiply_variable(0)
            X[4, 2, 3, 1]
            sage: a.multiply_variable(1)
            X[3, 4, 2, 1]
            sage: a.multiply_variable(2)
            X[3, 2, 5, 1, 4] - X[3, 4, 2, 1] - X[4, 2, 3, 1]
            sage: a.multiply_variable(3)
            X[3, 2, 4, 5, 1]
        """

class SchubertPolynomialRing_xbasis(CombinatorialFreeModule):
    Element = SchubertPolynomial_class
    def __init__(self, R) -> None:
        """
        EXAMPLES::

            sage: X = SchubertPolynomialRing(QQ)
            sage: X == loads(dumps(X))
            True
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the unit of this algebra.

        EXAMPLES::

            sage: X = SchubertPolynomialRing(QQ)
            sage: X.one()  # indirect doctest
            X[1]
        """
    def some_elements(self):
        """
        Return some elements.

        EXAMPLES::

            sage: X = SchubertPolynomialRing(QQ)
            sage: X.some_elements()
            [X[1], X[1] + 2*X[2, 1], -X[3, 2, 1] + X[4, 2, 1, 3]]
        """
    def product_on_basis(self, left, right):
        """
        EXAMPLES::

            sage: p1 = Permutation([3,2,1])
            sage: p2 = Permutation([2,1,3])
            sage: X = SchubertPolynomialRing(QQ)
            sage: X.product_on_basis(p1,p2)
            X[4, 2, 1, 3]
        """
