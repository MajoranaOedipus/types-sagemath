from sage.categories.groups import Groups as Groups
from sage.groups.generic import structure_description as structure_description
from sage.groups.group import Group as Group
from sage.groups.libgap_mixin import GroupMixinLibGAP as GroupMixinLibGAP
from sage.groups.libgap_wrapper import ParentLibGAP as ParentLibGAP
from sage.groups.matrix_gps.group_element import MatrixGroupElement_gap as MatrixGroupElement_gap
from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic as MatrixGroup_generic

class MatrixGroup_gap(GroupMixinLibGAP, MatrixGroup_generic, ParentLibGAP):
    Element = MatrixGroupElement_gap
    def __init__(self, degree, base_ring, libgap_group, ambient=None, category=None) -> None:
        """
        Base class for matrix groups that implements GAP interface.

        INPUT:

        - ``degree`` -- integer; the degree (matrix size) of the
          matrix group

        - ``base_ring`` -- ring; the base ring of the matrices

        - ``libgap_group`` -- the defining libgap group

        - ``ambient`` -- a derived class of :class:`ParentLibGAP` or
          ``None`` (default); the ambient class if ``libgap_group``
          has been defined as a subgroup

        TESTS:

        ::

            sage: from sage.groups.matrix_gps.matrix_group_gap import MatrixGroup_gap
            sage: MatrixGroup_gap(2, ZZ, libgap.eval('GL(2, Integers)'))
            Matrix group over Integer Ring with 3 generators (
            [0 1]  [-1  0]  [1 1]
            [1 0], [ 0  1], [0 1]
            )

        Check that the slowness of GAP iterators and enumerators for matrix groups
        (cf. http://tracker.gap-system.org/issues/369) has been fixed::

            sage: i = iter(GL(6,5))
            sage: [ next(i) for j in range(8) ]
            [
            [1 0 0 0 0 0]  [4 0 0 0 0 1]  [0 4 0 0 0 0]  [0 4 0 0 0 0]
            [0 1 0 0 0 0]  [4 0 0 0 0 0]  [0 0 4 0 0 0]  [0 0 4 0 0 0]
            [0 0 1 0 0 0]  [0 4 0 0 0 0]  [0 0 0 4 0 0]  [0 0 0 4 0 0]
            [0 0 0 1 0 0]  [0 0 4 0 0 0]  [0 0 0 0 4 0]  [0 0 0 0 4 0]
            [0 0 0 0 1 0]  [0 0 0 4 0 0]  [0 0 0 0 0 4]  [0 0 0 0 0 4]
            [0 0 0 0 0 1], [0 0 0 0 4 0], [1 4 0 0 0 0], [2 4 0 0 0 0],
            [3 0 0 0 0 1]  [4 0 0 1 3 3]  [0 0 0 2 0 0]  [1 0 0 0 4 4]
            [3 0 0 0 0 0]  [4 0 0 0 3 3]  [0 0 0 0 4 0]  [1 0 0 0 0 4]
            [0 4 0 0 0 0]  [3 0 0 0 0 1]  [2 2 0 0 0 2]  [1 0 0 0 0 0]
            [0 0 4 0 0 0]  [3 0 0 0 0 0]  [1 4 0 0 0 0]  [0 1 0 0 0 0]
            [0 0 0 4 0 0]  [0 4 0 0 0 0]  [0 2 4 0 0 0]  [0 0 1 0 0 0]
            [4 0 0 0 2 3], [2 0 3 4 4 4], [0 0 1 4 0 0], [0 0 0 1 0 0]
            ]

        And the same for listing the group elements, as well as few other issues::

            sage: F = GF(3)
            sage: gens = [matrix(F,2, [1,0, -1,1]), matrix(F, 2, [1,1,0,1])]
            sage: G = MatrixGroup(gens)
            sage: G.cardinality()
            24
            sage: v = G.list()
            sage: len(v)
            24
            sage: v[:5]
            (
            [1 0]  [2 0]  [0 1]  [0 2]  [1 2]
            [0 1], [0 2], [2 0], [1 0], [2 2]
            )
            sage: all(g in G for g in G.list())
            True

        An example over a ring (see :issue:`5241`)::

            sage: M1 = matrix(ZZ,2,[[-1,0],[0,1]])
            sage: M2 = matrix(ZZ,2,[[1,0],[0,-1]])
            sage: M3 = matrix(ZZ,2,[[-1,0],[0,-1]])
            sage: MG = MatrixGroup([M1, M2, M3])
            sage: MG.list()
            (
            [1 0]  [ 1  0]  [-1  0]  [-1  0]
            [0 1], [ 0 -1], [ 0  1], [ 0 -1]
            )
            sage: MG.list()[1]
            [ 1  0]
            [ 0 -1]
            sage: MG.list()[1].parent()
            Matrix group over Integer Ring with 3 generators (
            [-1  0]  [ 1  0]  [-1  0]
            [ 0  1], [ 0 -1], [ 0 -1]
            )

        An example over a field (see :issue:`10515`)::

            sage: gens = [matrix(QQ,2,[1,0,0,1])]
            sage: MatrixGroup(gens).list()
            (
            [1 0]
            [0 1]
            )

        Another example over a ring (see :issue:`9437`)::

            sage: len(SL(2, Zmod(4)).list())
            48

        An error is raised if the group is not finite::

            sage: GL(2,ZZ).list()
            Traceback (most recent call last):
            ...
            NotImplementedError: group must be finite
        """
    def __iter__(self):
        '''
        Iterate over the elements of the group.

        This method overrides the matrix group enumerator in GAP which
        does not (and often just cannot) work for infinite groups.

        TESTS:

        infinite groups can be dealt with::

            sage: import itertools
            sage: W = WeylGroup(["A",3,1])                                              # needs sage.rings.number_field
            sage: list(itertools.islice(W, int(4)))                                     # needs sage.rings.number_field
            [
            [1 0 0 0]  [-1  1  0  1]  [ 1  0  0  0]  [ 1  0  0  0]
            [0 1 0 0]  [ 0  1  0  0]  [ 1 -1  1  0]  [ 0  1  0  0]
            [0 0 1 0]  [ 0  0  1  0]  [ 0  0  1  0]  [ 0  1 -1  1]
            [0 0 0 1], [ 0  0  0  1], [ 0  0  0  1], [ 0  0  0  1]
            ]

        and finite groups, too::

            sage: G = GL(6,5)
            sage: list(itertools.islice(G, int(4)))
            [
            [1 0 0 0 0 0]  [4 0 0 0 0 1]  [0 4 0 0 0 0]  [0 4 0 0 0 0]
            [0 1 0 0 0 0]  [4 0 0 0 0 0]  [0 0 4 0 0 0]  [0 0 4 0 0 0]
            [0 0 1 0 0 0]  [0 4 0 0 0 0]  [0 0 0 4 0 0]  [0 0 0 4 0 0]
            [0 0 0 1 0 0]  [0 0 4 0 0 0]  [0 0 0 0 4 0]  [0 0 0 0 4 0]
            [0 0 0 0 1 0]  [0 0 0 4 0 0]  [0 0 0 0 0 4]  [0 0 0 0 0 4]
            [0 0 0 0 0 1], [0 0 0 0 4 0], [1 4 0 0 0 0], [2 4 0 0 0 0]
            ]
        '''
    def subgroup(self, generators, check: bool = True):
        """
        Return the subgroup generated by the given generators.

        INPUT:

        - ``generators`` -- list/tuple/iterable of group elements of ``self``
        - ``check`` -- boolean (default: ``True``); whether to check that each
          matrix is invertible

        OUTPUT: the subgroup generated by ``generators`` as an instance of
        :class:`FinitelyGeneratedMatrixGroup_gap`

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: UCF = UniversalCyclotomicField()
            sage: G  = GL(3, UCF)
            sage: e3 = UCF.gen(3); e5 = UCF.gen(5)
            sage: m = matrix(UCF, 3,3, [[e3, 1, 0], [0, e5, 7],[4, 3, 2]])
            sage: S = G.subgroup([m]); S
            Subgroup with 1 generators (
            [E(3)    1    0]
            [   0 E(5)    7]
            [   4    3    2]
            ) of General Linear Group of degree 3 over Universal Cyclotomic Field

            sage: # needs sage.rings.number_field
            sage: CF3 = CyclotomicField(3)
            sage: G  = GL(3, CF3)
            sage: e3 = CF3.gen()
            sage: m = matrix(CF3, 3,3, [[e3, 1, 0], [0, ~e3, 7],[4, 3, 2]])
            sage: S = G.subgroup([m]); S
            Subgroup with 1 generators (
            [     zeta3          1          0]
            [         0 -zeta3 - 1          7]
            [         4          3          2]
            ) of General Linear Group of degree 3 over Cyclotomic Field of order 3 and degree 2

        TESTS::

            sage: TestSuite(G).run()                                                    # needs sage.rings.number_field
            sage: TestSuite(S).run()                                                    # needs sage.rings.number_field

            sage: # needs sage.rings.number_field
            sage: W = CoxeterGroup(['I',7])
            sage: s = W.simple_reflections()
            sage: G = W.subgroup([s[1]])
            sage: G.category()
            Category of finite groups

            sage: # needs sage.rings.number_field
            sage: W = WeylGroup(['A',2])
            sage: s = W.simple_reflections()
            sage: G = W.subgroup([s[1]])
            sage: G.category()
            Category of finite groups
        """
