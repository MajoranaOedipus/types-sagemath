from _typeshed import Incomplete
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CartanTypeFactory(SageObject):
    def __call__(self, *args):
        '''
        Construct a Cartan type object.

        INPUT:

        - ``[letter, rank]`` -- letter is one of \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\'
          and rank is an integer or a pair of integers

        - ``[letter, rank, twist]`` -- letter is one of \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'BC\'
          and rank and twist are integers

        - ``str`` -- string

        - ``object`` -- a Cartan type, or an object with a Cartan type method

        EXAMPLES:

        We construct the Cartan type `D_4`::

            sage: d4 = CartanType([\'D\',4])
            sage: d4
            [\'D\', 4]

        or, for short::

            sage: CartanType("D4")
            [\'D\', 4]

        .. SEEALSO:: :func:`~sage.combinat.root_system.cartan_type.CartanType`

        TESTS:

        Check that this is compatible with :class:`CartanTypeFolded`::

            sage: fct = CartanType([\'C\', 4, 1]).as_folding()
            sage: CartanType(fct)
            [\'C\', 4, 1]

        Check that :issue:`13774` is fixed::

            sage: CT = CartanType([[\'A\',2]])
            sage: CT.is_irreducible()
            True
            sage: CT.cartan_matrix()                                                    # needs sage.graphs
            [ 2 -1]
            [-1  2]
            sage: CT = CartanType([\'A2\'])
            sage: CT.is_irreducible()
            True
            sage: CartanType(\'A2\')
            [\'A\', 2]

        Check that we can pass any Cartan type as a single element list::

            sage: CT = CartanType([\'A2\', \'A2\', \'A2\'])
            sage: CartanType([CT])
            A2xA2xA2

            sage: CT = CartanType(\'A2\').relabel({1:-1, 2:-2})
            sage: CartanType([CT])
            [\'A\', 2] relabelled by {1: -1, 2: -2}

        Check the errors from :issue:`20973`::

            sage: CartanType([\'A\',-1])
            Traceback (most recent call last):
            ...
            ValueError: [\'A\', -1] is not a valid Cartan type

        Check that unicode is handled properly (:issue:`23323`)::

            sage: CartanType(u"A3")
            [\'A\', 3]
        '''
    def samples(self, finite=None, affine=None, crystallographic=None):
        """
        Return a sample of the available Cartan types.

        INPUT:

        - ``finite`` -- boolean or ``None`` (default: ``None``)

        - ``affine`` -- boolean or ``None`` (default: ``None``)

        - ``crystallographic`` -- boolean or ``None`` (default: ``None``)

        The sample contains all the exceptional finite and affine
        Cartan types, as well as typical representatives of the
        infinite families.

        EXAMPLES::

            sage: CartanType.samples()
            [['A', 1], ['A', 5], ['B', 1], ['B', 5], ['C', 1], ['C', 5], ['D', 2], ['D', 3], ['D', 5],
             ['E', 6], ['E', 7], ['E', 8], ['F', 4], ['G', 2], ['I', 5], ['H', 3], ['H', 4],
             ['A', 1, 1], ['A', 5, 1], ['B', 1, 1], ['B', 5, 1],
             ['C', 1, 1], ['C', 5, 1], ['D', 3, 1], ['D', 5, 1],
             ['E', 6, 1], ['E', 7, 1], ['E', 8, 1], ['F', 4, 1], ['G', 2, 1], ['BC', 1, 2], ['BC', 5, 2],
             ['B', 5, 1]^*, ['C', 4, 1]^*, ['F', 4, 1]^*, ['G', 2, 1]^*, ['BC', 1, 2]^*, ['BC', 5, 2]^*]

        The finite, affine and crystallographic options allow
        respectively for restricting to (non) finite, (non) affine,
        and (non) crystallographic Cartan types::

            sage: CartanType.samples(finite=True)
            [['A', 1], ['A', 5], ['B', 1], ['B', 5], ['C', 1], ['C', 5], ['D', 2], ['D', 3], ['D', 5],
             ['E', 6], ['E', 7], ['E', 8], ['F', 4], ['G', 2], ['I', 5], ['H', 3], ['H', 4]]

            sage: CartanType.samples(affine=True)
            [['A', 1, 1], ['A', 5, 1], ['B', 1, 1], ['B', 5, 1],
             ['C', 1, 1], ['C', 5, 1], ['D', 3, 1], ['D', 5, 1],
             ['E', 6, 1], ['E', 7, 1], ['E', 8, 1], ['F', 4, 1], ['G', 2, 1], ['BC', 1, 2], ['BC', 5, 2],
             ['B', 5, 1]^*, ['C', 4, 1]^*, ['F', 4, 1]^*, ['G', 2, 1]^*, ['BC', 1, 2]^*, ['BC', 5, 2]^*]

            sage: CartanType.samples(crystallographic=True)
            [['A', 1], ['A', 5], ['B', 1], ['B', 5], ['C', 1], ['C', 5], ['D', 2], ['D', 3], ['D', 5],
             ['E', 6], ['E', 7], ['E', 8], ['F', 4], ['G', 2],
             ['A', 1, 1], ['A', 5, 1], ['B', 1, 1], ['B', 5, 1],
             ['C', 1, 1], ['C', 5, 1], ['D', 3, 1], ['D', 5, 1],
             ['E', 6, 1], ['E', 7, 1], ['E', 8, 1], ['F', 4, 1], ['G', 2, 1], ['BC', 1, 2], ['BC', 5, 2],
             ['B', 5, 1]^*, ['C', 4, 1]^*, ['F', 4, 1]^*, ['G', 2, 1]^*, ['BC', 1, 2]^*, ['BC', 5, 2]^*]

            sage: CartanType.samples(crystallographic=False)
            [['I', 5], ['H', 3], ['H', 4]]

        .. TODO:: add some reducible Cartan types (suggestions?)

        TESTS::

            sage: for ct in CartanType.samples(): TestSuite(ct).run()
        """
    @classmethod
    def color(cls, i):
        """
        Default color scheme for the vertices of a Dynkin diagram (and associated objects).

        EXAMPLES::

            sage: CartanType.color(1)
            'blue'
            sage: CartanType.color(2)
            'red'
            sage: CartanType.color(3)
            'green'

        The default color is black::

            sage: CartanType.color(0)
            'black'

        Negative indices get the same color as their positive counterparts::

            sage: CartanType.color(-1)
            'blue'
            sage: CartanType.color(-2)
            'red'
            sage: CartanType.color(-3)
            'green'
        """
    class options(GlobalOptions):
        """
        Set and display the options for Cartan types. If no parameters
        are set, then the function returns a copy of the options dictionary.

        The ``options`` to partitions can be accessed as the method
        :obj:`CartanType.options` of
        :class:`CartanType <CartanTypeFactory>`.

        @OPTIONS@

        EXAMPLES::

            sage: ct = CartanType(['D',5,2]); ct
            ['C', 4, 1]^*
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O=<=O---O---O=>=O
            0   1   2   3   4
            C4~*
            sage: latex(ct)
            C_{4}^{(1)\\vee}
            sage: CartanType.options(dual_str='#', dual_latex='\\\\ast',)
            sage: ct
            ['C', 4, 1]^#
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O=<=O---O---O=>=O
            0   1   2   3   4
            C4~#
            sage: latex(ct)
            C_{4}^{(1)\\ast}
            sage: CartanType.options(notation='kac', mark_special_node='both')
            sage: ct
            ['D', 5, 2]
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            @=<=O---O---O=>=O
            0   1   2   3   4
            D5^2
            sage: latex(ct)
            D_{5}^{(2)}

        For type `A_{2n}^{(2)\\dagger}`, the dual string/latex options are
        automatically overridden::

            sage: dct = CartanType(['A',8,2]).dual(); dct
            ['A', 8, 2]^+
            sage: latex(dct)
            A_{8}^{(2)\\dagger}
            sage: dct.dynkin_diagram()                                                  # needs sage.graphs
            @=>=O---O---O=>=O
            0   1   2   3   4
            A8^2+
            sage: CartanType.options._reset()
        """
        NAME: str
        module: str
        option_class: str
        notation: Incomplete
        dual_str: Incomplete
        dual_latex: Incomplete
        mark_special_node: Incomplete
        special_node_str: Incomplete
        marked_node_str: Incomplete
        latex_relabel: Incomplete
        latex_marked: Incomplete

CartanType: Incomplete

class CartanType_abstract:
    """
    Abstract class for Cartan types

    Subclasses should implement:

    - :meth:`dynkin_diagram()`

    - :meth:`cartan_matrix()`

    - :meth:`is_finite()`

    - :meth:`is_affine()`

    - :meth:`is_irreducible()`
    """
    def type(self) -> None:
        """
        Return the type of ``self``, or ``None`` if unknown.

        This method should be overridden in any subclass.

        EXAMPLES::

            sage: from sage.combinat.root_system.cartan_type import CartanType_abstract
            sage: C = CartanType_abstract()
            sage: C.type() is None
            True
        """
    @abstract_method
    def rank(self) -> None:
        """
        Return the rank of ``self``.

        This is the number of nodes of the associated Coxeter or
        Dynkin diagram.

        EXAMPLES::

            sage: CartanType(['A', 4]).rank()
            4
            sage: CartanType(['A', 7, 2]).rank()
            5
            sage: CartanType(['I', 8]).rank()
            2
        """
    @abstract_method
    def index_set(self) -> None:
        """
        Return the index set for ``self``.

        This is the list of the nodes of the associated Coxeter or
        Dynkin diagram.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).index_set()
            (0, 1, 2, 3)
            sage: CartanType(['D', 4]).index_set()
            (1, 2, 3, 4)
            sage: CartanType(['A', 7, 2]).index_set()
            (0, 1, 2, 3, 4)
            sage: CartanType(['A', 7, 2]).index_set()
            (0, 1, 2, 3, 4)
            sage: CartanType(['A', 6, 2]).index_set()
            (0, 1, 2, 3)
            sage: CartanType(['D', 6, 2]).index_set()
            (0, 1, 2, 3, 4, 5)
            sage: CartanType(['E', 6, 1]).index_set()
            (0, 1, 2, 3, 4, 5, 6)
            sage: CartanType(['E', 6, 2]).index_set()
            (0, 1, 2, 3, 4)
            sage: CartanType(['A', 2, 2]).index_set()
            (0, 1)
            sage: CartanType(['G', 2, 1]).index_set()
            (0, 1, 2)
            sage: CartanType(['F', 4, 1]).index_set()
            (0, 1, 2, 3, 4)
        """
    def coxeter_diagram(self) -> None:
        """
        Return the Coxeter diagram for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: CartanType(['B',3]).coxeter_diagram()
            Graph on 3 vertices
            sage: CartanType(['A',3]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 3)]
            sage: CartanType(['B',3]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 4)]
            sage: CartanType(['G',2]).coxeter_diagram().edges(sort=True)
            [(1, 2, 6)]
            sage: CartanType(['F',4]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 4), (3, 4, 3)]
        """
    @cached_method
    def coxeter_matrix(self):
        """
        Return the Coxeter matrix for ``self``.

        EXAMPLES::

            sage: CartanType(['A', 4]).coxeter_matrix()                                 # needs sage.graphs
            [1 3 2 2]
            [3 1 3 2]
            [2 3 1 3]
            [2 2 3 1]
        """
    def coxeter_type(self):
        """
        Return the Coxeter type for ``self``.

        EXAMPLES::

            sage: CartanType(['A', 4]).coxeter_type()
            Coxeter type of ['A', 4]
        """
    def dual(self):
        '''
        Return the dual Cartan type, possibly just as a formal dual.

        EXAMPLES::

            sage: CartanType([\'A\',3]).dual()
            [\'A\', 3]
            sage: CartanType(["B", 3]).dual()
            [\'C\', 3]
            sage: CartanType([\'C\',2]).dual()
            [\'B\', 2]
            sage: CartanType([\'D\',4]).dual()
            [\'D\', 4]
            sage: CartanType([\'E\',8]).dual()
            [\'E\', 8]
            sage: CartanType([\'F\',4]).dual()
            [\'F\', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
        '''
    def relabel(self, relabelling):
        """
        Return a relabelled copy of this Cartan type.

        INPUT:

        - ``relabelling`` -- a function (or a list or dictionary)

        OUTPUT:

        an isomorphic Cartan type obtained by relabelling the nodes of
        the Dynkin diagram. Namely, the node with label ``i`` is
        relabelled ``f(i)`` (or, by ``f[i]`` if ``f`` is a list or
        dictionary).

        EXAMPLES::

           sage: CartanType(['F',4]).relabel({ 1:4, 2:3, 3:2, 4:1 }).dynkin_diagram()   # needs sage.graphs
           O---O=>=O---O
           4   3   2   1
           F4 relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
        """
    def subtype(self, index_set):
        """
        Return a subtype of ``self`` given by ``index_set``.

        A subtype can be considered the Dynkin diagram induced from
        the Dynkin diagram of ``self`` by ``index_set``.

        EXAMPLES::

            sage: ct = CartanType(['A',6,2])
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O=<=O---O=<=O
            0   1   2   3
            BC3~
            sage: ct.subtype([1,2,3])                                                   # needs sage.graphs
            ['C', 3]
        """
    def marked_nodes(self, marked_nodes):
        """
        Return a Cartan type with the nodes ``marked_nodes`` marked.

        INPUT:

        - ``marked_nodes`` -- list of nodes to mark

        EXAMPLES::

            sage: CartanType(['F',4]).marked_nodes([1, 3]).dynkin_diagram()             # needs sage.graphs
            X---O=>=X---O
            1   2   3   4
            F4 with nodes (1, 3) marked
        """
    def is_reducible(self):
        '''
        Report whether the root system is reducible (i.e. not simple), that
        is whether it can be factored as a product of root systems.

        EXAMPLES::

            sage: CartanType("A2xB3").is_reducible()
            True
            sage: CartanType([\'A\',2]).is_reducible()
            False
        '''
    def is_irreducible(self):
        """
        Report whether this Cartan type is irreducible (i.e. simple). This
        should be overridden in any subclass.

        This returns ``False`` by default. Derived class should override this
        appropriately.

        EXAMPLES::

            sage: from sage.combinat.root_system.cartan_type import CartanType_abstract
            sage: C = CartanType_abstract()
            sage: C.is_irreducible()
            False
        """
    def is_atomic(self):
        '''
        This method is usually equivalent to :meth:`is_reducible`,
        except for the Cartan type `D_2`.

        `D_2` is not a standard Cartan type. It is equivalent to type
        `A_1 \\times A_1` which is reducible; however the isomorphism
        from its ambient space (for the orthogonal group of degree 4)
        to that of `A_1 \\times A_1` is non trivial, and it is useful to
        have it.

        From a programming point of view its implementation is more
        similar to the irreducible types, and so the method
        :meth:`is_atomic()` is supplied.

        EXAMPLES::

            sage: CartanType("D2").is_atomic()
            True
            sage: CartanType("D2").is_irreducible()
            False

        TESTS::

            sage: all( T.is_irreducible() == T.is_atomic() for T in CartanType.samples() if T != CartanType("D2"))
            True
        '''
    def is_compound(self):
        """
        A short hand for not :meth:`is_atomic`.

        TESTS::

            sage: all( T.is_compound() == (not T.is_atomic()) for T in CartanType.samples())
            True
        """
    @abstract_method
    def is_finite(self) -> None:
        """
        Return whether this Cartan type is finite.

        EXAMPLES::

            sage: from sage.combinat.root_system.cartan_type import CartanType_abstract
            sage: C = CartanType_abstract()
            sage: C.is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method is_finite at ...>

        ::

            sage: CartanType(['A',4]).is_finite()
            True
            sage: CartanType(['A',4, 1]).is_finite()
            False
        """
    @abstract_method
    def is_affine(self) -> None:
        """
        Return whether ``self`` is affine.

        EXAMPLES::

            sage: CartanType(['A', 3]).is_affine()
            False
            sage: CartanType(['A', 3, 1]).is_affine()
            True
        """
    def is_crystallographic(self):
        """
        Return whether this Cartan type is crystallographic.

        This returns ``False`` by default. Derived class should override this
        appropriately.

        EXAMPLES::

            sage: [ [t, t.is_crystallographic() ] for t in CartanType.samples(finite=True) ]
            [[['A', 1], True], [['A', 5], True],
             [['B', 1], True], [['B', 5], True],
             [['C', 1], True], [['C', 5], True],
             [['D', 2], True], [['D', 3], True], [['D', 5], True],
             [['E', 6], True], [['E', 7], True], [['E', 8], True],
             [['F', 4], True], [['G', 2], True],
             [['I', 5], False], [['H', 3], False], [['H', 4], False]]
        """
    def is_simply_laced(self):
        """
        Return whether this Cartan type is simply laced.

        This returns ``False`` by default. Derived class should override this
        appropriately.

        EXAMPLES::

            sage: [ [t, t.is_simply_laced() ] for t in CartanType.samples() ]
            [[['A', 1], True], [['A', 5], True],
             [['B', 1], True], [['B', 5], False],
             [['C', 1], True], [['C', 5], False],
             [['D', 2], True], [['D', 3], True], [['D', 5], True],
             [['E', 6], True], [['E', 7], True], [['E', 8], True],
             [['F', 4], False], [['G', 2], False], [['I', 5], False],
             [['H', 3], False], [['H', 4], False],
             [['A', 1, 1], False], [['A', 5, 1], True],
             [['B', 1, 1], False], [['B', 5, 1], False],
             [['C', 1, 1], False], [['C', 5, 1], False],
             [['D', 3, 1], True], [['D', 5, 1], True],
             [['E', 6, 1], True], [['E', 7, 1], True], [['E', 8, 1], True],
             [['F', 4, 1], False], [['G', 2, 1], False],
             [['BC', 1, 2], False], [['BC', 5, 2], False],
             [['B', 5, 1]^*, False], [['C', 4, 1]^*, False],
             [['F', 4, 1]^*, False], [['G', 2, 1]^*, False],
             [['BC', 1, 2]^*, False], [['BC', 5, 2]^*, False]]
        """
    def is_implemented(self):
        '''
        Check whether the Cartan datum for ``self`` is actually implemented.

        EXAMPLES::

            sage: CartanType(["A",4,1]).is_implemented()                                # needs sage.graphs
            True
            sage: CartanType([\'H\',3]).is_implemented()
            True
        '''
    def root_system(self):
        """
        Return the root system associated to ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).root_system()
            Root system of type ['A', 4]
        """
    def as_folding(self, folding_of=None, sigma=None):
        """
        Return ``self`` realized as a folded Cartan type.

        For finite and affine types, this is realized by the Dynkin
        diagram foldings:

        .. MATH::

            \\begin{array}{ccl}
            C_n^{(1)}, A_{2n}^{(2)}, A_{2n}^{(2)\\dagger}, D_{n+1}^{(2)}
            & \\hookrightarrow & A_{2n-1}^{(1)}, \\\\\n            A_{2n-1}^{(2)}, B_n^{(1)} & \\hookrightarrow & D_{n+1}^{(1)}, \\\\\n            E_6^{(2)}, F_4^{(1)} & \\hookrightarrow & E_6^{(1)}, \\\\\n            D_4^{(3)}, G_2^{(1)} & \\hookrightarrow & D_4^{(1)}, \\\\\n            C_n & \\hookrightarrow & A_{2n-1}, \\\\\n            B_n & \\hookrightarrow & D_{n+1}, \\\\\n            F_4 & \\hookrightarrow & E_6, \\\\\n            G_2 & \\hookrightarrow & D_4.
            \\end{array}

        For general types, this returns ``self`` as a folded type of ``self``
        with `\\sigma` as the identity map.

        For more information on these foldings and folded Cartan types, see
        :class:`sage.combinat.root_system.type_folded.CartanTypeFolded`.

        If the optional inputs ``folding_of`` and ``sigma`` are specified, then
        this returns the folded Cartan type of ``self`` in ``folding_of`` given
        by the automorphism ``sigma``.

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).as_folding()
            ['B', 3, 1] as a folding of  ['D', 4, 1]
            sage: CartanType(['F', 4]).as_folding()
            ['F', 4] as a folding of  ['E', 6]
            sage: CartanType(['BC', 3, 2]).as_folding()
            ['BC', 3, 2] as a folding of  ['A', 5, 1]
            sage: CartanType(['D', 4, 3]).as_folding()
            ['G', 2, 1]^* relabelled by {0: 0, 1: 2, 2: 1} as a folding of ['D', 4, 1]
        """
    options: Incomplete

class CartanType_crystallographic(CartanType_abstract):
    """
    An abstract class for crystallographic Cartan types.
    """
    def ascii_art(self, label: str = 'lambda x: x', node=None) -> None:
        """
        Return an ascii art representation of the Dynkin diagram.

        INPUT:

        - ``label`` -- (default: the identity) a relabeling function
          for the nodes
        - ``node`` -- (optional) a function which returns
          the character for a node

        EXAMPLES::

            sage: cartan_type = CartanType(['B',5,1])
            sage: print(cartan_type.ascii_art())
                O 0
                |
                |
            O---O---O---O=>=O
            1   2   3   4   5

        The label option is useful to visualize various statistics on
        the nodes of the Dynkin diagram::

            sage: a = cartan_type.col_annihilator(); a                                  # needs sage.graphs
            Finite family {0: 1, 1: 1, 2: 2, 3: 2, 4: 2, 5: 2}
            sage: print(CartanType(['B',5,1]).ascii_art(label=a.__getitem__))           # needs sage.graphs
                O 1
                |
                |
            O---O---O---O=>=O
            1   2   2   2   2
        """
    @abstract_method
    def dynkin_diagram(self) -> None:
        """
        Return the Dynkin diagram associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).dynkin_diagram()                                  # needs sage.graphs
            O---O---O---O
            1   2   3   4
            A4

        .. NOTE::

            Derived subclasses should typically implement this as a cached
            method.
        """
    @cached_method
    def cartan_matrix(self):
        """
        Return the Cartan matrix associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).cartan_matrix()                                   # needs sage.graphs
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -1]
            [ 0  0 -1  2]
        """
    def coxeter_diagram(self):
        """
        Return the Coxeter diagram for ``self``.

        This implementation constructs it from the Dynkin diagram.

        .. SEEALSO:: :meth:`CartanType_abstract.coxeter_diagram`

        EXAMPLES::

            sage: # needs sage.graphs
            sage: CartanType(['A',3]).coxeter_diagram()
            Graph on 3 vertices
            sage: CartanType(['A',3]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 3)]
            sage: CartanType(['B',3]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 4)]
            sage: CartanType(['G',2]).coxeter_diagram().edges(sort=True)
            [(1, 2, 6)]
            sage: CartanType(['F',4]).coxeter_diagram().edges(sort=True)
            [(1, 2, 3), (2, 3, 4), (3, 4, 3)]
            sage: CartanType(['A',2,2]).coxeter_diagram().edges(sort=True)
            [(0, 1, +Infinity)]
        """
    def is_crystallographic(self):
        """
        Implement :meth:`CartanType_abstract.is_crystallographic`
        by returning ``True``.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).is_crystallographic()
            True
        """
    @cached_method
    def symmetrizer(self):
        '''
        Return the symmetrizer of the Cartan matrix of ``self``.

        A Cartan matrix `M` is symmetrizable if there exists a non
        trivial diagonal matrix `D` such that `DM` is a symmetric
        matrix, that is `DM = M^tD`. In that case, `D` is unique, up
        to a scalar factor for each connected component of the Dynkin
        diagram.

        This method computes the unique minimal such `D` with positive
        integral coefficients. If `D` exists, it is returned as a
        family. Otherwise ``None`` is returned.

        The coefficients are coerced to ``base_ring``.

        EXAMPLES::

            sage: CartanType(["B",5]).symmetrizer()                                     # needs sage.graphs
            Finite family {1: 2, 2: 2, 3: 2, 4: 2, 5: 1}

        Here is a neat trick to visualize it better::

            sage: T = CartanType(["B",5])
            sage: print(T.ascii_art(T.symmetrizer().__getitem__))                       # needs sage.graphs
            O---O---O---O=>=O
            2   2   2   2   1

            sage: T = CartanType(["BC",5, 2])
            sage: print(T.ascii_art(T.symmetrizer().__getitem__))                       # needs sage.graphs
            O=<=O---O---O---O=<=O
            1   2   2   2   2   4

        Here is the symmetrizer of some reducible Cartan types::

            sage: T = CartanType(["D", 2])
            sage: print(T.ascii_art(T.symmetrizer().__getitem__))                       # needs sage.graphs
            O   O
            1   1

            sage: T = CartanType(["B",5],["BC",5, 2])
            sage: print(T.ascii_art(T.symmetrizer().__getitem__))                       # needs sage.graphs
            O---O---O---O=>=O
            2   2   2   2   1
            O=<=O---O---O---O=<=O
            1   2   2   2   2   4

        Property: up to an overall scalar factor, this gives the norm
        of the simple roots in the ambient space::

            sage: T = CartanType(["C",5])
            sage: print(T.ascii_art(T.symmetrizer().__getitem__))                       # needs sage.graphs
            O---O---O---O=<=O
            1   1   1   1   2

            sage: alpha = RootSystem(T).ambient_space().simple_roots()
            sage: print(T.ascii_art(lambda i: alpha[i].scalar(alpha[i])))
            O---O---O---O=<=O
            2   2   2   2   4
        '''
    def index_set_bipartition(self):
        """
        Return a bipartition `\\{L,R\\}` of the vertices of the Dynkin diagram.

        For `i` and `j` both in `L` (or both in `R`), the simple
        reflections `s_i` and `s_j` commute.

        Of course, the Dynkin diagram should be bipartite. This is
        always the case for all finite types.

        EXAMPLES::

            sage: CartanType(['A',5]).index_set_bipartition()                           # needs sage.graphs
            ({1, 3, 5}, {2, 4})

            sage: CartanType(['A',2,1]).index_set_bipartition()                         # needs sage.graphs
            Traceback (most recent call last):
            ...
            ValueError: the Dynkin diagram must be bipartite
        """

class CartanType_simply_laced(CartanType_crystallographic):
    """
    An abstract class for simply laced Cartan types.
    """
    def is_simply_laced(self):
        """
        Return whether ``self`` is simply laced, which is ``True``.

        EXAMPLES::

            sage: CartanType(['A',3,1]).is_simply_laced()
            True
            sage: CartanType(['A',2]).is_simply_laced()
            True
        """
    def dual(self):
        '''
        Simply laced Cartan types are self-dual, so return ``self``.

        EXAMPLES::

            sage: CartanType(["A", 3]).dual()
            [\'A\', 3]
            sage: CartanType(["A", 3, 1]).dual()
            [\'A\', 3, 1]
            sage: CartanType(["D", 3]).dual()
            [\'D\', 3]
            sage: CartanType(["D", 4, 1]).dual()
            [\'D\', 4, 1]
            sage: CartanType(["E", 6]).dual()
            [\'E\', 6]
            sage: CartanType(["E", 6, 1]).dual()
            [\'E\', 6, 1]
        '''

class CartanType_simple(CartanType_abstract):
    """
    An abstract class for simple Cartan types.
    """
    def is_irreducible(self):
        """
        Return whether ``self`` is irreducible, which is ``True``.

        EXAMPLES::

            sage: CartanType(['A', 3]).is_irreducible()
            True
        """

class CartanType_finite(CartanType_abstract):
    """
    An abstract class for simple affine Cartan types.
    """
    def is_finite(self):
        '''
        EXAMPLES::

            sage: CartanType(["A", 3]).is_finite()
            True
        '''
    def is_affine(self):
        '''
        EXAMPLES::

            sage: CartanType(["A", 3]).is_affine()
            False
        '''

class CartanType_affine(CartanType_simple, CartanType_crystallographic):
    """
    An abstract class for simple affine Cartan types
    """
    AmbientSpace: Incomplete
    def is_finite(self):
        """
        EXAMPLES::

            sage: CartanType(['A', 3, 1]).is_finite()
            False
        """
    def is_affine(self):
        """
        EXAMPLES::

            sage: CartanType(['A', 3, 1]).is_affine()
            True
        """
    def is_untwisted_affine(self):
        """
        Return whether ``self`` is untwisted affine.

        A Cartan type is untwisted affine if it is the canonical
        affine extension of some finite type. Every affine type is
        either untwisted affine, dual thereof, or of type ``BC``.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).is_untwisted_affine()
            True
            sage: CartanType(['A', 3, 1]).dual().is_untwisted_affine()  # this one is self dual!
            True
            sage: CartanType(['B', 3, 1]).dual().is_untwisted_affine()
            False
            sage: CartanType(['BC', 3, 2]).is_untwisted_affine()
            False
        """
    @abstract_method
    def special_node(self) -> None:
        """
        Return a special node of the Dynkin diagram.

        A *special* node is a node of the Dynkin diagram such that
        pruning it yields a Dynkin diagram for the associated
        classical type (see :meth:`classical`).

        This method returns the label of some special node. This is
        usually `0` in the standard conventions.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).special_node()
            0

        The choice is guaranteed to be consistent with the indexing of
        the nodes of the classical Dynkin diagram::

            sage: CartanType(['A', 3, 1]).index_set()
            (0, 1, 2, 3)
            sage: CartanType(['A', 3, 1]).classical().index_set()
            (1, 2, 3)
        """
    @cached_method
    def special_nodes(self):
        """
        Return the set of special nodes of the affine Dynkin diagram.

        EXAMPLES::

            sage: # needs sage.graphs sage.groups
            sage: CartanType(['A',3,1]).special_nodes()
            (0, 1, 2, 3)
            sage: CartanType(['C',2,1]).special_nodes()
            (0, 2)
            sage: CartanType(['D',4,1]).special_nodes()
            (0, 1, 3, 4)
            sage: CartanType(['E',6,1]).special_nodes()
            (0, 1, 6)
            sage: CartanType(['D',3,2]).special_nodes()
            (0, 2)
            sage: CartanType(['A',4,2]).special_nodes()
            (0,)
        """
    @abstract_method
    def classical(self) -> None:
        """
        Return the classical Cartan type associated with this affine Cartan type.

        EXAMPLES::

            sage: CartanType(['A', 1, 1]).classical()
            ['A', 1]
            sage: CartanType(['A', 3, 1]).classical()
            ['A', 3]
            sage: CartanType(['B', 3, 1]).classical()
            ['B', 3]

            sage: CartanType(['A', 2, 2]).classical()
            ['C', 1]
            sage: CartanType(['BC', 1, 2]).classical()
            ['C', 1]
            sage: CartanType(['A', 4, 2]).classical()
            ['C', 2]
            sage: CartanType(['BC', 2, 2]).classical()
            ['C', 2]
            sage: CartanType(['A', 10, 2]).classical()
            ['C', 5]
            sage: CartanType(['BC', 5, 2]).classical()
            ['C', 5]

            sage: CartanType(['D', 5, 2]).classical()
            ['B', 4]
            sage: CartanType(['E', 6, 1]).classical()
            ['E', 6]
            sage: CartanType(['G', 2, 1]).classical()
            ['G', 2]
            sage: CartanType(['E', 6, 2]).classical()
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: CartanType(['D', 4, 3]).classical()
            ['G', 2]

        We check that :meth:`classical`,
        :meth:`sage.combinat.root_system.cartan_type.CartanType_crystallographic.dynkin_diagram`,
        and :meth:`special_node` are consistent::

            sage: for ct in CartanType.samples(affine=True):                            # needs sage.graphs
            ....:     g1 = ct.classical().dynkin_diagram()
            ....:     g2 = ct.dynkin_diagram()
            ....:     g2.delete_vertex(ct.special_node())
            ....:     assert g1.vertices(sort=True) == g2.vertices(sort=True)
            ....:     assert g1.edges(sort=True) == g2.edges(sort=True)
        """
    @abstract_method
    def basic_untwisted(self) -> None:
        """
        Return the basic untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic untwisted type is `X_n`.
        In other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: CartanType(['A', 1, 1]).basic_untwisted()
            ['A', 1]
            sage: CartanType(['A', 3, 1]).basic_untwisted()
            ['A', 3]
            sage: CartanType(['B', 3, 1]).basic_untwisted()
            ['B', 3]
            sage: CartanType(['E', 6, 1]).basic_untwisted()
            ['E', 6]
            sage: CartanType(['G', 2, 1]).basic_untwisted()
            ['G', 2]

            sage: CartanType(['A', 2, 2]).basic_untwisted()
            ['A', 2]
            sage: CartanType(['A', 4, 2]).basic_untwisted()
            ['A', 4]
            sage: CartanType(['A', 11, 2]).basic_untwisted()
            ['A', 11]
            sage: CartanType(['D', 5, 2]).basic_untwisted()
            ['D', 5]
            sage: CartanType(['E', 6, 2]).basic_untwisted()
            ['E', 6]
            sage: CartanType(['D', 4, 3]).basic_untwisted()
            ['D', 4]
        """
    def row_annihilator(self, m=None):
        """
        Return the unique minimal non trivial annihilating linear
        combination of `\\alpha_0, \\alpha_1, \\ldots, \\alpha_n` with
        nonnegative coefficients (or alternatively, the unique minimal
        non trivial annihilating linear combination of the rows of the
        Cartan matrix with nonnegative coefficients).

        Throw an error if the existence of uniqueness does not hold

        The optional argument ``m`` is for internal use only.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: RootSystem(['C',2,1]).cartan_type().acheck()
            Finite family {0: 1, 1: 1, 2: 1}
            sage: RootSystem(['D',4,1]).cartan_type().acheck()
            Finite family {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}
            sage: RootSystem(['F',4,1]).cartan_type().acheck()
            Finite family {0: 1, 1: 2, 2: 3, 3: 2, 4: 1}
            sage: RootSystem(['BC',4,2]).cartan_type().acheck()
            Finite family {0: 1, 1: 2, 2: 2, 3: 2, 4: 2}

        ``acheck`` is a shortcut for row_annihilator::

            sage: RootSystem(['BC',4,2]).cartan_type().row_annihilator()                # needs sage.graphs
            Finite family {0: 1, 1: 2, 2: 2, 3: 2, 4: 2}

        FIXME:

        - The current implementation assumes that the Cartan matrix
          is indexed by `[0,1,...]`, in the same order as the index set.
        - This really should be a method of :class:`CartanMatrix`.
        """
    acheck = row_annihilator
    def col_annihilator(self):
        """
        Return the unique minimal non trivial annihilating linear
        combination of `\\alpha^\\vee_0, \\alpha^\\vee, \\ldots, \\alpha^\\vee` with
        nonnegative coefficients (or alternatively, the unique minimal
        non trivial annihilating linear combination of the columns of the
        Cartan matrix with nonnegative coefficients).

        Throw an error if the existence or uniqueness does not hold

        FIXME: the current implementation assumes that the Cartan
        matrix is indexed by `[0,1,...]`, in the same order as the
        index set.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: RootSystem(['C',2,1]).cartan_type().a()
            Finite family {0: 1, 1: 2, 2: 1}
            sage: RootSystem(['D',4,1]).cartan_type().a()
            Finite family {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}
            sage: RootSystem(['F',4,1]).cartan_type().a()
            Finite family {0: 1, 1: 2, 2: 3, 3: 4, 4: 2}
            sage: RootSystem(['BC',4,2]).cartan_type().a()
            Finite family {0: 2, 1: 2, 2: 2, 3: 2, 4: 1}

        ``a`` is a shortcut for col_annihilator::

            sage: RootSystem(['BC',4,2]).cartan_type().col_annihilator()                # needs sage.graphs
            Finite family {0: 2, 1: 2, 2: 2, 3: 2, 4: 1}
        """
    a = col_annihilator
    def c(self):
        '''
        Return the family (c_i)_i of integer coefficients defined by
        `c_i=max(1, a_i/a^vee_i)` (see e.g. [FSS07]_ p. 3)

        FIXME: the current implementation assumes that the Cartan
        matrix is indexed by `[0,1,...]`, in the same order as the
        index set.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: RootSystem([\'C\',2,1]).cartan_type().c()
            Finite family {0: 1, 1: 2, 2: 1}
            sage: RootSystem([\'D\',4,1]).cartan_type().c()
            Finite family {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
            sage: RootSystem([\'F\',4,1]).cartan_type().c()
            Finite family {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: RootSystem([\'BC\',4,2]).cartan_type().c()
            Finite family {0: 2, 1: 1, 2: 1, 3: 1, 4: 1}

        TESTS::

            sage: CartanType(["B", 3, 1]).c().map(parent)                               # needs sage.graphs
            Finite family {0: Integer Ring, 1: Integer Ring, 2: Integer Ring, 3: Integer Ring}

        REFERENCES:

        .. [FSS07] \\G. Fourier, A. Schilling, and M. Shimozono,
           *Demazure structure inside Kirillov-Reshetikhin crystals*,
           J. Algebra, Vol. 309, (2007), p. 386-404
           :arxiv:`math/0605451`
        '''
    def translation_factors(self):
        '''
        Return the translation factors for ``self``.

        Those are the smallest factors `t_i` such that the translation
        by `t_i \\alpha_i` maps the fundamental polygon to another
        polygon in the alcove picture.

        OUTPUT:

        a dictionary from ``self.index_set()`` to `\\ZZ`
        (or `\\QQ` for affine type `BC`)

        Those coefficients are all `1` for dual untwisted, and in
        particular for simply laced. They coincide with the usual
        `c_i` coefficients (see :meth:`c`) for untwisted and dual
        thereof. See the discussion below for affine type `BC`.

        .. NOTE::

            One usually realizes the alcove picture in the coweight
            lattice, with translations by coroots; in that case, one will
            use the translation factors for the dual Cartan type.

        FIXME: the current implementation assumes that the Cartan
        matrix is indexed by `[0,1,...]`, in the same order as the
        index set.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: CartanType([\'C\',2,1]).translation_factors()
            Finite family {0: 1, 1: 2, 2: 1}
            sage: CartanType([\'C\',2,1]).dual().translation_factors()
            Finite family {0: 1, 1: 1, 2: 1}
            sage: CartanType([\'D\',4,1]).translation_factors()
            Finite family {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
            sage: CartanType([\'F\',4,1]).translation_factors()
            Finite family {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
            sage: CartanType([\'BC\',4,2]).translation_factors()
            Finite family {0: 1, 1: 1, 2: 1, 3: 1, 4: 1/2}

        We proceed with systematic tests taken from MuPAD-Combinat\'s
        testsuite::

            sage: # needs sage.graphs
            sage: list(CartanType(["A", 1, 1]).translation_factors())
            [1, 1]
            sage: list(CartanType(["A", 5, 1]).translation_factors())
            [1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["B", 5, 1]).translation_factors())
            [1, 1, 1, 1, 1, 2]
            sage: list(CartanType(["C", 5, 1]).translation_factors())
            [1, 2, 2, 2, 2, 1]
            sage: list(CartanType(["D", 5, 1]).translation_factors())
            [1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["E", 6, 1]).translation_factors())
            [1, 1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["E", 7, 1]).translation_factors())
            [1, 1, 1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["E", 8, 1]).translation_factors())
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["F", 4, 1]).translation_factors())
            [1, 1, 1, 2, 2]
            sage: list(CartanType(["G", 2, 1]).translation_factors())
            [1, 3, 1]
            sage: list(CartanType(["A", 2, 2]).translation_factors())
            [1, 1/2]
            sage: list(CartanType(["A", 2, 2]).dual().translation_factors())
            [1/2, 1]
            sage: list(CartanType(["A", 10, 2]).translation_factors())
            [1, 1, 1, 1, 1, 1/2]
            sage: list(CartanType(["A", 10, 2]).dual().translation_factors())
            [1/2, 1, 1, 1, 1, 1]
            sage: list(CartanType(["A", 9, 2]).translation_factors())
            [1, 1, 1, 1, 1, 1]
            sage: list(CartanType(["D", 5, 2]).translation_factors())
            [1, 1, 1, 1, 1]
            sage: list(CartanType(["D", 4, 3]).translation_factors())
            [1, 1, 1]
            sage: list(CartanType(["E", 6, 2]).translation_factors())
            [1, 1, 1, 1, 1]

        We conclude with a discussion of the appropriate value for
        affine type `BC`. Let us consider the alcove picture realized
        in the weight lattice. It is obtained by taking the level-`1`
        affine hyperplane in the weight lattice, and projecting it
        along `\\Lambda_0`::

            sage: R = RootSystem(["BC",2,2])
            sage: alpha = R.weight_space().simple_roots()                               # needs sage.graphs
            sage: alphacheck = R.coroot_space().simple_roots()
            sage: Lambda = R.weight_space().fundamental_weights()

        Here are the levels of the fundamental weights::

            sage: Lambda[0].level(), Lambda[1].level(), Lambda[2].level()               # needs sage.graphs
            (1, 2, 2)

        So the "center" of the fundamental polygon at level `1` is::

            sage: O = Lambda[0]
            sage: O.level()                                                             # needs sage.graphs
            1

        We take the projection `\\omega_1` at level `0` of `\\Lambda_1`
        as unit vector on the `x`-axis, and the projection `\\omega_2`
        at level 0 of `\\Lambda_2` as unit vector of the `y`-axis::

            sage: omega1 = Lambda[1] - 2*Lambda[0]
            sage: omega2 = Lambda[2] - 2*Lambda[0]
            sage: omega1.level(), omega2.level()                                        # needs sage.graphs
            (0, 0)

        The projections of the simple roots can be read off::

            sage: alpha[0]                                                              # needs sage.graphs
            2*Lambda[0] - Lambda[1]
            sage: alpha[1]                                                              # needs sage.graphs
            -2*Lambda[0] + 2*Lambda[1] - Lambda[2]
            sage: alpha[2]                                                              # needs sage.graphs
            -2*Lambda[1] + 2*Lambda[2]

        Namely `\\alpha_0 = -\\omega_1`, `\\alpha_1 = 2\\omega_1 -
        \\omega_2` and `\\alpha_2 = -2 \\omega_1 + 2 \\omega_2`.

        The reflection hyperplane defined by `\\alpha_0^\\vee` goes
        through the points `O+1/2 \\omega_1` and `O+1/2 \\omega_2`::

            sage: (O+(1/2)*omega1).scalar(alphacheck[0])
            0
            sage: (O+(1/2)*omega2).scalar(alphacheck[0])
            0

        Hence, the fundamental alcove is the triangle `(O, O+1/2
        \\omega_1, O+1/2 \\omega_2)`. By successive reflections, one can
        tile the full plane. This induces a tiling of the full plane
        by translates of the fundamental polygon.

        .. TODO::

            Add the picture here, once root system plots in the
            weight lattice will be implemented. In the mean time, the
            reader may look up the dual picture on Figure 2 of [HST09]_
            which was produced by MuPAD-Combinat.

        From this picture, one can read that translations by
        `\\alpha_0`, `\\alpha_1`, and `1/2\\alpha_2` map the fundamental
        polygon to translates of it in the alcove picture, and are
        smallest with this property. Hence, the translation factors
        for affine type `BC` are `t_0=1, t_1=1, t_2=1/2`::

            sage: CartanType([\'BC\',2,2]).translation_factors()                          # needs sage.graphs
            Finite family {0: 1, 1: 1, 2: 1/2}

        TESTS::

            sage: CartanType(["B", 3, 1]).translation_factors().map(parent)             # needs sage.graphs
            Finite family {0: Integer Ring, 1: Integer Ring, 2: Integer Ring, 3: Integer Ring}
            sage: CartanType(["BC", 3, 2]).translation_factors().map(parent)            # needs sage.graphs
            Finite family {0: Integer Ring, 1: Integer Ring, 2: Integer Ring, 3: Rational Field}

        REFERENCES:

        .. [HST09] \\F. Hivert, A. Schilling, and N. M. Thiéry,
           *Hecke group algebras as quotients of affine Hecke
           algebras at level 0*, JCT A, Vol. 116, (2009) p. 844-863
           :arxiv:`0804.3781`
        '''
    def other_affinization(self):
        '''
        Return the other affinization of the same classical type.

        EXAMPLES::

            sage: CartanType(["A", 3, 1]).other_affinization()
            [\'A\', 3, 1]
            sage: CartanType(["B", 3, 1]).other_affinization()
            [\'C\', 3, 1]^*
            sage: CartanType(["C", 3, 1]).dual().other_affinization()
            [\'B\', 3, 1]

        Is this what we want?::

            sage: CartanType(["BC", 3, 2]).dual().other_affinization()
            [\'B\', 3, 1]
        '''

class CartanType_standard(UniqueRepresentation, SageObject):
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: len(CartanType(['A',4]))
            2
            sage: len(CartanType(['A',4,1]))
            3
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: t = CartanType(['B', 3])
            sage: t[0]
            'B'
            sage: t[1]
            3
            sage: t[2]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """

class CartanType_standard_finite(CartanType_standard, CartanType_finite):
    """
    A concrete base class for the finite standard Cartan types.

    This includes for example `A_3`, `D_4`, or `E_8`.

     TESTS::

         sage: ct1 = CartanType(['A',4])
         sage: ct2 = CartanType(['A',4])
         sage: ct3 = CartanType(['A',5])
         sage: ct1 == ct2
         True
         sage: ct1 != ct3
         True
    """
    letter: Incomplete
    n: Incomplete
    def __init__(self, letter, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['A',4])

        TESTS::

            sage: TestSuite(ct).run(verbose = True)
            running ._test_category() . . . pass
            running ._test_new() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . pass
        """
    def __reduce__(self):
        """
        TESTS::

            sage: T = CartanType(['D', 4])
            sage: T.__reduce__()
            (CartanType, ('D', 4))
            sage: T == loads(dumps(T))
            True
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['A',2])
            sage: hash(ct) #random
            -5684143898951441983
        """
    def index_set(self):
        """
        Implement :meth:`CartanType_abstract.index_set`.

        The index set for all standard finite Cartan types is of the form
        `\\{1, \\ldots, n\\}`. (See :mod:`~sage.combinat.root_system.type_I`
        for a slight abuse of this).

        EXAMPLES::

            sage: CartanType(['A', 5]).index_set()
            (1, 2, 3, 4, 5)
        """
    def rank(self):
        """
        Return the rank of ``self`` which for type `X_n` is `n`.

        EXAMPLES::

            sage: CartanType(['A', 3]).rank()
            3
            sage: CartanType(['B', 3]).rank()
            3
            sage: CartanType(['C', 3]).rank()
            3
            sage: CartanType(['D', 4]).rank()
            4
            sage: CartanType(['E', 6]).rank()
            6
        """
    def affine(self):
        """
        Return the corresponding untwisted affine Cartan type.

        EXAMPLES::

            sage: CartanType(['A',3]).affine()
            ['A', 3, 1]
        """
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        The Coxeter number is the order of a Coxeter element of the
        corresponding Weyl group.

        See Bourbaki, Lie Groups and Lie Algebras V.6.1 or
        :wikipedia:`Coxeter_element` for more information.

        EXAMPLES::

            sage: CartanType(['A',4]).coxeter_number()
            5
            sage: CartanType(['B',4]).coxeter_number()
            8
            sage: CartanType(['C',4]).coxeter_number()
            8
        """
    def dual_coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).dual_coxeter_number()
            5
            sage: CartanType(['B',4]).dual_coxeter_number()
            7
            sage: CartanType(['C',4]).dual_coxeter_number()
            5
        """
    def type(self):
        """
        Return the type of ``self``.

        EXAMPLES::

            sage: CartanType(['A', 4]).type()
            'A'
            sage: CartanType(['A', 4, 1]).type()
            'A'
        """
    @cached_method
    def opposition_automorphism(self):
        """
        Return the opposition automorphism.

        The *opposition automorphism* is the automorphism
        `i \\mapsto i^*` of the vertices Dynkin diagram such that,
        for `w_0` the longest element of the Weyl group, and any
        simple root `\\alpha_i`, one has `\\alpha_{i^*} = -w_0(\\alpha_i)`.

        The automorphism is returned as a :class:`Family`.

        EXAMPLES::

            sage: ct = CartanType(['A', 5])
            sage: ct.opposition_automorphism()                                          # needs sage.libs.gap
            Finite family {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

            sage: ct = CartanType(['D', 4])
            sage: ct.opposition_automorphism()                                          # needs sage.libs.gap
            Finite family {1: 1, 2: 2, 3: 3, 4: 4}

            sage: ct = CartanType(['D', 5])
            sage: ct.opposition_automorphism()                                          # needs sage.libs.gap
            Finite family {1: 1, 2: 2, 3: 3, 4: 5, 5: 4}

            sage: ct = CartanType(['C', 4])
            sage: ct.opposition_automorphism()                                          # needs sage.libs.gap
            Finite family {1: 1, 2: 2, 3: 3, 4: 4}
        """

class CartanType_standard_affine(CartanType_standard, CartanType_affine):
    """
    A concrete class for affine simple Cartan types.
    """
    letter: Incomplete
    n: Incomplete
    affine: Incomplete
    def __init__(self, letter, n, affine: int = 1) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['A',4,1])
            sage: TestSuite(ct).run()

        TESTS::

            sage: ct1 = CartanType(['A',3, 1])
            sage: ct2 = CartanType(['B',3, 1])
            sage: ct3 = CartanType(['A',3])
            sage: ct1 == ct1
            True
            sage: ct1 == ct2
            False
            sage: ct1 == ct3
            False
        """
    def __reduce__(self):
        """
        TESTS::

            sage: T = CartanType(['D', 4, 1])
            sage: T.__reduce__()
            (CartanType, ('D', 4, 1))
            sage: T == loads(dumps(T))
            True
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: t = CartanType(['A', 3, 1])
            sage: t[0]
            'A'
            sage: t[1]
            3
            sage: t[2]
            1
            sage: t[3]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """
    def rank(self):
        """
        Return the rank of ``self`` which for type `X_n^{(1)}` is `n + 1`.

        EXAMPLES::

            sage: CartanType(['A', 4, 1]).rank()
            5
            sage: CartanType(['B', 4, 1]).rank()
            5
            sage: CartanType(['C', 3, 1]).rank()
            4
            sage: CartanType(['D', 4, 1]).rank()
            5
            sage: CartanType(['E', 6, 1]).rank()
            7
            sage: CartanType(['E', 7, 1]).rank()
            8
            sage: CartanType(['F', 4, 1]).rank()
            5
            sage: CartanType(['G', 2, 1]).rank()
            3
            sage: CartanType(['A', 2, 2]).rank()
            2
            sage: CartanType(['A', 6, 2]).rank()
            4
            sage: CartanType(['A', 7, 2]).rank()
            5
            sage: CartanType(['D', 5, 2]).rank()
            5
            sage: CartanType(['E', 6, 2]).rank()
            5
            sage: CartanType(['D', 4, 3]).rank()
            3
        """
    def index_set(self):
        """
        Implement :meth:`CartanType_abstract.index_set`.

        The index set for all standard affine Cartan types is of the form
        `\\{0, \\ldots, n\\}`.

        EXAMPLES::

            sage: CartanType(['A', 5, 1]).index_set()
            (0, 1, 2, 3, 4, 5)
        """
    def special_node(self):
        """
        Implement :meth:`CartanType_abstract.special_node`.

        With the standard labelling conventions, `0` is always a
        special node.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).special_node()
            0
        """
    def type(self):
        """
        Return the type of ``self``.

        EXAMPLES::

            sage: CartanType(['A', 4, 1]).type()
            'A'
        """

class CartanType_standard_untwisted_affine(CartanType_standard_affine):
    """
    A concrete class for the standard untwisted affine Cartan types.
    """
    def classical(self):
        """
        Return the classical Cartan type associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A', 3, 1]).classical()
            ['A', 3]
            sage: CartanType(['B', 3, 1]).classical()
            ['B', 3]
            sage: CartanType(['C', 3, 1]).classical()
            ['C', 3]
            sage: CartanType(['D', 4, 1]).classical()
            ['D', 4]
            sage: CartanType(['E', 6, 1]).classical()
            ['E', 6]
            sage: CartanType(['F', 4, 1]).classical()
            ['F', 4]
            sage: CartanType(['G', 2, 1]).classical()
            ['G', 2]
        """
    def basic_untwisted(self):
        """
        Return the basic_untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic_untwisted type is `X_n`. In
        other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: CartanType(['A', 1, 1]).basic_untwisted()
            ['A', 1]
            sage: CartanType(['A', 3, 1]).basic_untwisted()
            ['A', 3]
            sage: CartanType(['B', 3, 1]).basic_untwisted()
            ['B', 3]
            sage: CartanType(['E', 6, 1]).basic_untwisted()
            ['E', 6]
            sage: CartanType(['G', 2, 1]).basic_untwisted()
            ['G', 2]
        """
    def is_untwisted_affine(self):
        """
        Implement :meth:`CartanType_affine.is_untwisted_affine` by
        returning ``True``.

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).is_untwisted_affine()
            True
        """

class CartanType_decorator(UniqueRepresentation, SageObject, CartanType_abstract):
    """
    Concrete base class for Cartan types that decorate another Cartan type.
    """
    def __init__(self, ct) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: TestSuite(ct).run()
        """
    def is_irreducible(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.is_irreducible()
            True
        """
    def is_finite(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.is_finite()
            True
        """
    def is_crystallographic(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.is_crystallographic()
            True
        """
    def is_affine(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.is_affine()
            False
        """
    def rank(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.rank()
            2
        """
    def index_set(self):
        """
        EXAMPLES::

           sage: ct = CartanType(['F', 4, 1]).dual()
           sage: ct.index_set()
           (0, 1, 2, 3, 4)
        """

class SuperCartanType_standard(UniqueRepresentation, SageObject):
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: len(CartanType(['A',[4,3]]))
            2
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: t = CartanType(['A', [3,6]])
            sage: t[0]
            'A'
            sage: t[1]
            [3, 6]
            sage: t[2]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """
    options: Incomplete
