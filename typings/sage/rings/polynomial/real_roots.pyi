import _cython_3_2_1
from sage.arith.misc import binomial as binomial, factorial as factorial
from sage.categories.category import RDF as RDF, RIF as RIF, RR as RR, ZZ as ZZ
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.functional import denominator as denominator, numerator as numerator
from sage.misc.misc_c import prod as prod
from sage.misc.randstate import randstate as randstate
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar import AA as AA
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

bernstein_down: _cython_3_2_1.cython_function_or_method
bernstein_expand: _cython_3_2_1.cython_function_or_method
bernstein_up: _cython_3_2_1.cython_function_or_method
bitsize_doctest: _cython_3_2_1.cython_function_or_method
cl_maximum_root: _cython_3_2_1.cython_function_or_method
cl_maximum_root_first_lambda: _cython_3_2_1.cython_function_or_method
cl_maximum_root_local_max: _cython_3_2_1.cython_function_or_method
de_casteljau_doublevec: _cython_3_2_1.cython_function_or_method
de_casteljau_intvec: _cython_3_2_1.cython_function_or_method
degree_reduction_next_size: _cython_3_2_1.cython_function_or_method
dprod_imatrow_vec: _cython_3_2_1.cython_function_or_method
dr_cache: dict
get_realfield_rndu: _cython_3_2_1.cython_function_or_method
intvec_to_doublevec: _cython_3_2_1.cython_function_or_method
lmap: linear_map
max_abs_doublevec: _cython_3_2_1.cython_function_or_method
max_bitsize_intvec_doctest: _cython_3_2_1.cython_function_or_method
maximum_root_first_lambda: _cython_3_2_1.cython_function_or_method
maximum_root_local_max: _cython_3_2_1.cython_function_or_method
min_max_delta_intvec: _cython_3_2_1.cython_function_or_method
min_max_diff_doublevec: _cython_3_2_1.cython_function_or_method
min_max_diff_intvec: _cython_3_2_1.cython_function_or_method
mk_context: _cython_3_2_1.cython_function_or_method
mk_ibpf: _cython_3_2_1.cython_function_or_method
mk_ibpi: _cython_3_2_1.cython_function_or_method
precompute_degree_reduction_cache: _cython_3_2_1.cython_function_or_method
pseudoinverse: _cython_3_2_1.cython_function_or_method
rational_root_bounds: _cython_3_2_1.cython_function_or_method
real_roots: _cython_3_2_1.cython_function_or_method
realfield_rndu_cache: dict
relative_bounds: _cython_3_2_1.cython_function_or_method
reverse_intvec: _cython_3_2_1.cython_function_or_method
root_bounds: _cython_3_2_1.cython_function_or_method
scale_intvec_var: _cython_3_2_1.cython_function_or_method
split_for_targets: _cython_3_2_1.cython_function_or_method
subsample_vec_doctest: _cython_3_2_1.cython_function_or_method
taylor_shift1_intvec: _cython_3_2_1.cython_function_or_method
to_bernstein: _cython_3_2_1.cython_function_or_method
to_bernstein_warp: _cython_3_2_1.cython_function_or_method
wordsize_rational: _cython_3_2_1.cython_function_or_method

class PrecisionError(ValueError): ...

class bernstein_polynomial_factory:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2530)

        An abstract base class for bernstein_polynomial factories.  That
        is, elements of subclasses represent Bernstein polynomials
        (exactly), and are responsible for creating
        interval_bernstein_polynomial_integer approximations at arbitrary
        precision.

        Supports four methods, coeffs_bitsize(), bernstein_polynomial(),
        lsign(), and usign().  The coeffs_bitsize() method gives an
        integer approximation to the log2 of the max of the absolute
        values of the Bernstein coefficients.  The
        bernstein_polynomial(scale_log2) method gives an approximation
        where the maximum coefficient has approximately coeffs_bitsize() -
        scale_log2 bits.  The lsign() and usign() methods give the (exact)
        sign of the first and last coefficient, respectively.
    """
    def lsign(self) -> Any:
        """bernstein_polynomial_factory.lsign(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2555)

        Return the sign of the first coefficient of this
        Bernstein polynomial."""
    def usign(self) -> Any:
        """bernstein_polynomial_factory.usign(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2562)

        Return the sign of the last coefficient of this
        Bernstein polynomial."""

class bernstein_polynomial_factory_ar(bernstein_polynomial_factory):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2734)

        This class holds an exact Bernstein polynomial (represented as a
        list of algebraic real coefficients), and returns
        arbitrarily-precise interval approximations of this polynomial on
        demand.
    """
    def __init__(self, poly, neg) -> Any:
        """bernstein_polynomial_factory_ar.__init__(self, poly, neg)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2742)

        Initialize a ``bernstein_polynomial_factory_ar``,
        given a polynomial with algebraic real coefficients.
        If neg is True, then gives the Bernstein polynomial for
        the negative half-line; if neg is False, the positive.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: x = polygen(AA)
            sage: p = (x - 1) * (x - sqrt(AA(2))) * (x - 2)
            sage: bernstein_polynomial_factory_ar(p, False)
            degree 3 Bernstein factory with algebraic real coefficients"""
    def bernstein_polynomial(self, scale_log2) -> Any:
        """bernstein_polynomial_factory_ar.bernstein_polynomial(self, scale_log2)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2802)

        Compute an interval_bernstein_polynomial_integer that approximates
        this polynomial, using the given scale_log2.  (Smaller scale_log2
        values give more accurate approximations.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: x = polygen(AA)
            sage: p = (x - 1) * (x - sqrt(AA(2))) * (x - 2)
            sage: bpf = bernstein_polynomial_factory_ar(p, False)
            sage: print(bpf.bernstein_polynomial(0))
            degree 3 IBP with 2-bit coefficients
            sage: bpf.bernstein_polynomial(-20)
            <IBP: ((-2965821, 2181961, -1542880, 1048576) + [0 .. 1)) * 2^-20>
            sage: bpf = bernstein_polynomial_factory_ar(p, True)
            sage: bpf.bernstein_polynomial(-20)
            <IBP: ((-2965821, -2181962, -1542880, -1048576) + [0 .. 1)) * 2^-20>
            sage: p = x^2 - 1
            sage: bpf = bernstein_polynomial_factory_ar(p, False)
            sage: bpf.bernstein_polynomial(-10)
            <IBP: ((-1024, 0, 1024) + [0 .. 1)) * 2^-10>"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ar.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2787)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: x = polygen(AA)
            sage: p = (x - 1) * (x - sqrt(AA(2))) * (x - 2)
            sage: bernstein_polynomial_factory_ar(p, False).coeffs_bitsize()
            1"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ar.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2787)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: x = polygen(AA)
            sage: p = (x - 1) * (x - sqrt(AA(2))) * (x - 2)
            sage: bernstein_polynomial_factory_ar(p, False).coeffs_bitsize()
            1"""

class bernstein_polynomial_factory_intlist(bernstein_polynomial_factory):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2570)

        This class holds an exact Bernstein polynomial (represented
        as a list of integer coefficients), and returns arbitrarily-precise
        interval approximations of this polynomial on demand.
    """
    def __init__(self, coeffs) -> Any:
        """bernstein_polynomial_factory_intlist.__init__(self, coeffs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2577)

        Initialize a ``bernstein_polynomial_factory_intlist``,
        given a list of integer coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_intlist([1, 2, 3])
            degree 2 Bernstein factory with 2-bit integer coefficients"""
    def bernstein_polynomial(self, scale_log2) -> Any:
        """bernstein_polynomial_factory_intlist.bernstein_polynomial(self, scale_log2)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2618)

        Compute an interval_bernstein_polynomial_integer that approximates
        this polynomial, using the given scale_log2.  (Smaller scale_log2
        values give more accurate approximations.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bpf = bernstein_polynomial_factory_intlist([10, -20, 30, -40])
            sage: print(bpf.bernstein_polynomial(0))
            degree 3 IBP with 6-bit coefficients
            sage: bpf.bernstein_polynomial(20)
            <IBP: ((0, -1, 0, -1) + [0 .. 1)) * 2^20; lsign 1>
            sage: bpf.bernstein_polynomial(0)
            <IBP: (10, -20, 30, -40) + [0 .. 1)>
            sage: bpf.bernstein_polynomial(-20)
            <IBP: ((10485760, -20971520, 31457280, -41943040) + [0 .. 1)) * 2^-20>"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_intlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2603)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_intlist([1, 2, 3, -60000]).coeffs_bitsize()
            16"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_intlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2603)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_intlist([1, 2, 3, -60000]).coeffs_bitsize()
            16"""

class bernstein_polynomial_factory_ratlist(bernstein_polynomial_factory):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2649)

        This class holds an exact Bernstein polynomial (represented
        as a list of rational coefficients), and returns arbitrarily-precise
        interval approximations of this polynomial on demand.
    """
    def __init__(self, coeffs) -> Any:
        """bernstein_polynomial_factory_ratlist.__init__(self, coeffs)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2656)

        Initialize a ``bernstein_polynomial_factory_intlist``,
        given a list of rational coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_ratlist([1, 1/2, 1/3])
            degree 2 Bernstein factory with 0-bit rational coefficients"""
    def bernstein_polynomial(self, scale_log2) -> Any:
        """bernstein_polynomial_factory_ratlist.bernstein_polynomial(self, scale_log2)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2704)

        Compute an interval_bernstein_polynomial_integer that approximates
        this polynomial, using the given scale_log2.  (Smaller scale_log2
        values give more accurate approximations.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bpf = bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99])
            sage: print(bpf.bernstein_polynomial(0))
            degree 3 IBP with 3-bit coefficients
            sage: bpf.bernstein_polynomial(20)
            <IBP: ((0, -1, 0, -1) + [0 .. 1)) * 2^20; lsign 1>
            sage: bpf.bernstein_polynomial(0)
            <IBP: (0, -4, 2, -2) + [0 .. 1); lsign 1>
            sage: bpf.bernstein_polynomial(-20)
            <IBP: ((349525, -3295525, 2850354, -1482835) + [0 .. 1)) * 2^-20>"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ratlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2682)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_ratlist([1, 2, 3, -60000]).coeffs_bitsize()
            15
            sage: bernstein_polynomial_factory_ratlist([65535/65536]).coeffs_bitsize()
            -1
            sage: bernstein_polynomial_factory_ratlist([65536/65535]).coeffs_bitsize()
            1"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ratlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2682)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_ratlist([1, 2, 3, -60000]).coeffs_bitsize()
            15
            sage: bernstein_polynomial_factory_ratlist([65535/65536]).coeffs_bitsize()
            -1
            sage: bernstein_polynomial_factory_ratlist([65536/65535]).coeffs_bitsize()
            1"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ratlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2682)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_ratlist([1, 2, 3, -60000]).coeffs_bitsize()
            15
            sage: bernstein_polynomial_factory_ratlist([65535/65536]).coeffs_bitsize()
            -1
            sage: bernstein_polynomial_factory_ratlist([65536/65535]).coeffs_bitsize()
            1"""
    @overload
    def coeffs_bitsize(self) -> Any:
        """bernstein_polynomial_factory_ratlist.coeffs_bitsize(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2682)

        Compute the approximate log2 of the maximum of the absolute
        values of the coefficients.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bernstein_polynomial_factory_ratlist([1, 2, 3, -60000]).coeffs_bitsize()
            15
            sage: bernstein_polynomial_factory_ratlist([65535/65536]).coeffs_bitsize()
            -1
            sage: bernstein_polynomial_factory_ratlist([65536/65535]).coeffs_bitsize()
            1"""

class context:
    """context(do_logging, seed, wordsize)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 4318)

    A simple context class, which is passed through parts of the
    real root isolation algorithm to avoid global variables.

    Holds logging information, a random number generator, and
    the target machine wordsize."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, do_logging, seed, wordsize) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 4327)

                Initialize a context class.
        """
    def get_be_log(self) -> Any:
        """context.get_be_log(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 4375)"""
    def get_dc_log(self) -> Any:
        """context.get_dc_log(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 4372)"""

class interval_bernstein_polynomial:
    '''File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 168)

        An interval_bernstein_polynomial is an approximation to an exact
        polynomial.  This approximation is in the form of a Bernstein
        polynomial (a polynomial given as coefficients over a Bernstein
        basis) with interval coefficients.

        The Bernstein basis of degree n over the region [a .. b] is the
        set of polynomials

        .. MATH::

          \\binom{n}{k} (x-a)^k (b-x)^{n-k} / (b-a)^n

        for `0 \\le k \\le n`.

        A degree-n interval Bernstein polynomial P with its region [a .. b] can
        represent an exact polynomial p in two different ways: it can
        "contain" the polynomial or it can "bound" the polynomial.

        We say that P contains p if, when p is represented as a degree-n
        Bernstein polynomial over [a .. b], its coefficients are contained
        in the corresponding interval coefficients of P.  For instance,
        [0.9 .. 1.1]*x^2 (which is a degree-2 interval Bernstein polynomial
        over [0 .. 1]) contains x^2.

        We say that P bounds p if, for all a <= x <= b, there exists a
        polynomial p\' contained in P such that p(x) == p\'(x).  For instance,
        [0 .. 1]*x is a degree-1 interval Bernstein polynomial which bounds
        x^2 over [0 .. 1].

        If P contains p, then P bounds p; but the converse is not necessarily
        true.  In particular, if n < m, it is possible for a degree-n interval
        Bernstein polynomial to bound a degree-m polynomial; but it cannot
        contain the polynomial.

        In the case where P bounds p, we maintain extra information, the
        "slope error".  We say that P (over [a .. b]) bounds p with a
        slope error of E (where E is an interval) if there is a polynomial
        p\' contained in P such that the derivative of (p - p\') is bounded
        by E in the range [a .. b].  If P bounds p with a slope error of 0
        then P contains p.

        (Note that "contains" and "bounds" are not standard terminology;
        I just made them up.)

        Interval Bernstein polynomials are useful in finding real roots
        because of the following properties:

        - Given an exact real polynomial p, we can compute an interval Bernstein
          polynomial over an arbitrary region containing p.

        - Given an interval Bernstein polynomial P over [a .. c], where a < b < c,
          we can compute interval Bernstein polynomials P1 over [a .. b] and P2
          over [b .. c], where P1 and P2 contain (or bound) all polynomials that P
          contains (or bounds).

        - Given a degree-n interval Bernstein polynomial P over [a .. b], and m <
          n, we can compute a degree-m interval Bernstein polynomial P\' over [a ..
          b] that bounds all polynomials that P bounds.

        - It is sometimes possible to prove that no polynomial bounded by P over [a
          .. b] has any roots in [a .. b].  (Roughly, this is possible when no
          polynomial contained by P has any complex roots near the line segment [a
          .. b], where "near" is defined relative to the length b-a.)

        - It is sometimes possible to prove that every polynomial bounded by P over
          [a .. b] with slope error E has exactly one root in [a .. b].  (Roughly,
          this is possible when every polynomial contained by P over [a .. b] has
          exactly one root in [a .. b], there are no other complex roots near the
          line segment [a .. b], and every polynomial contained in P has a
          derivative which is bounded away from zero over [a .. b] by an amount
          which is large relative to E.)

        - Starting from a sufficiently precise interval Bernstein polynomial, it is
          always possible to split it into polynomials which provably have 0 or 1
          roots (as long as your original polynomial has no multiple real roots).

        So a rough outline of a family of algorithms would be:

        - Given a polynomial p, compute a region [a .. b] in which any real roots
          must lie.
        - Compute an interval Bernstein polynomial P containing p over [a .. b].
        - Keep splitting P until you have isolated all the roots.  Optionally,
          reduce the degree or the precision of the interval Bernstein polynomials
          at intermediate stages (to reduce computation time).  If this seems not
          to be working, go back and try again with higher precision.

        Obviously, there are many details to be worked out to turn this
        into a full algorithm, like:

        - What initial precision is selected for computing P?
        - How do you decide when to reduce the degree of intermediate polynomials?
        - How do you decide when to reduce the precision of intermediate
          polynomials?
        - How do you decide where to split the interval Bernstein polynomial
          regions?
        - How do you decide when to give up and start over with higher precision?

        Each set of answers to these questions gives a different algorithm
        (potentially with very different performance characteristics), but all of
        them can use this ``interval_bernstein_polynomial`` class as their basic
        building block.

        To save computation time, all coefficients in an
        ``interval_bernstein_polynomial`` share the same interval width.
        (There is one exception: when creating an ``interval_bernstein_polynomial``,
        the first and last coefficients can be marked as "known positive"
        or "known negative".  This has some of the same effect as having
        a (potentially) smaller interval width for these two coefficients,
        although it does not affect de Casteljau splitting.)
        To allow for widely varying coefficient magnitudes, all
        coefficients in an interval_bernstein_polynomial are scaled
        by `2^n` (where `n` may be positive, negative, or zero).

        There are two representations for interval_bernstein_polynomials,
        integer and floating-point. These are the two subclasses of
        this class; ``interval_bernstein_polynomial`` itself is an abstract
        class.

        ``interval_bernstein_polynomial`` and its subclasses are not expected
        to be used outside this file.
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def region(self) -> Any:
        """interval_bernstein_polynomial.region(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 429)"""
    def region_width(self) -> Any:
        """interval_bernstein_polynomial.region_width(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 432)"""
    def try_rand_split(self, contextctx, logging_note) -> Any:
        """interval_bernstein_polynomial.try_rand_split(self, context ctx, logging_note)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 369)

        Compute a random split point r (using the random number generator
        embedded in ctx).  We require 1/4 <= r < 3/4 (to ensure that
        recursive algorithms make progress).

        Then, try doing a de Casteljau split of this polynomial at r, resulting
        in polynomials p1 and p2.  If we see that the sign of this polynomial
        is determined at r, then return (p1, p2, r); otherwise,
        return None.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: bp1, bp2, _ = bp.try_rand_split(mk_context(), None)
            sage: bp1
            <IBP: (50, 29, -27, -56, -11) + [0 .. 6) over [0 .. 43/64]>
            sage: bp2
            <IBP: (-11, 10, 49, 111, 200) + [0 .. 6) over [43/64 .. 1]>
            sage: bp1, bp2, _ = bp.try_rand_split(mk_context(seed=42), None)
            sage: bp1
            <IBP: (50, 32, -11, -41, -29) + [0 .. 6) over [0 .. 583/1024]>
            sage: bp2
            <IBP: (-29, -20, 13, 83, 200) + [0 .. 6) over [583/1024 .. 1]>
            sage: bp = mk_ibpf([0.5, 0.2, -0.9, -0.7, 0.99], neg_err=-0.1, pos_err=0.01)
            sage: bp1, bp2, _ = bp.try_rand_split(mk_context(), None)
            sage: bp1  # rel tol
            <IBP: (0.5, 0.2984375, -0.2642578125, -0.5511661529541015, -0.3145806974172592) + [-0.10000000000000069 .. 0.010000000000000677] over [0 .. 43/64]>
            sage: bp2  # rel tol
            <IBP: (-0.3145806974172592, -0.19903896331787108, 0.04135986328125002, 0.43546875, 0.99) + [-0.10000000000000069 .. 0.010000000000000677] over [43/64 .. 1]>"""
    def try_split(self, contextctx, logging_note) -> Any:
        """interval_bernstein_polynomial.try_split(self, context ctx, logging_note)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 340)

        Try doing a de Casteljau split of this polynomial at 1/2, resulting
        in polynomials p1 and p2.  If we see that the sign of this polynomial
        is determined at 1/2, then return (p1, p2, 1/2); otherwise,
        return None.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: bp1, bp2, _ = bp.try_split(mk_context(), None)
            sage: bp1
            <IBP: (50, 35, 0, -29, -31) + [0 .. 6) over [0 .. 1/2]>
            sage: bp2
            <IBP: (-31, -33, -8, 65, 200) + [0 .. 6) over [1/2 .. 1]>
            sage: bp = mk_ibpf([0.5, 0.2, -0.9, -0.7, 0.99], neg_err=-0.1, pos_err=0.01)
            sage: bp1, bp2, _ = bp.try_split(mk_context(), None)
            sage: bp1
            <IBP: (0.5, 0.35, 0.0, -0.2875, -0.369375) + [-0.10000000000000023 .. 0.010000000000000226] over [0 .. 1/2]>
            sage: bp2
            <IBP: (-0.369375, -0.45125, -0.3275, 0.14500000000000002, 0.99) + [-0.10000000000000023 .. 0.010000000000000226] over [1/2 .. 1]>"""
    def variations(self) -> Any:
        """interval_bernstein_polynomial.variations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 292)

        Consider a polynomial (written in either the normal power basis
        or the Bernstein basis).  Take its list of coefficients, omitting
        zeroes.  Count the number of positions in the list where the
        sign of one coefficient is opposite the sign of the next coefficient.

        This count is the number of sign variations of the polynomial.
        According to Descartes' rule of signs, the number of real
        roots of the polynomial (counted with multiplicity) in a
        certain interval is always less than or equal to the number of
        sign variations, and the difference is always even.  (If the
        polynomial is written in the power basis, the region is the
        positive reals; if the polynomial is written in the Bernstein
        basis over a particular region, then we count roots in that region.)

        In particular, a polynomial with no sign variations has no real
        roots in the region, and a polynomial with one sign variation
        has one real root in the region.

        In an interval Bernstein polynomial, we do not necessarily
        know the signs of the coefficients (if some of the coefficient
        intervals contain zero), so the polynomials contained by
        this interval polynomial may not all have the same number
        of sign variations.  However, we can compute a range of
        possible numbers of sign variations.

        This function returns the range, as a 2-tuple of integers."""

class interval_bernstein_polynomial_float(interval_bernstein_polynomial):
    """interval_bernstein_polynomial_float(Vector_real_double_dense coeffs, Rational lower, Rational upper, int lsign, int usign, double neg_err, double pos_err, int scale_log2, int level, RealIntervalFieldElement slope_err)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1335)

    This is the subclass of :class:`interval_bernstein_polynomial` where
    polynomial coefficients are represented using floating-point numbers.

    In the floating-point representation, each coefficient is represented
    as an IEEE double-precision float A, and the (shared) lower and
    upper interval widths E1 and E2.  These represent the coefficients
    (A+E1)*2^n <= c <= (A+E2)*2^n.

    Note that we always have E1 <= 0 <= E2.  Also, each floating-point
    coefficient has absolute value less than one.

    (Note that :func:`mk_ibpf` is a simple helper function for creating
    elements of :class:`interval_bernstein_polynomial_float` in doctests.)

    EXAMPLES::

        sage: from sage.rings.polynomial.real_roots import *
        sage: bp = mk_ibpf([0.1, 0.2, 0.3], pos_err=0.5); print(bp)
        degree 2 IBP with floating-point coefficients
        sage: bp
        <IBP: (0.1, 0.2, 0.3) + [0.0 .. 0.5]>
        sage: bp.variations()
        (0, 0)
        sage: bp = mk_ibpf([-0.3, -0.1, 0.1, -0.1, -0.3, -0.1],                         # needs sage.symbolic
        ....:              lower=1, upper=5/4, usign=1, pos_err=0.2,
        ....:              scale_log2=-3, level=2, slope_err=RIF(pi)); print(bp)
        degree 5 IBP with floating-point coefficients
        sage: bp                                                                        # needs sage.symbolic
        <IBP: ((-0.3, -0.1, 0.1, -0.1, -0.3, -0.1) + [0.0 .. 0.2]) * 2^-3
              over [1 .. 5/4]; usign 1; level 2; slope_err 3.141592653589794?>
        sage: bp.variations()                                                           # needs sage.symbolic
        (3, 3)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Vector_real_double_densecoeffs, Rationallower, Rationalupper, intlsign, intusign, doubleneg_err, doublepos_err, intscale_log2, intlevel, RealIntervalFieldElementslope_err) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1371)

                Initialize an interval_bernstein_polynomial_float.

                INPUT:

                - ``coeffs`` -- a coefficient vector for a polynomial in Bernstein form
                  (all coefficients must have absolute value less than one)
                - ``lower`` -- the lower bound of the region over which the Bernstein basis
                  is defined
                - ``upper`` -- the upper bound of the region over which the Bernstein basis
                  is defined
                - ``lsign`` -- the sign of the polynomial at lower, if known
                - ``usign`` -- the sign of the polynomial at upper, if known
                - ``neg_err`` -- the minimum error in the Bernstein coefficients
                - ``pos_err`` -- the maximum error in the Bernstein coefficients (so a
                  Bernstein coefficient x really represents the range [neg_err+x ..
                  pos_err+x]
                - ``scale_log2`` -- the log2 of the scaling factor for the Bernstein
                  coefficients
                - ``level`` -- the number of times we have performed degree reduction to
                  get this polynomial
                - ``slope_err`` -- the maximum extra error in the derivative of this
                  polynomial from degree reduction

                EXAMPLES::

                    sage: from sage.rings.polynomial.real_roots import *
                    sage: bp = interval_bernstein_polynomial_float(vector(RDF, [0.50, -0.30, -0.10]), -3/7, 4/7, 0, -1, -0.02, 0.17, 3, 2, RIF(10^-30))
                    sage: print(bp)
                    degree 2 IBP with floating-point coefficients
                    sage: bp
                    <IBP: ((0.5, -0.3, -0.1) + [-0.02 .. 0.17]) * 2^3 over [-3/7 .. 4/7]; usign -1; level 2; slope_err 1.0000000000000000?e-30>
        """
    def as_float(self) -> Any:
        """interval_bernstein_polynomial_float.as_float(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1642)"""
    def de_casteljau(self, contextctx, mid, msign=...) -> Any:
        """interval_bernstein_polynomial_float.de_casteljau(self, context ctx, mid, msign=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1562)

        Uses de Casteljau's algorithm to compute the representation
        of this polynomial in a Bernstein basis over new regions.

        INPUT:

        - ``mid`` -- where to split the Bernstein basis region; ``0 < mid < 1``
        - ``msign`` -- default 0 (unknown); the sign of this polynomial at ``mid``

        OUTPUT:

        - ``bp1``, ``bp2`` -- the new interval Bernstein polynomials
        - ``ok`` -- boolean; ``True`` if the sign of the original polynomial at
          ``mid`` is known

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: ctx = mk_context()
            sage: bp = mk_ibpf([0.5, 0.2, -0.9, -0.7, 0.99], neg_err=-0.1, pos_err=0.01)
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 1/2)
            sage: bp1
            <IBP: (0.5, 0.35, 0.0, -0.2875, -0.369375) + [-0.10000000000000023 .. 0.010000000000000226] over [0 .. 1/2]>
            sage: bp2
            <IBP: (-0.369375, -0.45125, -0.3275, 0.14500000000000002, 0.99) + [-0.10000000000000023 .. 0.010000000000000226] over [1/2 .. 1]>
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 2/3)
            sage: bp1 # rel tol 2e-16
            <IBP: (0.5, 0.30000000000000004, -0.2555555555555555, -0.5444444444444444, -0.32172839506172846) + [-0.10000000000000069 .. 0.010000000000000677] over [0 .. 2/3]>
            sage: bp2  # rel tol 3e-15
            <IBP: (-0.32172839506172846, -0.21037037037037046, 0.028888888888888797, 0.4266666666666666, 0.99) + [-0.10000000000000069 .. 0.010000000000000677] over [2/3 .. 1]>
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 7/39)
            sage: bp1  # rel tol
            <IBP: (0.5, 0.4461538461538461, 0.36653517422748183, 0.27328680523946786, 0.1765692706232836) + [-0.10000000000000069 .. 0.010000000000000677] over [0 .. 7/39]>
            sage: bp2  # rel tol
            <IBP: (0.1765692706232836, -0.26556803047927313, -0.7802038132807364, -0.3966666666666666, 0.99) + [-0.10000000000000069 .. 0.010000000000000677] over [7/39 .. 1]>"""
    def get_msb_bit(self) -> Any:
        """interval_bernstein_polynomial_float.get_msb_bit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1645)

        Return an approximation of the log2 of the maximum of the
        absolute values of the coefficients, as an integer."""
    @overload
    def slope_range(self) -> Any:
        """interval_bernstein_polynomial_float.slope_range(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1652)

        Compute a bound on the derivative of this polynomial, over its region.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpf([0.5, 0.2, -0.9, -0.7, 0.99], neg_err=-0.1, pos_err=0.01)
            sage: bp.slope_range().str(style='brackets')
            '[-4.8400000000000017 .. 7.2000000000000011]'"""
    @overload
    def slope_range(self) -> Any:
        """interval_bernstein_polynomial_float.slope_range(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 1652)

        Compute a bound on the derivative of this polynomial, over its region.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpf([0.5, 0.2, -0.9, -0.7, 0.99], neg_err=-0.1, pos_err=0.01)
            sage: bp.slope_range().str(style='brackets')
            '[-4.8400000000000017 .. 7.2000000000000011]'"""

class interval_bernstein_polynomial_integer(interval_bernstein_polynomial):
    """interval_bernstein_polynomial_integer(Vector_integer_dense coeffs, Rational lower, Rational upper, int lsign, int usign, int error, int scale_log2, int level, RealIntervalFieldElement slope_err)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 437)

    This is the subclass of :class:`interval_bernstein_polynomial` where
    polynomial coefficients are represented using integers.

    In this integer representation, each coefficient is represented by
    a GMP arbitrary-precision integer A, and a (shared) interval width
    E (which is a machine integer).  These represent the coefficients
    A*2^n <= c < (A+E)*2^n.

    (Note that :func:`mk_ibpi is a simple helper` function for creating
    elements of :class:`interval_bernstein_polynomial_integer` in doctests.)

    EXAMPLES::

        sage: from sage.rings.polynomial.real_roots import *
        sage: bp = mk_ibpi([1, 2, 3], error=5); print(bp)
        degree 2 IBP with 2-bit coefficients
        sage: bp
        <IBP: (1, 2, 3) + [0 .. 5)>
        sage: bp.variations()
        (0, 0)
        sage: bp = mk_ibpi([-3, -1, 1, -1, -3, -1], lower=1, upper=5/4, usign=1,        # needs sage.symbolic
        ....:              error=2, scale_log2=-3, level=2, slope_err=RIF(pi)); print(bp)
        degree 5 IBP with 2-bit coefficients
        sage: bp                                                                        # needs sage.symbolic
        <IBP: ((-3, -1, 1, -1, -3, -1) + [0 .. 2)) * 2^-3 over [1 .. 5/4]; usign 1;
              level 2; slope_err 3.141592653589794?>
        sage: bp.variations()                                                           # needs sage.symbolic
        (3, 3)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Vector_integer_densecoeffs, Rationallower, Rationalupper, intlsign, intusign, interror, intscale_log2, intlevel, RealIntervalFieldElementslope_err) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 469)

                Initialize an interval_bernstein_polynomial_integer.

                INPUT:

                - ``coeffs`` -- a coefficient vector for a polynomial in Bernstein form
                - ``lower`` -- the lower bound of the region over which the Bernstein basis is defined
                - ``upper`` -- the upper bound of the region over which the Bernstein basis is defined
                - ``lsign`` -- the sign of the polynomial at lower, if known
                - ``usign`` -- the sign of the polynomial at upper, if known
                - ``error`` -- the maximum error in the Bernstein coefficients
                - ``scale_log2`` -- the log2 of the scaling factor for the Bernstein coefficients
                - ``level`` -- the number of times we have performed degree reduction to get this polynomial
                - ``slope_err`` -- the maximum extra error in the derivative of this polynomial from degree reduction

                EXAMPLES::

                    sage: from sage.rings.polynomial.real_roots import *
                    sage: bp = interval_bernstein_polynomial_integer(vector(ZZ, [50, -30, -10]), -3/7, 4/7, 0, -1, 17, 3, 2, RIF(10^-30))
                    sage: print(bp)
                    degree 2 IBP with 6-bit coefficients
                    sage: bp
                    <IBP: ((50, -30, -10) + [0 .. 17)) * 2^3 over [-3/7 .. 4/7]; usign -1; level 2; slope_err 1.0000000000000000?e-30>
        """
    @overload
    def as_float(self) -> Any:
        """interval_bernstein_polynomial_integer.as_float(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 758)

        Compute an interval_bernstein_polynomial_float which contains
        (or bounds) all the polynomials this interval polynomial
        contains (or bounds).

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: print(bp.as_float())
            degree 4 IBP with floating-point coefficients
            sage: bp.as_float()
            <IBP: ((0.1953125, 0.078125, -0.3515625, -0.2734375, 0.78125) + [-1.1275702593849246e-16 .. 0.01953125000000017]) * 2^8>"""
    @overload
    def as_float(self) -> Any:
        """interval_bernstein_polynomial_integer.as_float(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 758)

        Compute an interval_bernstein_polynomial_float which contains
        (or bounds) all the polynomials this interval polynomial
        contains (or bounds).

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: print(bp.as_float())
            degree 4 IBP with floating-point coefficients
            sage: bp.as_float()
            <IBP: ((0.1953125, 0.078125, -0.3515625, -0.2734375, 0.78125) + [-1.1275702593849246e-16 .. 0.01953125000000017]) * 2^8>"""
    @overload
    def as_float(self) -> Any:
        """interval_bernstein_polynomial_integer.as_float(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 758)

        Compute an interval_bernstein_polynomial_float which contains
        (or bounds) all the polynomials this interval polynomial
        contains (or bounds).

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: print(bp.as_float())
            degree 4 IBP with floating-point coefficients
            sage: bp.as_float()
            <IBP: ((0.1953125, 0.078125, -0.3515625, -0.2734375, 0.78125) + [-1.1275702593849246e-16 .. 0.01953125000000017]) * 2^8>"""
    def de_casteljau(self, contextctx, mid, msign=...) -> Any:
        """interval_bernstein_polynomial_integer.de_casteljau(self, context ctx, mid, msign=0)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 687)

        Uses de Casteljau's algorithm to compute the representation
        of this polynomial in a Bernstein basis over new regions.

        INPUT:

        - ``mid`` -- where to split the Bernstein basis region; 0 < mid < 1
        - ``msign`` -- default 0 (unknown); the sign of this polynomial at mid

        OUTPUT:

        - ``bp1``, ``bp2`` -- the new interval Bernstein polynomials
        - ``ok`` -- boolean; ``True`` if the sign of the original polynomial at
          mid is known

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([50, 20, -90, -70, 200], error=5)
            sage: ctx = mk_context()
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 1/2)
            sage: bp1
            <IBP: (50, 35, 0, -29, -31) + [0 .. 6) over [0 .. 1/2]>
            sage: bp2
            <IBP: (-31, -33, -8, 65, 200) + [0 .. 6) over [1/2 .. 1]>
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 2/3)
            sage: bp1
            <IBP: (50, 30, -26, -55, -13) + [0 .. 6) over [0 .. 2/3]>
            sage: bp2
            <IBP: (-13, 8, 47, 110, 200) + [0 .. 6) over [2/3 .. 1]>
            sage: bp1, bp2, ok = bp.de_casteljau(ctx, 7/39)
            sage: bp1
            <IBP: (50, 44, 36, 27, 17) + [0 .. 6) over [0 .. 7/39]>
            sage: bp2
            <IBP: (17, -26, -75, -22, 200) + [0 .. 6) over [7/39 .. 1]>"""
    def down_degree(self, contextctx, max_err, exp_err_shift) -> Any:
        '''interval_bernstein_polynomial_integer.down_degree(self, context ctx, max_err, exp_err_shift)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 786)

        Compute an interval_bernstein_polynomial_integer which bounds
        all the polynomials this interval polynomial bounds, but is
        of lesser degree.

        During the computation, we find an "expected error"
        expected_err, which is the error inherent in our approach
        (this depends on the degrees involved, and is proportional
        to the error of the current polynomial).

        We require that the error of the new interval polynomial
        be bounded both by max_err, and by expected_err << exp_err_shift.
        If we find such a polynomial p, then we return a pair of p and some
        debugging/logging information.  Otherwise, we return the pair
        (None, None).

        If the resulting polynomial would have error more than 2^17,
        then it is downscaled before returning.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([0, 100, 400, 903], error=2)
            sage: ctx = mk_context()
            sage: bp
            <IBP: (0, 100, 400, 903) + [0 .. 2)>
            sage: dbp, _ = bp.down_degree(ctx, 10, 32)
            sage: dbp
            <IBP: (-1, 148, 901) + [0 .. 4); level 1; slope_err 0.?e2>'''
    def down_degree_iter(self, contextctx, max_scale) -> Any:
        """interval_bernstein_polynomial_integer.down_degree_iter(self, context ctx, max_scale)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 893)

        Compute a degree-reduced version of this interval polynomial, by
        iterating down_degree.

        We stop when degree reduction would give a polynomial which is
        too inaccurate, meaning that either we think the current polynomial
        may have more roots in its region than the degree of the
        reduced polynomial, or that the least significant accurate bit
        in the result (on the absolute scale) would be larger than
        1 << max_scale.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([0, 100, 400, 903, 1600, 2500], error=2)
            sage: ctx = mk_context()
            sage: bp
            <IBP: (0, 100, 400, 903, 1600, 2500) + [0 .. 2)>
            sage: rbp = bp.down_degree_iter(ctx, 6)
            sage: rbp
            <IBP: (-4, 249, 2497) + [0 .. 9); level 2; slope_err 0.?e3>"""
    def downscale(self, bits) -> Any:
        '''interval_bernstein_polynomial_integer.downscale(self, bits)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 936)

        Compute an interval_bernstein_polynomial_integer which
        contains (or bounds) all the polynomials this interval
        polynomial contains (or bounds), but uses
        "bits" fewer bits.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([0, 100, 400, 903], error=2)
            sage: bp.downscale(5)
            <IBP: ((0, 3, 12, 28) + [0 .. 1)) * 2^5>'''
    def get_msb_bit(self) -> Any:
        """interval_bernstein_polynomial_integer.get_msb_bit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 779)

        Return an approximation of the log2 of the maximum of the
        absolute values of the coefficients, as an integer."""
    @overload
    def slope_range(self) -> Any:
        """interval_bernstein_polynomial_integer.slope_range(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 955)

        Compute a bound on the derivative of this polynomial, over its region.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([0, 100, 400, 903], error=2)
            sage: bp.slope_range().str(style='brackets')
            '[294.00000000000000 .. 1515.0000000000000]'"""
    @overload
    def slope_range(self) -> Any:
        """interval_bernstein_polynomial_integer.slope_range(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 955)

        Compute a bound on the derivative of this polynomial, over its region.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: bp = mk_ibpi([0, 100, 400, 903], error=2)
            sage: bp.slope_range().str(style='brackets')
            '[294.00000000000000 .. 1515.0000000000000]'"""

class island:
    '''island(interval_bernstein_polynomial bp, rr_gap lgap, rr_gap rgap)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3260)

    This implements the island portion of my ocean-island root isolation
    algorithm.  See the documentation for class ocean, for more
    information on the overall algorithm.

    Island root refinement starts with a Bernstein polynomial whose
    region is the whole island (or perhaps slightly more than the
    island in certain cases).  There are two subalgorithms; one when
    looking at a Bernstein polynomial covering a whole island (so we
    know that there are gaps on the left and right), and one when
    looking at a Bernstein polynomial covering the left segment of an
    island (so we know that there is a gap on the left, but the right
    is in the middle of an island).  An important invariant of the
    left-segment subalgorithm over the region [l .. r] is that it
    always finds a gap [r0 .. r] ending at its right endpoint.

    Ignoring degree reduction, downscaling (precision reduction), and
    failures to split, the algorithm is roughly:

    Whole island:

    1. If the island definitely has exactly one root, then return.
    2. Split the island in (approximately) half.
    3. If both halves definitely have no roots, then remove this island from
       its doubly-linked list (merging its left and right gaps) and return.
    4. If either half definitely has no roots, then discard that half
       and call the whole-island algorithm with the other half, then return.
    5. If both halves may have roots, then call the left-segment algorithm
       on the left half.
    6. We now know that there is a gap immediately to the left of the
       right half, so call the whole-island algorithm on the right half,
       then return.

    Left segment:

    1. Split the left segment in (approximately) half.
    2. If both halves definitely have no roots, then extend the left gap
       over the segment and return.
    3. If the left half definitely has no roots, then extend the left gap
       over this half and call the left-segment algorithm on the right half,
       then return.
    4. If the right half definitely has no roots, then split the island
       in two, creating a new gap.  Call the whole-island algorithm on the
       left half, then return.
    5. Both halves may have roots.  Call the left-segment algorithm on
       the left half.
    6. We now know that there is a gap immediately to the left of the
       right half, so call the left-segment algorithm on the right half,
       then return.

    Degree reduction complicates this picture only slightly.  Basically,
    we use heuristics to decide when degree reduction might be likely
    to succeed and be helpful; whenever this is the case, we attempt
    degree reduction.

    Precision reduction and split failure add more complications.
    The algorithm maintains a stack of different-precision representations
    of the interval Bernstein polynomial.  The base of the stack
    is at the highest (currently known) precision; each stack entry has
    approximately half the precision of the entry below it.  When we
    do a split, we pop off the top of the stack, split it, then push
    whichever half we\'re interested in back on the stack (so the
    different Bernstein polynomials may be over different regions).
    When we push a polynomial onto the stack, we may heuristically decide to
    push further lower-precision versions of the same polynomial onto the
    stack.

    In the algorithm above, whenever we say "split in (approximately) half",
    we attempt to split the top-of-stack polynomial using try_split()
    and try_rand_split().  However, these will fail if the sign of the
    polynomial at the chosen split point is unknown (if the polynomial is
    not known to high enough precision, or if the chosen split point
    actually happens to be a root of the polynomial).  If this fails, then
    we discard the top-of-stack polynomial, and try again with the
    next polynomial down (which has approximately twice the precision).
    This next polynomial may not be over the same region; if not, we
    split it using de Casteljau\'s algorithm to get a polynomial over
    (approximately) the same region first.

    If we run out of higher-precision polynomials (if we empty out the
    entire stack), then we give up on root refinement for this island.
    The ocean class will notice this, provide the island with a
    higher-precision polynomial, and restart root refinement.  Basically
    the only information kept in that case is the lower and upper bounds
    on the island.  Since these are updated whenever we discover a "half"
    (of an island or a segment) that definitely contains no roots, we
    never need to re-examine these gaps.  (We could keep more information.
    For example, we could keep a record of split points that succeeded
    and failed.  However, a split point that failed at lower precision
    is likely to succeed at higher precision, so it\'s not worth avoiding.
    It could be useful to select split points that are known to succeed,
    but starting from a new Bernstein polynomial over a slightly different
    region, hitting such split points would require de Casteljau splits
    with non-power-of-two denominators, which are much much slower.)'''
    def __init__(self, interval_bernstein_polynomialbp, rr_gaplgap, rr_gaprgap) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3357)

                Initialize an island from a Bernstein polynomial, and the gaps to
                the left and right of the island.
        """
    def bp_done(self, interval_bernstein_polynomialbp) -> Any:
        '''island.bp_done(self, interval_bernstein_polynomial bp)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3703)

        Examine the given Bernstein polynomial to see if it is known
        to have exactly one root in its region.  (In addition, we require
        that the polynomial region not include 0 or 1.  This makes things
        work if the user gives explicit bounds to real_roots(),
        where the lower or upper bound is a root of the polynomial.
        real_roots() deals with this by explicitly detecting it,
        dividing out the appropriate linear polynomial, and adding the
        root to the returned list of roots; but then if the island
        considers itself "done" with a region including 0 or 1, the returned
        root regions can overlap with each other.)'''
    def done(self, contextctx) -> Any:
        """island.done(self, context ctx)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3735)

        Check to see if the island is known to contain zero roots or
        is known to contain one root."""
    def has_root(self) -> bool:
        """island.has_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3753)

        Assuming that the island is done (has either 0 or 1 roots),
        reports whether the island has a root."""
    def less_bits(self, ancestors, interval_bernstein_polynomialbp) -> Any:
        """island.less_bits(self, ancestors, interval_bernstein_polynomial bp)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3569)

        Heuristically push lower-precision polynomials on
        the polynomial stack.  See the class documentation for class
        island for more information."""
    def more_bits(self, contextctx, ancestors, interval_bernstein_polynomialbp, rightmost) -> Any:
        '''island.more_bits(self, context ctx, ancestors, interval_bernstein_polynomial bp, rightmost)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3589)

        Find a Bernstein polynomial on the "ancestors" stack with
        more precision than bp; if it is over a different region,
        then shrink its region to (approximately) match that of bp.
        (If this is rightmost -- if bp covers the whole island -- then
        we only require that the new region cover the whole island
        fairly tightly; if this is not rightmost, then the new region
        will have exactly the same right boundary as bp, although the
        left boundary may vary slightly.)'''
    def refine(self, contextctx) -> Any:
        """island.refine(self, context ctx)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3409)

        Attempts to shrink and/or split this island into sub-island
        that each definitely contain exactly one root."""
    def refine_recurse(self, contextctx, interval_bernstein_polynomialbp, ancestors, history, rightmost) -> Any:
        """island.refine_recurse(self, context ctx, interval_bernstein_polynomial bp, ancestors, history, rightmost)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3420)

        This implements the root isolation algorithm described in the
        class documentation for class island.  This is the implementation
        of both the whole-island and the left-segment algorithms;
        if the flag rightmost is True, then it is the whole-island algorithm,
        otherwise the left-segment algorithm.

        The precision-reduction stack is (ancestors + [bp]); that is, the
        top-of-stack is maintained separately."""
    def reset_root_width(self, target_width) -> Any:
        '''island.reset_root_width(self, target_width)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3689)

        Modify the criteria for this island to require that it is not "done"
        until its width is less than or equal to target_width.'''
    def shrink_bp(self, contextctx) -> Any:
        """island.shrink_bp(self, context ctx)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3383)

        If the island's Bernstein polynomial covers a region much larger
        than the island itself (in particular, if either the island's
        left gap or right gap are totally contained in the polynomial's
        region) then shrink the polynomial down to cover the island more
        tightly."""

class linear_map:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3782)

        A simple class to map linearly between original coordinates
        (ranging from [lower .. upper]) and ocean coordinates (ranging
        from [0 .. 1]).
    """
    def __init__(self, lower, upper) -> Any:
        """linear_map.__init__(self, lower, upper)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3789)"""
    def from_ocean(self, region) -> Any:
        """linear_map.from_ocean(self, region)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3794)"""
    def to_ocean(self, region) -> Any:
        """linear_map.to_ocean(self, region)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3798)"""

class ocean:
    '''ocean(ctx, bpf, mapping)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 2971)

    Given the tools we\'ve defined so far, there are many possible root
    isolation algorithms that differ on where to select split points,
    what precision to work at when, and when to attempt degree
    reduction.

    Here we implement one particular algorithm, which I call the
    ocean-island algorithm.  We start with an interval Bernstein
    polynomial defined over the region [0 .. 1].  This region is
    the "ocean".  Using de Casteljau\'s algorithm and Descartes\'
    rule of signs, we divide this region into subregions which may
    contain roots, and subregions which are guaranteed not to contain
    roots.  Subregions which may contain roots are "islands"; subregions
    known not to contain roots are "gaps".

    All the real root isolation work happens in class island.  See the
    documentation of that class for more information.

    An island can be told to refine itself until it contains only a
    single root.  This may not succeed, if the island\'s interval
    Bernstein polynomial does not have enough precision.  The ocean
    basically loops, refining each of its islands, then increasing the
    precision of islands which did not succeed in isolating a single
    root; until all islands are done.

    Increasing the precision of unsuccessful islands is done in a
    single pass using split_for_target(); this means it is possible
    to share work among multiple islands.'''
    def __init__(self, ctx, bpf, mapping) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3002)

                Initialize an ocean from a context and a Bernstein polynomial
                factory.

                EXAMPLES::

                    sage: from sage.rings.polynomial.real_roots import *
                    sage: ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
                    ocean with precision 120 and 1 island(s)
        """
    @overload
    def all_done(self) -> Any:
        """ocean.all_done(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3165)

        Return ``True`` iff all islands are known to contain exactly one root.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.all_done()
            False
            sage: oc.find_roots()
            sage: oc.all_done()
            True"""
    @overload
    def all_done(self) -> Any:
        """ocean.all_done(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3165)

        Return ``True`` iff all islands are known to contain exactly one root.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.all_done()
            False
            sage: oc.find_roots()
            sage: oc.all_done()
            True"""
    @overload
    def all_done(self) -> Any:
        """ocean.all_done(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3165)

        Return ``True`` iff all islands are known to contain exactly one root.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.all_done()
            False
            sage: oc.find_roots()
            sage: oc.all_done()
            True"""
    def approx_bp(self, scale_log2) -> Any:
        """ocean.approx_bp(self, scale_log2)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3082)

        Return an approximation to our Bernstein polynomial with the
        given scale_log2.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.approx_bp(0)
            <IBP: (0, -4, 2, -2) + [0 .. 1); lsign 1>
            sage: oc.approx_bp(-20)
            <IBP: ((349525, -3295525, 2850354, -1482835) + [0 .. 1)) * 2^-20>"""
    @overload
    def find_roots(self) -> Any:
        """ocean.find_roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3098)

        Isolate all roots in this ocean.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 120 and 3 island(s)
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 240 and 3 island(s)"""
    @overload
    def find_roots(self) -> Any:
        """ocean.find_roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3098)

        Isolate all roots in this ocean.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 120 and 3 island(s)
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 240 and 3 island(s)"""
    @overload
    def find_roots(self) -> Any:
        """ocean.find_roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3098)

        Isolate all roots in this ocean.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 120 and 3 island(s)
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 240 and 3 island(s)"""
    @overload
    def increase_precision(self) -> Any:
        """ocean.increase_precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3220)

        Increase the precision of the interval Bernstein polynomial held
        by any islands which are not done.  (In normal use, calls to this
        function are separated by calls to self.refine_all().)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc
            ocean with precision 960 and 1 island(s)"""
    @overload
    def increase_precision(self) -> Any:
        """ocean.increase_precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3220)

        Increase the precision of the interval Bernstein polynomial held
        by any islands which are not done.  (In normal use, calls to this
        function are separated by calls to self.refine_all().)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc
            ocean with precision 960 and 1 island(s)"""
    @overload
    def increase_precision(self) -> Any:
        """ocean.increase_precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3220)

        Increase the precision of the interval Bernstein polynomial held
        by any islands which are not done.  (In normal use, calls to this
        function are separated by calls to self.refine_all().)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc
            ocean with precision 960 and 1 island(s)"""
    @overload
    def increase_precision(self) -> Any:
        """ocean.increase_precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3220)

        Increase the precision of the interval Bernstein polynomial held
        by any islands which are not done.  (In normal use, calls to this
        function are separated by calls to self.refine_all().)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc.increase_precision()
            sage: oc
            ocean with precision 960 and 1 island(s)"""
    @overload
    def refine_all(self) -> Any:
        """ocean.refine_all(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3144)

        Refine all islands which are not done (which are not known to
        contain exactly one root).

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.refine_all()
            sage: oc
            ocean with precision 120 and 3 island(s)"""
    @overload
    def refine_all(self) -> Any:
        """ocean.refine_all(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3144)

        Refine all islands which are not done (which are not known to
        contain exactly one root).

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc
            ocean with precision 120 and 1 island(s)
            sage: oc.refine_all()
            sage: oc
            ocean with precision 120 and 3 island(s)"""
    def reset_root_width(self, intisle_num, target_width) -> Any:
        """ocean.reset_root_width(self, int isle_num, target_width)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3190)

        Require that the isle_num island have a width at most target_width.

        If this is followed by a call to find_roots(), then the
        corresponding root will be refined to the specified width.

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([-1, -1, 1]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(1/2, 3/4)]
            sage: oc.reset_root_width(0, 1/2^200)
            sage: oc.find_roots()
            sage: oc
            ocean with precision 240 and 1 island(s)
            sage: RR(RealIntervalField(300)(oc.roots()[0]).absolute_diameter()).log2()
            -232.668979560890"""
    @overload
    def roots(self) -> Any:
        """ocean.roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3120)

        Return the locations of all islands in this ocean.  (If run
        after find_roots(), this is the location of all roots in the ocean.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(1/32, 1/16), (1/2, 5/8), (3/4, 7/8)]
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(95761241267509487747625/9671406556917033397649408, 191522482605387719863145/19342813113834066795298816), (1496269395904347376805/151115727451828646838272, 374067366568272936175/37778931862957161709568), (31/32, 63/64)]"""
    @overload
    def roots(self) -> Any:
        """ocean.roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3120)

        Return the locations of all islands in this ocean.  (If run
        after find_roots(), this is the location of all roots in the ocean.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(1/32, 1/16), (1/2, 5/8), (3/4, 7/8)]
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(95761241267509487747625/9671406556917033397649408, 191522482605387719863145/19342813113834066795298816), (1496269395904347376805/151115727451828646838272, 374067366568272936175/37778931862957161709568), (31/32, 63/64)]"""
    @overload
    def roots(self) -> Any:
        """ocean.roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3120)

        Return the locations of all islands in this ocean.  (If run
        after find_roots(), this is the location of all roots in the ocean.)

        EXAMPLES::

            sage: from sage.rings.polynomial.real_roots import *
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1/3, -22/7, 193/71, -140/99]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(1/32, 1/16), (1/2, 5/8), (3/4, 7/8)]
            sage: oc = ocean(mk_context(), bernstein_polynomial_factory_ratlist([1, 0, -1111/2, 0, 11108889/14, 0, 0, 0, 0, -1]), lmap)
            sage: oc.find_roots()
            sage: oc.roots()
            [(95761241267509487747625/9671406556917033397649408, 191522482605387719863145/19342813113834066795298816), (1496269395904347376805/151115727451828646838272, 374067366568272936175/37778931862957161709568), (31/32, 63/64)]"""

class rr_gap:
    '''rr_gap(lower, upper, sign)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3763)

    A simple class representing the gaps between islands, in my
    ocean-island root isolation algorithm.  Named "rr_gap" for
    "real roots gap", because "gap" seemed too short and generic.'''
    def __init__(self, lower, upper, sign) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3770)

                Initialize an rr_gap element.
        """
    def region(self) -> Any:
        """rr_gap.region(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3778)"""

class warp_map:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3806)

        A class to map between original coordinates and ocean coordinates.
        If neg is False, then the original->ocean transform is
        x -> x/(x+1), and the ocean->original transform is x/(1-x);
        this maps between [0 .. infinity] and [0 .. 1].
        If neg is True, then the original->ocean transform is
        x -> -x/(1-x), and the ocean->original transform is the same thing:
        -x/(1-x).  This maps between [0 .. -infinity] and [0 .. 1].
    """
    def __init__(self, neg) -> Any:
        """warp_map.__init__(self, neg)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3817)"""
    def from_ocean(self, region) -> Any:
        """warp_map.from_ocean(self, region)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3820)"""
    def to_ocean(self, region) -> Any:
        """warp_map.to_ocean(self, region)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/real_roots.pyx (starting at line 3827)"""
