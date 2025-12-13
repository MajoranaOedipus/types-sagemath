from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.backtrack import GenericBacktracker as GenericBacktracker
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.partition import Partition as Partition
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CompositionTableau(CombinatorialElement, metaclass=ClasscallMetaclass):
    """
    A composition tableau.

    A *composition tableau* `t` of shape `I = (I_1, \\ldots, I_{\\ell})` is an
    array of boxes in rows,  `I_i` boxes in row `i`, filled with positive
    integers such that:

    1) the entries in the rows of `t` weakly decrease from left to right,
    2) the left-most column of `t` strictly increase from top to bottom.
    3) Add zero entries to the rows of `t` until the resulting array is
       rectangular of  shape `\\ell \\times m`. For `1 \\leq i < j \\leq \\ell,
       2 \\leq k \\leq m` and `(t(j,k) \\neq 0`, and also if `t(j,k) \\geq t(i,k))`
       implies `t(j,k) > t(i,k-1).`

    INPUT:

    - ``t`` -- list of lists

    EXAMPLES::

        sage: CompositionTableau([[1],[2,2]])
        [[1], [2, 2]]
        sage: CompositionTableau([[1],[3,2],[4,4]])
        [[1], [3, 2], [4, 4]]
        sage: CompositionTableau([])
        []
    """
    @staticmethod
    def __classcall_private__(self, t):
        """
        This ensures that a composition tableau is only ever constructed as
        an ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = CompositionTableau([[1],[2,2]])
            sage: TestSuite(t).run()

            sage: t.parent()
            Composition Tableaux
            sage: t.category()
            Category of elements of Composition Tableaux
        """
    def __init__(self, parent, t) -> None:
        """
        Initialize a composition tableau.

        TESTS::

            sage: t = CompositionTableaux()([[1],[2,2]])
            sage: s = CompositionTableaux(3)([[1],[2,2]])
            sage: s == t
            True
            sage: t.parent()
            Composition Tableaux
            sage: s.parent()
            Composition Tableaux of size 3 and maximum entry 3
            sage: r = CompositionTableaux()(s)
            sage: r.parent()
            Composition Tableaux
        """
    def __call__(self, *cell):
        """
        Return the value in the corresponding cell of ``self``.

        EXAMPLES::

            sage: t = CompositionTableau([[1],[3,2],[4,4]])
            sage: t(1,1)
            2
            sage: t(2,0)
            4
            sage: t(2,2)
            Traceback (most recent call last):
            ...
            IndexError: the cell (2,2) is not contained in [[1], [3, 2], [4, 4]]
        """
    def pp(self) -> None:
        """
        Return a pretty print string of ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1],[3,2],[4,4]]).pp()
            1
            3  2
            4  4
        """
    def size(self):
        """
        Return the number of boxes in ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1],[3,2],[4,4]]).size()
            5
        """
    def weight(self):
        """
        Return a composition where entry `i` is the number of times that `i` appears in
        ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1],[3,2],[4,4]]).weight()
            [1, 1, 1, 2, 0]
        """
    def descent_set(self):
        """
        Return the set of all `i` that do *not* have `i+1` appearing strictly
        to the left of `i` in ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1],[3,2],[4,4]]).descent_set()
            [1, 3]
        """
    def descent_composition(self):
        """
        Return the composition corresponding to the set of all `i` that do
        not have `i+1` appearing strictly to the left of `i` in ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1],[3,2],[4,4]]).descent_composition()
            [1, 2, 2]
        """
    def shape_composition(self):
        """
        Return a Composition object which is the shape of ``self``.

        EXAMPLES::

            sage: CompositionTableau([[1,1],[3,2],[4,4,3]]).shape_composition()
            [2, 2, 3]
            sage: CompositionTableau([[2,1],[3],[4]]).shape_composition()
            [2, 1, 1]
        """
    def shape_partition(self):
        """
        Return a partition which is the shape of ``self`` sorted into weakly
        decreasing order.

        EXAMPLES::

            sage: CompositionTableau([[1,1],[3,2],[4,4,3]]).shape_partition()
            [3, 2, 2]
            sage: CompositionTableau([[2,1],[3],[4]]).shape_partition()
            [2, 1, 1]
        """
    def is_standard(self):
        """
        Return ``True`` if ``self`` is a standard composition tableau and
        ``False`` otherwise.

        EXAMPLES::

            sage: CompositionTableau([[1,1],[3,2],[4,4,3]]).is_standard()
            False
            sage: CompositionTableau([[2,1],[3],[4]]).is_standard()
            True
        """

class CompositionTableaux(UniqueRepresentation, Parent):
    """
    Composition tableaux.

    INPUT:

    - ``size`` -- the size of the composition tableaux
    - ``shape`` -- the shape of the composition tableaux
    - ``max_entry`` -- the maximum entry for the composition tableaux

    The first argument is interpreted as ``size`` or ``shape`` depending on
    whether it is an integer or a composition.

    EXAMPLES::

        sage: CT = CompositionTableaux(3); CT
        Composition Tableaux of size 3 and maximum entry 3
        sage: list(CT)
        [[[1], [2], [3]],
         [[1], [2, 2]],
         [[1], [3, 2]],
         [[1], [3, 3]],
         [[2], [3, 3]],
         [[1, 1], [2]],
         [[1, 1], [3]],
         [[2, 1], [3]],
         [[2, 2], [3]],
         [[1, 1, 1]],
         [[2, 1, 1]],
         [[2, 2, 1]],
         [[2, 2, 2]],
         [[3, 1, 1]],
         [[3, 2, 1]],
         [[3, 2, 2]],
         [[3, 3, 1]],
         [[3, 3, 2]],
         [[3, 3, 3]]]

        sage: CT = CompositionTableaux([1,2,1]); CT
        Composition tableaux of shape [1, 2, 1] and maximum entry 4
        sage: list(CT)
        [[[1], [2, 2], [3]],
         [[1], [2, 2], [4]],
         [[1], [3, 2], [4]],
         [[1], [3, 3], [4]],
         [[2], [3, 3], [4]]]

        sage: CT = CompositionTableaux(shape=[1,2,1],max_entry=3); CT
        Composition tableaux of shape [1, 2, 1] and maximum entry 3
        sage: list(CT)
        [[[1], [2, 2], [3]]]

        sage: CT = CompositionTableaux(2,max_entry=3); CT
        Composition Tableaux of size 2 and maximum entry 3
        sage: list(CT)
        [[[1], [2]],
         [[1], [3]],
         [[2], [3]],
         [[1, 1]],
         [[2, 1]],
         [[2, 2]],
         [[3, 1]],
         [[3, 2]],
         [[3, 3]]]

        sage: CT = CompositionTableaux(0); CT
        Composition Tableaux of size 0 and maximum entry 0
        sage: list(CT)
        [[]]
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        """
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`CompositionTableaux` for
        more information.

        TESTS::

            sage: CT = CompositionTableaux(3); CT
            Composition Tableaux of size 3 and maximum entry 3
            sage: CT = CompositionTableaux(size=3); CT
            Composition Tableaux of size 3 and maximum entry 3
            sage: CT = CompositionTableaux([1,2]); CT
            Composition tableaux of shape [1, 2] and maximum entry 3
            sage: CT = CompositionTableaux(shape=[1,2]); CT
            Composition tableaux of shape [1, 2] and maximum entry 3
            sage: CT = CompositionTableaux(shape=[]); CT
            Composition tableaux of shape [] and maximum entry 0
            sage: CT = CompositionTableaux(0); CT
            Composition Tableaux of size 0 and maximum entry 0
            sage: CT = CompositionTableaux(max_entry=3); CT
            Composition tableaux with maximum entry 3
            sage: CT = CompositionTableaux([1,2],max_entry=3); CT
            Composition tableaux of shape [1, 2] and maximum entry 3
            sage: CT = CompositionTableaux(size=2,shape=[1,2]); CT
            Traceback (most recent call last):
            ...
            ValueError: size and shape are different sizes
        """
    max_entry: Incomplete
    def __init__(self, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: CT = CompositionTableaux()
            sage: TestSuite(CT).run()
        """
    Element = CompositionTableau
    def __contains__(self, T) -> bool:
        """
        Return ``True`` if ``T`` can be interpreted as
        :class:`CompositionTableau`.

        TESTS::

            sage: [[1],[2,2]] in CompositionTableaux(3)
            True
            sage: [[1],[2,2]] in CompositionTableaux(shape=[1,2])
            True
            sage: CompositionTableau([[1],[2,2]]) in CompositionTableaux()
            True
            sage: [[1],[2,2],[2]] in CompositionTableaux()
            False
        """

class CompositionTableaux_all(CompositionTableaux, DisjointUnionEnumeratedSets):
    """
    All composition tableaux.
    """
    max_entry: Incomplete
    def __init__(self, max_entry=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: CT = CompositionTableaux()
            sage: TestSuite(CT).run()
        """
    def an_element(self):
        """
        Return a particular element of ``self``.

        EXAMPLES::

            sage: CT = CompositionTableaux()
            sage: CT.an_element()
            [[1, 1], [2]]
        """

class CompositionTableaux_size(CompositionTableaux):
    """
    Composition tableaux of a fixed size `n`.

    INPUT:

    - ``n`` -- nonnegative integer
    - ``max_entry`` -- nonnegative integer (default: `n`)

    OUTPUT: the class of composition tableaux of size `n`
    """
    size: Incomplete
    def __init__(self, n, max_entry=None) -> None:
        """
        Initialize the class of composition tableaux of size `n`.

        TESTS::

            sage: CT = CompositionTableaux(4)
            sage: TestSuite(CT).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[1],[2,2]] in CompositionTableaux(3)
            True
            sage: [[1],[2,2]] in CompositionTableaux(4)
            False
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [t for t in CompositionTableaux(3)]
            [[[1], [2], [3]],
             [[1], [2, 2]],
             [[1], [3, 2]],
             [[1], [3, 3]],
             [[2], [3, 3]],
             [[1, 1], [2]],
             [[1, 1], [3]],
             [[2, 1], [3]],
             [[2, 2], [3]],
             [[1, 1, 1]],
             [[2, 1, 1]],
             [[2, 2, 1]],
             [[2, 2, 2]],
             [[3, 1, 1]],
             [[3, 2, 1]],
             [[3, 2, 2]],
             [[3, 3, 1]],
             [[3, 3, 2]],
             [[3, 3, 3]]]

            sage: CompositionTableaux(3)[0].parent() is CompositionTableaux(3)
            True
        """

class CompositionTableaux_shape(CompositionTableaux):
    """
    Composition tableaux of a fixed shape ``comp`` with a given max entry.

    INPUT:

    - ``comp`` -- a composition
    - ``max_entry`` -- nonnegative integer (default: size of ``comp``)
    """
    shape: Incomplete
    def __init__(self, comp, max_entry=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: CT = CompositionTableaux([1,2])
            sage: TestSuite(CT).run()

            sage: CT = CompositionTableaux([1,2], max_entry=4)
            sage: TestSuite(CT).run()
        """
    def __iter__(self):
        """
        An iterator for composition tableaux of a given shape.

        EXAMPLES::

            sage: [t for t in CompositionTableaux([1,2])]
            [[[1], [2, 2]], [[1], [3, 2]], [[1], [3, 3]], [[2], [3, 3]]]
            sage: [t for t in CompositionTableaux([1,2],max_entry=4)]
            [[[1], [2, 2]],
             [[1], [3, 2]],
             [[1], [3, 3]],
             [[1], [4, 2]],
             [[1], [4, 3]],
             [[1], [4, 4]],
             [[2], [3, 3]],
             [[2], [4, 3]],
             [[2], [4, 4]],
             [[3], [4, 4]]]
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2],[4,3]] in CompositionTableaux([1,2])
            True
            sage: [[2],[3,2]] in CompositionTableaux([1,2])
            False
        """

class CompositionTableauxBacktracker(GenericBacktracker):
    """
    A backtracker class for generating sets of composition tableaux.
    """
    max_entry: Incomplete
    def __init__(self, shape, max_entry=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.composition_tableau import CompositionTableauxBacktracker
            sage: n = CompositionTableauxBacktracker([1,3,2])
            sage: n._ending_position
            (2, 1)
            sage: n._initial_state
            (0, 0)
        """
    def get_next_pos(self, ii, jj):
        """
        EXAMPLES::

            sage: from sage.combinat.composition_tableau import CompositionTableauxBacktracker
            sage: T = CompositionTableau([[2,1],[5,4,3,2],[6],[7,7,6]])
            sage: n = CompositionTableauxBacktracker(T.shape_composition())
            sage: n.get_next_pos(1,1)
            (1, 2)
        """
