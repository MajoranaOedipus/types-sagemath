from .base_QQ import Polyhedron_QQ as Polyhedron_QQ
from .base_ZZ import Polyhedron_ZZ as Polyhedron_ZZ
from .base_mutable import Polyhedron_mutable as Polyhedron_mutable
from .representation import EQUATION as EQUATION, INEQUALITY as INEQUALITY, LINE as LINE, RAY as RAY, VERTEX as VERTEX
from sage.arith.functions import LCM_list as LCM_list
from sage.features import PythonModule as PythonModule
from sage.misc.functional import denominator as denominator
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Element as Element

class Polyhedron_ppl(Polyhedron_mutable):
    """
    Polyhedra with ppl.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)], rays=[(1,1)], lines=[], backend='ppl')
        sage: TestSuite(p).run()
    """
    def __init__(self, parent, Vrep, Hrep, ppl_polyhedron=None, mutable: bool = False, **kwds) -> None:
        """
        Initialize the polyhedron.

        See :class:`Polyhedron_ppl` for a description of the input
        data.

        TESTS::

            sage: p = Polyhedron()
            sage: TestSuite(p).run()
            sage: p = Polyhedron(vertices=[(1, 1)], rays=[(0, 1)])
            sage: TestSuite(p).run()
            sage: q = polytopes.cube()
            sage: p = q.parent().element_class(q.parent(), None, None, q._ppl_polyhedron)
            sage: TestSuite(p).run()
        """
    def set_immutable(self) -> None:
        '''
        Make this polyhedron immutable. This operation cannot be undone.

        EXAMPLES::

            sage: p = Polyhedron([[1, 1]], mutable=True)
            sage: p.is_mutable()
            True
            sage: hasattr(p, "_Vrepresentation")
            False
            sage: p.set_immutable()
            sage: hasattr(p, "_Vrepresentation")
            True

        TESTS:

        Check that :issue:`33666` is fixed::

            sage: cube = polytopes.cube()
            sage: parent = cube.parent()
            sage: smaller_cube_ZZ = parent._element_constructor_(1/2 * cube, mutable=True)
            sage: smaller_cube_ZZ.set_immutable()
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer
            sage: smaller_cube_ZZ.is_immutable()
            False
            sage: smaller_cube_ZZ.set_immutable()
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer
            sage: smaller_cube_ZZ.is_immutable()
            False
            sage: smaller_cube_QQ = smaller_cube_ZZ.base_extend(QQ)
            sage: smaller_cube_QQ.set_immutable()
            sage: smaller_cube_QQ.is_immutable()
            True
        '''
    def Vrepresentation(self, index=None):
        """
        Return the objects of the V-representation. Each entry is
        either a vertex, a ray, or a line.

        See :mod:`sage.geometry.polyhedron.constructor` for a
        definition of vertex/ray/line.

        INPUT:

        - ``index`` -- either an integer or ``None``

        OUTPUT:

        The optional argument is an index running from ``0`` to
        ``self.n_Vrepresentation()-1``. If present, the
        V-representation object at the given index will be
        returned. Without an argument, returns the list of all
        V-representation objects.

        EXAMPLES::

            sage: p = polytopes.cube()
            sage: p.Vrepresentation(0)
            A vertex at (1, -1, -1)

        ::

            sage: P = p.parent()
            sage: p = P._element_constructor_(p, mutable=True)
            sage: p.Vrepresentation(0)
            A vertex at (-1, -1, -1)
            sage: p._clear_cache()
            sage: p.Vrepresentation(0)
            A vertex at (-1, -1, -1)
            sage: TestSuite(p).run()

        TESTS:

        Check that :issue:`33666` is fixed::

            sage: cube = polytopes.cube()
            sage: parent = cube.parent()
            sage: smaller_cube_ZZ = parent._element_constructor_(1/2 * cube, mutable=True)
            sage: smaller_cube_ZZ.Hrepresentation()
            (An inequality (0, 0, -2) x + 1 >= 0,
            An inequality (0, -2, 0) x + 1 >= 0,
            An inequality (-2, 0, 0) x + 1 >= 0,
            An inequality (2, 0, 0) x + 1 >= 0,
            An inequality (0, 0, 2) x + 1 >= 0,
            An inequality (0, 2, 0) x + 1 >= 0)
            sage: smaller_cube_ZZ.Vrepresentation()
            Traceback (most recent call last):
            ...
            TypeError: the polyhedron is not integral; do a base extension ``self.base_extend(QQ)``
            sage: smaller_cube_ZZ.Vrepresentation()
            Traceback (most recent call last):
            ...
            TypeError: the polyhedron is not integral; do a base extension ``self.base_extend(QQ)``
            sage: smaller_cube_QQ = smaller_cube_ZZ.base_extend(QQ)
            sage: smaller_cube_QQ.Hrepresentation()
            (An inequality (0, 0, -2) x + 1 >= 0,
            An inequality (0, -2, 0) x + 1 >= 0,
            An inequality (-2, 0, 0) x + 1 >= 0,
            An inequality (2, 0, 0) x + 1 >= 0,
            An inequality (0, 0, 2) x + 1 >= 0,
            An inequality (0, 2, 0) x + 1 >= 0)
        """
    def Hrepresentation(self, index=None):
        """
        Return the objects of the H-representation. Each entry is
        either an inequality or a equation.

        INPUT:

        - ``index`` -- either an integer or ``None``

        OUTPUT:

        The optional argument is an index running from ``0`` to
        ``self.n_Hrepresentation()-1``. If present, the
        H-representation object at the given index will be
        returned. Without an argument, returns the list of all
        H-representation objects.

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: p.Hrepresentation(0)
            An inequality (-1, 0, 0) x + 1 >= 0
            sage: p.Hrepresentation(0) == p.Hrepresentation()[0]
            True

        ::

            sage: P = p.parent()
            sage: p = P._element_constructor_(p, mutable=True)
            sage: p.Hrepresentation(0)
            An inequality (0, 0, -1) x + 1 >= 0
            sage: p._clear_cache()
            sage: p.Hrepresentation(0)
            An inequality (0, 0, -1) x + 1 >= 0
            sage: TestSuite(p).run()
        """

class Polyhedron_QQ_ppl(Polyhedron_ppl, Polyhedron_QQ):
    """
    Polyhedra over `\\QQ` with ppl.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)], rays=[(1,1)], lines=[],
        ....:                backend='ppl', base_ring=QQ)
        sage: TestSuite(p).run()
    """
class Polyhedron_ZZ_ppl(Polyhedron_ppl, Polyhedron_ZZ):
    """
    Polyhedra over `\\ZZ` with ppl.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)], rays=[(1,1)], lines=[],
        ....:                backend='ppl', base_ring=ZZ)
        sage: TestSuite(p).run()
    """
