from _typeshed import Incomplete
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class InfinityCrystalOfMultisegments(Parent, UniqueRepresentation):
    """
    The type `A_n^{(1)}` crystal `B(\\infty)` realized using
    Bernstein-Zelevinsky (BZ) multisegments.

    Using (a modified version of the) notation from [JL2009]_, for `\\ell \\in
    \\ZZ_{>0}` and `i \\in \\ZZ / (n+1)\\ZZ`, a segment of length `\\ell` and head
    `i` is the sequence of consecutive residues `[i,i+1,\\dots,i+\\ell-1]`.  The
    notation  for a segment of length `\\ell` and head `i` is simplified to
    `[i; \\ell)`.  Similarly, a segment of length `\\ell` and tail `i` is the
    sequence of consecutive residues `[i-\\ell+1, \\ldots, i-1, i]`.  The latter
    is denoted simply by `(\\ell;i]`.  Finally, a multisegment is a formal
    linear combination of segments, usually written in the form

    .. MATH::

        \\psi =
        \\sum_{\\substack{i \\in \\ZZ/(n+1)\\ZZ \\\\ \\ell \\in \\ZZ_{>0}}}
        m_{(\\ell;i]} (\\ell; i].

    Such a multisegment is called aperiodic if, for every `\\ell > 0`, there
    exists some `i \\in \\ZZ / (n+1)\\ZZ` such that `(\\ell; i]` does not appear
    in `\\psi`. Denote the set of all periodic multisegments, together with
    the empty multisegment `\\varnothing`, by `\\Psi`.  We define a crystal
    structure on multisegments as follows.  Set `S_{\\ell,i} = \\sum_{k \\ge \\ell}
    (m_{(k;i-1]} - m_{(k;i]})` and let `\\ell_f` be the minimal `\\ell` that
    attains the value `\\min_{\\ell > 0} S_{\\ell,i}`. Then we have

    .. MATH::

        f_i \\psi =
        \\begin{cases}
         \\psi + (1;i] & \\text{ if } \\ell_f = 1,\\\\\n         \\psi + (\\ell_f;i] - (\\ell_f-1;i-1] & \\text{ if } \\ell_f > 1.
        \\end{cases}

    Similarly, let `\\ell_e` be the maximal `\\ell` that attains the value
    `\\min_{\\ell > 0} S_{\\ell,i}`.  Then we have

    .. MATH::

        e_i \\psi =
        \\begin{cases}
         0 & \\text{ if } \\min_{\\ell > 0} S_{\\ell,i} = 0, \\\\\n         \\psi + (1; i] & \\text{ if } \\ell_e = 1,\\\\\n         \\psi - (\\ell_e; i] + (\\ell_e-1; i-1] & \\text{ if } \\ell_e > 1.
        \\end{cases}

    Alternatively, the crystal operators may be defined using a signature
    rule, as detailed in Section 4 of [JL2009]_ (following [AJL2011]_).  For
    `\\psi \\in \\Psi` and `i \\in \\ZZ/(n+1)\\ZZ`, encode all segments in `\\psi`
    with tail `i` by the symbol `R` and all segments in `\\psi` with tail
    `i-1` by `A`.  For `\\ell > 0`, set
    `w_{i,\\ell} = R^{m_{(\\ell;i]}} A^{m_{(\\ell;i-1]}}` and
    `w_i = \\prod_{\\ell\\ge 1} w_{i,\\ell}`.  By successively canceling out
    as many `RA` factors as possible, set
    `\\widetilde{w}_i = A^{a_i(\\psi)} R^{r_i(\\psi)}`.  If `a_i(\\psi) > 0`,
    denote by `\\ell_f > 0` the length of the rightmost segment `A` in
    `\\widetilde{w}_i`.  If `a_i(\\psi) = 0`, set `\\ell_f = 0`.  Then

    .. MATH::

        f_i \\psi =
        \\begin{cases}
         \\psi + (1; i] & \\text{ if } a_i(\\psi) = 0,\\\\\n         \\psi + (\\ell_f; i] - (\\ell_f-1; i-1] & \\text{ if } a_i(\\psi) > 0.
        \\end{cases}

    The rule for computing `e_i \\psi` is similar.

    INPUT:

    - ``n`` -- for type `A_n^{(1)}`

    EXAMPLES::

        sage: B = crystals.infinity.Multisegments(2)
        sage: x = B([(8,1),(6,0),(5,1),(5,0),(4,0),(4,1),(4,1),(3,0),(3,0),(3,1),(3,1),(1,0),(1,2),(1,2)]); x
        (8; 1] + (6; 0] + (5; 0] + (5; 1] + (4; 0] + 2 * (4; 1]
         + 2 * (3; 0] + 2 * (3; 1] + (1; 0] + 2 * (1; 2]
        sage: x.f(1)
        (8; 1] + (6; 0] + (5; 0] + (5; 1] + (4; 0] + 2 * (4; 1]
         + 2 * (3; 0] + 2 * (3; 1] + (2; 1] + 2 * (1; 2]
        sage: x.f(1).f(1)
        (8; 1] + (6; 0] + (5; 0] + (5; 1] + (4; 0] + 2 * (4; 1]
         + 2 * (3; 0] + 2 * (3; 1] + (2; 1] + (1; 1] + 2 * (1; 2]
        sage: x.e(1)
        (7; 0] + (6; 0] + (5; 0] + (5; 1] + (4; 0] + 2 * (4; 1]
         + 2 * (3; 0] + 2 * (3; 1] + (1; 0] + 2 * (1; 2]
        sage: x.e(1).e(1)
        sage: x.f(0)
        (8; 1] + (6; 0] + (5; 0] + (5; 1] + (4; 0] + 2 * (4; 1]
         + 2 * (3; 0] + 2 * (3; 1] + (2; 0] + (1; 0] + (1; 2]

    We check an `\\widehat{\\mathfrak{sl}}_2` example against the generalized
    Young walls::

        sage: B = crystals.infinity.Multisegments(1)
        sage: G = B.subcrystal(max_depth=4).digraph()
        sage: C = crystals.infinity.GeneralizedYoungWalls(1)
        sage: GC = C.subcrystal(max_depth=4).digraph()
        sage: G.is_isomorphic(GC, edge_labels=True)
        True

    REFERENCES:

    - [AJL2011]_
    - [JL2009]_
    - [LTV1999]_
    """
    module_generators: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Multisegments(2)
            sage: TestSuite(B).run()
        """
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Multisegments(2)
            sage: B.highest_weight_vector()
            0
        """
    def weight_lattice_realization(self):
        """
        Return a realization of the weight lattice of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Multisegments(2)
            sage: B.weight_lattice_realization()
            Extended weight lattice of the Root system of type ['A', 2, 1]
        """
    class Element(ElementWrapper):
        """
        An element in a BZ multisegments crystal.
        """
        def __init__(self, parent, value) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: mg = B.highest_weight_vector()
                sage: TestSuite(mg).run()
            """
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: b = B([(4,2), (3,0), (3,1), (1,1), (1,0)])
                sage: b.e(0)
                (4; 2] + (3; 0] + (3; 1] + (1; 1]
                sage: b.e(1)
                sage: b.e(2)
                (3; 0] + 2 * (3; 1] + (1; 0] + (1; 1]
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: b = B([(4,2), (3,0), (3,1), (1,1), (1,0)])
                sage: b.f(0)
                (4; 2] + (3; 0] + (3; 1] + 2 * (1; 0] + (1; 1]
                sage: b.f(1)
                (4; 2] + (3; 0] + (3; 1] + (1; 0] + 2 * (1; 1]
                sage: b.f(2)
                2 * (4; 2] + (3; 0] + (1; 0] + (1; 1]
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: b = B([(4,2), (3,0), (3,1), (1,1), (1,0)])
                sage: b.epsilon(0)
                1
                sage: b.epsilon(1)
                0
                sage: b.epsilon(2)
                1
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            Let `\\psi \\in \\Psi`. Define `\\varphi_i(\\psi) :=
            \\varepsilon_i(\\psi) + \\langle h_i, \\mathrm{wt}(\\psi) \\rangle`,
            where `h_i` is the `i`-th simple coroot and `\\mathrm{wt}(\\psi)` is the
            :meth:`weight` of `\\psi`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: b = B([(4,2), (3,0), (3,1), (1,1), (1,0)])
                sage: b.phi(0)
                1
                sage: b.phi(1)
                0
                sage: mg = B.highest_weight_vector()
                sage: mg.f(1).phi(0)
                1
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: B = crystals.infinity.Multisegments(2)
                sage: b = B([(4,2), (3,0), (3,1), (1,1), (1,0)])
                sage: b.weight()
                -4*delta
            """
