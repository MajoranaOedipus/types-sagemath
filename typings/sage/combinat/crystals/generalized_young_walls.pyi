from _typeshed import Incomplete
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class GeneralizedYoungWall(CombinatorialElement):
    """
    A generalized Young wall.

    For more information, see
    :class:`~sage.combinat.crystals.generalized_young_walls.InfinityCrystalOfGeneralizedYoungWalls`.

    EXAMPLES::

        sage: Y = crystals.infinity.GeneralizedYoungWalls(4)
        sage: mg = Y.module_generators[0]; mg.pp()
        0
        sage: mg.f_string([1,2,0,1]).pp()
        1|2|
        0|1|
           |
    """
    rows: Incomplete
    cols: int
    data: Incomplete
    def __init__(self, parent, data) -> None:
        """
        EXAMPLES::

            sage: Y = crystals.infinity.GeneralizedYoungWalls(2)
            sage: mg = Y.module_generators[0]
            sage: TestSuite(mg).run()
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: GYW = crystals.infinity.GeneralizedYoungWalls(2)
            sage: y = GYW([[],[1,0],[2,1]])
            sage: x = GYW([[],[1,0],[2,1]])
            sage: z = GYW([[],[1],[2]])
            sage: x == y
            True
            sage: x == z
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: GYW = crystals.infinity.GeneralizedYoungWalls(2)
            sage: h = hash(GYW)
        """
    def raw_signature(self, i):
        """
        Return the sequence from `\\{+,-\\}` obtained from all `i`-admissible
        slots and removable `i`-boxes  without canceling any `(+,-)`-pairs.
        The result also notes the row and column of the sign.

        EXAMPLES::

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.raw_signature(2)
            [['-', 3, 6], ['-', 1, 4], ['-', 6, 1]]
        """
    def generate_signature(self, i):
        """
        The `i`-signature of ``self`` (with whitespace where cancellation
        occurs) together with the unreduced sequence from `\\{+,-\\}`.  The
        result also records to the row and column position of the sign.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(2)([[0],[1,0],[2,1,0,2],[],[1]])
            sage: y.generate_signature(1)
            ([['+', 2, 5], ['-', 4, 1]], '  ')
        """
    def signature(self, i):
        """
        Return the `i`-signature of ``self``.

        The signature is obtained by reading ``self`` in columns bottom to top starting from the left.
        Then add a `-` at every `i`-box which may be removed from ``self`` and still obtain a legal
        generalized Young wall, and add a `+` at each site for which an `i`-box may be added and still
        obtain a valid generalized Young wall.  Then successively cancel any `(+,-)`-pair to obtain a
        sequence of the form `- \\cdots -+ \\cdots +`.  This resulting sequence is the output.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(2)([[0],[1,0],[2,1,0,2],[],[1]])
            sage: y.signature(1)
            ''

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.signature(2)
            '---'
        """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(2)([[0,2,1],[1,0,2,1,0],[],[0],[1,0,2],[],[],[1]])
            sage: y.pp()
                    1|
                     |
                     |
                2|0|1|
                    0|
                     |
            0|1|2|0|1|
                1|2|0|
        """
    def content(self):
        """
        Return total number of blocks in ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(2)([[0],[1,0],[2,1,0,2],[],[1]])
            sage: y.content()
            8

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.content()
            13
        """
    def number_of_parts(self):
        """
        Return the value of `\\mathscr{N}` on ``self``.

        In [KLRS2016]_, the statistic `\\mathscr{N}` was defined on elements in
        `\\mathcal{Y}(\\infty)` which counts how many parts are in the
        corresponding Kostant partition.  Specifically, the computation of
        `\\mathscr{N}(Y)` is done using the following algorithm:

        - If `Y` has no rows whose right-most box is colored `n` and such that
          the length of this row is a multiple of `n+1`, then `\\mathscr{N}(Y)`
          is the total number of distinct rows in `Y`, not counting multiplicity.

        - Otherwise, search `Y` for the longest row such that the right-most box
          is colored `n` and such that the total number of boxes in the row is
          `k(n+1)` for some `k\\ge 1`.  Replace this row by `n+1` distinct rows
          of length `k`, reordering all rows, if necessary, so that the result
          is a proper wall.  (Note that the resulting wall may no longer be
          reduced.) Repeat the search and replace process for all other rows of
          the above form for each `k' < k`.  Then `\\mathscr{N}(Y)` is the number
          of distinct rows, not counting multiplicity, in the wall resulting
          from this process.

        EXAMPLES::

            sage: Y = crystals.infinity.GeneralizedYoungWalls(3)
            sage: y = Y([[0],[],[],[],[0],[],[],[],[0]])
            sage: y.number_of_parts()
            1

            sage: Y = crystals.infinity.GeneralizedYoungWalls(3)
            sage: y = Y([[0,3,2],[1,0],[],[],[0,3],[1,0],[],[],[0]])
            sage: y.number_of_parts()
            4

            sage: Y = crystals.infinity.GeneralizedYoungWalls(2)
            sage: y = Y([[0,2,1],[1,0],[2,1,0,2,1,0,2,1,0],[],[2,1,0,2,1,0]])
            sage: y.number_of_parts()
            8
        """
    def sum_of_weighted_row_lengths(self):
        """
        Return the value of `\\mathscr{M}` on ``self``.

        Let `\\mathcal{Y}_0 \\subset \\mathcal{Y}(\\infty)` be the set of
        generalized Young walls which have no rows whose right-most box is
        colored `n`.  For `Y \\in \\mathcal{Y}_0`,

        .. MATH::

            \\mathscr{M}(Y) = \\sum_{i=1}^n (i+1)M_i(Y),

        where `M_i(Y)` is the number of nonempty rows in `Y` whose right-most
        box is colored `i-1`.

        EXAMPLES::

            sage: Y = crystals.infinity.GeneralizedYoungWalls(2)
            sage: y = Y([[0,2,1,0,2],[1,0,2],[],[0,2],[1,0],[],[0],[1,0]])
            sage: y.sum_of_weighted_row_lengths()
            15
        """
    def e(self, i):
        """
        Return the application of the Kashiwara raising operator
        `e_i` on ``self``.

        This will remove the `i`-colored box corresponding to the
        rightmost `+` in ``self.signature(i)``.

        EXAMPLES::

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.e(2)
            [[], [1, 0, 3, 2], [2, 1], [3, 2, 1, 0, 3, 2]]
            sage: _.e(2)
            [[], [1, 0, 3], [2, 1], [3, 2, 1, 0, 3, 2]]
            sage: _.e(2)
            [[], [1, 0, 3], [2, 1], [3, 2, 1, 0, 3]]
            sage: _.e(2)
        """
    def f(self, i):
        """
        Return the application of the Kashiwara lowering operator
        `f_i` on ``self``.

        This will add an `i`-colored colored box to the site corresponding
        to the leftmost plus in ``self.signature(i)``.

        EXAMPLES::

            sage: hw = crystals.infinity.GeneralizedYoungWalls(2)([])
            sage: hw.f(1)
            [[], [1]]
            sage: _.f(2)
            [[], [1], [2]]
            sage: _.f(0)
            [[], [1, 0], [2]]
            sage: _.f(0)
            [[0], [1, 0], [2]]
        """
    def latex_large(self) -> str:
        """
        Generate LaTeX code for ``self`` but the output is larger.

        This requires TikZ.

        EXAMPLES::

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.latex_large()
            '\\\\begin{tikzpicture}[baseline=5,scale=.45] \\n \\\\foreach \\\\x [count=\\\\s from 0] in \\n{{},{1,0,3,2},{2,1},{3,2,1,0,3,2},{},{},{2}} \\n{\\\\foreach \\\\y [count=\\\\t from 0] in \\\\x {  \\\\node[font=\\\\scriptsize] at (-\\\\t,\\\\s) {$\\\\y$}; \\n \\\\draw (-\\\\t+.5,\\\\s+.5) to (-\\\\t-.5,\\\\s+.5); \\n \\\\draw (-\\\\t+.5,\\\\s-.5) to (-\\\\t-.5,\\\\s-.5); \\n \\\\draw (-\\\\t-.5,\\\\s-.5) to (-\\\\t-.5,\\\\s+.5);  } \\n \\\\draw[-,thick] (.5,\\\\s+1) to (.5,-.5) to (-\\\\s-1,-.5); } \\n \\\\end{tikzpicture} \\n'
        """
    def weight(self, root_lattice: bool = False):
        """
        Return the weight of ``self``.

        INPUT:

        - ``root_lattice`` -- boolean determining whether weight should appear
          in root lattice or not in extended affine weight lattice

        EXAMPLES::

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.weight()
            2*Lambda[0] + Lambda[1] - 4*Lambda[2] + Lambda[3] - 2*delta
            sage: x.weight(root_lattice=True)
            -2*alpha[0] - 3*alpha[1] - 5*alpha[2] - 3*alpha[3]
        """
    def epsilon(self, i):
        """
        Return the number of `i`-colored arrows in the `i`-string above
        ``self`` in the crystal graph.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: y.epsilon(1)
            0
            sage: y.epsilon(2)
            3
            sage: y.epsilon(0)
            0
        """
    def Epsilon(self):
        """
        Return `\\sum_{i=0}^n \\varepsilon_i(Y) \\Lambda_i` where `Y` is ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: y.Epsilon()
            Lambda[0] + 3*Lambda[2]
        """
    def phi(self, i):
        """
        Return the value `\\varepsilon_i(Y) + \\langle h_i,
        \\mathrm{wt}(Y)\\rangle`, where `h_i` is the `i`-th simple
        coroot and `Y` is ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: y.phi(1)
            3
            sage: y.phi(2)
            -1
        """
    def Phi(self):
        """
        Return `\\sum_{i=0}^n \\varphi_i(Y) \\Lambda_i` where `Y` is ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: y.Phi()
            -Lambda[0] + 3*Lambda[1] - Lambda[2] + 3*Lambda[3]

            sage: x = crystals.infinity.GeneralizedYoungWalls(3)([[],[1,0,3,2],[2,1],[3,2,1,0,3,2],[],[],[2]])
            sage: x.Phi()
            2*Lambda[0] + Lambda[1] - Lambda[2] + Lambda[3]
        """
    def column(self, k):
        """
        Return the list of boxes from the ``k``-th column of ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: y.column(2)
            [None, 0, 1, 2, None, None, None]

            sage: hw = crystals.infinity.GeneralizedYoungWalls(5)([])
            sage: hw.column(1)
            []
        """
    def a(self, i, k):
        """
        Return the number `a_i(k)` of `i`-colored boxes in the ``k``-th
        column of ``self``.

        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: y.a(1,2)
            1
            sage: y.a(0,2)
            1
            sage: y.a(3,2)
            0
        """
    def in_highest_weight_crystal(self, La):
        """
        Return a boolean indicating if the generalized Young wall element
        is in the highest weight crystal cut out by the given highest weight
        ``La``.

        By Theorem 4.1 of [KS2010]_, a generalized Young wall `Y` represents a
        vertex in the highest weight crystal `Y(\\lambda)`, with
        `\\lambda = \\Lambda_{i_1} + \\Lambda_{i_2} + \\cdots + \\Lambda_{i_\\ell}`
        a dominant integral weight of level `\\ell > 0`, if it satisfies the
        following condition. For each positive integer `k`, if there exists
        `j \\in I` such that `a_j(k) - a_{j-1}(k) > 0`, then for some
        `p = 1, \\ldots, \\ell`,

        .. MATH::

            j + k \\equiv i_p + 1 \\bmod n+1 \\text{ and } a_j(k) - a_{j-1}(k)
            \\le \\lambda(h_{i_p}),

        where `\\{h_0, h_1, \\ldots, h_n\\}` is the set of simple coroots attached
        to `A_n^{(1)}`.

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()[1]
            sage: GYW = crystals.infinity.GeneralizedYoungWalls(2)
            sage: y = GYW([[],[1,0],[2,1]])
            sage: y.in_highest_weight_crystal(La)
            True
            sage: x = GYW([[],[1],[2],[],[],[2],[],[],[2]])
            sage: x.in_highest_weight_crystal(La)
            False
        """

class InfinityCrystalOfGeneralizedYoungWalls(UniqueRepresentation, Parent):
    """
    The crystal `\\mathcal{Y}(\\infty)` of generalized Young walls of
    type `A_n^{(1)}` as defined in [KS2010]_.

    A generalized Young wall is a collection of boxes stacked on a fixed board,
    such that color of the box at the site located in the `j`-th row from the
    bottom and the `i`-th column from the right is `j-1 \\bmod n+1`.  There are
    several growth conditions on elements in `Y \\in \\mathcal{Y}(\\infty)`:

    - Walls grow in rows from right to left.  That is, for every box `y\\in Y`
      that is not in the rightmost column, there must be a box immediately to
      the right of `y`.

    - For all `p>q` such that `p-q \\equiv 0 \\bmod n+1`, the `p`-th row has
      most as many boxes as the `q`-th row.

    - There does not exist a column in the wall such that if one `i`-colored
      box, for every `i = 0,1,\\ldots,n`, is removed from that column, then the
      result satisfies the above conditions.

    There is a crystal structure on `\\mathcal{Y}(\\infty)` defined as follows.
    Define maps

    .. MATH::

        e_i,\\ f_i \\colon \\mathcal{Y}(\\infty)
        \\longrightarrow \\mathcal{Y}(\\infty) \\sqcup \\{0\\}, \\qquad
        \\varepsilon_i,\\ \\varphi_i \\colon \\mathcal{Y}(\\infty)
        \\longrightarrow \\ZZ, \\qquad
        \\mathrm{wt}\\colon \\mathcal{Y}(\\infty) \\longrightarrow
        \\bigoplus_{i=0}^n \\ZZ \\Lambda_i \\oplus \\ZZ \\delta,

    by

    .. MATH::

        \\mathrm{wt}(Y) = -\\sum_{i=0}^n m_i(Y) \\alpha_i,

    where `m_i(Y)` is the number of `i`-boxes in `Y`, `\\varepsilon_i(Y)`
    is the number of `-` in the `i`-signature of `Y`, and

    .. MATH::

        \\varphi_i(Y)  = \\varepsilon_i(Y) + \\langle h_i, \\mathrm{wt}(Y) \\rangle.

    See :meth:`GeneralizedYoungWall.e()`, :meth:`GeneralizedYoungWall.f()`,
    and :meth:`GeneralizedYoungWall.signature()` for more about
    `e_i`, `f_i`, and `i`-signatures.


    INPUT:

    - ``n`` -- type `A_n^{(1)}`

    EXAMPLES::

        sage: Yinf = crystals.infinity.GeneralizedYoungWalls(3)
        sage: y = Yinf([[0],[1,0,3,2],[],[3,2,1],[0],[1,0]])
        sage: y.pp()
            0|1|
              0|
          1|2|3|
               |
        2|3|0|1|
              0|
        sage: y.weight(root_lattice=True)
        -4*alpha[0] - 3*alpha[1] - 2*alpha[2] - 2*alpha[3]
        sage: y.f(0)
        [[0], [1, 0, 3, 2], [], [3, 2, 1], [0], [1, 0], [], [], [0]]
        sage: y.e(0).pp()
            0|1|
               |
          1|2|3|
               |
        2|3|0|1|
              0|

    To display the crystal down to depth 3::

        sage: S = Yinf.subcrystal(max_depth=3)
        sage: G = Yinf.digraph(subset=S) # long time
        sage: view(G) # not tested
    """
    @staticmethod
    def __classcall_private__(cls, n, category=None):
        """
        Normalize input to ensure a unique representation.

        INPUT:

        - ``n`` -- type `A_n^{(1)}`

        EXAMPLES::

            sage: Yinf = crystals.infinity.GeneralizedYoungWalls(3)
            sage: Yinf2 = crystals.infinity.GeneralizedYoungWalls(int(3))
            sage: Yinf is Yinf2
            True
        """
    module_generators: Incomplete
    def __init__(self, n, category) -> None:
        """
        EXAMPLES::

            sage: Yinf = crystals.infinity.GeneralizedYoungWalls(3)
            sage: TestSuite(Yinf).run()
        """
    Element = GeneralizedYoungWall

class CrystalOfGeneralizedYoungWallsElement(GeneralizedYoungWall):
    """
    Element of the highest weight crystal of generalized Young walls.
    """
    def e(self, i):
        """
        Compute the action of `e_i` restricted to the highest weight crystal.

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()[1]
            sage: hwy = crystals.GeneralizedYoungWalls(2,La)([[],[1,0],[2,1]])
            sage: hwy.e(1)
            [[], [1, 0], [2]]
            sage: hwy.e(2)
            sage: hwy.e(3)
        """
    def f(self, i):
        """
        Compute the action of `f_i` restricted to the highest weight crystal.

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()[1]
            sage: GYW = crystals.infinity.GeneralizedYoungWalls(2)
            sage: y = GYW([[],[1,0],[2,1]])
            sage: y.f(1)
            [[], [1, 0], [2, 1], [], [1]]
            sage: hwy = crystals.GeneralizedYoungWalls(2,La)([[],[1,0],[2,1]])
            sage: hwy.f(1)
        """
    def weight(self):
        """
        Return the weight of ``self`` in the highest weight crystal as an
        element of the weight lattice `\\bigoplus_{i=0}^n \\ZZ \\Lambda_i`.

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()[1]
            sage: hwy = crystals.GeneralizedYoungWalls(2,La)([[],[1,0],[2,1]])
            sage: hwy.weight()
            Lambda[0] - Lambda[1] + Lambda[2] - delta
        """
    def phi(self, i):
        """
        Return the value `\\varepsilon_i(Y) + \\langle h_i,
        \\mathrm{wt}(Y)\\rangle`, where `h_i` is the `i`-th simple
        coroot and `Y` is ``self``.

        EXAMPLES::

            sage: La = RootSystem(['A',3,1]).weight_lattice(extended=True).fundamental_weights()
            sage: y = crystals.GeneralizedYoungWalls(3,La[0])([])
            sage: y.phi(1)
            0
            sage: y.phi(2)
            0
        """

class CrystalOfGeneralizedYoungWalls(InfinityCrystalOfGeneralizedYoungWalls):
    """
    The crystal `\\mathcal{Y}(\\lambda)` of generalized Young walls of the given
    type with highest weight `\\lambda`.

    These were characterized in Theorem 4.1 of [KS2010]_.
    See :meth:`GeneralizedYoungWall.in_highest_weight_crystal()`.

    INPUT:

    - ``n`` -- type `A_n^{(1)}`

    - ``weight`` -- dominant integral weight

    EXAMPLES::

        sage: La = RootSystem(['A',3,1]).weight_lattice(extended=True).fundamental_weights()[1]
        sage: YLa = crystals.GeneralizedYoungWalls(3,La)
        sage: y = YLa([[0],[1,0,3,2,1],[2,1,0],[3]])
        sage: y.pp()
                3|
            0|1|2|
        1|2|3|0|1|
                0|
        sage: y.weight()
        -Lambda[0] + Lambda[2] + Lambda[3] - 3*delta
        sage: y.in_highest_weight_crystal(La)
        True
        sage: y.f(1)
        [[0], [1, 0, 3, 2, 1], [2, 1, 0], [3], [], [1]]
        sage: y.f(1).f(1)
        sage: yy = crystals.infinity.GeneralizedYoungWalls(3)([[0], [1, 0, 3, 2, 1], [2, 1, 0], [3], [], [1]])
        sage: yy.f(1)
        [[0], [1, 0, 3, 2, 1], [2, 1, 0], [3], [], [1], [], [], [], [1]]
        sage: yyy = yy.f(1)
        sage: yyy.in_highest_weight_crystal(La)
        False

        sage: LS = crystals.LSPaths(['A',3,1],[1,0,0,0])
        sage: C = LS.subcrystal(max_depth=4)
        sage: G = LS.digraph(subset=C)
        sage: P = RootSystem(['A',3,1]).weight_lattice(extended=True)
        sage: La = P.fundamental_weights()
        sage: YW = crystals.GeneralizedYoungWalls(3,La[0])
        sage: CW = YW.subcrystal(max_depth=4)
        sage: GW = YW.digraph(subset=CW)
        sage: GW.is_isomorphic(G,edge_labels=True)
        True

    To display the crystal down to a specified depth::

        sage: S = YLa.subcrystal(max_depth=4)
        sage: G = YLa.digraph(subset=S)
        sage: view(G) # not tested
    """
    @staticmethod
    def __classcall_private__(cls, n, La):
        """
        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()[2]
            sage: Al = RootSystem(['A',2,1]).weight_lattice(extended=True).monomial(2)
            sage: Y = crystals.GeneralizedYoungWalls(2,La)
            sage: Y1 = crystals.GeneralizedYoungWalls(int(2),Al)
            sage: Y is Y1
            True
        """
    hw: Incomplete
    def __init__(self, n, La) -> None:
        '''
        EXAMPLES::

            sage: La = RootSystem([\'A\',2,1]).weight_lattice(extended=True).fundamental_weights()[1]
            sage: YLa = crystals.GeneralizedYoungWalls(2,La)

        We skip the two tests because they take a very long time::

            sage: TestSuite(YLa).run(skip=["_test_enumerated_set_contains","_test_stembridge_local_axioms"]) # long time
        '''
    Element = CrystalOfGeneralizedYoungWallsElement
    def __iter__(self):
        """
        EXAMPLES::

            sage: y = crystals.infinity.GeneralizedYoungWalls(3)([[0],[1,0,3,2],[2,1],[3,2,1,0,3,2],[0],[],[2]])
            sage: x = y.__iter__()
            sage: next(x)
            [0]
        """
