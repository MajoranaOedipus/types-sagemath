from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.backtrack import GenericBacktracker as GenericBacktracker
from sage.combinat.combinat import CombinatorialObject as CombinatorialObject
from sage.combinat.combination import Combinations as Combinations
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.words.word import Word as Word
from sage.misc.misc_c import prod as prod
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LatticeDiagram(CombinatorialObject):
    def boxes(self):
        """
        EXAMPLES::

            sage: a = LatticeDiagram([3,0,2])
            sage: a.boxes()
            [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2)]
            sage: a = LatticeDiagram([2, 1, 3, 0, 0, 2])
            sage: a.boxes()
            [(1, 1), (1, 2), (2, 1), (3, 1), (3, 2), (3, 3), (6, 1), (6, 2)]
        """
    def __getitem__(self, i):
        """
        Return the `i`-th entry of ``self``.

        Note that the indexing for lattice diagrams starts at `1`.

        EXAMPLES::

            sage: a = LatticeDiagram([3,0,2])
            sage: a[1]
            3
            sage: a[0]
            Traceback (most recent call last):
            ...
            ValueError: indexing starts at 1
            sage: a[-1]
            2
        """
    def leg(self, i, j):
        """
        Return the leg of the box ``(i,j)`` in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.leg(5,2)
            [(5, 3)]
        """
    def arm_left(self, i, j):
        """
        Return the left arm of the box ``(i,j)`` in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.arm_left(5,2)
            [(1, 2), (3, 2)]
        """
    def arm_right(self, i, j):
        """
        Return the right arm of the box ``(i,j)`` in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.arm_right(5,2)
            [(8, 1)]
        """
    def arm(self, i, j):
        """
        Return the arm of the box ``(i,j)`` in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.arm(5,2)
            [(1, 2), (3, 2), (8, 1)]
        """
    def l(self, i, j):
        """
        Return ``self[i] - j``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.l(5,2)
            1
        """
    def a(self, i, j):
        """
        Return the length of the arm of the box ``(i,j)`` in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.a(5,2)
            3
        """
    def size(self):
        """
        Return the number of boxes in ``self``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,1,2,4,3,0,4,2,3])
            sage: a.size()
            22
        """
    def flip(self):
        """
        Return the flip of ``self``, where flip is defined as follows. Let
        ``r = max(self)``. Then ``self.flip()[i] = r - self[i]``.

        EXAMPLES::

            sage: a = LatticeDiagram([3,0,2])
            sage: a.flip()
            [0, 3, 1]
        """
    def boxes_same_and_lower_right(self, ii, jj) -> Generator[Incomplete]:
        """
        Return an iterator of the boxes of ``self`` that are in row ``jj``
        but not identical with ``(ii, jj)``, or lie in the row
        ``jj - 1`` (the row directly below ``jj``; this might be the
        basement) and strictly to the right of ``(ii, jj)``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a = a.shape()
            sage: list(a.boxes_same_and_lower_right(1,1))
            [(2, 1), (3, 1), (6, 1), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
            sage: list(a.boxes_same_and_lower_right(1,2))
            [(3, 2), (6, 2), (2, 1), (3, 1), (6, 1)]
            sage: list(a.boxes_same_and_lower_right(3,3))
            [(6, 2)]
            sage: list(a.boxes_same_and_lower_right(2,3))
            [(3, 3), (3, 2), (6, 2)]
        """

class AugmentedLatticeDiagramFilling(CombinatorialObject):
    def __init__(self, l, pi=None) -> None:
        """
        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a == loads(dumps(a))
            True
            sage: pi = Permutation([2,3,1]).to_permutation_group_element()
            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]],pi)
            sage: a == loads(dumps(a))
            True
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a[0]
            Traceback (most recent call last):
            ...
            ValueError: indexing starts at 1
            sage: a[1,0]
            1
            sage: a[2,0]
            2
            sage: a[3,2]
            4
            sage: a[3][2]
            4
        """
    def shape(self):
        """
        Return the shape of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.shape()
            [2, 1, 3, 0, 0, 2]
        """
    def __contains__(self, ij) -> bool:
        """
        Return ``True`` if the box ``(i,j) (= ij)`` is in ``self``. Note that this
        does not include the basement row.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: (1,1) in a
            True
            sage: (1,0) in a
            False
        """
    def are_attacking(self, i, j, ii, jj):
        """
        Return ``True`` if the boxes ``(i,j)`` and ``(ii,jj)`` in ``self`` are attacking.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: all( a.are_attacking(i,j,ii,jj) for (i,j),(ii,jj) in a.attacking_boxes())
            True
            sage: a.are_attacking(1,1,3,2)
            False
        """
    def boxes(self):
        """
        Return a list of the coordinates of the boxes of ``self``, including
        the 'basement row'.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.boxes()
            [(1, 1),
             (1, 2),
             (2, 1),
             (3, 1),
             (3, 2),
             (3, 3),
             (6, 1),
             (6, 2),
             (1, 0),
             (2, 0),
             (3, 0),
             (4, 0),
             (5, 0),
             (6, 0)]
        """
    def attacking_boxes(self):
        """
        Return a list of pairs of boxes in ``self`` that are attacking.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.attacking_boxes()[:5]
            [((1, 1), (2, 1)),
             ((1, 1), (3, 1)),
             ((1, 1), (6, 1)),
             ((1, 1), (2, 0)),
             ((1, 1), (3, 0))]
        """
    def is_non_attacking(self):
        """
        Return ``True`` if ``self`` is non-attacking.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.is_non_attacking()
            True
            sage: a = AugmentedLatticeDiagramFilling([[1, 1, 1], [2, 3], [3]])
            sage: a.is_non_attacking()
            False
            sage: a = AugmentedLatticeDiagramFilling([[2,2],[1]])
            sage: a.is_non_attacking()
            False
            sage: pi = Permutation([2,1]).to_permutation_group_element()
            sage: a = AugmentedLatticeDiagramFilling([[2,2],[1]],pi)
            sage: a.is_non_attacking()
            True
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.weight()
            [1, 2, 1, 1, 2, 1]
        """
    def descents(self):
        """
        Return a list of the descents of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.descents()
            [(1, 2), (3, 2)]
        """
    def maj(self):
        """
        Return the major index of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.maj()
            3
        """
    def reading_order(self):
        """
        Return a list of coordinates of the boxes in ``self``, starting from
        the top right, and reading from right to left.

        Note that this includes the 'basement row' of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.reading_order()
            [(3, 3),
             (6, 2),
             (3, 2),
             (1, 2),
             (6, 1),
             (3, 1),
             (2, 1),
             (1, 1),
             (6, 0),
             (5, 0),
             (4, 0),
             (3, 0),
             (2, 0),
             (1, 0)]
        """
    def reading_word(self):
        """
        Return the reading word of ``self``, obtained by reading the boxes
        entries of ``self`` from right to left, starting in the upper right.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.reading_word()
            word: 25465321
        """
    def inversions(self):
        """
        Return a list of the inversions of ``self``.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.inversions()[:5]
            [((6, 2), (3, 2)),
             ((1, 2), (6, 1)),
             ((1, 2), (3, 1)),
             ((1, 2), (2, 1)),
             ((6, 1), (3, 1))]
            sage: len(a.inversions())
            25
        """
    def inv(self):
        """
        Return ``self``'s inversion statistic.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.inv()
            15
        """
    def coinv(self):
        """
        Return ``self``'s co-inversion statistic.

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: a.coinv()
            2
        """
    def coeff(self, q, t):
        """
        Return the coefficient in front of ``self`` in the HHL formula for the
        expansion of the non-symmetric Macdonald polynomial
        E(self.shape()).

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: q,t = var('q,t')                                                      # needs sage.symbolic
            sage: a.coeff(q,t)                                                          # needs sage.symbolic
            (t - 1)^4/((q^2*t^3 - 1)^2*(q*t^2 - 1)^2)
        """
    def coeff_integral(self, q, t):
        """
        Return the coefficient in front of ``self`` in the HHL formula for the
        expansion of the integral non-symmetric Macdonald polynomial
        E(self.shape())

        EXAMPLES::

            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: q,t = var('q,t')                                                      # needs sage.symbolic
            sage: a.coeff_integral(q,t)                                                 # needs sage.symbolic
            (q^2*t^3 - 1)^2*(q*t^2 - 1)^2*(t - 1)^4
        """
    def permuted_filling(self, sigma):
        """
        EXAMPLES::

            sage: pi=Permutation([2,1,4,3]).to_permutation_group_element()
            sage: fill=[[2],[1,2,3],[],[3,1]]
            sage: AugmentedLatticeDiagramFilling(fill).permuted_filling(pi)
            [[2, 1], [1, 2, 1, 4], [4], [3, 4, 2]]
        """

def NonattackingFillings(shape, pi=None):
    """
    Returning the finite set of nonattacking fillings of a
    given shape.

    EXAMPLES::

        sage: NonattackingFillings([0,1,2])
        Nonattacking fillings of [0, 1, 2]
        sage: NonattackingFillings([0,1,2]).list()
        [[[1], [2, 1], [3, 2, 1]],
         [[1], [2, 1], [3, 2, 2]],
         [[1], [2, 1], [3, 2, 3]],
         [[1], [2, 1], [3, 3, 1]],
         [[1], [2, 1], [3, 3, 2]],
         [[1], [2, 1], [3, 3, 3]],
         [[1], [2, 2], [3, 1, 1]],
         [[1], [2, 2], [3, 1, 2]],
         [[1], [2, 2], [3, 1, 3]],
         [[1], [2, 2], [3, 3, 1]],
         [[1], [2, 2], [3, 3, 2]],
         [[1], [2, 2], [3, 3, 3]]]
    """

class NonattackingFillings_shape(Parent, UniqueRepresentation):
    pi: Incomplete
    def __init__(self, shape, pi=None) -> None:
        """
        EXAMPLES::

            sage: n = NonattackingFillings([0,1,2])
            sage: n == loads(dumps(n))
            True
        """
    def flip(self):
        """
        Return the nonattacking fillings of the flipped shape.

        EXAMPLES::

            sage: NonattackingFillings([0,1,2]).flip()
            Nonattacking fillings of [2, 1, 0]
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: NonattackingFillings([0,1,2]).list()  #indirect doctest
            [[[1], [2, 1], [3, 2, 1]],
             [[1], [2, 1], [3, 2, 2]],
             [[1], [2, 1], [3, 2, 3]],
             [[1], [2, 1], [3, 3, 1]],
             [[1], [2, 1], [3, 3, 2]],
             [[1], [2, 1], [3, 3, 3]],
             [[1], [2, 2], [3, 1, 1]],
             [[1], [2, 2], [3, 1, 2]],
             [[1], [2, 2], [3, 1, 3]],
             [[1], [2, 2], [3, 3, 1]],
             [[1], [2, 2], [3, 3, 2]],
             [[1], [2, 2], [3, 3, 3]]]
            sage: len(_)
            12

        TESTS::

            sage: NonattackingFillings([3,2,1,1]).cardinality()
            3
            sage: NonattackingFillings([3,2,1,2]).cardinality()
            4
            sage: NonattackingFillings([1,2,3]).cardinality()
            12
            sage: NonattackingFillings([2,2,2]).cardinality()
            1
            sage: NonattackingFillings([1,2,3,2]).cardinality()
            24
        """

class NonattackingBacktracker(GenericBacktracker):
    pi: Incomplete
    def __init__(self, shape, pi=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.sf.ns_macdonald import NonattackingBacktracker
            sage: n = NonattackingBacktracker(LatticeDiagram([0,1,2]))
            sage: n._ending_position
            (3, 2)
            sage: n._initial_state
            (2, 1)
        """
    def get_next_pos(self, ii, jj):
        """
        EXAMPLES::

            sage: from sage.combinat.sf.ns_macdonald import NonattackingBacktracker
            sage: a = AugmentedLatticeDiagramFilling([[1,6],[2],[3,4,2],[],[],[5,5]])
            sage: n = NonattackingBacktracker(a.shape())
            sage: n.get_next_pos(1, 1)
            (2, 1)
            sage: n.get_next_pos(6, 1)
            (1, 2)
            sage: n = NonattackingBacktracker(LatticeDiagram([2,2,2]))
            sage: n.get_next_pos(3, 1)
            (1, 2)
        """

def E(mu, q=None, t=None, pi=None):
    """
    Return the non-symmetric Macdonald polynomial in type A
    corresponding to a shape ``mu``, with basement permuted according to
    ``pi``.

    Note that if both `q` and `t` are specified, then they must have
    the same parent.

    REFERENCE:

    - J. Haglund, M. Haiman, N. Loehr.
      *A combinatorial formula for non-symmetric Macdonald polynomials*.
      :arxiv:`math/0601693v3`.

    .. SEEALSO::

        :class:`~sage.combinat.root_system.non_symmetric_macdonald_polynomials.NonSymmetricMacdonaldPolynomials`
        for a type free implementation where the polynomials are
        constructed recursively by the application of intertwining
        operators.

    EXAMPLES::

        sage: from sage.combinat.sf.ns_macdonald import E
        sage: E([0,0,0])
        1
        sage: E([1,0,0])
        x0
        sage: E([0,1,0])
        (t - 1)/(q*t^2 - 1)*x0 + x1
        sage: E([0,0,1])
        (t - 1)/(q*t - 1)*x0 + (t - 1)/(q*t - 1)*x1 + x2
        sage: E([1,1,0])
        x0*x1
        sage: E([1,0,1])
        (t - 1)/(q*t^2 - 1)*x0*x1 + x0*x2
        sage: E([0,1,1])
        (t - 1)/(q*t - 1)*x0*x1 + (t - 1)/(q*t - 1)*x0*x2 + x1*x2
        sage: E([2,0,0])
        x0^2 + (q*t - q)/(q*t - 1)*x0*x1 + (q*t - q)/(q*t - 1)*x0*x2
        sage: E([0,2,0])
        (t - 1)/(q^2*t^2 - 1)*x0^2 + (q^2*t^3 - q^2*t^2 + q*t^2 - 2*q*t + q - t + 1)/(q^3*t^3 - q^2*t^2 - q*t + 1)*x0*x1 + x1^2 + (q*t^2 - 2*q*t + q)/(q^3*t^3 - q^2*t^2 - q*t + 1)*x0*x2 + (q*t - q)/(q*t - 1)*x1*x2
    """
def E_integral(mu, q=None, t=None, pi=None):
    """
    Return the integral form for the non-symmetric Macdonald
    polynomial in type A corresponding to a shape mu.

    Note that if both q and t are specified, then they must have the
    same parent.

    REFERENCE:

    - J. Haglund, M. Haiman, N. Loehr.
      *A combinatorial formula for non-symmetric Macdonald polynomials*.
      :arxiv:`math/0601693v3`.

    EXAMPLES::

        sage: from sage.combinat.sf.ns_macdonald import E_integral
        sage: E_integral([0,0,0])
        1
        sage: E_integral([1,0,0])
        (-t + 1)*x0
        sage: E_integral([0,1,0])
        (-q*t^2 + 1)*x0 + (-t + 1)*x1
        sage: E_integral([0,0,1])
        (-q*t + 1)*x0 + (-q*t + 1)*x1 + (-t + 1)*x2
        sage: E_integral([1,1,0])
        (t^2 - 2*t + 1)*x0*x1
        sage: E_integral([1,0,1])
        (q*t^3 - q*t^2 - t + 1)*x0*x1 + (t^2 - 2*t + 1)*x0*x2
        sage: E_integral([0,1,1])
        (q^2*t^3 + q*t^4 - q*t^3 - q*t^2 - q*t - t^2 + t + 1)*x0*x1 + (q*t^2 - q*t - t + 1)*x0*x2 + (t^2 - 2*t + 1)*x1*x2
        sage: E_integral([2,0,0])
        (t^2 - 2*t + 1)*x0^2 + (q^2*t^2 - q^2*t - q*t + q)*x0*x1 + (q^2*t^2 - q^2*t - q*t + q)*x0*x2
        sage: E_integral([0,2,0])
        (q^2*t^3 - q^2*t^2 - t + 1)*x0^2 + (q^4*t^3 - q^3*t^2 - q^2*t + q*t^2 - q*t + q - t + 1)*x0*x1 + (t^2 - 2*t + 1)*x1^2 + (q^4*t^3 - q^3*t^2 - q^2*t + q)*x0*x2 + (q^2*t^2 - q^2*t - q*t + q)*x1*x2
    """
def Ht(mu, q=None, t=None, pi=None):
    """
    Return the symmetric Macdonald polynomial using the Haiman,
    Haglund, and Loehr formula.

    Note that if both `q` and `t` are specified, then they must have the
    same parent.

    REFERENCE:

    - J. Haglund, M. Haiman, N. Loehr.
      *A combinatorial formula for non-symmetric Macdonald polynomials*.
      :arxiv:`math/0601693v3`.

    EXAMPLES::

        sage: from sage.combinat.sf.ns_macdonald import Ht
        sage: HHt = SymmetricFunctions(QQ['q','t'].fraction_field()).macdonald().Ht()
        sage: Ht([0,0,1])
        x0 + x1 + x2
        sage: HHt([1]).expand(3)
        x0 + x1 + x2
        sage: Ht([0,0,2])
        x0^2 + (q + 1)*x0*x1 + x1^2 + (q + 1)*x0*x2 + (q + 1)*x1*x2 + x2^2
        sage: HHt([2]).expand(3)
        x0^2 + (q + 1)*x0*x1 + x1^2 + (q + 1)*x0*x2 + (q + 1)*x1*x2 + x2^2
    """
