from _typeshed import Incomplete
from collections.abc import Iterator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.dyck_word import DyckWord as DyckWord
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.prandom import randint as randint
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_a(x, n=None) -> bool:
    """
    Check whether a list is a parking function.

    If a size `n` is specified, checks if a list is a parking function
    of size `n`.

    TESTS::

        sage: from sage.combinat.parking_functions import is_a
        sage: is_a([1,1,2])
        True
        sage: is_a([1,2,1])
        True
        sage: is_a([1,1,4])
        False
        sage: is_a([3,1,1], 3)
        True
    """

class ParkingFunction(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    A Parking Function.

    A *parking function* of size `n` is a sequence `(a_1, \\ldots,a_n)`
    of positive integers such that if `b_1 \\leq b_2 \\leq \\cdots \\leq b_n` is
    the increasing rearrangement of `a_1, \\ldots, a_n`, then `b_i \\leq i`.

    A *parking function* of size `n` is a pair `(L, D)` of two sequences
    `L` and `D` where `L` is a permutation and `D` is an area sequence
    of a Dyck Path of size `n` such that `D[i] \\geq 0`, `D[i+1] \\leq D[i]+1`
    and if `D[i+1] = D[i]+1` then `L[i+1] > L[i]`.

    The number of parking functions of size `n` is equal to the number
    of rooted forests on `n` vertices and is equal to `(n+1)^{n-1}`.

    INPUT:

    - ``pf`` -- (default: ``None``) a list whose increasing rearrangement
      satisfies `b_i \\leq i`

    - ``labelling`` -- (default: ``None``) a labelling of the Dyck path

    - ``area_sequence`` -- (default: ``None``) an area sequence of a Dyck path

    - ``labelled_dyck_word`` -- (default: ``None``) a Dyck word with 1s
      replaced by labelling

    OUTPUT: a parking function

    EXAMPLES::

        sage: ParkingFunction([])
        []
        sage: ParkingFunction([1])
        [1]
        sage: ParkingFunction([2])
        Traceback (most recent call last):
        ...
        ValueError: [2] is not a parking function
        sage: ParkingFunction([1,2])
        [1, 2]
        sage: ParkingFunction([1,1,2])
        [1, 1, 2]
        sage: ParkingFunction([1,4,1])
        Traceback (most recent call last):
        ...
        ValueError: [1, 4, 1] is not a parking function
        sage: ParkingFunction(labelling=[3,1,2], area_sequence=[0,0,1])
        [2, 2, 1]
        sage: ParkingFunction([2,2,1]).to_labelled_dyck_word()
        [3, 0, 1, 2, 0, 0]
        sage: ParkingFunction(labelled_dyck_word=[3,0,1,2,0,0])
        [2, 2, 1]
        sage: ParkingFunction(labelling=[3,1,2], area_sequence=[0,1,1])
        Traceback (most recent call last):
        ...
        ValueError: [3, 1, 2] is not a valid labeling of area sequence [0, 1, 1]
    """
    @staticmethod
    def __classcall_private__(cls, pf=None, labelling=None, area_sequence=None, labelled_dyck_word=None):
        """
        Construct a parking function based on the input.

        TESTS::

            sage: PF = ParkingFunction([1,2])
            sage: isinstance(PF, ParkingFunctions().element_class)
            True
        """
    def __init__(self, parent, lst) -> None:
        """
        TESTS::

            sage: ParkingFunction([1, 1, 2, 2, 5, 6])
            [1, 1, 2, 2, 5, 6]

            sage: PF = ParkingFunction([1, 1, 2, 2, 5, 6])
            sage: PF[0]
            1
            sage: PF[2]
            2

            sage: PF4 = ParkingFunctions(4)
            sage: a = PF4.list()[36]
            sage: b = PF4([1,3,2,1])
            sage: type(a)
            <class 'sage.combinat.parking_functions.ParkingFunctions_n_with_category.element_class'>
            sage: type(b)
            <class 'sage.combinat.parking_functions.ParkingFunctions_n_with_category.element_class'>

        Some checks for more general inputs::

            sage: PF = ParkingFunction((1, 1, 2, 2, 5, 6))
            sage: PF = ParkingFunction(Permutation([4,2,3,1]))
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid parking function.

        EXAMPLES::

            sage: PF = ParkingFunction([1, 1, 2, 2, 5, 6])
            sage: PF.check()
        """
    def grade(self):
        """
        Return the length of the parking function.

        EXAMPLES::

            sage: PF = ParkingFunction([1, 1, 2, 2, 5, 6])
            sage: PF.grade()
            6
        """
    def __call__(self, n):
        """
        Return the image of ``n`` under the parking function.

        EXAMPLES::

            sage: PF = ParkingFunction([1, 1, 2, 2, 5, 6])
            sage: PF(3)
            2
            sage: PF(6)
            6
        """
    def diagonal_reading_word(self) -> Permutation:
        """
        Return a diagonal word of the labelled Dyck path corresponding to parking
        function (see [Hag08]_ p. 75).

        OUTPUT:

        - returns a word, read diagonally from NE to SW of the pretty
          print of the labelled Dyck path that corresponds to ``self``
          and the same size as ``self``

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.diagonal_reading_word()
            [5, 1, 7, 4, 6, 3, 2]

        ::

            sage: ParkingFunction([1, 1, 1]).diagonal_reading_word()
            [3, 2, 1]
            sage: ParkingFunction([1, 2, 3]).diagonal_reading_word()
            [3, 2, 1]
            sage: ParkingFunction([1, 1, 3, 4]).diagonal_reading_word()
            [2, 4, 3, 1]

        ::

            sage: ParkingFunction([1, 1, 1]).diagonal_word()
            [3, 2, 1]
            sage: ParkingFunction([1, 2, 3]).diagonal_word()
            [3, 2, 1]
            sage: ParkingFunction([1, 4, 3, 1]).diagonal_word()
            [4, 2, 3, 1]
        """
    diagonal_word = diagonal_reading_word
    def parking_permutation(self) -> Permutation:
        """
        Return the sequence of parking spots that are taken by cars 1
        through `n` and corresponding to the parking function.

        For example, ``parking_permutation(PF) = [6, 1, 5, 2, 3, 4,
        7]`` means that spot 6 is taken by car 1, spot 1 by car 2,
        spot 5 by car 3, spot 2 is taken by car 4, spot 3 is taken by
        car 5, spot 4 is taken by car 6 and spot 7 is taken by car 7.

        OUTPUT:

        - the permutation of parking spots that corresponds to
          the parking function and which is the same size as parking
          function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.parking_permutation()
            [6, 1, 5, 2, 3, 4, 7]

        ::

            sage: ParkingFunction([3,1,1,4]).parking_permutation()
            [3, 1, 2, 4]
            sage: ParkingFunction([4,1,1,1]).parking_permutation()
            [4, 1, 2, 3]
            sage: ParkingFunction([2,1,4,1]).parking_permutation()
            [2, 1, 4, 3]
        """
    def cars_permutation(self) -> Permutation:
        """
        Return the sequence of cars that take parking spots 1 through `n`
        and corresponding to the parking function.

        For example, ``cars_permutation(PF) = [2, 4, 5, 6, 3, 1, 7]``
        means that car 2 takes spots 1, car 4 takes spot 2, ..., car 1
        takes spot 6 and car 7 takes spot 7.

        OUTPUT:

        - the permutation of cars corresponding to the parking function
          and which is the same size as parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.cars_permutation()
            [2, 4, 5, 6, 3, 1, 7]

        ::

            sage: ParkingFunction([3,1,1,4]).cars_permutation()
            [2, 3, 1, 4]
            sage: ParkingFunction([4,1,1,1]).cars_permutation()
            [2, 3, 4, 1]
            sage: ParkingFunction([2,1,4,1]).cars_permutation()
            [2, 1, 4, 3]
        """
    def jump_list(self) -> list:
        """
        Return the displacements of cars that corresponds to the parking function.

        For example, ``jump_list(PF) = [0, 0, 0, 0, 1, 3, 2]``
        means that car 1 through 4 parked in their preferred spots,
        car 5 had to park one spot farther (jumped or was displaced by one
        spot), car 6 had to jump 3 spots, and car 7 had to jump two spots.

        OUTPUT:

        - the displacements sequence of parked cars which corresponds
          to the parking function and which is the same size as parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.jump_list()
            [0, 0, 0, 0, 1, 3, 2]

        ::

            sage: ParkingFunction([3,1,1,4]).jump_list()
            [0, 0, 1, 0]
            sage: ParkingFunction([4,1,1,1]).jump_list()
            [0, 0, 1, 2]
            sage: ParkingFunction([2,1,4,1]).jump_list()
            [0, 0, 0, 2]
        """
    def jump(self) -> Integer:
        """
        Return the sum of the differences between the parked and
        preferred parking spots.

        See [Shin]_ p. 18.

        OUTPUT:

        - the sum of the differences between the parked and preferred parking
          spots

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.jump()
            6

        ::

            sage: ParkingFunction([3,1,1,4]).jump()
            1
            sage: ParkingFunction([4,1,1,1]).jump()
            3
            sage: ParkingFunction([2,1,4,1]).jump()
            2
        """
    def lucky_cars(self):
        """
        Return the cars that can park in their preferred spots.  For example,
        ``lucky_cars(PF) = [1, 2, 7]`` means that cars 1, 2 and 7 parked in
        their preferred spots and all the other cars did not.

        OUTPUT: the cars that can park in their preferred spots

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.lucky_cars()
            [1, 2, 3, 4]

        ::

            sage: ParkingFunction([3,1,1,4]).lucky_cars()
            [1, 2, 4]
            sage: ParkingFunction([4,1,1,1]).lucky_cars()
            [1, 2]
            sage: ParkingFunction([2,1,4,1]).lucky_cars()
            [1, 2, 3]
        """
    def luck(self) -> Integer:
        """
        Return the number of cars that parked in their preferred parking spots
        (see [Shin]_ p. 33).

        OUTPUT: the number of cars that parked in their preferred parking spots

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.luck()
            4

        ::

            sage: ParkingFunction([3,1,1,4]).luck()
            3
            sage: ParkingFunction([4,1,1,1]).luck()
            2
            sage: ParkingFunction([2,1,4,1]).luck()
            3
        """
    def primary_dinversion_pairs(self) -> list[tuple[int, int]]:
        """
        Return the primary descent inversion pairs of a labelled Dyck path
        corresponding to the parking function.

        OUTPUT:

        The pairs `(i, j)` such that `i < j`, and `i`-th area = `j`-th area,
        and `i`-th label < `j`-th label

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.primary_dinversion_pairs()
            [(0, 4), (1, 5), (2, 5)]

        ::

            sage: ParkingFunction([3,1,1,4]).primary_dinversion_pairs()
            [(0, 3), (2, 3)]
            sage: ParkingFunction([4,1,1,1]).primary_dinversion_pairs()
            []
            sage: ParkingFunction([2,1,4,1]).primary_dinversion_pairs()
            [(0, 3)]
        """
    def secondary_dinversion_pairs(self) -> list[tuple[int, int]]:
        """
        Return the secondary descent inversion pairs of a labelled Dyck path
        corresponding to the parking function.

        OUTPUT:

        The pairs `(i, j)` such that `i < j`, and `i`-th area = `j`-th area +1,
        and `i`-th label > `j`-th label

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.secondary_dinversion_pairs()
            [(1, 4), (2, 4), (3, 6)]

        ::

            sage: ParkingFunction([3,1,1,4]).secondary_dinversion_pairs()
            [(1, 2)]
            sage: ParkingFunction([4,1,1,1]).secondary_dinversion_pairs()
            [(1, 3)]
            sage: ParkingFunction([2,1,4,1]).secondary_dinversion_pairs()
            [(1, 3)]
        """
    def dinversion_pairs(self) -> list[tuple[int, int]]:
        """
        Return the descent inversion pairs of a labelled Dyck path
        corresponding to the parking function.

        OUTPUT: the primary and secondary diversion pairs

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.dinversion_pairs()
            [(0, 4), (1, 5), (2, 5), (1, 4), (2, 4), (3, 6)]

        ::

            sage: ParkingFunction([3,1,1,4]).dinversion_pairs()
            [(0, 3), (2, 3), (1, 2)]
            sage: ParkingFunction([4,1,1,1]).dinversion_pairs()
            [(1, 3)]
            sage: ParkingFunction([2,1,4,1]).dinversion_pairs()
            [(0, 3), (1, 3)]
        """
    def dinv(self) -> int:
        """
        Return the number of inversions of a labelled Dyck path corresponding
        to the parking function (see [Hag08]_ p. 74).

        Same as the cardinality of :meth:`dinversion_pairs`.

        OUTPUT: the number of dinversion pairs

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.dinv()
            6

        ::

            sage: ParkingFunction([3,1,1,4]).dinv()
            3
            sage: ParkingFunction([4,1,1,1]).dinv()
            1
            sage: ParkingFunction([2,1,4,1]).dinv()
            2
        """
    def area(self) -> Integer:
        """
        Return the area of the labelled Dyck path corresponding to the
        parking function.

        OUTPUT:

        - the sum of squares under and over the main diagonal the Dyck Path,
          corresponding to the parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.area()
            6

        ::

            sage: ParkingFunction([3,1,1,4]).area()
            1
            sage: ParkingFunction([4,1,1,1]).area()
            3
            sage: ParkingFunction([2,1,4,1]).area()
            2
        """
    def ides_composition(self):
        """
        Return the
        :meth:`~sage.combinat.permutation.Permutation.descents_composition`
        of the inverse of the :meth:`diagonal_reading_word` of
        corresponding parking function.

        For example, ``ides_composition(PF) = [4, 2, 1]`` means that
        the descents of the inverse of the permutation
        :meth:`diagonal_reading_word` of the parking function with
        word ``PF`` are at the 4th and 6th positions.

        OUTPUT:

        - the descents composition of the inverse of the
          :meth:`diagonal_reading_word` of the parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.ides_composition()
            [2, 1, 1, 2, 1]

        ::

            sage: ParkingFunction([3,1,1,4]).ides_composition()
            [2, 2]
            sage: ParkingFunction([4,1,1,1]).ides_composition()
            [2, 1, 1]
            sage: ParkingFunction([4,3,1,1]).ides_composition()
            [3, 1]
        """
    def ides(self):
        """
        Return the :meth:`~sage.combinat.permutation.Permutation.descents`
        sequence of the inverse of the :meth:`diagonal_reading_word`
        of ``self``.

        .. WARNING::

            Here we use the standard convention that descent labels
            start at `1`. This behaviour has been changed in
            :issue:`20555`.

        For example, ``ides(PF) = [2, 3, 4, 6]`` means that descents are at
        the 2nd, 3rd, 4th and 6th positions in the inverse of the
        :meth:`diagonal_reading_word` of the parking function (see [GXZ]_ p. 2).

        OUTPUT:

        - the descents sequence of the inverse of the
          :meth:`diagonal_reading_word` of the parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.ides()
            [2, 3, 4, 6]

        ::

            sage: ParkingFunction([3,1,1,4]).ides()
            [2]
            sage: ParkingFunction([4,1,1,1]).ides()
            [2, 3]
            sage: ParkingFunction([4,3,1,1]).ides()
            [3]
        """
    def touch_points(self):
        """
        Return the sequence of touch points which corresponds to the
        labelled Dyck path after initial step.

        For example, ``touch_points(PF) = [4, 7]`` means that after
        the initial step, the path touches the main diagonal at points
        `(4, 4)` and `(7, 7)`.

        OUTPUT:

        - the sequence of touch points after the initial step of the
          labelled Dyck path that corresponds to the parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.touch_points()
            [4, 7]

        ::

            sage: ParkingFunction([3,1,1,4]).touch_points()
            [2, 3, 4]
            sage: ParkingFunction([4,1,1,1]).touch_points()
            [3, 4]
            sage: ParkingFunction([2,1,4,1]).touch_points()
            [3, 4]
        """
    def touch_composition(self):
        """
        Return the composition of the labelled Dyck path corresponding
        to the parking function.

        For example, ``touch_composition(PF) = [4, 3]`` means that the
        first touch is four diagonal units from the starting point,
        and the second is three units further (see [GXZ]_ p. 2).

        OUTPUT:

        - the length between the corresponding touch points which
          of the labelled Dyck path that corresponds to the parking function

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.touch_composition()
            [4, 3]

        ::

            sage: ParkingFunction([3,1,1,4]).touch_composition()
            [2, 1, 1]
            sage: ParkingFunction([4,1,1,1]).touch_composition()
            [3, 1]
            sage: ParkingFunction([2,1,4,1]).touch_composition()
            [3, 1]
        """
    diagonal_composition = touch_composition
    def to_labelling_permutation(self) -> Permutation:
        """
        Return the labelling of the support Dyck path of the parking function.

        OUTPUT: the labelling of the Dyck path

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_labelling_permutation()
            [2, 6, 4, 5, 3, 7, 1]

        ::

            sage: ParkingFunction([3,1,1,4]).to_labelling_permutation()
            [2, 3, 1, 4]
            sage: ParkingFunction([4,1,1,1]).to_labelling_permutation()
            [2, 3, 4, 1]
            sage: ParkingFunction([2,1,4,1]).to_labelling_permutation()
            [2, 4, 1, 3]
        """
    def to_area_sequence(self) -> list:
        """
        Return the area sequence of the support Dyck path of the
        parking function.

        OUTPUT: the area sequence of the Dyck path

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_area_sequence()
            [0, 1, 1, 2, 0, 1, 1]

        ::

            sage: ParkingFunction([3,1,1,4]).to_area_sequence()
            [0, 1, 0, 0]
            sage: ParkingFunction([4,1,1,1]).to_area_sequence()
            [0, 1, 2, 0]
            sage: ParkingFunction([2,1,4,1]).to_area_sequence()
            [0, 1, 1, 0]
        """
    def to_labelling_area_sequence_pair(self):
        """
        Return a pair consisting of a labelling and an area sequence
        of a Dyck path which corresponds to the given parking
        function.

        OUTPUT:

        - returns a pair ``(L, D)`` where ``L`` is a labelling and ``D`` is the
          area sequence of the underlying Dyck path

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_labelling_area_sequence_pair()
            ([2, 6, 4, 5, 3, 7, 1], [0, 1, 1, 2, 0, 1, 1])

        ::

            sage: ParkingFunction([1, 1, 1]).to_labelling_area_sequence_pair()
            ([1, 2, 3], [0, 1, 2])
            sage: ParkingFunction([1, 2, 3]).to_labelling_area_sequence_pair()
            ([1, 2, 3], [0, 0, 0])
            sage: ParkingFunction([1, 1, 2]).to_labelling_area_sequence_pair()
            ([1, 2, 3], [0, 1, 1])
            sage: ParkingFunction([1, 1, 3, 1]).to_labelling_area_sequence_pair()
            ([1, 2, 4, 3], [0, 1, 2, 1])
        """
    def to_dyck_word(self) -> DyckWord:
        """
        Return the support Dyck word of the parking function.

        OUTPUT: the Dyck word of the corresponding parking function

        .. SEEALSO:: :meth:`DyckWord`

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_dyck_word()
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]

        ::

            sage: ParkingFunction([3,1,1,4]).to_dyck_word()
            [1, 1, 0, 0, 1, 0, 1, 0]
            sage: ParkingFunction([4,1,1,1]).to_dyck_word()
            [1, 1, 1, 0, 0, 0, 1, 0]
            sage: ParkingFunction([2,1,4,1]).to_dyck_word()
            [1, 1, 0, 1, 0, 0, 1, 0]
        """
    def to_labelled_dyck_word(self):
        """
        Return the labelled Dyck word corresponding to the parking function.

        This is a representation of the parking function as a list
        where the entries of 1 in the Dyck word are replaced with the
        corresponding label.

        OUTPUT:

        - the labelled Dyck word of the corresponding parking function
          which is twice the size of parking function word

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_labelled_dyck_word()
            [2, 6, 0, 4, 5, 0, 0, 0, 3, 7, 0, 1, 0, 0]

        ::

            sage: ParkingFunction([3,1,1,4]).to_labelled_dyck_word()
            [2, 3, 0, 0, 1, 0, 4, 0]
            sage: ParkingFunction([4,1,1,1]).to_labelled_dyck_word()
            [2, 3, 4, 0, 0, 0, 1, 0]
            sage: ParkingFunction([2,1,4,1]).to_labelled_dyck_word()
            [2, 4, 0, 1, 0, 0, 3, 0]
        """
    def to_labelling_dyck_word_pair(self) -> tuple[Permutation, DyckWord]:
        """
        Return the pair ``(L, D)`` where ``L`` is a labelling and
        ``D`` is the Dyck word of the parking function.

        OUTPUT:

        - the pair ``(L, D)``, where ``L`` is the labelling and ``D`` is
          the Dyck word of the parking function

        .. SEEALSO:: :meth:`DyckWord`

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_labelling_dyck_word_pair()
            ([2, 6, 4, 5, 3, 7, 1], [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0])

        ::

            sage: ParkingFunction([3,1,1,4]).to_labelling_dyck_word_pair()
            ([2, 3, 1, 4], [1, 1, 0, 0, 1, 0, 1, 0])
            sage: ParkingFunction([4,1,1,1]).to_labelling_dyck_word_pair()
            ([2, 3, 4, 1], [1, 1, 1, 0, 0, 0, 1, 0])
            sage: ParkingFunction([2,1,4,1]).to_labelling_dyck_word_pair()
            ([2, 4, 1, 3], [1, 1, 0, 1, 0, 0, 1, 0])
        """
    def to_NonDecreasingParkingFunction(self) -> PF:
        """
        Return the non-decreasing parking function which underlies the
        parking function.

        OUTPUT: a sorted parking function

        .. SEEALSO:: :meth:`NonDecreasingParkingFunction`

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.to_NonDecreasingParkingFunction()
            [1, 1, 2, 2, 5, 5, 6]

        ::

            sage: ParkingFunction([3,1,1,4]).to_NonDecreasingParkingFunction()
            [1, 1, 3, 4]
            sage: ParkingFunction([4,1,1,1]).to_NonDecreasingParkingFunction()
            [1, 1, 1, 4]
            sage: ParkingFunction([2,1,4,1]).to_NonDecreasingParkingFunction()
            [1, 1, 2, 4]
            sage: ParkingFunction([4,1,2,1]).to_NonDecreasingParkingFunction()
            [1, 1, 2, 4]
        """
    def characteristic_quasisymmetric_function(self, q=None, R=...):
        """
        Return the characteristic quasisymmetric function of ``self``.

        The characteristic function of the Parking Function is the sum
        over all permutation labellings of the Dyck path `q^{dinv(PF)}
        F_{ides(PF)}` where `ides(PF)` (:meth:`ides_composition`) is
        the descent composition of diagonal reading word of the
        parking function.

        INPUT:

        - ``q`` -- (default: ``q = R('q')``) a parameter for the
          generating function power

        - ``R`` -- (default: ``R = QQ['q','t'].fraction_field()``) the
          base ring to do the calculations over

        OUTPUT: an element of the quasisymmetric functions over the ring ``R``

        EXAMPLES::

            sage: # needs sage.modules
            sage: R = QQ['q','t'].fraction_field()
            sage: (q,t) = R.gens()
            sage: cqf = sum(t**PF.area() * PF.characteristic_quasisymmetric_function()
            ....:           for PF in ParkingFunctions(3)); cqf
            (q^3+q^2*t+q*t^2+t^3+q*t)*F[1, 1, 1] + (q^2+q*t+t^2+q+t)*F[1, 2]
             + (q^2+q*t+t^2+q+t)*F[2, 1] + F[3]
            sage: s = SymmetricFunctions(R).s()
            sage: s(cqf.to_symmetric_function())
            (q^3+q^2*t+q*t^2+t^3+q*t)*s[1, 1, 1] + (q^2+q*t+t^2+q+t)*s[2, 1] + s[3]
            sage: s(cqf.to_symmetric_function()).nabla(power=-1)
            s[1, 1, 1]

        ::

            sage: p = ParkingFunction([3, 1, 2])
            sage: p.characteristic_quasisymmetric_function()                            # needs sage.modules
            q*F[2, 1]
            sage: pf = ParkingFunction([1,2,7,2,1,2,3,2,1])
            sage: pf.characteristic_quasisymmetric_function()                           # needs sage.modules
            q^2*F[1, 1, 1, 2, 1, 3]
        """
    def pretty_print(self, underpath: bool = True) -> None:
        """
        Displays a parking function as a lattice path consisting of a
        Dyck path and a labelling with the labels displayed along the
        edges of the Dyck path.

        INPUT:

        - ``underpath`` -- if the length of the parking function is
          less than or equal to 9 then display the labels under the
          path if ``underpath`` is ``True`` otherwise display them to the
          right of the path (default: ``True``)

        EXAMPLES::

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.pretty_print()
                       ___
                     _|1x
                    |7x  .
               _____|3 . .
              |5x x  . . .
             _|4x  . . . .
            |6x  . . . . .
            |2 . . . . . .

            sage: PF = ParkingFunction([6, 1, 5, 2, 2, 1, 5])
            sage: PF.pretty_print(underpath = false)
                       ___
                     _| x  1
                    | x  . 7
               _____|  . . 3
              | x x  . . . 5
             _| x  . . . . 4
            | x  . . . . . 6
            |  . . . . . . 2

        ::

            sage: ParkingFunction([3, 1, 1, 4]).pretty_print()
                   _
                 _|4
             ___|1 .
            |3x  . .
            |2 . . .

            sage: ParkingFunction([1,1,1]).pretty_print()
             _____
            |3x x
            |2x  .
            |1 . .

            sage: ParkingFunction([4,1,1,1]).pretty_print()
                   _
             _____|1
            |4x x  .
            |3x  . .
            |2 . . .

            sage: ParkingFunction([2,1,4,1]).pretty_print()
                   _
               ___|3
             _|1x  .
            |4x  . .
            |2 . . .

            sage: ParkingFunction([2,1,4,1]).pretty_print(underpath = false)
                   _
               ___|  3
             _| x  . 1
            | x  . . 4
            |  . . . 2

            sage: pf = ParkingFunction([1,2,3,7,3,2,1,2,3,2,1])
            sage: pf.pretty_print()
                         _________
                 _______| x x x x   4
                | x x x x x x x  .  9
                | x x x x x x  . .  5
               _| x x x x x  . . .  3
              | x x x x x  . . . . 10
              | x x x x  . . . . .  8
              | x x x  . . . . . .  6
             _| x x  . . . . . . .  2
            | x x  . . . . . . . . 11
            | x  . . . . . . . . .  7
            |  . . . . . . . . . .  1
        """
PF = ParkingFunction

def from_labelling_and_area_sequence(L, D) -> PF:
    """
    Return the parking function corresponding to the labelling area
    sequence pair.

    INPUT:

    - ``L`` -- a labelling permutation

    - ``D`` -- an area sequence for a Dyck word

    OUTPUT:

    - the parking function corresponding the labelling permutation ``L``
      and ``D`` an area sequence of the corresponding Dyck path

    EXAMPLES::

        sage: from sage.combinat.parking_functions import from_labelling_and_area_sequence
        sage: from_labelling_and_area_sequence([2, 6, 4, 5, 3, 7, 1], [0, 1, 1, 2, 0, 1, 1])
        [6, 1, 5, 2, 2, 1, 5]

    ::

        sage: from_labelling_and_area_sequence([1, 2, 3], [0, 1, 2])
        [1, 1, 1]
        sage: from_labelling_and_area_sequence([1, 2, 3], [0, 0, 0])
        [1, 2, 3]
        sage: from_labelling_and_area_sequence([1, 2, 3], [0, 1, 1])
        [1, 1, 2]
        sage: from_labelling_and_area_sequence([1, 2, 4, 3], [0, 1, 2, 1])
        [1, 1, 3, 1]

    TESTS::

        sage: PF = from_labelling_and_area_sequence([1, 2, 4, 3], [0, 1, 2, 1])
        sage: isinstance(PF, ParkingFunctions().element_class)
        True
    """
def from_labelled_dyck_word(LDW) -> PF:
    """
    Return the parking function corresponding to the labelled Dyck word.

    INPUT:

    - ``LDW`` -- labelled Dyck word

    OUTPUT:

    - the parking function corresponding to the labelled Dyck
      word that is half the size of ``LDW``

    EXAMPLES::

        sage: from sage.combinat.parking_functions import from_labelled_dyck_word
        sage: LDW = [2, 6, 0, 4, 5, 0, 0, 0, 3, 7, 0, 1, 0, 0]
        sage: from_labelled_dyck_word(LDW)
        [6, 1, 5, 2, 2, 1, 5]

    ::

        sage: from_labelled_dyck_word([2, 3, 0, 0, 1, 0, 4, 0])
        [3, 1, 1, 4]
        sage: from_labelled_dyck_word([2, 3, 4, 0, 0, 0, 1, 0])
        [4, 1, 1, 1]
        sage: from_labelled_dyck_word([2, 4, 0, 1, 0, 0, 3, 0])
        [2, 1, 4, 1]
    """

class ParkingFunctions(UniqueRepresentation, Parent):
    """
    Return the combinatorial class of Parking Functions.

    A *parking function* of size `n` is a sequence `(a_1, \\ldots,a_n)`
    of positive integers such that if `b_1 \\leq b_2 \\leq \\cdots \\leq b_n` is
    the increasing rearrangement of `a_1, \\ldots, a_n`, then `b_i \\leq i`.

    A *parking function* of size `n` is a pair `(L, D)` of two sequences
    `L` and `D` where `L` is a permutation and `D` is an area sequence
    of a Dyck Path of size n such that `D[i] \\geq 0`, `D[i+1] \\leq D[i]+1`
    and if `D[i+1] = D[i]+1` then `L[i+1] > L[i]`.

    The number of parking functions of size `n` is equal to the number
    of rooted forests on `n` vertices and is equal to `(n+1)^{n-1}`.

    EXAMPLES:

    Here are all parking functions of size 3::

        sage: from sage.combinat.parking_functions import ParkingFunctions
        sage: ParkingFunctions(3).list()
        [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1, 3], [1, 3, 1],
         [3, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1], [1, 2, 3], [1, 3, 2],
         [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    If no size is specified, then ParkingFunctions returns the
    combinatorial class of all parking functions. ::

        sage: PF = ParkingFunctions(); PF
        Parking functions
        sage: [] in PF
        True
        sage: [1] in PF
        True
        sage: [2] in PF
        False
        sage: [1,3,1] in PF
        True
        sage: [1,4,1] in PF
        False

    If the size `n` is specified, then ParkingFunctions returns
    the combinatorial class of all parking functions of size `n`.

    ::

        sage: PF = ParkingFunctions(0)
        sage: PF.list()
        [[]]
        sage: PF = ParkingFunctions(1)
        sage: PF.list()
        [[1]]
        sage: PF = ParkingFunctions(3)
        sage: PF.list()
        [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1, 3],
         [1, 3, 1], [3, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1],
         [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    ::

        sage: PF3 = ParkingFunctions(3); PF3
        Parking functions of size 3
        sage: [] in PF3
        False
        sage: [1] in PF3
        False
        sage: [1,3,1] in PF3
        True
        sage: [1,4,1] in PF3
        False

    TESTS::

        sage: PF = ParkingFunctions(5)
        sage: TestSuite(PF).run()
        sage: len(PF.list()) == PF.cardinality()
        True
    """
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        Return the correct parent based on input.

        TESTS::

            sage: type(ParkingFunctions(5))
            <class 'sage.combinat.parking_functions.ParkingFunctions_n_with_category'>
            sage: type(ParkingFunctions())
            <class 'sage.combinat.parking_functions.ParkingFunctions_all_with_category'>
        """

class ParkingFunctions_all(ParkingFunctions):
    def __init__(self) -> None:
        """
        TESTS::

            sage: PF = ParkingFunctions()
            sage: TestSuite(PF).run()
        """
    Element = ParkingFunction
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [] in ParkingFunctions()
            True
            sage: [1] in ParkingFunctions()
            True
            sage: [2] in ParkingFunctions()
            False
            sage: [1,3,1] in ParkingFunctions()
            True
            sage: [1,4,1] in ParkingFunctions()
            False
        """
    def graded_component(self, n):
        """
        Return the graded component.

        EXAMPLES::

            sage: PF = ParkingFunctions()
            sage: PF.graded_component(4) == ParkingFunctions(4)
            True
            sage: it = iter(ParkingFunctions()) # indirect doctest
            sage: [next(it) for i in range(8)]
            [[], [1], [1, 1], [1, 2], [2, 1], [1, 1, 1], [1, 1, 2], [1, 2, 1]]
        """
    def __iter__(self) -> Iterator:
        """
        Return an iterator.

        TESTS::

            sage: it = iter(ParkingFunctions()) # indirect doctest
            sage: [next(it) for i in range(8)]
            [[], [1], [1, 1], [1, 2], [2, 1], [1, 1, 1], [1, 1, 2], [1, 2, 1]]
        """

class ParkingFunctions_n(ParkingFunctions):
    """
    The combinatorial class of parking functions of size `n`.

    A *parking function* of size `n` is a sequence `(a_1, \\ldots,a_n)`
    of positive integers such that if `b_1 \\leq b_2 \\leq \\cdots \\leq b_n` is
    the increasing rearrangement of `a_1, \\ldots, a_n`, then `b_i \\leq i`.

    A *parking function* of size `n` is a pair `(L, D)` of two sequences
    `L` and `D` where `L` is a permutation and `D` is an area sequence
    of a Dyck Path of size `n` such that `D[i] \\geq 0`, `D[i+1] \\leq D[i]+1`
    and if `D[i+1] = D[i]+1` then `L[i+1] > L[i]`.

    The number of parking functions of size `n` is equal to the number
    of rooted forests on `n` vertices and is equal to `(n+1)^{n-1}`.

    EXAMPLES::

        sage: PF = ParkingFunctions(3)
        sage: PF.list()
        [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1, 3],
        [1, 3, 1], [3, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1],
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        sage: [ParkingFunctions(i).cardinality() for i in range(6)]
        [1, 1, 3, 16, 125, 1296]

    .. WARNING::

        The precise order in which the parking function are generated or
        listed is not fixed, and may change in the future.

    TESTS:

    Check that :issue:`15216` is fixed::

        sage: PF = ParkingFunctions()
        sage: PF3 = ParkingFunctions(3)
        sage: [1,1,1] in PF3
        True
        sage: PF3([1,1,1]) in PF3
        True
        sage: PF3([1,1,1]) in PF
        True
        sage: PF([1,1,1]) in PF
        True
        sage: PF3(PF3([1,1,1]))
        [1, 1, 1]
    """
    n: Incomplete
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: PF = ParkingFunctions(3)
            sage: TestSuite(PF).run()
        """
    Element = ParkingFunction
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: PF3 = ParkingFunctions(3); PF3
            Parking functions of size 3
            sage: [] in PF3
            False
            sage: [1] in PF3
            False
            sage: [1,3,1] in PF3
            True
            sage: [1,1,1] in PF3
            True
            sage: [1,4,1] in PF3
            False
            sage: ParkingFunction([1,2]) in PF3
            False
            sage: all(p in PF3 for p in PF3)
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the number of parking functions of size ``n``.

        The cardinality is equal to `(n+1)^{n-1}`.

        EXAMPLES::

            sage: [ParkingFunctions(i).cardinality() for i in range(6)]
            [1, 1, 3, 16, 125, 1296]
        """
    def __iter__(self) -> Iterator:
        """
        Return an iterator for parking functions of size `n`.

        .. WARNING::

            The precise order in which the parking function are
            generated is not fixed, and may change in the future.

        EXAMPLES::

            sage: PF = ParkingFunctions(0)
            sage: [e for e in PF]      # indirect doctest
            [[]]
            sage: PF = ParkingFunctions(1)
            sage: [e for e in PF]      # indirect doctest
            [[1]]
            sage: PF = ParkingFunctions(2)
            sage: [e for e in PF]      # indirect doctest
            [[1, 1], [1, 2], [2, 1]]
            sage: PF = ParkingFunctions(3)
            sage: [e for e in PF]      # indirect doctest
            [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1, 3],
            [1, 3, 1], [3, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1],
            [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        TESTS::

            sage: PF = ParkingFunctions(5)
            sage: [e for e in PF] == PF.list()
            True
            sage: PF = ParkingFunctions(6)
            sage: [e for e in PF] == PF.list()
            True
        """
    def random_element(self) -> PF:
        """
        Return a random parking function of size `n`.

        The algorithm uses a circular parking space with `n+1`
        spots. Then all `n` cars can park and there remains one empty
        spot. Spots are then renumbered so that the empty spot is `0`.

        The probability distribution is uniform on the set of
        `(n+1)^{n-1}` parking functions of size `n`.

        EXAMPLES::

            sage: pf = ParkingFunctions(8)
            sage: a = pf.random_element(); a  # random
            [5, 7, 2, 4, 2, 5, 1, 3]
            sage: a in pf
            True
        """
