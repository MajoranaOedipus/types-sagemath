import _cython_3_2_1
import sage.modules.vector_integer_dense
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_ToricLatticeElement: _cython_3_2_1.cython_function_or_method
unpickle_v1: _cython_3_2_1.cython_function_or_method

class ToricLatticeElement(sage.modules.vector_integer_dense.Vector_integer_dense):
    """File: /build/sagemath/src/sage/src/sage/geometry/toric_lattice_element.pyx (starting at line 142)

        Create an element of a toric lattice.

        .. WARNING::

            You probably should not construct such elements explicitly.

        INPUT:

        - same as for
          :class:`~sage.modules.vector_integer_dense.Vector_integer_dense`.

        OUTPUT: element of a toric lattice

        TESTS::

            sage: N = ToricLattice(3)
            sage: from sage.geometry.toric_lattice_element import (
            ....:           ToricLatticeElement)
            sage: e = ToricLatticeElement(N, [1,2,3])
            sage: e
            N(1, 2, 3)
            sage: TestSuite(e).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def plot(self, **options) -> Any:
        """ToricLatticeElement.plot(self, **options)

        File: /build/sagemath/src/sage/src/sage/geometry/toric_lattice_element.pyx (starting at line 373)

        Plot ``self``.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: n = N(1,2,3)
            sage: n.plot()                                                              # needs sage.plot
            Graphics3d Object"""
    @overload
    def plot(self) -> Any:
        """ToricLatticeElement.plot(self, **options)

        File: /build/sagemath/src/sage/src/sage/geometry/toric_lattice_element.pyx (starting at line 373)

        Plot ``self``.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: n = N(1,2,3)
            sage: n.plot()                                                              # needs sage.plot
            Graphics3d Object"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """ToricLatticeElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/toric_lattice_element.pyx (starting at line 205)

        Return the hash of ``self``.

        OUTPUT: integer

        TESTS::

            sage: N = ToricLattice(3)
            sage: n = N(1,2,3)
            sage: hash(n)
            Traceback (most recent call last):
            ...
            TypeError: mutable vectors are unhashable
            sage: n.set_immutable()
            sage: hash(n) == hash(n)
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """ToricLatticeElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/toric_lattice_element.pyx (starting at line 360)

        Override the base ``__reduce__`` to correctly pickle/unpickle elements.

        EXAMPLES::

            sage: N = ToricLattice(3)
            sage: loads(dumps(N(1,2,3)))
            N(1, 2, 3)"""
