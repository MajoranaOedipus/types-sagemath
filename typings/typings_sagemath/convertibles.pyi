from .numbers import Int
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


# possible others, if it has a `_integer_` method 
# note that `list`, `tuple` objects are only convertible when `base` > 1
type ConvertibleToInteger = Int | Gen | mpz | bytes | None

# possible others, if it has a `_symbolic_` method, or it is a finite set (in Sets() and is_finite)
type ConvertibleToExpression = Expression | str | float | complex | int | RealNumber | RingElement | Matrix | Factorization | PlusInfinity | MinusInfinity| UnsignedInfinity | IntegerRing_class | AlgebraicField | RationalField | NonNegativeIntegerSemiring