from _typeshed import Incomplete
from collections.abc import Iterator
from sage.categories.domains import Domains as Domains
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.rings import Rings as Rings
from sage.combinat.composition import Compositions as Compositions
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.words.finite_word import FiniteWord_class as FiniteWord_class
from sage.combinat.words.word import Word as Word
from sage.combinat.words.words import Words as Words
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.fast_methods import Singleton as Singleton
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.multiple_zeta_F_algebra import F_algebra as F_algebra
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.structure.element import parent as parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE

B_data: list[list[tuple]]
Words10: Incomplete

def coproduct_iterator(paire) -> Iterator[list]:
    """
    Return an iterator for terms in the coproduct.

    This is an auxiliary function.

    INPUT:

    - ``paire`` -- a pair (list of indices, end of word)

    OUTPUT: iterator for terms in the motivic coproduct

    Each term is seen as a list of positions.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import coproduct_iterator
        sage: list(coproduct_iterator(([0],[0,1,0,1])))
        [[0, 1, 2, 3]]
        sage: list(coproduct_iterator(([0],[0,1,0,1,1,0,1])))
        [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 6], [0, 1, 5, 6], [0, 4, 5, 6], [0, 6]]
    """
def composition_to_iterated(w, reverse: bool = False) -> tuple[int, ...]:
    """
    Convert a composition to a word in 0 and 1.

    By default, the chosen convention maps (2,3) to (1,0,1,0,0),
    respecting the reading order from left to right.

    The inverse map is given by :func:`iterated_to_composition`.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import composition_to_iterated
        sage: composition_to_iterated((1,2))
        (1, 1, 0)
        sage: composition_to_iterated((3,1,2))
        (1, 0, 0, 1, 1, 0)
        sage: composition_to_iterated((3,1,2,4))
        (1, 0, 0, 1, 1, 0, 1, 0, 0, 0)

    TESTS::

        sage: composition_to_iterated((1,2), True)
        (1, 0, 1)
    """
def iterated_to_composition(w, reverse: bool = False) -> tuple[int, ...]:
    """
    Convert a word in 0 and 1 to a composition.

    By default, the chosen convention maps (1,0,1,0,0) to (2,3).

    The inverse map is given by :func:`composition_to_iterated`.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import iterated_to_composition
        sage: iterated_to_composition([1,0,1,0,0])
        (2, 3)
        sage: iterated_to_composition(Word([1,1,0]))
        (1, 2)
        sage: iterated_to_composition(Word([1,1,0,1,1,0,0]))
        (1, 2, 1, 3)

    TESTS::

        sage: iterated_to_composition([1,0,1,0,0], True)
        (3, 2)
    """
def dual_composition(c) -> tuple[int, ...]:
    """
    Return the dual composition of ``c``.

    This is an involution on compositions such that associated
    multizetas are equal.

    INPUT:

    - ``c`` -- a composition

    OUTPUT: a composition

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import dual_composition
        sage: dual_composition([3])
        (1, 2)
        sage: dual_composition(dual_composition([3,4,5])) == (3,4,5)
        True
    """
def minimize_term(w, cf):
    """
    Return the largest among ``w`` and the dual word of ``w``.

    INPUT:

    - ``w`` -- a word in the letters 0 and 1

    - ``cf`` -- a coefficient

    OUTPUT:

    (word, coefficient)

    The chosen order is lexicographic with 1 < 0.

    If the dual word is chosen, the sign of the coefficient is changed,
    otherwise the coefficient is returned unchanged.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import minimize_term, Words10
        sage: minimize_term(Words10((1,1,0)), 1)
        (word: 100, -1)
        sage: minimize_term(Words10((1,0,0)), 1)
        (word: 100, 1)
    """

class MultizetaValues(Singleton):
    """
    Custom cache for numerical values of multiple zetas.

    Computations are performed using the PARI/GP :pari:`zetamultall` (for the
    cache) and :pari:`zetamult` (for indices/precision outside of the cache).

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import MultizetaValues
        sage: M = MultizetaValues()

        sage: M((1,2))
        1.202056903159594285399738161511449990764986292340...
        sage: parent(M((2,3)))
        Real Field with 1024 bits of precision

        sage: M((2,3), prec=53)
        0.228810397603354
        sage: parent(M((2,3), prec=53))
        Real Field with 53 bits of precision

        sage: M((2,3), reverse=False) == M((3,2))
        True

        sage: M((2,3,4,5))
        2.9182061974731261426525583710934944310404272413...e-6
        sage: M((2,3,4,5), reverse=False)
        0.0011829360522243605614404196778185433287651...

        sage: parent(M((2,3,4,5)))
        Real Field with 1024 bits of precision
        sage: parent(M((2,3,4,5), prec=128))
        Real Field with 128 bits of precision
    """
    max_weight: int
    prec: int
    def __init__(self) -> None:
        """
        When first called, pre-compute up to weight 8 at precision 1024.

        TESTS::

            sage: from sage.modular.multiple_zeta import MultizetaValues
            sage: M = MultizetaValues()
        """
    def reset(self, max_weight: int = 8, prec: int = 1024) -> None:
        """
        Reset the cache to its default values or to given arguments.

        TESTS::

            sage: from sage.modular.multiple_zeta import MultizetaValues
            sage: M = MultizetaValues()
            sage: M
            Cached multiple zeta values at precision 1024 up to weight 8
            sage: M.reset(5, 64)
            sage: M
            Cached multiple zeta values at precision 64 up to weight 5
            sage: M.reset()
            sage: M
            Cached multiple zeta values at precision 1024 up to weight 8
        """
    def update(self, max_weight, prec) -> None:
        """
        Compute and store more values if needed.

        TESTS::

            sage: from sage.modular.multiple_zeta import MultizetaValues
            sage: M = MultizetaValues()
            sage: M
            Cached multiple zeta values at precision 1024 up to weight 8
            sage: M.update(5, 64)
            sage: M
            Cached multiple zeta values at precision 1024 up to weight 8
            sage: M.update(5, 2048)
            sage: M
            Cached multiple zeta values at precision 2048 up to weight 8
            sage: M.reset()
        """
    def pari_eval(self, index):
        """
        TESTS::

            sage: from sage.modular.multiple_zeta import MultizetaValues
            sage: M = MultizetaValues()
            sage: [M.pari_eval((n,)) for n in range(2,20)]
            [1.64493406684823, 1.20205690315959, 1.08232323371114, 1.03692775514337, ... 1.00000381729326, 1.00000190821272]
        """
    def __call__(self, index, prec=None, reverse: bool = True):
        """
        Numerical multiple zeta value as a Sage real floating point number.

        TESTS::

            sage: from sage.modular.multiple_zeta import MultizetaValues

            sage: V = MultizetaValues()
            sage: V((3,2))
            0.7115661975505724320969738060864026120925612044383392364...
            sage: V((3,2), reverse=False)
            0.2288103976033537597687461489416887919325093427198821602...
            sage: V((3,2), prec=128)
            0.71156619755057243209697380608640261209
            sage: V((3,2), prec=128, reverse=False)
            0.22881039760335375976874614894168879193

            sage: V((1,3))
            0.2705808084277845478790009241352919756936877379796817269...
            sage: V((3,1), reverse=False)
            0.2705808084277845478790009241352919756936877379796817269...

            sage: V((3,1))
            Traceback (most recent call last):
            ...
            ValueError: divergent zeta value
            sage: V((1,3), reverse=False)
            Traceback (most recent call last):
            ...
            ValueError: divergent zeta value
        """

Values: Incomplete

def extend_multiplicative_basis(B, n) -> Iterator[tuple]:
    """
    Extend a multiplicative basis into a basis.

    This is an iterator.

    INPUT:

    - ``B`` -- function mapping integer to list of tuples of compositions

    - ``n`` -- integer

    OUTPUT: each term is a tuple of tuples of compositions

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import extend_multiplicative_basis
        sage: from sage.modular.multiple_zeta import B_data
        sage: list(extend_multiplicative_basis(B_data,5))
        [((5,),), ((3,), (2,))]
        sage: list(extend_multiplicative_basis(B_data,6))
        [((3,), (3,)), ((2,), (2,), (2,))]
        sage: list(extend_multiplicative_basis(B_data,7))
        [((7,),), ((5,), (2,)), ((3,), (2,), (2,))]
    """
def Multizeta(*args):
    """
    Common entry point for multiple zeta values.

    If the argument is a sequence of 0 and 1, an element of
    :class:`Multizetas_iterated` will be returned.

    Otherwise, an element of :class:`Multizetas` will be returned.

    The base ring is `\\QQ`.

    EXAMPLES::

        sage: Z = Multizeta
        sage: Z(1,0,1,0)
        I(1010)
        sage: Z(3,2,2)
        ζ(3,2,2)

    TESTS::

        sage: Z(3,2,2).iterated().composition()
        ζ(3,2,2)
        sage: Z(1,0,1,0).composition().iterated()
        I(1010)
    """

class Multizetas(CombinatorialFreeModule):
    """
    Main class for the algebra of multiple zeta values.

    The convention is chosen so that `\\zeta(1,2)` is convergent.

    EXAMPLES::

        sage: M = Multizetas(QQ)
        sage: x = M((2,))
        sage: y = M((4,3))
        sage: x+5*y
        ζ(2) + 5*ζ(4,3)
        sage: x*y
        6*ζ(1,4,4) + 8*ζ(1,5,3) + 3*ζ(2,3,4) + 4*ζ(2,4,3) + 3*ζ(3,2,4)
        + 2*ζ(3,3,3) + 6*ζ(4,1,4) + 3*ζ(4,2,3) + ζ(4,3,2)

    TESTS::

        sage: A = QQ['u']
        sage: u = A.gen()
        sage: M = Multizetas(A)
        sage: (u*M((2,))+M((3,)))*M((2,))
        4*u*ζ(1,3) + 6*ζ(1,4) + 2*u*ζ(2,2) + 3*ζ(2,3) + ζ(3,2)

    Check for :issue:`30925`::

        sage: M = Multizetas(QQ)
        sage: l = [1,2,3]
        sage: z = M(l)
        sage: l[0] = 19
        sage: z
        ζ(1,2,3)
    """
    def __init__(self, R) -> None:
        """
        TESTS::

            sage: M = Multizetas(QQ)
            sage: TestSuite(M).run()  # not tested
            sage: M.category()
            Category of commutative no zero divisors graded algebras
            with basis over Rational Field
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the unit for the algebra.

        This is the empty word.

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: M.one_basis()
            word:
        """
    def some_elements(self) -> tuple:
        """
        Return some elements of the algebra.

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: M.some_elements()
            (ζ(), ζ(2), ζ(3), ζ(4), ζ(1,2))
        """
    def product_on_basis(self, w1, w2):
        """
        Compute the product of two monomials.

        This is done by converting to iterated integrals and
        using the shuffle product.

        INPUT:

        - ``w1``, ``w2`` -- compositions as words

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: W = M.basis().keys()
            sage: M.product_on_basis(W([2]),W([2]))
            4*ζ(1,3) + 2*ζ(2,2)
            sage: x = M((2,))
            sage: x*x
            4*ζ(1,3) + 2*ζ(2,2)
        """
    def half_product(self, w1, w2):
        """
        Compute half of the product of two elements.

        This comes from half of the shuffle product.

        .. WARNING:: This is not a motivic operation.

        INPUT:

        - ``w1``, ``w2`` -- elements

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: M.half_product(M([2]),M([2]))
            2*ζ(1,3) + ζ(2,2)

        TESTS:

            sage: M.half_product(M.one(), M([2]))
            Traceback (most recent call last):
            ...
            ValueError: not defined on the unit
        """
    @lazy_attribute
    def iterated(self):
        """
        Convert to the algebra of iterated integrals.

        This is also available as a method of elements.

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: x = M((3,2))
            sage: M.iterated(3*x)
            3*I(10010)
            sage: x = M((2,3,2))
            sage: M.iterated(4*x)
            -4*I(1010010)
        """
    def iterated_on_basis(self, w):
        """
        Convert to the algebra of iterated integrals.

        Beware that this conversion involves signs in our chosen convention.

        INPUT:

        - ``w`` -- a word

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: x = M.basis().keys()((3,2))
            sage: M.iterated_on_basis(x)
            I(10010)
            sage: x = M.basis().keys()((2,3,2))
            sage: M.iterated_on_basis(x)
            -I(1010010)
        """
    def degree_on_basis(self, w):
        """
        Return the degree of the monomial ``w``.

        This is the sum of terms in ``w``.

        INPUT:

        - ``w`` -- a composition

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: x = (2,3)
            sage: M.degree_on_basis(x)  # indirect doctest
            5
        """
    @lazy_attribute
    def phi(self):
        """
        Return the morphism ``phi``.

        This sends multiple zeta values to the auxiliary F-algebra,
        which is a shuffle algebra in odd generators `f_3,f_5,f_7,\\dots`
        over the polynomial ring in one variable `f_2`.

        This is a ring isomorphism, that depends on the choice of a
        multiplicative basis for the ring of motivic multiple zeta
        values. Here we use one specific hardcoded basis.

        For the precise definition of ``phi`` by induction, see [Brown2012]_.

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: m = Multizeta(2,2) + 2*Multizeta(1,3); m
            2*ζ(1,3) + ζ(2,2)
            sage: M.phi(m)
            1/2*f2^2

            sage: Z = Multizeta
            sage: B5 = [3*Z(1,4) + 2*Z(2,3) + Z(3,2), 3*Z(1,4) + Z(2,3)]
            sage: [M.phi(b) for b in B5]
            [-1/2*f5 + f2*f3, 1/2*f5]
        """
    def algebra_generators(self, n) -> list:
        """
        Return a set of multiplicative generators in weight ``n``.

        This is obtained from hardcoded data, available only up to weight 17.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: M.algebra_generators(5)
            [ζ(5)]
            sage: M.algebra_generators(8)
            [ζ(3,5)]
        """
    def basis_data(self, basering, n) -> Iterator:
        """
        Return an iterator for a basis in weight ``n``.

        This is obtained from hardcoded data, available only up to weight 17.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: list(M.basis_data(QQ, 4))
            [4*ζ(1,3) + 2*ζ(2,2)]
        """
    def basis_brown(self, n) -> list:
        """
        Return a basis of the algebra of multiple zeta values in weight ``n``.

        It was proved by Francis Brown that this is a basis of motivic
        multiple zeta values.

        This is made of all `\\zeta(n_1, ..., n_r)` with parts in {2,3}.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: M = Multizetas(QQ)
            sage: M.basis_brown(3)
            [ζ(3)]
            sage: M.basis_brown(4)
            [ζ(2,2)]
            sage: M.basis_brown(5)
            [ζ(3,2), ζ(2,3)]
            sage: M.basis_brown(6)
            [ζ(3,3), ζ(2,2,2)]
        """
    @cached_method
    def basis_filtration(self, d, reverse: bool = False):
        """
        Return a module basis of the homogeneous components of weight ``d`` compatible with
        the length filtration.

        INPUT:

        - ``d`` -- nonnegative integer; the weight

        - ``reverse`` -- boolean (default: ``False``); change the ordering of compositions

        EXAMPLES::

            sage: M = Multizetas(QQ)

            sage: M.basis_filtration(5)
            [ζ(5), ζ(1,4)]
            sage: M.basis_filtration(6)
            [ζ(6), ζ(1,5)]
            sage: M.basis_filtration(8)
            [ζ(8), ζ(1,7), ζ(2,6), ζ(1,1,6)]
            sage: M.basis_filtration(8, reverse=True)
            [ζ(8), ζ(6,2), ζ(5,3), ζ(5,1,2)]

            sage: M.basis_filtration(0)
            [ζ()]
            sage: M.basis_filtration(1)
            []
        """
    class Element(CombinatorialFreeModule.Element):
        def iterated(self):
            """
            Convert to the algebra of iterated integrals.

            Beware that this conversion involves signs.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: x = M((2,3,4))
                sage: x.iterated()
                -I(101001000)
            """
        def single_valued(self):
            """
            Return the single-valued version of ``self``.

            This is the projection map onto the sub-algebra of
            single-valued motivic multiple zeta values, as defined by
            F. Brown in [Bro2013]_.

            This morphism of algebras sends in particular `\\zeta(2)` to `0`.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: x = M((2,))
                sage: x.single_valued()
                0
                sage: x = M((3,))
                sage: x.single_valued()
                2*ζ(3)
                sage: x = M((5,))
                sage: x.single_valued()
                2*ζ(5)
                sage: x = M((2,3))
                sage: x.single_valued()
                -11*ζ(5)

                sage: Z = Multizeta
                sage: Z(3,5).single_valued() == -10*Z(3)*Z(5)
                True
                sage: Z(5,3).single_valued() == 14*Z(3)*Z(5)
                True
            """
        def simplify(self):
            """
            Gather terms using the duality relations.

            This can help to lower the number of monomials.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: z = 3*M((3,)) + 5*M((1,2))
                sage: z.simplify()
                8*ζ(3)
            """
        def simplify_full(self, basis=None):
            """
            Rewrite the term in a given basis.

            INPUT:

            - ``basis`` -- either ``None`` (default) or a function such that
              ``basis(d)`` is a basis of the weight ``d`` multiple zeta values.
              If ``None``, the Hoffman basis is used.

            EXAMPLES::

                sage: z = Multizeta(5) + Multizeta(1,4) + Multizeta(3,2) - 5 * Multizeta(2,3)
                sage: z.simplify_full()
                -22/5*ζ(2,3) + 12/5*ζ(3,2)
                sage: z.simplify_full(basis=z.parent().basis_filtration)
                18*ζ(1,4) - ζ(5)

                sage: z == z.simplify_full() == z.simplify_full(basis=z.parent().basis_filtration)
                True

            Be careful, that this does not optimize the number of terms::

                sage: Multizeta(7).simplify_full()
                352/151*ζ(2,2,3) + 672/151*ζ(2,3,2) + 528/151*ζ(3,2,2)

            TESTS::

                sage: Multizetas(QQ).one().simplify_full()
                ζ()
            """
        def __bool__(self) -> bool:
            """
            EXAMPLES::

                sage: bool(Multizeta(2))
                True
                sage: bool(3*Multizeta(4) - 4*Multizeta(2,2))
                False
            """
        def is_zero(self) -> bool:
            """
            Return whether this element is zero.

            EXAMPLES::

                sage: M = Multizeta

                sage: (4*M(2,3) + 6*M(3,2) - 5*M(5)).is_zero()
                True
                sage: (3*M(4) - 4*M(2,2)).is_zero()
                True
                sage: (4*M(2,3) + 6*M(3,2) + 3*M(4) - 5*M(5) - 4*M(2,2)).is_zero()
                True

                sage: (4*M(2,3) + 6*M(3,2) - 4*M(5)).is_zero()
                False
                sage: (M(4) - M(2,2)).is_zero()
                False
                sage: (4*M(2,3) + 6*M(3,2) + 3*M(4) - 4*M(5) - 4*M(2,2)).is_zero()
                False
            """
        def __hash__(self) -> int:
            """
            Return the hash of ``self``.

            EXAMPLES::

                sage: M = Multizeta
                sage: hash(M(1,2)) != hash(M(6))
                True
            """
        def phi(self):
            """
            Return the image of ``self`` by the morphism ``phi``.

            This sends multiple zeta values to the auxiliary F-algebra.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: M((1,2)).phi()
                f3

            TESTS::

                sage: A = QQ['u']
                sage: u = A.gen()
                sage: M = Multizetas(A)
                sage: tst = u*M((1,2))+M((3,))
                sage: tst.phi()
                (u+1)*f3
            """
        def phi_as_vector(self):
            """
            Return the image of ``self`` by the morphism ``phi`` as a vector.

            The morphism ``phi`` sends multiple zeta values to the algebra
            :func:`F_ring`. Then the image is expressed as a vector in
            a fixed basis of one graded component of this algebra.

            This is only defined for homogeneous elements.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: M((3,2)).phi_as_vector()
                (9/2, -2)
                sage: M(0).phi_as_vector()
                ()

            TESTS::

                sage: (M((4,))+M((1,2))).phi_as_vector()
                Traceback (most recent call last):
                ...
                ValueError: only defined for homogeneous elements
            """
        def numerical_approx(self, prec=None, digits=None, algorithm=None):
            """
            Return a numerical value for this element.

            EXAMPLES::

                sage: M = Multizetas(QQ)
                sage: M(Word((3,2))).n()  # indirect doctest
                0.711566197550572
                sage: parent(M(Word((3,2))).n())
                Real Field with 53 bits of precision

                sage: (M((3,)) * M((2,))).n(prec=80)
                1.9773043502972961181971
                sage: M((1,2)).n(70)
                1.2020569031595942854

                sage: M((3,)).n(digits=10)
                1.202056903

            If you plan to use intensively numerical approximation at high precision,
            you might want to add more values and/or accuracy to the cache::

                sage: from sage.modular.multiple_zeta import MultizetaValues
                sage: M = MultizetaValues()
                sage: M.update(max_weight=9, prec=2048)
                sage: M
                Cached multiple zeta values at precision 2048 up to weight 9
                sage: M.reset()  # restore precision for the other doctests

            TESTS::

                sage: Multizetas(QQ).zero().n()
                0.000000000000000
            """

class Multizetas_iterated(CombinatorialFreeModule):
    """
    Secondary class for the algebra of multiple zeta values.

    This is used to represent multiple zeta values as iterated integrals
    of the differential forms `\\omega_0 = dt/t` and `\\omega_1 = dt/(t-1)`.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import Multizetas_iterated
        sage: M = Multizetas_iterated(QQ); M
        Algebra of motivic multiple zeta values as convergent iterated
        integrals over Rational Field
        sage: M((1,0))
        I(10)
        sage: M((1,0))**2
        4*I(1100) + 2*I(1010)
        sage: M((1,0))*M((1,0,0))
        6*I(11000) + 3*I(10100) + I(10010)
    """
    def __init__(self, R) -> None:
        """
        TESTS::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: TestSuite(M).run()  # not tested
            sage: M.category()
            Category of commutative no zero divisors graded algebras
            with basis over Rational Field
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the unit for the algebra.

        This is the empty word.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: M.one_basis()
            word:
        """
    def product_on_basis(self, w1, w2):
        """
        Compute the product of two monomials.

        This is the shuffle product.

        INPUT:

        - ``w1``, ``w2`` -- words in 0 and 1

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = Word([1,0])
            sage: M.product_on_basis(x,x)
            4*I(1100) + 2*I(1010)
            sage: y = Word([1,1,0])
            sage: M.product_on_basis(y,x)
            I(10110) + 3*I(11010) + 6*I(11100)
        """
    def half_product_on_basis(self, w1, w2):
        """
        Compute half of the product of two monomials.

        This is half of the shuffle product.

        .. WARNING:: This is not a motivic operation.

        INPUT:

        - ``w1``, ``w2`` -- monomials

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = Word([1,0])
            sage: M.half_product_on_basis(x,x)
            2*I(1100) + I(1010)
        """
    @lazy_attribute
    def half_product(self):
        """
        Compute half of the product of two elements.

        This is half of the shuffle product.

        .. WARNING:: This is not a motivic operation.

        INPUT:

        - ``w1``, ``w2`` -- elements

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = M(Word([1,0]))
            sage: M.half_product(x,x)
            2*I(1100) + I(1010)
        """
    def coproduct_on_basis(self, w):
        """
        Return the motivic coproduct of a monomial.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: M.coproduct_on_basis([1,0])
            I() # I(10)

            sage: M.coproduct_on_basis((1,0,1,0))
            I() # I(1010)
        """
    @lazy_attribute
    def coproduct(self):
        """
        Return the motivic coproduct of an element.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: a = 3*Multizeta(1,4) + Multizeta(2,3)
            sage: M.coproduct(a.iterated())
            3*I() # I(11000) + I() # I(10100) + 3*I(11000) # I()
            + I(10100) # I()
        """
    @lazy_attribute
    def composition(self):
        """
        Convert to the algebra of multiple zeta values of composition style.

        This means the algebra :class:`Multizetas`.

        This is also available as a method of elements.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = M((1,0))
            sage: M.composition(2*x)
            -2*ζ(2)
            sage: x = M((1,0,1,0,0))
            sage: M.composition(x)
            ζ(2,3)
        """
    def composition_on_basis(self, w, basering=None):
        """
        Convert to the algebra of multiple zeta values of composition style.

        INPUT:

        - ``basering`` -- (optional) choice of the coefficient ring

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = Word((1,0,1,0,0))
            sage: M.composition_on_basis(x)
            ζ(2,3)
            sage: x = Word((1,0,1,0,0,1,0))
            sage: M.composition_on_basis(x)
            -ζ(2,3,2)
        """
    def dual_on_basis(self, w):
        """
        Return the order of the word and exchange letters 0 and 1.

        This is an involution.

        INPUT:

        - ``w`` -- a word in 0 and 1

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = Word((1,0,1,0,0))
            sage: M.dual_on_basis(x)
            -I(11010)
        """
    def degree_on_basis(self, w):
        """
        Return the degree of the monomial ``w``.

        This is the length of the word.

        INPUT:

        - ``w`` -- a word in 0 and 1

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: x = Word((1,0,1,0,0))
            sage: M.degree_on_basis(x)
            5
        """
    def D_on_basis(self, k, w):
        """
        Return the action of the operator `D_k` on the monomial ``w``.

        This is one main tool in the procedure that allows
        to map the algebra of multiple zeta values to
        the F Ring.

        INPUT:

        - ``k`` -- an odd integer, at least 3

        - ``w`` -- a word in 0 and 1

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: M.D_on_basis(3,(1,1,1,0,0))
            I(110) # I(10) + 2*I(100) # I(10)

            sage: M.D_on_basis(3,(1,0,1,0,0))
            3*I(100) # I(10)
            sage: M.D_on_basis(5,(1,0,0,0,1,0,0,1,0,0))
            10*I(10000) # I(10100)
        """
    def D(self, k):
        """
        Return the operator `D_k`.

        INPUT:

        - ``k`` -- an odd integer, at least 3

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: D3 = M.D(3)
            sage: elt = M((1,0,1,0,0)) + 2 * M((1,1,0,0,1,0))
            sage: D3(elt)
            -6*I(100) # I(110) + 3*I(100) # I(10)
        """
    @cached_method
    def phi_extended(self, w):
        """
        Return the image of the monomial ``w`` by the morphism ``phi``.

        INPUT:

        - ``w`` -- a word in 0 and 1

        OUTPUT: an element in the auxiliary F-algebra

        The coefficients are in the base ring.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: M.phi_extended((1,0))
            -f2
            sage: M.phi_extended((1,0,0))
            -f3
            sage: M.phi_extended((1,1,0))
            f3
            sage: M.phi_extended((1,0,1,0,0))
            -11/2*f5 + 3*f2*f3

        More complicated examples::

            sage: from sage.modular.multiple_zeta import composition_to_iterated
            sage: M.phi_extended(composition_to_iterated((4,3)))
            -18*f7 + 10*f2*f5 + 2/5*f2^2*f3

            sage: M.phi_extended(composition_to_iterated((3,4)))
            17*f7 - 10*f2*f5

            sage: M.phi_extended(composition_to_iterated((4,2)))
            -2*f3f3 + 10/21*f2^3
            sage: M.phi_extended(composition_to_iterated((3,5)))
            -5*f5f3
            sage: M.phi_extended(composition_to_iterated((3,7)))
            -6*f5f5 - 14*f7f3

            sage: M.phi_extended(composition_to_iterated((3,3,2)))
            9*f3f5 - 9/2*f5f3 - 4*f2*f3f3 - 793/875*f2^4

        TESTS::

           sage: M.phi_extended(tuple())
           1
        """
    @lazy_attribute
    def phi(self):
        """
        Return the morphism ``phi``.

        This sends multiple zeta values to the auxiliary F-algebra.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import Multizetas_iterated
            sage: M = Multizetas_iterated(QQ)
            sage: m = Multizeta(1,0,1,0) + 2*Multizeta(1,1,0,0); m
            2*I(1100) + I(1010)
            sage: M.phi(m)
            1/2*f2^2

            sage: Z = Multizeta
            sage: B5 = [3*Z(1,4) + 2*Z(2,3) + Z(3,2), 3*Z(1,4) + Z(2,3)]
            sage: [M.phi(b.iterated()) for b in B5]
            [-1/2*f5 + f2*f3, 1/2*f5]

            sage: B6 = [6*Z(1,5) + 3*Z(2,4) + Z(3,3),
            ....:  6*Z(1,1,4) + 4*Z(1,2,3) + 2*Z(1,3,2) + 2*Z(2,1,3) + Z(2,2,2)]
            sage: [M.phi(b.iterated()) for b in B6]
            [f3f3, 1/6*f2^3]
        """
    class Element(CombinatorialFreeModule.Element):
        def simplify(self):
            """
            Gather terms using the duality relations.

            This can help to lower the number of monomials.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: z = 4*M((1,0,0)) + 3*M((1,1,0))
                sage: z.simplify()
                I(100)
            """
        def coproduct(self):
            """
            Return the coproduct of ``self``.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: a = 3*Multizeta(1,3) + Multizeta(2,3)
                sage: a.iterated().coproduct()
                3*I() # I(1100) + I() # I(10100) + I(10100) # I() + 3*I(100) # I(10)
            """
        def composition(self):
            """
            Convert to the algebra of multiple zeta values of composition style.

            This means the algebra :class:`Multizetas`.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: x = M((1,0,1,0))
                sage: x.composition()
                ζ(2,2)
                sage: x = M((1,0,1,0,0))
                sage: x.composition()
                ζ(2,3)
                sage: x = M((1,0,1,0,0,1,0))
                sage: x.composition()
                -ζ(2,3,2)
            """
        def numerical_approx(self, prec=None, digits=None, algorithm=None):
            """
            Return a numerical approximation as a sage real.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: x = M((1,0,1,0))
                sage: y = M((1, 0, 0))
                sage: (3*x+y).n()  # indirect doctest
                1.23317037269047
            """
        def phi(self):
            """
            Return the image of ``self`` by the morphism ``phi``.

            This sends multiple zeta values to the auxiliary F-algebra.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: M((1,1,0)).phi()
                f3
            """
        def __bool__(self) -> bool:
            """
            TESTS::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: bool(M(0))
                False
                sage: bool(M(1))
                True
                sage: bool(M((1,0,0)))
                True
            """
        def is_zero(self) -> bool:
            """
            Return whether this element is zero.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import Multizetas_iterated
                sage: M = Multizetas_iterated(QQ)
                sage: M(0).is_zero()
                True
                sage: M(1).is_zero()
                False
                sage: (M((1,1,0)) - -M((1,0,0))).is_zero()
                True
            """

class All_iterated(CombinatorialFreeModule):
    '''
    Auxiliary class for multiple zeta value as generalized iterated integrals.

    This is used to represent multiple zeta values as possibly
    divergent iterated integrals
    of the differential forms `\\omega_0 = dt/t` and `\\omega_1 = dt/(t-1)`.

    This means that the elements are symbols
    `I(a_0 ; a_1,a_2,...a_n ; a_{n+1})`
    where all arguments, including the starting and ending points
    can be 0 or 1.

    This comes with a "regularise" method mapping
    to :class:`Multizetas_iterated`.

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import All_iterated
        sage: M = All_iterated(QQ); M
        Space of motivic multiple zeta values as general iterated integrals
        over Rational Field
        sage: M((0,1,0,1))
        I(0;10;1)
        sage: x = M((1,1,0,0)); x
        I(1;10;0)
        sage: x.regularise()
        -I(10)
    '''
    def __init__(self, R) -> None:
        """
        TESTS::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: TestSuite(M).run()  # not tested
        """
    def dual_on_basis(self, w):
        """
        Reverse the word and exchange the letters 0 and 1.

        This is the operation R4 in [Brown2012]_.

        This should be used only when `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((0,0,1,0,1))
            sage: M.dual_on_basis(x)
            I(0;010;1)
            sage: x = Word((0,1,0,1,1))
            sage: M.dual_on_basis(x)
            -I(0;010;1)
        """
    @lazy_attribute
    def dual(self):
        """
        Reverse words and exchange the letters 0 and 1.

        This is the operation R4 in [Brown2012]_.

        This should be used only when `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((0,0,1,1,1))
            sage: y = Word((0,0,1,0,1))
            sage: M.dual(M(x)+5*M(y))
            5*I(0;010;1) - I(0;001;1)
        """
    def reversal_on_basis(self, w):
        """
        Reverse the word if necessary.

        This is the operation R3 in [Brown2012]_.

        This reverses the word only if `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((1,0,1,0,0))
            sage: M.reversal_on_basis(x)
            -I(0;010;1)
            sage: x = Word((0,0,1,1,1))
            sage: M.reversal_on_basis(x)
            I(0;011;1)
        """
    @lazy_attribute
    def reversal(self):
        """
        Reverse words if necessary.

        This is the operation R3 in [Brown2012]_.

        This reverses the word only if `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((1,0,1,0,0))
            sage: y = Word((0,0,1,1,1))
            sage: M.reversal(M(x)+2*M(y))
            2*I(0;011;1) - I(0;010;1)
        """
    def expand_on_basis(self, w):
        """
        Perform an expansion as a linear combination.

        This is the operation R2 in [Brown2012]_.

        This should be used only when `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((0,0,1,0,1))
            sage: M.expand_on_basis(x)
            -2*I(0;100;1)

            sage: x = Word((0,0,0,1,0,1,0,0,1))
            sage: M.expand_on_basis(x)
            6*I(0;1010000;1) + 6*I(0;1001000;1) + 3*I(0;1000100;1)

            sage: x = Word((0,1,1,0,1))
            sage: M.expand_on_basis(x)
            I(0;110;1)
        """
    @lazy_attribute
    def expand(self):
        """
        Perform an expansion as a linear combination.

        This is the operation R2 in [Brown2012]_.

        This should be used only when `a_0 = 0` and `a_{n+1} = 1`.

        EXAMPLES::

            sage: from sage.modular.multiple_zeta import All_iterated
            sage: M = All_iterated(QQ)
            sage: x = Word((0,0,1,0,1))
            sage: y = Word((0,0,1,1,1))
            sage: M.expand(M(x)+2*M(y))
            -2*I(0;110;1) - 2*I(0;101;1) - 2*I(0;100;1)
            sage: M.expand(M([0,1,1,0,1]))
            I(0;110;1)
            sage: M.expand(M([0,1,0,0,1]))
            I(0;100;1)
        """
    class Element(CombinatorialFreeModule.Element):
        def conversion(self):
            """
            Conversion to the :class:`Multizetas_iterated`.

            This assumed that the element has been prepared.

            Not to be used directly.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import All_iterated
                sage: M = All_iterated(QQ)
                sage: x = Word((0,1,0,0,1))
                sage: y = M(x).conversion(); y
                I(100)
                sage: y.parent()
                Algebra of motivic multiple zeta values as convergent iterated
                integrals over Rational Field
            """
        def regularise(self):
            """
            Conversion to the :class:`Multizetas_iterated`.

            This is the regularisation procedure, done in several steps.

            EXAMPLES::

                sage: from sage.modular.multiple_zeta import All_iterated
                sage: M = All_iterated(QQ)
                sage: x = Word((0,0,1,0,1))
                sage: M(x).regularise()
                -2*I(100)
                sage: x = Word((0,1,1,0,1))
                sage: M(x).regularise()
                I(110)

                sage: x = Word((1,0,1,0,0))
                sage: M(x).regularise()
                2*I(100)
            """

def coeff_phi(w):
    """
    Return the coefficient of `f_k` in the image by ``phi``.

    INPUT:

    - ``w`` -- a word in 0 and 1 with `k` letters (where `k` is odd)

    OUTPUT: a rational number

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import coeff_phi
        sage: coeff_phi(Word([1,0,0]))
        -1
        sage: coeff_phi(Word([1,1,0]))
        1
        sage: coeff_phi(Word([1,1,0,1,0]))
        11/2
        sage: coeff_phi(Word([1,1,0,0,0,1,0]))
        109/16
    """
def phi_on_multiplicative_basis(compo):
    """
    Compute ``phi`` on one single multiple zeta value.

    INPUT:

    - ``compo`` -- a composition (in the hardcoded multiplicative base)

    OUTPUT: an element in :func:`F_ring` with rational coefficients

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import phi_on_multiplicative_basis
        sage: phi_on_multiplicative_basis((2,))
        f2
        sage: phi_on_multiplicative_basis((3,))
        f3
    """
def phi_on_basis(L):
    """
    Compute the value of phi on the hardcoded basis.

    INPUT:

    - ``L`` -- list of compositions; each composition in the hardcoded basis

    This encodes a product of multiple zeta values.

    OUTPUT: an element in :func:`F_ring`

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import phi_on_basis
        sage: phi_on_basis([(3,),(3,)])
        2*f3f3
        sage: phi_on_basis([(2,),(2,)])
        f2^2
        sage: phi_on_basis([(2,),(3,),(3,)])
        2*f2*f3f3
    """
def D_on_compo(k, compo):
    """
    Return the value of the operator `D_k` on a multiple zeta value.

    This is now only used as a place to keep many doctests.

    INPUT:

    - ``k`` -- an odd integer

    - ``compo`` -- a composition

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import D_on_compo
        sage: D_on_compo(3,(2,3))
        3*I(100) # I(10)

        sage: D_on_compo(3,(4,3))
        I(100) # I(1000)
        sage: D_on_compo(5,(4,3))
        10*I(10000) # I(10)

        sage: [D_on_compo(k, [3,5]) for k in (3,5,7)]
        [0, -5*I(10000) # I(100), 0]

        sage: [D_on_compo(k, [3,7]) for k in (3,5,7,9)]
        [0, -6*I(10000) # I(10000), -14*I(1000000) # I(100), 0]

        sage: D_on_compo(3,(4,3,3))
        -I(100) # I(1000100)
        sage: D_on_compo(5,(4,3,3))
        -10*I(10000) # I(10100)
        sage: D_on_compo(7,(4,3,3))
        4*I(1001000) # I(100) + 2*I(1000100) # I(100)

        sage: [D_on_compo(k,(1,3,1,3,1,3)) for k in range(3,10,2)]
        [0, 0, 0, 0]
    """
def compute_u_on_compo(compo):
    """
    Compute the value of the map ``u`` on a multiple zeta value.

    INPUT:

    - ``compo`` -- a composition

    OUTPUT: an element of :func:`F_ring` over `\\QQ`

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import compute_u_on_compo
        sage: compute_u_on_compo((2,4))
        2*f3f3
        sage: compute_u_on_compo((2,3,2))
        -11/2*f2*f5
        sage: compute_u_on_compo((3,2,3,2))
        -75/4*f3f7 + 81/4*f5f5 + 75/8*f7f3 + 11*f2*f3f5 - 9*f2*f5f3
    """
def compute_u_on_basis(w):
    """
    Compute the value of ``u`` on a multiple zeta value.

    INPUT:

    - ``w`` -- a word in 0,1

    OUTPUT: an element of :func:`F_ring` over `\\QQ`

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import compute_u_on_basis
        sage: compute_u_on_basis((1,0,0,0,1,0))
        -2*f3f3

        sage: compute_u_on_basis((1,1,1,0,0))
        f2*f3

        sage: compute_u_on_basis((1,0,0,1,0,0,0,0))
        -5*f5f3

        sage: compute_u_on_basis((1,0,1,0,0,1,0))
        11/2*f2*f5

        sage: compute_u_on_basis((1,0,0,1,0,1,0,0,1,0))
        -75/4*f3f7 + 81/4*f5f5 + 75/8*f7f3 + 11*f2*f3f5 - 9*f2*f5f3
    """
@cached_function
def rho_matrix_inverse(n):
    """
    Return the matrix of the inverse of ``rho``.

    This is the matrix in the chosen bases, namely the hardcoded basis
    of multiple zeta values and the natural basis of the F ring.

    INPUT:

    - ``n`` -- integer

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import rho_matrix_inverse
        sage: rho_matrix_inverse(3)
        [1]
        sage: rho_matrix_inverse(8)
        [-1/5    0    0    0]
        [ 1/5    1    0    0]
        [   0    0  1/2    0]
        [   0    0    0    1]
    """
def rho_inverse(elt):
    '''
    Return the image by the inverse of ``rho``.

    INPUT:

    - ``elt`` -- an homogeneous element of the F ring

    OUTPUT: a linear combination of multiple zeta values

    EXAMPLES::

        sage: from sage.modular.multiple_zeta import rho_inverse
        sage: from sage.modular.multiple_zeta_F_algebra import F_algebra
        sage: A = F_algebra(QQ)
        sage: f = A.gen
        sage: rho_inverse(f(3))
        ζ(3)
        sage: rho_inverse(f(9))
        ζ(9)
        sage: rho_inverse(A("53"))
        -1/5*ζ(3,5)
    '''
