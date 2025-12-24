r"""
Arbitrary precision real intervals using MPFI

AUTHORS:

- Carl Witty (2007-01-21): based on ``real_mpfr.pyx``; changed it to
  use mpfi rather than mpfr.

- William Stein (2007-01-24): modifications and clean up and docs, etc.

- Niles Johnson (2010-08): :issue:`3893`: ``random_element()`` should pass
  on ``*args`` and ``**kwds``.

- Travis Scrimshaw (2012-10-20): Fixing scientific notation output
  to fix :issue:`13634`.

- Travis Scrimshaw (2012-11-02): Added doctests for full coverage

This is a straightforward binding to the :ref:`MPFI library <spkg_mpfi>`;
it may be useful to refer to its documentation for more details.

An interval is represented as a pair of floating-point numbers `a`
and `b` (where `a \leq b`) and is printed as a standard floating-point
number with a question mark (for instance, ``3.1416?``). The question
mark indicates that the preceding digit may have an error of `\pm 1`.
These floating-point numbers are implemented using MPFR (the same
as the :class:`RealNumber` elements of
:class:`~sage.rings.real_mpfr.RealField_class`).

There is also an alternate method of printing, where the interval
prints as ``[a .. b]`` (for instance, ``[3.1415 .. 3.1416]``).

The interval represents the set `\{ x : a \leq x \leq b \}` (so if `a = b`,
then the interval represents that particular floating-point number). The
endpoints can include positive and negative infinity, with the
obvious meaning. It is also possible to have a ``NaN`` (Not-a-Number)
interval, which is represented by having either endpoint be ``NaN``.

PRINTING:

There are two styles for printing intervals: 'brackets' style and
'question' style (the default).

In question style, we print the "known correct" part of the number,
followed by a question mark. The question mark indicates that the
preceding digit is possibly wrong by `\pm 1`.

::

    sage: RIF(sqrt(2))                                                                  # needs sage.symbolic
    1.414213562373095?

However, if the interval is precise (its lower bound is equal to
its upper bound) and equal to a not-too-large integer, then we just
print that integer.

::

    sage: RIF(0)
    0
    sage: RIF(654321)
    654321

::

    sage: RIF(123, 125)
    124.?
    sage: RIF(123, 126)
    1.3?e2

As we see in the last example, question style can discard almost a
whole digit's worth of precision. We can reduce this by allowing
"error digits": an error following the question mark, that gives
the maximum error of the digit(s) before the question mark. If the
error is absent (which it always is in the default printing), then
it is taken to be 1.

::

    sage: RIF(123, 126).str(error_digits=1)
    '125.?2'
    sage: RIF(123, 127).str(error_digits=1)
    '125.?2'
    sage: v = RIF(-e, pi); v                                                            # needs sage.symbolic
    0.?e1
    sage: v.str(error_digits=1)                                                         # needs sage.symbolic
    '1.?4'
    sage: v.str(error_digits=5)                                                         # needs sage.symbolic
    '0.2117?29300'

Error digits also sometimes let us indicate that the interval is
actually equal to a single floating-point number::

    sage: RIF(54321/256)
    212.19140625000000?
    sage: RIF(54321/256).str(error_digits=1)
    '212.19140625000000?0'

In brackets style, intervals are printed with the left value
rounded down and the right rounded up, which is conservative, but
in some ways unsatisfying.

Consider a 3-bit interval containing exactly the floating-point
number 1.25. In round-to-nearest or round-down, this prints as 1.2;
in round-up, this prints as 1.3. The straightforward options, then,
are to print this interval as ``[1.2 .. 1.2]`` (which does not even
contain the true value, 1.25), or to print it as ``[1.2 .. 1.3]``
(which gives the impression that the upper and lower bounds are not
equal, even though they really are). Neither of these is very
satisfying, but we have chosen the latter.

::

    sage: R = RealIntervalField(3)
    sage: a = R(1.25)
    sage: a.str(style='brackets')
    '[1.2 .. 1.3]'
    sage: a == 5/4
    True
    sage: a == 2
    False

Some default printing options can be set by modifying module globals::

    sage: from sage.rings import real_mpfi
    sage: x = RIF(sqrt(2), sqrt(2)+1e-10); x
    1.4142135624?
    sage: real_mpfi.printing_error_digits = 2
    sage: x
    1.414213562424?51
    sage: real_mpfi.printing_style = 'brackets'
    sage: x
    [1.4142135623730949 .. 1.4142135624730952]
    sage: real_mpfi.printing_style = 'question'; real_mpfi.printing_error_digits = 0  # revert to default

The default value of using scientific notation can be configured at field construction instead::

    sage: RealIntervalField(53, sci_not=False)(0.5)
    0.50000000000000000?
    sage: RealIntervalField(53, sci_not=True)(0.5)
    5.0000000000000000?e-1

COMPARISONS:

Comparison operations (``==``, ``!=``, ``<``, ``<=``, ``>``, ``>=``)
return ``True`` if every value in the first interval has the given relation
to every value in the second interval.

This convention for comparison operators has good and bad points.  The
good:

- Expected transitivity properties hold (if ``a > b`` and ``b == c``, then
  ``a > c``; etc.)

- ``a == 0`` is true if the interval contains only the floating-point number
  0; similarly for ``a == 1``

- ``a > 0`` means something useful (that every value in the interval is
  greater than 0)

The bad:

- Trichotomy fails to hold: there are values ``(a,b)`` such that none of
  ``a < b``, ``a == b``, or ``a > b`` are true

- There are values ``a`` and ``b`` such that ``a <= b`` but neither ``a < b``
  nor ``a == b`` hold.

- There are values ``a`` and ``b`` such that neither ``a != b``
  nor ``a == b`` hold.

.. NOTE::

    Intervals ``a`` and ``b`` overlap iff ``not(a != b)``.

.. WARNING::

    The ``cmp(a, b)`` function should not be used to compare real
    intervals. Note that ``cmp`` will disappear in Python3.

EXAMPLES::

    sage: 0 < RIF(1, 2)
    True
    sage: 0 == RIF(0)
    True
    sage: not(0 == RIF(0, 1))
    True
    sage: not(0 != RIF(0, 1))
    True
    sage: 0 <= RIF(0, 1)
    True
    sage: not(0 < RIF(0, 1))
    True

Comparison with infinity is defined through coercion to the infinity
ring where semi-infinite intervals are sent to their central value
(plus or minus infinity); this implements the above convention for
inequalities::

    sage: InfinityRing.has_coerce_map_from(RIF)
    True
    sage: -oo < RIF(-1,1) < oo
    True
    sage: -oo < RIF(0,oo) <= oo
    True
    sage: -oo <= RIF(-oo,-1) < oo
    True

Comparison by equality shows what the semi-infinite intervals actually
coerce to::

    sage: RIF(1,oo) == oo
    True
    sage: RIF(-oo,-1) == -oo
    True

For lack of a better value in the infinity ring, the doubly infinite
interval coerces to plus infinity::

    sage: RIF(-oo,oo) == oo
    True

If you want to compare two intervals lexicographically, you can use the
method ``lexico_cmp``. However, the behavior of this method is not
specified if given a non-interval and an interval::

    sage: RIF(0).lexico_cmp(RIF(0, 1))
    -1
    sage: RIF(0, 1).lexico_cmp(RIF(0))
    1
    sage: RIF(0, 1).lexico_cmp(RIF(1))
    -1
    sage: RIF(0, 1).lexico_cmp(RIF(0, 1))
    0

.. WARNING::

    Mixing symbolic expressions with intervals (in particular, converting
    constant symbolic expressions to intervals), can lead to incorrect
    results::

        sage: ref = RealIntervalField(100)(ComplexBallField(100).one().airy_ai().real())
        sage: ref
        0.135292416312881415524147423515?
        sage: val = RIF(airy_ai(1)); val # known bug
        0.13529241631288142?
        sage: val.overlaps(ref)          # known bug
        False

TESTS::

    sage: import numpy                                                                  # needs numpy
    sage: if int(numpy.version.short_version[0]) > 1:                                   # needs numpy
    ....:     _ = numpy.set_printoptions(legacy="1.25")                                     # needs numpy
    sage: RIF(2) == numpy.int8('2')                                                     # needs numpy
    True
    sage: numpy.int8('2') == RIF(2)                                                     # needs numpy
    True
    sage: RIF(0,1) < float('2')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for <: ...
"""
import _cython_3_2_1
import sage as sage
import sage.rings.abc
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.superseded import deprecation as deprecation
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

def RealInterval(s: str | object, upper=None, base: int=10, pad: int = 0, min_prec=53):
    r"""
    Return the real number defined by the string s as an element of
    ``RealIntervalField(prec=n)``, where ``n`` potentially has
    slightly more (controlled by pad) bits than given by ``s``.

    INPUT:

    - ``s`` -- string that defines a real number (or
      something whose string representation defines a number)

    - ``upper`` -- (default: ``None``) upper endpoint of
      interval if given, in which case ``s`` is the lower endpoint

    - ``base`` -- integer between 2 and 36

    - ``pad`` -- integer (default: 0)

    - ``min_prec`` -- number will have at least this many
      bits of precision, no matter what

    EXAMPLES::

        sage: RealInterval('2.3')
        2.300000000000000?
        sage: RealInterval(10)
        10
        sage: RealInterval('1.0000000000000000000000000000000000')
        1
        sage: RealInterval('1.2345678901234567890123456789012345')
        1.23456789012345678901234567890123450?
        sage: RealInterval(29308290382930840239842390482, 3^20).str(style='brackets')
        '[3.48678440100000000000000000000e9 .. 2.93082903829308402398423904820e28]'

    TESTS:

    Make sure we've rounded up ``log(10,2)`` enough to guarantee
    sufficient precision (:issue:`10164`).  This is a little tricky
    because at the time of writing, we don't support intervals long
    enough to trip the error.  However, at least we can make sure
    that we either do it correctly or fail noisily::

        sage: ks = 5*10**5, 10**6
        sage: for k in ks:
        ....:    try:
        ....:        z = RealInterval("1." + "1"*k)
        ....:        assert len(str(z))-4 >= k
        ....:    except TypeError:
        ....:        pass
    """
def RealIntervalField(prec=53, sci_not=False) -> RealIntervalField_class:
    r"""
    Construct a :class:`RealIntervalField_class`, with caching.

    INPUT:

    - ``prec`` -- integer (default: 53); precision.
      The number of bits used to represent the mantissa of a
      floating-point number. The precision can be any integer between
      :func:`mpfr_prec_min()` and :func:`mpfr_prec_max()`. In the current
      implementation, :func:`mpfr_prec_min()` is equal to 2.

    - ``sci_not`` -- boolean (default: ``False``); whether or not to display using
      scientific notation

    EXAMPLES::

        sage: RealIntervalField()
        Real Interval Field with 53 bits of precision
        sage: RealIntervalField(200, sci_not=True)
        Real Interval Field with 200 bits of precision
        sage: RealIntervalField(53) is RIF
        True
        sage: RealIntervalField(200) is RIF
        False
        sage: RealIntervalField(200) is RealIntervalField(200)
        True

    See the documentation for :class:`RealIntervalField_class
    <sage.rings.real_mpfi.RealIntervalField_class>` for many more
    examples.
    """
def is_RealIntervalField(x):
    """
    Check if ``x`` is a :class:`RealIntervalField_class`.

    EXAMPLES::

        sage: sage.rings.real_mpfi.is_RealIntervalField(RIF)
        doctest:warning...
        DeprecationWarning: The function is_RealIntervalField is deprecated;
        use 'isinstance(..., RealIntervalField_class)' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: sage.rings.real_mpfi.is_RealIntervalField(RealIntervalField(200))
        True
    """
def is_RealIntervalFieldElement(x):
    """
    Check if ``x`` is a :class:`RealIntervalFieldElement`.

    EXAMPLES::

        sage: sage.rings.real_mpfi.is_RealIntervalFieldElement(RIF(2.2))
        doctest:warning...
        DeprecationWarning: The function is_RealIntervalFieldElement is deprecated;
        use 'isinstance(..., RealIntervalFieldElement)' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: sage.rings.real_mpfi.is_RealIntervalFieldElement(RealIntervalField(200)(2.2))
        True
    """
printing_error_digits: int
printing_style: str

class RealIntervalFieldElement(sage.structure.element.RingElement):
    """RealIntervalFieldElement(parent, x, int base=10)

    File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1191)

    A real number interval."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, intbase=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1222)

                Initialize a real interval element. Should be called by first
                creating a :class:`RealIntervalField`, as illustrated in the
                examples.

                INPUT:

                - ``x`` -- a number, string, or 2-tuple

                - ``base`` -- integer (default: 10); only used if ``x`` is a string

                EXAMPLES::

                    sage: R = RealIntervalField()
                    sage: R('1.2456')
                    1.245600000000000?
                    sage: R = RealIntervalField(3)
                    sage: R('1.2456').str(style='brackets')
                    '[1.0 .. 1.3]'

                ::

                    sage: RIF = RealIntervalField(53)
                    sage: RIF(RR.pi())
                    3.1415926535897932?
                    sage: RIF(RDF.pi())
                    3.1415926535897932?
                    sage: RIF(math.pi)
                    3.1415926535897932?
                    sage: RIF.pi()
                    3.141592653589794?

                Rounding::

                    sage: w = RealIntervalField(3)(5/2)
                    sage: RealIntervalField(2)(w).str(2, style='brackets')
                    '[10. .. 11.]'

                TESTS::

                    sage: a = RealIntervalField(428)(factorial(100)/exp(2)); a
                    1.26303298005073195998439505058085204028142920134742241494671502106333548593576383141666758300089860337889002385197008191910406895?e157
                    sage: a.diameter()
                    4.7046373946079775711568954992429894854882556641460240333441655212438503516287848720594584761250430179569094634219773739322602945e-129

                Type: ``RealIntervalField?`` for many more examples.
        """
    @overload
    def absolute_diameter(self) -> Any:
        """RealIntervalFieldElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2389)

        The diameter of this interval (for `[a .. b]`, this is `b-a`), rounded
        upward, as a :class:`RealNumber`.

        EXAMPLES::

            sage: RIF(1, pi).absolute_diameter()                                        # needs sage.symbolic
            2.14159265358979"""
    @overload
    def absolute_diameter(self) -> Any:
        """RealIntervalFieldElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2389)

        The diameter of this interval (for `[a .. b]`, this is `b-a`), rounded
        upward, as a :class:`RealNumber`.

        EXAMPLES::

            sage: RIF(1, pi).absolute_diameter()                                        # needs sage.symbolic
            2.14159265358979"""
    @overload
    def alea(self) -> Any:
        """RealIntervalFieldElement.alea(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2595)

        Return a floating-point number picked at random from the interval.

        EXAMPLES::

            sage: RIF(1, 2).alea() # random
            1.34696133696137"""
    @overload
    def alea(self) -> Any:
        """RealIntervalFieldElement.alea(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2595)

        Return a floating-point number picked at random from the interval.

        EXAMPLES::

            sage: RIF(1, 2).alea() # random
            1.34696133696137"""
    def algdep(self, *args, **kwargs):
        '''RealIntervalFieldElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4999)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by ``self``.

        .. NOTE::

            The returned polynomial need not be irreducible, and indeed usually
            won\'t be if ``self`` is a good approximation to an algebraic number
            of degree less than `n`.

        Pari needs to know the number of "known good bits" in the number;
        we automatically get that from the interval width.

        ALGORITHM:

        This uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: r = sqrt(RIF(2)); r
            1.414213562373095?
            sage: r.algebraic_dependency(5)
            x^2 - 2

        If we compute a wrong, but precise, interval, we get a wrong
        answer::

            sage: r = sqrt(RealIntervalField(200)(2)) + (1/2)^40; r
            1.414213562374004543503461652447613117632171875376948073176680?
            sage: r.algebraic_dependency(5)
            7266488*x^5 + 22441629*x^4 - 90470501*x^3 + 23297703*x^2 + 45778664*x + 13681026

        But if we compute an interval that includes the number we mean,
        we\'re much more likely to get the right answer, even if the
        interval is very imprecise::

            sage: r = r.union(sqrt(2.0))
            sage: r.algebraic_dependency(5)
            x^2 - 2

        Even on this extremely imprecise interval we get an answer which is
        technically correct::

            sage: RIF(-1, 1).algebraic_dependency(5)
            x'''
    def algebraic_dependency(self, n) -> Any:
        '''RealIntervalFieldElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4999)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by ``self``.

        .. NOTE::

            The returned polynomial need not be irreducible, and indeed usually
            won\'t be if ``self`` is a good approximation to an algebraic number
            of degree less than `n`.

        Pari needs to know the number of "known good bits" in the number;
        we automatically get that from the interval width.

        ALGORITHM:

        This uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: r = sqrt(RIF(2)); r
            1.414213562373095?
            sage: r.algebraic_dependency(5)
            x^2 - 2

        If we compute a wrong, but precise, interval, we get a wrong
        answer::

            sage: r = sqrt(RealIntervalField(200)(2)) + (1/2)^40; r
            1.414213562374004543503461652447613117632171875376948073176680?
            sage: r.algebraic_dependency(5)
            7266488*x^5 + 22441629*x^4 - 90470501*x^3 + 23297703*x^2 + 45778664*x + 13681026

        But if we compute an interval that includes the number we mean,
        we\'re much more likely to get the right answer, even if the
        interval is very imprecise::

            sage: r = r.union(sqrt(2.0))
            sage: r.algebraic_dependency(5)
            x^2 - 2

        Even on this extremely imprecise interval we get an answer which is
        technically correct::

            sage: RIF(-1, 1).algebraic_dependency(5)
            x'''
    @overload
    def arccos(self) -> Any:
        """RealIntervalFieldElement.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4703)

        Return the inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/3; q
            1.047197551196598?
            sage: i = q.cos(); i
            0.500000000000000?
            sage: q2 = i.arccos(); q2
            1.047197551196598?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arccos(self) -> Any:
        """RealIntervalFieldElement.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4703)

        Return the inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/3; q
            1.047197551196598?
            sage: i = q.cos(); i
            0.500000000000000?
            sage: q2 = i.arccos(); q2
            1.047197551196598?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arccosh(self) -> Any:
        """RealIntervalFieldElement.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4838)

        Return the hyperbolic inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/2
            sage: i = q.arccosh() ; i
            1.023227478547551?"""
    @overload
    def arccosh(self) -> Any:
        """RealIntervalFieldElement.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4838)

        Return the hyperbolic inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/2
            sage: i = q.arccosh() ; i
            1.023227478547551?"""
    @overload
    def arccoth(self) -> Any:
        """RealIntervalFieldElement.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

        Return the inverse hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccoth()
            0.549306144334054845697622618462?
            sage: (2.0).arccoth()
            0.549306144334055"""
    @overload
    def arccoth(self) -> Any:
        """RealIntervalFieldElement.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

        Return the inverse hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccoth()
            0.549306144334054845697622618462?
            sage: (2.0).arccoth()
            0.549306144334055"""
    @overload
    def arccoth(self) -> Any:
        """RealIntervalFieldElement.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

        Return the inverse hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccoth()
            0.549306144334054845697622618462?
            sage: (2.0).arccoth()
            0.549306144334055"""
    @overload
    def arccsch(self) -> Any:
        """RealIntervalFieldElement.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

        Return the inverse hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccsch()
            0.481211825059603447497758913425?
            sage: (2.0).arccsch()
            0.481211825059603"""
    @overload
    def arccsch(self) -> Any:
        """RealIntervalFieldElement.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

        Return the inverse hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccsch()
            0.481211825059603447497758913425?
            sage: (2.0).arccsch()
            0.481211825059603"""
    @overload
    def arccsch(self) -> Any:
        """RealIntervalFieldElement.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

        Return the inverse hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).arccsch()
            0.481211825059603447497758913425?
            sage: (2.0).arccsch()
            0.481211825059603"""
    @overload
    def arcsech(self) -> Any:
        """RealIntervalFieldElement.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

        Return the inverse hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(0.5).arcsech()
            1.316957896924816708625046347308?
            sage: (0.5).arcsech()
            1.31695789692482"""
    @overload
    def arcsech(self) -> Any:
        """RealIntervalFieldElement.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

        Return the inverse hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(0.5).arcsech()
            1.316957896924816708625046347308?
            sage: (0.5).arcsech()
            1.31695789692482"""
    @overload
    def arcsech(self) -> Any:
        """RealIntervalFieldElement.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

        Return the inverse hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(0.5).arcsech()
            1.316957896924816708625046347308?
            sage: (0.5).arcsech()
            1.31695789692482"""
    @overload
    def arcsin(self) -> Any:
        """RealIntervalFieldElement.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4732)

        Return the inverse sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/5; q
            0.6283185307179587?
            sage: i = q.sin(); i
            0.587785252292474?
            sage: q2 = i.arcsin(); q2
            0.628318530717959?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arcsin(self) -> Any:
        """RealIntervalFieldElement.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4732)

        Return the inverse sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/5; q
            0.6283185307179587?
            sage: i = q.sin(); i
            0.587785252292474?
            sage: q2 = i.arcsin(); q2
            0.628318530717959?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arcsinh(self) -> Any:
        """RealIntervalFieldElement.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4854)

        Return the hyperbolic inverse sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/7
            sage: i = q.sinh() ; i
            0.464017630492991?
            sage: i.arcsinh() - q
            0.?e-15"""
    @overload
    def arcsinh(self) -> Any:
        """RealIntervalFieldElement.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4854)

        Return the hyperbolic inverse sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/7
            sage: i = q.sinh() ; i
            0.464017630492991?
            sage: i.arcsinh() - q
            0.?e-15"""
    @overload
    def arctan(self) -> Any:
        """RealIntervalFieldElement.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4761)

        Return the inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/5; q
            0.6283185307179587?
            sage: i = q.tan(); i
            0.726542528005361?
            sage: q2 = i.arctan(); q2
            0.628318530717959?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arctan(self) -> Any:
        """RealIntervalFieldElement.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4761)

        Return the inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/5; q
            0.6283185307179587?
            sage: i = q.tan(); i
            0.726542528005361?
            sage: q2 = i.arctan(); q2
            0.628318530717959?
            sage: q == q2
            False
            sage: q != q2
            False
            sage: q2.lower() == q.lower()
            False
            sage: q - q2
            0.?e-15
            sage: q in q2
            True"""
    @overload
    def arctanh(self) -> Any:
        """RealIntervalFieldElement.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4872)

        Return the hyperbolic inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/7
            sage: i = q.tanh() ; i
            0.420911241048535?
            sage: i.arctanh() - q
            0.?e-15"""
    @overload
    def arctanh(self) -> Any:
        """RealIntervalFieldElement.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4872)

        Return the hyperbolic inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/7
            sage: i = q.tanh() ; i
            0.420911241048535?
            sage: i.arctanh() - q
            0.?e-15"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def argument(self) -> Any:
        """RealIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

        The argument of this interval, if it is well-defined, in the
        complex sense. Otherwise raises a :exc:`ValueError`.

        OUTPUT:

        - an element of the parent of this interval (0 or pi)

        EXAMPLES::

            sage: RIF(1).argument()
            0
            sage: RIF(-1).argument()
            3.141592653589794?
            sage: RIF(0,1).argument()
            0
            sage: RIF(-1,0).argument()
            3.141592653589794?
            sage: RIF(0).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of an exact zero
            sage: RIF(-1,1).argument()
            Traceback (most recent call last):
            ...
            ValueError: Can't take the argument of interval strictly containing zero"""
    @overload
    def bisection(self) -> Any:
        """RealIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

        Return the bisection of ``self`` into two intervals of half the size
        whose union is ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: a, b = RIF(1,2).bisection()
            sage: a.lower(), a.upper()
            (1.00000000000000, 1.50000000000000)
            sage: b.lower(), b.upper()
            (1.50000000000000, 2.00000000000000)

            sage: # needs sage.symbolic
            sage: I = RIF(e, pi)
            sage: a, b = I.bisection()
            sage: a.intersection(b) == RIF(I.center())
            True
            sage: a.union(b).endpoints() == I.endpoints()
            True"""
    @overload
    def bisection(self) -> Any:
        """RealIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

        Return the bisection of ``self`` into two intervals of half the size
        whose union is ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: a, b = RIF(1,2).bisection()
            sage: a.lower(), a.upper()
            (1.00000000000000, 1.50000000000000)
            sage: b.lower(), b.upper()
            (1.50000000000000, 2.00000000000000)

            sage: # needs sage.symbolic
            sage: I = RIF(e, pi)
            sage: a, b = I.bisection()
            sage: a.intersection(b) == RIF(I.center())
            True
            sage: a.union(b).endpoints() == I.endpoints()
            True"""
    @overload
    def bisection(self) -> Any:
        """RealIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

        Return the bisection of ``self`` into two intervals of half the size
        whose union is ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: a, b = RIF(1,2).bisection()
            sage: a.lower(), a.upper()
            (1.00000000000000, 1.50000000000000)
            sage: b.lower(), b.upper()
            (1.50000000000000, 2.00000000000000)

            sage: # needs sage.symbolic
            sage: I = RIF(e, pi)
            sage: a, b = I.bisection()
            sage: a.intersection(b) == RIF(I.center())
            True
            sage: a.union(b).endpoints() == I.endpoints()
            True"""
    @overload
    def ceil(self) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def ceil(self) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def ceil(self) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def ceil(self) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def ceil(self) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def ceil(self, a) -> Any:
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    def ceiling(self, *args, **kwargs):
        """RealIntervalFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

        Return the ceiling of this interval as an interval.

        The ceiling of a real number `x` is the smallest integer larger than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_ceil` -- return the ceil as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards minus infinity
            - :meth:`trunc` -- truncation towards zero
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: (2.99).ceil()
            3
            sage: (2.00).ceil()
            2
            sage: (2.01).ceil()
            3
            sage: R = RealIntervalField(30)
            sage: a = R(-9.5, -11.3); a.str(style='brackets')
            '[-11.300000012 .. -9.5000000000]'
            sage: a.floor().str(style='brackets')
            '[-12.000000000 .. -10.000000000]'
            sage: a.ceil()
            -10.?
            sage: ceil(a).str(style='brackets')
            '[-11.000000000 .. -9.0000000000]'"""
    @overload
    def center(self) -> Any:
        """RealIntervalFieldElement.center(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2553)

        Compute the center of the interval `[a .. b]` which is `(a+b) / 2`.

        EXAMPLES::

            sage: RIF(1, 2).center()
            1.50000000000000"""
    @overload
    def center(self) -> Any:
        """RealIntervalFieldElement.center(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2553)

        Compute the center of the interval `[a .. b]` which is `(a+b) / 2`.

        EXAMPLES::

            sage: RIF(1, 2).center()
            1.50000000000000"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: RIF(0).contains_zero()
            True
            sage: RIF(1, 2).contains_zero()
            False
            sage: RIF(-1, 1).contains_zero()
            True
            sage: RIF(-1, 0).contains_zero()
            True"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: RIF(0).contains_zero()
            True
            sage: RIF(1, 2).contains_zero()
            False
            sage: RIF(-1, 1).contains_zero()
            True
            sage: RIF(-1, 0).contains_zero()
            True"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: RIF(0).contains_zero()
            True
            sage: RIF(1, 2).contains_zero()
            False
            sage: RIF(-1, 1).contains_zero()
            True
            sage: RIF(-1, 0).contains_zero()
            True"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: RIF(0).contains_zero()
            True
            sage: RIF(1, 2).contains_zero()
            False
            sage: RIF(-1, 1).contains_zero()
            True
            sage: RIF(-1, 0).contains_zero()
            True"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: RIF(0).contains_zero()
            True
            sage: RIF(1, 2).contains_zero()
            False
            sage: RIF(-1, 1).contains_zero()
            True
            sage: RIF(-1, 0).contains_zero()
            True"""
    @overload
    def cos(self) -> Any:
        """RealIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = RIF(pi)/2
            sage: t.cos()
            0.?e-15
            sage: t.cos().str(style='brackets')
            '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
            sage: t.cos().cos()
            0.9999999999999999?

        TESTS:

        This looped forever with an earlier version of MPFI, but now
        it works::

            sage: RIF(-1, 1).cos().str(style='brackets')
            '[0.54030230586813965 .. 1.0000000000000000]'"""
    @overload
    def cos(self) -> Any:
        """RealIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = RIF(pi)/2
            sage: t.cos()
            0.?e-15
            sage: t.cos().str(style='brackets')
            '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
            sage: t.cos().cos()
            0.9999999999999999?

        TESTS:

        This looped forever with an earlier version of MPFI, but now
        it works::

            sage: RIF(-1, 1).cos().str(style='brackets')
            '[0.54030230586813965 .. 1.0000000000000000]'"""
    @overload
    def cos(self) -> Any:
        """RealIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = RIF(pi)/2
            sage: t.cos()
            0.?e-15
            sage: t.cos().str(style='brackets')
            '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
            sage: t.cos().cos()
            0.9999999999999999?

        TESTS:

        This looped forever with an earlier version of MPFI, but now
        it works::

            sage: RIF(-1, 1).cos().str(style='brackets')
            '[0.54030230586813965 .. 1.0000000000000000]'"""
    @overload
    def cos(self) -> Any:
        """RealIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = RIF(pi)/2
            sage: t.cos()
            0.?e-15
            sage: t.cos().str(style='brackets')
            '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
            sage: t.cos().cos()
            0.9999999999999999?

        TESTS:

        This looped forever with an earlier version of MPFI, but now
        it works::

            sage: RIF(-1, 1).cos().str(style='brackets')
            '[0.54030230586813965 .. 1.0000000000000000]'"""
    @overload
    def cos(self) -> Any:
        """RealIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: t = RIF(pi)/2
            sage: t.cos()
            0.?e-15
            sage: t.cos().str(style='brackets')
            '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
            sage: t.cos().cos()
            0.9999999999999999?

        TESTS:

        This looped forever with an earlier version of MPFI, but now
        it works::

            sage: RIF(-1, 1).cos().str(style='brackets')
            '[0.54030230586813965 .. 1.0000000000000000]'"""
    @overload
    def cosh(self) -> Any:
        """RealIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4790)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/12
            sage: q.cosh()
            1.034465640095511?"""
    @overload
    def cosh(self) -> Any:
        """RealIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4790)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/12
            sage: q.cosh()
            1.034465640095511?"""
    @overload
    def cot(self) -> Any:
        """RealIntervalFieldElement.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4916)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).cot()
            -0.457657554360285763750277410432?"""
    @overload
    def cot(self) -> Any:
        """RealIntervalFieldElement.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4916)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).cot()
            -0.457657554360285763750277410432?"""
    @overload
    def coth(self) -> Any:
        """RealIntervalFieldElement.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4949)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).coth()
            1.03731472072754809587780976477?"""
    @overload
    def coth(self) -> Any:
        """RealIntervalFieldElement.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4949)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).coth()
            1.03731472072754809587780976477?"""
    @overload
    def csc(self) -> Any:
        """RealIntervalFieldElement.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4905)

        Return the cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).csc()
            1.099750170294616466756697397026?"""
    @overload
    def csc(self) -> Any:
        """RealIntervalFieldElement.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4905)

        Return the cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).csc()
            1.099750170294616466756697397026?"""
    @overload
    def csch(self) -> Any:
        """RealIntervalFieldElement.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4938)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).csch()
            0.275720564771783207758351482163?"""
    @overload
    def csch(self) -> Any:
        """RealIntervalFieldElement.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4938)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).csch()
            0.275720564771783207758351482163?"""
    @overload
    def diameter(self) -> Any:
        """RealIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

        If 0 is in ``self``, then return :meth:`absolute_diameter()`,
        otherwise return :meth:`relative_diameter()`.

        EXAMPLES::

            sage: RIF(1, 2).diameter()
            0.666666666666667
            sage: RIF(1, 2).absolute_diameter()
            1.00000000000000
            sage: RIF(1, 2).relative_diameter()
            0.666666666666667

            sage: # needs sage.symbolic
            sage: RIF(pi).diameter()
            1.41357985842823e-16
            sage: RIF(pi).absolute_diameter()
            4.44089209850063e-16
            sage: RIF(pi).relative_diameter()
            1.41357985842823e-16
            sage: (RIF(pi) - RIF(3, 22/7)).diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
            2.03604377705518"""
    @overload
    def diameter(self) -> Any:
        """RealIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

        If 0 is in ``self``, then return :meth:`absolute_diameter()`,
        otherwise return :meth:`relative_diameter()`.

        EXAMPLES::

            sage: RIF(1, 2).diameter()
            0.666666666666667
            sage: RIF(1, 2).absolute_diameter()
            1.00000000000000
            sage: RIF(1, 2).relative_diameter()
            0.666666666666667

            sage: # needs sage.symbolic
            sage: RIF(pi).diameter()
            1.41357985842823e-16
            sage: RIF(pi).absolute_diameter()
            4.44089209850063e-16
            sage: RIF(pi).relative_diameter()
            1.41357985842823e-16
            sage: (RIF(pi) - RIF(3, 22/7)).diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
            2.03604377705518"""
    @overload
    def diameter(self) -> Any:
        """RealIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

        If 0 is in ``self``, then return :meth:`absolute_diameter()`,
        otherwise return :meth:`relative_diameter()`.

        EXAMPLES::

            sage: RIF(1, 2).diameter()
            0.666666666666667
            sage: RIF(1, 2).absolute_diameter()
            1.00000000000000
            sage: RIF(1, 2).relative_diameter()
            0.666666666666667

            sage: # needs sage.symbolic
            sage: RIF(pi).diameter()
            1.41357985842823e-16
            sage: RIF(pi).absolute_diameter()
            4.44089209850063e-16
            sage: RIF(pi).relative_diameter()
            1.41357985842823e-16
            sage: (RIF(pi) - RIF(3, 22/7)).diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
            2.03604377705518"""
    @overload
    def diameter(self) -> Any:
        """RealIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

        If 0 is in ``self``, then return :meth:`absolute_diameter()`,
        otherwise return :meth:`relative_diameter()`.

        EXAMPLES::

            sage: RIF(1, 2).diameter()
            0.666666666666667
            sage: RIF(1, 2).absolute_diameter()
            1.00000000000000
            sage: RIF(1, 2).relative_diameter()
            0.666666666666667

            sage: # needs sage.symbolic
            sage: RIF(pi).diameter()
            1.41357985842823e-16
            sage: RIF(pi).absolute_diameter()
            4.44089209850063e-16
            sage: RIF(pi).relative_diameter()
            1.41357985842823e-16
            sage: (RIF(pi) - RIF(3, 22/7)).diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
            0.142857142857144
            sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
            2.03604377705518"""
    @overload
    def edges(self) -> Any:
        """RealIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

        Return the lower and upper endpoints of this interval as
        intervals.

        OUTPUT: a 2-tuple of real intervals
        (lower endpoint, upper endpoint)
        each containing just one point.

        .. SEEALSO::

            :meth:`endpoints` which returns the endpoints as real
            numbers instead of intervals.

        EXAMPLES::

            sage: RIF(1,2).edges()
            (1, 2)
            sage: RIF(pi).edges()                                                       # needs sage.symbolic
            (3.1415926535897932?, 3.1415926535897936?)"""
    @overload
    def edges(self) -> Any:
        """RealIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

        Return the lower and upper endpoints of this interval as
        intervals.

        OUTPUT: a 2-tuple of real intervals
        (lower endpoint, upper endpoint)
        each containing just one point.

        .. SEEALSO::

            :meth:`endpoints` which returns the endpoints as real
            numbers instead of intervals.

        EXAMPLES::

            sage: RIF(1,2).edges()
            (1, 2)
            sage: RIF(pi).edges()                                                       # needs sage.symbolic
            (3.1415926535897932?, 3.1415926535897936?)"""
    @overload
    def edges(self) -> Any:
        """RealIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

        Return the lower and upper endpoints of this interval as
        intervals.

        OUTPUT: a 2-tuple of real intervals
        (lower endpoint, upper endpoint)
        each containing just one point.

        .. SEEALSO::

            :meth:`endpoints` which returns the endpoints as real
            numbers instead of intervals.

        EXAMPLES::

            sage: RIF(1,2).edges()
            (1, 2)
            sage: RIF(pi).edges()                                                       # needs sage.symbolic
            (3.1415926535897932?, 3.1415926535897936?)"""
    @overload
    def endpoints(self, rnd=...) -> Any:
        """RealIntervalFieldElement.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

        Return the lower and upper endpoints of this interval.

        OUTPUT: a 2-tuple of real numbers
        (lower endpoint, upper endpoint)

        .. SEEALSO::

            :meth:`edges` which returns the endpoints as exact
            intervals instead of real numbers.

        EXAMPLES::

            sage: RIF(1,2).endpoints()
            (1.00000000000000, 2.00000000000000)
            sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
            (3.14159265358979, 3.14159265358980)
            sage: a = CIF(RIF(1,2), RIF(3,4))
            sage: a.real().endpoints()
            (1.00000000000000, 2.00000000000000)

        As with ``lower()`` and ``upper()``, a rounding mode is accepted::

            sage: RIF(1,2).endpoints('RNDD')[0].parent()
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalFieldElement.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

        Return the lower and upper endpoints of this interval.

        OUTPUT: a 2-tuple of real numbers
        (lower endpoint, upper endpoint)

        .. SEEALSO::

            :meth:`edges` which returns the endpoints as exact
            intervals instead of real numbers.

        EXAMPLES::

            sage: RIF(1,2).endpoints()
            (1.00000000000000, 2.00000000000000)
            sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
            (3.14159265358979, 3.14159265358980)
            sage: a = CIF(RIF(1,2), RIF(3,4))
            sage: a.real().endpoints()
            (1.00000000000000, 2.00000000000000)

        As with ``lower()`` and ``upper()``, a rounding mode is accepted::

            sage: RIF(1,2).endpoints('RNDD')[0].parent()
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalFieldElement.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

        Return the lower and upper endpoints of this interval.

        OUTPUT: a 2-tuple of real numbers
        (lower endpoint, upper endpoint)

        .. SEEALSO::

            :meth:`edges` which returns the endpoints as exact
            intervals instead of real numbers.

        EXAMPLES::

            sage: RIF(1,2).endpoints()
            (1.00000000000000, 2.00000000000000)
            sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
            (3.14159265358979, 3.14159265358980)
            sage: a = CIF(RIF(1,2), RIF(3,4))
            sage: a.real().endpoints()
            (1.00000000000000, 2.00000000000000)

        As with ``lower()`` and ``upper()``, a rounding mode is accepted::

            sage: RIF(1,2).endpoints('RNDD')[0].parent()
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalFieldElement.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

        Return the lower and upper endpoints of this interval.

        OUTPUT: a 2-tuple of real numbers
        (lower endpoint, upper endpoint)

        .. SEEALSO::

            :meth:`edges` which returns the endpoints as exact
            intervals instead of real numbers.

        EXAMPLES::

            sage: RIF(1,2).endpoints()
            (1.00000000000000, 2.00000000000000)
            sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
            (3.14159265358979, 3.14159265358980)
            sage: a = CIF(RIF(1,2), RIF(3,4))
            sage: a.real().endpoints()
            (1.00000000000000, 2.00000000000000)

        As with ``lower()`` and ``upper()``, a rounding mode is accepted::

            sage: RIF(1,2).endpoints('RNDD')[0].parent()
            Real Field with 53 bits of precision and rounding RNDD"""
    def exp(self) -> Any:
        """RealIntervalFieldElement.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4538)

        Return `e^\\mathtt{self}`.

        EXAMPLES::

            sage: r = RIF(0.0)
            sage: r.exp()
            1

        ::

            sage: r = RIF(32.3)
            sage: a = r.exp(); a
            1.065888472748645?e14
            sage: a.log()
            32.30000000000000?

        ::

            sage: r = RIF(-32.3)
            sage: r.exp()
            9.38184458849869?e-15"""
    def exp2(self) -> Any:
        """RealIntervalFieldElement.exp2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4568)

        Return `2^\\mathtt{self}`.

        EXAMPLES::

            sage: r = RIF(0.0)
            sage: r.exp2()
            1

        ::

            sage: r = RIF(32.0)
            sage: r.exp2()
            4294967296

        ::

            sage: r = RIF(-32.3)
            sage: r.exp2()
            1.891172482530207?e-10"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def factorial(self) -> Any:
        """RealIntervalFieldElement.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

        Return the factorial evaluated on ``self``.

        EXAMPLES::

            sage: RIF(5).factorial()
            120
            sage: RIF(2.3,5.7).factorial()
            1.?e3
            sage: RIF(2.3).factorial()
            2.683437381955768?

        Recover the factorial as integer::

            sage: f = RealIntervalField(200)(50).factorial()
            sage: f
            3.0414093201713378043612608166064768844377641568960512000000000?e64
            sage: f.unique_integer()
            30414093201713378043612608166064768844377641568960512000000000000
            sage: 50.factorial()
            30414093201713378043612608166064768844377641568960512000000000000"""
    @overload
    def floor(self) -> Any:
        """RealIntervalFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

        Return the floor of this interval as an interval.

        The floor of a real number `x` is the largest integer smaller than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_floor` -- method which returns the floor as an integer
              if it is unique or raises a :exc:`ValueError` otherwise
            - :meth:`ceil` -- truncation towards plus infinity
            - :meth:`round` -- rounding
            - :meth:`trunc` -- truncation towards zero

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: (2.99).floor()
            2
            sage: (2.00).floor()
            2
            sage: floor(RR(-5/2))
            -3
            sage: R = RealIntervalField(100)
            sage: a = R(9.5, 11.3); a.str(style='brackets')
            '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
            sage: floor(a).str(style='brackets')
            '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
            sage: a.floor()
            10.?
            sage: ceil(a)
            11.?
            sage: a.ceil().str(style='brackets')
            '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
    @overload
    def floor(self) -> Any:
        """RealIntervalFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

        Return the floor of this interval as an interval.

        The floor of a real number `x` is the largest integer smaller than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_floor` -- method which returns the floor as an integer
              if it is unique or raises a :exc:`ValueError` otherwise
            - :meth:`ceil` -- truncation towards plus infinity
            - :meth:`round` -- rounding
            - :meth:`trunc` -- truncation towards zero

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: (2.99).floor()
            2
            sage: (2.00).floor()
            2
            sage: floor(RR(-5/2))
            -3
            sage: R = RealIntervalField(100)
            sage: a = R(9.5, 11.3); a.str(style='brackets')
            '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
            sage: floor(a).str(style='brackets')
            '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
            sage: a.floor()
            10.?
            sage: ceil(a)
            11.?
            sage: a.ceil().str(style='brackets')
            '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
    @overload
    def floor(self) -> Any:
        """RealIntervalFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

        Return the floor of this interval as an interval.

        The floor of a real number `x` is the largest integer smaller than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_floor` -- method which returns the floor as an integer
              if it is unique or raises a :exc:`ValueError` otherwise
            - :meth:`ceil` -- truncation towards plus infinity
            - :meth:`round` -- rounding
            - :meth:`trunc` -- truncation towards zero

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: (2.99).floor()
            2
            sage: (2.00).floor()
            2
            sage: floor(RR(-5/2))
            -3
            sage: R = RealIntervalField(100)
            sage: a = R(9.5, 11.3); a.str(style='brackets')
            '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
            sage: floor(a).str(style='brackets')
            '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
            sage: a.floor()
            10.?
            sage: ceil(a)
            11.?
            sage: a.ceil().str(style='brackets')
            '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
    @overload
    def floor(self, a) -> Any:
        """RealIntervalFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

        Return the floor of this interval as an interval.

        The floor of a real number `x` is the largest integer smaller than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_floor` -- method which returns the floor as an integer
              if it is unique or raises a :exc:`ValueError` otherwise
            - :meth:`ceil` -- truncation towards plus infinity
            - :meth:`round` -- rounding
            - :meth:`trunc` -- truncation towards zero

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: (2.99).floor()
            2
            sage: (2.00).floor()
            2
            sage: floor(RR(-5/2))
            -3
            sage: R = RealIntervalField(100)
            sage: a = R(9.5, 11.3); a.str(style='brackets')
            '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
            sage: floor(a).str(style='brackets')
            '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
            sage: a.floor()
            10.?
            sage: ceil(a)
            11.?
            sage: a.ceil().str(style='brackets')
            '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
    @overload
    def floor(self) -> Any:
        """RealIntervalFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

        Return the floor of this interval as an interval.

        The floor of a real number `x` is the largest integer smaller than or
        equal to `x`.

        .. SEEALSO::

            - :meth:`unique_floor` -- method which returns the floor as an integer
              if it is unique or raises a :exc:`ValueError` otherwise
            - :meth:`ceil` -- truncation towards plus infinity
            - :meth:`round` -- rounding
            - :meth:`trunc` -- truncation towards zero

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: (2.99).floor()
            2
            sage: (2.00).floor()
            2
            sage: floor(RR(-5/2))
            -3
            sage: R = RealIntervalField(100)
            sage: a = R(9.5, 11.3); a.str(style='brackets')
            '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
            sage: floor(a).str(style='brackets')
            '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
            sage: a.floor()
            10.?
            sage: ceil(a)
            11.?
            sage: a.ceil().str(style='brackets')
            '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
    def fp_rank_diameter(self) -> Any:
        '''RealIntervalFieldElement.fp_rank_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2452)

        Compute the diameter of this interval in terms of the
        "floating-point rank".

        The floating-point rank is the number of floating-point numbers (of
        the current precision) contained in the given interval, minus one. An
        ``fp_rank_diameter`` of 0 means that the interval is exact; an
        ``fp_rank_diameter`` of 1 means that the interval is
        as tight as possible, unless the number you\'re trying to represent
        is actually exactly representable as a floating-point number.

        EXAMPLES::

            sage: RIF(12345).fp_rank_diameter()
            0
            sage: RIF(5/8).fp_rank_diameter()
            0
            sage: RIF(5/7).fp_rank_diameter()
            1

            sage: # needs sage.symbolic
            sage: RIF(pi).fp_rank_diameter()
            1
            sage: RIF(-sqrt(2)).fp_rank_diameter()
            1
            sage: a = RIF(pi)^12345; a
            2.06622879260?e6137
            sage: a.fp_rank_diameter()
            30524
            sage: (RIF(sqrt(2)) - RIF(sqrt(2))).fp_rank_diameter()
            9671406088542672151117826            # 32-bit
            41538374868278620559869609387229186  # 64-bit

        Just because we have the best possible interval, doesn\'t mean the
        interval is actually small::

            sage: a = RIF(pi)^12345678901234567890; a                                   # needs sage.symbolic
            [2.0985787164673874e323228496 .. +infinity]            # 32-bit
            [5.8756537891115869e1388255822130839282 .. +infinity]  # 64-bit
            sage: a.fp_rank_diameter()                                                  # needs sage.symbolic
            1'''
    @overload
    def frac(self) -> Any:
        """RealIntervalFieldElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3172)

        Return the fractional part of this interval as an interval.

        The fractional part `y` of a real number `x` is the unique element in the
        interval `(-1,1)` that has the same sign as `x` and such that `x-y` is
        an integer. The integer `x-y` can be obtained through the method
        :meth:`trunc`.

        The output of this function is the smallest interval that contains all
        possible values of `frac(x)` for `x` in this interval. Note that if it
        contains an integer then the answer might not be very meaningful. More
        precisely, if the endpoints are `a` and `b` then:

        - if `floor(b) > \\max(a,0)` then the interval obtained contains `[0,1]`,
        - if `ceil(a) < \\min(b,0)` then the interval obtained contains `[-1,0]`.

        .. SEEALSO::

            :meth:`trunc` -- return the integer part complement to this
            fractional part

        EXAMPLES::

            sage: RIF(2.37123, 2.372).frac()
            0.372?
            sage: RIF(-23.12, -23.13).frac()
            -0.13?

            sage: RIF(.5, 1).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(1, 1.5).frac().endpoints()
            (0.000000000000000, 0.500000000000000)

            sage: r = RIF(-22.47, -22.468)
            sage: r in (r.frac() + r.trunc())
            True

            sage: r = RIF(18.222, 18.223)
            sage: r in (r.frac() + r.trunc())
            True

            sage: RIF(1.99, 2.025).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(1.99, 2.00).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(2.00, 2.025).frac().endpoints()
            (0.000000000000000, 0.0250000000000000)

            sage: RIF(-2.1,-0.9).frac().endpoints()
            (-1.00000000000000, -0.000000000000000)
            sage: RIF(-0.5,0.5).frac().endpoints()
            (-0.500000000000000, 0.500000000000000)"""
    @overload
    def frac(self, x) -> Any:
        """RealIntervalFieldElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3172)

        Return the fractional part of this interval as an interval.

        The fractional part `y` of a real number `x` is the unique element in the
        interval `(-1,1)` that has the same sign as `x` and such that `x-y` is
        an integer. The integer `x-y` can be obtained through the method
        :meth:`trunc`.

        The output of this function is the smallest interval that contains all
        possible values of `frac(x)` for `x` in this interval. Note that if it
        contains an integer then the answer might not be very meaningful. More
        precisely, if the endpoints are `a` and `b` then:

        - if `floor(b) > \\max(a,0)` then the interval obtained contains `[0,1]`,
        - if `ceil(a) < \\min(b,0)` then the interval obtained contains `[-1,0]`.

        .. SEEALSO::

            :meth:`trunc` -- return the integer part complement to this
            fractional part

        EXAMPLES::

            sage: RIF(2.37123, 2.372).frac()
            0.372?
            sage: RIF(-23.12, -23.13).frac()
            -0.13?

            sage: RIF(.5, 1).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(1, 1.5).frac().endpoints()
            (0.000000000000000, 0.500000000000000)

            sage: r = RIF(-22.47, -22.468)
            sage: r in (r.frac() + r.trunc())
            True

            sage: r = RIF(18.222, 18.223)
            sage: r in (r.frac() + r.trunc())
            True

            sage: RIF(1.99, 2.025).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(1.99, 2.00).frac().endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(2.00, 2.025).frac().endpoints()
            (0.000000000000000, 0.0250000000000000)

            sage: RIF(-2.1,-0.9).frac().endpoints()
            (-1.00000000000000, -0.000000000000000)
            sage: RIF(-0.5,0.5).frac().endpoints()
            (-0.500000000000000, 0.500000000000000)"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def gamma(self) -> Any:
        """RealIntervalFieldElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

        Return the gamma function evaluated on ``self``.

        EXAMPLES::

            sage: RIF(1).gamma()
            1
            sage: RIF(5).gamma()
            24
            sage: a = RIF(3,4).gamma(); a
            1.?e1
            sage: a.lower(), a.upper()
            (2.00000000000000, 6.00000000000000)
            sage: RIF(-1/2).gamma()
            -3.54490770181104?
            sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
            True
            sage: RIF1000 = RealIntervalField(1000)
            sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
            True
            sage: gamma(RIF(100))
            9.33262154439442?e155
            sage: gamma(RIF(-10000/3))
            1.31280781451?e-10297

        Verify the result contains the local minima::

            sage: 0.88560319441088 in RIF(1, 2).gamma()
            True
            sage: 0.88560319441088 in RIF(0.25, 4).gamma()
            True
            sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
            True

            sage: (-0.99).gamma()
            -100.436954665809
            sage: (-0.01).gamma()
            -100.587197964411
            sage: RIF(-0.99, -0.01).gamma().upper()
            -1.60118039970055

        Correctly detects poles::

            sage: gamma(RIF(-3/2,-1/2))
            [-infinity .. +infinity]"""
    @overload
    def imag(self) -> Any:
        """RealIntervalFieldElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1478)

        Return the imaginary part of this real interval.

        (Since this is interval is real, this simply returns the zero interval.)

        .. SEEALSO::

            :meth:`real`

        EXAMPLES::

            sage: RIF(2,3).imag()
            0"""
    @overload
    def imag(self) -> Any:
        """RealIntervalFieldElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1478)

        Return the imaginary part of this real interval.

        (Since this is interval is real, this simply returns the zero interval.)

        .. SEEALSO::

            :meth:`real`

        EXAMPLES::

            sage: RIF(2,3).imag()
            0"""
    def intersection(self, other) -> Any:
        """RealIntervalFieldElement.intersection(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4074)

        Return the intersection of two intervals. If the intervals do not
        overlap, raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1, 2).intersection(RIF(1.5, 3)).str(style='brackets')
            '[1.5000000000000000 .. 2.0000000000000000]'
            sage: RIF(1, 2).intersection(RIF(4/3, 5/3)).str(style='brackets')
            '[1.3333333333333332 .. 1.6666666666666668]'
            sage: RIF(1, 2).intersection(RIF(3, 4))
            Traceback (most recent call last):
            ...
            ValueError: intersection of non-overlapping intervals"""
    @overload
    def is_NaN(self) -> Any:
        """RealIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3703)

        Check to see if ``self`` is Not-a-Number ``NaN``.

        EXAMPLES::

            sage: a = RIF(0) / RIF(0.0,0.00); a
            [.. NaN ..]
            sage: a.is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """RealIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3703)

        Check to see if ``self`` is Not-a-Number ``NaN``.

        EXAMPLES::

            sage: a = RIF(0) / RIF(0.0,0.00); a
            [.. NaN ..]
            sage: a.is_NaN()
            True"""
    @overload
    def is_exact(self) -> Any:
        """RealIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

        Return whether this real interval is exact (i.e. contains exactly
        one real value).

        EXAMPLES::

            sage: RIF(3).is_exact()
            True
            sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

        Return whether this real interval is exact (i.e. contains exactly
        one real value).

        EXAMPLES::

            sage: RIF(3).is_exact()
            True
            sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

        Return whether this real interval is exact (i.e. contains exactly
        one real value).

        EXAMPLES::

            sage: RIF(3).is_exact()
            True
            sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
            False"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    @overload
    def is_int(self) -> Any:
        """RealIntervalFieldElement.is_int(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

        Check to see whether this interval includes exactly one integer.

        OUTPUT:

        If this contains exactly one integer, it returns the tuple
        ``(True, n)``, where ``n`` is that integer; otherwise, this returns
        ``(False, None)``.

        EXAMPLES::

            sage: a = RIF(0.8,1.5)
            sage: a.is_int()
            (True, 1)
            sage: a = RIF(1.1,1.5)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(1,2)
            sage: a.is_int()
            (False, None)
            sage: a = RIF(-1.1, -0.9)
            sage: a.is_int()
            (True, -1)
            sage: a = RIF(0.1, 1.9)
            sage: a.is_int()
            (True, 1)
            sage: RIF(+infinity,+infinity).is_int()
            (False, None)"""
    def lexico_cmp(self, left, right) -> Any:
        """RealIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3948)

        Compare two intervals lexicographically.

        This means that the left bounds are compared first and then
        the right bounds are compared if the left bounds coincide.

        Return 0 if they are the same interval, -1 if the second is larger,
        or 1 if the first is larger.

        EXAMPLES::

            sage: RIF(0).lexico_cmp(RIF(1))
            -1
            sage: RIF(0, 1).lexico_cmp(RIF(1))
            -1
            sage: RIF(0, 1).lexico_cmp(RIF(1, 2))
            -1
            sage: RIF(0, 0.99999).lexico_cmp(RIF(1, 2))
            -1
            sage: RIF(1, 2).lexico_cmp(RIF(0, 1))
            1
            sage: RIF(1, 2).lexico_cmp(RIF(0))
            1
            sage: RIF(0, 1).lexico_cmp(RIF(0, 2))
            -1
            sage: RIF(0, 1).lexico_cmp(RIF(0, 1))
            0
            sage: RIF(0, 1).lexico_cmp(RIF(0, 1/2))
            1"""
    @overload
    def log(self, base=...) -> Any:
        """RealIntervalFieldElement.log(self, base='e')

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

        Return the logarithm of ``self`` to the given ``base``.

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: r = R(2); r.log()
            0.6931471805599453?
            sage: r = R(-2); r.log()
            0.6931471805599453? + 3.141592653589794?*I"""
    @overload
    def log(self) -> Any:
        """RealIntervalFieldElement.log(self, base='e')

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

        Return the logarithm of ``self`` to the given ``base``.

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: r = R(2); r.log()
            0.6931471805599453?
            sage: r = R(-2); r.log()
            0.6931471805599453? + 3.141592653589794?*I"""
    @overload
    def log(self) -> Any:
        """RealIntervalFieldElement.log(self, base='e')

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

        Return the logarithm of ``self`` to the given ``base``.

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: r = R(2); r.log()
            0.6931471805599453?
            sage: r = R(-2); r.log()
            0.6931471805599453? + 3.141592653589794?*I"""
    @overload
    def log10(self) -> Any:
        """RealIntervalFieldElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0); r.log10()
            1.204119982655925?
            sage: r.log() / RIF(10).log()
            1.204119982655925?

        ::

            sage: r = RIF(39.9); r.log10()
            1.600972895686749?

        ::

            sage: r = RIF(0.0)
            sage: r.log10()
            [-infinity .. -infinity]

        ::

            sage: r = RIF(-1.0)
            sage: r.log10()
            1.364376353841841?*I"""
    @overload
    def log10(self) -> Any:
        """RealIntervalFieldElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0); r.log10()
            1.204119982655925?
            sage: r.log() / RIF(10).log()
            1.204119982655925?

        ::

            sage: r = RIF(39.9); r.log10()
            1.600972895686749?

        ::

            sage: r = RIF(0.0)
            sage: r.log10()
            [-infinity .. -infinity]

        ::

            sage: r = RIF(-1.0)
            sage: r.log10()
            1.364376353841841?*I"""
    @overload
    def log10(self) -> Any:
        """RealIntervalFieldElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0); r.log10()
            1.204119982655925?
            sage: r.log() / RIF(10).log()
            1.204119982655925?

        ::

            sage: r = RIF(39.9); r.log10()
            1.600972895686749?

        ::

            sage: r = RIF(0.0)
            sage: r.log10()
            [-infinity .. -infinity]

        ::

            sage: r = RIF(-1.0)
            sage: r.log10()
            1.364376353841841?*I"""
    @overload
    def log10(self) -> Any:
        """RealIntervalFieldElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0); r.log10()
            1.204119982655925?
            sage: r.log() / RIF(10).log()
            1.204119982655925?

        ::

            sage: r = RIF(39.9); r.log10()
            1.600972895686749?

        ::

            sage: r = RIF(0.0)
            sage: r.log10()
            [-infinity .. -infinity]

        ::

            sage: r = RIF(-1.0)
            sage: r.log10()
            1.364376353841841?*I"""
    @overload
    def log10(self) -> Any:
        """RealIntervalFieldElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0); r.log10()
            1.204119982655925?
            sage: r.log() / RIF(10).log()
            1.204119982655925?

        ::

            sage: r = RIF(39.9); r.log10()
            1.600972895686749?

        ::

            sage: r = RIF(0.0)
            sage: r.log10()
            [-infinity .. -infinity]

        ::

            sage: r = RIF(-1.0)
            sage: r.log10()
            1.364376353841841?*I"""
    @overload
    def log2(self) -> Any:
        """RealIntervalFieldElement.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

        Return ``log`` to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0)
            sage: r.log2()
            4

        ::

            sage: r = RIF(31.9); r.log2()
            4.995484518877507?

        ::

            sage: r = RIF(0.0, 2.0)
            sage: r.log2()
            [-infinity .. 1.0000000000000000]"""
    @overload
    def log2(self) -> Any:
        """RealIntervalFieldElement.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

        Return ``log`` to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0)
            sage: r.log2()
            4

        ::

            sage: r = RIF(31.9); r.log2()
            4.995484518877507?

        ::

            sage: r = RIF(0.0, 2.0)
            sage: r.log2()
            [-infinity .. 1.0000000000000000]"""
    @overload
    def log2(self) -> Any:
        """RealIntervalFieldElement.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

        Return ``log`` to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0)
            sage: r.log2()
            4

        ::

            sage: r = RIF(31.9); r.log2()
            4.995484518877507?

        ::

            sage: r = RIF(0.0, 2.0)
            sage: r.log2()
            [-infinity .. 1.0000000000000000]"""
    @overload
    def log2(self) -> Any:
        """RealIntervalFieldElement.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

        Return ``log`` to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RIF(16.0)
            sage: r.log2()
            4

        ::

            sage: r = RIF(31.9); r.log2()
            4.995484518877507?

        ::

            sage: r = RIF(0.0, 2.0)
            sage: r.log2()
            [-infinity .. 1.0000000000000000]"""
    @overload
    def lower(self, rnd=...) -> Any:
        """RealIntervalFieldElement.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

        Return the lower bound of this interval.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards minus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().lower().str()
            '3.1411'

        ::

            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.lower()
            1.19
            sage: x.lower('RNDU')
            1.20
            sage: x.lower('RNDN')
            1.20
            sage: x.lower('RNDZ')
            1.19
            sage: x.lower('RNDA')
            1.20
            sage: x.lower().parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.lower('RNDU').parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.lower('RNDA').parent()
            Real Field with 13 bits of precision and rounding RNDA
            sage: x.lower() == x.lower('RNDU')
            True"""
    @overload
    def lower(self) -> Any:
        """RealIntervalFieldElement.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

        Return the lower bound of this interval.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards minus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().lower().str()
            '3.1411'

        ::

            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.lower()
            1.19
            sage: x.lower('RNDU')
            1.20
            sage: x.lower('RNDN')
            1.20
            sage: x.lower('RNDZ')
            1.19
            sage: x.lower('RNDA')
            1.20
            sage: x.lower().parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.lower('RNDU').parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.lower('RNDA').parent()
            Real Field with 13 bits of precision and rounding RNDA
            sage: x.lower() == x.lower('RNDU')
            True"""
    @overload
    def lower(self) -> Any:
        """RealIntervalFieldElement.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

        Return the lower bound of this interval.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards minus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().lower().str()
            '3.1411'

        ::

            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.lower()
            1.19
            sage: x.lower('RNDU')
            1.20
            sage: x.lower('RNDN')
            1.20
            sage: x.lower('RNDZ')
            1.19
            sage: x.lower('RNDA')
            1.20
            sage: x.lower().parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.lower('RNDU').parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.lower('RNDA').parent()
            Real Field with 13 bits of precision and rounding RNDA
            sage: x.lower() == x.lower('RNDU')
            True"""
    @overload
    def lower(self) -> Any:
        """RealIntervalFieldElement.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

        Return the lower bound of this interval.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards minus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().lower().str()
            '3.1411'

        ::

            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.lower()
            1.19
            sage: x.lower('RNDU')
            1.20
            sage: x.lower('RNDN')
            1.20
            sage: x.lower('RNDZ')
            1.19
            sage: x.lower('RNDA')
            1.20
            sage: x.lower().parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.lower('RNDU').parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.lower('RNDA').parent()
            Real Field with 13 bits of precision and rounding RNDA
            sage: x.lower() == x.lower('RNDU')
            True"""
    @overload
    def magnitude(self) -> Any:
        """RealIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

        The largest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: RIF(-2, 1).magnitude()
            2.00000000000000
            sage: RIF(-1, 2).magnitude()
            2.00000000000000
            sage: parent(RIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """RealIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

        The largest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: RIF(-2, 1).magnitude()
            2.00000000000000
            sage: RIF(-1, 2).magnitude()
            2.00000000000000
            sage: parent(RIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """RealIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

        The largest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: RIF(-2, 1).magnitude()
            2.00000000000000
            sage: RIF(-1, 2).magnitude()
            2.00000000000000
            sage: parent(RIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """RealIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

        The largest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: RIF(-2, 1).magnitude()
            2.00000000000000
            sage: RIF(-1, 2).magnitude()
            2.00000000000000
            sage: parent(RIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def max(self, *_others) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def max(self, a, b) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def max(self, a, c) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def max(self, b, c) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def max(self, a, b, c) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def max(self, *elements) -> Any:
        """RealIntervalFieldElement.max(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

        Return an interval containing the maximum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: RIF(-1, 1).max(0).endpoints()
            (0.000000000000000, 1.00000000000000)
            sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
            (2.00000000000000, 3.00000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
            (-1.00000000000000, 100.000000000000)
            sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
            (5.00000000000000, 100.000000000000)

        Note that if the maximum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.max(a, b) is c
            True
            sage: b.max(a, c) is c
            True
            sage: a.max(b, c) is c
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.max(a, b, c) is c
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.max(*elements) is c
            True

        The generic max does not always do the right thing::

            sage: max(0, RIF(-1, 1))
            0
            sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').max(1, 2)
            2
            sage: RIF(-1/3).max(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').max(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

        TESTS::

            sage: a.max('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def mignitude(self) -> Any:
        """RealIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

        The smallest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: RIF(-2, 1).mignitude()
            0.000000000000000
            sage: RIF(-2, -1).mignitude()
            1.00000000000000
            sage: RIF(3, 4).mignitude()
            3.00000000000000
            sage: parent(RIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """RealIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

        The smallest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: RIF(-2, 1).mignitude()
            0.000000000000000
            sage: RIF(-2, -1).mignitude()
            1.00000000000000
            sage: RIF(3, 4).mignitude()
            3.00000000000000
            sage: parent(RIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """RealIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

        The smallest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: RIF(-2, 1).mignitude()
            0.000000000000000
            sage: RIF(-2, -1).mignitude()
            1.00000000000000
            sage: RIF(3, 4).mignitude()
            3.00000000000000
            sage: parent(RIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """RealIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

        The smallest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: RIF(-2, 1).mignitude()
            0.000000000000000
            sage: RIF(-2, -1).mignitude()
            1.00000000000000
            sage: RIF(3, 4).mignitude()
            3.00000000000000
            sage: parent(RIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """RealIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

        The smallest absolute value of the elements of the interval.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: RIF(-2, 1).mignitude()
            0.000000000000000
            sage: RIF(-2, -1).mignitude()
            1.00000000000000
            sage: RIF(3, 4).mignitude()
            3.00000000000000
            sage: parent(RIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def min(self, *_others) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, pi) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, a, b) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, a, c) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, b, c) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, a, b, c) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    @overload
    def min(self, *elements) -> Any:
        """RealIntervalFieldElement.min(self, *_others)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

        Return an interval containing the minimum of ``self`` and the
        arguments.

        EXAMPLES::

            sage: a = RIF(-1, 1).min(0).endpoints()
            sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
            True
            sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
            (-1.00000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
            (-100.000000000000, 1.00000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
            (-100.000000000000, 0.000000000000000)
            sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
            (-200.000000000000, -3.00000000000000)

        Note that if the minimum is one of the given elements,
        that element will be returned. ::

            sage: a = RIF(-1, 1)
            sage: b = RIF(2, 3)
            sage: c = RIF(3, 4)
            sage: c.min(a, b) is a
            True
            sage: b.min(a, c) is a
            True
            sage: a.min(b, c) is a
            True

        It might also be convenient to call the method as a function::

            sage: from sage.rings.real_mpfi import RealIntervalFieldElement
            sage: RealIntervalFieldElement.min(a, b, c) is a
            True
            sage: elements = [a, b, c]
            sage: RealIntervalFieldElement.min(*elements) is a
            True

        The generic min does not always do the right thing::

            sage: min(0, RIF(-1, 1))
            0
            sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
            (-1.00000000000000, 1.00000000000000)

        Note that calls involving NaNs try to return a number when possible.
        This is consistent with IEEE-754-2008 but may be surprising. ::

            sage: RIF('nan').min(2, 1)
            1
            sage: RIF(-1/3).min(RIF('nan'))
            -0.3333333333333334?
            sage: RIF('nan').min(RIF('nan'))
            [.. NaN ..]

        .. SEEALSO::

            :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

        TESTS::

            sage: a.min('x')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to real interval"""
    def multiplicative_order(self) -> Any:
        """RealIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2982)

        Return `n` such that ``self^n == 1``.

        Only `\\pm 1` have finite multiplicative order.

        EXAMPLES::

            sage: RIF(1).multiplicative_order()
            1
            sage: RIF(-1).multiplicative_order()
            2
            sage: RIF(3).multiplicative_order()
            +Infinity"""
    @overload
    def overlaps(self, RealIntervalFieldElementother) -> Any:
        """RealIntervalFieldElement.overlaps(self, RealIntervalFieldElement other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4050)

        Return ``True`` if ``self`` and ``other`` are intervals with at least one
        value in common. For intervals ``a`` and ``b``, we have
        ``a.overlaps(b)`` iff ``not(a!=b)``.

        EXAMPLES::

            sage: RIF(0, 1).overlaps(RIF(1, 2))
            True
            sage: RIF(1, 2).overlaps(RIF(0, 1))
            True
            sage: RIF(0, 1).overlaps(RIF(2, 3))
            False
            sage: RIF(2, 3).overlaps(RIF(0, 1))
            False
            sage: RIF(0, 3).overlaps(RIF(1, 2))
            True
            sage: RIF(0, 2).overlaps(RIF(1, 3))
            True"""
    @overload
    def overlaps(self, b) -> Any:
        """RealIntervalFieldElement.overlaps(self, RealIntervalFieldElement other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4050)

        Return ``True`` if ``self`` and ``other`` are intervals with at least one
        value in common. For intervals ``a`` and ``b``, we have
        ``a.overlaps(b)`` iff ``not(a!=b)``.

        EXAMPLES::

            sage: RIF(0, 1).overlaps(RIF(1, 2))
            True
            sage: RIF(1, 2).overlaps(RIF(0, 1))
            True
            sage: RIF(0, 1).overlaps(RIF(2, 3))
            False
            sage: RIF(2, 3).overlaps(RIF(0, 1))
            False
            sage: RIF(0, 3).overlaps(RIF(1, 2))
            True
            sage: RIF(0, 2).overlaps(RIF(1, 3))
            True"""
    def prec(self, *args, **kwargs):
        """RealIntervalFieldElement.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

        Return the precision of ``self``.

        EXAMPLES::

            sage: RIF(2.1).precision()
            53
            sage: RealIntervalField(200)(2.1).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalFieldElement.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

        Return the precision of ``self``.

        EXAMPLES::

            sage: RIF(2.1).precision()
            53
            sage: RealIntervalField(200)(2.1).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalFieldElement.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

        Return the precision of ``self``.

        EXAMPLES::

            sage: RIF(2.1).precision()
            53
            sage: RealIntervalField(200)(2.1).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalFieldElement.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

        Return the precision of ``self``.

        EXAMPLES::

            sage: RIF(2.1).precision()
            53
            sage: RealIntervalField(200)(2.1).precision()
            200"""
    @overload
    def psi(self) -> Any:
        """RealIntervalFieldElement.psi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5155)

        Return the digamma function evaluated on ``self``.

        OUTPUT: a :class:`RealIntervalFieldElement`

        EXAMPLES::

            sage: psi_1 = RIF(1).psi()
            sage: psi_1
            -0.577215664901533?
            sage: psi_1.overlaps(-RIF.euler_constant())
            True"""
    @overload
    def psi(self) -> Any:
        """RealIntervalFieldElement.psi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5155)

        Return the digamma function evaluated on ``self``.

        OUTPUT: a :class:`RealIntervalFieldElement`

        EXAMPLES::

            sage: psi_1 = RIF(1).psi()
            sage: psi_1
            -0.577215664901533?
            sage: psi_1.overlaps(-RIF.euler_constant())
            True"""
    @overload
    def real(self) -> Any:
        """RealIntervalFieldElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1461)

        Return the real part of this real interval.

        (Since this interval is real, this simply returns itself.)

        .. SEEALSO::

            :meth:`imag`

        EXAMPLES::

            sage: RIF(1.2465).real() == RIF(1.2465)
            True"""
    @overload
    def real(self) -> Any:
        """RealIntervalFieldElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1461)

        Return the real part of this real interval.

        (Since this interval is real, this simply returns itself.)

        .. SEEALSO::

            :meth:`imag`

        EXAMPLES::

            sage: RIF(1.2465).real() == RIF(1.2465)
            True"""
    @overload
    def relative_diameter(self) -> Any:
        """RealIntervalFieldElement.relative_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2404)

        The relative diameter of this interval (for `[a .. b]`, this is
        `(b-a)/((a+b)/2)`), rounded upward, as a :class:`RealNumber`.

        EXAMPLES::

            sage: RIF(1, pi).relative_diameter()                                        # needs sage.symbolic
            1.03418797197910"""
    @overload
    def relative_diameter(self) -> Any:
        """RealIntervalFieldElement.relative_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2404)

        The relative diameter of this interval (for `[a .. b]`, this is
        `(b-a)/((a+b)/2)`), rounded upward, as a :class:`RealNumber`.

        EXAMPLES::

            sage: RIF(1, pi).relative_diameter()                                        # needs sage.symbolic
            1.03418797197910"""
    def round(self) -> Any:
        """RealIntervalFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3097)

        Return the nearest integer of this interval as an interval.

        .. SEEALSO::

            - :meth:`unique_round` -- return the round as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards `-\\infty`
            - :meth:`ceil` -- truncation towards `+\\infty`
            - :meth:`trunc` -- truncation towards `0`

        EXAMPLES::

            sage: RIF(7.2, 7.3).round()
            7
            sage: RIF(-3.2, -3.1).round()
            -3

        Be careful that the answer is not an integer but an interval::

            sage: RIF(2.2, 2.3).round().parent()
            Real Interval Field with 53 bits of precision

        And in some cases, the lower and upper bounds of this interval do not
        agree::

            sage: r = RIF(2.5, 3.5).round()
            sage: r
            4.?
            sage: r.lower()
            3.00000000000000
            sage: r.upper()
            4.00000000000000"""
    @overload
    def sec(self) -> Any:
        """RealIntervalFieldElement.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4894)

        Return the secant of this number.

        EXAMPLES::

            sage: RealIntervalField(100)(2).sec()
            -2.40299796172238098975460040142?"""
    @overload
    def sec(self) -> Any:
        """RealIntervalFieldElement.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4894)

        Return the secant of this number.

        EXAMPLES::

            sage: RealIntervalField(100)(2).sec()
            -2.40299796172238098975460040142?"""
    @overload
    def sech(self) -> Any:
        """RealIntervalFieldElement.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4927)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).sech()
            0.265802228834079692120862739820?"""
    @overload
    def sech(self) -> Any:
        """RealIntervalFieldElement.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4927)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RealIntervalField(100)(2).sech()
            0.265802228834079692120862739820?"""
    @overload
    def simplest_rational(self, low_open=..., high_open=...) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self, high_open=...) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self, high_open=...) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def simplest_rational(self) -> Any:
        """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

        Return the simplest rational in this interval. Given rationals
        `a / b` and `c / d` (both in lowest terms), the former is simpler if
        `b<d` or if `b = d` and `|a| < |c|`.

        If optional parameters ``low_open`` or ``high_open`` are ``True``,
        then treat this as an open interval on that end.

        EXAMPLES::

            sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
            22/7
            sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
            355/113
            sage: RIF(0.123, 0.567).simplest_rational()
            1/2
            sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
            2/5
            sage: RIF(1234/567).simplest_rational()
            1234/567
            sage: RIF(-8765/432).simplest_rational()
            -8765/432
            sage: RIF(-1.234, 0.003).simplest_rational()
            0
            sage: RIF(RR(1/3)).simplest_rational()
            6004799503160661/18014398509481984
            sage: RIF(RR(1/3)).simplest_rational(high_open=True)
            Traceback (most recent call last):
            ...
            ValueError: simplest_rational() on open, empty interval
            sage: RIF(1/3, 1/2).simplest_rational()
            1/2
            sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
            1/3
            sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
            sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
            True"""
    @overload
    def sin(self) -> Any:
        """RealIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4668)

        Return the sine of ``self``.

        EXAMPLES::

            sage: R = RealIntervalField(100)
            sage: R(2).sin()
            0.909297426825681695396019865912?"""
    @overload
    def sin(self) -> Any:
        """RealIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4668)

        Return the sine of ``self``.

        EXAMPLES::

            sage: R = RealIntervalField(100)
            sage: R(2).sin()
            0.909297426825681695396019865912?"""
    @overload
    def sinh(self) -> Any:
        """RealIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4806)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/12
            sage: q.sinh()
            0.2648002276022707?"""
    @overload
    def sinh(self) -> Any:
        """RealIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4806)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/12
            sage: q.sinh()
            0.2648002276022707?"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalFieldElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

        Return a square root of ``self``. Raises an error if ``self`` is
        nonpositive.

        If you use :meth:`square_root()` then an interval will always be
        returned (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(4.0)
            sage: r.sqrt()
            2
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RIF(4344)
            sage: r.sqrt()
            65.90902821313633?
            sage: r.sqrt()^2 == r
            False
            sage: r in r.sqrt()^2
            True
            sage: r.sqrt()^2 - r
            0.?e-11
            sage: (r.sqrt()^2 - r).str(style='brackets')
            '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

        ::

            sage: r = RIF(-2.0)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0

        ::

            sage: r = RIF(-2, 2)
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=0.?e1) is not >= 0"""
    @overload
    def square(self) -> Any:
        """RealIntervalFieldElement.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

        Return the square of ``self``.

        .. NOTE::

            Squaring an interval is different than multiplying it by itself,
            because the square can never be negative.

        EXAMPLES::

            sage: RIF(1, 2).square().str(style='brackets')
            '[1.0000000000000000 .. 4.0000000000000000]'
            sage: RIF(-1, 1).square().str(style='brackets')
            '[0.0000000000000000 .. 1.0000000000000000]'
            sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
            '[-1.0000000000000000 .. 1.0000000000000000]'"""
    @overload
    def square(self) -> Any:
        """RealIntervalFieldElement.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

        Return the square of ``self``.

        .. NOTE::

            Squaring an interval is different than multiplying it by itself,
            because the square can never be negative.

        EXAMPLES::

            sage: RIF(1, 2).square().str(style='brackets')
            '[1.0000000000000000 .. 4.0000000000000000]'
            sage: RIF(-1, 1).square().str(style='brackets')
            '[0.0000000000000000 .. 1.0000000000000000]'
            sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
            '[-1.0000000000000000 .. 1.0000000000000000]'"""
    @overload
    def square(self) -> Any:
        """RealIntervalFieldElement.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

        Return the square of ``self``.

        .. NOTE::

            Squaring an interval is different than multiplying it by itself,
            because the square can never be negative.

        EXAMPLES::

            sage: RIF(1, 2).square().str(style='brackets')
            '[1.0000000000000000 .. 4.0000000000000000]'
            sage: RIF(-1, 1).square().str(style='brackets')
            '[0.0000000000000000 .. 1.0000000000000000]'
            sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
            '[-1.0000000000000000 .. 1.0000000000000000]'"""
    @overload
    def square_root(self) -> Any:
        """RealIntervalFieldElement.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4401)

        Return a square root of ``self``. An interval will always be returned
        (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(-2.0)
            sage: r.square_root()
            [.. NaN ..]
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0"""
    @overload
    def square_root(self) -> Any:
        """RealIntervalFieldElement.square_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4401)

        Return a square root of ``self``. An interval will always be returned
        (though it will be ``NaN`` if ``self`` is nonpositive).

        EXAMPLES::

            sage: r = RIF(-2.0)
            sage: r.square_root()
            [.. NaN ..]
            sage: r.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: self (=-2) is not >= 0"""
    @overload
    def str(self, intbase=..., style=..., no_sci=..., e=..., error_digits=...) -> Any:
        '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- base for output

        - ``style`` -- the printing style; either ``\'brackets\'`` or
          ``\'question\'`` (or ``None``, to use the current default)

        - ``no_sci`` -- if ``True`` do not print using scientific
          notation; if ``False`` print with scientific notation; if ``None``
          (the default), print how the parent prints.

        - ``e`` -- symbol used in scientific notation

        - ``error_digits`` -- the number of digits of error to
          print, in ``\'question\'`` style

        We support two different styles of printing; ``\'question\'`` style and
        ``\'brackets\'`` style. In question style (the default), we print the
        "known correct" part of the number, followed by a question mark::

            sage: RIF(pi).str()                                                         # needs sage.symbolic
            \'3.141592653589794?\'
            sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
            \'3.142?\'
            sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
            \'3.142?\'

        However, if the interval is precisely equal to some integer that\'s
        not too large, we just return that integer::

            sage: RIF(-42).str()
            \'-42\'
            sage: RIF(0).str()
            \'0\'
            sage: RIF(12^5).str(base=3)
            \'110122100000\'

        Very large integers, however, revert to the normal question-style
        printing::

            sage: RIF(3^7).str()
            \'2187\'
            sage: RIF(3^7 * 2^256).str()
            \'2.5323729916201052?e80\'

        In brackets style, we print the lower and upper bounds of the
        interval within brackets::

            sage: RIF(237/16).str(style=\'brackets\')
            \'[14.812500000000000 .. 14.812500000000000]\'

        Note that the lower bound is rounded down, and the upper bound is
        rounded up. So even if the lower and upper bounds are equal, they
        may print differently. (This is done so that the printed
        representation of the interval contains all the numbers in the
        internal binary interval.)

        For instance, we find the best 10-bit floating point representation
        of ``1/3``::

            sage: RR10 = RealField(10)
            sage: RR(RR10(1/3))
            0.333496093750000

        And we see that the point interval containing only this
        floating-point number prints as a wider decimal interval, that does
        contain the number::

            sage: RIF10 = RealIntervalField(10)
            sage: RIF10(RR10(1/3)).str(style=\'brackets\')
            \'[0.33349 .. 0.33350]\'

        We always use brackets style for ``NaN`` and infinities::

            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]

        Let\'s take a closer, formal look at the question style. In its full
        generality, a number printed in the question style looks like:

        MANTISSA ?ERROR eEXPONENT

        (without the spaces). The "eEXPONENT" part is optional; if it is
        missing, then the exponent is 0. (If the base is greater than 10,
        then the exponent separator is "@" instead of "e".)

        The "ERROR" is optional; if it is missing, then the error is 1.

        The mantissa is printed in base `b`, and always contains a
        decimal point (also known as a radix point, in bases other than
        10). (The error and exponent are always printed in base 10.)

        We define the "precision" of a floating-point printed
        representation to be the positional value of the last digit of the
        mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
        in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
        is `10^{-2}`. This precision will always be `10^k`
        for some `k` (or, for an arbitrary base `b`, `b^k`).

        Then the interval is contained in the interval:

        .. MATH::

            \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
            .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
            b^k

        To control the printing, we can specify a maximum number of error
        digits. The default is 0, which means that we do not print an error
        at all (so that the error is always the default, 1).

        Now, consider the precisions needed to represent the endpoints
        (this is the precision that would be produced by
        ``v.lower().str(no_sci=False)``). Our
        result is no more precise than the less precise endpoint, and is
        sufficiently imprecise that the error can be represented with the
        given number of decimal digits. Our result is the most precise
        possible result, given these restrictions. When there are two
        possible results of equal precision and with the same error width,
        then we pick the one which is farther from zero. (For instance,
        ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
        ``62.?62``. We prefer the latter because it makes it clear that the
        interval is known not to be negative.)

        EXAMPLES::

            sage: a = RIF(59/27); a
            2.185185185185186?
            sage: a.str()
            \'2.185185185185186?\'
            sage: a.str(style=\'brackets\')
            \'[2.1851851851851851 .. 2.1851851851851856]\'
            sage: a.str(16)
            \'2.2f684bda12f69?\'
            sage: a.str(no_sci=False)
            \'2.185185185185186?e0\'
            sage: pi_appr = RIF(pi, 22/7)
            sage: pi_appr.str(style=\'brackets\')
            \'[3.1415926535897931 .. 3.1428571428571433]\'
            sage: pi_appr.str()
            \'3.142?\'
            sage: pi_appr.str(error_digits=1)
            \'3.1422?7\'
            sage: pi_appr.str(error_digits=2)
            \'3.14223?64\'
            sage: pi_appr.str(base=36)
            \'3.6?\'
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]
            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
            [-infinity .. 3.1415926535897936]
            sage: RealIntervalField(210)(3).sqrt()
            1.732050807568877293527446341505872366942805253810380628055806980?
            sage: RealIntervalField(210)(RIF(3).sqrt())
            1.732050807568878?
            sage: RIF(3).sqrt()
            1.732050807568878?
            sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
            1.?e-71

        TESTS:

        Check that :issue:`13634` is fixed::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?'''
    @overload
    def str(self) -> Any:
        '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- base for output

        - ``style`` -- the printing style; either ``\'brackets\'`` or
          ``\'question\'`` (or ``None``, to use the current default)

        - ``no_sci`` -- if ``True`` do not print using scientific
          notation; if ``False`` print with scientific notation; if ``None``
          (the default), print how the parent prints.

        - ``e`` -- symbol used in scientific notation

        - ``error_digits`` -- the number of digits of error to
          print, in ``\'question\'`` style

        We support two different styles of printing; ``\'question\'`` style and
        ``\'brackets\'`` style. In question style (the default), we print the
        "known correct" part of the number, followed by a question mark::

            sage: RIF(pi).str()                                                         # needs sage.symbolic
            \'3.141592653589794?\'
            sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
            \'3.142?\'
            sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
            \'3.142?\'

        However, if the interval is precisely equal to some integer that\'s
        not too large, we just return that integer::

            sage: RIF(-42).str()
            \'-42\'
            sage: RIF(0).str()
            \'0\'
            sage: RIF(12^5).str(base=3)
            \'110122100000\'

        Very large integers, however, revert to the normal question-style
        printing::

            sage: RIF(3^7).str()
            \'2187\'
            sage: RIF(3^7 * 2^256).str()
            \'2.5323729916201052?e80\'

        In brackets style, we print the lower and upper bounds of the
        interval within brackets::

            sage: RIF(237/16).str(style=\'brackets\')
            \'[14.812500000000000 .. 14.812500000000000]\'

        Note that the lower bound is rounded down, and the upper bound is
        rounded up. So even if the lower and upper bounds are equal, they
        may print differently. (This is done so that the printed
        representation of the interval contains all the numbers in the
        internal binary interval.)

        For instance, we find the best 10-bit floating point representation
        of ``1/3``::

            sage: RR10 = RealField(10)
            sage: RR(RR10(1/3))
            0.333496093750000

        And we see that the point interval containing only this
        floating-point number prints as a wider decimal interval, that does
        contain the number::

            sage: RIF10 = RealIntervalField(10)
            sage: RIF10(RR10(1/3)).str(style=\'brackets\')
            \'[0.33349 .. 0.33350]\'

        We always use brackets style for ``NaN`` and infinities::

            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]

        Let\'s take a closer, formal look at the question style. In its full
        generality, a number printed in the question style looks like:

        MANTISSA ?ERROR eEXPONENT

        (without the spaces). The "eEXPONENT" part is optional; if it is
        missing, then the exponent is 0. (If the base is greater than 10,
        then the exponent separator is "@" instead of "e".)

        The "ERROR" is optional; if it is missing, then the error is 1.

        The mantissa is printed in base `b`, and always contains a
        decimal point (also known as a radix point, in bases other than
        10). (The error and exponent are always printed in base 10.)

        We define the "precision" of a floating-point printed
        representation to be the positional value of the last digit of the
        mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
        in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
        is `10^{-2}`. This precision will always be `10^k`
        for some `k` (or, for an arbitrary base `b`, `b^k`).

        Then the interval is contained in the interval:

        .. MATH::

            \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
            .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
            b^k

        To control the printing, we can specify a maximum number of error
        digits. The default is 0, which means that we do not print an error
        at all (so that the error is always the default, 1).

        Now, consider the precisions needed to represent the endpoints
        (this is the precision that would be produced by
        ``v.lower().str(no_sci=False)``). Our
        result is no more precise than the less precise endpoint, and is
        sufficiently imprecise that the error can be represented with the
        given number of decimal digits. Our result is the most precise
        possible result, given these restrictions. When there are two
        possible results of equal precision and with the same error width,
        then we pick the one which is farther from zero. (For instance,
        ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
        ``62.?62``. We prefer the latter because it makes it clear that the
        interval is known not to be negative.)

        EXAMPLES::

            sage: a = RIF(59/27); a
            2.185185185185186?
            sage: a.str()
            \'2.185185185185186?\'
            sage: a.str(style=\'brackets\')
            \'[2.1851851851851851 .. 2.1851851851851856]\'
            sage: a.str(16)
            \'2.2f684bda12f69?\'
            sage: a.str(no_sci=False)
            \'2.185185185185186?e0\'
            sage: pi_appr = RIF(pi, 22/7)
            sage: pi_appr.str(style=\'brackets\')
            \'[3.1415926535897931 .. 3.1428571428571433]\'
            sage: pi_appr.str()
            \'3.142?\'
            sage: pi_appr.str(error_digits=1)
            \'3.1422?7\'
            sage: pi_appr.str(error_digits=2)
            \'3.14223?64\'
            sage: pi_appr.str(base=36)
            \'3.6?\'
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]
            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
            [-infinity .. 3.1415926535897936]
            sage: RealIntervalField(210)(3).sqrt()
            1.732050807568877293527446341505872366942805253810380628055806980?
            sage: RealIntervalField(210)(RIF(3).sqrt())
            1.732050807568878?
            sage: RIF(3).sqrt()
            1.732050807568878?
            sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
            1.?e-71

        TESTS:

        Check that :issue:`13634` is fixed::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?'''
    @overload
    def str(self) -> Any:
        '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- base for output

        - ``style`` -- the printing style; either ``\'brackets\'`` or
          ``\'question\'`` (or ``None``, to use the current default)

        - ``no_sci`` -- if ``True`` do not print using scientific
          notation; if ``False`` print with scientific notation; if ``None``
          (the default), print how the parent prints.

        - ``e`` -- symbol used in scientific notation

        - ``error_digits`` -- the number of digits of error to
          print, in ``\'question\'`` style

        We support two different styles of printing; ``\'question\'`` style and
        ``\'brackets\'`` style. In question style (the default), we print the
        "known correct" part of the number, followed by a question mark::

            sage: RIF(pi).str()                                                         # needs sage.symbolic
            \'3.141592653589794?\'
            sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
            \'3.142?\'
            sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
            \'3.142?\'

        However, if the interval is precisely equal to some integer that\'s
        not too large, we just return that integer::

            sage: RIF(-42).str()
            \'-42\'
            sage: RIF(0).str()
            \'0\'
            sage: RIF(12^5).str(base=3)
            \'110122100000\'

        Very large integers, however, revert to the normal question-style
        printing::

            sage: RIF(3^7).str()
            \'2187\'
            sage: RIF(3^7 * 2^256).str()
            \'2.5323729916201052?e80\'

        In brackets style, we print the lower and upper bounds of the
        interval within brackets::

            sage: RIF(237/16).str(style=\'brackets\')
            \'[14.812500000000000 .. 14.812500000000000]\'

        Note that the lower bound is rounded down, and the upper bound is
        rounded up. So even if the lower and upper bounds are equal, they
        may print differently. (This is done so that the printed
        representation of the interval contains all the numbers in the
        internal binary interval.)

        For instance, we find the best 10-bit floating point representation
        of ``1/3``::

            sage: RR10 = RealField(10)
            sage: RR(RR10(1/3))
            0.333496093750000

        And we see that the point interval containing only this
        floating-point number prints as a wider decimal interval, that does
        contain the number::

            sage: RIF10 = RealIntervalField(10)
            sage: RIF10(RR10(1/3)).str(style=\'brackets\')
            \'[0.33349 .. 0.33350]\'

        We always use brackets style for ``NaN`` and infinities::

            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]

        Let\'s take a closer, formal look at the question style. In its full
        generality, a number printed in the question style looks like:

        MANTISSA ?ERROR eEXPONENT

        (without the spaces). The "eEXPONENT" part is optional; if it is
        missing, then the exponent is 0. (If the base is greater than 10,
        then the exponent separator is "@" instead of "e".)

        The "ERROR" is optional; if it is missing, then the error is 1.

        The mantissa is printed in base `b`, and always contains a
        decimal point (also known as a radix point, in bases other than
        10). (The error and exponent are always printed in base 10.)

        We define the "precision" of a floating-point printed
        representation to be the positional value of the last digit of the
        mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
        in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
        is `10^{-2}`. This precision will always be `10^k`
        for some `k` (or, for an arbitrary base `b`, `b^k`).

        Then the interval is contained in the interval:

        .. MATH::

            \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
            .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
            b^k

        To control the printing, we can specify a maximum number of error
        digits. The default is 0, which means that we do not print an error
        at all (so that the error is always the default, 1).

        Now, consider the precisions needed to represent the endpoints
        (this is the precision that would be produced by
        ``v.lower().str(no_sci=False)``). Our
        result is no more precise than the less precise endpoint, and is
        sufficiently imprecise that the error can be represented with the
        given number of decimal digits. Our result is the most precise
        possible result, given these restrictions. When there are two
        possible results of equal precision and with the same error width,
        then we pick the one which is farther from zero. (For instance,
        ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
        ``62.?62``. We prefer the latter because it makes it clear that the
        interval is known not to be negative.)

        EXAMPLES::

            sage: a = RIF(59/27); a
            2.185185185185186?
            sage: a.str()
            \'2.185185185185186?\'
            sage: a.str(style=\'brackets\')
            \'[2.1851851851851851 .. 2.1851851851851856]\'
            sage: a.str(16)
            \'2.2f684bda12f69?\'
            sage: a.str(no_sci=False)
            \'2.185185185185186?e0\'
            sage: pi_appr = RIF(pi, 22/7)
            sage: pi_appr.str(style=\'brackets\')
            \'[3.1415926535897931 .. 3.1428571428571433]\'
            sage: pi_appr.str()
            \'3.142?\'
            sage: pi_appr.str(error_digits=1)
            \'3.1422?7\'
            sage: pi_appr.str(error_digits=2)
            \'3.14223?64\'
            sage: pi_appr.str(base=36)
            \'3.6?\'
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]
            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
            [-infinity .. 3.1415926535897936]
            sage: RealIntervalField(210)(3).sqrt()
            1.732050807568877293527446341505872366942805253810380628055806980?
            sage: RealIntervalField(210)(RIF(3).sqrt())
            1.732050807568878?
            sage: RIF(3).sqrt()
            1.732050807568878?
            sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
            1.?e-71

        TESTS:

        Check that :issue:`13634` is fixed::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?'''
    @overload
    def str(self, style=...) -> Any:
        '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- base for output

        - ``style`` -- the printing style; either ``\'brackets\'`` or
          ``\'question\'`` (or ``None``, to use the current default)

        - ``no_sci`` -- if ``True`` do not print using scientific
          notation; if ``False`` print with scientific notation; if ``None``
          (the default), print how the parent prints.

        - ``e`` -- symbol used in scientific notation

        - ``error_digits`` -- the number of digits of error to
          print, in ``\'question\'`` style

        We support two different styles of printing; ``\'question\'`` style and
        ``\'brackets\'`` style. In question style (the default), we print the
        "known correct" part of the number, followed by a question mark::

            sage: RIF(pi).str()                                                         # needs sage.symbolic
            \'3.141592653589794?\'
            sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
            \'3.142?\'
            sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
            \'3.142?\'

        However, if the interval is precisely equal to some integer that\'s
        not too large, we just return that integer::

            sage: RIF(-42).str()
            \'-42\'
            sage: RIF(0).str()
            \'0\'
            sage: RIF(12^5).str(base=3)
            \'110122100000\'

        Very large integers, however, revert to the normal question-style
        printing::

            sage: RIF(3^7).str()
            \'2187\'
            sage: RIF(3^7 * 2^256).str()
            \'2.5323729916201052?e80\'

        In brackets style, we print the lower and upper bounds of the
        interval within brackets::

            sage: RIF(237/16).str(style=\'brackets\')
            \'[14.812500000000000 .. 14.812500000000000]\'

        Note that the lower bound is rounded down, and the upper bound is
        rounded up. So even if the lower and upper bounds are equal, they
        may print differently. (This is done so that the printed
        representation of the interval contains all the numbers in the
        internal binary interval.)

        For instance, we find the best 10-bit floating point representation
        of ``1/3``::

            sage: RR10 = RealField(10)
            sage: RR(RR10(1/3))
            0.333496093750000

        And we see that the point interval containing only this
        floating-point number prints as a wider decimal interval, that does
        contain the number::

            sage: RIF10 = RealIntervalField(10)
            sage: RIF10(RR10(1/3)).str(style=\'brackets\')
            \'[0.33349 .. 0.33350]\'

        We always use brackets style for ``NaN`` and infinities::

            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]

        Let\'s take a closer, formal look at the question style. In its full
        generality, a number printed in the question style looks like:

        MANTISSA ?ERROR eEXPONENT

        (without the spaces). The "eEXPONENT" part is optional; if it is
        missing, then the exponent is 0. (If the base is greater than 10,
        then the exponent separator is "@" instead of "e".)

        The "ERROR" is optional; if it is missing, then the error is 1.

        The mantissa is printed in base `b`, and always contains a
        decimal point (also known as a radix point, in bases other than
        10). (The error and exponent are always printed in base 10.)

        We define the "precision" of a floating-point printed
        representation to be the positional value of the last digit of the
        mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
        in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
        is `10^{-2}`. This precision will always be `10^k`
        for some `k` (or, for an arbitrary base `b`, `b^k`).

        Then the interval is contained in the interval:

        .. MATH::

            \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
            .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
            b^k

        To control the printing, we can specify a maximum number of error
        digits. The default is 0, which means that we do not print an error
        at all (so that the error is always the default, 1).

        Now, consider the precisions needed to represent the endpoints
        (this is the precision that would be produced by
        ``v.lower().str(no_sci=False)``). Our
        result is no more precise than the less precise endpoint, and is
        sufficiently imprecise that the error can be represented with the
        given number of decimal digits. Our result is the most precise
        possible result, given these restrictions. When there are two
        possible results of equal precision and with the same error width,
        then we pick the one which is farther from zero. (For instance,
        ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
        ``62.?62``. We prefer the latter because it makes it clear that the
        interval is known not to be negative.)

        EXAMPLES::

            sage: a = RIF(59/27); a
            2.185185185185186?
            sage: a.str()
            \'2.185185185185186?\'
            sage: a.str(style=\'brackets\')
            \'[2.1851851851851851 .. 2.1851851851851856]\'
            sage: a.str(16)
            \'2.2f684bda12f69?\'
            sage: a.str(no_sci=False)
            \'2.185185185185186?e0\'
            sage: pi_appr = RIF(pi, 22/7)
            sage: pi_appr.str(style=\'brackets\')
            \'[3.1415926535897931 .. 3.1428571428571433]\'
            sage: pi_appr.str()
            \'3.142?\'
            sage: pi_appr.str(error_digits=1)
            \'3.1422?7\'
            sage: pi_appr.str(error_digits=2)
            \'3.14223?64\'
            sage: pi_appr.str(base=36)
            \'3.6?\'
            sage: RIF(NaN)                                                              # needs sage.symbolic
            [.. NaN ..]
            sage: RIF(pi, infinity)                                                     # needs sage.symbolic
            [3.1415926535897931 .. +infinity]
            sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
            [-infinity .. 3.1415926535897936]
            sage: RealIntervalField(210)(3).sqrt()
            1.732050807568877293527446341505872366942805253810380628055806980?
            sage: RealIntervalField(210)(RIF(3).sqrt())
            1.732050807568878?
            sage: RIF(3).sqrt()
            1.732050807568878?
            sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
            1.?e-71

        TESTS:

        Check that :issue:`13634` is fixed::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?'''
    @overload
    def tan(self) -> Any:
        """RealIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/3
            sage: q.tan()
            1.732050807568877?
            sage: q = RIF.pi()/6
            sage: q.tan()
            0.577350269189626?"""
    @overload
    def tan(self) -> Any:
        """RealIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/3
            sage: q.tan()
            1.732050807568877?
            sage: q = RIF.pi()/6
            sage: q.tan()
            0.577350269189626?"""
    @overload
    def tan(self) -> Any:
        """RealIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/3
            sage: q.tan()
            1.732050807568877?
            sage: q = RIF.pi()/6
            sage: q.tan()
            0.577350269189626?"""
    @overload
    def tanh(self) -> Any:
        """RealIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4822)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/11
            sage: q.tanh()
            0.2780794292958503?"""
    @overload
    def tanh(self) -> Any:
        """RealIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4822)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: q = RIF.pi()/11
            sage: q.tanh()
            0.2780794292958503?"""
    def trunc(self) -> Any:
        """RealIntervalFieldElement.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3134)

        Return the truncation of this interval as an interval.

        The truncation of `x` is the floor of `x` if `x` is nonnegative or the
        ceil of `x` if `x` is negative.

        .. SEEALSO::

            - :meth:`unique_trunc` -- return the trunc as an integer if it is
              unique and raises a :exc:`ValueError` otherwise
            - :meth:`floor` -- truncation towards `-\\infty`
            - :meth:`ceil` -- truncation towards `+\\infty`
            - :meth:`round` -- rounding

        EXAMPLES::

            sage: RIF(2.3, 2.7).trunc()
            2
            sage: parent(_)
            Real Interval Field with 53 bits of precision

            sage: RIF(-0.9, 0.9).trunc()
            0
            sage: RIF(-7.5, -7.3).trunc()
            -7

        In the above example, the obtained interval contains only one element.
        But on the following it is not the case anymore::

            sage: r = RIF(2.99, 3.01).trunc()
            sage: r.upper()
            3.00000000000000
            sage: r.lower()
            2.00000000000000"""
    @overload
    def union(self, other) -> Any:
        """RealIntervalFieldElement.union(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4103)

        Return the union of two intervals, or of an interval and a real
        number (more precisely, the convex hull).

        EXAMPLES::

            sage: RIF(1, 2).union(RIF(pi, 22/7)).str(style='brackets')
            '[1.0000000000000000 .. 3.1428571428571433]'
            sage: RIF(1, 2).union(pi).str(style='brackets')
            '[1.0000000000000000 .. 3.1415926535897936]'
            sage: RIF(1).union(RIF(0, 2)).str(style='brackets')
            '[0.0000000000000000 .. 2.0000000000000000]'
            sage: RIF(1).union(RIF(-1)).str(style='brackets')
            '[-1.0000000000000000 .. 1.0000000000000000]'"""
    @overload
    def union(self, pi) -> Any:
        """RealIntervalFieldElement.union(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4103)

        Return the union of two intervals, or of an interval and a real
        number (more precisely, the convex hull).

        EXAMPLES::

            sage: RIF(1, 2).union(RIF(pi, 22/7)).str(style='brackets')
            '[1.0000000000000000 .. 3.1428571428571433]'
            sage: RIF(1, 2).union(pi).str(style='brackets')
            '[1.0000000000000000 .. 3.1415926535897936]'
            sage: RIF(1).union(RIF(0, 2)).str(style='brackets')
            '[0.0000000000000000 .. 2.0000000000000000]'
            sage: RIF(1).union(RIF(-1)).str(style='brackets')
            '[-1.0000000000000000 .. 1.0000000000000000]'"""
    @overload
    def unique_ceil(self) -> Any:
        """RealIntervalFieldElement.unique_ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

        Return the unique ceiling of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`ceil` -- return the ceil as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
            4
            sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
            315
            sage: RIF(100, 200).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil"""
    @overload
    def unique_ceil(self) -> Any:
        """RealIntervalFieldElement.unique_ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

        Return the unique ceiling of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`ceil` -- return the ceil as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
            4
            sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
            315
            sage: RIF(100, 200).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil"""
    @overload
    def unique_ceil(self) -> Any:
        """RealIntervalFieldElement.unique_ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

        Return the unique ceiling of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`ceil` -- return the ceil as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
            4
            sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
            315
            sage: RIF(100, 200).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil"""
    @overload
    def unique_ceil(self) -> Any:
        """RealIntervalFieldElement.unique_ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

        Return the unique ceiling of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`ceil` -- return the ceil as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
            4
            sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
            315
            sage: RIF(100, 200).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil"""
    @overload
    def unique_floor(self) -> Any:
        """RealIntervalFieldElement.unique_floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

        Return the unique floor of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`floor` -- return the floor as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
            3
            sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
            314
            sage: RIF(100, 200).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor"""
    @overload
    def unique_floor(self) -> Any:
        """RealIntervalFieldElement.unique_floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

        Return the unique floor of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`floor` -- return the floor as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
            3
            sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
            314
            sage: RIF(100, 200).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor"""
    @overload
    def unique_floor(self) -> Any:
        """RealIntervalFieldElement.unique_floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

        Return the unique floor of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`floor` -- return the floor as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
            3
            sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
            314
            sage: RIF(100, 200).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor"""
    @overload
    def unique_floor(self) -> Any:
        """RealIntervalFieldElement.unique_floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

        Return the unique floor of this interval, if it is well defined,
        otherwise raise a :exc:`ValueError`.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`floor` -- return the floor as an interval (and never raise
            error)

        EXAMPLES::

            sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
            3
            sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
            314
            sage: RIF(100, 200).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor"""
    @overload
    def unique_integer(self) -> Any:
        """RealIntervalFieldElement.unique_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

        Return the unique integer in this interval, if there is exactly one,
        otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains no integer
            sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
            4
            sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains more than one integer
            sage: RIF(100).unique_integer()
            100"""
    @overload
    def unique_integer(self) -> Any:
        """RealIntervalFieldElement.unique_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

        Return the unique integer in this interval, if there is exactly one,
        otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains no integer
            sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
            4
            sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains more than one integer
            sage: RIF(100).unique_integer()
            100"""
    @overload
    def unique_integer(self) -> Any:
        """RealIntervalFieldElement.unique_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

        Return the unique integer in this interval, if there is exactly one,
        otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains no integer
            sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
            4
            sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains more than one integer
            sage: RIF(100).unique_integer()
            100"""
    @overload
    def unique_integer(self) -> Any:
        """RealIntervalFieldElement.unique_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

        Return the unique integer in this interval, if there is exactly one,
        otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains no integer
            sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
            4
            sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains more than one integer
            sage: RIF(100).unique_integer()
            100"""
    @overload
    def unique_integer(self) -> Any:
        """RealIntervalFieldElement.unique_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

        Return the unique integer in this interval, if there is exactly one,
        otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains no integer
            sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
            4
            sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: interval contains more than one integer
            sage: RIF(100).unique_integer()
            100"""
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_round(self) -> Any:
        """RealIntervalFieldElement.unique_round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

         Return the unique round (nearest integer) of this interval,
         if it is well defined, otherwise raise a :exc:`ValueError`.

         OUTPUT: integer

         .. SEEALSO::

             :meth:`round` -- return the round as an interval (and never raise
             error)

         EXAMPLES::

             sage: RIF(pi).unique_round()                                                # needs sage.symbolic
             3
             sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
             3142
             sage: RIF(100, 200).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1.2, 1.7).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(0.7, 1.2).unique_round()
             1
             sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
             -3
             sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
             (5, -5)

        TESTS::

             sage: RIF(-1/2, -1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/2, 1/3).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(-1/3, 1/3).unique_round()
             0
             sage: RIF(-1/2, 0).unique_round()
             Traceback (most recent call last):
             ...
             ValueError: interval does not have a unique round (nearest integer)
             sage: RIF(1/2).unique_round()
             1
             sage: RIF(-1/2).unique_round()
             -1
             sage: RIF(0).unique_round()
             0
 """
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_sign(self) -> Any:
        """RealIntervalFieldElement.unique_sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

        Return the sign of this element if it is well defined.

        This method returns `+1` if all elements in this interval are positive,
        `-1` if all of them are negative and `0` if it contains only zero.
        Otherwise it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: RIF(1.2,5.7).unique_sign()
            1
            sage: RIF(-3,-2).unique_sign()
            -1
            sage: RIF(0).unique_sign()
            0
            sage: RIF(0,1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-1,0).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign
            sage: RIF(-0.1, 0.1).unique_sign()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique sign"""
    @overload
    def unique_trunc(self) -> Any:
        """RealIntervalFieldElement.unique_trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

        Return the nearest integer toward zero if it is unique, otherwise raise
        a :exc:`ValueError`.

        .. SEEALSO::

            :meth:`trunc` -- return the truncation as an interval (and never
            raise error)

        EXAMPLES::

            sage: RIF(1.3,1.4).unique_trunc()
            1
            sage: RIF(-3.3, -3.2).unique_trunc()
            -3
            sage: RIF(2.9,3.2).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)
            sage: RIF(-3.1,-2.9).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
    @overload
    def unique_trunc(self) -> Any:
        """RealIntervalFieldElement.unique_trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

        Return the nearest integer toward zero if it is unique, otherwise raise
        a :exc:`ValueError`.

        .. SEEALSO::

            :meth:`trunc` -- return the truncation as an interval (and never
            raise error)

        EXAMPLES::

            sage: RIF(1.3,1.4).unique_trunc()
            1
            sage: RIF(-3.3, -3.2).unique_trunc()
            -3
            sage: RIF(2.9,3.2).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)
            sage: RIF(-3.1,-2.9).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
    @overload
    def unique_trunc(self) -> Any:
        """RealIntervalFieldElement.unique_trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

        Return the nearest integer toward zero if it is unique, otherwise raise
        a :exc:`ValueError`.

        .. SEEALSO::

            :meth:`trunc` -- return the truncation as an interval (and never
            raise error)

        EXAMPLES::

            sage: RIF(1.3,1.4).unique_trunc()
            1
            sage: RIF(-3.3, -3.2).unique_trunc()
            -3
            sage: RIF(2.9,3.2).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)
            sage: RIF(-3.1,-2.9).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
    @overload
    def unique_trunc(self) -> Any:
        """RealIntervalFieldElement.unique_trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

        Return the nearest integer toward zero if it is unique, otherwise raise
        a :exc:`ValueError`.

        .. SEEALSO::

            :meth:`trunc` -- return the truncation as an interval (and never
            raise error)

        EXAMPLES::

            sage: RIF(1.3,1.4).unique_trunc()
            1
            sage: RIF(-3.3, -3.2).unique_trunc()
            -3
            sage: RIF(2.9,3.2).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)
            sage: RIF(-3.1,-2.9).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
    @overload
    def unique_trunc(self) -> Any:
        """RealIntervalFieldElement.unique_trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

        Return the nearest integer toward zero if it is unique, otherwise raise
        a :exc:`ValueError`.

        .. SEEALSO::

            :meth:`trunc` -- return the truncation as an interval (and never
            raise error)

        EXAMPLES::

            sage: RIF(1.3,1.4).unique_trunc()
            1
            sage: RIF(-3.3, -3.2).unique_trunc()
            -3
            sage: RIF(2.9,3.2).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)
            sage: RIF(-3.1,-2.9).unique_trunc()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
    @overload
    def upper(self, rnd=...) -> Any:
        """RealIntervalFieldElement.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

        Return the upper bound of ``self``.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards plus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().upper().str()
            '3.1417'

        ::

            sage: R = RealIntervalField(13)
            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.upper()
            1.31
            sage: x.upper('RNDU')
            1.31
            sage: x.upper('RNDN')
            1.30
            sage: x.upper('RNDD')
            1.30
            sage: x.upper('RNDZ')
            1.30
            sage: x.upper('RNDA')
            1.31
            sage: x.upper().parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.upper('RNDD').parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.upper() == x.upper('RNDD')
            True"""
    @overload
    def upper(self) -> Any:
        """RealIntervalFieldElement.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

        Return the upper bound of ``self``.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards plus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().upper().str()
            '3.1417'

        ::

            sage: R = RealIntervalField(13)
            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.upper()
            1.31
            sage: x.upper('RNDU')
            1.31
            sage: x.upper('RNDN')
            1.30
            sage: x.upper('RNDD')
            1.30
            sage: x.upper('RNDZ')
            1.30
            sage: x.upper('RNDA')
            1.31
            sage: x.upper().parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.upper('RNDD').parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.upper() == x.upper('RNDD')
            True"""
    @overload
    def upper(self) -> Any:
        """RealIntervalFieldElement.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

        Return the upper bound of ``self``.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards plus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().upper().str()
            '3.1417'

        ::

            sage: R = RealIntervalField(13)
            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.upper()
            1.31
            sage: x.upper('RNDU')
            1.31
            sage: x.upper('RNDN')
            1.30
            sage: x.upper('RNDD')
            1.30
            sage: x.upper('RNDZ')
            1.30
            sage: x.upper('RNDA')
            1.31
            sage: x.upper().parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.upper('RNDD').parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.upper() == x.upper('RNDD')
            True"""
    @overload
    def upper(self) -> Any:
        """RealIntervalFieldElement.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

        Return the upper bound of ``self``.

        INPUT:

        - ``rnd`` -- the rounding mode (default: towards plus infinity,
          see :class:`sage.rings.real_mpfr.RealField` for possible values)

        The rounding mode does not affect the value returned as a
        floating-point number, but it does control which variety of
        ``RealField`` the returned number is in, which affects printing and
        subsequent operations.

        EXAMPLES::

            sage: R = RealIntervalField(13)
            sage: R.pi().upper().str()
            '3.1417'

        ::

            sage: R = RealIntervalField(13)
            sage: x = R(1.2,1.3); x.str(style='brackets')
            '[1.1999 .. 1.3001]'
            sage: x.upper()
            1.31
            sage: x.upper('RNDU')
            1.31
            sage: x.upper('RNDN')
            1.30
            sage: x.upper('RNDD')
            1.30
            sage: x.upper('RNDZ')
            1.30
            sage: x.upper('RNDA')
            1.31
            sage: x.upper().parent()
            Real Field with 13 bits of precision and rounding RNDU
            sage: x.upper('RNDD').parent()
            Real Field with 13 bits of precision and rounding RNDD
            sage: x.upper() == x.upper('RNDD')
            True"""
    def zeta(self, a=...) -> Any:
        """RealIntervalFieldElement.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5172)

        Return the image of this interval by the Hurwitz zeta function.

        For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

        EXAMPLES::

            sage: zeta(RIF(3))
            1.202056903159594?
            sage: _.parent()
            Real Interval Field with 53 bits of precision
            sage: RIF(3).zeta(1/2)
            8.41439832211716?"""
    @overload
    def __abs__(self) -> Any:
        """RealIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RIF(2).__abs__()
            2
            sage: RIF(2.1).__abs__()
            2.1000000000000001?
            sage: RIF(-2.1).__abs__()
            2.1000000000000001?"""
    @overload
    def __abs__(self) -> Any:
        """RealIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RIF(2).__abs__()
            2
            sage: RIF(2.1).__abs__()
            2.1000000000000001?
            sage: RIF(-2.1).__abs__()
            2.1000000000000001?"""
    @overload
    def __abs__(self) -> Any:
        """RealIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RIF(2).__abs__()
            2
            sage: RIF(2.1).__abs__()
            2.1000000000000001?
            sage: RIF(-2.1).__abs__()
            2.1000000000000001?"""
    @overload
    def __abs__(self) -> Any:
        """RealIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RIF(2).__abs__()
            2
            sage: RIF(2.1).__abs__()
            2.1000000000000001?
            sage: RIF(-2.1).__abs__()
            2.1000000000000001?"""
    def __add__(self, left, right) -> Any:
        """RealIntervalFieldElement.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2613)

        TESTS::

            sage: RIF(1) + RR(1)
            doctest:...:
            DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
            See https://github.com/sagemath/sage/issues/15114 for details.
            2
            sage: import warnings; warnings.resetwarnings()"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __complex__(self) -> Any:
        """RealIntervalFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3305)

        Convert ``self`` to a ``complex``.

        EXAMPLES::

            sage: complex(RIF(1))
            (1+0j)"""
    def __contains__(self, other) -> Any:
        """RealIntervalFieldElement.__contains__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3998)

        Test whether one interval (or real number) is totally contained in
        another.

        EXAMPLES::

            sage: RIF(0, 2) in RIF(1, 3)
            False
            sage: RIF(0, 2) in RIF(0, 2)
            True
            sage: RIF(1, 2) in RIF(0, 3)
            True
            sage: 1.0 in RIF(0, 2)
            True
            sage: pi in RIF(3.1415, 3.1416)                                             # needs sage.symbolic
            True
            sage: 22/7 in RIF(3.1415, 3.1416)
            False"""
    def __copy__(self) -> Any:
        """RealIntervalFieldElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2200)

        Return copy of ``self``.

        Since ``self`` is immutable, we just return ``self`` again.

        EXAMPLES::

            sage: a = RIF(3.5)
            sage: copy(a) is  a
            True"""
    def __deepcopy__(self, memo) -> Any:
        """RealIntervalFieldElement.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2214)

        EXAMPLES::

            sage: a = RIF(3.5)
            sage: deepcopy(a) is  a
            True"""
    def __float__(self) -> Any:
        """RealIntervalFieldElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3294)

        Convert ``self`` to a ``float``.

        EXAMPLES::

            sage: float(RIF(1))
            1.0"""
    def __hash__(self) -> Any:
        """RealIntervalFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1433)

        Return a hash value of ``self``.

        EXAMPLES::

            sage: hash(RIF(e)) == hash(RIF(e))  # indirect doctest                      # needs sage.symbolic
            True"""
    def __invert__(self) -> Any:
        '''RealIntervalFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2732)

        Return the multiplicative "inverse" of this interval. (Technically,
        non-precise intervals don\'t have multiplicative inverses.)

        EXAMPLES::

            sage: v = RIF(2); v
            2
            sage: ~v
            0.50000000000000000?
            sage: v * ~v
            1
            sage: v = RIF(1.5, 2.5); v.str(style=\'brackets\')
            \'[1.5000000000000000 .. 2.5000000000000000]\'
            sage: (~v).str(style=\'brackets\')
            \'[0.39999999999999996 .. 0.66666666666666675]\'
            sage: (v * ~v).str(style=\'brackets\')
            \'[0.59999999999999986 .. 1.6666666666666670]\'
            sage: ~RIF(-1, 1)
            [-infinity .. +infinity]'''
    def __lshift__(self, x, y) -> Any:
        """RealIntervalFieldElement.__lshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2935)

        Return `x * 2^y`, for `y` an integer. Much faster
        than an ordinary multiplication.

        EXAMPLES::

            sage: RIF(1.0) << 32
            4294967296"""
    def __mul__(self, left, right) -> Any:
        """RealIntervalFieldElement.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2661)

        TESTS::

            sage: RIF(1) * RR(1)
            doctest:...:
            DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
            See https://github.com/sagemath/sage/issues/15114 for details.
            1
            sage: import warnings; warnings.resetwarnings()"""
    def __pow__(self, exponent, modulus) -> Any:
        """RealIntervalFieldElement.__pow__(self, exponent, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4422)

        Raise ``self`` to ``exponent``.

        EXAMPLES::

            sage: R = RealIntervalField(17)
            sage: x = R((-e, pi))                                                       # needs sage.symbolic
            sage: x2 = x^2; x2.lower(), x2.upper()                                      # needs sage.symbolic
            (0.0000, 9.870)
            sage: x3 = x^3; x3.lower(), x3.upper()                                      # needs sage.symbolic
            (-26.83, 31.01)"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """RealIntervalFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1275)

        Pickling support.

        EXAMPLES::

            sage: a = RIF(5,5.5)
            sage: loads(dumps(a)).lexico_cmp(a)
            0
            sage: R = RealIntervalField(sci_not=1, prec=200)
            sage: b = R('393.39203845902384098234098230948209384028340')
            sage: loads(dumps(b)).lexico_cmp(b)
            0
            sage: b = R(1)/R(0); b # R(0) has no particular sign, thus 1/R(0) covers the whole reals
            [-infinity .. +infinity]
            sage: c = loads(dumps(b))
            sage: (c.lower(), c.upper()) == (b.lower(), b.upper())
            True
            sage: b = R(-1)/R(0); b # same as above
            [-infinity .. +infinity]
            sage: c = loads(dumps(b))
            sage: (c.lower(), c.upper()) == (b.lower(), b.upper())
            True
            sage: b = R('[2 .. 3]'); b.str(error_digits=1)
            '2.5?5e0'
            sage: loads(dumps(b)).lexico_cmp(b)
            0
            sage: R = RealIntervalField(4000)
            sage: s = 1/R(3)
            sage: t = loads(dumps(s))
            sage: (t.upper(), t.lower()) == (s.upper(), s.lower())
            True
            sage: loads(dumps(1/RIF(0,1)))
            [1.0000000000000000 .. +infinity]"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, x, y) -> Any:
        """RealIntervalFieldElement.__rshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2966)

        Return `x / 2^y`, for `y` an integer.

        Much faster than an ordinary division.

        EXAMPLES::

            sage: RIF(1024.0) >> 14
            0.062500000000000000?"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, left, right) -> Any:
        """RealIntervalFieldElement.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2637)

        TESTS::

            sage: RIF(2) - RR(1)
            doctest:...:
            DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
            See https://github.com/sagemath/sage/issues/15114 for details.
            1
            sage: import warnings; warnings.resetwarnings()"""
    def __truediv__(self, left, right) -> Any:
        """RealIntervalFieldElement.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2685)

        TESTS::

            sage: RIF(1) / RR(1/2)
            doctest:...:
            DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
            See https://github.com/sagemath/sage/issues/15114 for details.
            2
            sage: import warnings; warnings.resetwarnings()"""

class RealIntervalField_class(sage.rings.abc.RealIntervalField):
    '''RealIntervalField_class(mpfr_prec_t prec=53, int sci_not=0)

    File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 369)

    Class of the real interval field.

    INPUT:

    - ``prec`` -- integer (default: 53); precision ``prec`` is
      the number of bits used to represent the mantissa of a
      floating-point number. The precision can be any integer between
      :func:`~sage.rings.real_mpfr.mpfr_prec_min()` and
      :func:`~sage.rings.real_mpfr.mpfr_prec_max()`. In the current
      implementation, :func:`~sage.rings.real_mpfr.mpfr_prec_min()`
      is equal to 2.

    - ``sci_not`` -- boolean (default: ``False``); whether or not to display using
      scientific notation

    EXAMPLES::

        sage: RealIntervalField(10)
        Real Interval Field with 10 bits of precision
        sage: RealIntervalField()
        Real Interval Field with 53 bits of precision
        sage: RealIntervalField(100000)
        Real Interval Field with 100000 bits of precision

    .. NOTE::

       The default precision is 53, since according to the GMP manual:
       \'mpfr should be able to exactly reproduce all computations with
       double-precision machine floating-point numbers (double type in
       C), except the default exponent range is much wider and
       subnormal numbers are not implemented.\'

    EXAMPLES:

    Creation of elements.

    First with default precision. First we coerce elements of various
    types, then we coerce intervals::

        sage: RIF = RealIntervalField(); RIF
        Real Interval Field with 53 bits of precision
        sage: RIF(3)
        3
        sage: RIF(RIF(3))
        3
        sage: RIF(pi)                                                                   # needs sage.symbolic
        3.141592653589794?
        sage: RIF(RealField(53)(\'1.5\'))
        1.5000000000000000?
        sage: RIF(-2/19)
        -0.1052631578947369?
        sage: RIF(-3939)
        -3939
        sage: RIF(-3939r)
        -3939
        sage: RIF(\'1.5\')
        1.5000000000000000?
        sage: R200 = RealField(200)
        sage: RIF(R200.pi())
        3.141592653589794?
        sage: RIF(10^100)
        1.000000000000000?e100

    The base must be explicitly specified as a named parameter::

        sage: RIF(\'101101\', base=2)
        45
        sage: RIF(\'+infinity\')
        [+infinity .. +infinity]
        sage: RIF(\'[1..3]\').str(style=\'brackets\')
        \'[1.0000000000000000 .. 3.0000000000000000]\'

    All string-like types are accepted::

        sage: RIF(b"100", u"100")
        100

    Next we coerce some 2-tuples, which define intervals::

        sage: RIF((-1.5, -1.3))
        -1.4?
        sage: RIF((RDF(\'-1.5\'), RDF(\'-1.3\')))
        -1.4?
        sage: RIF((1/3,2/3)).str(style=\'brackets\')
        \'[0.33333333333333331 .. 0.66666666666666675]\'

    The extra parentheses aren\'t needed::

        sage: RIF(1/3,2/3).str(style=\'brackets\')
        \'[0.33333333333333331 .. 0.66666666666666675]\'
        sage: RIF((1,2)).str(style=\'brackets\')
        \'[1.0000000000000000 .. 2.0000000000000000]\'
        sage: RIF((1r,2r)).str(style=\'brackets\')
        \'[1.0000000000000000 .. 2.0000000000000000]\'
        sage: RIF((pi, e)).str(style=\'brackets\')
        \'[2.7182818284590450 .. 3.1415926535897936]\'

    Values which can be represented as an exact floating-point number
    (of the precision of this ``RealIntervalField``) result in a precise
    interval, where the lower bound is equal to the upper bound (even
    if they print differently). Other values typically result in an
    interval where the lower and upper bounds are adjacent
    floating-point numbers.

    ::

        sage: def check(x):
        ....:     return (x, x.lower() == x.upper())
        sage: check(RIF(pi))                                                            # needs sage.symbolic
        (3.141592653589794?, False)
        sage: check(RIF(RR(pi)))                                                        # needs sage.symbolic
        (3.1415926535897932?, True)
        sage: check(RIF(1.5))
        (1.5000000000000000?, True)
        sage: check(RIF(\'1.5\'))
        (1.5000000000000000?, True)
        sage: check(RIF(0.1))
        (0.10000000000000001?, True)
        sage: check(RIF(1/10))
        (0.10000000000000000?, False)
        sage: check(RIF(\'0.1\'))
        (0.10000000000000000?, False)

    Similarly, when specifying both ends of an interval, the lower end
    is rounded down and the upper end is rounded up::

        sage: outward = RIF(1/10, 7/10); outward.str(style=\'brackets\')
        \'[0.099999999999999991 .. 0.70000000000000007]\'
        sage: nearest = RIF(RR(1/10), RR(7/10)); nearest.str(style=\'brackets\')
        \'[0.10000000000000000 .. 0.69999999999999996]\'
        sage: nearest.lower() - outward.lower()
        1.38777878078144e-17
        sage: outward.upper() - nearest.upper()
        1.11022302462516e-16

    Some examples with a real interval field of higher precision::

        sage: R = RealIntervalField(100)
        sage: R(3)
        3
        sage: R(R(3))
        3
        sage: R(pi)                                                                     # needs sage.symbolic
        3.14159265358979323846264338328?
        sage: R(-2/19)
        -0.1052631578947368421052631578948?
        sage: R(e,pi).str(style=\'brackets\')                                             # needs sage.symbolic
        \'[2.7182818284590452353602874713512 .. 3.1415926535897932384626433832825]\'

    TESTS::

        sage: RIF(0, 10^200)
        1.?e200
        sage: RIF(10^100, 10^200)
        1.?e200
        sage: RIF.lower_field() is RealField(53, rnd=\'RNDD\')
        True
        sage: RIF.upper_field() is RealField(53, rnd=\'RNDU\')
        True
        sage: RIF.middle_field() is RR
        True
        sage: TestSuite(RIF).run()

        sage: RealIntervalField(10).is_finite()
        False

    .. SEEALSO::

        - :mod:`sage.rings.real_mpfi`
        - :mod:`sage.rings.complex_interval_field`
        - :class:`sage.rings.real_arb.RealBallField` (alternative
          implementation of real intervals, with more features)'''

    class Element(sage.structure.element.RingElement):
        """RealIntervalFieldElement(parent, x, int base=10)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1191)

        A real number interval."""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1222)

                    Initialize a real interval element. Should be called by first
                    creating a :class:`RealIntervalField`, as illustrated in the
                    examples.

                    INPUT:

                    - ``x`` -- a number, string, or 2-tuple

                    - ``base`` -- integer (default: 10); only used if ``x`` is a string

                    EXAMPLES::

                        sage: R = RealIntervalField()
                        sage: R('1.2456')
                        1.245600000000000?
                        sage: R = RealIntervalField(3)
                        sage: R('1.2456').str(style='brackets')
                        '[1.0 .. 1.3]'

                    ::

                        sage: RIF = RealIntervalField(53)
                        sage: RIF(RR.pi())
                        3.1415926535897932?
                        sage: RIF(RDF.pi())
                        3.1415926535897932?
                        sage: RIF(math.pi)
                        3.1415926535897932?
                        sage: RIF.pi()
                        3.141592653589794?

                    Rounding::

                        sage: w = RealIntervalField(3)(5/2)
                        sage: RealIntervalField(2)(w).str(2, style='brackets')
                        '[10. .. 11.]'

                    TESTS::

                        sage: a = RealIntervalField(428)(factorial(100)/exp(2)); a
                        1.26303298005073195998439505058085204028142920134742241494671502106333548593576383141666758300089860337889002385197008191910406895?e157
                        sage: a.diameter()
                        4.7046373946079775711568954992429894854882556641460240333441655212438503516287848720594584761250430179569094634219773739322602945e-129

                    Type: ``RealIntervalField?`` for many more examples.
        """
        @overload
        def absolute_diameter(self) -> Any:
            """RealIntervalFieldElement.absolute_diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2389)

            The diameter of this interval (for `[a .. b]`, this is `b-a`), rounded
            upward, as a :class:`RealNumber`.

            EXAMPLES::

                sage: RIF(1, pi).absolute_diameter()                                        # needs sage.symbolic
                2.14159265358979"""
        @overload
        def absolute_diameter(self) -> Any:
            """RealIntervalFieldElement.absolute_diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2389)

            The diameter of this interval (for `[a .. b]`, this is `b-a`), rounded
            upward, as a :class:`RealNumber`.

            EXAMPLES::

                sage: RIF(1, pi).absolute_diameter()                                        # needs sage.symbolic
                2.14159265358979"""
        @overload
        def alea(self) -> Any:
            """RealIntervalFieldElement.alea(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2595)

            Return a floating-point number picked at random from the interval.

            EXAMPLES::

                sage: RIF(1, 2).alea() # random
                1.34696133696137"""
        @overload
        def alea(self) -> Any:
            """RealIntervalFieldElement.alea(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2595)

            Return a floating-point number picked at random from the interval.

            EXAMPLES::

                sage: RIF(1, 2).alea() # random
                1.34696133696137"""
        def algdep(self, *args, **kwargs):
            '''RealIntervalFieldElement.algebraic_dependency(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4999)

            Return a polynomial of degree at most `n` which is
            approximately satisfied by ``self``.

            .. NOTE::

                The returned polynomial need not be irreducible, and indeed usually
                won\'t be if ``self`` is a good approximation to an algebraic number
                of degree less than `n`.

            Pari needs to know the number of "known good bits" in the number;
            we automatically get that from the interval width.

            ALGORITHM:

            This uses the PARI C-library :pari:`algdep` command.

            EXAMPLES::

                sage: r = sqrt(RIF(2)); r
                1.414213562373095?
                sage: r.algebraic_dependency(5)
                x^2 - 2

            If we compute a wrong, but precise, interval, we get a wrong
            answer::

                sage: r = sqrt(RealIntervalField(200)(2)) + (1/2)^40; r
                1.414213562374004543503461652447613117632171875376948073176680?
                sage: r.algebraic_dependency(5)
                7266488*x^5 + 22441629*x^4 - 90470501*x^3 + 23297703*x^2 + 45778664*x + 13681026

            But if we compute an interval that includes the number we mean,
            we\'re much more likely to get the right answer, even if the
            interval is very imprecise::

                sage: r = r.union(sqrt(2.0))
                sage: r.algebraic_dependency(5)
                x^2 - 2

            Even on this extremely imprecise interval we get an answer which is
            technically correct::

                sage: RIF(-1, 1).algebraic_dependency(5)
                x'''
        def algebraic_dependency(self, n) -> Any:
            '''RealIntervalFieldElement.algebraic_dependency(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4999)

            Return a polynomial of degree at most `n` which is
            approximately satisfied by ``self``.

            .. NOTE::

                The returned polynomial need not be irreducible, and indeed usually
                won\'t be if ``self`` is a good approximation to an algebraic number
                of degree less than `n`.

            Pari needs to know the number of "known good bits" in the number;
            we automatically get that from the interval width.

            ALGORITHM:

            This uses the PARI C-library :pari:`algdep` command.

            EXAMPLES::

                sage: r = sqrt(RIF(2)); r
                1.414213562373095?
                sage: r.algebraic_dependency(5)
                x^2 - 2

            If we compute a wrong, but precise, interval, we get a wrong
            answer::

                sage: r = sqrt(RealIntervalField(200)(2)) + (1/2)^40; r
                1.414213562374004543503461652447613117632171875376948073176680?
                sage: r.algebraic_dependency(5)
                7266488*x^5 + 22441629*x^4 - 90470501*x^3 + 23297703*x^2 + 45778664*x + 13681026

            But if we compute an interval that includes the number we mean,
            we\'re much more likely to get the right answer, even if the
            interval is very imprecise::

                sage: r = r.union(sqrt(2.0))
                sage: r.algebraic_dependency(5)
                x^2 - 2

            Even on this extremely imprecise interval we get an answer which is
            technically correct::

                sage: RIF(-1, 1).algebraic_dependency(5)
                x'''
        @overload
        def arccos(self) -> Any:
            """RealIntervalFieldElement.arccos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4703)

            Return the inverse cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/3; q
                1.047197551196598?
                sage: i = q.cos(); i
                0.500000000000000?
                sage: q2 = i.arccos(); q2
                1.047197551196598?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arccos(self) -> Any:
            """RealIntervalFieldElement.arccos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4703)

            Return the inverse cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/3; q
                1.047197551196598?
                sage: i = q.cos(); i
                0.500000000000000?
                sage: q2 = i.arccos(); q2
                1.047197551196598?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arccosh(self) -> Any:
            """RealIntervalFieldElement.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4838)

            Return the hyperbolic inverse cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/2
                sage: i = q.arccosh() ; i
                1.023227478547551?"""
        @overload
        def arccosh(self) -> Any:
            """RealIntervalFieldElement.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4838)

            Return the hyperbolic inverse cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/2
                sage: i = q.arccosh() ; i
                1.023227478547551?"""
        @overload
        def arccoth(self) -> Any:
            """RealIntervalFieldElement.arccoth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

            Return the inverse hyperbolic cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccoth()
                0.549306144334054845697622618462?
                sage: (2.0).arccoth()
                0.549306144334055"""
        @overload
        def arccoth(self) -> Any:
            """RealIntervalFieldElement.arccoth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

            Return the inverse hyperbolic cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccoth()
                0.549306144334054845697622618462?
                sage: (2.0).arccoth()
                0.549306144334055"""
        @overload
        def arccoth(self) -> Any:
            """RealIntervalFieldElement.arccoth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4986)

            Return the inverse hyperbolic cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccoth()
                0.549306144334054845697622618462?
                sage: (2.0).arccoth()
                0.549306144334055"""
        @overload
        def arccsch(self) -> Any:
            """RealIntervalFieldElement.arccsch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

            Return the inverse hyperbolic cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccsch()
                0.481211825059603447497758913425?
                sage: (2.0).arccsch()
                0.481211825059603"""
        @overload
        def arccsch(self) -> Any:
            """RealIntervalFieldElement.arccsch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

            Return the inverse hyperbolic cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccsch()
                0.481211825059603447497758913425?
                sage: (2.0).arccsch()
                0.481211825059603"""
        @overload
        def arccsch(self) -> Any:
            """RealIntervalFieldElement.arccsch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4973)

            Return the inverse hyperbolic cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).arccsch()
                0.481211825059603447497758913425?
                sage: (2.0).arccsch()
                0.481211825059603"""
        @overload
        def arcsech(self) -> Any:
            """RealIntervalFieldElement.arcsech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

            Return the inverse hyperbolic secant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(0.5).arcsech()
                1.316957896924816708625046347308?
                sage: (0.5).arcsech()
                1.31695789692482"""
        @overload
        def arcsech(self) -> Any:
            """RealIntervalFieldElement.arcsech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

            Return the inverse hyperbolic secant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(0.5).arcsech()
                1.316957896924816708625046347308?
                sage: (0.5).arcsech()
                1.31695789692482"""
        @overload
        def arcsech(self) -> Any:
            """RealIntervalFieldElement.arcsech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4960)

            Return the inverse hyperbolic secant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(0.5).arcsech()
                1.316957896924816708625046347308?
                sage: (0.5).arcsech()
                1.31695789692482"""
        @overload
        def arcsin(self) -> Any:
            """RealIntervalFieldElement.arcsin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4732)

            Return the inverse sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/5; q
                0.6283185307179587?
                sage: i = q.sin(); i
                0.587785252292474?
                sage: q2 = i.arcsin(); q2
                0.628318530717959?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arcsin(self) -> Any:
            """RealIntervalFieldElement.arcsin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4732)

            Return the inverse sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/5; q
                0.6283185307179587?
                sage: i = q.sin(); i
                0.587785252292474?
                sage: q2 = i.arcsin(); q2
                0.628318530717959?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arcsinh(self) -> Any:
            """RealIntervalFieldElement.arcsinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4854)

            Return the hyperbolic inverse sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/7
                sage: i = q.sinh() ; i
                0.464017630492991?
                sage: i.arcsinh() - q
                0.?e-15"""
        @overload
        def arcsinh(self) -> Any:
            """RealIntervalFieldElement.arcsinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4854)

            Return the hyperbolic inverse sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/7
                sage: i = q.sinh() ; i
                0.464017630492991?
                sage: i.arcsinh() - q
                0.?e-15"""
        @overload
        def arctan(self) -> Any:
            """RealIntervalFieldElement.arctan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4761)

            Return the inverse tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/5; q
                0.6283185307179587?
                sage: i = q.tan(); i
                0.726542528005361?
                sage: q2 = i.arctan(); q2
                0.628318530717959?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arctan(self) -> Any:
            """RealIntervalFieldElement.arctan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4761)

            Return the inverse tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/5; q
                0.6283185307179587?
                sage: i = q.tan(); i
                0.726542528005361?
                sage: q2 = i.arctan(); q2
                0.628318530717959?
                sage: q == q2
                False
                sage: q != q2
                False
                sage: q2.lower() == q.lower()
                False
                sage: q - q2
                0.?e-15
                sage: q in q2
                True"""
        @overload
        def arctanh(self) -> Any:
            """RealIntervalFieldElement.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4872)

            Return the hyperbolic inverse tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/7
                sage: i = q.tanh() ; i
                0.420911241048535?
                sage: i.arctanh() - q
                0.?e-15"""
        @overload
        def arctanh(self) -> Any:
            """RealIntervalFieldElement.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4872)

            Return the hyperbolic inverse tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/7
                sage: i = q.tanh() ; i
                0.420911241048535?
                sage: i.arctanh() - q
                0.?e-15"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def argument(self) -> Any:
            """RealIntervalFieldElement.argument(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3354)

            The argument of this interval, if it is well-defined, in the
            complex sense. Otherwise raises a :exc:`ValueError`.

            OUTPUT:

            - an element of the parent of this interval (0 or pi)

            EXAMPLES::

                sage: RIF(1).argument()
                0
                sage: RIF(-1).argument()
                3.141592653589794?
                sage: RIF(0,1).argument()
                0
                sage: RIF(-1,0).argument()
                3.141592653589794?
                sage: RIF(0).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of an exact zero
                sage: RIF(-1,1).argument()
                Traceback (most recent call last):
                ...
                ValueError: Can't take the argument of interval strictly containing zero"""
        @overload
        def bisection(self) -> Any:
            """RealIntervalFieldElement.bisection(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

            Return the bisection of ``self`` into two intervals of half the size
            whose union is ``self`` and intersection is :meth:`center()`.

            EXAMPLES::

                sage: a, b = RIF(1,2).bisection()
                sage: a.lower(), a.upper()
                (1.00000000000000, 1.50000000000000)
                sage: b.lower(), b.upper()
                (1.50000000000000, 2.00000000000000)

                sage: # needs sage.symbolic
                sage: I = RIF(e, pi)
                sage: a, b = I.bisection()
                sage: a.intersection(b) == RIF(I.center())
                True
                sage: a.union(b).endpoints() == I.endpoints()
                True"""
        @overload
        def bisection(self) -> Any:
            """RealIntervalFieldElement.bisection(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

            Return the bisection of ``self`` into two intervals of half the size
            whose union is ``self`` and intersection is :meth:`center()`.

            EXAMPLES::

                sage: a, b = RIF(1,2).bisection()
                sage: a.lower(), a.upper()
                (1.00000000000000, 1.50000000000000)
                sage: b.lower(), b.upper()
                (1.50000000000000, 2.00000000000000)

                sage: # needs sage.symbolic
                sage: I = RIF(e, pi)
                sage: a, b = I.bisection()
                sage: a.intersection(b) == RIF(I.center())
                True
                sage: a.union(b).endpoints() == I.endpoints()
                True"""
        @overload
        def bisection(self) -> Any:
            """RealIntervalFieldElement.bisection(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2567)

            Return the bisection of ``self`` into two intervals of half the size
            whose union is ``self`` and intersection is :meth:`center()`.

            EXAMPLES::

                sage: a, b = RIF(1,2).bisection()
                sage: a.lower(), a.upper()
                (1.00000000000000, 1.50000000000000)
                sage: b.lower(), b.upper()
                (1.50000000000000, 2.00000000000000)

                sage: # needs sage.symbolic
                sage: I = RIF(e, pi)
                sage: a, b = I.bisection()
                sage: a.intersection(b) == RIF(I.center())
                True
                sage: a.union(b).endpoints() == I.endpoints()
                True"""
        @overload
        def ceil(self) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def ceil(self) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def ceil(self) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def ceil(self) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def ceil(self) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def ceil(self, a) -> Any:
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        def ceiling(self, *args, **kwargs):
            """RealIntervalFieldElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3060)

            Return the ceiling of this interval as an interval.

            The ceiling of a real number `x` is the smallest integer larger than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_ceil` -- return the ceil as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards minus infinity
                - :meth:`trunc` -- truncation towards zero
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: (2.99).ceil()
                3
                sage: (2.00).ceil()
                2
                sage: (2.01).ceil()
                3
                sage: R = RealIntervalField(30)
                sage: a = R(-9.5, -11.3); a.str(style='brackets')
                '[-11.300000012 .. -9.5000000000]'
                sage: a.floor().str(style='brackets')
                '[-12.000000000 .. -10.000000000]'
                sage: a.ceil()
                -10.?
                sage: ceil(a).str(style='brackets')
                '[-11.000000000 .. -9.0000000000]'"""
        @overload
        def center(self) -> Any:
            """RealIntervalFieldElement.center(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2553)

            Compute the center of the interval `[a .. b]` which is `(a+b) / 2`.

            EXAMPLES::

                sage: RIF(1, 2).center()
                1.50000000000000"""
        @overload
        def center(self) -> Any:
            """RealIntervalFieldElement.center(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2553)

            Compute the center of the interval `[a .. b]` which is `(a+b) / 2`.

            EXAMPLES::

                sage: RIF(1, 2).center()
                1.50000000000000"""
        @overload
        def contains_zero(self) -> Any:
            """RealIntervalFieldElement.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

            Return ``True`` if ``self`` is an interval containing zero.

            EXAMPLES::

                sage: RIF(0).contains_zero()
                True
                sage: RIF(1, 2).contains_zero()
                False
                sage: RIF(-1, 1).contains_zero()
                True
                sage: RIF(-1, 0).contains_zero()
                True"""
        @overload
        def contains_zero(self) -> Any:
            """RealIntervalFieldElement.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

            Return ``True`` if ``self`` is an interval containing zero.

            EXAMPLES::

                sage: RIF(0).contains_zero()
                True
                sage: RIF(1, 2).contains_zero()
                False
                sage: RIF(-1, 1).contains_zero()
                True
                sage: RIF(-1, 0).contains_zero()
                True"""
        @overload
        def contains_zero(self) -> Any:
            """RealIntervalFieldElement.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

            Return ``True`` if ``self`` is an interval containing zero.

            EXAMPLES::

                sage: RIF(0).contains_zero()
                True
                sage: RIF(1, 2).contains_zero()
                False
                sage: RIF(-1, 1).contains_zero()
                True
                sage: RIF(-1, 0).contains_zero()
                True"""
        @overload
        def contains_zero(self) -> Any:
            """RealIntervalFieldElement.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

            Return ``True`` if ``self`` is an interval containing zero.

            EXAMPLES::

                sage: RIF(0).contains_zero()
                True
                sage: RIF(1, 2).contains_zero()
                False
                sage: RIF(-1, 1).contains_zero()
                True
                sage: RIF(-1, 0).contains_zero()
                True"""
        @overload
        def contains_zero(self) -> Any:
            """RealIntervalFieldElement.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4033)

            Return ``True`` if ``self`` is an interval containing zero.

            EXAMPLES::

                sage: RIF(0).contains_zero()
                True
                sage: RIF(1, 2).contains_zero()
                False
                sage: RIF(-1, 1).contains_zero()
                True
                sage: RIF(-1, 0).contains_zero()
                True"""
        @overload
        def cos(self) -> Any:
            """RealIntervalFieldElement.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

            Return the cosine of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: t = RIF(pi)/2
                sage: t.cos()
                0.?e-15
                sage: t.cos().str(style='brackets')
                '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
                sage: t.cos().cos()
                0.9999999999999999?

            TESTS:

            This looped forever with an earlier version of MPFI, but now
            it works::

                sage: RIF(-1, 1).cos().str(style='brackets')
                '[0.54030230586813965 .. 1.0000000000000000]'"""
        @overload
        def cos(self) -> Any:
            """RealIntervalFieldElement.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

            Return the cosine of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: t = RIF(pi)/2
                sage: t.cos()
                0.?e-15
                sage: t.cos().str(style='brackets')
                '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
                sage: t.cos().cos()
                0.9999999999999999?

            TESTS:

            This looped forever with an earlier version of MPFI, but now
            it works::

                sage: RIF(-1, 1).cos().str(style='brackets')
                '[0.54030230586813965 .. 1.0000000000000000]'"""
        @overload
        def cos(self) -> Any:
            """RealIntervalFieldElement.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

            Return the cosine of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: t = RIF(pi)/2
                sage: t.cos()
                0.?e-15
                sage: t.cos().str(style='brackets')
                '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
                sage: t.cos().cos()
                0.9999999999999999?

            TESTS:

            This looped forever with an earlier version of MPFI, but now
            it works::

                sage: RIF(-1, 1).cos().str(style='brackets')
                '[0.54030230586813965 .. 1.0000000000000000]'"""
        @overload
        def cos(self) -> Any:
            """RealIntervalFieldElement.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

            Return the cosine of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: t = RIF(pi)/2
                sage: t.cos()
                0.?e-15
                sage: t.cos().str(style='brackets')
                '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
                sage: t.cos().cos()
                0.9999999999999999?

            TESTS:

            This looped forever with an earlier version of MPFI, but now
            it works::

                sage: RIF(-1, 1).cos().str(style='brackets')
                '[0.54030230586813965 .. 1.0000000000000000]'"""
        @overload
        def cos(self) -> Any:
            """RealIntervalFieldElement.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4639)

            Return the cosine of ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: t = RIF(pi)/2
                sage: t.cos()
                0.?e-15
                sage: t.cos().str(style='brackets')
                '[-1.6081226496766367e-16 .. 6.1232339957367661e-17]'
                sage: t.cos().cos()
                0.9999999999999999?

            TESTS:

            This looped forever with an earlier version of MPFI, but now
            it works::

                sage: RIF(-1, 1).cos().str(style='brackets')
                '[0.54030230586813965 .. 1.0000000000000000]'"""
        @overload
        def cosh(self) -> Any:
            """RealIntervalFieldElement.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4790)

            Return the hyperbolic cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/12
                sage: q.cosh()
                1.034465640095511?"""
        @overload
        def cosh(self) -> Any:
            """RealIntervalFieldElement.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4790)

            Return the hyperbolic cosine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/12
                sage: q.cosh()
                1.034465640095511?"""
        @overload
        def cot(self) -> Any:
            """RealIntervalFieldElement.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4916)

            Return the cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).cot()
                -0.457657554360285763750277410432?"""
        @overload
        def cot(self) -> Any:
            """RealIntervalFieldElement.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4916)

            Return the cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).cot()
                -0.457657554360285763750277410432?"""
        @overload
        def coth(self) -> Any:
            """RealIntervalFieldElement.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4949)

            Return the hyperbolic cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).coth()
                1.03731472072754809587780976477?"""
        @overload
        def coth(self) -> Any:
            """RealIntervalFieldElement.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4949)

            Return the hyperbolic cotangent of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).coth()
                1.03731472072754809587780976477?"""
        @overload
        def csc(self) -> Any:
            """RealIntervalFieldElement.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4905)

            Return the cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).csc()
                1.099750170294616466756697397026?"""
        @overload
        def csc(self) -> Any:
            """RealIntervalFieldElement.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4905)

            Return the cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).csc()
                1.099750170294616466756697397026?"""
        @overload
        def csch(self) -> Any:
            """RealIntervalFieldElement.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4938)

            Return the hyperbolic cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).csch()
                0.275720564771783207758351482163?"""
        @overload
        def csch(self) -> Any:
            """RealIntervalFieldElement.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4938)

            Return the hyperbolic cosecant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).csch()
                0.275720564771783207758351482163?"""
        @overload
        def diameter(self) -> Any:
            """RealIntervalFieldElement.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

            If 0 is in ``self``, then return :meth:`absolute_diameter()`,
            otherwise return :meth:`relative_diameter()`.

            EXAMPLES::

                sage: RIF(1, 2).diameter()
                0.666666666666667
                sage: RIF(1, 2).absolute_diameter()
                1.00000000000000
                sage: RIF(1, 2).relative_diameter()
                0.666666666666667

                sage: # needs sage.symbolic
                sage: RIF(pi).diameter()
                1.41357985842823e-16
                sage: RIF(pi).absolute_diameter()
                4.44089209850063e-16
                sage: RIF(pi).relative_diameter()
                1.41357985842823e-16
                sage: (RIF(pi) - RIF(3, 22/7)).diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
                2.03604377705518"""
        @overload
        def diameter(self) -> Any:
            """RealIntervalFieldElement.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

            If 0 is in ``self``, then return :meth:`absolute_diameter()`,
            otherwise return :meth:`relative_diameter()`.

            EXAMPLES::

                sage: RIF(1, 2).diameter()
                0.666666666666667
                sage: RIF(1, 2).absolute_diameter()
                1.00000000000000
                sage: RIF(1, 2).relative_diameter()
                0.666666666666667

                sage: # needs sage.symbolic
                sage: RIF(pi).diameter()
                1.41357985842823e-16
                sage: RIF(pi).absolute_diameter()
                4.44089209850063e-16
                sage: RIF(pi).relative_diameter()
                1.41357985842823e-16
                sage: (RIF(pi) - RIF(3, 22/7)).diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
                2.03604377705518"""
        @overload
        def diameter(self) -> Any:
            """RealIntervalFieldElement.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

            If 0 is in ``self``, then return :meth:`absolute_diameter()`,
            otherwise return :meth:`relative_diameter()`.

            EXAMPLES::

                sage: RIF(1, 2).diameter()
                0.666666666666667
                sage: RIF(1, 2).absolute_diameter()
                1.00000000000000
                sage: RIF(1, 2).relative_diameter()
                0.666666666666667

                sage: # needs sage.symbolic
                sage: RIF(pi).diameter()
                1.41357985842823e-16
                sage: RIF(pi).absolute_diameter()
                4.44089209850063e-16
                sage: RIF(pi).relative_diameter()
                1.41357985842823e-16
                sage: (RIF(pi) - RIF(3, 22/7)).diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
                2.03604377705518"""
        @overload
        def diameter(self) -> Any:
            """RealIntervalFieldElement.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2419)

            If 0 is in ``self``, then return :meth:`absolute_diameter()`,
            otherwise return :meth:`relative_diameter()`.

            EXAMPLES::

                sage: RIF(1, 2).diameter()
                0.666666666666667
                sage: RIF(1, 2).absolute_diameter()
                1.00000000000000
                sage: RIF(1, 2).relative_diameter()
                0.666666666666667

                sage: # needs sage.symbolic
                sage: RIF(pi).diameter()
                1.41357985842823e-16
                sage: RIF(pi).absolute_diameter()
                4.44089209850063e-16
                sage: RIF(pi).relative_diameter()
                1.41357985842823e-16
                sage: (RIF(pi) - RIF(3, 22/7)).diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).absolute_diameter()
                0.142857142857144
                sage: (RIF(pi) - RIF(3, 22/7)).relative_diameter()
                2.03604377705518"""
        @overload
        def edges(self) -> Any:
            """RealIntervalFieldElement.edges(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

            Return the lower and upper endpoints of this interval as
            intervals.

            OUTPUT: a 2-tuple of real intervals
            (lower endpoint, upper endpoint)
            each containing just one point.

            .. SEEALSO::

                :meth:`endpoints` which returns the endpoints as real
                numbers instead of intervals.

            EXAMPLES::

                sage: RIF(1,2).edges()
                (1, 2)
                sage: RIF(pi).edges()                                                       # needs sage.symbolic
                (3.1415926535897932?, 3.1415926535897936?)"""
        @overload
        def edges(self) -> Any:
            """RealIntervalFieldElement.edges(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

            Return the lower and upper endpoints of this interval as
            intervals.

            OUTPUT: a 2-tuple of real intervals
            (lower endpoint, upper endpoint)
            each containing just one point.

            .. SEEALSO::

                :meth:`endpoints` which returns the endpoints as real
                numbers instead of intervals.

            EXAMPLES::

                sage: RIF(1,2).edges()
                (1, 2)
                sage: RIF(pi).edges()                                                       # needs sage.symbolic
                (3.1415926535897932?, 3.1415926535897936?)"""
        @overload
        def edges(self) -> Any:
            """RealIntervalFieldElement.edges(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2357)

            Return the lower and upper endpoints of this interval as
            intervals.

            OUTPUT: a 2-tuple of real intervals
            (lower endpoint, upper endpoint)
            each containing just one point.

            .. SEEALSO::

                :meth:`endpoints` which returns the endpoints as real
                numbers instead of intervals.

            EXAMPLES::

                sage: RIF(1,2).edges()
                (1, 2)
                sage: RIF(pi).edges()                                                       # needs sage.symbolic
                (3.1415926535897932?, 3.1415926535897936?)"""
        @overload
        def endpoints(self, rnd=...) -> Any:
            """RealIntervalFieldElement.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

            Return the lower and upper endpoints of this interval.

            OUTPUT: a 2-tuple of real numbers
            (lower endpoint, upper endpoint)

            .. SEEALSO::

                :meth:`edges` which returns the endpoints as exact
                intervals instead of real numbers.

            EXAMPLES::

                sage: RIF(1,2).endpoints()
                (1.00000000000000, 2.00000000000000)
                sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
                (3.14159265358979, 3.14159265358980)
                sage: a = CIF(RIF(1,2), RIF(3,4))
                sage: a.real().endpoints()
                (1.00000000000000, 2.00000000000000)

            As with ``lower()`` and ``upper()``, a rounding mode is accepted::

                sage: RIF(1,2).endpoints('RNDD')[0].parent()
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def endpoints(self) -> Any:
            """RealIntervalFieldElement.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

            Return the lower and upper endpoints of this interval.

            OUTPUT: a 2-tuple of real numbers
            (lower endpoint, upper endpoint)

            .. SEEALSO::

                :meth:`edges` which returns the endpoints as exact
                intervals instead of real numbers.

            EXAMPLES::

                sage: RIF(1,2).endpoints()
                (1.00000000000000, 2.00000000000000)
                sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
                (3.14159265358979, 3.14159265358980)
                sage: a = CIF(RIF(1,2), RIF(3,4))
                sage: a.real().endpoints()
                (1.00000000000000, 2.00000000000000)

            As with ``lower()`` and ``upper()``, a rounding mode is accepted::

                sage: RIF(1,2).endpoints('RNDD')[0].parent()
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def endpoints(self) -> Any:
            """RealIntervalFieldElement.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

            Return the lower and upper endpoints of this interval.

            OUTPUT: a 2-tuple of real numbers
            (lower endpoint, upper endpoint)

            .. SEEALSO::

                :meth:`edges` which returns the endpoints as exact
                intervals instead of real numbers.

            EXAMPLES::

                sage: RIF(1,2).endpoints()
                (1.00000000000000, 2.00000000000000)
                sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
                (3.14159265358979, 3.14159265358980)
                sage: a = CIF(RIF(1,2), RIF(3,4))
                sage: a.real().endpoints()
                (1.00000000000000, 2.00000000000000)

            As with ``lower()`` and ``upper()``, a rounding mode is accepted::

                sage: RIF(1,2).endpoints('RNDD')[0].parent()
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def endpoints(self) -> Any:
            """RealIntervalFieldElement.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2328)

            Return the lower and upper endpoints of this interval.

            OUTPUT: a 2-tuple of real numbers
            (lower endpoint, upper endpoint)

            .. SEEALSO::

                :meth:`edges` which returns the endpoints as exact
                intervals instead of real numbers.

            EXAMPLES::

                sage: RIF(1,2).endpoints()
                (1.00000000000000, 2.00000000000000)
                sage: RIF(pi).endpoints()                                                   # needs sage.symbolic
                (3.14159265358979, 3.14159265358980)
                sage: a = CIF(RIF(1,2), RIF(3,4))
                sage: a.real().endpoints()
                (1.00000000000000, 2.00000000000000)

            As with ``lower()`` and ``upper()``, a rounding mode is accepted::

                sage: RIF(1,2).endpoints('RNDD')[0].parent()
                Real Field with 53 bits of precision and rounding RNDD"""
        def exp(self) -> Any:
            """RealIntervalFieldElement.exp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4538)

            Return `e^\\mathtt{self}`.

            EXAMPLES::

                sage: r = RIF(0.0)
                sage: r.exp()
                1

            ::

                sage: r = RIF(32.3)
                sage: a = r.exp(); a
                1.065888472748645?e14
                sage: a.log()
                32.30000000000000?

            ::

                sage: r = RIF(-32.3)
                sage: r.exp()
                9.38184458849869?e-15"""
        def exp2(self) -> Any:
            """RealIntervalFieldElement.exp2(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4568)

            Return `2^\\mathtt{self}`.

            EXAMPLES::

                sage: r = RIF(0.0)
                sage: r.exp2()
                1

            ::

                sage: r = RIF(32.0)
                sage: r.exp2()
                4294967296

            ::

                sage: r = RIF(-32.3)
                sage: r.exp2()
                1.891172482530207?e-10"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def factorial(self) -> Any:
            """RealIntervalFieldElement.factorial(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5061)

            Return the factorial evaluated on ``self``.

            EXAMPLES::

                sage: RIF(5).factorial()
                120
                sage: RIF(2.3,5.7).factorial()
                1.?e3
                sage: RIF(2.3).factorial()
                2.683437381955768?

            Recover the factorial as integer::

                sage: f = RealIntervalField(200)(50).factorial()
                sage: f
                3.0414093201713378043612608166064768844377641568960512000000000?e64
                sage: f.unique_integer()
                30414093201713378043612608166064768844377641568960512000000000000
                sage: 50.factorial()
                30414093201713378043612608166064768844377641568960512000000000000"""
        @overload
        def floor(self) -> Any:
            """RealIntervalFieldElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

            Return the floor of this interval as an interval.

            The floor of a real number `x` is the largest integer smaller than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_floor` -- method which returns the floor as an integer
                  if it is unique or raises a :exc:`ValueError` otherwise
                - :meth:`ceil` -- truncation towards plus infinity
                - :meth:`round` -- rounding
                - :meth:`trunc` -- truncation towards zero

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: (2.99).floor()
                2
                sage: (2.00).floor()
                2
                sage: floor(RR(-5/2))
                -3
                sage: R = RealIntervalField(100)
                sage: a = R(9.5, 11.3); a.str(style='brackets')
                '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
                sage: floor(a).str(style='brackets')
                '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
                sage: a.floor()
                10.?
                sage: ceil(a)
                11.?
                sage: a.ceil().str(style='brackets')
                '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
        @overload
        def floor(self) -> Any:
            """RealIntervalFieldElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

            Return the floor of this interval as an interval.

            The floor of a real number `x` is the largest integer smaller than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_floor` -- method which returns the floor as an integer
                  if it is unique or raises a :exc:`ValueError` otherwise
                - :meth:`ceil` -- truncation towards plus infinity
                - :meth:`round` -- rounding
                - :meth:`trunc` -- truncation towards zero

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: (2.99).floor()
                2
                sage: (2.00).floor()
                2
                sage: floor(RR(-5/2))
                -3
                sage: R = RealIntervalField(100)
                sage: a = R(9.5, 11.3); a.str(style='brackets')
                '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
                sage: floor(a).str(style='brackets')
                '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
                sage: a.floor()
                10.?
                sage: ceil(a)
                11.?
                sage: a.ceil().str(style='brackets')
                '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
        @overload
        def floor(self) -> Any:
            """RealIntervalFieldElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

            Return the floor of this interval as an interval.

            The floor of a real number `x` is the largest integer smaller than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_floor` -- method which returns the floor as an integer
                  if it is unique or raises a :exc:`ValueError` otherwise
                - :meth:`ceil` -- truncation towards plus infinity
                - :meth:`round` -- rounding
                - :meth:`trunc` -- truncation towards zero

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: (2.99).floor()
                2
                sage: (2.00).floor()
                2
                sage: floor(RR(-5/2))
                -3
                sage: R = RealIntervalField(100)
                sage: a = R(9.5, 11.3); a.str(style='brackets')
                '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
                sage: floor(a).str(style='brackets')
                '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
                sage: a.floor()
                10.?
                sage: ceil(a)
                11.?
                sage: a.ceil().str(style='brackets')
                '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
        @overload
        def floor(self, a) -> Any:
            """RealIntervalFieldElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

            Return the floor of this interval as an interval.

            The floor of a real number `x` is the largest integer smaller than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_floor` -- method which returns the floor as an integer
                  if it is unique or raises a :exc:`ValueError` otherwise
                - :meth:`ceil` -- truncation towards plus infinity
                - :meth:`round` -- rounding
                - :meth:`trunc` -- truncation towards zero

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: (2.99).floor()
                2
                sage: (2.00).floor()
                2
                sage: floor(RR(-5/2))
                -3
                sage: R = RealIntervalField(100)
                sage: a = R(9.5, 11.3); a.str(style='brackets')
                '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
                sage: floor(a).str(style='brackets')
                '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
                sage: a.floor()
                10.?
                sage: ceil(a)
                11.?
                sage: a.ceil().str(style='brackets')
                '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
        @overload
        def floor(self) -> Any:
            """RealIntervalFieldElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3022)

            Return the floor of this interval as an interval.

            The floor of a real number `x` is the largest integer smaller than or
            equal to `x`.

            .. SEEALSO::

                - :meth:`unique_floor` -- method which returns the floor as an integer
                  if it is unique or raises a :exc:`ValueError` otherwise
                - :meth:`ceil` -- truncation towards plus infinity
                - :meth:`round` -- rounding
                - :meth:`trunc` -- truncation towards zero

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: (2.99).floor()
                2
                sage: (2.00).floor()
                2
                sage: floor(RR(-5/2))
                -3
                sage: R = RealIntervalField(100)
                sage: a = R(9.5, 11.3); a.str(style='brackets')
                '[9.5000000000000000000000000000000 .. 11.300000000000000710542735760101]'
                sage: floor(a).str(style='brackets')
                '[9.0000000000000000000000000000000 .. 11.000000000000000000000000000000]'
                sage: a.floor()
                10.?
                sage: ceil(a)
                11.?
                sage: a.ceil().str(style='brackets')
                '[10.000000000000000000000000000000 .. 12.000000000000000000000000000000]'"""
        def fp_rank_diameter(self) -> Any:
            '''RealIntervalFieldElement.fp_rank_diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2452)

            Compute the diameter of this interval in terms of the
            "floating-point rank".

            The floating-point rank is the number of floating-point numbers (of
            the current precision) contained in the given interval, minus one. An
            ``fp_rank_diameter`` of 0 means that the interval is exact; an
            ``fp_rank_diameter`` of 1 means that the interval is
            as tight as possible, unless the number you\'re trying to represent
            is actually exactly representable as a floating-point number.

            EXAMPLES::

                sage: RIF(12345).fp_rank_diameter()
                0
                sage: RIF(5/8).fp_rank_diameter()
                0
                sage: RIF(5/7).fp_rank_diameter()
                1

                sage: # needs sage.symbolic
                sage: RIF(pi).fp_rank_diameter()
                1
                sage: RIF(-sqrt(2)).fp_rank_diameter()
                1
                sage: a = RIF(pi)^12345; a
                2.06622879260?e6137
                sage: a.fp_rank_diameter()
                30524
                sage: (RIF(sqrt(2)) - RIF(sqrt(2))).fp_rank_diameter()
                9671406088542672151117826            # 32-bit
                41538374868278620559869609387229186  # 64-bit

            Just because we have the best possible interval, doesn\'t mean the
            interval is actually small::

                sage: a = RIF(pi)^12345678901234567890; a                                   # needs sage.symbolic
                [2.0985787164673874e323228496 .. +infinity]            # 32-bit
                [5.8756537891115869e1388255822130839282 .. +infinity]  # 64-bit
                sage: a.fp_rank_diameter()                                                  # needs sage.symbolic
                1'''
        @overload
        def frac(self) -> Any:
            """RealIntervalFieldElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3172)

            Return the fractional part of this interval as an interval.

            The fractional part `y` of a real number `x` is the unique element in the
            interval `(-1,1)` that has the same sign as `x` and such that `x-y` is
            an integer. The integer `x-y` can be obtained through the method
            :meth:`trunc`.

            The output of this function is the smallest interval that contains all
            possible values of `frac(x)` for `x` in this interval. Note that if it
            contains an integer then the answer might not be very meaningful. More
            precisely, if the endpoints are `a` and `b` then:

            - if `floor(b) > \\max(a,0)` then the interval obtained contains `[0,1]`,
            - if `ceil(a) < \\min(b,0)` then the interval obtained contains `[-1,0]`.

            .. SEEALSO::

                :meth:`trunc` -- return the integer part complement to this
                fractional part

            EXAMPLES::

                sage: RIF(2.37123, 2.372).frac()
                0.372?
                sage: RIF(-23.12, -23.13).frac()
                -0.13?

                sage: RIF(.5, 1).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(1, 1.5).frac().endpoints()
                (0.000000000000000, 0.500000000000000)

                sage: r = RIF(-22.47, -22.468)
                sage: r in (r.frac() + r.trunc())
                True

                sage: r = RIF(18.222, 18.223)
                sage: r in (r.frac() + r.trunc())
                True

                sage: RIF(1.99, 2.025).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(1.99, 2.00).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(2.00, 2.025).frac().endpoints()
                (0.000000000000000, 0.0250000000000000)

                sage: RIF(-2.1,-0.9).frac().endpoints()
                (-1.00000000000000, -0.000000000000000)
                sage: RIF(-0.5,0.5).frac().endpoints()
                (-0.500000000000000, 0.500000000000000)"""
        @overload
        def frac(self, x) -> Any:
            """RealIntervalFieldElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3172)

            Return the fractional part of this interval as an interval.

            The fractional part `y` of a real number `x` is the unique element in the
            interval `(-1,1)` that has the same sign as `x` and such that `x-y` is
            an integer. The integer `x-y` can be obtained through the method
            :meth:`trunc`.

            The output of this function is the smallest interval that contains all
            possible values of `frac(x)` for `x` in this interval. Note that if it
            contains an integer then the answer might not be very meaningful. More
            precisely, if the endpoints are `a` and `b` then:

            - if `floor(b) > \\max(a,0)` then the interval obtained contains `[0,1]`,
            - if `ceil(a) < \\min(b,0)` then the interval obtained contains `[-1,0]`.

            .. SEEALSO::

                :meth:`trunc` -- return the integer part complement to this
                fractional part

            EXAMPLES::

                sage: RIF(2.37123, 2.372).frac()
                0.372?
                sage: RIF(-23.12, -23.13).frac()
                -0.13?

                sage: RIF(.5, 1).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(1, 1.5).frac().endpoints()
                (0.000000000000000, 0.500000000000000)

                sage: r = RIF(-22.47, -22.468)
                sage: r in (r.frac() + r.trunc())
                True

                sage: r = RIF(18.222, 18.223)
                sage: r in (r.frac() + r.trunc())
                True

                sage: RIF(1.99, 2.025).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(1.99, 2.00).frac().endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(2.00, 2.025).frac().endpoints()
                (0.000000000000000, 0.0250000000000000)

                sage: RIF(-2.1,-0.9).frac().endpoints()
                (-1.00000000000000, -0.000000000000000)
                sage: RIF(-0.5,0.5).frac().endpoints()
                (-0.500000000000000, 0.500000000000000)"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def gamma(self) -> Any:
            """RealIntervalFieldElement.gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5086)

            Return the gamma function evaluated on ``self``.

            EXAMPLES::

                sage: RIF(1).gamma()
                1
                sage: RIF(5).gamma()
                24
                sage: a = RIF(3,4).gamma(); a
                1.?e1
                sage: a.lower(), a.upper()
                (2.00000000000000, 6.00000000000000)
                sage: RIF(-1/2).gamma()
                -3.54490770181104?
                sage: gamma(-1/2).n(100) in RIF(-1/2).gamma()                               # needs sage.symbolic
                True
                sage: RIF1000 = RealIntervalField(1000)
                sage: 0 in (RIF1000(RealField(2000)(-19/3).gamma()) - RIF1000(-19/3).gamma())
                True
                sage: gamma(RIF(100))
                9.33262154439442?e155
                sage: gamma(RIF(-10000/3))
                1.31280781451?e-10297

            Verify the result contains the local minima::

                sage: 0.88560319441088 in RIF(1, 2).gamma()
                True
                sage: 0.88560319441088 in RIF(0.25, 4).gamma()
                True
                sage: 0.88560319441088 in RIF(1.4616, 1.46164).gamma()
                True

                sage: (-0.99).gamma()
                -100.436954665809
                sage: (-0.01).gamma()
                -100.587197964411
                sage: RIF(-0.99, -0.01).gamma().upper()
                -1.60118039970055

            Correctly detects poles::

                sage: gamma(RIF(-3/2,-1/2))
                [-infinity .. +infinity]"""
        @overload
        def imag(self) -> Any:
            """RealIntervalFieldElement.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1478)

            Return the imaginary part of this real interval.

            (Since this is interval is real, this simply returns the zero interval.)

            .. SEEALSO::

                :meth:`real`

            EXAMPLES::

                sage: RIF(2,3).imag()
                0"""
        @overload
        def imag(self) -> Any:
            """RealIntervalFieldElement.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1478)

            Return the imaginary part of this real interval.

            (Since this is interval is real, this simply returns the zero interval.)

            .. SEEALSO::

                :meth:`real`

            EXAMPLES::

                sage: RIF(2,3).imag()
                0"""
        def intersection(self, other) -> Any:
            """RealIntervalFieldElement.intersection(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4074)

            Return the intersection of two intervals. If the intervals do not
            overlap, raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1, 2).intersection(RIF(1.5, 3)).str(style='brackets')
                '[1.5000000000000000 .. 2.0000000000000000]'
                sage: RIF(1, 2).intersection(RIF(4/3, 5/3)).str(style='brackets')
                '[1.3333333333333332 .. 1.6666666666666668]'
                sage: RIF(1, 2).intersection(RIF(3, 4))
                Traceback (most recent call last):
                ...
                ValueError: intersection of non-overlapping intervals"""
        @overload
        def is_NaN(self) -> Any:
            """RealIntervalFieldElement.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3703)

            Check to see if ``self`` is Not-a-Number ``NaN``.

            EXAMPLES::

                sage: a = RIF(0) / RIF(0.0,0.00); a
                [.. NaN ..]
                sage: a.is_NaN()
                True"""
        @overload
        def is_NaN(self) -> Any:
            """RealIntervalFieldElement.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3703)

            Check to see if ``self`` is Not-a-Number ``NaN``.

            EXAMPLES::

                sage: a = RIF(0) / RIF(0.0,0.00); a
                [.. NaN ..]
                sage: a.is_NaN()
                True"""
        @overload
        def is_exact(self) -> Any:
            """RealIntervalFieldElement.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

            Return whether this real interval is exact (i.e. contains exactly
            one real value).

            EXAMPLES::

                sage: RIF(3).is_exact()
                True
                sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
                False"""
        @overload
        def is_exact(self) -> Any:
            """RealIntervalFieldElement.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

            Return whether this real interval is exact (i.e. contains exactly
            one real value).

            EXAMPLES::

                sage: RIF(3).is_exact()
                True
                sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
                False"""
        @overload
        def is_exact(self) -> Any:
            """RealIntervalFieldElement.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2497)

            Return whether this real interval is exact (i.e. contains exactly
            one real value).

            EXAMPLES::

                sage: RIF(3).is_exact()
                True
                sage: RIF(2*pi).is_exact()                                                  # needs sage.symbolic
                False"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        @overload
        def is_int(self) -> Any:
            """RealIntervalFieldElement.is_int(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4596)

            Check to see whether this interval includes exactly one integer.

            OUTPUT:

            If this contains exactly one integer, it returns the tuple
            ``(True, n)``, where ``n`` is that integer; otherwise, this returns
            ``(False, None)``.

            EXAMPLES::

                sage: a = RIF(0.8,1.5)
                sage: a.is_int()
                (True, 1)
                sage: a = RIF(1.1,1.5)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(1,2)
                sage: a.is_int()
                (False, None)
                sage: a = RIF(-1.1, -0.9)
                sage: a.is_int()
                (True, -1)
                sage: a = RIF(0.1, 1.9)
                sage: a.is_int()
                (True, 1)
                sage: RIF(+infinity,+infinity).is_int()
                (False, None)"""
        def lexico_cmp(self, left, right) -> Any:
            """RealIntervalFieldElement.lexico_cmp(left, right)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3948)

            Compare two intervals lexicographically.

            This means that the left bounds are compared first and then
            the right bounds are compared if the left bounds coincide.

            Return 0 if they are the same interval, -1 if the second is larger,
            or 1 if the first is larger.

            EXAMPLES::

                sage: RIF(0).lexico_cmp(RIF(1))
                -1
                sage: RIF(0, 1).lexico_cmp(RIF(1))
                -1
                sage: RIF(0, 1).lexico_cmp(RIF(1, 2))
                -1
                sage: RIF(0, 0.99999).lexico_cmp(RIF(1, 2))
                -1
                sage: RIF(1, 2).lexico_cmp(RIF(0, 1))
                1
                sage: RIF(1, 2).lexico_cmp(RIF(0))
                1
                sage: RIF(0, 1).lexico_cmp(RIF(0, 2))
                -1
                sage: RIF(0, 1).lexico_cmp(RIF(0, 1))
                0
                sage: RIF(0, 1).lexico_cmp(RIF(0, 1/2))
                1"""
        @overload
        def log(self, base=...) -> Any:
            """RealIntervalFieldElement.log(self, base='e')

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

            Return the logarithm of ``self`` to the given ``base``.

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: r = R(2); r.log()
                0.6931471805599453?
                sage: r = R(-2); r.log()
                0.6931471805599453? + 3.141592653589794?*I"""
        @overload
        def log(self) -> Any:
            """RealIntervalFieldElement.log(self, base='e')

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

            Return the logarithm of ``self`` to the given ``base``.

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: r = R(2); r.log()
                0.6931471805599453?
                sage: r = R(-2); r.log()
                0.6931471805599453? + 3.141592653589794?*I"""
        @overload
        def log(self) -> Any:
            """RealIntervalFieldElement.log(self, base='e')

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4446)

            Return the logarithm of ``self`` to the given ``base``.

            EXAMPLES::

                sage: R = RealIntervalField()
                sage: r = R(2); r.log()
                0.6931471805599453?
                sage: r = R(-2); r.log()
                0.6931471805599453? + 3.141592653589794?*I"""
        @overload
        def log10(self) -> Any:
            """RealIntervalFieldElement.log10(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

            Return log to the base 10 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0); r.log10()
                1.204119982655925?
                sage: r.log() / RIF(10).log()
                1.204119982655925?

            ::

                sage: r = RIF(39.9); r.log10()
                1.600972895686749?

            ::

                sage: r = RIF(0.0)
                sage: r.log10()
                [-infinity .. -infinity]

            ::

                sage: r = RIF(-1.0)
                sage: r.log10()
                1.364376353841841?*I"""
        @overload
        def log10(self) -> Any:
            """RealIntervalFieldElement.log10(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

            Return log to the base 10 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0); r.log10()
                1.204119982655925?
                sage: r.log() / RIF(10).log()
                1.204119982655925?

            ::

                sage: r = RIF(39.9); r.log10()
                1.600972895686749?

            ::

                sage: r = RIF(0.0)
                sage: r.log10()
                [-infinity .. -infinity]

            ::

                sage: r = RIF(-1.0)
                sage: r.log10()
                1.364376353841841?*I"""
        @overload
        def log10(self) -> Any:
            """RealIntervalFieldElement.log10(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

            Return log to the base 10 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0); r.log10()
                1.204119982655925?
                sage: r.log() / RIF(10).log()
                1.204119982655925?

            ::

                sage: r = RIF(39.9); r.log10()
                1.600972895686749?

            ::

                sage: r = RIF(0.0)
                sage: r.log10()
                [-infinity .. -infinity]

            ::

                sage: r = RIF(-1.0)
                sage: r.log10()
                1.364376353841841?*I"""
        @overload
        def log10(self) -> Any:
            """RealIntervalFieldElement.log10(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

            Return log to the base 10 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0); r.log10()
                1.204119982655925?
                sage: r.log() / RIF(10).log()
                1.204119982655925?

            ::

                sage: r = RIF(39.9); r.log10()
                1.600972895686749?

            ::

                sage: r = RIF(0.0)
                sage: r.log10()
                [-infinity .. -infinity]

            ::

                sage: r = RIF(-1.0)
                sage: r.log10()
                1.364376353841841?*I"""
        @overload
        def log10(self) -> Any:
            """RealIntervalFieldElement.log10(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4502)

            Return log to the base 10 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0); r.log10()
                1.204119982655925?
                sage: r.log() / RIF(10).log()
                1.204119982655925?

            ::

                sage: r = RIF(39.9); r.log10()
                1.600972895686749?

            ::

                sage: r = RIF(0.0)
                sage: r.log10()
                [-infinity .. -infinity]

            ::

                sage: r = RIF(-1.0)
                sage: r.log10()
                1.364376353841841?*I"""
        @overload
        def log2(self) -> Any:
            """RealIntervalFieldElement.log2(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

            Return ``log`` to the base 2 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0)
                sage: r.log2()
                4

            ::

                sage: r = RIF(31.9); r.log2()
                4.995484518877507?

            ::

                sage: r = RIF(0.0, 2.0)
                sage: r.log2()
                [-infinity .. 1.0000000000000000]"""
        @overload
        def log2(self) -> Any:
            """RealIntervalFieldElement.log2(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

            Return ``log`` to the base 2 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0)
                sage: r.log2()
                4

            ::

                sage: r = RIF(31.9); r.log2()
                4.995484518877507?

            ::

                sage: r = RIF(0.0, 2.0)
                sage: r.log2()
                [-infinity .. 1.0000000000000000]"""
        @overload
        def log2(self) -> Any:
            """RealIntervalFieldElement.log2(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

            Return ``log`` to the base 2 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0)
                sage: r.log2()
                4

            ::

                sage: r = RIF(31.9); r.log2()
                4.995484518877507?

            ::

                sage: r = RIF(0.0, 2.0)
                sage: r.log2()
                [-infinity .. 1.0000000000000000]"""
        @overload
        def log2(self) -> Any:
            """RealIntervalFieldElement.log2(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4473)

            Return ``log`` to the base 2 of ``self``.

            EXAMPLES::

                sage: r = RIF(16.0)
                sage: r.log2()
                4

            ::

                sage: r = RIF(31.9); r.log2()
                4.995484518877507?

            ::

                sage: r = RIF(0.0, 2.0)
                sage: r.log2()
                [-infinity .. 1.0000000000000000]"""
        @overload
        def lower(self, rnd=...) -> Any:
            """RealIntervalFieldElement.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

            Return the lower bound of this interval.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards minus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().lower().str()
                '3.1411'

            ::

                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.lower()
                1.19
                sage: x.lower('RNDU')
                1.20
                sage: x.lower('RNDN')
                1.20
                sage: x.lower('RNDZ')
                1.19
                sage: x.lower('RNDA')
                1.20
                sage: x.lower().parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.lower('RNDU').parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.lower('RNDA').parent()
                Real Field with 13 bits of precision and rounding RNDA
                sage: x.lower() == x.lower('RNDU')
                True"""
        @overload
        def lower(self) -> Any:
            """RealIntervalFieldElement.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

            Return the lower bound of this interval.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards minus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().lower().str()
                '3.1411'

            ::

                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.lower()
                1.19
                sage: x.lower('RNDU')
                1.20
                sage: x.lower('RNDN')
                1.20
                sage: x.lower('RNDZ')
                1.19
                sage: x.lower('RNDA')
                1.20
                sage: x.lower().parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.lower('RNDU').parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.lower('RNDA').parent()
                Real Field with 13 bits of precision and rounding RNDA
                sage: x.lower() == x.lower('RNDU')
                True"""
        @overload
        def lower(self) -> Any:
            """RealIntervalFieldElement.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

            Return the lower bound of this interval.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards minus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().lower().str()
                '3.1411'

            ::

                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.lower()
                1.19
                sage: x.lower('RNDU')
                1.20
                sage: x.lower('RNDN')
                1.20
                sage: x.lower('RNDZ')
                1.19
                sage: x.lower('RNDA')
                1.20
                sage: x.lower().parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.lower('RNDU').parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.lower('RNDA').parent()
                Real Field with 13 bits of precision and rounding RNDA
                sage: x.lower() == x.lower('RNDU')
                True"""
        @overload
        def lower(self) -> Any:
            """RealIntervalFieldElement.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2225)

            Return the lower bound of this interval.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards minus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().lower().str()
                '3.1411'

            ::

                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.lower()
                1.19
                sage: x.lower('RNDU')
                1.20
                sage: x.lower('RNDN')
                1.20
                sage: x.lower('RNDZ')
                1.19
                sage: x.lower('RNDA')
                1.20
                sage: x.lower().parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.lower('RNDU').parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.lower('RNDA').parent()
                Real Field with 13 bits of precision and rounding RNDA
                sage: x.lower() == x.lower('RNDU')
                True"""
        @overload
        def magnitude(self) -> Any:
            """RealIntervalFieldElement.magnitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

            The largest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDU``

            EXAMPLES::

                sage: RIF(-2, 1).magnitude()
                2.00000000000000
                sage: RIF(-1, 2).magnitude()
                2.00000000000000
                sage: parent(RIF(1).magnitude())
                Real Field with 53 bits of precision and rounding RNDU"""
        @overload
        def magnitude(self) -> Any:
            """RealIntervalFieldElement.magnitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

            The largest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDU``

            EXAMPLES::

                sage: RIF(-2, 1).magnitude()
                2.00000000000000
                sage: RIF(-1, 2).magnitude()
                2.00000000000000
                sage: parent(RIF(1).magnitude())
                Real Field with 53 bits of precision and rounding RNDU"""
        @overload
        def magnitude(self) -> Any:
            """RealIntervalFieldElement.magnitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

            The largest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDU``

            EXAMPLES::

                sage: RIF(-2, 1).magnitude()
                2.00000000000000
                sage: RIF(-1, 2).magnitude()
                2.00000000000000
                sage: parent(RIF(1).magnitude())
                Real Field with 53 bits of precision and rounding RNDU"""
        @overload
        def magnitude(self) -> Any:
            """RealIntervalFieldElement.magnitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2511)

            The largest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDU``

            EXAMPLES::

                sage: RIF(-2, 1).magnitude()
                2.00000000000000
                sage: RIF(-1, 2).magnitude()
                2.00000000000000
                sage: parent(RIF(1).magnitude())
                Real Field with 53 bits of precision and rounding RNDU"""
        @overload
        def max(self, *_others) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def max(self, a, b) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def max(self, a, c) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def max(self, b, c) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def max(self, a, b, c) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def max(self, *elements) -> Any:
            """RealIntervalFieldElement.max(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4242)

            Return an interval containing the maximum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: RIF(-1, 1).max(0).endpoints()
                (0.000000000000000, 1.00000000000000)
                sage: RIF(-1, 1).max(RIF(2, 3)).endpoints()
                (2.00000000000000, 3.00000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100)).endpoints()
                (-1.00000000000000, 100.000000000000)
                sage: RIF(-1, 1).max(RIF(-100, 100), RIF(5, 10)).endpoints()
                (5.00000000000000, 100.000000000000)

            Note that if the maximum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.max(a, b) is c
                True
                sage: b.max(a, c) is c
                True
                sage: a.max(b, c) is c
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.max(a, b, c) is c
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.max(*elements) is c
                True

            The generic max does not always do the right thing::

                sage: max(0, RIF(-1, 1))
                0
                sage: max(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').max(1, 2)
                2
                sage: RIF(-1/3).max(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').max(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.min`

            TESTS::

                sage: a.max('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def mignitude(self) -> Any:
            """RealIntervalFieldElement.mignitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

            The smallest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDD``

            EXAMPLES::

                sage: RIF(-2, 1).mignitude()
                0.000000000000000
                sage: RIF(-2, -1).mignitude()
                1.00000000000000
                sage: RIF(3, 4).mignitude()
                3.00000000000000
                sage: parent(RIF(1).mignitude())
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def mignitude(self) -> Any:
            """RealIntervalFieldElement.mignitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

            The smallest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDD``

            EXAMPLES::

                sage: RIF(-2, 1).mignitude()
                0.000000000000000
                sage: RIF(-2, -1).mignitude()
                1.00000000000000
                sage: RIF(3, 4).mignitude()
                3.00000000000000
                sage: parent(RIF(1).mignitude())
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def mignitude(self) -> Any:
            """RealIntervalFieldElement.mignitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

            The smallest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDD``

            EXAMPLES::

                sage: RIF(-2, 1).mignitude()
                0.000000000000000
                sage: RIF(-2, -1).mignitude()
                1.00000000000000
                sage: RIF(3, 4).mignitude()
                3.00000000000000
                sage: parent(RIF(1).mignitude())
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def mignitude(self) -> Any:
            """RealIntervalFieldElement.mignitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

            The smallest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDD``

            EXAMPLES::

                sage: RIF(-2, 1).mignitude()
                0.000000000000000
                sage: RIF(-2, -1).mignitude()
                1.00000000000000
                sage: RIF(3, 4).mignitude()
                3.00000000000000
                sage: parent(RIF(1).mignitude())
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def mignitude(self) -> Any:
            """RealIntervalFieldElement.mignitude(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2531)

            The smallest absolute value of the elements of the interval.

            OUTPUT: a real number with rounding mode ``RNDD``

            EXAMPLES::

                sage: RIF(-2, 1).mignitude()
                0.000000000000000
                sage: RIF(-2, -1).mignitude()
                1.00000000000000
                sage: RIF(3, 4).mignitude()
                3.00000000000000
                sage: parent(RIF(1).mignitude())
                Real Field with 53 bits of precision and rounding RNDD"""
        @overload
        def min(self, *_others) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, pi) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, a, b) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, a, c) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, b, c) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, a, b, c) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        @overload
        def min(self, *elements) -> Any:
            """RealIntervalFieldElement.min(self, *_others)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4135)

            Return an interval containing the minimum of ``self`` and the
            arguments.

            EXAMPLES::

                sage: a = RIF(-1, 1).min(0).endpoints()
                sage: a[0] == -1.0 and a[1].abs() == 0.0 # in MPFI, the sign of 0.0 is not specified
                True
                sage: RIF(-1, 1).min(pi).endpoints()                                        # needs sage.symbolic
                (-1.00000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 100)).endpoints()
                (-100.000000000000, 1.00000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 0)).endpoints()
                (-100.000000000000, 0.000000000000000)
                sage: RIF(-1, 1).min(RIF(-100, 2), RIF(-200, -3)).endpoints()
                (-200.000000000000, -3.00000000000000)

            Note that if the minimum is one of the given elements,
            that element will be returned. ::

                sage: a = RIF(-1, 1)
                sage: b = RIF(2, 3)
                sage: c = RIF(3, 4)
                sage: c.min(a, b) is a
                True
                sage: b.min(a, c) is a
                True
                sage: a.min(b, c) is a
                True

            It might also be convenient to call the method as a function::

                sage: from sage.rings.real_mpfi import RealIntervalFieldElement
                sage: RealIntervalFieldElement.min(a, b, c) is a
                True
                sage: elements = [a, b, c]
                sage: RealIntervalFieldElement.min(*elements) is a
                True

            The generic min does not always do the right thing::

                sage: min(0, RIF(-1, 1))
                0
                sage: min(RIF(-1, 1), RIF(-100, 100)).endpoints()
                (-1.00000000000000, 1.00000000000000)

            Note that calls involving NaNs try to return a number when possible.
            This is consistent with IEEE-754-2008 but may be surprising. ::

                sage: RIF('nan').min(2, 1)
                1
                sage: RIF(-1/3).min(RIF('nan'))
                -0.3333333333333334?
                sage: RIF('nan').min(RIF('nan'))
                [.. NaN ..]

            .. SEEALSO::

                :meth:`~sage.rings.real_mpfi.RealIntervalFieldElement.max`

            TESTS::

                sage: a.min('x')
                Traceback (most recent call last):
                ...
                TypeError: unable to convert 'x' to real interval"""
        def multiplicative_order(self) -> Any:
            """RealIntervalFieldElement.multiplicative_order(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2982)

            Return `n` such that ``self^n == 1``.

            Only `\\pm 1` have finite multiplicative order.

            EXAMPLES::

                sage: RIF(1).multiplicative_order()
                1
                sage: RIF(-1).multiplicative_order()
                2
                sage: RIF(3).multiplicative_order()
                +Infinity"""
        @overload
        def overlaps(self, RealIntervalFieldElementother) -> Any:
            """RealIntervalFieldElement.overlaps(self, RealIntervalFieldElement other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4050)

            Return ``True`` if ``self`` and ``other`` are intervals with at least one
            value in common. For intervals ``a`` and ``b``, we have
            ``a.overlaps(b)`` iff ``not(a!=b)``.

            EXAMPLES::

                sage: RIF(0, 1).overlaps(RIF(1, 2))
                True
                sage: RIF(1, 2).overlaps(RIF(0, 1))
                True
                sage: RIF(0, 1).overlaps(RIF(2, 3))
                False
                sage: RIF(2, 3).overlaps(RIF(0, 1))
                False
                sage: RIF(0, 3).overlaps(RIF(1, 2))
                True
                sage: RIF(0, 2).overlaps(RIF(1, 3))
                True"""
        @overload
        def overlaps(self, b) -> Any:
            """RealIntervalFieldElement.overlaps(self, RealIntervalFieldElement other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4050)

            Return ``True`` if ``self`` and ``other`` are intervals with at least one
            value in common. For intervals ``a`` and ``b``, we have
            ``a.overlaps(b)`` iff ``not(a!=b)``.

            EXAMPLES::

                sage: RIF(0, 1).overlaps(RIF(1, 2))
                True
                sage: RIF(1, 2).overlaps(RIF(0, 1))
                True
                sage: RIF(0, 1).overlaps(RIF(2, 3))
                False
                sage: RIF(2, 3).overlaps(RIF(0, 1))
                False
                sage: RIF(0, 3).overlaps(RIF(1, 2))
                True
                sage: RIF(0, 2).overlaps(RIF(1, 3))
                True"""
        def prec(self, *args, **kwargs):
            """RealIntervalFieldElement.precision(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

            Return the precision of ``self``.

            EXAMPLES::

                sage: RIF(2.1).precision()
                53
                sage: RealIntervalField(200)(2.1).precision()
                200"""
        @overload
        def precision(self) -> Any:
            """RealIntervalFieldElement.precision(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

            Return the precision of ``self``.

            EXAMPLES::

                sage: RIF(2.1).precision()
                53
                sage: RealIntervalField(200)(2.1).precision()
                200"""
        @overload
        def precision(self) -> Any:
            """RealIntervalFieldElement.precision(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

            Return the precision of ``self``.

            EXAMPLES::

                sage: RIF(2.1).precision()
                53
                sage: RealIntervalField(200)(2.1).precision()
                200"""
        @overload
        def precision(self) -> Any:
            """RealIntervalFieldElement.precision(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3003)

            Return the precision of ``self``.

            EXAMPLES::

                sage: RIF(2.1).precision()
                53
                sage: RealIntervalField(200)(2.1).precision()
                200"""
        @overload
        def psi(self) -> Any:
            """RealIntervalFieldElement.psi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5155)

            Return the digamma function evaluated on ``self``.

            OUTPUT: a :class:`RealIntervalFieldElement`

            EXAMPLES::

                sage: psi_1 = RIF(1).psi()
                sage: psi_1
                -0.577215664901533?
                sage: psi_1.overlaps(-RIF.euler_constant())
                True"""
        @overload
        def psi(self) -> Any:
            """RealIntervalFieldElement.psi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5155)

            Return the digamma function evaluated on ``self``.

            OUTPUT: a :class:`RealIntervalFieldElement`

            EXAMPLES::

                sage: psi_1 = RIF(1).psi()
                sage: psi_1
                -0.577215664901533?
                sage: psi_1.overlaps(-RIF.euler_constant())
                True"""
        @overload
        def real(self) -> Any:
            """RealIntervalFieldElement.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1461)

            Return the real part of this real interval.

            (Since this interval is real, this simply returns itself.)

            .. SEEALSO::

                :meth:`imag`

            EXAMPLES::

                sage: RIF(1.2465).real() == RIF(1.2465)
                True"""
        @overload
        def real(self) -> Any:
            """RealIntervalFieldElement.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1461)

            Return the real part of this real interval.

            (Since this interval is real, this simply returns itself.)

            .. SEEALSO::

                :meth:`imag`

            EXAMPLES::

                sage: RIF(1.2465).real() == RIF(1.2465)
                True"""
        @overload
        def relative_diameter(self) -> Any:
            """RealIntervalFieldElement.relative_diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2404)

            The relative diameter of this interval (for `[a .. b]`, this is
            `(b-a)/((a+b)/2)`), rounded upward, as a :class:`RealNumber`.

            EXAMPLES::

                sage: RIF(1, pi).relative_diameter()                                        # needs sage.symbolic
                1.03418797197910"""
        @overload
        def relative_diameter(self) -> Any:
            """RealIntervalFieldElement.relative_diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2404)

            The relative diameter of this interval (for `[a .. b]`, this is
            `(b-a)/((a+b)/2)`), rounded upward, as a :class:`RealNumber`.

            EXAMPLES::

                sage: RIF(1, pi).relative_diameter()                                        # needs sage.symbolic
                1.03418797197910"""
        def round(self) -> Any:
            """RealIntervalFieldElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3097)

            Return the nearest integer of this interval as an interval.

            .. SEEALSO::

                - :meth:`unique_round` -- return the round as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards `-\\infty`
                - :meth:`ceil` -- truncation towards `+\\infty`
                - :meth:`trunc` -- truncation towards `0`

            EXAMPLES::

                sage: RIF(7.2, 7.3).round()
                7
                sage: RIF(-3.2, -3.1).round()
                -3

            Be careful that the answer is not an integer but an interval::

                sage: RIF(2.2, 2.3).round().parent()
                Real Interval Field with 53 bits of precision

            And in some cases, the lower and upper bounds of this interval do not
            agree::

                sage: r = RIF(2.5, 3.5).round()
                sage: r
                4.?
                sage: r.lower()
                3.00000000000000
                sage: r.upper()
                4.00000000000000"""
        @overload
        def sec(self) -> Any:
            """RealIntervalFieldElement.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4894)

            Return the secant of this number.

            EXAMPLES::

                sage: RealIntervalField(100)(2).sec()
                -2.40299796172238098975460040142?"""
        @overload
        def sec(self) -> Any:
            """RealIntervalFieldElement.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4894)

            Return the secant of this number.

            EXAMPLES::

                sage: RealIntervalField(100)(2).sec()
                -2.40299796172238098975460040142?"""
        @overload
        def sech(self) -> Any:
            """RealIntervalFieldElement.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4927)

            Return the hyperbolic secant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).sech()
                0.265802228834079692120862739820?"""
        @overload
        def sech(self) -> Any:
            """RealIntervalFieldElement.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4927)

            Return the hyperbolic secant of ``self``.

            EXAMPLES::

                sage: RealIntervalField(100)(2).sech()
                0.265802228834079692120862739820?"""
        @overload
        def simplest_rational(self, low_open=..., high_open=...) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self, high_open=...) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self, high_open=...) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def simplest_rational(self) -> Any:
            """RealIntervalFieldElement.simplest_rational(self, low_open=False, high_open=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3596)

            Return the simplest rational in this interval. Given rationals
            `a / b` and `c / d` (both in lowest terms), the former is simpler if
            `b<d` or if `b = d` and `|a| < |c|`.

            If optional parameters ``low_open`` or ``high_open`` are ``True``,
            then treat this as an open interval on that end.

            EXAMPLES::

                sage: RealIntervalField(10)(pi).simplest_rational()                         # needs sage.symbolic
                22/7
                sage: RealIntervalField(20)(pi).simplest_rational()                         # needs sage.symbolic
                355/113
                sage: RIF(0.123, 0.567).simplest_rational()
                1/2
                sage: RIF(RR(1/3).nextabove(), RR(3/7)).simplest_rational()
                2/5
                sage: RIF(1234/567).simplest_rational()
                1234/567
                sage: RIF(-8765/432).simplest_rational()
                -8765/432
                sage: RIF(-1.234, 0.003).simplest_rational()
                0
                sage: RIF(RR(1/3)).simplest_rational()
                6004799503160661/18014398509481984
                sage: RIF(RR(1/3)).simplest_rational(high_open=True)
                Traceback (most recent call last):
                ...
                ValueError: simplest_rational() on open, empty interval
                sage: RIF(1/3, 1/2).simplest_rational()
                1/2
                sage: RIF(1/3, 1/2).simplest_rational(high_open=True)
                1/3
                sage: phi = ((RealIntervalField(500)(5).sqrt() + 1)/2)
                sage: phi.simplest_rational() == fibonacci(362)/fibonacci(361)
                True"""
        @overload
        def sin(self) -> Any:
            """RealIntervalFieldElement.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4668)

            Return the sine of ``self``.

            EXAMPLES::

                sage: R = RealIntervalField(100)
                sage: R(2).sin()
                0.909297426825681695396019865912?"""
        @overload
        def sin(self) -> Any:
            """RealIntervalFieldElement.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4668)

            Return the sine of ``self``.

            EXAMPLES::

                sage: R = RealIntervalField(100)
                sage: R(2).sin()
                0.909297426825681695396019865912?"""
        @overload
        def sinh(self) -> Any:
            """RealIntervalFieldElement.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4806)

            Return the hyperbolic sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/12
                sage: q.sinh()
                0.2648002276022707?"""
        @overload
        def sinh(self) -> Any:
            """RealIntervalFieldElement.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4806)

            Return the hyperbolic sine of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/12
                sage: q.sinh()
                0.2648002276022707?"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def sqrt(self) -> Any:
            """RealIntervalFieldElement.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4351)

            Return a square root of ``self``. Raises an error if ``self`` is
            nonpositive.

            If you use :meth:`square_root()` then an interval will always be
            returned (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(4.0)
                sage: r.sqrt()
                2
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RIF(4344)
                sage: r.sqrt()
                65.90902821313633?
                sage: r.sqrt()^2 == r
                False
                sage: r in r.sqrt()^2
                True
                sage: r.sqrt()^2 - r
                0.?e-11
                sage: (r.sqrt()^2 - r).str(style='brackets')
                '[-9.0949470177292824e-13 .. 1.8189894035458565e-12]'

            ::

                sage: r = RIF(-2.0)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0

            ::

                sage: r = RIF(-2, 2)
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=0.?e1) is not >= 0"""
        @overload
        def square(self) -> Any:
            """RealIntervalFieldElement.square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

            Return the square of ``self``.

            .. NOTE::

                Squaring an interval is different than multiplying it by itself,
                because the square can never be negative.

            EXAMPLES::

                sage: RIF(1, 2).square().str(style='brackets')
                '[1.0000000000000000 .. 4.0000000000000000]'
                sage: RIF(-1, 1).square().str(style='brackets')
                '[0.0000000000000000 .. 1.0000000000000000]'
                sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
                '[-1.0000000000000000 .. 1.0000000000000000]'"""
        @overload
        def square(self) -> Any:
            """RealIntervalFieldElement.square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

            Return the square of ``self``.

            .. NOTE::

                Squaring an interval is different than multiplying it by itself,
                because the square can never be negative.

            EXAMPLES::

                sage: RIF(1, 2).square().str(style='brackets')
                '[1.0000000000000000 .. 4.0000000000000000]'
                sage: RIF(-1, 1).square().str(style='brackets')
                '[0.0000000000000000 .. 1.0000000000000000]'
                sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
                '[-1.0000000000000000 .. 1.0000000000000000]'"""
        @overload
        def square(self) -> Any:
            """RealIntervalFieldElement.square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2895)

            Return the square of ``self``.

            .. NOTE::

                Squaring an interval is different than multiplying it by itself,
                because the square can never be negative.

            EXAMPLES::

                sage: RIF(1, 2).square().str(style='brackets')
                '[1.0000000000000000 .. 4.0000000000000000]'
                sage: RIF(-1, 1).square().str(style='brackets')
                '[0.0000000000000000 .. 1.0000000000000000]'
                sage: (RIF(-1, 1) * RIF(-1, 1)).str(style='brackets')
                '[-1.0000000000000000 .. 1.0000000000000000]'"""
        @overload
        def square_root(self) -> Any:
            """RealIntervalFieldElement.square_root(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4401)

            Return a square root of ``self``. An interval will always be returned
            (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(-2.0)
                sage: r.square_root()
                [.. NaN ..]
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0"""
        @overload
        def square_root(self) -> Any:
            """RealIntervalFieldElement.square_root(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4401)

            Return a square root of ``self``. An interval will always be returned
            (though it will be ``NaN`` if ``self`` is nonpositive).

            EXAMPLES::

                sage: r = RIF(-2.0)
                sage: r.square_root()
                [.. NaN ..]
                sage: r.sqrt()
                Traceback (most recent call last):
                ...
                ValueError: self (=-2) is not >= 0"""
        @overload
        def str(self, intbase=..., style=..., no_sci=..., e=..., error_digits=...) -> Any:
            '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

            Return a string representation of ``self``.

            INPUT:

            - ``base`` -- base for output

            - ``style`` -- the printing style; either ``\'brackets\'`` or
              ``\'question\'`` (or ``None``, to use the current default)

            - ``no_sci`` -- if ``True`` do not print using scientific
              notation; if ``False`` print with scientific notation; if ``None``
              (the default), print how the parent prints.

            - ``e`` -- symbol used in scientific notation

            - ``error_digits`` -- the number of digits of error to
              print, in ``\'question\'`` style

            We support two different styles of printing; ``\'question\'`` style and
            ``\'brackets\'`` style. In question style (the default), we print the
            "known correct" part of the number, followed by a question mark::

                sage: RIF(pi).str()                                                         # needs sage.symbolic
                \'3.141592653589794?\'
                sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
                \'3.142?\'
                sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
                \'3.142?\'

            However, if the interval is precisely equal to some integer that\'s
            not too large, we just return that integer::

                sage: RIF(-42).str()
                \'-42\'
                sage: RIF(0).str()
                \'0\'
                sage: RIF(12^5).str(base=3)
                \'110122100000\'

            Very large integers, however, revert to the normal question-style
            printing::

                sage: RIF(3^7).str()
                \'2187\'
                sage: RIF(3^7 * 2^256).str()
                \'2.5323729916201052?e80\'

            In brackets style, we print the lower and upper bounds of the
            interval within brackets::

                sage: RIF(237/16).str(style=\'brackets\')
                \'[14.812500000000000 .. 14.812500000000000]\'

            Note that the lower bound is rounded down, and the upper bound is
            rounded up. So even if the lower and upper bounds are equal, they
            may print differently. (This is done so that the printed
            representation of the interval contains all the numbers in the
            internal binary interval.)

            For instance, we find the best 10-bit floating point representation
            of ``1/3``::

                sage: RR10 = RealField(10)
                sage: RR(RR10(1/3))
                0.333496093750000

            And we see that the point interval containing only this
            floating-point number prints as a wider decimal interval, that does
            contain the number::

                sage: RIF10 = RealIntervalField(10)
                sage: RIF10(RR10(1/3)).str(style=\'brackets\')
                \'[0.33349 .. 0.33350]\'

            We always use brackets style for ``NaN`` and infinities::

                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]

            Let\'s take a closer, formal look at the question style. In its full
            generality, a number printed in the question style looks like:

            MANTISSA ?ERROR eEXPONENT

            (without the spaces). The "eEXPONENT" part is optional; if it is
            missing, then the exponent is 0. (If the base is greater than 10,
            then the exponent separator is "@" instead of "e".)

            The "ERROR" is optional; if it is missing, then the error is 1.

            The mantissa is printed in base `b`, and always contains a
            decimal point (also known as a radix point, in bases other than
            10). (The error and exponent are always printed in base 10.)

            We define the "precision" of a floating-point printed
            representation to be the positional value of the last digit of the
            mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
            in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
            is `10^{-2}`. This precision will always be `10^k`
            for some `k` (or, for an arbitrary base `b`, `b^k`).

            Then the interval is contained in the interval:

            .. MATH::

                \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
                .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
                b^k

            To control the printing, we can specify a maximum number of error
            digits. The default is 0, which means that we do not print an error
            at all (so that the error is always the default, 1).

            Now, consider the precisions needed to represent the endpoints
            (this is the precision that would be produced by
            ``v.lower().str(no_sci=False)``). Our
            result is no more precise than the less precise endpoint, and is
            sufficiently imprecise that the error can be represented with the
            given number of decimal digits. Our result is the most precise
            possible result, given these restrictions. When there are two
            possible results of equal precision and with the same error width,
            then we pick the one which is farther from zero. (For instance,
            ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
            ``62.?62``. We prefer the latter because it makes it clear that the
            interval is known not to be negative.)

            EXAMPLES::

                sage: a = RIF(59/27); a
                2.185185185185186?
                sage: a.str()
                \'2.185185185185186?\'
                sage: a.str(style=\'brackets\')
                \'[2.1851851851851851 .. 2.1851851851851856]\'
                sage: a.str(16)
                \'2.2f684bda12f69?\'
                sage: a.str(no_sci=False)
                \'2.185185185185186?e0\'
                sage: pi_appr = RIF(pi, 22/7)
                sage: pi_appr.str(style=\'brackets\')
                \'[3.1415926535897931 .. 3.1428571428571433]\'
                sage: pi_appr.str()
                \'3.142?\'
                sage: pi_appr.str(error_digits=1)
                \'3.1422?7\'
                sage: pi_appr.str(error_digits=2)
                \'3.14223?64\'
                sage: pi_appr.str(base=36)
                \'3.6?\'
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]
                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
                [-infinity .. 3.1415926535897936]
                sage: RealIntervalField(210)(3).sqrt()
                1.732050807568877293527446341505872366942805253810380628055806980?
                sage: RealIntervalField(210)(RIF(3).sqrt())
                1.732050807568878?
                sage: RIF(3).sqrt()
                1.732050807568878?
                sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
                1.?e-71

            TESTS:

            Check that :issue:`13634` is fixed::

                sage: RIF(0.025)
                0.025000000000000002?
                sage: RIF.scientific_notation(True)
                sage: RIF(0.025)
                2.5000000000000002?e-2
                sage: RIF.scientific_notation(False)
                sage: RIF(0.025)
                0.025000000000000002?'''
        @overload
        def str(self) -> Any:
            '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

            Return a string representation of ``self``.

            INPUT:

            - ``base`` -- base for output

            - ``style`` -- the printing style; either ``\'brackets\'`` or
              ``\'question\'`` (or ``None``, to use the current default)

            - ``no_sci`` -- if ``True`` do not print using scientific
              notation; if ``False`` print with scientific notation; if ``None``
              (the default), print how the parent prints.

            - ``e`` -- symbol used in scientific notation

            - ``error_digits`` -- the number of digits of error to
              print, in ``\'question\'`` style

            We support two different styles of printing; ``\'question\'`` style and
            ``\'brackets\'`` style. In question style (the default), we print the
            "known correct" part of the number, followed by a question mark::

                sage: RIF(pi).str()                                                         # needs sage.symbolic
                \'3.141592653589794?\'
                sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
                \'3.142?\'
                sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
                \'3.142?\'

            However, if the interval is precisely equal to some integer that\'s
            not too large, we just return that integer::

                sage: RIF(-42).str()
                \'-42\'
                sage: RIF(0).str()
                \'0\'
                sage: RIF(12^5).str(base=3)
                \'110122100000\'

            Very large integers, however, revert to the normal question-style
            printing::

                sage: RIF(3^7).str()
                \'2187\'
                sage: RIF(3^7 * 2^256).str()
                \'2.5323729916201052?e80\'

            In brackets style, we print the lower and upper bounds of the
            interval within brackets::

                sage: RIF(237/16).str(style=\'brackets\')
                \'[14.812500000000000 .. 14.812500000000000]\'

            Note that the lower bound is rounded down, and the upper bound is
            rounded up. So even if the lower and upper bounds are equal, they
            may print differently. (This is done so that the printed
            representation of the interval contains all the numbers in the
            internal binary interval.)

            For instance, we find the best 10-bit floating point representation
            of ``1/3``::

                sage: RR10 = RealField(10)
                sage: RR(RR10(1/3))
                0.333496093750000

            And we see that the point interval containing only this
            floating-point number prints as a wider decimal interval, that does
            contain the number::

                sage: RIF10 = RealIntervalField(10)
                sage: RIF10(RR10(1/3)).str(style=\'brackets\')
                \'[0.33349 .. 0.33350]\'

            We always use brackets style for ``NaN`` and infinities::

                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]

            Let\'s take a closer, formal look at the question style. In its full
            generality, a number printed in the question style looks like:

            MANTISSA ?ERROR eEXPONENT

            (without the spaces). The "eEXPONENT" part is optional; if it is
            missing, then the exponent is 0. (If the base is greater than 10,
            then the exponent separator is "@" instead of "e".)

            The "ERROR" is optional; if it is missing, then the error is 1.

            The mantissa is printed in base `b`, and always contains a
            decimal point (also known as a radix point, in bases other than
            10). (The error and exponent are always printed in base 10.)

            We define the "precision" of a floating-point printed
            representation to be the positional value of the last digit of the
            mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
            in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
            is `10^{-2}`. This precision will always be `10^k`
            for some `k` (or, for an arbitrary base `b`, `b^k`).

            Then the interval is contained in the interval:

            .. MATH::

                \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
                .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
                b^k

            To control the printing, we can specify a maximum number of error
            digits. The default is 0, which means that we do not print an error
            at all (so that the error is always the default, 1).

            Now, consider the precisions needed to represent the endpoints
            (this is the precision that would be produced by
            ``v.lower().str(no_sci=False)``). Our
            result is no more precise than the less precise endpoint, and is
            sufficiently imprecise that the error can be represented with the
            given number of decimal digits. Our result is the most precise
            possible result, given these restrictions. When there are two
            possible results of equal precision and with the same error width,
            then we pick the one which is farther from zero. (For instance,
            ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
            ``62.?62``. We prefer the latter because it makes it clear that the
            interval is known not to be negative.)

            EXAMPLES::

                sage: a = RIF(59/27); a
                2.185185185185186?
                sage: a.str()
                \'2.185185185185186?\'
                sage: a.str(style=\'brackets\')
                \'[2.1851851851851851 .. 2.1851851851851856]\'
                sage: a.str(16)
                \'2.2f684bda12f69?\'
                sage: a.str(no_sci=False)
                \'2.185185185185186?e0\'
                sage: pi_appr = RIF(pi, 22/7)
                sage: pi_appr.str(style=\'brackets\')
                \'[3.1415926535897931 .. 3.1428571428571433]\'
                sage: pi_appr.str()
                \'3.142?\'
                sage: pi_appr.str(error_digits=1)
                \'3.1422?7\'
                sage: pi_appr.str(error_digits=2)
                \'3.14223?64\'
                sage: pi_appr.str(base=36)
                \'3.6?\'
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]
                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
                [-infinity .. 3.1415926535897936]
                sage: RealIntervalField(210)(3).sqrt()
                1.732050807568877293527446341505872366942805253810380628055806980?
                sage: RealIntervalField(210)(RIF(3).sqrt())
                1.732050807568878?
                sage: RIF(3).sqrt()
                1.732050807568878?
                sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
                1.?e-71

            TESTS:

            Check that :issue:`13634` is fixed::

                sage: RIF(0.025)
                0.025000000000000002?
                sage: RIF.scientific_notation(True)
                sage: RIF(0.025)
                2.5000000000000002?e-2
                sage: RIF.scientific_notation(False)
                sage: RIF(0.025)
                0.025000000000000002?'''
        @overload
        def str(self) -> Any:
            '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

            Return a string representation of ``self``.

            INPUT:

            - ``base`` -- base for output

            - ``style`` -- the printing style; either ``\'brackets\'`` or
              ``\'question\'`` (or ``None``, to use the current default)

            - ``no_sci`` -- if ``True`` do not print using scientific
              notation; if ``False`` print with scientific notation; if ``None``
              (the default), print how the parent prints.

            - ``e`` -- symbol used in scientific notation

            - ``error_digits`` -- the number of digits of error to
              print, in ``\'question\'`` style

            We support two different styles of printing; ``\'question\'`` style and
            ``\'brackets\'`` style. In question style (the default), we print the
            "known correct" part of the number, followed by a question mark::

                sage: RIF(pi).str()                                                         # needs sage.symbolic
                \'3.141592653589794?\'
                sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
                \'3.142?\'
                sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
                \'3.142?\'

            However, if the interval is precisely equal to some integer that\'s
            not too large, we just return that integer::

                sage: RIF(-42).str()
                \'-42\'
                sage: RIF(0).str()
                \'0\'
                sage: RIF(12^5).str(base=3)
                \'110122100000\'

            Very large integers, however, revert to the normal question-style
            printing::

                sage: RIF(3^7).str()
                \'2187\'
                sage: RIF(3^7 * 2^256).str()
                \'2.5323729916201052?e80\'

            In brackets style, we print the lower and upper bounds of the
            interval within brackets::

                sage: RIF(237/16).str(style=\'brackets\')
                \'[14.812500000000000 .. 14.812500000000000]\'

            Note that the lower bound is rounded down, and the upper bound is
            rounded up. So even if the lower and upper bounds are equal, they
            may print differently. (This is done so that the printed
            representation of the interval contains all the numbers in the
            internal binary interval.)

            For instance, we find the best 10-bit floating point representation
            of ``1/3``::

                sage: RR10 = RealField(10)
                sage: RR(RR10(1/3))
                0.333496093750000

            And we see that the point interval containing only this
            floating-point number prints as a wider decimal interval, that does
            contain the number::

                sage: RIF10 = RealIntervalField(10)
                sage: RIF10(RR10(1/3)).str(style=\'brackets\')
                \'[0.33349 .. 0.33350]\'

            We always use brackets style for ``NaN`` and infinities::

                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]

            Let\'s take a closer, formal look at the question style. In its full
            generality, a number printed in the question style looks like:

            MANTISSA ?ERROR eEXPONENT

            (without the spaces). The "eEXPONENT" part is optional; if it is
            missing, then the exponent is 0. (If the base is greater than 10,
            then the exponent separator is "@" instead of "e".)

            The "ERROR" is optional; if it is missing, then the error is 1.

            The mantissa is printed in base `b`, and always contains a
            decimal point (also known as a radix point, in bases other than
            10). (The error and exponent are always printed in base 10.)

            We define the "precision" of a floating-point printed
            representation to be the positional value of the last digit of the
            mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
            in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
            is `10^{-2}`. This precision will always be `10^k`
            for some `k` (or, for an arbitrary base `b`, `b^k`).

            Then the interval is contained in the interval:

            .. MATH::

                \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
                .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
                b^k

            To control the printing, we can specify a maximum number of error
            digits. The default is 0, which means that we do not print an error
            at all (so that the error is always the default, 1).

            Now, consider the precisions needed to represent the endpoints
            (this is the precision that would be produced by
            ``v.lower().str(no_sci=False)``). Our
            result is no more precise than the less precise endpoint, and is
            sufficiently imprecise that the error can be represented with the
            given number of decimal digits. Our result is the most precise
            possible result, given these restrictions. When there are two
            possible results of equal precision and with the same error width,
            then we pick the one which is farther from zero. (For instance,
            ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
            ``62.?62``. We prefer the latter because it makes it clear that the
            interval is known not to be negative.)

            EXAMPLES::

                sage: a = RIF(59/27); a
                2.185185185185186?
                sage: a.str()
                \'2.185185185185186?\'
                sage: a.str(style=\'brackets\')
                \'[2.1851851851851851 .. 2.1851851851851856]\'
                sage: a.str(16)
                \'2.2f684bda12f69?\'
                sage: a.str(no_sci=False)
                \'2.185185185185186?e0\'
                sage: pi_appr = RIF(pi, 22/7)
                sage: pi_appr.str(style=\'brackets\')
                \'[3.1415926535897931 .. 3.1428571428571433]\'
                sage: pi_appr.str()
                \'3.142?\'
                sage: pi_appr.str(error_digits=1)
                \'3.1422?7\'
                sage: pi_appr.str(error_digits=2)
                \'3.14223?64\'
                sage: pi_appr.str(base=36)
                \'3.6?\'
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]
                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
                [-infinity .. 3.1415926535897936]
                sage: RealIntervalField(210)(3).sqrt()
                1.732050807568877293527446341505872366942805253810380628055806980?
                sage: RealIntervalField(210)(RIF(3).sqrt())
                1.732050807568878?
                sage: RIF(3).sqrt()
                1.732050807568878?
                sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
                1.?e-71

            TESTS:

            Check that :issue:`13634` is fixed::

                sage: RIF(0.025)
                0.025000000000000002?
                sage: RIF.scientific_notation(True)
                sage: RIF(0.025)
                2.5000000000000002?e-2
                sage: RIF.scientific_notation(False)
                sage: RIF(0.025)
                0.025000000000000002?'''
        @overload
        def str(self, style=...) -> Any:
            '''RealIntervalFieldElement.str(self, int base=10, style=None, no_sci=None, e=None, error_digits=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1500)

            Return a string representation of ``self``.

            INPUT:

            - ``base`` -- base for output

            - ``style`` -- the printing style; either ``\'brackets\'`` or
              ``\'question\'`` (or ``None``, to use the current default)

            - ``no_sci`` -- if ``True`` do not print using scientific
              notation; if ``False`` print with scientific notation; if ``None``
              (the default), print how the parent prints.

            - ``e`` -- symbol used in scientific notation

            - ``error_digits`` -- the number of digits of error to
              print, in ``\'question\'`` style

            We support two different styles of printing; ``\'question\'`` style and
            ``\'brackets\'`` style. In question style (the default), we print the
            "known correct" part of the number, followed by a question mark::

                sage: RIF(pi).str()                                                         # needs sage.symbolic
                \'3.141592653589794?\'
                sage: RIF(pi, 22/7).str()                                                   # needs sage.symbolic
                \'3.142?\'
                sage: RIF(pi, 22/7).str(style=\'question\')                                   # needs sage.symbolic
                \'3.142?\'

            However, if the interval is precisely equal to some integer that\'s
            not too large, we just return that integer::

                sage: RIF(-42).str()
                \'-42\'
                sage: RIF(0).str()
                \'0\'
                sage: RIF(12^5).str(base=3)
                \'110122100000\'

            Very large integers, however, revert to the normal question-style
            printing::

                sage: RIF(3^7).str()
                \'2187\'
                sage: RIF(3^7 * 2^256).str()
                \'2.5323729916201052?e80\'

            In brackets style, we print the lower and upper bounds of the
            interval within brackets::

                sage: RIF(237/16).str(style=\'brackets\')
                \'[14.812500000000000 .. 14.812500000000000]\'

            Note that the lower bound is rounded down, and the upper bound is
            rounded up. So even if the lower and upper bounds are equal, they
            may print differently. (This is done so that the printed
            representation of the interval contains all the numbers in the
            internal binary interval.)

            For instance, we find the best 10-bit floating point representation
            of ``1/3``::

                sage: RR10 = RealField(10)
                sage: RR(RR10(1/3))
                0.333496093750000

            And we see that the point interval containing only this
            floating-point number prints as a wider decimal interval, that does
            contain the number::

                sage: RIF10 = RealIntervalField(10)
                sage: RIF10(RR10(1/3)).str(style=\'brackets\')
                \'[0.33349 .. 0.33350]\'

            We always use brackets style for ``NaN`` and infinities::

                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]

            Let\'s take a closer, formal look at the question style. In its full
            generality, a number printed in the question style looks like:

            MANTISSA ?ERROR eEXPONENT

            (without the spaces). The "eEXPONENT" part is optional; if it is
            missing, then the exponent is 0. (If the base is greater than 10,
            then the exponent separator is "@" instead of "e".)

            The "ERROR" is optional; if it is missing, then the error is 1.

            The mantissa is printed in base `b`, and always contains a
            decimal point (also known as a radix point, in bases other than
            10). (The error and exponent are always printed in base 10.)

            We define the "precision" of a floating-point printed
            representation to be the positional value of the last digit of the
            mantissa. For instance, in ``2.7?e5``, the precision is `10^4`;
            in ``8.?``, the precision is `10^0`; and in ``9.35?`` the precision
            is `10^{-2}`. This precision will always be `10^k`
            for some `k` (or, for an arbitrary base `b`, `b^k`).

            Then the interval is contained in the interval:

            .. MATH::

                \\text{mantissa} \\cdot b^{\\text{exponent}} - \\text{error} \\cdot b^k
                .. \\text{mantissa} \\cdot b^{\\text{exponent}} + \\text{error} \\cdot
                b^k

            To control the printing, we can specify a maximum number of error
            digits. The default is 0, which means that we do not print an error
            at all (so that the error is always the default, 1).

            Now, consider the precisions needed to represent the endpoints
            (this is the precision that would be produced by
            ``v.lower().str(no_sci=False)``). Our
            result is no more precise than the less precise endpoint, and is
            sufficiently imprecise that the error can be represented with the
            given number of decimal digits. Our result is the most precise
            possible result, given these restrictions. When there are two
            possible results of equal precision and with the same error width,
            then we pick the one which is farther from zero. (For instance,
            ``RIF(0, 123)`` with two error digits could print as ``61.?62`` or
            ``62.?62``. We prefer the latter because it makes it clear that the
            interval is known not to be negative.)

            EXAMPLES::

                sage: a = RIF(59/27); a
                2.185185185185186?
                sage: a.str()
                \'2.185185185185186?\'
                sage: a.str(style=\'brackets\')
                \'[2.1851851851851851 .. 2.1851851851851856]\'
                sage: a.str(16)
                \'2.2f684bda12f69?\'
                sage: a.str(no_sci=False)
                \'2.185185185185186?e0\'
                sage: pi_appr = RIF(pi, 22/7)
                sage: pi_appr.str(style=\'brackets\')
                \'[3.1415926535897931 .. 3.1428571428571433]\'
                sage: pi_appr.str()
                \'3.142?\'
                sage: pi_appr.str(error_digits=1)
                \'3.1422?7\'
                sage: pi_appr.str(error_digits=2)
                \'3.14223?64\'
                sage: pi_appr.str(base=36)
                \'3.6?\'
                sage: RIF(NaN)                                                              # needs sage.symbolic
                [.. NaN ..]
                sage: RIF(pi, infinity)                                                     # needs sage.symbolic
                [3.1415926535897931 .. +infinity]
                sage: RIF(-infinity, pi)                                                    # needs sage.symbolic
                [-infinity .. 3.1415926535897936]
                sage: RealIntervalField(210)(3).sqrt()
                1.732050807568877293527446341505872366942805253810380628055806980?
                sage: RealIntervalField(210)(RIF(3).sqrt())
                1.732050807568878?
                sage: RIF(3).sqrt()
                1.732050807568878?
                sage: RIF(0, 3^-150)                                                        # needs sage.symbolic
                1.?e-71

            TESTS:

            Check that :issue:`13634` is fixed::

                sage: RIF(0.025)
                0.025000000000000002?
                sage: RIF.scientific_notation(True)
                sage: RIF(0.025)
                2.5000000000000002?e-2
                sage: RIF.scientific_notation(False)
                sage: RIF(0.025)
                0.025000000000000002?'''
        @overload
        def tan(self) -> Any:
            """RealIntervalFieldElement.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

            Return the tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/3
                sage: q.tan()
                1.732050807568877?
                sage: q = RIF.pi()/6
                sage: q.tan()
                0.577350269189626?"""
        @overload
        def tan(self) -> Any:
            """RealIntervalFieldElement.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

            Return the tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/3
                sage: q.tan()
                1.732050807568877?
                sage: q = RIF.pi()/6
                sage: q.tan()
                0.577350269189626?"""
        @overload
        def tan(self) -> Any:
            """RealIntervalFieldElement.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4684)

            Return the tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/3
                sage: q.tan()
                1.732050807568877?
                sage: q = RIF.pi()/6
                sage: q.tan()
                0.577350269189626?"""
        @overload
        def tanh(self) -> Any:
            """RealIntervalFieldElement.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4822)

            Return the hyperbolic tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/11
                sage: q.tanh()
                0.2780794292958503?"""
        @overload
        def tanh(self) -> Any:
            """RealIntervalFieldElement.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4822)

            Return the hyperbolic tangent of ``self``.

            EXAMPLES::

                sage: q = RIF.pi()/11
                sage: q.tanh()
                0.2780794292958503?"""
        def trunc(self) -> Any:
            """RealIntervalFieldElement.trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3134)

            Return the truncation of this interval as an interval.

            The truncation of `x` is the floor of `x` if `x` is nonnegative or the
            ceil of `x` if `x` is negative.

            .. SEEALSO::

                - :meth:`unique_trunc` -- return the trunc as an integer if it is
                  unique and raises a :exc:`ValueError` otherwise
                - :meth:`floor` -- truncation towards `-\\infty`
                - :meth:`ceil` -- truncation towards `+\\infty`
                - :meth:`round` -- rounding

            EXAMPLES::

                sage: RIF(2.3, 2.7).trunc()
                2
                sage: parent(_)
                Real Interval Field with 53 bits of precision

                sage: RIF(-0.9, 0.9).trunc()
                0
                sage: RIF(-7.5, -7.3).trunc()
                -7

            In the above example, the obtained interval contains only one element.
            But on the following it is not the case anymore::

                sage: r = RIF(2.99, 3.01).trunc()
                sage: r.upper()
                3.00000000000000
                sage: r.lower()
                2.00000000000000"""
        @overload
        def union(self, other) -> Any:
            """RealIntervalFieldElement.union(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4103)

            Return the union of two intervals, or of an interval and a real
            number (more precisely, the convex hull).

            EXAMPLES::

                sage: RIF(1, 2).union(RIF(pi, 22/7)).str(style='brackets')
                '[1.0000000000000000 .. 3.1428571428571433]'
                sage: RIF(1, 2).union(pi).str(style='brackets')
                '[1.0000000000000000 .. 3.1415926535897936]'
                sage: RIF(1).union(RIF(0, 2)).str(style='brackets')
                '[0.0000000000000000 .. 2.0000000000000000]'
                sage: RIF(1).union(RIF(-1)).str(style='brackets')
                '[-1.0000000000000000 .. 1.0000000000000000]'"""
        @overload
        def union(self, pi) -> Any:
            """RealIntervalFieldElement.union(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4103)

            Return the union of two intervals, or of an interval and a real
            number (more precisely, the convex hull).

            EXAMPLES::

                sage: RIF(1, 2).union(RIF(pi, 22/7)).str(style='brackets')
                '[1.0000000000000000 .. 3.1428571428571433]'
                sage: RIF(1, 2).union(pi).str(style='brackets')
                '[1.0000000000000000 .. 3.1415926535897936]'
                sage: RIF(1).union(RIF(0, 2)).str(style='brackets')
                '[0.0000000000000000 .. 2.0000000000000000]'
                sage: RIF(1).union(RIF(-1)).str(style='brackets')
                '[-1.0000000000000000 .. 1.0000000000000000]'"""
        @overload
        def unique_ceil(self) -> Any:
            """RealIntervalFieldElement.unique_ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

            Return the unique ceiling of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`ceil` -- return the ceil as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
                4
                sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
                315
                sage: RIF(100, 200).unique_ceil()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique ceil"""
        @overload
        def unique_ceil(self) -> Any:
            """RealIntervalFieldElement.unique_ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

            Return the unique ceiling of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`ceil` -- return the ceil as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
                4
                sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
                315
                sage: RIF(100, 200).unique_ceil()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique ceil"""
        @overload
        def unique_ceil(self) -> Any:
            """RealIntervalFieldElement.unique_ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

            Return the unique ceiling of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`ceil` -- return the ceil as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
                4
                sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
                315
                sage: RIF(100, 200).unique_ceil()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique ceil"""
        @overload
        def unique_ceil(self) -> Any:
            """RealIntervalFieldElement.unique_ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3421)

            Return the unique ceiling of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`ceil` -- return the ceil as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_ceil()                                                 # needs sage.symbolic
                4
                sage: RIF(100*pi).unique_ceil()                                             # needs sage.symbolic
                315
                sage: RIF(100, 200).unique_ceil()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique ceil"""
        @overload
        def unique_floor(self) -> Any:
            """RealIntervalFieldElement.unique_floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

            Return the unique floor of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`floor` -- return the floor as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
                3
                sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
                314
                sage: RIF(100, 200).unique_floor()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique floor"""
        @overload
        def unique_floor(self) -> Any:
            """RealIntervalFieldElement.unique_floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

            Return the unique floor of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`floor` -- return the floor as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
                3
                sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
                314
                sage: RIF(100, 200).unique_floor()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique floor"""
        @overload
        def unique_floor(self) -> Any:
            """RealIntervalFieldElement.unique_floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

            Return the unique floor of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`floor` -- return the floor as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
                3
                sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
                314
                sage: RIF(100, 200).unique_floor()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique floor"""
        @overload
        def unique_floor(self) -> Any:
            """RealIntervalFieldElement.unique_floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3392)

            Return the unique floor of this interval, if it is well defined,
            otherwise raise a :exc:`ValueError`.

            OUTPUT: integer

            .. SEEALSO::

                :meth:`floor` -- return the floor as an interval (and never raise
                error)

            EXAMPLES::

                sage: RIF(pi).unique_floor()                                                # needs sage.symbolic
                3
                sage: RIF(100*pi).unique_floor()                                            # needs sage.symbolic
                314
                sage: RIF(100, 200).unique_floor()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique floor"""
        @overload
        def unique_integer(self) -> Any:
            """RealIntervalFieldElement.unique_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

            Return the unique integer in this interval, if there is exactly one,
            otherwise raise a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains no integer
                sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
                4
                sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains more than one integer
                sage: RIF(100).unique_integer()
                100"""
        @overload
        def unique_integer(self) -> Any:
            """RealIntervalFieldElement.unique_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

            Return the unique integer in this interval, if there is exactly one,
            otherwise raise a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains no integer
                sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
                4
                sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains more than one integer
                sage: RIF(100).unique_integer()
                100"""
        @overload
        def unique_integer(self) -> Any:
            """RealIntervalFieldElement.unique_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

            Return the unique integer in this interval, if there is exactly one,
            otherwise raise a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains no integer
                sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
                4
                sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains more than one integer
                sage: RIF(100).unique_integer()
                100"""
        @overload
        def unique_integer(self) -> Any:
            """RealIntervalFieldElement.unique_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

            Return the unique integer in this interval, if there is exactly one,
            otherwise raise a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains no integer
                sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
                4
                sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains more than one integer
                sage: RIF(100).unique_integer()
                100"""
        @overload
        def unique_integer(self) -> Any:
            """RealIntervalFieldElement.unique_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3544)

            Return the unique integer in this interval, if there is exactly one,
            otherwise raise a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(pi).unique_integer()                                              # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains no integer
                sage: RIF(pi, pi+1).unique_integer()                                        # needs sage.symbolic
                4
                sage: RIF(pi, pi+2).unique_integer()                                        # needs sage.symbolic
                Traceback (most recent call last):
                ...
                ValueError: interval contains more than one integer
                sage: RIF(100).unique_integer()
                100"""
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_round(self) -> Any:
            """RealIntervalFieldElement.unique_round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3450)

             Return the unique round (nearest integer) of this interval,
             if it is well defined, otherwise raise a :exc:`ValueError`.

             OUTPUT: integer

             .. SEEALSO::

                 :meth:`round` -- return the round as an interval (and never raise
                 error)

             EXAMPLES::

                 sage: RIF(pi).unique_round()                                                # needs sage.symbolic
                 3
                 sage: RIF(1000*pi).unique_round()                                           # needs sage.symbolic
                 3142
                 sage: RIF(100, 200).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1.2, 1.7).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(0.7, 1.2).unique_round()
                 1
                 sage: RIF(-pi).unique_round()                                               # needs sage.symbolic
                 -3
                 sage: (RIF(4.5).unique_round(), RIF(-4.5).unique_round())
                 (5, -5)

            TESTS::

                 sage: RIF(-1/2, -1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/2, 1/3).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(-1/3, 1/3).unique_round()
                 0
                 sage: RIF(-1/2, 0).unique_round()
                 Traceback (most recent call last):
                 ...
                 ValueError: interval does not have a unique round (nearest integer)
                 sage: RIF(1/2).unique_round()
                 1
                 sage: RIF(-1/2).unique_round()
                 -1
                 sage: RIF(0).unique_round()
                 0
 """
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_sign(self) -> Any:
            """RealIntervalFieldElement.unique_sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3316)

            Return the sign of this element if it is well defined.

            This method returns `+1` if all elements in this interval are positive,
            `-1` if all of them are negative and `0` if it contains only zero.
            Otherwise it raises a :exc:`ValueError`.

            EXAMPLES::

                sage: RIF(1.2,5.7).unique_sign()
                1
                sage: RIF(-3,-2).unique_sign()
                -1
                sage: RIF(0).unique_sign()
                0
                sage: RIF(0,1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-1,0).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign
                sage: RIF(-0.1, 0.1).unique_sign()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique sign"""
        @overload
        def unique_trunc(self) -> Any:
            """RealIntervalFieldElement.unique_trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

            Return the nearest integer toward zero if it is unique, otherwise raise
            a :exc:`ValueError`.

            .. SEEALSO::

                :meth:`trunc` -- return the truncation as an interval (and never
                raise error)

            EXAMPLES::

                sage: RIF(1.3,1.4).unique_trunc()
                1
                sage: RIF(-3.3, -3.2).unique_trunc()
                -3
                sage: RIF(2.9,3.2).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)
                sage: RIF(-3.1,-2.9).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
        @overload
        def unique_trunc(self) -> Any:
            """RealIntervalFieldElement.unique_trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

            Return the nearest integer toward zero if it is unique, otherwise raise
            a :exc:`ValueError`.

            .. SEEALSO::

                :meth:`trunc` -- return the truncation as an interval (and never
                raise error)

            EXAMPLES::

                sage: RIF(1.3,1.4).unique_trunc()
                1
                sage: RIF(-3.3, -3.2).unique_trunc()
                -3
                sage: RIF(2.9,3.2).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)
                sage: RIF(-3.1,-2.9).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
        @overload
        def unique_trunc(self) -> Any:
            """RealIntervalFieldElement.unique_trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

            Return the nearest integer toward zero if it is unique, otherwise raise
            a :exc:`ValueError`.

            .. SEEALSO::

                :meth:`trunc` -- return the truncation as an interval (and never
                raise error)

            EXAMPLES::

                sage: RIF(1.3,1.4).unique_trunc()
                1
                sage: RIF(-3.3, -3.2).unique_trunc()
                -3
                sage: RIF(2.9,3.2).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)
                sage: RIF(-3.1,-2.9).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
        @overload
        def unique_trunc(self) -> Any:
            """RealIntervalFieldElement.unique_trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

            Return the nearest integer toward zero if it is unique, otherwise raise
            a :exc:`ValueError`.

            .. SEEALSO::

                :meth:`trunc` -- return the truncation as an interval (and never
                raise error)

            EXAMPLES::

                sage: RIF(1.3,1.4).unique_trunc()
                1
                sage: RIF(-3.3, -3.2).unique_trunc()
                -3
                sage: RIF(2.9,3.2).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)
                sage: RIF(-3.1,-2.9).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
        @overload
        def unique_trunc(self) -> Any:
            """RealIntervalFieldElement.unique_trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3512)

            Return the nearest integer toward zero if it is unique, otherwise raise
            a :exc:`ValueError`.

            .. SEEALSO::

                :meth:`trunc` -- return the truncation as an interval (and never
                raise error)

            EXAMPLES::

                sage: RIF(1.3,1.4).unique_trunc()
                1
                sage: RIF(-3.3, -3.2).unique_trunc()
                -3
                sage: RIF(2.9,3.2).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)
                sage: RIF(-3.1,-2.9).unique_trunc()
                Traceback (most recent call last):
                ...
                ValueError: interval does not have a unique trunc (nearest integer toward zero)"""
        @overload
        def upper(self, rnd=...) -> Any:
            """RealIntervalFieldElement.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

            Return the upper bound of ``self``.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards plus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().upper().str()
                '3.1417'

            ::

                sage: R = RealIntervalField(13)
                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.upper()
                1.31
                sage: x.upper('RNDU')
                1.31
                sage: x.upper('RNDN')
                1.30
                sage: x.upper('RNDD')
                1.30
                sage: x.upper('RNDZ')
                1.30
                sage: x.upper('RNDA')
                1.31
                sage: x.upper().parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.upper('RNDD').parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.upper() == x.upper('RNDD')
                True"""
        @overload
        def upper(self) -> Any:
            """RealIntervalFieldElement.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

            Return the upper bound of ``self``.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards plus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().upper().str()
                '3.1417'

            ::

                sage: R = RealIntervalField(13)
                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.upper()
                1.31
                sage: x.upper('RNDU')
                1.31
                sage: x.upper('RNDN')
                1.30
                sage: x.upper('RNDD')
                1.30
                sage: x.upper('RNDZ')
                1.30
                sage: x.upper('RNDA')
                1.31
                sage: x.upper().parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.upper('RNDD').parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.upper() == x.upper('RNDD')
                True"""
        @overload
        def upper(self) -> Any:
            """RealIntervalFieldElement.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

            Return the upper bound of ``self``.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards plus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().upper().str()
                '3.1417'

            ::

                sage: R = RealIntervalField(13)
                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.upper()
                1.31
                sage: x.upper('RNDU')
                1.31
                sage: x.upper('RNDN')
                1.30
                sage: x.upper('RNDD')
                1.30
                sage: x.upper('RNDZ')
                1.30
                sage: x.upper('RNDA')
                1.31
                sage: x.upper().parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.upper('RNDD').parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.upper() == x.upper('RNDD')
                True"""
        @overload
        def upper(self) -> Any:
            """RealIntervalFieldElement.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2276)

            Return the upper bound of ``self``.

            INPUT:

            - ``rnd`` -- the rounding mode (default: towards plus infinity,
              see :class:`sage.rings.real_mpfr.RealField` for possible values)

            The rounding mode does not affect the value returned as a
            floating-point number, but it does control which variety of
            ``RealField`` the returned number is in, which affects printing and
            subsequent operations.

            EXAMPLES::

                sage: R = RealIntervalField(13)
                sage: R.pi().upper().str()
                '3.1417'

            ::

                sage: R = RealIntervalField(13)
                sage: x = R(1.2,1.3); x.str(style='brackets')
                '[1.1999 .. 1.3001]'
                sage: x.upper()
                1.31
                sage: x.upper('RNDU')
                1.31
                sage: x.upper('RNDN')
                1.30
                sage: x.upper('RNDD')
                1.30
                sage: x.upper('RNDZ')
                1.30
                sage: x.upper('RNDA')
                1.31
                sage: x.upper().parent()
                Real Field with 13 bits of precision and rounding RNDU
                sage: x.upper('RNDD').parent()
                Real Field with 13 bits of precision and rounding RNDD
                sage: x.upper() == x.upper('RNDD')
                True"""
        def zeta(self, a=...) -> Any:
            """RealIntervalFieldElement.zeta(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 5172)

            Return the image of this interval by the Hurwitz zeta function.

            For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

            EXAMPLES::

                sage: zeta(RIF(3))
                1.202056903159594?
                sage: _.parent()
                Real Interval Field with 53 bits of precision
                sage: RIF(3).zeta(1/2)
                8.41439832211716?"""
        @overload
        def __abs__(self) -> Any:
            """RealIntervalFieldElement.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RIF(2).__abs__()
                2
                sage: RIF(2.1).__abs__()
                2.1000000000000001?
                sage: RIF(-2.1).__abs__()
                2.1000000000000001?"""
        @overload
        def __abs__(self) -> Any:
            """RealIntervalFieldElement.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RIF(2).__abs__()
                2
                sage: RIF(2.1).__abs__()
                2.1000000000000001?
                sage: RIF(-2.1).__abs__()
                2.1000000000000001?"""
        @overload
        def __abs__(self) -> Any:
            """RealIntervalFieldElement.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RIF(2).__abs__()
                2
                sage: RIF(2.1).__abs__()
                2.1000000000000001?
                sage: RIF(-2.1).__abs__()
                2.1000000000000001?"""
        @overload
        def __abs__(self) -> Any:
            """RealIntervalFieldElement.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2863)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RIF(2).__abs__()
                2
                sage: RIF(2.1).__abs__()
                2.1000000000000001?
                sage: RIF(-2.1).__abs__()
                2.1000000000000001?"""
        def __add__(self, left, right) -> Any:
            """RealIntervalFieldElement.__add__(left, right)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2613)

            TESTS::

                sage: RIF(1) + RR(1)
                doctest:...:
                DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
                See https://github.com/sagemath/sage/issues/15114 for details.
                2
                sage: import warnings; warnings.resetwarnings()"""
        def __bool__(self) -> bool:
            """True if self else False"""
        def __complex__(self) -> Any:
            """RealIntervalFieldElement.__complex__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3305)

            Convert ``self`` to a ``complex``.

            EXAMPLES::

                sage: complex(RIF(1))
                (1+0j)"""
        def __contains__(self, other) -> Any:
            """RealIntervalFieldElement.__contains__(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3998)

            Test whether one interval (or real number) is totally contained in
            another.

            EXAMPLES::

                sage: RIF(0, 2) in RIF(1, 3)
                False
                sage: RIF(0, 2) in RIF(0, 2)
                True
                sage: RIF(1, 2) in RIF(0, 3)
                True
                sage: 1.0 in RIF(0, 2)
                True
                sage: pi in RIF(3.1415, 3.1416)                                             # needs sage.symbolic
                True
                sage: 22/7 in RIF(3.1415, 3.1416)
                False"""
        def __copy__(self) -> Any:
            """RealIntervalFieldElement.__copy__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2200)

            Return copy of ``self``.

            Since ``self`` is immutable, we just return ``self`` again.

            EXAMPLES::

                sage: a = RIF(3.5)
                sage: copy(a) is  a
                True"""
        def __deepcopy__(self, memo) -> Any:
            """RealIntervalFieldElement.__deepcopy__(self, memo)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2214)

            EXAMPLES::

                sage: a = RIF(3.5)
                sage: deepcopy(a) is  a
                True"""
        def __float__(self) -> Any:
            """RealIntervalFieldElement.__float__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 3294)

            Convert ``self`` to a ``float``.

            EXAMPLES::

                sage: float(RIF(1))
                1.0"""
        def __hash__(self) -> Any:
            """RealIntervalFieldElement.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1433)

            Return a hash value of ``self``.

            EXAMPLES::

                sage: hash(RIF(e)) == hash(RIF(e))  # indirect doctest                      # needs sage.symbolic
                True"""
        def __invert__(self) -> Any:
            '''RealIntervalFieldElement.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2732)

            Return the multiplicative "inverse" of this interval. (Technically,
            non-precise intervals don\'t have multiplicative inverses.)

            EXAMPLES::

                sage: v = RIF(2); v
                2
                sage: ~v
                0.50000000000000000?
                sage: v * ~v
                1
                sage: v = RIF(1.5, 2.5); v.str(style=\'brackets\')
                \'[1.5000000000000000 .. 2.5000000000000000]\'
                sage: (~v).str(style=\'brackets\')
                \'[0.39999999999999996 .. 0.66666666666666675]\'
                sage: (v * ~v).str(style=\'brackets\')
                \'[0.59999999999999986 .. 1.6666666666666670]\'
                sage: ~RIF(-1, 1)
                [-infinity .. +infinity]'''
        def __lshift__(self, x, y) -> Any:
            """RealIntervalFieldElement.__lshift__(x, y)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2935)

            Return `x * 2^y`, for `y` an integer. Much faster
            than an ordinary multiplication.

            EXAMPLES::

                sage: RIF(1.0) << 32
                4294967296"""
        def __mul__(self, left, right) -> Any:
            """RealIntervalFieldElement.__mul__(left, right)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2661)

            TESTS::

                sage: RIF(1) * RR(1)
                doctest:...:
                DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
                See https://github.com/sagemath/sage/issues/15114 for details.
                1
                sage: import warnings; warnings.resetwarnings()"""
        def __pow__(self, exponent, modulus) -> Any:
            """RealIntervalFieldElement.__pow__(self, exponent, modulus)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 4422)

            Raise ``self`` to ``exponent``.

            EXAMPLES::

                sage: R = RealIntervalField(17)
                sage: x = R((-e, pi))                                                       # needs sage.symbolic
                sage: x2 = x^2; x2.lower(), x2.upper()                                      # needs sage.symbolic
                (0.0000, 9.870)
                sage: x3 = x^3; x3.lower(), x3.upper()                                      # needs sage.symbolic
                (-26.83, 31.01)"""
        def __radd__(self, other):
            """Return value+self."""
        def __reduce__(self) -> Any:
            """RealIntervalFieldElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1275)

            Pickling support.

            EXAMPLES::

                sage: a = RIF(5,5.5)
                sage: loads(dumps(a)).lexico_cmp(a)
                0
                sage: R = RealIntervalField(sci_not=1, prec=200)
                sage: b = R('393.39203845902384098234098230948209384028340')
                sage: loads(dumps(b)).lexico_cmp(b)
                0
                sage: b = R(1)/R(0); b # R(0) has no particular sign, thus 1/R(0) covers the whole reals
                [-infinity .. +infinity]
                sage: c = loads(dumps(b))
                sage: (c.lower(), c.upper()) == (b.lower(), b.upper())
                True
                sage: b = R(-1)/R(0); b # same as above
                [-infinity .. +infinity]
                sage: c = loads(dumps(b))
                sage: (c.lower(), c.upper()) == (b.lower(), b.upper())
                True
                sage: b = R('[2 .. 3]'); b.str(error_digits=1)
                '2.5?5e0'
                sage: loads(dumps(b)).lexico_cmp(b)
                0
                sage: R = RealIntervalField(4000)
                sage: s = 1/R(3)
                sage: t = loads(dumps(s))
                sage: (t.upper(), t.lower()) == (s.upper(), s.lower())
                True
                sage: loads(dumps(1/RIF(0,1)))
                [1.0000000000000000 .. +infinity]"""
        def __rlshift__(self, other):
            """Return value<<self."""
        def __rmul__(self, other):
            """Return value*self."""
        def __rpow__(self, other):
            """Return pow(value, self, mod)."""
        def __rrshift__(self, other):
            """Return value>>self."""
        def __rshift__(self, x, y) -> Any:
            """RealIntervalFieldElement.__rshift__(x, y)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2966)

            Return `x / 2^y`, for `y` an integer.

            Much faster than an ordinary division.

            EXAMPLES::

                sage: RIF(1024.0) >> 14
                0.062500000000000000?"""
        def __rsub__(self, other):
            """Return value-self."""
        def __rtruediv__(self, other):
            """Return value/self."""
        def __sub__(self, left, right) -> Any:
            """RealIntervalFieldElement.__sub__(left, right)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2637)

            TESTS::

                sage: RIF(2) - RR(1)
                doctest:...:
                DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
                See https://github.com/sagemath/sage/issues/15114 for details.
                1
                sage: import warnings; warnings.resetwarnings()"""
        def __truediv__(self, left, right) -> Any:
            """RealIntervalFieldElement.__truediv__(left, right)

            File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 2685)

            TESTS::

                sage: RIF(1) / RR(1/2)
                doctest:...:
                DeprecationWarning: automatic conversions from floating-point numbers to intervals are deprecated
                See https://github.com/sagemath/sage/issues/15114 for details.
                2
                sage: import warnings; warnings.resetwarnings()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, mpfr_prec_tprec=..., intsci_not=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 546)

                Initialize ``self``.

                EXAMPLES::

                    sage: RealIntervalField()
                    Real Interval Field with 53 bits of precision
                    sage: RealIntervalField(200)
                    Real Interval Field with 200 bits of precision
        """
    @overload
    def algebraic_closure(self) -> Any:
        """RealIntervalField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 741)

        Return the algebraic closure of this interval field, i.e., the
        complex interval field with the same precision.

        EXAMPLES::

            sage: RIF.algebraic_closure()
            Complex Interval Field with 53 bits of precision
            sage: RIF.algebraic_closure() is CIF
            True
            sage: RealIntervalField(100).algebraic_closure()
            Complex Interval Field with 100 bits of precision"""
    @overload
    def algebraic_closure(self) -> Any:
        """RealIntervalField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 741)

        Return the algebraic closure of this interval field, i.e., the
        complex interval field with the same precision.

        EXAMPLES::

            sage: RIF.algebraic_closure()
            Complex Interval Field with 53 bits of precision
            sage: RIF.algebraic_closure() is CIF
            True
            sage: RealIntervalField(100).algebraic_closure()
            Complex Interval Field with 100 bits of precision"""
    @overload
    def algebraic_closure(self) -> Any:
        """RealIntervalField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 741)

        Return the algebraic closure of this interval field, i.e., the
        complex interval field with the same precision.

        EXAMPLES::

            sage: RIF.algebraic_closure()
            Complex Interval Field with 53 bits of precision
            sage: RIF.algebraic_closure() is CIF
            True
            sage: RealIntervalField(100).algebraic_closure()
            Complex Interval Field with 100 bits of precision"""
    @overload
    def algebraic_closure(self) -> Any:
        """RealIntervalField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 741)

        Return the algebraic closure of this interval field, i.e., the
        complex interval field with the same precision.

        EXAMPLES::

            sage: RIF.algebraic_closure()
            Complex Interval Field with 53 bits of precision
            sage: RIF.algebraic_closure() is CIF
            True
            sage: RealIntervalField(100).algebraic_closure()
            Complex Interval Field with 100 bits of precision"""
    @overload
    def characteristic(self) -> Any:
        """RealIntervalField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1007)

        Return 0, since the field of real numbers has characteristic 0.

        EXAMPLES::

            sage: RealIntervalField(10).characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """RealIntervalField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1007)

        Return 0, since the field of real numbers has characteristic 0.

        EXAMPLES::

            sage: RealIntervalField(10).characteristic()
            0"""
    @overload
    def complex_field(self) -> Any:
        """RealIntervalField_class.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 931)

        Return complex field of the same precision.

        EXAMPLES::

            sage: RIF.complex_field()
            Complex Interval Field with 53 bits of precision"""
    @overload
    def complex_field(self) -> Any:
        """RealIntervalField_class.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 931)

        Return complex field of the same precision.

        EXAMPLES::

            sage: RIF.complex_field()
            Complex Interval Field with 53 bits of precision"""
    def construction(self) -> Any:
        """RealIntervalField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 757)

        Return the functorial construction of ``self``, namely, completion of
        the rational numbers with respect to the prime at `\\infty`,
        and the note that this is an interval field.

        Also preserves other information that makes this field unique (e.g.
        precision, print mode).

        EXAMPLES::

            sage: R = RealIntervalField(123)
            sage: c, S = R.construction(); S
            Rational Field
            sage: R == c(S)
            True"""
    def euler_constant(self) -> Any:
        """RealIntervalField_class.euler_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1106)

        Return Euler's gamma constant to the precision of this field.

        EXAMPLES::

            sage: RealIntervalField(100).euler_constant()
            0.577215664901532860606512090083?"""
    def gen(self, i=...) -> Any:
        """RealIntervalField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 913)

        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: RIF.gen(0)
            1
            sage: RIF.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: self has only one generator"""
    @overload
    def gens(self) -> tuple:
        """RealIntervalField_class.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 953)

        Return a tuple of generators.

        EXAMPLES::

            sage: RIF.gens()
            (1,)"""
    @overload
    def gens(self) -> Any:
        """RealIntervalField_class.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 953)

        Return a tuple of generators.

        EXAMPLES::

            sage: RIF.gens()
            (1,)"""
    @overload
    def is_exact(self) -> bool:
        """RealIntervalField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 691)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: RIF.is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealIntervalField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 691)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: RIF.is_exact()
            False"""
    def log2(self) -> Any:
        """RealIntervalField_class.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1119)

        Return `\\log(2)` to the precision of this field.

        EXAMPLES::

            sage: R=RealIntervalField(100)
            sage: R.log2()
            0.693147180559945309417232121458?
            sage: R(2).log()
            0.693147180559945309417232121458?"""
    @overload
    def lower_field(self) -> Any:
        """RealIntervalField_class.lower_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 570)

        Return the :class:`RealField_class` with rounding mode ``'RNDD'``
        (rounding towards minus infinity).

        EXAMPLES::

            sage: RIF.lower_field()
            Real Field with 53 bits of precision and rounding RNDD
            sage: RealIntervalField(200).lower_field()
            Real Field with 200 bits of precision and rounding RNDD"""
    @overload
    def lower_field(self) -> Any:
        """RealIntervalField_class.lower_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 570)

        Return the :class:`RealField_class` with rounding mode ``'RNDD'``
        (rounding towards minus infinity).

        EXAMPLES::

            sage: RIF.lower_field()
            Real Field with 53 bits of precision and rounding RNDD
            sage: RealIntervalField(200).lower_field()
            Real Field with 200 bits of precision and rounding RNDD"""
    @overload
    def lower_field(self) -> Any:
        """RealIntervalField_class.lower_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 570)

        Return the :class:`RealField_class` with rounding mode ``'RNDD'``
        (rounding towards minus infinity).

        EXAMPLES::

            sage: RIF.lower_field()
            Real Field with 53 bits of precision and rounding RNDD
            sage: RealIntervalField(200).lower_field()
            Real Field with 200 bits of precision and rounding RNDD"""
    @overload
    def middle_field(self) -> Any:
        """RealIntervalField_class.middle_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 584)

        Return the :class:`RealField_class` with rounding mode ``'RNDN'``
        (rounding towards nearest).

        EXAMPLES::

            sage: RIF.middle_field()
            Real Field with 53 bits of precision
            sage: RealIntervalField(200).middle_field()
            Real Field with 200 bits of precision"""
    @overload
    def middle_field(self) -> Any:
        """RealIntervalField_class.middle_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 584)

        Return the :class:`RealField_class` with rounding mode ``'RNDN'``
        (rounding towards nearest).

        EXAMPLES::

            sage: RIF.middle_field()
            Real Field with 53 bits of precision
            sage: RealIntervalField(200).middle_field()
            Real Field with 200 bits of precision"""
    @overload
    def middle_field(self) -> Any:
        """RealIntervalField_class.middle_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 584)

        Return the :class:`RealField_class` with rounding mode ``'RNDN'``
        (rounding towards nearest).

        EXAMPLES::

            sage: RIF.middle_field()
            Real Field with 53 bits of precision
            sage: RealIntervalField(200).middle_field()
            Real Field with 200 bits of precision"""
    @overload
    def name(self) -> Any:
        """RealIntervalField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1018)

        Return the name of ``self``.

        EXAMPLES::

            sage: RIF.name()
            'IntervalRealIntervalField53'
            sage: RealIntervalField(200).name()
            'IntervalRealIntervalField200'"""
    @overload
    def name(self) -> Any:
        """RealIntervalField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1018)

        Return the name of ``self``.

        EXAMPLES::

            sage: RIF.name()
            'IntervalRealIntervalField53'
            sage: RealIntervalField(200).name()
            'IntervalRealIntervalField200'"""
    @overload
    def name(self) -> Any:
        """RealIntervalField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1018)

        Return the name of ``self``.

        EXAMPLES::

            sage: RIF.name()
            'IntervalRealIntervalField53'
            sage: RealIntervalField(200).name()
            'IntervalRealIntervalField200'"""
    @overload
    def ngens(self) -> Any:
        """RealIntervalField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 942)

        Return the number of generators of ``self``, which is 1.

        EXAMPLES::

            sage: RIF.ngens()
            1"""
    @overload
    def ngens(self) -> Any:
        """RealIntervalField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 942)

        Return the number of generators of ``self``, which is 1.

        EXAMPLES::

            sage: RIF.ngens()
            1"""
    def pi(self) -> Any:
        """RealIntervalField_class.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1087)

        Return `\\pi` to the precision of this field.

        EXAMPLES::

            sage: R = RealIntervalField(100)
            sage: R.pi()
            3.14159265358979323846264338328?
            sage: R.pi().sqrt()/2
            0.88622692545275801364908374167?
            sage: R = RealIntervalField(150)
            sage: R.pi().sqrt()/2
            0.886226925452758013649083741670572591398774728?"""
    def prec(self, *args, **kwargs):
        """RealIntervalField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1044)

        Return the precision of this field (in bits).

        EXAMPLES::

            sage: RIF.precision()
            53
            sage: RealIntervalField(200).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1044)

        Return the precision of this field (in bits).

        EXAMPLES::

            sage: RIF.precision()
            53
            sage: RealIntervalField(200).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1044)

        Return the precision of this field (in bits).

        EXAMPLES::

            sage: RIF.precision()
            53
            sage: RealIntervalField(200).precision()
            200"""
    @overload
    def precision(self) -> Any:
        """RealIntervalField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1044)

        Return the precision of this field (in bits).

        EXAMPLES::

            sage: RIF.precision()
            53
            sage: RealIntervalField(200).precision()
            200"""
    @overload
    def random_element(self, *args, **kwds) -> Any:
        """RealIntervalField_class.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 890)

        Return a random element of ``self``. Any arguments or keywords are
        passed onto the random element function in real field.

        By default, this is uniformly distributed in `[-1, 1]`.

        EXAMPLES::

            sage: RIF.random_element().parent() is RIF
            True
            sage: -100 <= RIF.random_element(-100, 100) <= 100
            True

        Passes extra positional or keyword arguments through::

            sage: 0 <= RIF.random_element(min=0, max=100) <= 100
            True
            sage: -100 <= RIF.random_element(min=-100, max=0) <= 0
            True"""
    @overload
    def random_element(self) -> Any:
        """RealIntervalField_class.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 890)

        Return a random element of ``self``. Any arguments or keywords are
        passed onto the random element function in real field.

        By default, this is uniformly distributed in `[-1, 1]`.

        EXAMPLES::

            sage: RIF.random_element().parent() is RIF
            True
            sage: -100 <= RIF.random_element(-100, 100) <= 100
            True

        Passes extra positional or keyword arguments through::

            sage: 0 <= RIF.random_element(min=0, max=100) <= 100
            True
            sage: -100 <= RIF.random_element(min=-100, max=0) <= 0
            True"""
    @overload
    def random_element(self, min=..., max=...) -> Any:
        """RealIntervalField_class.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 890)

        Return a random element of ``self``. Any arguments or keywords are
        passed onto the random element function in real field.

        By default, this is uniformly distributed in `[-1, 1]`.

        EXAMPLES::

            sage: RIF.random_element().parent() is RIF
            True
            sage: -100 <= RIF.random_element(-100, 100) <= 100
            True

        Passes extra positional or keyword arguments through::

            sage: 0 <= RIF.random_element(min=0, max=100) <= 100
            True
            sage: -100 <= RIF.random_element(min=-100, max=0) <= 0
            True"""
    @overload
    def random_element(self, min=..., max=...) -> Any:
        """RealIntervalField_class.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 890)

        Return a random element of ``self``. Any arguments or keywords are
        passed onto the random element function in real field.

        By default, this is uniformly distributed in `[-1, 1]`.

        EXAMPLES::

            sage: RIF.random_element().parent() is RIF
            True
            sage: -100 <= RIF.random_element(-100, 100) <= 100
            True

        Passes extra positional or keyword arguments through::

            sage: 0 <= RIF.random_element(min=0, max=100) <= 100
            True
            sage: -100 <= RIF.random_element(min=-100, max=0) <= 0
            True"""
    @overload
    def scientific_notation(self, status=...) -> Any:
        """RealIntervalField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1135)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then real numbers with this space as parent
        print using scientific notation.

        INPUT:

        - ``status`` -- boolean optional flag

        EXAMPLES::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?"""
    @overload
    def scientific_notation(self, _True) -> Any:
        """RealIntervalField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1135)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then real numbers with this space as parent
        print using scientific notation.

        INPUT:

        - ``status`` -- boolean optional flag

        EXAMPLES::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?"""
    @overload
    def scientific_notation(self, _False) -> Any:
        """RealIntervalField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1135)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then real numbers with this space as parent
        print using scientific notation.

        INPUT:

        - ``status`` -- boolean optional flag

        EXAMPLES::

            sage: RIF(0.025)
            0.025000000000000002?
            sage: RIF.scientific_notation(True)
            sage: RIF(0.025)
            2.5000000000000002?e-2
            sage: RIF.scientific_notation(False)
            sage: RIF(0.025)
            0.025000000000000002?"""
    def to_prec(self, prec) -> Any:
        """RealIntervalField_class.to_prec(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1059)

        Return a real interval field to the given precision.

        EXAMPLES::

            sage: RIF.to_prec(200)
            Real Interval Field with 200 bits of precision
            sage: RIF.to_prec(20)
            Real Interval Field with 20 bits of precision
            sage: RIF.to_prec(53) is RIF
            True"""
    @overload
    def upper_field(self) -> Any:
        """RealIntervalField_class.upper_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 598)

        Return the :class:`RealField_class` with rounding mode ``'RNDU'``
        (rounding towards plus infinity).

        EXAMPLES::

            sage: RIF.upper_field()
            Real Field with 53 bits of precision and rounding RNDU
            sage: RealIntervalField(200).upper_field()
            Real Field with 200 bits of precision and rounding RNDU"""
    @overload
    def upper_field(self) -> Any:
        """RealIntervalField_class.upper_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 598)

        Return the :class:`RealField_class` with rounding mode ``'RNDU'``
        (rounding towards plus infinity).

        EXAMPLES::

            sage: RIF.upper_field()
            Real Field with 53 bits of precision and rounding RNDU
            sage: RealIntervalField(200).upper_field()
            Real Field with 200 bits of precision and rounding RNDU"""
    @overload
    def upper_field(self) -> Any:
        """RealIntervalField_class.upper_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 598)

        Return the :class:`RealField_class` with rounding mode ``'RNDU'``
        (rounding towards plus infinity).

        EXAMPLES::

            sage: RIF.upper_field()
            Real Field with 53 bits of precision and rounding RNDU
            sage: RealIntervalField(200).upper_field()
            Real Field with 200 bits of precision and rounding RNDU"""
    @overload
    def zeta(self, n=...) -> Any:
        """RealIntervalField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1162)

        Return an `n`-th root of unity in the real field, if one
        exists, or raise a :exc:`ValueError` otherwise.

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: R.zeta()
            -1
            sage: R.zeta(1)
            1
            sage: R.zeta(5)
            Traceback (most recent call last):
            ...
            ValueError: No 5th root of unity in self"""
    @overload
    def zeta(self) -> Any:
        """RealIntervalField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1162)

        Return an `n`-th root of unity in the real field, if one
        exists, or raise a :exc:`ValueError` otherwise.

        EXAMPLES::

            sage: R = RealIntervalField()
            sage: R.zeta()
            -1
            sage: R.zeta(1)
            1
            sage: R.zeta(5)
            Traceback (most recent call last):
            ...
            ValueError: No 5th root of unity in self"""
    def __call__(self, x=..., y=..., **kwds) -> Any:
        """RealIntervalField_class.__call__(self, x=None, y=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 702)

        Create an element in this real interval field.

        INPUT:

        - ``x`` -- a number, string, or 2-tuple

        - ``y`` -- (default: ``None``) if given ``x`` is set to ``(x,y)``;
          this is so you can write ``R(2,3)`` to make the interval from 2 to 3

        - ``base`` -- integer (default: 10); only used if ``x`` is a string

        OUTPUT: an element of this real interval field

        EXAMPLES::

            sage: R = RealIntervalField(20)
            sage: R('1.234')
            1.23400?
            sage: R('2', base=2)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert '2' to real interval
            sage: a = R('1.1001', base=2); a
            1.5625000?
            sage: a.str(2)
            '1.1001000000000000000?'

        Type: RealIntervalField? for more information."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """RealIntervalField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 1031)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: hash(RIF) == hash(RealIntervalField(53)) # indirect doctest
            True
            sage: hash(RealIntervalField(200)) == hash(RealIntervalField(200))
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """RealIntervalField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_mpfi.pyx (starting at line 878)

        For pickling.

        EXAMPLES::

            sage: R = RealIntervalField(sci_not=1, prec=200)
            sage: loads(dumps(R)) == R
            True"""

RIF: RealIntervalField_class