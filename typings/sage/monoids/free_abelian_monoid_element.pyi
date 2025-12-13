import _cython_3_2_1
import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_FreeAbelianMonoidElement: _cython_3_2_1.cython_function_or_method

class FreeAbelianMonoidElement(sage.structure.element.MonoidElement):
    """FreeAbelianMonoidElement(parent, x)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 105)

                Create the element ``x`` of the FreeAbelianMonoid ``parent``.

                EXAMPLES::

                    sage: F = FreeAbelianMonoid(5, 'abcde')
                    sage: F
                    Free abelian monoid on 5 generators (a, b, c, d, e)
                    sage: F(1)
                    1
                    sage: F(2)
                    Traceback (most recent call last):
                    ...
                    TypeError: argument x (= 2) is of the wrong type
                    sage: F(int(1))
                    1
                    sage: a, b, c, d, e = F.gens()
                    sage: a^2 * b^3 * a^2 * b^4
                    a^4*b^7
                    sage: F = FreeAbelianMonoid(5, 'abcde')
                    sage: a, b, c, d, e = F.gens()
                    sage: a in F
                    True
                    sage: a*b in F
                    True
        """
    @overload
    def list(self) -> Any:
        """FreeAbelianMonoidElement.list(self)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 381)

        Return the underlying list used to represent ``self``.

        If this is a monoid in an abelian monoid on `n` generators,
        then this is a list of nonnegative integers of length `n`.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5, 'abcde')
            sage: (a, b, c, d, e) = F.gens()
            sage: a.list()
            [1, 0, 0, 0, 0]"""
    @overload
    def list(self) -> Any:
        """FreeAbelianMonoidElement.list(self)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 381)

        Return the underlying list used to represent ``self``.

        If this is a monoid in an abelian monoid on `n` generators,
        then this is a list of nonnegative integers of length `n`.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5, 'abcde')
            sage: (a, b, c, d, e) = F.gens()
            sage: a.list()
            [1, 0, 0, 0, 0]"""
    def __copy__(self) -> Any:
        """FreeAbelianMonoidElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 167)

        Return a copy of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5, 'abcde')
            sage: a, b, c, d, e = F.gens()
            sage: x = a^2 * b^3
            sage: copy(x) == x
            True
            sage: copy(x) is x
            False"""
    def __hash__(self) -> Any:
        '''FreeAbelianMonoidElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 367)

        Return the hash of ``self``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5,names = list("abcde"))
            sage: (a,b,c,d,e) = F.gens()
            sage: x = a*b^2*e*d
            sage: hash(x) == hash(x)
            True'''
    def __mul__(self, y) -> Any:
        """FreeAbelianMonoidElement.__mul__(self, y)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 304)

        Multiply ``self`` with ``y``.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5, 'abcde')
            sage: a, b, c, d, e = F.gens()
            sage: b * a^2 * b^3
            a^2*b^4"""
    def __pow__(self, n, modulus) -> Any:
        '''FreeAbelianMonoidElement.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 326)

        Raise ``self`` to the power of ``n``.

        AUTHORS:

        - Tom Boothby (2007-08): Replaced O(log n) time, O(n) space
          algorithm with O(1) time and space "algorithm".

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5,names = list("abcde"))
            sage: (a,b,c,d,e) = F.gens()
            sage: x = a*b^2*e*d; x
            a*b^2*d*e
            sage: x^3
            a^3*b^6*d^3*e^3
            sage: x^0
            1'''
    def __reduce__(self) -> Any:
        """FreeAbelianMonoidElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/monoids/free_abelian_monoid_element.pyx (starting at line 188)

        Used in pickling.

        EXAMPLES::

            sage: F = FreeAbelianMonoid(5, 'abcde')
            sage: a, b, c, d, e = F.gens()
            sage: x = a^2 * b^3
            sage: loads(dumps(x)) == x
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
