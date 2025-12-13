import _cython_3_2_1
import sage.rings.padics.pow_computer
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

PowComputer_relative_maker: _cython_3_2_1.cython_function_or_method

class PowComputer_relative(sage.rings.padics.pow_computer.PowComputer_class):
    """PowComputer_relative(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly, shift_seed)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 33)

    Base class for a ``PowComputer`` for use in `p`-adics implemented by Sage
    Polynomials.

    For a description of inputs see :func:`PowComputer_relative_maker`.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
        sage: R.<a> = ZqFM(25)
        sage: S.<x> = R[]
        sage: f = x^3 - 5*x - 5*a
        sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
        sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
        sage: PC = PowComputer_relative_maker(3, 20, 20, 60, False, f, shift_seed, 'fixed-mod')

    TESTS::

        sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative
        sage: isinstance(PC, PowComputer_relative)                                      # needs sage.libs.flint
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    base_ring: base_ring
    modulus: modulus
    poly_ring: poly_ring
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly, shift_seed) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 72)

                TESTS::

                    sage: # needs sage.libs.flint
                    sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
                    sage: R.<a> = ZqFM(25)
                    sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
                    sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
                    sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
                    sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')  # indirect doctest
                    sage: TestSuite(PC).run()
        """
    @overload
    def polynomial(self, n=..., var=...) -> Any:
        """PowComputer_relative.polynomial(self, n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 164)

        Return the modulus of the `p`-adic extension that is handled by this
        ``PowComputer``.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
            sage: R.<a> = ZqFM(25)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
            sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
            sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')  # indirect doctest
            sage: PC.polynomial() is f
            True"""
    @overload
    def polynomial(self) -> Any:
        """PowComputer_relative.polynomial(self, n=None, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 164)

        Return the modulus of the `p`-adic extension that is handled by this
        ``PowComputer``.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
            sage: R.<a> = ZqFM(25)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
            sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
            sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')  # indirect doctest
            sage: PC.polynomial() is f
            True"""
    def __reduce__(self) -> Any:
        """PowComputer_relative.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 117)

        Return a picklable representation of this ``PowComputer``.

        TESTS::

            sage: # needs sage.libs.flint
            sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
            sage: R.<a> = ZqFM(25)
            sage: S.<x> = R[]
            sage: f = x^3 - 5*x - 5*a
            sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
            sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
            sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')  # indirect doctest
            sage: loads(dumps(PC)) == PC
            True"""

class PowComputer_relative_eis(PowComputer_relative):
    """PowComputer_relative_eis(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly, shift_seed)

    File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 184)

    A ``PowComputer`` for a relative extension defined by an Eisenstein polynomial.

    For a description of inputs see :func:`PowComputer_relative_maker`.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_eis, PowComputer_relative_maker
        sage: R.<a> = ZqFM(25)
        sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
        sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
        sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
        sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')

    TESTS::

        sage: isinstance(PC, PowComputer_relative_eis)                                  # needs sage.libs.flint
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly, shift_seed) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 205)

                TESTS::

                    sage: # needs sage.libs.flint
                    sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
                    sage: R.<a> = ZqFM(25)
                    sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
                    sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
                    sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
                    sage: PC = PowComputer_relative_maker(5, 20, 20, 60, False, f, shift_seed, 'fixed-mod')
                    sage: TestSuite(PC).run()
        """
    def invert(self, Polynomial_generic_densea, longprec) -> Polynomial_generic_dense:
        """PowComputer_relative_eis.invert(self, Polynomial_generic_dense a, long prec) -> Polynomial_generic_dense

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 221)

        Return the inverse of ``a``.

        INPUT:

        - ``a`` -- a `p`-adic element, represented as a reduced
          Polynomial in ``poly_ring``

        - ``prec`` -- a ``long``, the required precision

        OUTPUT: a polynomial ``b`` such that ``a*b`` is one modulo `π^\\mathrm{prec}`

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker
            sage: R.<a> = ZqFM(25,3)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: W.<w> = R.ext(f)
            sage: g = 1 + 2*w; ginv = ~g
            sage: ginv
            1 + 3*w + 4*w^2 + 2*w^3 + (3*a + 3)*w^4 + ... + (3*a + 2)*w^8
            sage: RFP = R.change(field=False, show_prec=False, type='floating-point')
            sage: shift_seed = (-f[:3] // 5).change_ring(RFP)
            sage: PC = PowComputer_relative_maker(5, 3, 3, 9, False, f, shift_seed, 'fixed-mod')
            sage: g = 1 + 2*x
            sage: ginv = PC.invert(g, 5); ginv
            (4 + (3*a + 1)*5 + (2*a + 2)*5^2)*x^2 + (3 + (a + 1)*5 + (3*a + 2)*5^2)*x + 1 + 2*a*5 + 2*5^2"""
    def px_pow(self, r) -> Any:
        """PowComputer_relative_eis.px_pow(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 268)

        Return `p/π^r` where π is the uniformizer and `p` is the uniformizer of
        the base ring (not necessarily an integer.)

        INPUT:

        - ``r`` -- integer with 0 <= r < e

        OUTPUT: a reduced polynomial in π

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(25, prec=3)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: W.<w> = R.ext(f)
            sage: elt = W.prime_pow.px_pow(2); elt
            ((4*a + 4) + (4*a + 1)*5 + (4*a + 2)*5^2)*x^2 + ((2*a + 3) + (2*a + 4)*5 + (2*a + 4)*5^2)*x + (a + 1)*5 + 3*5^2 + 2*5^3"""
    def pxe_pow(self, r) -> Any:
        """PowComputer_relative_eis.pxe_pow(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 298)

        Return the ``r``-th power of the unit `p/π^e` where `e` is the relative
        ramification index and `p` is the uniformizer of the base ring (not necessarily an integer.)

        INPUT:

        - ``r`` -- nonnegative integer

        OUTPUT: a reduced polynomial in π

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(25, prec=3)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: W.<w> = R.ext(f)
            sage: elt = W.prime_pow.pxe_pow(2); elt
            ((4*a + 2) + (a + 4)*5 + 2*a*5^2)*x^2 + ((a + 2) + (a + 2)*5 + (2*a + 4)*5^2)*x + (a + 1) + (3*a + 2)*5 + (2*a + 2)*5^2"""
    def uniformizer_pow(self, r) -> Any:
        """PowComputer_relative_eis.uniformizer_pow(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_relative.pyx (starting at line 330)

        Return the ``r``-th power of the uniformizer.

        INPUT:

        - ``r`` -- nonnegative integer

        OUTPUT: a reduced polynomial in π

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<a> = Zq(25, prec=3)
            sage: S.<x> = R[]; f = x^3 - 5*x - 5*a
            sage: W.<w> = R.ext(f)
            sage: W.prime_pow.uniformizer_pow(2)
            x^2"""
