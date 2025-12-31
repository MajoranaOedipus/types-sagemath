"""
`p`-adic distributions spaces

This module implements `p`-adic distributions, a `p`-adic Banach
space dual to locally analytic functions on a disc.

EXAMPLES::

    sage: D = OverconvergentDistributions(5, 7, 15)
    sage: v = D([7,14,21,28,35]); v
    (7 + O(7^5), 2*7 + O(7^4), 3*7 + O(7^3), 4*7 + O(7^2), O(7))

REFERENCES:

- [PS2011]_
"""
import sage.categories.action
import sage.structure.element
from sage.arith.misc import bernoulli as bernoulli
from sage.categories.category import ZZ as ZZ
from sage.categories.fields import Fields as Fields
from sage.matrix.constructor import matrix as matrix
from sage.misc.verbose import verbose as verbose
from sage.modular.pollack_stevens.sigma0 import Sigma0 as Sigma0
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import Infinity as Infinity
from sage.rings.padics.padic_generic import pAdicGeneric as pAdicGeneric
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

def get_dist_classes(p, prec_cap, base, symk, implementation):
    r"""
    Determine the element and action classes to be used for given inputs.

    INPUT:

    - ``p`` -- prime

    - ``prec_cap`` -- the `p`-adic precision cap

    - ``base`` -- the base ring

    - ``symk`` -- an element of Symk

    - ``implementation`` -- string; if not ``None``, override the
      automatic choice of implementation. May be 'long' or 'vector',
      otherwise raise a :exc:`NotImplementedError`.

    OUTPUT:

    - Either a Dist_vector and WeightKAction_vector, or a Dist_vector_long
      and WeightKAction_vector_long

    EXAMPLES::

        sage: D = OverconvergentDistributions(2, 3, 5); D # indirect doctest
        Space of 3-adic distributions with k=2 action and precision cap 5
    """

class Dist(sage.structure.element.ModuleElement):
    """File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 92)

            The main `p`-adic distribution class, implemented as per the paper [PS2011]__.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def act_right(self, gamma) -> Any:
        """Dist.act_right(self, gamma)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 686)

        The image of this element under the right action by a
        `2 \\times 2` matrix.

        INPUT:

        - ``gamma`` -- the matrix by which to act

        OUTPUT:

        - ``self | gamma``

        .. NOTE::

            You may also just use multiplication ``self * gamma``.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 7, 10)
            sage: v = D([98,49,21,28,35])
            sage: M = matrix([[1,0], [7,1]])
            sage: v.act_right(M)
            (2*7^2 + 7^3 + 5*7^4 + O(7^5), 3*7^2 + 6*7^3 + O(7^4), 3*7 + 7^2 + O(7^3), 4*7 + O(7^2), O(7))"""
    def diagonal_valuation(self, p=...) -> Any:
        """Dist.diagonal_valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 524)

        Return the largest `m` so that this distribution lies in `Fil^m`.

        INPUT:

        - ``p`` -- (default: ``None``) a positive integral prime

        OUTPUT:

        The largest integer `m` so that `p^m` divides the `0`-th
        moment, `p^{m-1}` divides the first moment, etc.

        EXAMPLES::

            sage: D = OverconvergentDistributions(8, 7, 15)
            sage: v = D([7^(5-i) for i in range(1,5)])
            sage: v
            (O(7^4), O(7^3), O(7^2), O(7))
            sage: v.diagonal_valuation(7)
            4"""
    @overload
    def find_scalar(self, _other, p, M=..., check=...) -> Any:
        """Dist.find_scalar(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 285)

        Return an ``alpha`` with ``other = self * alpha``, or raises
        a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if this distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar(self, w, p=...) -> Any:
        """Dist.find_scalar(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 285)

        Return an ``alpha`` with ``other = self * alpha``, or raises
        a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if this distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar(self, w, p=..., M=...) -> Any:
        """Dist.find_scalar(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 285)

        Return an ``alpha`` with ``other = self * alpha``, or raises
        a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if this distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar(self, u, p=...) -> Any:
        """Dist.find_scalar(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 285)

        Return an ``alpha`` with ``other = self * alpha``, or raises
        a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if this distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar_from_zeroth_moment(self, _other, p, M=..., check=...) -> Any:
        """Dist.find_scalar_from_zeroth_moment(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 407)

        Return an ``alpha`` with ``other = self * alpha`` using only
        the zeroth moment, or raises a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if the zeroth moment of the
        distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar_from_zeroth_moment(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar_from_zeroth_moment(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar_from_zeroth_moment(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar_from_zeroth_moment(self, w, p=...) -> Any:
        """Dist.find_scalar_from_zeroth_moment(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 407)

        Return an ``alpha`` with ``other = self * alpha`` using only
        the zeroth moment, or raises a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if the zeroth moment of the
        distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar_from_zeroth_moment(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar_from_zeroth_moment(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar_from_zeroth_moment(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar_from_zeroth_moment(self, w, p=..., M=...) -> Any:
        """Dist.find_scalar_from_zeroth_moment(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 407)

        Return an ``alpha`` with ``other = self * alpha`` using only
        the zeroth moment, or raises a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if the zeroth moment of the
        distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar_from_zeroth_moment(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar_from_zeroth_moment(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar_from_zeroth_moment(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def find_scalar_from_zeroth_moment(self, u, p=...) -> Any:
        """Dist.find_scalar_from_zeroth_moment(self, _other, p, M=None, check=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 407)

        Return an ``alpha`` with ``other = self * alpha`` using only
        the zeroth moment, or raises a :exc:`ValueError`.

        It will also raise a :exc:`ValueError` if the zeroth moment of the
        distribution is zero.

        INPUT:

        - ``other`` -- another distribution

        - ``p`` -- an integral prime (only used if the parent is not a Symk)

        - ``M`` -- (default: ``None``) an integer, the relative precision
          to which the scalar must be determined

        - ``check`` -- boolean (default: ``True``); whether to validate
          that ``other`` is actually a multiple of this element

        OUTPUT: a scalar ``alpha`` with ``other = self * alpha``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5])
            sage: w = D([3,6,9,12,15])
            sage: v.find_scalar_from_zeroth_moment(w,p=7)
            3 + O(7^5)
            sage: v.find_scalar_from_zeroth_moment(w,p=7,M=4)
            3 + O(7^4)

            sage: u = D([1,4,9,16,25])
            sage: v.find_scalar_from_zeroth_moment(u,p=7)
            Traceback (most recent call last):
            ...
            ValueError: not a scalar multiple"""
    @overload
    def is_zero(self, p=..., M=...) -> bool:
        """Dist.is_zero(self, p=None, M=None) -> bool

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 214)

        Return ``True`` if the `i`-th moment is zero for all `i` (case ``M`` is
        ``None``) or zero modulo `p^{M-i}` for all `i` (when ``M`` is not
        ``None``).

        Note that some moments are not known to precision ``M``, in which
        case they are only checked to be equal to zero modulo the
        precision to which they are defined.

        INPUT:

        - ``p`` -- prime

        - ``M`` -- precision

        OUTPUT: boolean

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.is_zero()
            False
            sage: v = D(5*[0])
            sage: v.is_zero()
            True

        ::

            sage: D = Symk(0)
            sage: v = D([0])
            sage: v.is_zero(5,3)
            True"""
    @overload
    def is_zero(self) -> Any:
        """Dist.is_zero(self, p=None, M=None) -> bool

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 214)

        Return ``True`` if the `i`-th moment is zero for all `i` (case ``M`` is
        ``None``) or zero modulo `p^{M-i}` for all `i` (when ``M`` is not
        ``None``).

        Note that some moments are not known to precision ``M``, in which
        case they are only checked to be equal to zero modulo the
        precision to which they are defined.

        INPUT:

        - ``p`` -- prime

        - ``M`` -- precision

        OUTPUT: boolean

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.is_zero()
            False
            sage: v = D(5*[0])
            sage: v.is_zero()
            True

        ::

            sage: D = Symk(0)
            sage: v = D([0])
            sage: v.is_zero(5,3)
            True"""
    @overload
    def is_zero(self) -> Any:
        """Dist.is_zero(self, p=None, M=None) -> bool

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 214)

        Return ``True`` if the `i`-th moment is zero for all `i` (case ``M`` is
        ``None``) or zero modulo `p^{M-i}` for all `i` (when ``M`` is not
        ``None``).

        Note that some moments are not known to precision ``M``, in which
        case they are only checked to be equal to zero modulo the
        precision to which they are defined.

        INPUT:

        - ``p`` -- prime

        - ``M`` -- precision

        OUTPUT: boolean

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.is_zero()
            False
            sage: v = D(5*[0])
            sage: v.is_zero()
            True

        ::

            sage: D = Symk(0)
            sage: v = D([0])
            sage: v.is_zero(5,3)
            True"""
    def lift(self, p=..., M=..., new_base_ring=...) -> Any:
        """Dist.lift(self, p=None, M=None, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 619)

        Lift a distribution or element of `Sym^k` to an overconvergent distribution.

        INPUT:

        - ``p`` -- (default: ``None``) a positive integral prime.  If ``None``
          then ``p`` must be available in the parent

        - ``M`` -- (default: ``None``) a positive integer giving the
          desired number of moments. If ``None``, returns a distribution having one
          more moment than this one.

        - ``new_base_ring`` -- (default: ``None``) a ring giving the desired base
          ring of the result. If ``None``, a base ring is chosen automatically.

        OUTPUT:

        - An overconvergent distribution with `M` moments whose image
          under the specialization map is this element.

        EXAMPLES::

            sage: V = Symk(0)
            sage: x = V(1/4)
            sage: y = x.lift(17, 5)
            sage: y
            (13 + 12*17 + 12*17^2 + 12*17^3 + 12*17^4 + O(17^5), O(17^4), O(17^3), O(17^2), O(17))
            sage: y.specialize()._moments == x._moments
            True"""
    def moment(self, n) -> Any:
        """Dist.moment(self, n)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 96)

        Return the `n`-th moment.

        INPUT:

        - ``n`` -- integer or slice, to be passed on to moments

        OUTPUT:

        - the `n`-th moment, or a list of moments in the case that `n`
          is a slice.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 7, 10)
            sage: v = D([7,14,21,28,35])
            sage: v.moment(3)
            4*7 + O(7^2)
            sage: v.moment(0)
            7 + O(7^5)"""
    @overload
    def moments(self) -> Any:
        """Dist.moments(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 120)

        Return the vector of moments.

        OUTPUT: the vector of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 5, 10, base = Qp(5))
            sage: v = D([1,7,4,2,-1])
            sage: v = 1/5^3 * v
            sage: v
            5^-3 * (1 + O(5^5), 2 + 5 + O(5^4), 4 + O(5^3), 2 + O(5^2), 4 + O(5))
            sage: v.moments()
            (5^-3 + O(5^2), 2*5^-3 + 5^-2 + O(5), 4*5^-3 + O(5^0), 2*5^-3 + O(5^-1), 4*5^-3 + O(5^-2))"""
    @overload
    def moments(self) -> Any:
        """Dist.moments(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 120)

        Return the vector of moments.

        OUTPUT: the vector of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 5, 10, base = Qp(5))
            sage: v = D([1,7,4,2,-1])
            sage: v = 1/5^3 * v
            sage: v
            5^-3 * (1 + O(5^5), 2 + 5 + O(5^4), 4 + O(5^3), 2 + O(5^2), 4 + O(5))
            sage: v.moments()
            (5^-3 + O(5^2), 2*5^-3 + 5^-2 + O(5), 4*5^-3 + O(5^0), 2*5^-3 + O(5^-1), 4*5^-3 + O(5^-2))"""
    @overload
    def normalize(self, include_zeroth_moment=...) -> Any:
        """Dist.normalize(self, include_zeroth_moment=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 138)

        Normalize so that the precision of the `i`-th moment is `n-i`,
        where `n` is the number of moments.

        OUTPUT: normalized entries of the distribution

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15); D
            Space of 7-adic distributions with k=5 action and precision cap 15
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.normalize()
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))"""
    @overload
    def normalize(self) -> Any:
        """Dist.normalize(self, include_zeroth_moment=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 138)

        Normalize so that the precision of the `i`-th moment is `n-i`,
        where `n` is the number of moments.

        OUTPUT: normalized entries of the distribution

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15); D
            Space of 7-adic distributions with k=5 action and precision cap 15
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.normalize()
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))"""
    def scale(self, left) -> Any:
        """Dist.scale(self, left)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 181)

        Scale the moments of the distribution by ``left``.

        INPUT:

        - ``left`` -- scalar

        OUTPUT: scales the moments by ``left``

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: v = D([1,2,3,4,5]); v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.scale(2)
            (2 + O(7^5), 4 + O(7^4), 6 + O(7^3), 1 + 7 + O(7^2), 3 + O(7))"""
    @overload
    def specialize(self, new_base_ring=...) -> Any:
        """Dist.specialize(self, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 585)

        Return the image of this overconvergent distribution under
        the canonical projection from distributions of weight `k` to
        `Sym^k`.

        INPUT:

        - ``new_base_ring`` -- (default: ``None``) a ring giving the
          desired base ring of the result

        OUTPUT:

        An element of `Sym^k(K)`, where `K` is the specified base ring.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 13)
            sage: d = D([0,2,4,6,8,10,12])
            sage: d.specialize()
            (O(13^7), 2 + O(13^6), 4 + O(13^5), 6 + O(13^4), 8 + O(13^3))"""
    @overload
    def specialize(self) -> Any:
        """Dist.specialize(self, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 585)

        Return the image of this overconvergent distribution under
        the canonical projection from distributions of weight `k` to
        `Sym^k`.

        INPUT:

        - ``new_base_ring`` -- (default: ``None``) a ring giving the
          desired base ring of the result

        OUTPUT:

        An element of `Sym^k(K)`, where `K` is the specified base ring.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 13)
            sage: d = D([0,2,4,6,8,10,12])
            sage: d.specialize()
            (O(13^7), 2 + O(13^6), 4 + O(13^5), 6 + O(13^4), 8 + O(13^3))"""
    def valuation(self, p=...) -> Any:
        """Dist.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 551)

        Return the minimum valuation of any moment.

        INPUT:

        - ``p`` -- (default: ``None``) a positive integral prime

        OUTPUT: integer

        .. WARNING::

            Since only finitely many moments are computed, this valuation may
            be larger than the actual valuation of this distribution.
            Moreover, this valuation may be smaller than the actual
            valuation if all entries are zero to the known precision.

        EXAMPLES::

            sage: D = OverconvergentDistributions(8, 7, 15)
            sage: v = D([7^(5-i) for i in range(1,5)])
            sage: v
            (O(7^4), O(7^3), O(7^2), O(7))
            sage: v.valuation(7)
            4"""

class Dist_vector(Dist):
    """Dist_vector(moments, parent, ordp=0, check=True, normalize=True)

    File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 713)

    A distribution is stored as a vector whose `j`-th entry is the `j`-th moment of the distribution.

    The `j`-th entry is stored modulo `p^{N-j}` where `N` is the total number of moments.
    (This is the accuracy that is maintained after acting by `\\Gamma_0(p)`.)

    INPUT:

    - ``moments`` -- the list of moments.  If ``check == False`` it
      must be a vector in the appropriate approximation module.

    - ``parent`` -- a :class:`distributions.OverconvergentDistributions_class` or
      :class:`distributions.Symk_class` instance

    - ``ordp`` -- integer;  this *must* be zero in the case of Symk
      of an exact ring

    - ``check`` -- boolean (default: ``True``); whether to validate input

    EXAMPLES::

        sage: D = OverconvergentDistributions(3,5,6) # indirect doctest
        sage: v = D([1,1,1])"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, moments, parent, ordp=..., check=..., normalize=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 738)

                Initialization.

                TESTS::

                    sage: Symk(4)(0)
                    (0, 0, 0, 0, 0)
        """
    @overload
    def normalize(self, include_zeroth_moment=...) -> Any:
        """Dist_vector.normalize(self, include_zeroth_moment=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1028)

        Normalize by reducing modulo `Fil^N`, where `N` is the number of moments.

        If the parent is Symk, then normalize has no effect.  If the
        parent is a space of distributions, then normalize reduces the
        `i`-th moment modulo `p^{N-i}`.

        OUTPUT: this distribution, after normalizing

        .. WARNING::

            This function modifies the distribution in place as well as returning it.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3,7,10)
            sage: v = D([1,2,3,4,5]) ; v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: w = v.reduce_precision(3) ; w
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3))
            sage: w.normalize()
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: w
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: v.reduce_precision(3).normalize(include_zeroth_moment=False)
            (1 + O(7^5), 2 + O(7^2), 3 + O(7))"""
    @overload
    def normalize(self) -> Any:
        """Dist_vector.normalize(self, include_zeroth_moment=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1028)

        Normalize by reducing modulo `Fil^N`, where `N` is the number of moments.

        If the parent is Symk, then normalize has no effect.  If the
        parent is a space of distributions, then normalize reduces the
        `i`-th moment modulo `p^{N-i}`.

        OUTPUT: this distribution, after normalizing

        .. WARNING::

            This function modifies the distribution in place as well as returning it.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3,7,10)
            sage: v = D([1,2,3,4,5]) ; v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: w = v.reduce_precision(3) ; w
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3))
            sage: w.normalize()
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: w
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: v.reduce_precision(3).normalize(include_zeroth_moment=False)
            (1 + O(7^5), 2 + O(7^2), 3 + O(7))"""
    @overload
    def normalize(self, include_zeroth_moment=...) -> Any:
        """Dist_vector.normalize(self, include_zeroth_moment=True)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1028)

        Normalize by reducing modulo `Fil^N`, where `N` is the number of moments.

        If the parent is Symk, then normalize has no effect.  If the
        parent is a space of distributions, then normalize reduces the
        `i`-th moment modulo `p^{N-i}`.

        OUTPUT: this distribution, after normalizing

        .. WARNING::

            This function modifies the distribution in place as well as returning it.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3,7,10)
            sage: v = D([1,2,3,4,5]) ; v
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: w = v.reduce_precision(3) ; w
            (1 + O(7^5), 2 + O(7^4), 3 + O(7^3))
            sage: w.normalize()
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: w
            (1 + O(7^3), 2 + O(7^2), 3 + O(7))
            sage: v.reduce_precision(3).normalize(include_zeroth_moment=False)
            (1 + O(7^5), 2 + O(7^2), 3 + O(7))"""
    @overload
    def precision_absolute(self) -> Any:
        """Dist_vector.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1006)

        Return the absolute precision of this distribution.

        The absolute precision is the sum of the relative precision
        (number of moments) and the valuation.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 7, base = Qp(7))
            sage: v = D([3,1,10,0])
            sage: v.precision_absolute()
            4
            sage: v *= 7
            sage: v.precision_absolute()
            5
            sage: v = 1/7^10 * v
            sage: v.precision_absolute()
            -5"""
    @overload
    def precision_absolute(self) -> Any:
        """Dist_vector.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1006)

        Return the absolute precision of this distribution.

        The absolute precision is the sum of the relative precision
        (number of moments) and the valuation.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 7, base = Qp(7))
            sage: v = D([3,1,10,0])
            sage: v.precision_absolute()
            4
            sage: v *= 7
            sage: v.precision_absolute()
            5
            sage: v = 1/7^10 * v
            sage: v.precision_absolute()
            -5"""
    @overload
    def precision_absolute(self) -> Any:
        """Dist_vector.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1006)

        Return the absolute precision of this distribution.

        The absolute precision is the sum of the relative precision
        (number of moments) and the valuation.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 7, base = Qp(7))
            sage: v = D([3,1,10,0])
            sage: v.precision_absolute()
            4
            sage: v *= 7
            sage: v.precision_absolute()
            5
            sage: v = 1/7^10 * v
            sage: v.precision_absolute()
            -5"""
    @overload
    def precision_absolute(self) -> Any:
        """Dist_vector.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1006)

        Return the absolute precision of this distribution.

        The absolute precision is the sum of the relative precision
        (number of moments) and the valuation.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 7, base = Qp(7))
            sage: v = D([3,1,10,0])
            sage: v.precision_absolute()
            4
            sage: v *= 7
            sage: v.precision_absolute()
            5
            sage: v = 1/7^10 * v
            sage: v.precision_absolute()
            -5"""
    @overload
    def precision_relative(self) -> Any:
        """Dist_vector.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 980)

        Return the relative precision of this distribution.

        The precision is just the number of moments stored, which is
        also `k+1` in the case of `Sym^k(R)`.  For overconvergent
        distributions, the precision is the integer `m` so that the
        sequence of moments is known modulo `Fil^m`.

        OUTPUT: integer giving the number of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11, 15)
            sage: v = D([1,1,10,9,6,15])
            sage: v.precision_relative()
            6
            sage: v = v.reduce_precision(4); v.precision_relative()
            4
            sage: D = Symk(10)
            sage: v = D.random_element()
            sage: v.precision_relative()
            11"""
    @overload
    def precision_relative(self) -> Any:
        """Dist_vector.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 980)

        Return the relative precision of this distribution.

        The precision is just the number of moments stored, which is
        also `k+1` in the case of `Sym^k(R)`.  For overconvergent
        distributions, the precision is the integer `m` so that the
        sequence of moments is known modulo `Fil^m`.

        OUTPUT: integer giving the number of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11, 15)
            sage: v = D([1,1,10,9,6,15])
            sage: v.precision_relative()
            6
            sage: v = v.reduce_precision(4); v.precision_relative()
            4
            sage: D = Symk(10)
            sage: v = D.random_element()
            sage: v.precision_relative()
            11"""
    @overload
    def precision_relative(self) -> Any:
        """Dist_vector.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 980)

        Return the relative precision of this distribution.

        The precision is just the number of moments stored, which is
        also `k+1` in the case of `Sym^k(R)`.  For overconvergent
        distributions, the precision is the integer `m` so that the
        sequence of moments is known modulo `Fil^m`.

        OUTPUT: integer giving the number of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11, 15)
            sage: v = D([1,1,10,9,6,15])
            sage: v.precision_relative()
            6
            sage: v = v.reduce_precision(4); v.precision_relative()
            4
            sage: D = Symk(10)
            sage: v = D.random_element()
            sage: v.precision_relative()
            11"""
    @overload
    def precision_relative(self) -> Any:
        """Dist_vector.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 980)

        Return the relative precision of this distribution.

        The precision is just the number of moments stored, which is
        also `k+1` in the case of `Sym^k(R)`.  For overconvergent
        distributions, the precision is the integer `m` so that the
        sequence of moments is known modulo `Fil^m`.

        OUTPUT: integer giving the number of moments

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11, 15)
            sage: v = D([1,1,10,9,6,15])
            sage: v.precision_relative()
            6
            sage: v = v.reduce_precision(4); v.precision_relative()
            4
            sage: D = Symk(10)
            sage: v = D.random_element()
            sage: v.precision_relative()
            11"""
    def reduce_precision(self, M) -> Any:
        """Dist_vector.reduce_precision(self, M)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1076)

        Only hold on to `M` moments.

        INPUT:

        - ``M`` -- positive integer less than the precision of this
          distribution

        OUTPUT:

        - a new distribution with `M` moments equal to the first `M`
          moments of this distribution.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3,7,10)
            sage: v = D([3,4,5])
            sage: v
            (3 + O(7^3), 4 + O(7^2), 5 + O(7))
            sage: v.reduce_precision(2)
            (3 + O(7^3), 4 + O(7^2))"""
    def solve_difference_equation(self) -> Any:
        """Dist_vector.solve_difference_equation(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1106)

        Solve the difference equation. `self = v | \\Delta`, where `\\Delta = [1, 1; 0, 1] - 1`.

        See Theorem 4.5 and Lemma 4.4 of [PS2011]_.

        OUTPUT:

        - a distribution `v` so that `self = v | Delta` , assuming ``self.moment(0) == 0``.
          Otherwise solves the difference equation for ``self - (self.moment(0),0,...,0)``.

        EXAMPLES::

            sage: D = OverconvergentDistributions(5,7,15)
            sage: v = D(([0,2,3,4,5]))
            sage: g = D._act.actor()(Matrix(ZZ,2,2,[1,1,0,1]))
            sage: w = v.solve_difference_equation()
            sage: v - (w*g - w)
            (O(7^4), O(7^3), O(7^2), O(7))
            sage: v = D(([7,2,3,4,5]))
            sage: w = v.solve_difference_equation()
            sage: v - (w*g - w)
            (7 + O(7^4), O(7^3), O(7^2), O(7))"""
    @overload
    def __reduce__(self) -> Any:
        """Dist_vector.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 775)

        Used for pickling.

        EXAMPLES::

            sage: D = sage.modular.pollack_stevens.distributions.Symk(2)
            sage: x = D([2,3,4])
            sage: x.__reduce__()
            (<class 'sage.modular.pollack_stevens.dist.Dist_vector'>, ((2, 3, 4), Sym^2 Q^2, 0, False))"""
    @overload
    def __reduce__(self) -> Any:
        """Dist_vector.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 775)

        Used for pickling.

        EXAMPLES::

            sage: D = sage.modular.pollack_stevens.distributions.Symk(2)
            sage: x = D([2,3,4])
            sage: x.__reduce__()
            (<class 'sage.modular.pollack_stevens.dist.Dist_vector'>, ((2, 3, 4), Sym^2 Q^2, 0, False))"""

class WeightKAction(sage.categories.action.Action):
    """WeightKAction(Dk, character, adjuster, on_left, dettwist, padic=False)

    File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1180)

    Encode the action of the monoid `\\Sigma_0(N)` on the space of distributions.

    INPUT:

    - ``Dk`` -- a space of distributions
    - ``character`` -- data specifying a Dirichlet character to apply to
      the top right corner, and a power of the determinant by which to scale.
      See the documentation of
      :class:`sage.modular.pollack_stevens.distributions.OverconvergentDistributions_factory`
      for more details.
    - ``adjuster`` -- a callable object that turns matrices into 4-tuples
    - ``on_left`` -- whether this action should be on the left
    - ``dettwist`` -- a power of the determinant to twist by
    - ``padic`` -- if ``True``, define an action of `p`-adic matrices (not just integer ones)

    EXAMPLES::

        sage: D = OverconvergentDistributions(4,5,10,base = Qp(5,20)); D
        Space of 5-adic distributions with k=4 action and precision cap 10
        sage: D._act
        Right action by Monoid Sigma0(5) with coefficients in 5-adic Field with capped relative precision 20 on Space of 5-adic distributions with k=4 action and precision cap 10"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Dk, character, adjuster, on_left, dettwist, padic=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1204)

                Initialization.

                TESTS::

                    sage: D = OverconvergentDistributions(4,5,10,base = Qp(5,20)); D # indirect doctest
                    Space of 5-adic distributions with k=4 action and precision cap 10
                    sage: D = Symk(10) # indirect doctest
        """
    def acting_matrix(self, g, M) -> Any:
        """WeightKAction.acting_matrix(self, g, M)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1252)

        The matrix defining the action of ``g`` at precision ``M``.

        INPUT:

        - ``g`` -- an instance of
          :class:`sage.matrix.matrix_generic_dense.Matrix_generic_dense`

        - ``M`` -- positive integer giving the precision at which
          ``g`` should act

        OUTPUT:

        - An `M \\times M` matrix so that the action of `g` on a
          distribution with `M` moments is given by a vector-matrix
          multiplication.

        .. NOTE::

            This function caches its results.  To clear the cache use
            :meth:`clear_cache`.

        EXAMPLES::

            sage: D = Symk(3)
            sage: v = D([5,2,7,1])
            sage: g = Matrix(ZZ,2,2,[1,3,0,1])
            sage: v * D._act.actor()(g) # indirect doctest
            (5, 17, 64, 253)"""
    @overload
    def clear_cache(self) -> Any:
        """WeightKAction.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1236)

        Clear the cached matrices which define the action of `U_p`
        (these depend on the desired precision) and the
        dictionary that stores the maximum precisions computed so far.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4,5,4)
            sage: D([1,2,5,3]) * D._act.actor()(Matrix(ZZ,2,2,[1,1,0,1]))
            (1 + O(5^4), 3 + O(5^3), 2*5 + O(5^2), O(5))
            sage: D._act.clear_cache()"""
    @overload
    def clear_cache(self) -> Any:
        """WeightKAction.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/modular/pollack_stevens/dist.pyx (starting at line 1236)

        Clear the cached matrices which define the action of `U_p`
        (these depend on the desired precision) and the
        dictionary that stores the maximum precisions computed so far.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4,5,4)
            sage: D([1,2,5,3]) * D._act.actor()(Matrix(ZZ,2,2,[1,1,0,1]))
            (1 + O(5^4), 3 + O(5^3), 2*5 + O(5^2), O(5))
            sage: D._act.clear_cache()"""

class WeightKAction_vector(WeightKAction):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
