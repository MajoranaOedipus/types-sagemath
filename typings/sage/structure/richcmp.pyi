r"""
Cython-like rich comparisons in Python

With "rich comparisons", we mean the Python 3 comparisons which are
usually implemented in Python using methods like ``__eq__`` and
``__lt__``. Internally in Python, there is only one rich comparison
slot ``tp_richcompare``. The actual operator is passed as an integer
constant (defined in this module as
``op_LT``, ``op_LE``, ``op_EQ``, ``op_NE``, ``op_GT``, ``op_GE``).

Cython exposes rich comparisons in ``cdef`` classes as the
``__richcmp__`` special method. The Sage coercion model also supports
rich comparisons this way: for two instances ``x`` and ``y``
of :class:`~sage.structure.element.Element`, ``x._richcmp_(y, op)``
is called when the user does something like ``x <= y``
(possibly after coercion if ``x`` and ``y`` have different parents).

Various helper functions exist to make it easier to implement rich
comparison: the most important one is the :func:`richcmp` function.
This is analogous to the Python 2 function ``cmp()`` but implements
rich comparison, with the comparison operator (e.g. ``op_GE``) as
third argument. There is also :func:`richcmp_not_equal` which is like
:func:`richcmp` but it is optimized assuming that the compared objects
are not equal.

The functions :func:`rich_to_bool` and :func:`rich_to_bool_sgn` can be
used to convert results of ``cmp()`` (i.e. -1, 0 or 1) to a boolean
``True``/``False`` for rich comparisons.

AUTHORS:

- Jeroen Demeyer
"""
from typing import Literal
from typings_sagemath import CmpOperator, SupportsRichCmp, RichCmpMixin
import _cython_3_2_1

op_LT: Literal[0]
op_LE: Literal[1]
op_EQ: Literal[2]
op_NE: Literal[3]
op_GT: Literal[4]
op_GE: Literal[5]


def richcmp_item(x, y, op: CmpOperator):
    """
    This function is meant to implement lexicographic rich comparison
    of sequences (lists, vectors, polynomials, ...).
    The inputs ``x`` and ``y`` are corresponding items of such lists
    which should compared.

    INPUT:

    - ``x``, ``y`` -- arbitrary Python objects; typically, these are
      ``X[i]`` and ``Y[i]`` for sequences ``X`` and ``Y``

    - ``op`` -- comparison operator (one of ``op_LT``, ``op_LE``,
      ``op_EQ``, ``op_NE``, ``op_GT``, ``op_GE``)

    OUTPUT: assuming that ``x = X[i]`` and ``y = Y[i]``:

    - if the comparison ``X {op} Y`` (where ``op`` is the given
      operation) could not be decided yet (i.e. we should compare the
      next items in the list): return ``NotImplemented``

    - otherwise, if the comparison ``X {op} Y`` could be decided:
      return ``x {op} y``, which should then also be the result for
      ``X {op} Y``.

    .. NOTE::

        Since ``x {op} y`` cannot return ``NotImplemented``, the two
        cases above are mutually exclusive.

    The semantics of the comparison is different from Python lists or
    tuples in the case that the order is not total. Assume that ``A``
    and ``B`` are lists whose rich comparison is implemented using
    ``richcmp_item`` (as in EXAMPLES below). Then

    - ``A == B`` iff ``A[i] == B[i]`` for all indices `i`.

    - ``A != B`` iff ``A[i] != B[i]`` for some index `i`.

    - ``A < B`` iff ``A[i] < B[i]`` for some index `i` and
      for all `j < i`, ``A[j] <= B[j]``.

    - ``A <= B`` iff ``A < B`` or ``A[i] <= B[i]`` for all `i`.

    - ``A > B`` iff ``A[i] > B[i]`` for some index `i` and
      for all `j < i`, ``A[j] >= B[j]``.

    - ``A >= B`` iff ``A > B`` or ``A[i] >= B[i]`` for all `i`.

    See below for a detailed description of the exact semantics of
    ``richcmp_item`` in general.

    EXAMPLES::

        sage: from sage.structure.richcmp import *
        sage: @richcmp_method
        ....: class Listcmp(list):
        ....:     def __richcmp__(self, other, op):
        ....:         for i in range(len(self)):  # Assume equal lengths
        ....:             res = richcmp_item(self[i], other[i], op)
        ....:             if res is not NotImplemented:
        ....:                 return res
        ....:         return rich_to_bool(op, 0)  # Consider the lists to be equal
        sage: a = Listcmp([0, 1, 3])
        sage: b = Listcmp([0, 2, 1])
        sage: a == a
        True
        sage: a != a
        False
        sage: a < a
        False
        sage: a <= a
        True
        sage: a > a
        False
        sage: a >= a
        True
        sage: a == b, b == a
        (False, False)
        sage: a != b, b != a
        (True, True)
        sage: a < b, b > a
        (True, True)
        sage: a <= b, b >= a
        (True, True)
        sage: a > b, b < a
        (False, False)
        sage: a >= b, b <= a
        (False, False)

    The above tests used a list of integers, where the result of
    comparisons are the same as for Python lists.

    If we want to see the difference, we need more general entries in
    the list. The comparison rules are made to be consistent with
    setwise operations. If `A` and `B` are sets, we define ``A {op} B``
    to be true if ``a {op} B`` is true for every `a` in `A` and
    `b` in `B`. Interval comparisons are a special case of this. For
    lists of non-empty(!) sets, we want that ``[A1, A2] {op} [B1, B2]``
    is true if and only if ``[a1, a2] {op} [b1, b2]`` is true for all
    elements. We verify this::

        sage: @richcmp_method
        ....: class Setcmp(tuple):
        ....:     def __richcmp__(self, other, op):
        ....:         return all(richcmp(x, y, op) for x in self for y in other)
        sage: sym = {op_EQ: "==", op_NE: "!=", op_LT: "<", op_GT: ">", op_LE: "<=", op_GE: ">="}
        sage: for A1 in Set(range(4)).subsets():  # long time
        ....:     if not A1: continue
        ....:     for B1 in Set(range(4)).subsets():
        ....:         if not B1: continue
        ....:         for A2 in Set(range(4)).subsets():
        ....:             if not A2: continue
        ....:             for B2 in Set(range(3)).subsets():
        ....:                 if not B2: continue
        ....:                 L1 = Listcmp([Setcmp(A1), Setcmp(A2)])
        ....:                 L2 = Listcmp([Setcmp(B1), Setcmp(B2)])
        ....:                 for op in range(6):
        ....:                     reslist = richcmp(L1, L2, op)
        ....:                     reselt = all(richcmp([a1, a2], [b1, b2], op) for a1 in A1 for a2 in A2 for b1 in B1 for b2 in B2)
        ....:                     assert reslist is reselt

    EXACT SEMANTICS:

    Above, we only described how ``richcmp_item`` behaves when it is
    used to compare sequences. Here, we specify the exact semantics.
    First of all, recall that the result of ``richcmp_item(x, y, op)``
    is either ``NotImplemented`` or ``x {op} y``.

    - if ``op`` is ``==``: return ``NotImplemented`` if ``x == y``.
      If ``x == y`` is false, then return ``x == y``.

    - if ``op`` is ``!=``: return ``NotImplemented`` if not ``x != y``.
      If ``x != y`` is true, then return ``x != y``.

    - if ``op`` is ``<``: return ``NotImplemented`` if ``x == y``.
      If ``x < y`` or not ``x <= y``, return ``x < y``.
      Otherwise (if both ``x == y`` and ``x < y`` are false but
      ``x <= y`` is true), return ``NotImplemented``.

    - if ``op`` is ``<=``: return ``NotImplemented`` if ``x == y``.
      If ``x < y`` or not ``x <= y``, return ``x <= y``.
      Otherwise (if both ``x == y`` and ``x < y`` are false but
      ``x <= y`` is true), return ``NotImplemented``.

    - the ``>`` and ``>=`` operators are analogous to ``<`` and ``<=``.
    """

# for type
def richcmp_method[_T](cls: SupportsRichCmp[_T]) -> RichCmpMixin[_T]:
    """
    Class decorator to implement rich comparison using the special
    method ``__richcmp__`` (analogous to Cython) instead of the 6
    methods ``__eq__`` and friends.

    This changes the class in-place and returns the given class.

    EXAMPLES::

        sage: from sage.structure.richcmp import *
        sage: sym = {op_EQ: "==", op_NE: "!=", op_LT: "<", op_GT: ">", op_LE: "<=", op_GE: ">="}
        sage: @richcmp_method
        ....: class A(str):
        ....:     def __richcmp__(self, other, op):
        ....:         print("%s %s %s" % (self, sym[op], other))
        sage: A("left") < A("right")
        left < right
        sage: object() <= A("right")
        right >= <object object at ...>

    We can call this comparison with the usual Python special methods::

        sage: x = A("left"); y = A("right")
        sage: x.__eq__(y)
        left == right
        sage: A.__eq__(x, y)
        left == right

    Everything still works in subclasses::

        sage: class B(A):
        ....:     pass
        sage: x = B("left"); y = B("right")
        sage: x != y
        left != right
        sage: x.__ne__(y)
        left != right
        sage: B.__ne__(x, y)
        left != right

    We can override ``__richcmp__`` with standard Python rich
    comparison methods and conversely::

        sage: class C(A):
        ....:     def __ne__(self, other):
        ....:         return False
        sage: C("left") != C("right")
        False
        sage: C("left") == C("right")  # Calls __eq__ from class A
        left == right

        sage: class Base():
        ....:     def __eq__(self, other):
        ....:         return False
        sage: @richcmp_method
        ....: class Derived(Base):
        ....:     def __richcmp__(self, other, op):
        ....:         return True
        sage: Derived() == Derived()
        True

    TESTS::

        sage: richcmp_method(None)
        Traceback (most recent call last):
        ...
        TypeError: None is not a class

        sage: @richcmp_method
        ....: class X():
        ....:     def __eq__(self, other):
        ....:         pass
        ....:     def __richcmp__(self, other, op):
        ....:         pass
        Traceback (most recent call last):
        ...
        TypeError: class <class '__main__.X'> defines __eq__ which cannot be combined with @richcmp_method
    """

revop: _cython_3_2_1.cython_function_or_method
rich_to_bool: _cython_3_2_1.cython_function_or_method
rich_to_bool_sgn: _cython_3_2_1.cython_function_or_method
richcmp: _cython_3_2_1.cython_function_or_method
richcmp_by_eq_and_lt: _cython_3_2_1.cython_function_or_method

richcmp_not_equal: _cython_3_2_1.cython_function_or_method
