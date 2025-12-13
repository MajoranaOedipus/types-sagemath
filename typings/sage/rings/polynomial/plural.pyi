import _cython_3_2_1
import sage as sage
import sage.rings.ring
import sage.structure.element
import sage.structure.factory
from sage.categories.algebras import Algebras as Algebras
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.functional import coerce as coerce
from sage.rings.finite_rings.finite_field_prime_modn import FiniteField_prime_modn as FiniteField_prime_modn
from sage.rings.integer_ring import IntegerRing_class as IntegerRing_class
from sage.rings.polynomial.multi_polynomial_ideal import NCPolynomialIdeal as NCPolynomialIdeal
from sage.rings.polynomial.polydict import ETuple as ETuple
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.ring import CommutativeRing as CommutativeRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

ExteriorAlgebra: _cython_3_2_1.cython_function_or_method
SCA: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
g_Algebra: G_AlgFactory
new_CRing: _cython_3_2_1.cython_function_or_method
new_NRing: _cython_3_2_1.cython_function_or_method
new_Ring: _cython_3_2_1.cython_function_or_method
unpickle_NCPolynomial_plural: _cython_3_2_1.cython_function_or_method

class ExteriorAlgebra_plural(NCPolynomialRing_plural):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class G_AlgFactory(sage.structure.factory.UniqueFactory):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 150)

        A factory for the creation of g-algebras as unique parents.

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: H is A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}) # indirect doctest
            True
    """
    def create_key_and_extra_args(self, base_ring, c, d, names=..., order=..., category=..., check=..., commutative=...) -> Any:
        """G_AlgFactory.create_key_and_extra_args(self, base_ring, c, d, names=None, order=None, category=None, check=None, commutative=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 186)

        Create a unique key for g-algebras.

        INPUT:

        - ``base_ring`` -- a ring
        - ``c``, ``d`` -- two matrices
        - ``names`` -- tuple or list of names
        - ``order`` -- (optional) term order
        - ``category`` -- (optional) category
        - ``check`` -- (optional) boolean
        - ``commutative`` -- (optional) boolean

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: H is A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}) # indirect doctest
            True

            sage: P = A.g_algebra(relations={}, order='lex')
            sage: P.category()
            Category of commutative algebras over Rational Field"""
    def create_object(self, version, key, **extra_args) -> Any:
        """G_AlgFactory.create_object(self, version, key, **extra_args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 161)

        Create a g-algebra to a given unique key.

        INPUT:

        - ``key`` -- a 6-tuple, formed by a base ring, a tuple of names, two
          matrices over a polynomial ring over the base ring with the given
          variable names, a term order, and a category
        - ``extra_args`` -- dictionary, whose only relevant key is 'check'

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: sorted(H.relations().items(), key=str)
            [(y*x, x*y - z), (z*x, x*z + 2*x), (z*y, y*z - 2*y)]"""

class NCPolynomialRing_plural(sage.rings.ring.Ring):
    """NCPolynomialRing_plural(base_ring, names, c, d, order, category, check=True)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 246)

    A non-commutative polynomial ring.

    EXAMPLES::

        sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
        sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
        sage: H._is_category_initialized()
        True
        sage: H.category()
        Category of algebras over Rational Field
        sage: TestSuite(H).run()

    Note that two variables commute if they are not part of the given
    relations::

        sage: H.<x,y,z> = A.g_algebra({z*x:x*z+2*x, z*y:y*z-2*y})
        sage: x*y == y*x
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base_ring, names, c, d, order, category, check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 267)

                Construct a noncommutative polynomial G-algebra subject to the following conditions:

                INPUT:

                - ``base_ring`` -- base ring (must be either `\\GF{q}`, `\\ZZ`, `\\ZZ/n\\ZZ`, `\\QQ` or absolute number field)
                - ``names`` -- tuple of names of ring variables
                - ``c``, ``d`` -- upper triangular matrices of coefficients,
                  resp. commutative polynomials, satisfying the nondegeneracy
                  conditions, which are to be tested if ``check`` is ``True``. These
                  matrices describe the noncommutative relations:

                    ``self.gen(j)*self.gen(i) == c[i, j] * self.gen(i)*self.gen(j) + d[i, j],``

                  where ``0 <= i < j < self.ngens()``. Note that two variables
                  commute if they are not part of one of these relations.
                - ``order`` -- term order
                - ``check`` -- check the noncommutative conditions (default: ``True``)

                TESTS:

                It is strongly recommended to construct a g-algebra using
                :class:`G_AlgFactory`. The following is just for documenting
                the arguments of the ``__init__`` method::

                    sage: from sage.matrix.constructor  import Matrix
                    sage: c0 = Matrix(3)
                    sage: c0[0,1] = -1
                    sage: c0[0,2] = 1
                    sage: c0[1,2] = 1

                    sage: d0 = Matrix(3)
                    sage: d0[0, 1] = 17
                    sage: P = QQ['x','y','z']
                    sage: c = c0.change_ring(P)
                    sage: d = d0.change_ring(P)

                    sage: from sage.rings.polynomial.plural import NCPolynomialRing_plural
                    sage: P.<x,y,z> = NCPolynomialRing_plural(QQ, c = c, d = d, order=TermOrder('lex',3), category=Algebras(QQ))

                    sage: P # indirect doctest
                    Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: -x*y + 17}

                    sage: P(x*y)
                    x*y

                    sage: f = 27/113 * x^2 + y*z + 1/2; f
                    27/113*x^2 + y*z + 1/2

                    sage: P.term_order()
                    Lexicographic term order

                    sage: from sage.rings.polynomial.plural import NCPolynomialRing_plural
                    sage: P = GF(7)['x','y','z']
                    sage: c = c0.change_ring(P)
                    sage: d = d0.change_ring(P)
                    sage: P.<x,y,z> = NCPolynomialRing_plural(GF(7), c = c, d = d, order=TermOrder('degrevlex',3), category=Algebras(GF(7)))

                    sage: P # indirect doctest
                    Noncommutative Multivariate Polynomial Ring in x, y, z over Finite Field of size 7, nc-relations: {y*x: -x*y + 3}

                    sage: P(x*y)
                    x*y

                    sage: f = 3 * x^2 + y*z + 5; f
                    3*x^2 + y*z - 2

                    sage: P.term_order()
                    Degree reverse lexicographic term order
        """
    @overload
    def algebra_generators(self) -> Any:
        """NCPolynomialRing_plural.algebra_generators(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 863)

        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order='lex')
            sage: P.algebra_generators()
            Finite family {'x': x, 'y': y, 'z': z}"""
    @overload
    def algebra_generators(self) -> Any:
        """NCPolynomialRing_plural.algebra_generators(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 863)

        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order='lex')
            sage: P.algebra_generators()
            Finite family {'x': x, 'y': y, 'z': z}"""
    @overload
    def free_algebra(self) -> Any:
        """NCPolynomialRing_plural.free_algebra(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 604)

        Return the free algebra of which this is the quotient.

        EXAMPLES::

           sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
           sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
           sage: B = P.free_algebra()
           sage: A == B
           True"""
    @overload
    def free_algebra(self) -> Any:
        """NCPolynomialRing_plural.free_algebra(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 604)

        Return the free algebra of which this is the quotient.

        EXAMPLES::

           sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
           sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
           sage: B = P.free_algebra()
           sage: A == B
           True"""
    def gen(self, intn=...) -> Any:
        """NCPolynomialRing_plural.gen(self, int n=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 829)

        Return the ``n``-th generator of this noncommutative polynomial
        ring.

        INPUT:

        - ``n`` -- nonnegative integer

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.gen(),P.gen(1)
            (x, y)

        Note that the generators are not cached::

            sage: P.gen(1) is P.gen(1)
            False"""
    def ideal(self, *gens, **kwds) -> Any:
        '''NCPolynomialRing_plural.ideal(self, *gens, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 877)

        Create an ideal in this polynomial ring.

        INPUT:

        - ``*gens`` -- list or tuple of generators (or several input arguments)
        - ``coerce`` -- boolean (default: ``True``); this must be a
          keyword argument. Only set it to ``False`` if you are certain
          that each generator is already in the ring.
        - ``side`` -- string (either "left", which is the default, or "twosided")
          Must be a keyword argument. Defines whether the ideal is a left ideal
          or a two-sided ideal. Right ideals are not implemented.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P.<x,y,z> = A.g_algebra(relations={y*x:-x*y}, order = \'lex\')

            sage: P.ideal([x + 2*y + 2*z-1, 2*x*y + 2*y*z-y, x^2 + 2*y^2 + 2*z^2-x])
            Left Ideal (x + 2*y + 2*z - 1, 2*x*y + 2*y*z - y, x^2 - x + 2*y^2 + 2*z^2) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: -x*y}
            sage: P.ideal([x + 2*y + 2*z-1, 2*x*y + 2*y*z-y, x^2 + 2*y^2 + 2*z^2-x], side=\'twosided\')
            Twosided Ideal (x + 2*y + 2*z - 1, 2*x*y + 2*y*z - y, x^2 - x + 2*y^2 + 2*z^2) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: -x*y}'''
    @overload
    def is_field(self) -> Any:
        """NCPolynomialRing_plural.is_field(self, *args, **kwargs) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 689)

        Return ``False``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.is_field()
            False

        TESTS:

        Make the method accept additional parameters, such as the flag ``proof``.
        See :issue:`22910`::

            sage: P.is_field(proof=False)
            False"""
    @overload
    def is_field(self, proof=...) -> Any:
        """NCPolynomialRing_plural.is_field(self, *args, **kwargs) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 689)

        Return ``False``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.is_field()
            False

        TESTS:

        Make the method accept additional parameters, such as the flag ``proof``.
        See :issue:`22910`::

            sage: P.is_field(proof=False)
            False"""
    @overload
    def is_field(self, *args, **kwargs) -> bool:
        """NCPolynomialRing_plural.is_field(self, *args, **kwargs) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 689)

        Return ``False``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.is_field()
            False

        TESTS:

        Make the method accept additional parameters, such as the flag ``proof``.
        See :issue:`22910`::

            sage: P.is_field(proof=False)
            False"""
    def monomial_all_divisors(self, NCPolynomial_pluralt) -> Any:
        """NCPolynomialRing_plural.monomial_all_divisors(self, NCPolynomial_plural t)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1344)

        Return a list of all monomials that divide ``t``.

        Coefficients are ignored.

        INPUT:

        - ``t`` -- a monomial

        OUTPUT: list of monomials

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_all_divisors(x^2*z^3)
            [x, x^2, z, x*z, x^2*z, z^2, x*z^2, x^2*z^2, z^3, x*z^3, x^2*z^3]

        ALGORITHM: addwithcarry idea by Toon Segers"""
    def monomial_divides(self, NCPolynomial_plurala, NCPolynomial_pluralb) -> Any:
        """NCPolynomialRing_plural.monomial_divides(self, NCPolynomial_plural a, NCPolynomial_plural b)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1079)

        Return ``False`` if ``a`` does not divide ``b`` and ``True``
        otherwise.

        Coefficients are ignored.

        INPUT:

        - ``a`` -- monomial

        - ``b`` -- monomial

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_divides(x*y*z, x^3*y^2*z^4)
            True
            sage: P.monomial_divides(x^3*y^2*z^4, x*y*z)
            False

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: Q = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: Q.inject_variables()
            Defining x, y, z

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_divides(P(1), P(0))
            True
            sage: P.monomial_divides(P(1), x)
            True"""
    def monomial_lcm(self, NCPolynomial_pluralf, NCPolynomial_pluralg) -> Any:
        """NCPolynomialRing_plural.monomial_lcm(self, NCPolynomial_plural f, NCPolynomial_plural g)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1141)

        LCM for monomials. Coefficients are ignored.

        INPUT:

        - ``f`` -- monomial

        - ``g`` -- monomial

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_lcm(3/2*x*y,x)
            x*y

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_lcm(x*y,R.gen()) # not tested
            x*y

            sage: P.monomial_lcm(P(3/2),P(2/3))
            1

            sage: P.monomial_lcm(x,P(1))
            x"""
    def monomial_pairwise_prime(self, NCPolynomial_pluralg, NCPolynomial_pluralh) -> Any:
        """NCPolynomialRing_plural.monomial_pairwise_prime(self, NCPolynomial_plural g, NCPolynomial_plural h)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1268)

        Return ``True`` if ``h`` and ``g`` are pairwise prime.

        Both ``h`` and ``g`` are treated as monomials.

        Coefficients are ignored.

        INPUT:

        - ``h`` -- monomial
        - ``g`` -- monomial

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_pairwise_prime(x^2*z^3, y^4)
            True

            sage: P.monomial_pairwise_prime(1/2*x^3*y^2, 3/4*y^3)
            False

        TESTS::

            sage: A.<x1,y1,z1> = FreeAlgebra(QQ, 3)
            sage: Q = A.g_algebra(relations={y1*x1:-x1*y1},  order='lex')
            sage: Q.inject_variables()
            Defining x1, y1, z1

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_pairwise_prime(x^2*z^3, x1^4) # not tested
            True

            sage: P.monomial_pairwise_prime((2)*x^3*y^2, Q.zero()) # not tested
            True

            sage: P.monomial_pairwise_prime(2*P.one(),x)
            False"""
    def monomial_quotient(self, NCPolynomial_pluralf, NCPolynomial_pluralg, coeff=...) -> Any:
        """NCPolynomialRing_plural.monomial_quotient(self, NCPolynomial_plural f, NCPolynomial_plural g, coeff=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 977)

        Return ``f/g``, where both ``f`` and ``g`` are treated as
        monomials.

        Coefficients are ignored by default.

        INPUT:

        - ``f`` -- monomial
        - ``g`` -- monomial
        - ``coeff`` -- divide coefficients as well (default: ``False``)

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_quotient(3/2*x*y,x,coeff=True)
            3/2*y

        Note that `\\ZZ` behaves differently if ``coeff=True``::

            sage: P.monomial_quotient(2*x,3*x)
            1
            sage: P.monomial_quotient(2*x,3*x,coeff=True)
            2/3

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: P.monomial_quotient(x*y,x)
            y

            sage: P.monomial_quotient(x*y,R.gen()) # not tested
            y

            sage: P.monomial_quotient(P(0),P(1))
            0

            sage: P.monomial_quotient(P(1),P(0))
            Traceback (most recent call last):
            ...
            ZeroDivisionError

            sage: P.monomial_quotient(P(3/2),P(2/3), coeff=True)
            9/4

            sage: P.monomial_quotient(x,P(1))
            x

        TESTS::

            sage: P.monomial_quotient(x,y) # Note the wrong result
            x*y^...

        .. WARNING::

            Assumes that the head term of f is a multiple of the head
            term of g and return the multiplicant m. If this rule is
            violated, funny things may happen."""
    @overload
    def monomial_reduce(self, NCPolynomial_pluralf, G) -> Any:
        """NCPolynomialRing_plural.monomial_reduce(self, NCPolynomial_plural f, G)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1204)

        Try to find a ``g`` in ``G`` where ``g.lm()`` divides
        ``f``. If found ``(flt,g)`` is returned, ``(0,0)`` otherwise,
        where ``flt`` is ``f/g.lm()``.

        It is assumed that ``G`` is iterable and contains *only*
        elements in this polynomial ring.

        Coefficients are ignored.

        INPUT:

        - ``f`` -- monomial
        - ``G`` -- list/set of mpolynomials

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: f = x*y^2
            sage: G = [ 3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, 1/2  ]
            sage: P.monomial_reduce(f,G)
            (y, 1/4*x*y + 2/7)

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: Q = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: Q.inject_variables()
            Defining x, y, z

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z
            sage: f = x*y^2
            sage: G = [ 3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, 1/2  ]

            sage: P.monomial_reduce(P(0),G)
            (0, 0)

            sage: P.monomial_reduce(f,[P(0)])
            (0, 0)"""
    @overload
    def monomial_reduce(self, f, G) -> Any:
        """NCPolynomialRing_plural.monomial_reduce(self, NCPolynomial_plural f, G)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1204)

        Try to find a ``g`` in ``G`` where ``g.lm()`` divides
        ``f``. If found ``(flt,g)`` is returned, ``(0,0)`` otherwise,
        where ``flt`` is ``f/g.lm()``.

        It is assumed that ``G`` is iterable and contains *only*
        elements in this polynomial ring.

        Coefficients are ignored.

        INPUT:

        - ``f`` -- monomial
        - ``G`` -- list/set of mpolynomials

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z

            sage: f = x*y^2
            sage: G = [ 3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, 1/2  ]
            sage: P.monomial_reduce(f,G)
            (y, 1/4*x*y + 2/7)

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: Q = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: Q.inject_variables()
            Defining x, y, z

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y},  order='lex')
            sage: P.inject_variables()
            Defining x, y, z
            sage: f = x*y^2
            sage: G = [ 3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, 1/2  ]

            sage: P.monomial_reduce(P(0),G)
            (0, 0)

            sage: P.monomial_reduce(f,[P(0)])
            (0, 0)"""
    @overload
    def ngens(self) -> Any:
        """NCPolynomialRing_plural.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 816)

        Return the number of variables in this noncommutative polynomial ring.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P.<x,y,z> = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.ngens()
            3"""
    @overload
    def ngens(self) -> Any:
        """NCPolynomialRing_plural.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 816)

        Return the number of variables in this noncommutative polynomial ring.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P.<x,y,z> = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.ngens()
            3"""
    @overload
    def relations(self, add_commutative=...) -> Any:
        """NCPolynomialRing_plural.relations(self, add_commutative=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 759)

        Return the relations of this g-algebra.

        INPUT:

        - ``add_commutative`` -- boolean (default: ``False``)

        OUTPUT:

        The defining relations. There are some implicit relations:
        Two generators commute if they are not part of any given
        relation. The implicit relations are not provided, unless
        ``add_commutative==True``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({z*x:x*z+2*x, z*y:y*z-2*y})
            sage: x*y == y*x
            True
            sage: H.relations()
            {z*x: x*z + 2*x, z*y: y*z - 2*y}
            sage: H.relations(add_commutative=True)
            {y*x: x*y, z*x: x*z + 2*x, z*y: y*z - 2*y}"""
    @overload
    def relations(self) -> Any:
        """NCPolynomialRing_plural.relations(self, add_commutative=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 759)

        Return the relations of this g-algebra.

        INPUT:

        - ``add_commutative`` -- boolean (default: ``False``)

        OUTPUT:

        The defining relations. There are some implicit relations:
        Two generators commute if they are not part of any given
        relation. The implicit relations are not provided, unless
        ``add_commutative==True``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({z*x:x*z+2*x, z*y:y*z-2*y})
            sage: x*y == y*x
            True
            sage: H.relations()
            {z*x: x*z + 2*x, z*y: y*z - 2*y}
            sage: H.relations(add_commutative=True)
            {y*x: x*y, z*x: x*z + 2*x, z*y: y*z - 2*y}"""
    @overload
    def relations(self, add_commutative=...) -> Any:
        """NCPolynomialRing_plural.relations(self, add_commutative=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 759)

        Return the relations of this g-algebra.

        INPUT:

        - ``add_commutative`` -- boolean (default: ``False``)

        OUTPUT:

        The defining relations. There are some implicit relations:
        Two generators commute if they are not part of any given
        relation. The implicit relations are not provided, unless
        ``add_commutative==True``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({z*x:x*z+2*x, z*y:y*z-2*y})
            sage: x*y == y*x
            True
            sage: H.relations()
            {z*x: x*z + 2*x, z*y: y*z - 2*y}
            sage: H.relations(add_commutative=True)
            {y*x: x*y, z*x: x*z + 2*x, z*y: y*z - 2*y}"""
    @overload
    def term_order(self) -> Any:
        """NCPolynomialRing_plural.term_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 672)

        Return the term ordering of the noncommutative ring.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.term_order()
            Lexicographic term order

            sage: P = A.g_algebra(relations={y*x:-x*y})
            sage: P.term_order()
            Degree reverse lexicographic term order"""
    @overload
    def term_order(self) -> Any:
        """NCPolynomialRing_plural.term_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 672)

        Return the term ordering of the noncommutative ring.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.term_order()
            Lexicographic term order

            sage: P = A.g_algebra(relations={y*x:-x*y})
            sage: P.term_order()
            Degree reverse lexicographic term order"""
    @overload
    def term_order(self) -> Any:
        """NCPolynomialRing_plural.term_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 672)

        Return the term ordering of the noncommutative ring.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P.term_order()
            Lexicographic term order

            sage: P = A.g_algebra(relations={y*x:-x*y})
            sage: P.term_order()
            Degree reverse lexicographic term order"""
    def __hash__(self) -> Any:
        """NCPolynomialRing_plural.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 619)

        Return a hash for this noncommutative ring.

        This is a hash of the string
        representation of this polynomial ring.

        NOTE:

        G-algebras are unique parents, provided that the g-algebra constructor
        is used. Thus, the hash simply is the memory address of the g-algebra
        (so, it is a session hash, but no stable hash). It is possible to
        destroy uniqueness of g-algebras on purpose, but that's your own
        problem if you do those things.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: {P:2}[P]            # indirect doctest
            2"""
    def __pow__(self, n, _) -> Any:
        """NCPolynomialRing_plural.__pow__(self, n, _)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 643)

        Return the free module of rank `n` over this ring.

        .. NOTE::

            This is not properly implemented yet. Thus, there is
            a warning.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: P.<x,y,z> = A.g_algebra(relations={y*x:-x*y}, order = 'lex')
            sage: P^3
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            Ambient free module of rank 3 over Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: -x*y}"""
    def __reduce__(self) -> Any:
        """NCPolynomialRing_plural.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 371)

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: H is A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            True
            sage: H is loads(dumps(H))  # indirect doctest
            True
            sage: A2.<x,y,z> = FreeAlgebra(GF(5), 3)
            sage: R2 = A2.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}, order=TermOrder('degrevlex', 2))

        Check that :issue:`17224` is fixed::

            sage: from sage.rings.polynomial.term_order import TermOrder
            sage: F.<x,y> = FreeAlgebra(QQ)
            sage: g = F.g_algebra({y*x:-x*y}, order=TermOrder('wdegrevlex', [1,2]))
            sage: loads(dumps(g)) == g
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class NCPolynomial_plural(sage.structure.element.RingElement):
    """NCPolynomial_plural(NCPolynomialRing_plural parent)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1422)

    A noncommutative multivariate polynomial implemented using libSINGULAR."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, NCPolynomialRing_pluralparent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1426)

                Construct a zero element in parent.

                EXAMPLES::

                    sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
                    sage: H = A.g_algebra(relations={y*x:-x*y},  order='lex')
                    sage: from sage.rings.polynomial.plural import NCPolynomial_plural
                    sage: NCPolynomial_plural(H)
                    0
        """
    @overload
    def coefficient(self, degrees) -> Any:
        """NCPolynomial_plural.coefficient(self, degrees)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2017)

        Return the coefficient of the variables with the degrees
        specified in the python dictionary ``degrees``.

        Mathematically, this is the coefficient in the base ring
        adjoined by the variables of this ring not listed in
        ``degrees``.  However, the result has the same parent as this
        polynomial.

        This function contrasts with the function
        :meth:`monomial_coefficient` which returns the coefficient in the
        base ring of a monomial.

        INPUT:

        - ``degrees`` -- can be any of:
          - a dictionary of degree restrictions
          - a list of degree restrictions (with ``None`` in the unrestricted variables)
          - a monomial (very fast, but not as flexible)

        OUTPUT: element of the parent of this element

        .. NOTE::

           For coefficients of specific monomials, look at :meth:`monomial_coefficient`.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=x*y+y+5
            sage: f.coefficient({x:0,y:1})
            1
            sage: f.coefficient({x:0})
            y + 5
            sage: f=(1+y+y^2)*(1+x+x^2)
            sage: f.coefficient({x:0})
            z + y^2 + y + 1

            sage: f.coefficient(x)
            y^2 - y + 1

            sage: f.coefficient([0,None]) # not tested
            y^2 + y + 1

        Be aware that this may not be what you think! The physical
        appearance of the variable x is deceiving -- particularly if
        the exponent would be a variable. ::

            sage: f.coefficient(x^0) # outputs the full polynomial
            x^2*y^2 + x^2*y + x^2 + x*y^2 - x*y + x + z + y^2 + y + 1

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=x*y+5
            sage: c=f.coefficient({x:0,y:0}); c
            5
            sage: parent(c)
            Noncommutative Multivariate Polynomial Ring in x, z, y over Finite Field of size 389, nc-relations: {y*x: -x*y + z}

        AUTHOR:

        - Joel B. Mohler (2007-10-31)"""
    @overload
    def coefficient(self, x) -> Any:
        """NCPolynomial_plural.coefficient(self, degrees)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2017)

        Return the coefficient of the variables with the degrees
        specified in the python dictionary ``degrees``.

        Mathematically, this is the coefficient in the base ring
        adjoined by the variables of this ring not listed in
        ``degrees``.  However, the result has the same parent as this
        polynomial.

        This function contrasts with the function
        :meth:`monomial_coefficient` which returns the coefficient in the
        base ring of a monomial.

        INPUT:

        - ``degrees`` -- can be any of:
          - a dictionary of degree restrictions
          - a list of degree restrictions (with ``None`` in the unrestricted variables)
          - a monomial (very fast, but not as flexible)

        OUTPUT: element of the parent of this element

        .. NOTE::

           For coefficients of specific monomials, look at :meth:`monomial_coefficient`.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=x*y+y+5
            sage: f.coefficient({x:0,y:1})
            1
            sage: f.coefficient({x:0})
            y + 5
            sage: f=(1+y+y^2)*(1+x+x^2)
            sage: f.coefficient({x:0})
            z + y^2 + y + 1

            sage: f.coefficient(x)
            y^2 - y + 1

            sage: f.coefficient([0,None]) # not tested
            y^2 + y + 1

        Be aware that this may not be what you think! The physical
        appearance of the variable x is deceiving -- particularly if
        the exponent would be a variable. ::

            sage: f.coefficient(x^0) # outputs the full polynomial
            x^2*y^2 + x^2*y + x^2 + x*y^2 - x*y + x + z + y^2 + y + 1

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=x*y+5
            sage: c=f.coefficient({x:0,y:0}); c
            5
            sage: parent(c)
            Noncommutative Multivariate Polynomial Ring in x, z, y over Finite Field of size 389, nc-relations: {y*x: -x*y + z}

        AUTHOR:

        - Joel B. Mohler (2007-10-31)"""
    @overload
    def constant_coefficient(self) -> Any:
        """NCPolynomial_plural.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2599)

        Return the constant coefficient of this multivariate
        polynomial.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.constant_coefficient()
            5
            sage: f = 3*x^2
            sage: f.constant_coefficient()
            0"""
    @overload
    def constant_coefficient(self) -> Any:
        """NCPolynomial_plural.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2599)

        Return the constant coefficient of this multivariate
        polynomial.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.constant_coefficient()
            5
            sage: f = 3*x^2
            sage: f.constant_coefficient()
            0"""
    @overload
    def constant_coefficient(self) -> Any:
        """NCPolynomial_plural.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2599)

        Return the constant coefficient of this multivariate
        polynomial.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.constant_coefficient()
            5
            sage: f = 3*x^2
            sage: f.constant_coefficient()
            0"""
    @overload
    def degree(self, NCPolynomial_pluralx=...) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, x) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, y) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, x) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, y) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, x) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degree(self, x) -> Any:
        """NCPolynomial_plural.degree(self, NCPolynomial_plural x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1889)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent of
          self) If x is not specified (or is ``None``), return the total
          degree, which is the maximum degree of any monomial.

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: P(0).degree(x)
            -1
            sage: P(1).degree(x)
            0"""
    @overload
    def degrees(self) -> Any:
        """NCPolynomial_plural.degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1986)

        Return a tuple with the maximal degree of each variable in
        this polynomial.

        The list of degrees is ordered by the order
        of the generators.

        EXAMPLES::

            sage: A.<y0,y1,y2> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y1*y0:-y0*y1 + y2},  order='lex')
            sage: R.inject_variables()
            Defining y0, y1, y2
            sage: q = 3*y0*y1*y1*y2; q
            3*y0*y1^2*y2
            sage: q.degrees()
            (1, 2, 1)
            sage: (q + y0^5).degrees()
            (5, 2, 1)"""
    @overload
    def degrees(self) -> Any:
        """NCPolynomial_plural.degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1986)

        Return a tuple with the maximal degree of each variable in
        this polynomial.

        The list of degrees is ordered by the order
        of the generators.

        EXAMPLES::

            sage: A.<y0,y1,y2> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y1*y0:-y0*y1 + y2},  order='lex')
            sage: R.inject_variables()
            Defining y0, y1, y2
            sage: q = 3*y0*y1*y1*y2; q
            3*y0*y1^2*y2
            sage: q.degrees()
            (1, 2, 1)
            sage: (q + y0^5).degrees()
            (5, 2, 1)"""
    @overload
    def degrees(self) -> Any:
        """NCPolynomial_plural.degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1986)

        Return a tuple with the maximal degree of each variable in
        this polynomial.

        The list of degrees is ordered by the order
        of the generators.

        EXAMPLES::

            sage: A.<y0,y1,y2> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y1*y0:-y0*y1 + y2},  order='lex')
            sage: R.inject_variables()
            Defining y0, y1, y2
            sage: q = 3*y0*y1*y1*y2; q
            3*y0*y1^2*y2
            sage: q.degrees()
            (1, 2, 1)
            sage: (q + y0^5).degrees()
            (5, 2, 1)"""
    @overload
    def dict(self) -> dict:
        """NCPolynomial_plural.dict(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2200)

        Return a dictionary representing ``self``. This dictionary is in
        the same format as the generic MPolynomial: The dictionary
        consists of ``ETuple:coefficient`` pairs.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y

            sage: f = (2*x*y^3*z^2 + (7)*x^2 + (3))
            sage: f.dict()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}

            sage: f.monomial_coefficients()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}"""
    @overload
    def dict(self) -> Any:
        """NCPolynomial_plural.dict(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2200)

        Return a dictionary representing ``self``. This dictionary is in
        the same format as the generic MPolynomial: The dictionary
        consists of ``ETuple:coefficient`` pairs.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y

            sage: f = (2*x*y^3*z^2 + (7)*x^2 + (3))
            sage: f.dict()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}

            sage: f.monomial_coefficients()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}"""
    @overload
    def exponents(self, as_ETuples=...) -> Any:
        """NCPolynomial_plural.exponents(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2415)

        Return the exponents of the monomials appearing in this polynomial.

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True`` returns
          the result as an list of ETuples, otherwise returns a list of tuples

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = x^3 + y + 2*z^2
            sage: f.exponents()
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]
            sage: f.exponents(as_ETuples=False)
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]"""
    @overload
    def exponents(self) -> Any:
        """NCPolynomial_plural.exponents(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2415)

        Return the exponents of the monomials appearing in this polynomial.

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True`` returns
          the result as an list of ETuples, otherwise returns a list of tuples

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = x^3 + y + 2*z^2
            sage: f.exponents()
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]
            sage: f.exponents(as_ETuples=False)
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]"""
    @overload
    def exponents(self, as_ETuples=...) -> Any:
        """NCPolynomial_plural.exponents(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2415)

        Return the exponents of the monomials appearing in this polynomial.

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True`` returns
          the result as an list of ETuples, otherwise returns a list of tuples

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = x^3 + y + 2*z^2
            sage: f.exponents()
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]
            sage: f.exponents(as_ETuples=False)
            [(3, 0, 0), (0, 2, 0), (0, 0, 1)]"""
    @overload
    def is_constant(self) -> Any:
        """NCPolynomial_plural.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2630)

        Return ``True`` if this polynomial is constant.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_constant()
            False
            sage: P(1).is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """NCPolynomial_plural.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2630)

        Return ``True`` if this polynomial is constant.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_constant()
            False
            sage: P(1).is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """NCPolynomial_plural.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2630)

        Return ``True`` if this polynomial is constant.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_constant()
            False
            sage: P(1).is_constant()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_homogeneous(self) -> Any:
        """NCPolynomial_plural.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2458)

        Return ``True`` if this polynomial is homogeneous.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y+z).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x+y^2+z^3).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """NCPolynomial_plural.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2486)

        Return ``True`` if this polynomial is a monomial.

        A monomial is defined to be a product of generators with
        coefficient 1.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_monomial()
            True
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True
            sage: (x*y + x).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """NCPolynomial_plural.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2486)

        Return ``True`` if this polynomial is a monomial.

        A monomial is defined to be a product of generators with
        coefficient 1.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_monomial()
            True
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True
            sage: (x*y + x).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """NCPolynomial_plural.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2486)

        Return ``True`` if this polynomial is a monomial.

        A monomial is defined to be a product of generators with
        coefficient 1.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_monomial()
            True
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True
            sage: (x*y + x).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """NCPolynomial_plural.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2486)

        Return ``True`` if this polynomial is a monomial.

        A monomial is defined to be a product of generators with
        coefficient 1.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_monomial()
            True
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True
            sage: (x*y + x).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """NCPolynomial_plural.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2486)

        Return ``True`` if this polynomial is a monomial.

        A monomial is defined to be a product of generators with
        coefficient 1.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: x.is_monomial()
            True
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True
            sage: (x*y + x).is_monomial()
            False"""
    @overload
    def is_zero(self) -> Any:
        """NCPolynomial_plural.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2766)

        Return ``True`` if this polynomial is zero.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y

            sage: x.is_zero()
            False
            sage: (x-x).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """NCPolynomial_plural.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2766)

        Return ``True`` if this polynomial is zero.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y

            sage: x.is_zero()
            False
            sage: (x-x).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """NCPolynomial_plural.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2766)

        Return ``True`` if this polynomial is zero.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y

            sage: x.is_zero()
            False
            sage: (x-x).is_zero()
            True"""
    @overload
    def lc(self) -> Any:
        """NCPolynomial_plural.lc(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2700)

        Leading coefficient of this polynomial with respect to the
        term order of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lc()
            3

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lc()
            5"""
    @overload
    def lc(self) -> Any:
        """NCPolynomial_plural.lc(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2700)

        Leading coefficient of this polynomial with respect to the
        term order of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lc()
            3

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lc()
            5"""
    @overload
    def lc(self) -> Any:
        """NCPolynomial_plural.lc(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2700)

        Leading coefficient of this polynomial with respect to the
        term order of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lc()
            3

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lc()
            5"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lm(self) -> Any:
        """NCPolynomial_plural.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2647)

        Return the lead monomial of ``self`` with respect to the term
        order of ``self.parent()``.

        In Sage, a monomial is a product of variables in some power
        without a coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2 + y^3*z^4
            sage: f.lm()
            x*y^2
            sage: f = x^3*y^2*z^4 + x^3*y^2*z^1
            sage: f.lm()
            x^3*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='deglex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^2*z^3 + x^3*y^2*z^0
            sage: f.lm()
            x*y^2*z^3
            sage: f = x^1*y^2*z^4 + x^1*y^1*z^5
            sage: f.lm()
            x*y^2*z^4

            sage: A.<x,y,z> = FreeAlgebra(GF(127), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='degrevlex')
            sage: R.inject_variables()
            Defining x, y, z
            sage: f = x^1*y^5*z^2 + x^4*y^1*z^3
            sage: f.lm()
            x*y^5*z^2
            sage: f = x^4*y^7*z^1 + x^4*y^2*z^3
            sage: f.lm()
            x^4*y^7*z"""
    @overload
    def lt(self) -> Any:
        """NCPolynomial_plural.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2738)

        Return the leading term of this polynomial.

        In Sage, a term is a product of variables in some power and a
        coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lt()
            3*x*y^2

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lt()
            -2*x^3*y^2*z^4"""
    @overload
    def lt(self) -> Any:
        """NCPolynomial_plural.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2738)

        Return the leading term of this polynomial.

        In Sage, a term is a product of variables in some power and a
        coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lt()
            3*x*y^2

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lt()
            -2*x^3*y^2*z^4"""
    @overload
    def lt(self) -> Any:
        """NCPolynomial_plural.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2738)

        Return the leading term of this polynomial.

        In Sage, a term is a product of variables in some power and a
        coefficient.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(GF(7), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, y, z

            sage: f = 3*x^1*y^2 + 2*y^3*z^4
            sage: f.lt()
            3*x*y^2

            sage: f = 5*x^3*y^2*z^4 + 4*x^3*y^2*z^1
            sage: f.lt()
            -2*x^3*y^2*z^4"""
    def monomial_coefficient(self, NCPolynomial_pluralmon) -> Any:
        """NCPolynomial_plural.monomial_coefficient(self, NCPolynomial_plural mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2142)

        Return the coefficient in the base ring of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same parent as ``self``.

        This function contrasts with the function :meth:`coefficient`
        which returns the coefficient of a monomial viewing this
        polynomial in a polynomial ring over a base ring having fewer
        variables.

        INPUT:

        - ``mon`` -- a monomial

        OUTPUT: coefficient in base ring

        .. SEEALSO::

            For coefficients in a base ring of fewer variables, look at :meth:`coefficient`

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y

            The parent of the return is a member of the base ring.
            sage: f = 2 * x * y
            sage: c = f.monomial_coefficient(x*y); c
            2
            sage: c.parent()
            Finite Field of size 389

            sage: f = y^2 + y^2*x - x^9 - 7*x + 5*x*y
            sage: f.monomial_coefficient(y^2)
            1
            sage: f.monomial_coefficient(x*y)
            5
            sage: f.monomial_coefficient(x^9)
            388
            sage: f.monomial_coefficient(x^10)
            0"""
    @overload
    def monomial_coefficients(self, boolcopy=...) -> dict:
        """NCPolynomial_plural.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2243)

        Return a dictionary representation of ``self`` with the keys
        the exponent vectors and the values the corresponding coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = (2*x*y^3*z^2 + (7)*x^2 + (3))
            sage: d = f.monomial_coefficients(False); d
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}
            sage: d.clear()
            sage: f.monomial_coefficients()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}"""
    @overload
    def monomial_coefficients(self, _False) -> Any:
        """NCPolynomial_plural.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2243)

        Return a dictionary representation of ``self`` with the keys
        the exponent vectors and the values the corresponding coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = (2*x*y^3*z^2 + (7)*x^2 + (3))
            sage: d = f.monomial_coefficients(False); d
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}
            sage: d.clear()
            sage: f.monomial_coefficients()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """NCPolynomial_plural.monomial_coefficients(self, bool copy=True) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2243)

        Return a dictionary representation of ``self`` with the keys
        the exponent vectors and the values the corresponding coefficients.

        INPUT:

        - ``copy`` -- ignored

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = (2*x*y^3*z^2 + (7)*x^2 + (3))
            sage: d = f.monomial_coefficients(False); d
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}
            sage: d.clear()
            sage: f.monomial_coefficients()
            {(0, 0, 0): 3, (1, 2, 3): 2, (2, 0, 0): 7}"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def monomials(self) -> Any:
        """NCPolynomial_plural.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2527)

        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x + (3*2)*y*z^2 + (2+3)
            sage: f.monomials()
            [x, z^2*y, 1]
            sage: f = P(3^2)
            sage: f.monomials()
            [1]

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: f = x
            sage: f.monomials()
            [x]

        Check if :issue:`12706` is fixed::

            sage: f = P(0)
            sage: f.monomials()
            []

        Check if :issue:`7152` is fixed::

            sage: # needs sage.symbolic
            sage: x = var('x')
            sage: K.<rho> = NumberField(x**2 + 1)
            sage: R.<x,y> = QQ[]
            sage: p = rho*x
            sage: q = x
            sage: p.monomials()
            [x]
            sage: q.monomials()
            [x]
            sage: p.monomials()
            [x]"""
    @overload
    def reduce(self, I) -> Any:
        """NCPolynomial_plural.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1747)


        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()],coerce=False)

        The result of reduction is not the normal form, if one reduces
        by a list of polynomials::

            sage: (x*z).reduce(I.gens())
            x*z

        However, if the argument is an ideal, then a normal form (reduction
        with respect to a two-sided Groebner basis) is returned::

            sage: (x*z).reduce(I)
            -x

        The Groebner basis shows that the result is correct::

            sage: I.std() #random
            Left Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2) of
            Noncommutative Multivariate Polynomial Ring in x, y, z over Rational
            Field, nc-relations: {z*x: x*z + 2*x, z*y: y*z - 2*y, y*x: x*y - z}
            sage: sorted(I.std().gens(),key=str)
            [2*x*y - z - 1, x*z + x, x^2, y*z - y, y^2, z^2 - 1]"""
    @overload
    def reduce(self, I) -> Any:
        """NCPolynomial_plural.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1747)


        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: I = H.ideal([y^2, x^2, z^2-H.one()],coerce=False)

        The result of reduction is not the normal form, if one reduces
        by a list of polynomials::

            sage: (x*z).reduce(I.gens())
            x*z

        However, if the argument is an ideal, then a normal form (reduction
        with respect to a two-sided Groebner basis) is returned::

            sage: (x*z).reduce(I)
            -x

        The Groebner basis shows that the result is correct::

            sage: I.std() #random
            Left Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2) of
            Noncommutative Multivariate Polynomial Ring in x, y, z over Rational
            Field, nc-relations: {z*x: x*z + 2*x, z*y: y*z - 2*y, y*x: x*y - z}
            sage: sorted(I.std().gens(),key=str)
            [2*x*y - z - 1, x*z + x, x^2, y*z - y, y^2, z^2 - 1]"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    @overload
    def total_degree(self) -> Any:
        """NCPolynomial_plural.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1941)

        Return the total degree of ``self``, which is the maximum degree
        of all monomials in ``self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f=2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f=4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f=99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f=x*y^3*z^6+3*x^2
            sage: f.total_degree()
            10
            sage: f=z^3+8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f=z^9+10*x^4+y^8*x^2
            sage: f.total_degree()
            10

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: R(0).total_degree()
            -1
            sage: R(1).total_degree()
            0"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """NCPolynomial_plural.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2800)

        EXAMPLES::

            sage: F.<x,y,z>=FreeAlgebra(QQ,3)
            sage: G = F.g_algebra({y*x: -x*y})
            sage: G.inject_variables()
            Defining x, y, z
            sage: a = x+y+x*y
            sage: a.subs(x=0, y=1)
            1
            sage: a.subs(x=y,y=x) == x + y - x*y
            True"""
    def __getitem__(self, x) -> Any:
        """NCPolynomial_plural.__getitem__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 2351)

        Same as :meth:`monomial_coefficient` but for exponent vectors.

        INPUT:

        - ``x`` -- tuple or, in case of a single-variable MPolynomial
          ring ``x`` can also be an integer

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(GF(389), 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = (-10*x^3*y + 17*x*y)* ( 15*z^3 + 2*x*y*z - 1); f
            20*x^4*z*y^2 - 150*x^3*z^3*y - 20*x^3*z^2*y + 10*x^3*y - 34*x^2*z*y^2 - 134*x*z^3*y + 34*x*z^2*y - 17*x*y
            sage: f[4,1,2]
            20
            sage: f[1,0,1]
            372
            sage: f[0,0,0]
            0

            sage: R.<x> = PolynomialRing(GF(7), implementation='singular'); R
            Multivariate Polynomial Ring in x over Finite Field of size 7
            sage: f = 5*x^2 + 3; f
            -2*x^2 + 3
            sage: f[2]
            5"""
    def __hash__(self) -> Any:
        """NCPolynomial_plural.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1458)

        This hash incorporates the variable name in an effort to
        respect the obvious inclusions into multi-variable polynomial
        rings.

        The tuple algorithm is borrowed from http://effbot.org/zone/python-hash.htm.

        EXAMPLES::

            sage: R.<x>=QQ[]
            sage: S.<x,y>=QQ[]
            sage: hash(S(1/2))==hash(1/2)  # respect inclusions of the rationals
            True
            sage: hash(S.0)==hash(R.0)  # respect inclusions into mpoly rings
            True
            sage: # the point is to make for more flexible dictionary look ups
            sage: d={S.0:12}
            sage: d[R.0]
            12"""
    def __neg__(self) -> Any:
        """NCPolynomial_plural.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1727)

        Return ``-self``.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = x^3 + y
            sage: -f
            -x^3 - y"""
    def __pow__(self, NCPolynomial_pluralself, exp, mod) -> Any:
        """NCPolynomial_plural.__pow__(NCPolynomial_plural self, exp, mod)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1669)

        Return ``self**(exp)``.

        The exponent must be an integer.

        EXAMPLES::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: R = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: R.inject_variables()
            Defining x, z, y
            sage: f = x^3 + y
            sage: f^2
            x^6 + x^2*z + y^2

        TESTS::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: (x+y^2^31)^10
            Traceback (most recent call last):
            ....
            OverflowError: exponent overflow (2147483648)

        Check that using third argument raises an error::

            sage: A.<x,z,y> = FreeAlgebra(QQ, 3)
            sage: P = A.g_algebra(relations={y*x:-x*y + z},  order='lex')
            sage: P.inject_variables()
            Defining x, z, y
            sage: pow(x + y + z, 2, x)
            Traceback (most recent call last):
            ...
            NotImplementedError: pow() with a modulus is not implemented for this ring"""
    def __reduce__(self) -> Any:
        """NCPolynomial_plural.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/plural.pyx (starting at line 1447)

        TESTS::

            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: loads(dumps(x*y+2*z+4*x*y*z*x))
            4*x^2*y*z + 8*x^2*y - 4*x*z^2 + x*y - 8*x*z + 2*z"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
