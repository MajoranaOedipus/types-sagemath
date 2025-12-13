import sage.structure.parent
import sage.structure.sage_object
from sage.categories.sets_cat import Sets as Sets
from sage.matrix.constructor import matrix as matrix
from typing import Any, ClassVar, overload

class ConnectedTriangulationsIterator(sage.structure.sage_object.SageObject):
    """ConnectedTriangulationsIterator(point_configuration, seed=None, star=None, fine=False)

    File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 801)

    A Python shim for the C++-class 'triangulations'.

    INPUT:

    - ``point_configuration`` -- a
      :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`

    - ``seed`` -- a regular triangulation or ``None`` (default). In
      the latter case, a suitable triangulation is generated
      automatically. Otherwise, you can explicitly specify the seed
      triangulation as

        * A
          :class:`~sage.geometry.triangulation.element.Triangulation`
          object, or

        * an iterable of iterables specifying the vertices of the simplices, or

        * an iterable of integers, which are then considered the
          enumerated simplices (see
          :meth:`~PointConfiguration_base.simplex_to_int`.

    - ``star`` -- either ``None`` (default) or an integer. If an
      integer is passed, all returned triangulations will be star with
      respect to the

    - ``fine`` -- boolean (default: ``False``); whether to return only
      fine triangulations, that is, simplicial decompositions that
      make use of all the points of the configuration.

    OUTPUT:

    An iterator. The generated values are tuples of
    integers, which encode simplices of the triangulation. The output
    is a suitable input to
    :class:`~sage.geometry.triangulation.element.Triangulation`.

    EXAMPLES::

        sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
        sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
        sage: ci = ConnectedTriangulationsIterator(p)
        sage: next(ci)
        (9, 10)
        sage: next(ci)
        (2, 3, 4, 5)
        sage: next(ci)
        (7, 8)
        sage: next(ci)
        (1, 3, 5, 7)
        sage: next(ci)
        Traceback (most recent call last):
        ...
        StopIteration

    You can reconstruct the triangulation from the compressed output via::

        sage: from sage.geometry.triangulation.element import Triangulation
        sage: Triangulation((2, 3, 4, 5), p)
        (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>)

    How to use the restrictions::

        sage: ci = ConnectedTriangulationsIterator(p, fine=True)
        sage: list(ci)
        [(2, 3, 4, 5), (1, 3, 5, 7)]
        sage: ci = ConnectedTriangulationsIterator(p, star=1)
        sage: list(ci)
        [(7, 8)]
        sage: ci = ConnectedTriangulationsIterator(p, star=1, fine=True)
        sage: list(ci)
        []"""
    def __init__(self, point_configuration, seed=..., star=..., fine=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 892)

                The Python constructor.

                See :class:`ConnectedTriangulationsIterator` for a description
                of the arguments.

                TESTS::

                    sage: p = PointConfiguration([[0,4],[2,3],[3,2],[4,0],[3,-2],[2,-3],[0,-4],[-2,-3],[-3,-2],[-4,0],[-3,2],[-2,3]])
                    sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
                    sage: ci = ConnectedTriangulationsIterator(p)
                    sage: len(list(ci))  # long time (26s on sage.math, 2012)
                    16796
                    sage: ci = ConnectedTriangulationsIterator(p, star=3)
                    sage: len(list(ci))  # long time (26s on sage.math, 2012)
                    1
        """
    @overload
    def __iter__(self) -> Any:
        """ConnectedTriangulationsIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 931)

        The iterator interface: Start iterating.

        TESTS::

            sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: ci = ConnectedTriangulationsIterator(p, fine=True)
            sage: ci.__iter__()
            <sage.geometry.triangulation.base.ConnectedTriangulationsIterator object at ...>
            sage: ci.__iter__() is ci
            True"""
    @overload
    def __iter__(self) -> Any:
        """ConnectedTriangulationsIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 931)

        The iterator interface: Start iterating.

        TESTS::

            sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: ci = ConnectedTriangulationsIterator(p, fine=True)
            sage: ci.__iter__()
            <sage.geometry.triangulation.base.ConnectedTriangulationsIterator object at ...>
            sage: ci.__iter__() is ci
            True"""
    @overload
    def __iter__(self) -> Any:
        """ConnectedTriangulationsIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 931)

        The iterator interface: Start iterating.

        TESTS::

            sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: ci = ConnectedTriangulationsIterator(p, fine=True)
            sage: ci.__iter__()
            <sage.geometry.triangulation.base.ConnectedTriangulationsIterator object at ...>
            sage: ci.__iter__() is ci
            True"""
    @overload
    def __next__(self) -> Any:
        """ConnectedTriangulationsIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 947)

        The iterator interface: Next iteration.

        EXAMPLES::

            sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: ci = ConnectedTriangulationsIterator(p)
            sage: ci.__next__()
            (9, 10)"""
    @overload
    def __next__(self) -> Any:
        """ConnectedTriangulationsIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 947)

        The iterator interface: Next iteration.

        EXAMPLES::

            sage: from sage.geometry.triangulation.base import ConnectedTriangulationsIterator
            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: ci = ConnectedTriangulationsIterator(p)
            sage: ci.__next__()
            (9, 10)"""

class Point(sage.structure.sage_object.SageObject):
    """Point(point_configuration, i, projective, affine, reduced)

    File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 36)

    A point of a point configuration.

    Note that the coordinates of the points of a point configuration
    are somewhat arbitrary. What counts are the abstract linear
    relations between the points, for example encoded by the
    :meth:`~sage.geometry.triangulation.point_configuration.PointConfiguration.circuits`.

    .. WARNING::

        You should not create :class:`Point` objects manually. The
        constructor of :class:`PointConfiguration_base` takes care of
        this for you.

    INPUT:

    - ``point_configuration`` -- :class:`PointConfiguration_base`; the
      point configuration to which the point belongs

    - ``i`` -- integer; the index of the point in the point
      configuration

    - ``projective`` -- the projective coordinates of the point

    - ``affine`` -- the affine coordinates of the point

    - ``reduced`` -- the reduced (with linearities removed)
      coordinates of the point

    EXAMPLES::

        sage: pc = PointConfiguration([(0,0)])
        sage: from sage.geometry.triangulation.base import Point
        sage: Point(pc, 123, (0,0,1), (0,0), ())
        P(0, 0)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, point_configuration, i, projective, affine, reduced) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 79)

                Construct a :class:`Point`.

                EXAMPLES::

                    sage: pc = PointConfiguration([(0,0)])
                    sage: from sage.geometry.triangulation.base import Point
                    sage: Point(pc, 123, (0,0,1), (0,0), ())   # indirect doctest
                    P(0, 0)
        """
    @overload
    def affine(self) -> Any:
        """Point.affine(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 197)

        Return the affine coordinates of the point in the ambient space.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def affine(self) -> Any:
        """Point.affine(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 197)

        Return the affine coordinates of the point in the ambient space.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def index(self) -> Any:
        """Point.index(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 159)

        Return the index of the point in the point configuration.

        EXAMPLES::

            sage: pc = PointConfiguration([[0, 1], [0, 0], [1, 0]])
            sage: p = pc.point(2); p
            P(1, 0)
            sage: p.index()
            2"""
    @overload
    def index(self) -> Any:
        """Point.index(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 159)

        Return the index of the point in the point configuration.

        EXAMPLES::

            sage: pc = PointConfiguration([[0, 1], [0, 0], [1, 0]])
            sage: p = pc.point(2); p
            P(1, 0)
            sage: p.index()
            2"""
    @overload
    def point_configuration(self) -> Any:
        """Point.point_configuration(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 112)

        Return the point configuration to which the point belongs.

        OUTPUT: a :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`

        EXAMPLES::

            sage: pc = PointConfiguration([ (0,0), (1,0), (0,1) ])
            sage: p = pc.point(0)
            sage: p is pc.point(0)
            True
            sage: p.point_configuration() is pc
            True"""
    @overload
    def point_configuration(self) -> Any:
        """Point.point_configuration(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 112)

        Return the point configuration to which the point belongs.

        OUTPUT: a :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`

        EXAMPLES::

            sage: pc = PointConfiguration([ (0,0), (1,0), (0,1) ])
            sage: p = pc.point(0)
            sage: p is pc.point(0)
            True
            sage: p.point_configuration() is pc
            True"""
    @overload
    def projective(self) -> Any:
        """Point.projective(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 173)

        Return the projective coordinates of the point in the ambient space.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def projective(self) -> Any:
        """Point.projective(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 173)

        Return the projective coordinates of the point in the ambient space.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_affine(self) -> Any:
        """Point.reduced_affine(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 221)

        Return the affine coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_affine(self) -> Any:
        """Point.reduced_affine(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 221)

        Return the affine coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_affine_vector(self) -> Any:
        """Point.reduced_affine_vector(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 271)

        Return the affine coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_affine_vector(self) -> Any:
        """Point.reduced_affine_vector(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 271)

        Return the affine coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_projective(self) -> Any:
        """Point.reduced_projective(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 246)

        Return the projective coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    @overload
    def reduced_projective(self) -> Any:
        """Point.reduced_projective(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 246)

        Return the projective coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)"""
    def reduced_projective_vector(self) -> Any:
        """Point.reduced_projective_vector(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 296)

        Return the affine coordinates of the point on the hyperplane
        spanned by the point configuration.

        OUTPUT: a tuple containing the coordinates

        EXAMPLES::

            sage: pc = PointConfiguration([[10, 0, 1], [10, 0, 0], [10, 2, 3]])
            sage: p = pc.point(2); p
            P(10, 2, 3)
            sage: p.affine()
            (10, 2, 3)
            sage: p.projective()
            (10, 2, 3, 1)
            sage: p.reduced_affine()
            (2, 2)
            sage: p.reduced_projective()
            (2, 2, 1)
            sage: p.reduced_affine_vector()
            (2, 2)
            sage: type(p.reduced_affine_vector())
            <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>"""
    def __hash__(self) -> Any:
        """Point.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 100)

        Hash value for a point in a point configuration.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[0,1],[1,1]])
            sage: hash(p[0]) # random
            35822008390213632"""
    def __iter__(self) -> Any:
        """Point.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 129)

        Iterate through the affine ambient space coordinates of the point.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0)])
            sage: from sage.geometry.triangulation.base import Point
            sage: p = Point(pc, 123, (1,2,1), (3,4), ())
            sage: list(p)  # indirect doctest
            [3, 4]"""
    @overload
    def __len__(self) -> Any:
        """Point.__len__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 143)

        Return the affine ambient space dimension.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0)])
            sage: from sage.geometry.triangulation.base import Point
            sage: p = Point(pc, 123, (1,2,1), (3,4), ())
            sage: len(p)
            2
            sage: p.__len__()
            2"""
    @overload
    def __len__(self) -> Any:
        """Point.__len__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 143)

        Return the affine ambient space dimension.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0)])
            sage: from sage.geometry.triangulation.base import Point
            sage: p = Point(pc, 123, (1,2,1), (3,4), ())
            sage: len(p)
            2
            sage: p.__len__()
            2"""

class PointConfiguration_base(sage.structure.parent.Parent):
    """PointConfiguration_base(points, defined_affine)

    File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 341)

    The cython abstract base class for
    :class:`~sage.geometry.triangulation.PointConfiguration`.

    .. WARNING::

        You should not instantiate this base class, but only its
        derived class
        :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, points, defined_affine) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 353)

                Construct a :class:`PointConfiguration_base`.

                INPUT:

                - ``points`` -- tuple of tuples of projective coordinates
                  with ``1`` as the final coordinate

                - ``defined_affine`` -- boolean; whether the point
                  configuration is defined as a configuration of affine (as
                  opposed to projective) points

                TESTS::

                    sage: from sage.geometry.triangulation.base import PointConfiguration_base
                    sage: PointConfiguration_base(((1,2,1),(2,3,1),(3,4,1)), False)
                    <sage.geometry.triangulation.base.PointConfiguration_base object at ...>
        """
    @overload
    def ambient_dim(self) -> Any:
        """PointConfiguration_base.ambient_dim(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 490)

        Return the dimension of the ambient space of the point
        configuration.

        See also :meth:`dimension`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0]])
            sage: p.ambient_dim()
            3
            sage: p.dim()
            0"""
    @overload
    def ambient_dim(self) -> Any:
        """PointConfiguration_base.ambient_dim(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 490)

        Return the dimension of the ambient space of the point
        configuration.

        See also :meth:`dimension`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0]])
            sage: p.ambient_dim()
            3
            sage: p.dim()
            0"""
    @overload
    def base_ring(self) -> Any:
        """PointConfiguration_base.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 523)

        Return the base ring, that is, the ring containing the
        coordinates of the points.

        OUTPUT: a ring

        EXAMPLES::

            sage: p = PointConfiguration([(0,0)])
            sage: p.base_ring()
            Integer Ring

            sage: p = PointConfiguration([(1/2,3)])
            sage: p.base_ring()
            Rational Field

            sage: p = PointConfiguration([(0.2, 5)])
            sage: p.base_ring()
            Real Field with 53 bits of precision"""
    @overload
    def base_ring(self) -> Any:
        """PointConfiguration_base.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 523)

        Return the base ring, that is, the ring containing the
        coordinates of the points.

        OUTPUT: a ring

        EXAMPLES::

            sage: p = PointConfiguration([(0,0)])
            sage: p.base_ring()
            Integer Ring

            sage: p = PointConfiguration([(1/2,3)])
            sage: p.base_ring()
            Rational Field

            sage: p = PointConfiguration([(0.2, 5)])
            sage: p.base_ring()
            Real Field with 53 bits of precision"""
    @overload
    def base_ring(self) -> Any:
        """PointConfiguration_base.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 523)

        Return the base ring, that is, the ring containing the
        coordinates of the points.

        OUTPUT: a ring

        EXAMPLES::

            sage: p = PointConfiguration([(0,0)])
            sage: p.base_ring()
            Integer Ring

            sage: p = PointConfiguration([(1/2,3)])
            sage: p.base_ring()
            Rational Field

            sage: p = PointConfiguration([(0.2, 5)])
            sage: p.base_ring()
            Real Field with 53 bits of precision"""
    @overload
    def base_ring(self) -> Any:
        """PointConfiguration_base.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 523)

        Return the base ring, that is, the ring containing the
        coordinates of the points.

        OUTPUT: a ring

        EXAMPLES::

            sage: p = PointConfiguration([(0,0)])
            sage: p.base_ring()
            Integer Ring

            sage: p = PointConfiguration([(1/2,3)])
            sage: p.base_ring()
            Rational Field

            sage: p = PointConfiguration([(0.2, 5)])
            sage: p.base_ring()
            Real Field with 53 bits of precision"""
    @overload
    def dim(self) -> Any:
        """PointConfiguration_base.dim(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 507)

        Return the actual dimension of the point configuration.

        See also :meth:`ambient_dim`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0]])
            sage: p.ambient_dim()
            3
            sage: p.dim()
            0"""
    @overload
    def dim(self) -> Any:
        """PointConfiguration_base.dim(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 507)

        Return the actual dimension of the point configuration.

        See also :meth:`ambient_dim`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0]])
            sage: p.ambient_dim()
            3
            sage: p.dim()
            0"""
    def int_to_simplex(self, ints) -> Any:
        """PointConfiguration_base.int_to_simplex(self, int s)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 749)

        Reverse the enumeration of possible simplices in
        :meth:`simplex_to_int`.

        The enumeration is compatible with [PUNTOS]_.

        INPUT:

        - ``s`` -- integer that uniquely specifies a simplex

        OUTPUT:

        An ordered tuple consisting of the indices of the vertices of
        the simplex.

        EXAMPLES::

            sage: U=matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ])
            sage: pc = PointConfiguration(U.columns())
            sage: pc.simplex_to_int([1,3,4,7,10,13])
            1678
            sage: pc.int_to_simplex(1678)
            (1, 3, 4, 7, 10, 13)"""
    @overload
    def is_affine(self) -> bool:
        """PointConfiguration_base.is_affine(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 546)

        Return whether the configuration is defined by affine points.

        OUTPUT: boolean; if true, the homogeneous coordinates all have `1` as
        their last entry

        EXAMPLES::

            sage: p = PointConfiguration([(0.2, 5), (3, 0.1)])
            sage: p.is_affine()
            True

            sage: p = PointConfiguration([(0.2, 5, 1), (3, 0.1, 1)], projective=True)
            sage: p.is_affine()
            False"""
    @overload
    def is_affine(self) -> Any:
        """PointConfiguration_base.is_affine(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 546)

        Return whether the configuration is defined by affine points.

        OUTPUT: boolean; if true, the homogeneous coordinates all have `1` as
        their last entry

        EXAMPLES::

            sage: p = PointConfiguration([(0.2, 5), (3, 0.1)])
            sage: p.is_affine()
            True

            sage: p = PointConfiguration([(0.2, 5, 1), (3, 0.1, 1)], projective=True)
            sage: p.is_affine()
            False"""
    @overload
    def is_affine(self) -> Any:
        """PointConfiguration_base.is_affine(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 546)

        Return whether the configuration is defined by affine points.

        OUTPUT: boolean; if true, the homogeneous coordinates all have `1` as
        their last entry

        EXAMPLES::

            sage: p = PointConfiguration([(0.2, 5), (3, 0.1)])
            sage: p.is_affine()
            True

            sage: p = PointConfiguration([(0.2, 5, 1), (3, 0.1, 1)], projective=True)
            sage: p.is_affine()
            False"""
    @overload
    def n_points(self) -> Any:
        """PointConfiguration_base.n_points(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 609)

        Return the number of points.

        Same as ``len(self)``.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: len(p)
            5
            sage: p.n_points()
            5"""
    @overload
    def n_points(self) -> Any:
        """PointConfiguration_base.n_points(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 609)

        Return the number of points.

        Same as ``len(self)``.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: len(p)
            5
            sage: p.n_points()
            5"""
    def point(self, i) -> Any:
        """PointConfiguration_base.point(self, i)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 655)

        Return the `i`-th point of the configuration.

        Same as :meth:`__getitem__`

        INPUT:

        - ``i`` -- integer

        OUTPUT: a point of the point configuration

        EXAMPLES::

            sage: pconfig = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: list(pconfig)
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: [ p for p in pconfig.points() ]
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: pconfig.point(0)
            P(0, 0)
            sage: pconfig[0]
            P(0, 0)
            sage: pconfig.point(1)
            P(0, 1)
            sage: pconfig.point( pconfig.n_points()-1 )
            P(-1, -1)"""
    @overload
    def points(self) -> Any:
        """PointConfiguration_base.points(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 630)

        Return a list of the points.

        OUTPUT:

        A list of the points. See also the :meth:`__iter__`
        method, which returns the corresponding generator.

        EXAMPLES::

            sage: pconfig = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: list(pconfig)
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: [ p for p in pconfig.points() ]
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: pconfig.point(0)
            P(0, 0)
            sage: pconfig.point(1)
            P(0, 1)
            sage: pconfig.point( pconfig.n_points()-1 )
            P(-1, -1)"""
    @overload
    def points(self) -> Any:
        """PointConfiguration_base.points(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 630)

        Return a list of the points.

        OUTPUT:

        A list of the points. See also the :meth:`__iter__`
        method, which returns the corresponding generator.

        EXAMPLES::

            sage: pconfig = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: list(pconfig)
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: [ p for p in pconfig.points() ]
            [P(0, 0), P(0, 1), P(1, 0), P(1, 1), P(-1, -1)]
            sage: pconfig.point(0)
            P(0, 0)
            sage: pconfig.point(1)
            P(0, 1)
            sage: pconfig.point( pconfig.n_points()-1 )
            P(-1, -1)"""
    @overload
    def reduced_affine_vector_space(self) -> Any:
        """PointConfiguration_base.reduced_affine_vector_space(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 453)

        Return the vector space that contains the affine points.

        OUTPUT: a vector space over the fraction field of :meth:`base_ring`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0], [1,2,3]])
            sage: p.base_ring()
            Integer Ring
            sage: p.reduced_affine_vector_space()
            Vector space of dimension 1 over Rational Field
            sage: p.reduced_projective_vector_space()
            Vector space of dimension 2 over Rational Field"""
    @overload
    def reduced_affine_vector_space(self) -> Any:
        """PointConfiguration_base.reduced_affine_vector_space(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 453)

        Return the vector space that contains the affine points.

        OUTPUT: a vector space over the fraction field of :meth:`base_ring`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0], [1,2,3]])
            sage: p.base_ring()
            Integer Ring
            sage: p.reduced_affine_vector_space()
            Vector space of dimension 1 over Rational Field
            sage: p.reduced_projective_vector_space()
            Vector space of dimension 2 over Rational Field"""
    @overload
    def reduced_projective_vector_space(self) -> Any:
        """PointConfiguration_base.reduced_projective_vector_space(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 471)

        Return the vector space that is spanned by the homogeneous
        coordinates.

        OUTPUT: a vector space over the fraction field of :meth:`base_ring`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0], [1,2,3]])
            sage: p.base_ring()
            Integer Ring
            sage: p.reduced_affine_vector_space()
            Vector space of dimension 1 over Rational Field
            sage: p.reduced_projective_vector_space()
            Vector space of dimension 2 over Rational Field"""
    @overload
    def reduced_projective_vector_space(self) -> Any:
        """PointConfiguration_base.reduced_projective_vector_space(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 471)

        Return the vector space that is spanned by the homogeneous
        coordinates.

        OUTPUT: a vector space over the fraction field of :meth:`base_ring`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0,0], [1,2,3]])
            sage: p.base_ring()
            Integer Ring
            sage: p.reduced_affine_vector_space()
            Vector space of dimension 1 over Rational Field
            sage: p.reduced_projective_vector_space()
            Vector space of dimension 2 over Rational Field"""
    def simplex_to_int(self, simplex) -> Any:
        """PointConfiguration_base.simplex_to_int(self, simplex)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 706)

        Return an integer that uniquely identifies the given simplex.

        See also the inverse method :meth:`int_to_simplex`.

        The enumeration is compatible with [PUNTOS]_.

        INPUT:

        - ``simplex`` -- iterable, for example a list. The elements
          are the vertex indices of the simplex

        OUTPUT: integer that uniquely specifies the simplex

        EXAMPLES::

            sage: U=matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ])
            sage: pc = PointConfiguration(U.columns())
            sage: pc.simplex_to_int([1,3,4,7,10,13])
            1678
            sage: pc.int_to_simplex(1678)
            (1, 3, 4, 7, 10, 13)"""
    def __getitem__(self, i) -> Any:
        """PointConfiguration_base.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 583)

        Return the ``i``-th point.

        Same as :meth:`point`.

        INPUT:

        - ``i`` -- integer

        OUTPUT: the ``i``-th point of the point configuration

        EXAMPLES::

            sage: p = PointConfiguration([[1,0], [2,3], [3,2]])
            sage: [p[i] for i in range(p.n_points())]
            [P(1, 0), P(2, 3), P(3, 2)]
            sage: list(p)
            [P(1, 0), P(2, 3), P(3, 2)]
            sage: list(p.points())
            [P(1, 0), P(2, 3), P(3, 2)]
            sage: [p.point(i) for i in range(p.n_points())]
            [P(1, 0), P(2, 3), P(3, 2)]"""
    def __hash__(self) -> Any:
        """PointConfiguration_base.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 441)

        Hash function.

        TESTS::

            sage: p = PointConfiguration([[0,0],[0,1]])
            sage: hash(p) # random
            8746748042501"""
    def __len__(self) -> Any:
        """PointConfiguration_base.__len__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/triangulation/base.pyx (starting at line 685)

        Return the number of points.

        Same as :meth:`n_points`

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: p
            A point configuration in affine 2-space over Integer Ring
            consisting of 5 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: len(p)
            5
            sage: p.n_points()
            5"""
