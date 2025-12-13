from sage.combinat.root_system.cartan_type import CartanType as CartanType, CartanType_abstract as CartanType_abstract
from sage.combinat.root_system.reflection_group_complex import ComplexReflectionGroup as ComplexReflectionGroup, IrreducibleComplexReflectionGroup as IrreducibleComplexReflectionGroup
from sage.combinat.root_system.reflection_group_element import RealReflectionGroupElement as RealReflectionGroupElement
from sage.interfaces.gap3 import gap3 as gap3
from sage.misc.cachefunc import cached_function as cached_function, cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ

def ReflectionGroup(*args, **kwds):
    """
    Construct a finite (complex or real) reflection group as a Sage
    permutation group by fetching the permutation representation of the
    generators from chevie's database.

    INPUT:

    Can be one or multiple of the following:

    - a triple `(r, p, n)` with `p` divides `r`, which denotes the group
      `G(r, p, n)`

    - an integer between `4` and `37`, which denotes an exceptional
      irreducible complex reflection group

    - a finite Cartan-Killing type

    EXAMPLES:

    Finite reflection groups can be constructed from

    Cartan-Killing classification types::

        sage: W = ReflectionGroup(['A',3]); W
         Irreducible real reflection group of rank 3 and type A3

        sage: W = ReflectionGroup(['H',4]); W
         Irreducible real reflection group of rank 4 and type H4

        sage: W = ReflectionGroup(['I',5]); W
         Irreducible real reflection group of rank 2 and type I2(5)

    the complex infinite family `G(r,p,n)` with `p` divides `r`::

        sage: W = ReflectionGroup((1,1,4)); W
        Irreducible real reflection group of rank 3 and type A3

        sage: W = ReflectionGroup((2,1,3)); W
        Irreducible real reflection group of rank 3 and type B3

    Chevalley-Shepard-Todd exceptional classification types::

        sage: W = ReflectionGroup(23); W
        Irreducible real reflection group of rank 3 and type H3

    Cartan types and matrices::

        sage: ReflectionGroup(CartanType(['A',2]))
        Irreducible real reflection group of rank 2 and type A2

        sage: ReflectionGroup(CartanType((['A',2],['A',2])))
        Reducible real reflection group of rank 4 and type A2 x A2

        sage: C = CartanMatrix(['A',2])
        sage: ReflectionGroup(C)
        Irreducible real reflection group of rank 2 and type A2

    multiples of the above::

        sage: W = ReflectionGroup(['A',2],['B',2]); W
        Reducible real reflection group of rank 4 and type A2 x B2

        sage: W = ReflectionGroup(['A',2],4); W
        Reducible complex reflection group of rank 4 and type A2 x ST4

        sage: W = ReflectionGroup((4,2,2),4); W
        Reducible complex reflection group of rank 4 and type G(4,2,2) x ST4
    """
@cached_function
def is_chevie_available():
    """
    Test whether the GAP3 Chevie package is available.

    EXAMPLES::

        sage: # needs sage.groups
        sage: from sage.combinat.root_system.reflection_group_real import is_chevie_available
        sage: is_chevie_available() # random
        False
        sage: is_chevie_available() in [True, False]
        True
    """

class RealReflectionGroup(ComplexReflectionGroup):
    """
    A real reflection group given as a permutation group.

    .. SEEALSO::

        :func:`ReflectionGroup`
    """
    def __init__(self, W_types, index_set=None, hyperplane_index_set=None, reflection_index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: W = ReflectionGroup(['A',3])
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
          * ``\'parabolic\'`` -- iterate by using parabolic subgroups

        - ``tracking_words`` -- boolean (default: ``True``); whether or not to
          keep track of the reduced words and store them in ``_reduced_word``

        .. NOTE::

            The fastest iteration is the parabolic iteration and the
            depth first algorithm without tracking words is second.
            In particular, ``\'depth\'`` is ~1.5x faster than ``\'breadth\'``.

        .. NOTE::

            The ``\'parabolic\'`` iteration does not track words and requires
            keeping the subgroup corresponding to `I \\setminus \\{i\\}` in
            memory (for each `i` individually).

        EXAMPLES::

            sage: W = ReflectionGroup(["B",2])

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
        '''
    def __iter__(self):
        '''
        Return an iterator going through all elements in ``self``.

        For options and faster iteration see :meth:`iteration`.

        EXAMPLES::

            sage: W = ReflectionGroup(["B",2])

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
    def bipartite_index_set(self):
        '''
        Return the bipartite index set of a real reflection group.

        EXAMPLES::

            sage: W = ReflectionGroup(["A",5])
            sage: W.bipartite_index_set()
            [[1, 3, 5], [2, 4]]

            sage: W = ReflectionGroup(["A",5],index_set=[\'a\',\'b\',\'c\',\'d\',\'e\'])
            sage: W.bipartite_index_set()
            [[\'a\', \'c\', \'e\'], [\'b\', \'d\']]
        '''
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: W.cartan_type()
            ['A', 3]

            sage: W = ReflectionGroup(['A',3], ['B',3])
            sage: W.cartan_type()
            A3xB3 relabelled by {1: 3, 2: 2, 3: 1}

        TESTS:

        Check that dihedral types are handled properly::

            sage: W = ReflectionGroup(['I',3]); W
            Irreducible real reflection group of rank 2 and type A2

            sage: W = ReflectionGroup(['I',4]); W
            Irreducible real reflection group of rank 2 and type C2

            sage: W = ReflectionGroup(['I',5]); W
            Irreducible real reflection group of rank 2 and type I2(5)
        """
    def positive_roots(self):
        """
        Return the positive roots of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3], ['B',2])
            sage: W.positive_roots()
            [(1, 0, 0, 0, 0),
             (0, 1, 0, 0, 0),
             (0, 0, 1, 0, 0),
             (0, 0, 0, 1, 0),
             (0, 0, 0, 0, 1),
             (1, 1, 0, 0, 0),
             (0, 1, 1, 0, 0),
             (0, 0, 0, 1, 1),
             (1, 1, 1, 0, 0),
             (0, 0, 0, 2, 1)]

            sage: W = ReflectionGroup(['A',3])
            sage: W.positive_roots()
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 1, 1)]
        """
    def almost_positive_roots(self):
        """
        Return the almost positive roots of ``self``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3], ['B',2])
            sage: W.almost_positive_roots()
            [(-1, 0, 0, 0, 0),
             (0, -1, 0, 0, 0),
             (0, 0, -1, 0, 0),
             (0, 0, 0, -1, 0),
             (0, 0, 0, 0, -1),
             (1, 0, 0, 0, 0),
             (0, 1, 0, 0, 0),
             (0, 0, 1, 0, 0),
             (0, 0, 0, 1, 0),
             (0, 0, 0, 0, 1),
             (1, 1, 0, 0, 0),
             (0, 1, 1, 0, 0),
             (0, 0, 0, 1, 1),
             (1, 1, 1, 0, 0),
             (0, 0, 0, 2, 1)]

            sage: W = ReflectionGroup(['A',3])
            sage: W.almost_positive_roots()
            [(-1, 0, 0),
             (0, -1, 0),
             (0, 0, -1),
             (1, 0, 0),
             (0, 1, 0),
             (0, 0, 1),
             (1, 1, 0),
             (0, 1, 1),
             (1, 1, 1)]
        """
    def root_to_reflection(self, root):
        """
        Return the reflection along the given ``root``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: for beta in W.roots(): W.root_to_reflection(beta)
            (1,4)(2,3)(5,6)
            (1,3)(2,5)(4,6)
            (1,5)(2,4)(3,6)
            (1,4)(2,3)(5,6)
            (1,3)(2,5)(4,6)
            (1,5)(2,4)(3,6)
        """
    def reflection_to_positive_root(self, r):
        """
        Return the positive root orthogonal to the given reflection.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: for r in W.reflections():
            ....:     print(W.reflection_to_positive_root(r))
            (1, 0)
            (0, 1)
            (1, 1)
        """
    @cached_method
    def fundamental_weights(self):
        '''
        Return the fundamental weights of ``self`` in terms of the simple roots.

        The fundamental weights are defined by
        `s_j(\\omega_i) = \\omega_i - \\delta_{i=j}\\alpha_j`
        for the simple reflection `s_j` with corresponding simple
        roots `\\alpha_j`.

        In other words, the transpose Cartan matrix sends the weight
        basis to the root basis. Observe again that the action here is
        defined as a right action, see the example below.

        EXAMPLES::

            sage: W = ReflectionGroup([\'A\',3], [\'B\',2])
            sage: W.fundamental_weights()
            Finite family {1: (3/4, 1/2, 1/4, 0, 0), 2: (1/2, 1, 1/2, 0, 0), 3: (1/4, 1/2, 3/4, 0, 0), 4: (0, 0, 0, 1, 1/2), 5: (0, 0, 0, 1, 1)}

            sage: W = ReflectionGroup([\'A\',3])
            sage: W.fundamental_weights()
            Finite family {1: (3/4, 1/2, 1/4), 2: (1/2, 1, 1/2), 3: (1/4, 1/2, 3/4)}

            sage: W = ReflectionGroup([\'A\',3])
            sage: S = W.simple_reflections()
            sage: N = W.fundamental_weights()
            sage: for i in W.index_set():
            ....:     for j in W.index_set():
            ....:         print("{} {} {} {}".format(i, j, N[i], N[i]*S[j].to_matrix()))
            1 1 (3/4, 1/2, 1/4) (-1/4, 1/2, 1/4)
            1 2 (3/4, 1/2, 1/4) (3/4, 1/2, 1/4)
            1 3 (3/4, 1/2, 1/4) (3/4, 1/2, 1/4)
            2 1 (1/2, 1, 1/2) (1/2, 1, 1/2)
            2 2 (1/2, 1, 1/2) (1/2, 0, 1/2)
            2 3 (1/2, 1, 1/2) (1/2, 1, 1/2)
            3 1 (1/4, 1/2, 3/4) (1/4, 1/2, 3/4)
            3 2 (1/4, 1/2, 3/4) (1/4, 1/2, 3/4)
            3 3 (1/4, 1/2, 3/4) (1/4, 1/2, -1/4)
        '''
    def fundamental_weight(self, i):
        """
        Return the fundamental weight with index ``i``.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: [ W.fundamental_weight(i) for i in W.index_set() ]
            [(3/4, 1/2, 1/4), (1/2, 1, 1/2), (1/4, 1/2, 3/4)]
        """
    @cached_method
    def coxeter_diagram(self):
        """
        Return the Coxeter diagram associated to ``self``.

        EXAMPLES::

            sage: G = ReflectionGroup(['B',3])
            sage: G.coxeter_diagram().edges(labels=True, sort=True)
            [(1, 2, 4), (2, 3, 3)]
        """
    @cached_method
    def coxeter_matrix(self):
        """
        Return the Coxeter matrix associated to ``self``.

        EXAMPLES::

            sage: G = ReflectionGroup(['A',3])
            sage: G.coxeter_matrix()
            [1 3 2]
            [3 1 3]
            [2 3 1]
        """
    @cached_method
    def right_coset_representatives(self, J):
        '''
        Return the right coset representatives of ``self`` for the
        parabolic subgroup generated by the simple reflections in ``J``.

        EXAMPLES::

            sage: W = ReflectionGroup(["A",3])
            sage: for J in Subsets([1,2,3]): W.right_coset_representatives(J)
            [(), (2,5)(3,9)(4,6)(8,11)(10,12), (1,4)(2,8)(3,5)(7,10)(9,11),
             (1,7)(2,4)(5,6)(8,10)(11,12), (1,2,10)(3,6,5)(4,7,8)(9,12,11),
             (1,4,6)(2,3,11)(5,8,9)(7,10,12), (1,6,4)(2,11,3)(5,9,8)(7,12,10),
             (1,7)(2,6)(3,9)(4,5)(8,12)(10,11),
             (1,10,2)(3,5,6)(4,8,7)(9,11,12), (1,2,3,12)(4,5,10,11)(6,7,8,9),
             (1,5,9,10)(2,12,8,6)(3,4,7,11), (1,6)(2,9)(3,8)(5,11)(7,12),
             (1,8)(2,7)(3,6)(4,10)(9,12), (1,10,9,5)(2,6,8,12)(3,11,7,4),
             (1,12,3,2)(4,11,10,5)(6,9,8,7), (1,3)(2,12)(4,10)(5,11)(6,8)(7,9),
             (1,5,12)(2,9,4)(3,10,8)(6,7,11), (1,8,11)(2,5,7)(3,12,4)(6,10,9),
             (1,11,8)(2,7,5)(3,4,12)(6,9,10), (1,12,5)(2,4,9)(3,8,10)(6,11,7),
             (1,3,7,9)(2,11,6,10)(4,8,5,12), (1,9,7,3)(2,10,6,11)(4,12,5,8),
             (1,11)(3,10)(4,9)(5,7)(6,12), (1,9)(2,8)(3,7)(4,11)(5,10)(6,12)]
            [(), (2,5)(3,9)(4,6)(8,11)(10,12), (1,4)(2,8)(3,5)(7,10)(9,11),
             (1,2,10)(3,6,5)(4,7,8)(9,12,11), (1,4,6)(2,3,11)(5,8,9)(7,10,12),
             (1,6,4)(2,11,3)(5,9,8)(7,12,10), (1,2,3,12)(4,5,10,11)(6,7,8,9),
             (1,5,9,10)(2,12,8,6)(3,4,7,11), (1,6)(2,9)(3,8)(5,11)(7,12),
             (1,3)(2,12)(4,10)(5,11)(6,8)(7,9),
             (1,5,12)(2,9,4)(3,10,8)(6,7,11), (1,3,7,9)(2,11,6,10)(4,8,5,12)]
            [(), (2,5)(3,9)(4,6)(8,11)(10,12), (1,7)(2,4)(5,6)(8,10)(11,12),
             (1,4,6)(2,3,11)(5,8,9)(7,10,12),
             (1,7)(2,6)(3,9)(4,5)(8,12)(10,11),
             (1,10,2)(3,5,6)(4,8,7)(9,11,12), (1,2,3,12)(4,5,10,11)(6,7,8,9),
             (1,10,9,5)(2,6,8,12)(3,11,7,4), (1,12,3,2)(4,11,10,5)(6,9,8,7),
             (1,8,11)(2,5,7)(3,12,4)(6,10,9), (1,12,5)(2,4,9)(3,8,10)(6,11,7),
             (1,11)(3,10)(4,9)(5,7)(6,12)]
            [(), (1,4)(2,8)(3,5)(7,10)(9,11), (1,7)(2,4)(5,6)(8,10)(11,12),
             (1,2,10)(3,6,5)(4,7,8)(9,12,11), (1,6,4)(2,11,3)(5,9,8)(7,12,10),
             (1,10,2)(3,5,6)(4,8,7)(9,11,12), (1,5,9,10)(2,12,8,6)(3,4,7,11),
             (1,8)(2,7)(3,6)(4,10)(9,12), (1,12,3,2)(4,11,10,5)(6,9,8,7),
             (1,3)(2,12)(4,10)(5,11)(6,8)(7,9),
             (1,11,8)(2,7,5)(3,4,12)(6,9,10), (1,9,7,3)(2,10,6,11)(4,12,5,8)]
            [(), (2,5)(3,9)(4,6)(8,11)(10,12), (1,4,6)(2,3,11)(5,8,9)(7,10,12),
             (1,2,3,12)(4,5,10,11)(6,7,8,9)]
            [(), (1,4)(2,8)(3,5)(7,10)(9,11), (1,2,10)(3,6,5)(4,7,8)(9,12,11),
             (1,6,4)(2,11,3)(5,9,8)(7,12,10), (1,5,9,10)(2,12,8,6)(3,4,7,11),
             (1,3)(2,12)(4,10)(5,11)(6,8)(7,9)]
            [(), (1,7)(2,4)(5,6)(8,10)(11,12), (1,10,2)(3,5,6)(4,8,7)(9,11,12),
             (1,12,3,2)(4,11,10,5)(6,9,8,7)]
            [()]
        '''
    def simple_root_index(self, i):
        """
        Return the index of the simple root `\\alpha_i`.

        This is the position of `\\alpha_i` in the list of simple roots.

        EXAMPLES::

            sage: W = ReflectionGroup(['A',3])
            sage: [W.simple_root_index(i) for i in W.index_set()]
            [0, 1, 2]
        """
    def bruhat_cone(self, x, y, side: str = 'upper', backend: str = 'cdd'):
        """
        Return the (upper or lower) Bruhat cone associated to the interval ``[x,y]``.

        To a cover relation `v \\prec w` in strong Bruhat order you can assign a positive
        root `\\beta` given by the unique reflection `s_\\beta` such that `s_\\beta v = w`.

        The upper Bruhat cone of the interval `[x,y]` is the non-empty, polyhedral cone generated
        by the roots corresponding to `x \\prec a` for all atoms `a` in the interval.
        The lower Bruhat cone of the interval `[x,y]` is the non-empty, polyhedral cone generated
        by the roots corresponding to `c \\prec y` for all coatoms `c` in the interval.

        INPUT:

        - ``x`` -- an element in the group `W`
        - ``y`` -- an element in the group `W`
        - ``side`` -- (default: ``'upper'``) must be one of the following:

          * ``'upper'`` -- return the upper Bruhat cone of the interval [``x``, ``y``]
          * ``'lower'`` -- return the lower Bruhat cone of the interval [``x``, ``y``]

        - ``backend`` -- string (default: ``'cdd'``); the backend to use to create the polyhedron

        EXAMPLES::

            sage: W = ReflectionGroup(['A',2])
            sage: x = W.from_reduced_word([1])
            sage: y = W.w0
            sage: W.bruhat_cone(x, y)
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 rays

            sage: W = ReflectionGroup(['E',6])
            sage: x = W.one()
            sage: y = W.w0
            sage: W.bruhat_cone(x, y, side='lower')
            A 6-dimensional polyhedron in QQ^6 defined as the convex hull of 1 vertex and 6 rays

        TESTS::

            sage: W = ReflectionGroup(['A',2])
            sage: x = W.one()
            sage: y = W.w0
            sage: W.bruhat_cone(x, y, side='nonsense')
            Traceback (most recent call last):
            ...
            ValueError: side must be either 'upper' or 'lower'

        REFERENCES:

        - [Dy1994]_
        - [JS2021]_
        """
    class Element(RealReflectionGroupElement, ComplexReflectionGroup.Element):
        @cached_in_parent_method
        def right_coset_representatives(self):
            '''
            Return the right coset representatives of ``self``.

            EXAMPLES::

                sage: W = ReflectionGroup([\'A\',2])
                sage: for w in W:
                ....:     rcr = w.right_coset_representatives()
                ....:     print("%s %s"%(w.reduced_word(),
                ....:                    [v.reduced_word() for v in rcr]))
                [] [[], [2], [1], [2, 1], [1, 2], [1, 2, 1]]
                [2] [[], [2], [1]]
                [1] [[], [1], [1, 2]]
                [1, 2] [[]]
                [2, 1] [[]]
                [1, 2, 1] [[], [2], [2, 1]]
            '''
        def left_coset_representatives(self):
            '''
            Return the left coset representatives of ``self``.

            .. SEEALSO:: :meth:`right_coset_representatives`

            EXAMPLES::

                sage: W = ReflectionGroup([\'A\',2])
                sage: for w in W:
                ....:     lcr = w.left_coset_representatives()
                ....:     print("%s %s"%(w.reduced_word(),
                ....:                    [v.reduced_word() for v in lcr]))
                [] [[], [2], [1], [1, 2], [2, 1], [1, 2, 1]]
                [2] [[], [2], [1]]
                [1] [[], [1], [2, 1]]
                [1, 2] [[]]
                [2, 1] [[]]
                [1, 2, 1] [[], [2], [1, 2]]
            '''

class IrreducibleRealReflectionGroup(RealReflectionGroup, IrreducibleComplexReflectionGroup):
    class Element(RealReflectionGroup.Element, IrreducibleComplexReflectionGroup.Element): ...
