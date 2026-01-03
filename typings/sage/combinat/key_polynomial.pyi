r"""
Key and Atom Polynomials

Key polynomials (also known as type A Demazure characters) are defined by
applying the divided difference operator `\pi_{\sigma}`, where `\sigma` is
a permutation, to a monomial corresponding to an integer partition
`\mu \vdash n`.

.. SEEALSO::

    For Demazure characters in other types, see

    - :meth:`sage.combinat.root_system.weyl_characters.WeylCharacterRing.demazure_character`
    - :meth:`sage.categories.classical_crystals.ClassicalCrystals.ParentMethods.demazure_character`

Atom polynomials (also known as Demazure atoms) are defined analogously by
using a deformed divided difference operator `\bar{\pi}_i = \pi_i - 1`.

AUTHORS:

- Trevor K. Karn (2022-08-17): initial version
- Travis Scrimshaw (2025-10-10): expanded to atoms
"""
from _typeshed import Incomplete
from typing import Any, Self, SupportsIndex
from collections.abc import Iterable
from typings_sagemath import StrictlyComparable, ElementWithGens, Int
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialGen
from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial_sparse
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.integer import Integer
from sage.combinat.schubert_polynomial import SchubertPolynomial_class

from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.permutation import Permutation as Permutation
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing as InfinitePolynomialRing, InfinitePolynomialRing_sparse as InfinitePolynomialRing_sparse

from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_commutative as PolynomialRing_commutative
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import parent as parent

def sorting_word[Item: StrictlyComparable](
        alpha: Iterable[Item]) -> tuple[list[int], list[Item]]:
    """
    Get a reduced word for the permutation which sorts ``alpha``
    into a partition.

    The result is a list ``l = [i0, i1, i2, ...]`` where each ``ij``
    is a positive integer such that it applies the simple
    transposition `(i_j, i_j+1)`. The transpositions are applied
    starting with ``i0``, then ``i1`` is applied, followed by ``i2``,
    and so on. See :meth:`sage.combinat.permutation.Permutation.reduced_words`
    for the convention used.

    EXAMPLES::

        sage: IV = IntegerVectors()
        sage: from sage.combinat.key_polynomial import sorting_word
        sage: list(sorting_word(IV([2,3,2]))[0])
        [1]
        sage: sorting_word(IV([2,3,2]))[1]
        [3, 2, 2]
        sage: list(sorting_word(IV([5,6,7]))[0])
        [1, 2, 1]
        sage: list(sorting_word(IV([0,3,2]))[0])
        [2, 1]
        sage: list(sorting_word(IV([0,3,0,2]))[0])
        [2, 3, 1]
        sage: list(sorting_word(IV([3,2,1]))[0])
        []
        sage: list(sorting_word(IV([2,3,3]))[0])
        [2, 1]
    """
    ...

def divided_difference(
        f: InfinitePolynomial_sparse | ElementWithGens, i: SupportsIndex
    ) -> MPolynomial | InfinitePolynomial_sparse:
    """
    Apply the ``i``-th divided difference operator to the polynomial ``f``.

    EXAMPLES::

        sage: from sage.combinat.key_polynomial import divided_difference
        sage: k = KeyPolynomials(QQ)
        sage: z = k.poly_gens()
        sage: f = z[1]*z[2]^3 + z[1]*z[2]*z[3]
        sage: divided_difference(f, 3)
        z_3^2*z_1 + z_3*z_2*z_1 + z_2^2*z_1

        sage: k = KeyPolynomials(QQ, 4)
        sage: z = k.poly_gens()
        sage: f = z[1]*z[2]^3 + z[1]*z[2]*z[3]
        sage: divided_difference(f, 3)
        z_1*z_2^2 + z_1*z_2*z_3 + z_1*z_3^2

        sage: k = KeyPolynomials(QQ)
        sage: R = k.polynomial_ring(); R
        Infinite polynomial ring in z over Rational Field
        sage: z = R.gen()
        sage: divided_difference(z[1]*z[2]^3, 2)
        -z_2^2*z_1 - z_2*z_1^2
        sage: divided_difference(z[1]*z[2]*z[3], 3)
        0
        sage: divided_difference(z[1]*z[2]*z[3], 4)
        z_2*z_1
        sage: divided_difference(z[1]*z[2]*z[4], 4)
        -z_2*z_1

        sage: k = KeyPolynomials(QQ, 5)
        sage: z = k.polynomial_ring().gens()
        sage: divided_difference(z[1]*z[2]^3, 2)
        -z_1^2*z_2 - z_1*z_2^2
        sage: divided_difference(z[1]*z[2]*z[3], 3)
        0
        sage: divided_difference(z[1]*z[2]*z[3], 4)
        z_1*z_2
        sage: divided_difference(z[1]*z[2]*z[4], 4)
        -z_1*z_2
    """

def isobaric_divided_difference(
        f: InfinitePolynomial_sparse | ElementWithGens, 
        w: SupportsIndex | Iterable[SupportsIndex]) -> MPolynomial | InfinitePolynomial_sparse:
    """
    Apply the isobaric divided difference operator `\\pi_w` to the
    polynomial `f`.

    ``w`` may be either a single index or a list of
    indices of simple transpositions.

    .. WARNING::

        The simple transpositions should be applied from left to right.

    EXAMPLES::

        sage: from sage.combinat.key_polynomial import isobaric_divided_difference as idd
        sage: R.<z> = InfinitePolynomialRing(GF(3))
        sage: idd(z[1]^4*z[2]^2*z[4], 4)
        0

        sage: idd(z[1]^4*z[2]^2*z[3]*z[4], 3)
        z_4*z_3^2*z_2*z_1^4 + z_4*z_3*z_2^2*z_1^4

        sage: idd(z[1]^4*z[2]^2*z[3]*z[4], [3, 4])
        z_4^2*z_3*z_2*z_1^4 + z_4*z_3^2*z_2*z_1^4 + z_4*z_3*z_2^2*z_1^4

        sage: idd(z[1]^4*z[2]^2*z[3]*z[4], [4, 3])
        z_4*z_3^2*z_2*z_1^4 + z_4*z_3*z_2^2*z_1^4

        sage: idd(z[1]^2*z[2], [3, 2])
        z_3*z_2^2 + z_3*z_2*z_1 + z_3*z_1^2 + z_2^2*z_1 + z_2*z_1^2
    """

def isobaric_divided_difference_bar(
        f: InfinitePolynomial_sparse | ElementWithGens, 
        w: SupportsIndex | Iterable[SupportsIndex]
    ) -> MPolynomial | InfinitePolynomial_sparse:
    r"""
    Apply the isobaric divided difference operator `\bar{\pi}_w` to the
    polynomial `f`.

    This map is defined by `\bar{\pi}_i := \pi_i - 1`.

    ``w`` may be either a single index or a list of
    indices of simple transpositions.

    .. WARNING::

        The simple transpositions should be applied from left to right.

    EXAMPLES::

        sage: from sage.combinat.key_polynomial import isobaric_divided_difference_bar as iddb
        sage: R.<z> = InfinitePolynomialRing(GF(3))
        sage: iddb(z[1]^4*z[2]^2*z[4], 4)
        -z_4*z_2^2*z_1^4

        sage: iddb(z[1]^4*z[2]^2*z[3]*z[4], 3)
        z_4*z_3^2*z_2*z_1^4

        sage: iddb(z[1]^4*z[2]^2*z[3]*z[4], [3, 4])
        z_4^2*z_3*z_2*z_1^4

        sage: iddb(z[1]^4*z[2]^2*z[3]*z[4], [4, 3])
        0

        sage: iddb(z[1]^2*z[2], [3, 2])
        z_3*z_2^2 + z_3*z_2*z_1
    """

class OperatorPolynomial(CombinatorialFreeModule.Element):
    r"""
    Abstract base class for a polynomial defined recursively by
    divided difference type operators.

    Parents should implement the divided difference operator as
    a ``staticmethod`` ``_operator``.
    """

    def expand(self) -> MPolynomial | InfinitePolynomial_sparse:
        r"""
        Return ``self`` written in the monomial basis (i.e., as an element
        in the corresponding polynomial ring).

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: f = k([4,3,2,1])
            sage: f.expand()
            z_3*z_2^2*z_1^3*z_0^4

            sage: f = k([1,2,3])
            sage: f.expand()
            z_2^3*z_1^2*z_0 + z_2^3*z_1*z_0^2 + z_2^2*z_1^3*z_0
             + 2*z_2^2*z_1^2*z_0^2 + z_2^2*z_1*z_0^3 + z_2*z_1^3*z_0^2
             + z_2*z_1^2*z_0^3
        """

    to_polynomial = expand

    def divided_difference(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Apply the divided difference operator `\partial_w` to ``self``.

        The convention is to apply from left to right so if
        ``w = [w1, w2, ..., wm]`` then we apply
        `\partial_{w_2 \cdots w_m} \circ \partial_{w_1}`

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k([3,2,1]).divided_difference(2)
            k[3, 1, 1]
            sage: k([3,2,1]).divided_difference([2,3])
            k[3, 1]

            sage: k = KeyPolynomials(QQ, 4)
            sage: k([3,2,1,0]).divided_difference(2)
            k[3, 1, 1, 0]
        """

    def isobaric_divided_difference(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Apply the isobaric divided difference operator `\pi_w` to ``self``.

        The convention is to apply from left to right so if
        ``w = [w1, w2, ..., wm]`` then we apply
        `\pi_{w_2 \cdots w_m} \circ \pi_{w_1}`

        EXAMPLES::

            sage: a = AtomPolynomials(QQ)
            sage: a([3,2,1]).isobaric_divided_difference(2)
            a[3, 1, 2] + a[3, 2, 1]
            sage: a([3,2,1]).isobaric_divided_difference([2, 3])
            a[3, 1, 0, 2] + a[3, 1, 2] + a[3, 2, 0, 1] + a[3, 2, 1]

            sage: a = AtomPolynomials(QQ, 4)
            sage: a([3,2,1,0]).divided_difference(2)
            a[3, 1, 1, 0]
        """

class KeyPolynomial(OperatorPolynomial):
    r"""
    A key polynomial.

    Key polynomials are polynomials that form a basis for a polynomial ring
    and are indexed by weak compositions.

    Elements should be created by first creating the basis
    :class:`KeyPolynomialBasis` and passing a list representing the indexing
    composition.

    EXAMPLES::

        sage: k = KeyPolynomials(QQ)
        sage: f = k([4,3,2,1]) + k([1,2,3,4]); f
        k[1, 2, 3, 4] + k[4, 3, 2, 1]
        sage: f in k
        True
    """
    def pi(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Apply the operator `\pi_w` to ``self``.

        ``w`` may be either a ``Permutation`` or a list of indices of simple
        transpositions (1-based).

        The convention is to apply from left to right so if
        ``w = [w1, w2, ..., wm]`` then we apply
        `\pi_{w_2 \cdots w_m} \circ \pi_{w_1}`

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k([3,2,1]).pi(2)
            k[3, 1, 2]
            sage: k([3,2,1]).pi([2,1])
            k[1, 3, 2]
            sage: k([3,2,1]).pi(Permutation([3,2,1]))
            k[1, 2, 3]
            sage: f = k([3,2,1]) + k([3,2,1,1])
            sage: f.pi(2)
            k[3, 1, 2] + k[3, 1, 2, 1]
            sage: k.one().pi(1)
            k[]

            sage: k([3,2,1,0]).pi(2).pi(2)
            k[3, 1, 2]
            sage: (-k([3,2,1,0]) + 4*k([3,1,2,0])).pi(2)
            3*k[3, 1, 2]

            sage: k = KeyPolynomials(QQ, 4)
            sage: k([3,2,1,0]).pi(2)
            k[3, 1, 2, 0]
            sage: k([3,2,1,0]).pi([2,1])
            k[1, 3, 2, 0]
            sage: k([3,2,1,0]).pi(Permutation([3,2,1,4]))
            k[1, 2, 3, 0]
            sage: f = k([3,2,1,0]) + k([3,2,1,1])
            sage: f.pi(2)
            k[3, 1, 2, 0] + k[3, 1, 2, 1]
            sage: k.one().pi(1)
            k[0, 0, 0, 0]

        TESTS:

        We check that this is consistent with the definition via the
        isobaric divided difference operators::

            sage: from sage.combinat.key_polynomial import isobaric_divided_difference as idd
            sage: k = KeyPolynomials(QQ, 4)
            sage: S4 = Permutations(4)
            sage: f = k([4,2,2,0])
            sage: all(idd(f.expand(), w.reduced_word()) == f.pi(w).expand() for w in S4)
            True

            sage: f = k([4,2,0,1]) - 3 * k([2,0,1,2])
            sage: all(idd(f.expand(), w.reduced_word()) == f.pi(w).expand() for w in S4)
            True
        """
        ...
    isobaric_divided_difference = pi

    def pibar(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Apply the operator `\bar{\pi}_w` to ``self``.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k[2,3,1].pibar(2)
            k[2, 1, 3] - k[2, 3, 1]
            sage: k[2,3,1].pibar([2,3])
            k[2, 1, 0, 3] - k[2, 1, 3] - k[2, 3, 0, 1] + k[2, 3, 1]
            sage: k[2,3,1].pibar([2,2]) == -k[2,3,1].pibar(2)
            True

        TESTS:

        We check that this is consistent with the definition via the
        isobaric divided difference operators::

            sage: from sage.combinat.key_polynomial import isobaric_divided_difference_bar as iddb
            sage: k = KeyPolynomials(QQ, 4)
            sage: S4 = Permutations(4)
            sage: f = k[4,2,2,0]
            sage: all(iddb(f.expand(), w.reduced_word()) == f.pibar(w).expand() for w in S4)
            True

            sage: f = k([4,2,0,1]) - 3 * k([2,0,1,2])
            sage: all(iddb(f.expand(), w.reduced_word()) == f.pibar(w).expand() for w in S4)
            True
        """
        ...

class AtomPolynomial(OperatorPolynomial):
    r"""
    An atom polynomial.

    Atom polynomials are polynomials that form a basis for a polynomial
    ring and are indexed by weak compositions.

    Elements should be created by first creating the basis
    :class:`AtomPolynomialBasis` and passing a list representing
    the indexing composition.

    EXAMPLES::

        sage: a = AtomPolynomials(QQ)
        sage: f = a([4,3,2,1]) + a([1,2,3,4]); f
        a[1, 2, 3, 4] + a[4, 3, 2, 1]
        sage: f in a
        True
    """
    def pibar(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Apply the operator `\bar{\pi}_w` to ``self``.

        ``w`` may be either a ``Permutation`` or a list of indices of simple
        transpositions (1-based).

        The convention is to apply from left to right so if
        ``w = [w1, w2, ..., wm]`` then we apply
        `\bar{\pi}_{w_2 \cdots w_m} \circ \bar{\pi}_{w_1}`.

        EXAMPLES::

            sage: a = AtomPolynomials(QQ)
            sage: a([3,2,1]).pibar(2)
            a[3, 1, 2]
            sage: a([3,2,1]).pibar([2,1])
            a[1, 3, 2]
            sage: a([3,2,1]).pibar(Permutation([3,2,1]))
            a[1, 2, 3]
            sage: f = a([3,2,1]) + a([3,2,1,1])
            sage: f.pibar(2)
            a[3, 1, 2] + a[3, 1, 2, 1]
            sage: a.one().pibar(1)
            0

            sage: a([3,2,1,0]).pibar(2).pibar(2)
            -a[3, 1, 2]
            sage: (-a([3,2,1,0]) + 4*a([3,1,2,0])).pibar(2)
            -5*a[3, 1, 2]

            sage: a = AtomPolynomials(QQ, 4)
            sage: a([3,2,1,0]).pibar(2)
            a[3, 1, 2, 0]
            sage: a([3,2,1,0]).pibar([2,1])
            a[1, 3, 2, 0]
            sage: a([3,2,1,0]).pibar(Permutation([3,2,1,4]))
            a[1, 2, 3, 0]
            sage: f = a([3,2,1,0]) + a([3,2,1,1])
            sage: f.pibar(2)
            a[3, 1, 2, 0] + a[3, 1, 2, 1]
            sage: a.one().pibar(1)
            0

        TESTS:

        We check that this is consistent with the definition via the
        defining isobaric divided difference operators::

            sage: from sage.combinat.key_polynomial import isobaric_divided_difference_bar as iddb
            sage: a = AtomPolynomials(QQ, 4)
            sage: S4 = Permutations(4)
            sage: f = a([4,2,2,0])
            sage: all(iddb(f.expand(), w.reduced_word()) == f.pibar(w).expand() for w in S4)
            True

            sage: f = a([4,2,0,1]) - 3 * a([2,0,1,2])
            sage: all(iddb(f.expand(), w.reduced_word()) == f.pibar(w).expand() for w in S4)
            True
        """
        ...

    def pi(self, w: SupportsIndex | Iterable[SupportsIndex]) -> Self:
        r"""
        Return the action of the isobaric divided difference operator `\pi_w`
        on ``self``.

        EXAMPLES::

            sage: a = AtomPolynomials(QQ)
            sage: a[2,3,1].pi(2)
            a[2, 1, 3] + a[2, 3, 1]
            sage: a[2,3,1].pi([2,3])
            a[2, 1, 0, 3] + a[2, 1, 3] + a[2, 3, 0, 1] + a[2, 3, 1]
            sage: a[2,3,1].pi([2,2]) == a[2,3,1].pi(2)
            True

        TESTS:

        We check that this is consistent with the definition via the
        isobaric divided difference operators::

            sage: from sage.combinat.key_polynomial import isobaric_divided_difference as idd
            sage: a = AtomPolynomials(QQ, 4)
            sage: S4 = Permutations(4)
            sage: f = a[4,2,2,0]
            sage: all(idd(f.expand(), w.reduced_word()) == f.pi(w).expand() for w in S4)
            True

            sage: f = a([4,2,0,1]) - 3 * a([2,0,1,2])
            sage: all(idd(f.expand(), w.reduced_word()) == f.pi(w).expand() for w in S4)
            True
        """
        ...
    isobaric_divided_difference = pi

class OperatorPolynomialBasis(CombinatorialFreeModule):
    r"""
    A basis for a polynomial ring defined recursively by divided difference
    type operators such that the result is a triangular change of basis with
    the natural monomial basis.
    """
    @staticmethod
    def __classcall__(cls, R=None, k=None, poly_ring=None, poly_coeffs=False):
        r"""
        Normalize input.

        EXAMPLES::

            sage: KeyPolynomials(InfinitePolynomialRing(QQ, ['x', 'y']))
            Traceback (most recent call last):
            ...
            ValueError: polynomial ring has too many generators

            sage: KeyPolynomials(QQ['t0','t1','t2','t3'])
            Key polynomial basis over Rational Field

            sage: KeyPolynomials(QQ['t'])
            Key polynomial basis over Rational Field

            sage: KeyPolynomials(InfinitePolynomialRing(QQ['t'], 'z'))
            Key polynomial basis over Univariate Polynomial Ring in t over Rational Field

            sage: KeyPolynomials(QQ)
            Key polynomial basis over Rational Field

            sage: KeyPolynomials(QQ, 3)
            Key polynomial basis over Rational Field
        """

    def __init__(self, R=None, k=None, poly_ring=None):
        r"""
        Initialize ``self``.

        EXAMPLES::

            sage: R = GF(3)['t'].fraction_field()
            sage: k = KeyPolynomials(QQ)
            sage: TestSuite(k).run()
            sage: k = KeyPolynomials(R)
            sage: TestSuite(k).run()

            sage: k = KeyPolynomials(QQ, 4)
            sage: TestSuite(k).run()
            sage: k = KeyPolynomials(R, 4)
            sage: TestSuite(k).run()
        """
        ...

    def __getitem__(
            self, 
            c: SupportsIndex | tuple[SupportsIndex, ...] | list[tuple[SupportsIndex, ...]]
        ):
        """
        This method implements the abuses of notations ``k[2,1]``,
        ``k[[2,1]]``, etc.

        INPUT:

        - ``c`` -- anything that can represent an index of a basis element

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k[3]
            k[3]
            sage: k[3, 0, 2]
            k[3, 0, 2]
            sage: k[3, 1, 2, 0, 0]
            k[3, 1, 2]

            sage: k = KeyPolynomials(QQ, 4)
            sage: k[3, 0, 1, 0]
            k[3, 0, 1, 0]
            sage: k[3]
            Traceback (most recent call last):
            ...
            ValueError: [3] doesn't satisfy correct constraints
        """   

    @cached_method
    def one_basis(self):
        r"""
        Return the basis element indexing the identity.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k.one_basis()
            []

            sage: k = KeyPolynomials(QQ, 4)
            sage: k.one_basis()
            [0, 0, 0, 0]
        """

    def degree_on_basis(self, alpha: list[Int]) -> Integer:
        """
        Return the degree of the basis element indexed by ``alpha``.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k.degree_on_basis([2,1,0,2])
            5

            sage: k = KeyPolynomials(QQ, 5)
            sage: k.degree_on_basis([2,1,0,2,0])
            5
        """

    def polynomial_ring(self) -> MPolynomial | InfinitePolynomial_sparse:
        r"""
        Return the polynomial ring associated to ``self``.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k.polynomial_ring()
            Infinite polynomial ring in z over Rational Field

            sage: k = KeyPolynomials(QQ, 4)
            sage: k.polynomial_ring()
            Multivariate Polynomial Ring in z_0, z_1, z_2, z_3 over Rational Field
        """

    def poly_gens(self) -> InfinitePolynomialGen | Incomplete:
        r"""
        Return the polynomial generators for the polynomial ring
        associated to ``self``.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: k.poly_gens()
            z_*

            sage: k = KeyPolynomials(QQ, 4)
            sage: k.poly_gens()
            (z_0, z_1, z_2, z_3)
        """

    def from_polynomial(self, f):
        r"""
        Expand a polynomial in terms of ``self``.

        EXAMPLES::

            sage: k = KeyPolynomials(QQ)
            sage: z = k.poly_gens(); z
            z_*
            sage: p = z[0]^4*z[1]^2*z[2]*z[3] + z[0]^4*z[1]*z[2]^2*z[3]
            sage: k.from_polynomial(p)
            k[4, 1, 2, 1]

            sage: all(k(c) == k.from_polynomial(k(c).expand()) for c in IntegerVectors(n=5, k=4))
            True

            sage: T = crystals.Tableaux(['A', 4], shape=[4,2,1,1])
            sage: k.from_polynomial(T.demazure_character([2]))
            k[4, 1, 2, 1]
        """

class KeyPolynomialBasis(OperatorPolynomialBasis):
    r"""
    The key polynomial basis for a polynomial ring.

    For a full definition, see
    `SymmetricFunctions.com <https://www.symmetricfunctions.com/key.htm>`__.
    Key polynomials are indexed by weak compositions with no trailing zeros,
    and `\sigma` is the permutation of shortest length which sorts the
    indexing composition into a partition.

    EXAMPLES:

    Key polynomials are a basis, indexed by (weak) compositions,
    for polynomial rings::

        sage: k = KeyPolynomials(QQ)
        sage: k([3,0,1,2])
        k[3, 0, 1, 2]
        sage: k([3,0,1,2])/2
        1/2*k[3, 0, 1, 2]
        sage: R = k.polynomial_ring(); R
        Infinite polynomial ring in z over Rational Field

        sage: K = KeyPolynomials(GF(5)); K
        Key polynomial basis over Finite Field of size 5
        sage: 2*K([3,0,1,2])
        2*k[3, 0, 1, 2]
        sage: 5*(K([3,0,1,2]) + K([3,1,1]))
        0

    We can expand them in the standard monomial basis::

        sage: k([3,0,1,2]).expand()
        z_3^2*z_2*z_0^3 + z_3^2*z_1*z_0^3 + z_3*z_2^2*z_0^3
         + 2*z_3*z_2*z_1*z_0^3 + z_3*z_1^2*z_0^3 + z_2^2*z_1*z_0^3
         + z_2*z_1^2*z_0^3

        sage: k([0,0,2]).expand()
        z_2^2 + z_2*z_1 + z_2*z_0 + z_1^2 + z_1*z_0 + z_0^2

    If we have a polynomial, we can express it in the key basis::

        sage: z = R.gen()
        sage: k.from_polynomial(z[2]^2*z[1]*z[0])
        k[1, 1, 2] - k[1, 2, 1]

        sage: f = z[3]^2*z[2]*z[0]^3 + z[3]^2*z[1]*z[0]^3 + z[3]*z[2]^2*z[0]^3 + \
        ....: 2*z[3]*z[2]*z[1]*z[0]^3 + z[3]*z[1]^2*z[0]^3 + z[2]^2*z[1]*z[0]^3 + \
        ....: z[2]*z[1]^2*z[0]^3
        sage: k.from_polynomial(f)
        k[3, 0, 1, 2]

    Since the ring of key polynomials may be regarded as a different choice of
    basis for a polynomial ring, it forms an algebra, so we have
    multiplication::

        sage: k([10,5,2])*k([1,1,1])
        k[11, 6, 3]

    We can also multiply by polynomials in the monomial basis::

        sage: k([10,9,1])*z[0]
        k[11, 9, 1]
        sage: z[0] * k([10,9,1])
        k[11, 9, 1]
        sage: k([10,9,1])*(z[0] + z[3])
        k[10, 9, 1, 1] + k[11, 9, 1]

    When the sorting permutation is the longest element, the key polynomial
    agrees with the Schur polynomial::

        sage: s = SymmetricFunctions(QQ).schur()
        sage: k([1,2,3]).expand()
        z_2^3*z_1^2*z_0 + z_2^3*z_1*z_0^2 + z_2^2*z_1^3*z_0
         + 2*z_2^2*z_1^2*z_0^2 + z_2^2*z_1*z_0^3 + z_2*z_1^3*z_0^2
         + z_2*z_1^2*z_0^3
        sage: s[3,2,1].expand(3)
        x0^3*x1^2*x2 + x0^2*x1^3*x2 + x0^3*x1*x2^2 + 2*x0^2*x1^2*x2^2
         + x0*x1^3*x2^2 + x0^2*x1*x2^3 + x0*x1^2*x2^3

    The polynomial expansions can be computed using crystals and expressed in
    terms of the key basis::

        sage: T = crystals.Tableaux(['A',3],shape=[2,1])
        sage: f = T.demazure_character([3,2,1])
        sage: k.from_polynomial(f)
        k[1, 0, 0, 2]

    The default behavior is to work in a polynomial ring with infinitely many
    variables. One can work in a specicfied number of variables::

        sage: k = KeyPolynomials(QQ, 4)
        sage: k([3,0,1,2]).expand()
        z_0^3*z_1^2*z_2 + z_0^3*z_1*z_2^2 + z_0^3*z_1^2*z_3
         + 2*z_0^3*z_1*z_2*z_3 + z_0^3*z_2^2*z_3 + z_0^3*z_1*z_3^2 + z_0^3*z_2*z_3^2

        sage: k([0,0,2,0]).expand()
        z_0^2 + z_0*z_1 + z_1^2 + z_0*z_2  + z_1*z_2 + z_2^2

        sage: k([0,0,2,0]).expand().parent()
        Multivariate Polynomial Ring in z_0, z_1, z_2, z_3 over Rational Field

    If working in a specified number of variables, the length of the indexing
    composition must be the same as the number of variables::

        sage: k([0,0,2])
        Traceback (most recent call last):
         ...
        TypeError: do not know how to make x (= [0, 0, 2]) an element of self
         (=Key polynomial basis over Rational Field)

    One can also work in a specified polynomial ring::

        sage: k = KeyPolynomials(QQ['x0', 'x1', 'x2', 'x3'])
        sage: k([0,2,0,0])
        k[0, 2, 0, 0]
        sage: k([4,0,0,0]).expand()
        x0^4

    If one wishes to use a polynomial ring as coefficients for the key
    polynomials, pass the keyword argument ``poly_coeffs=True``::

        sage: k = KeyPolynomials(QQ['q'], poly_coeffs=True)
        sage: R = k.base_ring(); R
        Univariate Polynomial Ring in q over Rational Field
        sage: R.inject_variables()
        Defining q
        sage: (q^2 + q + 1)*k([0,2,2,0,3,2])
        (q^2+q+1)*k[0, 2, 2, 0, 3, 2]
    """
    Element = KeyPolynomial
    def from_schubert_polynomial(self, x: SchubertPolynomial_class | Any):
        r"""
        Expand a Schubert polynomial in ``self``.

        EXAMPLES::

            sage: k = KeyPolynomials(ZZ)
            sage: X = SchubertPolynomialRing(ZZ)
            sage: f = X([2,1,5,4,3])
            sage: k.from_schubert_polynomial(f)
            k[1, 0, 2, 1] + k[2, 0, 2] + k[3, 0, 0, 1]
            sage: k.from_schubert_polynomial(2)
            2*k[]
            sage: k(f)
            k[1, 0, 2, 1] + k[2, 0, 2] + k[3, 0, 0, 1]

            sage: k = KeyPolynomials(GF(7), 4)
            sage: k.from_schubert_polynomial(f)
            k[1, 0, 2, 1] + k[2, 0, 2, 0] + k[3, 0, 0, 1]

        TESTS::

            sage: k = KeyPolynomials(ZZ)
            sage: k.from_schubert_polynomial(k([3,2]))
            Traceback (most recent call last):
            ...
            ValueError: not a Schubert polynomial

            sage: k = KeyPolynomials(ZZ)
            sage: X = SchubertPolynomialRing(ZZ)
            sage: it = iter(Compositions())
            sage: for _ in range(50):
            ....:     C = next(it)
            ....:     assert k.from_schubert_polynomial(X(k[C])) == k[C], C

            sage: k = KeyPolynomials(ZZ, 4)
            sage: X = SchubertPolynomialRing(ZZ)
            sage: it = iter(k.basis().keys())
            sage: for _ in range(50):
            ....:     C = next(it)
            ....:     assert k.from_schubert_polynomial(X(k[C])) == k[C], C
        """

class AtomPolynomialBasis(OperatorPolynomialBasis):
    r"""
    The atom polynomial basis for a polynomial ring.

    For a full definition, see
    `SymmetricFunctions.com <https://www.symmetricfunctions.com/key.htm#atom>`__.
    Atom polynomials are indexed by weak compositions `\alpha` with no
    trailing zeros. A basis element is given by

    .. MATH::

        a_{\alpha} = \bar{\pi}_{\sigma} x^{\mu},

    where `\sigma` is the permutation of shortest length which sorts the
    `\alpha` into a partition `\mu`.

    EXAMPLES:

    Atom polynomials are a basis, indexed by (weak) compositions,
    for polynomial rings::

        sage: a = AtomPolynomials(QQ)
        sage: a([3,0,1,2])
        a[3, 0, 1, 2]
        sage: a([3,0,1,2])/2
        1/2*a[3, 0, 1, 2]
        sage: R = a.polynomial_ring(); R
        Infinite polynomial ring in z over Rational Field

        sage: A = AtomPolynomials(GF(5)); A
        Atom polynomial basis over Finite Field of size 5
        sage: 2*A([3,0,1,2])
        2*a[3, 0, 1, 2]
        sage: 5*(A([3,0,1,2]) + A([3,1,1]))
        0

    We can expand them in the standard monomial basis::

        sage: a([2,1,3,2]).expand()
        z_3^2*z_2^3*z_1*z_0^2 + z_3^2*z_2^2*z_1^2*z_0^2

        sage: a[0,2,2].expand()
        z_2^2*z_1^2 + z_2^2*z_1*z_0 + z_2*z_1^2*z_0

    If we have a polynomial, we can express it in the atom basis::

        sage: z = R.gen()
        sage: a.from_polynomial(z[2]^2*z[1]*z[0])
        a[1, 1, 2]
        sage: a.from_polynomial(z[2]^3*z[1]^2*z[0])
        a[1, 2, 3]

        sage: f = (z[3]^2*z[2]*z[0]^3 + z[3]^2*z[1]*z[0]^3 + z[3]*z[2]^2*z[0]^3
        ....:      + 2*z[3]*z[2]*z[1]*z[0]^3 + z[3]*z[1]^2*z[0]^3
        ....:      + z[2]^2*z[1]*z[0]^3 + z[2]*z[1]^2*z[0]^3)
        sage: a.from_polynomial(f)
        a[3, 0, 1, 2] + a[3, 0, 2, 1] + a[3, 1, 0, 2] + a[3, 1, 2]
         + a[3, 2, 0, 1] + a[3, 2, 1]

    Since the ring of atom polynomials may be regarded as a different
    choice of basis for a polynomial ring, it forms an algebra, so
    we have multiplication::

        sage: a[10,5,2] * a[1,1,1]
        a[11, 6, 3]

    We can also multiply by polynomials in the monomial basis::

        sage: a([10,9,1]) * z[0]
        a[11, 9, 1]
        sage: z[0] * a([10,9,1])
        a[11, 9, 1]
        sage: a([10,9,1]) * (z[0] + z[3])
        a[10, 9, 1, 1] + a[11, 9, 1]
    """
    Element = AtomPolynomial

    def from_key_polynomial(self, x):
        r"""
        Expand a key polynomial in ``self``.

        EXAMPLES::

            sage: a = AtomPolynomials(ZZ)
            sage: k = KeyPolynomials(ZZ)
            sage: f = k[1,2,3]
            sage: a.from_key_polynomial(f)
            a[1, 2, 3] + a[1, 3, 2] + a[2, 1, 3] + a[2, 3, 1] + a[3, 1, 2] + a[3, 2, 1]
            sage: a.from_key_polynomial(2)
            2*a[]
            sage: a(f)
            a[1, 2, 3] + a[1, 3, 2] + a[2, 1, 3] + a[2, 3, 1] + a[3, 1, 2] + a[3, 2, 1]

            sage: a = AtomPolynomials(GF(7), 4)
            sage: a.from_key_polynomial(f)
            a[1, 2, 3, 0] + a[1, 3, 2, 0] + a[2, 1, 3, 0]
             + a[2, 3, 1, 0] + a[3, 1, 2, 0] + a[3, 2, 1, 0]

        TESTS::

            sage: a = AtomPolynomials(ZZ)
            sage: a.from_key_polynomial(a([3,2]))
            Traceback (most recent call last):
            ...
            ValueError: not a key polynomial

            sage: a = AtomPolynomials(ZZ)
            sage: k = KeyPolynomials(ZZ)
            sage: it = iter(a.basis().keys())
            sage: for _ in range(50):
            ....:     C = next(it)
            ....:     assert a.from_key_polynomial(k.from_polynomial(a[C].expand())) == a[C], C

            sage: a = AtomPolynomials(ZZ, 4)
            sage: k = KeyPolynomials(ZZ, 4)
            sage: it = iter(a.basis().keys())
            sage: for _ in range(50):
            ....:     C = next(it)
            ....:     assert a.from_key_polynomial(k.from_polynomial(a[C].expand())) == a[C], C
        """

