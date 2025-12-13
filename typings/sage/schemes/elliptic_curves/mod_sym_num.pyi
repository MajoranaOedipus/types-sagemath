import sage as sage
import sage.rings.fast_arith
from sage.arith.misc import euler_phi as euler_phi, kronecker_symbol as kronecker_symbol
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

fa: sage.rings.fast_arith.arith_llong

class ModularSymbolNumerical:
    '''ModularSymbolNumerical(E, sign=1)

    File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 685)

    This class assigning to an elliptic curve over `\\QQ` a modular symbol.
    Unlike the other implementations this class does not precompute a
    basis for this space. Instead at each call, it evaluates the integral
    using numerical approximation. All bounds are very strictly
    implemented and the output is a correct proven rational number.

    INPUT:

    - ``E`` -- an elliptic curve over the rational numbers

    - ``sign`` -- either -1 or +1 (default). This sets the default
      value of ``sign`` throughout the class. Both are still accessible.

    OUTPUT: a modular symbol

    EXAMPLES::

        sage: E = EllipticCurve("5077a1")
        sage: M = E.modular_symbol(implementation=\'num\')
        sage: M(0)
        0
        sage: M(77/57)
        -1
        sage: M(33/37, -1)
        2
        sage: M = E.modular_symbol(sign=-1, implementation=\'num\')
        sage: M(2/7)
        2

        sage: from sage.schemes.elliptic_curves.mod_sym_num \\\n        ....: import ModularSymbolNumerical
        sage: M = ModularSymbolNumerical(EllipticCurve("11a1"))
        sage: M(1/3, -1)
        1/2
        sage: M(1/2)
        -4/5'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, E, sign=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 766)

                See the class docstring for full documentation.

                EXAMPLES::

                    sage: E = EllipticCurve("27a1")
                    sage: M = E. modular_symbol(implementation=\'num\')
                    sage: M(1/9)
                    1/2
                    sage: M(1/3)
                    -1/6
                    sage: M(1/3, -1)
                    1/6
        '''
    def all_values_for_one_denominator(self, llongm, intsign=...) -> Any:
        """ModularSymbolNumerical.all_values_for_one_denominator(self, llong m, int sign=0)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 3111)

        Given an integer ``m`` and a ``sign``, this returns the
        modular symbols `[a/m]` for all `a` coprime to `m`
        using partial sums.
        This is much quicker than computing them one by one.

        This will only work if `m` is relatively small and
        if the cusps `a/m` are unitary.

        INPUT:

        - ``m`` -- a natural number

        - ``sign`` -- either +1 or -1, or 0 (default),
          in which case the sign passed to the class is taken

        OUTPUT: a dictionary of fractions with denominator `m`
        giving rational numbers.

        EXAMPLES::

            sage: E = EllipticCurve('5077a1')
            sage: M = E.modular_symbol(implementation='num')
            sage: M.all_values_for_one_denominator(7)
            {1/7: 3, 2/7: 0, 3/7: -3, 4/7: -3, 5/7: 0, 6/7: 3}
            sage: [M(a/7) for a in [1..6]]
            [3, 0, -3, -3, 0, 3]
            sage: M.all_values_for_one_denominator(3,-1)
            {1/3: 4, 2/3: -4}

            sage: E = EllipticCurve('11a1')
            sage: M = E.modular_symbol(implementation='num')
            sage: M.all_values_for_one_denominator(12)
            {1/12: 1/5, 5/12: -23/10, 7/12: -23/10, 11/12: 1/5}
            sage: M.all_values_for_one_denominator(12, -1)
            {1/12: 0, 5/12: 1/2, 7/12: -1/2, 11/12: 0}

            sage: E = EllipticCurve('20a1')
            sage: M = E.modular_symbol(implementation='num')
            sage: M.all_values_for_one_denominator(4)
            {1/4: 0, 3/4: 0}
            sage: M.all_values_for_one_denominator(8)
            {1/8: 1/2, 3/8: -1/2, 5/8: -1/2, 7/8: 1/2}"""
    def approximative_value(self, r, intsign=..., intprec=..., use_twist=...) -> Any:
        '''ModularSymbolNumerical.approximative_value(self, r, int sign=0, int prec=20, use_twist=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 903)

        The numerical modular symbol evaluated at rational.

        It returns a real number, which should be equal
        to a rational number to the given binary
        precision ``prec``. In practice the precision is
        often much higher. See the examples below.

        INPUT:

        - ``r`` -- a rational (or integer)

        - ``sign`` -- either +1 or -1, or 0 (default),
          in which case the sign passed to the class is taken

        - ``prec`` -- integer (default: 20)

        - ``use_twist`` -- ``True`` (default) allows to use a
          quadratic twist of the curve to lower the conductor

        OUTPUT: a real number

        EXAMPLES::

            sage: E = EllipticCurve("5077a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.approximative_value(123/567)  # abs tol 1e-11
            -4.00000000000845
            sage: M.approximative_value(123/567,prec=2) # abs tol 1e-9
            -4.00002815242902

            sage: E = EllipticCurve([11,88])
            sage: E.conductor()
            1715296
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.approximative_value(0,prec=2)   # abs tol 1e-11
            -0.0000176374317982166
            sage: M.approximative_value(1/7,prec=2)  # abs tol 1e-11
            0.999981178147778
            sage: M.approximative_value(1/7,prec=10) # abs tol 1e-11
            0.999999972802649'''
    @overload
    def clear_cache(self) -> Any:
        '''ModularSymbolNumerical.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 1349)

        Clear the cached values in all methods of this class.

        EXAMPLES::

            sage: E = EllipticCurve("11a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M(0)
            1/5
            sage: M.clear_cache()
            sage: M(0)
            1/5'''
    @overload
    def clear_cache(self) -> Any:
        '''ModularSymbolNumerical.clear_cache(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 1349)

        Clear the cached values in all methods of this class.

        EXAMPLES::

            sage: E = EllipticCurve("11a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M(0)
            1/5
            sage: M.clear_cache()
            sage: M(0)
            1/5'''
    @overload
    def elliptic_curve(self) -> Any:
        '''ModularSymbolNumerical.elliptic_curve(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 829)

        Return the elliptic curve of this modular symbol.

        EXAMPLES::

            sage: E = EllipticCurve("15a4")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.elliptic_curve()
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + 35*x - 28 over Rational Field'''
    @overload
    def elliptic_curve(self) -> Any:
        '''ModularSymbolNumerical.elliptic_curve(self)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 829)

        Return the elliptic curve of this modular symbol.

        EXAMPLES::

            sage: E = EllipticCurve("15a4")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.elliptic_curve()
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + 35*x - 28 over Rational Field'''
    def manin_symbol(self, llongu, llongv, intsign=...) -> Any:
        """ModularSymbolNumerical.manin_symbol(self, llong u, llong v, int sign=0)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 2850)

        Given a pair `(u,v)` presenting a point in
        `\\mathbb{P}^1(\\mathbb{Z}/N\\mathbb{Z})` and hence a coset of
        `\\Gamma_0(N)`, this computes the value of the Manin
        symbol `M(u:v)`.

        INPUT:

        - ``u`` -- integer

        - ``v`` -- integer such that `(u:v)` is a projective point
          modulo `N`

        - ``sign`` -- either +1 or -1, or 0 (default),
          in which case the sign passed to the class is taken

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: M = E.modular_symbol(implementation='num')
            sage: M.manin_symbol(1,3)
            -1/2
            sage: M.manin_symbol(1,3, sign=-1)
            -1/2
            sage: M.manin_symbol(1,5)
            1
            sage: M.manin_symbol(1,5)
            1

            sage: E = EllipticCurve('14a1')
            sage: M = E.modular_symbol(implementation='num')
            sage: M.manin_symbol(1,2)
            -1/2
            sage: M.manin_symbol(17,6)
            -1/2
            sage: M.manin_symbol(-1,12)
            -1/2"""
    def transportable_symbol(self, Rationalr, Rationalrr, intsign=...) -> Any:
        '''ModularSymbolNumerical.transportable_symbol(self, Rational r, Rational rr, int sign=0)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 2595)

        Return the symbol `[r\']^+ - [r]^+` where `r\'=\\gamma(r)` for some
        `\\gamma\\in\\Gamma_0(N)`. These symbols can be computed by transporting
        the path into the upper half plane close to one of the unitary cusps.
        Here we have implemented it only to move close to `i\\infty` and `0`.

        INPUT:

        - ``r``, ``rr`` -- two rational numbers

        - ``sign`` -- either +1 or -1, or 0 (default),
          in which case the sign passed to the class is taken

        OUTPUT: a rational number

        EXAMPLES::

            sage: E = EllipticCurve("11a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.transportable_symbol(0/1,-2/7)
            -1/2

            sage: E = EllipticCurve("37a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.transportable_symbol(0/1,-1/19)
            0
            sage: M.transportable_symbol(0/1,-1/19,-1)
            0

            sage: E = EllipticCurve("5077a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M.transportable_symbol(0/1,-35/144)
            -3
            sage: M.transportable_symbol(0/1,-35/144,-1)
            0
            sage: M.transportable_symbol(0/1, -7/31798)
            0
            sage: M.transportable_symbol(0/1, -7/31798, -1)
            -5'''
    def __call__(self, r, intsign=..., use_twist=...) -> Any:
        '''ModularSymbolNumerical.__call__(self, r, int sign=0, use_twist=True)

        File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 842)

        The modular symbol evaluated at rational. It returns a
        rational number.

        INPUT:

        - ``r`` -- a rational (or integer)

        - ``sign`` -- either +1 or -1, or 0 (default),
          in which case the sign passed to the class is taken

        - ``use_twist`` -- boolean (default: ``True``); decides if we
          allow to use a quadratic twist

        OUTPUT: a rational number

        EXAMPLES::

            sage: E = EllipticCurve("36a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M(2/5)
            -1/3
            sage: M(2/5, -1)
            1/2

            sage: E = EllipticCurve("54a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M(5/9)
            -1/2

            sage: E = EllipticCurve("5077a1")
            sage: M = E.modular_symbol(implementation=\'num\')
            sage: M(234/567)
            0
            sage: M(112379/43568779)
            5'''

class _CuspsForModularSymbolNumerical:
    """_CuspsForModularSymbolNumerical(Rational r, llong N)

    File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 557)

    Minimalistic class implementing cusps (not `\\infty`).
    Here a cusp is a rational number together with a level.
    This class provides the methods atkin_lehner and
    is_unitary and attaches _width, _a, _m to it.

    It is to only to be used internally."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Rationalr, llongN) -> Any:
        """File: /build/sagemath/src/sage/src/sage/schemes/elliptic_curves/mod_sym_num.pyx (starting at line 570)

                The rational (non-infinite) cusp r on X_0(N).

                INPUT:

                - ``r`` -- a rational number

                - ``N`` -- the level as a long long

                EXAMPLES::

                    sage: from sage.schemes.elliptic_curves.mod_sym_num \\\n                    ....: import _CuspsForModularSymbolNumerical
                    sage: r = _CuspsForModularSymbolNumerical(3/7,99)
        """
