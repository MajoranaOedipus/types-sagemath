import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.abc
import sage.structure.element
from sage.categories.category import RDF as RDF, ZZ as ZZ
from sage.libs.pari.convert_sage_complex_double import pari_to_cdf as pari_to_cdf
from sage.misc.parser import Parser as Parser
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

ComplexDoubleField: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
complex_double_element_agm: None
complex_double_element_dilog: None
complex_double_element_eta: None
complex_double_element_gamma: None
complex_double_element_gamma_inc: None
complex_double_element_zeta: None
is_ComplexDoubleElement: _cython_3_2_1.cython_function_or_method
new_gen_from_complex_double_element: None

class ComplexDoubleElement(sage.structure.element.FieldElement):
    """ComplexDoubleElement(real, imag)

    File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 722)

    An approximation to a complex number using double precision
    floating point numbers. Answers derived from calculations with such
    approximations may differ from what they would be if those
    calculations were performed with true complex numbers. This is due
    to the rounding errors inherent to finite precision calculations."""
    __array_interface__: ClassVar[dict] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, real, imag) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 744)

                Construct an element of a complex double field with specified real
                and imaginary values.

                EXAMPLES::

                    sage: ComplexDoubleElement(1,-2)
                    1.0 - 2.0*I
        """
    @overload
    def abs(self) -> Any:
        """ComplexDoubleElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1318)

        This function returns the magnitude `|z|` of the complex number `z`.

        .. SEEALSO::

            - :meth:`norm`

        EXAMPLES::

            sage: CDF(2,3).abs()
            3.605551275463989"""
    @overload
    def abs(self) -> Any:
        """ComplexDoubleElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1318)

        This function returns the magnitude `|z|` of the complex number `z`.

        .. SEEALSO::

            - :meth:`norm`

        EXAMPLES::

            sage: CDF(2,3).abs()
            3.605551275463989"""
    @overload
    def abs2(self) -> Any:
        """ComplexDoubleElement.abs2(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1351)

        This function returns the squared magnitude `|z|^2` of the complex
        number `z`, otherwise known as the complex norm.

        .. SEEALSO::

            - :meth:`norm`

        EXAMPLES::

            sage: CDF(2,3).abs2()
            13.0"""
    @overload
    def abs2(self) -> Any:
        """ComplexDoubleElement.abs2(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1351)

        This function returns the squared magnitude `|z|^2` of the complex
        number `z`, otherwise known as the complex norm.

        .. SEEALSO::

            - :meth:`norm`

        EXAMPLES::

            sage: CDF(2,3).abs2()
            13.0"""
    def agm(self, right, algorithm=...) -> Any:
        """ComplexDoubleElement.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2248)

        Return the Arithmetic-Geometric Mean (AGM) of ``self`` and ``right``.

        INPUT:

        - ``right`` -- complex; another complex number

        - ``algorithm`` -- string (default: ``'optimal'``); the algorithm to
          use (see below)

        OUTPUT:

        (complex) A value of the AGM of ``self`` and ``right``.  Note that
        this is a multi-valued function, and the algorithm used
        affects the value returned, as follows:

        - ``'pari'``: Call the :pari:`agm` function from the pari library.

        - ``'optimal'``: Use the AGM sequence such that at each stage
          `(a,b)` is replaced by `(a_1,b_1)=((a+b)/2,\\pm\\sqrt{ab})`
          where the sign is chosen so that `|a_1-b_1| \\leq |a_1+b_1|`, or
          equivalently `\\Re(b_1/a_1) \\geq 0`.  The resulting limit is
          maximal among all possible values.

        - ``'principal'``: Use the AGM sequence such that at each stage
          `(a,b)` is replaced by `(a_1,b_1)=((a+b)/2,\\pm\\sqrt{ab})`
          where the sign is chosen so that `\\Re(b_1/a_1) \\geq 0` (the
          so-called principal branch of the square root).

        See :wikipedia:`Arithmetic-geometric mean`

        EXAMPLES::

            sage: i = CDF(I)                                                            # needs sage.symbolic
            sage: (1+i).agm(2-i)  # rel tol 1e-15                                       # needs sage.symbolic
            1.6278054848727064 + 0.1368275483973686*I

        An example to show that the returned value depends on the algorithm
        parameter::

            sage: a = CDF(-0.95,-0.65)
            sage: b = CDF(0.683,0.747)
            sage: a.agm(b, algorithm='optimal')  # rel tol 1e-15
            -0.3715916523517613 + 0.31989466020683005*I
            sage: a.agm(b, algorithm='principal')  # rel tol 2e-15
            0.33817546298618006 - 0.013532696956540483*I
            sage: a.agm(b, algorithm='pari')
            -0.37159165235176134 + 0.31989466020683005*I

        Some degenerate cases::

            sage: CDF(0).agm(a)
            0.0
            sage: a.agm(0)
            0.0
            sage: a.agm(-a)
            0.0"""
    def algdep(self, *args, **kwargs):
        """ComplexDoubleElement.algebraic_dependency(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2443)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        Note that the returned polynomial need not be irreducible, and
        indeed usually will not be if `z` is a good approximation to an
        algebraic number of degree less than `n`.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: z = (1/2)*(1 + RDF(sqrt(3)) * CDF.0); z   # abs tol 1e-16             # needs sage.symbolic
            0.5 + 0.8660254037844387*I
            sage: p = z.algebraic_dependency(5); p                                      # needs sage.libs.pari sage.symbolic
            x^2 - x + 1
            sage: abs(z^2 - z + 1) < 1e-14                                              # needs sage.symbolic
            True

        ::

            sage: CDF(0,2).algebraic_dependency(10)                                     # needs sage.libs.pari
            x^2 + 4
            sage: CDF(1,5).algebraic_dependency(2)                                      # needs sage.libs.pari
            x^2 - 2*x + 26"""
    def algebraic_dependency(self, longn) -> Any:
        """ComplexDoubleElement.algebraic_dependency(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2443)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        Note that the returned polynomial need not be irreducible, and
        indeed usually will not be if `z` is a good approximation to an
        algebraic number of degree less than `n`.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: z = (1/2)*(1 + RDF(sqrt(3)) * CDF.0); z   # abs tol 1e-16             # needs sage.symbolic
            0.5 + 0.8660254037844387*I
            sage: p = z.algebraic_dependency(5); p                                      # needs sage.libs.pari sage.symbolic
            x^2 - x + 1
            sage: abs(z^2 - z + 1) < 1e-14                                              # needs sage.symbolic
            True

        ::

            sage: CDF(0,2).algebraic_dependency(10)                                     # needs sage.libs.pari
            x^2 + 4
            sage: CDF(1,5).algebraic_dependency(2)                                      # needs sage.libs.pari
            x^2 - 2*x + 26"""
    def arccos(self) -> Any:
        """ComplexDoubleElement.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1911)

        This function returns the complex arccosine of the complex number
        `z`, `{\\rm arccos}(z)`. The branch cuts are on the
        real axis, less than -1 and greater than 1.

        EXAMPLES::

            sage: CDF(1,1).arccos()
            0.9045568943023814 - 1.0612750619050357*I"""
    def arccosh(self) -> Any:
        """ComplexDoubleElement.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2089)

        This function returns the complex hyperbolic arccosine of the
        complex number `z`, `{\\rm arccosh}(z)`. The branch
        cut is on the real axis, less than 1.

        EXAMPLES::

            sage: CDF(1,1).arccosh()
            1.0612750619050357 + 0.9045568943023814*I"""
    def arccot(self) -> Any:
        """ComplexDoubleElement.arccot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1949)

        This function returns the complex arccotangent of the complex
        number `z`, `{\\rm arccot}(z) = {\\rm arctan}(1/z).`

        EXAMPLES::

            sage: CDF(1,1).arccot()  # rel tol 1e-15
            0.5535743588970452 - 0.4023594781085251*I"""
    def arccoth(self) -> Any:
        """ComplexDoubleElement.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2139)

        This function returns the complex hyperbolic arccotangent of the
        complex number `z`, `{\\rm arccoth}(z) = {\\rm arctanh(1/z)}`.

        EXAMPLES::

            sage: CDF(1,1).arccoth()  # rel tol 1e-15
            0.4023594781085251 - 0.5535743588970452*I"""
    def arccsc(self) -> Any:
        """ComplexDoubleElement.arccsc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1937)

        This function returns the complex arccosecant of the complex number
        `z`, `{\\rm arccsc}(z) = {\\rm arcsin}(1/z)`.

        EXAMPLES::

            sage: CDF(1,1).arccsc()  # rel tol 1e-15
            0.45227844715119064 - 0.5306375309525178*I"""
    def arccsch(self) -> Any:
        """ComplexDoubleElement.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2127)

        This function returns the complex hyperbolic arccosecant of the
        complex number `z`, `{\\rm arccsch}(z) = {\\rm arcsin}(1/z)`.

        EXAMPLES::

            sage: CDF(1,1).arccsch()  # rel tol 1e-15
            0.5306375309525178 - 0.45227844715119064*I"""
    def arcsec(self) -> Any:
        """ComplexDoubleElement.arcsec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1961)

        This function returns the complex arcsecant of the complex number
        `z`, `{\\rm arcsec}(z) = {\\rm arccos}(1/z)`.

        EXAMPLES::

            sage: CDF(1,1).arcsec()  # rel tol 1e-15
            1.118517879643706 + 0.5306375309525178*I"""
    def arcsech(self) -> Any:
        """ComplexDoubleElement.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2115)

        This function returns the complex hyperbolic arcsecant of the
        complex number `z`, `{\\rm arcsech}(z) = {\\rm arccosh}(1/z)`.

        EXAMPLES::

            sage: CDF(1,1).arcsech()  # rel tol 1e-15
            0.5306375309525176 - 1.118517879643706*I"""
    def arcsin(self) -> Any:
        """ComplexDoubleElement.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1898)

        This function returns the complex arcsine of the complex number
        `z`, `{\\rm arcsin}(z)`. The branch cuts are on the
        real axis, less than -1 and greater than 1.

        EXAMPLES::

            sage: CDF(1,1).arcsin()
            0.6662394324925152 + 1.0612750619050357*I"""
    def arcsinh(self) -> Any:
        """ComplexDoubleElement.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2076)

        This function returns the complex hyperbolic arcsine of the complex
        number `z`, `{\\rm arcsinh}(z)`. The branch cuts are
        on the imaginary axis, below `-i` and above `i`.

        EXAMPLES::

            sage: CDF(1,1).arcsinh()
            1.0612750619050357 + 0.6662394324925152*I"""
    def arctan(self) -> Any:
        """ComplexDoubleElement.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1924)

        This function returns the complex arctangent of the complex number
        `z`, `{\\rm arctan}(z)`. The branch cuts are on the
        imaginary axis, below `-i` and above `i`.

        EXAMPLES::

            sage: CDF(1,1).arctan()
            1.0172219678978514 + 0.4023594781085251*I"""
    def arctanh(self) -> Any:
        """ComplexDoubleElement.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2102)

        This function returns the complex hyperbolic arctangent of the
        complex number `z`, `{\\rm arctanh} (z)`. The branch
        cuts are on the real axis, less than -1 and greater than 1.

        EXAMPLES::

            sage: CDF(1,1).arctanh()
            0.4023594781085251 + 1.0172219678978514*I"""
    def arg(self) -> Any:
        """ComplexDoubleElement.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1285)

        This function returns the argument of ``self``, the complex number
        `z`, denoted by `\\arg(z)`, where `-\\pi < \\arg(z) <= \\pi`.

        EXAMPLES::

            sage: CDF(1,0).arg()
            0.0
            sage: CDF(0,1).arg()
            1.5707963267948966
            sage: CDF(0,-1).arg()
            -1.5707963267948966
            sage: CDF(-1,0).arg()
            3.141592653589793"""
    def argument(self) -> Any:
        """ComplexDoubleElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1333)

        This function returns the argument of the ``self``, the complex number
        `z`, in the interval `-\\pi < arg(z) \\leq \\pi`.

        EXAMPLES::

            sage: CDF(6).argument()
            0.0
            sage: CDF(i).argument()                                                     # needs sage.symbolic
            1.5707963267948966
            sage: CDF(-1).argument()
            3.141592653589793
            sage: CDF(-1 - 0.000001*i).argument()                                       # needs sage.symbolic
            -3.1415916535897934"""
    def conj(self) -> Any:
        """ComplexDoubleElement.conj(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1266)

        This function returns the complex conjugate of the complex number `z`:

        .. MATH::

            \\overline{z} = x - i y.

        EXAMPLES::

            sage: z = CDF(2,3); z.conj()
            2.0 - 3.0*I"""
    def conjugate(self) -> Any:
        """ComplexDoubleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1251)

        This function returns the complex conjugate of the complex number `z`:

        .. MATH::

            \\overline{z} = x - i y.

        EXAMPLES::

            sage: z = CDF(2,3); z.conjugate()
            2.0 - 3.0*I"""
    def cos(self) -> Any:
        """ComplexDoubleElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1820)

        This function returns the complex cosine of the complex number `z`:

        .. MATH::

            \\cos(z) = \\frac{e^{iz} + e^{-iz}}{2}

        EXAMPLES::

            sage: CDF(1,1).cos()   # abs tol 1e-16
            0.8337300251311491 - 0.9888977057628651*I"""
    def cosh(self) -> Any:
        """ComplexDoubleElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1993)

        This function returns the complex hyperbolic cosine of the complex
        number `z`:

        .. MATH::

            \\cosh(z) = \\frac{e^z + e^{-z}}{2}.

        EXAMPLES::

            sage: CDF(1,1).cosh()  # abs tol 1e-16
            0.8337300251311491 + 0.9888977057628651*I"""
    def cot(self) -> Any:
        """ComplexDoubleElement.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1880)

        This function returns the complex cotangent of the complex number `z`:

        .. MATH::

            \\cot(z) = \\frac{1}{\\tan(z)}.

        EXAMPLES::

            sage: CDF(1,1).cot()  # rel tol 1e-15
            0.21762156185440268 - 0.8680141428959249*I"""
    def coth(self) -> Any:
        """ComplexDoubleElement.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2057)

        This function returns the complex hyperbolic cotangent of the
        complex number `z`:

        .. MATH::

            \\coth(z) = \\frac{1}{\\tanh(z)}.

        EXAMPLES::

            sage: CDF(1,1).coth()  # rel tol 1e-15
            0.8680141428959249 - 0.21762156185440268*I"""
    def csc(self) -> Any:
        """ComplexDoubleElement.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1865)

        This function returns the complex cosecant of the complex number `z`:

        .. MATH::

            \\csc(z) = \\frac{1}{\\sin(z)}.

        EXAMPLES::

            sage: CDF(1,1).csc()  # rel tol 1e-15
            0.6215180171704284 - 0.30393100162842646*I"""
    def csch(self) -> Any:
        """ComplexDoubleElement.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2041)

        This function returns the complex hyperbolic cosecant of the
        complex number `z`:

        .. MATH::

            {\\rm csch}(z) = \\frac{1}{{\\rm sinh}(z)}.

        EXAMPLES::

            sage: CDF(1,1).csch()  # rel tol 1e-15
            0.30393100162842646 - 0.6215180171704284*I"""
    def dilog(self) -> Any:
        """ComplexDoubleElement.dilog(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2348)

        Return the principal branch of the dilogarithm of `x`, i.e., analytic
        continuation of the power series

        .. MATH::

            \\log_2(x) = \\sum_{n \\ge 1} x^n / n^2.

        EXAMPLES::

            sage: CDF(1,2).dilog()                                                      # needs sage.libs.pari
            -0.059474798673809476 + 2.0726479717747566*I
            sage: CDF(10000000,10000000).dilog()                                        # needs sage.libs.pari
            -134.411774490731 + 38.79396299904504*I"""
    def eta(self, intomit_frac=...) -> Any:
        """ComplexDoubleElement.eta(self, int omit_frac=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2154)

        Return the value of the Dedekind `\\eta` function on ``self``.

        INPUT:

        - ``self`` -- element of the upper half plane (if not,
          raises a ValueError)

        - ``omit_frac`` -- boolean (default: ``False``); if ``True``,
          omit the `e^{\\pi i z / 12}` factor

        OUTPUT: a complex double number

        ALGORITHM: Uses the PARI C library.

        The `\\eta` function is

        .. MATH::

            \\eta(z) = e^{\\pi i z / 12} \\prod_{n=1}^{\\infty} (1 - e^{2\\pi inz})

        EXAMPLES:

        We compute a few values of :meth:`eta()`::

            sage: CDF(0,1).eta()                                                        # needs sage.libs.pari
            0.7682254223260566
            sage: CDF(1,1).eta()                                                        # needs sage.libs.pari
            0.7420487758365647 + 0.1988313702299107*I
            sage: CDF(25,1).eta()                                                       # needs sage.libs.pari
            0.7420487758365647 + 0.1988313702299107*I

        :meth:`eta()` works even if the inputs are large::

            sage: CDF(0, 10^15).eta()
            0.0
            sage: CDF(10^15, 0.1).eta()  # abs tol 1e-10                                # needs sage.libs.pari
            -0.115342592727 - 0.19977923088*I

        We compute a few values of :meth:`eta()`, but with the fractional power
        of `e` omitted::

            sage: CDF(0,1).eta(True)                                                    # needs sage.libs.pari
            0.9981290699259585

        We compute :meth:`eta()` to low precision directly from the
        definition::

            sage: z = CDF(1,1); z.eta()                                                 # needs sage.libs.pari
            0.7420487758365647 + 0.1988313702299107*I
            sage: i = CDF(0,1); pi = CDF(pi)                                            # needs sage.symbolic
            sage: exp(pi * i * z / 12) * prod(1 - exp(2*pi*i*n*z)                       # needs sage.libs.pari sage.symbolic
            ....:                             for n in range(1, 10))
            0.7420487758365647 + 0.19883137022991068*I

        The optional argument allows us to omit the fractional part::

            sage: z.eta(omit_frac=True)                                                 # needs sage.libs.pari
            0.9981290699259585
            sage: pi = CDF(pi)                                                          # needs sage.symbolic
            sage: prod(1 - exp(2*pi*i*n*z) for n in range(1,10))  # abs tol 1e-12       # needs sage.libs.pari sage.symbolic
            0.998129069926 + 4.59084695545e-19*I

        We illustrate what happens when `z` is not in the upper half plane::

            sage: z = CDF(1)
            sage: z.eta()
            Traceback (most recent call last):
            ...
            ValueError: value must be in the upper half plane

        You can also use functional notation::

            sage: z = CDF(1,1)
            sage: eta(z)                                                                # needs sage.libs.pari
            0.7420487758365647 + 0.1988313702299107*I"""
    def exp(self) -> Any:
        """ComplexDoubleElement.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1714)

        This function returns the complex exponential of the complex number
        `z`, `\\exp(z)`.

        EXAMPLES::

            sage: CDF(1,1).exp()  # abs tol 4e-16
            1.4686939399158851 + 2.2873552871788423*I

        We numerically verify a famous identity to the precision of a double::

            sage: z = CDF(0, 2*pi); z                                                   # needs sage.symbolic
            6.283185307179586*I
            sage: exp(z)  # rel tol 1e-4                                                # needs sage.symbolic
            1.0 - 2.4492935982947064e-16*I"""
    def gamma(self) -> Any:
        """ComplexDoubleElement.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2369)

        Return the gamma function `\\Gamma(z)` evaluated at ``self``, the
        complex number `z`.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: CDF(5,0).gamma()
            24.0
            sage: CDF(1,1).gamma()
            0.49801566811835607 - 0.15494982830181067*I
            sage: CDF(0).gamma()
            Infinity
            sage: CDF(-1,0).gamma()
            Infinity"""
    def gamma_inc(self, t) -> Any:
        """ComplexDoubleElement.gamma_inc(self, t)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2402)

        Return the incomplete gamma function evaluated at this complex number.

        EXAMPLES::

            sage: CDF(1,1).gamma_inc(CDF(2,3))                                          # needs sage.libs.pari
            0.0020969148636468277 - 0.059981913655449706*I
            sage: CDF(1,1).gamma_inc(5)                                                 # needs sage.libs.pari
            -0.001378130936215849 + 0.006519820023119819*I
            sage: CDF(2,0).gamma_inc(CDF(1,1))                                          # needs sage.libs.pari
            0.7070920963459381 - 0.4203536409598115*I"""
    @overload
    def imag(self) -> Any:
        """ComplexDoubleElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1446)

        Return the imaginary part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.imag()
            -2.0
            sage: a.imag_part()
            -2.0"""
    @overload
    def imag(self) -> Any:
        """ComplexDoubleElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1446)

        Return the imaginary part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.imag()
            -2.0
            sage: a.imag_part()
            -2.0"""
    def imag_part(self) -> Any:
        """ComplexDoubleElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1446)

        Return the imaginary part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.imag()
            -2.0
            sage: a.imag_part()
            -2.0"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1607)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CDF(1, 2).is_NaN()
            False
            sage: CDF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1/CDF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1607)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CDF(1, 2).is_NaN()
            False
            sage: CDF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1/CDF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1607)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CDF(1, 2).is_NaN()
            False
            sage: CDF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1/CDF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1607)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CDF(1, 2).is_NaN()
            False
            sage: CDF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1/CDF(0, 0)).is_NaN()
            True"""
    def is_infinity(self) -> Any:
        """ComplexDoubleElement.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1594)

        Check if ``self`` is `\\infty`.

        EXAMPLES::

            sage: CDF(1, 2).is_infinity()
            False
            sage: CDF(0, oo).is_infinity()
            True"""
    @overload
    def is_integer(self) -> Any:
        """ComplexDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1549)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: CDF(0.5).is_integer()
            False
            sage: CDF(I).is_integer()                                                   # needs sage.symbolic
            False
            sage: CDF(2).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """ComplexDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1549)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: CDF(0.5).is_integer()
            False
            sage: CDF(I).is_integer()                                                   # needs sage.symbolic
            False
            sage: CDF(2).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """ComplexDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1549)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: CDF(0.5).is_integer()
            False
            sage: CDF(I).is_integer()                                                   # needs sage.symbolic
            False
            sage: CDF(2).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """ComplexDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1549)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: CDF(0.5).is_integer()
            False
            sage: CDF(I).is_integer()                                                   # needs sage.symbolic
            False
            sage: CDF(2).is_integer()
            True"""
    def is_negative_infinity(self) -> Any:
        """ComplexDoubleElement.is_negative_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1579)

        Check if ``self`` is `-\\infty`.

        EXAMPLES::

            sage: CDF(1, 2).is_negative_infinity()
            False
            sage: CDF(-oo, 0).is_negative_infinity()
            True
            sage: CDF(0, -oo).is_negative_infinity()
            False"""
    def is_positive_infinity(self) -> Any:
        """ComplexDoubleElement.is_positive_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1564)

        Check if ``self`` is `+\\infty`.

        EXAMPLES::

            sage: CDF(1, 2).is_positive_infinity()
            False
            sage: CDF(oo, 0).is_positive_infinity()
            True
            sage: CDF(0, oo).is_positive_infinity()
            False"""
    def is_square(self) -> Any:
        """ComplexDoubleElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1538)

        This function always returns ``True`` as `\\CC` is algebraically closed.

        EXAMPLES::

            sage: CDF(-1).is_square()
            True"""
    def log(self, base=...) -> Any:
        """ComplexDoubleElement.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1733)

        This function returns the complex natural logarithm to the given
        base of the complex number `z`, `\\log(z)`. The
        branch cut is the negative real axis.

        INPUT:

        - ``base`` -- (default: `e`) the base of the natural logarithm

        EXAMPLES::

            sage: CDF(1,1).log()
            0.34657359027997264 + 0.7853981633974483*I

        This is the only example different from the GSL::

            sage: CDF(0,0).log()
            -infinity"""
    def log10(self) -> Any:
        """ComplexDoubleElement.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1764)

        This function returns the complex base-10 logarithm of the complex
        number `z`, `\\log_{10}(z)`.

        The branch cut is the negative real axis.

        EXAMPLES::

            sage: CDF(1,1).log10()
            0.15051499783199057 + 0.3410940884604603*I"""
    def log_b(self, b) -> Any:
        """ComplexDoubleElement.log_b(self, b)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1780)

        This function returns the complex base-`b` logarithm of the
        complex number `z`, `\\log_b(z)`. This quantity is
        computed as the ratio `\\log(z)/\\log(b)`.

        The branch cut is the negative real axis.

        EXAMPLES::

            sage: CDF(1,1).log_b(10)  # rel tol 1e-15
            0.15051499783199057 + 0.3410940884604603*I"""
    def logabs(self) -> Any:
        """ComplexDoubleElement.logabs(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1407)

        This function returns the natural logarithm of the magnitude of the
        complex number `z`, `\\log|z|`.

        This allows for an accurate evaluation of `\\log|z|` when `|z|` is
        close to `1`. The direct evaluation of ``log(abs(z))`` would lead
        to a loss of precision in this case.

        EXAMPLES::

            sage: CDF(1.1,0.1).logabs()
            0.09942542937258267
            sage: log(abs(CDF(1.1,0.1)))
            0.09942542937258259

        ::

            sage: log(abs(ComplexField(200)(1.1,0.1)))
            0.099425429372582595066319157757531449594489450091985182495705"""
    def norm(self) -> Any:
        """ComplexDoubleElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1367)

        This function returns the squared magnitude `|z|^2` of the complex
        number `z`, otherwise known as the complex norm. If `c = a + bi`
        is a complex number, then the norm of `c` is defined as the product of
        `c` and its complex conjugate:

        .. MATH::

            \\text{norm}(c)
            =
            \\text{norm}(a + bi)
            =
            c \\cdot \\overline{c}
            =
            a^2 + b^2.

        The norm of a complex number is different from its absolute value.
        The absolute value of a complex number is defined to be the square
        root of its norm. A typical use of the complex norm is in the
        integral domain `\\ZZ[i]` of Gaussian integers, where the norm of
        each Gaussian integer `c = a + bi` is defined as its complex norm.

        .. SEEALSO::

            - :meth:`abs`

            - :meth:`abs2`

            - :func:`sage.misc.functional.norm`

            - :meth:`sage.rings.complex_mpfr.ComplexNumber.norm`

        EXAMPLES::

            sage: CDF(2,3).norm()
            13.0"""
    def nth_root(self, n, all=...) -> Any:
        """ComplexDoubleElement.nth_root(self, n, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1507)

        The ``n``-th root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all ``n``-th roots

        EXAMPLES::

            sage: a = CDF(125)
            sage: a.nth_root(3)
            5.000000000000001
            sage: a = CDF(10, 2)
            sage: [r^5 for r in a.nth_root(5, all=True)]  # rel tol 1e-14
            [9.999999999999998 + 2.0*I, 9.999999999999993 + 2.000000000000002*I, 9.999999999999996 + 1.9999999999999907*I, 9.999999999999993 + 2.0000000000000004*I, 9.999999999999998 + 1.9999999999999802*I]
            sage: abs(sum(a.nth_root(111, all=True)))  # rel tol 0.1
            1.1057313523818259e-13"""
    @overload
    def prec(self) -> Any:
        """ComplexDoubleElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 888)

        Return the precision of this number (to be more similar to
        :class:`ComplexNumber`). Always returns 53.

        EXAMPLES::

            sage: CDF(0).prec()
            53"""
    @overload
    def prec(self) -> Any:
        """ComplexDoubleElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 888)

        Return the precision of this number (to be more similar to
        :class:`ComplexNumber`). Always returns 53.

        EXAMPLES::

            sage: CDF(0).prec()
            53"""
    @overload
    def real(self) -> Any:
        """ComplexDoubleElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1430)

        Return the real part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.real()
            3.0
            sage: a.real_part()
            3.0"""
    @overload
    def real(self) -> Any:
        """ComplexDoubleElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1430)

        Return the real part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.real()
            3.0
            sage: a.real_part()
            3.0"""
    def real_part(self) -> Any:
        """ComplexDoubleElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1430)

        Return the real part of this complex double.

        EXAMPLES::

            sage: a = CDF(3,-2)
            sage: a.real()
            3.0
            sage: a.real_part()
            3.0"""
    def sec(self) -> Any:
        """ComplexDoubleElement.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1850)

        This function returns the complex secant of the complex number `z`:

        .. MATH::

            {\\rm sec}(z) = \\frac{1}{\\cos(z)}.

        EXAMPLES::

            sage: CDF(1,1).sec()  # rel tol 1e-15
            0.4983370305551868 + 0.591083841721045*I"""
    def sech(self) -> Any:
        """ComplexDoubleElement.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2025)

        This function returns the complex hyperbolic secant of the complex
        number `z`:

        .. MATH::

            {\\rm sech}(z) = \\frac{1}{{\\rm cosh}(z)}.

        EXAMPLES::

            sage: CDF(1,1).sech()  # rel tol 1e-15
            0.4983370305551868 - 0.591083841721045*I"""
    def sin(self) -> Any:
        """ComplexDoubleElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1805)

        This function returns the complex sine of the complex number `z`:

        .. MATH::

            \\sin(z) = \\frac{e^{iz} - e^{-iz}}{2i}.

        EXAMPLES::

            sage: CDF(1,1).sin()
            1.2984575814159773 + 0.6349639147847361*I"""
    def sinh(self) -> Any:
        """ComplexDoubleElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1977)

        This function returns the complex hyperbolic sine of the complex
        number `z`:

        .. MATH::

            \\sinh(z) = \\frac{e^z - e^{-z}}{2}.

        EXAMPLES::

            sage: CDF(1,1).sinh()
            0.6349639147847361 + 1.2984575814159773*I"""
    @overload
    def sqrt(self, all=..., **kwds) -> Any:
        """ComplexDoubleElement.sqrt(self, all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1465)

        The square root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        If all is ``False``, the branch cut is the negative real axis. The
        result always lies in the right half of the complex plane.

        EXAMPLES:

        We compute several square roots::

            sage: a = CDF(2,3)
            sage: b = a.sqrt(); b  # rel tol 1e-15
            1.6741492280355401 + 0.8959774761298381*I
            sage: b^2  # rel tol 1e-15
            2.0 + 3.0*I
            sage: a^(1/2)   # abs tol 1e-16
            1.6741492280355401 + 0.895977476129838*I

        We compute the square root of -1::

            sage: a = CDF(-1)
            sage: a.sqrt()
            1.0*I

        We compute all square roots::

            sage: CDF(-2).sqrt(all=True)
            [1.4142135623730951*I, -1.4142135623730951*I]
            sage: CDF(0).sqrt(all=True)
            [0.0]"""
    @overload
    def sqrt(self) -> Any:
        """ComplexDoubleElement.sqrt(self, all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1465)

        The square root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        If all is ``False``, the branch cut is the negative real axis. The
        result always lies in the right half of the complex plane.

        EXAMPLES:

        We compute several square roots::

            sage: a = CDF(2,3)
            sage: b = a.sqrt(); b  # rel tol 1e-15
            1.6741492280355401 + 0.8959774761298381*I
            sage: b^2  # rel tol 1e-15
            2.0 + 3.0*I
            sage: a^(1/2)   # abs tol 1e-16
            1.6741492280355401 + 0.895977476129838*I

        We compute the square root of -1::

            sage: a = CDF(-1)
            sage: a.sqrt()
            1.0*I

        We compute all square roots::

            sage: CDF(-2).sqrt(all=True)
            [1.4142135623730951*I, -1.4142135623730951*I]
            sage: CDF(0).sqrt(all=True)
            [0.0]"""
    @overload
    def sqrt(self) -> Any:
        """ComplexDoubleElement.sqrt(self, all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1465)

        The square root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        If all is ``False``, the branch cut is the negative real axis. The
        result always lies in the right half of the complex plane.

        EXAMPLES:

        We compute several square roots::

            sage: a = CDF(2,3)
            sage: b = a.sqrt(); b  # rel tol 1e-15
            1.6741492280355401 + 0.8959774761298381*I
            sage: b^2  # rel tol 1e-15
            2.0 + 3.0*I
            sage: a^(1/2)   # abs tol 1e-16
            1.6741492280355401 + 0.895977476129838*I

        We compute the square root of -1::

            sage: a = CDF(-1)
            sage: a.sqrt()
            1.0*I

        We compute all square roots::

            sage: CDF(-2).sqrt(all=True)
            [1.4142135623730951*I, -1.4142135623730951*I]
            sage: CDF(0).sqrt(all=True)
            [0.0]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """ComplexDoubleElement.sqrt(self, all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1465)

        The square root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        If all is ``False``, the branch cut is the negative real axis. The
        result always lies in the right half of the complex plane.

        EXAMPLES:

        We compute several square roots::

            sage: a = CDF(2,3)
            sage: b = a.sqrt(); b  # rel tol 1e-15
            1.6741492280355401 + 0.8959774761298381*I
            sage: b^2  # rel tol 1e-15
            2.0 + 3.0*I
            sage: a^(1/2)   # abs tol 1e-16
            1.6741492280355401 + 0.895977476129838*I

        We compute the square root of -1::

            sage: a = CDF(-1)
            sage: a.sqrt()
            1.0*I

        We compute all square roots::

            sage: CDF(-2).sqrt(all=True)
            [1.4142135623730951*I, -1.4142135623730951*I]
            sage: CDF(0).sqrt(all=True)
            [0.0]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """ComplexDoubleElement.sqrt(self, all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1465)

        The square root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        If all is ``False``, the branch cut is the negative real axis. The
        result always lies in the right half of the complex plane.

        EXAMPLES:

        We compute several square roots::

            sage: a = CDF(2,3)
            sage: b = a.sqrt(); b  # rel tol 1e-15
            1.6741492280355401 + 0.8959774761298381*I
            sage: b^2  # rel tol 1e-15
            2.0 + 3.0*I
            sage: a^(1/2)   # abs tol 1e-16
            1.6741492280355401 + 0.895977476129838*I

        We compute the square root of -1::

            sage: a = CDF(-1)
            sage: a.sqrt()
            1.0*I

        We compute all square roots::

            sage: CDF(-2).sqrt(all=True)
            [1.4142135623730951*I, -1.4142135623730951*I]
            sage: CDF(0).sqrt(all=True)
            [0.0]"""
    def tan(self) -> Any:
        """ComplexDoubleElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1835)

        This function returns the complex tangent of the complex number `z`:

        .. MATH::

            \\tan(z) = \\frac{\\sin(z)}{\\cos(z)}.

        EXAMPLES::

            sage: CDF(1,1).tan()
            0.27175258531951174 + 1.0839233273386946*I"""
    def tanh(self) -> Any:
        """ComplexDoubleElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2009)

        This function returns the complex hyperbolic tangent of the complex
        number `z`:

        .. MATH::

            \\tanh(z) = \\frac{\\sinh(z)}{\\cosh(z)}.

        EXAMPLES::

            sage: CDF(1,1).tanh()
            1.0839233273386946 + 0.27175258531951174*I"""
    @overload
    def zeta(self) -> Any:
        """ComplexDoubleElement.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2420)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: z = CDF(1, 1)
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(CDF(1))                                                          # needs sage.libs.pari
            Infinity"""
    @overload
    def zeta(self) -> Any:
        """ComplexDoubleElement.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2420)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: z = CDF(1, 1)
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(CDF(1))                                                          # needs sage.libs.pari
            Infinity"""
    @overload
    def zeta(self, z) -> Any:
        """ComplexDoubleElement.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2420)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: z = CDF(1, 1)
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.5821580597520036 - 0.9268485643308071*I
            sage: zeta(CDF(1))                                                          # needs sage.libs.pari
            Infinity"""
    def __abs__(self) -> Any:
        """ComplexDoubleElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1303)

        This function returns the magnitude of the complex number `z`, `|z|`.

        EXAMPLES::

            sage: abs(CDF(1,2)) # indirect doctest
            2.23606797749979
            sage: abs(CDF(1,0)) # indirect doctest
            1.0
            sage: abs(CDF(-2,3))
            3.605551275463989"""
    def __complex__(self) -> Any:
        """ComplexDoubleElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 946)

        Convert ``self`` to python's ``complex`` object.

        EXAMPLES::

            sage: a = complex(2303,-3939)
            sage: CDF(a)
            2303.0 - 3939.0*I
            sage: complex(CDF(a))
            (2303-3939j)"""
    @overload
    def __float__(self) -> Any:
        """ComplexDoubleElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 919)

        Method for converting ``self`` to type ``float``. Called by the
        ``float`` function.  This conversion will throw an error if
        the number has a nonzero imaginary part.

        EXAMPLES::

            sage: a = CDF(1, 0)
            sage: float(a)
            1.0
            sage: a = CDF(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.0 + 1.0*I to float; use abs() or real_part() as desired
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.0 + 1.0*I to float; use abs() or real_part() as desired
            sage: float(abs(CDF(1,1)))
            1.4142135623730951"""
    @overload
    def __float__(self) -> Any:
        """ComplexDoubleElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 919)

        Method for converting ``self`` to type ``float``. Called by the
        ``float`` function.  This conversion will throw an error if
        the number has a nonzero imaginary part.

        EXAMPLES::

            sage: a = CDF(1, 0)
            sage: float(a)
            1.0
            sage: a = CDF(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.0 + 1.0*I to float; use abs() or real_part() as desired
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.0 + 1.0*I to float; use abs() or real_part() as desired
            sage: float(abs(CDF(1,1)))
            1.4142135623730951"""
    def __format__(self, format_spec) -> Any:
        """ComplexDoubleElement.__format__(self, format_spec)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1073)

        Return a formatted string representation of this complex number.

        INPUT:

        - ``format_spec`` -- string; a floating point format specifier as
          defined by :python:`the format specification mini-language
          <library/string.html#formatspec>` in Python

        EXAMPLES::

            sage: format(CDF(32/3, 0), ' .4f')
            ' 10.6667 + 0.0000*I'
            sage: format(CDF(-2/3, -2/3), '.4e')
            '-6.6667e-01 - 6.6667e-01*I'
            sage: format(CDF(3, 0), '.4g')
            '3 + 0*I'
            sage: format(CDF(3, 0), '#.4g')
            '3.000 + 0.000*I'

        If the representation type character is absent, the output matches the
        string representation of the complex number. This has the effect that
        real and imaginary part are only shown if they are not zero::

            sage: format(CDF(0, 2/3), '.4')
            '0.6667*I'
            sage: format(CDF(2, 0), '.4')
            '2.0'
            sage: format(CDF(0, 0), '+#.4')
            '+0.000'"""
    def __getitem__(self, n) -> Any:
        """ComplexDoubleElement.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 842)

        Return the real or imaginary part of ``self``.

        INPUT:

        - ``n`` -- integer (either 0 or 1)

        Raises an :exc:`IndexError` if ``n`` is not 0 or 1.

        EXAMPLES::

            sage: P = CDF(2,3)
            sage: P[0]
            2.0
            sage: P[1]
            3.0
            sage: P[3]
            Traceback (most recent call last):
            ...
            IndexError: index n must be 0 or 1"""
    def __hash__(self) -> Any:
        """ComplexDoubleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 778)

        Return the hash of ``self``, which coincides with the python ``float``
        and ``complex`` (and often ``int``) types for ``self``.

        EXAMPLES::

            sage: hash(CDF(1.2)) == hash(1.2r)
            True
            sage: hash(CDF(-1))
            -2
            sage: hash(CDF(1.2, 1.3)) == hash(complex(1.2r, 1.3r))
            True"""
    def __int__(self) -> Any:
        """ComplexDoubleElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 904)

        Convert ``self`` to an ``int``.

        EXAMPLES::

            sage: int(CDF(1,1))
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))
            sage: int(abs(CDF(1,1)))
            1"""
    def __invert__(self) -> Any:
        """ComplexDoubleElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1213)

        This function returns the inverse, or reciprocal, of the complex
        number `z`:

        .. MATH::

            1/z = (x - i y)/(x^2 + y^2).

        EXAMPLES::

            sage: ~CDF(2,1)
            0.39999999999999997 - 0.19999999999999998*I
            sage: 1/CDF(2,1)
            0.39999999999999997 - 0.19999999999999998*I

        The inverse of 0 is ``NaN`` (it doesn't raise an exception)::

            sage: ~(0*CDF(0,1))
            NaN + NaN*I"""
    @overload
    def __mpc__(self) -> Any:
        """ComplexDoubleElement.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1147)

        Convert Sage ``ComplexDoubleElement`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: c = CDF(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')"""
    @overload
    def __mpc__(self) -> Any:
        """ComplexDoubleElement.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1147)

        Convert Sage ``ComplexDoubleElement`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: c = CDF(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')"""
    @overload
    def __pari__(self) -> Any:
        """ComplexDoubleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1126)

        Return PARI version of ``self``, as ``t_COMPLEX`` or ``t_REAL``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: CDF(1,2).__pari__()
            1.00000000000000 + 2.00000000000000*I
            sage: pari(CDF(1,2))
            1.00000000000000 + 2.00000000000000*I
            sage: pari(CDF(2.0))
            2.00000000000000
            sage: pari(CDF(I))
            1.00000000000000*I"""
    @overload
    def __pari__(self) -> Any:
        """ComplexDoubleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 1126)

        Return PARI version of ``self``, as ``t_COMPLEX`` or ``t_REAL``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: CDF(1,2).__pari__()
            1.00000000000000 + 2.00000000000000*I
            sage: pari(CDF(1,2))
            1.00000000000000 + 2.00000000000000*I
            sage: pari(CDF(2.0))
            2.00000000000000
            sage: pari(CDF(I))
            1.00000000000000*I"""
    def __reduce__(self) -> Any:
        """ComplexDoubleElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 756)

        For pickling.

        EXAMPLES::

            sage: a = CDF(-2.7, -3)
            sage: loads(dumps(a)) == a
            True"""

class ComplexDoubleField_class(sage.rings.abc.ComplexDoubleField):
    """ComplexDoubleField_class()

    File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 118)

    An approximation to the field of complex numbers using double
    precision floating point numbers. Answers derived from calculations
    in this approximation may differ from what they would be if those
    calculations were performed in the true field of complex numbers.
    This is due to the rounding errors inherent to finite precision
    calculations.

    ALGORITHM:

    Arithmetic is done using GSL (the GNU Scientific Library)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 131)

                Construct field of complex double precision numbers.

                EXAMPLES::

                    sage: from sage.rings.complex_double import ComplexDoubleField_class
                    sage: CDF == ComplexDoubleField_class()
                    True
                    sage: TestSuite(CDF).run(skip = ["_test_prod"])

                .. WARNING:: due to rounding errors, one can have `x^2 != x*x`::

                    sage: x = CDF.an_element()
                    sage: x
                    1.0*I
                    sage: x*x, x**2, x*x == x**2
                    (-1.0, -1.0 + 1.2246...e-16*I, False)
        '''
    @overload
    def algebraic_closure(self) -> Any:
        """ComplexDoubleField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 534)

        Return the algebraic closure of ``self``, i.e., the complex double
        field.

        EXAMPLES::

            sage: CDF.algebraic_closure()
            Complex Double Field"""
    @overload
    def algebraic_closure(self) -> Any:
        """ComplexDoubleField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 534)

        Return the algebraic closure of ``self``, i.e., the complex double
        field.

        EXAMPLES::

            sage: CDF.algebraic_closure()
            Complex Double Field"""
    @overload
    def characteristic(self) -> Any:
        """ComplexDoubleField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 207)

        Return the characteristic of the complex double field, which is 0.

        EXAMPLES::

            sage: CDF.characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """ComplexDoubleField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 207)

        Return the characteristic of the complex double field, which is 0.

        EXAMPLES::

            sage: CDF.characteristic()
            0"""
    @overload
    def construction(self) -> Any:
        """ComplexDoubleField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 569)

        Return the functorial construction of ``self``, namely, algebraic
        closure of the real double field.

        EXAMPLES::

            sage: c, S = CDF.construction(); S
            Real Double Field
            sage: CDF == c(S)
            True"""
    @overload
    def construction(self) -> Any:
        """ComplexDoubleField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 569)

        Return the functorial construction of ``self``, namely, algebraic
        closure of the real double field.

        EXAMPLES::

            sage: c, S = CDF.construction(); S
            Real Double Field
            sage: CDF == c(S)
            True"""
    def gen(self, n=...) -> Any:
        """ComplexDoubleField_class.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 506)

        Return the generator of the complex double field.

        EXAMPLES::

            sage: CDF.0
            1.0*I
            sage: CDF.gen(0)
            1.0*I"""
    @overload
    def is_exact(self) -> bool:
        """ComplexDoubleField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 166)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: CDF.is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexDoubleField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 166)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: CDF.is_exact()
            False"""
    def ngens(self) -> Any:
        """ComplexDoubleField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 521)

        The number of generators of this complex field as an `\\RR`-algebra.

        There is one generator, namely ``sqrt(-1)``.

        EXAMPLES::

            sage: CDF.ngens()
            1"""
    def pi(self) -> Any:
        """ComplexDoubleField_class.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 558)

        Return `\\pi` as a double precision complex number.

        EXAMPLES::

            sage: CDF.pi()
            3.141592653589793"""
    @overload
    def prec(self) -> Any:
        """ComplexDoubleField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 473)

        Return the precision of this complex double field (to be more
        similar to :class:`ComplexField`). Always returns 53.

        EXAMPLES::

            sage: CDF.prec()
            53"""
    @overload
    def prec(self) -> Any:
        """ComplexDoubleField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 473)

        Return the precision of this complex double field (to be more
        similar to :class:`ComplexField`). Always returns 53.

        EXAMPLES::

            sage: CDF.prec()
            53"""
    def precision(self, *args, **kwargs):
        """ComplexDoubleField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 473)

        Return the precision of this complex double field (to be more
        similar to :class:`ComplexField`). Always returns 53.

        EXAMPLES::

            sage: CDF.prec()
            53"""
    @overload
    def random_element(self, doublexmin=..., doublexmax=..., doubleymin=..., doubleymax=...) -> Any:
        """ComplexDoubleField_class.random_element(self, double xmin=-1, double xmax=1, double ymin=-1, double ymax=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 219)

        Return a random element of this complex double field with real and
        imaginary part bounded by ``xmin``, ``xmax``, ``ymin``, ``ymax``.

        EXAMPLES::

            sage: CDF.random_element().parent() is CDF
            True
            sage: re, im = CDF.random_element()
            sage: -1 <= re <= 1, -1 <= im <= 1
            (True, True)
            sage: re, im = CDF.random_element(-10,10,-10,10)
            sage: -10 <= re <= 10, -10 <= im <= 10
            (True, True)
            sage: re, im = CDF.random_element(-10^20,10^20,-2,2)
            sage: -10^20 <= re <= 10^20, -2 <= im <= 2
            (True, True)"""
    @overload
    def random_element(self) -> Any:
        """ComplexDoubleField_class.random_element(self, double xmin=-1, double xmax=1, double ymin=-1, double ymax=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 219)

        Return a random element of this complex double field with real and
        imaginary part bounded by ``xmin``, ``xmax``, ``ymin``, ``ymax``.

        EXAMPLES::

            sage: CDF.random_element().parent() is CDF
            True
            sage: re, im = CDF.random_element()
            sage: -1 <= re <= 1, -1 <= im <= 1
            (True, True)
            sage: re, im = CDF.random_element(-10,10,-10,10)
            sage: -10 <= re <= 10, -10 <= im <= 10
            (True, True)
            sage: re, im = CDF.random_element(-10^20,10^20,-2,2)
            sage: -10^20 <= re <= 10^20, -2 <= im <= 2
            (True, True)"""
    @overload
    def random_element(self) -> Any:
        """ComplexDoubleField_class.random_element(self, double xmin=-1, double xmax=1, double ymin=-1, double ymax=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 219)

        Return a random element of this complex double field with real and
        imaginary part bounded by ``xmin``, ``xmax``, ``ymin``, ``ymax``.

        EXAMPLES::

            sage: CDF.random_element().parent() is CDF
            True
            sage: re, im = CDF.random_element()
            sage: -1 <= re <= 1, -1 <= im <= 1
            (True, True)
            sage: re, im = CDF.random_element(-10,10,-10,10)
            sage: -10 <= re <= 10, -10 <= im <= 10
            (True, True)
            sage: re, im = CDF.random_element(-10^20,10^20,-2,2)
            sage: -10^20 <= re <= 10^20, -2 <= im <= 2
            (True, True)"""
    @overload
    def real_double_field(self) -> Any:
        """ComplexDoubleField_class.real_double_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 546)

        The real double field, which you may view as a subfield of this
        complex double field.

        EXAMPLES::

            sage: CDF.real_double_field()
            Real Double Field"""
    @overload
    def real_double_field(self) -> Any:
        """ComplexDoubleField_class.real_double_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 546)

        The real double field, which you may view as a subfield of this
        complex double field.

        EXAMPLES::

            sage: CDF.real_double_field()
            Real Double Field"""
    def to_prec(self, prec) -> Any:
        """ComplexDoubleField_class.to_prec(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 487)

        Return the complex field to the specified precision. As doubles
        have fixed precision, this will only return a complex double field
        if prec is exactly 53.

        EXAMPLES::

            sage: CDF.to_prec(53)
            Complex Double Field
            sage: CDF.to_prec(250)
            Complex Field with 250 bits of precision"""
    def zeta(self, n=...) -> Any:
        """ComplexDoubleField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 584)

        Return a primitive `n`-th root of unity in this CDF, for
        `n \\geq 1`.

        INPUT:

        - ``n`` -- positive integer (default: 2)

        OUTPUT: a complex `n`-th root of unity

        EXAMPLES::

            sage: CDF.zeta(7)  # rel tol 1e-15
            0.6234898018587336 + 0.7818314824680298*I
            sage: CDF.zeta(1)
            1.0
            sage: CDF.zeta()
            -1.0
            sage: CDF.zeta() == CDF.zeta(2)
            True

        ::

            sage: CDF.zeta(0.5)
            Traceback (most recent call last):
            ...
            ValueError: n must be a positive integer
            sage: CDF.zeta(0)
            Traceback (most recent call last):
            ...
            ValueError: n must be a positive integer
            sage: CDF.zeta(-1)
            Traceback (most recent call last):
            ...
            ValueError: n must be a positive integer"""
    def __call__(self, x=..., im=...) -> Any:
        '''ComplexDoubleField_class.__call__(self, x=None, im=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 273)

        Create a complex double using ``x`` and optionally an imaginary part
        ``im``.

        EXAMPLES::

            sage: CDF(0,1) # indirect doctest
            1.0*I
            sage: CDF(2/3) # indirect doctest
            0.6666666666666666
            sage: CDF(5) # indirect doctest
            5.0
            sage: CDF(\'i\') # indirect doctest
            1.0*I
            sage: CDF(complex(2,-3)) # indirect doctest
            2.0 - 3.0*I
            sage: CDF(4.5) # indirect doctest
            4.5
            sage: CDF(1+I)  # indirect doctest                                          # needs sage.symbolic
            1.0 + 1.0*I
            sage: CDF(pari(1))                                                          # needs sage.libs.pari
            1.0
            sage: CDF(pari("I"))                                                        # needs sage.libs.pari
            1.0*I
            sage: CDF(pari("x^2 + x + 1").polroots()[0])                                # needs sage.libs.pari
            -0.5 - 0.8660254037844386*I
            sage: from gmpy2 import mpc
            sage: CDF(mpc(\'2.0+1.0j\'))
            2.0 + 1.0*I

        A :exc:`TypeError` is raised if the coercion doesn\'t make sense::

            sage: CDF(QQ[\'x\'].0)
            Traceback (most recent call last):
            ...
            TypeError: cannot convert nonconstant polynomial

        One can convert back and forth between double precision complex
        numbers and higher-precision ones, though of course there may be
        loss of precision::

            sage: # needs sage.rings.real_mpfr
            sage: a = ComplexField(200)(-2).sqrt(); a
            1.4142135623730950488016887242096980785696718753769480731767*I
            sage: b = CDF(a); b
            1.4142135623730951*I
            sage: a.parent()(b)
            1.4142135623730951454746218587388284504413604736328125000000*I
            sage: a.parent()(b) == b
            True
            sage: b == CC(a)
            True

        TESTS:

        Check that :issue:`31836` is fixed::

            sage: a = CDF(); a
            0.0
            sage: a.parent()
            Complex Double Field'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """ComplexDoubleField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 192)

        Return the hash for ``self``.

        This class is intended for use as a singleton so any instance
        of it should be equivalent from a hashing perspective.

        TESTS::

            sage: from sage.rings.complex_double import ComplexDoubleField_class
            sage: hash(CDF) == hash(ComplexDoubleField_class())
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """ComplexDoubleField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 155)

        For pickling.

        EXAMPLES::

            sage: loads(dumps(CDF)) is CDF
            True"""

class ComplexToCDF(sage.categories.morphism.Morphism):
    """ComplexToCDF(R)

    File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2553)

    Fast morphism for anything such that the elements have attributes ``.real``
    and ``.imag`` (e.g. numpy complex types).

    EXAMPLES::

        sage: # needs numpy
        sage: import numpy
        sage: f = CDF.coerce_map_from(numpy.complex128)
        sage: f(numpy.complex128(I))
        1.0*I
        sage: f(numpy.complex128(I)).parent()
        Complex Double Field"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2568)"""

class FloatToCDF(sage.categories.morphism.Morphism):
    """FloatToCDF(R)

    File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2476)

    Fast morphism from anything with a ``__float__`` method to a CDF element.

    EXAMPLES::

        sage: f = CDF.coerce_map_from(ZZ); f
        Native morphism:
          From: Integer Ring
          To:   Complex Double Field
        sage: f(4)
        4.0
        sage: f = CDF.coerce_map_from(QQ); f
        Native morphism:
          From: Rational Field
          To:   Complex Double Field
        sage: f(1/2)
        0.5
        sage: f = CDF.coerce_map_from(int); f
        Native morphism:
          From: Set of Python objects of class 'int'
          To:   Complex Double Field
        sage: f(3r)
        3.0
        sage: f = CDF.coerce_map_from(float); f
        Native morphism:
          From: Set of Python objects of class 'float'
          To:   Complex Double Field
        sage: f(3.5)
        3.5"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_double.pyx (starting at line 2507)

                Initialize ``self``.

                EXAMPLES::

                    sage: f = CDF.coerce_map_from(ZZ); f
                    Native morphism:
                      From: Integer Ring
                      To:   Complex Double Field
        """

CDF: ComplexDoubleField_class