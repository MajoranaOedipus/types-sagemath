from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.structure.element import Element as Element, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FastCrystal(UniqueRepresentation, Parent):
    """
    An alternative implementation of rank 2 crystals. The root
    operators are implemented in memory by table lookup. This means
    that in comparison with the
    :class:`~sage.combinat.crystals.tensor_product.CrystalsOfTableaux`, these
    crystals are slow to instantiate but faster for computation. Implemented
    for types `A_2`, `B_2`, and `C_2`.

    INPUT:

    - ``cartan_type`` -- the Cartan type and must be either type `A_2`, `B_2`, or `C_2`

    - ``shape`` -- a shape is of the form ``[l1,l2]`` where ``l1`` and ``l2``
      are either integers or (in type `B_2`) half integers such that
      ``l1 - l2`` is integral. It is assumed that ``l1 >= l2 >= 0``. If
      ``l1`` and ``l2`` are integers, this will produce a crystal
      isomorphic to the one obtained by
      ``crystals.Tableaux(type, shape=[l1,l2])``. Furthermore
      ``crystals.FastRankTwo(['B', 2], l1+1/2, l2+1/2)`` produces a crystal
      isomorphic to the following crystal ``T``::

          sage: C = crystals.Tableaux(['B',2], shape=[l1,l2])               # not tested
          sage: D = crystals.Spins(['B',2])                                 # not tested
          sage: T = crystals.TensorProduct(C, D, C.list()[0], D.list()[0])  # not tested

    - ``format`` -- (default: ``'string'``) the default representation of
      elements is in term of theBerenstein-Zelevinsky-Littelmann (BZL)
      strings ``[a1, a2, ...]`` described under metapost in
      :mod:`~sage.categories.crystals`. Alternative representations may be
      obtained by the options ``'dual_string'`` or ``'simple'``.
      In the ``'simple'`` format, the element is represented by and integer,
      and in the ``'dual_string'`` format, it is represented by the
      BZL string, but the underlying decomposition of the long Weyl group
      element into simple reflections is changed.

    TESTS::

        sage: C = crystals.FastRankTwo(['A',2],shape=[4,1])
        sage: C.cardinality()
        24
        sage: C.cartan_type()
        ['A', 2]
        sage: TestSuite(C).run()
        sage: C = crystals.FastRankTwo(['B',2],shape=[4,1])
        sage: C.cardinality()
        154
        sage: TestSuite(C).run()
        sage: C = crystals.FastRankTwo(['B',2],shape=[3/2,1/2])
        sage: C.cardinality()
        16
        sage: TestSuite(C).run()
        sage: C = crystals.FastRankTwo(['C',2],shape=[2,1])
        sage: C.cardinality()
        16
        sage: C = crystals.FastRankTwo(['C',2],shape=[3,1])
        sage: C.cardinality()
        35
        sage: TestSuite(C).run()

        sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
        sage: C.list()
        [[0, 0, 0],
         [1, 0, 0],
         [0, 1, 1],
         [0, 2, 1],
         [1, 2, 1],
         [0, 1, 0],
         [1, 1, 0],
         [2, 1, 0]]
    """
    @staticmethod
    def __classcall__(cls, cartan_type, shape, format: str = 'string'):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: C1 = crystals.FastRankTwo(['A',2],            shape=(4,1))
            sage: C2 = crystals.FastRankTwo(CartanType(['A',2]),shape=[4,1])
            sage: C1 is C2
            True
        """
    delpat: Incomplete
    gampat: Incomplete
    format: Incomplete
    size: Incomplete
    shape: Incomplete
    module_generators: Incomplete
    def __init__(self, ct, shape, format) -> None:
        """
        EXAMPLES::

            sage: C = crystals.FastRankTwo(['A',2],shape=[4,1]); C
            The fast crystal for A2 with shape [4,1]
            sage: TestSuite(C).run()
        """
    def __call__(self, value):
        """
        EXAMPLES::

            sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
            sage: C(0)
            [0, 0, 0]
            sage: C(1)
            [1, 0, 0]
            sage: x = C(0)
            sage: C(x) is x
            True
        """
    def digraph(self):
        """
        Return the digraph associated to ``self``.

        EXAMPLES::

            sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
            sage: C.digraph()
            Digraph on 8 vertices
        """
    def cmp_elements(self, x, y):
        """
        Return ``True`` if and only if there is a path from `x` to `y` in the
        crystal graph.

        Because the crystal graph is classical, it is a directed acyclic
        graph which can be interpreted as a poset. This function implements
        the comparison function of this poset.

        EXAMPLES::

            sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
            sage: x = C(0)
            sage: y = C(1)
            sage: C.cmp_elements(x,y)
            -1
            sage: C.cmp_elements(y,x)
            1
            sage: C.cmp_elements(x,x)
            0
        """
    class Element(Element):
        value: Incomplete
        format: Incomplete
        def __init__(self, parent, value, format) -> None:
            """
            EXAMPLES::

                sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
                sage: c = C(0); c
                [0, 0, 0]
                sage: C[0].parent()
                The fast crystal for A2 with shape [2,1]
                sage: TestSuite(c).run()
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: [v.weight() for v in crystals.FastRankTwo(['A',2], shape=[2,1])]
                [(2, 1, 0), (1, 2, 0), (1, 1, 1), (1, 0, 2), (0, 1, 2), (2, 0, 1), (1, 1, 1), (0, 2, 1)]
                sage: [v.weight() for v in crystals.FastRankTwo(['B',2], shape=[1,0])]
                [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]
                sage: [v.weight() for v in crystals.FastRankTwo(['B',2], shape=[1/2,1/2])]
                [(1/2, 1/2), (1/2, -1/2), (-1/2, 1/2), (-1/2, -1/2)]
                sage: [v.weight() for v in crystals.FastRankTwo(['C',2], shape=[1,0])]
                [(1, 0), (0, 1), (0, -1), (-1, 0)]
                sage: [v.weight() for v in crystals.FastRankTwo(['C',2], shape=[1,1])]
                [(1, 1), (1, -1), (0, 0), (-1, 1), (-1, -1)]
            """
        def __hash__(self):
            """
            TESTS::

                sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
                sage: hash(C(0))
                0
            """
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
                sage: C(1).e(1)
                [0, 0, 0]
                sage: C(0).e(1) is None
                True
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.FastRankTwo(['A',2],shape=[2,1])
                sage: C(6).f(1)
                [1, 2, 1]
                sage: C(7).f(1) is None
                True
            """
