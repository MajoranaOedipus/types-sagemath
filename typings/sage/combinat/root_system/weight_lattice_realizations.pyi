from .root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family

class WeightLatticeRealizations(Category_over_base_ring):
    '''
    The category of weight lattice realizations over a given base ring.

    A *weight lattice realization* `L` over a base ring `R` is a free
    module (or vector space if `R` is a field) endowed with an embedding
    of the root lattice of some root system. By restriction, this
    embedding defines an embedding of the root lattice of this root
    system, which makes `L` a root lattice realization.

    Typical weight lattice realizations over `\\ZZ` include the weight
    lattice, and ambient lattice. Typical weight lattice realizations
    over `\\QQ` include the weight space, and ambient space.

    To describe the embedding, a weight lattice realization must
    implement a method
    :meth:`~RootLatticeRealizations.ParentMethods.fundamental_weight`(i)
    returning for each `i` in the index set the image of the fundamental
    weight `\\Lambda_i` under the embedding.

    In order to be a proper root lattice realization, a weight lattice
    realization should also implement the scalar product with the coroot
    lattice; on the other hand, the embedding of the simple roots is
    given for free.

    .. SEEALSO::

        - :class:`~sage.combinat.root_system.root_system.RootSystem`
        - :class:`~sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations`
        - :class:`~sage.combinat.root_system.weight_space.WeightSpace`
        - :class:`~sage.combinat.root_system.ambient_space.AmbientSpace`

    EXAMPLES:

    Here, we consider the root system of type `A_7`, and embed the weight
    lattice element `x = \\Lambda_1 + 2 \\Lambda_3` in several root lattice
    realizations::

        sage: R = RootSystem(["A",7])
        sage: Lambda = R.weight_lattice().fundamental_weights()
        sage: x = Lambda[2] + 2 * Lambda[5]

        sage: L = R.weight_space()
        sage: L(x)
        Lambda[2] + 2*Lambda[5]

        sage: L = R.ambient_lattice()
        sage: L(x)
        (3, 3, 2, 2, 2, 0, 0, 0)

    We embed the weight space element `x = \\Lambda_1 + 1/2 \\Lambda_3` in
    the ambient space::

        sage: Lambda = R.weight_space().fundamental_weights()
        sage: x = Lambda[2] + 1/2 * Lambda[5]

        sage: L = R.ambient_space()
        sage: L(x)
        (3/2, 3/2, 1/2, 1/2, 1/2, 0, 0, 0)

    Of course, one can\'t embed the weight space in the ambient lattice::

        sage: L = R.ambient_lattice()
        sage: L(x)
        Traceback (most recent call last):
        ...
        TypeError: do not know how to make x (= Lambda[2] + 1/2*Lambda[5])
        an element of self (=Ambient lattice of the Root system of type [\'A\', 7])

    If `K_1` is a subring of `K_2`, then one could in theory have an
    embedding from the weight space over `K_1` to any weight lattice
    realization over `K_2`; this is not implemented::

        sage: K1 = QQ
        sage: K2 = QQ[\'q\']
        sage: L = R.ambient_space(K2)

        sage: Lambda = R.weight_space(K2).fundamental_weights()
        sage: L(Lambda[1])
        (1, 0, 0, 0, 0, 0, 0, 0)

        sage: Lambda = R.weight_space(K1).fundamental_weights()
        sage: L(Lambda[1])
        Traceback (most recent call last):
        ...
        TypeError: do not know how to make x (= Lambda[1]) an element
        of self (=Ambient space of the Root system of type [\'A\', 7])
    '''
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.combinat.root_system.weight_lattice_realizations import WeightLatticeRealizations
            sage: WeightLatticeRealizations(QQ).super_categories()
            [Category of root lattice realizations over Rational Field]
        """
    class ParentMethods:
        @abstract_method
        def fundamental_weight(self, i) -> None:
            '''
            Return the `i`-th fundamental weight.

            INPUT:

            - ``i`` -- an element of the index set

            By a slight notational abuse, for an affine type this method
            should also accept ``\'delta\'`` as input, and return the image
            of `\\delta` of the extended weight lattice in this
            realization.

            This should be overridden by any subclass, and typically
            be implemented as a cached method for efficiency.

            EXAMPLES::

                sage: L = RootSystem(["A",3]).ambient_lattice()
                sage: L.fundamental_weight(1)
                (1, 0, 0, 0)

                sage: L = RootSystem(["A",3,1]).weight_lattice(extended=True)
                sage: L.fundamental_weight(1)
                Lambda[1]
                sage: L.fundamental_weight("delta")
                delta

            TESTS::

                sage: super(sage.combinat.root_system.weight_space.WeightSpace, L).fundamental_weight(1)
                Traceback (most recent call last):
                ...
                NotImplementedError: <abstract method fundamental_weight at ...>
            '''
        def is_extended(self):
            '''
            Return whether this is a realization of the extended weight lattice.

            .. SEEALSO:: :class:`sage.combinat.root_system.weight_space.WeightSpace`

            EXAMPLES::

                sage: RootSystem(["A",3,1]).weight_lattice().is_extended()
                False
                sage: RootSystem(["A",3,1]).weight_lattice(extended=True).is_extended()
                True

            This method is irrelevant for finite root systems, since the
            weight lattice need not be extended to ensure that the root
            lattice embeds faithfully::

                sage: RootSystem(["A",3]).weight_lattice().is_extended()
                False
            '''
        def __init_extra__(self) -> None:
            '''
            Registers the embedding of the weight lattice into ``self``.

            Also registers the embedding of the weight space over the same
            base field `K` into ``self`` if `K` is not `\\ZZ`.

            If ``self`` is a realization of the extended weight lattice,
            then the embeddings from the extended weight space/lattices
            are registered instead.

            EXAMPLES:

            We embed the fundamental weight `\\Lambda_1` of the weight
            lattice in the ambient lattice::

                sage: R = RootSystem(["A",3])
                sage: Lambda = R.root_lattice().simple_roots()
                sage: L = R.ambient_space()
                sage: L(Lambda[2])
                (0, 1, -1, 0)

            .. NOTE::

                More examples are given in :class:`WeightLatticeRealizations`;
                The embeddings are systematically tested in
                :meth:`_test_weight_lattice_realization`.
            '''
        @cached_method
        def fundamental_weights(self):
            """
            Return the family `(\\Lambda_i)_{i\\in I}` of the fundamental weights.

            EXAMPLES::

                sage: e = RootSystem(['A',3]).ambient_lattice()
                sage: f = e.fundamental_weights()
                sage: [f[i] for i in [1,2,3]]
                [(1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0)]
            """
        @cached_method
        def simple_root(self, i):
            '''
            Return the `i`-th simple root.

            This default implementation takes the `i`-th simple root in
            the weight lattice and embeds it in ``self``.

            EXAMPLES:

            Since all the weight lattice realizations in Sage currently
            implement a ``simple_root`` method, we have to call this one by
            hand::

                sage: from sage.combinat.root_system.weight_lattice_realizations import WeightLatticeRealizations
                sage: simple_root = WeightLatticeRealizations(QQ).parent_class.simple_root.f
                sage: L = RootSystem("A3").ambient_space()
                sage: simple_root(L, 1)                                                 # needs sage.graphs
                (1, -1, 0, 0)
                sage: simple_root(L, 2)                                                 # needs sage.graphs
                (0, 1, -1, 0)
                sage: simple_root(L, 3)                                                 # needs sage.graphs
                (1, 1, 2, 0)

            Note that this last root differs from the one implemented in
            ``L`` by a multiple of the vector ``(1,1,1,1)``::

                sage: L.simple_roots()                                                  # needs sage.graphs
                Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1)}

            This is a harmless artefact of the `SL` versus `GL`
            interpretation of type `A`; see the thematic tutorial on Lie
            Methods and Related Combinatorics in Sage for details.
            '''
        @cached_method
        def rho(self):
            """
            EXAMPLES::

                sage: RootSystem(['A',3]).ambient_lattice().rho()
                (3, 2, 1, 0)
            """
        def reduced_word_of_alcove_morphism(self, f):
            '''
            Return the reduced word of an alcove morphism.

            INPUT:

            - ``f`` -- a linear map from ``self`` to ``self`` which
              preserves alcoves

            Let `A` be the fundamental alcove. This returns a reduced word
            `i_1, \\ldots, i_k` such that the affine Weyl group element `w =
            s_{i_1} \\circ \\cdots \\circ s_{i_k}` maps the alcove `f(A)` back
            to `A`. In other words, the alcove walk `i_1, \\ldots, i_k` brings
            the fundamental alcove to the corresponding translated alcove.

            Let us throw in a bit of context to explain the main use
            case.  It is customary to realize the alcove picture in
            the coroot or coweight lattice `R^\\vee`. The extended
            affine Weyl group is then the group of linear maps on
            `R^\\vee` which preserve the alcoves. By
            [Kac "Infinite-dimensional Lie algebra", Proposition 6.5]
            the affine Weyl group is the semidirect product of the
            associated finite Weyl group and the group of translations
            in the coroot lattice (the extended affine Weyl group uses
            the coweight lattice instead). In other words, an element
            of the extended affine Weyl group admits a unique
            decomposition of the form:

            .. MATH:: f = d w ,

            where `w` is in the Weyl group, and `d` is a function which
            maps the fundamental alcove to itself. As `d` permutes the
            walls of the fundamental alcove, it permutes accordingly the
            corresponding simple roots, which induces an automorphism of
            the Dynkin diagram.

            This method returns a reduced word for `w`, whereas the method
            :meth:`dynkin_diagram_automorphism_of_alcove_morphism` returns
            `d` as a permutation of the nodes of the Dynkin diagram.

            Nota bene: recall that the coroot (resp. coweight) lattice is
            implemented as the root (resp weight) lattice of the dual root
            system. Hence, this method is implemented for weight lattice
            realizations, but in practice is most of the time used on the
            dual side.

            EXAMPLES:

            We start with type `A` which is simply laced; hence we do not
            have to worry about the distinction between the weight and
            coweight lattice::

                sage: R = RootSystem(["A",2,1]).weight_lattice()
                sage: alpha = R.simple_roots()                                          # needs sage.graphs
                sage: Lambda = R.fundamental_weights()

            We consider first translations by elements of the root lattice::

                sage: R.reduced_word_of_alcove_morphism(alpha[0].translation)           # needs sage.graphs
                [1, 2, 1, 0]
                sage: R.reduced_word_of_alcove_morphism(alpha[1].translation)           # needs sage.graphs
                [0, 2, 0, 1]
                sage: R.reduced_word_of_alcove_morphism(alpha[2].translation)           # needs sage.graphs
                [0, 1, 0, 2]

            We continue with translations by elements of the classical
            weight lattice, embedded at level `0`:

                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - Lambda[0]

                sage: R.reduced_word_of_alcove_morphism(omega1.translation)             # needs sage.graphs
                [0, 2]
                sage: R.reduced_word_of_alcove_morphism(omega2.translation)             # needs sage.graphs
                [0, 1]

            The following tests ensure that the code agrees with the tables
            in Kashiwara\'s private notes on affine quantum algebras (2008).

            TESTS::

                sage: # needs sage.graphs
                sage: R = RootSystem([\'A\',5,1]).weight_lattice()
                sage: alpha = R.simple_roots()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = Lambda[1] - Lambda[0]
                sage: R.reduced_word_of_alcove_morphism(omega1.translation)
                [0, 5, 4, 3, 2]
                sage: R.reduced_word_of_alcove_morphism(alpha[0].translation)
                [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

                sage: # needs sage.graphs
                sage: R = RootSystem([\'C\',3,1]).weight_lattice()
                sage: alpha = R.simple_roots()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = 2*(Lambda[1] - Lambda[0])
                sage: omega2 = 2*(Lambda[2] - Lambda[0])
                sage: omega3 = Lambda[3] - Lambda[0]
                sage: R.reduced_word_of_alcove_morphism(omega1.translation)
                [0, 1, 2, 3, 2, 1]
                sage: R.reduced_word_of_alcove_morphism(omega2.translation)
                [0, 1, 0, 2, 1, 3, 2, 1, 3, 2]
                sage: R.reduced_word_of_alcove_morphism(omega3.translation)
                [0, 1, 0, 2, 1, 0]

                sage: # needs sage.libs.gap
                sage: W = WeylGroup([\'C\',3,1])
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[1]*s[2]*s[3]*s[2]
                sage: W.from_reduced_word(R.reduced_word_of_alcove_morphism(omega2.translation)) == w*w                 # needs sage.graphs
                True
                sage: w = s[0]*s[1]*s[2]*s[0]*s[1]*s[0]
                sage: W.from_reduced_word(R.reduced_word_of_alcove_morphism(omega3.translation)) == w                   # needs sage.graphs
                True

                sage: # needs sage.graphs
                sage: R = RootSystem([\'D\',4,1]).weight_lattice()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - 2*Lambda[0]
                sage: omega3 = Lambda[3] - Lambda[0]
                sage: omega4 = Lambda[4] - Lambda[0]
                sage: R.reduced_word_of_alcove_morphism(omega1.translation)
                [0, 2, 3, 4, 2, 0]
                sage: R.reduced_word_of_alcove_morphism(omega2.translation)
                [0, 2, 1, 3, 2, 4, 2, 1, 3, 2]
                sage: R.reduced_word_of_alcove_morphism(omega3.translation)
                [0, 2, 1, 4, 2, 0]
                sage: R.reduced_word_of_alcove_morphism(omega4.translation)
                [0, 2, 1, 3, 2, 0]

                sage: # needs sage.libs.gap
                sage: W = WeylGroup([\'D\',4,1])
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[2]*s[3]*s[4]*s[2]
                sage: w1= s[1]*s[2]*s[3]*s[4]*s[2]
                sage: W.from_reduced_word(R.reduced_word_of_alcove_morphism(omega2.translation)) == w*w1                # needs sage.graphs
                True

                sage: R = RootSystem([\'D\',5,1]).weight_lattice()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - 2*Lambda[0]
                sage: R.reduced_word_of_alcove_morphism(omega1.translation)             # needs sage.graphs
                [0, 2, 3, 4, 5, 3, 2, 0]

                sage: # needs sage.libs.gap
                sage: W = WeylGroup([\'D\',5,1])
                sage: s = W.simple_reflections()
                sage: w = s[0]*s[2]*s[3]*s[4]*s[5]*s[3]*s[2]
                sage: w1= s[1]*s[2]*s[3]*s[4]*s[5]*s[3]*s[2]
                sage: W.from_reduced_word(R.reduced_word_of_alcove_morphism(omega2.translation)) == w*w1                # needs sage.graphs
                True
            '''
        def dynkin_diagram_automorphism_of_alcove_morphism(self, f):
            '''
            Return the Dynkin diagram automorphism induced by an alcove morphism.

            INPUT:

            - ``f`` -- a linear map from ``self`` to ``self`` which preserves alcoves

            This method returns the Dynkin diagram automorphism for
            the decomposition `f = d w` (see
            :meth:`reduced_word_of_alcove_morphism`), as a dictionary
            mapping elements of the index set to itself.

            EXAMPLES::

                sage: R = RootSystem(["A",2,1]).weight_lattice()
                sage: alpha = R.simple_roots()                                          # needs sage.graphs
                sage: Lambda = R.fundamental_weights()

            Translations by elements of the root lattice induce a
            trivial Dynkin diagram automorphism::

                sage: # needs sage.graphs sage.libs.gap
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(alpha[0].translation)
                {0: 0, 1: 1, 2: 2}
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(alpha[1].translation)
                {0: 0, 1: 1, 2: 2}
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(alpha[2].translation)
                {0: 0, 1: 1, 2: 2}

            This is no more the case for translations by general
            elements of the (classical) weight lattice at level 0::

                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - Lambda[0]

                sage: # needs sage.graphs sage.libs.gap
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(omega1.translation)
                {0: 1, 1: 2, 2: 0}
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(omega2.translation)
                {0: 2, 1: 0, 2: 1}

                sage: # needs sage.graphs sage.libs.gap
                sage: R = RootSystem([\'C\',2,1]).weight_lattice()
                sage: alpha = R.simple_roots()
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(alpha[1].translation)
                {0: 2, 1: 1, 2: 0}

                sage: # needs sage.graphs sage.libs.gap
                sage: R = RootSystem([\'D\',5,1]).weight_lattice()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - 2*Lambda[0]
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(omega1.translation)
                {0: 1, 1: 0, 2: 2, 3: 3, 4: 5, 5: 4}
                sage: R.dynkin_diagram_automorphism_of_alcove_morphism(omega2.translation)
                {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

            Algorithm: computes `w` of the decomposition, and see how
            `f\\circ w^{-1}` permutes the simple roots.
            '''
        def reduced_word_of_translation(self, t):
            '''
            Given an element of the root lattice, this returns a reduced
            word `i_1, \\ldots, i_k` such that the Weyl group element `s_{i_1}
            \\circ \\cdots \\circ s_{i_k}` implements the "translation"
            where `x` maps to `x + level(x)*t`. In other words, the alcove walk
            `i_1, \\ldots, i_k` brings the fundamental alcove to the
            corresponding translated alcove.

            .. NOTE::

                There are some technical conditions for `t` to actually
                be a translation; those are not tested (TODO: detail).

            EXAMPLES::

                sage: # needs sage.graphs
                sage: R = RootSystem(["A",2,1]).weight_lattice()
                sage: alpha = R.simple_roots()
                sage: R.reduced_word_of_translation(alpha[1])
                [0, 2, 0, 1]
                sage: R.reduced_word_of_translation(alpha[2])
                [0, 1, 0, 2]
                sage: R.reduced_word_of_translation(alpha[0])
                [1, 2, 1, 0]

                sage: R = RootSystem([\'D\',5,1]).weight_lattice()
                sage: Lambda = R.fundamental_weights()
                sage: omega1 = Lambda[1] - Lambda[0]
                sage: omega2 = Lambda[2] - 2*Lambda[0]
                sage: R.reduced_word_of_translation(omega1)                             # needs sage.graphs
                [0, 2, 3, 4, 5, 3, 2, 0]
                sage: R.reduced_word_of_translation(omega2)                             # needs sage.graphs
                [0, 2, 1, 3, 2, 4, 3, 5, 3, 2, 1, 4, 3, 2]

            A non simply laced case::

                sage: R = RootSystem(["C",2,1]).weight_lattice()
                sage: Lambda = R.fundamental_weights()
                sage: c = R.cartan_type().translation_factors(); c                      # needs sage.graphs
                Finite family {0: 1, 1: 2, 2: 1}
                sage: R.reduced_word_of_translation((Lambda[1]-Lambda[0]) * c[1])       # needs sage.graphs
                [0, 1, 2, 1]
                sage: R.reduced_word_of_translation((Lambda[2]-Lambda[0]) * c[2])       # needs sage.graphs
                [0, 1, 0]

            See also :meth:`_test_reduced_word_of_translation`.

            .. TODO::

                 - Add a picture in the doc
                 - Add a method which, given an element of the classical
                   weight lattice, constructs the appropriate value for t
            '''
        def signs_of_alcovewalk(self, walk):
            """
            Let walk = `[i_1,\\ldots,i_n]` denote an alcove walk starting
            from the fundamental alcove `y_0`, crossing at step 1 the
            wall `i_1`, and so on.

            For each `k`, set `w_k = s_{i_1} \\circ s_{i_k}`, and denote
            by `y_k = w_k(y_0)` the alcove reached after `k` steps. Then,
            `y_k` is obtained recursively from `y_{k-1}` by applying the
            following reflection:

            .. MATH::

                  y_k = s_{w_{k-1} \\alpha_{i_k}} y_{k-1}.

            The step is said positive if `w_{k-1} \\alpha_{i_k}` is a
            negative root (considering `w_{k-1}` as element of the
            classical Weyl group and `\\alpha_{i_k}` as a classical
            root) and negative otherwise. The algorithm implemented
            here use the equivalent property::

                .. MATH:: \\langle w_{k-1}^{-1} \\rho_0, \\alpha^\\vee_{i_k}\\rangle > 0

            Where `\\rho_0` is the sum of the classical fundamental
            weights embedded at level 0 in this space (see
            :meth:`rho_classical`), and `\\alpha^\\vee_{i_k}` is the
            simple coroot associated to `\\alpha_{i_k}`.

            This function returns a list of the form `[+1,+1,-1,...]`,
            where the `k`-th entry denotes whether the `k`-th step was
            positive or negative.

            See equation 3.4, of Ram: Alcove walks ..., :arxiv:`math/0601343v1`

            EXAMPLES::

                sage: L = RootSystem(['C',2,1]).weight_lattice()
                sage: L.signs_of_alcovewalk([1,2,0,1,2,1,2,0,1,2])                      # needs sage.libs.gap
                [-1, -1, 1, -1, 1, 1, 1, 1, 1, 1]

                sage: L = RootSystem(['A',2,1]).weight_lattice()
                sage: L.signs_of_alcovewalk([0,1,2,1,2,0,1,2,0,1,2,0])                  # needs sage.libs.gap
                [1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

                sage: L = RootSystem(['B',2,1]).coweight_lattice()
                sage: L.signs_of_alcovewalk([0,1,2,0,1,2])                              # needs sage.libs.gap
                [1, -1, 1, -1, 1, 1]

            .. WARNING::

                This method currently does not work in the weight
                lattice for type BC dual because `\\rho_0` does not
                live in this lattice (but an integral multiple of it
                would do the job as well).
            """
        def rho_classical(self):
            '''
            Return the embedding at level 0 of `\\rho` of the classical lattice.

            EXAMPLES::

                sage: RootSystem([\'C\',4,1]).weight_lattice().rho_classical()            # needs sage.graphs
                -4*Lambda[0] + Lambda[1] + Lambda[2] + Lambda[3] + Lambda[4]
                sage: L = RootSystem([\'D\',4,1]).weight_lattice()
                sage: L.rho_classical().scalar(L.null_coroot())                         # needs sage.graphs
                0

            .. WARNING::

                In affine type BC dual, this does not live in the weight lattice::

                    sage: L = CartanType(["BC",2,2]).dual().root_system().weight_space()
                    sage: L.rho_classical()                                             # needs sage.graphs
                    -3/2*Lambda[0] + Lambda[1] + Lambda[2]
                    sage: L = CartanType(["BC",2,2]).dual().root_system().weight_lattice()
                    sage: L.rho_classical()                                             # needs sage.graphs
                    Traceback (most recent call last):
                    ...
                    ValueError: 5 is not divisible by 2
            '''
        def embed_at_level(self, x, level: int = 1):
            '''
            Embed the classical weight `x` in the level ``level`` hyperplane.

            This is achieved by translating the straightforward
            embedding of `x` by `c\\Lambda_0` for `c` some appropriate
            scalar.

            INPUT:

            - ``x`` -- an element of the corresponding classical weight/ambient lattice
            - ``level`` -- integer or element of the base ring (default: 1)

            EXAMPLES::

                sage: # needs sage.graphs
                sage: L = RootSystem(["B",3,1]).weight_space()
                sage: L0 = L.classical()
                sage: alpha = L0.simple_roots()
                sage: omega = L0.fundamental_weights()
                sage: L.embed_at_level(omega[1], 1)
                Lambda[1]
                sage: L.embed_at_level(omega[2], 1)
                -Lambda[0] + Lambda[2]
                sage: L.embed_at_level(omega[3], 1)
                Lambda[3]
                sage: L.embed_at_level(alpha[1], 1)
                Lambda[0] + 2*Lambda[1] - Lambda[2]
            '''
        def weyl_dimension(self, highest_weight):
            """
            Return the dimension of the highest weight representation of highest weight ``highest_weight``.

            EXAMPLES::

                sage: RootSystem(['A',3]).ambient_lattice().weyl_dimension([2,1,0,0])
                20
                sage: P = RootSystem(['C',2]).weight_lattice()
                sage: La = P.basis()
                sage: P.weyl_dimension(La[1]+La[2])                                     # needs sage.graphs
                16

                sage: type(RootSystem(['A',3]).ambient_lattice().weyl_dimension([2,1,0,0]))
                <class 'sage.rings.integer.Integer'>
            """
    class ElementMethods:
        def symmetric_form(self, la):
            """
            Return the symmetric form of ``self`` with ``la``.

            Return the pairing `( | )` on the weight lattice. See Chapter 6
            in Kac, Infinite Dimensional Lie Algebras for more details.

            .. WARNING::

                For affine root systems, if you are not working in the
                extended weight lattice/space, this may return incorrect
                results.

            EXAMPLES::

                sage: # needs sage.graphs
                sage: P = RootSystem(['C',2]).weight_lattice()
                sage: al = P.simple_roots()
                sage: al[1].symmetric_form(al[1])
                2
                sage: al[1].symmetric_form(al[2])
                -2
                sage: al[2].symmetric_form(al[1])
                -2
                sage: Q = RootSystem(['C',2]).root_lattice()
                sage: alQ = Q.simple_roots()
                sage: all(al[i].symmetric_form(al[j]) == alQ[i].symmetric_form(alQ[j])
                ....:     for i in P.index_set() for j in P.index_set())
                True

                sage: # needs sage.graphs
                sage: P = RootSystem(['C',2,1]).weight_lattice(extended=True)
                sage: al = P.simple_roots()
                sage: al[1].symmetric_form(al[1])
                2
                sage: al[1].symmetric_form(al[2])
                -2
                sage: al[1].symmetric_form(al[0])
                -2
                sage: al[0].symmetric_form(al[1])
                -2
                sage: Q = RootSystem(['C',2,1]).root_lattice()
                sage: alQ = Q.simple_roots()
                sage: all(al[i].symmetric_form(al[j]) == alQ[i].symmetric_form(alQ[j])
                ....:     for i in P.index_set() for j in P.index_set())
                True
                sage: La = P.basis()
                sage: [La['delta'].symmetric_form(al) for al in P.simple_roots()]
                [0, 0, 0]
                sage: [La[0].symmetric_form(al) for al in P.simple_roots()]
                [1, 0, 0]

                sage: P = RootSystem(['C',2,1]).weight_lattice()
                sage: Q = RootSystem(['C',2,1]).root_lattice()
                sage: al = P.simple_roots()                                             # needs sage.graphs
                sage: alQ = Q.simple_roots()                                            # needs sage.graphs
                sage: all(al[i].symmetric_form(al[j]) == alQ[i].symmetric_form(alQ[j])  # needs sage.graphs
                ....:     for i in P.index_set() for j in P.index_set())
                True

            The result of `(\\Lambda_0 | \\alpha_0)` should be `1`, however we
            get `0` because we are not working in the extended weight
            lattice::

                sage: La = P.basis()
                sage: [La[0].symmetric_form(al) for al in P.simple_roots()]             # needs sage.graphs
                [0, 0, 0]

            TESTS:

            We check that `A_{2n}^{(2)}` has 3 different root lengths::

                sage: P = RootSystem(['A',4,2]).weight_lattice()
                sage: al = P.simple_roots()                                             # needs sage.graphs
                sage: [al[i].symmetric_form(al[i]) for i in P.index_set()]              # needs sage.graphs
                [2, 4, 8]

            Check that :issue:`31410` is fixed, and the symmetric form
            computed on the weight space is the same as the symmetric
            form computed on the root space::

                sage: def s1(ct):
                ....:    L = RootSystem(ct).weight_space()
                ....:    P = L.positive_roots()
                ....:    rho = L.rho()
                ....:    return [beta.symmetric_form(rho) for beta in P]

                sage: def s2(ct):
                ....:    R = RootSystem(ct).root_space()
                ....:    P = R.positive_roots()
                ....:    rho = 1/2*sum(P)
                ....:    return [beta.symmetric_form(rho) for beta in P]

                sage: all(s1(ct) == s2(ct)                                              # needs sage.graphs
                ....:     for ct in CartanType.samples(finite=True, crystallographic=True))
                True
            """
        def to_weight_space(self, base_ring=None):
            """
            Map ``self`` to the weight space.

            .. WARNING::

                Implemented for finite Cartan type.

            EXAMPLES::

                sage: b = CartanType(['B',2]).root_system().ambient_space().from_vector(vector([1,-2])); b
                (1, -2)
                sage: b.to_weight_space()
                3*Lambda[1] - 4*Lambda[2]
                sage: b = CartanType(['B',2]).root_system().ambient_space().from_vector(vector([1/2,0])); b
                (1/2, 0)
                sage: b.to_weight_space()
                1/2*Lambda[1]
                sage: b.to_weight_space(ZZ)
                Traceback (most recent call last):
                ...
                TypeError: no conversion of this rational to integer
                sage: b = CartanType(['G',2]).root_system().ambient_space().from_vector(vector([4,-5,1])); b
                (4, -5, 1)
                sage: b.to_weight_space()
                -6*Lambda[1] + 5*Lambda[2]
            """
