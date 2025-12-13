from _typeshed import Incomplete
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.geometry.polyhedron.backend_cdd import Polyhedron_QQ_cdd as Polyhedron_QQ_cdd
from sage.geometry.polyhedron.backend_field import Polyhedron_field as Polyhedron_field
from sage.geometry.polyhedron.backend_normaliz import Polyhedron_QQ_normaliz as Polyhedron_QQ_normaliz
from sage.geometry.polyhedron.backend_polymake import Polyhedron_polymake as Polyhedron_polymake
from sage.geometry.polyhedron.backend_ppl import Polyhedron_QQ_ppl as Polyhedron_QQ_ppl
from sage.geometry.polyhedron.parent import Polyhedra as Polyhedra, Polyhedra_QQ_cdd as Polyhedra_QQ_cdd, Polyhedra_QQ_normaliz as Polyhedra_QQ_normaliz, Polyhedra_QQ_ppl as Polyhedra_QQ_ppl, Polyhedra_base as Polyhedra_base, Polyhedra_field as Polyhedra_field, Polyhedra_polymake as Polyhedra_polymake
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

ancestors_of_associahedron: Incomplete

def Associahedron(cartan_type, backend: str = 'ppl'):
    """
    Construct an associahedron.

    The generalized associahedron is a polytopal complex with vertices in
    one-to-one correspondence with clusters in the cluster complex, and with
    edges between two vertices if and only if the associated two clusters
    intersect in codimension 1.

    The associahedron of type `A_n` is one way to realize the classical
    associahedron as defined in the :wikipedia:`Associahedron`.

    A polytopal realization of the associahedron can be found in [CFZ2002]_. The
    implementation is based on [CFZ2002]_, Theorem 1.5, Remark 1.6, and Corollary
    1.9.

    INPUT:

    - ``cartan_type`` -- a cartan type according to
      :class:`sage.combinat.root_system.cartan_type.CartanTypeFactory`

    - ``backend`` -- string (``'ppl'``); the backend to use;
      see :meth:`sage.geometry.polyhedron.constructor.Polyhedron`

    EXAMPLES::

        sage: Asso = polytopes.associahedron(['A',2]); Asso
        Generalized associahedron of type ['A', 2] with 5 vertices

        sage: sorted(Asso.Hrepresentation(), key=repr)
        [An inequality (-1, 0) x + 1 >= 0,
         An inequality (0, -1) x + 1 >= 0,
         An inequality (0, 1) x + 1 >= 0,
         An inequality (1, 0) x + 1 >= 0,
         An inequality (1, 1) x + 1 >= 0]

        sage: Asso.Vrepresentation()
        (A vertex at (1, -1), A vertex at (1, 1), A vertex at (-1, 1),
         A vertex at (-1, 0), A vertex at (0, -1))

        sage: polytopes.associahedron(['B',2])
        Generalized associahedron of type ['B', 2] with 6 vertices

    The two pictures of [CFZ2002]_ can be recovered with::

        sage: Asso = polytopes.associahedron(['A',3]); Asso
        Generalized associahedron of type ['A', 3] with 14 vertices
        sage: Asso.plot()  # long time
        Graphics3d Object

        sage: Asso = polytopes.associahedron(['B',3]); Asso
        Generalized associahedron of type ['B', 3] with 20 vertices
        sage: Asso.plot()  # long time
        Graphics3d Object

    TESTS::

        sage: sorted(polytopes.associahedron(['A',3]).vertices())
        [A vertex at (-3/2, 0, -1/2), A vertex at (-3/2, 0, 3/2),
         A vertex at (-3/2, 1, -3/2), A vertex at (-3/2, 2, -3/2),
         A vertex at (-3/2, 2, 3/2), A vertex at (-1/2, -1, -1/2),
         A vertex at (-1/2, 0, -3/2), A vertex at (1/2, -2, 1/2),
         A vertex at (1/2, -2, 3/2), A vertex at (3/2, -2, 1/2),
         A vertex at (3/2, -2, 3/2), A vertex at (3/2, 0, -3/2),
         A vertex at (3/2, 2, -3/2), A vertex at (3/2, 2, 3/2)]

        sage: sorted(polytopes.associahedron(['B',3]).vertices())
        [A vertex at (-3, 0, 0), A vertex at (-3, 0, 3),
         A vertex at (-3, 2, -2), A vertex at (-3, 4, -3),
         A vertex at (-3, 5, -3), A vertex at (-3, 5, 3),
         A vertex at (-2, 1, -2), A vertex at (-2, 3, -3),
         A vertex at (-1, -2, 0), A vertex at (-1, -1, -1),
         A vertex at (1, -4, 1), A vertex at (1, -3, 0),
         A vertex at (2, -5, 2), A vertex at (2, -5, 3),
         A vertex at (3, -5, 2), A vertex at (3, -5, 3),
         A vertex at (3, -3, 0), A vertex at (3, 3, -3),
         A vertex at (3, 5, -3), A vertex at (3, 5, 3)]

        sage: polytopes.associahedron(['A',4]).f_vector()
        (1, 42, 84, 56, 14, 1)
        sage: polytopes.associahedron(['B',4]).f_vector()
        (1, 70, 140, 90, 20, 1)

        sage: p1 = polytopes.associahedron(['A',4], backend='normaliz')   # optional - pynormaliz
        sage: TestSuite(p1).run(skip='_test_pickling')                    # optional - pynormaliz
        sage: p2 = polytopes.associahedron(['A',4], backend='cdd')
        sage: TestSuite(p2).run()
        sage: p3 = polytopes.associahedron(['A',4], backend='field')
        sage: TestSuite(p3).run()
    """

class Associahedron_class_base:
    """
    The base class of the Python class of an associahedron

    You should use the :func:`Associahedron` convenience function to
    construct associahedra from the Cartan type.

    TESTS::

        sage: Asso = polytopes.associahedron(['A',2]); Asso
        Generalized associahedron of type ['A', 2] with 5 vertices
        sage: TestSuite(Asso).run()
    """
    def __new__(typ, parent=None, Vrep=None, Hrep=None, cartan_type=None, **kwds):
        """
        Return instance of :class:`Assciahedron_class_base`, if ``cartan_type`` is provided
        or object is being unpickled.

        In other cases, this call is a result of a polyhedral construction with an associahedron.
        Thus we return the corresponding instance of
        :class:`sage.geometry.polyhedron.base.Polyhedron_base` (not an associahedron).

        TESTS:

        Check that faces of associahedra work::

            sage: A = polytopes.associahedron(['A',3], backend='ppl'); A
            Generalized associahedron of type ['A', 3] with 14 vertices
            sage: face = A.faces(2)[3]
            sage: P = face.as_polyhedron(); P
            A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 4 vertices
            sage: P.backend()
            'ppl'
            sage: A = polytopes.associahedron(['A',3], backend='field'); A
            Generalized associahedron of type ['A', 3] with 14 vertices
            sage: A.faces(2)[3].as_polyhedron().backend()
            'field'

        Check other polytopal constructions::

            sage: A = polytopes.associahedron(['A',4], backend='ppl')
            sage: A + A
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 42 vertices
            sage: A - A
            A 0-dimensional polyhedron in QQ^4 defined as the convex hull of 1 vertex
            sage: A.intersection(A)
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 42 vertices
            sage: A.translation(A.center())
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 42 vertices
            sage: A.dilation(2)
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 42 vertices
            sage: A.dilation(2.0)
            A 4-dimensional polyhedron in RDF^4 defined as the convex hull of 42 vertices
            sage: A.convex_hull(A)
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 42 vertices
            sage: A.polar()
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 14 vertices
        """
    def __init__(self, parent, Vrep, Hrep, cartan_type=None, **kwds) -> None:
        """
        Initialize an associahedron.

        If ``'cartan_type'`` is ``None``, :meth:`Associahedron_class_base.__new__`
        returns a (general) polyhedron instead.

        TESTS::

            sage: A = polytopes.associahedron(['A',3], backend='ppl'); A
            Generalized associahedron of type ['A', 3] with 14 vertices
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: polytopes.associahedron(['A',3]).cartan_type()
            ['A', 3]
        """
    def vertices_in_root_space(self):
        """
        Return the vertices of ``self`` as elements in the root space.

        EXAMPLES::

            sage: Asso = polytopes.associahedron(['A',2])
            sage: Asso.vertices()
            (A vertex at (1, -1), A vertex at (1, 1),
             A vertex at (-1, 1), A vertex at (-1, 0),
             A vertex at (0, -1))

            sage: Asso.vertices_in_root_space()
            (alpha[1] - alpha[2], alpha[1] + alpha[2], -alpha[1] + alpha[2],
            -alpha[1], -alpha[2])
        """

class Associahedron_class_ppl(Associahedron_class_base, Polyhedron_QQ_ppl): ...
class Associahedron_class_normaliz(Associahedron_class_base, Polyhedron_QQ_normaliz): ...
class Associahedron_class_cdd(Associahedron_class_base, Polyhedron_QQ_cdd): ...
class Associahedron_class_polymake(Associahedron_class_base, Polyhedron_polymake): ...
class Associahedron_class_field(Associahedron_class_base, Polyhedron_field): ...

def Associahedra(base_ring, ambient_dim, backend: str = 'ppl'):
    """
    Construct a parent class of Associahedra according to ``backend``.

    TESTS::

        sage: from sage.combinat.root_system.associahedron import Associahedra
        sage: Associahedra(QQ, 4, 'ppl').parent()
        <class 'sage.combinat.root_system.associahedron.Associahedra_ppl_with_category'>
        sage: Associahedra(QQ, 4, 'normaliz').parent() # optional - pynormaliz
        <class 'sage.combinat.root_system.associahedron.Associahedra_normaliz_with_category'>
        sage: Associahedra(QQ, 4, 'polymake').parent() # optional - jupymake
        <class 'sage.combinat.root_system.associahedron.Associahedra_polymake_with_category'>
        sage: Associahedra(QQ, 4, 'field').parent()
        <class 'sage.combinat.root_system.associahedron.Associahedra_field_with_category'>
        sage: Associahedra(QQ, 4, 'cdd').parent()
        <class 'sage.combinat.root_system.associahedron.Associahedra_cdd_with_category'>

    .. SEEALSO::

        :class:`Associahedra_base`.
    """

class Associahedra_base:
    """
    Base class of parent of Associahedra of specified dimension

    EXAMPLES::

        sage: from sage.combinat.root_system.associahedron import Associahedra
        sage: parent = Associahedra(QQ,2,'ppl');  parent
        Polyhedra in QQ^2
        sage: type(parent)
        <class 'sage.combinat.root_system.associahedron.Associahedra_ppl_with_category'>
        sage: parent(['A',2])
        Generalized associahedron of type ['A', 2] with 5 vertices

    Importantly, the parent knows the dimension of the ambient
    space. If you try to construct an associahedron of a different
    dimension, a :exc:`ValueError` is raised::

        sage: parent(['A',3])
        Traceback (most recent call last):
        ...
        ValueError: V-representation data requires a list of length ambient_dim
    """

class Associahedra_ppl(Associahedra_base, Polyhedra_QQ_ppl):
    Element = Associahedron_class_ppl

class Associahedra_normaliz(Associahedra_base, Polyhedra_QQ_normaliz):
    Element = Associahedron_class_normaliz

class Associahedra_cdd(Associahedra_base, Polyhedra_QQ_cdd):
    Element = Associahedron_class_cdd

class Associahedra_polymake(Associahedra_base, Polyhedra_polymake):
    Element = Associahedron_class_polymake

class Associahedra_field(Associahedra_base, Polyhedra_field):
    Element = Associahedron_class_field
