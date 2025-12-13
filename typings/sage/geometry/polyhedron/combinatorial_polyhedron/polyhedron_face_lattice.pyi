from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.geometry.polyhedron.combinatorial_polyhedron.conversions import facets_tuple_to_bit_rep_of_Vrep as facets_tuple_to_bit_rep_of_Vrep, facets_tuple_to_bit_rep_of_facets as facets_tuple_to_bit_rep_of_facets
from typing import Any, ClassVar

class PolyhedronFaceLattice:
    """PolyhedronFaceLattice(CombinatorialPolyhedron C)

    File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/polyhedron_face_lattice.pyx (starting at line 76)

    A class to generate incidences of :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`.

    On initialization all faces of the given :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`
    are added and sorted (except coatoms). The incidences can be used to
    generate the ``face_lattice``.

    Might generate the faces of the dual polyhedron for speed.

    INPUT:

    - :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.baseCombinatorialPolyhedron`

    .. SEEALSO::

        :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron._record_all_faces`,
        :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron._record_all_faces_helper`,
        :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron.face_lattice`,
        :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron._compute_face_lattice_incidences`.

    EXAMPLES::

        sage: P = polytopes.Birkhoff_polytope(3)
        sage: C = CombinatorialPolyhedron(P)
        sage: C._record_all_faces()  # indirect doctests
        sage: C.face_lattice()                                                          # needs sage.combinat
        Finite lattice containing 50 elements

    ALGORITHM:

    The faces are recorded with :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator` in Bit-representation.
    Once created, all level-sets but the coatoms are sorted with merge sort.
    Non-trivial incidences of elements whose rank differs by 1 are determined
    by intersecting with all coatoms. Then each intersection is looked up in
    the sorted level sets."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    dual: File
    def __init__(self, CombinatorialPolyhedronC) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/polyhedron_face_lattice.pyx (starting at line 205)

                Initialize :class:`PolyhedronFaceLattice`.

                See :class:`PolyhedronFaceLattice`.

                EXAMPLES::

                    sage: P = polytopes.cube()
                    sage: C = CombinatorialPolyhedron(P)
                    sage: C._record_all_faces() # indirect doctests
                    sage: C.face_lattice()                                                      # needs sage.combinat
                    Finite lattice containing 28 elements

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.polyhedron_face_lattice.PolyhedronFaceLattice).run()
        """
    def get_face(self, intdimension, size_tindex) -> CombinatorialFace:
        """PolyhedronFaceLattice.get_face(self, int dimension, size_t index) -> CombinatorialFace

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/polyhedron_face_lattice.pyx (starting at line 316)

        Return the face of dimension ``dimension`` and index ``index``.

        INPUT:

        - ``dimension`` -- dimension of the face
        - ``index`` -- index of the face
        - ``names`` -- if ``True`` returns the names of the ``[vertices, rays, lines]``
          as given on initialization of :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.polyhedron_face_lattice \\\n            ....:         import PolyhedronFaceLattice
            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: F = PolyhedronFaceLattice(C)
            sage: it = C.face_generator(dimension=1)
            sage: face = next(it)
            sage: index = F._find_face_from_combinatorial_face(face)
            sage: F.get_face(face.dimension(), index).ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 3), A vertex at (1, 2, 4, 3))
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 3), A vertex at (1, 2, 4, 3))
            sage: all(F.get_face(face.dimension(),
            ....:                F._find_face_from_combinatorial_face(face)).ambient_Vrepresentation() ==
            ....:     face.ambient_Vrepresentation() for face in it)
            True

            sage: P = polytopes.twenty_four_cell()
            sage: C = CombinatorialPolyhedron(P)
            sage: F = PolyhedronFaceLattice(C)
            sage: it = C.face_generator()
            sage: face = next(it)
            sage: while (face.dimension() == 3): face = next(it)
            sage: index = F._find_face_from_combinatorial_face(face)
            sage: F.get_face(face.dimension(), index).ambient_Vrepresentation()
            (A vertex at (-1/2, 1/2, -1/2, -1/2),
             A vertex at (-1/2, 1/2, 1/2, -1/2),
             A vertex at (0, 0, 0, -1))
            sage: all(F.get_face(face.dimension(),
            ....:                F._find_face_from_combinatorial_face(face)).ambient_V_indices() ==
            ....:     face.ambient_V_indices() for face in it)
            True"""
