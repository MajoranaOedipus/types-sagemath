from _typeshed import Incomplete
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations, from_cycles as from_cycles
from sage.combinat.specht_module import SymmetricGroupRepresentation as SymmetricGroupRepresentation_mixin
from sage.combinat.tableau import StandardTableaux as StandardTableaux, Tableau as Tableau
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.sets.finite_enumerated_set import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def SymmetricGroupRepresentation(partition, implementation: str = 'specht', ring=None, cache_matrices: bool = True):
    '''
    The irreducible representation of the symmetric group corresponding to
    ``partition``.

    INPUT:

    - ``partition`` -- a partition of a positive integer

    - ``implementation`` -- string (default: ``\'specht\'``); one of:

      * ``\'seminormal\'`` -- for Young\'s seminormal representation
      * ``\'orthogonal\'`` -- for Young\'s orthogonal representation
      * ``\'specht\'`` -- for Specht\'s representation
      * ``\'unitary\'`` -- for the unitary representation

    - ``ring`` -- the ring over which the representation is defined

    - ``cache_matrices`` -- boolean (default: ``True``); if ``True``, then any
      representation matrices that are computed are cached

    EXAMPLES:

    Young\'s orthogonal representation: the matrices are orthogonal.

    ::

        sage: orth = SymmetricGroupRepresentation([2,1], "orthogonal"); orth            # needs sage.symbolic
        Orthogonal representation of the symmetric group corresponding to [2, 1]
        sage: all(a*a.transpose() == a.parent().identity_matrix() for a in orth)        # needs sage.symbolic
        True

    ::

        sage: # needs sage.symbolic
        sage: orth = SymmetricGroupRepresentation([3,2], "orthogonal"); orth
        Orthogonal representation of the symmetric group corresponding to [3, 2]
        sage: orth([2,1,3,4,5])
        [ 1  0  0  0  0]
        [ 0  1  0  0  0]
        [ 0  0 -1  0  0]
        [ 0  0  0  1  0]
        [ 0  0  0  0 -1]
        sage: orth([1,3,2,4,5])
        [          1           0           0           0           0]
        [          0        -1/2 1/2*sqrt(3)           0           0]
        [          0 1/2*sqrt(3)         1/2           0           0]
        [          0           0           0        -1/2 1/2*sqrt(3)]
        [          0           0           0 1/2*sqrt(3)         1/2]
        sage: orth([1,2,4,3,5])
        [       -1/3 2/3*sqrt(2)           0           0           0]
        [2/3*sqrt(2)         1/3           0           0           0]
        [          0           0           1           0           0]
        [          0           0           0           1           0]
        [          0           0           0           0          -1]

    The Specht representation::

        sage: spc = SymmetricGroupRepresentation([3,2], "specht")
        sage: spc.scalar_product_matrix(Permutation([1,2,3,4,5]))
        [ 1  0  0  0  0]
        [ 0 -1  0  0  0]
        [ 0  0  1  0  0]
        [ 0  0  0  1  0]
        [-1  0  0  0 -1]
        sage: spc.scalar_product_matrix(Permutation([5,4,3,2,1]))
        [ 1 -1  0  1  0]
        [ 0  0  1  0 -1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [-1  0  0  0 -1]
        sage: spc([5,4,3,2,1])
        [ 1 -1  0  1  0]
        [ 0  0 -1  0  1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [ 0  1  0 -1  1]
        sage: spc.verify_representation()
        True

    The unitary representation::

        sage: unitary = SymmetricGroupRepresentation([3,1], "unitary"); unitary
        Unitary representation of the symmetric group corresponding to [3, 1]
        sage: unitary_GF49 = SymmetricGroupRepresentation([3,1], "unitary", ring=GF(7**2)); unitary_GF49
        Unitary representation of the symmetric group corresponding to [3, 1]
        sage: unitary_GF49([2,1,3,4])
        [6 0 0]
        [0 1 0]
        [0 0 1]
        sage: unitary_GF49([3,2,1,4])
        [       4 2*z2 + 3        0]
        [5*z2 + 5        3        0]
        [       0        0        1]
        sage: unitary_GF49.verify_representation()
        True

    By default, any representation matrices that are computed are cached::

        sage: spc = SymmetricGroupRepresentation([3,2], "specht")
        sage: spc([5,4,3,2,1])
        [ 1 -1  0  1  0]
        [ 0  0 -1  0  1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [ 0  1  0 -1  1]
        sage: spc._cache__representation_matrix
        {(([5, 4, 3, 2, 1],), ()): [ 1 -1  0  1  0]
        [ 0  0 -1  0  1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [ 0  1  0 -1  1]}

    This can be turned off with the keyword ``cache_matrices``::

        sage: spc = SymmetricGroupRepresentation([3,2], "specht", cache_matrices=False)
        sage: spc([5,4,3,2,1])
        [ 1 -1  0  1  0]
        [ 0  0 -1  0  1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [ 0  1  0 -1  1]
        sage: hasattr(spc, \'_cache__representation_matrix\')
        False

    .. NOTE::

        The implementation is based on the paper [Las]_.

    REFERENCES:

    .. [Las] Alain Lascoux, \'Young representations of the symmetric group.\'
       http://phalanstere.univ-mlv.fr/~al/ARTICLES/ProcCrac.ps.gz

    AUTHORS:

    - Franco Saliola (2009-04-23)
    '''
def SymmetricGroupRepresentations(n, implementation: str = 'specht', ring=None, cache_matrices: bool = True):
    '''
    Irreducible representations of the symmetric group.

    INPUT:

    - ``n`` -- positive integer

    - ``implementation`` -- string (default: ``\'specht\'``); one of:

      * ``\'seminormal\'`` -- for Young\'s seminormal representation
      * ``\'orthogonal\'`` -- for Young\'s orthogonal representation
      * ``\'specht\'`` -- for Specht\'s representation
      * ``\'unitary\'`` -- for the unitary representation

    - ``ring`` -- the ring over which the representation is defined

    - ``cache_matrices`` -- boolean (default: ``True``); if ``True``, then any
      representation matrices that are computed are cached

    EXAMPLES:

    Young\'s orthogonal representation: the matrices are orthogonal.

    ::

        sage: orth = SymmetricGroupRepresentations(3, "orthogonal"); orth               # needs sage.symbolic
        Orthogonal representations of the symmetric group of order 3! over Symbolic Ring
        sage: orth.list()                                                               # needs sage.symbolic
        [Orthogonal representation of the symmetric group corresponding to [3],
         Orthogonal representation of the symmetric group corresponding to [2, 1],
         Orthogonal representation of the symmetric group corresponding to [1, 1, 1]]
        sage: orth([2,1])([1,2,3])                                                      # needs sage.symbolic
        [1 0]
        [0 1]

    Young\'s seminormal representation.

    ::

        sage: snorm = SymmetricGroupRepresentations(3, "seminormal"); snorm
        Seminormal representations of the symmetric group of order 3! over Rational Field
        sage: sgn = snorm([1,1,1]); sgn
        Seminormal representation of the symmetric group corresponding to [1, 1, 1]
        sage: list(map(sgn, Permutations(3)))
        [[1], [-1], [-1], [1], [1], [-1]]

    The Specht Representation.

    ::

        sage: spc = SymmetricGroupRepresentations(5, "specht"); spc
        Specht representations of the symmetric group of order 5! over Integer Ring
        sage: spc([3,2])([5,4,3,2,1])
        [ 1 -1  0  1  0]
        [ 0  0 -1  0  1]
        [ 0  0  0 -1  1]
        [ 0  1 -1 -1  1]
        [ 0  1  0 -1  1]

    The unitary representation.

    ::

        sage: unitary = SymmetricGroupRepresentations(3, "unitary"); unitary
        Unitary representations of the symmetric group of order 3! over Symbolic Ring
        sage: unitary_GF49 = SymmetricGroupRepresentations(4, "unitary", ring=GF(7**2)); unitary_GF49
        Unitary representations of the symmetric group of order 4! over Finite Field in z2 of size 7^2
        sage: unitary_GF49([3,1])([2,1,3,4])
        [6 0 0]
        [0 1 0]
        [0 0 1]
        sage: unitary_GF49([3,1])([3,2,1,4])
        [       4 2*z2 + 3        0]
        [5*z2 + 5        3        0]
        [       0        0        1]

    .. NOTE::

        The implementation is based on the paper [Las]_.

    AUTHORS:

    - Franco Saliola (2009-04-23)
    '''

class SymmetricGroupRepresentation_generic_class(Element):
    """
    Generic methods for a representation of the symmetric group.
    """
    representation_matrix: Incomplete
    def __init__(self, parent, partition) -> None:
        """
        An irreducible representation of the symmetric group corresponding
        to ``partition``.

        For more information, see the documentation for
        :func:`SymmetricGroupRepresentation`.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([3])
            sage: spc([3,2,1])
            [1]
            sage: spc == loads(dumps(spc))
            True

            sage: spc = SymmetricGroupRepresentation([3], cache_matrices=False)
            sage: spc([3,2,1])
            [1]
            sage: spc == loads(dumps(spc))
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: spc1 = SymmetricGroupRepresentation([3], cache_matrices=True)
            sage: hash(spc1) ^^ hash((3,)) == hash(ZZ)
            True
        """
    def __eq__(self, other):
        """
        Test for equality.

        EXAMPLES::

            sage: spc1 = SymmetricGroupRepresentation([3], cache_matrices=True)
            sage: spc1([3,1,2])
            [1]
            sage: spc2 = loads(dumps(spc1))
            sage: spc1 == spc2
            True

        ::

            sage: spc3 = SymmetricGroupRepresentation([3], cache_matrices=False)
            sage: spc3([3,1,2])
            [1]
            sage: spc4 = loads(dumps(spc3))
            sage: spc3 == spc4
            True
            sage: spc1 == spc3
            True

        TESTS:

        The following tests against some bug that was fixed in :issue:`8611`::

            sage: spc = SymmetricGroupRepresentation([3])
            sage: spc.important_info = 'Sage rules'
            sage: spc == SymmetricGroupRepresentation([3])
            True
        """
    def __ne__(self, other):
        """
        Test for inequality.

        EXAMPLES::

            sage: spc1 = SymmetricGroupRepresentation([3], cache_matrices=True)
            sage: loads(dumps(spc1)) != spc1
            False
            sage: spc2 = SymmetricGroupRepresentation([2,1])
            sage: spc1 != spc2
            True
            sage: spc3 = SymmetricGroupRepresentation([3], cache_matrices=False)
            sage: spc1 != spc3
            False
        """
    def __call__(self, permutation):
        """
        Return the image of ``permutation`` in the representation.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([2,1])
            sage: spc([1,3,2])
            [ 1  0]
            [ 1 -1]
        """
    def __iter__(self):
        """
        Iterate over the matrices representing the elements of the
        symmetric group.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([1,1,1])
            sage: list(spc)
            [[1], [-1], [-1], [1], [1], [-1]]
        """
    def verify_representation(self):
        """
        Verify the representation.

        This tests that the images of the simple transpositions are
        involutions and tests that the braid relations hold.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([1,1,1])
            sage: spc.verify_representation()
            True
            sage: spc = SymmetricGroupRepresentation([4,2,1])
            sage: spc.verify_representation()
            True
        """
    def to_character(self):
        """
        Return the character of the representation.

        EXAMPLES:

        The trivial character::

            sage: rho = SymmetricGroupRepresentation([3])
            sage: chi = rho.to_character(); chi
            Character of Symmetric group of order 3! as a permutation group
            sage: chi.values()
            [1, 1, 1]
            sage: all(chi(g) == 1 for g in SymmetricGroup(3))
            True

        The sign character::

            sage: rho = SymmetricGroupRepresentation([1,1,1])
            sage: chi = rho.to_character(); chi
            Character of Symmetric group of order 3! as a permutation group
            sage: chi.values()
            [1, -1, 1]
            sage: all(chi(g) == g.sign() for g in SymmetricGroup(3))
            True

        The defining representation::

            sage: triv = SymmetricGroupRepresentation([4])
            sage: hook = SymmetricGroupRepresentation([3,1])
            sage: def_rep = lambda p : triv(p).block_sum(hook(p)).trace()
            sage: list(map(def_rep, Permutations(4)))
            [4, 2, 2, 1, 1, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0]
            sage: [p.to_matrix().trace() for p in Permutations(4)]
            [4, 2, 2, 1, 1, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0]
        """

class SymmetricGroupRepresentations_class(UniqueRepresentation, Parent):
    """
    Generic methods for the CombinatorialClass of irreducible
    representations of the symmetric group.
    """
    def __init__(self, n, ring=None, cache_matrices: bool = True) -> None:
        '''
        Irreducible representations of the symmetric group.

        See the documentation for :func:`SymmetricGroupRepresentations`
        for more information.

        EXAMPLES::

            sage: snorm = SymmetricGroupRepresentations(3, "seminormal")
            sage: snorm == loads(dumps(snorm))
            True
        '''
    def cardinality(self):
        '''
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: sp = SymmetricGroupRepresentations(4, "specht")
            sage: sp.cardinality()
            5
        '''
    def __iter__(self):
        '''
        Iterate through all the irreducible representations of the
        symmetric group.

        EXAMPLES::

            sage: orth = SymmetricGroupRepresentations(3, "orthogonal")                 # needs sage.symbolic
            sage: for x in orth: print(x)                                               # needs sage.symbolic
            Orthogonal representation of the symmetric group corresponding to [3]
            Orthogonal representation of the symmetric group corresponding to [2, 1]
            Orthogonal representation of the symmetric group corresponding to [1, 1, 1]
        '''

class YoungRepresentation_generic(SymmetricGroupRepresentation_generic_class):
    """
    Generic methods for Young's representations of the symmetric group.
    """
    @cached_method
    def representation_matrix_for_simple_transposition(self, i):
        '''
        Return the matrix representing the transposition that swaps ``i`` and
        ``i+1``.

        EXAMPLES::

            sage: orth = SymmetricGroupRepresentation([2,1], "orthogonal")              # needs sage.symbolic
            sage: orth.representation_matrix_for_simple_transposition(1)                # needs sage.symbolic
            [ 1  0]
            [ 0 -1]
            sage: orth.representation_matrix_for_simple_transposition(2)                # needs sage.symbolic
            [       -1/2 1/2*sqrt(3)]
            [1/2*sqrt(3)         1/2]

            sage: norm = SymmetricGroupRepresentation([2,1], "seminormal")
            sage: norm.representation_matrix_for_simple_transposition(1)
            [ 1  0]
            [ 0 -1]
            sage: norm.representation_matrix_for_simple_transposition(2)
            [-1/2  3/2]
            [ 1/2  1/2]
        '''
    @cached_method
    def representation_matrix(self, permutation):
        '''
        Return the matrix representing ``permutation``.

        EXAMPLES::

            sage: orth = SymmetricGroupRepresentation([2,1], "orthogonal")              # needs sage.symbolic
            sage: orth.representation_matrix(Permutation([2,1,3]))                      # needs sage.symbolic
            [ 1  0]
            [ 0 -1]
            sage: orth.representation_matrix(Permutation([1,3,2]))                      # needs sage.symbolic
            [       -1/2 1/2*sqrt(3)]
            [1/2*sqrt(3)         1/2]

        ::

            sage: norm = SymmetricGroupRepresentation([2,1], "seminormal")
            sage: p = PermutationGroupElement([2,1,3])
            sage: norm.representation_matrix(p)
            [ 1  0]
            [ 0 -1]
            sage: p = PermutationGroupElement([1,3,2])
            sage: norm.representation_matrix(p)
            [-1/2  3/2]
            [ 1/2  1/2]
        '''

class YoungRepresentation_Seminormal(YoungRepresentation_generic): ...

class YoungRepresentations_Seminormal(SymmetricGroupRepresentations_class):
    Element = YoungRepresentation_Seminormal

class YoungRepresentation_Orthogonal(YoungRepresentation_generic): ...

class YoungRepresentations_Orthogonal(SymmetricGroupRepresentations_class):
    Element = YoungRepresentation_Orthogonal

class SpechtRepresentation(SymmetricGroupRepresentation_generic_class):
    @cached_method
    def scalar_product(self, u, v):
        """
        Return ``0`` if ``u+v`` is not a permutation, and the signature of the
        permutation otherwise.

        This is the scalar product of a vertex ``u`` of the underlying
        Yang-Baxter graph with the vertex ``v`` in the 'dual' Yang-Baxter
        graph.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([3,2], 'specht')
            sage: spc.scalar_product((1,0,2,1,0),(0,3,0,3,0))
            -1
            sage: spc.scalar_product((1,0,2,1,0),(3,0,0,3,0))
            0
        """
    def scalar_product_matrix(self, permutation=None):
        """
        Return the scalar product matrix corresponding to ``permutation``.

        The entries are given by the scalar products of ``u`` and
        ``permutation.action(v)``, where ``u`` is a vertex in the underlying
        Yang-Baxter graph and ``v`` is a vertex in the dual graph.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([3,1], 'specht')
            sage: spc.scalar_product_matrix()
            [ 1  0  0]
            [ 0 -1  0]
            [ 0  0  1]
        """
    @cached_method
    def representation_matrix(self, permutation):
        """
        Return the matrix representing the ``permutation`` in this
        irreducible representation.

        .. NOTE::

            This method caches the results.

        EXAMPLES::

            sage: spc = SymmetricGroupRepresentation([3,1], 'specht')
            sage: spc.representation_matrix(Permutation([2,1,3,4]))
            [ 0 -1  0]
            [-1  0  0]
            [ 0  0  1]
            sage: spc.representation_matrix(Permutation([3,2,1,4]))
            [0 0 1]
            [0 1 0]
            [1 0 0]
        """

class SpechtRepresentations(SymmetricGroupRepresentations_class):
    Element = SpechtRepresentation

class UnitaryRepresentation(SymmetricGroupRepresentation_generic_class):
    """
    A unitary representation of the symmetric group.

    In characteristic zero, this is the same as the orthogonal representation since
    they are defined over the reals. In positive characteristic, we are able to construct
    representations when the field is finite, has square order, and the characteristic does not divide
    the order of the group. In this case, we construct the representation by first
    constructing the orthogonal representation `\\rho` and then taking the extended
    Cholesky decomposition of the unique solution `U` to the equation
    `\\rho(g)^T U \\rho(g) = U` for all `g` in `G`.
    """
    def __init__(self, parent, partition) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: U = SymmetricGroupRepresentation([2,1], "unitary")
            sage: TestSuite(U).run()
            sage: U = SymmetricGroupRepresentation([2,1], "unitary", GF(7))
            Traceback (most recent call last):
            ...
            ValueError: the base ring must be a finite field of square order
            sage: U = SymmetricGroupRepresentation([2,1], "unitary", GF(7**2))
            sage: TestSuite(U).run()
        '''
    @cached_method
    def representation_matrix(self, permutation):
        """
        Return the matrix representing the ``permutation`` in this
        irreducible representation.

        .. NOTE::

            This method caches the results.

        EXAMPLES::

            sage: unitary_specht = SymmetricGroupRepresentation([3,1], 'unitary', ring=GF(7**2))
            sage: unitary_specht.representation_matrix(Permutation([2,1,3,4]))
            [6 0 0]
            [0 1 0]
            [0 0 1]
            sage: unitary_specht.representation_matrix(Permutation([3,2,1,4]))
            [       4 2*z2 + 3        0]
            [5*z2 + 5        3        0]
            [       0        0        1]
            sage: all(A * A.H == 1 for A in [unitary_specht.representation_matrix(g)
            ....:                            for g in Permutations(4)])
            True
        """

class UnitaryRepresentations(SymmetricGroupRepresentations_class):
    Element = UnitaryRepresentation

def partition_to_vector_of_contents(partition, reverse: bool = False):
    '''
    Return the "vector of contents" associated to ``partition``.

    EXAMPLES::

        sage: from sage.combinat.symmetric_group_representations import partition_to_vector_of_contents
        sage: partition_to_vector_of_contents([3,2])
        (0, 1, 2, -1, 0)
    '''

class GarsiaProcesiModule(UniqueRepresentation, QuotientRing_generic, SymmetricGroupRepresentation_mixin):
    """
    A Garsia-Procesi module.

    Let `\\lambda` be a partition of `n` and `R` be a commutative
    ring. The *Garsia-Procesi module* is defined by `R_{\\lambda}
    := R[x_1, \\ldots, x_n] / I_{\\lambda}`, where

    .. MATH::

        I_{\\lambda} := \\langle e_r(x_{i_1}, \\ldots, x_{i_k}) \\mid
        \\{i_1, \\ldots, i_k\\} \\subseteq [n] \\text{ and }
        k \\geq r > k - d_k(\\lambda) \\rangle,

    with `e_r` being the `r`-the elementary symmetric function and
    `d_k(\\lambda) = \\lambda'_n + \\cdots + \\lambda'_{n+1-k}`, is the
    *Tanisaki ideal*.

    If we consider `R = \\QQ`, then the Garsia-Procesi module has the
    following interpretation. Let `\\mathcal{F}_n = GL_n / B` denote
    the (complex type A) flag variety. Consider the Springer fiber
    `F_{\\lambda} \\subseteq \\mathcal{F}_n` associated to a nilpotent
    matrix with Jordan blocks sizes `\\lambda`. Springer showed that
    the cohomology ring `H^*(F_{\\lambda})` admits a graded `S_n`-action
    that agrees with the induced representation of the sign representation
    of the Young subgroup `S_{\\lambda}`. From work of De Concini
    and Procesi, this `S_n`-representation is isomorphic to `R_{\\lambda}`.
    Moreover, the graded Frobenius image is known to be a modified
    Hall-Littlewood polynomial.

    EXAMPLES::

        sage: SGA = SymmetricGroupAlgebra(QQ, 7)
        sage: GP421 = SGA.garsia_procesi_module([4, 2, 1])
        sage: GP421.dimension()
        105
        sage: v = GP421.an_element(); v
        -gp1 - gp2 - gp3 - gp4 - gp5 - gp6
        sage: SGA.an_element() * v
        -6*gp1 - 6*gp2 - 6*gp3 - 6*gp4 - 6*gp5 - 5*gp6

    We verify the result is a modified Hall-Littlewood polynomial by using
    the `Q'` Hall-Littlewood polynomials, replacing `q \\mapsto q^{-1}` and
    multiplying by the smallest power of `q` so the coefficients are again
    polynomials::

        sage: GP421.graded_frobenius_image()
        q^4*s[4, 2, 1] + q^3*s[4, 3] + q^3*s[5, 1, 1] + (q^3+q^2)*s[5, 2]
         + (q^2+q)*s[6, 1] + s[7]
        sage: R.<q> = QQ[]
        sage: Sym = SymmetricFunctions(R)
        sage: s = Sym.s()
        sage: Qp = Sym.hall_littlewood(q).Qp()
        sage: mHL = s(Qp[4,2,1]); mHL
        s[4, 2, 1] + q*s[4, 3] + q*s[5, 1, 1] + (q^2+q)*s[5, 2]
         + (q^3+q^2)*s[6, 1] + q^4*s[7]
        sage: mHL.map_coefficients(lambda c: R(q^4*c(q^-1)))
        q^4*s[4, 2, 1] + q^3*s[4, 3] + q^3*s[5, 1, 1] + (q^3+q^2)*s[5, 2]
         + (q^2+q)*s[6, 1] + s[7]

    We show that the maximal degree component corresponds to the Yamanouchi
    words of content `\\lambda`::

        sage: B = GP421.graded_decomposition(4).basis()
        sage: top_deg = [Word([i+1 for i in b.lift().lift().exponents()[0]]) for b in B]
        sage: yamanouchi = [P.to_packed_word() for P in OrderedSetPartitions(range(7), [4, 2, 1])
        ....:               if P.to_packed_word().reversal().is_yamanouchi()]
        sage: set(top_deg) == set(yamanouchi)
        True
    """
    @staticmethod
    def __classcall_private__(cls, SGA, shape):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: from sage.combinat.symmetric_group_representations import GarsiaProcesiModule
            sage: GP1 = GarsiaProcesiModule(SGA, [2, 2, 1])
            sage: GP2 = GarsiaProcesiModule(SGA, Partitions(5)([2, 2, 1]))
            sage: GP1 is GP2
            True
            sage: GarsiaProcesiModule(SGA, [3])
            Traceback (most recent call last):
            ...
            ValueError: [3] is not a partition of 5
        """
    def __init__(self, SGA, shape) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: GP = SGA.garsia_procesi_module([2, 2])
            sage: TestSuite(GP).run()

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: GP = SGA.garsia_procesi_module([3, 1, 1])
            sage: TestSuite(GP).run()
        """
    @cached_method
    def get_order(self):
        """
        Return the order of the elements in the basis.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: GP = SGA.garsia_procesi_module([2, 2])
            sage: GP.get_order()
            (0, 1, 2, 3, 4, 5)
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: GP = SGA.garsia_procesi_module([2, 2])
            sage: GP.basis()
            Family (gp2*gp3, gp1*gp3, gp3, gp2, gp1, 1)
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the basis element `1`.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 4)
            sage: GP = SGA.garsia_procesi_module([2, 2])
            sage: GP.one_basis()
            5
        """
    @cached_method
    def dimension(self):
        """
        Return the dimension of ``self``.

        The graded Frobenius character of the Garsia-Procesi module
        `R_{\\lambda}` is given by the modified Hall-Littlewood polynomial
        `\\widetilde{H}_{\\lambda'}(x; q)`.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.s()
            sage: Qp = Sym.hall_littlewood(1).Qp()
            sage: for la in Partitions(5):
            ....:     print(SGA.garsia_procesi_module(la).dimension(),
            ....:           sum(c * StandardTableaux(la).cardinality()
            ....:               for la, c in s(Qp[la])))
            1 1
            5 5
            10 10
            20 20
            30 30
            60 60
            120 120
        """
    @cached_method
    def graded_frobenius_image(self):
        """
        Return the graded Frobenius image of ``self``.

        The graded Frobenius image is the sum of the :meth:`frobenius_image`
        of each graded component, which is known to result in the modified
        Hall-Littlewood polynomial `\\widetilde{H}_{\\lambda}(x; q)`.

        EXAMPLES:

        We verify that the result is the modified Hall-Littlewood polynomial
        for `n = 5`::

            sage: R.<q> = QQ[]
            sage: Sym = SymmetricFunctions(R)
            sage: s = Sym.s()
            sage: Qp = Sym.hall_littlewood(q).Qp()
            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: for la in Partitions(5):
            ....:     f = SGA.garsia_procesi_module(la).graded_frobenius_image()
            ....:     d = f[la].degree()
            ....:     assert f.map_coefficients(lambda c: R(c(~q)*q^d)) == s(Qp[la])
        """
    @cached_method
    def graded_character(self):
        """
        Return the graded character of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(QQ, 5)
            sage: GP = SGA.garsia_procesi_module([2, 2, 1])
            sage: gchi = GP.graded_character(); gchi
            (5*q^4 + 11*q^3 + 9*q^2 + 4*q + 1, -q^4 + q^3 + 3*q^2 + 2*q + 1,
             q^4 - q^3 + q^2 + 1, -q^4 - q^3 + q + 1, -q^4 + q^3 - q + 1,
             q^4 - q^3 - q^2 + 1, q^3 - q^2 - q + 1)
            sage: R.<q> = QQ[]
            sage: gchi == sum(q^d * D.character()
            ....:             for d, D in GP.graded_decomposition().items())
            True
        """
    def graded_decomposition(self, k=None):
        """
        Return the decomposition of ``self`` as a direct sum of
        representations given by a fixed grading.

        INPUT:

        - ``k`` -- (optional) integer; if given, return the `k`-th graded part

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: GP32 = SGA.garsia_procesi_module([3, 2])
            sage: decomp = GP32.graded_decomposition(); decomp
            {0: Subrepresentation with basis {0} of Garsia-Procesi ...,
             1: Subrepresentation with basis {0, 1, 2, 3} of Garsia-Procesi ...,
             2: Subrepresentation with basis {0, 1, 2, 3, 4} of Garsia-Procesi ...}
            sage: decomp[2] is GP32.graded_decomposition(2)
            True
            sage: GP32.graded_decomposition(10)
            Subrepresentation with basis {} of Garsia-Procesi module
             of shape [3, 2] over Finite Field of size 2
        """
    def graded_representation_matrix(self, elt, q=None):
        """
        Return the matrix corresponding to the left action of the symmetric
        group (algebra) element ``elt`` on ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(3), 3)
            sage: GP = SGA.garsia_procesi_module([1, 1, 1])
            sage: elt = SGA.an_element(); elt
            [1, 2, 3] + 2*[1, 3, 2] + [3, 1, 2]
            sage: X = GP.graded_representation_matrix(elt); X
            [  0   0   0   0   0   0]
            [  0 q^2   0   0   0   0]
            [  0 q^2   0   0   0   0]
            [  0   0   0   q   0   0]
            [  0   0   0   q   0   0]
            [  0   0   0   0   0   1]
            sage: X.parent()
            Full MatrixSpace of 6 by 6 dense matrices over
             Univariate Polynomial Ring in q over Finite Field of size 3
            sage: R.<q> = GF(3)[]
            sage: t = R.quotient([q^2+2*q+1]).gen()
            sage: GP.graded_representation_matrix(elt, t)
            [       0        0        0        0        0        0]
            [       0 qbar + 2        0        0        0        0]
            [       0 qbar + 2        0        0        0        0]
            [       0        0        0     qbar        0        0]
            [       0        0        0     qbar        0        0]
            [       0        0        0        0        0        1]
        """
    def graded_brauer_character(self):
        """
        Return the graded Brauer character of ``self``.

        EXAMPLES::

            sage: SGA = SymmetricGroupAlgebra(GF(2), 5)
            sage: GP311 = SGA.garsia_procesi_module([3, 1, 1])
            sage: GP311.graded_brauer_character()
            (6*q^3 + 9*q^2 + 4*q + 1, q + 1, q^3 - q^2 - q + 1)
        """
    class Element(QuotientRing_generic.Element):
        def to_vector(self, order=None):
            """
            Return ``self`` as a (dense) free module vector.

            EXAMPLES::

                sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
                sage: GP22 = SGA.garsia_procesi_module([2, 2])
                sage: v = GP22.an_element(); v
                -gp1 - gp2 - gp3
                sage: v.to_vector()
                (0, 0, 2, 2, 2, 0)
            """
        def monomial_coefficients(self, copy=None):
            """
            Return the monomial coefficients of ``self``.

            EXAMPLES::

                sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
                sage: GP31 = SGA.garsia_procesi_module([3, 1])
                sage: v = GP31.an_element(); v
                -gp1 - gp2 - gp3
                sage: v.monomial_coefficients()
                {0: 2, 1: 2, 2: 2, 3: 0}
            """
        def degree(self):
            """
            Return the degree of ``self``.

            EXAMPLES::

                sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
                sage: GP22 = SGA.garsia_procesi_module([2, 2])
                sage: for b in GP22.basis():
                ....:     print(b, b.degree())
                gp2*gp3 2
                gp1*gp3 2
                gp3 1
                gp2 1
                gp1 1
                1 0
                sage: v = sum(GP22.basis())
                sage: v.degree()
                2
            """
        def homogeneous_degree(self):
            """
            Return the (homogeneous) degree of ``self`` if homogeneous
            otherwise raise an error.

            EXAMPLES::

                sage: SGA = SymmetricGroupAlgebra(GF(2), 4)
                sage: GP31 = SGA.garsia_procesi_module([3, 1])
                sage: for b in GP31.basis():
                ....:     print(b, b.homogeneous_degree())
                gp3 1
                gp2 1
                gp1 1
                1 0
                sage: v = sum(GP31.basis()); v
                gp1 + gp2 + gp3 + 1
                sage: v.homogeneous_degree()
                Traceback (most recent call last):
                ...
                ValueError: element is not homogeneous

            TESTS::

                sage: SGA = SymmetricGroupAlgebra(GF(3), 4)
                sage: GP4 = SGA.garsia_procesi_module([4])
                sage: GP4.zero().homogeneous_degree()
                Traceback (most recent call last):
                ...
                ValueError: the zero element does not have a well-defined degree
            """
