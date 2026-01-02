r"""
Error functions

This module provides symbolic error functions. These functions use the
`mpmath library` for numerical evaluation and Maxima, Pynac for
symbolics.

The main objects which are exported from this module are:

 * :meth:`erf <Function_erf>` -- the error function
 * :meth:`erfc <Function_erfc>` -- the complementary error function
 * :meth:`erfi <Function_erfi>` -- the imaginary error function
 * :meth:`erfinv <Function_erfinv>` -- the inverse error function
 * :meth:`fresnel_sin <Function_Fresnel_sin>` -- the Fresnel integral `S(x)`
 * :meth:`fresnel_cos <Function_Fresnel_cos>` -- the Fresnel integral `C(x)`

AUTHORS:

 * Original authors ``erf``/``error_fcn`` (c) 2006-2014:
   Karl-Dieter Crisman, Benjamin Jones, Mike Hansen, William Stein,
   Burcin Erocal, Jeroen Demeyer, W. D. Joyner, R. Andrew Ohana
 * Reorganisation in new file, addition of ``erfi``/``erfinv``/``erfc``
   (c) 2016: Ralf Stephan
 * Fresnel integrals (c) 2017 Marcelo Forets

REFERENCES:

- [DLMF-Error]_

- [WP-Error]_
"""

from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import unsigned_infinity as unsigned_infinity
from sage.rings.rational import Rational as Rational
from sage.structure.element import Expression as Expression
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

class Function_erf(BuiltinFunction):
    '''
    The error function.

    The error function is defined for real values as

    .. MATH::

        \\operatorname{erf}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_0^x e^{-t^2} dt.

    This function is also defined for complex values, via analytic
    continuation.

    EXAMPLES:

    We can evaluate numerically::

        sage: erf(2)                                                                    # needs sage.symbolic
        erf(2)
        sage: erf(2).n()                                                                # needs sage.symbolic
        0.995322265018953
        sage: erf(2).n(100)                                                             # needs sage.symbolic
        0.99532226501895273416206925637
        sage: erf(ComplexField(100)(2+3j))                                              # needs sage.rings.real_mpfr
        -20.829461427614568389103088452 + 8.6873182714701631444280787545*I

    Basic symbolic properties are handled by Sage and Maxima::

        sage: x = var("x")                                                              # needs sage.symbolic
        sage: diff(erf(x),x)                                                            # needs sage.symbolic
        2*e^(-x^2)/sqrt(pi)
        sage: integrate(erf(x),x)                                                       # needs sage.symbolic
        x*erf(x) + e^(-x^2)/sqrt(pi)

    ALGORITHM:

    Sage implements numerical evaluation of the error function via the
    ``erf()`` function from mpmath. Symbolics are handled by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Error_function`
    - http://mpmath.googlecode.com/svn/trunk/doc/build/functions/expintegrals.html#error-functions

    TESTS:

    Check limits::

        sage: limit(erf(x), x=0)                                                        # needs sage.symbolic
        0
        sage: limit(erf(x), x=infinity)                                                 # needs sage.symbolic
        1

     Check that it\'s odd::

         sage: erf(1.0)                                                                 # needs mpmath
         0.842700792949715
         sage: erf(-1.0)                                                                # needs mpmath
         -0.842700792949715

    Check against other implementations and against the definition::

        sage: erf(3).n()                                                                # needs sage.symbolic
        0.999977909503001
        sage: maxima.erf(3).n()                                                         # needs sage.symbolic
        0.999977909503001
        sage: 1 - pari(3).erfc()                                                        # needs sage.libs.pari
        0.999977909503001
        sage: RR(3).erf()                                                               # needs sage.rings.real_mpfr
        0.999977909503001
        sage: (integrate(exp(-x**2), (x,0,3))*2/sqrt(pi)).n()                           # needs sage.symbolic
        0.999977909503001

    :issue:`9044`::

        sage: N(erf(sqrt(2)),200)                                                       # needs sage.symbolic
        0.95449973610364158559943472566693312505644755259664313203267

    :issue:`11626`::

        sage: n(erf(2),100)                                                             # needs sage.symbolic
        0.99532226501895273416206925637
        sage: erf(2).n(100)                                                             # needs sage.symbolic
        0.99532226501895273416206925637

    Test (indirectly) :issue:`11885`::

        sage: erf(float(0.5))
        0.5204998778130465
        sage: erf(complex(0.5))                                                         # needs sage.rings.complex_double
        (0.5204998778130465+0j)

    Ensure conversion from maxima elements works::

        sage: merf = maxima(erf(x)).sage().operator()                                   # needs sage.symbolic
        sage: merf.parent() == erf.parent()                                             # needs sage.symbolic
        True

    Make sure we can dump and load it::

        sage: loads(dumps(erf(2)))                                                      # needs sage.symbolic
        erf(2)

    Special-case 0 for immediate evaluation::

        sage: erf(0)                                                                    # needs mpmath
        0
        sage: solve(erf(x)==0, x)                                                       # needs sage.symbolic
        [x == 0]

    Make sure that we can hold::

        sage: erf(0, hold=True)                                                         # needs sage.symbolic
        erf(0)
        sage: simplify(erf(0, hold=True))                                               # needs sage.symbolic
        0

    Check that high-precision ComplexField inputs work::

        sage: CC(erf(ComplexField(1000)(2+3j)))                                         # needs sage.rings.real_mpfr
        -20.8294614276146 + 8.68731827147016*I
    '''
    def __init__(self) -> None:
        """
        See docstring for :meth:`Function_erf`.

        EXAMPLES::

            sage: maxima(erf(2))                                                        # needs sage.symbolic
            erf(2)
            sage: erf(2)._sympy_()                                                      # needs sympy sage.symbolic
            erf(2)
        """

erf: Function_erf

class Function_erfi(BuiltinFunction):
    """
    The imaginary error function.

    The imaginary error function is defined by

    .. MATH::

        \\operatorname{erfi}(x) = -i \\operatorname{erf}(ix).
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: maxima(erfi(2))                                                       # needs sage.symbolic
            erfi(2)
            sage: erfi(2)._sympy_()                                                     # needs sympy sage.symbolic
            erfi(2)
        """

erfi: Function_erfi

class Function_erfc(BuiltinFunction):
    """
    The complementary error function.

    The complementary error function is defined by

    .. MATH::

        \\frac{2}{\\sqrt{\\pi}} \\int_t^\\infty e^{-x^2} dx.

    EXAMPLES::

        sage: erfc(6)                                                                   # needs sage.symbolic
        erfc(6)
        sage: erfc(6).n()                                                               # needs sage.symbolic
        2.15197367124989e-17
        sage: erfc(RealField(100)(1/2))                                                 # needs sage.rings.real_mpfr
        0.47950012218695346231725334611

        sage: 1 - erfc(0.5)                                                             # needs mpmath
        0.520499877813047
        sage: erf(0.5)                                                                  # needs mpmath
        0.520499877813047

    TESTS:

    Check that :issue:`25991` is fixed::

            sage: erfc(x)._fricas_()                                            # optional - fricas, needs sage.symbolic
            - erf(x) + 1
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: maxima(erfc(2))                                                       # needs sage.symbolic
            erfc(2)
            sage: erfc(2)._sympy_()                                                     # needs sympy sage.symbolic
            erfc(2)
        """

erfc: Function_erfc

class Function_erfinv(BuiltinFunction):
    """
    The inverse error function.

    The inverse error function is defined by:

    .. MATH::

        \\operatorname{erfinv}(x) = \\operatorname{erf}^{-1}(x).
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: erfinv(2)._sympy_()                                                   # needs sympy sage.symbolic
            erfinv(2)
            sage: maxima(erfinv(2))                                                     # needs sage.symbolic
            inverse_erf(2)

        TESTS:

        Check that :issue:`11349` is fixed::

            sage: # needs sage.symbolic
            sage: _ = var('z,t')
            sage: PDF = exp(-x^2 /2)/sqrt(2*pi)
            sage: integralExpr = integrate(PDF,x,z,oo).subs(z==log(t))
            sage: y = solve(integralExpr==z,t)[0].rhs().subs(z==1/4)
            sage: y
            e^(sqrt(2)*erfinv(1/2))
            sage: y.n()
            1.96303108415826
        """

erfinv: Function_erfinv

class Function_Fresnel_sin(BuiltinFunction):
    def __init__(self) -> None:
        """
        The sine Fresnel integral.

        It is defined by the integral

        .. MATH ::

            \\operatorname{S}(x) = \\int_0^x \\sin\\left(\\frac{\\pi t^2}{2}\\right)\\, dt

        for real `x`. Using power series expansions, it can be extended to the
        domain of complex numbers. See the :wikipedia:`Fresnel_integral`.

        INPUT:

        - ``x`` -- the argument of the function

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: fresnel_sin(0)
            0
            sage: fresnel_sin(x).subs(x==0)
            0
            sage: x = var('x')
            sage: fresnel_sin(1).n(100)
            0.43825914739035476607675669662
            sage: fresnel_sin(x)._sympy_()                                              # needs sympy
            fresnels(x)
        """

fresnel_sin: Function_Fresnel_sin

class Function_Fresnel_cos(BuiltinFunction):
    def __init__(self) -> None:
        """
        The cosine Fresnel integral.

        It is defined by the integral

        .. MATH ::

            \\operatorname{C}(x) = \\int_0^x \\cos\\left(\\frac{\\pi t^2}{2}\\right)\\, dt

        for real `x`. Using power series expansions, it can be extended to the
        domain of complex numbers. See the :wikipedia:`Fresnel_integral`.

        INPUT:

        - ``x`` -- the argument of the function

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: fresnel_cos(0)
            0
            sage: fresnel_cos(x).subs(x==0)
            0
            sage: x = var('x')
            sage: fresnel_cos(1).n(100)
            0.77989340037682282947420641365
            sage: fresnel_cos(x)._sympy_()                                              # needs sympy
            fresnelc(x)
        """

fresnel_cos: Function_Fresnel_cos
