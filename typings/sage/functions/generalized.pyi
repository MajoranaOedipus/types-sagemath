r"""
Generalized functions

Sage implements several generalized functions (also known as
distributions) such as Dirac delta, Heaviside step functions. These
generalized functions can be manipulated within Sage like any other
symbolic functions.


AUTHORS:

- Golam Mortuza Hossain (2009-06-26): initial version

EXAMPLES:

Dirac delta function::

    sage: dirac_delta(x)                                                                # needs sage.symbolic
    dirac_delta(x)

Heaviside step function::

    sage: heaviside(x)                                                                  # needs sage.symbolic
    heaviside(x)

Unit step function::

    sage: unit_step(x)                                                                  # needs sage.symbolic
    unit_step(x)

Signum (sgn) function::

    sage: sgn(x)                                                                        # needs sage.symbolic
    sgn(x)

Kronecker delta function::

    sage: m, n = var('m,n')                                                             # needs sage.symbolic
    sage: kronecker_delta(m, n)                                                         # needs sage.symbolic
    kronecker_delta(m, n)
"""

from sage.rings.integer_ring import ZZ as ZZ
from sage.symbolic.function import BuiltinFunction as BuiltinFunction, GinacFunction as GinacFunction

class FunctionDiracDelta(BuiltinFunction):
    """
    The Dirac delta (generalized) function, `\\delta(x)` (``dirac_delta(x)``).

    INPUT:

    - ``x`` -- a real number or a symbolic expression

    DEFINITION:

    Dirac delta function `\\delta(x)`, is defined in Sage as:

        `\\delta(x) = 0` for real `x \\ne 0` and
        `\\int_{-\\infty}^{\\infty} \\delta(x) dx = 1`

    Its alternate definition with respect to an arbitrary test
    function `f(x)` is

        `\\int_{-\\infty}^{\\infty} f(x) \\delta(x-a) dx = f(a)`

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: dirac_delta(1)
        0
        sage: dirac_delta(0)
        dirac_delta(0)
        sage: dirac_delta(x)
        dirac_delta(x)
        sage: integrate(dirac_delta(x), x, -1, 1, algorithm='sympy')                    # needs sympy
        1

    REFERENCES:

    - :wikipedia:`Dirac_delta_function`
    """
    def __init__(self) -> None:
        """
        The Dirac delta (generalized) function, ``dirac_delta(x)``.

        INPUT:

        - ``x`` -- a real number or a symbolic expression

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: dirac_delta(1)
            0
            sage: dirac_delta(0)
            dirac_delta(0)
            sage: dirac_delta(x)
            dirac_delta(x)
            sage: latex(dirac_delta(x))
            \\delta\\left(x\\right)

            sage: loads(dumps(dirac_delta(x)))                                          # needs sage.symbolic
            dirac_delta(x)
            sage: dirac_delta(x)._sympy_()                                              # needs sympy sage.symbolic
            DiracDelta(x)
        """

dirac_delta: FunctionDiracDelta

class FunctionHeaviside(GinacFunction):
    """
    The Heaviside step function, `H(x)` (``heaviside(x)``).

    INPUT:

    - ``x`` -- a real number or a symbolic expression

    DEFINITION:

    The Heaviside step function, `H(x)` is defined in Sage as:

        `H(x) = 0` for `x < 0` and `H(x) = 1` for `x > 0`

    .. SEEALSO:: :func:`unit_step()<sage.functions.generalized.FunctionUnitStep>`

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: heaviside(-1)
        0
        sage: heaviside(1)
        1
        sage: heaviside(0)
        heaviside(0)
        sage: heaviside(x)
        heaviside(x)

        sage: heaviside(-1/2)                                                           # needs sage.symbolic
        0
        sage: heaviside(exp(-1000000000000000000000))                                   # needs sage.symbolic
        1

    TESTS::

        sage: heaviside(x)._sympy_()                                                    # needs sympy sage.symbolic
        Heaviside(x)
        sage: heaviside(x).subs(x=1)                                                    # needs sage.symbolic
        1
        sage: heaviside(x).subs(x=-1)                                                   # needs sage.symbolic
        0

    ::

        sage: # needs sage.symbolic
        sage: ex = heaviside(x) + 1
        sage: t = loads(dumps(ex)); t
        heaviside(x) + 1
        sage: bool(t == ex)
        True
        sage: t.subs(x=1)
        2

    REFERENCES:

    -  :wikipedia:`Heaviside_function`
    """
    def __init__(self) -> None:
        """
        The Heaviside step function, ``heaviside(x)``.

        INPUT:

        - ``x`` -- a real number or a symbolic expression

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: heaviside(-1)
            0
            sage: heaviside(1)
            1
            sage: heaviside(0)
            heaviside(0)
            sage: heaviside(x)
            heaviside(x)
            sage: latex(heaviside(x))
            H\\left(x\\right)
            sage: heaviside(x)._sympy_()                                                # needs sympy
            Heaviside(x)
            sage: heaviside(x)._giac_()                                                 # needs giac
            Heaviside(sageVARx)
            sage: h(x) = heaviside(x)
            sage: h(pi).numerical_approx()
            1.00000000000000
        """

heaviside: FunctionHeaviside

class FunctionUnitStep(GinacFunction):
    """
    The unit step function, `\\mathrm{u}(x)` (``unit_step(x)``).

    INPUT:

    - ``x`` -- a real number or a symbolic expression

    DEFINITION:

    The unit step function, `\\mathrm{u}(x)` is defined in Sage as:

        `\\mathrm{u}(x) = 0` for `x < 0` and `\\mathrm{u}(x) = 1` for `x \\geq 0`

    .. SEEALSO:: :func:`heaviside()<sage.functions.generalized.FunctionHeaviside>`

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: unit_step(-1)
        0
        sage: unit_step(1)
        1
        sage: unit_step(0)
        1
        sage: unit_step(x)
        unit_step(x)
        sage: unit_step(-exp(-10000000000000000000))
        0

    TESTS::

        sage: # needs sage.symbolic
        sage: unit_step(x).subs(x=1)
        1
        sage: unit_step(x).subs(x=0)
        1
        sage: h(x) = unit_step(x)
        sage: h(pi).numerical_approx()
        1.00000000000000
    """
    def __init__(self) -> None:
        """
        The unit step function, ``unit_step(x)``.

        INPUT:

        - ``x`` -- a real number or a symbolic expression

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: unit_step(-1)
            0
            sage: unit_step(1)
            1
            sage: unit_step(0)
            1
            sage: unit_step(x)
            unit_step(x)
            sage: latex(unit_step(x))
            \\mathrm{u}\\left(x\\right)

        TESTS::

            sage: t = loads(dumps(unit_step(x) + 1)); t                                 # needs sage.symbolic
            unit_step(x) + 1
            sage: t.subs(x=0)                                                           # needs sage.symbolic
            2
        """

unit_step: FunctionUnitStep

class FunctionSignum(BuiltinFunction):
    """
    The signum or sgn function `\\mathrm{sgn}(x)` (``sgn(x)``).

    INPUT:

    - ``x`` -- a real number or a symbolic expression

    DEFINITION:

    The sgn function, `\\mathrm{sgn}(x)` is defined as:

        `\\mathrm{sgn}(x) =  1` for `x > 0`,
        `\\mathrm{sgn}(x) =  0` for `x = 0` and
        `\\mathrm{sgn}(x) = -1` for `x < 0`

    EXAMPLES::

        sage: sgn(-1)
        -1
        sage: sgn(1)
        1
        sage: sgn(0)
        0
        sage: sgn(x)                                                                    # needs sage.symbolic
        sgn(x)

    We can also use ``sign``::

        sage: sign(1)
        1
        sage: sign(0)
        0
        sage: a = AA(-5).nth_root(7)                                                    # needs sage.rings.number_field
        sage: sign(a)                                                                   # needs sage.rings.number_field
        -1

    TESTS:

    Check if conversions to sympy and others work (:issue:`11921`)::

        sage: sgn(x)._sympy_()                                                          # needs sympy sage.symbolic
        sign(x)
        sage: sgn(x)._fricas_init_()                                                    # needs sage.symbolic
        '(x+->abs(x)/x)(x)'
        sage: sgn(x)._giac_()                                                           # needs giac sage.symbolic
        sign(sageVARx)

    Test for :issue:`31085`::

        sage: fricas(sign(x)).eval(x=-3)        # optional - fricas                     # needs sage.symbolic
        - 1

    REFERENCES:

    - :wikipedia:`Sign_function`
    """
    def __init__(self) -> None:
        """
        The sgn function, ``sgn(x)``.

        EXAMPLES::

            sage: sgn(-1)
            -1
            sage: sgn(1)
            1
            sage: sgn(0)
            0
            sage: sgn(x)                                                                # needs sage.symbolic
            sgn(x)
            sage: sgn(x)._sympy_()                                                      # needs sympy sage.symbolic
            sign(x)
        """

sgn: FunctionSignum
sign = sgn

class FunctionKroneckerDelta(BuiltinFunction):
    """
    The Kronecker delta function `\\delta_{m,n}` (``kronecker_delta(m, n)``).

    INPUT:

    - ``m`` -- a number or a symbolic expression
    - ``n`` -- a number or a symbolic expression

    DEFINITION:

    Kronecker delta function `\\delta_{m,n}` is defined as:

        `\\delta_{m,n} = 0` for `m \\ne n` and
        `\\delta_{m,n} = 1` for `m = n`

    EXAMPLES::

        sage: kronecker_delta(1, 2)                                                     # needs sage.rings.complex_interval_field
        0
        sage: kronecker_delta(1, 1)                                                     # needs sage.rings.complex_interval_field
        1
        sage: m, n = var('m,n')                                                         # needs sage.symbolic
        sage: kronecker_delta(m, n)                                                     # needs sage.symbolic
        kronecker_delta(m, n)

    REFERENCES:

    - :wikipedia:`Kronecker_delta`
    """
    def __init__(self) -> None:
        """
        The Kronecker delta function.

        EXAMPLES::

            sage: kronecker_delta(1, 2)                                                 # needs sage.rings.complex_interval_field
            0
            sage: kronecker_delta(1, 1)                                                 # needs sage.rings.complex_interval_field
            1
            sage: y = var('y')                                                          # needs sage.symbolic
            sage: kronecker_delta(x, y)._sympy_()                                       # needs sympy sage.symbolic
            KroneckerDelta(x, y)
        """

kronecker_delta: FunctionKroneckerDelta
