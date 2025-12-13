from _typeshed import Incomplete
from sage.algebras.cellular_basis import CellularBasis as CellularBasis
from sage.algebras.group_algebra import GroupAlgebra_class as GroupAlgebra_class
from sage.arith.misc import factorial as factorial
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.categories.weyl_groups import WeylGroups as WeylGroups
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.partition import Partitions as Partitions, Partitions_n as Partitions_n
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations, from_permutation_group_element as from_permutation_group_element
from sage.combinat.permutation_cython import left_action_same_n as left_action_same_n, right_action_same_n as right_action_same_n
from sage.combinat.skew_tableau import SkewTableau as SkewTableau
from sage.combinat.tableau import StandardTableaux as StandardTableaux, StandardTableaux_shape as StandardTableaux_shape, StandardTableaux_size as StandardTableaux_size, Tableau as Tableau
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.modules.free_module_element import vector as vector
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def SymmetricGroupAlgebra(R, W, category=None):
    '''
    Return the symmetric group algebra of order ``W`` over the ring ``R``.

    INPUT:

    - ``W`` -- a symmetric group; alternatively an integer `n` can be
      provided, as shorthand for ``Permutations(n)``.
    - ``R`` -- a base ring
    - ``category`` -- a category (default: the category of ``W``)

    This supports several implementations of the symmetric group. At
    this point this has been tested with ``W=Permutations(n)`` and
    ``W=SymmetricGroup(n)``.

    .. WARNING::

        Some features are failing in the latter case, in particular if
        the domain of the symmetric group is not `1,\\ldots,n`.

    .. NOTE::

        The brave can also try setting ``W=WeylGroup([\'A\',n-1])``, but
        little support for this currently exists.

    EXAMPLES::

        sage: QS3 = SymmetricGroupAlgebra(QQ, 3); QS3
        Symmetric group algebra of order 3 over Rational Field
        sage: QS3(1)
        [1, 2, 3]
        sage: QS3(2)
        2*[1, 2, 3]
        sage: basis = [QS3(p) for p in Permutations(3)]
        sage: a = sum(basis); a
        [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
        sage: a^2
        6*[1, 2, 3] + 6*[1, 3, 2] + 6*[2, 1, 3] + 6*[2, 3, 1]
        + 6*[3, 1, 2] + 6*[3, 2, 1]
        sage: a^2 == 6*a
        True
        sage: b = QS3([3, 1, 2])
        sage: b
        [3, 1, 2]
        sage: b*a
        [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
        sage: b*a == a
        True

    We now construct the symmetric group algebra by providing
    explicitly the underlying group::

        sage: SGA = SymmetricGroupAlgebra(QQ, Permutations(4)); SGA
        Symmetric group algebra of order 4 over Rational Field
        sage: SGA.group()
        Standard permutations of 4
        sage: SGA.an_element()
        [1, 2, 3, 4] + 2*[1, 2, 4, 3] + 3*[1, 3, 2, 4] + [4, 1, 2, 3]

        sage: SGA = SymmetricGroupAlgebra(QQ, SymmetricGroup(4)); SGA
        Symmetric group algebra of order 4 over Rational Field
        sage: SGA.group()
        Symmetric group of order 4! as a permutation group
        sage: SGA.an_element()
        () + (2,3,4) + 2*(1,3)(2,4) + 3*(1,4)(2,3)

        sage: SGA = SymmetricGroupAlgebra(QQ, WeylGroup(["A",3], prefix=\'s\')); SGA
        Symmetric group algebra of order 4 over Rational Field
        sage: SGA.group()
        Weyl Group of type [\'A\', 3] (as a matrix group acting
        on the ambient space)
        sage: SGA.an_element()
        s1*s2*s3 + 3*s2*s3*s1*s2 + 2*s3*s1 + 1

    The preferred way to construct the symmetric group algebra is to
    go through the usual ``algebra`` method::

        sage: SGA = Permutations(3).algebra(QQ); SGA
        Symmetric group algebra of order 3 over Rational Field
        sage: SGA.group()
        Standard permutations of 3

        sage: SGA = SymmetricGroup(3).algebra(QQ); SGA
        Symmetric group algebra of order 3 over Rational Field
        sage: SGA.group()
        Symmetric group of order 3! as a permutation group

    The canonical embedding from the symmetric group algebra of order
    `n` to the symmetric group algebra of order `p > n` is available as
    a coercion::

        sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
        sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
        sage: QS4.coerce_map_from(QS3)
        Generic morphism:
          From: Symmetric group algebra of order 3 over Rational Field
          To:   Symmetric group algebra of order 4 over Rational Field

        sage: x3  = QS3([3,1,2]) + 2 * QS3([2,3,1]); x3
        2*[2, 3, 1] + [3, 1, 2]
        sage: QS4(x3)
        2*[2, 3, 1, 4] + [3, 1, 2, 4]

    This allows for mixed expressions::

        sage: x4  = 3 * QS4([3, 1, 4, 2])
        sage: x3 + x4
        2*[2, 3, 1, 4] + [3, 1, 2, 4] + 3*[3, 1, 4, 2]

        sage: QS0 = SymmetricGroupAlgebra(QQ, 0)
        sage: QS1 = SymmetricGroupAlgebra(QQ, 1)
        sage: x0 = QS0([])
        sage: x1 = QS1([1])
        sage: x0 * x1
        [1]
        sage: x3 - (2*x0 + x1) - x4
        -3*[1, 2, 3, 4] + 2*[2, 3, 1, 4] + [3, 1, 2, 4] - 3*[3, 1, 4, 2]

    Caveat: to achieve this, constructing ``SymmetricGroupAlgebra(QQ,
    10)`` currently triggers the construction of all symmetric group
    algebras of smaller order. Is this a feature we really want to have?

    .. WARNING::

        The semantics of multiplication in symmetric group algebras
        with index set ``Permutations(n)`` is determined by the order
        in which permutations are multiplied, which currently defaults
        to "in such a way that multiplication is associative with
        permutations acting on integers from the right", but can be
        changed to the opposite order at runtime by setting the global
        variable ``Permutations.options[\'mult\']`` (see
        :meth:`sage.combinat.permutation.Permutations.options` ).
        On the other hand, the semantics of multiplication in symmetric
        group algebras with index set ``SymmetricGroup(n)`` does not
        depend on this global variable. (This has the awkward
        consequence that the coercions between these two sorts of
        symmetric group algebras do not respect multiplication when
        this global variable is set to ``\'r2l\'``.)
        In view of this, it is recommended that code not rely on the
        usual multiplication function, but rather use the methods
        :meth:`left_action_product` and :meth:`right_action_product`
        for multiplying permutations (these methods don\'t depend on the
        setting). See :issue:`14885` for more information.

    We conclude by constructing the algebra of the symmetric group as
    a monoid algebra::

        sage: QS3 = SymmetricGroupAlgebra(QQ, 3, category=Monoids())
        sage: QS3.category()
        Category of finite dimensional cellular monoid algebras
        over Rational Field
        sage: TestSuite(QS3).run(skip=[\'_test_construction\'])


    TESTS::

        sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
        sage: TestSuite(QS3).run()

        sage: QS3.group()
        Standard permutations of 3

        sage: QS3.one_basis()
        [1, 2, 3]

        sage: p1 = Permutation([1,2,3])
        sage: p2 = Permutation([2,1,3])
        sage: QS3.product_on_basis(p1,p2)
        [2, 1, 3]

        sage: W = WeylGroup(["A",3])
        sage: SGA = SymmetricGroupAlgebra(QQ, W)
        sage: SGA.group() is W
        True
        sage: TestSuite(SGA).run(skip=["_test_cellular", "_test_construction"])
        sage: W = WeylGroup(["A",2])
        sage: SGA = SymmetricGroupAlgebra(QQ, W)
        sage: SGA._test_cellular()

        sage: SG = SymmetricGroupAlgebra(ZZ, 3)
        sage: SG.group().conjugacy_classes_representatives()
        [[1, 2, 3], [2, 1, 3], [2, 3, 1]]

        sage: SGg = SymmetricGroup(3).algebra(ZZ)
        sage: SGg.group().conjugacy_classes_representatives()
        [(), (1,2), (1,2,3)]
    '''

class SymmetricGroupAlgebra_n(GroupAlgebra_class):
    n: Incomplete
    def __init__(self, R, W, category) -> None:
        '''
        TESTS::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: TestSuite(QS3).run()

            sage: QS3 in GroupAlgebras(QQ)
            True
            sage: QS3 in FiniteDimensionalAlgebrasWithBasis(QQ)
            True

        Check that :issue:`16926` works::

            sage: S = SymmetricGroup(4)
            sage: SGA = S.algebra(QQ)
            sage: TestSuite(SGA).run(skip=\'_test_cellular\')
            sage: SGA._test_cellular() # long time

        Checking that coercion works between equivalent indexing sets::

            sage: G = SymmetricGroup(4).algebra(QQ)
            sage: S = SymmetricGroupAlgebra(QQ,4)
            sage: S(G.an_element())
            [1, 2, 3, 4] + [1, 3, 4, 2] + 2*[3, 4, 1, 2] + 3*[4, 3, 2, 1]
            sage: G(S.an_element())
            () + 2*(3,4) + 3*(2,3) + (1,4,3,2)

        Checking the recovery of `n`:

            sage: SymmetricGroup(4).algebra(QQ).n
            4
            sage: SymmetricGroup(1).algebra(QQ).n
            1
            sage: SymmetricGroup(0).algebra(QQ).n
            0
            sage: Permutations(4).algebra(QQ).n
            4
            sage: Permutations(1).algebra(QQ).n
            1
            sage: Permutations(0).algebra(QQ).n
            0
            sage: SymmetricGroupAlgebra(QQ, WeylGroup(["A",3])).n
            4
            sage: SymmetricGroupAlgebra(QQ, WeylGroup(["A",1])).n
            2
            sage: SymmetricGroupAlgebra(QQ, WeylGroup(["A",0])).n # todo: not implemented
            1
        '''
    def left_action_product(self, left, right):
        """
        Return the product of two elements ``left`` and ``right`` of
        ``self``, where multiplication is defined in such a way that
        for two permutations `p` and `q`, the product `pq` is the
        permutation obtained by first applying `q` and then applying
        `p`. This definition of multiplication is tailored to make
        multiplication of permutations associative with their action on
        numbers if permutations are to act on numbers from the left.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: p1 = Permutation([2, 1, 3])
            sage: p2 = Permutation([3, 1, 2])
            sage: QS3.left_action_product(QS3(p1), QS3(p2))
            [3, 2, 1]
            sage: x = QS3([1, 2, 3]) - 2*QS3([1, 3, 2])
            sage: y = 1/2 * QS3([3, 1, 2]) + 3*QS3([1, 2, 3])
            sage: QS3.left_action_product(x, y)
            3*[1, 2, 3] - 6*[1, 3, 2] - [2, 1, 3] + 1/2*[3, 1, 2]
            sage: QS3.left_action_product(0, x)
            0

        The method coerces its input into the algebra ``self``::

            sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
            sage: QS4.left_action_product(QS3([1, 2, 3]), QS3([2, 1, 3]))
            [2, 1, 3, 4]
            sage: QS4.left_action_product(1, Permutation([4, 1, 2, 3]))
            [4, 1, 2, 3]

        TESTS::

            sage: QS4 = SymmetricGroup(4).algebra(QQ)
            sage: QS4.left_action_product(QS4((1,2)), QS4((2,3)))
            (1,2,3)
            sage: QS4.left_action_product(1, QS4((1,2)))
            (1,2)

        .. WARNING::

            Note that coercion presently works from permutations of ``n``
            into the ``n``-th symmetric group algebra, and also from all
            smaller symmetric group algebras into the ``n``-th symmetric
            group algebra, but not from permutations of integers smaller
            than ``n`` into the ``n``-th symmetric group algebra.
        """
    def right_action_product(self, left, right):
        """
        Return the product of two elements ``left`` and ``right`` of
        ``self``, where multiplication is defined in such a way that
        for two permutations `p` and `q`, the product `pq` is the
        permutation obtained by first applying `p` and then applying
        `q`. This definition of multiplication is tailored to make
        multiplication of permutations associative with their action on
        numbers if permutations are to act on numbers from the right.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: p1 = Permutation([2, 1, 3])
            sage: p2 = Permutation([3, 1, 2])
            sage: QS3.right_action_product(QS3(p1), QS3(p2))
            [1, 3, 2]
            sage: x = QS3([1, 2, 3]) - 2*QS3([1, 3, 2])
            sage: y = 1/2 * QS3([3, 1, 2]) + 3*QS3([1, 2, 3])
            sage: QS3.right_action_product(x, y)
            3*[1, 2, 3] - 6*[1, 3, 2] + 1/2*[3, 1, 2] - [3, 2, 1]
            sage: QS3.right_action_product(0, x)
            0

        The method coerces its input into the algebra ``self``::

            sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
            sage: QS4.right_action_product(QS3([1, 2, 3]), QS3([2, 1, 3]))
            [2, 1, 3, 4]
            sage: QS4.right_action_product(1, Permutation([4, 1, 2, 3]))
            [4, 1, 2, 3]

        TESTS::

            sage: QS4 = SymmetricGroup(4).algebra(QQ)
            sage: QS4.right_action_product(QS4((1,2)), QS4((2,3)))
            (1,3,2)
            sage: QS4.right_action_product(1, QS4((1,2)))
            (1,2)

        .. WARNING::

            Note that coercion presently works from permutations of ``n``
            into the ``n``-th symmetric group algebra, and also from all
            smaller symmetric group algebras into the ``n``-th symmetric
            group algebra, but not from permutations of integers smaller
            than ``n`` into the ``n``-th symmetric group algebra.
        """
    def canonical_embedding(self, other):
        """
        Return the canonical coercion of ``self`` into a symmetric
        group algebra ``other``.

        INPUT:

        - ``other`` -- a symmetric group algebra with order `p`
          satisfying `p \\geq n`, where `n` is the order of ``self``,
          over a ground ring into which the ground ring of ``self``
          coerces.

        EXAMPLES::

            sage: QS2 = SymmetricGroupAlgebra(QQ, 2)
            sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
            sage: phi = QS2.canonical_embedding(QS4); phi
            Generic morphism:
              From: Symmetric group algebra of order 2 over Rational Field
              To:   Symmetric group algebra of order 4 over Rational Field

            sage: x = QS2([2,1]) + 2 * QS2([1,2])
            sage: phi(x)
            2*[1, 2, 3, 4] + [2, 1, 3, 4]

            sage: loads(dumps(phi))
            Generic morphism:
              From: Symmetric group algebra of order 2 over Rational Field
              To:   Symmetric group algebra of order 4 over Rational Field

            sage: ZS2 = SymmetricGroupAlgebra(ZZ, 2)
            sage: phi = ZS2.canonical_embedding(QS4); phi
            Generic morphism:
              From: Symmetric group algebra of order 2 over Integer Ring
              To:   Symmetric group algebra of order 4 over Rational Field

            sage: phi = ZS2.canonical_embedding(QS2); phi
            Generic morphism:
              From: Symmetric group algebra of order 2 over Integer Ring
              To:   Symmetric group algebra of order 2 over Rational Field

            sage: QS4.canonical_embedding(QS2)
            Traceback (most recent call last):
            ...
            ValueError: There is no canonical embedding from Symmetric group
             algebra of order 2 over Rational Field to Symmetric group
             algebra of order 4 over Rational Field

            sage: QS4g = SymmetricGroup(4).algebra(QQ)
            sage: QS4.canonical_embedding(QS4g)(QS4([1,3,2,4]))
            (2,3)
            sage: QS4g.canonical_embedding(QS4)(QS4g((2,3)))
            [1, 3, 2, 4]
            sage: ZS2.canonical_embedding(QS4g)(ZS2([2,1]))
            (1,2)
            sage: ZS2g = SymmetricGroup(2).algebra(ZZ)
            sage: ZS2g.canonical_embedding(QS4)(ZS2g((1,2)))
            [2, 1, 3, 4]
        """
    def monomial_from_smaller_permutation(self, permutation):
        """
        Convert ``permutation`` into a permutation, possibly extending it
        to the appropriate size, and return the corresponding basis
        element of ``self``.

        EXAMPLES::

            sage: QS5 = SymmetricGroupAlgebra(QQ, 5)
            sage: QS5.monomial_from_smaller_permutation([])
            [1, 2, 3, 4, 5]
            sage: QS5.monomial_from_smaller_permutation(Permutation([3,1,2]))
            [3, 1, 2, 4, 5]
            sage: QS5.monomial_from_smaller_permutation([5,3,4,1,2])
            [5, 3, 4, 1, 2]
            sage: QS5.monomial_from_smaller_permutation(SymmetricGroup(2)((1,2)))
            [2, 1, 3, 4, 5]

            sage: QS5g = SymmetricGroup(5).algebra(QQ)
            sage: QS5g.monomial_from_smaller_permutation([2,1])
            (1,2)

        TESTS::

            sage: QS5.monomial_from_smaller_permutation([5,3,4,1,2]).parent()
            Symmetric group algebra of order 5 over Rational Field
        """
    def antipode(self, x):
        """
        Return the image of the element ``x`` of ``self`` under the
        antipode of the Hopf algebra ``self`` (where the
        comultiplication is the usual one on a group algebra).

        Explicitly, this is obtained by replacing each permutation
        `\\sigma` by `\\sigma^{-1}` in ``x`` while keeping all
        coefficients as they are.

        EXAMPLES::

            sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
            sage: QS4.antipode(2 * QS4([1, 3, 4, 2]) - 1/2 * QS4([1, 4, 2, 3]))
            -1/2*[1, 3, 4, 2] + 2*[1, 4, 2, 3]
            sage: all( QS4.antipode(QS4(p)) == QS4(p.inverse())
            ....:      for p in Permutations(4) )
            True

            sage: ZS3 = SymmetricGroupAlgebra(ZZ, 3)
            sage: ZS3.antipode(ZS3.zero())
            0
            sage: ZS3.antipode(-ZS3(Permutation([2, 3, 1])))
            -[3, 1, 2]
        """
    @cached_method
    def cell_poset(self):
        """
        Return the cell poset of ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 4)
            sage: S.cell_poset()
            Finite poset containing 5 elements
        """
    def cell_module_indices(self, la):
        """
        Return the indices of the cell module of ``self``
        indexed by ``la`` .

        This is the finite set `M(\\lambda)`.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 4)
            sage: S.cell_module_indices([3,1])
            Standard tableaux of shape [3, 1]
        """
    def cell_module(self, la, **kwds):
        """
        Return the cell module indexed by ``la``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: M = S.cell_module(Partition([2,1])); M
            Cell module indexed by [2, 1] of Cellular basis of
             Symmetric group algebra of order 3 over Rational Field

        We check that the input ``la`` is standardized::

            sage: N = S.cell_module([2,1])
            sage: M is N
            True
        """
    def retract_plain(self, f, m):
        """
        Return the plain retract of the element `f \\in R S_n`
        to `R S_m`, where `m \\leq n` (and where `R S_n` is ``self``).

        If `m` is a nonnegative integer less or equal to `n`, then the
        plain retract from `S_n` to `S_m` is defined as an `R`-linear
        map `S_n \\to S_m` which sends every permutation `p \\in S_n`
        to

        .. MATH::

            \\begin{cases} \\mbox{pret}(p) &\\mbox{if } \\mbox{pret}(p)\\mbox{ is defined;} \\\\\n            0 & \\mbox{otherwise} \\end{cases}.

        Here `\\mbox{pret}(p)` denotes the plain retract of the
        permutation `p` to `S_m`, which is defined in
        :meth:`~sage.combinat.permutation.Permutation.retract_plain`.

        EXAMPLES::

            sage: SGA3 = SymmetricGroupAlgebra(QQ, 3)
            sage: SGA3.retract_plain(2*SGA3([1,2,3]) - 4*SGA3([2,1,3]) + 7*SGA3([1,3,2]), 2)
            2*[1, 2] - 4*[2, 1]
            sage: SGA3.retract_plain(2*SGA3([1,3,2]) - 5*SGA3([2,3,1]), 2)
            0

            sage: SGA5 = SymmetricGroupAlgebra(QQ, 5)
            sage: SGA5.retract_plain(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 4)
            11*[3, 2, 1, 4]
            sage: SGA5.retract_plain(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 3)
            11*[3, 2, 1]
            sage: SGA5.retract_plain(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 2)
            0
            sage: SGA5.retract_plain(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 1)
            0

            sage: SGA5.retract_plain(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 3)
            8*[1, 2, 3] - 6*[1, 3, 2]
            sage: SGA5.retract_plain(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 1)
            8*[1]
            sage: SGA5.retract_plain(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 0)
            8*[]

        TESTS:

        Check this works with other indexing sets::

            sage: G = SymmetricGroup(4).algebra(QQ)
            sage: G.retract_plain(G.an_element(), 3)
            ()

        .. SEEALSO::

            :meth:`retract_direct_product`, :meth:`retract_okounkov_vershik`
        """
    def retract_direct_product(self, f, m):
        """
        Return the direct-product retract of the element `f \\in R S_n`
        to `R S_m`, where `m \\leq n` (and where `R S_n` is ``self``).

        If `m` is a nonnegative integer less or equal to `n`, then the
        direct-product retract from `S_n` to `S_m` is defined as an
        `R`-linear map `S_n \\to S_m` which sends every permutation
        `p \\in S_n` to

        .. MATH::

            \\begin{cases} \\mbox{dret}(p) &\\mbox{if } \\mbox{dret}(p)\\mbox{ is defined;} \\\\\n            0 & \\mbox{otherwise} \\end{cases}.

        Here `\\mbox{dret}(p)` denotes the direct-product retract of the
        permutation `p` to `S_m`, which is defined in
        :meth:`~sage.combinat.permutation.Permutation.retract_direct_product`.

        EXAMPLES::

            sage: SGA3 = SymmetricGroupAlgebra(QQ, 3)
            sage: SGA3.retract_direct_product(2*SGA3([1,2,3]) - 4*SGA3([2,1,3]) + 7*SGA3([1,3,2]), 2)
            2*[1, 2] - 4*[2, 1]
            sage: SGA3.retract_direct_product(2*SGA3([1,3,2]) - 5*SGA3([2,3,1]), 2)
            0

            sage: SGA5 = SymmetricGroupAlgebra(QQ, 5)
            sage: SGA5.retract_direct_product(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 4)
            11*[3, 2, 1, 4]
            sage: SGA5.retract_direct_product(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 3)
            -6*[1, 3, 2] + 11*[3, 2, 1]
            sage: SGA5.retract_direct_product(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 2)
            0
            sage: SGA5.retract_direct_product(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 1)
            2*[1]

            sage: SGA5.retract_direct_product(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 3)
            8*[1, 2, 3] - 6*[1, 3, 2]
            sage: SGA5.retract_direct_product(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 1)
            2*[1]
            sage: SGA5.retract_direct_product(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 0)
            2*[]

        TESTS:

        Check this works with other indexing sets::

            sage: G = SymmetricGroup(4).algebra(QQ)
            sage: G.retract_direct_product(G.an_element(), 3)
            ()

        .. SEEALSO::

            :meth:`retract_plain`, :meth:`retract_okounkov_vershik`
        """
    def retract_okounkov_vershik(self, f, m):
        """
        Return the Okounkov-Vershik retract of the element `f \\in R S_n`
        to `R S_m`, where `m \\leq n` (and where `R S_n` is ``self``).

        If `m` is a nonnegative integer less or equal to `n`, then the
        Okounkov-Vershik retract from `S_n` to `S_m` is defined as an
        `R`-linear map `S_n \\to S_m` which sends every permutation
        `p \\in S_n` to the Okounkov-Vershik retract of the permutation
        `p` to `S_m`, which is defined in
        :meth:`~sage.combinat.permutation.Permutation.retract_okounkov_vershik`.

        EXAMPLES::

            sage: SGA3 = SymmetricGroupAlgebra(QQ, 3)
            sage: SGA3.retract_okounkov_vershik(2*SGA3([1,2,3]) - 4*SGA3([2,1,3]) + 7*SGA3([1,3,2]), 2)
            9*[1, 2] - 4*[2, 1]
            sage: SGA3.retract_okounkov_vershik(2*SGA3([1,3,2]) - 5*SGA3([2,3,1]), 2)
            2*[1, 2] - 5*[2, 1]

            sage: SGA5 = SymmetricGroupAlgebra(QQ, 5)
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 4)
            -6*[1, 3, 2, 4] + 8*[1, 4, 2, 3] + 11*[3, 2, 1, 4]
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 3)
            2*[1, 3, 2] + 11*[3, 2, 1]
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 2)
            13*[1, 2]
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,4,2,5,3]) - 6*SGA5([1,3,2,5,4]) + 11*SGA5([3,2,1,4,5]), 1)
            13*[1]

            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 3)
            8*[1, 2, 3] - 6*[1, 3, 2]
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 1)
            2*[1]
            sage: SGA5.retract_okounkov_vershik(8*SGA5([1,2,3,4,5]) - 6*SGA5([1,3,2,4,5]), 0)
            2*[]

        TESTS:

        Check this works with other indexing sets::

            sage: G = SymmetricGroup(4).algebra(QQ)
            sage: G.retract_okounkov_vershik(G.an_element(), 3)
            () + 4*(2,3) + 2*(1,3)

        .. SEEALSO::

            :meth:`retract_plain`, :meth:`retract_direct_product`
        """
    def central_orthogonal_idempotents(self):
        '''
        Return a maximal list of central orthogonal idempotents for ``self``.

        This method does not require that ``self`` be semisimple, relying
        on Nakayama\'s Conjecture whenever ``self.base_ring()`` has
        positive characteristic.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ,3)
            sage: a = QS3.central_orthogonal_idempotents()
            sage: a[0]  # [3]
            1/6*[1, 2, 3] + 1/6*[1, 3, 2] + 1/6*[2, 1, 3] + 1/6*[2, 3, 1]
             + 1/6*[3, 1, 2] + 1/6*[3, 2, 1]
            sage: a[1]  # [2, 1]
            2/3*[1, 2, 3] - 1/3*[2, 3, 1] - 1/3*[3, 1, 2]

        TESTS:

        Check this works with other indexing sets::

            sage: G = SymmetricGroup(3).algebra(QQ)
            sage: a = G.central_orthogonal_idempotents()
            sage: a[0]
            1/6*() + 1/6*(2,3) + 1/6*(1,2) + 1/6*(1,2,3) + 1/6*(1,3,2) + 1/6*(1,3)
            sage: a[1]
            2/3*() - 1/3*(1,2,3) - 1/3*(1,3,2)

            sage: G = SymmetricGroup(3).algebra(GF(2))
            sage: a = G.central_orthogonal_idempotents()
            sage: a[0]
            (1,2,3) + (1,3,2)
            sage: a[1]
            () + (1,2,3) + (1,3,2)

        Check this works in positive characteristic::

            sage: def test_n_with_primes(n, primes):
            ....:     Sn = {p:SymmetricGroupAlgebra(GF(p), n) for p in primes}
            ....:     for p in primes:
            ....:         idems = Sn[p].central_orthogonal_idempotents()
            ....:         tst = [sum(idems)==Sn[p].one()]
            ....:         for i in range(len(idems)-1):
            ....:             e = idems[i]
            ....:             for j in range(i, len(idems)):
            ....:                 f = idems[j]
            ....:                 if i == j:
            ....:                     tst.append(e*e == e)
            ....:                 else:
            ....:                     tst.append(e*f == 0)
            ....:         print("{0} blocks for p={1} ... {2}".format( len(idems), p, all(tst) ))
            sage: test_n_with_primes(5, [2,3,5,7])  # long time
            2 blocks for p=2 ... True
            3 blocks for p=3 ... True
            3 blocks for p=5 ... True
            7 blocks for p=7 ... True

        .. SEEALSO::

            - :meth:`central_orthogonal_idempotent`
        '''
    def central_orthogonal_idempotent(self, la, block: bool = True):
        """
        Return the central idempotent for the symmetric group of order `n`
        corresponding to the indecomposable block to which the partition
        ``la`` is associated.

        If ``self.base_ring()`` contains `\\QQ`, this corresponds to the
        classical central idempotent corresponding to the irreducible
        representation indexed by ``la``.

        Alternatively, if ``self.base_ring()`` has characteristic `p > 0`,
        then Theorem 2.8 in [Mur1983]_ provides that ``la`` is associated
        to an idempotent `f_\\mu`, where `\\mu` is the `p`-core of ``la``.
        This `f_\\mu` is a sum of classical idempotents,

        .. MATH::

            f_\\mu = \\sum_{c(\\lambda)=\\mu} e_\\lambda,

        where the sum ranges over the partitions `\\lambda` of `n` with
        `p`-core equal to `\\mu`.

        INPUT:

        - ``la`` -- a partition of ``self.n`` or a
          ``self.base_ring().characteristic()``-core of such
          a partition

        - ``block`` -- boolean (default: ``True``); when ``False``,
          this returns the classical idempotent associated to ``la``
          (defined over `\\QQ`)

        OUTPUT:

        If ``block=False`` and the corresponding coefficients are
        not defined over ``self.base_ring()``, then return ``None``.
        Otherwise return an element of ``self``.

        EXAMPLES:

        Asking for block idempotents in any characteristic, by
        passing a partition of ``self.n``::

            sage: S0 = SymmetricGroup(4).algebra(QQ)
            sage: S2 = SymmetricGroup(4).algebra(GF(2))
            sage: S3 = SymmetricGroup(4).algebra(GF(3))
            sage: S0.central_orthogonal_idempotent([2,1,1])
            3/8*() - 1/8*(3,4) - 1/8*(2,3) - 1/8*(2,4) - 1/8*(1,2)
             - 1/8*(1,2)(3,4) + 1/8*(1,2,3,4) + 1/8*(1,2,4,3)
             + 1/8*(1,3,4,2) - 1/8*(1,3) - 1/8*(1,3)(2,4)
             + 1/8*(1,3,2,4) + 1/8*(1,4,3,2) - 1/8*(1,4)
             + 1/8*(1,4,2,3) - 1/8*(1,4)(2,3)
            sage: S2.central_orthogonal_idempotent([2,1,1])
            ()
            sage: idem = S3.central_orthogonal_idempotent([4]); idem
             () + (1,2)(3,4) + (1,3)(2,4) + (1,4)(2,3)
            sage: idem == S3.central_orthogonal_idempotent([1,1,1,1])
            True
            sage: S3.central_orthogonal_idempotent([2,2])
            () + (1,2)(3,4) + (1,3)(2,4) + (1,4)(2,3)

        Asking for block idempotents in any characteristic, by
        passing `p`-cores::

            sage: S0.central_orthogonal_idempotent([1,1])
            Traceback (most recent call last):
            ...
            ValueError: [1, 1] is not a partition of integer 4
            sage: S2.central_orthogonal_idempotent([])
            ()
            sage: S2.central_orthogonal_idempotent([1])
            Traceback (most recent call last):
            ...
            ValueError: the 2-core of [1] is not a 2-core of a partition of 4
            sage: S3.central_orthogonal_idempotent([1])
            () + (1,2)(3,4) + (1,3)(2,4) + (1,4)(2,3)
            sage: S3.central_orthogonal_idempotent([7])
            () + (1,2)(3,4) + (1,3)(2,4) + (1,4)(2,3)

        Asking for classical idempotents::

            sage: S3.central_orthogonal_idempotent([2,2], block=False) is None
            True
            sage: S3.central_orthogonal_idempotent([2,1,1], block=False)
            (3,4) + (2,3) + (2,4) + (1,2) + (1,2)(3,4) + 2*(1,2,3,4)
             + 2*(1,2,4,3) + 2*(1,3,4,2) + (1,3) + (1,3)(2,4)
             + 2*(1,3,2,4) + 2*(1,4,3,2) + (1,4) + 2*(1,4,2,3)
             + (1,4)(2,3)

        .. SEEALSO::

            - :meth:`sage.combinat.partition.Partition.core`
        """
    def ladder_idempotent(self, la):
        """
        Return the ladder idempotent of ``self``.

        Let `F` be a field of characteristic `p`. The *ladder idempotent*
        of shape `\\lambda` is the idempotent of `F[S_n]` defined as follows.
        Let `T` be the :meth:`ladder tableau
        <sage.combinat.partition.Partition.ladder_tableau>` of shape `\\lambda`.
        Let `[T]` be the set of standard tableaux whose residue sequence
        is the same as for `T`. Let `\\alpha` be the sizes of the ladders
        of `\\lambda`. Then the ladder idempotent is constructed as

        .. MATH::

            \\widetilde{e}_{\\lambda} := \\frac{1}{\\alpha!}
              \\left( \\sum_{\\sigma \\in S_{\\alpha}} \\sigma \\right)
              \\left( \\overline{\\sum_{U \\in [T]} E_U} \\right),

        where `E_{UU}` is the :meth:`seminormal_basis` element over `\\QQ`
        and we project the sum to `F`, `S_{\\alpha}` is the Young subgroup
        corresponding to `\\alpha`, and `\\alpha! = \\alpha_1! \\cdots \\alpha_k!`.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
            sage: for la in Partitions(SGA.n):
            ....:     idem = SGA.ladder_idempotent(la)
            ....:     print(la)
            ....:     print(idem)
            ....:     assert idem^2 == idem
            [4]
            2*[1, 2, 3, 4] + 2*[1, 2, 4, 3] + 2*[2, 1, 3, 4] + 2*[2, 1, 4, 3]
             + 2*[3, 4, 1, 2] + 2*[3, 4, 2, 1] + 2*[4, 3, 1, 2] + 2*[4, 3, 2, 1]
            [3, 1]
            2*[1, 2, 3, 4] + 2*[1, 2, 4, 3] + 2*[2, 1, 3, 4] + 2*[2, 1, 4, 3]
             + [3, 4, 1, 2] + [3, 4, 2, 1] + [4, 3, 1, 2] + [4, 3, 2, 1]
            [2, 2]
            2*[1, 2, 3, 4] + 2*[1, 2, 4, 3] + 2*[2, 1, 3, 4] + 2*[2, 1, 4, 3]
             + 2*[3, 4, 1, 2] + 2*[3, 4, 2, 1] + 2*[4, 3, 1, 2] + 2*[4, 3, 2, 1]
            [2, 1, 1]
            2*[1, 2, 3, 4] + [1, 2, 4, 3] + 2*[1, 3, 2, 4] + [1, 3, 4, 2]
             + [1, 4, 2, 3] + 2*[1, 4, 3, 2] + 2*[2, 1, 3, 4] + [2, 1, 4, 3]
             + 2*[2, 3, 1, 4] + [2, 3, 4, 1] + [2, 4, 1, 3] + 2*[2, 4, 3, 1]
             + 2*[3, 1, 2, 4] + [3, 1, 4, 2] + 2*[3, 2, 1, 4] + [3, 2, 4, 1]
             + [4, 1, 2, 3] + 2*[4, 1, 3, 2] + [4, 2, 1, 3] + 2*[4, 2, 3, 1]
            [1, 1, 1, 1]
            2*[1, 2, 3, 4] + [1, 2, 4, 3] + [2, 1, 3, 4] + 2*[2, 1, 4, 3]
             + 2*[3, 4, 1, 2] + [3, 4, 2, 1] + [4, 3, 1, 2] + 2*[4, 3, 2, 1]

        When `p = 0`, these idempotents will generate all of the simple
        modules (which are the :meth:`Specht modules <specht_module>`
        and also projective modules)::

            sage: # long time
            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: for la in Partitions(SGA.n):
            ....:     idem = SGA.ladder_idempotent(la)
            ....:     assert idem^2 == idem
            ....:     print(la, SGA.principal_ideal(idem).dimension())
            [5] 1
            [4, 1] 4
            [3, 2] 5
            [3, 1, 1] 6
            [2, 2, 1] 5
            [2, 1, 1, 1] 4
            [1, 1, 1, 1, 1] 1
            sage: [StandardTableaux(la).cardinality() for la in Partitions(SGA.n)]
            [1, 4, 5, 6, 5, 4, 1]

        REFERENCES:

        - [Ryom2015]_
        """
    @cached_method
    def algebra_generators(self):
        """
        Return generators of this group algebra (as algebra) as a
        list of permutations.

        The generators used for the group algebra of `S_n` are the
        transposition `(2, 1)` and the `n`-cycle `(1, 2, \\ldots, n)`,
        unless `n \\leq 1` (in which case no generators are needed).

        EXAMPLES::

            sage: SymmetricGroupAlgebra(ZZ,5).algebra_generators()
            Family ([2, 1, 3, 4, 5], [2, 3, 4, 5, 1])

            sage: SymmetricGroupAlgebra(QQ,0).algebra_generators()
            Family ()

            sage: SymmetricGroupAlgebra(QQ,1).algebra_generators()
            Family ()

        TESTS:

        Check that :issue:`15309` is fixed::

            sage: S3 = SymmetricGroupAlgebra(QQ, 3)
            sage: S3.algebra_generators()
            Family ([2, 1, 3], [2, 3, 1])
            sage: C = CombinatorialFreeModule(ZZ, ZZ)
            sage: M = C.module_morphism(lambda x: S3.zero(), codomain=S3)
            sage: M.register_as_coercion()
        """
    def rsw_shuffling_element(self, k):
        """
        Return the `k`-th Reiner-Saliola-Welker shuffling element in
        the group algebra ``self``.

        The `k`-th Reiner-Saliola-Welker shuffling element in the
        symmetric group algebra `R S_n` over a ring `R` is defined as the
        sum `\\sum_{\\sigma \\in S_n} \\mathrm{noninv}_k(\\sigma) \\cdot \\sigma`,
        where for every permutation `\\sigma`, the number
        `\\mathrm{noninv}_k(\\sigma)` is the number of all
        `k`-noninversions of `\\sigma` (that is, the number of all
        `k`-element subsets of `\\{ 1, 2, \\ldots, n \\}` on which
        `\\sigma` restricts to a strictly increasing map). See
        :meth:`sage.combinat.permutation.number_of_noninversions` for
        the `\\mathrm{noninv}` map.

        This element is more or less the operator `\\nu_{k, 1^{n-k}}`
        introduced in [RSW2011]_; more precisely, `\\nu_{k, 1^{n-k}}`
        is the left multiplication by this element.

        It is a nontrivial theorem (Theorem 1.1 in [RSW2011]_) that
        the operators `\\nu_{k, 1^{n-k}}` (for fixed `n` and varying
        `k`) pairwise commute. It is a conjecture (Conjecture 1.2 in
        [RSW2011]_) that all their eigenvalues are integers (which, in
        light of their commutativity and easily established symmetry,
        yields that they can be simultaneously diagonalized over `\\QQ`
        with only integer eigenvalues).

        EXAMPLES:

        The Reiner-Saliola-Welker shuffling elements on `\\QQ S_3`::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: QS3.rsw_shuffling_element(0)
            [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
            sage: QS3.rsw_shuffling_element(1)
            3*[1, 2, 3] + 3*[1, 3, 2] + 3*[2, 1, 3] + 3*[2, 3, 1] + 3*[3, 1, 2] + 3*[3, 2, 1]
            sage: QS3.rsw_shuffling_element(2)
            3*[1, 2, 3] + 2*[1, 3, 2] + 2*[2, 1, 3] + [2, 3, 1] + [3, 1, 2]
            sage: QS3.rsw_shuffling_element(3)
            [1, 2, 3]
            sage: QS3.rsw_shuffling_element(4)
            0

        Checking the commutativity of Reiner-Saliola-Welker shuffling
        elements (we leave out the ones for which it is trivial)::

            sage: def test_rsw_comm(n):
            ....:     QSn = SymmetricGroupAlgebra(QQ, n)
            ....:     rsws = [QSn.rsw_shuffling_element(k) for k in range(2, n)]
            ....:     return all(ri * rsws[j] == rsws[j] * ri
            ....:                for i, ri in enumerate(rsws) for j in range(i))
            sage: test_rsw_comm(3)
            True
            sage: test_rsw_comm(4)   # long time
            True
            sage: test_rsw_comm(5)   # not tested
            True

        .. NOTE::

            For large ``k`` (relative to ``n``), it might be faster to call
            ``QSn.left_action_product(QSn.semi_rsw_element(k), QSn.antipode(binary_unshuffle_sum(k)))``
            than ``QSn.rsw_shuffling_element(n)``.

        .. SEEALSO::

            :meth:`semi_rsw_element`, :meth:`binary_unshuffle_sum`
        """
    def semi_rsw_element(self, k):
        """
        Return the `k`-th semi-RSW element in the group algebra ``self``.

        The `k`-th semi-RSW element in the symmetric group algebra
        `R S_n` over a ring `R` is defined as the sum of all permutations
        `\\sigma \\in S_n` satisfying
        `\\sigma(1) < \\sigma(2) < \\cdots < \\sigma(k)`.

        This element has the property that, if it is denoted by `s_k`,
        then `s_k S(s_k)` is `(n-k)!` times the `k`-th
        Reiner-Saliola-Welker shuffling element of `R S_n` (see
        :meth:`rsw_shuffling_element`). Here, `S` denotes the antipode
        of the group algebra `R S_n`.

        The `k`-th semi-RSW element is the image of the complete
        non-commutative symmetric function `S^{(k, 1^{n-k})}` in the
        ring of non-commutative symmetric functions under the canonical
        projection on the symmetric group algebra (through the descent
        algebra).

        EXAMPLES:

        The semi-RSW elements on `\\QQ S_3`::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: QS3.semi_rsw_element(0)
            [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
            sage: QS3.semi_rsw_element(1)
            [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
            sage: QS3.semi_rsw_element(2)
            [1, 2, 3] + [1, 3, 2] + [2, 3, 1]
            sage: QS3.semi_rsw_element(3)
            [1, 2, 3]
            sage: QS3.semi_rsw_element(4)
            0

        Let us check the relation with the `k`-th Reiner-Saliola-Welker
        shuffling element stated in the docstring::

            sage: def test_rsw(n):
            ....:     ZSn = SymmetricGroupAlgebra(ZZ, n)
            ....:     for k in range(1, n):
            ....:         a = ZSn.semi_rsw_element(k)
            ....:         b = ZSn.left_action_product(a, ZSn.antipode(a))
            ....:         if factorial(n-k) * ZSn.rsw_shuffling_element(k) != b:
            ....:             return False
            ....:     return True
            sage: test_rsw(3)
            True
            sage: test_rsw(4)
            True
            sage: test_rsw(5)  # long time
            True

        Let us also check the statement about the complete
        non-commutative symmetric function::

            sage: def test_rsw_ncsf(n):
            ....:     ZSn = SymmetricGroupAlgebra(ZZ, n)
            ....:     NSym = NonCommutativeSymmetricFunctions(ZZ)
            ....:     S = NSym.S()
            ....:     for k in range(1, n):
            ....:         a = S(Composition([k] + [1]*(n-k))).to_symmetric_group_algebra()
            ....:         if a != ZSn.semi_rsw_element(k):
            ....:             return False
            ....:     return True
            sage: test_rsw_ncsf(3)
            True
            sage: test_rsw_ncsf(4)
            True
            sage: test_rsw_ncsf(5)  # long time
            True
        """
    def binary_unshuffle_sum(self, k):
        """
        Return the `k`-th binary unshuffle sum in the group algebra
        ``self``.

        The `k`-th binary unshuffle sum in the symmetric group algebra
        `R S_n` over a ring `R` is defined as the sum of all permutations
        `\\sigma \\in S_n` satisfying
        `\\sigma(1) < \\sigma(2) < \\cdots < \\sigma(k)` and
        `\\sigma(k+1) < \\sigma(k+2) < \\cdots < \\sigma(n)`.

        This element has the property that, if it is denoted by `t_k`,
        and if the `k`-th semi-RSW element (see :meth:`semi_rsw_element`)
        is denoted by `s_k`, then `s_k S(t_k)` and `t_k S(s_k)` both
        equal the `k`-th Reiner-Saliola-Welker shuffling element of
        `R S_n` (see :meth:`rsw_shuffling_element`).

        The `k`-th binary unshuffle sum is the image of the complete
        non-commutative symmetric function `S^{(k, n-k)}` in the
        ring of non-commutative symmetric functions under the canonical
        projection on the symmetric group algebra (through the descent
        algebra).

        EXAMPLES:

        The binary unshuffle sums on `\\QQ S_3`::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: QS3.binary_unshuffle_sum(0)
            [1, 2, 3]
            sage: QS3.binary_unshuffle_sum(1)
            [1, 2, 3] + [2, 1, 3] + [3, 1, 2]
            sage: QS3.binary_unshuffle_sum(2)
            [1, 2, 3] + [1, 3, 2] + [2, 3, 1]
            sage: QS3.binary_unshuffle_sum(3)
            [1, 2, 3]
            sage: QS3.binary_unshuffle_sum(4)
            0

        Let us check the relation with the `k`-th Reiner-Saliola-Welker
        shuffling element stated in the docstring::

            sage: def test_rsw(n):
            ....:     ZSn = SymmetricGroupAlgebra(ZZ, n)
            ....:     for k in range(1, n):
            ....:         a = ZSn.semi_rsw_element(k)
            ....:         b = ZSn.binary_unshuffle_sum(k)
            ....:         c = ZSn.left_action_product(a, ZSn.antipode(b))
            ....:         d = ZSn.left_action_product(b, ZSn.antipode(a))
            ....:         e = ZSn.rsw_shuffling_element(k)
            ....:         if c != e or d != e:
            ....:             return False
            ....:     return True
            sage: test_rsw(3)
            True
            sage: test_rsw(4)  # long time
            True
            sage: test_rsw(5)  # long time
            True

        Let us also check the statement about the complete
        non-commutative symmetric function::

            sage: def test_rsw_ncsf(n):
            ....:     ZSn = SymmetricGroupAlgebra(ZZ, n)
            ....:     NSym = NonCommutativeSymmetricFunctions(ZZ)
            ....:     S = NSym.S()
            ....:     for k in range(1, n):
            ....:         a = S(Composition([k, n-k])).to_symmetric_group_algebra()
            ....:         if a != ZSn.binary_unshuffle_sum(k):
            ....:             return False
            ....:     return True
            sage: test_rsw_ncsf(3)
            True
            sage: test_rsw_ncsf(4)
            True
            sage: test_rsw_ncsf(5)  # long time
            True
        """
    def specht_module(self, D):
        """
        Return the Specht module of ``self`` indexed by the diagram ``D``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SM = SGA.specht_module(Partition([3,1,1]))
            sage: SM
            Specht module of [3, 1, 1] over Rational Field
            sage: SM.frobenius_image()
            s[3, 1, 1]

            sage: SM = SGA.specht_module([(1,1),(1,3),(2,2),(3,1),(3,2)])
            sage: SM
            Specht module of [(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)] over Rational Field
            sage: SM.frobenius_image()
            s[2, 2, 1] + s[3, 1, 1] + s[3, 2]
        """
    def tabloid_module(self, D):
        """
        Return the module of tabloids with the natural action of ``self``.

        .. SEEALSO::

            :class:`~sage.combinat.specht_module.TabloidModule`

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: TM = SGA.tabloid_module(Partition([3,1,1]))
            sage: TM
            Tabloid module of [3, 1, 1] over Rational Field
            sage: s = SymmetricFunctions(QQ).s()
            sage: s(TM.frobenius_image())
            s[3, 1, 1] + s[3, 2] + 2*s[4, 1] + s[5]
        """
    def specht_module_dimension(self, D):
        """
        Return the dimension of the Specht module of ``self`` indexed by ``D``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: SGA.specht_module_dimension(Partition([3,1,1]))
            6
            sage: SGA.specht_module_dimension([(1,1),(1,3),(2,2),(3,1),(3,2)])
            16
        """
    def simple_module_parameterization(self):
        """
        Return a parameterization of the simple modules of ``self``.

        The symmetric group algebra of `S_n` over a field of characteristic `p`
        has its simple modules indexed by all `p`-regular partitions of `n`.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 6)
            sage: SGA.simple_module_parameterization()
            Partitions of the integer 6

            sage: SGA = SymmetricGroupAlgebra(GF(2), 6)
            sage: SGA.simple_module_parameterization()
            2-Regular Partitions of the integer 6
        """
    def simple_module(self, la):
        """
        Return the simple module of ``self`` indexed by the partition ``la``.

        Over a field of characteristic `0`, this simply returns the Specht
        module.

        .. SEEALSO::

            :class:`sage.combinat.specht_module.SimpleModule`

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
            sage: D = SGA.simple_module(Partition([3,1,1]))
            sage: D
            Simple module of [3, 1, 1] over Finite Field of size 3
            sage: D.brauer_character()
            (6, 0, -2, 0, 1)
        """
    def simple_module_dimension(self, la):
        """
        Return the dimension of the simple module of ``self`` indexed by the
        partition ``la``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(5), 6)
            sage: SGA.simple_module_dimension(Partition([4,1,1]))
            10

        TESTS::

            sage: SGA = SymmetricGroupAlgebra(GF(5), 6)
            sage: SGA.simple_module_dimension(Partition([3,1,1]))
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 1] is not a partition of 6
        """
    def garsia_procesi_module(self, la):
        """
        Return the :class:`Garsia-Procesi module
        <sage.combinat.symmetric_group_representations.GarsiaProcesiModule>`
        of ``self`` indexed by ``la``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 6)
            sage: SGA.garsia_procesi_module(Partition([2,2,1,1]))
            Garsia-Procesi module of shape [2, 2, 1, 1] over Finite Field of size 2
        """
    def jucys_murphy(self, k):
        """
        Return the Jucys-Murphy element `J_k` (also known as a
        Young-Jucys-Murphy element) for the symmetric group
        algebra ``self``.

        The Jucys-Murphy element `J_k` in the symmetric group algebra
        `R S_n` is defined for every `k \\in \\{ 1, 2, \\ldots, n \\}` by

        .. MATH::

            J_k = (1, k) + (2, k) + \\cdots + (k-1, k) \\in R S_n,

        where the addends are transpositions in `S_n` (regarded as
        elements of `R S_n`). We note that there is not a dependence on `n`,
        so it is often suppressed in the notation.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: QS3.jucys_murphy(1)
            0
            sage: QS3.jucys_murphy(2)
            [2, 1, 3]
            sage: QS3.jucys_murphy(3)
            [1, 3, 2] + [3, 2, 1]

            sage: QS4 = SymmetricGroupAlgebra(QQ, 4)
            sage: j3 = QS4.jucys_murphy(3); j3
            [1, 3, 2, 4] + [3, 2, 1, 4]
            sage: j4 = QS4.jucys_murphy(4); j4
            [1, 2, 4, 3] + [1, 4, 3, 2] + [4, 2, 3, 1]
            sage: j3*j4 == j4*j3
            True

            sage: QS5 = SymmetricGroupAlgebra(QQ, 5)
            sage: QS5.jucys_murphy(4)
            [1, 2, 4, 3, 5] + [1, 4, 3, 2, 5] + [4, 2, 3, 1, 5]

        TESTS::

            sage: QS3.jucys_murphy(4)
            Traceback (most recent call last):
            ...
            ValueError: k (= 4) must be between 1 and n (= 3) (inclusive)
        """
    def seminormal_basis(self, mult: str = 'l2r'):
        '''
        Return a list of the seminormal basis elements of ``self``.

        The seminormal basis of a symmetric group algebra is defined as
        follows:

        Let `n` be a nonnegative integer. Let `R` be a `\\QQ`-algebra.
        In the following, we will use the "left action" convention for
        multiplying permutations. This means that for all permutations
        `p` and `q` in `S_n`, the product `pq` is defined in such a way
        that `(pq)(i) = p(q(i))` for each `i \\in \\{ 1, 2, \\ldots, n \\}`
        (this is the same convention as in :meth:`left_action_product`,
        but not the default semantics of the `*` operator on
        permutations in Sage). Thus, for instance, `s_2 s_1` is the
        permutation obtained by first transposing `1` with `2` and
        then transposing `2` with `3` (where `s_i = (i, i+1)`).

        For every partition `\\lambda` of `n`, let

        .. MATH::

            \\kappa_{\\lambda} = \\frac{n!}{f^{\\lambda}}

        where `f^{\\lambda}` is the number of standard Young tableaux
        of shape `\\lambda`. Note that `\\kappa_{\\lambda}` is an integer,
        namely the product of all hook lengths of `\\lambda` (by the
        hook length formula). In Sage, this integer can be computed by
        using :func:`sage.combinat.symmetric_group_algebra.kappa()`.

        Let `T` be a standard tableau of size `n`.

        Let `a(T)` denote the formal sum (in `R S_n`) of all
        permutations in `S_n` which stabilize the rows of `T` (as
        sets), i. e., which map each entry `i` of `T` to an entry in
        the same row as `i`. (See
        :func:`sage.combinat.symmetric_group_algebra.a()` for
        an implementation of this.)

        Let `b(T)` denote the signed formal sum (in `R S_n`) of all
        permutations in `S_n` which stabilize the columns of `T` (as
        sets). Here, "signed" means that each permutation is
        multiplied with its sign. (This is implemented in
        :func:`sage.combinat.symmetric_group_algebra.b()`.)

        Define an element `e(T)` of `R S_n` to be `a(T) b(T)`. (This
        is implemented in :func:`sage.combinat.symmetric_group_algebra.e()`
        for `R = \\QQ`.)

        Let `\\mathrm{sh}(T)` denote the shape of `T`.
        (See :meth:`~sage.combinat.tableau.Tableau.shape`.)

        Let `\\overline{T}` denote the standard tableau of size `n-1`
        obtained by removing the letter `n` (along with its cell) from
        `T` (if `n \\geq 1`).

        Now, we define an element `\\epsilon(T)` of `R S_n`. We define
        it by induction on the size `n` of `T`, so we set
        `\\epsilon(\\emptyset) = 1` and only need to define `\\epsilon(T)`
        for `n \\geq 1`, assuming that `\\epsilon(\\overline{T})` is
        already defined. We do this by setting

        .. MATH::

            \\epsilon(T) = \\frac{1}{\\kappa_{\\mathrm{sh}(T)}}
                          \\epsilon(\\overline{T})
                          e(T) \\epsilon(\\overline{T}).

        This element `\\epsilon(T)` is implemented as
        :func:`sage.combinat.symmetric_group_algebra.epsilon` for
        `R = \\QQ`, but it is also a particular case of the elements
        `\\epsilon(T, S)` defined below.

        Now let `S` be a further tableau of the same shape as `T`
        (possibly equal to `T`). Let `\\pi_{T, S}` denote the
        permutation in `S_n` such that applying this permutation to
        the entries of `T` yields the tableau `S`. Define an element
        `\\epsilon(T, S)` of `R S_n` by

        .. MATH::

            \\epsilon(T, S) = \\frac{1}{\\kappa_{\\mathrm{sh}(T)}}
                             \\epsilon(\\overline S) \\pi_{T, S}
                             e(T) \\epsilon(\\overline T)
                           = \\frac{1}{\\kappa_{\\mathrm{sh}(T)}}
                             \\epsilon(\\overline S) a(S) \\pi_{T, S}
                             b(T) \\epsilon(\\overline T).

        This element `\\epsilon(T, S)` is called *Young\'s seminormal
        unit corresponding to the bitableau `(T, S)`*, and is the
        return value of :meth:`epsilon_ik` applied to ``T`` and
        ``S``. Note that `\\epsilon(T, T) = \\epsilon(T)`.

        If we let `\\lambda` run through all partitions of `n`, and
        `(T, S)` run through all pairs of tableaux of shape
        `\\lambda`, then the elements `\\epsilon(T, S)` form a basis
        of `R S_n`. This basis is called *Young\'s seminormal basis*
        and has the properties that

        .. MATH::

            \\epsilon(T, S) \\epsilon(U, V) = \\delta_{T, V} \\epsilon(U, S)

        (where `\\delta` stands for the Kronecker delta).

        .. WARNING::

            Because of our convention, we are multiplying our elements in
            reverse of those given in some papers, for example [Ram1997]_.
            Using the other convention of multiplying permutations, we would
            instead have
            `\\epsilon(U, V) \\epsilon(T, S) = \\delta_{T, V} \\epsilon(U, S)`.

        In other words, Young\'s seminormal basis consists of the matrix
        units in a (particular) Artin-Wedderburn decomposition of `R S_n`
        into a direct product of matrix algebras over `\\QQ`.

        The output of :meth:`seminormal_basis` is a list of all
        elements of the seminormal basis of ``self``.

        INPUT:

        - ``mult`` -- string (default: ``\'l2r\'``); if set to ``\'r2l\'``,
          this causes the method to return the list of the
          antipodes (:meth:`antipode`) of all `\\epsilon(T, S)`
          instead of the `\\epsilon(T, S)` themselves.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ,3)
            sage: QS3.seminormal_basis()
            [1/6*[1, 2, 3] + 1/6*[1, 3, 2] + 1/6*[2, 1, 3] + 1/6*[2, 3, 1] + 1/6*[3, 1, 2] + 1/6*[3, 2, 1],
            1/3*[1, 2, 3] + 1/6*[1, 3, 2] - 1/3*[2, 1, 3] - 1/6*[2, 3, 1] - 1/6*[3, 1, 2] + 1/6*[3, 2, 1],
            1/3*[1, 3, 2] + 1/3*[2, 3, 1] - 1/3*[3, 1, 2] - 1/3*[3, 2, 1],
            1/4*[1, 3, 2] - 1/4*[2, 3, 1] + 1/4*[3, 1, 2] - 1/4*[3, 2, 1],
            1/3*[1, 2, 3] - 1/6*[1, 3, 2] + 1/3*[2, 1, 3] - 1/6*[2, 3, 1] - 1/6*[3, 1, 2] - 1/6*[3, 2, 1],
            1/6*[1, 2, 3] - 1/6*[1, 3, 2] - 1/6*[2, 1, 3] + 1/6*[2, 3, 1] + 1/6*[3, 1, 2] - 1/6*[3, 2, 1]]

        TESTS::

            sage: QS3g = SymmetricGroup(3).algebra(QQ)
            sage: QS3g.seminormal_basis()
            [1/6*() + 1/6*(2,3) + 1/6*(1,2) + 1/6*(1,2,3) + 1/6*(1,3,2) + 1/6*(1,3),
             1/3*() + 1/6*(2,3) - 1/3*(1,2) - 1/6*(1,2,3) - 1/6*(1,3,2) + 1/6*(1,3),
             1/3*(2,3) + 1/3*(1,2,3) - 1/3*(1,3,2) - 1/3*(1,3),
             1/4*(2,3) - 1/4*(1,2,3) + 1/4*(1,3,2) - 1/4*(1,3),
             1/3*() - 1/6*(2,3) + 1/3*(1,2) - 1/6*(1,2,3) - 1/6*(1,3,2) - 1/6*(1,3),
             1/6*() - 1/6*(2,3) - 1/6*(1,2) + 1/6*(1,2,3) + 1/6*(1,3,2) - 1/6*(1,3)]
        '''
    def dft(self, form=None, mult: str = 'l2r'):
        '''
        Return the discrete Fourier transform for ``self``.

        See [Mur1983]_ for the construction of central primitive orthogonal idempotents.
        For each idempotent `e_i` we have a homomorphic projection `v \\mapsto v e_i`.
        Choose a basis for each submodule spanned by `\\{\\sigma e_i | \\sigma \\in S_n\\}`.
        The change-of-basis from the standard basis `\\{\\sigma\\}_\\sigma` is returned.

        INPUT:

        - ``mult`` -- string (default: `l2r`); if set to `r2l`,
          this causes the method to use the antipodes
          (:meth:`antipode`) of the seminormal basis instead of
          the seminormal basis.

        - ``form`` -- string (default: ``"modular"`` if `p|n!` else ``"seminormal"``);
          one of the following:

          * ``"seminormal"`` -- use the seminormal basis
          * ``"modular"`` -- use the modular DFT, which uses the Peirce decomposition
            of the group algebra into blocks with central orthogonal idempotents
          * ``"unitary"`` -- use the unitary DFT, which computes the extended
            Cholesky decomposition of an `S_n`-invariant symmetric bilinear form as
            a change-of-basis matrix (for positive characteristics, it must be
            a finite field of square order)

        EXAMPLES:

        The default is the seminormal DFT when the characteristic does not divide the group order::

            sage: QQ_S3 = SymmetricGroupAlgebra(QQ, 3)
            sage: QQ_S3.dft()
            [   1    1    1    1    1    1]
            [   1  1/2   -1 -1/2 -1/2  1/2]
            [   0  3/4    0  3/4 -3/4 -3/4]
            [   0    1    0   -1    1   -1]
            [   1 -1/2    1 -1/2 -1/2 -1/2]
            [   1   -1   -1    1    1   -1]

        The unitary form works in characteristic zero::

            sage: U = QQ_S3.dft(form=\'unitary\'); U
            [-1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2]
            [       1/3*sqrt3        1/6*sqrt3       -1/3*sqrt3       -1/6*sqrt3       -1/6*sqrt3        1/6*sqrt3]
            [               0              1/2                0              1/2             -1/2             -1/2]
            [               0              1/2                0             -1/2              1/2             -1/2]
            [       1/3*sqrt3       -1/6*sqrt3        1/3*sqrt3       -1/6*sqrt3       -1/6*sqrt3       -1/6*sqrt3]
            [-1/6*sqrt3*sqrt2  1/6*sqrt3*sqrt2  1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2 -1/6*sqrt3*sqrt2  1/6*sqrt3*sqrt2]
            sage: U*U.H == 1
            True

        Over finite fields of square order with characteristic `p > n`, we can perform the unitary DFT::

            sage: GF25_S3 = SymmetricGroupAlgebra(GF(5**2), 3)
            sage: U = GF25_S3.dft(form=\'unitary\'); U
            [       1        1        1        1        1        1]
            [2*z2 + 4   z2 + 2 3*z2 + 1 4*z2 + 3 4*z2 + 3   z2 + 2]
            [       0        2        0        2        3        3]
            [       0   z2 + 1        0 4*z2 + 4   z2 + 1 4*z2 + 4]
            [2*z2 + 4 4*z2 + 3 2*z2 + 4 4*z2 + 3 4*z2 + 3 4*z2 + 3]
            [       1        4        4        1        1        4]
            sage: U*U.H == 1
            True

        Over fields of characteristic `p > 0` such that `p|n!`, we use the
        modular Fourier transform (:issue:`37751`)::

            sage: GF2_S3 = SymmetricGroupAlgebra(GF(2), 3)
            sage: GF2_S3.dft()
            [1 0 0 0 1 0]
            [0 1 0 0 0 1]
            [0 0 1 0 0 1]
            [0 0 0 1 1 0]
            [1 0 0 1 1 0]
            [0 1 1 0 0 1]
        '''
    def epsilon_ik(self, itab, ktab, star: int = 0, mult: str = 'l2r'):
        """
        Return the seminormal basis element of ``self`` corresponding to the
        pair of tableaux ``itab`` and ``ktab`` (or restrictions of these
        tableaux, if the optional variable ``star`` is set).

        INPUT:

        - ``itab``, ``ktab`` -- two standard tableaux of size `n`

        - ``star`` -- integer (default: `0`)

        - ``mult`` -- string (default: `l2r`); if set to `r2l`,
          this causes the method to return the antipode
          (:meth:`antipode`) of `\\epsilon(I, K)` instead of
          `\\epsilon(I, K)` itself.

        OUTPUT:

        The element `\\epsilon(I, K)`, where `I` and `K` are the tableaux
        obtained by removing all entries higher than `n - \\mathrm{star}`
        from ``itab`` and ``ktab``, respectively. Here, we are using the
        notations from :meth:`seminormal_basis`.

        EXAMPLES::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = QS3.epsilon_ik([[1,2,3]], [[1,2,3]]); a
            1/6*[1, 2, 3] + 1/6*[1, 3, 2] + 1/6*[2, 1, 3] + 1/6*[2, 3, 1] + 1/6*[3, 1, 2] + 1/6*[3, 2, 1]
            sage: QS3.dft()*vector(a)
            (1, 0, 0, 0, 0, 0)
            sage: a = QS3.epsilon_ik([[1,2],[3]], [[1,2],[3]]); a
            1/3*[1, 2, 3] - 1/6*[1, 3, 2] + 1/3*[2, 1, 3] - 1/6*[2, 3, 1] - 1/6*[3, 1, 2] - 1/6*[3, 2, 1]
            sage: QS3.dft()*vector(a)
            (0, 0, 0, 0, 1, 0)

        Let us take some properties of the seminormal basis listed in
        the docstring of :meth:`seminormal_basis`, and verify them on
        the situation of `S_3`.

        First, check the formula

        .. MATH::

            \\epsilon(T) = \\frac{1}{\\kappa_{\\mathrm{sh}(T)}}
                          \\epsilon(\\overline{T})
                          e(T) \\epsilon(\\overline{T}).

        In fact::

            sage: from sage.combinat.symmetric_group_algebra import e
            sage: def test_sn1(n):
            ....:     QSn = SymmetricGroupAlgebra(QQ, n)
            ....:     QSn1 = SymmetricGroupAlgebra(QQ, n - 1)
            ....:     for T in StandardTableaux(n):
            ....:         TT = T.restrict(n-1)
            ....:         eTT = QSn1.epsilon_ik(TT, TT)
            ....:         eT = QSn.epsilon_ik(T, T)
            ....:         kT = prod(T.shape().hooks())
            ....:         if kT * eT != eTT * e(T) * eTT:
            ....:             return False
            ....:     return True
            sage: test_sn1(3)
            True
            sage: test_sn1(4)   # long time
            True

        Next, we check the identity

        .. MATH::

            \\epsilon(T, S) = \\frac{1}{\\kappa_{\\mathrm{sh}(T)}}
                             \\epsilon(\\overline S) \\pi_{T, S}
                             e(T) \\epsilon(\\overline T)

        which we used to define `\\epsilon(T, S)`. In fact::

            sage: from sage.combinat.symmetric_group_algebra import e
            sage: def test_sn2(n):
            ....:     QSn = SymmetricGroupAlgebra(QQ, n)
            ....:     mul = QSn.left_action_product
            ....:     QSn1 = SymmetricGroupAlgebra(QQ, n - 1)
            ....:     for lam in Partitions(n):
            ....:         k = prod(lam.hooks())
            ....:         for T in StandardTableaux(lam):
            ....:             for S in StandardTableaux(lam):
            ....:                 TT = T.restrict(n-1)
            ....:                 SS = S.restrict(n-1)
            ....:                 eTT = QSn1.epsilon_ik(TT, TT)
            ....:                 eSS = QSn1.epsilon_ik(SS, SS)
            ....:                 eTS = QSn.epsilon_ik(T, S)
            ....:                 piTS = [0] * n
            ....:                 for (i, j) in T.cells():
            ....:                     piTS[T[i][j] - 1] = S[i][j]
            ....:                 piTS = QSn(Permutation(piTS))
            ....:                 if k * eTS != mul(mul(eSS, piTS), mul(e(T), eTT)):
            ....:                     return False
            ....:     return True
            sage: test_sn2(3)
            True
            sage: test_sn2(4)   # long time
            True

        Let us finally check the identity

        .. MATH::

            \\epsilon(T, S) \\epsilon(U, V) = \\delta_{T, V} \\epsilon(U, S)

        In fact::

            sage: def test_sn3(lam):
            ....:     n = lam.size()
            ....:     QSn = SymmetricGroupAlgebra(QQ, n)
            ....:     mul = QSn.left_action_product
            ....:     for T in StandardTableaux(lam):
            ....:         for S in StandardTableaux(lam):
            ....:             for U in StandardTableaux(lam):
            ....:                 for V in StandardTableaux(lam):
            ....:                     lhs = mul(QSn.epsilon_ik(T, S), QSn.epsilon_ik(U, V))
            ....:                     if T == V:
            ....:                         rhs = QSn.epsilon_ik(U, S)
            ....:                     else:
            ....:                         rhs = QSn.zero()
            ....:                     if rhs != lhs:
            ....:                         return False
            ....:     return True
            sage: all( test_sn3(lam) for lam in Partitions(3) )
            True
            sage: all( test_sn3(lam) for lam in Partitions(4) )   # long time
            True
        """
    def murphy_basis(self):
        """
        Return the :class:`Murphy basis
        <sage.combinat.symmetric_group_algebra.MurphyBasis>` of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: M = SGA.murphy_basis()
            sage: M(SGA.an_element())
            -C([1, 1, 1], [[1], [2], [3]], [[1], [2], [3]])
             + C([2, 1], [[1, 2], [3]], [[1, 2], [3]])
             + C([2, 1], [[1, 2], [3]], [[1, 3], [2]])
             + 2*C([2, 1], [[1, 3], [2]], [[1, 2], [3]])
             + 4*C([2, 1], [[1, 3], [2]], [[1, 3], [2]])
             - 3*C([3], [[1, 2, 3]], [[1, 2, 3]])
        """
    def murphy_basis_element(self, S, T):
        """
        Return the Murphy basis element indexed by ``S`` and ``T``.

        .. SEEALSO::

            :class:`~sage.combinat.symmetric_group_algebra.MurphyBasis`

        EXAMPLES::

            sage: import itertools
            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: for S, T in itertools.product(StandardTableaux([2,1]), repeat=2):
            ....:     print(S, T, SGA.murphy_basis_element(S, T))
            [[1, 3], [2]] [[1, 3], [2]] [1, 2, 3] + [2, 1, 3]
            [[1, 3], [2]] [[1, 2], [3]] [1, 3, 2] + [3, 1, 2]
            [[1, 2], [3]] [[1, 3], [2]] [1, 3, 2] + [2, 3, 1]
            [[1, 2], [3]] [[1, 2], [3]] [1, 2, 3] + [3, 2, 1]

        TESTS::

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: SGA.murphy_basis_element([[1,2,3,4]], [[1,2],[3,4]])
            Traceback (most recent call last):
            ...
            ValueError: [[1, 2, 3, 4]] is not an element of Standard tableaux of size 3
            sage: SGA.murphy_basis_element([[1,2,3]], [[1,2],[3]])
            Traceback (most recent call last):
            ...
            ValueError: S and T must have the same shape
        """
    def young_symmetrizer(self, la):
        """
        Return the Young symmetrizer of shape ``la`` of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, SymmetricGroup(3))
            sage: SGA.young_symmetrizer([2,1])
            () + (1,2) - (1,3,2) - (1,3)
            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: SGA.young_symmetrizer([2,1,1])
            [1, 2, 3, 4] - [1, 2, 4, 3] + [2, 1, 3, 4] - [2, 1, 4, 3]
             - [3, 1, 2, 4] + [3, 1, 4, 2] - [3, 2, 1, 4] + [3, 2, 4, 1]
             + [4, 1, 2, 3] - [4, 1, 3, 2] + [4, 2, 1, 3] - [4, 2, 3, 1]
            sage: SGA.young_symmetrizer([5,1,1])
            Traceback (most recent call last):
            ...
            ValueError: the partition [5, 1, 1] is not of size 4
        """
    def kazhdan_lusztig_cellular_basis(self):
        """
        Return the Kazhdan-Lusztig basis (at `q = 1`) of ``self``
        as a cellular basis.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: KL = SGA.kazhdan_lusztig_cellular_basis()
            sage: KL(SGA.an_element())
            C([2, 1], [[1, 2], [3]], [[1, 2], [3]])
             + C([2, 1], [[1, 3], [2]], [[1, 2], [3]])
             + 2*C([2, 1], [[1, 3], [2]], [[1, 3], [2]])
             - 3*C([3], [[1, 2, 3]], [[1, 2, 3]])
        """
    @cached_method
    def kazhdan_lusztig_basis_element(self, w):
        """
        Return the Kazhdan-Lusztig `C'_w` basis element at `q = 1`.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: for w in SGA.group():
            ....:     print(w, SGA.kazhdan_lusztig_basis_element(w))
            [1, 2, 3] [1, 2, 3]
            [1, 3, 2] [1, 2, 3] + [1, 3, 2]
            [2, 1, 3] [1, 2, 3] + [2, 1, 3]
            [2, 3, 1] [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1]
            [3, 1, 2] [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [3, 1, 2]
            [3, 2, 1] [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
        """

epsilon_ik_cache: Incomplete

def epsilon_ik(itab, ktab, star: int = 0):
    """
    Return the seminormal basis element of the symmetric group
    algebra `\\QQ S_n` corresponding to the pair of tableaux
    ``itab`` and ``ktab`` (or restrictions of these tableaux,
    if the optional variable ``star`` is set).

    INPUT:

    - ``itab``, ``ktab`` -- two standard tableaux of same size

    - ``star`` -- integer (default: `0`)

    OUTPUT:

    The element `\\epsilon(I, K) \\in \\QQ S_n`, where `I` and `K`
    are the tableaux obtained by removing all entries higher
    than `n - \\mathrm{star}` from ``itab`` and ``ktab``,
    respectively (where `n` is the size of ``itab`` and
    ``ktab``). Here, we are using the notations from
    :meth:`~sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra_n.seminormal_basis`.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import epsilon_ik
        sage: epsilon_ik([[1,2],[3]], [[1,3],[2]])
        1/4*[1, 3, 2] - 1/4*[2, 3, 1] + 1/4*[3, 1, 2] - 1/4*[3, 2, 1]
        sage: epsilon_ik([[1,2],[3]], [[1,3],[2]], star=1)
        Traceback (most recent call last):
        ...
        ValueError: the two tableaux must be of the same shape
    """

epsilon_cache: Incomplete

def epsilon(tab, star: int = 0):
    """
    The `(T, T)`-th element of the seminormal basis of the group
    algebra `\\QQ[S_n]`, where `T` is the tableau ``tab`` (with its
    ``star`` highest entries removed if the optional variable
    ``star`` is set).

    See the docstring of
    :meth:`~sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra_n.seminormal_basis`
    for the notation used herein.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import epsilon
        sage: epsilon([[1,2]])
        1/2*[1, 2] + 1/2*[2, 1]
        sage: epsilon([[1],[2]])
        1/2*[1, 2] - 1/2*[2, 1]
    """
def pi_ik(itab, ktab):
    """
    Return the permutation `p` which sends every entry of the
    tableau ``itab`` to the respective entry of the tableau
    ``ktab``, as an element of the corresponding symmetric group
    algebra.

    This assumes that ``itab`` and ``ktab`` are tableaux (possibly
    given just as lists of lists) of the same shape. Both
    tableaux are allowed to be skew.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import pi_ik
        sage: pi_ik([[1,3],[2]], [[1,2],[3]])
        [1, 3, 2]

    The same with skew tableaux::

        sage: from sage.combinat.symmetric_group_algebra import pi_ik
        sage: pi_ik([[None,1,3],[2]], [[None,1,2],[3]])
        [1, 3, 2]
    """
def kappa(alpha):
    """
    Return `\\kappa_\\alpha`, which is `n!` divided by the number
    of standard tableaux of shape `\\alpha` (where `\\alpha` is a
    partition of `n`).

    INPUT:

    - ``alpha`` -- integer partition (can be encoded as a list)

    OUTPUT:

    The factorial of the size of ``alpha``, divided by the number of
    standard tableaux of shape ``alpha``. Equivalently, the product
    of all hook lengths of ``alpha``.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import kappa
        sage: kappa(Partition([2,1]))
        3
        sage: kappa([2,1])
        3
    """
def a(tableau, star: int = 0, base_ring=...):
    """
    The row projection operator corresponding to the Young tableau
    ``tableau`` (which is supposed to contain every integer from
    `1` to its size precisely once, but may and may not be standard).

    This is the sum (in the group algebra of the relevant symmetric
    group over `\\QQ`) of all the permutations which preserve
    the rows of ``tableau``. It is called `a_{\\text{tableau}}` in
    [EGHLSVY]_, Section 4.2.

    INPUT:

    - ``tableau`` -- Young tableau which contains every integer
      from `1` to its size precisely once

    - ``star`` -- nonnegative integer (default: `0`); when this
      optional variable is set, the method computes not the row
      projection operator of ``tableau``, but the row projection
      operator of the restriction of ``tableau`` to the entries
      ``1, 2, ..., tableau.size() - star`` instead.

    - ``base_ring`` -- commutative ring (default: ``QQ``); when this
      optional variable is set, the row projection operator is
      computed over a user-determined base ring instead of `\\QQ`.
      (Note that symmetric group algebras currently don't preserve
      coercion, so e. g. a symmetric group algebra over `\\ZZ`
      does not coerce into the corresponding one over `\\QQ`; so
      convert manually or choose your base rings wisely!)

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import a
        sage: a([[1,2]])
        [1, 2] + [2, 1]
        sage: a([[1],[2]])
        [1, 2]
        sage: a([])
        []
        sage: a([[1, 5], [2, 3], [4]])
        [1, 2, 3, 4, 5] + [1, 3, 2, 4, 5] + [5, 2, 3, 4, 1] + [5, 3, 2, 4, 1]
        sage: a([[1,4], [2,3]], base_ring=ZZ)
        [1, 2, 3, 4] + [1, 3, 2, 4] + [4, 2, 3, 1] + [4, 3, 2, 1]

    The same with a skew tableau::

        sage: a([[None,1,4], [2,3]], base_ring=ZZ)
        [1, 2, 3, 4] + [1, 3, 2, 4] + [4, 2, 3, 1] + [4, 3, 2, 1]
    """
def b(tableau, star: int = 0, base_ring=...):
    """
    The column projection operator corresponding to the Young tableau
    ``tableau`` (which is supposed to contain every integer from
    `1` to its size precisely once, but may and may not be standard).

    This is the signed sum (in the group algebra of the relevant
    symmetric group over `\\QQ`) of all the permutations which
    preserve the column of ``tableau`` (where the signs are the usual
    signs of the permutations). It is called `b_{\\text{tableau}}` in
    [EGHLSVY]_, Section 4.2.

    INPUT:

    - ``tableau`` -- Young tableau which contains every integer
      from `1` to its size precisely once

    - ``star`` -- nonnegative integer (default: `0`). When this
      optional variable is set, the method computes not the column
      projection operator of ``tableau``, but the column projection
      operator of the restriction of ``tableau`` to the entries
      ``1, 2, ..., tableau.size() - star`` instead.

    - ``base_ring`` -- commutative ring (default: ``QQ``). When this
      optional variable is set, the column projection operator is
      computed over a user-determined base ring instead of `\\QQ`.
      (Note that symmetric group algebras currently don't preserve
      coercion, so e. g. a symmetric group algebra over `\\ZZ`
      does not coerce into the corresponding one over `\\QQ`; so
      convert manually or choose your base rings wisely!)

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import b
        sage: b([[1,2]])
        [1, 2]
        sage: b([[1],[2]])
        [1, 2] - [2, 1]
        sage: b([])
        []
        sage: b([[1, 2, 4], [5, 3]])
        [1, 2, 3, 4, 5] - [1, 3, 2, 4, 5] - [5, 2, 3, 4, 1] + [5, 3, 2, 4, 1]
        sage: b([[1, 4], [2, 3]], base_ring=ZZ)
        [1, 2, 3, 4] - [1, 2, 4, 3] - [2, 1, 3, 4] + [2, 1, 4, 3]
        sage: b([[1, 4], [2, 3]], base_ring=Integers(5))
        [1, 2, 3, 4] + 4*[1, 2, 4, 3] + 4*[2, 1, 3, 4] + [2, 1, 4, 3]

    The same with a skew tableau::

        sage: b([[None, 2, 4], [1, 3], [5]])
        [1, 2, 3, 4, 5] - [1, 3, 2, 4, 5] - [5, 2, 3, 4, 1] + [5, 3, 2, 4, 1]

    With the ``l2r`` setting for multiplication, the unnormalized
    Young symmetrizer ``e(tableau)`` should be the product
    ``b(tableau) * a(tableau)`` for every ``tableau``. Let us check
    this on the standard tableaux of size 5::

        sage: from sage.combinat.symmetric_group_algebra import a, b, e
        sage: all( e(t) == b(t) * a(t) for t in StandardTableaux(5) )
        True
    """

e_cache: Incomplete

def e(tableau, star: int = 0):
    '''
    The unnormalized Young projection operator corresponding to
    the Young tableau ``tableau`` (which is supposed to contain
    every integer from `1` to its size precisely once, but may
    and may not be standard).

    If `n` is a nonnegative integer, and `T` is a Young tableau
    containing every integer from `1` to `n` exactly once, then
    the unnormalized Young projection operator `e(T)` is defined by

    .. MATH::

        e(T) = a(T) b(T) \\in \\QQ S_n,

    where `a(T) \\in \\QQ S_n` is the sum of all permutations in `S_n`
    which fix the rows of `T` (as sets), and `b(T) \\in \\QQ S_n` is the
    signed sum of all permutations in `S_n` which fix the columns of
    `T` (as sets). Here, "signed" means that each permutation is
    multiplied with its sign; and the product on the group `S_n` is
    defined in such a way that `(pq)(i) = p(q(i))` for any
    permutations `p` and `q` and any `1 \\leq i \\leq n`.

    Note that the definition of `e(T)` is not uniform across
    literature. Others define it as `b(T) a(T)` instead, or include
    certain scalar factors (we do not, whence "unnormalized").

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import e
        sage: e([[1,2]])
        [1, 2] + [2, 1]
        sage: e([[1],[2]])
        [1, 2] - [2, 1]
        sage: e([])
        []

    There are differing conventions for the order of the symmetrizers
    and antisymmetrizers.  This example illustrates our conventions::

        sage: e([[1,2],[3]])
        [1, 2, 3] + [2, 1, 3] - [3, 1, 2] - [3, 2, 1]

    To obtain the product `b(T) a(T)`, one has to take the antipode
    of this::

        sage: QS3 = parent(e([[1,2],[3]]))
        sage: QS3.antipode(e([[1,2],[3]]))
        [1, 2, 3] + [2, 1, 3] - [2, 3, 1] - [3, 2, 1]

    And here is an example for a skew tableau::

        sage: e([[None, 2, 1], [4, 3]])
        [1, 2, 3, 4] + [1, 2, 4, 3] - [1, 3, 2, 4] - [1, 4, 2, 3]
         + [2, 1, 3, 4] + [2, 1, 4, 3] - [2, 3, 1, 4] - [2, 4, 1, 3]

    .. SEEALSO::

        :func:`e_hat`
    '''

ehat_cache: Incomplete

def e_hat(tab, star: int = 0):
    '''
    The Young projection operator corresponding to the Young tableau
    ``tab`` (which is supposed to contain every integer from `1` to
    its size precisely once, but may and may not be standard). This
    is an idempotent in the rational group algebra.

    If `n` is a nonnegative integer, and `T` is a Young tableau
    containing every integer from `1` to `n` exactly once, then
    the Young projection operator `\\widehat{e}(T)` is defined by

    .. MATH::

        \\widehat{e}(T) = \\frac{1}{\\kappa_\\lambda} a(T) b(T) \\in \\QQ S_n,

    where `\\lambda` is the shape of `T`, where `\\kappa_\\lambda` is
    `n!` divided by the number of standard tableaux of shape
    `\\lambda`, where `a(T) \\in \\QQ S_n` is the sum of all
    permutations in `S_n` which fix the rows of `T` (as sets), and
    where `b(T) \\in \\QQ S_n` is the signed sum of all permutations
    in `S_n` which fix the columns of `T` (as sets). Here, "signed"
    means that each permutation is multiplied with its sign; and
    the product on the group `S_n` is defined in such a way that
    `(pq)(i) = p(q(i))` for any permutations `p` and `q` and any
    `1 \\leq i \\leq n`.

    Note that the definition of `\\widehat{e}(T)` is not uniform
    across literature. Others define it as
    `\\frac{1}{\\kappa_\\lambda} b(T) a(T)` instead.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import e_hat
        sage: e_hat([[1,2,3]])
        1/6*[1, 2, 3] + 1/6*[1, 3, 2] + 1/6*[2, 1, 3] + 1/6*[2, 3, 1] + 1/6*[3, 1, 2] + 1/6*[3, 2, 1]
        sage: e_hat([[1],[2]])
        1/2*[1, 2] - 1/2*[2, 1]

    There are differing conventions for the order of the symmetrizers
    and antisymmetrizers.  This example illustrates our conventions::

        sage: e_hat([[1,2],[3]])
        1/3*[1, 2, 3] + 1/3*[2, 1, 3] - 1/3*[3, 1, 2] - 1/3*[3, 2, 1]

    .. SEEALSO::

        :func:`e`
    '''

e_ik_cache: Incomplete

def e_ik(itab, ktab, star: int = 0):
    """
    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import e_ik
        sage: e_ik([[1,2,3]], [[1,2,3]])
        [1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1] + [3, 1, 2] + [3, 2, 1]
        sage: e_ik([[1,2,3]], [[1,2,3]], star=1)
        [1, 2] + [2, 1]
    """
def seminormal_test(n):
    """
    Run a variety of tests to verify that the construction of the
    seminormal basis works as desired. The numbers appearing are
    results in James and Kerber's 'Representation Theory of the
    Symmetric Group' [JK1981]_.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_algebra import seminormal_test
        sage: seminormal_test(3)
        True
    """

class SGACellularBasis(CellularBasis):
    """
    A cellular basis of the symmetric group algebra.
    """
    def __init__(self, SGA) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 3)
            sage: M = SGA.murphy_basis()
            sage: TestSuite(M).run()
            sage: KL = SGA.kazhdan_lusztig_cellular_basis()
            sage: TestSuite(KL).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the basis element for the multiplicative identity.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
            sage: M = SGA.murphy_basis()
            sage: M.one_basis()
            ([4], [[1, 2, 3, 4]], [[1, 2, 3, 4]])
        """
    @cached_method
    def one(self):
        """
        Return the element `1` in ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
            sage: M = SGA.murphy_basis()
            sage: M.one()
            C([4], [[1, 2, 3, 4]], [[1, 2, 3, 4]])
        """

class MurphyBasis(SGACellularBasis):
    """
    The Murphy basis of a symmetric group algebra.

    Let `R` be a commutative ring, and let `A = R[S_n]` denote the group
    algebra (over `R`) of `S_n`. The *Murphy basis* is the basis of `A`
    defined as follows. Let `S, T` be standard tableaux of shape `\\lambda`.
    Define `T^{\\lambda}` as the standard tableau of shape `\\lambda` with
    the first row filled with `1, \\ldots, \\lambda_1`, the second row
    `\\lambda_1+1, \\ldots, \\lambda_1+\\lambda_2`, and so on. Let `d(S)` be
    the unique permutation such that `S = T^{\\lambda} d(S)` under the natural
    action. Then the Murphy basis element indexed by `S` and `T` is

    .. MATH::

        M_{S'T'} = d(S)^{-1} R_{\\lambda} d(T),

    where `S'` denotes the conjugate tableau.
    The Murphy basis is a :class:`cellular basis
    <sage.algebras.cellular_basis.CellularBasis>` of `A`.

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
        sage: M = SGA.murphy_basis()
        sage: for la in M.simple_module_parameterization():
        ....:     CM = M.cell_module(la)
        ....:     print(la, CM.dimension(), CM.simple_module().dimension())
        [2, 2, 1] 5 4
        [3, 1, 1] 6 6
        [3, 2] 5 1
        [4, 1] 4 4
        [5] 1 1

    REFERENCES:

    - [DJM1998]_
    - [Mathas2004]_
    """
class KLCellularBasis(SGACellularBasis):
    """
    The Kazhdan-Lusztig `C'` basis (at `q = 1`) of the symmetric group
    algebra realized as a :class:`cellular basis
    <sage.algebras.cellular_basis.CellularBasis>`

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(GF(3), 5)
        sage: KL = SGA.kazhdan_lusztig_cellular_basis()
        sage: for la in KL.simple_module_parameterization():
        ....:     CM = KL.cell_module(la)
        ....:     print(la, CM.dimension(), CM.simple_module().dimension())
        [2, 2, 1] 5 4
        [3, 1, 1] 6 6
        [3, 2] 5 1
        [4, 1] 4 4
        [5] 1 1
    """

def HeckeAlgebraSymmetricGroupT(R, n, q=None):
    '''
    Return the Hecke algebra of the symmetric group `S_n` on the T-basis
    with quantum parameter ``q`` over the ring `R`.

    If `R` is a commutative ring and `q` is an invertible element of `R`,
    and if `n` is a nonnegative integer, then the Hecke algebra of the
    symmetric group `S_n` over `R` with quantum parameter `q` is defined
    as the algebra generated by the generators `T_1, T_2, \\ldots, T_{n-1}`
    with relations

    .. MATH::

        T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}

    for all `i < n-1` ("braid relations"),

    .. MATH::

        T_i T_j = T_j T_i

    for all `i` and `j` such that `| i-j | > 1` ("locality relations"),
    and

    .. MATH::

        T_i^2 = q + (q-1) T_i

    for all `i` (the "quadratic relations", also known in the form
    `(T_i + 1) (T_i - q) = 0`). (This is only one of several existing
    definitions in literature, not all of which are fully equivalent.
    We are following the conventions of [Go1993]_.) For any permutation
    `w \\in S_n`, we can define an element `T_w` of this Hecke algebra by
    setting `T_w = T_{i_1} T_{i_2} \\cdots T_{i_k}`, where
    `w = s_{i_1} s_{i_2} \\cdots s_{i_k}` is a reduced word for `w`
    (with `s_i` meaning the transposition `(i, i+1)`, and the product of
    permutations being evaluated by first applying `s_{i_k}`, then
    `s_{i_{k-1}}`, etc.). This element is independent of the choice of
    the reduced decomposition, and can be computed in Sage by calling
    ``H[w]`` where ``H`` is the Hecke algebra and ``w`` is the
    permutation.

    The Hecke algebra of the symmetric group `S_n` with quantum parameter
    `q` over `R` can be seen as a deformation of the group algebra
    `R S_n`; indeed, it becomes `R S_n` when `q = 1`.

    .. WARNING::

        The multiplication on the Hecke algebra of the symmetric group
        does *not* follow the global option ``mult`` of the
        :class:`Permutations` class (see
        :meth:`~sage.combinat.permutation.Permutations.options`).
        It is always as defined above. It does not match the default
        option (``mult=l2r``) of the symmetric group algebra!

    EXAMPLES::

        sage: HeckeAlgebraSymmetricGroupT(QQ, 3)
        Hecke algebra of the symmetric group of order 3 on the T basis over Univariate Polynomial Ring in q over Rational Field

    ::

        sage: HeckeAlgebraSymmetricGroupT(QQ, 3, 2)
        Hecke algebra of the symmetric group of order 3 with q=2 on the T basis over Rational Field

    The multiplication on the Hecke algebra follows a different convention
    than the one on the symmetric group algebra does by default::

        sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3)
        sage: H3([1,3,2]) * H3([2,1,3])
        T[3, 1, 2]
        sage: S3 = SymmetricGroupAlgebra(QQ, 3)
        sage: S3([1,3,2]) * S3([2,1,3])
        [2, 3, 1]

        sage: TestSuite(H3).run()

    .. NOTE::

        :class:`~sage.algebras.iwahori_hecke_algebra.IwahoriHeckeAlgebra` gives
        a different implementation of the Iwahori-Hecke algebras of a Coxeter
        system `(W,S)`. This includes the Hecke algebras of the symmetric group
        as special case.
    '''

class HeckeAlgebraSymmetricGroup_generic(CombinatorialFreeModule):
    n: Incomplete
    def __init__(self, R, n, q=None) -> None:
        """
        TESTS::

            sage: HeckeAlgebraSymmetricGroupT(QQ, 3)
            Hecke algebra of the symmetric group of order 3 on the T basis over Univariate Polynomial Ring in q over Rational Field

        ::

            sage: HeckeAlgebraSymmetricGroupT(QQ, 3, q=1)
            Hecke algebra of the symmetric group of order 3 with q=1 on the T basis over Rational Field
        """
    @cached_method
    def one_basis(self):
        """
        Return the identity permutation.

        EXAMPLES::

            sage: HeckeAlgebraSymmetricGroupT(QQ, 3).one()  # indirect doctest
            T[1, 2, 3]
        """
    def q(self):
        """
        Return the variable or parameter `q`.

        EXAMPLES::

            sage: HeckeAlgebraSymmetricGroupT(QQ, 3).q()
            q
            sage: HeckeAlgebraSymmetricGroupT(QQ, 3, 2).q()
            2
        """

class HeckeAlgebraSymmetricGroup_t(HeckeAlgebraSymmetricGroup_generic):
    def __init__(self, R, n, q=None) -> None:
        """
        TESTS::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3)
            sage: H3 == loads(dumps(H3))
            True
        """
    def t_action_on_basis(self, perm, i):
        """
        Return the product `T_i \\cdot T_{perm}`, where ``perm`` is a
        permutation in the symmetric group `S_n`.

        EXAMPLES::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3)
            sage: H3.t_action_on_basis(Permutation([2,1,3]), 1)
            q*T[1, 2, 3] + (q-1)*T[2, 1, 3]
            sage: H3.t_action_on_basis(Permutation([1,2,3]), 1)
            T[2, 1, 3]
            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3, 1)
            sage: H3.t_action_on_basis(Permutation([2,1,3]), 1)
            T[1, 2, 3]
            sage: H3.t_action_on_basis(Permutation([1,3,2]), 2)
            T[1, 2, 3]
        """
    def t_action(self, a, i):
        """
        Return the product `T_i \\cdot a`.

        EXAMPLES::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3)
            sage: a = H3([2,1,3])+2*H3([1,2,3])
            sage: H3.t_action(a, 1)
            q*T[1, 2, 3] + (q+1)*T[2, 1, 3]
            sage: H3.t(1)*a
            q*T[1, 2, 3] + (q+1)*T[2, 1, 3]
        """
    def product_on_basis(self, perm1, perm2):
        """
        EXAMPLES::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ, 3, 1)
            sage: a = H3([2,1,3])+2*H3([1,2,3])-H3([3,2,1])
            sage: a^2 #indirect doctest
            6*T[1, 2, 3] + 4*T[2, 1, 3] - T[2, 3, 1]
            - T[3, 1, 2] - 4*T[3, 2, 1]

        ::

            sage: QS3 = SymmetricGroupAlgebra(QQ, 3)
            sage: a = QS3([2,1,3])+2*QS3([1,2,3])-QS3([3,2,1])
            sage: a^2
            6*[1, 2, 3] + 4*[2, 1, 3] - [2, 3, 1] - [3, 1, 2] - 4*[3, 2, 1]
        """
    def t(self, i):
        """
        Return the element `T_i` of the Hecke algebra ``self``.

        EXAMPLES::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ,3)
            sage: H3.t(1)
            T[2, 1, 3]
            sage: H3.t(2)
            T[1, 3, 2]
            sage: H3.t(0)
            Traceback (most recent call last):
            ...
            ValueError: i (= 0) must be between 1 and n-1 (= 2)
        """
    def algebra_generators(self):
        """
        Return the generators of the algebra.

        EXAMPLES::

            sage: HeckeAlgebraSymmetricGroupT(QQ,3).algebra_generators()
            [T[2, 1, 3], T[1, 3, 2]]
        """
    def jucys_murphy(self, k):
        '''
        Return the Jucys-Murphy element `J_k` of the Hecke algebra.

        These Jucys-Murphy elements are defined by

        .. MATH::

            J_k = (T_{k-1} T_{k-2} \\cdots T_1) (T_1 T_2 \\cdots T_{k-1}).

        More explicitly,

        .. MATH::

            J_k = q^{k-1} + \\sum_{l=1}^{k-1} (q^l - q^{l-1}) T_{(l, k)}.

        For generic `q`, the `J_k` generate a maximal commutative
        sub-algebra of the Hecke algebra.

        .. WARNING::

            The specialization `q = 1` does *not* map these elements
            `J_k` to the Young-Jucys-Murphy elements of the group
            algebra `R S_n`. (Instead, it maps the "reduced"
            Jucys-Murphy elements `(J_k - q^{k-1}) / (q - 1)` to the
            Young-Jucys-Murphy elements of `R S_n`.)

        EXAMPLES::

            sage: H3 = HeckeAlgebraSymmetricGroupT(QQ,3)
            sage: j2 = H3.jucys_murphy(2); j2
            q*T[1, 2, 3] + (q-1)*T[2, 1, 3]
            sage: j3 = H3.jucys_murphy(3); j3
            q^2*T[1, 2, 3] + (q^2-q)*T[1, 3, 2] + (q-1)*T[3, 2, 1]
            sage: j2*j3 == j3*j2
            True
            sage: j0 = H3.jucys_murphy(1); j0 == H3.one()
            True
            sage: H3.jucys_murphy(0)
            Traceback (most recent call last):
            ...
            ValueError: k (= 0) must be between 1 and n (= 3)
        '''
