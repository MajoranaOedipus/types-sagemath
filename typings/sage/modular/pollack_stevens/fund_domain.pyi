from .sigma0 import Sigma0 as Sigma0
from _typeshed import Incomplete
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.modular.modsym.all import P1List as P1List
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

M2ZSpace: Incomplete

def M2Z(x):
    """
    Create an immutable `2 \\times 2` integer matrix from ``x``.

    INPUT:

    - ``x`` -- anything that can be converted into a `2 \\times 2` matrix

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.fund_domain import M2Z
        sage: M2Z([1,2,3,4])
        [1 2]
        [3 4]
        sage: M2Z(1)
        [1 0]
        [0 1]
    """

Id: Incomplete
sig: Incomplete
tau: Incomplete
minone_inf_path: Incomplete
t00: Incomplete
t10: Incomplete
t01: Incomplete
t11: Incomplete

class PollackStevensModularDomain(SageObject):
    """
    The domain of a modular symbol.

    INPUT:

    - ``N`` -- positive integer, the level of the congruence subgroup
      `\\Gamma_0(N)`

    - ``reps`` -- list of `2 \\times 2` matrices, the coset
      representatives of `Div^0(P^1(\\QQ))`

    - ``indices`` -- list of integers; indices of elements in
      ``reps`` which are generators

    - ``rels`` -- list of list of triples ``(d, A, i)``, one for each
      coset representative of ``reps`` which describes how to express the
      elements of ``reps`` in terms of generators specified by ``indices``.
      See :meth:`relations` for a detailed explanations of these triples.

    - ``equiv_ind`` -- dictionary which maps normalized coordinates on
      `P^1(\\ZZ/N\\ZZ)` to an integer such that a matrix whose bottom row is
      equivalent to `[a:b]` in `P^1(\\ZZ/N\\ZZ)` is in the coset of
      ``reps[equiv_ind[(a,b)]]``

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.fund_domain import PollackStevensModularDomain, M2Z
        sage: PollackStevensModularDomain(2 , [M2Z([1,0,0,1]), M2Z([1,1,-1,0]), M2Z([0,-1,1,1])], [0,2], [[(1, M2Z([1,0,0,1]), 0)], [(-1,M2Z([-1,-1,0,-1]),0)], [(1, M2Z([1,0,0,1]), 2)]], {(0,1): 0, (1,0): 1, (1,1): 2})
        Modular Symbol domain of level 2

    TESTS:

    The level ``N`` must be an integer::

        sage: PollackStevensModularDomain(1/2, None, None, None, None)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
        sage: PollackStevensModularDomain(Gamma0(11), None, None, None, None)
        Traceback (most recent call last):
        ...
        TypeError: unable to coerce <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class_with_category'> to an integer
    """
    def __init__(self, N, reps, indices, rels, equiv_ind) -> None:
        """
        INPUT:

        See :class:`PollackStevensModularDomain`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import PollackStevensModularDomain, ManinRelations
            sage: isinstance(ManinRelations(11), PollackStevensModularDomain) # indirect doctest
            True
        """
    def __len__(self) -> int:
        """
        Return the number of coset representatives.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: len(A)
            12
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th coset representative.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A[4]
            [-1 -2]
            [ 2  3]
        """
    def __iter__(self):
        """
        Return an iterator over all coset representatives.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: for rep in A:
            ....:     if rep[1,0] == 1:
            ....:         print(rep)
            [ 0 -1]
            [ 1  3]
            [ 0 -1]
            [ 1  2]
            [ 0 -1]
            [ 1  1]
        """
    def gens(self) -> tuple:
        """
        Return the tuple of coset representatives chosen as generators.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.gens()
            (
            [1 0]  [ 0 -1]  [-1 -1]
            [0 1], [ 1  3], [ 3  2]
            )
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator.

        INPUT:

        - ``n`` -- integer (default: 0); which generator is desired

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(137)
            sage: A.gen(17)
            [-4 -1]
            [ 9  2]
        """
    def ngens(self):
        """
        Return the number of generators.

        OUTPUT:

        The number of coset representatives from which a modular symbol's value
        on any coset can be derived.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(1137)
            sage: A.ngens()
            255
        """
    def level(self):
        """
        Return the level `N` of `\\Gamma_0(N)` that we work with.

        OUTPUT:

        The integer `N` of the group `\\Gamma_0(N)` for which the Manin
        Relations are being computed.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.level()
            11
        """
    def indices(self, n=None):
        """
        Return the `n`-th index of the coset representatives which were
        chosen as our generators.

        In particular, the divisors associated to these coset representatives
        generate all divisors over `\\ZZ[\\Gamma_0(N)]`, and thus a modular
        symbol is uniquely determined by its values on these divisors.

        INPUT:

        - ``n`` -- integer (default: ``None``)

        OUTPUT:

        The ``n``-th index of the generating set in ``self.reps()`` or all
        indices if ``n`` is ``None``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.indices()
            [0, 2, 3]

            sage: A.indices(2)
            3

            sage: A = ManinRelations(13)
            sage: A.indices()
            [0, 2, 3, 4, 5]

            sage: A = ManinRelations(101)
            sage: A.indices()
            [0, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 16, 17, 19, 20, 23, 24, 26, 28]
        """
    def reps(self, n=None):
        """
        Return the ``n``-th coset representative associated with our
        fundamental domain.

        INPUT:

        - ``n`` -- integer (default: ``None``)

        OUTPUT:

        The ``n``-th coset representative or all coset representatives if ``n``
        is ``None``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.reps(0)
            [1 0]
            [0 1]
            sage: A.reps(1)
            [ 1  1]
            [-1  0]
            sage: A.reps(2)
            [ 0 -1]
            [ 1  3]
            sage: A.reps()
            [
            [1 0]  [ 1  1]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -1]  [ 0 -1]  [ 1  0]
            [0 1], [-1  0], [ 1  3], [ 3  2], [ 2  3], [ 3  1], [ 1  2], [-2  1],
            <BLANKLINE>
            [ 0 -1]  [ 1  0]  [-1 -1]  [ 1 -1]
            [ 1  1], [-1  1], [ 2  1], [-1  2]
            ]
        """
    def relations(self, A=None):
        """
        Express the divisor attached to the coset representative of ``A`` in
        terms of our chosen generators.

        INPUT:

        - ``A`` -- ``None``, an integer, or a coset representative (default:
          ``None``)

        OUTPUT:

        A `\\ZZ[\\Gamma_0(N)]`-relation expressing the divisor attached to ``A``
        in terms of the generating set. The relation is given as a list of
        triples ``(d, B, i)`` such that the divisor attached to ``A`` is the sum
        of ``d`` times the divisor attached to ``B^{-1} * self.reps(i)``.

        If ``A`` is an integer, then return this data for the ``A``-th
        coset representative.

        If ``A`` is ``None``, then return this data in a list for all coset
        representatives.

        .. NOTE::

            These relations allow us to recover the value of a modular symbol
            on any coset representative in terms of its values on our
            generating set.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(11)
            sage: MR.indices()
            [0, 2, 3]
            sage: MR.relations(0)
            [(1, [1 0]
            [0 1], 0)]
            sage: MR.relations(2)
            [(1, [1 0]
            [0 1], 2)]
            sage: MR.relations(3)
            [(1, [1 0]
            [0 1], 3)]

        The fourth coset representative can be expressed through the
        second coset representative::

            sage: MR.reps(4)
            [-1 -2]
            [ 2  3]
            sage: d, B, i = MR.relations(4)[0]
            sage: P = B.inverse()*MR.reps(i); P
            [ 2 -1]
            [-3  2]
            sage: d # the above corresponds to minus the divisor of A.reps(4) since d is -1
            -1

        The sixth coset representative can be expressed as the sum of
        the second and the third::

            sage: MR.reps(6)
            [ 0 -1]
            [ 1  2]
            sage: MR.relations(6)
            [(1, [1 0]
            [0 1], 2), (1, [1 0]
            [0 1], 3)]
            sage: MR.reps(2), MR.reps(3) # MR.reps(6) is the sum of these divisors
            (
            [ 0 -1]  [-1 -1]
            [ 1  3], [ 3  2]
            )

        TESTS:

        Test that the other ways of calling this method work::

            sage: MR.relations(MR.reps(6))
            [(1, [1 0]
            [0 1], 2), (1, [1 0]
            [0 1], 3)]
            sage: MR.relations(None)
            [[(1, [1 0]
            [0 1], 0)], [(-1, [-1 -1]
            [ 0 -1], 0)], [(1, [1 0]
            [0 1], 2)], [(1, [1 0]
            [0 1], 3)], [(-1, [-3 -2]
            [11  7], 2)], [(-1, [-4 -3]
            [11  8], 3)], [(1, [1 0]
            [0 1], 2), (1, [1 0]
            [0 1], 3)], [(-1, [1 0]
            [0 1], 2), (-1, [1 0]
            [0 1], 3)], [(1, [1 0]
            [0 1], 2), (1, [1 0]
            [0 1], 3), (-1, [-3 -2]
            [11  7], 2), (-1, [-4 -3]
            [11  8], 3)], [(-1, [1 0]
            [0 1], 2), (-1, [1 0]
            [0 1], 3), (1, [-3 -2]
            [11  7], 2), (1, [-4 -3]
            [11  8], 3)], [(-1, [-3 -2]
            [11  7], 2), (-1, [-4 -3]
            [11  8], 3)], [(1, [-3 -2]
            [11  7], 2), (1, [-4 -3]
            [11  8], 3)]]
        """
    def equivalent_index(self, A):
        """
        Return the index of the coset representative equivalent to ``A``.

        Here by equivalent we mean the unique coset representative whose bottom
        row is equivalent to the bottom row of ``A`` in `P^1(\\ZZ/N\\ZZ)`.

        INPUT:

        - ``A`` -- an element of `SL_2(\\ZZ)`

        OUTPUT:

        The unique integer ``j`` satisfying that the bottom row of
        ``self.reps(j)`` is equivalent to the bottom row of ``A``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(11)
            sage: A = matrix(ZZ,2,2,[1,5,3,16])
            sage: j = MR.equivalent_index(A); j
            11
            sage: MR.reps(11)
            [ 1 -1]
            [-1  2]
            sage: MR.equivalent_rep(A)
            [ 1 -1]
            [-1  2]
            sage: MR.P1().normalize(3,16)
            (1, 9)
        """
    def equivalent_rep(self, A):
        """
        Return a coset representative that is equivalent to ``A`` modulo
        `\\Gamma_0(N)`.

        INPUT:

        - ``A`` -- a matrix in `SL_2(\\ZZ)`

        OUTPUT:

        The unique generator congruent to ``A`` modulo `\\Gamma_0(N)`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = matrix([[5,3],[38,23]])
            sage: ManinRelations(60).equivalent_rep(A)
            [-7 -3]
            [26 11]
        """
    def P1(self):
        """
        Return the Sage representation of `P^1(\\ZZ/N\\ZZ)`.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.P1()
            The projective line over the integers modulo 11
        """

class ManinRelations(PollackStevensModularDomain):
    """
    This class gives a description of `Div^0(P^1(\\QQ))` as a
    `\\ZZ[\\Gamma_0(N)]`-module.

    INPUT:

    - ``N`` -- positive integer, the level of `\\Gamma_0(N)` to work with

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
        sage: ManinRelations(1)
        Manin Relations of level 1
        sage: ManinRelations(11)
        Manin Relations of level 11

    Large values of ``N`` are not supported::

        sage: ManinRelations(2^20)
        Traceback (most recent call last):
        ...
        OverflowError: Modulus is too large (must be <= 46340)

    TESTS:

    ``N`` has to be a positive integer::

        sage: ManinRelations(0)
        Traceback (most recent call last):
        ...
        ValueError: N must be a positive integer
        sage: ManinRelations(-5)
        Traceback (most recent call last):
        ...
        ValueError: N must be a positive integer
    """
    gammas: Incomplete
    def __init__(self, N) -> None:
        """
        Create an instance of this class.

        INPUT:

        - ``N`` -- positive integer; the level of `\\Gamma_0(N)` to work with

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: type(ManinRelations(30))
            <class 'sage.modular.pollack_stevens.fund_domain.ManinRelations'>
        """
    def indices_with_two_torsion(self):
        """
        Return the indices of coset representatives whose associated unimodular path
        contains a point fixed by a `\\Gamma_0(N)` element of order 2 (where the
        order is computed in `PSL_2(\\ZZ)`).

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(11)
            sage: MR.indices_with_two_torsion()
            []
            sage: MR = ManinRelations(13)
            sage: MR.indices_with_two_torsion()
            [3, 4]
            sage: MR.reps(3), MR.reps(4)
            (
            [-1 -1]  [-1 -2]
            [ 3  2], [ 2  3]
            )

        The corresponding matrix of order 2::

            sage: A = MR.two_torsion_matrix(MR.reps(3)); A
            [  5   2]
            [-13  -5]
            sage: A^2
            [-1  0]
            [ 0 -1]

        You can see that multiplication by ``A`` just interchanges the rational
        cusps determined by the columns of the matrix ``MR.reps(3)``::

            sage: MR.reps(3), A*MR.reps(3)
            (
            [-1 -1]  [ 1 -1]
            [ 3  2], [-2  3]
            )
        """
    def reps_with_two_torsion(self):
        """
        The coset representatives whose associated unimodular path contains a
        point fixed by a `\\Gamma_0(N)` element of order 2 (where the order is
        computed in `PSL_2(\\ZZ)`).

        OUTPUT: list of matrices

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(11)
            sage: MR.reps_with_two_torsion()
            []
            sage: MR = ManinRelations(13)
            sage: MR.reps_with_two_torsion()
            [
            [-1 -1]  [-1 -2]
            [ 3  2], [ 2  3]
            ]
            sage: B = MR.reps_with_two_torsion()[0]

        The corresponding matrix of order 2::

            sage: A = MR.two_torsion_matrix(B); A
            [  5   2]
            [-13  -5]
            sage: A^2
            [-1  0]
            [ 0 -1]

        You can see that multiplication by ``A`` just interchanges the rational
        cusps determined by the columns of the matrix ``MR.reps(3)``::

            sage: B, A*B
            (
            [-1 -1]  [ 1 -1]
            [ 3  2], [-2  3]
            )
        """
    def two_torsion_matrix(self, A):
        """
        Return the matrix of order two in `\\Gamma_0(N)` which
        corresponds to an ``A`` in ``self.reps_with_two_torsion()``.

        INPUT:

        - ``A`` -- a matrix in ``self.reps_with_two_torsion()``

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(25)
            sage: B = MR.reps_with_two_torsion()[0]

        The corresponding matrix of order 2::

            sage: A = MR.two_torsion_matrix(B); A
            [  7   2]
            [-25  -7]
            sage: A^2
            [-1  0]
            [ 0 -1]
        """
    def indices_with_three_torsion(self):
        """
        A list of indices of coset representatives whose associated unimodular
        path contains a point fixed by a `\\Gamma_0(N)` element of order 3 in
        the ideal triangle directly below that path (the order is computed in
        `PSL_2(\\ZZ)`).

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(11)
            sage: MR.indices_with_three_torsion()
            []
            sage: MR = ManinRelations(13)
            sage: MR.indices_with_three_torsion()
            [2, 5]
            sage: B = MR.reps(2); B
            [ 0 -1]
            [ 1  3]

        The corresponding matrix of order three::

            sage: A = MR.three_torsion_matrix(B); A
            [-4 -1]
            [13  3]
            sage: A^3
            [1 0]
            [0 1]

        The columns of ``B`` and the columns of ``A*B`` and ``A^2*B`` give the
        same rational cusps::

            sage: B
            [ 0 -1]
            [ 1  3]
            sage: A*B, A^2*B
            (
            [-1  1]  [ 1  0]
            [ 3 -4], [-4  1]
            )
        """
    def reps_with_three_torsion(self):
        """
        A list of coset representatives whose associated unimodular
        path contains a point fixed by a `\\Gamma_0(N)` element of
        order 3 in the ideal triangle directly below that path (the
        order is computed in `PSL_2(\\ZZ)`).

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(13)
            sage: B = MR.reps_with_three_torsion()[0]; B
            [ 0 -1]
            [ 1  3]

        The corresponding matrix of order three::

            sage: A = MR.three_torsion_matrix(B); A
            [-4 -1]
            [13  3]
            sage: A^3
            [1 0]
            [0 1]

        The columns of ``B`` and the columns of ``A*B`` and ``A^2*B``
        give the same rational cusps::

            sage: B
            [ 0 -1]
            [ 1  3]
            sage: A*B, A^2*B
            (
            [-1  1]  [ 1  0]
            [ 3 -4], [-4  1]
            )
        """
    def three_torsion_matrix(self, A):
        """
        Return the matrix of order two in `\\Gamma_0(N)` which
        corresponds to an ``A`` in ``self.reps_with_two_torsion()``.

        INPUT:

        - ``A`` -- a matrix in ``self.reps_with_two_torsion()``

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: MR = ManinRelations(37)
            sage: B = MR.reps_with_three_torsion()[0]

        The corresponding matrix of order 3::

            sage: A = MR.three_torsion_matrix(B); A
            [-11  -3]
            [ 37  10]
            sage: A^3
            [1 0]
            [0 1]
        """
    def form_list_of_cusps(self):
        """
        Return the intersection of a fundamental domain for `\\Gamma_0(N)` with
        the real axis.

        The construction of this fundamental domain follows the arguments of
        [PS2011]_ Section 2.  The boundary of this fundamental domain consists
        entirely of unimodular paths when `\\Gamma_0(N)` has no elements of
        order 3.  (See [PS2011]_ Section 2.5 for the case when there are
        elements of order 3.)

        OUTPUT:

        A sorted list of rational numbers marking the intersection of a
        fundamental domain for `\\Gamma_0(N)` with the real axis.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.form_list_of_cusps()
            [-1, -2/3, -1/2, -1/3, 0]
            sage: A = ManinRelations(13)
            sage: A.form_list_of_cusps()
            [-1, -2/3, -1/2, -1/3, 0]
            sage: A = ManinRelations(101)
            sage: A.form_list_of_cusps()
            [-1, -6/7, -5/6, -4/5, -7/9, -3/4, -11/15, -8/11, -5/7, -7/10,
            -9/13, -2/3, -5/8, -13/21, -8/13, -3/5, -7/12, -11/19, -4/7, -1/2,
            -4/9, -3/7, -5/12, -7/17, -2/5, -3/8, -4/11, -1/3, -2/7, -3/11,
            -1/4, -2/9, -1/5, -1/6, 0]
        """
    def is_unimodular_path(self, r1, r2) -> bool:
        """
        Determine whether two (non-infinite) cusps are connected by a
        unimodular path.

        INPUT:

        - ``r1``, ``r2`` -- rational numbers

        OUTPUT:

        A boolean expressing whether or not a unimodular path connects ``r1``
        to ``r2``.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.is_unimodular_path(0,1/3)
            True
            sage: A.is_unimodular_path(1/3,0)
            True
            sage: A.is_unimodular_path(0,2/3)
            False
            sage: A.is_unimodular_path(2/3,0)
            False
        """
    def unimod_to_matrices(self, r1, r2):
        """
        Return the two matrices whose associated unimodular paths connect
        ``r1`` and ``r2`` and ``r2`` and ``r1``, respectively.

        INPUT:

        - ``r1``, ``r2`` -- rational numbers (that are assumed to be connected
          by a unimodular path)

        OUTPUT: a pair of `2 \\times 2` matrices of determinant 1

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: A.unimod_to_matrices(0,1/3)
            (
            [ 0  1]  [1 0]
            [-1  3], [3 1]
            )
        """
    def fd_boundary(self, C):
        """
        Find matrices whose associated unimodular paths give the
        boundary of a fundamental domain.

        Here the fundamental domain is for `\\Gamma_0(N)`.  (In the
        case when `\\Gamma_0(N)` has elements of order three the shape
        cut out by these unimodular matrices is a little smaller than
        a fundamental domain.  See Section 2.5 of [PS2011]_.)

        INPUT:

        - ``C`` -- list of rational numbers coming from
          ``self.form_list_of_cusps()``

        OUTPUT:

        A list of `2 \\times 2` integer matrices of determinant 1 whose associated
        unimodular paths give the boundary of a fundamental domain for
        `\\Gamma_0(N)` (or nearly so in the case of 3-torsion).

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.fund_domain import ManinRelations
            sage: A = ManinRelations(11)
            sage: C = A.form_list_of_cusps(); C
            [-1, -2/3, -1/2, -1/3, 0]
            sage: A.fd_boundary(C)
            [
            [1 0]  [ 1  1]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -1]
            [0 1], [-1  0], [ 1  3], [ 3  2], [ 2  3], [ 3  1]
            ]
            sage: A = ManinRelations(13)
            sage: C = A.form_list_of_cusps(); C
            [-1, -2/3, -1/2, -1/3, 0]
            sage: A.fd_boundary(C)
            [
            [1 0]  [ 1  1]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -1]
            [0 1], [-1  0], [ 1  3], [ 3  2], [ 2  3], [ 3  1]
            ]
            sage: A = ManinRelations(101)
            sage: C = A.form_list_of_cusps(); C
            [-1, -6/7, -5/6, -4/5, -7/9, -3/4, -11/15, -8/11, -5/7, -7/10,
            -9/13, -2/3, -5/8, -13/21, -8/13, -3/5, -7/12, -11/19, -4/7, -1/2,
            -4/9, -3/7, -5/12, -7/17, -2/5, -3/8, -4/11, -1/3, -2/7, -3/11,
            -1/4, -2/9, -1/5, -1/6, 0]
            sage: A.fd_boundary(C)
            [
            [1 0]  [ 1  1]  [ 0 -1]  [-1 -1]  [-1 -2]  [-2 -1]  [-1 -3]  [-3 -2]
            [0 1], [-1  0], [ 1  6], [ 6  5], [ 5  9], [ 9  4], [ 4 11], [11  7],
            <BLANKLINE>
            [-2 -1]  [-1 -4]  [-4 -3]  [-3 -2]  [-2 -7]  [-7 -5]  [-5 -3]  [-3 -4]
            [ 7  3], [ 3 11], [11  8], [ 8  5], [ 5 17], [17 12], [12  7], [ 7  9],
            <BLANKLINE>
            [-4 -1]  [-1 -4]  [ -4 -11]  [-11  -7]  [-7 -3]  [-3 -8]  [ -8 -13]
            [ 9  2], [ 2  7], [  7  19], [ 19  12], [12  5], [ 5 13], [ 13  21],
            <BLANKLINE>
            [-13  -5]  [-5 -2]  [-2 -9]  [-9 -7]  [-7 -5]  [-5 -8]  [ -8 -11]
            [ 21   8], [ 8  3], [ 3 13], [13 10], [10  7], [ 7 11], [ 11  15],
            <BLANKLINE>
            [-11  -3]  [-3 -7]  [-7 -4]  [-4 -5]  [-5 -6]  [-6 -1]
            [ 15   4], [ 4  9], [ 9  5], [ 5  6], [ 6  7], [ 7  1]
            ]
        """
    @cached_method
    def prep_hecke_on_gen(self, l, gen, modulus=None):
        """
        This function does some precomputations needed to compute `T_l`.

        In particular, if `\\phi` is a modular symbol and `D_m` is the divisor
        associated to the generator ``gen``, to compute `(\\phi|T_{l})(D_m)` one
        needs to compute `\\phi(\\gamma_a D_m)|\\gamma_a` where `\\gamma_a` runs
        through the `l+1` matrices defining `T_l`.  One
        then takes `\\gamma_a D_m` and writes it as a sum of unimodular
        divisors.  For each such unimodular divisor, say `[M]` where `M` is a
        `SL_2` matrix, we then write `M=\\gamma h` where `\\gamma` is in
        `\\Gamma_0(N)` and `h` is one of our chosen coset representatives.  Then
        `\\phi([M]) = \\phi([h]) | \\gamma^{-1}`.  Thus, one has

        .. MATH::

            (\\phi | \\gamma_a)(D_m) = \\sum_h \\sum_j \\phi([h]) | \\gamma_{hj}^{-1} \\cdot \\gamma_a

        as `h` runs over all coset representatives and `j` simply runs over
        however many times `M_h` appears in the above computation.

        Finally, the output of this function is a dictionary ``D``
        whose keys are the coset representatives in ``self.reps()``
        where each value is a list of matrices, and the entries of
        ``D`` satisfy:

        .. MATH::

            D[h][j] = \\gamma_{hj} * \\gamma_a

        INPUT:

        - ``l`` -- a prime
        - ``gen`` -- a generator

        OUTPUT:

        A list of lists (see above).

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: M = phi.parent().source()
            sage: w = M.prep_hecke_on_gen(2, M.gens()[0])
            sage: one = Matrix(ZZ,2,2,1)
            sage: one.set_immutable()
            sage: w[one]
            [[1 0]
            [0 2], [1 1]
            [0 2], [2 0]
            [0 1]]
        """
    @cached_method
    def prep_hecke_on_gen_list(self, l, gen, modulus=None):
        """
        Return the precomputation to compute `T_l` in a way that
        speeds up the Hecke calculation.

        Namely, returns a list of the form [h,A].

        INPUT:

        - ``l`` -- a prime
        - ``gen`` -- a generator

        OUTPUT:

        A list of lists (see above).

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: M = phi.parent().source()
            sage: len(M.prep_hecke_on_gen_list(2, M.gens()[0]))
            4
        """

def basic_hecke_matrix(a, l):
    """
    Return the `2 \\times 2` matrix with entries ``[1, a, 0, l]`` if ``a<l``
    and ``[l, 0, 0, 1]`` if ``a>=l``.

    INPUT:

    - ``a`` -- integer or Infinity
    - ``l`` -- a prime

    OUTPUT: a `2 \\times 2` matrix of determinant l

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.fund_domain import basic_hecke_matrix
        sage: basic_hecke_matrix(0, 7)
        [1 0]
        [0 7]
        sage: basic_hecke_matrix(5, 7)
        [1 5]
        [0 7]
        sage: basic_hecke_matrix(7, 7)
        [7 0]
        [0 1]
        sage: basic_hecke_matrix(19, 7)
        [7 0]
        [0 1]
        sage: basic_hecke_matrix(infinity, 7)
        [7 0]
        [0 1]
    """
