from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.partition import Partitions_n as Partitions_n
from sage.combinat.permutation import Permutation as Permutation, from_cycles as from_cycles
from sage.combinat.set_partition import SetPartitions as SetPartitions
from sage.groups.conjugacy_classes import ConjugacyClass as ConjugacyClass, ConjugacyClassGAP as ConjugacyClassGAP
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.sets.set import Set as Set

class SymmetricGroupConjugacyClassMixin:
    """
    Mixin class which contains methods for conjugacy classes of
    the symmetric group.
    """
    def __init__(self, domain, part) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: g = G([(1,2), (3,4,5)])
            sage: C = G.conjugacy_class(Partition([3,2]))                               # needs sage.combinat
            sage: type(C._part)                                                         # needs sage.combinat
            <class 'sage.combinat.partition.Partitions_n_with_category.element_class'>
        """
    def __eq__(self, other):
        """
        Comparison of conjugacy classes is done by comparing the
        defining cycle types.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: g = G([(1,2), (3,4,5)])
            sage: C = G.conjugacy_class(Partition([3,2]))                               # needs sage.combinat
            sage: Cp = G.conjugacy_class(g)                                             # needs sage.combinat
            sage: C == Cp                                                               # needs sage.combinat
            True
        """
    def __ne__(self, other):
        """
        Test for unequality.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: g = G([(1,3), (2,4,5)])
            sage: C = G.conjugacy_class(Partition([3,2]))                               # needs sage.combinat
            sage: Cp = G.conjugacy_class(g)                                             # needs sage.combinat
            sage: C != Cp                                                               # needs sage.combinat
            False
        """
    def partition(self):
        """
        Return the partition of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: g = G([(1,2), (3,4,5)])
            sage: C = G.conjugacy_class(g)                                              # needs sage.combinat
        """

class SymmetricGroupConjugacyClass(SymmetricGroupConjugacyClassMixin, ConjugacyClassGAP):
    """
    A conjugacy class of the symmetric group.

    INPUT:

    - ``group`` -- the symmetric group
    - ``part`` -- a partition or an element of ``group``
    """
    def __init__(self, group, part) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = SymmetricGroup(5)
            sage: g = G([(1,2), (3,4,5)])
            sage: C = G.conjugacy_class(g)
            sage: TestSuite(C).run()
            sage: C = G.conjugacy_class(Partition([3,2]))
            sage: TestSuite(C).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: C = G.conjugacy_class(Partition([3,1]))                               # needs sage.combinat
            sage: for x in C: x                                                         # needs sage.combinat
            (2,3,4)
            (2,4,3)
            (1,2,3)
            (1,3,2)
            (1,2,4)
            (1,4,2)
            (1,3,4)
            (1,4,3)
        """
    def set(self):
        """
        The set of all elements in the conjugacy class ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: g = G((1,2))
            sage: C = G.conjugacy_class(g)                                              # needs sage.combinat
            sage: S = [(2,3), (1,2), (1,3)]
            sage: C.set() == Set(G(x) for x in S)                                       # needs sage.combinat
            True
        """

class PermutationsConjugacyClass(SymmetricGroupConjugacyClassMixin, ConjugacyClass):
    """
    A conjugacy class of the permutations of `n`.

    INPUT:

    - ``P`` -- the permutations of `n`
    - ``part`` -- a partition or an element of ``P``
    """
    def __init__(self, P, part) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: G = Permutations(5)
            sage: g = G([2, 1, 4, 5, 3])
            sage: C = G.conjugacy_class(g)
            sage: TestSuite(C).run()
            sage: C = G.conjugacy_class(Partition([3,2]))
            sage: TestSuite(C).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: G = Permutations(4)
            sage: C = G.conjugacy_class(Partition([3,1]))                               # needs sage.combinat
            sage: for x in C: x                                                         # needs sage.combinat
            [1, 3, 4, 2]
            [1, 4, 2, 3]
            [2, 3, 1, 4]
            [3, 1, 2, 4]
            [2, 4, 3, 1]
            [4, 1, 3, 2]
            [3, 2, 4, 1]
            [4, 2, 1, 3]
        """
    def set(self):
        """
        The set of all elements in the conjugacy class ``self``.

        EXAMPLES::

            sage: G = Permutations(3)
            sage: g = G([2, 1, 3])
            sage: C = G.conjugacy_class(g)                                              # needs sage.combinat
            sage: S = [[1, 3, 2], [2, 1, 3], [3, 2, 1]]
            sage: C.set() == Set(G(x) for x in S)                                       # needs sage.combinat
            True
        """

def default_representative(part, G):
    """
    Construct the default representative for the conjugacy class of
    cycle type ``part`` of a symmetric group ``G``.

    Let `\\lambda` be a partition of `n`. We pick a representative by

    .. MATH::

        (1, 2, \\ldots, \\lambda_1)
        (\\lambda_1 + 1, \\ldots, \\lambda_1 + \\lambda_2)
        (\\lambda_1 + \\lambda_2 + \\cdots + \\lambda_{\\ell-1}, \\ldots, n),

    where `\\ell` is the length (or number of parts) of `\\lambda`.

    INPUT:

    - ``part`` -- partition

    - ``G`` -- a symmetric group

    EXAMPLES::

        sage: from sage.groups.perm_gps.symgp_conjugacy_class import default_representative         # needs sage.combinat
        sage: S = SymmetricGroup(4)
        sage: for p in Partitions(4):                                                   # needs sage.combinat
        ....:     print(default_representative(p, S))
        (1,2,3,4)
        (1,2,3)
        (1,2)(3,4)
        (1,2)
        ()
    """
def conjugacy_class_iterator(part, S=None) -> Generator[Incomplete]:
    """
    Return an iterator over the conjugacy class associated to
    the partition ``part``.

    The elements are given as a list of tuples, each tuple being a cycle.

    INPUT:

    - ``part`` -- partition

    - ``S`` -- (default: `\\{ 1, 2, \\ldots, n \\}`, where `n`
      is the size of ``part``) a set

    OUTPUT: an iterator over the conjugacy class consisting of all
    permutations of the set ``S`` whose cycle type is ``part``

    EXAMPLES::

        sage: from sage.groups.perm_gps.symgp_conjugacy_class import conjugacy_class_iterator       # needs sage.combinat
        sage: for p in conjugacy_class_iterator([2,2]): print(p)                        # needs sage.combinat
        [(1, 2), (3, 4)]
        [(1, 4), (2, 3)]
        [(1, 3), (2, 4)]

    In order to get permutations, one just has to wrap::

        sage: S = SymmetricGroup(5)
        sage: for p in conjugacy_class_iterator([3,2]): print(S(p))                     # needs sage.combinat
        (1,3)(2,4,5)
        (1,3)(2,5,4)
        (1,2)(3,4,5)
        (1,2)(3,5,4)
        ...
        (1,4)(2,3,5)
        (1,4)(2,5,3)

    Check that the number of elements is the number of elements in
    the conjugacy class::

        sage: s = lambda p: sum(1 for _ in conjugacy_class_iterator(p))
        sage: all(s(p) == p.conjugacy_class_size() for p in Partitions(5))              # needs sage.combinat
        True

    It is also possible to specify any underlying set::

        sage: it = conjugacy_class_iterator([2,2,2], 'abcdef')                          # needs sage.combinat
        sage: sorted(flatten(next(it)))                                                 # needs sage.combinat
        ['a', 'b', 'c', 'd', 'e', 'f']
        sage: all(len(x) == 2 for x in next(it))                                        # needs sage.combinat
        True
    """
