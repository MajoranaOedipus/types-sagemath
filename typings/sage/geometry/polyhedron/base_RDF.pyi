from .base import Polyhedron_base as Polyhedron_base
from sage.rings.real_double import RDF as RDF

class Polyhedron_RDF(Polyhedron_base):
    """
    Base class for polyhedra over ``RDF``.

    TESTS::

        sage: p = Polyhedron([(0,0)], base_ring=RDF);  p
        A 0-dimensional polyhedron in RDF^2 defined as the convex hull of 1 vertex
        sage: TestSuite(p).run()
    """
