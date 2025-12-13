import _cython_3_2_1
import sage as sage
import sage.categories.action
import sage.misc.weak_dict
import sage.monoids.monoid
import sage.rings.polynomial.multi_polynomial
import sage.rings.polynomial.multi_polynomial_ideal
import sage.rings.polynomial.multi_polynomial_ring_base
import sage.structure.element
import sage.structure.unique_representation
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.randstate import current_randstate as current_randstate
from sage.monoids.monoid import Monoid_class as Monoid_class
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.ideal import FieldIdeal as FieldIdeal
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal as MPolynomialIdeal
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

Monomial: MonomialFactory
Polynomial: PolynomialFactory
TermOrder_from_pb_order: _cython_3_2_1.cython_function_or_method
Variable: VariableFactory
add_up_polynomials: _cython_3_2_1.cython_function_or_method
block_dlex: int
block_dp_asc: int
contained_vars: _cython_3_2_1.cython_function_or_method
dlex: int
dp: int
dp_asc: int
easy_linear_factors: _cython_3_2_1.cython_function_or_method
gauss_on_polys: _cython_3_2_1.cython_function_or_method
get_var_mapping: _cython_3_2_1.cython_function_or_method
if_then_else: _cython_3_2_1.cython_function_or_method
interpolate: _cython_3_2_1.cython_function_or_method
interpolate_smallest_lex: _cython_3_2_1.cython_function_or_method
inv_order_dict: dict
ll_red_nf_noredsb: _cython_3_2_1.cython_function_or_method
ll_red_nf_noredsb_single_recursive_call: _cython_3_2_1.cython_function_or_method
ll_red_nf_redsb: _cython_3_2_1.cython_function_or_method
lp: int
map_every_x_to_x_plus_one: _cython_3_2_1.cython_function_or_method
mod_mon_set: _cython_3_2_1.cython_function_or_method
mod_var_set: _cython_3_2_1.cython_function_or_method
mult_fact_sim_C: _cython_3_2_1.cython_function_or_method
nf3: _cython_3_2_1.cython_function_or_method
order_dict: dict
order_mapping: dict
parallel_reduce: _cython_3_2_1.cython_function_or_method
random_set: _cython_3_2_1.cython_function_or_method
recursively_insert: _cython_3_2_1.cython_function_or_method
red_tail: _cython_3_2_1.cython_function_or_method
rings: sage.misc.weak_dict.WeakValueDictionary
set_random_seed: _cython_3_2_1.cython_function_or_method
substitute_variables: _cython_3_2_1.cython_function_or_method
top_index: _cython_3_2_1.cython_function_or_method
unpickle_BooleanPolynomial: _cython_3_2_1.cython_function_or_method
unpickle_BooleanPolynomial0: _cython_3_2_1.cython_function_or_method
unpickle_BooleanPolynomialRing: _cython_3_2_1.cython_function_or_method
zeros: _cython_3_2_1.cython_function_or_method

class BooleConstant:
    """BooleConstant(int value)"""
    def __init__(self, intvalue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7767)

                Construct a boolean constant (modulo 2) from integer value:

                INPUT:

                - ``i`` -- integer

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
                    sage: [BooleConstant(i) for i in range(5)]
                    [0, 1, 0, 1, 0]
        """
    @overload
    def deg(self) -> Any:
        """BooleConstant.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7795)

        Get degree of boolean constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).deg()
            -1
            sage: BooleConstant(1).deg()
            0"""
    @overload
    def deg(self) -> Any:
        """BooleConstant.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7795)

        Get degree of boolean constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).deg()
            -1
            sage: BooleConstant(1).deg()
            0"""
    @overload
    def deg(self) -> Any:
        """BooleConstant.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7795)

        Get degree of boolean constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).deg()
            -1
            sage: BooleConstant(1).deg()
            0"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleConstant.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7865)

        This is true for `BooleConstant(1)`.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).has_constant_part()
            True
            sage: BooleConstant(0).has_constant_part()
            False"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleConstant.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7865)

        This is true for `BooleConstant(1)`.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).has_constant_part()
            True
            sage: BooleConstant(0).has_constant_part()
            False"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleConstant.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7865)

        This is true for `BooleConstant(1)`.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).has_constant_part()
            True
            sage: BooleConstant(0).has_constant_part()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleConstant.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7851)

        This is always true for in this case.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_constant()
            True
            sage: BooleConstant(0).is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """BooleConstant.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7851)

        This is always true for in this case.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_constant()
            True
            sage: BooleConstant(0).is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """BooleConstant.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7851)

        This is always true for in this case.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_constant()
            True
            sage: BooleConstant(0).is_constant()
            True"""
    @overload
    def is_one(self) -> Any:
        """BooleConstant.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7823)

        Check whether boolean constant is one.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).is_one()
            False
            sage: BooleConstant(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """BooleConstant.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7823)

        Check whether boolean constant is one.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).is_one()
            False
            sage: BooleConstant(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """BooleConstant.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7823)

        Check whether boolean constant is one.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).is_one()
            False
            sage: BooleConstant(1).is_one()
            True"""
    @overload
    def is_zero(self) -> Any:
        """BooleConstant.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7837)

        Check whether boolean constant is zero.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_zero()
            False
            sage: BooleConstant(0).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """BooleConstant.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7837)

        Check whether boolean constant is zero.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_zero()
            False
            sage: BooleConstant(0).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """BooleConstant.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7837)

        Check whether boolean constant is zero.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(1).is_zero()
            False
            sage: BooleConstant(0).is_zero()
            True"""
    @overload
    def variables(self) -> Any:
        """BooleConstant.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7809)

        Get variables (return always and empty tuple).

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).variables()
            ()
            sage: BooleConstant(1).variables()
            ()"""
    @overload
    def variables(self, returnalwaysandemptytuple) -> Any:
        """BooleConstant.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7809)

        Get variables (return always and empty tuple).

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).variables()
            ()
            sage: BooleConstant(1).variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleConstant.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7809)

        Get variables (return always and empty tuple).

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).variables()
            ()
            sage: BooleConstant(1).variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleConstant.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7809)

        Get variables (return always and empty tuple).

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleConstant
            sage: BooleConstant(0).variables()
            ()
            sage: BooleConstant(1).variables()
            ()"""

class BooleSet:
    """BooleSet(param=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5237)

    Return a new set of boolean monomials. This data type is also
    implemented on the top of ZDDs and allows to see polynomials from
    a different angle. Also, it makes high-level set operations
    possible, which are in most cases faster than operations handling
    individual terms, because the complexity of the algorithms depends
    only on the structure of the diagrams.

    Objects of type :class:`BooleanPolynomial` can easily be converted
    to the type :class:`BooleSet` by using the member function
    :meth:`BooleanPolynomial.set()`.

    INPUT:

    - ``param`` -- either a :class:`CCuddNavigator`, a :class:`BooleSet` or
      ``None``
    - ``ring`` -- boolean polynomial ring

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori.pbori import BooleSet
        sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
        sage: BS = BooleSet(a.set())
        sage: BS
        {{a}}

        sage: BS = BooleSet((a*b + c + 1).set())
        sage: BS
        {{a,b}, {c}, {}}

        sage: from sage.rings.polynomial.pbori.pbori import *
        sage: from sage.rings.polynomial.pbori.PyPolyBoRi import Monomial
        sage: BooleSet([Monomial(B)])
        {{}}

    .. NOTE::

      :class:`BooleSet` prints as ``{}`` but are not Python dictionaries."""
    def __init__(self, param=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5277)"""
    def cartesian_product(self, rhs) -> Any:
        """BooleSet.cartesian_product(self, rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5407)

        Return the Cartesian product of this set and the set ``rhs``.

        The Cartesian product of two sets X and Y is the set of all
        possible ordered pairs whose first component is a member of X and
        whose second component is a member of Y.


        .. MATH::

            X\\times Y = \\{(x,y) | x\\in X\\;\\mathrm{and}\\;y\\in Y\\}.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: g = x4 + 1
            sage: t = g.set(); t
            {{x4}, {}}
            sage: s.cartesian_product(t)
            {{x1,x2,x4}, {x1,x2}, {x2,x3,x4}, {x2,x3}}"""
    def change(self, ind) -> Any:
        """BooleSet.change(self, ind)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5503)

        Swaps the presence of ``x_i`` in each entry of the set.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing()
            sage: f = a+b
            sage: s = f.set(); s
            {{a}, {b}}
            sage: s.change(0)
            {{a,b}, {}}
            sage: s.change(1)
            {{a,b}, {}}
            sage: s.change(2)
            {{a,c}, {b,c}}"""
    def diff(self, rhs) -> Any:
        """BooleSet.diff(self, rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5436)

        Return the set theoretic difference of this set and the set
        ``rhs``.

        The difference of two sets `X` and `Y` is defined as:


        .. MATH::

            X \\ Y = \\{x | x\\in X\\;\\mathrm{and}\\;x\\not\\in Y\\}.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: g = x2*x3 + 1
            sage: t = g.set(); t
            {{x2,x3}, {}}
            sage: s.diff(t)
            {{x1,x2}}"""
    def divide(self, BooleanMonomialrhs) -> Any:
        """BooleSet.divide(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5667)

        Divide each element of this set by the monomial ``rhs`` and
        return a new set containing the result.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='lex')
            sage: f = b*e + b*c*d + b
            sage: s = f.set(); s
            {{b,c,d}, {b,e}, {b}}
            sage: s.divide(b.lm())
            {{c,d}, {e}, {}}

            sage: f = b*e + b*c*d + b + c
            sage: s = f.set()
            sage: s.divide(b.lm())
            {{c,d}, {e}, {}}"""
    def divisors_of(self, BooleanMonomialm) -> Any:
        """BooleSet.divisors_of(self, BooleanMonomial m)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5797)

        Return those members which are divisors of ``m``.

        INPUT:

        - ``m`` -- boolean monomial

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set()
            sage: s.divisors_of((x1*x2*x4).lead())
            {{x1,x2}}"""
    @overload
    def empty(self) -> Any:
        """BooleSet.empty(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5337)

        Return ``True`` if this set is empty.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.empty()
            False

            sage: BS = B(0).set()
            sage: BS.empty()
            True"""
    @overload
    def empty(self) -> Any:
        """BooleSet.empty(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5337)

        Return ``True`` if this set is empty.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.empty()
            False

            sage: BS = B(0).set()
            sage: BS.empty()
            True"""
    @overload
    def empty(self) -> Any:
        """BooleSet.empty(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5337)

        Return ``True`` if this set is empty.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.empty()
            False

            sage: BS = B(0).set()
            sage: BS.empty()
            True"""
    @overload
    def include_divisors(self) -> Any:
        """BooleSet.include_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5737)

        Extend this set to include all divisors of the elements
        already in this set and return the result as a new set.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: f = a*d*e + a*f + b*d*e + c*d*e + 1
            sage: s = f.set(); s
            {{a,d,e}, {a,f}, {b,d,e}, {c,d,e}, {}}

            sage: s.include_divisors()
            {{a,d,e}, {a,d}, {a,e}, {a,f}, {a}, {b,d,e}, {b,d}, {b,e},
             {b}, {c,d,e}, {c,d}, {c,e}, {c}, {d,e}, {d}, {e}, {f}, {}}"""
    @overload
    def include_divisors(self) -> Any:
        """BooleSet.include_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5737)

        Extend this set to include all divisors of the elements
        already in this set and return the result as a new set.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: f = a*d*e + a*f + b*d*e + c*d*e + 1
            sage: s = f.set(); s
            {{a,d,e}, {a,f}, {b,d,e}, {c,d,e}, {}}

            sage: s.include_divisors()
            {{a,d,e}, {a,d}, {a,e}, {a,f}, {a}, {b,d,e}, {b,d}, {b,e},
             {b}, {c,d,e}, {c,d}, {c,e}, {c}, {d,e}, {d}, {e}, {f}, {}}"""
    def intersect(self, BooleSetother) -> Any:
        """BooleSet.intersect(self, BooleSet other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5770)

        Return the set theoretic intersection of this set and the set
        ``rhs``.

        The union of two sets `X` and `Y` is defined as:


        .. MATH::

            X \\cap Y = \\{x | x\\in X\\;\\mathrm{and}\\;x\\in Y\\}.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: g = x2*x3 + 1
            sage: t = g.set(); t
            {{x2,x3}, {}}
            sage: s.intersect(t)
            {{x2,x3}}"""
    @overload
    def minimal_elements(self) -> Any:
        """BooleSet.minimal_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5755)

        Return a new set containing a divisor of all elements of this set.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: f = a*d*e + a*f + a*b*d*e + a*c*d*e + a
            sage: s = f.set(); s
            {{a,b,d,e}, {a,c,d,e}, {a,d,e}, {a,f}, {a}}
            sage: s.minimal_elements()
            {{a}}"""
    @overload
    def minimal_elements(self) -> Any:
        """BooleSet.minimal_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5755)

        Return a new set containing a divisor of all elements of this set.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: f = a*d*e + a*f + a*b*d*e + a*c*d*e + a
            sage: s = f.set(); s
            {{a,b,d,e}, {a,c,d,e}, {a,d,e}, {a,f}, {a}}
            sage: s.minimal_elements()
            {{a}}"""
    def multiples_of(self, BooleanMonomialm) -> Any:
        """BooleSet.multiples_of(self, BooleanMonomial m)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5816)

        Return those members which are multiples of ``m``.

        INPUT:

        - ``m`` -- boolean monomial

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set()
            sage: s.multiples_of(x1.lm())
            {{x1,x2}}"""
    @overload
    def n_nodes(self) -> Any:
        """BooleSet.n_nodes(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5539)

        Return the number of nodes in the ZDD.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: s.n_nodes()
            4"""
    @overload
    def n_nodes(self) -> Any:
        """BooleSet.n_nodes(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5539)

        Return the number of nodes in the ZDD.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: s.n_nodes()
            4"""
    @overload
    def navigation(self) -> Any:
        """BooleSet.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5354)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav = s.navigation()
            sage: BooleSet(nav, s.ring())
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav.value()
            1

            sage: nav_else = nav.else_branch()

            sage: BooleSet(nav_else, s.ring())
            {{x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav_else.value()
            2"""
    @overload
    def navigation(self) -> Any:
        """BooleSet.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5354)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav = s.navigation()
            sage: BooleSet(nav, s.ring())
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav.value()
            1

            sage: nav_else = nav.else_branch()

            sage: BooleSet(nav_else, s.ring())
            {{x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav_else.value()
            2"""
    @overload
    def ring(self) -> Any:
        """BooleSet.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5393)

        Return the parent ring.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: f.set().ring() is B
            True"""
    @overload
    def ring(self) -> Any:
        """BooleSet.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5393)

        Return the parent ring.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: f.set().ring() is B
            True"""
    @overload
    def set(self) -> Any:
        """BooleSet.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5324)

        Return ``self``.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.set() is BS
            True"""
    @overload
    def set(self) -> Any:
        """BooleSet.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5324)

        Return ``self``.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.set() is BS
            True"""
    @overload
    def set(self) -> Any:
        """BooleSet.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5324)

        Return ``self``.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: BS = (a*b + c).set()
            sage: BS.set() is BS
            True"""
    @overload
    def size_double(self) -> Any:
        """BooleSet.size_double(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5835)

        Return the size of this set as a floating point number.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set()
            sage: s.size_double()
            2.0"""
    @overload
    def size_double(self) -> Any:
        """BooleSet.size_double(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5835)

        Return the size of this set as a floating point number.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set()
            sage: s.size_double()
            2.0"""
    @overload
    def stable_hash(self) -> Any:
        """BooleSet.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5648)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x.set() is x.set()
            False
            sage: x.set().stable_hash() == x.set().stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    @overload
    def stable_hash(self) -> Any:
        """BooleSet.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5648)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x.set() is x.set()
            False
            sage: x.set().stable_hash() == x.set().stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    def subset0(self, inti) -> Any:
        """BooleSet.subset0(self, int i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5688)

        Return a set of those elements in this set which do not
        contain the variable indexed by ``i``.

        INPUT:

        - ``i`` -- an index

        EXAMPLES::

            sage: BooleanPolynomialRing(5,'x')
            Boolean PolynomialRing in x0, x1, x2, x3, x4
            sage: B = BooleanPolynomialRing(5,'x')
            sage: B.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: s.subset0(1)
            {{x2,x3}}"""
    def subset1(self, inti) -> Any:
        """BooleSet.subset1(self, int i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5712)

        Return a set of those elements in this set which do contain
        the variable indexed by ``i`` and evaluate the variable
        indexed by ``i`` to 1.

        INPUT:

        - ``i`` -- an index

        EXAMPLES::

            sage: BooleanPolynomialRing(5,'x')
            Boolean PolynomialRing in x0, x1, x2, x3, x4
            sage: B = BooleanPolynomialRing(5,'x')
            sage: B.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: s.subset1(1)
            {{x2}}"""
    def union(self, rhs) -> Any:
        """BooleSet.union(self, rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5470)

        Return the set theoretic union of this set and the set
        ``rhs``.

        The union of two sets `X` and `Y` is defined as:

        .. MATH::

            X \\cup Y = \\{x | x\\in X\\;\\mathrm{or}\\;x\\in Y\\}.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: g = x2*x3 + 1
            sage: t = g.set(); t
            {{x2,x3}, {}}
            sage: s.union(t)
            {{x1,x2}, {x2,x3}, {}}"""
    @overload
    def vars(self) -> Any:
        """BooleSet.vars(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5522)

        Return the variables in this set as a monomial.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='lex')
            sage: f = a + b*e + d*f + e + 1
            sage: s = f.set()
            sage: s
            {{a}, {b,e}, {d,f}, {e}, {}}
            sage: s.vars()
            a*b*d*e*f"""
    @overload
    def vars(self) -> Any:
        """BooleSet.vars(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5522)

        Return the variables in this set as a monomial.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='lex')
            sage: f = a + b*e + d*f + e + 1
            sage: s = f.set()
            sage: s
            {{a}, {b,e}, {d,f}, {e}, {}}
            sage: s.vars()
            a*b*d*e*f"""
    def __contains__(self, BooleanMonomialm) -> Any:
        """BooleSet.__contains__(self, BooleanMonomial m)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5618)

        Return ``True`` if ``m`` is in this set.

        INPUT:

        - ``m`` -- a monomial

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: f = a*b
            sage: s  = f.set()
            sage: a.lm() in s
            False

        TESTS::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: f = a*b
            sage: s  = f.set()
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: a.lm() in s
            Traceback (most recent call last):
            ...
            AssertionError"""
    def __hash__(self) -> Any:
        """BooleSet.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5582)

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: {s:1}
            {{{x1,x2}, {x2,x3}}: 1}"""
    def __iter__(self) -> Any:
        """BooleSet.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5555)

        Create an iterator over elements of ``self``.

        EXAMPLES::

            sage: P.<x, y> = BooleanPolynomialRing(2)
            sage: f = x*y+x+y+1; s = f.set()
            sage: list(s)
            [x*y, x, y, 1]"""
    def __len__(self) -> Any:
        """BooleSet.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5568)

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3
            sage: s = f.set(); s
            {{x1,x2}, {x2,x3}}
            sage: len(s)
            2"""
    def __mod__(self, BooleSetvs) -> Any:
        """BooleSet.__mod__(self, BooleSet vs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5596)

        Return a set of all monomials which are not divisible by
        monomials in ``vs``.

        INPUT:

        - ``vs`` -- boolean set

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: f = a*b + b + 1
            sage: s = f.set(); s
            {{a,b}, {b}, {}}
            sage: s % a.set()
            {{b}, {}}
            sage: s % b.set()
            {{}}"""
    def __rmod__(self, other):
        """Return value%self."""

class BooleSetIterator:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5863)

        Helper class to iterate over boolean sets.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """BooleSetIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5871)

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: f = B.random_element()
            sage: it = iter(f.set()) # indirect doctest"""
    def __next__(self) -> Any:
        """BooleSetIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5881)

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: f = B.random_element()
            sage: it = iter(f.set())
            sage: sum(next(it) for _ in range(5)) == f
            True"""

class BooleanMonomial(sage.structure.element.MonoidElement):
    """BooleanMonomial(parent)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2211)

    Construct a boolean monomial.

    INPUT:

    - ``parent`` -- parent monoid this element lives in

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid, BooleanMonomial
        sage: P.<x,y,z> = BooleanPolynomialRing(3)
        sage: M = BooleanMonomialMonoid(P)
        sage: BooleanMonomial(M)
        1

    .. NOTE::

       Use the :meth:`BooleanMonomialMonoid__call__` method and not
       this constructor to construct these objects."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2232)

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid, BooleanMonomial
                    sage: P.<x,y,z> = BooleanPolynomialRing(3)
                    sage: M = BooleanMonomialMonoid(P)
                    sage: BooleanMonomial(M)
                    1


                .. NOTE::

                  See class documentation for parameters.
        """
    @overload
    def __init__(self, M) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2232)

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid, BooleanMonomial
                    sage: P.<x,y,z> = BooleanPolynomialRing(3)
                    sage: M = BooleanMonomialMonoid(P)
                    sage: BooleanMonomial(M)
                    1


                .. NOTE::

                  See class documentation for parameters.
        """
    @overload
    def deg(self) -> Any:
        """BooleanMonomial.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2441)

        Return degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).deg()
            2

            sage: M(x*x*y*z).deg()
            3

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def deg(self) -> Any:
        """BooleanMonomial.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2441)

        Return degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).deg()
            2

            sage: M(x*x*y*z).deg()
            3

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def deg(self) -> Any:
        """BooleanMonomial.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2441)

        Return degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).deg()
            2

            sage: M(x*x*y*z).deg()
            3

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def degree(self, BooleanPolynomialx=...) -> Any:
        """BooleanMonomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2462)

        Return the degree of this monomial in ``x``, where
        ``x`` must be one of the generators of the polynomial ring.

        INPUT:

        - ``x`` -- boolean multivariate polynomial (a generator of the
          polynomial ring). If ``x`` is not specified (or is ``None``),
          return the total degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).degree()
            2
            sage: M(x*y).degree(x)
            1
            sage: M(x*y).degree(z)
            0"""
    @overload
    def degree(self) -> Any:
        """BooleanMonomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2462)

        Return the degree of this monomial in ``x``, where
        ``x`` must be one of the generators of the polynomial ring.

        INPUT:

        - ``x`` -- boolean multivariate polynomial (a generator of the
          polynomial ring). If ``x`` is not specified (or is ``None``),
          return the total degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).degree()
            2
            sage: M(x*y).degree(x)
            1
            sage: M(x*y).degree(z)
            0"""
    @overload
    def degree(self, x) -> Any:
        """BooleanMonomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2462)

        Return the degree of this monomial in ``x``, where
        ``x`` must be one of the generators of the polynomial ring.

        INPUT:

        - ``x`` -- boolean multivariate polynomial (a generator of the
          polynomial ring). If ``x`` is not specified (or is ``None``),
          return the total degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).degree()
            2
            sage: M(x*y).degree(x)
            1
            sage: M(x*y).degree(z)
            0"""
    @overload
    def degree(self, z) -> Any:
        """BooleanMonomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2462)

        Return the degree of this monomial in ``x``, where
        ``x`` must be one of the generators of the polynomial ring.

        INPUT:

        - ``x`` -- boolean multivariate polynomial (a generator of the
          polynomial ring). If ``x`` is not specified (or is ``None``),
          return the total degree of this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*y).degree()
            2
            sage: M(x*y).degree(x)
            1
            sage: M(x*y).degree(z)
            0"""
    @overload
    def divisors(self) -> Any:
        """BooleanMonomial.divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2496)

        Return a set of boolean monomials with all divisors of this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.divisors()
            {{x,y}, {x}, {y}, {}}"""
    @overload
    def divisors(self) -> Any:
        """BooleanMonomial.divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2496)

        Return a set of boolean monomials with all divisors of this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.divisors()
            {{x,y}, {x}, {y}, {}}"""
    @overload
    def gcd(self, BooleanMonomialrhs) -> Any:
        """BooleanMonomial.gcd(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2774)

        Return the greatest common divisor of this boolean monomial
        and ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: a,b,c,d = a.lm(), b.lm(), c.lm(), d.lm()
            sage: (a*b).gcd(b*c)
            b
            sage: (a*b*c).gcd(d)
            1"""
    @overload
    def gcd(self, d) -> Any:
        """BooleanMonomial.gcd(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2774)

        Return the greatest common divisor of this boolean monomial
        and ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: a,b,c,d = a.lm(), b.lm(), c.lm(), d.lm()
            sage: (a*b).gcd(b*c)
            b
            sage: (a*b*c).gcd(d)
            1"""
    @overload
    def index(self) -> Any:
        """BooleanMonomial.index(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2411)

        Return the variable index of the first variable in this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.index()
            0

        TESTS:

        Check that :issue:`13133` is resolved::

            sage: B(1).lm().index()
            Traceback (most recent call last):
            ...
            ValueError: no variables in constant monomial ; cannot take index()

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def index(self) -> Any:
        """BooleanMonomial.index(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2411)

        Return the variable index of the first variable in this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.index()
            0

        TESTS:

        Check that :issue:`13133` is resolved::

            sage: B(1).lm().index()
            Traceback (most recent call last):
            ...
            ValueError: no variables in constant monomial ; cannot take index()

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def index(self) -> Any:
        """BooleanMonomial.index(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2411)

        Return the variable index of the first variable in this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.index()
            0

        TESTS:

        Check that :issue:`13133` is resolved::

            sage: B(1).lm().index()
            Traceback (most recent call last):
            ...
            ValueError: no variables in constant monomial ; cannot take index()

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def index(self) -> Any:
        """BooleanMonomial.index(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2411)

        Return the variable index of the first variable in this
        monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.index()
            0

        TESTS:

        Check that :issue:`13133` is resolved::

            sage: B(1).lm().index()
            Traceback (most recent call last):
            ...
            ValueError: no variables in constant monomial ; cannot take index()

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def iterindex(self) -> Any:
        """BooleanMonomial.iterindex(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2616)

        Return an iterator over the indices of the variables in ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: list(M(x*z).iterindex())
            [0, 2]"""
    @overload
    def iterindex(self) -> Any:
        """BooleanMonomial.iterindex(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2616)

        Return an iterator over the indices of the variables in ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: list(M(x*z).iterindex())
            [0, 2]"""
    @overload
    def multiples(self, BooleanMonomialrhs) -> Any:
        """BooleanMonomial.multiples(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2511)

        Return a set of boolean monomials with all multiples of this
        monomial up to the bound ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x
            sage: m = f.lm()
            sage: g = x*y*z
            sage: n = g.lm()
            sage: m.multiples(n)
            {{x,y,z}, {x,y}, {x,z}, {x}}
            sage: n.multiples(m)
            {{x,y,z}}

        .. NOTE::

           The returned set always contains ``self`` even if the bound
           ``rhs`` is smaller than ``self``."""
    @overload
    def multiples(self, n) -> Any:
        """BooleanMonomial.multiples(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2511)

        Return a set of boolean monomials with all multiples of this
        monomial up to the bound ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x
            sage: m = f.lm()
            sage: g = x*y*z
            sage: n = g.lm()
            sage: m.multiples(n)
            {{x,y,z}, {x,y}, {x,z}, {x}}
            sage: n.multiples(m)
            {{x,y,z}}

        .. NOTE::

           The returned set always contains ``self`` even if the bound
           ``rhs`` is smaller than ``self``."""
    @overload
    def multiples(self, m) -> Any:
        """BooleanMonomial.multiples(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2511)

        Return a set of boolean monomials with all multiples of this
        monomial up to the bound ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x
            sage: m = f.lm()
            sage: g = x*y*z
            sage: n = g.lm()
            sage: m.multiples(n)
            {{x,y,z}, {x,y}, {x,z}, {x}}
            sage: n.multiples(m)
            {{x,y,z}}

        .. NOTE::

           The returned set always contains ``self`` even if the bound
           ``rhs`` is smaller than ``self``."""
    @overload
    def navigation(self) -> Any:
        """BooleanMonomial.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2744)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: m = f.lm(); m
            x1*x2

            sage: nav = m.navigation()
            sage: BooleSet(nav, B)
            {{x1,x2}}

            sage: nav.value()
            1"""
    @overload
    def navigation(self) -> Any:
        """BooleanMonomial.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2744)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1
            sage: m = f.lm(); m
            x1*x2

            sage: nav = m.navigation()
            sage: BooleSet(nav, B)
            {{x1,x2}}

            sage: nav.value()
            1"""
    def reducible_by(self, BooleanMonomialrhs) -> Any:
        """BooleanMonomial.reducible_by(self, BooleanMonomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2540)

        Return ``True`` if ``self`` is reducible by ``rhs``.

        INPUT:

        - ``rhs`` -- boolean monomial

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.reducible_by((x*y).lm())
            True
            sage: m.reducible_by((x*z).lm())
            False"""
    @overload
    def ring(self) -> Any:
        """BooleanMonomial.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2399)

        Return the corresponding boolean ring.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: a.lm().ring() is B
            True"""
    @overload
    def ring(self) -> Any:
        """BooleanMonomial.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2399)

        Return the corresponding boolean ring.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: a.lm().ring() is B
            True"""
    @overload
    def set(self) -> Any:
        """BooleanMonomial.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2560)

        Return a boolean set of variables in this monomials.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.set()
            {{x,y}}"""
    @overload
    def set(self) -> Any:
        """BooleanMonomial.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2560)

        Return a boolean set of variables in this monomials.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m.set()
            {{x,y}}"""
    @overload
    def stable_hash(self) -> Any:
        """BooleanMonomial.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2380)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x.lm() is x.lm()
            False
            sage: x.lm().stable_hash() == x.lm().stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    @overload
    def stable_hash(self) -> Any:
        """BooleanMonomial.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2380)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x.lm() is x.lm()
            False
            sage: x.lm().stable_hash() == x.lm().stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    @overload
    def variables(self) -> Any:
        """BooleanMonomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2602)

        Return a tuple of the variables in this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*z).variables() # indirect doctest
            (x, z)"""
    @overload
    def variables(self) -> Any:
        """BooleanMonomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2602)

        Return a tuple of the variables in this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M(x*z).variables() # indirect doctest
            (x, z)"""
    def __add__(self, left, right) -> Any:
        """BooleanMonomial.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2656)

        Addition operator. Return a boolean polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: x = M(x); xy = M(x*y)
            sage: x + xy
            x*y + x

            sage: x+0
            x
            sage: 0+x   # todo: not implemented
            x

            sage: x+1
            x + 1
            sage: 1 + x     # todo: not implemented
            x + 1"""
    def __call__(self, *args, **kwds) -> Any:
        """BooleanMonomial.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2334)

        Evaluate this monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: m(B(0),B(1))
            0
            sage: m(x=B(1))
            y"""
    def __floordiv__(self, BooleanMonomialleft, right) -> Any:
        """BooleanMonomial.__floordiv__(BooleanMonomial left, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2700)

        Floordiv operator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: x = M(x); xy = M(x*y)
            sage: xy//x
            y
            sage: x//xy
            0

            sage: x//0
            Traceback (most recent call last):
            ...
            ZeroDivisionError

            sage: x//1
            x"""
    def __hash__(self) -> Any:
        """BooleanMonomial.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2366)

        Return a hash of this monomial.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y
            sage: m = f.lm()
            sage: {m:1} #indirect doctest
            {x*y: 1}"""
    def __iter__(self) -> Any:
        """BooleanMonomial.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2588)

        Return an iterator over the variables in this monomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: list(M(x*z)) # indirect doctest
            [x, z]"""
    def __len__(self) -> Any:
        """BooleanMonomial.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2574)

        Return 1.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: len(M(x*y))
            1"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """BooleanMonomial.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2250)

        Pickling.

        TESTS::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: R.<z,x> = BooleanPolynomialRing(2)
            sage: M = BooleanMonomialMonoid(R)
            sage: t = M.0*M.1
            sage: loads(dumps(t)) == t   # indirect doctest
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""

class BooleanMonomialIterator:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2874)

        An iterator over the variable indices of a monomial.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """BooleanMonomialIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2878)

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + 1
            sage: for m in f: list(m.iterindex())# indirect doctest
            [0, 1]
            [2]
            []"""
    def __next__(self) -> Any:
        """BooleanMonomialIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2891)

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + 1
            sage: m = f.lm()
            sage: next(m.iterindex())
            0"""

class BooleanMonomialMonoid(sage.structure.unique_representation.UniqueRepresentation, sage.monoids.monoid.Monoid_class):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1849)

        Construct a boolean monomial monoid given a boolean polynomial
        ring.

        This object provides a parent for boolean monomials.

        INPUT:

        - ``polring`` -- the polynomial ring our monomials lie in

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: M = BooleanMonomialMonoid(P)
            sage: M
            MonomialMonoid of Boolean PolynomialRing in x, y

            sage: M.gens()
            (x, y)
            sage: type(M.gen(0))
            <class 'sage.rings.polynomial.pbori.pbori.BooleanMonomial'>

        Since :issue:`9138`, boolean monomial monoids are
        unique parents and are fit into the category framework::

            sage: loads(dumps(M)) is M
            True
            sage: TestSuite(M).run()
    """
    def __init__(self, BooleanPolynomialRingpolring) -> Any:
        """BooleanMonomialMonoid.__init__(self, BooleanPolynomialRing polring)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1880)

        Create a new boolean polynomial ring.

        TESTS::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: B.<a,b,c> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(B)
            sage: M
            MonomialMonoid of Boolean PolynomialRing in a, b, c


        .. NOTE::

            See class documentation for parameters."""
    def gen(self, Py_ssize_ti=...) -> Any:
        """BooleanMonomialMonoid.gen(self, Py_ssize_t i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1946)

        Return the `i`-th generator of ``self``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M.gen(0)
            x
            sage: M.gen(2)
            z

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: M = BooleanMonomialMonoid(P)
            sage: M.gen(50)
            x50"""
    @overload
    def gens(self) -> tuple:
        """BooleanMonomialMonoid.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1977)

        Return the tuple of generators of this monoid.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M.gens()
            (x, y, z)"""
    @overload
    def gens(self) -> Any:
        """BooleanMonomialMonoid.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1977)

        Return the tuple of generators of this monoid.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: M = BooleanMonomialMonoid(P)
            sage: M.gens()
            (x, y, z)"""
    @overload
    def ngens(self) -> Any:
        """BooleanMonomialMonoid.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1932)

        Return the number of variables in this monoid.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P = BooleanPolynomialRing(100, 'x')
            sage: M = BooleanMonomialMonoid(P)
            sage: M.ngens()
            100"""
    @overload
    def ngens(self) -> Any:
        """BooleanMonomialMonoid.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1932)

        Return the number of variables in this monoid.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P = BooleanPolynomialRing(100, 'x')
            sage: M = BooleanMonomialMonoid(P)
            sage: M.ngens()
            100"""
    def __hash__(self) -> Any:
        """BooleanMonomialMonoid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1918)

        Return a hash for this monoid.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleanMonomialMonoid
            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: M = BooleanMonomialMonoid(P)
            sage: {M:1} # indirect doctest
            {MonomialMonoid of Boolean PolynomialRing in x, y: 1}"""

class BooleanMonomialVariableIterator:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """BooleanMonomialVariableIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2822)

        Return an iterator over the variables of a boolean monomial.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + 1
            sage: for m in f: list(m)# indirect doctest
            [x, y]
            [z]
            []"""
    def __next__(self) -> Any:
        """BooleanMonomialVariableIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2837)

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + 1
            sage: m = f.lm()
            sage: next(iter(m))
            x"""

class BooleanMulAction(sage.categories.action.Action):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class BooleanPolynomial(sage.rings.polynomial.multi_polynomial.MPolynomial):
    """BooleanPolynomial(parent)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2922)

    Construct a boolean polynomial object in the given boolean
    polynomial ring.

    INPUT:

    - ``parent`` -- boolean polynomial ring

    TESTS::

        sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomial
        sage: B.<a,b,z> = BooleanPolynomialRing(3)
        sage: BooleanPolynomial(B)
        0

    .. NOTE::

        Do not use this method to construct boolean polynomials, but
        use the appropriate ``__call__`` method in the parent."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2943)"""
    @overload
    def __init__(self, B) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 2943)"""
    @overload
    def constant(self) -> Any:
        """BooleanPolynomial.constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4235)

        Return ``True`` if this element is constant.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: x.constant()
            False

        ::

            sage: B(1).constant()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def constant(self) -> Any:
        """BooleanPolynomial.constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4235)

        Return ``True`` if this element is constant.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: x.constant()
            False

        ::

            sage: B(1).constant()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def constant(self) -> Any:
        """BooleanPolynomial.constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4235)

        Return ``True`` if this element is constant.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: x.constant()
            False

        ::

            sage: B(1).constant()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def constant_coefficient(self) -> Any:
        """BooleanPolynomial.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3830)

        Return the constant coefficient of this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b> = BooleanPolynomialRing()
            sage: a.constant_coefficient()
            0
            sage: (a+1).constant_coefficient()
            1"""
    @overload
    def constant_coefficient(self) -> Any:
        """BooleanPolynomial.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3830)

        Return the constant coefficient of this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b> = BooleanPolynomialRing()
            sage: a.constant_coefficient()
            0
            sage: (a+1).constant_coefficient()
            1"""
    @overload
    def constant_coefficient(self) -> Any:
        """BooleanPolynomial.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3830)

        Return the constant coefficient of this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b> = BooleanPolynomialRing()
            sage: a.constant_coefficient()
            0
            sage: (a+1).constant_coefficient()
            1"""
    def deg(self) -> Any:
        """BooleanPolynomial.deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4101)

        Return the degree of ``self``. This is usually
        equivalent to the total degree except for weighted term orderings
        which are not implemented yet.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def degree(self, BooleanPolynomialx=...) -> Any:
        """BooleanPolynomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3284)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        If x is not specified (or is ``None``), return the total
        degree, which is the maximum degree of any monomial.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

            sage: (x*y + x + y + 1).degree(x)
            1"""
    @overload
    def degree(self) -> Any:
        """BooleanPolynomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3284)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        If x is not specified (or is ``None``), return the total
        degree, which is the maximum degree of any monomial.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

            sage: (x*y + x + y + 1).degree(x)
            1"""
    @overload
    def degree(self) -> Any:
        """BooleanPolynomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3284)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        If x is not specified (or is ``None``), return the total
        degree, which is the maximum degree of any monomial.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

            sage: (x*y + x + y + 1).degree(x)
            1"""
    @overload
    def degree(self) -> Any:
        """BooleanPolynomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3284)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        If x is not specified (or is ``None``), return the total
        degree, which is the maximum degree of any monomial.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

            sage: (x*y + x + y + 1).degree(x)
            1"""
    @overload
    def degree(self, x) -> Any:
        """BooleanPolynomial.degree(self, BooleanPolynomial x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3284)

        Return the maximal degree of this polynomial in ``x``, where
        ``x`` must be one of the generators for the parent of this
        polynomial.

        If x is not specified (or is ``None``), return the total
        degree, which is the maximum degree of any monomial.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).degree()
            1

        ::

            sage: P(1).degree()
            0

        ::

            sage: (x*y + x + y + 1).degree()
            2

            sage: (x*y + x + y + 1).degree(x)
            1"""
    @overload
    def elength(self) -> Any:
        """BooleanPolynomial.elength(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4129)

        Return elimination length as used in the SlimGB algorithm.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.elength()
            1
            sage: f = x*y + 1
            sage: f.elength()
            2

        REFERENCES:

        - Michael Brickenstein; SlimGB: Groebner Bases with Slim
          Polynomials
          http://www.mathematik.uni-kl.de/~zca/Reports_on_ca/35/paper_35_full.ps.gz

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def elength(self) -> Any:
        """BooleanPolynomial.elength(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4129)

        Return elimination length as used in the SlimGB algorithm.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.elength()
            1
            sage: f = x*y + 1
            sage: f.elength()
            2

        REFERENCES:

        - Michael Brickenstein; SlimGB: Groebner Bases with Slim
          Polynomials
          http://www.mathematik.uni-kl.de/~zca/Reports_on_ca/35/paper_35_full.ps.gz

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def elength(self) -> Any:
        """BooleanPolynomial.elength(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4129)

        Return elimination length as used in the SlimGB algorithm.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.elength()
            1
            sage: f = x*y + 1
            sage: f.elength()
            2

        REFERENCES:

        - Michael Brickenstein; SlimGB: Groebner Bases with Slim
          Polynomials
          http://www.mathematik.uni-kl.de/~zca/Reports_on_ca/35/paper_35_full.ps.gz

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def first_term(self) -> Any:
        """BooleanPolynomial.first_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4332)

        Return the first term with respect to the lexicographical term
        ordering.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3,order='lex')
            sage: f = b*z + a + 1
            sage: f.first_term()
            a

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def first_term(self) -> Any:
        """BooleanPolynomial.first_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4332)

        Return the first term with respect to the lexicographical term
        ordering.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3,order='lex')
            sage: f = b*z + a + 1
            sage: f.first_term()
            a

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    def graded_part(self, intdeg) -> Any:
        """BooleanPolynomial.graded_part(self, int deg)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4414)

        Return graded part of this boolean polynomial of degree
        ``deg``.

        INPUT:

        - ``deg`` -- a degree

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: f.graded_part(2)
            a*b + c*d

        ::

            sage: f.graded_part(0)
            1

        TESTS::

            sage: f.graded_part(-1)
            0"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleanPolynomial.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4443)

        Return ``True`` if this boolean polynomial has a
        constant part, i.e. if ``1`` is a term.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: f.has_constant_part()
            True

        ::

            sage: f = a*b*c + c*d + a*b
            sage: f.has_constant_part()
            False"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleanPolynomial.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4443)

        Return ``True`` if this boolean polynomial has a
        constant part, i.e. if ``1`` is a term.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: f.has_constant_part()
            True

        ::

            sage: f = a*b*c + c*d + a*b
            sage: f.has_constant_part()
            False"""
    @overload
    def has_constant_part(self) -> Any:
        """BooleanPolynomial.has_constant_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4443)

        Return ``True`` if this boolean polynomial has a
        constant part, i.e. if ``1`` is a term.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: f.has_constant_part()
            True

        ::

            sage: f = a*b*c + c*d + a*b
            sage: f.has_constant_part()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleanPolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3547)

        Check if ``self`` is constant.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_constant()
            True

            sage: P(0).is_constant()
            True

            sage: x.is_constant()
            False

            sage: (x*y).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleanPolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3547)

        Check if ``self`` is constant.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_constant()
            True

            sage: P(0).is_constant()
            True

            sage: x.is_constant()
            False

            sage: (x*y).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleanPolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3547)

        Check if ``self`` is constant.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_constant()
            True

            sage: P(0).is_constant()
            True

            sage: x.is_constant()
            False

            sage: (x*y).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleanPolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3547)

        Check if ``self`` is constant.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_constant()
            True

            sage: P(0).is_constant()
            True

            sage: x.is_constant()
            False

            sage: (x*y).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """BooleanPolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3547)

        Check if ``self`` is constant.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_constant()
            True

            sage: P(0).is_constant()
            True

            sage: x.is_constant()
            False

            sage: (x*y).is_constant()
            False"""
    @overload
    def is_equal(self, BooleanPolynomialright) -> Any:
        """BooleanPolynomial.is_equal(self, BooleanPolynomial right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3095)

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*z + b + 1
            sage: g = b + z
            sage: f.is_equal(g)
            False

            sage: f.is_equal((f + 1) - 1)
            True

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def is_equal(self, g) -> Any:
        """BooleanPolynomial.is_equal(self, BooleanPolynomial right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3095)

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*z + b + 1
            sage: g = b + z
            sage: f.is_equal(g)
            False

            sage: f.is_equal((f + 1) - 1)
            True

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def is_homogeneous(self) -> Any:
        """BooleanPolynomial.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4063)

        Return ``True`` if this element is a homogeneous
        polynomial.

        EXAMPLES::

            sage: P.<x, y> = BooleanPolynomialRing()
            sage: (x+y).is_homogeneous()
            True
            sage: P(0).is_homogeneous()
            True
            sage: (x+1).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """BooleanPolynomial.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4063)

        Return ``True`` if this element is a homogeneous
        polynomial.

        EXAMPLES::

            sage: P.<x, y> = BooleanPolynomialRing()
            sage: (x+y).is_homogeneous()
            True
            sage: P(0).is_homogeneous()
            True
            sage: (x+1).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """BooleanPolynomial.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4063)

        Return ``True`` if this element is a homogeneous
        polynomial.

        EXAMPLES::

            sage: P.<x, y> = BooleanPolynomialRing()
            sage: (x+y).is_homogeneous()
            True
            sage: P(0).is_homogeneous()
            True
            sage: (x+1).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """BooleanPolynomial.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4063)

        Return ``True`` if this element is a homogeneous
        polynomial.

        EXAMPLES::

            sage: P.<x, y> = BooleanPolynomialRing()
            sage: (x+y).is_homogeneous()
            True
            sage: P(0).is_homogeneous()
            True
            sage: (x+1).is_homogeneous()
            False"""
    @overload
    def is_one(self) -> Any:
        """BooleanPolynomial.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3508)

        Check if ``self`` is 1.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_one()
            True

            sage: P.one().is_one()
            True

            sage: x.is_one()
            False

            sage: P(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """BooleanPolynomial.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3508)

        Check if ``self`` is 1.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_one()
            True

            sage: P.one().is_one()
            True

            sage: x.is_one()
            False

            sage: P(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """BooleanPolynomial.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3508)

        Check if ``self`` is 1.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_one()
            True

            sage: P.one().is_one()
            True

            sage: x.is_one()
            False

            sage: P(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """BooleanPolynomial.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3508)

        Check if ``self`` is 1.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_one()
            True

            sage: P.one().is_one()
            True

            sage: x.is_one()
            False

            sage: P(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """BooleanPolynomial.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3508)

        Check if ``self`` is 1.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(1).is_one()
            True

            sage: P.one().is_one()
            True

            sage: x.is_one()
            False

            sage: P(0).is_one()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_pair(self) -> Any:
        """BooleanPolynomial.is_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3436)

        Check if ``self`` has exactly two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_pair()
            False

            sage: x.is_pair()
            False

            sage: P(1).is_pair()
            False

            sage: (x*y).is_pair()
            False

            sage: (x + y).is_pair()
            True

            sage: (x + 1).is_pair()
            True

            sage: (x*y + 1).is_pair()
            True

            sage: (x + y + 1).is_pair()
            False

            sage: ((x + 1)*(y + 1)).is_pair()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton(self) -> Any:
        """BooleanPolynomial.is_singleton(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3364)

        Check if ``self`` has at most one term.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton()
            True

            sage: x.is_singleton()
            True

            sage: P(1).is_singleton()
            True

            sage: (x*y).is_singleton()
            True

            sage: (x + y).is_singleton()
            False

            sage: (x + 1).is_singleton()
            False

            sage: (x*y + 1).is_singleton()
            False

            sage: (x + y + 1).is_singleton()
            False

            sage: ((x + 1)*(y + 1)).is_singleton()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_singleton_or_pair(self) -> Any:
        """BooleanPolynomial.is_singleton_or_pair(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3400)

        Check if ``self`` has at most two terms.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_singleton_or_pair()
            True

            sage: x.is_singleton_or_pair()
            True

            sage: P(1).is_singleton_or_pair()
            True

            sage: (x*y).is_singleton_or_pair()
            True

            sage: (x + y).is_singleton_or_pair()
            True

            sage: (x + 1).is_singleton_or_pair()
            True

            sage: (x*y + 1).is_singleton_or_pair()
            True

            sage: (x + y + 1).is_singleton_or_pair()
            False

            sage: ((x + 1)*(y + 1)).is_singleton_or_pair()
            False"""
    @overload
    def is_unit(self) -> Any:
        """BooleanPolynomial.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3529)

        Check if ``self`` is invertible in the parent ring.

        Note that this condition is equivalent to being 1 for boolean
        polynomials.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.one().is_unit()
            True

            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """BooleanPolynomial.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3529)

        Check if ``self`` is invertible in the parent ring.

        Note that this condition is equivalent to being 1 for boolean
        polynomials.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.one().is_unit()
            True

            sage: x.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """BooleanPolynomial.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3529)

        Check if ``self`` is invertible in the parent ring.

        Note that this condition is equivalent to being 1 for boolean
        polynomials.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.one().is_unit()
            True

            sage: x.is_unit()
            False"""
    @overload
    def is_univariate(self) -> Any:
        """BooleanPolynomial.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3667)

        Return ``True`` if ``self`` is a univariate polynomial.

        This means that ``self`` contains at most one variable.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing()
            sage: f = x + 1
            sage: f.is_univariate()
            True
            sage: f = y*x + 1
            sage: f.is_univariate()
            False
            sage: f = P(0)
            sage: f.is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """BooleanPolynomial.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3667)

        Return ``True`` if ``self`` is a univariate polynomial.

        This means that ``self`` contains at most one variable.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing()
            sage: f = x + 1
            sage: f.is_univariate()
            True
            sage: f = y*x + 1
            sage: f.is_univariate()
            False
            sage: f = P(0)
            sage: f.is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """BooleanPolynomial.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3667)

        Return ``True`` if ``self`` is a univariate polynomial.

        This means that ``self`` contains at most one variable.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing()
            sage: f = x + 1
            sage: f.is_univariate()
            True
            sage: f = y*x + 1
            sage: f.is_univariate()
            False
            sage: f = P(0)
            sage: f.is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """BooleanPolynomial.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3667)

        Return ``True`` if ``self`` is a univariate polynomial.

        This means that ``self`` contains at most one variable.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing()
            sage: f = x + 1
            sage: f.is_univariate()
            True
            sage: f = y*x + 1
            sage: f.is_univariate()
            False
            sage: f = P(0)
            sage: f.is_univariate()
            True"""
    @overload
    def is_zero(self) -> Any:
        """BooleanPolynomial.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3472)

        Check if ``self`` is zero.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_zero()
            True

            sage: x.is_zero()
            False

            sage: P(1).is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """BooleanPolynomial.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3472)

        Check if ``self`` is zero.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_zero()
            True

            sage: x.is_zero()
            False

            sage: P(1).is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """BooleanPolynomial.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3472)

        Check if ``self`` is zero.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_zero()
            True

            sage: x.is_zero()
            False

            sage: P(1).is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """BooleanPolynomial.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3472)

        Check if ``self`` is zero.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P(0).is_zero()
            True

            sage: x.is_zero()
            False

            sage: P(1).is_zero()
            False"""
    @overload
    def lead(self) -> Any:
        """BooleanPolynomial.lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4154)

        Return the leading monomial of boolean polynomial, with respect to
        to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lead()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lead()
            y*z

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead(self) -> Any:
        """BooleanPolynomial.lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4154)

        Return the leading monomial of boolean polynomial, with respect to
        to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lead()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lead()
            y*z

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead(self) -> Any:
        """BooleanPolynomial.lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4154)

        Return the leading monomial of boolean polynomial, with respect to
        to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lead()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lead()
            y*z

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_deg(self) -> Any:
        """BooleanPolynomial.lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3568)

        Return the total degree of the leading monomial of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + y*z
            sage: p.lead_deg()
            1

            sage: P.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: p = x + y*z
            sage: p.lead_deg()
            2

            sage: P(0).lead_deg()
            0

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_deg(self) -> Any:
        """BooleanPolynomial.lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3568)

        Return the total degree of the leading monomial of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + y*z
            sage: p.lead_deg()
            1

            sage: P.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: p = x + y*z
            sage: p.lead_deg()
            2

            sage: P(0).lead_deg()
            0

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_deg(self) -> Any:
        """BooleanPolynomial.lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3568)

        Return the total degree of the leading monomial of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + y*z
            sage: p.lead_deg()
            1

            sage: P.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: p = x + y*z
            sage: p.lead_deg()
            2

            sage: P(0).lead_deg()
            0

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_deg(self) -> Any:
        """BooleanPolynomial.lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3568)

        Return the total degree of the leading monomial of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + y*z
            sage: p.lead_deg()
            1

            sage: P.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: p = x + y*z
            sage: p.lead_deg()
            2

            sage: P(0).lead_deg()
            0

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_divisors(self) -> Any:
        """BooleanPolynomial.lead_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4314)

        Return a ``BooleSet`` of all divisors of the leading
        monomial.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*b + z + 1
            sage: f.lead_divisors()
            {{a,b}, {a}, {b}, {}}

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lead_divisors(self) -> Any:
        """BooleanPolynomial.lead_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4314)

        Return a ``BooleSet`` of all divisors of the leading
        monomial.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*b + z + 1
            sage: f.lead_divisors()
            {{a,b}, {a}, {b}, {}}

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead(self) -> Any:
        """BooleanPolynomial.lex_lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4178)

        Return the leading monomial of boolean polynomial, with respect to
        the lexicographical term ordering.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lex_lead()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lex_lead()
            x

            sage: P(0).lex_lead()
            0

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead(self) -> Any:
        """BooleanPolynomial.lex_lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4178)

        Return the leading monomial of boolean polynomial, with respect to
        the lexicographical term ordering.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lex_lead()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lex_lead()
            x

            sage: P(0).lex_lead()
            0

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead(self) -> Any:
        """BooleanPolynomial.lex_lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4178)

        Return the leading monomial of boolean polynomial, with respect to
        the lexicographical term ordering.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lex_lead()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lex_lead()
            x

            sage: P(0).lex_lead()
            0

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead(self) -> Any:
        """BooleanPolynomial.lex_lead(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4178)

        Return the leading monomial of boolean polynomial, with respect to
        the lexicographical term ordering.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lex_lead()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lex_lead()
            x

            sage: P(0).lex_lead()
            0

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead_deg(self) -> Any:
        """BooleanPolynomial.lex_lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4206)

        Return degree of leading monomial with respect to the
        lexicographical ordering.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='lex')
            sage: f = x + y*z
            sage: f
            x + y*z
            sage: f.lex_lead_deg()
            1

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: f = x + y*z
            sage: f
            y*z + x
            sage: f.lex_lead_deg()
            1

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead_deg(self) -> Any:
        """BooleanPolynomial.lex_lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4206)

        Return degree of leading monomial with respect to the
        lexicographical ordering.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='lex')
            sage: f = x + y*z
            sage: f
            x + y*z
            sage: f.lex_lead_deg()
            1

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: f = x + y*z
            sage: f
            y*z + x
            sage: f.lex_lead_deg()
            1

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lex_lead_deg(self) -> Any:
        """BooleanPolynomial.lex_lead_deg(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4206)

        Return degree of leading monomial with respect to the
        lexicographical ordering.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='lex')
            sage: f = x + y*z
            sage: f
            x + y*z
            sage: f.lex_lead_deg()
            1

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: f = x + y*z
            sage: f
            y*z + x
            sage: f.lex_lead_deg()
            1

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def lm(self) -> Any:
        """BooleanPolynomial.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3319)

        Return the leading monomial of this boolean polynomial, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lm()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lm()
            y*z

            sage: P(0).lm()
            0"""
    @overload
    def lm(self) -> Any:
        """BooleanPolynomial.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3319)

        Return the leading monomial of this boolean polynomial, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lm()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lm()
            y*z

            sage: P(0).lm()
            0"""
    @overload
    def lm(self) -> Any:
        """BooleanPolynomial.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3319)

        Return the leading monomial of this boolean polynomial, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lm()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lm()
            y*z

            sage: P(0).lm()
            0"""
    @overload
    def lm(self) -> Any:
        """BooleanPolynomial.lm(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3319)

        Return the leading monomial of this boolean polynomial, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lm()
            x

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lm()
            y*z

            sage: P(0).lm()
            0"""
    @overload
    def lt(self) -> Any:
        """BooleanPolynomial.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3342)

        Return the leading term of this boolean polynomial, with respect to
        the order of the parent ring.

        Note that for boolean polynomials this is equivalent to returning
        leading monomials.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lt()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lt()
            y*z"""
    @overload
    def lt(self) -> Any:
        """BooleanPolynomial.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3342)

        Return the leading term of this boolean polynomial, with respect to
        the order of the parent ring.

        Note that for boolean polynomials this is equivalent to returning
        leading monomials.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lt()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lt()
            y*z"""
    @overload
    def lt(self) -> Any:
        """BooleanPolynomial.lt(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3342)

        Return the leading term of this boolean polynomial, with respect to
        the order of the parent ring.

        Note that for boolean polynomials this is equivalent to returning
        leading monomials.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x+y+y*z).lt()
            x

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: (x+y+y*z).lt()
            y*z"""
    @overload
    def map_every_x_to_x_plus_one(self) -> Any:
        """BooleanPolynomial.map_every_x_to_x_plus_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4297)

        Map every variable ``x_i`` in this polynomial to ``x_i + 1``.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*b + z + 1; f
            a*b + z + 1
            sage: f.map_every_x_to_x_plus_one()
            a*b + a + b + z + 1
            sage: f(a+1,b+1,z+1)
            a*b + a + b + z + 1"""
    @overload
    def map_every_x_to_x_plus_one(self) -> Any:
        """BooleanPolynomial.map_every_x_to_x_plus_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4297)

        Map every variable ``x_i`` in this polynomial to ``x_i + 1``.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*b + z + 1; f
            a*b + z + 1
            sage: f.map_every_x_to_x_plus_one()
            a*b + a + b + z + 1
            sage: f(a+1,b+1,z+1)
            a*b + a + b + z + 1"""
    @overload
    def monomial_coefficient(self, mon) -> Any:
        """BooleanPolynomial.monomial_coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3791)

        Return the coefficient of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same
        parent as ``self``.

        INPUT:

        - ``mon`` -- a monomial

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.monomial_coefficient(x)
            1
            sage: x.monomial_coefficient(y)
            0
            sage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)
            sage: f=(1-x)*(1+y); f
            x*y + x + y + 1

        ::

            sage: f.monomial_coefficient(1)
            1

        ::

            sage: f.monomial_coefficient(0)
            0"""
    @overload
    def monomial_coefficient(self, x) -> Any:
        """BooleanPolynomial.monomial_coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3791)

        Return the coefficient of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same
        parent as ``self``.

        INPUT:

        - ``mon`` -- a monomial

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.monomial_coefficient(x)
            1
            sage: x.monomial_coefficient(y)
            0
            sage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)
            sage: f=(1-x)*(1+y); f
            x*y + x + y + 1

        ::

            sage: f.monomial_coefficient(1)
            1

        ::

            sage: f.monomial_coefficient(0)
            0"""
    @overload
    def monomial_coefficient(self, y) -> Any:
        """BooleanPolynomial.monomial_coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3791)

        Return the coefficient of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same
        parent as ``self``.

        INPUT:

        - ``mon`` -- a monomial

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: x.monomial_coefficient(x)
            1
            sage: x.monomial_coefficient(y)
            0
            sage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)
            sage: f=(1-x)*(1+y); f
            x*y + x + y + 1

        ::

            sage: f.monomial_coefficient(1)
            1

        ::

            sage: f.monomial_coefficient(0)
            0"""
    @overload
    def monomials(self) -> Any:
        """BooleanPolynomial.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3735)

        Return a list of monomials appearing in ``self``
        ordered largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.monomials()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.monomials()
            [b*c, a]
            sage: P.zero().monomials()
            []"""
    @overload
    def monomials(self) -> Any:
        """BooleanPolynomial.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3735)

        Return a list of monomials appearing in ``self``
        ordered largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.monomials()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.monomials()
            [b*c, a]
            sage: P.zero().monomials()
            []"""
    @overload
    def monomials(self) -> Any:
        """BooleanPolynomial.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3735)

        Return a list of monomials appearing in ``self``
        ordered largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.monomials()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.monomials()
            [b*c, a]
            sage: P.zero().monomials()
            []"""
    @overload
    def monomials(self) -> Any:
        """BooleanPolynomial.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3735)

        Return a list of monomials appearing in ``self``
        ordered largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.monomials()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.monomials()
            [b*c, a]
            sage: P.zero().monomials()
            []"""
    @overload
    def n_nodes(self) -> Any:
        """BooleanPolynomial.n_nodes(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4377)

        Return the number of nodes in the ZDD implementing this
        polynomial.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2 + x2*x3 + 1
            sage: f.n_nodes()
            4

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def n_nodes(self) -> Any:
        """BooleanPolynomial.n_nodes(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4377)

        Return the number of nodes in the ZDD implementing this
        polynomial.

        EXAMPLES::

            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2 + x2*x3 + 1
            sage: f.n_nodes()
            4

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def n_vars(self) -> Any:
        """BooleanPolynomial.n_vars(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4396)

        Return the number of variables used to form this boolean
        polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + 1
            sage: f.n_vars()
            3

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def n_vars(self) -> Any:
        """BooleanPolynomial.n_vars(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4396)

        Return the number of variables used to form this boolean
        polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + 1
            sage: f.n_vars()
            3

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def navigation(self) -> Any:
        """BooleanPolynomial.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4256)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1

            sage: nav = f.navigation()
            sage: BooleSet(nav, B)
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav.value()
            1

            sage: nav_else = nav.else_branch()

            sage: BooleSet(nav_else, B)
            {{x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav_else.value()
            2

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def navigation(self) -> Any:
        """BooleanPolynomial.navigation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4256)

        Navigators provide an interface to diagram nodes, accessing
        their index as well as the corresponding then- and
        else-branches.

        You should be very careful and always keep a reference to the
        original object, when dealing with navigators, as navigators
        contain only a raw pointer as data. For the same reason, it is
        necessary to supply the ring as argument, when constructing a
        set out of a navigator.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import BooleSet
            sage: B = BooleanPolynomialRing(5,'x')
            sage: x0,x1,x2,x3,x4 = B.gens()
            sage: f = x1*x2+x2*x3*x4+x2*x4+x3+x4+1

            sage: nav = f.navigation()
            sage: BooleSet(nav, B)
            {{x1,x2}, {x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav.value()
            1

            sage: nav_else = nav.else_branch()

            sage: BooleSet(nav_else, B)
            {{x2,x3,x4}, {x2,x4}, {x3}, {x4}, {}}

            sage: nav_else.value()
            2

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def nvariables(self) -> Any:
        """BooleanPolynomial.nvariables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3654)

        Return the number of variables used to form this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + 1
            sage: f.nvariables()
            3"""
    @overload
    def nvariables(self) -> Any:
        """BooleanPolynomial.nvariables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3654)

        Return the number of variables used to form this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + 1
            sage: f.nvariables()
            3"""
    @overload
    def reduce(self, I) -> Any:
        """BooleanPolynomial.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4575)

        Return the normal form of ``self`` w.r.t.  ``I``, i.e. return
        the remainder of ``self`` with respect to the polynomials in
        ``I``. If the polynomial set/list ``I`` is not a Groebner
        basis the result is not canonical.

        INPUT:

        - ``I`` -- list/set of polynomials in ``self.parent()``; if I is an
          ideal, the generators are used

        EXAMPLES::

            sage: B.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: I = B.ideal((x0 + x1 + x2 + x3,
            ....:              x0*x1 + x1*x2 + x0*x3 + x2*x3,
            ....:              x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            ....:              x0*x1*x2*x3 + 1))
            sage: gb = I.groebner_basis()
            sage: f,g,h,i = I.gens()
            sage: f.reduce(gb)
            0
            sage: p = f*g + x0*h + x2*i
            sage: p.reduce(gb)
            0
            sage: p.reduce(I)
            x1*x2*x3 + x2
            sage: p.reduce([])
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        .. NOTE::

           If this function is called repeatedly with the same I then
           it is advised to use PolyBoRi's :class:`GroebnerStrategy`
           object directly, since that will be faster. See the source
           code of this function for details.

        TESTS::

            sage: R=BooleanPolynomialRing(20,'x','lex')
            sage: a=R.random_element()
            sage: a.reduce([None,None])
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def reduce(self, gb) -> Any:
        """BooleanPolynomial.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4575)

        Return the normal form of ``self`` w.r.t.  ``I``, i.e. return
        the remainder of ``self`` with respect to the polynomials in
        ``I``. If the polynomial set/list ``I`` is not a Groebner
        basis the result is not canonical.

        INPUT:

        - ``I`` -- list/set of polynomials in ``self.parent()``; if I is an
          ideal, the generators are used

        EXAMPLES::

            sage: B.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: I = B.ideal((x0 + x1 + x2 + x3,
            ....:              x0*x1 + x1*x2 + x0*x3 + x2*x3,
            ....:              x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            ....:              x0*x1*x2*x3 + 1))
            sage: gb = I.groebner_basis()
            sage: f,g,h,i = I.gens()
            sage: f.reduce(gb)
            0
            sage: p = f*g + x0*h + x2*i
            sage: p.reduce(gb)
            0
            sage: p.reduce(I)
            x1*x2*x3 + x2
            sage: p.reduce([])
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        .. NOTE::

           If this function is called repeatedly with the same I then
           it is advised to use PolyBoRi's :class:`GroebnerStrategy`
           object directly, since that will be faster. See the source
           code of this function for details.

        TESTS::

            sage: R=BooleanPolynomialRing(20,'x','lex')
            sage: a=R.random_element()
            sage: a.reduce([None,None])
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def reduce(self, gb) -> Any:
        """BooleanPolynomial.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4575)

        Return the normal form of ``self`` w.r.t.  ``I``, i.e. return
        the remainder of ``self`` with respect to the polynomials in
        ``I``. If the polynomial set/list ``I`` is not a Groebner
        basis the result is not canonical.

        INPUT:

        - ``I`` -- list/set of polynomials in ``self.parent()``; if I is an
          ideal, the generators are used

        EXAMPLES::

            sage: B.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: I = B.ideal((x0 + x1 + x2 + x3,
            ....:              x0*x1 + x1*x2 + x0*x3 + x2*x3,
            ....:              x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            ....:              x0*x1*x2*x3 + 1))
            sage: gb = I.groebner_basis()
            sage: f,g,h,i = I.gens()
            sage: f.reduce(gb)
            0
            sage: p = f*g + x0*h + x2*i
            sage: p.reduce(gb)
            0
            sage: p.reduce(I)
            x1*x2*x3 + x2
            sage: p.reduce([])
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        .. NOTE::

           If this function is called repeatedly with the same I then
           it is advised to use PolyBoRi's :class:`GroebnerStrategy`
           object directly, since that will be faster. See the source
           code of this function for details.

        TESTS::

            sage: R=BooleanPolynomialRing(20,'x','lex')
            sage: a=R.random_element()
            sage: a.reduce([None,None])
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def reduce(self, I) -> Any:
        """BooleanPolynomial.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4575)

        Return the normal form of ``self`` w.r.t.  ``I``, i.e. return
        the remainder of ``self`` with respect to the polynomials in
        ``I``. If the polynomial set/list ``I`` is not a Groebner
        basis the result is not canonical.

        INPUT:

        - ``I`` -- list/set of polynomials in ``self.parent()``; if I is an
          ideal, the generators are used

        EXAMPLES::

            sage: B.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: I = B.ideal((x0 + x1 + x2 + x3,
            ....:              x0*x1 + x1*x2 + x0*x3 + x2*x3,
            ....:              x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            ....:              x0*x1*x2*x3 + 1))
            sage: gb = I.groebner_basis()
            sage: f,g,h,i = I.gens()
            sage: f.reduce(gb)
            0
            sage: p = f*g + x0*h + x2*i
            sage: p.reduce(gb)
            0
            sage: p.reduce(I)
            x1*x2*x3 + x2
            sage: p.reduce([])
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        .. NOTE::

           If this function is called repeatedly with the same I then
           it is advised to use PolyBoRi's :class:`GroebnerStrategy`
           object directly, since that will be faster. See the source
           code of this function for details.

        TESTS::

            sage: R=BooleanPolynomialRing(20,'x','lex')
            sage: a=R.random_element()
            sage: a.reduce([None,None])
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def reducible_by(self, BooleanPolynomialrhs) -> Any:
        """BooleanPolynomial.reducible_by(self, BooleanPolynomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4351)

        Return ``True`` if this boolean polynomial is reducible
        by the polynomial ``rhs``.

        INPUT:

        - ``rhs`` -- boolean polynomial

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4,order='deglex')
            sage: f = (a*b + 1)*(c + 1)
            sage: f.reducible_by(d)
            False
            sage: f.reducible_by(c)
            True
            sage: f.reducible_by(c + 1)
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def reducible_by(self, d) -> Any:
        """BooleanPolynomial.reducible_by(self, BooleanPolynomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4351)

        Return ``True`` if this boolean polynomial is reducible
        by the polynomial ``rhs``.

        INPUT:

        - ``rhs`` -- boolean polynomial

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4,order='deglex')
            sage: f = (a*b + 1)*(c + 1)
            sage: f.reducible_by(d)
            False
            sage: f.reducible_by(c)
            True
            sage: f.reducible_by(c + 1)
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def reducible_by(self, c) -> Any:
        """BooleanPolynomial.reducible_by(self, BooleanPolynomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4351)

        Return ``True`` if this boolean polynomial is reducible
        by the polynomial ``rhs``.

        INPUT:

        - ``rhs`` -- boolean polynomial

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4,order='deglex')
            sage: f = (a*b + 1)*(c + 1)
            sage: f.reducible_by(d)
            False
            sage: f.reducible_by(c)
            True
            sage: f.reducible_by(c + 1)
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def ring(self) -> Any:
        """BooleanPolynomial.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4563)

        Return the parent of this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: a.ring() is B
            True"""
    @overload
    def ring(self) -> Any:
        """BooleanPolynomial.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4563)

        Return the parent of this boolean polynomial.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: a.ring() is B
            True"""
    @overload
    def set(self) -> Any:
        """BooleanPolynomial.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4088)

        Return a ``BooleSet`` with all monomials appearing in
        this polynomial.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: (a*b+z+1).set()
            {{a,b}, {z}, {}}"""
    @overload
    def set(self) -> Any:
        """BooleanPolynomial.set(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4088)

        Return a ``BooleSet`` with all monomials appearing in
        this polynomial.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: (a*b+z+1).set()
            {{a,b}, {z}, {}}"""
    @overload
    def spoly(self, BooleanPolynomialrhs) -> Any:
        """BooleanPolynomial.spoly(self, BooleanPolynomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4524)

        Return the S-Polynomial of this boolean polynomial and the other
        boolean polynomial ``rhs``.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: g = c*d + b
            sage: f.spoly(g)
            a*b + a*c*d + c*d + 1

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def spoly(self, g) -> Any:
        """BooleanPolynomial.spoly(self, BooleanPolynomial rhs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4524)

        Return the S-Polynomial of this boolean polynomial and the other
        boolean polynomial ``rhs``.

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b*c + c*d + a*b + 1
            sage: g = c*d + b
            sage: f.spoly(g)
            a*b + a*c*d + c*d + 1

        .. NOTE::

           This function is part of the upstream PolyBoRi interface."""
    @overload
    def stable_hash(self) -> Any:
        """BooleanPolynomial.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4544)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x is B.gen(0)
            False
            sage: x.stable_hash() == B.gen(0).stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    @overload
    def stable_hash(self) -> Any:
        """BooleanPolynomial.stable_hash(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4544)

        A hash value which is stable across processes.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing()
            sage: x is B.gen(0)
            False
            sage: x.stable_hash() == B.gen(0).stable_hash()
            True

        .. NOTE::

           This function is part of the upstream PolyBoRi
           interface. In Sage all hashes are stable."""
    @overload
    def subs(self, in_dict=..., **kwds) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, x=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, x=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, x=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, y=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, y=..., z=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, z=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def subs(self, x=..., y=..., z=...) -> Any:
        """BooleanPolynomial.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3949)

        Fixes some given variables in a given boolean polynomial and
        returns the changed boolean polynomials. The polynomial itself is
        not affected. The variable, value pairs for fixing are to be
        provided as dictionary of the form {variable:value} or named
        parameters (see examples below).

        INPUT:

        - ``in_dict`` -- (optional) dict with variable:value pairs

        - ``**kwds`` -- names parameters

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + y*z + 1
            sage: f.subs(x=1)
            y*z + y + z + 1
            sage: f.subs(x=0)
            y*z + z + 1

        ::

            sage: f.subs(x=y)
            y*z + y + z + 1

        ::

            sage: f.subs({x:1},y=1)
            0
            sage: f.subs(y=1)
            x + 1
            sage: f.subs(y=1,z=1)
            x + 1
            sage: f.subs(z=1)
            x*y + y
            sage: f.subs({'x':1},y=1)
            0

        This method can work fully symbolic::

            sage: f.subs(x=var('a'), y=var('b'), z=var('c'))                            # needs sage.symbolic
            a*b + b*c + c + 1
            sage: f.subs({'x': var('a'), 'y': var('b'), 'z': var('c')})                 # needs sage.symbolic
            a*b + b*c + c + 1"""
    @overload
    def terms(self) -> Any:
        """BooleanPolynomial.terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3772)

        Return a list of monomials appearing in ``self`` ordered
        largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.terms()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.terms()
            [b*c, a]"""
    @overload
    def terms(self) -> Any:
        """BooleanPolynomial.terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3772)

        Return a list of monomials appearing in ``self`` ordered
        largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.terms()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.terms()
            [b*c, a]"""
    @overload
    def terms(self) -> Any:
        """BooleanPolynomial.terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3772)

        Return a list of monomials appearing in ``self`` ordered
        largest to smallest.

        EXAMPLES::

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='lex')
            sage: f = a + c*b
            sage: f.terms()
            [a, b*c]

            sage: P.<a,b,c> = BooleanPolynomialRing(3,order='deglex')
            sage: f = a + c*b
            sage: f.terms()
            [b*c, a]"""
    @overload
    def total_degree(self) -> Any:
        """BooleanPolynomial.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3262)

        Return the total degree of ``self``.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).total_degree()
            1

        ::

            sage: P(1).total_degree()
            0

        ::

            sage: (x*y + x + y + 1).total_degree()
            2"""
    @overload
    def total_degree(self) -> Any:
        """BooleanPolynomial.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3262)

        Return the total degree of ``self``.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).total_degree()
            1

        ::

            sage: P(1).total_degree()
            0

        ::

            sage: (x*y + x + y + 1).total_degree()
            2"""
    @overload
    def total_degree(self) -> Any:
        """BooleanPolynomial.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3262)

        Return the total degree of ``self``.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).total_degree()
            1

        ::

            sage: P(1).total_degree()
            0

        ::

            sage: (x*y + x + y + 1).total_degree()
            2"""
    @overload
    def total_degree(self) -> Any:
        """BooleanPolynomial.total_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3262)

        Return the total degree of ``self``.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: (x+y).total_degree()
            1

        ::

            sage: P(1).total_degree()
            0

        ::

            sage: (x*y + x + y + 1).total_degree()
            2"""
    @overload
    def univariate_polynomial(self, R=...) -> Any:
        """BooleanPolynomial.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3688)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  This is checked using the
        :meth:`is_univariate()` method.  The new Polynomial is over
        GF(2)  and in the variable ``x`` if no ring ``R`` is provided.

            sage: R.<x, y> = BooleanPolynomialRing()
            sage: f = x - y + x*y + 1
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must involve at most one variable
            sage: g = f.subs({x:0}); g
            y + 1
            sage: g.univariate_polynomial ()
            y + 1
            sage: g.univariate_polynomial(GF(2)['foo'])
            foo + 1

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()                                                            # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Finite Field of size 2 (using GF2X)"""
    @overload
    def univariate_polynomial(self) -> Any:
        """BooleanPolynomial.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3688)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  This is checked using the
        :meth:`is_univariate()` method.  The new Polynomial is over
        GF(2)  and in the variable ``x`` if no ring ``R`` is provided.

            sage: R.<x, y> = BooleanPolynomialRing()
            sage: f = x - y + x*y + 1
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must involve at most one variable
            sage: g = f.subs({x:0}); g
            y + 1
            sage: g.univariate_polynomial ()
            y + 1
            sage: g.univariate_polynomial(GF(2)['foo'])
            foo + 1

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()                                                            # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Finite Field of size 2 (using GF2X)"""
    @overload
    def univariate_polynomial(self) -> Any:
        """BooleanPolynomial.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3688)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  This is checked using the
        :meth:`is_univariate()` method.  The new Polynomial is over
        GF(2)  and in the variable ``x`` if no ring ``R`` is provided.

            sage: R.<x, y> = BooleanPolynomialRing()
            sage: f = x - y + x*y + 1
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must involve at most one variable
            sage: g = f.subs({x:0}); g
            y + 1
            sage: g.univariate_polynomial ()
            y + 1
            sage: g.univariate_polynomial(GF(2)['foo'])
            foo + 1

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()                                                            # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Finite Field of size 2 (using GF2X)"""
    def variable(self, i=...) -> Any:
        """BooleanPolynomial.variable(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3756)

        Return the i-th variable occurring in ``self``. The index i is the
        index in ``self.variables()``

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*z + z + 1
            sage: f.variables()
            (x, z)
            sage: f.variable(1)
            z"""
    @overload
    def variables(self) -> Any:
        """BooleanPolynomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3629)

        Return a tuple of all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).variables()
            (x, y)

            sage: (x*y + z).variables()
            (x, y, z)

            sage: P.zero().variables()
            ()

            sage: P.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleanPolynomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3629)

        Return a tuple of all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).variables()
            (x, y)

            sage: (x*y + z).variables()
            (x, y, z)

            sage: P.zero().variables()
            ()

            sage: P.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleanPolynomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3629)

        Return a tuple of all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).variables()
            (x, y)

            sage: (x*y + z).variables()
            (x, y, z)

            sage: P.zero().variables()
            ()

            sage: P.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleanPolynomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3629)

        Return a tuple of all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).variables()
            (x, y)

            sage: (x*y + z).variables()
            (x, y, z)

            sage: P.zero().variables()
            ()

            sage: P.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """BooleanPolynomial.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3629)

        Return a tuple of all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).variables()
            (x, y)

            sage: (x*y + z).variables()
            (x, y, z)

            sage: P.zero().variables()
            ()

            sage: P.one().variables()
            ()"""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def vars_as_monomial(self) -> Any:
        """BooleanPolynomial.vars_as_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3595)

        Return a boolean monomial with all variables appearing in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: (x + y).vars_as_monomial()
            x*y

            sage: (x*y + z).vars_as_monomial()
            x*y*z

            sage: P.zero().vars_as_monomial()
            1

            sage: P.one().vars_as_monomial()
            1

        TESTS::

            sage: R = BooleanPolynomialRing(1, 'y')
            sage: y.vars_as_monomial()
            y
            sage: R
            Boolean PolynomialRing in y

        .. NOTE::

            This function is part of the upstream PolyBoRi interface."""
    @overload
    def zeros_in(self, s) -> Any:
        """BooleanPolynomial.zeros_in(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4463)

        Return a set containing all elements of ``s`` where
        this boolean polynomial evaluates to zero.

        If ``s`` is given as a ``BooleSet``, then
        the return type is also a ``BooleSet``. If
        ``s`` is a set/list/tuple of tuple this function
        returns a tuple of tuples.

        INPUT:

        - ``s`` -- candidate points for evaluation to zero

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b + c + d + 1

        Now we create a set of points::

            sage: s = a*b + a*b*c + c*d + 1
            sage: s = s.set(); s
            {{a,b,c}, {a,b}, {c,d}, {}}

        This encodes the points (1,1,1,0), (1,1,0,0), (0,0,1,1) and
        (0,0,0,0). But of these only (1,1,0,0) evaluates to zero.

        ::

            sage: f.zeros_in(s)
            {{a,b}}

        ::

            sage: f.zeros_in([(1,1,1,0), (1,1,0,0), (0,0,1,1), (0,0,0,0)])
            ((1, 1, 0, 0),)"""
    @overload
    def zeros_in(self, s) -> Any:
        """BooleanPolynomial.zeros_in(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4463)

        Return a set containing all elements of ``s`` where
        this boolean polynomial evaluates to zero.

        If ``s`` is given as a ``BooleSet``, then
        the return type is also a ``BooleSet``. If
        ``s`` is a set/list/tuple of tuple this function
        returns a tuple of tuples.

        INPUT:

        - ``s`` -- candidate points for evaluation to zero

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing(4)
            sage: f = a*b + c + d + 1

        Now we create a set of points::

            sage: s = a*b + a*b*c + c*d + 1
            sage: s = s.set(); s
            {{a,b,c}, {a,b}, {c,d}, {}}

        This encodes the points (1,1,1,0), (1,1,0,0), (0,0,1,1) and
        (0,0,0,0). But of these only (1,1,0,0) evaluates to zero.

        ::

            sage: f.zeros_in(s)
            {{a,b}}

        ::

            sage: f.zeros_in([(1,1,1,0), (1,1,0,0), (0,0,1,1), (0,0,0,0)])
            ((1, 1, 0, 0),)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args, **kwds) -> Any:
        """BooleanPolynomial.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3887)

        Evaluate this boolean polynomials.

        EXAMPLES::

            sage: B.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = x*y + z + 1
            sage: f(0,1,1)
            0
            sage: f(z,y,x)
            x + y*z + 1
            sage: f(x=z)
            y*z + z + 1

        ::

            sage: P.<a,b,c> = PolynomialRing(QQ)
            sage: f(a,b,c)
            a*b + c + 1
            sage: f(x=a,y=b,z=1)
            a*b + 2

        Evaluation of polynomials can be used fully symbolic::

            sage: f(x=var('a'), y=var('b'), z=var('c'))                                 # needs sage.symbolic
            a*b + c + 1
            sage: f(var('a'), var('b'), 1)                                              # needs sage.symbolic
            a*b"""
    def __hash__(self) -> Any:
        """BooleanPolynomial.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3848)

        Return hash for ``self``.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: {x:1} # indirect doctest
            {x: 1}"""
    def __iter__(self) -> Any:
        """BooleanPolynomial.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3163)

        Return an iterator over the monomials of ``self``, in
        the order of the parent ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + z + x*y + y*z + x*y*z
            sage: list(iter(p))
            [x*y*z, x*y, x, y*z, z]

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: p = x + z + x*y + y*z + x*y*z
            sage: list(iter(p))
            [x*y*z, x*y, y*z, x, z]

        ::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: p = x + z + x*y + y*z + x*y*z
            sage: list(iter(p))
            [x*y*z, x*y, y*z, x, z]

        TESTS::

            sage: R = BooleanPolynomialRing(1,'y')
            sage: list(iter(y))
            [y]
            sage: R
            Boolean PolynomialRing in y"""
    def __len__(self) -> Any:
        """BooleanPolynomial.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3860)

        Return number of monomials in ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: len(x + y)
            2

        ::

            sage: len(P.one())
            1

        ::

            sage: len(x*y + y + z + x*z)
            4

        ::

            sage: len(P.zero())
            0"""
    def __neg__(self) -> Any:
        """BooleanPolynomial.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3249)

        Return -``self``.

        EXAMPLES::

            sage: B.<a,b,z> = BooleanPolynomialRing(3)
            sage: f = a*z + b + 1
            sage: -f
            a*z + b + 1"""
    def __pow__(self, BooleanPolynomialself, intexp, ignored) -> Any:
        """BooleanPolynomial.__pow__(BooleanPolynomial self, int exp, ignored)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 3199)

        Return ``self^(exp)``.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: p = x + y
            sage: p^0
            1

        ::

            sage: p^1
            x + y

        ::

            sage: p^5
            x + y

        ::

            sage: p^-1
            Traceback (most recent call last):
            ...
            NotImplementedError: negative exponents for non constant boolean polynomials not implemented

        ::

            sage: z = P(0)
            sage: z^0
            1

        ::

            sage: z^1
            0"""
    def __reduce__(self) -> Any:
        """BooleanPolynomial.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4035)

        EXAMPLES::

            sage: P.<a,b> = BooleanPolynomialRing(2)
            sage: loads(dumps(a)) == a
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class BooleanPolynomialEntry:
    """BooleanPolynomialEntry(p)"""
    p: p
    def __init__(self, p) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6426)"""

class BooleanPolynomialIdeal(sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal):
    def __init__(self, ring, gens=..., coerce=...) -> Any:
        """BooleanPolynomialIdeal.__init__(self, ring, gens=[], coerce=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4802)

        Construct an ideal in the boolean polynomial ring.

        INPUT:

        - ``ring`` -- the ring this ideal is defined in

        - ``gens`` -- list of generators

        - ``coerce`` -- coerce all elements to the ring ``ring`` (default: ``True``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I
            Ideal (x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0) of Boolean PolynomialRing in x0, x1, x2, x3
            sage: loads(dumps(I)) == I
            True"""
    @overload
    def dimension(self) -> Any:
        """BooleanPolynomialIdeal.dimension(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4825)

        Return the dimension of ``self``, which is always zero.

        TESTS:

        Check that :issue:`13155` is solved::

            sage: R = BooleanPolynomialRing(11, 'x')
            sage: R2 = PolynomialRing(GF(2), 11, 'x')
            sage: I = ideal([ R(f) for f in sage.rings.ideal.Cyclic(R2, 11).gens() ])
            sage: I.dimension()
            0"""
    @overload
    def dimension(self) -> Any:
        """BooleanPolynomialIdeal.dimension(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4825)

        Return the dimension of ``self``, which is always zero.

        TESTS:

        Check that :issue:`13155` is solved::

            sage: R = BooleanPolynomialRing(11, 'x')
            sage: R2 = PolynomialRing(GF(2), 11, 'x')
            sage: I = ideal([ R(f) for f in sage.rings.ideal.Cyclic(R2, 11).gens() ])
            sage: I.dimension()
            0"""
    @overload
    def groebner_basis(self, algorithm=..., **kwds) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self, algorithm=..., prot=...) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def groebner_basis(self) -> Any:
        '''BooleanPolynomialIdeal.groebner_basis(self, algorithm=\'polybori\', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4841)

        Return a Groebner basis of this ideal.

        INPUT:

        - ``algorithm`` -- either ``\'polybori\'`` (built-in default)
          or ``\'magma\'`` (requires Magma)

        - ``red_tail`` -- tail reductions in intermediate polynomials,
          this options affects mainly heuristics. The reducedness of
          the output polynomials can only be guaranteed by the option
          redsb (default: ``True``).

        - ``minsb`` -- return a minimal Groebner basis (default: ``True``)

        - ``redsb`` -- return a minimal Groebner basis and all tails
          are reduced (default: ``True``)

        - ``deg_bound`` -- only compute Groebner basis up to a given
          degree bound (default: ``False``)

        - ``faugere`` -- turn off or on the linear algebra (default: ``False``)

        - ``linear_algebra_in_last_block`` -- this affects the last
          block of block orderings and degree orderings. If it is set
          to ``True`` linear algebra takes affect in this
          block. (default: ``True``)

        - ``gauss_on_linear`` -- perform Gaussian elimination on linear
          polynomials (default: ``True``)

        - ``selection_size`` -- maximum number of polynomials for
          parallel reductions (default: ``1000``)

        - ``heuristic`` -- turn off heuristic by setting
          ``heuristic=False`` (default: ``True``)

        - ``lazy`` -- (default: ``True``)

        - ``invert`` -- setting ``invert=True`` input and output get a
          transformation ``x+1`` for each variable ``x``, which should not
          effect the calculated GB, but the algorithm.

        - ``other_ordering_first`` -- possible values are ``False`` or
          an ordering code. In practice, many Boolean examples have
          very few solutions and a very easy Groebner basis. So, a
          complex walk algorithm (which cannot be implemented using
          the data structures) seems unnecessary, as such Groebner
          bases can be converted quite fast by the normal Buchberger
          algorithm from one ordering into another
          ordering. (default: ``False``)

        - ``prot`` -- show protocol (default: ``False``)

        - ``full_prot`` -- show full protocol (default: ``False``)

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
            sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
            sage: I.groebner_basis()
            [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        Another somewhat bigger example::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis()  # not tested, known bug, unstable (see :issue:`32083`)
            Polynomial Sequence with 36 Polynomials in 36 Variables

        We compute the same example with Magma::

            sage: sr = mq.SR(2,1,1,4,gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: I.groebner_basis(algorithm=\'magma\', prot=\'sage\') # optional - magma
            Leading term degree:  1. Critical pairs: 148.
            ...
            Highest degree reached during computation:  3.
            Polynomial Sequence with ... Polynomials in 36 Variables

        TESTS:

        This example shows, that a bug in our variable indices was
        indeed fixed::

            sage: R.<a111,a112,a121,a122,b111,b112,b211,b212,c111,c112> = BooleanPolynomialRing(order=\'lex\')
            sage: I = (a111 * b111 * c111 + a112 * b112 * c112 - 1, a111 * b211 * c111 + a112 * b212 * c112 - 0,
            ....:      a121 * b111 * c111 + a122 * b112 * c112, a121 * b211 * c111 + a122 * b212 * c112 - 1)*R
            sage: I.groebner_basis()
            [a111 + b212, a112 + b211, a121 + b112, a122 + b111, b111*b112 + b111 + b112 + 1,
             b111*b211 + b111 + b211 + 1, b111*b212 + b112*b211 + 1, b112*b212 + b112 + b212 + 1,
             b211*b212 + b211 + b212 + 1, c111 + 1, c112 + 1]


        The following example shows whether boolean constants are handled correctly::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: I = Ideal([x*z + y*z + z, x*y + x*z + x + y*z + y + z])
            sage: I.groebner_basis()
            [x, y, z]

        Check that this no longer crash (:issue:`12792`)::

            sage: names = [ "s{0}s{1}".format(i,j) for i in range(4) for j in range(8)]
            sage: R = BooleanPolynomialRing(32, names)
            sage: R.inject_variables()
            Defining s0s0, ...
            sage: problem = [s1s0*s1s1, s0s0*s0s1 + s0s0 + s0s1 + s2s0 + s3s0*s3s1 + s3s0 + s3s1,
            ....:            s1s1 + s2s0 + s3s0 + s3s1 + 1, s0s0*s0s1 + s1s1 + s3s0*s3s1 + s3s0,
            ....:            s0s1 + s1s0 + s1s1 + s3s0, s0s0*s0s1 + s0s0 + s0s1 + s1s1 + s2s0 + s3s1,
            ....:            s0s1 + s1s0, s0s0*s0s1 + s0s0 + s0s1 + s1s0 + s2s0 + s3s1,
            ....:            s0s0 + s2s0 + s3s0*s3s1 + s3s0 + 1, s0s0 + s1s1]
            sage: ideal(problem).groebner_basis()
            [1]'''
    @overload
    def interreduced_basis(self) -> Any:
        """BooleanPolynomialIdeal.interreduced_basis(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5115)

        If this ideal is spanned by ``(f_1, ..., f_n)`` this method
        returns ``(g_1, ..., g_s)`` such that:

        - ``<f_1,...,f_n> = <g_1,...,g_s>``
        - ``LT(g_i) != LT(g_j)`` for all ``i != j``
        - ``LT(g_i)`` does not divide ``m`` for all monomials ``m`` of
          ``{g_1,...,g_{i-1},g_{i+1},...,g_s}``

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: g = I.interreduced_basis()
            sage: len(g) == len(set(gi.lt() for gi in g))
            True
            sage: for i in range(len(g)):
            ....:     lt = g[i].lt()
            ....:     for j in range(len(g)):
            ....:         if i == j:
            ....:             continue
            ....:         for t in iter(g[j]):
            ....:             assert lt not in t.divisors()"""
    @overload
    def interreduced_basis(self) -> Any:
        """BooleanPolynomialIdeal.interreduced_basis(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5115)

        If this ideal is spanned by ``(f_1, ..., f_n)`` this method
        returns ``(g_1, ..., g_s)`` such that:

        - ``<f_1,...,f_n> = <g_1,...,g_s>``
        - ``LT(g_i) != LT(g_j)`` for all ``i != j``
        - ``LT(g_i)`` does not divide ``m`` for all monomials ``m`` of
          ``{g_1,...,g_{i-1},g_{i+1},...,g_s}``

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: g = I.interreduced_basis()
            sage: len(g) == len(set(gi.lt() for gi in g))
            True
            sage: for i in range(len(g)):
            ....:     lt = g[i].lt()
            ....:     for j in range(len(g)):
            ....:         if i == j:
            ....:             continue
            ....:         for t in iter(g[j]):
            ....:             assert lt not in t.divisors()"""
    def reduce(self, f) -> Any:
        """BooleanPolynomialIdeal.reduce(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5084)

        Reduce an element modulo the reduced Groebner basis for this ideal.
        This returns 0 if and only if the element is in this ideal. In any
        case, this reduction is unique up to monomial orders.

        EXAMPLES::

            sage: P = PolynomialRing(GF(2),10, 'x')
            sage: B = BooleanPolynomialRing(10,'x')
            sage: I = sage.rings.ideal.Cyclic(P)
            sage: I = B.ideal([B(f) for f in I.gens()])
            sage: gb = I.groebner_basis()
            sage: I.reduce(gb[0])
            0
            sage: I.reduce(gb[0] + 1)
            1
            sage: I.reduce(gb[0]*gb[1])
            0
            sage: I.reduce(gb[0]*B.gen(1))
            0"""
    @overload
    def variety(self, **kwds) -> Any:
        '''BooleanPolynomialIdeal.variety(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5021)

        Return the variety associated to this boolean ideal.

        EXAMPLES:

        A simple example::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: I.variety()
            [{z: 0, y: 1, x: 0}, {z: 1, y: 1, x: 1}]

        TESTS:

        BooleanIdeal and regular (quotient) Ideal should coincide::

            sage: R = BooleanPolynomialRing(6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: R.inject_variables()
            Defining...
            sage: polys = [
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x1 + x2 + x3*x4 + x3*x5 + x3 + x4*x5 + x4*x6 + x4 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x6 + x2*x3 + x2*x6 + x2 + x3*x4 + x5*x6,
            ....:     x1*x3 + x1*x4 + x1*x6 + x1 + x2*x5 + x2*x6 + x3*x4 + x3 + x4*x6 + x4 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x5 + x2 + x3*x5 + x3*x6 + x3 + x5 + x6,
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x6 + x2*x4 + x2*x5 + x2*x6 + x3*x6 + x4*x6 + x5*x6 + x5]
            sage: I = R.ideal( polys )
            sage: I.variety()
             [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
              {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]

            sage: R = PolynomialRing(GF(2), 6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: I = R.ideal( polys )
            sage: v = (I + sage.rings.ideal.FieldIdeal(R)).variety()
            sage: v
            [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
             {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]


        Check that :issue:`13976` is fixed::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: sols = I.variety()
            sage: sols[0][y]
            1

        Make sure the result is a key converting dict, as discussed in
        :issue:`9788` and consistent with
        :meth:`sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal_singular_repr.variety`::

            sage: sols[0]["y"]
            1'''
    @overload
    def variety(self) -> Any:
        '''BooleanPolynomialIdeal.variety(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5021)

        Return the variety associated to this boolean ideal.

        EXAMPLES:

        A simple example::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: I.variety()
            [{z: 0, y: 1, x: 0}, {z: 1, y: 1, x: 1}]

        TESTS:

        BooleanIdeal and regular (quotient) Ideal should coincide::

            sage: R = BooleanPolynomialRing(6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: R.inject_variables()
            Defining...
            sage: polys = [
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x1 + x2 + x3*x4 + x3*x5 + x3 + x4*x5 + x4*x6 + x4 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x6 + x2*x3 + x2*x6 + x2 + x3*x4 + x5*x6,
            ....:     x1*x3 + x1*x4 + x1*x6 + x1 + x2*x5 + x2*x6 + x3*x4 + x3 + x4*x6 + x4 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x5 + x2 + x3*x5 + x3*x6 + x3 + x5 + x6,
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x6 + x2*x4 + x2*x5 + x2*x6 + x3*x6 + x4*x6 + x5*x6 + x5]
            sage: I = R.ideal( polys )
            sage: I.variety()
             [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
              {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]

            sage: R = PolynomialRing(GF(2), 6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: I = R.ideal( polys )
            sage: v = (I + sage.rings.ideal.FieldIdeal(R)).variety()
            sage: v
            [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
             {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]


        Check that :issue:`13976` is fixed::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: sols = I.variety()
            sage: sols[0][y]
            1

        Make sure the result is a key converting dict, as discussed in
        :issue:`9788` and consistent with
        :meth:`sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal_singular_repr.variety`::

            sage: sols[0]["y"]
            1'''
    @overload
    def variety(self) -> Any:
        '''BooleanPolynomialIdeal.variety(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5021)

        Return the variety associated to this boolean ideal.

        EXAMPLES:

        A simple example::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: I.variety()
            [{z: 0, y: 1, x: 0}, {z: 1, y: 1, x: 1}]

        TESTS:

        BooleanIdeal and regular (quotient) Ideal should coincide::

            sage: R = BooleanPolynomialRing(6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: R.inject_variables()
            Defining...
            sage: polys = [
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x1 + x2 + x3*x4 + x3*x5 + x3 + x4*x5 + x4*x6 + x4 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x6 + x2*x3 + x2*x6 + x2 + x3*x4 + x5*x6,
            ....:     x1*x3 + x1*x4 + x1*x6 + x1 + x2*x5 + x2*x6 + x3*x4 + x3 + x4*x6 + x4 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x5 + x2 + x3*x5 + x3*x6 + x3 + x5 + x6,
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x6 + x2*x4 + x2*x5 + x2*x6 + x3*x6 + x4*x6 + x5*x6 + x5]
            sage: I = R.ideal( polys )
            sage: I.variety()
             [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
              {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]

            sage: R = PolynomialRing(GF(2), 6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: I = R.ideal( polys )
            sage: v = (I + sage.rings.ideal.FieldIdeal(R)).variety()
            sage: v
            [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
             {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]


        Check that :issue:`13976` is fixed::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: sols = I.variety()
            sage: sols[0][y]
            1

        Make sure the result is a key converting dict, as discussed in
        :issue:`9788` and consistent with
        :meth:`sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal_singular_repr.variety`::

            sage: sols[0]["y"]
            1'''
    @overload
    def variety(self) -> Any:
        '''BooleanPolynomialIdeal.variety(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5021)

        Return the variety associated to this boolean ideal.

        EXAMPLES:

        A simple example::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: I.variety()
            [{z: 0, y: 1, x: 0}, {z: 1, y: 1, x: 1}]

        TESTS:

        BooleanIdeal and regular (quotient) Ideal should coincide::

            sage: R = BooleanPolynomialRing(6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: R.inject_variables()
            Defining...
            sage: polys = [
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x1 + x2 + x3*x4 + x3*x5 + x3 + x4*x5 + x4*x6 + x4 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x6 + x2*x3 + x2*x6 + x2 + x3*x4 + x5*x6,
            ....:     x1*x3 + x1*x4 + x1*x6 + x1 + x2*x5 + x2*x6 + x3*x4 + x3 + x4*x6 + x4 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x5 + x2 + x3*x5 + x3*x6 + x3 + x5 + x6,
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x6 + x2*x4 + x2*x5 + x2*x6 + x3*x6 + x4*x6 + x5*x6 + x5]
            sage: I = R.ideal( polys )
            sage: I.variety()
             [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
              {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]

            sage: R = PolynomialRing(GF(2), 6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: I = R.ideal( polys )
            sage: v = (I + sage.rings.ideal.FieldIdeal(R)).variety()
            sage: v
            [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
             {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]


        Check that :issue:`13976` is fixed::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: sols = I.variety()
            sage: sols[0][y]
            1

        Make sure the result is a key converting dict, as discussed in
        :issue:`9788` and consistent with
        :meth:`sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal_singular_repr.variety`::

            sage: sols[0]["y"]
            1'''
    @overload
    def variety(self) -> Any:
        '''BooleanPolynomialIdeal.variety(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5021)

        Return the variety associated to this boolean ideal.

        EXAMPLES:

        A simple example::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: I.variety()
            [{z: 0, y: 1, x: 0}, {z: 1, y: 1, x: 1}]

        TESTS:

        BooleanIdeal and regular (quotient) Ideal should coincide::

            sage: R = BooleanPolynomialRing(6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: R.inject_variables()
            Defining...
            sage: polys = [
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x1 + x2 + x3*x4 + x3*x5 + x3 + x4*x5 + x4*x6 + x4 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x6 + x2*x3 + x2*x6 + x2 + x3*x4 + x5*x6,
            ....:     x1*x3 + x1*x4 + x1*x6 + x1 + x2*x5 + x2*x6 + x3*x4 + x3 + x4*x6 + x4 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x3 + x1*x4 + x1*x5 + x2 + x3*x5 + x3*x6 + x3 + x5 + x6,
            ....:     x1*x2 + x1*x4 + x1*x5 + x1*x6 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5*x6 + x5 + x6,
            ....:     x1*x2 + x1*x6 + x2*x4 + x2*x5 + x2*x6 + x3*x6 + x4*x6 + x5*x6 + x5]
            sage: I = R.ideal( polys )
            sage: I.variety()
             [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
              {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]

            sage: R = PolynomialRing(GF(2), 6, [\'x%d\'%(i+1) for i in range(6)], order=\'lex\')
            sage: I = R.ideal( polys )
            sage: v = (I + sage.rings.ideal.FieldIdeal(R)).variety()
            sage: v
            [{x6: 0, x5: 0, x4: 0, x3: 0, x2: 0, x1: 0},
             {x6: 1, x5: 0, x4: 0, x3: 1, x2: 1, x1: 1}]


        Check that :issue:`13976` is fixed::

            sage: R.<x,y,z> = BooleanPolynomialRing()
            sage: I = ideal( [ x*y*z + x*z + y + 1, x+y+z+1 ] )
            sage: sols = I.variety()
            sage: sols[0][y]
            1

        Make sure the result is a key converting dict, as discussed in
        :issue:`9788` and consistent with
        :meth:`sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal_singular_repr.variety`::

            sage: sols[0]["y"]
            1'''
    def __eq__(self, other) -> Any:
        """BooleanPolynomialIdeal.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5148)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: J = Ideal(I.interreduced_basis())
            sage: I == J
            True
            sage: J = Ideal(I.gens()[1:] + [I.gens()[0] + 1])
            sage: I == J
            False"""
    def __ne__(self, other) -> Any:
        """BooleanPolynomialIdeal.__ne__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5174)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: I = F.ideal()
            sage: J = Ideal(I.interreduced_basis())
            sage: I != J
            False
            sage: J = Ideal(I.gens()[1:] + [I.gens()[0] + 1])
            sage: I != J
            True"""

class BooleanPolynomialIterator:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4750)

        Iterator over the monomials of a boolean polynomial.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """BooleanPolynomialIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4758)

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: f = B.random_element()
            sage: entries = list(f)  # indirect doctest
            sage: sum(entries) == f
            True"""
    def __next__(self) -> Any:
        """BooleanPolynomialIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4770)

        EXAMPLES::

            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: f = B.random_element()
            sage: it = iter(f)
            sage: sum(next(it) for _ in range(5)) == f  # indirect doctest
            True"""

class BooleanPolynomialRing(sage.rings.polynomial.multi_polynomial_ring_base.BooleanPolynomialRing_base):
    '''BooleanPolynomialRing(n=None, names=None, order=\'lex\')

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 255)

    Construct a boolean polynomial ring with the following parameters:

    INPUT:

    - ``n`` -- integer > 1; number of variables

    - ``names`` -- names of ring variables; may be a string or
      list/tuple

    - ``order`` -- term order (default: lex)

    EXAMPLES::

        sage: R.<x, y, z> = BooleanPolynomialRing()
        sage: R
        Boolean PolynomialRing in x, y, z

    ::

        sage: p = x*y + x*z + y*z
        sage: x*p
        x*y*z + x*y + x*z

    ::

        sage: R.term_order()
        Lexicographic term order

    ::

        sage: R = BooleanPolynomialRing(5,\'x\',order=\'deglex(3),deglex(2)\')
        sage: R.term_order()
        Block term order with blocks:
        (Degree lexicographic term order of length 3,
         Degree lexicographic term order of length 2)

    ::

        sage: R = BooleanPolynomialRing(3,\'x\',order=\'deglex\')
        sage: R.term_order()
        Degree lexicographic term order

    TESTS::

        sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4,order=\'deglex(2),deglex(2)\')
        sage: x0 > x1
        True
        sage: x2 > x3
        True
        sage: TestSuite(P).run(skip=["_test_zero_divisors", "_test_elements"])

    Boolean polynomial rings are unique parent structures. We
    thus have::

        sage: P.<x,y> = BooleanPolynomialRing(2)
        sage: R.<x,y> = BooleanPolynomialRing(2)
        sage: P is R
        True

    ::

        sage: Q.<x,z> = BooleanPolynomialRing(2)
        sage: P == Q
        False

    ::

        sage: S.<x,y> = BooleanPolynomialRing(2, order=\'deglex\')
        sage: P == S
        False'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, n=..., names=..., order=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 328)

                Create a new boolean polynomial ring.

                EXAMPLES::

                    sage: R.<x, y, z> = BooleanPolynomialRing()
                    sage: R
                    Boolean PolynomialRing in x, y, z

                .. NOTE::

                    See class documentation for parameters.
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 328)

                Create a new boolean polynomial ring.

                EXAMPLES::

                    sage: R.<x, y, z> = BooleanPolynomialRing()
                    sage: R
                    Boolean PolynomialRing in x, y, z

                .. NOTE::

                    See class documentation for parameters.
        """
    @overload
    def change_ring(self, base_ring=..., names=..., order=...) -> Any:
        """BooleanPolynomialRing.change_ring(self, base_ring=None, names=None, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 552)

        Return a new multivariate polynomial ring with base ring ``base_ring``,
        variable names set to ``names``, and term ordering given by ``order``.

        When ``base_ring`` is not specified, this function returns
        a ``BooleanPolynomialRing`` isomorphic to ``self``. Otherwise,
        this returns a ``MPolynomialRing``. Each argument above is optional.

        INPUT:

        - ``base_ring`` -- a base ring
        - ``names`` -- variable names
        - ``order`` -- a term order

        EXAMPLES::

            sage: P.<x, y, z> = BooleanPolynomialRing()
            sage: P.term_order()
            Lexicographic term order
            sage: R = P.change_ring(names=('a', 'b', 'c'), order='deglex')
            sage: R
            Boolean PolynomialRing in a, b, c
            sage: R.term_order()
            Degree lexicographic term order
            sage: T = P.change_ring(base_ring=GF(3))
            sage: T
            Multivariate Polynomial Ring in x, y, z over Finite Field of size 3
            sage: T.term_order()
            Lexicographic term order"""
    @overload
    def change_ring(self, names=..., order=...) -> Any:
        """BooleanPolynomialRing.change_ring(self, base_ring=None, names=None, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 552)

        Return a new multivariate polynomial ring with base ring ``base_ring``,
        variable names set to ``names``, and term ordering given by ``order``.

        When ``base_ring`` is not specified, this function returns
        a ``BooleanPolynomialRing`` isomorphic to ``self``. Otherwise,
        this returns a ``MPolynomialRing``. Each argument above is optional.

        INPUT:

        - ``base_ring`` -- a base ring
        - ``names`` -- variable names
        - ``order`` -- a term order

        EXAMPLES::

            sage: P.<x, y, z> = BooleanPolynomialRing()
            sage: P.term_order()
            Lexicographic term order
            sage: R = P.change_ring(names=('a', 'b', 'c'), order='deglex')
            sage: R
            Boolean PolynomialRing in a, b, c
            sage: R.term_order()
            Degree lexicographic term order
            sage: T = P.change_ring(base_ring=GF(3))
            sage: T
            Multivariate Polynomial Ring in x, y, z over Finite Field of size 3
            sage: T.term_order()
            Lexicographic term order"""
    @overload
    def change_ring(self, base_ring=...) -> Any:
        """BooleanPolynomialRing.change_ring(self, base_ring=None, names=None, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 552)

        Return a new multivariate polynomial ring with base ring ``base_ring``,
        variable names set to ``names``, and term ordering given by ``order``.

        When ``base_ring`` is not specified, this function returns
        a ``BooleanPolynomialRing`` isomorphic to ``self``. Otherwise,
        this returns a ``MPolynomialRing``. Each argument above is optional.

        INPUT:

        - ``base_ring`` -- a base ring
        - ``names`` -- variable names
        - ``order`` -- a term order

        EXAMPLES::

            sage: P.<x, y, z> = BooleanPolynomialRing()
            sage: P.term_order()
            Lexicographic term order
            sage: R = P.change_ring(names=('a', 'b', 'c'), order='deglex')
            sage: R
            Boolean PolynomialRing in a, b, c
            sage: R.term_order()
            Degree lexicographic term order
            sage: T = P.change_ring(base_ring=GF(3))
            sage: T
            Multivariate Polynomial Ring in x, y, z over Finite Field of size 3
            sage: T.term_order()
            Lexicographic term order"""
    @overload
    def clone(self, ordering=..., names=..., blocks=...) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def clone(self, ordering=..., names=..., block=...) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def clone(self) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def clone(self, ordering=...) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def clone(self, names=...) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def clone(self, blocks=...) -> Any:
        """BooleanPolynomialRing.clone(self, ordering=None, names=[], blocks=[])

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1704)

        Shallow copy this boolean polynomial ring, but with different
        ordering, names or blocks if given.

        ring.clone(ordering=..., names=..., block=...) generates a shallow copy
        of ring, but with different ordering, names or blocks if given.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: B.clone()
            Boolean PolynomialRing in a, b, c

        ::

            sage: B.<x,y,z> = BooleanPolynomialRing(3,order='deglex')
            sage: y*z > x
            True

        Now we call the clone method and generate a compatible, but 'lex' ordered, ring::

            sage: C = B.clone(ordering=0)
            sage: C(y*z) > C(x)
            False

        Now we change variable names::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P
            Boolean PolynomialRing in x0, x1

        ::

            sage: Q = P.clone(names=['t'])
            sage: Q
            Boolean PolynomialRing in t, x1

        We can also append blocks to block orderings this way::

            sage: R.<x1,x2,x3,x4> = BooleanPolynomialRing(order='deglex(1),deglex(3)')
            sage: x2 > x3*x4
            False

        Now we call the internal method and change the blocks::

            sage: S = R.clone(blocks=[3])
            sage: S(x2) > S(x3*x4)
            True


        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def construction(self) -> Any:
        '''BooleanPolynomialRing.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 449)

        A boolean polynomial ring is the quotient of a polynomial ring,
        in a special implementation.

        Before :issue:`15223`, the boolean polynomial rings returned the
        construction of a polynomial ring, which was of course wrong.

        Now, a :class:`~sage.categories.pushout.QuotientFunctor` is returned
        that knows about the `"pbori"` implementation.

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4,order=\'degneglex(2),degneglex(2)\')
            sage: F,O = P.construction()
            sage: O
            Multivariate Polynomial Ring in x0, x1, x2, x3 over Finite Field of size 2
            sage: F
            QuotientFunctor
            sage: F(O) is P
            True'''
    @overload
    def construction(self) -> Any:
        '''BooleanPolynomialRing.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 449)

        A boolean polynomial ring is the quotient of a polynomial ring,
        in a special implementation.

        Before :issue:`15223`, the boolean polynomial rings returned the
        construction of a polynomial ring, which was of course wrong.

        Now, a :class:`~sage.categories.pushout.QuotientFunctor` is returned
        that knows about the `"pbori"` implementation.

        EXAMPLES::

            sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4,order=\'degneglex(2),degneglex(2)\')
            sage: F,O = P.construction()
            sage: O
            Multivariate Polynomial Ring in x0, x1, x2, x3 over Finite Field of size 2
            sage: F
            QuotientFunctor
            sage: F(O) is P
            True'''
    def cover_ring(self) -> Any:
        """BooleanPolynomialRing.cover_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1368)

        Return `R = \\GF{2}[x_1,x_2,...,x_n]` if ``x_1,x_2,...,x_n`` is
        the ordered list of variable names of this ring. ``R`` also
        has the same term ordering as this ring.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing(2)
            sage: R = B.cover_ring(); R
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

        ::

            sage: B.term_order() == R.term_order()
            True

        The cover ring is cached::

            sage: B.cover_ring() is B.cover_ring()
            True"""
    def defining_ideal(self) -> Any:
        """BooleanPolynomialRing.defining_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1397)

        Return `I = <x_i^2 + x_i> \\subset R` where ``R =
        self.cover_ring()``, and `x_i` any element in the set of
        variables of this ring.

        EXAMPLES::

            sage: B.<x,y> = BooleanPolynomialRing(2)
            sage: I = B.defining_ideal(); I
            Ideal (x^2 + x, y^2 + y) of Multivariate Polynomial Ring
            in x, y over Finite Field of size 2"""
    @overload
    def gen(self, i=...) -> Any:
        """BooleanPolynomialRing.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 497)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gen()
            x
            sage: P.gen(2)
            z
            sage: m = x.monomials()[0]
            sage: P.gen(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.gen(0)
            x"""
    @overload
    def gen(self) -> Any:
        """BooleanPolynomialRing.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 497)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gen()
            x
            sage: P.gen(2)
            z
            sage: m = x.monomials()[0]
            sage: P.gen(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.gen(0)
            x"""
    @overload
    def gen(self, m) -> Any:
        """BooleanPolynomialRing.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 497)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gen()
            x
            sage: P.gen(2)
            z
            sage: m = x.monomials()[0]
            sage: P.gen(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.gen(0)
            x"""
    @overload
    def gens(self) -> tuple:
        """BooleanPolynomialRing.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 532)

        Return the tuple of variables in this ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gens()
            (x, y, z)

        ::

            sage: P = BooleanPolynomialRing(10,'x')
            sage: P.gens()
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)"""
    @overload
    def gens(self) -> Any:
        """BooleanPolynomialRing.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 532)

        Return the tuple of variables in this ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gens()
            (x, y, z)

        ::

            sage: P = BooleanPolynomialRing(10,'x')
            sage: P.gens()
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)"""
    @overload
    def gens(self) -> Any:
        """BooleanPolynomialRing.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 532)

        Return the tuple of variables in this ring.

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.gens()
            (x, y, z)

        ::

            sage: P = BooleanPolynomialRing(10,'x')
            sage: P.gens()
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)"""
    @overload
    def get_base_order_code(self) -> Any:
        """BooleanPolynomialRing.get_base_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1640)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_base_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_base_order_code()
            1
            sage: T = TermOrder('deglex',2) + TermOrder('deglex',2)
            sage: B.<a,b,c,d> = BooleanPolynomialRing(4, order=T)
            sage: B.get_base_order_code()
            1

        .. NOTE::

          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_base_order_code(self) -> Any:
        """BooleanPolynomialRing.get_base_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1640)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_base_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_base_order_code()
            1
            sage: T = TermOrder('deglex',2) + TermOrder('deglex',2)
            sage: B.<a,b,c,d> = BooleanPolynomialRing(4, order=T)
            sage: B.get_base_order_code()
            1

        .. NOTE::

          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_base_order_code(self) -> Any:
        """BooleanPolynomialRing.get_base_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1640)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_base_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_base_order_code()
            1
            sage: T = TermOrder('deglex',2) + TermOrder('deglex',2)
            sage: B.<a,b,c,d> = BooleanPolynomialRing(4, order=T)
            sage: B.get_base_order_code()
            1

        .. NOTE::

          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_base_order_code(self) -> Any:
        """BooleanPolynomialRing.get_base_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1640)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_base_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_base_order_code()
            1
            sage: T = TermOrder('deglex',2) + TermOrder('deglex',2)
            sage: B.<a,b,c,d> = BooleanPolynomialRing(4, order=T)
            sage: B.get_base_order_code()
            1

        .. NOTE::

          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_order_code(self) -> Any:
        """BooleanPolynomialRing.get_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1619)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_order_code()
            1

        .. NOTE::


          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_order_code(self) -> Any:
        """BooleanPolynomialRing.get_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1619)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_order_code()
            1

        .. NOTE::


          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def get_order_code(self) -> Any:
        """BooleanPolynomialRing.get_order_code(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1619)


        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: B.get_order_code()
            0

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(order='deglex')
            sage: B.get_order_code()
            1

        .. NOTE::


          This function which is part of the PolyBoRi upstream API works
          with a current global ring. This notion is avoided in Sage."""
    @overload
    def has_degree_order(self) -> Any:
        """BooleanPolynomialRing.has_degree_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1664)

        Return checks whether the order code corresponds to a degree ordering.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.has_degree_order()
            False"""
    @overload
    def has_degree_order(self) -> Any:
        """BooleanPolynomialRing.has_degree_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1664)

        Return checks whether the order code corresponds to a degree ordering.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.has_degree_order()
            False"""
    @overload
    def id(self) -> Any:
        '''BooleanPolynomialRing.id(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1565)

        Return a unique identifier for this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: print("id: {}".format(P.id()))
            id: ...

            sage: P = BooleanPolynomialRing(10, \'x\')
            sage: Q = BooleanPolynomialRing(20, \'x\')

            sage: P.id() != Q.id()
            True'''
    @overload
    def id(self) -> Any:
        '''BooleanPolynomialRing.id(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1565)

        Return a unique identifier for this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: print("id: {}".format(P.id()))
            id: ...

            sage: P = BooleanPolynomialRing(10, \'x\')
            sage: Q = BooleanPolynomialRing(20, \'x\')

            sage: P.id() != Q.id()
            True'''
    @overload
    def id(self) -> Any:
        '''BooleanPolynomialRing.id(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1565)

        Return a unique identifier for this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: print("id: {}".format(P.id()))
            id: ...

            sage: P = BooleanPolynomialRing(10, \'x\')
            sage: Q = BooleanPolynomialRing(20, \'x\')

            sage: P.id() != Q.id()
            True'''
    def ideal(self, *gens, **kwds) -> Any:
        """BooleanPolynomialRing.ideal(self, *gens, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1090)

        Create an ideal in this ring.

        INPUT:

        - ``gens`` -- list or tuple of generators

        - ``coerce`` -- boolean (default: ``True``); automatically
          coerce the given polynomials to this ring to form the ideal

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.ideal(x+y)
            Ideal (x + y) of Boolean PolynomialRing in x, y, z

        ::

            sage: P.ideal(x*y, y*z)
            Ideal (x*y, y*z) of Boolean PolynomialRing in x, y, z

        ::

            sage: P.ideal([x+y, z])
            Ideal (x + y, z) of Boolean PolynomialRing in x, y, z"""
    @overload
    def interpolation_polynomial(self, zeros, ones) -> Any:
        '''BooleanPolynomialRing.interpolation_polynomial(self, zeros, ones)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1464)

        Return the lexicographically minimal boolean polynomial for the
        given sets of points.

        Given two sets of points ``zeros`` - evaluating to zero
        - and ``ones`` - evaluating to one -, compute the
        lexicographically minimal boolean polynomial satisfying these
        points.

        INPUT:

        - ``zeros`` -- the set of interpolation points mapped to zero

        - ``ones`` -- the set of interpolation points mapped to one

        EXAMPLES:

        First we create a random-ish boolean polynomial.

        ::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(6)
            sage: f = a*b*c*e + a*d*e + a*f + b + c + e + f + 1

        Now we find interpolation points mapping to zero and to one.

        ::

            sage: zeros = set([(1, 0, 1, 0, 0, 0), (1, 0, 0, 0, 1, 0),
            ....:              (0, 0, 1, 1, 1, 1), (1, 0, 1, 1, 1, 1),
            ....:              (0, 0, 0, 0, 1, 0), (0, 1, 1, 1, 1, 0),
            ....:              (1, 1, 0, 0, 0, 1), (1, 1, 0, 1, 0, 1)])
            sage: ones = set([(0, 0, 0, 0, 0, 0), (1, 0, 1, 0, 1, 0),
            ....:             (0, 0, 0, 1, 1, 1), (1, 0, 0, 1, 0, 1),
            ....:             (0, 0, 0, 0, 1, 1), (0, 1, 1, 0, 1, 1),
            ....:             (0, 1, 1, 1, 1, 1), (1, 1, 1, 0, 1, 0)])
            sage: [f(*p) for p in zeros]
            [0, 0, 0, 0, 0, 0, 0, 0]
            sage: [f(*p) for p in ones]
            [1, 1, 1, 1, 1, 1, 1, 1]

        Finally, we find the lexicographically smallest interpolation
        polynomial using PolyBoRi .

        ::

            sage: g = B.interpolation_polynomial(zeros, ones); g
            b*f + c + d*f + d + e*f + e + 1

        ::

            sage: [g(*p) for p in zeros]
            [0, 0, 0, 0, 0, 0, 0, 0]
            sage: [g(*p) for p in ones]
            [1, 1, 1, 1, 1, 1, 1, 1]

        Alternatively, we can work with PolyBoRi\'s native
        ``BooleSet``\'s. This example is from the PolyBoRi tutorial::

            sage: B = BooleanPolynomialRing(4,"x0,x1,x2,x3")
            sage: x = B.gen
            sage: V=(x(0)+x(1)+x(2)+x(3)+1).set(); V
            {{x0}, {x1}, {x2}, {x3}, {}}
            sage: f=x(0)*x(1)+x(1)+x(2)+1
            sage: z = f.zeros_in(V); z
            {{x1}, {x2}}
            sage: o = V.diff(z); o
            {{x0}, {x3}, {}}
            sage: B.interpolation_polynomial(z,o)
            x1 + x2 + 1

        ALGORITHM: Calls ``interpolate_smallest_lex`` as described in
        the PolyBoRi tutorial.'''
    @overload
    def interpolation_polynomial(self, zeros, ones) -> Any:
        '''BooleanPolynomialRing.interpolation_polynomial(self, zeros, ones)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1464)

        Return the lexicographically minimal boolean polynomial for the
        given sets of points.

        Given two sets of points ``zeros`` - evaluating to zero
        - and ``ones`` - evaluating to one -, compute the
        lexicographically minimal boolean polynomial satisfying these
        points.

        INPUT:

        - ``zeros`` -- the set of interpolation points mapped to zero

        - ``ones`` -- the set of interpolation points mapped to one

        EXAMPLES:

        First we create a random-ish boolean polynomial.

        ::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing(6)
            sage: f = a*b*c*e + a*d*e + a*f + b + c + e + f + 1

        Now we find interpolation points mapping to zero and to one.

        ::

            sage: zeros = set([(1, 0, 1, 0, 0, 0), (1, 0, 0, 0, 1, 0),
            ....:              (0, 0, 1, 1, 1, 1), (1, 0, 1, 1, 1, 1),
            ....:              (0, 0, 0, 0, 1, 0), (0, 1, 1, 1, 1, 0),
            ....:              (1, 1, 0, 0, 0, 1), (1, 1, 0, 1, 0, 1)])
            sage: ones = set([(0, 0, 0, 0, 0, 0), (1, 0, 1, 0, 1, 0),
            ....:             (0, 0, 0, 1, 1, 1), (1, 0, 0, 1, 0, 1),
            ....:             (0, 0, 0, 0, 1, 1), (0, 1, 1, 0, 1, 1),
            ....:             (0, 1, 1, 1, 1, 1), (1, 1, 1, 0, 1, 0)])
            sage: [f(*p) for p in zeros]
            [0, 0, 0, 0, 0, 0, 0, 0]
            sage: [f(*p) for p in ones]
            [1, 1, 1, 1, 1, 1, 1, 1]

        Finally, we find the lexicographically smallest interpolation
        polynomial using PolyBoRi .

        ::

            sage: g = B.interpolation_polynomial(zeros, ones); g
            b*f + c + d*f + d + e*f + e + 1

        ::

            sage: [g(*p) for p in zeros]
            [0, 0, 0, 0, 0, 0, 0, 0]
            sage: [g(*p) for p in ones]
            [1, 1, 1, 1, 1, 1, 1, 1]

        Alternatively, we can work with PolyBoRi\'s native
        ``BooleSet``\'s. This example is from the PolyBoRi tutorial::

            sage: B = BooleanPolynomialRing(4,"x0,x1,x2,x3")
            sage: x = B.gen
            sage: V=(x(0)+x(1)+x(2)+x(3)+1).set(); V
            {{x0}, {x1}, {x2}, {x3}, {}}
            sage: f=x(0)*x(1)+x(1)+x(2)+1
            sage: z = f.zeros_in(V); z
            {{x1}, {x2}}
            sage: o = V.diff(z); o
            {{x0}, {x3}, {}}
            sage: B.interpolation_polynomial(z,o)
            x1 + x2 + 1

        ALGORITHM: Calls ``interpolate_smallest_lex`` as described in
        the PolyBoRi tutorial.'''
    @overload
    def n_variables(self) -> Any:
        """BooleanPolynomialRing.n_variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1772)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.n_variables()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.n_variables()
            1000

        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def n_variables(self) -> Any:
        """BooleanPolynomialRing.n_variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1772)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.n_variables()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.n_variables()
            1000

        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def n_variables(self) -> Any:
        """BooleanPolynomialRing.n_variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1772)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.n_variables()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.n_variables()
            1000

        .. NOTE::

            This is part of PolyBoRi's native interface."""
    @overload
    def ngens(self) -> Any:
        """BooleanPolynomialRing.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 479)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.ngens()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.ngens()
            1000"""
    @overload
    def ngens(self) -> Any:
        """BooleanPolynomialRing.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 479)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.ngens()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.ngens()
            1000"""
    @overload
    def ngens(self) -> Any:
        """BooleanPolynomialRing.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 479)

        Return the number of variables in this boolean polynomial ring.

        EXAMPLES::

            sage: P.<x,y> = BooleanPolynomialRing(2)
            sage: P.ngens()
            2

        ::

            sage: P = BooleanPolynomialRing(1000, 'x')
            sage: P.ngens()
            1000"""
    @overload
    def one(self) -> Any:
        """BooleanPolynomialRing.one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1684)

        EXAMPLES::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P.one()
            1"""
    @overload
    def one(self) -> Any:
        """BooleanPolynomialRing.one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1684)

        EXAMPLES::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P.one()
            1"""
    @overload
    def random_element(self, degree=..., terms=..., choose_degree=..., vars_set=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, terms=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, degree=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, degree=..., terms=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, degree=..., terms=..., vars_set=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def random_element(self, terms=...) -> Any:
        """BooleanPolynomialRing.random_element(self, degree=None, terms=None, choose_degree=False, vars_set=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1122)

        Return a random boolean polynomial. Generated polynomial has the
        given number of terms, and at most given degree.

        INPUT:

        - ``degree`` -- maximum degree (default: 2 for len(var_set) > 1, 1 otherwise)

        - ``terms`` -- number of terms requested (default: 5). If more
          terms are requested than exist, then this parameter is
          silently reduced to the maximum number of available terms.

        - ``choose_degree`` -- choose degree of monomials
          randomly first, rather than monomials uniformly random

        - ``vars_set`` -- list of integer indices of
          generators of ``self`` to use in the generated polynomial

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: f = P.random_element(degree=3, terms=4)
            sage: f.degree() <= 3
            True
            sage: len(f.terms())
            4

        ::

            sage: f = P.random_element(degree=1, terms=2)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

        In corner cases this function will return fewer terms by default::

            sage: P = BooleanPolynomialRing(2,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            2

            sage: P = BooleanPolynomialRing(1,'y')
            sage: f = P.random_element()
            sage: len(f.terms())
            1

        We return uniformly random polynomials up to degree 2::

            sage: from collections import defaultdict
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: counter = 0.0
            sage: dic = defaultdict(Integer)
            sage: def more_terms():
            ....:     global counter, dic
            ....:     for t in B.random_element(terms=Infinity).terms():
            ....:         counter += 1.0
            ....:         dic[t] += 1

            sage: more_terms()
            sage: while any(abs(dic[t]/counter - 1.0/11) > 0.01 for t in dic):
            ....:     more_terms()

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.random_element(degree=4)
            Traceback (most recent call last):
            ...
            ValueError: given degree should be less than or equal to number of variables (3)

            sage: f = P.random_element(degree=1, terms=5)
            sage: f.degree() <= 1
            True
            sage: len(f.terms())
            2

            sage: f = P.random_element(degree=2, terms=5, vars_set=(0,1))
            sage: f.degree() <= 2
            True
            sage: len(f.terms())
            2
            sage: all(t in [x, y, x*y, P(1)] for t in f.terms())
            True

        We test that :issue:`13845` is fixed::

            sage: n = 10
            sage: B = BooleanPolynomialRing(n, 'x')
            sage: r = B.random_element(terms=(n/2)**2)"""
    @overload
    def remove_var(self, *var, order=...) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, z) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, z, x) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, y, z, x) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, y, z, x, w) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, y) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, y) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, x, y, z) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def remove_var(self, x, y, z, order=...) -> Any:
        """BooleanPolynomialRing.remove_var(self, *var, order=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1035)

        Remove a variable or sequence of variables from this ring.

        If ``order`` is not specified, then the subring inherits the
        term order of the original ring, if possible.

        EXAMPLES::

            sage: R.<x,y,z,w> = BooleanPolynomialRing()
            sage: R.remove_var(z)
            Boolean PolynomialRing in x, y, w
            sage: R.remove_var(z,x)
            Boolean PolynomialRing in y, w
            sage: R.remove_var(y,z,x)
            Boolean PolynomialRing in w

        Removing all variables results in the base ring::

            sage: R.remove_var(y,z,x,w)
            Finite Field of size 2

        If possible, the term order is kept:

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='deglex')
             sage: R.remove_var(y).term_order()
             Degree lexicographic term order

             sage: R.<x,y,z,w> = BooleanPolynomialRing(order='lex')
             sage: R.remove_var(y).term_order()
             Lexicographic term order

        Be careful with block orders when removing variables::

            sage: R.<x,y,z,u,v> = BooleanPolynomialRing(order='deglex(2),deglex(3)')
            sage: R.remove_var(x,y,z)
            Traceback (most recent call last):
            ...
            ValueError: impossible to use the original term order (most likely because it was a block order); please specify the term order for the subring
            sage: R.remove_var(x,y,z, order='deglex')
            Boolean PolynomialRing in u, v"""
    @overload
    def variable(self, i=...) -> Any:
        """BooleanPolynomialRing.variable(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1583)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.variable()
            x
            sage: P.variable(2)
            z
            sage: m = x.monomials()[0]
            sage: P.variable(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.variable(0)
            x"""
    @overload
    def variable(self) -> Any:
        """BooleanPolynomialRing.variable(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1583)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.variable()
            x
            sage: P.variable(2)
            z
            sage: m = x.monomials()[0]
            sage: P.variable(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.variable(0)
            x"""
    @overload
    def variable(self, m) -> Any:
        """BooleanPolynomialRing.variable(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1583)

        Return the `i`-th generator of this boolean polynomial ring.

        INPUT:

        - ``i`` -- integer or a boolean monomial in one variable

        EXAMPLES::

            sage: P.<x,y,z> = BooleanPolynomialRing(3)
            sage: P.variable()
            x
            sage: P.variable(2)
            z
            sage: m = x.monomials()[0]
            sage: P.variable(m)
            x

        TESTS::

            sage: P.<x,y,z> = BooleanPolynomialRing(3, order='deglex')
            sage: P.variable(0)
            x"""
    @overload
    def zero(self) -> Any:
        """BooleanPolynomialRing.zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1694)

        EXAMPLES::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P.zero()
            0"""
    @overload
    def zero(self) -> Any:
        """BooleanPolynomialRing.zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1694)

        EXAMPLES::

            sage: P.<x0,x1> = BooleanPolynomialRing(2)
            sage: P.zero()
            0"""
    def __hash__(self) -> Any:
        """BooleanPolynomialRing.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 1019)

        Return a hash of this boolean polynomial ring.

        EXAMPLES::

            sage: P.<a,b,c,d> = BooleanPolynomialRing(4, order='lex')
            sage: P
            Boolean PolynomialRing in a, b, c, d
            sage: {P:1} # indirect doctest
            {Boolean PolynomialRing in a, b, c, d: 1}"""
    def __reduce__(self) -> Any:
        """BooleanPolynomialRing.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 436)

        EXAMPLES::

            sage: P.<a,b> = BooleanPolynomialRing(2)
            sage: loads(dumps(P)) == P # indirect doctest
            True"""

class BooleanPolynomialVector:
    """BooleanPolynomialVector(I=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5960)

    A vector of boolean polynomials.

    EXAMPLES::

        sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
        sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
        sage: l = [B.random_element() for _ in range(3)]
        sage: v = BooleanPolynomialVector(l)
        sage: len(v)
        3
        sage: all(vi.parent() is B for vi in v)
        True"""
    @overload
    def __init__(self, I=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5975)

                Create a new :class:`BooleanPolynomialVector`.

                INPUT:

                - ``I`` -- list of boolean polynomials

                EXAMPLES::

                    sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
                    sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
                    sage: l = [B.random_element() for _ in range(3)]
                    sage: v = BooleanPolynomialVector(l)
                    sage: len(v)
                    3
                    sage: all(vi.parent() is B for vi in v)
                    True
        """
    @overload
    def __init__(self, l) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5975)

                Create a new :class:`BooleanPolynomialVector`.

                INPUT:

                - ``I`` -- list of boolean polynomials

                EXAMPLES::

                    sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
                    sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
                    sage: l = [B.random_element() for _ in range(3)]
                    sage: v = BooleanPolynomialVector(l)
                    sage: len(v)
                    3
                    sage: all(vi.parent() is B for vi in v)
                    True
        """
    def append(self, el) -> Any:
        """BooleanPolynomialVector.append(self, el)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6089)

        Append the element ``el`` to this vector.

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: v = BooleanPolynomialVector()
            sage: entries = []
            sage: for i in range(5):
            ....:   entries.append(B.random_element())
            ....:   v.append(entries[-1])

            sage: list(v) == entries
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """BooleanPolynomialVector.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6031)

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: l = [B.random_element() for _ in range(3)]
            sage: v = BooleanPolynomialVector(l)
            sage: len(v)
            3
            sage: v[-1] == v[2]
            True
            sage: v[3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: v['a']
            Traceback (most recent call last):
            ...
            TypeError: 'str' object cannot be interpreted as an i..."""
    def __iter__(self) -> Any:
        """BooleanPolynomialVector.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6002)

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: l = [B.random_element() for _ in range(3)]
            sage: v = BooleanPolynomialVector(l)
            sage: list(iter(v)) == [v[0], v[1], v[2]]
            True"""
    def __len__(self) -> Any:
        """BooleanPolynomialVector.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6015)

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: l = [B.random_element() for _ in range(3)]
            sage: v = BooleanPolynomialVector()
            sage: len(v)
            0
            sage: v = BooleanPolynomialVector(l)
            sage: len(v)
            3"""
    def __setitem__(self, Py_ssize_ti, p) -> Any:
        """BooleanPolynomialVector.__setitem__(self, Py_ssize_t i, p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6059)

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: l = [B.random_element() for _ in range(3)]
            sage: v = BooleanPolynomialVector(l)
            sage: len(v)
            3
            sage: v[0] = a; v[0]
            a
            sage: v[-1] = b; v[-1]
            b
            sage: v[3] = c
            Traceback (most recent call last):
            ...
            IndexError"""

class BooleanPolynomialVectorIterator:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __iter__(self) -> Any:
        """BooleanPolynomialVectorIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6127)"""
    def __next__(self) -> Any:
        """BooleanPolynomialVectorIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6130)"""

class CCuddNavigator:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def constant(self) -> Any:
        """CCuddNavigator.constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5928)"""
    def else_branch(self) -> Any:
        """CCuddNavigator.else_branch(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5922)"""
    def terminal_one(self) -> Any:
        """CCuddNavigator.terminal_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5931)"""
    def then_branch(self) -> Any:
        """CCuddNavigator.then_branch(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5925)"""
    def value(self) -> Any:
        """CCuddNavigator.value(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5917)"""
    def __call__(self) -> Any:
        """CCuddNavigator.__call__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5914)"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """CCuddNavigator.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 5956)"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class FGLMStrategy:
    """FGLMStrategy(from_ring, to_ring, BooleanPolynomialVector vec)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6430)

    Strategy object for the FGLM algorithm to translate from one
    Groebner basis with respect to a term ordering A to another
    Groebner basis with respect to a term ordering B."""
    def __init__(self, from_ring, to_ring, BooleanPolynomialVectorvec) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6436)

                Execute the FGLM algorithm.

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import *
                    sage: B.<x,y,z> = BooleanPolynomialRing()
                    sage: x > y > z
                    True
                    sage: old_ring  = B
                    sage: new_ring = B.clone(ordering=lp)
                    sage: new_ring.gen(0) > new_ring.gen(1) > new_ring.gen(2)
                    True
                    sage: new_ring.gen(2) > new_ring.gen(1) > new_ring.gen(0)
                    False
                    sage: ideal = BooleanPolynomialVector([x+z, y+z])
                    sage: FGLMStrategy(old_ring, new_ring, ideal)
                    <sage.rings.polynomial.pbori.pbori.FGLMStrategy object at 0x...>

                Check that :issue:`13883` is fixed::

                    sage: nonreduced = BooleanPolynomialVector([x+z, x+y])
                    sage: FGLMStrategy(old_ring, new_ring, nonreduced) # optional - debug
                    Traceback (most recent call last):
                    ...
                    RuntimeError...
        """
    @overload
    def main(self) -> Any:
        """FGLMStrategy.main(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6483)

        Execute the FGLM algorithm.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: ideal = BooleanPolynomialVector([x+z, y+z])
            sage: list(ideal)
            [x + z, y + z]
            sage: old_ring = B
            sage: new_ring = B.clone(ordering=dp_asc)
            sage: list(FGLMStrategy(old_ring, new_ring, ideal).main())
            [y + x, z + x]"""
    @overload
    def main(self) -> Any:
        """FGLMStrategy.main(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6483)

        Execute the FGLM algorithm.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: ideal = BooleanPolynomialVector([x+z, y+z])
            sage: list(ideal)
            [x + z, y + z]
            sage: old_ring = B
            sage: new_ring = B.clone(ordering=dp_asc)
            sage: list(FGLMStrategy(old_ring, new_ring, ideal).main())
            [y + x, z + x]"""

class GroebnerStrategy:
    """GroebnerStrategy(param)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6502)

    A Groebner strategy is the main object to control the strategy for
    computing Groebner bases.

    .. NOTE::

      This class is mainly used internally."""
    reduction_strategy: reduction_strategy
    def __init__(self, param) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6511)

                INPUT:

                - ``param`` -- either ``None`` or a :class:`GroebnerStrategy` object

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
                    sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
                    sage: G = GroebnerStrategy(B)
                    sage: H = GroebnerStrategy(G)
                    sage: del G
                    sage: del H
        """
    def add_as_you_wish(self, BooleanPolynomialp) -> Any:
        """GroebnerStrategy.add_as_you_wish(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6594)

        Add a new generator but let the strategy object decide whether
        to perform immediate interreduction.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: gbs = GroebnerStrategy(B)
            sage: gbs.add_as_you_wish(a + b)
            sage: list(gbs)
            [a + b]
            sage: gbs.add_as_you_wish(a + c)

        Note that nothing happened immediately but that the generator
        was indeed added::

            sage: list(gbs)
            [a + b]

            sage: gbs.symmGB_F2()
            sage: list(gbs)
            [a + c, b + c]"""
    def add_generator(self, BooleanPolynomialp) -> Any:
        """GroebnerStrategy.add_generator(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6567)

        Add a new generator.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: gbs = GroebnerStrategy(B)
            sage: gbs.add_generator(a + b)
            sage: list(gbs)
            [a + b]
            sage: gbs.add_generator(a + c)
            Traceback (most recent call last):
            ...
            ValueError: strategy already contains a polynomial with same lead"""
    def add_generator_delayed(self, BooleanPolynomialp) -> Any:
        """GroebnerStrategy.add_generator_delayed(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6539)

        Add a new generator but do not perform interreduction
        immediately.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: gbs = GroebnerStrategy(B)
            sage: gbs.add_generator(a + b)
            sage: list(gbs)
            [a + b]
            sage: gbs.add_generator_delayed(a + c)
            sage: list(gbs)
            [a + b]

            sage: list(gbs.all_generators())
            [a + b, a + c]"""
    @overload
    def all_generators(self) -> Any:
        """GroebnerStrategy.all_generators(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6767)

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: gbs = GroebnerStrategy(B)
            sage: gbs.add_as_you_wish(a + b)
            sage: list(gbs)
            [a + b]
            sage: gbs.add_as_you_wish(a + c)

            sage: list(gbs)
            [a + b]

            sage: list(gbs.all_generators())
            [a + b, a + c]"""
    @overload
    def all_generators(self) -> Any:
        """GroebnerStrategy.all_generators(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6767)

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: gbs = GroebnerStrategy(B)
            sage: gbs.add_as_you_wish(a + b)
            sage: list(gbs)
            [a + b]
            sage: gbs.add_as_you_wish(a + c)

            sage: list(gbs)
            [a + b]

            sage: list(gbs.all_generators())
            [a + b, a + c]"""
    def all_spolys_in_next_degree(self) -> Any:
        """GroebnerStrategy.all_spolys_in_next_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6746)"""
    def clean_top_by_chain_criterion(self) -> Any:
        """GroebnerStrategy.clean_top_by_chain_criterion(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6639)"""
    @overload
    def contains_one(self) -> Any:
        """GroebnerStrategy.contains_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6654)

        Return ``True`` if 1 is in the generating system.

        EXAMPLES:

        We construct an example which contains ``1`` in the ideal
        spanned by the generators but not in the set of generators::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: gb = GroebnerStrategy(B)
            sage: gb.add_generator(a*c + a*f + d*f + d + f)
            sage: gb.add_generator(b*c + b*e + c + d + 1)
            sage: gb.add_generator(a*f + a + c + d + 1)
            sage: gb.add_generator(a*d + a*e + b*e + c + f)
            sage: gb.add_generator(b*d + c + d*f + e + f)
            sage: gb.add_generator(a*b + b + c*e + e + 1)
            sage: gb.add_generator(a + b + c*d + c*e + 1)
            sage: gb.contains_one()
            False

        Still, we have that::

            sage: from sage.rings.polynomial.pbori import groebner_basis
            sage: groebner_basis(gb)
            [1]"""
    @overload
    def contains_one(self) -> Any:
        """GroebnerStrategy.contains_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6654)

        Return ``True`` if 1 is in the generating system.

        EXAMPLES:

        We construct an example which contains ``1`` in the ideal
        spanned by the generators but not in the set of generators::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: gb = GroebnerStrategy(B)
            sage: gb.add_generator(a*c + a*f + d*f + d + f)
            sage: gb.add_generator(b*c + b*e + c + d + 1)
            sage: gb.add_generator(a*f + a + c + d + 1)
            sage: gb.add_generator(a*d + a*e + b*e + c + f)
            sage: gb.add_generator(b*d + c + d*f + e + f)
            sage: gb.add_generator(a*b + b + c*e + e + 1)
            sage: gb.add_generator(a + b + c*d + c*e + 1)
            sage: gb.contains_one()
            False

        Still, we have that::

            sage: from sage.rings.polynomial.pbori import groebner_basis
            sage: groebner_basis(gb)
            [1]"""
    @overload
    def faugere_step_dense(self, BooleanPolynomialVectorv) -> Any:
        """GroebnerStrategy.faugere_step_dense(self, BooleanPolynomialVector v)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6684)

        Reduces a vector of polynomials using linear algebra.

        INPUT:

        - ``v`` -- boolean polynomial vector

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: gb = GroebnerStrategy(B)
            sage: gb.add_generator(a*c + a*f + d*f + d + f)
            sage: gb.add_generator(b*c + b*e + c + d + 1)
            sage: gb.add_generator(a*f + a + c + d + 1)
            sage: gb.add_generator(a*d + a*e + b*e + c + f)
            sage: gb.add_generator(b*d + c + d*f + e + f)
            sage: gb.add_generator(a*b + b + c*e + e + 1)
            sage: gb.add_generator(a + b + c*d + c*e + 1)

            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: V= BooleanPolynomialVector([b*d, a*b])
            sage: list(gb.faugere_step_dense(V))
            [b + c*e + e + 1, c + d*f + e + f]"""
    @overload
    def faugere_step_dense(self, V) -> Any:
        """GroebnerStrategy.faugere_step_dense(self, BooleanPolynomialVector v)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6684)

        Reduces a vector of polynomials using linear algebra.

        INPUT:

        - ``v`` -- boolean polynomial vector

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: gb = GroebnerStrategy(B)
            sage: gb.add_generator(a*c + a*f + d*f + d + f)
            sage: gb.add_generator(b*c + b*e + c + d + 1)
            sage: gb.add_generator(a*f + a + c + d + 1)
            sage: gb.add_generator(a*d + a*e + b*e + c + f)
            sage: gb.add_generator(b*d + c + d*f + e + f)
            sage: gb.add_generator(a*b + b + c*e + e + 1)
            sage: gb.add_generator(a + b + c*d + c*e + 1)

            sage: from sage.rings.polynomial.pbori.pbori import BooleanPolynomialVector
            sage: V= BooleanPolynomialVector([b*d, a*b])
            sage: list(gb.faugere_step_dense(V))
            [b + c*e + e + 1, c + d*f + e + f]"""
    def implications(self, i) -> Any:
        '''GroebnerStrategy.implications(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6627)

        Compute "useful" implied polynomials of ``i``-th generator,
        and add them to the strategy, if it finds any.

        INPUT:

        - ``i`` -- an index'''
    def ll_reduce_all(self) -> Any:
        """GroebnerStrategy.ll_reduce_all(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6754)

        Use the built-in ll-encoded :class:`BooleSet` of polynomials
        with linear lexicographical leading term, which coincides with
        leading term in current ordering, to reduce the tails of all
        polynomials in the strategy."""
    def minimalize(self) -> Any:
        """GroebnerStrategy.minimalize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6713)

        Return a vector of all polynomials with minimal leading terms.

        .. NOTE::

           Use this function if strat contains a GB."""
    def minimalize_and_tail_reduce(self) -> Any:
        """GroebnerStrategy.minimalize_and_tail_reduce(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6724)

        Return a vector of all polynomials with minimal leading terms
        and do tail reductions.

        .. NOTE::

          Use that if strat contains a GB and you want a reduced GB."""
    def next_spoly(self) -> Any:
        """GroebnerStrategy.next_spoly(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6763)"""
    def nf(self, BooleanPolynomialp) -> Any:
        """GroebnerStrategy.nf(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6827)

        Compute the normal form of ``p`` with respect to the
        generating set.

        INPUT:

        - ``p`` -- boolean polynomial

        EXAMPLES::

            sage: P = PolynomialRing(GF(2),10, 'x')
            sage: B = BooleanPolynomialRing(10,'x')
            sage: I = sage.rings.ideal.Cyclic(P)
            sage: I = B.ideal([B(f) for f in I.gens()])
            sage: gb = I.groebner_basis()

            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy

            sage: G = GroebnerStrategy(B)
            sage: _ = [G.add_generator(f) for f in gb]
            sage: G.nf(gb[0])
            0
            sage: G.nf(gb[0] + 1)
            1
            sage: G.nf(gb[0]*gb[1])
            0
            sage: G.nf(gb[0]*B.gen(1))
            0

        .. NOTE::

          The result is only canonical if the generating set is a
          Groebner basis."""
    def npairs(self) -> Any:
        """GroebnerStrategy.npairs(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6736)"""
    def select(self, BooleanMonomialm) -> Any:
        """GroebnerStrategy.select(self, BooleanMonomial m)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6864)

        Return the index of the generator which can reduce the
        monomial ``m``.

        INPUT:

        - ``m`` -- a :class:`BooleanMonomial`

        EXAMPLES::

            sage: B.<a,b,c,d,e> = BooleanPolynomialRing()
            sage: f = B.random_element()
            sage: g = B.random_element()
            sage: while g.lt() == f.lt():
            ....:     g = B.random_element()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: strat = GroebnerStrategy(B)
            sage: strat.add_generator(f)
            sage: strat.add_generator(g)
            sage: strat.select(f.lm())
            0
            sage: strat.select(g.lm())
            1
            sage: strat.select(e.lm())
            -1"""
    def small_spolys_in_next_degree(self, doublef, intn) -> Any:
        """GroebnerStrategy.small_spolys_in_next_degree(self, double f, int n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6750)"""
    def some_spolys_in_next_degree(self, n) -> Any:
        """GroebnerStrategy.some_spolys_in_next_degree(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6742)"""
    def suggest_plugin_variable(self) -> Any:
        """GroebnerStrategy.suggest_plugin_variable(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6788)"""
    def symmGB_F2(self) -> Any:
        """GroebnerStrategy.symmGB_F2(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6642)

        Compute a Groebner basis for the generating system.

        .. NOTE::

          This implementation is out of date, but it will revived at
          some point in time. Use the ``groebner_basis()`` function
          instead."""
    def top_sugar(self) -> Any:
        """GroebnerStrategy.top_sugar(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6739)"""
    def variable_has_value(self, intv) -> Any:
        """GroebnerStrategy.variable_has_value(self, int v)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6791)

        Compute whether there exists some polynomial of the form
        `v+c` in the Strategy -- where ``c`` is a constant -- in the
        list of generators.

        INPUT:

        - ``v`` -- the index of a variable

        EXAMPLES::

            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy
            sage: gb = GroebnerStrategy(B)
            sage: gb.add_generator(a*c + a*f + d*f + d + f)
            sage: gb.add_generator(b*c + b*e + c + d + 1)
            sage: gb.add_generator(a*f + a + c + d + 1)
            sage: gb.add_generator(a*d + a*e + b*e + c + f)
            sage: gb.add_generator(b*d + c + d*f + e + f)
            sage: gb.add_generator(a*b + b + c*e + e + 1)
            sage: gb.variable_has_value(0)
            False

            sage: from sage.rings.polynomial.pbori import groebner_basis
            sage: g = groebner_basis(gb)
            sage: list(g)
            [a, b + 1, c + 1, d, e + 1, f]

            sage: gb = GroebnerStrategy(B)
            sage: _ = [gb.add_generator(f) for f in g]
            sage: gb.variable_has_value(0)
            True"""
    def __delattr__(self, name):
        """Implement delattr(self, name)."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """GroebnerStrategy.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6915)"""
    def __len__(self) -> Any:
        """GroebnerStrategy.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6893)

        Return the number of generators.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.rings.polynomial.pbori.pbori import GroebnerStrategy

            sage: G = GroebnerStrategy(B)
            sage: G.add_as_you_wish(a)
            sage: len(G)
            1
            sage: G.add_as_you_wish(b)
            sage: len(G)
            2
            sage: G.add_as_you_wish(b + 1)
            sage: len(G)
            2"""
    def __setattr__(self, name, val) -> Any:
        """GroebnerStrategy.__setattr__(self, name, val)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6951)"""

class MonomialConstruct:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4687)

        Implement PolyBoRi's ``Monomial()`` constructor.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __call__(self, x) -> Any:
        """MonomialConstruct.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4691)

        Construct a new :class:`BooleanMonomial` or return ``x`` if
        it is a :class:`BooleanMonomial` already.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: MonomialConstruct()(B)
            1
            sage: MonomialConstruct()(a.lm())
            a
            sage: MonomialConstruct()(a)
            a"""

class MonomialFactory:
    """MonomialFactory(BooleanPolynomialRing ring=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7955)

    Implement PolyBoRi's ``Monomial()`` constructor. If a ring is given is
    can be used as a  Monomial factory for the given ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: fac = MonomialFactory()
            sage: fac = MonomialFactory(B)"""
    def __init__(self, BooleanPolynomialRingring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7967)

                Initialized a polynomial factory of ring is given.
                Otherwise it initializes a plain constructor.

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import *
                    sage: B.<a,b,c> = BooleanPolynomialRing()
                    sage: MonomialFactory()(B)
                    1
                    sage: MonomialFactory()(a.lm())
                    a
                    sage: MonomialFactory()(a)
                    a
                    sage: MonomialFactory(B)()
                    1
        """
    def __call__(self, arg=...) -> Any:
        """MonomialFactory.__call__(self, arg=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7989)

        Generates a Boolean monomial from argument.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: MonomialFactory()(B)
            1
            sage: MonomialFactory()(a.lm())
            a
            sage: MonomialFactory()(a)
            a
            sage: MonomialFactory(B)()
            1"""

class PolynomialConstruct:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4636)

        Implement PolyBoRi's ``Polynomial()`` constructor.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def lead(self, x) -> Any:
        """PolynomialConstruct.lead(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4640)

        Return the leading monomial of boolean polynomial ``x``, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialConstruct().lead(a)
            a"""
    @overload
    def lead(self, a) -> Any:
        """PolynomialConstruct.lead(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4640)

        Return the leading monomial of boolean polynomial ``x``, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialConstruct().lead(a)
            a"""
    def __call__(self, x, ring=...) -> Any:
        """PolynomialConstruct.__call__(self, x, ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4654)

        Construct a new :class:`BooleanPolynomial` or return ``x`` if
        it is a :class:`BooleanPolynomial` already.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialConstruct()(1, B)
            1
            sage: PolynomialConstruct()(a)
            a"""

class PolynomialFactory:
    """PolynomialFactory(BooleanPolynomialRing ring=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 8028)

    Implement PolyBoRi's ``Polynomial()`` constructor and
    a polynomial factory for given rings."""
    def __init__(self, BooleanPolynomialRingring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 8033)

                Construct a polynomial factory if ring is given,
                or plain constructor otherwise.

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import *
                    sage: B.<a,b,c> = BooleanPolynomialRing()
                    sage: fac = PolynomialFactory()
        """
    @overload
    def lead(self, x) -> Any:
        """PolynomialFactory.lead(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 8048)

        Return the leading monomial of boolean polynomial ``x``, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialFactory().lead(a)
            a"""
    @overload
    def lead(self, a) -> Any:
        """PolynomialFactory.lead(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 8048)

        Return the leading monomial of boolean polynomial ``x``, with
        respect to the order of parent ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialFactory().lead(a)
            a"""
    def __call__(self, arg, ring=...) -> Any:
        """PolynomialFactory.__call__(self, arg, ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 8062)

        Construct a new :class:`BooleanPolynomial` or return ``arg`` if
        it is a :class:`BooleanPolynomial` already.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: PolynomialFactory()(1, B)
            1
            sage: PolynomialFactory()(a)
            a
            sage: PolynomialFactory(B)(1)
            1"""

class ReductionStrategy:
    """ReductionStrategy(ring)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6153)

    Functions and options for boolean polynomial reduction."""
    def __init__(self, ring) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6157)

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import *
                    sage: B.<x,y> = BooleanPolynomialRing()
                    sage: red = ReductionStrategy(B)
                    sage: del red
        """
    @overload
    def add_generator(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.add_generator(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6169)

        Add the new generator ``p`` to this strategy.

        INPUT:

        - ``p`` -- boolean polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x)
            sage: [f.p for f in red]
            [x]

        TESTS:

        Check if :issue:`8966` is fixed::

            sage: red = ReductionStrategy(B)
            sage: red.add_generator(None)
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def add_generator(self, x) -> Any:
        """ReductionStrategy.add_generator(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6169)

        Add the new generator ``p`` to this strategy.

        INPUT:

        - ``p`` -- boolean polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x)
            sage: [f.p for f in red]
            [x]

        TESTS:

        Check if :issue:`8966` is fixed::

            sage: red = ReductionStrategy(B)
            sage: red.add_generator(None)
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    @overload
    def add_generator(self, _None) -> Any:
        """ReductionStrategy.add_generator(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6169)

        Add the new generator ``p`` to this strategy.

        INPUT:

        - ``p`` -- boolean polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x)
            sage: [f.p for f in red]
            [x]

        TESTS:

        Check if :issue:`8966` is fixed::

            sage: red = ReductionStrategy(B)
            sage: red.add_generator(None)
            Traceback (most recent call last):
            ...
            TypeError: argument must be a BooleanPolynomial"""
    def can_rewrite(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.can_rewrite(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6273)

        Return ``True`` if ``p`` can be reduced by the generators of
        this strategy.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(a*b + c + 1)
            sage: red.add_generator(b*c + d + 1)
            sage: red.can_rewrite(a*b + a)
            True
            sage: red.can_rewrite(b + c)
            False
            sage: red.can_rewrite(a*d + b*c + d + 1)
            True"""
    def cheap_reductions(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.cheap_reductions(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6294)

        Perform 'cheap' reductions on ``p``.

        INPUT:

        - ``p`` -- boolean polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c,d> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(a*b + c + 1)
            sage: red.add_generator(b*c + d + 1)
            sage: red.add_generator(a)
            sage: red.cheap_reductions(a*b + a)
            0
            sage: red.cheap_reductions(b + c)
            b + c
            sage: red.cheap_reductions(a*d + b*c + d + 1)
            b*c + d + 1"""
    def head_normal_form(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.head_normal_form(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6246)

        Compute the normal form of ``p`` with respect to the
        generators of this strategy but do not perform tail any
        reductions.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.opt_red_tail = True
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(y*z + z)

            sage: red.head_normal_form(x + y*z)
            y + z + 1

            sage: red.nf(x + y*z)
            y + z + 1"""
    @overload
    def nf(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.nf(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6202)

        Compute the normal form of ``p`` w.r.t. to the generators of
        this reduction strategy object.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(y*z + z)
            sage: red.nf(x)
            y + 1

            sage: red.nf(y*z + x)
            y + z + 1"""
    @overload
    def nf(self, x) -> Any:
        """ReductionStrategy.nf(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6202)

        Compute the normal form of ``p`` w.r.t. to the generators of
        this reduction strategy object.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(y*z + z)
            sage: red.nf(x)
            y + 1

            sage: red.nf(y*z + x)
            y + z + 1"""
    @overload
    def reduced_normal_form(self, BooleanPolynomialp) -> Any:
        """ReductionStrategy.reduced_normal_form(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6222)

        Compute the normal form of ``p`` with respect to the
        generators of this strategy and perform tail reductions.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(y*z + z)
            sage: red.reduced_normal_form(x)
            y + 1

            sage: red.reduced_normal_form(y*z + x)
            y + z + 1"""
    @overload
    def reduced_normal_form(self, x) -> Any:
        """ReductionStrategy.reduced_normal_form(self, BooleanPolynomial p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6222)

        Compute the normal form of ``p`` with respect to the
        generators of this strategy and perform tail reductions.

        INPUT:

        - ``p`` -- a polynomial

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(y*z + z)
            sage: red.reduced_normal_form(x)
            y + 1

            sage: red.reduced_normal_form(y*z + x)
            y + z + 1"""
    def __delattr__(self, name):
        """Implement delattr(self, name)."""
    def __getitem__(self, Py_ssize_ti) -> Any:
        """ReductionStrategy.__getitem__(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6418)"""
    def __len__(self) -> Any:
        """ReductionStrategy.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6402)

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<x,y,z> = BooleanPolynomialRing()
            sage: red = ReductionStrategy(B)
            sage: red.opt_red_tail = True
            sage: red.add_generator(x + y + 1)
            sage: red.add_generator(x*y + y)
            sage: red.add_generator(y*z + z)
            sage: len(red)
            3"""
    def __setattr__(self, name, val) -> Any:
        """ReductionStrategy.__setattr__(self, name, val)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 6389)"""

class VariableBlock:
    """VariableBlock(int size, int start_index, int offset, bool reverse, BooleanPolynomialRing ring)"""
    def __init__(self, intsize, intstart_index, intoffset, boolreverse, BooleanPolynomialRingring) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7015)"""
    def __call__(self, inti) -> Any:
        """VariableBlock.__call__(self, int i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7025)"""

class VariableConstruct:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4725)

        Implement PolyBoRi's ``Variable()`` constructor.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __call__(self, arg, ring=...) -> Any:
        """VariableConstruct.__call__(self, arg, ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 4729)

        Return a Variable for ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: VariableConstruct()(B)
            a
            sage: VariableConstruct()(0, B)
            a"""

class VariableFactory:
    """VariableFactory(BooleanPolynomialRing ring=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7907)
    Implements PolyBoRi's ``Variable()`` constructor and
        a variable factory for given ring """
    def __init__(self, BooleanPolynomialRingring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7911)

                Initialize variable factory, if ring is given.
                Otherwise it initializes a plain constructor

                EXAMPLES::

                    sage: from sage.rings.polynomial.pbori.pbori import *
                    sage: B.<a,b,c> = BooleanPolynomialRing()
                    sage: fac = VariableFactory()
                    sage: fac = VariableFactory(B)
        """
    def __call__(self, arg=..., ring=...) -> Any:
        """VariableFactory.__call__(self, arg=0, ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/pbori/pbori.pyx (starting at line 7927)

        Return a Variable for ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.pbori.pbori import *
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: VariableFactory()(B)
            a
            sage: VariableFactory()(0, B)
            a
            sage: VariableFactory(B)()
            a
            sage: VariableFactory(B)(0)
            a"""
