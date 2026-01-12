from .numbers import Int
from cypari2.gen import Gen
from gmpy2 import mpz

# possible others, if it has a `_integer_` method 
# note that `list`, `tuple` objects are only convertible when `base` > 1
type ConvertibleToInteger = Int | Gen | mpz | bytes | None