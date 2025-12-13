from sage.misc.abstract_method import abstract_method as abstract_method
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.lattice_precision import pRational as pRational
from sage.rings.padics.padic_generic_element import pAdicGenericElement as pAdicGenericElement
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

def unpickle_le(parent, value, prec):
    """
    Unpickle `p`-adic elements.

    INPUT:

    - ``parent`` -- the parent, a `p`-adic ring

    - ``value`` -- a rational number

    - ``prec`` -- integer

    EXAMPLES::

        sage: from sage.rings.padics.padic_lattice_element import unpickle_le
        sage: R = ZpLC(5,8)
        sage: a = unpickle_le(R, 42, 6); a
        2 + 3*5 + 5^2 + O(5^6)
        sage: a.parent() is R
        True
    """

class pAdicLatticeElement(pAdicGenericElement):
    """
    Construct new element with given parent and value.

    INPUT:

    - ``parent`` -- the parent of this element

    - ``x`` -- the newly created element

    - ``prec`` -- integer; the absolute precision at which this
      element has to be capped

    - ``dx`` -- dictionary representing the differential of ``x``

    - ``dx_mode`` -- string; either ``'linear_combination'`` (the default)
      or ``'values'``

    - ``valuation`` -- integer or ``None`` (default: ``None``);
      the valuation of this element

    - ``check`` -- boolean (default: ``True``); whether the function
      should check that the given values are well formed and coherent

    - ``reduce`` -- boolean (default: ``True``); whether the given
      values need to be reduced

    TESTS::

        sage: R = ZpLC(2)
        sage: x = R(1, 10)  # indirect doctest
        sage: x
        1 + O(2^10)
    """
    def __init__(self, parent, x, prec=None, dx=[], dx_mode: str = 'linear_combination', valuation=None, check: bool = True, reduce: bool = True) -> None:
        """
        TESTS::

            sage: R = ZpLC(2)
            sage: x = R(1, 10)  # indirect doctest
            sage: x
            1 + O(2^10)
        """
    def __reduce__(self):
        """
        Return a tuple of a function and data that can be used to unpickle this
        element.

        EXAMPLES::

            sage: R = ZpLC(5)
            sage: a = R(-3)
            sage: loads(dumps(a)) == a
            True

        For now, diffused digits of precision are not preserved by pickling::

            sage: x, y = R(1, 10), R(1, 5)
            sage: u, v = x+y, x-y
            sage: u + v
            2 + O(5^10)

            sage: up = loads(dumps(u))
            sage: vp = loads(dumps(v))
            sage: up + vp
            2 + O(5^5)
        """
    def approximation(self):
        """
        Return an approximation of this element at
        its absolute precision.

        EXAMPLES::

            sage: R = ZpLC(2, print_mode='terse')
            sage: x = R(1234, 10); x
            210 + O(2^10)
            sage: x.approximation()
            210
        """
    def value(self):
        """
        Return the actual approximation of this element
        stored in memory.
        In presence of diffused digits of precision, it can
        have more precision than the absolute precision of
        the element.

        EXAMPLES::

            sage: R = ZpLC(2, print_mode='terse')
            sage: x = R(1234, 10); x
            210 + O(2^10)
            sage: x.approximation()
            210

        Another example with diffused digits::

            sage: x = R(2, 10); y = R(7, 5)
            sage: u = x - y
            sage: u
            27 + O(2^5)
            sage: u.value()
            1048571
        """
    def residue(self, absprec: int = 1, field=None, check_prec: bool = True):
        """
        Reduces this element modulo `p^{\\mathrm{absprec}}`.

        INPUT:

        - ``absprec`` -- nonnegative integer (default: 1)

        - ``field`` -- boolean (default: ``None``); whether to return an
          element of GF(p) or Zmod(p)

        - ``check_prec`` -- boolean (default: ``True``); whether to raise an
          error if this element has insufficient precision to determine the
          reduction

        OUTPUT:

        This element reduced modulo `p^\\mathrm{absprec}` as an element of
        `\\ZZ/p^\\mathrm{absprec}\\ZZ`

        EXAMPLES::

            sage: R = ZpLC(7,4)
            sage: a = R(8)
            sage: a.residue(1)
            1

        TESTS::

            sage: R = ZpLC(7,4)
            sage: a = R(8)
            sage: a.residue(0)
            0
            sage: a.residue(-1)
            Traceback (most recent call last):
            ...
            ValueError: cannot reduce modulo a negative power of p
            sage: a.residue(5)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision known in order to compute residue
            sage: a.residue(5, check_prec=False)
            8

            sage: a.residue(field=True).parent()
            Finite Field of size 7
        """
    def precision_lattice(self):
        """
        Return the precision object (which is a lattice in a possibly
        high-dimensional vector space) that handles the precision of
        this element.

        EXAMPLES::

            sage: R = ZpLC(2, label='precision')
            sage: x = R.random_element()
            sage: y = R.random_element()
            sage: x.precision_lattice()
            Precision lattice on 2 objects (label: precision)

        .. SEEALSO::

            :class:`sage.rings.padics.lattice_precision.PrecisionLattice`
        """
    def precision_absolute(self):
        """
        Return the absolute precision of this element.

        This precision is computed by projecting the lattice precision
        onto the coordinate defined by this element.

        EXAMPLES::

            sage: R = ZpLC(2, print_mode='terse')
            sage: x = R(1234, 10); x
            210 + O(2^10)
            sage: x.precision_absolute()
            10

        Another example with diffused digits::

            sage: x = R(1, 10); y = R(1, 5)
            sage: x, y = x+y, x-y
            sage: x.precision_absolute()
            5
            sage: y.precision_absolute()
            5
            sage: (x+y).precision_absolute()
            11
        """
    def is_precision_capped(self):
        """
        Return whether the absolute precision on this element results from a
        cap coming from the parent.

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(1, 10); x
            1 + O(2^10)
            sage: x.is_precision_capped()
            False

            sage: y = x-x; y
            O(2^40)
            sage: y.is_precision_capped()
            True

            sage: y = x << 35; y
            2^35 + O(2^40)
            sage: y.is_precision_capped()
            True
            sage: z = y >> 35; z
            1 + O(2^5)
            sage: z.is_precision_capped()
            True
        """
    def valuation(self, secure: bool = False):
        """
        Return the valuation of this element.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); when ``True``,
          an error is raised if the precision on the element is not
          enough to determine for sure its valuation. Otherwise the
          absolute precision (which is the smallest possible valuation)
          is returned.

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(12, 10); x
            2^2 + 2^3 + O(2^10)
            sage: x.valuation()
            2

            sage: y = x - x; y
            O(2^40)
            sage: y.valuation()
            40
            sage: y.valuation(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision
        """
    def precision_relative(self, secure: bool = False):
        """
        Return the relative precision of this element, that is
        the difference between its absolute precision and its
        valuation.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); when ``True``,
          an error is raised if the precision on the element is not
          enough to determine for sure its valuation

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(12, 10); x
            2^2 + 2^3 + O(2^10)
            sage: x.precision_relative()
            8

            sage: y = x - x; y
            O(2^40)
            sage: y.precision_relative()
            0
            sage: y.precision_relative(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision
        """
    def is_equal_to(self, other, prec):
        """
        Return ``True`` if this element is indistinguishable
        from ``other`` at precision ``prec``

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(1, 5)
            sage: y = R(128, 10)
            sage: z = x + y

            sage: x
            1 + O(2^5)
            sage: z
            1 + O(2^5)

            sage: x.is_equal_to(z, 5)
            True

            sage: x.is_equal_to(z, 10)
            False
            sage: z - x
            2^7 + O(2^10)
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of this element.

        .. NOTE::

            The result of division always lives in the fraction field,
            even if the element to be inverted is a unit.

        EXAMPLES::

            sage: R = ZpLC(19)
            sage: x = R(-5/2, 5); x
            7 + 9*19 + 9*19^2 + 9*19^3 + 9*19^4 + O(19^5)

            sage: y = ~x    # indirect doctest
            sage: y
            11 + 7*19 + 11*19^2 + 7*19^3 + 11*19^4 + O(19^5)
            sage: y == -2/5
            True

        TESTS::

            sage: a = R.random_element()
            sage: a * ~a == 1
            True
        """
    def add_bigoh(self, prec):
        """
        Return a new element with absolute precision decreased to
        the specified precision.

        INPUT:

        - ``prec`` -- integer or infinity

        EXAMPLES::

           sage: R = ZpLC(7)
           sage: a = R(8); a.add_bigoh(1)
           1 + O(7)
           sage: b = R(0); b.add_bigoh(3)
           O(7^3)

           sage: R = QpLC(7, 4)
           sage: a = R(8); a.add_bigoh(1)
           1 + O(7)
           sage: b = R(0); b.add_bigoh(3)
           O(7^3)

           The precision never increases::

           sage: R(4).add_bigoh(2).add_bigoh(4)
           4 + O(7^2)

        If ``prec`` is negative, the output is an element of the
        fraction field::

           sage: c = a.add_bigoh(-1); c
           O(7^-1)
           sage: c.parent()
           7-adic Field with lattice-cap precision
        """
    def lift_to_precision(self, prec=None, infer_precision: bool = False):
        """
        Return another element of the same parent with absolute precision
        at least ``prec``, congruent to this `p`-adic element modulo the
        precision of this element.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision of the result. If ``None``, lifts to the
          maximum precision allowed.

        - ``infer_precision`` -- boolean (default: ``False``)

        NOTE:

        In the lattice precision model, the precision of all variables is
        handled globally by a unique object, namely a lattice in a certain
        vector space.

        When ``infer_precision`` is set to ``True``, the precision lattice
        is recomputed. This may affect the precision of other variables
        with the same parent.

        When ``infer_precision`` is set to ``False``, the precision on the
        newly created variable is independent as if the variable were created
        by hand by setting independently the value of the absolute precision.
        In particular, if ``self`` used to share diffused digits of precision
        with other variables, they are not preserved.

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(1, 10); x
            1 + O(2^10)
            sage: x.lift_to_precision(15)
            1 + O(2^15)
            sage: x.lift_to_precision()
            1 + O(2^20)

        An example with diffused digits of precision::

            sage: x = R(1, 10); y = R(1, 5)
            sage: u = x+y; u
            2 + O(2^5)
            sage: v = x-y; v
            O(2^5)
            sage: u + v
            2 + O(2^11)

        The gain of precision on ``u + v`` is due to the presence of diffused
        digits of precision between ``u`` and ``v``.

        However, if we call :meth:`lift_to_precision` on one of these variables,
        these diffused digits are lost and the precision on the sum is no longer
        sharp::

            sage: u.lift_to_precision() + v
            2 + O(2^5)

        We can avoid this issue as follows::

            sage: u.lift_to_precision(infer_precision=True) + v
            2 + O(2^11)

        But now the precision on ``y`` has changed::

            sage: y
            1 + O(2^10)

        Indeed if the absolute precision on ``u = x+y`` (resp. on ``x``)
        is 20 (resp. 10), we deduce that the absolution precision on
        ``y = u-x`` is 10.

        .. SEEALSO::

            :meth:`lift_to_precision` of the precision object
        """
    def is_zero(self, prec=None):
        """
        Return ``True`` if this element is indistinguishable from zero
        at the given precision (if given).

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``)

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(2/5, 10); x
            2 + 2^3 + 2^4 + 2^7 + 2^8 + O(2^10)
            sage: x.is_zero()
            False
            sage: x.is_zero(1)
            True

            sage: (5*x-2).is_zero()
            True
            sage: 5*x == 2   # indirect doctest
            True
        """
    def lift(self):
        """
        Return an integer or rational congruent to this element modulo
        its absolute precision.
        If a rational is returned, its denominator will be a power of `p`.

        EXAMPLES::

           sage: R = ZpLC(7)
           sage: a = R(8); a.lift()
           8

           sage: R = QpLC(7)
           sage: a = R(8); a.lift()
           8
           sage: b = R(8/7); b.lift()
           8/7
        """
    def __rshift__(self, n):
        """
        Divide this element by ``p^n``, and truncate
        (if the parent is not a field).

        EXAMPLES::

            sage: R = ZpLC(997, 7)
            sage: a = R(123456878908); a
            964*997 + 572*997^2 + 124*997^3 + O(997^8)

            sage: S = ZpLC(5)
            sage: b = S(17); b
            2 + 3*5 + O(5^20)

        Shifting to the right divides by a power of `p`, but drops
        terms with negative valuation::

            sage: a >> 3
            124 + O(997^5)
            sage: b >> 1
            3 + O(5^19)
            sage: b >> 40
            O(5^0)

        If the parent is a field no truncation is performed::

            sage: K = QpLC(5)
            sage: b = K(17); b
            2 + 3*5 + O(5^20)
            sage: b >> 1
            2*5^-1 + 3 + O(5^19)

        A negative shift multiplies by that power of `p`::

            sage: a >> -3
            964*997^4 + 572*997^5 + 124*997^6 + O(997^11)
            sage: b >> -5
            2*5^5 + 3*5^6 + O(5^25)
        """
    def __lshift__(self, n):
        """
        Multiply this element by ``p^n``.

        If ``n`` is negative and this element does not lie in a field,
        digits may be truncated.  See :meth:`__rshift__` for details.

        EXAMPLES::

            sage: R = ZpLC(5)
            sage: a = R(1000); a
            3*5^3 + 5^4 + O(5^23)
            sage: a >> 1
            3*5^2 + 5^3 + O(5^22)

            sage: S = Zp(5); b = S(1000); b
            3*5^3 + 5^4 + O(5^23)
        """
    def unit_part(self):
        """
        Return `u`, where this element is `p^v u` and `u` is a unit.

        EXAMPLES::

            sage: R = ZpLC(17)
            sage: a = R(18*17, 4)
            sage: a.unit_part()
            1 + 17 + O(17^3)

            sage: b=1/a; b
            17^-1 + 16 + O(17^2)
            sage: b.unit_part()
            1 + 16*17 + O(17^3)

        If the element is indistinguishable from zero, an error is raised::

            sage: c = R(0, 5); c
            O(17^5)
            sage: c.unit_part()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision
        """
    def val_unit(self):
        """
        Return the pair `(v, u)`, where this element is
        `p^v u` and `u` is a unit.

        EXAMPLES::

            sage: R = ZpLC(17)
            sage: a = R(18*17, 4)
            sage: a.val_unit()
            (1, 1 + 17 + O(17^3))

            sage: b=1/a; b
            17^-1 + 16 + O(17^2)
            sage: b.val_unit()
            (-1, 1 + 16*17 + O(17^3))

        If the element is indistinguishable from zero, an error is raised

            sage: c = R(0, 5); c
            O(17^5)
            sage: c.val_unit()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision
        """
    def __copy__(self):
        """
        Return a copy of this element.

        TESTS::

            sage: R = ZpLC(2)
            sage: x = R(1, 10); x
            1 + O(2^10)
            sage: y = copy(x)   # indirect doctest
            sage: y
            1 + O(2^10)

            sage: x - y
            O(2^20)
        """
    def expansion(self, n=None, lift_mode: str = 'simple', start_val=None):
        """
        Return a list giving the `p`-adic expansion of this element.
        If this is a field element, start at
        `p^{\\mbox{valuation}}`, if a ring element at `p^0`.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``); if given,
          return the corresponding entry in the expansion

        - ``lift_mode`` -- string (default: ``'simple'``); currently
          only ``'simple'`` is implemented

        - ``start_val`` -- integer or ``None`` (default: ``None``);
          start at this valuation rather than the default (`0` or the
          valuation of this element).

        EXAMPLES::

            sage: R = ZpLC(5, 10)
            sage: x = R(123456789); x
            4 + 2*5 + 5^2 + 4*5^3 + 5^5 + 5^6 + 5^8 + 3*5^9 + O(5^10)
            sage: x.expansion()
            [4, 2, 1, 4, 0, 1, 1, 0, 1, 3]

            sage: x.expansion(3)
            4

            sage: x.expansion(start_val=5)
            [1, 1, 0, 1, 3]

        If any, trailing zeros are included in the expansion::

            sage: y = R(1234); y
            4 + 5 + 4*5^2 + 4*5^3 + 5^4 + O(5^10)
            sage: y.expansion()
            [4, 1, 4, 4, 1, 0, 0, 0, 0, 0]
        """
    def dist(self, other):
        """
        Return the distance between this element and ``other``.
        The distance is normalized so that `dist(0,p) = 1/p`.

        EXAMPLES::

            sage: R = ZpLC(3)
            sage: x = R(1, 5)
            sage: y = R(4, 5)
            sage: x.dist(y)
            1/3

        TESTS::

            sage: z = R(3^7,10)
            sage: x
            1 + O(3^5)
            sage: x + z
            1 + O(3^5)
            sage: x.dist(x+z)
            1/2187
        """

class pAdicLatticeCapElement(pAdicLatticeElement): ...
class pAdicLatticeFloatElement(pAdicLatticeElement): ...
