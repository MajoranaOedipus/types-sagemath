import _cython_3_2_1
import sage.structure.sage_object
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal as MPolynomialIdeal, NCPolynomialIdeal as NCPolynomialIdeal
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_GroebnerStrategy0: _cython_3_2_1.cython_function_or_method
unpickle_NCGroebnerStrategy0: _cython_3_2_1.cython_function_or_method

class GroebnerStrategy(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 38)

        A Wrapper for Singular's Groebner Strategy Object.

        This object provides functions for normal form computations and
        other functions for Groebner basis computation.

        ALGORITHM:

        Uses Singular via libSINGULAR
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def ideal(self) -> Any:
        """GroebnerStrategy.ideal(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 198)

        Return the ideal this strategy object is defined for.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(GF(32003))
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.ideal()
            Ideal (x + z, y + z) of Multivariate Polynomial Ring in x, y, z over Finite Field of size 32003"""
    @overload
    def ideal(self) -> Any:
        """GroebnerStrategy.ideal(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 198)

        Return the ideal this strategy object is defined for.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(GF(32003))
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.ideal()
            Ideal (x + z, y + z) of Multivariate Polynomial Ring in x, y, z over Finite Field of size 32003"""
    @overload
    def normal_form(self, MPolynomial_libsingularp) -> MPolynomial_libsingular:
        """GroebnerStrategy.normal_form(self, MPolynomial_libsingular p) -> MPolynomial_libsingular

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 263)

        Compute the normal form of ``p`` with respect to the
        generators of this object.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.normal_form(x*y) # indirect doctest
            z^2
            sage: strat.normal_form(x + 1)
            -z + 1

        TESTS::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([P(0)])
            sage: strat = GroebnerStrategy(I)
            sage: strat.normal_form(x)
            x
            sage: strat.normal_form(P(0))
            0"""
    @overload
    def normal_form(self, x) -> Any:
        """GroebnerStrategy.normal_form(self, MPolynomial_libsingular p) -> MPolynomial_libsingular

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 263)

        Compute the normal form of ``p`` with respect to the
        generators of this object.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.normal_form(x*y) # indirect doctest
            z^2
            sage: strat.normal_form(x + 1)
            -z + 1

        TESTS::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: I = Ideal([P(0)])
            sage: strat = GroebnerStrategy(I)
            sage: strat.normal_form(x)
            x
            sage: strat.normal_form(P(0))
            0"""
    @overload
    def ring(self) -> Any:
        """GroebnerStrategy.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 213)

        Return the ring this strategy object is defined over.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(GF(32003))
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.ring()
            Multivariate Polynomial Ring in x, y, z over Finite Field of size 32003"""
    @overload
    def ring(self) -> Any:
        """GroebnerStrategy.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 213)

        Return the ring this strategy object is defined over.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(GF(32003))
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: strat.ring()
            Multivariate Polynomial Ring in x, y, z over Finite Field of size 32003"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """GroebnerStrategy.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 250)

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import GroebnerStrategy
            sage: P.<x,y,z> = PolynomialRing(GF(32003))
            sage: I = Ideal([x + z, y + z])
            sage: strat = GroebnerStrategy(I)
            sage: loads(dumps(strat)) == strat
            True"""

class NCGroebnerStrategy(sage.structure.sage_object.SageObject):
    """NCGroebnerStrategy(L)

    File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 301)

    A Wrapper for Singular's Groebner Strategy Object.

    This object provides functions for normal form computations and
    other functions for Groebner basis computation.

    ALGORITHM:

    Uses Singular via libSINGULAR"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, L) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 312)

                Create a new :class:`GroebnerStrategy` object for the
                generators of the ideal ``L``.

                INPUT:

                - ``L`` -- an ideal in a g-algebra

                EXAMPLES::

                    sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
                    sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
                    sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
                    sage: I = H.ideal([y^2, x^2, z^2-H.one()])
                    sage: NCGroebnerStrategy(I) #random
                    Groebner Strategy for ideal generated by 3 elements over Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {z*x: x*z + 2*x, z*y: y*z - 2*y, y*x: x*y - z}

                TESTS::

                    sage: strat = NCGroebnerStrategy(None)
                    Traceback (most recent call last):
                    ...
                    TypeError: First parameter must be an ideal in a g-algebra.

                    sage: P.<x,y,z> = PolynomialRing(CC,order='neglex')
                    sage: I = Ideal([x+z,y+z+1])
                    sage: strat = NCGroebnerStrategy(I)
                    Traceback (most recent call last):
                    ...
                    TypeError:  First parameter must be an ideal in a g-algebra.

                Check that tail reduction is applied too::

                    sage: F = PolynomialRing(QQ,'t').fraction_field()
                    sage: FA = FreeAlgebra(F, 6, 'x1,x2,x3,x4,x5,x6')
                    sage: N = FA.g_algebra({FA.gen(j)*FA.gen(i):-FA.gen(i)*FA.gen(j) for i in range(5) for j in range(i+1,6)})
                    sage: I = N.ideal([g^2 for g in N.gens()],side='twosided')
                    sage: N.inject_variables()
                    Defining x1, x2, x3, x4, x5, x6
                    sage: I.reduce(x1*x2*x3 + x2^2*x4)
                    x1*x2*x3
        """
    @overload
    def ideal(self) -> Any:
        """NCGroebnerStrategy.ideal(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 443)

        Return the ideal this strategy object is defined for.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()])
            sage: strat = NCGroebnerStrategy(I)
            sage: strat.ideal() == I
            True"""
    @overload
    def ideal(self) -> Any:
        """NCGroebnerStrategy.ideal(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 443)

        Return the ideal this strategy object is defined for.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()])
            sage: strat = NCGroebnerStrategy(I)
            sage: strat.ideal() == I
            True"""
    def normal_form(self, NCPolynomial_pluralp) -> NCPolynomial_plural:
        """NCGroebnerStrategy.normal_form(self, NCPolynomial_plural p) -> NCPolynomial_plural

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 512)

        Compute the normal form of ``p`` with respect to the
        generators of this object.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: JL = H.ideal([x^3, y^3, z^3 - 4*z])
            sage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')
            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: SL = NCGroebnerStrategy(JL.std())
            sage: ST = NCGroebnerStrategy(JT.std())
            sage: SL.normal_form(x*y^2)
            x*y^2
            sage: ST.normal_form(x*y^2)
            y*z"""
    @overload
    def ring(self) -> Any:
        """NCGroebnerStrategy.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 459)

        Return the ring this strategy object is defined over.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()])
            sage: strat = NCGroebnerStrategy(I)
            sage: strat.ring() is H
            True"""
    @overload
    def ring(self) -> Any:
        """NCGroebnerStrategy.ring(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 459)

        Return the ring this strategy object is defined over.

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()])
            sage: strat = NCGroebnerStrategy(I)
            sage: strat.ring() is H
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """NCGroebnerStrategy.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/singular/groebner_strategy.pyx (starting at line 498)

        EXAMPLES::

            sage: from sage.libs.singular.groebner_strategy import NCGroebnerStrategy
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()])
            sage: strat = NCGroebnerStrategy(I)
            sage: loads(dumps(strat)) == strat
            True"""
