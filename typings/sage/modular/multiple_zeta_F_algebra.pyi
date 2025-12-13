from collections.abc import Iterator
from sage.arith.misc import bernoulli as bernoulli
from sage.categories.bialgebras_with_basis import BialgebrasWithBasis as BialgebrasWithBasis
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.words.finite_word import FiniteWord_class as FiniteWord_class
from sage.combinat.words.words import Words as Words
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.integer_range import IntegerRange as IntegerRange
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

def W_Odds(start: int = 3):
    """
    Indexing set for the odd generators.

    This is the set of pairs
    (integer power of `f_2`, word in `s, s+2, s+4, \\ldots`)
    where `s` is the chosen odd start index.

    INPUT:

    - ``start`` -- (default: ``3``) odd start index for odd generators

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import W_Odds
        sage: W_Odds(3)
        Finite words over {3, 5, ...}
    """
def str_to_index(x: str) -> tuple:
    '''
    Convert a string to an index.

    Every letter ``\'2\'`` contributes to the power of `f_2`. Other letters
    are odd and define a word in `f_1, f_3, f_5, \\ldots`

    Usually the letters ``\'2\'`` form a prefix of the input.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import str_to_index
        sage: str_to_index("22357")
        (2, [3, 5, 7])

        sage: str_to_index("22317")
        (2, [3, 1, 7])
    '''
def basis_f_odd_iterator(n, start: int = 3) -> Iterator[tuple]:
    """
    Return an iterator over compositions of `n` with odd parts.

    Let `s` be the chosen odd start index. The allowed parts are the
    odd integers at least equal to `s`, in the set `s,s+2,s+4,s+6,\\ldots`.

    This set of compositions is used to index a basis.

    INPUT:

    - ``n`` -- integer

    - ``start`` -- odd integer (default: `3`); start index for odd generators

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import basis_f_odd_iterator
        sage: [list(basis_f_odd_iterator(i)) for i in range(2,9)]
        [[], [(3,)], [], [(5,)], [(3, 3)], [(7,)], [(5, 3), (3, 5)]]
        sage: list(basis_f_odd_iterator(14))
        [(11, 3),
         (5, 3, 3, 3),
         (3, 5, 3, 3),
         (3, 3, 5, 3),
         (9, 5),
         (3, 3, 3, 5),
         (7, 7),
         (5, 9),
         (3, 11)]
    """
def basis_f_iterator(n, start: int = 3) -> Iterator[tuple]:
    """
    Return an iterator for decompositions of `n` using `2` and odd integers.

    Let `s` be the chosen odd start index. The allowed odd parts are the
    odd integers at least equal to `s`, in the set `s,s+2,s+4,s+6,\\ldots`.

    The means that each term is made of a power of 2 and a composition
    of the remaining integer with parts in `(s,s+2,s+4,\\ldots)`.

    This set is indexing a basis of the homogeneous component of weight ``n``.

    INPUT:

    - ``n`` -- integer

    - ``start`` -- (default: `3`) odd start index for odd generators

    Each term is returned as a pair (integer, word) where
    the integer is the exponent of 2.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import basis_f_iterator
        sage: [list(basis_f_iterator(i)) for i in range(2,9)]
        [[(1, word: )],
         [(0, word: 3)],
         [(2, word: )],
         [(0, word: 5), (1, word: 3)],
         [(0, word: 33), (3, word: )],
         [(0, word: 7), (1, word: 5), (2, word: 3)],
         [(0, word: 53), (0, word: 35), (1, word: 33), (4, word: )]]
        sage: list(basis_f_iterator(11))
        [(0, word: 11),
         (0, word: 533),
         (0, word: 353),
         (0, word: 335),
         (1, word: 9),
         (1, word: 333),
         (2, word: 7),
         (3, word: 5),
         (4, word: 3)]

    TESTS::

        sage: list(basis_f_iterator(0))
        [(0, word: )]
        sage: list(basis_f_iterator(3, start=1))
        [(0, word: 3), (0, word: 111), (1, word: 1)]
    """
def morphism_constructor(data: dict, start: int = 3):
    '''
    Build a morphism from the F-algebra to some codomain.

    Let `s` be the chosen odd start index.

    INPUT:

    - ``data`` -- dictionary with integer keys containing the images of
      `f_2, f_s, f_{s+2}, f_{s+4}, \\ldots`

    - ``start`` -- (default: 3) start index for odd generators

    OUTPUT: the unique morphism defined by the dictionary ``data``

    The codomain must be a zinbiel algebra, namely have both a
    commutative associative product ``*`` and a zinbiel product
    available as ``half_product``.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import F_algebra, morphism_constructor
        sage: Z = Multizeta
        sage: D = {2: Z(2), 3: Z(3)}
        sage: rho = morphism_constructor(D)
        sage: F = rho.domain()
        sage: rho(F("2"))
        ζ(2)
        sage: rho(F("3"))
        ζ(3)
        sage: rho(F("33"))
        6*ζ(1,5) + 3*ζ(2,4) + ζ(3,3)
        sage: rho(F("23"))
        6*ζ(1,4) + 3*ζ(2,3) + ζ(3,2)
    '''

class F_algebra(CombinatorialFreeModule):
    '''
    Auxiliary algebra for the study of motivic multiple zeta values.

    INPUT:

    - ``R`` -- ring

    - ``start`` -- (default: ``3``) odd start index for odd generators

    EXAMPLES::

        sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
        sage: F = F_algebra(QQ); F
        F-ring over Rational Field
        sage: F.base_ring()
        Rational Field
        sage: F.is_commutative()
        True
        sage: TestSuite(F).run()

        sage: f2 = F("2")
        sage: f3 = F("3")
        sage: f5 = F("5")

        sage: s = f2*f3+f5; s
        f5 + f2*f3
    '''
    def __init__(self, R, start: int = 3) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``R`` -- base ring

        - ``start`` -- (default: ``3``) odd start index for odd generators

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: F = F_algebra(QQ); F
            F-ring over Rational Field

        TESTS::

            sage: F_algebra(24)
            Traceback (most recent call last):
            ...
            TypeError: argument R must be a ring
        """
    @cached_method
    def one_basis(self):
        """
        Return the pair (0, empty word), which index of `1` of this algebra.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: A.one_basis()
            (0, word: )
        """
    def product_on_basis(self, pw1, pw2):
        '''
        Return the product of basis elements ``pw1`` and ``pw2``.

        INPUT:

        - ``pw1``, ``pw2`` -- basis elements

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: W = A.basis().keys()
            sage: A.product(A("23"), A("25"))  # indirect doctest
            f2^2*f3f5 + f2^2*f5f3
        '''
    def half_product_on_basis(self, pw1, pw2):
        '''
        Return the half product of basis elements ``pw1`` and ``pw2``.

        This is an extension of the zinbiel product of the shuffle algebra.

        INPUT:

        - ``pw1``, ``pw2`` -- basis elements

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: W = A.basis().keys()
            sage: t = A.half_product(A("23"), A("25")); t  # indirect doctest
            f2^2*f3f5

        TESTS::

            sage: [list(pw[1]) for pw, cf in t]
            [[3, 5]]
        '''
    @lazy_attribute
    def half_product(self):
        '''
        Return the `<` product.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: W = A.basis().keys()
            sage: A.half_product(A("235"), A("227"))
            f2^3*f3f5f7 + f2^3*f3f7f5
        '''
    def gen(self, i):
        """
        Return the generator of the F ring over `\\QQ`.

        INPUT:

        - ``i`` -- nonnegative integer (at least 2)

        If ``i`` is odd, this returns a single generator `f_i` of the free
        shuffle algebra.

        Otherwise, it returns an appropriate multiple of a power of `f_2`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: [A.gen(i) for i in range(2,8)]
            [f2, f3, 2/5*f2^2, f5, 8/35*f2^3, f7]
        """
    def some_elements(self) -> list:
        """
        Return some typical elements.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: F = F_algebra(ZZ)
            sage: F.some_elements()
            [0, 1, f2, f3 + f5]
        """
    def coproduct_on_basis(self, pw):
        """
        Return the coproduct of the basis element indexed by the pair ``pw``.

        The coproduct is given by deconcatenation on the shuffle part,
        and extended by the value

        .. MATH::

            \\Delta(f_2) = 1 \\otimes f_2.

        INPUT:

        - ``pw`` -- an index

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: F = F_algebra(QQ)
            sage: W = F.basis().keys()
            sage: F.coproduct_on_basis(W((1,[])))
            1 # f2
            sage: F.coproduct_on_basis(W((0,[3])))
            1 # f3 + f3 # 1
            sage: F.coproduct_on_basis(W((1,[3])))
            1 # f2*f3 + f3 # f2
            sage: F.coproduct_on_basis(W((0,[3,5])))
            1 # f3f5 + f3 # f5 + f3f5 # 1
            sage: F.coproduct_on_basis(W((0,[])))
            1 # 1

        TESTS::

            sage: F = F_algebra(QQ)
            sage: S = F.an_element(); S
            3*f2*f3f5 + f2*f5f3
            sage: F.coproduct(S)
            3*1 # f2*f3f5 + 1 # f2*f5f3 + 3*f3 # f2*f5 + 3*f3f5 # f2
            + f5 # f2*f3 + f5f3 # f2
        """
    def degree_on_basis(self, pw):
        """
        Return the degree of the element ``w``.

        This is the sum of the power of `f_2` and the indices in the word.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: A = F_algebra(QQ)
            sage: [A.degree_on_basis(x.leading_support()) for x in A.some_elements() if x != 0]
            [0, 1, 5]
        """
    def homogeneous_from_vector(self, vec, N):
        """
        Convert back a vector to an element of the F-algebra.

        INPUT:

        - ``vec`` -- a vector with coefficients in some base ring

        - ``N`` -- integer; the homogeneous weight

        OUTPUT: a homogeneous element of :func:`F_ring` over this base ring

        .. SEEALSO:: :meth:`F_algebra.homogeneous_to_vector`

        EXAMPLES::

            sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
            sage: F = F_algebra(QQ)
            sage: F.homogeneous_from_vector((4,5),6)
            4*f3f3 + 5*f2^3
            sage: _.homogeneous_to_vector()
            (4, 5)
        """
    class Element(CombinatorialFreeModule.Element):
        def coefficient(self, w):
            '''
            Return the coefficient of the given index.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
                sage: F = F_algebra(QQ)
                sage: S = F.an_element(); S
                3*f2*f3f5 + f2*f5f3
                sage: S.coefficient("235")
                3
                sage: S.coefficient((1,[5,3]))
                1
            '''
        def homogeneous_to_vector(self):
            '''
            Convert an homogeneous element to a vector.

            This is using a fixed enumeration of the basis.

            OUTPUT: a vector with coefficients in the base ring

            .. SEEALSO:: :meth:`F_algebra.homogeneous_from_vector`

            EXAMPLES::

                sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
                sage: F = F_algebra(QQ)
                sage: f2 = F("2")
                sage: x = f2**4 + 34 * F("233")
                sage: x.homogeneous_to_vector()
                (0, 0, 34, 1)
                sage: x.coefficients()
                [34, 1]

            TESTS::

                sage: x = F.monomial(F._indices((0,[11]))); x
                f11
                sage: x.homogeneous_to_vector()
                (1, 0, 0, 0, 0, 0, 0, 0, 0)
            '''
        def without_f2(self):
            '''
            Remove all terms containing a power of `f_2`.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
                sage: F = F_algebra(QQ)
                sage: t = 4 * F("35") + F("27")
                sage: t.without_f2()
                4*f3f5
            '''
        def single_valued(self):
            '''
            Return the single-valued version of ``self``.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
                sage: F = F_algebra(QQ)
                sage: t = 4 * F("2") + F("3")
                sage: t.single_valued()
                2*f3
                sage: t = 4 * F("35") + F("27")
                sage: t.single_valued()
                8*f3f5 + 8*f5f3
            '''
