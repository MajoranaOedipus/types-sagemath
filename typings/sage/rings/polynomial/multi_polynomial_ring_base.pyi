import _cython_3_2_1
import sage as sage
import sage.categories as categories
import sage.rings.polynomial.polynomial_ring as polynomial_ring
import sage.rings.ring
from sage.arith.misc import binomial as binomial
from sage.categories.category import ZZ as ZZ
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.morphism import IdentityMorphism as IdentityMorphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing, polynomial_default_category as polynomial_default_category
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_MPolynomialRing: _cython_3_2_1.cython_function_or_method
unpickle_MPolynomialRing_generic: _cython_3_2_1.cython_function_or_method
unpickle_MPolynomialRing_generic_v1: _cython_3_2_1.cython_function_or_method

class BooleanPolynomialRing_base(MPolynomialRing_base):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1821)

        Abstract base class for :class:`~sage.rings.polynomial.pbori.pbori.BooleanPolynomialRing`.

        This class is defined for the purpose of ``isinstance`` tests.  It should not be
        instantiated.

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring_base import BooleanPolynomialRing_base
            sage: R.<x, y, z> = BooleanPolynomialRing()                                     # needs sage.rings.polynomial.pbori
            sage: isinstance(R, BooleanPolynomialRing_base)                                 # needs sage.rings.polynomial.pbori
            True

        By design, there is only one direct implementation subclass::

            sage: len(BooleanPolynomialRing_base.__subclasses__()) <= 1
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class MPolynomialRing_base(sage.rings.ring.CommutativeRing):
    """MPolynomialRing_base(base_ring, n, names, order)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 41)

                Create a polynomial ring in several variables over a commutative ring.

                EXAMPLES::

                    sage: R.<x,y> = ZZ['x,y']; R
                    Multivariate Polynomial Ring in x, y over Integer Ring
                    sage: cat = Rings().Commutative()
                    sage: class CR(Parent):
                    ....:     def __init__(self):
                    ....:         Parent.__init__(self, self, category=cat)
                    ....:     def __call__(self, x):
                    ....:         return None
                    sage: cr = CR()
                    sage: cr.is_commutative()
                    True
                    sage: cr['x,y']
                    Multivariate Polynomial Ring in x, y over
                    <__main__.CR_with_category object at ...>

                TESTS:

                Check that containment works correctly (:issue:`10355`)::

                    sage: A1.<a> = PolynomialRing(QQ)
                    sage: A2.<a,b> = PolynomialRing(QQ)
                    sage: 3 in A2
                    True
                    sage: A1(a) in A2
                    True

                Check that :issue:`26958` is fixed::

                    sage: from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular            # needs sage.libs.singular
                    sage: class Foo(MPolynomialRing_libsingular):                                                               # needs sage.libs.singular
                    ....:     pass
                    sage: Foo(QQ, 2, ['x','y'], 'degrevlex')                                                                    # needs sage.libs.singular
                    Multivariate Polynomial Ring in x, y over Rational Field

                Check that :meth:`basis` works correctly::

                    sage: R = PolynomialRing(QQ, [])
                    sage: R.basis()
                    Lazy family (...monomial...(i))_{i in Integer vectors of length 0}
                    sage: [*R.basis()]
                    [1]
                    sage: R.<x,y> = QQ[]
                    sage: R.basis()
                    Lazy family (...monomial...(i))_{i in Integer vectors of length 2}
                    sage: import itertools
                    sage: list(itertools.islice(R.basis(), 16))
                    [1, x, y, x^2, x*y, y^2, x^3, x^2*y, x*y^2, y^3, x^4, x^3*y, x^2*y^2, x*y^3, y^4, x^5]
        """
    @overload
    def change_ring(self, base_ring=..., names=..., order=...) -> Any:
        """MPolynomialRing_base.change_ring(self, base_ring=None, names=None, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1359)

        Return a new multivariate polynomial ring which is isomorphic to
        ``self``, but has a different ordering given by the parameter
        ``order`` or names given by the parameter ``names``.

        INPUT:

        - ``base_ring`` -- a base ring
        - ``names`` -- variable names
        - ``order`` -- a term order

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(GF(127), 3, order='lex')
            sage: x > y^2
            True
            sage: Q.<x,y,z> = P.change_ring(order='degrevlex')
            sage: x > y^2
            False"""
    @overload
    def change_ring(self, order=...) -> Any:
        """MPolynomialRing_base.change_ring(self, base_ring=None, names=None, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1359)

        Return a new multivariate polynomial ring which is isomorphic to
        ``self``, but has a different ordering given by the parameter
        ``order`` or names given by the parameter ``names``.

        INPUT:

        - ``base_ring`` -- a base ring
        - ``names`` -- variable names
        - ``order`` -- a term order

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(GF(127), 3, order='lex')
            sage: x > y^2
            True
            sage: Q.<x,y,z> = P.change_ring(order='degrevlex')
            sage: x > y^2
            False"""
    @overload
    def characteristic(self) -> Any:
        """MPolynomialRing_base.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 887)

        Return the characteristic of this polynomial ring.

        EXAMPLES::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.characteristic()
            0
            sage: R = PolynomialRing(GF(7), 'x', 20)
            sage: R.characteristic()
            7"""
    @overload
    def characteristic(self) -> Any:
        """MPolynomialRing_base.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 887)

        Return the characteristic of this polynomial ring.

        EXAMPLES::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.characteristic()
            0
            sage: R = PolynomialRing(GF(7), 'x', 20)
            sage: R.characteristic()
            7"""
    @overload
    def characteristic(self) -> Any:
        """MPolynomialRing_base.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 887)

        Return the characteristic of this polynomial ring.

        EXAMPLES::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.characteristic()
            0
            sage: R = PolynomialRing(GF(7), 'x', 20)
            sage: R.characteristic()
            7"""
    @overload
    def completion(self, names=..., prec=..., extras=..., **kwds) -> Any:
        """MPolynomialRing_base.completion(self, names=None, prec=20, extras={}, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 198)

        Return the completion of ``self`` with respect to the ideal
        generated by the variable(s) ``names``.

        INPUT:

        - ``names`` -- (optional) variable or list/tuple of variables
          (given either as elements of the polynomial ring or as strings);
          the default is all variables of ``self``
        - ``prec`` -- default precision of resulting power series ring,
          possibly infinite
        - ``extras`` -- passed as keywords to :class:`PowerSeriesRing`
          or :class:`LazyPowerSeriesRing`; can also be keyword arguments

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion('w')
            Power Series Ring in w over Multivariate Polynomial Ring in
             x, y, z over Integer Ring
            sage: P.completion((w,x,y))
            Multivariate Power Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring
            sage: Q.<w,x,y,z> = P.completion(); Q
            Multivariate Power Series Ring in w, x, y, z over Integer Ring

            sage: H = PolynomialRing(PolynomialRing(ZZ,3,'z'),4,'f'); H
            Multivariate Polynomial Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens())
            Multivariate Power Series Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens()[2])
            Power Series Ring in f2 over
             Multivariate Polynomial Ring in f0, f1, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion(prec=oo)                                                 # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in x, y, z, w over Integer Ring
            sage: P.completion((w,x,y), prec=oo)                                        # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring

        TESTS::

            sage: P.<x,y> = PolynomialRing(ZZ)
            sage: P.completion([]) is P
            True
            sage: P.completion(SR.var('x'))                                             # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: x is not an element of Multivariate Polynomial Ring
            in x, y over Integer Ring
            sage: P.completion(x + y)
            Traceback (most recent call last):
            ...
            ValueError: x + y is not a variable of Multivariate Polynomial
            Ring in x, y over Integer Ring
            sage: P.completion('q')
            Traceback (most recent call last):
            ...
            ValueError: q is not a variable of Multivariate Polynomial Ring
            in x, y over Integer Ring"""
    @overload
    def completion(self) -> Any:
        """MPolynomialRing_base.completion(self, names=None, prec=20, extras={}, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 198)

        Return the completion of ``self`` with respect to the ideal
        generated by the variable(s) ``names``.

        INPUT:

        - ``names`` -- (optional) variable or list/tuple of variables
          (given either as elements of the polynomial ring or as strings);
          the default is all variables of ``self``
        - ``prec`` -- default precision of resulting power series ring,
          possibly infinite
        - ``extras`` -- passed as keywords to :class:`PowerSeriesRing`
          or :class:`LazyPowerSeriesRing`; can also be keyword arguments

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion('w')
            Power Series Ring in w over Multivariate Polynomial Ring in
             x, y, z over Integer Ring
            sage: P.completion((w,x,y))
            Multivariate Power Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring
            sage: Q.<w,x,y,z> = P.completion(); Q
            Multivariate Power Series Ring in w, x, y, z over Integer Ring

            sage: H = PolynomialRing(PolynomialRing(ZZ,3,'z'),4,'f'); H
            Multivariate Polynomial Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens())
            Multivariate Power Series Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens()[2])
            Power Series Ring in f2 over
             Multivariate Polynomial Ring in f0, f1, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion(prec=oo)                                                 # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in x, y, z, w over Integer Ring
            sage: P.completion((w,x,y), prec=oo)                                        # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring

        TESTS::

            sage: P.<x,y> = PolynomialRing(ZZ)
            sage: P.completion([]) is P
            True
            sage: P.completion(SR.var('x'))                                             # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: x is not an element of Multivariate Polynomial Ring
            in x, y over Integer Ring
            sage: P.completion(x + y)
            Traceback (most recent call last):
            ...
            ValueError: x + y is not a variable of Multivariate Polynomial
            Ring in x, y over Integer Ring
            sage: P.completion('q')
            Traceback (most recent call last):
            ...
            ValueError: q is not a variable of Multivariate Polynomial Ring
            in x, y over Integer Ring"""
    @overload
    def completion(self, prec=...) -> Any:
        """MPolynomialRing_base.completion(self, names=None, prec=20, extras={}, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 198)

        Return the completion of ``self`` with respect to the ideal
        generated by the variable(s) ``names``.

        INPUT:

        - ``names`` -- (optional) variable or list/tuple of variables
          (given either as elements of the polynomial ring or as strings);
          the default is all variables of ``self``
        - ``prec`` -- default precision of resulting power series ring,
          possibly infinite
        - ``extras`` -- passed as keywords to :class:`PowerSeriesRing`
          or :class:`LazyPowerSeriesRing`; can also be keyword arguments

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion('w')
            Power Series Ring in w over Multivariate Polynomial Ring in
             x, y, z over Integer Ring
            sage: P.completion((w,x,y))
            Multivariate Power Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring
            sage: Q.<w,x,y,z> = P.completion(); Q
            Multivariate Power Series Ring in w, x, y, z over Integer Ring

            sage: H = PolynomialRing(PolynomialRing(ZZ,3,'z'),4,'f'); H
            Multivariate Polynomial Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens())
            Multivariate Power Series Ring in f0, f1, f2, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: H.completion(H.gens()[2])
            Power Series Ring in f2 over
             Multivariate Polynomial Ring in f0, f1, f3 over
             Multivariate Polynomial Ring in z0, z1, z2 over Integer Ring

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.completion(prec=oo)                                                 # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in x, y, z, w over Integer Ring
            sage: P.completion((w,x,y), prec=oo)                                        # needs sage.combinat
            Multivariate Lazy Taylor Series Ring in w, x, y over
             Univariate Polynomial Ring in z over Integer Ring

        TESTS::

            sage: P.<x,y> = PolynomialRing(ZZ)
            sage: P.completion([]) is P
            True
            sage: P.completion(SR.var('x'))                                             # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: x is not an element of Multivariate Polynomial Ring
            in x, y over Integer Ring
            sage: P.completion(x + y)
            Traceback (most recent call last):
            ...
            ValueError: x + y is not a variable of Multivariate Polynomial
            Ring in x, y over Integer Ring
            sage: P.completion('q')
            Traceback (most recent call last):
            ...
            ValueError: q is not a variable of Multivariate Polynomial Ring
            in x, y over Integer Ring"""
    @overload
    def construction(self) -> Any:
        """MPolynomialRing_base.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 162)

        Return a functor ``F`` and base ring ``R`` such that ``F(R) == self``.

        EXAMPLES::

            sage: S = ZZ['x,y']
            sage: F, R = S.construction(); R
            Integer Ring
            sage: F
            MPoly[x,y]
            sage: F(R) == S
            True
            sage: F(R) == ZZ['x']['y']
            False"""
    @overload
    def construction(self) -> Any:
        """MPolynomialRing_base.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 162)

        Return a functor ``F`` and base ring ``R`` such that ``F(R) == self``.

        EXAMPLES::

            sage: S = ZZ['x,y']
            sage: F, R = S.construction(); R
            Integer Ring
            sage: F
            MPoly[x,y]
            sage: F(R) == S
            True
            sage: F(R) == ZZ['x']['y']
            False"""
    @overload
    def flattening_morphism(self) -> Any:
        """MPolynomialRing_base.flattening_morphism(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 138)

        Return the flattening morphism of this polynomial ring.

        EXAMPLES::

            sage: QQ['a','b']['x','y'].flattening_morphism()
            Flattening morphism:
              From: Multivariate Polynomial Ring in x, y
                    over Multivariate Polynomial Ring in a, b over Rational Field
              To:   Multivariate Polynomial Ring in a, b, x, y over Rational Field

            sage: QQ['x,y'].flattening_morphism()
            Identity endomorphism of
             Multivariate Polynomial Ring in x, y over Rational Field"""
    @overload
    def flattening_morphism(self) -> Any:
        """MPolynomialRing_base.flattening_morphism(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 138)

        Return the flattening morphism of this polynomial ring.

        EXAMPLES::

            sage: QQ['a','b']['x','y'].flattening_morphism()
            Flattening morphism:
              From: Multivariate Polynomial Ring in x, y
                    over Multivariate Polynomial Ring in a, b over Rational Field
              To:   Multivariate Polynomial Ring in a, b, x, y over Rational Field

            sage: QQ['x,y'].flattening_morphism()
            Identity endomorphism of
             Multivariate Polynomial Ring in x, y over Rational Field"""
    @overload
    def flattening_morphism(self) -> Any:
        """MPolynomialRing_base.flattening_morphism(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 138)

        Return the flattening morphism of this polynomial ring.

        EXAMPLES::

            sage: QQ['a','b']['x','y'].flattening_morphism()
            Flattening morphism:
              From: Multivariate Polynomial Ring in x, y
                    over Multivariate Polynomial Ring in a, b over Rational Field
              To:   Multivariate Polynomial Ring in a, b, x, y over Rational Field

            sage: QQ['x,y'].flattening_morphism()
            Identity endomorphism of
             Multivariate Polynomial Ring in x, y over Rational Field"""
    def gen(self, n=...) -> Any:
        """MPolynomialRing_base.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 902)"""
    @overload
    def interpolation(self, bound, *args) -> Any:
        """MPolynomialRing_base.interpolation(self, bound, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 371)

        Create a polynomial with specified evaluations.

        CALL FORMATS:

        This function can be called in two ways:

        1. ``interpolation(bound, points, values)``

        2. ``interpolation(bound, function)``

        INPUT:

        - ``bound`` -- either an integer bounding the total degree or a
          list/tuple of integers bounding the degree of the variables

        - ``points`` -- list/tuple containing the evaluation points

        - ``values`` -- list/tuple containing the desired values at ``points``

        - ``function`` -- evaluable function in `n` variables, where `n` is the
          number of variables of the polynomial ring

        OUTPUT:

        1. A polynomial respecting the bounds and having ``values`` as values
           when evaluated at ``points``.

        2. A polynomial respecting the bounds and having the same values as
           ``function`` at exactly so many points so that the polynomial is
           unique.

        EXAMPLES::

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation(4, F)                                                 # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation([3,1,2], F)                                           # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: points = [(5,1,1),(7,2,2),(8,5,-1),(2,5,3),(1,4,0),(5,9,0),
            ....: (2,7,0),(1,10,13),(0,0,1),(-1,1,0),(2,5,3),(1,1,1),(7,4,11),
            ....: (12,1,9),(1,1,3),(4,-1,2),(0,1,5),(5,1,3),(3,1,-2),(2,11,3),
            ....: (4,12,19),(3,1,1),(5,2,-3),(12,1,1),(2,3,4)]
            sage: R.interpolation([3,1,2], points, [F(*x) for x in points])             # needs sage.modules
            x^3*y + z^2 + y + 25

        ALGORITHM:

        Solves a linear system of equations with the linear algebra module. If
        the points are not specified, it samples exactly as many points as
        needed for a unique solution.

        .. NOTE::

            It will only run if the base ring is a field, even though it might
            work otherwise as well. If your base ring is an integral domain,
            let it run over the fraction field.

            Also, if the solution is not unique, it spits out one solution,
            without any notice that there are more.

            For interpolation in the univariate case use
            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`.

        .. WARNING::

            If you don't provide point/value pairs but just a function, it
            will only use as many points as needed for a unique solution with
            the given bounds. In particular it will *not* notice or check
            whether the result yields the correct evaluation for other points
            as well. So if you give wrong bounds, you will get a wrong answer
            without any warning. ::

                sage: def F(a, b, c):
                ....:     return a^3*b + b + c^2 + 25
                ....:
                sage: R.<x,y,z> = PolynomialRing(QQ)
                sage: R.interpolation(3, F)                                             # needs sage.modules
                1/2*x^3 + x*y + z^2 - 1/2*x + y + 25

        .. SEEALSO::

            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`"""
    @overload
    def interpolation(self, bound, points, values) -> Any:
        """MPolynomialRing_base.interpolation(self, bound, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 371)

        Create a polynomial with specified evaluations.

        CALL FORMATS:

        This function can be called in two ways:

        1. ``interpolation(bound, points, values)``

        2. ``interpolation(bound, function)``

        INPUT:

        - ``bound`` -- either an integer bounding the total degree or a
          list/tuple of integers bounding the degree of the variables

        - ``points`` -- list/tuple containing the evaluation points

        - ``values`` -- list/tuple containing the desired values at ``points``

        - ``function`` -- evaluable function in `n` variables, where `n` is the
          number of variables of the polynomial ring

        OUTPUT:

        1. A polynomial respecting the bounds and having ``values`` as values
           when evaluated at ``points``.

        2. A polynomial respecting the bounds and having the same values as
           ``function`` at exactly so many points so that the polynomial is
           unique.

        EXAMPLES::

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation(4, F)                                                 # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation([3,1,2], F)                                           # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: points = [(5,1,1),(7,2,2),(8,5,-1),(2,5,3),(1,4,0),(5,9,0),
            ....: (2,7,0),(1,10,13),(0,0,1),(-1,1,0),(2,5,3),(1,1,1),(7,4,11),
            ....: (12,1,9),(1,1,3),(4,-1,2),(0,1,5),(5,1,3),(3,1,-2),(2,11,3),
            ....: (4,12,19),(3,1,1),(5,2,-3),(12,1,1),(2,3,4)]
            sage: R.interpolation([3,1,2], points, [F(*x) for x in points])             # needs sage.modules
            x^3*y + z^2 + y + 25

        ALGORITHM:

        Solves a linear system of equations with the linear algebra module. If
        the points are not specified, it samples exactly as many points as
        needed for a unique solution.

        .. NOTE::

            It will only run if the base ring is a field, even though it might
            work otherwise as well. If your base ring is an integral domain,
            let it run over the fraction field.

            Also, if the solution is not unique, it spits out one solution,
            without any notice that there are more.

            For interpolation in the univariate case use
            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`.

        .. WARNING::

            If you don't provide point/value pairs but just a function, it
            will only use as many points as needed for a unique solution with
            the given bounds. In particular it will *not* notice or check
            whether the result yields the correct evaluation for other points
            as well. So if you give wrong bounds, you will get a wrong answer
            without any warning. ::

                sage: def F(a, b, c):
                ....:     return a^3*b + b + c^2 + 25
                ....:
                sage: R.<x,y,z> = PolynomialRing(QQ)
                sage: R.interpolation(3, F)                                             # needs sage.modules
                1/2*x^3 + x*y + z^2 - 1/2*x + y + 25

        .. SEEALSO::

            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`"""
    @overload
    def interpolation(self, bound, function) -> Any:
        """MPolynomialRing_base.interpolation(self, bound, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 371)

        Create a polynomial with specified evaluations.

        CALL FORMATS:

        This function can be called in two ways:

        1. ``interpolation(bound, points, values)``

        2. ``interpolation(bound, function)``

        INPUT:

        - ``bound`` -- either an integer bounding the total degree or a
          list/tuple of integers bounding the degree of the variables

        - ``points`` -- list/tuple containing the evaluation points

        - ``values`` -- list/tuple containing the desired values at ``points``

        - ``function`` -- evaluable function in `n` variables, where `n` is the
          number of variables of the polynomial ring

        OUTPUT:

        1. A polynomial respecting the bounds and having ``values`` as values
           when evaluated at ``points``.

        2. A polynomial respecting the bounds and having the same values as
           ``function`` at exactly so many points so that the polynomial is
           unique.

        EXAMPLES::

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation(4, F)                                                 # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: R.interpolation([3,1,2], F)                                           # needs sage.modules
            x^3*y + z^2 + y + 25

            sage: def F(a, b, c):
            ....:     return a^3*b + b + c^2 + 25
            ....:
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: points = [(5,1,1),(7,2,2),(8,5,-1),(2,5,3),(1,4,0),(5,9,0),
            ....: (2,7,0),(1,10,13),(0,0,1),(-1,1,0),(2,5,3),(1,1,1),(7,4,11),
            ....: (12,1,9),(1,1,3),(4,-1,2),(0,1,5),(5,1,3),(3,1,-2),(2,11,3),
            ....: (4,12,19),(3,1,1),(5,2,-3),(12,1,1),(2,3,4)]
            sage: R.interpolation([3,1,2], points, [F(*x) for x in points])             # needs sage.modules
            x^3*y + z^2 + y + 25

        ALGORITHM:

        Solves a linear system of equations with the linear algebra module. If
        the points are not specified, it samples exactly as many points as
        needed for a unique solution.

        .. NOTE::

            It will only run if the base ring is a field, even though it might
            work otherwise as well. If your base ring is an integral domain,
            let it run over the fraction field.

            Also, if the solution is not unique, it spits out one solution,
            without any notice that there are more.

            For interpolation in the univariate case use
            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`.

        .. WARNING::

            If you don't provide point/value pairs but just a function, it
            will only use as many points as needed for a unique solution with
            the given bounds. In particular it will *not* notice or check
            whether the result yields the correct evaluation for other points
            as well. So if you give wrong bounds, you will get a wrong answer
            without any warning. ::

                sage: def F(a, b, c):
                ....:     return a^3*b + b + c^2 + 25
                ....:
                sage: R.<x,y,z> = PolynomialRing(QQ)
                sage: R.interpolation(3, F)                                             # needs sage.modules
                1/2*x^3 + x*y + z^2 - 1/2*x + y + 25

        .. SEEALSO::

            :meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_field.lagrange_polynomial`"""
    @overload
    def irrelevant_ideal(self) -> Any:
        """MPolynomialRing_base.irrelevant_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 182)

        Return the irrelevant ideal of this multivariate polynomial ring.

        This is the ideal generated by all of the indeterminate
        generators of this ring.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.irrelevant_ideal()
            Ideal (x, y, z) of Multivariate Polynomial Ring in x, y, z over
            Rational Field"""
    @overload
    def irrelevant_ideal(self) -> Any:
        """MPolynomialRing_base.irrelevant_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 182)

        Return the irrelevant ideal of this multivariate polynomial ring.

        This is the ideal generated by all of the indeterminate
        generators of this ring.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: R.irrelevant_ideal()
            Ideal (x, y, z) of Multivariate Polynomial Ring in x, y, z over
            Rational Field"""
    @overload
    def is_exact(self) -> bool:
        """MPolynomialRing_base.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 848)

        Test whether this multivariate polynomial ring is defined over an exact
        base ring.

        EXAMPLES::

            sage: PolynomialRing(QQ, 2, 'x').is_exact()
            True
            sage: PolynomialRing(RDF, 2, 'x').is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """MPolynomialRing_base.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 848)

        Test whether this multivariate polynomial ring is defined over an exact
        base ring.

        EXAMPLES::

            sage: PolynomialRing(QQ, 2, 'x').is_exact()
            True
            sage: PolynomialRing(RDF, 2, 'x').is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """MPolynomialRing_base.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 848)

        Test whether this multivariate polynomial ring is defined over an exact
        base ring.

        EXAMPLES::

            sage: PolynomialRing(QQ, 2, 'x').is_exact()
            True
            sage: PolynomialRing(RDF, 2, 'x').is_exact()
            False"""
    @overload
    def is_field(self, proof=...) -> Any:
        """MPolynomialRing_base.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 862)

        Test whether this multivariate polynomial ring is a field.

        A polynomial ring is a field when there are no variable and the base
        ring is a field.

        EXAMPLES::

            sage: PolynomialRing(QQ, 'x', 2).is_field()
            False
            sage: PolynomialRing(QQ, 'x', 0).is_field()
            True
            sage: PolynomialRing(ZZ, 'x', 0).is_field()
            False
            sage: PolynomialRing(Zmod(1), names=['x','y']).is_finite()
            True"""
    @overload
    def is_field(self) -> Any:
        """MPolynomialRing_base.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 862)

        Test whether this multivariate polynomial ring is a field.

        A polynomial ring is a field when there are no variable and the base
        ring is a field.

        EXAMPLES::

            sage: PolynomialRing(QQ, 'x', 2).is_field()
            False
            sage: PolynomialRing(QQ, 'x', 0).is_field()
            True
            sage: PolynomialRing(ZZ, 'x', 0).is_field()
            False
            sage: PolynomialRing(Zmod(1), names=['x','y']).is_finite()
            True"""
    @overload
    def is_field(self) -> Any:
        """MPolynomialRing_base.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 862)

        Test whether this multivariate polynomial ring is a field.

        A polynomial ring is a field when there are no variable and the base
        ring is a field.

        EXAMPLES::

            sage: PolynomialRing(QQ, 'x', 2).is_field()
            False
            sage: PolynomialRing(QQ, 'x', 0).is_field()
            True
            sage: PolynomialRing(ZZ, 'x', 0).is_field()
            False
            sage: PolynomialRing(Zmod(1), names=['x','y']).is_finite()
            True"""
    @overload
    def is_field(self) -> Any:
        """MPolynomialRing_base.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 862)

        Test whether this multivariate polynomial ring is a field.

        A polynomial ring is a field when there are no variable and the base
        ring is a field.

        EXAMPLES::

            sage: PolynomialRing(QQ, 'x', 2).is_field()
            False
            sage: PolynomialRing(QQ, 'x', 0).is_field()
            True
            sage: PolynomialRing(ZZ, 'x', 0).is_field()
            False
            sage: PolynomialRing(Zmod(1), names=['x','y']).is_finite()
            True"""
    @overload
    def is_integral_domain(self, proof=...) -> Any:
        """MPolynomialRing_base.is_integral_domain(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 116)

        EXAMPLES::

            sage: ZZ['x,y'].is_integral_domain()
            True
            sage: Integers(8)['x,y'].is_integral_domain()
            False"""
    @overload
    def is_integral_domain(self) -> Any:
        """MPolynomialRing_base.is_integral_domain(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 116)

        EXAMPLES::

            sage: ZZ['x,y'].is_integral_domain()
            True
            sage: Integers(8)['x,y'].is_integral_domain()
            False"""
    @overload
    def is_integral_domain(self) -> Any:
        """MPolynomialRing_base.is_integral_domain(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 116)

        EXAMPLES::

            sage: ZZ['x,y'].is_integral_domain()
            True
            sage: Integers(8)['x,y'].is_integral_domain()
            False"""
    @overload
    def is_noetherian(self) -> Any:
        """MPolynomialRing_base.is_noetherian(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 127)

        EXAMPLES::

            sage: ZZ['x,y'].is_noetherian()
            True
            sage: Integers(8)['x,y'].is_noetherian()
            True"""
    @overload
    def is_noetherian(self) -> Any:
        """MPolynomialRing_base.is_noetherian(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 127)

        EXAMPLES::

            sage: ZZ['x,y'].is_noetherian()
            True
            sage: Integers(8)['x,y'].is_noetherian()
            True"""
    @overload
    def is_noetherian(self) -> Any:
        """MPolynomialRing_base.is_noetherian(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 127)

        EXAMPLES::

            sage: ZZ['x,y'].is_noetherian()
            True
            sage: Integers(8)['x,y'].is_noetherian()
            True"""
    def krull_dimension(self) -> Any:
        """MPolynomialRing_base.krull_dimension(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 959)"""
    @overload
    def macaulay_resultant(self, *args, **kwds) -> Any:
        """MPolynomialRing_base.macaulay_resultant(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1586)

        Return the Macaulay resultant.

        This computes the resultant of universal polynomials as well as
        polynomials with constant coefficients. This is a project done
        in sage days 55. It is based on the implementation in Maple by
        Manfred Minimair, which in turn is based on the references
        listed below. It calculates the Macaulay resultant for a list
        of polynomials, up to sign!

        REFERENCES:

        - [CLO2005]_

        - [Can1990]_

        - [Mac1916]_

        AUTHORS:

        - Hao Chen, Solomon Vishkautsan (7-2014)

        INPUT:

        - ``args`` -- list of `n` homogeneous polynomials in `n` variables
          works when ``args[0]`` is the list of polynomials,
          or ``args`` is itself the list of polynomials

        kwds:

        - ``sparse`` -- boolean (default: ``False``); if ``True``, the function
          creates sparse matrices

        OUTPUT: the Macaulay resultant, an element of the base ring of ``self``

        .. TODO::

            Working with sparse matrices should usually give faster results,
            but with the current implementation it actually works slower.
            There should be a way to improve performance with regards to this.

        EXAMPLES:

        The number of polynomials has to match the number of variables::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z])                                      # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: number of polynomials(= 2) must equal number of variables (= 3)

        The polynomials need to be all homogeneous::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z, z + x^3])                             # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: resultant for non-homogeneous polynomials is not supported

        All polynomials must be in the same ring::

            sage: S.<x,y> = PolynomialRing(QQ, 2)
            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: S.macaulay_resultant([y, z+x])                                        # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: not all inputs are polynomials in the calling ring

        The following example recreates Proposition 2.10 in Ch.3 in [CLO2005]::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist, R = K._macaulay_resultant_universal_polynomials([1,1,2])
            sage: R.macaulay_resultant(flist)                                           # needs sage.modules
            u2^2*u4^2*u6 - 2*u1*u2*u4*u5*u6 + u1^2*u5^2*u6 - u2^2*u3*u4*u7 +
            u1*u2*u3*u5*u7 + u0*u2*u4*u5*u7 - u0*u1*u5^2*u7 + u1*u2*u3*u4*u8 -
            u0*u2*u4^2*u8 - u1^2*u3*u5*u8 + u0*u1*u4*u5*u8 + u2^2*u3^2*u9 -
            2*u0*u2*u3*u5*u9 + u0^2*u5^2*u9 - u1*u2*u3^2*u10 +
            u0*u2*u3*u4*u10 + u0*u1*u3*u5*u10 - u0^2*u4*u5*u10 +
            u1^2*u3^2*u11 - 2*u0*u1*u3*u4*u11 + u0^2*u4^2*u11

        The following example degenerates into the determinant of
        a `3\\times 3` matrix::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist,R = K._macaulay_resultant_universal_polynomials([1,1,1])
            sage: R.macaulay_resultant(flist)                                           # needs sage.modules
            -u2*u4*u6 + u1*u5*u6 + u2*u3*u7 - u0*u5*u7 - u1*u3*u8 + u0*u4*u8

        The following example is by Patrick Ingram (:arxiv:`1310.4114`)::

            sage: U = PolynomialRing(ZZ,'y',2); y0,y1 = U.gens()
            sage: R = PolynomialRing(U,'x',3); x0,x1,x2 = R.gens()
            sage: f0 = y0*x2^2 - x0^2 + 2*x1*x2
            sage: f1 = y1*x2^2 - x1^2 + 2*x0*x2
            sage: f2 = x0*x1 - x2^2
            sage: flist = [f0,f1,f2]
            sage: R.macaulay_resultant([f0,f1,f2])                                      # needs sage.modules
            y0^2*y1^2 - 4*y0^3 - 4*y1^3 + 18*y0*y1 - 27

        A simple example with constant rational coefficients::

            sage: R.<x,y,z,w> = PolynomialRing(QQ, 4)
            sage: R.macaulay_resultant([w, z, y, x])                                    # needs sage.modules
            1

        An example where the resultant vanishes::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([x + y, y^2, x])                                 # needs sage.modules
            0

        An example of bad reduction at a prime `p = 5`::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x^3 + 25*y^2*x, 5*z])                        # needs sage.libs.pari sage.modules
            125

        The input can given as an unpacked list of polynomials::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant(y, x^3 + 25*y^2*x, 5*z)                          # needs sage.libs.pari sage.modules
            125

        An example when the coefficients live in a finite field::

            sage: F = FiniteField(11)
            sage: R.<x,y,z,w> = PolynomialRing(F, 4)
            sage: R.macaulay_resultant([z, x^3, 5*y, w])                                # needs sage.modules sage.rings.finite_rings
            4

        Example when the denominator in the algorithm vanishes(in this case
        the resultant is the constant term of the quotient of
        char polynomials of numerator/denominator)::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z, z^2])                                 # needs sage.libs.pari sage.modules
            -1

        When there are only 2 polynomials, the Macaulay resultant degenerates
        to the traditional resultant::

            sage: R.<x> = PolynomialRing(QQ, 1)
            sage: f =  x^2 + 1; g = x^5 + 1
            sage: fh = f.homogenize()
            sage: gh = g.homogenize()
            sage: RH = fh.parent()
            sage: f.resultant(g) == RH.macaulay_resultant([fh, gh])                     # needs sage.modules
            True"""
    @overload
    def macaulay_resultant(self, flist) -> Any:
        """MPolynomialRing_base.macaulay_resultant(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1586)

        Return the Macaulay resultant.

        This computes the resultant of universal polynomials as well as
        polynomials with constant coefficients. This is a project done
        in sage days 55. It is based on the implementation in Maple by
        Manfred Minimair, which in turn is based on the references
        listed below. It calculates the Macaulay resultant for a list
        of polynomials, up to sign!

        REFERENCES:

        - [CLO2005]_

        - [Can1990]_

        - [Mac1916]_

        AUTHORS:

        - Hao Chen, Solomon Vishkautsan (7-2014)

        INPUT:

        - ``args`` -- list of `n` homogeneous polynomials in `n` variables
          works when ``args[0]`` is the list of polynomials,
          or ``args`` is itself the list of polynomials

        kwds:

        - ``sparse`` -- boolean (default: ``False``); if ``True``, the function
          creates sparse matrices

        OUTPUT: the Macaulay resultant, an element of the base ring of ``self``

        .. TODO::

            Working with sparse matrices should usually give faster results,
            but with the current implementation it actually works slower.
            There should be a way to improve performance with regards to this.

        EXAMPLES:

        The number of polynomials has to match the number of variables::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z])                                      # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: number of polynomials(= 2) must equal number of variables (= 3)

        The polynomials need to be all homogeneous::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z, z + x^3])                             # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: resultant for non-homogeneous polynomials is not supported

        All polynomials must be in the same ring::

            sage: S.<x,y> = PolynomialRing(QQ, 2)
            sage: R.<x,y,z> = PolynomialRing(QQ,3)
            sage: S.macaulay_resultant([y, z+x])                                        # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: not all inputs are polynomials in the calling ring

        The following example recreates Proposition 2.10 in Ch.3 in [CLO2005]::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist, R = K._macaulay_resultant_universal_polynomials([1,1,2])
            sage: R.macaulay_resultant(flist)                                           # needs sage.modules
            u2^2*u4^2*u6 - 2*u1*u2*u4*u5*u6 + u1^2*u5^2*u6 - u2^2*u3*u4*u7 +
            u1*u2*u3*u5*u7 + u0*u2*u4*u5*u7 - u0*u1*u5^2*u7 + u1*u2*u3*u4*u8 -
            u0*u2*u4^2*u8 - u1^2*u3*u5*u8 + u0*u1*u4*u5*u8 + u2^2*u3^2*u9 -
            2*u0*u2*u3*u5*u9 + u0^2*u5^2*u9 - u1*u2*u3^2*u10 +
            u0*u2*u3*u4*u10 + u0*u1*u3*u5*u10 - u0^2*u4*u5*u10 +
            u1^2*u3^2*u11 - 2*u0*u1*u3*u4*u11 + u0^2*u4^2*u11

        The following example degenerates into the determinant of
        a `3\\times 3` matrix::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist,R = K._macaulay_resultant_universal_polynomials([1,1,1])
            sage: R.macaulay_resultant(flist)                                           # needs sage.modules
            -u2*u4*u6 + u1*u5*u6 + u2*u3*u7 - u0*u5*u7 - u1*u3*u8 + u0*u4*u8

        The following example is by Patrick Ingram (:arxiv:`1310.4114`)::

            sage: U = PolynomialRing(ZZ,'y',2); y0,y1 = U.gens()
            sage: R = PolynomialRing(U,'x',3); x0,x1,x2 = R.gens()
            sage: f0 = y0*x2^2 - x0^2 + 2*x1*x2
            sage: f1 = y1*x2^2 - x1^2 + 2*x0*x2
            sage: f2 = x0*x1 - x2^2
            sage: flist = [f0,f1,f2]
            sage: R.macaulay_resultant([f0,f1,f2])                                      # needs sage.modules
            y0^2*y1^2 - 4*y0^3 - 4*y1^3 + 18*y0*y1 - 27

        A simple example with constant rational coefficients::

            sage: R.<x,y,z,w> = PolynomialRing(QQ, 4)
            sage: R.macaulay_resultant([w, z, y, x])                                    # needs sage.modules
            1

        An example where the resultant vanishes::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([x + y, y^2, x])                                 # needs sage.modules
            0

        An example of bad reduction at a prime `p = 5`::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x^3 + 25*y^2*x, 5*z])                        # needs sage.libs.pari sage.modules
            125

        The input can given as an unpacked list of polynomials::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant(y, x^3 + 25*y^2*x, 5*z)                          # needs sage.libs.pari sage.modules
            125

        An example when the coefficients live in a finite field::

            sage: F = FiniteField(11)
            sage: R.<x,y,z,w> = PolynomialRing(F, 4)
            sage: R.macaulay_resultant([z, x^3, 5*y, w])                                # needs sage.modules sage.rings.finite_rings
            4

        Example when the denominator in the algorithm vanishes(in this case
        the resultant is the constant term of the quotient of
        char polynomials of numerator/denominator)::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: R.macaulay_resultant([y, x + z, z^2])                                 # needs sage.libs.pari sage.modules
            -1

        When there are only 2 polynomials, the Macaulay resultant degenerates
        to the traditional resultant::

            sage: R.<x> = PolynomialRing(QQ, 1)
            sage: f =  x^2 + 1; g = x^5 + 1
            sage: fh = f.homogenize()
            sage: gh = g.homogenize()
            sage: RH = fh.parent()
            sage: f.resultant(g) == RH.macaulay_resultant([fh, gh])                     # needs sage.modules
            True"""
    @overload
    def monomial(self, *exponents) -> Any:
        """MPolynomialRing_base.monomial(self, *exponents)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1390)

        Return the monomial with given exponents.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3)
            sage: R.monomial(1,1,1)
            x*y*z
            sage: e=(1,2,3)
            sage: R.monomial(*e)
            x*y^2*z^3
            sage: m = R.monomial(1,2,3)
            sage: R.monomial(*m.degrees()) == m
            True

        We also allow to specify the exponents in a single tuple::

            sage: R.monomial(e)
            x*y^2*z^3

        TESTS:

        Check that :class:`.ETuple`s and :class:`.IntegerVector` also work
        (:class:`.IntegerVector` is used for :meth:`basis`)::

            sage: from sage.combinat.integer_vector import IntegerVector, IntegerVectors
            sage: from sage.rings.polynomial.polydict import ETuple
            sage: R.monomial(ETuple(e))
            x*y^2*z^3
            sage: R.monomial(IntegerVector(IntegerVectors(), e))
            x*y^2*z^3

        Corner case::

            sage: R = PolynomialRing(QQ, [])
            sage: R
            Multivariate Polynomial Ring in no variables over Rational Field
            sage: R.monomial(())
            1
            sage: R.monomial()
            1
            sage: R.monomial(ETuple([]))
            1
            sage: R.monomial(IntegerVector(IntegerVectors(), []))
            1"""
    @overload
    def monomial(self, *e) -> Any:
        """MPolynomialRing_base.monomial(self, *exponents)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1390)

        Return the monomial with given exponents.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3)
            sage: R.monomial(1,1,1)
            x*y*z
            sage: e=(1,2,3)
            sage: R.monomial(*e)
            x*y^2*z^3
            sage: m = R.monomial(1,2,3)
            sage: R.monomial(*m.degrees()) == m
            True

        We also allow to specify the exponents in a single tuple::

            sage: R.monomial(e)
            x*y^2*z^3

        TESTS:

        Check that :class:`.ETuple`s and :class:`.IntegerVector` also work
        (:class:`.IntegerVector` is used for :meth:`basis`)::

            sage: from sage.combinat.integer_vector import IntegerVector, IntegerVectors
            sage: from sage.rings.polynomial.polydict import ETuple
            sage: R.monomial(ETuple(e))
            x*y^2*z^3
            sage: R.monomial(IntegerVector(IntegerVectors(), e))
            x*y^2*z^3

        Corner case::

            sage: R = PolynomialRing(QQ, [])
            sage: R
            Multivariate Polynomial Ring in no variables over Rational Field
            sage: R.monomial(())
            1
            sage: R.monomial()
            1
            sage: R.monomial(ETuple([]))
            1
            sage: R.monomial(IntegerVector(IntegerVectors(), []))
            1"""
    @overload
    def monomial(self, e) -> Any:
        """MPolynomialRing_base.monomial(self, *exponents)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1390)

        Return the monomial with given exponents.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3)
            sage: R.monomial(1,1,1)
            x*y*z
            sage: e=(1,2,3)
            sage: R.monomial(*e)
            x*y^2*z^3
            sage: m = R.monomial(1,2,3)
            sage: R.monomial(*m.degrees()) == m
            True

        We also allow to specify the exponents in a single tuple::

            sage: R.monomial(e)
            x*y^2*z^3

        TESTS:

        Check that :class:`.ETuple`s and :class:`.IntegerVector` also work
        (:class:`.IntegerVector` is used for :meth:`basis`)::

            sage: from sage.combinat.integer_vector import IntegerVector, IntegerVectors
            sage: from sage.rings.polynomial.polydict import ETuple
            sage: R.monomial(ETuple(e))
            x*y^2*z^3
            sage: R.monomial(IntegerVector(IntegerVectors(), e))
            x*y^2*z^3

        Corner case::

            sage: R = PolynomialRing(QQ, [])
            sage: R
            Multivariate Polynomial Ring in no variables over Rational Field
            sage: R.monomial(())
            1
            sage: R.monomial()
            1
            sage: R.monomial(ETuple([]))
            1
            sage: R.monomial(IntegerVector(IntegerVectors(), []))
            1"""
    @overload
    def monomial(self) -> Any:
        """MPolynomialRing_base.monomial(self, *exponents)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1390)

        Return the monomial with given exponents.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3)
            sage: R.monomial(1,1,1)
            x*y*z
            sage: e=(1,2,3)
            sage: R.monomial(*e)
            x*y^2*z^3
            sage: m = R.monomial(1,2,3)
            sage: R.monomial(*m.degrees()) == m
            True

        We also allow to specify the exponents in a single tuple::

            sage: R.monomial(e)
            x*y^2*z^3

        TESTS:

        Check that :class:`.ETuple`s and :class:`.IntegerVector` also work
        (:class:`.IntegerVector` is used for :meth:`basis`)::

            sage: from sage.combinat.integer_vector import IntegerVector, IntegerVectors
            sage: from sage.rings.polynomial.polydict import ETuple
            sage: R.monomial(ETuple(e))
            x*y^2*z^3
            sage: R.monomial(IntegerVector(IntegerVectors(), e))
            x*y^2*z^3

        Corner case::

            sage: R = PolynomialRing(QQ, [])
            sage: R
            Multivariate Polynomial Ring in no variables over Rational Field
            sage: R.monomial(())
            1
            sage: R.monomial()
            1
            sage: R.monomial(ETuple([]))
            1
            sage: R.monomial(IntegerVector(IntegerVectors(), []))
            1"""
    def monomials_of_degree(self, degree) -> Any:
        """MPolynomialRing_base.monomials_of_degree(self, degree)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1442)

        Return a list of all monomials of the given total degree in this
        multivariate polynomial ring.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: R.<x,y,z> = ZZ[]
            sage: mons = R.monomials_of_degree(2)
            sage: mons
            [z^2, y*z, x*z, y^2, x*y, x^2]
            sage: P = PolynomialRing(QQ, 3, 'x, y, z', order=TermOrder('wdeglex', [1, 2, 1]))
            sage: P.monomials_of_degree(2)
            [z^2, y, x*z, x^2]
            sage: P = PolynomialRing(QQ, 3, 'x, y, z', order='lex')
            sage: P.monomials_of_degree(3)
            [z^3, y*z^2, y^2*z, y^3, x*z^2, x*y*z, x*y^2, x^2*z, x^2*y, x^3]
            sage: P = PolynomialRing(QQ, 3, 'x, y, z', order='invlex')
            sage: P.monomials_of_degree(3)
            [x^3, x^2*y, x*y^2, y^3, x^2*z, x*y*z, y^2*z, x*z^2, y*z^2, z^3]

        The number of such monomials equals `\\binom{n+k-1}{k}`
        where `n` is the number of variables and `k` the degree::

            sage: len(mons) == binomial(3 + 2 - 1, 2)                                   # needs sage.combinat
            True"""
    def ngens(self) -> Any:
        """MPolynomialRing_base.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 962)"""
    @overload
    def random_element(self) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=..., choose_degree=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=...) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def random_element(self, degree=..., terms=..., choose_degree=..., *args, **kwargs) -> Any:
        """MPolynomialRing_base.random_element(self, degree=2, terms=None, choose_degree=False, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1145)

        Return a random polynomial of at most degree `d` and at most `t`
        terms.

        First monomials are chosen uniformly random from the set of all
        possible monomials of degree up to `d` (inclusive). This means
        that it is more likely that a monomial of degree `d` appears than
        a monomial of degree `d-1` because the former class is bigger.

        Exactly `t` *distinct* monomials are chosen this way and each one gets
        a random coefficient (possibly zero) from the base ring assigned.

        The returned polynomial is the sum of this list of terms.

        INPUT:

        - ``degree`` -- maximal degree (likely to be reached) (default: 2)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degrees of monomials randomly first
          rather than monomials uniformly random

        - ``**kwargs`` -- passed to the random element generator of the base
          ring

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ)
            sage: f = P.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

            sage: f = P.random_element(2, 5, choose_degree=True)
            sage: f.degree() <= 2
            True
            sage: f.parent() is P
            True
            sage: len(list(f)) <= 5
            True

        Stacked rings::

            sage: R = QQ['x,y']
            sage: S = R['t,u']
            sage: f = S._random_nonzero_element(degree=2, terms=1)
            sage: len(list(f))
            1
            sage: f.degree() <= 2
            True
            sage: f.parent() is S
            True

        Default values apply if no degree and/or number of terms is
        provided::

            sage: # needs sage.modules
            sage: M = random_matrix(QQ['x,y,z'], 2, 2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 5 for a in M.list())
            True
            sage: M = random_matrix(QQ['x,y,z'], 2, 2, terms=1, degree=2)
            sage: all(a.degree() <= 2 for a in M.list())
            True
            sage: all(len(list(a)) <= 1 for a in M.list())
            True

            sage: P.random_element(0, 1) in QQ
            True

            sage: P.random_element(2, 0)
            0

            sage: R.<x> = PolynomialRing(Integers(3), 1)
            sage: f = R.random_element()
            sage: f.degree() <= 2
            True
            sage: len(list(f)) <= 3
            True

        To produce a dense polynomial, pick ``terms=Infinity``::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=Infinity)
            sage: while len(list(f)) != 10:
            ....:     f = P.random_element(degree=2, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)
            sage: f = P.random_element(degree=3, terms=Infinity, choose_degree=True)
            sage: while len(list(f)) != 20:
            ....:     f = P.random_element(degree=3, terms=Infinity)

        The number of terms is silently reduced to the maximum
        available if more terms are requested::

            sage: P.<x,y,z> = GF(127)[]
            sage: f = P.random_element(degree=2, terms=1000)
            sage: len(list(f)) <= 10
            True

        TESTS:

        Random ring elements should live in the ring. We check the degree-
        zero case for :issue:`28855`, but the same should hold generally::

            sage: R = PolynomialRing(QQ, 'X,Y')
            sage: R.random_element(degree=0).parent() == R
            True
            sage: R.random_element().parent() == R
            True"""
    @overload
    def remove_var(self, *var, order=...) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, z) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, z, x) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, y, z, x) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, y, z, x, w) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, y) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, y) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, x, y, z) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    @overload
    def remove_var(self, x, y, z, order=...) -> Any:
        """MPolynomialRing_base.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 294)

        Remove a variable or sequence of variables from ``self``.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: P.<x,y,z,w> = PolynomialRing(ZZ)
            sage: P.remove_var(z)
            Multivariate Polynomial Ring in x, y, w over Integer Ring
            sage: P.remove_var(z, x)
            Multivariate Polynomial Ring in y, w over Integer Ring
            sage: P.remove_var(y, z, x)
            Univariate Polynomial Ring in w over Integer Ring

        Removing all variables results in the base ring::

            sage: P.remove_var(y, z, x, w)
            Integer Ring

        If possible, the term order is kept::

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='deglex')
            sage: R.remove_var(y).term_order()
            Degree lexicographic term order

            sage: R.<x,y,z,w> = PolynomialRing(ZZ, order='lex')
            sage: R.remove_var(y).term_order()
            Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = PolynomialRing(ZZ, order='deglex(2),lex(3)')
            sage: R.remove_var(x, y, z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most
            likely because it was a block order). Please specify the term
            order for the subring
            sage: R.remove_var(x,y,z, order='degrevlex')
            Multivariate Polynomial Ring in u, v over Integer Ring"""
    def repr_long(self, *args, **kwargs):
        """MPolynomialRing_base.repr_long(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 703)

        Return structured string representation of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ, order=TermOrder('degrevlex',1)
            ....:                                      + TermOrder('lex',2))
            sage: print(P.repr_long())
            Polynomial Ring
             Base Ring : Rational Field
                  Size : 3 Variables
              Block  0 : Ordering : degrevlex
                         Names    : x
              Block  1 : Ordering : lex
                         Names    : y, z"""
    @overload
    def some_elements(self) -> Any:
        """MPolynomialRing_base.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1340)

        Return a list of polynomials.

        This is typically used for running generic tests.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: R.some_elements()
            [x, y, x + y, x^2 + x*y, 0, 1]"""
    @overload
    def some_elements(self) -> Any:
        """MPolynomialRing_base.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1340)

        Return a list of polynomials.

        This is typically used for running generic tests.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: R.some_elements()
            [x, y, x + y, x^2 + x*y, 0, 1]"""
    def term_order(self) -> Any:
        """MPolynomialRing_base.term_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 884)"""
    @overload
    def univariate_ring(self, x) -> Any:
        """MPolynomialRing_base.univariate_ring(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 353)

        Return a univariate polynomial ring whose base ring comprises all
        but one variables of ``self``.

        INPUT:

        - ``x`` -- a variable of ``self``

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: P.univariate_ring(y)
            Univariate Polynomial Ring in y
             over Multivariate Polynomial Ring in x, z over Rational Field"""
    @overload
    def univariate_ring(self, y) -> Any:
        """MPolynomialRing_base.univariate_ring(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 353)

        Return a univariate polynomial ring whose base ring comprises all
        but one variables of ``self``.

        INPUT:

        - ``x`` -- a variable of ``self``

        EXAMPLES::

            sage: P.<x,y,z> = QQ[]
            sage: P.univariate_ring(y)
            Univariate Polynomial Ring in y
             over Multivariate Polynomial Ring in x, z over Rational Field"""
    @overload
    def variable_names_recursive(self, depth=...) -> Any:
        """MPolynomialRing_base.variable_names_recursive(self, depth=sage.rings.infinity.infinity)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 907)

        Return the list of variable names of this and its base rings, as if
        it were a single multi-variate polynomial.

        EXAMPLES::

            sage: R = QQ['x,y']['z,w']
            sage: R.variable_names_recursive()
            ('x', 'y', 'z', 'w')
            sage: R.variable_names_recursive(3)
            ('y', 'z', 'w')"""
    @overload
    def variable_names_recursive(self) -> Any:
        """MPolynomialRing_base.variable_names_recursive(self, depth=sage.rings.infinity.infinity)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 907)

        Return the list of variable names of this and its base rings, as if
        it were a single multi-variate polynomial.

        EXAMPLES::

            sage: R = QQ['x,y']['z,w']
            sage: R.variable_names_recursive()
            ('x', 'y', 'z', 'w')
            sage: R.variable_names_recursive(3)
            ('y', 'z', 'w')"""
    @overload
    def weyl_algebra(self) -> Any:
        """MPolynomialRing_base.weyl_algebra(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1805)

        Return the Weyl algebra generated from ``self``.

        EXAMPLES::

            sage: R = QQ['x,y,z']
            sage: W = R.weyl_algebra(); W                                               # needs sage.modules
            Differential Weyl algebra of polynomials in x, y, z over Rational Field
            sage: W.polynomial_ring() == R                                              # needs sage.modules
            True"""
    @overload
    def weyl_algebra(self) -> Any:
        """MPolynomialRing_base.weyl_algebra(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 1805)

        Return the Weyl algebra generated from ``self``.

        EXAMPLES::

            sage: R = QQ['x,y,z']
            sage: W = R.weyl_algebra(); W                                               # needs sage.modules
            Differential Weyl algebra of polynomials in x, y, z over Rational Field
            sage: W.polynomial_ring() == R                                              # needs sage.modules
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
        """MPolynomialRing_base.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial_ring_base.pyx (starting at line 968)"""
