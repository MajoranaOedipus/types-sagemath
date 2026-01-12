import _cython_3_2_1
import sage.structure.parent_gens
from sage.categories.algebras import Algebras as Algebras
from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.dedekind_domains import DedekindDomains as DedekindDomains
from sage.categories.fields import Fields as Fields
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.noetherian_rings import NoetherianRings as NoetherianRings
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.superseded import deprecation as deprecation
from typing import Any, ClassVar, overload

__pyx_capi__: dict
is_Ring: _cython_3_2_1.cython_function_or_method

class Algebra(Ring):
    """Algebra(base_ring, *args, **kwds)"""
    
    def __init__(self, base_ring, *args, **kwds):
        """"""

class CommutativeAlgebra(CommutativeRing):
    """CommutativeAlgebra(base_ring, *args, **kwds)"""
    
    def __init__(self, base_ring, *args, **kwds):
        """"""

class CommutativeRing(Ring):
    """
    Generic commutative ring."""
    
    def __init__(self, base_ring, names=..., normalize=..., category=...):
        """
                Initialize ``self``.

                EXAMPLES::

                    sage: Integers(389)['x,y']
                    Multivariate Polynomial Ring in x, y over Ring of integers modulo 389
        """
    def extension(self, poly, name=..., names=..., **kwds) -> Any:
        """
        Algebraically extend ``self`` by taking the quotient
        ``self[x] / (f(x))``.

        INPUT:

        - ``poly`` -- a polynomial whose coefficients are coercible into
          ``self``

        - ``name`` -- (optional) name for the root of `f`

        .. NOTE::

            Using this method on an algebraically complete field does *not*
            return this field; the construction ``self[x] / (f(x))`` is done
            anyway.

        EXAMPLES::

            sage: R = QQ['x']
            sage: y = polygen(R)
            sage: R.extension(y^2 - 5, 'a')                                             # needs sage.libs.pari
            Univariate Quotient Polynomial Ring in a over
             Univariate Polynomial Ring in x over Rational Field with modulus a^2 - 5

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x> = PolynomialRing(GF(5))
            sage: F.<a> = GF(5).extension(x^2 - 2)
            sage: P.<t> = F[]
            sage: R.<b> = F.extension(t^2 - a); R
            Univariate Quotient Polynomial Ring in b over
             Finite Field in a of size 5^2 with modulus b^2 + 4*a"""

    def fraction_field(self) -> Any:
        """
        Return the fraction field of ``self``.

        EXAMPLES::

            sage: R = Integers(389)['x,y']
            sage: Frac(R)
            Fraction Field of Multivariate Polynomial Ring in x, y over Ring of integers modulo 389
            sage: R.fraction_field()
            Fraction Field of Multivariate Polynomial Ring in x, y over Ring of integers modulo 389"""

class DedekindDomain(CommutativeRing):
    """DedekindDomain(*args, **kwds)"""
    
    def __init__(self, *args, **kwds):
        """"""

class Field(CommutativeRing):
    """
        Generic field

        TESTS::

            sage: QQ.is_noetherian()
            True
    """
    
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class IntegralDomain(CommutativeRing):
    """IntegralDomain(*args, **kwds)"""
    
    def __init__(self, *args, **kwds):
        """"""

class NoetherianRing(CommutativeRing):
    """NoetherianRing(*args, **kwds)"""
    
    def __init__(self, *args, **kwds):
        """"""

class PrincipalIdealDomain(CommutativeRing):
    """PrincipalIdealDomain(*args, **kwds)"""
    
    def __init__(self, *args, **kwds):
        """"""

class Ring(sage.structure.parent_gens.ParentWithGens):
    """
    Generic ring class.

    TESTS:

    This is to test against the bug fixed in :issue:`9138`::

        sage: R.<x> = QQ[]
        sage: R.sum([x,x])
        2*x
        sage: R.<x,y> = ZZ[]
        sage: R.sum([x,y])
        x + y
        sage: TestSuite(QQ['x']).run(verbose=True)
        running ._test_additive_associativity() . . . pass
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_characteristic() . . . pass
        running ._test_construction() . . . pass
        running ._test_distributivity() . . . pass
        running ._test_divides() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_monomial_coefficients() . . . pass
          running ._test_new() . . . pass
          running ._test_nonzero_equal() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_eq() . . . pass
        running ._test_euclidean_degree() . . . pass
        running ._test_fraction_field() . . . pass
        running ._test_gcd_vs_xgcd() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_quo_rem() . . . pass
        running ._test_some_elements() . . . pass
        running ._test_zero() . . . pass
        running ._test_zero_divisors() . . . pass
        sage: TestSuite(QQ['x','y']).run(skip='_test_elements')                         # needs sage.libs.singular
        sage: TestSuite(ZZ['x','y']).run(skip='_test_elements')                         # needs sage.libs.singular
        sage: TestSuite(ZZ['x','y']['t']).run()

    Test against another bug fixed in :issue:`9944`::

        sage: QQ['x'].category()
        Join of Category of euclidean domains
            and Category of algebras with basis
                over (number fields and quotient fields and metric spaces)
            and Category of commutative algebras
                over (number fields and quotient fields and metric spaces)
            and Category of infinite sets
        sage: QQ['x','y'].category()
        Join of Category of unique factorization domains
            and Category of algebras with basis
                over (number fields and quotient fields and metric spaces)
            and Category of commutative algebras
                over (number fields and quotient fields and metric spaces)
            and Category of infinite sets
        sage: PolynomialRing(MatrixSpace(QQ, 2),'x').category()                         # needs sage.modules
        Category of infinite algebras with basis
            over (finite dimensional algebras with basis
                    over (number fields and quotient fields and metric spaces)
                  and infinite sets)
        sage: PolynomialRing(SteenrodAlgebra(2),'x').category()                         # needs sage.combinat sage.modules
        Category of infinite algebras with basis
            over (super Hopf algebras with basis over Finite Field of size 2
                  and supercocommutative super coalgebras
                      over Finite Field of size 2)

    TESTS::

        sage: Zp(7)._repr_option('element_is_atomic')                                   # needs sage.rings.padics
        False
        sage: QQ._repr_option('element_is_atomic')
        True
        sage: CDF._repr_option('element_is_atomic')                                     # needs sage.rings.complex_double
        False

    Check that categories correctly implement ``is_finite`` and ``cardinality``::

        sage: QQ.is_finite()
        False
        sage: GF(2^10, 'a').is_finite()                                                 # needs sage.rings.finite_rings
        True
        sage: R.<x> = GF(7)[]
        sage: R.is_finite()
        False
        sage: S.<y> = R.quo(x^2 + 1)                                                    # needs sage.rings.finite_rings
        sage: S.is_finite()                                                             # needs sage.rings.finite_rings
        True

        sage: Integers(7).cardinality()
        7
        sage: QQ.cardinality()
        +Infinity
 """
    
    def __init__(self, base, names=..., normalize=..., category=...):
        """
                Initialize ``self``.

                EXAMPLES::

                    sage: ZZ
                    Integer Ring
                    sage: R.<x,y> = QQ[]
                    sage: R
                    Multivariate Polynomial Ring in x, y over Rational Field
        """
    def base_extend(self, R) -> Any:
        """
        EXAMPLES::

            sage: QQ.base_extend(GF(7))
            Traceback (most recent call last):
            ...
            TypeError: no base extension defined
            sage: ZZ.base_extend(GF(7))
            Finite Field of size 7"""

    def category(self) -> Any:
        """
        Return the category to which this ring belongs.

        .. NOTE::

            This method exists because sometimes a ring is its own base ring.
            During initialisation of a ring `R`, it may be checked whether the
            base ring (hence, the ring itself) is a ring. Hence, it is
            necessary that ``R.category()`` tells that ``R`` is a ring, even
            *before* its category is properly initialised.

        EXAMPLES::

            sage: FreeAlgebra(QQ, 3, 'x').category()  # todo: use a ring which is not an algebra!   # needs sage.combinat sage.modules
            Category of algebras with basis over Rational Field

        Since a quotient of the integers is its own base ring, and during
        initialisation of a ring it is tested whether the base ring belongs
        to the category of rings, the following is an indirect test that the
        ``category()`` method of rings returns the category of rings
        even before the initialisation was successful::

            sage: I = Integers(15)
            sage: I.base_ring() is I
            True
            sage: I.category()
            Join of Category of finite commutative rings
                and Category of subquotients of monoids
                and Category of quotients of semigroups
                and Category of finite enumerated sets"""

    def one(self) -> Any:
        """
        Return the one element of this ring (cached), if it exists.

        EXAMPLES::

            sage: ZZ.one()
            1
            sage: QQ.one()
            1
            sage: QQ['x'].one()
            1

        The result is cached::

            sage: ZZ.one() is ZZ.one()
            True"""

    def order(self) -> Any:
        """
        The number of elements of ``self``.

        EXAMPLES::

            sage: GF(19).order()
            19
            sage: QQ.order()
            +Infinity"""

    def zero(self) -> Any:
        """
        Return the zero element of this ring (cached).

        EXAMPLES::

            sage: ZZ.zero()
            0
            sage: QQ.zero()
            0
            sage: QQ['x'].zero()
            0

        The result is cached::

            sage: ZZ.zero() is ZZ.zero()
            True"""
    def __iter__(ZZ) -> Any:
        """
        Return an iterator through the elements of ``self``.
        Not implemented in general.

        EXAMPLES::

            sage: sage.rings.ring.Ring.__iter__(ZZ)
            Traceback (most recent call last):
            ...
            NotImplementedError: object does not support iteration"""
    def __len__(self) -> Any:
        """
        Return the cardinality of this ring if it is finite, else raise
        a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: len(Integers(24))
            24
            sage: len(RR)
            Traceback (most recent call last):
            ...
            NotImplementedError: len() of an infinite set"""
    def __mul__(self, x) -> Any:
        """
        Return the ideal ``x*R`` generated by ``x``, where ``x`` is either an
        element or tuple or list of elements.

        EXAMPLES::

            sage: R.<x,y,z> = GF(7)[]
            sage: (x + y) * R
            Ideal (x + y) of Multivariate Polynomial Ring in x, y, z
             over Finite Field of size 7
            sage: (x + y, z + y^3) * R
            Ideal (x + y, y^3 + z) of Multivariate Polynomial Ring in x, y, z
             over Finite Field of size 7

        The following was implemented in :issue:`7797`::

            sage: # needs sage.combinat sage.modules
            sage: A = SteenrodAlgebra(2)
            sage: A * [A.1 + A.2, A.1^2]
            Left Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra, milnor basis
            sage: [A.1 + A.2, A.1^2] * A
            Right Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra, milnor basis
            sage: A * [A.1 + A.2, A.1^2] * A
            Twosided Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra, milnor basis"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __xor__(self, n) -> Any:
        """
        Trap the operation ``^``.

        EXAMPLES::

            sage: eval('RR^3')
            Traceback (most recent call last):
            ...
            RuntimeError: use ** for exponentiation, not '^', which means xor in Python, and has the wrong precedence"""
