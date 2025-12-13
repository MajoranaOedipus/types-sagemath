import _cython_3_2_1
import sage.structure.element
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

path_algebra_element_unpickle: _cython_3_2_1.cython_function_or_method

class PathAlgebraElement(sage.structure.element.RingElement):
    """PathAlgebraElement(S, data)

    File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 23)

    Elements of a :class:`~sage.quivers.algebra.PathAlgebra`.

    .. NOTE::

        Upon creation of a path algebra, one can choose among several
        monomial orders, which are all positive or negative degree
        orders. Monomial orders that are not degree orders are not
        supported.

    EXAMPLES:

    After creating a path algebra and getting hold of its generators, one can
    create elements just as usual::

        sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
        sage: A.inject_variables()
        Defining e_0, e_1, e_2, a, b, c, d, e, f
        sage: x = a+2*b+3*c+5*e_0+3*e_2
        sage: x
        5*e_0 + a + 2*b + 3*c + 3*e_2

    The path algebra decomposes as a direct sum according to start- and endpoints::

        sage: x.sort_by_vertices()
        [(5*e_0, 0, 0),
         (a, 0, 1),
         (2*b, 0, 2),
         (3*c, 1, 0),
         (3*e_2, 2, 2)]
        sage: (x^3+x^2).sort_by_vertices()
        [(150*e_0 + 33*a*c, 0, 0),
         (30*a + 3*a*c*a, 0, 1),
         (114*b + 6*a*c*b, 0, 2),
         (90*c + 9*c*a*c, 1, 0),
         (18*c*a, 1, 1),
         (54*c*b, 1, 2),
         (36*e_2, 2, 2)]

    For a consistency test, we create a path algebra that is isomorphic to a
    free associative algebra, and compare arithmetic with two other
    implementations of free algebras (note that the letterplace implementation
    only allows weighted homogeneous elements)::

        sage: F.<x,y,z> = FreeAlgebra(GF(25,'t'))
        sage: pF = x+y*z*x+2*y-z+1
        sage: pF2 = x^4+x*y*x*z+2*z^2*x*y
        sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
        sage: pP = sage_eval('x+y*z*x+2*y-z+1', P.gens_dict())
        sage: pP^5+3*pP^3 == sage_eval(repr(pF^5+3*pF^3), P.gens_dict())
        True
        sage: L.<x,y,z> = FreeAlgebra(GF(25,'t'), implementation='letterplace')
        sage: pL2 = x^4+x*y*x*z+2*z^2*x*y
        sage: pP2 = sage_eval('x^4+x*y*x*z+2*z^2*x*y', P.gens_dict())
        sage: pP2^7 == sage_eval(repr(pF2^7), P.gens_dict())
        True
        sage: pP2^7 == sage_eval(repr(pL2^7), P.gens_dict())
        True

    When the Cython implementation of path algebra elements was
    introduced, it was faster than both the default implementation and
    the letterplace implementation of free algebras. The following
    timings where obtained with a 32-bit operating system; using 64-bit
    on the same machine, the letterplace implementation has not become
    faster, but the timing for path algebra elements has improved by
    about 20%::

        sage: # not tested
        sage: timeit('pF^5+3*pF^3')
        1 loops, best of 3: 338 ms per loop
        sage: timeit('pP^5+3*pP^3')
        100 loops, best of 3: 2.55 ms per loop
        sage: timeit('pF2^7')
        10000 loops, best of 3: 513 ms per loop
        sage: timeit('pL2^7')
        125 loops, best of 3: 1.99 ms per loop
        sage: timeit('pP2^7')
        10000 loops, best of 3: 1.54 ms per loop

    So, if one is merely interested in basic arithmetic operations for
    free associative algebras, it could make sense to model the free
    associative algebra as a path algebra. However, standard basis
    computations are not available for path algebras, yet. Hence, to
    implement computations in graded quotients of free algebras, the
    letterplace implementation currently is the only option."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, S, data) -> Any:
        """File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 135)

                Do not call directly.

                INPUT:

                - ``S`` -- path algebra

                - ``data`` -- dictionary; most of its keys are
                  :class:`~sage.quivers.paths.QuiverPath`, the value giving its
                  coefficient

                .. NOTE::

                    Monomial orders that are not degree orders are not supported.

                EXAMPLES::

                    sage: P1 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
                    sage: P1.inject_variables()     # indirect doctest
                    Defining e_1, x, y, z
                    sage: (x+2*z+1)^2
                    e_1 + 4*z + 2*x + 4*z*z + 2*x*z + 2*z*x + x*x
                    sage: P2 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
                    sage: P2.inject_variables()
                    Defining e_1, x, y, z
                    sage: (x+2*z+1)^2
                    4*z*z + 2*x*z + 2*z*x + x*x + 4*z + 2*x + e_1
                    sage: P3 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='negdeglex')
                    sage: P3.inject_variables()
                    Defining e_1, x, y, z
                    sage: (x+2*z+1)^2
                    e_1 + 4*z + 2*x + 4*z*z + 2*z*x + 2*x*z + x*x
                    sage: P4 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='deglex')
                    sage: P4.inject_variables()
                    Defining e_1, x, y, z
                    sage: (x+2*z+1)^2
                    4*z*z + 2*z*x + 2*x*z + x*x + 4*z + 2*x + e_1
        """
    def coefficient(self, QuiverPathP) -> Any:
        """PathAlgebraElement.coefficient(self, QuiverPath P)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 688)

        Return the coefficient of a monomial.

        INPUT:

        - ``P`` -- an element of the underlying partial semigroup

        OUTPUT:

        The coefficient of the given semigroup element in ``self``, or zero if
        it does not appear.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.coefficient(sage_eval('x*x*z', P.semigroup().gens_dict()))
            2
            sage: p.coefficient(sage_eval('z*x*x*x', P.semigroup().gens_dict()))
            0"""
    @overload
    def coefficients(self) -> list:
        """PathAlgebraElement.coefficients(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 454)

        Return the list of coefficients.

        .. NOTE::

            The order in which the coefficients are returned corresponds to the
            order in which the terms are printed. That is *not* the same as the
            order given by the monomial order, since the terms are first ordered
            according to initial and terminal vertices, before applying the
            monomial order of the path algebra.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.coefficients()
            [3, 4, 4, 2, 4, 2, 2, 1, 2, 1, 1, 3, 1, 3, 1]"""
    @overload
    def coefficients(self) -> Any:
        """PathAlgebraElement.coefficients(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 454)

        Return the list of coefficients.

        .. NOTE::

            The order in which the coefficients are returned corresponds to the
            order in which the terms are printed. That is *not* the same as the
            order given by the monomial order, since the terms are first ordered
            according to initial and terminal vertices, before applying the
            monomial order of the path algebra.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.coefficients()
            [3, 4, 4, 2, 4, 2, 2, 1, 2, 1, 1, 3, 1, 3, 1]"""
    @overload
    def degree(self) -> Py_ssize_t:
        """PathAlgebraElement.degree(self) -> Py_ssize_t

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 333)

        Return the degree, provided the element is homogeneous.

        An error is raised if the element is not homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.degree()
            3
            sage: p = (x+2*z+1)^3
            sage: p.degree()
            Traceback (most recent call last):
            ...
            ValueError: element is not homogeneous"""
    @overload
    def degree(self) -> Any:
        """PathAlgebraElement.degree(self) -> Py_ssize_t

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 333)

        Return the degree, provided the element is homogeneous.

        An error is raised if the element is not homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.degree()
            3
            sage: p = (x+2*z+1)^3
            sage: p.degree()
            Traceback (most recent call last):
            ...
            ValueError: element is not homogeneous"""
    @overload
    def degree(self) -> Any:
        """PathAlgebraElement.degree(self) -> Py_ssize_t

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 333)

        Return the degree, provided the element is homogeneous.

        An error is raised if the element is not homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.degree()
            3
            sage: p = (x+2*z+1)^3
            sage: p.degree()
            Traceback (most recent call last):
            ...
            ValueError: element is not homogeneous"""
    @overload
    def is_homogeneous(self) -> bool:
        """PathAlgebraElement.is_homogeneous(self) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 372)

        Tell whether this element is homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.is_homogeneous()
            True
            sage: p = (x+2*z+1)^3
            sage: p.is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """PathAlgebraElement.is_homogeneous(self) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 372)

        Tell whether this element is homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.is_homogeneous()
            True
            sage: p = (x+2*z+1)^3
            sage: p.is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """PathAlgebraElement.is_homogeneous(self) -> bool

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 372)

        Tell whether this element is homogeneous.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: q = (x+y+2*z)^3
            sage: q.is_homogeneous()
            True
            sage: p = (x+2*z+1)^3
            sage: p.is_homogeneous()
            False"""
    @overload
    def monomial_coefficients(self) -> dict:
        """PathAlgebraElement.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 405)

        Return the dictionary keyed by the monomials appearing
        in this element, the values being the coefficients.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: sorted(p.monomial_coefficients().items())
            [(x*x*x, 1),
             (z*x*x, 2),
             (x*z*x, 2),
             (z*z*x, 4),
             (x*x*z, 2),
             (z*x*z, 4),
             (x*z*z, 4),
             (z*z*z, 3),
             (x*x, 3),
             (z*x, 1),
             (x*z, 1),
             (z*z, 2),
             (x, 3),
             (z, 1),
             (e_1, 1)]

        Note that the dictionary can be fed to the algebra, to reconstruct the
        element::

            sage: P(p.monomial_coefficients()) == p
            True"""
    @overload
    def monomial_coefficients(self) -> Any:
        """PathAlgebraElement.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 405)

        Return the dictionary keyed by the monomials appearing
        in this element, the values being the coefficients.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: sorted(p.monomial_coefficients().items())
            [(x*x*x, 1),
             (z*x*x, 2),
             (x*z*x, 2),
             (z*z*x, 4),
             (x*x*z, 2),
             (z*x*z, 4),
             (x*z*z, 4),
             (z*z*z, 3),
             (x*x, 3),
             (z*x, 1),
             (x*z, 1),
             (z*z, 2),
             (x, 3),
             (z, 1),
             (e_1, 1)]

        Note that the dictionary can be fed to the algebra, to reconstruct the
        element::

            sage: P(p.monomial_coefficients()) == p
            True"""
    @overload
    def monomial_coefficients(self) -> Any:
        """PathAlgebraElement.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 405)

        Return the dictionary keyed by the monomials appearing
        in this element, the values being the coefficients.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: sorted(p.monomial_coefficients().items())
            [(x*x*x, 1),
             (z*x*x, 2),
             (x*z*x, 2),
             (z*z*x, 4),
             (x*x*z, 2),
             (z*x*z, 4),
             (x*z*z, 4),
             (z*z*z, 3),
             (x*x, 3),
             (z*x, 1),
             (x*z, 1),
             (z*z, 2),
             (x, 3),
             (z, 1),
             (e_1, 1)]

        Note that the dictionary can be fed to the algebra, to reconstruct the
        element::

            sage: P(p.monomial_coefficients()) == p
            True"""
    def monomials(self) -> list:
        """PathAlgebraElement.monomials(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 488)

        Return the list of monomials appearing in this element.

        .. NOTE::

            The order in which the monomials are returned corresponds to the
            order in which the element's terms are printed. That is *not* the
            same as the order given by the monomial order, since the terms are
            first ordered according to initial and terminal vertices, before
            applying the monomial order of the path algebra.

            The monomials are not elements of the underlying partial
            semigroup, but of the algebra.

        .. SEEALSO:: :meth:`support`

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.monomials()
            [z*z*z,
             x*z*z,
             z*x*z,
             x*x*z,
             z*z*x,
             x*z*x,
             z*x*x,
             x*x*x,
             z*z,
             x*z,
             z*x,
             x*x,
             z,
             x,
             e_1]
            sage: p.monomials()[1].parent() is P
            True"""
    @overload
    def sort_by_vertices(self) -> Any:
        """PathAlgebraElement.sort_by_vertices(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 881)

        Return a list of triples ``(element, v1, v2)``, where ``element`` is
        an element whose monomials all have initial vertex ``v1`` and terminal
        vertex ``v2``, so that the sum of elements is ``self``.

        EXAMPLES::

            sage: A1 = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: A1.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = (b*e*b*e+4*b+e_0)^2
            sage: y = (a*c*b+1)^3
            sage: x.sort_by_vertices()
            [(e_0 + 2*b*e*b*e + b*e*b*e*b*e*b*e, 0, 0), (4*b + 4*b*e*b*e*b, 0, 2)]
            sage: sum(c[0] for c in x.sort_by_vertices()) == x
            True
            sage: y.sort_by_vertices()
            [(e_0, 0, 0), (3*a*c*b, 0, 2), (e_1, 1, 1), (e_2, 2, 2)]
            sage: sum(c[0] for c in y.sort_by_vertices()) == y
            True"""
    @overload
    def sort_by_vertices(self) -> Any:
        """PathAlgebraElement.sort_by_vertices(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 881)

        Return a list of triples ``(element, v1, v2)``, where ``element`` is
        an element whose monomials all have initial vertex ``v1`` and terminal
        vertex ``v2``, so that the sum of elements is ``self``.

        EXAMPLES::

            sage: A1 = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: A1.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = (b*e*b*e+4*b+e_0)^2
            sage: y = (a*c*b+1)^3
            sage: x.sort_by_vertices()
            [(e_0 + 2*b*e*b*e + b*e*b*e*b*e*b*e, 0, 0), (4*b + 4*b*e*b*e*b, 0, 2)]
            sage: sum(c[0] for c in x.sort_by_vertices()) == x
            True
            sage: y.sort_by_vertices()
            [(e_0, 0, 0), (3*a*c*b, 0, 2), (e_1, 1, 1), (e_2, 2, 2)]
            sage: sum(c[0] for c in y.sort_by_vertices()) == y
            True"""
    @overload
    def sort_by_vertices(self) -> Any:
        """PathAlgebraElement.sort_by_vertices(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 881)

        Return a list of triples ``(element, v1, v2)``, where ``element`` is
        an element whose monomials all have initial vertex ``v1`` and terminal
        vertex ``v2``, so that the sum of elements is ``self``.

        EXAMPLES::

            sage: A1 = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: A1.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = (b*e*b*e+4*b+e_0)^2
            sage: y = (a*c*b+1)^3
            sage: x.sort_by_vertices()
            [(e_0 + 2*b*e*b*e + b*e*b*e*b*e*b*e, 0, 0), (4*b + 4*b*e*b*e*b, 0, 2)]
            sage: sum(c[0] for c in x.sort_by_vertices()) == x
            True
            sage: y.sort_by_vertices()
            [(e_0, 0, 0), (3*a*c*b, 0, 2), (e_1, 1, 1), (e_2, 2, 2)]
            sage: sum(c[0] for c in y.sort_by_vertices()) == y
            True"""
    @overload
    def sort_by_vertices(self) -> Any:
        """PathAlgebraElement.sort_by_vertices(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 881)

        Return a list of triples ``(element, v1, v2)``, where ``element`` is
        an element whose monomials all have initial vertex ``v1`` and terminal
        vertex ``v2``, so that the sum of elements is ``self``.

        EXAMPLES::

            sage: A1 = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: A1.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = (b*e*b*e+4*b+e_0)^2
            sage: y = (a*c*b+1)^3
            sage: x.sort_by_vertices()
            [(e_0 + 2*b*e*b*e + b*e*b*e*b*e*b*e, 0, 0), (4*b + 4*b*e*b*e*b, 0, 2)]
            sage: sum(c[0] for c in x.sort_by_vertices()) == x
            True
            sage: y.sort_by_vertices()
            [(e_0, 0, 0), (3*a*c*b, 0, 2), (e_1, 1, 1), (e_2, 2, 2)]
            sage: sum(c[0] for c in y.sort_by_vertices()) == y
            True"""
    @overload
    def sort_by_vertices(self) -> Any:
        """PathAlgebraElement.sort_by_vertices(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 881)

        Return a list of triples ``(element, v1, v2)``, where ``element`` is
        an element whose monomials all have initial vertex ``v1`` and terminal
        vertex ``v2``, so that the sum of elements is ``self``.

        EXAMPLES::

            sage: A1 = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: A1.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = (b*e*b*e+4*b+e_0)^2
            sage: y = (a*c*b+1)^3
            sage: x.sort_by_vertices()
            [(e_0 + 2*b*e*b*e + b*e*b*e*b*e*b*e, 0, 0), (4*b + 4*b*e*b*e*b, 0, 2)]
            sage: sum(c[0] for c in x.sort_by_vertices()) == x
            True
            sage: y.sort_by_vertices()
            [(e_0, 0, 0), (3*a*c*b, 0, 2), (e_1, 1, 1), (e_2, 2, 2)]
            sage: sum(c[0] for c in y.sort_by_vertices()) == y
            True"""
    def support(self) -> list:
        """PathAlgebraElement.support(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 603)

        Return the list of monomials, as elements of the underlying partial semigroup.

        .. NOTE::

            The order in which the monomials are returned corresponds to the
            order in which the element's terms are printed. That is *not* the
            same as the order given by the monomial order, since the terms are
            first ordered according to initial and terminal vertices, before
            applying the monomial order of the path algebra.

        .. SEEALSO:: :meth:`monomials`

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.support()
            [z*z*z,
             x*z*z,
             z*x*z,
             x*x*z,
             z*z*x,
             x*z*x,
             z*x*x,
             x*x*x,
             z*z,
             x*z,
             z*x,
             x*x,
             z,
             x,
             e_1]
            sage: p.support()[1].parent() is P.semigroup()
            True"""
    @overload
    def support_of_term(self) -> Any:
        """PathAlgebraElement.support_of_term(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 659)

        If ``self`` consists of a single term, return the corresponding
        element of the underlying path semigroup.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = 4*a*d*c*b*e
            sage: x.support_of_term()
            a*d*c*b*e
            sage: x.support_of_term().parent() is A.semigroup()
            True
            sage: (x + f).support_of_term()
            Traceback (most recent call last):
            ...
            ValueError: 4*a*d*c*b*e + f is not a single term"""
    @overload
    def support_of_term(self) -> Any:
        """PathAlgebraElement.support_of_term(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 659)

        If ``self`` consists of a single term, return the corresponding
        element of the underlying path semigroup.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = 4*a*d*c*b*e
            sage: x.support_of_term()
            a*d*c*b*e
            sage: x.support_of_term().parent() is A.semigroup()
            True
            sage: (x + f).support_of_term()
            Traceback (most recent call last):
            ...
            ValueError: 4*a*d*c*b*e + f is not a single term"""
    @overload
    def support_of_term(self) -> Any:
        """PathAlgebraElement.support_of_term(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 659)

        If ``self`` consists of a single term, return the corresponding
        element of the underlying path semigroup.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = 4*a*d*c*b*e
            sage: x.support_of_term()
            a*d*c*b*e
            sage: x.support_of_term().parent() is A.semigroup()
            True
            sage: (x + f).support_of_term()
            Traceback (most recent call last):
            ...
            ValueError: 4*a*d*c*b*e + f is not a single term"""
    @overload
    def support_of_term(self) -> Any:
        """PathAlgebraElement.support_of_term(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 659)

        If ``self`` consists of a single term, return the corresponding
        element of the underlying path semigroup.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: x = 4*a*d*c*b*e
            sage: x.support_of_term()
            a*d*c*b*e
            sage: x.support_of_term().parent() is A.semigroup()
            True
            sage: (x + f).support_of_term()
            Traceback (most recent call last):
            ...
            ValueError: 4*a*d*c*b*e + f is not a single term"""
    @overload
    def terms(self) -> list:
        """PathAlgebraElement.terms(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 550)

        Return the list of terms.

        .. NOTE::

            The order in which the terms are returned corresponds to the order
            in which they are printed. That is *not* the same as the
            order given by the monomial order, since the terms are first
            ordered according to initial and terminal vertices, before
            applying the monomial order of the path algebra.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.terms()
            [3*z*z*z,
             4*x*z*z,
             4*z*x*z,
             2*x*x*z,
             4*z*z*x,
             2*x*z*x,
             2*z*x*x,
             x*x*x,
             2*z*z,
             x*z,
             z*x,
             3*x*x,
             z,
             3*x,
             e_1]"""
    @overload
    def terms(self) -> Any:
        """PathAlgebraElement.terms(self) -> list

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 550)

        Return the list of terms.

        .. NOTE::

            The order in which the terms are returned corresponds to the order
            in which they are printed. That is *not* the same as the
            order given by the monomial order, since the terms are first
            ordered according to initial and terminal vertices, before
            applying the monomial order of the path algebra.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: p.terms()
            [3*z*z*z,
             4*x*z*z,
             4*z*x*z,
             2*x*x*z,
             4*z*z*x,
             2*x*z*x,
             2*z*x*x,
             x*x*x,
             2*z*z,
             x*z,
             z*x,
             3*x*x,
             z,
             3*x,
             e_1]"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """PathAlgebraElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 789)

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: copy(p) is p
            False
            sage: copy(p) == p   # indirect doctest
            True"""
    def __getitem__(self, k) -> Any:
        """PathAlgebraElement.__getitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 804)

        Either return the coefficient in ``self`` of an element of the
        underlying partial semigroup, or the sum of terms of ``self`` whose
        monomials have a given initial and terminal vertex.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: X = (a+2*b+3*c+5*e_0+3*e_2)^3
            sage: X[A.semigroup()('c')]
            75
            sage: X.sort_by_vertices()
            [(125*e_0 + 30*a*c, 0, 0),
             (25*a + 3*a*c*a, 0, 1),
             (98*b + 6*a*c*b, 0, 2),
             (75*c + 9*c*a*c, 1, 0),
             (15*c*a, 1, 1),
             (48*c*b, 1, 2),
             (27*e_2, 2, 2)]
            sage: X.sort_by_vertices()
            [(125*e_0 + 30*a*c, 0, 0),
             (25*a + 3*a*c*a, 0, 1),
             (98*b + 6*a*c*b, 0, 2),
             (75*c + 9*c*a*c, 1, 0),
             (15*c*a, 1, 1),
             (48*c*b, 1, 2),
             (27*e_2, 2, 2)]
            sage: X[0,2]
            98*b + 6*a*c*b"""
    def __hash__(self) -> Any:
        """PathAlgebraElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 918)

        The hash is cached, to make it faster.

        EXAMPLES::

            sage: P1 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(3,'t'))
            sage: P2 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(3,'t'), order='deglex')
            sage: P1.inject_variables()
            Defining e_1, x, y, z
            sage: p = x+y
            sage: P2.inject_variables()
            Defining e_1, x, y, z
            sage: q = x+y
            sage: D = dict([(p^i,i) for i in range(1,8)])
            sage: len(D)
            7
            sage: hash(q^5) == hash(p^5)    # indirect doctest
            True
            sage: D[q^6]
            6"""
    def __iter__(self) -> Any:
        """PathAlgebraElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 735)

        Iterate over the pairs (monomial, coefficient) appearing in ``self``.

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P.inject_variables()
            Defining e_1, x, y, z
            sage: p = (x+2*z+1)^3
            sage: p
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: list(p)   # indirect doctest
            [(z*z*z, 3),
             (x*z*z, 4),
             (z*x*z, 4),
             (x*x*z, 2),
             (z*z*x, 4),
             (x*z*x, 2),
             (z*x*x, 2),
             (x*x*x, 1),
             (z*z, 2),
             (x*z, 1),
             (z*x, 1),
             (x*x, 3),
             (z, 1),
             (x, 3),
             (e_1, 1)]"""
    def __len__(self) -> Any:
        """PathAlgebraElement.__len__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 310)

        Return the number of terms appearing in this element.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: X = a+2*b+3*c+5*e_0+3*e_2
            sage: len(X)
            5
            sage: len(X^5)
            17"""
    def __reduce__(self) -> Any:
        """PathAlgebraElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 201)

        EXAMPLES::

            sage: P = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: p = sage_eval('(x+2*z+1)^3', P.gens_dict())
            sage: loads(dumps(p)) == p     # indirect doctest
            True"""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, x) -> Any:
        """PathAlgebraElement.__truediv__(self, x)

        File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pyx (starting at line 1245)

        Division by coefficients.

        EXAMPLES::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ.quo(15))
            sage: X = sage_eval('a+2*b+3*c+5*e_0+3*e_2', A.gens_dict())
            sage: X/2
            10*e_0 + 8*a + b + 9*c + 9*e_2
            sage: (X/2)*2 == X    # indirect doctest
            True

        ::

            sage: A = DiGraph({0:{1:['a'], 2:['b']}, 1:{0:['c'], 1:['d']}, 2:{0:['e'],2:['f']}}).path_semigroup().algebra(ZZ)
            sage: A.inject_variables()
            Defining e_0, e_1, e_2, a, b, c, d, e, f
            sage: X = a+2*b+3*c+5*e_0+3*e_2
            sage: X/4
            5/4*e_0 + 1/4*a + 1/2*b + 3/4*c + 3/4*e_2
            sage: (X/4).parent()
            Path algebra of Looped multi-digraph on 3 vertices over Rational Field
            sage: (X/4)*4 == X
            True"""

class _FreeListProtector:
    """File: /build/sagemath/src/sage/src/sage/quivers/algebra_elements.pxi (starting at line 294)

        The purpose of this class is to deallocate our freelist
        of path algebra terms. When its only instance is deleted (which
        should only happen when a SageMath session ends), then the
        freelist is cleared.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
