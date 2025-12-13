from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent

class ConjugacyClass(Parent):
    """
    Generic conjugacy classes for elements in a group.

    This is the default fall-back implementation to be used whenever
    GAP cannot handle the group.

    EXAMPLES::

        sage: G = SymmetricGroup(4)
        sage: g = G((1,2,3,4))
        sage: ConjugacyClass(G,g)
        Conjugacy class of (1,2,3,4) in Symmetric group of order 4! as a
        permutation group
    """
    def __init__(self, group, element) -> None:
        """
        Generic conjugacy classes for elements in a group.

        This is the default fall-back implementation to be used whenever
        GAP cannot handle the group.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: ConjugacyClass(G,g)
            Conjugacy class of (1,2,3,4) in Symmetric group of order 4! as a
            permutation group
            sage: TestSuite(G).run()                                                    # needs sage.rings.number_field
        """
    def __eq__(self, other):
        """
        Equality of conjugacy classes is tested by comparing the
        underlying sets.

        EXAMPLES::

            sage: F = GF(5)
            sage: gens = [matrix(F,2,[1,2, -1, 1]), matrix(F,2, [1,1, 0,1])]
            sage: H = MatrixGroup(gens)
            sage: h = H(matrix(F,2,[1,2, -1, 1]))
            sage: h2 = H(matrix(F,2,[1,1, 0, 1]))
            sage: g = h2*h*h2^(-1)
            sage: C = ConjugacyClass(H,h)
            sage: D = ConjugacyClass(H,g)
            sage: C == D
            True
        """
    def __ne__(self, other):
        """
        Negation of equality.

        EXAMPLES::

            sage: F = GF(5)
            sage: gens = [matrix(F,2, [1,2,-1,1]), matrix(F,2, [1,1,0,1])]
            sage: H = MatrixGroup(gens)
            sage: h = H(matrix(F,2, [1,2,-1,1]))
            sage: h2 = H(matrix(F,2, [1,1,0,1]))
            sage: g = h2 * h * h2^(-1)
            sage: C = ConjugacyClass(H, h)
            sage: D = ConjugacyClass(H, g)
            sage: C != D
            False
            sage: C != ConjugacyClass(H, H(identity_matrix(F, 2)))
            True
        """
    def __contains__(self, element) -> bool:
        """
        Check if ``element`` belongs to the conjugacy class ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: C = ConjugacyClass(G,g)
            sage: g in C
            True
        """
    def __iter__(self):
        '''
        Naive algorithm to give the elements of the conjugacy class.

        .. TODO::

            Implement a non-naive algorithm, cf. for instance
            G. Butler: "An Inductive Schema for Computing Conjugacy Classes
            in Permutation Groups", Math. of Comp. Vol. 62, No. 205 (1994)

        EXAMPLES:

        Groups of permutations::

            sage: G = SymmetricGroup(3)
            sage: g = G((1,2))
            sage: C = ConjugacyClass(G,g)
            sage: sorted(C)
            [(2,3), (1,2), (1,3)]

        It works for infinite groups::

            sage: a = matrix(ZZ,2,[1,1,0,1])
            sage: b = matrix(ZZ,2,[1,0,1,1])
            sage: G = MatrixGroup([a,b])        # takes 1s
            sage: a = G(a)
            sage: C = ConjugacyClass(G, a)
            sage: it = iter(C)
            sage: [next(it) for _ in range(5)] # random (nothing guarantees enumeration order)
            [
            [1 1]  [ 2  1]  [ 0  1]  [ 3  1]  [ 3  4]
            [0 1], [-1  0], [-1  2], [-4 -1], [-1 -1]
            ]

        We check that two matrices are in C::

            sage: b = G(b)
            sage: m1 = b * a * ~b
            sage: m2 = ~b * a * b
            sage: any(x == m1 for x in C)
            True
            sage: any(x == m2 for x in C)
            True
        '''
    @cached_method
    def set(self):
        """
        Return the set of elements of the conjugacy class.

        EXAMPLES:

        Groups of permutations::

            sage: G = SymmetricGroup(3)
            sage: g = G((1,2))
            sage: C = ConjugacyClass(G,g)
            sage: S = [(2,3), (1,2), (1,3)]
            sage: C.set() == Set(G(x) for x in S)
            True

        Groups of matrices over finite fields::

            sage: F = GF(5)
            sage: gens = [matrix(F,2,[1,2, -1, 1]), matrix(F,2, [1,1, 0,1])]
            sage: H = MatrixGroup(gens)
            sage: h = H(matrix(F,2,[1,2, -1, 1]))
            sage: C = ConjugacyClass(H,h)
            sage: S = [[[3, 2], [2, 4]], [[0, 1], [2, 2]], [[3, 4], [1, 4]],\\\n            ....: [[0, 3], [4, 2]], [[1, 2], [4, 1]], [[2, 1], [2, 0]],\\\n            ....: [[4, 1], [4, 3]], [[4, 4], [1, 3]], [[2, 4], [3, 0]],\\\n            ....: [[1, 4], [2, 1]], [[3, 3], [3, 4]], [[2, 3], [4, 0]],\\\n            ....: [[0, 2], [1, 2]], [[1, 3], [1, 1]], [[4, 3], [3, 3]],\\\n            ....: [[4, 2], [2, 3]], [[0, 4], [3, 2]], [[1, 1], [3, 1]],\\\n            ....: [[2, 2], [1, 0]], [[3, 1], [4, 4]]]
            sage: C.set() == Set(H(x) for x in S)
            True

        It is not implemented for infinite groups::

            sage: a = matrix(ZZ,2,[1,1,0,1])
            sage: b = matrix(ZZ,2,[1,0,1,1])
            sage: G = MatrixGroup([a,b])        # takes 1s
            sage: g = G(a)
            sage: C = ConjugacyClass(G, g)
            sage: C.set()
            Traceback (most recent call last):
            ...
            NotImplementedError: Listing the elements of conjugacy classes is not implemented for infinite groups! Use the iter function instead.
        """
    def list(self):
        """
        Return a list with all the elements of ``self``.

        EXAMPLES:

        Groups of permutations::

            sage: G = SymmetricGroup(3)
            sage: g = G((1,2,3))
            sage: c = ConjugacyClass(G,g)
            sage: L = c.list()
            sage: Set(L) == Set([G((1,3,2)), G((1,2,3))])
            True
        """
    def is_real(self):
        """
        Check if ``self`` is real (closed for inverses).

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: c = ConjugacyClass(G,g)
            sage: c.is_real()
            True
        """
    def is_rational(self):
        """
        Check if ``self`` is rational (closed for powers).

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: c = ConjugacyClass(G,g)
            sage: c.is_rational()
            False
        """
    def representative(self):
        """
        Return a representative of ``self``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: g = G((1,2,3))
            sage: C = ConjugacyClass(G,g)
            sage: C.representative()
            (1,2,3)
        """
    an_element = representative

class ConjugacyClassGAP(ConjugacyClass):
    """
    Class for a conjugacy class for groups defined over GAP.

    Intended for wrapping GAP methods on conjugacy classes.

    INPUT:

    - ``group`` -- the group in which the conjugacy class is taken

    - ``element`` -- the element generating the conjugacy class

    EXAMPLES::

        sage: G = SymmetricGroup(4)
        sage: g = G((1,2,3,4))
        sage: ConjugacyClassGAP(G,g)
        Conjugacy class of (1,2,3,4) in Symmetric group of order 4! as a
        permutation group
    """
    def __init__(self, group, element) -> None:
        """
        Constructor for the class.

        EXAMPLES:

        Conjugacy classes for groups of permutations::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: ConjugacyClassGAP(G,g)
            Conjugacy class of (1,2,3,4) in Symmetric group of order 4! as a permutation group

        Conjugacy classes for groups of matrices::

            sage: F = GF(5)
            sage: gens = [matrix(F,2,[1,2, -1, 1]), matrix(F,2, [1,1, 0,1])]
            sage: H = MatrixGroup(gens)
            sage: h = H(matrix(F,2,[1,2, -1, 1]))
            sage: ConjugacyClassGAP(H,h)
            Conjugacy class of [1 2]
            [4 1] in Matrix group over Finite Field of size 5 with 2 generators (
            [1 2]  [1 1]
            [4 1], [0 1]
            )
        """
    def cardinality(self):
        """
        Return the size of this conjugacy class.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: W = WeylGroup(['C',6])
            sage: cc = W.conjugacy_class(W.an_element())
            sage: cc.cardinality()
            3840
            sage: type(cc.cardinality())
            <class 'sage.rings.integer.Integer'>
        """
    def __contains__(self, g) -> bool:
        """
        Containment test.

        Wraps ``IsConjugate`` from GAP.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: W = WeylGroup(['C',6])
            sage: g0,g1,g2,g3,g4,g5 = W.gens()
            sage: cc = W.conjugacy_class(g0)
            sage: g0 in cc
            True
            sage: g1 in cc
            True
            sage: g2 in cc
            True
            sage: g3 in cc
            True
            sage: g4 in cc
            True
            sage: g5 in cc
            False

        Only trivial cases are implemented for infinite groups::

            sage: G = SL(2,ZZ)
            sage: m1 = G([[1,1],[0,1]])
            sage: m2 = G([[1,0],[1,1]])
            sage: m1 in G.conjugacy_class(m1) and m2 in G.conjugacy_class(m2)
            True
            sage: m2 in G.conjugacy_class(m1)
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented for finite groups
        """
    @cached_method
    def set(self):
        """
        Return a Sage ``Set`` with all the elements of the conjugacy class.

        By default attempts to use GAP construction of the conjugacy class.
        If GAP method is not implemented for the given group, and the group
        is finite, falls back to a naive algorithm.

        .. WARNING::

            The naive algorithm can be really slow and memory intensive.

        EXAMPLES:

        Groups of permutations::

            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: C = ConjugacyClassGAP(G,g)
            sage: S = [(1,3,2,4), (1,4,3,2), (1,3,4,2), (1,2,3,4), (1,4,2,3), (1,2,4,3)]
            sage: C.set() == Set(G(x) for x in S)
            True
        """
