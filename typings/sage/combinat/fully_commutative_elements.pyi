from _typeshed import Incomplete
from collections import deque as deque
from collections.abc import Generator
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.list_clone import NormalizedClonableList as NormalizedClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FullyCommutativeElement(NormalizedClonableList):
    """
    A fully commutative (FC) element in a Coxeter system.

    An element `w` in a Coxeter system (W,S) is fully commutative (FC) if every
    two reduced word of w can be related by a sequence of only commutation
    relations, i.e., relations of the form `st=ts` where `s,t` are commuting
    generators in `S`.

    Every FC element has a canonical reduced word called its Cartier--Foata
    form. See [Gre2006]_. We will normalize each FC element to this form.
    """
    def group_element(self):
        """
        Get the actual element of the Coxeter group associated with
        ``self.parent()`` corresponding to ``self``.

        EXAMPLES::

            sage: W = CoxeterGroup(['A', 3])
            sage: FC = W.fully_commutative_elements()
            sage: x = FC([1, 2])
            sage: x.group_element()
            [ 0 -1  1]
            [ 1 -1  1]
            [ 0  0  1]
            sage: x.group_element() in W
            True
        """
    def check(self) -> None:
        """
        Called automatically when an element is created.

        EXAMPLES::

            sage: CoxeterGroup(['A', 3]).fully_commutative_elements()([1, 2]) # indirect doctest
            [1, 2]
            sage: CoxeterGroup(['A', 3]).fully_commutative_elements()([1, 2, 1]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the input is not a reduced word of a fully commutative element
        """
    def normalize(self) -> None:
        """
        Mutate ``self`` into Cartier-Foata normal form.

        EXAMPLES:

        The following reduced words express the same FC elements in `B_5`::

            sage: FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            sage: FC([1, 4, 3, 5, 2, 4, 3]) # indirect doctest
            [1, 4, 3, 5, 2, 4, 3]
            sage: FC([4, 1, 3, 5, 2, 4, 3]) # indirect doctest
            [1, 4, 3, 5, 2, 4, 3]
            sage: FC([4, 3, 1, 5, 4, 2, 3]) # indirect doctest
            [1, 4, 3, 5, 2, 4, 3]

        .. NOTE::

            The Cartier--Foata form of a reduced word of an FC element `w` can
            be found recursively by repeatedly moving left descents of
            elements to the left and ordering the left descents from small to
            large. In the above example, the left descents of the element are
            4 and 1, therefore the Cartier--Foata form of the element is the
            concatenation of [1,4] with the Cartier--Foata form of the
            remaining part of the word. See [Gre2006]_.

        .. SEEALSO:: :func:`descents`
        """
    def is_fully_commutative(self):
        """
        Check if ``self`` is the reduced word of an FC element.

        To check if ``self`` is FC, we use the well-known characterization that
        an element `w` in a Coxeter system `(W,S)` is FC if and only if for
        every pair of generators `s,t \\in S` for which `m(s,t)>2`, no reduced
        word of `w` contains the 'braid' word `sts...` of length `m(s,t)` as a
        contiguous subword. See [Ste1996]_.

        :func:`check` is an alias of this method, and is called automatically
        when an element is created.

        EXAMPLES::

            sage: FC = CoxeterGroup(['A', 3]).fully_commutative_elements()
            sage: x = FC([1, 2]); x.is_fully_commutative()
            True
            sage: x = FC.element_class(FC, [1, 2, 1], check=False); x.is_fully_commutative()
            False
        """
    def heap(self, **kargs):
        """
        Create the heap poset of ``self``.

        The heap of an FC element `w` is a labeled poset that can be defined
        from any reduced word of `w`. Different reduced words yield isomorphic
        labeled posets, so the heap is well defined.

        Heaps are very useful for visualizing and studying FC elements; see, for
        example, [Ste1996]_ and [GX2020]_.

        INPUT:

        - ``self`` -- list; a reduced word `w=s_0... s_{k-1}` of an FC element

        - ``one_index`` -- boolean (default: ``False``); setting the value to True
          will change the underlying set of the poset to `\\{1, 2, \\dots, n\\}`

        - ``display_labeling`` -- boolean (default: ``False``); setting the value to
          ``True`` will display the label `s_i` for each element `i` of the poset

        OUTPUT:

        A labeled poset where the underlying set is `\\{0,1,...,k-1\\}`
        and where each element `i` carries `s_i` as its label. The partial order
        `\\prec` on the poset is defined by declaring `i\\prec j` if `i<j` and
        `m(s_i,s_j)\\neq 2`.

        EXAMPLES::

            sage: FC = CoxeterGroup(['A', 5]).fully_commutative_elements()
            sage: FC([1, 4, 3, 5, 2, 4]).heap().cover_relations()
            [[1, 2], [1, 3], [2, 5], [2, 4], [3, 5], [0, 4]]
            sage: FC([1, 4, 3, 5, 4, 2]).heap(one_index=True).cover_relations()
            [[2, 3], [2, 4], [3, 6], [3, 5], [4, 6], [1, 5]]
        """
    def plot_heap(self):
        """
        Display the Hasse diagram of the heap of ``self``.

        The Hasse diagram is rendered in the lattice `S \\times \\NN`, with
        every element `i` in the poset drawn as a point labelled by its label
        `s_i`. Every point is placed in the column for its label at a certain
        level. The levels start at 0 and the level k of an element `i` is the
        maximal number `k` such that the heap contains a chain `i_0\\prec
        i_1\\prec ... \\prec i_k` where `i_k=i`. See [Ste1996]_ and [GX2020]_.

        OUTPUT: GraphicsObject

        EXAMPLES::

            sage: FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            sage: FC([3,2,4,3,1]).plot_heap()                                           # needs sage.plot
            Graphics object consisting of 15 graphics primitives

        .. PLOT::
            :width: 400 px

            FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            g = FC([3,2,4,3,1]).plot_heap()
            sphinx_plot(g)
        """
    def n_value(self):
        """
        Calculate the n-value of ``self``.

        The *n-value* of a fully commutative element is the *width* (length of
        any longest antichain) of its heap. The n-value is important as it
        coincides with Lusztig's a-value for FC elements in all Weyl and affine
        Weyl groups as well as so-called star-reducible groups; see [GX2020]_.

        EXAMPLES::

            sage: FC = CoxeterGroup(['A', 5]).fully_commutative_elements()
            sage: FC([1,3]).n_value()
            2
            sage: FC([1,2,3]).n_value()
            1
            sage: FC([1,3,2]).n_value()
            2
            sage: FC([1,3,2,5]).n_value()
            3
        """
    def find_descent(self, s, side: str = 'left'):
        """
        Check if ``s`` is a descent of ``self`` and find its position if so.

        A generator `s` is called a left or right descent of an element `w` if
        `l(sw)` or `l(ws)` is smaller than `l(w)`, respectively. If `w` is FC,
        then `s` is a left descent of `w` if and only if `s` appears to in the
        word and every generator to the left of the leftmost `s` in the word
        commutes with `s`. A similar characterization exists for right descents
        of FC elements.

        INPUT:

        - ``s`` -- integer representing a generator of the Coxeter system

        - ``side`` -- string (default: ``'left'``); if the argument is set to
          'right', the function checks if ``s`` is a right descent of ``self``
          and finds the index of the rightmost occurrence of ``s`` if so

        OUTPUT:

        Determine if the generator ``s`` is a left descent of ``self``; return
        the index of the leftmost occurrence of ``s`` in ``self`` if so and
        return ``None`` if not.

        EXAMPLES::

            sage: FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            sage: w = FC([1, 4, 3, 5, 2, 4, 3])
            sage: w.find_descent(1)
            0
            sage: w.find_descent(1, side='right')
            <BLANKLINE>
            sage: w.find_descent(4)
            1
            sage: w.find_descent(4, side='right')
            <BLANKLINE>
            sage: w.find_descent(3)
            <BLANKLINE>
        """
    def has_descent(self, s, side: str = 'left') -> bool:
        """
        Determine if ``s`` is a descent on the appropriate side of ``self``.

        INPUT:

        - ``side`` -- string (default: ``'left'``); if set to 'right', determine
          if ``self`` has ``s`` as a right descent

        OUTPUT: boolean

        EXAMPLES::

            sage: FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            sage: w = FC([1, 4, 3, 5, 2, 4, 3])
            sage: w.has_descent(1)
            True
            sage: w.has_descent(1, side='right')
            False
            sage: w.has_descent(4)
            True
            sage: w.has_descent(4, side='right')
            False

        .. SEEALSO:: :func:`find_descent`
        """
    def descents(self, side: str = 'left'):
        """
        Obtain the set of descents on the appropriate side of ``self``.

        INPUT:

        - ``side`` -- string (default: ``'left'``); if set to 'right', find the
          right descents

        A generator `s` is called a left or right descent of an element `w` if
        `l(sw)` or `l(ws)` is smaller than `l(w)`, respectively. If `w` is FC,
        then `s` is a left descent of `w` if and only if `s` appears to in the
        word and every generator to the left of the leftmost `s` in the word
        commutes with `s`. A similar characterization exists for right descents
        of FC elements.

        EXAMPLES::

            sage: FC = CoxeterGroup(['B', 5]).fully_commutative_elements()
            sage: w = FC([1, 4, 3, 5, 2, 4, 3])
            sage: sorted(w.descents())
            [1, 4]
            sage: w.descents(side='right')
            {3}
            sage: FC = CoxeterGroup(['A', 5]).fully_commutative_elements()
            sage: sorted(FC([1, 4, 3, 5, 2, 4, 3]).descents())
            [1, 4]

        .. SEEALSO:: :func:`find_descent`
        """
    def coset_decomposition(self, J, side: str = 'left'):
        '''
        Return the coset decomposition of ``self`` with respect to the parabolic
        subgroup generated by ``J``.

        INPUT:

        - ``J`` -- subset of the generating set `S` of the Coxeter system

        - ``side`` -- string (default: ``\'left\'``); if the value is set to
          \'right\', then the function returns the tuple `(w\'^J, w\'_J)` from the
          coset decomposition `w = w\'^J \\cdot w\'_J` of `w` with respect to `J`

        OUTPUT:

        The tuple of elements `(w_J, w^J)` such that `w=w_J \\cdot w^J`, `w_J` is
        generated by the elements in `J`, and `w^J` has no left descent from
        `J`. This tuple is unique and satisfies the equation `\\ell(w) =
        \\ell(w_J) + \\ell(w^J)`, where `\\ell` denotes Coxeter length, by general
        theory; see Proposition 2.4.4 of [BB2005]_.

        EXAMPLES::

            sage: FC = CoxeterGroup([\'B\', 6]).fully_commutative_elements()
            sage: w = FC([1, 6, 2, 5, 4, 6, 5])
            sage: w.coset_decomposition({1})
            ([1], [6, 2, 5, 4, 6, 5])
            sage: w.coset_decomposition({1}, side = \'right\')
            ([1, 6, 2, 5, 4, 6, 5], [])
            sage: w.coset_decomposition({5, 6})
            ([6, 5, 6], [1, 2, 4, 5])
            sage: w.coset_decomposition({5, 6}, side=\'right\')
            ([1, 6, 2, 5, 4], [6, 5])

        .. NOTE::

            The factor `w_J` of the coset decomposition `w = w_J \\cdot
            w^J` can be obtained by greedily "pulling left descents of `w` that
            are in `J` to the left"; see the proof of [BB2005]_. This greedy
            algorithm works for all elements in Coxeter group, but it becomes
            especially simple for FC elements because descents are easier to
            find for FC elements.
        '''
    def star_operation(self, J, direction, side: str = 'left'):
        """
        Apply a star operation on ``self`` relative to two noncommuting
        generators.

        Star operations were first defined on elements of Coxeter groups by
        Kazhdan and Lusztig in [KL1979]_ with respect to pair of generators
        `s,t` such that `m(s,t)=3`. Later, Lusztig generalized the definition in
        [Lus1985]_, via coset decompositions, to allow star operations with
        respect to any pair of generators `s,t` such that `m(s,t)\\ge 3`. Given
        such a pair, we can potentially perform four types of star operations
        corresponding to all combinations of a 'direction' and a 'side': upper
        left, lower left, upper right and lower right; see [Gre2006]_.

        Let `w` be an element in `W` and let `J` be any pair `\\{s, t\\}` of
        noncommuting generators in `S`. Consider the coset decomposition `w =
        w_J \\cdot {}^J w` of `w` relative to `J`. Then an upper left star
        operation is defined on `w` if and only if  `1 \\le l(w_J) \\le m(s,t)-2`;
        when this is the case, the operation returns `x\\cdot w_J\\cdot w^J` where
        `x` is the letter `J` different from the leftmost letter of `w_J`. A
        lower left star operation is defined on `w` if and only if `2 \\le l(w_J)
        \\le m(s,t)-1`; when this is the case, the operation removes the leftmost
        letter of `w_J` from `w`.  Similar facts hold for right star operations.
        See [Gre2006]_.

        The facts of the previous paragraph hold in general, even if `w` is not
        FC. Note that if `f` is a star operation of any kind, then for every
        element `w \\in W`, the elements `w` and `f(w)` are either both FC or
        both not FC.

        INPUT:

        - ``J`` -- set of two integers representing two noncommuting
          generators of the Coxeter system

        - ``direction`` -- string, ``'upper'`` or ``'lower'``; the function
          performs an upper or lower star operation according to ``direction``

        - ``side`` -- string (default: ``'left'``); if this is set to 'right',
          the function performs a right star operation

        OUTPUT:

        The Cartier--Foata form of the result of the star operation if the
        operation is defined on ``self``, ``None`` otherwise.

        EXAMPLES:

        We will compute all star operations on the following FC element in type
        `B_6` relative to `J = \\{5, 6\\}`::

            sage: FC = CoxeterGroup(['B', 6]).fully_commutative_elements()
            sage: w = FC([1, 6, 2, 5, 4, 6, 5])

        Whether and how a left star operations can be applied depend on the
        coset decomposition `w = w_J \\cdot w^J`::

            sage: w.coset_decomposition({5, 6})
            ([6, 5, 6], [1, 2, 4, 5])

        Only the lower star operation is defined on the left on `w`::

            sage: w.star_operation({5,6}, 'upper')
            <BLANKLINE>
            sage: w.star_operation({5,6}, 'lower')
            [1, 5, 2, 4, 6, 5]

        Whether and how a right star operations can be applied depend on the
        coset decomposition `w = w^J \\cdot w_J`::

            sage: w.coset_decomposition({5, 6}, side='right')
            ([1, 6, 2, 5, 4], [6, 5])

        Both types of right star operations on defined for this example::

            sage: w.star_operation({5, 6}, 'upper', side='right')
            [1, 6, 2, 5, 4, 6, 5, 6]

            sage: w.star_operation({5, 6}, 'lower', side='right')
            [1, 6, 2, 5, 4, 6]
        """

class FullyCommutativeElements(UniqueRepresentation, Parent):
    """
    Class for the set of fully commutative (FC) elements of a Coxeter system.

    Coxeter systems with finitely many FC elements, or *FC-finite* Coxeter
    systems, are classified by Stembridge in [Ste1996]_. They fall into seven
    families, namely the groups of types `A_n, B_n, D_n, E_n, F_n, H_n` and
    `I_2(m)`.

    INPUT:

    - ``data`` -- CoxeterMatrix, CartanType, or the usual datum that can is
      taken in the constructors for these classes (see
      :func:`sage.combinat.root_system.coxeter_group.CoxeterGroup`)

    OUTPUT:

    The class of fully commutative elements in the Coxeter group constructed
    from ``data``. This will belong to the category of enumerated sets. If the
    Coxeter data corresponds to a Cartan type, the category is further refined
    to either finite enumerated sets or infinite enumerated sets depending on
    whether the Coxeter group is FC-finite; the refinement is not carried out
    if ``data`` is a Coxeter matrix not corresponding to a Cartan type.

    .. TODO::

        It would be ideal to implement the aforementioned refinement to finite
        and infinite enumerated sets for all possible ``data``, regardless of
        whether it corresponds to a Cartan type. Doing so requires determining
        if an arbitrary Coxeter matrix corresponds to a Cartan type. It may be
        best to address this issue in ``sage.combinat.root_system``. On the other
        hand, the refinement in the general case may be unnecessary in light of
        the fact that Stembridge's classification of FC-finite groups contains
        a very small number of easily-recognizable families.

    EXAMPLES:

    Create the enumerate set of fully commutative elements in `B_3`::

        sage: FC = CoxeterGroup(['B', 3]).fully_commutative_elements(); FC
        Fully commutative elements of Finite Coxeter group over Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095? with Coxeter matrix:
        [1 3 2]
        [3 1 4]
        [2 4 1]

    Construct elements::

        sage: FC([])
        []
        sage: FC([1,2])
        [1, 2]
        sage: FC([2,3,2])
        [2, 3, 2]
        sage: FC([3,2,3])
        [3, 2, 3]

    Elements are normalized to Cartier--Foata normal form upon construction::

        sage: FC([3,1])
        [1, 3]
        sage: FC([2,3,1])
        [2, 1, 3]
        sage: FC([1,3]) == FC([3,1])
        True

    Attempting to create an element from an input that is not the reduced word
    of a fully commutative element throws a :exc:`ValueError`::

        sage: FC([1,2,1])
        Traceback (most recent call last):
        ...
        ValueError: the input is not a reduced word of a fully commutative element
        sage: FC([2,3,2,3])
        Traceback (most recent call last):
        ...
        ValueError: the input is not a reduced word of a fully commutative element

    Enumerate the FC elements in `A_3`::

        sage: FCA3 = CoxeterGroup(['A', 3]).fully_commutative_elements()
        sage: FCA3.category()
        Category of finite enumerated sets
        sage: FCA3.list()
        [[],
         [1],
         [2],
         [3],
         [2, 1],
         [1, 3],
         [1, 2],
         [3, 2],
         [2, 3],
         [3, 2, 1],
         [2, 1, 3],
         [1, 3, 2],
         [1, 2, 3],
         [2, 1, 3, 2]]

    Count the FC elements in `B_8`::

        sage: FCB8 = CoxeterGroup(['B', 8]).fully_commutative_elements()
        sage: len(FCB8)    # long time (7 seconds)
        14299

    Iterate through the FC elements of length up to 2 in the non-FC-finite group
    affine `A_2`::

        sage: FCAffineA2 = CoxeterGroup(['A', 2, 1]).fully_commutative_elements()
        sage: FCAffineA2.category()
        Category of infinite enumerated sets
        sage: list(FCAffineA2.iterate_to_length(2))
        [[], [0], [1], [2], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2]]

    The cardinality of the set is determined from the classification of
    FC-finite Coxeter groups::

        sage: CoxeterGroup('A2').fully_commutative_elements().category()
        Category of finite enumerated sets
        sage: CoxeterGroup('B7').fully_commutative_elements().category()
        Category of finite enumerated sets
        sage: CoxeterGroup('A3~').fully_commutative_elements().category()
        Category of infinite enumerated sets
        sage: CoxeterGroup('F4~').fully_commutative_elements().category()
        Category of finite enumerated sets
        sage: CoxeterGroup('E8~').fully_commutative_elements().category()
        Category of finite enumerated sets
        sage: CoxeterGroup('F4~xE8~').fully_commutative_elements().category()
        Category of finite enumerated sets
        sage: CoxeterGroup('B4~xE8~').fully_commutative_elements().category()
        Category of infinite enumerated sets
    """
    @staticmethod
    def __classcall_private__(cls, data):
        """
        EXAMPLES::

            sage: from sage.combinat.fully_commutative_elements import FullyCommutativeElements
            sage: x1 = FullyCommutativeElements(CoxeterGroup(['B', 3])); x1
            Fully commutative elements of Finite Coxeter group over Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095? with Coxeter matrix:
            [1 3 2]
            [3 1 4]
            [2 4 1]
            sage: x2 = FullyCommutativeElements(['B', 3]); x2
            Fully commutative elements of Finite Coxeter group over Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095? with Coxeter matrix:
            [1 3 2]
            [3 1 4]
            [2 4 1]
            sage: x3 = FullyCommutativeElements(CoxeterMatrix([[1, 3, 2], [3, 1, 4], [2, 4, 1]])); x3
            Fully commutative elements of Finite Coxeter group over Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095? with Coxeter matrix:
            [1 3 2]
            [3 1 4]
            [2 4 1]
            sage: x1 is x2 is x3
            True
            sage: FullyCommutativeElements(CartanType(['B', 3]).relabel({1: 3, 2: 2, 3: 1}))
            Fully commutative elements of Finite Coxeter group over Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095? with Coxeter matrix:
            [1 4 2]
            [4 1 3]
            [2 3 1]
            sage: m = CoxeterMatrix([(1, 5, 2, 2, 2), (5, 1, 3, 2, 2), (2, 3, 1, 3, 2), (2, 2, 3, 1, 3), (2, 2, 2, 3, 1)]); FullyCommutativeElements(m)
            Fully commutative elements of Coxeter group over Universal Cyclotomic Field with Coxeter matrix:
            [1 5 2 2 2]
            [5 1 3 2 2]
            [2 3 1 3 2]
            [2 2 3 1 3]
            [2 2 2 3 1]
        """
    def __init__(self, coxeter_group) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.fully_commutative_elements import FullyCommutativeElements
            sage: FC = FullyCommutativeElements(CoxeterGroup(['H', 4]))
            sage: TestSuite(FC).run()
        """
    Element = FullyCommutativeElement
    def coxeter_group(self):
        """
        Obtain the Coxeter group associated with ``self``.

        EXAMPLES::

            sage: FCA3 = CoxeterGroup(['A', 3]).fully_commutative_elements()
            sage: FCA3.coxeter_group()
            Finite Coxeter group over Integer Ring with Coxeter matrix:
            [1 3 2]
            [3 1 3]
            [2 3 1]
        """
    def __iter__(self):
        """
        Enumerate the elements of this set by length, starting with the empty
        word and, if the group is FC-finite, ending with the longest fully
        commutative element.

        TESTS::

            sage: FC = CoxeterGroup(['A', 10]).fully_commutative_elements()
            sage: next(iter(FC)) # indirect doctest
            []
        """
    def iterate_to_length(self, length) -> Generator[Incomplete]:
        """
        Iterate through the elements of this class up to a maximum length.

        INPUT:

        - ``length`` -- integer; maximum length of element to generate

        OUTPUT: generator for elements of ``self`` of length up to ``length``

        EXAMPLES:

        The following example produces all FC elements of length up to 2 in the
        group `A_3`::

            sage: FCA3 = CoxeterGroup(['A', 3]).fully_commutative_elements()
            sage: list(FCA3.iterate_to_length(2))
            [[], [1], [2], [3], [2, 1], [1, 3], [1, 2], [3, 2], [2, 3]]

        The lists for length 4 and 5 are the same since 4 is the maximum length
        of an FC element in `A_3`::

            sage: list(FCA3.iterate_to_length(4))
            [[], [1], [2], [3], [2, 1], [1, 3], [1, 2], [3, 2], [2, 3],
             [3, 2, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3], [2, 1, 3, 2]]
            sage: list(FCA3.iterate_to_length(5))
            [[], [1], [2], [3], [2, 1], [1, 3], [1, 2], [3, 2], [2, 3],
             [3, 2, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3], [2, 1, 3, 2]]
            sage: list(FCA3.iterate_to_length(4)) == list(FCA3)
            True

        The following example produces all FC elements of length up to 4 in the
        affine Weyl group `\\tilde A_2`::

            sage: FCAffineA2 = CoxeterGroup(['A', 2, 1]).fully_commutative_elements()
            sage: FCAffineA2.category()
            Category of infinite enumerated sets
            sage: list(FCAffineA2.iterate_to_length(4))
            [[], [0], [1], [2], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2],
             [1, 2], [2, 1, 0], [1, 2, 0], [2, 0, 1], [0, 2, 1], [1, 0, 2],
             [0, 1, 2], [0, 2, 1, 0], [0, 1, 2, 0], [1, 2, 0, 1],
             [1, 0, 2, 1], [2, 1, 0, 2], [2, 0, 1, 2]]
        """
