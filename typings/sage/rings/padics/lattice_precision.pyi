from _typeshed import Incomplete
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.timing import walltime as walltime
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

DEFAULT_THRESHOLD_DELETION: int
STARTING_ADDITIONAL_PREC: int

class pRational:
    """
    This class implements rational numbers viewed as elements of ``Qp``.
    In particular, it provides additional methods which are specific to
    `p`-adics (as `p`-adic valuation).

    Only for internal use.

    INPUT:

    - ``p`` -- a prime number

    - ``x`` -- a rational number

    - ``exponent`` -- integer (default: 0)

    - ``valuation`` -- integer or ``None`` (default: ``None``);
      the `p`-adic valuation of this element

    If not ``None``, this method trusts the given value to the
    attribute ``valuation``.

    TESTS::

        sage: from sage.rings.padics.lattice_precision import pRational
        sage: x = pRational(2, 5); x
        5
        sage: y = pRational(2, 5/3, 2); y
        2^2 * 5/3

        sage: x + y
        35/3
        sage: x - y
        -5/3
        sage: x * y
        2^2 * 25/3
        sage: x / y
        2^-2 * 3

        sage: x.valuation()
        0
        sage: y.valuation()
        2

        sage: z = pRational(2, 1024, valuation=4)
        sage: z
        1024
        sage: z.valuation()
        4
    """
    p: Incomplete
    x: Incomplete
    exponent: Incomplete
    def __init__(self, p, x, exponent: int = 0, valuation=None) -> None:
        """
        Construct the element ``x * p^exponent``.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: pRational(2, 5)
            5
            sage: pRational(2, 5/3, 2)
            2^2 * 5/3
        """
    def reduce(self, prec):
        """
        Return this element reduced modulo ``p^prec``.

        INPUT:

        - ``prec`` -- integer

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 1234567); x
            1234567
            sage: x.reduce(12)
            1671

            sage: x = pRational(2, 1234/567); x
            1234/567
            sage: x.reduce(12)
            190
        """
    def reduce_relative(self, prec):
        """
        Return this element reduced modulo ``p^n`` where ``n = prec + val(x)``.

        INPUT:

        - ``prec`` -- nonnegative integer

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 1234567); x
            1234567
            sage: x.reduce_relative(12)
            1671

            sage: x = pRational(2, 1234/567); x
            1234/567
            sage: x.reduce_relative(12)
            190
        """
    def normalize(self) -> None:
        """
        Normalize this element, i.e. write it as ``p^v * u`` where
        ``u`` is coprime to `p`.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x.normalize(); x
            2^13 * 1929
        """
    def valuation(self):
        """
        Return the `p`-adic valuation of this element.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x.valuation()
            13
        """
    def is_p_power(self):
        """
        Return ``True`` if this element is a power of `p`.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 1024, 2); x
            2^2 * 1024
            sage: x.is_p_power()
            True

            sage: y = pRational(2, 123456, 7); y
            2^7 * 123456
            sage: y.is_p_power()
            False
        """
    def is_zero(self):
        """
        Return ``True`` if this element vanishes.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x.is_zero()
            False

            sage: (x-x).is_zero()
            True
        """
    def __add__(self, other):
        """
        Return the sum of ``self`` and ``other``.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: y = pRational(2, 891011, 12); y
            2^12 * 891011
            sage: x + y
            2^7 * 28635808
        """
    def __sub__(self, other):
        """
        Return the subtraction of ``self`` by ``other``.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: y = pRational(2, 891011, 12); y
            2^12 * 891011
            sage: x - y
            2^7 * -28388896
        """
    def __neg__(self):
        """
        Return the opposite of this element.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: -x
            2^7 * -123456
        """
    def __mul__(self, other):
        """
        Return the product of ``self`` and ``other``.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: y = pRational(2, 891011, 12); y
            2^12 * 891011
            sage: x * y
            2^19 * 110000654016
        """
    def __truediv__(self, other):
        """
        Return the quotient of ``self`` by ``other``.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: y = pRational(2, 891011, 12); y
            2^12 * 891011
            sage: x / y
            2^-5 * 123456/891011
        """
    def __lshift__(self, n):
        """
        Return the product of this element by ``p^n``.

        INPUT:

        - ``n`` -- relative integer

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x << 10
            2^17 * 123456
        """
    def __rshift__(self, n):
        """
        Return the quotient of this element by ``p^n``.

        INPUT:

        - ``n`` -- relative integer

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x >> 10
            2^-3 * 123456
        """
    def unit_part(self):
        """
        Return the unit part of this element, that is the part ``u``
        in the writing ``u * p^v`` with ``u`` coprime to `p`.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x.unit_part()
            1929
        """
    def xgcd(self, other):
        """
        Return the gcd of ``self`` and ``other`` together with two
        elements ``u`` and ``v`` such that ``u*self + v*other = gcd``.

        The ``gcd`` is normalized so that it is a power of `p`.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: y = pRational(2, 891011, 12); y
            2^12 * 891011

            sage: d, u, v = x.xgcd(y)
            sage: d
            2^7 * 32
            sage: d.normalize(); d
            2^12 * 1

            sage: u*x + v*y
            2^7 * 32
        """
    def value(self):
        """
        Return this element as a rational number.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456, 7); x
            2^7 * 123456
            sage: x.value()
            15802368
        """
    def list(self, prec):
        """
        Return the list of the digits of this element (written in radix
        `p`) up to position ``prec``.

        The first zeros are omitted.

        TESTS::

            sage: from sage.rings.padics.lattice_precision import pRational
            sage: x = pRational(2, 123456); x
            123456
            sage: x.list(5)
            []
            sage: x.list(20)
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]

            sage: y = pRational(2, 123/456); y
            41/152
            sage: y.list(10)
            [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]

            sage: z = pRational(2, 0)
            sage: z.list(10)
            []
            sage: z.list(100)
            []
        """

class DifferentialPrecisionGeneric(SageObject):
    """
    A generic class for precision objects obtained by automatic
    differentiation.

    INPUT:

    - ``p`` -- a prime number

    - ``label`` -- string; the label of the parents to which the elements
      belong that are tracked by this precision module

    .. NOTE::

        This object is used internally by the parent ring. You should not
        create instances of this class on your own.

    EXAMPLES::

        sage: R = ZpLC(2, label='init')
        sage: R.precision()
        Precision lattice on 0 objects (label: init)
    """
    def __init__(self, p, label) -> None:
        """
        TESTS::

            sage: prec = ZpLC(2, label='init').precision()
            sage: from sage.rings.padics.lattice_precision import DifferentialPrecisionGeneric
            sage: isinstance(prec, DifferentialPrecisionGeneric)
            True
        """
    def __reduce__(self) -> None:
        """
        TESTS::

            sage: R = ZpLF(2)
            sage: prec = R.precision()
            sage: dumps(prec)
            Traceback (most recent call last):
            ...
            NotImplementedError: pickling/unpickling precision modules is not implemented yet
        """
    def threshold_deletion(self, threshold=None):
        """
        Return (and set) the threshold for column deletion.

        When a variable dies, i.e., goes out of scope, the ambient space in
        which the precision module lives can be reduced (by projection onto the
        hyperplane defined by the dead variable).
        This reduction has a cost because it leads to re-echelonization
        of a part of the matrix that encodes the precision. The size of this
        part is roughly measured by the number of columns between the last
        column and the one corresponding to the dead variable.

        This threshold returned by this method is the maximal distance until
        which a column of a dead variable is removed and the matrix
        re-echelonized. Beyond the threshold, the column of the dead variable
        is kept in this matrix as if the variable were not destroyed.

        INPUT:

        - ``threshold`` -- nonnegative integer, ``Infinity`` or ``None``
          (default: ``None``); if not ``None`` set the threshold to the given
          value.

        .. NOTE::

            Setting the threshold to ``0`` disables the dimension reduction.

            Setting the threshold to ``Infinity`` forces the dimension reduction
            after each deletion.

        EXAMPLES::

            sage: R = ZpLC(2, label='threshold_deletion')
            sage: prec = R.precision()
            sage: prec.threshold_deletion()
            50

            sage: prec.threshold_deletion(20)
            20
            sage: prec.threshold_deletion()
            20

            sage: prec.threshold_deletion(-2)
            Traceback (most recent call last):
            ...
            ValueError: The threshold must be a nonnegative integer or Infinity
        """
    def prime(self):
        """
        Return the underlying prime number attached to this precision lattice.

        EXAMPLES::

            sage: R = ZpLC(2, label='mylabel')
            sage: R.precision().prime()
            2
        """
    def ambient_dimension(self):
        """
        Return the dimension of the vector space in which the precision
        module/lattice lives.

        EXAMPLES::

            sage: R = ZpLC(2, label='ambient_dim')
            sage: prec = R.precision()

            sage: x, y = R(1, 10), R(1, 5)
            sage: prec.ambient_dimension()
            2
            sage: prec.dimension()
            2

            sage: u = x + y
            sage: prec.ambient_dimension()
            3
            sage: prec.dimension()
            3

        In the case of ``ZpLC`` (lattice-cap precision), it is always
        equal to the dimension of the lattice.

        In the case of ``ZpLF`` (lattice-float precision), the precision
        object is not necessarily a lattice and then may have smaller
        dimension::

            sage: R = ZpLF(2, label='ambient_dim')
            sage: prec = R.precision()

            sage: x, y = R(1, 10), R(1, 5)
            sage: prec.ambient_dimension()
            2
            sage: prec.dimension()
            2

            sage: u = x + y
            sage: prec.ambient_dimension()
            3
            sage: prec.dimension()
            2
        """
    @abstract_method
    def dimension(self) -> None:
        """
        Return the dimension of this precision module.

        EXAMPLES::

            sage: R = ZpLC(5, label='dim')
            sage: prec = R.precision()
            sage: prec.dimension()
            0

            sage: x = R(1, 10)
            sage: prec.dimension()
            1
        """
    @abstract_method
    def del_elements(self, threshold=None) -> None:
        """
        Delete (or mark for future deletion) the columns of precision
        matrix corresponding to elements that were collected by the
        garbage collector.

        INPUT:

        - ``threshold`` -- integer or ``None`` (default: ``None``);
          a column whose distance to the right is greater than the
          threshold is not erased but marked for deletion.
          If ``None``, always erase (never mark for deletion).

        EXAMPLES::

            sage: R = ZpLC(2, label='del_elements')
            sage: prec = R.precision()

            sage: x = R(1, 10)
            sage: prec
            Precision lattice on 1 object (label: del_elements)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: del x
            sage: prec
            Precision lattice on 1 object (label: del_elements)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: prec.del_elements()
            sage: prec
            Precision lattice on 0 objects (label: del_elements)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            []
        """
    @abstract_method
    def precision_lattice(self, elements=None) -> None:
        """
        Return a lattice modeling the precision on the given set of elements
        or, if not given, on the whole set of elements tracked by the precision
        module.

        INPUT:

        - ``elements`` -- list of elements or ``None`` (default: ``None``)

        EXAMPLES::

            sage: R = ZpLC(2, label='precision_lattice')
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: u = x + y
            sage: v = x - y
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [         1024             0          1024          1024]
            [            0            32            32 1099511627744]
            [            0             0       2097152             0]
            [            0             0             0 1099511627776]
            sage: prec.precision_lattice([u, v])                                        # needs sage.geometry.polyhedron
            [  32 2016]
            [   0 2048]

        If the precision module does not project to a lattice,
        an error is raised. ::

            sage: R = ZpLF(2, label='precision_lattice')
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: u = x + y
            sage: v = x - y
            sage: prec.precision_lattice([x,y,u,v])                                     # needs sage.geometry.polyhedron
            Traceback (most recent call last):
            ...
            PrecisionError: the differential is not surjective
        """
    def diffused_digits(self, elements=None):
        """
        Return the number of diffused digits of precision within a
        subset of elements.

        A diffused digit of precision is a known digit which is not
        located on a single variable but only appears on a suitable
        linear combination of variables.

        The number of diffused digits of precision quantifies the
        quality of the approximation of the lattice precision by a
        jagged precision (that is a precision which is split over
        all variables).

        We refer to [CRV2018]_ for a detail exposition of the notion of
        diffused digits.

        EXAMPLES::

            sage: R = ZpLC(2)
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: u = x + y
            sage: v = x - y

            sage: prec.diffused_digits([x, y])                                          # needs sage.geometry.polyhedron
            0
            sage: prec.diffused_digits([u, v])                                          # needs sage.geometry.polyhedron
            6

        The elements `u` and `v` are known at absolute precision `O(2^5)`.
        However, the sum `u + v = 2x` is known at precision `O(2^11)`, that
        is with `6` more digits.
        That is where the `6` diffused digits of precision comes from.

        Here is another example with matrices::

            sage: M = matrix(R, 2, 2, [R(3, 5), R(7, 5), R(1, 5), R(11, 1)])            # needs sage.modules
            sage: N = M^10                                                              # needs sage.modules

        The next syntax provides as easy way to select an interesting
        subset of variables (the selected subset consists of the four
        entries of the matrix ``N``)::

            sage: prec.diffused_digits(N)                                               # needs sage.geometry.polyhedron sage.modules
            17

        Note that, in some cases, the number of diffused digits can be
        infinite::

            sage: R = ZpLF(2)
            sage: prec = R.precision()
            sage: x = R(1, 10)
            sage: y = x
            sage: prec.diffused_digits([x, y])                                          # needs sage.geometry.polyhedron
            +Infinity
        """
    def tracked_elements(self, values: bool = True, dead: bool = True):
        """
        Return the list of tracked elements.

        INPUT:

        - ``values`` -- boolean (default: ``True``); if ``False``,
          the method returns a list of weak references on tracked
          elements instead

        - ``dead`` -- boolean (default: ``True``); whether dead
          elements for which the corresponding column is still not
          erased should be listed or not

        EXAMPLES::

            sage: R = ZpLC(2, label='tracked')
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: prec.tracked_elements()
            [1 + O(2^10), 1 + O(2^5)]
            sage: prec.tracked_elements(values=False)
            [WeakProxy#...,
             WeakProxy#...,
             WeakProxy#...]
            sage: prec.tracked_elements(values=False, dead=False)
            [WeakProxy#...,
             WeakProxy#...]

            sage: # needs sage.rings.padics
            sage: u = x + y
            sage: v = x - y
            sage: prec.tracked_elements()
            [1 + O(2^10), 1 + O(2^5), 2 + O(2^5), O(2^5)]
            sage: prec.tracked_elements(values=False)
            [WeakProxy#...,
             WeakProxy#...,
             WeakProxy#...,
             WeakProxy#...,
             WeakProxy#...]
            sage: del x; del y
            sage: prec.tracked_elements()
            [None, None, 2 + O(2^5), O(2^5), None]
            sage: prec.tracked_elements(values=False)
            [WeakProxy#...,
             WeakProxy#...,
             WeakProxy#...]
        """
    def history_enable(self) -> None:
        """
        Enable history.

        We refer to the documentation of the method :meth:`history` for
        a complete documentation (including examples) about history.

        TESTS::

            sage: R = ZpLC(2, label='history_en')
            sage: prec = R.precision()

            sage: print(prec.history())  # history is disabled by default
            Traceback (most recent call last):
            ...
            ValueError: History is not tracked

            sage: prec.history_enable()
            sage: print(prec.history())
             Timings
               ---

        .. SEEALSO::

            :meth:`history`, :meth:`history_disable`, :meth:`history_clear`
        """
    def history_disable(self) -> None:
        """
        Disable history.

        We refer to the documentation of the method :meth:`history` for
        a complete documentation (including examples) about history.

        TESTS::

            sage: R = ZpLC(2, label='history_dis')
            sage: prec = R.precision()

            sage: print(prec.history())  # history is disabled by default
            Traceback (most recent call last):
            ...
            ValueError: History is not tracked

            sage: prec.history_enable()
            sage: print(prec.history())
             Timings
               ---

            sage: prec.history_disable()
            sage: print(prec.history())
            Traceback (most recent call last):
            ...
            ValueError: History is not tracked

        .. SEEALSO::

            :meth:`history`, :meth:`history_enable`, :meth:`history_clear`
        """
    def history_clear(self) -> None:
        """
        Clear history.

        We refer to the documentation of the method :meth:`history` for
        a complete documentation (including examples) about history.

        TESTS::

            sage: R = ZpLC(2, label='history_clear')
            sage: prec = R.precision()
            sage: prec.history_enable()

            sage: x = R(1, 10); y = R(1, 5)
            sage: x, y = x+y, x-y
            sage: print(prec.history())  # somewhat random
             Timings
            0.000213s  oooo

        When we clear history, only the last line is kept::

            sage: prec.history_clear()
            sage: print(prec.history())
             Timings   oooo
               ---     oooo

            sage: prec.del_elements()

            sage: print(prec.history())  # somewhat random
             Timings   oooo
            0.000005s  ~~oo
            0.000285s  oo

        .. SEEALSO::

            :meth:`history`, :meth:`history_enable`, :meth:`history_disable`
        """
    def history(self, compact: bool = True, separate_reduce: bool = False, timings: bool = True, output_type: str = 'asciiart'):
        """
        Show history.

        The history records creations and deletions of elements attached
        to this precision lattice, together with many timings.

        INPUT:

        - ``compact`` -- boolean (default: ``True``); if ``True``, all
          consecutive operations of the same type appear on a single row

        - ``separate_reduce`` -- boolean (default: ``False``); specify
          whether partial/full Hermite reduction should be displayed
          separately

        - ``timings`` -- boolean (default: ``True``); specify whether
          timings should be displayed

        - ``output_type`` -- only ``asciiart`` is implemented for now

        IMPORTANT NOTE:

        History is disabled by default.
        It should then be enabled (through a call to the method :meth:`history_enable`)
        before use.

        EXAMPLES::

            sage: R = ZpLC(2, label='history_en')
            sage: prec = R.precision()

        We first enable history::

            sage: prec.history_enable()

        At the beginning, the history is of course empty::

            sage: print(prec.history())
             Timings
               ---

        Now we start creating and deleting elements::

            sage: L = [ R.random_element() for _ in range(20) ]
            sage: for p in range(20):
            ....:    if is_prime(p): L[p] = None
            sage: prec.del_elements()

            sage: print(prec.history())  # somewhat random
             Timings
            0.001108s  oooooooooooooooooooo
            0.000009s  oo~~o~o~ooo~o~ooo~o~
            0.014250s  oooooooooooo

        The legend is the following:

        - the symbol ``o`` represents a tracked element,
        - the symbol ``~`` represents an element which is marked for deletion.

        On the history, we see:

        - 1st line: twenty new elements were created
          (this corresponds to the affectation of the list ``L``);
        - 2nd line: elements at prime positions were marked for deletion
          (this corresponds to the ``for`` loop);
        - 3rd line: the above elements are indeed deleted
          (this corresponds to the call of the method :meth:`del_elements`.

        Here are some variants::

            sage: print(prec.history(timings=False))
            oooooooooooooooooooo
            oo~~o~o~ooo~o~ooo~o~
            oooooooooooo

            sage: print(prec.history(separate_reduce=True))  # somewhat random
             Timings
            0.001063s  oooooooooooooooooooo
            0.000014s  oo~~o~o~ooo~o~ooo~o~
            0.000798s  oo~~o~o~ooo~ooooo
            0.000233s  oo~~o~o~ooo~orrrr
            0.000824s  oo~~o~o~oooooooo
            0.000375s  oo~~o~o~ooorrrrr
            0.001724s  oo~~o~ooooooooo
            0.001020s  oo~~o~orrrrrrrr
            0.001989s  oo~~oooooooooo
            0.001303s  oo~~orrrrrrrrr
            0.002352s  oo~oooooooooo
            0.001632s  oo~rrrrrrrrrr
            0.002265s  oooooooooooo
            0.001630s  oorrrrrrrrrr
               ---     oooooooooooo

        The symbol ``r`` represents a column of the precision matrix which is
        currently under partial Hermite reduction.

        Timings for automatic reduction do not appear because they are included
        in the timings for deletion.

        The symbol ``R`` is used to symbolize a column which is under full
        Hermite reduction. Note that full Hermite reduction are never performed
        automatically but needs to be called by hand::

            sage: prec.reduce()
            sage: print(prec.history(separate_reduce=True))  # somewhat random
             Timings
            0.001063s  oooooooooooooooooooo
            0.000014s  oo~~o~o~ooo~o~ooo~o~
            0.000798s  oo~~o~o~ooo~ooooo
            0.000233s  oo~~o~o~ooo~orrrr
            0.000824s  oo~~o~o~oooooooo
            0.000375s  oo~~o~o~ooorrrrr
            0.001724s  oo~~o~ooooooooo
            0.001020s  oo~~o~orrrrrrrr
            0.001989s  oo~~oooooooooo
            0.001303s  oo~~orrrrrrrrr
            0.002352s  oo~oooooooooo
            0.001632s  oo~rrrrrrrrrr
            0.002265s  oooooooooooo
            0.001630s  oorrrrrrrrrr
            0.001486s  RRRRRRRRRRRR
               ---     oooooooooooo

        Here is a more common example with matrices::

            sage: R = ZpLC(3)
            sage: prec = R.precision()
            sage: prec.history_enable()
            sage: M = random_matrix(R, 5)                                               # needs sage.geometry.polyhedron
            sage: d = M.determinant()                                                   # needs sage.geometry.polyhedron
            sage: print(prec.history())  # somewhat random
               ---
            0.004212s  oooooooooooooooooooooooooooooooooooo
            0.000003s  oooooooooooooooooooooooooooooooooo~~
            0.000010s  oooooooooooooooooooooooooooooooooo
            0.001560s  ooooooooooooooooooooooooooooooooooooooooo
            0.000004s  ooooooooooooooooooooooooooooo~oooo~oooo~o
            0.002168s  oooooooooooooooooooooooooooooooooooooo
            0.001787s  ooooooooooooooooooooooooooooooooooooooooo
            0.000004s  oooooooooooooooooooooooooooooooooooooo~~o
            0.000198s  ooooooooooooooooooooooooooooooooooooooo
            0.001152s  ooooooooooooooooooooooooooooooooooooooooo
            0.000005s  ooooooooooooooooooooooooooooooooo~oooo~~o
            0.000853s  oooooooooooooooooooooooooooooooooooooo
            0.000610s  ooooooooooooooooooooooooooooooooooooooo
             [...]
            0.003879s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000006s  oooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~~
            0.000036s  oooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.006737s  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000005s  oooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~~ooooo
            0.002637s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.007118s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000008s  oooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~o~~~~oooo
            0.003504s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.005371s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000006s  ooooooooooooooooooooooooooooooooooooooooooooooooooooo~~~o~~~ooo
            0.001858s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.003584s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000004s  oooooooooooooooooooooooooooooooooooooooooooooooooooooo~~o~~oo
            0.000801s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.001916s  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            0.000022s  ooooooooooooooooooooooooooooo~~~~~~~~~~~~~~~~~~~~~~oooo~o~o
            0.014705s  ooooooooooooooooooooooooooooooooooo
            0.001292s  ooooooooooooooooooooooooooooooooooooo

        We observe that deleted variables appear mostly on the right.
        This is the so-called principal of temporal locality.

        .. SEEALSO::

            :meth:`history_enable`, :meth:`history_disable`, :meth:`history_clear`
        """
    def timings(self, action=None):
        """
        Return cumulated timings (grouped by actions) since the last
        time history has been cleared.

        INPUT:

        - ``action`` -- ``None`` (default), ``'add'``, ``'mark'``, ``'del'``,
          ``'partial reduce'`` or ``'full reduce'``; if not ``None``, return the
          cumulated timing corresponding to this action; otherwise, return
          a dictionary

        Here are the meanings of the keywords above:

        - ``'add'``: time spent in adding new columns to the precision matrix
          (corresponding to the creation of new elements)
        - ``'mark'``: time spent in marking elements for deletion
        - ``'del'``: time spent in deleting columns of the precision matrix
          and re-echelonizing the matrix
        - ``'partial reduce'``: time spent in partial Hermite reduction
        - ``'full reduce'``: time spent in full Hermite reduction.

        EXAMPLES::

            sage: R = ZpLC(2, label='timings')
            sage: prec = R.precision()
            sage: prec.history_enable()
            sage: M = random_matrix(R, 5, 5)                                            # needs sage.geometry.polyhedron
            sage: N = M^10                                                              # needs sage.geometry.polyhedron
            sage: prec.timings()    # somewhat random
            {'add': 1.0530245304107666,
             'del': 0.24358701705932617,
             'mark': 0.0013289451599121094,
             'partial reduce': 0.21604204177856445
             'full reduce': 0}

        TESTS::

            sage: prec.history_clear()
            sage: prec.timings()
            {'add': 0, 'del': 0, 'full reduce': 0, 'mark': 0, 'partial reduce': 0}
        """

class PrecisionLattice(UniqueRepresentation, DifferentialPrecisionGeneric):
    """
    A class for handling precision lattices which are used to
    track precision in the ZpLC model.

    The precision lattice is stored as a triangular matrix whose
    rows are generators of the lattice.

    INPUT:

    - ``p`` -- a prime number

    - ``label`` -- string; the label of the parents to which the elements
      tracked by this lattice belong

    .. NOTE::

        You should not create instances of this class directly. The precision
        lattice is automatically initialized at the creation of the parent.

    EXAMPLES::

        sage: R = ZpLC(2, label='init')
        sage: R.precision()
        Precision lattice on 0 objects (label: init)
    """
    def __init__(self, p, label) -> None:
        """
        TESTS::

            sage: from sage.rings.padics.lattice_precision import PrecisionLattice
            sage: R = ZpLC(2)
            sage: isinstance(R.precision(), PrecisionLattice)
            True
        """
    def __reduce__(self) -> None:
        """
        TESTS::

            sage: R = ZpLC(2)
            sage: prec = R.precision()
            sage: dumps(prec)
            Traceback (most recent call last):
            ...
            NotImplementedError: pickling/unpickling precision modules is not implemented yet
        """
    def dimension(self):
        """
        Return the dimension of this lattice.

        EXAMPLES::

            sage: R = ZpLC(5, label='dimension')
            sage: prec = R.precision()
            sage: prec.dimension()
            0

            sage: x = R(1, 10)
            sage: prec.dimension()
            1
        """
    def reduce(self, index: int = 0, partial: bool = False) -> None:
        """
        Reduce the size of the entries above the diagonal of the precision matrix.

        INPUT:

        - ``index`` -- integer; the starting row for which the reduction
          is performed

        - ``partial`` -- boolean (default: ``False``); specifying whether a
          partial or a full Hermite reduction should be performed

        NOTE:

        The partial reduction has cost `O(m^2)` where `m` is the number of
        rows that need to be reduced (that is the difference between the
        total number of rows and ``index``).

        The full Hermite reduction has cost `O(m^3)`.

        .. NOTE::

            The software ensures that the precision lattice is always partially
            reduced.  Calling the function manually with the argument
            ``partial=True`` should then just do nothing.

        TESTS::

            sage: R = ZpLC(2)
            sage: x = R.random_element()
            sage: del x
            sage: R.precision().del_elements()   # indirect doctest
        """
    def del_elements(self, threshold=None) -> None:
        """
        Erase columns of the lattice precision matrix corresponding to
        elements which are marked for deletion and echelonize the matrix
        in order to keep it upper triangular.

        INPUT:

        - ``threshold`` -- integer or ``None`` (default: ``None``);
          a column whose distance to the right is greater than the
          threshold is not erased

        EXAMPLES::

            sage: R = ZpLC(2, label='delelts')
            sage: prec = R.precision()

            sage: x = R(1, 10)
            sage: prec
            Precision lattice on 1 object (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: del x
            sage: prec
            Precision lattice on 1 object (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: prec.del_elements()
            sage: prec
            Precision lattice on 0 objects (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            []
        """
    def precision_lattice(self, elements=None):
        """
        Return a matrix representing the precision lattice on a
        subset of elements.

        INPUT:

        - ``elements`` -- list of elements or ``None`` (default: ``None``)

        - ``echelon`` -- boolean (default: ``True``); whether the result
          should be in echelon form

        EXAMPLES::

            sage: R = ZpLC(2, label='preclattice')
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: u = x + y
            sage: v = x - y
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [         1024             0          1024          1024]
            [            0            32            32 1099511627744]
            [            0             0       2097152             0]
            [            0             0             0 1099511627776]
            sage: prec.precision_lattice([u, v])                                        # needs sage.geometry.polyhedron
            [  32 2016]
            [   0 2048]

        Here is another example with matrices::

            sage: M = matrix(R, 2, 2, [R(3, 5), R(7, 5), R(1, 5), R(11, 1)])            # needs sage.modules
            sage: N = M^10                                                              # needs sage.modules
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron sage.modules
            23 x 23 dense matrix over Integer Ring (use the '.str()' method to see the entries)

        The next syntax provides as easy way to select an interesting
        subset of variables (the selected subset consists of the four
        entries of the matrix ``N``)::

            sage: prec.precision_lattice(N)                                             # needs sage.modules
            [  2048    512  28160 230400]
            [     0   2048  14336 258048]
            [     0      0  65536  65536]
            [     0      0      0 262144]

        We can give a list of matrices as well::

            sage: prec.precision_lattice([M, N])                                        # needs sage.modules
            [       32         0         0         0 226115584  96788480  52174848  82804736]
            [        0        32         0         0  52174848 121765888  11829248  28516352]
            [        0         0        32         0  96788480  42762240 121765888 199614464]
            [        0         0         0         2   5175296  12475904   1782272   4045824]
            [        0         0         0         0 268435456         0         0         0]
            [        0         0         0         0         0 268435456         0         0]
            [        0         0         0         0         0         0 268435456         0]
            [        0         0         0         0         0         0         0 268435456]
        """

class PrecisionModule(UniqueRepresentation, DifferentialPrecisionGeneric):
    """
    A class for handling precision modules which are used to
    track precision in the ZpLF model.

    The precision module (which is not necessarily a lattice)
    is stored as a matrix whose rows are generators.
    """
    def __init__(self, p, label, prec) -> None:
        """
        Initialize this precision module.

        INPUT:

        - ``p`` -- a prime number

        - ``label`` -- string; the label of the parents to which belong
          the elements tracked by this precision module

        NOTE:

        The precision module is automatically initialized at the
        creation of the parent.

        TESTS::

            sage: R = ZpLF(2, label='init')
            sage: R.precision()
            Precision module on 0 objects (label: init)
        """
    def __reduce__(self) -> None:
        """
        TESTS::

            sage: R = ZpLF(2)
            sage: prec = R.precision()
            sage: dumps(prec)
            Traceback (most recent call last):
            ...
            NotImplementedError: pickling/unpickling precision modules is not implemented yet
        """
    def internal_prec(self):
        """
        Return the relative precision at which computations is handled
        internally.

        It is slightly greater than the actual precision and increases
        a bit (at a logarithmic rate) when new elements are created
        and/or computed.

        EXAMPLES::

            sage: R = ZpLF(5, prec=20, label='internal_prec')
            sage: prec = R.precision()

            sage: prec.internal_prec()
            25

            sage: L = [ R.random_element() for _ in range(50) ]
            sage: prec.internal_prec()
            28
        """
    def dimension(self):
        """
        Return the dimension of this precision module.

        EXAMPLES:

        In general, the dimension increases by 1 when a new
        element with a given precision is created::

            sage: R = ZpLF(2, label='dimension')
            sage: prec = R.precision()

            sage: prec.dimension()
            0
            sage: x = R.random_element(prec=10)
            sage: prec.dimension()
            1
            sage: y = R.random_element(prec=10)
            sage: prec.dimension()
            2

        However in general it does not increase while
        doing computations::

            sage: u = x + y
            sage: v = x^2 + 3*y + x*y + y^3
            sage: prec.dimension()
            2

        Of course, it may also decrease when a sufficient
        number of variables are collected::

            sage: del x, y, u
            sage: prec.del_elements()
            sage: prec.dimension()
            1

            sage: del v
            sage: prec.del_elements()
            sage: prec.dimension()
            0
        """
    def is_lattice(self):
        """
        Return ``True`` if this precision module is a lattice
        (i.e. has maximal dimension).

        EXAMPLES::

            sage: R = ZpLF(2, label='is_lattice')
            sage: prec = R.precision()

            sage: x = R(1, 10)
            sage: y = R(1, 5)
            sage: prec.is_lattice()
            True

            sage: u = x + y
            sage: prec.is_lattice()
            False

        .. SEEALSO::

            :meth:`dimension`
        """
    def del_elements(self, threshold=None) -> None:
        """
        Erase columns of the lattice precision matrix corresponding to
        elements which were collected by the garbage collector.
        Then reduce the matrix in order to keep it in echelon form.

        INPUT:

        - ``threshold`` -- integer or ``None`` (default: ``None``);
          a non-pivot column whose distance to the right is greater than
          the threshold is not erased but only marked for future deletion

        EXAMPLES::

            sage: R = ZpLF(2, label='delelts')
            sage: prec = R.precision()

            sage: x = R(1, 10)
            sage: prec
            Precision module on 1 object (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: del x
            sage: prec
            Precision module on 1 object (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024]

            sage: prec.del_elements()
            sage: prec
            Precision module on 0 objects (label: delelts)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            []
        """
    def precision_lattice(self, elements=None):
        """
        Return a matrix representing the precision lattice on a
        subset of elements.

        INPUT:

        - ``elements`` -- list of elements or ``None`` (default: ``None``)

        EXAMPLES::

            sage: R = ZpLF(2, label='preclattice')
            sage: prec = R.precision()
            sage: x = R(1, 10); y = R(1, 5)
            sage: prec.precision_lattice()                                              # needs sage.geometry.polyhedron
            [1024    0]
            [   0   32]

            sage: u = x + y
            sage: v = x - y
            sage: prec.precision_lattice([u, v])                                        # needs sage.geometry.polyhedron
            [  32 2016]
            [   0 2048]

        If the precision module does not project to a lattice,
        an error is raised. ::

            sage: prec.precision_lattice([x, y, u, v])                                  # needs sage.geometry.polyhedron
            Traceback (most recent call last):
            ...
            PrecisionError: the differential is not surjective

        Here is another example with matrices::

            sage: M = matrix(R, 2, 2, [R(3, 5), R(7, 5), R(1, 5), R(11, 1)])            # needs sage.modules
            sage: N = M^10                                                              # needs sage.modules

        The next syntax provides as easy way to select an interesting
        subset of variables (the selected subset consists of the four
        entries of the matrix ``N``)::

            sage: prec.precision_lattice(N)                                             # needs sage.geometry.polyhedron sage.modules
            [  2048    512  28160 230400]
            [     0   2048  14336 258048]
            [     0      0  65536  65536]
            [     0      0      0 262144]
        """

class pAdicLatticeElementWeakProxy:
    """
    The implementations of :class:`DifferentialPrecisionGeneric` hold
    weak references to :class:`pAdicLatticeElement`. They are stored in
    dictionaries, e.g., a dictionary that maps an element to the corresponding
    column in the precision lattice matrix.
    However, weak references as implemented by Python are tricky to use as
    dictionary keys. Their equality depends on the equality of the element they
    point to (as long as that element is alive) and then on the equality by
    ``id``. This means that statements such as: ``ref in D == ref in D`` could
    be false if the garbage collector kicks in between the two invocations.
    To prevent very subtle and hardly reproducible bugs, we wrap weak
    references in a proxy that gives every lattice element a unique increasing
    id and uses that id for comparisons.

    EXAMPLES:

    Proxy elements exist only internally and are not usually exposed to the user::

        sage: from sage.rings.padics.lattice_precision import pAdicLatticeElementWeakProxy
        sage: R = ZpLF(2, label='proxy')
        sage: p = R(2)
        sage: prec = R.precision()
        sage: proxy = prec._elements[0]
        sage: isinstance(proxy, pAdicLatticeElementWeakProxy)
        True
    """
    def __init__(self, element, callback=None) -> None:
        """
        TESTS::

            sage: from sage.rings.padics.lattice_precision import pAdicLatticeElementWeakProxy
            sage: R = ZpLF(2, label='proxy')
            sage: p = R(2)
            sage: pAdicLatticeElementWeakProxy(p) == pAdicLatticeElementWeakProxy(p)
            True
            sage: pAdicLatticeElementWeakProxy(p) is pAdicLatticeElementWeakProxy(p)
            False
        """
    def __hash__(self):
        """
        Return a hash value for this proxy.

        EXAMPLES::

            sage: from sage.rings.padics.lattice_precision import pAdicLatticeElementWeakProxy
            sage: R = ZpLF(2, label='proxy')
            sage: p = R(2)
            sage: hash(pAdicLatticeElementWeakProxy(p)) == hash(pAdicLatticeElementWeakProxy(p))
            True
        """
    def __eq__(self, other):
        """
        Return whether this proxy is undistinguishable from ``other``.

        EXAMPLES::

            sage: from sage.rings.padics.lattice_precision import pAdicLatticeElementWeakProxy
            sage: R = ZpLF(2, label='proxy')
            sage: p = R(2)
            sage: q = R(2)
            sage: pAdicLatticeElementWeakProxy(p) == pAdicLatticeElementWeakProxy(p)
            True
            sage: pAdicLatticeElementWeakProxy(q) == pAdicLatticeElementWeakProxy(p)
            False
        """
    def __call__(self):
        """
        Return the lattice element this proxy points to, or ``None`` if the
        target has already been finalized.

        EXAMPLES::

            sage: from sage.rings.padics.lattice_precision import pAdicLatticeElementWeakProxy
            sage: R = ZpLF(2, label='proxy')
            sage: p = R(2)
            sage: pAdicLatticeElementWeakProxy(p)()
            2 + O(2^21)
        """

def list_of_padics(elements):
    """
    Convert a list of `p`-adic composed elements (such as polynomials, matrices)
    to a list of weak references of their `p`-adic coefficients.

    This is a helper function for the method :meth:`precision_lattice`.

    TESTS::

        sage: from sage.rings.padics.lattice_precision import list_of_padics
        sage: R = ZpLC(2)
        sage: M = random_matrix(R, 2, 2)                                                # needs sage.geometry.polyhedron
        sage: list_of_padics(M)                                                         # needs sage.geometry.polyhedron
        [WeakProxy#...,
         WeakProxy#...,
         WeakProxy#...,
         WeakProxy#...]
    """
