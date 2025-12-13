import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class CombinatorialFace(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 84)

        A class of the combinatorial type of a polyhedral face.

        EXAMPLES:

        Obtain a combinatorial face from a face iterator::

            sage: P = polytopes.cyclic_polytope(5,8)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it)
            A 0-dimensional face of a 5-dimensional combinatorial polyhedron

        Obtain a combinatorial face from an index of the face lattice::

            sage: F = C.face_lattice()                                                      # needs sage.combinat
            sage: F._elements[3]                                                            # needs sage.combinat
            34
            sage: C.face_by_face_lattice_index(29)
            A 1-dimensional face of a 5-dimensional combinatorial polyhedron

        Obtain the dimension of a combinatorial face::

            sage: face = next(it)
            sage: face.dimension()
            0

        The dimension of the polyhedron::

            sage: face.ambient_dimension()
            5

        The Vrepresentation::

            sage: face.ambient_Vrepresentation()
            (A vertex at (6, 36, 216, 1296, 7776),)
            sage: face.ambient_V_indices()
            (6,)
            sage: face.n_ambient_Vrepresentation()
            1

        The Hrepresentation::

            sage: face.ambient_Hrepresentation()
            (An inequality (60, -112, 65, -14, 1) x + 0 >= 0,
             An inequality (180, -216, 91, -16, 1) x + 0 >= 0,
             An inequality (360, -342, 119, -18, 1) x + 0 >= 0,
             An inequality (840, -638, 179, -22, 1) x + 0 >= 0,
             An inequality (-2754, 1175, -245, 25, -1) x + 2520 >= 0,
             An inequality (504, -450, 145, -20, 1) x + 0 >= 0,
             An inequality (-1692, 853, -203, 23, -1) x + 1260 >= 0,
             An inequality (252, -288, 113, -18, 1) x + 0 >= 0,
             An inequality (-844, 567, -163, 21, -1) x + 420 >= 0,
             An inequality (84, -152, 83, -16, 1) x + 0 >= 0,
             An inequality (-210, 317, -125, 19, -1) x + 0 >= 0)
            sage: face.ambient_H_indices()
            (3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19)
            sage: face.n_ambient_Hrepresentation()
            11
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def ambient_H_indices(self, add_equations=...) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self, add_equations=...) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self, add_equations=...) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self, add_equations=...) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self, add_equations=...) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_H_indices(self) -> Any:
        """CombinatorialFace.ambient_H_indices(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 746)

        Return the indices of the Hrepresentation objects
        of the ambient polyhedron defining the face.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to include the equations

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (28, 29)
            sage: face2 = next(it)
            sage: face2.ambient_H_indices(add_equations=False)
            (25, 29)

        Add the indices of the equation::

            sage: face.ambient_H_indices(add_equations=True)                            # needs sage.combinat
            (28, 29, 30)
            sage: face2.ambient_H_indices(add_equations=True)                           # needs sage.combinat
            (25, 29, 30)

        Another example::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: _ = next(it); _ = next(it)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 4, 5, 7)
            sage: next(it).ambient_H_indices()
            (0, 1, 5, 6, 7, 8)
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 6, 8)
            sage: [next(it).dimension() for _ in range(2)]
            [0, 1]
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (4, 5, 7)

        .. SEEALSO::

            :meth:`ambient_Hrepresentation`."""
    @overload
    def ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 686)

        Return the Hrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the facets/inequalities that contain the face
        and the equations defining the ambient polyhedron.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (1, 1, 1, 0, 0) x - 6 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (30, -31, 10, -1) x + 0 >= 0,
             An inequality (10, -17, 8, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-50, 35, -10, 1) x + 24 >= 0,
             An inequality (-12, 19, -8, 1) x + 0 >= 0,
             An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)

        .. SEEALSO::

            :meth:`ambient_H_indices`."""
    @overload
    def ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 686)

        Return the Hrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the facets/inequalities that contain the face
        and the equations defining the ambient polyhedron.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (1, 1, 1, 0, 0) x - 6 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (30, -31, 10, -1) x + 0 >= 0,
             An inequality (10, -17, 8, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-50, 35, -10, 1) x + 24 >= 0,
             An inequality (-12, 19, -8, 1) x + 0 >= 0,
             An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)

        .. SEEALSO::

            :meth:`ambient_H_indices`."""
    @overload
    def ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 686)

        Return the Hrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the facets/inequalities that contain the face
        and the equations defining the ambient polyhedron.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (1, 1, 1, 0, 0) x - 6 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (30, -31, 10, -1) x + 0 >= 0,
             An inequality (10, -17, 8, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-50, 35, -10, 1) x + 24 >= 0,
             An inequality (-12, 19, -8, 1) x + 0 >= 0,
             An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)

        .. SEEALSO::

            :meth:`ambient_H_indices`."""
    @overload
    def ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 686)

        Return the Hrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the facets/inequalities that contain the face
        and the equations defining the ambient polyhedron.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (1, 1, 1, 0, 0) x - 6 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (30, -31, 10, -1) x + 0 >= 0,
             An inequality (10, -17, 8, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-50, 35, -10, 1) x + 24 >= 0,
             An inequality (-12, 19, -8, 1) x + 0 >= 0,
             An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)

        .. SEEALSO::

            :meth:`ambient_H_indices`."""
    @overload
    def ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 686)

        Return the Hrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the facets/inequalities that contain the face
        and the equations defining the ambient polyhedron.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (1, 1, 1, 0, 0) x - 6 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (30, -31, 10, -1) x + 0 >= 0,
             An inequality (10, -17, 8, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)
            sage: next(it).ambient_Hrepresentation()
            (An inequality (-50, 35, -10, 1) x + 24 >= 0,
             An inequality (-12, 19, -8, 1) x + 0 >= 0,
             An inequality (-20, 29, -10, 1) x + 0 >= 0,
             An inequality (60, -47, 12, -1) x + 0 >= 0,
             An inequality (-154, 71, -14, 1) x + 120 >= 0,
             An inequality (-78, 49, -12, 1) x + 40 >= 0)

        .. SEEALSO::

            :meth:`ambient_H_indices`."""
    @overload
    def ambient_V_indices(self) -> Any:
        """CombinatorialFace.ambient_V_indices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 609)

        Return the indices of the Vrepresentation
        objects of the ambient polyhedron defining the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: next(it).ambient_V_indices()
            (32, 91, 92, 93, 94, 95)
            sage: next(it).ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_V_indices())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_Vrepresentation`."""
    @overload
    def ambient_V_indices(self) -> Any:
        """CombinatorialFace.ambient_V_indices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 609)

        Return the indices of the Vrepresentation
        objects of the ambient polyhedron defining the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: next(it).ambient_V_indices()
            (32, 91, 92, 93, 94, 95)
            sage: next(it).ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_V_indices())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_Vrepresentation`."""
    @overload
    def ambient_V_indices(self) -> Any:
        """CombinatorialFace.ambient_V_indices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 609)

        Return the indices of the Vrepresentation
        objects of the ambient polyhedron defining the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: next(it).ambient_V_indices()
            (32, 91, 92, 93, 94, 95)
            sage: next(it).ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_V_indices())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_Vrepresentation`."""
    @overload
    def ambient_V_indices(self) -> Any:
        """CombinatorialFace.ambient_V_indices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 609)

        Return the indices of the Vrepresentation
        objects of the ambient polyhedron defining the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: next(it).ambient_V_indices()
            (32, 91, 92, 93, 94, 95)
            sage: next(it).ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_V_indices())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_Vrepresentation`."""
    @overload
    def ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 541)

        Return the Vrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the vertices/rays/lines
        that face contains.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_Vrepresentation())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_V_indices`."""
    @overload
    def ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 541)

        Return the Vrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the vertices/rays/lines
        that face contains.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_Vrepresentation())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_V_indices`."""
    @overload
    def ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 541)

        Return the Vrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the vertices/rays/lines
        that face contains.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_Vrepresentation())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_V_indices`."""
    @overload
    def ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 541)

        Return the Vrepresentation objects of the ambient polyhedron
        defining the face.

        It consists of the vertices/rays/lines
        that face contains.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it)
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: (face.dimension(), face.ambient_Vrepresentation())
            (2, (1, 2, 3))
            (2, (0, 2, 3))
            (2, (0, 1, 3))
            (2, (0, 1, 2))
            (1, (2, 3))
            (1, (1, 3))
            (1, (1, 2))
            (0, (3,))
            (0, (2,))
            (0, (1,))
            (1, (0, 3))
            (1, (0, 2))
            (0, (0,))
            (1, (0, 1))

        .. SEEALSO::

            :meth:`ambient_V_indices`."""
    @overload
    def ambient_dimension(self) -> Any:
        """CombinatorialFace.ambient_dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 526)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_dimension()
            3"""
    @overload
    def ambient_dimension(self) -> Any:
        """CombinatorialFace.ambient_dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 526)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_dimension()
            3"""
    def as_combinatorial_polyhedron(self, quotient=...) -> Any:
        """CombinatorialFace.as_combinatorial_polyhedron(self, quotient=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 861)

        Return ``self`` as combinatorial polyhedron.

        If ``quotient`` is ``True``, return the quotient of the
        polyhedron by ``self``.
        Let ``G`` be the face corresponding to ``self`` in the dual/polar polytope.
        The ``quotient`` is the dual/polar of ``G``.

        Let `[\\hat{0}, \\hat{1}]` be the face lattice of the ambient polyhedron
        and `F` be ``self`` as element of the face lattice.
        The face lattice of ``self`` as polyhedron corresponds to
        `[\\hat{0}, F]` and the face lattice of the quotient by ``self``
        corresponds to `[F, \\hat{1}]`.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(7,11)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(4)
            sage: f = next(it); f
            A 4-dimensional face of a 7-dimensional combinatorial polyhedron
            sage: F = f.as_combinatorial_polyhedron(); F
            A 4-dimensional combinatorial polyhedron with 5 facets
            sage: F.f_vector()
            (1, 5, 10, 10, 5, 1)
            sage: F_alt = polytopes.cyclic_polytope(4,5).combinatorial_polyhedron()
            sage: F_alt.vertex_facet_graph().is_isomorphic(F.vertex_facet_graph())      # needs sage.graphs
            True

        Obtaining the quotient::

            sage: Q = f.as_combinatorial_polyhedron(quotient=True); Q
            A 2-dimensional combinatorial polyhedron with 6 facets
            sage: Q
            A 2-dimensional combinatorial polyhedron with 6 facets
            sage: Q.f_vector()
            (1, 6, 6, 1)

        The Vrepresentation of the face as polyhedron is given by the
        ambient Vrepresentation of the face in that order::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: F = f.as_combinatorial_polyhedron()
            sage: C.Vrepresentation()
            (A vertex at (1, -1, -1),
            A vertex at (1, 1, -1),
            A vertex at (1, 1, 1),
            A vertex at (1, -1, 1),
            A vertex at (-1, -1, 1),
            A vertex at (-1, -1, -1),
            A vertex at (-1, 1, -1),
            A vertex at (-1, 1, 1))
            sage: f.ambient_Vrepresentation()
            (A vertex at (1, -1, -1),
            A vertex at (1, -1, 1),
            A vertex at (-1, -1, 1),
            A vertex at (-1, -1, -1))
            sage: F.Vrepresentation()
            (0, 1, 2, 3)

        To obtain the facets of the face as polyhedron,
        we compute the meet of each facet with the face.
        The first representative of each element strictly
        contained in the face is kept::

            sage: C.facets(names=False)
            ((0, 1, 2, 3),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (4, 5, 6, 7),
             (0, 1, 5, 6),
             (0, 3, 4, 5))
            sage: F.facets(names=False)
            ((0, 1), (1, 2), (2, 3), (0, 3))

        The Hrepresentation of the quotient by the face is given by the
        ambient Hrepresentation of the face in that order::

            sage: it = C.face_generator(1)
            sage: f = next(it)
            sage: Q = f.as_combinatorial_polyhedron(quotient=True)
            sage: C.Hrepresentation()
            (An inequality (-1, 0, 0) x + 1 >= 0,
            An inequality (0, -1, 0) x + 1 >= 0,
            An inequality (0, 0, -1) x + 1 >= 0,
            An inequality (1, 0, 0) x + 1 >= 0,
            An inequality (0, 0, 1) x + 1 >= 0,
            An inequality (0, 1, 0) x + 1 >= 0)
            sage: f.ambient_Hrepresentation()
            (An inequality (0, 0, 1) x + 1 >= 0, An inequality (0, 1, 0) x + 1 >= 0)
            sage: Q.Hrepresentation()
            (0, 1)

        To obtain the vertices of the face as polyhedron,
        we compute the join of each vertex with the face.
        The first representative of each element strictly
        containing the face is kept::

            sage: [g.ambient_H_indices() for g in C.face_generator(0)]
            [(3, 4, 5),
            (0, 4, 5),
            (2, 3, 5),
            (0, 2, 5),
            (1, 3, 4),
            (0, 1, 4),
            (1, 2, 3),
            (0, 1, 2)]
            sage: [g.ambient_H_indices() for g in Q.face_generator(0)]
            [(1,), (0,)]

        The method is not implemented for unbounded polyhedra::

            sage: P = Polyhedron(rays=[[0,1]])*polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: f.as_combinatorial_polyhedron()
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented for bounded polyhedra

        REFERENCES:

            For more information, see Exercise 2.9 of [Zie2007]_.

        .. NOTE::

            This method is tested in
            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base._test_combinatorial_face_as_combinatorial_polyhedron`."""
    def dim(self) -> Any:
        """CombinatorialFace.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 500)

        Return the dimension of the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.associahedron(['A', 3])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.dimension()
            2

        ``dim`` is an alias::

            sage: face.dim()                                                            # needs sage.combinat
            2"""
    @overload
    def dimension(self) -> Any:
        """CombinatorialFace.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 500)

        Return the dimension of the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.associahedron(['A', 3])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.dimension()
            2

        ``dim`` is an alias::

            sage: face.dim()                                                            # needs sage.combinat
            2"""
    @overload
    def dimension(self) -> Any:
        """CombinatorialFace.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 500)

        Return the dimension of the face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.associahedron(['A', 3])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.dimension()
            2

        ``dim`` is an alias::

            sage: face.dim()                                                            # needs sage.combinat
            2"""
    @overload
    def is_subface(self, CombinatorialFaceother) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face2) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face2) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, v7) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, v7) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face2) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face2) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, face2) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def is_subface(self, other_face) -> Any:
        """CombinatorialFace.is_subface(self, CombinatorialFace other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 380)

        Return whether ``self`` is contained in ``other``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face2 = next(it)
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face.is_subface(face2)
            False
            sage: face2.is_subface(face)
            False
            sage: it.only_subfaces()
            sage: face3 = next(it)
            sage: face3.ambient_V_indices()
            (0, 5)
            sage: face3.is_subface(face2)
            True
            sage: face3.is_subface(face)
            True

        Works for faces of the same combinatorial polyhedron;
        also from different iterators::

            sage: it = C.face_generator(algorithm='dual')
            sage: v7 = next(it); v7.ambient_V_indices()
            (7,)
            sage: v6 = next(it); v6.ambient_V_indices()
            (6,)
            sage: v5 = next(it); v5.ambient_V_indices()
            (5,)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.is_subface(v7)
            False
            sage: v7.is_subface(face)
            False
            sage: v6.is_subface(face)
            False
            sage: v5.is_subface(face)
            True
            sage: face2.ambient_V_indices()
            (0, 1, 5, 6)
            sage: face2.is_subface(v7)
            False
            sage: v7.is_subface(face2)
            False
            sage: v6.is_subface(face2)
            True
            sage: v5.is_subface(face2)
            True

        Only implemented for faces of the same combinatorial polyhedron::

            sage: P1 = polytopes.cube()
            sage: C1 = P1.combinatorial_polyhedron()
            sage: it = C1.face_generator()
            sage: other_face = next(it)
            sage: other_face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: face.ambient_V_indices()
            (0, 3, 4, 5)
            sage: C is C1
            False
            sage: face.is_subface(other_face)
            Traceback (most recent call last):
            ...
            NotImplementedError: is_subface only implemented for faces of the same polyhedron"""
    @overload
    def n_ambient_Hrepresentation(self, add_equations=...) -> Any:
        """CombinatorialFace.n_ambient_Hrepresentation(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 818)

        Return the length of the :meth:`CombinatorialFace.ambient_H_indices`.

        Might be faster than then using ``len``.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to count the equations

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Hrepresentation() == len(face.ambient_Hrepresentation()) for face in it)
            True

        Specifying whether to count the equations or not::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: f.n_ambient_Hrepresentation(add_equations=True)
            3
            sage: f.n_ambient_Hrepresentation(add_equations=False)
            2

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    @overload
    def n_ambient_Hrepresentation(self) -> Any:
        """CombinatorialFace.n_ambient_Hrepresentation(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 818)

        Return the length of the :meth:`CombinatorialFace.ambient_H_indices`.

        Might be faster than then using ``len``.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to count the equations

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Hrepresentation() == len(face.ambient_Hrepresentation()) for face in it)
            True

        Specifying whether to count the equations or not::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: f.n_ambient_Hrepresentation(add_equations=True)
            3
            sage: f.n_ambient_Hrepresentation(add_equations=False)
            2

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    @overload
    def n_ambient_Hrepresentation(self, add_equations=...) -> Any:
        """CombinatorialFace.n_ambient_Hrepresentation(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 818)

        Return the length of the :meth:`CombinatorialFace.ambient_H_indices`.

        Might be faster than then using ``len``.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to count the equations

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Hrepresentation() == len(face.ambient_Hrepresentation()) for face in it)
            True

        Specifying whether to count the equations or not::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: f.n_ambient_Hrepresentation(add_equations=True)
            3
            sage: f.n_ambient_Hrepresentation(add_equations=False)
            2

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    @overload
    def n_ambient_Hrepresentation(self, add_equations=...) -> Any:
        """CombinatorialFace.n_ambient_Hrepresentation(self, add_equations=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 818)

        Return the length of the :meth:`CombinatorialFace.ambient_H_indices`.

        Might be faster than then using ``len``.

        INPUT:

        - ``add_equations`` -- boolean (default: ``True``); whether or not to count the equations

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Hrepresentation() == len(face.ambient_Hrepresentation()) for face in it)
            True

        Specifying whether to count the equations or not::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(2)
            sage: f = next(it)
            sage: f.n_ambient_Hrepresentation(add_equations=True)
            3
            sage: f.n_ambient_Hrepresentation(add_equations=False)
            2

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    @overload
    def n_ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.n_ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 660)

        Return the length of the :meth:`CombinatorialFace.ambient_V_indices`.

        Might be faster than using ``len``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Vrepresentation() == len(face.ambient_Vrepresentation()) for face in it)
            True

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    @overload
    def n_ambient_Vrepresentation(self) -> Any:
        """CombinatorialFace.n_ambient_Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 660)

        Return the length of the :meth:`CombinatorialFace.ambient_V_indices`.

        Might be faster than using ``len``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: all(face.n_ambient_Vrepresentation() == len(face.ambient_Vrepresentation()) for face in it)
            True

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """CombinatorialFace.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 295)

        Return an index for the face.

        This is constructed such that for faces `F,G` constructed in the same manner (same face iterator or face lattice)
        it holds that `F` contained in `G` implies ``hash(F) < hash(G)``.

        If the face was constructed from a :class:`sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
        then this is the index of the occurrence in the iterator.
        In dual mode this value is then deducted from the maximal value of ``size_t``.

        If the face was constructed from
        :meth:`sage:geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron.face_by_face_lattice_index`,
        then this is the total number of faces plus the index in the level set plus the number of lower dimensional faces
        (or higher dimensional faces in dual mode).
        In dual mode this value is then deducted from the maximal value of ``size_t``.

        EXAMPLES::

            sage: P = polytopes.simplex(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: [hash(face) for face in it]
            [1, 2, 3, 4, 5, 6]

        TESTS::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()
            sage: G = F.relabel(C.face_by_face_lattice_index)

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()                                                  # needs sage.combinat
            sage: G = F.relabel(C.face_by_face_lattice_index)                           # needs sage.combinat"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other) -> Any:
        """CombinatorialFace.__lt__(self, other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 335)

        Compare faces of the same polyhedron.

        This is a helper function.
        In order to construct a Hasse diagram (a digraph) with combinatorial faces,
        we must define some order relation that is compatible with the Hasse diagram.

        Any order relation compatible with ordering by dimension is suitable.
        We use :meth:`__hash__` to define the relation.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: F1 = C.face_by_face_lattice_index(0)
            sage: F2 = C.face_by_face_lattice_index(1)
            sage: F1 < F2
            True
            sage: for i,j in Combinations(range(28), 2):
            ....:     F1 = C.face_by_face_lattice_index(i)
            ....:     F2 = C.face_by_face_lattice_index(j)
            ....:     if F1.dim() != F2.dim():
            ....:          assert (F1.dim() < F2.dim()) == (F1 < F2)

            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: F1 = C.face_by_face_lattice_index(0)
            sage: F2 = C.face_by_face_lattice_index(1)
            sage: F1 < F2
            True
            sage: for i,j in Combinations(range(28), 2):
            ....:     F1 = C.face_by_face_lattice_index(i)
            ....:     F2 = C.face_by_face_lattice_index(j)
            ....:     if F1.dim() != F2.dim():
            ....:          assert (F1.dim() < F2.dim()) == (F1 < F2)"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """CombinatorialFace.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx (starting at line 278)

        Override __reduce__ to indicate that pickle/unpickle will not work.

        EXAMPLES::

            sage: P = polytopes.simplex()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: face1 = loads(face.dumps())
            Traceback (most recent call last):
            ...
            NotImplementedError"""
