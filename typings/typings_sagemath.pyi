from sage.rings.integer import Integer
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



type Int = int | Integer

type RealInexact = float | RealNumber | RealBall | RealIntervalFieldElement | RealDoubleElement | RealDoubleElement_gsl | RealIntervalAbsoluteElement
type ComplexInexact = complex | ComplexNumber | ComplexBall | ComplexIntervalFieldElement | ComplexDoubleElement | MPComplexNumber
type NumInexact = RealInexact | ComplexInexact

type Real = RealInexact | Rational | Int
type Complex = ComplexInexact
type FiniteNum = Real | Complex

type Floating =  RealInexact | ComplexInexact

type Num = Real | Complex

type Inf = PlusInfinity | MinusInfinity

type Expr = Expression

