import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.geometry.polyhedron.face import PolyhedronFace as PolyhedronFace, combinatorial_face_to_polyhedral_face as combinatorial_face_to_polyhedral_face
from sage.misc.lazy_import import LazyImport as LazyImport
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class FaceIterator(FaceIterator_base):
    """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1315)

        A class to iterate over all combinatorial faces of a polyhedron.

        Construct all proper faces from the facets. In dual mode, construct all proper
        faces from the vertices. Dual will be faster for less vertices than facets.

        INPUT:

        - ``C`` -- a :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`
        - ``dual`` -- if ``True``, then dual polyhedron is used for iteration
          (only possible for bounded Polyhedra)
        - ``output_dimension`` -- if not ``None``, then the face iterator will only yield
          faces of this dimension

        .. SEEALSO::

            :class:`FaceIterator`,
            :class:`FaceIterator_geom`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`.

        EXAMPLES:

        Construct a face iterator::

            sage: P = polytopes.cuboctahedron()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron

        Construct faces by the dual or not::

            sage: it = C.face_generator(algorithm='primal')
            sage: next(it).dimension()
            2

            sage: it = C.face_generator(algorithm='dual')
            sage: next(it).dimension()
            0

        For unbounded polyhedra only non-dual iteration is possible::

            sage: P = Polyhedron(rays=[[0,0,1], [0,1,0], [1,0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: [face.ambient_Vrepresentation() for face in it]
            [(A vertex at (0, 0, 0),
              A ray in the direction (0, 1, 0),
              A ray in the direction (1, 0, 0)),
             (A vertex at (0, 0, 0),
              A ray in the direction (0, 0, 1),
              A ray in the direction (1, 0, 0)),
             (A vertex at (0, 0, 0),
              A ray in the direction (0, 0, 1),
              A ray in the direction (0, 1, 0)),
             (A vertex at (0, 0, 0), A ray in the direction (1, 0, 0)),
             (A vertex at (0, 0, 0), A ray in the direction (0, 1, 0)),
             (A vertex at (0, 0, 0),),
             (A vertex at (0, 0, 0), A ray in the direction (0, 0, 1))]
            sage: it = C.face_generator(algorithm='dual')
            Traceback (most recent call last):
            ...
            ValueError: dual algorithm only available for bounded polyhedra

        Construct a face iterator only yielding dimension `2` faces::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: counter = 0
            sage: for _ in it: counter += 1
            sage: print ('permutahedron(5) has', counter,
            ....:        'faces of dimension 2')
            permutahedron(5) has 150 faces of dimension 2
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

        In non-dual mode one can ignore all faces contained in the current face::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: face = next(it)
            sage: face.ambient_H_indices()
            (5,)
            sage: it.ignore_subfaces()
            sage: [face.ambient_H_indices() for face in it]
            [(4,),
             (3,),
             (2,),
             (1,),
             (0,),
             (3, 4),
             (1, 4),
             (0, 4),
             (1, 3, 4),
             (0, 1, 4),
             (2, 3),
             (1, 3),
             (1, 2, 3),
             (1, 2),
             (0, 2),
             (0, 1, 2),
             (0, 1)]

            sage: it = C.face_generator(algorithm='dual')
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        In dual mode one can ignore all faces that contain the current face::

            sage: it = C.face_generator(algorithm='dual')
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: face = next(it)
            sage: face.ambient_V_indices()
            (6,)
            sage: [face.ambient_V_indices() for face in it]
            [(5,),
             (4,),
             (3,),
             (2,),
             (1,),
             (0,),
             (6, 7),
             (4, 7),
             (2, 7),
             (4, 5, 6, 7),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (5, 6),
             (1, 6),
             (0, 1, 5, 6),
             (4, 5),
             (0, 5),
             (0, 3, 4, 5),
             (3, 4),
             (2, 3),
             (0, 3),
             (0, 1, 2, 3),
             (1, 2),
             (0, 1)]

            sage: it = C.face_generator(algorithm='primal')
            sage: next(it)
            A 2-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: it.ignore_supfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when in dual mode

        ALGORITHM:

        The algorithm to visit all proper faces exactly once is roughly
        equivalent to the following. A (slightly generalized) description of the
        algorithm can be found in [KS2019]_.

        Initialization::

            faces = [set(facet) for facet in P.facets()]
            face_iterator(faces, [])

        The function ``face_iterator`` is defined recursively. It visits all faces of
        the polyhedron `P`, except those contained in any of ``visited_all``.
        It assumes ``faces`` to be exactly those facets of `P`
        that are not contained in any of the ``visited_all``.
        It assumes ``visited_all`` to be some list of faces of
        a polyhedron `P_2`, which contains `P` as one of its faces::

            def face_iterator(faces, visited_all):
                while facets:
                    one_face = faces.pop()
                    maybe_new_faces = [one_face.intersection(face) for face in faces]
            ...

        At this point we claim that ``maybe_new_faces`` contains all facets of ``one_face``,
        which we have not visited before.

        Proof: Let `F` be a facet of ``one_face``. We have a chain:
        `P \\supset{}` ``one_face`` `{}\\supset F`.
        By the diamond property, there exists a ``second_face`` with
        `P \\supset{}` ``second_face`` `{}\\supset F`.

        Now either ``second_face`` is not an element of ``faces``:
        Hence ``second_face`` is contained in one of ``visited_all``.
        In particular, `F` is contained in ``visited_all``.

        Or ``second_face`` is an element of ``faces``:
        Then, intersecting ``one_face`` with ``second_face`` gives ``F``.

        This concludes the proof.

        Moreover, if an element in ``maybe_new_faces`` is inclusion-maximal
        and not contained in any of the ``visited_all``, it is a facet of ``one_face``.
        Any facet in ``maybe_new_faces`` of ``one_face`` is inclusion-maximal.

        Hence, in the following loop, an element ``face1`` in ``maybe_new_faces``
        is a facet of ``one_face`` if and only if it is not contained in another facet::

            ...
                    maybe_new_faces2 = []
                    for i, face1 in enumerate(maybe_new_faces):
                        if (all(not face1 < face2 for face2 in maybe_new_faces[:i])
                                and all(not face1 <= face2 for face2 in maybe_new_faces[i+1:])):
                            maybe_new_faces2.append(face1)
            ...

        Now ``maybe_new_faces2`` contains only facets of ``one_face``
        and some faces contained in any of ``visited_all``.
        It also contains all the facets not contained in any of ``visited_all``.

        We construct ``new_faces`` as the list of all facets of ``one_face``
        not contained in any of ``visited_all``::

            ...
                    new_faces = []
                    for face1 in maybe_new_faces2:
                        if all(not face1 < face2 for face2 in visited_all):
                            new_faces.append(face1)
            ...

        By induction we can apply the algorithm, to visit all
        faces of ``one_face`` not contained in ``visited_all``::

            ...
                    face_iterator(new_faces, visited_all)
            ...

        Finally we visit ``one_face`` and add it to ``visited_all``::

            ...
                    visit(one_face)
                    visited_all.append(one_face)

        Note: At this point, we have visited exactly those faces,
        contained in any of the ``visited_all``. The function ends here.


        ALGORITHM for the special case that all intervals of the lattice not
        containing zero are boolean (e.g. when the polyhedron is simple):

        We do not assume any other properties of our lattice in this case.
        Note that intervals of length 2 not containing zero, have exactly 2 elements now.
        But the atom-representation of faces might not be unique.

        We do the following modifications:

        - To check whether an intersection of faces is zero, we check whether the
          atom-representation is zero. Although not unique,
          it works to distinct from zero.

        - The intersection of two (relative) facets has always codimension `1` unless empty.

        - To intersect we now additionally unite the coatom representation.
          This gives the correct representation of the new face
          unless the intersection is zero.

        - To mark a face as visited, we save its coatom representation.

        - To check whether we have seen a face already, we check containment of the coatom representation.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __next__(self) -> Any:
        """FaceIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1604)

        Return the next face.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: [next(it) for _ in range(7)]
            [A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron]"""

class FaceIterator_base(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 196)

        A base class to iterate over all faces of a polyhedron.

        Construct all proper faces from the facets. In dual mode, construct all proper
        faces from the vertices. Dual will be faster for less vertices than facets.

        See :class:`FaceIterator`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    dual: File
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def current(self) -> Any:
        """FaceIterator_base.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 448)

        Retrieve the last value of :meth:`next`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.combinatorial_polyhedron().face_generator()
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: it.current()
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def current(self) -> Any:
        """FaceIterator_base.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 448)

        Retrieve the last value of :meth:`next`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.combinatorial_polyhedron().face_generator()
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: it.current()
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def current(self) -> Any:
        """FaceIterator_base.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 448)

        Retrieve the last value of :meth:`next`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.combinatorial_polyhedron().face_generator()
            sage: next(it)
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: it.current()
            A 0-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def ignore_subfaces(self) -> Any:
        """FaceIterator_base.ignore_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 508)

        The iterator will not visit any faces of the current face.

        Only possible when not in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: n_non_simplex_faces = 1
            sage: for face in it:
            ....:     if face.n_ambient_Vrepresentation() > face.dimension() + 1:
            ....:         n_non_simplex_faces += 1
            ....:     else:
            ....:         it.ignore_subfaces()
            ....:
            sage: n_non_simplex_faces
            127

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Ignoring the same face as was requested to visit only consumes the iterator::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.only_subfaces()
            sage: it.ignore_subfaces()
            sage: list(it)
            []

        Face iterator must be set to a face first::

            sage: it = C.face_generator(algorithm='primal')
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet"""
    @overload
    def ignore_subfaces(self) -> Any:
        """FaceIterator_base.ignore_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 508)

        The iterator will not visit any faces of the current face.

        Only possible when not in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: n_non_simplex_faces = 1
            sage: for face in it:
            ....:     if face.n_ambient_Vrepresentation() > face.dimension() + 1:
            ....:         n_non_simplex_faces += 1
            ....:     else:
            ....:         it.ignore_subfaces()
            ....:
            sage: n_non_simplex_faces
            127

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Ignoring the same face as was requested to visit only consumes the iterator::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.only_subfaces()
            sage: it.ignore_subfaces()
            sage: list(it)
            []

        Face iterator must be set to a face first::

            sage: it = C.face_generator(algorithm='primal')
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet"""
    @overload
    def ignore_subfaces(self) -> Any:
        """FaceIterator_base.ignore_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 508)

        The iterator will not visit any faces of the current face.

        Only possible when not in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: n_non_simplex_faces = 1
            sage: for face in it:
            ....:     if face.n_ambient_Vrepresentation() > face.dimension() + 1:
            ....:         n_non_simplex_faces += 1
            ....:     else:
            ....:         it.ignore_subfaces()
            ....:
            sage: n_non_simplex_faces
            127

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Ignoring the same face as was requested to visit only consumes the iterator::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.only_subfaces()
            sage: it.ignore_subfaces()
            sage: list(it)
            []

        Face iterator must be set to a face first::

            sage: it = C.face_generator(algorithm='primal')
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet"""
    @overload
    def ignore_subfaces(self) -> Any:
        """FaceIterator_base.ignore_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 508)

        The iterator will not visit any faces of the current face.

        Only possible when not in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: n_non_simplex_faces = 1
            sage: for face in it:
            ....:     if face.n_ambient_Vrepresentation() > face.dimension() + 1:
            ....:         n_non_simplex_faces += 1
            ....:     else:
            ....:         it.ignore_subfaces()
            ....:
            sage: n_non_simplex_faces
            127

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Ignoring the same face as was requested to visit only consumes the iterator::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.only_subfaces()
            sage: it.ignore_subfaces()
            sage: list(it)
            []

        Face iterator must be set to a face first::

            sage: it = C.face_generator(algorithm='primal')
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet"""
    @overload
    def ignore_subfaces(self) -> Any:
        """FaceIterator_base.ignore_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 508)

        The iterator will not visit any faces of the current face.

        Only possible when not in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='primal')
            sage: n_non_simplex_faces = 1
            sage: for face in it:
            ....:     if face.n_ambient_Vrepresentation() > face.dimension() + 1:
            ....:         n_non_simplex_faces += 1
            ....:     else:
            ....:         it.ignore_subfaces()
            ....:
            sage: n_non_simplex_faces
            127

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Ignoring the same face as was requested to visit only consumes the iterator::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.only_subfaces()
            sage: it.ignore_subfaces()
            sage: list(it)
            []

        Face iterator must be set to a face first::

            sage: it = C.face_generator(algorithm='primal')
            sage: it.ignore_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet"""
    @overload
    def ignore_supfaces(self) -> Any:
        """FaceIterator_base.ignore_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 559)

        The iterator will not visit any faces containing the current face.

        Only possible when in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='dual')
            sage: n_faces_with_non_simplex_quotient = 1
            sage: for face in it:
            ....:     n_facets = face.n_ambient_Hrepresentation(add_equations=False)
            ....:     if n_facets > C.dimension() - face.dimension() + 1:
            ....:         n_faces_with_non_simplex_quotient += 1
            ....:     else:
            ....:         it.ignore_supfaces()
            ....:
            sage: n_faces_with_non_simplex_quotient
            4845

        Face iterator must be in dual mode::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.ignore_supfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when in dual mode"""
    @overload
    def ignore_supfaces(self) -> Any:
        """FaceIterator_base.ignore_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 559)

        The iterator will not visit any faces containing the current face.

        Only possible when in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='dual')
            sage: n_faces_with_non_simplex_quotient = 1
            sage: for face in it:
            ....:     n_facets = face.n_ambient_Hrepresentation(add_equations=False)
            ....:     if n_facets > C.dimension() - face.dimension() + 1:
            ....:         n_faces_with_non_simplex_quotient += 1
            ....:     else:
            ....:         it.ignore_supfaces()
            ....:
            sage: n_faces_with_non_simplex_quotient
            4845

        Face iterator must be in dual mode::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.ignore_supfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when in dual mode"""
    @overload
    def ignore_supfaces(self) -> Any:
        """FaceIterator_base.ignore_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 559)

        The iterator will not visit any faces containing the current face.

        Only possible when in dual mode.

        EXAMPLES::

            sage: P = polytopes.Gosset_3_21()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(algorithm='dual')
            sage: n_faces_with_non_simplex_quotient = 1
            sage: for face in it:
            ....:     n_facets = face.n_ambient_Hrepresentation(add_equations=False)
            ....:     if n_facets > C.dimension() - face.dimension() + 1:
            ....:         n_faces_with_non_simplex_quotient += 1
            ....:     else:
            ....:         it.ignore_supfaces()
            ....:
            sage: n_faces_with_non_simplex_quotient
            4845

        Face iterator must be in dual mode::

            sage: it = C.face_generator(algorithm='primal')
            sage: _ = next(it)
            sage: it.ignore_supfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when in dual mode"""
    @overload
    def join_of_Vrep(self, *indices) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def join_of_Vrep(self) -> Any:
        """FaceIterator_base.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 685)

        Construct the join of the Vrepresentatives indicated by the indices.

        This is the smallest face containing all Vrepresentatives with the given indices.

        The iterator must be reset if not newly initialized.

        .. NOTE::

            In the case of unbounded polyhedra, the smallest face containing given Vrepresentatives
            may not be well defined.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (0, 1, 2, 3)
            sage: it.join_of_Vrep(1,5).ambient_V_indices()
            (0, 1, 5, 6)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.join_of_Vrep().ambient_V_indices()
            ()
            sage: it.join_of_Vrep(1,3).ambient_V_indices()
            (1, 3)
            sage: it.join_of_Vrep(1,2).ambient_V_indices()
            (1, 2)
            sage: it.join_of_Vrep(1,6).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: it.join_of_Vrep(8)
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.join_of_Vrep(1,10)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.join_of_Vrep(1,10).ambient_V_indices()
            (1, 10)

        In the case of an unbounded polyhedron, we try to make sense of the input::

            sage: P = polytopes.cube()*Polyhedron(lines=[[1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0, 1)
            A 1-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 1 vertex and 1 line
            sage: it.join_of_Vrep(0)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined

            sage: P = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1)
            A 0-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(2)
            Traceback (most recent call last):
            ...
            ValueError: the join is not well-defined
            sage: it.join_of_Vrep(0,2)
            A 1-dimensional face of a Polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray

            sage: P = Polyhedron(rays=[[1,0], [0,1]])
            sage: it = P.face_generator()
            sage: it.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: it.join_of_Vrep(1,2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^1
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.Vrepresentation()
            (A line in the direction (1, 1), A vertex at (0, 0))
            sage: P.join_of_Vrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.join_of_Vrep(1)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 0], [0, 1]])
            sage: P.join_of_Vrep()
            A -1-dimensional face of a Polyhedron in ZZ^2
            sage: P.join_of_Vrep(0)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: P.join_of_Vrep(0, 1, 2)
            A 2-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines"""
    @overload
    def meet_of_Hrep(self, *indices) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """FaceIterator_base.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 594)

        Construct the meet of the facets indicated by the indices.

        This is the largest face contained in all facets with the given indices.

        The iterator must be reset if not newly initialized.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep(1,2)
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 3)
            sage: it.meet_of_Hrep(1,5).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)

            sage: P = polytopes.cross_polytope(4)
            sage: it = P.face_generator()
            sage: it.meet_of_Hrep().ambient_H_indices()
            ()
            sage: it.meet_of_Hrep(1,3).ambient_H_indices()
            (1, 2, 3, 4)
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,6).ambient_H_indices()
            (1, 6)
            sage: it.meet_of_Hrep(1,2,6).ambient_H_indices()
            (1, 2, 6, 7)
            sage: it.meet_of_Hrep(1,2,5,6).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)

            sage: s = cones.schur(4)
            sage: C = CombinatorialPolyhedron(s)
            sage: it = C.face_generator()
            sage: it.meet_of_Hrep(1,2).ambient_H_indices()
            (1, 2)
            sage: it.meet_of_Hrep(1,2,3).ambient_H_indices()
            Traceback (most recent call last):
            ...
            IndexError: coatoms out of range

        If the iterator has already been used, it must be reset before::

            sage: # needs sage.groups sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it).ambient_V_indices()
            (15, 16, 17, 18, 19)
            sage: it.meet_of_Hrep(9,11)
            Traceback (most recent call last):
            ...
            ValueError: please reset the face iterator
            sage: it.reset()
            sage: it.meet_of_Hrep(9,11).ambient_H_indices()
            (9, 11)

        TESTS:

        Check that things work fine, if the face iterator was never properly initialized::

            sage: P = Polyhedron()
            sage: P.meet_of_Hrep()
            A -1-dimensional face of a Polyhedron in ZZ^0
            sage: P = Polyhedron([[0,0]])
            sage: P.meet_of_Hrep()
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P.meet_of_Hrep(0)
            A 0-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P = Polyhedron(lines=[[1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^1 defined as the convex hull of 1 vertex and 1 line
            sage: P = Polyhedron(lines=[[1, 1]])
            sage: P.meet_of_Hrep()
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
            sage: P.meet_of_Hrep(0)
            A 1-dimensional face of a Polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line"""
    def next(self, *args, **kwargs):
        """FaceIterator_base.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 429)

        Must be implemented by a derived class.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator \\\n            ....:         import FaceIterator_base
            sage: P = polytopes.octahedron()
            sage: C = CombinatorialPolyhedron(P)
            sage: next(FaceIterator_base(C, False))
            Traceback (most recent call last):
            ...
            NotImplementedError: a derived class must implement this"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_subfaces(self) -> Any:
        """FaceIterator_base.only_subfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1076)

        The iterator will visit all (remaining) subfaces of the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_H_indices()
            ()
            sage: next(it).ambient_H_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_H_indices()
            (5,)
            sage: next(it).ambient_H_indices()
            (4,)
            sage: it.only_subfaces()
            sage: list(f.ambient_H_indices() for f in it)
            [(4, 5), (3, 4), (1, 4), (0, 4), (3, 4, 5), (0, 4, 5), (1, 3, 4), (0, 1, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_H_indices(add_equations=False)
            (15,)
            sage: next(it).ambient_H_indices(add_equations=False)
            (14,)
            sage: it.only_subfaces()
            sage: all(14 in f.ambient_H_indices() for f in it)
            True

        Face iterator needs to be set to a face first::

            sage: it = C.face_generator()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: iterator not set to a face yet

        Face iterator must not be in dual mode::

            sage: it = C.face_generator(algorithm='dual')
            sage: _ = next(it)
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: only possible when not in dual mode

        Cannot run ``only_subfaces`` after ``ignore_subfaces``::

            sage: it = C.face_generator()
            sage: _ = next(it)
            sage: it.ignore_subfaces()
            sage: it.only_subfaces()
            Traceback (most recent call last):
            ...
            ValueError: cannot only visit subsets after ignoring a face"""
    @overload
    def only_supfaces(self) -> Any:
        """FaceIterator_base.only_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1140)

        The iterator will visit all (remaining) faces
        containing the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(3)
            sage: it = P.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (5,)
            sage: next(it).ambient_V_indices()
            (4,)
            sage: it.only_supfaces()
            sage: list(f.ambient_V_indices() for f in it)
            [(4, 5), (3, 4), (2, 4), (0, 4), (3, 4, 5), (2, 4, 5), (0, 3, 4), (0, 2, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='dual')
            sage: next(it).ambient_V_indices()
            (23,)
            sage: next(it).ambient_V_indices()
            (22,)
            sage: it.only_supfaces()
            sage: all(22 in f.ambient_V_indices() for f in it)
            True"""
    @overload
    def only_supfaces(self) -> Any:
        """FaceIterator_base.only_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1140)

        The iterator will visit all (remaining) faces
        containing the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(3)
            sage: it = P.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (5,)
            sage: next(it).ambient_V_indices()
            (4,)
            sage: it.only_supfaces()
            sage: list(f.ambient_V_indices() for f in it)
            [(4, 5), (3, 4), (2, 4), (0, 4), (3, 4, 5), (2, 4, 5), (0, 3, 4), (0, 2, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='dual')
            sage: next(it).ambient_V_indices()
            (23,)
            sage: next(it).ambient_V_indices()
            (22,)
            sage: it.only_supfaces()
            sage: all(22 in f.ambient_V_indices() for f in it)
            True"""
    @overload
    def only_supfaces(self) -> Any:
        """FaceIterator_base.only_supfaces(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1140)

        The iterator will visit all (remaining) faces
        containing the current face and then terminate.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(3)
            sage: it = P.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (5,)
            sage: next(it).ambient_V_indices()
            (4,)
            sage: it.only_supfaces()
            sage: list(f.ambient_V_indices() for f in it)
            [(4, 5), (3, 4), (2, 4), (0, 4), (3, 4, 5), (2, 4, 5), (0, 3, 4), (0, 2, 4)]

        ::

            sage: P = polytopes.Birkhoff_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='dual')
            sage: next(it).ambient_V_indices()
            (23,)
            sage: next(it).ambient_V_indices()
            (22,)
            sage: it.only_supfaces()
            sage: all(22 in f.ambient_V_indices() for f in it)
            True"""
    @overload
    def reset(self) -> Any:
        """FaceIterator_base.reset(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 370)

        Reset the iterator.

        The iterator will start with the first face again.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)
            sage: it.reset()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)

        TESTS:

        Resetting will fix the order of the coatoms after ``only_subsets``::

            sage: P = polytopes.Birkhoff_polytope(3)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='primal')
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (7,)
            sage: it.only_subfaces()
            sage: it.reset()
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)"""
    @overload
    def reset(self) -> Any:
        """FaceIterator_base.reset(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 370)

        Reset the iterator.

        The iterator will start with the first face again.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)
            sage: it.reset()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)

        TESTS:

        Resetting will fix the order of the coatoms after ``only_subsets``::

            sage: P = polytopes.Birkhoff_polytope(3)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='primal')
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (7,)
            sage: it.only_subfaces()
            sage: it.reset()
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)"""
    @overload
    def reset(self) -> Any:
        """FaceIterator_base.reset(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 370)

        Reset the iterator.

        The iterator will start with the first face again.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)
            sage: it.reset()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)

        TESTS:

        Resetting will fix the order of the coatoms after ``only_subsets``::

            sage: P = polytopes.Birkhoff_polytope(3)
            sage: C = P.combinatorial_polyhedron()
            sage: it = C.face_generator(algorithm='primal')
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (7,)
            sage: it.only_subfaces()
            sage: it.reset()
            sage: face = next(it)
            sage: face.ambient_H_indices(add_equations=False)
            (8,)"""
    def __iter__(self) -> Any:
        """FaceIterator_base.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 467)

        EXAMPLES::

            sage: P = polytopes.simplex()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: [d for d in it]
            [A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron]"""
    def __next__(self) -> Any:
        """FaceIterator_base.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 429)

        Must be implemented by a derived class.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator \\\n            ....:         import FaceIterator_base
            sage: P = polytopes.octahedron()
            sage: C = CombinatorialPolyhedron(P)
            sage: next(FaceIterator_base(C, False))
            Traceback (most recent call last):
            ...
            NotImplementedError: a derived class must implement this"""
    def __reduce__(self) -> Any:
        """FaceIterator_base.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 492)

        Override __reduce__ to indicate that pickle/unpickle will not work.

        EXAMPLES::

            sage: P = polytopes.simplex()
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator()
            sage: it1 = loads(it.dumps())
            Traceback (most recent call last):
            ...
            NotImplementedError"""

class FaceIterator_geom(FaceIterator_base):
    """FaceIterator_geom(P, dual=None, output_dimension=None)

    File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1629)

    A class to iterate over all geometric faces of a polyhedron.

    Construct all faces from the facets. In dual mode, construct all
    faces from the vertices. Dual will be faster for less vertices than facets.

    INPUT:

    - ``P`` -- an instance of :class:`~sage.geometry.polyhedron.base.Polyhedron_base`
    - ``dual`` -- if ``True``, then dual polyhedron is used for iteration
      (only possible for bounded Polyhedra)
    - ``output_dimension`` -- if not ``None``, then the FaceIterator will only yield
      faces of this dimension

    EXAMPLES:

    Construct a geometric face iterator::

        sage: P = polytopes.cuboctahedron()
        sage: it = P.face_generator()
        sage: next(it)
        A 3-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 12 vertices

    Construct faces by the dual or not::

        sage: it = P.face_generator(algorithm='primal')
        sage: _ = next(it), next(it)
        sage: next(it).dim()
        2

        sage: it = P.face_generator(algorithm='dual')
        sage: _ = next(it), next(it)
        sage: next(it).dim()
        0

    For unbounded polyhedra only non-dual iteration is possible::

        sage: P = Polyhedron(rays=[[0,0,1], [0,1,0], [1,0,0]])
        sage: it = P.face_generator()
        sage: [face.ambient_Vrepresentation() for face in it]
        [(A vertex at (0, 0, 0),
          A ray in the direction (0, 0, 1),
          A ray in the direction (0, 1, 0),
          A ray in the direction (1, 0, 0)),
         (),
         (A vertex at (0, 0, 0),
          A ray in the direction (0, 1, 0),
          A ray in the direction (1, 0, 0)),
         (A vertex at (0, 0, 0),
          A ray in the direction (0, 0, 1),
          A ray in the direction (1, 0, 0)),
         (A vertex at (0, 0, 0),
          A ray in the direction (0, 0, 1),
          A ray in the direction (0, 1, 0)),
         (A vertex at (0, 0, 0), A ray in the direction (1, 0, 0)),
         (A vertex at (0, 0, 0), A ray in the direction (0, 1, 0)),
         (A vertex at (0, 0, 0),),
         (A vertex at (0, 0, 0), A ray in the direction (0, 0, 1))]
        sage: it = P.face_generator(algorithm='dual')
        Traceback (most recent call last):
        ...
        ValueError: cannot iterate over dual of unbounded Polyedron

    Construct a FaceIterator only yielding dimension `2` faces::

        sage: P = polytopes.permutahedron(5)
        sage: it = P.face_generator(face_dimension=2)
        sage: counter = 0
        sage: for _ in it: counter += 1
        sage: print ('permutahedron(5) has', counter,
        ....:        'faces of dimension 2')
        permutahedron(5) has 150 faces of dimension 2
        sage: P.f_vector()
        (1, 120, 240, 150, 30, 1)

    In non-dual mode one can ignore all faces contained in the current face::

        sage: P = polytopes.cube()
        sage: it = P.face_generator(algorithm='primal')
        sage: _ = next(it), next(it)
        sage: face = next(it)
        sage: face.ambient_H_indices()
        (5,)
        sage: it.ignore_subfaces()
        sage: [face.ambient_H_indices() for face in it]
        [(4,),
         (3,),
         (2,),
         (1,),
         (0,),
         (3, 4),
         (1, 4),
         (0, 4),
         (1, 3, 4),
         (0, 1, 4),
         (2, 3),
         (1, 3),
         (1, 2, 3),
         (1, 2),
         (0, 2),
         (0, 1, 2),
         (0, 1)]

        sage: it = P.face_generator(algorithm='dual')
        sage: _ = next(it), next(it)
        sage: next(it)
        A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
        sage: it.ignore_subfaces()
        Traceback (most recent call last):
        ...
        ValueError: only possible when not in dual mode

    In dual mode one can ignore all faces that contain the current face::

        sage: P = polytopes.cube()
        sage: it = P.face_generator(algorithm='dual')
        sage: _ = next(it), next(it)
        sage: next(it)
        A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
        sage: face = next(it)
        sage: face.ambient_V_indices()
        (6,)
        sage: [face.ambient_V_indices() for face in it]
        [(5,),
         (4,),
         (3,),
         (2,),
         (1,),
         (0,),
         (6, 7),
         (4, 7),
         (2, 7),
         (4, 5, 6, 7),
         (1, 2, 6, 7),
         (2, 3, 4, 7),
         (5, 6),
         (1, 6),
         (0, 1, 5, 6),
         (4, 5),
         (0, 5),
         (0, 3, 4, 5),
         (3, 4),
         (2, 3),
         (0, 3),
         (0, 1, 2, 3),
         (1, 2),
         (0, 1)]

        sage: it = P.face_generator(algorithm='primal')
        sage: _ = next(it), next(it)
        sage: next(it)
        A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices
        sage: it.ignore_supfaces()
        Traceback (most recent call last):
        ...
        ValueError: only possible when in dual mode

    .. SEEALSO::

        :class:`FaceIterator_base`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    P: File
    def __init__(self, P, dual=..., output_dimension=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1791)

                Initialize :class:`FaceIterator_base`.

                See :class:`FaceIterator_base`.

                EXAMPLES::

                    sage: P = polytopes.permutahedron(4)
                    sage: it = P.face_generator()  # indirect doctest
                    sage: it
                    Iterator over the faces of a 3-dimensional polyhedron in ZZ^4
                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator_geom).run()
        """
    @overload
    def current(self) -> Any:
        """FaceIterator_geom.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1908)

        Retrieve the last value of :meth:`__next__`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.current()
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def current(self) -> Any:
        """FaceIterator_geom.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1908)

        Retrieve the last value of :meth:`__next__`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.current()
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def current(self) -> Any:
        """FaceIterator_geom.current(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1908)

        Retrieve the last value of :meth:`__next__`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: it = P.face_generator()
            sage: _ = next(it), next(it)
            sage: next(it)
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: it.current()
            A 0-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 1 vertex
            sage: next(it).ambient_V_indices() == it.current().ambient_V_indices()
            True"""
    @overload
    def reset(self) -> Any:
        """FaceIterator_geom.reset(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1810)

        Reset the iterator.

        The iterator will start with the first face again.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)
            sage: it.reset()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)"""
    @overload
    def reset(self) -> Any:
        """FaceIterator_geom.reset(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1810)

        Reset the iterator.

        The iterator will start with the first face again.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)
            sage: it.reset()
            sage: next(it).ambient_V_indices()
            (0, 1, 2, 3, 4, 5, 6, 7)
            sage: next(it).ambient_V_indices()
            ()
            sage: next(it).ambient_V_indices()
            (0, 3, 4, 5)"""
    def __next__(self) -> Any:
        """FaceIterator_geom.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx (starting at line 1869)

        Return the next face.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: it = P.face_generator()
            sage: [next(it) for _ in range(7)]
            [A 3-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 8 vertices,
             A -1-dimensional face of a Polyhedron in ZZ^3,
             A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices,
             A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices,
             A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices,
             A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices,
             A 2-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 4 vertices]"""
