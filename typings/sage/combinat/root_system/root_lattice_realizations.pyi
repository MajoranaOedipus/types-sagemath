from _typeshed import Incomplete
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.combinat.root_system.plot import PlotOptions as PlotOptions, barycentric_projection_matrix as barycentric_projection_matrix
from sage.matrix.constructor import matrix as matrix
from sage.misc.abstract_method import AbstractMethod as AbstractMethod, abstract_method as abstract_method
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.call import attrcall as attrcall
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet
from sage.structure.element import Element as Element

class RootLatticeRealizations(Category_over_base_ring):
    '''
    The category of root lattice realizations over a given base ring.

    A *root lattice realization* `L` over a base ring `R` is a free
    module (or vector space if `R` is a field) endowed with an embedding
    of the root lattice of some root system.

    Typical root lattice realizations over `\\ZZ` include the root
    lattice, weight lattice, and ambient lattice. Typical root lattice
    realizations over `\\QQ` include the root space, weight space, and
    ambient space.

    To describe the embedding, a root lattice realization must
    implement a method
    :meth:`~RootLatticeRealizations.ParentMethods.simple_root`
    returning for each `i` in the index set the image of the simple root
    `\\alpha_i` under the embedding.

    A root lattice realization must further implement a method on elements
    :meth:`~RootLatticeRealizations.ElementMethods.scalar`, computing
    the scalar product with elements of the coroot lattice or coroot space.

    Using those, this category provides tools for reflections, roots,
    the Weyl group and its action, ...

    .. SEEALSO::

        - :class:`~sage.combinat.root_system.root_system.RootSystem`
        - :class:`~sage.combinat.root_system.weight_lattice_realizations.WeightLatticeRealizations`
        - :class:`~sage.combinat.root_system.root_space.RootSpace`
        - :class:`~sage.combinat.root_system.weight_space.WeightSpace`
        - :class:`~sage.combinat.root_system.ambient_space.AmbientSpace`

    EXAMPLES:

    Here, we consider the root system of type `A_7`, and embed the root
    lattice element `x = \\alpha_2 + 2 \\alpha_6` in several root lattice
    realizations::

        sage: R = RootSystem(["A",7])
        sage: alpha = R.root_lattice().simple_roots()
        sage: x = alpha[2] + 2 * alpha[5]

        sage: L = R.root_space()
        sage: L(x)
        alpha[2] + 2*alpha[5]

        sage: L = R.weight_lattice()
        sage: L(x)                                                                      # needs sage.graphs
        -Lambda[1] + 2*Lambda[2] - Lambda[3] - 2*Lambda[4] + 4*Lambda[5] - 2*Lambda[6]

        sage: L = R.ambient_space()
        sage: L(x)
        (0, 1, -1, 0, 2, -2, 0, 0)

    We embed the root space element `x = \\alpha_2 + 1/2 \\alpha_6` in
    several root lattice realizations::

        sage: alpha = R.root_space().simple_roots()
        sage: x = alpha[2] + 1/2 * alpha[5]

        sage: L = R.weight_space()
        sage: L(x)                                                                      # needs sage.graphs
        -Lambda[1] + 2*Lambda[2] - Lambda[3] - 1/2*Lambda[4] + Lambda[5] - 1/2*Lambda[6]

        sage: L = R.ambient_space()
        sage: L(x)
        (0, 1, -1, 0, 1/2, -1/2, 0, 0)

    Of course, one can\'t embed the root space in the weight lattice::

        sage: L = R.weight_lattice()
        sage: L(x)
        Traceback (most recent call last):
        ...
        TypeError: do not know how to make x (= alpha[2] + 1/2*alpha[5])
        an element of self (=Weight lattice of the Root system of type [\'A\', 7])

    If `K_1` is a subring of `K_2`, then one could in theory have
    an embedding from the root space over `K_1` to any root
    lattice realization over `K_2`; this is not implemented::

        sage: K1 = QQ
        sage: K2 = QQ[\'q\']
        sage: L = R.weight_space(K2)

        sage: alpha = R.root_space(K2).simple_roots()
        sage: L(alpha[1])                                                               # needs sage.graphs
        2*Lambda[1] - Lambda[2]

        sage: alpha = R.root_space(K1).simple_roots()
        sage: L(alpha[1])
        Traceback (most recent call last):
        ...
        TypeError: do not know how to make x (= alpha[1]) an element of self
        (=Weight space over the Univariate Polynomial Ring in q
        over Rational Field of the Root system of type [\'A\', 7])

    By a slight abuse, the embedding of the root lattice is not actually
    required to be faithful. Typically for an affine root system, the
    null root of the root lattice is killed in the non extended weight
    lattice::

        sage: R = RootSystem(["A", 3, 1])
        sage: delta = R.root_lattice().null_root()                                      # needs sage.graphs
        sage: L = R.weight_lattice()
        sage: L(delta)                                                                  # needs sage.graphs
        0

    TESTS::

        sage: TestSuite(L).run()                                                        # needs sage.graphs
    '''
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations
            sage: RootLatticeRealizations(QQ).super_categories()
            [Category of vector spaces with basis over Rational Field]
        """
    Algebras: Incomplete
    class ParentMethods:
        def __init_extra__(self) -> None:
            '''
            Register the embedding of the root lattice into ``self``.

            Also registers the embedding of the root space over the same
            base field `K` into ``self`` if `K` is not `\\ZZ`.

            EXAMPLES:

            We embed the simple root `\\alpha_2` of the root lattice in
            the weight lattice::

                sage: R = RootSystem(["A",3])
                sage: alpha = R.root_lattice().simple_roots()
                sage: L = R.weight_lattice()
                sage: L(alpha[2])                                                       # needs sage.graphs
                -Lambda[1] + 2*Lambda[2] - Lambda[3]

            .. NOTE::

                More examples are given in :class:`RootLatticeRealizations`;
                The embeddings are systematically tested in
                :meth:`_test_root_lattice_realization`.
            '''
        def cartan_type(self):
            """
            EXAMPLES::

                sage: r = RootSystem(['A',4]).root_space()
                sage: r.cartan_type()
                ['A', 4]
            """
        def index_set(self):
            """
            EXAMPLES::

                sage: r = RootSystem(['A',4]).root_space()
                sage: r.index_set()
                (1, 2, 3, 4)
            """
        def dynkin_diagram(self):
            """
            EXAMPLES::

                sage: r = RootSystem(['A',4]).root_space()
                sage: r.dynkin_diagram()                                                # needs sage.graphs
                O---O---O---O
                1   2   3   4
                A4
            """
        def some_elements(self):
            '''
            Return some elements of this root lattice realization.

            EXAMPLES::

                sage: L = RootSystem(["A",2]).weight_lattice()
                sage: L.some_elements()                                                 # needs sage.graphs
                [2*Lambda[1] + 2*Lambda[2], 2*Lambda[1] - Lambda[2],
                 -Lambda[1] + 2*Lambda[2], Lambda[1], Lambda[2]]
                sage: L = RootSystem(["A",2]).root_lattice()
                sage: L.some_elements()
                [2*alpha[1] + 2*alpha[2], alpha[1], alpha[2]]
            '''
        @cached_method
        def highest_root(self):
            """
            Return the highest root (for an irreducible finite root system).

            EXAMPLES::

                sage: RootSystem(['A',4]).ambient_space().highest_root()
                (1, 0, 0, 0, -1)

                sage: RootSystem(['E',6]).weight_space().highest_root()                 # needs sage.graphs
                Lambda[2]
            """
        @cached_method
        def a_long_simple_root(self):
            """
            Return a long simple root, corresponding to the highest outgoing edge
            in the Dynkin diagram.

            .. warning::

                This may be broken in affine type `A_{2n}^{(2)}`

                Is it meaningful/broken for non irreducible?

            .. TODO::

                implement CartanType.nodes_by_length as in
                MuPAD-Combinat (using CartanType.symmetrizer), and use it
                here.

            TESTS::

                sage: X = RootSystem(['A',1]).weight_space()
                sage: X.a_long_simple_root()                                            # needs sage.graphs
                2*Lambda[1]
                sage: X = RootSystem(['A',5]).weight_space()
                sage: X.a_long_simple_root()                                            # needs sage.graphs
                2*Lambda[1] - Lambda[2]
            """
        @abstract_method
        def simple_root(self, i) -> None:
            '''
            Return the `i`-th simple root.

            This should be overridden by any subclass, and typically
            implemented as a cached method for efficiency.

            EXAMPLES::

                sage: r = RootSystem(["A",3]).root_lattice()
                sage: r.simple_root(1)
                alpha[1]

            TESTS::

                sage: super(sage.combinat.root_system.root_space.RootSpace, r).simple_root(1)
                Traceback (most recent call last):
                ...
                NotImplementedError: <abstract method simple_root at ...>
            '''
        @cached_method
        def simple_roots(self):
            '''
            Return the family `(\\alpha_i)_{i\\in I}` of the simple roots.

            EXAMPLES::

                sage: alpha = RootSystem(["A",3]).root_lattice().simple_roots()
                sage: [alpha[i] for i in [1,2,3]]
                [alpha[1], alpha[2], alpha[3]]
            '''
        @cached_method
        def alpha(self):
            '''
            Return the family `(\\alpha_i)_{i\\in I}` of the simple roots,
            with the extra feature that, for simple irreducible root
            systems, `\\alpha_0` yields the opposite of the highest root.

            EXAMPLES::

                sage: alpha = RootSystem(["A",2]).root_lattice().alpha()
                sage: alpha[1]
                alpha[1]
                sage: alpha[0]                                                          # needs sage.graphs
                -alpha[1] - alpha[2]
            '''
        @cached_method
        def basic_imaginary_roots(self):
            """
            Return the basic imaginary roots of ``self``.

            The basic imaginary roots `\\delta` are the set of imaginary roots
            in `-C^{\\vee}` where `C` is the dominant chamber (i.e.,
            `\\langle \\beta, \\alpha_i^{\\vee} \\rangle \\leq 0` for all `i \\in I`).
            All imaginary roots are `W`-conjugate to a simple imaginary root.

            EXAMPLES::

                sage: RootSystem(['A', 2]).root_lattice().basic_imaginary_roots()
                ()
                sage: Q = RootSystem(['A', 2, 1]).root_lattice()
                sage: Q.basic_imaginary_roots()                                         # needs sage.graphs
                (alpha[0] + alpha[1] + alpha[2],)
                sage: delta = Q.basic_imaginary_roots()[0]                              # needs sage.graphs
                sage: all(delta.scalar(Q.simple_coroot(i)) <= 0                         # needs sage.graphs
                ....:     for i in Q.index_set())
                True
            """
        @cached_method
        def simple_roots_tilde(self):
            '''
            Return the family `(\\tilde\\alpha_i)_{i\\in I}` of the simple roots.

            INPUT:

            - ``self`` -- an affine root lattice realization

            The `\\tilde \\alpha_i` give the embedding of the root
            lattice of the other affinization of the same classical
            root lattice into this root lattice (space?).

            This uses the fact that `\\alpha_i = \\tilde \\alpha_i` for
            `i` not a special node, and that

            .. MATH::

                \\delta = \\sum a_i \\alpha_i = \\sum b_i \\tilde \\alpha_i

            EXAMPLES:

            In simply laced cases, this is boring::

                sage: RootSystem(["A",3, 1]).root_lattice().simple_roots_tilde()        # needs sage.graphs
                Finite family {0: alpha[0], 1: alpha[1], 2: alpha[2], 3: alpha[3]}

            This was checked by hand::

                sage: RootSystem(["C",2,1]).coroot_lattice().simple_roots_tilde()       # needs sage.graphs
                Finite family {0: alphacheck[0] - alphacheck[2],
                               1: alphacheck[1],
                               2: alphacheck[2]}
                sage: RootSystem(["B",2,1]).coroot_lattice().simple_roots_tilde()       # needs sage.graphs
                Finite family {0: alphacheck[0] - alphacheck[1],
                               1: alphacheck[1],
                               2: alphacheck[2]}

            What about type BC?
            '''
        def roots(self):
            '''
            Return the roots of ``self``.

            EXAMPLES::

                sage: RootSystem([\'A\',2]).ambient_lattice().roots()
                [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]

            This matches with :wikipedia:`Root_systems`::

                sage: for T in CartanType.samples(finite=True, crystallographic=True):  # needs sage.graphs
                ....:     print("%s %3s %3s"%(T, len(RootSystem(T).root_lattice().roots()),
                ....:                            len(RootSystem(T).weight_lattice().roots())))
                [\'A\', 1]   2   2
                [\'A\', 5]  30  30
                [\'B\', 1]   2   2
                [\'B\', 5]  50  50
                [\'C\', 1]   2   2
                [\'C\', 5]  50  50
                [\'D\', 2]   4   4
                [\'D\', 3]  12  12
                [\'D\', 5]  40  40
                [\'E\', 6]  72  72
                [\'E\', 7] 126 126
                [\'E\', 8] 240 240
                [\'F\', 4]  48  48
                [\'G\', 2]  12  12

            .. TODO::

                The result should be an enumerated set, and handle
                infinite root systems.
            '''
        def short_roots(self):
            """
            Return a list of the short roots of ``self``.

            EXAMPLES::

                sage: L = RootSystem(['B',3]).root_lattice()
                sage: sorted(L.short_roots())                                           # needs sage.graphs
                [-alpha[1] - alpha[2] - alpha[3],
                 alpha[1] + alpha[2] + alpha[3],
                 -alpha[2] - alpha[3],
                 alpha[2] + alpha[3],
                 -alpha[3],
                 alpha[3]]
            """
        def long_roots(self):
            """
            Return a list of the long roots of ``self``.

            EXAMPLES::

                sage: L = RootSystem(['B',3]).root_lattice()
                sage: sorted(L.long_roots())                                            # needs sage.graphs
                [-alpha[1], -alpha[1] - 2*alpha[2] - 2*alpha[3],
                 -alpha[1] - alpha[2], -alpha[1] - alpha[2] - 2*alpha[3],
                 alpha[1], alpha[1] + alpha[2],
                 alpha[1] + alpha[2] + 2*alpha[3],
                 alpha[1] + 2*alpha[2] + 2*alpha[3], -alpha[2],
                 -alpha[2] - 2*alpha[3], alpha[2], alpha[2] + 2*alpha[3]]
            """
        @cached_method
        def positive_roots(self, index_set=None):
            """
            Return the positive roots of ``self``.

            If ``index_set`` is not ``None``, returns the positive roots of
            the parabolic subsystem with simple roots in ``index_set``.

            Algorithm for finite type: generate them from the simple roots by
            applying successive reflections toward the positive chamber.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).root_lattice()
                sage: sorted(L.positive_roots())                                        # needs sage.graphs
                [alpha[1], alpha[1] + alpha[2],
                 alpha[1] + alpha[2] + alpha[3], alpha[2],
                 alpha[2] + alpha[3], alpha[3]]
                sage: sorted(L.positive_roots((1,2)))                                   # needs sage.graphs
                [alpha[1], alpha[1] + alpha[2], alpha[2]]
                sage: sorted(L.positive_roots(()))                                      # needs sage.graphs
                []

                sage: L = RootSystem(['A',3,1]).root_lattice()
                sage: PR = L.positive_roots(); PR                                       # needs sage.graphs
                Disjoint union of Family (Positive real roots of type ['A', 3, 1],
                    Positive imaginary roots of type ['A', 3, 1])
                sage: [PR.unrank(i) for i in range(10)]                                 # needs sage.graphs
                [alpha[1],
                 alpha[2],
                 alpha[3],
                 alpha[1] + alpha[2],
                 alpha[2] + alpha[3],
                 alpha[1] + alpha[2] + alpha[3],
                 alpha[0] + 2*alpha[1] + alpha[2] + alpha[3],
                 alpha[0] + alpha[1] + 2*alpha[2] + alpha[3],
                 alpha[0] + alpha[1] + alpha[2] + 2*alpha[3],
                 alpha[0] + 2*alpha[1] + 2*alpha[2] + alpha[3]]
            """
        @cached_method
        def nonparabolic_positive_roots(self, index_set=None):
            """
            Return the positive roots of ``self`` that are not in the
            parabolic subsystem indicated by ``index_set``.

            If ``index_set`` is ``None``, as in :meth:`positive_roots`
            it is assumed to be the entire Dynkin node set. Then the
            parabolic subsystem consists of all positive roots and the
            empty list is returned.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).root_lattice()
                sage: L.nonparabolic_positive_roots()                                   # needs sage.graphs
                []
                sage: sorted(L.nonparabolic_positive_roots((1,2)))                      # needs sage.graphs
                [alpha[1] + alpha[2] + alpha[3], alpha[2] + alpha[3], alpha[3]]
                sage: sorted(L.nonparabolic_positive_roots(()))                         # needs sage.graphs
                [alpha[1], alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3],
                 alpha[2], alpha[2] + alpha[3], alpha[3]]
            """
        @cached_method
        def nonparabolic_positive_root_sum(self, index_set=None):
            """
            Return the sum of positive roots not in a parabolic subsystem.

            The conventions for ``index_set`` are as in :meth:`nonparabolic_positive_roots`.

            EXAMPLES::

                sage: Q = RootSystem(['A',3]).root_lattice()
                sage: Q.nonparabolic_positive_root_sum((1,2))                           # needs sage.graphs
                alpha[1] + 2*alpha[2] + 3*alpha[3]
                sage: Q.nonparabolic_positive_root_sum()                                # needs sage.graphs
                0
                sage: Q.nonparabolic_positive_root_sum(())                              # needs sage.graphs
                3*alpha[1] + 4*alpha[2] + 3*alpha[3]
            """
        def positive_real_roots(self):
            """
            Return the positive real roots of ``self``.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).root_lattice()
                sage: sorted(L.positive_real_roots())                                   # needs sage.graphs
                [alpha[1], alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3],
                 alpha[2], alpha[2] + alpha[3], alpha[3]]

                sage: L = RootSystem(['A',3,1]).root_lattice()
                sage: PRR = L.positive_real_roots(); PRR                                # needs sage.graphs
                Positive real roots of type ['A', 3, 1]
                sage: [PRR.unrank(i) for i in range(10)]                                # needs sage.graphs
                [alpha[1],
                 alpha[2],
                 alpha[3],
                 alpha[1] + alpha[2],
                 alpha[2] + alpha[3],
                 alpha[1] + alpha[2] + alpha[3],
                 alpha[0] + 2*alpha[1] + alpha[2] + alpha[3],
                 alpha[0] + alpha[1] + 2*alpha[2] + alpha[3],
                 alpha[0] + alpha[1] + alpha[2] + 2*alpha[3],
                 alpha[0] + 2*alpha[1] + 2*alpha[2] + alpha[3]]

                sage: Q = RootSystem(['A',4,2]).root_lattice()
                sage: PR = Q.positive_roots()                                           # needs sage.graphs
                sage: [PR.unrank(i) for i in range(5)]                                  # needs sage.graphs
                [alpha[1],
                 alpha[2],
                 alpha[1] + alpha[2],
                 2*alpha[1] + alpha[2],
                 alpha[0] + alpha[1] + alpha[2]]

                sage: Q = RootSystem(['D',3,2]).root_lattice()
                sage: PR = Q.positive_roots()                                           # needs sage.graphs
                sage: [PR.unrank(i) for i in range(5)]                                  # needs sage.graphs
                [alpha[1],
                 alpha[2],
                 alpha[1] + 2*alpha[2],
                 alpha[1] + alpha[2],
                 alpha[0] + alpha[1] + 2*alpha[2]]
            """
        def positive_imaginary_roots(self):
            """
            Return the positive imaginary roots of ``self``.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).root_lattice()
                sage: L.positive_imaginary_roots()
                ()

                sage: L = RootSystem(['A',3,1]).root_lattice()
                sage: PIR = L.positive_imaginary_roots(); PIR                           # needs sage.graphs
                Positive imaginary roots of type ['A', 3, 1]
                sage: [PIR.unrank(i) for i in range(5)]                                 # needs sage.graphs
                [alpha[0] + alpha[1] + alpha[2] + alpha[3],
                 2*alpha[0] + 2*alpha[1] + 2*alpha[2] + 2*alpha[3],
                 3*alpha[0] + 3*alpha[1] + 3*alpha[2] + 3*alpha[3],
                 4*alpha[0] + 4*alpha[1] + 4*alpha[2] + 4*alpha[3],
                 5*alpha[0] + 5*alpha[1] + 5*alpha[2] + 5*alpha[3]]
            """
        @cached_method
        def positive_roots_by_height(self, increasing: bool = True):
            """
            Return a list of positive roots in increasing order by height.

            If ``increasing`` is False, returns them in decreasing order.

            .. warning::

                Raise an error if the Cartan type is not finite.

            EXAMPLES::

                sage: L = RootSystem(['C',2]).root_lattice()
                sage: L.positive_roots_by_height()                                      # needs sage.graphs
                [alpha[2], alpha[1], alpha[1] + alpha[2], 2*alpha[1] + alpha[2]]
                sage: L.positive_roots_by_height(increasing=False)                      # needs sage.graphs
                [2*alpha[1] + alpha[2], alpha[1] + alpha[2], alpha[2], alpha[1]]

                sage: L = RootSystem(['A',2,1]).root_lattice()
                sage: L.positive_roots_by_height()                                      # needs sage.graphs
                Traceback (most recent call last):
                ...
                NotImplementedError: Only implemented for finite Cartan type
            """
        @cached_method
        def positive_roots_parabolic(self, index_set=None):
            """
            Return the set of positive roots for the parabolic subsystem with Dynkin node set ``index_set``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the Dynkin node set of the
              parabolic subsystem. It should be a tuple. The default value
              implies the entire Dynkin node set

            EXAMPLES::

                sage: lattice =  RootSystem(['A',3]).root_lattice()
                sage: sorted(lattice.positive_roots_parabolic((1,3)), key=str)          # needs sage.graphs
                [alpha[1], alpha[3]]
                sage: sorted(lattice.positive_roots_parabolic((2,3)), key=str)          # needs sage.graphs
                [alpha[2], alpha[2] + alpha[3], alpha[3]]
                sage: sorted(lattice.positive_roots_parabolic(), key=str)               # needs sage.graphs
                [alpha[1], alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3],
                 alpha[2], alpha[2] + alpha[3], alpha[3]]

            .. WARNING::

                This returns an error if the Cartan type is not finite.
            """
        @cached_method
        def positive_roots_nonparabolic(self, index_set=None):
            """
            Return the set of positive roots outside the parabolic subsystem with Dynkin node set ``index_set``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the Dynkin node set of the
              parabolic subsystem. It should be a tuple. The default value
              implies the entire Dynkin node set

            EXAMPLES::

                sage: # needs sage.graphs
                sage: lattice = RootSystem(['A',3]).root_lattice()
                sage: sorted(lattice.positive_roots_nonparabolic((1,3)), key=str)
                [alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3],
                 alpha[2], alpha[2] + alpha[3]]
                sage: sorted(lattice.positive_roots_nonparabolic((2,3)), key=str)
                [alpha[1], alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3]]
                sage: lattice.positive_roots_nonparabolic()
                []
                sage: lattice.positive_roots_nonparabolic((1,2,3))
                []

            .. WARNING::

                This returns an error if the Cartan type is not finite.
            """
        @cached_method
        def positive_roots_nonparabolic_sum(self, index_set=None):
            """
            Return the sum of positive roots outside the parabolic subsystem with Dynkin node set ``index_set``.

            INPUT:

            - ``index_set`` -- (default: ``None``) the Dynkin node set of the
              parabolic subsystem. It should be a tuple. The default value
              implies the entire Dynkin node set

            EXAMPLES::

                sage: # needs sage.graphs
                sage: lattice = RootSystem(['A',3]).root_lattice()
                sage: lattice.positive_roots_nonparabolic_sum((1,3))
                2*alpha[1] + 4*alpha[2] + 2*alpha[3]
                sage: lattice.positive_roots_nonparabolic_sum((2,3))
                3*alpha[1] + 2*alpha[2] + alpha[3]
                sage: lattice.positive_roots_nonparabolic_sum(())
                3*alpha[1] + 4*alpha[2] + 3*alpha[3]
                sage: lattice.positive_roots_nonparabolic_sum()
                0
                sage: lattice.positive_roots_nonparabolic_sum((1,2,3))
                0

            .. WARNING::

                This returns an error if the Cartan type is not finite.
            """
        def root_poset(self, restricted: bool = False, facade: bool = False):
            """
            Return the (restricted) root poset associated to ``self``.

            The elements are given by the positive roots (resp. non-simple,
            positive roots), and `\\alpha \\leq \\beta` iff `\\beta - \\alpha` is a
            nonnegative linear combination of simple roots.

            INPUT:

            - ``restricted`` -- boolean (default: ``False``); if ``True``, only
              non-simple roots are considered.
            - ``facade`` -- boolean (default: ``False``); passes facade option
              to the poset generator

            EXAMPLES::

                sage: # needs sage.graphs
                sage: Phi = RootSystem(['A',1]).root_poset(); Phi
                Finite poset containing 1 elements
                sage: Phi.cover_relations()
                []
                sage: Phi = RootSystem(['A',2]).root_poset(); Phi
                Finite poset containing 3 elements
                sage: sorted(Phi.cover_relations(), key=str)
                [[alpha[1], alpha[1] + alpha[2]], [alpha[2], alpha[1] + alpha[2]]]
                sage: Phi = RootSystem(['A',3]).root_poset(restricted=True); Phi
                Finite poset containing 3 elements
                sage: sorted(Phi.cover_relations(), key=str)
                [[alpha[1] + alpha[2], alpha[1] + alpha[2] + alpha[3]],
                 [alpha[2] + alpha[3], alpha[1] + alpha[2] + alpha[3]]]
                sage: Phi = RootSystem(['B',2]).root_poset(); Phi
                Finite poset containing 4 elements
                sage: sorted(Phi.cover_relations(), key=str)
                [[alpha[1] + alpha[2], alpha[1] + 2*alpha[2]],
                 [alpha[1], alpha[1] + alpha[2]],
                 [alpha[2], alpha[1] + alpha[2]]]

            TESTS:

            Check that :issue:`17982` is fixed::

                sage: RootSystem(['A', 2]).ambient_space().root_poset()                 # needs sage.graphs
                Finite poset containing 3 elements
            """
        def nonnesting_partition_lattice(self, facade: bool = False):
            """
            Return the lattice of nonnesting partitions.

            This is the lattice of order ideals of the root poset.

            This has been defined by Postnikov, see Remark 2 in [Reiner97]_.

            .. SEEALSO::

                :meth:`generalized_nonnesting_partition_lattice`, :meth:`root_poset`

            EXAMPLES::

                sage: R = RootSystem(['A', 3])
                sage: RS = R.root_lattice()
                sage: P = RS.nonnesting_partition_lattice(); P                          # needs sage.graphs
                Finite lattice containing 14 elements
                sage: P.coxeter_transformation()**10 == 1                               # needs sage.graphs sage.libs.flint
                True

                sage: # needs sage.graphs
                sage: R = RootSystem(['B', 3])
                sage: RS = R.root_lattice()
                sage: P = RS.nonnesting_partition_lattice(); P
                Finite lattice containing 20 elements
                sage: P.coxeter_transformation()**7 == 1                                # needs sage.libs.flint
                True

            REFERENCES:

            .. [Reiner97] Victor Reiner. *Non-crossing partitions for
               classical reflection groups*. Discrete Mathematics 177 (1997)
            .. [Arm06] Drew Armstrong. *Generalized Noncrossing Partitions and
               Combinatorics of Coxeter Groups*. :arxiv:`math/0611106`
            """
        def generalized_nonnesting_partition_lattice(self, m, facade: bool = False):
            """
            Return the lattice of `m`-nonnesting partitions.

            This has been defined by Athanasiadis, see chapter 5 of [Arm06]_.

            INPUT:

            - ``m`` -- integer

            .. SEEALSO::

                :meth:`nonnesting_partition_lattice`

            EXAMPLES::

                sage: R = RootSystem(['A', 2])
                sage: RS = R.root_lattice()
                sage: P = RS.generalized_nonnesting_partition_lattice(2); P             # needs sage.graphs
                Finite lattice containing 12 elements
                sage: P.coxeter_transformation()**20 == 1                               # needs sage.graphs sage.libs.flint
                True
            """
        def almost_positive_roots(self):
            """
            Return the almost positive roots of ``self``.

            These are the positive roots together with the simple negative roots.

            .. SEEALSO:: :meth:`almost_positive_root_decomposition`, :meth:`tau_plus_minus`

            EXAMPLES::

                sage: L = RootSystem(['A',2]).root_lattice()
                sage: L.almost_positive_roots()                                         # needs sage.graphs
                [-alpha[1], alpha[1], alpha[1] + alpha[2], -alpha[2], alpha[2]]
            """
        def negative_roots(self):
            """
            Return the negative roots of ``self``.

            EXAMPLES::

                sage: L = RootSystem(['A', 2]).weight_lattice()
                sage: sorted(L.negative_roots())                                        # needs sage.graphs
                [-2*Lambda[1] + Lambda[2], -Lambda[1] - Lambda[2], Lambda[1] - 2*Lambda[2]]

            Algorithm: negate the positive roots
            """
        def coroot_lattice(self):
            """
            Return the coroot lattice.

            EXAMPLES::

                sage: RootSystem(['A',2]).root_lattice().coroot_lattice()
                Coroot lattice of the Root system of type ['A', 2]
            """
        def coroot_space(self, base_ring=...):
            """
            Return the coroot space over ``base_ring``.

            INPUT:

            - ``base_ring`` -- a ring (default: `\\QQ`)

            EXAMPLES::

                sage: RootSystem(['A',2]).root_lattice().coroot_space()
                Coroot space over the Rational Field of the Root system of type ['A', 2]

                sage: RootSystem(['A',2]).root_lattice().coroot_space(QQ['q'])
                Coroot space over the Univariate Polynomial Ring in q over Rational Field
                 of the Root system of type ['A', 2]
            """
        def simple_coroot(self, i):
            """
            Return the `i`-th simple coroot.

            EXAMPLES::

                sage: RootSystem(['A',2]).root_lattice().simple_coroot(1)
                alphacheck[1]
            """
        cache_simple_coroots: Incomplete
        @cached_method
        def simple_coroots(self):
            """
            Return the family `(\\alpha^\\vee_i)_{i\\in I}` of the simple coroots.

            EXAMPLES::

                sage: alphacheck = RootSystem(['A',3]).root_lattice().simple_coroots()
                sage: [alphacheck[i] for i in [1, 2, 3]]
                [alphacheck[1], alphacheck[2], alphacheck[3]]
            """
        @cached_method
        def alphacheck(self):
            '''
            Return the family `(\\alpha^\\vee_i)_{i \\in I}` of the simple
            coroots, with the extra feature that, for simple irreducible
            root systems, `\\alpha^\\vee_0` yields the coroot associated to
            the opposite of the highest root (caveat: for non-simply-laced
            root systems, this is not the opposite of the highest coroot!).

            EXAMPLES::

                sage: alphacheck = RootSystem(["A",2]).ambient_space().alphacheck()
                sage: alphacheck
                Finite family {1: (1, -1, 0), 2: (0, 1, -1)}

            Here is now `\\alpha^\\vee_0`:

                (-1, 0, 1)

            .. TODO:: add a non simply laced example

            Finally, here is an affine example::

                sage: RootSystem(["A",2,1]).weight_space().alphacheck()
                Finite family {0: alphacheck[0], 1: alphacheck[1], 2: alphacheck[2]}

                sage: RootSystem(["A",3]).ambient_space().alphacheck()
                Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1)}
            '''
        @cached_method
        def cohighest_root(self):
            """
            Return the associated coroot of the highest root.

            .. NOTE:: this is usually not the highest coroot.

            EXAMPLES::

                sage: RootSystem(['A', 3]).ambient_space().cohighest_root()
                (1, 0, 0, -1)
            """
        @cached_method
        def null_root(self):
            """
            Return the null root of ``self``.

            The null root is the smallest non trivial positive root which is
            orthogonal to all simple coroots. It exists for any affine root
            system.

            EXAMPLES::

                sage: RootSystem(['C',2,1]).root_lattice().null_root()                  # needs sage.graphs
                alpha[0] + 2*alpha[1] + alpha[2]
                sage: RootSystem(['D',4,1]).root_lattice().null_root()                  # needs sage.graphs
                alpha[0] + alpha[1] + 2*alpha[2] + alpha[3] + alpha[4]
                sage: RootSystem(['F',4,1]).root_lattice().null_root()                  # needs sage.graphs
                alpha[0] + 2*alpha[1] + 3*alpha[2] + 4*alpha[3] + 2*alpha[4]
            """
        @cached_method
        def null_coroot(self):
            """
            Return the null coroot of ``self``.

            The null coroot is the smallest non trivial positive coroot which is
            orthogonal to all simple roots. It exists for any affine root
            system.

            EXAMPLES::

                sage: RootSystem(['C',2,1]).root_lattice().null_coroot()                # needs sage.graphs
                alphacheck[0] + alphacheck[1] + alphacheck[2]
                sage: RootSystem(['D',4,1]).root_lattice().null_coroot()                # needs sage.graphs
                alphacheck[0] + alphacheck[1] + 2*alphacheck[2]
                 + alphacheck[3] + alphacheck[4]
                sage: RootSystem(['F',4,1]).root_lattice().null_coroot()                # needs sage.graphs
                alphacheck[0] + 2*alphacheck[1] + 3*alphacheck[2]
                 + 2*alphacheck[3] + alphacheck[4]
            """
        def fundamental_weights_from_simple_roots(self):
            '''
            Return the fundamental weights.

            This is computed from the simple roots by using the
            inverse of the Cartan matrix. This method is therefore
            only valid for finite types and if this realization of the
            root lattice is large enough to contain them.

            EXAMPLES:

            In the root space, we retrieve the inverse of the Cartan matrix::

                sage: L = RootSystem(["B",3]).root_space()
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Finite family {1:     alpha[1] +   alpha[2] +     alpha[3],
                               2:     alpha[1] + 2*alpha[2] +   2*alpha[3],
                               3: 1/2*alpha[1] +   alpha[2] + 3/2*alpha[3]}
                sage: ~L.cartan_type().cartan_matrix()                                  # needs sage.graphs
                [  1   1 1/2]
                [  1   2   1]
                [  1   2 3/2]

            In the weight lattice and the ambient space, we retrieve
            the fundamental weights::

                sage: L = RootSystem(["B",3]).weight_lattice()
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Finite family {1: Lambda[1], 2: Lambda[2], 3: Lambda[3]}

                sage: L = RootSystem(["B",3]).ambient_space()
                sage: L.fundamental_weights()
                Finite family {1: (1, 0, 0), 2: (1, 1, 0), 3: (1/2, 1/2, 1/2)}
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Finite family {1: (1, 0, 0), 2: (1, 1, 0), 3: (1/2, 1/2, 1/2)}

            However the fundamental weights do not belong to the root
            lattice::

                sage: L = RootSystem(["B",3]).root_lattice()
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Traceback (most recent call last):
                ...
                ValueError: The fundamental weights do not live in this realization
                of the root lattice

            Beware of the usual `GL_n` vs `SL_n` catch in type `A`::

                sage: L = RootSystem(["A",3]).ambient_space()
                sage: L.fundamental_weights()
                Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1, 1, 1, 0)}
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Finite family {1: (3/4, -1/4, -1/4, -1/4),
                               2: (1/2, 1/2, -1/2, -1/2),
                               3: (1/4, 1/4, 1/4, -3/4)}

                sage: L = RootSystem(["A",3]).ambient_lattice()
                sage: L.fundamental_weights_from_simple_roots()                         # needs sage.graphs
                Traceback (most recent call last):
                ...
                ValueError: The fundamental weights do not live in this realization
                of the root lattice
            '''
        def reflection(self, root, coroot=None):
            """
            Return the reflection along the ``root``, and across the hyperplane
            defined by ``coroot``, as a function from ``self`` to ``self``.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',2]).weight_lattice()
                sage: x = space.simple_roots()[1]
                sage: y = space.simple_coroots()[1]
                sage: s = space.reflection(x,y)
                sage: x
                2*Lambda[1] - Lambda[2]
                sage: s(x)
                -2*Lambda[1] + Lambda[2]
                sage: s(-x)
                2*Lambda[1] - Lambda[2]
            """
        @cached_method
        def simple_reflection(self, i):
            """
            Return the `i`-th simple reflection, as a function from
            ``self`` to ``self``.

            INPUT:

            - ``i`` -- an element of the index set of ``self``

            EXAMPLES::

                sage: space = RootSystem(['A',2]).ambient_lattice()
                sage: s = space.simple_reflection(1)
                sage: x = space.simple_roots()[1]; x
                (1, -1, 0)
                sage: s(x)
                (-1, 1, 0)
            """
        @cached_method
        def simple_reflections(self):
            '''
            Return the family `(s_i)_{i\\in I}` of the simple reflections
            of this root system.

            EXAMPLES::

                sage: r = RootSystem(["A", 2]).root_lattice()
                sage: s = r.simple_reflections()
                sage: s[1]( r.simple_root(1) )                                          # needs sage.graphs
                -alpha[1]

            TESTS::

                sage: s
                simple reflections
            '''
        s = simple_reflections
        def projection(self, root, coroot=None, to_negative: bool = True):
            """
            Return the projection along the ``root``, and across the
            hyperplane defined by ``coroot``, as a function `\\pi` from ``self`` to
            ``self``.

            `\\pi` is a half-linear map which stabilizes the negative
            half space and acts by reflection on the positive half space.

            If ``to_negative`` is ``False``, then project onto the positive
            half space instead.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',2]).weight_lattice()
                sage: x = space.simple_roots()[1]
                sage: y = space.simple_coroots()[1]
                sage: pi = space.projection(x,y)
                sage: x
                2*Lambda[1] - Lambda[2]
                sage: pi(x)
                -2*Lambda[1] + Lambda[2]
                sage: pi(-x)
                -2*Lambda[1] + Lambda[2]
                sage: pi = space.projection(x,y,False)
                sage: pi(-x)
                2*Lambda[1] - Lambda[2]
            """
        @cached_method
        def simple_projection(self, i, to_negative: bool = True):
            """
            Return the projection along the `i`-th simple root, and across the
            hyperplane define by the `i`-th simple coroot, as a function from
            ``self`` to ``self``.

            INPUT:

            - ``i`` -- an element of the index set of ``self``

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',2]).weight_lattice()
                sage: x = space.simple_roots()[1]
                sage: pi = space.simple_projection(1)
                sage: x
                2*Lambda[1] - Lambda[2]
                sage: pi(x)
                -2*Lambda[1] + Lambda[2]
                sage: pi(-x)
                -2*Lambda[1] + Lambda[2]
                sage: pi = space.simple_projection(1,False)
                sage: pi(-x)
                2*Lambda[1] - Lambda[2]
            """
        @cached_method
        def simple_projections(self, to_negative: bool = True):
            """
            Return the family `(s_i)_{i\\in I}` of the simple projections
            of this root system.

            EXAMPLES::

                sage: space = RootSystem(['A',2]).weight_lattice()
                sage: pi = space.simple_projections()                                   # needs sage.graphs
                sage: x = space.simple_roots()                                          # needs sage.graphs
                sage: pi[1](x[2])                                                       # needs sage.graphs
                -Lambda[1] + 2*Lambda[2]

            TESTS::

                sage: pi                                                                # needs sage.graphs
                pi
            """
        def weyl_group(self, prefix=None):
            """
            Return the Weyl group associated to ``self``.

            EXAMPLES::

                sage: RootSystem(['F',4]).ambient_space().weyl_group()                  # needs sage.libs.gap
                Weyl Group of type ['F', 4] (as a matrix group acting on the ambient space)
                sage: RootSystem(['F',4]).root_space().weyl_group()                     # needs sage.libs.gap
                Weyl Group of type ['F', 4] (as a matrix group acting on the root space)
            """
        def tau_epsilon_operator_on_almost_positive_roots(self, J):
            """
            The `\\tau_\\epsilon` operator on almost positive roots.

            Given a subset `J` of non adjacent vertices of the Dynkin
            diagram, this constructs the operator on the almost positive
            roots which fixes the negative simple roots `\\alpha_i` for `i`
            not in `J`, and acts otherwise by:

            .. MATH::

                \\tau_+( \\beta ) = (\\prod_{i \\in J} s_i) (\\beta)

            See Equation (1.2) of [CFZ2002]_.

            EXAMPLES::

                sage: L = RootSystem(['A',4]).root_lattice()
                sage: tau = L.tau_epsilon_operator_on_almost_positive_roots([1,3])      # needs sage.libs.gap
                sage: alpha = L.simple_roots()                                          # needs sage.graphs

            The action on a negative simple root not in `J`::

                sage: tau(-alpha[2])                                                    # needs sage.graphs sage.libs.gap
                -alpha[2]

            The action on a negative simple root in `J`::

                sage: tau(-alpha[1])                                                    # needs sage.graphs sage.libs.gap
                alpha[1]

            The action on all almost positive roots::

                sage: for root in L.almost_positive_roots():                            # needs sage.graphs sage.libs.gap
                ....:     print('tau({:<41}) = {}'.format(str(root), tau(root)))
                tau(-alpha[1]                                ) = alpha[1]
                tau(alpha[1]                                 ) = -alpha[1]
                tau(alpha[1] + alpha[2]                      ) = alpha[2] + alpha[3]
                tau(alpha[1] + alpha[2] + alpha[3]           ) = alpha[2]
                tau(alpha[1] + alpha[2] + alpha[3] + alpha[4]) = alpha[2] + alpha[3] + alpha[4]
                tau(-alpha[2]                                ) = -alpha[2]
                tau(alpha[2]                                 ) = alpha[1] + alpha[2] + alpha[3]
                tau(alpha[2] + alpha[3]                      ) = alpha[1] + alpha[2]
                tau(alpha[2] + alpha[3] + alpha[4]           ) = alpha[1] + alpha[2] + alpha[3] + alpha[4]
                tau(-alpha[3]                                ) = alpha[3]
                tau(alpha[3]                                 ) = -alpha[3]
                tau(alpha[3] + alpha[4]                      ) = alpha[4]
                tau(-alpha[4]                                ) = -alpha[4]
                tau(alpha[4]                                 ) = alpha[3] + alpha[4]

            This method works on any root lattice realization::

                sage: L = RootSystem(['B',3]).ambient_space()
                sage: tau = L.tau_epsilon_operator_on_almost_positive_roots([1,3])      # needs sage.libs.gap
                sage: for root in L.almost_positive_roots():                            # needs sage.graphs sage.libs.gap
                ....:     print('tau({:<41}) = {}'.format(str(root), tau(root)))
                tau((-1, 1, 0)                               ) = (1, -1, 0)
                tau((1, 0, 0)                                ) = (0, 1, 0)
                tau((1, -1, 0)                               ) = (-1, 1, 0)
                tau((1, 1, 0)                                ) = (1, 1, 0)
                tau((1, 0, -1)                               ) = (0, 1, 1)
                tau((1, 0, 1)                                ) = (0, 1, -1)
                tau((0, -1, 1)                               ) = (0, -1, 1)
                tau((0, 1, 0)                                ) = (1, 0, 0)
                tau((0, 1, -1)                               ) = (1, 0, 1)
                tau((0, 1, 1)                                ) = (1, 0, -1)
                tau((0, 0, -1)                               ) = (0, 0, 1)
                tau((0, 0, 1)                                ) = (0, 0, -1)

            .. SEEALSO:: :meth:`tau_plus_minus`
            """
        def tau_plus_minus(self):
            '''
            Return the `\\tau^+` and `\\tau^-` piecewise linear operators on ``self``.

            Those operators are induced by the bipartition `\\{L,R\\}` of
            the simple roots of ``self``, and stabilize the almost
            positive roots. Namely, `\\tau_+` fixes the negative simple
            roots `\\alpha_i` for `i` in `R`, and acts otherwise by:

            .. MATH::

                \\tau_+( \\beta ) = (\\prod_{i \\in L} s_i) (\\beta)

            `\\tau_-` acts analogously, with `L` and `R` interchanged.

            Those operators are used to construct the associahedron, a
            polytopal realization of the cluster complex (see
            :class:`Associahedron`).

            .. SEEALSO:: :meth:`tau_epsilon_operator_on_almost_positive_roots`

            EXAMPLES:

            We explore the example of [CFZ2002]_ Eq.(1.3)::

                sage: S = RootSystem([\'A\',2]).root_lattice()
                sage: taup, taum = S.tau_plus_minus()                                   # needs sage.graphs sage.libs.gap
                sage: for beta in S.almost_positive_roots():                            # needs sage.graphs sage.libs.gap
                ....:     print("{} , {} , {}".format(beta, taup(beta), taum(beta)))
                -alpha[1] , alpha[1] , -alpha[1]
                alpha[1] , -alpha[1] , alpha[1] + alpha[2]
                alpha[1] + alpha[2] , alpha[2] , alpha[1]
                -alpha[2] , -alpha[2] , alpha[2]
                alpha[2] , alpha[1] + alpha[2] , -alpha[2]
            '''
        def almost_positive_roots_decomposition(self):
            """
            Return the decomposition of the almost positive roots of ``self``.

            This is the list of the orbits of the almost positive roots
            under the action of the dihedral group generated by the
            operators `\\tau_+` and `\\tau_-`.

            .. SEEALSO::

                - :meth:`almost_positive_roots`
                - :meth:`tau_plus_minus`

            EXAMPLES::

                sage: RootSystem(['A',2]).root_lattice().almost_positive_roots_decomposition()      # needs sage.graphs sage.libs.gap
                [[-alpha[1], alpha[1], alpha[1] + alpha[2], alpha[2], -alpha[2]]]

                sage: RootSystem(['B',2]).root_lattice().almost_positive_roots_decomposition()      # needs sage.graphs sage.libs.gap
                [[-alpha[1], alpha[1], alpha[1] + 2*alpha[2]],
                 [-alpha[2], alpha[2], alpha[1] + alpha[2]]]

                sage: RootSystem(['D',4]).root_lattice().almost_positive_roots_decomposition()      # needs sage.graphs sage.libs.gap
                [[-alpha[1], alpha[1], alpha[1] + alpha[2], alpha[2] + alpha[3] + alpha[4]],
                 [-alpha[2], alpha[2], alpha[1] + alpha[2] + alpha[3] + alpha[4],
                     alpha[1] + 2*alpha[2] + alpha[3] + alpha[4]],
                 [-alpha[3], alpha[3], alpha[2] + alpha[3], alpha[1] + alpha[2] + alpha[4]],
                 [-alpha[4], alpha[4], alpha[2] + alpha[4], alpha[1] + alpha[2] + alpha[3]]]
            """
        @cached_method
        def classical(self):
            '''
            Return the corresponding root/weight/ambient lattice/space.

            EXAMPLES::

                sage: RootSystem(["A",4,1]).root_lattice().classical()
                Root lattice of the Root system of type [\'A\', 4]
                sage: RootSystem(["A",4,1]).weight_lattice().classical()
                Weight lattice of the Root system of type [\'A\', 4]
                sage: RootSystem(["A",4,1]).ambient_space().classical()
                Ambient space of the Root system of type [\'A\', 4]
            '''
        def plot(self, roots: str = 'simple', coroots: bool = False, reflection_hyperplanes: str = 'simple', fundamental_weights=None, fundamental_chamber=None, alcoves=None, alcove_labels: bool = False, alcove_walk=None, **options):
            '''
            Return a picture of this root lattice realization.

            INPUT:

            - ``roots`` -- which roots to display, if any
              Can be one of the following:

              * ``\'simple\'`` -- the simple roots (the default)
              * ``\'classical\'`` -- not yet implemented
              * ``\'all\'`` -- only works in the finite case
              * A list or tuple of roots
              * ``False``

            - ``coroots`` -- which coroots to display, if any
              Can be one of the following:

              * ``\'simple\'`` -- the simple coroots (the default)
              * ``\'classical\'`` -- not yet implemented
              * ``\'all\'`` -- only works in the finite case
              * A list or tuple of coroots
              * ``False``

            - ``fundamental_weights`` -- boolean or ``None`` (default: ``None``)
              whether to display the fundamental weights.
              If ``None``, the fundamental weights are drawn if available.

            - ``reflection_hyperplanes`` -- which reflection
              hyperplanes to display, if any. Can be one of the
              following:

              * ``\'simple\'`` -- the simple roots
              * ``\'classical\'`` -- not yet implemented
              * ``\'all\'`` -- only works in the finite case
              * A list or tuple of roots
              * ``False`` (the default)

            - ``fundamental_chamber`` -- whether and how to draw the
              fundamental chamber. Can be one of the following:

              * A boolean -- Set to ``True`` to draw the fundamental
                chamber
              * ``\'classical\'`` -- draw the classical fundamental chamber
              * ``None`` -- (the default) The fundamental chamber is
                drawn except in the root lattice where this is not yet
                implemented. For affine types the classical
                fundamental chamber is drawn instead.

            - ``alcoves`` -- one of the following (default: ``True``):

              * A boolean -- whether to display the alcoves
              * A list of alcoves -- The alcoves to be drawn. Each alcove is
                specified by the coordinates of its center in the root lattice
                (affine type only). Otherwise the alcoves that intersect the
                bounding box are drawn.

            - ``alcove_labels`` -- one of the following (default: ``False``):

              * A boolean -- whether to display the elements of the Weyl group
                indexing the alcoves. This currently requires to also
                set the ``alcoves`` option.
              * A number `l` -- the label is drawn at level `l` (affine type
                only), which only makes sense if ``affine`` is ``False``.

            - ``bounding_box`` -- a rational number or a list of pairs
              thereof (default: 3)

              Specifies a bounding box, in the coordinate system for
              this plot, in which to plot alcoves and other infinite
              objects. If the bounding box is a number `a`, then the
              bounding box is of the form `[-a,a]` in all directions.
              Beware that there can be some border effects and the
              returned graphic is not necessarily strictly contained
              in the bounding box.

            - ``alcove_walk`` -- an alcove walk or ``None`` (default: ``None``)

              The alcove walk is described by a list (or iterable) of
              vertices of the Dynkin diagram which specifies which
              wall is crossed at each step, starting from the
              fundamental alcove.

            - ``projection`` -- one of the following (default: ``True``):

              * ``True`` -- the default projection for the root
                lattice realization is used.
              * ``False`` -- no projection is used.
              * ``barycentric`` -- a barycentric projection is used.
              * A function -- If a function is specified, it should implement a
                linear (or affine) map taking as input an element of
                this root lattice realization and returning its
                desired coordinates in the plot, as a vector with
                rational coordinates.

            - ``color`` -- a function mapping vertices of the Dynkin
              diagram to colors (default: ``\'black\'`` for 0,
              ``\'blue\'`` for 1, ``\'red\'`` for 2, ``\'green\'`` for 3)

              This is used to set the color for the simple roots,
              fundamental weights, reflection hyperplanes, alcove
              facets, etc. If the color is ``None``, the object is not
              drawn.

            - ``labels`` -- boolean (default: ``True``)
              whether to display labels on the simple roots,
              fundamental weights, etc.

            EXAMPLES::

                sage: L = RootSystem(["A",2,1]).ambient_space().plot()  # long time, needs sage.plot sage.symbolic

            .. SEEALSO::

                - :meth:`plot_parse_options`
                - :meth:`plot_roots`, :meth:`plot_coroots`
                - :meth:`plot_fundamental_weights`
                - :meth:`plot_fundamental_chamber`
                - :meth:`plot_reflection_hyperplanes`
                - :meth:`plot_alcoves`
                - :meth:`plot_alcove_walk`
                - :meth:`plot_ls_paths`
                - :meth:`plot_mv_polytope`
                - :meth:`plot_crystal`
            '''
        def plot_parse_options(self, **args):
            '''
            Return an option object to be used for root system plotting.

            EXAMPLES::

                sage: L = RootSystem(["A",2,1]).ambient_space()
                sage: options = L.plot_parse_options(); options                         # needs sage.symbolic
                <sage.combinat.root_system.plot.PlotOptions object at ...>

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting
            '''
        def plot_roots(self, collection: str = 'simple', **options):
            '''
            Plot the (simple/classical) roots of this root lattice.

            INPUT:

            - ``collection`` -- which roots to display
              can be one of the following:

              * ``\'simple\'`` (the default)
              * ``\'classical\'``
              * ``\'all\'``

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: RootSystem(["B",3]).ambient_space().plot_roots()                  # needs sage.plot
                Graphics3d Object
                sage: RootSystem(["B",3]).ambient_space().plot_roots("all")             # needs sage.plot
                Graphics3d Object

            TESTS::

                sage: list(RootSystem(["A",2]).root_lattice().plot_roots())             # needs sage.plot sage.symbolic
                [Arrow from (0.0,0.0) to (1.0,0.0),
                 Text \'$\\alpha_{1}$\' at the point (1.05,0.0),
                 Arrow from (0.0,0.0) to (0.0,1.0),
                 Text \'$\\alpha_{2}$\' at the point (0.0,1.05)]

                sage: list(RootSystem(["A",2]).weight_lattice().plot_roots(labels=False))           # needs sage.plot sage.symbolic
                [Arrow from (0.0,0.0) to (2.0,-1.0),
                 Arrow from (0.0,0.0) to (-1.0,2.0)]

                 sage: list(RootSystem(["A",2]).ambient_lattice().plot_roots())         # needs sage.plot sage.symbolic
                 [Arrow from (0.0,0.0) to (1.5,0.86...),
                  Text \'$\\alpha_{1}$\' at the point (1.575...,0.90...),
                  Arrow from (0.0,0.0) to (-1.5,0.86...),
                  Text \'$\\alpha_{2}$\' at the point (-1.575...,0.90...)]

                 sage: list(RootSystem(["B",2]).ambient_space().plot_roots())           # needs sage.plot sage.symbolic
                 [Arrow from (0.0,0.0) to (1.0,-1.0),
                  Text \'$\\alpha_{1}$\' at the point (1.05,-1.05),
                  Arrow from (0.0,0.0) to (0.0,1.0),
                  Text \'$\\alpha_{2}$\' at the point (0.0,1.05)]

                sage: list(RootSystem(["A",2]).root_lattice().plot_roots("all"))        # needs sage.plot sage.symbolic
                [Arrow from (0.0,0.0) to (1.0,0.0),
                 Text \'$\\alpha_{1}$\' at the point (1.05,0.0),
                 Arrow from (0.0,0.0) to (0.0,1.0),
                 Text \'$\\alpha_{2}$\' at the point (0.0,1.05),
                 Arrow from (0.0,0.0) to (1.0,1.0),
                 Text \'$\\alpha_{1} + \\alpha_{2}$\' at the point (1.05,1.05),
                 Arrow from (0.0,0.0) to (-1.0,0.0),
                 Text \'$-\\alpha_{1}$\' at the point (-1.05,0.0),
                 Arrow from (0.0,0.0) to (0.0,-1.0),
                 Text \'$-\\alpha_{2}$\' at the point (0.0,-1.05),
                 Arrow from (0.0,0.0) to (-1.0,-1.0),
                 Text \'$-\\alpha_{1} - \\alpha_{2}$\' at the point (-1.05,-1.05)]
            '''
        def plot_coroots(self, collection: str = 'simple', **options):
            '''
            Plot the (simple/classical) coroots of this root lattice.

            INPUT:

            - ``collection`` -- which coroots to display
              Can be one of the following:

              * ``\'simple\'`` (the default)
              * ``\'classical\'``
              * ``\'all\'``

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: RootSystem(["B",3]).ambient_space().plot_coroots()                # needs sage.plot sage.symbolic
                Graphics3d Object

            TESTS::

                 sage: list(RootSystem(["B",2]).ambient_space().plot_coroots())         # needs sage.plot sage.symbolic
                 [Arrow from (0.0,0.0) to (1.0,-1.0),
                  Text \'$\\alpha^\\vee_{1}$\' at the point (1.05,-1.05),
                  Arrow from (0.0,0.0) to (0.0,2.0),
                  Text \'$\\alpha^\\vee_{2}$\' at the point (0.0,2.1)]
            '''
        def plot_fundamental_weights(self, **options):
            '''
            Plot the fundamental weights of this root lattice.

            INPUT:

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: RootSystem(["B",3]).ambient_space().plot_fundamental_weights()    # needs sage.plot
                Graphics3d Object

            TESTS::

                sage: sorted(RootSystem(["A",2]).weight_lattice().plot_fundamental_weights(), key=str)                  # needs sage.plot sage.symbolic
                [Arrow from (0.0,0.0) to (0.0,1.0),
                 Arrow from (0.0,0.0) to (1.0,0.0),
                 Text \'$\\Lambda_{1}$\' at the point (1.05,0.0),
                 Text \'$\\Lambda_{2}$\' at the point (0.0,1.05)]

                 sage: sorted(RootSystem(["A",2]).ambient_lattice().plot_fundamental_weights(), key=str)                # needs sage.plot sage.symbolic
                 [Arrow from (0.0,0.0) to (-0.5,0.86602451838...),
                  Arrow from (0.0,0.0) to (0.5,0.86602451838...),
                  Text \'$\\Lambda_{1}$\' at the point (0.525,0.909325744308...),
                  Text \'$\\Lambda_{2}$\' at the point (-0.525,0.909325744308...)]
            '''
        def plot_reflection_hyperplanes(self, collection: str = 'simple', **options):
            '''
            Plot the simple reflection hyperplanes.

            INPUT:

            - ``collection`` -- which reflection hyperplanes to display
              Can be one of the following:

              * ``\'simple\'`` (the default)
              * ``\'classical\'``
              * ``\'all\'``

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: # needs sage.plot sage.symbolic
                sage: RootSystem(["A",2,1]).ambient_space().plot_reflection_hyperplanes()
                Graphics object consisting of 6 graphics primitives
                sage: RootSystem(["G",2,1]).ambient_space().plot_reflection_hyperplanes()
                Graphics object consisting of 6 graphics primitives
                sage: RootSystem(["A",3]).weight_space().plot_reflection_hyperplanes()
                Graphics3d Object
                sage: RootSystem(["B",3]).ambient_space().plot_reflection_hyperplanes()
                Graphics3d Object
                sage: RootSystem(["A",3,1]).weight_space().plot_reflection_hyperplanes()
                Graphics3d Object
                sage: RootSystem(["B",3,1]).ambient_space().plot_reflection_hyperplanes()
                Graphics3d Object
                sage: RootSystem(["A",2,1]).weight_space().plot_reflection_hyperplanes(affine=False, level=1)
                Graphics3d Object
                sage: RootSystem(["A",2]).root_lattice().plot_reflection_hyperplanes()
                Graphics object consisting of 4 graphics primitives

            TESTS::

                sage: L = RootSystem(["A",2]).ambient_space()
                sage: print(L.plot_reflection_hyperplanes().description())                          # needs sage.plot sage.symbolic
                Text \'$H_{\\alpha^\\vee_{1}}$\' at the point (-1.81...,3.15...)
                Text \'$H_{\\alpha^\\vee_{2}}$\' at the point (1.81...,3.15...)
                Line defined by 2 points: [(-1.73..., 3.0), (1.73..., -3.0)]
                Line defined by 2 points: [(1.73..., 3.0), (-1.73..., -3.0)]

                sage: print(L.plot_reflection_hyperplanes("all").description())                     # needs sage.plot sage.symbolic
                Text \'$H_{\\alpha^\\vee_{1} + \\alpha^\\vee_{2}}$\' at the point (3.15...,0.0)
                Text \'$H_{\\alpha^\\vee_{1}}$\' at the point (-1.81...,3.15...)
                Text \'$H_{\\alpha^\\vee_{2}}$\' at the point (1.81...,3.15...)
                Line defined by 2 points: [(-1.73..., 3.0), (1.73..., -3.0)]
                Line defined by 2 points: [(1.73..., 3.0), (-1.73..., -3.0)]
                Line defined by 2 points: [(3.0, 0.0), (-3.0, 0.0)]

                sage: L = RootSystem(["A",2,1]).ambient_space()
                sage: print(L.plot_reflection_hyperplanes().description())                          # needs sage.plot sage.symbolic
                Text \'$H_{\\alpha^\\vee_{0}}$\' at the point (3.15...,0.90...)
                Text \'$H_{\\alpha^\\vee_{1}}$\' at the point (-1.81...,3.15...)
                Text \'$H_{\\alpha^\\vee_{2}}$\' at the point (1.81...,3.15...)
                Line defined by 2 points: [(-1.73..., 3.0), (1.73..., -3.0)]
                Line defined by 2 points: [(1.73..., 3.0), (-1.73..., -3.0)]
                Line defined by 2 points: [(3.0, 0.86...), (-3.0, 0.86...)]

            .. TODO:: Provide an option for transparency?
            '''
        def plot_hedron(self, **options):
            '''
            Plot the polyhedron whose vertices are given by the orbit
            of `\\rho`.

            In type `A`, this is the usual permutohedron.

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: # needs sage.plot sage.symbolic
                sage: RootSystem(["A",2]).ambient_space().plot_hedron()
                Graphics object consisting of 8 graphics primitives
                sage: RootSystem(["A",3]).ambient_space().plot_hedron()
                Graphics3d Object
                sage: RootSystem(["B",3]).ambient_space().plot_hedron()
                Graphics3d Object
                sage: RootSystem(["C",3]).ambient_space().plot_hedron()
                Graphics3d Object
                sage: RootSystem(["D",3]).ambient_space().plot_hedron()
                Graphics3d Object

            Surprise: polyhedra of large dimension know how to
            project themselves nicely::

                sage: RootSystem(["F",4]).ambient_space().plot_hedron()         # long time, needs sage.plot sage.symbolic
                Graphics3d Object

            TESTS::

                sage: L = RootSystem(["B",2]).ambient_space()
                sage: print(L.plot_hedron().description())                              # needs sage.plot sage.symbolic
                Polygon defined by 8 points: [(1.5, 0.5), (0.5, 1.5), (-0.5, 1.5), (-1.5, 0.5), (-1.5, -0.5), (-0.5, -1.5), (0.5, -1.5), (1.5, -0.5)]
                Line defined by 2 points: [(-0.5, -1.5), (0.5, -1.5)]
                Line defined by 2 points: [(-0.5, 1.5), (0.5, 1.5)]
                Line defined by 2 points: [(-1.5, -0.5), (-0.5, -1.5)]
                Line defined by 2 points: [(-1.5, -0.5), (-1.5, 0.5)]
                Line defined by 2 points: [(-1.5, 0.5), (-0.5, 1.5)]
                Line defined by 2 points: [(0.5, -1.5), (1.5, -0.5)]
                Line defined by 2 points: [(0.5, 1.5), (1.5, 0.5)]
                Line defined by 2 points: [(1.5, -0.5), (1.5, 0.5)]
                Point set defined by 8 point(s): [(-1.5, -0.5), (-1.5, 0.5), (-0.5, -1.5), (-0.5, 1.5), (0.5, -1.5), (0.5, 1.5), (1.5, -0.5), (1.5, 0.5)]
            '''
        def plot_fundamental_chamber(self, style: str = 'normal', **options):
            '''
            Plot the (classical) fundamental chamber.

            INPUT:

            - ``style`` -- ``\'normal\'`` or ``\'classical\'`` (default: ``\'normal\'``)

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES:

            2D plots::

                sage: RootSystem(["B",2]).ambient_space().plot_fundamental_chamber()    # needs sage.plot
                Graphics object consisting of 1 graphics primitive
                sage: RootSystem(["B",2,1]).ambient_space().plot_fundamental_chamber()  # needs sage.plot
                Graphics object consisting of 1 graphics primitive
                sage: RootSystem(["B",2,1]).ambient_space().plot_fundamental_chamber("classical")   # needs sage.plot
                Graphics object consisting of 1 graphics primitive

            3D plots::

                sage: RootSystem(["A",3,1]).weight_space() .plot_fundamental_chamber()  # needs sage.plot
                Graphics3d Object
                sage: RootSystem(["B",3,1]).ambient_space().plot_fundamental_chamber()  # needs sage.plot
                Graphics3d Object

            This feature is currently not available in the root lattice/space::

                sage: list(RootSystem(["A",2]).root_lattice().plot_fundamental_chamber())           # needs sage.plot
                Traceback (most recent call last):
                ...
                TypeError: classical fundamental chamber not yet available in the root lattice

            TESTS::

                sage: L = RootSystem(["B",2,1]).ambient_space()
                sage: print(L.plot_fundamental_chamber().description())                             # needs sage.plot
                Polygon defined by 3 points:     [(0.5, 0.5), (1.0, 0.0), (0.0, 0.0)]

                sage: print(L.plot_fundamental_chamber(style=\'classical\').description())            # needs sage.plot
                Polygon defined by 3 points:     [(0.0, 0.0), (3.0, 3.0), (3.0, 0.0)]
            '''
        def plot_alcoves(self, alcoves: bool = True, alcove_labels: bool = False, wireframe: bool = False, **options):
            '''
            Plot the alcoves and optionally their labels.

            INPUT:

            - ``alcoves`` -- list of alcoves or ``True`` (default: ``True``)

            - ``alcove_labels`` -- boolean or a number specifying at
              which level to put the label (default: ``False``)

            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a
                  tutorial on root system plotting, and in particular
                  how the alcoves can be specified.

            EXAMPLES:

            2D plots::

                sage: RootSystem(["B",2,1]).ambient_space().plot_alcoves()      # long time (3s), needs sage.plot sage.symbolic
                Graphics object consisting of 228 graphics primitives

            3D plots::

                sage: RootSystem(["A",2,1]).weight_space() .plot_alcoves(affine=False)  # long time (3s), needs sage.plot sage.symbolic
                Graphics3d Object
                sage: RootSystem(["G",2,1]).ambient_space().plot_alcoves(affine=False, level=1)  # long time (3s), needs sage.plot sage.symbolic
                Graphics3d Object

            Here we plot a single alcove::

                sage: L = RootSystem(["A",3,1]).ambient_space()
                sage: W = L.weyl_group()                                                # needs sage.libs.gap
                sage: L.plot(alcoves=[W.one()], reflection_hyperplanes=False, bounding_box=2)       # needs sage.libs.gap sage.plot sage.symbolic
                Graphics3d Object

            TESTS::

                sage: L = RootSystem(["A",2,1]).weight_space()
                sage: p = L.plot_alcoves(alcoves=[[0,0]])                               # needs sage.plot sage.symbolic
                sage: print(p.description())                                            # needs sage.plot sage.symbolic
                Line defined by 2 points: [(-1.0, 0.0), (0.0, -1.0)]
                Line defined by 2 points: [(-1.0, 1.0), (-1.0, 0.0)]
                Line defined by 2 points: [(-1.0, 1.0), (0.0, 0.0)]
                Line defined by 2 points: [(0.0, 0.0), (-1.0, 0.0)]
                Line defined by 2 points: [(0.0, 0.0), (0.0, -1.0)]
                Line defined by 2 points: [(0.0, 0.0), (1.0, -1.0)]
                Line defined by 2 points: [(0.0, 1.0), (-1.0, 1.0)]
                Line defined by 2 points: [(0.0, 1.0), (0.0, 0.0)]
                Line defined by 2 points: [(0.0, 1.0), (1.0, 0.0)]
                Line defined by 2 points: [(1.0, -1.0), (0.0, -1.0)]
                Line defined by 2 points: [(1.0, 0.0), (0.0, 0.0)]
                Line defined by 2 points: [(1.0, 0.0), (1.0, -1.0)]
                sage: sorted((line.options()[\'rgbcolor\'], line.options()[\'thickness\']) for line in p)                   # needs sage.plot sage.symbolic
                [(\'black\', 2), (\'black\', 2), (\'black\', 2),
                 (\'black\', 2), (\'black\', 2), (\'black\', 2),
                 (\'blue\', 1), (\'blue\', 1), (\'blue\', 1),
                 (\'red\', 1), (\'red\', 1), (\'red\', 1)]
            '''
        def plot_bounding_box(self, **options):
            '''
            Plot the bounding box.

            INPUT:

            - ``**options`` -- plotting options

            This is mostly for testing purposes.

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: L = RootSystem(["A",2,1]).ambient_space()
                sage: L.plot_bounding_box()                                             # needs sage.plot sage.symbolic
                Graphics object consisting of 1 graphics primitive

            TESTS::

                sage: list(L.plot_bounding_box())                                       # needs sage.plot sage.symbolic
                [Polygon defined by 4 points]
            '''
        def plot_alcove_walk(self, word, start=None, foldings=None, color: str = 'orange', **options):
            '''
            Plot an alcove walk.

            INPUT:

            - ``word`` -- list of elements of the index set
            - ``foldings`` -- list of booleans or ``None`` (default: ``None``)
            - ``start`` -- an element of this space (default: ``None`` for `\\rho`)
            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES:

            An alcove walk of type `A_2^{(1)}`::

                sage: L = RootSystem(["A",2,1]).ambient_space()
                sage: w1 = [0,2,1,2,0,2,1,0,2,1,2,1,2,0,2,0,1,2,0]
                sage: p = L.plot_alcoves(bounding_box=5)        # long time (5s)        # needs sage.plot sage.symbolic
                sage: p += L.plot_alcove_walk(w1)       # long time                     # needs sage.plot sage.symbolic
                sage: p                         # long time                             # needs sage.plot sage.symbolic
                Graphics object consisting of 375 graphics primitives

            The same plot with another alcove walk::

                sage: w2 = [2,1,2,0,2,0,2,1,2,0,1,2,1,2,1,0,1,2,0,2,0,1,2,0,2]
                sage: p += L.plot_alcove_walk(w2, color=\'orange\')       # long time, needs sage.plot sage.symbolic

            And another with some foldings::

                sage: pic = L.plot_alcoves(bounding_box=3)              # long time, needs sage.plot sage.symbolic
                sage: pic += L.plot_alcove_walk([0,1,2,0,2,0,1,2,0,1],  # long time (3s), needs sage.plot sage.symbolic
                ....:                      foldings=[False, False, True, False, False,
                ....:                                False, True, False, True, False],
                ....:                      color=\'green\'); pic
                Graphics object consisting of 155 graphics primitives

            TESTS::

                sage: L = RootSystem(["A",2,1]).weight_space()
                sage: p = L.plot_alcove_walk([0,1,2,0,2,0,1,2,0,1],                     # needs sage.plot sage.symbolic
                ....:                        foldings=[False, False, True, False, False,
                ....:                                  False, True, False, True, False],
                ....:                        color=\'green\',
                ....:                        start=L.rho())
                sage: print(p.description())                                            # needs sage.plot sage.symbolic
                Line defined by 2 points: [(-1.0, 8.0), (-1.5, 9.0)]
                Line defined by 2 points: [(1.0, 4.0), (1.5, 4.5)]
                Line defined by 2 points: [(1.0, 7.0), (1.5, 6.0)]
                Arrow from (-1.0,5.0) to (-2.0,7.0)
                Arrow from (-1.0,8.0) to (1.0,7.0)
                Arrow from (-1.5,9.0) to (-1.0,8.0)
                Arrow from (-2.0,7.0) to (-1.0,8.0)
                Arrow from (1.0,1.0) to (2.0,2.0)
                Arrow from (1.0,4.0) to (-1.0,5.0)
                Arrow from (1.0,7.0) to (2.0,8.0)
                Arrow from (1.5,4.5) to (1.0,4.0)
                Arrow from (1.5,6.0) to (1.0,7.0)
                Arrow from (2.0,2.0) to (1.0,4.0)
            '''
        def plot_ls_paths(self, paths, plot_labels=None, colored_labels: bool = True, **options):
            """
            Plot LS paths.

            INPUT:

            - ``paths`` -- a finite crystal or list of LS paths
            - ``plot_labels`` -- (default: ``None``) the distance to plot
              the LS labels from the endpoint of the path; set to ``None``
              to not display the labels
            - ``colored_labels`` -- boolean (default: ``True``); if ``True``, then
              color the labels the same color as the LS path
            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: B = crystals.LSPaths(['A',2], [1,1])                              # needs sage.combinat
                sage: L = RootSystem(['A',2]).ambient_space()
                sage: L.plot_fundamental_weights() + L.plot_ls_paths(B)                 # needs sage.combinat sage.plot sage.symbolic
                Graphics object consisting of 14 graphics primitives

            This also works in 3 dimensions::

                sage: B = crystals.LSPaths(['B',3], [2,0,0])                            # needs sage.combinat
                sage: L = RootSystem(['B',3]).ambient_space()
                sage: L.plot_ls_paths(B)                                                # needs sage.combinat sage.plot sage.symbolic
                Graphics3d Object
            """
        def plot_mv_polytope(self, mv_polytope, mark_endpoints: bool = True, circle_size: float = 0.06, circle_thickness: float = 1.6, wireframe: str = 'blue', fill: str = 'green', alpha: int = 1, **options):
            """
            Plot an MV polytope.

            INPUT:

            - ``mv_polytope`` -- an MV polytope
            - ``mark_endpoints`` -- boolean (default: ``True``); mark the endpoints
              of the MV polytope
            - ``circle_size`` -- (default: 0.06) the size of the circles
            - ``circle_thickness`` -- (default: 1.6) the thinkness of the
              extra rings of circles
            - ``wireframe`` -- (default: ``'blue'``) color to draw the
              wireframe of the polytope with
            - ``fill`` -- (default: ``'green'``) color to fill the polytope with
            - ``alpha`` -- (default: 1) the alpha value (opacity) of the fill
            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: B = crystals.infinity.MVPolytopes(['C',2])                        # needs sage.combinat
                sage: L = RootSystem(['C',2]).ambient_space()
                sage: p = B.highest_weight_vector().f_string([1,2,1,2])                 # needs sage.combinat
                sage: L.plot_fundamental_weights() + L.plot_mv_polytope(p)              # needs sage.combinat sage.geometry.polyhedron sage.plot sage.symbolic
                Graphics object consisting of 14 graphics primitives

            This also works in 3 dimensions::

                sage: B = crystals.infinity.MVPolytopes(['A',3])                        # needs sage.combinat
                sage: L = RootSystem(['A',3]).ambient_space()
                sage: p = B.highest_weight_vector().f_string([2,1,3,2])                 # needs sage.combinat
                sage: L.plot_mv_polytope(p)                                             # needs sage.combinat sage.geometry.polyhedron sage.plot sage.symbolic
                Graphics3d Object
            """
        def plot_crystal(self, crystal, plot_labels: bool = True, label_color: str = 'black', edge_labels: bool = False, circle_size: float = 0.06, circle_thickness: float = 1.6, **options):
            """
            Plot a finite crystal.

            INPUT:

            - ``crystal`` -- the finite crystal to plot
            - ``plot_labels`` -- boolean (default: ``True``); can be one of the
              following:

              * ``True`` -- use the latex labels
              * ``'circles'`` -- use circles for multiplicity up to 4; if the
                multiplicity is larger, then it uses the multiplicity
              * ``'multiplicities'`` -- use the multiplicities

            - ``label_color`` -- (default: ``'black'``) the color of the
              labels
            - ``edge_labels`` -- boolean (default: ``False``); if ``True``, then draw
              in the edge label
            - ``circle_size`` -- (default: 0.06) the size of the circles
            - ``circle_thickness`` -- (default: 1.6) the thinkness of the
              extra rings of circles
            - ``**options`` -- plotting options

            .. SEEALSO::

                - :meth:`plot` for a description of the plotting options
                - :ref:`sage.combinat.root_system.plot` for a tutorial
                  on root system plotting

            EXAMPLES::

                sage: # needs sage.combinat sage.plot sage.symbolic
                sage: L = RootSystem(['A',2]).ambient_space()
                sage: C = crystals.Tableaux(['A',2], shape=[2,1])
                sage: L.plot_crystal(C, plot_labels='multiplicities')
                Graphics object consisting of 15 graphics primitives
                sage: C = crystals.Tableaux(['A',2], shape=[8,4])
                sage: p = L.plot_crystal(C, plot_labels='circles')
                sage: p.show(figsize=15)

            A 3-dimensional example::

                sage: L = RootSystem(['B',3]).ambient_space()
                sage: C = crystals.Tableaux(['B',3], shape=[2,1])                       # needs sage.combinat
                sage: L.plot_crystal(C, plot_labels='circles',  # long time             # needs sage.combinat sage.plot sage.symbolic
                ....:                edge_labels=True)
                Graphics3d Object

            TESTS:

            Check that :issue:`29548` is fixed::

                sage: LS = crystals.LSPaths(['A',2], [1,1])                             # needs sage.combinat
                sage: L = RootSystem(['A',2]).ambient_space()
                sage: L.plot_crystal(LS)                                                # needs sage.combinat sage.plot sage.symbolic
                Graphics object consisting of 16 graphics primitives
            """
        @cached_method
        def dual_type_cospace(self):
            """
            Return the cospace of dual type.

            For example, if invoked on the root lattice of type `['B',2]`, returns the
            coroot lattice of type `['C',2]`.

            .. WARNING::

                Not implemented for ambient spaces.

            EXAMPLES::

                sage: CartanType(['B',2]).root_system().root_lattice().dual_type_cospace()
                Coroot lattice of the Root system of type ['C', 2]
                sage: CartanType(['F',4]).root_system().coweight_lattice().dual_type_cospace()
                Weight lattice of the Root system of type ['F', 4]
                 relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            """
        def to_ambient_space_morphism(self) -> None:
            """
            Return the morphism to the ambient space.

            EXAMPLES::

                sage: B2rs = CartanType(['B',2]).root_system()
                sage: B2rs.root_lattice().to_ambient_space_morphism()
                Generic morphism:
                  From: Root lattice of the Root system of type ['B', 2]
                  To:   Ambient space of the Root system of type ['B', 2]
                sage: B2rs.coroot_lattice().to_ambient_space_morphism()
                Generic morphism:
                  From: Coroot lattice of the Root system of type ['B', 2]
                  To:   Ambient space of the Root system of type ['B', 2]
                sage: B2rs.weight_lattice().to_ambient_space_morphism()
                Generic morphism:
                  From: Weight lattice of the Root system of type ['B', 2]
                  To:   Ambient space of the Root system of type ['B', 2]
            """
    class ElementMethods:
        @abstract_method
        def scalar(self, lambdacheck) -> None:
            """
            Implement the natural pairing with the coroot lattice.

            INPUT:

            - ``self`` -- an element of a root lattice realization
            - ``lambdacheck`` -- an element of the coroot lattice or coroot space

            OUTPUT: the scalar product of ``self`` and ``lambdacheck``

            EXAMPLES::

                sage: L = RootSystem(['A',4]).root_lattice()
                sage: alpha      = L.simple_roots()
                sage: alphacheck = L.simple_coroots()
                sage: alpha[1].scalar(alphacheck[1])                                    # needs sage.graphs
                2
                sage: alpha[1].scalar(alphacheck[2])                                    # needs sage.graphs
                -1
                sage: matrix([ [ alpha[i].scalar(alphacheck[j])                         # needs sage.graphs
                ....:            for i in L.index_set() ]
                ....:          for j in L.index_set() ])
                [ 2 -1  0  0]
                [-1  2 -1  0]
                [ 0 -1  2 -1]
                [ 0  0 -1  2]

            TESTS::

                sage: super(sage.combinat.root_system.root_space.RootSpaceElement,alpha[1]).scalar(alphacheck[1])
                Traceback (most recent call last):
                ...
                NotImplementedError: <abstract method scalar at ...>
            """
        def symmetric_form(self, alpha):
            """
            Return the symmetric form of ``self`` with ``alpha``.

            Consider the simple roots `\\alpha_i` and let `(b_{ij})_{ij}`
            denote the symmetrized Cartan matrix `(a_{ij})_{ij}`, we have

            .. MATH::

                (\\alpha_i | \\alpha_j) = b_{ij}

            and extended bilinearly. See Chapter 6 in Kac, Infinite
            Dimensional Lie Algebras for more details.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[1].symmetric_form(alpha[0])
                0
                sage: alpha[1].symmetric_form(alpha[1])
                4
                sage: elt = alpha[0] - 3*alpha[1] + alpha[2]
                sage: elt.symmetric_form(alpha[1])
                -14
                sage: elt.symmetric_form(alpha[0]+2*alpha[2])
                14

                sage: Q = RootSystem(CartanType(['A',4,2]).dual()).root_lattice()
                sage: Qc = RootSystem(['A',4,2]).coroot_lattice()
                sage: alpha = Q.simple_roots()
                sage: alphac = Qc.simple_roots()
                sage: elt = alpha[0] + 2*alpha[1] + 2*alpha[2]
                sage: eltc = alphac[0] + 2*alphac[1] + 2*alphac[2]
                sage: elt.symmetric_form(alpha[1])                                      # needs sage.graphs
                0
                sage: eltc.symmetric_form(alphac[1])                                    # needs sage.graphs
                0
            """
        def norm_squared(self):
            """
            Return the norm squared of ``self`` with respect to the
            symmetric form.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[1].norm_squared()
                4
                sage: alpha[2].norm_squared()
                2
                sage: elt = alpha[0] - 3*alpha[1] + alpha[2]
                sage: elt.norm_squared()
                50
                sage: elt = alpha[0] + alpha[1] + 2*alpha[2]
                sage: elt.norm_squared()
                0

                sage: Q = RootSystem(CartanType(['A',4,2]).dual()).root_lattice()
                sage: Qc = RootSystem(['A',4,2]).coroot_lattice()
                sage: alpha = Q.simple_roots()
                sage: alphac = Qc.simple_roots()
                sage: elt = alpha[0] + 2*alpha[1] + 2*alpha[2]
                sage: eltc = alphac[0] + 2*alphac[1] + 2*alphac[2]
                sage: elt.norm_squared()                                                # needs sage.graphs
                0
                sage: eltc.norm_squared()                                               # needs sage.graphs
                0
            """
        def simple_reflection(self, i):
            '''
            Return the image of ``self`` by the `i`-th simple reflection.

            EXAMPLES::

                sage: alpha = RootSystem(["A", 3]).root_lattice().alpha()
                sage: alpha[1].simple_reflection(2)                                     # needs sage.graphs
                alpha[1] + alpha[2]

                sage: Q = RootSystem([\'A\', 3, 1]).weight_lattice(extended=True)
                sage: Lambda = Q.fundamental_weights()
                sage: L = Lambda[0] + Q.null_root()                                     # needs sage.graphs
                sage: L.simple_reflection(0)                                            # needs sage.graphs
                -Lambda[0] + Lambda[1] + Lambda[3]
            '''
        def simple_reflections(self):
            '''
            The images of ``self`` by all the simple reflections.

            EXAMPLES::

                sage: alpha = RootSystem(["A", 3]).root_lattice().alpha()
                sage: alpha[1].simple_reflections()                                     # needs sage.graphs
                [-alpha[1], alpha[1] + alpha[2], alpha[1]]
            '''
        def orbit(self):
            '''
            The orbit of ``self`` under the action of the Weyl group.

            EXAMPLES:

            `\\rho` is a regular element whose orbit is in bijection
            with the Weyl group. In particular, it has 6 elements for
            the symmetric group `S_3`::

                sage: L = RootSystem(["A", 2]).ambient_lattice()
                sage: sorted(L.rho().orbit())               # the output order is not specified
                [(1, 2, 0), (1, 0, 2), (2, 1, 0),
                 (2, 0, 1), (0, 1, 2), (0, 2, 1)]

                sage: L = RootSystem(["A", 3]).weight_lattice()
                sage: len(L.rho().orbit())                                              # needs sage.graphs
                24
                sage: len(L.fundamental_weights()[1].orbit())                           # needs sage.graphs
                4
                sage: len(L.fundamental_weights()[2].orbit())                           # needs sage.graphs
                6

            TESTS::

                sage: la = RootSystem([\'A\',1,1]).weight_lattice().fundamental_weight(0)
                sage: la.orbit()
                Traceback (most recent call last):
                ...
                ValueError: cannot list an infinite set
            '''
        def dot_orbit(self):
            """
            The orbit of ``self`` under the dot or affine action of
            the Weyl group.

            EXAMPLES::

                sage: L = RootSystem(['A', 2]).ambient_lattice()
                sage: sorted(L.rho().dot_orbit())                      # the output order is not specified              # needs sage.graphs
                [(-2, 1, 4), (-2, 3, 2), (2, -1, 2),
                 (2, 1, 0), (0, -1, 4), (0, 3, 0)]

                sage: L = RootSystem(['B',2]).weight_lattice()
                sage: sorted(L.fundamental_weights()[1].dot_orbit())   # the output order is not specified              # needs sage.graphs
                [-4*Lambda[1], -4*Lambda[1] + 4*Lambda[2],
                 -3*Lambda[1] - 2*Lambda[2], -3*Lambda[1] + 4*Lambda[2],
                 Lambda[1], Lambda[1] - 6*Lambda[2],
                 2*Lambda[1] - 6*Lambda[2], 2*Lambda[1] - 2*Lambda[2]]

            We compare the dot action orbit to the regular orbit::

                sage: # needs sage.graphs
                sage: L = RootSystem(['A', 3]).weight_lattice()
                sage: len(L.rho().dot_orbit())
                24
                sage: len((-L.rho()).dot_orbit())
                1
                sage: La = L.fundamental_weights()
                sage: len(La[1].dot_orbit())
                24
                sage: len(La[1].orbit())
                4
                sage: len((-L.rho() + La[1]).dot_orbit())
                4
                sage: len(La[2].dot_orbit())
                24
                sage: len(La[2].orbit())
                6
                sage: len((-L.rho() + La[2]).dot_orbit())
                6
            """
        affine_orbit = dot_orbit
        def associated_coroot(self) -> None:
            '''
            Return the coroot associated to this root.

            EXAMPLES::

                sage: alpha = RootSystem(["A", 3]).root_space().simple_roots()
                sage: alpha[1].associated_coroot()                                      # needs sage.graphs
                alphacheck[1]
            '''
        def reflection(self, root, use_coroot: bool = False):
            """
            Reflect ``self`` across the hyperplane orthogonal to ``root``.

            If ``use_coroot`` is ``True``, ``root`` is interpreted as a coroot.

            EXAMPLES::

                sage: R = RootSystem(['C',4])
                sage: weight_lattice = R.weight_lattice()
                sage: mu = weight_lattice.from_vector(vector([0,0,1,2]))
                sage: coroot_lattice = R.coroot_lattice()
                sage: alphavee = coroot_lattice.from_vector(vector([0,0,1,1]))
                sage: mu.reflection(alphavee, use_coroot=True)                          # needs sage.graphs
                6*Lambda[2] - 5*Lambda[3] + 2*Lambda[4]
                sage: root_lattice = R.root_lattice()
                sage: beta = root_lattice.from_vector(vector([0,1,1,0]))
                sage: mu.reflection(beta)                                               # needs sage.graphs
                Lambda[1] - Lambda[2] + 3*Lambda[4]
            """
        def has_descent(self, i, positive: bool = False) -> bool:
            """
            Test if ``self`` has a descent at position `i`, that is, if ``self`` is
            on the strict negative side of the `i`-th simple reflection
            hyperplane.

            If positive is ``True``, tests if it is on the strict positive
            side instead.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',5]).weight_space()
                sage: alpha = RootSystem(['A',5]).weight_space().simple_roots()
                sage: [alpha[i].has_descent(1) for i in space.index_set()]
                [False, True, False, False, False]
                sage: [(-alpha[i]).has_descent(1) for i in space.index_set()]
                [True, False, False, False, False]
                sage: [alpha[i].has_descent(1, True) for i in space.index_set()]
                [True, False, False, False, False]
                sage: [(-alpha[i]).has_descent(1, True) for i in space.index_set()]
                [False, True, False, False, False]
                sage: (alpha[1]+alpha[2]+alpha[4]).has_descent(3)
                True
                sage: (alpha[1]+alpha[2]+alpha[4]).has_descent(1)
                False
                sage: (alpha[1]+alpha[2]+alpha[4]).has_descent(1, True)
                True
            """
        def first_descent(self, index_set=None, positive: bool = False):
            """
            Return the first descent of pt.

            One can use the ``index_set`` option to restrict to the parabolic
            subgroup indexed by ``index_set``.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',5]).weight_space()
                sage: alpha = space.simple_roots()
                sage: (alpha[1]+alpha[2]+alpha[4]).first_descent()
                3
                sage: (alpha[1]+alpha[2]+alpha[4]).first_descent([1,2,5])
                5
                sage: (alpha[1]+alpha[2]+alpha[4]).first_descent([1,2,5,3,4])
                5
            """
        def descents(self, index_set=None, positive: bool = False):
            """
            Return the descents of pt.

            EXAMPLES::

                sage: space=RootSystem(['A',5]).weight_space()
                sage: alpha = space.simple_roots()                                      # needs sage.graphs
                sage: (alpha[1]+alpha[2]+alpha[4]).descents()                           # needs sage.graphs
                [3, 5]
            """
        def to_dominant_chamber(self, index_set=None, positive: bool = True, reduced_word: bool = False):
            """
            Return the unique dominant element in the Weyl group orbit of the vector ``self``.

            If ``positive`` is ``False``, returns the antidominant orbit element.

            With the ``index_set`` optional parameter, this is done with
            respect to the corresponding parabolic subgroup.

            If ``reduced_word`` is ``True``, returns the 2-tuple (``weight``, ``direction``)
            where ``weight`` is the (anti)dominant orbit element and ``direction`` is a reduced word
            for the Weyl group element sending ``weight`` to ``self``.

            .. warning::

                In infinite type, an orbit may not contain a dominant element.
                In this case the function may go into an infinite loop.

                For affine root systems, errors are generated if
                the orbit does not contain the requested kind of representative.
                If the input vector is of positive (resp. negative)
                level, then there is a dominant (resp. antidominant) element in its orbit
                but not an antidominant (resp. dominant) one. If the vector is of level zero,
                then there are neither dominant nor antidominant orbit representatives, except
                for multiples of the null root, which are themselves both dominant and antidominant
                orbit representatives.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: space = RootSystem(['A',5]).weight_space()
                sage: alpha = RootSystem(['A',5]).weight_space().simple_roots()
                sage: alpha[1].to_dominant_chamber()
                Lambda[1] + Lambda[5]
                sage: alpha[1].to_dominant_chamber([1,2])
                Lambda[1] + Lambda[2] - Lambda[3]
                sage: wl = RootSystem(['A',2,1]).weight_lattice(extended=True)
                sage: mu = wl.from_vector(vector([1,-3,0]))
                sage: mu.to_dominant_chamber(positive=False, reduced_word=True)
                (-Lambda[1] - Lambda[2] - delta, [0, 2])

                sage: # needs sage.graphs
                sage: R = RootSystem(['A',1,1])
                sage: rl = R.root_lattice()
                sage: nu = rl.zero()
                sage: nu.to_dominant_chamber()
                0
                sage: nu.to_dominant_chamber(positive=False)
                0
                sage: mu = rl.from_vector(vector([0,1]))
                sage: mu.to_dominant_chamber()
                Traceback (most recent call last):
                ...
                ValueError: alpha[1] is not in the orbit of the fundamental chamber
                sage: mu.to_dominant_chamber(positive=False)
                Traceback (most recent call last):
                ...
                ValueError: alpha[1] is not in the orbit of the negative of the fundamental chamber
            """
        def reduced_word(self, index_set=None, positive: bool = True):
            """
            Return a reduced word for the inverse of the shortest Weyl group element that sends the vector ``self`` into the dominant chamber.

            With the ``index_set`` optional parameter, this is done with
            respect to the corresponding parabolic subgroup.

            If ``positive`` is False, use the antidominant chamber instead.

            EXAMPLES::

                sage: space = RootSystem(['A',5]).weight_space()
                sage: alpha = RootSystem(['A',5]).weight_space().simple_roots()         # needs sage.graphs
                sage: alpha[1].reduced_word()                                           # needs sage.graphs
                [2, 3, 4, 5]
                sage: alpha[1].reduced_word([1,2])                                      # needs sage.graphs
                [2]
            """
        def is_dominant(self, index_set=None, positive: bool = True):
            """
            Return whether ``self`` is dominant.

            This is done with respect to the sub--root system indicated by the subset of Dynkin nodes
            ``index_set``. If ``index_set`` is ``None``, then the entire Dynkin node set is used.
            If positive is ``False``, then the dominance condition is replaced by antidominance.

            EXAMPLES::

                sage: L = RootSystem(['A',2]).ambient_lattice()
                sage: Lambda = L.fundamental_weights()
                sage: [x.is_dominant() for x in Lambda]
                [True, True]
                sage: [x.is_dominant(positive=False) for x in Lambda]
                [False, False]
                sage: (Lambda[1]-Lambda[2]).is_dominant()
                False
                sage: (-Lambda[1]+Lambda[2]).is_dominant()
                False
                sage: (Lambda[1]-Lambda[2]).is_dominant([1])
                True
                sage: (Lambda[1]-Lambda[2]).is_dominant([2])
                False
                sage: [x.is_dominant() for x in L.roots()]
                [False, True, False, False, False, False]
                sage: [x.is_dominant(positive=False) for x in L.roots()]
                [False, False, False, False, True, False]
            """
        def is_dominant_weight(self):
            """
            Test whether ``self`` is a dominant element of the weight lattice.

            EXAMPLES::

                sage: L = RootSystem(['A',2]).ambient_lattice()
                sage: Lambda = L.fundamental_weights()
                sage: [x.is_dominant() for x in Lambda]
                [True, True]
                sage: (3*Lambda[1]+Lambda[2]).is_dominant()
                True
                sage: (Lambda[1]-Lambda[2]).is_dominant()
                False
                sage: (-Lambda[1]+Lambda[2]).is_dominant()
                False

            Tests that the scalar products with the coroots are all
            nonnegative integers. For example, if `x` is the sum of a
            dominant element of the weight lattice plus some other element
            orthogonal to all coroots, then the implementation correctly
            reports `x` to be a dominant weight::

               sage: x = Lambda[1] + L([-1,-1,-1])
               sage: x.is_dominant_weight()
               True
            """
        def is_verma_dominant(self, positive: bool = True):
            """
            Return if ``self`` is Verma dominant.

            A weight `\\lambda` is *Verma dominant* if

            .. MATH::

                \\langle \\lambda + \\rho, \\alpha^{\\vee} \\rangle \\notin \\ZZ_{<0}

            for all positive roots `\\alpha`. Note that begin Verma dominant does
            *not* imply that `\\langle \\lambda+\\rho, \\alpha^{\\vee} \\rangle \\geq 0`
            for any positive root `\\alpha`. This is used to determine if
            a Verma module is simple or projective.

            INPUT:

            - ``positive`` -- boolean (default: ``True``); if ``False``, then
              this checks if the weight is Verma anti-dominant, where
              `\\ZZ_{<0}` is replaced with `\\ZZ_{>0}` in the definition.

            EXAMPLES::

                sage: P = RootSystem(['A', 3]).weight_space()
                sage: La = P.fundamental_weights()
                sage: alphacheck = P.coroot_lattice().positive_roots()
                sage: rho = P.rho()
                sage: (La[1] + 2*La[2]).is_verma_dominant()
                True
                sage: la = La[1] - 3/2*La[3] - rho
                sage: la.is_verma_dominant()
                True
                sage: la.is_verma_dominant(positive=False)
                False
                sage: [(la+rho).scalar(coroot) for coroot in alphacheck]
                [1, 0, -3/2, 1, -3/2, -1/2]
                sage: mu = 1/2*La[1] - 3/2*La[3] - rho
                sage: mu.is_verma_dominant()
                False
                sage: mu.is_verma_dominant(positive=False)
                True
                sage: [(mu+rho).scalar(coroot) for coroot in alphacheck]
                [1/2, 0, -3/2, 1/2, -3/2, -1]
            """
        def succ(self, index_set=None):
            """
            Return the immediate successors of ``self`` for the weak order.

            INPUT:

            - ``index_set`` -- a subset (as a list or iterable) of the
              nodes of the Dynkin diagram; (default: ``None`` for all of them)

            If ``index_set`` is specified, the successors for the
            corresponding parabolic subsystem are returned.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: L = RootSystem(['A',3]).weight_lattice()
                sage: Lambda = L.fundamental_weights()
                sage: Lambda[1].succ()
                [-Lambda[1] + Lambda[2]]
                sage: L.rho().succ()
                [-Lambda[1] + 2*Lambda[2] + Lambda[3],
                 2*Lambda[1] - Lambda[2] + 2*Lambda[3],
                 Lambda[1] + 2*Lambda[2] - Lambda[3]]
                sage: (-L.rho()).succ()
                []
                sage: L.rho().succ(index_set=[1])
                [-Lambda[1] + 2*Lambda[2] + Lambda[3]]
                sage: L.rho().succ(index_set=[2])
                [2*Lambda[1] - Lambda[2] + 2*Lambda[3]]
            """
        def pred(self, index_set=None):
            """
            Return the immediate predecessors of ``self`` for the weak order.

            INPUT:

            - ``index_set`` -- a subset (as a list or iterable) of the
              nodes of the Dynkin diagram; (default: ``None`` for all of them)

            If ``index_set`` is specified, the successors for the
            corresponding parabolic subsystem are returned.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).weight_lattice()
                sage: Lambda = L.fundamental_weights()
                sage: Lambda[1].pred()
                []
                sage: L.rho().pred()
                []
                sage: (-L.rho()).pred()                                                 # needs sage.graphs
                [Lambda[1] - 2*Lambda[2] - Lambda[3],
                 -2*Lambda[1] + Lambda[2] - 2*Lambda[3],
                 -Lambda[1] - 2*Lambda[2] + Lambda[3]]
                sage: (-L.rho()).pred(index_set=[1])                                    # needs sage.graphs
                [Lambda[1] - 2*Lambda[2] - Lambda[3]]
            """
        def greater(self):
            """
            Return the elements in the orbit of ``self`` which are
            greater than ``self`` in the weak order.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).ambient_lattice()
                sage: e = L.basis()
                sage: e[2].greater()
                [(0, 0, 1, 0), (0, 0, 0, 1)]
                sage: len(L.rho().greater())
                24
                sage: len((-L.rho()).greater())
                1
                sage: sorted([len(x.greater()) for x in L.rho().orbit()])
                [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 8, 8, 8, 8, 12, 12, 12, 24]
            """
        def smaller(self):
            """
            Return the elements in the orbit of ``self`` which are
            smaller than ``self`` in the weak order.

            EXAMPLES::

                sage: L = RootSystem(['A',3]).ambient_lattice()
                sage: e = L.basis()
                sage: e[2].smaller()
                [(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)]
                sage: len(L.rho().smaller())
                1
                sage: len((-L.rho()).smaller())
                24
                sage: sorted([len(x.smaller()) for x in L.rho().orbit()])
                [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 8, 8, 8, 8, 12, 12, 12, 24]
            """
        def extraspecial_pair(self):
            """
            Return the extraspecial pair of ``self`` under the ordering
            defined by
            :meth:`~sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods.positive_roots_by_height`.

            The *extraspecial pair* of a positive root `\\gamma` with some total
            ordering `<` of the root lattice that respects height is the pair
            of positive roots `(\\alpha, \\beta)` such that `\\gamma = \\alpha +
            \\beta` and `\\alpha` is as small as possible.

            EXAMPLES::

                sage: Q = RootSystem(['G', 2]).root_lattice()
                sage: Q.highest_root().extraspecial_pair()                              # needs sage.graphs
                (alpha[2], 3*alpha[1] + alpha[2])
            """
        def height(self):
            """
            Return the height of ``self``.

            The height of a root `\\alpha = \\sum_i a_i \\alpha_i` is defined
            to be `h(\\alpha) := \\sum_i a_i`.

            EXAMPLES::

                sage: Q = RootSystem(['G', 2]).root_lattice()
                sage: Q.highest_root().height()                                         # needs sage.graphs
                5
            """
        def level(self):
            """
            EXAMPLES::

                sage: L = RootSystem(['A',2,1]).weight_lattice()
                sage: L.rho().level()                                                   # needs sage.graphs
                3
            """
        @cached_in_parent_method
        def to_simple_root(self, reduced_word: bool = False):
            '''
            Return (the index of) a simple root in the orbit of the positive root ``self``.

            INPUT:

            - ``self`` -- a positive root
            - ``reduced_word`` -- boolean (default: ``False``)

            OUTPUT:

            - The index `i` of a simple root `\\alpha_i`.
              If ``reduced_word`` is ``True``, this returns instead a pair
              ``(i, word)``, where word is a sequence of reflections
              mapping `\\alpha_i` up the root poset to ``self``.

            EXAMPLES::

                sage: L = RootSystem(["A",3]).root_lattice()
                sage: positive_roots = L.positive_roots()
                sage: for alpha in sorted(positive_roots):                              # needs sage.graphs
                ....:     print("{} {}".format(alpha, alpha.to_simple_root()))
                alpha[1] 1
                alpha[1] + alpha[2] 2
                alpha[1] + alpha[2] + alpha[3] 3
                alpha[2] 2
                alpha[2] + alpha[3] 3
                alpha[3] 3
                sage: for alpha in sorted(positive_roots):                              # needs sage.graphs
                ....:     print("{} {}".format(alpha, alpha.to_simple_root(reduced_word=True)))
                alpha[1] (1, ())
                alpha[1] + alpha[2] (2, (1,))
                alpha[1] + alpha[2] + alpha[3] (3, (1, 2))
                alpha[2] (2, ())
                alpha[2] + alpha[3] (3, (2,))
                alpha[3] (3, ())

            ALGORITHM:

            This method walks from ``self`` down to the antidominant
            chamber by applying successively the simple reflection
            given by the first descent. Since ``self`` is a positive
            root, each step goes down the root poset, and one must
            eventually cross a simple root `\\alpha_i`.

            .. SEEALSO::

                - :meth:`first_descent`
                - :meth:`to_dominant_chamber`

            .. WARNING::

                The behavior is not specified if the input is not a
                positive root. For a finite root system, this is
                currently caught (albeit with a not perfect message)::

                    sage: alpha = L.simple_roots()                                      # needs sage.graphs
                    sage: (2*alpha[1]).to_simple_root()                                 # needs sage.graphs
                    Traceback (most recent call last):
                    ...
                    ValueError: -2*alpha[1] - 2*alpha[2] - 2*alpha[3] is not a positive root

                For an infinite root system, this method may run into
                an infinite recursion if the input is not a positive
                root.
            '''
        @cached_in_parent_method
        def associated_reflection(self):
            """
            Given a positive root ``self``, return a reduced word for the reflection orthogonal to ``self``.

            Since the answer is cached, it is a tuple instead of a list.

            EXAMPLES::

                sage: C3_rl = RootSystem(['C',3]).root_lattice()                        # needs sage.graphs
                sage: C3_rl.simple_root(3).weyl_action([1,2]).associated_reflection()   # needs sage.graphs
                (1, 2, 3, 2, 1)
                sage: C3_rl.simple_root(2).associated_reflection()                      # needs sage.graphs
                (2,)
            """
        def translation(self, x):
            """
            Return `x` translated by `t`, that is, `x+level(x) t`.

            INPUT:

            - ``self`` -- an element `t` at level `0`
            - ``x`` -- an element of the same space

            EXAMPLES::

                sage: L = RootSystem(['A',2,1]).weight_lattice()
                sage: alpha = L.simple_roots()                                          # needs sage.graphs
                sage: Lambda = L.fundamental_weights()                                  # needs sage.graphs
                sage: t = alpha[2]                                                      # needs sage.graphs

            Let us look at the translation of an element of level `1`::

                sage: Lambda[1].level()                                                 # needs sage.graphs
                1
                sage: t.translation(Lambda[1])                                          # needs sage.graphs
                -Lambda[0] + 2*Lambda[2]
                sage: Lambda[1] + t                                                     # needs sage.graphs
                -Lambda[0] + 2*Lambda[2]

            and of an element of level `0`::

                sage: alpha[1].level()                                                  # needs sage.graphs
                0
                sage: t.translation(alpha [1])                                          # needs sage.graphs
                -Lambda[0] + 2*Lambda[1] - Lambda[2]
                sage: alpha[1] + 0*t                                                    # needs sage.graphs
                -Lambda[0] + 2*Lambda[1] - Lambda[2]

            The arguments are given in this seemingly unnatural order to
            make it easy to construct the translation function::

                sage: f = t.translation                                                 # needs sage.graphs
                sage: f(Lambda[1])                                                      # needs sage.graphs
                -Lambda[0] + 2*Lambda[2]
            """
        def weyl_action(self, element, inverse: bool = False):
            """
            Act on ``self`` by an element of the Coxeter or Weyl group.

            INPUT:

            - ``element`` -- an element of a Coxeter or Weyl group
              of the same Cartan type, or a tuple or a list (such as a
              reduced word) of elements from the index set

            - ``inverse`` -- boolean (default: ``False``); whether to
              act by the inverse element

            EXAMPLES::

                sage: wl = RootSystem(['A',3]).weight_lattice()
                sage: mu = wl.from_vector(vector([1,0,-2]))
                sage: mu
                Lambda[1] - 2*Lambda[3]
                sage: mudom, rw = mu.to_dominant_chamber(positive=False,                # needs sage.graphs
                ....:                                    reduced_word=True)
                sage: mudom, rw                                                         # needs sage.graphs
                (-Lambda[2] - Lambda[3], [1, 2])

            Acting by a (reduced) word::

                sage: mudom.weyl_action(rw)                                             # needs sage.graphs
                Lambda[1] - 2*Lambda[3]
                sage: mu.weyl_action(rw, inverse=True)                                  # needs sage.graphs
                -Lambda[2] - Lambda[3]

            Acting by an element of the Coxeter or Weyl group on a vector in its own
            lattice of definition (implemented by matrix multiplication on a vector)::

                sage: w = wl.weyl_group().from_reduced_word([1, 2])                     # needs sage.graphs sage.libs.gap
                sage: mudom.weyl_action(w)                                              # needs sage.graphs sage.libs.gap
                Lambda[1] - 2*Lambda[3]

            Acting by an element of an isomorphic Coxeter or Weyl group (implemented by the
            action of a corresponding reduced word)::

                sage: # needs sage.libs.gap
                sage: W = WeylGroup(['A',3], prefix='s')
                sage: w = W.from_reduced_word([1, 2])
                sage: wl.weyl_group() == W
                False
                sage: mudom.weyl_action(w)                                              # needs sage.graphs
                Lambda[1] - 2*Lambda[3]
            """
        def weyl_stabilizer(self, index_set=None):
            """
            Return the subset of Dynkin nodes whose reflections fix ``self``.

            If ``index_set`` is not ``None``, only consider nodes in this set.
            Note that if ``self`` is dominant or antidominant, then its stabilizer is the
            parabolic subgroup defined by the returned node set.

            EXAMPLES::

                sage: wl = RootSystem(['A',2,1]).weight_lattice(extended=True)
                sage: al = wl.null_root()                                               # needs sage.graphs
                sage: al.weyl_stabilizer()                                              # needs sage.graphs
                [0, 1, 2]
                sage: wl = RootSystem(['A',4]).weight_lattice()
                sage: mu = wl.from_vector(vector([1,1,0,0]))
                sage: mu.weyl_stabilizer()
                [3, 4]
                sage: mu.weyl_stabilizer(index_set = [1,2,3])
                [3]
            """
        def dot_action(self, w, inverse: bool = False):
            """
            Act on ``self`` by ``w`` using the dot or affine action.

            Let `w` be an element of the Weyl group. The *dot action*
            or *affine action* is given by:

            .. MATH::

                w \\bullet \\lambda = w (\\lambda + \\rho) - \\rho,

            where `\\rho` is the sum of the fundamental weights.

            INPUT:

            - ``w`` -- an element of a Coxeter or Weyl group of
              the same Cartan type, or a tuple or a list (such
              as a reduced word) of elements from the index set

            - ``inverse`` -- boolean (default: ``False``); whether
              to act by the inverse element

            EXAMPLES::

                sage: P = RootSystem(['B',3]).weight_lattice()
                sage: La = P.fundamental_weights()
                sage: mu = La[1] + 2*La[2] - 3*La[3]
                sage: mu.dot_action([1])                                                # needs sage.graphs
                -3*Lambda[1] + 4*Lambda[2] - 3*Lambda[3]
                sage: mu.dot_action([3])                                                # needs sage.graphs
                Lambda[1] + Lambda[3]
                sage: mu.dot_action([1,2,3])                                            # needs sage.graphs
                -4*Lambda[1] + Lambda[2] + 3*Lambda[3]

            We check that the origin of this action is at `-\\rho`::

                sage: all((-P.rho()).dot_action([i]) == -P.rho()                        # needs sage.graphs
                ....:     for i in P.index_set())
                True

            REFERENCES:

            - :wikipedia:`Affine_action`
            """
        def is_parabolic_root(self, index_set):
            """
            Return whether ``root`` is in the parabolic subsystem with Dynkin nodes ``index_set``.

            This assumes that ``self`` is a root.

            INPUT:

            - ``index_set`` -- the Dynkin node set of the parabolic subsystem

            .. TODO:: This implementation is only valid in the root or weight lattice

            EXAMPLES::

                sage: alpha = RootSystem(['A',3]).root_lattice().from_vector(vector([1,1,0]))
                sage: alpha.is_parabolic_root([1,3])
                False
                sage: alpha.is_parabolic_root([1,2])
                True
                sage: alpha.is_parabolic_root([2])
                False
            """
        def is_short_root(self):
            """
            Return ``True`` if ``self`` is a short (real) root.

            Returns ``False`` unless the parent is an irreducible root system of finite type
            having two root lengths and ``self`` is of the shorter length.
            There is no check of whether ``self`` is actually a root.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: Q = RootSystem(['C',2]).root_lattice()
                sage: al = Q.simple_root(1).weyl_action([1,2]); al
                alpha[1] + alpha[2]
                sage: al.is_short_root()
                True
                sage: bt = Q.simple_root(2).weyl_action([2,1,2]); bt
                -2*alpha[1] - alpha[2]
                sage: bt.is_short_root()
                False
                sage: RootSystem(['A',2]).root_lattice().simple_root(1).is_short_root()
                False

            An example in affine type::

                sage: # needs sage.graphs
                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[0].is_short_root()
                False
                sage: alpha[1].is_short_root()
                False
                sage: alpha[2].is_short_root()
                True
            """
        def to_dual_type_cospace(self):
            """
            Map ``self`` to the dual type cospace.

            For example, if ``self`` is in the root lattice of type `['B',2]`, send it to
            the coroot lattice of type `['C',2]`.

            EXAMPLES::

                sage: v = CartanType(['C',3]).root_system().weight_lattice().an_element(); v
                2*Lambda[1] + 2*Lambda[2] + 3*Lambda[3]
                sage: w = v.to_dual_type_cospace(); w
                2*Lambdacheck[1] + 2*Lambdacheck[2] + 3*Lambdacheck[3]
                sage: w.parent()
                Coweight lattice of the Root system of type ['B', 3]
            """
        def to_classical(self):
            """
            Map ``self`` to the classical lattice/space.

            Only makes sense for affine type.

            EXAMPLES::

                sage: R = CartanType(['A',3,1]).root_system()
                sage: alpha = R.root_lattice().an_element(); alpha
                2*alpha[0] + 2*alpha[1] + 3*alpha[2]
                sage: alb = alpha.to_classical(); alb                                   # needs sage.graphs
                alpha[2] - 2*alpha[3]
                sage: alb.parent()                                                      # needs sage.graphs
                Root lattice of the Root system of type ['A', 3]
                sage: v = R.ambient_space().an_element(); v
                2*e[0] + 2*e[1] + 3*e[2]
                sage: v.to_classical()                                                  # needs sage.graphs
                (2, 2, 3, 0)
            """
        def to_ambient(self) -> None:
            """
            Map ``self`` to the ambient space.

            EXAMPLES::

                sage: B4_rs = CartanType(['B',4]).root_system()
                sage: alpha = B4_rs.root_lattice().an_element(); alpha
                2*alpha[1] + 2*alpha[2] + 3*alpha[3]
                sage: alpha.to_ambient()
                (2, 0, 1, -3)
                sage: mu = B4_rs.weight_lattice().an_element(); mu
                2*Lambda[1] + 2*Lambda[2] + 3*Lambda[3]
                sage: mu.to_ambient()
                (7, 5, 3, 0)
                sage: v = B4_rs.ambient_space().an_element(); v
                (2, 2, 3, 0)
                sage: v.to_ambient()
                (2, 2, 3, 0)
                sage: alphavee = B4_rs.coroot_lattice().an_element(); alphavee
                2*alphacheck[1] + 2*alphacheck[2] + 3*alphacheck[3]
                sage: alphavee.to_ambient()
                (2, 0, 1, -3)
            """
        def is_long_root(self):
            """
            Return ``True`` if ``self`` is a long (real) root.

            EXAMPLES::

                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[0].is_long_root()                                           # needs sage.graphs
                True
                sage: alpha[1].is_long_root()                                           # needs sage.graphs
                True
                sage: alpha[2].is_long_root()                                           # needs sage.graphs
                False
            """
        def is_imaginary_root(self):
            """
            Return ``True`` if ``self`` is an imaginary root.

            A root `\\alpha` is imaginary if it is not `W`-conjugate
            to a simple root where `W` is the corresponding Weyl group.

            EXAMPLES::

                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[0].is_imaginary_root()                                      # needs sage.graphs
                False
                sage: elt = alpha[0] + alpha[1] + 2*alpha[2]
                sage: elt.is_imaginary_root()                                           # needs sage.graphs
                True
            """
        def is_real_root(self):
            """
            Return ``True`` if ``self`` is a real root.

            A root `\\alpha` is real if it is `W`-conjugate to a simple
            root where `W` is the corresponding Weyl group.

            EXAMPLES::

                sage: Q = RootSystem(['B',2,1]).root_lattice()
                sage: alpha = Q.simple_roots()
                sage: alpha[0].is_real_root()                                           # needs sage.graphs
                True
                sage: elt = alpha[0] + alpha[1] + 2*alpha[2]
                sage: elt.is_real_root()                                                # needs sage.graphs
                False
            """
