from . import composition as composition, permutation as permutation, tableau as tableau
from .combinat import CombinatorialElement as CombinatorialElement
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial, factorial as factorial, gcd as gcd, multinomial as multinomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.combinat_cython import conjugate as conjugate
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.integer_lists import IntegerListsLex as IntegerListsLex
from sage.combinat.integer_lists.invlex import IntegerListsBackend_invlex as IntegerListsBackend_invlex
from sage.combinat.partition_tuple import PartitionTuples_level_size as PartitionTuples_level_size
from sage.combinat.partitions import ZS1_iterator as ZS1_iterator, ZS1_iterator_nk as ZS1_iterator_nk, ZS1_next as ZS1_next, ZS2_next as ZS2_next
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.prandom import randrange as randrange
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Partition(CombinatorialElement):
    """
    A partition `p` of a nonnegative integer `n` is a
    non-increasing list of positive integers (the *parts* of the
    partition) with total sum `n`.

    A partition is often represented as a diagram consisting of **cells**,
    or **boxes**, placed in rows on top of each other such that the number of
    cells in the `i`-th row, reading from top to bottom, is the `i`-th
    part of the partition. The rows are left-justified (and become shorter
    and shorter the farther down one goes). This diagram is called the
    **Young diagram** of the partition, or more precisely its Young diagram
    in English notation. (French and Russian notations are variations on this
    representation.)

    The coordinate system related to a partition applies from the top
    to the bottom and from left to right. So, the corners of the
    partition ``[5, 3, 1]`` are ``[[0,4], [1,2], [2,0]]``.

    For display options, see :meth:`Partitions.options`.

    .. NOTE::

        Partitions are 0 based with coordinates in the form of (row-index,
        column-index). For example consider the partition
        ``mu=Partition([4,3,2,2])``, the first part is ``mu[0]`` (which is 4),
        the second is ``mu[1]``, and so on, and the upper-left cell in English
        convention is ``(0, 0)``.

    A partition can be specified in one of the following ways:

    - a list (the default)
    - using exponential notation
    - by Frobenius coordinates
    - specifying its `0-1` sequence
    - specifying the core and the quotient

    See the examples below.

    EXAMPLES:

    Creating partitions though parents::

        sage: mu = Partitions(8)([3,2,1,1,1]); mu
        [3, 2, 1, 1, 1]
        sage: nu = Partition([3,2,1,1,1]); nu
        [3, 2, 1, 1, 1]
        sage: mu == nu
        True
        sage: mu is nu
        False
        sage: mu in Partitions()
        True
        sage: mu.parent()
        Partitions of the integer 8
        sage: mu.size()
        8
        sage: mu.category()
        Category of elements of Partitions of the integer 8
        sage: nu.parent()
        Partitions
        sage: nu.category()
        Category of elements of Partitions
        sage: mu[0]
        3
        sage: mu[1]
        2
        sage: mu[2]
        1
        sage: mu.pp()
        ***
        **
        *
        *
        *
        sage: mu.removable_cells()
        [(0, 2), (1, 1), (4, 0)]
        sage: mu.down_list()
        [[2, 2, 1, 1, 1], [3, 1, 1, 1, 1], [3, 2, 1, 1]]
        sage: mu.addable_cells()
        [(0, 3), (1, 2), (2, 1), (5, 0)]
        sage: mu.up_list()
        [[4, 2, 1, 1, 1], [3, 3, 1, 1, 1], [3, 2, 2, 1, 1], [3, 2, 1, 1, 1, 1]]
        sage: mu.conjugate()
        [5, 2, 1]
        sage: mu.dominates(nu)
        True
        sage: nu.dominates(mu)
        True

    Creating partitions using ``Partition``::

        sage: Partition([3,2,1])
        [3, 2, 1]
        sage: Partition(exp=[2,1,1])
        [3, 2, 1, 1]
        sage: Partition(core=[2,1], quotient=[[2,1],[3],[1,1,1]])
        [11, 5, 5, 3, 2, 2, 2]
        sage: Partition(frobenius_coordinates=([3,2],[4,0]))
        [4, 4, 1, 1, 1]
        sage: Partitions().from_zero_one([1, 1, 1, 1, 0, 1, 0])
        [5, 4]
        sage: [2,1] in Partitions()
        True
        sage: [2,1,0] in Partitions()
        True
        sage: Partition([1,2,3])
        Traceback (most recent call last):
        ...
        ValueError: [1, 2, 3] is not an element of Partitions

    Sage ignores trailing zeros at the end of partitions::

        sage: Partition([3,2,1,0])
        [3, 2, 1]
        sage: Partitions()([3,2,1,0])
        [3, 2, 1]
        sage: Partitions(6)([3,2,1,0])
        [3, 2, 1]

    TESTS:

    Check that only trailing zeros are stripped::

        sage: TestSuite( Partition([]) ).run()
        sage: TestSuite( Partition([4,3,2,2,2,1]) ).run()
        sage: Partition([3,2,2,2,1,0,0,0])
        [3, 2, 2, 2, 1]
        sage: Partition([3,0,2,2,2,1,0])
        Traceback (most recent call last):
        ...
        ValueError: [3, 0, 2, 2, 2, 1, 0] is not an element of Partitions
        sage: Partition([0,7,3])
        Traceback (most recent call last):
        ...
        ValueError: [0, 7, 3] is not an element of Partitions
    """
    @staticmethod
    def __classcall_private__(cls, mu=None, **keyword):
        """
        This constructs a list from optional arguments and delegates the
        construction of a :class:`Partition` to the ``element_class()`` call
        of the appropriate parent.

        EXAMPLES::

            sage: Partition([3,2,1])
            [3, 2, 1]
            sage: Partition(exp=[2,1,1])
            [3, 2, 1, 1]
            sage: Partition(core=[2,1], quotient=[[2,1],[3],[1,1,1]])
            [11, 5, 5, 3, 2, 2, 2]
        """
    def __init__(self, parent, mu) -> None:
        """
        Initialize ``self``.

        We assume that ``mu`` is a weakly decreasing list of
        nonnegative elements in ``ZZ``.

        EXAMPLES::

            sage: p = Partition([3,1])
            sage: TestSuite(p).run()

        TESTS:

        Fix that tuples raise the correct error::

            sage: Partition((3,1,7))
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 7] is not an element of Partitions
        """
    @cached_method
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: P = Partition([4,2,2,1])
            sage: hash(P) == hash(P)
            True
        """
    def level(self) -> int:
        """
        Return the level of ``self``, which is always 1.

        This method exists only for compatibility with
        :class:`PartitionTuples`.

        EXAMPLES::

            sage: Partition([4,3,2]).level()
            1
        """
    def components(self) -> list:
        """
        Return a list containing the shape of ``self``.

        This method exists only for compatibility with
        :class:`PartitionTuples`.

        EXAMPLES::

            sage: Partition([3,2]).components()
            [[3, 2]]
        """
    def ferrers_diagram(self) -> str:
        '''
        Return the Ferrers diagram of ``self``.

        EXAMPLES::

            sage: mu = Partition([5,5,2,1])
            sage: Partitions.options(diagram_str=\'*\', convention=\'english\')
            sage: print(mu.ferrers_diagram())
            *****
            *****
            **
            *
            sage: Partitions.options(diagram_str=\'▉\')
            sage: print(mu.ferrers_diagram())
            ▉▉▉▉▉
            ▉▉▉▉▉
            ▉▉
            ▉
            sage: Partitions.options.convention="french"
            sage: print(mu.ferrers_diagram())
            ▉
            ▉▉
            ▉▉▉▉▉
            ▉▉▉▉▉
            sage: print(Partition([]).ferrers_diagram())
            -
            sage: Partitions.options(diagram_str=\'-\')
            sage: print(Partition([]).ferrers_diagram())
            (/)
            sage: Partitions.options._reset()
        '''
    def pp(self) -> None:
        """
        Print the Ferrers diagram.

        See :meth:`ferrers_diagram` for more on the Ferrers diagram.

        EXAMPLES::

            sage: Partition([5,5,2,1]).pp()
            *****
            *****
            **
            *
            sage: Partitions.options.convention='French'
            sage: Partition([5,5,2,1]).pp()
            *
            **
            *****
            *****
            sage: Partitions.options._reset()
        """
    def __truediv__(self, p):
        """
        Return the skew partition ``self / p``.

        EXAMPLES::

            sage: p = Partition([3,2,1])
            sage: p/[1,1]
            [3, 2, 1] / [1, 1]
            sage: p/[3,2,1]
            [3, 2, 1] / [3, 2, 1]
            sage: p/Partition([1,1])
            [3, 2, 1] / [1, 1]
            sage: p/[2,2,2]
            Traceback (most recent call last):
            ...
            ValueError: to form a skew partition p/q, q must be contained in p
        """
    def stretch(self, k):
        """
        Return the partition obtained by multiplying each part with the
        given number.

        EXAMPLES::

            sage: p = Partition([4,2,2,1,1])
            sage: p.stretch(3)
            [12, 6, 6, 3, 3]
        """
    def power(self, k):
        """
        Return the cycle type of the `k`-th power of any permutation
        with cycle type ``self`` (thus describes the powermap of
        symmetric groups).

        Equivalent to GAP's ``PowerPartition``.

        EXAMPLES::

            sage: p = Partition([5,3])
            sage: p.power(1)
            [5, 3]
            sage: p.power(2)
            [5, 3]
            sage: p.power(3)
            [5, 1, 1, 1]
            sage: p.power(4)
            [5, 3]

        Now let us compare this to the power map on `S_8`::

            sage: # needs sage.groups
            sage: G = SymmetricGroup(8)
            sage: g = G([(1,2,3,4,5),(6,7,8)]); g
            (1,2,3,4,5)(6,7,8)
            sage: g^2
            (1,3,5,2,4)(6,8,7)
            sage: g^3
            (1,4,2,5,3)
            sage: g^4
            (1,5,4,3,2)(6,7,8)

        ::

            sage: Partition([3,2,1]).power(3)
            [2, 1, 1, 1, 1]
        """
    def __next__(self):
        """
        Return the partition that lexicographically follows ``self``, of the
        same size. If ``self`` is the last partition, then return ``False``.

        EXAMPLES::

            sage: next(Partition([4]))
            [3, 1]
            sage: next(Partition([1,1,1,1]))
            False
        """
    next = __next__
    def size(self):
        """
        Return the size of ``self``.

        EXAMPLES::

            sage: Partition([2,2]).size()
            4
            sage: Partition([3,2,1]).size()
            6
        """
    def sign(self):
        """
        Return the sign of any permutation with cycle type ``self``.

        This function corresponds to a homomorphism from the symmetric
        group `S_n` into the cyclic group of order 2, whose kernel
        is exactly the alternating group `A_n`. Partitions of sign
        `1` are called even partitions while partitions of sign
        `-1` are called odd.

        EXAMPLES::

            sage: Partition([5,3]).sign()
            1
            sage: Partition([5,2]).sign()
            -1

        Zolotarev's lemma states that the Legendre symbol
        `\\left(\\frac{a}{p}\\right)` for an integer
        `a \\pmod p` (`p` a prime number), can be computed
        as sign(p_a), where sign denotes the sign of a permutation and
        p_a the permutation of the residue classes `\\pmod p`
        induced by modular multiplication by `a`, provided
        `p` does not divide `a`.

        We verify this in some examples.

        ::

            sage: F = GF(11)                                                            # needs sage.rings.finite_rings
            sage: a = F.multiplicative_generator();a                                    # needs sage.rings.finite_rings
            2
            sage: plist = [int(a*F(x)) for x in range(1,11)]; plist                     # needs sage.rings.finite_rings
            [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

        This corresponds to the permutation (1, 2, 4, 8, 5, 10, 9, 7, 3, 6)
        (acting the set `\\{1,2,...,10\\}`) and to the partition
        [10].

        ::

            sage: p = PermutationGroupElement('(1, 2, 4, 8, 5, 10, 9, 7, 3, 6)')        # needs sage.groups
            sage: p.sign()                                                              # needs sage.groups
            -1
            sage: Partition([10]).sign()
            -1
            sage: kronecker_symbol(11,2)
            -1

        Now replace `2` by `3`::

            sage: plist = [int(F(3*x)) for x in range(1,11)]; plist                     # needs sage.rings.finite_rings
            [3, 6, 9, 1, 4, 7, 10, 2, 5, 8]
            sage: list(range(1, 11))
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: p = PermutationGroupElement('(3,4,8,7,9)')                            # needs sage.groups
            sage: p.sign()                                                              # needs sage.groups
            1
            sage: kronecker_symbol(3,11)
            1
            sage: Partition([5,1,1,1,1,1]).sign()
            1

        In both cases, Zolotarev holds.

        REFERENCES:

        - :wikipedia:`Zolotarev%27s_lemma`
        """
    def k_size(self, k):
        """
        Given a partition ``self`` and a ``k``, return the size of the
        `k`-boundary.

        This is the same as the length method
        :meth:`sage.combinat.core.Core.length` of the
        :class:`sage.combinat.core.Core` object, with the exception that here we
        don't require ``self`` to be a `k+1`-core.

        EXAMPLES::

            sage: Partition([2, 1, 1]).k_size(1)
            2
            sage: Partition([2, 1, 1]).k_size(2)
            3
            sage: Partition([2, 1, 1]).k_size(3)
            3
            sage: Partition([2, 1, 1]).k_size(4)
            4

        .. SEEALSO::

            :meth:`k_boundary`, :meth:`SkewPartition.size`
        """
    def boundary(self):
        """
        Return the integer coordinates of points on the boundary of ``self``.

        For the following description, picture the Ferrer's diagram of ``self``
        using the French convention.  Recall that the French convention puts
        the longest row on the bottom and the shortest row on the top.  In
        addition, interpret the Ferrer's diagram as 1 x 1 cells in the Euclidean
        plane.  So if ``self`` was the partition [3, 1], the lower-left vertices
        of the 1 x 1 cells in the Ferrer's diagram would be (0, 0), (1, 0),
        (2, 0), and (0, 1).

        The boundary of a partition is the set `\\{ \\text{NE}(d) \\mid \\forall
        d\\:\\text{diagonal} \\}`.  That is, for every diagonal line `y = x + b`
        where `b \\in \\mathbb{Z}`, we find the northeasternmost (NE) point on
        that diagonal which is also in the Ferrer's diagram.

        The boundary will go from bottom-right to top-left.

        EXAMPLES:

        Consider the partition (1) depicted as a square on a cartesian plane
        with vertices (0, 0), (1, 0), (1, 1), and (0, 1).  Three of those
        vertices in the appropriate order form the boundary::

            sage: Partition([1]).boundary()
            [(1, 0), (1, 1), (0, 1)]

        The partition (3, 1) can be visualized as three squares on a cartesian
        plane. The coordinates of the appropriate vertices form the boundary::

            sage: Partition([3, 1]).boundary()
            [(3, 0), (3, 1), (2, 1), (1, 1), (1, 2), (0, 2)]

        TESTS::

            sage: Partition([1]).boundary()
            [(1, 0), (1, 1), (0, 1)]
            sage: Partition([2, 1]).boundary()
            [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
            sage: Partition([3, 1]).boundary()
            [(3, 0), (3, 1), (2, 1), (1, 1), (1, 2), (0, 2)]
            sage: Partition([2, 1, 1]).boundary()
            [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (0, 3)]

        .. SEEALSO::

            :meth:`k_rim`.  You might have been looking for :meth:`k_boundary`
            instead.
        """
    def k_rim(self, k):
        '''
        Return the ``k``-rim of ``self`` as a list of integer coordinates.

        The `k`-rim of a partition is the "line between" (or "intersection of")
        the `k`-boundary and the `k`-interior.  (Section 2.3 of [HM2011]_)

        It will be output as an ordered list of integer coordinates, where the
        origin is `(0, 0)`.  It will start at the top-left of the `k`-rim (using
        French convention) and end at the bottom-right.

        EXAMPLES:

        Consider the partition (3, 1) split up into its 1-interior and
        1-boundary:

        .. image:: ../../media/k-rim.JPG
            :height: 180px
            :align: center

        The line shown in bold is the 1-rim, and that information is equivalent
        to the integer coordinates of the points that occur along that line::

            sage: Partition([3, 1]).k_rim(1)
            [(3, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)]

        TESTS::

            sage: Partition([1]).k_rim(0)
            [(1, 0),  (1, 1),  (0, 1)]
            sage: Partition([3,  1]).k_rim(0)
            [(3, 0),  (3, 1),  (2, 1),  (1, 1),  (1, 2),  (0, 2)]
            sage: Partition([3,  1]).k_rim(1)
            [(3, 0),  (2, 0),  (2, 1),  (1, 1),  (0, 1),  (0, 2)]
            sage: Partition([3,  1]).k_rim(2)
            [(3, 0),  (2, 0),  (1, 0),  (1, 1),  (0, 1),  (0, 2)]
            sage: Partition([3,  1]).k_rim(3)
            [(3, 0),  (2, 0),  (1, 0),  (1, 1),  (0, 1),  (0, 2)]

        .. SEEALSO::

            :meth:`k_interior`, :meth:`k_boundary`, :meth:`boundary`
        '''
    def k_row_lengths(self, k):
        """
        Return the ``k``-row-shape of the partition ``self``.

        This is equivalent to taking the `k`-boundary of the partition and then
        returning the row-shape of that.  We do *not* discard rows of length 0.
        (Section 2.2 of [LLMS2013]_)

        EXAMPLES::

            sage: Partition([6, 1]).k_row_lengths(2)
            [2, 1]

            sage: Partition([4, 4, 4, 3, 2]).k_row_lengths(2)
            [0, 1, 1, 1, 2]

        .. SEEALSO::

            :meth:`k_column_lengths`, :meth:`k_boundary`,
            :meth:`SkewPartition.row_lengths`,
            :meth:`SkewPartition.column_lengths`
        """
    def k_column_lengths(self, k):
        """
        Return the ``k``-column-shape of the partition ``self``.

        This is the 'column' analog of :meth:`k_row_lengths`.

        EXAMPLES::

            sage: Partition([6, 1]).k_column_lengths(2)
            [1, 0, 0, 0, 1, 1]

            sage: Partition([4, 4, 4, 3, 2]).k_column_lengths(2)
            [1, 1, 1, 2]

        .. SEEALSO::

            :meth:`k_row_lengths`, :meth:`k_boundary`,
            :meth:`SkewPartition.row_lengths`,
            :meth:`SkewPartition.column_lengths`
        """
    def has_rectangle(self, h, w) -> bool:
        """
        Return ``True`` if the Ferrer's diagram of ``self`` has ``h``
        (*or more*) rows of length ``w`` (*exactly*).

        INPUT:

        - ``h`` -- integer `h \\geq 1`;  the (*minimum*) height of the
          rectangle

        - ``w`` -- integer `w \\geq 1`;  the width of the rectangle

        EXAMPLES::

            sage: Partition([3, 3, 3, 3]).has_rectangle(2, 3)
            True
            sage: Partition([3, 3]).has_rectangle(2, 3)
            True
            sage: Partition([4, 3]).has_rectangle(2, 3)
            False
            sage: Partition([3]).has_rectangle(2, 3)
            False

        TESTS::

            sage: Partition([1, 1, 1]).has_rectangle(4, 1)
            False
            sage: Partition([1, 1, 1]).has_rectangle(3, 1)
            True
            sage: Partition([1, 1, 1]).has_rectangle(2, 1)
            True
            sage: Partition([1, 1, 1]).has_rectangle(1, 2)
            False
            sage: Partition([3]).has_rectangle(1, 3)
            True
            sage: Partition([3]).has_rectangle(1, 2)
            False
            sage: Partition([3]).has_rectangle(2, 3)
            False

        .. SEEALSO::

            :meth:`has_k_rectangle`
        """
    def has_k_rectangle(self, k) -> bool:
        """
        Return ``True`` if the Ferrer's diagram of ``self`` contains `k-i+1`
        rows (*or more*) of length `i` (*exactly*) for any `i` in `[1, k]`.

        This is mainly a helper function for :meth:`is_k_reducible` and
        :meth:`is_k_irreducible`, the only difference between this function and
        :meth:`is_k_reducible` being that this function allows any partition as
        input while :meth:`is_k_reducible` requires the input to be `k`-bounded.

        EXAMPLES:

        The partition [1, 1, 1] has at least 2 rows of length 1::

            sage: Partition([1, 1, 1]).has_k_rectangle(2)
            True

        The partition [1, 1, 1] does *not* have 4 rows of length 1, 3 rows of
        length 2, 2 rows of length 3, nor 1 row of length 4::

            sage: Partition([1, 1, 1]).has_k_rectangle(4)
            False

        TESTS::

            sage: Partition([1]).has_k_rectangle(1)
            True
            sage: Partition([1]).has_k_rectangle(2)
            False
            sage: Partition([1, 1, 1]).has_k_rectangle(3)
            True
            sage: Partition([1, 1, 1]).has_k_rectangle(2)
            True
            sage: Partition([1, 1, 1]).has_k_rectangle(4)
            False
            sage: Partition([3]).has_k_rectangle(3)
            True
            sage: Partition([3]).has_k_rectangle(2)
            False
            sage: Partition([3]).has_k_rectangle(4)
            False

        .. SEEALSO::

            :meth:`is_k_irreducible`, :meth:`is_k_reducible`,
            :meth:`has_rectangle`
        """
    def is_k_bounded(self, k) -> bool:
        """
        Return ``True`` if the partition ``self`` is bounded by ``k``.

        EXAMPLES::

            sage: Partition([4, 3, 1]).is_k_bounded(4)
            True
            sage: Partition([4, 3, 1]).is_k_bounded(7)
            True
            sage: Partition([4, 3, 1]).is_k_bounded(3)
            False
        """
    def is_k_reducible(self, k):
        """
        Return ``True`` if the partition ``self`` is ``k``-reducible.

        A `k`-bounded partition is `k`-*reducible* if its Ferrer's diagram
        contains `k-i+1` rows (or more) of length `i` (exactly) for some
        `i \\in [1, k]`.

        (Also, a `k`-bounded partition is `k`-reducible if and only if it is not `k`-irreducible.)

        EXAMPLES:

        The partition [1, 1, 1] has at least 2 rows of length 1::

            sage: Partition([1, 1, 1]).is_k_reducible(2)
            True

        The partition [1, 1, 1] does *not* have 4 rows of length 1, 3 rows of
        length 2, 2 rows of length 3, nor 1 row of length 4::

            sage: Partition([1, 1, 1]).is_k_reducible(4)
            False

        .. SEEALSO::

            :meth:`is_k_irreducible`, :meth:`has_k_rectangle`
        """
    def is_k_irreducible(self, k):
        """
        Return ``True`` if the partition ``self`` is ``k``-irreducible.

        A `k`-bounded partition is `k`-*irreducible* if its Ferrer's diagram
        does *not* contain `k-i+1` rows (or more) of length `i` (exactly) for
        every `i \\in [1, k]`.

        (Also, a `k`-bounded partition is `k`-irreducible if and only if it is
        not `k`-reducible.)

        EXAMPLES:

        The partition [1, 1, 1] has at least 2 rows of length 1::

            sage: Partition([1, 1, 1]).is_k_irreducible(2)
            False

        The partition [1, 1, 1] does *not* have 4 rows of length 1, 3 rows of
        length 2, 2 rows of length 3, nor 1 row of length 4::

            sage: Partition([1, 1, 1]).is_k_irreducible(4)
            True

        .. SEEALSO::

            :meth:`is_k_reducible`, :meth:`has_k_rectangle`
        """
    def is_symmetric(self):
        """
        Return ``True`` if the partition ``self`` equals its own transpose.

        EXAMPLES::

            sage: Partition([2, 1]).is_symmetric()
            True
            sage: Partition([3, 1]).is_symmetric()
            False
        """
    def next_within_bounds(self, min=[], max=None, partition_type=None):
        """
        Get the next partition lexicographically that contains ``min`` and is
        contained in ``max``.

        INPUT:

        - ``min`` -- (default: ``[]``, the empty partition) the
          'minimum partition' that ``next_within_bounds(self)`` must contain

        - ``max`` -- (default: ``None``) the 'maximum partition' that
          ``next_within_bounds(self)`` must be contained in;  if set to ``None``,
          then there is no restriction

        - ``partition_type`` -- (default: ``None``) the type of partitions
          allowed;  for example, 'strict' for strictly decreasing partitions, or
          ``None`` to allow any valid partition

        EXAMPLES::

            sage: m = [1, 1]
            sage: M = [3, 2, 1]
            sage: Partition([1, 1]).next_within_bounds(min=m, max=M)
            [1, 1, 1]
            sage: Partition([1, 1, 1]).next_within_bounds(min=m, max=M)
            [2, 1]
            sage: Partition([2, 1]).next_within_bounds(min=m, max=M)
            [2, 1, 1]
            sage: Partition([2, 1, 1]).next_within_bounds(min=m, max=M)
            [2, 2]
            sage: Partition([2, 2]).next_within_bounds(min=m, max=M)
            [2, 2, 1]
            sage: Partition([2, 2, 1]).next_within_bounds(min=m, max=M)
            [3, 1]
            sage: Partition([3, 1]).next_within_bounds(min=m, max=M)
            [3, 1, 1]
            sage: Partition([3, 1, 1]).next_within_bounds(min=m, max=M)
            [3, 2]
            sage: Partition([3, 2]).next_within_bounds(min=m, max=M)
            [3, 2, 1]
            sage: Partition([3, 2, 1]).next_within_bounds(min=m, max=M) == None
            True

        .. SEEALSO::

            :meth:`next`
        """
    def row_standard_tableaux(self):
        """
        Return the :class:`row standard tableaux
        <sage.combinat.tableau.RowStandardTableaux>` of shape ``self``.

        EXAMPLES::

            sage: Partition([3,2,2,1]).row_standard_tableaux()
            Row standard tableaux of shape [3, 2, 2, 1]
        """
    def standard_tableaux(self):
        """
        Return the :class:`standard tableaux<StandardTableaux>`
        of shape ``self``.

        EXAMPLES::

            sage: Partition([3,2,2,1]).standard_tableaux()
            Standard tableaux of shape [3, 2, 2, 1]
        """
    def up(self) -> Generator[Incomplete]:
        """
        Return a generator for partitions that can be obtained from ``self``
        by adding a cell.

        EXAMPLES::

            sage: list(Partition([2,1,1]).up())
            [[3, 1, 1], [2, 2, 1], [2, 1, 1, 1]]
            sage: list(Partition([3,2]).up())
            [[4, 2], [3, 3], [3, 2, 1]]
            sage: [p for p in Partition([]).up()]
            [[1]]
        """
    def up_list(self):
        """
        Return a list of the partitions that can be formed from ``self`` by
        adding a cell.

        EXAMPLES::

            sage: Partition([2,1,1]).up_list()
            [[3, 1, 1], [2, 2, 1], [2, 1, 1, 1]]
            sage: Partition([3,2]).up_list()
            [[4, 2], [3, 3], [3, 2, 1]]
            sage: Partition([]).up_list()
            [[1]]
        """
    def down(self) -> Generator[Incomplete]:
        """
        Return a generator for partitions that can be obtained from ``self``
        by removing a cell.

        EXAMPLES::

            sage: [p for p in Partition([2,1,1]).down()]
            [[1, 1, 1], [2, 1]]
            sage: [p for p in Partition([3,2]).down()]
            [[2, 2], [3, 1]]
            sage: [p for p in Partition([3,2,1]).down()]
            [[2, 2, 1], [3, 1, 1], [3, 2]]

        TESTS:

        We check that :issue:`11435` is fixed::

            sage: Partition([]).down_list() #indirect doctest
            []
        """
    def down_list(self):
        """
        Return a list of the partitions that can be obtained from ``self``
        by removing a cell.

        EXAMPLES::

            sage: Partition([2,1,1]).down_list()
            [[1, 1, 1], [2, 1]]
            sage: Partition([3,2]).down_list()
            [[2, 2], [3, 1]]
            sage: Partition([3,2,1]).down_list()
            [[2, 2, 1], [3, 1, 1], [3, 2]]
            sage: Partition([]).down_list()  #checks :issue:`11435`
            []
        """
    def cell_poset(self, orientation: str = 'SE'):
        '''
        Return the Young diagram of ``self`` as a poset. The optional
        keyword variable ``orientation`` determines the order relation
        of the poset.

        The poset always uses the set of cells of the Young diagram
        of ``self`` as its ground set. The order relation of the poset
        depends on the ``orientation`` variable (which defaults to
        ``\'SE\'``). Concretely, ``orientation`` has to be specified to
        one of the strings ``\'NW\'``, ``\'NE\'``, ``\'SW\'``, and ``\'SE\'``,
        standing for "northwest", "northeast", "southwest" and
        "southeast", respectively. If ``orientation`` is ``\'SE\'``, then
        the order relation of the poset is such that a cell `u` is
        greater or equal to a cell `v` in the poset if and only if `u`
        lies weakly southeast of `v` (this means that `u` can be
        reached from `v` by a sequence of south and east steps; the
        sequence is allowed to consist of south steps only, or of east
        steps only, or even be empty). Similarly the order relation is
        defined for the other three orientations. The Young diagram is
        supposed to be drawn in English notation.

        The elements of the poset are the cells of the Young diagram
        of ``self``, written as tuples of zero-based coordinates (so
        that `(3, 7)` stands for the `8`-th cell of the `4`-th row,
        etc.).

        EXAMPLES::

            sage: # needs sage.graphs
            sage: p = Partition([3,3,1])
            sage: Q = p.cell_poset(); Q
            Finite poset containing 7 elements
            sage: sorted(Q)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
            sage: sorted(Q.maximal_elements())
            [(1, 2), (2, 0)]
            sage: Q.minimal_elements()
            [(0, 0)]
            sage: sorted(Q.upper_covers((1, 0)))
            [(1, 1), (2, 0)]
            sage: Q.upper_covers((1, 1))
            [(1, 2)]

            sage: # needs sage.graphs
            sage: P = p.cell_poset(orientation="NW"); P
            Finite poset containing 7 elements
            sage: sorted(P)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
            sage: sorted(P.minimal_elements())
            [(1, 2), (2, 0)]
            sage: P.maximal_elements()
            [(0, 0)]
            sage: P.upper_covers((2, 0))
            [(1, 0)]
            sage: sorted(P.upper_covers((1, 2)))
            [(0, 2), (1, 1)]
            sage: sorted(P.upper_covers((1, 1)))
            [(0, 1), (1, 0)]
            sage: sorted([len(P.upper_covers(v)) for v in P])
            [0, 1, 1, 1, 1, 2, 2]

            sage: # needs sage.graphs
            sage: R = p.cell_poset(orientation="NE"); R
            Finite poset containing 7 elements
            sage: sorted(R)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
            sage: R.maximal_elements()
            [(0, 2)]
            sage: R.minimal_elements()
            [(2, 0)]
            sage: sorted([len(R.upper_covers(v)) for v in R])
            [0, 1, 1, 1, 1, 2, 2]
            sage: R.is_isomorphic(P)
            False
            sage: R.is_isomorphic(P.dual())
            False

        Linear extensions of ``p.cell_poset()`` are in 1-to-1 correspondence
        with standard Young tableaux of shape `p`::

            sage: all( len(p.cell_poset().linear_extensions())                          # needs sage.graphs
            ....:      == len(p.standard_tableaux())
            ....:      for n in range(8) for p in Partitions(n) )
            True

        This is not the case for northeast orientation::

            sage: q = Partition([3, 1])
            sage: q.cell_poset(orientation="NE").is_chain()                             # needs sage.graphs
            True

        TESTS:

        We check that the posets are really what they should be for size
        up to `7`::

            sage: def check_NW(n):
            ....:     for p in Partitions(n):
            ....:         P = p.cell_poset(orientation="NW")
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.le(c, d) != (c[0] >= d[0]
            ....:                                   and c[1] >= d[1]):
            ....:                     return False
            ....:     return True
            sage: all( check_NW(n) for n in range(8) )                                  # needs sage.graphs
            True

            sage: def check_NE(n):
            ....:     for p in Partitions(n):
            ....:         P = p.cell_poset(orientation="NE")
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.le(c, d) != (c[0] >= d[0]
            ....:                                   and c[1] <= d[1]):
            ....:                     return False
            ....:     return True
            sage: all( check_NE(n) for n in range(8) )                                  # needs sage.graphs
            True

            sage: def test_duality(n, ori1, ori2):
            ....:     for p in Partitions(n):
            ....:         P = p.cell_poset(orientation=ori1)
            ....:         Q = p.cell_poset(orientation=ori2)
            ....:         for c in p.cells():
            ....:             for d in p.cells():
            ....:                 if P.lt(c, d) != Q.lt(d, c):
            ....:                     return False
            ....:     return True
            sage: all( test_duality(n, "NW", "SE") for n in range(8) )                  # needs sage.graphs
            True
            sage: all( test_duality(n, "NE", "SW") for n in range(8) )                  # needs sage.graphs
            True
            sage: all( test_duality(n, "NE", "SE") for n in range(4) )                  # needs sage.graphs
            False
        '''
    def frobenius_coordinates(self) -> tuple[list, list]:
        """
        Return a pair of sequences of Frobenius coordinates aka beta numbers
        of the partition.

        These are two strictly decreasing sequences of nonnegative integers
        of the same length.

        EXAMPLES::

            sage: Partition([]).frobenius_coordinates()
            ([], [])
            sage: Partition([1]).frobenius_coordinates()
            ([0], [0])
            sage: Partition([3,3,3]).frobenius_coordinates()
            ([2, 1, 0], [2, 1, 0])
            sage: Partition([9,1,1,1,1,1,1]).frobenius_coordinates()
            ([8], [6])
        """
    def frobenius_rank(self):
        """
        Return the Frobenius rank of the partition ``self``.

        The Frobenius rank of a partition
        `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3, \\cdots)` is
        defined to be the largest `i` such that `\\lambda_i \\geq i`.
        In other words, it is the number of cells on the main diagonal
        of `\\lambda`. In yet other words, it is the size of the largest
        square fitting into the Young diagram of `\\lambda`.

        EXAMPLES::

            sage: Partition([]).frobenius_rank()
            0
            sage: Partition([1]).frobenius_rank()
            1
            sage: Partition([3,3,3]).frobenius_rank()
            3
            sage: Partition([9,1,1,1,1,1]).frobenius_rank()
            1
            sage: Partition([2,1,1,1,1,1]).frobenius_rank()
            1
            sage: Partition([2,2,1,1,1,1]).frobenius_rank()
            2
            sage: Partition([3,2]).frobenius_rank()
            2
            sage: Partition([3,2,2]).frobenius_rank()
            2
            sage: Partition([8,4,4,4,4]).frobenius_rank()
            4
            sage: Partition([8,4,1]).frobenius_rank()
            2
            sage: Partition([3,3,1]).frobenius_rank()
            2
        """
    def beta_numbers(self, length=None):
        """
        Return the set of beta numbers corresponding to ``self``.

        The optional argument ``length`` specifies the length of the beta set
        (which must be at least the length of ``self``).

        For more on beta numbers, see :meth:`frobenius_coordinates`.

        EXAMPLES::

            sage: Partition([4,3,2]).beta_numbers()
            [6, 4, 2]
            sage: Partition([4,3,2]).beta_numbers(5)
            [8, 6, 4, 1, 0]
            sage: Partition([]).beta_numbers()
            []
            sage: Partition([]).beta_numbers(3)
            [2, 1, 0]
            sage: Partition([6,4,1,1]).beta_numbers()
            [9, 6, 2, 1]
            sage: Partition([6,4,1,1]).beta_numbers(6)
            [11, 8, 4, 3, 1, 0]
            sage: Partition([1,1,1]).beta_numbers()
            [3, 2, 1]
            sage: Partition([1,1,1]).beta_numbers(4)
            [4, 3, 2, 0]
        """
    def crank(self):
        """
        Return the Dyson crank of ``self``.

        The Dyson crank of a partition `\\lambda` is defined as follows:
        If `\\lambda` contains at least one `1`, then the crank is
        `\\mu(\\lambda) - \\omega(\\lambda)`, where `\\omega(\\lambda)` is the
        number of `1`s in `\\lambda`, and `\\mu(\\lambda)` is the number of
        parts of `\\lambda` larger than `\\omega(\\lambda)`. If `\\lambda`
        contains no `1`, then the crank is simply the largest part of
        `\\lambda`.

        REFERENCES:

        - [AG1988]_

        EXAMPLES::

            sage: Partition([]).crank()
            0
            sage: Partition([3,2,2]).crank()
            3
            sage: Partition([5,4,2,1,1]).crank()
            0
            sage: Partition([1,1,1]).crank()
            -3
            sage: Partition([6,4,4,3]).crank()
            6
            sage: Partition([6,3,3,1,1]).crank()
            1
            sage: Partition([6]).crank()
            6
            sage: Partition([5,1]).crank()
            0
            sage: Partition([4,2]).crank()
            4
            sage: Partition([4,1,1]).crank()
            -1
            sage: Partition([3,3]).crank()
            3
            sage: Partition([3,2,1]).crank()
            1
            sage: Partition([3,1,1,1]).crank()
            -3
            sage: Partition([2,2,2]).crank()
            2
            sage: Partition([2,2,1,1]).crank()
            -2
            sage: Partition([2,1,1,1,1]).crank()
            -4
            sage: Partition([1,1,1,1,1,1]).crank()
            -6
        """
    def t_completion(self, t):
        """
        Return the ``t``-completion of the partition ``self``.

        If `\\lambda = (\\lambda_1, \\lambda_2, \\lambda_3, \\ldots)` is a
        partition and `t` is an integer greater or equal to
        `\\left\\lvert \\lambda \\right\\rvert + \\lambda_1`, then the
        `t`-*completion of* `\\lambda` is defined as the partition
        `(t - \\left\\lvert \\lambda \\right\\rvert, \\lambda_1, \\lambda_2,
        \\lambda_3, \\ldots)` of `t`. This partition is denoted by `\\lambda[t]`
        in [BOR2009]_, by `\\lambda_{[t]}` in [BdVO2012]_, and by `\\lambda(t)`
        in [CO2010]_.

        EXAMPLES::

            sage: Partition([]).t_completion(0)
            []
            sage: Partition([]).t_completion(1)
            [1]
            sage: Partition([]).t_completion(2)
            [2]
            sage: Partition([]).t_completion(3)
            [3]
            sage: Partition([2, 1]).t_completion(5)
            [2, 2, 1]
            sage: Partition([2, 1]).t_completion(6)
            [3, 2, 1]
            sage: Partition([4, 2, 2, 1]).t_completion(13)
            [4, 4, 2, 2, 1]
            sage: Partition([4, 2, 2, 1]).t_completion(19)
            [10, 4, 2, 2, 1]
            sage: Partition([4, 2, 2, 1]).t_completion(10)
            Traceback (most recent call last):
            ...
            ValueError: 10-completion is not defined
            sage: Partition([4, 2, 2, 1]).t_completion(5)
            Traceback (most recent call last):
            ...
            ValueError: 5-completion is not defined
        """
    def larger_lex(self, rhs):
        """
        Return ``True`` if ``self`` is larger than ``rhs`` in lexicographic
        order. Otherwise return ``False``.

        EXAMPLES::

            sage: p = Partition([3,2])
            sage: p.larger_lex([3,1])
            True
            sage: p.larger_lex([1,4])
            True
            sage: p.larger_lex([3,2,1])
            False
            sage: p.larger_lex([3])
            True
            sage: p.larger_lex([5])
            False
            sage: p.larger_lex([3,1,1,1,1,1,1,1])
            True
        """
    def dominates(self, p2):
        """
        Return ``True`` if ``self`` dominates the partition ``p2``. Otherwise
        it returns ``False``.

        EXAMPLES::

            sage: p = Partition([3,2])
            sage: p.dominates([3,1])
            True
            sage: p.dominates([2,2])
            True
            sage: p.dominates([2,1,1])
            True
            sage: p.dominates([3,3])
            False
            sage: p.dominates([4])
            False
            sage: Partition([4]).dominates(p)
            False
            sage: Partition([]).dominates([1])
            False
            sage: Partition([]).dominates([])
            True
            sage: Partition([1]).dominates([])
            True
        """
    def cells(self):
        """
        Return the coordinates of the cells of ``self``.

        EXAMPLES::

            sage: Partition([2,2]).cells()
            [(0, 0), (0, 1), (1, 0), (1, 1)]
            sage: Partition([3,2]).cells()
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
        """
    def generalized_pochhammer_symbol(self, a, alpha):
        """
        Return the generalized Pochhammer symbol
        `(a)_{self}^{(\\alpha)}`. This is the product over all
        cells `(i,j)` in ``self`` of `a - (i-1) / \\alpha + j - 1`.

        EXAMPLES::

            sage: Partition([2,2]).generalized_pochhammer_symbol(2,1)
            12
        """
    def get_part(self, i, default=...):
        """
        Return the `i`-th part of ``self``, or ``default`` if it does
        not exist.

        EXAMPLES::

            sage: p = Partition([2,1])
            sage: p.get_part(0), p.get_part(1), p.get_part(2)
            (2, 1, 0)
            sage: p.get_part(10,-1)
            -1
            sage: Partition([]).get_part(0)
            0
        """
    def to_dyck_word(self, n=None):
        """
        Return the ``n``-Dyck word whose corresponding partition is
        ``self`` (or, if ``n`` is not specified, the `n`-Dyck word with
        smallest `n` to satisfy this property).

        If `w` is an `n`-Dyck word (that is, a Dyck word with `n` open
        symbols and `n` close symbols), then the Dyck path corresponding
        to `w` can be regarded as a lattice path in the northeastern
        half of an `n \\times n`-square. The region to the northeast of
        this Dyck path can be regarded as a partition. It is called the
        partition corresponding to the Dyck word `w`. (See
        :meth:`~sage.combinat.dyck_word.DyckWord.to_partition`.)

        For every partition `\\lambda` and every nonnegative integer `n`,
        there exists at most one `n`-Dyck word `w` such that the
        partition corresponding to `w` is `\\lambda` (in fact, such `w`
        exists if and only if `\\lambda_i + i \\leq n` for every `i`,
        where `\\lambda` is written in the form
        `(\\lambda_1, \\lambda_2, \\ldots, \\lambda_k)` with `\\lambda_k > 0`).
        This method computes this `w` for a given `\\lambda` and `n`.
        If `n` is not specified, this method computes the `w` for the
        smallest possible `n` for which such an `w` exists.
        (The minimality of `n` means that the partition demarcated by the
        Dyck path touches the diagonal.)

        EXAMPLES::

            sage: Partition([2,2]).to_dyck_word()
            [1, 1, 0, 0, 1, 1, 0, 0]
            sage: Partition([2,2]).to_dyck_word(4)
            [1, 1, 0, 0, 1, 1, 0, 0]
            sage: Partition([2,2]).to_dyck_word(5)
            [1, 1, 1, 0, 0, 1, 1, 0, 0, 0]
            sage: Partition([6,3,1]).to_dyck_word()
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
            sage: Partition([]).to_dyck_word()
            []
            sage: Partition([]).to_dyck_word(3)
            [1, 1, 1, 0, 0, 0]

        The partition corresponding to ``self.dyck_word()`` is ``self``
        indeed::

            sage: all( p.to_dyck_word().to_partition() == p
            ....:      for p in Partitions(5) )
            True
        """
    def conjugate(self):
        """
        Return the conjugate partition of the partition ``self``.

        This is also called the associated partition or the transpose
        in the literature.

        EXAMPLES::

            sage: Partition([2,2]).conjugate()
            [2, 2]
            sage: Partition([6,3,1]).conjugate()
            [3, 2, 2, 1, 1, 1]

        The conjugate partition is obtained by transposing the Ferrers
        diagram of the partition (see :meth:`.ferrers_diagram`)::

            sage: print(Partition([6,3,1]).ferrers_diagram())
            ******
            ***
            *
            sage: print(Partition([6,3,1]).conjugate().ferrers_diagram())
            ***
            **
            **
            *
            *
            *
        """
    def glaisher_franklin(self, s):
        """
        Apply the Glaisher-Franklin bijection to ``self``.

        The Franklin-Glaisher bijection, with parameter `s`, returns
        a partition whose set of parts that are repeated at least `s`
        times equals the set of parts divisible by `s` in ``self``,
        after dividing each part by `s`.

        INPUT:

        - ``s`` -- positive integer

        EXAMPLES::

            sage: Partition([4, 3, 2, 2, 1]).glaisher_franklin(2)
            [3, 2, 2, 1, 1, 1, 1, 1]

        TESTS:

        The map preserves the size::

            sage: all(mu.glaisher_franklin(s).size() == n
            ....:     for n in range(20) for mu in Partitions(n)
            ....:     for s in range(1, 5))
            True

        The map is bijective::

            sage: l = [[mu.glaisher_franklin(s)
            ....:      for n in range(20) for mu in Partitions(n)]
            ....:     for s in range(1, 5)]
            sage: all(len(set(ls)) == len(ls) for ls in l)
            True

        The map transports the statistics::

            sage: d = lambda la, s: set(p / s for p in la if p % s == 0)
            sage: r = lambda la, s: set(p for p in la if list(la).count(p) >= s)
            sage: all(d(mu, s) == r(mu.glaisher_franklin(s), s)
            ....:     for n in range(20) for mu in Partitions(n)
            ....:     for s in range(1, 5))
            True

        For `s=2`, the map is known to findstat::

            sage: findmap(Partitions, lambda mu: mu.glaisher_franklin(2))       # optional - internet
            0: Mp00312 (quality [100])
        """
    def glaisher_franklin_inverse(self, s):
        """
        Apply the inverse of the Glaisher-Franklin bijection to ``self``.

        The inverse of the Franklin-Glaisher bijection, with
        parameter `s`, returns a partition whose set of parts that
        are divisible by `s`, after dividing each by `s`, equals the
        equals the set of parts repeated at least `s` times in
        ``self``.

        INPUT:

        - ``s`` -- positive integer

        EXAMPLES::

            sage: Partition([4, 3, 2, 2, 1]).glaisher_franklin(2)
            [3, 2, 2, 1, 1, 1, 1, 1]
            sage: Partition([3, 2, 2, 1, 1, 1, 1, 1]).glaisher_franklin_inverse(2)
            [4, 3, 2, 2, 1]

        TESTS:

        The map is inverse to :meth:`glaisher_franklin`::

            sage: all(mu.glaisher_franklin(s).glaisher_franklin_inverse(s) == mu
            ....:     and mu.glaisher_franklin_inverse(s).glaisher_franklin(s) == mu
            ....:     for n in range(20) for mu in Partitions(n)
            ....:     for s in range(1, 5))
            True

        For `s=2`, the map is known to findstat::

            sage: findmap(Partitions, lambda mu: mu.glaisher_franklin_inverse(2))         # optional - internet
            0: Mp00313 (quality [100])
        """
    def suter_diagonal_slide(self, n, exp: int = 1):
        """
        Return the image of ``self`` in `Y_n` under Suter's diagonal slide
        `\\sigma_n`, where the notations used are those defined in [Sut2002]_.

        The set `Y_n` is defined as the set of all partitions
        `\\lambda` such that the hook length of the `(0, 0)`-cell (i.e. the
        northwestern most cell in English notation) of `\\lambda` is less
        than `n`, including the empty partition.

        The map `\\sigma_n` sends a partition (with nonzero entries)
        `(\\lambda_1, \\lambda_2, \\ldots, \\lambda_m) \\in Y_n` to the partition
        `(\\lambda_2 + 1, \\lambda_3 + 1, \\ldots, \\lambda_m + 1,
        \\underbrace{1, 1, \\ldots, 1}_{n - m - \\lambda_1\\text{ ones}})`.
        In other words, it pads the partition with trailing zeroes
        until it has length `n - \\lambda_1`, then removes its first
        part, and finally adds `1` to each part.

        By Theorem 2.1 of [Sut2002]_, the dihedral group `D_n` with
        `2n` elements acts on `Y_n` by letting the primitive rotation
        act as `\\sigma_n` and the reflection act as conjugation of
        partitions (:meth:`conjugate()`). This action is faithful if
        `n \\geq 3`.

        INPUT:

        - ``n`` -- nonnegative integer

        - ``exp`` -- (default: 1) how many times `\\sigma_n` should be applied

        OUTPUT:

        The result of applying Suter's diagonal slide `\\sigma_n` to
        ``self``, assuming that ``self`` lies in `Y_n`. If the
        optional argument ``exp`` is set, then the slide
        `\\sigma_n` is applied not just once, but ``exp`` times
        (note that ``exp`` is allowed to be negative, since
        the slide has finite order).

        EXAMPLES::

            sage: Partition([5,4,1]).suter_diagonal_slide(8)
            [5, 2]
            sage: Partition([5,4,1]).suter_diagonal_slide(9)
            [5, 2, 1]
            sage: Partition([]).suter_diagonal_slide(7)
            [1, 1, 1, 1, 1, 1]
            sage: Partition([]).suter_diagonal_slide(1)
            []
            sage: Partition([]).suter_diagonal_slide(7, exp=-1)
            [6]
            sage: Partition([]).suter_diagonal_slide(1, exp=-1)
            []
            sage: P7 = Partitions(7)
            sage: all( p == p.suter_diagonal_slide(9, exp=-1).suter_diagonal_slide(9)
            ....:      for p in P7 )
            True
            sage: all( p == p.suter_diagonal_slide(9, exp=3)
            ....:            .suter_diagonal_slide(9, exp=3)
            ....:            .suter_diagonal_slide(9, exp=3)
            ....:      for p in P7 )
            True
            sage: all( p == p.suter_diagonal_slide(9, exp=6)
            ....:            .suter_diagonal_slide(9, exp=6)
            ....:            .suter_diagonal_slide(9, exp=6)
            ....:      for p in P7 )
            True
            sage: all( p == p.suter_diagonal_slide(9, exp=-1)
            ....:            .suter_diagonal_slide(9, exp=1)
            ....:      for p in P7 )
            True

        Check of the assertion in [Sut2002]_ that `\\sigma_n\\bigl( \\sigma_n(
        \\lambda^{\\prime})^{\\prime} \\bigr) = \\lambda`::

            sage: all( p.suter_diagonal_slide(8).conjugate()
            ....:      == p.conjugate().suter_diagonal_slide(8, exp=-1)
            ....:      for p in P7 )
            True

        Check of Claim 1 in [Sut2002]_::

            sage: P5 = Partitions(5)
            sage: all( all( (p.suter_diagonal_slide(6) in q.suter_diagonal_slide(6).down())
            ....:           or (q.suter_diagonal_slide(6) in p.suter_diagonal_slide(6).down())
            ....:           for p in q.down() )
            ....:      for q in P5 )
            True

        TESTS:

        Check for ``exp = 0``::

            sage: P = Partitions(4)
            sage: all(p == p.suter_diagonal_slide(7, 0) for p in P)
            True

        Check for invalid input::

            sage: p = Partition([2,1])
            sage: p.hook_length(0, 0)
            3
            sage: p.suter_diagonal_slide(2)
            Traceback (most recent call last):
            ...
            ValueError: the hook length must be less than n
        """
    def reading_tableau(self):
        """
        Return the RSK recording tableau of the reading word of the
        (standard) tableau `T` labeled down (in English convention)
        each column to the shape of ``self``.

        For an example of the tableau `T`, consider the partition
        `\\lambda = (3,2,1)`, then we have::

            1 4 6
            2 5
            3

        For more, see :func:`~sage.combinat.rsk.RSK()`.

        EXAMPLES::

            sage: Partition([3,2,1]).reading_tableau()
            [[1, 3, 6], [2, 5], [4]]
        """
    def initial_tableau(self):
        """
        Return the :class:`standard tableau<StandardTableau>` which has the
        numbers `1, 2, \\ldots, n` where `n` is the :meth:`size` of ``self``
        entered in order from left to right along the rows of each component,
        where the components are ordered from left to right.

        EXAMPLES::

            sage: Partition([3,2,2]).initial_tableau()
            [[1, 2, 3], [4, 5], [6, 7]]
        """
    def initial_column_tableau(self):
        """
        Return the initial column tableau of shape ``self``.

        The initial column tableau of shape ``self`` is the standard tableau
        that has the numbers `1` to `n`, where `n` is the :meth:`size` of ``self``,
        entered in order from top to bottom and then left to right down the
        columns of ``self``.

        EXAMPLES::

            sage: Partition([3,2]).initial_column_tableau()
            [[1, 3, 5], [2, 4]]
        """
    def garnir_tableau(self, *cell):
        '''
        Return the Garnir tableau of shape ``self`` corresponding to the cell
        ``cell``. If ``cell`` `= (a,c)` then `(a+1,c)` must belong to the
        diagram of ``self``.

        The Garnir tableaux play an important role in integral and
        non-semisimple representation theory because they determine the
        "straightening" rules for the Specht modules over an arbitrary ring.

        The Garnir tableaux are the "first" non-standard tableaux which arise
        when you act by simple transpositions. If `(a,c)` is a cell in the
        Young diagram of a partition, which is not at the bottom of its
        column, then the corresponding Garnir tableau has the integers
        `1, 2, \\ldots, n` entered in order from left to right along the rows
        of the diagram up to the cell `(a,c-1)`, then along the cells
        `(a+1,1)` to `(a+1,c)`, then `(a,c)` until the end of row `a` and
        then continuing from left to right in the remaining positions. The
        examples below probably make this clearer!

        .. NOTE::

            The function also sets ``g._garnir_cell``, where ``g`` is the
            resulting Garnir tableau, equal to ``cell`` which is used by
            some other functions.

        EXAMPLES::

            sage: g = Partition([5,3,3,2]).garnir_tableau((0,2)); g.pp()
              1  2  6  7  8
              3  4  5
              9 10 11
             12 13
            sage: g.is_row_strict(); g.is_column_strict()
            True
            False

            sage: Partition([5,3,3,2]).garnir_tableau(0,2).pp()
              1  2  6  7  8
              3  4  5
              9 10 11
             12 13
            sage: Partition([5,3,3,2]).garnir_tableau(2,1).pp()
              1  2  3  4  5
              6  7  8
              9 12 13
             10 11
            sage: Partition([5,3,3,2]).garnir_tableau(2,2).pp()
            Traceback (most recent call last):
            ...
            ValueError: (row+1, col) must be inside the diagram

        .. SEEALSO::

            - :meth:`top_garnir_tableau`
        '''
    def top_garnir_tableau(self, e, cell):
        '''
        Return the most dominant *standard* tableau which dominates the
        corresponding Garnir tableau and has the same ``e``-residue.

        The Garnir tableau play an important role in integral and non-semisimple
        representation theory because they determine the "straightening" rules
        for the Specht modules. The *top Garnir tableaux* arise in the graded
        representation theory of the symmetric groups and higher level Hecke
        algebras. They were introduced in [KMR2012]_.

        If the Garnir node is ``cell=(r,c)`` and `m` and `M` are the entries
        in the cells ``(r,c)`` and ``(r+1,c)``, respectively, in the initial
        tableau then the top ``e``-Garnir tableau is obtained by inserting the
        numbers `m, m+1, \\ldots, M` in order from left to right first in the
        cells in row ``r+1`` which are not in the ``e``-Garnir belt, then in
        the cell in rows ``r`` and ``r+1`` which are in the Garnir belt and
        then, finally, in the remaining cells in row ``r`` which are not in
        the Garnir belt. All other entries in the tableau remain unchanged.

        If ``e = 0``, or if there are no ``e``-bricks in either row ``r``
        or ``r+1``, then the top Garnir tableau is the corresponding Garnir
        tableau.

        EXAMPLES::

            sage: Partition([5,4,3,2]).top_garnir_tableau(2,(0,2)).pp()
               1  2  4  5  8
               3  6  7  9
              10 11 12
              13 14
            sage: Partition([5,4,3,2]).top_garnir_tableau(3,(0,2)).pp()
               1  2  3  4  5
               6  7  8  9
              10 11 12
              13 14
            sage: Partition([5,4,3,2]).top_garnir_tableau(4,(0,2)).pp()
               1  2  6  7  8
               3  4  5  9
              10 11 12
              13 14
            sage: Partition([5,4,3,2]).top_garnir_tableau(0,(0,2)).pp()
               1  2  6  7  8
               3  4  5  9
              10 11 12
              13 14

        TESTS::

            sage: Partition([5,4,3,2]).top_garnir_tableau(0,(3,2)).pp()
            Traceback (most recent call last):
            ...
            ValueError: (4,2)=(row+1,col) must be inside the diagram

        REFERENCES:

        - [KMR2012]_
        '''
    def ladder_tableau(self, e, ladder_lengths: bool = False):
        """
        Return the ladder tableau of shape ``self``.

        The `e`-*ladder tableau* is the standard Young tableau obtained
        by reading the *ladders*, the set of cells `(i, j)` that differ
        from `(i+e-1, j-1)`, of the partition `\\lambda` from left-to-right.

        INPUT:

        - ``e`` -- nonnegative integer; `0` is considered as `\\infty`
          (analogous to the characteristic of a ring)
        - ``ladder_sizes`` -- boolean (default: ``False``); if ``True``, also
          return the sizes of the ladders

        .. SEEALSO::

            :meth:`ladders`

        EXAMPLES::

            sage: la = Partition([6, 5, 3, 1])
            sage: ascii_art(la.ladder_tableau(3))
              1  2  3  5  7 10
              4  6  8 11 13
              9 12 14
             15
            sage: la.ladder_tableau(3, ladder_lengths=True)[1]
            [1, 1, 2, 2, 3, 3, 3]

            sage: ascii_art(la.ladder_tableau(0))
              1  2  3  4  5  6
              7  8  9 10 11
             12 13 14
             15
            sage: all(ll == 1 for ll in la.ladder_tableau(0, ladder_lengths=True)[1])
            True
        """
    def ladders(self, e):
        """
        Return a dictionary containing the ladders in the diagram of ``self``.

        For `e > 0`, a node `(i, j)` in a partition belongs to the `l`-th
        `e`-ladder if `l = (e - 1) r + c`.

        INPUT:

        - ``e`` -- nonnegative integer; if ``0``, then we
          set ``e = self.size() + 1``

        EXAMPLES::

            sage: Partition([3, 2]).ladders(3)
            {0: [(0, 0)], 1: [(0, 1)], 2: [(0, 2), (1, 0)], 3: [(1, 1)]}

        When ``e`` is ``0``, the cells are in bijection with the ladders,
        but the index of the ladder depends on the size of the partition::

            sage: Partition([3, 2]).ladders(0)
            {0: [(0, 0)], 1: [(0, 1)], 2: [(0, 2)], 5: [(1, 0)], 6: [(1, 1)]}
            sage: Partition([3, 2, 1]).ladders(0)
            {0: [(0, 0)], 1: [(0, 1)], 2: [(0, 2)], 6: [(1, 0)], 7: [(1, 1)],
             12: [(2, 0)]}
            sage: Partition([3, 1, 1]).ladders(0)
            {0: [(0, 0)], 1: [(0, 1)], 2: [(0, 2)], 5: [(1, 0)], 10: [(2, 0)]}
            sage: Partition([1, 1, 1]).ladders(0)
            {0: [(0, 0)], 3: [(1, 0)], 6: [(2, 0)]}
        """
    @cached_method
    def young_subgroup(self):
        """
        Return the corresponding Young, or parabolic, subgroup of the symmetric
        group.

        The Young subgroup of a partition
        `\\lambda = (\\lambda_1, \\lambda_2, \\ldots, \\lambda_{\\ell})` of `n` is
        the group:

        .. MATH::

            S_{\\lambda_1} \\times S_{\\lambda_2} \\times \\cdots \\times
            S_{\\lambda_{\\ell}}

        embedded into `S_n` in the standard way (i.e.,
        the `S_{\\lambda_i}` factor acts on the numbers from
        `\\lambda_1 + \\lambda_2 + \\cdots + \\lambda_{i-1} + 1` to
        `\\lambda_1 + \\lambda_2 + \\cdots + \\lambda_i`).

        EXAMPLES::

            sage: Partition([4,2]).young_subgroup()                                     # needs sage.groups
            Permutation Group with generators [(), (5,6), (3,4), (2,3), (1,2)]
        """
    def young_subgroup_generators(self):
        """
        Return an indexing set for the generators of the corresponding Young
        subgroup. Here the generators correspond to the simple adjacent
        transpositions `s_i = (i \\; i+1)`.

        EXAMPLES::

            sage: Partition([4,2]).young_subgroup_generators()
            [1, 2, 3, 5]
            sage: Partition([1,1,1]).young_subgroup_generators()
            []
            sage: Partition([2,2]).young_subgroup_generators()
            [1, 3]

        .. SEEALSO::

            :meth:`young_subgroup`
        """
    def degree(self, e):
        '''
        Return the ``e``-th degree of ``self``.

        The `e`-th degree of a partition `\\lambda` is the sum of the `e`-th
        degrees of the standard tableaux of shape `\\lambda`. The `e`-th degree
        is the exponent of `\\Phi_e(q)` in the Gram determinant of the Specht
        module for a semisimple Iwahori-Hecke algebra of type `A` with
        parameter `q`.

        INPUT:

        - ``e`` -- an  integer  `e > 1`

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: Partition([4,3]).degree(2)
            28
            sage: Partition([4,3]).degree(3)
            15
            sage: Partition([4,3]).degree(4)
            8
            sage: Partition([4,3]).degree(5)
            13
            sage: Partition([4,3]).degree(6)
            0
            sage: Partition([4,3]).degree(7)
            0

        Therefore, the Gram determinant of `S(5,3)` when the Hecke parameter
        `q` is "generic" is

        .. MATH::

            q^N \\Phi_2(q)^{28} \\Phi_3(q)^{15} \\Phi_4(q)^8 \\Phi_5(q)^{13}

        for some integer `N`. Compare with :meth:`prime_degree`.
        '''
    def prime_degree(self, p):
        """
        Return the prime degree for the prime integer``p`` for ``self``.

        INPUT:

        - ``p`` -- prime integer

        OUTPUT: nonnegative integer

        The degree of a partition `\\lambda` is the sum of the
        `e`-:meth:`degree` of the standard tableaux of shape `\\lambda`, for
        `e` a power of the prime `p`. The prime degree gives the exponent of
        `p` in the Gram determinant of the integral Specht module of the
        symmetric group.

        EXAMPLES::

            sage: Partition([4,3]).prime_degree(2)
            36
            sage: Partition([4,3]).prime_degree(3)
            15
            sage: Partition([4,3]).prime_degree(5)
            13
            sage: Partition([4,3]).prime_degree(7)
            0

        Therefore, the Gram determinant of `S(5,3)` when `q = 1` is
        `2^{36} 3^{15} 5^{13}`.  Compare with :meth:`degree`.
        """
    def arm_length(self, i, j):
        """
        Return the length of the arm of cell `(i,j)` in ``self``.

        The arm of cell `(i,j)` is the cells that appear to the right of
        cell `(i,j)`.

        The cell coordinates are zero-based, i. e., the northwesternmost
        cell is `(0,0)`.

        INPUT:

        - ``i``, ``j`` -- two integers

        OUTPUT: integer or a :exc:`ValueError`

        EXAMPLES::

            sage: p = Partition([2,2,1])
            sage: p.arm_length(0, 0)
            1
            sage: p.arm_length(0, 1)
            0
            sage: p.arm_length(2, 0)
            0
            sage: Partition([3,3]).arm_length(0, 0)
            2
            sage: Partition([3,3]).arm_length(*[0,0])
            2
        """
    def arm_lengths(self, flat: bool = False):
        """
        Return a tableau of shape ``self`` where each cell is filled with
        its arm length.

        The optional boolean parameter ``flat`` provides the option of
        returning a flat list.

        EXAMPLES::

            sage: Partition([2,2,1]).arm_lengths()
            [[1, 0], [1, 0], [0]]
            sage: Partition([2,2,1]).arm_lengths(flat=True)
            [1, 0, 1, 0, 0]
            sage: Partition([3,3]).arm_lengths()
            [[2, 1, 0], [2, 1, 0]]
            sage: Partition([3,3]).arm_lengths(flat=True)
            [2, 1, 0, 2, 1, 0]
        """
    def arm_cells(self, i, j):
        """
        Return the list of the cells of the arm of cell `(i,j)` in ``self``.

        The arm of cell `c = (i,j)` is the boxes that appear to the right of
        `c`.

        The cell coordinates are zero-based, i. e., the northwesternmost
        cell is `(0,0)`.

        INPUT:

        - ``i``, ``j`` -- two integers

        OUTPUT: list of pairs of integers

        EXAMPLES::

            sage: Partition([4,4,3,1]).arm_cells(1,1)
            [(1, 2), (1, 3)]

            sage: Partition([]).arm_cells(0,0)
            Traceback (most recent call last):
            ...
            ValueError: the cell is not in the diagram
        """
    def leg_length(self, i, j):
        """
        Return the length of the leg of cell `(i,j)` in ``self``.

        The leg of cell `c = (i,j)` is defined to be the cells below `c`
        (in English convention).

        The cell coordinates are zero-based, i. e., the northwesternmost
        cell is `(0,0)`.

        INPUT:

        - ``i``, ``j`` -- two integers

        OUTPUT: integer or a :exc:`ValueError`

        EXAMPLES::

            sage: p = Partition([2,2,1])
            sage: p.leg_length(0, 0)
            2
            sage: p.leg_length(0,1)
            1
            sage: p.leg_length(2,0)
            0
            sage: Partition([3,3]).leg_length(0, 0)
            1
            sage: cell = [0,0]; Partition([3,3]).leg_length(*cell)
            1
        """
    def leg_lengths(self, flat: bool = False):
        """
        Return a tableau of shape ``self`` with each cell filled in with
        its leg length.  The optional boolean parameter ``flat`` provides
        the option of returning a flat list.

        EXAMPLES::

            sage: Partition([2,2,1]).leg_lengths()
            [[2, 1], [1, 0], [0]]
            sage: Partition([2,2,1]).leg_lengths(flat=True)
            [2, 1, 1, 0, 0]
            sage: Partition([3,3]).leg_lengths()
            [[1, 1, 1], [0, 0, 0]]
            sage: Partition([3,3]).leg_lengths(flat=True)
            [1, 1, 1, 0, 0, 0]
        """
    def leg_cells(self, i, j):
        """
        Return the list of the cells of the leg of cell `(i,j)` in ``self``.

        The leg of cell `c = (i,j)` is defined to be the cells below `c` (in
        English convention).

        The cell coordinates are zero-based, i. e., the northwesternmost
        cell is `(0,0)`.

        INPUT:

        - ``i``, ``j`` -- two integers

        OUTPUT: list of pairs of integers

        EXAMPLES::

            sage: Partition([4,4,3,1]).leg_cells(1,1)
            [(2, 1)]
            sage: Partition([4,4,3,1]).leg_cells(0,1)
            [(1, 1), (2, 1)]

            sage: Partition([]).leg_cells(0,0)
            Traceback (most recent call last):
            ...
            ValueError: the cell is not in the diagram
        """
    def attacking_pairs(self):
        """
        Return a list of the attacking pairs of the Young diagram of
        ``self``.

        A pair of cells `(c, d)` of a Young diagram (in English notation) is
        said to be attacking if one of the following conditions holds:

        1. `c` and `d` lie in the same row with `c` strictly to the west
           of `d`.

        2. `c` is in the row immediately to the south of `d`, and `c`
           lies strictly east of `d`.

        This particular method returns each pair `(c, d)` as a tuple,
        where each of `c` and `d` is given as a tuple `(i, j)` with
        `i` and `j` zero-based (so `i = 0` means that the cell lies
        in the topmost row).

        EXAMPLES::

            sage: p = Partition([3, 2])
            sage: p.attacking_pairs()
            [((0, 0), (0, 1)),
             ((0, 0), (0, 2)),
             ((0, 1), (0, 2)),
             ((1, 0), (1, 1)),
             ((1, 1), (0, 0))]
            sage: Partition([]).attacking_pairs()
            []
        """
    def dominated_partitions(self, rows=None):
        """
        Return a list of the partitions dominated by `n`. If ``rows`` is
        specified, then it only returns the ones whose number of rows
        is at most ``rows``.

        EXAMPLES::

            sage: Partition([3,2,1]).dominated_partitions()
            [[3, 2, 1], [3, 1, 1, 1], [2, 2, 2], [2, 2, 1, 1], [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
            sage: Partition([3,2,1]).dominated_partitions(rows=3)
            [[3, 2, 1], [2, 2, 2]]
        """
    def contains(self, x):
        """
        Return ``True`` if ``x`` is a partition whose Ferrers diagram is
        contained in the Ferrers diagram of ``self``.

        EXAMPLES::

            sage: p = Partition([3,2,1])
            sage: p.contains([2,1])
            True
            sage: all(p.contains(mu) for mu in Partitions(3))
            True
            sage: all(p.contains(mu) for mu in Partitions(4))
            False
        """
    def hook_product(self, a):
        """
        Return the Jack hook-product.

        EXAMPLES::

            sage: Partition([3,2,1]).hook_product(x)                                    # needs sage.symbolic
            (2*x + 3)*(x + 2)^2
            sage: Partition([2,2]).hook_product(x)                                      # needs sage.symbolic
            2*(x + 2)*(x + 1)
        """
    def hook_polynomial(self, q, t):
        """
        Return the two-variable hook polynomial.

        EXAMPLES::

            sage: R.<q,t> = PolynomialRing(QQ)
            sage: a = Partition([2,2]).hook_polynomial(q,t)
            sage: a == (1 - t)*(1 - q*t)*(1 - t^2)*(1 - q*t^2)
            True
            sage: a = Partition([3,2,1]).hook_polynomial(q,t)
            sage: a == (1 - t)^3*(1 - q*t^2)^2*(1 - q^2*t^3)
            True
        """
    def hook_length(self, i, j):
        """
        Return the length of the hook of cell `(i,j)` in ``self``.

        The (length of the) hook of cell `(i,j)` of a partition `\\lambda`
        is

        .. MATH::

            \\lambda_i + \\lambda^{\\prime}_j - i - j + 1

        where `\\lambda^{\\prime}` is the conjugate partition. In English
        convention, the hook length is the number of cells horizontally
        to the right and vertically below the cell `(i,j)` (including
        that cell).

        EXAMPLES::

            sage: p = Partition([2,2,1])
            sage: p.hook_length(0, 0)
            4
            sage: p.hook_length(0, 1)
            2
            sage: p.hook_length(2, 0)
            1
            sage: Partition([3,3]).hook_length(0, 0)
            4
            sage: cell = [0,0]; Partition([3,3]).hook_length(*cell)
            4
        """
    def hooks(self):
        """
        Return a sorted list of the hook lengths in ``self``.

        EXAMPLES::

            sage: Partition([3,2,1]).hooks()
            [5, 3, 3, 1, 1, 1]
        """
    def hook_lengths(self):
        """
        Return a tableau of shape ``self`` with the cells filled in with the
        hook lengths.

        In each cell, put the sum of one plus the number of cells
        horizontally to the right and vertically below the cell (the
        hook length).

        For example, consider the partition ``[3,2,1]`` of 6 with Ferrers
        diagram::

            # # #
            # #
            #

        When we fill in the cells with the hook lengths, we obtain::

            5 3 1
            3 1
            1

        EXAMPLES::

            sage: Partition([2,2,1]).hook_lengths()
            [[4, 2], [3, 1], [1]]
            sage: Partition([3,3]).hook_lengths()
            [[4, 3, 2], [3, 2, 1]]
            sage: Partition([3,2,1]).hook_lengths()
            [[5, 3, 1], [3, 1], [1]]
            sage: Partition([2,2]).hook_lengths()
            [[3, 2], [2, 1]]
            sage: Partition([5]).hook_lengths()
            [[5, 4, 3, 2, 1]]

        REFERENCES:

        - http://mathworld.wolfram.com/HookLengthFormula.html
        """
    def upper_hook(self, i, j, alpha):
        """
        Return the upper hook length of the cell `(i,j)` in ``self``.
        When ``alpha = 1``, this is just the normal hook length.

        The upper hook length of a cell `(i,j)` in a partition
        `\\kappa` is defined by

        .. MATH::

            h^*_\\kappa(i,j) = \\kappa^\\prime_j - i + \\alpha(\\kappa_i - j + 1).

        EXAMPLES::

            sage: p = Partition([2,1])
            sage: p.upper_hook(0,0,1)
            3
            sage: p.hook_length(0,0)
            3
            sage: [ p.upper_hook(i,j,x) for i,j in p.cells() ]                          # needs sage.symbolic
            [2*x + 1, x, x]
        """
    def upper_hook_lengths(self, alpha):
        """
        Return a tableau of shape ``self`` with the cells filled in with the
        upper hook lengths. When ``alpha = 1``, these are just the normal hook
        lengths.

        The upper hook length of a cell `(i,j)` in a partition
        `\\kappa` is defined by

        .. MATH::

            h^*_\\kappa(i,j) = \\kappa^\\prime_j - i + \\alpha(\\kappa_i - j + 1).

        EXAMPLES::

            sage: Partition([3,2,1]).upper_hook_lengths(x)                              # needs sage.symbolic
            [[3*x + 2, 2*x + 1, x], [2*x + 1, x], [x]]
            sage: Partition([3,2,1]).upper_hook_lengths(1)
            [[5, 3, 1], [3, 1], [1]]
            sage: Partition([3,2,1]).hook_lengths()
            [[5, 3, 1], [3, 1], [1]]
        """
    def lower_hook(self, i, j, alpha):
        """
        Return the lower hook length of the cell `(i,j)` in ``self``.
        When ``alpha = 1``, this is just the normal hook length.

        The lower hook length of a cell `(i,j)` in a partition
        `\\kappa` is defined by

        .. MATH::

            h_*^\\kappa(i,j) = \\kappa^\\prime_j - i + 1 + \\alpha(\\kappa_i - j).

        EXAMPLES::

            sage: p = Partition([2,1])
            sage: p.lower_hook(0,0,1)
            3
            sage: p.hook_length(0,0)
            3
            sage: [ p.lower_hook(i,j,x) for i,j in p.cells() ]                          # needs sage.symbolic
            [x + 2, 1, 1]
        """
    def lower_hook_lengths(self, alpha):
        """
        Return a tableau of shape ``self`` with the cells filled in with the
        lower hook lengths. When ``alpha = 1``, these are just the normal hook
        lengths.

        The lower hook length of a cell `(i,j)` in a partition
        `\\kappa` is defined by

        .. MATH::

            h_*^\\kappa(i,j) = \\kappa^\\prime_j - i + 1 + \\alpha(\\kappa_i - j).

        EXAMPLES::

            sage: Partition([3,2,1]).lower_hook_lengths(x)                              # needs sage.symbolic
            [[2*x + 3, x + 2, 1], [x + 2, 1], [1]]
            sage: Partition([3,2,1]).lower_hook_lengths(1)
            [[5, 3, 1], [3, 1], [1]]
            sage: Partition([3,2,1]).hook_lengths()
            [[5, 3, 1], [3, 1], [1]]
        """
    def weighted_size(self):
        """
        Return the weighted size of ``self``.

        The weighted size of a partition `\\lambda` is

        .. MATH::

            \\sum_i i \\cdot \\lambda_i,

        where `\\lambda = (\\lambda_0, \\lambda_1, \\lambda_2, \\cdots )`.

        This also the sum of the leg length of every cell in `\\lambda`, or

        .. MATH::

            \\sum_i \\binom{\\lambda^{\\prime}_i}{2}

        where `\\lambda^{\\prime}` is the conjugate partition of `\\lambda`.

        EXAMPLES::

            sage: Partition([2,2]).weighted_size()
            2
            sage: Partition([3,3,3]).weighted_size()
            9
            sage: Partition([5,2]).weighted_size()
            2
            sage: Partition([]).weighted_size()
            0
        """
    def is_empty(self):
        """
        Return ``True`` if ``self`` is the empty partition.

        EXAMPLES::

            sage: Partition([]).is_empty()
            True
            sage: Partition([2,1,1]).is_empty()
            False
        """
    def length(self):
        """
        Return the number of parts in ``self``.

        EXAMPLES::

            sage: Partition([3,2]).length()
            2
            sage: Partition([2,2,1]).length()
            3
            sage: Partition([]).length()
            0
        """
    def to_exp(self, k: int = 0):
        """
        Return a list of the multiplicities of the parts of a partition.
        Use the optional parameter ``k`` to get a return list of length at
        least ``k``.

        EXAMPLES::

            sage: Partition([3,2,2,1]).to_exp()
            [1, 2, 1]
            sage: Partition([3,2,2,1]).to_exp(5)
            [1, 2, 1, 0, 0]

        TESTS::

            sage: [parent(x) for x in Partition([3,2,2,1]).to_exp(5)]
            [Integer Ring, Integer Ring, Integer Ring, Integer Ring, Integer Ring]
        """
    def evaluation(self):
        """
        Return the evaluation of ``self``.

        The **commutative evaluation**, often shortened to **evaluation**, of
        a word (we think of a partition as a word in `\\{1, 2, 3, \\ldots\\}`)
        is its image in the free commutative monoid. In other words,
        this counts how many occurrences there are of each letter.

        This is also is known as **Parikh vector** and **abelianization** and
        has the same output as :meth:`to_exp()`.

        EXAMPLES::

            sage: Partition([4,3,1,1]).evaluation()
            [2, 0, 1, 1]
        """
    def to_exp_dict(self):
        """
        Return a dictionary containing the multiplicities of the parts of
        ``self``.

        EXAMPLES::

            sage: p = Partition([4,2,2,1])
            sage: d = p.to_exp_dict()
            sage: d[4]
            1
            sage: d[2]
            2
            sage: d[1]
            1
            sage: 5 in d
            False
        """
    def centralizer_size(self, t: int = 0, q: int = 0):
        """
        Return the size of the centralizer of any permutation of cycle type
        ``self``.

        If `m_i` is the multiplicity of `i` as a part of `p`, this is given by

        .. MATH::

           \\prod_i m_i! i^{m_i}.

        Including the optional parameters `t` and `q` gives the `q,t` analog,
        which is the former product times

        .. MATH::

           \\prod_{i=1}^{\\mathrm{length}(p)} \\frac{1 - q^{p_i}}{1 - t^{p_i}}.

        See Section 1.3, p. 24, in [Ke1991]_.

        EXAMPLES::

            sage: Partition([2,2,1]).centralizer_size()
            8
            sage: Partition([2,2,2]).centralizer_size()
            48
            sage: Partition([2,2,1]).centralizer_size(q=2, t=3)
            9/16
            sage: Partition([]).centralizer_size()
            1
            sage: Partition([]).centralizer_size(q=2, t=4)
            1

        TESTS::

            sage: Partition([2,2,2]).aut()
            48
        """
    aut = centralizer_size
    def content(self, r, c, multicharge=(0,)):
        """
        Return the content of the cell at row `r` and column `c`.

        The content of a cell is `c - r`.

        For consistency with partition tuples there is also an optional
        ``multicharge`` argument which is an offset to the usual content. By
        setting the ``multicharge`` equal to the 0-element of the ring
        `\\ZZ/e\\ZZ`, the corresponding `e`-residue will be returned. This is
        the content modulo `e`.

        The content (and residue) do not strictly depend on the partition,
        however, this method is included because it is often useful in the
        context of partitions.

        EXAMPLES::

            sage: Partition([2,1]).content(1,0)
            -1
            sage: p = Partition([3,2])
            sage: sum([p.content(*c) for c in p.cells()])
            2

        and now we return the 3-residue of a cell::

            sage: Partition([2,1]).content(1,0, multicharge=[IntegerModRing(3)(0)])
            2
        """
    def residue(self, r, c, l):
        """
        Return the ``l``-residue of the cell at row ``r`` and column ``c``.

        The `\\ell`-residue of a cell is `c - r` modulo `\\ell`.

        This does not strictly depend upon the partition, however, this method
        is included because it is often useful in the context of partitions.

        EXAMPLES::

            sage: Partition([2,1]).residue(1, 0, 3)
            2
        """
    @cached_method
    def block(self, e, multicharge=(0,)):
        """
        Return a dictionary `\\beta` that determines the block associated to
        the partition ``self`` and the
        :meth:`~sage.combinat.tableau_residues.ResidueSequence.quantum_characteristic` ``e``.

        INPUT:

        - ``e`` -- the quantum characteristic

        - ``multicharge`` -- the multicharge (default: `(0,)`)

        OUTPUT:

        - A dictionary giving the multiplicities of the residues in the
          partition tuple ``self``

        In more detail, the value ``beta[i]`` is equal to the
        number of nodes of residue ``i``. This corresponds to
        the positive root

        .. MATH::

            \\sum_{i\\in I} \\beta_i \\alpha_i \\in Q^+,

        a element of the positive root lattice of the corresponding
        Kac-Moody algebra. See [DJM1998]_ and [BK2009]_ for more details.

        This is a useful statistics because two Specht modules for a
        Hecke algebra of type `A` belong to the same block if and only if they
        correspond to same element `\\beta` of the root lattice, given above.

        We return a dictionary because when the quantum characteristic is `0`,
        the Cartan type is `A_{\\infty}`, in which case the simple roots are
        indexed by the integers.

        EXAMPLES::

            sage: Partition([4,3,2]).block(0)
            {-2: 1, -1: 2, 0: 2, 1: 2, 2: 1, 3: 1}
            sage: Partition([4,3,2]).block(2)
            {0: 4, 1: 5}
            sage: Partition([4,3,2]).block(2, multicharge=(1,))
            {0: 5, 1: 4}
            sage: Partition([4,3,2]).block(3)
            {0: 3, 1: 3, 2: 3}
            sage: Partition([4,3,2]).block(4)
            {0: 2, 1: 2, 2: 2, 3: 3}
        """
    def defect(self, e, multicharge=(0,)):
        """
        Return the ``e``-defect or the ``e``-weight of ``self``.

        The `e`-defect is the number of (connected) `e`-rim hooks that
        can be removed from the partition.

        The defect of a partition is given by

        .. MATH::

            \\text{defect}(\\beta) = (\\Lambda, \\beta) - \\tfrac12(\\beta, \\beta),

        where `\\Lambda = \\sum_r \\Lambda_{\\kappa_r}` for the multicharge
        `(\\kappa_1, \\ldots, \\kappa_{\\ell})` and
        `\\beta = \\sum_{(r,c)} \\alpha_{(c-r) \\pmod e}`, with the sum
        being over the cells in the partition.

        INPUT:

        - ``e`` -- the quantum characteristic

        - ``multicharge`` -- the multicharge (default: `(0,)`)

        OUTPUT: nonnegative integer, which is the defect of the block
        containing the partition ``self``

        EXAMPLES::

            sage: Partition([4,3,2]).defect(2)
            3
            sage: Partition([0]).defect(2)
            0
            sage: Partition([3]).defect(2)
            1
            sage: Partition([6]).defect(2)
            3
            sage: Partition([9]).defect(2)
            4
            sage: Partition([12]).defect(2)
            6
            sage: Partition([4,3,2]).defect(3)
            3
            sage: Partition([0]).defect(3)
            0
            sage: Partition([3]).defect(3)
            1
            sage: Partition([6]).defect(3)
            2
            sage: Partition([9]).defect(3)
            3
            sage: Partition([12]).defect(3)
            4

        TESTS::

            sage: all(mu.core(e).size() + e * mu.defect(e) == 9
            ....:     for mu in Partitions(9) for e in [2,3,4])
            True
        """
    def contents_tableau(self, multicharge=(0,)):
        """
        Return the tableau which has ``(k,r,c)``-th cell equal to the
        content ``multicharge[k] - r + c`` of the cell.

        EXAMPLES::

            sage: Partition([2,1]).contents_tableau()
            [[0, 1], [-1]]
            sage: Partition([3,2,1,1]).contents_tableau().pp()
                0  1  2
                -1  0
                -2
                -3
            sage: Partition([3,2,1,1]).contents_tableau([ IntegerModRing(3)(0)] ).pp()
                0  1  2
                2  0
                1
                0
        """
    def is_restricted(self, e, multicharge=(0,)):
        """
        Return ``True`` is this is an ``e``-restricted partition.

        An `e`-restricted partition is a partition such that the
        difference of consecutive parts is always strictly less
        than `e`, where partitions are considered to have an infinite
        number of `0` parts. I.e., the last part must be strictly
        less than `e`.

        EXAMPLES::

          sage: Partition([4,3,3,2]).is_restricted(2)
          False
          sage: Partition([4,3,3,2]).is_restricted(3)
          True
          sage: Partition([4,3,3,2]).is_restricted(4)
          True
          sage: Partition([4]).is_restricted(4)
          False
        """
    def is_regular(self, e, multicharge=(0,)) -> bool:
        """
        Return ``True`` is this is an ``e``-regular partition.

        A partition is `e`-regular if it does not have `e` equal
        nonzero parts.

        EXAMPLES::

          sage: Partition([4,3,3,3]).is_regular(2)
          False
          sage: Partition([4,3,3,3]).is_regular(3)
          False
          sage: Partition([4,3,3,3]).is_regular(4)
          True
        """
    def conjugacy_class_size(self):
        """
        Return the size of the conjugacy class of the symmetric group
        indexed by ``self``.

        EXAMPLES::

            sage: Partition([2,2,2]).conjugacy_class_size()
            15
            sage: Partition([2,2,1]).conjugacy_class_size()
            15
            sage: Partition([2,1,1]).conjugacy_class_size()
            6
        """
    def corners(self) -> list:
        '''
        Return a list of the corners of the partition ``self``.

        A corner of a partition `\\lambda` is a cell of the Young diagram
        of `\\lambda` which can be removed from the Young diagram while
        still leaving a straight shape behind.

        The entries of the list returned are pairs of the form `(i,j)`,
        where `i` and `j` are the coordinates of the respective corner.
        The coordinates are counted from `0`.

        .. NOTE::

            This is referred to as an "inner corner" in [Sag2001]_.

        EXAMPLES::

            sage: Partition([3,2,1]).corners()
            [(0, 2), (1, 1), (2, 0)]
            sage: Partition([3,3,1]).corners()
            [(1, 2), (2, 0)]
            sage: Partition([]).corners()
            []
        '''
    inside_corners = corners
    removable_cells = corners
    def corners_residue(self, i, l):
        """
        Return a list of the corners of the partition ``self`` having
        ``l``-residue ``i``.

        A corner of a partition `\\lambda` is a cell of the Young diagram
        of `\\lambda` which can be removed from the Young diagram while
        still leaving a straight shape behind. See :meth:`residue` for
        the definition of the ``l``-residue.

        The entries of the list returned are pairs of the form `(i,j)`,
        where `i` and `j` are the coordinates of the respective corner.
        The coordinates are counted from `0`.

        EXAMPLES::

            sage: Partition([3,2,1]).corners_residue(0, 3)
            [(1, 1)]
            sage: Partition([3,2,1]).corners_residue(1, 3)
            [(2, 0)]
            sage: Partition([3,2,1]).corners_residue(2, 3)
            [(0, 2)]
        """
    inside_corners_residue = corners_residue
    removable_cells_residue = corners_residue
    def outside_corners(self):
        '''
        Return a list of the outside corners of the partition ``self``.

        An outside corner (also called a cocorner) of a partition
        `\\lambda` is a cell on `\\ZZ^2` which does not belong to
        the Young diagram of `\\lambda` but can be added to this Young
        diagram to still form a straight-shape Young diagram.

        The entries of the list returned are pairs of the form `(i,j)`,
        where `i` and `j` are the coordinates of the respective corner.
        The coordinates are counted from `0`.

        .. NOTE::

            These are called "outer corners" in [Sag2001]_.

        EXAMPLES::

            sage: Partition([2,2,1]).outside_corners()
            [(0, 2), (2, 1), (3, 0)]
            sage: Partition([2,2]).outside_corners()
            [(0, 2), (2, 0)]
            sage: Partition([6,3,3,1,1,1]).outside_corners()
            [(0, 6), (1, 3), (3, 1), (6, 0)]
            sage: Partition([]).outside_corners()
            [(0, 0)]
        '''
    addable_cells = outside_corners
    def outside_corners_residue(self, i, l):
        """
        Return a list of the outside corners of the partition ``self``
        having ``l``-residue ``i``.

        An outside corner (also called a cocorner) of a partition
        `\\lambda` is a cell on `\\ZZ^2` which does not belong to
        the Young diagram of `\\lambda` but can be added to this Young
        diagram to still form a straight-shape Young diagram. See
        :meth:`residue` for the definition of the ``l``-residue.

        The entries of the list returned are pairs of the form `(i,j)`,
        where `i` and `j` are the coordinates of the respective corner.
        The coordinates are counted from `0`.

        EXAMPLES::

            sage: Partition([3,2,1]).outside_corners_residue(0, 3)
            [(0, 3), (3, 0)]
            sage: Partition([3,2,1]).outside_corners_residue(1, 3)
            [(1, 2)]
            sage: Partition([3,2,1]).outside_corners_residue(2, 3)
            [(2, 1)]
        """
    addable_cells_residue = outside_corners_residue
    def rim(self):
        """
        Return the rim of ``self``.

        The rim of a partition `\\lambda` is defined as the cells which belong
        to `\\lambda` and which are adjacent to cells not in `\\lambda`.

        EXAMPLES:

        The rim of the partition `[5,5,2,1]` consists of the cells marked with
        ``#`` below::

            ****#
            *####
            ##
            #

            sage: Partition([5,5,2,1]).rim()
            [(3, 0), (2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4)]

            sage: Partition([2,2,1]).rim()
            [(2, 0), (1, 0), (1, 1), (0, 1)]
            sage: Partition([2,2]).rim()
            [(1, 0), (1, 1), (0, 1)]
            sage: Partition([6,3,3,1,1]).rim()
            [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5)]
            sage: Partition([]).rim()
            []
        """
    def outer_rim(self):
        """
        Return the outer rim of ``self``.

        The outer rim of a partition `\\lambda` is defined as the cells which do
        not belong to `\\lambda` and which are adjacent to cells in `\\lambda`.

        EXAMPLES:

        The outer rim of the partition `[4,1]` consists of the cells marked
        with ``#`` below::

            ****#
            *####
            ##

        ::

            sage: Partition([4,1]).outer_rim()
            [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4)]

            sage: Partition([2,2,1]).outer_rim()
            [(3, 0), (3, 1), (2, 1), (2, 2), (1, 2), (0, 2)]
            sage: Partition([2,2]).outer_rim()
            [(2, 0), (2, 1), (2, 2), (1, 2), (0, 2)]
            sage: Partition([6,3,3,1,1]).outer_rim()
            [(5, 0), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (0, 6)]
            sage: Partition([]).outer_rim()
            [(0, 0)]
        """
    def zero_one_sequence(self):
        """
        Compute the finite `0-1` sequence of the partition.

        The full `0-1` sequence is the sequence (infinite in both
        directions) indicating the steps taken when following the
        outer rim of the diagram of the partition. We use the convention
        that in English convention, a 1 corresponds to an East step, and
        a 0 corresponds to a North step.

        Note that every full `0-1` sequence starts with infinitely many 0s and
        ends with infinitely many 1s.

        One place where these arise is in the affine symmetric group where
        one takes an affine permutation `w` and every `i` such that
        `w(i) \\leq 0` corresponds to a 1 and `w(i) > 0` corresponds to a 0.
        See pages 24-25 of [LLMSSZ2013]_ for connections to affine Grassmannian
        elements (note there they use the French convention for their
        partitions).

        These are also known as **path sequences**, **Maya diagrams**,
        **plus-minus diagrams**, **Comet code** [Sta-EC2]_, among others.

        OUTPUT:

        The finite `0-1` sequence is obtained from the full `0-1`
        sequence by omitting all heading 0s and trailing 1s. The
        output sequence is finite, starts with a 1 and ends with a
        0 (unless it is empty, for the empty partition). Its length
        is the sum of the first part of the partition with the
        length of the partition.

        EXAMPLES::

            sage: Partition([5,4]).zero_one_sequence()
            [1, 1, 1, 1, 0, 1, 0]
            sage: Partition([]).zero_one_sequence()
            []
            sage: Partition([2]).zero_one_sequence()
            [1, 1, 0]

        TESTS::

            sage: all(Partitions().from_zero_one(mu.zero_one_sequence()) == mu for n in range(10) for mu in Partitions(n))
            True
        """
    def core(self, length):
        """
        Return the ``length``-core of the partition -- in the literature
        the core is commonly referred to as the `k`-core, `p`-core,
        `r`-core, ... .

        The `r`-core of a partition `\\lambda` can be obtained by
        repeatedly removing rim hooks of size `r` from (the Young diagram
        of) `\\lambda` until this is no longer possible. The remaining
        partition is the core.

        EXAMPLES::

            sage: Partition([6,3,2,2]).core(3)
            [2, 1, 1]
            sage: Partition([]).core(3)
            []
            sage: Partition([8,7,7,4,1,1,1,1,1]).core(3)
            [2, 1, 1]

        TESTS::

            sage: Partition([3,3,3,2,1]).core(3)
            []
            sage: Partition([10,8,7,7]).core(4)
            []
            sage: Partition([21,15,15,9,6,6,6,3,3]).core(3)
            []
        """
    def quotient(self, length):
        """
        Return the quotient of the partition  -- in the literature the
        quotient is commonly referred to as the `k`-quotient, `p`-quotient,
        `r`-quotient, ... .

        The `r`-quotient of a partition `\\lambda` is a list of `r`
        partitions (labelled from `0` to `r-1`), constructed in the following
        way. Label each cell in the Young diagram of `\\lambda` with its
        content modulo `r`. Let `R_i` be the set of rows ending in a cell
        labelled `i`, and `C_i` be the set of columns ending in a cell
        labelled `i`. Then the `j`-th component of the quotient of
        `\\lambda` is the partition defined by intersecting `R_j` with
        `C_{j+1}`. (See Theorem 2.7.37 in [JK1981]_.)

        EXAMPLES::

            sage: Partition([7,7,5,3,3,3,1]).quotient(3)
            ([2], [1], [2, 2, 2])

        TESTS::

            sage: Partition([8,7,7,4,1,1,1,1,1]).quotient(3)
            ([2, 1], [2, 2], [2])
            sage: Partition([10,8,7,7]).quotient(4)
            ([2], [3], [2], [1])
            sage: Partition([6,3,3]).quotient(3)
            ([1], [1], [2])
            sage: Partition([3,3,3,2,1]).quotient(3)
            ([1], [1, 1], [1])
            sage: Partition([6,6,6,3,3,3]).quotient(3)
            ([2, 1], [2, 1], [2, 1])
            sage: Partition([21,15,15,9,6,6,6,3,3]).quotient(3)
            ([5, 2, 1], [5, 2, 1], [7, 3, 2])
            sage: Partition([21,15,15,9,6,6,3,3]).quotient(3)
            ([5, 2], [5, 2, 1], [7, 3, 1])
            sage: Partition([14,12,11,10,10,10,10,9,6,4,3,3,2,1]).quotient(5)
            ([3, 3], [2, 2, 1], [], [3, 3, 3], [1])

            sage: all(p == Partition(core=p.core(k), quotient=p.quotient(k))
            ....:     for i in range(10) for p in Partitions(i)
            ....:     for k in range(1,6))
            True
        """
    def is_core(self, k):
        """
        Return ``True`` if the Partition ``self`` is a ``k``-core.

        A partition is said to be a *`k`-core* if it has no hooks of length
        `k`. Equivalently, a partition is said to be a `k`-core if it is its
        own `k`-core (where the latter is defined as in :meth:`core`).

        Visually, this can be checked by trying to remove border strips of size
        `k` from ``self``.  If this is not possible, then ``self`` is a
        `k`-core.

        EXAMPLES:

        In the partition (2, 1), a hook length of 2 does not occur, but a hook
        length of 3 does::

            sage: p = Partition([2, 1])
            sage: p.is_core(2)
            True
            sage: p.is_core(3)
            False

            sage: q = Partition([12, 8, 5, 5, 2, 2, 1])
            sage: q.is_core(4)
            False
            sage: q.is_core(5)
            True
            sage: q.is_core(0)
            True

        .. SEEALSO::

            :meth:`core`, :class:`Core`
        """
    def k_interior(self, k):
        """
        Return the partition consisting of the cells of ``self`` whose hook
        lengths are greater than ``k``.

        EXAMPLES::

            sage: p = Partition([3,2,1])
            sage: p.hook_lengths()
            [[5, 3, 1], [3, 1], [1]]
            sage: p.k_interior(2)
            [2, 1]
            sage: p.k_interior(3)
            [1]

            sage: p = Partition([])
            sage: p.k_interior(3)
            []
        """
    def k_boundary(self, k):
        """
        Return the skew partition formed by removing the cells of the
        ``k``-interior, see :meth:`k_interior`.

        EXAMPLES::

            sage: p = Partition([3,2,1])
            sage: p.k_boundary(2)
            [3, 2, 1] / [2, 1]
            sage: p.k_boundary(3)
            [3, 2, 1] / [1]

            sage: p = Partition([12,8,5,5,2,2,1])
            sage: p.k_boundary(4)
            [12, 8, 5, 5, 2, 2, 1] / [8, 5, 2, 2]
        """
    def add_cell(self, i, j=None):
        """
        Return a partition corresponding to ``self`` with a cell added in
        row ``i``. (This does not change ``self``.)

        EXAMPLES::

            sage: Partition([3, 2, 1, 1]).add_cell(0)
            [4, 2, 1, 1]
            sage: cell = [4, 0]; Partition([3, 2, 1, 1]).add_cell(*cell)
            [3, 2, 1, 1, 1]
        """
    def remove_cell(self, i, j=None):
        """
        Return the partition obtained by removing a cell at the end of row
        ``i`` of ``self``.

        EXAMPLES::

            sage: Partition([2,2]).remove_cell(1)
            [2, 1]
            sage: Partition([2,2,1]).remove_cell(2)
            [2, 2]
            sage: #Partition([2,2]).remove_cell(0)

        ::

            sage: Partition([2,2]).remove_cell(1,1)
            [2, 1]
            sage: #Partition([2,2]).remove_cell(1,0)
        """
    def k_irreducible(self, k):
        """
        Return the partition with all `r \\times (k+1-r)` rectangles removed.

        If ``self`` is a `k`-bounded partition, then this method will return the partition
        where all rectangles of dimension `r \\times (k+1-r)` for `1 \\leq r \\leq k`
        have been deleted.

        If ``self`` is not a `k`-bounded partition then the method will raise an error.

        INPUT:

        - ``k`` -- nonnegative integer

        OUTPUT: a partition

        EXAMPLES::

            sage: Partition([3,2,2,1,1,1]).k_irreducible(4)
            [3, 2, 2, 1, 1, 1]
            sage: Partition([3,2,2,1,1,1]).k_irreducible(3)
            []
            sage: Partition([3,3,3,2,2,2,2,2,1,1,1,1]).k_irreducible(3)
            [2, 1]
        """
    def k_skew(self, k):
        """
        Return the `k`-skew partition.

        The `k`-skew diagram of a `k`-bounded partition is the skew diagram
        denoted `\\lambda/^k` satisfying the conditions:

        1. row `i` of `\\lambda/^k` has length `\\lambda_i`,

        2. no cell in `\\lambda/^k` has hook-length exceeding `k`,

        3. every square above the diagram of `\\lambda/^k` has hook
           length exceeding `k`.

        REFERENCES:

        - [LM2004]_

        EXAMPLES::

            sage: p = Partition([4,3,2,2,1,1])
            sage: p.k_skew(4)
            [9, 5, 3, 2, 1, 1] / [5, 2, 1]
        """
    def to_core(self, k):
        """
        Map the `k`-bounded partition ``self`` to its corresponding `k+1`-core.

        See also :meth:`k_skew`.

        EXAMPLES::

            sage: p = Partition([4,3,2,2,1,1])
            sage: c = p.to_core(4); c
            [9, 5, 3, 2, 1, 1]
            sage: type(c)
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>
            sage: c.to_bounded_partition() == p
            True
        """
    def from_kbounded_to_reduced_word(self, k):
        """
        Map a `k`-bounded partition to a reduced word for an element in
        the affine permutation group.

        This uses the fact that there is a bijection between `k`-bounded
        partitions and `(k+1)`-cores and an action of the affine nilCoxeter
        algebra of type `A_k^{(1)}` on `(k+1)`-cores as described in [LM2006b]_.

        EXAMPLES::

            sage: p = Partition([2,1,1])
            sage: p.from_kbounded_to_reduced_word(2)
            [2, 1, 2, 0]
            sage: p = Partition([3,1])
            sage: p.from_kbounded_to_reduced_word(3)
            [3, 2, 1, 0]
            sage: p.from_kbounded_to_reduced_word(2)
            Traceback (most recent call last):
            ...
            ValueError: the partition must be 2-bounded
            sage: p = Partition([])
            sage: p.from_kbounded_to_reduced_word(2)
            []
        """
    def from_kbounded_to_grassmannian(self, k):
        """
        Map a `k`-bounded partition to a Grassmannian element in
        the affine Weyl group of type `A_k^{(1)}`.

        For details, see the documentation of the method
        :meth:`from_kbounded_to_reduced_word` .

        EXAMPLES::

            sage: p = Partition([2,1,1])
            sage: p.from_kbounded_to_grassmannian(2)                                    # needs sage.modules
            [-1  1  1]
            [-2  2  1]
            [-2  1  2]
            sage: p = Partition([])
            sage: p.from_kbounded_to_grassmannian(2)                                    # needs sage.modules
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def to_list(self):
        """
        Return ``self`` as a list.

        EXAMPLES::

            sage: p = Partition([2,1]).to_list(); p
            [2, 1]
            sage: type(p)
            <class 'list'>

        TESTS::

            sage: p = Partition([2,1])
            sage: pl = p.to_list()
            sage: pl[0] = 0; p
            [2, 1]
        """
    def add_vertical_border_strip(self, k):
        """
        Return a list of all the partitions that can be obtained by adding
        a vertical border strip of length ``k`` to ``self``.

        EXAMPLES::

            sage: Partition([]).add_vertical_border_strip(0)
            [[]]
            sage: Partition([3,2,1]).add_vertical_border_strip(0)
            [[3, 2, 1]]
            sage: Partition([]).add_vertical_border_strip(2)
            [[1, 1]]
            sage: Partition([2,2]).add_vertical_border_strip(2)
            [[3, 3], [3, 2, 1], [2, 2, 1, 1]]
            sage: Partition([3,2,2]).add_vertical_border_strip(2)
            [[4, 3, 2], [4, 2, 2, 1], [3, 3, 3], [3, 3, 2, 1], [3, 2, 2, 1, 1]]
        """
    def add_horizontal_border_strip(self, k):
        """
        Return a list of all the partitions that can be obtained by adding
        a horizontal border strip of length ``k`` to ``self``.

        EXAMPLES::

            sage: Partition([]).add_horizontal_border_strip(0)
            [[]]
            sage: Partition([3,2,1]).add_horizontal_border_strip(0)
            [[3, 2, 1]]
            sage: Partition([]).add_horizontal_border_strip(2)
            [[2]]
            sage: Partition([2,2]).add_horizontal_border_strip(2)
            [[4, 2], [3, 2, 1], [2, 2, 2]]
            sage: Partition([3,2,2]).add_horizontal_border_strip(2)
            [[5, 2, 2], [4, 3, 2], [4, 2, 2, 1], [3, 3, 2, 1], [3, 2, 2, 2]]
        """
    def vertical_border_strip_cells(self, k) -> Generator[Incomplete, None, Incomplete]:
        """
        Return a list of all the vertical border strips of length ``k``
        which can be added to ``self``, where each horizontal border strip is
        a ``generator`` of cells.

        EXAMPLES::

            sage: list(Partition([]).vertical_border_strip_cells(0))
            []
            sage: list(Partition([3,2,1]).vertical_border_strip_cells(0))
            []
            sage: list(Partition([]).vertical_border_strip_cells(2))
            [[(0, 0), (1, 0)]]
            sage: list(Partition([2,2]).vertical_border_strip_cells(2))
            [[(0, 2), (1, 2)],
             [(0, 2), (2, 0)],
             [(2, 0), (3, 0)]]
            sage: list(Partition([3,2,2]).vertical_border_strip_cells(2))
            [[(0, 3), (1, 2)],
             [(0, 3), (3, 0)],
             [(1, 2), (2, 2)],
             [(1, 2), (3, 0)],
             [(3, 0), (4, 0)]]
        """
    def horizontal_border_strip_cells(self, k) -> Generator[Incomplete, None, Incomplete]:
        """
        Return a list of all the horizontal border strips of length ``k``
        which can be added to ``self``, where each horizontal border strip is
        a ``generator`` of cells.

        EXAMPLES::

            sage: list(Partition([]).horizontal_border_strip_cells(0))
            []
            sage: list(Partition([3,2,1]).horizontal_border_strip_cells(0))
            []
            sage: list(Partition([]).horizontal_border_strip_cells(2))
            [[(0, 0), (0, 1)]]
            sage: list(Partition([2,2]).horizontal_border_strip_cells(2))
            [[(0, 2), (0, 3)], [(0, 2), (2, 0)], [(2, 0), (2, 1)]]
            sage: list(Partition([3,2,2]).horizontal_border_strip_cells(2))
            [[(0, 3), (0, 4)],
             [(0, 3), (1, 2)],
             [(0, 3), (3, 0)],
             [(1, 2), (3, 0)],
             [(3, 0), (3, 1)]]
        """
    def remove_horizontal_border_strip(self, k):
        """
        Return the partitions obtained from ``self`` by removing an
        horizontal border strip of length ``k``.

        EXAMPLES::

            sage: Partition([5,3,1]).remove_horizontal_border_strip(0).list()
            [[5, 3, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(1).list()
            [[5, 3], [5, 2, 1], [4, 3, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(2).list()
            [[5, 2], [5, 1, 1], [4, 3], [4, 2, 1], [3, 3, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(3).list()
            [[5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(4).list()
            [[4, 1], [3, 2], [3, 1, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(5).list()
            [[3, 1]]
            sage: Partition([5,3,1]).remove_horizontal_border_strip(6).list()
            []

        The result is returned as an instance of
        :class:`Partitions_with_constraints`::

            sage: Partition([5,3,1]).remove_horizontal_border_strip(5)
            The subpartitions of [5, 3, 1] obtained by removing a horizontal border strip of length 5

        TESTS::

            sage: Partition([3,2,2]).remove_horizontal_border_strip(2).list()
            [[3, 2], [2, 2, 1]]
            sage: Partition([3,2,2]).remove_horizontal_border_strip(2).first().parent()
            The subpartitions of [3, 2, 2] obtained by removing a horizontal border strip of length 2
            sage: Partition([]).remove_horizontal_border_strip(0).list()
            [[]]
            sage: Partition([]).remove_horizontal_border_strip(6).list()
            []
        """
    def k_conjugate(self, k):
        """
        Return the ``k``-conjugate of ``self``.

        The `k`-conjugate is the partition that is given by the columns of
        the `k`-skew diagram of the partition.

        We can also define the `k`-conjugate in the following way. Let `P`
        denote the bijection from `(k+1)`-cores to `k`-bounded partitions. The
        `k`-conjugate of a `(k+1)`-core `\\lambda` is

        .. MATH::

            \\lambda^{(k)} = P^{-1}\\left( (P(\\lambda))^{\\prime} \\right).

        EXAMPLES::

            sage: p = Partition([4,3,2,2,1,1])
            sage: p.k_conjugate(4)
            [3, 2, 2, 1, 1, 1, 1, 1, 1]
        """
    def arms_legs_coeff(self, i, j):
        """
        This is a statistic on a cell `c = (i,j)` in the diagram of partition
        `p` given by

        .. MATH::

            \\frac{ 1 - q^a \\cdot t^{\\ell + 1} }{ 1 - q^{a + 1} \\cdot t^{\\ell} }

        where `a` is the arm length of `c` and `\\ell` is the leg length of `c`.

        The coordinates ``i`` and ``j`` of the cell are understood to be
        `0`-based, so that ``(0, 0)`` is the northwesternmost cell (in
        English notation).

        EXAMPLES::

            sage: Partition([3,2,1]).arms_legs_coeff(1,1)
            (-t + 1)/(-q + 1)
            sage: Partition([3,2,1]).arms_legs_coeff(0,0)
            (-q^2*t^3 + 1)/(-q^3*t^2 + 1)
            sage: Partition([3,2,1]).arms_legs_coeff(*[0,0])
            (-q^2*t^3 + 1)/(-q^3*t^2 + 1)
        """
    def atom(self):
        """
        Return a list of the standard tableaux of size ``self.size()`` whose
        atom is equal to ``self``.

        EXAMPLES::

            sage: Partition([2,1]).atom()
            [[[1, 2], [3]]]
            sage: Partition([3,2,1]).atom()
            [[[1, 2, 3, 6], [4, 5]], [[1, 2, 3], [4, 5], [6]]]
        """
    def k_atom(self, k):
        """
        Return a list of the standard tableaux of size ``self.size()`` whose
        ``k``-atom is equal to ``self``.

        EXAMPLES::

            sage: p = Partition([3,2,1])
            sage: p.k_atom(1)
            []
            sage: p.k_atom(3)
            [[[1, 1, 1, 2, 3], [2]],
             [[1, 1, 1, 3], [2, 2]],
             [[1, 1, 1, 2], [2], [3]],
             [[1, 1, 1], [2, 2], [3]]]
            sage: Partition([3,2,1]).k_atom(4)
            [[[1, 1, 1, 3], [2, 2]], [[1, 1, 1], [2, 2], [3]]]

        TESTS::

            sage: Partition([1]).k_atom(1)
            [[[1]]]
            sage: Partition([1]).k_atom(2)
            [[[1]]]
            sage: Partition([]).k_atom(1)
            [[]]
        """
    def k_split(self, k):
        """
        Return the ``k``-split of ``self``.

        EXAMPLES::

            sage: Partition([4,3,2,1]).k_split(3)
            []
            sage: Partition([4,3,2,1]).k_split(4)
            [[4], [3, 2], [1]]
            sage: Partition([4,3,2,1]).k_split(5)
            [[4, 3], [2, 1]]
            sage: Partition([4,3,2,1]).k_split(6)
            [[4, 3, 2], [1]]
            sage: Partition([4,3,2,1]).k_split(7)
            [[4, 3, 2, 1]]
            sage: Partition([4,3,2,1]).k_split(8)
            [[4, 3, 2, 1]]
        """
    def jacobi_trudi(self):
        """
        Return the Jacobi-Trudi matrix of ``self`` thought of as a skew
        partition. See :meth:`SkewPartition.jacobi_trudi()
        <sage.combinat.skew_partition.SkewPartition.jacobi_trudi>`.

        EXAMPLES::

            sage: # needs sage.modules
            sage: part = Partition([3,2,1])
            sage: jt = part.jacobi_trudi(); jt
            [h[3] h[1]    0]
            [h[4] h[2]  h[]]
            [h[5] h[3] h[1]]
            sage: s = SymmetricFunctions(QQ).schur()
            sage: h = SymmetricFunctions(QQ).homogeneous()
            sage: h( s(part) )
            h[3, 2, 1] - h[3, 3] - h[4, 1, 1] + h[5, 1]
            sage: jt.det()
            h[3, 2, 1] - h[3, 3] - h[4, 1, 1] + h[5, 1]
        """
    def character_polynomial(self):
        """
        Return the character polynomial associated to the partition ``self``.

        The character polynomial `q_\\mu` associated to a partition `\\mu`
        is defined by

        .. MATH::

            q_\\mu(x_1, x_2, \\ldots, x_k) = \\downarrow \\sum_{\\alpha \\vdash k}
            \\frac{ \\chi^\\mu_\\alpha }{1^{a_1}2^{a_2}\\cdots k^{a_k}a_1!a_2!\\cdots
            a_k!} \\prod_{i=1}^{k} (ix_i-1)^{a_i}

        where `k` is the size of `\\mu`, and `a_i` is the multiplicity of
        `i` in `\\alpha`.

        It is computed in the following manner:

        1. Expand the Schur function `s_\\mu` in the power-sum basis,

        2. Replace each `p_i` with `ix_i-1`,

        3. Apply the umbral operator `\\downarrow` to the resulting polynomial.

        EXAMPLES::

            sage: Partition([1]).character_polynomial()                                 # needs sage.modules
            x - 1
            sage: Partition([1,1]).character_polynomial()                               # needs sage.modules
            1/2*x0^2 - 3/2*x0 - x1 + 1
            sage: Partition([2,1]).character_polynomial()                               # needs sage.modules
            1/3*x0^3 - 2*x0^2 + 8/3*x0 - x2
        """
    def dimension(self, smaller=None, k: int = 1):
        """
        Return the number of paths from the ``smaller`` partition to
        the partition ``self``, where each step consists of adding a
        `k`-ribbon while keeping a partition.

        Note that a 1-ribbon is just a single cell, so this counts paths
        in the Young graph when `k = 1`.

        Note also that the default case (`k = 1` and ``smaller = []``)
        gives the dimension of the irreducible representation of the
        symmetric group corresponding to ``self``.

        INPUT:

        - ``smaller`` -- a partition (default: an empty list ``[]``)

        - ``k`` -- positive integer (default: 1)

        OUTPUT: the number of such paths

        EXAMPLES:

        Looks at the number of ways of getting from ``[5,4]`` to the empty
        partition, removing one cell at a time::

            sage: mu = Partition([5,4])
            sage: mu.dimension()
            42

        Same, but removing one 3-ribbon at a time. Note that the 3-core of
        ``mu`` is empty::

            sage: mu.dimension(k=3)
            3

        The 2-core of ``mu`` is not the empty partition::

            sage: mu.dimension(k=2)
            0

        Indeed, the 2-core of ``mu`` is ``[1]``::

            sage: mu.dimension(Partition([1]),k=2)
            2

        TESTS:

        Checks that the sum of squares of dimensions of characters of the
        symmetric group is the order of the group::

            sage: all(sum(mu.dimension()^2 for mu in Partitions(i)) == factorial(i)
            ....:     for i in range(10))
            True

        A check coming from the theory of `k`-differentiable posets::

            sage: k = 2; core = Partition([2,1])
            sage: all(sum(mu.dimension(core,k=2)^2
            ....:         for mu in Partitions(3+i*2) if mu.core(2) == core)
            ....:     == 2^i*factorial(i) for i in range(10))
            True

        Checks that the dimension satisfies the obvious recursion relation::

            sage: test = lambda larger, smaller: larger.dimension(smaller) == sum(mu.dimension(smaller) for mu in larger.down())
            sage: all(test(larger,smaller) for l in range(1,8) for s in range(8)
            ....:     for larger in Partitions(l) for smaller in Partitions(s) if smaller != larger)
            True

        ALGORITHM:

        Depending on the parameters given, different simplifications
        occur. When `k=1` and ``smaller`` is empty, this function uses
        the hook formula. When `k=1` and ``smaller`` is not empty, it
        uses a formula from [ORV]_.

        When `k \\neq 1`, we first check that both ``self`` and
        ``smaller`` have the same `k`-core, then use the `k`-quotients
        and the same algorithm on each of the `k`-quotients.

        AUTHORS:

        - Paul-Olivier Dehaye (2011-06-07)
        """
    def plancherel_measure(self):
        """
        Return the probability of ``self`` under the Plancherel probability
        measure on partitions of the same size.

        This probability distribution comes from the uniform distribution
        on permutations via the Robinson-Schensted correspondence.

        See :wikipedia:`Plancherel\\_measure`
        and :meth:`Partitions_n.random_element_plancherel`.

        EXAMPLES::

            sage: Partition([]).plancherel_measure()
            1
            sage: Partition([1]).plancherel_measure()
            1
            sage: Partition([2]).plancherel_measure()
            1/2
            sage: [mu.plancherel_measure() for mu in Partitions(3)]
            [1/6, 2/3, 1/6]
            sage: Partition([5,4]).plancherel_measure()
            7/1440

        TESTS::

            sage: all(sum(mu.plancherel_measure() for mu in Partitions(n))==1 for n in range(10))
            True
        """
    def outline(self, variable=None):
        '''
        Return the outline of the partition ``self``.

        This is a piecewise linear function, normalized so that the area
        under the partition ``[1]`` is 2.

        INPUT:

        - ``variable`` -- a variable (default: ``\'x\'`` in the symbolic ring)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: [Partition([5,4]).outline()(x=i) for i in range(-10, 11)]
            [10, 9, 8, 7, 6, 5, 6, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: Partition([]).outline()
            abs(x)
            sage: Partition([1]).outline()
            abs(x + 1) + abs(x - 1) - abs(x)
            sage: y = SR.var("y")
            sage: Partition([6,5,1]).outline(variable=y)
            abs(y + 6) - abs(y + 5) + abs(y + 4) - abs(y + 3)
             + abs(y - 1) - abs(y - 2) + abs(y - 3)

        TESTS::

            sage: integrate(Partition([1]).outline() - abs(x), (x, -10, 10))              # needs sage.symbolic
            2
        '''
    def dual_equivalence_graph(self, directed: bool = False, coloring=None):
        """
        Return the dual equivalence graph of ``self``.

        Two permutations `p` and `q` in the symmetric group `S_n`
        differ by an `i`-*elementary dual equivalence (or dual Knuth)
        relation* (where `i` is an integer with `1 < i < n`) when the
        following two conditions are satisfied:

        - In the one-line notation of the permutation `p`, the letter
          `i` does not appear between `i-1` and `i+1`.

        - The permutation `q` is obtained from `p` by switching two
          of the three letters `i-1, i, i+1` (in its one-line
          notation) -- namely, the leftmost and the rightmost one
          in order of their appearance in `p`.

        Notice that this is equivalent to the statement that the
        permutations `p^{-1}` and `q^{-1}` differ by an elementary
        Knuth equivalence at positions `i-1, i, i+1`.

        Two standard Young tableaux of shape `\\lambda` differ by an
        `i`-elementary dual equivalence relation (of color `i`), if
        their reading words differ by an `i`-elementary dual
        equivalence relation.

        The *dual equivalence graph* of the partition `\\lambda` is the
        edge-colored graph whose vertices are the standard Young
        tableaux of shape `\\lambda`, and whose edges colored by `i` are
        given by the `i`-elementary dual equivalences.

        INPUT:

        - ``directed`` -- boolean (default: ``False``); whether to have the
          dual equivalence graph be directed (where we have a directed edge
          `S \\to T` if `i` appears to the left of `i+1` in the reading word of
          `T`; otherwise we have the directed edge `T \\to S`)

        - ``coloring`` -- (optional) a function which sends each
          integer `i > 1` to a color (as a string, e.g., ``'red'`` or
          ``'black'``) to be used when visually representing the
          resulting graph using dot2tex; the default choice is
          ``2 -> 'red', 3 -> 'blue', 4 -> 'green', 5 -> 'purple',
          6 -> 'brown', 7 -> 'orange', 8 -> 'yellow', anything greater
          than 8 -> 'black'``.

        REFERENCES:

        - [As2008b]_

        EXAMPLES::

            sage: # needs sage.graphs
            sage: P = Partition([3,1,1])
            sage: G = P.dual_equivalence_graph()
            sage: G.edges(sort=True)
            [([[1, 2, 3], [4], [5]], [[1, 2, 4], [3], [5]], 3),
             ([[1, 2, 4], [3], [5]], [[1, 2, 5], [3], [4]], 4),
             ([[1, 2, 4], [3], [5]], [[1, 3, 4], [2], [5]], 2),
             ([[1, 2, 5], [3], [4]], [[1, 3, 5], [2], [4]], 2),
             ([[1, 3, 4], [2], [5]], [[1, 3, 5], [2], [4]], 4),
             ([[1, 3, 5], [2], [4]], [[1, 4, 5], [2], [3]], 3)]
            sage: G = P.dual_equivalence_graph(directed=True)
            sage: G.edges(sort=True)
            [([[1, 2, 4], [3], [5]], [[1, 2, 3], [4], [5]], 3),
             ([[1, 2, 5], [3], [4]], [[1, 2, 4], [3], [5]], 4),
             ([[1, 3, 4], [2], [5]], [[1, 2, 4], [3], [5]], 2),
             ([[1, 3, 5], [2], [4]], [[1, 2, 5], [3], [4]], 2),
             ([[1, 3, 5], [2], [4]], [[1, 3, 4], [2], [5]], 4),
             ([[1, 4, 5], [2], [3]], [[1, 3, 5], [2], [4]], 3)]

        TESTS::

            sage: # needs sage.graphs
            sage: G = Partition([1]).dual_equivalence_graph()
            sage: G.vertices(sort=False)
            [[[1]]]
            sage: G = Partition([]).dual_equivalence_graph()
            sage: G.vertices(sort=False)
            [[]]
            sage: P = Partition([3,1,1])
            sage: G = P.dual_equivalence_graph(coloring=lambda x: 'red')
            sage: G2 = P.dual_equivalence_graph(coloring={2: 'black', 3: 'blue',
            ....:                                         4: 'cyan', 5: 'grey'})
            sage: G is G2
            False
            sage: G == G2
            True
        """
    def specht_module(self, base_ring=None):
        """
        Return the Specht module corresponding to ``self``.

        EXAMPLES::

            sage: SM = Partition([2,2,1]).specht_module(QQ); SM                         # needs sage.modules
            Specht module of [2, 2, 1] over Rational Field
            sage: SM.frobenius_image()                                                  # needs sage.modules
            s[2, 2, 1]
        """
    def garsia_procesi_module(self, base_ring=None):
        """
        Return the :class:`Garsia-Procesi module
        <sage.combinat.symmetric_group_representations.GarsiaProcesiModule>`
        corresponding to ``self``.

        INPUT:

        - ``base_ring`` -- (default: `\\QQ`) the base ring

        EXAMPLES::

            sage: GP = Partition([3,2,1]).garsia_procesi_module(QQ); GP
            Garsia-Procesi module of shape [3, 2, 1] over Rational Field
            sage: GP.graded_frobenius_image()
            q^4*s[3, 2, 1] + q^3*s[3, 3] + q^3*s[4, 1, 1] + (q^3+q^2)*s[4, 2]
             + (q^2+q)*s[5, 1] + s[6]

            sage: Partition([3,2,1]).garsia_procesi_module(GF(3))
            Garsia-Procesi module of shape [3, 2, 1] over Finite Field of size 3
        """
    def specht_module_dimension(self, base_ring=None):
        """
        Return the dimension of the Specht module corresponding to ``self``.

        This is equal to the number of standard tableaux of shape ``self`` when
        over a field of characteristic `0`.

        INPUT:

        - ``base_ring`` -- (default: `\\QQ`) the base ring

        EXAMPLES::

            sage: Partition([2,2,1]).specht_module_dimension()
            5
            sage: Partition([2,2,1]).specht_module_dimension(GF(2))                     # needs sage.rings.finite_rings
            5
        """
    def simple_module_dimension(self, base_ring=None):
        """
        Return the dimension of the simple module corresponding to ``self``.

        When the base ring is a field of characteristic `0`, this is equal
        to the dimension of the Specht module.

        INPUT:

        - ``base_ring`` -- (default: `\\QQ`) the base ring

        EXAMPLES::

            sage: Partition([2,2,1]).simple_module_dimension()
            5
            sage: Partition([2,2,1]).specht_module_dimension(GF(3))                     # needs sage.rings.finite_rings
            5
            sage: Partition([2,2,1]).simple_module_dimension(GF(3))                     # needs sage.rings.finite_rings
            4

            sage: for la in Partitions(6, regular=3):
            ....:     print(la, la.specht_module_dimension(), la.simple_module_dimension(GF(3)))
            [6] 1 1
            [5, 1] 5 4
            [4, 2] 9 9
            [4, 1, 1] 10 6
            [3, 3] 5 1
            [3, 2, 1] 16 4
            [2, 2, 1, 1] 9 9
        """
    def tabloid_module(self, base_ring=None):
        """
        Return the tabloid module corresponding to ``self``.

        EXAMPLES::

            sage: TM = Partition([2,2,1]).tabloid_module(QQ); TM
            Tabloid module of [2, 2, 1] over Rational Field
            sage: TM.frobenius_image()
            s[2, 2, 1] + s[3, 1, 1] + 2*s[3, 2] + 2*s[4, 1] + s[5]
        """

class Partitions(UniqueRepresentation, Parent):
    """
    ``Partitions(n, **kwargs)`` returns the combinatorial class of
    integer partitions of `n` subject to the constraints given by the
    keywords.

    Valid keywords are: ``starting``, ``ending``, ``min_part``,
    ``max_part``, ``max_length``, ``min_length``, ``length``,
    ``max_slope``, ``min_slope``, ``inner``, ``outer``, ``parts_in``,
    ``regular``, and ``restricted``. They have the following meanings:

    - ``starting=p`` specifies that the partitions should all be less
      than or equal to `p` in lex order. This argument cannot be combined
      with any other (see :issue:`15467`).

    - ``ending=p`` specifies that the partitions should all be greater than
      or equal to `p` in lex order. This argument cannot be combined with any
      other (see :issue:`15467`).

    - ``length=k`` specifies that the partitions have
      exactly `k` parts.

    - ``min_length=k`` specifies that the partitions have
      at least `k` parts.

    - ``min_part=k`` specifies that all parts of the
      partitions are at least `k`.

    - ``inner=p`` specifies that the partitions must contain the
      partition `p`.

    - ``outer=p`` specifies that the partitions
      be contained inside the partition `p`.

    - ``min_slope=k`` specifies that the partitions have slope at least
      `k`; the slope at position `i` is the difference between the
      `(i+1)`-th part and the `i`-th part.

    - ``parts_in=S`` specifies that the partitions have parts in the set
      `S`, which can be any sequence of pairwise distinct positive
      integers. This argument cannot be combined with any other
      (see :issue:`15467`).

    - ``regular=ell`` specifies that the partitions are `\\ell`-regular,
      and can only be combined with the ``max_length`` or ``max_part``, but
      not both, keywords if `n` is not specified

    - ``restricted=ell`` specifies that the partitions are `\\ell`-restricted,
      and cannot be combined with any other keywords

    The ``max_*`` versions, along with ``inner`` and ``ending``, work
    analogously.

    Right now, the ``parts_in``, ``starting``, ``ending``, ``regular``, and
    ``restricted`` keyword arguments are mutually exclusive, both of each
    other and of other keyword arguments. If you specify, say, ``parts_in``,
    all other keyword arguments will be ignored; ``starting``, ``ending``,
    ``regular``, and ``restricted`` work the same way.

    EXAMPLES:

    If no arguments are passed, then the combinatorial class
    of all integer partitions is returned::

        sage: Partitions()
        Partitions
        sage: [2,1] in Partitions()
        True

    If an integer `n` is passed, then the combinatorial class of integer
    partitions of `n` is returned::

        sage: Partitions(3)
        Partitions of the integer 3
        sage: Partitions(3).list()
        [[3], [2, 1], [1, 1, 1]]

    If ``starting=p`` is passed, then the combinatorial class of partitions
    greater than or equal to `p` in lexicographic order is returned::

        sage: Partitions(3, starting=[2,1])
        Partitions of the integer 3 starting with [2, 1]
        sage: Partitions(3, starting=[2,1]).list()
        [[2, 1], [1, 1, 1]]

    If ``ending=p`` is passed, then the combinatorial class of
    partitions at most `p` in lexicographic order is returned::

        sage: Partitions(3, ending=[2,1])
        Partitions of the integer 3 ending with [2, 1]
        sage: Partitions(3, ending=[2,1]).list()
        [[3], [2, 1]]

    Using ``max_slope=-1`` yields partitions into distinct parts -- each
    part differs from the next by at least 1. Use a different
    ``max_slope`` to get parts that differ by, say, 2::

        sage: Partitions(7, max_slope=-1).list()
        [[7], [6, 1], [5, 2], [4, 3], [4, 2, 1]]
        sage: Partitions(15, max_slope=-1).cardinality()
        27

    The number of partitions of `n` into odd parts equals the number of
    partitions into distinct parts. Let's test that for `n` from 10 to 20::

        sage: def test(n):
        ....:     return (Partitions(n, max_slope=-1).cardinality()
        ....:              == Partitions(n, parts_in=[1,3..n]).cardinality())
        sage: all(test(n) for n in [10..20])                                            # needs sage.libs.gap
        True

    The number of partitions of `n` into distinct parts that differ by
    at least 2 equals the number of partitions into parts that equal 1
    or 4 modulo 5; this is one of the Rogers-Ramanujan identities::

        sage: def test(n):
        ....:     return (Partitions(n, max_slope=-2).cardinality()
        ....:              == Partitions(n, parts_in=([1,6..n] + [4,9..n])).cardinality())
        sage: all(test(n) for n in [10..20])                                            # needs sage.libs.gap
        True

    Here are some more examples illustrating ``min_part``, ``max_part``,
    and ``length``::

        sage: Partitions(5, min_part=2)
        Partitions of 5 whose parts are at least 2
        sage: Partitions(5, min_part=2).list()
        [[5], [3, 2]]

    ::

        sage: Partitions(3, max_length=2).list()
        [[3], [2, 1]]

    ::

        sage: Partitions(10, min_part=2, length=3).list()
        [[6, 2, 2], [5, 3, 2], [4, 4, 2], [4, 3, 3]]

    Some examples using the ``regular`` keyword::

        sage: Partitions(regular=4)
        4-Regular Partitions
        sage: Partitions(regular=4, max_length=3)
        4-Regular Partitions with max length 3
        sage: Partitions(regular=4, max_part=3)
        4-Regular 3-Bounded Partitions
        sage: Partitions(3, regular=4)
        4-Regular Partitions of the integer 3

    Some examples using the ``restricted`` keyword::

        sage: Partitions(restricted=4)
        4-Restricted Partitions
        sage: Partitions(3, restricted=4)
        4-Restricted Partitions of the integer 3

    Here are some further examples using various constraints::

        sage: [x for x in Partitions(4)]
        [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
        sage: [x for x in Partitions(4, length=2)]
        [[3, 1], [2, 2]]
        sage: [x for x in Partitions(4, min_length=2)]
        [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
        sage: [x for x in Partitions(4, max_length=2)]
        [[4], [3, 1], [2, 2]]
        sage: [x for x in Partitions(4, min_length=2, max_length=2)]
        [[3, 1], [2, 2]]
        sage: [x for x in Partitions(4, max_part=2)]
        [[2, 2], [2, 1, 1], [1, 1, 1, 1]]
        sage: [x for x in Partitions(4, min_part=2)]
        [[4], [2, 2]]
        sage: [x for x in Partitions(4, outer=[3,1,1])]
        [[3, 1], [2, 1, 1]]
        sage: [x for x in Partitions(4, outer=[infinity, 1, 1])]
        [[4], [3, 1], [2, 1, 1]]
        sage: [x for x in Partitions(4, inner=[1,1,1])]
        [[2, 1, 1], [1, 1, 1, 1]]
        sage: [x for x in Partitions(4, max_slope=-1)]
        [[4], [3, 1]]
        sage: [x for x in Partitions(4, min_slope=-1)]
        [[4], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
        sage: [x for x in Partitions(11, max_slope=-1, min_slope=-3, min_length=2, max_length=4)]
        [[7, 4], [6, 5], [6, 4, 1], [6, 3, 2], [5, 4, 2], [5, 3, 2, 1]]
        sage: [x for x in Partitions(11, max_slope=-1, min_slope=-3, min_length=2, max_length=4, outer=[6,5,2])]
        [[6, 5], [6, 4, 1], [6, 3, 2], [5, 4, 2]]

    Note that if you specify ``min_part=0``, then it will treat the minimum
    part as being 1 (see :issue:`13605`)::

        sage: [x for x in Partitions(4, length=3, min_part=0)]
        [[2, 1, 1]]
        sage: [x for x in Partitions(4, min_length=3, min_part=0)]
        [[2, 1, 1], [1, 1, 1, 1]]

    Except for very special cases, counting is done by brute force iteration
    through all the partitions. However the iteration itself has a reasonable
    complexity (see :class:`IntegerListsLex`), which allows for
    manipulating large partitions::

        sage: Partitions(1000, max_length=1).list()
        [[1000]]

    In particular, getting the first element is also constant time::

        sage: Partitions(30, max_part=29).first()
        [29, 1]

    TESTS::

        sage: TestSuite(Partitions(0)).run()                                            # needs sage.libs.flint
        sage: TestSuite(Partitions(5)).run()                                            # needs sage.libs.flint
        sage: TestSuite(Partitions(5, min_part=2)).run()                                # needs sage.libs.flint

        sage: repr(Partitions(5, min_part=2))
        'Partitions of 5 whose parts are at least 2'

        sage: P = Partitions(5, min_part=2)
        sage: P.first().parent()
        Partitions...
        sage: [2,1] in P
        False
        sage: [2,2,1] in P
        False
        sage: [3,2] in P
        True

        sage: Partitions(5, inner=[2,1], min_length=3).list()
        [[3, 1, 1], [2, 2, 1], [2, 1, 1, 1]]
        sage: Partitions(5, inner=Partition([2,2]), min_length=3).list()
        [[2, 2, 1]]
        sage: Partitions(7, inner=(2, 2), min_length=3).list()
        [[4, 2, 1], [3, 3, 1], [3, 2, 2], [3, 2, 1, 1], [2, 2, 2, 1], [2, 2, 1, 1, 1]]
        sage: Partitions(5, inner=[2,0,0,0,0,0]).list()
        [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1]]
        sage: Partitions(6, length=2, max_slope=-1).list()
        [[5, 1], [4, 2]]

        sage: Partitions(length=2, max_slope=-1).list()
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot list an infinite set

        sage: Partitions(max_part=3)
        3-Bounded Partitions

    Check that :issue:`14145` has been fixed::

        sage: 1 in Partitions()
        False

    Check :issue:`15467`::

        sage: Partitions(5, parts_in=[1,2,3,4], length=4)
        Traceback (most recent call last):
        ...
        ValueError: the parameters 'parts_in', 'starting', 'ending', 'regular' and 'restricted' cannot be combined with anything else
        sage: Partitions(5, starting=[3,2], length=2)
        Traceback (most recent call last):
        ...
        ValueError: the parameters 'parts_in', 'starting', 'ending', 'regular' and 'restricted' cannot be combined with anything else
        sage: Partitions(5, ending=[3,2], length=2)
        Traceback (most recent call last):
        ...
        ValueError: the parameters 'parts_in', 'starting', 'ending', 'regular' and 'restricted' cannot be combined with anything else
        sage: Partitions(5, restricted=2, length=2)
        Traceback (most recent call last):
        ...
        ValueError: the parameters 'parts_in', 'starting', 'ending', 'regular' and 'restricted' cannot be combined with anything else
        sage: Partitions(5, regular=5, length=2)
        Traceback (most recent call last):
        ...
        ValueError: the parameters 'parts_in', 'starting', 'ending', 'regular' and 'restricted' cannot be combined with anything else
        sage: Partitions(NN, length=2)
        Partitions satisfying constraints length=2

        sage: Partitions(('la','la','laaaa'), max_part=8)
        Traceback (most recent call last):
        ...
        ValueError: n must be an integer or be equal to one of None, NN, NonNegativeIntegers()

    Check that calling ``Partitions`` with ``outer=a`` no longer
    mutates ``a`` (:issue:`16234`)::

        sage: a = [4,3,2,1,1,1,1]
        sage: for p in Partitions(8, outer=a, min_slope=-1):
        ....:    print(p)
        [3, 3, 2]
        [3, 2, 2, 1]
        [3, 2, 1, 1, 1]
        [2, 2, 2, 1, 1]
        [2, 2, 1, 1, 1, 1]
        [2, 1, 1, 1, 1, 1, 1]
        sage: a
        [4, 3, 2, 1, 1, 1, 1]

    Check that ``inner`` and ``outer`` indeed accept a partition as
    argument (:issue:`18423`)::

        sage: P = Partitions(5, inner=Partition([2,1]), outer=Partition([3,2])); P
        Partitions of the integer 5 satisfying constraints inner=[2, 1], outer=[3, 2]
        sage: P.list()
        [[3, 2]]

    Check that contradictory length requirements are handled correctly::

        sage: list(Partitions(5, max_length=1, length=3))
        Traceback (most recent call last):
        ...
        ValueError: do not specify the length together with the minimal or maximal length

        sage: list(Partitions(5, min_length=2, max_length=1))
        []

    Check that :issue:`38897` is fixed::

        sage: Partitions(40, min_length=10).cardinality()
        24000

        sage: Partitions(40, max_length=10).cardinality()
        16928
    """
    @staticmethod
    def __classcall_private__(cls, n=None, **kwargs):
        """
        Return the correct parent based upon the input.

        TESTS::

            sage: P = Partitions()
            sage: P2 = Partitions(NN)
            sage: P is P2
            True
            sage: P2 = Partitions(NonNegativeIntegers())
            sage: P is P2
            True
            sage: P = Partitions(4)
            sage: P2 = Partitions(int(4))
            sage: P is P2
            True

        Check that :issue:`17898` is fixed::

            sage: P = Partitions(5, min_slope=0)
            sage: list(P)
            [[5], [1, 1, 1, 1, 1]]
        """
    def __init__(self, is_infinite: bool = False) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``is_infinite`` -- boolean (default: ``False``); if ``True``, then
          the number of partitions in this set is infinite

        EXAMPLES::

            sage: Partitions()
            Partitions
            sage: Partitions(2)
            Partitions of the integer 2
        """
    Element = Partition
    class options(GlobalOptions):
        '''
        Set and display the global options for elements of the partition,
        skew partition, and partition tuple classes.  If no parameters are
        set, then the function returns a copy of the options dictionary.

        The ``options`` to partitions can be accessed as the method
        :obj:`Partitions.options` of :class:`Partitions` and
        related parent classes.

        @OPTIONS@

        EXAMPLES::

            sage: P = Partition([4,2,2,1])
            sage: P
            [4, 2, 2, 1]
            sage: Partitions.options.display="exp"
            sage: P
            1, 2^2, 4
            sage: Partitions.options.display="exp_high"
            sage: P
            4, 2^2, 1

        It is also possible to use user defined functions for the ``display`` and
        ``latex`` options::

            sage: Partitions.options(display=lambda mu: \'<%s>\' % \',\'.join(\'%s\'%m for m in mu._list)); P
            <4,2,2,1>
            sage: Partitions.options(latex=lambda mu: \'\\\\Diagram{%s}\' % \',\'.join(\'%s\'%m for m in mu._list)); latex(P)
            \\Diagram{4,2,2,1}
            sage: Partitions.options(display=\'diagram\', diagram_str=\'#\')
            sage: P
            ####
            ##
            ##
            #
            sage: Partitions.options(diagram_str=\'*\', convention=\'french\')
            sage: print(P.ferrers_diagram())
            *
            **
            **
            ****

        Changing the ``convention`` for partitions also changes the ``convention``
        option for tableaux and vice versa::

            sage: T = Tableau([[1,2,3],[4,5]])
            sage: T.pp()
              4  5
              1  2  3
            sage: Tableaux.options.convention="english"
            sage: print(P.ferrers_diagram())
            ****
            **
            **
            *
            sage: T.pp()
              1  2  3
              4  5
            sage: Partitions.options._reset()
        '''
        NAME: str
        module: str
        display: Incomplete
        latex: Incomplete
        diagram_str: Incomplete
        latex_diagram_str: Incomplete
        convention: Incomplete
        notation: Incomplete
    def __reversed__(self) -> Generator[Incomplete]:
        """
        A reversed iterator.

        EXAMPLES::

            sage: [x for x in reversed(Partitions(4))]
            [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: P = Partitions()
            sage: Partition([2,1]) in P
            True
            sage: [2,1] in P
            True
            sage: [3,2,1] in P
            True
            sage: [1,2] in P
            False
            sage: [] in P
            True
            sage: [0] in P
            True

        Check that types that represent integers are not excluded::

            sage: P = Partitions()
            sage: [3/1, 2/2] in P
            True
            sage: Partition([3/1, 2]) in P
            True

        Check that non-integers and non-lists are excluded::

            sage: P = Partitions()
            sage: [2,1.5] in P
            False

            sage: 0 in P
            False
        """
    def subset(self, *args, **kwargs):
        """
        Return ``self`` if no arguments are given.

        Otherwise, it raises a :exc:`ValueError`.

        EXAMPLES::

            sage: P = Partitions(5, starting=[3,1]); P
            Partitions of the integer 5 starting with [3, 1]
            sage: P.subset()
            Partitions of the integer 5 starting with [3, 1]
            sage: P.subset(ending=[3,1])
            Traceback (most recent call last):
            ...
            ValueError: invalid combination of arguments
        """

class Partitions_all(Partitions):
    """
    Class of all partitions.

    TESTS::

        sage: TestSuite( sage.combinat.partition.Partitions_all() ).run()
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: P = Partitions()
            sage: P.category()
            Category of infinite enumerated sets
            sage: Partitions().cardinality()
            +Infinity
            sage: TestSuite(P).run()
        """
    def subset(self, size=None, **kwargs):
        """
        Return the subset of partitions of a given size and additional
        keyword arguments.

        EXAMPLES::

            sage: P = Partitions()
            sage: P.subset(4)
            Partitions of the integer 4
        """
    def __iter__(self):
        """
        An iterator for all partitions.

        EXAMPLES::

            sage: p = Partitions()
            sage: it = p.__iter__()
            sage: [next(it) for i in range(10)]
            [[], [1], [2], [1, 1], [3], [2, 1], [1, 1, 1], [4], [3, 1], [2, 2]]
        """
    def __reversed__(self) -> Generator[Incomplete]:
        """
        A reversed iterator for all partitions.

        This reverse iterates through partitions of fixed `n` and incrementing
        `n` after reaching the end.

        EXAMPLES::

            sage: p = Partitions()
            sage: revit = p.__reversed__()
            sage: [next(revit) for i in range(10)]
            [[], [1], [1, 1], [2], [1, 1, 1], [2, 1], [3], [1, 1, 1, 1], [2, 1, 1], [2, 2]]
        """
    def from_frobenius_coordinates(self, frobenius_coordinates):
        """
        Return a partition from a pair of sequences of Frobenius coordinates.

        EXAMPLES::

            sage: Partitions().from_frobenius_coordinates(([],[]))
            []
            sage: Partitions().from_frobenius_coordinates(([0],[0]))
            [1]
            sage: Partitions().from_frobenius_coordinates(([1],[1]))
            [2, 1]
            sage: Partitions().from_frobenius_coordinates(([6,3,2],[4,1,0]))
            [7, 5, 5, 1, 1]
        """
    def from_beta_numbers(self, beta):
        """
        Return a partition corresponding to a sequence of beta numbers.

        A sequence of beta numbers is a strictly increasing sequence
        `0 \\leq b_1 < \\cdots < b_k` of nonnegative integers. The
        corresponding partition `\\mu = (\\mu_k, \\ldots, \\mu_1)` is
        given by `\\mu_i = [1,i) \\setminus \\{ b_1, \\ldots, b_i \\}`. This gives
        a bijection from the set of partitions with at most `k` nonzero parts
        to the set of strictly increasing sequences of nonnegative integers
        of length `k`.

        EXAMPLES::

            sage: Partitions().from_beta_numbers([0,1,2,4,5,8])
            [3, 1, 1]
            sage: Partitions().from_beta_numbers([0,2,3,6])
            [3, 1, 1]
        """
    def from_exp(self, exp):
        """
        Return a partition from its list of multiplicities.

        EXAMPLES::

            sage: Partitions().from_exp([2,2,1])
            [3, 2, 2, 1, 1]
        """
    def from_zero_one(self, seq):
        """
        Return a partition from its `0-1` sequence.

        The full `0-1` sequence is the sequence (infinite in both
        directions) indicating the steps taken when following the
        outer rim of the diagram of the partition. We use the convention
        that in English convention, a 1 corresponds to an East step, and
        a 0 corresponds to a North step.

        Note that every full `0-1` sequence starts with infinitely many 0s and
        ends with infinitely many 1s.

        .. SEEALSO::

            :meth:`Partition.zero_one_sequence()`

        INPUT:

        The input should be a finite sequence of 0s and 1s. The
        heading 0s and trailing 1s will be discarded.

        EXAMPLES::

            sage: Partitions().from_zero_one([])
            []
            sage: Partitions().from_zero_one([1,0])
            [1]
            sage: Partitions().from_zero_one([1, 1, 1, 1, 0, 1, 0])
            [5, 4]

        Heading 0s and trailing 1s are correctly handled::

            sage: Partitions().from_zero_one([0,0,1,1,1,1,0,1,0,1,1,1])
            [5, 4]

        TESTS::

            sage: all(Partitions().from_zero_one(mu.zero_one_sequence()) == mu for n in range(10) for mu in Partitions(n))
            True
        """
    def from_core_and_quotient(self, core, quotient):
        """
        Return a partition from its core and quotient.

        Algorithm from mupad-combinat.

        EXAMPLES::

            sage: Partitions().from_core_and_quotient([2,1], [[2,1],[3],[1,1,1]])
            [11, 5, 5, 3, 2, 2, 2]

        TESTS::

            sage: Partitions().from_core_and_quotient([2,1], [[2,1],[2,3,1],[1,1,1]])
            Traceback (most recent call last):
            ...
            ValueError: the quotient [[2, 1], [2, 3, 1], [1, 1, 1]] must be a tuple of partitions

        We check that :issue:`11412` is actually fixed::

            sage: test = lambda x, k: x == Partition(core=x.core(k),
            ....:                                    quotient=x.quotient(k))
            sage: all(test(mu,k) for k in range(1,5)
            ....:     for n in range(10) for mu in Partitions(n))
            True
            sage: test2 = lambda core, mus: (
            ....:     Partition(core=core, quotient=mus).core(mus.level()) == core
            ....:     and
            ....:     Partition(core=core, quotient=mus).quotient(mus.level()) == mus)
            sage: all(test2(core,mus)  # long time (5s on sage.math, 2011)
            ....:     for k in range(1,10)
            ....:     for n_core in range(10-k)
            ....:     for core in Partitions(n_core)
            ....:     if core.core(k) == core
            ....:     for n_mus in range(10-k)
            ....:     for mus in PartitionTuples(k,n_mus))
            True
        """

class Partitions_all_constrained(Partitions):
    def __init__(self, **kwargs) -> None:
        """
        TESTS::

            sage: TestSuite(sage.combinat.partition.Partitions_all_constrained(max_length=3, max_slope=0)).run() # long time

            sage: list(Partitions(max_part=4, max_slope=-3))
            [[], [1], [2], [3], [4], [4, 1]]

            sage: [pi for n in range(10) for pi in Partitions(n, max_part=4, max_slope=-3)]
            [[], [1], [2], [3], [4], [4, 1]]
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: from sage.combinat.partition import Partitions_all_constrained
            sage: P = Partitions_all_constrained(max_part=3, max_length=2, max_slope=0)
            sage: 1 in P
            False
            sage: Partition([2,1]) in P
            True
            sage: [2,1] in P
            True
            sage: [3,2,1] in P
            False
            sage: [1,2] in P
            False
            sage: [5,1] in P
            False
            sage: [0] in P
            True
            sage: [] in P
            True
            sage: [3,1,0] in P
            True
        """
    def __iter__(self):
        """
        An iterator for partitions with various constraints.

        EXAMPLES::

            sage: P = Partitions(max_length=2)
            sage: it = iter(P)
            sage: [next(it) for i in range(10)]
            [[], [1], [2], [1, 1], [3], [2, 1], [4], [3, 1], [2, 2], [5]]

            sage: P = Partitions(inner=[2,2], outer=[3,2,1])
            sage: list(P)
            [[2, 2], [3, 2], [2, 2, 1], [3, 2, 1]]
        """

class Partitions_all_bounded(Partitions):
    """
    Partitions whose parts do not exceed a given bound.
    """
    k: Incomplete
    def __init__(self, k) -> None:
        """
        TESTS::

            sage: TestSuite(sage.combinat.partition.Partitions_all_bounded(3)).run() # long time
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: P = Partitions(max_part=3)
            sage: 1 in P
            False
            sage: 0 in P
            False
            sage: Partition([2,1]) in P
            True
            sage: [2,1] in P
            True
            sage: [3,2,1] in P
            True
            sage: [1,2] in P
            False
            sage: [5,1] in P
            False
            sage: [0] in P
            True
            sage: [] in P
            True
        """
    def __iter__(self):
        """
        An iterator for all `k`-bounded partitions.

        EXAMPLES::

            sage: p = Partitions(max_part=3)
            sage: it = p.__iter__()
            sage: [next(it) for i in range(10)]
            [[], [1], [2], [1, 1], [3], [2, 1], [1, 1, 1], [3, 1], [2, 2], [2, 1, 1]]
        """

class Partitions_n(Partitions):
    """
    Partitions of the integer `n`.

    TESTS::

        sage: TestSuite( sage.combinat.partition.Partitions_n(0) ).run()                # needs sage.libs.flint
        sage: TestSuite( sage.combinat.partition.Partitions_n(0) ).run()                # needs sage.libs.flint
    """
    n: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: TestSuite(  Partitions(5) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: P = Partitions(5)
            sage: 5 in P
            False
            sage: [2,1] in P
            False
            sage: [2,2,1] in P
            True
            sage: [3,2] in P
            True
            sage: [2,3] in P
            False
        """
    def cardinality(self, algorithm: str = 'flint'):
        """
        Return the number of partitions of the specified size.

        INPUT:

        - ``algorithm`` -- (default: ``'flint'``)

          - ``'flint'`` -- use FLINT (currently the fastest)
          - ``'gap'`` -- use GAP (VERY *slow*)
          - ``'pari'`` -- use PARI. Speed seems the same as GAP until
            `n` is in the thousands, in which case PARI is faster

        It is possible to associate with every partition of the integer `n` a
        conjugacy class of permutations in the symmetric group on `n` points
        and vice versa. Therefore the number of partitions `p_n` is the number
        of conjugacy classes of the symmetric group on `n` points.

        EXAMPLES::

            sage: v = Partitions(5).list(); v
            [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
            sage: len(v)
            7
            sage: Partitions(5).cardinality(algorithm='gap')                            # needs sage.libs.gap
            7

        ::

            sage: # needs sage.libs.flint
            sage: Partitions(3).cardinality()
            3
            sage: number_of_partitions(5, algorithm='flint')
            7
            sage: Partitions(10).cardinality()
            42
            sage: Partitions(40).cardinality()
            37338
            sage: Partitions(100).cardinality()
            190569292

        ::

            sage: # needs sage.libs.pari
            sage: Partitions(3).cardinality(algorithm='pari')
            3
            sage: Partitions(5).cardinality(algorithm='pari')
            7
            sage: Partitions(10).cardinality(algorithm='pari')
            42

        A generating function for `p_n` is given by the reciprocal of
        Euler's function:

        .. MATH::

           \\sum_{n=0}^{\\infty} p_n x^n = \\prod_{k=1}^{\\infty} \\frac{1}{1-x^k}.

        We use Sage to verify that the first several coefficients do
        indeed agree::

            sage: q = PowerSeriesRing(QQ, 'q', default_prec=9).gen()
            sage: prod([(1-q^k)^(-1) for k in range(1,9)])  # partial product of
            1 + q + 2*q^2 + 3*q^3 + 5*q^4 + 7*q^5 + 11*q^6 + 15*q^7 + 22*q^8 + O(q^9)
            sage: [Partitions(k).cardinality() for k in range(2,10)]                    # needs sage.libs.flint
            [2, 3, 5, 7, 11, 15, 22, 30]

        Another consistency test for ``n`` up to 500::

            sage: len([n for n in [1..500]                                              # needs sage.libs.flint sage.libs.pari
            ....:     if Partitions(n).cardinality() != Partitions(n).cardinality(algorithm='pari')])
            0

        For negative inputs, the result is zero (the algorithm is ignored)::

            sage: Partitions(-5).cardinality()
            0

        REFERENCES:

        - :wikipedia:`Partition\\_(number\\_theory)`
        """
    def random_element(self, measure: str = 'uniform'):
        """
        Return a random partitions of `n` for the specified measure.

        INPUT:

        - ``measure`` -- ``'uniform'`` or ``'Plancherel'``
          (default: ``'uniform'``)

        .. SEEALSO::

            - :meth:`random_element_uniform`
            - :meth:`random_element_plancherel`

        EXAMPLES::

            sage: Partitions(5).random_element()  # random                              # needs sage.libs.flint
            [2, 1, 1, 1]
            sage: Partitions(5).random_element(measure='Plancherel')  # random          # needs sage.libs.flint
            [2, 1, 1, 1]
        """
    def random_element_uniform(self):
        """
        Return a random partition of `n` with uniform probability.

        EXAMPLES::

            sage: Partitions(5).random_element_uniform()  # random                      # needs sage.libs.flint
            [2, 1, 1, 1]
            sage: Partitions(20).random_element_uniform()  # random                     # needs sage.libs.flint
            [9, 3, 3, 2, 2, 1]

        TESTS::

            sage: all(Part.random_element_uniform() in Part                             # needs sage.libs.flint
            ....:     for Part in map(Partitions, range(10)))
            True

        Check that :issue:`18752` is fixed::

            sage: P = Partitions(5)
            sage: la = P.random_element_uniform()                                       # needs sage.libs.flint
            sage: la.parent() is P                                                      # needs sage.libs.flint
            True

        ALGORITHM:

        - It is a python Implementation of RANDPAR, see [NW1978]_.  The
          complexity is unknown, there may be better algorithms.

           .. TODO::

               Check in Knuth AOCP4.

        - There is also certainly a lot of room for optimizations, see
          comments in the code.

        AUTHOR:

        - Florent Hivert (2009-11-23)
        """
    def random_element_plancherel(self):
        """
        Return a random partition of `n` (for the Plancherel measure).

        This probability distribution comes from the uniform distribution
        on permutations via the Robinson-Schensted correspondence.

        See :wikipedia:`Plancherel\\_measure`
        and :meth:`Partition.plancherel_measure`.

        EXAMPLES::

            sage: Partitions(5).random_element_plancherel()   # random
            [2, 1, 1, 1]
            sage: Partitions(20).random_element_plancherel()  # random
            [9, 3, 3, 2, 2, 1]

        TESTS::

            sage: all(Part.random_element_plancherel() in Part
            ....:     for Part in map(Partitions, range(10)))
            True

        Check that :issue:`18752` is fixed::

            sage: P = Partitions(5)
            sage: la = P.random_element_plancherel()
            sage: la.parent() is P
            True

        ALGORITHM:

        - insert by Robinson-Schensted a uniform random permutations of n and
          returns the shape of the resulting tableau. The complexity is
          `O(n\\ln(n))` which is likely optimal. However, the implementation
          could be optimized.

        AUTHOR:

        - Florent Hivert (2009-11-23)
        """
    def first(self):
        """
        Return the lexicographically first partition of a positive integer
        `n`. This is the partition ``[n]``.

        EXAMPLES::

            sage: Partitions(4).first()
            [4]
        """
    def next(self, p):
        """
        Return the lexicographically next partition after the partition ``p``.

        EXAMPLES::

            sage: Partitions(4).next([4])
            [3, 1]
            sage: Partitions(4).next([1,1,1,1]) is None
            True
        """
    def prev(self, p):
        """
        Return the lexicographically previous partition before partition ``p``.

        EXAMPLES::

            sage: Partitions(4).prev([3, 1])
            [4]
            sage: Partitions(4).prev([4]) is None
            True
        """
    def last(self):
        """
        Return the lexicographically last partition of the positive
        integer `n`. This is the all-ones partition.

        EXAMPLES::

            sage: Partitions(4).last()
            [1, 1, 1, 1]
        """
    def __iter__(self):
        """
        An iterator for the partitions of `n`.

        EXAMPLES::

            sage: [x for x in Partitions(4)]
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

        TESTS::

            sage: all(isinstance(i, Integer) for p in Partitions(4) for i in p)
            True
        """
    def subset(self, **kwargs):
        """
        Return a subset of ``self`` with the additional optional arguments.

        EXAMPLES::

            sage: P = Partitions(5); P
            Partitions of the integer 5
            sage: P.subset(starting=[3,1])
            Partitions of the integer 5 starting with [3, 1]
        """

class Partitions_nk(Partitions):
    """
    Partitions of the integer `n` of length equal to `k`.

    TESTS::

        sage: TestSuite( sage.combinat.partition.Partitions_nk(0,0) ).run()
        sage: TestSuite( sage.combinat.partition.Partitions_nk(0,0) ).run()
    """
    n: Incomplete
    k: Incomplete
    def __init__(self, n, k) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: TestSuite(  Partitions(5, length=2) ).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: P = Partitions(5, length=2)
            sage: [2,1] in P
            False
            sage: [2,2,1] in P
            False
            sage: [3,2] in P
            True
            sage: [2,3] in P
            False
            sage: [4,1] in P
            True
            sage: [1,1,1,1,1] in P
            False
            sage: [5] in P
            False
            sage: [4,1,0] in P
            True
            sage: [] in Partitions(0, length=0)
            True
            sage: [0] in Partitions(0, length=0)
            True
            sage: [] in Partitions(0, length=1)
            False
        """
    def __iter__(self):
        """
        An iterator for all partitions of `n` of length `k`.

        EXAMPLES::

            sage: p = Partitions(9, length=3)
            sage: it = p.__iter__()
            sage: list(it)
            [[7, 1, 1], [6, 2, 1], [5, 3, 1], [5, 2, 2], [4, 4, 1], [4, 3, 2], [3, 3, 3]]

            sage: p = Partitions(9, length=10)
            sage: list(p.__iter__())
            []

            sage: p = Partitions(0, length=0)
            sage: list(p.__iter__())
            [[]]

            sage: from sage.combinat.partition import number_of_partitions_length
            sage: all( len(Partitions(n, length=k).list())                              # needs sage.libs.flint
            ....:      == number_of_partitions_length(n, k)
            ....:      for n in range(9) for k in range(n+2) )
            True

        TESTS::

            sage: partitions = Partitions(9, length=3)
            sage: all(isinstance(i, Integer) for p in partitions for i in p)
            True
        """
    def cardinality(self, algorithm: str = 'hybrid'):
        """
        Return the number of partitions of the specified size with the
        specified length.

        INPUT:

        - ``algorithm`` -- (default: ``'hybrid'``) the algorithm to compute
          the cardinality and can be one of the following:

          * ``'hybrid'`` -- use a hybrid algorithm which uses heuristics to
            reduce the complexity
          * ``'gap'`` -- use GAP

        EXAMPLES::

            sage: v = Partitions(5, length=2).list(); v
            [[4, 1], [3, 2]]
            sage: len(v)
            2
            sage: Partitions(5, length=2).cardinality()
            2

        More generally, the number of partitions of `n` of length `2`
        is `\\left\\lfloor \\frac{n}{2} \\right\\rfloor`::

            sage: all( Partitions(n, length=2).cardinality()
            ....:      == n // 2 for n in range(10) )
            True

        The number of partitions of `n` of length `1` is `1` for `n`
        positive::

            sage: all( Partitions(n, length=1).cardinality() == 1
            ....:      for n in range(1, 10) )
            True

        Further examples::

            sage: # needs sage.libs.flint
            sage: Partitions(5, length=3).cardinality()
            2
            sage: Partitions(6, length=3).cardinality()
            3
            sage: Partitions(8, length=4).cardinality()
            5
            sage: Partitions(8, length=5).cardinality()
            3
            sage: Partitions(15, length=6).cardinality()
            26
            sage: Partitions(0, length=0).cardinality()
            1
            sage: Partitions(0, length=1).cardinality()
            0
            sage: Partitions(1, length=0).cardinality()
            0
            sage: Partitions(1, length=4).cardinality()
            0

        TESTS:

        We check the hybrid approach gives the same results as GAP::

            sage: N = [0, 1, 2, 3, 5, 10, 20, 500, 850]
            sage: K = [0, 1, 2, 3, 5, 10, 11, 20, 21, 250, 499, 500]
            sage: all(Partitions(n, length=k).cardinality()                             # needs sage.libs.flint
            ....:       == Partitions(n,length=k).cardinality('gap')
            ....:     for n in N for k in K)
            True
            sage: P = Partitions(4562, length=2800)
            sage: P.cardinality() == P.cardinality('gap')                               # needs sage.libs.flint
            True
        """
    def subset(self, **kwargs):
        """
        Return a subset of ``self`` with the additional optional arguments.

        EXAMPLES::

            sage: P = Partitions(5, length=2); P
            Partitions of the integer 5 of length 2
            sage: P.subset(max_part=3)
            Partitions of 5 having length 2 and whose parts are at most 3
        """

class Partitions_parts_in(Partitions):
    """
    Partitions of `n` with parts in a given set `S`.

    This is invoked indirectly when calling
    ``Partitions(n, parts_in=parts)``, where ``parts`` is a list of
    pairwise distinct integers.

    TESTS::

        sage: TestSuite( sage.combinat.partition.Partitions_parts_in(6, parts=[2,1]) ).run()        # needs sage.libs.gap
    """
    @staticmethod
    def __classcall_private__(cls, n, parts):
        """
        Normalize the input to ensure a unique representation.

        TESTS::

            sage: P = Partitions(4, parts_in=[2,1])
            sage: P2 = Partitions(4, parts_in=(1,2))
            sage: P is P2
            True

        Ensure that :issue:`38640` is fixed::

            sage: list(Partitions(4,parts_in=vector(QQ,[2,4])))
            [[4], [2, 2]]
            sage: list(Partitions(4,parts_in=vector(QQ,[2,1/4])))
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer
            sage: list(Partitions(4,parts_in=vector(ZZ,[2,4])))
            [[4], [2, 2]]
        """
    n: Incomplete
    parts: Incomplete
    def __init__(self, n, parts) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: TestSuite(Partitions(5, parts_in=[1,2,3])).run()                      # needs sage.libs.gap
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import Partitions_parts_in
            sage: P = Partitions_parts_in(5, [1,2])
            sage: 5 in P
            False
            sage: [2,1,1,1] in P
            True
            sage: [4,1] in P
            False
            sage: [2,1,1,1,0] in P
            True
        """
    def cardinality(self):
        """
        Return the number of partitions with parts in ``self``. Wraps GAP's
        ``NrRestrictedPartitions``.

        EXAMPLES::

            sage: Partitions(15, parts_in=[2,3,7]).cardinality()                        # needs sage.libs.gap
            5

        If you can use all parts 1 through `n`, we'd better get `p(n)`::

            sage: (Partitions(20, parts_in=[1..20]).cardinality()                       # needs sage.libs.gap
            ....:   == Partitions(20).cardinality())
            True

        TESTS:

        Let's check the consistency of GAP's function and our own
        algorithm that actually generates the partitions::

            sage: # needs sage.libs.gap
            sage: ps = Partitions(15, parts_in=[1,2,3])
            sage: ps.cardinality() == len(ps.list())
            True
            sage: ps = Partitions(15, parts_in=[])
            sage: ps.cardinality() == len(ps.list())
            True
            sage: ps = Partitions(3000, parts_in=[50,100,500,1000])
            sage: ps.cardinality() == len(ps.list())
            True
            sage: ps = Partitions(10, parts_in=[3,6,9])
            sage: ps.cardinality() == len(ps.list())
            True
            sage: ps = Partitions(0, parts_in=[1,2])
            sage: ps.cardinality() == len(ps.list())
            True
        """
    def first(self):
        """
        Return the lexicographically first partition of a positive
        integer `n` with the specified parts, or ``None`` if no such
        partition exists.

        EXAMPLES::

            sage: Partitions(9, parts_in=[3,4]).first()
            [3, 3, 3]
            sage: Partitions(6, parts_in=[1..6]).first()
            [6]
            sage: Partitions(30, parts_in=[4,7,8,10,11]).first()
            [11, 11, 8]
        """
    def last(self):
        """
        Return the lexicographically last partition of the positive
        integer `n` with the specified parts, or ``None`` if no such
        partition exists.

        EXAMPLES::

            sage: Partitions(15, parts_in=[2,3]).last()
            [3, 2, 2, 2, 2, 2, 2]
            sage: Partitions(30, parts_in=[4,7,8,10,11]).last()
            [7, 7, 4, 4, 4, 4]
            sage: Partitions(10, parts_in=[3,6]).last() is None
            True
            sage: Partitions(50, parts_in=[11,12,13]).last()
            [13, 13, 12, 12]
            sage: Partitions(30, parts_in=[4,7,8,10,11]).last()
            [7, 7, 4, 4, 4, 4]

        TESTS::

            sage: Partitions(6, parts_in=[1..6]).last()
            [1, 1, 1, 1, 1, 1]
            sage: Partitions(0, parts_in=[]).last()
            []
            sage: Partitions(50, parts_in=[11,12]).last() is None
            True
        """
    def __iter__(self):
        """
        An iterator through the partitions of `n` with all parts belonging
        to a particular set.

        EXAMPLES::

            sage: [x for x in Partitions(5, parts_in=[1,2,3])]
            [[3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        """

class Partitions_starting(Partitions):
    """
    All partitions with a given start.
    """
    @staticmethod
    def __classcall_private__(cls, n, starting_partition):
        """
        Normalize the input to ensure a unique representation.

        TESTS::

            sage: P = Partitions(4, starting=[2,1])
            sage: P2 = Partitions(4, starting=[2,1])
            sage: P is P2
            True
        """
    n: Incomplete
    def __init__(self, n, starting_partition) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Partitions(3, starting=[2,1])
            Partitions of the integer 3 starting with [2, 1]
            sage: Partitions(3, starting=[2,1]).list()
            [[2, 1], [1, 1, 1]]

            sage: Partitions(7, starting=[2,2,1]).list()
            [[2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]

            sage: Partitions(7, starting=[3,2]).list()
            [[3, 1, 1, 1, 1],
             [2, 2, 2, 1],
             [2, 2, 1, 1, 1],
             [2, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]

            sage: Partitions(4, starting=[3,2]).list()
            [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

            sage: Partitions(3, starting=[1,1]).list()
            []

        TESTS::

            sage: p = Partitions(3, starting=[2,1])
            sage: TestSuite(p).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: p = Partitions(3, starting=[2,1])
            sage: [1,1] in p
            False
            sage: [2,1] in p
            True
            sage: [1,1,1] in p
            True
            sage: [3] in p
            False

        TESTS::

            sage: from sage.combinat.partition import Partitions_starting
            sage: [2,1,0] in Partitions_starting(3, [2, 1])
            True
        """
    def first(self):
        """
        Return the first partition in ``self``.

        EXAMPLES::

            sage: Partitions(3, starting=[2,1]).first()
            [2, 1]
            sage: Partitions(3, starting=[1,1,1]).first()
            [1, 1, 1]
            sage: Partitions(3, starting=[1,1]).first()
            False
            sage: Partitions(3, starting=[3,1]).first()
            [3]
            sage: Partitions(3, starting=[2,2]).first()
            [2, 1]
        """
    def next(self, part):
        """
        Return the next partition after ``part`` in ``self``.

        EXAMPLES::

            sage: Partitions(3, starting=[2,1]).next(Partition([2,1]))
            [1, 1, 1]
        """

class Partitions_ending(Partitions):
    """
    All partitions with a given ending.
    """
    @staticmethod
    def __classcall_private__(cls, n, ending_partition):
        """
        Normalize the input to ensure a unique representation.

        TESTS::

            sage: P = Partitions(4)
            sage: P2 = Partitions(4)
            sage: P is P2
            True
        """
    n: Incomplete
    def __init__(self, n, ending_partition) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Partitions(4, ending=[1,1,1,1]).list()
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
            sage: Partitions(4, ending=[2,2]).list()
            [[4], [3, 1], [2, 2]]
            sage: Partitions(4, ending=[4]).list()
            [[4]]
            sage: Partitions(4, ending=[5]).list()
            []

        TESTS::

            sage: p = Partitions(4, ending=[1,1,1,1])
            sage: TestSuite(p).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: p = Partitions(4, ending=[2,2])
            sage: [4] in p
            True
            sage: [2,1,1] in p
            False
            sage: [2,1] in p
            False

        TESTS::

            sage: from sage.combinat.partition import Partitions_ending
            sage: [4,0] in Partitions_ending(4, [2, 2])
            True
        """
    def first(self):
        """
        Return the first partition in ``self``.

        EXAMPLES::

            sage: Partitions(4, ending=[1,1,1,1]).first()
            [4]
            sage: Partitions(4, ending=[5]).first() is None
            True
        """
    def next(self, part):
        """
        Return the next partition after ``part`` in ``self``.

        EXAMPLES::
            sage: Partitions(4, ending=[1,1,1,1,1]).next(Partition([4]))
            [3, 1]
            sage: Partitions(4, ending=[3,2]).next(Partition([3,1])) is None
            True
            sage: Partitions(4, ending=[1,1,1,1]).next(Partition([4]))
            [3, 1]
            sage: Partitions(4, ending=[1,1,1,1]).next(Partition([1,1,1,1])) is None
            True
            sage: Partitions(4, ending=[3]).next(Partition([3,1])) is None
            True
        """

class PartitionsInBox(Partitions):
    """
    All partitions which fit in an `h \\times w` box.

    EXAMPLES::

        sage: PartitionsInBox(2, 2)
        Integer partitions which fit in a 2 x 2 box
        sage: PartitionsInBox(2, 2).list()
        [[], [1], [1, 1], [2], [2, 1], [2, 2]]

        sage: Partitions(max_part=2, max_length=3)
        Integer partitions which fit in a 3 x 2 box
    """
    h: Incomplete
    w: Incomplete
    def __init__(self, h, w) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: p = PartitionsInBox(2,2)
            sage: TestSuite(p).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: [] in PartitionsInBox(2,2)
            True
            sage: [2,1] in PartitionsInBox(2,2)
            True
            sage: [3,1] in PartitionsInBox(2,2)
            False
            sage: [2,1,1] in PartitionsInBox(2,2)
            False
            sage: [3,1] in PartitionsInBox(3, 2)
            False
            sage: [3,1] in PartitionsInBox(2, 3)
            True
            sage: [0] in PartitionsInBox(2,2)
            True
            sage: [3,1,0] in PartitionsInBox(2, 3)
            True
        """
    def list(self):
        """
        Return a list of all the partitions inside a box of height `h` and
        width `w`.

        EXAMPLES::

            sage: PartitionsInBox(2,2).list()
            [[], [1], [1, 1], [2], [2, 1], [2, 2]]
            sage: PartitionsInBox(2,3).list()
            [[], [1], [1, 1], [2], [2, 1], [2, 2], [3], [3, 1], [3, 2], [3, 3]]

        TESTS:

        Check :issue:`10890`::

            sage: type(PartitionsInBox(0,0)[0])
            <class 'sage.combinat.partition.PartitionsInBox_with_category.element_class'>
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: PartitionsInBox(2, 3).cardinality()
            10

        TESTS:

        Check the corner case::

            sage: PartitionsInBox(0, 0).cardinality()
            1

            sage: PartitionsInBox(0, 1).cardinality()
            1

            sage: all(PartitionsInBox(a, b).cardinality() ==
            ....:     len(PartitionsInBox(a, b).list())
            ....:     for a in range(6) for b in range(6))
            True
        """

class Partitions_constraints(IntegerListsLex):
    """
    For unpickling old constrained ``Partitions_constraints`` objects created
    with sage <= 3.4.1. See :class:`Partitions`.
    """

class Partitions_with_constraints(IntegerListsLex):
    """
    Partitions which satisfy a set of constraints.

    EXAMPLES::

        sage: P = Partitions(6, inner=[1,1], max_slope=-1)
        sage: list(P)
        [[5, 1], [4, 2], [3, 2, 1]]

    TESTS::

        sage: P = Partitions(6, min_part=2, max_slope=-1)
        sage: TestSuite(P).run()

    Test that :issue:`15525` is fixed::

        sage: loads(dumps(P)) == P
        True
    """
    Element = Partition
    options = Partitions.options
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: P = Partitions(4, max_slope=-2)
            sage: [3,1] in P
            True
            sage: [3,1,0] in P
            True
            sage: [2,2] in P
            False
            sage: [3,1,None] in P
            False

            sage: [1,3] in Partitions(4, min_slope=-1)
            False
        """

class RegularPartitions(Partitions):
    """
    Base class for `\\ell`-regular partitions.

    Let `\\ell` be a positive integer. A partition `\\lambda` is
    `\\ell`-*regular* if `m_i < \\ell` for all `i`, where `m_i` is the
    multiplicity of `i` in `\\lambda`.

    .. NOTE::

        This is conjugate to the notion of `\\ell`-*restricted* partitions,
        where the difference between any two consecutive
        parts is `< \\ell`.

    INPUT:

    - ``ell`` -- the positive integer `\\ell`
    - ``is_infinite`` -- boolean; if the subset of `\\ell`-regular
      partitions is infinite
    """
    def __init__(self, ell, is_infinite: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=2)
            sage: TestSuite(P).run()
        """
    def ell(self):
        """
        Return the value `\\ell`.

        EXAMPLES::

            sage: P = Partitions(regular=2)
            sage: P.ell()
            2
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RegularPartitions
            sage: P = RegularPartitions(3)
            sage: [5] in P
            True
            sage: [] in P
            True
            sage: [3, 3, 2, 2] in P
            True
            sage: [3, 3, 3, 1] in P
            False
            sage: [4, 0, 0, 0, 0, 0] in P
            True
            sage: Partition([4,2,2,1]) in P
            True
            sage: Partition([4,2,2,2]) in P
            False
            sage: Partition([10,1]) in P
            True
        """

class RegularPartitions_all(RegularPartitions):
    """
    The class of all `\\ell`-regular partitions.

    INPUT:

    - ``ell`` -- the positive integer `\\ell`

    .. SEEALSO::

        :class:`~sage.combinat.partition.RegularPartitions`
    """
    def __init__(self, ell) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=4)
            sage: TestSuite(P).run()

        1-regular partitions::

            sage: P = Partitions(regular=1)
            sage: P in FiniteEnumeratedSets()
            True
            sage: TestSuite(P).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=3)
            sage: it = P.__iter__()
            sage: [next(it) for x in range(10)]
            [[], [1], [2], [1, 1], [3], [2, 1], [4], [3, 1], [2, 2], [2, 1, 1]]

        Check that 1-regular partitions works (:issue:`20584`)::

            sage: P = Partitions(regular=1)
            sage: list(P)
            [[]]
        """

class RegularPartitions_truncated(RegularPartitions):
    """
    The class of `\\ell`-regular partitions with max length `k`.

    INPUT:

    - ``ell`` -- the integer `\\ell`
    - ``max_len`` -- integer; the maximum length

    .. SEEALSO::

        :class:`~sage.combinat.partition.RegularPartitions`
    """
    def __init__(self, ell, max_len) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=4, max_length=3)
            sage: TestSuite(P).run()
        """
    def max_length(self):
        """
        Return the maximum length of the partitions of ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=4, max_length=3)
            sage: P.max_length()
            3
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RegularPartitions_truncated
            sage: P = RegularPartitions_truncated(4, 3)
            sage: 3 in P
            False
            sage: [3, 3, 3] in P
            True
            sage: [] in P
            True
            sage: [4, 2, 1, 1] in P
            False
            sage: [0, 0, 0, 0] in P
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=3, max_length=2)
            sage: it = P.__iter__()
            sage: [next(it) for x in range(10)]
            [[], [1], [2], [1, 1], [3], [2, 1], [4], [3, 1], [2, 2], [5]]

        Check that 1-regular partitions works (:issue:`20584`)::

            sage: P = Partitions(regular=1, max_length=2)
            sage: list(P)
            [[]]
        """

class RegularPartitions_bounded(RegularPartitions):
    """
    The class of `\\ell`-regular `k`-bounded partitions.

    INPUT:

    - ``ell`` -- the integer `\\ell`
    - ``k`` -- integer; the value `k`

    .. SEEALSO::

        :class:`~sage.combinat.partition.RegularPartitions`
    """
    k: Incomplete
    def __init__(self, ell, k) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=4, max_part=3)
            sage: TestSuite(P).run()

        1-regular partitions::

            sage: P = Partitions(regular=1, max_part=3)
            sage: P in FiniteEnumeratedSets()
            True
            sage: TestSuite(P).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RegularPartitions_bounded
            sage: P = RegularPartitions_bounded(4, 3)
            sage: 0 in P
            False
            sage: [3, 3, 3] in P
            True
            sage: [] in P
            True
            sage: [4, 2, 1] in P
            False
            sage: [0, 0, 0, 0, 0] in P
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(regular=2, max_part=3)
            sage: list(P)
            [[3, 2, 1], [3, 2], [3, 1], [3], [2, 1], [2], [1], []]

        Check that 1-regular partitions works (:issue:`20584`)::

            sage: P = Partitions(regular=1, max_part=3)
            sage: list(P)
            [[]]
        """

class RegularPartitions_n(RegularPartitions, Partitions_n):
    """
    The class of `\\ell`-regular partitions of `n`.

    INPUT:

    - ``n`` -- the integer `n` to partition
    - ``ell`` -- the integer `\\ell`

    .. SEEALSO::

        :class:`~sage.combinat.partition.RegularPartitions`
    """
    def __init__(self, n, ell) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(5, regular=3)
            sage: TestSuite(P).run()

        1-regular partitions::

            sage: P = Partitions(5, regular=1)
            sage: TestSuite(P).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RegularPartitions_n
            sage: P = RegularPartitions_n(5, 3)
            sage: [3, 1, 1] in P
            True
            sage: [3, 2, 1] in P
            False
            sage: [5, 0, 0, 0, 0] in P
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(5, regular=3)
            sage: list(P)
            [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: P = Partitions(5, regular=3)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            5
            sage: P = Partitions(5, regular=6)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            7
            sage: P.cardinality() == Partitions(5).cardinality()                        # needs sage.libs.flint
            True

        TESTS:

        Check the corner case::

            sage: P = Partitions(0, regular=3)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            1

        Check for 1-regular partitions::

            sage: P = Partitions(0, regular=1)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            1
            sage: P = Partitions(5, regular=1)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            0
        """

class OrderedPartitions(Partitions):
    """
    The class of ordered partitions of `n`. If `k` is specified, then this
    contains only the ordered partitions of length `k`.

    An *ordered partition* of a nonnegative integer `n` means a list of
    positive integers whose sum is `n`. This is the same as a composition
    of `n`.

    .. NOTE::

       It is recommended that you use :meth:`Compositions` instead as
       :meth:`OrderedPartitions` wraps GAP.

    EXAMPLES::

        sage: OrderedPartitions(3)
        Ordered partitions of 3
        sage: OrderedPartitions(3).list()                                               # needs sage.libs.gap
        [[3], [2, 1], [1, 2], [1, 1, 1]]
        sage: OrderedPartitions(3,2)
        Ordered partitions of 3 of length 2
        sage: OrderedPartitions(3,2).list()                                             # needs sage.libs.gap
        [[2, 1], [1, 2]]

        sage: OrderedPartitions(10, k=2).list()                                         # needs sage.libs.gap
        [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9]]
        sage: OrderedPartitions(4).list()                                               # needs sage.libs.gap
        [[4], [3, 1], [2, 2], [2, 1, 1], [1, 3], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
    """
    @staticmethod
    def __classcall_private__(cls, n, k=None):
        """
        Normalize the input to ensure a unique representation.

        TESTS::

            sage: P = OrderedPartitions(3,2)
            sage: P2 = OrderedPartitions(3,2)
            sage: P is P2
            True
        """
    n: Incomplete
    k: Incomplete
    def __init__(self, n, k) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: o = OrderedPartitions(4,2)

        TESTS::

            sage: TestSuite( OrderedPartitions(5,3) ).run()                             # needs sage.libs.gap
        """
    def __contains__(self, x) -> bool:
        """
        Check to see if ``x`` is an element of ``self``.

        EXAMPLES::

            sage: o = OrderedPartitions(4,2)
            sage: [2,1] in o
            False
            sage: [2,2] in o
            True
            sage: [1,2,1] in o
            False
        """
    def list(self):
        """
        Return a list of partitions in ``self``.

        EXAMPLES::

            sage: OrderedPartitions(3).list()                                           # needs sage.libs.gap
            [[3], [2, 1], [1, 2], [1, 1, 1]]
            sage: OrderedPartitions(3,2).list()                                         # needs sage.libs.gap
            [[2, 1], [1, 2]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: OrderedPartitions(3).cardinality()
            4
            sage: OrderedPartitions(3,2).cardinality()
            2
            sage: OrderedPartitions(10,2).cardinality()
            9
            sage: OrderedPartitions(15).cardinality()
            16384
        """

class Partitions_length_and_parts_constrained(Partitions):
    """
    The class of all integer partitions having parts and length in a
    given range.

    This class is strictly more general than
    :class:`PartitionsGreatestLE`, except that we insist that the
    size of the partition is positive and that neither the
    constraints on the parts nor on the length are contradictory.

    INPUT:

    - ``n`` -- the size of the partition, positive
    - ``min_length`` -- the lower bound on the number of parts, between 1 and ``n``
    - ``max_length`` -- the upper bound on the number of parts, between ``min_length`` and ``n``
    - ``min_part`` -- the bound on the smallest part, between 1 and ``n``
    - ``max_part`` -- the bound on the largest part, between ``min_part`` and ``n``

    EXAMPLES::

        sage: from sage.combinat.partition import Partitions_length_and_parts_constrained
        sage: Partitions_length_and_parts_constrained(10, 1, 10, 2, 5)
        Partitions of 10 whose parts are between 2 and 5
        sage: list(Partitions_length_and_parts_constrained(9, 3, 4, 2, 4))
        [[4, 3, 2], [3, 3, 3], [3, 2, 2, 2]]

        sage: [4,3,2,1] in Partitions_length_and_parts_constrained(10, 1, 10, 2, 10)
        False
        sage: [2,2,2,2,2] in Partitions_length_and_parts_constrained(10, 1, 10, 2, 10)
        True

    .. WARNING::

        If ``min_length`` and ``min_part`` equal 1 and ``max_length``
        and ``max_part`` equal ``n``, this class contains the same
        partitions as :class:`~sage.combinat.partition.Partitions`,
        but is different from that class.

    ::

        sage: Partitions_length_and_parts_constrained(9, 1, 9, 1, 9)
        Partitions of 9
        sage: Partitions_length_and_parts_constrained(9, 1, 9, 1, 9) == Partitions(9)
        False
    """
    def __init__(self, n, min_length, max_length, min_part, max_part) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.partition import Partitions_length_and_parts_constrained
            sage: p = Partitions_length_and_parts_constrained(10, 2, 5, 3, 4)
            sage: TestSuite(p).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is contained in ``self``.

        TESTS::

            sage: from sage.combinat.partition import Partitions_length_and_parts_constrained
            sage: P = Partitions_length_and_parts_constrained(10, 2, 4, 2, 5)
            sage: 1 in P
            False
            sage: Partition([]) in P
            False
            sage: Partition([3]) in P
            False
            sage: Partition([5, 3, 2]) in P
            True
            sage: [5, 3, 2, 0, 0] in P
            True
        """
    def __iter__(self):
        """
        Iterator over the set of partitions in ``self``.

        EXAMPLES::

            sage: list(Partitions(9, min_part=2, max_part=4, min_length=3, max_length=4))
            [[4, 3, 2], [3, 3, 3], [3, 2, 2, 2]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: from sage.combinat.partition import Partitions_length_and_parts_constrained
            sage: list(Partitions_length_and_parts_constrained(9, 1, 2, 3, 9))
            [[9], [6, 3], [5, 4]]
            sage: Partitions_length_and_parts_constrained(9, 1, 2, 3, 9).cardinality()
            3

        TESTS::

            sage: from itertools import product
            sage: P = Partitions
            sage: all(P(n, min_length=k, max_length=m, min_part=a, max_part=b).cardinality()
            ....:     == len(list(P(n, min_length=k, max_length=m, min_part=a, max_part=b)))
            ....:     for n, k, m, a, b in product(range(-1, 5), repeat=5))
            True
        """

class PartitionsGreatestLE(UniqueRepresentation, IntegerListsLex):
    '''
    The class of all (unordered) "restricted" partitions of the
    integer `n` having parts less than or equal to the integer `k`.

    EXAMPLES::

        sage: PartitionsGreatestLE(10, 2)
        Partitions of 10 having parts less than or equal to 2
        sage: PartitionsGreatestLE(10, 2).list()
        [[2, 2, 2, 2, 2],
         [2, 2, 2, 2, 1, 1],
         [2, 2, 2, 1, 1, 1, 1],
         [2, 2, 1, 1, 1, 1, 1, 1],
         [2, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        sage: [4,3,2,1] in PartitionsGreatestLE(10, 2)
        False
        sage: [2,2,2,2,2] in PartitionsGreatestLE(10, 2)
        True
        sage: PartitionsGreatestLE(10, 2).first().parent()
        Partitions...
    '''
    n: Incomplete
    k: Incomplete
    def __init__(self, n, k) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: p = PartitionsGreatestLE(10, 2)
            sage: p.n, p.k
            (10, 2)
            sage: TestSuite(p).run()
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: PartitionsGreatestLE(9, 5).cardinality()                              # needs sage.libs.gap
            23

        TESTS::

            sage: all(PartitionsGreatestLE(n, a).cardinality() ==
            ....:     len(list(PartitionsGreatestLE(n, a)))
            ....:     for n in range(20) for a in range(6))
            True
        """
    Element = Partition
    options = Partitions.options

class PartitionsGreatestEQ(UniqueRepresentation, IntegerListsLex):
    '''
    The class of all (unordered) "restricted" partitions of the integer `n`
    having all its greatest parts equal to the integer `k`.

    EXAMPLES::

        sage: PartitionsGreatestEQ(10, 2)
        Partitions of 10 having greatest part equal to 2
        sage: PartitionsGreatestEQ(10, 2).list()
        [[2, 2, 2, 2, 2],
         [2, 2, 2, 2, 1, 1],
         [2, 2, 2, 1, 1, 1, 1],
         [2, 2, 1, 1, 1, 1, 1, 1],
         [2, 1, 1, 1, 1, 1, 1, 1, 1]]

        sage: [4,3,2,1] in PartitionsGreatestEQ(10, 2)
        False
        sage: [2,2,2,2,2] in PartitionsGreatestEQ(10, 2)
        True

    The empty partition has no maximal part, but it is contained in
    the set of partitions with any specified maximal part::

        sage: PartitionsGreatestEQ(0, 2).list()
        [[]]

    TESTS::

        sage: [1]*10 in PartitionsGreatestEQ(10, 2)
        False

        sage: PartitionsGreatestEQ(10, 2).first().parent()
        Partitions...
    '''
    n: Incomplete
    k: Incomplete
    def __init__(self, n, k) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: p = PartitionsGreatestEQ(10, 2)
            sage: p.n, p.k
            (10, 2)
            sage: TestSuite(p).run()
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: PartitionsGreatestEQ(10, 2).cardinality()
            5

        TESTS::

            sage: all(PartitionsGreatestEQ(n, a).cardinality() ==                       # needs sage.libs.flint
            ....:     len(PartitionsGreatestEQ(n, a).list())
            ....:     for n in range(20) for a in range(6))
            True
        """
    Element = Partition
    options = Partitions.options

class RestrictedPartitions_generic(Partitions):
    """
    Base class for `\\ell`-restricted partitions.

    Let `\\ell` be a positive integer. A partition `\\lambda` is
    `\\ell`-*restricted* if `\\lambda_i - \\lambda_{i+1} < \\ell` for all `i`,
    including rows of length 0.

    .. NOTE::

        This is conjugate to the notion of `\\ell`-*regular* partitions,
        where the multiplicity of any parts is at most `\\ell`.

    INPUT:

    - ``ell`` -- the positive integer `\\ell`
    - ``is_infinite`` -- boolean; if the subset of `\\ell`-restricted
      partitions is infinite
    """
    def __init__(self, ell, is_infinite: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(restricted=2)
            sage: TestSuite(P).run()
        """
    def ell(self):
        """
        Return the value `\\ell`.

        EXAMPLES::

            sage: P = Partitions(restricted=2)
            sage: P.ell()
            2
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RestrictedPartitions_generic
            sage: P = RestrictedPartitions_generic(3)
            sage: [5] in P
            False
            sage: [2] in P
            True
            sage: [] in P
            True
            sage: [3, 3, 3, 3, 2, 2] in P
            True
            sage: [3, 3, 3, 1] in P
            True
            sage: [8, 3, 3, 1] in P
            False
            sage: [2, 0, 0, 0, 0, 0] in P
            True
            sage: Partition([4,2,2,1]) in P
            True
            sage: Partition([4,2,2,2]) in P
            True
            sage: Partition([6,6,6,6,4,3,2]) in P
            True
            sage: Partition([7,6,6,2]) in P
            False
            sage: Partition([6,5]) in P
            False
            sage: Partition([10,1]) in P
            False
            sage: Partition([3,3] + [1]*10) in P
            True
        """

class RestrictedPartitions_all(RestrictedPartitions_generic):
    """
    The class of all `\\ell`-restricted partitions.

    INPUT:

    - ``ell`` -- the positive integer `\\ell`

    .. SEEALSO::

        :class:`~sage.combinat.partition.RestrictedPartitions_generic`
    """
    def __init__(self, ell) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(restricted=4)
            sage: TestSuite(P).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(restricted=3)
            sage: it = P.__iter__()
            sage: [next(it) for x in range(10)]
            [[], [1], [2], [1, 1], [2, 1], [1, 1, 1],
             [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
        """

class RestrictedPartitions_n(RestrictedPartitions_generic, Partitions_n):
    """
    The class of `\\ell`-restricted partitions of `n`.

    INPUT:

    - ``n`` -- the integer `n` to partition
    - ``ell`` -- the integer `\\ell`

    .. SEEALSO::

        :class:`~sage.combinat.partition.RestrictedPartitions_generic`
    """
    def __init__(self, n, ell) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = Partitions(5, restricted=3)
            sage: TestSuite(P).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: from sage.combinat.partition import RestrictedPartitions_n
            sage: P = RestrictedPartitions_n(5, 3)
            sage: [3, 1, 1] in P
            True
            sage: [3, 2, 1] in P
            False
            sage: [3, 2, 0, 0, 0] in P
            True
            sage: [5] in P
            False
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: P = Partitions(5, restricted=3)
            sage: list(P)
            [[3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: P = Partitions(5, restricted=3)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            5
            sage: P = Partitions(5, restricted=6)
            sage: P.cardinality()                                                       # needs sage.libs.flint
            7
            sage: P.cardinality() == Partitions(5).cardinality()                        # needs sage.libs.flint
            True
        """

def number_of_partitions(n, algorithm: str = 'default'):
    """
    Return the number of partitions of `n` with, optionally, at most `k`
    parts.

    The options of :meth:`number_of_partitions()` are being deprecated
    :issue:`13072` in favour of :meth:`Partitions_n.cardinality()` so that
    :meth:`number_of_partitions()` can become a stripped down version of
    the fastest algorithm available (currently this is using FLINT).

    INPUT:

    - ``n`` -- integer

    - ``algorithm`` -- (default: ``'default'``)
       [Will be deprecated except in Partition().cardinality() ]

       - ``'default'`` -- if ``k`` is not ``None``, then use Gap (very slow);
          if  ``k`` is ``None``, use FLINT

       - ``'flint'`` -- use FLINT

    EXAMPLES::

        sage: v = Partitions(5).list(); v
        [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        sage: len(v)
        7

    The input must be a nonnegative integer or a :exc:`ValueError` is raised.

    ::

        sage: number_of_partitions(-5)
        Traceback (most recent call last):
        ...
        ValueError: n (=-5) must be a nonnegative integer

    ::

        sage: # needs sage.libs.flint
        sage: number_of_partitions(10)
        42
        sage: number_of_partitions(3)
        3
        sage: number_of_partitions(10)
        42
        sage: number_of_partitions(40)
        37338
        sage: number_of_partitions(100)
        190569292
        sage: number_of_partitions(100000)
        27493510569775696512677516320986352688173429315980054758203125984302147328114964173055050741660736621590157844774296248940493063070200461792764493033510116079342457190155718943509725312466108452006369558934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519

    A generating function for the number of partitions `p_n` is given by the
    reciprocal of Euler's function:

    .. MATH::

        \\sum_{n=0}^{\\infty} p_n x^n = \\prod_{k=1}^{\\infty} \\left(
        \\frac{1}{1-x^k} \\right).

    We use Sage to verify that the first several coefficients do
    instead agree::

        sage: q = PowerSeriesRing(QQ, 'q', default_prec=9).gen()
        sage: prod([(1-q^k)^(-1) for k in range(1,9)])  # partial product of
        1 + q + 2*q^2 + 3*q^3 + 5*q^4 + 7*q^5 + 11*q^6 + 15*q^7 + 22*q^8 + O(q^9)
        sage: [number_of_partitions(k) for k in range(2,10)]                            # needs sage.libs.flint
        [2, 3, 5, 7, 11, 15, 22, 30]

    REFERENCES:

    - :wikipedia:`Partition\\_(number\\_theory)`

    TESTS::

        sage: # needs sage.libs.flint
        sage: n = 500 + randint(0,500)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1500 + randint(0,1500)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 1000000 + randint(0,1000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
        True
        sage: n = 100000000 + randint(0,100000000)
        sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0     # long time (4s on sage.math, 2011)
        True
    """
def number_of_partitions_length(n, k, algorithm: str = 'hybrid'):
    """
    Return the number of partitions of `n` with length `k`.

    This is a wrapper for GAP's ``NrPartitions`` function.

    EXAMPLES::

        sage: # needs sage.libs.gap
        sage: from sage.combinat.partition import number_of_partitions_length
        sage: number_of_partitions_length(5, 2)
        2
        sage: number_of_partitions_length(10, 2)
        5
        sage: number_of_partitions_length(10, 4)
        9
        sage: number_of_partitions_length(10, 0)
        0
        sage: number_of_partitions_length(10, 1)
        1
        sage: number_of_partitions_length(0, 0)
        1
        sage: number_of_partitions_length(0, 1)
        0
    """
@cached_function
def number_of_partitions_max_length_max_part(n, k, b):
    """
    Return the number of partitions of `n` with at most `k`
    parts, all of which are at most `b`.

    EXAMPLES:

    This could also be computed using the `q`-binomial coefficient::

        sage: from sage.combinat.partition import number_of_partitions_max_length_max_part as f
        sage: all(f(n, k, b) == q_binomial(k + b, b)[n] for n in range(5) for k in range(n+1) for b in range(n+1))
        True

    However, although the `q`-binomial coefficient is faster for
    individual invocations, it seems that the caching we use here is
    essential for some computations::

        sage: def A(n):
        ....:     s1 = number_of_partitions(n)
        ....:     s2 = sum(Partitions(m, max_part=l, length=k).cardinality()
        ....:              * Partitions(n-m-l^2, min_length=k+2*l).cardinality()
        ....:              for l in range(1, (n+1).isqrt())
        ....:              for m in range((n-l^2-2*l)*l//(l+1)+1)
        ....:              for k in range(ceil(m/l), min(m, n-m-l^2-2*l)+1))
        ....:     return s1 + s2

        sage: A(100)
        10934714090
    """

cached_number_of_partitions: Incomplete
