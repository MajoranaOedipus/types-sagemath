from _typeshed import Incomplete
from sage.combinat.root_system import ambient_space as ambient_space, cartan_type as cartan_type
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.call import attrcall as attrcall
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class CartanType(cartan_type.CartanType_decorator, cartan_type.CartanType_crystallographic):
    '''
    A class for dual Cartan types.

    The dual of a (crystallographic) Cartan type is a Cartan type with
    the same index set, but all arrows reversed in the Dynkin diagram
    (otherwise said, the Cartan matrix is transposed). It shares a lot
    of properties in common with its dual. In particular, the Weyl
    group is isomorphic to that of the dual as a Coxeter group.

    EXAMPLES:

    For all finite Cartan types, and in particular the simply laced
    ones, the dual Cartan type is given by another preexisting Cartan
    type::

        sage: CartanType([\'A\',4]).dual()
        [\'A\', 4]
        sage: CartanType([\'B\',4]).dual()
        [\'C\', 4]
        sage: CartanType([\'C\',4]).dual()
        [\'B\', 4]
        sage: CartanType([\'F\',4]).dual()
        [\'F\', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}

    So to exercise this class we consider some non simply laced affine
    Cartan types and also create explicitly `F_4^*` as a dual cartan
    type::

        sage: from sage.combinat.root_system.type_dual import CartanType as CartanTypeDual
        sage: F4d = CartanTypeDual(CartanType([\'F\',4])); F4d
        [\'F\', 4]^*
        sage: G21d = CartanType([\'G\',2,1]).dual(); G21d
        [\'G\', 2, 1]^*

    They share many properties with their original Cartan types::

        sage: F4d.is_irreducible()
        True
        sage: F4d.is_crystallographic()
        True
        sage: F4d.is_simply_laced()
        False
        sage: F4d.is_finite()
        True
        sage: G21d.is_finite()
        False
        sage: F4d.is_affine()
        False
        sage: G21d.is_affine()
        True

    TESTS::

        sage: TestSuite(F4d).run(skip=["_test_pickling"])
        sage: TestSuite(G21d).run()

    .. NOTE:: F4d is pickled by construction as F4.dual() hence the above failure.
    '''
    __class__: Incomplete
    def __init__(self, type) -> None:
        '''
        INPUT:

        - ``type`` -- a Cartan type

        EXAMPLES::

           sage: ct = CartanType([\'F\',4,1]).dual()
           sage: TestSuite(ct).run()

        TESTS::

            sage: ct1 = CartanType([\'B\',3,1]).dual()
            sage: ct2 = CartanType([\'B\',3,1]).dual()
            sage: ct3 = CartanType([\'D\',4,1]).dual()
            sage: ct1 == ct2
            True
            sage: ct1 == ct3
            False

        Test that the produced Cartan type is in the appropriate
        abstract classes (see :issue:`13724`)::

            sage: from sage.combinat.root_system import cartan_type
            sage: ct = CartanType([\'B\',3,1]).dual()
            sage: TestSuite(ct).run()
            sage: isinstance(ct, cartan_type.CartanType_simple)
            True
            sage: isinstance(ct, cartan_type.CartanType_finite)
            False
            sage: isinstance(ct, cartan_type.CartanType_affine)
            True
            sage: isinstance(ct, cartan_type.CartanType_crystallographic)
            True
            sage: isinstance(ct, cartan_type.CartanType_simply_laced)
            False

        By default, the dual of a reducible and finite type is not
        constructed as such::

            sage: ct = CartanType([[\'B\',4],[\'A\',2]]).dual(); ct
            C4xA2

        In order to exercise the dual infrastructure we force the
        construction as a dual::

            sage: from sage.combinat.root_system import type_dual
            sage: ct = type_dual.CartanType(CartanType([[\'B\',4],[\'A\',2]])); ct
            B4xA2^*
            sage: isinstance(ct, type_dual.CartanType)
            True
            sage: TestSuite(ct).run(skip=["_test_pickling"])
            sage: isinstance(ct, cartan_type.CartanType_finite)
            True
            sage: isinstance(ct, cartan_type.CartanType_simple)
            False
            sage: isinstance(ct, cartan_type.CartanType_affine)
            False
            sage: isinstance(ct, cartan_type.CartanType_crystallographic)
            True
            sage: isinstance(ct, cartan_type.CartanType_simply_laced)
            False
        '''
    def __reduce__(self):
        """
        TESTS::

            sage: CartanType(['F', 4, 1]).dual().__reduce__()
            (*.dual(), (['F', 4, 1],))
        """
    def ascii_art(self, label=None, node=None):
        '''
        Return an ascii art representation of this Cartan type.

        (by hacking the ascii art representation of the dual Cartan type)

        EXAMPLES::

            sage: print(CartanType(["B", 3, 1]).dual().ascii_art())
                O 0
                |
                |
            O---O=<=O
            1   2   3
            sage: print(CartanType(["C", 4, 1]).dual().ascii_art())
            O=<=O---O---O=>=O
            0   1   2   3   4
            sage: print(CartanType(["G", 2, 1]).dual().ascii_art())
              3
            O=>=O---O
            1   2   0
            sage: print(CartanType(["F", 4, 1]).dual().ascii_art())
            O---O---O=<=O---O
            0   1   2   3   4
            sage: print(CartanType(["BC", 4, 2]).dual().ascii_art())
            O=>=O---O---O=>=O
            0   1   2   3   4
        '''
    def __eq__(self, other):
        """
        Return whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: B41 = CartanType(['B', 4, 1])
            sage: B41dual = CartanType(['B', 4, 1]).dual()
            sage: F41dual = CartanType(['F', 4, 1]).dual()

            sage: F41dual == F41dual
            True
            sage: F41dual == B41dual
            False
            sage: B41dual == B41
            False
        """
    def __ne__(self, other):
        """
        Return whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: B41 = CartanType(['B', 4, 1])
            sage: B41dual = CartanType(['B', 4, 1]).dual()
            sage: F41dual = CartanType(['F', 4, 1]).dual()

            sage: F41dual != F41dual
            False
            sage: F41dual != B41dual
            True
            sage: B41dual != B41
            True
        """
    def __hash__(self):
        """
        Compute the hash of ``self``.

        EXAMPLES::

            sage: B41 = CartanType(['B', 4, 1])
            sage: B41dual = CartanType(['B', 4, 1]).dual()
            sage: h = hash(B41dual)
        """
    def dual(self):
        """
        EXAMPLES::

           sage: ct = CartanType(['F', 4, 1]).dual()
           sage: ct.dual()
           ['F', 4, 1]
        """
    def dynkin_diagram(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['F', 4, 1]).dual()
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O---O---O=<=O---O
            0   1   2   3   4
            F4~*
        """

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    Ambient space for a dual finite Cartan type.

    It is constructed in the canonical way from the ambient space of
    the original Cartan type by switching the roles of simple roots,
    fundamental weights, etc.

    .. NOTE::

        Recall that, for any finite Cartan type, and in particular the
        a simply laced one, the dual Cartan type is constructed as
        another preexisting Cartan type. Furthermore the ambient space
        for an affine type is constructed from the ambient space for
        its classical type. Thus this code is not actually currently
        used.

        It is kept for cross-checking and for reference in case it
        could become useful, e.g., for dual of general Kac-Moody
        types.

        For the doctests, we need to explicitly create a dual type.
        Subsequently, since reconstruction of the dual of type `F_4`
        is the relabelled Cartan type, pickling fails on the
        ``TestSuite`` run.

    EXAMPLES::

        sage: ct = sage.combinat.root_system.type_dual.CartanType(CartanType([\'F\',4]))
        sage: L = ct.root_system().ambient_space(); L
        Ambient space of the Root system of type [\'F\', 4]^*
        sage: TestSuite(L).run(skip=["_test_elements","_test_pickling"])                # needs sage.graphs
    '''
    def dimension(self):
        """
        Return the dimension of this ambient space.

        .. SEEALSO:: :meth:`sage.combinat.root_system.ambient_space.AmbientSpace.dimension`

        EXAMPLES::

            sage: ct = sage.combinat.root_system.type_dual.CartanType(CartanType(['F',4]))
            sage: L = ct.root_system().ambient_space()
            sage: L.dimension()
            4
        """
    @cached_method
    def simple_root(self, i):
        """
        Return the ``i``-th simple root.

        It is constructed by looking up the corresponding simple
        coroot in the ambient space for the dual Cartan type.

        EXAMPLES::

            sage: ct = sage.combinat.root_system.type_dual.CartanType(CartanType(['F',4]))
            sage: ct.root_system().ambient_space().simple_root(1)
            (0, 1, -1, 0)

            sage: ct.root_system().ambient_space().simple_roots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 2), 4: (1, -1, -1, -1)}

            sage: ct.dual().root_system().ambient_space().simple_coroots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 2), 4: (1, -1, -1, -1)}

        Note that this ambient space is isomorphic, but not equal, to
        that obtained by constructing `F_4` dual by relabelling::

            sage: ct = CartanType(['F',4]).dual(); ct
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: ct.root_system().ambient_space().simple_roots()
            Finite family {1: (1/2, -1/2, -1/2, -1/2), 2: (0, 0, 0, 1), 3: (0, 0, 1, -1), 4: (0, 1, -1, 0)}
        """
    @cached_method
    def fundamental_weights(self):
        """
        Return the fundamental weights.

        They are computed from the simple roots by inverting the
        Cartan matrix. This is acceptable since this is only about
        ambient spaces for finite Cartan types. Also, we do not have
        to worry about the usual `GL_n` vs `SL_n` catch because type
        `A` is self dual.

        An alternative would have been to start from the fundamental
        coweights in the dual ambient space, but those are not yet
        implemented.

        EXAMPLES::

            sage: ct = sage.combinat.root_system.type_dual.CartanType(CartanType(['F',4]))
            sage: L = ct.root_system().ambient_space()
            sage: L.fundamental_weights()                                               # needs sage.graphs
            Finite family {1: (1, 1, 0, 0), 2: (2, 1, 1, 0), 3: (3, 1, 1, 1), 4: (2, 0, 0, 0)}

        Note that this ambient space is isomorphic, but not equal, to
        that obtained by constructing `F_4` dual by relabelling::

            sage: ct = CartanType(['F',4]).dual(); ct
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: ct.root_system().ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (3/2, 1/2, 1/2, 1/2), 3: (2, 1, 1, 0), 4: (1, 1, 0, 0)}
        """

class CartanType_finite(CartanType, cartan_type.CartanType_finite):
    AmbientSpace = AmbientSpace

class CartanType_affine(CartanType, cartan_type.CartanType_affine):
    def classical(self):
        """
        Return the classical Cartan type associated with ``self`` (which should
        be affine).

        EXAMPLES::

            sage: CartanType(['A',3,1]).dual().classical()
            ['A', 3]
            sage: CartanType(['B',3,1]).dual().classical()
            ['C', 3]
            sage: CartanType(['F',4,1]).dual().classical()
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: CartanType(['BC',4,2]).dual().classical()
            ['B', 4]
        """
    def basic_untwisted(self):
        """
        Return the basic untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic untwisted type is `X_n`.
        In other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: CartanType(['A', 7, 2]).basic_untwisted()
            ['A', 7]
            sage: CartanType(['E', 6, 2]).basic_untwisted()
            ['E', 6]
            sage: CartanType(['D', 4, 3]).basic_untwisted()
            ['D', 4]
        """
    def special_node(self):
        """
        Implement :meth:`CartanType_affine.special_node`.

        The special node of the dual of an affine type `T` is the
        special node of `T`.

        EXAMPLES::

            sage: CartanType(['A',3,1]).dual().special_node()
            0
            sage: CartanType(['B',3,1]).dual().special_node()
            0
            sage: CartanType(['F',4,1]).dual().special_node()
            0
            sage: CartanType(['BC',4,2]).dual().special_node()
            0
        """
