from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class ListOfFaces:
    """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 101)

        A class to store the Bit-representation of faces in.

        This class will allocate the memory for the faces.

        INPUT:

        - ``n_faces`` -- the number of faces to be stored
        - ``n_atoms`` -- the total number of atoms the faces contain
        - ``n_coatoms`` -- the total number of coatoms of the polyhedron

        .. SEEALSO::

            :meth:`incidence_matrix_to_bit_rep_of_facets`,
            :meth:`incidence_matrix_to_bit_rep_of_Vrep`,
            :meth:`facets_tuple_to_bit_rep_of_facets`,
            :meth:`facets_tuple_to_bit_rep_of_Vrep`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: facets = ListOfFaces(5, 13, 5)
            sage: facets.matrix().dimensions()
            (5, 13)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def compute_dimension(self) -> int:
        """ListOfFaces.compute_dimension(self) -> int

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 213)

        Compute the dimension of a polyhedron by its facets.

        This assumes that ``self`` is the list of facets of a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:            facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: Vrep.compute_dimension()
            3

        ALGORITHM:

        This is done by iteration:

        Computes the facets of one of the facets (i.e. the ridges contained in
        one of the facets). Then computes the dimension of the facet, by
        considering its facets.

        Repeats until a face has only one facet. Usually this is a vertex.

        However, in the unbounded case, this might be different. The face with only
        one facet might be a ray or a line. So the correct dimension of a
        polyhedron with one facet is the number of ``[lines, rays, vertices]``
        that the facet contains.

        Hence, we know the dimension of a face, which has only one facet and
        iteratively we know the dimension of entire polyhedron we started from.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import incidence_matrix_to_bit_rep_of_facets, \\\n            ....:            incidence_matrix_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: for _ in range(10):
            ....:     points = tuple(tuple(randint(-1000,1000) for _ in range(10))
            ....:                    for _ in range(randint(3,15)))
            ....:     P = Polyhedron(vertices=points)
            ....:     inc = P.incidence_matrix()
            ....:     mod_inc = inc.delete_columns([i for i,V in enumerate(P.Hrepresentation()) if V.is_equation()])
            ....:     facets = incidence_matrix_to_bit_rep_of_facets(mod_inc)
            ....:     vertices = incidence_matrix_to_bit_rep_of_Vrep(mod_inc)
            ....:     d1 = P.dimension()
            ....:     if d1 == 0:
            ....:         continue
            ....:     d2 = facets.compute_dimension()
            ....:     d3 = vertices.compute_dimension()
            ....:     if not d1 == d2 == d3:
            ....:         print('calculation_dimension() seems to be incorrect')"""
    @overload
    def compute_dimension(self) -> Any:
        """ListOfFaces.compute_dimension(self) -> int

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 213)

        Compute the dimension of a polyhedron by its facets.

        This assumes that ``self`` is the list of facets of a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:            facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: Vrep.compute_dimension()
            3

        ALGORITHM:

        This is done by iteration:

        Computes the facets of one of the facets (i.e. the ridges contained in
        one of the facets). Then computes the dimension of the facet, by
        considering its facets.

        Repeats until a face has only one facet. Usually this is a vertex.

        However, in the unbounded case, this might be different. The face with only
        one facet might be a ray or a line. So the correct dimension of a
        polyhedron with one facet is the number of ``[lines, rays, vertices]``
        that the facet contains.

        Hence, we know the dimension of a face, which has only one facet and
        iteratively we know the dimension of entire polyhedron we started from.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import incidence_matrix_to_bit_rep_of_facets, \\\n            ....:            incidence_matrix_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: for _ in range(10):
            ....:     points = tuple(tuple(randint(-1000,1000) for _ in range(10))
            ....:                    for _ in range(randint(3,15)))
            ....:     P = Polyhedron(vertices=points)
            ....:     inc = P.incidence_matrix()
            ....:     mod_inc = inc.delete_columns([i for i,V in enumerate(P.Hrepresentation()) if V.is_equation()])
            ....:     facets = incidence_matrix_to_bit_rep_of_facets(mod_inc)
            ....:     vertices = incidence_matrix_to_bit_rep_of_Vrep(mod_inc)
            ....:     d1 = P.dimension()
            ....:     if d1 == 0:
            ....:         continue
            ....:     d2 = facets.compute_dimension()
            ....:     d3 = vertices.compute_dimension()
            ....:     if not d1 == d2 == d3:
            ....:         print('calculation_dimension() seems to be incorrect')"""
    @overload
    def compute_dimension(self) -> Any:
        """ListOfFaces.compute_dimension(self) -> int

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 213)

        Compute the dimension of a polyhedron by its facets.

        This assumes that ``self`` is the list of facets of a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:            facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: Vrep.compute_dimension()
            3

        ALGORITHM:

        This is done by iteration:

        Computes the facets of one of the facets (i.e. the ridges contained in
        one of the facets). Then computes the dimension of the facet, by
        considering its facets.

        Repeats until a face has only one facet. Usually this is a vertex.

        However, in the unbounded case, this might be different. The face with only
        one facet might be a ray or a line. So the correct dimension of a
        polyhedron with one facet is the number of ``[lines, rays, vertices]``
        that the facet contains.

        Hence, we know the dimension of a face, which has only one facet and
        iteratively we know the dimension of entire polyhedron we started from.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import incidence_matrix_to_bit_rep_of_facets, \\\n            ....:            incidence_matrix_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: for _ in range(10):
            ....:     points = tuple(tuple(randint(-1000,1000) for _ in range(10))
            ....:                    for _ in range(randint(3,15)))
            ....:     P = Polyhedron(vertices=points)
            ....:     inc = P.incidence_matrix()
            ....:     mod_inc = inc.delete_columns([i for i,V in enumerate(P.Hrepresentation()) if V.is_equation()])
            ....:     facets = incidence_matrix_to_bit_rep_of_facets(mod_inc)
            ....:     vertices = incidence_matrix_to_bit_rep_of_Vrep(mod_inc)
            ....:     d1 = P.dimension()
            ....:     if d1 == 0:
            ....:         continue
            ....:     d2 = facets.compute_dimension()
            ....:     d3 = vertices.compute_dimension()
            ....:     if not d1 == d2 == d3:
            ....:         print('calculation_dimension() seems to be incorrect')"""
    @overload
    def compute_dimension(self) -> Any:
        """ListOfFaces.compute_dimension(self) -> int

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 213)

        Compute the dimension of a polyhedron by its facets.

        This assumes that ``self`` is the list of facets of a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:            facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: Vrep.compute_dimension()
            3

        ALGORITHM:

        This is done by iteration:

        Computes the facets of one of the facets (i.e. the ridges contained in
        one of the facets). Then computes the dimension of the facet, by
        considering its facets.

        Repeats until a face has only one facet. Usually this is a vertex.

        However, in the unbounded case, this might be different. The face with only
        one facet might be a ray or a line. So the correct dimension of a
        polyhedron with one facet is the number of ``[lines, rays, vertices]``
        that the facet contains.

        Hence, we know the dimension of a face, which has only one facet and
        iteratively we know the dimension of entire polyhedron we started from.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import incidence_matrix_to_bit_rep_of_facets, \\\n            ....:            incidence_matrix_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: for _ in range(10):
            ....:     points = tuple(tuple(randint(-1000,1000) for _ in range(10))
            ....:                    for _ in range(randint(3,15)))
            ....:     P = Polyhedron(vertices=points)
            ....:     inc = P.incidence_matrix()
            ....:     mod_inc = inc.delete_columns([i for i,V in enumerate(P.Hrepresentation()) if V.is_equation()])
            ....:     facets = incidence_matrix_to_bit_rep_of_facets(mod_inc)
            ....:     vertices = incidence_matrix_to_bit_rep_of_Vrep(mod_inc)
            ....:     d1 = P.dimension()
            ....:     if d1 == 0:
            ....:         continue
            ....:     d2 = facets.compute_dimension()
            ....:     d3 = vertices.compute_dimension()
            ....:     if not d1 == d2 == d3:
            ....:         print('calculation_dimension() seems to be incorrect')"""
    @overload
    def compute_dimension(self) -> Any:
        """ListOfFaces.compute_dimension(self) -> int

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 213)

        Compute the dimension of a polyhedron by its facets.

        This assumes that ``self`` is the list of facets of a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:            facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: Vrep.compute_dimension()
            3

        ALGORITHM:

        This is done by iteration:

        Computes the facets of one of the facets (i.e. the ridges contained in
        one of the facets). Then computes the dimension of the facet, by
        considering its facets.

        Repeats until a face has only one facet. Usually this is a vertex.

        However, in the unbounded case, this might be different. The face with only
        one facet might be a ray or a line. So the correct dimension of a
        polyhedron with one facet is the number of ``[lines, rays, vertices]``
        that the facet contains.

        Hence, we know the dimension of a face, which has only one facet and
        iteratively we know the dimension of entire polyhedron we started from.

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import incidence_matrix_to_bit_rep_of_facets, \\\n            ....:            incidence_matrix_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: for _ in range(10):
            ....:     points = tuple(tuple(randint(-1000,1000) for _ in range(10))
            ....:                    for _ in range(randint(3,15)))
            ....:     P = Polyhedron(vertices=points)
            ....:     inc = P.incidence_matrix()
            ....:     mod_inc = inc.delete_columns([i for i,V in enumerate(P.Hrepresentation()) if V.is_equation()])
            ....:     facets = incidence_matrix_to_bit_rep_of_facets(mod_inc)
            ....:     vertices = incidence_matrix_to_bit_rep_of_Vrep(mod_inc)
            ....:     d1 = P.dimension()
            ....:     if d1 == 0:
            ....:         continue
            ....:     d2 = facets.compute_dimension()
            ....:     d3 = vertices.compute_dimension()
            ....:     if not d1 == d2 == d3:
            ....:         print('calculation_dimension() seems to be incorrect')"""
    @overload
    def matrix(self) -> Any:
        """ListOfFaces.matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 479)

        Obtain the matrix of ``self``.

        Each row represents a face and each column an atom.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:     facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4), (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.matrix()
            [1 1 0 0 1 0]
            [0 1 1 0 1 0]
            [0 0 1 1 1 0]
            [1 0 0 1 1 0]
            [1 1 0 0 0 1]
            [0 1 1 0 0 1]
            [0 0 1 1 0 1]
            [1 0 0 1 0 1]
            sage: facets.matrix().transpose() == Vrep.matrix()
            True"""
    @overload
    def matrix(self) -> Any:
        """ListOfFaces.matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 479)

        Obtain the matrix of ``self``.

        Each row represents a face and each column an atom.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:     facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4), (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.matrix()
            [1 1 0 0 1 0]
            [0 1 1 0 1 0]
            [0 0 1 1 1 0]
            [1 0 0 1 1 0]
            [1 1 0 0 0 1]
            [0 1 1 0 0 1]
            [0 0 1 1 0 1]
            [1 0 0 1 0 1]
            sage: facets.matrix().transpose() == Vrep.matrix()
            True"""
    @overload
    def matrix(self) -> Any:
        """ListOfFaces.matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 479)

        Obtain the matrix of ``self``.

        Each row represents a face and each column an atom.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets, \\\n            ....:     facets_tuple_to_bit_rep_of_Vrep
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4), (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
            sage: facets.matrix()
            [1 1 0 0 1 0]
            [0 1 1 0 1 0]
            [0 0 1 1 1 0]
            [1 0 0 1 1 0]
            [1 1 0 0 0 1]
            [0 1 1 0 0 1]
            [0 0 1 1 0 1]
            [1 0 0 1 0 1]
            sage: facets.matrix().transpose() == Vrep.matrix()
            True"""
    @overload
    def pyramid(self) -> ListOfFaces:
        """ListOfFaces.pyramid(self) -> ListOfFaces

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 306)

        Return the list of faces of the pyramid.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:         import facets_tuple_to_bit_rep_of_facets
            sage: facets = ((0,1,2), (0,1,3), (0,2,3), (1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 0]
            [1 1 0 1]
            [1 0 1 1]
            [0 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 0 1]
            [1 1 0 1 1]
            [1 0 1 1 1]
            [0 1 1 1 1]
            [1 1 1 1 0]

        Incorrect facets that illustrate how this method works::

            sage: facets = ((0,1,2,3), (0,1,2,3), (0,1,2,3), (0,1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 0]

        ::

            sage: facets = ((), (), (), ())
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            sage: face_list.pyramid().matrix()
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [1 1 1 1 0]"""
    @overload
    def pyramid(self) -> Any:
        """ListOfFaces.pyramid(self) -> ListOfFaces

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 306)

        Return the list of faces of the pyramid.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:         import facets_tuple_to_bit_rep_of_facets
            sage: facets = ((0,1,2), (0,1,3), (0,2,3), (1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 0]
            [1 1 0 1]
            [1 0 1 1]
            [0 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 0 1]
            [1 1 0 1 1]
            [1 0 1 1 1]
            [0 1 1 1 1]
            [1 1 1 1 0]

        Incorrect facets that illustrate how this method works::

            sage: facets = ((0,1,2,3), (0,1,2,3), (0,1,2,3), (0,1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 0]

        ::

            sage: facets = ((), (), (), ())
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            sage: face_list.pyramid().matrix()
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [1 1 1 1 0]"""
    @overload
    def pyramid(self) -> Any:
        """ListOfFaces.pyramid(self) -> ListOfFaces

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 306)

        Return the list of faces of the pyramid.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:         import facets_tuple_to_bit_rep_of_facets
            sage: facets = ((0,1,2), (0,1,3), (0,2,3), (1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 0]
            [1 1 0 1]
            [1 0 1 1]
            [0 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 0 1]
            [1 1 0 1 1]
            [1 0 1 1 1]
            [0 1 1 1 1]
            [1 1 1 1 0]

        Incorrect facets that illustrate how this method works::

            sage: facets = ((0,1,2,3), (0,1,2,3), (0,1,2,3), (0,1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 0]

        ::

            sage: facets = ((), (), (), ())
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            sage: face_list.pyramid().matrix()
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [1 1 1 1 0]"""
    @overload
    def pyramid(self) -> Any:
        """ListOfFaces.pyramid(self) -> ListOfFaces

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 306)

        Return the list of faces of the pyramid.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:         import facets_tuple_to_bit_rep_of_facets
            sage: facets = ((0,1,2), (0,1,3), (0,2,3), (1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 0]
            [1 1 0 1]
            [1 0 1 1]
            [0 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 0 1]
            [1 1 0 1 1]
            [1 0 1 1 1]
            [0 1 1 1 1]
            [1 1 1 1 0]

        Incorrect facets that illustrate how this method works::

            sage: facets = ((0,1,2,3), (0,1,2,3), (0,1,2,3), (0,1,2,3))
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]
            sage: face_list.pyramid().matrix()
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 1]
            [1 1 1 1 0]

        ::

            sage: facets = ((), (), (), ())
            sage: face_list = facets_tuple_to_bit_rep_of_facets(facets, 4)
            sage: face_list.matrix()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            sage: face_list.pyramid().matrix()
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [0 0 0 0 1]
            [1 1 1 1 0]"""
    def __copy__(self) -> ListOfFaces:
        """ListOfFaces.__copy__(self) -> ListOfFaces

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx (starting at line 181)

        Return a copy of ``self``.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces \\\n            ....:     import ListOfFaces
            sage: facets = ListOfFaces(5, 13, 5)
            sage: copy(facets).matrix().dimensions()
            (5, 13)

        TESTS::

            sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n            ....:     import facets_tuple_to_bit_rep_of_facets
            sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
            ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
            sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
            sage: facets.compute_dimension()
            3
            sage: copy(facets).compute_dimension()
            3
            sage: facets.matrix() == copy(facets).matrix()
            True
            sage: copy(facets) is facets
            False"""
