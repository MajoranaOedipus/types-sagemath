from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.shifted_primed_tableau import PrimedEntry as PrimedEntry
from sage.combinat.tableau import SemistandardTableaux as SemistandardTableaux, StandardTableaux as StandardTableaux, Tableau as Tableau, Tableaux as Tableaux
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.parent import Parent as Parent

class SemistandardSuperTableau(Tableau):
    '''
    A semistandard super tableau.

    A semistandard super tableau is a tableau with primed positive integer entries.
    As defined in [Muth2019]_, a semistandard super tableau weakly increases along
    the rows and down the columns. Also, the letters of even parity (unprimed)
    strictly increases down the columns, and letters of oddd parity (primed)
    strictly increases along the rows. Note that Sage uses the English convention
    for partitions and tableaux; the longer rows are displayed on top.

    INPUT:

    - ``t`` -- a tableau, a list of iterables, or an empty list

    EXAMPLES::

        sage: t = SemistandardSuperTableau([[\'1p\',2,"3\'"],[2,3]]); t
        [[1\', 2, 3\'], [2, 3]]
        sage: t.shape()
        [3, 2]
        sage: t.pp() # pretty printing
        1\' 2 3\'
        2 3
        sage: t = Tableau([["1p",2],[2]])
        sage: s = SemistandardSuperTableau(t); s
        [[1\', 2], [2]]
        sage: SemistandardSuperTableau([]) # The empty tableau
        []

    TESTS::

        sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
        sage: t = Tableaux()([[1,1],[2]])
        sage: s = SemistandardSuperTableaux()([[PrimedEntry(1),PrimedEntry(1)],
        ....:                                   [PrimedEntry(2)]])
        sage: s == t
        True
        sage: s.parent()
        Semistandard super tableaux
        sage: r = SemistandardSuperTableaux()(t); r.parent()
        Semistandard super tableaux
        sage: isinstance(r, Tableau)
        True
        sage: s2 = SemistandardSuperTableaux()([[PrimedEntry(1),
        ....:       PrimedEntry(1)], [PrimedEntry(2)]])
        sage: s2 == s
        True
        sage: s2.parent()
        Semistandard super tableaux
    '''
    @staticmethod
    def __classcall_private__(cls, t):
        """
        This ensures that a SemistandardSuperTableau is only ever constructed
        as an element_class call of an appropriate parent.

        TESTS::

            sage: t = SemistandardSuperTableau([[1,1],[2]])
            sage: TestSuite(t).run()
            sage: t.parent()
            Semistandard super tableaux
            sage: t.category()
            Category of elements of Semistandard super tableaux
            sage: type(t)
            <class 'sage.combinat.super_tableau.SemistandardSuperTableaux_all_with_category.element_class'>
        """
    def __init__(self, parent, t, check: bool = True, preprocessed: bool = False) -> None:
        '''
        Initialize a semistandard super tableau for given tableau ``t``.

        TESTS::

            sage: s = SemistandardSuperTableau([[1,"2\'","3\'",3], [2,"3\'"]])
            sage: t = SemistandardSuperTableaux()([[1,"2p","3p",3], [2,"3p"]])
            sage: s == t
            True
            sage: s.parent()
            Semistandard super tableaux
            sage: TestSuite(t).run()
            sage: r = SemistandardSuperTableaux()(s); r.parent()
            Semistandard super tableaux
            sage: s is t  # identical super tableaux are distinct objects
            False
        '''
    def check(self) -> None:
        """
        Check that ``self`` is a valid semistandard super tableau.

        TESTS::

            sage: SemistandardSuperTableau([[1,2,3],[1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the unprimed entries of each column must
            be strictly increasing

            sage: SemistandardSuperTableau([[1,2,1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in each row of a semistandard super
            tableau must be weakly increasing

            sage: SemistandardSuperTableau([[0,1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries of a semistandard super tableau must be
            nonnegative primed integers
        """

class StandardSuperTableau(SemistandardSuperTableau):
    '''
    A standard super tableau.

    A standard super tableau is a semistandard super tableau whose entries
    are in bijection with positive primed integers `1\', 1, 2\' \\ldots n`.

    For more information refer [Muth2019]_.

    INPUT:

    - ``t`` -- a Tableau, a list of iterables, or an empty list

    EXAMPLES::

        sage: t = StandardSuperTableau([["1\'",1,"2\'",2,"3\'"],[3,"4\'"]]); t
        [[1\', 1, 2\', 2, 3\'], [3, 4\']]
        sage: t.shape()
        [5, 2]
        sage: t.pp() # pretty printing
        1\' 1 2\' 2 3\'
        3 4\'
        sage: t.is_standard()
        True
        sage: StandardSuperTableau([]) # The empty tableau
        []

    TESTS::

        sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
        sage: t = Tableaux()([[PrimedEntry(\'1p\'), PrimedEntry(\'2p\')],
        ....:                [PrimedEntry(1)]])
        sage: s = StandardSuperTableaux()([[\'1p\',\'2p\'],[1]])
        sage: s == t
        True
        sage: s.parent()
        Standard super tableaux
        sage: r = StandardSuperTableaux()([]); r.parent()
        Standard super tableaux
        sage: isinstance(r, Tableau)
        True
    '''
    @staticmethod
    def __classcall_private__(self, t):
        """
        This ensures that a :class:`StandardSuperTableau` is only ever
        constructed as an ``element_class`` call of an appropriate parent.

        TESTS::

            sage: t = StandardSuperTableau([['1p','2p'],[1]])
            sage: TestSuite(t).run()
            sage: t.parent()
            Standard super tableaux
            sage: type(t)
            <class 'sage.combinat.super_tableau.StandardSuperTableaux_all_with_category.element_class'>
        """
    def check(self) -> None:
        """
        Check that ``self`` is a standard tableau.

        TESTS::

            sage: StandardSuperTableau([[1,2,3],[4,5]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in a standard tableau must be in
            bijection with 1',1,2',2,...,n

            sage: StandardSuperTableau([[1,3,2]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the entries in each row of a semistandard super
            tableau must be weakly increasing
        """
    def is_standard(self) -> bool:
        """
        Return ``True`` since ``self`` is a standard super tableau.

        EXAMPLES::

            sage: StandardSuperTableau([['1p', 1], ['2p', 2]]).is_standard()
            True
        """

class SemistandardSuperTableaux(SemistandardTableaux):
    """
    The set of semistandard super tableaux.

    A semistandard super tableau is a tableau with primed positive integer entries.
    As defined in [Muth2019]_, a semistandard super tableau weakly increases along
    the rows and down the columns. Also, the letters of even parity (unprimed)
    strictly increases down the columns, and letters of oddd parity (primed)
    strictly increases along the rows. Note that Sage uses the English convention
    for partitions and tableaux; the longer rows are displayed on top.

    EXAMPLES::

        sage: SST = SemistandardSuperTableaux(); SST
        Semistandard super tableaux
    """
    @staticmethod
    def __classcall_private__(cls):
        """
        Normalize and process input to return the correct parent and
        ensure a unique representation.

        TESTS::

            sage: SemistandardSuperTableaux()
            Semistandard super tableaux
        """
    Element = SemistandardSuperTableau
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as a
        :class:`SemistandardSuperTableau`.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: T = sage.combinat.super_tableau.SemistandardSuperTableaux_all()
            sage: [[1,2],[2]] in T
            True
            sage: [[PrimedEntry('1p'),PrimedEntry(2)],[PrimedEntry(2)]] in T
            True
            sage: [] in T
            True
            sage: Tableau([[1]]) in T
            True
            sage: StandardSuperTableau([[1]]) in T
            Traceback (most recent call last):
            ...
            ValueError: the entries in a standard tableau must be in bijection
            with 1',1,2',2,...,n

            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            True
            sage: [[1,3,2]] in T
            False
        """

class SemistandardSuperTableaux_all(SemistandardSuperTableaux):
    """
    All semistandard super tableaux.
    """
    def __init__(self) -> None:
        """
        Initialize the class of all semistandard super tableaux.

        TESTS::

            sage: from sage.combinat.super_tableau import SemistandardSuperTableaux_all
            sage: SST = SemistandardSuperTableaux_all(); SST
            Semistandard super tableaux
        """

class StandardSuperTableaux(SemistandardSuperTableaux, Parent):
    '''
    The set of standard super tableaux.

    A standard super tableau is a tableau whose entries are primed positive
    integers, which are strictly increasing in rows and down columns and
    contains each letters from 1\',1,2\'...n exactly once.

    For more information refer [Muth2019]_.

    INPUT:

    - ``n`` -- a nonnegative integer or a partition

    EXAMPLES::

        sage: SST = StandardSuperTableaux()
        sage: SST
        Standard super tableaux
        sage: SST([["1\'",1,"2\'",2,"3\'"],[3,"4\'"]])
        [[1\', 1, 2\', 2, 3\'], [3, 4\']]
        sage: SST = StandardSuperTableaux(3)
        sage: SST
        Standard super tableaux of size 3
        sage: SST.first()
        [[1\', 1, 2\']]
        sage: SST.last()
        [[1\'], [1], [2\']]
        sage: SST.cardinality()
        4
        sage: SST.list()
        [[[1\', 1, 2\']], [[1\', 2\'], [1]], [[1\', 1], [2\']], [[1\'], [1], [2\']]]
        sage: SST = StandardSuperTableaux([3,2])
        sage: SST
        Standard super tableaux of shape [3, 2]

    TESTS::

        sage: StandardSuperTableaux()([])
        []
        sage: SST = StandardSuperTableaux([3,2]); SST
        Standard super tableaux of shape [3, 2]
        sage: SST.first()
        [[1\', 2\', 3\'], [1, 2]]
        sage: SST.last()
        [[1\', 1, 2\'], [2, 3\']]
        sage: SST.cardinality()
        5
        sage: SST.cardinality() == StandardTableaux([3,2]).cardinality()
        True
        sage: SST.list()
        [[[1\', 2\', 3\'], [1, 2]],
         [[1\', 1, 3\'], [2\', 2]],
         [[1\', 2\', 2], [1, 3\']],
         [[1\', 1, 2], [2\', 3\']],
         [[1\', 1, 2\'], [2, 3\']]]
        sage: TestSuite(SST).run()
    '''
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        This class returns the appropriate parent based on arguments.
        See the documentation for :class:`StandardTableaux` for more
        information.

        TESTS::

            sage: SST = StandardSuperTableaux(); SST
            Standard super tableaux
            sage: StandardSuperTableaux(3)
            Standard super tableaux of size 3
            sage: StandardSuperTableaux([2,2])
            Standard super tableaux of shape [2, 2]
            sage: StandardSuperTableaux(-1)
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a
            partition
            sage: StandardSuperTableaux([[1]])
            Traceback (most recent call last):
            ...
            ValueError: the argument must be a nonnegative integer or a
            partition
        """
    Element = StandardSuperTableau
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``t`` can be interpreted as a
        :class:`StandardSuperTableau`.

        TESTS::

            sage: from sage.combinat.shifted_primed_tableau import PrimedEntry
            sage: T = sage.combinat.super_tableau.StandardSuperTableaux_all()
            sage: [[0.5,1],[1.5]] in T
            True
            sage: [[PrimedEntry('1p'),PrimedEntry('2p')],[PrimedEntry(1)]] in T
            True
            sage: [] in T
            True
            sage: Tableau([['1p']]) in T
            True
            sage: StandardSuperTableau([['1p']]) in T
            True
            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            False
            sage: [[1,3,2]] in T
            False
        """

class StandardSuperTableaux_all(StandardSuperTableaux, DisjointUnionEnumeratedSets):
    """
    All standard super tableaux.
    """
    def __init__(self) -> None:
        """
        Initialize the class of all standard super tableaux.

        TESTS::

            sage: from sage.combinat.super_tableau import StandardSuperTableaux_all
            sage: SST = StandardSuperTableaux_all(); SST
            Standard super tableaux
            sage: TestSuite(SST).run()
        """

class StandardSuperTableaux_size(StandardSuperTableaux, DisjointUnionEnumeratedSets):
    """
    Standard super tableaux of fixed size `n`.

    EXAMPLES::

        sage: [ t for t in StandardSuperTableaux(1) ]
        [[[1']]]
        sage: [ t for t in StandardSuperTableaux(2) ]
        [[[1', 1]], [[1'], [1]]]
        sage: [ t for t in StandardSuperTableaux(3) ]
        [[[1', 1, 2']], [[1', 2'], [1]], [[1', 1], [2']], [[1'], [1], [2']]]
        sage: StandardSuperTableaux(4)[:]
        [[[1', 1, 2', 2]],
         [[1', 2', 2], [1]],
         [[1', 1, 2], [2']],
         [[1', 1, 2'], [2]],
         [[1', 2'], [1, 2]],
         [[1', 1], [2', 2]],
         [[1', 2], [1], [2']],
         [[1', 2'], [1], [2]],
         [[1', 1], [2'], [2]],
         [[1'], [1], [2'], [2]]]
    """
    size: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize the class of all standard super tableaux of size ``n``.

        TESTS::

            sage: TestSuite( StandardSuperTableaux(4) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: SST3 = StandardSuperTableaux(3)
            sage: all(st in SST3 for st in SST3)
            True
            sage: SST4 = StandardSuperTableaux(4)
            sage: [x for x in SST4 if x in SST3]
            []
            sage: 1 in StandardSuperTableaux(4)
            False
        """
    def cardinality(self):
        """
        Return the number of all standard super tableaux of size ``n``.

        The standard super tableaux of size `n` are in bijection with the
        corresponding standard tableaux (under the alphabet relabeling). Refer
        :class:`sage.combinat.tableau.StandardTableaux_size` for more details.

        EXAMPLES::

            sage: StandardSuperTableaux(3).cardinality()
            4
            sage: ns = [1,2,3,4,5,6]
            sage: sts = [StandardSuperTableaux(n) for n in ns]
            sage: all(st.cardinality() == len(st.list()) for st in sts)
            True
            sage: StandardSuperTableaux(50).cardinality()  # long time
            27886995605342342839104615869259776

        TESTS::

            sage: def cardinality_using_hook_formula(n):
            ....:     c = 0
            ....:     for p in Partitions(n):
            ....:         c += StandardSuperTableaux(p).cardinality()
            ....:     return c
            sage: all(cardinality_using_hook_formula(i) ==
            ....:       StandardSuperTableaux(i).cardinality()
            ....:       for i in range(10))
            True
        """

class StandardSuperTableaux_shape(StandardSuperTableaux):
    """
    Standard super tableaux of a fixed shape `p`.
    """
    shape: Incomplete
    def __init__(self, p) -> None:
        """
        Initialize the class of all standard super tableaux of a given shape.

        TESTS::

            sage: TestSuite( StandardSuperTableaux([2,2,1]) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: ST = StandardSuperTableaux([2,1,1])
            sage: all(st in ST for st in ST)
            True
            sage: len([x for x in StandardSuperTableaux(4) if x in ST])
            3
            sage: ST.cardinality()
            3
            sage: 1 in StandardSuperTableaux([2,1,1])
            False
        """
    def cardinality(self):
        """
        Return the number of standard super tableaux of given shape.

        The standard super tableaux of a fixed shape `p` are in bijection with
        the corresponding standard tableaux (under the alphabet relabeling).
        Refer :class:`sage.combinat.tableau.StandardTableaux_shape` for more
        details.

        EXAMPLES::

            sage: StandardSuperTableaux([3,2,1]).cardinality()
            16
            sage: StandardSuperTableaux([2,2]).cardinality()
            2
            sage: StandardSuperTableaux([5]).cardinality()
            1
            sage: StandardSuperTableaux([6,5,5,3]).cardinality()
            6651216
            sage: StandardSuperTableaux([]).cardinality()
            1
        """
    def __iter__(self):
        """
        An iterator for the standard super tableaux associated to the
        shape `p` of ``self``.

        EXAMPLES::

            sage: [t for t in StandardSuperTableaux([2,2])]
            [[[1', 2'], [1, 2]], [[1', 1], [2', 2]]]
            sage: [t for t in StandardSuperTableaux([3,2])]
            [[[1', 2', 3'], [1, 2]],
             [[1', 1, 3'], [2', 2]],
             [[1', 2', 2], [1, 3']],
             [[1', 1, 2], [2', 3']],
             [[1', 1, 2'], [2, 3']]]
            sage: st = StandardSuperTableaux([2,1])
            sage: st[0].parent() is st
            True
        """
