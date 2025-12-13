from .weight_lattice_realizations import WeightLatticeRealizations as WeightLatticeRealizations
from _typeshed import Incomplete
from sage.categories.homset import End as End
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class AmbientSpace(CombinatorialFreeModule):
    '''
    Abstract class for ambient spaces.

    All subclasses should implement a class method
    ``smallest_base_ring`` taking a Cartan type as input, and a method
    ``dimension`` working on a partially initialized instance with
    just ``root_system`` as attribute. There is no safe default
    implementation for the later, so none is provided.

    EXAMPLES::

        sage: AL = RootSystem([\'A\',2]).ambient_lattice()

    .. NOTE:: This is only used so far for finite root systems.

    Caveat: Most of the ambient spaces currently have a basis indexed
    by `0,\\dots, n`, unlike the usual mathematical convention::

        sage: e = AL.basis()
        sage: e[0], e[1], e[2]
        ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    This will be cleaned up!

    .. SEEALSO::

        - :class:`sage.combinat.root_system.type_A.AmbientSpace`
        - :class:`sage.combinat.root_system.type_B.AmbientSpace`
        - :class:`sage.combinat.root_system.type_C.AmbientSpace`
        - :class:`sage.combinat.root_system.type_D.AmbientSpace`
        - :class:`sage.combinat.root_system.type_E.AmbientSpace`
        - :class:`sage.combinat.root_system.type_F.AmbientSpace`
        - :class:`sage.combinat.root_system.type_G.AmbientSpace`
        - :class:`sage.combinat.root_system.type_dual.AmbientSpace`
        - :class:`sage.combinat.root_system.type_affine.AmbientSpace`

    TESTS::

        sage: # needs sage.libs.gap
        sage: types = CartanType.samples(crystallographic=True) + [CartanType(["A",2],["C",5])]
        sage: for e in [ct.root_system().ambient_space() for ct in types]:
        ....:     TestSuite(e).run()

        sage: e1 = RootSystem([\'A\',3]).ambient_lattice()
        sage: e2 = RootSystem([\'B\',3]).ambient_lattice()
        sage: e1 == e1
        True
        sage: e1 == e2
        False

        sage: e1 = RootSystem([\'A\',3]).ambient_space(QQ)
        sage: e2 = RootSystem([\'A\',3]).ambient_space(RR)
        sage: e1 == e2
        False
    '''
    root_system: Incomplete
    n: Incomplete
    def __init__(self, root_system, base_ring, index_set=None) -> None:
        """
        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: s = e.simple_reflections()

            sage: L = RootSystem(['A',3]).coroot_lattice()
            sage: e.has_coerce_map_from(L)
            True
            sage: e(L.simple_root(1))
            (1, -1, 0, 0)
        """
    def dimension(self) -> None:
        """
        Return the dimension of this ambient space.

        EXAMPLES::

            sage: from sage.combinat.root_system.ambient_space import AmbientSpace
            sage: e = RootSystem(['F',4]).ambient_space()
            sage: AmbientSpace.dimension(e)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    @classmethod
    def smallest_base_ring(cls, cartan_type=None):
        """
        Return the smallest ground ring over which the ambient space can be realized.

        This class method will get called with the Cartan type as
        input. This default implementation returns `\\QQ`; subclasses
        should override it as appropriate.

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: e.smallest_base_ring()
            Rational Field
        """
    def __call__(self, v):
        """
        TESTS::

            sage: R = RootSystem(['A',4]).ambient_lattice()
            sage: R([1,2,3,4,5])
            (1, 2, 3, 4, 5)
            sage: len(R([1,0,0,0,0]).monomial_coefficients())
            1
        """
    def __getitem__(self, i):
        """
        Note that indexing starts at 1.

        EXAMPLES::

            sage: e = RootSystem(['A',2]).ambient_lattice()
            sage: e[1]
            (1, 0, 0)
            sage: e[0]
            Traceback (most recent call last):
            ...
            IndexError: value out of range
        """
    def coroot_lattice(self):
        '''
        EXAMPLES::

            sage: e = RootSystem(["A", 3]).ambient_lattice()
            sage: e.coroot_lattice()
            Ambient lattice of the Root system of type [\'A\', 3]
        '''
    def simple_coroot(self, i):
        '''
        Return the `i`-th simple coroot, as an element of this space.

        EXAMPLES::

            sage: R = RootSystem(["A",3])
            sage: L = R.ambient_lattice()
            sage: L.simple_coroot(1)
            (1, -1, 0, 0)
            sage: L.simple_coroot(2)
            (0, 1, -1, 0)
            sage: L.simple_coroot(3)
            (0, 0, 1, -1)
        '''
    def reflection(self, root, coroot=None):
        '''
        EXAMPLES::

            sage: e = RootSystem(["A", 3]).ambient_lattice()
            sage: a = e.simple_root(0); a
            (-1, 0, 0, 0)
            sage: b = e.simple_root(1); b
            (1, -1, 0, 0)
            sage: s_a = e.reflection(a)
            sage: s_a(b)
            (0, -1, 0, 0)
        '''
    @cached_method
    def fundamental_weight(self, i):
        """
        Return the fundamental weight `\\Lambda_i` in ``self``.

        In several of the ambient spaces, it is more convenient to
        construct all fundamental weights at once. To support this, we
        provide this default implementation of ``fundamental_weight``
        using the method ``fundamental_weights``. Beware that this
        will cause a loop if neither ``fundamental_weight`` nor
        ``fundamental_weights`` is implemented.

        EXAMPLES::

            sage: e =  RootSystem(['F',4]).ambient_space()
            sage: e.fundamental_weight(3)
            (3/2, 1/2, 1/2, 1/2)

            sage: e =  RootSystem(['G',2]).ambient_space()
            sage: e.fundamental_weight(1)
            (1, 0, -1)

            sage: e =  RootSystem(['E',6]).ambient_space()
            sage: e.fundamental_weight(3)
            (-1/2, 1/2, 1/2, 1/2, 1/2, -5/6, -5/6, 5/6)
        """
    def from_vector_notation(self, weight, style: str = 'lattice'):
        '''
        INPUT:

        - ``weight`` -- a vector or tuple representing a weight

        Returns an element of ``self``. If the weight lattice is not
        of full rank, it coerces it into the weight lattice, or
        its ambient space by orthogonal projection. This arises
        in two cases: for SL(r+1), the weight lattice is
        contained in a hyperplane of codimension one in the ambient,
        space, and for types E6 and E7, the weight lattice is
        contained in a subspace of codimensions 2 or 3, respectively.

        If style="coroots" and the data is a tuple of integers, it
        is assumed that the data represent a linear combination of
        fundamental weights. If style=\'coroots\', and the root lattice
        is not of full rank in the ambient space, it is projected
        into the subspace corresponding to the semisimple derived group.
        This arises with Cartan type A, E6 and E7.

        EXAMPLES::

            sage: RootSystem("A2").ambient_space().from_vector_notation((1,0,0))
            (1, 0, 0)
            sage: RootSystem("A2").ambient_space().from_vector_notation([1,0,0])
            (1, 0, 0)
            sage: RootSystem("A2").ambient_space().from_vector_notation((1,0),style=\'coroots\')
            (2/3, -1/3, -1/3)
        '''
    def to_ambient_space_morphism(self):
        """
        Return the identity map on ``self``.

        This is present for uniformity of use; the corresponding method
        for abstract root and weight lattices/spaces, is not trivial.

        EXAMPLES::

            sage: P = RootSystem(['A',2]).ambient_space()
            sage: f = P.to_ambient_space_morphism()
            sage: p = P.an_element()
            sage: p
            (2, 2, 3)
            sage: f(p)
            (2, 2, 3)
            sage: f(p)==p
            True
        """

class AmbientSpaceElement(CombinatorialFreeModule.Element):
    def inner_product(self, lambdacheck):
        """
        The scalar product with elements of the ambient space.

        EXAMPLES::

            sage: e = RootSystem(['A',2]).ambient_space()
            sage: a = e.simple_root(0); a
            (-1, 0, 0)
            sage: a.inner_product(a)
            2

        TESTS:

        Verify that :issue:`15325` (A) is fixed::

            sage: rt = RootSystem(['E', 8])
            sage: lat = rt.root_lattice()
            sage: spc = rt.ambient_space()
            sage: spc.simple_root(1).scalar(lat.simple_coroot(2))
            0
        """
    scalar = inner_product
    dot_product = inner_product
    def associated_coroot(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: a = e.simple_root(0); a
            (1/2, -1/2, -1/2, -1/2)
            sage: a.associated_coroot()
            (1, -1, -1, -1)
        """
    def is_positive_root(self):
        """
        EXAMPLES::

            sage: R = RootSystem(['A',3]).ambient_space()
            sage: r=R.simple_root(1)+R.simple_root(2)
            sage: r.is_positive_root()
            True
            sage: r=R.simple_root(1)-R.simple_root(2)
            sage: r.is_positive_root()
            False
        """
    def coerce_to_sl(self):
        '''
        For type [\'A\',r], this coerces the element of the ambient space into the
        root space by orthogonal projection. The root space has codimension one
        and corresponds to the Lie algebra of SL(r+1,CC), whereas the full weight
        space corresponds to the Lie algebra of GL(r+1,CC). So this operation
        corresponds to multiplication by a (possibly fractional) power of the
        determinant to give a weight determinant one.

        EXAMPLES::

            sage: [fw.coerce_to_sl() for fw in RootSystem("A2").ambient_space().fundamental_weights()]
            [(2/3, -1/3, -1/3), (1/3, 1/3, -2/3)]
            sage: L = RootSystem("A2xA3").ambient_space()
            sage: L([1,2,3,4,5,0,0]).coerce_to_sl()
            (-1, 0, 1, 7/4, 11/4, -9/4, -9/4)
        '''
    def coerce_to_e7(self):
        '''
        For type E8, this orthogonally projects the given element of
        the E8 root lattice into the E7 root lattice. This operation on
        weights corresponds to intersection with the semisimple subgroup E7.

        EXAMPLES::

            sage: [b.coerce_to_e7() for b in RootSystem("E8").ambient_space().basis()]
            [(1, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0),
             (0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0),
             (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0),
             (0, 0, 0, 0, 0, 0, 1/2, -1/2), (0, 0, 0, 0, 0, 0, -1/2, 1/2)]
        '''
    def coerce_to_e6(self):
        '''
        For type E7 or E8, orthogonally projects an element of the root lattice
        into the E6 root lattice. This operation on weights corresponds to
        intersection with the semisimple subgroup E6.

        EXAMPLES::

            sage: [b.coerce_to_e6() for b in RootSystem("E8").ambient_space().basis()]
            [(1, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1/3, 1/3, -1/3),
            (0, 0, 0, 0, 0, 1/3, 1/3, -1/3), (0, 0, 0, 0, 0, -1/3, -1/3, 1/3)]
        '''
    def to_ambient(self):
        """
        Map ``self`` to the ambient space.

        This exists for uniformity. Its analogue for root and weight lattice realizations,
        is not trivial.

        EXAMPLES::

            sage: v = CartanType(['C',3]).root_system().ambient_space().an_element(); v
            (2, 2, 3)
            sage: v.to_ambient()
            (2, 2, 3)
        """
