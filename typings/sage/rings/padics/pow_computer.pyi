import _cython_3_2_1
import sage.structure.sage_object
from sage.rings.infinity import infinity as infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar

PowComputer: _cython_3_2_1.cython_function_or_method
pow_comp_cache: dict

class PowComputer_base(PowComputer_class):
    """PowComputer_base(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None, shift_seed=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=..., shift_seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer.pyx (starting at line 494)

                Initialization.

                TESTS::

                    sage: PC = PowComputer(5, 7, 10)
                    sage: PC(3)
                    125
        """
    def __reduce__(self) -> Any:
        """PowComputer_base.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer.pyx (starting at line 545)

        Pickling.

        EXAMPLES::

            sage: P = PowComputer(5, 7, 10)
            sage: R = loads(dumps(P))
            sage: P == R
            True"""

class PowComputer_class(sage.structure.sage_object.SageObject):
    """PowComputer_class(Integer prime, long cache_limit, long prec_cap, long ram_prec_cap, bool in_field, poly=None, shift_seed=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Integerprime, longcache_limit, longprec_cap, longram_prec_cap, boolin_field, poly=..., shift_seed=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer.pyx (starting at line 70)

                Initialize ``self``.

                INPUT:

                - ``prime`` -- the prime that is the base of the exponentials
                  stored in this ``pow_computer``

                - ``cache_limit`` -- how high to cache powers of prime

                - ``prec_cap`` -- data stored for `p`-adic elements using this
                  ``pow_computer`` (so they have C-level access to fields
                  common to all elements of the same parent)

                - ``ram_prec_cap`` -- prec_cap * e

                - ``in_field`` -- same idea as prec_cap

                - ``poly`` -- same idea as prec_cap

                - ``shift_seed`` -- same idea as prec_cap

                EXAMPLES::

                    sage: PC = PowComputer(3, 5, 10)
                    sage: PC.pow_Integer_Integer(2)
                    9
        """
    def pow_Integer_Integer(self, n) -> Any:
        """PowComputer_class.pow_Integer_Integer(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer.pyx (starting at line 163)

        Test the ``pow_Integer`` function.

        EXAMPLES::

            sage: PC = PowComputer(3, 5, 10)
            sage: PC.pow_Integer_Integer(4)
            81
            sage: PC.pow_Integer_Integer(6)
            729
            sage: PC.pow_Integer_Integer(0)
            1
            sage: PC.pow_Integer_Integer(10)
            59049

            sage: # needs sage.libs.ntl
            sage: PC = PowComputer_ext_maker(3, 5, 10, 20, False, ntl.ZZ_pX([-3,0,1], 3^10), 'big','e',ntl.ZZ_pX([1],3^10))
            sage: PC.pow_Integer_Integer(4)
            81
            sage: PC.pow_Integer_Integer(6)
            729
            sage: PC.pow_Integer_Integer(0)
            1
            sage: PC.pow_Integer_Integer(10)
            59049"""
    def __call__(self, n) -> Any:
        """PowComputer_class.__call__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer.pyx (starting at line 399)

        Return ``self.prime^n``.

        EXAMPLES::

            sage: P = PowComputer(3, 4, 6)
            sage: P(3)
            27
            sage: P(6)
            729
            sage: P(5)
            243
            sage: P(7)
            2187
            sage: P(0)
            1
            sage: P(-2)
            1/9"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
