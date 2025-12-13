import sage.rings.abc
from .lattice_precision import PrecisionLattice as PrecisionLattice, PrecisionModule as PrecisionModule
from .padic_lattice_element import pAdicLatticeCapElement as pAdicLatticeCapElement, pAdicLatticeElement as pAdicLatticeElement, pAdicLatticeFloatElement as pAdicLatticeFloatElement
from sage.rings.infinity import SignError as SignError, infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.local_generic import LocalGeneric as LocalGeneric
from sage.rings.padics.padic_base_generic import pAdicBaseGeneric as pAdicBaseGeneric
from sage.rings.padics.padic_generic import pAdicGeneric as pAdicGeneric
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ

class CappedAbsoluteGeneric(LocalGeneric):
    def is_capped_absolute(self):
        """
        Return whether this `p`-adic ring bounds precision in a
        capped absolute fashion.

        The absolute precision of an element is the power of `p` modulo
        which that element is defined.  In a capped absolute ring, the
        absolute precision of elements are bounded by a constant
        depending on the ring.

        EXAMPLES::

            sage: R = ZpCA(5, 15)
            sage: R.is_capped_absolute()
            True
            sage: R(5^7)
            5^7 + O(5^15)
            sage: S = Zp(5, 15)
            sage: S.is_capped_absolute()
            False
            sage: S(5^7)
            5^7 + O(5^22)
        """

class CappedRelativeGeneric(LocalGeneric):
    def is_capped_relative(self):
        """
        Return whether this `p`-adic ring bounds precision in a capped
        relative fashion.

        The relative precision of an element is the power of p modulo
        which the unit part of that element is defined.  In a capped
        relative ring, the relative precision of elements are bounded
        by a constant depending on the ring.

        EXAMPLES::

            sage: R = ZpCA(5, 15)
            sage: R.is_capped_relative()
            False
            sage: R(5^7)
            5^7 + O(5^15)
            sage: S = Zp(5, 15)
            sage: S.is_capped_relative()
            True
            sage: S(5^7)
            5^7 + O(5^22)
        """

class FixedModGeneric(LocalGeneric):
    def is_fixed_mod(self):
        """
        Return whether this `p`-adic ring bounds precision in a fixed
        modulus fashion.

        The absolute precision of an element is the power of p modulo
        which that element is defined.  In a fixed modulus ring, the
        absolute precision of every element is defined to be the
        precision cap of the parent.  This means that some operations,
        such as division by `p`, don't return a well defined answer.

        EXAMPLES::

            sage: R = ZpFM(5,15)
            sage: R.is_fixed_mod()
            True
            sage: R(5^7,absprec=9)
            5^7
            sage: S = ZpCA(5, 15)
            sage: S.is_fixed_mod()
            False
            sage: S(5^7,absprec=9)
            5^7 + O(5^9)
        """

class FloatingPointGeneric(LocalGeneric):
    def is_floating_point(self):
        """
        Return whether this `p`-adic ring uses a floating point precision model.

        Elements in the floating point model are stored by giving a
        valuation and a unit part.  Arithmetic is done where the unit
        part is truncated modulo a fixed power of the uniformizer,
        stored in the precision cap of the parent.

        EXAMPLES::

            sage: R = ZpFP(5,15)
            sage: R.is_floating_point()
            True
            sage: R(5^7,absprec=9)
            5^7
            sage: S = ZpCR(5,15)
            sage: S.is_floating_point()
            False
            sage: S(5^7,absprec=9)
            5^7 + O(5^9)
        """

class FloatingPointRingGeneric(FloatingPointGeneric): ...
class FloatingPointFieldGeneric(FloatingPointGeneric): ...
class CappedRelativeRingGeneric(CappedRelativeGeneric): ...
class CappedRelativeFieldGeneric(CappedRelativeGeneric): ...

class pAdicLatticeGeneric(pAdicGeneric):
    """
    An implementation of the `p`-adic rationals with lattice precision.

    INPUT:

    - ``p`` -- the underlying prime number

    - ``prec`` -- the precision

    - ``subtype`` -- either ``'cap'`` or ``'float'``,
      specifying the precision model used for tracking precision

    - ``label`` -- string or ``None`` (default: ``None``)

    TESTS::

        sage: R = ZpLC(17)   # indirect doctest
        doctest:...: FutureWarning: This class/method/function is marked as experimental. It, its functionality or its interface might change without a formal deprecation.
        See https://github.com/sagemath/sage/issues/23505 for details.
        sage: R._prec_type()
        'lattice-cap'

        sage: R = ZpLF(17)   # indirect doctest
        sage: R._prec_type()
        'lattice-float'

        sage: R = QpLC(17)   # indirect doctest
        sage: R._prec_type()
        'lattice-cap'

        sage: R = QpLF(17)   # indirect doctest
        sage: R._prec_type()
        'lattice-float'
    """
    def __init__(self, p, prec, print_mode, names, label=None, category=None) -> None:
        """
        Initialization.

        TESTS::

            sage: R = ZpLC(17)   # indirect doctest
            sage: R._prec_type()
            'lattice-cap'
            sage: R._subtype
            'cap'

            sage: R = ZpLF(17)   # indirect doctest
            sage: R._prec_type()
            'lattice-float'
            sage: R._subtype
            'float'
        """
    def is_lattice_prec(self):
        """
        Return whether this `p`-adic ring bounds precision using
        a lattice model.

        In lattice precision, relationships between elements
        are stored in a precision object of the parent, which
        allows for optimal precision tracking at the cost of
        increased memory usage and runtime.

        EXAMPLES::

            sage: R = ZpCR(5, 15)
            sage: R.is_lattice_prec()
            False
            sage: x = R(25, 8)
            sage: x - x
            O(5^8)
            sage: S = ZpLC(5, 15)
            sage: S.is_lattice_prec()
            True
            sage: x = S(25, 8)
            sage: x - x
            O(5^30)
        """
    def precision_cap(self):
        """
        Return the relative precision cap for this ring if it is finite.
        Otherwise return the absolute precision cap.

        EXAMPLES::

            sage: R = ZpLC(3)
            sage: R.precision_cap()
            20
            sage: R.precision_cap_relative()
            20

            sage: R = ZpLC(3, prec=(infinity,20))
            sage: R.precision_cap()
            20
            sage: R.precision_cap_relative()
            +Infinity
            sage: R.precision_cap_absolute()
            20

        .. SEEALSO::

            :meth:`precision_cap_relative`, :meth:`precision_cap_absolute`
        """
    def precision_cap_relative(self):
        """
        Return the relative precision cap for this ring.

        EXAMPLES::

            sage: R = ZpLC(3)
            sage: R.precision_cap_relative()
            20

            sage: R = ZpLC(3, prec=(infinity,20))
            sage: R.precision_cap_relative()
            +Infinity

        .. SEEALSO::

            :meth:`precision_cap`, :meth:`precision_cap_absolute`
        """
    def precision_cap_absolute(self):
        """
        Return the absolute precision cap for this ring.

        EXAMPLES::

            sage: R = ZpLC(3)
            sage: R.precision_cap_absolute()
            40

            sage: R = ZpLC(3, prec=(infinity,20))
            sage: R.precision_cap_absolute()
            20

        .. SEEALSO::

            :meth:`precision_cap`, :meth:`precision_cap_relative`
        """
    def precision(self):
        """
        Return the lattice precision object attached to this parent.

        EXAMPLES::

            sage: R = ZpLC(5, label='precision')
            sage: R.precision()
            Precision lattice on 0 objects (label: precision)

            sage: x = R(1, 10); y = R(1, 5)
            sage: R.precision()
            Precision lattice on 2 objects (label: precision)

        .. SEEALSO::

            :class:`sage.rings.padics.lattice_precision.PrecisionLattice`
        """
    def label(self):
        """
        Return the label of this parent.

        NOTE:

        Labels can be used to distinguish between parents with
        the same defining data.

        They are useful in the lattice precision framework in order
        to limit the size of the lattice modeling the precision (which
        is roughly the number of elements having this parent).

        Elements of a parent with some label do not coerce to a parent
        with a different label. However conversions are allowed.

        EXAMPLES::

            sage: R = ZpLC(5)
            sage: R.label()  # no label by default

            sage: R = ZpLC(5, label='mylabel')
            sage: R.label()
            'mylabel'

        Labels are typically useful to isolate computations.
        For example, assume that we first want to do some calculations
        with matrices::

            sage: R = ZpLC(5, label='matrices')
            sage: M = random_matrix(R, 4, 4)                                            # needs sage.geometry.polyhedron
            sage: d = M.determinant()                                                   # needs sage.geometry.polyhedron

        Now, if we want to do another unrelated computation, we can
        use a different label::

            sage: R = ZpLC(5, label='polynomials')
            sage: S.<x> = PolynomialRing(R)
            sage: P = (x-1)*(x-2)*(x-3)*(x-4)*(x-5)

        Without labels, the software would have modeled the
        precision on the matrices and on the polynomials using the same
        lattice (manipulating a lattice of higher
        dimension can have a significant impact on performance).
        """
    def convert_multiple(self, *elts):
        """
        Convert a list of elements to this parent.

        NOTE:

        This function tries to be sharp on precision as much as
        possible.
        In particular, if the precision of the input elements are
        handled by a lattice, diffused digits of precision are
        preserved during the conversion.

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: x = R(1, 10); y = R(1, 5)
            sage: x,y = x+y, x-y

        Remark that the pair `(x,y)` has diffused digits of precision::

            sage: x
            2 + O(2^5)
            sage: y
            O(2^5)
            sage: x + y
            2 + O(2^11)

            sage: R.precision().diffused_digits([x,y])                                  # needs sage.geometry.polyhedron
            6

        As a consequence, if we convert ``x`` and ``y`` separately, we
        lose some precision::

            sage: R2 = ZpLC(2, label='copy')
            sage: x2 = R2(x); y2 = R2(y)
            sage: x2
            2 + O(2^5)
            sage: y2
            O(2^5)
            sage: x2 + y2
            2 + O(2^5)

            sage: R2.precision().diffused_digits([x2,y2])                               # needs sage.geometry.polyhedron
            0

        On the other hand, this issue disappears when we use multiple
        conversion::

            sage: x2,y2 = R2.convert_multiple(x,y)                                      # needs sage.geometry.polyhedron
            sage: x2 + y2                                                               # needs sage.rings.padics
            2 + O(2^11)

            sage: R2.precision().diffused_digits([x2,y2])                               # needs sage.geometry.polyhedron
            6
        """

class pAdicRelaxedGeneric(pAdicGeneric):
    """
    Generic class for relaxed `p`-adics.

    INPUT:

    - ``p`` -- the underlying prime number

    - ``prec`` -- the default precision

    TESTS::

        sage: R = ZpER(17)   # indirect doctest                                         # needs sage.libs.flint
        sage: R._prec_type()                                                            # needs sage.libs.flint
        'relaxed'
    """
    def is_relaxed(self):
        """
        Return whether this `p`-adic ring is relaxed.

        EXAMPLES::

            sage: R = Zp(5)
            sage: R.is_relaxed()
            False
            sage: S = ZpER(5)                                                           # needs sage.libs.flint
            sage: S.is_relaxed()                                                        # needs sage.libs.flint
            True
        """
    def is_secure(self):
        """
        Return ``False`` if this `p`-adic relaxed ring is not secure
        (i.e., if indistinguishable elements at the working precision
        are considered as equal); ``True`` otherwise (in which case,
        an error is raised when equality cannot be decided).

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R = ZpER(5)
            sage: R.is_secure()
            False
            sage: x = R(20/21)
            sage: y = x + 5^50
            sage: x == y
            True

            sage: # needs sage.libs.flint
            sage: S = ZpER(5, secure=True)
            sage: S.is_secure()
            True
            sage: x = S(20/21)
            sage: y = x + 5^50
            sage: x == y
            Traceback (most recent call last):
            ...
            PrecisionError: unable to decide equality; try to bound precision
        """
    def default_prec(self):
        """
        Return the default precision of this relaxed `p`-adic ring.

        The default precision is mostly used for printing: it is the
        number of digits which are printed for unbounded elements
        (that is elements having infinite absolute precision).

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R = ZpER(5, print_mode='digits')
            sage: R.default_prec()
            20
            sage: R(1/17)
            ...34024323104201213403
            sage: S = ZpER(5, prec=10, print_mode='digits')
            sage: S.default_prec()
            10
            sage: S(1/17)
            ...4201213403
        """
    def halting_prec(self):
        """
        Return the default halting precision of this relaxed `p`-adic ring.

        The halting precision is the precision at which elements of this
        parent are compared (unless more digits have been previously
        computed).
        By default, it is twice the default precision.

        EXAMPLES::

            sage: R = ZpER(5, print_mode='digits')                                      # needs sage.libs.flint
            sage: R.halting_prec()                                                      # needs sage.libs.flint
            40
        """
    def precision_cap(self):
        """
        Return the precision cap of this `p`-adic ring, which is infinite
        in the case of relaxed rings.

        EXAMPLES::

            sage: R = ZpER(5)                                                           # needs sage.libs.flint
            sage: R.precision_cap()                                                     # needs sage.libs.flint
            +Infinity
        """
    def an_element(self, unbounded: bool = False):
        """
        Return an element in this ring.

        EXAMPLES::

            sage: R = ZpER(7, prec=5)                                                   # needs sage.libs.flint
            sage: R.an_element()                                                        # needs sage.libs.flint
            7 + O(7^5)
            sage: R.an_element(unbounded=True)                                          # needs sage.libs.flint
            7 + ...
        """
    def some_elements(self, unbounded: bool = False):
        """
        Return a list of elements in this ring.

        This is typically used for running generic tests (see :class:`TestSuite`).

        EXAMPLES::

            sage: R = ZpER(7, prec=5)                                                   # needs sage.libs.flint
            sage: R.some_elements()                                                     # needs sage.libs.flint
            [O(7^5),
             1 + O(7^5),
             7 + O(7^5),
             7 + O(7^5),
             1 + 5*7 + 3*7^2 + 6*7^3 + O(7^5),
             7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)]

            sage: R.some_elements(unbounded=True)                                       # needs sage.libs.flint
            [0,
             1 + ...,
             7 + ...,
             7 + ...,
             1 + 5*7 + 3*7^2 + 6*7^3 + ...,
             7 + 6*7^2 + 6*7^3 + 6*7^4 + ...]
        """
    def unknown(self, start_val: int = 0, digits=None):
        """
        Return a self-referent number in this ring.

        INPUT:

        - ``start_val`` -- integer (default: 0); a lower bound on the
          valuation of the returned element

        - ``digits`` -- an element, a list, or ``None`` (default: ``None``);
          the first digit or the list of the digits of the returned element

        NOTE:

        Self-referent numbers are numbers whose digits are defined in terms
        of the previous ones. This method is used to declare a self-referent
        number (and optionally, to set its first digits).
        The definition of the number itself will be given afterwords using
        to method :meth:`sage.rings.padics.relaxed_template.RelaxedElement_unknown.set`
        of the element.

        EXAMPLES:

            sage: R = ZpER(5, prec=10)                                                  # needs sage.libs.flint

        We declare a self-referent number::

            sage: a = R.unknown()                                                       # needs sage.libs.flint

        So far, we do not know anything on `a` (except that it has nonnegative
        valuation)::

            sage: a                                                                     # needs sage.libs.flint
            O(5^0)

        We can now use the method :meth:`sage.rings.padics.relaxed_template.RelaxedElement_unknown.set`
        to define `a`. Below, for example, we say that the digits of `a` have to
        agree with the digits of `1 + 5 a`. Note that the factor `5` shifts the
        digits; the `n`-th digit of `a` is then defined by the previous ones::

            sage: a.set(1 + 5*a)                                                        # needs sage.libs.flint
            True

        After this, `a` contains the solution of the equation `a = 1 + 5 a`, that
        is `a = -1/4`::

            sage: a                                                                     # needs sage.libs.flint
            1 + 5 + 5^2 + 5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 5^8 + 5^9 + ...

        Here is another example with an equation of degree `2`::

            sage: # needs sage.libs.flint
            sage: b = R.unknown()
            sage: b.set(1 - 5*b^2)
            True
            sage: b
            1 + 4*5 + 5^2 + 3*5^4 + 4*5^6 + 4*5^8 + 2*5^9 + ...
            sage: (sqrt(R(21)) - 1) / 10
            1 + 4*5 + 5^2 + 3*5^4 + 4*5^6 + 4*5^8 + 2*5^9 + ...

        Cross self-referent definitions are also allowed::

            sage: # needs sage.libs.flint
            sage: u = R.unknown()
            sage: v = R.unknown()
            sage: w = R.unknown()
            sage: u.set(1 + 2*v + 3*w^2 + 5*u*v*w)
            True
            sage: v.set(2 + 4*w + sqrt(1 + 5*u + 10*v + 15*w))
            True
            sage: w.set(3 + 25*(u*v + v*w + u*w))
            True
            sage: u
            3 + 3*5 + 4*5^2 + 5^3 + 3*5^4 + 5^5 + 5^6 + 3*5^7 + 5^8 + 3*5^9 + ...
            sage: v
            4*5 + 2*5^2 + 4*5^3 + 5^4 + 5^5 + 3*5^6 + 5^8 + 5^9 + ...
            sage: w
            3 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 2*5^6 + 5^8 + 5^9 + ...

        TESTS::

            sage: # needs sage.libs.flint
            sage: a = R.unknown()
            sage: a.set(1 + 3*a)
            True
            sage: a
            O(5^0)
            sage: a.at_precision_absolute(10)
            Traceback (most recent call last):
            ...
            RecursionError: definition looks circular
        """
    def random_element(self, integral: bool = False, prec=None):
        """
        Return a random element in this ring.

        INPUT:

        - ``integral`` -- boolean (default: ``False``); if ``True``,
          return a random element in the ring of integers of this ring

        - ``prec`` -- integer or ``None`` (default: ``None``);
          if given, bound the precision of the output to ``prec``

        EXAMPLES::

            sage: R = ZpER(5, prec=10)                                                  # needs sage.libs.flint

        By default, this method returns a unbounded element::

            sage: a = R.random_element()                                                # needs sage.libs.flint
            sage: a  # random                                                           # needs sage.libs.flint
            4 + 3*5 + 3*5^2 + 5^3 + 3*5^4 + 2*5^5 + 2*5^6 + 5^7 + 5^9 + ...
            sage: a.precision_absolute()                                                # needs sage.libs.flint
            +Infinity

        The precision can be bounded by passing in a precision::

            sage: b = R.random_element(prec=15)                                         # needs sage.libs.flint
            sage: b  # random                                                           # needs sage.libs.flint
            2 + 3*5^2 + 5^3 + 3*5^4 + 5^5 + 3*5^6 + 3*5^8 + 3*5^9 + 4*5^10
             + 5^11 + 4*5^12 + 5^13 + 2*5^14 + O(5^15)
            sage: b.precision_absolute()                                                # needs sage.libs.flint
            15
        """
    def teichmuller(self, x):
        """
        Return the Teichmuller representative of `x`.

        EXAMPLES::

            sage: R = ZpER(5, print_mode='digits')                                      # needs sage.libs.flint
            sage: R.teichmuller(2)                                                      # needs sage.libs.flint
            ...40423140223032431212
        """
    def teichmuller_system(self):
        """
        Return a set of teichmuller representatives for the invertible elements
        of `\\ZZ / p\\ZZ`.

        EXAMPLES::

            sage: R = ZpER(7, print_mode='digits')                                      # needs sage.libs.flint
            sage: R.teichmuller_system()                                                # needs sage.libs.flint
            [...00000000000000000001,
             ...16412125443426203642,
             ...16412125443426203643,
             ...50254541223240463024,
             ...50254541223240463025,
             ...66666666666666666666]
        """

class pAdicRingGeneric(pAdicGeneric, sage.rings.abc.pAdicRing):
    def is_field(self, proof: bool = True):
        """
        Return whether this ring is actually a field, ie ``False``.

        EXAMPLES::

            sage: Zp(5).is_field()
            False
        """
    def krull_dimension(self):
        """
        Return the Krull dimension of self, i.e. 1.

        INPUT:

        - ``self`` -- a `p`-adic ring

        OUTPUT: the Krull dimension of ``self``.  Since ``self`` is a `p`-adic
        ring, this is 1.

        EXAMPLES::

            sage: Zp(5).krull_dimension()
            1
        """

class pAdicFieldGeneric(pAdicGeneric, sage.rings.abc.pAdicField):
    def is_field(self, proof: bool = True):
        """
        Return whether this ring is actually a field, ie ``True``.

        EXAMPLES::

            sage: Qp(5).is_field()
            True
        """

class pAdicFixedModRingGeneric(pAdicRingGeneric, FixedModGeneric): ...
class pAdicCappedAbsoluteRingGeneric(pAdicRingGeneric, CappedAbsoluteGeneric): ...
class pAdicCappedRelativeRingGeneric(pAdicRingGeneric, CappedRelativeRingGeneric): ...
class pAdicCappedRelativeFieldGeneric(pAdicFieldGeneric, CappedRelativeFieldGeneric): ...
class pAdicFloatingPointRingGeneric(pAdicRingGeneric, FloatingPointRingGeneric): ...
class pAdicFloatingPointFieldGeneric(pAdicFieldGeneric, FloatingPointFieldGeneric): ...

class pAdicRingBaseGeneric(pAdicBaseGeneric, pAdicRingGeneric):
    def construction(self, forbid_frac_field: bool = False):
        """
        Return the functorial construction of ``self``, namely,
        completion of the rational numbers with respect to a given prime.

        Also preserves other information that makes this field unique
        (e.g., precision, rounding, print mode).

        INPUT:

        - ``forbid_frac_field`` -- ignored, for compatibility with other `p`-adic types

        EXAMPLES::

            sage: K = Zp(17, 8, print_mode='val-unit', print_sep='&')
            sage: c, L = K.construction(); L
            Integer Ring
            sage: c(L)
            17-adic Ring with capped relative precision 8
            sage: K == c(L)
            True

        TESTS::

            sage: R = ZpLC(13,(31,41))
            sage: R._precision_cap()
            (31, 41)
            sage: F, Z = R.construction()
            sage: S = F(Z)
            sage: S._precision_cap()
            (31, 41)

        The `secure` attribute for relaxed type is included in the functor::

            sage: R = ZpER(5, secure=True)                                              # needs sage.libs.flint
            sage: R.construction()                                                      # needs sage.libs.flint
            (Completion[5, prec=(20, 40, True)], Integer Ring)
        """
    def random_element(self, algorithm: str = 'default'):
        """
        Return a random element of ``self``, optionally using the
        ``algorithm`` argument to decide how it generates the
        element. Algorithms currently implemented:

        - ``'default'``: Choose `a_i`, `i \\geq 0`, randomly between `0` and
          `p-1` until a nonzero choice is made. Then continue choosing
          `a_i` randomly between `0` and `p-1` until we reach
          precision_cap, and return `\\sum a_i p^i`.

        EXAMPLES::

            sage: Zp(5,6).random_element().parent() is Zp(5,6)
            True
            sage: ZpCA(5,6).random_element().parent() is ZpCA(5,6)
            True
            sage: ZpFM(5,6).random_element().parent() is ZpFM(5,6)
            True
        """

class pAdicFieldBaseGeneric(pAdicBaseGeneric, pAdicFieldGeneric):
    def composite(self, subfield1, subfield2):
        """
        Return the composite of two subfields of ``self``, i.e., the
        largest subfield containing both

        INPUT:

        - ``self`` -- a `p`-adic field
        - ``subfield1`` -- a subfield
        - ``subfield2`` -- a subfield

        OUTPUT: the composite of ``subfield1`` and ``subfield2``

        EXAMPLES::

            sage: K = Qp(17); K.composite(K, K) is K
            True
        """
    def subfields_of_degree(self, n):
        """
        Return the number of subfields of ``self`` of degree `n`.

        INPUT:

        - ``self`` -- a `p`-adic field
        - ``n`` -- integer

        OUTPUT:

        integer -- the number of subfields of degree `n` over ``self.base_ring()``

        EXAMPLES::

            sage: K = Qp(17)
            sage: K.subfields_of_degree(1)
            1
        """
    def subfield(self, list):
        """
        Return the subfield generated by the elements in ``list``.

        INPUT:

        - ``self`` -- a `p`-adic field
        - ``list`` -- list of elements of ``self``

        OUTPUT: the subfield of ``self`` generated by the elements of ``list``

        EXAMPLES::

            sage: K = Qp(17); K.subfield([K(17), K(1827)]) is K
            True
        """
    def construction(self, forbid_frac_field: bool = False):
        """
        Return the functorial construction of ``self``, namely,
        completion of the rational numbers with respect a given prime.

        Also preserves other information that makes this field unique
        (e.g., precision, rounding, print mode).

        INPUT:

        - ``forbid_frac_field`` -- require a completion functor rather
          than a fraction field functor.  This is used in the
          :meth:`sage.rings.padics.local_generic.LocalGeneric.change` method.

        EXAMPLES::

            sage: K = Qp(17, 8, print_mode='val-unit', print_sep='&')
            sage: c, L = K.construction(); L
            17-adic Ring with capped relative precision 8
            sage: c
            FractionField
            sage: c(L)
            17-adic Field with capped relative precision 8
            sage: K == c(L)
            True

        We can get a completion functor by forbidding the fraction field::

            sage: c, L = K.construction(forbid_frac_field=True); L
            Rational Field
            sage: c
            Completion[17, prec=8]
            sage: c(L)
            17-adic Field with capped relative precision 8
            sage: K == c(L)
            True

        TESTS::

            sage: R = QpLC(13,(31,41))
            sage: R._precision_cap()
            (31, 41)
            sage: F, Z = R.construction()
            sage: S = F(Z)
            sage: S._precision_cap()
            (31, 41)

        The `secure` attribute for relaxed type is included in the functor::

            sage: K = QpER(5, secure=True)                                              # needs sage.libs.flint
            sage: K.construction(forbid_frac_field=True)                                # needs sage.libs.flint
            (Completion[5, prec=(20, 40, True)], Rational Field)
        """
