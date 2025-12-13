from _typeshed import Incomplete
from dataclasses import dataclass
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.matrix.constructor import matrix as matrix
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.set import Set_base as Set_base
from sage.structure.sage_object import SageObject as SageObject
from typing import Any

@dataclass
class AffineHullProjectionData:
    image: Any = ...
    projection_linear_map: Any = ...
    projection_translation: Any = ...
    section_linear_map: Any = ...
    section_translation: Any = ...

class ConvexSet_base(SageObject, Set_base):
    """
    Abstract base class for convex sets.
    """
    def is_empty(self):
        """
        Test whether ``self`` is the empty set.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = LatticePolytope([], lattice=ToricLattice(3).dual()); p
            -1-d lattice polytope in 3-d lattice M
            sage: p.is_empty()
            True
        """
    def is_finite(self):
        """
        Test whether ``self`` is a finite set.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = LatticePolytope([], lattice=ToricLattice(3).dual()); p
            -1-d lattice polytope in 3-d lattice M
            sage: p.is_finite()
            True
            sage: q = Polyhedron(ambient_dim=2); q
            The empty polyhedron in ZZ^2
            sage: q.is_finite()
            True
            sage: r = Polyhedron(rays=[(1, 0)]); r
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 ray
            sage: r.is_finite()
            False
        """
    def cardinality(self):
        """
        Return the cardinality of this set.

        OUTPUT: either an integer or ``Infinity``

        EXAMPLES::

            sage: p = LatticePolytope([], lattice=ToricLattice(3).dual()); p
            -1-d lattice polytope in 3-d lattice M
            sage: p.cardinality()
            0
            sage: q = Polyhedron(ambient_dim=2); q
            The empty polyhedron in ZZ^2
            sage: q.cardinality()
            0
            sage: r = Polyhedron(rays=[(1, 0)]); r
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 ray
            sage: r.cardinality()
            +Infinity
        """
    def is_universe(self):
        """
        Test whether ``self`` is the whole ambient space.

        OUTPUT: boolean

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.is_universe()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def dim(self):
        """
        Return the dimension of ``self``.

        Subclasses must provide an implementation of this method or of the
        method :meth:`an_affine_basis`.

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.dim()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        This is the same as :meth:`dim`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def dim(self):
            ....:         return 42
            sage: ExampleSet().dimension()
            42
        """
    @abstract_method
    def ambient_vector_space(self, base_field=None) -> None:
        """
        Return the ambient vector space.

        Subclasses must provide an implementation of this method.

        The default implementations of :meth:`ambient`, :meth:`ambient_dim`,
        :meth:`ambient_dimension` use this method.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.ambient_vector_space()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method ambient_vector_space at ...>
        """
    def ambient(self):
        """
        Return the ambient convex set or space.

        The default implementation delegates to :meth:`ambient_vector_space`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def ambient_vector_space(self, base_field=None):
            ....:         return (base_field or QQ)^2001
            sage: ExampleSet().ambient()
            Vector space of dimension 2001 over Rational Field
        """
    def ambient_dim(self):
        """
        Return the dimension of the ambient convex set or space.

        The default implementation obtains it from :meth:`ambient`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def ambient(self):
            ....:         return QQ^7
            sage: ExampleSet().ambient_dim()
            7
        """
    def ambient_dimension(self):
        """
        Return the dimension of the ambient convex set or space.

        This is the same as :meth:`ambient_dim`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def ambient_dim(self):
            ....:         return 91
            sage: ExampleSet().ambient_dimension()
            91
        """
    def an_affine_basis(self) -> None:
        """
        Return points that form an affine basis for the affine hull.

        The points are guaranteed to lie in the topological closure of ``self``.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.an_affine_basis()
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """
    def affine_hull(self, *args, **kwds):
        """
        Return the affine hull of ``self`` as a polyhedron.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_compact
            sage: class EmbeddedDisk(ConvexSet_compact):
            ....:     def an_affine_basis(self):
            ....:         return [vector([1, 0, 0]), vector([1, 1, 0]), vector([1, 0, 1])]
            sage: O = EmbeddedDisk()
            sage: O.dim()
            2
            sage: O.affine_hull()
            A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex and 2 lines
        """
    def affine_hull_projection(self, as_convex_set=None, as_affine_map: bool = False, orthogonal: bool = False, orthonormal: bool = False, extend: bool = False, minimal: bool = False, return_all_data: bool = False, **kwds):
        """
        Return ``self`` projected into its affine hull.

        Each convex set is contained in some smallest affine subspace
        (possibly the entire ambient space) -- its affine hull.  We
        provide an affine linear map that projects the ambient space of
        the convex set to the standard Euclidean space of dimension of
        the convex set, which restricts to a bijection from the affine
        hull.

        The projection map is not unique; some parameters control the
        choice of the map.  Other parameters control the output of the
        function.

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[1, 0], [0, 1]])
            sage: ri_P = P.relative_interior(); ri_P
            Relative interior of a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_P.affine_hull_projection(as_affine_map=True)
            (Vector space morphism represented by the matrix:
            [1]
            [0]
            Domain: Vector space of dimension 2 over Rational Field
            Codomain: Vector space of dimension 1 over Rational Field,
            (0))
            sage: P_aff = P.affine_hull_projection(); P_aff
            A 1-dimensional polyhedron in ZZ^1 defined as the convex hull of 2 vertices
            sage: ri_P_aff = ri_P.affine_hull_projection(); ri_P_aff
            Relative interior of a 1-dimensional polyhedron in QQ^1 defined as the convex hull of 2 vertices
            sage: ri_P_aff.closure() == P_aff
            True
        """
    def codimension(self):
        """
        Return the codimension of ``self`` in ``self.ambient()``.

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,2,3)], rays=[(1,0,0)])
            sage: P.codimension()
            2

        An alias is :meth:`codim`::

            sage: P.codim()
            2
        """
    codim = codimension
    def is_full_dimensional(self):
        """
        Return whether ``self`` is full dimensional.

        OUTPUT: boolean; whether the polyhedron is not contained in any strict
        affine subspace

        EXAMPLES::

            sage: c = Cone([(1,0)])
            sage: c.is_full_dimensional()
            False

            sage: polytopes.hypercube(3).is_full_dimensional()
            True
            sage: Polyhedron(vertices=[(1,2,3)], rays=[(1,0,0)]).is_full_dimensional()
            False
        """
    def is_open(self):
        """
        Return whether ``self`` is open.

        The default implementation of this method only knows that the
        empty set and the ambient space are open.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def is_empty(self):
            ....:         return False
            ....:     def is_universe(self):
            ....:         return True
            sage: ExampleSet().is_open()
            True
        """
    def is_relatively_open(self):
        """
        Return whether ``self`` is relatively open.

        The default implementation of this method only knows that open
        sets are also relatively open, and in addition singletons are
        relatively open.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def is_open(self):
            ....:         return True
            sage: ExampleSet().is_relatively_open()
            True
        """
    def is_closed(self):
        """
        Return whether ``self`` is closed.

        The default implementation of this method only knows that the
        empty set, a singleton set, and the ambient space are closed.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def dim(self):
            ....:         return 0
            sage: ExampleSet().is_closed()
            True
        """
    def is_compact(self):
        """
        Return whether ``self`` is compact.

        The default implementation of this method only knows that a
        non-closed set cannot be compact, and that the empty set and
        a singleton set are compact.

        OUTPUT: boolean

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: class ExampleSet(ConvexSet_base):
            ....:     def dim(self):
            ....:         return 0
            sage: ExampleSet().is_compact()
            True
        """
    def closure(self):
        """
        Return the topological closure of ``self``.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_closed
            sage: C = ConvexSet_closed()
            sage: C.closure() is C
            True
        """
    def interior(self):
        """
        Return the topological interior of ``self``.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_open
            sage: C = ConvexSet_open()
            sage: C.interior() is C
            True
        """
    def relative_interior(self):
        """
        Return the relative interior of ``self``.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_relatively_open
            sage: C = ConvexSet_relatively_open()
            sage: C.relative_interior() is C
            True
        """
    @cached_method
    def representative_point(self):
        '''
        Return a "generic" point of ``self``.

        OUTPUT: a point in the relative interior of ``self`` as a coordinate vector

        EXAMPLES::

            sage: C = Cone([[1, 2, 0], [2, 1, 0]])
            sage: C.representative_point()
            (1, 1, 0)
        '''
    def an_element(self):
        """
        Return a point of ``self``.

        If ``self`` is empty, an :exc:`EmptySetError` will be raised.

        The default implementation delegates to :meth:`_some_elements_`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_compact
            sage: class BlueBox(ConvexSet_compact):
            ....:     def _some_elements_(self):
            ....:         yield 'blue'
            ....:         yield 'cyan'
            sage: BlueBox().an_element()
            'blue'
        """
    def some_elements(self):
        """
        Return a list of some points of ``self``.

        If ``self`` is empty, an empty list is returned; no exception will be raised.

        The default implementation delegates to :meth:`_some_elements_`.

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_compact
            sage: class BlueBox(ConvexSet_compact):
            ....:     def _some_elements_(self):
            ....:         yield 'blue'
            ....:         yield 'cyan'
            sage: BlueBox().some_elements()
            ['blue', 'cyan']
        """
    def cartesian_product(self, other) -> None:
        """
        Return the Cartesian product.

        INPUT:

        - ``other`` -- another convex set

        OUTPUT: the Cartesian product of ``self`` and ``other``

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.cartesian_product(C)
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """
    def contains(self, point) -> None:
        """
        Test whether ``self`` contains the given ``point``.

        INPUT:

        - ``point`` -- a point or its coordinates

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.contains(vector([0, 0]))
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """
    def intersection(self, other) -> None:
        """
        Return the intersection of ``self`` and ``other``.

        INPUT:

        - ``other`` -- another convex set

        OUTPUT: the intersection

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: C.intersection(C)
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """
    def dilation(self, scalar):
        """
        Return the dilated (uniformly stretched) set.

        INPUT:

        - ``scalar`` -- a scalar, not necessarily in :meth:`base_ring`

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_compact
            sage: class GlorifiedPoint(ConvexSet_compact):
            ....:     def __init__(self, p):
            ....:         self._p = p
            ....:     def ambient_vector_space(self):
            ....:         return self._p.parent().vector_space()
            ....:     def linear_transformation(self, linear_transf):
            ....:         return GlorifiedPoint(linear_transf * self._p)
            sage: P = GlorifiedPoint(vector([2, 3]))
            sage: P.dilation(10)._p
            (20, 30)
        """
    def linear_transformation(self, linear_transf) -> None:
        """
        Return the linear transformation of ``self``.

        INPUT:

        - ``linear_transf`` -- a matrix

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: T = matrix.identity(3)
            sage: C.linear_transformation(T)
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """
    def translation(self, displacement) -> None:
        """
        Return the translation of ``self`` by a ``displacement`` vector.

        INPUT:

        - ``displacement`` -- a displacement vector or a list/tuple of
          coordinates that determines a displacement vector

        TESTS::

            sage: from sage.geometry.convex_set import ConvexSet_base
            sage: C = ConvexSet_base()
            sage: t = vector([1, 2, 3])
            sage: C.translation(t)
            Traceback (most recent call last):
            ...
            TypeError: 'NotImplementedType' object is not callable
        """

class ConvexSet_closed(ConvexSet_base):
    """
    Abstract base class for closed convex sets.
    """
    def is_closed(self):
        """
        Return whether ``self`` is closed.

        OUTPUT: boolean

        EXAMPLES::

            sage: hcube = polytopes.hypercube(5)
            sage: hcube.is_closed()
            True
        """
    def is_open(self):
        """
        Return whether ``self`` is open.

        OUTPUT: boolean

        EXAMPLES::

            sage: hcube = polytopes.hypercube(5)
            sage: hcube.is_open()
            False

            sage: zerocube = polytopes.hypercube(0)
            sage: zerocube.is_open()
            True
        """

class ConvexSet_compact(ConvexSet_closed):
    """
    Abstract base class for compact convex sets.
    """
    def is_universe(self):
        """
        Return whether ``self`` is the whole ambient space.

        OUTPUT: boolean

        EXAMPLES::

            sage: cross3 = lattice_polytope.cross_polytope(3)
            sage: cross3.is_universe()
            False
            sage: point0 = LatticePolytope([[]]); point0
            0-d reflexive polytope in 0-d lattice M
            sage: point0.is_universe()
            True
        """
    def is_compact(self):
        """
        Return whether ``self`` is compact.

        OUTPUT: boolean

        EXAMPLES::

            sage: cross3 = lattice_polytope.cross_polytope(3)
            sage: cross3.is_compact()
            True
        """
    is_relatively_open: Incomplete

class ConvexSet_relatively_open(ConvexSet_base):
    """
    Abstract base class for relatively open convex sets.
    """
    def is_relatively_open(self):
        """
        Return whether ``self`` is relatively open.

        OUTPUT: boolean

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior()
            sage: ri_segment.is_relatively_open()
            True
        """
    def is_open(self):
        """
        Return whether ``self`` is open.

        OUTPUT: boolean

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior()
            sage: ri_segment.is_open()
            False
        """

class ConvexSet_open(ConvexSet_relatively_open):
    """
    Abstract base class for open convex sets.
    """
    def is_open(self):
        """
        Return whether ``self`` is open.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_open
            sage: b = ConvexSet_open()
            sage: b.is_open()
            True
        """
    def is_closed(self):
        """
        Return whether ``self`` is closed.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.convex_set import ConvexSet_open
            sage: class OpenBall(ConvexSet_open):
            ....:     def dim(self):
            ....:         return 3
            ....:     def is_universe(self):
            ....:         return False
            sage: OpenBall().is_closed()
            False
        """
