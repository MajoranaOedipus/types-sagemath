from sage.features.databases import DatabaseReflexivePolytopes as DatabaseReflexivePolytopes
from sage.features.palp import PalpExecutable as PalpExecutable
from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL as LatticePolytope_PPL
from sage.interfaces.process import terminate as terminate
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class PALPreader(SageObject):
    """
    Read PALP database of polytopes.

    INPUT:

    - ``dim`` -- integer; the dimension of the polyhedra

    - ``data_basename`` -- string or ``None`` (default). The directory
      and database base filename (PALP usually uses ``'zzdb'``) name
      containing the PALP database to read. Defaults to the built-in
      database location.

    - ``output`` -- string. How to return the reflexive polyhedron
      data. Allowed values = ``'list'``, ``'Polyhedron'`` (default),
      ``'pointcollection'``, and ``'PPL'``. Case is ignored.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.palp_database import PALPreader
        sage: polygons = PALPreader(2)
        sage: [ (p.n_Vrepresentation(), len(p.integral_points())) for p in polygons ]
        [(3, 4), (3, 10), (3, 5), (3, 9), (3, 7), (4, 6), (4, 8), (4, 9),
         (4, 5), (4, 5), (4, 9), (4, 7), (5, 8), (5, 6), (5, 7), (6, 7)]

        sage: next(iter(PALPreader(2, output='list')))
        [[1, 0], [0, 1], [-1, -1]]
        sage: type(_)
        <... 'list'>

        sage: next(iter(PALPreader(2, output='Polyhedron')))
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
        sage: type(_)
        <class 'sage.geometry.polyhedron.parent.Polyhedra_ZZ_ppl_with_category.element_class'>

        sage: next(iter(PALPreader(2, output='PPL')))
        A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
        sage: type(_)
        <class 'sage.geometry.polyhedron.ppl_lattice_polygon.LatticePolygon_PPL_class'>

        sage: next(iter(PALPreader(2, output='PointCollection')))
        [ 1,  0],
        [ 0,  1],
        [-1, -1]
        in Ambient free module of rank 2 over the principal ideal domain Integer Ring
        sage: type(_)
        <class 'sage.geometry.point_collection.PointCollection'>
    """
    def __init__(self, dim, data_basename=None, output: str = 'Polyhedron') -> None:
        """
        The Python constructor.

        See :class:`PALPreader` for documentation.

        TESTS::

            sage: from sage.geometry.polyhedron.palp_database import PALPreader
            sage: polygons = PALPreader(2)
        """
    def __iter__(self):
        """
        Iterate over all polytopes.

        OUTPUT: an iterator for all polytopes

        TESTS::

            sage: from sage.geometry.polyhedron.palp_database import PALPreader
            sage: polygons = PALPreader(2)
            sage: polygons.__iter__()
            <generator object ..._iterate_Polyhedron at 0x...>
        """
    def __getitem__(self, item):
        """
        Return the polytopes(s) indexed by ``item``.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.palp_database import PALPreader
            sage: palp = PALPreader(3)
            sage: list(palp[10:30:10])
            [A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices,
             A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices]
        """

class Reflexive4dHodge(PALPreader):
    """
    Read the PALP database for Hodge numbers of 4d polytopes.

    The database is very large and not installed by default. You can
    install it with the shell command ``sage -i polytopes_db_4d``.

    INPUT:

    - ``h11``, ``h21`` -- integer; the Hodge numbers of the reflexive
      polytopes to list

    Any additional keyword arguments are passed to
    :class:`PALPreader`.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.palp_database import Reflexive4dHodge
        sage: ref = Reflexive4dHodge(1,101)             # optional - polytopes_db_4d
        sage: next(iter(ref)).Vrepresentation()         # optional - polytopes_db_4d
        (A vertex at (-1, -1, -1, -1), A vertex at (0, 0, 0, 1),
         A vertex at (0, 0, 1, 0), A vertex at (0, 1, 0, 0), A vertex at (1, 0, 0, 0))
    """
    def __init__(self, h11, h21, data_basename=None, **kwds) -> None:
        """
        The Python constructor.

        See :class:`Reflexive4dHodge` for documentation.

        TESTS::

            sage: from sage.geometry.polyhedron.palp_database import Reflexive4dHodge
            sage: Reflexive4dHodge(1,101)  # optional - polytopes_db_4d
            <sage.geometry.polyhedron.palp_database.Reflexive4dHodge object at ...>
        """
