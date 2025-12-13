from .combinat import CombinatorialElement as CombinatorialElement
from .integer_lists import IntegerListsLex as IntegerListsLex
from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.additive_monoids import AdditiveMonoids as AdditiveMonoids
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Composition(CombinatorialElement):
    '''
    Integer compositions.

    A composition of a nonnegative integer `n` is a list
    `(i_1, \\ldots, i_k)` of positive integers with total sum `n`.

    EXAMPLES:

    The simplest way to create a composition is by specifying its
    entries as a list, tuple (or other iterable)::

        sage: Composition([3,1,2])
        [3, 1, 2]
        sage: Composition((3,1,2))
        [3, 1, 2]
        sage: Composition(i for i in range(2,5))
        [2, 3, 4]

    You can also create a composition from its code. The *code* of
    a composition `(i_1, i_2, \\ldots, i_k)` of `n` is a list of length `n`
    that consists of a `1` followed by `i_1-1` zeros, then a `1` followed
    by `i_2-1` zeros, and so on.

    ::

        sage: Composition([4,1,2,3,5]).to_code()
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
        sage: Composition(code=_)
        [4, 1, 2, 3, 5]
        sage: Composition([3,1,2,3,5]).to_code()
        [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
        sage: Composition(code=_)
        [3, 1, 2, 3, 5]

    You can also create the composition of `n` corresponding to a subset of
    `\\{1, 2, \\ldots, n-1\\}` under the bijection that maps the composition
    `(i_1, i_2, \\ldots, i_k)` of `n` to the subset
    `\\{i_1, i_1 + i_2, i_1 + i_2 + i_3, \\ldots, i_1 + \\cdots + i_{k-1}\\}`
    (see :meth:`to_subset`)::

        sage: Composition(from_subset=({1, 2, 4}, 5))
        [1, 1, 2, 1]
        sage: Composition([1, 1, 2, 1]).to_subset()
        {1, 2, 4}

    The following notation equivalently specifies the composition from the
    set `\\{i_1 - 1, i_1 + i_2 - 1, i_1 + i_2 + i_3 - 1, \\dots, i_1 + \\cdots
    + i_{k-1} - 1, n-1\\}` or `\\{i_1 - 1, i_1 + i_2 - 1, i_1 + i_2 + i_3
    - 1, \\dots, i_1 + \\cdots + i_{k-1} - 1\\}` and `n`. This provides
    compatibility with Python\'s `0`-indexing.

    ::

        sage: Composition(descents=[1,0,4,8,11])
        [1, 1, 3, 4, 3]
        sage: Composition(descents=[0,1,3,4])
        [1, 1, 2, 1]
        sage: Composition(descents=([0,1,3],5))
        [1, 1, 2, 1]
        sage: Composition(descents=({0,1,3},5))
        [1, 1, 2, 1]

    An integer composition may be regarded as a sequence. Thus it is an
    instance of the Python abstract base class ``Sequence`` allows us to check if objects
    behave "like" sequences based on implemented methods. Note that
    ``collections.abc.Sequence`` is not the same as
    :class:`sage.structure.sequence.Sequence`::

        sage: import collections.abc
        sage: C = Composition([3,2,3])
        sage: isinstance(C, collections.abc.Sequence)
        True
        sage: issubclass(C.__class__, collections.abc.Sequence)
        True

    Typically, instances of ``collections.abc.Sequence`` have a ``.count`` method.
    ``Composition.count`` counts the number of parts of a specified size::

        sage: C.count(3)
        2

    EXAMPLES::

        sage: C = Composition([3,1,2])
        sage: TestSuite(C).run()
    '''
    @staticmethod
    def __classcall_private__(cls, co=None, descents=None, code=None, from_subset=None):
        '''
        This constructs a list from optional arguments and delegates the
        construction of a :class:`Composition` to the ``element_class()`` call
        of the appropriate parent.

        EXAMPLES::

            sage: Composition([3,2,1])
            [3, 2, 1]
            sage: Composition(from_subset=({1, 2, 4}, 5))
            [1, 1, 2, 1]
            sage: Composition(descents=[1,0,4,8,11])
            [1, 1, 3, 4, 3]
            sage: Composition([4,1,2,3,5]).to_code()
            [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
            sage: Composition(code=_)
            [4, 1, 2, 3, 5]

        TESTS:

        Let us check that :issue:`14862` is solved::

            sage: C = Compositions()
            sage: C([3,-1,1])
            Traceback (most recent call last):
            ...
            ValueError: not a composition
            sage: C("strawberry")
            Traceback (most recent call last):
            ...
            ValueError: not a composition
        '''
    def __init__(self, parent, lst) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = Composition([3,1,2])
            sage: TestSuite(C).run()
        """
    def conjugate(self) -> Composition:
        """
        Return the conjugate of the composition ``self``.

        The conjugate of a composition `I` is defined as the
        complement (see :meth:`complement`) of the reverse composition
        (see :meth:`reversed`) of `I`.

        An equivalent definition of the conjugate goes by saying that
        the ribbon shape of the conjugate of a composition `I` is the
        conjugate of the ribbon shape of `I`. (The ribbon shape of a
        composition is returned by :meth:`to_skew_partition`.)

        This implementation uses the algorithm from mupad-combinat.

        EXAMPLES::

            sage: Composition([1, 1, 3, 1, 2, 1, 3]).conjugate()
            [1, 1, 3, 3, 1, 3]

        The ribbon shape of the conjugate of `I` is the conjugate of
        the ribbon shape of `I`::

            sage: all( I.conjugate().to_skew_partition()                                # needs sage.combinat
            ....:      == I.to_skew_partition().conjugate()
            ....:      for I in Compositions(4) )
            True

        TESTS::

            sage: parent(list(Compositions(1))[0].conjugate())
            Compositions of 1
            sage: parent(list(Compositions(0))[0].conjugate())
            Compositions of 0
        """
    def reversed(self) -> Composition:
        """
        Return the reverse composition of ``self``.

        The reverse composition of a composition `(i_1, i_2, \\ldots, i_k)`
        is defined as the composition `(i_k, i_{k-1}, \\ldots, i_1)`.

        EXAMPLES::

            sage: Composition([1, 1, 3, 1, 2, 1, 3]).reversed()
            [3, 1, 2, 1, 3, 1, 1]
        """
    def complement(self) -> Composition:
        """
        Return the complement of the composition ``self``.

        The complement of a composition `I` is defined as follows:

        If `I` is the empty composition, then the complement is the empty
        composition as well. Otherwise, let `S` be the descent set of `I`
        (that is, the subset
        `\\{ i_1, i_1 + i_2, \\ldots, i_1 + i_2 + \\cdots + i_{k-1} \\}`
        of `\\{ 1, 2, \\ldots, |I|-1 \\}`, where `I` is written as
        `(i_1, i_2, \\ldots, i_k)`). Then, the complement of `I` is
        defined as the composition of size `|I|` whose descent set is
        `\\{ 1, 2, \\ldots, |I|-1 \\} \\setminus S`.

        The complement of a composition `I` also is the reverse
        composition (:meth:`reversed`) of the conjugate
        (:meth:`conjugate`) of `I`.

        EXAMPLES::

            sage: Composition([1, 1, 3, 1, 2, 1, 3]).conjugate()
            [1, 1, 3, 3, 1, 3]
            sage: Composition([1, 1, 3, 1, 2, 1, 3]).complement()
            [3, 1, 3, 3, 1, 1]
        """
    def __add__(self, other) -> Composition:
        """
        Return the concatenation of two compositions.

        EXAMPLES::

            sage: Composition([1, 1, 3]) + Composition([4, 1, 2])
            [1, 1, 3, 4, 1, 2]

        TESTS::

            sage: Composition([]) + Composition([]) == Composition([])
            True
        """
    def size(self) -> int:
        """
        Return the size of ``self``, that is the sum of its parts.

        EXAMPLES::

            sage: Composition([7,1,3]).size()
            11
        """
    @staticmethod
    def sum(compositions) -> Composition:
        """
        Return the concatenation of the given compositions.

        INPUT:

        - ``compositions`` -- list (or iterable) of compositions

        EXAMPLES::

            sage: Composition.sum([Composition([1, 1, 3]), Composition([4, 1, 2]), Composition([3,1])])
            [1, 1, 3, 4, 1, 2, 3, 1]

        Any iterable can be provided as input::

            sage: Composition.sum([Composition([i,i]) for i in [4,1,3]])
            [4, 4, 1, 1, 3, 3]

        Empty inputs are handled gracefully::

            sage: Composition.sum([]) == Composition([])
            True
        """
    def near_concatenation(self, other):
        """
        Return the near-concatenation of two nonempty compositions
        ``self`` and ``other``.

        The near-concatenation `I \\odot J` of two nonempty compositions
        `I` and `J` is defined as the composition
        `(i_1, i_2, \\ldots , i_{n-1}, i_n + j_1, j_2, j_3, \\ldots , j_m)`,
        where `(i_1, i_2, \\ldots , i_n) = I` and
        `(j_1, j_2, \\ldots , j_m) = J`.

        This method returns ``None`` if one of the two input
        compositions is empty.

        EXAMPLES::

            sage: Composition([1, 1, 3]).near_concatenation(Composition([4, 1, 2]))
            [1, 1, 7, 1, 2]
            sage: Composition([6]).near_concatenation(Composition([1, 5]))
            [7, 5]
            sage: Composition([1, 5]).near_concatenation(Composition([6]))
            [1, 11]

        TESTS::

            sage: Composition([]).near_concatenation(Composition([]))
            <BLANKLINE>
            sage: Composition([]).near_concatenation(Composition([2, 1]))
            <BLANKLINE>
            sage: Composition([3, 2]).near_concatenation(Composition([]))
            <BLANKLINE>
        """
    def ribbon_decomposition(self, other, check: bool = True):
        '''
        Return a pair describing the ribbon decomposition of a composition
        ``self`` with respect to a composition ``other`` of the same size.

        If `I` and `J` are two compositions of the same nonzero size, then
        the ribbon decomposition of `I` with respect to `J` is defined as
        follows: Write `I` and `J` as `I = (i_1, i_2, \\ldots , i_n)` and
        `J = (j_1, j_2, \\ldots , j_m)`. Then, the equality
        `I = I_1 \\bullet I_2 \\bullet \\ldots \\bullet I_m` holds for a
        unique `m`-tuple `(I_1, I_2, \\ldots , I_m)` of compositions such
        that each `I_k` has size `j_k` and for a unique choice of `m-1`
        signs `\\bullet` each of which is either the concatenation sign
        `\\cdot` or the near-concatenation sign `\\odot` (see
        :meth:`__add__` and :meth:`near_concatenation` for the definitions
        of these two signs). This `m`-tuple and this choice of signs
        together are said to form the ribbon decomposition of `I` with
        respect to `J`. If `I` and `J` are empty, then the same definition
        applies, except that there are `0` rather than `m-1` signs.

        See Section 4.8 of [NCSF1]_.

        INPUT:

        - ``other`` -- composition of same size as ``self``

        - ``check`` -- boolean (default: ``True``); whether to check the input
          compositions for having the same size

        OUTPUT:

        - a pair ``(u, v)``, where ``u`` is a tuple of compositions
          (corresponding to the `m`-tuple `(I_1, I_2, \\ldots , I_m)` in
          the above definition), and ``v`` is a tuple of `0`s and `1`s
          (encoding the choice of signs `\\bullet` in the above definition,
          with a `0` standing for `\\cdot` and a `1` standing for `\\odot`).

        EXAMPLES::

            sage: Composition([3, 1, 1, 3, 1]).ribbon_decomposition([4, 3, 2])
            (([3, 1], [1, 2], [1, 1]), (0, 1))
            sage: Composition([9, 6]).ribbon_decomposition([1, 3, 6, 3, 2])
            (([1], [3], [5, 1], [3], [2]), (1, 1, 1, 1))
            sage: Composition([9, 6]).ribbon_decomposition([1, 3, 5, 1, 3, 2])
            (([1], [3], [5], [1], [3], [2]), (1, 1, 0, 1, 1))
            sage: Composition([1, 1, 1, 1, 1]).ribbon_decomposition([3, 2])
            (([1, 1, 1], [1, 1]), (0,))
            sage: Composition([4, 2]).ribbon_decomposition([6])
            (([4, 2],), ())
            sage: Composition([]).ribbon_decomposition([])
            ((), ())

        Let us check that the defining property
        `I = I_1 \\bullet I_2 \\bullet \\ldots \\bullet I_m` is satisfied::

            sage: def compose_back(u, v):
            ....:     comp = u[0]
            ....:     r = len(v)
            ....:     if len(u) != r + 1:
            ....:         raise ValueError("something is wrong")
            ....:     for i in range(r):
            ....:         if v[i] == 0:
            ....:             comp += u[i + 1]
            ....:         else:
            ....:             comp = comp.near_concatenation(u[i + 1])
            ....:     return comp
            sage: all( all( all( compose_back(*(I.ribbon_decomposition(J))) == I
            ....:                for J in Compositions(n) )
            ....:           for I in Compositions(n) )
            ....:      for n in range(1, 5) )
            True

        TESTS::

            sage: Composition([3, 1, 1, 3, 1]).ribbon_decomposition([4, 3, 1])
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 1, 3, 1] is not the same size as [4, 3, 1]

        AUTHORS:

        - Darij Grinberg (2013-08-29)
        '''
    def join(self, other, check: bool = True) -> Composition:
        """
        Return the join of ``self`` with a composition ``other`` of the
        same size.

        The join of two compositions `I` and `J` of size `n` is the
        coarsest composition of `n` which refines each of `I` and `J`. It
        can be described as the composition whose descent set is the
        union of the descent sets of `I` and `J`. It is also the
        concatenation of `I_1, I_2, \\cdots , I_m`, where
        `I = I_1 \\bullet I_2 \\bullet \\ldots \\bullet I_m` is the ribbon
        decomposition of `I` with respect to `J` (see
        :meth:`ribbon_decomposition`).

        INPUT:

        - ``other`` -- composition of same size as ``self``

        - ``check`` -- boolean (default: ``True``); whether to check the input
          compositions for having the same size

        OUTPUT: the join of the compositions ``self`` and ``other``

        EXAMPLES::

            sage: Composition([3, 1, 1, 3, 1]).join([4, 3, 2])
            [3, 1, 1, 2, 1, 1]
            sage: Composition([9, 6]).join([1, 3, 6, 3, 2])
            [1, 3, 5, 1, 3, 2]
            sage: Composition([9, 6]).join([1, 3, 5, 1, 3, 2])
            [1, 3, 5, 1, 3, 2]
            sage: Composition([1, 1, 1, 1, 1]).join([3, 2])
            [1, 1, 1, 1, 1]
            sage: Composition([4, 2]).join([3, 3])
            [3, 1, 2]
            sage: Composition([]).join([])
            []

        Let us verify on small examples that the join
        of `I` and `J` refines both of `I` and `J`::

            sage: all( all( I.join(J).is_finer(I) and
            ....:           I.join(J).is_finer(J)
            ....:           for J in Compositions(4) )
            ....:      for I in Compositions(4) )
            True

        and is the coarsest composition to do so::

            sage: all( all( all( K.is_finer(I.join(J))
            ....:                for K in I.finer()
            ....:                if K.is_finer(J) )
            ....:           for J in Compositions(3) )
            ....:      for I in Compositions(3) )
            True

        Let us check that the join of `I` and `J` is indeed the
        concatenation of `I_1, I_2, \\cdots , I_m`, where
        `I = I_1 \\bullet I_2 \\bullet \\ldots \\bullet I_m` is the ribbon
        decomposition of `I` with respect to `J`::

            sage: all( all( Composition.sum(I.ribbon_decomposition(J)[0])
            ....:           == I.join(J) for J in Compositions(4) )
            ....:      for I in Compositions(4) )
            True

        Also, the descent set of the join of `I` and `J` is the
        union of the descent sets of `I` and `J`::

            sage: all( all( I.to_subset().union(J.to_subset())
            ....:           == I.join(J).to_subset()
            ....:           for J in Compositions(4) )
            ....:      for I in Compositions(4) )
            True

        TESTS::

            sage: Composition([3, 1, 1, 3, 1]).join([4, 3, 1])
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 1, 3, 1] is not the same size as [4, 3, 1]

        .. SEEALSO::

            :meth:`meet`, :meth:`ribbon_decomposition`

        AUTHORS:

        - Darij Grinberg (2013-09-05)
        """
    sup = join
    def meet(self, other, check: bool = True) -> Composition:
        """
        Return the meet of ``self`` with a composition ``other`` of the
        same size.

        The meet of two compositions `I` and `J` of size `n` is the
        finest composition of `n` which is coarser than each of `I` and
        `J`. It can be described as the composition whose descent set is
        the intersection of the descent sets of `I` and `J`.

        INPUT:

        - ``other`` -- composition of same size as ``self``

        - ``check`` -- boolean (default: ``True``); whether to check the input
          compositions for having the same size

        OUTPUT: the meet of the compositions ``self`` and ``other``

        EXAMPLES::

            sage: Composition([3, 1, 1, 3, 1]).meet([4, 3, 2])
            [4, 5]
            sage: Composition([9, 6]).meet([1, 3, 6, 3, 2])
            [15]
            sage: Composition([9, 6]).meet([1, 3, 5, 1, 3, 2])
            [9, 6]
            sage: Composition([1, 1, 1, 1, 1]).meet([3, 2])
            [3, 2]
            sage: Composition([4, 2]).meet([3, 3])
            [6]
            sage: Composition([]).meet([])
            []
            sage: Composition([1]).meet([1])
            [1]

        Let us verify on small examples that the meet
        of `I` and `J` is coarser than both of `I` and `J`::

            sage: all( all( I.is_finer(I.meet(J)) and
            ....:           J.is_finer(I.meet(J))
            ....:           for J in Compositions(4) )
            ....:      for I in Compositions(4) )
            True

        and is the finest composition to do so::

            sage: all( all( all( I.meet(J).is_finer(K)
            ....:                for K in I.fatter()
            ....:                if J.is_finer(K) )
            ....:           for J in Compositions(3) )
            ....:      for I in Compositions(3) )
            True

        The descent set of the meet of `I` and `J` is the
        intersection of the descent sets of `I` and `J`::

            sage: def test_meet(n):
            ....:     return all( all( I.to_subset().intersection(J.to_subset())
            ....:                      == I.meet(J).to_subset()
            ....:                      for J in Compositions(n) )
            ....:                 for I in Compositions(n) )
            sage: all( test_meet(n) for n in range(1, 5) )
            True

        TESTS::

            sage: Composition([3, 1, 1, 3, 1]).meet([4, 3, 1])
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 1, 3, 1] is not the same size as [4, 3, 1]

        .. SEEALSO::

            :meth:`join`

        AUTHORS:

        - Darij Grinberg (2013-09-05)
        """
    inf = meet
    def finer(self):
        """
        Return the set of compositions which are finer than ``self``.

        EXAMPLES::

            sage: C = Composition([3,2]).finer()
            sage: C.cardinality()
            8
            sage: C.list()
            [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 1, 1], [1, 2, 2], [2, 1, 1, 1], [2, 1, 2], [3, 1, 1], [3, 2]]

            sage: Composition([]).finer()
            {[]}
        """
    def is_finer(self, co2) -> bool:
        """
        Return ``True`` if the composition ``self`` is finer than the
        composition ``co2``; otherwise, return ``False``.

        EXAMPLES::

            sage: Composition([4,1,2]).is_finer([3,1,3])
            False
            sage: Composition([3,1,3]).is_finer([4,1,2])
            False
            sage: Composition([1,2,2,1,1,2]).is_finer([5,1,3])
            True
            sage: Composition([2,2,2]).is_finer([4,2])
            True
        """
    def fatten(self, grouping) -> Composition:
        """
        Return the composition fatter than ``self``, obtained by grouping
        together consecutive parts according to ``grouping``.

        INPUT:

        - ``grouping`` -- a composition whose sum is the length of ``self``

        EXAMPLES:

        Let us start with the composition::

            sage: c = Composition([4,5,2,7,1])

        With ``grouping`` equal to `(1, \\ldots, 1)`, `c` is left unchanged::

            sage: c.fatten(Composition([1,1,1,1,1]))
            [4, 5, 2, 7, 1]

        With ``grouping`` equal to `(\\ell)` where `\\ell` is the length of
        `c`, this yields the coarsest composition above `c`::

            sage: c.fatten(Composition([5]))
            [19]

        Other values for ``grouping`` yield (all the) other compositions
        coarser than `c`::

            sage: c.fatten(Composition([2,1,2]))
            [9, 2, 8]
            sage: c.fatten(Composition([3,1,1]))
            [11, 7, 1]

        TESTS::

            sage: Composition([]).fatten(Composition([]))
            []
            sage: c.fatten(Composition([3,1,1])).__class__ == c.__class__
            True
        """
    def fatter(self):
        """
        Return the set of compositions which are fatter than ``self``.

        Complexity for generation: `O(|c|)` memory, `O(|r|)` time where `|c|`
        is the size of ``self`` and `r` is the result.

        EXAMPLES::

            sage: C = Composition([4,5,2]).fatter()
            sage: C.cardinality()
            4
            sage: list(C)
            [[4, 5, 2], [4, 7], [9, 2], [11]]

        Some extreme cases::

            sage: list(Composition([5]).fatter())
            [[5]]
            sage: list(Composition([]).fatter())
            [[]]
            sage: list(Composition([1,1,1,1]).fatter()) == list(Compositions(4))
            True
        """
    def refinement_splitting(self, J) -> list[Composition]:
        """
        Return the refinement splitting of ``self`` according to ``J``.

        INPUT:

        - ``J`` -- a composition such that ``self`` is finer than ``J``

        OUTPUT:

        - the unique list of compositions `(I^{(p)})_{p=1, \\ldots , m}`,
          obtained by splitting `I`, such that
          `|I^{(p)}| = J_p` for all `p = 1, \\ldots, m`.

        .. SEEALSO::

            :meth:`refinement_splitting_lengths`

        EXAMPLES::

            sage: Composition([1,2,2,1,1,2]).refinement_splitting([5,1,3])
            [[1, 2, 2], [1], [1, 2]]
            sage: Composition([]).refinement_splitting([])
            []
            sage: Composition([3]).refinement_splitting([2])
            Traceback (most recent call last):
            ...
            ValueError: compositions self (= [3]) and J (= [2]) must be of the same size
            sage: Composition([2,1]).refinement_splitting([1,2])
            Traceback (most recent call last):
            ...
            ValueError: composition J (= [2, 1]) does not refine self (= [1, 2])
        """
    def refinement_splitting_lengths(self, J):
        """
        Return the lengths of the compositions in the refinement splitting of
        ``self`` according to ``J``.

        .. SEEALSO::

            :meth:`refinement_splitting` for the definition of refinement splitting

        EXAMPLES::

            sage: Composition([1,2,2,1,1,2]).refinement_splitting_lengths([5,1,3])
            [3, 1, 2]
            sage: Composition([]).refinement_splitting_lengths([])
            []
            sage: Composition([3]).refinement_splitting_lengths([2])
            Traceback (most recent call last):
            ...
            ValueError: compositions self (= [3]) and J (= [2]) must be of the same size
            sage: Composition([2,1]).refinement_splitting_lengths([1,2])
            Traceback (most recent call last):
            ...
            ValueError: composition J (= [2, 1]) does not refine self (= [1, 2])
        """
    def major_index(self) -> int:
        """
        Return the major index of ``self``. The major index is
        defined as the sum of the descents.

        EXAMPLES::

            sage: Composition([1, 1, 3, 1, 2, 1, 3]).major_index()
            31
        """
    def to_code(self) -> list:
        """
        Return the code of the composition ``self``.

        The code of a composition `I` is a list of length
        `\\mathrm{size}(I)` of 1s and 0s such that there is a 1
        wherever a new part starts. (Exceptional case: When the
        composition is empty, the code is ``[0]``.)

        EXAMPLES::

            sage: Composition([4,1,2,3,5]).to_code()
            [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]

        TESTS::

            sage: Composition([]).to_code()
            [0]
        """
    def partial_sums(self, final: bool = True) -> list:
        """
        The partial sums of the sequence defined by the entries of the
        composition.

        If `I = (i_1, \\ldots, i_m)` is a composition, then the partial sums of
        the entries of the composition are
        `[i_1, i_1 + i_2, \\ldots, i_1 + i_2 + \\cdots + i_m]`.

        INPUT:

        - ``final`` -- boolean (default: ``True``); whether or not to include
          the final partial sum, which is always the size of the composition

        .. SEEALSO::

            :meth:`to_subset`

        EXAMPLES::

            sage: Composition([1,1,3,1,2,1,3]).partial_sums()
            [1, 2, 5, 6, 8, 9, 12]

        With ``final = False``, the last partial sum is not included::

            sage: Composition([1,1,3,1,2,1,3]).partial_sums(final=False)
            [1, 2, 5, 6, 8, 9]
        """
    def to_subset(self, final: bool = False):
        """
        The subset corresponding to ``self`` under the bijection (see below)
        between compositions of `n` and subsets of `\\{1, 2, \\ldots, n-1\\}`.

        The bijection maps a composition `(i_1, \\ldots, i_k)` of `n` to
        `\\{i_1, i_1 + i_2, i_1 + i_2 + i_3, \\ldots, i_1 + \\cdots + i_{k-1}\\}`.

        INPUT:

        - ``final`` -- boolean (default: ``False``); whether or not to include
          the final partial sum, which is always the size of the composition

        .. SEEALSO::

            :meth:`partial_sums`

        EXAMPLES::

            sage: Composition([1,1,3,1,2,1,3]).to_subset()
            {1, 2, 5, 6, 8, 9}
            sage: for I in Compositions(3): print(I.to_subset())
            {1, 2}
            {1}
            {2}
            {}

        With ``final=True``, the sum of all the elements of the composition is
        included in the subset::

            sage: Composition([1,1,3,1,2,1,3]).to_subset(final=True)
            {1, 2, 5, 6, 8, 9, 12}

        TESTS:

        We verify that ``to_subset`` is indeed a bijection for compositions of
        size `n = 8`::

            sage: n = 8
            sage: all(Composition(from_subset=(S, n)).to_subset() == S
            ....:     for S in Subsets(n-1))
            True
            sage: all(Composition(from_subset=(I.to_subset(), n)) == I
            ....:     for I in Compositions(n))
            True
        """
    def descents(self, final_descent: bool = False) -> list:
        """
        This gives one fewer than the partial sums of the composition.

        This is here to maintain some sort of backward compatibility, even
        through the original implementation was broken (it gave the wrong
        answer). The same information can be found in :meth:`partial_sums`.

        .. SEEALSO::

            :meth:`partial_sums`

        INPUT:

        - ``final_descent`` -- boolean (default: ``False``)

        OUTPUT:

        - the list of partial sums of ``self`` with each part
          decremented by `1`. This includes the sum of all entries when
          ``final_descent`` is ``True``.

        EXAMPLES::

            sage: c = Composition([2,1,3,2])
            sage: c.descents()
            [1, 2, 5]
            sage: c.descents(final_descent=True)
            [1, 2, 5, 7]
        """
    def peaks(self) -> list:
        """
        Return a list of the peaks of the composition ``self``.

        The peaks of a composition are the descents which do not
        immediately follow another descent.

        EXAMPLES::

            sage: Composition([1, 1, 3, 1, 2, 1, 3]).peaks()
            [4, 7]
        """
    def to_partition(self):
        """
        Return the partition obtained by sorting ``self`` into decreasing
        order.

        EXAMPLES::

            sage: Composition([2,1,3]).to_partition()                                   # needs sage.combinat
            [3, 2, 1]
            sage: Composition([4,2,2]).to_partition()                                   # needs sage.combinat
            [4, 2, 2]
            sage: Composition([]).to_partition()                                        # needs sage.combinat
            []
        """
    def to_skew_partition(self, overlap: int = 1):
        """
        Return the skew partition obtained from ``self``.

        This is a skew partition whose rows have the entries of
        ``self`` as their length, taken in reverse order (so the first
        entry of ``self`` is the length of the lowermost row,
        etc.). The parameter ``overlap`` indicates the number of cells
        on each row that are directly below cells of the previous
        row. When it is set to `1` (its default value), the result is
        the ribbon shape of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: Composition([3,4,1]).to_skew_partition()
            [6, 6, 3] / [5, 2]
            sage: Composition([3,4,1]).to_skew_partition(overlap=0)
            [8, 7, 3] / [7, 3]
            sage: Composition([]).to_skew_partition()
            [] / []
            sage: Composition([1,2]).to_skew_partition()
            [2, 1] / []
            sage: Composition([2,1]).to_skew_partition()
            [2, 2] / [1]
        """
    def shuffle_product(self, other, overlap: bool = False):
        """
        The (overlapping) shuffles of ``self`` and ``other``.

        Suppose `I = (i_1, \\ldots, i_k)` and `J = (j_1, \\ldots, j_l)` are two
        compositions. A *shuffle* of `I` and `J` is a composition of length
        `k + l` that contains both `I` and `J` as subsequences.

        More generally, an *overlapping shuffle* of `I` and `J` is obtained by
        distributing the elements of `I` and `J` (preserving the relative
        ordering of these elements) among the positions of an empty list; an
        element of `I` and an element of `J` are permitted to share the same
        position, in which case they are replaced by their sum. In particular,
        a shuffle of `I` and `J` is an overlapping shuffle of `I` and `J`.

        INPUT:

        - ``other`` -- composition

        - ``overlap`` -- boolean (default: ``False``); if ``True``, the
          overlapping shuffle product is returned

        OUTPUT:

        An enumerated set (allowing for multiplicities)

        EXAMPLES:

        The shuffle product of `[2,2]` and `[1,1,3]`::

            sage: alph = Composition([2,2])
            sage: beta = Composition([1,1,3])
            sage: S = alph.shuffle_product(beta); S                                     # needs sage.combinat
            Shuffle product of [2, 2] and [1, 1, 3]
            sage: S.list()                                                              # needs sage.combinat
            [[2, 2, 1, 1, 3], [2, 1, 2, 1, 3], [2, 1, 1, 2, 3], [2, 1, 1, 3, 2],
             [1, 2, 2, 1, 3], [1, 2, 1, 2, 3], [1, 2, 1, 3, 2], [1, 1, 2, 2, 3],
             [1, 1, 2, 3, 2], [1, 1, 3, 2, 2]]

        The *overlapping* shuffle product of `[2,2]` and `[1,1,3]`::

            sage: alph = Composition([2,2])
            sage: beta = Composition([1,1,3])
            sage: O = alph.shuffle_product(beta, overlap=True); O                       # needs sage.combinat
            Overlapping shuffle product of [2, 2] and [1, 1, 3]
            sage: O.list()                                                              # needs sage.combinat
            [[2, 2, 1, 1, 3], [2, 1, 2, 1, 3], [2, 1, 1, 2, 3], [2, 1, 1, 3, 2],
             [1, 2, 2, 1, 3], [1, 2, 1, 2, 3], [1, 2, 1, 3, 2], [1, 1, 2, 2, 3],
             [1, 1, 2, 3, 2], [1, 1, 3, 2, 2],
             [3, 2, 1, 3], [2, 3, 1, 3], [3, 1, 2, 3], [2, 1, 3, 3], [3, 1, 3, 2],
             [2, 1, 1, 5], [1, 3, 2, 3], [1, 2, 3, 3], [1, 3, 3, 2], [1, 2, 1, 5],
             [1, 1, 5, 2], [1, 1, 2, 5],
             [3, 3, 3], [3, 1, 5], [1, 3, 5]]

        Note that the shuffle product of two compositions can include the same
        composition more than once since a composition can be a shuffle of two
        compositions in several ways. For example::

            sage: # needs sage.combinat
            sage: w1 = Composition([1])
            sage: S = w1.shuffle_product(w1); S
            Shuffle product of [1] and [1]
            sage: S.list()
            [[1, 1], [1, 1]]
            sage: O = w1.shuffle_product(w1, overlap=True); O
            Overlapping shuffle product of [1] and [1]
            sage: O.list()
            [[1, 1], [1, 1], [2]]

        TESTS::

            sage: empty = Composition([])
            sage: empty.shuffle_product(empty).list()                                   # needs sage.combinat
            [[]]
        """
    def wll_gt(self, co2) -> bool:
        '''
        Return ``True`` if the composition ``self`` is greater than the
        composition ``co2`` with respect to the wll-ordering; otherwise,
        return ``False``.

        The wll-ordering is a total order on the set of all compositions
        defined as follows: A composition `I` is greater than a
        composition `J` if and only if one of the following conditions
        holds:

        - The size of `I` is greater than the size of `J`.

        - The size of `I` equals the size of `J`, but the length of `I`
          is greater than the length of `J`.

        - The size of `I` equals the size of `J`, and the length of `I`
          equals the length of `J`, but `I` is lexicographically
          greater than `J`.

        ("wll-ordering" is short for "weight, length, lexicographic
        ordering".)

        EXAMPLES::

            sage: Composition([4,1,2]).wll_gt([3,1,3])
            True
            sage: Composition([7]).wll_gt([4,1,2])
            False
            sage: Composition([8]).wll_gt([4,1,2])
            True
            sage: Composition([3,2,2,2]).wll_gt([5,2])
            True
            sage: Composition([]).wll_gt([3])
            False
            sage: Composition([2,1]).wll_gt([2,1])
            False
            sage: Composition([2,2,2]).wll_gt([4,2])
            True
            sage: Composition([4,2]).wll_gt([2,2,2])
            False
            sage: Composition([1,1,2]).wll_gt([2,2])
            True
            sage: Composition([2,2]).wll_gt([1,3])
            True
            sage: Composition([2,1,2]).wll_gt([])
            True
        '''
    def count(self, n):
        """
        Return the number of parts of size  ``n``.

        EXAMPLES::

            sage: C = Composition([3,2,3])
            sage: C.count(3)
            2
            sage: C.count(2)
            1
            sage: C.count(1)
            0
        """
    def specht_module(self, base_ring=None):
        """
        Return the Specht module corresponding to ``self``.

        EXAMPLES::

            sage: SM = Composition([1,2,2]).specht_module(QQ); SM                       # needs sage.combinat sage.modules
            Specht module of [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)] over Rational Field
            sage: s = SymmetricFunctions(QQ).s()                                        # needs sage.combinat sage.modules
            sage: s(SM.frobenius_image())                                               # needs sage.combinat sage.modules
            s[2, 2, 1]
        """
    def specht_module_dimension(self, base_ring=None):
        """
        Return the dimension of the Specht module corresponding to ``self``.

        INPUT:

        - ``base_ring`` -- (default: `\\QQ`) the base ring

        EXAMPLES::

            sage: Composition([1,2,2]).specht_module_dimension()                        # needs sage.combinat sage.modules
            5
            sage: Composition([1,2,2]).specht_module_dimension(GF(2))                   # needs sage.combinat sage.modules sage.rings.finite_rings
            5
        """

class Compositions(UniqueRepresentation, Parent):
    """
    Set of integer compositions.

    A composition `c` of a nonnegative integer `n` is a list of
    positive integers with total sum `n`.

    .. SEEALSO::

        - :class:`Composition`
        - :class:`Partitions`
        - :class:`IntegerVectors`

    EXAMPLES:

    There are 8 compositions of 4::

        sage: Compositions(4).cardinality()
        8

    Here is the list of them::

        sage: Compositions(4).list()
        [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1], [4]]

    You can use the ``.first()`` method to get the 'first' composition of
    a number::

        sage: Compositions(4).first()
        [1, 1, 1, 1]

    You can also calculate the 'next' composition given the current
    one::

        sage: Compositions(4).next([1,1,2])
        [1, 2, 1]

    If `n` is not specified, this returns the combinatorial class of
    all (nonnegative) integer compositions::

        sage: Compositions()
        Compositions of nonnegative integers
        sage: [] in Compositions()
        True
        sage: [2,3,1] in Compositions()
        True
        sage: [-2,3,1] in Compositions()
        False

    If `n` is specified, it returns the class of compositions of `n`::

        sage: Compositions(3)
        Compositions of 3
        sage: list(Compositions(3))
        [[1, 1, 1], [1, 2], [2, 1], [3]]
        sage: Compositions(3).cardinality()
        4

    The following examples show how to test whether or not an object
    is a composition::

        sage: [3,4] in Compositions()
        True
        sage: [3,4] in Compositions(7)
        True
        sage: [3,4] in Compositions(5)
        False

    Similarly, one can check whether or not an object is a composition
    which satisfies further constraints::

        sage: [4,2] in Compositions(6, inner=[2,2])
        True
        sage: [4,2] in Compositions(6, inner=[2,3])
        False
        sage: [4,1] in Compositions(5, inner=[2,1], max_slope = 0)
        True

    An example with incompatible constraints::

        sage: [4,2] in Compositions(6, inner=[2,2], min_part=3)
        False

    The options ``length``, ``min_length``, and ``max_length`` can be used
    to set length constraints on the compositions. For example, the
    compositions of 4 of length equal to, at least, and at most 2 are
    given by::

        sage: Compositions(4, length=2).list()
        [[3, 1], [2, 2], [1, 3]]
        sage: Compositions(4, min_length=2).list()
        [[3, 1], [2, 2], [2, 1, 1], [1, 3], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(4, max_length=2).list()
        [[4], [3, 1], [2, 2], [1, 3]]

    Setting both ``min_length`` and ``max_length`` to the same value is
    equivalent to setting ``length`` to this value::

        sage: Compositions(4, min_length=2, max_length=2).list()
        [[3, 1], [2, 2], [1, 3]]

    The options ``inner`` and ``outer`` can be used to set part-by-part
    containment constraints. The list of compositions of 4 bounded
    above by ``[3,1,2]`` is given by::

        sage: list(Compositions(4, outer=[3,1,2]))
        [[3, 1], [2, 1, 1], [1, 1, 2]]

    ``outer`` sets ``max_length`` to the length of its argument. Moreover, the
    parts of ``outer`` may be infinite to clear the constraint on specific
    parts. This is the list of compositions of 4 of length at most 3
    such that the first and third parts are at most 1::

        sage: Compositions(4, outer=[1,oo,1]).list()
        [[1, 3], [1, 2, 1]]

    This is the list of compositions of 4 bounded below by ``[1,1,1]``::

        sage: Compositions(4, inner=[1,1,1]).list()
        [[2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]

    The options ``min_slope`` and ``max_slope`` can be used to set constraints
    on the slope, that is the difference ``p[i+1]-p[i]`` of two
    consecutive parts. The following is the list of weakly increasing
    compositions of 4::

        sage: Compositions(4, min_slope=0).list()
        [[4], [2, 2], [1, 3], [1, 1, 2], [1, 1, 1, 1]]

    Here are the weakly decreasing ones::

        sage: Compositions(4, max_slope=0).list()
        [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

    The following is the list of compositions of 4 such that two
    consecutive parts differ by at most one::

        sage: Compositions(4, min_slope=-1, max_slope=1).list()
        [[4], [2, 2], [2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]

    The constraints can be combined together in all reasonable ways.
    This is the list of compositions of 5 of length between 2 and 4
    such that the difference between consecutive parts is between -2
    and 1::

        sage: Compositions(5, max_slope=1, min_slope=-2, min_length=2, max_length=4).list()
        [[3, 2], [3, 1, 1], [2, 3], [2, 2, 1], [2, 1, 2], [2, 1, 1, 1], [1, 2, 2], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]

    We can do the same thing with an outer constraint::

        sage: Compositions(5, max_slope=1, min_slope=-2, min_length=2, max_length=4, outer=[2,5,2]).list()
        [[2, 3], [2, 2, 1], [2, 1, 2], [1, 2, 2]]

    However, providing incoherent constraints may yield strange
    results. It is up to the user to ensure that the inner and outer
    compositions themselves satisfy the parts and slope constraints.

    Note that setting ``min_part=0`` is not allowed::

        sage: Compositions(2, length=3, min_part=0)
        Traceback (most recent call last):
        ...
        ValueError: setting min_part=0 is not allowed for Compositions

    Instead you must use ``IntegerVectors``::

        sage: list(IntegerVectors(2, 3))
        [[2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]

    The generation algorithm is constant amortized time, and handled
    by the generic tool :class:`IntegerListsLex`.

    TESTS::

        sage: C = Compositions(4, length=2)
        sage: C == loads(dumps(C))
        True

        sage: Compositions(6, min_part=2, length=3)
        Compositions of the integer 6 satisfying constraints length=3, min_part=2

        sage: [2, 1] in Compositions(3, length=2)
        True
        sage: [2,1,2] in Compositions(5, min_part=1)
        True
        sage: [2,1,2] in Compositions(5, min_part=2)
        False

        sage: Compositions(4, length=2).cardinality()
        3
        sage: Compositions(4, min_length=2).cardinality()
        7
        sage: Compositions(4, max_length=2).cardinality()
        4
        sage: Compositions(4, max_part=2).cardinality()
        5
        sage: Compositions(4, min_part=2).cardinality()
        2
        sage: Compositions(4, outer=[3,1,2]).cardinality()
        3

        sage: Compositions(4, length=2).list()
        [[3, 1], [2, 2], [1, 3]]
        sage: Compositions(4, min_length=2).list()
        [[3, 1], [2, 2], [2, 1, 1], [1, 3], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(4, max_length=2).list()
        [[4], [3, 1], [2, 2], [1, 3]]
        sage: Compositions(4, max_part=2).list()
        [[2, 2], [2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(4, min_part=2).list()
        [[4], [2, 2]]
        sage: Compositions(4, outer=[3,1,2]).list()
        [[3, 1], [2, 1, 1], [1, 1, 2]]
        sage: Compositions(3, outer = Composition([3,2])).list()
        [[3], [2, 1], [1, 2]]
        sage: Compositions(4, outer=[1,oo,1]).list()
        [[1, 3], [1, 2, 1]]
        sage: Compositions(4, inner=[1,1,1]).list()
        [[2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(4, inner=Composition([1,2])).list()
        [[2, 2], [1, 3], [1, 2, 1]]
        sage: Compositions(4, min_slope=0).list()
        [[4], [2, 2], [1, 3], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(4, min_slope=-1, max_slope=1).list()
        [[4], [2, 2], [2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
        sage: Compositions(5, max_slope=1, min_slope=-2, min_length=2, max_length=4).list()
        [[3, 2], [3, 1, 1], [2, 3], [2, 2, 1], [2, 1, 2], [2, 1, 1, 1], [1, 2, 2], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]
        sage: Compositions(5, max_slope=1, min_slope=-2, min_length=2, max_length=4, outer=[2,5,2]).list()
        [[2, 3], [2, 2, 1], [2, 1, 2], [1, 2, 2]]
    """
    @staticmethod
    def __classcall_private__(self, n=None, **kwargs):
        """
        Return the correct parent based upon the input.

        EXAMPLES::

            sage: C = Compositions(3)
            sage: C2 = Compositions(int(3))
            sage: C is C2
            True
        """
    def __init__(self, is_infinite: bool = False, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = Compositions()
            sage: TestSuite(C).run()
        """
    Element = Composition
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [2,1,3] in Compositions()
            True
            sage: [] in Compositions()
            True
            sage: [-2,-1] in Compositions()
            False
            sage: [0,0] in Compositions()
            True
        """
    def from_descents(self, descents, nps=None) -> Composition:
        """
        Return a composition from the list of descents.

        INPUT:

        - ``descents`` -- an iterable

        - ``nps`` -- integer or ``None`` (default: ``None``)

        OUTPUT:

        - The composition of ``nps`` whose descents are listed in
          ``descents``, assuming that ``nps`` is not ``None`` (otherwise,
          the last element of ``descents`` is removed from ``descents``, and
          ``nps`` is set to be this last element plus 1).

        EXAMPLES::

            sage: [x-1 for x in Composition([1, 1, 3, 4, 3]).to_subset()]
            [0, 1, 4, 8]
            sage: Compositions().from_descents([1,0,4,8],12)
            [1, 1, 3, 4, 3]
            sage: Compositions().from_descents([1,0,4,8,11])
            [1, 1, 3, 4, 3]
        """
    def from_subset(self, S, n) -> Composition:
        """
        The composition of `n` corresponding to the subset ``S`` of
        `\\{1, 2, \\ldots, n-1\\}` under the bijection that maps the composition
        `(i_1, i_2, \\ldots, i_k)` of `n` to the subset
        `\\{i_1, i_1 + i_2, i_1 + i_2 + i_3, \\ldots, i_1 + \\cdots + i_{k-1}\\}`
        (see :meth:`Composition.to_subset`).

        INPUT:

        - ``S`` -- an iterable, a subset of `\\{1, 2, \\ldots, n-1\\}`

        - ``n`` -- integer

        EXAMPLES::

            sage: Compositions().from_subset([2,1,5,9], 12)
            [1, 1, 3, 4, 3]
            sage: Compositions().from_subset({2,1,5,9}, 12)
            [1, 1, 3, 4, 3]

            sage: Compositions().from_subset([], 12)
            [12]
            sage: Compositions().from_subset([], 0)
            []

        TESTS::

            sage: Compositions().from_subset([2,1,5,9],9)
            Traceback (most recent call last):
            ...
            ValueError: S (=[1, 2, 5, 9]) is not a subset of {1, ..., 8}
        """
    def from_code(self, code) -> Composition:
        """
        Return the composition from its code. The code of a composition
        `I` is a list of length `\\mathrm{size}(I)` consisting of 1s and
        0s such that there is a 1 wherever a new part starts.
        (Exceptional case: When the composition is empty, the code is
        ``[0]``.)

        EXAMPLES::

            sage: Composition([4,1,2,3,5]).to_code()
            [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
            sage: Compositions().from_code(_)
            [4, 1, 2, 3, 5]
            sage: Composition([3,1,2,3,5]).to_code()
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
            sage: Compositions().from_code(_)
            [3, 1, 2, 3, 5]
        """

class Compositions_constraints(IntegerListsLex): ...

class Compositions_all(Compositions):
    """
    Class of all compositions.
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: C = Compositions()
            sage: TestSuite(C).run()
        """
    def subset(self, size=None):
        """
        Return the set of compositions of the given size.

        EXAMPLES::

            sage: C = Compositions()
            sage: C.subset(4)
            Compositions of 4
            sage: C.subset(size=3)
            Compositions of 3
        """
    def zero(self):
        """
        Return the zero of the additive monoid.

        This is the empty composition.

        EXAMPLES::

            sage: C = Compositions()
            sage: C.zero()
            []
        """
    def __iter__(self):
        """
        Iterate over all compositions.

        TESTS::

            sage: C = Compositions()
            sage: it = C.__iter__()
            sage: [next(it) for i in range(10)]
            [[], [1], [1, 1], [2], [1, 1, 1], [1, 2], [2, 1], [3], [1, 1, 1, 1], [1, 1, 2]]
        """

class Compositions_n(Compositions):
    """
    Class of compositions of a fixed `n`.
    """
    @staticmethod
    def __classcall_private__(cls, n):
        """
        Standardize input to ensure a unique representation.

        EXAMPLES::

            sage: C = Compositions(5)
            sage: C2 = Compositions(int(5))
            sage: C3 = Compositions(ZZ(5))
            sage: C is C2
            True
            sage: C is C3
            True
        """
    n: Incomplete
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: C = Compositions(3)
            sage: C == loads(dumps(C))
            True
            sage: TestSuite(C).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [2,1,3] in Compositions(6)
            True
            sage: [2,1,2] in Compositions(6)
            False
            sage: [] in Compositions(0)
            True
            sage: [0] in Compositions(0)
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the number of compositions of `n`.

        TESTS::

            sage: Compositions(3).cardinality()
            4
            sage: Compositions(0).cardinality()
            1
        """
    def random_element(self) -> Composition:
        """
        Return a random ``Composition`` with uniform probability.

        This method generates a random binary word starting with a 1
        and then uses the bijection between compositions and their code.

        EXAMPLES::

            sage: Compositions(5).random_element() # random
            [2, 1, 1, 1]
            sage: Compositions(0).random_element()
            []
            sage: Compositions(1).random_element()
            [1]

        TESTS::

            sage: all(Compositions(10).random_element() in Compositions(10) for i in range(20))
            True
        """
    def __iter__(self):
        """
        Iterate over the compositions of `n`.

        TESTS::

            sage: Compositions(4).list()
            [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1], [4]]
            sage: Compositions(0).list()
            [[]]
        """

def composition_iterator_fast(n) -> Generator[Incomplete]:
    """
    Iterator over compositions of `n` yielded as lists.

    TESTS::

        sage: from sage.combinat.composition import composition_iterator_fast
        sage: L = list(composition_iterator_fast(4)); L
        [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1], [4]]
        sage: type(L[0])
        <class 'list'>
    """
