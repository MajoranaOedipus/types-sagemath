from sage.arith.misc import binomial as binomial
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule, CombinatorialFreeModule_Tensor as CombinatorialFreeModule_Tensor
from sage.combinat.integer_lists import IntegerListsLex as IntegerListsLex
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.combinat.symmetric_group_algebra import SymmetricGroupAlgebra as SymmetricGroupAlgebra
from sage.combinat.tableau import SemistandardTableaux as SemistandardTableaux
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def schur_representative_indices(n, r):
    """
    Return a set which functions as a basis of `S_K(n,r)`.

    More specifically, the basis for `S_K(n,r)` consists of
    equivalence classes of pairs of tuples of length ``r`` on the alphabet
    `\\{1, \\dots, n\\}`, where the equivalence relation is simultaneous
    permutation of the two tuples.  We can therefore fix a
    representative for each equivalence class in which the entries of
    the first tuple weakly increase, and the entries of the second tuple
    whose corresponding values in the first tuple are equal, also
    weakly increase.

    EXAMPLES::

        sage: from sage.algebras.schur_algebra import schur_representative_indices
        sage: schur_representative_indices(2, 2)
        [((1, 1), (1, 1)), ((1, 1), (1, 2)),
         ((1, 1), (2, 2)), ((1, 2), (1, 1)),
         ((1, 2), (1, 2)), ((1, 2), (2, 1)),
         ((1, 2), (2, 2)), ((2, 2), (1, 1)),
         ((2, 2), (1, 2)), ((2, 2), (2, 2))]
    """
def schur_representative_from_index(i0, i1):
    """
    Simultaneously reorder a pair of tuples to obtain the equivalent
    element of the distinguished basis of the Schur algebra.

    .. SEEALSO::

        :func:`schur_representative_indices`

    INPUT:

    - A pair of tuples of length `r` with elements in `\\{1,\\dots,n\\}`

    OUTPUT: the corresponding pair of tuples ordered correctly

    EXAMPLES::

        sage: from sage.algebras.schur_algebra import schur_representative_from_index
        sage: schur_representative_from_index([2,1,2,2], [1,3,0,0])
        ((1, 2, 2, 2), (3, 0, 0, 1))
    """

class SchurAlgebra(CombinatorialFreeModule):
    """
    A Schur algebra.

    Let `R` be a commutative ring, `n` be a positive integer, and `r`
    be a nonnegative integer. Define `A_R(n,r)` to be the set of
    homogeneous polynomials of degree `r` in `n^2` variables `x_{ij}`.
    Therefore we can write `R[x_{ij}] = \\bigoplus_{r \\geq 0} A_R(n,r)`,
    and `R[x_{ij}]` is known to be a bialgebra with coproduct given by
    `\\Delta(x_{ij}) = \\sum_l x_{il} \\otimes x_{lj}` and counit
    `\\varepsilon(x_{ij}) = \\delta_{ij}`. Therefore `A_R(n,r)` is a
    subcoalgebra of `R[x_{ij}]`. The *Schur algebra* `S_R(n,r)` is the
    linear dual to `A_R(n,r)`, that is `S_R(n,r) := \\hom(A_R(n,r), R)`,
    and `S_R(n,r)` obtains its algebra structure naturally by dualizing
    the comultiplication of `A_R(n,r)`.

    Let `V = R^n`. One of the most important properties of the Schur
    algebra `S_R(n, r)` is that it is isomorphic to the endomorphisms
    of `V^{\\otimes r}` which commute with the natural action of `S_r`.

    EXAMPLES::

        sage: S = SchurAlgebra(ZZ, 2, 2); S
        Schur algebra (2, 2) over Integer Ring

    REFERENCES:

    - [Gr2007]_
    - :wikipedia:`Schur_algebra`
    """
    def __init__(self, R, n, r) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: S = SchurAlgebra(ZZ, 2, 2)
            sage: TestSuite(S).run()

        ::

            sage: SchurAlgebra(ZZ, -2, 2)
            Traceback (most recent call last):
            ...
            ValueError: n (=-2) must be a positive integer
            sage: SchurAlgebra(ZZ, 2, -2)
            Traceback (most recent call last):
            ...
            ValueError: r (=-2) must be a nonnegative integer
            sage: SchurAlgebra('niet', 2, 2)
            Traceback (most recent call last):
            ...
            ValueError: R (=niet) must be a commutative ring
        """
    @cached_method
    def one(self):
        """
        Return the element `1` of ``self``.

        EXAMPLES::

            sage: S = SchurAlgebra(ZZ, 2, 2)
            sage: e = S.one(); e
            S((1, 1), (1, 1)) + S((1, 2), (1, 2)) + S((2, 2), (2, 2))

            sage: x = S.an_element()
            sage: x * e == x
            True
            sage: all(e * x == x for x in S.basis())
            True

            sage: S = SchurAlgebra(ZZ, 4, 4)
            sage: e = S.one()
            sage: x = S.an_element()
            sage: x * e == x
            True
        """
    def product_on_basis(self, e_ij, e_kl):
        """
        Return the product of basis elements.

        EXAMPLES::

            sage: S = SchurAlgebra(QQ, 2, 3)
            sage: B = S.basis()

        If we multiply two basis elements `x` and `y`, such that
        `x[1]` and `y[0]` are not permutations of each other, the
        result is zero::

            sage: S.product_on_basis(((1, 1, 1), (1, 1, 2)), ((1, 2, 2), (1, 1, 2)))
            0

        If we multiply a basis element `x` by a basis element which
        consists of the same tuple repeated twice (on either side),
        the result is either zero (if the previous case applies) or `x`::

            sage: ww = B[((1, 2, 2), (1, 2, 2))]
            sage: x = B[((1, 2, 2), (1, 1, 2))]
            sage: ww * x
            S((1, 2, 2), (1, 1, 2))

        An arbitrary product, on the other hand, may have multiplicities::

            sage: x = B[((1, 1, 1), (1, 1, 2))]
            sage: y = B[((1, 1, 2), (1, 2, 2))]
            sage: x * y
            2*S((1, 1, 1), (1, 2, 2))
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        The dimension of the Schur algebra `S_R(n, r)` is

        .. MATH::

            \\dim S_R(n,r) = \\binom{n^2+r-1}{r}.

        EXAMPLES::

            sage: S = SchurAlgebra(QQ, 4, 2)
            sage: S.dimension()
            136
            sage: S = SchurAlgebra(QQ, 2, 4)
            sage: S.dimension()
            35
        """

class SchurTensorModule(CombinatorialFreeModule_Tensor):
    """
    The space `V^{\\otimes r}` where `V = R^n` equipped with a left action
    of the Schur algebra `S_R(n,r)` and a right action of the symmetric
    group `S_r`.

    Let `R` be a commutative ring and `V = R^n`. We consider the module
    `V^{\\otimes r}` equipped with a natural right action of the symmetric
    group `S_r` given by

    .. MATH::

        (v_1 \\otimes v_2 \\otimes \\cdots \\otimes v_n) \\sigma
        = v_{\\sigma(1)} \\otimes v_{\\sigma(2)} \\otimes \\cdots
        \\otimes v_{\\sigma(n)}.

    The Schur algebra `S_R(n,r)` is naturally isomorphic to the
    endomorphisms of `V^{\\otimes r}` which commutes with the `S_r` action.
    We get the natural left action of `S_R(n,r)` by this isomorphism.

    EXAMPLES::

        sage: T = SchurTensorModule(QQ, 2, 3); T
        The 3-fold tensor product of a free module of dimension 2
         over Rational Field
        sage: A = SchurAlgebra(QQ, 2, 3)
        sage: P = Permutations(3)
        sage: t = T.an_element(); t
        2*B[1] # B[1] # B[1] + 2*B[1] # B[1] # B[2] + 3*B[1] # B[2] # B[1]
        sage: a = A.an_element(); a
        2*S((1, 1, 1), (1, 1, 1)) + 2*S((1, 1, 1), (1, 1, 2))
         + 3*S((1, 1, 1), (1, 2, 2))
        sage: p = P.an_element(); p
        [3, 1, 2]
        sage: y = a * t; y
        14*B[1] # B[1] # B[1]
        sage: y * p
        14*B[1] # B[1] # B[1]
        sage: z = t * p; z
        2*B[1] # B[1] # B[1] + 3*B[1] # B[1] # B[2] + 2*B[2] # B[1] # B[1]
        sage: a * z
        14*B[1] # B[1] # B[1]

    We check the commuting action property::

        sage: all( (bA * bT) * p == bA * (bT * p)
        ....:      for bT in T.basis() for bA in A.basis() for p in P)
        True
    """
    def __init__(self, R, n, r) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: T = SchurTensorModule(QQ, 2, 3)
            sage: TestSuite(T).run()
        """
    def construction(self) -> None:
        """
        Return ``None``.

        There is no functorial construction for ``self``.

        EXAMPLES::

            sage: T = SchurTensorModule(QQ, 2, 3)
            sage: T.construction()
        """
    class Element(CombinatorialFreeModule_Tensor.Element): ...

def GL_irreducible_character(n, mu, KK):
    """
    Return the character of the irreducible module indexed by ``mu``
    of `GL(n)` over the field ``KK``.

    INPUT:

    - ``n`` -- positive integer
    - ``mu`` -- a partition of at most `n` parts
    - ``KK`` -- a field

    OUTPUT: a symmetric function which should be interpreted in `n`
    variables to be meaningful as a character

    EXAMPLES:

    Over `\\QQ`, the irreducible character for `\\mu` is the Schur
    function associated to `\\mu`, plus garbage terms (Schur
    functions associated to partitions with more than `n` parts)::

        sage: from sage.algebras.schur_algebra import GL_irreducible_character
        sage: sbasis = SymmetricFunctions(QQ).s()
        sage: z = GL_irreducible_character(2, [2], QQ)
        sage: sbasis(z)
        s[2]

        sage: z = GL_irreducible_character(4, [3, 2], QQ)
        sage: sbasis(z)
        -5*s[1, 1, 1, 1, 1] + s[3, 2]

    Over a Galois field, the irreducible character for `\\mu` will
    in general be smaller.

    In characteristic `p`, for a one-part partition `(r)`, where
    `r = a_0 + p a_1 + p^2 a_2 + \\dots`, the result is (see [Gr2007]_,
    after 5.5d) the product of `h[a_0], h[a_1]( pbasis[p]), h[a_2]
    ( pbasis[p^2]), \\dots,` which is consistent with the following ::

        sage: from sage.algebras.schur_algebra import GL_irreducible_character
        sage: GL_irreducible_character(2, [7], GF(3))
        m[4, 3] + m[6, 1] + m[7]
    """
