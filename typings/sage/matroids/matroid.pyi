import sage.structure.sage_object
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matrix.constructor import matrix as matrix
from sage.matroids.utilities import cmp_elements_key as cmp_elements_key, newlabel as newlabel, sanitize_contractions_deletions as sanitize_contractions_deletions, spanning_forest as spanning_forest, spanning_stars as spanning_stars
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.misc.prandom import shuffle as shuffle
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias, deprecation as deprecation
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class Matroid(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 368)

        The abstract matroid class, from which all matroids are derived. Do not
        use this class directly!

        To implement a subclass, the least you should do is implement the
        ``__init__()``, ``_rank()`` and ``groundset()`` methods. See the source of
        :mod:`rank_matroid.py <sage.matroids.rank_matroid>` for a bare-bones
        example of this.

        EXAMPLES:

        In a partition matroid, a subset is independent if it has at most one
        element from each partition. The following is a very basic implementation,
        in which the partition is specified as a list of lists::

            sage: class PartitionMatroid(sage.matroids.matroid.Matroid):
            ....:     def __init__(self, partition):
            ....:         self.partition = partition
            ....:         E = set()
            ....:         for P in partition:
            ....:             E.update(P)
            ....:         self.E = frozenset(E)
            ....:     def groundset(self):
            ....:         return self.E
            ....:     def _rank(self, X):
            ....:         X2 = set(X)
            ....:         used_indices = set()
            ....:         r = 0
            ....:         while X2:
            ....:             e = X2.pop()
            ....:             for i in range(len(self.partition)):
            ....:                 if e in self.partition[i]:
            ....:                     if i not in used_indices:
            ....:                         used_indices.add(i)
            ....:                         r = r + 1
            ....:                     break
            ....:         return r
            ....:
            sage: M = PartitionMatroid([[1, 2], [3, 4, 5], [6, 7]])
            sage: M.full_rank()
            3
            sage: M.tutte_polynomial(var('x'), var('y'))                                    # needs sage.symbolic
            x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 3*x^2*y + 3*x*y^2 + y^3

        .. NOTE::

            The abstract base class has no idea about the data used to represent
            the matroid. Hence some methods need to be customized to function
            properly.

            Necessary:

            - ``def __init__(self, ...)``
            - ``def groundset(self)``
            - ``def _rank(self, X)``

            Representation:

            - ``def _repr_(self)``

            Comparison:

            - ``def __hash__(self)``
            - ``def __eq__(self, other)``
            - ``def __ne__(self, other)``

            In Cythonized classes, use ``__richcmp__()`` instead of ``__eq__()``,
            ``__ne__()``.

            Copying, loading, saving:

            - ``def __copy__(self)``
            - ``def __deepcopy__(self, memo={})``
            - ``def __reduce__(self)``

            See, for instance,
            :mod:`rank_matroid.py <sage.matroids.rank_matroid>` or
            :mod:`circuit_closures_matroid.pyx <sage.matroids.circuit_closures_matroid>`
            for sample implementations of these.

        .. NOTE::

            Many methods (such as ``M.rank()``) have a companion method whose name
            starts with an underscore (such as ``M._rank()``). The method with the
            underscore does not do any checks on its input. For instance, it may
            assume of its input that

            - Any input that should be a subset of the groundset, is one. The
              interface is compatible with Python's ``frozenset`` type.
            - Any input that should be a list of things, supports iteration, and
              recursively these rules apply to its members.

            Using the underscored version could improve the speed of code a
            little, but will generate more cryptic error messages when presented
            with wrong input. In some instances, no error might occur and a
            nonsensical answer returned.

            A subclass should always override the underscored method, if
            available, and as a rule leave the regular method alone.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def augment(self, X, Y=...) -> Any:
        """Matroid.augment(self, X, Y=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1643)

        Return a maximal subset `I` of `Y - X` such that
        `r(X + I) = r(X) + r(I)`.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset
        - ``Y`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a subset of `Y - X`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: X = set(['a']); Y = M.groundset()
            sage: Z = M.augment(X, Y)
            sage: M.is_independent(Z.union(X))
            True
            sage: W = Z.union(X)
            sage: all(M.is_dependent(W.union([y])) for y in Y if y not in W)
            True
            sage: sorted(M.augment(['x']))
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: sorted(M.augment(['a'], ['x']))
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    @overload
    def augment(self, X, Y) -> Any:
        """Matroid.augment(self, X, Y=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1643)

        Return a maximal subset `I` of `Y - X` such that
        `r(X + I) = r(X) + r(I)`.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset
        - ``Y`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a subset of `Y - X`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: X = set(['a']); Y = M.groundset()
            sage: Z = M.augment(X, Y)
            sage: M.is_independent(Z.union(X))
            True
            sage: W = Z.union(X)
            sage: all(M.is_dependent(W.union([y])) for y in Y if y not in W)
            True
            sage: sorted(M.augment(['x']))
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: sorted(M.augment(['a'], ['x']))
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    def augmented_bergman_complex(self) -> Any:
        """Matroid.augmented_bergman_complex(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8402)

        Return the augmented Bergman complex of ``self``.

        Given a matroid `M` with groundset `E=\\{1,2,\\ldots,n\\}`,
        the *augmented Bergman complex* can be seen as a hybrid of the complex
        of independent sets of `M` and the Bergman complex of `M`. It is
        defined as the simplicial complex on vertex set

        .. MATH::

            \\{y_1,\\ldots,y_n\\}\\cup\\{x_F:\\text{ proper flats } F\\subsetneq E\\},

        with simplices given by

        .. MATH::

            \\{y_i\\}_{i\\in I}\\cup\\{x_{F_1},\\ldots,x_{F_\\ell}\\},

        for which `I` is an independent set and `I\\subseteq F_1\\subsetneq F_2
        \\subsetneq\\cdots\\subsetneq F_\\ell`.

        OUTPUT: a simplicial complex

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: A = M.augmented_bergman_complex(); A                                  # needs sage.graphs
            Simplicial complex with 22 vertices and 91 facets

            sage: M = matroids.Uniform(2,3)
            sage: A = M.augmented_bergman_complex(); A                                  # needs sage.graphs
            Simplicial complex with 7 vertices and 9 facets

        Both the independent set complex of the matroid and the usual
        Bergman complex are subcomplexes of the augmented Bergman complex.
        The vertices of the complex are labeled by ``L`` when they belong
        to the independent set complex and ``R`` when they belong to the
        (cone of) the Bergman complex. The cone point is ``'R[]'``::

            sage: sorted(A.faces()[0])                                                  # needs sage.graphs
            [('L0',), ('L1',), ('L2',), ('R[0]',), ('R[1]',), ('R[2]',), ('R[]',)]
            sage: sorted(map(sorted, A.faces()[1]))                                     # needs sage.graphs
            [['L0', 'L1'],
             ['L0', 'L2'],
             ['L0', 'R[0]'],
             ['L1', 'L2'],
             ['L1', 'R[1]'],
             ['L2', 'R[2]'],
             ['R[0]', 'R[]'],
             ['R[1]', 'R[]'],
             ['R[2]', 'R[]']]

        .. SEEALSO::

            :meth:`M.bergman_complex() <sage.matroids.matroid.Matroid.bergman_complex>`

        .. TODO::

            It is possible that this method could be optimized by building up
            the maximal chains using a sort of dynamic programming approach.

        REFERENCES:

        - [BHMPW20a]_
        - [BHMPW20b]_"""
    def automorphism_group(self) -> Any:
        """Matroid.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8344)

        Return the automorphism group of ``self``.

        For a matroid `M`, an automorphism is a permutation `\\sigma` of `E(M)`
        (the groundset) such that `r(X) = r(\\sigma(X))` for all `X \\subseteq
        E(M)`. The set of automorphisms of `M` forms a group under composition.
        This automorphism group is transitive if, for every two elements `x`
        and `y` of `M`, there is an automorphism that maps `x` to `y`.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: G = M.automorphism_group()
            sage: G.is_transitive()
            True
            sage: G.structure_description()
            'PSL(3,2)'
            sage: M = matroids.catalog.P8pp()
            sage: M.automorphism_group().is_transitive()
            True
            sage: M = matroids.catalog.ExtendedTernaryGolayCode()
            sage: G = M.automorphism_group()
            sage: G.is_transitive()
            True
            sage: G.structure_description()
            'M12'

        REFERENCES:

        [Oxl2011]_, p. 189."""
    @overload
    def bases(self) -> SetSystem:
        """Matroid.bases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2756)

        Return the bases of the matroid.

        A *basis* is a maximal independent set.

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: sorted([sorted(X) for X in M.bases()])
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``

        .. SEEALSO::

            :meth:`M.independent_sets() <sage.matroids.matroid.Matroid.independent_sets>`"""
    @overload
    def bases(self) -> Any:
        """Matroid.bases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2756)

        Return the bases of the matroid.

        A *basis* is a maximal independent set.

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: sorted([sorted(X) for X in M.bases()])
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``

        .. SEEALSO::

            :meth:`M.independent_sets() <sage.matroids.matroid.Matroid.independent_sets>`"""
    @overload
    def bases_iterator(self) -> Any:
        """Matroid.bases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2780)

        Return an iterator over the bases of the matroid.

        A *basis* is a maximal independent set.

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``.

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: sorted([sorted(X) for X in M.bases_iterator()])
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

        .. SEEALSO::

            :meth:`M.independent_sets_iterator() <sage.matroids.matroid.Matroid.independent_sets_iterator>`"""
    @overload
    def bases_iterator(self) -> Any:
        """Matroid.bases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2780)

        Return an iterator over the bases of the matroid.

        A *basis* is a maximal independent set.

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``.

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: sorted([sorted(X) for X in M.bases_iterator()])
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

        .. SEEALSO::

            :meth:`M.independent_sets_iterator() <sage.matroids.matroid.Matroid.independent_sets_iterator>`"""
    @overload
    def basis(self) -> Any:
        """Matroid.basis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1442)

        Return an arbitrary basis of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. NOTE::

            The output of this method can change in between calls.

        OUTPUT: a set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: B = M.basis()
            sage: M.is_basis(B)
            True
            sage: len(B)
            3
            sage: M.rank(B)
            3
            sage: M.full_rank()
            3"""
    @overload
    def basis(self) -> Any:
        """Matroid.basis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1442)

        Return an arbitrary basis of the matroid.

        A *basis* is an inclusionwise maximal independent set.

        .. NOTE::

            The output of this method can change in between calls.

        OUTPUT: a set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: B = M.basis()
            sage: M.is_basis(B)
            True
            sage: len(B)
            3
            sage: M.rank(B)
            3
            sage: M.full_rank()
            3"""
    @overload
    def bergman_complex(self) -> Any:
        """Matroid.bergman_complex(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8379)

        Return the Bergman complex of ``self``.

        Let `L` be the lattice of flats of a matroid `M` with the minimum and
        maximum elements removed. The *Bergman complex* of a matroid `M` is the
        order complex of `L`.

        OUTPUT: a simplicial complex

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: B = M.bergman_complex(); B                                            # needs sage.graphs
            Simplicial complex with 14 vertices and 21 facets

        .. SEEALSO::

            :meth:`M.augmented_bergman_complex() <sage.matroids.matroid.Matroid.augmented_bergman_complex>`"""
    @overload
    def bergman_complex(self) -> Any:
        """Matroid.bergman_complex(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8379)

        Return the Bergman complex of ``self``.

        Let `L` be the lattice of flats of a matroid `M` with the minimum and
        maximum elements removed. The *Bergman complex* of a matroid `M` is the
        order complex of `L`.

        OUTPUT: a simplicial complex

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: B = M.bergman_complex(); B                                            # needs sage.graphs
            Simplicial complex with 14 vertices and 21 facets

        .. SEEALSO::

            :meth:`M.augmented_bergman_complex() <sage.matroids.matroid.Matroid.augmented_bergman_complex>`"""
    @overload
    def binary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """Matroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6335)

        Return a binary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a binary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is binary

        OUTPUT: either a :class:`BinaryMatroid`, or ``None``

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a binary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.local_binary_matroid()
            <sage.matroids.matroid.Matroid._local_binary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.binary_matroid()
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: N = matroids.catalog.NonFano()
            sage: N.binary_matroid() is None
            True"""
    @overload
    def binary_matroid(self) -> Any:
        """Matroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6335)

        Return a binary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a binary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is binary

        OUTPUT: either a :class:`BinaryMatroid`, or ``None``

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a binary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.local_binary_matroid()
            <sage.matroids.matroid.Matroid._local_binary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.binary_matroid()
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: N = matroids.catalog.NonFano()
            sage: N.binary_matroid() is None
            True"""
    @overload
    def binary_matroid(self) -> Any:
        """Matroid.binary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6335)

        Return a binary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a binary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is binary

        OUTPUT: either a :class:`BinaryMatroid`, or ``None``

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a binary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.local_binary_matroid()
            <sage.matroids.matroid.Matroid._local_binary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.binary_matroid()
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: N = matroids.catalog.NonFano()
            sage: N.binary_matroid() is None
            True"""
    @overload
    def broken_circuit_complex(self, ordering=...) -> Any:
        """Matroid.broken_circuit_complex(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8289)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: M.broken_circuit_complex()                                            # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5,4,3,2,1])                                 # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(flats={0: ['a'], 1: ['ab', 'ac'], 2: ['abc']})
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined

        TESTS::

            sage: for M in matroids.AllMatroids(5):  # optional - matroid_database
            ....:     r = M.rank()
            ....:     if r > 0 and not M.dual().loops():
            ....:         C = SimplicialComplex(M.bases(), maximality_check=False)
            ....:         betti = C.betti()
            ....:         betti[0] -= 1  # reduced homology
            ....:         assert betti[r-1] == len(M.dual().broken_circuit_complex().facets())"""
    @overload
    def broken_circuit_complex(self) -> Any:
        """Matroid.broken_circuit_complex(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8289)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: M.broken_circuit_complex()                                            # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5,4,3,2,1])                                 # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(flats={0: ['a'], 1: ['ab', 'ac'], 2: ['abc']})
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined

        TESTS::

            sage: for M in matroids.AllMatroids(5):  # optional - matroid_database
            ....:     r = M.rank()
            ....:     if r > 0 and not M.dual().loops():
            ....:         C = SimplicialComplex(M.bases(), maximality_check=False)
            ....:         betti = C.betti()
            ....:         betti[0] -= 1  # reduced homology
            ....:         assert betti[r-1] == len(M.dual().broken_circuit_complex().facets())"""
    @overload
    def broken_circuit_complex(self) -> Any:
        """Matroid.broken_circuit_complex(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8289)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: M.broken_circuit_complex()                                            # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5,4,3,2,1])                                 # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(flats={0: ['a'], 1: ['ab', 'ac'], 2: ['abc']})
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined

        TESTS::

            sage: for M in matroids.AllMatroids(5):  # optional - matroid_database
            ....:     r = M.rank()
            ....:     if r > 0 and not M.dual().loops():
            ....:         C = SimplicialComplex(M.bases(), maximality_check=False)
            ....:         betti = C.betti()
            ....:         betti[0] -= 1  # reduced homology
            ....:         assert betti[r-1] == len(M.dual().broken_circuit_complex().facets())"""
    @overload
    def broken_circuit_complex(self) -> Any:
        """Matroid.broken_circuit_complex(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8289)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: M.broken_circuit_complex()                                            # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5,4,3,2,1])                                 # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(flats={0: ['a'], 1: ['ab', 'ac'], 2: ['abc']})
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined

        TESTS::

            sage: for M in matroids.AllMatroids(5):  # optional - matroid_database
            ....:     r = M.rank()
            ....:     if r > 0 and not M.dual().loops():
            ....:         C = SimplicialComplex(M.bases(), maximality_check=False)
            ....:         betti = C.betti()
            ....:         betti[0] -= 1  # reduced homology
            ....:         assert betti[r-1] == len(M.dual().broken_circuit_complex().facets())"""
    def broken_circuits(self, ordering=...) -> SetSystem:
        """Matroid.broken_circuits(self, ordering=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3167)

        Return the broken circuits of ``self``.

        Let `M` be a matroid with groundset `E`, and let `<` be a total
        ordering on `E`. A *broken circuit* for `M` means a subset `B` of
        `E` such that there exists a `u \\in E` for which `B \\cup \\{ u \\}`
        is a circuit of `M` and `u < b` for all `b \\in B`.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: sorted([sorted(X) for X in M.broken_circuits()])
            [[2, 3], [2, 4, 5], [4, 5]]
            sage: sorted([sorted(X) for X in M.broken_circuits([5,4,3,2,1])])
            [[1, 2], [1, 2, 4], [3, 4]]

        ::

            sage: M = Matroid(circuits=[[1,2,3], [1,4,5], [2,3,4,5]])
            sage: sorted([sorted(X) for X in M.broken_circuits([5,4,3,2,1])])
            [[1, 2], [1, 4], [2, 3, 4]]"""
    def characteristic_polynomial(self, la=...) -> Any:
        """Matroid.characteristic_polynomial(self, la=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7942)

        Return the characteristic polynomial of the matroid.

        The *characteristic polynomial* of a matroid `M` is the polynomial

        .. MATH::

            \\chi_M(\\lambda) = \\sum_{S \\subseteq E} (-1)^{|S|}\\lambda^{r(E)-r(S)},

        where `E` is the groundset and `r` is the matroid's rank function. The
        characteristic polynomial is also equal to
        `\\sum_{i = 0}^r w_i\\lambda^{r-i}`, where `\\{w_i\\}_{i=0}^r` are the
        Whitney numbers of the first kind.

        INPUT:

        - ``la`` -- a variable or numerical argument (optional)

        OUTPUT: the characteristic polynomial, `\\chi_M(\\lambda)`, where
        `\\lambda` is substituted with any value provided as input

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(5)
            sage: M.characteristic_polynomial()
            l^4 - 10*l^3 + 35*l^2 - 50*l + 24
            sage: M.characteristic_polynomial().factor()
            (l - 4) * (l - 3) * (l - 2) * (l - 1)
            sage: M.characteristic_polynomial(5)
            24

        .. SEEALSO::

            :meth:`~sage.matroids.matroid.Matroid.whitney_numbers`

        TESTS::

            sage: M = Matroid(groundset=[0,1,2], circuits=[[0]])
            sage: M.characteristic_polynomial()
            0
            sage: l = -1
            sage: for M in matroids.AllMatroids(6):  # optional - matroid_database
            ....:     r = M.rank()
            ....:     assert M.characteristic_polynomial(l) == (-1)**r * M.tutte_polynomial(1 - l, 0)
            ....:     if not M.loops():
            ....:         assert (-1)**r * M.characteristic_polynomial(l) == sum(M.broken_circuit_complex().f_vector())"""
    @overload
    def chordality(self) -> Any:
        """Matroid.chordality(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6848)

        Return the minimal `k` such that the matroid ``M`` is `k`-chordal.

        .. SEEALSO::

            :meth:`M.is_chordal() <sage.matroids.matroid.Matroid.is_chordal>`

        EXAMPLES::

            sage: M = matroids.Uniform(2,4)
            sage: M.chordality()
            4
            sage: M = matroids.catalog.NonFano()
            sage: M.chordality()
            5
            sage: M = matroids.catalog.Fano()
            sage: M.chordality()
            4"""
    @overload
    def chordality(self) -> Any:
        """Matroid.chordality(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6848)

        Return the minimal `k` such that the matroid ``M`` is `k`-chordal.

        .. SEEALSO::

            :meth:`M.is_chordal() <sage.matroids.matroid.Matroid.is_chordal>`

        EXAMPLES::

            sage: M = matroids.Uniform(2,4)
            sage: M.chordality()
            4
            sage: M = matroids.catalog.NonFano()
            sage: M.chordality()
            5
            sage: M = matroids.catalog.Fano()
            sage: M.chordality()
            4"""
    @overload
    def chordality(self) -> Any:
        """Matroid.chordality(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6848)

        Return the minimal `k` such that the matroid ``M`` is `k`-chordal.

        .. SEEALSO::

            :meth:`M.is_chordal() <sage.matroids.matroid.Matroid.is_chordal>`

        EXAMPLES::

            sage: M = matroids.Uniform(2,4)
            sage: M.chordality()
            4
            sage: M = matroids.catalog.NonFano()
            sage: M.chordality()
            5
            sage: M = matroids.catalog.Fano()
            sage: M.chordality()
            4"""
    @overload
    def chordality(self) -> Any:
        """Matroid.chordality(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6848)

        Return the minimal `k` such that the matroid ``M`` is `k`-chordal.

        .. SEEALSO::

            :meth:`M.is_chordal() <sage.matroids.matroid.Matroid.is_chordal>`

        EXAMPLES::

            sage: M = matroids.Uniform(2,4)
            sage: M.chordality()
            4
            sage: M = matroids.catalog.NonFano()
            sage: M.chordality()
            5
            sage: M = matroids.catalog.Fano()
            sage: M.chordality()
            4"""
    @overload
    def chow_ring(self, R, augmented=..., presentation=...) -> Any:
        '''Matroid.chow_ring(self, R, augmented=False, presentation=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8054)

        Return the (augmented) Chow ring of ``self`` over ``R``.

        .. SEEALSO::

            - :mod:`sage.matroids.chow_ring_ideal`
            - :mod:`sage.matroids.chow_ring`

        INPUT:

        - ``M`` -- matroid
        - ``R`` -- commutative ring
        - ``augmented`` -- boolean (default: ``False``); when ``True``, this
          is the augmented Chow ring and if ``False``, this is the
          non-augmented Chow ring
        - ``presentation`` -- string; one of the following:

          * ``"fy"`` - the Feitchner-Yuzvinsky presentation
          * ``"atom-free"`` - the atom-free presentation
          * ``"simplicial"`` - the simplicial presentation

        EXAMPLES::

            sage: M = matroids.Wheel(2)
            sage: A = M.chow_ring(R=ZZ, augmented=False, presentation=\'fy\'); A
            Chow ring of Wheel(2): Regular matroid of rank 2 on 4 elements with
            5 bases in Feitchner-Yuzvinsky presentation over Integer Ring
            sage: A.defining_ideal()._gens_constructor(A.defining_ideal().ring())
            [A0*A1, A0*A23, A1*A23, A0 + A0123, A1 + A0123, A23 + A0123]
            sage: A23 = A.gen(0)
            sage: A23*A23
            0

        We construct a more interesting example using the Fano matroid::

            sage: M = matroids.catalog.Fano()
            sage: A = M.chow_ring(QQ, False, \'fy\'); A
            Chow ring of Fano: Binary matroid of rank 3 on 7 elements,
            type (3, 0) in Feitchner-Yuzvinsky presentation over Rational Field

        Next we get the non-trivial generators and do some computations::

            sage: # needs sage.libs.singular sage.rings.finite_rings
            sage: G = A.gens()[7:]; G
            (Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg)
            sage: Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg = G
            sage: Aabf*Aabf
            -Aabcdefg^2
            sage: Aabf*Acfg
            0
            sage: matrix([[x * y for x in G] for y in G])
            [-Aabcdefg^2           0           0           0           0           0           0           0]
            [          0 -Aabcdefg^2           0           0           0           0           0           0]
            [          0           0 -Aabcdefg^2           0           0           0           0           0]
            [          0           0           0 -Aabcdefg^2           0           0           0           0]
            [          0           0           0           0 -Aabcdefg^2           0           0           0]
            [          0           0           0           0           0 -Aabcdefg^2           0           0]
            [          0           0           0           0           0           0 -Aabcdefg^2           0]
            [          0           0           0           0           0           0           0  Aabcdefg^2]

        The augmented Chow ring can also be constructed with the
        Feitchner-Yuzvinsky and atom-free presentation::

            sage: M = matroids.Wheel(3)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'fy\'); ch
            Augmented Chow ring of Wheel(3): Regular matroid of rank 3 on
            6 elements with 16 bases in Feitchner-Yuzvinsky presentation over
            Rational Field
            sage: M = matroids.Uniform(3, 6)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'atom-free\'); ch
            Augmented Chow ring of U(3, 6): Matroid of rank 3 on 6 elements with circuit-closures
            {3: {{0, 1, 2, 3, 4, 5}}} in atom-free presentation over Rational Field'''
    @overload
    def chow_ring(self, R=..., augmented=..., presentation=...) -> Any:
        '''Matroid.chow_ring(self, R, augmented=False, presentation=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8054)

        Return the (augmented) Chow ring of ``self`` over ``R``.

        .. SEEALSO::

            - :mod:`sage.matroids.chow_ring_ideal`
            - :mod:`sage.matroids.chow_ring`

        INPUT:

        - ``M`` -- matroid
        - ``R`` -- commutative ring
        - ``augmented`` -- boolean (default: ``False``); when ``True``, this
          is the augmented Chow ring and if ``False``, this is the
          non-augmented Chow ring
        - ``presentation`` -- string; one of the following:

          * ``"fy"`` - the Feitchner-Yuzvinsky presentation
          * ``"atom-free"`` - the atom-free presentation
          * ``"simplicial"`` - the simplicial presentation

        EXAMPLES::

            sage: M = matroids.Wheel(2)
            sage: A = M.chow_ring(R=ZZ, augmented=False, presentation=\'fy\'); A
            Chow ring of Wheel(2): Regular matroid of rank 2 on 4 elements with
            5 bases in Feitchner-Yuzvinsky presentation over Integer Ring
            sage: A.defining_ideal()._gens_constructor(A.defining_ideal().ring())
            [A0*A1, A0*A23, A1*A23, A0 + A0123, A1 + A0123, A23 + A0123]
            sage: A23 = A.gen(0)
            sage: A23*A23
            0

        We construct a more interesting example using the Fano matroid::

            sage: M = matroids.catalog.Fano()
            sage: A = M.chow_ring(QQ, False, \'fy\'); A
            Chow ring of Fano: Binary matroid of rank 3 on 7 elements,
            type (3, 0) in Feitchner-Yuzvinsky presentation over Rational Field

        Next we get the non-trivial generators and do some computations::

            sage: # needs sage.libs.singular sage.rings.finite_rings
            sage: G = A.gens()[7:]; G
            (Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg)
            sage: Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg = G
            sage: Aabf*Aabf
            -Aabcdefg^2
            sage: Aabf*Acfg
            0
            sage: matrix([[x * y for x in G] for y in G])
            [-Aabcdefg^2           0           0           0           0           0           0           0]
            [          0 -Aabcdefg^2           0           0           0           0           0           0]
            [          0           0 -Aabcdefg^2           0           0           0           0           0]
            [          0           0           0 -Aabcdefg^2           0           0           0           0]
            [          0           0           0           0 -Aabcdefg^2           0           0           0]
            [          0           0           0           0           0 -Aabcdefg^2           0           0]
            [          0           0           0           0           0           0 -Aabcdefg^2           0]
            [          0           0           0           0           0           0           0  Aabcdefg^2]

        The augmented Chow ring can also be constructed with the
        Feitchner-Yuzvinsky and atom-free presentation::

            sage: M = matroids.Wheel(3)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'fy\'); ch
            Augmented Chow ring of Wheel(3): Regular matroid of rank 3 on
            6 elements with 16 bases in Feitchner-Yuzvinsky presentation over
            Rational Field
            sage: M = matroids.Uniform(3, 6)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'atom-free\'); ch
            Augmented Chow ring of U(3, 6): Matroid of rank 3 on 6 elements with circuit-closures
            {3: {{0, 1, 2, 3, 4, 5}}} in atom-free presentation over Rational Field'''
    @overload
    def chow_ring(self, QQ, augmented=..., presentation=...) -> Any:
        '''Matroid.chow_ring(self, R, augmented=False, presentation=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8054)

        Return the (augmented) Chow ring of ``self`` over ``R``.

        .. SEEALSO::

            - :mod:`sage.matroids.chow_ring_ideal`
            - :mod:`sage.matroids.chow_ring`

        INPUT:

        - ``M`` -- matroid
        - ``R`` -- commutative ring
        - ``augmented`` -- boolean (default: ``False``); when ``True``, this
          is the augmented Chow ring and if ``False``, this is the
          non-augmented Chow ring
        - ``presentation`` -- string; one of the following:

          * ``"fy"`` - the Feitchner-Yuzvinsky presentation
          * ``"atom-free"`` - the atom-free presentation
          * ``"simplicial"`` - the simplicial presentation

        EXAMPLES::

            sage: M = matroids.Wheel(2)
            sage: A = M.chow_ring(R=ZZ, augmented=False, presentation=\'fy\'); A
            Chow ring of Wheel(2): Regular matroid of rank 2 on 4 elements with
            5 bases in Feitchner-Yuzvinsky presentation over Integer Ring
            sage: A.defining_ideal()._gens_constructor(A.defining_ideal().ring())
            [A0*A1, A0*A23, A1*A23, A0 + A0123, A1 + A0123, A23 + A0123]
            sage: A23 = A.gen(0)
            sage: A23*A23
            0

        We construct a more interesting example using the Fano matroid::

            sage: M = matroids.catalog.Fano()
            sage: A = M.chow_ring(QQ, False, \'fy\'); A
            Chow ring of Fano: Binary matroid of rank 3 on 7 elements,
            type (3, 0) in Feitchner-Yuzvinsky presentation over Rational Field

        Next we get the non-trivial generators and do some computations::

            sage: # needs sage.libs.singular sage.rings.finite_rings
            sage: G = A.gens()[7:]; G
            (Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg)
            sage: Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg = G
            sage: Aabf*Aabf
            -Aabcdefg^2
            sage: Aabf*Acfg
            0
            sage: matrix([[x * y for x in G] for y in G])
            [-Aabcdefg^2           0           0           0           0           0           0           0]
            [          0 -Aabcdefg^2           0           0           0           0           0           0]
            [          0           0 -Aabcdefg^2           0           0           0           0           0]
            [          0           0           0 -Aabcdefg^2           0           0           0           0]
            [          0           0           0           0 -Aabcdefg^2           0           0           0]
            [          0           0           0           0           0 -Aabcdefg^2           0           0]
            [          0           0           0           0           0           0 -Aabcdefg^2           0]
            [          0           0           0           0           0           0           0  Aabcdefg^2]

        The augmented Chow ring can also be constructed with the
        Feitchner-Yuzvinsky and atom-free presentation::

            sage: M = matroids.Wheel(3)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'fy\'); ch
            Augmented Chow ring of Wheel(3): Regular matroid of rank 3 on
            6 elements with 16 bases in Feitchner-Yuzvinsky presentation over
            Rational Field
            sage: M = matroids.Uniform(3, 6)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'atom-free\'); ch
            Augmented Chow ring of U(3, 6): Matroid of rank 3 on 6 elements with circuit-closures
            {3: {{0, 1, 2, 3, 4, 5}}} in atom-free presentation over Rational Field'''
    @overload
    def chow_ring(self, QQ, augmented=..., presentation=...) -> Any:
        '''Matroid.chow_ring(self, R, augmented=False, presentation=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8054)

        Return the (augmented) Chow ring of ``self`` over ``R``.

        .. SEEALSO::

            - :mod:`sage.matroids.chow_ring_ideal`
            - :mod:`sage.matroids.chow_ring`

        INPUT:

        - ``M`` -- matroid
        - ``R`` -- commutative ring
        - ``augmented`` -- boolean (default: ``False``); when ``True``, this
          is the augmented Chow ring and if ``False``, this is the
          non-augmented Chow ring
        - ``presentation`` -- string; one of the following:

          * ``"fy"`` - the Feitchner-Yuzvinsky presentation
          * ``"atom-free"`` - the atom-free presentation
          * ``"simplicial"`` - the simplicial presentation

        EXAMPLES::

            sage: M = matroids.Wheel(2)
            sage: A = M.chow_ring(R=ZZ, augmented=False, presentation=\'fy\'); A
            Chow ring of Wheel(2): Regular matroid of rank 2 on 4 elements with
            5 bases in Feitchner-Yuzvinsky presentation over Integer Ring
            sage: A.defining_ideal()._gens_constructor(A.defining_ideal().ring())
            [A0*A1, A0*A23, A1*A23, A0 + A0123, A1 + A0123, A23 + A0123]
            sage: A23 = A.gen(0)
            sage: A23*A23
            0

        We construct a more interesting example using the Fano matroid::

            sage: M = matroids.catalog.Fano()
            sage: A = M.chow_ring(QQ, False, \'fy\'); A
            Chow ring of Fano: Binary matroid of rank 3 on 7 elements,
            type (3, 0) in Feitchner-Yuzvinsky presentation over Rational Field

        Next we get the non-trivial generators and do some computations::

            sage: # needs sage.libs.singular sage.rings.finite_rings
            sage: G = A.gens()[7:]; G
            (Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg)
            sage: Aabf, Aace, Aadg, Abcd, Abeg, Acfg, Adef, Aabcdefg = G
            sage: Aabf*Aabf
            -Aabcdefg^2
            sage: Aabf*Acfg
            0
            sage: matrix([[x * y for x in G] for y in G])
            [-Aabcdefg^2           0           0           0           0           0           0           0]
            [          0 -Aabcdefg^2           0           0           0           0           0           0]
            [          0           0 -Aabcdefg^2           0           0           0           0           0]
            [          0           0           0 -Aabcdefg^2           0           0           0           0]
            [          0           0           0           0 -Aabcdefg^2           0           0           0]
            [          0           0           0           0           0 -Aabcdefg^2           0           0]
            [          0           0           0           0           0           0 -Aabcdefg^2           0]
            [          0           0           0           0           0           0           0  Aabcdefg^2]

        The augmented Chow ring can also be constructed with the
        Feitchner-Yuzvinsky and atom-free presentation::

            sage: M = matroids.Wheel(3)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'fy\'); ch
            Augmented Chow ring of Wheel(3): Regular matroid of rank 3 on
            6 elements with 16 bases in Feitchner-Yuzvinsky presentation over
            Rational Field
            sage: M = matroids.Uniform(3, 6)
            sage: ch = M.chow_ring(QQ, augmented=True, presentation=\'atom-free\'); ch
            Augmented Chow ring of U(3, 6): Matroid of rank 3 on 6 elements with circuit-closures
            {3: {{0, 1, 2, 3, 4, 5}}} in atom-free presentation over Rational Field'''
    @overload
    def circuit(self, X=...) -> Any:
        """Matroid.circuit(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1494)

        Return a circuit.

        A *circuit* of a matroid is an inclusionwise minimal dependent subset.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a set of elements

        - If ``X`` is not ``None``, the output is a circuit contained in ``X``
          if such a circuit exists. Otherwise an error is raised.
        - If ``X`` is ``None``, the output is a circuit contained in
          ``self.groundset()`` if such a circuit exists. Otherwise an error is
          raised.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.circuit(['a', 'c', 'd', 'e', 'f']))
            ['c', 'd', 'e', 'f']
            sage: sorted(M.circuit(['a', 'c', 'd']))
            Traceback (most recent call last):
            ...
            ValueError: no circuit in independent set
            sage: M.circuit(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: C = M.circuit()
            sage: sorted(C)  # random
            ['a', 'b', 'c', 'd']
            sage: M.is_circuit(C)
            True"""
    @overload
    def circuit(self) -> Any:
        """Matroid.circuit(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1494)

        Return a circuit.

        A *circuit* of a matroid is an inclusionwise minimal dependent subset.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a set of elements

        - If ``X`` is not ``None``, the output is a circuit contained in ``X``
          if such a circuit exists. Otherwise an error is raised.
        - If ``X`` is ``None``, the output is a circuit contained in
          ``self.groundset()`` if such a circuit exists. Otherwise an error is
          raised.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.circuit(['a', 'c', 'd', 'e', 'f']))
            ['c', 'd', 'e', 'f']
            sage: sorted(M.circuit(['a', 'c', 'd']))
            Traceback (most recent call last):
            ...
            ValueError: no circuit in independent set
            sage: M.circuit(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: C = M.circuit()
            sage: sorted(C)  # random
            ['a', 'b', 'c', 'd']
            sage: M.is_circuit(C)
            True"""
    @overload
    def circuit_closures(self) -> dict:
        """Matroid.circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2577)

        Return the closures of circuits of the matroid.

        A *circuit closure* is a closed set containing a circuit.

        OUTPUT: a dictionary containing the circuit closures of the matroid,
        indexed by their ranks

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: CC = M.circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            1
            sage: len(CC[1])
            Traceback (most recent call last):
            ...
            KeyError: 1
            sage: [sorted(X) for X in CC[3]]
            [['a', 'b', 'c', 'd', 'e', 'f', 'g']]"""
    @overload
    def circuit_closures(self) -> Any:
        """Matroid.circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2577)

        Return the closures of circuits of the matroid.

        A *circuit closure* is a closed set containing a circuit.

        OUTPUT: a dictionary containing the circuit closures of the matroid,
        indexed by their ranks

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: CC = M.circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            1
            sage: len(CC[1])
            Traceback (most recent call last):
            ...
            KeyError: 1
            sage: [sorted(X) for X in CC[3]]
            [['a', 'b', 'c', 'd', 'e', 'f', 'g']]"""
    @overload
    def circuits(self, k=...) -> SetSystem:
        """Matroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2374)

        Return the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if provided, return only circuits of
          length `k`

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.circuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
            ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'],
            ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'],
            ['c', 'f', 'g'], ['d', 'e', 'f']]"""
    @overload
    def circuits(self) -> Any:
        """Matroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2374)

        Return the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if provided, return only circuits of
          length `k`

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.circuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
            ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'],
            ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'],
            ['c', 'f', 'g'], ['d', 'e', 'f']]"""
    @overload
    def circuits_iterator(self, k=...) -> Any:
        """Matroid.circuits_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2416)

        Return an iterator over the circuits of the matroid.

        .. SEEALSO::

            :meth:`~sage.matroids.matroid.Matroid.circuit`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.circuits_iterator()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
            ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'],
            ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'],
            ['c', 'f', 'g'], ['d', 'e', 'f']]"""
    @overload
    def circuits_iterator(self) -> Any:
        """Matroid.circuits_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2416)

        Return an iterator over the circuits of the matroid.

        .. SEEALSO::

            :meth:`~sage.matroids.matroid.Matroid.circuit`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.circuits_iterator()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'],
            ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'],
            ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'],
            ['c', 'f', 'g'], ['d', 'e', 'f']]"""
    def closure(self, X) -> Any:
        """Matroid.closure(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1567)

        Return the closure of a set ``X``.

        A set is *closed* if adding any extra element to it will increase the
        rank of the set. The *closure* of a set is the smallest closed set
        containing it.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: superset of ``X``

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.closure(set(['a', 'b', 'c'])))
            ['a', 'b', 'c', 'd']
            sage: M.closure(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    @overload
    def cobasis(self) -> Any:
        """Matroid.cobasis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1736)

        Return an arbitrary cobasis of the matroid.

        A *cobasis* is the complement of a basis. A cobasis is
        a basis of the dual matroid.

        .. NOTE::

            Output can change between calls.

        OUTPUT: a set of elements

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.matroid.Matroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: B = M.cobasis()
            sage: M.is_cobasis(B)
            True
            sage: len(B)
            6
            sage: M.corank(B)
            6
            sage: M.full_corank()
            6"""
    @overload
    def cobasis(self) -> Any:
        """Matroid.cobasis(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1736)

        Return an arbitrary cobasis of the matroid.

        A *cobasis* is the complement of a basis. A cobasis is
        a basis of the dual matroid.

        .. NOTE::

            Output can change between calls.

        OUTPUT: a set of elements

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.matroid.Matroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: B = M.cobasis()
            sage: M.is_cobasis(B)
            True
            sage: len(B)
            6
            sage: M.corank(B)
            6
            sage: M.full_corank()
            6"""
    @overload
    def cocircuit(self, X=...) -> Any:
        """Matroid.cocircuit(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1835)

        Return a cocircuit.

        A *cocircuit* is an inclusionwise minimal subset that is dependent in
        the dual matroid.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a set of elements

        - If ``X`` is not ``None``, the output is a cocircuit contained in
          ``X`` if such a cocircuit exists. Otherwise an error is raised.
        - If ``X`` is ``None``, the output is a cocircuit contained in
          ``self.groundset()`` if such a cocircuit exists. Otherwise an error
          is raised.

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.cocircuit(['a', 'c', 'd', 'e', 'f']))
            ['c', 'd', 'e', 'f']
            sage: sorted(M.cocircuit(['a', 'c', 'd']))
            Traceback (most recent call last):
            ...
            ValueError: no cocircuit in coindependent set.
            sage: M.cocircuit(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: C = M.cocircuit()
            sage: sorted(C)  # random
            ['e', 'f', 'g', 'h']
            sage: M.is_cocircuit(C)
            True"""
    @overload
    def cocircuit(self) -> Any:
        """Matroid.cocircuit(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1835)

        Return a cocircuit.

        A *cocircuit* is an inclusionwise minimal subset that is dependent in
        the dual matroid.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: a set of elements

        - If ``X`` is not ``None``, the output is a cocircuit contained in
          ``X`` if such a cocircuit exists. Otherwise an error is raised.
        - If ``X`` is ``None``, the output is a cocircuit contained in
          ``self.groundset()`` if such a cocircuit exists. Otherwise an error
          is raised.

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.cocircuit(['a', 'c', 'd', 'e', 'f']))
            ['c', 'd', 'e', 'f']
            sage: sorted(M.cocircuit(['a', 'c', 'd']))
            Traceback (most recent call last):
            ...
            ValueError: no cocircuit in coindependent set.
            sage: M.cocircuit(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset
            sage: C = M.cocircuit()
            sage: sorted(C)  # random
            ['e', 'f', 'g', 'h']
            sage: M.is_cocircuit(C)
            True"""
    @overload
    def cocircuits(self) -> SetSystem:
        """Matroid.cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2506)

        Return the cocircuits of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.cocircuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'f'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'],
            ['c', 'd', 'e', 'g']]"""
    @overload
    def cocircuits(self) -> Any:
        """Matroid.cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2506)

        Return the cocircuits of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.cocircuits()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'f'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'],
            ['c', 'd', 'e', 'g']]"""
    @overload
    def cocircuits_iterator(self) -> Any:
        """Matroid.cocircuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2529)

        Return an iterator over the cocircuits of the matroid.

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.cocircuits_iterator()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'f'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'],
            ['c', 'd', 'e', 'g']]"""
    @overload
    def cocircuits_iterator(self) -> Any:
        """Matroid.cocircuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2529)

        Return an iterator over the cocircuits of the matroid.

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.cocircuits_iterator()])
            [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'f'],
            ['a', 'e', 'f', 'g'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'],
            ['c', 'd', 'e', 'g']]"""
    def coclosure(self, X) -> Any:
        """Matroid.coclosure(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1805)

        Return the coclosure of a set ``X``.

        A set is *coclosed* if it is closed in the dual matroid. The
        *coclosure* of `X` is the smallest coclosed set containing `X`.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: superset of ``X``

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.coclosure(set(['a', 'b', 'c'])))
            ['a', 'b', 'c', 'd']
            sage: M.coclosure(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    def coextension(self, element=..., subsets=...) -> Any:
        """Matroid.coextension(self, element=None, subsets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4576)

        Return a coextension of the matroid.

        A *coextension* of `M` by an element `e` is a matroid `M'` such that
        `M' / e = M`. The element ``element`` is placed such that it
        lies in the
        :meth:`coclosure <sage.matroids.matroid.Matroid.coclosure>` of
        each set in ``subsets``, and otherwise as freely as possible.

        This is the dual method of
        :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`. See
        the documentation there for more details.

        INPUT:

        - ``element`` -- (default: ``None``) the label of the new element. If
          not specified, a new label will be generated automatically.
        - ``subsets`` -- (default: ``None``) a set of subsets of the matroid.
          The coextension should be such that the new element is in the cospan
          of each of these. If not specified, the element is assumed to be in
          the cospan of the full groundset.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.coextensions() <sage.matroids.matroid.Matroid.coextensions>`,
            :meth:`M.modular_cut() <sage.matroids.matroid.Matroid.modular_cut>`,
            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`

        EXAMPLES:

        Add an element in general position::

            sage: M = matroids.Uniform(3, 6)
            sage: N = M.coextension(6)
            sage: N.is_isomorphic(matroids.Uniform(4, 7))
            True

        Add one inside the span of a specified hyperplane::

            sage: M = matroids.Uniform(3, 6)
            sage: H = [frozenset([0, 1])]
            sage: N = M.coextension(6, H)
            sage: N
            Matroid of rank 4 on 7 elements with 34 bases
            sage: [sorted(C) for C in N.cocircuits() if len(C) == 3]
            [[0, 1, 6]]

        Put an element in series with another::

            sage: M = matroids.catalog.Fano()
            sage: N = M.coextension('z', ['c'])
            sage: N.corank('cz')
            1"""
    def coextensions(self, element=..., coline_length=..., subsets=...) -> Any:
        """Matroid.coextensions(self, element=None, coline_length=None, subsets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4854)

        Return an iterable set of single-element coextensions of the matroid.

        A *coextension* of a matroid `M` by element `e` is a matroid `M'` such
        that `M' / e = M`. By default, this method returns an iterable
        containing all coextensions, but it can be restricted in two ways. If
        ``coline_length`` is specified, the output is restricted to those
        matroids not containing a coline minor of length `k` greater than
        ``coline_length``. If ``subsets`` is specified, then the output is
        restricted to those matroids for which the new element lies in the
        :meth:`coclosure <sage.matroids.matroid.Matroid.coclosure>` of each
        member of ``subsets``.

        This method is dual to
        :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`.

        INPUT:

        - ``element`` -- (optional) the name of the newly added element in
          each coextension.
        - ``coline_length`` -- (optional) a natural number. If given,
          restricts the output to coextensions that do not contain a
          `U_{k - 2, k}` minor where ``k > coline_length``.
        - ``subsets`` -- (optional) a collection of subsets of the groundset.
          If given, restricts the output to extensions where the new element
          is contained in all cohyperplanes that contain an element of
          ``subsets``.

        OUTPUT: an iterable containing matroids

        .. NOTE::

            The coextension by a coloop will always occur.
            The extension by a loop will never occur.

        .. SEEALSO::

            :meth:`M.coextension() <sage.matroids.matroid.Matroid.coextension>`,
            :meth:`M.modular_cut() <sage.matroids.matroid.Matroid.modular_cut>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`,
            :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`,
            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`

        EXAMPLES::

            sage: M = matroids.catalog.P8()
            sage: len(list(M.coextensions()))
            1705
            sage: len(list(M.coextensions(coline_length=4)))
            41
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            sage: len(list(M.coextensions(subsets=[{'a', 'b'}], coline_length=4)))
            5"""
    def coflats(self, longk) -> SetSystem:
        """Matroid.coflats(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3022)

        Return the collection of coflats of the matroid of specified corank.

        A *coflat* is a coclosed set.

        INPUT:

        - ``k`` -- integer

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.coclosure() <sage.matroids.matroid.Matroid.coclosure>`

        EXAMPLES::

            sage: M = matroids.catalog.Q6()                                             # needs sage.rings.finite_rings
            sage: sorted([sorted(F) for F in M.coflats(2)])                             # needs sage.rings.finite_rings
            [['a', 'b'], ['a', 'c'], ['a', 'd', 'f'], ['a', 'e'], ['b', 'c'],
            ['b', 'd'], ['b', 'e'], ['b', 'f'], ['c', 'd'], ['c', 'e', 'f'],
            ['d', 'e']]"""
    def coloops(self) -> Any:
        """Matroid.coloops(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2122)

        Return the set of coloops of the matroid.

        A *coloop* is an element `u` of the groundset such that the
        one-element set `\\{ u \\}` is a cocircuit. In other words, a coloop
        is a loop of the dual of the matroid.

        OUTPUT: a set of elements

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: M.coloops()
            frozenset()
            sage: (M.delete(['a', 'b'])).coloops()
            frozenset({'f'})"""
    @overload
    def components(self) -> Any:
        """Matroid.components(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5055)

        Return a list of the components of the matroid.

        A *component* is an inclusionwise maximal connected subset of the
        matroid. A subset is *connected* if the matroid resulting from
        deleting the complement of that subset is
        :meth:`connected <sage.matroids.matroid.Matroid.is_connected>`.

        OUTPUT: list of subsets

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: setprint(M.components())
            [{0, 1, 3, 4}, {2, 5}]"""
    @overload
    def components(self) -> Any:
        """Matroid.components(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5055)

        Return a list of the components of the matroid.

        A *component* is an inclusionwise maximal connected subset of the
        matroid. A subset is *connected* if the matroid resulting from
        deleting the complement of that subset is
        :meth:`connected <sage.matroids.matroid.Matroid.is_connected>`.

        OUTPUT: list of subsets

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: setprint(M.components())
            [{0, 1, 3, 4}, {2, 5}]"""
    def connectivity(self, S, T=...) -> Any:
        """Matroid.connectivity(self, S, T=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5131)

        Evaluate the connectivity function of the matroid.

        If the input is a single subset `S` of the groundset `E`,
        then the output is `r(S) + r(E\\S) - r(E)`.

        If the input are disjoint subsets `S, T` of the groundset,
        then the output is

        .. MATH::

            \\min \\{ r(X) + r(Y) - r(E) \\mid X \\subseteq S, Y \\subseteq T,
            {X,Y} \\text{a partition of} E \\}.

        INPUT:

        - ``S`` -- a subset (or any iterable) of the groundset
        - ``T`` -- (optional) a subset (or any iterable) of the groundset
          disjoint from ``S``

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.BetsyRoss()
            sage: M.connectivity('ab')
            2
            sage: M.connectivity('ab', 'cd')
            2"""
    def contract(self, X) -> Any:
        """Matroid.contract(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4129)

        Contract elements.

        If `e` is a non-loop element, then the matroid `M / e` is a matroid
        on groundset `E(M) - e`. A set `X` is independent in `M / e` if and
        only if `X \\cup e` is independent in `M`. If `e` is a loop then
        contracting `e` is the same as deleting `e`. We say that `M / e` is
        the matroid obtained from `M` by *contracting* `e`. Contracting an
        element in `M` is the same as deleting an element in the dual of `M`.

        When contracting a set, the elements of that set are contracted one by
        one. It can be shown that the resulting matroid does not depend on the
        order of the contractions.

        Sage supports the shortcut notation ``M / X`` for ``M.contract(X)``.

        INPUT:

        - ``X`` -- either a single element of the groundset, or a collection
          of elements

        OUTPUT: the matroid obtained by contracting the element(s) in ``X``

        .. SEEALSO::

            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`
            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`
            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: M.contract(['a', 'c'])
            Binary matroid of rank 1 on 5 elements, type (1, 0)
            sage: M.contract(['a']) == M / ['a']
            True

        One can use a single element, rather than a set::

            sage: M = matroids.CompleteGraphic(4)                                       # needs sage.graphs
            sage: M.contract(1) == M.contract([1])                                      # needs sage.graphs
            True
            sage: M / 1                                                                 # needs sage.graphs
            Graphic matroid of rank 2 on 5 elements

        Note that one can iterate over strings::

            sage: M = matroids.catalog.Fano()
            sage: M / 'abc'
            Binary matroid of rank 0 on 4 elements, type (0, 0)

        The following is therefore ambiguous. Sage will contract the single
        element::

            sage: M = Matroid(groundset=['a', 'b', 'c', 'abc'],
            ....:             bases=[['a', 'b', 'c'], ['a', 'b', 'abc']])
            sage: sorted((M / 'abc').groundset())
            ['a', 'b', 'c']"""
    @overload
    def corank(self, X=...) -> Any:
        """Matroid.corank(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1679)

        Return the corank of ``X``, or the corank of the groundset if ``X`` is
        ``None``.

        The *corank* of a set `X` is the rank of `X` in the dual matroid.

        If ``X`` is ``None``, the corank of the groundset is returned.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.corank()
            4
            sage: M.corank('cdeg')
            3
            sage: M.rank(['a', 'b', 'x'])
            Traceback (most recent call last):
            ...
            ValueError: ['a', 'b', 'x'] is not a subset of the groundset"""
    @overload
    def corank(self) -> Any:
        """Matroid.corank(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1679)

        Return the corank of ``X``, or the corank of the groundset if ``X`` is
        ``None``.

        The *corank* of a set `X` is the rank of `X` in the dual matroid.

        If ``X`` is ``None``, the corank of the groundset is returned.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.corank()
            4
            sage: M.corank('cdeg')
            3
            sage: M.rank(['a', 'b', 'x'])
            Traceback (most recent call last):
            ...
            ValueError: ['a', 'b', 'x'] is not a subset of the groundset"""
    @overload
    def cosimplify(self) -> Any:
        """Matroid.cosimplify(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4954)

        Return the cosimplification of the matroid.

        A matroid is *cosimple* if it contains no cocircuits of length 1 or 2.
        The *cosimplification* of a matroid is obtained by contracting
        all coloops (cocircuits of length 1) and contracting all but one
        element from each series class (a coclosed set of rank 1, that is,
        each pair in it forms a cocircuit of length 2).

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.is_cosimple() <sage.matroids.matroid.Matroid.is_cosimple>`,
            :meth:`M.coloops() <sage.matroids.matroid.Matroid.coloops>`,
            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.simplify() <sage.matroids.matroid.Matroid.simplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual().delete('a')
            sage: M.cosimplify().size()
            3"""
    @overload
    def cosimplify(self) -> Any:
        """Matroid.cosimplify(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4954)

        Return the cosimplification of the matroid.

        A matroid is *cosimple* if it contains no cocircuits of length 1 or 2.
        The *cosimplification* of a matroid is obtained by contracting
        all coloops (cocircuits of length 1) and contracting all but one
        element from each series class (a coclosed set of rank 1, that is,
        each pair in it forms a cocircuit of length 2).

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.is_cosimple() <sage.matroids.matroid.Matroid.is_cosimple>`,
            :meth:`M.coloops() <sage.matroids.matroid.Matroid.coloops>`,
            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.simplify() <sage.matroids.matroid.Matroid.simplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual().delete('a')
            sage: M.cosimplify().size()
            3"""
    def delete(self, X) -> Any:
        """Matroid.delete(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4207)

        Delete elements.

        If `e` is an element, then the matroid `M \\setminus e` is a matroid
        on groundset `E(M) - e`. A set `X` is independent in `M \\setminus e`
        if and only if `X` is independent in `M`. We say that `M \\setminus e`
        is the matroid obtained from `M` by *deleting* `e`.

        When deleting a set, the elements of that set are deleted one by
        one. It can be shown that the resulting matroid does not depend on the
        order of the deletions.

        DEPRECATED: Sage supports the shortcut notation ``M \\ X`` for
        ``M.delete(X)``.

        INPUT:

        - ``X`` -- either a single element of the groundset, or a collection
          of elements

        OUTPUT: the matroid obtained by deleting the element(s) in ``X``

        .. SEEALSO::

            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`
            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Fano()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            sage: M.delete(['a', 'c'])
            Binary matroid of rank 3 on 5 elements, type (1, 6)
            sage: M.delete(['a']) == M.delete(['a'])
            True

        One can use a single element, rather than a set::

            sage: M = matroids.CompleteGraphic(4)                                       # needs sage.graphs
            sage: M.delete(1) == M.delete([1])                                          # needs sage.graphs
            True
            sage: M.delete(1)                                                           # needs sage.graphs
            Graphic matroid of rank 3 on 5 elements

        Note that one can iterate over strings::

            sage: M = matroids.catalog.Fano()
            sage: M.delete('abc')
            Binary matroid of rank 3 on 4 elements, type (0, 5)

        The following is therefore ambiguous. Sage will delete the single
        element::

            sage: M = Matroid(groundset=['a', 'b', 'c', 'abc'],
            ....:             bases=[['a', 'b', 'c'], ['a', 'b', 'abc']])
            sage: sorted((M.delete('abc')).groundset())
            ['a', 'b', 'c']"""
    def dependent_sets(self, longk) -> SetSystem:
        """Matroid.dependent_sets(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2698)

        Return the dependent sets of fixed size.

        INPUT:

        - ``k`` -- integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.dependent_sets(3)
            SetSystem of 0 sets over 8 elements
            sage: sorted([sorted(X) for X in
            ....: matroids.catalog.Vamos().dependent_sets(4)])
            [['a', 'b', 'c', 'd'], ['a', 'b', 'e', 'f'], ['a', 'b', 'g', 'h'],
            ['c', 'd', 'e', 'f'], ['e', 'f', 'g', 'h']]

        ALGORITHM:

        Test all subsets of the groundset of cardinality `k`."""
    def dependent_sets_iterator(self, longk) -> Any:
        """Matroid.dependent_sets_iterator(self, long k)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2728)

        Return an iterator over the dependent sets of fixed size.

        INPUT:

        - ``k`` -- integer

        ALGORITHM:

        Test all subsets of the groundset of cardinality `k`.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: list(M.dependent_sets_iterator(3))
            []
            sage: sorted([sorted(X) for X in
            ....: matroids.catalog.Vamos().dependent_sets_iterator(4)])
            [['a', 'b', 'c', 'd'], ['a', 'b', 'e', 'f'], ['a', 'b', 'g', 'h'],
            ['c', 'd', 'e', 'f'], ['e', 'f', 'g', 'h']]"""
    def direct_sum(self, matroids) -> Any:
        """Matroid.direct_sum(self, matroids)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8538)

        Return the matroid direct sum with another matroid or list of
        matroids.

        Let `(M_1, M_2, \\ldots, M_k)` be a list of matroids where each `M_i`
        has groundset `E_i`. The matroid sum of `(E_1,I_1),\\ldots,(E_n,I_n)`
        is a matroid `(E,I)` where `E= \\bigsqcup_{i=1}^n E_i` and
        `I= \\bigsqcup_{i=1}^n I_i`.

        INPUT:

        - ``matroids`` -- matroid or list of matroids

        OUTPUT: an instance of
        :class:`MatroidSum <sage.matroids.union_matroid.MatroidSum>`

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.Fano().direct_sum(M); N
            Matroid of rank 6 on 16 elements as matroid sum of
            Binary matroid of rank 3 on 7 elements, type (3, 0)
            Matroid of rank 3 on 9 elements with 9 nonspanning circuits
            sage: len(N.independent_sets())
            6897
            sage: len(N.bases())
            2100"""
    def dual(self) -> Any:
        """Matroid.dual(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4288)

        Return the dual of the matroid.

        Let `M` be a matroid with groundset `E`. If `B` is the set of bases
        of `M`, then the set `\\{E - b : b \\in B\\}` is the set of bases of
        another matroid, the *dual* of `M`.

        .. NOTE::

            This function wraps ``self`` in a ``DualMatroid`` object. For more
            efficiency, subclasses that can, should override this method.

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: N = M.dual()
            sage: N.rank()
            6
            sage: N
            Dual of 'Pappus: Matroid of rank 3 on 9 elements with 9 nonspanning circuits'"""
    @overload
    def equals(self, other) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    @overload
    def equals(self, M1) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    @overload
    def equals(self, M2) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    @overload
    def equals(self, M2) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    @overload
    def equals(self, M3) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    @overload
    def equals(self, N) -> Any:
        '''Matroid.equals(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3676)

        Test for matroid equality.

        Two matroids `M` and `N` are *equal* if they have the same groundset
        and a subset `X` is independent in `M` if and only if it is
        independent in `N`.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        .. NOTE::

            This method tests abstract matroid equality. The ``==`` operator
            takes a more restricted view: ``M == N`` returns ``True`` only if

            #. the internal representations are of the same type,
            #. those representations are equivalent (for an appropriate
               meaning of "equivalent" in that class), and
            #. ``M.equals(N)``.

        EXAMPLES:

        A :class:`BinaryMatroid <sage.matroids.linear_matroid.BinaryMatroid>`
        and :class:`BasisMatroid <sage.matroids.basis_matroid.BasisMatroid>`
        use different representations of the matroid internally, so ``==``
        yields ``False``, even if the matroids are equal::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano(); M
            Fano: Binary matroid of rank 3 on 7 elements, type (3, 0)
            sage: M1 = BasisMatroid(M)
            sage: M2 = Matroid(groundset=\'abcdefg\', reduced_matrix=[
            ....:      [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]], field=GF(2))
            sage: M.equals(M1)
            True
            sage: M.equals(M2)
            True
            sage: M == M1
            False
            sage: M == M2
            True

        :class:`LinearMatroid <sage.matroids.linear_matroid.LinearMatroid>`
        instances ``M`` and ``N`` satisfy ``M == N`` if the representations
        are equivalent up to row operations and column scaling::

            sage: M1 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 2]]))
            sage: M2 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[1, 0, 1, 1], [0, 1, 1, 3]]))
            sage: M3 = LinearMatroid(groundset=\'abcd\', matrix=Matrix(GF(7),
            ....:                               [[2, 6, 1, 0], [6, 1, 0, 1]]))
            sage: M1.equals(M2)
            True
            sage: M1.equals(M3)
            True
            sage: M1 == M2
            False
            sage: M1 == M3
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.equals(N)
            False'''
    def extension(self, element=..., subsets=...) -> Any:
        """Matroid.extension(self, element=None, subsets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4501)

        Return an extension of the matroid.

        An *extension* of `M` by an element `e` is a matroid `M'` such that
        `M' \\setminus e = M`. The element ``element`` is placed such that it
        lies in the :meth:`closure <sage.matroids.matroid.Matroid.closure>` of
        each set in ``subsets``, and otherwise as freely as possible. More
        precisely, the extension is defined by the
        :meth:`modular cut <sage.matroids.matroid.Matroid.modular_cut>`
        generated by the sets in ``subsets``.

        INPUT:

        - ``element`` -- (default: ``None``) the label of the new element. If
          not specified, a new label will be generated automatically.
        - ``subsets`` -- (default: ``None``) a set of subsets of the matroid.
          The extension should be such that the new element is in the span of
          each of these. If not specified, the element is assumed to be in the
          span of the full groundset.

        OUTPUT: matroid

        .. NOTE::

            Internally, sage uses the notion of a *linear subclass* for
            matroid extension. If ``subsets`` already consists of a linear
            subclass (i.e. the set of hyperplanes of a modular cut) then the
            faster method ``M._extension()`` can be used.

        .. SEEALSO::

            :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`,
            :meth:`M.modular_cut() <sage.matroids.matroid.Matroid.modular_cut>`,
            :meth:`M.coextension() <sage.matroids.matroid.Matroid.coextension>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`

        EXAMPLES:

        First we add an element in general position::

            sage: M = matroids.Uniform(3, 6)
            sage: N = M.extension(6)
            sage: N.is_isomorphic(matroids.Uniform(3, 7))
            True

        Next we add one inside the span of a specified hyperplane::

            sage: M = matroids.Uniform(3, 6)
            sage: H = [frozenset([0, 1])]
            sage: N = M.extension(6, H)
            sage: N
            Matroid of rank 3 on 7 elements with 34 bases
            sage: [sorted(C) for C in N.circuits() if len(C) == 3]
            [[0, 1, 6]]

        Putting an element in parallel with another::

            sage: M = matroids.catalog.Fano()
            sage: N = M.extension('z', ['c'])
            sage: N.rank('cz')
            1"""
    def extensions(self, element=..., line_length=..., subsets=...) -> Any:
        """Matroid.extensions(self, element=None, line_length=None, subsets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4793)

        Return an iterable set of single-element extensions of the matroid.

        An *extension* of a matroid `M` by element `e` is a matroid `M'` such
        that `M' \\setminus e = M`. By default, this method returns an iterable
        containing all extensions, but it can be restricted in two ways. If
        ``line_length`` is specified, the output is restricted to those
        matroids not containing a line minor of length `k` greater than
        ``line_length``. If ``subsets`` is specified, then the output is
        restricted to those matroids for which the new element lies in the
        :meth:`closure <sage.matroids.matroid.Matroid.closure>` of each
        member of ``subsets``.

        INPUT:

        - ``element`` -- (optional) the name of the newly added element in
          each extension.
        - ``line_length`` -- (optional) a natural number. If given, restricts
          the output to extensions that do not contain a `U_{2, k}` minor
          where ``k > line_length``.
        - ``subsets`` -- (optional) a collection of subsets of the groundset.
          If given, restricts the output to extensions where the new element
          is contained in all hyperplanes that contain an element of
          ``subsets``.

        OUTPUT: an iterable containing matroids

        .. NOTE::

            The extension by a loop will always occur.
            The extension by a coloop will never occur.

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.modular_cut() <sage.matroids.matroid.Matroid.modular_cut>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`,
            :meth:`M.coextensions() <sage.matroids.matroid.Matroid.coextensions>`

        EXAMPLES::

            sage: M = matroids.catalog.P8()
            sage: len(list(M.extensions()))
            1705
            sage: len(list(M.extensions(line_length=4)))
            41
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            sage: len(list(M.extensions(subsets=[{'a', 'b'}], line_length=4)))
            5"""
    def f_vector(self) -> list:
        """Matroid.f_vector(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3084)

        Return the `f`-vector of the matroid.

        The `f`-*vector* is a vector `(f_0, \\ldots, f_r)`, where `f_i` is the
        number of independent sets of rank `i`, and `r` is the rank of the
        matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.f_vector()
            [1, 8, 28, 56, 65]

        TESTS::

            sage: for M in matroids.AllMatroids(5):                                     # optional - matroid_database
            ....:     assert M.f_vector() == SimplicialComplex(M.bases()).f_vector()"""
    @overload
    def flat_cover(self, solver=..., verbose=..., integrality_tolerance=...) -> Any:
        """Matroid.flat_cover(self, solver=None, verbose=0, integrality_tolerance=1e-3)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7998)

        Return a minimum-size cover of the nonbases by nonspanning flats.

        A *nonbasis* is a subset that has the size of a basis, yet is
        dependent. A *flat* is a closed set.

        INPUT:

        - ``solver`` -- (default: ``None``) specify a Linear Program (LP) solver
          to be used. If set to ``None``, the default one is used. For more
          information on LP solvers and which default solver is used, see the
          method :meth:`~sage.numerical.mip.MixedIntegerLinearProgram.solve` of
          the class :class:`~sage.numerical.mip.MixedIntegerLinearProgram`.

        - ``verbose`` -- integer (default: 0); sets the level of verbosity
          of the LP solver. Set to 0 by default, which means quiet.

        .. SEEALSO::

            :meth:`M.nonbases() <sage.matroids.matroid.Matroid.nonbases>`,
            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: setprint(M.flat_cover())                                              # needs sage.rings.finite_rings
            [{'a', 'b', 'f'}, {'a', 'c', 'e'}, {'a', 'd', 'g'},
             {'b', 'c', 'd'}, {'b', 'e', 'g'}, {'c', 'f', 'g'},
             {'d', 'e', 'f'}]"""
    @overload
    def flat_cover(self) -> Any:
        """Matroid.flat_cover(self, solver=None, verbose=0, integrality_tolerance=1e-3)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7998)

        Return a minimum-size cover of the nonbases by nonspanning flats.

        A *nonbasis* is a subset that has the size of a basis, yet is
        dependent. A *flat* is a closed set.

        INPUT:

        - ``solver`` -- (default: ``None``) specify a Linear Program (LP) solver
          to be used. If set to ``None``, the default one is used. For more
          information on LP solvers and which default solver is used, see the
          method :meth:`~sage.numerical.mip.MixedIntegerLinearProgram.solve` of
          the class :class:`~sage.numerical.mip.MixedIntegerLinearProgram`.

        - ``verbose`` -- integer (default: 0); sets the level of verbosity
          of the LP solver. Set to 0 by default, which means quiet.

        .. SEEALSO::

            :meth:`M.nonbases() <sage.matroids.matroid.Matroid.nonbases>`,
            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: setprint(M.flat_cover())                                              # needs sage.rings.finite_rings
            [{'a', 'b', 'f'}, {'a', 'c', 'e'}, {'a', 'd', 'g'},
             {'b', 'c', 'd'}, {'b', 'e', 'g'}, {'c', 'f', 'g'},
             {'d', 'e', 'f'}]"""
    def flats(self, longk) -> SetSystem:
        """Matroid.flats(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2996)

        Return the collection of flats of the matroid of specified rank.

        A *flat* is a closed set.

        INPUT:

        - ``k`` -- integer

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(F) for F in M.flats(2)])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def full_corank(self) -> Any:
        """Matroid.full_corank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1714)

        Return the corank of the matroid.

        The *corank* of the matroid equals the rank of the dual matroid. It is
        given by ``M.size() - M.full_rank()``.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.matroid.Matroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_corank()
            4"""
    @overload
    def full_corank(self) -> Any:
        """Matroid.full_corank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1714)

        Return the corank of the matroid.

        The *corank* of the matroid equals the rank of the dual matroid. It is
        given by ``M.size() - M.full_rank()``.

        OUTPUT: integer

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.full_rank() <sage.matroids.matroid.Matroid.full_rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_corank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """Matroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1421)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """Matroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1421)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """Matroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1421)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    def fundamental_circuit(self, B, e) -> Any:
        """Matroid.fundamental_circuit(self, B, e)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1534)

        Return the `B`-fundamental circuit using `e`.

        If `B` is a basis, and `e` an element not in `B`, then the
        `B`-*fundamental circuit* using `e` is the unique matroid circuit
        contained in `B\\cup e`.

        INPUT:

        - ``B`` -- a basis of the matroid
        - ``e`` -- an element not in ``B``

        OUTPUT: a set of elements

        .. SEEALSO::

            :meth:`M.circuit() <Matroid.circuit>`,
            :meth:`M.basis() <Matroid.basis>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.fundamental_circuit('defg', 'c'))
            ['c', 'd', 'e', 'f']"""
    def fundamental_cocircuit(self, B, e) -> Any:
        """Matroid.fundamental_cocircuit(self, B, e)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1881)

        Return the `B`-fundamental cocircuit using `e`.

        If `B` is a basis, and `e` an element of `B`, then the
        `B`-*fundamental cocircuit* using `e` is the unique matroid cocircuit
        that intersects `B` only in `e`.

        This is equal to
        ``M.dual().fundamental_circuit(M.groundset().difference(B), e)``.

        INPUT:

        - ``B`` -- a basis of the matroid
        - ``e`` -- an element of ``B``

        OUTPUT: a set of elements

        .. SEEALSO::

            :meth:`M.cocircuit() <Matroid.cocircuit>`,
            :meth:`M.basis() <Matroid.basis>`,
            :meth:`M.fundamental_circuit() <Matroid.fundamental_circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: sorted(M.fundamental_cocircuit('abch', 'c'))
            ['c', 'd', 'e', 'f']"""
    def girth(self) -> Any:
        """Matroid.girth(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6265)

        Return the girth of the matroid.

        The girth is the size of the smallest circuit. In case the matroid has
        no circuits the girth is `\\infty`.

        EXAMPLES::

            sage: matroids.Uniform(5, 5).girth()
            +Infinity
            sage: matroids.catalog.K4().girth()
            3
            sage: matroids.catalog.Vamos().girth()
            4

        REFERENCES:

        [Oxl2011]_, p. 327."""
    @overload
    def groundset(self) -> frozenset:
        """Matroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 472)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: :class:`frozenset`

        .. NOTE::

            Subclasses should implement this method. The return type should be
            frozenset or any type with compatible interface.

        EXAMPLES::

            sage: M = sage.matroids.matroid.Matroid()
            sage: M.groundset()
            Traceback (most recent call last):
            ...
            NotImplementedError: subclasses need to implement this"""
    @overload
    def groundset(self) -> Any:
        """Matroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 472)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: :class:`frozenset`

        .. NOTE::

            Subclasses should implement this method. The return type should be
            frozenset or any type with compatible interface.

        EXAMPLES::

            sage: M = sage.matroids.matroid.Matroid()
            sage: M.groundset()
            Traceback (most recent call last):
            ...
            NotImplementedError: subclasses need to implement this"""
    def has_line_minor(self, k, hyperlines=..., certificate=...) -> Any:
        """Matroid.has_line_minor(self, k, hyperlines=None, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4387)

        Test if the matroid has a `U_{2, k}`-minor.

        The matroid `U_{2, k}` is a matroid on `k` elements in which every
        subset of at most 2 elements is independent, and every subset of more
        than two elements is dependent.

        The optional argument ``hyperlines`` restricts the search space: this
        method returns ``True`` if `si(M/F)` is isomorphic to `U_{2, l}` with
        `l \\geq k` for some `F` in ``hyperlines``, and ``False`` otherwise.

        INPUT:

        - ``k`` -- the length of the line minor
        - ``hyperlines`` -- (default: ``None``) a set of flats of codimension
          2. Defaults to the set of all flats of codimension 2.
        - ``certificate`` -- boolean (default: ``False``); if ``True`` returns
          ``(True, F)``, where ``F`` is a flat and
          ``self.minor(contractions=F)`` has a `U_{2,k}` restriction or
          ``(False, None)``.

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`Matroid.has_minor`

        EXAMPLES::

            sage: M = matroids.catalog.N1()
            sage: M.has_line_minor(4)
            True
            sage: M.has_line_minor(5)
            False
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c']])
            False
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]])
            True
            sage: M.has_line_minor(4, certificate=True)
            (True, frozenset({'a', 'b', 'd'}))
            sage: M.has_line_minor(5, certificate=True)
            (False, None)
            sage: M.has_line_minor(k=4, hyperlines=[['a', 'b', 'c'],
            ....:                                   ['a', 'b', 'd' ]], certificate=True)
            (True, frozenset({'a', 'b', 'd'}))"""
    @overload
    def has_minor(self, N, boolcertificate=...) -> Any:
        """Matroid.has_minor(self, N, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4342)

        Check if ``self`` has a minor isomorphic to ``N``,
        and optionally return frozensets ``X`` and ``Y`` so that ``N`` is isomorphic to ``self.minor(X, Y)``.

        INPUT:

        - ``N`` -- an instance of a :class:`Matroid` object
        - ``certificate`` -- boolean (default: ``False``); if ``True``, returns
          ``True, (X, Y, dic)`` where ``N`` is isomorphic to
          ``self.minor(X, Y)``, and ``dic`` is an isomorphism between ``N`` and
          ``self.minor(X, Y)``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_minor(M)
            False
            sage: matroids.catalog.NonFano().has_minor(M)
            True
            sage: matroids.catalog.NonFano().has_minor(M, certificate=True)
            (True, (frozenset(), frozenset({...}), {...}))
            sage: M = matroids.catalog.Fano()
            sage: M.has_minor(M, True)
            (True,
             (frozenset(),
              frozenset(),
              {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}))"""
    @overload
    def has_minor(self, M) -> Any:
        """Matroid.has_minor(self, N, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4342)

        Check if ``self`` has a minor isomorphic to ``N``,
        and optionally return frozensets ``X`` and ``Y`` so that ``N`` is isomorphic to ``self.minor(X, Y)``.

        INPUT:

        - ``N`` -- an instance of a :class:`Matroid` object
        - ``certificate`` -- boolean (default: ``False``); if ``True``, returns
          ``True, (X, Y, dic)`` where ``N`` is isomorphic to
          ``self.minor(X, Y)``, and ``dic`` is an isomorphism between ``N`` and
          ``self.minor(X, Y)``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_minor(M)
            False
            sage: matroids.catalog.NonFano().has_minor(M)
            True
            sage: matroids.catalog.NonFano().has_minor(M, certificate=True)
            (True, (frozenset(), frozenset({...}), {...}))
            sage: M = matroids.catalog.Fano()
            sage: M.has_minor(M, True)
            (True,
             (frozenset(),
              frozenset(),
              {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}))"""
    @overload
    def has_minor(self, M) -> Any:
        """Matroid.has_minor(self, N, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4342)

        Check if ``self`` has a minor isomorphic to ``N``,
        and optionally return frozensets ``X`` and ``Y`` so that ``N`` is isomorphic to ``self.minor(X, Y)``.

        INPUT:

        - ``N`` -- an instance of a :class:`Matroid` object
        - ``certificate`` -- boolean (default: ``False``); if ``True``, returns
          ``True, (X, Y, dic)`` where ``N`` is isomorphic to
          ``self.minor(X, Y)``, and ``dic`` is an isomorphism between ``N`` and
          ``self.minor(X, Y)``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_minor(M)
            False
            sage: matroids.catalog.NonFano().has_minor(M)
            True
            sage: matroids.catalog.NonFano().has_minor(M, certificate=True)
            (True, (frozenset(), frozenset({...}), {...}))
            sage: M = matroids.catalog.Fano()
            sage: M.has_minor(M, True)
            (True,
             (frozenset(),
              frozenset(),
              {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}))"""
    @overload
    def has_minor(self, M, certificate=...) -> Any:
        """Matroid.has_minor(self, N, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4342)

        Check if ``self`` has a minor isomorphic to ``N``,
        and optionally return frozensets ``X`` and ``Y`` so that ``N`` is isomorphic to ``self.minor(X, Y)``.

        INPUT:

        - ``N`` -- an instance of a :class:`Matroid` object
        - ``certificate`` -- boolean (default: ``False``); if ``True``, returns
          ``True, (X, Y, dic)`` where ``N`` is isomorphic to
          ``self.minor(X, Y)``, and ``dic`` is an isomorphism between ``N`` and
          ``self.minor(X, Y)``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_minor(M)
            False
            sage: matroids.catalog.NonFano().has_minor(M)
            True
            sage: matroids.catalog.NonFano().has_minor(M, certificate=True)
            (True, (frozenset(), frozenset({...}), {...}))
            sage: M = matroids.catalog.Fano()
            sage: M.has_minor(M, True)
            (True,
             (frozenset(),
              frozenset(),
              {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}))"""
    @overload
    def has_minor(self, M, _True) -> Any:
        """Matroid.has_minor(self, N, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4342)

        Check if ``self`` has a minor isomorphic to ``N``,
        and optionally return frozensets ``X`` and ``Y`` so that ``N`` is isomorphic to ``self.minor(X, Y)``.

        INPUT:

        - ``N`` -- an instance of a :class:`Matroid` object
        - ``certificate`` -- boolean (default: ``False``); if ``True``, returns
          ``True, (X, Y, dic)`` where ``N`` is isomorphic to
          ``self.minor(X, Y)``, and ``dic`` is an isomorphism between ``N`` and
          ``self.minor(X, Y)``

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.minor() <sage.matroids.matroid.Matroid.minor>`,
            :meth:`M.is_isomorphic() <sage.matroids.matroid.Matroid.is_isomorphic>`

        .. TODO::

            This important method can (and should) be optimized considerably.
            See [Hli2006]_ p.1219 for hints to that end.

        EXAMPLES::

            sage: M = matroids.Whirl(3)
            sage: matroids.catalog.Fano().has_minor(M)
            False
            sage: matroids.catalog.NonFano().has_minor(M)
            True
            sage: matroids.catalog.NonFano().has_minor(M, certificate=True)
            (True, (frozenset(), frozenset({...}), {...}))
            sage: M = matroids.catalog.Fano()
            sage: M.has_minor(M, True)
            (True,
             (frozenset(),
              frozenset(),
              {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}))"""
    @overload
    def hyperplanes(self) -> SetSystem:
        """Matroid.hyperplanes(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3063)

        Return the hyperplanes of the matroid.

        A *hyperplane* is a flat of rank ``self.full_rank() - 1``. A *flat* is
        a closed set.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 3)
            sage: sorted([sorted(F) for F in M.hyperplanes()])
            [[0], [1], [2]]"""
    @overload
    def hyperplanes(self) -> Any:
        """Matroid.hyperplanes(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3063)

        Return the hyperplanes of the matroid.

        A *hyperplane* is a flat of rank ``self.full_rank() - 1``. A *flat* is
        a closed set.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 3)
            sage: sorted([sorted(F) for F in M.hyperplanes()])
            [[0], [1], [2]]"""
    def independence_matroid_polytope(self) -> Any:
        """Matroid.independence_matroid_polytope(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3477)

        Return the independence matroid polytope of ``self``.

        This is defined as the convex hull of the vertices

        .. MATH::

            \\sum_{i \\in I} e_i

        over all independent sets `I` of the matroid. Here `e_i` are
        the standard basis vectors of `\\RR^n`. An arbitrary labelling
        of the groundset by `\\{0,\\ldots,n-1\\}` is chosen.

        .. SEEALSO::

            :meth:`matroid_polytope`

        EXAMPLES::

            sage: M = matroids.Whirl(4)
            sage: M.independence_matroid_polytope()                                     # needs sage.geometry.polyhedron sage.rings.finite_rings
            A 8-dimensional polyhedron in ZZ^8 defined as the convex hull
            of 135 vertices

            sage: M = matroids.catalog.NonFano()
            sage: M.independence_matroid_polytope()                                     # needs sage.geometry.polyhedron sage.rings.finite_rings
            A 7-dimensional polyhedron in ZZ^7 defined as the convex hull
            of 58 vertices

        REFERENCES:

        [DLHK2007]_"""
    def independent_r_sets(self, *args, **kwargs):
        """Deprecated: Use :meth:`independent_sets` instead.
        See :issue:`38057` for details.

        """
    @overload
    def independent_sets(self, longk=...) -> SetSystem:
        """Matroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2806)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: I = M.independent_sets()
            sage: len(I)
            121
            sage: M.independent_sets(4)
            SetSystem of 0 sets over 9 elements
            sage: S = M.independent_sets(3); S
            SetSystem of 75 sets over 9 elements
            sage: frozenset({'a', 'c', 'e'}) in S
            True

        .. SEEALSO::

            :meth:`M.bases() <sage.matroids.matroid.Matroid.bases>`"""
    @overload
    def independent_sets(self) -> Any:
        """Matroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2806)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: I = M.independent_sets()
            sage: len(I)
            121
            sage: M.independent_sets(4)
            SetSystem of 0 sets over 9 elements
            sage: S = M.independent_sets(3); S
            SetSystem of 75 sets over 9 elements
            sage: frozenset({'a', 'c', 'e'}) in S
            True

        .. SEEALSO::

            :meth:`M.bases() <sage.matroids.matroid.Matroid.bases>`"""
    @overload
    def independent_sets_iterator(self, k=...) -> Any:
        """Matroid.independent_sets_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2873)

        Return an iterator over the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return an iterator over
          the size-`k` independent sets of the matroid

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: I = list(M.independent_sets_iterator())
            sage: len(I)
            121
            sage: M = matroids.catalog.Pappus()
            sage: list(M.independent_sets_iterator(4))
            []
            sage: S = list(M.independent_sets_iterator(3))
            sage: len(S)
            75
            sage: frozenset({'a', 'c', 'e'}) in S
            True

        .. SEEALSO::

            :meth:`M.bases_iterator() <sage.matroids.matroid.Matroid.bases_iterator>`"""
    @overload
    def independent_sets_iterator(self) -> Any:
        """Matroid.independent_sets_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2873)

        Return an iterator over the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return an iterator over
          the size-`k` independent sets of the matroid

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: I = list(M.independent_sets_iterator())
            sage: len(I)
            121
            sage: M = matroids.catalog.Pappus()
            sage: list(M.independent_sets_iterator(4))
            []
            sage: S = list(M.independent_sets_iterator(3))
            sage: len(S)
            75
            sage: frozenset({'a', 'c', 'e'}) in S
            True

        .. SEEALSO::

            :meth:`M.bases_iterator() <sage.matroids.matroid.Matroid.bases_iterator>`"""
    @overload
    def intersection(self, other, weights=...) -> Any:
        """Matroid.intersection(self, other, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7356)

        Return a maximum-weight common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`. The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid
        - ``weights`` -- (default: ``None``) a dictionary which specifies a
          weight for each element of the common groundset; defaults to the
          all-1 weight function

        OUTPUT: a subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: w = {'a':30, 'b':10, 'c':11, 'd':20, 'e':70, 'f':21, 'g':90,
            ....:      'h':12, 'i':80, 'j':13, 'k':40, 'l':21}
            sage: Y = M.intersection(N, w)
            sage: sorted(Y)
            ['a', 'd', 'e', 'g', 'i', 'k']
            sage: sum([w[y] for y in Y])
            330
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    @overload
    def intersection(self, N, w) -> Any:
        """Matroid.intersection(self, other, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7356)

        Return a maximum-weight common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`. The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid
        - ``weights`` -- (default: ``None``) a dictionary which specifies a
          weight for each element of the common groundset; defaults to the
          all-1 weight function

        OUTPUT: a subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: w = {'a':30, 'b':10, 'c':11, 'd':20, 'e':70, 'f':21, 'g':90,
            ....:      'h':12, 'i':80, 'j':13, 'k':40, 'l':21}
            sage: Y = M.intersection(N, w)
            sage: sorted(Y)
            ['a', 'd', 'e', 'g', 'i', 'k']
            sage: sum([w[y] for y in Y])
            330
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    @overload
    def intersection(self, N) -> Any:
        """Matroid.intersection(self, other, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7356)

        Return a maximum-weight common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`. The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid
        - ``weights`` -- (default: ``None``) a dictionary which specifies a
          weight for each element of the common groundset; defaults to the
          all-1 weight function

        OUTPUT: a subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: w = {'a':30, 'b':10, 'c':11, 'd':20, 'e':70, 'f':21, 'g':90,
            ....:      'h':12, 'i':80, 'j':13, 'k':40, 'l':21}
            sage: Y = M.intersection(N, w)
            sage: sorted(Y)
            ['a', 'd', 'e', 'g', 'i', 'k']
            sage: sum([w[y] for y in Y])
            330
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    @overload
    def intersection_unweighted(self, other) -> Any:
        """Matroid.intersection_unweighted(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7541)

        Return a maximum-cardinality common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid

        OUTPUT: subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: len(M.intersection_unweighted(N))
            6
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection_unweighted(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    @overload
    def intersection_unweighted(self, N) -> Any:
        """Matroid.intersection_unweighted(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7541)

        Return a maximum-cardinality common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid

        OUTPUT: subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: len(M.intersection_unweighted(N))
            6
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection_unweighted(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    @overload
    def intersection_unweighted(self, N) -> Any:
        """Matroid.intersection_unweighted(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7541)

        Return a maximum-cardinality common independent set.

        A *common independent set* of matroids `M` and `N` with the same
        groundset `E` is a subset of `E` that is independent both in `M` and
        `N`.

        INPUT:

        - ``other`` -- a second matroid with the same groundset as this
          matroid

        OUTPUT: subset of the groundset

        EXAMPLES::

            sage: M = matroids.catalog.T12()
            sage: N = matroids.catalog.ExtendedTernaryGolayCode()
            sage: len(M.intersection_unweighted(N))
            6
            sage: M = matroids.catalog.Fano()
            sage: N = matroids.Uniform(4, 7)
            sage: M.intersection_unweighted(N)
            Traceback (most recent call last):
            ...
            ValueError: matroid intersection requires equal groundsets."""
    def is_3connected(self, certificate=..., algorithm=...) -> Any:
        """Matroid.is_3connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5459)

        Return ``True`` if the matroid is 3-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        A `k`-*separation* in a matroid is a partition `(X, Y)` of the
        groundset with `|X| \\geq k, |Y| \\geq k` and `r(X) + r(Y) - r(M) < k`.
        A matroid is `k`-*connected* if it has no `l`-separations for `l < k`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 3-connected,
          and ``False,`` `X` otherwise, where `X` is a `<3`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 3-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'bridges'`` -- Bixby and Cunningham's algorithm, based on bridges
            [BC1977]_; note that this cannot return a separator
          - ``'intersection'`` -- an algorithm based on matroid intersection
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_4connected() <sage.matroids.matroid.Matroid.is_4connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        ALGORITHM:

        - Bridges based: The 3-connectivity algorithm from [BC1977]_ which runs in `O((r(E))^2|E|)` time.
        - Matroid intersection based: Evaluates the connectivity between `O(|E|^2)` pairs of disjoint
          sets `S`, `T` with `|S| = |T| = 2`.
        - Shifting algorithm: The shifting algorithm from [Raj1987]_ which runs in `O((r(E))^2|E|)` time.

        EXAMPLES::

            sage: matroids.Uniform(2, 3).is_3connected()
            True
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: M.is_3connected()
            False
            sage: M.is_3connected() == M.is_3connected(algorithm='bridges')
            True
            sage: M.is_3connected() == M.is_3connected(algorithm='intersection')
            True
            sage: N = Matroid(circuit_closures={2: ['abc', 'cdef'],
            ....:                               3: ['abcdef']},
            ....:             groundset='abcdef')
            sage: N.is_3connected()
            False
            sage: matroids.catalog.BetsyRoss().is_3connected()                          # needs sage.graphs
            True
            sage: M = matroids.catalog.R6()
            sage: M.is_3connected()                                                     # needs sage.graphs
            False
            sage: B, X = M.is_3connected(True)
            sage: M.connectivity(X)
            1"""
    @overload
    def is_4connected(self, certificate=..., algorithm=...) -> Any:
        """Matroid.is_4connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5537)

        Return ``True`` if the matroid is 4-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 4-connected,
          and ``False,`` `X` otherwise, where `X` is a `<4`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 4-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'intersection'`` -- an algorithm based on matroid intersection, equivalent
            to calling ``is_kconnected(4, certificate)``
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 6)
            sage: B, X = M.is_4connected(True)
            sage: (B, M.connectivity(X)<=3)
            (False, True)
            sage: matroids.Uniform(4, 8).is_4connected()
            True
            sage: M = Matroid(field=GF(2), matrix=[[1,0,0,1,0,1,1,0,0,1,1,1],
            ....:                                  [0,1,0,1,0,1,0,1,0,0,0,1],
            ....:                                  [0,0,1,1,0,0,1,1,0,1,0,1],
            ....:                                  [0,0,0,0,1,1,1,1,0,0,1,1],
            ....:                                  [0,0,0,0,0,0,0,0,1,1,1,1]])
            sage: M.is_4connected() == M.is_4connected(algorithm='shifting')            # needs sage.graphs
            True
            sage: M.is_4connected() == M.is_4connected(algorithm='intersection')
            True"""
    @overload
    def is_4connected(self, _True) -> Any:
        """Matroid.is_4connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5537)

        Return ``True`` if the matroid is 4-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 4-connected,
          and ``False,`` `X` otherwise, where `X` is a `<4`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 4-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'intersection'`` -- an algorithm based on matroid intersection, equivalent
            to calling ``is_kconnected(4, certificate)``
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 6)
            sage: B, X = M.is_4connected(True)
            sage: (B, M.connectivity(X)<=3)
            (False, True)
            sage: matroids.Uniform(4, 8).is_4connected()
            True
            sage: M = Matroid(field=GF(2), matrix=[[1,0,0,1,0,1,1,0,0,1,1,1],
            ....:                                  [0,1,0,1,0,1,0,1,0,0,0,1],
            ....:                                  [0,0,1,1,0,0,1,1,0,1,0,1],
            ....:                                  [0,0,0,0,1,1,1,1,0,0,1,1],
            ....:                                  [0,0,0,0,0,0,0,0,1,1,1,1]])
            sage: M.is_4connected() == M.is_4connected(algorithm='shifting')            # needs sage.graphs
            True
            sage: M.is_4connected() == M.is_4connected(algorithm='intersection')
            True"""
    @overload
    def is_4connected(self) -> Any:
        """Matroid.is_4connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5537)

        Return ``True`` if the matroid is 4-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 4-connected,
          and ``False,`` `X` otherwise, where `X` is a `<4`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 4-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'intersection'`` -- an algorithm based on matroid intersection, equivalent
            to calling ``is_kconnected(4, certificate)``
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 6)
            sage: B, X = M.is_4connected(True)
            sage: (B, M.connectivity(X)<=3)
            (False, True)
            sage: matroids.Uniform(4, 8).is_4connected()
            True
            sage: M = Matroid(field=GF(2), matrix=[[1,0,0,1,0,1,1,0,0,1,1,1],
            ....:                                  [0,1,0,1,0,1,0,1,0,0,0,1],
            ....:                                  [0,0,1,1,0,0,1,1,0,1,0,1],
            ....:                                  [0,0,0,0,1,1,1,1,0,0,1,1],
            ....:                                  [0,0,0,0,0,0,0,0,1,1,1,1]])
            sage: M.is_4connected() == M.is_4connected(algorithm='shifting')            # needs sage.graphs
            True
            sage: M.is_4connected() == M.is_4connected(algorithm='intersection')
            True"""
    @overload
    def is_4connected(self, algorithm=...) -> Any:
        """Matroid.is_4connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5537)

        Return ``True`` if the matroid is 4-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 4-connected,
          and ``False,`` `X` otherwise, where `X` is a `<4`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 4-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'intersection'`` -- an algorithm based on matroid intersection, equivalent
            to calling ``is_kconnected(4, certificate)``
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 6)
            sage: B, X = M.is_4connected(True)
            sage: (B, M.connectivity(X)<=3)
            (False, True)
            sage: matroids.Uniform(4, 8).is_4connected()
            True
            sage: M = Matroid(field=GF(2), matrix=[[1,0,0,1,0,1,1,0,0,1,1,1],
            ....:                                  [0,1,0,1,0,1,0,1,0,0,0,1],
            ....:                                  [0,0,1,1,0,0,1,1,0,1,0,1],
            ....:                                  [0,0,0,0,1,1,1,1,0,0,1,1],
            ....:                                  [0,0,0,0,0,0,0,0,1,1,1,1]])
            sage: M.is_4connected() == M.is_4connected(algorithm='shifting')            # needs sage.graphs
            True
            sage: M.is_4connected() == M.is_4connected(algorithm='intersection')
            True"""
    @overload
    def is_4connected(self, algorithm=...) -> Any:
        """Matroid.is_4connected(self, certificate=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5537)

        Return ``True`` if the matroid is 4-connected, ``False`` otherwise. It can
        optionally return a separator as a witness.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is 4-connected,
          and ``False,`` `X` otherwise, where `X` is a `<4`-separation
        - ``algorithm`` -- (default: ``None``) specify which algorithm
          to compute 4-connectivity:

          - ``None`` -- the most appropriate algorithm is chosen automatically
          - ``'intersection'`` -- an algorithm based on matroid intersection, equivalent
            to calling ``is_kconnected(4, certificate)``
          - ``'shifting'`` -- an algorithm based on the shifting algorithm [Raj1987]_

        OUTPUT: boolean, or a tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_kconnected() <sage.matroids.matroid.Matroid.is_kconnected>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 6)
            sage: B, X = M.is_4connected(True)
            sage: (B, M.connectivity(X)<=3)
            (False, True)
            sage: matroids.Uniform(4, 8).is_4connected()
            True
            sage: M = Matroid(field=GF(2), matrix=[[1,0,0,1,0,1,1,0,0,1,1,1],
            ....:                                  [0,1,0,1,0,1,0,1,0,0,0,1],
            ....:                                  [0,0,1,1,0,0,1,1,0,1,0,1],
            ....:                                  [0,0,0,0,1,1,1,1,0,0,1,1],
            ....:                                  [0,0,0,0,0,0,0,0,1,1,1,1]])
            sage: M.is_4connected() == M.is_4connected(algorithm='shifting')            # needs sage.graphs
            True
            sage: M.is_4connected() == M.is_4connected(algorithm='intersection')
            True"""
    def is_basis(self, X) -> Any:
        """Matroid.is_basis(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1985)

        Check if a subset is a basis of the matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_basis('abc')
            False
            sage: M.is_basis('abce')
            True
            sage: M.is_basis('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    @overload
    def is_binary(self, randomized_tests=...) -> Any:
        """Matroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6390)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        binary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.is_binary()
            False"""
    @overload
    def is_binary(self) -> Any:
        """Matroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6390)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        binary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.is_binary()
            False"""
    @overload
    def is_binary(self) -> Any:
        """Matroid.is_binary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6390)

        Decide if ``self`` is a binary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being binary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the binary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        binary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.binary_matroid()
            <sage.matroids.matroid.Matroid.binary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_binary()
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.is_binary()
            False"""
    def is_chordal(self, k1=..., k2=..., boolcertificate=...) -> Any:
        """Matroid.is_chordal(self, k1=4, k2=None, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6795)

        Return if a matroid is ``[k1, k2]``-chordal.

        A matroid `M` is `[k_1, k_2]`-chordal if every circuit of length
        `\\ell` with `k_1 \\leq \\ell \\leq k_2` has a
        :meth:`chord <sage.matroids.matroid.Matroid.is_circuit_chordal>`.
        We say `M` is `k`-chordal if `k_1 = k` and `k_2 = \\infty`.
        We call `M` *chordal* if it is `4`-chordal.

        INPUT:

        - ``k1`` -- (optional) the integer `k_1`
        - ``k2`` -- (optional) the integer `k_2`; if not specified,
          then this method returns if ``self`` is `k_1`-chordal
        - ``certificate`` -- boolean (default: ``False``);  if
          ``True`` return ``True, C``, where ``C`` is a non
          ``k1`` ``k2`` circuit

        OUTPUT: boolean or tuple

        .. SEEALSO::

            :meth:`M.chordality() <sage.matroids.matroid.Matroid.chordality>`

        EXAMPLES::

            sage: M = matroids.Uniform(2,4)
            sage: [M.is_chordal(i) for i in range(4, 8)]
            [True, True, True, True]
            sage: M = matroids.catalog.NonFano()
            sage: [M.is_chordal(i) for i in range(4, 8)]
            [False, True, True, True]
            sage: M = matroids.catalog.N2()
            sage: [M.is_chordal(i) for i in range(4, 10)]
            [False, False, False, False, True, True]
            sage: M.is_chordal(4, 5)
            False
            sage: M.is_chordal(4, 5, certificate=True)
            (False, frozenset({...}))"""
    def is_circuit(self, X) -> Any:
        """Matroid.is_circuit(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2096)

        Test if a subset is a circuit of the matroid.

        A *circuit* is an inclusionwise minimal dependent subset.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_circuit('abc')
            False
            sage: M.is_circuit('abcd')
            True
            sage: M.is_circuit('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_circuit_chordal(self, C, boolcertificate=...) -> Any:
        """Matroid.is_circuit_chordal(self, C, bool certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6755)

        Check if the circuit ``C`` has a chord.

        A circuit `C` in a matroid `M` has a *chord* `x \\in E` if there
        exists sets `A, B` such that `C = A \\sqcup B` and `A + x` and
        `B + x` are circuits.

        INPUT:

        - ``C`` -- a circuit
        - ``certificate`` -- boolean (default: ``False``); if ``True``
          return ``True, (x, Ax, Bx)``, where ``x`` is a chord and ``Ax`` and
          ``Bx`` are circuits whose union is the elements of ``C``
          together with ``x``, if ``False`` return ``False, None``

        OUTPUT: boolean or tuple

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.is_circuit_chordal(['b','c','d'])
            False
            sage: M.is_circuit_chordal(['b','c','d'], certificate=True)
            (False, None)
            sage: M.is_circuit_chordal(['a','b','d','e'])
            True
            sage: X = M.is_circuit_chordal(frozenset(['a','b','d','e']),
            ....:                          certificate=True)[1]
            sage: X  # random
            ('c', frozenset({'b', 'c', 'd'}), frozenset({'a', 'c', 'e'}))
            sage: M.is_circuit(X[1]) and M.is_circuit(X[2])
            True
            sage: X[1].intersection(X[2]) == frozenset([X[0]])
            True"""
    def is_closed(self, X) -> Any:
        """Matroid.is_closed(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2012)

        Test if a subset is a closed set of the matroid.

        A set is *closed* if adding any element to it will increase the rank
        of the set.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_closed('abc')
            False
            sage: M.is_closed('abcd')
            True
            sage: M.is_closed('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_cobasis(self, X) -> Any:
        """Matroid.is_cobasis(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2209)

        Check if a subset is a cobasis of the matroid.

        A *cobasis* is the complement of a basis. It is a basis of the dual
        matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.is_basis() <sage.matroids.matroid.Matroid.is_basis>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_cobasis('abc')
            False
            sage: M.is_cobasis('abce')
            True
            sage: M.is_cobasis('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_cocircuit(self, X) -> Any:
        """Matroid.is_cocircuit(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2244)

        Test if a subset is a cocircuit of the matroid.

        A *cocircuit* is an inclusionwise minimal subset that is dependent in
        the dual matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.is_circuit() <sage.matroids.matroid.Matroid.is_circuit>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_cocircuit('abc')
            False
            sage: M.is_cocircuit('abcd')
            True
            sage: M.is_cocircuit('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_coclosed(self, X) -> Any:
        """Matroid.is_coclosed(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2276)

        Test if a subset is a coclosed set of the matroid.

        A set is *coclosed* if it is a closed set of the dual matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.is_closed() <sage.matroids.matroid.Matroid.is_closed>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_coclosed('abc')
            False
            sage: M.is_coclosed('abcd')
            True
            sage: M.is_coclosed('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_codependent(self, X) -> Any:
        """Matroid.is_codependent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2178)

        Check if a subset is codependent in the matroid.

        A set is *codependent* if it is dependent in the dual of the matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.is_dependent() <sage.matroids.matroid.Matroid.is_dependent>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_codependent('abc')
            False
            sage: M.is_codependent('abcd')
            True
            sage: M.is_codependent('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_coindependent(self, X) -> Any:
        """Matroid.is_coindependent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2147)

        Check if a subset is coindependent in the matroid.

        A set is *coindependent* if it is independent in the dual matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.is_independent() <sage.matroids.matroid.Matroid.is_independent>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_coindependent('abc')
            True
            sage: M.is_coindependent('abcd')
            False
            sage: M.is_coindependent('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    def is_connected(self, certificate=...) -> Any:
        """Matroid.is_connected(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5094)

        Test if the matroid is connected.

        A *separation* in a matroid is a partition `(X, Y)` of the
        groundset with `X, Y` nonempty and `r(X) + r(Y) = r(X\\cup Y)`.
        A matroid is *connected* if it has no separations.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.components() <sage.matroids.matroid.Matroid.components>`,
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`

        EXAMPLES::

            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: M.is_connected()
            False
            sage: matroids.catalog.Pappus().is_connected()
            True"""
    @overload
    def is_cosimple(self) -> Any:
        """Matroid.is_cosimple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5021)

        Test if the matroid is cosimple.

        A matroid is *cosimple* if it contains no cocircuits of length 1 or 2.

        Dual method of
        :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`,
            :meth:`M.coloops() <sage.matroids.matroid.Matroid.coloops>`,
            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.cosimplify() <sage.matroids.matroid.Matroid.cosimplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: M.is_cosimple()
            True
            sage: N = M.delete('a')
            sage: N.is_cosimple()
            False"""
    @overload
    def is_cosimple(self) -> Any:
        """Matroid.is_cosimple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5021)

        Test if the matroid is cosimple.

        A matroid is *cosimple* if it contains no cocircuits of length 1 or 2.

        Dual method of
        :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`,
            :meth:`M.coloops() <sage.matroids.matroid.Matroid.coloops>`,
            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.cosimplify() <sage.matroids.matroid.Matroid.cosimplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: M.is_cosimple()
            True
            sage: N = M.delete('a')
            sage: N.is_cosimple()
            False"""
    @overload
    def is_cosimple(self) -> Any:
        """Matroid.is_cosimple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5021)

        Test if the matroid is cosimple.

        A matroid is *cosimple* if it contains no cocircuits of length 1 or 2.

        Dual method of
        :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`,
            :meth:`M.coloops() <sage.matroids.matroid.Matroid.coloops>`,
            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.cosimplify() <sage.matroids.matroid.Matroid.cosimplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: M.is_cosimple()
            True
            sage: N = M.delete('a')
            sage: N.is_cosimple()
            False"""
    def is_dependent(self, X) -> Any:
        """Matroid.is_dependent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1961)

        Check if a subset ``X`` is dependent in the matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_dependent('abc')
            False
            sage: M.is_dependent('abcd')
            True
            sage: M.is_dependent('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    @overload
    def is_graphic(self) -> bool:
        """Matroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6606)

        Return if ``self`` is graphic.

        A matroid is graphic if and only if it has no minor isomorphic to any
        of the matroids `U_{2, 4}`, `F_7`, `F_7^*`, `M^*(K_5)`, and
        `M^*(K_{3, 3})`.

        EXAMPLES::

            sage: M = matroids.catalog.Wheel4()
            sage: M.is_graphic()
            True
            sage: M = matroids.catalog.U24()
            sage: M.is_graphic()
            False

        REFERENCES:

        [Oxl2011]_, p. 385."""
    @overload
    def is_graphic(self) -> Any:
        """Matroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6606)

        Return if ``self`` is graphic.

        A matroid is graphic if and only if it has no minor isomorphic to any
        of the matroids `U_{2, 4}`, `F_7`, `F_7^*`, `M^*(K_5)`, and
        `M^*(K_{3, 3})`.

        EXAMPLES::

            sage: M = matroids.catalog.Wheel4()
            sage: M.is_graphic()
            True
            sage: M = matroids.catalog.U24()
            sage: M.is_graphic()
            False

        REFERENCES:

        [Oxl2011]_, p. 385."""
    @overload
    def is_graphic(self) -> Any:
        """Matroid.is_graphic(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6606)

        Return if ``self`` is graphic.

        A matroid is graphic if and only if it has no minor isomorphic to any
        of the matroids `U_{2, 4}`, `F_7`, `F_7^*`, `M^*(K_5)`, and
        `M^*(K_{3, 3})`.

        EXAMPLES::

            sage: M = matroids.catalog.Wheel4()
            sage: M.is_graphic()
            True
            sage: M = matroids.catalog.U24()
            sage: M.is_graphic()
            False

        REFERENCES:

        [Oxl2011]_, p. 385."""
    def is_independent(self, X) -> Any:
        """Matroid.is_independent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1937)

        Check if a subset ``X`` is independent in the matroid.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_independent('abc')
            True
            sage: M.is_independent('abcd')
            False
            sage: M.is_independent('abcx')
            Traceback (most recent call last):
            ...
            ValueError: 'abcx' is not a subset of the groundset"""
    @overload
    def is_isomorphic(self, other, certificate=...) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphic(self, M2) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphic(self, M2, certificate=...) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphic(self, G3) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphic(self, M2) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphic(self, M2, certificate=...) -> Any:
        """Matroid.is_isomorphic(self, other, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3527)

        Test matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.

        INPUT:

        - ``other`` -- matroid
        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, and, if ``certificate=True``, a dictionary or
        ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: M1.is_isomorphic(M2)                                                  # needs sage.graphs
            True
            sage: M1.is_isomorphic(M2, certificate=True)                                # needs sage.graphs
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4})
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.is_isomorphic(G3)                                                  # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.


            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.is_isomorphic(M2)
            False
            sage: M1.is_isomorphic(M2, certificate=True)
            (False, None)"""
    @overload
    def is_isomorphism(self, other, morphism) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, N, morphism) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, M, P) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, M, f) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, N, f) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, M, f) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    @overload
    def is_isomorphism(self, M, g) -> Any:
        """Matroid.is_isomorphism(self, other, morphism)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3761)

        Test if a provided morphism induces a matroid isomorphism.

        A *morphism* is a map from the groundset of ``self`` to the groundset
        of ``other``.

        INPUT:

        - ``other`` -- matroid
        - ``morphism`` -- a map; can be, for instance, a dictionary, function,
          or permutation

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_isomorphism() <sage.matroids.matroid.Matroid.is_isomorphism>`

        .. NOTE::

            If you know the input is valid, consider using the faster method
            ``self._is_isomorphism``.

        EXAMPLES:

        ::

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: N.is_isomorphism(M, {e:e for e in M.groundset()})
            False

            sage: M = matroids.catalog.Fano().delete(['g'])
            sage: N = matroids.Wheel(3)
            sage: morphism = {'a':0, 'b':1, 'c': 2, 'd':4, 'e':5, 'f':3}
            sage: M.is_isomorphism(N, morphism)
            True

        A morphism can be specified as a dictionary (above), a permutation,
        a function, and many other types of maps::

            sage: M = matroids.catalog.Fano()
            sage: P = PermutationGroup([[('a', 'b', 'c'),                               # needs sage.rings.finite_rings
            ....:                        ('d', 'e', 'f'), ('g')]]).gen()
            sage: M.is_isomorphism(M, P)                                                # needs sage.rings.finite_rings
            True

            sage: M = matroids.catalog.Pappus()
            sage: N = matroids.catalog.NonPappus()
            sage: def f(x):
            ....:     return x
            ....:
            sage: N.is_isomorphism(M, f)
            False
            sage: N.is_isomorphism(N, f)
            True

        There is extensive checking for inappropriate input::

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: M.is_isomorphism(graphs.CompleteGraph(4), lambda x: x)
            Traceback (most recent call last):
            ...
            TypeError: can only test for isomorphism between matroids.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 2, 2: 3})
            Traceback (most recent call last):
            ...
            ValueError: domain of morphism does not contain groundset of this
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(4)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
            sage: M.is_isomorphism(M, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
            Traceback (most recent call last):
            ...
            ValueError: range of morphism does not contain groundset of other
            matroid.

            sage: # needs sage.graphs
            sage: M = matroids.CompleteGraphic(3)
            sage: N = Matroid(bases=['ab', 'ac', 'bc'])
            sage: f = [0, 1, 2]
            sage: g = {'a': 0, 'b': 1, 'c': 2}
            sage: N.is_isomorphism(M, f)
            Traceback (most recent call last):
            ...
            ValueError: the morphism argument does not seem to be an
            isomorphism.

            sage: # needs sage.graphs
            sage: N.is_isomorphism(M, g)
            True

        TESTS:

        Check that :issue:`35946` is fixed::

            sage: M = matroids.Uniform(3,5)
            sage: N = matroids.Uniform(2,5)
            sage: M.is_isomorphism(N, {e: e for e in M.groundset()})
            False"""
    def is_k_closed(self, intk) -> Any:
        """Matroid.is_k_closed(self, int k)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6673)

        Return if ``self`` is a ``k``-closed matroid.

        We say a matroid is `k`-closed if all `k`-closed subsets
        are closed in ``M``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: PR = RootSystem(['A',4]).root_lattice().positive_roots()
            sage: m = matrix([x.to_vector() for x in PR]).transpose()
            sage: M = Matroid(m)
            sage: M.is_k_closed(3)
            True
            sage: M.is_k_closed(4)
            True

            sage: # needs sage.combinat
            sage: PR = RootSystem(['D',4]).root_lattice().positive_roots()
            sage: m = matrix([x.to_vector() for x in PR]).transpose()
            sage: M = Matroid(m)
            sage: M.is_k_closed(3)
            False
            sage: M.is_k_closed(4)
            True"""
    def is_kconnected(self, k, certificate=...) -> Any:
        """Matroid.is_kconnected(self, k, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5335)

        Return ``True`` if the matroid is `k`-connected, ``False`` otherwise.  It can
        optionally return a separator as a witness.

        INPUT:

        - ``k`` -- integer greater or equal to 1
        - ``certificate`` -- boolean (default: ``False``); if ``True``,
          then return ``True, None`` if the matroid is k-connected,
          and ``False, X`` otherwise, where ``X`` is a `<k`-separation

        OUTPUT: boolean or tuple ``(boolean, frozenset)``

        .. SEEALSO::

            :meth:`M.is_connected() <sage.matroids.matroid.Matroid.is_connected>`
            :meth:`M.is_3connected() <sage.matroids.matroid.Matroid.is_3connected>`
            :meth:`M.is_4connected() <sage.matroids.matroid.Matroid.is_4connected>`

        ALGORITHM:

        Apply linking algorithm to find small separator.

        EXAMPLES::

            sage: matroids.Uniform(2, 3).is_kconnected(3)
            True
            sage: M = Matroid(ring=QQ, matrix=[[1, 0, 0, 1, 1, 0],
            ....:                              [0, 1, 0, 1, 2, 0],
            ....:                              [0, 0, 1, 0, 0, 1]])
            sage: M.is_kconnected(3)
            False
            sage: N = Matroid(circuit_closures={2: ['abc', 'cdef'],
            ....:                               3: ['abcdef']},
            ....:             groundset='abcdef')
            sage: N.is_kconnected(3)
            False
            sage: matroids.catalog.BetsyRoss().is_kconnected(3)                         # needs sage.graphs
            True
            sage: matroids.AG(5,2).is_kconnected(4)
            True
            sage: M = matroids.catalog.R6()
            sage: M.is_kconnected(3)                                                    # needs sage.graphs
            False
            sage: B, X = M.is_kconnected(3,True)
            sage: M.connectivity(X)<3
            True"""
    @overload
    def is_max_weight_coindependent_generic(self, X=..., weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_coindependent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_coindependent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7202)

        Test if only one cobasis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by increasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are coindependent
        of all that was selected before. If an element is not coindependent of the
        previously selected elements, then we check if it is coindependent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_coindependent_generic(weights=wt)
            True
            sage: M.is_max_weight_coindependent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_coindependent_generic()
            False

            sage: M = matroids.Uniform(2, 5)
            sage: wt = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.dual().is_max_weight_coindependent_generic(weights=wt)
            True

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_coindependent_generic()
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_coindependent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            False

            sage: M.is_max_weight_coindependent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, X=..., weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_max_weight_independent_generic(self, weights=...) -> Any:
        """Matroid.is_max_weight_independent_generic(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7055)

        Test if only one basis of the subset ``X`` has maximal
        weight.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: boolean

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before. If an element is not independent of the
        previously selected elements, then we check if it is independent with the
        previously selected elements with higher weight.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: M.is_max_weight_independent_generic()
            False

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: M.is_max_weight_independent_generic(weights=wt)
            True
            sage: M.is_max_weight_independent_generic(weights={x: x for x in M.groundset()})
            True
            sage: M.is_max_weight_independent_generic()
            False

        Here is an example from [GriRei18]_ (Example 7.4.12 in v6)::

            sage: A = Matrix(QQ, [[ 1,  1,  0,  0],
            ....:                 [-1,  0,  1,  1],
            ....:                 [ 0, -1, -1, -1]])
            sage: M = Matroid(A)
            sage: M.is_max_weight_independent_generic()
            False
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 3, 3: 2})
            True
            sage: M.is_max_weight_independent_generic(weights={0: 1, 1: 3, 2: 2, 3: 2})
            False
            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: 1, 3: 1})
            True

            sage: M.is_max_weight_independent_generic(weights={0: 2, 1: 3, 2: -1, 3: 1})
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected."""
    @overload
    def is_paving(self) -> bool:
        """Matroid.is_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6195)

        Return if ``self`` is paving.

        A matroid is paving if each of its circuits has size `r` or `r+1`.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_paving()
            True
            sage: M = matroids.Theta(4)
            sage: M.is_paving()
            False

        REFERENCES:

        [Oxl2011]_, p. 24."""
    @overload
    def is_paving(self) -> Any:
        """Matroid.is_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6195)

        Return if ``self`` is paving.

        A matroid is paving if each of its circuits has size `r` or `r+1`.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_paving()
            True
            sage: M = matroids.Theta(4)
            sage: M.is_paving()
            False

        REFERENCES:

        [Oxl2011]_, p. 24."""
    @overload
    def is_paving(self) -> Any:
        """Matroid.is_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6195)

        Return if ``self`` is paving.

        A matroid is paving if each of its circuits has size `r` or `r+1`.

        OUTPUT: boolean

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_paving()
            True
            sage: M = matroids.Theta(4)
            sage: M.is_paving()
            False

        REFERENCES:

        [Oxl2011]_, p. 24."""
    def is_regular(self) -> bool:
        """Matroid.is_regular(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6640)

        Return if ``self`` is regular.

        A regular matroid is one that can be represented by a totally
        unimodular matrix, the latter being a matrix over `\\mathbb{R}` for
        which every square submatrix has determinant in `\\{0, 1, -1\\}`. A
        matroid is regular if and only if it is representable over every field.
        Alternatively, a matroid is regular if and only if it has no minor
        isomorphic to `U_{2, 4}`, `F_7`, or `F_7^*`.

        EXAMPLES::

            sage: M = matroids.catalog.Wheel4()
            sage: M.is_regular()
            True
            sage: M = matroids.catalog.R9()
            sage: M.is_regular()
            False

        REFERENCES:

        [Oxl2011]_, p. 373."""
    @overload
    def is_simple(self) -> Any:
        """Matroid.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4990)

        Test if the matroid is simple.

        A matroid is *simple* if it contains no circuits of length 1 or 2.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_cosimple() <sage.matroids.matroid.Matroid.is_cosimple>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.simplify() <sage.matroids.matroid.Matroid.simplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.is_simple()
            True
            sage: N = M / 'a'
            sage: N.is_simple()
            False"""
    @overload
    def is_simple(self) -> Any:
        """Matroid.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4990)

        Test if the matroid is simple.

        A matroid is *simple* if it contains no circuits of length 1 or 2.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_cosimple() <sage.matroids.matroid.Matroid.is_cosimple>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.simplify() <sage.matroids.matroid.Matroid.simplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.is_simple()
            True
            sage: N = M / 'a'
            sage: N.is_simple()
            False"""
    @overload
    def is_simple(self) -> Any:
        """Matroid.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4990)

        Test if the matroid is simple.

        A matroid is *simple* if it contains no circuits of length 1 or 2.

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.is_cosimple() <sage.matroids.matroid.Matroid.is_cosimple>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.simplify() <sage.matroids.matroid.Matroid.simplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.is_simple()
            True
            sage: N = M / 'a'
            sage: N.is_simple()
            False"""
    @overload
    def is_sparse_paving(self) -> bool:
        """Matroid.is_sparse_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6221)

        Return if ``self`` is sparse-paving.

        A matroid is sparse-paving if it is paving and its dual is paving.

        OUTPUT: boolean

        ALGORITHM:

        First, check that the matroid is paving. Then, verify that the
        symmetric difference of every pair of distinct `r`-circuits is greater
        than 2.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_sparse_paving()
            True
            sage: M = matroids.catalog.N1()
            sage: M.is_sparse_paving()
            False

        REFERENCES:

        The definition of sparse-paving matroids can be found in [MNWW2011]_.
        The algorithm uses an alternative characterization from [Jer2006]_.

        TESTS::

            sage: M = matroids.Uniform(4, 50)  # fast because we don't check M.dual().is_paving()
            sage: M.is_sparse_paving()
            True
            sage: for M in matroids.AllMatroids(8):  # optional - matroid_database
            ....:    assert M.is_sparse_paving() == (M.is_paving() and M.dual().is_paving())"""
    @overload
    def is_sparse_paving(self) -> Any:
        """Matroid.is_sparse_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6221)

        Return if ``self`` is sparse-paving.

        A matroid is sparse-paving if it is paving and its dual is paving.

        OUTPUT: boolean

        ALGORITHM:

        First, check that the matroid is paving. Then, verify that the
        symmetric difference of every pair of distinct `r`-circuits is greater
        than 2.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_sparse_paving()
            True
            sage: M = matroids.catalog.N1()
            sage: M.is_sparse_paving()
            False

        REFERENCES:

        The definition of sparse-paving matroids can be found in [MNWW2011]_.
        The algorithm uses an alternative characterization from [Jer2006]_.

        TESTS::

            sage: M = matroids.Uniform(4, 50)  # fast because we don't check M.dual().is_paving()
            sage: M.is_sparse_paving()
            True
            sage: for M in matroids.AllMatroids(8):  # optional - matroid_database
            ....:    assert M.is_sparse_paving() == (M.is_paving() and M.dual().is_paving())"""
    @overload
    def is_sparse_paving(self) -> Any:
        """Matroid.is_sparse_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6221)

        Return if ``self`` is sparse-paving.

        A matroid is sparse-paving if it is paving and its dual is paving.

        OUTPUT: boolean

        ALGORITHM:

        First, check that the matroid is paving. Then, verify that the
        symmetric difference of every pair of distinct `r`-circuits is greater
        than 2.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_sparse_paving()
            True
            sage: M = matroids.catalog.N1()
            sage: M.is_sparse_paving()
            False

        REFERENCES:

        The definition of sparse-paving matroids can be found in [MNWW2011]_.
        The algorithm uses an alternative characterization from [Jer2006]_.

        TESTS::

            sage: M = matroids.Uniform(4, 50)  # fast because we don't check M.dual().is_paving()
            sage: M.is_sparse_paving()
            True
            sage: for M in matroids.AllMatroids(8):  # optional - matroid_database
            ....:    assert M.is_sparse_paving() == (M.is_paving() and M.dual().is_paving())"""
    @overload
    def is_sparse_paving(self) -> Any:
        """Matroid.is_sparse_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6221)

        Return if ``self`` is sparse-paving.

        A matroid is sparse-paving if it is paving and its dual is paving.

        OUTPUT: boolean

        ALGORITHM:

        First, check that the matroid is paving. Then, verify that the
        symmetric difference of every pair of distinct `r`-circuits is greater
        than 2.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_sparse_paving()
            True
            sage: M = matroids.catalog.N1()
            sage: M.is_sparse_paving()
            False

        REFERENCES:

        The definition of sparse-paving matroids can be found in [MNWW2011]_.
        The algorithm uses an alternative characterization from [Jer2006]_.

        TESTS::

            sage: M = matroids.Uniform(4, 50)  # fast because we don't check M.dual().is_paving()
            sage: M.is_sparse_paving()
            True
            sage: for M in matroids.AllMatroids(8):  # optional - matroid_database
            ....:    assert M.is_sparse_paving() == (M.is_paving() and M.dual().is_paving())"""
    @overload
    def is_sparse_paving(self) -> Any:
        """Matroid.is_sparse_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6221)

        Return if ``self`` is sparse-paving.

        A matroid is sparse-paving if it is paving and its dual is paving.

        OUTPUT: boolean

        ALGORITHM:

        First, check that the matroid is paving. Then, verify that the
        symmetric difference of every pair of distinct `r`-circuits is greater
        than 2.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_sparse_paving()
            True
            sage: M = matroids.catalog.N1()
            sage: M.is_sparse_paving()
            False

        REFERENCES:

        The definition of sparse-paving matroids can be found in [MNWW2011]_.
        The algorithm uses an alternative characterization from [Jer2006]_.

        TESTS::

            sage: M = matroids.Uniform(4, 50)  # fast because we don't check M.dual().is_paving()
            sage: M.is_sparse_paving()
            True
            sage: for M in matroids.AllMatroids(8):  # optional - matroid_database
            ....:    assert M.is_sparse_paving() == (M.is_paving() and M.dual().is_paving())"""
    def is_subset_k_closed(self, X, intk) -> Any:
        """Matroid.is_subset_k_closed(self, X, int k)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2043)

        Test if ``X`` is a ``k``-closed set of the matroid.

        A set `S` is `k`-*closed* if the closure of any `k` element subsets
        is contained in `S`.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset
        - ``k`` -- positive integer

        OUTPUT: boolean

        .. SEEALSO::

            :meth:`M.k_closure() <sage.matroids.matroid.Matroid.k_closure>`

        EXAMPLES::

            sage: m = matrix([[1,2,5,2], [0,2,1,0]])
            sage: M = Matroid(m)
            sage: M.is_subset_k_closed({1,3}, 2)
            False
            sage: M.is_subset_k_closed({0,1}, 1)
            False
            sage: M.is_subset_k_closed({1,2}, 1)
            True

            sage: m = matrix([[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            ....:            [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2],
            ....:            [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
            ....:            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]])
            sage: M = Matroid(m)
            sage: M.is_subset_k_closed({0,2,3,11}, 3)
            True
            sage: M.is_subset_k_closed({0,2,3,11}, 4)
            False
            sage: M.is_subset_k_closed({0,1}, 4)
            False
            sage: M.is_subset_k_closed({0,1,4}, 4)
            True"""
    @overload
    def is_ternary(self, randomized_tests=...) -> Any:
        """Matroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6571)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        ternary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            False
            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            True"""
    @overload
    def is_ternary(self) -> Any:
        """Matroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6571)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        ternary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            False
            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            True"""
    @overload
    def is_ternary(self) -> Any:
        """Matroid.is_ternary(self, randomized_tests=1)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6571)

        Decide if ``self`` is a ternary matroid.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization

        OUTPUT: boolean

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``False``. This
        test is performed ``randomized_tests`` times. Next, test if a
        ternary matroid local to some basis is isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M.ternary_matroid()
            <sage.matroids.matroid.Matroid.ternary_matroid>`

        EXAMPLES::

            sage: N = matroids.catalog.Fano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            False
            sage: N = matroids.catalog.NonFano()
            sage: N.is_ternary()                                                        # needs sage.graphs
            True"""
    def is_valid(self, certificate=...) -> Any:
        '''Matroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2309)

        Test if the data obey the matroid axioms.

        The default implementation checks the (disproportionately slow) rank
        axioms. If `r` is the rank function of a matroid, we check, for all
        pairs `X, Y` of subsets,

        * `0 \\leq r(X) \\leq |X|`
        * If `X \\subseteq Y` then `r(X) \\leq r(Y)`
        * `r(X\\cup Y) + r(X\\cap Y) \\leq r(X) + r(Y)`

        Certain subclasses may check other axioms instead.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.is_valid()
            True

        The following is the \'Escher matroid\' by Brylawski and Kelly. See
        Example 1.5.5 in [Oxl2011]_ ::

            sage: M = Matroid(circuit_closures={2: [[1, 2, 3], [1, 4, 5]],
            ....: 3: [[1, 2, 3, 4, 5], [1, 2, 3, 6, 7], [1, 4, 5, 6, 7]]})
            sage: M.is_valid()
            False

        TESTS::

            sage: def r(X):
            ....:     return -1
            sage: M = Matroid(groundset=[0,1,2], rank_function=r)
            sage: M.is_valid(certificate=True)
            (False,
             {\'error\': "the rank must be between 0 and the set\'s cardinality",
              \'set\': frozenset()})'''
    @overload
    def isomorphism(self, other) -> Any:
        """Matroid.isomorphism(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3607)

        Return a matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.
        This method returns one isomorphism `f` from ``self`` to ``other``, if
        such an isomorphism exists.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: dictionary or ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: morphism = M1.isomorphism(M2)                                         # needs sage.graphs
            sage: M1.is_isomorphism(M2, morphism)                                       # needs sage.graphs
            True
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.isomorphism(G3)                                                    # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only give isomorphism between matroids.

            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.isomorphism(M2) is not None
            False"""
    @overload
    def isomorphism(self, M2) -> Any:
        """Matroid.isomorphism(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3607)

        Return a matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.
        This method returns one isomorphism `f` from ``self`` to ``other``, if
        such an isomorphism exists.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: dictionary or ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: morphism = M1.isomorphism(M2)                                         # needs sage.graphs
            sage: M1.is_isomorphism(M2, morphism)                                       # needs sage.graphs
            True
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.isomorphism(G3)                                                    # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only give isomorphism between matroids.

            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.isomorphism(M2) is not None
            False"""
    @overload
    def isomorphism(self, G3) -> Any:
        """Matroid.isomorphism(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3607)

        Return a matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.
        This method returns one isomorphism `f` from ``self`` to ``other``, if
        such an isomorphism exists.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: dictionary or ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: morphism = M1.isomorphism(M2)                                         # needs sage.graphs
            sage: M1.is_isomorphism(M2, morphism)                                       # needs sage.graphs
            True
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.isomorphism(G3)                                                    # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only give isomorphism between matroids.

            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.isomorphism(M2) is not None
            False"""
    @overload
    def isomorphism(self, M2) -> Any:
        """Matroid.isomorphism(self, other)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3607)

        Return a matroid isomorphism.

        Two matroids `M` and `N` are *isomorphic* if there is a bijection `f`
        from the groundset of `M` to the groundset of `N` such that a subset
        `X` is independent in `M` if and only if `f(X)` is independent in `N`.
        This method returns one isomorphism `f` from ``self`` to ``other``, if
        such an isomorphism exists.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: dictionary or ``None``

        EXAMPLES::

            sage: M1 = matroids.Wheel(3)
            sage: M2 = matroids.CompleteGraphic(4)                                      # needs sage.graphs
            sage: morphism = M1.isomorphism(M2)                                         # needs sage.graphs
            sage: M1.is_isomorphism(M2, morphism)                                       # needs sage.graphs
            True
            sage: G3 = graphs.CompleteGraph(4)                                          # needs sage.graphs
            sage: M1.isomorphism(G3)                                                    # needs sage.graphs
            Traceback (most recent call last):
            ...
            TypeError: can only give isomorphism between matroids.

            sage: M1 = matroids.catalog.Fano()
            sage: M2 = matroids.catalog.NonFano()
            sage: M1.isomorphism(M2) is not None
            False"""
    def k_closure(self, X, k) -> Any:
        """Matroid.k_closure(self, X, k)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1593)

        Return the ``k``-closure of ``X``.

        A subset `S` of the groundset is `k`-*closed* if the closure of
        any subset `T` of `S` satisfying `|T| \\leq k` is contained in `S`.
        The `k`-*closure* of a set `X` is the smallest `k`-closed set
        containing `X`.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset
        - ``k`` -- positive integer

        EXAMPLES::

            sage: m = matrix([[1,2,5,2], [0,2,1,0]])
            sage: M = Matroid(m)
            sage: sorted(M.k_closure({1,3}, 2))
            [0, 1, 2, 3]
            sage: sorted(M.k_closure({0,1}, 1))
            [0, 1, 3]
            sage: sorted(M.k_closure({1,2}, 1))
            [1, 2]

            sage: m = matrix([[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            ....:            [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2],
            ....:            [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
            ....:            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]])
            sage: M = Matroid(m)
            sage: sorted(M.k_closure({0,2,3,11}, 3))
            [0, 2, 3, 11]
            sage: sorted(M.k_closure({0,2,3,11}, 4))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            sage: sorted(M.k_closure({0,1}, 4))
            [0, 1, 4]"""
    @overload
    def lattice_of_flats(self) -> Any:
        """Matroid.lattice_of_flats(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3048)

        Return the lattice of flats of the matroid.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.lattice_of_flats()                                                  # needs sage.graphs
            Finite lattice containing 16 elements"""
    @overload
    def lattice_of_flats(self) -> Any:
        """Matroid.lattice_of_flats(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3048)

        Return the lattice of flats of the matroid.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.lattice_of_flats()                                                  # needs sage.graphs
            Finite lattice containing 16 elements"""
    def linear_subclasses(self, line_length=..., subsets=...) -> Any:
        """Matroid.linear_subclasses(self, line_length=None, subsets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4726)

        Return an iterable set of linear subclasses of the matroid.

        A *linear subclass* is a set of hyperplanes (i.e. closed sets of rank
        `r(M) - 1`) with the following property:

        - If `H_1` and `H_2` are members, and `r(H_1 \\cap H_2) = r(M) - 2`,
          then any hyperplane `H_3` containing `H_1 \\cap H_2` is a member too.

        A linear subclass is the set of hyperplanes of a
        :meth:`modular cut <sage.matroids.matroid.Matroid.modular_cut>` and
        uniquely determines the modular cut. Hence the collection of linear
        subclasses is in 1-to-1 correspondence with the collection of
        single-element extensions of a matroid. See [Oxl2011]_, section 7.2.

        INPUT:

        - ``line_length`` -- (default: ``None``) a natural number. If given,
          restricts the output to modular cuts that generate an extension by
          `e` that does not contain a minor `N` isomorphic to `U_{2, k}`,
          where ``k > line_length``, and such that `e \\in E(N)`.
        - ``subsets`` -- (default: ``None``) a collection of subsets of the
          groundset. If given, restricts the output to linear subclasses such
          that each hyperplane contains an element of ``subsets``.

        OUTPUT: an iterable collection of linear subclasses

        .. NOTE::

            The ``line_length`` argument only checks for lines using the new
            element of the corresponding extension. It is still possible that
            a long line exists by contracting the new element!

        .. SEEALSO::

            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`,
            :meth:`M.modular_cut() <sage.matroids.matroid.Matroid.modular_cut>`,
            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :mod:`sage.matroids.extension <sage.matroids.extension>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: len(list(M.linear_subclasses()))
            16
            sage: len(list(M.linear_subclasses(line_length=3)))
            8
            sage: len(list(M.linear_subclasses(subsets=[{'a', 'b'}])))
            5

        The following matroid has an extension by element `e` such that
        contracting `e` creates a 6-point line, but no 6-point line minor uses
        `e`. Consequently, this method returns the modular cut, but the
        :meth:`M.extensions() <sage.matroids.matroid.Matroid.extensions>`
        method doesn't return the corresponding extension::

            sage: M = Matroid(circuit_closures={2: ['abc', 'def'],
            ....:                               3: ['abcdef']})
            sage: len(list(M.extensions('g', line_length=5)))
            43
            sage: len(list(M.linear_subclasses(line_length=5)))
            44"""
    def link(self, S, T) -> Any:
        """Matroid.link(self, S, T)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 5207)

        Given disjoint subsets `S` and `T`, return a connector `I` and a separation `X`,
        which are optimal dual solutions in Tutte's Linking Theorem:

        .. MATH::

            \\max \\{ r_N(S) + r_N(T) - r(N) \\mid N = M/I\\setminus J, E(N) = S\\cup T\\}=\\\\\n            \\min \\{ r_M(X) + r_M(Y) - r_M(E) \\mid X \\subseteq S, Y \\subseteq T,
            E = X\\cup Y, X\\cap Y = \\emptyset \\}.

        Here `M` denotes this matroid.

        INPUT:

        - ``S`` -- a subset (or any iterable) of the groundset
        - ``T`` -- a subset (or any iterable) of the groundset disjoint
          from ``S``

        OUTPUT: a tuple ``(I, X)`` containing a frozenset ``I`` and a frozenset
        ``X``

        ALGORITHM:

        Compute a maximum-cardinality common independent set `I` of
        of `M / S \\setminus T` and `M \\setminus S / T`.

        EXAMPLES::

            sage: M = matroids.catalog.BetsyRoss()
            sage: S = set('ab')
            sage: T = set('cd')
            sage: I, X = M.link(S, T)
            sage: M.connectivity(X)
            2
            sage: J = M.groundset()-(S|T|I)
            sage: N = (M/I).delete(J)
            sage: N.connectivity(S)
            2"""
    def loops(self) -> Any:
        """Matroid.loops(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1918)

        Return the set of loops of the matroid.

        A *loop* is an element `u` of the groundset such that the
        one-element set `\\{ u \\}` is dependent.

        OUTPUT: a set of elements

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.loops()
            frozenset()
            sage: (M / ['a', 'b']).loops()
            frozenset({'f'})"""
    def matroid_polytope(self) -> Any:
        """Matroid.matroid_polytope(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3430)

        Return the matroid polytope of ``self``.

        This is defined as the convex hull of the vertices

        .. MATH::

            e_B = \\sum_{i \\in B} e_i

        over all bases `B` of the matroid. Here `e_i` are the standard
        basis vectors of `\\RR^n`. An arbitrary labelling of the
        groundset by `\\{0,\\ldots,n-1\\}` is chosen.

        .. SEEALSO::

            :meth:`independence_matroid_polytope`

        EXAMPLES::

            sage: M = matroids.Whirl(4)
            sage: P = M.matroid_polytope(); P                                           # needs sage.geometry.polyhedron sage.rings.finite_rings
            A 7-dimensional polyhedron in ZZ^8 defined as the convex hull
            of 46 vertices

            sage: M = matroids.catalog.NonFano()
            sage: M.matroid_polytope()                                                  # needs sage.geometry.polyhedron sage.rings.finite_rings
            A 6-dimensional polyhedron in ZZ^7 defined as the convex hull
            of 29 vertices

        REFERENCES:

        [DLHK2007]_"""
    def max_coindependent(self, X) -> Any:
        """Matroid.max_coindependent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1769)

        Compute a maximal coindependent subset of ``X``.

        A set is *coindependent* if it is independent in the dual matroid.
        A set is coindependent if and only if the complement is *spanning*
        (i.e. contains a basis of the matroid).

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: a subset of ``X``

        .. SEEALSO::

            :meth:`M.dual() <sage.matroids.matroid.Matroid.dual>`,
            :meth:`M.max_independent() <sage.matroids.matroid.Matroid.max_independent>`

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: X = M.max_coindependent(['a', 'c', 'd', 'e', 'f'])
            sage: sorted(X)  # random
            ['a', 'c', 'd', 'f']
            sage: M.is_coindependent(X)
            True
            sage: all(M.is_codependent(X.union([y])) for y in M.groundset() if y not in X)
            True
            sage: M.max_coindependent(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    def max_independent(self, X) -> Any:
        """Matroid.max_independent(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1469)

        Compute a maximal independent subset of ``X``.

        INPUT:

        - ``X`` -- a subset (or any iterable) of the groundset

        OUTPUT: subset of ``X``

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: X = M.max_independent(['a', 'c', 'd', 'e', 'f'])
            sage: M.is_independent(X)
            True
            sage: all(M.is_dependent(X.union([y])) for y in M.groundset() if y not in X)
            True
            sage: M.max_independent(['x'])
            Traceback (most recent call last):
            ...
            ValueError: ['x'] is not a subset of the groundset"""
    @overload
    def max_weight_coindependent(self, X=..., weights=...) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self, weights=...) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self, weights=...) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self, weights=...) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_coindependent(self, X=..., weights=...) -> Any:
        """Matroid.max_weight_coindependent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6965)

        Return a maximum-weight coindependent set contained in ``X``.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort
        the elements of ``X`` by decreasing weight, and otherwise use the
        ordering in which ``X``  lists its elements. Then greedily select
        elements if they are coindependent of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_coindependent()
            sage: M.is_cobasis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {'b', 'c', 'f', 'g'}
            sage: wt = {'a': 1, 'b': -10, 'c': 2, 'd': 1/2, 'e': 1, 'f': 2, 'g': 2}
            sage: setprint(M.max_weight_coindependent(weights=wt))
            Traceback (most recent call last):
            ...
            ValueError: nonnegative weights were expected.

            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_coindependent(weights=wt))
            {2, 3, 4, 5, 6, 7}
            sage: setprint(M.max_weight_coindependent())
            {0, 1, 2, 3, 4, 5}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_independent(self, X=..., weights=...) -> Any:
        """Matroid.max_weight_independent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6880)

        Return a maximum-weight independent set contained in a subset.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_independent()
            sage: M.is_basis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1,
            ....:       'f': 2, 'g': 2}
            sage: setprint(M.max_weight_independent(weights=wt))
            {'b', 'f', 'g'}
            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_independent(weights=wt))
            {6, 7}
            sage: setprint(M.max_weight_independent())
            {0, 1}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_independent(self) -> Any:
        """Matroid.max_weight_independent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6880)

        Return a maximum-weight independent set contained in a subset.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_independent()
            sage: M.is_basis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1,
            ....:       'f': 2, 'g': 2}
            sage: setprint(M.max_weight_independent(weights=wt))
            {'b', 'f', 'g'}
            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_independent(weights=wt))
            {6, 7}
            sage: setprint(M.max_weight_independent())
            {0, 1}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_independent(self, weights=...) -> Any:
        """Matroid.max_weight_independent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6880)

        Return a maximum-weight independent set contained in a subset.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_independent()
            sage: M.is_basis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1,
            ....:       'f': 2, 'g': 2}
            sage: setprint(M.max_weight_independent(weights=wt))
            {'b', 'f', 'g'}
            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_independent(weights=wt))
            {6, 7}
            sage: setprint(M.max_weight_independent())
            {0, 1}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_independent(self, weights=...) -> Any:
        """Matroid.max_weight_independent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6880)

        Return a maximum-weight independent set contained in a subset.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_independent()
            sage: M.is_basis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1,
            ....:       'f': 2, 'g': 2}
            sage: setprint(M.max_weight_independent(weights=wt))
            {'b', 'f', 'g'}
            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_independent(weights=wt))
            {6, 7}
            sage: setprint(M.max_weight_independent())
            {0, 1}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def max_weight_independent(self) -> Any:
        """Matroid.max_weight_independent(self, X=None, weights=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6880)

        Return a maximum-weight independent set contained in a subset.

        The *weight* of a subset ``S`` is ``sum(weights(e) for e in S)``.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset
        - ``weights`` -- dictionary or function mapping the elements of
          ``X`` to nonnegative weights

        OUTPUT: a subset of ``X``

        ALGORITHM:

        The greedy algorithm. If a weight function is given, then sort the elements
        of ``X`` by decreasing weight, and otherwise use the ordering in which ``X``
        lists its elements. Then greedily select elements if they are independent
        of all that was selected before.

        EXAMPLES::

            sage: from sage.matroids.advanced import setprint
            sage: M = matroids.catalog.Fano()
            sage: X = M.max_weight_independent()
            sage: M.is_basis(X)
            True

            sage: wt = {'a': 1, 'b': 2, 'c': 2, 'd': 1/2, 'e': 1,
            ....:       'f': 2, 'g': 2}
            sage: setprint(M.max_weight_independent(weights=wt))
            {'b', 'f', 'g'}
            sage: def wt(x):
            ....:   return x
            ....:
            sage: M = matroids.Uniform(2, 8)
            sage: setprint(M.max_weight_independent(weights=wt))
            {6, 7}
            sage: setprint(M.max_weight_independent())
            {0, 1}
            sage: M.max_weight_coindependent(X=[], weights={})
            frozenset()"""
    @overload
    def minor(self, contractions=..., deletions=...) -> Any:
        """Matroid.minor(self, contractions=None, deletions=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4015)

        Return the minor of ``self`` obtained by contracting, respectively
        deleting, the element(s) of ``contractions`` and ``deletions``.

        A *minor* of a matroid is a matroid obtained by repeatedly removing
        elements in one of two ways: either
        :meth:`contract <sage.matroids.matroid.Matroid.contract>` or
        :meth:`delete <sage.matroids.matroid.Matroid.delete>` them. It can be
        shown that the final matroid does not depend on the order in which
        elements are removed.

        INPUT:

        - ``contractions`` -- (default: ``None``) an element or set of
          elements to be contracted
        - ``deletions`` -- (default: ``None``) an element or set of elements
          to be deleted

        OUTPUT: matroid

        .. NOTE::

            The output is either of the same type as ``self``, or an instance
            of
            :class:`MinorMatroid <sage.matroids.minor_matroid.MinorMatroid>`.

        .. SEEALSO::

            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES:

        ::

            sage: M = matroids.Wheel(4)
            sage: N = M.minor(contractions=[7], deletions=[0])
            sage: N.is_isomorphic(matroids.Wheel(3))
            True

        The sets of contractions and deletions need not be independent,
        respectively coindependent::

            sage: M = matroids.catalog.Fano()
            sage: M.rank('abf')
            2
            sage: M.minor(contractions='abf')
            Binary matroid of rank 1 on 4 elements, type (1, 0)

        However, they need to be subsets of the groundset, and disjoint::

            sage: M = matroids.catalog.Vamos()
            sage: N = M.minor('abc', 'defg')
            sage: N
            M / {'a', 'b', 'c'} \\ {'d', 'e', 'f', 'g'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            ...
            sage: N.groundset()
            frozenset({'h'})

            sage: N = M.minor('defgh', 'abc')
            sage: N  # random
            M / {'d', 'e', 'f', 'g'} \\ {'a', 'b', 'c', 'h'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
            sage: N.groundset()
            frozenset()

            sage: M.minor([1, 2, 3], 'efg')
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('efg', [1, 2, 3])
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('ade', 'efg')
            Traceback (most recent call last):
            ...
            ValueError: contraction and deletion sets are not disjoint.

        .. WARNING::

            There can be ambiguity if elements of the groundset are themselves
            iterable, and their elements are in the groundset. The main
            example of this is when an element is a string. See the
            documentation of the methods
            :meth:`contract() <sage.matroids.matroid.Matroid.contract>` and
            :meth:`delete() <sage.matroids.matroid.Matroid.delete>` for an
            example of this."""
    @overload
    def minor(self, contractions=..., deletions=...) -> Any:
        """Matroid.minor(self, contractions=None, deletions=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4015)

        Return the minor of ``self`` obtained by contracting, respectively
        deleting, the element(s) of ``contractions`` and ``deletions``.

        A *minor* of a matroid is a matroid obtained by repeatedly removing
        elements in one of two ways: either
        :meth:`contract <sage.matroids.matroid.Matroid.contract>` or
        :meth:`delete <sage.matroids.matroid.Matroid.delete>` them. It can be
        shown that the final matroid does not depend on the order in which
        elements are removed.

        INPUT:

        - ``contractions`` -- (default: ``None``) an element or set of
          elements to be contracted
        - ``deletions`` -- (default: ``None``) an element or set of elements
          to be deleted

        OUTPUT: matroid

        .. NOTE::

            The output is either of the same type as ``self``, or an instance
            of
            :class:`MinorMatroid <sage.matroids.minor_matroid.MinorMatroid>`.

        .. SEEALSO::

            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES:

        ::

            sage: M = matroids.Wheel(4)
            sage: N = M.minor(contractions=[7], deletions=[0])
            sage: N.is_isomorphic(matroids.Wheel(3))
            True

        The sets of contractions and deletions need not be independent,
        respectively coindependent::

            sage: M = matroids.catalog.Fano()
            sage: M.rank('abf')
            2
            sage: M.minor(contractions='abf')
            Binary matroid of rank 1 on 4 elements, type (1, 0)

        However, they need to be subsets of the groundset, and disjoint::

            sage: M = matroids.catalog.Vamos()
            sage: N = M.minor('abc', 'defg')
            sage: N
            M / {'a', 'b', 'c'} \\ {'d', 'e', 'f', 'g'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            ...
            sage: N.groundset()
            frozenset({'h'})

            sage: N = M.minor('defgh', 'abc')
            sage: N  # random
            M / {'d', 'e', 'f', 'g'} \\ {'a', 'b', 'c', 'h'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
            sage: N.groundset()
            frozenset()

            sage: M.minor([1, 2, 3], 'efg')
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('efg', [1, 2, 3])
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('ade', 'efg')
            Traceback (most recent call last):
            ...
            ValueError: contraction and deletion sets are not disjoint.

        .. WARNING::

            There can be ambiguity if elements of the groundset are themselves
            iterable, and their elements are in the groundset. The main
            example of this is when an element is a string. See the
            documentation of the methods
            :meth:`contract() <sage.matroids.matroid.Matroid.contract>` and
            :meth:`delete() <sage.matroids.matroid.Matroid.delete>` for an
            example of this."""
    @overload
    def minor(self, contractions=...) -> Any:
        """Matroid.minor(self, contractions=None, deletions=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4015)

        Return the minor of ``self`` obtained by contracting, respectively
        deleting, the element(s) of ``contractions`` and ``deletions``.

        A *minor* of a matroid is a matroid obtained by repeatedly removing
        elements in one of two ways: either
        :meth:`contract <sage.matroids.matroid.Matroid.contract>` or
        :meth:`delete <sage.matroids.matroid.Matroid.delete>` them. It can be
        shown that the final matroid does not depend on the order in which
        elements are removed.

        INPUT:

        - ``contractions`` -- (default: ``None``) an element or set of
          elements to be contracted
        - ``deletions`` -- (default: ``None``) an element or set of elements
          to be deleted

        OUTPUT: matroid

        .. NOTE::

            The output is either of the same type as ``self``, or an instance
            of
            :class:`MinorMatroid <sage.matroids.minor_matroid.MinorMatroid>`.

        .. SEEALSO::

            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`,
            :meth:`M.delete() <sage.matroids.matroid.Matroid.delete>`

        EXAMPLES:

        ::

            sage: M = matroids.Wheel(4)
            sage: N = M.minor(contractions=[7], deletions=[0])
            sage: N.is_isomorphic(matroids.Wheel(3))
            True

        The sets of contractions and deletions need not be independent,
        respectively coindependent::

            sage: M = matroids.catalog.Fano()
            sage: M.rank('abf')
            2
            sage: M.minor(contractions='abf')
            Binary matroid of rank 1 on 4 elements, type (1, 0)

        However, they need to be subsets of the groundset, and disjoint::

            sage: M = matroids.catalog.Vamos()
            sage: N = M.minor('abc', 'defg')
            sage: N
            M / {'a', 'b', 'c'} \\ {'d', 'e', 'f', 'g'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            ...
            sage: N.groundset()
            frozenset({'h'})

            sage: N = M.minor('defgh', 'abc')
            sage: N  # random
            M / {'d', 'e', 'f', 'g'} \\ {'a', 'b', 'c', 'h'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
            sage: N.groundset()
            frozenset()

            sage: M.minor([1, 2, 3], 'efg')
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('efg', [1, 2, 3])
            Traceback (most recent call last):
            ...
            ValueError: [1, 2, 3] is not a subset of the groundset
            sage: M.minor('ade', 'efg')
            Traceback (most recent call last):
            ...
            ValueError: contraction and deletion sets are not disjoint.

        .. WARNING::

            There can be ambiguity if elements of the groundset are themselves
            iterable, and their elements are in the groundset. The main
            example of this is when an element is a string. See the
            documentation of the methods
            :meth:`contract() <sage.matroids.matroid.Matroid.contract>` and
            :meth:`delete() <sage.matroids.matroid.Matroid.delete>` for an
            example of this."""
    def modular_cut(self, subsets) -> Any:
        """Matroid.modular_cut(self, subsets)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4638)

        Compute the modular cut generated by ``subsets``.

        A *modular cut* is a collection `C` of flats such that

        - If `F \\in C` and `F'` is a flat containing `F`, then `F' \\in C`
        - If `F_1, F_2 \\in C` form a modular pair of flats, then
          `F_1\\cap F_2 \\in C`.

        A *flat* is a closed set, a *modular pair* is a pair `F_1, F_2` of
        flats with `r(F_1) + r(F_2) = r(F_1\\cup F_2) + r(F_1\\cap F_2)`,
        where `r` is the rank function of the matroid.

        The modular cut *generated by* ``subsets`` is the smallest modular cut
        `C` for which closure`(S) \\in C` for all `S` in ``subsets``.

        There is a one-to-one correspondence between the modular cuts of a
        matroid and the single-element extensions of the matroid. See [Oxl2011]_
        Section 7.2 for more information.

        .. NOTE::

            Sage uses linear subclasses, rather than modular cuts, internally
            for matroid extension. A linear subclass is the set of hyperplanes
            (flats of rank `r(M) - 1`) of a modular cut. It determines the
            modular cut uniquely (see [Oxl2011]_ Section 7.2).

        INPUT:

        - ``subsets`` -- a collection of subsets of the groundset

        OUTPUT: a collection of subsets

        .. SEEALSO::

            :meth:`M.flats() <sage.matroids.matroid.Matroid.flats>`,
            :meth:`M.linear_subclasses() <sage.matroids.matroid.Matroid.linear_subclasses>`,
            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`

        EXAMPLES:

        Any extension of the Vamos matroid where the new point is placed on
        the lines through elements `\\{a, b\\}` and through `\\{c, d\\}` is an
        extension by a loop::

            sage: M = matroids.catalog.Vamos()
            sage: frozenset() in M.modular_cut(['ab', 'cd'])
            True

        In any extension of the matroid `S_8 \\setminus h`, a point on the
        lines through `\\{c, g\\}` and `\\{a, e\\}` also is on the line through
        `\\{b, f\\}`::

            sage: M = matroids.catalog.S8()
            sage: N = M.delete('h')
            sage: frozenset('bf') in N.modular_cut(['cg', 'ae'])
            True

        The modular cut of the full groundset is equal to just the groundset::

            sage: M = matroids.catalog.Fano()
            sage: M.modular_cut([M.groundset()]).difference(
            ....:                               [frozenset(M.groundset())])
            set()"""
    @overload
    def no_broken_circuits_sets(self, ordering=...) -> SetSystem:
        """Matroid.no_broken_circuits_sets(self, ordering=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3209)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]]))
            sage: SimplicialComplex(M.no_broken_circuits_sets())                        # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5,4,3,2,1]))             # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1,2,3], [1,4,5], [2,3,4,5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5,4,3,2,1]))             # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        ALGORITHM:

        The following algorithm is adapted from page 7 of [BDPR2011]_.

        .. NOTE::

            Sage uses the convention that a broken circuit is found by
            removing a minimal element from a circuit, while [BDPR2011]_.
            use the convention that removal of the *maximal* element of
            circuit yields a broken circuit. This implementation reverses
            the provided order so that it returns n.b.c. sets under the
            minimal-removal convention, while the implementation is not
            modified from the published algorithm."""
    @overload
    def no_broken_circuits_sets(self) -> Any:
        """Matroid.no_broken_circuits_sets(self, ordering=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3209)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]]))
            sage: SimplicialComplex(M.no_broken_circuits_sets())                        # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5,4,3,2,1]))             # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1,2,3], [1,4,5], [2,3,4,5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5,4,3,2,1]))             # needs sage.graphs
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        ALGORITHM:

        The following algorithm is adapted from page 7 of [BDPR2011]_.

        .. NOTE::

            Sage uses the convention that a broken circuit is found by
            removing a minimal element from a circuit, while [BDPR2011]_.
            use the convention that removal of the *maximal* element of
            circuit yields a broken circuit. This implementation reverses
            the provided order so that it returns n.b.c. sets under the
            minimal-removal convention, while the implementation is not
            modified from the published algorithm."""
    @overload
    def no_broken_circuits_sets_iterator(self, ordering=...) -> Any:
        """Matroid.no_broken_circuits_sets_iterator(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3298)

        Return an iterator over no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator()))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator([5,4,3,2,1])))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1,2,3], [1,4,5], [2,3,4,5]])
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator([5,4,3,2,1])))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        For a matroid with loops all sets contain the broken circuit
        `\\emptyset`, and thus we shouldn't get any set as output::

            sage: M = Matroid(groundset=[1,2,3], circuits=[[3]])
            sage: list(M.no_broken_circuits_sets_iterator())
            []"""
    @overload
    def no_broken_circuits_sets_iterator(self) -> Any:
        """Matroid.no_broken_circuits_sets_iterator(self, ordering=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3298)

        Return an iterator over no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset

        EXAMPLES::

            sage: M = Matroid(circuits=[[1,2,3], [3,4,5], [1,2,4,5]])
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator()))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator([5,4,3,2,1])))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1,2,3], [1,4,5], [2,3,4,5]])
            sage: SimplicialComplex(list(M.no_broken_circuits_sets_iterator([5,4,3,2,1])))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        For a matroid with loops all sets contain the broken circuit
        `\\emptyset`, and thus we shouldn't get any set as output::

            sage: M = Matroid(groundset=[1,2,3], circuits=[[3]])
            sage: list(M.no_broken_circuits_sets_iterator())
            []"""
    @overload
    def nonbases(self) -> SetSystem:
        """Matroid.nonbases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2642)

        Return the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases()]
            [['a', 'b', 'c']]

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``"""
    @overload
    def nonbases(self) -> Any:
        """Matroid.nonbases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2642)

        Return the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases()]
            [['a', 'b', 'c']]

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``"""
    @overload
    def nonbases(self) -> Any:
        """Matroid.nonbases(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2642)

        Return the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases()]
            [['a', 'b', 'c']]

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``"""
    @overload
    def nonbases_iterator(self) -> Any:
        """Matroid.nonbases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2669)

        Return an iterator over the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``.

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases_iterator())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases_iterator()]
            [['a', 'b', 'c']]"""
    @overload
    def nonbases_iterator(self) -> Any:
        """Matroid.nonbases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2669)

        Return an iterator over the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``.

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases_iterator())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases_iterator()]
            [['a', 'b', 'c']]"""
    @overload
    def nonbases_iterator(self) -> Any:
        """Matroid.nonbases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2669)

        Return an iterator over the nonbases of the matroid.

        A *nonbasis* is a set with cardinality ``self.full_rank()`` that is
        not a basis.

        .. SEEALSO::

            :meth:`M.basis() <sage.matroids.matroid.Matroid.basis>`

        ALGORITHM:

        Test all subsets of the groundset of cardinality ``self.full_rank()``.

        EXAMPLES::

            sage: M = matroids.Uniform(2, 4)
            sage: list(M.nonbases_iterator())
            []
            sage: [sorted(X) for X in matroids.catalog.P6().nonbases_iterator()]
            [['a', 'b', 'c']]"""
    @overload
    def noncospanning_cocircuits(self) -> SetSystem:
        """Matroid.noncospanning_cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2553)

        Return the noncospanning cocircuits of the matroid.

        A *noncospanning cocircuit* is a cocircuit whose corank is strictly
        smaller than the corank of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.corank() <sage.matroids.matroid.Matroid.corank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: sorted([sorted(C) for C in M.noncospanning_cocircuits()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def noncospanning_cocircuits(self) -> Any:
        """Matroid.noncospanning_cocircuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2553)

        Return the noncospanning cocircuits of the matroid.

        A *noncospanning cocircuit* is a cocircuit whose corank is strictly
        smaller than the corank of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.cocircuit() <sage.matroids.matroid.Matroid.cocircuit>`,
            :meth:`M.corank() <sage.matroids.matroid.Matroid.corank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().dual()
            sage: sorted([sorted(C) for C in M.noncospanning_cocircuits()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def nonspanning_circuit_closures(self) -> dict:
        """Matroid.nonspanning_circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2611)

        Return the closures of nonspanning circuits of the matroid.

        A *nonspanning circuit closure* is a closed set containing a
        nonspanning circuit.

        OUTPUT: a dictionary containing the nonspanning circuit closures of the
        matroid, indexed by their ranks

        .. SEEALSO::

            :meth:`M.nonspanning_circuits() <sage.matroids.matroid.Matroid.nonspanning_circuits>`,
            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: CC = M.nonspanning_circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            Traceback (most recent call last):
            ...
            KeyError: 3"""
    @overload
    def nonspanning_circuit_closures(self) -> Any:
        """Matroid.nonspanning_circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2611)

        Return the closures of nonspanning circuits of the matroid.

        A *nonspanning circuit closure* is a closed set containing a
        nonspanning circuit.

        OUTPUT: a dictionary containing the nonspanning circuit closures of the
        matroid, indexed by their ranks

        .. SEEALSO::

            :meth:`M.nonspanning_circuits() <sage.matroids.matroid.Matroid.nonspanning_circuits>`,
            :meth:`M.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: CC = M.nonspanning_circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            Traceback (most recent call last):
            ...
            KeyError: 3"""
    @overload
    def nonspanning_circuits(self) -> SetSystem:
        """Matroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2450)

        Return the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.nonspanning_circuits()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def nonspanning_circuits(self) -> Any:
        """Matroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2450)

        Return the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        OUTPUT: :class:`SetSystem`

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.nonspanning_circuits()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def nonspanning_circuits_iterator(self) -> Any:
        """Matroid.nonspanning_circuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2478)

        Return an iterator over the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.nonspanning_circuits_iterator()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def nonspanning_circuits_iterator(self) -> Any:
        """Matroid.nonspanning_circuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 2478)

        Return an iterator over the nonspanning circuits of the matroid.

        A *nonspanning circuit* is a circuit whose rank is strictly smaller
        than the rank of the matroid.

        .. SEEALSO::

            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.rank() <sage.matroids.matroid.Matroid.rank>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: sorted([sorted(C) for C in M.nonspanning_circuits_iterator()])
            [['a', 'b', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'],
            ['b', 'c', 'd'], ['b', 'e', 'g'], ['c', 'f', 'g'],
            ['d', 'e', 'f']]"""
    @overload
    def orlik_solomon_algebra(self, R, ordering=..., **kwargs) -> Any:
        """Matroid.orlik_solomon_algebra(self, R, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3368)

        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ordering`` -- (optional) an ordering of the groundset
        - ``invariant`` -- (optional) either a semigroup ``G`` whose
          ``__call__`` acts on the groundset, or pair ``(G, action)`` where
          ``G`` is a semigroup and ``action`` is a function ``action(g,e)``
          which takes a pair of a group element and a groundset element and
          returns the groundset element which is the result of ``e`` acted upon
          by ``g``

        .. SEEALSO::

            :class:`~sage.algebras.orlik_solomon.OrlikSolomonAlgebra`

        EXAMPLES::

            sage: M = matroids.Uniform(3, 4)
            sage: OS = M.orlik_solomon_algebra(QQ)
            sage: OS
            Orlik-Solomon algebra of U(3, 4): Matroid of rank 3 on 4 elements
             with circuit-closures
             {3: {{0, 1, 2, 3}}}

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OSG = M.orlik_solomon_algebra(QQ, invariant=G)                        # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g,x: g(x+1)-1
            sage: OSG1 = M.orlik_solomon_algebra(QQ, invariant=(G,action))
            sage: OSG2 = M.orlik_solomon_algebra(QQ, invariant=(action,G))
            sage: OSG1 is OSG2
            True"""
    @overload
    def orlik_solomon_algebra(self, QQ) -> Any:
        """Matroid.orlik_solomon_algebra(self, R, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3368)

        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ordering`` -- (optional) an ordering of the groundset
        - ``invariant`` -- (optional) either a semigroup ``G`` whose
          ``__call__`` acts on the groundset, or pair ``(G, action)`` where
          ``G`` is a semigroup and ``action`` is a function ``action(g,e)``
          which takes a pair of a group element and a groundset element and
          returns the groundset element which is the result of ``e`` acted upon
          by ``g``

        .. SEEALSO::

            :class:`~sage.algebras.orlik_solomon.OrlikSolomonAlgebra`

        EXAMPLES::

            sage: M = matroids.Uniform(3, 4)
            sage: OS = M.orlik_solomon_algebra(QQ)
            sage: OS
            Orlik-Solomon algebra of U(3, 4): Matroid of rank 3 on 4 elements
             with circuit-closures
             {3: {{0, 1, 2, 3}}}

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OSG = M.orlik_solomon_algebra(QQ, invariant=G)                        # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g,x: g(x+1)-1
            sage: OSG1 = M.orlik_solomon_algebra(QQ, invariant=(G,action))
            sage: OSG2 = M.orlik_solomon_algebra(QQ, invariant=(action,G))
            sage: OSG1 is OSG2
            True"""
    @overload
    def orlik_solomon_algebra(self, QQ, invariant=...) -> Any:
        """Matroid.orlik_solomon_algebra(self, R, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3368)

        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ordering`` -- (optional) an ordering of the groundset
        - ``invariant`` -- (optional) either a semigroup ``G`` whose
          ``__call__`` acts on the groundset, or pair ``(G, action)`` where
          ``G`` is a semigroup and ``action`` is a function ``action(g,e)``
          which takes a pair of a group element and a groundset element and
          returns the groundset element which is the result of ``e`` acted upon
          by ``g``

        .. SEEALSO::

            :class:`~sage.algebras.orlik_solomon.OrlikSolomonAlgebra`

        EXAMPLES::

            sage: M = matroids.Uniform(3, 4)
            sage: OS = M.orlik_solomon_algebra(QQ)
            sage: OS
            Orlik-Solomon algebra of U(3, 4): Matroid of rank 3 on 4 elements
             with circuit-closures
             {3: {{0, 1, 2, 3}}}

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OSG = M.orlik_solomon_algebra(QQ, invariant=G)                        # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g,x: g(x+1)-1
            sage: OSG1 = M.orlik_solomon_algebra(QQ, invariant=(G,action))
            sage: OSG2 = M.orlik_solomon_algebra(QQ, invariant=(action,G))
            sage: OSG1 is OSG2
            True"""
    @overload
    def orlik_solomon_algebra(self, QQ, invariant=...) -> Any:
        """Matroid.orlik_solomon_algebra(self, R, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3368)

        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ordering`` -- (optional) an ordering of the groundset
        - ``invariant`` -- (optional) either a semigroup ``G`` whose
          ``__call__`` acts on the groundset, or pair ``(G, action)`` where
          ``G`` is a semigroup and ``action`` is a function ``action(g,e)``
          which takes a pair of a group element and a groundset element and
          returns the groundset element which is the result of ``e`` acted upon
          by ``g``

        .. SEEALSO::

            :class:`~sage.algebras.orlik_solomon.OrlikSolomonAlgebra`

        EXAMPLES::

            sage: M = matroids.Uniform(3, 4)
            sage: OS = M.orlik_solomon_algebra(QQ)
            sage: OS
            Orlik-Solomon algebra of U(3, 4): Matroid of rank 3 on 4 elements
             with circuit-closures
             {3: {{0, 1, 2, 3}}}

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OSG = M.orlik_solomon_algebra(QQ, invariant=G)                        # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g,x: g(x+1)-1
            sage: OSG1 = M.orlik_solomon_algebra(QQ, invariant=(G,action))
            sage: OSG2 = M.orlik_solomon_algebra(QQ, invariant=(action,G))
            sage: OSG1 is OSG2
            True"""
    @overload
    def orlik_solomon_algebra(self, QQ, invariant=...) -> Any:
        """Matroid.orlik_solomon_algebra(self, R, ordering=None, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3368)

        Return the Orlik-Solomon algebra of ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ordering`` -- (optional) an ordering of the groundset
        - ``invariant`` -- (optional) either a semigroup ``G`` whose
          ``__call__`` acts on the groundset, or pair ``(G, action)`` where
          ``G`` is a semigroup and ``action`` is a function ``action(g,e)``
          which takes a pair of a group element and a groundset element and
          returns the groundset element which is the result of ``e`` acted upon
          by ``g``

        .. SEEALSO::

            :class:`~sage.algebras.orlik_solomon.OrlikSolomonAlgebra`

        EXAMPLES::

            sage: M = matroids.Uniform(3, 4)
            sage: OS = M.orlik_solomon_algebra(QQ)
            sage: OS
            Orlik-Solomon algebra of U(3, 4): Matroid of rank 3 on 4 elements
             with circuit-closures
             {3: {{0, 1, 2, 3}}}

            sage: G = SymmetricGroup(3);                                                # needs sage.groups
            sage: OSG = M.orlik_solomon_algebra(QQ, invariant=G)                        # needs sage.groups

            sage: # needs sage.groups
            sage: G = SymmetricGroup(4)
            sage: action = lambda g,x: g(x+1)-1
            sage: OSG1 = M.orlik_solomon_algebra(QQ, invariant=(G,action))
            sage: OSG2 = M.orlik_solomon_algebra(QQ, invariant=(action,G))
            sage: OSG1 is OSG2
            True"""
    @overload
    def partition(self) -> Any:
        """Matroid.partition(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7743)

        Return a minimum number of disjoint independent sets that covers the
        groundset.

        OUTPUT: list of disjoint independent sets that covers the groundset

        EXAMPLES::

            sage: M = matroids.catalog.Block_9_4()
            sage: P = M.partition()
            sage: all(map(M.is_independent,P))
            True
            sage: set.union(*P)==M.groundset()
            True
            sage: sum(map(len,P))==len(M.groundset())
            True
            sage: Matroid(matrix([])).partition()
            []

        ALGORITHM:

        Reduce partition to a matroid intersection between a matroid sum
        and a partition matroid. It's known the direct method doesn't gain
        much advantage over matroid intersection. [Cun1986]"""
    @overload
    def partition(self) -> Any:
        """Matroid.partition(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7743)

        Return a minimum number of disjoint independent sets that covers the
        groundset.

        OUTPUT: list of disjoint independent sets that covers the groundset

        EXAMPLES::

            sage: M = matroids.catalog.Block_9_4()
            sage: P = M.partition()
            sage: all(map(M.is_independent,P))
            True
            sage: set.union(*P)==M.groundset()
            True
            sage: sum(map(len,P))==len(M.groundset())
            True
            sage: Matroid(matrix([])).partition()
            []

        ALGORITHM:

        Reduce partition to a matroid intersection between a matroid sum
        and a partition matroid. It's known the direct method doesn't gain
        much advantage over matroid intersection. [Cun1986]"""
    @overload
    def partition(self) -> Any:
        """Matroid.partition(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7743)

        Return a minimum number of disjoint independent sets that covers the
        groundset.

        OUTPUT: list of disjoint independent sets that covers the groundset

        EXAMPLES::

            sage: M = matroids.catalog.Block_9_4()
            sage: P = M.partition()
            sage: all(map(M.is_independent,P))
            True
            sage: set.union(*P)==M.groundset()
            True
            sage: sum(map(len,P))==len(M.groundset())
            True
            sage: Matroid(matrix([])).partition()
            []

        ALGORITHM:

        Reduce partition to a matroid intersection between a matroid sum
        and a partition matroid. It's known the direct method doesn't gain
        much advantage over matroid intersection. [Cun1986]"""
    @overload
    def plot(self, B=..., lineorders=..., pos_method=..., pos_dict=..., save_pos=...) -> Any:
        """Matroid.plot(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8131)

        Return geometric representation as a sage graphics object.

        INPUT:

        - ``B`` -- (optional) list containing a basis; if internal point
          placement is used, these elements will be placed as vertices of a
          triangle
        - ``lineorders`` -- (optional) list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: force directed (Not yet implemented)

        - ``pos_dict`` -- dictionary mapping groundset elements to their (x,y)
          positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session

        OUTPUT:

        A sage graphics object of type <class 'sage.plot.graphics.Graphics'> that
        corresponds to the geometric representation of the matroid.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: G = M.plot()                                                          # needs sage.plot sage.rings.finite_rings
            sage: type(G)                                                               # needs sage.plot sage.rings.finite_rings
            <class 'sage.plot.graphics.Graphics'>
            sage: G.show()                                                              # needs sage.plot sage.rings.finite_rings"""
    @overload
    def plot(self) -> Any:
        """Matroid.plot(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8131)

        Return geometric representation as a sage graphics object.

        INPUT:

        - ``B`` -- (optional) list containing a basis; if internal point
          placement is used, these elements will be placed as vertices of a
          triangle
        - ``lineorders`` -- (optional) list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: force directed (Not yet implemented)

        - ``pos_dict`` -- dictionary mapping groundset elements to their (x,y)
          positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session

        OUTPUT:

        A sage graphics object of type <class 'sage.plot.graphics.Graphics'> that
        corresponds to the geometric representation of the matroid.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: G = M.plot()                                                          # needs sage.plot sage.rings.finite_rings
            sage: type(G)                                                               # needs sage.plot sage.rings.finite_rings
            <class 'sage.plot.graphics.Graphics'>
            sage: G.show()                                                              # needs sage.plot sage.rings.finite_rings"""
    @overload
    def rank(self, X=...) -> Any:
        """Matroid.rank(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1389)

        Return the rank of ``X``.

        The *rank* of a subset `X` is the size of the largest independent set
        contained in `X`.

        If ``X`` is ``None``, the rank of the groundset is returned.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.rank()
            3
            sage: M.rank(['a', 'b', 'f'])
            2
            sage: M.rank(['a', 'b', 'x'])
            Traceback (most recent call last):
            ...
            ValueError: ['a', 'b', 'x'] is not a subset of the groundset"""
    @overload
    def rank(self) -> Any:
        """Matroid.rank(self, X=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1389)

        Return the rank of ``X``.

        The *rank* of a subset `X` is the size of the largest independent set
        contained in `X`.

        If ``X`` is ``None``, the rank of the groundset is returned.

        INPUT:

        - ``X`` -- (default: the groundset) a subset (or any iterable)
          of the groundset

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.rank()
            3
            sage: M.rank(['a', 'b', 'f'])
            2
            sage: M.rank(['a', 'b', 'x'])
            Traceback (most recent call last):
            ...
            ValueError: ['a', 'b', 'x'] is not a subset of the groundset"""
    @overload
    def relabel(self, mapping) -> Any:
        """Matroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8616)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.rank_matroid import RankMatroid
            sage: N = matroids.catalog.Sp8pp()
            sage: M = RankMatroid(groundset=N.groundset(), rank_function=N.rank)
            sage: sorted(M.groundset())
            [1, 2, 3, 4, 5, 6, 7, 8]
            sage: N = M.relabel({8: 0})
            sage: sorted(N.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7]
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.rank_matroid import RankMatroid
            sage: N = matroids.catalog.Sp8pp()
            sage: M = RankMatroid(groundset=N.groundset(), rank_function=N.rank)
            sage: f = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """Matroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8616)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.rank_matroid import RankMatroid
            sage: N = matroids.catalog.Sp8pp()
            sage: M = RankMatroid(groundset=N.groundset(), rank_function=N.rank)
            sage: sorted(M.groundset())
            [1, 2, 3, 4, 5, 6, 7, 8]
            sage: N = M.relabel({8: 0})
            sage: sorted(N.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7]
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.rank_matroid import RankMatroid
            sage: N = matroids.catalog.Sp8pp()
            sage: M = RankMatroid(groundset=N.groundset(), rank_function=N.rank)
            sage: f = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def show(self, B=..., lineorders=..., pos_method=..., pos_dict=..., save_pos=..., lims=...) -> Any:
        """Matroid.show(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False, lims=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8195)

        Show the geometric representation of the matroid.

        INPUT:

        - ``B`` -- (optional) a list containing elements of the groundset not
          in any particular order. If internal point placement is used, these
          elements will be placed as vertices of a triangle.
        - ``lineorders`` -- (optional) a list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying the positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: Force directed (Not yet implemented).

        - ``pos_dict`` -- dictionary mapping groundset elements to their
          (x, y) positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session
        - ``lims`` -- list of 4 elements ``[xmin,xmax,ymin,ymax]``

        EXAMPLES::

            sage: M = matroids.catalog.TernaryDowling3()
            sage: M.show(B=['a','b','c'])                                               # needs sage.plot sage.rings.finite_rings
            sage: M.show(B=['a','b','c'], lineorders=[['f','e','i']])                   # needs sage.plot sage.rings.finite_rings
            sage: pos = {'a':(0,0), 'b': (0,1), 'c':(1,0), 'd':(1,1),                   # needs sage.plot
            ....:        'e':(1,-1), 'f':(-1,1), 'g':(-1,-1),'h':(2,0), 'i':(0,2)}
            sage: M.show(pos_method=1, pos_dict=pos, lims=[-3,3,-3,3])                  # needs sage.plot sage.rings.finite_rings"""
    @overload
    def show(self, B=...) -> Any:
        """Matroid.show(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False, lims=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8195)

        Show the geometric representation of the matroid.

        INPUT:

        - ``B`` -- (optional) a list containing elements of the groundset not
          in any particular order. If internal point placement is used, these
          elements will be placed as vertices of a triangle.
        - ``lineorders`` -- (optional) a list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying the positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: Force directed (Not yet implemented).

        - ``pos_dict`` -- dictionary mapping groundset elements to their
          (x, y) positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session
        - ``lims`` -- list of 4 elements ``[xmin,xmax,ymin,ymax]``

        EXAMPLES::

            sage: M = matroids.catalog.TernaryDowling3()
            sage: M.show(B=['a','b','c'])                                               # needs sage.plot sage.rings.finite_rings
            sage: M.show(B=['a','b','c'], lineorders=[['f','e','i']])                   # needs sage.plot sage.rings.finite_rings
            sage: pos = {'a':(0,0), 'b': (0,1), 'c':(1,0), 'd':(1,1),                   # needs sage.plot
            ....:        'e':(1,-1), 'f':(-1,1), 'g':(-1,-1),'h':(2,0), 'i':(0,2)}
            sage: M.show(pos_method=1, pos_dict=pos, lims=[-3,3,-3,3])                  # needs sage.plot sage.rings.finite_rings"""
    @overload
    def show(self, B=..., lineorders=...) -> Any:
        """Matroid.show(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False, lims=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8195)

        Show the geometric representation of the matroid.

        INPUT:

        - ``B`` -- (optional) a list containing elements of the groundset not
          in any particular order. If internal point placement is used, these
          elements will be placed as vertices of a triangle.
        - ``lineorders`` -- (optional) a list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying the positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: Force directed (Not yet implemented).

        - ``pos_dict`` -- dictionary mapping groundset elements to their
          (x, y) positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session
        - ``lims`` -- list of 4 elements ``[xmin,xmax,ymin,ymax]``

        EXAMPLES::

            sage: M = matroids.catalog.TernaryDowling3()
            sage: M.show(B=['a','b','c'])                                               # needs sage.plot sage.rings.finite_rings
            sage: M.show(B=['a','b','c'], lineorders=[['f','e','i']])                   # needs sage.plot sage.rings.finite_rings
            sage: pos = {'a':(0,0), 'b': (0,1), 'c':(1,0), 'd':(1,1),                   # needs sage.plot
            ....:        'e':(1,-1), 'f':(-1,1), 'g':(-1,-1),'h':(2,0), 'i':(0,2)}
            sage: M.show(pos_method=1, pos_dict=pos, lims=[-3,3,-3,3])                  # needs sage.plot sage.rings.finite_rings"""
    @overload
    def show(self, pos_method=..., pos_dict=..., lims=...) -> Any:
        """Matroid.show(self, B=None, lineorders=None, pos_method=None, pos_dict=None, save_pos=False, lims=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8195)

        Show the geometric representation of the matroid.

        INPUT:

        - ``B`` -- (optional) a list containing elements of the groundset not
          in any particular order. If internal point placement is used, these
          elements will be placed as vertices of a triangle.
        - ``lineorders`` -- (optional) a list of lists where each of the inner
          lists specify groundset elements in a certain order which will be
          used to draw the corresponding line in geometric representation (if
          it exists)
        - ``pos_method`` -- integer specifying the positioning method
            - ``0``: default positioning
            - ``1``: use pos_dict if it is not ``None``
            - ``2``: Force directed (Not yet implemented).

        - ``pos_dict`` -- dictionary mapping groundset elements to their
          (x, y) positions
        - ``save_pos`` -- boolean indicating that point placements (either
          internal or user provided) and line orders (if provided) will be
          cached in the matroid (``M._cached_info``) and can be used for
          reproducing the geometric representation during the same session
        - ``lims`` -- list of 4 elements ``[xmin,xmax,ymin,ymax]``

        EXAMPLES::

            sage: M = matroids.catalog.TernaryDowling3()
            sage: M.show(B=['a','b','c'])                                               # needs sage.plot sage.rings.finite_rings
            sage: M.show(B=['a','b','c'], lineorders=[['f','e','i']])                   # needs sage.plot sage.rings.finite_rings
            sage: pos = {'a':(0,0), 'b': (0,1), 'c':(1,0), 'd':(1,1),                   # needs sage.plot
            ....:        'e':(1,-1), 'f':(-1,1), 'g':(-1,-1),'h':(2,0), 'i':(0,2)}
            sage: M.show(pos_method=1, pos_dict=pos, lims=[-3,3,-3,3])                  # needs sage.plot sage.rings.finite_rings"""
    @overload
    def simplify(self) -> Any:
        """Matroid.simplify(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4918)

        Return the simplification of the matroid.

        A matroid is *simple* if it contains no circuits of length 1 or 2.
        The *simplification* of a matroid is obtained by deleting all loops
        (circuits of length 1) and deleting all but one element from each
        parallel class (a closed set of rank 1, that is, each pair in it forms
        a circuit of length 2).

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.cosimplify() <sage.matroids.matroid.Matroid.cosimplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().contract('a')
            sage: M.size() - M.simplify().size()
            3"""
    @overload
    def simplify(self) -> Any:
        """Matroid.simplify(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4918)

        Return the simplification of the matroid.

        A matroid is *simple* if it contains no circuits of length 1 or 2.
        The *simplification* of a matroid is obtained by deleting all loops
        (circuits of length 1) and deleting all but one element from each
        parallel class (a closed set of rank 1, that is, each pair in it forms
        a circuit of length 2).

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.is_simple() <sage.matroids.matroid.Matroid.is_simple>`,
            :meth:`M.loops() <sage.matroids.matroid.Matroid.loops>`,
            :meth:`M.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`M.cosimplify() <sage.matroids.matroid.Matroid.cosimplify>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano().contract('a')
            sage: M.size() - M.simplify().size()
            3"""
    @overload
    def size(self) -> Any:
        """Matroid.size(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1314)

        Return the size of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.size()
            8"""
    @overload
    def size(self) -> Any:
        """Matroid.size(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1314)

        Return the size of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.size()
            8"""
    @overload
    def ternary_matroid(self, randomized_tests=..., verify=...) -> Any:
        """Matroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6514)

        Return a ternary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a ternary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is ternary

        OUTPUT: either a
        :class:`TernaryMatroid <sage.matroids.linear_matroid.TernaryMatroid>`,
        or ``None``

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a ternary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M._local_ternary_matroid()
            <sage.matroids.matroid.Matroid._local_ternary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.ternary_matroid() is None                                           # needs sage.graphs
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid()                                                   # needs sage.graphs
            NonFano: Ternary matroid of rank 3 on 7 elements, type 0-"""
    @overload
    def ternary_matroid(self) -> Any:
        """Matroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6514)

        Return a ternary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a ternary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is ternary

        OUTPUT: either a
        :class:`TernaryMatroid <sage.matroids.linear_matroid.TernaryMatroid>`,
        or ``None``

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a ternary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M._local_ternary_matroid()
            <sage.matroids.matroid.Matroid._local_ternary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.ternary_matroid() is None                                           # needs sage.graphs
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid()                                                   # needs sage.graphs
            NonFano: Ternary matroid of rank 3 on 7 elements, type 0-"""
    @overload
    def ternary_matroid(self) -> Any:
        """Matroid.ternary_matroid(self, randomized_tests=1, verify=True)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 6514)

        Return a ternary matroid representing ``self``, if such a
        representation exists.

        INPUT:

        - ``randomized_tests`` -- (default: 1) an integer; the number of
          times a certain necessary condition for being ternary is tested,
          using randomization
        - ``verify`` -- boolean (default: ``True``); if ``True``,
          any output will be a ternary matroid representing ``self``; if
          ``False``, any output will represent ``self`` if and only if the
          matroid is ternary

        OUTPUT: either a
        :class:`TernaryMatroid <sage.matroids.linear_matroid.TernaryMatroid>`,
        or ``None``

        ALGORITHM:

        First, compare the ternary matroids local to two random bases.
        If these matroids are not  isomorphic, return ``None``. This
        test is performed ``randomized_tests`` times. Next, if ``verify``
        is ``True``, test if a ternary matroid local to some basis is
        isomorphic to ``self``.

        .. SEEALSO::

            :meth:`M._local_ternary_matroid()
            <sage.matroids.matroid.Matroid._local_ternary_matroid>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.ternary_matroid() is None                                           # needs sage.graphs
            True
            sage: N = matroids.catalog.NonFano()
            sage: N.ternary_matroid()                                                   # needs sage.graphs
            NonFano: Ternary matroid of rank 3 on 7 elements, type 0-"""
    @overload
    def truncation(self) -> Any:
        """Matroid.truncation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4313)

        Return a rank-1 truncation of the matroid.

        Let `M` be a matroid of rank `r`. The *truncation* of `M` is the
        matroid obtained by declaring all subsets of size `r` dependent. It
        can be obtained by adding an element freely to the span of the matroid
        and then contracting that element.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = M.truncation()
            sage: N.is_isomorphic(matroids.Uniform(2, 7))
            True"""
    @overload
    def truncation(self) -> Any:
        """Matroid.truncation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4313)

        Return a rank-1 truncation of the matroid.

        Let `M` be a matroid of rank `r`. The *truncation* of `M` is the
        matroid obtained by declaring all subsets of size `r` dependent. It
        can be obtained by adding an element freely to the span of the matroid
        and then contracting that element.

        OUTPUT: matroid

        .. SEEALSO::

            :meth:`M.extension() <sage.matroids.matroid.Matroid.extension>`,
            :meth:`M.contract() <sage.matroids.matroid.Matroid.contract>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = M.truncation()
            sage: N.is_isomorphic(matroids.Uniform(2, 7))
            True"""
    def tutte_polynomial(self, x=..., y=...) -> Any:
        """Matroid.tutte_polynomial(self, x=None, y=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 7881)

        Return the Tutte polynomial of the matroid.

        The *Tutte polynomial* of a matroid is the polynomial

        .. MATH::

            T(x, y) = \\sum_{A \\subseteq E} (x - 1)^{r(E) - r(A)} (y - 1)^{r^*(E) - r^*(E\\setminus A)},

        where `E` is the groundset of the matroid, `r` is the rank function,
        and `r^*` is the corank function. Tutte defined his polynomial
        differently:

        .. MATH::

            T(x, y)=\\sum_{B} x^i(B) y^e(B),

        where the sum ranges over all bases of the matroid, `i(B)` is the
        number of internally active elements of `B`, and `e(B)` is the number
        of externally active elements of `B`.

        INPUT:

        - ``x`` -- (optional) a variable or numerical argument
        - ``y`` -- (optional) a variable or numerical argument

        OUTPUT:

        The Tutte-polynomial `T(x, y)`, where `x` and `y` are substituted with
        any values provided as input.

        .. TODO::

            Make implementation more efficient, e.g. generalizing the
            approach from :issue:`1314` from graphs to matroids.

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: M.tutte_polynomial()
            y^4 + x^3 + 3*y^3 + 4*x^2 + 7*x*y + 6*y^2 + 3*x + 3*y
            sage: M.tutte_polynomial(1, 1) == M.bases_count()
            True

        ALGORITHM:

        Enumerate the bases and compute the internal and external activities
        for each `B`."""
    def union(self, matroids) -> Any:
        """Matroid.union(self, matroids)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 8498)

        Return the matroid union with another matroid or a list of matroids.

        Let `(M_1, M_2, \\ldots, M_k)` be a list of matroids where each `M_i`
        has groundset `E_i`. The *matroid
        union* `M` of `(M_1, M_2, \\ldots, M_k)` has groundset `E = \\cup E_i`.
        Moreover, a set `I \\subseteq E` is independent in `M` if and only if
        the restriction of `I` to `E_i` is independent in `M_i` for every `i`.

        INPUT:

        - ``matroids`` -- matroid or a list of matroids

        OUTPUT: an instance of
        :class:`MatroidUnion <sage.matroids.union_matroid.MatroidUnion>`

        EXAMPLES::

            sage: M = matroids.catalog.Fano()
            sage: N = M.union(matroids.catalog.NonFano()); N
            Matroid of rank 6 on 7 elements as matroid union of
            Binary matroid of rank 3 on 7 elements, type (3, 0)
            Ternary matroid of rank 3 on 7 elements, type 0-"""
    def whitney_numbers(self) -> list:
        """Matroid.whitney_numbers(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3114)

        Return the Whitney numbers of the first kind of the matroid.

        The Whitney numbers of the first kind -- here encoded as a vector
        `(w_0=1, \\ldots, w_r)` -- are numbers of alternating sign, where `w_i`
        is the value of the coefficient of the `(r-i)`-th degree term of the
        matroid's characteristic polynomial. Moreover, `|w_i|` is the number of
        `(i-1)`-dimensional faces of the broken circuit complex of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: M = matroids.catalog.BetsyRoss()
            sage: M.whitney_numbers()
            [1, -11, 35, -25]

        TESTS::

            sage: M = Matroid(groundset=[0,1,2], circuits=[[0]])
            sage: M.whitney_numbers()
            []"""
    def whitney_numbers2(self) -> list:
        """Matroid.whitney_numbers2(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3143)

        Return the Whitney numbers of the second kind of the matroid.

        The Whitney numbers of the second kind are here encoded as a vector
        `(W_0, \\ldots, W_r)`, where `W_i` is the number of flats of rank `i`,
        and `r` is the rank of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: M = matroids.catalog.BetsyRoss()
            sage: M.whitney_numbers2()
            [1, 11, 20, 1]"""
    def __copy__(self) -> Any:
        """Matroid.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 524)

        Create a shallow copy.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: matroids_lst = [
            ....:     BasisMatroid(matroids.catalog.Vamos()),
            ....:     CircuitsMatroid(matroids.catalog.Vamos()),
            ....:     CircuitClosuresMatroid(matroids.catalog.Vamos()),
            ....:     FlatsMatroid(matroids.catalog.Vamos()),
            ....:     Matroid(groundset=range(10), rank_function=lambda X: min(len(X), 4)),
            ....:     Matroid(Matrix(GF(7), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(2), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(3), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(4, 'x'), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     matroids.catalog.R10()
            ....: ]
            sage: for M in matroids_lst:  # indirect doctest
            ....:     N = copy(M)
            ....:     assert M == N
            ....:     assert M.groundset() is N.groundset()

            sage: M = Matroid(graphs.PappusGraph())
            sage: N = copy(M)
            sage: M == N
            True
            sage: M._G is N._G
            True

            sage: M = MinorMatroid(matroid=matroids.catalog.Vamos(),
            ....:                  contractions={'a', 'b'}, deletions={'f'})
            sage: N = copy(M)  # indirect doctest
            sage: M == N
            True
            sage: M._matroid is N._matroid
            True

            sage: from sage.matroids.lean_matrix import *
            sage: A = GenericMatrix(2, 5, Matrix(GF(5), [[1, 0, 1, 1, 1], [0, 1, 1, 2, 3]]))
            sage: A == copy(A)  # indirect doctest
            True"""
    def __deepcopy__(self, memo=...) -> Any:
        """Matroid.__deepcopy__(self, memo=None)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 570)

        Create a deep copy.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: matroids_lst = [
            ....:     BasisMatroid(matroids.catalog.Vamos()),
            ....:     CircuitsMatroid(matroids.catalog.Vamos()),
            ....:     CircuitClosuresMatroid(matroids.catalog.Vamos()),
            ....:     FlatsMatroid(matroids.catalog.Vamos()),
            ....:     Matroid(groundset=range(10), rank_function=lambda X: min(len(X), 4)),
            ....:     Matroid(Matrix(GF(7), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(2), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(3), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     Matroid(Matrix(GF(4, 'x'), [[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,3]])),
            ....:     matroids.catalog.R10()
            ....: ]
            sage: for M in matroids_lst:  # indirect doctest
            ....:     N = deepcopy(M)
            ....:     assert M == N
            ....:     assert M.groundset() is N.groundset()

            sage: M = Matroid(graphs.PappusGraph())
            sage: N = deepcopy(M)
            sage: M == N
            True
            sage: M._G is N._G
            True

            sage: M = MinorMatroid(matroid=matroids.catalog.Vamos(),
            ....:                  contractions={'a', 'b'}, deletions={'f'})
            sage: N = deepcopy(M)  # indirect doctest
            sage: M == N
            True
            sage: M._matroid is N._matroid
            True

            sage: from sage.matroids.lean_matrix import *
            sage: A = GenericMatrix(2, 5, Matrix(GF(5), [[1, 0, 1, 1, 1], [0, 1, 1, 2, 3]]))
            sage: A == deepcopy(A)  # indirect doctest
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """Matroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 3935)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: M = matroids.catalog.BetsyRoss()
            sage: N = matroids.catalog.BetsyRoss()
            sage: hash(M) == hash(N)
            True
            sage: O = matroids.catalog.TicTacToe()
            sage: hash(M) == hash(O)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """Matroid.__len__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 1302)

        Return the size of the groundset.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: len(M)
            8"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __truediv__(self, X) -> Any:
        """Matroid.__truediv__(self, X)

        File: /build/sagemath/src/sage/src/sage/matroids/matroid.pyx (starting at line 4195)

        Shorthand for ``self.contract(X)``.

        EXAMPLES::

            sage: M = matroids.CompleteGraphic(4)                                       # needs sage.graphs
            sage: M.contract(1) == M.__truediv__(1)                                     # needs sage.graphs
            True"""
