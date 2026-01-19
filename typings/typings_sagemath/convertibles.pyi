from .numbers import Int, RealInexactSage, ComplexInexactSage
from cypari2.gen import Gen
from gmpy2 import mpz
from sage.rings.infinity import PlusInfinity, MinusInfinity, UnsignedInfinity
from sage.rings.real_mpfr import RealNumber
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.qqbar import AlgebraicField # TODO: with_category
from sage.rings.rational_field import RationalField
from sage.rings.semirings.non_negative_integer_semiring import NonNegativeIntegerSemiring
from sage.structure.factorization import Factorization
from sage.structure.element import Matrix, RingElement
from sage.symbolic.expression import Expression
from numpy import (
    integer as NumPyInteger, 
    floating as NumPyFloating, 
    complexfloating as NumPyComplexFloating
)
from sympy.core.basic import Basic as SymPyBasic

# possible others, if it has a `_integer_` method 
# note that `list`, `tuple` objects are only convertible when `base` > 1
type ConvertibleToInteger = Int | str | Gen | bytes | None

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
