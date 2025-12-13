import _cython_3_2_1
import sage.modules.vector_rational_dense
from sage.misc.latex import latex as latex
from sage.modules.free_module_element import vector as vector
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_ToricRationalDivisorClass: _cython_3_2_1.cython_function_or_method

class ToricRationalDivisorClass(sage.modules.vector_rational_dense.Vector_rational_dense):
    """File: /build/sagemath/src/sage/src/sage/schemes/toric/divisor_class.pyx (starting at line 94)

        Create a toric rational divisor class.

        .. WARNING::

            You probably should not construct divisor classes explicitly.

        INPUT:

        - same as for
          :class:`~sage.modules.vector_rational_dense.Vector_rational_dense`.

        OUTPUT: toric rational divisor class

        TESTS::

            sage: dP6 = toric_varieties.dP6()
            sage: Cl = dP6.rational_class_group()
            sage: D = dP6.divisor(2)
            sage: Cl(D)
            Divisor class [0, 0, 1, 0]
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def lift(self) -> Any:
        """ToricRationalDivisorClass.lift(self)

        File: /build/sagemath/src/sage/src/sage/schemes/toric/divisor_class.pyx (starting at line 255)

        Return a divisor representing this divisor class.

        OUTPUT: an instance of :class:`ToricDivisor` representing ``self``

        EXAMPLES::

            sage: X = toric_varieties.Cube_nonpolyhedral()
            sage: D = X.divisor([0,1,2,3,4,5,6,7]); D
            V(z1) + 2*V(z2) + 3*V(z3) + 4*V(z4) + 5*V(z5) + 6*V(z6) + 7*V(z7)
            sage: D.divisor_class()
            Divisor class [29, 6, 8, 10, 0]
            sage: Dequiv = D.divisor_class().lift(); Dequiv
            15*V(z1) - 11*V(z2) - 9*V(z5) + 19*V(z6) + 10*V(z7)
            sage: Dequiv == D
            False
            sage: Dequiv.divisor_class() == D.divisor_class()
            True"""
    @overload
    def lift(self) -> Any:
        """ToricRationalDivisorClass.lift(self)

        File: /build/sagemath/src/sage/src/sage/schemes/toric/divisor_class.pyx (starting at line 255)

        Return a divisor representing this divisor class.

        OUTPUT: an instance of :class:`ToricDivisor` representing ``self``

        EXAMPLES::

            sage: X = toric_varieties.Cube_nonpolyhedral()
            sage: D = X.divisor([0,1,2,3,4,5,6,7]); D
            V(z1) + 2*V(z2) + 3*V(z3) + 4*V(z4) + 5*V(z5) + 6*V(z6) + 7*V(z7)
            sage: D.divisor_class()
            Divisor class [29, 6, 8, 10, 0]
            sage: Dequiv = D.divisor_class().lift(); Dequiv
            15*V(z1) - 11*V(z2) - 9*V(z5) + 19*V(z6) + 10*V(z7)
            sage: Dequiv == D
            False
            sage: Dequiv.divisor_class() == D.divisor_class()
            True"""
    def __reduce__(self) -> Any:
        """ToricRationalDivisorClass.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/schemes/toric/divisor_class.pyx (starting at line 118)

        Prepare ``self`` for pickling.

        TESTS::

            sage: dP6 = toric_varieties.dP6()
            sage: Cl = dP6.rational_class_group()
            sage: D = Cl([1, -2, 3, -4])
            sage: D
            Divisor class [1, -2, 3, -4]
            sage: loads(dumps(D))
            Divisor class [1, -2, 3, -4]"""
