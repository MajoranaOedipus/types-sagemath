import sage.rings.real_double
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class RealDoubleElement_gsl(sage.rings.real_double.RealDoubleElement):
    _factorial: ClassVar[method] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def acosh(self) -> Any:
        """RealDoubleElement_gsl.acosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 649)

        Return the hyperbolic inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.cosh(); i
            2.5091784786580567
            sage: abs(i.acosh()-q) < 1e-15
            True"""
    @overload
    def acosh(self) -> Any:
        """RealDoubleElement_gsl.acosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 649)

        Return the hyperbolic inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.cosh(); i
            2.5091784786580567
            sage: abs(i.acosh()-q) < 1e-15
            True"""
    @overload
    def arccos(self) -> Any:
        """RealDoubleElement_gsl.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 574)

        Return the inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/3
            sage: i = q.cos()
            sage: i.arccos() == q
            True"""
    @overload
    def arccos(self) -> Any:
        """RealDoubleElement_gsl.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 574)

        Return the inverse cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/3
            sage: i = q.cos()
            sage: i.arccos() == q
            True"""
    @overload
    def arcsin(self) -> Any:
        """RealDoubleElement_gsl.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 587)

        Return the inverse sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/5
            sage: i = q.sin()
            sage: i.arcsin() == q
            True"""
    @overload
    def arcsin(self) -> Any:
        """RealDoubleElement_gsl.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 587)

        Return the inverse sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/5
            sage: i = q.sin()
            sage: i.arcsin() == q
            True"""
    @overload
    def arcsinh(self) -> Any:
        """RealDoubleElement_gsl.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 663)

        Return the hyperbolic inverse sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.sinh(); i
            2.3012989023072947
            sage: abs(i.arcsinh()-q) < 1e-15
            True"""
    @overload
    def arcsinh(self) -> Any:
        """RealDoubleElement_gsl.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 663)

        Return the hyperbolic inverse sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.sinh(); i
            2.3012989023072947
            sage: abs(i.arcsinh()-q) < 1e-15
            True"""
    @overload
    def arctan(self) -> Any:
        """RealDoubleElement_gsl.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 600)

        Return the inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/5
            sage: i = q.tan()
            sage: i.arctan() == q
            True"""
    @overload
    def arctan(self) -> Any:
        """RealDoubleElement_gsl.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 600)

        Return the inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/5
            sage: i = q.tan()
            sage: i.arctan() == q
            True"""
    @overload
    def arctanh(self) -> Any:
        """RealDoubleElement_gsl.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 677)

        Return the hyperbolic inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.tanh(); i
            0.9171523356672744
            sage: i.arctanh() - q  # rel tol 1
            4.440892098500626e-16"""
    @overload
    def arctanh(self) -> Any:
        """RealDoubleElement_gsl.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 677)

        Return the hyperbolic inverse tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/2
            sage: i = q.tanh(); i
            0.9171523356672744
            sage: i.arctanh() - q  # rel tol 1
            4.440892098500626e-16"""
    @overload
    def cos(self) -> Any:
        """RealDoubleElement_gsl.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 466)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: t=RDF.pi()/2
            sage: t.cos()
            6.123233995736757e-17"""
    @overload
    def cos(self) -> Any:
        """RealDoubleElement_gsl.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 466)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: t=RDF.pi()/2
            sage: t.cos()
            6.123233995736757e-17"""
    @overload
    def cosh(self) -> Any:
        """RealDoubleElement_gsl.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 613)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.cosh()
            1.0344656400955106"""
    @overload
    def cosh(self) -> Any:
        """RealDoubleElement_gsl.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 613)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.cosh()
            1.0344656400955106"""
    @overload
    def coth(self) -> Any:
        """RealDoubleElement_gsl.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 717)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RDF(pi).coth()
            1.003741873197321
            sage: CDF(pi).coth()
            1.0037418731973213"""
    @overload
    def coth(self) -> Any:
        """RealDoubleElement_gsl.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 717)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RDF(pi).coth()
            1.003741873197321
            sage: CDF(pi).coth()
            1.0037418731973213"""
    @overload
    def coth(self) -> Any:
        """RealDoubleElement_gsl.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 717)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: RDF(pi).coth()
            1.003741873197321
            sage: CDF(pi).coth()
            1.0037418731973213"""
    @overload
    def csch(self) -> Any:
        """RealDoubleElement_gsl.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 704)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RDF(pi).csch()
            0.08658953753004694
            sage: CDF(pi).csch()  # rel tol 1e-15
            0.08658953753004696"""
    @overload
    def csch(self) -> Any:
        """RealDoubleElement_gsl.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 704)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RDF(pi).csch()
            0.08658953753004694
            sage: CDF(pi).csch()  # rel tol 1e-15
            0.08658953753004696"""
    @overload
    def csch(self) -> Any:
        """RealDoubleElement_gsl.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 704)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: RDF(pi).csch()
            0.08658953753004694
            sage: CDF(pi).csch()  # rel tol 1e-15
            0.08658953753004696"""
    def dilog(self) -> Any:
        """RealDoubleElement_gsl.dilog(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 489)

        Return the dilogarithm of ``self``.

        This is defined by the
        series `\\sum_n x^n/n^2` for `|x| \\le 1`. When the absolute
        value of ``self`` is greater than 1, the returned value is the
        real part of (the analytic continuation to `\\CC` of) the
        dilogarithm of ``self``.

        EXAMPLES::

            sage: RDF(1).dilog()  # rel tol 1.0e-13
            1.6449340668482264
            sage: RDF(2).dilog()  # rel tol 1.0e-13
            2.46740110027234"""
    @overload
    def erf(self) -> Any:
        """RealDoubleElement_gsl.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 730)

        Return the value of the error function on ``self``.

        EXAMPLES::

            sage: RDF(6).erf()
            1.0"""
    @overload
    def erf(self) -> Any:
        """RealDoubleElement_gsl.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 730)

        Return the value of the error function on ``self``.

        EXAMPLES::

            sage: RDF(6).erf()
            1.0"""
    def exp(self) -> Any:
        """RealDoubleElement_gsl.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 378)

        Return `e^\\mathtt{self}`.

        EXAMPLES::

            sage: r = RDF(0.0)
            sage: r.exp()
            1.0

        ::

            sage: r = RDF('32.3')
            sage: a = r.exp(); a
            106588847274864.47
            sage: a.log()
            32.3

        ::

            sage: r = RDF('-32.3')
            sage: r.exp()
            9.381844588498685e-15

        ::

            sage: RDF(1000).exp()
            +infinity"""
    def exp10(self) -> Any:
        """RealDoubleElement_gsl.exp10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 439)

        Return `10^\\mathtt{self}`.

        EXAMPLES::

            sage: r = RDF(0.0)
            sage: r.exp10()
            1.0

        ::

            sage: r = RDF(32.0)
            sage: r.exp10()
            1.0000000000000069e+32

        ::

            sage: r = RDF(-32.3)
            sage: r.exp10()
            5.011872336272702e-33"""
    def exp2(self) -> Any:
        """RealDoubleElement_gsl.exp2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 412)

        Return `2^\\mathtt{self}`.

        EXAMPLES::

            sage: r = RDF(0.0)
            sage: r.exp2()
            1.0

        ::

            sage: r = RDF(32.0)
            sage: r.exp2()
            4294967295.9999967

        ::

            sage: r = RDF(-32.3)
            sage: r.exp2()
            1.8911724825302065e-10"""
    @overload
    def gamma(self) -> Any:
        """RealDoubleElement_gsl.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 755)

        Return the value of the Euler gamma function on ``self``.

        EXAMPLES::

            sage: RDF(6).gamma()
            120.0
            sage: RDF(1.5).gamma()  # rel tol 1e-15
            0.8862269254527584"""
    @overload
    def gamma(self) -> Any:
        """RealDoubleElement_gsl.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 755)

        Return the value of the Euler gamma function on ``self``.

        EXAMPLES::

            sage: RDF(6).gamma()
            120.0
            sage: RDF(1.5).gamma()  # rel tol 1e-15
            0.8862269254527584"""
    @overload
    def gamma(self) -> Any:
        """RealDoubleElement_gsl.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 755)

        Return the value of the Euler gamma function on ``self``.

        EXAMPLES::

            sage: RDF(6).gamma()
            120.0
            sage: RDF(1.5).gamma()  # rel tol 1e-15
            0.8862269254527584"""
    def hypot(self, other) -> Any:
        """RealDoubleElement_gsl.hypot(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 556)

        Compute the value `\\sqrt{s^2 + o^2}` where `s` is ``self`` and `o`
        is ``other`` in such a way as to avoid overflow.

        EXAMPLES::

            sage: x = RDF(4e300); y = RDF(3e300)
            sage: x.hypot(y)
            5e+300
            sage: sqrt(x^2+y^2) # overflow
            +infinity"""
    @overload
    def log(self, base=...) -> Any:
        '''RealDoubleElement_gsl.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 237)

        Return the logarithm.

        INPUT:

        - ``base`` -- integer or ``None`` (default). The base of the
          logarithm. If ``None`` is specified, the base is `e` (the so-called
          natural logarithm).

        OUTPUT:

        The logarithm of ``self``.  If ``self`` is positive, a double
        floating point number. Infinity if ``self`` is zero. A
        imaginary complex floating point number if ``self`` is
        negative.

        EXAMPLES::

            sage: RDF(2).log()
            0.6931471805599453
            sage: RDF(2).log(2)
            1.0
            sage: RDF(2).log(pi)                                                        # needs sage.symbolic
            0.6055115613982801
            sage: RDF(2).log(10)
            0.30102999566398114
            sage: RDF(2).log(1.5)
            1.7095112913514547
            sage: RDF(0).log()
            -infinity
            sage: RDF(-1).log()
            3.141592653589793*I
            sage: RDF(-1).log(2)  # rel tol 1e-15
            4.532360141827194*I

        TESTS:

        Make sure that we can take the log of small numbers accurately
        and the fix doesn\'t break preexisting values (:issue:`12557`)::

            sage: R = RealField(128)
            sage: def check_error(x):
            ....:   x = RDF(x)
            ....:   log_RDF = x.log()
            ....:   log_RR = R(x).log()
            ....:   diff = R(log_RDF) - log_RR
            ....:   if abs(diff) < log_RDF.ulp():
            ....:       return True
            ....:   print("logarithm check failed for %s (diff = %s ulp)"%             ....:       (x, diff/log_RDF.ulp()))
            ....:   return False
            sage: all( check_error(2^x) for x in range(-100,100) )
            True
            sage: all( check_error(x) for x in sxrange(0.01, 2.00, 0.01) )
            True
            sage: all( check_error(x) for x in sxrange(0.99, 1.01, 0.001) )
            True
            sage: RDF(1.000000001).log()
            1.000000082240371e-09
            sage: RDF(1e-17).log()
            -39.14394658089878
            sage: RDF(1e-50).log()
            -115.12925464970229'''
    @overload
    def log(self) -> Any:
        '''RealDoubleElement_gsl.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 237)

        Return the logarithm.

        INPUT:

        - ``base`` -- integer or ``None`` (default). The base of the
          logarithm. If ``None`` is specified, the base is `e` (the so-called
          natural logarithm).

        OUTPUT:

        The logarithm of ``self``.  If ``self`` is positive, a double
        floating point number. Infinity if ``self`` is zero. A
        imaginary complex floating point number if ``self`` is
        negative.

        EXAMPLES::

            sage: RDF(2).log()
            0.6931471805599453
            sage: RDF(2).log(2)
            1.0
            sage: RDF(2).log(pi)                                                        # needs sage.symbolic
            0.6055115613982801
            sage: RDF(2).log(10)
            0.30102999566398114
            sage: RDF(2).log(1.5)
            1.7095112913514547
            sage: RDF(0).log()
            -infinity
            sage: RDF(-1).log()
            3.141592653589793*I
            sage: RDF(-1).log(2)  # rel tol 1e-15
            4.532360141827194*I

        TESTS:

        Make sure that we can take the log of small numbers accurately
        and the fix doesn\'t break preexisting values (:issue:`12557`)::

            sage: R = RealField(128)
            sage: def check_error(x):
            ....:   x = RDF(x)
            ....:   log_RDF = x.log()
            ....:   log_RR = R(x).log()
            ....:   diff = R(log_RDF) - log_RR
            ....:   if abs(diff) < log_RDF.ulp():
            ....:       return True
            ....:   print("logarithm check failed for %s (diff = %s ulp)"%             ....:       (x, diff/log_RDF.ulp()))
            ....:   return False
            sage: all( check_error(2^x) for x in range(-100,100) )
            True
            sage: all( check_error(x) for x in sxrange(0.01, 2.00, 0.01) )
            True
            sage: all( check_error(x) for x in sxrange(0.99, 1.01, 0.001) )
            True
            sage: RDF(1.000000001).log()
            1.000000082240371e-09
            sage: RDF(1e-17).log()
            -39.14394658089878
            sage: RDF(1e-50).log()
            -115.12925464970229'''
    @overload
    def log(self, pi) -> Any:
        '''RealDoubleElement_gsl.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 237)

        Return the logarithm.

        INPUT:

        - ``base`` -- integer or ``None`` (default). The base of the
          logarithm. If ``None`` is specified, the base is `e` (the so-called
          natural logarithm).

        OUTPUT:

        The logarithm of ``self``.  If ``self`` is positive, a double
        floating point number. Infinity if ``self`` is zero. A
        imaginary complex floating point number if ``self`` is
        negative.

        EXAMPLES::

            sage: RDF(2).log()
            0.6931471805599453
            sage: RDF(2).log(2)
            1.0
            sage: RDF(2).log(pi)                                                        # needs sage.symbolic
            0.6055115613982801
            sage: RDF(2).log(10)
            0.30102999566398114
            sage: RDF(2).log(1.5)
            1.7095112913514547
            sage: RDF(0).log()
            -infinity
            sage: RDF(-1).log()
            3.141592653589793*I
            sage: RDF(-1).log(2)  # rel tol 1e-15
            4.532360141827194*I

        TESTS:

        Make sure that we can take the log of small numbers accurately
        and the fix doesn\'t break preexisting values (:issue:`12557`)::

            sage: R = RealField(128)
            sage: def check_error(x):
            ....:   x = RDF(x)
            ....:   log_RDF = x.log()
            ....:   log_RR = R(x).log()
            ....:   diff = R(log_RDF) - log_RR
            ....:   if abs(diff) < log_RDF.ulp():
            ....:       return True
            ....:   print("logarithm check failed for %s (diff = %s ulp)"%             ....:       (x, diff/log_RDF.ulp()))
            ....:   return False
            sage: all( check_error(2^x) for x in range(-100,100) )
            True
            sage: all( check_error(x) for x in sxrange(0.01, 2.00, 0.01) )
            True
            sage: all( check_error(x) for x in sxrange(0.99, 1.01, 0.001) )
            True
            sage: RDF(1.000000001).log()
            1.000000082240371e-09
            sage: RDF(1e-17).log()
            -39.14394658089878
            sage: RDF(1e-50).log()
            -115.12925464970229'''
    @overload
    def log(self) -> Any:
        '''RealDoubleElement_gsl.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 237)

        Return the logarithm.

        INPUT:

        - ``base`` -- integer or ``None`` (default). The base of the
          logarithm. If ``None`` is specified, the base is `e` (the so-called
          natural logarithm).

        OUTPUT:

        The logarithm of ``self``.  If ``self`` is positive, a double
        floating point number. Infinity if ``self`` is zero. A
        imaginary complex floating point number if ``self`` is
        negative.

        EXAMPLES::

            sage: RDF(2).log()
            0.6931471805599453
            sage: RDF(2).log(2)
            1.0
            sage: RDF(2).log(pi)                                                        # needs sage.symbolic
            0.6055115613982801
            sage: RDF(2).log(10)
            0.30102999566398114
            sage: RDF(2).log(1.5)
            1.7095112913514547
            sage: RDF(0).log()
            -infinity
            sage: RDF(-1).log()
            3.141592653589793*I
            sage: RDF(-1).log(2)  # rel tol 1e-15
            4.532360141827194*I

        TESTS:

        Make sure that we can take the log of small numbers accurately
        and the fix doesn\'t break preexisting values (:issue:`12557`)::

            sage: R = RealField(128)
            sage: def check_error(x):
            ....:   x = RDF(x)
            ....:   log_RDF = x.log()
            ....:   log_RR = R(x).log()
            ....:   diff = R(log_RDF) - log_RR
            ....:   if abs(diff) < log_RDF.ulp():
            ....:       return True
            ....:   print("logarithm check failed for %s (diff = %s ulp)"%             ....:       (x, diff/log_RDF.ulp()))
            ....:   return False
            sage: all( check_error(2^x) for x in range(-100,100) )
            True
            sage: all( check_error(x) for x in sxrange(0.01, 2.00, 0.01) )
            True
            sage: all( check_error(x) for x in sxrange(0.99, 1.01, 0.001) )
            True
            sage: RDF(1.000000001).log()
            1.000000082240371e-09
            sage: RDF(1e-17).log()
            -39.14394658089878
            sage: RDF(1e-50).log()
            -115.12925464970229'''
    @overload
    def log(self) -> Any:
        '''RealDoubleElement_gsl.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 237)

        Return the logarithm.

        INPUT:

        - ``base`` -- integer or ``None`` (default). The base of the
          logarithm. If ``None`` is specified, the base is `e` (the so-called
          natural logarithm).

        OUTPUT:

        The logarithm of ``self``.  If ``self`` is positive, a double
        floating point number. Infinity if ``self`` is zero. A
        imaginary complex floating point number if ``self`` is
        negative.

        EXAMPLES::

            sage: RDF(2).log()
            0.6931471805599453
            sage: RDF(2).log(2)
            1.0
            sage: RDF(2).log(pi)                                                        # needs sage.symbolic
            0.6055115613982801
            sage: RDF(2).log(10)
            0.30102999566398114
            sage: RDF(2).log(1.5)
            1.7095112913514547
            sage: RDF(0).log()
            -infinity
            sage: RDF(-1).log()
            3.141592653589793*I
            sage: RDF(-1).log(2)  # rel tol 1e-15
            4.532360141827194*I

        TESTS:

        Make sure that we can take the log of small numbers accurately
        and the fix doesn\'t break preexisting values (:issue:`12557`)::

            sage: R = RealField(128)
            sage: def check_error(x):
            ....:   x = RDF(x)
            ....:   log_RDF = x.log()
            ....:   log_RR = R(x).log()
            ....:   diff = R(log_RDF) - log_RR
            ....:   if abs(diff) < log_RDF.ulp():
            ....:       return True
            ....:   print("logarithm check failed for %s (diff = %s ulp)"%             ....:       (x, diff/log_RDF.ulp()))
            ....:   return False
            sage: all( check_error(2^x) for x in range(-100,100) )
            True
            sage: all( check_error(x) for x in sxrange(0.01, 2.00, 0.01) )
            True
            sage: all( check_error(x) for x in sxrange(0.99, 1.01, 0.001) )
            True
            sage: RDF(1.000000001).log()
            1.000000082240371e-09
            sage: RDF(1e-17).log()
            -39.14394658089878
            sage: RDF(1e-50).log()
            -115.12925464970229'''
    @overload
    def log10(self) -> Any:
        """RealDoubleElement_gsl.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 336)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RDF('16.0'); r.log10()
            1.2041199826559248
            sage: r.log() / RDF(log(10))                                                # needs sage.symbolic
            1.2041199826559246
            sage: r = RDF('39.9'); r.log10()
            1.6009728956867482"""
    @overload
    def log10(self) -> Any:
        """RealDoubleElement_gsl.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 336)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RDF('16.0'); r.log10()
            1.2041199826559248
            sage: r.log() / RDF(log(10))                                                # needs sage.symbolic
            1.2041199826559246
            sage: r = RDF('39.9'); r.log10()
            1.6009728956867482"""
    @overload
    def log10(self) -> Any:
        """RealDoubleElement_gsl.log10(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 336)

        Return log to the base 10 of ``self``.

        EXAMPLES::

            sage: r = RDF('16.0'); r.log10()
            1.2041199826559248
            sage: r.log() / RDF(log(10))                                                # needs sage.symbolic
            1.2041199826559246
            sage: r = RDF('39.9'); r.log10()
            1.6009728956867482"""
    @overload
    def log2(self) -> Any:
        """RealDoubleElement_gsl.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 313)

        Return log to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RDF(16.0)
            sage: r.log2()
            4.0

        ::

            sage: r = RDF(31.9); r.log2()
            4.9954845188775066"""
    @overload
    def log2(self) -> Any:
        """RealDoubleElement_gsl.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 313)

        Return log to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RDF(16.0)
            sage: r.log2()
            4.0

        ::

            sage: r = RDF(31.9); r.log2()
            4.9954845188775066"""
    @overload
    def log2(self) -> Any:
        """RealDoubleElement_gsl.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 313)

        Return log to the base 2 of ``self``.

        EXAMPLES::

            sage: r = RDF(16.0)
            sage: r.log2()
            4.0

        ::

            sage: r = RDF(31.9); r.log2()
            4.9954845188775066"""
    def logpi(self) -> Any:
        """RealDoubleElement_gsl.logpi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 357)

        Return log to the base `\\pi` of ``self``.

        EXAMPLES::

            sage: r = RDF(16); r.logpi()
            2.4220462455931204
            sage: r.log() / RDF(log(pi))                                                # needs sage.symbolic
            2.4220462455931204
            sage: r = RDF('39.9'); r.logpi()
            3.2203023346075152"""
    def nth_root(self, intn) -> Any:
        """RealDoubleElement_gsl.nth_root(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 27)

        Return the `n`-th root of ``self``.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        The output is a complex double if ``self`` is negative and `n` is even,
        otherwise it is a real double.

        EXAMPLES::

            sage: r = RDF(-125.0); r.nth_root(3)
            -5.000000000000001
            sage: r.nth_root(5)
            -2.6265278044037674
            sage: RDF(-2).nth_root(5)^5  # rel tol 1e-15
            -2.000000000000001
            sage: RDF(-1).nth_root(5)^5
            -1.0
            sage: RDF(3).nth_root(10)^10
            2.9999999999999982
            sage: RDF(-1).nth_root(2)
            6.123233995736757e-17 + 1.0*I
            sage: RDF(-1).nth_root(4)
            0.7071067811865476 + 0.7071067811865475*I"""
    def restrict_angle(self) -> Any:
        """RealDoubleElement_gsl.restrict_angle(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 508)

        Return a number congruent to ``self`` mod `2\\pi` that lies in
        the interval `(-\\pi, \\pi]`.

        Specifically, it is the unique `x \\in (-\\pi, \\pi]` such
        that ``self`` `= x + 2\\pi n` for some `n \\in \\ZZ`.

        EXAMPLES::

            sage: RDF(pi).restrict_angle()                                              # needs sage.symbolic
            3.141592653589793
            sage: RDF(pi + 1e-10).restrict_angle()                                      # needs sage.symbolic
            -3.1415926534897936
            sage: RDF(1+10^10*pi).restrict_angle()                                      # needs sage.symbolic
            0.9999977606..."""
    @overload
    def sech(self) -> Any:
        """RealDoubleElement_gsl.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 691)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RDF(pi).sech()
            0.08626673833405443
            sage: CDF(pi).sech()
            0.08626673833405443"""
    @overload
    def sech(self) -> Any:
        """RealDoubleElement_gsl.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 691)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RDF(pi).sech()
            0.08626673833405443
            sage: CDF(pi).sech()
            0.08626673833405443"""
    @overload
    def sech(self) -> Any:
        """RealDoubleElement_gsl.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 691)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: RDF(pi).sech()
            0.08626673833405443
            sage: CDF(pi).sech()
            0.08626673833405443"""
    @overload
    def sin(self) -> Any:
        """RealDoubleElement_gsl.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 478)

        Return the sine of ``self``.

        EXAMPLES::

            sage: RDF(2).sin()
            0.9092974268256817"""
    @overload
    def sin(self) -> Any:
        """RealDoubleElement_gsl.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 478)

        Return the sine of ``self``.

        EXAMPLES::

            sage: RDF(2).sin()
            0.9092974268256817"""
    @overload
    def sincos(self) -> Any:
        """RealDoubleElement_gsl.sincos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 544)

        Return a pair consisting of the sine and cosine of ``self``.

        EXAMPLES::

            sage: t = RDF.pi()/6
            sage: t.sincos()
            (0.49999999999999994, 0.8660254037844387)"""
    @overload
    def sincos(self) -> Any:
        """RealDoubleElement_gsl.sincos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 544)

        Return a pair consisting of the sine and cosine of ``self``.

        EXAMPLES::

            sage: t = RDF.pi()/6
            sage: t.sincos()
            (0.49999999999999994, 0.8660254037844387)"""
    @overload
    def sinh(self) -> Any:
        """RealDoubleElement_gsl.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 625)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.sinh()
            0.26480022760227073"""
    @overload
    def sinh(self) -> Any:
        """RealDoubleElement_gsl.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 625)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.sinh()
            0.26480022760227073"""
    @overload
    def tan(self) -> Any:
        """RealDoubleElement_gsl.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 527)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/3
            sage: q.tan()
            1.7320508075688767
            sage: q = RDF.pi()/6
            sage: q.tan()
            0.5773502691896256"""
    @overload
    def tan(self) -> Any:
        """RealDoubleElement_gsl.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 527)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/3
            sage: q.tan()
            1.7320508075688767
            sage: q = RDF.pi()/6
            sage: q.tan()
            0.5773502691896256"""
    @overload
    def tan(self) -> Any:
        """RealDoubleElement_gsl.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 527)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/3
            sage: q.tan()
            1.7320508075688767
            sage: q = RDF.pi()/6
            sage: q.tan()
            0.5773502691896256"""
    @overload
    def tanh(self) -> Any:
        """RealDoubleElement_gsl.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 637)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.tanh()
            0.25597778924568454"""
    @overload
    def tanh(self) -> Any:
        """RealDoubleElement_gsl.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 637)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: q = RDF.pi()/12
            sage: q.tanh()
            0.25597778924568454"""
    @overload
    def zeta(self) -> Any:
        """RealDoubleElement_gsl.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 771)

        Return the Riemann zeta function evaluated at this real number.

        .. NOTE::

           PARI is vastly more efficient at computing the Riemann zeta
           function. See the example below for how to use it.

        EXAMPLES::

            sage: RDF(2).zeta()  # rel tol 1e-15
            1.6449340668482269
            sage: RDF.pi()^2/6
            1.6449340668482264
            sage: RDF(-2).zeta()
            0.0
            sage: RDF(1).zeta()
            +infinity"""
    @overload
    def zeta(self) -> Any:
        """RealDoubleElement_gsl.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 771)

        Return the Riemann zeta function evaluated at this real number.

        .. NOTE::

           PARI is vastly more efficient at computing the Riemann zeta
           function. See the example below for how to use it.

        EXAMPLES::

            sage: RDF(2).zeta()  # rel tol 1e-15
            1.6449340668482269
            sage: RDF.pi()^2/6
            1.6449340668482264
            sage: RDF(-2).zeta()
            0.0
            sage: RDF(1).zeta()
            +infinity"""
    @overload
    def zeta(self) -> Any:
        """RealDoubleElement_gsl.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 771)

        Return the Riemann zeta function evaluated at this real number.

        .. NOTE::

           PARI is vastly more efficient at computing the Riemann zeta
           function. See the example below for how to use it.

        EXAMPLES::

            sage: RDF(2).zeta()  # rel tol 1e-15
            1.6449340668482269
            sage: RDF.pi()^2/6
            1.6449340668482264
            sage: RDF(-2).zeta()
            0.0
            sage: RDF(1).zeta()
            +infinity"""
    @overload
    def zeta(self) -> Any:
        """RealDoubleElement_gsl.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double_element_gsl.pyx (starting at line 771)

        Return the Riemann zeta function evaluated at this real number.

        .. NOTE::

           PARI is vastly more efficient at computing the Riemann zeta
           function. See the example below for how to use it.

        EXAMPLES::

            sage: RDF(2).zeta()  # rel tol 1e-15
            1.6449340668482269
            sage: RDF.pi()^2/6
            1.6449340668482264
            sage: RDF(-2).zeta()
            0.0
            sage: RDF(1).zeta()
            +infinity"""
