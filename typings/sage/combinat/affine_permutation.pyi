from _typeshed import Incomplete
from sage.categories.affine_weyl_groups import AffineWeylGroups as AffineWeylGroups
from sage.combinat.composition import Composition as Composition
from sage.combinat.partition import Partition as Partition
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.prandom import randint as randint
from sage.rings.integer import Integer as Integer
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AffinePermutation(ClonableArray):
    """
    An affine permutation, represented in the window notation, and
    considered as a bijection from `\\ZZ` to `\\ZZ`.

    EXAMPLES::

        sage: A = AffinePermutationGroup(['A',7,1])
        sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
        sage: p
        Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]
    """
    k: Incomplete
    n: Incomplete
    N: Incomplete
    def __init__(self, parent, lst, check: bool = True) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``parent`` -- the parent affine permutation group

        - ``lst`` -- list giving the base window of the affine permutation

        - ``check`` -- whether to test if the affine permutation is valid

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p
            Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]
            sage: TestSuite(p).run()

        TESTS:

        Check that :issue:`26436` is fixed::

            sage: A = AffinePermutationGroup(['A',3,1])
            sage: p = A([-3/1,2/1,3/1,8/1])
            sage: q = ~p
            sage: q * p
            Type A affine permutation with window [1, 2, 3, 4]
        """
    def __rmul__(self, q) -> AffinePermutation:
        """
        Given ``self`` and `q`, returns ``self*q``.

        INPUT:

        - ``q`` -- an element of ``self.parent()``

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: q = A([0, 2, 3, 4, 5, 6, 7, 9])
            sage: p.__rmul__(q)
            Type A affine permutation with window [1, -1, 0, 6, 5, 4, 10, 11]
        """
    def __lmul__(self, q) -> AffinePermutation:
        """
        Given ``self`` and `q`, returns ``q*self``.

        INPUT:

        - ``q`` -- an element of ``self.parent()``

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: q = A([0,2,3,4,5,6,7,9])
            sage: p.__lmul__(q)
            Type A affine permutation with window [3, -1, 1, 6, 5, 4, 10, 8]
        """
    def __mul__(self, q) -> AffinePermutation:
        """
        Given ``self`` and `q`, returns ``self*q``.

        INPUT:

        - ``q`` -- an element of ``self.parent()``

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: s1 = AffinePermutationGroup(['A',7,1]).one().apply_simple_reflection(1)
            sage: p * s1
            Type A affine permutation with window [-1, 3, 0, 6, 5, 4, 10, 9]
            sage: p.apply_simple_reflection(1, 'right')
            Type A affine permutation with window [-1, 3, 0, 6, 5, 4, 10, 9]
        """
    @cached_method
    def __invert__(self) -> AffinePermutation:
        """
        Return the inverse affine permutation.

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.inverse()  # indirect doctest
            Type A affine permutation with window [0, -1, 1, 6, 5, 4, 10, 11]
        """
    def apply_simple_reflection(self, i, side: str = 'right') -> AffinePermutation:
        """
        Apply a simple reflection.

        INPUT:

        - ``i`` -- integer
        - ``side`` -- (default: ``'right'``) determines whether to apply the
          reflection on the ``'right'`` or ``'left'``

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.apply_simple_reflection(3)
            Type A affine permutation with window [3, -1, 6, 0, 5, 4, 10, 9]
            sage: p.apply_simple_reflection(11)
            Type A affine permutation with window [3, -1, 6, 0, 5, 4, 10, 9]
            sage: p.apply_simple_reflection(3, 'left')
            Type A affine permutation with window [4, -1, 0, 6, 5, 3, 10, 9]
            sage: p.apply_simple_reflection(11, 'left')
            Type A affine permutation with window [4, -1, 0, 6, 5, 3, 10, 9]
        """
    def __call__(self, i):
        """
        Return the image of the integer ``i`` under this permutation.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.value(1) #indirect doctest
            3
            sage: p.value(9)
            11
        """
    def is_i_grassmannian(self, i: int = 0, side: str = 'right') -> bool:
        """
        Test whether ``self`` is `i`-grassmannian, i.e., either is the
        identity or has ``i`` as the sole descent.

        INPUT:

        - ``i`` -- an element of the index set
        - ``side`` -- determines the side on which to check the descents

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.is_i_grassmannian()
            False
            sage: q = A.from_word([3,2,1,0])
            sage: q.is_i_grassmannian()
            True
            sage: q = A.from_word([2,3,4,5])
            sage: q.is_i_grassmannian(5)
            True
            sage: q.is_i_grassmannian(2, side='left')
            True
        """
    def index_set(self) -> tuple[int, ...]:
        """
        Index set of the affine permutation group.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: A.index_set()
            (0, 1, 2, 3, 4, 5, 6, 7)
        """
    def lower_covers(self, side: str = 'right') -> list[AffinePermutation]:
        """
        Return lower covers of ``self``.

        The set of affine permutations of one less length related by
        multiplication by a simple transposition on the indicated side.
        These are the elements that ``self`` covers in weak order.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.lower_covers()
            [Type A affine permutation with window [-1, 3, 0, 6, 5, 4, 10, 9],
             Type A affine permutation with window [3, -1, 0, 5, 6, 4, 10, 9],
             Type A affine permutation with window [3, -1, 0, 6, 4, 5, 10, 9],
             Type A affine permutation with window [3, -1, 0, 6, 5, 4, 9, 10]]
        """
    def is_one(self) -> bool:
        """
        Test whether the affine permutation is the identity.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.is_one()
            False
            sage: q = A.one()
            sage: q.is_one()
            True
        """
    def reduced_word(self) -> list[int]:
        """
        Return a reduced word for the affine permutation.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.reduced_word()
            [0, 7, 4, 1, 0, 7, 5, 4, 2, 1]
        """
    def signature(self) -> int:
        """
        Signature of the affine permutation, `(-1)^l`, where `l` is the
        length of the permutation.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.signature()
            1
        """
    @cached_method
    def to_weyl_group_element(self):
        """
        The affine Weyl group element corresponding to the affine permutation.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.to_weyl_group_element()
            [ 0 -1  0  1  0  0  1  0]
            [ 1 -1  0  1  0  0  1 -1]
            [ 1 -1  0  1  0  0  0  0]
            [ 0  0  0  1  0  0  0  0]
            [ 0  0  0  1  0 -1  1  0]
            [ 0  0  0  1 -1  0  1  0]
            [ 0  0  0  0  0  0  1  0]
            [ 0 -1  1  0  0  0  1  0]
        """
    def grassmannian_quotient(self, i: int = 0, side: str = 'right') -> tuple:
        """
        Return the Grassmannian quotient.

        Factors ``self`` into a unique product of a Grassmannian and a
        finite-type element.  Returns a tuple containing the Grassmannian
        and finite elements, in order according to ``side``.

        INPUT:

        - ``i`` -- (default: 0) an element of the index set; the descent
          checked for

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: gq=p.grassmannian_quotient()
            sage: gq
            (Type A affine permutation with window [-1, 0, 3, 4, 5, 6, 9, 10],
             Type A affine permutation with window [3, 1, 2, 6, 5, 4, 8, 7])
            sage: gq[0].is_i_grassmannian()
            True
            sage: 0 not in gq[1].reduced_word()
            True
            sage: prod(gq)==p
            True

            sage: gqLeft=p.grassmannian_quotient(side='left')
            sage: 0 not in gqLeft[0].reduced_word()
            True
            sage: gqLeft[1].is_i_grassmannian(side='left')
            True
            sage: prod(gqLeft)==p
            True
        """

class AffinePermutationTypeA(AffinePermutation):
    def check(self) -> None:
        """
        Check that ``self`` is an affine permutation.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p
            Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]
            sage: q = A([1,2,3])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: length of list must be k+1=8
            sage: q = A([1,2,3,4,5,6,7,0])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: window does not sum to 36
            sage: q = A([1,1,3,4,5,6,7,9])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: entries must have distinct residues
        """
    def value(self, i, base_window: bool = False):
        """
        Return the image of the integer ``i`` under this permutation.

        INPUT:

        - ``base_window`` -- boolean; indicating whether ``i`` is in the
          base window; if ``True``, will run a bit faster, but the method
          will screw up if ``i`` is not actually in the index set

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.value(1)
            3
            sage: p.value(9)
            11
        """
    def position(self, i):
        """
        Find the position ``j`` such the ``self.value(j) == i``.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.position(3)
            1
            sage: p.position(11)
            9
        """
    def apply_simple_reflection_right(self, i) -> AffinePermutationTypeA:
        """
        Apply the simple reflection to positions `i`, `i+1`.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.apply_simple_reflection_right(3)
            Type A affine permutation with window [3, -1, 6, 0, 5, 4, 10, 9]
            sage: p.apply_simple_reflection_right(11)
            Type A affine permutation with window [3, -1, 6, 0, 5, 4, 10, 9]
        """
    def apply_simple_reflection_left(self, i) -> AffinePermutationTypeA:
        """
        Apply the simple reflection to the values `i`, `i+1`.

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.apply_simple_reflection_left(3)
            Type A affine permutation with window [4, -1, 0, 6, 5, 3, 10, 9]
            sage: p.apply_simple_reflection_left(11)
            Type A affine permutation with window [4, -1, 0, 6, 5, 3, 10, 9]
        """
    def has_right_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.has_right_descent(1)
            True
            sage: p.has_right_descent(9)
            True
            sage: p.has_right_descent(0)
            False
        """
    def has_left_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.has_left_descent(1)
            True
            sage: p.has_left_descent(9)
            True
            sage: p.has_left_descent(0)
            True
        """
    def to_type_a(self) -> AffinePermutationTypeA:
        """
        Return an embedding of ``self`` into the affine permutation group of
        type `A`.  (For type `A`, just returns ``self``.)

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.to_type_a() is p
            True
        """
    def flip_automorphism(self) -> AffinePermutationTypeA:
        """
        The Dynkin diagram automorphism which fixes `s_0` and reverses all
        other indices.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.flip_automorphism()
            Type A affine permutation with window [0, -1, 5, 4, 3, 9, 10, 6]
        """
    def promotion(self) -> AffinePermutationTypeA:
        """
        The Dynkin diagram automorphism which sends `s_i` to `s_{i+1}`.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.promotion()
            Type A affine permutation with window [2, 4, 0, 1, 7, 6, 5, 11]
        """
    def maximal_cyclic_factor(self, typ: str = 'decreasing', side: str = 'right', verbose: bool = False) -> list:
        """
        For an affine permutation `x`, find the unique maximal subset `A`
        of the index set such that `x = yd_A` is a reduced product.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'``
          (default: ``'decreasing'``); chooses whether to find increasing
          or decreasing sets

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``); chooses
          whether to find maximal sets starting from the left or the right

        - ``verbose`` -- boolean;  if ``True``, outputs information about how
          the cyclically increasing element was found

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.maximal_cyclic_factor()
            [7, 5, 4, 2, 1]
            sage: p.maximal_cyclic_factor(side='left')
            [1, 0, 7, 5, 4]
            sage: p.maximal_cyclic_factor('increasing','right')
            [4, 5, 7, 0, 1]
            sage: p.maximal_cyclic_factor('increasing','left')
            [0, 1, 2, 4, 5]
        """
    def maximal_cyclic_decomposition(self, typ: str = 'decreasing', side: str = 'right', verbose: bool = False):
        """
        Find the unique maximal decomposition of ``self`` into cyclically
        decreasing/increasing elements.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'``
          (default: ``'decreasing'``); chooses whether to find increasing
          or decreasing sets

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``) chooses
          whether to find maximal sets starting from the left or the right

        - ``verbose`` -- boolean (default: ``False``); print extra information
          while finding the decomposition

        EXAMPLES::

            sage: p = AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.maximal_cyclic_decomposition()
            [[0, 7], [4, 1, 0], [7, 5, 4, 2, 1]]
            sage: p.maximal_cyclic_decomposition(side='left')
            [[1, 0, 7, 5, 4], [1, 0, 5], [2, 1]]
            sage: p.maximal_cyclic_decomposition(typ='increasing', side='right')
            [[1], [5, 0, 1, 2], [4, 5, 7, 0, 1]]
            sage: p.maximal_cyclic_decomposition(typ='increasing', side='left')
            [[0, 1, 2, 4, 5], [4, 7, 0, 1], [7]]

        TESTS::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: S = p.maximal_cyclic_decomposition()
            sage: p == prod(A.from_word(l) for l in S)
            True
            sage: S = p.maximal_cyclic_decomposition(typ='increasing', side='left')
            sage: p == prod(A.from_word(l) for l in S)
            True
            sage: S = p.maximal_cyclic_decomposition(typ='increasing', side='right')
            sage: p == prod(A.from_word(l) for l in S)
            True
            sage: S = p.maximal_cyclic_decomposition(typ='decreasing', side='right')
            sage: p == prod(A.from_word(l) for l in S)
            True
        """
    def to_lehmer_code(self, typ: str = 'decreasing', side: str = 'right') -> Composition:
        """
        Return the affine Lehmer code.

        There are four such codes; the options ``typ`` and ``side`` determine
        which code is generated.  The codes generated are the shape of the
        maximal cyclic decompositions of ``self`` according to the given
        ``typ`` and ``side`` options.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'``
          (default: ``'decreasing'``); chooses whether to find increasing
          or decreasing sets

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``) chooses
          whether to find maximal sets starting from the left or the right

        EXAMPLES::

            sage: import itertools
            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: orders = ('increasing','decreasing')
            sage: sides = ('left','right')
            sage: for o,s in itertools.product(orders, sides):
            ....:   p.to_lehmer_code(o,s)
            [2, 3, 2, 0, 1, 2, 0, 0]
            [2, 2, 0, 0, 2, 1, 0, 3]
            [3, 1, 0, 0, 2, 1, 0, 3]
            [0, 3, 3, 0, 1, 2, 0, 1]
            sage: for a in itertools.product(orders, sides):
            ....:   A.from_lehmer_code(p.to_lehmer_code(a[0],a[1]), a[0],a[1])==p
            True
            True
            True
            True
        """
    def is_fully_commutative(self) -> bool:
        """
        Determine whether ``self`` is fully commutative.

        This means that it has no reduced word with a braid.

        This uses a specific algorithm.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.is_fully_commutative()
            False
            sage: q = A([-3, -2, 0, 7, 9, 2, 11, 12])
            sage: q.is_fully_commutative()
            True
        """
    def to_bounded_partition(self, typ: str = 'decreasing', side: str = 'right') -> Partition:
        """
        Return the `k`-bounded partition associated to the dominant element
        obtained by sorting the Lehmer code.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'`` (default: ``'decreasing'``);
          chooses whether to find increasing or decreasing sets

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``); chooses
          whether to find maximal sets starting from the left or the right

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',2,1])
            sage: p = A.from_lehmer_code([4,1,0])
            sage: p.to_bounded_partition()
            [2, 1, 1, 1]
        """
    def to_core(self, typ: str = 'decreasing', side: str = 'right'):
        """
        Return the core associated to the dominant element obtained by sorting
        the Lehmer code.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'`` (default: ``'decreasing'``.)

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``.)  Chooses whether to
          find maximal sets starting from the left or the right

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',2,1])
            sage: p = A.from_lehmer_code([4,1,0])
            sage: p.to_bounded_partition()
            [2, 1, 1, 1]
            sage: p.to_core()
            [4, 2, 1, 1]
        """
    def to_dominant(self, typ: str = 'decreasing', side: str = 'right') -> AffinePermutationTypeA:
        """
        Find the Lehmer code and then sort it. Return the affine permutation
        with the given sorted Lehmer code.

        This element is 0-dominant.

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'``
          (default: ``'decreasing'``) chooses whether to find increasing
          or decreasing sets

        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``) chooses
          whether to find maximal sets starting from the left or the right

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.to_dominant()
            Type A affine permutation with window [-2, -1, 1, 3, 4, 8, 10, 13]
            sage: p.to_dominant(typ='increasing', side='left')
            Type A affine permutation with window [3, 4, -1, 5, 0, 9, 6, 10]
        """
    def tableau_of_word(self, w, typ: str = 'decreasing', side: str = 'right', alpha=None):
        """
        Finds a tableau on the Lehmer code of ``self`` corresponding
        to the given reduced word.

        For a full description of this algorithm, see [Den2012]_.

        INPUT:

        - ``w`` -- a reduced word for ``self``
        - ``typ`` -- ``'increasing'`` or ``'decreasing'``; the type of
          Lehmer code used
        - ``side`` -- ``'right'`` or ``'left'``
        - ``alpha`` -- a content vector; ``w`` should be of type ``alpha``;
          specifying ``alpha`` produces semistandard tableaux

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.tableau_of_word(p.reduced_word())
            [[], [1, 6, 9], [2, 7, 10], [], [3], [4, 8], [], [5]]
            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: w = p.reduced_word(); w
            [0, 7, 4, 1, 0, 7, 5, 4, 2, 1]
            sage: alpha = [5,3,2]
            sage: p.tableau_of_word(p.reduced_word(), alpha=alpha)
            [[], [1, 2, 3], [1, 2, 3], [], [1], [1, 2], [], [1]]
            sage: p.tableau_of_word(p.reduced_word(), side='left')
            [[1, 4, 9], [6], [], [], [3, 7], [8], [], [2, 5, 10]]
            sage: p.tableau_of_word(p.reduced_word(), typ='increasing', side='right')
            [[9, 10], [1, 2], [], [], [3, 4], [8], [], [5, 6, 7]]
            sage: p.tableau_of_word(p.reduced_word(), typ='increasing', side='left')
            [[1, 2], [4, 5, 6], [9, 10], [], [3], [7, 8], [], []]
        """

class AffinePermutationTypeC(AffinePermutation):
    def check(self) -> None:
        """
        Check that ``self`` is an affine permutation.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: x
            Type C affine permutation with window [-1, 5, 3, 7]
        """
    def value(self, i):
        """
        Return the image of the integer ``i`` under this permutation.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C.one()
            sage: all(x.value(i) == i for i in range(-10,10))
            True
        """
    def position(self, i):
        """
        Find the position `j` such the ``self.value(j)=i``.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C.one()
            sage: all(x.position(i) == i for i in range(-10,10))
            True
        """
    def apply_simple_reflection_right(self, i) -> AffinePermutationTypeC:
        """
        Apply the simple reflection indexed by ``i`` on positions.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: for i in C.index_set(): x.apply_simple_reflection_right(i)
            Type C affine permutation with window [1, 5, 3, 7]
            Type C affine permutation with window [5, -1, 3, 7]
            Type C affine permutation with window [-1, 3, 5, 7]
            Type C affine permutation with window [-1, 5, 7, 3]
            Type C affine permutation with window [-1, 5, 3, 2]
        """
    def apply_simple_reflection_left(self, i) -> AffinePermutationTypeC:
        """
        Apply the simple reflection indexed by ``i`` on values.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: for i in C.index_set(): x.apply_simple_reflection_left(i)
            Type C affine permutation with window [1, 5, 3, 7]
            Type C affine permutation with window [-2, 5, 3, 8]
            Type C affine permutation with window [-1, 5, 2, 6]
            Type C affine permutation with window [-1, 6, 4, 7]
            Type C affine permutation with window [-1, 4, 3, 7]
        """
    def has_right_descent(self, i) -> bool:
        """
        Determine whether there is a descent at index ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: for i in C.index_set(): x.has_right_descent(i)
            True
            False
            True
            False
            True
        """
    def has_left_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: for i in C.index_set(): x.has_left_descent(i)
            True
            False
            True
            False
            True
        """
    def to_type_a(self) -> AffinePermutationTypeA:
        """
        Return an embedding of ``self`` into the affine permutation group of
        type `A`.

        EXAMPLES::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: x = C([-1,5,3,7])
            sage: x.to_type_a()
            Type A affine permutation with window [-1, 5, 3, 7, 2, 6, 4, 10, 9]
        """

class AffinePermutationTypeB(AffinePermutationTypeC):
    def check(self) -> None:
        """
        Check that ``self`` is an affine permutation.

        EXAMPLES::

            sage: B = AffinePermutationGroup(['B',4,1])
            sage: x = B([-5,1,6,-2])
            sage: x
            Type B affine permutation with window [-5, 1, 6, -2]
        """
    def apply_simple_reflection_right(self, i) -> AffinePermutationTypeB:
        """
        Apply the simple reflection indexed by ``i`` on positions.

        EXAMPLES::

            sage: B = AffinePermutationGroup(['B',4,1])
            sage: p = B([-5,1,6,-2])
            sage: p.apply_simple_reflection_right(1)
            Type B affine permutation with window [1, -5, 6, -2]
            sage: p.apply_simple_reflection_right(0)
            Type B affine permutation with window [-1, 5, 6, -2]
            sage: p.apply_simple_reflection_right(4)
            Type B affine permutation with window [-5, 1, 6, 11]
        """
    def apply_simple_reflection_left(self, i) -> AffinePermutationTypeB:
        """
        Apply the simple reflection indexed by ``i`` on values.

        EXAMPLES::

            sage: B = AffinePermutationGroup(['B',4,1])
            sage: p = B([-5,1,6,-2])
            sage: p.apply_simple_reflection_left(0)
            Type B affine permutation with window [-5, -2, 6, 1]
            sage: p.apply_simple_reflection_left(2)
            Type B affine permutation with window [-5, 1, 7, -3]
            sage: p.apply_simple_reflection_left(4)
            Type B affine permutation with window [-4, 1, 6, -2]
        """
    def has_right_descent(self, i) -> bool:
        """
        Determine whether there is a descent at index ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: B = AffinePermutationGroup(['B',4,1])
            sage: p = B([-5,1,6,-2])
            sage: [p.has_right_descent(i) for i in B.index_set()]
            [True, False, False, True, False]
        """
    def has_left_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: B = AffinePermutationGroup(['B',4,1])
            sage: p = B([-5,1,6,-2])
            sage: [p.has_left_descent(i) for i in B.index_set()]
            [True, True, False, False, True]
        """

class AffinePermutationTypeD(AffinePermutationTypeC):
    def check(self) -> None:
        """
        Check that ``self`` is an affine permutation.

        EXAMPLES::

            sage: D = AffinePermutationGroup(['D',4,1])
            sage: p = D([1,-6,5,-2])
            sage: p
            Type D affine permutation with window [1, -6, 5, -2]
        """
    def apply_simple_reflection_right(self, i) -> AffinePermutationTypeD:
        """
        Apply the simple reflection indexed by ``i`` on positions.

        EXAMPLES::

            sage: D = AffinePermutationGroup(['D',4,1])
            sage: p = D([1,-6,5,-2])
            sage: p.apply_simple_reflection_right(0)
            Type D affine permutation with window [6, -1, 5, -2]
            sage: p.apply_simple_reflection_right(1)
            Type D affine permutation with window [-6, 1, 5, -2]
            sage: p.apply_simple_reflection_right(4)
            Type D affine permutation with window [1, -6, 11, 4]
        """
    def apply_simple_reflection_left(self, i) -> AffinePermutationTypeD:
        """
        Apply simple reflection indexed by ``i`` on values.

        EXAMPLES::

            sage: D = AffinePermutationGroup(['D',4,1])
            sage: p = D([1,-6,5,-2])
            sage: p.apply_simple_reflection_left(0)
            Type D affine permutation with window [-2, -6, 5, 1]
            sage: p.apply_simple_reflection_left(1)
            Type D affine permutation with window [2, -6, 5, -1]
            sage: p.apply_simple_reflection_left(4)
            Type D affine permutation with window [1, -4, 3, -2]
        """
    def has_right_descent(self, i) -> bool:
        """
        Determine whether there is a descent at index ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: D = AffinePermutationGroup(['D',4,1])
            sage: p = D([1,-6,5,-2])
            sage: [p.has_right_descent(i) for i in D.index_set()]
            [True, True, False, True, False]
        """
    def has_left_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: D = AffinePermutationGroup(['D',4,1])
            sage: p = D([1,-6,5,-2])
            sage: [p.has_left_descent(i) for i in D.index_set()]
            [True, True, False, True, True]
        """

class AffinePermutationTypeG(AffinePermutation):
    def check(self) -> None:
        """
        Check that ``self`` is an affine permutation.

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: p
            Type G affine permutation with window [2, 10, -5, 12, -3, 5]
        """
    def value(self, i, base_window: bool = False):
        """
        Return the image of the integer ``i`` under this permutation.

        INPUT:

        - ``base_window`` -- boolean indicating whether ``i`` is between 1 and
          `k+1`; if ``True``, will run a bit faster, but the method will screw
          up if ``i`` is not actually in the index set

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: [p.value(i) for i in [1..12]]
            [2, 10, -5, 12, -3, 5, 8, 16, 1, 18, 3, 11]
        """
    def position(self, i):
        """
        Find the position ``j`` such the ``self.value(j) == i``.

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: [p.position(i) for i in p]
            [1, 2, 3, 4, 5, 6]
        """
    def apply_simple_reflection_right(self, i) -> AffinePermutationTypeG:
        """
        Apply the simple reflection indexed by ``i`` on positions.

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: p.apply_simple_reflection_right(0)
            Type G affine permutation with window [-9, -1, -5, 12, 8, 16]
            sage: p.apply_simple_reflection_right(1)
            Type G affine permutation with window [10, 2, 12, -5, 5, -3]
            sage: p.apply_simple_reflection_right(2)
            Type G affine permutation with window [2, -5, 10, -3, 12, 5]
        """
    def apply_simple_reflection_left(self, i) -> AffinePermutationTypeG:
        """
        Apply simple reflection indexed by `i` on values.

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: p.apply_simple_reflection_left(0)
            Type G affine permutation with window [0, 10, -7, 14, -3, 7]
            sage: p.apply_simple_reflection_left(1)
            Type G affine permutation with window [1, 9, -4, 11, -2, 6]
            sage: p.apply_simple_reflection_left(2)
            Type G affine permutation with window [3, 11, -5, 12, -4, 4]
        """
    def has_right_descent(self, i) -> bool:
        """
        Determine whether there is a descent at index `i`.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: [p.has_right_descent(i) for i in G.index_set()]
            [False, False, True]
        """
    def has_left_descent(self, i) -> bool:
        """
        Determine whether there is a descent at ``i``.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: [p.has_left_descent(i) for i in G.index_set()]
            [False, True, False]
        """
    def to_type_a(self) -> AffinePermutationTypeA:
        """
        Return an embedding of ``self`` into the affine permutation group of
        type A.

        EXAMPLES::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: p = G([2, 10, -5, 12, -3, 5])
            sage: p.to_type_a()
            Type A affine permutation with window [2, 10, -5, 12, -3, 5]
        """

def AffinePermutationGroup(cartan_type):
    """
    Wrapper function for specific affine permutation groups.

    These are combinatorial implementations of the affine Weyl groups of
    types `A`, `B`, `C`, `D`, and `G` as permutations of the set of all integers.
    the basic algorithms are derived from [BB2005]_ and [Eri1995]_.

    EXAMPLES::

        sage: ct = CartanType(['A',7,1])
        sage: A = AffinePermutationGroup(ct)
        sage: A
        The group of affine permutations of type ['A', 7, 1]

    We define an element of ``A``::

        sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
        sage: p
        Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]

    We find the value `p(1)`, considering `p` as a bijection on the integers.
    This is the same as calling the
    :meth:`~sage.combinat.affine_permutation.AffinePermutation.value` method::

        sage: p.value(1)
        3
        sage: p(1) == p.value(1)
        True

    We can also find the position of the integer 3 in `p` considered as a
    sequence, equivalent to finding `p^{-1}(3)`::

        sage: p.position(3)
        1
        sage: (p^-1)(3)
        1

    Since the affine permutation group is a group, we demonstrate its
    group properties::

        sage: A.one()
        Type A affine permutation with window [1, 2, 3, 4, 5, 6, 7, 8]

        sage: q = A([0, 2, 3, 4, 5, 6, 7, 9])
        sage: p * q
        Type A affine permutation with window [1, -1, 0, 6, 5, 4, 10, 11]
        sage: q * p
        Type A affine permutation with window [3, -1, 1, 6, 5, 4, 10, 8]

        sage: p^-1
        Type A affine permutation with window [0, -1, 1, 6, 5, 4, 10, 11]
        sage: p^-1 * p == A.one()
        True
        sage: p * p^-1 == A.one()
        True

    If we decide we prefer the Weyl Group implementation of the affine Weyl
    group, we can easily get it::

        sage: p.to_weyl_group_element()
        [ 0 -1  0  1  0  0  1  0]
        [ 1 -1  0  1  0  0  1 -1]
        [ 1 -1  0  1  0  0  0  0]
        [ 0  0  0  1  0  0  0  0]
        [ 0  0  0  1  0 -1  1  0]
        [ 0  0  0  1 -1  0  1  0]
        [ 0  0  0  0  0  0  1  0]
        [ 0 -1  1  0  0  0  1  0]

    We can find a reduced word and do all of the other things one expects in
    a Coxeter group::

        sage: p.has_right_descent(1)
        True
        sage: p.apply_simple_reflection(1)
        Type A affine permutation with window [-1, 3, 0, 6, 5, 4, 10, 9]
        sage: p.apply_simple_reflection(0)
        Type A affine permutation with window [1, -1, 0, 6, 5, 4, 10, 11]
        sage: p.reduced_word()
        [0, 7, 4, 1, 0, 7, 5, 4, 2, 1]
        sage: p.length()
        10

    The following methods are particular to type `A`.
    We can check if the element is fully commutative::

        sage: p.is_fully_commutative()
        False
        sage: q.is_fully_commutative()
        True

    We can also compute the affine Lehmer code of the permutation,
    a weak composition with `k + 1` entries::

        sage: p.to_lehmer_code()
        [0, 3, 3, 0, 1, 2, 0, 1]

    Once we have the Lehmer code, we can obtain a `k`-bounded partition by
    sorting the Lehmer code, and then reading the row lengths.
    There is a unique 0-Grassmanian (dominant) affine permutation associated
    to this `k`-bounded partition, and a `k`-core as well. ::

        sage: p.to_bounded_partition()
        [5, 3, 2]
        sage: p.to_dominant()
        Type A affine permutation with window [-2, -1, 1, 3, 4, 8, 10, 13]
        sage: p.to_core()
        [5, 3, 2]

    Finally, we can take a reduced word for `p` and insert it to find a
    standard composition tableau associated uniquely to that word::

        sage: p.tableau_of_word(p.reduced_word())
        [[], [1, 6, 9], [2, 7, 10], [], [3], [4, 8], [], [5]]

    We can also form affine permutation groups in types `B`, `C`, `D`,
    and `G`::

        sage: B = AffinePermutationGroup(['B',4,1])
        sage: B.an_element()
        Type B affine permutation with window [-1, 3, 4, 11]

        sage: C = AffinePermutationGroup(['C',4,1])
        sage: C.an_element()
        Type C affine permutation with window [2, 3, 4, 10]

        sage: D = AffinePermutationGroup(['D',4,1])
        sage: D.an_element()
        Type D affine permutation with window [-1, 3, 11, 5]

        sage: G = AffinePermutationGroup(['G',2,1])
        sage: G.an_element()
        Type G affine permutation with window [0, 4, -1, 8, 3, 7]
    """

class AffinePermutationGroupGeneric(UniqueRepresentation, Parent):
    """
    The generic affine permutation group class, in which we define all type-free
    methods for the specific affine permutation groups.

    TESTS::

        sage: AffinePermutationGroup(['A',7,1])([3, -1, 0, 6, 5, 4, 10, 9])
        Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]
    """
    k: Incomplete
    n: Incomplete
    N: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        TESTS::

            sage: AffinePermutationGroup(['A',7,1])
            The group of affine permutations of type ['A', 7, 1]
        """
    def weyl_group(self):
        """
        Return the Weyl Group of the same type as ``self``.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: A.weyl_group()
            Weyl Group of type ['A', 7, 1] (as a matrix group acting on the root space)
        """
    def classical(self):
        """
        Return the finite permutation group.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: A.classical()
            Symmetric group of order 8! as a permutation group
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).cartan_type()
            ['A', 7, 1]
        """
    def cartan_matrix(self):
        """
        Return the Cartan matrix of ``self``.

        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).cartan_matrix()
            [ 2 -1  0  0  0  0  0 -1]
            [-1  2 -1  0  0  0  0  0]
            [ 0 -1  2 -1  0  0  0  0]
            [ 0  0 -1  2 -1  0  0  0]
            [ 0  0  0 -1  2 -1  0  0]
            [ 0  0  0  0 -1  2 -1  0]
            [ 0  0  0  0  0 -1  2 -1]
            [-1  0  0  0  0  0 -1  2]
        """
    def is_crystallographic(self) -> bool:
        """
        Tell whether the affine permutation group is crystallographic.

        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).is_crystallographic()
            True
        """
    def index_set(self):
        """
        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).index_set()
            (0, 1, 2, 3, 4, 5, 6, 7)
        """
    def reflection_index_set(self):
        """
        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).reflection_index_set()
            (0, 1, 2, 3, 4, 5, 6, 7)
        """
    def rank(self):
        """
        Rank of the affine permutation group, equal to `k+1`.

        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).rank()
            8
        """
    def random_element(self, n=None) -> AffinePermutation:
        """
        Return a random affine permutation of length ``n``.

        If ``n`` is not specified, then ``n`` is chosen as a random
        nonnegative integer in `[0, 1000]`.

        Starts at the identity, then chooses an upper cover at random.
        Not very uniform: actually constructs a uniformly random reduced word
        of length `n`.  Thus we most likely get elements with lots of reduced
        words!

        For the actual code, see
        :meth:`sage.categories.coxeter_group.random_element_of_length`.

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: A.random_element() # random
            Type A affine permutation with window [-12, 16, 19, -1, -2, 10, -3, 9]
            sage: p = A.random_element(10)
            sage: p.length() == 10
            True
        """
    def from_word(self, w) -> AffinePermutation:
        """
        Build an affine permutation from a given word.
        Note: Already in category as ``from_reduced_word``, but this is less
        typing!

        EXAMPLES::

            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: A.from_word([0, 7, 4, 1, 0, 7, 5, 4, 2, 1])
            Type A affine permutation with window [3, -1, 0, 6, 5, 4, 10, 9]
        """

class AffinePermutationGroupTypeA(AffinePermutationGroupGeneric):
    @cached_method
    def one(self) -> AffinePermutation:
        """
        Return the identity element.

        EXAMPLES::

            sage: AffinePermutationGroup(['A',7,1]).one()
            Type A affine permutation with window [1, 2, 3, 4, 5, 6, 7, 8]

        TESTS::

            sage: A = AffinePermutationGroup(['A',5,1])
            sage: A == loads(dumps(A))
            True
            sage: TestSuite(A).run()
        """
    def from_lehmer_code(self, C, typ: str = 'decreasing', side: str = 'right') -> AffinePermutation:
        """
        Return the affine permutation with the supplied Lehmer code (a weak
        composition with `k+1` parts, at least one of which is 0).

        INPUT:

        - ``typ`` -- ``'increasing'`` or ``'decreasing'``
          (default: ``'decreasing'``); type of product
        - ``side`` -- ``'right'`` or ``'left'`` (default: ``'right'``);
          whether the decomposition is from the right or left

        EXAMPLES::

            sage: import itertools
            sage: A = AffinePermutationGroup(['A',7,1])
            sage: p = A([3, -1, 0, 6, 5, 4, 10, 9])
            sage: p.to_lehmer_code()
            [0, 3, 3, 0, 1, 2, 0, 1]
            sage: A.from_lehmer_code(p.to_lehmer_code()) == p
            True
            sage: orders = ('increasing','decreasing')
            sage: sides = ('left','right')
            sage: all(A.from_lehmer_code(p.to_lehmer_code(o,s),o,s) == p
            ....:     for o,s in itertools.product(orders,sides))
            True
        """
    Element = AffinePermutationTypeA

class AffinePermutationGroupTypeC(AffinePermutationGroupGeneric):
    @cached_method
    def one(self) -> AffinePermutation:
        """
        Return the identity element.

        EXAMPLES::

            sage: ct = CartanType(['C',4,1])
            sage: C = AffinePermutationGroup(ct)
            sage: C.one()
            Type C affine permutation with window [1, 2, 3, 4]
            sage: C.one()*C.one()==C.one()
            True

        TESTS::

            sage: C = AffinePermutationGroup(['C',4,1])
            sage: C == loads(dumps(C))
            True
            sage: TestSuite(C).run()
        """
    Element = AffinePermutationTypeC

class AffinePermutationGroupTypeB(AffinePermutationGroupTypeC):
    Element = AffinePermutationTypeB

class AffinePermutationGroupTypeD(AffinePermutationGroupTypeC):
    Element = AffinePermutationTypeD

class AffinePermutationGroupTypeG(AffinePermutationGroupGeneric):
    @cached_method
    def one(self) -> AffinePermutation:
        """
        Return the identity element.

        EXAMPLES::

            sage: AffinePermutationGroup(['G',2,1]).one()
            Type G affine permutation with window [1, 2, 3, 4, 5, 6]

        TESTS::

            sage: G = AffinePermutationGroup(['G',2,1])
            sage: G == loads(dumps(G))
            True
            sage: TestSuite(G).run()
        """
    Element = AffinePermutationTypeG
