import _cython_3_2_1
import sage.structure.sage_object
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.polynomial.pbori.pbori import BooleanPolynomial as BooleanPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
random_boolean_function: _cython_3_2_1.cython_function_or_method
unpickle_BooleanFunction: _cython_3_2_1.cython_function_or_method

class BooleanFunction(sage.structure.sage_object.SageObject):
    '''File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 152)

        This module implements Boolean functions represented as a truth table.

        We can construct a Boolean Function from either:

        - an integer -- the result is the zero function with ``x`` variables;
        - a list -- it is expected to be the truth table of the
          result. Therefore it must be of length a power of 2, and its
          elements are interpreted as Booleans;
        - a string -- representing the truth table in hexadecimal;
        - a Boolean polynomial -- the result is the corresponding Boolean function;
        - a polynomial `P` over an extension of `\\GF{2}` -- the result is
          the Boolean function with truth table ``(Tr(P(x)) for x in
          GF(2^k))``

        EXAMPLES:

        from the number of variables::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: BooleanFunction(5)
            Boolean function with 5 variables

        from a truth table::

            sage: BooleanFunction([1,0,0,1])
            Boolean function with 2 variables

        note that elements can be of different types::

            sage: B = BooleanFunction([False, sqrt(2)]); B                                  # needs sage.symbolic
            Boolean function with 1 variable
            sage: [b for b in B]                                                            # needs sage.symbolic
            [False, True]

        from a string::

            sage: BooleanFunction("111e")
            Boolean function with 4 variables

        from a :class:`sage.rings.polynomial.pbori.BooleanPolynomial`::

            sage: R.<x,y,z> = BooleanPolynomialRing(3)                                      # needs sage.rings.polynomial.pbori
            sage: P = x*y                                                                   # needs sage.rings.polynomial.pbori
            sage: BooleanFunction(P)                                                        # needs sage.rings.polynomial.pbori
            Boolean function with 3 variables

        from a polynomial over a binary field::

            sage: R.<x> = GF(2^8,\'a\')[]                                                     # needs sage.rings.finite_rings
            sage: B = BooleanFunction(x^7); B                                               # needs sage.rings.finite_rings
            Boolean function with 8 variables

        two failure cases::

            sage: BooleanFunction(sqrt(2))                                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unable to init the Boolean function

            sage: BooleanFunction([1, 0, 1])
            Traceback (most recent call last):
            ...
            ValueError: the length of the truth table must be a power of 2
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def absolut_indicator(self, *args, **kwargs):
        """Deprecated: Use :meth:`absolute_indicator` instead.
        See :issue:`28001` for details.

        """
    @overload
    def absolute_autocorrelation(self) -> Any:
        '''BooleanFunction.absolute_autocorrelation(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 919)

        Return the absolute autocorrelation of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: sorted(B.absolute_autocorrelation().items())
            [(0, 33), (8, 58), (16, 28), (24, 6), (32, 2), (128, 1)]'''
    @overload
    def absolute_autocorrelation(self) -> Any:
        '''BooleanFunction.absolute_autocorrelation(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 919)

        Return the absolute autocorrelation of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: sorted(B.absolute_autocorrelation().items())
            [(0, 33), (8, 58), (16, 28), (24, 6), (32, 2), (128, 1)]'''
    @overload
    def absolute_indicator(self) -> Any:
        '''BooleanFunction.absolute_indicator(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 939)

        Return the absolute indicator of the function.

        The absolute indicator is defined as the maximal absolute value of
        the autocorrelation.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.absolute_indicator()
            32

        The old method\'s name contained a typo, it is deprecated::

            sage: B.absolut_indicator()
            doctest:warning
            ...
            DeprecationWarning: absolut_indicator is deprecated. Please use absolute_indicator instead.
            See https://github.com/sagemath/sage/issues/28001 for details.
            32'''
    @overload
    def absolute_indicator(self) -> Any:
        '''BooleanFunction.absolute_indicator(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 939)

        Return the absolute indicator of the function.

        The absolute indicator is defined as the maximal absolute value of
        the autocorrelation.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.absolute_indicator()
            32

        The old method\'s name contained a typo, it is deprecated::

            sage: B.absolut_indicator()
            doctest:warning
            ...
            DeprecationWarning: absolut_indicator is deprecated. Please use absolute_indicator instead.
            See https://github.com/sagemath/sage/issues/28001 for details.
            32'''
    @overload
    def absolute_walsh_spectrum(self) -> Any:
        '''BooleanFunction.absolute_walsh_spectrum(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 732)

        Return the absolute Walsh spectrum fo the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: sorted(B.absolute_walsh_spectrum().items())
            [(0, 64), (16, 64)]

            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.absolute_walsh_spectrum()
            {8: 64}'''
    @overload
    def absolute_walsh_spectrum(self) -> Any:
        '''BooleanFunction.absolute_walsh_spectrum(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 732)

        Return the absolute Walsh spectrum fo the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: sorted(B.absolute_walsh_spectrum().items())
            [(0, 64), (16, 64)]

            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.absolute_walsh_spectrum()
            {8: 64}'''
    @overload
    def absolute_walsh_spectrum(self) -> Any:
        '''BooleanFunction.absolute_walsh_spectrum(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 732)

        Return the absolute Walsh spectrum fo the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: sorted(B.absolute_walsh_spectrum().items())
            [(0, 64), (16, 64)]

            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.absolute_walsh_spectrum()
            {8: 64}'''
    @overload
    def algebraic_degree(self) -> Any:
        """BooleanFunction.algebraic_degree(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1099)

        Return the algebraic degree of this Boolean function.

        The algebraic degree of a Boolean function is defined as the degree
        of its algebraic normal form. Note that the degree of the constant
        zero function is defined to be equal to `-1`.

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B.<x0, x1, x2, x3> = BooleanPolynomialRing()
            sage: f = BooleanFunction(x1*x2 + x1*x2*x3 + x1)
            sage: f.algebraic_degree()
            3
            sage: g = BooleanFunction([0, 0])
            sage: g.algebraic_degree()
            -1"""
    @overload
    def algebraic_degree(self) -> Any:
        """BooleanFunction.algebraic_degree(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1099)

        Return the algebraic degree of this Boolean function.

        The algebraic degree of a Boolean function is defined as the degree
        of its algebraic normal form. Note that the degree of the constant
        zero function is defined to be equal to `-1`.

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B.<x0, x1, x2, x3> = BooleanPolynomialRing()
            sage: f = BooleanFunction(x1*x2 + x1*x2*x3 + x1)
            sage: f.algebraic_degree()
            3
            sage: g = BooleanFunction([0, 0])
            sage: g.algebraic_degree()
            -1"""
    @overload
    def algebraic_degree(self) -> Any:
        """BooleanFunction.algebraic_degree(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1099)

        Return the algebraic degree of this Boolean function.

        The algebraic degree of a Boolean function is defined as the degree
        of its algebraic normal form. Note that the degree of the constant
        zero function is defined to be equal to `-1`.

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B.<x0, x1, x2, x3> = BooleanPolynomialRing()
            sage: f = BooleanFunction(x1*x2 + x1*x2*x3 + x1)
            sage: f.algebraic_degree()
            3
            sage: g = BooleanFunction([0, 0])
            sage: g.algebraic_degree()
            -1"""
    @overload
    def algebraic_immunity(self, annihilator=...) -> Any:
        """BooleanFunction.algebraic_immunity(self, annihilator=False)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1056)

        Return the algebraic immunity of the Boolean function.

        This is the smallest integer `i` such that there exists a
        nontrivial annihilator for ``self`` or ``~self``.

        INPUT:

        - ``annihilator`` -- boolean (default: ``False``); if ``True``,
          returns also an annihilator of minimal degree

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x0,x1,x2,x3,x4,x5> = BooleanPolynomialRing(6)
            sage: B = BooleanFunction(x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5)
            sage: B.algebraic_immunity(annihilator=True)
            (2, x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5 + 1)
            sage: B[0] += 1
            sage: B.algebraic_immunity()
            2

            sage: # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            sage: R.<x> = GF(2^8,'a')[]
            sage: B = BooleanFunction(x^31)
            sage: B.algebraic_immunity()
            4"""
    @overload
    def algebraic_immunity(self, annihilator=...) -> Any:
        """BooleanFunction.algebraic_immunity(self, annihilator=False)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1056)

        Return the algebraic immunity of the Boolean function.

        This is the smallest integer `i` such that there exists a
        nontrivial annihilator for ``self`` or ``~self``.

        INPUT:

        - ``annihilator`` -- boolean (default: ``False``); if ``True``,
          returns also an annihilator of minimal degree

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x0,x1,x2,x3,x4,x5> = BooleanPolynomialRing(6)
            sage: B = BooleanFunction(x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5)
            sage: B.algebraic_immunity(annihilator=True)
            (2, x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5 + 1)
            sage: B[0] += 1
            sage: B.algebraic_immunity()
            2

            sage: # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            sage: R.<x> = GF(2^8,'a')[]
            sage: B = BooleanFunction(x^31)
            sage: B.algebraic_immunity()
            4"""
    @overload
    def algebraic_immunity(self) -> Any:
        """BooleanFunction.algebraic_immunity(self, annihilator=False)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1056)

        Return the algebraic immunity of the Boolean function.

        This is the smallest integer `i` such that there exists a
        nontrivial annihilator for ``self`` or ``~self``.

        INPUT:

        - ``annihilator`` -- boolean (default: ``False``); if ``True``,
          returns also an annihilator of minimal degree

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x0,x1,x2,x3,x4,x5> = BooleanPolynomialRing(6)
            sage: B = BooleanFunction(x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5)
            sage: B.algebraic_immunity(annihilator=True)
            (2, x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5 + 1)
            sage: B[0] += 1
            sage: B.algebraic_immunity()
            2

            sage: # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            sage: R.<x> = GF(2^8,'a')[]
            sage: B = BooleanFunction(x^31)
            sage: B.algebraic_immunity()
            4"""
    @overload
    def algebraic_immunity(self) -> Any:
        """BooleanFunction.algebraic_immunity(self, annihilator=False)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1056)

        Return the algebraic immunity of the Boolean function.

        This is the smallest integer `i` such that there exists a
        nontrivial annihilator for ``self`` or ``~self``.

        INPUT:

        - ``annihilator`` -- boolean (default: ``False``); if ``True``,
          returns also an annihilator of minimal degree

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x0,x1,x2,x3,x4,x5> = BooleanPolynomialRing(6)
            sage: B = BooleanFunction(x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5)
            sage: B.algebraic_immunity(annihilator=True)
            (2, x0*x1 + x1*x2 + x2*x3 + x3*x4 + x4*x5 + 1)
            sage: B[0] += 1
            sage: B.algebraic_immunity()
            2

            sage: # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            sage: R.<x> = GF(2^8,'a')[]
            sage: B = BooleanFunction(x^31)
            sage: B.algebraic_immunity()
            4"""
    @overload
    def algebraic_normal_form(self) -> Any:
        """BooleanFunction.algebraic_normal_form(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 491)

        Return the :class:`sage.rings.polynomial.pbori.BooleanPolynomial`
        corresponding to the algebraic normal form.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,1,0,1,0,1,1])
            sage: P = B.algebraic_normal_form(); P                                      # needs sage.rings.polynomial.pbori
            x0*x1*x2 + x0 + x1*x2 + x1 + x2
            sage: [P(*ZZ(i).digits(base=2, padto=3)) for i in range(8)]                 # needs sage.rings.polynomial.pbori
            [0, 1, 1, 0, 1, 0, 1, 1]"""
    @overload
    def algebraic_normal_form(self) -> Any:
        """BooleanFunction.algebraic_normal_form(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 491)

        Return the :class:`sage.rings.polynomial.pbori.BooleanPolynomial`
        corresponding to the algebraic normal form.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,1,0,1,0,1,1])
            sage: P = B.algebraic_normal_form(); P                                      # needs sage.rings.polynomial.pbori
            x0*x1*x2 + x0 + x1*x2 + x1 + x2
            sage: [P(*ZZ(i).digits(base=2, padto=3)) for i in range(8)]                 # needs sage.rings.polynomial.pbori
            [0, 1, 1, 0, 1, 0, 1, 1]"""
    def annihilator(self, d, dim=...) -> Any:
        '''BooleanFunction.annihilator(self, d, dim=False)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 987)

        Return (if it exists) an annihilator of the boolean function of
        degree at most `d`, that is a Boolean polynomial `g` such that

        .. MATH::

            f(x)g(x) = 0 \\forall x.

        INPUT:

        - ``d`` -- integer
        - ``dim`` -- boolean (default: ``False``); if ``True``, return also
          the dimension of the annihilator vector space

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: f = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: f.annihilator(1) is None                                              # needs sage.rings.polynomial.pbori
            True
            sage: g = BooleanFunction(f.annihilator(3))                                 # needs sage.rings.polynomial.pbori
            sage: set(fi*g(i) for i,fi in enumerate(f))                                 # needs sage.rings.polynomial.pbori
            {0}'''
    def autocorrelation(self) -> Any:
        '''BooleanFunction.autocorrelation(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 887)

        Return the autocorrelation of the function, defined by

        .. MATH:: \\Delta_f(j) = \\sum_{i\\in\\{0,1\\}^n} (-1)^{f(i)\\oplus f(i\\oplus j)}.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("03")
            sage: B.autocorrelation()
            (8, 8, 0, 0, 0, 0, 0, 0)'''
    @overload
    def correlation_immunity(self) -> Any:
        '''BooleanFunction.correlation_immunity(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 839)

        Return the maximum value `m` such that the function is
        correlation immune of order `m`.

        A Boolean function is said to be correlation immune of order
        `m` if the output of the function is statistically
        independent of the combination of any `m` of its inputs.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.correlation_immunity()
            2'''
    @overload
    def correlation_immunity(self) -> Any:
        '''BooleanFunction.correlation_immunity(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 839)

        Return the maximum value `m` such that the function is
        correlation immune of order `m`.

        A Boolean function is said to be correlation immune of order
        `m` if the output of the function is statistically
        independent of the combination of any `m` of its inputs.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.correlation_immunity()
            2'''
    def derivative(self, u) -> Any:
        """BooleanFunction.derivative(self, u)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1277)

        Return the derivative in direction of ``u``.

        INPUT:

        - ``u`` -- either an integer or a tuple/list of `\\GF{2}` elements
          of length equal to the number of variables


        The derivative of `f` in direction of `u` is defined as
        `x \\mapsto f(x) + f(x + u)`.

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: f = BooleanFunction([0,1,0,1,0,1,0,1])
            sage: f.derivative(1).algebraic_normal_form()
            1
            sage: u = [1,0,0]
            sage: f.derivative(u).algebraic_normal_form()
            1
            sage: v = vector(GF(2), u)                                                  # needs sage.modules
            sage: f.derivative(v).algebraic_normal_form()                               # needs sage.modules
            1
            sage: f.derivative(8).algebraic_normal_form()
            Traceback (most recent call last):
            ...
            IndexError: index out of bound"""
    def has_linear_structure(self) -> bool:
        """BooleanFunction.has_linear_structure(self) -> bool

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1212)

        Return ``True`` if this function has a linear structure.

        An `n`-variable Boolean function `f` has a linear structure if
        there exists a nonzero `a \\in \\GF{2}^n` such that
        `f(x \\oplus a) \\oplus f(x)` is a constant function.

        .. SEEALSO::

            :meth:`is_linear_structure`,
            :meth:`linear_structures`.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: f = BooleanFunction([0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0])
            sage: f.has_linear_structure()
            True
            sage: f.autocorrelation()
            (16, -16, 0, 0, 0, 0, 0, 0, -16, 16, 0, 0, 0, 0, 0, 0)
            sage: g = BooleanFunction([0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1])
            sage: g.has_linear_structure()
            False
            sage: g.autocorrelation()
            (16, 4, 4, 4, 4, -4, -4, -4, -4, 4, -4, -4, -4, 4, -4, -4)"""
    @overload
    def is_balanced(self) -> Any:
        """BooleanFunction.is_balanced(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 756)

        Return ``True`` if the function takes the value ``True`` half of the time.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(1)
            sage: B.is_balanced()
            False
            sage: B[0] = True
            sage: B.is_balanced()
            True"""
    @overload
    def is_balanced(self) -> Any:
        """BooleanFunction.is_balanced(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 756)

        Return ``True`` if the function takes the value ``True`` half of the time.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(1)
            sage: B.is_balanced()
            False
            sage: B[0] = True
            sage: B.is_balanced()
            True"""
    @overload
    def is_balanced(self) -> Any:
        """BooleanFunction.is_balanced(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 756)

        Return ``True`` if the function takes the value ``True`` half of the time.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(1)
            sage: B.is_balanced()
            False
            sage: B[0] = True
            sage: B.is_balanced()
            True"""
    @overload
    def is_bent(self) -> Any:
        '''BooleanFunction.is_bent(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 824)

        Return ``True`` if the function is bent.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.is_bent()
            True'''
    @overload
    def is_bent(self) -> Any:
        '''BooleanFunction.is_bent(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 824)

        Return ``True`` if the function is bent.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.is_bent()
            True'''
    def is_linear_structure(self, val) -> Any:
        """BooleanFunction.is_linear_structure(self, val)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1141)

        Return ``True`` if ``val`` is a linear structure of this Boolean
        function.

        INPUT:

        - ``val`` -- either an integer or a tuple/list of `\\GF{2}` elements
          of length equal to the number of variables

        .. SEEALSO::

            :meth:`has_linear_structure`,
            :meth:`linear_structures`.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: f = BooleanFunction([0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0])
            sage: f.is_linear_structure(1)
            True
            sage: l = [1, 0, 0, 1]
            sage: f.is_linear_structure(l)
            True
            sage: v = vector(GF(2), l)
            sage: f.is_linear_structure(v)
            True
            sage: f.is_linear_structure(7)
            False
            sage: f.is_linear_structure(20)  # parameter is out of range
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: v = vector(GF(3), [1, 0, 1, 1])
            sage: f.is_linear_structure(v)
            Traceback (most recent call last):
            ...
            TypeError: base ring of input vector must be GF(2)
            sage: v = vector(GF(2), [1, 0, 1, 1, 1])
            sage: f.is_linear_structure(v)
            Traceback (most recent call last):
            ...
            TypeError: input vector must be an element of a vector space with dimension 4
            sage: f.is_linear_structure('X')  # failure case
            Traceback (most recent call last):
            ...
            TypeError: cannot compute is_linear_structure() using parameter X"""
    def is_plateaued(self) -> Any:
        """BooleanFunction.is_plateaued(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1121)

        Return ``True`` if this function is plateaued, i.e. its Walsh transform
        takes at most three values `0` and `\\pm \\lambda`, where `\\lambda` is some
        positive integer.

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x0, x1, x2, x3> = BooleanPolynomialRing()
            sage: f = BooleanFunction(x0*x1 + x2 + x3)
            sage: f.walsh_hadamard_transform()
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, -8)
            sage: f.is_plateaued()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """BooleanFunction.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 772)

        Return ``True`` if the function is symmetric, i.e. invariant under
        permutation of its input bits.

        Another way to see it is that the
        output depends only on the Hamming weight of the input.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[3] = 1
            sage: B.is_symmetric()
            False
            sage: V_B = [0, 1, 1, 0, 1, 0]
            sage: for i in srange(32): B[i] = V_B[i.popcount()]
            sage: B.is_symmetric()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """BooleanFunction.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 772)

        Return ``True`` if the function is symmetric, i.e. invariant under
        permutation of its input bits.

        Another way to see it is that the
        output depends only on the Hamming weight of the input.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[3] = 1
            sage: B.is_symmetric()
            False
            sage: V_B = [0, 1, 1, 0, 1, 0]
            sage: for i in srange(32): B[i] = V_B[i.popcount()]
            sage: B.is_symmetric()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """BooleanFunction.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 772)

        Return ``True`` if the function is symmetric, i.e. invariant under
        permutation of its input bits.

        Another way to see it is that the
        output depends only on the Hamming weight of the input.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[3] = 1
            sage: B.is_symmetric()
            False
            sage: V_B = [0, 1, 1, 0, 1, 0]
            sage: for i in srange(32): B[i] = V_B[i.popcount()]
            sage: B.is_symmetric()
            True"""
    def linear_structures(self) -> Any:
        """BooleanFunction.linear_structures(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1244)

        Return all linear structures of this Boolean function as a
        vector subspace of `\\GF{2}^n`.

        .. SEEALSO::

            :meth:`is_linear_structure`,
            :meth:`has_linear_structure`.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: f = BooleanFunction([0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0])
            sage: LS = f.linear_structures()
            sage: LS.dimension()
            2
            sage: LS.basis_matrix()
            [1 0 0 0]
            [0 0 0 1]
            sage: LS.list()
            [(0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (1, 0, 0, 1)]"""
    @overload
    def nonlinearity(self) -> Any:
        '''BooleanFunction.nonlinearity(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 800)

        Return the nonlinearity of the function.

        This is the distance to the linear functions, or the number of
        output ones need to change to obtain a linear function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[1] = B[3] = 1
            sage: B.nonlinearity()
            2
            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.nonlinearity()
            28'''
    @overload
    def nonlinearity(self) -> Any:
        '''BooleanFunction.nonlinearity(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 800)

        Return the nonlinearity of the function.

        This is the distance to the linear functions, or the number of
        output ones need to change to obtain a linear function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[1] = B[3] = 1
            sage: B.nonlinearity()
            2
            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.nonlinearity()
            28'''
    @overload
    def nonlinearity(self) -> Any:
        '''BooleanFunction.nonlinearity(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 800)

        Return the nonlinearity of the function.

        This is the distance to the linear functions, or the number of
        output ones need to change to obtain a linear function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(5)
            sage: B[1] = B[3] = 1
            sage: B.nonlinearity()
            2
            sage: B = BooleanFunction("0113077C165E76A8")
            sage: B.nonlinearity()
            28'''
    @overload
    def nvariables(self) -> Any:
        """BooleanFunction.nvariables(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 530)

        The number of variables of this function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: BooleanFunction(4).nvariables()
            4"""
    @overload
    def nvariables(self) -> Any:
        """BooleanFunction.nvariables(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 530)

        The number of variables of this function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: BooleanFunction(4).nvariables()
            4"""
    @overload
    def resiliency_order(self) -> Any:
        '''BooleanFunction.resiliency_order(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 866)

        Return the maximum value `m` such that the function is
        resilient of order `m`.

        A Boolean function is said to be resilient of order `m` if it
        is balanced and correlation immune of order `m`.

        If the function is not balanced, we return `-1`.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("077CE5A2F8831A5DF8831A5D077CE5A26996699669699696669999665AA5A55A")
            sage: B.resiliency_order()
            3'''
    @overload
    def resiliency_order(self) -> Any:
        '''BooleanFunction.resiliency_order(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 866)

        Return the maximum value `m` such that the function is
        resilient of order `m`.

        A Boolean function is said to be resilient of order `m` if it
        is balanced and correlation immune of order `m`.

        If the function is not balanced, we return `-1`.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("077CE5A2F8831A5DF8831A5D077CE5A26996699669699696669999665AA5A55A")
            sage: B.resiliency_order()
            3'''
    @overload
    def sum_of_square_indicator(self) -> Any:
        '''BooleanFunction.sum_of_square_indicator(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 970)

        Return the sum of square indicator of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.sum_of_square_indicator()
            32768'''
    @overload
    def sum_of_square_indicator(self) -> Any:
        '''BooleanFunction.sum_of_square_indicator(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 970)

        Return the sum of square indicator of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction("7969817CC5893BA6AC326E47619F5AD0")
            sage: B.sum_of_square_indicator()
            32768'''
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    @overload
    def truth_table(self, format=...) -> Any:
        """BooleanFunction.truth_table(self, format='bin')

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 542)

        The truth table of the Boolean function.

        INPUT:

        - ``format`` -- string representing the desired format; can be either

          - ``'bin'`` -- (default) we return a tuple of Boolean values
          - ``'int'`` -- we return a tuple of 0 or 1 values
          - ``'hex'`` -- we return a string representing the truth table in
            hexadecimal

        EXAMPLES::

            sage: # needs sage.rings.polynomial.pbori
            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x,y,z> = BooleanPolynomialRing(3)
            sage: B = BooleanFunction(x*y*z + z + y + 1)
            sage: B.truth_table()
            (True, True, False, False, False, False, True, False)
            sage: B.truth_table(format='int')
            (1, 1, 0, 0, 0, 0, 1, 0)
            sage: B.truth_table(format='hex')
            '43'

            sage: BooleanFunction('00ab').truth_table(format='hex')                     # needs sage.rings.polynomial.pbori
            '00ab'

            sage: # needs sage.rings.polynomial.pbori
            sage: H = '0abbacadabbacad0'
            sage: len(H)
            16
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: H = H * 4
            sage: T = BooleanFunction(H).truth_table(format='hex')
            sage: T == H
            True
            sage: len(T)
            256
            sage: B.truth_table(format='oct')
            Traceback (most recent call last):
            ...
            ValueError: unknown output format"""
    def walsh_hadamard_transform(self) -> tuple:
        """BooleanFunction.walsh_hadamard_transform(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 702)

        Compute the Walsh Hadamard transform `W` of the function `f`.

        .. MATH:: W(j) = \\sum_{i\\in\\{0,1\\}^n} (-1)^{f(i)\\oplus i \\cdot j}

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: R.<x> = GF(2^3,'a')[]                                                 # needs sage.rings.finite_rings
            sage: B = BooleanFunction(x^3)                                              # needs sage.rings.finite_rings
            sage: B.walsh_hadamard_transform()                                          # needs sage.rings.finite_rings
            (0, -4, 0, 4, 0, 4, 0, 4)"""
    def __add__(self, BooleanFunctionother) -> Any:
        """BooleanFunction.__add__(self, BooleanFunction other)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 382)

        Return the element wise sum of ``self`` and ``other``,
        which must have the same number of variables.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: A = BooleanFunction([0, 1, 0, 1, 1, 0, 0, 1])
            sage: B = BooleanFunction([0, 1, 1, 0, 1, 0, 0, 0])
            sage: (A+B).truth_table(format='int')
            (0, 0, 1, 1, 0, 0, 0, 1)

        it also corresponds to the addition of algebraic normal forms::

            sage: S = A.algebraic_normal_form() + B.algebraic_normal_form()             # needs sage.rings.polynomial.pbori
            sage: (A+B).algebraic_normal_form() == S                                    # needs sage.rings.polynomial.pbori
            True

        TESTS::

            sage: A+BooleanFunction([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables"""
    def __call__(self, x) -> Any:
        """BooleanFunction.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 639)

        Return the value of the function for the given input.

        INPUT:

        - ``x`` -- either:

          - a list: then all elements are evaluated as booleans

          - an integer: then we consider its binary representation

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,0,0])
            sage: B(1)
            1
            sage: B([1,0])
            1
            sage: B(4)
            Traceback (most recent call last):
            ...
            IndexError: index out of bound"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """BooleanFunction.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1348)

        Return the value of the function for the given input.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,1,1])
            sage: [ int(B[i]) for i in range(len(B)) ]
            [0, 1, 1, 1]"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """BooleanFunction.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 367)

        Return the complement Boolean function of ``self``.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0, 1, 1, 0, 1, 0, 0, 0])
            sage: (~B).truth_table(format='int')
            (1, 0, 0, 1, 0, 1, 1, 1)"""
    def __iter__(self) -> Any:
        """BooleanFunction.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 675)

        Iterate through the value of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,1,0,1,0,1,0])
            sage: [int(b) for b in B]
            [0, 1, 1, 0, 1, 0, 1, 0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """BooleanFunction.__len__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 603)

        Return the number of different input values.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: len(BooleanFunction(4))
            16"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, BooleanFunctionother) -> Any:
        """BooleanFunction.__mul__(self, BooleanFunction other)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 414)

        Return the elementwise multiplication of ``self`` and ``other``,
        which must have the same number of variables.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: A = BooleanFunction([0, 1, 0, 1, 1, 0, 0, 1])
            sage: B = BooleanFunction([0, 1, 1, 0, 1, 0, 0, 0])
            sage: (A*B).truth_table(format='int')
            (0, 1, 0, 0, 1, 0, 0, 0)

        it also corresponds to the multiplication of algebraic normal forms::

            sage: P = A.algebraic_normal_form() * B.algebraic_normal_form()             # needs sage.rings.polynomial.pbori
            sage: (A*B).algebraic_normal_form() == P                                    # needs sage.rings.polynomial.pbori
            True

        TESTS::

            sage: A*BooleanFunction([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __or__(self, BooleanFunctionself, BooleanFunctionother) -> Any:
        """BooleanFunction.__or__(BooleanFunction self, BooleanFunction other)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 446)

        Return the concatenation of ``self`` and ``other``,
        which must have the same number of variables.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: A = BooleanFunction([0, 1, 0, 1])
            sage: B = BooleanFunction([0, 1, 1, 0])
            sage: (A|B).truth_table(format='int')
            (0, 1, 0, 1, 0, 1, 1, 0)

            sage: C = A.truth_table() + B.truth_table()
            sage: (A|B).truth_table(format='int') == C
            True

        TESTS::

            sage: A|BooleanFunction([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """BooleanFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1383)

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,1,1,0])
            sage: loads(dumps(B)) == B
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __ror__(self, other):
        """Return value|self."""
    def __setitem__(self, i, y) -> Any:
        """BooleanFunction.__setitem__(self, i, y)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1325)

        Set a value of the function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction([0,0,1,1])
            sage: B[0] = 1
            sage: B[2] = (3**17 == 9)
            sage: [b for b in B]
            [True, False, False, True]

        We take care to clear cached values::

            sage: W = B.walsh_hadamard_transform()
            sage: B[2] = 1
            sage: B._walsh_hadamard_transform_cached() is None
            True"""

class BooleanFunctionIterator:
    """BooleanFunctionIterator(f)"""
    def __init__(self, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1413)

                Iterator through the values of a Boolean function.

                EXAMPLES::

                    sage: from sage.crypto.boolean_function import BooleanFunction
                    sage: B = BooleanFunction(3)
                    sage: type(B.__iter__())
                    <class 'sage.crypto.boolean_function.BooleanFunctionIterator'>
        """
    def __iter__(self) -> Any:
        """BooleanFunctionIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1428)

        Iterator through the values of a Boolean function.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(1)
            sage: [b for b in B]  # indirect doctest
            [False, False]"""
    def __next__(self) -> Any:
        """BooleanFunctionIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/crypto/boolean_function.pyx (starting at line 1441)

        Next value.

        EXAMPLES::

            sage: from sage.crypto.boolean_function import BooleanFunction
            sage: B = BooleanFunction(1)
            sage: I = B.__iter__()
            sage: next(I)
            False"""
