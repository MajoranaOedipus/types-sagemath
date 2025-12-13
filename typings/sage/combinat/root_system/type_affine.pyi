from .weight_lattice_realizations import WeightLatticeRealizations as WeightLatticeRealizations
from _typeshed import Incomplete
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method

class AmbientSpace(CombinatorialFreeModule):
    '''
    Ambient space for affine types.

    This is constructed from the data in the corresponding classical
    ambient space. Namely, this space is obtained by adding two
    elements `\\delta` and `\\delta^\\vee` to the basis of the classical
    ambient space, and by endowing it with the canonical scalar product.

    The coefficient of an element in `\\delta^\\vee`, thus its scalar
    product with `\\delta^\\vee` gives its level, and dually for the
    colevel. The canonical projection onto the classical ambient space
    (by killing `\\delta` and `\\delta^\\vee`) maps the simple roots
    (except `\\alpha_0`) onto the corresponding classical simple roots,
    and similarly for the coroots, fundamental weights, ...
    Altogether, this uniquely determines the embedding of the root,
    coroot, weight, and coweight lattices. See :meth:`simple_root` and
    :meth:`fundamental_weight` for the details.

    .. WARNING::

        In type `BC`, the null root is in fact::

            sage: R = RootSystem(["BC",3,2]).ambient_space()
            sage: R.null_root()                                                         # needs sage.graphs
            2*e[\'delta\']

    .. WARNING::

        In the literature one often considers a larger affine ambient
        space obtained from the classical ambient space by adding four
        dimensions, namely for the fundamental weight `\\Lambda_0` the
        fundamental coweight `\\Lambda^\\vee_0`, the null root `\\delta`,
        and the null coroot `c` (aka central element).  In this larger
        ambient space, the scalar product is degenerate: `\\langle
        \\delta,\\delta\\rangle=0` and similarly for the null coroot.

        In the current implementation, `\\Lambda_0` and the null coroot
        are identified::

            sage: L = RootSystem(["A",3,1]).ambient_space()
            sage: Lambda = L.fundamental_weights()                                      # needs sage.graphs
            sage: Lambda[0]                                                             # needs sage.graphs
            e[\'deltacheck\']
            sage: L.null_coroot()                                                       # needs sage.graphs
            e[\'deltacheck\']

        Therefore the scalar product of the null coroot with itself
        differs from the larger ambient space::

            sage: L.null_coroot().scalar(L.null_coroot())                               # needs sage.graphs
            1

        In general, scalar products between two elements that do not
        live on "opposite sides" won\'t necessarily match.

    EXAMPLES::

        sage: R = RootSystem(["A",3,1])
        sage: e = R.ambient_space(); e
        Ambient space of the Root system of type [\'A\', 3, 1]
        sage: TestSuite(e).run()

    Systematic checks on all affine types::

        sage: for ct in CartanType.samples(affine=True, crystallographic=True):
        ....:     if ct.classical().root_system().ambient_space() is not None:
        ....:         print(ct)
        ....:         L = ct.root_system().ambient_space()
        ....:         assert L
        ....:         TestSuite(L).run()
        [\'A\', 1, 1]
        [\'A\', 5, 1]
        [\'B\', 1, 1]
        [\'B\', 5, 1]
        [\'C\', 1, 1]
        [\'C\', 5, 1]
        [\'D\', 3, 1]
        [\'D\', 5, 1]
        [\'E\', 6, 1]
        [\'E\', 7, 1]
        [\'E\', 8, 1]
        [\'F\', 4, 1]
        [\'G\', 2, 1]
        [\'BC\', 1, 2]
        [\'BC\', 5, 2]
        [\'B\', 5, 1]^*
        [\'C\', 4, 1]^*
        [\'F\', 4, 1]^*
        [\'G\', 2, 1]^*
        [\'BC\', 1, 2]^*
        [\'BC\', 5, 2]^*

    TESTS::

        sage: Lambda[1]                                                                 # needs sage.graphs
        e[0] + e[\'deltacheck\']
    '''
    @classmethod
    def smallest_base_ring(cls, cartan_type):
        '''
        Return the smallest base ring the ambient space can be defined on.

        This is the smallest base ring for the associated classical
        ambient space.

        .. SEEALSO:: :meth:`~sage.combinat.root_system.ambient_space.AmbientSpace.smallest_base_ring`

        EXAMPLES::

            sage: cartan_type = CartanType(["A",3,1])
            sage: cartan_type.AmbientSpace.smallest_base_ring(cartan_type)
            Integer Ring
            sage: cartan_type = CartanType(["B",3,1])
            sage: cartan_type.AmbientSpace.smallest_base_ring(cartan_type)
            Rational Field
        '''
    root_system: Incomplete
    def __init__(self, root_system, base_ring) -> None:
        '''
        EXAMPLES::

            sage: R = RootSystem(["A",3,1])
            sage: R.cartan_type().AmbientSpace
            <class \'sage.combinat.root_system.type_affine.AmbientSpace\'>
            sage: e = R.ambient_space(); e
            Ambient space of the Root system of type [\'A\', 3, 1]
            sage: TestSuite(R.ambient_space()).run()

            sage: L = RootSystem([\'A\',3]).coroot_lattice()
            sage: e.has_coerce_map_from(L)
            True
            sage: e(L.simple_root(1))
            e[0] - e[1]
        '''
    def is_extended(self):
        """
        Return whether this is a realization of the extended weight lattice: yes!

        .. SEEALSO::

            - :class:`sage.combinat.root_system.weight_space.WeightSpace`
            - :meth:`sage.combinat.root_system.weight_lattice_realizations.WeightLatticeRealizations.ParentMethods.is_extended`

        EXAMPLES::

            sage: RootSystem(['A',3,1]).ambient_space().is_extended()
            True
        """
    @cached_method
    def fundamental_weight(self, i):
        '''
        Return the fundamental weight `\\Lambda_i` in this ambient space.

        It is constructed by taking the corresponding fundamental
        weight of the classical ambient space (or `0` for `\\Lambda_0`)
        and raising it to the appropriate level by adding a suitable
        multiple of `\\delta^\\vee`.

        EXAMPLES::

            sage: RootSystem([\'A\',3,1]).ambient_space().fundamental_weight(2)           # needs sage.graphs
            e[0] + e[1] + e[\'deltacheck\']
            sage: RootSystem([\'A\',3,1]).ambient_space().fundamental_weights()           # needs sage.graphs
            Finite family {0: e[\'deltacheck\'],
                           1: e[0] + e[\'deltacheck\'],
                           2: e[0] + e[1] + e[\'deltacheck\'],
                           3: e[0] + e[1] + e[2] + e[\'deltacheck\']}
            sage: RootSystem([\'A\',3]).ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1, 1, 1, 0)}
            sage: A31wl = RootSystem([\'A\',3,1]).weight_lattice()
            sage: A31wl.fundamental_weights().map(attrcall("level"))                    # needs sage.graphs
            Finite family {0: 1, 1: 1, 2: 1, 3: 1}

            sage: RootSystem([\'B\',3,1]).ambient_space().fundamental_weights()           # needs sage.graphs
            Finite family {0: e[\'deltacheck\'],
                           1: e[0] + e[\'deltacheck\'],
                           2: e[0] + e[1] + 2*e[\'deltacheck\'],
                           3: 1/2*e[0] + 1/2*e[1] + 1/2*e[2] + e[\'deltacheck\']}
            sage: RootSystem([\'B\',3]).ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0), 2: (1, 1, 0), 3: (1/2, 1/2, 1/2)}
            sage: B31wl = RootSystem([\'B\',3,1]).weight_lattice()
            sage: B31wl.fundamental_weights().map(attrcall("level"))                    # needs sage.graphs
            Finite family {0: 1, 1: 1, 2: 2, 3: 1}

        In type `BC` dual, the coefficient of \'\\delta^\\vee\' is the level
        divided by `2` to take into account that the null coroot is
        `2\\delta^\\vee`::

            sage: R = CartanType([\'BC\',3,2]).dual().root_system()
            sage: R.ambient_space().fundamental_weights()                               # needs sage.graphs
            Finite family {0: e[\'deltacheck\'],
                           1: e[0] + e[\'deltacheck\'],
                           2: e[0] + e[1] + e[\'deltacheck\'],
                           3: 1/2*e[0] + 1/2*e[1] + 1/2*e[2] + 1/2*e[\'deltacheck\']}
            sage: R.weight_lattice().fundamental_weights().map(attrcall("level"))       # needs sage.graphs
            Finite family {0: 2, 1: 2, 2: 2, 3: 1}
            sage: R.ambient_space().null_coroot()                                       # needs sage.graphs
            2*e[\'deltacheck\']

        By a slight naming abuse this function also accepts "delta" as
        input so that it can be used to implement the embedding from
        the extended weight lattice::

            sage: RootSystem([\'A\',3,1]).ambient_space().fundamental_weight("delta")
            e[\'delta\']
        '''
    @cached_method
    def simple_root(self, i):
        '''
        Return the `i`-th simple root of this affine ambient space.

        EXAMPLES:

        It is built straightforwardly from the corresponding simple
        root `\\alpha_i` in the classical ambient space::

            sage: RootSystem(["A",3,1]).ambient_space().simple_root(1)
            e[0] - e[1]

        For the special node (typically `i=0`), `\\alpha_0` is built
        from the other simple roots using the column annihilator of
        the Cartan matrix and adding `\\delta`, where `\\delta` is the
        null root::

            sage: RootSystem(["A",3]).ambient_space().simple_roots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1)}
            sage: RootSystem(["A",3,1]).ambient_space().simple_roots()                  # needs sage.graphs
            Finite family {0: -e[0] + e[3] + e[\'delta\'], 1: e[0] - e[1],
                           2: e[1] - e[2], 3: e[2] - e[3]}

        Here is a twisted affine example::

            sage: B31v = RootSystem(CartanType(["B",3,1]).dual())
            sage: B31v.ambient_space().simple_roots()                                   # needs sage.graphs
            Finite family {0: -e[0] - e[1] + e[\'delta\'], 1: e[0] - e[1],
                           2: e[1] - e[2], 3: 2*e[2]}

        In fact `\\delta` is really `1/a_0` times the null root (see
        the discussion in :class:`~sage.combinat.root_system.weight_space.WeightSpace`)
        but this only makes a difference in type `BC`::

            sage: L = RootSystem(CartanType(["BC",3,2])).ambient_space()
            sage: L.simple_roots()                                                      # needs sage.graphs
            Finite family {0: -e[0] + e[\'delta\'], 1: e[0] - e[1],
                           2: e[1] - e[2], 3: 2*e[2]}
            sage: L.null_root()                                                         # needs sage.graphs
            2*e[\'delta\']

        .. NOTE::

            An alternative would have been to use the default
            implementation of the simple roots as linear combinations
            of the fundamental weights. However, as in type `A_n` it is
            preferable to take a slight variant to avoid rational
            coefficient (the usual `GL_n` vs `SL_n` issue).

        .. SEEALSO::

            - :meth:`~sage.combinat.root_system.weight_space.WeightSpace.simple_root`
            - :class:`~sage.combinat.root_system.weight_space.WeightSpace`
            - :meth:`CartanType.col_annihilator`
            - :meth:`null_root`
        '''
    @cached_method
    def simple_coroot(self, i):
        '''
        Return the `i`-th simple coroot `\\alpha_i^\\vee` of this affine ambient space.

        EXAMPLES::

            sage: RootSystem(["A",3,1]).ambient_space().simple_coroot(1)
            e[0] - e[1]

        It is built as the coroot associated to the simple root
        `\\alpha_i`::

            sage: RootSystem(["B",3,1]).ambient_space().simple_roots()                  # needs sage.graphs
            Finite family {0: -e[0] - e[1] + e[\'delta\'], 1: e[0] - e[1],
                           2: e[1] - e[2], 3: e[2]}
            sage: RootSystem(["B",3,1]).ambient_space().simple_coroots()                # needs sage.graphs
            Finite family {0: -e[0] - e[1] + e[\'deltacheck\'], 1: e[0] - e[1],
                           2: e[1] - e[2], 3: 2*e[2]}

        .. TODO:: Factor out this code with the classical ambient space.
        '''
    def coroot_lattice(self):
        '''
        EXAMPLES::

            sage: RootSystem(["A",3,1]).ambient_lattice().coroot_lattice()
            Ambient lattice of the Root system of type [\'A\', 3, 1]

        .. TODO:: Factor out this code with the classical ambient space.
        '''
    class Element(CombinatorialFreeModule.Element):
        def inner_product(self, other):
            """
            Implement the canonical inner product of ``self`` with ``other``.

            EXAMPLES::

                sage: e = RootSystem(['B',3,1]).ambient_space()
                sage: B = e.basis()
                sage: matrix([[x.inner_product(y) for x in B] for y in B])
                [1 0 0 0 0]
                [0 1 0 0 0]
                [0 0 1 0 0]
                [0 0 0 1 0]
                [0 0 0 0 1]
                sage: x = e.an_element(); x
                2*e[0] + 2*e[1] + 3*e[2]
                sage: x.inner_product(x)
                17

            :meth:`scalar` is an alias for this method::

                sage: x.scalar(x)
                17

            .. TODO:: Lift to CombinatorialFreeModule.Element as canonical_inner_product
            """
        scalar = inner_product
        def associated_coroot(self):
            """
            Return the coroot associated to ``self``.

            INPUT:

            - ``self`` -- a root

            EXAMPLES::

                sage: # needs sage.graphs
                sage: alpha = RootSystem(['C',2,1]).ambient_space().simple_roots()
                sage: alpha
                Finite family {0: -2*e[0] + e['delta'], 1: e[0] - e[1], 2: 2*e[1]}
                sage: alpha[0].associated_coroot()
                -e[0] + e['deltacheck']
                sage: alpha[1].associated_coroot()
                e[0] - e[1]
                sage: alpha[2].associated_coroot()
                e[1]
            """
