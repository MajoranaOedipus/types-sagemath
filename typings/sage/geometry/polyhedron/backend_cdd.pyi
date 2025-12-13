from .base import Polyhedron_base as Polyhedron_base
from .base_QQ import Polyhedron_QQ as Polyhedron_QQ
from sage.features.cddlib import CddExecutable as CddExecutable
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ

class Polyhedron_cdd(Polyhedron_base):
    """
    Base class for the cdd backend.
    """

class Polyhedron_QQ_cdd(Polyhedron_cdd, Polyhedron_QQ):
    """
    Polyhedra over QQ with cdd.

    INPUT:

    - ``parent`` -- the parent, an instance of
      :class:`~sage.geometry.polyhedron.parent.Polyhedra`

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: parent = Polyhedra(QQ, 2, backend='cdd')
        sage: from sage.geometry.polyhedron.backend_cdd import Polyhedron_QQ_cdd
        sage: Polyhedron_QQ_cdd(parent, [ [(1,0),(0,1),(0,0)], [], []], None, verbose=False)
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 3 vertices

    TESTS:

    Check that :issue:`19803` is fixed::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: P_cdd = Polyhedra(QQ, 3, 'cdd')
        sage: P_cdd([[],[],[]], None)
        The empty polyhedron in QQ^3
        sage: Polyhedron(vertices=[], backend='cdd', base_ring=QQ)
        The empty polyhedron in QQ^0
    """
    def __init__(self, parent, Vrep, Hrep, **kwds) -> None:
        """
        The Python constructor.

        See :class:`Polyhedron_base` for a description of the input
        data.

        TESTS::

            sage: p = Polyhedron(backend='cdd', base_ring=QQ)
            sage: type(p)
            <class 'sage.geometry.polyhedron.parent.Polyhedra_QQ_cdd_with_category.element_class'>
            sage: TestSuite(p).run()
        """
