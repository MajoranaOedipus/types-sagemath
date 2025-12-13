from sage.categories.simplicial_complexes import SimplicialComplexes as SimplicialComplexes
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import Element as Element
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.topology.simplicial_complex import Simplex as Simplex, SimplicialComplex as SimplicialComplex

class SubwordComplexFacet(Simplex, Element):
    """
    A facet of a subword complex.

    Facets of the subword complex `\\mathcal{SC}(Q,w)` are complements
    of sets of positions in `Q` defining a reduced expression for `w`.

    EXAMPLES::

        sage: # optional - gap3
        sage: W = ReflectionGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC = SubwordComplex([1,2,1,2,1], w)
        sage: F = SC[0]; F
        (0, 1)

        sage: W = CoxeterGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC = SubwordComplex([1,2,1,2,1], w)
        sage: F = SC[0]; F
        (0, 1)

    TESTS::

        sage: type(F)                                                   # optional - gap3
        <class 'sage.combinat.subword_complex.SubwordComplex_with_category.element_class'>
    """
    def __init__(self, parent, positions, facet_test: bool = True) -> None:
        """
        Initialize a facet of the subword complex ``parent``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: F = SC([1,2]); F                                      # optional - gap3
            (1, 2)

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: F = SC([1,2]); F
            (1, 2)

        TESTS::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC([1,3])                                             # optional - gap3
            Traceback (most recent call last):
            ...
            ValueError: the given iterable [1, 3] is not a facet of the Subword complex of type ['A', 2] for Q = (1, 2, 1, 2, 1) and pi = [1, 2, 1]

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: TestSuite(SC).run()                                   # optional - gap3
        """
    def extended_root_configuration(self):
        """
        Return the extended root configuration of ``self``.

        Let `Q = q_1 \\dots q_m \\in S^*` and `w \\in W`. The extended
        root configuration of a facet `I` of `\\mathcal{SC}(Q,w)` is
        the sequence `\\mathsf{r}(I, 1), \\dots, \\mathsf{r}(I, m)` of
        roots defined by `\\mathsf{r}(I, k) = \\Pi Q_{[k-1]
        \\smallsetminus I} (\\alpha_{q_k})`, where `\\Pi Q_{[k-1]
        \\smallsetminus I}` is the product of the simple reflections
        `q_i` for `i \\in [k-1] \\smallsetminus I` in this order.

        The extended root configuration is used to perform flips efficiently.

        .. SEEALSO::

            :meth:`flip`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.extended_root_configuration()
            [(1, 0), (1, 1), (-1, 0), (1, 1), (0, 1)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.extended_root_configuration()
            [(1, 0), (1, 1), (-1, 0), (1, 1), (0, 1)]
        """
    def root_configuration(self):
        """
        Return the root configuration of ``self``.

        Let `Q = q_1 \\dots q_m \\in S^*` and `w \\in W`. The root
        configuration of a facet `I = [i_1, \\dots, i_n]` of
        `\\mathcal{SC}(Q,w)` is the sequence `\\mathsf{r}(I, i_1),
        \\dots, \\mathsf{r}(I, i_n)` of roots defined by `\\mathsf{r}(I,
        k) = \\Pi Q_{[k-1] \\smallsetminus I} (\\alpha_{q_k})`, where
        `\\Pi Q_{[k-1] \\smallsetminus I}` is the product of the simple
        reflections `q_i` for `i \\in [k-1] \\smallsetminus I` in this
        order.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.root_configuration()
            [(1, 1), (-1, 0)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.root_configuration()                                # optional - gap3
            [(1, 1), (-1, 0)]
        """
    def kappa_preimage(self):
        """
        Return the fiber of ``self`` under the `\\kappa` map.

        The `\\kappa` map sends an element `w \\in W` to the unique
        facet of `I \\in \\mathcal{SC}(Q,w)` such that the root
        configuration of `I` is contained in `w(\\Phi^+)`.
        In other words, `w` is in the preimage of ``self`` under
        `\\kappa` if and only if `w^{-1}` sends every root in the
        root configuration to a positive root.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: w = W.from_reduced_word([1,2,1])                      # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1],w)                    # optional - gap3

            sage: F = SC([1,2]); F                                      # optional - gap3
            (1, 2)
            sage: F.kappa_preimage()                                    # optional - gap3
            [(1,4)(2,3)(5,6)]

            sage: F = SC([0,4]); F                                      # optional - gap3
            (0, 4)
            sage: F.kappa_preimage()                                    # optional - gap3
            [(1,3)(2,5)(4,6), (1,2,6)(3,4,5)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)

            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.kappa_preimage()
            [
            [-1  1]
            [ 0  1]
            ]

            sage: F = SC([0,4]); F
            (0, 4)
            sage: F.kappa_preimage()
            [
            [ 1  0]  [-1  1]
            [ 1 -1], [-1  0]
            ]
        """
    def is_vertex(self):
        """
        Return ``True`` if ``self`` is a vertex of the brick polytope
        of ``self.parent``.

        A facet is a vertex of the brick polytope if its root cone is
        pointed. Note that this property is always satisfied for
        root-independent subword complexes.

        .. SEEALSO::

            :meth:`root_cone`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',1])
            sage: w = W.from_reduced_word([1])
            sage: SC = SubwordComplex([1,1,1],w)
            sage: F = SC([0,1]); F.is_vertex()
            True
            sage: F = SC([0,2]); F.is_vertex()
            False

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1,2,1],w)
            sage: F = SC([0,1,2,3]); F.is_vertex()
            True
            sage: F = SC([0,1,2,6]); F.is_vertex()
            False

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1,2,1],w)
            sage: F = SC([0,1,2,3]); F.is_vertex()
            True
            sage: F = SC([0,1,2,6]); F.is_vertex()
            False
        """
    @cached_method
    def root_cone(self):
        """
        Return the polyhedral cone generated by the root configuration
        of ``self``.

        .. SEEALSO::

            :meth:`root_configuration`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',1])
            sage: w = W.from_reduced_word([1])
            sage: SC = SubwordComplex([1,1,1],w)
            sage: F = SC([0,2]); F.root_cone()
            1-d cone in 1-d lattice N

            sage: W = CoxeterGroup(['A',1])
            sage: w = W.from_reduced_word([1])
            sage: SC = SubwordComplex([1,1,1],w)
            sage: F = SC([0,2]); F.root_cone()
            1-d cone in 1-d lattice N
        """
    def upper_root_configuration(self):
        """
        Return the positive roots of the root configuration of ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.root_configuration()
            [(1, 1), (-1, 0)]
            sage: F.upper_root_configuration()
            [(1, 0)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.upper_root_configuration()
            [(1, 0)]
        """
    def extended_weight_configuration(self, coefficients=None):
        """
        Return the extended weight configuration of ``self``.

        Let `Q = q_1 \\dots q_m \\in S^*` and `w \\in W`. The extended
        weight configuration of a facet `I` of `\\mathcal{SC}(Q,w)` is
        the sequence `\\mathsf{w}(I, 1), \\dots, \\mathsf{w}(I, m)` of
        weights defined by `\\mathsf{w}(I, k) = \\Pi Q_{[k-1]
        \\smallsetminus I} (\\omega_{q_k})`, where `\\Pi Q_{[k-1]
        \\smallsetminus I}` is the product of the simple reflections
        `q_i` for `i \\in [k-1] \\smallsetminus I` in this order.

        The extended weight configuration is used to compute the brick vector.

        INPUT:

        - ``coefficients`` -- (optional) a list of coefficients used to
          scale the fundamental weights

        .. SEEALSO::

            :meth:`brick_vector`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2])
            sage: F.extended_weight_configuration()
            [(2/3, 1/3), (1/3, 2/3), (-1/3, 1/3), (1/3, 2/3), (-1/3, 1/3)]
            sage: F.extended_weight_configuration(coefficients=(1,2))
            [(2/3, 1/3), (2/3, 4/3), (-1/3, 1/3), (2/3, 4/3), (-1/3, 1/3)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2])
            sage: F.extended_weight_configuration()
            [(4/3, 2/3), (2/3, 4/3), (-2/3, 2/3), (2/3, 4/3), (-2/3, 2/3)]
            sage: F.extended_weight_configuration(coefficients=(1,2))
            [(4/3, 2/3), (4/3, 8/3), (-2/3, 2/3), (4/3, 8/3), (-2/3, 2/3)]
        """
    def weight_configuration(self):
        """
        Return the weight configuration of ``self``.

        Let `Q = q_1 \\dots q_m \\in S^*` and `w \\in W`. The weight
        configuration of a facet `I = [i_1, \\dots, i_n]` of
        `\\mathcal{SC}(Q,w)` is the sequence `\\mathsf{w}(I, i_1),
        \\dots, \\mathsf{w}(I, i_n)` of weights defined by
        `\\mathsf{w}(I, k) = \\Pi Q_{[k-1] \\smallsetminus I}
        (\\omega_{q_k})`, where `\\Pi Q_{[k-1] \\smallsetminus I}` is the
        product of the simple reflections `q_i` for `i \\in [k-1]
        \\smallsetminus I` in this order.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.weight_configuration()
            [(1/3, 2/3), (-1/3, 1/3)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.weight_configuration()
            [(2/3, 4/3), (-2/3, 2/3)]
        """
    @cached_method
    def weight_cone(self):
        """
        Return the polyhedral cone generated by the weight
        configuration of ``self``.

        .. SEEALSO::

            :meth:`weight_configuration`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: WC = F.weight_cone(); WC
            2-d cone in 2-d lattice N
            sage: WC.rays()
            N( 1, 2),
            N(-1, 1)
            in 2-d lattice N

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: WC = F.weight_cone(); WC
            2-d cone in 2-d lattice N
        """
    def brick_vector(self, coefficients=None):
        """
        Return the brick vector of ``self``.

        This is the sum of the weight vectors in the extended weight
        configuration.

        INPUT:

        - ``coefficients`` -- (optional) a list of coefficients used to
          scale the fundamental weights

        .. SEEALSO::

            :meth:`extended_weight_configuration`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.extended_weight_configuration()
            [(2/3, 1/3), (1/3, 2/3), (-1/3, 1/3), (1/3, 2/3), (-1/3, 1/3)]
            sage: F.brick_vector()
            (2/3, 7/3)
            sage: F.brick_vector(coefficients=[1,2])
            (4/3, 11/3)

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2])
            sage: F.brick_vector()
            (4/3, 14/3)
            sage: F.brick_vector(coefficients=[1,2])
            (8/3, 22/3)
        """
    def flip(self, i, return_position: bool = False):
        """
        Return the facet obtained after flipping position ``i`` in ``self``.

        INPUT:

        - ``i`` -- integer; position in the word `Q`
        - ``return_position`` -- boolean (default: ``False``); tells
          whether the new position should be returned as well

        OUTPUT:

        - The new subword complex facet.
        - The new position if ``return_position`` is ``True``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.flip(1)
            (2, 3)
            sage: F.flip(1, return_position=True)
            ((2, 3), 3)

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F
            (1, 2)
            sage: F.flip(1)
            (2, 3)
            sage: F.flip(1, return_position=True)
            ((2, 3), 3)
        """
    def plot(self, list_colors=None, labels=[], thickness: int = 3, fontsize: int = 14, shift=(0, 0), compact: bool = False, roots: bool = True, **args):
        """
        In type `A` or `B`, plot a pseudoline arrangement representing
        the facet ``self``.

        Pseudoline arrangements are graphical representations of
        facets of types A or B subword complexes.

        INPUT:

        - ``list_colors`` -- list (default: ``[]``); to change the colors
          of the pseudolines
        - ``labels`` -- list (default: ``[]``); to change the labels
          of the pseudolines
        - ``thickness`` -- integer (default: 3); for the thickness
          of the pseudolines
        - ``fontsize`` -- integer (default: 14); for the size
          of the font used for labels
        - ``shift`` -- couple of coordinates (default: ``(0,0)``)
          to change the origin
        - ``compact`` -- boolean (default: ``False``); to require
          a more compact representation
        - ``roots`` -- boolean (default: ``True``); whether to print
          the extended root configuration

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F.plot()                                               # needs sage.plot
            Graphics object consisting of 26 graphics primitives

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F.plot()                                               # needs sage.plot
            Graphics object consisting of 26 graphics primitives

            sage: # optional - gap3
            sage: W = ReflectionGroup(['B',3])
            sage: c = W.from_reduced_word([1,2,3])
            sage: Q = c.reduced_word()*2 + W.w0.coxeter_sorting_word(c)
            sage: SC = SubwordComplex(Q, W.w0)
            sage: F = SC[15]; F.plot()                                                  # needs sage.plot
            Graphics object consisting of 53 graphics primitives

        TESTS::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['D',4])
            sage: c = W.from_reduced_word([1,2,3,4])
            sage: Q = c.reduced_word() + W.w0.coxeter_sorting_word(c)
            sage: SC = SubwordComplex(Q, W.w0)
            sage: F = SC[1]; F.plot()                                                   # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: plotting is currently only implemented for irreducibles types A, B, and C.

            sage: W = CoxeterGroup(CoxeterMatrix((['A',2],['A',2])))
            sage: c = W.from_reduced_word([1,2,3,4])
            sage: Q = c.reduced_word() + W.w0.coxeter_sorting_word(c)
            sage: SC = SubwordComplex(Q, W.w0)
            sage: F = SC[1]; F.plot()                                                   # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: plotting is currently only implemented for irreducibles types A, B, and C.

        REFERENCES: [PilStu]_
        """
    def show(self, *kwds, **args):
        """
        Show the facet ``self``.

        .. SEEALSO::

            :meth:`plot`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1],w)
            sage: F = SC([1,2]); F.show()
            <BLANKLINE>
        """

class SubwordComplex(UniqueRepresentation, SimplicialComplex):
    """
    Fix a Coxeter system `(W,S)`. The subword complex
    `\\mathcal{SC}(Q,w)` associated to a word `Q \\in S^*` and an
    element `w \\in W` is the simplicial complex whose ground set is the set of
    positions in `Q` and whose facets are complements of sets of
    positions defining a reduced expression for `w`.

    A subword complex is a shellable sphere if and only if the
    Demazure product of `Q` equals `w`, otherwise it is a shellable
    ball.

    .. WARNING::

        This implementation only works for groups build using ``CoxeterGroup``,
        and does not work with groups build using ``WeylGroup``.

    EXAMPLES:

    As an example, dual associahedra are subword complexes in type
    `A_{n-1}` given by the word `[1, \\dots, n, 1, \\dots, n, 1, \\dots,
    n-1, \\dots, 1, 2, 1]` and the permutation `w_0`.

    ::

        sage: # optional - gap3
        sage: W = ReflectionGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC = SubwordComplex([1,2,1,2,1], w); SC
        Subword complex of type ['A', 2] for Q = (1, 2, 1, 2, 1) and pi = [1, 2, 1]
        sage: SC.facets()
        [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

        sage: W = CoxeterGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC = SubwordComplex([1,2,1,2,1], w); SC
        Subword complex of type ['A', 2] for Q = (1, 2, 1, 2, 1) and pi = [1, 2, 1]
        sage: SC.facets()
        [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

    REFERENCES: [KnuMil]_, [PilStu]_

    TESTS::

        sage: # optional - gap3
        sage: W = ReflectionGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC1 = SubwordComplex([1,2,1,2,1], w)
        sage: SC2 = SubwordComplex([1,2,1,2,1], w)
        sage: SC1 == SC2
        True

        sage: W = CoxeterGroup(['A',2])
        sage: w = W.from_reduced_word([1,2,1])
        sage: SC1 = SubwordComplex([1,2,1,2,1], w)
        sage: SC2 = SubwordComplex([1,2,1,2,1], w)
        sage: SC1 == SC2
        True
    """
    @staticmethod
    def __classcall__(cls, Q, w, algorithm: str = 'inductive'):
        """
        Making the input hashable.

        TESTS::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['B',2])
            sage: S = SubwordComplex((1,2)*3,W.w0)
            sage: T = SubwordComplex([1,2]*3,W.w0)
            sage: S is T
            True

            sage: W = CoxeterGroup(['B',2])
            sage: S = SubwordComplex((1,2)*3,W.w0)
            sage: T = SubwordComplex([1,2]*3,W.w0)
            sage: S is T
            True
        """
    def __init__(self, Q, w, algorithm: str = 'inductive') -> None:
        """
        Initialize the subword complex `\\mathcal{SC}(Q,w)`.

        INPUT:

        - ``Q`` -- word on the simple generators of the Coxeter group
        - ``w`` -- element of the Coxeter group
        - ``algorithm`` -- (default: ``'inductive'``) choice of the
          algorithm to generate the subword complex. Options are
          ``'inductive'`` or ``'greedy'``. The second option is
          recommended when `|Q|` is closed to `\\ell(w) + \\mathrm{rank}(W)`.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.from_reduced_word([1,2,3,1,2,1])
            sage: SC = SubwordComplex([1,2,3,1,2,3,1,2,1], w); SC
            Subword complex of type ['A', 3] for Q = (1, 2, 3, 1, 2, 3, 1, 2, 1) and pi = [1, 2, 1, 3, 2, 1]
            sage: len(SC)
            14

            sage: W = CoxeterGroup(['A',3])
            sage: w = W.from_reduced_word([1,2,3,1,2,1])
            sage: SC = SubwordComplex([1,2,3,1,2,3,1,2,1], w); SC
            Subword complex of type ['A', 3] for Q = (1, 2, 3, 1, 2, 3, 1, 2, 1) and pi = [1, 2, 3, 1, 2, 1]
            sage: len(SC)
            14

        TESTS:

        Check for methods from the enumerated sets category::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: list(SC)
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: list(SC)
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,1,1])
            sage: SC = SubwordComplex([1,2,2,2,1], w)
            sage: len(SC)
            2
        """
    def __call__(self, F, facet_test: bool = True):
        """
        Create a facet of ``self``.

        INPUT:

        - ``F`` -- an iterable of positions
        - ``facet_test`` -- boolean (default: ``True``); whether or
          not the facet ``F`` should be tested before creation

        OUTPUT: the facet of ``self`` at positions given by ``F``

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: F = SC([1,2]); F                                      # optional - gap3
            (1, 2)

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: F = SC([1,2]); F
            (1, 2)
        """
    Element = SubwordComplexFacet
    def __contains__(self, F) -> bool:
        """
        Test if ``self`` contains a given iterable ``F``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w  = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.facets()
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
            sage: [0,1] in SC
            True
            sage: [0,2] in SC
            False
            sage: [0,1,5] in SC
            False
            sage: [0] in SC
            False
            sage: ['a','b'] in SC
            False

            sage: W = CoxeterGroup(['A',2])
            sage: w  = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.facets()
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
            sage: [0,1] in SC
            True
            sage: [0,2] in SC
            False
            sage: [0,1,5] in SC
            False
            sage: [0] in SC
            False
            sage: ['a','b'] in SC
            False
        """
    def group(self):
        """
        Return the group associated to ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.group()
            Irreducible real reflection group of rank 2 and type A2

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.group()
            Finite Coxeter group over Integer Ring with Coxeter matrix:
            [1 3]
            [3 1]
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.cartan_type()
            ['A', 2]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.cartan_type()
            ['A', 2]
        """
    def word(self):
        """
        Return the word in the simple generators associated to ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.word()
            (1, 2, 1, 2, 1)

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.word()
            (1, 2, 1, 2, 1)
        """
    def pi(self):
        """
        Return the element in the Coxeter group associated to ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.pi().reduced_word()
            [1, 2, 1]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.pi().reduced_word()
            [1, 2, 1]
        """
    def facets(self):
        """
        Return all facets of ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.facets()
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.facets()
            [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
        """
    def __iter__(self):
        """
        Return an iterator on the facets of ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: for I in SC: print(I)
            (0, 1)
            (0, 4)
            (1, 2)
            (2, 3)
            (3, 4)

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: for I in SC: print(I)
            (0, 1)
            (0, 4)
            (1, 2)
            (2, 3)
            (3, 4)
        """
    def greedy_facet(self, side: str = 'positive'):
        """
        Return the negative (or positive) greedy facet of ``self``.

        This is the lexicographically last (or first) facet of ``self``.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.greedy_facet(side='positive')
            (0, 1)
            sage: SC.greedy_facet(side='negative')
            (3, 4)

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.greedy_facet(side='positive')
            (0, 1)
            sage: SC.greedy_facet(side='negative')
            (3, 4)
        """
    def is_sphere(self):
        """
        Return ``True`` if the subword complex ``self`` is a sphere.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_sphere()
            True

            sage: SC = SubwordComplex([3,2,1,3,2,3], w)                 # optional - gap3
            sage: SC.is_sphere()                                        # optional - gap3
            False

            sage: W = CoxeterGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_sphere()
            True
        """
    def is_ball(self):
        """
        Return ``True`` if the subword complex ``self`` is a ball.

        This is the case if and only if it is not a sphere.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_ball()
            False

            sage: SC = SubwordComplex([3,2,1,3,2,3], w)                 # optional - gap3
            sage: SC.is_ball()                                          # optional - gap3
            True

            sage: W = CoxeterGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_ball()
            False
        """
    def is_pure(self):
        """
        Return ``True`` since all subword complexes are pure.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_pure()
            True

            sage: W = CoxeterGroup(['A',3])
            sage: w = W.from_reduced_word([2,3,2])
            sage: SC = SubwordComplex([3,2,3,2,3], w)
            sage: SC.is_pure()
            True
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.dimension()                                        # optional - gap3
            1

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.dimension()
            1
        """
    @cached_method
    def is_root_independent(self):
        """
        Return ``True`` if ``self`` is root-independent.

        This means that the root configuration
        of any (or equivalently all) facets is linearly independent.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.is_root_independent()                              # optional - gap3
            True

            sage: SC = SubwordComplex([1,2,1,2,1,2], W.w0)              # optional - gap3
            sage: SC.is_root_independent()                              # optional - gap3
            False

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.is_root_independent()
            True
        """
    @cached_method
    def is_double_root_free(self):
        """
        Return ``True`` if ``self`` is double-root-free.

        This means that the root configurations
        of all facets do not contain a root twice.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.is_double_root_free()
            True

            sage: SC = SubwordComplex([1,1,2,2,1,1], w)                 # optional - gap3
            sage: SC.is_double_root_free()                              # optional - gap3
            True

            sage: SC = SubwordComplex([1,2,1,2,1,2], w)                 # optional - gap3
            sage: SC.is_double_root_free()                              # optional - gap3
            False

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.is_double_root_free()
            True
        """
    def kappa_preimages(self):
        '''
        Return a dictionary containing facets of ``self`` as keys,
        and list of elements of ``self.group()`` as values.

        .. SEEALSO::

            :meth:`kappa_preimage <sage.combinat.subword_complex.SubwordComplexFacet.kappa_preimage>`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup([\'A\',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: kappa = SC.kappa_preimages()
            sage: for F in SC: print("{} {}".format(F, [w.reduced_word() for w in kappa[F]]))
            (0, 1) [[]]
            (0, 4) [[2], [2, 1]]
            (1, 2) [[1]]
            (2, 3) [[1, 2]]
            (3, 4) [[1, 2, 1]]

            sage: W = CoxeterGroup([\'A\',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: kappa = SC.kappa_preimages()
            sage: for F in SC: print("{} {}".format(F, [w.reduced_word() for w in kappa[F]]))
            (0, 1) [[]]
            (0, 4) [[2], [2, 1]]
            (1, 2) [[1]]
            (2, 3) [[1, 2]]
            (3, 4) [[1, 2, 1]]
        '''
    def brick_fan(self):
        """
        Return the brick fan of ``self``.

        It is the normal fan of the brick polytope of ``self``. It is
        formed by the cones generated by the weight configurations of
        the facets of ``self``.

        .. SEEALSO::

            :func:`weight_cone <sage.combinat.subword_complex.SubwordComplexFacet.weight_cone>`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.brick_fan()
            Rational polyhedral fan in 2-d lattice N

            sage: W = CoxeterGroup(['A',2])
            sage: w = W.from_reduced_word([1,2,1])
            sage: SC = SubwordComplex([1,2,1,2,1], w)
            sage: SC.brick_fan()
            Rational polyhedral fan in 2-d lattice N
        """
    def brick_vectors(self, coefficients=None):
        """
        Return the list of all brick vectors of facets of ``self``.

        INPUT:

        - ``coefficients`` -- (optional) a list of coefficients used to
          scale the fundamental weights

        .. SEEALSO::

            :func:`brick_vector <sage.combinat.subword_complex.SubwordComplexFacet.brick_vector>`

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.brick_vectors()
            [(5/3, 7/3), (5/3, 1/3), (2/3, 7/3), (-1/3, 4/3), (-1/3, 1/3)]
            sage: SC.brick_vectors(coefficients=(1,2))
            [(7/3, 11/3), (7/3, 2/3), (4/3, 11/3), (-2/3, 5/3), (-2/3, 2/3)]

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.brick_vectors()
            [(10/3, 14/3), (10/3, 2/3), (4/3, 14/3), (-2/3, 8/3), (-2/3, 2/3)]
            sage: SC.brick_vectors(coefficients=(1,2))
            [(14/3, 22/3), (14/3, 4/3), (8/3, 22/3), (-4/3, 10/3), (-4/3, 4/3)]
        """
    def minkowski_summand(self, i):
        """
        Return the `i` th Minkowski summand of ``self``.

        INPUT:

        - ``i`` -- an integer defining a position in the word `Q`

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.minkowski_summand(1)                               # optional - gap3
            A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.minkowski_summand(1)
            A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex
        """
    def brick_polytope(self, coefficients=None):
        """
        Return the brick polytope of ``self``.

        This polytope is the convex hull of the brick vectors of ``self``.

        INPUT:

        - ``coefficients`` -- (optional) a list of coefficients used to
          scale the fundamental weights

        .. SEEALSO::

            :meth:`brick_vectors`

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: X = SC.brick_polytope(); X                            # optional - gap3
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices

            sage: Y = SC.brick_polytope(coefficients=[1,2]); Y          # optional - gap3
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices

            sage: X == Y                                                # optional - gap3
            False

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: X = SC.brick_polytope(); X
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices

            sage: # optional - gap3
            sage: W = ReflectionGroup(['H',3])
            sage: c = W.index_set(); Q = c + tuple(W.w0.coxeter_sorting_word(c))
            sage: SC = SubwordComplex(Q,W.w0)
            sage: SC.brick_polytope()
            doctest:...:
            RuntimeWarning: the polytope is built with rational vertices
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 32 vertices
        """
    def barycenter(self):
        """
        Return the barycenter of the brick polytope of ``self``.

        .. SEEALSO::

            :meth:`brick_polytope`

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.barycenter()                                       # optional - gap3
            (2/3, 4/3)

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.barycenter()
            (4/3, 8/3)
        """
    def cover_relations(self, label: bool = False):
        """
        Return the set of cover relations in the associated poset.

        INPUT:

        - ``label`` -- boolean (default: ``False``); whether or not to label
          the cover relations by the position of flip

        OUTPUT: list of pairs of facets

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: sorted(SC.cover_relations())                          # optional - gap3
            [((0, 1), (0, 4)),
             ((0, 1), (1, 2)),
             ((0, 4), (3, 4)),
             ((1, 2), (2, 3)),
             ((2, 3), (3, 4))]

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: sorted(SC.cover_relations())
            [((0, 1), (0, 4)),
             ((0, 1), (1, 2)),
             ((0, 4), (3, 4)),
             ((1, 2), (2, 3)),
             ((2, 3), (3, 4))]
        """
    def increasing_flip_graph(self, label: bool = True):
        """
        Return the increasing flip graph of the subword complex.

        OUTPUT: a directed graph

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.increasing_flip_graph()                            # optional - gap3
            Digraph on 5 vertices

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.increasing_flip_graph()
            Digraph on 5 vertices
        """
    def interval(self, I, J) -> set:
        """
        Return the interval [I,J] in the increasing flip graph subword complex.

        INPUT:

        - I, J -- two facets

        OUTPUT: a set of facets

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: F = SC([1,2])
            sage: SC.interval(F, F)
            {(1, 2)}

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: F = SC([1,2])
            sage: SC.interval(F, F)
            {(1, 2)}
        """
    def increasing_flip_poset(self):
        """
        Return the increasing flip poset of the subword complex.

        OUTPUT: a poset

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])                          # optional - gap3
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)                # optional - gap3
            sage: SC.increasing_flip_poset()                            # optional - gap3
            Finite poset containing 5 elements

            sage: W = CoxeterGroup(['A',2])
            sage: SC = SubwordComplex([1,2,1,2,1], W.w0)
            sage: SC.increasing_flip_poset()
            Finite poset containing 5 elements
        """
