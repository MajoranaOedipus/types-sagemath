import sage.structure.parent
from sage.categories.algebras import Algebras as Algebras
from sage.libs.singular.function import lib as lib
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.noncommutative_ideals import IdealMonoid_nc as IdealMonoid_nc
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class FreeAlgebra_letterplace(sage.structure.parent.Parent):
    '''FreeAlgebra_letterplace(R, degrees=None)

    File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 199)

    Finitely generated free algebra, with arithmetic restricted to weighted homogeneous elements.

    .. NOTE::

        The restriction to weighted homogeneous elements should be lifted
        as soon as the restriction to homogeneous elements is lifted in
        Singular\'s "Letterplace algebras".

    EXAMPLES::

        sage: K.<z> = GF(25)
        sage: F.<a,b,c> = FreeAlgebra(K, implementation=\'letterplace\')
        sage: F
        Free Associative Unital Algebra on 3 generators (a, b, c) over Finite Field in z of size 5^2
        sage: P = F.commutative_ring()
        sage: P
        Multivariate Polynomial Ring in a, b, c over Finite Field in z of size 5^2

    We can do arithmetic as usual, as long as we stay (weighted) homogeneous::

        sage: (z*a+(z+1)*b+2*c)^2
        (z + 3)*a*a + (2*z + 3)*a*b + (2*z)*a*c + (2*z + 3)*b*a + (3*z + 4)*b*b + (2*z + 2)*b*c + (2*z)*c*a + (2*z + 2)*c*b - c*c
        sage: a+1
        Traceback (most recent call last):
        ...
        ArithmeticError: can only add elements of the same weighted degree'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R, degrees=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 230)

                INPUT:

                A multivariate polynomial ring of type :class:`~sage.rings.polynomial.multipolynomial_libsingular.MPolynomialRing_libsingular`.

                OUTPUT: the free associative version of the given commutative ring

                .. NOTE::

                    One is supposed to use the :class:`FreeAlgebra` constructor,
                    in order to use the cache.

                TESTS::

                    sage: from sage.algebras.letterplace.free_algebra_letterplace import FreeAlgebra_letterplace
                    sage: FreeAlgebra_letterplace(QQ['x','y'])
                    Free Associative Unital Algebra on 2 generators (x, y) over Rational Field
                    sage: FreeAlgebra_letterplace(QQ['x'])
                    Traceback (most recent call last):
                    ...
                    TypeError: a letterplace algebra must be provided by a polynomial ring of type <... 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>

                ::

                    sage: K.<z> = GF(25)
                    sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace')
                    sage: TestSuite(F).run()
        """
    @overload
    def commutative_ring(self) -> Any:
        """FreeAlgebra_letterplace.commutative_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 383)

        Return the commutative version of this free algebra.

        .. NOTE::

            This commutative ring is used as a unique key of the free algebra.

        EXAMPLES::

            sage: K.<z> = GF(25)
            sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace')
            sage: F
            Free Associative Unital Algebra on 3 generators (a, b, c) over Finite Field in z of size 5^2
            sage: F.commutative_ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field in z of size 5^2
            sage: FreeAlgebra(F.commutative_ring()) is F
            True"""
    @overload
    def commutative_ring(self) -> Any:
        """FreeAlgebra_letterplace.commutative_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 383)

        Return the commutative version of this free algebra.

        .. NOTE::

            This commutative ring is used as a unique key of the free algebra.

        EXAMPLES::

            sage: K.<z> = GF(25)
            sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace')
            sage: F
            Free Associative Unital Algebra on 3 generators (a, b, c) over Finite Field in z of size 5^2
            sage: F.commutative_ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field in z of size 5^2
            sage: FreeAlgebra(F.commutative_ring()) is F
            True"""
    @overload
    def commutative_ring(self) -> Any:
        """FreeAlgebra_letterplace.commutative_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 383)

        Return the commutative version of this free algebra.

        .. NOTE::

            This commutative ring is used as a unique key of the free algebra.

        EXAMPLES::

            sage: K.<z> = GF(25)
            sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace')
            sage: F
            Free Associative Unital Algebra on 3 generators (a, b, c) over Finite Field in z of size 5^2
            sage: F.commutative_ring()
            Multivariate Polynomial Ring in a, b, c over Finite Field in z of size 5^2
            sage: FreeAlgebra(F.commutative_ring()) is F
            True"""
    @overload
    def current_ring(self) -> Any:
        """FreeAlgebra_letterplace.current_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 363)

        Return the commutative ring that is used to emulate
        the non-commutative multiplication out to the current degree.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c over Rational Field
            sage: a*b
            a*b
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1 over Rational Field
            sage: F.set_degbound(3)
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1, a_2, b_2, c_2 over Rational Field"""
    @overload
    def current_ring(self) -> Any:
        """FreeAlgebra_letterplace.current_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 363)

        Return the commutative ring that is used to emulate
        the non-commutative multiplication out to the current degree.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c over Rational Field
            sage: a*b
            a*b
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1 over Rational Field
            sage: F.set_degbound(3)
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1, a_2, b_2, c_2 over Rational Field"""
    @overload
    def current_ring(self) -> Any:
        """FreeAlgebra_letterplace.current_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 363)

        Return the commutative ring that is used to emulate
        the non-commutative multiplication out to the current degree.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c over Rational Field
            sage: a*b
            a*b
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1 over Rational Field
            sage: F.set_degbound(3)
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1, a_2, b_2, c_2 over Rational Field"""
    @overload
    def current_ring(self) -> Any:
        """FreeAlgebra_letterplace.current_ring(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 363)

        Return the commutative ring that is used to emulate
        the non-commutative multiplication out to the current degree.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c over Rational Field
            sage: a*b
            a*b
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1 over Rational Field
            sage: F.set_degbound(3)
            sage: F.current_ring()
            Multivariate Polynomial Ring in a, b, c, a_1, b_1, c_1, a_2, b_2, c_2 over Rational Field"""
    @overload
    def degbound(self) -> Any:
        """FreeAlgebra_letterplace.degbound(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 469)

        Return the degree bound that is currently used.

        .. NOTE::

            When multiplying two elements of this free algebra, the degree
            bound will be dynamically adapted. It can also be set by
            :meth:`set_degbound`.

        EXAMPLES:

        In order to avoid we get a free algebras from the cache that
        was created in another doctest and has a different degree
        bound, we choose a base ring that does not appear in other tests::

            sage: F.<x,y,z> = FreeAlgebra(ZZ, implementation='letterplace')
            sage: F.degbound()
            1
            sage: x*y
            x*y
            sage: F.degbound()
            2
            sage: F.set_degbound(4)
            sage: F.degbound()
            4"""
    @overload
    def degbound(self) -> Any:
        """FreeAlgebra_letterplace.degbound(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 469)

        Return the degree bound that is currently used.

        .. NOTE::

            When multiplying two elements of this free algebra, the degree
            bound will be dynamically adapted. It can also be set by
            :meth:`set_degbound`.

        EXAMPLES:

        In order to avoid we get a free algebras from the cache that
        was created in another doctest and has a different degree
        bound, we choose a base ring that does not appear in other tests::

            sage: F.<x,y,z> = FreeAlgebra(ZZ, implementation='letterplace')
            sage: F.degbound()
            1
            sage: x*y
            x*y
            sage: F.degbound()
            2
            sage: F.set_degbound(4)
            sage: F.degbound()
            4"""
    @overload
    def degbound(self) -> Any:
        """FreeAlgebra_letterplace.degbound(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 469)

        Return the degree bound that is currently used.

        .. NOTE::

            When multiplying two elements of this free algebra, the degree
            bound will be dynamically adapted. It can also be set by
            :meth:`set_degbound`.

        EXAMPLES:

        In order to avoid we get a free algebras from the cache that
        was created in another doctest and has a different degree
        bound, we choose a base ring that does not appear in other tests::

            sage: F.<x,y,z> = FreeAlgebra(ZZ, implementation='letterplace')
            sage: F.degbound()
            1
            sage: x*y
            x*y
            sage: F.degbound()
            2
            sage: F.set_degbound(4)
            sage: F.degbound()
            4"""
    @overload
    def degbound(self) -> Any:
        """FreeAlgebra_letterplace.degbound(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 469)

        Return the degree bound that is currently used.

        .. NOTE::

            When multiplying two elements of this free algebra, the degree
            bound will be dynamically adapted. It can also be set by
            :meth:`set_degbound`.

        EXAMPLES:

        In order to avoid we get a free algebras from the cache that
        was created in another doctest and has a different degree
        bound, we choose a base ring that does not appear in other tests::

            sage: F.<x,y,z> = FreeAlgebra(ZZ, implementation='letterplace')
            sage: F.degbound()
            1
            sage: x*y
            x*y
            sage: F.degbound()
            2
            sage: F.set_degbound(4)
            sage: F.degbound()
            4"""
    def gen(self, i) -> Any:
        """FreeAlgebra_letterplace.gen(self, i)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 321)

        Return the `i`-th generator.

        INPUT:

        - ``i`` -- integer

        OUTPUT: the generator with index `i`

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.1 is F.1  # indirect doctest
            True
            sage: F.gen(2)
            c"""
    def generator_degrees(self) -> Any:
        """FreeAlgebra_letterplace.generator_degrees(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 419)"""
    @overload
    def gens(self) -> tuple:
        """FreeAlgebra_letterplace.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 351)

        Return the tuple of generators.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.gens()
            (a, b, c)"""
    @overload
    def gens(self) -> Any:
        """FreeAlgebra_letterplace.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 351)

        Return the tuple of generators.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.gens()
            (a, b, c)"""
    @overload
    def ideal_monoid(self) -> Any:
        """FreeAlgebra_letterplace.ideal_monoid(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 554)

        Return the monoid of ideals of this free algebra.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(GF(2), implementation='letterplace')
            sage: F.ideal_monoid()
            Monoid of ideals of Free Associative Unital Algebra on 2 generators (x, y) over Finite Field of size 2
            sage: F.ideal_monoid() is F.ideal_monoid()
            True"""
    @overload
    def ideal_monoid(self) -> Any:
        """FreeAlgebra_letterplace.ideal_monoid(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 554)

        Return the monoid of ideals of this free algebra.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(GF(2), implementation='letterplace')
            sage: F.ideal_monoid()
            Monoid of ideals of Free Associative Unital Algebra on 2 generators (x, y) over Finite Field of size 2
            sage: F.ideal_monoid() is F.ideal_monoid()
            True"""
    @overload
    def ideal_monoid(self) -> Any:
        """FreeAlgebra_letterplace.ideal_monoid(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 554)

        Return the monoid of ideals of this free algebra.

        EXAMPLES::

            sage: F.<x,y> = FreeAlgebra(GF(2), implementation='letterplace')
            sage: F.ideal_monoid()
            Monoid of ideals of Free Associative Unital Algebra on 2 generators (x, y) over Finite Field of size 2
            sage: F.ideal_monoid() is F.ideal_monoid()
            True"""
    @overload
    def is_field(self, proof=...) -> Any:
        """FreeAlgebra_letterplace.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 423)

        Tell whether this free algebra is a field.

        .. NOTE::

            This would only be the case in the degenerate case of no generators.
            But such an example cannot be constructed in this implementation.

        TESTS::

            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.is_field()
            False"""
    @overload
    def is_field(self) -> Any:
        """FreeAlgebra_letterplace.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 423)

        Tell whether this free algebra is a field.

        .. NOTE::

            This would only be the case in the degenerate case of no generators.
            But such an example cannot be constructed in this implementation.

        TESTS::

            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.is_field()
            False"""
    @overload
    def ngens(self) -> Any:
        """FreeAlgebra_letterplace.ngens(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 309)

        Return the number of generators.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.ngens()
            3"""
    @overload
    def ngens(self) -> Any:
        """FreeAlgebra_letterplace.ngens(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 309)

        Return the number of generators.

        EXAMPLES::

            sage: F.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.ngens()
            3"""
    def set_degbound(self, d) -> Any:
        """FreeAlgebra_letterplace.set_degbound(self, d)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 498)

        Increase the degree bound that is currently in place.

        .. NOTE::

            The degree bound cannot be decreased.

        EXAMPLES:

        In order to avoid we get a free algebras from the cache that
        was created in another doctest and has a different degree
        bound, we choose a base ring that does not appear in other tests::

            sage: F.<x,y,z> = FreeAlgebra(GF(251), implementation='letterplace')
            sage: F.degbound()
            1
            sage: x*y
            x*y
            sage: F.degbound()
            2
            sage: F.set_degbound(4)
            sage: F.degbound()
            4
            sage: F.set_degbound(2)
            sage: F.degbound()
            4"""
    @overload
    def term_order_of_block(self) -> Any:
        """FreeAlgebra_letterplace.term_order_of_block(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 404)

        Return the term order that is used for the commutative version of this free algebra.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.term_order_of_block()
            Degree reverse lexicographic term order
            sage: L.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace',order='lex')
            sage: L.term_order_of_block()
            Lexicographic term order"""
    @overload
    def term_order_of_block(self) -> Any:
        """FreeAlgebra_letterplace.term_order_of_block(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 404)

        Return the term order that is used for the commutative version of this free algebra.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.term_order_of_block()
            Degree reverse lexicographic term order
            sage: L.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace',order='lex')
            sage: L.term_order_of_block()
            Lexicographic term order"""
    @overload
    def term_order_of_block(self) -> Any:
        """FreeAlgebra_letterplace.term_order_of_block(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 404)

        Return the term order that is used for the commutative version of this free algebra.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
            sage: F.term_order_of_block()
            Degree reverse lexicographic term order
            sage: L.<a,b,c> = FreeAlgebra(QQ, implementation='letterplace',order='lex')
            sage: L.term_order_of_block()
            Lexicographic term order"""
    def __reduce__(self) -> Any:
        """FreeAlgebra_letterplace.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 293)

        TESTS::

            sage: K.<z> = GF(25)
            sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace')
            sage: loads(dumps(F)) is F    # indirect doctest
            True"""

class FreeAlgebra_letterplace_libsingular:
    """FreeAlgebra_letterplace_libsingular(commutative_ring, degbound)

    File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 887)

    Internally used wrapper around a Singular Letterplace polynomial ring."""
    def __init__(self, commutative_ring, degbound) -> Any:
        """File: /build/sagemath/src/sage/src/sage/algebras/letterplace/free_algebra_letterplace.pyx (starting at line 903)"""
