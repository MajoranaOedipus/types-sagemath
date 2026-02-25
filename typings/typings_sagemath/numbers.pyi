from sage.rings.integer import Integer
from sage.rings.finite_rings.integer_mod import IntegerMod_int
from sage.symbolic.expression import Expression
from sage.rings.real_mpfr import RealNumber
from sage.rings.real_arb import RealBall
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.real_double import RealDoubleElement
from sage.rings.real_double_element_gsl import RealDoubleElement_gsl
from sage.rings.real_interval_absolute import RealIntervalAbsoluteElement
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.complex_arb import ComplexBall
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.complex_mpc import MPComplexNumber
from sage.rings.rational import Rational
from sage.rings.infinity import PlusInfinity, MinusInfinity

from numpy import floating as NumPyFloating, integer as NumPyInteger, complexfloating as NumPyComplex
from gmpy2 import mpz, mpfr

# possible others, if it can be lifted to `ZZ`'s element
type IntSupportingBitwiseOp = int | Integer | NumPyInteger | mpz
type Int = IntSupportingBitwiseOp | IntegerMod_int

type RealInexactSage = RealNumber | RealBall | RealIntervalFieldElement | RealDoubleElement | RealDoubleElement_gsl | RealIntervalAbsoluteElement
type RealInexact = float | mpfr | RealInexactSage | NumPyFloating
type ComplexInexactSage = ComplexNumber | ComplexBall | ComplexIntervalFieldElement | ComplexDoubleElement | MPComplexNumber
type ComplexInexact = complex | ComplexInexactSage | NumPyComplex
type NumInexact = RealInexact | ComplexInexact
type NumInexactSage = RealInexactSage | ComplexInexactSage

type Real = RealInexact | Rational | Int
type Complex = ComplexInexact
type FiniteNum = Real | Complex

type Floating =  RealInexact | ComplexInexact
type FloatingSage = RealInexactSage | ComplexInexactSage

type Num = Real | Complex

type Inf = PlusInfinity | MinusInfinity

type Expr = Expression



