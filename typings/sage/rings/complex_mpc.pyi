import _cython_3_2_1
import cypari2.pari_instance
import sage as sage
import sage.categories.map
import sage.rings.real_mpfr as real_mpfr
import sage.rings.ring
import sage.structure.element
from sage.categories.fields import Fields as Fields
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.complex_mpfr import ComplexField_class as ComplexField_class
from sage.rings.real_mpfr import mpfr_prec_max as mpfr_prec_max, mpfr_prec_min as mpfr_prec_min
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

AA: None
CDF: None
CLF: None
MPComplexField: _cython_3_2_1.cython_function_or_method
QQbar: None
RLF: None
cache: dict
complex_ten: str
digit_ten: str
exponent_ten: str
imaginary_ten: str
late_import: _cython_3_2_1.cython_function_or_method
number_ten: str
pari: cypari2.pari_instance.Pari
sign: str
split_complex_string: _cython_3_2_1.cython_function_or_method

class CCtoMPC(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class INTEGERtoMPC(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class MPComplexField_class(sage.rings.ring.Field):
    """MPComplexField_class(int prec=53, rnd='RNDNN')"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intprec=..., rnd=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 272)

                Initialize ``self``.

                INPUT:

                - ``prec`` -- integer (default: 53); precision

                  prec is the number of bits used to represent the mantissa of
                  both the real and imaginary part of complex floating-point number.

                - ``rnd`` -- string (default: ``'RNDNN'``); the rounding mode

                  Rounding mode is of the form ``'RNDxy'`` where ``x`` and ``y`` are
                  the rounding mode for respectively the real and imaginary parts and
                  are one of:

                  - ``'N'`` for rounding to nearest
                  - ``'Z'`` for rounding towards zero
                  - ``'U'`` for rounding towards plus infinity
                  - ``'D'`` for rounding towards minus infinity

                  For example, ``'RNDZU'`` indicates to round the real part towards
                  zero, and the imaginary part towards plus infinity.

                EXAMPLES::

                    sage: MPComplexField(17)
                    Complex Field with 17 bits of precision
                    sage: MPComplexField()
                    Complex Field with 53 bits of precision
                    sage: MPComplexField(1042,'RNDDZ')
                    Complex Field with 1042 bits of precision and rounding RNDDZ

                ALGORITHMS: Computations are done using the MPC library.

                TESTS::

                    sage: TestSuite(MPComplexField(17)).run()

                    sage: MPComplexField(17).is_finite()
                    False
        """
    @overload
    def characteristic(self) -> Any:
        """MPComplexField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 596)

        Return 0, since the field of complex numbers has characteristic 0.

        EXAMPLES::

            sage: MPComplexField(42).characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """MPComplexField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 596)

        Return 0, since the field of complex numbers has characteristic 0.

        EXAMPLES::

            sage: MPComplexField(42).characteristic()
            0"""
    @overload
    def gen(self, n=...) -> Any:
        """MPComplexField_class.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 527)

        Return the generator of this complex field over its real subfield.

        EXAMPLES::

            sage: MPComplexField(34).gen()
            1.00000000*I"""
    @overload
    def gen(self) -> Any:
        """MPComplexField_class.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 527)

        Return the generator of this complex field over its real subfield.

        EXAMPLES::

            sage: MPComplexField(34).gen()
            1.00000000*I"""
    @overload
    def is_exact(self) -> bool:
        """MPComplexField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 585)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: MPComplexField(42).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """MPComplexField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 585)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: MPComplexField(42).is_exact()
            False"""
    @overload
    def name(self) -> Any:
        """MPComplexField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 607)

        Return the name of the complex field.

        EXAMPLES::

            sage: C = MPComplexField(10, 'RNDNZ'); C.name()
            'MPComplexField10_RNDNZ'"""
    @overload
    def name(self) -> Any:
        """MPComplexField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 607)

        Return the name of the complex field.

        EXAMPLES::

            sage: C = MPComplexField(10, 'RNDNZ'); C.name()
            'MPComplexField10_RNDNZ'"""
    @overload
    def ngens(self) -> Any:
        """MPComplexField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 540)

        Return 1, the number of generators of this complex field over its real
        subfield.

        EXAMPLES::

            sage: MPComplexField(34).ngens()
            1"""
    @overload
    def ngens(self) -> Any:
        """MPComplexField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 540)

        Return 1, the number of generators of this complex field over its real
        subfield.

        EXAMPLES::

            sage: MPComplexField(34).ngens()
            1"""
    @overload
    def prec(self) -> Any:
        """MPComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 630)

        Return the precision of this field of complex numbers.

        EXAMPLES::

            sage: MPComplexField().prec()
            53
            sage: MPComplexField(22).prec()
            22"""
    @overload
    def prec(self) -> Any:
        """MPComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 630)

        Return the precision of this field of complex numbers.

        EXAMPLES::

            sage: MPComplexField().prec()
            53
            sage: MPComplexField(22).prec()
            22"""
    @overload
    def prec(self) -> Any:
        """MPComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 630)

        Return the precision of this field of complex numbers.

        EXAMPLES::

            sage: MPComplexField().prec()
            53
            sage: MPComplexField(22).prec()
            22"""
    @overload
    def random_element(self, min=..., max=...) -> Any:
        """MPComplexField_class.random_element(self, min=0, max=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 564)

        Return a random complex number, uniformly distributed with
        real and imaginary parts between min and max (default 0 to 1).

        EXAMPLES::

            sage: MPComplexField(100).random_element(-5, 10)  # random
            1.9305310520925994224072377281 + 0.94745292506956219710477444855*I
            sage: MPComplexField(10).random_element()  # random
            0.12 + 0.23*I"""
    @overload
    def random_element(self) -> Any:
        """MPComplexField_class.random_element(self, min=0, max=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 564)

        Return a random complex number, uniformly distributed with
        real and imaginary parts between min and max (default 0 to 1).

        EXAMPLES::

            sage: MPComplexField(100).random_element(-5, 10)  # random
            1.9305310520925994224072377281 + 0.94745292506956219710477444855*I
            sage: MPComplexField(10).random_element()  # random
            0.12 + 0.23*I"""
    @overload
    def rounding_mode(self) -> Any:
        """MPComplexField_class.rounding_mode(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 643)

        Return rounding modes used for each part of a complex number.

        EXAMPLES::

            sage: MPComplexField().rounding_mode()
            'RNDNN'
            sage: MPComplexField(rnd='RNDZU').rounding_mode()
            'RNDZU'"""
    @overload
    def rounding_mode(self) -> Any:
        """MPComplexField_class.rounding_mode(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 643)

        Return rounding modes used for each part of a complex number.

        EXAMPLES::

            sage: MPComplexField().rounding_mode()
            'RNDNN'
            sage: MPComplexField(rnd='RNDZU').rounding_mode()
            'RNDZU'"""
    @overload
    def rounding_mode(self) -> Any:
        """MPComplexField_class.rounding_mode(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 643)

        Return rounding modes used for each part of a complex number.

        EXAMPLES::

            sage: MPComplexField().rounding_mode()
            'RNDNN'
            sage: MPComplexField(rnd='RNDZU').rounding_mode()
            'RNDZU'"""
    @overload
    def rounding_mode_imag(self) -> Any:
        """MPComplexField_class.rounding_mode_imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 667)

        Return rounding mode used for the imaginary part of complex number.

        EXAMPLES::

            sage: MPComplexField(rnd='RNDZU').rounding_mode_imag()
            'RNDU'"""
    @overload
    def rounding_mode_imag(self) -> Any:
        """MPComplexField_class.rounding_mode_imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 667)

        Return rounding mode used for the imaginary part of complex number.

        EXAMPLES::

            sage: MPComplexField(rnd='RNDZU').rounding_mode_imag()
            'RNDU'"""
    @overload
    def rounding_mode_real(self) -> Any:
        """MPComplexField_class.rounding_mode_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 656)

        Return rounding mode used for the real part of complex number.

        EXAMPLES::

            sage: MPComplexField(rnd='RNDZU').rounding_mode_real()
            'RNDZ'"""
    @overload
    def rounding_mode_real(self) -> Any:
        """MPComplexField_class.rounding_mode_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 656)

        Return rounding mode used for the real part of complex number.

        EXAMPLES::

            sage: MPComplexField(rnd='RNDZU').rounding_mode_real()
            'RNDZ'"""
    def __call__(self, x, im=...) -> Any:
        """MPComplexField_class.__call__(self, x, im=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 373)

        Create a floating-point complex using ``x`` and optionally an imaginary
        part ``im``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: MPC(2) # indirect doctest
            2.00000000000000
            sage: MPC(0, 1) # indirect doctest
            1.00000000000000*I
            sage: MPC(1, 1)
            1.00000000000000 + 1.00000000000000*I
            sage: MPC(2, 3)
            2.00000000000000 + 3.00000000000000*I"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """MPComplexField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 618)

        Return the hash of ``self``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: hash(MPC) % 2^32 == hash(MPC.name()) % 2^32
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """MPComplexField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 492)

        For pickling.

        EXAMPLES::

            sage: C = MPComplexField(prec=200, rnd='RNDDZ')
            sage: loads(dumps(C)) == C
            True"""

class MPComplexNumber(sage.structure.element.FieldElement):
    """MPComplexNumber(MPComplexField_class parent, x, y=None, int base=10)

    File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 707)

    A floating point approximation to a complex number using any specified
    precision common to both real and imaginary part."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, MPComplexField_classparent, x, y=..., intbase=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 723)

                Create a complex number.

                INPUT:

                - ``x`` -- real part or the complex value in a string

                - ``y`` -- imaginary part

                - ``base`` -- when ``x`` or ``y`` is a string, base in which the
                  number is written

                A :class:`MPComplexNumber` should be called by first creating a
                :class:`MPComplexField`, as illustrated in the examples.

                EXAMPLES::

                    sage: C200 = MPComplexField(200)
                    sage: C200(1/3, \'0.6789\')
                    0.33333333333333333333333333333333333333333333333333333333333 + 0.67890000000000000000000000000000000000000000000000000000000*I
                    sage: C3 = MPComplexField(3)
                    sage: C3(\'1.2345\', \'0.6789\')
                    1.2 + 0.62*I
                    sage: C3(3.14159)
                    3.0

                Rounding modes::

                    sage: w = C3(5/2, 7/2); w.str(2)
                    \'10.1 + 11.1*I\'
                    sage: MPComplexField(2, rnd="RNDZN")(w).str(2)
                    \'10. + 100.*I\'
                    sage: MPComplexField(2, rnd="RNDDU")(w).str(2)
                    \'10. + 100.*I\'
                    sage: MPComplexField(2, rnd="RNDUD")(w).str(2)
                    \'11. + 11.*I\'
                    sage: MPComplexField(2, rnd="RNDNZ")(w).str(2)
                    \'10. + 11.*I\'

                TESTS::

                    sage: MPComplexField(42)._repr_option(\'element_is_atomic\')
                    False
        '''
    @overload
    def agm(self, right, algorithm=...) -> Any:
        """MPComplexNumber.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2314)

        Return the algebro-geometric mean of ``self`` and ``right``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(1, 4)
            sage: v = MPC(-2,5)
            sage: u.agm(v, algorithm='pari')
            -0.410522769709397 + 4.60061063922097*I
            sage: u.agm(v, algorithm='principal')
            1.24010691168158 - 0.472193567796433*I
            sage: u.agm(v, algorithm='optimal')
            -0.410522769709397 + 4.60061063922097*I"""
    @overload
    def agm(self, v, algorithm=...) -> Any:
        """MPComplexNumber.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2314)

        Return the algebro-geometric mean of ``self`` and ``right``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(1, 4)
            sage: v = MPC(-2,5)
            sage: u.agm(v, algorithm='pari')
            -0.410522769709397 + 4.60061063922097*I
            sage: u.agm(v, algorithm='principal')
            1.24010691168158 - 0.472193567796433*I
            sage: u.agm(v, algorithm='optimal')
            -0.410522769709397 + 4.60061063922097*I"""
    @overload
    def agm(self, v, algorithm=...) -> Any:
        """MPComplexNumber.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2314)

        Return the algebro-geometric mean of ``self`` and ``right``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(1, 4)
            sage: v = MPC(-2,5)
            sage: u.agm(v, algorithm='pari')
            -0.410522769709397 + 4.60061063922097*I
            sage: u.agm(v, algorithm='principal')
            1.24010691168158 - 0.472193567796433*I
            sage: u.agm(v, algorithm='optimal')
            -0.410522769709397 + 4.60061063922097*I"""
    @overload
    def agm(self, v, algorithm=...) -> Any:
        """MPComplexNumber.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2314)

        Return the algebro-geometric mean of ``self`` and ``right``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(1, 4)
            sage: v = MPC(-2,5)
            sage: u.agm(v, algorithm='pari')
            -0.410522769709397 + 4.60061063922097*I
            sage: u.agm(v, algorithm='principal')
            1.24010691168158 - 0.472193567796433*I
            sage: u.agm(v, algorithm='optimal')
            -0.410522769709397 + 4.60061063922097*I"""
    def algdep(self, *args, **kwargs):
        """MPComplexNumber.algebraic_dependency(self, n, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1361)

        Return an irreducible polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT: Type ``algebraic_dependency?`` at the top level prompt.

        All additional parameters are passed onto the top-level
        ``algebraic_dependency`` command.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: z = (1/2)*(1 + sqrt(3.0) * MPC.0); z
            0.500000000000000 + 0.866025403784439*I
            sage: p = z.algebraic_dependency(5)
            sage: p
            x^2 - x + 1
            sage: p(z)
            1.11022302462516e-16"""
    def algebraic_dependency(self, n, **kwds) -> Any:
        """MPComplexNumber.algebraic_dependency(self, n, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1361)

        Return an irreducible polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT: Type ``algebraic_dependency?`` at the top level prompt.

        All additional parameters are passed onto the top-level
        ``algebraic_dependency`` command.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: z = (1/2)*(1 + sqrt(3.0) * MPC.0); z
            0.500000000000000 + 0.866025403784439*I
            sage: p = z.algebraic_dependency(5)
            sage: p
            x^2 - x + 1
            sage: p(z)
            1.11022302462516e-16"""
    @overload
    def arccos(self) -> Any:
        """MPComplexNumber.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1755)

        Return the arccosine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arccos(u)
            1.11692611683177 - 2.19857302792094*I"""
    @overload
    def arccos(self, u) -> Any:
        """MPComplexNumber.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1755)

        Return the arccosine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arccos(u)
            1.11692611683177 - 2.19857302792094*I"""
    @overload
    def arccosh(self) -> Any:
        """MPComplexNumber.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1803)

        Return the hyperbolic arccos of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arccosh(u)
            2.19857302792094 + 1.11692611683177*I"""
    @overload
    def arccosh(self, u) -> Any:
        """MPComplexNumber.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1803)

        Return the hyperbolic arccos of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arccosh(u)
            2.19857302792094 + 1.11692611683177*I"""
    @overload
    def arccoth(self) -> Any:
        """MPComplexNumber.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1863)

        Return the hyperbolic arccotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arccoth()
            0.40235947810852509365018983331 - 0.55357435889704525150853273009*I"""
    @overload
    def arccoth(self) -> Any:
        """MPComplexNumber.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1863)

        Return the hyperbolic arccotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arccoth()
            0.40235947810852509365018983331 - 0.55357435889704525150853273009*I"""
    @overload
    def arccsch(self) -> Any:
        """MPComplexNumber.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1899)

        Return the hyperbolic arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arccsch()
            0.53063753095251782601650945811 - 0.45227844715119068206365839783*I"""
    @overload
    def arccsch(self) -> Any:
        """MPComplexNumber.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1899)

        Return the hyperbolic arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arccsch()
            0.53063753095251782601650945811 - 0.45227844715119068206365839783*I"""
    @overload
    def arcsech(self) -> Any:
        """MPComplexNumber.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1935)

        Return the hyperbolic arcsecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arcsech()
            0.53063753095251782601650945811 - 1.1185178796437059371676632938*I"""
    @overload
    def arcsech(self) -> Any:
        """MPComplexNumber.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1935)

        Return the hyperbolic arcsecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).arcsech()
            0.53063753095251782601650945811 - 1.1185178796437059371676632938*I"""
    @overload
    def arcsin(self) -> Any:
        """MPComplexNumber.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1771)

        Return the arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arcsin(u)
            0.453870209963122 + 2.19857302792094*I"""
    @overload
    def arcsin(self, u) -> Any:
        """MPComplexNumber.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1771)

        Return the arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arcsin(u)
            0.453870209963122 + 2.19857302792094*I"""
    @overload
    def arcsinh(self) -> Any:
        """MPComplexNumber.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1819)

        Return the hyperbolic arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arcsinh(u)
            2.18358521656456 + 1.09692154883014*I"""
    @overload
    def arcsinh(self, u) -> Any:
        """MPComplexNumber.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1819)

        Return the hyperbolic arcsine of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arcsinh(u)
            2.18358521656456 + 1.09692154883014*I"""
    @overload
    def arctan(self) -> Any:
        """MPComplexNumber.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1787)

        Return the arctangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(-2, 4)
            sage: arctan(u)
            -1.46704821357730 + 0.200586618131234*I"""
    @overload
    def arctan(self, u) -> Any:
        """MPComplexNumber.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1787)

        Return the arctangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(-2, 4)
            sage: arctan(u)
            -1.46704821357730 + 0.200586618131234*I"""
    @overload
    def arctanh(self) -> Any:
        """MPComplexNumber.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1835)

        Return the hyperbolic arctangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arctanh(u)
            0.0964156202029962 + 1.37153510396169*I"""
    @overload
    def arctanh(self, u) -> Any:
        """MPComplexNumber.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1835)

        Return the hyperbolic arctangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: arctanh(u)
            0.0964156202029962 + 1.37153510396169*I"""
    @overload
    def argument(self) -> Any:
        """MPComplexNumber.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1969)

        The argument (angle) of the complex number, normalized so that
        `-\\pi < \\theta \\leq \\pi`.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: i = MPC.0
            sage: (i^2).argument()
            3.14159265358979
            sage: (1+i).argument()
            0.785398163397448
            sage: i.argument()
            1.57079632679490
            sage: (-i).argument()
            -1.57079632679490
            sage: (RR('-0.001') - i).argument()
            -1.57179632646156"""
    @overload
    def argument(self, angle) -> Any:
        """MPComplexNumber.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1969)

        The argument (angle) of the complex number, normalized so that
        `-\\pi < \\theta \\leq \\pi`.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: i = MPC.0
            sage: (i^2).argument()
            3.14159265358979
            sage: (1+i).argument()
            0.785398163397448
            sage: i.argument()
            1.57079632679490
            sage: (-i).argument()
            -1.57079632679490
            sage: (RR('-0.001') - i).argument()
            -1.57179632646156"""
    def conjugate(self) -> Any:
        """MPComplexNumber.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1994)

        Return the complex conjugate of this complex number:

        .. MATH::

            \\mathrm{conjugate}(a + ib) = a - ib.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: i = MPC(0, 1)
            sage: (1+i).conjugate()
            1.00000000000000 - 1.00000000000000*I"""
    def cos(self) -> Any:
        """MPComplexNumber.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1635)

        Return the cosine of this complex number:

        .. MATH::

            \\cos(a + ib) = \\cos a \\cosh b -i \\sin a \\sinh b.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: cos(u)
            -11.3642347064011 - 24.8146514856342*I"""
    def cosh(self) -> Any:
        """MPComplexNumber.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1695)

        Return the hyperbolic cosine of this complex number:

        .. MATH::

            \\cosh(a + ib) = \\cosh a \\cos b + i \\sinh a \\sin b.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: cosh(u)
            -2.45913521391738 - 2.74481700679215*I"""
    @overload
    def cot(self) -> Any:
        """MPComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1947)

        Return the cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(53)
            sage: (1+MPC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = MPComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = MPComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I"""
    @overload
    def cot(self) -> Any:
        """MPComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1947)

        Return the cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(53)
            sage: (1+MPC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = MPComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = MPComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I"""
    @overload
    def cot(self) -> Any:
        """MPComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1947)

        Return the cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(53)
            sage: (1+MPC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = MPComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = MPComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I"""
    @overload
    def cot(self) -> Any:
        """MPComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1947)

        Return the cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(53)
            sage: (1+MPC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = MPComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = MPComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I"""
    @overload
    def coth(self) -> Any:
        """MPComplexNumber.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1851)

        Return the hyperbolic cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).coth()
            0.86801414289592494863584920892 - 0.21762156185440268136513424361*I"""
    @overload
    def coth(self) -> Any:
        """MPComplexNumber.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1851)

        Return the hyperbolic cotangent of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).coth()
            0.86801414289592494863584920892 - 0.21762156185440268136513424361*I"""
    @overload
    def csc(self) -> Any:
        """MPComplexNumber.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1875)

        Return the cosecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).csc()
            0.62151801717042842123490780586 - 0.30393100162842645033448560451*I"""
    @overload
    def csc(self) -> Any:
        """MPComplexNumber.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1875)

        Return the cosecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).csc()
            0.62151801717042842123490780586 - 0.30393100162842645033448560451*I"""
    @overload
    def csch(self) -> Any:
        """MPComplexNumber.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1887)

        Return the hyperbolic cosecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).csch()
            0.30393100162842645033448560451 - 0.62151801717042842123490780586*I"""
    @overload
    def csch(self) -> Any:
        """MPComplexNumber.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1887)

        Return the hyperbolic cosecant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).csch()
            0.30393100162842645033448560451 - 0.62151801717042842123490780586*I"""
    def dilog(self) -> Any:
        """MPComplexNumber.dilog(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2187)

        Return the complex dilogarithm of ``self``.

        The complex dilogarithm, or Spence's function, is defined by

        .. MATH::

            Li_2(z) = - \\int_0^z \\frac{\\log|1-\\zeta|}{\\zeta} d(\\zeta)
            = \\sum_{k=1}^\\infty \\frac{z^k}{k^2}.

        Note that the series definition can only be used for `|z| < 1`.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(1,0)
            sage: a.dilog()
            1.64493406684823
            sage: float(pi^2/6)                                                         # needs sage.symbolic
            1.6449340668482262

        ::

            sage: b = MPC(0,1)
            sage: b.dilog()
            -0.205616758356028 + 0.915965594177219*I

        ::

            sage: c = MPC(0,0)
            sage: c.dilog()
            0"""
    def eta(self, omit_frac=...) -> Any:
        """MPComplexNumber.eta(self, omit_frac=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2223)

        Return the value of the Dedekind `\\eta` function on ``self``,
        intelligently computed using `\\mathbb{SL}(2,\\ZZ)` transformations.

        The `\\eta` function is

        .. MATH::

            \\eta(z) = e^{\\pi i z / 12} \\prod_{n=1}^{\\infty}(1-e^{2\\pi inz})

        INPUT:

        - ``self`` -- element of the upper half plane (if not,
          raises a :exc:`ValueError`)

        - ``omit_frac`` -- -- boolean (default: ``False``); if ``True``,
          omit the `e^{\\pi i z / 12}` factor

        OUTPUT: a complex number

        ALGORITHM: Uses the PARI C library.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: i = MPC.0
            sage: z = 1+i; z.eta()
            0.742048775836565 + 0.198831370229911*I"""
    def exp(self) -> Any:
        """MPComplexNumber.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2055)

        Return the exponential of this complex number:

        .. MATH::

            \\exp(a + ib) = \\exp(a) (\\cos b + i \\sin b).

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: exp(u)
            -4.82980938326939 - 5.59205609364098*I"""
    @overload
    def gamma(self) -> Any:
        """MPComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2258)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(30)
            sage: i = MPC.0
            sage: (1+i).gamma()
            0.49801567 - 0.15494983*I

        TESTS::

            sage: MPC(0).gamma()
            Infinity

        ::

            sage: MPC(-1).gamma()
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """MPComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2258)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(30)
            sage: i = MPC.0
            sage: (1+i).gamma()
            0.49801567 - 0.15494983*I

        TESTS::

            sage: MPC(0).gamma()
            Infinity

        ::

            sage: MPC(-1).gamma()
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """MPComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2258)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(30)
            sage: i = MPC.0
            sage: (1+i).gamma()
            0.49801567 - 0.15494983*I

        TESTS::

            sage: MPC(0).gamma()
            Infinity

        ::

            sage: MPC(-1).gamma()
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """MPComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2258)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(30)
            sage: i = MPC.0
            sage: (1+i).gamma()
            0.49801567 - 0.15494983*I

        TESTS::

            sage: MPC(0).gamma()
            Infinity

        ::

            sage: MPC(-1).gamma()
            Infinity"""
    def gamma_inc(self, t) -> Any:
        """MPComplexNumber.gamma_inc(self, t)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2285)

        Return the incomplete Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: C, i = MPComplexField(30).objgen()
            sage: (1+i).gamma_inc(2 + 3*i)  # abs tol 2e-10
            0.0020969149 - 0.059981914*I
            sage: (1+i).gamma_inc(5)
            -0.0013781309 + 0.0065198200*I
            sage: C(2).gamma_inc(1 + i)
            0.70709210 - 0.42035364*I"""
    @overload
    def imag(self) -> Any:
        """MPComplexNumber.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1042)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: C = MPComplexField(100)
            sage: z = C(2, 3)
            sage: x = z.imag(); x
            3.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision"""
    @overload
    def imag(self) -> Any:
        """MPComplexNumber.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1042)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: C = MPComplexField(100)
            sage: z = C(2, 3)
            sage: x = z.imag(); x
            3.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision"""
    @overload
    def is_imaginary(self) -> Any:
        """MPComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1347)

        Return ``True`` if ``self`` is imaginary, i.e. has real part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23*i).is_imaginary()
            True
            sage: C200(1+i).is_imaginary()
            False"""
    @overload
    def is_imaginary(self) -> Any:
        """MPComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1347)

        Return ``True`` if ``self`` is imaginary, i.e. has real part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23*i).is_imaginary()
            True
            sage: C200(1+i).is_imaginary()
            False"""
    @overload
    def is_imaginary(self) -> Any:
        """MPComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1347)

        Return ``True`` if ``self`` is imaginary, i.e. has real part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23*i).is_imaginary()
            True
            sage: C200(1+i).is_imaginary()
            False"""
    @overload
    def is_real(self) -> Any:
        """MPComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1333)

        Return ``True`` if ``self`` is real, i.e. has imaginary part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23).is_real()
            True
            sage: C200(1+i).is_real()
            False"""
    @overload
    def is_real(self) -> Any:
        """MPComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1333)

        Return ``True`` if ``self`` is real, i.e. has imaginary part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23).is_real()
            True
            sage: C200(1+i).is_real()
            False"""
    @overload
    def is_real(self) -> Any:
        """MPComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1333)

        Return ``True`` if ``self`` is real, i.e. has imaginary part zero.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: C200(1.23).is_real()
            True
            sage: C200(1+i).is_real()
            False"""
    def is_square(self) -> Any:
        """MPComplexNumber.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1314)

        This function always returns true as `\\CC` is algebraically closed.

        EXAMPLES::

            sage: C200 = MPComplexField(200)
            sage: a = C200(2,1)
            sage: a.is_square()
            True

        `\\CC` is algebraically closed, hence every element is a square::

            sage: b = C200(5)
            sage: b.is_square()
            True"""
    def log(self) -> Any:
        """MPComplexNumber.log(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2075)

        Return the logarithm of this complex number with the branch
        cut on the negative real axis:

        .. MATH::

            \\log(z) = \\log |z| + i \\arg(z).

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: log(u)
            1.49786613677700 + 1.10714871779409*I"""
    def norm(self) -> Any:
        """MPComplexNumber.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1552)

        Return the norm of a complex number, rounded with the rounding
        mode of the real part.  The norm is the square of the absolute
        value:

        .. MATH::

            \\mathrm{norm}(a + ib) = a^2 + b^2.

        OUTPUT:

        A floating-point number in the real field of the real part
        (same precision, same rounding mode).

        EXAMPLES:

        This indeed acts as the square function when the imaginary
        component of ``self`` is equal to zero::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.norm()
            5.00000000000000
            sage: b = MPC(4.2,0)
            sage: b.norm()
            17.6400000000000
            sage: b^2
            17.6400000000000"""
    def nth_root(self, n, all=...) -> Any:
        """MPComplexNumber.nth_root(self, n, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2134)

        The `n`-th root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all `n`-th roots

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(27)
            sage: a.nth_root(3)
            3.00000000000000
            sage: a.nth_root(3, all=True)
            [3.00000000000000, -1.50000000000000 + 2.59807621135332*I, -1.50000000000000 - 2.59807621135332*I]"""
    @overload
    def prec(self) -> Any:
        """MPComplexNumber.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1012)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = MPComplexField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def prec(self) -> Any:
        """MPComplexNumber.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1012)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = MPComplexField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def real(self) -> Any:
        """MPComplexNumber.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1024)

        Return the real part of ``self``.

        EXAMPLES::

            sage: C = MPComplexField(100)
            sage: z = C(2, 3)
            sage: x = z.real(); x
            2.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision"""
    @overload
    def real(self) -> Any:
        """MPComplexNumber.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1024)

        Return the real part of ``self``.

        EXAMPLES::

            sage: C = MPComplexField(100)
            sage: z = C(2, 3)
            sage: x = z.real(); x
            2.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision"""
    @overload
    def sec(self) -> Any:
        """MPComplexNumber.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1911)

        Return the secant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).sec()
            0.49833703055518678521380589177 + 0.59108384172104504805039169297*I"""
    @overload
    def sec(self) -> Any:
        """MPComplexNumber.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1911)

        Return the secant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).sec()
            0.49833703055518678521380589177 + 0.59108384172104504805039169297*I"""
    @overload
    def sech(self) -> Any:
        """MPComplexNumber.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1923)

        Return the hyperbolic secant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).sech()
            0.49833703055518678521380589177 - 0.59108384172104504805039169297*I"""
    @overload
    def sech(self) -> Any:
        """MPComplexNumber.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1923)

        Return the hyperbolic secant of this complex number.

        EXAMPLES::

            sage: MPC = MPComplexField(100)
            sage: MPC(1,1).sech()
            0.49833703055518678521380589177 - 0.59108384172104504805039169297*I"""
    def sin(self) -> Any:
        """MPComplexNumber.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1655)

        Return the sine of this complex number:

        .. MATH::

            \\sin(a + ib) = \\sin a \\cosh b + i \\cos x \\sinh b.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: sin(u)
            24.8313058489464 - 11.3566127112182*I"""
    def sinh(self) -> Any:
        """MPComplexNumber.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1715)

        Return the hyperbolic sine of this complex number:

        .. MATH::

            \\sinh(a + ib) = \\sinh a \\cos b + i \\cosh a \\sin b.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: sinh(u)
            -2.37067416935200 - 2.84723908684883*I"""
    @overload
    def sqr(self) -> Any:
        """MPComplexNumber.sqr(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2014)

        Return the square of a complex number:

        .. MATH::

            (a + ib)^2 = (a^2 - b^2) + 2iab.

        EXAMPLES::

            sage: C = MPComplexField()
            sage: a = C(5, 1)
            sage: a.sqr()
            24.0000000000000 + 10.0000000000000*I"""
    @overload
    def sqr(self) -> Any:
        """MPComplexNumber.sqr(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2014)

        Return the square of a complex number:

        .. MATH::

            (a + ib)^2 = (a^2 - b^2) + 2iab.

        EXAMPLES::

            sage: C = MPComplexField()
            sage: a = C(5, 1)
            sage: a.sqr()
            24.0000000000000 + 10.0000000000000*I"""
    def sqrt(self) -> Any:
        """MPComplexNumber.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2034)

        Return the square root, taking the branch cut to be the negative real
        axis:

        .. MATH::

            \\sqrt z = \\sqrt{|z|}(\\cos(\\arg(z)/2) + i \\sin(\\arg(z)/2)).

        EXAMPLES::

            sage: C = MPComplexField()
            sage: a = C(24, 10)
            sage: a.sqrt()
            5.00000000000000 + 1.00000000000000*I"""
    @overload
    def str(self, base=..., **kwds) -> Any:
        """MPComplexNumber.str(self, base=10, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1060)

        Return a string of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: MPC = MPComplexField(64)
            sage: z = MPC(-4, 3)/7
            sage: z.str()
            '-0.571428571428571428564 + 0.428571428571428571436*I'
            sage: z.str(16)
            '-0.92492492492492490 + 0.6db6db6db6db6db70*I'
            sage: z.str(truncate=True)
            '-0.571428571428571429 + 0.428571428571428571*I'
            sage: z.str(2)
            '-0.1001001001001001001001001001001001001001001001001001001001001001 + 0.01101101101101101101101101101101101101101101101101101101101101110*I'"""
    @overload
    def str(self) -> Any:
        """MPComplexNumber.str(self, base=10, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1060)

        Return a string of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: MPC = MPComplexField(64)
            sage: z = MPC(-4, 3)/7
            sage: z.str()
            '-0.571428571428571428564 + 0.428571428571428571436*I'
            sage: z.str(16)
            '-0.92492492492492490 + 0.6db6db6db6db6db70*I'
            sage: z.str(truncate=True)
            '-0.571428571428571429 + 0.428571428571428571*I'
            sage: z.str(2)
            '-0.1001001001001001001001001001001001001001001001001001001001001001 + 0.01101101101101101101101101101101101101101101101101101101101101110*I'"""
    @overload
    def str(self) -> Any:
        """MPComplexNumber.str(self, base=10, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1060)

        Return a string of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: MPC = MPComplexField(64)
            sage: z = MPC(-4, 3)/7
            sage: z.str()
            '-0.571428571428571428564 + 0.428571428571428571436*I'
            sage: z.str(16)
            '-0.92492492492492490 + 0.6db6db6db6db6db70*I'
            sage: z.str(truncate=True)
            '-0.571428571428571429 + 0.428571428571428571*I'
            sage: z.str(2)
            '-0.1001001001001001001001001001001001001001001001001001001001001001 + 0.01101101101101101101101101101101101101101101101101101101101101110*I'"""
    @overload
    def str(self, truncate=...) -> Any:
        """MPComplexNumber.str(self, base=10, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1060)

        Return a string of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: MPC = MPComplexField(64)
            sage: z = MPC(-4, 3)/7
            sage: z.str()
            '-0.571428571428571428564 + 0.428571428571428571436*I'
            sage: z.str(16)
            '-0.92492492492492490 + 0.6db6db6db6db6db70*I'
            sage: z.str(truncate=True)
            '-0.571428571428571429 + 0.428571428571428571*I'
            sage: z.str(2)
            '-0.1001001001001001001001001001001001001001001001001001001001001001 + 0.01101101101101101101101101101101101101101101101101101101101101110*I'"""
    def tan(self) -> Any:
        """MPComplexNumber.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1675)

        Return the tangent of this complex number:

        .. MATH::

            \\tan(a + ib) = (\\sin 2a + i \\sinh 2b)/(\\cos 2a + \\cosh 2b).

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(-2, 4)
            sage: tan(u)
            0.000507980623470039 + 1.00043851320205*I"""
    def tanh(self) -> Any:
        """MPComplexNumber.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1735)

        Return the hyperbolic tangent of this complex number:

        .. MATH::

            \\tanh(a + ib) = (\\sinh 2a + i \\sin 2b)/(\\cosh 2a + \\cos 2b).

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: tanh(u)
            1.00468231219024 + 0.0364233692474037*I"""
    @overload
    def zeta(self) -> Any:
        """MPComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2301)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = MPComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()
            0.58215806 - 0.92684856*I"""
    @overload
    def zeta(self) -> Any:
        """MPComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2301)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = MPComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()
            0.58215806 - 0.92684856*I"""
    def __abs__(self) -> Any:
        """MPComplexNumber.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1511)

        Absolute value or modulus of this complex number,
        rounded with the rounding mode of the real part:

        .. MATH::

            |a + ib| = \\sqrt(a^2 + b^2).

        OUTPUT:

        A floating-point number in the real field of the real part
        (same precision, same rounding mode).

        EXAMPLES:

        Note that the absolute value of a complex number with imaginary
        component equal to zero is the absolute value of the real component::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: abs(a)
            2.23606797749979
            sage: a.__abs__()
            2.23606797749979
            sage: float(sqrt(2^2 + 1^1))                                                # needs sage.symbolic
            2.23606797749979

            sage: b = MPC(42,0)
            sage: abs(b)
            42.0000000000000
            sage: b.__abs__()
            42.0000000000000
            sage: b
            42.0000000000000"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __complex__(self) -> Any:
        """MPComplexNumber.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1174)

        Method for converting ``self`` to type ``complex``.

        Called by the ``complex`` function.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: complex(a)
            (2+1j)
            sage: type(complex(a))
            <... 'complex'>
            sage: a.__complex__()
            (2+1j)"""
    @overload
    def __complex__(self) -> Any:
        """MPComplexNumber.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1174)

        Method for converting ``self`` to type ``complex``.

        Called by the ``complex`` function.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: complex(a)
            (2+1j)
            sage: type(complex(a))
            <... 'complex'>
            sage: a.__complex__()
            (2+1j)"""
    def __copy__(self) -> Any:
        """MPComplexNumber.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1098)

        Return copy of ``self``.

        Since ``self`` is immutable, we just return ``self`` again.

        EXAMPLES::

            sage: a = MPComplexField()(3.5, 3)
            sage: copy(a) is  a
            True"""
    def __deepcopy__(self, memo) -> Any:
        """MPComplexNumber.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1112)

        EXAMPLES::

            sage: a = MPComplexField()(3.5, 3)
            sage: deepcopy(a) is  a
            True"""
    @overload
    def __float__(self) -> Any:
        """MPComplexNumber.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1145)

        Method for converting ``self`` to type ``float``.

        Called by the ``float`` function. Note that calling this method returns
        an error since if the imaginary part of the number is not zero.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(1, 0)
            sage: float(a)
            1.0
            sage: a = MPC(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to float; use abs(z)
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to float; use abs(z)"""
    @overload
    def __float__(self) -> Any:
        """MPComplexNumber.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1145)

        Method for converting ``self`` to type ``float``.

        Called by the ``float`` function. Note that calling this method returns
        an error since if the imaginary part of the number is not zero.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(1, 0)
            sage: float(a)
            1.0
            sage: a = MPC(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to float; use abs(z)
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to float; use abs(z)"""
    def __getitem__(self, i) -> Any:
        """MPComplexNumber.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 977)

        Return either the real or imaginary component of ``self``
        depending on the choice of ``i``: real (``i``=0), imaginary (``i``=1).

        INPUT:

        - ``i`` -- 0 or 1

          - ``0`` -- will return the real component of ``self``
          - ``1`` -- will return the imaginary component of ``self``

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.__getitem__(0)
            2.00000000000000
            sage: a.__getitem__(1)
            1.00000000000000

        ::

            sage: b = MPC(42,0)
            sage: b
            42.0000000000000
            sage: b.__getitem__(1)
            0.000000000000000"""
    def __hash__(self) -> Any:
        """MPComplexNumber.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 961)

        Return the hash of ``self``, which coincides with the python
        complex and float (and often int) types.

        This has the drawback that two very close high precision
        numbers will have the same hash, but allows them to play
        nicely with other real types.

        EXAMPLES::

            sage: hash(MPComplexField()('1.2', 33)) == hash(complex(1.2, 33))
            True"""
    @overload
    def __int__(self) -> Any:
        """MPComplexNumber.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1122)

        Method for converting ``self`` to type ``int``.

        Called by the ``int`` function. Note that calling this method returns
        an error since, in general, complex numbers cannot be coerced into
        integers.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))
            sage: a.__int__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))"""
    @overload
    def __int__(self) -> Any:
        """MPComplexNumber.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1122)

        Method for converting ``self`` to type ``int``.

        Called by the ``int`` function. Note that calling this method returns
        an error since, in general, complex numbers cannot be coerced into
        integers.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))
            sage: a.__int__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))"""
    def __invert__(self) -> Any:
        """MPComplexNumber.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1474)

        Return the multiplicative inverse.

        EXAMPLES::

            sage: C = MPComplexField()
            sage: a = ~C(5, 1)
            sage: a * C(5, 1)
            1.00000000000000"""
    def __lshift__(self, n) -> Any:
        """MPComplexNumber.__lshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2096)

        Fast multiplication by `2^n`.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: u<<2
            8.00000000000000 + 16.0000000000000*I
            sage: u<<(-1)
            1.00000000000000 + 2.00000000000000*I"""
    @overload
    def __mpc__(self) -> Any:
        """MPComplexNumber.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1239)

        Convert Sage ``MPComplexNumber`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: c = MPC(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')
            sage: MPCF = MPComplexField(42)
            sage: mpc(MPCF(12, 12)).precision
            (42, 42)
            sage: MPCF = MPComplexField(236)
            sage: mpc(MPCF(12, 12)).precision
            (236, 236)
            sage: MPCF = MPComplexField(63)
            sage: x = MPCF('15.64E+128', '15.64E+128')
            sage: y = mpc(x)
            sage: y.precision
            (63, 63)
            sage: MPCF(y) == x
            True
            sage: x = mpc('1.324+4e50j', precision=(70,70))
            sage: y = MPComplexField(70)(x)
            sage: mpc(y) == x
            True"""
    @overload
    def __mpc__(self) -> Any:
        """MPComplexNumber.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1239)

        Convert Sage ``MPComplexNumber`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: c = MPC(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')
            sage: MPCF = MPComplexField(42)
            sage: mpc(MPCF(12, 12)).precision
            (42, 42)
            sage: MPCF = MPComplexField(236)
            sage: mpc(MPCF(12, 12)).precision
            (236, 236)
            sage: MPCF = MPComplexField(63)
            sage: x = MPCF('15.64E+128', '15.64E+128')
            sage: y = mpc(x)
            sage: y.precision
            (63, 63)
            sage: MPCF(y) == x
            True
            sage: x = mpc('1.324+4e50j', precision=(70,70))
            sage: y = MPComplexField(70)(x)
            sage: mpc(y) == x
            True"""
    @overload
    def __neg__(self) -> Any:
        """MPComplexNumber.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1491)

        Return the negative of this complex number.

            -(a + ib) = -a -i b

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: -a
            -2.00000000000000 - 1.00000000000000*I
            sage: a.__neg__()
            -2.00000000000000 - 1.00000000000000*I"""
    @overload
    def __neg__(self) -> Any:
        """MPComplexNumber.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1491)

        Return the negative of this complex number.

            -(a + ib) = -a -i b

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: -a
            -2.00000000000000 - 1.00000000000000*I
            sage: a.__neg__()
            -2.00000000000000 - 1.00000000000000*I"""
    @overload
    def __pari__(self) -> Any:
        """MPComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1196)

        Convert ``self`` to a PARI object.

        OUTPUT: a PARI ``t_COMPLEX`` object if the input is not purely
        real. If the input is real, a ``t_REAL`` is returned.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.__pari__()                                                          # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a)                                                               # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()                                                        # needs sage.libs.pari
            't_COMPLEX'
            sage: a = MPC(pi)                                                           # needs sage.libs.pari sage.symbolic
            sage: pari(a)                                                               # needs sage.libs.pari sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.libs.pari sage.symbolic
            't_REAL'
            sage: a = MPC(-2).sqrt()
            sage: pari(a)                                                               # needs sage.libs.pari
            1.41421356237310*I

        The precision is preserved, rounded up to the wordsize::

            sage: MPC = MPComplexField(250)
            sage: MPC(1,2).__pari__().bitprecision()                                    # needs sage.libs.pari
            256
            sage: MPC(pi).__pari__().bitprecision()                                     # needs sage.libs.pari
            256"""
    @overload
    def __pari__(self) -> Any:
        """MPComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1196)

        Convert ``self`` to a PARI object.

        OUTPUT: a PARI ``t_COMPLEX`` object if the input is not purely
        real. If the input is real, a ``t_REAL`` is returned.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.__pari__()                                                          # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a)                                                               # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()                                                        # needs sage.libs.pari
            't_COMPLEX'
            sage: a = MPC(pi)                                                           # needs sage.libs.pari sage.symbolic
            sage: pari(a)                                                               # needs sage.libs.pari sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.libs.pari sage.symbolic
            't_REAL'
            sage: a = MPC(-2).sqrt()
            sage: pari(a)                                                               # needs sage.libs.pari
            1.41421356237310*I

        The precision is preserved, rounded up to the wordsize::

            sage: MPC = MPComplexField(250)
            sage: MPC(1,2).__pari__().bitprecision()                                    # needs sage.libs.pari
            256
            sage: MPC(pi).__pari__().bitprecision()                                     # needs sage.libs.pari
            256"""
    @overload
    def __pari__(self) -> Any:
        """MPComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1196)

        Convert ``self`` to a PARI object.

        OUTPUT: a PARI ``t_COMPLEX`` object if the input is not purely
        real. If the input is real, a ``t_REAL`` is returned.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.__pari__()                                                          # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a)                                                               # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()                                                        # needs sage.libs.pari
            't_COMPLEX'
            sage: a = MPC(pi)                                                           # needs sage.libs.pari sage.symbolic
            sage: pari(a)                                                               # needs sage.libs.pari sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.libs.pari sage.symbolic
            't_REAL'
            sage: a = MPC(-2).sqrt()
            sage: pari(a)                                                               # needs sage.libs.pari
            1.41421356237310*I

        The precision is preserved, rounded up to the wordsize::

            sage: MPC = MPComplexField(250)
            sage: MPC(1,2).__pari__().bitprecision()                                    # needs sage.libs.pari
            256
            sage: MPC(pi).__pari__().bitprecision()                                     # needs sage.libs.pari
            256"""
    @overload
    def __pari__(self) -> Any:
        """MPComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1196)

        Convert ``self`` to a PARI object.

        OUTPUT: a PARI ``t_COMPLEX`` object if the input is not purely
        real. If the input is real, a ``t_REAL`` is returned.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: a = MPC(2,1)
            sage: a.__pari__()                                                          # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a)                                                               # needs sage.libs.pari
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()                                                        # needs sage.libs.pari
            't_COMPLEX'
            sage: a = MPC(pi)                                                           # needs sage.libs.pari sage.symbolic
            sage: pari(a)                                                               # needs sage.libs.pari sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.libs.pari sage.symbolic
            't_REAL'
            sage: a = MPC(-2).sqrt()
            sage: pari(a)                                                               # needs sage.libs.pari
            1.41421356237310*I

        The precision is preserved, rounded up to the wordsize::

            sage: MPC = MPComplexField(250)
            sage: MPC(1,2).__pari__().bitprecision()                                    # needs sage.libs.pari
            256
            sage: MPC(pi).__pari__().bitprecision()                                     # needs sage.libs.pari
            256"""
    def __pow__(self, right, modulus) -> Any:
        """MPComplexNumber.__pow__(self, right, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 1587)

        Compute ``self`` raised to the power of exponent, rounded in
        the direction specified by the parent of ``self``.

        .. TODO::

            FIXME: Branch cut

        EXAMPLES::

            sage: MPC.<i> = MPComplexField(20)
            sage: a = i^2; a
            -1.0000
            sage: a.parent()
            Complex Field with 20 bits of precision
            sage: a = (1+i)^i; a
            0.42883 + 0.15487*I
            sage: (1+i)^(1+i)
            0.27396 + 0.58370*I
            sage: a.parent()
            Complex Field with 20 bits of precision
            sage: i^i
            0.20788
            sage: (2+i)^(0.5)
            1.4553 + 0.34356*I"""
    def __reduce__(self) -> Any:
        """MPComplexNumber.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 904)

        For pickling.

        EXAMPLES::

            sage: C = MPComplexField(prec=200, rnd='RNDUU')
            sage: b = C(393.39203845902384098234098230948209384028340)
            sage: loads(dumps(b)) == b
            True
            sage: b = C(-1).sqrt(); b
            1.0000000000000000000000000000000000000000000000000000000000*I
            sage: loads(dumps(b)) == b
            True

        Some tests with ``NaN``, which cannot be compared to anything::

            sage: b = C(1)/C(0); b
            NaN + NaN*I
            sage: loads(dumps(b))
            NaN + NaN*I
            sage: b = C(-1)/C(0.); b
            NaN + NaN*I
            sage: loads(dumps(b))
            NaN + NaN*I"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, n) -> Any:
        """MPComplexNumber.__rshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2115)

        Fast division by `2^n`.

        EXAMPLES::

            sage: MPC = MPComplexField()
            sage: u = MPC(2, 4)
            sage: u>>2
            0.500000000000000 + 1.00000000000000*I
            sage: u>>(-1)
            4.00000000000000 + 8.00000000000000*I"""

class MPCtoMPC(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def section(self) -> Any:
        """MPCtoMPC.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2484)

        EXAMPLES::

            sage: from sage.rings.complex_mpc import *
            sage: C10 = MPComplexField(10)
            sage: C100 = MPComplexField(100)
            sage: f = MPCtoMPC(C100, C10)
            sage: f.section()
            Generic map:
              From: Complex Field with 10 bits of precision
              To:   Complex Field with 100 bits of precision"""
    @overload
    def section(self) -> Any:
        """MPCtoMPC.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpc.pyx (starting at line 2484)

        EXAMPLES::

            sage: from sage.rings.complex_mpc import *
            sage: C10 = MPComplexField(10)
            sage: C100 = MPComplexField(100)
            sage: f = MPCtoMPC(C100, C10)
            sage: f.section()
            Generic map:
              From: Complex Field with 10 bits of precision
              To:   Complex Field with 100 bits of precision"""

class MPFRtoMPC(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
