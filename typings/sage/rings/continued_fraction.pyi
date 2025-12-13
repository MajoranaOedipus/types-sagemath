from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

ZZ_0: Incomplete
ZZ_1: Incomplete
ZZ_m1: Incomplete
ZZ_2: Incomplete

def last_two_convergents(x):
    """
    Given the list ``x`` that consists of numbers, return the two last
    convergents `p_{n-1}, q_{n-1}, p_n, q_n`.

    This function is principally used to compute the value of a ultimately
    periodic continued fraction.

    OUTPUT: a 4-tuple of Sage integers

    EXAMPLES::

        sage: from sage.rings.continued_fraction import last_two_convergents
        sage: last_two_convergents([])
        (0, 1, 1, 0)
        sage: last_two_convergents([0])
        (1, 0, 0, 1)
        sage: last_two_convergents([-1,1,3,2])
        (-1, 4, -2, 9)

    TESTS::

        sage: all(type(x) is Integer for x in last_two_convergents([]))
        True
    """
def rat_interval_cf_list(r1, r2):
    """
    Return the common prefix of the rationals ``r1`` and ``r2`` seen as
    continued fractions.

    OUTPUT: list of Sage integers

    EXAMPLES::

        sage: from sage.rings.continued_fraction import rat_interval_cf_list
        sage: rat_interval_cf_list(257/113, 5224/2297)
        [2, 3, 1, 1, 1, 4]
        sage: for prec in range(10,54):                                                 # needs sage.rings.real_interval_field
        ....:     R = RealIntervalField(prec)
        ....:     for _ in range(100):
        ....:         x = R.random_element() * R.random_element() + R.random_element() / 100
        ....:         l = x.lower().exact_rational()
        ....:         u = x.upper().exact_rational()
        ....:         if l.floor() != u.floor():
        ....:             continue
        ....:         cf = rat_interval_cf_list(l,u)
        ....:         a = continued_fraction(cf).value()
        ....:         b = continued_fraction(cf+[1]).value()
        ....:         if a > b:
        ....:             a,b = b,a
        ....:         assert a <= l
        ....:         assert b >= u
    """

class ContinuedFraction_base(SageObject):
    """
    Base class for (standard) continued fractions.

    If you want to implement your own continued fraction, simply derived from
    this class and implement the following methods:

    - ``def quotient(self, n)``: return the ``n``-th quotient of ``self`` as a
      Sage integer

    - ``def length(self)``: the number of partial quotients of ``self`` as a
      Sage integer or ``Infinity``.

    and optionally:

    - ``def value(self)``: return the value of ``self`` (an exact real number)

    This base class will provide:

    - computation of convergents in :meth:`convergent`, :meth:`numerator` and
      :meth:`denominator`

    - comparison with other continued fractions (see :meth:`__richcmp__`)

    - elementary arithmetic function :meth:`floor`, :meth:`ceil`, :meth:`sign`

    - accurate numerical approximations :meth:`_mpfr_`

    All other methods, in particular the ones involving binary operations like
    sum or product, rely on the optional method :meth:`value` (and not on
    convergents) and may fail at execution if it is not implemented.
    """
    def __init__(self) -> None:
        """
        INPUT:

        - ``parent`` -- the parent of ``self``

        TESTS::

            sage: TestSuite(continued_fraction(3)).run()
        """
    def str(self, nterms: int = 10, unicode: bool = False, join: bool = True):
        """
        Return a string representing this continued fraction.

        INPUT:

        - ``nterms`` -- the maximum number of terms to use

        - ``unicode`` -- (default: ``False``) whether to use unicode character

        - ``join`` -- (default: ``True``) if ``False`` instead of returning a
          string return a list of string, each of them representing a line

        EXAMPLES::

            sage: print(continued_fraction(pi).str())                                   # needs sage.symbolic
                                         1
            3 + ----------------------------------------------------
                                            1
                 7 + -----------------------------------------------
                                               1
                      15 + -----------------------------------------
                                                 1
                            1 + ------------------------------------
                                                     1
                                 292 + -----------------------------
                                                       1
                                        1 + ------------------------
                                                          1
                                             1 + -------------------
                                                            1
                                                  1 + --------------
                                                               1
                                                       2 + ---------
                                                            1 + ...
            sage: print(continued_fraction(pi).str(nterms=1))                           # needs sage.symbolic
            3 + ...
            sage: print(continued_fraction(pi).str(nterms=2))                           # needs sage.symbolic
                    1
            3 + ---------
                 7 + ...

            sage: print(continued_fraction(243/354).str())
                       1
            -----------------------
                         1
             1 + ------------------
                            1
                  2 + -------------
                              1
                       5 + --------
                                 1
                            3 + ---
                                 2
            sage: continued_fraction(243/354).str(join=False)
            ['           1           ',
             '-----------------------',
             '             1         ',
             ' 1 + ------------------',
             '                1      ',
             '      2 + -------------',
             '                  1    ',
             '           5 + --------',
             '                     1 ',
             '                3 + ---',
             '                     2 ']

            sage: print(continued_fraction(243/354).str(unicode=True))
                       1
            ───────────────────────
                         1
             1 + ──────────────────
                            1
                  2 + ─────────────
                              1
                       5 + ────────
                                 1
                            3 + ───
                                 2
        """
    def __abs__(self):
        """
        Return absolute value of ``self``.

        EXAMPLES::

            sage: a = continued_fraction(-17/389); a
            [-1; 1, 21, 1, 7, 2]
            sage: abs(a)
            [0; 22, 1, 7, 2]
            sage: QQ(abs(a))
            17/389
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison.

        EXAMPLES::

            sage: a = continued_fraction(-17/389)
            sage: b = continued_fraction(1/389)
            sage: c = continued_fraction([(),(1,)])     # the golden ratio
            sage: d = continued_fraction([(-1,),(1,)])
            sage: d < a and a < b and b < c
            True
            sage: d >= a
            False
            sage: d == d
            True

            sage: a == 'nothing'
            False
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: a = continued_fraction(-17/389); a
            [-1; 1, 21, 1, 7, 2]
            sage: float(a)                                                              # needs sage.rings.real_mpfr
            -0.043701799485861184
            sage: float(-17/389)
            -0.043701799485861184
        """
    def numerator(self, n):
        """
        Return the numerator of the `n`-th partial convergent of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: c = continued_fraction(pi); c
            [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
            sage: c.numerator(0)
            3
            sage: c.numerator(12)
            80143857
            sage: c.numerator(152)
            3943771611212266962743738812600748213157266596588744951727393497446921245353005283
        """
    p = numerator
    def denominator(self, n):
        """
        Return the denominator of the ``n``-th partial convergent of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: c = continued_fraction(pi); c
            [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
            sage: c.denominator(0)
            1
            sage: c.denominator(12)
            25510582
            sage: c.denominator(152)
            1255341492699841451528811722575401081588363886480089431843026103930863337221076748
        """
    q = denominator
    def convergent(self, n):
        """
        Return the ``n``-th partial convergent to ``self``.

        EXAMPLES::

            sage: a = continued_fraction(pi); a                                         # needs sage.symbolic
            [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
            sage: a.convergent(3)                                                       # needs sage.symbolic
            355/113
            sage: a.convergent(15)                                                      # needs sage.symbolic
            411557987/131002976
        """
    def convergents(self):
        """
        Return the list of partial convergents of ``self``.

        If ``self`` is an infinite continued fraction, then the object returned
        is a :class:`~sage.misc.lazy_list.lazy_list_generic` which
        behave like an infinite list.

        EXAMPLES::

            sage: a = continued_fraction(23/157); a
            [0; 6, 1, 4, 1, 3]
            sage: a.convergents()
            [0, 1/6, 1/7, 5/34, 6/41, 23/157]

        .. TODO::

            Add an example with infinite list.
        """
    def quotients(self):
        """
        Return the list of partial quotients of ``self``.

        If ``self`` is an infinite continued fraction, then the object returned
        is a :class:`~sage.misc.lazy_list.lazy_list_generic` which behaves
        like an infinite list.

        EXAMPLES::

            sage: a = continued_fraction(23/157); a
            [0; 6, 1, 4, 1, 3]
            sage: a.quotients()
            [0, 6, 1, 4, 1, 3]

        .. TODO::

            Add an example with infinite list.
        """
    def __getitem__(self, n):
        """
        Return the ``n``-th partial quotient of ``self`` or a continued fraction
        associated to a sublist of the partial quotients of ``self``.

        TESTS::

            sage: cf1 = continued_fraction(pi); cf1                                     # needs sage.symbolic
            [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
            sage: cf2 = continued_fraction(QuadraticField(2).gen()); cf2                # needs sage.rings.number_field
            [1; (2)*]
            sage: cf3 = continued_fraction(4/17); cf3
            [0; 4, 4]
            sage: cf1[3:17]                                                             # needs sage.symbolic
            [1; 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2]
            sage: cf2[:10]                                                              # needs sage.rings.number_field
            [1; 2, 2, 2, 2, 2, 2, 2, 2, 2]
            sage: cf3[1:16]
            [4; 4]

        Be careful that the truncation of an infinite continued fraction might
        be shorter by one::

            sage: len(continued_fraction(golden_ratio)[:8])                             # needs sage.symbolic
            7
        """
    def __iter__(self):
        """
        Iterate over the partial quotient of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: cf = continued_fraction(pi)
            sage: i = iter(cf)
            sage: [next(i) for _ in range(10)]
            [3, 7, 15, 1, 292, 1, 1, 1, 2, 1]
            sage: [next(i) for _ in range(10)]
            [3, 1, 14, 2, 1, 1, 2, 2, 2, 2]
            sage: [next(i) for _ in range(10)]
            [1, 84, 2, 1, 1, 15, 3, 13, 1, 4]
        """
    def __int__(self) -> int:
        """
        EXAMPLES::

            sage: a = continued_fraction(-17/389); a
            [-1; 1, 21, 1, 7, 2]
            sage: int(a)
            -1
        """
    def sign(self):
        """
        Return the sign of ``self`` as an Integer.

        The sign is defined to be ``0`` if ``self`` is ``0``, ``1`` if ``self``
        is positive and ``-1`` if ``self`` is negative.

        EXAMPLES::

            sage: continued_fraction(tan(pi/7)).sign()                                  # needs sage.symbolic
            1
            sage: continued_fraction(-34/2115).sign()
            -1
            sage: continued_fraction([0]).sign()
            0
        """
    def floor(self):
        """
        Return the floor of ``self``.

        EXAMPLES::

            sage: cf = continued_fraction([2,1,2,3])
            sage: cf.floor()
            2
        """
    def ceil(self):
        """
        Return the ceil of ``self``.

        EXAMPLES::

            sage: cf = continued_fraction([2,1,3,4])
            sage: cf.ceil()
            3
        """
    def __bool__(self) -> bool:
        """
        Return ``False`` if ``self`` is zero.

        EXAMPLES::

            sage: continued_fraction(0).is_zero()    # indirect doctest
            True
            sage: continued_fraction(1).is_zero()    # indirect doctest
            False
            sage: continued_fraction([(),(1,)]).is_zero()     # indirect doctest
            False
            sage: continued_fraction([(0,),(1,2)]).is_zero()  # indirect doctest
            False
        """
    def is_zero(self):
        """
        Test whether ``self`` is zero.

        EXAMPLES::

            sage: continued_fraction(0).is_zero()
            True
            sage: continued_fraction((0,1)).is_zero()
            False
            sage: continued_fraction(-1/2).is_zero()
            False
            sage: continued_fraction(pi).is_zero()                                      # needs sage.symbolic
            False
        """
    def is_one(self):
        """
        Test whether ``self`` is one.

        EXAMPLES::

            sage: continued_fraction(1).is_one()
            True
            sage: continued_fraction(5/4).is_one()
            False
            sage: continued_fraction(0).is_one()
            False
            sage: continued_fraction(pi).is_one()                                       # needs sage.symbolic
            False
        """
    def is_minus_one(self):
        """
        Test whether ``self`` is minus one.

        EXAMPLES::

            sage: continued_fraction(-1).is_minus_one()
            True
            sage: continued_fraction(1).is_minus_one()
            False
            sage: continued_fraction(0).is_minus_one()
            False
            sage: continued_fraction(-2).is_minus_one()
            False
            sage: continued_fraction([-1,1]).is_minus_one()
            False
        """
    def additive_order(self):
        """
        Return the additive order of this continued fraction,
        which we defined to be the additive order of its value.

        EXAMPLES::

            sage: continued_fraction(-1).additive_order()
            +Infinity
            sage: continued_fraction(0).additive_order()
            1
        """
    def multiplicative_order(self):
        """
        Return the multiplicative order of this continued fraction,
        which we defined to be the multiplicative order of its value.

        EXAMPLES::

            sage: continued_fraction(-1).multiplicative_order()
            2
            sage: continued_fraction(1).multiplicative_order()
            1
            sage: continued_fraction(pi).multiplicative_order()                         # needs sage.symbolic
            +Infinity
        """
    def numerical_approx(self, prec=None, digits=None, algorithm=None):
        """
        Return a numerical approximation of this continued fraction with
        ``prec`` bits (or decimal ``digits``) of precision.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- ignored for continued fractions

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: w = words.FibonacciWord([1,3])                                        # needs sage.combinat
            sage: cf = continued_fraction(w); cf                                        # needs sage.combinat
            [1; 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3...]
            sage: cf.numerical_approx(prec=53)                                          # needs sage.combinat
            1.28102513329557

        The method `n` is a shortcut to this one::

            sage: cf.n(digits=25)                                                       # needs sage.combinat
            1.281025133295569815552930
            sage: cf.n(digits=33)                                                       # needs sage.combinat
            1.28102513329556981555293038097590
        """
    n = numerical_approx
    def apply_homography(self, a, b, c, d, forward_value: bool = False):
        """
        Return the continued fraction of `(ax + b)/(cx + d)`.

        This is computed using Gosper's algorithm, see
        :mod:`~sage.rings.continued_fraction_gosper`.

        INPUT:

        - ``a``, ``b``, ``c``, ``d`` -- integers

        - ``forward_value`` -- boolean (default: ``False``); whether the
          returned continued fraction is given the symbolic value of
          `(a x + b)/(cx + d)` and not only the list of partial quotients
          obtained from Gosper's algorithm

        EXAMPLES::

            sage: (5 * 13/6 - 2) / (3 * 13/6 - 4)
            53/15
            sage: continued_fraction(13/6).apply_homography(5, -2,  3, -4).value()
            53/15

        We demonstrate now the effect of the optional argument ``forward_value``::

            sage: cf = continued_fraction(pi)                                           # needs sage.symbolic
            sage: h1 = cf.apply_homography(35, -27, 12, -5); h1                         # needs sage.symbolic
            [2; 1, 1, 6, 3, 1, 2, 1, 5, 3, 1, 1, 1, 1, 9, 12, 1, 1, 1, 3...]
            sage: h1.value()                                                            # needs sage.symbolic
            2.536941776086946?

            sage: h2 = cf.apply_homography(35, -27, 12, -5, forward_value=True); h2     # needs sage.symbolic
            [2; 1, 1, 6, 3, 1, 2, 1, 5, 3, 1, 1, 1, 1, 9, 12, 1, 1, 1, 3...]
            sage: h2.value()                                                            # needs sage.symbolic
            (35*pi - 27)/(12*pi - 5)

        TESTS::

            sage: CF = [continued_fraction(x) for x in [sqrt(2), AA(3).sqrt(),          # needs sage.rings.number_field sage.symbolic
            ....:       AA(3)**(1/3), QuadraticField(37).gen(), pi, 113/27,
            ....:       [3,1,2,2], words.FibonacciWord([1,3])]]
            sage: for _ in range(100):  # not tested, known bug (see :issue:`32086`)
            ....:     cf = choice(CF)
            ....:     forward_value = choice([True, False])
            ....:     a = ZZ.random_element(-30, 30)
            ....:     b = ZZ.random_element(-30, 30)
            ....:     c = ZZ.random_element(-30, 30)
            ....:     d = ZZ.random_element(-30, 30)
            ....:     if not c and not d:
            ....:         continue
            ....:     cf_gosper = cf.apply_homography(a, b, c, d, forward_value)
            ....:     x = cf.value()
            ....:     cf_hom = continued_fraction((a*x + b) / (c*x + d))
            ....:     assert cf_gosper[:30] == cf_hom[:30]

            sage: continued_fraction(13/25).apply_homography(0, 1, 25, -13)
            Traceback (most recent call last):
            ...
            ValueError: continued fraction can not represent infinity

            sage: continued_fraction(pi).apply_homography(0, 1, 0, 0)                   # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero

        REFERENCES:

        - [Gos1972]_
        - [Knu1998]_ Exercise 4.5.3.15
        - [LS1998]_
        """
    def __neg__(self):
        """
        Return the additive inverse of ``self``.

        EXAMPLES::

            sage: -continued_fraction(e)                                                # needs sage.symbolic
            [-3; 3, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14...]
            sage: -continued_fraction(sqrt(7))                                          # needs sage.symbolic
            [-3; 2, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4...]
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: ~continued_fraction(e)                                                # needs sage.symbolic
            [0; 2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1...]
            sage: ~continued_fraction(sqrt(7))                                          # needs sage.symbolic
            [0; 2, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1...]
        """

class ContinuedFraction_periodic(ContinuedFraction_base):
    """
    Continued fraction associated with rational or quadratic number.

    A rational number has a finite continued fraction expansion (or ultimately
    0). The one of a quadratic number, ie a number of the form `a + b \\sqrt{D}`
    with `a` and `b` rational, is ultimately periodic.

    .. NOTE::

        This class stores a tuple ``_x1`` for the preperiod and a tuple ``_x2``
        for the period. In the purely periodic case ``_x1`` is empty while in
        the rational case ``_x2`` is the tuple ``(0,)``.
    """
    def __init__(self, x1, x2=None, check: bool = True) -> None:
        """
        INPUT:

        - ``x1`` -- tuple of integers

        - ``x2`` -- tuple of integers

        TESTS::

            sage: cf = continued_fraction((1,1,2,3,4)) # indirect doctest
            sage: loads(dumps(cf)) == cf
            True
            sage: cf = continued_fraction((1,5),(3,2)) # indirect doctest
            sage: loads(dumps(cf)) == cf
            True
        """
    def period(self):
        """
        Return the periodic part of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt3> = QuadraticField(3)
            sage: cf = continued_fraction(sqrt3); cf
            [1; (1, 2)*]
            sage: cf.period()
            (1, 2)
            sage: for k in xsrange(2,40):
            ....:     if not k.is_square():
            ....:         s = QuadraticField(k).gen()
            ....:         cf = continued_fraction(s)
            ....:         print('%2d %d %s' % (k, len(cf.period()), cf))
             2 1 [1; (2)*]
             3 2 [1; (1, 2)*]
             5 1 [2; (4)*]
             6 2 [2; (2, 4)*]
             7 4 [2; (1, 1, 1, 4)*]
             8 2 [2; (1, 4)*]
            10 1 [3; (6)*]
            11 2 [3; (3, 6)*]
            12 2 [3; (2, 6)*]
            13 5 [3; (1, 1, 1, 1, 6)*]
            14 4 [3; (1, 2, 1, 6)*]
            ...
            35 2 [5; (1, 10)*]
            37 1 [6; (12)*]
            38 2 [6; (6, 12)*]
            39 2 [6; (4, 12)*]
        """
    def preperiod(self):
        """
        Return the preperiodic part of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt3> = QuadraticField(3)
            sage: cf = continued_fraction(sqrt3); cf
            [1; (1, 2)*]
            sage: cf.preperiod()
            (1,)
            sage: cf = continued_fraction(sqrt3/7); cf
            [0; 4, (24, 8)*]
            sage: cf.preperiod()
            (0, 4)
        """
    def quotient(self, n):
        """
        Return the ``n``-th partial quotient of ``self``.

        EXAMPLES::

            sage: cf = continued_fraction([(12,5),(1,3)])
            sage: [cf.quotient(i) for i in range(10)]
            [12, 5, 1, 3, 1, 3, 1, 3, 1, 3]
        """
    def length(self):
        """
        Return the number of partial quotients of ``self``.

        EXAMPLES::

            sage: continued_fraction(2/5).length()
            3
            sage: cf = continued_fraction([(0,1),(2,)]); cf
            [0; 1, (2)*]
            sage: cf.length()
            +Infinity
        """
    def preperiod_length(self):
        """
        Return the number of partial quotients of the preperiodic part of ``self``.

        EXAMPLES::

            sage: continued_fraction(2/5).preperiod_length()
            3
            sage: cf = continued_fraction([(0,1),(2,)]); cf
            [0; 1, (2)*]
            sage: cf.preperiod_length()
            2
        """
    def period_length(self):
        """
        Return the number of partial quotients of the preperiodic part of ``self``.

        EXAMPLES::

            sage: continued_fraction(2/5).period_length()
            1
            sage: cf = continued_fraction([(0,1),(2,)]); cf
            [0; 1, (2)*]
            sage: cf.period_length()
            1
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: a = continued_fraction([(0,),(1,2,3,1,2,3,1)]); a.n()
            0.694249167819459
            sage: b = continued_fraction([(0,),(1,2,3)]); b.n()
            0.694254176766073
            sage: c = continued_fraction([(0,1),(2,3)]); c.n()
            0.696140478029631
            sage: d = continued_fraction([(0,1,2),(3,)]); d.n()
            0.697224362268005
            sage: a < b and a < c and a < d
            True
            sage: b < c and b < d and c < d
            True
            sage: b == c
            False
            sage: c > c
            False
            sage: b >= d
            False
        """
    def value(self):
        """
        Return the value of ``self`` as a quadratic number (with square free
        discriminant).

        EXAMPLES:

        Some purely periodic examples::

            sage: cf = continued_fraction([(),(2,)]); cf
            [(2)*]
            sage: v = cf.value(); v                                                     # needs sage.rings.number_field
            sqrt2 + 1
            sage: v.continued_fraction()                                                # needs sage.rings.number_field
            [(2)*]

            sage: cf = continued_fraction([(),(1,2)]); cf
            [(1, 2)*]
            sage: v = cf.value(); v                                                     # needs sage.rings.number_field
            1/2*sqrt3 + 1/2
            sage: v.continued_fraction()                                                # needs sage.rings.number_field
            [(1, 2)*]

        The number ``sqrt3`` that appear above is actually internal to the
        continued fraction. In order to be access it from the console::

            sage: cf.value().parent().inject_variables()                                # needs sage.rings.number_field
            Defining sqrt3
            sage: sqrt3                                                                 # needs sage.rings.number_field
            sqrt3
            sage: ((sqrt3+1)/2).continued_fraction()                                    # needs sage.rings.number_field
            [(1, 2)*]

        Some ultimately periodic but non periodic examples::

            sage: cf = continued_fraction([(1,),(2,)]); cf
            [1; (2)*]
            sage: v = cf.value(); v                                                     # needs sage.rings.number_field
            sqrt2
            sage: v.continued_fraction()                                                # needs sage.rings.number_field
            [1; (2)*]

            sage: cf = continued_fraction([(1,3),(1,2)]); cf
            [1; 3, (1, 2)*]
            sage: v = cf.value(); v                                                     # needs sage.rings.number_field
            -sqrt3 + 3
            sage: v.continued_fraction()                                                # needs sage.rings.number_field
            [1; 3, (1, 2)*]

            sage: cf = continued_fraction([(-5,18), (1,3,1,5)])
            sage: cf.value().continued_fraction() == cf                                 # needs sage.rings.number_field
            True
            sage: cf = continued_fraction([(-1,),(1,)])
            sage: cf.value().continued_fraction() == cf                                 # needs sage.rings.number_field
            True

        TESTS::

            sage: a1 = ((0,1),(2,3))
            sage: a2 = ((-12,1,1),(2,3,2,4))
            sage: a3 = ((1,),(1,2))
            sage: a4 = ((-2,2),(1,124,13))
            sage: a5 = ((0,),(1,))
            sage: for a in a1,a2,a3,a4,a5:                                              # needs sage.rings.number_field
            ....:     cf = continued_fraction(a)
            ....:     assert cf.value().continued_fraction() == cf
        """
    def __len__(self) -> int:
        """
        Return the number of terms in this continued fraction.

        EXAMPLES::

            sage: len(continued_fraction([1,2,3,4,5]) )
            5

            sage: len(continued_fraction(([],[1])))
            Traceback (most recent call last):
            ...
            ValueError: the length is infinite
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: a = continued_fraction(13/25)
            sage: ~a == continued_fraction(25/13)
            True
            sage: a.value() * (~a).value()
            1

            sage: a = continued_fraction(-17/253)
            sage: ~a == continued_fraction(-253/17)
            True
            sage: a.value() * (~a).value()
            1

            sage: # needs sage.rings.number_field
            sage: K.<sqrt5> = QuadraticField(5)
            sage: a1 = (sqrt5+1)/2
            sage: c1 = a1.continued_fraction(); c1
            [(1)*]
            sage: ~c1
            [0; (1)*]
            sage: c1.value() * (~c1).value()
            1

            sage: c2 = (sqrt5/3 + 1/7).continued_fraction(); c2                         # needs sage.rings.number_field
            [0; 1, (7, 1, 17, ..., 1, 2)*]
            sage: c2.value() * (~c2).value()                                            # needs sage.rings.number_field
            1
        """
    def __neg__(self):
        """
        Return the additive inverse of ``self``.

        TESTS::

            sage: quots1 = [(0,),(1,),(2,),(0,1),(1,1),(2,1),(1,2),
            ....:           (0,1,1),(1,1,1),(1,1,1,1),(1,2)]
            sage: for q in quots1:
            ....:     cf = continued_fraction(q)
            ....:     ncf = -cf
            ....:     nncf = -ncf
            ....:     assert cf == nncf
            ....:     assert ncf.value() == -cf.value()
            ....:     assert cf.length() < 2 or cf.quotients()[-1] != 1
            ....:     assert ncf.length() < 2 or ncf.quotients()[-1] != 1
            ....:     assert nncf.length() < 2 or nncf.quotients()[-1] != 1

            sage: quots2 = [((),(1,)), ((), (1,2)), ((0,),(1,)),
            ....:           ((),(2,1)), ((3,),(2,1))]
            sage: for q in quots2:                                                      # needs sage.rings.number_field
            ....:     cf = continued_fraction(q)
            ....:     ncf = -cf
            ....:     nncf = -ncf
            ....:     assert cf == nncf
            ....:     assert ncf.value() == -cf.value()
        """

class ContinuedFraction_real(ContinuedFraction_base):
    """
    Continued fraction of a real (exact) number.

    This class simply wraps a real number into an attribute (that can be
    accessed through the method :meth:`value`). The number is assumed to be
    irrational.

    EXAMPLES::

        sage: cf = continued_fraction(pi); cf                                           # needs sage.symbolic
        [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
        sage: cf.value()                                                                # needs sage.symbolic
        pi

        sage: cf = continued_fraction(e); cf                                            # needs sage.symbolic
        [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, ...]
        sage: cf.value()                                                                # needs sage.symbolic
        e
    """
    def __init__(self, x) -> None:
        """
        INPUT:

        - ``x`` -- the real number from which we want the continued fraction

        TESTS::

            sage: TestSuite(continued_fraction(pi)).run()                               # needs sage.symbolic
        """
    def length(self):
        """
        Return infinity.

        EXAMPLES::

            sage: continued_fraction(pi).length()                                       # needs sage.symbolic
            +Infinity
        """
    def __len__(self) -> int:
        """
        TESTS::

            sage: len(continued_fraction(pi))                                           # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: the length is infinite!
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison.

        EXAMPLES::

            sage: continued_fraction(pi) > continued_fraction(e)                        # needs sage.symbolic
            True
            sage: continued_fraction(pi) > continued_fraction(e+4)                      # needs sage.symbolic
            False
        """
    def quotient(self, n):
        """
        Return the ``n``-th quotient of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: cf = continued_fraction(pi)
            sage: cf.quotient(27)
            13
            sage: cf.quotient(2552)
            152
            sage: cf.quotient(10000)            # long time
            5

        The algorithm is not efficient with element of the symbolic ring and,
        if possible, one can always prefer number fields elements. The reason is
        that, given a symbolic element ``x``, there is no automatic way to
        evaluate in ``RIF`` an expression of the form ``(a*x+b)/(c*x+d)`` where
        both the numerator and the denominator are extremely small::

            sage: # needs sage.symbolic
            sage: a1 = pi
            sage: c1 = continued_fraction(a1)
            sage: p0 = c1.numerator(12); q0 = c1.denominator(12)
            sage: p1 = c1.numerator(13); q1 = c1.denominator(13)
            sage: num = (q0*a1 - p0); num.n()
            1.49011611938477e-8
            sage: den = (q1*a1 - p1); den.n()
            -2.98023223876953e-8
            sage: a1 = -num/den
            sage: RIF(a1)
            [-infinity .. +infinity]

        The same computation with an element of a number field instead of
        ``pi`` gives a very satisfactory answer::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a2> = NumberField(x^3 - 2, embedding=1.25)
            sage: c2 = continued_fraction(a2)
            sage: p0 = c2.numerator(111); q0 = c2.denominator(111)
            sage: p1 = c2.numerator(112); q1 = c2.denominator(112)
            sage: num = (q0*a2 - p0); num.n()
            -4.56719261665907e46
            sage: den = (q1*a2 - p1); den.n()
            -3.65375409332726e47
            sage: a2 = -num/den
            sage: b2 = RIF(a2); b2
            1.002685823312715?
            sage: b2.absolute_diameter()
            8.88178419700125e-16

        The consequence is that the precision needed with ``c1`` grows when we
        compute larger and larger partial quotients::

            sage: # needs sage.symbolic
            sage: c1.quotient(100)
            2
            sage: c1._xa.parent()
            Real Interval Field with 353 bits of precision
            sage: c1.quotient(200)
            3
            sage: c1._xa.parent()
            Real Interval Field with 753 bits of precision
            sage: c1.quotient(300)
            5
            sage: c1._xa.parent()
            Real Interval Field with 1053 bits of precision

            sage: # needs sage.rings.number_field
            sage: c2.quotient(200)
            6
            sage: c2._xa.parent()
            Real Interval Field with 53 bits of precision
            sage: c2.quotient(500)
            1
            sage: c2._xa.parent()
            Real Interval Field with 53 bits of precision
            sage: c2.quotient(1000)
            1
            sage: c2._xa.parent()
            Real Interval Field with 53 bits of precision
        """
    def value(self):
        """
        Return the value of ``self`` (the number from which it was built).

        EXAMPLES::

            sage: cf = continued_fraction(e)                                            # needs sage.symbolic
            sage: cf.value()                                                            # needs sage.symbolic
            e
        """

class ContinuedFraction_infinite(ContinuedFraction_base):
    """
    A continued fraction defined by an infinite sequence of partial quotients.

    EXAMPLES::

        sage: t = continued_fraction(words.ThueMorseWord([1,2])); t                     # needs sage.combinat
        [1; 2, 2, 1, 2, 1, 1, 2, 2, 1...]
        sage: t.n(digits=100)                                                           # needs sage.combinat
        1.422388736882785488341547116024565825306879108991711829311892452916456747272565883312455412962072042

    We check that comparisons work well::

        sage: t > continued_fraction(1) and t < continued_fraction(3/2)                 # needs sage.combinat
        True
        sage: t < continued_fraction(1) or t > continued_fraction(2)                    # needs sage.combinat
        False

    Can also be called with a ``value`` option::

        sage: def f(n):
        ....:     if n % 3 == 2: return 2*(n+1)//3
        ....:     return 1
        sage: w = Word(f, alphabet=NN); w                                               # needs sage.combinat
        word: 1,1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,16,1,1,18,1,1,20,1,1,22,1,1,24,1,1,26,1,...
        sage: cf = continued_fraction(w, value=e-1); cf                                 # needs sage.combinat sage.symbolic
        [1; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1...]

    In that case a small check is done on the input::

        sage: cf = continued_fraction(w, value=pi)                                      # needs sage.combinat sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: value evaluates to 3.141592653589794? while the continued
        fraction evaluates to 1.718281828459046? in Real Interval Field
        with 53 bits of precision.
    """
    def __init__(self, w, value=None, check: bool = True) -> None:
        """
        INPUT:

        - ``parent`` -- a parent

        - ``w`` -- an infinite list

        - ``value`` -- an optional known value

        - ``check`` -- whether the constructor checks the input (default: ``True``)

        TESTS::

            sage: w = words.FibonacciWord(['a','b'])                                    # needs sage.combinat
            sage: continued_fraction(w)                                                 # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: the sequence must consist of integers

            sage: from itertools import count
            sage: w = Word(count(), length='infinite')                                  # needs sage.combinat
            sage: continued_fraction(w)                                                 # needs sage.combinat
            [0; 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19...]

            sage: w = Word(count(), length='unknown')                                   # needs sage.combinat
            sage: continued_fraction(w)                                                 # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: word with unknown length cannot be converted to
            continued fractions

            sage: continued_fraction(words.FibonacciWord([0,1]))                        # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: only the first partial quotient can be null

            sage: w = words.ThueMorseWord([int(1), int(2)])                             # needs sage.combinat
            sage: t = continued_fraction(w)                                             # needs sage.combinat
            sage: type(t.quotient(1))                                                   # needs sage.combinat
            <class 'sage.rings.integer.Integer'>
        """
    def length(self):
        """
        Return infinity.

        EXAMPLES::

            sage: w = words.FibonacciWord([3,13])                                       # needs sage.combinat
            sage: cf = continued_fraction(w)                                            # needs sage.combinat
            sage: cf.length()                                                           # needs sage.combinat
            +Infinity
        """
    def quotient(self, n):
        """
        Return the ``n``-th partial quotient of ``self``.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: # needs sage.combinat
            sage: w = words.FibonacciWord([1,3])
            sage: cf = continued_fraction(w)
            sage: cf.quotient(0)
            1
            sage: cf.quotient(1)
            3
            sage: cf.quotient(2)
            1
        """
    def quotients(self):
        """
        Return the infinite list from which this continued fraction was built.

        EXAMPLES::

            sage: w = words.FibonacciWord([1,5])                                        # needs sage.combinat
            sage: cf = continued_fraction(w)                                            # needs sage.combinat
            sage: cf.quotients()                                                        # needs sage.combinat
            word: 1511515115115151151511511515115115151151...
        """
    def value(self):
        """
        Return the value of ``self``.

        If this value was provided on initialization, just return this value
        otherwise return an element of the real lazy field.

        EXAMPLES::

            sage: def f(n):
            ....:     if n % 3 == 2: return 2*(n+1)//3
            ....:     return 1
            sage: w = Word(f, alphabet=NN); w                                           # needs sage.combinat
            word: 1,1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,16,1,1,18,1,1,20,1,1,22,1,1,24,1,1,26,1,...
            sage: cf = continued_fraction(w, value=e-1); cf                             # needs sage.combinat sage.symbolic
            [1; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1...]
            sage: cf.value()                                                            # needs sage.combinat sage.symbolic
            e - 1

            sage: w = words.FibonacciWord([2,5])                                        # needs sage.combinat
            sage: cf = continued_fraction(w); cf                                        # needs sage.combinat
            [2; 5, 2, 2, 5, 2, 5, 2, 2, 5, 2, 2, 5, 2, 5, 2, 2, 5, 2, 5...]
            sage: cf.value()                                                            # needs sage.combinat
            2.184951302409338?
        """
    def __neg__(self):
        """
        Return the opposite of ``self``.

        EXAMPLES::

            sage: -continued_fraction(words.FibonacciWord([2,5]))                       # needs sage.combinat
            [-3; 1, 4, 2, 2, 5, 2, 5, 2, 2, 5, 2, 2, 5, 2, 5, 2, 2, 5, 2...]

            sage: from sage.misc.lazy_list import lazy_list
            sage: l = lazy_list(lambda n: (n**2)%17)
            sage: -continued_fraction(l)                                                # needs sage.combinat
            [-1; 5, 9, 16, 8, 2, 15, 13, 13, 15, 2, 8, 16, 9, 4, 1, 0, 1, 4, 9...]
        """

def check_and_reduce_pair(x1, x2=None):
    """
    There are often two ways to represent a given continued fraction. This
    function makes it canonical.

    In the very special case of the number `0` we return the pair
    ``((0,),(0,))``.

    TESTS::

        sage: from sage.rings.continued_fraction import check_and_reduce_pair
        sage: check_and_reduce_pair([])
        Traceback (most recent call last):
        ...
        ValueError: continued fraction can not represent infinity
        sage: check_and_reduce_pair([-1,1])
        ((0,), (+Infinity,))
        sage: check_and_reduce_pair([1,1,1])
        ((1, 2), (+Infinity,))
        sage: check_and_reduce_pair([1,3],[2,3])
        ((1,), (3, 2))
        sage: check_and_reduce_pair([1,2,3],[2,3,2,3,2,3])
        ((1,), (2, 3))
        sage: check_and_reduce_pair([1,2],[])
        ((1, 2), (+Infinity,))
    """
def continued_fraction_list(x, type: str = 'std', partial_convergents: bool = False, bits=None, nterms=None):
    """
    Return the (finite) continued fraction of ``x`` as a list.

    The continued fraction expansion of ``x`` are the coefficients `a_i` in

    .. MATH::

        x = a_0 + 1/(a_1 + 1/(...))

    with `a_0` integer and `a_1`, `...` positive integers. The Hirzebruch-Jung
    continued fraction is the one for which the `+` signs are replaced with `-`
    signs

    .. MATH::

        x = a_0 - 1/(a_1 - 1/(...))

    .. SEEALSO::

        :func:`continued_fraction`

    INPUT:

    - ``x`` -- exact rational or floating-point number; the number to
      compute the continued fraction of

    - ``type`` -- either ``'std'`` (default) for standard continued fractions or
      ``'hj'`` for Hirzebruch-Jung ones

    - ``partial_convergents`` -- boolean; whether to return the
      partial convergents

    - ``bits`` -- an optional integer that specify a precision for the real
      interval field that is used internally

    - ``nterms`` -- integer; the upper bound on the number of terms in
      the continued fraction expansion to return

    OUTPUT:

    A list of integers, the coefficients in the continued fraction expansion of
    ``x``. If ``partial_convergents`` is set to ``True``, then return a pair
    containing the coefficient list and the partial convergents list is
    returned.

     EXAMPLES::

        sage: continued_fraction_list(45/19)
        [2, 2, 1, 2, 2]
        sage: 2 + 1/(2 + 1/(1 + 1/(2 + 1/2)))
        45/19

        sage: continued_fraction_list(45/19, type='hj')
        [3, 2, 3, 2, 3]
        sage: 3 - 1/(2 - 1/(3 - 1/(2 - 1/3)))
        45/19

    Specifying ``bits`` or ``nterms`` modify the length of the output::

        sage: # needs sage.symbolic
        sage: continued_fraction_list(e, bits=20)
        [2, 1, 2, 1, 1, 4, 2]
        sage: continued_fraction_list(sqrt(2) + sqrt(3), bits=30)
        [3, 6, 1, 5, 7, 2]
        sage: continued_fraction_list(pi, bits=53)
        [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14]
        sage: continued_fraction_list(log(3/2), nterms=15)
        [0, 2, 2, 6, 1, 11, 2, 1, 2, 2, 1, 4, 3, 1, 1]
        sage: continued_fraction_list(tan(sqrt(pi)), nterms=20)
        [-5, 9, 4, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 2, 4, 3, 1, 63]

    When the continued fraction is infinite (ie ``x`` is an irrational number)
    and the parameters ``bits`` and ``nterms`` are not specified then a warning
    is raised::

        sage: continued_fraction_list(sqrt(2))                                          # needs sage.symbolic
        doctest:...: UserWarning: the continued fraction of sqrt(2) seems infinite,
        return only the first 20 terms
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        sage: continued_fraction_list(sqrt(4/19))                                       # needs sage.symbolic
        doctest:...: UserWarning: the continued fraction of 2*sqrt(1/19) seems infinite,
        return only the first 20 terms
        [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 16]

    An examples with the list of partial convergents::

        sage: continued_fraction_list(RR(pi), partial_convergents=True)                 # needs sage.symbolic
        ([3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 3],
         [(3, 1),
          (22, 7),
          (333, 106),
          (355, 113),
          (103993, 33102),
          (104348, 33215),
          (208341, 66317),
          (312689, 99532),
          (833719, 265381),
          (1146408, 364913),
          (4272943, 1360120),
          (5419351, 1725033),
          (80143857, 25510582),
          (245850922, 78256779)])

    TESTS::

        sage: continued_fraction_list(1 + 10^-10, nterms=3)
        [1, 10000000000]
        sage: continued_fraction_list(1 + 10^-20 - e^-100, nterms=3)                    # needs sage.symbolic
        [1, 100000000000000000000, 2688]
        sage: continued_fraction_list(1 + 10^-20 - e^-100, nterms=5)                    # needs sage.symbolic
        [1, 100000000000000000000, 2688, 8, 1]
        sage: continued_fraction_list(1 + 10^-20 - e^-100, nterms=5)                    # needs sage.symbolic
        [1, 100000000000000000000, 2688, 8, 1]

    Fixed :issue:`18901`::

        sage: a = 1.575709393346379
        sage: type(a)                                                                   # needs sage.rings.real_mpfr
        <class 'sage.rings.real_mpfr.RealLiteral'>
        sage: continued_fraction_list(a)
        [1, 1, 1, 2, 1, 4, 18, 1, 5, 2, 25037802, 7, 1, 3, 1, 28, 1, 8, 2]

    Check that this works for arb elements (:issue:`20069`)::

        sage: continued_fraction(RBF(e))                                                # needs sage.symbolic
        [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12]
    """
def continued_fraction(x, value=None):
    '''
    Return the continued fraction of `x`.

    INPUT:

    - ``x`` -- a number or a list of partial quotients (for finite
      development) or two list of partial quotients (preperiod and period
      for ultimately periodic development)

    EXAMPLES:

    A finite continued fraction may be initialized by a number or by its list of
    partial quotients::

        sage: continued_fraction(12/571)
        [0; 47, 1, 1, 2, 2]
        sage: continued_fraction([3,2,1,4])
        [3; 2, 1, 4]

    It can be called with elements defined from symbolic values, in which case
    the partial quotients are evaluated in a lazy way::

        sage: c = continued_fraction(golden_ratio); c                                   # needs sage.symbolic
        [1; 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...]
        sage: c.convergent(12)                                                          # needs sage.symbolic
        377/233
        sage: fibonacci(14)/fibonacci(13)                                               # needs sage.libs.pari
        377/233

        sage: # needs sage.symbolic
        sage: continued_fraction(pi)
        [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
        sage: c = continued_fraction(pi); c
        [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
        sage: a = c.convergent(3); a
        355/113
        sage: a.n()
        3.14159292035398
        sage: pi.n()
        3.14159265358979

        sage: # needs sage.symbolic
        sage: continued_fraction(sqrt(2))
        [1; 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...]
        sage: continued_fraction(tan(1))
        [1; 1, 1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, ...]
        sage: continued_fraction(tanh(1))
        [0; 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, ...]
        sage: continued_fraction(e)
        [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, ...]

    If you want to play with quadratic numbers (such as ``golden_ratio`` and
    ``sqrt(2)`` above), it is much more convenient to use number fields as
    follows since preperiods and periods are computed::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, \'x\')
        sage: K.<sqrt5> = NumberField(x^2 - 5, embedding=2.23)
        sage: my_golden_ratio = (1 + sqrt5)/2
        sage: cf = continued_fraction((1+sqrt5)/2); cf
        [(1)*]
        sage: cf.convergent(12)
        377/233
        sage: cf.period()
        (1,)
        sage: cf = continued_fraction(2/3+sqrt5/5); cf
        [1; 8, (1, 3, 1, 1, 3, 9)*]
        sage: cf.preperiod()
        (1, 8)
        sage: cf.period()
        (1, 3, 1, 1, 3, 9)

        sage: # needs sage.rings.number_field
        sage: L.<sqrt2> = NumberField(x^2 - 2, embedding=1.41)
        sage: cf = continued_fraction(sqrt2); cf
        [1; (2)*]
        sage: cf.period()
        (2,)
        sage: cf = continued_fraction(sqrt2/3); cf
        [0; 2, (8, 4)*]
        sage: cf.period()
        (8, 4)

    It is also possible to go the other way around, build a ultimately periodic
    continued fraction from its preperiod and its period and get its value
    back::

        sage: cf = continued_fraction([(1,1), (2,8)]); cf
        [1; 1, (2, 8)*]
        sage: cf.value()                                                                # needs sage.rings.number_field
        2/11*sqrt5 + 14/11

    It is possible to deal with higher degree number fields but in that case the
    continued fraction expansion is known to be aperiodic::

        sage: K.<a> = NumberField(x^3 - 2, embedding=1.25)                              # needs sage.rings.number_field
        sage: cf = continued_fraction(a); cf                                            # needs sage.rings.number_field
        [1; 3, 1, 5, 1, 1, 4, 1, 1, 8, 1, 14, 1, 10, 2, 1, 4, 12, 2, 3, ...]

    Note that initial rounding can result in incorrect trailing partial
    quotients::

        sage: continued_fraction(RealField(39)(e))                                      # needs sage.symbolic
        [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 2]

    Note the value returned for floating point number is the continued fraction
    associated to the rational number you obtain with a conversion::

        sage: for _ in range(10):
        ....:     x = RR.random_element()
        ....:     cff = continued_fraction(x)
        ....:     cfe = QQ(x).continued_fraction()
        ....:     assert cff == cfe, "%s %s %s"%(x,cff,cfe)

    TESTS:

    Fixed :issue:`18901`. For RealLiteral, continued_fraction calls
    continued_fraction_list::

        sage: continued_fraction(1.575709393346379)
        [1; 1, 1, 2, 1, 4, 18, 1, 5, 2, 25037802, 7, 1, 3, 1, 28, 1, 8, 2]

    Constants in symbolic subrings work like constants in ``SR``::

        sage: SCR = SR.subring(no_variables=True)                                       # needs sage.symbolic
        sage: continued_fraction(SCR(pi))                                               # needs sage.symbolic
        [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, ...]
    '''
def convergents(x):
    """
    Return the (partial) convergents of the number ``x``.

    EXAMPLES::

        sage: from sage.rings.continued_fraction import convergents
        sage: convergents(143/255)
        [0, 1, 1/2, 4/7, 5/9, 9/16, 14/25, 23/41, 60/107, 143/255]
    """
