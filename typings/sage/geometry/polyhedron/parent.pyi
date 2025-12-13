from .representation import Equation as Equation, Inequality as Inequality, Line as Line, Ray as Ray, Vertex as Vertex
from sage.categories.fields import Fields as Fields
from sage.categories.modules import Modules as Modules
from sage.categories.rings import Rings as Rings
from sage.geometry.polyhedron.backend_cdd import Polyhedron_QQ_cdd as Polyhedron_QQ_cdd
from sage.geometry.polyhedron.backend_field import Polyhedron_field as Polyhedron_field
from sage.geometry.polyhedron.backend_normaliz import Polyhedron_QQ_normaliz as Polyhedron_QQ_normaliz, Polyhedron_ZZ_normaliz as Polyhedron_ZZ_normaliz, Polyhedron_normaliz as Polyhedron_normaliz
from sage.geometry.polyhedron.backend_number_field import Polyhedron_number_field as Polyhedron_number_field
from sage.geometry.polyhedron.backend_polymake import Polyhedron_polymake as Polyhedron_polymake
from sage.geometry.polyhedron.backend_ppl import Polyhedron_QQ_ppl as Polyhedron_QQ_ppl, Polyhedron_ZZ_ppl as Polyhedron_ZZ_ppl
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module import FreeModule as FreeModule, FreeModule_generic as FreeModule_generic
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.structure.element import get_coercion_model as get_coercion_model
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def Polyhedra(ambient_space_or_base_ring=None, ambient_dim=None, backend=None, *, ambient_space=None, base_ring=None):
    '''
    Construct a suitable parent class for polyhedra.

    INPUT:

    - ``base_ring`` -- a ring; currently there are backends for `\\ZZ`,
      `\\QQ`, and `\\RDF`

    - ``ambient_dim`` -- integer; the ambient space dimension

    - ``ambient_space`` -- a free module

    - ``backend`` -- string. The name of the backend for computations. There are
      several backends implemented:

        * ``backend="ppl"`` uses the Parma Polyhedra Library

        * ``backend="cdd"`` uses CDD

        * ``backend="normaliz"`` uses normaliz

        * ``backend="polymake"`` uses polymake

        * ``backend="field"`` a generic Sage implementation

    OUTPUT:

    A parent class for polyhedra over the given base ring if the
    backend supports it. If not, the parent base ring can be larger
    (for example, `\\QQ` instead of `\\ZZ`). If there is no
    implementation at all, a :exc:`ValueError` is raised.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: Polyhedra(AA, 3)                                                          # needs sage.rings.number_field
        Polyhedra in AA^3
        sage: Polyhedra(ZZ, 3)
        Polyhedra in ZZ^3
        sage: type(_)
        <class \'sage.geometry.polyhedron.parent.Polyhedra_ZZ_ppl_with_category\'>
        sage: Polyhedra(QQ, 3, backend=\'cdd\')
        Polyhedra in QQ^3
        sage: type(_)
        <class \'sage.geometry.polyhedron.parent.Polyhedra_QQ_cdd_with_category\'>

    CDD does not support integer polytopes directly::

        sage: Polyhedra(ZZ, 3, backend=\'cdd\')
        Polyhedra in QQ^3

    Using a more general form of the constructor::

        sage: V = VectorSpace(QQ, 3)
        sage: Polyhedra(V) is Polyhedra(QQ, 3)
        True
        sage: Polyhedra(V, backend=\'field\') is Polyhedra(QQ, 3, \'field\')
        True
        sage: Polyhedra(backend=\'field\', ambient_space=V) is Polyhedra(QQ, 3, \'field\')
        True

        sage: M = FreeModule(ZZ, 2)
        sage: Polyhedra(M, backend=\'ppl\') is Polyhedra(ZZ, 2, \'ppl\')
        True

    TESTS::

        sage: Polyhedra(RR, 3, backend=\'field\')                                         # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        ValueError: the \'field\' backend for polyhedron cannot be used with non-exact fields
        sage: Polyhedra(RR, 3)                                                          # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        ValueError: no default backend for computations with Real Field with 53 bits of precision
        sage: Polyhedra(QQ[I], 2)                                                       # needs sage.rings.number_field
        Traceback (most recent call last):
        ...
        ValueError: invalid base ring: Number Field in I
        with defining polynomial x^2 + 1 with I = 1*I
        cannot be coerced to a real field
        sage: Polyhedra(AA, 3, backend=\'polymake\')      # optional - jupymake           # needs sage.rings.number_field
        Traceback (most recent call last):
        ...
        ValueError: the \'polymake\' backend for polyhedron cannot be used with Algebraic Real Field

        sage: Polyhedra(QQ, 2, backend=\'normaliz\')
        Polyhedra in QQ^2
        sage: Polyhedra(SR, 2, backend=\'normaliz\')      # optional - pynormaliz         # needs sage.symbolic
        Polyhedra in (Symbolic Ring)^2
        sage: SCR = SR.subring(no_variables=True)                                       # needs sage.symbolic
        sage: Polyhedra(SCR, 2, backend=\'normaliz\')     # optional - pynormaliz         # needs sage.symbolic
        Polyhedra in (Symbolic Constants Subring)^2

        sage: Polyhedra(SCR, 2, backend=\'number_field\')                                 # needs sage.symbolic
        Polyhedra in (Symbolic Constants Subring)^2
    '''

class Polyhedra_base(UniqueRepresentation, Parent):
    '''
    Polyhedra in a fixed ambient space.

    INPUT:

    - ``base_ring`` -- either ``ZZ``, ``QQ``, or ``RDF``; the base
      ring of the ambient module/vector space

    - ``ambient_dim`` -- integer; the ambient space dimension

    - ``backend`` -- string; the name of the backend for computations. There are
      several backends implemented:

      * ``backend="ppl"`` uses the Parma Polyhedra Library

      * ``backend="cdd"`` uses CDD

      * ``backend="normaliz"`` uses normaliz

      * ``backend="polymake"`` uses polymake

      * ``backend="field"`` a generic Sage implementation

    EXAMPLES::

        sage: from sage.geometry.polyhedron.parent import Polyhedra
        sage: Polyhedra(ZZ, 3)
        Polyhedra in ZZ^3
    '''
    def __init__(self, base_ring, ambient_dim, backend) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 3)
            Polyhedra in QQ^3

        TESTS::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: P = Polyhedra(QQ, 3)
            sage: TestSuite(P).run()
            sage: P = Polyhedra(QQ, 0)
            sage: TestSuite(P).run()
        """
    def list(self):
        """
        Return the two polyhedra in ambient dimension 0, raise an error otherwise.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: P = Polyhedra(QQ, 3)
            sage: P.cardinality()
            +Infinity

            sage: # needs sage.rings.number_field
            sage: P = Polyhedra(AA, 0)
            sage: P.category()
            Category of finite enumerated polyhedral sets over Algebraic Real Field
            sage: P.list()
            [The empty polyhedron in AA^0,
             A 0-dimensional polyhedron in AA^0 defined as the convex hull of 1 vertex]
            sage: P.cardinality()
            2
        """
    def recycle(self, polyhedron) -> None:
        """
        Recycle the H/V-representation objects of a polyhedron.

        This speeds up creation of new polyhedra by reusing
        objects. After recycling a polyhedron object, it is not in a
        consistent state any more and neither the polyhedron nor its
        H/V-representation objects may be used any more.

        INPUT:

        - ``polyhedron`` -- a polyhedron whose parent is ``self``

        EXAMPLES::

            sage: p = Polyhedron([(0,0),(1,0),(0,1)])
            sage: p.parent().recycle(p)

        TESTS::

            sage: p = Polyhedron([(0,0),(1,0),(0,1)])
            sage: n = len(p.parent()._Vertex_pool)
            sage: p._delete()
            sage: len(p.parent()._Vertex_pool) - n
            3
        """
    def ambient_dim(self):
        """
        Return the dimension of the ambient space.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 3).ambient_dim()
            3
        """
    def backend(self):
        """
        Return the backend.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 3).backend()
            'ppl'
        """
    @cached_method
    def an_element(self):
        """
        Return a Polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 4).an_element()
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 5 vertices
        """
    @cached_method
    def some_elements(self):
        """
        Return a list of some elements of the semigroup.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 4).some_elements()
            [A 3-dimensional polyhedron in QQ^4
              defined as the convex hull of 4 vertices,
             A 4-dimensional polyhedron in QQ^4
              defined as the convex hull of 1 vertex and 4 rays,
             A 2-dimensional polyhedron in QQ^4
              defined as the convex hull of 2 vertices and 1 ray,
             The empty polyhedron in QQ^4]
            sage: Polyhedra(ZZ, 0).some_elements()
            [The empty polyhedron in ZZ^0,
             A 0-dimensional polyhedron in ZZ^0 defined as the convex hull of 1 vertex]
        """
    @cached_method
    def zero(self):
        """
        Return the polyhedron consisting of the origin, which is the
        neutral element for Minkowski addition.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: p = Polyhedra(QQ, 4).zero();  p
            A 0-dimensional polyhedron in QQ^4 defined as the convex hull of 1 vertex
            sage: p + p == p
            True
        """
    def empty(self):
        """
        Return the empty polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: P = Polyhedra(QQ, 4)
            sage: P.empty()
            The empty polyhedron in QQ^4
            sage: P.empty().is_empty()
            True
        """
    def universe(self):
        """
        Return the entire ambient space as polyhedron.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: P = Polyhedra(QQ, 4)
            sage: P.universe()
            A 4-dimensional polyhedron in QQ^4 defined as
             the convex hull of 1 vertex and 4 lines
            sage: P.universe().is_universe()
            True
        """
    @cached_method
    def Vrepresentation_space(self):
        """
        Return the ambient vector space.

        This is the vector space or module containing the
        Vrepresentation vectors.

        OUTPUT: a free module over the base ring of dimension :meth:`ambient_dim`

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(QQ, 4).Vrepresentation_space()
            Vector space of dimension 4 over Rational Field
            sage: Polyhedra(QQ, 4).ambient_space()
            Vector space of dimension 4 over Rational Field
        """
    ambient_space = Vrepresentation_space
    @cached_method
    def Hrepresentation_space(self):
        """
        Return the linear space containing the H-representation vectors.

        OUTPUT: a free module over the base ring of dimension :meth:`ambient_dim` + 1

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(ZZ, 2).Hrepresentation_space()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
        """
    def base_extend(self, base_ring, backend=None, ambient_dim=None):
        """
        Return the base extended parent.

        INPUT:

        - ``base_ring``, ``backend`` -- see
          :func:`~sage.geometry.polyhedron.constructor.Polyhedron`
        - ``ambient_dim`` -- if not ``None`` change ambient dimension
          accordingly

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(ZZ, 3).base_extend(QQ)
            Polyhedra in QQ^3
            sage: Polyhedra(ZZ, 3).an_element().base_extend(QQ)
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 4 vertices
            sage: Polyhedra(QQ, 2).base_extend(ZZ)
            Polyhedra in QQ^2

        TESTS:

        Test that :issue:`22575` is fixed::

            sage: P = Polyhedra(ZZ,3).base_extend(QQ, backend='field')
            sage: P.backend()
            'field'
        """
    def change_ring(self, base_ring, backend=None, ambient_dim=None):
        """
        Return the parent with the new base ring.

        INPUT:

        - ``base_ring``, ``backend`` -- see
          :func:`~sage.geometry.polyhedron.constructor.Polyhedron`
        - ``ambient_dim`` -- if not ``None`` change ambient dimension
          accordingly

        EXAMPLES::

            sage: from sage.geometry.polyhedron.parent import Polyhedra
            sage: Polyhedra(ZZ, 3).change_ring(QQ)
            Polyhedra in QQ^3
            sage: Polyhedra(ZZ, 3).an_element().change_ring(QQ)
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 4 vertices

            sage: Polyhedra(RDF, 3).change_ring(QQ).backend()
            'cdd'
            sage: Polyhedra(QQ, 3).change_ring(ZZ, ambient_dim=4)
            Polyhedra in ZZ^4
            sage: Polyhedra(QQ, 3, backend='cdd').change_ring(QQ, ambient_dim=4).backend()
            'cdd'
        """

class Polyhedra_ZZ_ppl(Polyhedra_base):
    Element = Polyhedron_ZZ_ppl

class Polyhedra_ZZ_normaliz(Polyhedra_base):
    Element = Polyhedron_ZZ_normaliz

class Polyhedra_QQ_ppl(Polyhedra_base):
    Element = Polyhedron_QQ_ppl

class Polyhedra_QQ_normaliz(Polyhedra_base):
    Element = Polyhedron_QQ_normaliz

class Polyhedra_QQ_cdd(Polyhedra_base):
    Element = Polyhedron_QQ_cdd

class Polyhedra_RDF_cdd(Polyhedra_base):
    Element = Polyhedron_RDF_cdd

class Polyhedra_normaliz(Polyhedra_base):
    Element = Polyhedron_normaliz

class Polyhedra_polymake(Polyhedra_base):
    Element = Polyhedron_polymake

class Polyhedra_field(Polyhedra_base):
    Element = Polyhedron_field

class Polyhedra_number_field(Polyhedra_base):
    Element = Polyhedron_number_field

@cached_function
def does_backend_handle_base_ring(base_ring, backend):
    """
    Return true, if ``backend`` can handle ``base_ring``.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.parent import does_backend_handle_base_ring
        sage: does_backend_handle_base_ring(QQ, 'ppl')
        True
        sage: does_backend_handle_base_ring(QQ[sqrt(5)], 'ppl')                         # needs sage.rings.number_field sage.symbolic
        False
        sage: does_backend_handle_base_ring(QQ[sqrt(5)], 'field')                       # needs sage.rings.number_field sage.symbolic
        True
    """
