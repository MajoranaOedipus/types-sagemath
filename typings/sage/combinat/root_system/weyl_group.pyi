from _typeshed import Incomplete
from sage.categories.affine_weyl_groups import AffineWeylGroups as AffineWeylGroups
from sage.categories.finite_weyl_groups import FiniteWeylGroups as FiniteWeylGroups
from sage.categories.permutation_groups import PermutationGroups as PermutationGroups
from sage.categories.weyl_groups import WeylGroups as WeylGroups
from sage.combinat.root_system.cartan_matrix import CartanMatrix as CartanMatrix
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.reflection_group_element import RealReflectionGroupElement as RealReflectionGroupElement
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap as FinitelyGeneratedMatrixGroup_gap
from sage.groups.matrix_gps.group_element_gap import MatrixGroupElement_gap as MatrixGroupElement_gap
from sage.groups.perm_gps.permgroup import PermutationGroup_generic as PermutationGroup_generic
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.constructor import Matrix as Matrix, diagonal_matrix as diagonal_matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def WeylGroup(x, prefix=None, implementation: str = 'matrix'):
    '''
    Return the Weyl group of the root system defined by the Cartan
    type (or matrix) ``ct``.

    INPUT:

    - ``x`` -- a root system or a Cartan type (or matrix)

    OPTIONAL:

    - ``prefix`` -- changes the representation of elements from matrices
      to products of simple reflections

    - ``implementation`` -- one of the following:

      * ``\'matrix\'`` -- as matrices acting on a root system
      * ``\'permutation\'`` -- as a permutation group acting on the roots

    EXAMPLES:

    The following constructions yield the same result, namely
    a weight lattice and its corresponding Weyl group::

        sage: G = WeylGroup([\'F\',4])
        sage: L = G.domain()

    or alternatively and equivalently::

        sage: L = RootSystem([\'F\',4]).ambient_space()
        sage: G = L.weyl_group()
        sage: W = WeylGroup(L)

    Either produces a weight lattice, with access to its roots and
    weights.

    ::

        sage: G = WeylGroup([\'F\',4])
        sage: G.order()
        1152
        sage: [s1,s2,s3,s4] = G.simple_reflections()
        sage: w = s1*s2*s3*s4; w
        [ 1/2  1/2  1/2  1/2]
        [-1/2  1/2  1/2 -1/2]
        [ 1/2  1/2 -1/2 -1/2]
        [ 1/2 -1/2  1/2 -1/2]
        sage: type(w) == G.element_class
        True
        sage: w.order()
        12
        sage: w.length() # length function on Weyl group
        4

    The default representation of Weyl group elements is as matrices.
    If you prefer, you may specify a prefix, in which case the
    elements are represented as products of simple reflections.

    ::

        sage: W=WeylGroup("C3",prefix=\'s\')
        sage: [s1,s2,s3]=W.simple_reflections() # lets Sage parse its own output
        sage: s2*s1*s2*s3
        s1*s2*s3*s1
        sage: s2*s1*s2*s3 == s1*s2*s3*s1
        True
        sage: (s2*s3)^2==(s3*s2)^2
        True
        sage: (s1*s2*s3*s1).matrix()
        [ 0  0 -1]
        [ 0  1  0]
        [ 1  0  0]

    ::

        sage: L = G.domain()
        sage: fw = L.fundamental_weights(); fw
        Finite family {1: (1, 1, 0, 0), 2: (2, 1, 1, 0), 3: (3/2, 1/2, 1/2, 1/2), 4: (1, 0, 0, 0)}
        sage: rho = sum(fw); rho
        (11/2, 5/2, 3/2, 1/2)
        sage: w.action(rho) # action of G on weight lattice
        (5, -1, 3, 2)

    We can also do the same for arbitrary Cartan matrices::

        sage: cm = CartanMatrix([[2,-5,0],[-2,2,-1],[0,-1,2]])
        sage: W = WeylGroup(cm)
        sage: W.gens()
        (
        [-1  5  0]  [ 1  0  0]  [ 1  0  0]
        [ 0  1  0]  [ 2 -1  1]  [ 0  1  0]
        [ 0  0  1], [ 0  0  1], [ 0  1 -1]
        )
        sage: s0,s1,s2 = W.gens()
        sage: s1*s2*s1
        [ 1  0  0]
        [ 2  0 -1]
        [ 2 -1  0]
        sage: s2*s1*s2
        [ 1  0  0]
        [ 2  0 -1]
        [ 2 -1  0]
        sage: s0*s1*s0*s2*s0
        [ 9  0 -5]
        [ 2  0 -1]
        [ 0  1 -1]

    Same Cartan matrix, but with a prefix to display using simple reflections::

        sage: W = WeylGroup(cm, prefix=\'s\')
        sage: s0,s1,s2 = W.gens()
        sage: s0*s2*s1
        s2*s0*s1
        sage: (s1*s2)^3
        1
        sage: (s0*s1)^5
        s0*s1*s0*s1*s0*s1*s0*s1*s0*s1
        sage: s0*s1*s2*s1*s2
        s2*s0*s1
        sage: s0*s1*s2*s0*s2
        s0*s1*s0

    TESTS::

        sage: TestSuite(WeylGroup(["A",3])).run()
        sage: TestSuite(WeylGroup(["A",2,1])).run() # long time

        sage: W = WeylGroup([\'A\',3,1])
        sage: s = W.simple_reflections()
        sage: w = s[0]*s[1]*s[2]
        sage: w.reduced_word()
        [0, 1, 2]
        sage: w = s[0]*s[2]
        sage: w.reduced_word()
        [2, 0]
        sage: W = groups.misc.WeylGroup([\'A\',3,1])
    '''

class WeylGroup_gens(UniqueRepresentation, FinitelyGeneratedMatrixGroup_gap):
    @staticmethod
    def __classcall__(cls, domain, prefix=None): ...
    n: Incomplete
    def __init__(self, domain, prefix) -> None:
        """
        EXAMPLES::

            sage: G = WeylGroup(['B',3])
            sage: TestSuite(G).run()
            sage: cm = CartanMatrix([[2,-5,0],[-2,2,-1],[0,-1,2]])
            sage: W = WeylGroup(cm)
            sage: TestSuite(W).run() # long time

        TESTS::

            sage: W = WeylGroup(SymmetricGroup(1))
        """
    @cached_method
    def cartan_type(self):
        """
        Return the ``CartanType`` associated to ``self``.

        EXAMPLES::

            sage: G = WeylGroup(['F',4])
            sage: G.cartan_type()
            ['F', 4]
        """
    @cached_method
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: G = WeylGroup(['F',4])
            sage: G.index_set()
            (1, 2, 3, 4)
            sage: G = WeylGroup(['A',3,1])
            sage: G.index_set()
            (0, 1, 2, 3)
        """
    def morphism_matrix(self, f): ...
    def from_morphism(self, f): ...
    @cached_method
    def simple_reflections(self):
        """
        Return the simple reflections of ``self``, as a family.

        EXAMPLES:

        There are the simple reflections for the symmetric group::

            sage: W=WeylGroup(['A',2])
            sage: s = W.simple_reflections(); s
            Finite family {1: [0 1 0]
            [1 0 0]
            [0 0 1], 2: [1 0 0]
            [0 0 1]
            [0 1 0]}

        As a special feature, for finite irreducible root systems,
        s[0] gives the reflection along the highest root::

            sage: s[0]
            [0 0 1]
            [0 1 0]
            [1 0 0]

        We now look at some further examples::

            sage: W=WeylGroup(['A',2,1])
            sage: W.simple_reflections()
            Finite family {0: [-1  1  1]
            [ 0  1  0]
            [ 0  0  1], 1: [ 1  0  0]
            [ 1 -1  1]
            [ 0  0  1], 2: [ 1  0  0]
            [ 0  1  0]
            [ 1  1 -1]}
            sage: W = WeylGroup(['F',4])
            sage: [s1,s2,s3,s4] = W.simple_reflections()
            sage: w = s1*s2*s3*s4; w
            [ 1/2  1/2  1/2  1/2]
            [-1/2  1/2  1/2 -1/2]
            [ 1/2  1/2 -1/2 -1/2]
            [ 1/2 -1/2  1/2 -1/2]
            sage: s4^2 == W.one()
            True
            sage: type(w) == W.element_class
            True
        """
    def reflections(self):
        '''
        Return the reflections of ``self``.

        The reflections of a Coxeter group `W` are the conjugates of
        the simple reflections. They are in bijection with the positive
        roots, for given a positive root, we may have the reflection in
        the hyperplane orthogonal to it. This method returns a family
        indexed by the positive roots taking values in the reflections.
        This requires ``self`` to be a finite Weyl group.

        .. NOTE::

            Prior to :issue:`20027`, the reflections were the keys
            of the family and the values were the positive roots.

        EXAMPLES::

            sage: W = WeylGroup("B2", prefix=\'s\')
            sage: refdict = W.reflections(); refdict
            Finite family {(1, -1): s1, (0, 1): s2, (1, 1): s2*s1*s2, (1, 0): s1*s2*s1}
            sage: [r+refdict[r].action(r) for r in refdict.keys()]
            [(0, 0), (0, 0), (0, 0), (0, 0)]

            sage: W = WeylGroup([\'A\',2,1], prefix=\'s\')
            sage: W.reflections()
            Lazy family (real root to reflection(i))_{i in
                        Positive real roots of type [\'A\', 2, 1]}

        TESTS::

            sage: CM = CartanMatrix([[2,-6],[-1,2]])
            sage: W = WeylGroup(CM, prefix=\'s\')
            sage: W.reflections()
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented for finite and affine Cartan types
        '''
    def character_table(self):
        '''
        Return the character table as a matrix.

        Each row is an irreducible character. For larger tables you
        may preface this with a command such as
        gap.eval("SizeScreen([120,40])") in order to widen the screen.

        EXAMPLES::

            sage: WeylGroup([\'A\',3]).character_table()
            CT1
            <BLANKLINE>
                 2  3  2  2  .  3
                 3  1  .  .  1  .
            <BLANKLINE>
                   1a 4a 2a 3a 2b
            <BLANKLINE>
            X.1     1 -1 -1  1  1
            X.2     3  1 -1  . -1
            X.3     2  .  . -1  2
            X.4     3 -1  1  . -1
            X.5     1  1  1  1  1
        '''
    @cached_method
    def one(self):
        """
        Return the unit element of the Weyl group.

        EXAMPLES::

            sage: W = WeylGroup(['A',3])
            sage: e = W.one(); e
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
            sage: type(e) == W.element_class
            True
        """
    unit = one
    def domain(self):
        """
        Return the domain of the element of ``self``, that is the
        root lattice realization on which they act.

        EXAMPLES::

            sage: G = WeylGroup(['F',4])
            sage: G.domain()
            Ambient space of the Root system of type ['F', 4]
            sage: G = WeylGroup(['A',3,1])
            sage: G.domain()
            Root space over the Rational Field of the Root system of type ['A', 3, 1]
        """
    def simple_reflection(self, i):
        """
        Return the `i`-th simple reflection.

        EXAMPLES::

            sage: G = WeylGroup(['F',4])
            sage: G.simple_reflection(1)
            [1 0 0 0]
            [0 0 1 0]
            [0 1 0 0]
            [0 0 0 1]
            sage: W=WeylGroup(['A',2,1])
            sage: W.simple_reflection(1)
            [ 1  0  0]
            [ 1 -1  1]
            [ 0  0  1]
        """
    def long_element_hardcoded(self):
        """
        Return the long Weyl group element (hardcoded data).

        Do we really want to keep it? There is a generic
        implementation which works in all cases. The hardcoded should
        have a better complexity (for large classical types), but
        there is a cache, so does this really matter?

        EXAMPLES::

            sage: types = [ ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6] ]
            sage: [WeylGroup(t).long_element().length() for t in types]
            [15, 9, 9, 12, 6, 24, 36]
            sage: all(WeylGroup(t).long_element() == WeylGroup(t).long_element_hardcoded() for t in types)  # long time (17s on sage.math, 2011)
            True
        """
    def classical(self):
        """
        If ``self`` is a Weyl group from an affine Cartan Type, this give
        the classical parabolic subgroup of ``self``.

        Caveat: we assume that 0 is a special node of the Dynkin diagram

        .. TODO:: extract parabolic subgroup method

        EXAMPLES::

            sage: G = WeylGroup(['A',3,1])
            sage: G.classical()
            Parabolic Subgroup of the Weyl Group of type ['A', 3, 1]
             (as a matrix group acting on the root space)
            sage: WeylGroup(['A',3]).classical()
            Traceback (most recent call last):
            ...
            ValueError: classical subgroup only defined for affine types
        """

class ClassicalWeylSubgroup(WeylGroup_gens):
    '''
    A class for Classical Weyl Subgroup of an affine Weyl Group.

    EXAMPLES::

        sage: G = WeylGroup(["A",3,1]).classical()
        sage: G
        Parabolic Subgroup of the Weyl Group of type [\'A\', 3, 1] (as a matrix group acting on the root space)
        sage: G.category()
        Category of finite irreducible Weyl groups
        sage: G.cardinality()
        24
        sage: G.index_set()
        (1, 2, 3)
        sage: TestSuite(G).run()

    TESTS::

        sage: from sage.combinat.root_system.weyl_group import ClassicalWeylSubgroup
        sage: H = ClassicalWeylSubgroup(RootSystem(["A", 3, 1]).root_space(), prefix=None)
        sage: H is G
        True

    Caveat: the interface is likely to change. The current main
    application is for plots.

    .. TODO::

        implement:

        - Parabolic subrootsystems
        - Parabolic subgroups with a set of nodes as argument
    '''
    @cached_method
    def cartan_type(self):
        """
        EXAMPLES::

            sage: WeylGroup(['A',3,1]).classical().cartan_type()
            ['A', 3]
            sage: WeylGroup(['A',3,1]).classical().index_set()
            (1, 2, 3)

        Note: won't be needed, once the lattice will be a parabolic sub root system
        """
    def simple_reflections(self):
        """
        EXAMPLES::

            sage: WeylGroup(['A',2,1]).classical().simple_reflections()
            Finite family {1: [ 1  0  0]
                              [ 1 -1  1]
                              [ 0  0  1],
                           2: [ 1  0  0]
                              [ 0  1  0]
                              [ 1  1 -1]}

        Note: won't be needed, once the lattice will be a parabolic sub root system
        """
    def weyl_group(self, prefix: str = 'hereditary'):
        """
        Return the Weyl group associated to the parabolic subgroup.

        EXAMPLES::

            sage: WeylGroup(['A',4,1]).classical().weyl_group()
            Weyl Group of type ['A', 4, 1] (as a matrix group acting on the root space)
            sage: WeylGroup(['C',4,1]).classical().weyl_group()
            Weyl Group of type ['C', 4, 1] (as a matrix group acting on the root space)
            sage: WeylGroup(['E',8,1]).classical().weyl_group()
            Weyl Group of type ['E', 8, 1] (as a matrix group acting on the root space)
        """

class WeylGroupElement(MatrixGroupElement_gap):
    """
    Class for a Weyl Group elements
    """
    def __init__(self, parent, g, check: bool = False) -> None:
        """
        EXAMPLES::

            sage: G = WeylGroup(['A',2])
            sage: s1 = G.simple_reflection(1)
            sage: TestSuite(s1).run()
        """
    def __hash__(self): ...
    def to_matrix(self):
        """
        Return ``self`` as a matrix.

        EXAMPLES::

            sage: G = WeylGroup(['A',2])
            sage: s1 = G.simple_reflection(1)
            sage: s1.to_matrix() == s1.matrix()
            True
        """
    def domain(self):
        """
        Return the ambient lattice associated with ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',2])
            sage: s1 = W.simple_reflection(1)
            sage: s1.domain()
            Ambient space of the Root system of type ['A', 2]
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: W = WeylGroup(['A',3])
            sage: s = W.simple_reflections()
            sage: s[1] == s[1]
            True
            sage: s[1] == s[2]
            False

        Note: this implementation of :meth:`__eq__` is not much faster
        than :meth:`__cmp__`. But it turned out to be useful for
        subclasses overriding __cmp__ with something slow for specific
        purposes.
        """
    def action(self, v):
        """
        Return the action of ``self`` on the vector `v`.

        EXAMPLES::

            sage: W = WeylGroup(['A',2])
            sage: s = W.simple_reflections()
            sage: v = W.domain()([1,0,0])
            sage: s[1].action(v)
            (0, 1, 0)

            sage: W = WeylGroup(RootSystem(['A',2]).root_lattice())
            sage: s = W.simple_reflections()
            sage: alpha = W.domain().simple_roots()
            sage: s[1].action(alpha[1])
            -alpha[1]

            sage: W=WeylGroup(['A',2,1])
            sage: alpha = W.domain().simple_roots()
            sage: s = W.simple_reflections()
            sage: s[1].action(alpha[1])
            -alpha[1]
            sage: s[1].action(alpha[0])
            alpha[0] + alpha[1]
        """
    def has_descent(self, i, positive: bool = False, side: str = 'right') -> bool:
        '''
        Test if ``self`` has a descent at position ``i``.

        An element `w` has a descent in position `i` if `w` is
        on the strict negative side of the `i`-th simple reflection
        hyperplane.

        If ``positive`` is ``True``, tests if it is on the strict
        positive side instead.

        EXAMPLES::

            sage: W = WeylGroup([\'A\',3])
            sage: s = W.simple_reflections()
            sage: [W.one().has_descent(i) for i in W.domain().index_set()]
            [False, False, False]
            sage: [s[1].has_descent(i) for i in W.domain().index_set()]
            [True, False, False]
            sage: [s[2].has_descent(i) for i in W.domain().index_set()]
            [False, True, False]
            sage: [s[3].has_descent(i) for i in W.domain().index_set()]
            [False, False, True]
            sage: [s[3].has_descent(i, True) for i in W.domain().index_set()]
            [True, True, False]
            sage: W = WeylGroup([\'A\',3,1])
            sage: s = W.simple_reflections()
            sage: [W.one().has_descent(i) for i in W.domain().index_set()]
            [False, False, False, False]
            sage: [s[0].has_descent(i) for i in W.domain().index_set()]
            [True, False, False, False]
            sage: w = s[0] * s[1]
            sage: [w.has_descent(i) for i in W.domain().index_set()]
            [False, True, False, False]
            sage: [w.has_descent(i, side = "left") for i in W.domain().index_set()]
            [True, False, False, False]
            sage: w = s[0] * s[2]
            sage: [w.has_descent(i) for i in W.domain().index_set()]
            [True, False, True, False]
            sage: [w.has_descent(i, side = "left") for i in W.domain().index_set()]
            [True, False, True, False]

            sage: W = WeylGroup([\'A\',3])
            sage: W.one().has_descent(0)
            True
            sage: W.w0.has_descent(0)
            False
        '''
    def has_left_descent(self, i) -> bool:
        """
        Test if ``self`` has a left descent at position ``i``.

        EXAMPLES::

            sage: W = WeylGroup(['A',3])
            sage: s = W.simple_reflections()
            sage: [W.one().has_left_descent(i) for i in W.domain().index_set()]
            [False, False, False]
            sage: [s[1].has_left_descent(i) for i in W.domain().index_set()]
            [True, False, False]
            sage: [s[2].has_left_descent(i) for i in W.domain().index_set()]
            [False, True, False]
            sage: [s[3].has_left_descent(i) for i in W.domain().index_set()]
            [False, False, True]
            sage: [(s[3]*s[2]).has_left_descent(i) for i in W.domain().index_set()]
            [False, False, True]
        """
    def has_right_descent(self, i) -> bool:
        """
        Test if ``self`` has a right descent at position ``i``.

        EXAMPLES::

            sage: W = WeylGroup(['A',3])
            sage: s = W.simple_reflections()
            sage: [W.one().has_right_descent(i) for i in W.domain().index_set()]
            [False, False, False]
            sage: [s[1].has_right_descent(i) for i in W.domain().index_set()]
            [True, False, False]
            sage: [s[2].has_right_descent(i) for i in W.domain().index_set()]
            [False, True, False]
            sage: [s[3].has_right_descent(i) for i in W.domain().index_set()]
            [False, False, True]
            sage: [(s[3]*s[2]).has_right_descent(i) for i in W.domain().index_set()]
            [False, True, False]
        """
    def apply_simple_reflection(self, i, side: str = 'right'): ...
    def to_permutation(self):
        """
        A first approximation of to_permutation ...

        This assumes types A,B,C,D on the ambient lattice

        This further assume that the basis is indexed by 0,1,...
        and returns a permutation of (5,4,2,3,1) (beuargl), as a tuple
        """
    def to_permutation_string(self):
        '''
        EXAMPLES::

            sage: W = WeylGroup(["A",3])
            sage: s = W.simple_reflections()
            sage: (s[1]*s[2]*s[3]).to_permutation_string()
            \'2341\'
        '''

class WeylGroup_permutation(UniqueRepresentation, PermutationGroup_generic):
    """
    A Weyl group given as a permutation group.
    """
    @staticmethod
    def __classcall__(cls, cartan_type, prefix=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: W1 = WeylGroup(['B',2], implementation='permutation')
            sage: W2 = WeylGroup(CartanType(['B',2]), implementation='permutation')
            sage: W1 is W2
            True
        """
    def __init__(self, cartan_type, prefix) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['F',4], implementation='permutation')
            sage: TestSuite(W).run()
        """
    def iteration(self, algorithm: str = 'breadth', tracking_words: bool = True):
        '''
        Return an iterator going through all elements in ``self``.

        INPUT:

        - ``algorithm`` -- (default: ``\'breadth\'``) must be one of
          the following:

          * ``\'breadth\'`` -- iterate over in a linear extension of the
            weak order
          * ``\'depth\'`` -- iterate by a depth-first-search

        - ``tracking_words`` -- boolean (default: ``True``); whether or not to keep
          track of the reduced words and store them in ``_reduced_word``

        .. NOTE::

            The fastest iteration is the depth first algorithm without
            tracking words. In particular, ``\'depth\'`` is ~1.5x faster.

        EXAMPLES::

            sage: W = WeylGroup(["B",2], implementation=\'permutation\')

            sage: for w in W.iteration("breadth",True):
            ....:     print("%s %s"%(w, w._reduced_word))
            () []
            (1,3)(2,6)(5,7) [1]
            (1,5)(2,4)(6,8) [0]
            (1,7,5,3)(2,4,6,8) [0, 1]
            (1,3,5,7)(2,8,6,4) [1, 0]
            (2,8)(3,7)(4,6) [1, 0, 1]
            (1,7)(3,5)(4,8) [0, 1, 0]
            (1,5)(2,6)(3,7)(4,8) [0, 1, 0, 1]

            sage: for w in W.iteration("depth", False): w
            ()
            (1,3)(2,6)(5,7)
            (1,5)(2,4)(6,8)
            (1,3,5,7)(2,8,6,4)
            (1,7)(3,5)(4,8)
            (1,7,5,3)(2,4,6,8)
            (2,8)(3,7)(4,6)
            (1,5)(2,6)(3,7)(4,8)

        TESTS::

            sage: W = WeylGroup(["A",0], implementation=\'permutation\')
            sage: list(W)
            [()]
            sage: W[0]
            ()
        '''
    def __iter__(self):
        '''
        Return an iterator going through all elements in ``self``.

        For options and faster iteration see :meth:`iteration`.

        EXAMPLES::

            sage: W = WeylGroup(["B",2], implementation=\'permutation\')
            sage: for w in W: print("%s %s"%(w, w._reduced_word))
            () []
            (1,3)(2,6)(5,7) [1]
            (1,5)(2,4)(6,8) [0]
            (1,7,5,3)(2,4,6,8) [0, 1]
            (1,3,5,7)(2,8,6,4) [1, 0]
            (2,8)(3,7)(4,6) [1, 0, 1]
            (1,7)(3,5)(4,8) [0, 1, 0]
            (1,5)(2,6)(3,7)(4,8) [0, 1, 0, 1]
        '''
    @cached_method
    def rank(self):
        """
        Return the rank of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',4], implementation='permutation')
            sage: W.rank()
            4
        """
    def simple_reflection(self, i):
        """
        Return the ``i``-th simple reflection of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',4], implementation='permutation')
            sage: W.simple_reflection(1)
            (1,11)(2,5)(6,8)(9,10)(12,15)(16,18)(19,20)
            sage: W.simple_reflections()
            Finite family {1: (1,11)(2,5)(6,8)(9,10)(12,15)(16,18)(19,20),
                           2: (1,5)(2,12)(3,6)(7,9)(11,15)(13,16)(17,19),
                           3: (2,6)(3,13)(4,7)(5,8)(12,16)(14,17)(15,18),
                           4: (3,7)(4,14)(6,9)(8,10)(13,17)(16,19)(18,20)}
        """
    @cached_method
    def simple_roots(self):
        """
        Return the simple roots of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',4], implementation='permutation')
            sage: W.simple_roots()
            Finite family {1: (1, 0, 0, 0), 2: (0, 1, 0, 0),
                           3: (0, 0, 1, 0), 4: (0, 0, 0, 1)}
        """
    independent_roots = simple_roots
    @cached_method
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',4], implementation='permutation')
            sage: W.index_set()
            (1, 2, 3, 4)
        """
    @cached_method
    def reflection_index_set(self):
        """
        Return the index set of reflections of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',3], implementation='permutation')
            sage: W.reflection_index_set()
            (1, 2, 3, 4, 5, 6)
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['A',4], implementation='permutation')
            sage: W.cartan_type()
            ['A', 4]
        """
    @cached_method
    def roots(self):
        """
        Return the roots of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['G',2], implementation='permutation')
            sage: W.roots()
            ((1, 0),
             (0, 1),
             (1, 1),
             (3, 1),
             (2, 1),
             (3, 2),
             (-1, 0),
             (0, -1),
             (-1, -1),
             (-3, -1),
             (-2, -1),
             (-3, -2))
        """
    def positive_roots(self):
        """
        Return the positive roots of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['C',3], implementation='permutation')
            sage: W.positive_roots()
            ((1, 0, 0),
             (0, 1, 0),
             (0, 0, 1),
             (1, 1, 0),
             (0, 1, 1),
             (0, 2, 1),
             (1, 1, 1),
             (2, 2, 1),
             (1, 2, 1))
        """
    @cached_method
    def number_of_reflections(self):
        """
        Return the number of reflections in ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['D',4], implementation='permutation')
            sage: W.number_of_reflections()
            12
        """
    @cached_method
    def distinguished_reflections(self):
        """
        Return the reflections of ``self``.

        EXAMPLES::

            sage: W = WeylGroup(['B',2], implementation='permutation')
            sage: W.distinguished_reflections()
            Finite family {1: (1,5)(2,4)(6,8), 2: (1,3)(2,6)(5,7),
                           3: (2,8)(3,7)(4,6), 4: (1,7)(3,5)(4,8)}
        """
    reflections = distinguished_reflections
    def simple_root_index(self, i):
        """
        Return the index of the simple root `\\alpha_i`.

        This is the position of `\\alpha_i` in the list of simple roots.

        EXAMPLES::

            sage: W = WeylGroup(['A',3], implementation='permutation')
            sage: [W.simple_root_index(i) for i in W.index_set()]
            [0, 1, 2]
        """
    class Element(RealReflectionGroupElement): ...
