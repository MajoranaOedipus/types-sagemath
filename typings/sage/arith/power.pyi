import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

__pyx_capi__: dict
def generic_power(a, n):
    r"""generic_power(a, n)

File: /build/sagemath/src/sage/src/sage/arith/power.pyx (starting at line 24)

Return `a^n`.

If `n` is negative, return `(1/a)^{-n}`.

INPUT:

- ``a`` -- any object supporting multiplication
  (and division if n < 0)

- ``n`` -- any integer (in the duck typing sense)

EXAMPLES::

    sage: from sage.arith.power import generic_power
    sage: generic_power(int(12), int(0))
    1
    sage: generic_power(int(0), int(100))
    0
    sage: generic_power(Integer(10), Integer(0))
    1
    sage: generic_power(Integer(0), Integer(23))
    0
    sage: sum([generic_power(2,i) for i in range(17)]) #test all 4-bit combinations
    131071
    sage: F = Zmod(5)
    sage: a = generic_power(F(2), 5); a
    2
    sage: a.parent() is F
    True
    sage: a = generic_power(F(1), 2)
    sage: a.parent() is F
    True

    sage: generic_power(int(5), 0)
    1
    sage: generic_power(2, 5/4)
    Traceback (most recent call last):
    ...
    NotImplementedError: non-integral exponents not supported

::

    sage: class SymbolicMul(str):
    ....:     def __mul__(self, other):
    ....:         s = "({}*{})".format(self, other)
    ....:         return type(self)(s)
    sage: x = SymbolicMul("x")
    sage: print(generic_power(x, 7))
    (((x*x)*(x*x))*((x*x)*x))
"""
