import sage.groups.perm_gps.permgroup_element
from sage.arith.functions import lcm as lcm
from sage.categories.category import ZZ as ZZ
from sage.combinat.root_system.reflection_group_c import reduce_in_coset as reduce_in_coset, reduced_word_c as reduced_word_c
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class ComplexReflectionGroupElement(sage.groups.perm_gps.permgroup_element.PermutationGroupElement):
    """File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 38)

        An element in a complex reflection group.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def action(self, vec, on_space=...) -> Any:
        '''ComplexReflectionGroupElement.action(self, vec, on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 354)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                      # optional - gap3
            sage: w = W.from_reduced_word([1, 2, 1, 1, 2])          # optional - gap3
            sage: for alpha in W.independent_roots():               # optional - gap3
            ....:     print("%s -> %s"%(alpha,w.action(alpha)))
            (1, 0) -> (E(3), 0)
            (-1, 1) -> (-E(3), E(3)^2)'''
    @overload
    def action(self, alpha) -> Any:
        '''ComplexReflectionGroupElement.action(self, vec, on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 354)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                      # optional - gap3
            sage: w = W.from_reduced_word([1, 2, 1, 1, 2])          # optional - gap3
            sage: for alpha in W.independent_roots():               # optional - gap3
            ....:     print("%s -> %s"%(alpha,w.action(alpha)))
            (1, 0) -> (E(3), 0)
            (-1, 1) -> (-E(3), E(3)^2)'''
    @overload
    def action_on_root(self, root) -> Any:
        '''ComplexReflectionGroupElement.action_on_root(self, root)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 436)

        Return the root obtained by applying ``self`` to ``root``
        on the right.

        INPUT:

        - ``root`` -- the root to act on

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

        TESTS::

            sage: W = ReflectionGroup(4); Phi = sorted(W.roots())   # optional - gap3
            sage: all(sorted([w.action_on_root(beta) for beta in Phi]) == Phi for w in W)   # optional - gap3
            True'''
    @overload
    def action_on_root(self, beta, side=...) -> Any:
        '''ComplexReflectionGroupElement.action_on_root(self, root)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 436)

        Return the root obtained by applying ``self`` to ``root``
        on the right.

        INPUT:

        - ``root`` -- the root to act on

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

        TESTS::

            sage: W = ReflectionGroup(4); Phi = sorted(W.roots())   # optional - gap3
            sage: all(sorted([w.action_on_root(beta) for beta in Phi]) == Phi for w in W)   # optional - gap3
            True'''
    @overload
    def action_on_root(self, beta) -> Any:
        '''ComplexReflectionGroupElement.action_on_root(self, root)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 436)

        Return the root obtained by applying ``self`` to ``root``
        on the right.

        INPUT:

        - ``root`` -- the root to act on

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

        TESTS::

            sage: W = ReflectionGroup(4); Phi = sorted(W.roots())   # optional - gap3
            sage: all(sorted([w.action_on_root(beta) for beta in Phi]) == Phi for w in W)   # optional - gap3
            True'''
    @overload
    def action_on_root_indices(self, i) -> Any:
        """ComplexReflectionGroupElement.action_on_root_indices(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 403)

        Return the right action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [4, 3, 5, 1, 0, 2]

        TESTS::

            sage: W = ReflectionGroup(4)                 # optional - gap3
            sage: N = len(W.roots())                     # optional - gap3
            sage: all(sorted([w.action_on_root_indices(i) for i in range(N)]) == list(range(N)) for w in W)   # optional - gap3
            True"""
    @overload
    def action_on_root_indices(self, i) -> Any:
        """ComplexReflectionGroupElement.action_on_root_indices(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 403)

        Return the right action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [4, 3, 5, 1, 0, 2]

        TESTS::

            sage: W = ReflectionGroup(4)                 # optional - gap3
            sage: N = len(W.roots())                     # optional - gap3
            sage: all(sorted([w.action_on_root_indices(i) for i in range(N)]) == list(range(N)) for w in W)   # optional - gap3
            True"""
    @overload
    def action_on_root_indices(self, i) -> Any:
        """ComplexReflectionGroupElement.action_on_root_indices(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 403)

        Return the right action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [4, 3, 5, 1, 0, 2]

        TESTS::

            sage: W = ReflectionGroup(4)                 # optional - gap3
            sage: N = len(W.roots())                     # optional - gap3
            sage: all(sorted([w.action_on_root_indices(i) for i in range(N)]) == list(range(N)) for w in W)   # optional - gap3
            True"""
    @overload
    def action_on_root_indices(self, i) -> Any:
        """ComplexReflectionGroupElement.action_on_root_indices(self, i)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 403)

        Return the right action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i) for i in range(N)]
            [4, 3, 5, 1, 0, 2]

        TESTS::

            sage: W = ReflectionGroup(4)                 # optional - gap3
            sage: N = len(W.roots())                     # optional - gap3
            sage: all(sorted([w.action_on_root_indices(i) for i in range(N)]) == list(range(N)) for w in W)   # optional - gap3
            True"""
    @overload
    def canonical_matrix(self) -> Any:
        """ComplexReflectionGroupElement.canonical_matrix(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 317)

        Return the matrix of ``self`` in the canonical faithful representation.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = WeylGroup(['A',2], prefix='s', implementation='permutation')
            sage: for w in W:
            ....:     w.reduced_word()
            ....:     w.canonical_matrix()
            []
            [1 0]
            [0 1]
            [2]
            [ 1  1]
            [ 0 -1]
            [1]
            [-1  0]
            [ 1  1]
            [1, 2]
            [-1 -1]
            [ 1  0]
            [2, 1]
            [ 0  1]
            [-1 -1]
            [1, 2, 1]
            [ 0 -1]
            [-1  0]"""
    @overload
    def canonical_matrix(self) -> Any:
        """ComplexReflectionGroupElement.canonical_matrix(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 317)

        Return the matrix of ``self`` in the canonical faithful representation.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = WeylGroup(['A',2], prefix='s', implementation='permutation')
            sage: for w in W:
            ....:     w.reduced_word()
            ....:     w.canonical_matrix()
            []
            [1 0]
            [0 1]
            [2]
            [ 1  1]
            [ 0 -1]
            [1]
            [-1  0]
            [ 1  1]
            [1, 2]
            [-1 -1]
            [ 1  0]
            [2, 1]
            [ 0  1]
            [-1 -1]
            [1, 2, 1]
            [ 0 -1]
            [-1  0]"""
    @overload
    def fix_space(self) -> Any:
        """ComplexReflectionGroupElement.fix_space(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 489)

        Return the fix space of ``self``.

        This is the sub vector space of the underlying vector space
        on which ``self`` acts trivially.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     w.reduced_word()
            ....:     w.fix_space()
            []
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
            [2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            [1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
            [1, 2]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [2, 1]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [1, 2, 1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -1]

            sage: W = ReflectionGroup(23)                 # optional - gap3
            sage: W.gen(0).fix_space()                    # optional - gap3
            Vector space of degree 3 and dimension 2 over Universal Cyclotomic Field
            Basis matrix:
            [0 1 0]
            [0 0 1]"""
    @overload
    def fix_space(self) -> Any:
        """ComplexReflectionGroupElement.fix_space(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 489)

        Return the fix space of ``self``.

        This is the sub vector space of the underlying vector space
        on which ``self`` acts trivially.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     w.reduced_word()
            ....:     w.fix_space()
            []
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
            [2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            [1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
            [1, 2]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [2, 1]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [1, 2, 1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -1]

            sage: W = ReflectionGroup(23)                 # optional - gap3
            sage: W.gen(0).fix_space()                    # optional - gap3
            Vector space of degree 3 and dimension 2 over Universal Cyclotomic Field
            Basis matrix:
            [0 1 0]
            [0 0 1]"""
    @overload
    def fix_space(self) -> Any:
        """ComplexReflectionGroupElement.fix_space(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 489)

        Return the fix space of ``self``.

        This is the sub vector space of the underlying vector space
        on which ``self`` acts trivially.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     w.reduced_word()
            ....:     w.fix_space()
            []
            Vector space of degree 2 and dimension 2 over Rational Field
            Basis matrix:
            [1 0]
            [0 1]
            [2]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [1 0]
            [1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [0 1]
            [1, 2]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [2, 1]
            Vector space of degree 2 and dimension 0 over Rational Field
            Basis matrix:
            []
            [1, 2, 1]
            Vector space of degree 2 and dimension 1 over Rational Field
            Basis matrix:
            [ 1 -1]

            sage: W = ReflectionGroup(23)                 # optional - gap3
            sage: W.gen(0).fix_space()                    # optional - gap3
            Vector space of degree 3 and dimension 2 over Universal Cyclotomic Field
            Basis matrix:
            [0 1 0]
            [0 0 1]"""
    @overload
    def galois_conjugates(self) -> Any:
        """ComplexReflectionGroupElement.galois_conjugates(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 586)

        Return all Galois conjugates of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print(w.galois_conjugates())
            [[1 0]
             [0 1]]
            [[   1    0]
             [   0 E(3)], [     1      0]
             [     0 E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[     1      0]
             [     0 E(3)^2], [   1    0]
             [   0 E(3)]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[   -1     0]
             [    0 -E(3)], [     -1       0]
             [      0 -E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[     -1       0]
             [      0 -E(3)^2], [   -1     0]
             [    0 -E(3)]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[-1  0]
             [ 0 -1]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]

            sage: data = {w: w.galois_conjugates() for w in W}      # optional - gap3
            sage: all(w.galois_conjugates() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def galois_conjugates(self) -> Any:
        """ComplexReflectionGroupElement.galois_conjugates(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 586)

        Return all Galois conjugates of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print(w.galois_conjugates())
            [[1 0]
             [0 1]]
            [[   1    0]
             [   0 E(3)], [     1      0]
             [     0 E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[     1      0]
             [     0 E(3)^2], [   1    0]
             [   0 E(3)]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[   -1     0]
             [    0 -E(3)], [     -1       0]
             [      0 -E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[     -1       0]
             [      0 -E(3)^2], [   -1     0]
             [    0 -E(3)]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[-1  0]
             [ 0 -1]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]

            sage: data = {w: w.galois_conjugates() for w in W}      # optional - gap3
            sage: all(w.galois_conjugates() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def galois_conjugates(self) -> Any:
        """ComplexReflectionGroupElement.galois_conjugates(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 586)

        Return all Galois conjugates of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print(w.galois_conjugates())
            [[1 0]
             [0 1]]
            [[   1    0]
             [   0 E(3)], [     1      0]
             [     0 E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[     1      0]
             [     0 E(3)^2], [   1    0]
             [   0 E(3)]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[   -1     0]
             [    0 -E(3)], [     -1       0]
             [      0 -E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[     -1       0]
             [      0 -E(3)^2], [   -1     0]
             [    0 -E(3)]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[-1  0]
             [ 0 -1]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]

            sage: data = {w: w.galois_conjugates() for w in W}      # optional - gap3
            sage: all(w.galois_conjugates() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def galois_conjugates(self) -> Any:
        """ComplexReflectionGroupElement.galois_conjugates(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 586)

        Return all Galois conjugates of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print(w.galois_conjugates())
            [[1 0]
             [0 1]]
            [[   1    0]
             [   0 E(3)], [     1      0]
             [     0 E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[     1      0]
             [     0 E(3)^2], [   1    0]
             [   0 E(3)]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[   -1     0]
             [    0 -E(3)], [     -1       0]
             [      0 -E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) + 4/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [ 4/3*E(3) + 2/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2]]
            [[ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2  2/3*E(3) + 1/3*E(3)^2],
             [-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2  1/3*E(3) + 2/3*E(3)^2]]
            [[-1/3*E(3) + 1/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[     -1       0]
             [      0 -E(3)^2], [   -1     0]
             [    0 -E(3)]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [-4/3*E(3) - 2/3*E(3)^2 -2/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) - 4/3*E(3)^2 -1/3*E(3) - 2/3*E(3)^2]]
            [[-1  0]
             [ 0 -1]]
            [[-1/3*E(3) + 1/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2]
             [ 2/3*E(3) - 2/3*E(3)^2  1/3*E(3) - 1/3*E(3)^2],
             [ 1/3*E(3) - 1/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]
             [-2/3*E(3) + 2/3*E(3)^2 -1/3*E(3) + 1/3*E(3)^2]]

            sage: data = {w: w.galois_conjugates() for w in W}      # optional - gap3
            sage: all(w.galois_conjugates() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def length(self) -> Any:
        '''ComplexReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 142)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print("{} {}".format(w.reduced_word(), w.length()))
            [] 0
            [1] 1
            [2] 1
            [1, 1] 2
            [1, 2] 2
            [2, 1] 2
            [2, 2] 2
            [1, 1, 2] 3
            [1, 2, 1] 3
            [1, 2, 2] 3
            [2, 1, 1] 3
            [2, 2, 1] 3
            [1, 1, 2, 1] 4
            [1, 1, 2, 2] 4
            [1, 2, 1, 1] 4
            [1, 2, 2, 1] 4
            [2, 1, 1, 2] 4
            [2, 2, 1, 1] 4
            [1, 1, 2, 1, 1] 5
            [1, 1, 2, 2, 1] 5
            [1, 2, 1, 1, 2] 5
            [1, 2, 2, 1, 1] 5
            [1, 1, 2, 1, 1, 2] 6
            [1, 1, 2, 2, 1, 1] 6

            sage: data = {w: (len(w.reduced_word()), w.length())    # optional - gap3
            ....:         for w in W.iteration_tracking_words()}
            sage: for w in W:                                       # optional - gap3
            ....:     assert data[w] == (w.length(), w.length()), w'''
    @overload
    def length(self) -> Any:
        '''ComplexReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 142)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print("{} {}".format(w.reduced_word(), w.length()))
            [] 0
            [1] 1
            [2] 1
            [1, 1] 2
            [1, 2] 2
            [2, 1] 2
            [2, 2] 2
            [1, 1, 2] 3
            [1, 2, 1] 3
            [1, 2, 2] 3
            [2, 1, 1] 3
            [2, 2, 1] 3
            [1, 1, 2, 1] 4
            [1, 1, 2, 2] 4
            [1, 2, 1, 1] 4
            [1, 2, 2, 1] 4
            [2, 1, 1, 2] 4
            [2, 2, 1, 1] 4
            [1, 1, 2, 1, 1] 5
            [1, 1, 2, 2, 1] 5
            [1, 2, 1, 1, 2] 5
            [1, 2, 2, 1, 1] 5
            [1, 1, 2, 1, 1, 2] 6
            [1, 1, 2, 2, 1, 1] 6

            sage: data = {w: (len(w.reduced_word()), w.length())    # optional - gap3
            ....:         for w in W.iteration_tracking_words()}
            sage: for w in W:                                       # optional - gap3
            ....:     assert data[w] == (w.length(), w.length()), w'''
    @overload
    def length(self) -> Any:
        '''ComplexReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 142)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print("{} {}".format(w.reduced_word(), w.length()))
            [] 0
            [1] 1
            [2] 1
            [1, 1] 2
            [1, 2] 2
            [2, 1] 2
            [2, 2] 2
            [1, 1, 2] 3
            [1, 2, 1] 3
            [1, 2, 2] 3
            [2, 1, 1] 3
            [2, 2, 1] 3
            [1, 1, 2, 1] 4
            [1, 1, 2, 2] 4
            [1, 2, 1, 1] 4
            [1, 2, 2, 1] 4
            [2, 1, 1, 2] 4
            [2, 2, 1, 1] 4
            [1, 1, 2, 1, 1] 5
            [1, 1, 2, 2, 1] 5
            [1, 2, 1, 1, 2] 5
            [1, 2, 2, 1, 1] 5
            [1, 1, 2, 1, 1, 2] 6
            [1, 1, 2, 2, 1, 1] 6

            sage: data = {w: (len(w.reduced_word()), w.length())    # optional - gap3
            ....:         for w in W.iteration_tracking_words()}
            sage: for w in W:                                       # optional - gap3
            ....:     assert data[w] == (w.length(), w.length()), w'''
    @overload
    def length(self) -> Any:
        '''ComplexReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 142)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:     print("{} {}".format(w.reduced_word(), w.length()))
            [] 0
            [1] 1
            [2] 1
            [1, 1] 2
            [1, 2] 2
            [2, 1] 2
            [2, 2] 2
            [1, 1, 2] 3
            [1, 2, 1] 3
            [1, 2, 2] 3
            [2, 1, 1] 3
            [2, 2, 1] 3
            [1, 1, 2, 1] 4
            [1, 1, 2, 2] 4
            [1, 2, 1, 1] 4
            [1, 2, 2, 1] 4
            [2, 1, 1, 2] 4
            [2, 2, 1, 1] 4
            [1, 1, 2, 1, 1] 5
            [1, 1, 2, 2, 1] 5
            [1, 2, 1, 1, 2] 5
            [1, 2, 2, 1, 1] 5
            [1, 1, 2, 1, 1, 2] 6
            [1, 1, 2, 2, 1, 1] 6

            sage: data = {w: (len(w.reduced_word()), w.length())    # optional - gap3
            ....:         for w in W.iteration_tracking_words()}
            sage: for w in W:                                       # optional - gap3
            ....:     assert data[w] == (w.length(), w.length()), w'''
    def matrix(self, *args, **kwargs):
        """ComplexReflectionGroupElement.to_matrix(self, on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 187)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                                          # optional - gap3
            sage: data = {w: [w.to_matrix(), w.to_matrix(on_space='dual')] for w in W}  # optional - gap3
            sage: for w in W.iteration_tracking_words():                                # optional - gap3
            ....:     w.reduced_word()
            ....:     mats = [w.to_matrix(), w.to_matrix(on_space='dual')]
            ....:     mats
            ....:     assert data[w] == mats
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [1]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0    1], [     0      1]
            ]
            [2]
            [
            [0 1]  [0 1]
            [1 0], [1 0]
            ]
            [1, 1]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0      1], [   0    1]
            ]
            [1, 2]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [   1    0], [     1      0]
            ]
            [2, 1]
            [
            [   0    1]  [     0      1]
            [E(3)    0], [E(3)^2      0]
            ]
            [1, 1, 2]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [     1      0], [   1    0]
            ]
            [1, 2, 1]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [E(3)    0], [E(3)^2      0]
            ]
            [2, 1, 1]
            [
            [     0      1]  [   0    1]
            [E(3)^2      0], [E(3)    0]
            ]
            [2, 1, 2]
            [
            [   1    0]  [     1      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [1, 1, 2, 1]
            [
            [     0 E(3)^2]  [     0   E(3)]
            [  E(3)      0], [E(3)^2      0]
            ]
            [1, 2, 1, 1]
            [
            [     0   E(3)]  [     0 E(3)^2]
            [E(3)^2      0], [  E(3)      0]
            ]
            [1, 2, 1, 2]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [2, 1, 1, 2]
            [
            [     1      0]  [   1    0]
            [     0 E(3)^2], [   0 E(3)]
            ]
            [1, 1, 2, 1, 1]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [E(3)^2      0], [E(3)    0]
            ]
            [1, 1, 2, 1, 2]
            [
            [E(3)^2      0]  [  E(3)      0]
            [     0   E(3)], [     0 E(3)^2]
            ]
            [1, 2, 1, 1, 2]
            [
            [  E(3)      0]  [E(3)^2      0]
            [     0 E(3)^2], [     0   E(3)]
            ]
            [1, 1, 2, 1, 1, 2]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0 E(3)^2], [   0 E(3)]
            ]"""
    @overload
    def reduced_word(self) -> Any:
        """ComplexReflectionGroupElement.reduced_word(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 90)

        Return a word in the simple reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((5,1,1), index_set=['a'], hyperplane_index_set=['x'], reflection_index_set=['A','B','C','D']) # optional - gap3
            sage: [w.reduced_word() for w in W]                     # optional - gap3
            [[], ['a'], ['a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a', 'a']]

        .. SEEALSO:: :meth:`reduced_word_in_reflections`"""
    @overload
    def reduced_word(self) -> Any:
        """ComplexReflectionGroupElement.reduced_word(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 90)

        Return a word in the simple reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((5,1,1), index_set=['a'], hyperplane_index_set=['x'], reflection_index_set=['A','B','C','D']) # optional - gap3
            sage: [w.reduced_word() for w in W]                     # optional - gap3
            [[], ['a'], ['a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a', 'a']]

        .. SEEALSO:: :meth:`reduced_word_in_reflections`"""
    @overload
    def reduced_word_in_reflections(self) -> Any:
        """ComplexReflectionGroupElement.reduced_word_in_reflections(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 122)

        Return a word in the reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((5,1,1), index_set=['a'], reflection_index_set=['A','B','C','D']) # optional - gap3
            sage: [w.reduced_word_in_reflections() for w in W]      # optional - gap3
            [[], ['A'], ['B'], ['C'], ['D']]

        .. SEEALSO:: :meth:`reduced_word`"""
    @overload
    def reduced_word_in_reflections(self) -> Any:
        """ComplexReflectionGroupElement.reduced_word_in_reflections(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 122)

        Return a word in the reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup((5,1,1), index_set=['a'], reflection_index_set=['A','B','C','D']) # optional - gap3
            sage: [w.reduced_word_in_reflections() for w in W]      # optional - gap3
            [[], ['A'], ['B'], ['C'], ['D']]

        .. SEEALSO:: :meth:`reduced_word`"""
    @overload
    def reflection_eigenvalues(self, is_class_representative=...) -> Any:
        """ComplexReflectionGroupElement.reflection_eigenvalues(self, is_class_representative=False)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 539)

        Return the reflection eigenvalues of ``self``.

        INPUT:

        - ``is_class_representative`` -- boolean (default: ``False``); whether
          to first replace ``self`` by the representative of its
          conjugacy class

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:      w.reflection_eigenvalues()
            [0, 0]
            [1/3, 0]
            [1/3, 0]
            [2/3, 0]
            [1/6, 1/2]
            [1/6, 1/2]
            [2/3, 0]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/3, 0]
            [1/2, 5/6]
            [1/3, 0]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/6, 1/2]
            [2/3, 0]
            [1/6, 1/2]
            [2/3, 0]
            [1/2, 1/2]
            [1/4, 3/4]

            sage: data = {w: w.reflection_eigenvalues() for w in W}  # optional - gap3
            sage: all(w.reflection_eigenvalues() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def reflection_eigenvalues(self) -> Any:
        """ComplexReflectionGroupElement.reflection_eigenvalues(self, is_class_representative=False)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 539)

        Return the reflection eigenvalues of ``self``.

        INPUT:

        - ``is_class_representative`` -- boolean (default: ``False``); whether
          to first replace ``self`` by the representative of its
          conjugacy class

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:      w.reflection_eigenvalues()
            [0, 0]
            [1/3, 0]
            [1/3, 0]
            [2/3, 0]
            [1/6, 1/2]
            [1/6, 1/2]
            [2/3, 0]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/3, 0]
            [1/2, 5/6]
            [1/3, 0]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/6, 1/2]
            [2/3, 0]
            [1/6, 1/2]
            [2/3, 0]
            [1/2, 1/2]
            [1/4, 3/4]

            sage: data = {w: w.reflection_eigenvalues() for w in W}  # optional - gap3
            sage: all(w.reflection_eigenvalues() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def reflection_eigenvalues(self) -> Any:
        """ComplexReflectionGroupElement.reflection_eigenvalues(self, is_class_representative=False)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 539)

        Return the reflection eigenvalues of ``self``.

        INPUT:

        - ``is_class_representative`` -- boolean (default: ``False``); whether
          to first replace ``self`` by the representative of its
          conjugacy class

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:      w.reflection_eigenvalues()
            [0, 0]
            [1/3, 0]
            [1/3, 0]
            [2/3, 0]
            [1/6, 1/2]
            [1/6, 1/2]
            [2/3, 0]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/3, 0]
            [1/2, 5/6]
            [1/3, 0]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/6, 1/2]
            [2/3, 0]
            [1/6, 1/2]
            [2/3, 0]
            [1/2, 1/2]
            [1/4, 3/4]

            sage: data = {w: w.reflection_eigenvalues() for w in W}  # optional - gap3
            sage: all(w.reflection_eigenvalues() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def reflection_eigenvalues(self) -> Any:
        """ComplexReflectionGroupElement.reflection_eigenvalues(self, is_class_representative=False)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 539)

        Return the reflection eigenvalues of ``self``.

        INPUT:

        - ``is_class_representative`` -- boolean (default: ``False``); whether
          to first replace ``self`` by the representative of its
          conjugacy class

        EXAMPLES::

            sage: W = ReflectionGroup(4)                            # optional - gap3
            sage: for w in W.iteration_tracking_words():            # optional - gap3
            ....:      w.reflection_eigenvalues()
            [0, 0]
            [1/3, 0]
            [1/3, 0]
            [2/3, 0]
            [1/6, 1/2]
            [1/6, 1/2]
            [2/3, 0]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/4, 3/4]
            [1/3, 0]
            [1/2, 5/6]
            [1/3, 0]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/2, 5/6]
            [1/6, 1/2]
            [2/3, 0]
            [1/6, 1/2]
            [2/3, 0]
            [1/2, 1/2]
            [1/4, 3/4]

            sage: data = {w: w.reflection_eigenvalues() for w in W}  # optional - gap3
            sage: all(w.reflection_eigenvalues() == data[w] for w in W.iteration_tracking_words())  # optional - gap3
            True"""
    @overload
    def to_matrix(self, on_space=...) -> Any:
        """ComplexReflectionGroupElement.to_matrix(self, on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 187)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                                          # optional - gap3
            sage: data = {w: [w.to_matrix(), w.to_matrix(on_space='dual')] for w in W}  # optional - gap3
            sage: for w in W.iteration_tracking_words():                                # optional - gap3
            ....:     w.reduced_word()
            ....:     mats = [w.to_matrix(), w.to_matrix(on_space='dual')]
            ....:     mats
            ....:     assert data[w] == mats
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [1]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0    1], [     0      1]
            ]
            [2]
            [
            [0 1]  [0 1]
            [1 0], [1 0]
            ]
            [1, 1]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0      1], [   0    1]
            ]
            [1, 2]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [   1    0], [     1      0]
            ]
            [2, 1]
            [
            [   0    1]  [     0      1]
            [E(3)    0], [E(3)^2      0]
            ]
            [1, 1, 2]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [     1      0], [   1    0]
            ]
            [1, 2, 1]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [E(3)    0], [E(3)^2      0]
            ]
            [2, 1, 1]
            [
            [     0      1]  [   0    1]
            [E(3)^2      0], [E(3)    0]
            ]
            [2, 1, 2]
            [
            [   1    0]  [     1      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [1, 1, 2, 1]
            [
            [     0 E(3)^2]  [     0   E(3)]
            [  E(3)      0], [E(3)^2      0]
            ]
            [1, 2, 1, 1]
            [
            [     0   E(3)]  [     0 E(3)^2]
            [E(3)^2      0], [  E(3)      0]
            ]
            [1, 2, 1, 2]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [2, 1, 1, 2]
            [
            [     1      0]  [   1    0]
            [     0 E(3)^2], [   0 E(3)]
            ]
            [1, 1, 2, 1, 1]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [E(3)^2      0], [E(3)    0]
            ]
            [1, 1, 2, 1, 2]
            [
            [E(3)^2      0]  [  E(3)      0]
            [     0   E(3)], [     0 E(3)^2]
            ]
            [1, 2, 1, 1, 2]
            [
            [  E(3)      0]  [E(3)^2      0]
            [     0 E(3)^2], [     0   E(3)]
            ]
            [1, 1, 2, 1, 1, 2]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0 E(3)^2], [   0 E(3)]
            ]"""
    @overload
    def to_matrix(self, on_space=...) -> Any:
        """ComplexReflectionGroupElement.to_matrix(self, on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 187)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                                          # optional - gap3
            sage: data = {w: [w.to_matrix(), w.to_matrix(on_space='dual')] for w in W}  # optional - gap3
            sage: for w in W.iteration_tracking_words():                                # optional - gap3
            ....:     w.reduced_word()
            ....:     mats = [w.to_matrix(), w.to_matrix(on_space='dual')]
            ....:     mats
            ....:     assert data[w] == mats
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [1]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0    1], [     0      1]
            ]
            [2]
            [
            [0 1]  [0 1]
            [1 0], [1 0]
            ]
            [1, 1]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0      1], [   0    1]
            ]
            [1, 2]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [   1    0], [     1      0]
            ]
            [2, 1]
            [
            [   0    1]  [     0      1]
            [E(3)    0], [E(3)^2      0]
            ]
            [1, 1, 2]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [     1      0], [   1    0]
            ]
            [1, 2, 1]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [E(3)    0], [E(3)^2      0]
            ]
            [2, 1, 1]
            [
            [     0      1]  [   0    1]
            [E(3)^2      0], [E(3)    0]
            ]
            [2, 1, 2]
            [
            [   1    0]  [     1      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [1, 1, 2, 1]
            [
            [     0 E(3)^2]  [     0   E(3)]
            [  E(3)      0], [E(3)^2      0]
            ]
            [1, 2, 1, 1]
            [
            [     0   E(3)]  [     0 E(3)^2]
            [E(3)^2      0], [  E(3)      0]
            ]
            [1, 2, 1, 2]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [2, 1, 1, 2]
            [
            [     1      0]  [   1    0]
            [     0 E(3)^2], [   0 E(3)]
            ]
            [1, 1, 2, 1, 1]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [E(3)^2      0], [E(3)    0]
            ]
            [1, 1, 2, 1, 2]
            [
            [E(3)^2      0]  [  E(3)      0]
            [     0   E(3)], [     0 E(3)^2]
            ]
            [1, 2, 1, 1, 2]
            [
            [  E(3)      0]  [E(3)^2      0]
            [     0 E(3)^2], [     0   E(3)]
            ]
            [1, 1, 2, 1, 1, 2]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0 E(3)^2], [   0 E(3)]
            ]"""
    @overload
    def to_matrix(self, on_space=...) -> Any:
        """ComplexReflectionGroupElement.to_matrix(self, on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 187)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup((3,1,2))                                          # optional - gap3
            sage: data = {w: [w.to_matrix(), w.to_matrix(on_space='dual')] for w in W}  # optional - gap3
            sage: for w in W.iteration_tracking_words():                                # optional - gap3
            ....:     w.reduced_word()
            ....:     mats = [w.to_matrix(), w.to_matrix(on_space='dual')]
            ....:     mats
            ....:     assert data[w] == mats
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [1]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0    1], [     0      1]
            ]
            [2]
            [
            [0 1]  [0 1]
            [1 0], [1 0]
            ]
            [1, 1]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0      1], [   0    1]
            ]
            [1, 2]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [   1    0], [     1      0]
            ]
            [2, 1]
            [
            [   0    1]  [     0      1]
            [E(3)    0], [E(3)^2      0]
            ]
            [1, 1, 2]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [     1      0], [   1    0]
            ]
            [1, 2, 1]
            [
            [   0 E(3)]  [     0 E(3)^2]
            [E(3)    0], [E(3)^2      0]
            ]
            [2, 1, 1]
            [
            [     0      1]  [   0    1]
            [E(3)^2      0], [E(3)    0]
            ]
            [2, 1, 2]
            [
            [   1    0]  [     1      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [1, 1, 2, 1]
            [
            [     0 E(3)^2]  [     0   E(3)]
            [  E(3)      0], [E(3)^2      0]
            ]
            [1, 2, 1, 1]
            [
            [     0   E(3)]  [     0 E(3)^2]
            [E(3)^2      0], [  E(3)      0]
            ]
            [1, 2, 1, 2]
            [
            [E(3)    0]  [E(3)^2      0]
            [   0 E(3)], [     0 E(3)^2]
            ]
            [2, 1, 1, 2]
            [
            [     1      0]  [   1    0]
            [     0 E(3)^2], [   0 E(3)]
            ]
            [1, 1, 2, 1, 1]
            [
            [     0 E(3)^2]  [   0 E(3)]
            [E(3)^2      0], [E(3)    0]
            ]
            [1, 1, 2, 1, 2]
            [
            [E(3)^2      0]  [  E(3)      0]
            [     0   E(3)], [     0 E(3)^2]
            ]
            [1, 2, 1, 1, 2]
            [
            [  E(3)      0]  [E(3)^2      0]
            [     0 E(3)^2], [     0   E(3)]
            ]
            [1, 1, 2, 1, 1, 2]
            [
            [E(3)^2      0]  [E(3)    0]
            [     0 E(3)^2], [   0 E(3)]
            ]"""
    @overload
    def to_permutation_of_roots(self) -> Any:
        '''ComplexReflectionGroupElement.to_permutation_of_roots(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 467)

        Return ``self`` as a permutation of the roots with indexing
        starting at `1`.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))                      # optional - gap3
            sage: for w in W:       # optional - gap3
            ....:     perm = w.to_permutation_of_roots()
            ....:     print("{} {}".format(perm, perm == w))
            () True
            (1,3)(2,5)(4,6) True
            (1,4)(2,3)(5,6) True
            (1,6,2)(3,5,4) True
            (1,2,6)(3,4,5) True
            (1,5)(2,4)(3,6) True'''
    @overload
    def to_permutation_of_roots(self) -> Any:
        '''ComplexReflectionGroupElement.to_permutation_of_roots(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 467)

        Return ``self`` as a permutation of the roots with indexing
        starting at `1`.

        EXAMPLES::

            sage: W = ReflectionGroup((1,1,3))                      # optional - gap3
            sage: for w in W:       # optional - gap3
            ....:     perm = w.to_permutation_of_roots()
            ....:     print("{} {}".format(perm, perm == w))
            () True
            (1,3)(2,5)(4,6) True
            (1,4)(2,3)(5,6) True
            (1,6,2)(3,5,4) True
            (1,2,6)(3,4,5) True
            (1,5)(2,4)(3,6) True'''
    def __hash__(self) -> Any:
        """ComplexReflectionGroupElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 42)

        Return a hash for this reflection group element.

        This hash stores both the element as a reduced word and the parent group.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',5])                      # optional - gap3
            sage: W_hash = set(hash(w) for w in W)                  # optional - gap3
            sage: len(W_hash) == W.cardinality()                    # optional - gap3
            True

        TESTS:

        Check that types B and C are hashed differently, see :issue:`29726`::

            sage: WB = ReflectionGroup(['B',5])                     # optional - gap3
            sage: WC = ReflectionGroup(['C',5])                     # optional - gap3

            sage: WB_hash = set(hash(w) for w in WB)                # optional - gap3
            sage: WC_hash = set(hash(w) for w in WC)                # optional - gap3

            sage: len(WB_hash) == WB.cardinality()                  # optional - gap3
            True

            sage: len(WC_hash) == WC.cardinality()                  # optional - gap3
            True

            sage: WB_hash.intersection(WC_hash)                     # optional - gap3
            set()

        Check that :issue:`34912` is fixed::

            sage: # optional - gap3
            sage: G4 = ReflectionGroup(4)
            sage: g0, g1 = G4.gens()
            sage: elt = g0^2 * g1 * g0^2 * g1
            sage: elt
            (1,12)(2,24)(3,19)(4,22)(5,17)(6,20)(7,23)(8,9)(10,21)(11,13)(14,18)(15,16)
            sage: y = (elt * G4.gen(1)) * G4.gen(1) * G4.gen(1)
            sage: elt == y
            True
            sage: hash(elt) == hash(y)
            True"""

class RealReflectionGroupElement(ComplexReflectionGroupElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def action(self, vec, side=..., on_space=...) -> Any:
        '''RealReflectionGroupElement.action(self, vec, side=\'right\', on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 965)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``side`` -- (default: ``\'right\'``) whether the
          action of ``self`` is on the ``\'left\'`` or on the ``\'right\'``

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action(weight,side=\'left\') for weight in W.fundamental_weights()]))
            [] [(2/3, 1/3), (1/3, 2/3)]
            [2] [(2/3, 1/3), (1/3, -1/3)]
            [1] [(-1/3, 1/3), (1/3, 2/3)]
            [1, 2] [(-1/3, 1/3), (-2/3, -1/3)]
            [2, 1] [(-1/3, -2/3), (1/3, -1/3)]
            [1, 2, 1] [(-1/3, -2/3), (-2/3, -1/3)]

        TESTS::

            sage: W = ReflectionGroup([\'B\',3])                      # optional - gap3
            sage: all(w.action(alpha,side=\'right\') == w.action_on_root(alpha,side=\'right\')  # optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True
            sage: all(w.action(alpha,side=\'left\') == w.action_on_root(alpha,side=\'left\')  #optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True'''
    @overload
    def action(self, weight, side=...) -> Any:
        '''RealReflectionGroupElement.action(self, vec, side=\'right\', on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 965)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``side`` -- (default: ``\'right\'``) whether the
          action of ``self`` is on the ``\'left\'`` or on the ``\'right\'``

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action(weight,side=\'left\') for weight in W.fundamental_weights()]))
            [] [(2/3, 1/3), (1/3, 2/3)]
            [2] [(2/3, 1/3), (1/3, -1/3)]
            [1] [(-1/3, 1/3), (1/3, 2/3)]
            [1, 2] [(-1/3, 1/3), (-2/3, -1/3)]
            [2, 1] [(-1/3, -2/3), (1/3, -1/3)]
            [1, 2, 1] [(-1/3, -2/3), (-2/3, -1/3)]

        TESTS::

            sage: W = ReflectionGroup([\'B\',3])                      # optional - gap3
            sage: all(w.action(alpha,side=\'right\') == w.action_on_root(alpha,side=\'right\')  # optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True
            sage: all(w.action(alpha,side=\'left\') == w.action_on_root(alpha,side=\'left\')  #optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True'''
    @overload
    def action(self, alpha, side=...) -> Any:
        '''RealReflectionGroupElement.action(self, vec, side=\'right\', on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 965)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``side`` -- (default: ``\'right\'``) whether the
          action of ``self`` is on the ``\'left\'`` or on the ``\'right\'``

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action(weight,side=\'left\') for weight in W.fundamental_weights()]))
            [] [(2/3, 1/3), (1/3, 2/3)]
            [2] [(2/3, 1/3), (1/3, -1/3)]
            [1] [(-1/3, 1/3), (1/3, 2/3)]
            [1, 2] [(-1/3, 1/3), (-2/3, -1/3)]
            [2, 1] [(-1/3, -2/3), (1/3, -1/3)]
            [1, 2, 1] [(-1/3, -2/3), (-2/3, -1/3)]

        TESTS::

            sage: W = ReflectionGroup([\'B\',3])                      # optional - gap3
            sage: all(w.action(alpha,side=\'right\') == w.action_on_root(alpha,side=\'right\')  # optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True
            sage: all(w.action(alpha,side=\'left\') == w.action_on_root(alpha,side=\'left\')  #optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True'''
    @overload
    def action(self, alpha, side=...) -> Any:
        '''RealReflectionGroupElement.action(self, vec, side=\'right\', on_space=\'primal\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 965)

        Return the image of ``vec`` under the action of ``self``.

        INPUT:

        - ``vec`` -- vector in the basis given by the simple root

        - ``side`` -- (default: ``\'right\'``) whether the
          action of ``self`` is on the ``\'left\'`` or on the ``\'right\'``

        - ``on_space`` -- (default: ``\'primal\'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action(weight,side=\'left\') for weight in W.fundamental_weights()]))
            [] [(2/3, 1/3), (1/3, 2/3)]
            [2] [(2/3, 1/3), (1/3, -1/3)]
            [1] [(-1/3, 1/3), (1/3, 2/3)]
            [1, 2] [(-1/3, 1/3), (-2/3, -1/3)]
            [2, 1] [(-1/3, -2/3), (1/3, -1/3)]
            [1, 2, 1] [(-1/3, -2/3), (-2/3, -1/3)]

        TESTS::

            sage: W = ReflectionGroup([\'B\',3])                      # optional - gap3
            sage: all(w.action(alpha,side=\'right\') == w.action_on_root(alpha,side=\'right\')  # optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True
            sage: all(w.action(alpha,side=\'left\') == w.action_on_root(alpha,side=\'left\')  #optional - gap3
            ....:     for w in W for alpha in W.simple_roots())
            True'''
    @overload
    def action_on_root(self, root, side=...) -> Any:
        '''RealReflectionGroupElement.action_on_root(self, root, side=\'right\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1096)

        Return the root obtained by applying ``self`` to ``root``.

        INPUT:

        - ``root`` -- the root to act on

        - ``side`` -- (default: ``\'right\'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'right\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(-1, -1), (1, 0), (0, -1)]
            [2, 1] [(0, 1), (-1, -1), (-1, 0)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]'''
    @overload
    def action_on_root(self, beta, side=...) -> Any:
        '''RealReflectionGroupElement.action_on_root(self, root, side=\'right\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1096)

        Return the root obtained by applying ``self`` to ``root``.

        INPUT:

        - ``root`` -- the root to act on

        - ``side`` -- (default: ``\'right\'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'right\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(-1, -1), (1, 0), (0, -1)]
            [2, 1] [(0, 1), (-1, -1), (-1, 0)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]'''
    @overload
    def action_on_root(self, beta, side=...) -> Any:
        '''RealReflectionGroupElement.action_on_root(self, root, side=\'right\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1096)

        Return the root obtained by applying ``self`` to ``root``.

        INPUT:

        - ``root`` -- the root to act on

        - ``side`` -- (default: ``\'right\'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'left\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(0, 1), (-1, -1), (-1, 0)]
            [2, 1] [(-1, -1), (1, 0), (0, -1)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]

            sage: W = ReflectionGroup([\'A\',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(),
            ....:           [w.action_on_root(beta,side=\'right\') for beta in W.positive_roots()]))
            [] [(1, 0), (0, 1), (1, 1)]
            [2] [(1, 1), (0, -1), (1, 0)]
            [1] [(-1, 0), (1, 1), (0, 1)]
            [1, 2] [(-1, -1), (1, 0), (0, -1)]
            [2, 1] [(0, 1), (-1, -1), (-1, 0)]
            [1, 2, 1] [(0, -1), (-1, 0), (-1, -1)]'''
    @overload
    def action_on_root_indices(self, i, side=...) -> Any:
        """RealReflectionGroupElement.action_on_root_indices(self, i, side='right')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1060)

        Return the action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        - ``side`` -- (default: ``'right'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [4, 3, 5, 1, 0, 2]"""
    @overload
    def action_on_root_indices(self, i, side=...) -> Any:
        """RealReflectionGroupElement.action_on_root_indices(self, i, side='right')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1060)

        Return the action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        - ``side`` -- (default: ``'right'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [4, 3, 5, 1, 0, 2]"""
    @overload
    def action_on_root_indices(self, i, side=...) -> Any:
        """RealReflectionGroupElement.action_on_root_indices(self, i, side='right')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1060)

        Return the action on the set of roots.

        INPUT:

        - ``i`` -- index of the root to act on

        - ``side`` -- (default: ``'right'``) whether the
          action is on the left or on the right

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',3])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [8, 7, 6, 10, 9, 11, 2, 1, 0, 4, 3, 5]

            sage: # optional - gap3
            sage: W = ReflectionGroup(['A',2], reflection_index_set=['A','B','C'])
            sage: w = W.w0
            sage: N = len(W.roots())
            sage: [w.action_on_root_indices(i,side='left') for i in range(N)]
            [4, 3, 5, 1, 0, 2]"""
    def coset_representative(self, index_set, side=...) -> Any:
        """RealReflectionGroupElement.coset_representative(self, index_set, side='right')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 829)

        Return the unique shortest element of the Coxeter group
        `W` which is in the same left (resp. right) coset as
        ``self``, with respect to the parabolic subgroup `W_I`.

        INPUT:

        - ``index_set`` -- a subset (or iterable) of the nodes of the index set
        - ``side`` -- (default: ``right``) ``'left'`` or ``'right'``

        EXAMPLES::

            sage: # needs sage.graphs
            sage: W = CoxeterGroup(['A',4], implementation='permutation')
            sage: s = W.simple_reflections()
            sage: w = s[2] * s[1] * s[3]
            sage: w.coset_representative([]).reduced_word()
            [2, 1, 3]
            sage: w.coset_representative([1]).reduced_word()
            [2, 3]
            sage: w.coset_representative([1,2]).reduced_word()
            [2, 3]
            sage: w.coset_representative([1,3]                 ).reduced_word()
            [2]
            sage: w.coset_representative([2,3]                 ).reduced_word()
            [2, 1]
            sage: w.coset_representative([1,2,3]               ).reduced_word()
            []
            sage: w.coset_representative([],      side = 'left').reduced_word()
            [2, 1, 3]
            sage: w.coset_representative([1],     side = 'left').reduced_word()
            [2, 1, 3]
            sage: w.coset_representative([1,2],   side = 'left').reduced_word()
            [3]
            sage: w.coset_representative([1,3],   side = 'left').reduced_word()
            [2, 1, 3]
            sage: w.coset_representative([2,3],   side = 'left').reduced_word()
            [1]
            sage: w.coset_representative([1,2,3], side = 'left').reduced_word()
            []"""
    def has_descent(self, i, side=..., positive=...) -> bool:
        '''RealReflectionGroupElement.has_descent(self, i, side=\'left\', positive=False) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 791)

        Return whether `i` is a descent (or ascent) of ``self``.

        This is done by testing whether `i` is mapped by ``self``
        to a negative root.

        INPUT:

        - ``i`` -- an index of a simple reflection
        - ``side`` -- (default: ``\'right\'``) ``\'left\'`` or ``\'right\'``
        - ``positive`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(["A",3])
            sage: s = W.simple_reflections()
            sage: (s[1]*s[2]).has_descent(1)
            True
            sage: (s[1]*s[2]).has_descent(2)
            False'''
    def has_left_descent(self, i) -> bool:
        '''RealReflectionGroupElement.has_left_descent(self, i) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 770)

        Return whether ``i`` is a left descent of ``self``.

        This is done by testing whether ``i`` is mapped by ``self``
        to a negative root.

        EXAMPLES::

            sage: # optional - gap3
            sage: W = ReflectionGroup(["A",3])
            sage: s = W.simple_reflections()
            sage: (s[1]*s[2]).has_left_descent(1)
            True
            sage: (s[1]*s[2]).has_left_descent(2)
            False'''
    def inversion_set(self, side=...) -> Any:
        '''RealReflectionGroupElement.inversion_set(self, side=\'right\')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 1134)

        Return the inversion set of ``self``.

        This is the set `\\{\\beta \\in \\Phi^+ : s(\\beta) \\in \\Phi^-\\}`,
        where `s` is ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(), w.inversion_set()))
            [] []
            [2] [(0, 1)]
            [1] [(1, 0)]
            [1, 2] [(1, 0), (1, 1)]
            [2, 1] [(0, 1), (1, 1)]
            [1, 2, 1] [(1, 0), (0, 1), (1, 1)]

            sage: W.from_reduced_word([1,2]).inversion_set(side=\'left\') # optional - gap3
            [(0, 1), (1, 1)]'''
    @overload
    def length(self) -> Any:
        '''RealReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 749)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(), w.length()))
            [] 0
            [2] 1
            [1] 1
            [1, 2] 2
            [2, 1] 2
            [1, 2, 1] 3'''
    @overload
    def length(self) -> Any:
        '''RealReflectionGroupElement.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 749)

        Return the length of ``self`` in generating reflections.

        This is the minimal numbers of generating reflections needed
        to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',2])                      # optional - gap3
            sage: for w in W:                                       # optional - gap3
            ....:     print("%s %s"%(w.reduced_word(), w.length()))
            [] 0
            [2] 1
            [1] 1
            [1, 2] 2
            [2, 1] 2
            [1, 2, 1] 3'''
    def matrix(self, *args, **kwargs):
        """RealReflectionGroupElement.to_matrix(self, side='right', on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 876)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``side`` -- (default: ``'right'``) whether the
          action of ``self`` is on the ``'left'`` or on the ``'right'``

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     w.reduced_word()
            ....:     [w.to_matrix(), w.to_matrix(on_space='dual')]
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [2]
            [
            [ 1  1]  [ 1  0]
            [ 0 -1], [ 1 -1]
            ]
            [1]
            [
            [-1  0]  [-1  1]
            [ 1  1], [ 0  1]
            ]
            [1, 2]
            [
            [-1 -1]  [ 0 -1]
            [ 1  0], [ 1 -1]
            ]
            [2, 1]
            [
            [ 0  1]  [-1  1]
            [-1 -1], [-1  0]
            ]
            [1, 2, 1]
            [
            [ 0 -1]  [ 0 -1]
            [-1  0], [-1  0]
            ]

        TESTS::

            sage: W = ReflectionGroup(['F',4])           # optional - gap3
            sage: all(w.to_matrix(side='left') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='right').transpose() for w in W) # optional - gap3
            True
            sage: all(w.to_matrix(side='right') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='left').transpose() for w in W) # optional - gap3
            True"""
    @overload
    def reduced_word_in_reflections(self) -> Any:
        """RealReflectionGroupElement.reduced_word_in_reflections(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 713)

        Return a word in the reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2], index_set=['a','b'], reflection_index_set=['A','B','C']) # optional - gap3
            sage: [(w.reduced_word(), w.reduced_word_in_reflections()) for w in W]  # optional - gap3
            [([], []),
             (['b'], ['B']),
             (['a'], ['A']),
             (['a', 'b'], ['A', 'B']),
             (['b', 'a'], ['A', 'C']),
             (['a', 'b', 'a'], ['C'])]

        .. SEEALSO:: :meth:`reduced_word`"""
    @overload
    def reduced_word_in_reflections(self) -> Any:
        """RealReflectionGroupElement.reduced_word_in_reflections(self)

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 713)

        Return a word in the reflections to obtain ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2], index_set=['a','b'], reflection_index_set=['A','B','C']) # optional - gap3
            sage: [(w.reduced_word(), w.reduced_word_in_reflections()) for w in W]  # optional - gap3
            [([], []),
             (['b'], ['B']),
             (['a'], ['A']),
             (['a', 'b'], ['A', 'B']),
             (['b', 'a'], ['A', 'C']),
             (['a', 'b', 'a'], ['C'])]

        .. SEEALSO:: :meth:`reduced_word`"""
    @overload
    def to_matrix(self, side=..., on_space=...) -> Any:
        """RealReflectionGroupElement.to_matrix(self, side='right', on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 876)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``side`` -- (default: ``'right'``) whether the
          action of ``self`` is on the ``'left'`` or on the ``'right'``

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     w.reduced_word()
            ....:     [w.to_matrix(), w.to_matrix(on_space='dual')]
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [2]
            [
            [ 1  1]  [ 1  0]
            [ 0 -1], [ 1 -1]
            ]
            [1]
            [
            [-1  0]  [-1  1]
            [ 1  1], [ 0  1]
            ]
            [1, 2]
            [
            [-1 -1]  [ 0 -1]
            [ 1  0], [ 1 -1]
            ]
            [2, 1]
            [
            [ 0  1]  [-1  1]
            [-1 -1], [-1  0]
            ]
            [1, 2, 1]
            [
            [ 0 -1]  [ 0 -1]
            [-1  0], [-1  0]
            ]

        TESTS::

            sage: W = ReflectionGroup(['F',4])           # optional - gap3
            sage: all(w.to_matrix(side='left') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='right').transpose() for w in W) # optional - gap3
            True
            sage: all(w.to_matrix(side='right') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='left').transpose() for w in W) # optional - gap3
            True"""
    @overload
    def to_matrix(self, on_space=...) -> Any:
        """RealReflectionGroupElement.to_matrix(self, side='right', on_space='primal')

        File: /build/sagemath/src/sage/src/sage/combinat/root_system/reflection_group_element.pyx (starting at line 876)

        Return ``self`` as a matrix acting on the underlying vector
        space.

        - ``side`` -- (default: ``'right'``) whether the
          action of ``self`` is on the ``'left'`` or on the ``'right'``

        - ``on_space`` -- (default: ``'primal'``) whether
          to act as the reflection representation on the given
          basis, or to act on the dual reflection representation
          on the dual basis

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])           # optional - gap3
            sage: for w in W:                            # optional - gap3
            ....:     w.reduced_word()
            ....:     [w.to_matrix(), w.to_matrix(on_space='dual')]
            []
            [
            [1 0]  [1 0]
            [0 1], [0 1]
            ]
            [2]
            [
            [ 1  1]  [ 1  0]
            [ 0 -1], [ 1 -1]
            ]
            [1]
            [
            [-1  0]  [-1  1]
            [ 1  1], [ 0  1]
            ]
            [1, 2]
            [
            [-1 -1]  [ 0 -1]
            [ 1  0], [ 1 -1]
            ]
            [2, 1]
            [
            [ 0  1]  [-1  1]
            [-1 -1], [-1  0]
            ]
            [1, 2, 1]
            [
            [ 0 -1]  [ 0 -1]
            [-1  0], [-1  0]
            ]

        TESTS::

            sage: W = ReflectionGroup(['F',4])           # optional - gap3
            sage: all(w.to_matrix(side='left') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='right').transpose() for w in W) # optional - gap3
            True
            sage: all(w.to_matrix(side='right') == W.from_reduced_word(reversed(w.reduced_word())).to_matrix(side='left').transpose() for w in W) # optional - gap3
            True"""
