import _cython_3_2_1
import sage.rings.padics.pow_computer
from sage.categories.category import ZZ as ZZ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

PowComputer_flint_maker: _cython_3_2_1.cython_function_or_method

class PowComputer_flint(sage.rings.padics.pow_computer.PowComputer_class):
    """PowComputer_flint(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None, shift_seed=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 24)

    A PowComputer for use in `p`-adics implemented via FLINT.

    For a description of inputs see :func:`PowComputer_flint_maker`.

    EXAMPLES::

        sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint
        sage: PowComputer_flint(5, 20, 20, 20, False)
        FLINT PowComputer for 5"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=..., shift_seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 63)

                Initialization.

                TESTS::

                    sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_maker
                    sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
                    sage: A = PowComputer_flint_maker(5, 20, 20, 20, False, f, 'capped-rel')  # indirect doctest
                    sage: TestSuite(A).run()
        """
    @overload
    def polynomial(self, n=..., var=...) -> Any:
        """PowComputer_flint.polynomial(self, n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 166)

        Return ``None``.

        For consistency with subclasses.

        EXAMPLES::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint
            sage: A = PowComputer_flint(5, 20, 20, 20, False, None)
            sage: A.polynomial() is None
            True"""
    @overload
    def polynomial(self) -> Any:
        """PowComputer_flint.polynomial(self, n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 166)

        Return ``None``.

        For consistency with subclasses.

        EXAMPLES::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint
            sage: A = PowComputer_flint(5, 20, 20, 20, False, None)
            sage: A.polynomial() is None
            True"""
    def __reduce__(self) -> Any:
        """PowComputer_flint.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 96)

        Pickling.

        TESTS::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_maker
            sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
            sage: A = PowComputer_flint_maker(5, 20, 20, 20, False, f, 'capped-rel')  # indirect doctest
            sage: A._test_pickling()  # indirect doctest"""

class PowComputer_flint_1step(PowComputer_flint):
    """PowComputer_flint_1step(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, _poly, shift_seed=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 181)

    A PowComputer for a `p`-adic extension defined by a single polynomial.

    For a description of inputs see :func:`PowComputer_flint_maker`.

    EXAMPLES::

        sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_1step
        sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
        sage: A = PowComputer_flint_1step(5, 20, 20, 20, False, f); A
        FLINT PowComputer for 5 with polynomial x^3 - 8*x - 2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, _poly, shift_seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 252)

                Initialization.

                TESTS::

                    sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_maker
                    sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
                    sage: A = PowComputer_flint_maker(5, 20, 20, 20, False, f, 'capped-rel')
                    sage: TestSuite(A).run()
        """
    @overload
    def polynomial(self, _n=..., var=...) -> Any:
        """PowComputer_flint_1step.polynomial(self, _n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 393)

        Return the polynomial attached to this ``PowComputer``, possibly
        reduced modulo a power of `p`.

        INPUT:

        - ``_n`` -- (default: ``None``) an integer, the power of `p`
          modulo which to reduce

        - ``var`` -- (default: ``'x'``) the variable for the returned polynomial

        .. NOTE::

            From Cython you should use :meth:`get_modulus` instead for
            speed.

        EXAMPLES::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_1step
            sage: R.<y> = ZZ[]; f = y^3 - 8*y - 2
            sage: A = PowComputer_flint_1step(5, 20, 20, 20, False, f)
            sage: A.polynomial()
            x^3 - 8*x - 2
            sage: A.polynomial(var='y')
            y^3 - 8*y - 2
            sage: A.polynomial(2)
            x^3 + 17*x + 23"""
    @overload
    def polynomial(self) -> Any:
        """PowComputer_flint_1step.polynomial(self, _n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 393)

        Return the polynomial attached to this ``PowComputer``, possibly
        reduced modulo a power of `p`.

        INPUT:

        - ``_n`` -- (default: ``None``) an integer, the power of `p`
          modulo which to reduce

        - ``var`` -- (default: ``'x'``) the variable for the returned polynomial

        .. NOTE::

            From Cython you should use :meth:`get_modulus` instead for
            speed.

        EXAMPLES::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_1step
            sage: R.<y> = ZZ[]; f = y^3 - 8*y - 2
            sage: A = PowComputer_flint_1step(5, 20, 20, 20, False, f)
            sage: A.polynomial()
            x^3 - 8*x - 2
            sage: A.polynomial(var='y')
            y^3 - 8*y - 2
            sage: A.polynomial(2)
            x^3 + 17*x + 23"""
    @overload
    def polynomial(self, var=...) -> Any:
        """PowComputer_flint_1step.polynomial(self, _n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 393)

        Return the polynomial attached to this ``PowComputer``, possibly
        reduced modulo a power of `p`.

        INPUT:

        - ``_n`` -- (default: ``None``) an integer, the power of `p`
          modulo which to reduce

        - ``var`` -- (default: ``'x'``) the variable for the returned polynomial

        .. NOTE::

            From Cython you should use :meth:`get_modulus` instead for
            speed.

        EXAMPLES::

            sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_1step
            sage: R.<y> = ZZ[]; f = y^3 - 8*y - 2
            sage: A = PowComputer_flint_1step(5, 20, 20, 20, False, f)
            sage: A.polynomial()
            x^3 - 8*x - 2
            sage: A.polynomial(var='y')
            y^3 - 8*y - 2
            sage: A.polynomial(2)
            x^3 + 17*x + 23"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
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

class PowComputer_flint_eis(PowComputer_flint_1step):
    """PowComputer_flint_eis(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 551)

    A PowComputer for a `p`-adic extension defined by an Eisenstein polynomial.

    For a description of inputs see :func:`PowComputer_flint_maker`.

    EXAMPLES::

        sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_eis
        sage: R.<x> = ZZ[]; f = x^3 - 25*x + 5
        sage: A = PowComputer_flint_eis(5, 20, 20, 60, False, f); A
        FLINT PowComputer for 5 with polynomial x^3 - 25*x + 5"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 564)

                Initialization.

                TESTS::

                    sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_eis
                    sage: R.<x> = ZZ[]; f = x^3 - 25*x + 5
                    sage: A = PowComputer_flint_eis(5, 20, 20, 60, False, f)
                    sage: type(A)
                    <class 'sage.rings.padics.pow_computer_flint.PowComputer_flint_eis'>
        """

class PowComputer_flint_unram(PowComputer_flint_1step):
    """PowComputer_flint_unram(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 442)

    A PowComputer for a `p`-adic extension defined by an unramified polynomial.

    For a description of inputs see :func:`PowComputer_flint_maker`.

    EXAMPLES::

        sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_unram
        sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
        sage: A = PowComputer_flint_unram(5, 20, 20, 20, False, f); A
        FLINT PowComputer for 5 with polynomial x^3 - 8*x - 2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_flint.pyx (starting at line 534)

                Initialization.

                TESTS::

                    sage: from sage.rings.padics.pow_computer_flint import PowComputer_flint_maker
                    sage: R.<x> = ZZ[]; f = x^3 - 8*x - 2
                    sage: A = PowComputer_flint_maker(5, 20, 20, 20, False, f, 'capped-rel')
                    sage: TestSuite(A).run()
        """
