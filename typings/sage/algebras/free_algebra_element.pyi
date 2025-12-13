from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement as IndexedFreeModuleElement
from sage.monoids.free_monoid_element import FreeMonoidElement as FreeMonoidElement
from sage.structure.element import AlgebraElement as AlgebraElement

class FreeAlgebraElement(IndexedFreeModuleElement, AlgebraElement):
    """
    A free algebra element.

    TESTS:

    The ordering is inherited from ``IndexedFreeModuleElement``::

        sage: R.<x,y> = FreeAlgebra(QQ,2)
        sage: x < y
        True
        sage: x * y < y * x
        True
        sage: y * x < x * y
        False
    """
    def __init__(self, A, x) -> None:
        """
        Create the element ``x`` of the FreeAlgebra ``A``.

        TESTS::

            sage: F.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: elt = x^3 * y - z^2*x
            sage: TestSuite(elt).run()
        """
    def __call__(self, *x, **kwds):
        """
        EXAMPLES::

            sage: A.<x,y,z>=FreeAlgebra(ZZ,3)
            sage: (x+3*y).subs(x=1,y=2,z=14)
            7
            sage: (2*x+y).subs({x:1,y:z})
            2 + z
            sage: f = x+3*y+z
            sage: f(1,2,1/2)
            15/2
            sage: f(1,2)
            Traceback (most recent call last):
            ...
            ValueError: must specify as many values as generators in parent

        AUTHORS:

        - Joel B. Mohler (2007-10-27)
        """
    def is_unit(self) -> bool:
        """
        Return ``True`` if ``self`` is invertible.

        EXAMPLES::

            sage: A.<x, y, z> = FreeAlgebra(ZZ)
            sage: A(-1).is_unit()
            True
            sage: A(2).is_unit()
            False
            sage: A(1 + x).is_unit()
            False
            sage: A.<x, y> = FreeAlgebra(QQ, degrees=(1,-1))
            sage: A(x * y).is_unit()
            False
            sage: A(2).is_unit()
            True
        """
    def __invert__(self):
        """
        EXAMPLES::

            sage: A.<x, y, z> = FreeAlgebra(QQ)
            sage: ~A(1)
            1

        TESTS::

            sage: ~A(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: element is not invertible

            sage: ~A(1 + x)
            Traceback (most recent call last):
            ...
            ArithmeticError: element is not invertible
        """
    def variables(self) -> list:
        """
        Return the variables used in ``self``.

        EXAMPLES::

            sage: A.<x,y,z> = FreeAlgebra(ZZ,3)
            sage: elt = x + x*y + x^3*y
            sage: elt.variables()
            [x, y]
            sage: elt = x + x^2 - x^4
            sage: elt.variables()
            [x]
            sage: elt = x + z*y + z*x
            sage: elt.variables()
            [x, y, z]
        """
    def to_pbw_basis(self):
        """
        Return ``self`` in the Poincaré-Birkhoff-Witt (PBW) basis.

        EXAMPLES::

            sage: F.<x,y,z> = FreeAlgebra(ZZ, 3)
            sage: p = x^2*y + 3*y*x + 2
            sage: p.to_pbw_basis()
            2*PBW[1] + 3*PBW[y]*PBW[x] + PBW[x^2*y]
             + 2*PBW[x*y]*PBW[x] + PBW[y]*PBW[x]^2
        """
