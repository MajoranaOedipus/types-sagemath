import _cython_3_2_1
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.category import ZZ as ZZ
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import column_matrix as column_matrix, diagonal_matrix as diagonal_matrix
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

loop_over_parallelotope_points: _cython_3_2_1.cython_function_or_method
parallelotope_points: _cython_3_2_1.cython_function_or_method
print_cache: _cython_3_2_1.cython_function_or_method
ray_matrix_normal_form: _cython_3_2_1.cython_function_or_method
rectangular_box_points: _cython_3_2_1.cython_function_or_method
simplex_points: _cython_3_2_1.cython_function_or_method

class InequalityCollection:
    """File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 970)

        A collection of inequalities.

        INPUT:

        - ``polyhedron`` -- a polyhedron defining the inequalities

        - ``permutation`` -- list; a 0-based permutation of the coordinates
          Will be used to permute the coordinates of the inequality

        - ``box_min``, ``box_max`` -- the (not permuted) minimal and maximal
          coordinates of the bounding box; used for bounds checking

        EXAMPLES::

            sage: from sage.geometry.integral_points import InequalityCollection
            sage: P_QQ = Polyhedron(identity_matrix(3).columns() + [(-2, -1,-1)], base_ring=QQ)
            sage: ieq = InequalityCollection(P_QQ, [0,1,2], [0]*3,[1]*3); ieq
            The collection of inequalities
            integer: (3, -2, -2) x + 2 >= 0
            integer: (-1, 4, -1) x + 1 >= 0
            integer: (-1, -1, 4) x + 1 >= 0
            integer: (-1, -1, -1) x + 1 >= 0

            sage: P_RR = Polyhedron(identity_matrix(2).columns() + [(-2.7, -1)], base_ring=RDF)
            sage: InequalityCollection(P_RR, [0,1], [0]*2, [1]*2)
            The collection of inequalities
            integer: (-1, -1) x + 1 >= 0
            generic: (-1.0, 3.7) x + 1.0 >= 0
            generic: (1.0, -1.35) x + 1.35 >= 0

            sage: line = Polyhedron(eqns=[(2,3,7)])
            sage: InequalityCollection(line, [0,1], [0]*2, [1]*2 )
            The collection of inequalities
            integer: (3, 7) x + 2 >= 0
            integer: (-3, -7) x + -2 >= 0

        TESTS::

            sage: TestSuite(ieq).run(skip='_test_pickling')
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def are_satisfied(self, inner_loop_variable) -> bool:
        """InequalityCollection.are_satisfied(self, inner_loop_variable) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 1317)

        Return whether all inequalities are satisfied.

        You must call :meth:`prepare_inner_loop` before calling this
        method.

        INPUT:

        - ``inner_loop_variable`` -- integer; the 0th coordinate of
          the lattice point

        OUTPUT: boolean; whether the lattice point is in the polyhedron

        EXAMPLES::

            sage: from sage.geometry.integral_points import InequalityCollection
            sage: line = Polyhedron(eqns=[(2,3,7)])
            sage: ieq = InequalityCollection(line, [0,1], [0]*2, [1]*2 )
            sage: ieq.prepare_next_to_inner_loop([3,4])
            sage: ieq.prepare_inner_loop([3,4])
            sage: ieq.are_satisfied(3)
            False"""
    def prepare_inner_loop(self, p) -> Any:
        """InequalityCollection.prepare_inner_loop(self, p)

        File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 1244)

        Peel off the inner loop.

        In the inner loop of :func:`rectangular_box_points`, we have
        to repeatedly evaluate `A x+b\\geq 0`. To speed up computation, we pre-evaluate

        .. MATH::

            c = A x - A_0 x_0 +b = b + \\sum_{i=1} A_i x_i

        and only test `A_0 x_0 +c \\geq 0` in the inner loop.

        You must call :meth:`prepare_next_to_inner_loop` before
        calling this method.

        INPUT:

        - ``p`` -- the coordinates of the point to loop over. Only the
          ``p[1:]`` entries are used

        EXAMPLES::

             sage: from sage.geometry.integral_points import InequalityCollection, print_cache
             sage: P = Polyhedron(ieqs=[(2,3,7,11)])
             sage: ieq = InequalityCollection(P, [0,1,2], [0]*3,[1]*3); ieq
             The collection of inequalities
             integer: (3, 7, 11) x + 2 >= 0
             sage: ieq.prepare_next_to_inner_loop([2,1,3])
             sage: ieq.prepare_inner_loop([2,1,3])
             sage: print_cache(ieq)
             Cached inner loop: 3 * x_0 + 42 >= 0
             Cached next-to-inner loop: 3 * x_0 + 7 * x_1 + 35 >= 0"""
    def prepare_next_to_inner_loop(self, p) -> Any:
        """InequalityCollection.prepare_next_to_inner_loop(self, p)

        File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 1206)

        Peel off the next-to-inner loop.

        In the next-to-inner loop of :func:`rectangular_box_points`,
        we have to repeatedly evaluate `A x-A_0 x_0+b`. To speed up
        computation, we pre-evaluate

        .. MATH::

            c = b + \\sum_{i=2} A_i x_i

        and only compute `A x-A_0 x_0+b = A_1 x_1 +c \\geq 0` in the
        next-to-inner loop.

        INPUT:

        - ``p`` -- the point coordinates. Only ``p[2:]`` coordinates
          are potentially used by this method

        EXAMPLES::

             sage: from sage.geometry.integral_points import InequalityCollection, print_cache
             sage: P = Polyhedron(ieqs=[(2,3,7,11)])
             sage: ieq = InequalityCollection(P, [0,1,2], [0]*3,[1]*3); ieq
             The collection of inequalities
             integer: (3, 7, 11) x + 2 >= 0
             sage: ieq.prepare_next_to_inner_loop([2,1,3])
             sage: ieq.prepare_inner_loop([2,1,3])
             sage: print_cache(ieq)
             Cached inner loop: 3 * x_0 + 42 >= 0
             Cached next-to-inner loop: 3 * x_0 + 7 * x_1 + 35 >= 0"""
    def satisfied_as_equalities(self, inner_loop_variable) -> frozenset:
        """InequalityCollection.satisfied_as_equalities(self, inner_loop_variable) -> frozenset

        File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 1356)

        Return the inequalities (by their index) that are satisfied as
        equalities.

        INPUT:

        - ``inner_loop_variable`` -- integer; the 0th coordinate of
          the lattice point

        OUTPUT:

        A set of integers in ascending order. Each integer is the
        index of a H-representation object of the polyhedron (either a
        inequality or an equation).

        EXAMPLES::

            sage: from sage.geometry.integral_points import InequalityCollection
            sage: quadrant = Polyhedron(rays=[(1,0), (0,1)])
            sage: ieqs = InequalityCollection(quadrant, [0,1], [-1]*2, [1]*2 )
            sage: ieqs.prepare_next_to_inner_loop([-1,0])
            sage: ieqs.prepare_inner_loop([-1,0])
            sage: ieqs.satisfied_as_equalities(-1)
            frozenset({1})
            sage: ieqs.satisfied_as_equalities(0)
            frozenset({0, 1})
            sage: ieqs.satisfied_as_equalities(1)
            frozenset({1})"""
    def swap_ineq_to_front(self, inti) -> Any:
        """InequalityCollection.swap_ineq_to_front(self, int i)

        File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 1283)

        Swap the ``i``-th entry of the list to the front of the list of inequalities.

        INPUT:

        - ``i`` -- integer; the :class:`Inequality_int` to swap to the
          beginning of the list of integral inequalities

        EXAMPLES::

            sage: from sage.geometry.integral_points import InequalityCollection
            sage: P_QQ = Polyhedron(identity_matrix(3).columns() + [(-2, -1,-1)], base_ring=QQ)
            sage: iec = InequalityCollection(P_QQ, [0,1,2], [0]*3,[1]*3)
            sage: iec
            The collection of inequalities
            integer: (3, -2, -2) x + 2 >= 0
            integer: (-1, 4, -1) x + 1 >= 0
            integer: (-1, -1, 4) x + 1 >= 0
            integer: (-1, -1, -1) x + 1 >= 0
            sage: iec.swap_ineq_to_front(3)
            sage: iec
            The collection of inequalities
            integer: (-1, -1, -1) x + 1 >= 0
            integer: (3, -2, -2) x + 2 >= 0
            integer: (-1, 4, -1) x + 1 >= 0
            integer: (-1, -1, 4) x + 1 >= 0"""

class Inequality_generic:
    """File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 716)

        An inequality whose coefficients are arbitrary Python/Sage objects

        INPUT:

        - ``A`` -- list of coefficients

        - ``b`` -- element

        OUTPUT: inequality `A x + b \\geq 0`

        EXAMPLES::

            sage: from sage.geometry.integral_points import Inequality_generic
            sage: Inequality_generic([2 * pi, sqrt(3), 7/2], -5.5)                          # needs sage.symbolic
            generic: (2*pi, sqrt(3), 7/2) x + -5.50000000000000 >= 0
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Inequality_int:
    """File: /build/sagemath/src/sage/src/sage/geometry/integral_points.pxi (starting at line 823)

        Fast version of inequality in the case that all coefficients fit
        into machine ints.

        INPUT:

        - ``A`` -- list of integers

        - ``b`` -- integer

        - ``max_abs_coordinates`` -- the maximum of the coordinates that
          one wants to evaluate the coordinates on; used for overflow
          checking

        OUTPUT:

        Inequality `A x + b \\geq 0`. A :exc:`OverflowError` is raised if a
        machine integer is not long enough to hold the results. A
        :exc:`ValueError` is raised if some of the input is not integral.

        EXAMPLES::

            sage: from sage.geometry.integral_points import Inequality_int
            sage: Inequality_int([2,3,7], -5, [10]*3)
            integer: (2, 3, 7) x + -5 >= 0

            sage: Inequality_int([1]*21, -5, [10]*21)
            Traceback (most recent call last):
            ...
            OverflowError: Dimension limit exceeded.

            sage: Inequality_int([2,3/2,7], -5, [10]*3)
            Traceback (most recent call last):
            ...
            ValueError: Not integral.

            sage: Inequality_int([2,3,7], -5.2, [10]*3)
            Traceback (most recent call last):
            ...
            ValueError: Not integral.

            sage: Inequality_int([2,3,7], -5*10^50, [10]*3)  # actual error message can differ between 32 and 64 bit
            Traceback (most recent call last):
            ...
            OverflowError: ...

        TESTS:

        Check that :issue:`21993` is fixed::

            sage: Inequality_int([18560500, -89466500], 108027, [178933, 37121])
            Traceback (most recent call last):
            ...
            OverflowError: ...
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
