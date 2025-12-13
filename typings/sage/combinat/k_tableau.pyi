from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.composition import Composition as Composition
from sage.combinat.core import Core as Core
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.skew_partition import SkewPartition as SkewPartition
from sage.combinat.skew_tableau import SemistandardSkewTableaux as SemistandardSkewTableaux, SkewTableau as SkewTableau
from sage.combinat.tableau import Tableaux as Tableaux
from sage.functions.generalized import sgn as sgn
from sage.misc.flatten import flatten as flatten
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.list_clone import ClonableList as ClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def WeakTableau(t, k, inner_shape=[], representation: str = 'core'):
    '''
    This is the dispatcher method for the element class of weak `k`-tableaux.

    Standard weak `k`-tableaux correspond to saturated chains in the weak order.
    There are three formulations of weak tableaux, one in terms of cores, one in terms
    of `k`-bounded partitions, and one in terms of factorizations of affine Grassmannian
    elements. For semistandard weak `k`-tableaux, all letters of the same value have to
    satisfy the conditions of a horizontal strip. In the affine Grassmannian formulation this
    means that all factors are cyclically decreasing elements. For more information, see
    for example [LLMSSZ2013]_.

    INPUT:

    - ``t`` -- a weak `k`-tableau in the specified representation:

      - for the \'core\' representation ``t`` is a list of lists where each subtableaux
        should have a `k+1`-core shape; ``None`` is allowed as an entry for skew weak
        `k`-tableaux
      - for the \'bounded\' representation ``t`` is a list of lists where each subtableaux
        should have a `k`-bounded shape; ``None`` is allowed as an entry for skew weak
        `k`-tableaux
      - for the \'factorized_permutation\' representation ``t`` is either a list of
        cyclically decreasing Weyl group elements or a list of reduced words of cyclically
        decreasing Weyl group elements; to indicate a skew tableau in this representation,
        ``inner_shape`` should be the inner shape as a `(k+1)`-core

    - ``k`` -- positive integer

    - ``inner_shape`` -- this entry is only relevant for the \'factorized_permutation\'
      representation and specifies the inner shape in case the tableau is skew
      (default: ``[]``)

    - ``representation`` -- \'core\', \'bounded\', or \'factorized_permutation\'
      (default: ``\'core\'``)

    EXAMPLES:

    Here is an example of a weak 3-tableau in core representation::

        sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
        sage: t.shape()
        [5, 2, 1]
        sage: t.weight()
        (2, 2, 2)
        sage: type(t)
        <class \'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class\'>

    And now we give a skew weak 3-tableau in core representation::

        sage: ts = WeakTableau([[None, 1, 1, 2, 2], [None, 2], [1]], 3)
        sage: ts.shape()
        ([5, 2, 1], [1, 1])
        sage: ts.weight()
        (2, 2)
        sage: type(ts)
        <class \'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class\'>

    Next we create the analogue of the first example in bounded representation::

        sage: tb = WeakTableau([[1,1,2],[2,3],[3]], 3, representation=\'bounded\')
        sage: tb.shape()
        [3, 2, 1]
        sage: tb.weight()
        (2, 2, 2)
        sage: type(tb)
        <class \'sage.combinat.k_tableau.WeakTableaux_bounded_with_category.element_class\'>
        sage: tb.to_core_tableau()
        [[1, 1, 2, 2, 3], [2, 3], [3]]
        sage: t == tb.to_core_tableau()
        True

    And the analogue of the skew example in bounded representation::

        sage: tbs = WeakTableau([[None, 1, 2], [None, 2], [1]], 3, representation = "bounded")
        sage: tbs.shape()
        ([3, 2, 1], [1, 1])
        sage: tbs.weight()
        (2, 2)
        sage: tbs.to_core_tableau()
        [[None, 1, 1, 2, 2], [None, 2], [1]]
        sage: ts.to_bounded_tableau() == tbs
        True

    Finally we do the same examples for the factorized permutation representation::

        sage: tf = WeakTableau([[2,0],[3,2],[1,0]], 3, representation = "factorized_permutation")
        sage: tf.shape()
        [5, 2, 1]
        sage: tf.weight()
        (2, 2, 2)
        sage: type(tf)
        <class \'sage.combinat.k_tableau.WeakTableaux_factorized_permutation_with_category.element_class\'>
        sage: tf.to_core_tableau() == t
        True

        sage: tfs = WeakTableau([[0,3],[2,1]], 3, inner_shape = [1,1], representation = \'factorized_permutation\')
        sage: tfs.shape()
        ([5, 2, 1], [1, 1])
        sage: tfs.weight()
        (2, 2)
        sage: type(tfs)
        <class \'sage.combinat.k_tableau.WeakTableaux_factorized_permutation_with_category.element_class\'>
        sage: tfs.to_core_tableau()
        [[None, 1, 1, 2, 2], [None, 2], [1]]

    Another way to pass from one representation to another is as follows::

        sage: ts
        [[None, 1, 1, 2, 2], [None, 2], [1]]
        sage: ts.parent()._representation
        \'core\'
        sage: ts.representation(\'bounded\')
        [[None, 1, 2], [None, 2], [1]]

    To test whether a given semistandard tableau is a weak `k`-tableau in the bounded representation,
    one can ask::

        sage: t = Tableau([[1,1,2],[2,3],[3]])
        sage: t.is_k_tableau(3)
        True
        sage: t = SkewTableau([[None, 1, 2], [None, 2], [1]])
        sage: t.is_k_tableau(3)
        True
        sage: t = SkewTableau([[None, 1, 1], [None, 2], [2]])
        sage: t.is_k_tableau(3)
        False

    TESTS::

        sage: t = WeakTableau([[2,0],[3,2],[1,0]], 3, representation = "bla")
        Traceback (most recent call last):
        ...
        NotImplementedError: The representation option needs to be \'core\', \'bounded\', or \'factorized_permutation\'
    '''
def WeakTableaux(k, shape, weight, representation: str = 'core'):
    """
    This is the dispatcher method for the parent class of weak `k`-tableaux.

    INPUT:

    - ``k`` -- positive integer
    - ``shape`` -- shape of the weak `k`-tableaux; for the 'core' and
      'factorized_permutation' representation, the shape is inputted as a `(k+1)`-core;
      for the 'bounded' representation, the shape is inputted as a `k`-bounded partition;
      for skew tableaux, the shape is inputted as a tuple of the outer and inner shape
    - ``weight`` -- the weight of the weak `k`-tableaux as a list or tuple
    - ``representation`` -- ``'core'``, ``'bounded'``, or ``'factorized_permutation'`` (default: ``'core'``)

    EXAMPLES::

        sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1])
        sage: T.list()
        [[[1, 3, 4, 5, 6], [2, 6], [4]],
        [[1, 2, 4, 5, 6], [3, 6], [4]],
        [[1, 2, 3, 4, 6], [4, 6], [5]],
        [[1, 2, 3, 4, 5], [4, 5], [6]]]
        sage: T.cardinality()
        4

        sage: T = WeakTableaux(3, [[5,2,1], [2]], [1,1,1,1])
        sage: T.list()
        [[[None, None, 2, 3, 4], [1, 4], [2]],
        [[None, None, 1, 2, 4], [2, 4], [3]],
        [[None, None, 1, 2, 3], [2, 3], [4]]]

        sage: T = WeakTableaux(3, [3,2,1], [1,1,1,1,1,1], representation = 'bounded')
        sage: T.list()
        [[[1, 3, 5], [2, 6], [4]],
        [[1, 2, 5], [3, 6], [4]],
        [[1, 2, 3], [4, 6], [5]],
        [[1, 2, 3], [4, 5], [6]]]

        sage: T = WeakTableaux(3, [[3,2,1], [2]], [1,1,1,1], representation = 'bounded')
        sage: T.list()
        [[[None, None, 3], [1, 4], [2]],
        [[None, None, 1], [2, 4], [3]],
        [[None, None, 1], [2, 3], [4]]]

        sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1], representation = 'factorized_permutation')
        sage: T.list()
        [[s0, s3, s2, s1, s3, s0],
        [s0, s3, s2, s3, s1, s0],
        [s0, s2, s3, s2, s1, s0],
        [s2, s0, s3, s2, s1, s0]]

        sage: T = WeakTableaux(3, [[5,2,1], [2]], [1,1,1,1], representation = 'factorized_permutation')
        sage: T.list()
        [[s0, s3, s2, s3], [s0, s2, s3, s2], [s2, s0, s3, s2]]
    """

class WeakTableau_abstract(ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    Abstract class for the various element classes of WeakTableau.
    """
    def shape(self):
        """
        Return the shape of ``self``.

        When the tableau is straight, the outer shape is returned.
        When the tableau is skew, the tuple of the outer and inner shape is returned.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.shape()
            [5, 2, 1]
            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.shape()
            ([5, 2, 1], [2])

            sage: t = WeakTableau([[1,1,1],[2,2],[3]], 3, representation = 'bounded')
            sage: t.shape()
            [3, 2, 1]
            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.shape()
            ([3, 2, 1], [2])

            sage: t = WeakTableau([[2],[0,3],[2,1,0]], 3, representation = 'factorized_permutation')
            sage: t.shape()
            [5, 2, 1]
            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.shape()
            ([5, 2, 1], [2])
        """
    def weight(self):
        """
        Return the weight of ``self``.

        The weight is a tuple whose `i`-th entry is the number of labels `i` in the
        bounded representation of ``self``.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.weight()
            (2, 2, 2)
            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.weight()
            (1, 1, 1, 1)
            sage: t = WeakTableau([[None,2,3],[3]],2)
            sage: t.weight()
            (0, 1, 1)

            sage: t = WeakTableau([[1,1,1],[2,2],[3]], 3, representation = 'bounded')
            sage: t.weight()
            (3, 2, 1)
            sage: t = WeakTableau([[1,1,2],[2,3],[3]], 3, representation = 'bounded')
            sage: t.weight()
            (2, 2, 2)
            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.weight()
            (1, 1, 1, 1)

            sage: t = WeakTableau([[2],[0,3],[2,1,0]], 3, representation = 'factorized_permutation')
            sage: t.weight()
            (3, 2, 1)
            sage: t = WeakTableau([[2,0],[3,2],[1,0]], 3, representation = 'factorized_permutation')
            sage: t.weight()
            (2, 2, 2)
            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.weight()
            (2, 2)
        """
    def size(self):
        """
        Return the size of the shape of ``self``.

        In the bounded representation, the size of the shape is the number of boxes in the
        outer shape minus the number of boxes in the inner shape. For the core and
        factorized permutation representation, the size is the length of the outer shape
        minus the length of the inner shape.

        .. SEEALSO:: :meth:`sage.combinat.core.Core.length`

        EXAMPLES::

            sage: t = WeakTableau([[None, 1, 1, 2, 2], [None, 2], [1]], 3)
            sage: t.shape()
            ([5, 2, 1], [1, 1])
            sage: t.size()
            4
            sage: t = WeakTableau([[1,1,2],[2,3],[3]], 3, representation='bounded')
            sage: t.shape()
            [3, 2, 1]
            sage: t.size()
            6
        """
    def intermediate_shapes(self):
        """
        Return the intermediate shapes of ``self``.

        A (skew) tableau with letters `1,2,\\ldots,\\ell` can be viewed as a sequence of shapes,
        where the `i`-th shape is given by the shape of the subtableau on letters `1,2,\\ldots,i`.
        The output is the list of these shapes.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: t.intermediate_shapes()
            [[], [2], [4, 1], [5, 2, 1]]

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.intermediate_shapes()
            [[2], [2, 1], [3, 1, 1], [4, 1, 1], [5, 2, 1]]

            sage: t = WeakTableau([[1,1,1],[2,2],[3]], 3, representation = 'bounded')
            sage: t.intermediate_shapes()
            [[], [3], [3, 2], [3, 2, 1]]

            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.intermediate_shapes()
            [[2], [3], [3, 1], [3, 1, 1], [3, 2, 1]]

            sage: t = WeakTableau([[0],[3],[2],[3]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.intermediate_shapes()
            [[2], [2, 1], [3, 1, 1], [4, 1, 1], [5, 2, 1]]
        """
    def pp(self) -> None:
        """
        Return a pretty print string of the tableau.

        EXAMPLES::

            sage: t = WeakTableau([[None, 1, 1, 2, 2], [None, 2], [1]], 3)
            sage: t.pp()
            .  1  1  2  2
            .  2
            1
            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.pp()
            [s2*s0, s3*s2]
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1], representation='core')
            sage: t = T[0]
            sage: hash(t) == hash(t)
            True
            sage: T = WeakTableaux(3, [2,2,1], [1,1,1,1,1], representation='bounded')
            sage: t = T[0]
            sage: hash(t) == hash(t)
            True
            sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1], representation='factorized_permutation')
            sage: t = T[0]
            sage: hash(t) == hash(t)
            True
        """
    def representation(self, representation: str = 'core'):
        """
        Return the analogue of ``self`` in the specified representation.

        INPUT:

        - ``representation`` -- 'core', 'bounded', or 'factorized_permutation' (default: ``'core'``)

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            sage: t.parent()._representation
            'core'
            sage: t.representation('bounded')
            [[1, 1, 2, 4], [2, 3, 5], [3, 4], [5, 6], [6], [7]]
            sage: t.representation('factorized_permutation')
            [s0, s3*s1, s2*s1, s0*s4, s3*s0, s4*s2, s1*s0]

            sage: tb = WeakTableau([[1, 1, 2, 4], [2, 3, 5], [3, 4], [5, 6], [6], [7]], 4, representation = 'bounded')
            sage: tb.parent()._representation
            'bounded'
            sage: tb.representation('core') == t
            True
            sage: tb.representation('factorized_permutation')
            [s0, s3*s1, s2*s1, s0*s4, s3*s0, s4*s2, s1*s0]

            sage: tp = WeakTableau([[0],[3,1],[2,1],[0,4],[3,0],[4,2],[1,0]], 4, representation = 'factorized_permutation')
            sage: tp.parent()._representation
            'factorized_permutation'
            sage: tp.representation('core') == t
            True
            sage: tp.representation('bounded') == tb
            True
        """

class WeakTableaux_abstract(UniqueRepresentation, Parent):
    """
    Abstract class for the various parent classes of WeakTableaux.
    """
    def shape(self):
        """
        Return the shape of the tableaux of ``self``.

        When ``self`` is the class of straight tableaux, the outer shape is returned.
        When ``self`` is the class of skew tableaux, the tuple of the outer and inner
        shape is returned.

        Note that in the 'core' and 'factorized_permutation' representation, the shapes
        are `(k+1)`-cores.  In the 'bounded' representation, the shapes are `k`-bounded
        partitions.

        If the user wants to access the skew shape (even if the inner shape is empty),
        please use ``self._shape``.

        EXAMPLES::

            sage: T = WeakTableaux(3, [5,2,2], [2,2,2,1])
            sage: T.shape()
            [5, 2, 2]
            sage: T._shape
            ([5, 2, 2], [])
            sage: T = WeakTableaux(3, [[5,2,2], [1]], [2,1,2,1])
            sage: T.shape()
            ([5, 2, 2], [1])

            sage: T = WeakTableaux(3, [3,2,2], [2,2,2,1], representation = 'bounded')
            sage: T.shape()
            [3, 2, 2]
            sage: T._shape
            ([3, 2, 2], [])
            sage: T = WeakTableaux(3, [[3,2,2], [1]], [2,1,2,1], representation = 'bounded')
            sage: T.shape()
            ([3, 2, 2], [1])

            sage: T = WeakTableaux(3, [4,1], [2,2], representation = 'factorized_permutation')
            sage: T.shape()
            [4, 1]
            sage: T._shape
            ([4, 1], [])
            sage: T = WeakTableaux(4, [[6,2,1], [2]], [2,1,1,1], representation = 'factorized_permutation')
            sage: T.shape()
            ([6, 2, 1], [2])
        """
    def size(self):
        """
        Return the size of the shape.

        In the bounded representation, the size of the shape is the number of boxes in the
        outer shape minus the number of boxes in the inner shape. For the core and
        factorized permutation representation, the size is the length of the outer shape
        minus the length of the inner shape.

        EXAMPLES::

            sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1])
            sage: T.size()
            6
            sage: T = WeakTableaux(3, [3,2,1], [1,1,1,1,1,1], representation = 'bounded')
            sage: T.size()
            6
            sage: T = WeakTableaux(4, [[6,2,1], [2]], [2,1,1,1], 'factorized_permutation')
            sage: T.size()
            5
        """
    def representation(self, representation: str = 'core'):
        """
        Return the analogue of ``self`` in the specified representation.

        INPUT:

        - ``representation`` -- 'core', 'bounded', or 'factorized_permutation' (default: ``'core'``)

        EXAMPLES::

            sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1])
            sage: T._representation
            'core'
            sage: T.representation('bounded')
            Bounded weak 3-Tableaux of (skew) 3-bounded shape [3, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('factorized_permutation')
            Factorized permutation (skew) weak 3-Tableaux of shape [5, 2, 1] and weight (1, 1, 1, 1, 1, 1)

            sage: T = WeakTableaux(3, [3,2,1], [1,1,1,1,1,1], representation = 'bounded')
            sage: T._representation
            'bounded'
            sage: T.representation('core')
            Core weak 3-Tableaux of (skew) core shape [5, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('bounded')
            Bounded weak 3-Tableaux of (skew) 3-bounded shape [3, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('bounded') == T
            True
            sage: T.representation('factorized_permutation')
            Factorized permutation (skew) weak 3-Tableaux of shape [5, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('factorized_permutation') == T
            False

            sage: T = WeakTableaux(3, [5,2,1], [1,1,1,1,1,1], representation = 'factorized_permutation')
            sage: T._representation
            'factorized_permutation'
            sage: T.representation('core')
            Core weak 3-Tableaux of (skew) core shape [5, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('bounded')
            Bounded weak 3-Tableaux of (skew) 3-bounded shape [3, 2, 1] and weight (1, 1, 1, 1, 1, 1)
            sage: T.representation('factorized_permutation')
            Factorized permutation (skew) weak 3-Tableaux of shape [5, 2, 1] and weight (1, 1, 1, 1, 1, 1)
        """

class WeakTableau_core(WeakTableau_abstract):
    """
    A (skew) weak `k`-tableau represented in terms of `(k+1)`-cores.
    """
    @staticmethod
    def __classcall_private__(cls, t, k):
        """
        Implement the shortcut ``WeakTableau_core(t, k)`` to
        ``WeakTableaux_core(k, shape , weight)(t)`` where ``shape`` is the
        shape of the tableau and ``weight`` is its weight.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_core
            sage: t = WeakTableau_core([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class'>
            sage: TestSuite(t).run()
            sage: t.parent()._skew
            False

            sage: t = WeakTableau_core([[None, None, 1, 1, 2], [1, 2], [2]],3)
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class'>
            sage: TestSuite(t).run()
            sage: t.parent()._skew
            True
        """
    k: Incomplete
    def __init__(self, parent, t) -> None:
        """
        Initialization of weak `k`-tableau ``t`` in core representation.

        INPUT:

        - ``t`` -- weak tableau in core representation; the input is supposed to be a list
          of lists specifying the rows of the tableau;
          ``None`` is allowed as an entry for skew weak `k`-tableaux

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_core, WeakTableaux_core
            sage: T = WeakTableaux_core(3,[5,2,1],[2,2,2])
            sage: t = T([[1, 1, 2, 2, 3], [2, 3], [3]]); t
            [[1, 1, 2, 2, 3], [2, 3], [3]]
            sage: c = WeakTableau_core([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: T = WeakTableaux_core(3,[5,2,1],[2,2,2])
            sage: t = T([[1, 1, 2, 2, 3], [2, 3], [3]]); t
            [[1, 1, 2, 2, 3], [2, 3], [3]]
            sage: c == t
            True
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class'>
            sage: t.parent()
            Core weak 3-Tableaux of (skew) core shape [5, 2, 1] and weight (2, 2, 2)
            sage: TestSuite(t).run()

            sage: t = WeakTableau_core([[None, None, 1, 1, 2], [1, 2], [2]],3);  t
            [[None, None, 1, 1, 2], [1, 2], [2]]
            sage: t.weight()
            (2, 2)
            sage: t.shape()
            ([5, 2, 1], [2])
            sage: TestSuite(t).run()
        """
    def shape_core(self):
        """
        Return the shape of ``self`` as a `(k+1)`-core.

        When the tableau is straight, the outer shape is returned as a core.  When the
        tableau is skew, the tuple of the outer and inner shape is returned as cores.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: t.shape_core()
            [5, 2, 1]

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.shape_core()
            ([5, 2, 1], [2])
        """
    def shape_bounded(self):
        """
        Return the shape of ``self`` as a `k`-bounded partition.

        When the tableau is straight, the outer shape is returned as a `k`-bounded
        partition.  When the tableau is skew, the tuple of the outer and inner shape is
        returned as `k`-bounded partitions.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: t.shape_bounded()
            [3, 2, 1]

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.shape_bounded()
            ([3, 2, 1], [2])
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid weak `k`-tableau.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2], [2]], 2)
            sage: t.check()
            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.check()

        TESTS::

            sage: T = WeakTableaux(2, [3,1], [1,1,1,1])
            sage: t = T([[1,2,3],[3]])
            Traceback (most recent call last):
            ...
            ValueError: The weight of the parent does not agree with the weight of the tableau!

            sage: t = WeakTableau([[1, 2, 2], [1]], 2)
            Traceback (most recent call last):
            ...
            ValueError: The tableau is not semistandard!
        """
    def to_bounded_tableau(self):
        """
        Return the bounded representation of the weak `k`-tableau ``self``.

        Each restricted subtableau of the output is a `k`-bounded partition.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: c = t.to_bounded_tableau(); c
            [[1, 1, 2], [2, 3], [3]]
            sage: type(c)
            <class 'sage.combinat.k_tableau.WeakTableaux_bounded_with_category.element_class'>

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.to_bounded_tableau()
            [[None, None, 3], [1, 4], [2]]
            sage: t.to_bounded_tableau().to_core_tableau() == t
            True
        """
    def to_factorized_permutation_tableau(self):
        """
        Return the factorized permutation representation of the weak `k`-tableau ``self``.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: c = t.to_factorized_permutation_tableau(); c
            [s2*s0, s3*s2, s1*s0]
            sage: type(c)
            <class 'sage.combinat.k_tableau.WeakTableaux_factorized_permutation_with_category.element_class'>
            sage: c.to_core_tableau() == t
            True

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: c = t.to_factorized_permutation_tableau(); c
            [s0, s3, s2, s3]
            sage: c._inner_shape
            [2]
            sage: c.to_core_tableau() == t
            True

        TESTS::

            sage: t = WeakTableau([], 4)
            sage: c = t.to_factorized_permutation_tableau(); c
            [1]
            sage: c._inner_shape
            []
            sage: c.to_core_tableau() == t
            True
        """
    def residues_of_entries(self, v):
        """
        Return a list of residues of cells of weak `k`-tableau ``self`` labeled by ``v``.

        INPUT:

        - ``v`` -- a label of a cell in ``self``

        OUTPUT: list of residues

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: t.residues_of_entries(1)
            [0, 1]

            sage: t = WeakTableau([[None, None, 1, 1, 4], [1, 4], [3]], 3)
            sage: t.residues_of_entries(1)
            [2, 3]
        """
    def dictionary_of_coordinates_at_residues(self, v):
        """
        Return a dictionary assigning to all residues of ``self`` with label ``v`` a list
        of cells with the given residue.

        INPUT:

        - ``v`` -- a label of a cell in ``self``

        OUTPUT: dictionary assigning coordinates in ``self`` to residues

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            sage: t.dictionary_of_coordinates_at_residues(3)
            {0: [(0, 4), (1, 1)], 2: [(2, 0)]}

            sage: t = WeakTableau([[None, None, 1, 1, 4], [1, 4], [3]], 3)
            sage: t.dictionary_of_coordinates_at_residues(1)
            {2: [(0, 2)], 3: [(0, 3), (1, 0)]}

            sage: t = WeakTableau([], 3)
            sage: t.dictionary_of_coordinates_at_residues(1)
            {}
        """
    def list_of_standard_cells(self):
        """
        Return a list of lists of the coordinates of the standard cells of ``self``.

        INPUT:

        - ``self`` -- a weak `k`-tableau in core representation with partition weight

        OUTPUT: list of lists of coordinates

        .. WARNING::

            This method currently only works for straight weak tableaux with partition
            weight.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.list_of_standard_cells()
            [[(0, 1), (1, 0), (2, 0)], [(0, 0), (0, 2), (1, 1)]]
            sage: t = WeakTableau([[1, 1, 1, 2], [2, 2, 3]], 5)
            sage: t.list_of_standard_cells()
            [[(0, 2), (1, 1), (1, 2)], [(0, 1), (1, 0)], [(0, 0), (0, 3)]]
            sage: t = WeakTableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            sage: t.list_of_standard_cells()
            [[(0, 1), (1, 0), (2, 0), (0, 5), (3, 0), (4, 0), (5, 0)], [(0, 0), (0, 2), (1, 1), (2, 1), (1, 2), (3, 1)]]

        TESTS::

            sage: t = WeakTableau([],3)
            sage: t.list_of_standard_cells()
            []

            sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            sage: t.list_of_standard_cells()
            Traceback (most recent call last):
            ...
            ValueError: This method only works for straight tableaux!

            sage: t = WeakTableau([[1,2],[2]], 3)
            sage: t.list_of_standard_cells()
            Traceback (most recent call last):
            ...
            ValueError: This method only works for weak tableaux with partition weight!
        """
    def k_charge(self, algorithm: str = 'I'):
        '''
        Return the `k`-charge of ``self``.

        INPUT:

        - ``algorithm`` -- (default: ``\'I\'``) if "I", computes `k`-charge using the `I`
          algorithm, otherwise uses the `J`-algorithm

        OUTPUT: nonnegative integer

        For the definition of `k`-charge and the various algorithms to compute it see
        Section 3.3 of [LLMSSZ2013]_.

        .. SEEALSO:: :meth:`k_charge_I` and :meth:`k_charge_J`

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.k_charge()
            2
            sage: t = WeakTableau([[1, 3, 4, 5, 6], [2, 6], [4]], 3)
            sage: t.k_charge()
            8
            sage: t = WeakTableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            sage: t.k_charge()
            12

        TESTS::

            sage: T = WeakTableaux(4, [13,9,5,3,2,1,1], [4,3,3,2,2,1,1,1])
            sage: T.cardinality()
            6
            sage: all(t.k_charge_I() == t.k_charge_J() for t in T)
            True
        '''
    def k_charge_I(self):
        """
        Return the `k`-charge of ``self`` using the `I`-algorithm.

        For the definition of `k`-charge and the `I`-algorithm see Section 3.3 of [LLMSSZ2013]_.

        OUTPUT: nonnegative integer

        .. SEEALSO:: :meth:`k_charge` and :meth:`k_charge_J`

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.k_charge_I()
            2
            sage: t = WeakTableau([[1, 3, 4, 5, 6], [2, 6], [4]], 3)
            sage: t.k_charge_I()
            8
            sage: t = WeakTableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            sage: t.k_charge_I()
            12

        TESTS::

            sage: t = WeakTableau([[None, None, 1, 1, 4], [1, 4], [3]], 3)
            sage: t.k_charge_I()
            Traceback (most recent call last):
            ...
            ValueError: k-charge is not defined for skew weak tableaux
        """
    def k_charge_J(self):
        """
        Return the `k`-charge of ``self`` using the `J`-algorithm.

        For the definition of `k`-charge and the `J`-algorithm see Section 3.3 of [LLMSSZ2013]_.

        OUTPUT: nonnegative integer

        .. SEEALSO:: :meth:`k_charge` and :meth:`k_charge_I`

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            sage: t.k_charge_J()
            2
            sage: t = WeakTableau([[1, 3, 4, 5, 6], [2, 6], [4]], 3)
            sage: t.k_charge_J()
            8
            sage: t = WeakTableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            sage: t.k_charge_J()
            12

        TESTS::

            sage: t = WeakTableau([[None, None, 1, 1, 4], [1, 4], [3]], 3)
            sage: t.k_charge_I()
            Traceback (most recent call last):
            ...
            ValueError: k-charge is not defined for skew weak tableaux

            sage: t = WeakTableau([[1, 1, 2, 3], [2, 4, 4], [3, 6], [5]], 4, representation='bounded')
            sage: t.k_charge() == t.k_charge(algorithm = 'J')
            True
        """

class WeakTableaux_core(WeakTableaux_abstract):
    """
    The class of (skew) weak `k`-tableaux in the core representation of shape ``shape``
    (as `k+1`-core) and weight ``weight``.

    INPUT:

    - ``k`` -- positive integer
    - ``shape`` -- the shape of the `k`-tableaux represented as a `(k+1)`-core; if the
      tableaux are skew, the shape is a tuple of the outer and inner shape (both as
      `(k+1)`-cores)
    - ``weight`` -- the weight of the `k`-tableaux

    EXAMPLES::

        sage: T = WeakTableaux(3, [4,1], [2,2])
        sage: T.list()
        [[[1, 1, 2, 2], [2]]]

        sage: T = WeakTableaux(3, [[5,2,1], [2]], [1,1,1,1])
        sage: T.list()
        [[[None, None, 2, 3, 4], [1, 4], [2]],
        [[None, None, 1, 2, 4], [2, 4], [3]],
        [[None, None, 1, 2, 3], [2, 3], [4]]]
    """
    @staticmethod
    def __classcall_private__(cls, k, shape, weight):
        """
        Straighten arguments before unique representation.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_core
            sage: T = WeakTableaux_core(3, [2,1], [1,1,1])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_core(3, [[5,2,1], [2]], [1,1,1,1])
            sage: TestSuite(T).run()
        """
    k: Incomplete
    def __init__(self, k, shape, weight) -> None:
        """
        Initialize the parent class of (skew) weak `k`-tableaux in core representation.

        INPUT:

        - ``k`` -- positive integer
        - ``outer_shape`` -- the outer shape of the `k`-tableaux represented as a
          `(k+1)`-core
        - ``weight`` -- the weight of the `k`-tableaux
        - ``inner_shape`` -- the inner shape of the skew `k`-tableaux represented as a
          `(k+1)`-core;  for straight tableaux the inner shape does not need to be
          specified (default: ``[]``)

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_core
            sage: T = WeakTableaux_core(3, [4,1], [2,2])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_core(3, [[5,2,1], [2]], [1,1,1,1])
            sage: TestSuite(T).run()
        """
    def __iter__(self):
        """
        TESTS::

            sage: T = WeakTableaux(3, [4,1], [2,2])
            sage: T.list()
            [[[1, 1, 2, 2], [2]]]
            sage: T = WeakTableaux(3, [5,2,2], [2,2,2,1])
            sage: T.list()
            [[[1, 1, 3, 3, 4], [2, 2], [3, 3]], [[1, 1, 2, 2, 3], [2, 3], [3, 4]]]
            sage: T = WeakTableaux(3, [[5,2,2], [1]], [2,1,2,1])
            sage: T.list()
            [[[None, 1, 3, 3, 4], [1, 2], [3, 3]],
            [[None, 1, 2, 3, 3], [1, 3], [2, 4]],
            [[None, 1, 1, 2, 3], [2, 3], [3, 4]]]
        """
    def diag(self, c, ha):
        """
        Return the number of diagonals strictly between cells ``c`` and ``ha`` of the same residue as ``c``.

        INPUT:

        - ``c`` -- a cell in the lattice
        - ``ha`` -- another cell in the lattice with bigger row and smaller column than `c`

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: T = WeakTableaux(4, [5,2,2], [2,2,2,1])
            sage: T.diag((1,2),(4,0))
            0
        """
    def circular_distance(self, cr, r):
        """
        Return the shortest counterclockwise distance between ``cr`` and ``r`` modulo `k+1`.

        INPUT:

        - ``cr``, ``r`` -- nonnegative integers between `0` and `k`

        OUTPUT: positive integer

        EXAMPLES::

            sage: T = WeakTableaux(10, [], [])
            sage: T.circular_distance(8, 6)
            2
            sage: T.circular_distance(8, 8)
            0
            sage: T.circular_distance(8, 9)
            10
        """
    Element = WeakTableau_core

class WeakTableau_bounded(WeakTableau_abstract):
    """
    A (skew) weak `k`-tableau represented in terms of `k`-bounded partitions.
    """
    @staticmethod
    def __classcall_private__(cls, t, k):
        """
        Implement the shortcut ``WeakTableau_bounded(t, k)`` to
        ``WeakTableaux_bounded(k, shape, weight)(t)`` where ``shape`` is the
        shape of the tableau and ``weight`` is its weight.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_bounded
            sage: t = WeakTableau_bounded([[1,1,2],[2,3],[3]],3)
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_bounded_with_category.element_class'>
            sage: TestSuite(t).run()
            sage: t.parent()._skew
            False

            sage: t = WeakTableau_bounded([[None, None, 1], [1, 2], [2]], 3)
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_bounded_with_category.element_class'>
            sage: TestSuite(t).run()
            sage: t.parent()._skew
            True
        """
    k: Incomplete
    def __init__(self, parent, t) -> None:
        """
        Initialization of (skew) weak `k`-tableau ``t`` in `k`-bounded representation.

        INPUT:

        - ``t`` -- weak tableau in `k`-bounded representation; the input is supposed to be
          a list of iterables specifying the rows of the tableau;  ``None`` is allowed as an
          entry for skew weak `k`-tableaux

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_bounded, WeakTableaux_bounded
            sage: c = WeakTableau_bounded([[1,1,2],[2,3],[3]],3)
            sage: T = WeakTableaux_bounded(3,[3,2,1],[2,2,2])
            sage: t = T([[1,1,2],[2,3],[3]]); t
            [[1, 1, 2], [2, 3], [3]]
            sage: c == t
            True
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_bounded_with_category.element_class'>
            sage: t.parent()
            Bounded weak 3-Tableaux of (skew) 3-bounded shape [3, 2, 1] and weight (2, 2, 2)
            sage: TestSuite(t).run()

            sage: t = WeakTableau_bounded([[None, None, 1], [2, 4], [3]], 3)
            sage: t.shape()
            ([3, 2, 1], [2])
            sage: t.weight()
            (1, 1, 1, 1)
            sage: TestSuite(t).run()

            sage: t = T([[1,1,3],[2,2],[3]])
            Traceback (most recent call last):
            ...
            ValueError: This is not a proper weak 3-tableau
        """
    def shape_core(self):
        """
        Return the shape of ``self`` as `(k+1)`-core.

        When the tableau is straight, the outer shape is returned as a `(k+1)`-core.
        When the tableau is skew, the tuple of the outer and inner shape is returned as
        `(k+1)`-cores.

        EXAMPLES::

            sage: t = WeakTableau([[1,1,1],[2,2],[3]], 3, representation = 'bounded')
            sage: t.shape_core()
            [5, 2, 1]

            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.shape_core()
            ([5, 2, 1], [2])
        """
    def shape_bounded(self):
        """
        Return the shape of ``self`` as `k`-bounded partition.

        When the tableau is straight, the outer shape is returned as a `k`-bounded
        partition.  When the tableau is skew, the tuple of the outer and inner shape is
        returned as `k`-bounded partitions.

        EXAMPLES::

            sage: t = WeakTableau([[1,1,1],[2,2],[3]], 3, representation = 'bounded')
            sage: t.shape_bounded()
            [3, 2, 1]

            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.shape_bounded()
            ([3, 2, 1], [2])
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid weak `k`-tableau.

        EXAMPLES::

            sage: t = WeakTableau([[1,1],[2]], 2, representation = 'bounded')
            sage: t.check()

            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.check()

        TESTS::

            sage: t = WeakTableau([[1,1,3],[2,2],[3]], 3, representation = 'bounded')
            Traceback (most recent call last):
            ...
            ValueError: This is not a proper weak 3-tableau

            sage: T = WeakTableaux(3, [3,1], [2,1], representation = 'bounded')
            sage: t = T([[None, 1,1], [2]])
            Traceback (most recent call last):
            ...
            ValueError: The inner shape of the parent does not agree with the inner shape of the tableau!

            sage: t = WeakTableau([[1,1],[1]], 3, representation = 'bounded')
            Traceback (most recent call last):
            ...
            ValueError: The tableaux is not semistandard!
        """
    def to_core_tableau(self):
        """
        Return the weak `k`-tableau ``self`` where the shape of each restricted tableau is a `(k+1)`-core.

        EXAMPLES::

            sage: t = WeakTableau([[1,1,2,4],[2,3,5],[3,4],[5,6],[6],[7]], 4, representation = 'bounded')
            sage: c = t.to_core_tableau(); c
            [[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]]
            sage: type(c)
            <class 'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class'>
            sage: t = WeakTableau([], 4, representation = 'bounded')
            sage: t.to_core_tableau()
            []

            sage: from sage.combinat.k_tableau import WeakTableau_bounded
            sage: t = WeakTableau([[1,1,2],[2,3],[3]], 3, representation = 'bounded')
            sage: WeakTableau_bounded.from_core_tableau(t.to_core_tableau(),3)
            [[1, 1, 2], [2, 3], [3]]
            sage: t == WeakTableau_bounded.from_core_tableau(t.to_core_tableau(),3)
            True

            sage: t = WeakTableau([[None, None, 1], [2, 4], [3]], 3, representation = 'bounded')
            sage: t.to_core_tableau()
            [[None, None, 1, 2, 4], [2, 4], [3]]
            sage: t == WeakTableau_bounded.from_core_tableau(t.to_core_tableau(),3)
            True
        """
    @classmethod
    def from_core_tableau(cls, t, k):
        """
        Construct weak `k`-bounded tableau from in `k`-core tableau.

        EXAMPLES::

            sage: from sage.combinat.k_tableau import WeakTableau_bounded
            sage: WeakTableau_bounded.from_core_tableau([[1, 1, 2, 2, 3], [2, 3], [3]], 3)
            [[1, 1, 2], [2, 3], [3]]

            sage: WeakTableau_bounded.from_core_tableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
            [[None, None, 3], [1, 4], [2]]

            sage: WeakTableau_bounded.from_core_tableau([[None,2,3],[3]], 2)
            [[None, 2], [3]]
        """
    def k_charge(self, algorithm: str = 'I'):
        '''
        Return the `k`-charge of ``self``.

        INPUT:

        - ``algorithm`` -- (default: ``\'I\'``) if "I", computes `k`-charge using the `I`
          algorithm, otherwise uses the `J`-algorithm

        OUTPUT: nonnegative integer

        For the definition of `k`-charge and the various algorithms to compute it see Section 3.3 of [LLMSSZ2013]_.

        EXAMPLES::

            sage: t = WeakTableau([[1, 1, 2], [2, 3], [3]], 3, representation = \'bounded\')
            sage: t.k_charge()
            2
            sage: t = WeakTableau([[1, 3, 5], [2, 6], [4]], 3, representation = \'bounded\')
            sage: t.k_charge()
            8
            sage: t = WeakTableau([[1, 1, 2, 4], [2, 3, 5], [3, 4], [5, 6], [6], [7]], 4, representation = \'bounded\')
            sage: t.k_charge()
            12
        '''

class WeakTableaux_bounded(WeakTableaux_abstract):
    """
    The class of (skew) weak `k`-tableaux in the bounded representation of shape ``shape``
    (as `k`-bounded partition or tuple of `k`-bounded partitions in the skew case) and
    weight ``weight``.

    INPUT:

    - ``k`` -- positive integer
    - ``shape`` -- the shape of the `k`-tableaux represented as a `k`-bounded partition;
      if the tableaux are skew, the shape is a tuple of the outer and inner shape each
      represented as a `k`-bounded partition
    - ``weight`` -- the weight of the `k`-tableaux

    EXAMPLES::

        sage: T = WeakTableaux(3, [3,1], [2,2], representation = 'bounded')
        sage: T.list()
        [[[1, 1, 2], [2]]]

        sage: T = WeakTableaux(3, [[3,2,1], [2]], [1,1,1,1], representation = 'bounded')
        sage: T.list()
        [[[None, None, 3], [1, 4], [2]],
        [[None, None, 1], [2, 4], [3]],
        [[None, None, 1], [2, 3], [4]]]
    """
    @staticmethod
    def __classcall_private__(cls, k, shape, weight):
        """
        Straighten arguments before unique representation.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_bounded
            sage: T = WeakTableaux_bounded(3, [2,1], [1,1,1])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_bounded(3, [[3,2,1], [2]], [1,1,1,1])
            sage: TestSuite(T).run()
        """
    k: Incomplete
    def __init__(self, k, shape, weight) -> None:
        """
        Initialize the parent class of (skew) weak `k`-tableaux in bounded representation.

        INPUT:

        - ``k`` -- positive integer
        - ``shape`` -- the shape of the `k`-tableaux represented as a `k`-bounded
          partition; if the tableaux are skew, the shape is a tuple of the outer and inner
          shape each represented as a `k`-bounded partition
        - ``weight`` -- the weight of the `k`-tableaux

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_bounded
            sage: T = WeakTableaux_bounded(3, [3,1], [2,2])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_bounded(3, [[3,2,1], [2]], [1,1,1,1])
            sage: TestSuite(T).run()
        """
    def __iter__(self):
        """
        TESTS::

            sage: T = WeakTableaux(3, [3,1], [2,2], representation = 'bounded')
            sage: T.list()
            [[[1, 1, 2], [2]]]
            sage: T = WeakTableaux(3, [3,2,2], [2,2,2,1], representation = 'bounded')
            sage: T.list()
            [[[1, 1, 4], [2, 2], [3, 3]], [[1, 1, 2], [2, 3], [3, 4]]]
            sage: T = WeakTableaux(3, [[3,2,2], [1]], [2,1,2,1], representation = 'bounded')
            sage: T.list()
            [[[None, 1, 4], [1, 2], [3, 3]],
            [[None, 1, 3], [1, 3], [2, 4]],
            [[None, 1, 1], [2, 3], [3, 4]]]
        """
    Element = WeakTableau_bounded

class WeakTableau_factorized_permutation(WeakTableau_abstract):
    """
    A weak (skew) `k`-tableau represented in terms of factorizations of affine
    permutations into cyclically decreasing elements.
    """
    @staticmethod
    def straighten_input(t, k):
        """
        Straightens input.

        INPUT:

        - ``t`` -- list of reduced words or a list of elements in the Weyl group of type
          `A_k^{(1)}`
        - ``k`` -- positive integer

        EXAMPLES::

            sage: from sage.combinat.k_tableau import WeakTableau_factorized_permutation
            sage: WeakTableau_factorized_permutation.straighten_input([[2,0],[3,2],[1,0]], 3)
            (s2*s0, s3*s2, s1*s0)
            sage: W = WeylGroup(['A',4,1])
            sage: WeakTableau_factorized_permutation.straighten_input([W.an_element(),W.an_element()], 4)
            (s0*s1*s2*s3*s4, s0*s1*s2*s3*s4)

        TESTS::

            sage: WeakTableau_factorized_permutation.straighten_input([W.an_element(),W.an_element()], 3)
            Traceback (most recent call last):
            ...
            ValueError: inconsistent number of rows: should be 4 but got 5
        """
    @staticmethod
    def __classcall_private__(cls, t, k, inner_shape=[]):
        """
        Implement the shortcut ``WeakTableau_factorized_permutation(t, k)`` to
        ``WeakTableaux_factorized_permutation(k, shape, weight)(t)``
        where ``shape`` is the shape of the tableau as a `(k+1)`-core (or a tuple of
        `(k+1)`-cores if the tableau is skew) and ``weight`` is its weight.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_factorized_permutation
            sage: t = WeakTableau_factorized_permutation([[2,0],[3,2],[1,0]], 3)
            sage: t.check()
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_factorized_permutation_with_category.element_class'>
            sage: TestSuite(t).run()

            sage: t = WeakTableau_factorized_permutation([[0,3],[2,1]], 3, inner_shape = [1,1])
            sage: t.check()
            sage: TestSuite(t).run()

            sage: t = WeakTableau_factorized_permutation([], 3); t
            [1]
            sage: t.check()
            sage: TestSuite(t).run()
        """
    k: Incomplete
    def __init__(self, parent, t) -> None:
        """
        Initialization of (skew) weak `k`-tableau ``t`` in factorized permutation representation.

        INPUT:

        - ``t`` -- (skew) weak tableau in factorized permutation representation; the input
          can either be a list of reduced words of cyclically decreasing elements, or a
          list of cyclically decreasing elements;  when the tableau is skew, the inner
          shape needs to be specified as a `(k+1)`-core

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableau_factorized_permutation, WeakTableaux_factorized_permutation
            sage: c = WeakTableau_factorized_permutation([[2,0],[3,2],[1,0]], 3)
            sage: T = WeakTableaux_factorized_permutation(3, [5,2,1],[2,2,2])
            sage: t = T([[2,0],[3,2],[1,0]]); t
            [s2*s0, s3*s2, s1*s0]
            sage: c == t
            True
            sage: type(t)
            <class 'sage.combinat.k_tableau.WeakTableaux_factorized_permutation_with_category.element_class'>
            sage: t.parent()
            Factorized permutation (skew) weak 3-Tableaux of shape [5, 2, 1] and weight (2, 2, 2)
            sage: TestSuite(t).run()

            sage: t = WeakTableau_factorized_permutation([[2,0],[3,2]], 3, inner_shape = [2]); t
            [s2*s0, s3*s2]
            sage: t._inner_shape
            [2]
            sage: t.weight()
            (2, 2)
            sage: t.shape()
            ([5, 2, 1], [2])
            sage: TestSuite(t).run()

            sage: t = T([[3,0],[0,3],[1,0]])
            Traceback (most recent call last):
            ...
            ValueError: The outer shape of the parent does not agree with the outer shape of the tableau!

            sage: t = WeakTableau_factorized_permutation([], 3); t
            [1]
            sage: t.parent()._outer_shape
            []
            sage: t.parent()._weight
            (0,)
        """
    def shape_core(self):
        """
        Return the shape of ``self`` as a `(k+1)`-core.

        When the tableau is straight, the outer shape is returned as a core.
        When the tableau is skew, the tuple of the outer and inner shape is returned as
        cores.

        EXAMPLES::

            sage: t = WeakTableau([[2],[0,3],[2,1,0]], 3, representation = 'factorized_permutation')
            sage: t.shape_core()
            [5, 2, 1]

            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.shape()
            ([5, 2, 1], [2])
        """
    def shape_bounded(self):
        """
        Return the shape of ``self`` as a `k`-bounded partition.

        When the tableau is straight, the outer shape is returned as a `k`-bounded
        partition.  When the tableau is skew, the tuple of the outer and inner shape is
        returned as `k`-bounded partitions.

        EXAMPLES::

            sage: t = WeakTableau([[2],[0,3],[2,1,0]], 3, representation = 'factorized_permutation')
            sage: t.shape_bounded()
            [3, 2, 1]

            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.shape_bounded()
            ([3, 2, 1], [2])
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid weak `k`-tableau.

        EXAMPLES::

            sage: t = WeakTableau([[2],[0,3],[2,1,0]], 3, representation = 'factorized_permutation')
            sage: t.check()

        TESTS::

            sage: t = WeakTableau([[2,0],[3,2]], 3, representation = 'factorized_permutation')
            Traceback (most recent call last):
            ...
            ValueError: this only works on type 'A' affine Grassmannian elements

            sage: T = WeakTableaux(3, [4,1], [2,1], representation = 'factorized_permutation')
            sage: t = T([[2],[1],[0]])
            Traceback (most recent call last):
            ...
            ValueError: The weight of the parent does not agree with the weight of the tableau!
        """
    def to_core_tableau(self):
        """
        Return the weak `k`-tableau ``self`` where the shape of each restricted tableau is a `(k+1)`-core.

        EXAMPLES::

            sage: t = WeakTableau([[0], [3,1], [2,1], [0,4], [3,0], [4,2], [1,0]], 4, representation = 'factorized_permutation'); t
            [s0, s3*s1, s2*s1, s0*s4, s3*s0, s4*s2, s1*s0]
            sage: c = t.to_core_tableau(); c
            [[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]]
            sage: type(c)
            <class 'sage.combinat.k_tableau.WeakTableaux_core_with_category.element_class'>
            sage: t = WeakTableau([[]], 4, representation = 'factorized_permutation'); t
            [1]
            sage: t.to_core_tableau()
            []

            sage: from sage.combinat.k_tableau import WeakTableau_factorized_permutation
            sage: t = WeakTableau([[2,0],[3,2],[1,0]], 3, representation = 'factorized_permutation')
            sage: WeakTableau_factorized_permutation.from_core_tableau(t.to_core_tableau(), 3)
            [s2*s0, s3*s2, s1*s0]
            sage: t == WeakTableau_factorized_permutation.from_core_tableau(t.to_core_tableau(), 3)
            True

            sage: t = WeakTableau([[2,0],[3,2]], 3, inner_shape = [2], representation = 'factorized_permutation')
            sage: t.to_core_tableau()
            [[None, None, 1, 1, 2], [1, 2], [2]]
            sage: t == WeakTableau_factorized_permutation.from_core_tableau(t.to_core_tableau(), 3)
            True
        """
    @classmethod
    def from_core_tableau(cls, t, k):
        """
        Construct weak factorized affine permutation tableau from a `k`-core tableau.

        EXAMPLES::

            sage: from sage.combinat.k_tableau import WeakTableau_factorized_permutation
            sage: WeakTableau_factorized_permutation.from_core_tableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
            [s2*s0, s3*s2, s1*s0]
            sage: WeakTableau_factorized_permutation.from_core_tableau([[1, 1, 2, 3, 4, 4, 5, 5, 6], [2, 3, 5, 5, 6], [3, 4, 7], [5, 6], [6], [7]], 4)
            [s0, s3*s1, s2*s1, s0*s4, s3*s0, s4*s2, s1*s0]
            sage: WeakTableau_factorized_permutation.from_core_tableau([[None, 1, 1, 2, 2], [None, 2], [1]], 3)
            [s0*s3, s2*s1]
        """
    def k_charge(self, algorithm: str = 'I'):
        """
        Return the `k`-charge of ``self``.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: t = WeakTableau([[2,0],[3,2],[1,0]], 3, representation = 'factorized_permutation')
            sage: t.k_charge()
            2
            sage: t = WeakTableau([[0],[3],[2],[1],[3],[0]], 3, representation = 'factorized_permutation')
            sage: t.k_charge()
            8
            sage: t = WeakTableau([[0],[3,1],[2,1],[0,4],[3,0],[4,2],[1,0]], 4, representation = 'factorized_permutation')
            sage: t.k_charge()
            12
        """

class WeakTableaux_factorized_permutation(WeakTableaux_abstract):
    """
    The class of (skew) weak `k`-tableaux in the factorized permutation representation of shape ``shape`` (as `k+1`-core
    or tuple of `(k+1)`-cores in the skew case) and weight ``weight``.

    INPUT:

    - ``k`` -- positive integer
    - ``shape`` -- the shape of the `k`-tableaux represented as a `(k+1)`-core;
      in the skew case the shape is a tuple of the outer and inner shape both as `(k+1)`-cores
    - ``weight`` -- the weight of the `k`-tableaux

    EXAMPLES::

        sage: T = WeakTableaux(3, [4,1], [2,2], representation = 'factorized_permutation')
        sage: T.list()
        [[s3*s2, s1*s0]]

        sage: T = WeakTableaux(4, [[6,2,1], [2]], [2,1,1,1], representation = 'factorized_permutation')
        sage: T.list()
        [[s0, s4, s3, s4*s2], [s0, s3, s4, s3*s2], [s3, s0, s4, s3*s2]]
    """
    @staticmethod
    def __classcall_private__(cls, k, shape, weight):
        """
        Straighten arguments before unique representation.

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_factorized_permutation
            sage: T = WeakTableaux_factorized_permutation(3, [2,1], [1,1,1])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_factorized_permutation(4, [[6,2,1], [2]], [2,1,1,1])
            sage: TestSuite(T).run() # long time
        """
    k: Incomplete
    def __init__(self, k, shape, weight) -> None:
        """
        Initialize the parent class of weak `k`-tableaux in factorized permutation representation.

        INPUT:

        - ``k`` -- positive integer
        - ``shape`` -- the shape of the `k`-tableaux represented as a `(k+1)`-core;
          in the skew case the shape is a tuple of the outer and inner shape both as
          `(k+1)`-cores
        - ``weight`` -- the weight of the `k`-tableaux

        TESTS::

            sage: from sage.combinat.k_tableau import WeakTableaux_factorized_permutation
            sage: T = WeakTableaux_factorized_permutation(3, [4,1], [2,2])
            sage: TestSuite(T).run()
            sage: T = WeakTableaux_factorized_permutation(4, [[6,2,1], [2]], [2,1,1,1])
            sage: TestSuite(T).run() # long time
        """
    def __iter__(self):
        """
        TESTS::

            sage: T = WeakTableaux(3, [4,1], [2,2], representation = 'factorized_permutation')
            sage: T.list()
            [[s3*s2, s1*s0]]
            sage: T = WeakTableaux(3, [5,2,2], [2,2,2,1], representation = 'factorized_permutation')
            sage: T.list()
            [[s0, s3*s2, s0*s3, s1*s0], [s3, s2*s0, s3*s2, s1*s0]]
            sage: T = WeakTableaux(4, [[6,2,1], [2]], [2,1,1,1], representation = 'factorized_permutation')
            sage: T.list()
            [[s0, s4, s3, s4*s2], [s0, s3, s4, s3*s2], [s3, s0, s4, s3*s2]]
        """
    Element = WeakTableau_factorized_permutation

class StrongTableau(ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    A (standard) strong `k`-tableau is a (saturated) chain in Bruhat order.

    Combinatorially, it is a sequence of embedded `k+1`-cores (subject to some conditions)
    together with a set of markings.

    A strong cover in terms of cores corresponds to certain translated ribbons. A marking
    corresponds to the choice of one of the translated ribbons, which is indicated by
    marking the head (southeast most cell in French notation) of the chosen ribbon.  For
    more information, see [LLMS2006]_ and [LLMSSZ2013]_.

    In Sage, a strong `k`-tableau is created by specifying `k`, a standard strong
    tableau together with its markings, and a weight `\\mu`. Here the standard tableau is
    represented by a sequence of `k+1`-cores

    .. MATH::

        \\lambda^{(0)} \\subseteq \\lambda^{(1)} \\subseteq \\cdots \\subseteq \\lambda^{(m)}

    where each of the `\\lambda^{(i)}` is a `k+1`-core.  The standard tableau is a filling
    of the diagram for the core `\\lambda^{(m)}/\\lambda^{(0)}` where a strong cover
    is represented by letters `\\pm i` in the skew shape `\\lambda^{(i)}/\\lambda^{(i-1)}`.
    Each skew `(k+1)`-core `\\lambda^{(i)}/\\lambda^{(i-1)}` is a ribbon or multiple
    copies of the same ribbon which are separated by `k+1` diagonals.  Precisely one of
    the copies of the ribbons will be marked in the largest diagonal of the connected
    component (the 'head' of the ribbon).  The marked cells are indicated by negative
    signs.

    The strong tableau is stored as a standard strong marked tableau (referred to as the
    standard part of the strong tableau) and a vector representing the weight.

    EXAMPLES::

        sage: StrongTableau( [[-1, -2, -3], [3]], 2, [3] )
        [[-1, -1, -1], [1]]
        sage: StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1])
        [[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4]]

    Alternatively, the strong `k`-tableau can also be entered directly in semistandard
    format and then the standard tableau and the weight are computed and stored::

        sage: T = StrongTableau([[-1,-1,-1],[1]], 2); T
        [[-1, -1, -1], [1]]
        sage: T.to_standard_list()
        [[-1, -2, -3], [3]]
        sage: T.weight()
        (3,)
        sage: T = StrongTableau([[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4]], 3); T
        [[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4]]
        sage: T.to_standard_list()
        [[-1, -2, -4, -7], [-3, 6, -6, 8], [4, 7], [-5, -8]]
        sage: T.weight()
        (2, 2, 3, 1)
    """
    k: Incomplete
    def __init__(self, parent, T) -> None:
        """
        INPUT:

        - ``parent`` -- an instance of ``StrongTableaux``
        - ``T`` -- standard marked strong (possibly skew) `k`-tableau or a semistandard
          marked strong (possibly skew) `k`-tableau with inner cells represented by
          ``None``

        EXAMPLES::

            sage: T = StrongTableau( [[-1, -2, -3]], 3 ); T
            [[-1, -2, -3]]
            sage: T
            [[-1, -2, -3]]
            sage: T.weight()
            (1, 1, 1)
            sage: T.size()
            3
            sage: T.parent()
            Set of strong 3-tableaux of shape [3] and of weight (1, 1, 1)
            sage: StrongTableau( [[-1, -2, -3], [3]], 2 )
            [[-1, -2, -3], [3]]
            sage: StrongTableau( [[-1, -1, 2], [-2]], 2 )
            [[-1, -1, 2], [-2]]
            sage: T = StrongTableau( [[-1, -2, 3], [-3]], 2, weight=[2,1] ); T
            [[-1, -1, 2], [-2]]
            sage: T = StrongTableau( [[-1, -2, 3], [-3]], 2, weight=[0,2,1] ); T
            [[-2, -2, 3], [-3]]
            sage: T.weight()
            (0, 2, 1)
            sage: T.size()
            3
            sage: T.parent()
            Set of strong 2-tableaux of shape [3, 1] and of weight (0, 2, 1)
            sage: StrongTableau( [[-1, -2, 3], [-3]], 2, weight=[1,2] )
            Traceback (most recent call last):
            ...
            ValueError: The weight=(1, 2) and the markings on the standard tableau=[[-1, -2, 3], [-3]] do not agree.
            sage: StrongTableau( [[None, None, -2, -4], [None, None], [-1, -3], [2, 4], [-5], [5], [5], [5]], 4 )
            [[None, None, -2, -4], [None, None], [-1, -3], [2, 4], [-5], [5], [5], [5]]
            sage: StrongTableau( [[None, None, -2, -4], [None, None], [-1, -3], [2, 4], [-5], [5], [5], [5]], 4, weight=[2,2,1] )
            [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]]
            sage: StrongTableau( [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]]

        TESTS::

            sage: T = StrongTableau([], 3); T
            []
            sage: T.weight()
            ()
            sage: T.parent()
            Set of strong 3-tableaux of shape [] and of weight ()
            sage: T = StrongTableau( [[None, None], [None, None]], 4, weight=() ); T
            [[None, None], [None, None]]
            sage: T.size()
            0
        """
    @staticmethod
    def __classcall_private__(cls, T, k, weight=None):
        """
        Straighten input and implement the shortcut ``StrongTableau(T, k, weight=None)``
        to ``StrongTableaux(k, shape, weight)(T)``.

        TESTS::

            sage: t = StrongTableau( [[-1, -2, -3]], 3 )
            sage: t.parent()
            Set of strong 3-tableaux of shape [3] and of weight (1, 1, 1)
            sage: TestSuite(t).run()
            sage: t = StrongTableau( [[-1, -2, 3], [-3]], 2, weight=[2,1] )
            sage: TestSuite(t).run()
            sage: StrongTableau([[-1,-1,-1]], 3)
            [[-1, -1, -1]]
            sage: StrongTableau([[None, None, None], [None]], 2)
            [[None, None, None], [None]]

            sage: StrongTableau([[-1, -2, -2], [1]], 2)
            Traceback (most recent call last):
            ...
            ValueError: Unable to parse strong marked tableau : [[-1, -2, -2], [1]]

            sage: StrongTableau([[-1,-1,-1,-1]], 3)
            Traceback (most recent call last):
            ...
            ValueError: [4] is not a 4-core

            sage: StrongTableau([[-1, -2], [2]], 3)
            Traceback (most recent call last):
            ...
            ValueError: The marks in [[-1, -2], [2]] are not correctly placed.

            sage: StrongTableau([[None, None, None], [None]], 3)
            Traceback (most recent call last):
            ...
            ValueError: [3, 1] is not a 4-core

            sage: StrongTableau([[None, -1, 2], [-2]], 2, [2])
            Traceback (most recent call last):
            ...
            ValueError: The weight=(2,) and the markings on the standard tableau=[[None, -1, 2], [-2]] do not agree.
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid strong `k`-tableau.

        This function verifies that the outer and inner shape of the parent class is equal to
        the outer and inner shape of the tableau, that the tableau portion of ``self`` is
        a valid standard tableau, that the marks are placed correctly and that the size
        and weight agree.

        EXAMPLES::

            sage: T = StrongTableau([[-1, -1, -2], [2]], 2)
            sage: T.check()
            sage: T = StrongTableau([[None, None, 2, -4, -4], [-1, 4], [-2]], 3)
            sage: T.check()

        TESTS::

            sage: ST = StrongTableaux(2, [3,1], [1,1,1,1])
            sage: ST([[-1,-2,3],[-3]])
            Traceback (most recent call last):
            ...
            ValueError: The size of the tableau [[-1, -2, 3], [-3]] and weight (1, 1, 1, 1) do not match
            sage: ST([[-1,-3],[-2],[3]])
            Traceback (most recent call last):
            ...
            ValueError: The outer shape of the parent does not agree with the outer shape of the tableau!

            sage: StrongTableau([[-1, -2, 2], [1]], 2)
            Traceback (most recent call last):
            ...
            ValueError: The marks in [[-1, -2, 2], [1]] are not correctly placed.

            sage: StrongTableau([[-1, -2, 3], [3]], 2)
            Traceback (most recent call last):
            ...
            ValueError: The marks in [[-1, -2, 3], [3]] are not correctly placed.

            sage: StrongTableau([[-1,-2,-4,7],[-3,6,-6,8],[4,-7],[-5,-8]], 3, [2,2,3,1])
            Traceback (most recent call last):
            ...
            ValueError: The weight=(2, 2, 3, 1) and the markings on the standard tableau=[[-1, -2, -4, 7], [-3, 6, -6, 8], [4, -7], [-5, -8]] do not agree.
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: t = StrongTableau([[-1, -1, -2], [2]], 2)
            sage: hash(t) == hash(t)
            True
        """
    def is_column_strict_with_weight(self, mu):
        """
        Test if ``self`` is a column strict tableau with respect to the weight ``mu``.

        INPUT:

        - ``mu`` -- a vector of weights

        OUTPUT: boolean; ``True`` means the underlying column strict strong
        marked tableau is valid

        EXAMPLES::

            sage: StrongTableau([[-1, -2, -3], [3]], 2).is_column_strict_with_weight([3])
            True
            sage: StrongTableau([[-1, -2, 3], [-3]], 2).is_column_strict_with_weight([3])
            False

        TESTS::

            sage: StrongTableau([[None, None, None], [None]], 2).is_column_strict_with_weight([])
            True
            sage: StrongTableau([], 4).is_column_strict_with_weight([])
            True
        """
    def cell_of_marked_head(self, v):
        """
        Return location of marked head labeled by ``v`` in the standard part of ``self``.

        Return the coordinates of the ``v``-th marked cell in the strong standard tableau
        ``self``.  If there is no mark, then the value returned is `(0, r)` where `r` is
        the length of the first row.

        INPUT:

        - ``v`` -- integer representing the label in the standard tableau

        OUTPUT: a pair of the coordinates of the marked cell with entry ``v``

        EXAMPLES::

            sage: T = StrongTableau([[-1, -3, 4, -5], [-2], [-4]], 3)
            sage: [ T.cell_of_marked_head(i) for i in range(1,7)]
            [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (0, 4)]
            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: [ T.cell_of_marked_head(i) for i in range(1,7)]
            [(2, 0), (0, 2), (2, 1), (0, 3), (4, 0), (0, 4)]

        TESTS::

            sage: StrongTableau([],4).cell_of_marked_head(4)
            (0, 0)
        """
    def content_of_marked_head(self, v):
        """
        Return the diagonal of the marked label ``v`` in the standard part of ``self``.

        Return the content (the `j-i` coordinate of the cell) of the ``v``-th marked cell
        in the strong standard tableau ``self``.  If there is no mark, then the value
        returned is the size of first row.

        INPUT:

        - ``v`` -- integer representing the label in the standard tableau

        OUTPUT: integer representing the residue of the location of the mark

        EXAMPLES::

            sage: [ StrongTableau([[-1, -3, 4, -5], [-2], [-4]], 3).content_of_marked_head(i) for i in range(1,7)]
            [0, -1, 1, -2, 3, 4]
            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: [ T.content_of_marked_head(i) for i in range(1,7)]
            [-2, 2, -1, 3, -4, 4]

        TESTS::

            sage: StrongTableau([],4).content_of_marked_head(4)
            0
        """
    def cells_of_marked_ribbon(self, v):
        """
        Return a list of all cells the marked ribbon labeled by ``v`` in the standard part of ``self``.

        Return the list of coordinates of the cells which are in the marked
        ribbon with label ``v`` in the standard part of the tableau.  Note that
        the result is independent of the weight of the tableau.

        The cells are listed from largest content (where the mark is located)
        to the smallest.  Hence, the first entry in this list will be the marked cell.

        INPUT:

        - ``v`` -- the entry of the standard tableau

        OUTPUT:

        - a list of pairs representing the coordinates of the cells of
          the marked ribbon

        EXAMPLES::

            sage: T = StrongTableau([[-1, -1, -2, -2, 3], [2, -3], [-3]],3)
            sage: T.to_standard_list()
            [[-1, -2, -3, -4, 6], [4, -6], [-5]]
            sage: T.cells_of_marked_ribbon(1)
            [(0, 0)]
            sage: T.cells_of_marked_ribbon(4)
            [(0, 3)]
            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3)
            sage: T.cells_of_marked_ribbon(6)
            [(1, 2), (1, 1)]
            sage: T.cells_of_marked_ribbon(9)
            []
            sage: T = StrongTableau([[None, None, -1, -1, 3], [1, -3], [-3]],3)
            sage: T.to_standard_list()
            [[None, None, -1, -2, 4], [2, -4], [-3]]
            sage: T.cells_of_marked_ribbon(1)
            [(0, 2)]

        TESTS::

            sage: StrongTableau([],3).cells_of_marked_ribbon(1)
            []
        """
    def cell_of_highest_head(self, v):
        """
        Return the cell of the highest head of label ``v`` in the standard part of ``self``.

        Return the cell where the head of the ribbon in the highest row is located
        in the underlying standard tableau.  If there is no cell with entry ``v`` then
        the cell returned is `(0, r)` where `r` is the length of the first row.

        This cell is calculated by iterating through the diagonals of the tableau.

        INPUT:

        - ``v`` -- integer indicating the label in the standard tableau

        OUTPUT: a pair of integers indicating the coordinates of the head of
        the highest ribbon with label ``v``

        EXAMPLES::

            sage: T = StrongTableau([[-1,2,-3],[-2,3],[3]], 1)
            sage: [T.cell_of_highest_head(v) for v in range(1,5)]
            [(0, 0), (1, 0), (2, 0), (0, 3)]
            sage: T = StrongTableau([[None,None,-3,4],[3,-4]],2)
            sage: [T.cell_of_highest_head(v) for v in range(1,5)]
            [(1, 0), (1, 1), (0, 4), (0, 4)]

        TESTS::

            sage: StrongTableau([],2).cell_of_highest_head(1)
            (0, 0)
        """
    def content_of_highest_head(self, v):
        """
        Return the diagonal of the highest head of the cells labeled ``v`` in the standard part of ``self``.

        Return the content of the cell of the head in the highest row of all ribbons labeled by ``v`` of
        the underlying standard tableau.  If there is no cell with entry ``v`` then
        the value returned is the length of the first row.

        INPUT:

        - ``v`` -- integer representing the label in the standard tableau

        OUTPUT: an integer representing the content of the head of the highest
        ribbon with label ``v``

        EXAMPLES::

            sage: [StrongTableau([[-1,2,-3],[-2,3],[3]], 1).content_of_highest_head(v) for v in range(1,5)]
            [0, -1, -2, 3]

        TESTS::

            sage: StrongTableau([], 4).content_of_highest_head(1)
            0
            sage: StrongTableau([[-1,-1]], 4).content_of_highest_head(3)
            2
        """
    def cells_head_dictionary(self):
        """
        Return a dictionary with the locations of the heads of all markings.

        Return a dictionary of values and lists of cells where the heads with the values
        are located.

        OUTPUT:

        - a dictionary with keys the entries in the tableau and values are the coordinates
          of the heads with those entries

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,-4,7],[-3,6,-6,8],[4,-7],[-5,-8]], 3)
            sage: T.cells_head_dictionary()
            {1: [(0, 0)],
             2: [(0, 1)],
             3: [(1, 0)],
             4: [(2, 0), (0, 2)],
             5: [(3, 0)],
             6: [(1, 2)],
             7: [(2, 1), (0, 3)],
             8: [(3, 1), (1, 3)]}
            sage: T = StrongTableau([[None, 4, -4, -6, -7, 8, 8, -8], [None, -5, 8, 8, 8], [-3, 6]],3)
            sage: T.cells_head_dictionary()
            {1: [(2, 0)],
             2: [(0, 2)],
             3: [(1, 1)],
             4: [(2, 1), (0, 3)],
             5: [(0, 4)],
             6: [(1, 4), (0, 7)]}
             sage: StrongTableau([[None, None], [None, -1]], 4).cells_head_dictionary()
             {1: [(1, 1)]}

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).cells_head_dictionary()
            {}
            sage: StrongTableau([],4).cells_head_dictionary()
            {}
        """
    def cells_of_heads(self, v):
        """
        Return a list of cells of the heads with label ``v`` in the standard part of ``self``.

        A list of cells which are heads of the ribbons with label ``v`` in the
        standard part of the tableau ``self``.  If there is no cell labelled by ``v`` then return the empty
        list.

        INPUT:

        - ``v`` -- integer label

        OUTPUT: a list of pairs of integers of the coordinates of the heads of
        the ribbons with label ``v``

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.cells_of_heads(1)
            [(2, 0)]
            sage: T.cells_of_heads(2)
            [(3, 0), (0, 2)]
            sage: T.cells_of_heads(3)
            [(2, 1)]
            sage: T.cells_of_heads(4)
            [(3, 1), (0, 3)]
            sage: T.cells_of_heads(5)
            [(4, 0)]
            sage: T.cells_of_heads(6)
            []

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).cells_of_heads(1)
            []
            sage: StrongTableau([],4).cells_of_heads(1)
            []
        """
    def contents_of_heads(self, v):
        """
        A list of contents of the cells which are heads of the ribbons with label ``v``.

        If there is no cell labelled by ``v`` then return the empty list.

        INPUT:

        - ``v`` -- integer label

        OUTPUT: list of integers of the content of the heads of the ribbons
        with label ``v``

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.contents_of_heads(1)
            [-2]
            sage: T.contents_of_heads(2)
            [-3, 2]
            sage: T.contents_of_heads(3)
            [-1]
            sage: T.contents_of_heads(4)
            [-2, 3]
            sage: T.contents_of_heads(5)
            [-4]
            sage: T.contents_of_heads(6)
            []

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).contents_of_heads(1)
            []
            sage: StrongTableau([],4).contents_of_heads(1)
            []
        """
    def entries_by_content(self, diag):
        """
        Return the entries on the diagonal of ``self``.

        Return the entries in the tableau that are in the cells `(i,j)` with
        `j-i` equal to ``diag`` (that is, with content equal to ``diag``).

        INPUT:

        - ``diag`` -- integer indicating the diagonal

        OUTPUT: list (perhaps empty) of labels on the diagonal ``diag``

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.entries_by_content(0)
            []
            sage: T.entries_by_content(1)
            []
            sage: T.entries_by_content(2)
            [-1]
            sage: T.entries_by_content(-2)
            [-1, 2]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).entries_by_content(1)
            []
            sage: StrongTableau([],4).entries_by_content(1)
            []
        """
    def entries_by_content_standard(self, diag):
        """
        Return the entries on the diagonal of the standard part of ``self``.

        Return the entries in the tableau that are in the cells `(i,j)` with
        `j-i` equal to ``diag`` (that is, with content equal to ``diag``) in the
        standard tableau.

        INPUT:

        - ``diag`` -- integer indicating the diagonal

        OUTPUT: list (perhaps empty) of labels on the diagonal ``diag``

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.entries_by_content_standard(0)
            []
            sage: T.entries_by_content_standard(1)
            []
            sage: T.entries_by_content_standard(2)
            [-2]
            sage: T.entries_by_content_standard(-2)
            [-1, 4]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).entries_by_content_standard(1)
            []
            sage: StrongTableau([],4).entries_by_content_standard(1)
            []
        """
    def ribbons_above_marked(self, v):
        """
        Number of ribbons of label ``v`` higher than the marked ribbon in the standard part.

        Return the number of copies of the ribbon with label ``v``  in the standard part
        of ``self`` which are in a higher row than the marked ribbon.  Note that the result
        is independent of the weight of the tableau.

        INPUT:

        - ``v`` -- the entry of the standard tableau

        OUTPUT:

        - an integer representing the number of copies of the ribbon above the marked
          ribbon

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3)
            sage: T.ribbons_above_marked(4)
            1
            sage: T.ribbons_above_marked(6)
            0
            sage: T.ribbons_above_marked(9)
            0
            sage: StrongTableau([[-1,-2,-3,-4],[2,3,4],[3,4],[4]], 1).ribbons_above_marked(4)
            3

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).ribbons_above_marked(1)
            0
            sage: StrongTableau([],4).ribbons_above_marked(1)
            0
        """
    def height_of_ribbon(self, v):
        """
        The number of rows occupied by one of the ribbons with label ``v``.

        The number of rows occupied by the marked ribbon with label ``v``
        (and by consequence the number of rows occupied by any ribbon with the same label)
        in the standard part of ``self``.

        INPUT:

        - ``v`` -- the label of the standard marked tableau

        OUTPUT: nonnegative integer representing the number of rows
        occupied by the ribbon which is marked

        EXAMPLES::

            sage: T = StrongTableau([[-1, -1, -2, -2, 3], [2, -3], [-3]],3)
            sage: T.to_standard_list()
            [[-1, -2, -3, -4, 6], [4, -6], [-5]]
            sage: T.height_of_ribbon(1)
            1
            sage: T.height_of_ribbon(4)
            1
            sage: T = StrongTableau([[None,None,1,-2],[None,-3,4,-5],[-1,3],[-4,5]], 3)
            sage: T.height_of_ribbon(3)
            2
            sage: T.height_of_ribbon(6)
            0

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).height_of_ribbon(1)
            0
            sage: StrongTableau([],4).height_of_ribbon(1)
            0
        """
    def number_of_connected_components(self, v):
        """
        Number of connected components of ribbons with label ``v`` in the standard part.

        The number of connected components is calculated by finding the number of cells
        with label ``v`` in the standard part of the tableau and dividing by the number
        of cells in the ribbon.

        INPUT:

        - ``v`` -- the label of the standard marked tableau

        OUTPUT: nonnegative integer representing the number of connected
        components

        EXAMPLES::

            sage: T = StrongTableau([[-1, -1, -2, -2, 3], [2, -3], [-3]],3)
            sage: T.to_standard_list()
            [[-1, -2, -3, -4, 6], [4, -6], [-5]]
            sage: T.number_of_connected_components(1)
            1
            sage: T.number_of_connected_components(4)
            2
            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3)
            sage: T.number_of_connected_components(6)
            1
            sage: T.number_of_connected_components(9)
            0

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).number_of_connected_components(1)
            0
            sage: StrongTableau([],4).number_of_connected_components(1)
            0
        """
    def intermediate_shapes(self):
        """
        Return the intermediate shapes of ``self``.

        A (skew) tableau with letters `1, 2, \\ldots, \\ell` can be viewed as a sequence of
        shapes, where the `i`-th shape is given by the shape of the subtableau on letters
        `1, 2, \\ldots, i`.

        The output is the list of these shapes.  The marked cells are ignored so to
        recover the strong tableau one would need the intermediate shapes and the
        :meth:`content_of_marked_head` for each pair of adjacent shapes in the list.

        OUTPUT: list of lists of integers representing `k+1`-cores

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1])
            sage: T.intermediate_shapes()
            [[], [2], [3, 1, 1], [4, 3, 2, 1], [4, 4, 2, 2]]
            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.intermediate_shapes()
            [[2, 2], [3, 2, 1, 1], [4, 2, 2, 2], [4, 2, 2, 2, 1, 1, 1, 1]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).intermediate_shapes()
            [[2, 1]]
            sage: StrongTableau([],4).intermediate_shapes()
            [[]]
        """
    def pp(self) -> None:
        """
        Print the strong tableau ``self`` in pretty print format.

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1])
            sage: T.pp()
            -1 -1 -2 -3
            -2  3 -3  4
             2  3
            -3 -4
            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.pp()
              .  . -1 -2
              .  .
             -1 -2
              1  2
             -3
              3
              3
              3
            sage: Tableaux.options(convention='French')
            sage: T.pp()
              3
              3
              3
             -3
              1  2
             -1 -2
              .  .
              .  . -1 -2
            sage: Tableaux.options(convention='English')
        """
    def outer_shape(self):
        """
        Return the outer shape of ``self``.

        This method returns the outer shape of ``self`` as viewed as a ``Core``.
        The outer shape of a strong tableau is always a `(k+1)`-core.

        OUTPUT:

        - a `(k+1)`-core

        EXAMPLES::

            sage: StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).outer_shape()
            [4, 2, 2, 2, 1, 1, 1, 1]
            sage: StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1]).outer_shape()
            [4, 4, 2, 2]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).outer_shape()
            [2, 1]
            sage: StrongTableau([],4).outer_shape()
            []
        """
    def inner_shape(self):
        """
        Return the inner shape of ``self``.

        If ``self`` is a strong skew tableau, then this method returns the inner shape
        (the shape of the cells labelled with ``None``).
        If ``self`` is not skew, then the inner shape is empty.

        OUTPUT:

        - a `(k+1)`-core

        EXAMPLES::

            sage: StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).inner_shape()
            [2, 2]
            sage: StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1]).inner_shape()
            []

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).inner_shape()
            [2, 1]
            sage: StrongTableau([],4).inner_shape()
            []
        """
    def shape(self):
        """
        Return the shape of ``self``.

        If ``self`` is a skew tableau then return a pair of `k+1`-cores consisting of the
        outer and the inner shape.  If ``self`` is strong tableau with no inner shape then
        return a `k+1`-core.

        INPUT:

        - ``form`` -- argument to indicate ``'inner'``, ``'outer'`` or
          ``'skew'`` (default: ``'outer'``)

        OUTPUT: a `k+1`-core or a pair of `k+1`-cores if form is not
        ``'inner'`` or ``'outer'``

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4)
            sage: T.shape()
            ([4, 2, 2, 2, 1, 1, 1, 1], [2, 2])
            sage: StrongTableau([[-1, -2, 3], [-3]], 2).shape()
            [3, 1]
            sage: type(StrongTableau([[-1, -2, 3], [-3]], 2).shape())
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>

        TESTS::

            sage: StrongTableau([[None, None, None], [None]], 2).shape()
            ([3, 1], [3, 1])
            sage: StrongTableau([],4).shape()
            []
        """
    def weight(self):
        """
        Return the weight of the tableau.

        The weight is a list of nonnegative integers indicating the number of 1s,
        number of 2s, number of 3s, etc.

        OUTPUT: list of nonnegative integers

        EXAMPLES::

            sage: T = StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3); T.weight()
            (1, 1, 1, 1, 1)
            sage: T.set_weight([3,1,1]).weight()
            (3, 1, 1)
            sage: StrongTableau([[-1,-1,-2,-3],[-2,3,-3,4],[2,3],[-3,-4]], 3).weight()
            (2, 2, 3, 1)

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).weight()
            ()
            sage: StrongTableau([],4).weight()
            ()
        """
    def size(self):
        """
        Return the size of the strong tableau.

        The size of the strong tableau is the sum of the entries in the
        :meth:`weight`.  It will also be equal to the length of the
        outer shape (as a `k+1`-core) minus the length of the inner shape.

        .. SEEALSO:: :meth:`sage.combinat.core.Core.length`

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3).size()
            5
            sage: StrongTableau([[None, None, -1, 2], [-2], [-3]], 3).size()
            3

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).size()
            0
            sage: StrongTableau([],4).size()
            0
        """
    def to_list(self):
        """
        Return the marked column strict (possibly skew) tableau as a list of lists.

        OUTPUT: list of lists of integers or ``None``

        EXAMPLES::

            sage: StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3).set_weight([2,1,1,1]).to_list()
            [[-1, -1, -2, 3], [-3], [-4]]
            sage: StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).to_list()
            [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]]
            sage: StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3, [3,1,1]).to_list()
            [[-1, -1, -1, 2], [-2], [-3]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_list()
            [[None, None], [None]]
            sage: StrongTableau([],4).to_list()
            []
        """
    def to_unmarked_list(self):
        """
        Return the tableau as a list of lists with markings removed.

        Return the list of lists of the rows of the tableau where the markings have been
        removed.

        OUTPUT: list of lists of integers or ``None``

        EXAMPLES::

            sage: T = StrongTableau( [[-1, -2, -3, 4], [-4], [-5]], 3, [3,1,1])
            sage: T.to_unmarked_list()
            [[1, 1, 1, 2], [2], [3]]
            sage: TT = T.set_weight([2,1,1,1])
            sage: TT.to_unmarked_list()
            [[1, 1, 2, 3], [3], [4]]
            sage: StrongTableau( [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).to_unmarked_list()
            [[None, None, 1, 2], [None, None], [1, 2], [1, 2], [3], [3], [3], [3]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_unmarked_list()
            [[None, None], [None]]
            sage: StrongTableau([],4).to_unmarked_list()
            []
        """
    def to_standard_list(self):
        """
        Return the underlying standard strong tableau as a list of lists.

        Internally, for a strong tableau the standard strong tableau and its weight
        is stored separately.  This method returns the underlying standard part.

        OUTPUT: list of lists of integers or ``None``

        EXAMPLES::

            sage: StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3, [3,1,1]).to_standard_list()
            [[-1, -2, -3, 4], [-4], [-5]]
            sage: StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).to_standard_list()
            [[None, None, -2, -4], [None, None], [-1, -3], [2, 4], [-5], [5], [5], [5]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_standard_list()
            [[None, None], [None]]
            sage: StrongTableau([],4).to_standard_list()
            []
        """
    def to_standard_tableau(self):
        """
        Return the underlying standard strong tableau as a ``StrongTableau`` object.

        Internally, for a strong tableau the standard strong tableau and its weight
        is stored separately.  This method returns the underlying standard part as a
        ``StrongTableau``.

        OUTPUT: a strong tableau with standard weight

        EXAMPLES::

            sage: T = StrongTableau([[-1, -2, -3, 4], [-4], [-5]], 3, [3,1,1])
            sage: T.to_standard_tableau()
            [[-1, -2, -3, 4], [-4], [-5]]
            sage: T.to_standard_tableau() == T.to_standard_list()
            False
            sage: StrongTableau([[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).to_standard_tableau()
            [[None, None, -2, -4], [None, None], [-1, -3], [2, 4], [-5], [5], [5], [5]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_standard_tableau()
            [[None, None], [None]]
            sage: StrongTableau([],4).to_standard_tableau()
            []
        """
    def to_unmarked_standard_list(self):
        """
        Return the standard part of the tableau as a list of lists with markings removed.

        Return the list of lists of the rows of the tableau where the markings have been
        removed.

        OUTPUT: list of lists of integers or ``None``

        EXAMPLES::

            sage: StrongTableau( [[-1, -2, -3, 4], [-4], [-5]], 3, [3,1,1]).to_unmarked_standard_list()
            [[1, 2, 3, 4], [4], [5]]
            sage: StrongTableau( [[None, None, -1, -2], [None, None], [-1, -2], [1, 2], [-3], [3], [3], [3]], 4).to_unmarked_standard_list()
            [[None, None, 2, 4], [None, None], [1, 3], [2, 4], [5], [5], [5], [5]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_unmarked_standard_list()
            [[None, None], [None]]
            sage: StrongTableau([],4).to_unmarked_standard_list()
            []
        """
    def restrict(self, r):
        """
        Restrict the standard part of the tableau to the labels `1, 2, \\ldots, r`.

        Return the tableau consisting of the labels of the standard part of ``self``
        restricted to the labels of `1` through ``r``.  The result is another
        ``StrongTableau`` object.

        INPUT:

        - ``r`` -- integer

        OUTPUT: a strong tableau

        EXAMPLES::

            sage: T = StrongTableau([[None, None, -4, 5, -5], [None, None], [-1, -3], [-2], [2], [2], [3]], 4, weight=[1,1,1,1,1])
            sage: T.restrict(3)
            [[None, None], [None, None], [-1, -3], [-2], [2], [2], [3]]
            sage: TT = T.restrict(0)
            sage: TT
            [[None, None], [None, None]]
            sage: TT == StrongTableau( [[None, None], [None, None]], 4 )
            True
            sage: T.restrict(5) == T
            True

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).restrict(1)
            [[None, None], [None]]
            sage: StrongTableau([],4).restrict(1)
            []
        """
    def set_weight(self, mu):
        """
        Set a new weight ``mu`` for ``self``.

        This method first tests if the underlying standard tableau is column-strict with
        respect to the weight ``mu``.  If it is, then it changes the weight and returns
        the tableau; otherwise it raises an error.

        INPUT:

        - ``mu`` -- list of nonnegative integers representing the new weight

        EXAMPLES::

            sage: StrongTableau( [[-1, -2, -3], [3]], 2 ).set_weight( [3] )
            [[-1, -1, -1], [1]]
            sage: StrongTableau( [[-1, -2, -3], [3]], 2 ).set_weight( [0,3] )
            [[-2, -2, -2], [2]]
            sage: StrongTableau( [[-1, -2, 3], [-3]], 2 ).set_weight( [2, 0, 1] )
            [[-1, -1, 3], [-3]]
            sage: StrongTableau( [[-1, -2, 3], [-3]], 2 ).set_weight( [3] )
            Traceback (most recent call last):
            ...
            ValueError: [[-1, -2, 3], [-3]] is not a semistandard strong tableau with respect to the partition [3]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).set_weight([])
            [[None, None], [None]]
            sage: StrongTableau([],4).set_weight([])
            []
        """
    def left_action(self, tij):
        """
        Action of transposition ``tij`` on ``self`` by adding marked ribbons.

        Computes the left action of the transposition ``tij`` on the tableau.
        If ``tij`` acting on the element of the affine Grassmannian raises the length by 1,
        then this function will add a cell to the standard tableau.

        INPUT:

        - ``tij`` -- a transposition represented as a pair `(i, j)`

        OUTPUT: ``self`` after it has been modified by the action of the transposition ``tij``

        EXAMPLES::

            sage: StrongTableau( [[None, -1, -2, -3], [3], [-4]], 3, weight=[1,1,1,1] ).left_action([0,1])
            [[None, -1, -2, -3, 5], [3, -5], [-4]]
            sage: StrongTableau( [[None, -1, -2, -3], [3], [-4]], 3, weight=[1,1,1,1] ).left_action([4,5])
            [[None, -1, -2, -3, -5], [3, 5], [-4]]
            sage: T = StrongTableau( [[None, -1, -2, -3], [3], [-4]], 3, weight=[1,1,1,1] )
            sage: T.left_action([-3,-2])
            [[None, -1, -2, -3], [3], [-4], [-5]]
            sage: T = StrongTableau( [[None, -1, -2, -3], [3], [-4]], 3, weight=[3,1] )
            sage: T.left_action([-3,-2])
            [[None, -1, -1, -1], [1], [-2], [-3]]
            sage: T
            [[None, -1, -1, -1], [1], [-2]]
            sage: T.check()
            sage: T.weight()
            (3, 1)

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).left_action([-2,-1])
            [[None, None], [None], [-1]]
            sage: StrongTableau([],4).left_action([0,1])
            [[-1]]
        """
    def follows_tableau(self):
        """
        Return a list of strong marked tableaux with length one longer than ``self``.

        Return list of all strong tableaux obtained from ``self`` by extending to a core
        which follows the shape of ``self`` in the strong order.

        OUTPUT: list of strong tableaux which follow ``self`` in strong order

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1])
            sage: T.follows_tableau()
            [[[-1, -1, -2, -3, 5, 5, -5], [-2, 3, -3, 4], [2, 3], [-3, -4]],
             [[-1, -1, -2, -3, 5], [-2, 3, -3, 4], [2, 3, 5], [-3, -4], [-5]],
             [[-1, -1, -2, -3, 5], [-2, 3, -3, 4], [2, 3, -5], [-3, -4], [5]],
             [[-1, -1, -2, -3, -5], [-2, 3, -3, 4], [2, 3, 5], [-3, -4], [5]],
             [[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4], [-5], [5], [5]]]
            sage: StrongTableau([[-1,-2],[-3,-4]],3).follows_tableau()
            [[[-1, -2, 5, 5, -5], [-3, -4]], [[-1, -2, 5], [-3, -4], [-5]],
             [[-1, -2, -5], [-3, -4], [5]], [[-1, -2], [-3, -4], [-5], [5], [5]]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).follows_tableau()
            [[[None, None, -1], [None]], [[None, None], [None, -1]], [[None, None], [None], [-1]]]
            sage: StrongTableau([],4).follows_tableau()
            [[[-1]]]
        """
    def spin_of_ribbon(self, v):
        """
        Return the spin of the ribbon with label ``v`` in the standard part of ``self``.

        The spin of a ribbon is an integer statistic.  It is the sum of `(h-1) r` plus
        the number of connected components above the marked one where `h` is the height
        of the marked ribbon and `r` is the number of connected components.

        .. SEEALSO:: :meth:`height_of_ribbon`, :meth:`number_of_connected_components`,
          :meth:`ribbons_above_marked`

        INPUT:

        - ``v`` -- a label of the standard part of the tableau

        OUTPUT: integer value representing the spin of the ribbon with label ``v``

        EXAMPLES::

            sage: T = StrongTableau([[-1,-2,5,6],[-3,-4,-7,8],[-5,-6],[7,-8]], 3)
            sage: [T.spin_of_ribbon(v) for v in range(1,9)]
            [0, 0, 0, 0, 0, 0, 1, 0]
            sage: T = StrongTableau([[None,None,-1,-3],[-2,3,-3,4],[2,3],[-3,-4]], 3)
            sage: [T.spin_of_ribbon(v) for v in range(1,7)]
            [0, 1, 0, 0, 1, 0]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).spin_of_ribbon(1)
            0
            sage: StrongTableau([],4).spin_of_ribbon(1)
            0
        """
    def spin(self):
        """
        Return the spin statistic of the tableau ``self``.

        The spin is an integer statistic on a strong marked tableau.  It is
        the sum of `(h-1) r` plus the number of connected components above the
        marked one where `h` is the height of the marked ribbon and `r` is
        the number of connected components.

        .. SEEALSO:: :meth:`height_of_ribbon`, :meth:`number_of_connected_components`,
          :meth:`ribbons_above_marked`

        The `k`-Schur functions with a parameter `t` can be defined as

        .. MATH::

            s^{(k)}_\\lambda[X; t] = \\sum_T t^{spin(T)} m_{weight(T)}[X]

        where the sum is over all column strict marked strong `k`-tableaux
        of shape `\\lambda` and partition content.

        OUTPUT: integer value representing the spin

        EXAMPLES::

            sage: StrongTableau([[-1,-2,5,6],[-3,-4,-7,8],[-5,-6],[7,-8]], 3, [2,2,3,1]).spin()
            1
            sage: StrongTableau([[-1,-2,-4,-7],[-3,6,-6,8],[4,7],[-5,-8]], 3, [2,2,3,1]).spin()
            2
            sage: StrongTableau([[None,None,-1,-3],[-2,3,-3,4],[2,3],[-3,-4]], 3).spin()
            2
            sage: ks3 = SymmetricFunctions(QQ['t'].fraction_field()).kschur(3)
            sage: t = ks3.realization_of().t
            sage: m = ks3.ambient().realization_of().m()
            sage: myks221 = sum(sum(t**T.spin() for T in StrongTableaux(3,[3,2,1],weight=mu))*m(mu) for mu in Partitions(5, max_part=3))
            sage: myks221 == m(ks3[2,2,1])
            True
            sage: h = ks3.ambient().realization_of().h()
            sage: Core([4,4,2,2],4).to_bounded_partition()
            [2, 2, 2, 2]
            sage: ks3[2,2,2,2].lift().scalar(h[3,3,2]) == sum( t**T.spin() for T in StrongTableaux(3, [4,4,2,2], weight=[3,3,2]) )
            True

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).spin()
            0
            sage: StrongTableau([],4).spin()
            0
        """
    def to_transposition_sequence(self):
        """
        Return a list of transpositions corresponding to ``self``.

        Given a strong column strict tableau ``self`` returns the list of transpositions
        which when applied to the left of an empty tableau gives the corresponding strong
        standard tableau.

        OUTPUT: list of pairs of values ``[i,j]`` representing the transpositions `t_{ij}`

        EXAMPLES::

            sage: T = StrongTableau([[-1, -1, -1], [1]],2)
            sage: T.to_transposition_sequence()
            [[2, 3], [1, 2], [0, 1]]
            sage: T = StrongTableau([[-1, -1, 2], [-2]],2)
            sage: T.to_transposition_sequence()
            [[-1, 0], [1, 2], [0, 1]]
            sage: T = StrongTableau([[None, -1, 2, -3], [-2, 3]],2)
            sage: T.to_transposition_sequence()
            [[3, 4], [-1, 0], [1, 2]]

        TESTS::

            sage: StrongTableau([[None, None], [None]], 4).to_transposition_sequence()
            []
            sage: StrongTableau([],4).to_transposition_sequence()
            []
        """

class StrongTableaux(UniqueRepresentation, Parent):
    k: Incomplete
    def __init__(self, k, shape, weight) -> None:
        """
        TESTS::

            sage: strongT = StrongTableaux(2, [3,1], weight=[2,1])
            sage: TestSuite(strongT).run()

            sage: strongT = StrongTableaux(0, [2,2], weight=[2,2])
            Traceback (most recent call last):
            ...
            ValueError: The input k has to be a positive integer
        """
    @staticmethod
    def __classcall_private__(cls, k, shape, weight=None):
        """
        Straighten arguments before unique representation.

        TESTS::

            sage: ST3 = StrongTableaux(3, [2,2], weight=[1,1,1,1])
            sage: TestSuite(ST3).run()
        """
    options = Tableaux.options
    def outer_shape(self):
        """
        Return the outer shape of the class of strong tableaux.

        OUTPUT: a `k+1`-core

        EXAMPLES::

            sage: StrongTableaux( 2, [3,1] ).outer_shape()
            [3, 1]
            sage: type(StrongTableaux( 2, [3,1] ).outer_shape())
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>
            sage: StrongTableaux( 4, [[2,1], [1]] ).outer_shape()
            [2, 1]
        """
    def inner_shape(self):
        """
        Return the inner shape of the class of strong tableaux.

        OUTPUT: a `k+1`-core

        EXAMPLES::

            sage: StrongTableaux( 2, [3,1] ).inner_shape()
            []
            sage: type(StrongTableaux( 2, [3,1] ).inner_shape())
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>
            sage: StrongTableaux( 4, [[2,1], [1]] ).inner_shape()
            [1]
        """
    def shape(self):
        """
        Return the shape of ``self``.

        If the ``self`` has an inner shape return a pair consisting of an inner and
        an outer shape.  If the inner shape is empty then return only the outer shape.

        OUTPUT: a `k+1`-core or a pair of `k+1`-cores

        EXAMPLES::

            sage: StrongTableaux( 2, [3,1] ).shape()
            [3, 1]
            sage: type(StrongTableaux( 2, [3,1] ).shape())
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>
            sage: StrongTableaux( 4, [[2,1], [1]] ).shape()
            ([2, 1], [1])
        """
    def __iter__(self):
        """
        TESTS::

            sage: ST = StrongTableaux(3, [4,1], weight=[2,2])
            sage: ST.list()
            [[[-1, -1, -2, -2], [2]], [[-1, -1, 2, -2], [-2]]]
            sage: ST = StrongTableaux(3, [5,2,2], weight=[2,2,2,1])
            sage: ST.cardinality()
            14
            sage: StrongTableaux(3, [5,2,2], weight=[3,3,1]).list()
            [[[-1, -1, -1, -2, -2], [-2, 2], [2, -3]], [[-1, -1, -1, 2, -2], [-2, -2], [2, -3]], [[-1, -1, -1, -2, -3], [-2, -2], [2, 2]]]
            sage: StrongTableaux(3, [4,1,1]).cardinality()
            10
            sage: StrongTableaux(3, [5,2,2], weight=[6,1]).list() # there are no strong column strict tableaux of shape [5,2,2] and weight (6,1)
            []
            sage: StrongTableaux(3, [[5,2,2], [3,1,1]], weight=[2,1]).list()
            [[[None, None, None, -1, -1], [None, 1], [None, -2]],
             [[None, None, None, 1, -1], [None, -1], [None, -2]],
             [[None, None, None, -1, -2], [None, -1], [None, 1]]]
            sage: StrongTableaux(2, [[4,3,3,2,2,1,1], [2,1,1]], weight=[1,1,1,1]).cardinality()
            150
            sage: StrongTableaux(2, [[7,5,3,1], [2,1,1]], weight=[2,2]).cardinality()
            18
            sage: StrongTableaux(2, [[3,1],[3,1]]).list()
            [[[None, None, None], [None]]]
            sage: StrongTableaux(4, []).list()
            [[]]
        """
    @classmethod
    def standard_unmarked_iterator(cls, k, size, outer_shape=None, inner_shape=[]) -> Generator[Incomplete]:
        """
        An iterator for standard unmarked strong tableaux.

        An iterator which generates all unmarked tableaux of a given ``size`` which are
        contained in ``outer_shape`` and which contain the ``inner_shape``.

        These are built recursively by building all standard marked strong tableaux of
        size ``size`` `-1` and adding all possible covers.

        If ``outer_shape`` is ``None`` then there is no restriction on the shape of the
        tableaux which are created.

        INPUT:

        - ``k``, ``size`` -- positive integers
        - ``outer_shape`` -- list representing a `k+1`-core (default: ``None``)
        - ``inner_shape`` -- list representing a `k+1`-core (default: ``[]``)

        OUTPUT:

        - an iterator which lists all standard strong unmarked tableaux with ``size``
          cells and which are contained in ``outer_shape`` and contain ``inner_shape``

        EXAMPLES::

            sage: list(StrongTableaux.standard_unmarked_iterator(2, 3))
            [[[1, 2, 3], [3]], [[1, 2], [3], [3]], [[1, 3, 3], [2]], [[1, 3], [2], [3]]]
            sage: list(StrongTableaux.standard_unmarked_iterator(2, 1, inner_shape=[1,1]))
            [[[None, 1, 1], [None]], [[None, 1], [None], [1]]]
            sage: len(list(StrongTableaux.standard_unmarked_iterator(4,4)))
            10
            sage: len(list(StrongTableaux.standard_unmarked_iterator(4,6)))
            98
            sage: len(list(StrongTableaux.standard_unmarked_iterator(4,4, inner_shape=[2,2])))
            92
            sage: len(list(StrongTableaux.standard_unmarked_iterator(4,4, outer_shape=[5,2,2,1], inner_shape=[2,2])))
            10

        TESTS::

            sage: list(StrongTableaux.standard_unmarked_iterator(2,0, outer_shape=[3,1], inner_shape=[3,1]))
            [[[None, None, None], [None]]]
            sage: list(StrongTableaux.standard_unmarked_iterator(4,0, outer_shape=[]))
            [[]]
        """
    @classmethod
    def marked_given_unmarked_and_weight_iterator(cls, unmarkedT, k, weight) -> Generator[Incomplete]:
        """
        An iterator generating strong marked tableaux from an unmarked strong tableau.

        Iterator which lists all marked tableaux of weight ``weight`` such that the
        standard unmarked part of the tableau is equal to ``unmarkedT``.

        INPUT:

        - ``unmarkedT`` -- list of lists representing a strong unmarked tableau
        - ``k`` -- positive integer
        - ``weight`` -- list of nonnegative integers indicating the weight

        OUTPUT: an iterator that returns ``StrongTableau`` objects

        EXAMPLES::

            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[1,2,3],[3]], 2, [3])
            sage: list(ST)
            [[[-1, -1, -1], [1]]]
            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[1,2,3],[3]], 2, [0,3])
            sage: list(ST)
            [[[-2, -2, -2], [2]]]
            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[1,2,3],[3]], 2, [1,2])
            sage: list(ST)
            [[[-1, -2, -2], [2]]]
            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[1,2,3],[3]], 2, [2,1])
            sage: list(ST)
            [[[-1, -1, 2], [-2]], [[-1, -1, -2], [2]]]
            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[None, None, 1, 2, 4], [2, 4], [3]], 3, [3,1])
            sage: list(ST)
            []
            sage: ST = StrongTableaux.marked_given_unmarked_and_weight_iterator([[None, None, 1, 2, 4], [2, 4], [3]], 3, [2,2])
            sage: list(ST)
            [[[None, None, -1, -1, 2], [1, -2], [-2]],
             [[None, None, -1, -1, -2], [1, 2], [-2]]]

        TESTS::

            sage: list(StrongTableaux.marked_given_unmarked_and_weight_iterator([[None, None, None],[None]], 2, []))
            [[[None, None, None], [None]]]
            sage: list(StrongTableaux.marked_given_unmarked_and_weight_iterator([], 4, weight=[]))
            [[]]
        """
    @classmethod
    def add_marking(cls, unmarkedT, marking, k, weight):
        """
        Add markings to a partially marked strong tableau.

        Given a partially marked standard tableau and a list of cells where the marks
        should be placed along with a ``weight``, return the semi-standard marked strong
        tableau.  The marking should complete the marking so that the result is a
        strong standard marked tableau.

        INPUT:

        - ``unmarkedT`` -- list of lists which is a partially marked strong `k`-tableau
        - ``marking`` -- list of pairs of coordinates where cells are to be marked
        - ``k`` -- positive integer
        - ``weight`` -- tuple of the weight of the output tableau

        OUTPUT: a ``StrongTableau`` object

        EXAMPLES::

            sage: StrongTableaux.add_marking([[None,1,2],[2]], [(0,1), (1,0)], 2, [1,1])
            [[None, -1, 2], [-2]]
            sage: StrongTableaux.add_marking([[None,1,2],[2]], [(0,1), (1,0)], 2, [2])
            Traceback (most recent call last):
            ...
            ValueError: The weight=(2,) and the markings on the standard tableau=[[None, -1, 2], [-2]] do not agree.
            sage: StrongTableaux.add_marking([[None,1,2],[2]], [(0,1), (0,2)], 2, [2])
            [[None, -1, -1], [1]]

        TESTS::

            sage: StrongTableaux.add_marking([[None,None,None],[None]], [], 2, [])
            [[None, None, None], [None]]
            sage: StrongTableaux.add_marking([], [], 2, [])
            []
        """
    @classmethod
    def follows_tableau_unsigned_standard(cls, Tlist, k):
        """
        Return a list of strong tableaux one longer in length than ``Tlist``.

        Return list of all standard strong tableaux obtained from ``Tlist`` by extending to
        a core which follows the shape of ``Tlist`` in the strong order.  It does not put
        the markings on the last entry that it adds but it does keep the markings on all
        entries smaller.  The objects returned are not ``StrongTableau`` objects (and
        cannot be) because the last entry will not properly marked.

        INPUT:

        - ``Tlist`` -- a filling of a `k+1`-core as a list of lists
        - ``k`` -- integer

        OUTPUT: list of strong tableaux which follow ``Tlist`` in strong order

        EXAMPLES::

            sage: StrongTableaux.follows_tableau_unsigned_standard([[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4]], 3)
            [[[-1, -1, -2, -3, 5, 5, 5], [-2, 3, -3, 4], [2, 3], [-3, -4]],
             [[-1, -1, -2, -3, 5], [-2, 3, -3, 4], [2, 3, 5], [-3, -4], [5]],
             [[-1, -1, -2, -3], [-2, 3, -3, 4], [2, 3], [-3, -4], [5], [5], [5]]]
            sage: StrongTableaux.follows_tableau_unsigned_standard([[None,-1],[-2,-3]],3)
            [[[None, -1, 4, 4, 4], [-2, -3]], [[None, -1, 4], [-2, -3], [4]],
             [[None, -1], [-2, -3], [4], [4], [4]]]

        TESTS::

            sage: StrongTableaux.follows_tableau_unsigned_standard([[None, None, None], [None]], 2)
            [[[None, None, None, 1], [None, 1]], [[None, None, None], [None], [1]]]
            sage: StrongTableaux.follows_tableau_unsigned_standard([], 4)
            [[[1]]]
        """
    @classmethod
    def standard_marked_iterator(cls, k, size, outer_shape=None, inner_shape=[]) -> Generator[Incomplete, Incomplete]:
        """
        An iterator for generating standard strong marked tableaux.

        An iterator which generates all standard marked `k`-tableaux of a given ``size``
        which are contained in ``outer_shape`` and contain the ``inner_shape``.
        If ``outer_shape`` is ``None`` then there is no restriction on the shape of the
        tableaux which are created.

        INPUT:

        - ``k`` -- positive integer
        - ``size`` -- positive integer
        - ``outer_shape`` -- list which is a `k+1`-core (default: ``None``)
        - ``inner_shape`` -- list which is a `k+1`-core (default: ``[]``)

        OUTPUT:

        - an iterator which returns the standard marked tableaux with ``size`` cells
          and that are contained in ``outer_shape`` and contain ``inner_shape``

        EXAMPLES::

            sage: list(StrongTableaux.standard_marked_iterator(2, 3))
            [[[-1, -2, 3], [-3]], [[-1, -2, -3], [3]], [[-1, -2], [-3], [3]], [[-1, 3, -3], [-2]], [[-1, 3], [-2], [-3]], [[-1, -3], [-2], [3]]]
            sage: list(StrongTableaux.standard_marked_iterator(2, 1, inner_shape=[1,1]))
            [[[None, 1, -1], [None]], [[None, 1], [None], [-1]], [[None, -1], [None], [1]]]
            sage: len(list(StrongTableaux.standard_marked_iterator(4,4)))
            10
            sage: len(list(StrongTableaux.standard_marked_iterator(4,6)))
            140
            sage: len(list(StrongTableaux.standard_marked_iterator(4,4, inner_shape=[2,2])))
            200
            sage: len(list(StrongTableaux.standard_marked_iterator(4,4, outer_shape=[5,2,2,1], inner_shape=[2,2])))
            24

        TESTS::

            sage: list(StrongTableaux.standard_marked_iterator(2,0,inner_shape=[3,1]))
            [[[None, None, None], [None]]]
            sage: list(StrongTableaux.standard_marked_iterator(4,0))
            [[]]
        """
    @classmethod
    def cells_head_dictionary(cls, T):
        """
        Return a dictionary with the locations of the heads of all markings.

        Return a dictionary of values and lists of cells where the heads with the values
        are located in a strong standard unmarked tableau ``T``.

        INPUT:

        - ``T`` -- a strong standard unmarked tableau as a list of lists

        OUTPUT:

        - a dictionary with keys the entries in the tableau and values are the coordinates
          of the heads with those entries

        EXAMPLES::

            sage: StrongTableaux.cells_head_dictionary([[1,2,4,7],[3,6,6,8],[4,7],[5,8]])
            {1: [(0, 0)],
             2: [(0, 1)],
             3: [(1, 0)],
             4: [(2, 0), (0, 2)],
             5: [(3, 0)],
             6: [(1, 2)],
             7: [(2, 1), (0, 3)],
             8: [(3, 1), (1, 3)]}
            sage: StrongTableaux.cells_head_dictionary([[None, 2, 2, 4, 5, 6, 6, 6], [None, 3, 6, 6, 6], [1, 4]])
            {1: [(2, 0)],
             2: [(0, 2)],
             3: [(1, 1)],
             4: [(2, 1), (0, 3)],
             5: [(0, 4)],
             6: [(1, 4), (0, 7)]}

        TESTS::

             sage: StrongTableaux.cells_head_dictionary([[None, None, None],[None]])
             {}
             sage: StrongTableaux.cells_head_dictionary([])
             {}
        """
    @classmethod
    def marked_CST_to_transposition_sequence(self, T, k):
        """
        Return a list of transpositions corresponding to ``T``.

        Given a strong column strict tableau ``T`` returns the list of transpositions
        which when applied to the left of an empty tableau gives the corresponding strong
        standard tableau.

        INPUT:

        - ``T`` -- a non-empty column strict tableau as a list of lists
        - ``k`` -- positive integer

        OUTPUT: list of pairs of values ``[i,j]`` representing the transpositions `t_{ij}`

        EXAMPLES::

            sage: CST_to_trans = StrongTableaux.marked_CST_to_transposition_sequence
            sage: CST_to_trans([[-1, -1, -1], [1]], 2)
            [[2, 3], [1, 2], [0, 1]]
            sage: CST_to_trans([], 2)
            []
            sage: CST_to_trans([[-2, -2, -2], [2]], 2)
            [[2, 3], [1, 2], [0, 1]]
            sage: CST_to_trans([[-1, -2, -2, -2, -2], [-2, 2], [2]], 3)
            [[4, 5], [3, 4], [2, 3], [1, 2], [-1, 0], [0, 1]]
            sage: CST_to_trans([[-1, -2, -5, 5, -5, 5, -5], [-3, -4, 5, 5], [5]],3)
            [[5, 7], [3, 5], [2, 3], [0, 1], [-1, 0], [1, 2], [0, 1]]
            sage: CST_to_trans([[-1, -2, -3, 4, -7], [-4, -6], [-5, 6]],3)
            [[4, 5], [-1, 1], [-2, -1], [-1, 0], [2, 3], [1, 2], [0, 1]]

        TESTS::

            sage: StrongTableaux.marked_CST_to_transposition_sequence([[None, None, None], [None]], 2)
            []
            sage: StrongTableaux.marked_CST_to_transposition_sequence([], 4)
            []
        """
    @classmethod
    def transpositions_to_standard_strong(self, transeq, k, emptyTableau=[]):
        """
        Return a strong tableau corresponding to a sequence of transpositions.

        This method returns the action by left multiplication on the empty strong tableau
        by transpositions specified by ``transeq``.

        INPUT:

        - ``transeq`` -- a sequence of transpositions `t_{ij}` (a list of pairs)
        - ``emptyTableau`` -- (default: ``[]``) an empty list or a skew strong tableau
          possibly consisting of ``None`` entries

        OUTPUT: a ``StrongTableau`` object

        EXAMPLES::

            sage: StrongTableaux.transpositions_to_standard_strong([[0,1]], 2)
            [[-1]]
            sage: StrongTableaux.transpositions_to_standard_strong([[-2,-1], [2,3]], 2, [[None, None]])
            [[None, None, -1], [1], [-2]]
            sage: StrongTableaux.transpositions_to_standard_strong([[2, 3], [1, 2], [0, 1]], 2)
            [[-1, -2, -3], [3]]
            sage: StrongTableaux.transpositions_to_standard_strong([[-1, 0], [1, 2], [0, 1]], 2)
            [[-1, -2, 3], [-3]]
            sage: StrongTableaux.transpositions_to_standard_strong([[3, 4], [-1, 0], [1, 2]], 2, [[None]])
            [[None, -1, 2, -3], [-2, 3]]

        TESTS::

            sage: StrongTableaux.transpositions_to_standard_strong([], 2, [[None, None, None], [None]])
            [[None, None, None], [None]]
            sage: StrongTableaux.transpositions_to_standard_strong([], 4, [])
            []
        """
    Element = StrongTableau

def nabs(v):
    """
    Return the absolute value of ``v`` or ``None``.

    INPUT:

    - ``v`` -- either an integer or ``None``

    OUTPUT: either a nonnegative integer or ``None``

    EXAMPLES::

        sage: from sage.combinat.k_tableau import nabs
        sage: nabs(None)
        sage: nabs(-3)
        3
        sage: nabs(None)
    """
def intermediate_shapes(t):
    """
    Return the intermediate shapes of tableau ``t``.

    A (skew) tableau with letters `1, 2,\\ldots, \\ell` can be viewed as a sequence of
    shapes, where the `i`-th shape is given by the shape of the subtableau on letters
    `1, 2, \\ldots, i`.  The output is the list of these shapes.

    OUTPUT: list of lists representing partitions

    EXAMPLES::

        sage: from sage.combinat.k_tableau import intermediate_shapes
        sage: t = WeakTableau([[1, 1, 2, 2, 3], [2, 3], [3]],3)
        sage: intermediate_shapes(t)
        [[], [2], [4, 1], [5, 2, 1]]

        sage: t = WeakTableau([[None, None, 2, 3, 4], [1, 4], [2]], 3)
        sage: intermediate_shapes(t)
        [[2], [2, 1], [3, 1, 1], [4, 1, 1], [5, 2, 1]]
    """
