from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial, euler_phi as euler_phi
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class QuiverMutationTypeFactory(SageObject):
    def __call__(self, *args):
        """
        For a detailed description, see :meth:`QuiverMutationType`.

        EXAMPLES::

            sage: from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import QuiverMutationTypeFactory
            sage: QuiverMutationTypeFactory()
            QuiverMutationType
        """
    def samples(self, finite=None, affine=None, elliptic=None, mutation_finite=None):
        """
        Return a sample of the available quiver mutations types.

        INPUT:

        - ``finite``

        - ``affine``

        - ``elliptic``

        - ``mutation_finite``

        All four input keywords default values are ``None``. If
        set to ``True`` or ``False``, only these samples are returned.

        EXAMPLES::

            sage: QuiverMutationType.samples()
            [['A', 1], ['A', 5], ['B', 2], ['B', 5], ['C', 3],
             ['C', 5], [ ['A', 1], ['A', 1] ], ['D', 5], ['E', 6],
             ['E', 7], ['E', 8], ['F', 4], ['G', 2],
             ['A', [1, 1], 1], ['A', [4, 5], 1], ['D', 4, 1],
             ['BB', 5, 1], ['E', 6, [1, 1]], ['E', 7, [1, 1]],
             ['R2', [1, 5]], ['R2', [3, 5]], ['E', 10], ['BE', 5],
             ['GR', [3, 10]], ['T', [3, 3, 4]]]

            sage: QuiverMutationType.samples(finite=True)
            [['A', 1], ['A', 5], ['B', 2], ['B', 5], ['C', 3],
             ['C', 5], [ ['A', 1], ['A', 1] ], ['D', 5], ['E', 6],
             ['E', 7], ['E', 8], ['F', 4], ['G', 2]]

            sage: QuiverMutationType.samples(affine=True)
            [['A', [1, 1], 1], ['A', [4, 5], 1], ['D', 4, 1], ['BB', 5, 1]]

            sage: QuiverMutationType.samples(elliptic=True)
            [['E', 6, [1, 1]], ['E', 7, [1, 1]]]

            sage: QuiverMutationType.samples(mutation_finite=False)
            [['R2', [1, 5]], ['R2', [3, 5]], ['E', 10], ['BE', 5],
             ['GR', [3, 10]], ['T', [3, 3, 4]]]
        """

QuiverMutationType: Incomplete

class QuiverMutationType_abstract(UniqueRepresentation, SageObject):
    """
    EXAMPLES::

        sage: mut_type1 = QuiverMutationType('A',5)
        sage: mut_type2 = QuiverMutationType('A',5)
        sage: mut_type3 = QuiverMutationType('A',6)
        sage: mut_type1 == mut_type2
        True
        sage: mut_type1 == mut_type3
        False
    """
    def plot(self, circular: bool = False, directed: bool = True):
        """
        Return the plot of the underlying graph or digraph of ``self``.

        INPUT:

        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used

        - ``directed`` -- boolean (default: ``True``); if ``True``, the
          directed version is shown, otherwise the undirected

        EXAMPLES::

            sage: QMT = QuiverMutationType(['A',5])
            sage: pl = QMT.plot()                                                       # needs sage.plot sage.symbolic
            sage: pl = QMT.plot(circular=True)                                          # needs sage.plot sage.symbolic
        """
    def show(self, circular: bool = False, directed: bool = True) -> None:
        """
        Show the plot of the underlying digraph of ``self``.

        INPUT:

        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used

        - ``directed`` -- boolean (default: ``True``); if ``True``, the
          directed version is shown, otherwise the undirected

        TESTS::

            sage: QMT = QuiverMutationType(['A', 5])
            sage: QMT.show()                    # long time                             # needs sage.plot sage.symbolic
        """
    def letter(self):
        """
        Return the classification letter of ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType( ['A',5] ); mut_type
            ['A', 5]
            sage: mut_type.letter()
            'A'

            sage: mut_type = QuiverMutationType( ['BC',5, 1] ); mut_type
            ['BC', 5, 1]
            sage: mut_type.letter()
            'BC'

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.letter()
            'A x B'

            sage: mut_type = QuiverMutationType(['A',3],['B',3],['X',6]); mut_type
            [ ['A', 3], ['B', 3], ['X', 6] ]
            sage: mut_type.letter()
            'A x B x X'
        """
    def rank(self):
        """
        Return the rank in the standard quiver of ``self``.

        The rank is the number of vertices.

        EXAMPLES::

            sage: mut_type = QuiverMutationType( ['A',5] ); mut_type
            ['A', 5]
            sage: mut_type.rank()
            5

            sage: mut_type = QuiverMutationType( ['A',[4,5], 1] ); mut_type
            ['A', [4, 5], 1]
            sage: mut_type.rank()
            9

            sage: mut_type = QuiverMutationType( ['BC',5, 1] ); mut_type
            ['BC', 5, 1]
            sage: mut_type.rank()
            6

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.rank()
            6

            sage: mut_type = QuiverMutationType(['A',3],['B',3],['X',6]); mut_type
            [ ['A', 3], ['B', 3], ['X', 6] ]
            sage: mut_type.rank()
            12
        """
    @cached_method
    def b_matrix(self):
        """
        Return the B-matrix of the standard quiver of ``self``.

        The conventions for B-matrices agree with Fomin-Zelevinsky (up
        to a reordering of the simple roots).

        EXAMPLES::

            sage: mut_type = QuiverMutationType(['A',5]); mut_type
            ['A', 5]
            sage: mut_type.b_matrix()                                                   # needs sage.modules
            [ 0  1  0  0  0]
            [-1  0 -1  0  0]
            [ 0  1  0  1  0]
            [ 0  0 -1  0 -1]
            [ 0  0  0  1  0]

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.b_matrix()                                                   # needs sage.modules
            [ 0  1  0  0  0  0]
            [-1  0 -1  0  0  0]
            [ 0  1  0  0  0  0]
            [ 0  0  0  0  1  0]
            [ 0  0  0 -1  0 -1]
            [ 0  0  0  0  2  0]
        """
    @cached_method
    def standard_quiver(self):
        """
        Return the standard quiver of ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType( ['A',5] ); mut_type
            ['A', 5]
            sage: mut_type.standard_quiver()                                            # needs sage.modules
            Quiver on 5 vertices of type ['A', 5]

            sage: mut_type = QuiverMutationType( ['A',[5,3], 1] ); mut_type
            ['A', [3, 5], 1]
            sage: mut_type.standard_quiver()                                            # needs sage.modules
            Quiver on 8 vertices of type ['A', [3, 5], 1]

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.standard_quiver()                                            # needs sage.modules
            Quiver on 6 vertices of type [ ['A', 3], ['B', 3] ]

            sage: mut_type = QuiverMutationType(['A',3],['B',3],['X',6]); mut_type
            [ ['A', 3], ['B', 3], ['X', 6] ]
            sage: mut_type.standard_quiver()                                            # needs sage.modules
            Quiver on 12 vertices of type [ ['A', 3], ['B', 3], ['X', 6] ]
        """
    @cached_method
    def cartan_matrix(self):
        """
        Return the Cartan matrix of ``self``.

        Note that (up to a reordering of the simple roots) the convention for
        the definition of Cartan matrix, used here and elsewhere in Sage,
        agrees with the conventions of Kac, Fulton-Harris, and
        Fomin-Zelevinsky, but disagrees with the convention of Bourbaki.
        The `(i,j)` entry is `2(\\alpha_i,\\alpha_j)/(\\alpha_i,\\alpha_i)`.

        EXAMPLES::

            sage: mut_type = QuiverMutationType(['A',5]); mut_type
            ['A', 5]
            sage: mut_type.cartan_matrix()                                              # needs sage.modules
            [ 2 -1  0  0  0]
            [-1  2 -1  0  0]
            [ 0 -1  2 -1  0]
            [ 0  0 -1  2 -1]
            [ 0  0  0 -1  2]

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.cartan_matrix()                                              # needs sage.modules
            [ 2 -1  0  0  0  0]
            [-1  2 -1  0  0  0]
            [ 0 -1  2  0  0  0]
            [ 0  0  0  2 -1  0]
            [ 0  0  0 -1  2 -1]
            [ 0  0  0  0 -2  2]
        """
    def is_irreducible(self):
        """
        Return ``True`` if ``self`` is irreducible.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_irreducible()
            True
        """
    def is_mutation_finite(self):
        """
        Return ``True`` if ``self`` is of finite mutation type.

        This means that its mutation class has only finitely many
        different B-matrices.

        EXAMPLES::

            sage: mt = QuiverMutationType(['D',5, 1])
            sage: mt.is_mutation_finite()
            True
        """
    def is_simply_laced(self):
        """
        Return ``True`` if ``self`` is simply laced.

        This means that the only arrows that appear in the quiver of
        ``self`` are single unlabelled arrows.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_simply_laced()
            True

            sage: mt = QuiverMutationType(['B', 2])
            sage: mt.is_simply_laced()
            False

            sage: mt = QuiverMutationType(['A',(1, 1), 1])
            sage: mt.is_simply_laced()
            False
        """
    def is_skew_symmetric(self):
        """
        Return ``True`` if the B-matrix of ``self`` is skew-symmetric.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_skew_symmetric()
            True

            sage: mt = QuiverMutationType(['B', 2])
            sage: mt.is_skew_symmetric()
            False

            sage: mt = QuiverMutationType(['A',(1, 1), 1])
            sage: mt.is_skew_symmetric()
            True
        """
    def is_finite(self):
        """
        Return ``True`` if ``self`` is of finite type.

        This means that the cluster algebra associated to ``self`` has
        only a finite number of cluster variables.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_finite()
            True

            sage: mt = QuiverMutationType(['A',[4, 2], 1])
            sage: mt.is_finite()
            False
        """
    def is_affine(self):
        """
        Return ``True`` if ``self`` is of affine type.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_affine()
            False

            sage: mt = QuiverMutationType(['A',[4, 2], 1])
            sage: mt.is_affine()
            True
        """
    def is_elliptic(self):
        """
        Return ``True`` if ``self`` is of elliptic type.

        EXAMPLES::

            sage: mt = QuiverMutationType(['A', 2])
            sage: mt.is_elliptic()
            False

            sage: mt = QuiverMutationType(['E',6,[1, 1]])
            sage: mt.is_elliptic()
            True
        """
    def properties(self) -> None:
        """
        Print a scheme of all properties of ``self``.

        Most properties have natural definitions for either irreducible or
        reducible types.  ``affine`` and ``elliptic`` are only defined for
        irreducible types.

        EXAMPLES::

            sage: mut_type = QuiverMutationType(['A',3]); mut_type
            ['A', 3]
            sage: mut_type.properties()
            ['A', 3] has rank 3 and the following properties:
                - irreducible:       True
                - mutation finite:   True
                - simply-laced:      True
                - skew-symmetric:    True
                - finite:            True
                - affine:            False
                - elliptic:          False

            sage: mut_type = QuiverMutationType(['B',3]); mut_type
            ['B', 3]
            sage: mut_type.properties()
            ['B', 3] has rank 3 and the following properties:
                - irreducible:       True
                - mutation finite:   True
                - simply-laced:      False
                - skew-symmetric:    False
                - finite:            True
                - affine:            False
                - elliptic:          False

            sage: mut_type = QuiverMutationType(['B',3, 1]); mut_type
            ['BD', 3, 1]
            sage: mut_type.properties()
            ['BD', 3, 1] has rank 4 and the following properties:
                - irreducible:       True
                - mutation finite:   True
                - simply-laced:      False
                - skew-symmetric:    False
                - finite:            False
                - affine:            True
                - elliptic:          False

            sage: mut_type = QuiverMutationType(['E',6,[1, 1]]); mut_type
            ['E', 6, [1, 1]]
            sage: mut_type.properties()
            ['E', 6, [1, 1]] has rank 8 and the following properties:
                - irreducible:       True
                - mutation finite:   True
                - simply-laced:      False
                - skew-symmetric:    True
                - finite:            False
                - affine:            False
                - elliptic:          True

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.properties()
            [ ['A', 3], ['B', 3] ] has rank 6 and the following properties:
                - irreducible:       False
                - mutation finite:   True
                - simply-laced:      False
                - skew-symmetric:    False
                - finite:            True

            sage: mut_type = QuiverMutationType('GR',[4,9]); mut_type
            ['GR', [4, 9]]
            sage: mut_type.properties()
            ['GR', [4, 9]] has rank 12 and the following properties:
                - irreducible:       True
                - mutation finite:   False
                - simply-laced:      True
                - skew-symmetric:    True
                - finite:            False
                - affine:            False
                - elliptic:          False
        """

class QuiverMutationType_Irreducible(QuiverMutationType_abstract):
    """
    The mutation type for a cluster algebra or a quiver. Should not be
    called directly, but through :class:`QuiverMutationType`.
    """
    def __init__(self, letter, rank, twist=None) -> None:
        """
        Should not be called directly but through QuiverMutationType.

        INPUT:

        - ``letter`` -- the letter of the mutation type
        - ``rank`` -- the rank of the mutation type
        - ``twist`` -- the twist of the mutation type

        EXAMPLES::

            sage: QuiverMutationType('A',5)
            ['A', 5]

            sage: QuiverMutationType('A',[4,5], 1)
            ['A', [4, 5], 1]

            sage: QuiverMutationType('BB',5, 1)
            ['BB', 5, 1]

            sage: QuiverMutationType('X',6)
            ['X', 6]
        """
    def irreducible_components(self):
        """
        Return a list of all irreducible components of ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType('A',3); mut_type
            ['A', 3]
            sage: mut_type.irreducible_components()
            (['A', 3],)
        """
    @cached_method
    def class_size(self):
        """
        If it is known, the size of the mutation class of all quivers
        which are mutation equivalent to the standard quiver of
        ``self`` (up to isomorphism) is returned.

        Otherwise, :obj:`NotImplemented` is returned.

        Formula for finite type A is taken from Torkildsen - Counting
        cluster-tilted algebras of type `A_n`.
        Formulas for affine type A and finite type D are taken from Bastian,
        Prellberg, Rubey, Stump - Counting the number of elements in the
        mutation classes of `\\widetilde A_n` quivers.
        Formulas for finite and affine types B and C are
        proven but not yet published.
        Conjectural formulas for several other non-simply-laced affine types
        are implemented.
        Exceptional Types (finite, affine, and elliptic) E, F, G, and X are
        hardcoded.

        EXAMPLES::

            sage: mut_type = QuiverMutationType( ['A',5] ); mut_type
            ['A', 5]
            sage: mut_type.class_size()
            19

            sage: mut_type = QuiverMutationType( ['A',[10,3], 1] ); mut_type
            ['A', [3, 10], 1]
            sage: mut_type.class_size()
            142120

            sage: mut_type = QuiverMutationType( ['B',6] ); mut_type
            ['B', 6]
            sage: mut_type.class_size()
            132

            sage: mut_type = QuiverMutationType( ['BD',6, 1] ); mut_type
            ['BD', 6, 1]
            sage: mut_type.class_size()
            Warning: This method uses a formula which has not been proved correct.
            504

        Check that :issue:`14048` is fixed::

            sage: mut_type = QuiverMutationType( ['F',4,(2, 1)] )
            sage: mut_type.class_size()
            90
        """
    def dual(self):
        """
        Return the :class:`QuiverMutationType` which is dual to ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType('A',5); mut_type
            ['A', 5]
            sage: mut_type.dual()
            ['A', 5]

            sage: mut_type = QuiverMutationType('B',5); mut_type
            ['B', 5]
            sage: mut_type.dual()
            ['C', 5]
            sage: mut_type.dual().dual()
            ['B', 5]
            sage: mut_type.dual().dual() == mut_type
            True
        """

class QuiverMutationType_Reducible(QuiverMutationType_abstract):
    """
    The mutation type for a cluster algebra or a quiver. Should not be
    called directly, but through :class:`QuiverMutationType`.  Inherits from
    :class:`QuiverMutationType_abstract`.
    """
    def __init__(self, *args) -> None:
        """
        Should not be called directly, but through QuiverMutationType.

        INPUT:

        - ``data`` -- list; each of whose entries is a
          :class:`QuiverMutationType_Irreducible`

        EXAMPLES::

            sage: QuiverMutationType(['A',4],['B',6])
            [ ['A', 4], ['B', 6] ]
        """
    def irreducible_components(self):
        """
        Return a list of all irreducible components of ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType('A',3); mut_type
            ['A', 3]
            sage: mut_type.irreducible_components()
            (['A', 3],)

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.irreducible_components()
            (['A', 3], ['B', 3])

            sage: mut_type = QuiverMutationType(['A',3],['B',3],['X',6])
            sage: mut_type
            [ ['A', 3], ['B', 3], ['X', 6] ]
            sage: mut_type.irreducible_components()
            (['A', 3], ['B', 3], ['X', 6])
        """
    @cached_method
    def class_size(self):
        """
        If it is known, the size of the mutation class of all quivers
        which are mutation equivalent to the standard quiver of
        ``self`` (up to isomorphism) is returned.

        Otherwise, :obj:`NotImplemented` is returned.

        EXAMPLES::

            sage: mut_type = QuiverMutationType(['A',3],['B',3]); mut_type
            [ ['A', 3], ['B', 3] ]
            sage: mut_type.class_size()
            20

            sage: mut_type = QuiverMutationType(['A',3],['B',3],['X',6])
            sage: mut_type
            [ ['A', 3], ['B', 3], ['X', 6] ]
            sage: mut_type.class_size()
            100
        """
    def dual(self):
        """
        Return the :class:`QuiverMutationType` which is dual to ``self``.

        EXAMPLES::

            sage: mut_type = QuiverMutationType(['A',5],['B',6],['C',5],['D',4]); mut_type
            [ ['A', 5], ['B', 6], ['C', 5], ['D', 4] ]
            sage: mut_type.dual()
            [ ['A', 5], ['C', 6], ['B', 5], ['D', 4] ]
        """

def save_quiver_data(n, up_to: bool = True, types: str = 'ClassicalExceptional', verbose: bool = True) -> None:
    """
    Save mutation classes of certain quivers of ranks up to and equal
    to `n` or equal to `n` to
    ``DOT_SAGE/cluster_algebra_quiver/mutation_classes_n.dig6``.

    This data will then be used to determine quiver mutation types.

    INPUT:

    - ``n`` -- the rank (or the upper limit on the rank) of the mutation
      classes that are being saved

    - ``up_to`` -- (default: ``True``) if ``True``, saves data for
      ranks smaller than or equal to `n`; if ``False``, saves data
      for rank exactly `n`

    - ``types`` -- (default: ``'ClassicalExceptional'``) if all, saves data
      for both exceptional mutation-finite quivers and for classical
      quiver; the input 'Exceptional' or 'Classical' is also allowed
      to save only part of this data

    TESTS::

        sage: # needs sage.modules
        sage: from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import save_quiver_data
        sage: save_quiver_data(2)
        <BLANKLINE>
        The following types are saved to file ... and will now be used to determine quiver mutation types:
        [('A', 1)]
        <BLANKLINE>
        The following types are saved to file ... and will now be used to determine quiver mutation types:
        [('A', (1, 1), 1), ('A', 2), ('B', 2), ('BC', 1, 1), ('G', 2)]
        sage: save_quiver_data(2,up_to=False)
        <BLANKLINE>
        The following types are saved to file ... and will now be used to determine quiver mutation types:
        [('A', (1, 1), 1), ('A', 2), ('B', 2), ('BC', 1, 1), ('G', 2)]
        sage: save_quiver_data(2,up_to=False, types='Classical')
        <BLANKLINE>
        The following types are saved to file ... and will now be used to determine quiver mutation types:
        [('A', (1, 1), 1), ('A', 2), ('B', 2), ('BC', 1, 1)]
        sage: save_quiver_data(2,up_to=False, types='Exceptional')
        <BLANKLINE>
        The following types are saved to file ... and will now be used to determine quiver mutation types:
        [('G', 2)]
        sage: save_quiver_data(2,up_to=False, verbose=False)
    """
