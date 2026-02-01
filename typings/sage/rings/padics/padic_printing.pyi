"""
`p`-adic Printing

This file contains code for printing `p`-adic elements.

It has been moved here to prevent code duplication and make finding
the relevant code easier.

AUTHORS:

- David Roe
"""
import sage.structure.sage_object
from sage.misc.latex import latex_variable_name as latex_variable_name
from sage.rings.padics.misc import trim_zeros as trim_zeros
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

def pAdicPrinter(ring, options={}):
    """
    Create a :class:`pAdicPrinter`.

    INPUT:

    - ``ring`` -- a `p`-adic ring or field

    - ``options`` -- dictionary, with keys in ``'mode'``, ``'pos'``,
      ``'ram_name'``, ``'unram_name'``, ``'var_name'``, ``'max_ram_terms'``,
      ``'max_unram_terms'``, ``'max_terse_terms'``, ``'sep'``, ``'alphabet'``; see
      :class:`pAdicPrinter_class` for the meanings of these keywords.

    EXAMPLES::

        sage: from sage.rings.padics.padic_printing import pAdicPrinter
        sage: R = Zp(5)
        sage: pAdicPrinter(R, {'sep': '&'})
        series printer for 5-adic Ring with capped relative precision 20
    """

class pAdicPrinterDefaults(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 75)

        This class stores global defaults for `p`-adic printing.
    """
    def __init__(self, mode=..., pos=..., max_ram_terms=..., max_unram_terms=..., max_terse_terms=..., sep=..., alphabet=...) -> Any:
        """pAdicPrinterDefaults.__init__(self, mode='series', pos=True, max_ram_terms=-1, max_unram_terms=-1, max_terse_terms=-1, sep='|', alphabet=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 79)

        Instances of this class store global defaults used in
        determining printing options during the creation of `p`-adic
        rings and fields.  One instance stored in padic_printing
        stores the globally relevant default values.

        See pAdicPrinter_class for details on the meanings of these
        inputs.

        TESTS::

            sage: from sage.rings.padics.padic_printing import pAdicPrinterDefaults
            sage: D = pAdicPrinterDefaults(sep='&'); D.sep()
            '&'"""
    @overload
    def allow_negatives(self, neg=...) -> Any:
        """pAdicPrinterDefaults.allow_negatives(self, neg=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 155)

        Controls whether or not to display a balanced representation.

        ``neg=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.allow_negatives(True)
            sage: padic_printing.allow_negatives()
            True
            sage: Qp(29)(-1)
            -1 + O(29^20)
            sage: Qp(29)(-1000)
            -14 - 5*29 - 29^2 + O(29^20)
            sage: padic_printing.allow_negatives(False)"""
    @overload
    def allow_negatives(self, _True) -> Any:
        """pAdicPrinterDefaults.allow_negatives(self, neg=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 155)

        Controls whether or not to display a balanced representation.

        ``neg=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.allow_negatives(True)
            sage: padic_printing.allow_negatives()
            True
            sage: Qp(29)(-1)
            -1 + O(29^20)
            sage: Qp(29)(-1000)
            -14 - 5*29 - 29^2 + O(29^20)
            sage: padic_printing.allow_negatives(False)"""
    @overload
    def allow_negatives(self) -> Any:
        """pAdicPrinterDefaults.allow_negatives(self, neg=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 155)

        Controls whether or not to display a balanced representation.

        ``neg=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.allow_negatives(True)
            sage: padic_printing.allow_negatives()
            True
            sage: Qp(29)(-1)
            -1 + O(29^20)
            sage: Qp(29)(-1000)
            -14 - 5*29 - 29^2 + O(29^20)
            sage: padic_printing.allow_negatives(False)"""
    @overload
    def allow_negatives(self, _False) -> Any:
        """pAdicPrinterDefaults.allow_negatives(self, neg=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 155)

        Controls whether or not to display a balanced representation.

        ``neg=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.allow_negatives(True)
            sage: padic_printing.allow_negatives()
            True
            sage: Qp(29)(-1)
            -1 + O(29^20)
            sage: Qp(29)(-1000)
            -14 - 5*29 - 29^2 + O(29^20)
            sage: padic_printing.allow_negatives(False)"""
    def alphabet(self, alphabet=...) -> Any:
        '''pAdicPrinterDefaults.alphabet(self, alphabet=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 276)

        Controls the alphabet used to translate `p`-adic digits into
        strings (so that no separator need be used in ``\'digits\'`` mode).

        ``alphabet`` should be passed in as a list or tuple.

        ``alphabet=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.alphabet("abc")
            sage: padic_printing.mode(\'digits\')
            sage: repr(Qp(3)(1234))
            \'...bcaacab\'

            sage: padic_printing.mode(\'series\')
            sage: padic_printing.alphabet((\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'A\',\'B\',\'C\',\'D\',\'E\',\'F\',\'G\',\'H\',\'I\',\'J\',\'K\',\'L\',\'M\',\'N\',\'O\',\'P\',\'Q\',\'R\',\'S\',\'T\',\'U\',\'V\',\'W\',\'X\',\'Y\',\'Z\',\'a\',\'b\',\'c\',\'d\',\'e\',\'f\',\'g\',\'h\',\'i\',\'j\',\'k\',\'l\',\'m\',\'n\',\'o\',\'p\',\'q\',\'r\',\'s\',\'t\',\'u\',\'v\',\'w\',\'x\',\'y\',\'z\'))'''
    @overload
    def max_poly_terms(self, max=...) -> Any:
        """pAdicPrinterDefaults.max_poly_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 227)

        Controls the number of terms appearing when printing
        polynomial representations in ``'terse'`` or ``'val-unit'`` modes.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_poly_terms(3)
            sage: padic_printing.max_poly_terms()
            3
            sage: padic_printing.mode('terse')
            sage: Zq(7^5, 5, names='a')([2,3,4])^8                                      # needs sage.libs.ntl
            2570 + 15808*a + 9018*a^2 + ... + O(7^5)

            sage: padic_printing.max_poly_terms(-1)
            sage: padic_printing.mode('series')"""
    @overload
    def max_poly_terms(self) -> Any:
        """pAdicPrinterDefaults.max_poly_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 227)

        Controls the number of terms appearing when printing
        polynomial representations in ``'terse'`` or ``'val-unit'`` modes.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_poly_terms(3)
            sage: padic_printing.max_poly_terms()
            3
            sage: padic_printing.mode('terse')
            sage: Zq(7^5, 5, names='a')([2,3,4])^8                                      # needs sage.libs.ntl
            2570 + 15808*a + 9018*a^2 + ... + O(7^5)

            sage: padic_printing.max_poly_terms(-1)
            sage: padic_printing.mode('series')"""
    @overload
    def max_series_terms(self, max=...) -> Any:
        """pAdicPrinterDefaults.max_series_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 177)

        Controls the maximum number of terms shown when printing in
        ``'series'``, ``'digits'`` or ``'bars'`` mode.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_series_terms(2)
            sage: padic_printing.max_series_terms()
            2
            sage: Qp(31)(1000)
            8 + 31 + ... + O(31^20)
            sage: padic_printing.max_series_terms(-1)
            sage: Qp(37)(100000)
            26 + 37 + 36*37^2 + 37^3 + O(37^20)"""
    @overload
    def max_series_terms(self) -> Any:
        """pAdicPrinterDefaults.max_series_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 177)

        Controls the maximum number of terms shown when printing in
        ``'series'``, ``'digits'`` or ``'bars'`` mode.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_series_terms(2)
            sage: padic_printing.max_series_terms()
            2
            sage: Qp(31)(1000)
            8 + 31 + ... + O(31^20)
            sage: padic_printing.max_series_terms(-1)
            sage: Qp(37)(100000)
            26 + 37 + 36*37^2 + 37^3 + O(37^20)"""
    @overload
    def max_unram_terms(self, max=...) -> Any:
        """pAdicPrinterDefaults.max_unram_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 202)

        For rings with non-prime residue fields, controls how many
        terms appear in the coefficient of each ``pi^n`` when printing in
        ``'series'`` or ``'bar'`` modes.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_unram_terms(2)
            sage: padic_printing.max_unram_terms()
            2
            sage: Zq(5^6, 5, names='a')([1,2,3,-1])^17                                  # needs sage.libs.ntl
            (3*a^4 + ... + 3) + (a^5 + ... + a)*5 + (3*a^3 + ... + 2)*5^2 + (3*a^5 + ... + 2)*5^3 + (4*a^5 + ... + 4)*5^4 + O(5^5)

            sage: padic_printing.max_unram_terms(-1)"""
    @overload
    def max_unram_terms(self) -> Any:
        """pAdicPrinterDefaults.max_unram_terms(self, max=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 202)

        For rings with non-prime residue fields, controls how many
        terms appear in the coefficient of each ``pi^n`` when printing in
        ``'series'`` or ``'bar'`` modes.

        ``max=None`` returns the current value.

        ``max=-1`` encodes 'no limit.'

        EXAMPLES::

            sage: padic_printing.max_unram_terms(2)
            sage: padic_printing.max_unram_terms()
            2
            sage: Zq(5^6, 5, names='a')([1,2,3,-1])^17                                  # needs sage.libs.ntl
            (3*a^4 + ... + 3) + (a^5 + ... + a)*5 + (3*a^3 + ... + 2)*5^2 + (3*a^5 + ... + 2)*5^3 + (4*a^5 + ... + 4)*5^4 + O(5^5)

            sage: padic_printing.max_unram_terms(-1)"""
    @overload
    def mode(self, mode=...) -> Any:
        """pAdicPrinterDefaults.mode(self, mode=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 114)

        Set the default printing mode.

        ``mode=None`` returns the current value.

        The allowed values for mode are: ``'val-unit'``, ``'series'``,
        ``'terse'``, ``'digits'`` and ``'bars'``.

        EXAMPLES::

            sage: padic_printing.mode('terse')
            sage: padic_printing.mode()
            'terse'
            sage: Qp(7)(100)
            100 + O(7^20)
            sage: padic_printing.mode('series')
            sage: Qp(11)(100)
            1 + 9*11 + O(11^20)
            sage: padic_printing.mode('val-unit')
            sage: Qp(13)(130)
            13 * 10 + O(13^21)
            sage: padic_printing.mode('digits')
            sage: repr(Qp(17)(100))
            '...5F'
            sage: repr(Qp(17)(1000))
            '...37E'
            sage: padic_printing.mode('bars')
            sage: repr(Qp(19)(1000))
            '...2|14|12'

            sage: padic_printing.mode('series')"""
    @overload
    def mode(self) -> Any:
        """pAdicPrinterDefaults.mode(self, mode=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 114)

        Set the default printing mode.

        ``mode=None`` returns the current value.

        The allowed values for mode are: ``'val-unit'``, ``'series'``,
        ``'terse'``, ``'digits'`` and ``'bars'``.

        EXAMPLES::

            sage: padic_printing.mode('terse')
            sage: padic_printing.mode()
            'terse'
            sage: Qp(7)(100)
            100 + O(7^20)
            sage: padic_printing.mode('series')
            sage: Qp(11)(100)
            1 + 9*11 + O(11^20)
            sage: padic_printing.mode('val-unit')
            sage: Qp(13)(130)
            13 * 10 + O(13^21)
            sage: padic_printing.mode('digits')
            sage: repr(Qp(17)(100))
            '...5F'
            sage: repr(Qp(17)(1000))
            '...37E'
            sage: padic_printing.mode('bars')
            sage: repr(Qp(19)(1000))
            '...2|14|12'

            sage: padic_printing.mode('series')"""
    @overload
    def sep(self, sep=...) -> Any:
        """pAdicPrinterDefaults.sep(self, sep=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 253)

        Controls the separator used in ``'bars'`` mode.

        ``sep=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.sep('][')
            sage: padic_printing.sep()
            ']['
            sage: padic_printing.mode('bars')
            sage: repr(Qp(61)(-1))
            '...60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60'

            sage: padic_printing.sep('|')
            sage: padic_printing.mode('series')"""
    @overload
    def sep(self) -> Any:
        """pAdicPrinterDefaults.sep(self, sep=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 253)

        Controls the separator used in ``'bars'`` mode.

        ``sep=None`` returns the current value.

        EXAMPLES::

            sage: padic_printing.sep('][')
            sage: padic_printing.sep()
            ']['
            sage: padic_printing.mode('bars')
            sage: repr(Qp(61)(-1))
            '...60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60][60'

            sage: padic_printing.sep('|')
            sage: padic_printing.mode('series')"""

_printer_defaults: pAdicPrinterDefaults = pAdicPrinterDefaults()

class pAdicPrinter_class(sage.structure.sage_object.SageObject):
    """pAdicPrinter_class(ring, mode, pos, ram_name, unram_name, var_name, max_ram_terms, max_unram_terms, max_terse_terms, sep, alphabet, show_prec)

    File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 304)

    This class stores the printing options for a specific `p`-adic ring
    or field, and uses these to compute the representations of
    elements."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ring, mode, pos, ram_name, unram_name, var_name, max_ram_terms, max_unram_terms, max_terse_terms, sep, alphabet, show_prec) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 310)

                Initialize a :class:`pAdicPrinter`.

                INPUT:

                - ``ring`` -- the ring or field to which this :class:`pAdicPrinter` is
                  attached

                - ``mode`` -- the allowed values for mode are: ``'val-unit'``,
                  ``'series'``, ``'terse'``, ``'digits'`` and ``'bars'``:

                  - ``'val-unit'`` -- elements are displayed as a power of the
                    uniformizer times a unit, which is displayed in terse mode

                  - ``'series'`` -- elements are displayed as power series in the
                    uniformizer

                  - ``'terse'`` -- for base rings and fields, elements are just
                    displayed as an integer lift.  For extensions rings and fields,
                    elements are displayed as a polynomial in the generator of the
                    extension.

                  - ``'digits'`` -- used only for small primes and totally ramified
                    extensions (or trivial extensions), elements are displayed as just
                    a string of `p`-adic digits, encoded using the 'alphabet' parameter

                  - ``'bars'`` -- like ``'digits'``, but uses a separator in order to
                    print a more canonical representation for each digit. This change
                    allows the use of this printing mode for unramified extensions and
                    extensions with larger primes.

                - ``pos`` -- if ``True`` then integers in the range [0,... p-1] will be
                  used; if ``False`` integers in the range [(1-p)/2,..., p/2] will be used

                - ``ram_name`` -- the string used to represent the uniformizer

                - ``unram_name`` -- the string used to represent the trivial lift of a
                  generator of the residue field over the prime field

                - ``var_name`` -- the string used to represent the user-specified
                  generator of this extension ring or field

                - ``max_ram_terms`` -- controls the maximum number of terms shown when
                  printing in ``'series'``, ``'digits'`` or ``'bars'`` mode

                - ``max_unram_terms`` -- for rings with non-prime residue fields,
                  controls how many terms appear in the coefficient of each pi^n when
                  printing in ``'series'`` or ``'bar'`` modes

                - ``max_terse_terms`` -- controls the number of terms appearing when
                  printing polynomial representations in ``'terse'`` or ``'val-unit'``
                  modes

                - ``sep`` -- controls the separator used in ``'bars'`` mode

                - ``alphabet`` -- controls the alphabet used to translate `p`-adic digits
                  into strings (so that no separator need be used in ``'digits'`` mode)

                - ``show_prec`` -- Specify how the precision is printed; it can be
                  ``'none'``, ``'bigoh'`` or ``'dots'`` (the latter being not available
                  for all modes)

                TESTS::

                    sage: R = Qp(7, print_mode='bars', print_sep='&')  # indirect doctest

                    sage: R = Zp(5, print_mode='digits', print_max_terms=10)
                    Traceback (most recent call last):
                    ...
                    ValueError: max_ram_terms must be unset when show_prec is 'dots'
        """
    def dict(self) -> Any:
        """pAdicPrinter_class.dict(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 630)

        Return a dictionary storing all of ``self``'s printing options.

        EXAMPLES::

            sage: D = Zp(5)._printer.dict(); D['sep']
            '|'"""
    @overload
    def repr_gen(self, elt, do_latex, pos=..., mode=..., ram_name=...) -> Any:
        """pAdicPrinter_class.repr_gen(self, elt, do_latex, pos=None, mode=None, ram_name=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 837)

        The entry point for printing an element.

        INPUT:

        - ``elt`` -- a `p`-adic element of the appropriate ring to print

        - ``do_latex`` -- whether to return a latex representation or
          a normal one

        EXAMPLES::

            sage: R = Zp(5,5); P = R._printer; a = R(-5); a
            4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + O(5^6)
            sage: P.repr_gen(a, False, pos=False)
            '-5 + O(5^6)'
            sage: P.repr_gen(a, False, ram_name='p')
            '4*p + 4*p^2 + 4*p^3 + 4*p^4 + 4*p^5 + O(p^6)'"""
    @overload
    def repr_gen(self, a, _False, pos=...) -> Any:
        """pAdicPrinter_class.repr_gen(self, elt, do_latex, pos=None, mode=None, ram_name=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 837)

        The entry point for printing an element.

        INPUT:

        - ``elt`` -- a `p`-adic element of the appropriate ring to print

        - ``do_latex`` -- whether to return a latex representation or
          a normal one

        EXAMPLES::

            sage: R = Zp(5,5); P = R._printer; a = R(-5); a
            4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + O(5^6)
            sage: P.repr_gen(a, False, pos=False)
            '-5 + O(5^6)'
            sage: P.repr_gen(a, False, ram_name='p')
            '4*p + 4*p^2 + 4*p^3 + 4*p^4 + 4*p^5 + O(p^6)'"""
    @overload
    def repr_gen(self, a, _False, ram_name=...) -> Any:
        """pAdicPrinter_class.repr_gen(self, elt, do_latex, pos=None, mode=None, ram_name=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 837)

        The entry point for printing an element.

        INPUT:

        - ``elt`` -- a `p`-adic element of the appropriate ring to print

        - ``do_latex`` -- whether to return a latex representation or
          a normal one

        EXAMPLES::

            sage: R = Zp(5,5); P = R._printer; a = R(-5); a
            4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + O(5^6)
            sage: P.repr_gen(a, False, pos=False)
            '-5 + O(5^6)'
            sage: P.repr_gen(a, False, ram_name='p')
            '4*p + 4*p^2 + 4*p^3 + 4*p^4 + 4*p^5 + O(p^6)'"""
    def richcmp_modes(self, pAdicPrinter_classother, intop) -> Any:
        """pAdicPrinter_class.richcmp_modes(self, pAdicPrinter_class other, int op)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 507)

        Return a comparison of the printing modes of ``self`` and ``other``.

        Return 0 if and only if all relevant modes are equal
        (``max_unram_terms`` is irrelevant if the ring is totally ramified
        over the base, for example). This does not check if the rings are
        equal (to prevent infinite recursion in the comparison
        functions of `p`-adic rings), but it does check if the primes
        are the same (since the prime affects whether ``pos`` is
        relevant).

        EXAMPLES::

            sage: R = Qp(7, print_mode='digits', print_pos=True)
            sage: S = Qp(7, print_mode='digits', print_pos=False)
            sage: R._printer == S._printer
            True
            sage: R = Qp(7)
            sage: S = Qp(7, print_mode='val-unit')
            sage: R == S
            False
            sage: R._printer < S._printer
            True"""
    def __enter__(self) -> Any:
        """pAdicPrinter_class.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 615)

        Used for context printing.

        EXAMPLES::

            sage: from sage.rings.padics.padic_printing import pAdicPrinter
            sage: R = Zp(5,5); a = R(-1); a
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5)
            sage: with pAdicPrinter(R, {'pos': False}): a
            -1 + O(5^5)"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __exit__(self, type, value, traceback) -> Any:
        """pAdicPrinter_class.__exit__(self, type, value, traceback)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 641)

        Used for context printing.

        EXAMPLES::

            sage: from sage.rings.padics.padic_printing import pAdicPrinter
            sage: R = Zp(5,5); a = R(-1); a
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5)
            sage: with pAdicPrinter(R, {'pos': False}): a
            -1 + O(5^5)
            sage: a
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5)"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """pAdicPrinter_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_printing.pyx (starting at line 467)

        Pickling.

        TESTS::

            sage: R = Zp(5, print_mode='bars', print_sep='&'); P = loads(dumps(R._printer))
            sage: R._printer == P
            True
            sage: P._sep()
            '&'"""
