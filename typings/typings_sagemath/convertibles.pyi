from numbers import Real
from typings_sagemath import FloatingSage, Num

from sage.symbolic.ring import SymbolicRing

from sage.rings.finite_rings.integer_mod import IntegerMod_int

from sage.rings.imaginary_unit import NumberFieldElement_gaussian
from .numbers import Int, RealInexactSage, ComplexInexactSage
from cypari2.gen import Gen
from gmpy2 import mpc, mpz, mpfr
from sage.rings.infinity import PlusInfinity, MinusInfinity, UnsignedInfinity
from sage.rings.real_mpfr import RealNumber
from sage.rings.real_double import RealDoubleElement
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.qqbar import AlgebraicField # TODO: with_category
from sage.rings.number_field.number_field_element_quadratic import OrderElement_quadratic
from sage.rings.rational_field import RationalField
from sage.rings.rational import Rational
from sage.rings.semirings.non_negative_integer_semiring import NonNegativeIntegerSemiring
from sage.structure.factorization import Factorization
from sage.structure.element import Matrix, RingElement
from sage.symbolic.expression import Expression
from sage.sets.real_set import InternalRealInterval, RealSet
from sage.libs.mpmath.all import mpf as MpMathMpf, mpc as MpMathMpc
from numpy import (
    integer as NumPyInteger, 
    floating as NumPyFloating, 
    complexfloating as NumPyComplexFloating,
    number as NumPyNumber
)
from sympy.core.basic import Basic as SymPyBasic

type _py_number = int | float | complex
type _MpMathNumber = MpMathMpf | MpMathMpc | MpMathMpi
type _signed_inf = PlusInfinity | MinusInfinity
type _inf = _signed_inf | UnsignedInfinity

# possible others, if it has a `_integer_` method 
# note that `list`, `tuple` objects are only convertible when `base` > 1
type ConvertibleToInteger = Int | str | Gen | bytes | None
type CoercibleToInteger = int | mpz | NumPyInteger | IntegerMod_int | Integer | str

# TODO
type ConvertibleToRealNumber = Int | str | float | mpfr | NumPyFloating | RealInexactSage | OrderElement_quadratic | Rational | Gen | Expression[SymbolicRing]
type ConvertibleToComplexNumber = (
    int | float | mpz | mpfr | NumPyFloating | NumPyInteger
        | Integer | Expression | RealNumber | RealDoubleElement
        | _signed_inf
)

# possible others, if it has a `_symbolic_` method, or it is a finite set (in Sets() and is_finite)
# c.f. symbolic.expression.new_Expression
type ConvertibleToExpression = (
    Expression | str | float | complex | int
        | RealNumber | RingElement | Matrix | Factorization 
        | PlusInfinity | MinusInfinity| UnsignedInfinity 
        | IntegerRing_class | AlgebraicField | RationalField 
        | NonNegativeIntegerSemiring 
    )

# not completed, need to check
#   (PolynomialRing_generic, MPolynomialRing_base, 
#    FractionField_generic, LaurentPolynomialRing_generic)
# elements
# also (sage.rings.abc.RealIntervalField,
#       sage.rings.abc.ComplexIntervalField,
#       sage.rings.abc.RealBallField,
#       sage.rings.abc.ComplexBallField,
#       sage.rings.abc.IntegerModRing,
#       FiniteField)
# elements are all coercible to SR
type CoercibleToExpression = (
    Expression | int | float | complex | bool
        | NumPyInteger | NumPyFloating | NumPyComplexFloating | SymPyBasic
        | RealInexactSage | ComplexInexactSage
)
type CoercibleToRealNumber = (
    Int | str | float | mpfr | NumPyFloating | RealInexactSage | OrderElement_quadratic
     | Rational | Gen | PlusInfinity | MinusInfinity | Expression[SymbolicRing]
)
type CoercibleToRDF = (
    Int | str | float | mpfr | NumPyFloating | RealInexactSage | OrderElement_quadratic
     | Rational | Gen | PlusInfinity | MinusInfinity | Expression[SymbolicRing]
)
type CoercibleToComplexNumber = (
    _py_number | mpz | mpfr | mpc | NumPyFloating | NumPyInteger
        | Integer | Rational | Expression | OrderElement_quadratic
        | NumberFieldElement_gaussian | FloatingSage | _signed_inf
)
type CoercibleToCDF = (
    _py_number | mpz | mpfr | mpc | NumPyNumber | OrderElement_quadratic
        | Integer | Rational | Expression
        | NumberFieldElement_gaussian | FloatingSage | _signed_inf
)

type ConvertibleToRealSet = RealSet | InternalRealInterval | tuple[Real, Real] | list[Real]

# c.f. libs/mpmath/ext_main.pyx: Context.convert and MPF_set_any
type ConvertibleToMpMathNumber = (
    _py_number | mpfr | Integer | IntegerMod_int | Expression[SymbolicRing]
    | OrderElement_quadratic | NumberFieldElement_gaussian | FloatingSage | str
    | PlusInfinity | MinusInfinity | _MpMathNumber
)